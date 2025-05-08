<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-08T06:02:58+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "hk"
}
-->
# Cross-platform inference with Rust

呢個教學會帶你用 Rust 同 HuggingFace 嘅 [Candle ML framework](https://github.com/huggingface/candle) 去做推理。用 Rust 做推理有好多好處，尤其係比起其他編程語言。Rust 以高效能聞名，媲美 C 同 C++，所以好適合處理計算量大嘅推理任務。呢個主要得益於佢嘅零成本抽象同高效嘅記憶體管理，無垃圾收集嘅開銷。Rust 嘅跨平台能力可以令你嘅程式碼喺唔同操作系統上運行，包括 Windows、macOS 同 Linux，甚至係手機系統，都唔使大改動。

跟住呢個教學之前，你要先 [安裝 Rust](https://www.rust-lang.org/tools/install)，入面包括 Rust 編譯器同 Cargo，Rust 嘅套件管理工具。

## Step 1: Create a New Rust Project

喺終端機輸入以下指令去建立一個新嘅 Rust 專案：

```bash
cargo new phi-console-app
```

呢個會生成一個初始嘅專案結構，有一個 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` 檔案：

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

喺 main.rs 檔案入面，我哋會設定推理嘅初始參數。為簡單起見，呢啲參數會寫死喺程式入面，但你可以按需要修改。

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

- **temperature**：控制抽樣嘅隨機程度。
- **sample_len**：指定生成文字嘅最大長度。
- **top_p**：用於 nucleus 抽樣，限制每一步考慮嘅 token 數量。
- **repeat_last_n**：控制考慮用嚟懲罰重複序列嘅 token 數量。
- **repeat_penalty**：用嚟懲罰重複 token 嘅數值。
- **seed**：隨機種子（用固定值可以令結果更可重現）。
- **prompt**：用嚟開始生成嘅初始提示文字。注意我哋叫模型生成一首關於冰球嘅俳句，並用特殊 token 包住用戶同助手嘅對話部分。模型會跟住呢個提示生成俳句。
- **device**：呢個例子用 CPU 做運算。Candle 亦支持用 CUDA 同 Metal 喺 GPU 上運行。

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

我哋用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 檔案去將輸入文字拆成 token。下載完模型會快啲，因為模型會快取喺本地，第一次執行會慢啲（要下載 2.4GB 模型），之後就快好多。

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我哋會將量化後嘅模型權重讀入記憶體，初始化 Phi-3 模型。呢步係從 `gguf` 檔案讀取模型權重，並喺指定裝置（呢度係 CPU）上準備好模型做推理。

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

呢一步，我哋會將輸入嘅提示文字 tokenize，轉成 token ID 序列，準備做推理。亦會初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 嘅值。每個 token 會轉成 tensor，然後傳入模型拎 logits。

個循環會處理提示入面每個 token，更新 logits 處理器，準備下一個 token 嘅生成。

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

喺推理循環入面，我哋會一個一個咁生成 token，直到達到設定嘅 sample_len 或者遇到結束序列 token。下一個 token 會轉成 tensor，傳入模型，logits 會被處理用嚟做懲罰同抽樣。之後抽樣出下一個 token，解碼，加入到序列度。

為咗避免文字重複，會根據 `repeat_last_n` and `repeat_penalty` 參數對重複嘅 token 施加懲罰。

最後，生成嘅文字會邊解碼邊即時輸出，確保有串流式嘅實時顯示。

## Step 7: Run the Application

喺終端機執行以下指令去跑呢個應用程式：

```bash
cargo run --release
```

呢個會打印一首 Phi-3 模型生成嘅冰球俳句。可能係咁：

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

或者係咁：

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

跟住呢啲步驟，我哋可以用 Rust 同 Candle 喺 100 行程式碼以內完成 Phi-3 模型嘅文字生成。程式碼會處理模型載入、tokenize 同推理，利用 tensor 同 logits 處理去生成根據提示嘅連貫文字。

呢個 console 應用可以喺 Windows、Linux 同 Mac OS 運行。因為 Rust 嘅可攜性，程式碼亦可以改寫成 library，喺手機 app 入面用（畢竟 console app 喺手機度跑唔到）。

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

注意：如果你想喺 aarch64 Linux 或 aarch64 Windows 跑呢段程式碼，記得加一個叫 `.cargo/config` 嘅檔案，內容如下：

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

> 你可以去官方 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository 睇多啲用 Rust 同 Candle 搭配 Phi-3 模型嘅例子，包括其他推理方法。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋致力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件嘅母語版本應視為權威來源。對於重要資訊，建議使用專業人手翻譯。對於因使用本翻譯而引致嘅任何誤解或誤釋，我哋概不負責。