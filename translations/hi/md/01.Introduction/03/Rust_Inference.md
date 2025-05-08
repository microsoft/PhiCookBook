<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-08T06:03:47+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "hi"
}
-->
# Cross-platform inference with Rust

यह ट्यूटोरियल हमें HuggingFace के [Candle ML framework](https://github.com/huggingface/candle) का उपयोग करके Rust के साथ inference करने की प्रक्रिया बताएगा। inference के लिए Rust का उपयोग करने के कई फायदे हैं, खासकर अन्य प्रोग्रामिंग भाषाओं की तुलना में। Rust अपनी उच्च प्रदर्शन क्षमता के लिए जाना जाता है, जो C और C++ के समान है। यह इसे inference कार्यों के लिए एक बेहतरीन विकल्प बनाता है, जो कि गणनात्मक रूप से भारी हो सकते हैं। खासतौर पर, यह zero-cost abstractions और कुशल मेमोरी प्रबंधन के कारण है, जिसमें कोई garbage collection overhead नहीं होता। Rust की cross-platform क्षमताएं कोड को विभिन्न ऑपरेटिंग सिस्टम जैसे Windows, macOS, Linux, और मोबाइल ऑपरेटिंग सिस्टम पर बिना बड़े बदलाव के चलाने की अनुमति देती हैं।

इस ट्यूटोरियल को फॉलो करने के लिए आवश्यक है कि आप [Rust इंस्टॉल करें](https://www.rust-lang.org/tools/install), जिसमें Rust compiler और Cargo, Rust का पैकेज मैनेजर शामिल है।

## Step 1: नया Rust प्रोजेक्ट बनाएं

नया Rust प्रोजेक्ट बनाने के लिए टर्मिनल में निम्न कमांड चलाएं:

```bash
cargo new phi-console-app
```

यह एक प्रारंभिक प्रोजेक्ट स्ट्रक्चर बनाएगा जिसमें `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` फाइल शामिल होगी:

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

## Step 2: बुनियादी पैरामीटर सेट करें

main.rs फाइल के अंदर, हम inference के लिए प्रारंभिक पैरामीटर सेट करेंगे। ये सभी सादगी के लिए हार्डकोडेड होंगे, लेकिन आवश्यकता अनुसार इन्हें बदला जा सकता है।

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

- **temperature**: सैंपलिंग प्रक्रिया की randomness को नियंत्रित करता है।
- **sample_len**: जनरेट किए जाने वाले टेक्स्ट की अधिकतम लंबाई निर्धारित करता है।
- **top_p**: nucleus sampling के लिए उपयोग किया जाता है, जो प्रत्येक चरण में विचार किए जाने वाले टोकन की संख्या को सीमित करता है।
- **repeat_last_n**: पुनरावृत्ति वाले अनुक्रमों को रोकने के लिए टोकन पर पेनल्टी लगाने के लिए विचार किए जाने वाले टोकन की संख्या को नियंत्रित करता है।
- **repeat_penalty**: दोहराए गए टोकन को रोकने के लिए पेनल्टी का मान।
- **seed**: एक रैंडम सीड (बेहतर पुनरुत्पादन के लिए हम एक स्थिर मान भी उपयोग कर सकते हैं)।
- **prompt**: जनरेशन शुरू करने के लिए प्रारंभिक प्रॉम्प्ट टेक्स्ट। ध्यान दें कि हम मॉडल से आइस हॉकी पर एक हाइकु जनरेट करने के लिए कहते हैं, और इसे बातचीत के user और assistant भागों को दर्शाने वाले विशेष टोकनों से घेरते हैं। मॉडल फिर इस प्रॉम्प्ट को हाइकु के साथ पूरा करेगा।
- **device**: इस उदाहरण में हम गणना के लिए CPU का उपयोग कर रहे हैं। Candle GPU पर CUDA और Metal के साथ भी चलाने का समर्थन करता है।

## Step 3: मॉडल और टोकनाइज़र डाउनलोड/तैयार करें

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

हम `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` फाइल का उपयोग अपने इनपुट टेक्स्ट को टोकनाइज़ करने के लिए करते हैं। एक बार मॉडल डाउनलोड हो जाने के बाद यह कैश हो जाता है, इसलिए पहली बार चलाने में धीमी गति होगी (क्योंकि 2.4GB का मॉडल डाउनलोड होता है), लेकिन बाद के चलाने तेज होंगे।

## Step 4: मॉडल लोड करें

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

हम क्वांटाइज्ड मॉडल वेट्स को मेमोरी में लोड करते हैं और Phi-3 मॉडल को इनिशियलाइज़ करते हैं। इस चरण में `gguf` फाइल से मॉडल वेट्स पढ़ना और निर्दिष्ट डिवाइस (इस केस में CPU) पर inference के लिए मॉडल सेटअप करना शामिल है।

## Step 5: प्रॉम्प्ट को प्रोसेस करें और inference के लिए तैयार करें

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

इस चरण में, हम इनपुट प्रॉम्प्ट को टोकनाइज़ करते हैं और उसे टोकन IDs की एक श्रृंखला में बदलकर inference के लिए तैयार करते हैं। साथ ही हम `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` मानों को इनिशियलाइज़ करते हैं। प्रत्येक टोकन को टेंसर में बदलकर मॉडल के माध्यम से पास किया जाता है ताकि logits प्राप्त हो सकें।

लूप प्रॉम्प्ट के प्रत्येक टोकन को प्रोसेस करता है, logits प्रोसेसर को अपडेट करता है और अगले टोकन जनरेशन के लिए तैयार करता है।

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

inference लूप में, हम टोकन एक-एक करके जनरेट करते हैं जब तक कि हम वांछित sample length तक न पहुंच जाएं या end-of-sequence टोकन न मिल जाए। अगला टोकन टेंसर में बदला जाता है और मॉडल के माध्यम से पास किया जाता है, जबकि logits को पेनल्टी और सैंपलिंग लागू करने के लिए प्रोसेस किया जाता है। फिर अगला टोकन सैंपल किया जाता है, डिकोड किया जाता है, और श्रृंखला में जोड़ा जाता है।

दोहराए गए टेक्स्ट से बचने के लिए, `repeat_last_n` and `repeat_penalty` पैरामीटर के आधार पर दोहराए गए टोकन पर पेनल्टी लगाई जाती है।

अंत में, जनरेट किया गया टेक्स्ट डिकोड होते ही प्रिंट किया जाता है, जिससे रियल-टाइम स्ट्रीमिंग आउटपुट सुनिश्चित होता है।

## Step 7: एप्लिकेशन चलाएं

एप्लिकेशन चलाने के लिए टर्मिनल में निम्न कमांड चलाएं:

```bash
cargo run --release
```

यह Phi-3 मॉडल द्वारा जनरेट किया गया आइस हॉकी पर एक हाइकु प्रिंट करेगा। कुछ ऐसा:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

या

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## निष्कर्ष

इन चरणों का पालन करके, हम Phi-3 मॉडल के साथ Rust और Candle का उपयोग करके 100 लाइनों से कम कोड में टेक्स्ट जनरेशन कर सकते हैं। कोड मॉडल लोडिंग, टोकनाइज़ेशन, और inference को संभालता है, टेंसर और logits प्रोसेसिंग का उपयोग करते हुए इनपुट प्रॉम्प्ट के आधार पर संगत टेक्स्ट जनरेट करता है।

यह कंसोल एप्लिकेशन Windows, Linux और Mac OS पर चल सकता है। Rust की पोर्टेबिलिटी के कारण, इस कोड को मोबाइल ऐप्स के अंदर चलने वाली लाइब्रेरी के रूप में भी अनुकूलित किया जा सकता है (क्योंकि हम वहां कंसोल ऐप्स नहीं चला सकते)।

## परिशिष्ट: पूरा कोड

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

ध्यान दें: aarch64 Linux या aarch64 Windows पर इस कोड को चलाने के लिए, `.cargo/config` नाम की एक फाइल बनाएं और उसमें निम्न सामग्री डालें:

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

> आप आधिकारिक [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपॉजिटरी पर जाकर Rust और Candle के साथ Phi-3 मॉडल का उपयोग करने के और उदाहरण देख सकते हैं, जिसमें inference के वैकल्पिक तरीके भी शामिल हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।