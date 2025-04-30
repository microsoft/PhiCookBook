<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2fa1ead890e358cc560ed4f9b3cf219a",
  "translation_date": "2025-04-04T06:02:47+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "tw"
}
-->
# 使用 Rust 進行跨平台推論

本教學將引導我們使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 進行推論。使用 Rust 進行推論具有許多優勢，尤其是與其他程式語言相比。Rust 以高效能著稱，其效能可媲美 C 和 C++，使其成為執行計算密集型推論任務的絕佳選擇。這得益於零成本抽象和高效的記憶體管理，且無需垃圾回收的額外負擔。Rust 的跨平台能力使得開發的程式碼可以在 Windows、macOS 和 Linux 等各種作業系統以及行動作業系統上執行，而不需對程式碼庫進行重大修改。

在開始學習本教學之前，請先 [安裝 Rust](https://www.rust-lang.org/tools/install)，其中包括 Rust 編譯器和套件管理工具 Cargo。

## 步驟 1：建立新的 Rust 專案

在終端機中執行以下指令以建立新的 Rust 專案：

```bash
cargo new phi-console-app
```

此指令會生成一個初始的專案結構，包含 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` 文件：

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

## 步驟 2：設定基本參數

在 main.rs 文件中，我們將設定推論所需的初始參數。為了簡化操作，這些參數都將被硬編碼，但可以根據需求進行修改。

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

- **temperature**：控制採樣過程的隨機性。
- **sample_len**：指定生成文字的最大長度。
- **top_p**：用於核採樣，限制每一步中考慮的 token 數量。
- **repeat_last_n**：控制用於懲罰重複序列的 token 數量。
- **repeat_penalty**：懲罰值，用於避免重複的 token。
- **seed**：隨機種子（為了更好的可重現性，可以使用固定值）。
- **prompt**：生成的初始提示文字。注意，我們要求模型生成一首關於冰球的俳句，並使用特殊 token 標示對話中使用者和助手的部分，模型將完成提示文字並生成俳句。
- **device**：此範例中使用 CPU 進行運算。Candle 也支援使用 CUDA 和 Metal 在 GPU 上執行。

## 步驟 3：下載/準備模型與分詞器

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

我們使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 文件來對輸入文字進行分詞。模型下載後會被快取，因此首次執行可能較慢（因為需要下載 2.4GB 的模型），但後續執行會更快。

## 步驟 4：載入模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化的模型權重載入記憶體並初始化 Phi-3 模型。此步驟包括從 `gguf` 文件讀取模型權重並設置模型以便在指定的設備（此範例中為 CPU）上進行推論。

## 步驟 5：處理提示文字並準備推論

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

在此步驟中，我們將輸入的提示文字進行分詞並準備推論，將其轉換為 token ID 的序列。我們還初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 的值。每個 token 會被轉換為張量並通過模型以獲得 logits。

迴圈會處理提示文字中的每個 token，更新 logits 處理器並為下一個 token 的生成做好準備。

## 步驟 6：推論

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

在推論迴圈中，我們逐一生成 token，直到達到預定的樣本長度或遇到序列結束的 token。下一個 token 會被轉換為張量並通過模型處理，logits 則會被應用懲罰與採樣。接著，下一個 token 會被抽樣、解碼並附加到序列中。

為了避免重複的文字，會根據 `repeat_last_n` and `repeat_penalty` 參數對重複的 token 應用懲罰。

最後，生成的文字會在解碼後即時輸出。

## 步驟 7：執行應用程式

在終端機中執行以下指令以執行應用程式：

```bash
cargo run --release
```

這應該會生成一首由 Phi-3 模型創作的冰球俳句，例如：

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

或

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 結論

通過以上步驟，我們可以使用 Rust 和 Candle 在不到 100 行程式碼中實現使用 Phi-3 模型進行文字生成。程式碼負責模型載入、分詞和推論，並利用張量和 logits 處理生成基於輸入提示的連貫文字。

此控制台應用程式可在 Windows、Linux 和 macOS 上執行。由於 Rust 的可移植性，程式碼也可以改寫為可在行動應用程式中執行的函式庫（畢竟我們無法在行動裝置上執行控制台應用程式）。

## 附錄：完整程式碼

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

注意：若要在 aarch64 Linux 或 aarch64 Windows 上執行此程式碼，請新增一個名為 `.cargo/config` 的文件，內容如下：

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

> 您可以造訪官方 [Candle 範例](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 資料庫，了解更多使用 Phi-3 模型與 Rust 和 Candle 的範例，包括推論的替代方法。

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具有權威性的來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。