<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:01:18+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "he"
}
-->
# הסקה חוצת פלטפורמות עם Rust

המדריך הזה ילווה אותנו בתהליך ביצוע הסקה באמצעות Rust ו-[Candle ML framework](https://github.com/huggingface/candle) מ-HuggingFace. השימוש ב-Rust להסקה מציע מספר יתרונות, במיוחד בהשוואה לשפות תכנות אחרות. Rust ידועה בביצועים גבוהים, המקבילים לאלו של C ו-C++. זה הופך אותה לבחירה מצוינת למשימות הסקה, שיכולות להיות עתירות חישוב. במיוחד, זה נובע מהאבסטרקציות ללא עלות וניהול זיכרון יעיל, ללא עומס של איסוף זבל. היכולות חוצות הפלטפורמות של Rust מאפשרות פיתוח קוד שרץ על מערכות הפעלה שונות, כולל Windows, macOS ו-Linux, כמו גם מערכות הפעלה ניידות, ללא שינויים משמעותיים בקוד.

התנאי המוקדם למעקב אחרי מדריך זה הוא [התקנת Rust](https://www.rust-lang.org/tools/install), הכוללת את מהדר Rust ו-Cargo, מנהל החבילות של Rust.

## שלב 1: יצירת פרויקט Rust חדש

כדי ליצור פרויקט Rust חדש, הריצו את הפקודה הבאה בטרמינל:

```bash
cargo new phi-console-app
```

זוהי יוצרת מבנה פרויקט ראשוני עם קובץ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## שלב 2: הגדרת פרמטרים בסיסיים

בתוך הקובץ main.rs נגדיר את הפרמטרים הראשוניים להסקה שלנו. כולם יהיו מקודדים בקוד לצורך פשטות, אך נוכל לשנותם לפי הצורך.

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

- **temperature**: שולט ברנדומליות של תהליך הדגימה.
- **sample_len**: מגדיר את האורך המקסימלי של הטקסט שנוצר.
- **top_p**: משמש לדגימת גרעין להגבלת מספר הטוקנים הנלקחים בחשבון בכל שלב.
- **repeat_last_n**: שולט במספר הטוקנים הנלקחים בחשבון ליישום עונש למניעת רצפים חוזרים.
- **repeat_penalty**: ערך העונש להרתעת טוקנים חוזרים.
- **seed**: זרע אקראי (אפשר להשתמש בערך קבוע לשחזור טוב יותר).
- **prompt**: טקסט הפתיחה להתחלת ההפקה. שימו לב שאנחנו מבקשים מהמודל לייצר הייקו על הוקי קרח, ושאנחנו עוטפים אותו בטוקנים מיוחדים כדי לציין את חלקי המשתמש והעוזר בשיחה. המודל ישלים את ההייקו בהתאם לפתיחה.
- **device**: בדוגמה זו אנו משתמשים במעבד (CPU) לחישוב. Candle תומך גם בהרצה על GPU עם CUDA ו-Metal.

## שלב 3: הורדה/הכנת המודל והטוקנייזר

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

הקובץ `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` משמש לטוקניזציה של הטקסט הקלט שלנו. לאחר ההורדה, המודל נשמר במטמון, לכן ההרצה הראשונה תהיה איטית (כיוון שמורידים 2.4GB של המודל), אך ההרצות הבאות יהיו מהירות יותר.

## שלב 4: טעינת המודל

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

אנחנו טוענים את משקלי המודל הכמותיים לזיכרון ומאתחלים את מודל Phi-3. שלב זה כולל קריאת משקלי המודל מקובץ `gguf` והכנת המודל להסקה על המכשיר שנבחר (במקרה זה CPU).

## שלב 5: עיבוד הפתיחה והכנה להסקה

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

בשלב זה אנחנו טוקניזים את הפתיחה ומכינים אותה להסקה על ידי המרתה לרצף של מזהי טוקנים. בנוסף, מאתחלים את ערכי `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. כל טוקן מומר לטנזור ומועבר דרך המודל לקבלת הלוגיטים.

הלולאה מעבדת כל טוקן בפתיחה, מעדכנת את מעבד הלוגיטים ומכינה להפקת הטוקן הבא.

## שלב 6: הסקה

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

בלולאת ההסקה, אנחנו מייצרים טוקנים אחד אחרי השני עד שנגיע לאורך המדגם הרצוי או לטוקן סוף-רצף. הטוקן הבא מומר לטנזור ומועבר דרך המודל, תוך עיבוד הלוגיטים ליישום עונשים ודגימה. לאחר מכן הטוקן הבא מדגם, מפוענח ומתווסף לרצף.
כדי למנוע טקסט חוזר, מיושם עונש על טוקנים חוזרים בהתבסס על הפרמטרים `repeat_last_n` and `repeat_penalty`.

לבסוף, הטקסט שנוצר מודפס בזמן אמת תוך פענוח, ומאפשר פלט זורם.

## שלב 7: הרצת האפליקציה

כדי להריץ את האפליקציה, הריצו את הפקודה הבאה בטרמינל:

```bash
cargo run --release
```

זה אמור להדפיס הייקו על הוקי קרח שנוצר על ידי מודל Phi-3. משהו בסגנון:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

או

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## סיכום

בעקבות השלבים האלה, נוכל לבצע יצירת טקסט באמצעות מודל Phi-3 עם Rust ו-Candle בפחות מ-100 שורות קוד. הקוד מטפל בטעינת המודל, טוקניזציה והסקה, תוך שימוש בטנזורים ועיבוד לוגיטים ליצירת טקסט קוהרנטי על בסיס הפתיחה.

אפליקציית הקונסול הזו יכולה לרוץ על Windows, Linux ו-Mac OS. בזכות ניידות Rust, ניתן גם להתאים את הקוד לספרייה שתרוץ בתוך אפליקציות ניידות (איננו יכולים להריץ אפליקציות קונסול שם, אחרי הכל).

## נספח: הקוד המלא

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

הערה: כדי להריץ קוד זה על aarch64 Linux או aarch64 Windows, הוסיפו קובץ בשם `.cargo/config` עם התוכן הבא:

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

> ניתן לבקר במאגר הרשמי של [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) למידע נוסף על שימוש במודל Phi-3 עם Rust ו-Candle, כולל גישות חלופיות להסקה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.