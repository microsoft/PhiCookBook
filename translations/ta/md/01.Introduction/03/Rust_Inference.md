<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-10-11T12:19:31+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ta"
}
-->
# ரஸ்ட் மூலம் பல்வேறு தளங்களில் முன்னறிவிப்பு

இந்த பயிற்சி HuggingFace இன் [Candle ML framework](https://github.com/huggingface/candle) பயன்படுத்தி ரஸ்ட் மூலம் முன்னறிவிப்பு செய்யும் செயல்முறையை வழிநடத்தும். ரஸ்ட் மூலம் முன்னறிவிப்பு செய்வது பல நன்மைகளை வழங்குகிறது, குறிப்பாக மற்ற நிரலாக்க மொழிகளுடன் ஒப்பிடும்போது. ரஸ்ட் அதன் உயர் செயல்திறனுக்காக அறியப்படுகிறது, இது C மற்றும் C++ உடன் ஒப்பிடக்கூடியது. இது கணினி மையமிக்க முன்னறிவிப்பு பணிகளுக்கு சிறந்த தேர்வாகும். குறிப்பாக, இது zero-cost abstractions மற்றும் திறமையான நினைவக மேலாண்மையால் இயக்கப்படுகிறது, இது garbage collection overhead இல்லாமல் செயல்படுகிறது. ரஸ்டின் பல்வேறு தளங்களுக்கான திறன்கள் Windows, macOS, Linux போன்ற பல்வேறு இயக்க முறைமைகளிலும், மொபைல் இயக்க முறைமைகளிலும், குறைந்த மாற்றங்களுடன் செயல்படும் குறியீடுகளை உருவாக்க அனுமதிக்கிறது.

இந்த பயிற்சியை பின்பற்றுவதற்கான முன்பைத் தயாரிப்பு [ரஸ்ட் நிறுவல்](https://www.rust-lang.org/tools/install) ஆகும், இது ரஸ்ட் கம்பைலர் மற்றும் Cargo, ரஸ்ட் பாக்கேஜ் மேலாளரை உள்ளடக்கியது.

## படி 1: புதிய ரஸ்ட் திட்டத்தை உருவாக்குதல்

புதிய ரஸ்ட் திட்டத்தை உருவாக்க, டெர்மினலில் பின்வரும் கட்டளையை இயக்கவும்:

```bash
cargo new phi-console-app
```

இது `Cargo.toml` கோப்புடன் மற்றும் `src` அடைவில் உள்ள `main.rs` கோப்புடன் ஆரம்ப திட்ட அமைப்பை உருவாக்குகிறது.

அடுத்ததாக, `Cargo.toml` கோப்பில் `candle`, `hf-hub` மற்றும் `tokenizers` crates ஆகியவற்றை நமது சார்புகளாக சேர்ப்போம்:

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

## படி 2: அடிப்படை அளவுரைகளை அமைத்தல்

`main.rs` கோப்பின் உள்ளே, நமது முன்னறிவிப்புக்கான ஆரம்ப அளவுரைகளை அமைப்போம். எளிமைக்காக அவை அனைத்தும் hardcoded ஆக இருக்கும், ஆனால் அவற்றை தேவையானபடி மாற்றலாம்.

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

- **temperature**: மாதிரியின் சாம்பிளிங் செயல்முறையின் சீரற்ற தன்மையை கட்டுப்படுத்துகிறது.
- **sample_len**: உருவாக்கப்பட்ட உரையின் அதிகபட்ச நீளத்தை குறிப்பிடுகிறது.
- **top_p**: nucleus sampling பயன்படுத்தி ஒவ்வொரு படியிலும் கருதப்படும் tokenகளின் எண்ணிக்கையை வரையறுக்கிறது.
- **repeat_last_n**: மீண்டும் மீண்டும் வரிசைகள் தோன்றுவதைத் தடுக்க penalty ஐப் பயன்படுத்தும் tokenகளின் எண்ணிக்கையை கட்டுப்படுத்துகிறது.
- **repeat_penalty**: மீண்டும் வரும் tokenகளைத் தடுக்க penalty மதிப்பை வழங்குகிறது.
- **seed**: ஒரு சீரற்ற seed (மீண்டும் உருவாக்கத்திற்காக constant மதிப்பை பயன்படுத்தலாம்).
- **prompt**: உருவாக்கத்தைத் தொடங்க ஆரம்ப prompt உரை. கவனிக்கவும், நாங்கள் மாதிரியை ice hockey பற்றிய ஒரு haiku உருவாக்குமாறு கேட்கிறோம், மேலும் உரையாடலின் user மற்றும் assistant பகுதிகளை குறிப்பிட சிறப்பு tokenகளுடன் அதைச் சுற்றி அமைக்கிறோம். மாதிரி prompt ஐ முடித்து haiku ஐ உருவாக்கும்.
- **device**: இந்த எடுத்துக்காட்டில் கணக்கீடுகளுக்கு CPU ஐ பயன்படுத்துகிறோம். Candle GPU-இல் CUDA மற்றும் Metal உடன் இயங்குவதற்கும் ஆதரவு அளிக்கிறது.

## படி 3: மாதிரி மற்றும் Tokenizer ஐ பதிவிறக்க/தயார் செய்யுதல்

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

`hf_hub` API ஐ பயன்படுத்தி Hugging Face மாதிரி hub-இல் இருந்து மாதிரி மற்றும் tokenizer கோப்புகளை பதிவிறக்குகிறோம். `gguf` கோப்பு quantized மாதிரி எடைகளைக் கொண்டுள்ளது, மேலும் `tokenizer.json` கோப்பு நமது உள்ளீட்டு உரையை token செய்ய பயன்படுத்தப்படுகிறது. ஒருமுறை பதிவிறக்கப்பட்ட பிறகு மாதிரி cache செய்யப்படும், எனவே முதல் செயல்பாடு மெதுவாக இருக்கும் (மாதிரியின் 2.4GB ஐ பதிவிறக்குவதால்), ஆனால் பின்னர் செயல்பாடுகள் வேகமாக இருக்கும்.

## படி 4: மாதிரியை ஏற்றுதல்

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Quantized மாதிரி எடைகளை நினைவகத்தில் ஏற்றுகிறோம் மற்றும் Phi-3 மாதிரியை ஆரம்பிக்கிறோம். இந்த படி `gguf` கோப்பிலிருந்து மாதிரி எடைகளைப் படிக்கிறது மற்றும் குறிப்பிட்ட சாதனத்தில் (இந்த எடுத்துக்காட்டில் CPU) முன்னறிவிப்புக்கான மாதிரியை அமைக்கிறது.

## படி 5: Prompt ஐ செயலாக்குதல் மற்றும் முன்னறிவிப்புக்குத் தயாராகுதல்

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

இந்த படியில், நாங்கள் உள்ளீட்டு prompt ஐ token செய்யிறோம் மற்றும் அதை token IDகளின் வரிசையாக மாற்றி முன்னறிவிப்புக்குத் தயாராகிறோம். `LogitsProcessor` ஐ initialize செய்து, கொடுக்கப்பட்ட `temperature` மற்றும் `top_p` மதிப்புகளின் அடிப்படையில் sampling செயல்முறையை (vocabulary-இல் probability distribution) கையாளுகிறோம். ஒவ்வொரு token ஐ tensor ஆக மாற்றி மாதிரியில் logits ஐ பெற அனுப்புகிறோம்.

Loop prompt இல் ஒவ்வொரு token ஐ செயலாக்குகிறது, logits processor ஐ புதுப்பிக்கிறது மற்றும் அடுத்த token உருவாக்கத்திற்குத் தயாராகிறது.

## படி 6: முன்னறிவிப்பு

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

முன்னறிவிப்பு loop இல், நாம் tokenகளை ஒன்றொன்றாக உருவாக்குகிறோம், sample length ஐ அடையும்வரை அல்லது end-of-sequence token ஐ சந்திக்கும்வரை. அடுத்த token tensor ஆக மாற்றி மாதிரியில் அனுப்பப்படுகிறது, மேலும் logits penalties மற்றும் sampling ஐப் பயன்படுத்த செயலாக்கப்படுகிறது. பின்னர் அடுத்த token sample செய்யப்படுகிறது, decode செய்யப்படுகிறது, மற்றும் வரிசையில் சேர்க்கப்படுகிறது.
மீண்டும் வரும் உரையைத் தவிர்க்க, `repeat_last_n` மற்றும் `repeat_penalty` அளவுருக்களின் அடிப்படையில் மீண்டும் வரும் tokenகளுக்கு penalty வழங்கப்படுகிறது.

இறுதியாக, உருவாக்கப்பட்ட உரை decode செய்யப்படும் போது அச்சிடப்படுகிறது, real-time output ஐ உறுதிசெய்கிறது.

## படி 7: பயன்பாட்டை இயக்குதல்

பயன்பாட்டை இயக்க, டெர்மினலில் பின்வரும் கட்டளையை இயக்கவும்:

```bash
cargo run --release
```

இது Phi-3 மாதிரியால் ice hockey பற்றிய haiku ஐ உருவாக்கி அச்சிட வேண்டும். இதுபோன்ற:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

அல்லது

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## முடிவு

இந்த படிகளைப் பின்பற்றுவதன் மூலம், நாங்கள் Phi-3 மாதிரியை ரஸ்ட் மற்றும் Candle மூலம் பயன்படுத்தி 100 வரிகளுக்குள் உரை உருவாக்க முடியும். இந்த குறியீடு மாதிரி ஏற்றுதல், tokenization மற்றும் முன்னறிவிப்பு ஆகியவற்றை கையாளுகிறது, tensors மற்றும் logits செயலாக்கத்தை பயன்படுத்தி உள்ளீட்டு prompt அடிப்படையில் தெளிவான உரையை உருவாக்குகிறது.

இந்த console பயன்பாடு Windows, Linux மற்றும் Mac OS-இல் இயங்கும். ரஸ்டின் portability காரணமாக, இந்த குறியீடு மொபைல் பயன்பாடுகளில் இயங்கும் ஒரு library ஆகவும் மாற்றப்படலாம் (console பயன்பாடுகளை அங்கு இயக்க முடியாது).

## இணைப்பு: முழு குறியீடு

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

குறிப்பு: aarch64 Linux அல்லது aarch64 Windows-இல் இந்த குறியீட்டை இயக்க, `.cargo/config` என்ற பெயரில் ஒரு கோப்பை பின்வரும் உள்ளடக்கத்துடன் சேர்க்கவும்:

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

> நீங்கள் ரஸ்ட் மற்றும் Candle உடன் Phi-3 மாதிரியைப் பயன்படுத்துவதற்கான மேலும் பல எடுத்துக்காட்டுகளுக்கு அதிகாரப்பூர்வ [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository ஐ பார்வையிடலாம், இதில் முன்னறிவிப்புக்கான மாற்று அணுகுமுறைகள் அடங்கும்.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.