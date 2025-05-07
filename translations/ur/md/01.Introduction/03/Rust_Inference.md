<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-07T14:40:28+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ur"
}
-->
# Cross-platform inference with Rust

یہ ٹیوٹوریل ہمیں Rust اور HuggingFace کے [Candle ML framework](https://github.com/huggingface/candle) کے ذریعے inference کرنے کے عمل سے روشناس کرائے گا۔ Rust کو inference کے لیے استعمال کرنے کے کئی فائدے ہیں، خاص طور پر جب اسے دیگر پروگرامنگ زبانوں سے موازنہ کیا جائے۔ Rust اپنی اعلیٰ کارکردگی کے لیے جانا جاتا ہے، جو C اور C++ کے برابر ہے۔ یہی اسے inference کے کاموں کے لیے بہترین انتخاب بناتا ہے، جو عموماً کمپیوٹیشنل لحاظ سے بھاری ہوتے ہیں۔ خاص طور پر، یہ صفر-لاگت abstraction اور مؤثر میموری مینجمنٹ کی بدولت ہے، جس میں کوئی garbage collection کا بوجھ نہیں ہوتا۔ Rust کی cross-platform صلاحیتیں مختلف آپریٹنگ سسٹمز جیسے Windows، macOS، Linux، اور موبائل آپریٹنگ سسٹمز پر بغیر کوڈ میں بڑی تبدیلی کے چلنے کی اجازت دیتی ہیں۔

اس ٹیوٹوریل کو فالو کرنے کے لیے شرط ہے کہ آپ نے [Rust انسٹال](https://www.rust-lang.org/tools/install) کیا ہو، جس میں Rust compiler اور Cargo، Rust کا پیکج مینیجر شامل ہے۔

## Step 1: Create a New Rust Project

نیا Rust پروجیکٹ بنانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo new phi-console-app
```

یہ ایک ابتدائی پروجیکٹ کا ڈھانچہ تیار کرتا ہے جس میں `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` فائل شامل ہے:

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

main.rs فائل کے اندر، ہم اپنے inference کے ابتدائی پیرامیٹرز سیٹ کریں گے۔ آسانی کے لیے یہ سب hardcoded ہوں گے، لیکن ضرورت کے مطابق انہیں تبدیل کیا جا سکتا ہے۔

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

- **temperature**: سیمپلنگ کے عمل میں randomness کو کنٹرول کرتا ہے۔
- **sample_len**: جنریٹ کیے جانے والے متن کی زیادہ سے زیادہ لمبائی بتاتا ہے۔
- **top_p**: nucleus sampling کے لیے استعمال ہوتا ہے تاکہ ہر قدم پر غور کیے جانے والے tokens کی تعداد محدود کی جا سکے۔
- **repeat_last_n**: اس بات کو کنٹرول کرتا ہے کہ کتنے tokens پر penalty لگائی جائے تاکہ بار بار دہرائے جانے والے جملوں سے بچا جا سکے۔
- **repeat_penalty**: دہرائے جانے والے tokens کو روکنے کے لیے penalty کی قیمت۔
- **seed**: ایک random seed (بہتر reproducibility کے لیے مستقل ویلیو بھی استعمال کی جا سکتی ہے)۔
- **prompt**: جنریشن شروع کرنے کے لیے ابتدائی متن۔ دھیان دیں کہ ہم ماڈل سے ice hockey پر ایک haiku بنانے کو کہتے ہیں، اور ہم اسے user اور assistant کے conversation حصوں کو ظاہر کرنے کے لیے خاص tokens کے ساتھ لپیٹتے ہیں۔ ماڈل پھر اس prompt کو haiku کے ساتھ مکمل کرے گا۔
- **device**: اس مثال میں ہم computation کے لیے CPU استعمال کر رہے ہیں۔ Candle GPU پر CUDA اور Metal کے ساتھ چلانے کی بھی حمایت کرتا ہے۔

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

ہم `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` فائل کو اپنے input متن کو tokenizing کرنے کے لیے استعمال کرتے ہیں۔ ماڈل ڈاؤن لوڈ ہونے کے بعد cache ہو جاتا ہے، اس لیے پہلی بار execution سست ہو گی (کیونکہ ماڈل کے 2.4GB ڈاؤن لوڈ ہوتے ہیں) لیکن بعد کی executionز تیز ہوں گی۔

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ہم quantized ماڈل کے وزن memory میں لوڈ کرتے ہیں اور Phi-3 ماڈل کو initialize کرتے ہیں۔ اس مرحلے میں `gguf` فائل سے ماڈل وزن پڑھنا اور مخصوص device (اس کیس میں CPU) پر inference کے لیے ماڈل سیٹ کرنا شامل ہے۔

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

اس مرحلے میں، ہم input prompt کو tokenize کرتے ہیں اور اسے token IDs کی ترتیب میں تبدیل کر کے inference کے لیے تیار کرتے ہیں۔ ہم `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ویلیوز کو بھی initialize کرتے ہیں۔ ہر token کو tensor میں تبدیل کر کے ماڈل سے logits حاصل کیے جاتے ہیں۔

لوپ prompt کے ہر token کو process کرتا ہے، logits processor کو اپڈیٹ کرتا ہے اور اگلے token کی جنریشن کے لیے تیار کرتا ہے۔

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

inference کے لوپ میں، ہم tokens کو ایک ایک کر کے جنریٹ کرتے ہیں جب تک کہ مطلوبہ sample length تک نہ پہنچ جائیں یا end-of-sequence token نہ مل جائے۔ اگلا token tensor میں تبدیل کر کے ماڈل سے گزارا جاتا ہے، اور logits کو penalties اور sampling کے لیے process کیا جاتا ہے۔ پھر اگلا token sample کیا جاتا ہے، decode کیا جاتا ہے، اور sequence میں شامل کیا جاتا ہے۔  
بار بار دہرائے جانے والے متن سے بچنے کے لیے، `repeat_last_n` and `repeat_penalty` پیرامیٹرز کی بنیاد پر repeated tokens پر penalty لگائی جاتی ہے۔

آخر میں، جنریٹ کیا گیا متن decode ہوتے ہی پرنٹ کیا جاتا ہے، تاکہ real-time streaming آؤٹ پٹ یقینی بنایا جا سکے۔

## Step 7: Run the Application

ایپلیکیشن چلانے کے لیے، ٹرمینل میں درج ذیل کمانڈ execute کریں:

```bash
cargo run --release
```

یہ Phi-3 ماڈل کے ذریعے ice hockey پر ایک haiku پرنٹ کرے گا۔ کچھ اس طرح:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

یا

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

ان مراحل کو فالو کر کے، ہم Phi-3 ماڈل کے ساتھ Rust اور Candle استعمال کرتے ہوئے 100 لائنوں سے کم کوڈ میں متن کی جنریشن کر سکتے ہیں۔ کوڈ ماڈل لوڈنگ، tokenization، اور inference کو ہینڈل کرتا ہے، tensors اور logits processing کا فائدہ اٹھاتے ہوئے input prompt کی بنیاد پر coherent متن تیار کرتا ہے۔

یہ console application Windows، Linux، اور Mac OS پر چل سکتا ہے۔ Rust کی portability کی وجہ سے، کوڈ کو موبائل ایپس کے اندر چلنے والی لائبریری میں بھی تبدیل کیا جا سکتا ہے (کیونکہ ہم وہاں console apps نہیں چلا سکتے)۔

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

نوٹ: aarch64 Linux یا aarch64 Windows پر یہ کوڈ چلانے کے لیے، `.cargo/config` نامی فائل بنائیں اور درج ذیل مواد شامل کریں:

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

> آپ مزید مثالوں کے لیے [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) کے official repository کا دورہ کر سکتے ہیں، جہاں Rust اور Candle کے ساتھ Phi-3 ماڈل کے استعمال کے متبادل طریقے اور inference کی مثالیں دستیاب ہیں۔

**دستخطی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔