<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:51:14+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "pa"
}
-->
# ਰਸਟ ਨਾਲ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਇੰਫਰੈਂਸ

ਇਹ ਟਿਊਟੋਰਿਯਲ ਸਾਨੂੰ ਰਸਟ ਅਤੇ HuggingFace ਦੇ [Candle ML framework](https://github.com/huggingface/candle) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੰਫਰੈਂਸ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ। ਇੰਫਰੈਂਸ ਲਈ ਰਸਟ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਕਈ ਫਾਇਦੇ ਹਨ, ਖਾਸ ਕਰਕੇ ਹੋਰ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਨਾਲ ਤੁਲਨਾ ਕਰਨ ਤੇ। ਰਸਟ ਆਪਣੀ ਉੱਚ ਪ੍ਰਦਰਸ਼ਨਸ਼ੀਲਤਾ ਲਈ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ C ਅਤੇ C++ ਦੇ ਬਰਾਬਰ ਹੈ। ਇਸ ਕਰਕੇ ਇਹ ਇੰਫਰੈਂਸ ਦੇ ਕੰਮਾਂ ਲਈ ਬਹੁਤ ਵਧੀਆ ਚੋਣ ਹੈ, ਜੋ ਕਿ ਗਣਨਾਤਮਕ ਤੌਰ 'ਤੇ ਭਾਰੀ ਹੋ ਸਕਦੇ ਹਨ। ਖਾਸ ਕਰਕੇ ਇਹ ਜ਼ੀਰੋ-ਕੋਸਟ ਐਬਸਟ੍ਰੈਕਸ਼ਨ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਮੈਮੋਰੀ ਮੈਨੇਜਮੈਂਟ ਨਾਲ ਸੰਭਵ ਹੁੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਕੋਈ ਗਾਰਬੇਜ ਕਲੇਕਸ਼ਨ ਦਾ ਓਵਰਹੈੱਡ ਨਹੀਂ ਹੁੰਦਾ। ਰਸਟ ਦੀ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਸਮਰੱਥਾ ਵੱਖ-ਵੱਖ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਜਿਵੇਂ ਕਿ Windows, macOS, ਅਤੇ Linux ਨਾਲ ਨਾਲ ਮੋਬਾਈਲ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ 'ਤੇ ਵੀ ਬਿਨਾਂ ਵੱਡੇ ਬਦਲਾਅ ਦੇ ਕੋਡ ਚਲਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।

ਇਸ ਟਿਊਟੋਰਿਯਲ ਨੂੰ ਫਾਲੋ ਕਰਨ ਲਈ ਲੋੜ ਹੈ ਕਿ ਤੁਸੀਂ [Rust ਇੰਸਟਾਲ ਕਰੋ](https://www.rust-lang.org/tools/install), ਜਿਸ ਵਿੱਚ Rust ਕੰਪਾਇਲਰ ਅਤੇ Cargo, Rust ਪੈਕੇਜ ਮੈਨੇਜਰ ਸ਼ਾਮਿਲ ਹਨ।

## ਕਦਮ 1: ਨਵਾਂ Rust ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

ਨਵਾਂ Rust ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
cargo new phi-console-app
```

ਇਸ ਨਾਲ ਇੱਕ ਮੂਲ ਪ੍ਰੋਜੈਕਟ ਸਟ੍ਰਕਚਰ ਬਣਦਾ ਹੈ ਜਿਸ ਵਿੱਚ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ਫਾਇਲ ਸ਼ਾਮਿਲ ਹੁੰਦੀ ਹੈ:

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

## ਕਦਮ 2: ਬੁਨਿਆਦੀ ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਸੰਰਚਨਾ ਕਰੋ

main.rs ਫਾਇਲ ਦੇ ਅੰਦਰ, ਅਸੀਂ ਆਪਣੇ ਇੰਫਰੈਂਸ ਲਈ ਮੁੱਢਲੇ ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰਾਂਗੇ। ਇਹ ਸਾਰੇ ਸੌਖਿਆ ਲਈ ਹਾਰਡਕੋਡ ਕੀਤੇ ਜਾਣਗੇ, ਪਰ ਜਰੂਰਤ ਅਨੁਸਾਰ ਅਸੀਂ ਇਹਨਾਂ ਨੂੰ ਬਦਲ ਸਕਦੇ ਹਾਂ।

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

- **temperature**: ਸੈਂਪਲਿੰਗ ਪ੍ਰਕਿਰਿਆ ਦੀ ਯਾਦਰਚਿੱਠਤਾ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।
- **sample_len**: ਬਣਾਈ ਗਈ ਲਿਖਤ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ ਦਰਸਾਉਂਦਾ ਹੈ।
- **top_p**: ਨਿਊਕਲੀਅਸ ਸੈਂਪਲਿੰਗ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ ਹਰ ਕਦਮ ਲਈ ਵਿਚਾਰੇ ਜਾਣ ਵਾਲੇ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਸੀਮਿਤ ਕਰਦਾ ਹੈ।
- **repeat_last_n**: ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ ਜੋ ਦੋਹਰਾਵਾਂ ਨੂੰ ਰੋਕਣ ਲਈ ਜੁਰਮਾਨਾ ਲਗਾਉਣ ਵਿੱਚ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।
- **repeat_penalty**: ਦੁਹਰਾਏ ਗਏ ਟੋਕਨਾਂ ਨੂੰ ਰੋਕਣ ਲਈ ਜੁਰਮਾਨਾ ਮੁੱਲ।
- **seed**: ਇੱਕ ਯਾਦਰਚਿੱਠ ਬੀਜ (ਸਹੀ ਦੁਹਰਾਵ ਲਈ ਅਸੀਂ ਇੱਕ ਸਥਿਰ ਮੁੱਲ ਵੀ ਵਰਤ ਸਕਦੇ ਹਾਂ)।
- **prompt**: ਸ਼ੁਰੂਆਤੀ ਪ੍ਰੰਪਟ ਲਿਖਤ ਜੋ ਜਨਰੇਸ਼ਨ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ ਅਸੀਂ ਮਾਡਲ ਨੂੰ ਆਈਸ ਹਾਕੀ ਬਾਰੇ ਇੱਕ ਹਾਈਕੂ ਬਣਾਉਣ ਲਈ ਕਹਿ ਰਹੇ ਹਾਂ, ਅਤੇ ਇਸ ਨੂੰ ਵਿਸ਼ੇਸ਼ ਟੋਕਨਾਂ ਨਾਲ ਲਪੇਟਿਆ ਗਿਆ ਹੈ ਜੋ ਯੂਜ਼ਰ ਅਤੇ ਅਸਿਸਟੈਂਟ ਹਿੱਸਿਆਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਮਾਡਲ ਫਿਰ ਪ੍ਰੰਪਟ ਨੂੰ ਇੱਕ ਹਾਈਕੂ ਨਾਲ ਪੂਰਾ ਕਰੇਗਾ।
- **device**: ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ ਗਣਨਾ ਲਈ CPU ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ। Candle GPU ਉੱਤੇ CUDA ਅਤੇ Metal ਨਾਲ ਚਲਾਉਣ ਦਾ ਸਮਰਥਨ ਵੀ ਕਰਦਾ ਹੈ।

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

ਅਸੀਂ `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` ਫਾਇਲ ਨੂੰ ਆਪਣੇ ਇਨਪੁੱਟ ਲਿਖਤ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਨ ਲਈ ਵਰਤਦੇ ਹਾਂ। ਇੱਕ ਵਾਰੀ ਮਾਡਲ ਡਾਊਨਲੋਡ ਹੋਣ 'ਤੇ ਕੈਸ਼ ਹੋ ਜਾਂਦਾ ਹੈ, ਇਸ ਲਈ ਪਹਿਲੀ ਵਾਰੀ ਚਲਾਉਣ ਵਿੱਚ ਸਮਾਂ ਲੱਗੇਗਾ (ਕਿਉਂਕਿ ਇਹ 2.4GB ਦਾ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ) ਪਰ ਅਗਲੇ ਚਲਾਉਣ ਤੇ ਇਹ ਤੇਜ਼ ਹੋਵੇਗਾ।

## ਕਦਮ 4: ਮਾਡਲ ਲੋਡ ਕਰੋ

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ਅਸੀਂ ਕੁਆਂਟਾਈਜ਼ਡ ਮਾਡਲ ਵਜ਼ਨ ਮੈਮੋਰੀ ਵਿੱਚ ਲੋਡ ਕਰਦੇ ਹਾਂ ਅਤੇ Phi-3 ਮਾਡਲ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ। ਇਹ ਕਦਮ `gguf` ਫਾਇਲ ਤੋਂ ਮਾਡਲ ਵਜ਼ਨ ਪੜ੍ਹਨ ਅਤੇ ਦਿੱਤੇ ਗਏ ਡਿਵਾਈਸ (ਇਸ ਮਾਮਲੇ ਵਿੱਚ CPU) 'ਤੇ ਇੰਫਰੈਂਸ ਲਈ ਮਾਡਲ ਸੈੱਟ ਕਰਨ ਨੂੰ ਸ਼ਾਮਿਲ ਕਰਦਾ ਹੈ।

## ਕਦਮ 5: ਪ੍ਰੰਪਟ ਪ੍ਰੋਸੈਸ ਕਰੋ ਅਤੇ ਇੰਫਰੈਂਸ ਲਈ ਤਿਆਰ ਕਰੋ

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

ਇਸ ਕਦਮ ਵਿੱਚ, ਅਸੀਂ ਇਨਪੁੱਟ ਪ੍ਰੰਪਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਟੋਕਨ IDਜ਼ ਦੀ ਲੜੀ ਵਿੱਚ ਬਦਲ ਕੇ ਇੰਫਰੈਂਸ ਲਈ ਤਿਆਰ ਕਰਦੇ ਹਾਂ। ਅਸੀਂ `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ਮੁੱਲ ਵੀ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ। ਹਰ ਟੋਕਨ ਨੂੰ ਟੈਂਸਰ ਵਿੱਚ ਬਦਲ ਕੇ ਮਾਡਲ ਵਿੱਚ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਲੌਜਿਟ ਪ੍ਰਾਪਤ ਹੋ ਸਕਣ।

ਲੂਪ ਪ੍ਰੰਪਟ ਦੇ ਹਰ ਟੋਕਨ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਦਾ ਹੈ, ਲੌਜਿਟ ਪ੍ਰੋਸੈਸਰ ਨੂੰ ਅਪਡੇਟ ਕਰਦਾ ਹੈ ਅਤੇ ਅਗਲੇ ਟੋਕਨ ਜਨਰੇਸ਼ਨ ਲਈ ਤਿਆਰੀ ਕਰਦਾ ਹੈ।

## ਕਦਮ 6: ਇੰਫਰੈਂਸ

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

ਇੰਫਰੈਂਸ ਲੂਪ ਵਿੱਚ, ਅਸੀਂ ਟੋਕਨਾਂ ਨੂੰ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਜਨਰੇਟ ਕਰਦੇ ਹਾਂ ਜਦ ਤੱਕ ਅਸੀਂ ਚਾਹੀਦੀ ਲੰਬਾਈ ਤੱਕ ਨਹੀਂ ਪਹੁੰਚ ਜਾਂਦੇ ਜਾਂ ਅੰਤ-ਅਨੁਕ੍ਰਮ ਟੋਕਨ ਨਹੀਂ ਮਿਲਦਾ। ਅਗਲਾ ਟੋਕਨ ਟੈਂਸਰ ਵਿੱਚ ਬਦਲ ਕੇ ਮਾਡਲ ਵਿੱਚ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ, ਜਦਕਿ ਲੌਜਿਟਸ ਨੂੰ ਜੁਰਮਾਨੇ ਅਤੇ ਸੈਂਪਲਿੰਗ ਲਾਗੂ ਕਰਨ ਲਈ ਪ੍ਰੋਸੈਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਫਿਰ ਅਗਲਾ ਟੋਕਨ ਸੈਂਪਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਡੀਕੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਲੜੀ ਵਿੱਚ ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ।

ਦੋਹਰਾਏ ਗਏ ਲਿਖਤ ਨੂੰ ਰੋਕਣ ਲਈ, `repeat_last_n` and `repeat_penalty` ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਜੁਰਮਾਨਾ ਲਗਾਇਆ ਜਾਂਦਾ ਹੈ।

ਅੰਤ ਵਿੱਚ, ਜਨਰੇਟ ਕੀਤੀ ਗਈ ਲਿਖਤ ਜਿਵੇਂ ਹੀ ਡੀਕੋਡ ਹੁੰਦੀ ਹੈ, ਪ੍ਰਿੰਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਇਸ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਸਟ੍ਰੀਮਿੰਗ ਆਉਟਪੁੱਟ ਮਿਲਦੀ ਹੈ।

## ਕਦਮ 7: ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ

ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
cargo run --release
```

ਇਸ ਨਾਲ Phi-3 ਮਾਡਲ ਦੁਆਰਾ ਬਣਾਇਆ ਗਿਆ ਆਈਸ ਹਾਕੀ ਬਾਰੇ ਇੱਕ ਹਾਈਕੂ ਪ੍ਰਿੰਟ ਹੋਵੇਗਾ। ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ:

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

ਇਹ ਕਦਮਾਂ ਨੂੰ ਫਾਲੋ ਕਰਕੇ, ਅਸੀਂ Phi-3 ਮਾਡਲ ਨਾਲ Rust ਅਤੇ Candle ਦੀ ਵਰਤੋਂ ਕਰਕੇ 100 ਲਾਈਨਾਂ ਤੋਂ ਘੱਟ ਕੋਡ ਵਿੱਚ ਲਿਖਤ ਜਨਰੇਸ਼ਨ ਕਰ ਸਕਦੇ ਹਾਂ। ਕੋਡ ਮਾਡਲ ਲੋਡਿੰਗ, ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਇੰਫਰੈਂਸ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ, ਟੈਂਸਰਾਂ ਅਤੇ ਲੌਜਿਟ ਪ੍ਰੋਸੈਸਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਪ੍ਰੰਪਟ ਦੇ ਆਧਾਰ 'ਤੇ ਸਮਝਦਾਰ ਲਿਖਤ ਬਣਾਉਂਦਾ ਹੈ।

ਇਹ ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ Windows, Linux ਅਤੇ Mac OS 'ਤੇ ਚਲ ਸਕਦਾ ਹੈ। ਰਸਟ ਦੀ ਪੋਰਟੇਬਿਲਿਟੀ ਦੇ ਕਾਰਨ, ਕੋਡ ਨੂੰ ਮੋਬਾਈਲ ਐਪਸ ਦੇ ਅੰਦਰ ਚਲਾਉਣ ਵਾਲੀ ਲਾਇਬ੍ਰੇਰੀ ਵਜੋਂ ਵੀ ਅਡੈਪਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ (ਅਸੀਂ ਕਨਸੋਲ ਐਪਸ ਉੱਥੇ ਨਹੀਂ ਚਲਾ ਸਕਦੇ, ਆਖ਼ਰਕਾਰ)।

## ਪਰਿਸ਼ਿਸ਼ਟ: ਪੂਰਾ ਕੋਡ

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

ਨੋਟ: aarch64 Linux ਜਾਂ aarch64 Windows 'ਤੇ ਇਹ ਕੋਡ ਚਲਾਉਣ ਲਈ, `.cargo/config` ਨਾਮ ਦੀ ਇੱਕ ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੋਵੇ:

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

> ਤੁਸੀਂ ਅਧਿਕ ਉਦਾਹਰਨਾਂ ਲਈ ਅਧਿਕਾਰਕ [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ਰਿਪੋਜ਼ਟਰੀ ਵੇਖ ਸਕਦੇ ਹੋ, ਜਿਸ ਵਿੱਚ Rust ਅਤੇ Candle ਨਾਲ Phi-3 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਦੇ ਹੋਰ ਤਰੀਕੇ ਅਤੇ ਇੰਫਰੈਂਸ ਦੇ ਵਿਕਲਪ ਹਨ।

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।