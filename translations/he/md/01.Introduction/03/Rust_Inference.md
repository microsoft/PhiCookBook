# הסקה חוצת פלטפורמות עם Rust

המדריך הזה ילווה אותנו בתהליך ביצוע הסקה באמצעות Rust ו-[Candle ML framework](https://github.com/huggingface/candle) של HuggingFace. שימוש ב-Rust להסקה מציע מספר יתרונות, במיוחד בהשוואה לשפות תכנות אחרות. Rust ידועה בביצועים הגבוהים שלה, המקבילים לאלו של C ו-C++. זה הופך אותה לבחירה מצוינת למשימות הסקה, שיכולות להיות עתירות חישוב. במיוחד, זה נובע מהאבסטרקציות ללא עלות וניהול זיכרון יעיל, ללא עומס של איסוף זבל. היכולות החוצות פלטפורמות של Rust מאפשרות פיתוח קוד שרץ על מערכות הפעלה שונות, כולל Windows, macOS ו-Linux, כמו גם מערכות הפעלה ניידות, ללא שינויים משמעותיים בקוד.

הדרישה המקדימה למעקב אחרי המדריך היא [התקנת Rust](https://www.rust-lang.org/tools/install), הכוללת את מהדר Rust ו-Cargo, מנהל החבילות של Rust.

## שלב 1: יצירת פרויקט Rust חדש

כדי ליצור פרויקט Rust חדש, הריצו את הפקודה הבאה בטרמינל:

```bash
cargo new phi-console-app
```

זה יוצר מבנה פרויקט ראשוני עם קובץ `Cargo.toml` ותיקיית `src` המכילה את הקובץ `main.rs`.

לאחר מכן, נוסיף את התלויות שלנו - כלומר את הקרייטים `candle`, `hf-hub` ו-`tokenizers` - לקובץ `Cargo.toml`:

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

בתוך הקובץ main.rs, נגדיר את הפרמטרים ההתחלתיים להסקה שלנו. כולם יהיו מקודדים ישירות לשם פשטות, אך נוכל לשנותם לפי הצורך.

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
- **top_p**: משמש לדגימת נוקלאוס להגבלת מספר הטוקנים הנלקחים בחשבון בכל שלב.
- **repeat_last_n**: שולט במספר הטוקנים הנלקחים בחשבון ליישום עונש למניעת רצפים חוזרים.
- **repeat_penalty**: ערך העונש לעידוד הימנעות מחזרות של טוקנים.
- **seed**: זרע אקראי (אפשר להשתמש בערך קבוע לשחזור טוב יותר).
- **prompt**: טקסט הפתיחה להתחלת ההפקה. שימו לב שאנו מבקשים מהמודל ליצור הייקו על הוקי קרח, ומקיפים אותו בטוקנים מיוחדים לציון חלקי המשתמש והעוזר בשיחה. המודל ישלים את הפתיחה עם הייקו.
- **device**: בדוגמה זו אנו משתמשים ב-CPU לחישוב. Candle תומך גם בהרצה על GPU עם CUDA ו-Metal.

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

אנו משתמשים ב-API של `hf_hub` להורדת קבצי המודל והטוקנייזר מ-Hugging Face model hub. קובץ ה-`gguf` מכיל את משקלי המודל הכמותיים, בעוד שקובץ `tokenizer.json` משמש לטוקניזציה של הטקסט הקלט שלנו. לאחר ההורדה, המודל נשמר במטמון, כך שההרצה הראשונה תהיה איטית (כי מורידים 2.4GB של המודל), אך הרצות הבאות יהיו מהירות יותר.

## שלב 4: טעינת המודל

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

אנו טוענים את משקלי המודל הכמותיים לזיכרון ומאתחלים את מודל Phi-3. שלב זה כולל קריאת משקלי המודל מקובץ ה-`gguf` והגדרת המודל להסקה על המכשיר שצויין (במקרה זה CPU).

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

בשלב זה, אנו טוקניזים את טקסט הפתיחה ומכינים אותו להסקה על ידי המרתו לרצף של מזהי טוקנים. בנוסף, מאתחלים את `LogitsProcessor` לטיפול בתהליך הדגימה (התפלגות ההסתברויות על אוצר המילים) בהתבסס על ערכי ה-`temperature` וה-`top_p` שניתנו. כל טוקן מומר לטנסור ומועבר דרך המודל לקבלת הלוגיטים.

הלולאה מעבדת כל טוקן בפתיחה, מעדכנת את מעבד הלוגיטים ומכינה לדור הטוקן הבא.

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

בלולאת ההסקה, אנו מייצרים טוקנים אחד אחרי השני עד שמגיעים לאורך הדגימה הרצוי או לטוקן סיום הרצף. הטוקן הבא מומר לטנסור ומועבר דרך המודל, בעוד שהלוגיטים מעובדים ליישום עונשים ודגימה. לאחר מכן הטוקן הבא מדגם, מפוענח ומתווסף לרצף.
כדי למנוע טקסט חוזר, מוחל עונש על טוקנים שחוזרים בהתבסס על הפרמטרים `repeat_last_n` ו-`repeat_penalty`.

לבסוף, הטקסט שנוצר מודפס תוך כדי פיענוח, כדי להבטיח פלט בזמן אמת בזרם.

## שלב 7: הרצת האפליקציה

להרצת האפליקציה, הריצו את הפקודה הבאה בטרמינל:

```bash
cargo run --release
```

זה אמור להדפיס הייקו על הוקי קרח שנוצר על ידי מודל Phi-3. משהו כמו:

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

בעקבות שלבים אלו, נוכל לבצע יצירת טקסט באמצעות מודל Phi-3 עם Rust ו-Candle בפחות מ-100 שורות קוד. הקוד מטפל בטעינת המודל, טוקניזציה והסקה, תוך שימוש בטנסורים ועיבוד לוגיטים ליצירת טקסט קוהרנטי בהתבסס על טקסט הפתיחה.

אפליקציית הקונסול הזו יכולה לרוץ על Windows, Linux ו-Mac OS. בזכות הניידות של Rust, הקוד יכול גם להיות מותאם לספרייה שתרוץ בתוך אפליקציות מובייל (אחרת לא נוכל להריץ אפליקציות קונסול שם).

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

> ניתן לבקר במאגר הרשמי של [דוגמאות Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) לקבלת דוגמאות נוספות לשימוש במודל Phi-3 עם Rust ו-Candle, כולל גישות חלופיות להסקה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.