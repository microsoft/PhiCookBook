<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:04:15+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "tl"
}
-->
# Cross-platform inference with Rust

Ang tutorial na ito ay gagabay sa atin sa proseso ng paggawa ng inference gamit ang Rust at ang [Candle ML framework](https://github.com/huggingface/candle) mula sa HuggingFace. Ang paggamit ng Rust para sa inference ay may ilang mga benepisyo, lalo na kung ikukumpara sa ibang mga programming language. Kilala ang Rust sa mataas nitong performance, na katulad ng C at C++. Kaya ito ay magandang pagpipilian para sa mga inference tasks na kadalasang mabigat sa computation. Partikular, ito ay dahil sa zero-cost abstractions at epektibong pamamahala ng memorya na walang overhead ng garbage collection. Ang kakayahan ng Rust na tumakbo sa iba't ibang platform ay nagpapahintulot sa pag-develop ng code na maaaring patakbuhin sa iba't ibang operating system tulad ng Windows, macOS, at Linux, pati na rin sa mga mobile operating system, nang hindi na kailangang baguhin nang malaki ang codebase.

Ang kinakailangan upang masundan ang tutorial na ito ay ang [pag-install ng Rust](https://www.rust-lang.org/tools/install), na kasama ang Rust compiler at Cargo, ang package manager ng Rust.

## Step 1: Create a New Rust Project

Para gumawa ng bagong Rust project, patakbuhin ang sumusunod na command sa terminal:

```bash
cargo new phi-console-app
```

Ito ay gagawa ng panimulang project structure na may `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` file:

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

## Step 2: Configure Basic Parameters

Sa loob ng main.rs file, iseset natin ang mga panimulang parameter para sa ating inference. Lahat ng ito ay hardcoded para sa pagiging simple, pero pwede natin itong baguhin kung kinakailangan.

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

- **temperature**: Kinokontrol ang randomness ng sampling process.
- **sample_len**: Tinutukoy ang maximum na haba ng generated na teksto.
- **top_p**: Ginagamit sa nucleus sampling para limitahan ang bilang ng tokens na isasaalang-alang sa bawat hakbang.
- **repeat_last_n**: Kinokontrol ang bilang ng tokens na isinaalang-alang para maglagay ng penalty upang maiwasan ang paulit-ulit na mga sequence.
- **repeat_penalty**: Ang penalty value para hindi maulit-ulit ang mga tokens.
- **seed**: Isang random seed (pwede rin gumamit ng constant value para mas reproducible).
- **prompt**: Ang panimulang prompt na teksto para simulan ang generation. Pansinin na hinihiling natin sa model na gumawa ng haiku tungkol sa ice hockey, at nilalagyan natin ito ng special tokens para ipakita ang bahagi ng user at assistant sa pag-uusap. Pagkatapos, kukumpletuhin ng model ang prompt ng isang haiku.
- **device**: Ginagamit natin ang CPU para sa computation sa halimbawang ito. Sinusuportahan din ng Candle ang pagpapatakbo sa GPU gamit ang CUDA at Metal.

## Step 3: Download/Prepare Model and Tokenizer

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

Ginagamit natin ang `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` file para i-tokenize ang input na teksto. Kapag na-download na, naka-cache na ang model, kaya ang unang pagtakbo ay mabagal (dahil idi-download ang 2.4GB na model) pero mas mabilis na ang mga susunod na pagtakbo.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Ini-load natin ang quantized model weights sa memorya at ini-initialize ang Phi-3 model. Kabilang dito ang pagbabasa ng model weights mula sa `gguf` file at pag-setup ng model para sa inference sa napiling device (CPU sa kasong ito).

## Step 5: Process Prompt and Prepare for Inference

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

Sa hakbang na ito, kino-convert natin ang input prompt sa tokens at inihahanda ito para sa inference sa pamamagitan ng pag-convert sa sequence ng token IDs. Ini-initialize din natin ang `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` values. Bawat token ay kino-convert sa tensor at pinapasa sa model para makuha ang logits.

Ang loop ay pinoproseso ang bawat token sa prompt, ina-update ang logits processor, at inihahanda para sa susunod na token generation.

## Step 6: Inference

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

Sa inference loop, gumagawa tayo ng mga tokens isa-isa hanggang maabot ang nais na sample length o ma-encounter ang end-of-sequence token. Ang susunod na token ay kino-convert sa tensor at pinapasa sa model, habang ang logits ay pinoproseso para mag-apply ng penalties at sampling. Pagkatapos, ang susunod na token ay nase-sample, na-de-decode, at ina-append sa sequence.
Para maiwasan ang paulit-ulit na teksto, naglalagay tayo ng penalty sa mga repeated tokens base sa `repeat_last_n` and `repeat_penalty` parameters.

Sa huli, ang generated na teksto ay piniprint habang nade-decode, para magkaroon ng real-time na output.

## Step 7: Run the Application

Para patakbuhin ang application, i-execute ang sumusunod na command sa terminal:

```bash
cargo run --release
```

Dapat itong mag-print ng haiku tungkol sa ice hockey na ginawa ng Phi-3 model. Halimbawa:

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

## Conclusion

Sa pagsunod sa mga hakbang na ito, makakagawa tayo ng text generation gamit ang Phi-3 model sa Rust at Candle sa loob ng mas mababa sa 100 lines ng code. Ang code ay humahawak sa pag-load ng model, tokenization, at inference, gamit ang tensors at logits processing para makabuo ng coherent na teksto base sa input prompt.

Ang console application na ito ay pwedeng tumakbo sa Windows, Linux, at Mac OS. Dahil sa portability ng Rust, pwede rin i-adapt ang code para maging library na tatakbo sa loob ng mga mobile apps (dahil hindi pwedeng patakbuhin ang console apps doon).

## Appendix: full code

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

Note: para mapatakbo ang code na ito sa aarch64 Linux o aarch64 Windows, magdagdag ng file na pinangalanang `.cargo/config` na may sumusunod na laman:

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

> Maaari mong bisitahin ang opisyal na [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository para sa iba pang mga halimbawa kung paano gamitin ang Phi-3 model gamit ang Rust at Candle, kabilang ang mga alternatibong paraan ng inference.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinakapinagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.