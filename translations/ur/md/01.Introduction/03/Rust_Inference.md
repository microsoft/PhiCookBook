# کراس-پلیٹ فارم انفرنس ود رسٹ

یہ ٹیوٹوریل ہمیں رسٹ اور [Candle ML framework](https://github.com/huggingface/candle) کے ذریعے انفرنس کرنے کے عمل سے گزاریگا۔ رسٹ کا استعمال انفرنس کے لیے کئی فوائد فراہم کرتا ہے، خاص طور پر جب اسے دیگر پروگرامنگ زبانوں سے موازنہ کیا جائے۔ رسٹ اپنی اعلیٰ کارکردگی کے لیے جانا جاتا ہے، جو C اور C++ کے برابر ہے۔ یہ انفرنس کے کاموں کے لیے ایک بہترین انتخاب ہے، جو اکثر کمپیوٹیشنل طور پر بھاری ہوتے ہیں۔ خاص طور پر، یہ زیرو-کوسٹ ابسٹریکشنز اور موثر میموری مینجمنٹ کی بدولت ہے، جس میں کوئی گاربیج کلیکشن کا اوور ہیڈ نہیں ہوتا۔ رسٹ کی کراس-پلیٹ فارم صلاحیتیں کوڈ کی ترقی کو ممکن بناتی ہیں جو مختلف آپریٹنگ سسٹمز جیسے ونڈوز، میک او ایس، اور لینکس کے ساتھ ساتھ موبائل آپریٹنگ سسٹمز پر بھی بغیر کسی بڑی تبدیلی کے چل سکتا ہے۔

اس ٹیوٹوریل کو فالو کرنے کے لیے ضروری ہے کہ آپ [رسٹ انسٹال کریں](https://www.rust-lang.org/tools/install)، جس میں رسٹ کمپائلر اور کارگو، رسٹ کا پیکیج مینیجر شامل ہے۔

## مرحلہ 1: نیا رسٹ پروجیکٹ بنائیں

نیا رسٹ پروجیکٹ بنانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo new phi-console-app
```

یہ ایک ابتدائی پروجیکٹ اسٹرکچر تیار کرتا ہے جس میں `Cargo.toml` فائل اور `src` ڈائریکٹری شامل ہے جس میں `main.rs` فائل موجود ہے۔

اگلے مرحلے میں، ہم اپنی dependencies یعنی `candle`, `hf-hub` اور `tokenizers` crates کو `Cargo.toml` فائل میں شامل کریں گے:

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

`main.rs` فائل کے اندر، ہم اپنی انفرنس کے ابتدائی پیرامیٹرز سیٹ کریں گے۔ یہ سب سادگی کے لیے ہارڈ کوڈ کیے جائیں گے، لیکن ضرورت کے مطابق انہیں تبدیل کیا جا سکتا ہے۔

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
- **sample_len**: پیدا ہونے والے متن کی زیادہ سے زیادہ لمبائی بتاتا ہے۔
- **top_p**: نیوکلئیس سیمپلنگ کے لیے استعمال ہوتا ہے تاکہ ہر قدم کے لیے زیر غور ٹوکنز کی تعداد محدود کی جا سکے۔
- **repeat_last_n**: دہرائے جانے والے سلسلوں کو روکنے کے لیے سزا لگانے کے لیے زیر غور ٹوکنز کی تعداد کو کنٹرول کرتا ہے۔
- **repeat_penalty**: دہرائے جانے والے ٹوکنز کو روکنے کے لیے سزا کی قیمت۔
- **seed**: ایک رینڈم سیڈ (بہتر دوبارہ پیداوار کے لیے ہم مستقل ویلیو استعمال کر سکتے ہیں)۔
- **prompt**: جنریشن شروع کرنے کے لیے ابتدائی پرامپٹ ٹیکسٹ۔ دھیان دیں کہ ہم ماڈل سے آئس ہاکی کے بارے میں ایک ہائیکو بنانے کو کہتے ہیں، اور ہم اسے خاص ٹوکنز کے ساتھ لپیٹتے ہیں تاکہ گفتگو کے یوزر اور اسسٹنٹ حصے کی نشاندہی ہو۔ ماڈل پھر اس پرامپٹ کو ہائیکو کے ساتھ مکمل کرے گا۔
- **device**: اس مثال میں ہم کمپیوٹیشن کے لیے CPU استعمال کر رہے ہیں۔ Candle GPU پر CUDA اور Metal کے ساتھ چلانے کی بھی حمایت کرتا ہے۔

## مرحلہ 3: ماڈل اور ٹوکنائزر ڈاؤن لوڈ/تیار کریں

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

ہم `hf_hub` API کا استعمال کرتے ہوئے Hugging Face ماڈل ہب سے ماڈل اور ٹوکنائزر فائلیں ڈاؤن لوڈ کرتے ہیں۔ `gguf` فائل میں کوانٹائزڈ ماڈل ویٹس ہوتے ہیں، جبکہ `tokenizer.json` فائل ہمارے ان پٹ ٹیکسٹ کو ٹوکنائز کرنے کے لیے استعمال ہوتی ہے۔ ایک بار ڈاؤن لوڈ ہونے کے بعد ماڈل کیش ہو جاتا ہے، اس لیے پہلی بار چلانے میں وقت لگے گا (کیونکہ یہ 2.4GB ماڈل ڈاؤن لوڈ کرتا ہے) لیکن بعد کے اجراء تیز ہوں گے۔

## مرحلہ 4: ماڈل لوڈ کریں

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ہم کوانٹائزڈ ماڈل ویٹس کو میموری میں لوڈ کرتے ہیں اور Phi-3 ماڈل کو انیشیالائز کرتے ہیں۔ اس مرحلے میں `gguf` فائل سے ماڈل ویٹس پڑھنا اور مخصوص ڈیوائس (اس کیس میں CPU) پر انفرنس کے لیے ماڈل سیٹ اپ کرنا شامل ہے۔

## مرحلہ 5: پرامپٹ کو پراسیس کریں اور انفرنس کے لیے تیار کریں

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

اس مرحلے میں، ہم ان پٹ پرامپٹ کو ٹوکنائز کرتے ہیں اور اسے ٹوکن آئی ڈیز کی ترتیب میں تبدیل کر کے انفرنس کے لیے تیار کرتے ہیں۔ ہم `LogitsProcessor` کو بھی انیشیالائز کرتے ہیں تاکہ دی گئی `temperature` اور `top_p` ویلیوز کی بنیاد پر سیمپلنگ کے عمل (ووکابیولری پر احتمال کی تقسیم) کو سنبھالا جا سکے۔ ہر ٹوکن کو ٹینسر میں تبدیل کیا جاتا ہے اور ماڈل کے ذریعے لاگٹس حاصل کیے جاتے ہیں۔

لوپ پرامپٹ کے ہر ٹوکن کو پراسیس کرتا ہے، لاگٹس پروسیسر کو اپ ڈیٹ کرتا ہے اور اگلے ٹوکن کی جنریشن کے لیے تیار ہوتا ہے۔

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

انفرنس لوپ میں، ہم ٹوکنز کو ایک ایک کر کے جنریٹ کرتے ہیں جب تک کہ مطلوبہ sample length تک نہ پہنچ جائیں یا end-of-sequence ٹوکن نہ مل جائے۔ اگلا ٹوکن ٹینسر میں تبدیل کیا جاتا ہے اور ماڈل کے ذریعے پاس کیا جاتا ہے، جبکہ لاگٹس کو سزا اور سیمپلنگ کے لیے پروسیس کیا جاتا ہے۔ پھر اگلا ٹوکن سیمپل کیا جاتا ہے، ڈیکوڈ کیا جاتا ہے، اور ترتیب میں شامل کیا جاتا ہے۔
دہرائے جانے والے متن سے بچنے کے لیے، `repeat_last_n` اور `repeat_penalty` پیرامیٹرز کی بنیاد پر دہرائے جانے والے ٹوکنز پر سزا لگائی جاتی ہے۔

آخر میں، پیدا شدہ متن کو جیسے ہی ڈیکوڈ کیا جاتا ہے پرنٹ کیا جاتا ہے، تاکہ ریئل ٹائم آؤٹ پٹ فراہم ہو۔

## مرحلہ 7: ایپلیکیشن چلائیں

ایپلیکیشن چلانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo run --release
```

یہ Phi-3 ماڈل کی جانب سے آئس ہاکی کے بارے میں ایک ہائیکو پرنٹ کرے گا۔ کچھ اس طرح:

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

ان مراحل کی پیروی کرتے ہوئے، ہم Phi-3 ماڈل کے ساتھ رسٹ اور Candle کا استعمال کرتے ہوئے 100 لائنوں سے کم کوڈ میں ٹیکسٹ جنریشن کر سکتے ہیں۔ کوڈ ماڈل لوڈنگ، ٹوکنائزیشن، اور انفرنس کو ہینڈل کرتا ہے، ٹینسرز اور لاگٹس پروسیسنگ کا فائدہ اٹھاتے ہوئے ان پٹ پرامپٹ کی بنیاد پر مربوط متن پیدا کرتا ہے۔

یہ کنسول ایپلیکیشن ونڈوز، لینکس اور میک او ایس پر چل سکتی ہے۔ رسٹ کی پورٹیبلٹی کی وجہ سے، کوڈ کو موبائل ایپس کے اندر چلنے والی لائبریری میں بھی تبدیل کیا جا سکتا ہے (کیونکہ ہم وہاں کنسول ایپس نہیں چلا سکتے)۔

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

نوٹ: aarch64 لینکس یا aarch64 ونڈوز پر اس کوڈ کو چلانے کے لیے، `.cargo/config` نامی فائل بنائیں اور اس میں درج ذیل مواد شامل کریں:

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

> آپ مزید مثالوں کے لیے [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) کے آفیشل ریپوزیٹری کا دورہ کر سکتے ہیں، جہاں رسٹ اور Candle کے ساتھ Phi-3 ماڈل کے استعمال کے مختلف طریقے اور انفرنس کے متبادل طریقے موجود ہیں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔