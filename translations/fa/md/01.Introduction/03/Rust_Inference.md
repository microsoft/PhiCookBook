# استنتاج چندسکویی با Rust

این آموزش ما را در فرآیند انجام استنتاج با استفاده از Rust و [چارچوب یادگیری ماشین Candle](https://github.com/huggingface/candle) از HuggingFace راهنمایی می‌کند. استفاده از Rust برای استنتاج مزایای متعددی دارد، به‌ویژه در مقایسه با سایر زبان‌های برنامه‌نویسی. Rust به خاطر عملکرد بالایش شناخته شده است که با زبان‌های C و C++ قابل مقایسه است. این موضوع آن را به گزینه‌ای عالی برای وظایف استنتاج تبدیل می‌کند که معمولاً محاسباتی سنگین هستند. به‌ویژه، این به دلیل انتزاعات بدون هزینه و مدیریت بهینه حافظه است که بدون سربار جمع‌آوری زباله انجام می‌شود. قابلیت‌های چندسکویی Rust امکان توسعه کدی را فراهم می‌کند که روی سیستم‌عامل‌های مختلف از جمله ویندوز، مک‌اواس و لینوکس و همچنین سیستم‌عامل‌های موبایل بدون تغییرات قابل توجه در کد اجرا شود.

پیش‌نیاز دنبال کردن این آموزش، [نصب Rust](https://www.rust-lang.org/tools/install) است که شامل کامپایلر Rust و Cargo، مدیر بسته Rust، می‌شود.

## مرحله ۱: ایجاد پروژه جدید Rust

برای ایجاد یک پروژه جدید Rust، دستور زیر را در ترمینال اجرا کنید:

```bash
cargo new phi-console-app
```

این دستور ساختار اولیه پروژه را با فایل `Cargo.toml` و پوشه `src` که شامل فایل `main.rs` است، ایجاد می‌کند.

سپس، وابستگی‌های خود را - یعنی crateهای `candle`، `hf-hub` و `tokenizers` - به فایل `Cargo.toml` اضافه می‌کنیم:

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

## مرحله ۲: پیکربندی پارامترهای پایه

در فایل main.rs، پارامترهای اولیه برای استنتاج را تنظیم می‌کنیم. برای سادگی همه آن‌ها به صورت ثابت تعریف شده‌اند، اما می‌توانیم در صورت نیاز آن‌ها را تغییر دهیم.

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

- **temperature**: میزان تصادفی بودن فرآیند نمونه‌گیری را کنترل می‌کند.
- **sample_len**: حداکثر طول متن تولید شده را مشخص می‌کند.
- **top_p**: برای نمونه‌گیری هسته‌ای استفاده می‌شود تا تعداد توکن‌های در نظر گرفته شده در هر مرحله محدود شود.
- **repeat_last_n**: تعداد توکن‌هایی که برای اعمال جریمه به منظور جلوگیری از تکرارهای مکرر در نظر گرفته می‌شوند را کنترل می‌کند.
- **repeat_penalty**: مقدار جریمه برای جلوگیری از تکرار توکن‌ها است.
- **seed**: یک مقدار تصادفی اولیه (می‌توانیم از مقدار ثابت برای تکرارپذیری بهتر استفاده کنیم).
- **prompt**: متن اولیه برای شروع تولید است. توجه کنید که از مدل می‌خواهیم یک هایکو درباره هاکی روی یخ تولید کند و آن را با توکن‌های خاصی که بخش‌های کاربر و دستیار را مشخص می‌کنند، می‌بندیم. مدل سپس هایکو را کامل می‌کند.
- **device**: در این مثال از CPU برای محاسبات استفاده می‌کنیم. Candle همچنین از اجرای روی GPU با CUDA و Metal پشتیبانی می‌کند.

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

ما از API `hf_hub` برای دانلود فایل‌های مدل و توکنایزر از مخزن مدل Hugging Face استفاده می‌کنیم. فایل `gguf` شامل وزن‌های مدل کوانتیزه شده است، در حالی که فایل `tokenizer.json` برای توکنیزه کردن متن ورودی ما به کار می‌رود. پس از دانلود، مدل کش می‌شود، بنابراین اجرای اول کند خواهد بود (چون ۲.۴ گیگابایت مدل دانلود می‌شود) اما اجراهای بعدی سریع‌تر خواهند بود.

## مرحله ۴: بارگذاری مدل

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

وزن‌های مدل کوانتیزه شده را در حافظه بارگذاری کرده و مدل Phi-3 را مقداردهی اولیه می‌کنیم. این مرحله شامل خواندن وزن‌های مدل از فایل `gguf` و آماده‌سازی مدل برای استنتاج روی دستگاه مشخص شده (در اینجا CPU) است.

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

در این مرحله، پرامپت ورودی را توکنیزه کرده و برای استنتاج آماده می‌کنیم، یعنی آن را به دنباله‌ای از شناسه‌های توکن تبدیل می‌کنیم. همچنین `LogitsProcessor` را برای مدیریت فرآیند نمونه‌گیری (توزیع احتمالات روی واژگان) بر اساس مقادیر `temperature` و `top_p` مقداردهی اولیه می‌کنیم. هر توکن به تنسور تبدیل شده و از مدل عبور داده می‌شود تا لگیت‌ها به دست آیند.

حلقه، هر توکن در پرامپت را پردازش می‌کند، پردازشگر لگیت‌ها را به‌روزرسانی کرده و برای تولید توکن بعدی آماده می‌شود.

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

در حلقه استنتاج، توکن‌ها یکی‌یکی تولید می‌شوند تا به طول نمونه مورد نظر برسیم یا توکن پایان دنباله دریافت شود. توکن بعدی به تنسور تبدیل شده و از مدل عبور داده می‌شود، در حالی که لگیت‌ها برای اعمال جریمه‌ها و نمونه‌گیری پردازش می‌شوند. سپس توکن بعدی نمونه‌گیری، رمزگشایی و به دنباله اضافه می‌شود.
برای جلوگیری از متن تکراری، بر اساس پارامترهای `repeat_last_n` و `repeat_penalty` جریمه‌ای به توکن‌های تکراری اعمال می‌شود.

در نهایت، متن تولید شده به صورت رمزگشایی شده چاپ می‌شود تا خروجی به صورت زنده و پیوسته نمایش داده شود.

## مرحله ۷: اجرای برنامه

برای اجرای برنامه، دستور زیر را در ترمینال اجرا کنید:

```bash
cargo run --release
```

این باید یک هایکو درباره هاکی روی یخ تولید شده توسط مدل Phi-3 چاپ کند. چیزی شبیه به:

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

با دنبال کردن این مراحل، می‌توانیم تولید متن را با مدل Phi-3 با Rust و Candle در کمتر از ۱۰۰ خط کد انجام دهیم. کد بارگذاری مدل، توکنیزه کردن و استنتاج را مدیریت می‌کند و با استفاده از تنسورها و پردازش لگیت‌ها متن منسجم بر اساس پرامپت ورودی تولید می‌کند.

این برنامه کنسولی می‌تواند روی ویندوز، لینوکس و مک‌اواس اجرا شود. به دلیل قابلیت حمل Rust، کد همچنین می‌تواند به کتابخانه‌ای تبدیل شود که در داخل اپلیکیشن‌های موبایل اجرا شود (چون در آنجا نمی‌توان برنامه‌های کنسولی را اجرا کرد).

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

توجه: برای اجرای این کد روی لینوکس aarch64 یا ویندوز aarch64، فایلی به نام `.cargo/config` با محتوای زیر اضافه کنید:

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

> می‌توانید به مخزن رسمی [نمونه‌های Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) مراجعه کنید تا نمونه‌های بیشتری درباره نحوه استفاده از مدل Phi-3 با Rust و Candle، از جمله روش‌های جایگزین استنتاج، ببینید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.