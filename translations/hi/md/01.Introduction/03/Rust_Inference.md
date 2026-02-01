# Rust के साथ क्रॉस-प्लेटफ़ॉर्म इन्फरेंस

यह ट्यूटोरियल हमें Rust और HuggingFace के [Candle ML framework](https://github.com/huggingface/candle) का उपयोग करके इन्फरेंस करने की प्रक्रिया से परिचित कराएगा। Rust का उपयोग इन्फरेंस के लिए कई फायदे प्रदान करता है, खासकर जब इसे अन्य प्रोग्रामिंग भाषाओं से तुलना की जाती है। Rust अपनी उच्च प्रदर्शन क्षमता के लिए जाना जाता है, जो C और C++ के बराबर है। यह इन्फरेंस कार्यों के लिए एक बेहतरीन विकल्प बनाता है, जो अक्सर गणनात्मक रूप से भारी होते हैं। विशेष रूप से, यह शून्य-लागत वाले अमूर्तीकरण और कुशल मेमोरी प्रबंधन के कारण संभव होता है, जिसमें कोई गार्बेज कलेक्शन ओवरहेड नहीं होता। Rust की क्रॉस-प्लेटफ़ॉर्म क्षमताएं कोड को विभिन्न ऑपरेटिंग सिस्टम्स जैसे Windows, macOS, Linux, और मोबाइल ऑपरेटिंग सिस्टम्स पर बिना बड़े बदलाव के चलाने में सक्षम बनाती हैं।

इस ट्यूटोरियल का पालन करने के लिए आवश्यक है कि आप [Rust इंस्टॉल करें](https://www.rust-lang.org/tools/install), जिसमें Rust कंपाइलर और Cargo, Rust का पैकेज मैनेजर शामिल है।

## चरण 1: नया Rust प्रोजेक्ट बनाएं

नया Rust प्रोजेक्ट बनाने के लिए, टर्मिनल में निम्न कमांड चलाएं:

```bash
cargo new phi-console-app
```

यह एक प्रारंभिक प्रोजेक्ट संरचना बनाएगा जिसमें `Cargo.toml` फ़ाइल और `src` डायरेक्टरी होगी, जिसमें `main.rs` फ़ाइल शामिल है।

इसके बाद, हम अपनी निर्भरताएं - अर्थात् `candle`, `hf-hub` और `tokenizers` क्रेट्स - को `Cargo.toml` फ़ाइल में जोड़ेंगे:

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

## चरण 2: बुनियादी पैरामीटर सेट करें

`main.rs` फ़ाइल के अंदर, हम अपने इन्फरेंस के लिए प्रारंभिक पैरामीटर सेट करेंगे। इन्हें सरलता के लिए हार्डकोड किया जाएगा, लेकिन आवश्यकता अनुसार इन्हें बदला जा सकता है।

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

- **temperature**: सैंपलिंग प्रक्रिया की यादृच्छिकता को नियंत्रित करता है।
- **sample_len**: उत्पन्न किए जाने वाले टेक्स्ट की अधिकतम लंबाई निर्दिष्ट करता है।
- **top_p**: न्यूक्लियस सैंपलिंग के लिए उपयोग किया जाता है ताकि प्रत्येक चरण के लिए विचार किए जाने वाले टोकन की संख्या सीमित हो सके।
- **repeat_last_n**: पुनरावृत्ति रोकने के लिए दंड लगाने हेतु विचार किए जाने वाले टोकन की संख्या को नियंत्रित करता है।
- **repeat_penalty**: दोहराए गए टोकन को हतोत्साहित करने के लिए दंड मान।
- **seed**: एक यादृच्छिक बीज (बेहतर पुनरुत्पादन के लिए हम एक स्थिर मान का उपयोग कर सकते हैं)।
- **prompt**: उत्पन्न करने के लिए प्रारंभिक प्रॉम्प्ट टेक्स्ट। ध्यान दें कि हम मॉडल से आइस हॉकी के बारे में एक हाइकू जनरेट करने के लिए कह रहे हैं, और इसे बातचीत के उपयोगकर्ता और सहायक भागों को दर्शाने वाले विशेष टोकनों के साथ लपेटा गया है। मॉडल फिर इस प्रॉम्प्ट को एक हाइकू के साथ पूरा करेगा।
- **device**: इस उदाहरण में हम गणना के लिए CPU का उपयोग कर रहे हैं। Candle GPU पर CUDA और Metal के साथ भी चलाने का समर्थन करता है।

## चरण 3: मॉडल और टोकनाइज़र डाउनलोड/तैयार करें

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

हम Hugging Face मॉडल हब से मॉडल और टोकनाइज़र फ़ाइलें डाउनलोड करने के लिए `hf_hub` API का उपयोग करते हैं। `gguf` फ़ाइल में क्वांटाइज़्ड मॉडल वेट्स होते हैं, जबकि `tokenizer.json` फ़ाइल हमारे इनपुट टेक्स्ट को टोकनाइज़ करने के लिए उपयोग की जाती है। एक बार डाउनलोड हो जाने के बाद मॉडल कैश हो जाता है, इसलिए पहली बार निष्पादन धीमा होगा (क्योंकि यह 2.4GB मॉडल डाउनलोड करता है), लेकिन बाद के निष्पादन तेज होंगे।

## चरण 4: मॉडल लोड करें

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

हम क्वांटाइज़्ड मॉडल वेट्स को मेमोरी में लोड करते हैं और Phi-3 मॉडल को इनिशियलाइज़ करते हैं। इस चरण में `gguf` फ़ाइल से मॉडल वेट्स पढ़ना और निर्दिष्ट डिवाइस (यहाँ CPU) पर इन्फरेंस के लिए मॉडल सेटअप करना शामिल है।

## चरण 5: प्रॉम्प्ट को प्रोसेस करें और इन्फरेंस के लिए तैयार करें

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

इस चरण में, हम इनपुट प्रॉम्प्ट को टोकनाइज़ करते हैं और इसे टोकन आईडी की एक श्रृंखला में बदलकर इन्फरेंस के लिए तैयार करते हैं। हम `LogitsProcessor` को भी इनिशियलाइज़ करते हैं ताकि दिए गए `temperature` और `top_p` मानों के आधार पर सैंपलिंग प्रक्रिया (शब्दावली पर संभाव्यता वितरण) को संभाला जा सके। प्रत्येक टोकन को टेंसर में बदला जाता है और मॉडल के माध्यम से लॉजिट्स प्राप्त करने के लिए पास किया जाता है।

लूप प्रॉम्प्ट के प्रत्येक टोकन को प्रोसेस करता है, लॉजिट प्रोसेसर को अपडेट करता है और अगले टोकन जनरेशन के लिए तैयारी करता है।

## चरण 6: इन्फरेंस

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

इन्फरेंस लूप में, हम टोकन एक-एक करके उत्पन्न करते हैं जब तक कि हम इच्छित सैंपल लंबाई तक न पहुँच जाएं या अंत-श्रृंखला टोकन न मिल जाए। अगला टोकन टेंसर में बदला जाता है और मॉडल के माध्यम से पास किया जाता है, जबकि लॉजिट्स को दंड और सैंपलिंग लागू करने के लिए प्रोसेस किया जाता है। फिर अगला टोकन सैंपल किया जाता है, डिकोड किया जाता है, और श्रृंखला में जोड़ा जाता है।  
दोहराए गए टेक्स्ट से बचने के लिए, `repeat_last_n` और `repeat_penalty` पैरामीटर के आधार पर दोहराए गए टोकन पर दंड लगाया जाता है।

अंत में, उत्पन्न टेक्स्ट को डिकोड करते हुए प्रिंट किया जाता है, जिससे रियल-टाइम स्ट्रीमिंग आउटपुट सुनिश्चित होता है।

## चरण 7: एप्लिकेशन चलाएं

एप्लिकेशन चलाने के लिए, टर्मिनल में निम्न कमांड निष्पादित करें:

```bash
cargo run --release
```

यह Phi-3 मॉडल द्वारा जनरेट किया गया आइस हॉकी के बारे में एक हाइकू प्रिंट करेगा। कुछ इस तरह:

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

इन चरणों का पालन करके, हम Phi-3 मॉडल के साथ Rust और Candle का उपयोग करके 100 लाइनों से कम कोड में टेक्स्ट जनरेशन कर सकते हैं। कोड मॉडल लोडिंग, टोकनाइज़ेशन, और इन्फरेंस को संभालता है, टेंसर और लॉजिट प्रोसेसिंग का उपयोग करते हुए इनपुट प्रॉम्प्ट के आधार पर सुसंगत टेक्स्ट उत्पन्न करता है।

यह कंसोल एप्लिकेशन Windows, Linux और Mac OS पर चल सकता है। Rust की पोर्टेबिलिटी के कारण, इस कोड को मोबाइल ऐप्स के अंदर चलने वाली लाइब्रेरी में भी बदला जा सकता है (क्योंकि हम वहां कंसोल एप्लिकेशन नहीं चला सकते)।

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

ध्यान दें: aarch64 Linux या aarch64 Windows पर इस कोड को चलाने के लिए, `.cargo/config` नामक एक फ़ाइल बनाएं जिसमें निम्न सामग्री हो:

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

> आप आधिकारिक [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपॉजिटरी पर जाकर Phi-3 मॉडल को Rust और Candle के साथ उपयोग करने के और उदाहरण देख सकते हैं, जिसमें इन्फरेंस के वैकल्पिक तरीके भी शामिल हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।