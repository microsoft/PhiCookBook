# ਰਸਟ ਨਾਲ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਇਨਫਰੈਂਸ

ਇਹ ਟਿਊਟੋਰਿਯਲ ਸਾਨੂੰ ਰਸਟ ਅਤੇ HuggingFace ਦੇ [Candle ML ਫਰੇਮਵਰਕ](https://github.com/huggingface/candle) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਫਰੈਂਸ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਰਾਹਨੁਮਾ ਕਰੇਗਾ। ਇਨਫਰੈਂਸ ਲਈ ਰਸਟ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਕਈ ਫਾਇਦੇ ਹਨ, ਖਾਸ ਕਰਕੇ ਹੋਰ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਨਾਲ ਤੁਲਨਾ ਕਰਨ 'ਤੇ। ਰਸਟ ਆਪਣੀ ਉੱਚ ਪ੍ਰਦਰਸ਼ਨਸ਼ੀਲਤਾ ਲਈ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ C ਅਤੇ C++ ਦੇ ਬਰਾਬਰ ਹੈ। ਇਸ ਕਰਕੇ ਇਹ ਇਨਫਰੈਂਸ ਟਾਸਕਾਂ ਲਈ ਬਹੁਤ ਵਧੀਆ ਚੋਣ ਹੈ, ਜੋ ਕਿ ਕਮਪਿਊਟੇਸ਼ਨਲ ਤੌਰ 'ਤੇ ਭਾਰੀ ਹੋ ਸਕਦੇ ਹਨ। ਖਾਸ ਕਰਕੇ, ਇਹ ਜ਼ੀਰੋ-ਕੋਸਟ ਐਬਸਟ੍ਰੈਕਸ਼ਨ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਮੈਮੋਰੀ ਮੈਨੇਜਮੈਂਟ ਨਾਲ ਸੰਚਾਲਿਤ ਹੁੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਕੋਈ ਗਾਰਬੇਜ ਕਲੇਕਸ਼ਨ ਓਵਰਹੈੱਡ ਨਹੀਂ ਹੁੰਦਾ। ਰਸਟ ਦੀ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਸਮਰੱਥਾ ਵੱਖ-ਵੱਖ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਜਿਵੇਂ ਕਿ Windows, macOS, ਅਤੇ Linux ਨਾਲ ਨਾਲ ਮੋਬਾਈਲ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ 'ਤੇ ਵੀ ਬਿਨਾਂ ਵੱਡੇ ਬਦਲਾਅ ਦੇ ਕੋਡ ਚਲਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।

ਇਸ ਟਿਊਟੋਰਿਯਲ ਨੂੰ ਫਾਲੋ ਕਰਨ ਲਈ ਪਹਿਲਾਂ [Rust ਇੰਸਟਾਲ ਕਰੋ](https://www.rust-lang.org/tools/install), ਜਿਸ ਵਿੱਚ Rust ਕੰਪਾਇਲਰ ਅਤੇ Cargo, Rust ਪੈਕੇਜ ਮੈਨੇਜਰ ਸ਼ਾਮਲ ਹਨ।

## ਕਦਮ 1: ਨਵਾਂ Rust ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

ਨਵਾਂ Rust ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
cargo new phi-console-app
```

ਇਸ ਨਾਲ ਇੱਕ ਮੁੱਢਲਾ ਪ੍ਰੋਜੈਕਟ ਸਟ੍ਰਕਚਰ ਬਣਦਾ ਹੈ ਜਿਸ ਵਿੱਚ `Cargo.toml` ਫਾਇਲ ਅਤੇ `src` ਡਾਇਰੈਕਟਰੀ ਹੁੰਦੀ ਹੈ ਜਿਸ ਵਿੱਚ `main.rs` ਫਾਇਲ ਸ਼ਾਮਲ ਹੈ।

ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਅਸੀਂ ਆਪਣੀਆਂ ਡਿਪੈਂਡੈਂਸੀਜ਼ - ਜਿਵੇਂ ਕਿ `candle`, `hf-hub` ਅਤੇ `tokenizers` crates - ਨੂੰ `Cargo.toml` ਫਾਇਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਾਂਗੇ:

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

## ਕਦਮ 2: ਬੁਨਿਆਦੀ ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰੋ

`main.rs` ਫਾਇਲ ਦੇ ਅੰਦਰ ਅਸੀਂ ਆਪਣੀ ਇਨਫਰੈਂਸ ਲਈ ਮੁੱਢਲੇ ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰਾਂਗੇ। ਇਹ ਸਾਰੇ ਸੌਖਿਆ ਲਈ ਹਾਰਡਕੋਡ ਕੀਤੇ ਜਾਣਗੇ, ਪਰ ਜਰੂਰਤ ਪੈਣ 'ਤੇ ਅਸੀਂ ਇਨ੍ਹਾਂ ਨੂੰ ਬਦਲ ਸਕਦੇ ਹਾਂ।

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

- **temperature**: ਸੈਂਪਲਿੰਗ ਪ੍ਰਕਿਰਿਆ ਦੀ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।
- **sample_len**: ਬਣਾਈ ਗਈ ਟੈਕਸਟ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ ਦੱਸਦਾ ਹੈ।
- **top_p**: ਨਿਊਕਲੀਅਸ ਸੈਂਪਲਿੰਗ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ ਹਰ ਕਦਮ ਲਈ ਵਿਚਾਰ ਕੀਤੇ ਜਾਣ ਵਾਲੇ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੂੰ ਸੀਮਿਤ ਕਰਦਾ ਹੈ।
- **repeat_last_n**: ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ ਲੜੀਵਾਰ ਟੋਕਨਾਂ 'ਤੇ ਜੁਰਮਾਨਾ ਲਗਾਉਣ ਲਈ ਵਿਚਾਰ ਕੀਤੇ ਜਾਣ ਵਾਲੇ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।
- **repeat_penalty**: ਦੁਹਰਾਏ ਗਏ ਟੋਕਨਾਂ ਨੂੰ ਰੋਕਣ ਲਈ ਜੁਰਮਾਨਾ ਮੁੱਲ।
- **seed**: ਇੱਕ ਰੈਂਡਮ ਸੀਡ (ਵਧੀਆ ਦੁਹਰਾਅਯੋਗਤਾ ਲਈ ਅਸੀਂ ਇੱਕ ਸਥਿਰ ਮੁੱਲ ਵਰਤ ਸਕਦੇ ਹਾਂ)।
- **prompt**: ਜਨਰੇਸ਼ਨ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਮੁੱਢਲਾ ਪ੍ਰਾਂਪਟ ਟੈਕਸਟ। ਧਿਆਨ ਦਿਓ ਕਿ ਅਸੀਂ ਮਾਡਲ ਨੂੰ ਆਈਸ ਹਾਕੀ ਬਾਰੇ ਇੱਕ ਹਾਇਕੂ ਬਣਾਉਣ ਲਈ ਕਹਿ ਰਹੇ ਹਾਂ, ਅਤੇ ਇਸਨੂੰ ਵਿਸ਼ੇਸ਼ ਟੋਕਨਾਂ ਨਾਲ ਘੇਰਿਆ ਗਿਆ ਹੈ ਜੋ ਗੱਲਬਾਤ ਵਿੱਚ ਯੂਜ਼ਰ ਅਤੇ ਅਸਿਸਟੈਂਟ ਹਿੱਸਿਆਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਮਾਡਲ ਫਿਰ ਇਸ ਪ੍ਰਾਂਪਟ ਨੂੰ ਹਾਇਕੂ ਨਾਲ ਪੂਰਾ ਕਰੇਗਾ।
- **device**: ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ ਗਣਨਾ ਲਈ CPU ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹਾਂ। Candle GPU 'ਤੇ CUDA ਅਤੇ Metal ਨਾਲ ਚਲਾਉਣ ਦਾ ਸਮਰਥਨ ਵੀ ਕਰਦਾ ਹੈ।

## ਕਦਮ 3: ਮਾਡਲ ਅਤੇ ਟੋਕਨਾਈਜ਼ਰ ਡਾਊਨਲੋਡ/ਤਿਆਰ ਕਰੋ

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

ਅਸੀਂ `hf_hub` API ਦੀ ਵਰਤੋਂ ਕਰਕੇ Hugging Face ਮਾਡਲ ਹੱਬ ਤੋਂ ਮਾਡਲ ਅਤੇ ਟੋਕਨਾਈਜ਼ਰ ਫਾਇਲਾਂ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹਾਂ। `gguf` ਫਾਇਲ ਵਿੱਚ ਕਵਾਂਟਾਈਜ਼ਡ ਮਾਡਲ ਵਜ਼ਨ ਹੁੰਦੇ ਹਨ, ਜਦਕਿ `tokenizer.json` ਫਾਇਲ ਸਾਡੇ ਇਨਪੁੱਟ ਟੈਕਸਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਇੱਕ ਵਾਰੀ ਡਾਊਨਲੋਡ ਹੋਣ ਤੋਂ ਬਾਅਦ ਮਾਡਲ ਕੈਸ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਇਸ ਲਈ ਪਹਿਲੀ ਵਾਰੀ ਚਲਾਉਣ ਵਿੱਚ ਸਮਾਂ ਲੱਗੇਗਾ (ਕਿਉਂਕਿ ਇਹ 2.4GB ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ), ਪਰ ਅਗਲੇ ਚਲਾਉਣ ਤੇ ਤੇਜ਼ੀ ਆਵੇਗੀ।

## ਕਦਮ 4: ਮਾਡਲ ਲੋਡ ਕਰੋ

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ਅਸੀਂ ਕਵਾਂਟਾਈਜ਼ਡ ਮਾਡਲ ਵਜ਼ਨ ਮੈਮੋਰੀ ਵਿੱਚ ਲੋਡ ਕਰਦੇ ਹਾਂ ਅਤੇ Phi-3 ਮਾਡਲ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ। ਇਸ ਕਦਮ ਵਿੱਚ `gguf` ਫਾਇਲ ਤੋਂ ਮਾਡਲ ਵਜ਼ਨ ਪੜ੍ਹਨਾ ਅਤੇ ਨਿਰਧਾਰਿਤ ਡਿਵਾਈਸ (ਇਸ ਮਾਮਲੇ ਵਿੱਚ CPU) 'ਤੇ ਇਨਫਰੈਂਸ ਲਈ ਮਾਡਲ ਸੈੱਟ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ।

## ਕਦਮ 5: ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸ ਕਰੋ ਅਤੇ ਇਨਫਰੈਂਸ ਲਈ ਤਿਆਰ ਕਰੋ

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

ਇਸ ਕਦਮ ਵਿੱਚ ਅਸੀਂ ਇਨਪੁੱਟ ਪ੍ਰਾਂਪਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਟੋਕਨ ID ਦੀ ਲੜੀ ਵਿੱਚ ਬਦਲ ਕੇ ਇਨਫਰੈਂਸ ਲਈ ਤਿਆਰ ਕਰਦੇ ਹਾਂ। ਅਸੀਂ `LogitsProcessor` ਨੂੰ ਵੀ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ ਜੋ ਦਿੱਤੇ ਗਏ `temperature` ਅਤੇ `top_p` ਮੁੱਲਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਸੈਂਪਲਿੰਗ ਪ੍ਰਕਿਰਿਆ (ਵੋਕੈਬੁਲਰੀ ਉੱਤੇ ਸੰਭਾਵਨਾ ਵੰਡ) ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਹਰ ਟੋਕਨ ਨੂੰ ਟੈਂਸਰ ਵਿੱਚ ਬਦਲ ਕੇ ਮਾਡਲ ਵਿੱਚ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਲੋਗਿਟਸ ਮਿਲ ਸਕਣ।

ਲੂਪ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਹਰ ਟੋਕਨ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਦਾ ਹੈ, ਲੋਗਿਟਸ ਪ੍ਰੋਸੈਸਰ ਨੂੰ ਅਪਡੇਟ ਕਰਦਾ ਹੈ ਅਤੇ ਅਗਲੇ ਟੋਕਨ ਜਨਰੇਸ਼ਨ ਲਈ ਤਿਆਰੀ ਕਰਦਾ ਹੈ।

## ਕਦਮ 6: ਇਨਫਰੈਂਸ

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

ਇਨਫਰੈਂਸ ਲੂਪ ਵਿੱਚ ਅਸੀਂ ਟੋਕਨ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਜਨਰੇਟ ਕਰਦੇ ਹਾਂ ਜਦ ਤੱਕ ਅਸੀਂ ਚਾਹੀਦੀ sample_len ਤੱਕ ਨਹੀਂ ਪਹੁੰਚ ਜਾਂਦੇ ਜਾਂ end-of-sequence ਟੋਕਨ ਨਹੀਂ ਮਿਲ ਜਾਂਦਾ। ਅਗਲਾ ਟੋਕਨ ਟੈਂਸਰ ਵਿੱਚ ਬਦਲ ਕੇ ਮਾਡਲ ਵਿੱਚ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ, ਜਦਕਿ ਲੋਗਿਟਸ ਨੂੰ ਜੁਰਮਾਨਾ ਲਗਾਉਣ ਅਤੇ ਸੈਂਪਲਿੰਗ ਲਈ ਪ੍ਰੋਸੈਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਫਿਰ ਅਗਲਾ ਟੋਕਨ ਸੈਂਪਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਡੀਕੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਲੜੀ ਵਿੱਚ ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ।  
ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ ਟੈਕਸਟ ਤੋਂ ਬਚਣ ਲਈ, `repeat_last_n` ਅਤੇ `repeat_penalty` ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਦੁਹਰਾਏ ਗਏ ਟੋਕਨਾਂ 'ਤੇ ਜੁਰਮਾਨਾ ਲਗਾਇਆ ਜਾਂਦਾ ਹੈ।

ਅੰਤ ਵਿੱਚ, ਜਨਰੇਟ ਕੀਤਾ ਟੈਕਸਟ ਜਿਵੇਂ ਹੀ ਡੀਕੋਡ ਹੁੰਦਾ ਹੈ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਸਟ੍ਰੀਮਿੰਗ ਆਉਟਪੁੱਟ ਮਿਲਦੀ ਹੈ।

## ਕਦਮ 7: ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ

ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਲਈ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
cargo run --release
```

ਇਸ ਨਾਲ Phi-3 ਮਾਡਲ ਦੁਆਰਾ ਜਨਰੇਟ ਕੀਤਾ ਗਿਆ ਆਈਸ ਹਾਕੀ ਬਾਰੇ ਇੱਕ ਹਾਇਕੂ ਪ੍ਰਿੰਟ ਹੋਵੇਗਾ। ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ਜਾਂ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## ਨਤੀਜਾ

ਇਨ੍ਹਾਂ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਅਸੀਂ Phi-3 ਮਾਡਲ ਨਾਲ ਰਸਟ ਅਤੇ Candle ਦੀ ਵਰਤੋਂ ਕਰਕੇ 100 ਲਾਈਨਾਂ ਤੋਂ ਘੱਟ ਕੋਡ ਵਿੱਚ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਕਰ ਸਕਦੇ ਹਾਂ। ਕੋਡ ਮਾਡਲ ਲੋਡਿੰਗ, ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਇਨਫਰੈਂਸ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ, ਟੈਂਸਰ ਅਤੇ ਲੋਗਿਟਸ ਪ੍ਰੋਸੈਸਿੰਗ ਦੀ ਮਦਦ ਨਾਲ ਇਨਪੁੱਟ ਪ੍ਰਾਂਪਟ ਦੇ ਆਧਾਰ 'ਤੇ ਸੰਗਠਿਤ ਟੈਕਸਟ ਬਣਾਉਂਦਾ ਹੈ।

ਇਹ ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ Windows, Linux ਅਤੇ Mac OS 'ਤੇ ਚੱਲ ਸਕਦਾ ਹੈ। ਰਸਟ ਦੀ ਪੋਰਟੇਬਿਲਿਟੀ ਕਾਰਨ, ਕੋਡ ਨੂੰ ਮੋਬਾਈਲ ਐਪਸ ਵਿੱਚ ਚਲਣ ਵਾਲੀ ਲਾਇਬ੍ਰੇਰੀ ਵਿੱਚ ਵੀ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ (ਅਸੀਂ ਉਥੇ ਕਨਸੋਲ ਐਪ ਨਹੀਂ ਚਲਾ ਸਕਦੇ, ਆਖਿਰਕਾਰ)।

## ਐਪੈਂਡਿਕਸ: ਪੂਰਾ ਕੋਡ

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

ਨੋਟ: aarch64 Linux ਜਾਂ aarch64 Windows 'ਤੇ ਇਹ ਕੋਡ ਚਲਾਉਣ ਲਈ `.cargo/config` ਨਾਮਕ ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੋਵੇ:

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

> ਤੁਸੀਂ ਅਧਿਕ ਜਾਣਕਾਰੀ ਲਈ ਅਧਿਕਾਰਿਕ [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ਰਿਪੋਜ਼ਟਰੀ ਵੇਖ ਸਕਦੇ ਹੋ, ਜਿੱਥੇ Rust ਅਤੇ Candle ਨਾਲ Phi-3 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਹੋਰ ਉਦਾਹਰਨਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਲਈ ਵਿਕਲਪਿਕ ਤਰੀਕੇ ਦਿੱਤੇ ਗਏ ਹਨ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।