<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-07T14:40:43+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "zh"
}
-->
# 使用 Rust 实现跨平台推理

本教程将引导我们使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 进行推理。与其他编程语言相比，使用 Rust 进行推理有许多优势。Rust 以其高性能著称，可媲美 C 和 C++。这使其成为计算密集型推理任务的理想选择。特别是，这得益于零开销抽象和高效的内存管理，没有垃圾回收的负担。Rust 的跨平台特性使得开发的代码能够在多个操作系统上运行，包括 Windows、macOS 和 Linux，以及移动操作系统，而无需对代码库进行重大修改。

本教程的前提是需要先[安装 Rust](https://www.rust-lang.org/tools/install)，其中包括 Rust 编译器和包管理工具 Cargo。

## 第一步：创建新的 Rust 项目

在终端中运行以下命令来创建一个新的 Rust 项目：

```bash
cargo new phi-console-app
```

这会生成一个初始项目结构，其中包含一个 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## 第二步：配置基本参数

在 main.rs 文件中，我们将设置推理的初始参数。为了简化，所有参数都会硬编码，但我们可以根据需要进行修改。

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

- **temperature**：控制采样过程的随机性。
- **sample_len**：指定生成文本的最大长度。
- **top_p**：用于核采样，限制每一步考虑的标记数量。
- **repeat_last_n**：控制考虑用于惩罚以防止重复序列的标记数量。
- **repeat_penalty**：用于惩罚重复标记的值。
- **seed**：随机种子（为了更好的可复现性，我们可以使用固定值）。
- **prompt**：用于生成的初始提示文本。注意，我们要求模型生成一首关于冰球的俳句，并且用特殊标记将对话中的用户和助手部分包裹起来。模型随后会完成这个提示，生成一首俳句。
- **device**：本例中使用 CPU 进行计算。Candle 也支持在 GPU 上运行，支持 CUDA 和 Metal。

## 第三步：下载/准备模型和分词器

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

我们使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 文件来对输入文本进行分词。模型下载完成后会被缓存，因此第一次执行会比较慢（因为要下载 2.4GB 的模型），但之后的执行会更快。

## 第四步：加载模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我们将量化后的模型权重加载到内存中，并初始化 Phi-3 模型。这一步包括从 `gguf` 文件中读取模型权重，并为指定设备（本例为 CPU）设置模型以进行推理。

## 第五步：处理提示并准备推理

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

这一步中，我们将输入提示进行分词，并将其转换为一系列标记 ID 以准备推理。同时初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 的值。每个标记被转换成张量并传入模型以获取 logits。

循环处理提示中的每个标记，更新 logits 处理器并为生成下一个标记做准备。

## 第六步：推理

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

在推理循环中，我们逐个生成标记，直到达到预定的生成长度或遇到结束序列标记。下一个标记被转换为张量并传入模型，同时对 logits 进行处理以应用惩罚和采样。然后采样出下一个标记，对其解码并追加到序列中。
为了避免重复文本，会根据 `repeat_last_n` and `repeat_penalty` 参数对重复标记施加惩罚。

最终，生成的文本会随着解码实时打印，确保流式实时输出。

## 第七步：运行应用程序

在终端中执行以下命令运行应用程序：

```bash
cargo run --release
```

这将打印由 Phi-3 模型生成的一首关于冰球的俳句。类似于：

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

## 结论

通过以上步骤，我们可以用不到 100 行代码，利用 Rust 和 Candle 使用 Phi-3 模型进行文本生成。代码涵盖了模型加载、分词和推理，利用张量和 logits 处理生成基于输入提示的连贯文本。

该控制台应用可在 Windows、Linux 和 macOS 上运行。由于 Rust 的可移植性，代码也可以改编为在移动应用中运行的库（毕竟控制台应用无法在移动端运行）。

## 附录：完整代码

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

注意：为了在 aarch64 Linux 或 aarch64 Windows 上运行此代码，需要添加一个名为 `.cargo/config` 的文件，内容如下：

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

> 你可以访问官方的 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 仓库，获取更多关于如何使用 Rust 和 Candle 调用 Phi-3 模型的示例，包括推理的替代方案。

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。