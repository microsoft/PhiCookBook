<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:33:49+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "bg"
}
-->
# Кросплатформено извеждане с Rust

Този урок ще ни преведе през процеса на извеждане с Rust и [Candle ML framework](https://github.com/huggingface/candle) от HuggingFace. Използването на Rust за извеждане предлага няколко предимства, особено в сравнение с други програмни езици. Rust е известен с високата си производителност, сравнима с тази на C и C++. Това го прави отличен избор за задачи по извеждане, които могат да бъдат изчислително интензивни. Особено това се дължи на абстракциите без допълнителни разходи и ефективното управление на паметта, което няма натоварване от garbage collection. Кросплатформените възможности на Rust позволяват разработка на код, който работи на различни операционни системи, включително Windows, macOS и Linux, както и мобилни операционни системи, без значителни промени в кода.

Предварителното условие за следване на този урок е да [инсталирате Rust](https://www.rust-lang.org/tools/install), което включва Rust компилатора и Cargo, пакетния мениджър на Rust.

## Стъпка 1: Създаване на нов Rust проект

За да създадете нов Rust проект, изпълнете следната команда в терминала:

```bash
cargo new phi-console-app
```

Това генерира начална структура на проекта с файл `Cargo.toml` и директория `src`, съдържаща файл `main.rs`.

След това ще добавим нашите зависимости - а именно `candle`, `hf-hub` и `tokenizers` crates - към файла `Cargo.toml`:

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

## Стъпка 2: Конфигуриране на основни параметри

Във файла main.rs ще зададем началните параметри за извеждането. Те ще бъдат твърдо кодирани за опростяване, но можем да ги променяме при нужда.

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

- **temperature**: Контролира случайността при извадката.
- **sample_len**: Определя максималната дължина на генерирания текст.
- **top_p**: Използва се за nucleus sampling, за да ограничи броя на токените, разглеждани на всяка стъпка.
- **repeat_last_n**: Контролира броя на токените, разглеждани за прилагане на наказание с цел предотвратяване на повтарящи се последователности.
- **repeat_penalty**: Стойността на наказанието за повторени токени.
- **seed**: Случаен seed (можем да използваме константна стойност за по-добра възпроизводимост).
- **prompt**: Началният текст за стартиране на генерирането. Забележете, че молим модела да генерира хайку за хокей на лед и го обграждаме със специални токени, за да обозначим частите на потребителя и асистента в разговора. Моделът след това ще допълни подканата с хайку.
- **device**: В този пример използваме CPU за изчисления. Candle поддържа изпълнение и на GPU с CUDA и Metal.

## Стъпка 3: Изтегляне/Подготовка на модела и токенизатора

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

Използваме API-то на `hf_hub`, за да изтеглим файловете на модела и токенизатора от Hugging Face model hub. Файлът `gguf` съдържа квантизираните тегла на модела, а файлът `tokenizer.json` се използва за токенизиране на входния текст. След като бъдат изтеглени, моделът се кешира, така че първото изпълнение ще бъде бавно (тъй като изтегля 2.4GB от модела), но следващите изпълнения ще са по-бързи.

## Стъпка 4: Зареждане на модела

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Зареждаме квантизираните тегла на модела в паметта и инициализираме модела Phi-3. Тази стъпка включва четене на теглата от файла `gguf` и настройване на модела за извеждане на посоченото устройство (в случая CPU).

## Стъпка 5: Обработка на подканата и подготовка за извеждане

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

В тази стъпка токенизираме входната подканa и я подготвяме за извеждане, като я преобразуваме в последователност от ID-та на токени. Също така инициализираме `LogitsProcessor`, който управлява процеса на извадка (разпределение на вероятностите върху речника) на базата на зададените стойности за `temperature` и `top_p`. Всеки токен се преобразува в тензор и се подава през модела, за да се получат логитите.

Цикълът обработва всеки токен от подканата, обновявайки логит процесора и подготвяйки се за генериране на следващия токен.

## Стъпка 6: Извеждане

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

В цикъла за извеждане генерираме токени един по един, докато достигнем желаната дължина на извадката или срещнем токена за край на последователността. Следващият токен се преобразува в тензор и се подава през модела, докато логитите се обработват за прилагане на наказания и извадка. След това следващият токен се избира, декодира и добавя към последователността.
За да избегнем повтарящ се текст, се прилага наказание на повторените токени според параметрите `repeat_last_n` и `repeat_penalty`.

Накрая генерираният текст се отпечатва в реално време, осигурявайки потоково изходно съдържание.

## Стъпка 7: Стартиране на приложението

За да стартирате приложението, изпълнете следната команда в терминала:

```bash
cargo run --release
```

Това трябва да отпечата хайку за хокей на лед, генерирано от модела Phi-3. Нещо като:

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

Следвайки тези стъпки, можем да извършим генериране на текст с модела Phi-3, използвайки Rust и Candle с по-малко от 100 реда код. Кодът се грижи за зареждането на модела, токенизацията и извеждането, използвайки тензори и обработка на логити за генериране на свързан текст на базата на входната подканa.

Това конзолно приложение може да работи на Windows, Linux и Mac OS. Благодарение на преносимостта на Rust, кодът може да бъде адаптиран и като библиотека, която да работи в мобилни приложения (в крайна сметка не можем да стартираме конзолни приложения там).

## Приложение: пълен код

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

Забележка: за да стартирате този код на aarch64 Linux или aarch64 Windows, добавете файл с име `.cargo/config` със следното съдържание:

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

> Можете да посетите официалното [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) хранилище за още примери как да използвате модела Phi-3 с Rust и Candle, включително алтернативни подходи за извеждане.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.