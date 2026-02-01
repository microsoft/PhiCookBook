# ರಸ್ಟ್‌ನೊಂದಿಗೆ ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಇನ್‌ಫರೆನ್ಸ್

ಈ ಟ್ಯುಟೋರಿಯಲ್ ನಮಗೆ HuggingFace ಕ್ಕಾರಿನ [Candle ML framework](https://github.com/huggingface/candle) ಬಳಸಿ ರಸ್ಟ್‌ನಲ್ಲಿ ಇನ್‌ಫರೆನ್ಸ್ ನಡೆಸುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು 안내 ಮಾಡುತ್ತದೆ. ಇನ್‌ಫರೆನ್ಸ್‌ಗಾಗಿ ರಸ್ಟ್ ಬಳಸುವುದರಿಂದ, ವಿಶೇಷವಾಗಿ ಅನ್ಯ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳೊಂದಿಗೆ ಹೋಲಿಸಿದಾಗ, ಹಲವಾರು ಪ್ರಯೋಜನಗಳಾಗುತ್ತವೆ. ರಸ್ಟ್ ತನ್ನ ಉನ್ನತ ಪ್ರದರ್ಶನಕ್ಕಾಗಿ (C ಮತ್ತು C++ ರ ಮಟ್ಟಿಗೆ) ಪರಿಚಿತವಾಗಿದೆ. ಇದು ಗಣನೆಗತವಾಗಿ ತೀವ್ರವಾದ ಇನ್‌ಫರೆನ್ಸ್ ಕಾರ್ಯಗಳಿಗೊಂದು ಒಳ್ಳೆಯ ಆಯ್ಕೆ ಒದಗಿಸುತ್ತದೆ. ವಿಶೇಷವಾಗಿ, ಇದು ಶೂನ್ಯ-ಖರ್ಚಿನ ಆಬ್ಸ್ಟ್ರಾಕ್ಷನ್‌ಗಳು ಮತ್ತು ಪರಿಣಾಮಕಾರಿ ಮemory ನಿರ್ವಹಣೆಯ ಮೂಲಕ ಚಾಲಿತವಾಗಿದ್ದು, ಗಾರ್ಬೇಜ್ ಕಲೆಕ್ಷನ್ ಒವರ್‌ಹೆಡ್‌ ಇಲ್ಲದೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ. ರಸ್ಟ್‌ನ ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಸಾಮರ್ಥ್ಯಗಳು ವಿವಿಧ ಕಾರ್ಯನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ — Windows, macOS ಮತ್ತು Linux ಸೇರಿದಂತೆ — ಹಾಗೂ ಮೊಬೈಲ್ ಕಾರ್ಯನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ ಸೂಕ್ತ ಬದಲಾವಣೆಗಳಿಲ್ಲದೆ ಕೋಡ್ ಅನ್ನು ಕಾರ್ಯಗೊಳಿಸಲು ಅನುಮತಿಸುತ್ತವೆ.

ಈ ಟ್ಯುಟೋರಿಯಲ್ ಅನುಸರಿಸಲು ಅಗತ್ಯವಿರುವ ಪೂರ್ವಶರ್ತು [Rust ಅನ್ನು ಸ್ಥಾಪಿಸಿ](https://www.rust-lang.org/tools/install), ಇದರಲ್ಲಿ ರಸ್ಟ್ ಕಂಪೈಲರ್ ಮತ್ತು Rust ಪ್ಯಾಕೇಜ್ ಮ್ಯಾನೇಜರ್ Cargo ಸೇರಿವೆ.

## Step 1: Create a New Rust Project

ಹೊಸ ರಸ್ಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು, ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ಚಲಾಯಿಸಿ:

```bash
cargo new phi-console-app
```

ಇದು ಆರಂಭಿಕ ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆಯನ್ನು ಉಂಟುಮಾಡುತ್ತದೆ, ಇದರೊಳಗೆ `Cargo.toml` ಫೈಲ್ ಮತ್ತು `src` ಡೈರೆಕ್ಟರಿ ಅಂದಾಜಿನಲ್ಲಿ `main.rs` ಫೈಲ್ ಇರುತ್ತದೆ.

ಅದರಲ್ಲಿ ನಾವು ನಮ್ಮ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸುತ್ತೇವೆ — ಮುಖ್ಯವಾಗಿ `candle`, `hf-hub` ಮತ್ತು `tokenizers` ಕ್ರೇಟ್ಸ್ — `Cargo.toml` ಫೈಲ್‌ಗೆ:

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

`main.rs` ಫೈಲ್‌ನ ಒಳಗಾಗಿಯೇ ನಾವು ಇನ್‌ಫರೆನ್ಸ್‌ಗಾಗಿ ಪ್ರಾಥಮಿಕ ಪರಿಮಾಣಗಳನ್ನು ಸೆಟ್ ಮಾಡೋಣ. ಸುಲಭತೆಗೆ ಅವುಗಳನ್ನು ಹಾರ್ಡ್‌ಕೋಡ್ ಮಾಡಲಾಗುತ್ತದೆ, ಆದರೆ ಬೇಕಾದರೆ ನಾವು ಅವನ್ನು ಬದಲಾಯಿಸಬಹುದು.

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

- **temperature**: ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರಕ್ರಿಯೆಯ ಅನಿಯಮಿತತೆಯನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.
- **sample_len**: ರಚಿಸಲಾಗುವ ಪಠ್ಯದ ಗರಿಷ್ಠ ಉದ್ದವನ್ನು ಸೂಚಿಸುತ್ತದೆ.
- **top_p**: ಪ್ರತಿ ಹಂತಕ್ಕಾಗಿ ಪರಿಗಣಿಸಲಾದ ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಮಿತಿಗೊಳಿಸಲು ನ್ಯೂಕ್ಲಿಯಸ್ ಸ್ಯಾಂಪ್ಲಿಂಗ್‌ನಲ್ಲಿ ಬಳಕೆಯಾಗುತ್ತದೆ.
- **repeat_last_n**: ಪುನರಾವೃತ್ತಿ ಸರಣಿಗಳನ್ನು ತಡೆಯಲು ದಂಡ ವಿಧಿಸಲು ಪರಿಗಣಿಸಬೇಕಾದ ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆಯನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.
- **repeat_penalty**: ಪುನರಾವೃತ್ತಿ ಟೋಕನ್‌ಗಳನ್ನು ನಮ್ರವಾಗಿ ತಡೆಯಲು ಅನ್ವಯಿಸುವ ದಂಡದ ಮೌಲ್ಯ.
- **seed**: ರ್ಯಾಂಡಮ್ ಬೀಜ (ಉತ್ತಮ ಪುನರಾವೃತ್ತಿಗಾಗಿ ಸ್ಥಿರ ಮೌಲ್ಯವನ್ನು ಬಳಸಬಹುದು).
- **prompt**: ರಚನೆ ಆರಂಭಿಸಲು ಆರಂಭಿಕ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯ. ಇಲ್ಲಿ ನಾವು ಮಾದರಿಯನ್ನು ಐಸ್ ಹಾಕಿ ಮೇಲೆ ಹೈಕು ರಚಿಸಲು ಕೇಳಿಸುತ್ತೇವೆ ಮತ್ತು ಬಳಕೆದಾರ ಮತ್ತು ಸಹಾಯಕ ಭಾಗಗಳನ್ನು ಸೂಚಿಸಲು ವಿಶೇಷ ಟೋಕನ್‌ಗಳಿಂದ ಅದನ್ನು ಮುಚ್ಚುತ್ತೇವೆ. ನಂತರ ಮಾದರಿ ಆ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಹೈಕು ಮೂಲಕ ಪೂರ್ಣಗೊಳಿಸುತ್ತದೆ.
- **device**: ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಗಣನೆಗಾಗಿ ನಾವು CPU ಬಳಕೆ ಮಾಡುತ್ತಿದ್ದೇವೆ. Candle CUDA ಮತ್ತು Metal ಮುಖಾಂತರ GPU ಯಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಣೆಯನ್ನು ಸಹ ಬೆಂಬಲಿಸುತ್ತದೆ.

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

ನಾವು Hugging Face ಮಾದರಿ ಹಬ್‌ನಿಂದモデル ಮತ್ತು ಟೋಕನೈಜರ್ ಫೈಲ್‌ಗಳನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಲು `hf_hub` API ಯನ್ನೇ ಬಳಸುತ್ತೇವೆ. `gguf` ಫೈಲ್ ಅನ್ನು ಕ್ವಾಂಟೈಜ್ಡ್ ಮಾದರಿ ತೂಕಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಮತ್ತು `tokenizer.json` ಫೈಲ್ ನಮ್ಮ ಇನ್‌ಪುಟ್ ಪಠ್ಯವನ್ನು ಟೋಕನೈಸ್ ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ. ಡೌನ್ಲೋಡ್ ಆದ ನಂತರ ಮಾದರಿ ಕ್ಯಾಶ್ ಆಗುತ್ತದೆ, ಆದ್ದರಿಂದ ಮೊದಲ ಕಾರ್ಯಗತ್ಕರಣೆ ನಿಧಾನವಾಗಿರುತ್ತದೆ (ಮಾದರಿ 2.4GB ಅನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡೋದರಿಂದ) ಆದರೆ ನಂತರದ ಚಲಾವಣೆಗಳು ವೇಗವಾಗಿರುತ್ತವೆ.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ನಾವು ಕ್ವಾಂಟೈಜ್ಡ್ ಮಾದರಿ ತೂಕಗಳನ್ನು ಮೆಮರಿಯಲ್ಲಿ ಲೋಡ್ ಮಾಡಿ Phi-3 ಮಾದರಿಯನ್ನು ಆರಂಭಿಸೋಣ. ಈ ಹಂತವು `gguf` ಫೈಲ್‌ನಿಂದ ಮಾದರಿ ತೂಕಗಳನ್ನು ಓದುವಂತಿದ್ದು, ನಿರ್ದಿಷ್ಟ ಸಾಧನದಲ್ಲಿ (ಈ ಉದಾಹರಣೆಯಲ್ಲಿ CPU) ಇನ್‌ಫರೆನ್ಸ್‌ಗೆ ಮಾದರಿಯನ್ನು ಸಜ್ಜುಗೊಳಿಸುವುದನ್ನು ಒಳಗೊಂಡಿದೆ.

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

ಈ ಹಂತದಲ್ಲಿ, ನಾವು ಇನ್‌ಪುಟ್ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಟೋಕನೈಸ್ ಮಾಡಿ ಟೋಕನ್ ಐಡಿಗಳ ಸರಣಿಯಾಗಿ ಪರಿವರ್ತನೆ ಮಾಡಲು ಅದನ್ನು ಇನ್‌ಫರೆನ್ಸ್‌ಗೆ ತಯಾರಿಸುತ್ತೇವೆ. ನಾವು ನೀಡಿರುವ `temperature` ಮತ್ತು `top_p` ಮೌಲ್ಯಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು (ಶಬ್ದಕೋಶದ ಮೇಲೆ ಪ್ರಾಬಬಿಲಿಟಿ ವಿತರಣೆಯನ್ನು) ನಿರ್ವಹಿಸಲು `LogitsProcessor` ಅನ್ನು ಸಹ ಪ್ರಾರಂಭಿಸುತ್ತೇವೆ. ಪ್ರತಿ ಟೋಕನ್ ಅನ್ನು ಟೆನ್ಸರ್ ಆಗಿ ಪರಿವರ್ತಿಸಿ ಮಾದರಿಯಲ್ಲಿಗೆ ಪಾಸು ಮಾಡಲಾಗುತ್ತದೆ ಮತ್ತು ಲಾಜಿಟ್‌ಗಳನ್ನು ಪಡೆಯಲಾಗುತ್ತದೆ.

ಲೂಪ್ ಪ್ರಾಂಪ್ಟ್‌ನ ಪ್ರತಿ ಟೋಕನ್ ಅನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುತ್ತದೆ, ಲಾಜಿಟ್ ಪ್ರೊಸೆಸರ್ ಅನ್ನು ನವೀಕರಿಸುತ್ತದೆ ಮತ್ತು ಮುಂದಿನ ಟೋಕನ್ ರಚನೆಗೆ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ.

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

ಇನ್‌ಫರೆನ್ಸ್ ಲೂಪ್‌ನಲ್ಲಿ, ನಾವು ಅಗತ್ಯ/sample_len ಗೆ ತಲುಪಿ ಅಥವಾ ಎಂಡ್-ಆಫ್-ಸಿಕ್ವೆನ್ಸ್ ಟೋಕನ್ ಕಂಡು ಬಿಡುವವರೆಗೂ ಟೋಕನ್‌ಗಳನ್ನು ಒಂದೊಂದಾಗಿ ರಚಿಸುತ್ತೇವೆ. ಮುಂದಿನ ಟೋಕನ್ ಅನ್ನು ಟೆನ್ಸರ್ ಆಗಿ ಪರಿವರ್ತಿಸಿ ಮಾದರಿಗೆ ಪಾಸು ಮಾಡಲಾಗುತ್ತದೆ, ಅಂದರೆ ಲಾಜಿಟ್‌ಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ ದಂಡಗಳು ಮತ್ತು ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನ್ವಯಿಸಲಾಗುತ್ತದೆ. ನಂತರ ಮುಂದಿನ ಟೋಕನ್ ನ sampಲ್ ಮಾಡಲಾಗುತ್ತದೆ, ಡಿಕೋಡ್ ಮಾಡಿ ಸರಣಿಗೆ ಸೇರಿಸಲಾಗುತ್ತದೆ.
ಪುನರಾವೃತ್ತಿ ಪಠ್ಯವನ್ನು ತಡೆಯಲು, `repeat_last_n` ಮತ್ತು `repeat_penalty` ಪರಿಮಾಣಗಳ ಆಧಾರದ ಮೇಲೆ ಪುನರಾವೃತ್ತಿ ಟೋಕನ್‌ಗಳಿಗೆ ದಂಡ ಅನ್ವಯಿಸಲಾಗುತ್ತದೆ.

ಕೊನೆಯಲ್ಲಿ, rಚಿಸಲಾದ ಪಠ್ಯ ಡಿಕೋಡ್ ಆಗುತ್ತಾ ಮುದ್ರಣವಾಗುತ್ತದೆ, ಈ ಮೂಲಕ ಸ್ಟ್ರೀಮ್ ಸ್ವರೂಪದಲ್ಲಿ ರಿಯಲ್-ಟೈಮ್ ಔಟ್‌ಪುಟ್ ಖಾತ್ರಿ ಮಾಡಲಾಗುತ್ತದೆ.

## Step 7: Run the Application

ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ರನ್ ಮಾಡಲು, ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ನಿರ್ವಹಿಸಿ:

```bash
cargo run --release
```

ಇದು Phi-3 ಮಾದರಿಯು ರಚಿಸಿದ ಐಸ್ ಹಾಕಿ ಬಗ್ಗೆ ಒಂದು ಹೈಕುವನ್ನು ಮುದ್ರಿತ ಮಾಡಬೇಕು. ಉದಾಹರಣೆಗೆ ಈ ರೀತಿ ಏನಾದರೂ:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ಅಥವಾ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸುವ ಮೂಲಕ, ನಾವು Rust ಮತ್ತು Candle ಬಳಸಿ Phi-3 ಮಾದರಿಯೊಂದಿಗೆ 100 ಸಾಲುಗಳೊಳಗಾಗಿ ಪಠ್ಯ ರಚನೆ ನಡೆಸಬಹುದು. ಕೋಡ್ ಮಾದರಿ ಲೋಡ್ ಮಾಡುವುದು, ಟೋಕನೈಜೇಶನ್ ಮತ್ತು ಇನ್‌ಫರೆನ್ಸ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಟೆನ್ಸರ್‌ಗಳು ಮತ್ತು ಲಾಜಿಟ್ಸ್ ಸಂಸ್ಕರಣೆಯನ್ನು ಉಪಯೋಗಿಸಿ ಇನ್‌ಪುಟ್ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರವಾಗಿ ಸನ್ಮಾನ್ಯವಾದ ಪಠ್ಯವನ್ನು ರಚಿಸುತ್ತದೆ.

ಈ ಕન્સೋಲ್ ಅಪ್ಲಿಕೇಶನ್ Windows, Linux ಮತ್ತು Mac OS ಮೇಲೆ ಚಾಲನೆ ಮಾಡಬಹುದು. ರಸ್ಟ್‌ನ ಪೋರ್ಟಬಿಲಿಟಿಯ ಕಾರಣದಿಂದಾಗಿ, ಕೋಡ್ ಅನ್ನು ಮೊಬೈಲ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಚಲಿಸುವ ಲೈಬ್ರರಿಯಾಗಿ ಕೂಡ ಹೊಂದಿಸಬಹುದಾಗಿದೆ (ಅವುದರಲ್ಲಿ ಕಾನ್ಸೋಲ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನೇರವಾಗಿ ಚಲಾಯಿಸಲು ಆಗುವುದಿಲ್ಲ).

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

Note: in order to run this code on aarch64 Linux or aarch64 Windows, add a file named `.cargo/config` with the following content:

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

> ನೀವು ಅಧಿಕೃತ [Candle ಉದಾಹರಣೆಗಳು](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ರೆಪೊಸಿಟರಿಯನ್ನು Phi-3 ಮಾದರಿ ಬಳಸಿ Rust ಮತ್ತು Candle ಮೂಲಕ ಬಳಸುವ ಮೇಲೆಯಲ್ಲಿ ಇನ್ನಷ್ಟು ಉದಾಹರಣೆಗಳಿಗಾಗಿ ಭೇಟಿ ಮಾಡಬಹುದು, ವೈಕಲ್ಪಿಕ ಇನ್‌ಫರೆನ್ಸ್ സമീപನಗಳನ್ನು ಒಳಗೊಂಡಂತೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿಟ್ಟು ಕೊಳ್ಳಿ. ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲೇ ಪ್ರಾಧಿಕಾರಪೂರ್ಣ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಲಾಗಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗರ್ಭಿತತೆಗಳಿಗೆ ಅಥವಾ ಕಲ್ಪನೆಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->