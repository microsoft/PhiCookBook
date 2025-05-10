<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:50:39+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ne"
}
-->
# Cross-platform inference with Rust

यो ट्युटोरियलले हामीलाई HuggingFace को [Candle ML framework](https://github.com/huggingface/candle) प्रयोग गरेर Rust बाट inference गर्ने प्रक्रिया देखाउनेछ। Rust लाई inference का लागि प्रयोग गर्दा धेरै फाइदा हुन्छ, विशेष गरी अन्य प्रोग्रामिङ भाषाहरूको तुलनामा। Rust को प्रदर्शन C र C++ जस्तै उच्च छ। यसले computational रूपमा गाह्रो हुने inference कामहरूका लागि उत्कृष्ट विकल्प बनाउँछ। यसको मुख्य कारण zero-cost abstractions र efficient memory management हो, जसमा कुनै garbage collection overhead हुँदैन। Rust को cross-platform क्षमता Windows, macOS, Linux लगायत मोबाइल अपरेटिङ सिस्टमहरूमा पनि कोडलाई धेरै परिवर्तन बिना चलाउन सकिन्छ।

यस ट्युटोरियललाई पछ्याउनको लागि [Rust स्थापना](https://www.rust-lang.org/tools/install) गर्नु आवश्यक छ, जसमा Rust compiler र Cargo, Rust को package manager समावेश छन्।

## Step 1: Create a New Rust Project

नयाँ Rust प्रोजेक्ट बनाउन, टर्मिनलमा तलको कमाण्ड चलाउनुहोस्:

```bash
cargo new phi-console-app
```

यसले `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` फाइल सहित प्रारम्भिक प्रोजेक्ट संरचना बनाउँछ:

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

main.rs फाइल भित्र, हामी inference का लागि प्रारम्भिक प्यारामिटरहरू सेट गर्नेछौं। यी सबै सजिलो बनाउन hardcoded गरिएका छन्, तर आवश्यक अनुसार परिवर्तन गर्न सकिन्छ।

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

- **temperature**: sampling प्रक्रिया कत्तिको random हुन्छ भन्ने नियन्त्रण गर्छ।
- **sample_len**: उत्पन्न हुने टेक्स्टको अधिकतम लम्बाइ निर्दिष्ट गर्छ।
- **top_p**: nucleus sampling मा प्रत्येक स्टेपमा विचार गरिने tokens को संख्या सीमित गर्न प्रयोग हुन्छ।
- **repeat_last_n**: दोहोरिने अनुक्रम रोक्न penalty लागू गर्ने tokens को संख्या नियन्त्रण गर्छ।
- **repeat_penalty**: दोहोरिएका tokens मा लागू हुने penalty को मान।
- **seed**: random seed (अधिक reproducibility का लागि constant मान प्रयोग गर्न सकिन्छ)।
- **prompt**: उत्पन्न सुरु गर्नको लागि प्रारम्भिक टेक्स्ट। यहाँ हामीले मोडेललाई ice hockey सम्बन्धि haiku बनाउन भनेका छौं, र user र assistant को संवाद भागहरू जनाउन विशेष tokens ले wrap गरेका छौं। मोडेलले त्यसपछि haiku पूरा गर्नेछ।
- **device**: यस उदाहरणमा हामी CPU प्रयोग गरेका छौं। Candle GPU मा CUDA र Metal समर्थन पनि गर्छ।

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

हामी `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` फाइल प्रयोग गरेर इनपुट टेक्स्टलाई tokenize गर्छौं। मोडेल एक पटक डाउनलोड भएपछि cache हुन्छ, त्यसैले पहिलो पटक चलाउँदा ढिलो हुन्छ (किनभने 2.4GB मोडेल डाउनलोड हुन्छ), तर त्यसपछि छिटो चल्नेछ।

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

quantized मोडेल weights लाई मेमोरीमा लोड गरेर Phi-3 मोडेल initialize गर्छौं। यो चरणमा `gguf` फाइलबाट मोडेल weights पढिन्छ र निर्दिष्ट गरिएको device (यहाँ CPU) मा inference को लागि मोडेल तयार गरिन्छ।

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

यस चरणमा, हामी इनपुट prompt लाई tokenize गरेर token ID को श्रृंखला तयार गर्छौं। साथै `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` मानहरू initialize गर्छौं। प्रत्येक token लाई tensor मा रूपान्तरण गरी मोडेलमा पास गरिन्छ र logits प्राप्त गरिन्छ।

लूपले prompt का हरेक token लाई process गर्छ, logits processor अपडेट गर्छ र अर्को token उत्पन्न गर्न तयारी गर्छ।

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

inference लूपमा, हामी tokens एक-एक गरी उत्पन्न गर्छौं जबसम्म sample length पुग्दैन वा end-of-sequence token भेटिंदैन। अर्को token लाई tensor मा रूपान्तरण गरी मोडेलमा पास गरिन्छ, logits लाई penalty र sampling लागू गरिन्छ। त्यसपछि अर्को token sample गरी decode गरी श्रृंखलामा थपिन्छ।

दोहोरो टेक्स्ट रोक्न `repeat_last_n` and `repeat_penalty` का आधारमा penalty लागू गरिन्छ।

अन्त्यमा, उत्पन्न टेक्स्ट decode हुँदा नै प्रिन्ट गरिन्छ, जसले streamed real-time output सुनिश्चित गर्छ।

## Step 7: Run the Application

एप्लिकेशन चलाउन टर्मिनलमा तलको कमाण्ड चलाउनुहोस्:

```bash
cargo run --release
```

यसले Phi-3 मोडेलद्वारा ice hockey सम्बन्धि haiku उत्पन्न गरी प्रिन्ट गर्नेछ। यस्तो केही:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

वा

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

यी चरणहरू पालना गरेर, हामी Rust र Candle प्रयोग गरी Phi-3 मोडेलबाट १०० लाइनभन्दा कम कोडमा टेक्स्ट जनरेशन गर्न सक्छौं। कोडले मोडेल लोडिंग, tokenization, र inference सम्हाल्छ, tensors र logits process गरेर इनपुट prompt अनुसार सुसंगत टेक्स्ट उत्पन्न गर्छ।

यो console application Windows, Linux र Mac OS मा चल्न सक्छ। Rust को portability का कारण, यो कोडलाई मोबाइल एप्लिकेशन भित्र चल्ने library मा पनि रूपान्तरण गर्न सकिन्छ (console apps मोबाइलमा चल्दैनन्, आखिरमा)।

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

ध्यान दिनुहोस्: aarch64 Linux वा aarch64 Windows मा यो कोड चलाउन `.cargo/config` नामको फाइल थप्नुहोस् र त्यसमा तलको सामग्री राख्नुहोस्:

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

> थप उदाहरणहरूको लागि, तपाईँले आधिकारिक [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपोजिटरी हेर्न सक्नुहुन्छ, जहाँ Rust र Candle सँग Phi-3 मोडेल कसरी प्रयोग गर्ने बारे विभिन्न वैकल्पिक तरिका पनि छन्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा गलतफहमी हुन सक्छ। मूल दस्तावेजलाई यसको मूल भाषामा नै आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।