<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2fa1ead890e358cc560ed4f9b3cf219a",
  "translation_date": "2025-04-04T12:09:34+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "mo"
}
-->
# Rust-ով բազմապլատֆորմ ինֆերենս

Այս ձեռնարկը մեզ կուղեկցի Rust-ի և HuggingFace-ի [Candle ML framework](https://github.com/huggingface/candle)-ի միջոցով ինֆերենս կատարելու գործընթացով։ Rust-ը ինֆերենսի համար առաջարկում է մի շարք առավելություններ, հատկապես՝ համեմատած այլ ծրագրավորման լեզուների հետ։ Rust-ը հայտնի է իր բարձր արդյունավետությամբ, որը համեմատելի է C-ի և C++-ի հետ։ Սա այն դարձնում է հիանալի ընտրություն՝ հաշվողականորեն ծանրաբեռնված ինֆերենսի առաջադրանքների համար։ Սա հատկապես պայմանավորված է զրոյական արժեք ունեցող աբստրակցիաներով և արդյունավետ հիշողության կառավարմամբ, որը չունի աղբահանության ավելորդ ծախսեր։ Rust-ի բազմապլատֆորմ հնարավորությունները թույլ են տալիս մշակել կոդ, որը կարող է աշխատել տարբեր օպերացիոն համակարգերում՝ ներառյալ Windows, macOS և Linux, ինչպես նաև բջջային օպերացիոն համակարգերում՝ առանց կոդի բազային էական փոփոխությունների։

Այս ձեռնարկը հետևելու համար նախապայման է [տեղադրել Rust](https://www.rust-lang.org/tools/install), որը ներառում է Rust կոմպիլյատորը և Cargo փաթեթների կառավարիչը։

## Քայլ 1: Ստեղծել նոր Rust նախագիծ

Նոր Rust նախագիծ ստեղծելու համար տերմինալում կատարեք հետևյալ հրամանը․

```bash
cargo new phi-console-app
```

Սա կստեղծի նախնական նախագծի կառուցվածք՝ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ֆայլով․

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

## Քայլ 2: Հիմնական պարամետրերի կարգավորում

`main.rs` ֆայլում մենք կկարգավորենք ինֆերենսի նախնական պարամետրերը։ Դրանք բոլորը կկոդավորվեն պարզության համար, սակայն հնարավոր է փոխել ըստ անհրաժեշտության։

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

- **temperature**: Կառավարում է նմուշառման գործընթացի պատահականությունը։
- **sample_len**: Սահմանում է գեներացված տեքստի առավելագույն երկարությունը։
- **top_p**: Օգտագործվում է նուկլեուսի նմուշառման համար՝ սահմանափակելու յուրաքանչյուր քայլի համար դիտարկվող տոքենների քանակը։
- **repeat_last_n**: Կառավարում է այն տոքենների քանակը, որոնք հաշվի են առնվում կրկնվող հաջորդականությունների կանխարգելման համար։
- **repeat_penalty**: Արժեք, որը խրախուսում է չկրկնվող տոքենների օգտագործումը։
- **seed**: Պատահական սերմ (կարող ենք օգտագործել հաստատուն արժեք՝ վերարտադրելիության համար)։
- **prompt**: Սկզբնական տեքստը, որով սկսվում է գեներացիան։ Ուշադրություն դարձրեք, որ մենք խնդրում ենք մոդելին ստեղծել հոկեյի մասին հայկու և այն փաթաթում ենք հատուկ տոքեններով՝ նշելու համար զրույցի օգտագործողի և օգնականի հատվածները։ Մոդելը կավարտի հուշումը՝ հայկուով։
- **device**: Այս օրինակում մենք օգտագործում ենք CPU հաշվարկի համար։ Candle-ը աջակցում է GPU-ի օգտագործմանը CUDA-ի և Metal-ի հետ։

## Քայլ 3: Ներբեռնել/Պատրաստել Մոդել և Տոքենիզատոր

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

Մենք օգտագործում ենք `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` ֆայլը՝ մեր մուտքային տեքստը տոքենիզացնելու համար։ Ներբեռնելուց հետո մոդելը քեշավորվում է, այնպես որ առաջին գործարկումը դանդաղ կլինի (քանի որ ներբեռնում է մոդելի 2.4 ԳԲ), բայց հաջորդ գործարկումները կլինեն ավելի արագ։

## Քայլ 4: Մոդելի բեռնում

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Մենք բեռնում ենք քվանտացված մոդելի կշիռները հիշողության մեջ և նախաձեռնում Phi-3 մոդելը։ Այս քայլը ներառում է կշիռների ընթերցում `gguf` ֆայլից և մոդելի նախապատրաստում ինֆերենսի համար նշված սարքում (այս դեպքում՝ CPU)։

## Քայլ 5: Հուշման մշակումը և ինֆերենսի նախապատրաստումը

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

Այս քայլում մենք տոքենիզացնում ենք մուտքային հուշումը և պատրաստում այն ինֆերենսի համար՝ վերածելով այն տոքեն ID-ների հաջորդականության։ Մենք նաև նախաձեռնում ենք `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` արժեքները։ Յուրաքանչյուր տոքեն վերածվում է տենսորի և փոխանցվում մոդելին՝ լոգիտներ ստանալու համար։

Ցիկլը մշակում է հուշման յուրաքանչյուր տոքեն՝ թարմացնելով լոգիտների պրոցեսորը և նախապատրաստվելով հաջորդ տոքենի գեներացիային։

## Քայլ 6: Ինֆերենս

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

Ինֆերենսի ցիկլում մենք գեներացնում ենք տոքենները մեկը մյուսի հետևից, մինչև հասնենք ցանկալի նմուշի երկարությանը կամ հանդիպենք հաջորդականության ավարտի տոքենին։ Հաջորդ տոքենը վերածվում է տենսորի և փոխանցվում մոդելին, իսկ լոգիտները մշակվում են՝ կիրառելու պատիժներ և նմուշառում։ Այնուհետև հաջորդ տոքենը նմուշառվում է, դեկոդավորվում և կցվում հաջորդականությանը։  
Կրկնվող տեքստից խուսափելու համար պատիժ է կիրառվում կրկնվող տոքենների վրա՝ հիմնվելով `repeat_last_n` and `repeat_penalty` պարամետրերի վրա։

Վերջում գեներացված տեքստը տպվում է՝ դեկոդավորվելով, ապահովելով իրական ժամանակում հոսքային արդյունք։

## Քայլ 7: Ծրագրի գործարկում

Ծրագիրը գործարկելու համար տերմինալում կատարեք հետևյալ հրամանը․

```bash
cargo run --release
```

Սա պետք է տպի հոկեյի մասին հայկու, որը գեներացված է Phi-3 մոդելի կողմից։ Ինչ-որ բան այսպիսի․

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

կամ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Եզրակացություն

Այս քայլերին հետևելով՝ մենք կարող ենք կատարել տեքստի գեներացիա Phi-3 մոդելի միջոցով Rust-ի և Candle-ի օգնությամբ՝ 100 տողից պակաս կոդով։ Կոդը կատարում է մոդելի բեռնում, տոքենիզացում և ինֆերենս՝ օգտագործելով տենսորներ և լոգիտների մշակում՝ գեներացնելու համահունչ տեքստ՝ հիմնված մուտքային հուշման վրա։

Այս կոնսոլային ծրագիրը կարող է աշխատել Windows, Linux և Mac OS-ում։ Rust-ի շարժունակության շնորհիվ կոդը կարող է նաև հարմարեցվել գրադարանի, որը կաշխատի բջջային հավելվածներում (չէ որ մենք չենք կարող կոնսոլային հավելվածներ աշխատեցնել այնտեղ)։

## Հավելված․ ամբողջական կոդ

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

Նշում. aarch64 Linux կամ aarch64 Windows-ում այս կոդը աշխատեցնելու համար ավելացրեք `.cargo/config` անունով ֆայլ հետևյալ պարունակությամբ․

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

> Կարող եք այցելել պաշտոնական [Candle օրինակների](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ռեպոզիտորիան՝ Rust-ի և Candle-ի միջոցով Phi-3 մոդելի օգտագործման այլ օրինակների համար, ներառյալ ինֆերենսի այլընտրանքային մոտեցումները։

It seems you've requested a translation to "mo." Could you please clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, is it Maori, Montenegrin, or something else? Let me know, and I'll assist you accordingly!