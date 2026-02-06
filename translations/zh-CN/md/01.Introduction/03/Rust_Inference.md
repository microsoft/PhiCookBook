# 使用 Rust 进行跨平台推理

本教程将引导我们使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 进行推理。与其他编程语言相比，使用 Rust 进行推理有诸多优势。Rust 以其高性能著称，性能可与 C 和 C++ 相媲美，这使其成为计算密集型推理任务的理想选择。特别是，Rust 通过零成本抽象和高效的内存管理（无垃圾回收开销）实现了这一点。Rust 的跨平台能力使得开发的代码可以在包括 Windows、macOS 和 Linux 以及移动操作系统在内的多种操作系统上运行，而无需对代码库进行重大修改。

要跟随本教程，前提是先[安装 Rust](https://www.rust-lang.org/tools/install)，其中包含 Rust 编译器和 Rust 包管理器 Cargo。

## 第一步：创建新的 Rust 项目

在终端中运行以下命令以创建一个新的 Rust 项目：

```bash
cargo new phi-console-app
```

这将生成一个初始项目结构，包含一个 `Cargo.toml` 文件和一个包含 `main.rs` 文件的 `src` 目录。

接下来，我们将在 `Cargo.toml` 文件中添加依赖项——即 `candle`、`hf-hub` 和 `tokenizers` crates：

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

在 main.rs 文件中，我们将设置推理的初始参数。为了简化，所有参数都将硬编码，但我们可以根据需要进行修改。

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
- **top_p**：用于核采样，限制每步考虑的 token 数量。
- **repeat_last_n**：控制用于惩罚以防止重复序列的 token 数量。
- **repeat_penalty**：惩罚值，用于抑制重复 token。
- **seed**：随机种子（为了更好的可复现性，可以使用常量值）。
- **prompt**：用于开始生成的初始提示文本。注意，我们让模型生成一首关于冰球的俳句，并用特殊标记包裹以指示对话中的用户和助手部分。模型随后会用一首俳句完成提示。
- **device**：本例中使用 CPU 进行计算。Candle 也支持使用 CUDA 和 Metal 在 GPU 上运行。

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

我们使用 `hf_hub` API 从 Hugging Face 模型库下载模型和分词器文件。`gguf` 文件包含量化后的模型权重，而 `tokenizer.json` 文件用于对输入文本进行分词。模型下载后会被缓存，因此首次执行会较慢（因为需要下载 2.4GB 的模型），但后续执行会更快。

## 第四步：加载模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我们将量化后的模型权重加载到内存中，并初始化 Phi-3 模型。此步骤涉及从 `gguf` 文件读取模型权重，并在指定设备（本例为 CPU）上设置模型以进行推理。

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

这一步中，我们对输入提示进行分词，并将其转换为 token ID 序列以准备推理。我们还初始化 `LogitsProcessor`，根据给定的 `temperature` 和 `top_p` 值处理采样过程（词汇表上的概率分布）。每个 token 被转换为张量并传入模型以获取 logits。

循环处理提示中的每个 token，更新 logits 处理器并为下一个 token 的生成做准备。

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

在推理循环中，我们逐个生成 token，直到达到期望的生成长度或遇到序列结束 token。下一个 token 被转换为张量并传入模型，同时对 logits 进行处理以应用惩罚和采样。然后对下一个 token 进行采样、解码并追加到序列中。

为了避免文本重复，根据 `repeat_last_n` 和 `repeat_penalty` 参数对重复 token 施加惩罚。

最后，生成的文本在解码时被打印出来，确保实时流式输出。

## 第七步：运行应用程序

在终端中执行以下命令以运行应用程序：

```bash
cargo run --release
```

这将打印由 Phi-3 模型生成的一首关于冰球的俳句。类似于：

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

## 结论

通过以上步骤，我们可以使用 Rust 和 Candle 在不到 100 行代码中完成基于 Phi-3 模型的文本生成。代码涵盖了模型加载、分词和推理，利用张量和 logits 处理生成基于输入提示的连贯文本。

该控制台应用程序可在 Windows、Linux 和 Mac OS 上运行。由于 Rust 的可移植性，代码也可以改编为在移动应用中运行的库（毕竟我们不能在移动端运行控制台应用）。

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

注意：若要在 aarch64 Linux 或 aarch64 Windows 上运行此代码，请添加一个名为 `.cargo/config` 的文件，内容如下：

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

> 你可以访问官方的 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 仓库，查看更多关于如何使用 Rust 和 Candle 运行 Phi-3 模型的示例，包括推理的替代方法。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。