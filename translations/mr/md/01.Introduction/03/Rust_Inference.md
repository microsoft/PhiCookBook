<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:49:42+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "mr"
}
-->
# Rust सह क्रॉस-प्लॅटफॉर्म इन्फरन्स

हा ट्यूटोरियल Rust आणि HuggingFace च्या [Candle ML framework](https://github.com/huggingface/candle) वापरून इन्फरन्स कसा करायचा हे दाखवेल. इन्फरन्ससाठी Rust वापरण्याचे अनेक फायदे आहेत, विशेषतः इतर प्रोग्रामिंग भाषांशी तुलना केल्यास. Rust उच्च कार्यक्षमता साठी ओळखले जाते, जी C आणि C++ इतकीच जलद आहे. त्यामुळे हे इन्फरन्स सारख्या गणनात्मकदृष्ट्या जड कामांसाठी उत्तम पर्याय आहे. विशेषतः, हे शून्य-खर्च अभिसरणे आणि कार्यक्षम मेमरी व्यवस्थापनामुळे शक्य होते, ज्यात गार्बेज कलेक्शनचा त्रास नाही. Rust च्या क्रॉस-प्लॅटफॉर्म क्षमतेमुळे विंडोज, macOS, Linux तसेच मोबाइल ऑपरेटिंग सिस्टिम्सवर देखील कोणत्याही मोठ्या बदलांशिवाय कोड चालवता येतो.

हा ट्यूटोरियल फॉलो करण्यासाठी आवश्यक आहे की तुम्ही [Rust इन्स्टॉल केलेले असावे](https://www.rust-lang.org/tools/install), ज्यामध्ये Rust कंपाइलर आणि Cargo, Rust पॅकेज मॅनेजर यांचा समावेश आहे.

## Step 1: नवीन Rust प्रोजेक्ट तयार करा

नवीन Rust प्रोजेक्ट तयार करण्यासाठी टर्मिनलमध्ये खालील कमांड चालवा:

```bash
cargo new phi-console-app
```

हे `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` फाइलसह प्राथमिक प्रोजेक्ट स्ट्रक्चर तयार करेल:

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

## Step 2: मूलभूत पॅरामीटर्स सेट करा

main.rs फाइलमध्ये आपण आपल्या इन्फरन्ससाठी सुरुवातीचे पॅरामीटर्स सेट करू. सोप्या साठी हे सर्व हार्डकोड केलेले असतील, पण आवश्यकतेनुसार तुम्ही त्यात बदल करू शकता.

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

- **temperature**: सॅम्पलिंग प्रक्रियेतील यादृच्छिकतेचे नियंत्रण करते.
- **sample_len**: जनरेट होणाऱ्या मजकुराची कमाल लांबी निर्दिष्ट करते.
- **top_p**: न्यूक्लिअस सॅम्पलिंगसाठी वापरले जाते, ज्यामुळे प्रत्येक टप्प्यासाठी विचारात घेतलेल्या टोकन्सची संख्या मर्यादित होते.
- **repeat_last_n**: पुनरावृत्ती टाळण्यासाठी टोकन्सवर दंड लागू करण्यासाठी विचारात घेतले जाणारे टोकन्सची संख्या नियंत्रित करते.
- **repeat_penalty**: पुनरावृत्ती टोकन्ससाठी दिला जाणारा दंड मूल्य.
- **seed**: यादृच्छिक बीज (चांगल्या पुनरुत्पादनासाठी स्थिर मूल्य वापरू शकतो).
- **prompt**: जनरेशन सुरू करण्यासाठी सुरुवातीचा प्रॉम्प्ट मजकूर. लक्षात घ्या की आपण मॉडेलला आइस हॉकी विषयी हायकू तयार करण्यास सांगतो आणि वापरकर्ता व सहाय्यक भाग दर्शवण्यासाठी विशेष टोकन्सने त्याला वेढले आहे. मॉडेल नंतर हा प्रॉम्प्ट पूर्ण करेल.
- **device**: या उदाहरणात आम्ही CPU वापरतो. Candle GPU वर CUDA आणि Metal वापरून चालवण्यासही समर्थ आहे.

## Step 3: मॉडेल आणि टोकनायझर डाउनलोड/तयार करा

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

`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` फाइल आपल्या इनपुट मजकूर टोकनायझ करण्यासाठी वापरली जाते. एकदा मॉडेल डाउनलोड केल्यावर ते कॅशमध्ये साठवले जाते, त्यामुळे पहिली अंमलबजावणी हळू होईल (कारण 2.4GB मॉडेल डाउनलोड होते), पण पुढील अंमलबजावण्या जलद होतील.

## Step 4: मॉडेल लोड करा

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

आम्ही क्वांटाइज्ड मॉडेल वेट्स मेमरीमध्ये लोड करतो आणि Phi-3 मॉडेल इनिशियलाइझ करतो. या टप्प्यात `gguf` फाइलमधून मॉडेल वेट्स वाचून, दिलेल्या डिव्हाइसवर (या प्रकरणात CPU) इन्फरन्ससाठी मॉडेल सेटअप केले जाते.

## Step 5: प्रॉम्प्ट प्रक्रिया करा आणि इन्फरन्ससाठी तयार करा

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

या टप्प्यात, आपण इनपुट प्रॉम्प्ट टोकनायझ करतो आणि त्याला टोकन आयडीजच्या सिक्वेन्समध्ये रूपांतरित करून इन्फरन्ससाठी तयार करतो. तसेच `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` व्हॅल्यूज इनिशियलाइझ करतो. प्रत्येक टोकनला टेन्सरमध्ये रूपांतरित करून मॉडेलमधून लॉजिट्स प्राप्त होतात.

लूपमध्ये प्रत्येक टोकन प्रक्रिया केली जाते, लॉजिट्स प्रोसेसर अपडेट केला जातो आणि पुढील टोकन जनरेशनसाठी तयारी केली जाते.

## Step 6: इन्फरन्स

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

इन्फरन्स लूपमध्ये, आपण टोकन्स एक-एक करून जनरेट करतो जोपर्यंत आपण इच्छित sample_len पर्यंत पोहोचत नाही किंवा end-of-sequence टोकन येत नाही. पुढील टोकन टेन्सरमध्ये रूपांतरित करून मॉडेलमध्ये दिला जातो, तर लॉजिट्सवर दंड आणि सॅम्पलिंग लागू केले जाते. त्यानंतर पुढील टोकन निवडला जातो, डीकोड केला जातो आणि सिक्वेन्समध्ये जोडला जातो.
पुनरावृत्ती टाळण्यासाठी, `repeat_last_n` and `repeat_penalty` पॅरामीटर्सनुसार पुनरावृत्ती टोकन्सवर दंड लागू केला जातो.

शेवटी, जनरेट केलेला मजकूर डीकोड होताच प्रिंट केला जातो, ज्यामुळे रिअल-टाइम आउटपुट मिळतो.

## Step 7: अॅप्लिकेशन चालवा

अॅप्लिकेशन चालवण्यासाठी टर्मिनलमध्ये खालील कमांड चालवा:

```bash
cargo run --release
```

हे Phi-3 मॉडेलने जनरेट केलेला आइस हॉकी विषयी हायकू प्रिंट करेल. काहीसे असे:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

किंवा

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## निष्कर्ष

या पायऱ्या फॉलो करून, आपण Phi-3 मॉडेल वापरून Rust आणि Candle मध्ये 100 ओळींपेक्षा कमी कोडमध्ये टेक्स्ट जनरेशन करू शकतो. कोड मॉडेल लोडिंग, टोकनायझेशन आणि इन्फरन्स हाताळतो, टेन्सर्स आणि लॉजिट्स प्रोसेसिंग वापरून इनपुट प्रॉम्प्टवर आधारित सुसंगत टेक्स्ट जनरेट करतो.

हे कन्सोल अॅप्लिकेशन Windows, Linux आणि Mac OS वर चालू शकते. Rust च्या पोर्टेबिलिटीमुळे, कोड मोबाइल अॅप्समध्ये वापरण्यासाठी लायब्ररीमध्ये रूपांतरित देखील करता येतो (कारण कन्सोल अॅप्स मोबाइलवर चालत नाहीत).

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

टीप: aarch64 Linux किंवा aarch64 Windows वर हा कोड चालवण्यासाठी, `.cargo/config` नावाची फाइल तयार करा आणि त्यात खालील कंटेंट जोडा:

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

> अधिक उदाहरणांसाठी आणि Phi-3 मॉडेल Rust आणि Candle सह कसे वापरायचे यासाठी, अधिक पर्यायी इन्फरन्स पद्धतींसह, अधिकृत [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपॉझिटरी भेट द्या.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावणीबद्दल आम्ही जबाबदार नाही.