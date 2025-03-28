<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-03-27T08:07:32+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "ru"
}
-->
# Кроссплатформенный вывод с использованием Rust

Этот учебник проведет нас через процесс выполнения вывода с использованием Rust и [Candle ML framework](https://github.com/huggingface/candle) от HuggingFace. Использование Rust для вывода предоставляет несколько преимуществ, особенно по сравнению с другими языками программирования. Rust известен своей высокой производительностью, сравнимой с C и C++. Это делает его отличным выбором для задач вывода, которые могут быть вычислительно сложными. Особенно это достигается благодаря абстракциям без дополнительной стоимости и эффективному управлению памятью, без накладных расходов на сборку мусора. Кроссплатформенные возможности Rust позволяют разрабатывать код, который работает на различных операционных системах, включая Windows, macOS и Linux, а также мобильные операционные системы, без значительных изменений в коде.

Предварительным условием для прохождения этого учебника является [установка Rust](https://www.rust-lang.org/tools/install), которая включает компилятор Rust и Cargo, менеджер пакетов Rust.

## Шаг 1: Создание нового проекта на Rust

Чтобы создать новый проект на Rust, выполните следующую команду в терминале:

```bash
cargo new phi-console-app
```

Это создаст начальную структуру проекта с файлами `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`:

```toml
[package]
name = "phi-console-app"
version = "0.1.0"
edition = "2021"

[dependencies]
candle-core = { version = "0.6.0" }
candle-transformers = { version = "0.6.0" }
hf-hub = { version = "0.3.2", features = ["tokio"] }
rand = "0.8"
tokenizers = "0.15.2"
```

## Шаг 2: Настройка базовых параметров

Внутри файла main.rs мы настроим начальные параметры для вывода. Все они будут жестко заданы для простоты, но мы можем изменять их по мере необходимости.

```rust
let temperature: f64 = 1.0;
let sample_len: usize = 100;
let top_p: Option<f64> = None;
let repeat_last_n: usize = 64;
let repeat_penalty: f32 = 1.2;
let mut rng = rand::thread_rng();
let seed: u64 = rng.gen();
let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";
let device = Device::Cpu;
```

- **temperature**: Управляет случайностью процесса выборки.
- **sample_len**: Указывает максимальную длину сгенерированного текста.
- **top_p**: Используется для выборки ядра, чтобы ограничить количество токенов, рассматриваемых на каждом шаге.
- **repeat_last_n**: Управляет количеством токенов, учитываемых для применения штрафа, чтобы избежать повторяющихся последовательностей.
- **repeat_penalty**: Значение штрафа для предотвращения повторяющихся токенов.
- **seed**: Случайное значение (мы можем использовать постоянное значение для лучшей воспроизводимости).
- **prompt**: Исходный текст, чтобы начать генерацию. Обратите внимание, что мы просим модель сгенерировать хокку о хоккее, и оборачиваем его специальными токенами, чтобы указать части разговора пользователя и помощника. Модель завершит запрос хокку.
- **device**: В этом примере мы используем процессор для вычислений. Candle поддерживает выполнение на GPU с использованием CUDA и Metal.

## Шаг 3: Загрузка/Подготовка модели и токенизатора

```rust
let api = hf_hub::api::sync::Api::new()?;
let model_path = api
    .repo(hf_hub::Repo::with_revision(
        "microsoft/Phi-3-mini-4k-instruct-gguf".to_string(),
        hf_hub::RepoType::Model,
        "main".to_string(),
    ))
    .get("Phi-3-mini-4k-instruct-q4.gguf")?;

let tokenizer_path = api
    .model("microsoft/Phi-3-mini-4k-instruct".to_string())
    .get("tokenizer.json")?;
let tokenizer = Tokenizer::from_file(tokenizer_path).map_err(|e| e.to_string())?;
```

Мы используем файл `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` для токенизации нашего входного текста. После загрузки модель кэшируется, поэтому первое выполнение будет медленным (так как загружается 2,4 ГБ модели), но последующие выполнения будут быстрее.

## Шаг 4: Загрузка модели

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Мы загружаем квантованные веса модели в память и инициализируем модель Phi-3. Этот шаг включает чтение весов модели из файла `gguf` и настройку модели для вывода на указанном устройстве (в данном случае CPU).

## Шаг 5: Обработка запроса и подготовка к выводу

```rust
let tokens = tokenizer.encode(prompt, true).map_err(|e| e.to_string())?;
let tokens = tokens.get_ids();
let to_sample = sample_len.saturating_sub(1);
let mut all_tokens = vec![];

let mut logits_processor = LogitsProcessor::new(seed, Some(temperature), top_p);

let mut next_token = *tokens.last().unwrap();
let eos_token = *tokenizer.get_vocab(true).get("").unwrap();
let mut prev_text_len = 0;

for (pos, &token) in tokens.iter().enumerate() {
    let input = Tensor::new(&[token], &device)?.unsqueeze(0)?;
    let logits = model.forward(&input, pos)?;
    let logits = logits.squeeze(0)?;

    if pos == tokens.len() - 1 {
        next_token = logits_processor.sample(&logits)?;
        all_tokens.push(next_token);
    }
}
```

На этом этапе мы токенизируем входной запрос и готовим его для вывода, преобразовывая его в последовательность идентификаторов токенов. Мы также инициализируем значения `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Каждый токен преобразуется в тензор и передается через модель для получения логитов.

Цикл обрабатывает каждый токен в запросе, обновляя процессор логитов и готовя следующий токен для генерации.

## Шаг 6: Вывод

```rust
for index in 0..to_sample {
    let input = Tensor::new(&[next_token], &device)?.unsqueeze(0)?;
    let logits = model.forward(&input, tokens.len() + index)?;
    let logits = logits.squeeze(0)?;
    let logits = if repeat_penalty == 1. {
        logits
    } else {
        let start_at = all_tokens.len().saturating_sub(repeat_last_n);
        candle_transformers::utils::apply_repeat_penalty(
            &logits,
            repeat_penalty,
            &all_tokens[start_at..],
        )?
    };

    next_token = logits_processor.sample(&logits)?;
    all_tokens.push(next_token);

    let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

    if decoded_text.len() > prev_text_len {
        let new_text = &decoded_text[prev_text_len..];
        print!("{new_text}");
        std::io::stdout().flush()?;
        prev_text_len = decoded_text.len();
    }

    if next_token == eos_token {
        break;
    }
}
```

В цикле вывода мы генерируем токены один за другим, пока не достигнем желаемой длины выборки или не встретим токен конца последовательности. Следующий токен преобразуется в тензор и передается через модель, при этом логиты обрабатываются для применения штрафов и выборки. Затем следующий токен выбирается, декодируется и добавляется к последовательности.
Чтобы избежать повторяющегося текста, применяется штраф к повторяющимся токенам на основе параметров `repeat_last_n` and `repeat_penalty`.

Наконец, сгенерированный текст выводится по мере его декодирования, обеспечивая потоковый вывод в реальном времени.

## Шаг 7: Запуск приложения

Чтобы запустить приложение, выполните следующую команду в терминале:

```bash
cargo run --release
```

Это должно вывести хокку о хоккее, сгенерированное моделью Phi-3. Например:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

или

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Заключение

Следуя этим шагам, мы можем выполнить генерацию текста с использованием модели Phi-3, Rust и Candle менее чем в 100 строках кода. Код обрабатывает загрузку модели, токенизацию и вывод, используя тензоры и обработку логитов для генерации связного текста на основе входного запроса.

Это консольное приложение может работать на Windows, Linux и Mac OS. Благодаря портативности Rust, код также может быть адаптирован в библиотеку, которая будет работать внутри мобильных приложений (консольные приложения там запустить нельзя).

## Приложение: полный код

```rust
use candle_core::{quantized::gguf_file, Device, Tensor};
use candle_transformers::{
    generation::LogitsProcessor, models::quantized_phi3::ModelWeights as Phi3,
};
use rand::Rng;
use std::io::Write;
use tokenizers::Tokenizer;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    // 1. configure basic parameters
    let temperature: f64 = 1.0;
    let sample_len: usize = 100;
    let top_p: Option<f64> = None;
    let repeat_last_n: usize = 64;
    let repeat_penalty: f32 = 1.2;
    let mut rng = rand::thread_rng();
    let seed: u64 = rng.gen();
    let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";

    // we will be running on CPU only
    let device = Device::Cpu;

    // 2. download/prepare model and tokenizer
    let api = hf_hub::api::sync::Api::new()?;
    let model_path = api
        .repo(hf_hub::Repo::with_revision(
            "microsoft/Phi-3-mini-4k-instruct-gguf".to_string(),
            hf_hub::RepoType::Model,
            "main".to_string(),
        ))
        .get("Phi-3-mini-4k-instruct-q4.gguf")?;

    let tokenizer_path = api
        .model("microsoft/Phi-3-mini-4k-instruct".to_string())
        .get("tokenizer.json")?;
    let tokenizer = Tokenizer::from_file(tokenizer_path).map_err(|e| e.to_string())?;

    // 3. load model
    let mut file = std::fs::File::open(&model_path)?;
    let model_content = gguf_file::Content::read(&mut file)?;
    let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;

    // 4. process prompt and prepare for inference
    let tokens = tokenizer.encode(prompt, true).map_err(|e| e.to_string())?;
    let tokens = tokens.get_ids();
    let to_sample = sample_len.saturating_sub(1);
    let mut all_tokens = vec![];

    let mut logits_processor = LogitsProcessor::new(seed, Some(temperature), top_p);

    let mut next_token = *tokens.last().unwrap();
    let eos_token = *tokenizer.get_vocab(true).get("<|end|>").unwrap();
    let mut prev_text_len = 0;

    for (pos, &token) in tokens.iter().enumerate() {
        let input = Tensor::new(&[token], &device)?.unsqueeze(0)?;
        let logits = model.forward(&input, pos)?;
        let logits = logits.squeeze(0)?;

        // Sample next token only for the last token in the prompt
        if pos == tokens.len() - 1 {
            next_token = logits_processor.sample(&logits)?;
            all_tokens.push(next_token);
        }
    }

    // 5. inference
    for index in 0..to_sample {
        let input = Tensor::new(&[next_token], &device)?.unsqueeze(0)?;
        let logits = model.forward(&input, tokens.len() + index)?;
        let logits = logits.squeeze(0)?;
        let logits = if repeat_penalty == 1. {
            logits
        } else {
            let start_at = all_tokens.len().saturating_sub(repeat_last_n);
            candle_transformers::utils::apply_repeat_penalty(
                &logits,
                repeat_penalty,
                &all_tokens[start_at..],
            )?
        };

        next_token = logits_processor.sample(&logits)?;
        all_tokens.push(next_token);

        // decode the current sequence of tokens
        let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

        // only print the new part of the decoded text
        if decoded_text.len() > prev_text_len {
            let new_text = &decoded_text[prev_text_len..];
            print!("{new_text}");
            std::io::stdout().flush()?;
            prev_text_len = decoded_text.len();
        }

        if next_token == eos_token {
            break;
        }
    }

    Ok(())
}
```

Примечание: чтобы запустить этот код на aarch64 Linux или aarch64 Windows, добавьте файл с именем `.cargo/config` со следующим содержимым:

```toml
[target.aarch64-pc-windows-msvc]
rustflags = [
    "-C", "target-feature=+fp16"
]

[target.aarch64-unknown-linux-gnu]
rustflags = [
    "-C", "target-feature=+fp16"
]
```

> Вы можете посетить официальный репозиторий [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) для получения дополнительных примеров использования модели Phi-3 с Rust и Candle, включая альтернативные подходы к выводу.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.