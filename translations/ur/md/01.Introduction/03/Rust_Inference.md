<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2fa1ead890e358cc560ed4f9b3cf219a",
  "translation_date": "2025-04-03T06:58:39+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "ur"
}
-->
# کراس پلیٹ فارم انفرنس رَسٹ کے ساتھ

یہ ٹیوٹوریل ہمیں رَسٹ اور [Candle ML فریم ورک](https://github.com/huggingface/candle) کے ذریعے انفرنس کرنے کے عمل کی رہنمائی کرے گا، جو HuggingFace کی جانب سے فراہم کیا گیا ہے۔ رَسٹ کو انفرنس کے لیے استعمال کرنے کے کئی فوائد ہیں، خاص طور پر دیگر پروگرامنگ زبانوں کے مقابلے میں۔ رَسٹ اپنی بہترین کارکردگی کے لیے جانا جاتا ہے، جو C اور C++ کے برابر ہے۔ یہ اسے انفرنس کے کاموں کے لیے ایک بہترین انتخاب بناتا ہے، جو کہ کمپیوٹیشنل طور پر بھاری ہو سکتے ہیں۔ خاص طور پر، یہ زیرو کاسٹ ایبسٹریکشنز اور مؤثر میموری مینجمنٹ کی وجہ سے ہوتا ہے، جس میں گاربیج کلیکشن کا کوئی اوورہیڈ نہیں ہوتا۔ رَسٹ کی کراس پلیٹ فارم صلاحیتیں ایسے کوڈ کی ڈیولپمنٹ کو ممکن بناتی ہیں جو مختلف آپریٹنگ سسٹمز، جیسے ونڈوز، میک او ایس، اور لینکس، کے ساتھ ساتھ موبائل آپریٹنگ سسٹمز پر بغیر کسی اہم تبدیلی کے چل سکتے ہیں۔

اس ٹیوٹوریل کو فالو کرنے کے لیے ضروری ہے کہ آپ [رَسٹ انسٹال کریں](https://www.rust-lang.org/tools/install)، جو رَسٹ کمپائلر اور پیکیج مینیجر، Cargo، شامل کرتا ہے۔

## مرحلہ 1: نیا رَسٹ پروجیکٹ بنائیں

نیا رَسٹ پروجیکٹ بنانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo new phi-console-app
```

یہ ایک ابتدائی پروجیکٹ اسٹرکچر جنریٹ کرے گا جس میں `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` فائل شامل ہوگی:

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

## مرحلہ 2: بنیادی پیرامیٹرز ترتیب دیں

`main.rs` فائل کے اندر، ہم انفرنس کے لیے ابتدائی پیرامیٹرز سیٹ کریں گے۔ سادگی کے لیے، یہ سب ہارڈ کوڈ کیے جائیں گے، لیکن ہم انہیں حسب ضرورت تبدیل کر سکتے ہیں۔

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

- **temperature**: سیمپلنگ کے عمل کی بے ترتیبی کو کنٹرول کرتا ہے۔
- **sample_len**: جنریٹ ہونے والے ٹیکسٹ کی زیادہ سے زیادہ لمبائی کا تعین کرتا ہے۔
- **top_p**: نیوکلئیس سیمپلنگ کے لیے استعمال ہوتا ہے تاکہ ہر قدم کے لیے محدود ٹوکنز پر غور کیا جائے۔
- **repeat_last_n**: ان ٹوکنز کی تعداد کو کنٹرول کرتا ہے جن پر ریپیٹیٹیو سیکوینسز کو روکنے کے لیے پینلٹی لگائی جاتی ہے۔
- **repeat_penalty**: ریپیٹڈ ٹوکنز کو روکنے کے لیے پینلٹی ویلیو۔
- **seed**: ایک رینڈم سیڈ (بہتر ریپروڈیوسیبلٹی کے لیے ہم مستقل ویلیو استعمال کر سکتے ہیں)۔
- **prompt**: جنریشن شروع کرنے کے لیے ابتدائی پرامپٹ ٹیکسٹ۔ نوٹ کریں کہ ہم ماڈل سے آئس ہاکی کے بارے میں ایک ہائیکو جنریٹ کرنے کو کہتے ہیں، اور اسے خاص ٹوکنز کے ساتھ لپیٹتے ہیں تاکہ صارف اور اسسٹنٹ کے حصے کی گفتگو کو ظاہر کیا جا سکے۔ ماڈل پرامپٹ کو مکمل کر کے ایک ہائیکو جنریٹ کرے گا۔
- **device**: اس مثال میں ہم کمپیوٹیشن کے لیے CPU استعمال کرتے ہیں۔ Candle GPU کے ساتھ CUDA اور Metal پر چلنے کی بھی سپورٹ فراہم کرتا ہے۔

## مرحلہ 3: ماڈل اور ٹوکنائزر ڈاؤنلوڈ/تیار کریں

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

ہم `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` فائل کو اپنے انپٹ ٹیکسٹ کو ٹوکنائز کرنے کے لیے استعمال کرتے ہیں۔ ایک بار ڈاؤنلوڈ ہونے کے بعد ماڈل کیش ہو جاتا ہے، اس لیے پہلی بار عمل سست ہوگا (کیونکہ یہ ماڈل کے 2.4GB ڈاؤنلوڈ کرے گا) لیکن اگلی بار عمل تیز ہوگا۔

## مرحلہ 4: ماڈل لوڈ کریں

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ہم کوانٹائزڈ ماڈل ویٹس کو میموری میں لوڈ کرتے ہیں اور Phi-3 ماڈل کو انیشیلائز کرتے ہیں۔ اس مرحلے میں `gguf` فائل سے ماڈل ویٹس کو پڑھنا اور مخصوص ڈیوائس (اس مثال میں CPU) پر انفرنس کے لیے ماڈل سیٹ اپ کرنا شامل ہے۔

## مرحلہ 5: پرامپٹ پروسیس کریں اور انفرنس کے لیے تیار کریں

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

اس مرحلے میں، ہم انپٹ پرامپٹ کو ٹوکنائز کرتے ہیں اور اسے انفرنس کے لیے تیار کرتے ہیں، یعنی اسے ٹوکن IDs کی سیکوینس میں تبدیل کرتے ہیں۔ ہم `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ویلیوز بھی انیشیلائز کرتے ہیں۔ ہر ٹوکن کو ٹینسر میں تبدیل کر کے ماڈل کے ذریعے لاجٹس حاصل کیے جاتے ہیں۔

یہ لوپ پرامپٹ کے ہر ٹوکن کو پروسیس کرتا ہے، لاجٹس پروسیسر کو اپڈیٹ کرتا ہے اور اگلے ٹوکن جنریشن کے لیے تیار کرتا ہے۔

## مرحلہ 6: انفرنس

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

انفرنس لوپ میں، ہم ایک ایک کر کے ٹوکنز جنریٹ کرتے ہیں جب تک کہ مطلوبہ سیمپل لمبائی تک نہ پہنچ جائیں یا اینڈ آف سیکوینس ٹوکن کا سامنا نہ ہو۔ اگلا ٹوکن ٹینسر میں تبدیل کر کے ماڈل کے ذریعے پروسیس کیا جاتا ہے، جبکہ لاجٹس پر پینلٹیز اور سیمپلنگ اپلائی کی جاتی ہیں۔ پھر اگلا ٹوکن سیمپل، ڈی کوڈ اور سیکوینس میں شامل کیا جاتا ہے۔

ریپیٹیٹو ٹیکسٹ سے بچنے کے لیے، `repeat_last_n` and `repeat_penalty` پیرامیٹرز کی بنیاد پر ریپیٹڈ ٹوکنز پر پینلٹی اپلائی کی جاتی ہے۔

آخر میں، جنریٹڈ ٹیکسٹ کو ڈی کوڈ کر کے پرنٹ کیا جاتا ہے، تاکہ ریئل ٹائم آؤٹ پٹ دکھایا جا سکے۔

## مرحلہ 7: ایپلیکیشن چلائیں

ایپلیکیشن چلانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo run --release
```

یہ آئس ہاکی کے بارے میں ایک ہائیکو پرنٹ کرے گا جو Phi-3 ماڈل نے جنریٹ کیا ہے۔ کچھ اس طرح:

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

## نتیجہ

ان مراحل کو فالو کر کے، ہم Phi-3 ماڈل کے ذریعے رَسٹ اور Candle کا استعمال کرتے ہوئے 100 لائنز سے کم کوڈ میں ٹیکسٹ جنریشن کر سکتے ہیں۔ کوڈ ماڈل لوڈنگ، ٹوکنائزیشن، اور انفرنس کو ہینڈل کرتا ہے، ٹینسرز اور لاجٹس پروسیسنگ کا فائدہ اٹھاتے ہوئے انپٹ پرامپٹ کی بنیاد پر مربوط ٹیکسٹ جنریٹ کرتا ہے۔

یہ کنسول ایپلیکیشن ونڈوز، لینکس، اور میک او ایس پر چل سکتی ہے۔ رَسٹ کی پورٹیبیلیٹی کی وجہ سے، کوڈ کو موبائل ایپس میں چلنے والی لائبریری میں بھی تبدیل کیا جا سکتا ہے (کنسول ایپس وہاں نہیں چل سکتیں، ظاہر ہے)۔

## ضمیمہ: مکمل کوڈ

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

نوٹ: اگر آپ اس کوڈ کو aarch64 Linux یا aarch64 Windows پر چلانا چاہتے ہیں، تو `.cargo/config` نامی ایک فائل بنائیں جس میں درج ذیل مواد ہو:

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

> آپ Candle کے آفیشل [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ریپوزیٹری پر مزید مثالوں کے لیے جا سکتے ہیں کہ Phi-3 ماڈل کو رَسٹ اور Candle کے ساتھ کیسے استعمال کیا جائے، بشمول انفرنس کے متبادل طریقے۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمے کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔