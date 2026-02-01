# การทำ inference ข้ามแพลตฟอร์มด้วย Rust

บทเรียนนี้จะแนะนำขั้นตอนการทำ inference โดยใช้ Rust และ [Candle ML framework](https://github.com/huggingface/candle) จาก HuggingFace การใช้ Rust สำหรับการทำ inference มีข้อดีหลายประการ โดยเฉพาะเมื่อเทียบกับภาษาโปรแกรมอื่นๆ Rust มีชื่อเสียงในเรื่องประสิทธิภาพสูงที่เทียบเท่ากับ C และ C++ ซึ่งทำให้เหมาะอย่างยิ่งสำหรับงาน inference ที่ต้องใช้การคำนวณหนัก โดยเฉพาะอย่างยิ่งเนื่องจากมี zero-cost abstractions และการจัดการหน่วยความจำที่มีประสิทธิภาพโดยไม่มี overhead จาก garbage collection ความสามารถข้ามแพลตฟอร์มของ Rust ช่วยให้พัฒนาโค้ดที่รันได้บนระบบปฏิบัติการต่างๆ เช่น Windows, macOS และ Linux รวมถึงระบบปฏิบัติการบนมือถือ โดยไม่ต้องแก้ไขโค้ดมากนัก

สิ่งที่ต้องเตรียมก่อนเริ่มบทเรียนนี้คือการ [ติดตั้ง Rust](https://www.rust-lang.org/tools/install) ซึ่งรวมถึง Rust compiler และ Cargo ตัวจัดการแพ็กเกจของ Rust

## ขั้นตอนที่ 1: สร้างโปรเจกต์ Rust ใหม่

เพื่อสร้างโปรเจกต์ Rust ใหม่ ให้รันคำสั่งต่อไปนี้ในเทอร์มินัล:

```bash
cargo new phi-console-app
```

คำสั่งนี้จะสร้างโครงสร้างโปรเจกต์เริ่มต้นพร้อมไฟล์ `Cargo.toml` และโฟลเดอร์ `src` ที่มีไฟล์ `main.rs`

ต่อไปเราจะเพิ่ม dependencies ของเรา ได้แก่ crate `candle`, `hf-hub` และ `tokenizers` ลงในไฟล์ `Cargo.toml`:

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

## ขั้นตอนที่ 2: กำหนดพารามิเตอร์พื้นฐาน

ในไฟล์ main.rs เราจะตั้งค่าพารามิเตอร์เริ่มต้นสำหรับการทำ inference โดยจะตั้งค่าแบบ hardcoded เพื่อความง่าย แต่สามารถแก้ไขได้ตามต้องการ

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

- **temperature**: ควบคุมความสุ่มของกระบวนการ sampling
- **sample_len**: กำหนดความยาวสูงสุดของข้อความที่สร้างขึ้น
- **top_p**: ใช้สำหรับ nucleus sampling เพื่อจำกัดจำนวน token ที่พิจารณาในแต่ละขั้นตอน
- **repeat_last_n**: ควบคุมจำนวน token ที่พิจารณาเพื่อใช้ลงโทษไม่ให้เกิดลำดับซ้ำ
- **repeat_penalty**: ค่าลงโทษเพื่อป้องกัน token ซ้ำ
- **seed**: ค่า seed แบบสุ่ม (สามารถใช้ค่าคงที่เพื่อให้ผลลัพธ์ซ้ำได้)
- **prompt**: ข้อความเริ่มต้นสำหรับการสร้างข้อความ สังเกตว่าเราให้โมเดลสร้าง haiku เกี่ยวกับ ice hockey และห่อหุ้มด้วย token พิเศษเพื่อบ่งบอกส่วนของผู้ใช้และผู้ช่วย โมเดลจะเติมข้อความต่อด้วย haiku
- **device**: ในตัวอย่างนี้เราใช้ CPU สำหรับการคำนวณ Candle รองรับการรันบน GPU ด้วย CUDA และ Metal ด้วยเช่นกัน

## ขั้นตอนที่ 3: ดาวน์โหลด/เตรียมโมเดลและ tokenizer

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

เราใช้ API `hf_hub` เพื่อดาวน์โหลดไฟล์โมเดลและ tokenizer จาก Hugging Face model hub ไฟล์ `gguf` จะเก็บน้ำหนักโมเดลที่ถูก quantize ส่วนไฟล์ `tokenizer.json` ใช้สำหรับการแปลงข้อความเข้าเป็น token เมื่อดาวน์โหลดแล้ว โมเดลจะถูกเก็บไว้ในแคช ดังนั้นการรันครั้งแรกจะช้า (เนื่องจากดาวน์โหลดโมเดลขนาด 2.4GB) แต่ครั้งถัดไปจะเร็วขึ้น

## ขั้นตอนที่ 4: โหลดโมเดล

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

เราจะโหลดน้ำหนักโมเดลที่ถูก quantize เข้าสู่หน่วยความจำและเริ่มต้นโมเดล Phi-3 ขั้นตอนนี้รวมถึงการอ่านน้ำหนักโมเดลจากไฟล์ `gguf` และตั้งค่าโมเดลสำหรับการทำ inference บนอุปกรณ์ที่ระบุ (ในที่นี้คือ CPU)

## ขั้นตอนที่ 5: ประมวลผล prompt และเตรียมสำหรับ inference

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

ในขั้นตอนนี้ เราจะทำการ tokenize ข้อความ prompt และเตรียมข้อมูลสำหรับการทำ inference โดยแปลงเป็นลำดับของ token IDs นอกจากนี้ยังเริ่มต้น `LogitsProcessor` เพื่อจัดการกระบวนการ sampling (การแจกแจงความน่าจะเป็นใน vocabulary) ตามค่า `temperature` และ `top_p` ที่กำหนด แต่ละ token จะถูกแปลงเป็น tensor และส่งผ่านโมเดลเพื่อรับ logits

ลูปนี้จะประมวลผลแต่ละ token ใน prompt โดยอัปเดต logits processor และเตรียมสำหรับการสร้าง token ถัดไป

## ขั้นตอนที่ 6: การทำ inference

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

ในลูปการทำ inference เราจะสร้าง token ทีละตัวจนกว่าจะถึงความยาวที่ต้องการหรือเจอ token สิ้นสุดลำดับ token ถัดไปจะถูกแปลงเป็น tensor และส่งผ่านโมเดล ขณะที่ logits จะถูกประมวลผลเพื่อลงโทษและ sampling จากนั้น token ถัดไปจะถูกสุ่ม เลขถอดรหัส และต่อเข้ากับลำดับข้อความ

เพื่อป้องกันข้อความซ้ำ จะมีการลงโทษ token ที่ซ้ำกันตามพารามิเตอร์ `repeat_last_n` และ `repeat_penalty`

สุดท้าย ข้อความที่สร้างขึ้นจะถูกพิมพ์ออกมาแบบเรียลไทม์ขณะถอดรหัส

## ขั้นตอนที่ 7: รันแอปพลิเคชัน

เพื่อรันแอปพลิเคชัน ให้รันคำสั่งต่อไปนี้ในเทอร์มินัล:

```bash
cargo run --release
```

ผลลัพธ์ควรเป็น haiku เกี่ยวกับ ice hockey ที่สร้างโดยโมเดล Phi-3 ประมาณว่า:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

หรือ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## สรุป

โดยทำตามขั้นตอนเหล่านี้ เราสามารถสร้างข้อความโดยใช้โมเดล Phi-3 ด้วย Rust และ Candle ในโค้ดไม่เกิน 100 บรรทัด โค้ดนี้จัดการการโหลดโมเดล การ tokenize และการทำ inference โดยใช้ tensor และการประมวลผล logits เพื่อสร้างข้อความที่สอดคล้องกับ prompt ที่ป้อนเข้าไป

แอปพลิเคชันคอนโซลนี้สามารถรันได้บน Windows, Linux และ Mac OS เนื่องจากความพกพาของ Rust โค้ดยังสามารถปรับใช้เป็นไลบรารีสำหรับรันในแอปมือถือได้ (เพราะเราไม่สามารถรันแอปคอนโซลบนมือถือได้)

## ภาคผนวก: โค้ดเต็ม

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

หมายเหตุ: หากต้องการรันโค้ดนี้บน aarch64 Linux หรือ aarch64 Windows ให้เพิ่มไฟล์ชื่อ `.cargo/config` โดยมีเนื้อหาดังนี้:

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

> คุณสามารถเยี่ยมชมที่เก็บตัวอย่าง [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) อย่างเป็นทางการเพื่อดูตัวอย่างเพิ่มเติมเกี่ยวกับการใช้โมเดล Phi-3 กับ Rust และ Candle รวมถึงวิธีการทำ inference แบบอื่นๆ ได้เช่นกัน

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้