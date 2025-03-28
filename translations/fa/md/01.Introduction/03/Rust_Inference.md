<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-03-27T08:09:35+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "fa"
}
-->
# استنتاج بین‌پلتفرمی با Rust

این آموزش ما را از طریق فرآیند انجام استنتاج با استفاده از زبان Rust و [چارچوب Candle ML](https://github.com/huggingface/candle) از HuggingFace راهنمایی می‌کند. استفاده از Rust برای استنتاج مزایای زیادی دارد، به‌ویژه در مقایسه با زبان‌های برنامه‌نویسی دیگر. Rust به دلیل عملکرد بالای خود که قابل مقایسه با زبان‌های C و C++ است، شناخته شده است. این ویژگی آن را به انتخابی عالی برای وظایف استنتاج که می‌توانند محاسباتی سنگین باشند، تبدیل می‌کند. به‌ویژه این موضوع به دلیل انتزاعات بدون هزینه و مدیریت کارآمد حافظه است که هیچ سربار جمع‌آوری زباله ندارد. قابلیت‌های بین‌پلتفرمی Rust امکان توسعه کدی را فراهم می‌کند که بدون تغییرات عمده روی سیستم‌عامل‌های مختلف از جمله ویندوز، macOS، لینوکس و سیستم‌عامل‌های موبایل اجرا می‌شود.

پیش‌نیاز دنبال کردن این آموزش، [نصب Rust](https://www.rust-lang.org/tools/install) است که شامل کامپایلر Rust و مدیر بسته Cargo می‌شود.

## مرحله ۱: ایجاد یک پروژه جدید Rust

برای ایجاد یک پروژه جدید Rust، دستور زیر را در ترمینال اجرا کنید:

```bash
cargo new phi-console-app
```

این دستور ساختار اولیه پروژه را با فایل‌های `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` تولید می‌کند:

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

## مرحله ۲: تنظیم پارامترهای اولیه

داخل فایل main.rs، پارامترهای اولیه برای استنتاج را تنظیم خواهیم کرد. این پارامترها به‌صورت ثابت تنظیم می‌شوند برای ساده‌سازی، اما می‌توانیم آنها را بر اساس نیاز تغییر دهیم.

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

- **temperature**: کنترل‌کننده تصادفی بودن فرآیند نمونه‌گیری.
- **sample_len**: طول حداکثر متن تولید شده را مشخص می‌کند.
- **top_p**: برای نمونه‌گیری هسته‌ای استفاده می‌شود تا تعداد توکن‌های موردنظر برای هر مرحله محدود شود.
- **repeat_last_n**: تعداد توکن‌هایی که برای اعمال جریمه جهت جلوگیری از توالی‌های تکراری در نظر گرفته می‌شوند.
- **repeat_penalty**: مقدار جریمه برای جلوگیری از تکرار توکن‌ها.
- **seed**: یک مقدار تصادفی (می‌توانیم برای بازتولید بهتر از یک مقدار ثابت استفاده کنیم).
- **prompt**: متن اولیه‌ای که تولید متن از آن آغاز می‌شود. توجه کنید که از مدل می‌خواهیم یک هایکو درباره هاکی روی یخ تولید کند و آن را با توکن‌های ویژه‌ای برای مشخص کردن بخش‌های کاربر و دستیار مکالمه می‌پیچیم. سپس مدل متن را با یک هایکو کامل می‌کند.
- **device**: در این مثال از CPU برای محاسبات استفاده می‌کنیم. Candle پشتیبانی از اجرای روی GPU با CUDA و Metal را نیز فراهم می‌کند.

## مرحله ۳: دانلود/آماده‌سازی مدل و توکنایزر

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

از فایل `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` برای توکن‌سازی متن ورودی استفاده می‌کنیم. پس از دانلود، مدل در حافظه کش ذخیره می‌شود، بنابراین اجرای اول ممکن است کند باشد (زیرا مدل ۲.۴ گیگابایتی را دانلود می‌کند) اما اجراهای بعدی سریع‌تر خواهند بود.

## مرحله ۴: بارگذاری مدل

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

وزن‌های مدل کوانتایزشده را به حافظه بارگذاری می‌کنیم و مدل Phi-3 را مقداردهی اولیه می‌کنیم. این مرحله شامل خواندن وزن‌های مدل از فایل `gguf` و تنظیم مدل برای استنتاج روی دستگاه مشخص شده (در اینجا CPU) است.

## مرحله ۵: پردازش پرامپت و آماده‌سازی برای استنتاج

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

در این مرحله، متن ورودی توکنایز شده و برای استنتاج آماده می‌شود، به‌طوری‌که به یک دنباله از شناسه‌های توکن تبدیل می‌شود. همچنین مقادیر `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` مقداردهی اولیه می‌شوند. هر توکن به یک تنسور تبدیل شده و از طریق مدل عبور داده می‌شود تا logits تولید شود.

این حلقه هر توکن موجود در پرامپت را پردازش کرده، پردازشگر logits را به‌روزرسانی می‌کند و برای تولید توکن بعدی آماده می‌شود.

## مرحله ۶: استنتاج

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

در حلقه استنتاج، توکن‌ها یک به یک تولید می‌شوند تا زمانی که به طول نمونه موردنظر برسیم یا به توکن پایان دنباله برسیم. توکن بعدی به تنسور تبدیل شده و از طریق مدل عبور داده می‌شود، در حالی که logits برای اعمال جریمه‌ها و نمونه‌گیری پردازش می‌شود. سپس توکن بعدی نمونه‌گیری، رمزگشایی و به دنباله اضافه می‌شود.
برای جلوگیری از متن تکراری، جریمه‌ای بر اساس پارامترهای `repeat_last_n` and `repeat_penalty` به توکن‌های تکراری اعمال می‌شود.

در نهایت، متن تولید شده به‌صورت رمزگشایی‌شده چاپ می‌شود و خروجی به‌صورت لحظه‌ای جریان پیدا می‌کند.

## مرحله ۷: اجرای برنامه

برای اجرای برنامه، دستور زیر را در ترمینال اجرا کنید:

```bash
cargo run --release
```

این دستور باید یک هایکو درباره هاکی روی یخ تولید شده توسط مدل Phi-3 را چاپ کند. چیزی شبیه به:

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

## نتیجه‌گیری

با دنبال کردن این مراحل، می‌توانیم تولید متن با استفاده از مدل Phi-3 با Rust و Candle را در کمتر از ۱۰۰ خط کد انجام دهیم. این کد بارگذاری مدل، توکن‌سازی و استنتاج را مدیریت می‌کند و با استفاده از تنسورها و پردازش logits متن منسجمی بر اساس پرامپت ورودی تولید می‌کند.

این برنامه کنسولی می‌تواند روی ویندوز، لینوکس و macOS اجرا شود. به دلیل قابلیت حمل Rust، کد همچنین می‌تواند به کتابخانه‌ای تبدیل شود که در داخل اپلیکیشن‌های موبایل اجرا شود (چراکه نمی‌توانیم برنامه‌های کنسولی را در آنجا اجرا کنیم).

## پیوست: کد کامل

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

توجه: برای اجرای این کد روی لینوکس aarch64 یا ویندوز aarch64، یک فایل با نام `.cargo/config` با محتوای زیر اضافه کنید:

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

> می‌توانید برای مشاهده نمونه‌های رسمی بیشتر در مورد استفاده از مدل Phi-3 با Rust و Candle، از جمله رویکردهای جایگزین برای استنتاج، به مخزن [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) مراجعه کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.