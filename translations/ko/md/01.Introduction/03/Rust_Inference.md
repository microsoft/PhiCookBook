<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-08T06:03:35+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ko"
}
-->
# Cross-platform inference with Rust

이 튜토리얼에서는 Rust와 HuggingFace의 [Candle ML framework](https://github.com/huggingface/candle)를 사용해 추론을 수행하는 과정을 안내합니다. Rust를 사용한 추론은 특히 다른 프로그래밍 언어와 비교했을 때 여러 장점이 있습니다. Rust는 C와 C++에 필적하는 높은 성능으로 알려져 있어, 계산 집약적인 추론 작업에 매우 적합합니다. 특히, 제로 코스트 추상화와 가비지 컬렉션 오버헤드가 없는 효율적인 메모리 관리 덕분입니다. Rust의 크로스 플랫폼 기능은 Windows, macOS, Linux뿐 아니라 모바일 운영체제에서도 코드 변경 없이 실행 가능한 코드를 개발할 수 있게 합니다.

이 튜토리얼을 따라가기 위해서는 Rust 컴파일러와 패키지 매니저 Cargo가 포함된 [Rust 설치](https://www.rust-lang.org/tools/install)가 선행되어야 합니다.

## Step 1: 새 Rust 프로젝트 생성

새 Rust 프로젝트를 생성하려면 터미널에서 다음 명령어를 실행하세요:

```bash
cargo new phi-console-app
```

이 명령은 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` 파일이 포함된 초기 프로젝트 구조를 생성합니다:

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

## Step 2: 기본 파라미터 설정

main.rs 파일 안에서 추론에 필요한 초기 파라미터를 설정합니다. 이해를 돕기 위해 모두 하드코딩되어 있지만 필요에 따라 수정할 수 있습니다.

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

- **temperature**: 샘플링 과정의 무작위성을 제어합니다.
- **sample_len**: 생성할 텍스트의 최대 길이를 지정합니다.
- **top_p**: 핵심 샘플링(nucleus sampling)에 사용되며, 각 단계에서 고려할 토큰 수를 제한합니다.
- **repeat_last_n**: 반복적인 문장 생성을 방지하기 위해 페널티를 적용할 토큰 수를 제어합니다.
- **repeat_penalty**: 반복 토큰에 부여하는 페널티 값입니다.
- **seed**: 무작위 시드 값으로, 재현성을 높이기 위해 상수값을 사용할 수 있습니다.
- **prompt**: 텍스트 생성을 시작할 초기 프롬프트입니다. 여기서는 아이스하키에 관한 하이쿠를 생성하도록 모델에 요청하며, 대화의 사용자와 어시스턴트 부분을 구분하는 특수 토큰으로 감싸져 있습니다. 모델은 이 프롬프트를 바탕으로 하이쿠를 완성합니다.
- **device**: 이 예제에서는 CPU를 사용합니다. Candle은 CUDA와 Metal을 지원하여 GPU에서도 실행할 수 있습니다.

## Step 3: 모델과 토크나이저 다운로드/준비

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

`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 파일은 입력 텍스트를 토크나이징하는 데 사용됩니다. 모델을 다운로드하면 캐시에 저장되므로, 첫 실행 시에는 2.4GB 모델 다운로드로 인해 느리지만 이후 실행은 더 빨라집니다.

## Step 4: 모델 로드

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

양자화된 모델 가중치를 메모리에 로드하고 Phi-3 모델을 초기화합니다. 이 단계에서는 `gguf` 파일에서 모델 가중치를 읽어와 지정한 디바이스(CPU)에서 추론할 수 있도록 설정합니다.

## Step 5: 프롬프트 처리 및 추론 준비

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

입력 프롬프트를 토크나이즈하여 토큰 ID 시퀀스로 변환하고 추론 준비를 합니다. 또한 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 값을 초기화합니다. 각 토큰은 텐서로 변환되어 모델에 전달되고, 로짓이 계산됩니다.

루프는 프롬프트 내 각 토큰을 처리하며, 로짓 프로세서를 업데이트하고 다음 토큰 생성을 준비합니다.

## Step 6: 추론

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

추론 루프에서는 원하는 샘플 길이에 도달하거나 시퀀스 종료 토큰을 만날 때까지 토큰을 하나씩 생성합니다. 다음 토큰은 텐서로 변환되어 모델에 입력되고, 로짓은 페널티와 샘플링을 적용해 처리됩니다. 이후 토큰이 샘플링, 디코딩되어 시퀀스에 추가됩니다.
반복 텍스트 생성을 방지하기 위해 `repeat_last_n` and `repeat_penalty` 파라미터에 기반해 반복 토큰에 페널티가 적용됩니다.

생성된 텍스트는 디코딩되는 즉시 출력되어 실시간 스트리밍 형태로 보여집니다.

## Step 7: 애플리케이션 실행

애플리케이션을 실행하려면 터미널에서 다음 명령어를 입력하세요:

```bash
cargo run --release
```

그러면 Phi-3 모델이 생성한 아이스하키에 관한 하이쿠가 출력됩니다. 예를 들어:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

또는

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 결론

이 과정을 따라 하면 100줄 미만의 코드로 Rust와 Candle을 이용해 Phi-3 모델 기반 텍스트 생성을 수행할 수 있습니다. 코드는 모델 로딩, 토크나이징, 추론을 처리하며, 텐서와 로짓 프로세싱을 활용해 입력 프롬프트에 맞는 일관된 텍스트를 생성합니다.

이 콘솔 애플리케이션은 Windows, Linux, Mac OS에서 실행 가능합니다. Rust의 이식성 덕분에 모바일 앱 내부에서 실행 가능한 라이브러리로도 쉽게 변환할 수 있습니다(콘솔 앱은 모바일에서 실행할 수 없으므로).

## 부록: 전체 코드

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

참고: aarch64 Linux 또는 aarch64 Windows에서 이 코드를 실행하려면 `.cargo/config`라는 파일을 생성하고 다음 내용을 추가하세요:

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

> Rust와 Candle을 이용해 Phi-3 모델을 사용하는 다양한 예제와 추론 대체 방법은 공식 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 저장소를 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역은 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서는 해당 언어의 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.