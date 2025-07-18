<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:26:44+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ko"
}
-->
# Rust를 이용한 크로스 플랫폼 추론

이 튜토리얼에서는 Rust와 HuggingFace의 [Candle ML 프레임워크](https://github.com/huggingface/candle)를 사용하여 추론을 수행하는 과정을 안내합니다. Rust를 추론에 사용하는 것은 특히 다른 프로그래밍 언어와 비교했을 때 여러 가지 장점이 있습니다. Rust는 C와 C++에 필적하는 높은 성능으로 잘 알려져 있습니다. 이는 계산 집약적인 추론 작업에 매우 적합합니다. 특히, 제로 코스트 추상화와 효율적인 메모리 관리 덕분에 가비지 컬렉션 오버헤드가 없습니다. Rust의 크로스 플랫폼 기능은 Windows, macOS, Linux뿐만 아니라 모바일 운영체제에서도 코드베이스를 크게 변경하지 않고 실행할 수 있는 코드를 개발할 수 있게 해줍니다.

이 튜토리얼을 따라가기 위한 전제 조건은 [Rust 설치](https://www.rust-lang.org/tools/install)입니다. 여기에는 Rust 컴파일러와 Rust 패키지 관리자 Cargo가 포함되어 있습니다.

## 1단계: 새로운 Rust 프로젝트 생성

터미널에서 다음 명령어를 실행하여 새로운 Rust 프로젝트를 생성합니다:

```bash
cargo new phi-console-app
```

이 명령어는 `Cargo.toml` 파일과 `main.rs` 파일이 포함된 `src` 디렉터리를 가진 초기 프로젝트 구조를 생성합니다.

다음으로, `Cargo.toml` 파일에 `candle`, `hf-hub`, `tokenizers` 크레이트를 의존성으로 추가합니다:

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

## 2단계: 기본 파라미터 설정

`main.rs` 파일 내에서 추론에 필요한 초기 파라미터를 설정합니다. 간단하게 하드코딩되어 있지만 필요에 따라 수정할 수 있습니다.

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

- **temperature**: 샘플링 과정의 무작위성을 조절합니다.
- **sample_len**: 생성할 텍스트의 최대 길이를 지정합니다.
- **top_p**: 누클리어스 샘플링에 사용되며, 각 단계에서 고려할 토큰 수를 제한합니다.
- **repeat_last_n**: 반복되는 시퀀스를 방지하기 위해 패널티를 적용할 토큰 수를 조절합니다.
- **repeat_penalty**: 반복된 토큰에 부여할 패널티 값입니다.
- **seed**: 랜덤 시드 (재현성을 위해 상수 값을 사용할 수 있습니다).
- **prompt**: 생성 시작을 위한 초기 프롬프트 텍스트입니다. 여기서는 아이스하키에 관한 하이쿠를 생성하도록 모델에 요청하며, 대화의 사용자와 어시스턴트 부분을 나타내는 특수 토큰으로 감싸져 있습니다. 모델은 이 프롬프트를 바탕으로 하이쿠를 완성합니다.
- **device**: 이 예제에서는 CPU를 사용합니다. Candle은 CUDA와 Metal을 이용한 GPU 실행도 지원합니다.

## 3단계: 모델 및 토크나이저 다운로드/준비

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

`hf_hub` API를 사용하여 Hugging Face 모델 허브에서 모델과 토크나이저 파일을 다운로드합니다. `gguf` 파일은 양자화된 모델 가중치를 포함하고, `tokenizer.json` 파일은 입력 텍스트를 토크나이징하는 데 사용됩니다. 모델이 다운로드되면 캐시에 저장되므로 첫 실행은 느리지만(모델 크기가 2.4GB임) 이후 실행은 더 빨라집니다.

## 4단계: 모델 로드

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

양자화된 모델 가중치를 메모리에 로드하고 Phi-3 모델을 초기화합니다. 이 단계에서는 `gguf` 파일에서 모델 가중치를 읽고 지정된 디바이스(CPU)에서 추론할 수 있도록 모델을 설정합니다.

## 5단계: 프롬프트 처리 및 추론 준비

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

이 단계에서는 입력 프롬프트를 토크나이징하고 토큰 ID 시퀀스로 변환하여 추론 준비를 합니다. 또한 주어진 `temperature`와 `top_p` 값에 따라 샘플링 과정을 처리할 `LogitsProcessor`를 초기화합니다. 각 토큰은 텐서로 변환되어 모델에 전달되어 로짓을 얻습니다.

루프는 프롬프트의 각 토큰을 처리하며, 로짓 프로세서를 업데이트하고 다음 토큰 생성을 준비합니다.

## 6단계: 추론

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

추론 루프에서는 원하는 샘플 길이에 도달하거나 종료 토큰을 만날 때까지 토큰을 하나씩 생성합니다. 다음 토큰은 텐서로 변환되어 모델에 전달되고, 로짓은 패널티와 샘플링을 적용하기 위해 처리됩니다. 이후 다음 토큰이 샘플링되고 디코딩되어 시퀀스에 추가됩니다. 반복되는 텍스트를 방지하기 위해 `repeat_last_n`과 `repeat_penalty` 파라미터에 따라 반복된 토큰에 패널티가 적용됩니다.

마지막으로, 생성된 텍스트는 디코딩되는 즉시 출력되어 실시간 스트리밍 결과를 제공합니다.

## 7단계: 애플리케이션 실행

터미널에서 다음 명령어를 실행하여 애플리케이션을 실행합니다:

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

이 단계를 따라 하면 100줄 미만의 코드로 Rust와 Candle을 사용해 Phi-3 모델로 텍스트 생성을 수행할 수 있습니다. 코드는 모델 로딩, 토크나이징, 추론을 처리하며, 텐서와 로짓 처리를 활용해 입력 프롬프트에 기반한 일관된 텍스트를 생성합니다.

이 콘솔 애플리케이션은 Windows, Linux, Mac OS에서 실행할 수 있습니다. Rust의 이식성 덕분에 모바일 앱 내에서 실행되는 라이브러리로도 쉽게 변환할 수 있습니다(모바일에서는 콘솔 앱 실행이 불가능하기 때문입니다).

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

> Rust와 Candle을 사용해 Phi-3 모델을 활용하는 다양한 예제와 대체 추론 방법은 공식 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 저장소에서 확인할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.