# Крос-платформско извођење инференце са Rust-ом

Овај туторијал ће нас провести кроз процес извођења инференце користећи Rust и [Candle ML framework](https://github.com/huggingface/candle) из HuggingFace-а. Коришћење Rust-а за инференцу нуди неколико предности, посебно у поређењу са другим програмским језицима. Rust је познат по високом перформансу, упоредивом са C и C++. То га чини одличним избором за задатке инференце, који могу бити рачунски захтевни. Ово је посебно омогућено захваљујући zero-cost апстракцијама и ефикасном управљању меморијом, без оптерећења garbage collection-а. Rust-ове крос-платформске могућности омогућавају развој кода који ради на различитим оперативним системима, укључујући Windows, macOS и Linux, као и мобилним оперативним системима, без значајних измена у коду.

Претпоставка за праћење овог туторијала је да [инсталирате Rust](https://www.rust-lang.org/tools/install), који укључује Rust компајлер и Cargo, Rust пакет менаџер.

## Корак 1: Креирање новог Rust пројекта

Да бисте креирали нови Rust пројекат, покрените следећу команду у терминалу:

```bash
cargo new phi-console-app
```

Ово генерише почетну структуру пројекта са `Cargo.toml` фајлом и `src` директоријумом који садржи `main.rs` фајл.

Затим ћемо додати наше зависности - односно `candle`, `hf-hub` и `tokenizers` crates - у `Cargo.toml` фајл:

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

## Корак 2: Конфигурисање основних параметара

Унутар `main.rs` фајла, подешавамо почетне параметре за нашу инференцу. Сви ће бити хардкодирани ради једноставности, али их можемо по потреби мењати.

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

- **temperature**: Контролише насумичност процеса узорковања.
- **sample_len**: Одређује максималну дужину генерисаног текста.
- **top_p**: Користи се за nucleus sampling да ограничи број токена који се разматрају у сваком кораку.
- **repeat_last_n**: Контролише број токена који се узимају у обзир за примену казне како би се спречиле понављајуће секвенце.
- **repeat_penalty**: Вредност казне која одвраћа од понављања истих токена.
- **seed**: Насумични seed (можемо користити константну вредност ради боље репродуктивности).
- **prompt**: Почетни текст који покреће генерисање. Обратите пажњу да тражимо од модела да генерише хајку о хокеју на леду, и да га обавијамо посебним токенима који означавају делове разговора корисника и асистента. Модел ће затим допунити prompt хајком.
- **device**: У овом примеру користимо CPU за израчунавање. Candle подржава и рад на GPU-у са CUDA и Metal.

## Корак 3: Преузимање/припрема модела и токенизера

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

Користимо `hf_hub` API за преузимање модела и фајлова токенизера са Hugging Face model hub-а. `gguf` фајл садржи квантоване тежине модела, док се `tokenizer.json` користи за токенизацију улазног текста. Након преузимања, модел се кешира, тако да ће прво извршење бити спорије (јер се преузима 2.4GB модела), али ће наредна извршења бити бржа.

## Корак 4: Учитавање модела

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Учитавају се квантоване тежине модела у меморију и иницијализује Phi-3 модел. Овај корак подразумева читање тежина из `gguf` фајла и подешавање модела за инференцу на одређеном уређају (у овом случају CPU).

## Корак 5: Обрада prompt-а и припрема за инференцу

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

У овом кораку токенизујемо улазни prompt и припремамо га за инференцу претварањем у низ ID-јева токена. Такође иницијализујемо `LogitsProcessor` који управља процесом узорковања (вероватноћна дистрибуција преко вокабулара) на основу задатих вредности `temperature` и `top_p`. Сваки токен се претвара у тензор и пролази кроз модел да би се добили логити.

Лупа обрађује сваки токен у prompt-у, ажурирајући logits processor и припремајући се за генерисање следећег токена.

## Корак 6: Инференца

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

У лупи инференце генеришемо токене један по један док не достигнемо жељену дужину узорка или док не наиђемо на end-of-sequence токен. Следећи токен се претвара у тензор и пролази кроз модел, док се логити обрађују да би се примениле казне и узорковање. Затим се следећи токен узоркује, декодира и додаје у низ.
Да би се избегло понављање текста, примењује се казна на понављајуће токене на основу параметара `repeat_last_n` и `repeat_penalty`.

На крају, генерисани текст се исписује како се декодира, обезбеђујући стриминг у реалном времену.

## Корак 7: Покретање апликације

Да бисте покренули апликацију, извршите следећу команду у терминалу:

```bash
cargo run --release
```

Ово би требало да испише хајку о хокеју на леду коју је генерисао Phi-3 модел. Нешто попут:

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

## Закључак

Пратећи ове кораке, можемо извршити генерисање текста користећи Phi-3 модел са Rust-ом и Candle-ом у мање од 100 линија кода. Код обрађује учитавање модела, токенизацију и инференцу, користећи тензоре и обраду логита да генерише кохерентан текст на основу улазног prompt-а.

Ова конзолна апликација може да ради на Windows-у, Linux-у и Mac OS-у. Због преносивости Rust-а, код се може прилагодити и као библиотека која би радила унутар мобилних апликација (јер конзолне апликације тамо не можемо покретати).

## Додатак: цео код

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

Напомена: да бисте покренули овај код на aarch64 Linux-у или aarch64 Windows-у, додајте фајл под именом `.cargo/config` са следећим садржајем:

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

> Можете посетити званични [Candle примери](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) репозиторијум за више примера како користити Phi-3 модел са Rust-ом и Candle-ом, укључујући и алтернативне приступе инференци.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.