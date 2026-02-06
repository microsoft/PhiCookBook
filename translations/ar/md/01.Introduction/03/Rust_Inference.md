# الاستدلال عبر المنصات باستخدام Rust

سيرشدنا هذا الدليل خلال عملية إجراء الاستدلال باستخدام Rust و[إطار عمل Candle ML](https://github.com/huggingface/candle) من HuggingFace. استخدام Rust للاستدلال يقدم عدة مزايا، خاصة عند مقارنته بلغات البرمجة الأخرى. تُعرف Rust بأدائها العالي، الذي يقارن بأداء C و C++، مما يجعلها خيارًا ممتازًا لمهام الاستدلال التي قد تكون مكثفة حسابيًا. يعود ذلك بشكل خاص إلى التجريدات ذات التكلفة الصفرية وإدارة الذاكرة الفعالة، التي لا تعتمد على جمع القمامة. تتيح قدرات Rust عبر المنصات تطوير كود يعمل على أنظمة تشغيل مختلفة، بما في ذلك Windows و macOS و Linux، بالإضافة إلى أنظمة تشغيل الهواتف المحمولة، دون الحاجة إلى تغييرات كبيرة في قاعدة الكود.

الشرط الأساسي لمتابعة هذا الدليل هو [تثبيت Rust](https://www.rust-lang.org/tools/install)، والذي يشمل مترجم Rust و Cargo، مدير حزم Rust.

## الخطوة 1: إنشاء مشروع Rust جديد

لإنشاء مشروع Rust جديد، نفذ الأمر التالي في الطرفية:

```bash
cargo new phi-console-app
```

هذا ينشئ هيكل مشروع ابتدائي مع ملف `Cargo.toml` ومجلد `src` يحتوي على ملف `main.rs`.

بعد ذلك، سنضيف التبعيات الخاصة بنا - وهي الحزم `candle`، `hf-hub` و `tokenizers` - إلى ملف `Cargo.toml`:

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

داخل ملف main.rs، سنقوم بضبط المعلمات الأولية للاستدلال. ستكون جميعها مبرمجة بشكل ثابت لتبسيط الأمور، لكن يمكننا تعديلها حسب الحاجة.

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

- **temperature**: تتحكم في عشوائية عملية العينة.
- **sample_len**: تحدد الحد الأقصى لطول النص المولد.
- **top_p**: تستخدم في العينة النواة لتحديد عدد الرموز التي يتم النظر فيها في كل خطوة.
- **repeat_last_n**: تتحكم في عدد الرموز التي يتم النظر فيها لتطبيق عقوبة لمنع التكرار.
- **repeat_penalty**: قيمة العقوبة لتقليل تكرار الرموز.
- **seed**: قيمة عشوائية (يمكن استخدام قيمة ثابتة لتحسين إمكانية إعادة الإنتاج).
- **prompt**: نص البداية لبدء التوليد. لاحظ أننا نطلب من النموذج توليد هايكو عن الهوكي على الجليد، وأننا نغلفه برموز خاصة لتحديد أجزاء المستخدم والمساعد في المحادثة. بعدها سيكمل النموذج النص بالهايكو.
- **device**: نستخدم وحدة المعالجة المركزية (CPU) للحساب في هذا المثال. يدعم Candle أيضًا التشغيل على GPU باستخدام CUDA و Metal.

## الخطوة 3: تنزيل/تحضير النموذج والمجزئ

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

نستخدم واجهة برمجة التطبيقات `hf_hub` لتنزيل ملفات النموذج والمجزئ من مستودع نماذج Hugging Face. يحتوي ملف `gguf` على أوزان النموذج المكممة، بينما يستخدم ملف `tokenizer.json` لتجزئة نص الإدخال. بعد التنزيل، يتم تخزين النموذج مؤقتًا، لذا سيكون التنفيذ الأول بطيئًا (لأنه ينزل 2.4 جيجابايت من النموذج) لكن التنفيذات التالية ستكون أسرع.

## الخطوة 4: تحميل النموذج

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

نقوم بتحميل أوزان النموذج المكممة إلى الذاكرة وتهيئة نموذج Phi-3. تتضمن هذه الخطوة قراءة أوزان النموذج من ملف `gguf` وإعداد النموذج للاستدلال على الجهاز المحدد (وحدة المعالجة المركزية في هذه الحالة).

## الخطوة 5: معالجة النص التحفيزي والتحضير للاستدلال

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

في هذه الخطوة، نقوم بتجزئة النص التحفيزي وتحضيره للاستدلال عن طريق تحويله إلى تسلسل من معرفات الرموز. كما نهيئ `LogitsProcessor` للتعامل مع عملية العينة (توزيع الاحتمالات على المفردات) بناءً على قيم `temperature` و `top_p` المعطاة. يتم تحويل كل رمز إلى موتر وتمريره عبر النموذج للحصول على القيم اللوجيتية.

تقوم الحلقة بمعالجة كل رمز في النص التحفيزي، محدثة معالج اللوجيتات ومستعدة لتوليد الرمز التالي.

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

في حلقة الاستدلال، نقوم بتوليد الرموز واحدًا تلو الآخر حتى نصل إلى طول العينة المطلوب أو نواجه رمز نهاية التسلسل. يتم تحويل الرمز التالي إلى موتر ويمرر عبر النموذج، بينما تتم معالجة اللوجيتات لتطبيق العقوبات والعينة. ثم يتم اختيار الرمز التالي، فك تشفيره، وإضافته إلى التسلسل.
لتجنب النصوص المتكررة، يتم تطبيق عقوبة على الرموز المكررة بناءً على معلمات `repeat_last_n` و `repeat_penalty`.

أخيرًا، يتم طباعة النص المولد أثناء فك تشفيره، مما يضمن إخراجًا متدفقًا في الوقت الحقيقي.

## الخطوة 7: تشغيل التطبيق

لتشغيل التطبيق، نفذ الأمر التالي في الطرفية:

```bash
cargo run --release
```

ينبغي أن يطبع هذا هايكو عن الهوكي على الجليد تم توليده بواسطة نموذج Phi-3. شيء مثل:

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

باتباع هذه الخطوات، يمكننا إجراء توليد نص باستخدام نموذج Phi-3 مع Rust و Candle في أقل من 100 سطر من الكود. يتعامل الكود مع تحميل النموذج، التجزئة، والاستدلال، مستفيدًا من الموترات ومعالجة اللوجيتات لتوليد نص متماسك بناءً على النص التحفيزي.

يمكن لهذا التطبيق النصي أن يعمل على Windows و Linux و Mac OS. وبفضل قابلية النقل في Rust، يمكن تعديل الكود ليصبح مكتبة تعمل داخل تطبيقات الهواتف المحمولة (لا يمكننا تشغيل تطبيقات نصية هناك، في النهاية).

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

ملاحظة: لتشغيل هذا الكود على aarch64 Linux أو aarch64 Windows، أضف ملفًا باسم `.cargo/config` بالمحتوى التالي:

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

> يمكنك زيارة المستودع الرسمي لأمثلة [Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) لمزيد من الأمثلة حول كيفية استخدام نموذج Phi-3 مع Rust و Candle، بما في ذلك طرق بديلة للاستدلال.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.