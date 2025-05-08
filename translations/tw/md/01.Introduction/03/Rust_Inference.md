<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-08T06:03:23+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "tw"
}
-->
# Cross-platform inference with Rust

這個教學會帶領我們使用 Rust 以及 HuggingFace 的 [Candle ML framework](https://github.com/huggingface/candle) 來進行推論。用 Rust 來做推論有很多優點，尤其是跟其他程式語言相比。Rust 以高效能著稱，效能可媲美 C 和 C++。這讓它成為推論任務的絕佳選擇，因為這類任務通常運算量很大。特別是因為 Rust 採用零成本抽象和高效的記憶體管理，沒有垃圾回收的負擔。Rust 的跨平台能力讓我們能夠開發能在多種作業系統上運行的程式碼，包括 Windows、macOS、Linux，以及行動作業系統，而且不需要對程式碼庫做太多修改。

跟著這個教學之前，需要先 [安裝 Rust](https://www.rust-lang.org/tools/install)，裡面包含 Rust 編譯器和 Rust 的套件管理工具 Cargo。

## Step 1: Create a New Rust Project

要建立新的 Rust 專案，可以在終端機執行以下指令：

```bash
cargo new phi-console-app
```

這會產生一個初始專案結構，裡面包含 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

在 main.rs 檔案裡，我們會設定推論的初始參數。為了簡化起見，這些參數都會硬編碼，但日後可以依需求修改。

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
- **top_p**：用於 nucleus 取樣，限制每一步考慮的 token 數量。
- **repeat_last_n**：控制用來套用懲罰以避免重複序列的 token 數量。
- **repeat_penalty**：懲罰值，用來抑制重複的 token。
- **seed**：隨機種子（我們可以用固定值以提高可重現性）。
- **prompt**：生成的起始提示文字。注意我們請模型生成一首關於冰球的俳句，並用特殊 token 標示使用者和助理的對話部分。模型會接著完成這個俳句。
- **device**：這個範例中使用 CPU 進行運算。Candle 也支援使用 CUDA 和 Metal 在 GPU 上運行。

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

我們使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 檔案來對輸入文字做分詞。模型下載後會被快取，所以第一次執行會比較慢（因為要下載 2.4GB 的模型），但之後執行就會快很多。

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化過的模型權重載入記憶體，並初始化 Phi-3 模型。這步驟會從 `gguf` 檔案讀取模型權重，並設定模型在指定裝置（這裡是 CPU）上進行推論。

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

這一步會將輸入的 prompt 做分詞，並轉換成 token ID 序列以準備推論。我們也會初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 的數值。每個 token 都會被轉成 tensor，並送入模型計算 logits。

迴圈會處理 prompt 中的每個 token，更新 logits 處理器，並為下一個 token 的生成做準備。

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

在推論迴圈中，我們會一個一個生成 token，直到達到設定的 sample 長度或遇到結束序列 token。下一個 token 會被轉成 tensor 並送入模型，logits 會經過處理以套用懲罰和取樣。接著下一個 token 會被取樣、解碼並加到序列中。

為避免重複文字，會根據 `repeat_last_n` and `repeat_penalty` 參數對重複 token 施加懲罰。

最後，生成的文字會在解碼後即時印出，確保串流即時輸出。

## Step 7: Run the Application

要執行這個應用程式，可以在終端機執行以下指令：

```bash
cargo run --release
```

這會印出一首由 Phi-3 模型生成的冰球俳句，大概像是：

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

## Conclusion

照著這些步驟，我們可以用不到 100 行的程式碼，利用 Rust 和 Candle 執行 Phi-3 模型的文字生成。程式碼負責模型載入、分詞和推論，利用 tensor 和 logits 處理，根據輸入 prompt 生成連貫的文字。

這個主控台應用程式能在 Windows、Linux 和 Mac OS 上執行。因為 Rust 的可攜性，程式碼也能改寫成函式庫，在行動裝置的應用程式中使用（畢竟行動裝置不能直接執行主控台程式）。

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

注意：如果要在 aarch64 Linux 或 aarch64 Windows 上執行這段程式碼，請新增一個名為 `.cargo/config` 的檔案，內容如下：

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

> 你也可以造訪官方的 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 倉庫，裡面有更多如何用 Rust 和 Candle 使用 Phi-3 模型的範例，包括其他推論方法。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。