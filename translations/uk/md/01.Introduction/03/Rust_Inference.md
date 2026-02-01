# Кросплатформене виконання висновків з Rust

Цей посібник проведе нас через процес виконання висновків за допомогою Rust та [Candle ML framework](https://github.com/huggingface/candle) від HuggingFace. Використання Rust для виконання висновків має кілька переваг, особливо у порівнянні з іншими мовами програмування. Rust відомий своєю високою продуктивністю, порівнянною з C та C++. Це робить його відмінним вибором для завдань висновку, які можуть бути обчислювально інтенсивними. Зокрема, це забезпечується абстракціями без додаткових витрат та ефективним управлінням пам’яттю без накладних витрат на збір сміття. Кросплатформені можливості Rust дозволяють розробляти код, який працюватиме на різних операційних системах, включно з Windows, macOS та Linux, а також мобільних ОС, без значних змін у кодовій базі.

Передумовою для проходження цього посібника є [встановлення Rust](https://www.rust-lang.org/tools/install), що включає компілятор Rust та Cargo — менеджер пакетів Rust.

## Крок 1: Створення нового Rust-проєкту

Щоб створити новий Rust-проєкт, виконайте наступну команду в терміналі:

```bash
cargo new phi-console-app
```

Це створить початкову структуру проєкту з файлом `Cargo.toml` та директорією `src`, що містить файл `main.rs`.

Далі додамо наші залежності — а саме crates `candle`, `hf-hub` та `tokenizers` — у файл `Cargo.toml`:

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

## Крок 2: Налаштування базових параметрів

У файлі main.rs ми встановимо початкові параметри для нашого висновку. Вони будуть жорстко закодовані для простоти, але ми можемо змінювати їх за потреби.

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

- **temperature**: Керує випадковістю процесу вибірки.
- **sample_len**: Визначає максимальну довжину згенерованого тексту.
- **top_p**: Використовується для nucleus sampling, щоб обмежити кількість токенів, які розглядаються на кожному кроці.
- **repeat_last_n**: Керує кількістю токенів, які враховуються для застосування штрафу, щоб уникнути повторюваних послідовностей.
- **repeat_penalty**: Значення штрафу для запобігання повторенню токенів.
- **seed**: Випадкове зерно (можна використовувати константне значення для кращої відтворюваності).
- **prompt**: Початковий текст підказки для запуску генерації. Зверніть увагу, що ми просимо модель згенерувати хайку про хокей на льоду, і обгортаємо його спеціальними токенами, щоб позначити частини розмови користувача та асистента. Модель потім доповнить підказку хайку.
- **device**: У цьому прикладі ми використовуємо CPU для обчислень. Candle також підтримує запуск на GPU з CUDA та Metal.

## Крок 3: Завантаження/підготовка моделі та токенізатора

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

Ми використовуємо API `hf_hub` для завантаження файлів моделі та токенізатора з Hugging Face model hub. Файл `gguf` містить квантизовані ваги моделі, а файл `tokenizer.json` використовується для токенізації вхідного тексту. Після завантаження модель кешується, тому перше виконання буде повільним (оскільки завантажується 2.4 ГБ моделі), але наступні виконання будуть швидшими.

## Крок 4: Завантаження моделі

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Ми завантажуємо квантизовані ваги моделі в пам’ять та ініціалізуємо модель Phi-3. Цей крок включає читання ваг моделі з файлу `gguf` та налаштування моделі для виконання висновку на вказаному пристрої (у цьому випадку CPU).

## Крок 5: Обробка підказки та підготовка до висновку

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

На цьому кроці ми токенізуємо вхідну підказку та готуємо її для висновку, перетворюючи у послідовність ID токенів. Також ініціалізуємо `LogitsProcessor` для керування процесом вибірки (розподіл ймовірностей по словнику) на основі заданих значень `temperature` та `top_p`. Кожен токен перетворюється у тензор і пропускається через модель для отримання логітів.

Цикл обробляє кожен токен у підказці, оновлюючи логіт-процесор і готуючись до генерації наступного токена.

## Крок 6: Виконання висновку

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

У циклі висновку ми генеруємо токени по одному, доки не досягнемо бажаної довжини зразка або не зустрінемо токен кінця послідовності. Наступний токен перетворюється у тензор і пропускається через модель, а логіти обробляються для застосування штрафів і вибірки. Потім наступний токен вибирається, декодується і додається до послідовності.  
Щоб уникнути повторюваного тексту, застосовується штраф до повторюваних токенів на основі параметрів `repeat_last_n` та `repeat_penalty`.

Нарешті, згенерований текст виводиться по мірі декодування, забезпечуючи потоковий вивід у реальному часі.

## Крок 7: Запуск додатку

Щоб запустити додаток, виконайте наступну команду в терміналі:

```bash
cargo run --release
```

Це має вивести хайку про хокей на льоду, згенероване моделлю Phi-3. Щось на кшталт:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

або

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Висновок

Дотримуючись цих кроків, ми можемо виконувати генерацію тексту за допомогою моделі Phi-3 з Rust та Candle менш ніж у 100 рядках коду. Код обробляє завантаження моделі, токенізацію та висновок, використовуючи тензори та обробку логітів для генерації зв’язного тексту на основі вхідної підказки.

Цей консольний додаток може працювати на Windows, Linux та Mac OS. Завдяки портативності Rust, код також можна адаптувати до бібліотеки, яка працюватиме всередині мобільних додатків (адже консольні додатки там запускати не можна).

## Додаток: повний код

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

Примітка: щоб запустити цей код на aarch64 Linux або aarch64 Windows, додайте файл з назвою `.cargo/config` з таким вмістом:

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

> Ви можете відвідати офіційний репозиторій [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) для отримання додаткових прикладів використання моделі Phi-3 з Rust та Candle, включно з альтернативними підходами до виконання висновків.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.