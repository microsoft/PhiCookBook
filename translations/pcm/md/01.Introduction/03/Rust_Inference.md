<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-12-22T01:32:24+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "pcm"
}
-->
# Cross-platform inference wit Rust

Dis tutorial go guide we through di process of doing inference using Rust and di [Candle ML framework](https://github.com/huggingface/candle) from HuggingFace. Using Rust for inference get plenti advantages, especially when you compare am with other programming languages. Rust dey known for im high performance, near same as C and C++. Dis make am fine choice for inference tasks wey fit heavy for computation. Specifically, na im zero-cost abstractions and efficient memory management wey no get garbage collection overhead dey drive am. Rust cross-platform ability make you fit write code wey go run for different operating systems like Windows, macOS, and Linux, and even mobile operating systems, without big changes for the codebase.

To follow dis tutorial you need to [install Rust](https://www.rust-lang.org/tools/install), wey include the Rust compiler and Cargo, the Rust package manager.

## Step 1: Create a New Rust Project

To create new Rust project, run di command below for your terminal:

```bash
cargo new phi-console-app
```

This go generate initial project structure with a `Cargo.toml` file and a `src` directory wey contain a `main.rs` file.

Next, we go add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` file:

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

Inside the `main.rs` file, we go set up di initial parameters for our inference. Dem go hardcode dem for simplicity, but we fit change dem as needed.

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

- **temperature**: Controls how random the sampling process go be.
- **sample_len**: Specifies di maximum length of di generated text.
- **top_p**: Na for nucleus sampling to limit how many tokens dem go consider for each step.
- **repeat_last_n**: Controls how many tokens dem go consider wen dem dey apply penalty to prevent repetitive sequences.
- **repeat_penalty**: Di penalty value to discourage repeated tokens.
- **seed**: Random seed (we fit use constant value for better reproducibility).
- **prompt**: Di initial prompt text wey go start di generation. Note say we ask di model make e generate a haiku about ice hockey, and we wrap am with special tokens to show di user and assistant parts of di conversation. Di model go then complete di prompt with a haiku.
- **device**: We dey use di CPU for computation for dis example. Candle fit also run on GPU with CUDA and Metal.

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

We use di `hf_hub` API to download di model and tokenizer files from di Hugging Face model hub. Di `gguf` file contain di quantized model weights, while di `tokenizer.json` file dey used for tokenizing our input text. Once di model don download e go cache, so di first execution go slow (as e go download di 2.4GB of di model) but subsequent executions go dey faster.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

We load di quantized model weights into memory and initialize di Phi-3 model. Dis step involve reading di model weights from di `gguf` file and setting up di model for inference on di specified device (CPU for dis case).

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

For dis step, we tokenize di input prompt and prepare am for inference by converting am into sequence of token IDs. We also initialize di `LogitsProcessor` to handle di sampling process (probability distribution over di vocabulary) based on di `temperature` and `top_p` values. Each token dey convert to a tensor and pass through di model to get di logits.

Di loop dey process each token for di prompt, dey update di logits processor and ready for di next token generation.

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

For di inference loop, we go generate tokens one by one until we reach di desired sample length or encounter di end-of-sequence token. Di next token dey convert to a tensor and pass through di model, while di logits dey processed to apply penalties and sampling. Then dem sample di next token, decode am, and append am to di sequence.
To avoid repetitive text, dem apply penalty to repeated tokens based on di `repeat_last_n` and `repeat_penalty` parameters.

Finally, di generated text dey printed as e dey decode, ensuring streamed real-time output.

## Step 7: Run the Application

To run di application, execute di following command in di terminal:

```bash
cargo run --release
```

This suppose print a haiku about ice hockey wey di Phi-3 model generate. Something like:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

or

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

If we follow these steps, we fit perform text generation using di Phi-3 model with Rust and Candle inside less than 100 lines of code. Di code dey handle model loading, tokenization, and inference, using tensors and logits processing to generate coherent text based on di input prompt.

Dis console application fit run for Windows, Linux and Mac OS. Because Rust portable, di code fit also adapt to a library wey go run inside mobile apps (we no fit run console apps there, after all).

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

Note: to run dis code on aarch64 Linux or aarch64 Windows, add a file named `.cargo/config` with di following content:

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

> You fit visit di official [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository for more examples on how to use di Phi-3 model with Rust and Candle, including other approaches to inference.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate wit AI translation service [Co-op Translator]. Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or inaccuracies. Di original document for im native language suppose be di authoritative source. If na important information, make una use professional human translation. We no go take responsibility for any misunderstanding or misinterpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->