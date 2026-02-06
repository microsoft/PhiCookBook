# Cross-platform inference gamit ang Rust

Ang tutorial na ito ay gagabay sa atin sa proseso ng paggawa ng inference gamit ang Rust at ang [Candle ML framework](https://github.com/huggingface/candle) mula sa HuggingFace. Ang paggamit ng Rust para sa inference ay may ilang mga benepisyo, lalo na kung ikukumpara sa ibang mga programming language. Kilala ang Rust sa mataas nitong performance, na katulad ng sa C at C++. Dahil dito, ito ay isang mahusay na pagpipilian para sa mga inference task na maaaring maging mabigat sa computation. Partikular, ito ay dahil sa zero-cost abstractions at mahusay na pamamahala ng memorya na walang overhead ng garbage collection. Ang kakayahan ng Rust na tumakbo sa iba't ibang platform ay nagpapahintulot sa pag-develop ng code na maaaring patakbuhin sa iba't ibang operating system, kabilang ang Windows, macOS, at Linux, pati na rin sa mga mobile operating system, nang hindi na kailangang baguhin nang malaki ang codebase.

Ang kinakailangan upang sundan ang tutorial na ito ay ang [pag-install ng Rust](https://www.rust-lang.org/tools/install), na kasama ang Rust compiler at Cargo, ang package manager ng Rust.

## Hakbang 1: Gumawa ng Bagong Rust Project

Para gumawa ng bagong Rust project, patakbuhin ang sumusunod na utos sa terminal:

```bash
cargo new phi-console-app
```

Ito ay gagawa ng panimulang istruktura ng proyekto na may `Cargo.toml` na file at isang `src` na direktoryo na naglalaman ng `main.rs` na file.

Susunod, idaragdag natin ang ating mga dependencies - ang `candle`, `hf-hub` at `tokenizers` crates - sa `Cargo.toml` na file:

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

## Hakbang 2: I-configure ang Mga Pangunahing Parameter

Sa loob ng main.rs na file, ise-set up natin ang mga panimulang parameter para sa ating inference. Lahat ng ito ay hardcoded para sa pagiging simple, ngunit maaari natin itong baguhin kung kinakailangan.

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

- **temperature**: Kinokontrol ang randomness ng proseso ng sampling.
- **sample_len**: Tinutukoy ang pinakamahabang haba ng generated na teksto.
- **top_p**: Ginagamit para sa nucleus sampling upang limitahan ang bilang ng mga token na isasaalang-alang sa bawat hakbang.
- **repeat_last_n**: Kinokontrol ang bilang ng mga token na isasaalang-alang para sa paglalapat ng penalty upang maiwasan ang paulit-ulit na mga sequence.
- **repeat_penalty**: Ang halaga ng penalty para hindi maulit ang mga token.
- **seed**: Isang random seed (maaari tayong gumamit ng constant na halaga para sa mas magandang reproducibility).
- **prompt**: Ang panimulang teksto para simulan ang generation. Pansinin na hinihiling natin sa modelo na gumawa ng haiku tungkol sa ice hockey, at nilalagyan natin ito ng espesyal na mga token upang ipakita ang bahagi ng user at assistant sa pag-uusap. Pagkatapos ay tatapusin ng modelo ang prompt gamit ang isang haiku.
- **device**: Ginagamit natin ang CPU para sa computation sa halimbawang ito. Sinusuportahan din ng Candle ang pagpapatakbo sa GPU gamit ang CUDA at Metal.

## Hakbang 3: I-download/Ihanda ang Modelo at Tokenizer

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

Ginagamit natin ang `hf_hub` API para i-download ang mga file ng modelo at tokenizer mula sa Hugging Face model hub. Ang `gguf` na file ay naglalaman ng quantized na timbang ng modelo, habang ang `tokenizer.json` na file ay ginagamit para sa pag-tokenize ng ating input na teksto. Kapag na-download na, naka-cache ang modelo, kaya ang unang pagtakbo ay magiging mabagal (dahil ida-download ang 2.4GB na modelo) ngunit ang mga susunod na pagtakbo ay magiging mas mabilis.

## Hakbang 4: I-load ang Modelo

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Ilo-load natin ang quantized na timbang ng modelo sa memorya at i-initialize ang Phi-3 na modelo. Kasama sa hakbang na ito ang pagbabasa ng timbang ng modelo mula sa `gguf` na file at pagsasaayos ng modelo para sa inference sa tinukoy na device (CPU sa kasong ito).

## Hakbang 5: Iproseso ang Prompt at Ihanda para sa Inference

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

Sa hakbang na ito, ita-tokenize natin ang input prompt at ihahanda ito para sa inference sa pamamagitan ng pag-convert nito sa isang sequence ng token IDs. I-initialize din natin ang `LogitsProcessor` para hawakan ang proseso ng sampling (probability distribution sa vocabulary) base sa ibinigay na `temperature` at `top_p` na mga halaga. Bawat token ay iko-convert sa tensor at ipapasa sa modelo upang makuha ang logits.

Pinoproseso ng loop ang bawat token sa prompt, ina-update ang logits processor at inihahanda ang susunod na token para sa generation.

## Hakbang 6: Inference

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

Sa inference loop, bumubuo tayo ng mga token isa-isa hanggang maabot ang nais na sample length o matagpuan ang end-of-sequence token. Ang susunod na token ay iko-convert sa tensor at ipapasa sa modelo, habang pinoproseso ang logits para mag-apply ng mga penalty at sampling. Pagkatapos, ang susunod na token ay isinasample, dine-decode, at idinadagdag sa sequence.  
Upang maiwasan ang paulit-ulit na teksto, naglalapat ng penalty sa mga paulit-ulit na token base sa `repeat_last_n` at `repeat_penalty` na mga parameter.

Sa huli, ang nabuo na teksto ay ipi-print habang dine-decode, na nagbibigay ng streamed na real-time output.

## Hakbang 7: Patakbuhin ang Aplikasyon

Para patakbuhin ang aplikasyon, isagawa ang sumusunod na utos sa terminal:

```bash
cargo run --release
```

Dapat itong mag-print ng isang haiku tungkol sa ice hockey na ginawa ng Phi-3 na modelo. Halimbawa:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

o kaya

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Konklusyon

Sa pagsunod sa mga hakbang na ito, maaari tayong gumawa ng text generation gamit ang Phi-3 na modelo gamit ang Rust at Candle sa loob ng mas mababa sa 100 linya ng code. Pinangangasiwaan ng code ang pag-load ng modelo, tokenization, at inference, gamit ang tensors at logits processing upang makabuo ng magkakaugnay na teksto base sa input prompt.

Ang console application na ito ay maaaring patakbuhin sa Windows, Linux, at Mac OS. Dahil sa portability ng Rust, maaari ring i-adapt ang code bilang isang library na tatakbo sa loob ng mga mobile app (hindi kasi pwedeng magpatakbo ng console apps doon).

## Apendise: buong code

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

Tandaan: para mapatakbo ang code na ito sa aarch64 Linux o aarch64 Windows, magdagdag ng file na pinangalanang `.cargo/config` na may sumusunod na nilalaman:

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

> Maaari mong bisitahin ang opisyal na [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository para sa iba pang mga halimbawa kung paano gamitin ang Phi-3 na modelo gamit ang Rust at Candle, kabilang ang mga alternatibong paraan ng inference.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.