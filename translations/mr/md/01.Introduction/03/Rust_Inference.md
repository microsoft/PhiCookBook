# Rust सह क्रॉस-प्लॅटफॉर्म इन्फरन्स

हा ट्युटोरियल Rust आणि HuggingFace च्या [Candle ML फ्रेमवर्क](https://github.com/huggingface/candle) वापरून इन्फरन्स कसा करायचा हे शिकवेल. Rust वापरून इन्फरन्स करण्याचे अनेक फायदे आहेत, विशेषतः इतर प्रोग्रामिंग भाषांच्या तुलनेत. Rust ची कार्यक्षमता C आणि C++ इतकीच उच्च आहे. त्यामुळे, गणनात्मकदृष्ट्या जास्त खर्चिक असलेल्या इन्फरन्स कामांसाठी Rust एक उत्कृष्ट पर्याय आहे. हे मुख्यतः शून्य-किंवा कमी खर्चाच्या अभिप्रेत संकल्पना आणि कार्यक्षम मेमरी व्यवस्थापनामुळे शक्य होते, ज्यात कोणताही गार्बेज कलेक्शनचा ओव्हरहेड नाही. Rust ची क्रॉस-प्लॅटफॉर्म क्षमता विविध ऑपरेटिंग सिस्टीम्सवर, जसे Windows, macOS, Linux तसेच मोबाइल ऑपरेटिंग सिस्टीम्सवर, मोठ्या प्रमाणात कोडमध्ये बदल न करता चालणारे कोड विकसित करण्यास अनुमती देते.

हा ट्युटोरियल फॉलो करण्यासाठी आवश्यक आहे की तुम्ही [Rust इन्स्टॉल](https://www.rust-lang.org/tools/install) केलेले असावे, ज्यात Rust कंपायलर आणि Cargo, Rust पॅकेज मॅनेजर, समाविष्ट आहे.

## पाऊल 1: नवीन Rust प्रोजेक्ट तयार करा

नवीन Rust प्रोजेक्ट तयार करण्यासाठी, टर्मिनलमध्ये खालील कमांड चालवा:

```bash
cargo new phi-console-app
```

यामुळे `Cargo.toml` फाइल आणि `src` डिरेक्टरीसह `main.rs` फाइल असलेली प्राथमिक प्रोजेक्ट रचना तयार होते.

यानंतर, आपले अवलंबित्व - म्हणजे `candle`, `hf-hub` आणि `tokenizers` क्रेट्स - `Cargo.toml` फाइलमध्ये जोडू:

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

## पाऊल 2: मूलभूत पॅरामीटर्स कॉन्फिगर करा

`main.rs` फाइलमध्ये, आपण आपल्या इन्फरन्ससाठी प्राथमिक पॅरामीटर्स सेट करू. सोप्या साठी हे सर्व हार्डकोड केलेले असतील, पण आवश्यकतेनुसार आपण त्यात बदल करू शकतो.

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

- **temperature**: सॅम्पलिंग प्रक्रियेतील यादृच्छिकतेवर नियंत्रण ठेवते.
- **sample_len**: तयार होणाऱ्या मजकुराची कमाल लांबी निर्दिष्ट करते.
- **top_p**: न्यूक्लियस सॅम्पलिंगसाठी वापरले जाते, ज्यामुळे प्रत्येक टप्प्यावर विचारात घेतल्या जाणाऱ्या टोकन्सची संख्या मर्यादित होते.
- **repeat_last_n**: पुनरावृत्ती होणाऱ्या अनुक्रमांना प्रतिबंध करण्यासाठी टोकन्सवर दंड लावण्यासाठी विचारात घेतल्या जाणाऱ्या टोकन्सची संख्या नियंत्रित करते.
- **repeat_penalty**: पुनरावृत्ती टोकन्सला टाळण्यासाठी लावलेला दंड मूल्य.
- **seed**: यादृच्छिक बीज (चांगल्या पुनरुत्पादकतेसाठी स्थिर मूल्य वापरू शकतो).
- **prompt**: जनरेशन सुरू करण्यासाठी प्रारंभिक प्रॉम्प्ट मजकूर. लक्षात घ्या की आपण मॉडेलला आइस हॉकीवर एक हायकू तयार करण्यास सांगितले आहे, आणि संवादातील वापरकर्ता आणि सहाय्यक भाग दर्शविण्यासाठी विशेष टोकन्सने याला वेढले आहे. मॉडेल नंतर हायकू पूर्ण करेल.
- **device**: या उदाहरणात गणनेसाठी CPU वापरले आहे. Candle GPU वर CUDA आणि Metal सह चालवण्यासही समर्थ आहे.

## पाऊल 3: मॉडेल आणि टोकनायझर डाउनलोड/तयार करा

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

आम्ही `hf_hub` API वापरून Hugging Face मॉडेल हबमधून मॉडेल आणि टोकनायझर फाइल्स डाउनलोड करतो. `gguf` फाइलमध्ये क्वांटाइज्ड मॉडेल वेट्स असतात, तर `tokenizer.json` फाइल इनपुट मजकूर टोकनायझ करण्यासाठी वापरली जाते. एकदा डाउनलोड झाल्यावर मॉडेल कॅश होते, त्यामुळे पहिल्या वेळी (2.4GB मॉडेल डाउनलोड करताना) प्रक्रिया हळू होईल, पण पुढील वेळा जलद होईल.

## पाऊल 4: मॉडेल लोड करा

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

आम्ही क्वांटाइज्ड मॉडेल वेट्स मेमरीमध्ये लोड करतो आणि Phi-3 मॉडेल इनिशियलाइझ करतो. या टप्प्यात `gguf` फाइलमधून मॉडेल वेट्स वाचल्या जातात आणि निर्दिष्ट डिव्हाइसवर (या प्रकरणात CPU) इन्फरन्ससाठी मॉडेल सेटअप केले जाते.

## पाऊल 5: प्रॉम्प्ट प्रक्रिया करा आणि इन्फरन्ससाठी तयार करा

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

या टप्प्यात, आम्ही इनपुट प्रॉम्प्ट टोकनायझ करतो आणि त्याला टोकन आयडीच्या अनुक्रमात रूपांतरित करून इन्फरन्ससाठी तयार करतो. तसेच, दिलेल्या `temperature` आणि `top_p` मूल्यांवर आधारित सॅम्पलिंग प्रक्रियेसाठी `LogitsProcessor` इनिशियलाइझ करतो. प्रत्येक टोकन टेन्सरमध्ये रूपांतरित होतो आणि मॉडेलमधून लॉजिट्स मिळवले जातात.

लूप प्रत्येक टोकनवर प्रक्रिया करतो, लॉजिट्स प्रोसेसर अपडेट करतो आणि पुढील टोकन जनरेशनसाठी तयारी करतो.

## पाऊल 6: इन्फरन्स

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

इन्फरन्स लूपमध्ये, आम्ही टोकन्स एक एक करून तयार करतो जोपर्यंत इच्छित सॅम्पल लांबी पूर्ण होत नाही किंवा एंड-ऑफ-सीक्वेन्स टोकन येत नाही. पुढील टोकन टेन्सरमध्ये रूपांतरित होतो आणि मॉडेलमधून जातो, तर लॉजिट्सवर दंड आणि सॅम्पलिंग लागू केले जाते. नंतर पुढील टोकन सॅम्पल केला जातो, डीकोड केला जातो आणि अनुक्रमात जोडला जातो.
पुनरावृत्ती टाळण्यासाठी, `repeat_last_n` आणि `repeat_penalty` पॅरामीटर्सच्या आधारे पुनरावृत्ती टोकन्सवर दंड लावला जातो.

शेवटी, तयार झालेला मजकूर डीकोड होताच प्रिंट केला जातो, ज्यामुळे रिअल-टाइम आउटपुट मिळतो.

## पाऊल 7: अ‍ॅप्लिकेशन चालवा

अ‍ॅप्लिकेशन चालवण्यासाठी, टर्मिनलमध्ये खालील कमांड चालवा:

```bash
cargo run --release
```

यामुळे Phi-3 मॉडेलने तयार केलेला आइस हॉकीवर एक हायकू प्रिंट होईल. काहीसे असे:

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

या पायऱ्या फॉलो करून, आपण Rust आणि Candle वापरून Phi-3 मॉडेलसह १०० ओळींपेक्षा कमी कोडमध्ये मजकूर निर्मिती करू शकतो. कोड मॉडेल लोडिंग, टोकनायझेशन आणि इन्फरन्स हाताळतो, टेन्सर्स आणि लॉजिट्स प्रोसेसिंगचा उपयोग करून इनपुट प्रॉम्प्टवर आधारित सुसंगत मजकूर तयार करतो.

हे कन्सोल अ‍ॅप्लिकेशन Windows, Linux आणि Mac OS वर चालू शकते. Rust च्या पोर्टेबिलिटीमुळे, हा कोड मोबाइल अ‍ॅप्समध्ये वापरण्यासाठी लायब्ररीमध्येही रूपांतरित केला जाऊ शकतो (कारण कन्सोल अ‍ॅप्स मोबाइलवर चालत नाहीत).

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

टीप: aarch64 Linux किंवा aarch64 Windows वर हा कोड चालवण्यासाठी, `.cargo/config` नावाची फाइल तयार करा आणि त्यात खालील सामग्री जोडा:

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

> अधिक उदाहरणांसाठी, Rust आणि Candle सह Phi-3 मॉडेल कसे वापरायचे याबाबत पर्यायी पद्धतींसह, तुम्ही अधिकृत [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रेपॉजिटरी पाहू शकता.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.