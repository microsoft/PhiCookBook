<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-03-27T08:08:34+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "ar"
}
-->
# الاستدلال عبر الأنظمة باستخدام لغة Rust

سيأخذنا هذا الدليل خطوة بخطوة عبر عملية إجراء الاستدلال باستخدام لغة Rust وإطار العمل [Candle ML](https://github.com/huggingface/candle) من HuggingFace. يوفر استخدام لغة Rust للاستدلال العديد من المزايا، خاصة عند مقارنتها بلغات البرمجة الأخرى. تُعرف Rust بأدائها العالي، الذي يُقارن بأداء C و C++. وهذا يجعلها خيارًا ممتازًا لمهام الاستدلال التي قد تكون مكثفة حسابيًا. ويرجع ذلك بشكل خاص إلى التجريدات ذات التكلفة الصفرية وإدارة الذاكرة الفعالة، التي لا تحتوي على عبء جمع القمامة. تتيح إمكانيات Rust عبر الأنظمة تطوير كود يعمل على أنظمة تشغيل مختلفة، بما في ذلك Windows وmacOS وLinux، بالإضافة إلى أنظمة التشغيل المحمولة، دون تغييرات كبيرة في الكود الأساسي.

المتطلب الأساسي لمتابعة هذا الدليل هو [تثبيت Rust](https://www.rust-lang.org/tools/install)، الذي يتضمن مترجم Rust ومدير الحزم Cargo.

## الخطوة 1: إنشاء مشروع Rust جديد

لإنشاء مشروع Rust جديد، قم بتنفيذ الأمر التالي في الطرفية:

```bash
cargo new phi-console-app
```

سيقوم هذا بإنشاء هيكل مشروع مبدئي يحتوي على الملف `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`:

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

## الخطوة 2: إعداد المعلمات الأساسية

داخل ملف main.rs، سنقوم بتعيين المعلمات الأولية للاستدلال. ستكون جميعها محددة بشكل ثابت لتبسيط الأمور، ولكن يمكننا تعديلها حسب الحاجة.

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

- **temperature**: يتحكم في عشوائية عملية التوليد.
- **sample_len**: يحدد الطول الأقصى للنص المُولد.
- **top_p**: يُستخدم لتقنية أخذ العينات النووية لتحديد عدد الرموز التي يتم أخذها بعين الاعتبار في كل خطوة.
- **repeat_last_n**: يتحكم في عدد الرموز التي يتم أخذها بعين الاعتبار لتطبيق عقوبة لتجنب التكرار.
- **repeat_penalty**: قيمة العقوبة لتثبيط الرموز المكررة.
- **seed**: قيمة عشوائية (يمكننا استخدام قيمة ثابتة لتحسين إمكانية إعادة الإنتاج).
- **prompt**: النص الابتدائي لبدء التوليد. لاحظ أننا نطلب من النموذج توليد هايكو عن رياضة الهوكي على الجليد، ونقوم بتغليفه برموز خاصة للإشارة إلى أجزاء المستخدم والمساعد في المحادثة. ثم يكمل النموذج النص بكتابة الهايكو.
- **device**: نستخدم وحدة المعالجة المركزية (CPU) للحساب في هذا المثال. يدعم Candle التشغيل على GPU باستخدام CUDA وMetal أيضًا.

## الخطوة 3: تنزيل/إعداد النموذج والمجزئ

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

نستخدم الملف `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` لتجزئة النصوص المدخلة. بمجرد تنزيل النموذج، يتم تخزينه مؤقتًا، لذلك ستكون أول عملية تنفيذ بطيئة (حيث يتم تنزيل 2.4 جيجابايت من النموذج)، ولكن العمليات اللاحقة ستكون أسرع.

## الخطوة 4: تحميل النموذج

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

نقوم بتحميل أوزان النموذج المضغوطة في الذاكرة وتهيئة نموذج Phi-3. تتضمن هذه الخطوة قراءة أوزان النموذج من ملف `gguf` وإعداد النموذج للاستدلال على الجهاز المحدد (وحدة المعالجة المركزية في هذه الحالة).

## الخطوة 5: معالجة النص الابتدائي والاستعداد للاستدلال

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

في هذه الخطوة، نقوم بتجزئة النص الابتدائي وتحضيره للاستدلال عن طريق تحويله إلى سلسلة من معرفات الرموز. كما نقوم بتهيئة قيم `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. يتم تحويل كل رمز إلى موتر وتمريره عبر النموذج للحصول على النتائج.

تقوم الحلقة بمعالجة كل رمز في النص الابتدائي، وتحديث معالج النتائج، والاستعداد لتوليد الرمز التالي.

## الخطوة 6: الاستدلال

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

في حلقة الاستدلال، نقوم بتوليد الرموز واحدًا تلو الآخر حتى نصل إلى الطول المطلوب أو نصادف رمز نهاية التسلسل. يتم تحويل الرمز التالي إلى موتر وتمريره عبر النموذج، بينما يتم معالجة النتائج لتطبيق العقوبات وأخذ العينات. بعد ذلك يتم أخذ العينة التالية، فك تشفيرها، وإضافتها إلى التسلسل.

لتجنب النصوص المتكررة، يتم تطبيق عقوبة على الرموز المكررة بناءً على المعلمات `repeat_last_n` and `repeat_penalty`.

أخيرًا، يتم طباعة النص المُولد أثناء فك تشفيره، مما يضمن إخراجًا متدفقًا في الوقت الفعلي.

## الخطوة 7: تشغيل التطبيق

لتشغيل التطبيق، قم بتنفيذ الأمر التالي في الطرفية:

```bash
cargo run --release
```

يجب أن يطبع هذا هايكو عن رياضة الهوكي على الجليد الذي تم توليده بواسطة نموذج Phi-3. شيء مثل:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

أو

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## الخاتمة

باتباع هذه الخطوات، يمكننا توليد نصوص باستخدام نموذج Phi-3 مع Rust وCandle في أقل من 100 سطر من الكود. يتعامل الكود مع تحميل النموذج، التجزئة، والاستدلال، مع الاستفادة من الموترات ومعالجة النتائج لتوليد نص مترابط بناءً على النص الابتدائي.

يمكن لهذا التطبيق العمل على أنظمة Windows وLinux وMac OS. وبفضل قابلية Rust للتنقل، يمكن أيضًا تكييف الكود إلى مكتبة تعمل داخل تطبيقات الهواتف المحمولة (لا يمكننا تشغيل تطبيقات الطرفية هناك، بعد كل شيء).

## الملحق: الكود الكامل

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

ملاحظة: لتشغيل هذا الكود على Linux أو Windows بمعمارية aarch64، أضف ملفًا باسم `.cargo/config` يحتوي على المحتوى التالي:

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

> يمكنك زيارة [أمثلة Candle الرسمية](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) للحصول على المزيد من الأمثلة حول كيفية استخدام نموذج Phi-3 مع Rust وCandle، بما في ذلك أساليب بديلة للاستدلال.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.