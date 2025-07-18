<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:27:54+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ne"
}
-->
# Rust सँग क्रस-प्लेटफर्म इन्फरेन्स

यस ट्युटोरियलले हामीलाई Rust र HuggingFace को [Candle ML framework](https://github.com/huggingface/candle) प्रयोग गरेर इन्फरेन्स गर्ने प्रक्रिया सिकाउनेछ। Rust प्रयोग गरेर इन्फरेन्स गर्दा धेरै फाइदाहरू छन्, विशेष गरी अन्य प्रोग्रामिङ भाषाहरूको तुलनामा। Rust उच्च प्रदर्शनका लागि परिचित छ, जुन C र C++ जस्तै छ। यसले इन्फरेन्स कार्यहरूका लागि उत्कृष्ट विकल्प बनाउँछ, जुन प्रायः कम्प्युटेशनल रूपमा गाह्रो हुन्छ। विशेष गरी, यो शून्य-लागत अमूर्तता र कुशल मेमोरी व्यवस्थापनको कारणले हो, जसमा कुनै गार्बेज कलेक्सन ओभरहेड हुँदैन। Rust को क्रस-प्लेटफर्म क्षमता विभिन्न अपरेटिङ सिस्टमहरूमा, जस्तै Windows, macOS, Linux, साथै मोबाइल अपरेटिङ सिस्टमहरूमा पनि, कोडमा ठूलो परिवर्तन नगरी चलाउन सकिन्छ।

यस ट्युटोरियल अनुसरण गर्नको लागि पूर्वशर्त [Rust इन्स्टल गर्नुहोस्](https://www.rust-lang.org/tools/install), जसमा Rust कम्पाइलर र Rust प्याकेज म्यानेजर Cargo समावेश छ।

## चरण १: नयाँ Rust प्रोजेक्ट बनाउनुहोस्

नयाँ Rust प्रोजेक्ट बनाउन, टर्मिनलमा तलको कमाण्ड चलाउनुहोस्:

```bash
cargo new phi-console-app
```

यसले `Cargo.toml` फाइल र `src` डाइरेक्टरी भित्र `main.rs` फाइल सहित प्रारम्भिक प्रोजेक्ट संरचना बनाउँछ।

अर्को, हामी हाम्रो निर्भरता थप्नेछौं - अर्थात् `candle`, `hf-hub` र `tokenizers` क्रेटहरू - `Cargo.toml` फाइलमा:

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

## चरण २: आधारभूत प्यारामिटरहरू सेटअप गर्नुहोस्

`main.rs` फाइल भित्र, हामी हाम्रो इन्फरेन्सका लागि प्रारम्भिक प्यारामिटरहरू सेट गर्नेछौं। यी सबै सजिलो बनाउन हार्डकोड गरिनेछन्, तर आवश्यक अनुसार परिवर्तन गर्न सकिन्छ।

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

- **temperature**: स्याम्पलिङ प्रक्रियाको अनियमितता नियन्त्रण गर्छ।
- **sample_len**: उत्पन्न हुने टेक्स्टको अधिकतम लम्बाइ निर्दिष्ट गर्छ।
- **top_p**: न्युक्लियस स्याम्पलिङका लागि प्रयोग गरिन्छ, प्रत्येक चरणमा विचार गरिने टोकनहरूको संख्या सीमित गर्न।
- **repeat_last_n**: दोहोरिने अनुक्रमहरू रोक्नको लागि लागू गरिने दण्डको लागि विचार गरिने टोकनहरूको संख्या नियन्त्रण गर्छ।
- **repeat_penalty**: दोहोरिएका टोकनहरूलाई रोक्नको लागि दण्ड मान।
- **seed**: एउटा र्यान्डम सिड (रिप्रोड्युसिबिलिटीका लागि स्थिर मान प्रयोग गर्न सकिन्छ)।
- **prompt**: उत्पन्न सुरु गर्नको लागि प्रारम्भिक प्रॉम्प्ट टेक्स्ट। यहाँ हामी मोडेललाई आइस हकीबारे हाइकु बनाउन भनिरहेका छौं, र यसलाई विशेष टोकनहरूले प्रयोगकर्ता र सहायक भागहरू जनाउन घेरिएको छ। मोडेल त्यसपछि हाइकु पूरा गर्नेछ।
- **device**: यस उदाहरणमा हामी CPU प्रयोग गर्दैछौं। Candle GPU मा CUDA र Metal मार्फत पनि चलाउन समर्थन गर्छ।

## चरण ३: मोडेल र टोकनाइजर डाउनलोड/तयार गर्नुहोस्

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

हामी `hf_hub` API प्रयोग गरेर Hugging Face मोडेल हबबाट मोडेल र टोकनाइजर फाइलहरू डाउनलोड गर्छौं। `gguf` फाइलमा क्वान्टाइज्ड मोडेल वेटहरू हुन्छन्, जबकि `tokenizer.json` फाइल हाम्रो इनपुट टेक्स्ट टोकनाइज गर्न प्रयोग हुन्छ। एक पटक डाउनलोड भएपछि मोडेल क्यास हुन्छ, त्यसैले पहिलो पटक चलाउँदा ढिलो हुन्छ (किनभने २.४GB मोडेल डाउनलोड हुन्छ), तर पछि छिटो चल्नेछ।

## चरण ४: मोडेल लोड गर्नुहोस्

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

हामी क्वान्टाइज्ड मोडेल वेटहरू मेमोरीमा लोड गर्छौं र Phi-3 मोडेल इनिसियलाइज गर्छौं। यस चरणमा `gguf` फाइलबाट मोडेल वेटहरू पढिन्छ र निर्दिष्ट गरिएको डिभाइस (यस अवस्थामा CPU) मा इन्फरेन्सका लागि मोडेल सेटअप गरिन्छ।

## चरण ५: प्रॉम्प्ट प्रक्रिया गरी इन्फरेन्सका लागि तयार गर्नुहोस्

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

यस चरणमा, हामी इनपुट प्रॉम्प्टलाई टोकनाइज गर्छौं र टोकन ID को अनुक्रममा रूपान्तरण गरेर इन्फरेन्सका लागि तयार पार्छौं। हामी `LogitsProcessor` पनि इनिसियलाइज गर्छौं, जुन दिइएका `temperature` र `top_p` मानहरूका आधारमा स्याम्पलिङ प्रक्रिया (शब्दावलीमा सम्भाव्यता वितरण) सम्हाल्छ। प्रत्येक टोकनलाई टेन्सरमा रूपान्तरण गरी मोडेलमा पठाइन्छ र logits प्राप्त गरिन्छ।

लूपले प्रॉम्प्टका प्रत्येक टोकनलाई प्रक्रिया गर्छ, logits प्रोसेसर अपडेट गर्छ र अर्को टोकन उत्पन्न गर्न तयार पार्छ।

## चरण ६: इन्फरेन्स

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

इन्फरेन्स लूपमा, हामी टोकनहरू एक-एक गरी उत्पन्न गर्छौं जबसम्म चाहिएको नमूना लम्बाइ पुग्दैन वा अन्त्य-क्रम टोकन भेटिँदैन। अर्को टोकनलाई टेन्सरमा रूपान्तरण गरी मोडेलमा पठाइन्छ, logits लाई दण्ड र स्याम्पलिङ लागू गर्न प्रोसेस गरिन्छ। त्यसपछि अर्को टोकन स्याम्पल गरिन्छ, डिकोड गरिन्छ र अनुक्रममा थपिन्छ।

दोहोरो टेक्स्टबाट बच्न, `repeat_last_n` र `repeat_penalty` प्यारामिटरहरूका आधारमा दोहोरिएका टोकनहरूमा दण्ड लागू गरिन्छ।

अन्तमा, उत्पन्न टेक्स्ट डिकोड हुँदै प्रिन्ट गरिन्छ, जसले स्ट्रिम गरिएको रियल-टाइम आउटपुट सुनिश्चित गर्छ।

## चरण ७: एप्लिकेशन चलाउनुहोस्

एप्लिकेशन चलाउन, टर्मिनलमा तलको कमाण्ड चलाउनुहोस्:

```bash
cargo run --release
```

यसले Phi-3 मोडेलद्वारा उत्पन्न आइस हकीबारे हाइकु प्रिन्ट गर्नेछ। केही यस्तै:

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

## निष्कर्ष

यी चरणहरू पालना गरेर, हामी Rust र Candle प्रयोग गरी Phi-3 मोडेलबाट १०० लाइनभन्दा कम कोडमा टेक्स्ट उत्पन्न गर्न सक्छौं। कोडले मोडेल लोडिङ, टोकनाइजेशन, र इन्फरेन्स सम्हाल्छ, टेन्सर र logits प्रोसेसिङ प्रयोग गरी इनपुट प्रॉम्प्टको आधारमा सुसंगत टेक्स्ट उत्पन्न गर्छ।

यो कन्सोल एप्लिकेशन Windows, Linux र Mac OS मा चल्न सक्छ। Rust को पोर्टेबिलिटीका कारण, कोडलाई मोबाइल एप्स भित्र चल्ने लाइब्रेरीमा पनि अनुकूलन गर्न सकिन्छ (किनभने त्यहाँ कन्सोल एप्स चल्दैनन्)।

## परिशिष्ट: पूर्ण कोड

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

ध्यान दिनुहोस्: aarch64 Linux वा aarch64 Windows मा यो कोड चलाउन `.cargo/config` नामक फाइल थप्नुहोस् र तलको सामग्री राख्नुहोस्:

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

> तपाईंले आधिकारिक [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपोजिटरीमा गएर Rust र Candle सँग Phi-3 मोडेल कसरी प्रयोग गर्ने बारे थप उदाहरणहरू र वैकल्पिक इन्फरेन्स तरिकाहरू हेर्न सक्नुहुन्छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।