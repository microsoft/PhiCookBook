<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2fa1ead890e358cc560ed4f9b3cf219a",
  "translation_date": "2025-04-04T17:53:40+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "hk"
}
-->
# 使用 Rust 跨平台推理

本教程會教大家如何使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 進行推理。使用 Rust 進行推理有多項優勢，特別是與其他程式語言相比。Rust 以高效能著稱，其效能可與 C 和 C++ 媲美，這使得它非常適合處理計算密集型的推理任務。這主要得益於 Rust 的零成本抽象和高效的記憶體管理，完全沒有垃圾回收的負擔。此外，Rust 的跨平台能力讓開發者可以編寫可在多個操作系統（如 Windows、macOS、Linux，以及移動操作系統）上運行的程式碼，且不需要對代碼進行大幅修改。

在開始本教程之前，需先[安裝 Rust](https://www.rust-lang.org/tools/install)，包括 Rust 編譯器和套件管理工具 Cargo。

## 步驟 1：建立新的 Rust 專案

在終端中執行以下命令以建立新的 Rust 專案：

```bash
cargo new phi-console-app
```

這會生成一個初始的專案結構，包括 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## 步驟 2：設定基本參數

在 main.rs 檔案中，我們將設置推理的初始參數。為了簡化，我們會直接硬編碼這些參數，但可以根據需求進行修改。

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
- **sample_len**：指定生成文本的最大長度。
- **top_p**：用於核採樣，限制每一步考慮的 token 數量。
- **repeat_last_n**：控制考慮用來應用懲罰以防止重複序列的 token 數量。
- **repeat_penalty**：懲罰值，用於降低重複 token 的概率。
- **seed**：隨機種子（可以使用固定值來提高可重現性）。
- **prompt**：生成的初始提示文本。注意，我們要求模型生成一首關於冰球的俳句，並用特殊的 token 包裹提示，以標示用戶和助手的對話部分。模型會根據提示完成俳句。
- **device**：在此範例中，我們使用 CPU 進行計算。Candle 支援使用 CUDA 和 Metal 在 GPU 上運行。

## 步驟 3：下載/準備模型和 Tokenizer

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

我們使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 檔案來對輸入文本進行分詞。模型下載後會被緩存，因此首次執行可能會較慢（因為需要下載 2.4GB 的模型），但之後的執行速度會更快。

## 步驟 4：載入模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化的模型權重載入記憶體並初始化 Phi-3 模型。這一步包括從 `gguf` 檔案中讀取模型權重並設定模型在指定設備（此例為 CPU）上的推理。

## 步驟 5：處理提示並準備推理

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

在這一步中，我們將輸入提示進行分詞並準備推理，將其轉換為 token ID 的序列。我們還初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 的值。每個 token 都會轉換為 tensor，並通過模型獲取 logits。

迴圈會處理提示中的每個 token，更新 logits 處理器並準備生成下一個 token。

## 步驟 6：推理

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

在推理迴圈中，我們逐個生成 token，直到達到所需的樣本長度或遇到序列結束的 token。下一個 token 會被轉換為 tensor 並通過模型處理，同時 logits 被處理以應用懲罰和採樣。接著，下一個 token 被採樣、解碼並添加到序列中。
為避免重複文本，根據 `repeat_last_n` and `repeat_penalty` 參數對重複的 token 應用懲罰。

最後，生成的文本會被解碼並即時打印出來。

## 步驟 7：運行應用程式

在終端中執行以下命令以運行應用程式：

```bash
cargo run --release
```

這應該會打印出由 Phi-3 模型生成的關於冰球的俳句，例如：

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

或者

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 結論

按照這些步驟，我們可以使用 Rust 和 Candle 在不到 100 行代碼中完成使用 Phi-3 模型的文本生成。代碼處理了模型載入、分詞和推理，利用 tensor 和 logits 處理生成基於輸入提示的連貫文本。

這個控制台應用程式可以在 Windows、Linux 和 macOS 上運行。由於 Rust 的可移植性，代碼也可以改編成在移動應用程式中運行的函式庫（畢竟我們無法在移動端運行控制台應用程式）。

## 附錄：完整代碼

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

注意：若要在 aarch64 Linux 或 aarch64 Windows 上運行此代碼，需新增名為 `.cargo/config` 的檔案，內容如下：

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

> 你可以訪問官方 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 儲存庫，了解更多使用 Phi-3 模型與 Rust 和 Candle 的範例，包括推理的替代方法。

**免責聲明**:  
本文件使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。