<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:26:15+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "tw"
}
-->
# 使用 Rust 進行跨平台推論

本教學將帶領我們使用 Rust 以及 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 來執行推論。與其他程式語言相比，使用 Rust 進行推論有多項優勢。Rust 以其高效能著稱，效能可媲美 C 和 C++，因此非常適合計算密集的推論任務。這主要得益於其零成本抽象和高效的記憶體管理，且沒有垃圾回收的負擔。Rust 的跨平台能力使得開發的程式碼能在多種作業系統上運行，包括 Windows、macOS 和 Linux，以及行動作業系統，且不需對程式碼做太多修改。

要跟隨本教學，前提是先[安裝 Rust](https://www.rust-lang.org/tools/install)，其中包含 Rust 編譯器和 Rust 套件管理工具 Cargo。

## 第一步：建立新的 Rust 專案

在終端機中執行以下指令來建立新的 Rust 專案：

```bash
cargo new phi-console-app
```

這會產生一個初始的專案結構，包含 `Cargo.toml` 檔案和一個 `src` 目錄，裡面有 `main.rs` 檔案。

接著，我們會將所需的依賴套件，也就是 `candle`、`hf-hub` 和 `tokenizers` crates，加入到 `Cargo.toml` 檔案中：

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

## 第二步：設定基本參數

在 `main.rs` 檔案中，我們會設定推論的初始參數。為了簡化起見，這些參數都會硬編碼，但日後可以根據需求調整。

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

- **temperature**：控制取樣過程的隨機程度。
- **sample_len**：指定生成文字的最大長度。
- **top_p**：用於 nucleus 取樣，限制每一步考慮的詞彙數量。
- **repeat_last_n**：控制考慮用來施加懲罰以避免重複序列的詞彙數量。
- **repeat_penalty**：用來抑制重複詞彙的懲罰值。
- **seed**：隨機種子（可使用固定值以提高可重現性）。
- **prompt**：生成的起始提示文字。注意，我們請模型生成一首關於冰球的俳句，並用特殊標記包裹以區分使用者和助理的對話部分。模型會接著完成這個俳句。
- **device**：本範例使用 CPU 進行計算。Candle 也支援使用 CUDA 和 Metal 在 GPU 上運行。

## 第三步：下載/準備模型與分詞器

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

我們使用 `hf_hub` API 從 Hugging Face 模型庫下載模型和分詞器檔案。`gguf` 檔案包含量化後的模型權重，而 `tokenizer.json` 用於將輸入文字分詞。下載後模型會被快取，因此第一次執行會較慢（因為要下載約 2.4GB 的模型），之後執行速度會更快。

## 第四步：載入模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化後的模型權重載入記憶體，並初始化 Phi-3 模型。這一步驟會從 `gguf` 檔案讀取模型權重，並在指定的裝置（本例為 CPU）上設定模型以供推論。

## 第五步：處理提示並準備推論

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

這一步，我們將輸入的提示文字進行分詞，並轉換成詞彙 ID 序列以準備推論。我們也會初始化 `LogitsProcessor`，根據設定的 `temperature` 和 `top_p` 來處理取樣過程（詞彙的機率分布）。每個詞彙會被轉成張量並送入模型以取得 logits。

迴圈會處理提示中的每個詞彙，更新 logits 處理器並準備生成下一個詞彙。

## 第六步：推論

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

在推論迴圈中，我們會一個一個生成詞彙，直到達到指定的生成長度或遇到結束序列標記。下一個詞彙會被轉成張量並送入模型，logits 會被處理以施加懲罰和取樣。接著抽樣出下一個詞彙，解碼後加入序列中。

為避免重複文字，會根據 `repeat_last_n` 和 `repeat_penalty` 參數對重複詞彙施加懲罰。

最後，生成的文字會在解碼時即時輸出，確保串流式的即時顯示。

## 第七步：執行應用程式

在終端機中執行以下指令來執行應用程式：

```bash
cargo run --release
```

這會印出由 Phi-3 模型生成的關於冰球的俳句。可能會是類似以下的內容：

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

或是

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 結論

透過以上步驟，我們可以用不到 100 行的程式碼，利用 Rust 和 Candle 進行 Phi-3 模型的文字生成。程式碼涵蓋模型載入、分詞和推論，並利用張量與 logits 處理來根據輸入提示生成連貫的文字。

這個命令列應用程式可以在 Windows、Linux 和 Mac OS 上執行。由於 Rust 的可攜性，程式碼也能改寫成可在行動裝置應用程式中運行的函式庫（畢竟行動裝置無法直接執行命令列應用程式）。

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

注意：若要在 aarch64 Linux 或 aarch64 Windows 上執行此程式，請新增一個名為 `.cargo/config` 的檔案，內容如下：

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

> 你可以造訪官方的 [Candle 範例](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 倉庫，查看更多如何使用 Rust 和 Candle 搭配 Phi-3 模型的範例，包括其他推論方法。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。