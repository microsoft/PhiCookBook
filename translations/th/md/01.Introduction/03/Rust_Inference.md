<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:56:48+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "th"
}
-->
# การทำ inference ข้ามแพลตฟอร์มด้วย Rust

บทเรียนนี้จะแนะนำขั้นตอนการทำ inference โดยใช้ Rust และ [Candle ML framework](https://github.com/huggingface/candle) จาก HuggingFace การใช้ Rust สำหรับ inference มีข้อดีหลายประการ โดยเฉพาะเมื่อเทียบกับภาษาโปรแกรมอื่น ๆ Rust มีชื่อเสียงเรื่องประสิทธิภาพสูงที่เทียบเท่ากับ C และ C++ ซึ่งทำให้เหมาะอย่างยิ่งสำหรับงาน inference ที่ต้องใช้การคำนวณหนัก โดยเฉพาะอย่างยิ่งเพราะมี zero-cost abstractions และการจัดการหน่วยความจำที่มีประสิทธิภาพโดยไม่มีภาระของ garbage collection ความสามารถข้ามแพลตฟอร์มของ Rust ช่วยให้สามารถพัฒนาโค้ดที่ทำงานได้บนระบบปฏิบัติการหลากหลาย เช่น Windows, macOS และ Linux รวมถึงระบบปฏิบัติการมือถือ โดยไม่ต้องแก้ไขโค้ดมากนัก

สิ่งที่ต้องเตรียมก่อนทำตามบทเรียนนี้คือการ [ติดตั้ง Rust](https://www.rust-lang.org/tools/install) ซึ่งรวมถึงตัวคอมไพเลอร์ Rust และ Cargo ตัวจัดการแพ็กเกจของ Rust

## ขั้นตอนที่ 1: สร้างโปรเจกต์ Rust ใหม่

เพื่อสร้างโปรเจกต์ Rust ใหม่ ให้รันคำสั่งต่อไปนี้ในเทอร์มินัล:

```bash
cargo new phi-console-app
```

คำสั่งนี้จะสร้างโครงสร้างโปรเจกต์เริ่มต้นพร้อมไฟล์ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ดังนี้:

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

ในไฟล์ main.rs เราจะตั้งค่าพารามิเตอร์เริ่มต้นสำหรับการทำ inference ทั้งหมดจะถูกกำหนดค่าแบบ hardcoded เพื่อความง่าย แต่เราสามารถแก้ไขได้ตามต้องการ

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
- **top_p**: ใช้สำหรับ nucleus sampling เพื่อจำกัดจำนวนโทเค็นที่พิจารณาในแต่ละขั้นตอน
- **repeat_last_n**: ควบคุมจำนวนโทเค็นที่พิจารณาเพื่อใช้ลงโทษเพื่อป้องกันการซ้ำซ้อนของลำดับ
- **repeat_penalty**: ค่าลงโทษเพื่อไม่ให้โทเค็นซ้ำกัน
- **seed**: ค่าตัวเลขสุ่ม (สามารถใช้ค่าคงที่เพื่อให้ผลลัพธ์ซ้ำได้)
- **prompt**: ข้อความเริ่มต้นสำหรับการสร้างข้อความ สังเกตว่าเราให้โมเดลสร้าง haiku เกี่ยวกับไอซ์ฮอกกี้ และห่อหุ้มด้วยโทเค็นพิเศษเพื่อแยกส่วนของผู้ใช้และผู้ช่วยสนทนา โมเดลจะเติมเต็ม prompt ด้วย haiku
- **device**: ในตัวอย่างนี้เราใช้ CPU สำหรับการคำนวณ Candle รองรับการทำงานบน GPU ด้วย CUDA และ Metal ด้วย

## ขั้นตอนที่ 3: ดาวน์โหลด/เตรียมโมเดลและ Tokenizer

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

เราใช้ไฟล์ `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` สำหรับการแบ่งคำในข้อความอินพุต เมื่อดาวน์โหลดโมเดลแล้วจะถูกเก็บไว้ในแคช ดังนั้นการรันครั้งแรกจะช้า (เนื่องจากดาวน์โหลดโมเดลขนาด 2.4GB) แต่ครั้งถัดไปจะเร็วขึ้น

## ขั้นตอนที่ 4: โหลดโมเดล

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

เราจะโหลดน้ำหนักโมเดลที่ถูก quantize เข้าไปในหน่วยความจำและเริ่มต้นโมเดล Phi-3 ขั้นตอนนี้รวมถึงการอ่านน้ำหนักโมเดลจากไฟล์ `gguf` และตั้งค่าโมเดลสำหรับทำ inference บนอุปกรณ์ที่กำหนด (ในที่นี้คือ CPU)

## ขั้นตอนที่ 5: ประมวลผล Prompt และเตรียมสำหรับ Inference

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

ในขั้นตอนนี้ เราจะแบ่งคำใน prompt และเตรียมข้อมูลสำหรับการทำ inference โดยแปลงเป็นลำดับของรหัสโทเค็น นอกจากนี้ยังเริ่มต้นค่าของ `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` แต่ละโทเค็นจะแปลงเป็น tensor และส่งผ่านโมเดลเพื่อรับ logits

ลูปนี้จะประมวลผลโทเค็นแต่ละตัวใน prompt อัปเดต logits processor และเตรียมสำหรับการสร้างโทเค็นถัดไป

## ขั้นตอนที่ 6: การทำ Inference

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

ในลูปการทำ inference เราจะสร้างโทเค็นทีละตัวจนกว่าจะถึงความยาวที่ต้องการหรือเจอโทเค็นสิ้นสุดลำดับ โทเค็นถัดไปจะแปลงเป็น tensor และส่งผ่านโมเดล ในขณะที่ logits จะถูกประมวลผลเพื่อลงโทษและทำ sampling จากนั้นโทเค็นถัดไปจะถูกสุ่ม แปลงรหัส และเพิ่มเข้าไปในลำดับ

เพื่อป้องกันข้อความซ้ำซ้อน จะมีการลงโทษโทเค็นที่ซ้ำกันตามพารามิเตอร์ `repeat_last_n` and `repeat_penalty`

สุดท้าย ข้อความที่สร้างขึ้นจะถูกพิมพ์ออกมาตามที่ถอดรหัส เพื่อให้แสดงผลแบบสตรีมมิ่งแบบเรียลไทม์

## ขั้นตอนที่ 7: รันแอปพลิเคชัน

เพื่อรันแอปพลิเคชัน ให้รันคำสั่งต่อไปนี้ในเทอร์มินัล:

```bash
cargo run --release
```

ผลลัพธ์ควรจะพิมพ์ haiku เกี่ยวกับไอซ์ฮอกกี้ที่สร้างโดยโมเดล Phi-3 ออกมา คล้ายกับ:

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

โดยการทำตามขั้นตอนเหล่านี้ เราสามารถสร้างข้อความโดยใช้โมเดล Phi-3 กับ Rust และ Candle ในโค้ดไม่เกิน 100 บรรทัด โค้ดจะจัดการเรื่องการโหลดโมเดล การแบ่งคำ และการทำ inference โดยใช้ tensor และการประมวลผล logits เพื่อสร้างข้อความที่สมเหตุสมผลตาม prompt ที่รับเข้าไป

แอปพลิเคชันคอนโซลนี้สามารถรันบน Windows, Linux และ Mac OS ได้ เนื่องจากความสามารถในการพกพาของ Rust โค้ดยังสามารถปรับใช้เป็นไลบรารีสำหรับรันในแอปมือถือได้ (เพราะเราไม่สามารถรันแอปคอนโซลในมือถือได้)

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

หมายเหตุ: หากต้องการรันโค้ดนี้บน aarch64 Linux หรือ aarch64 Windows ให้เพิ่มไฟล์ชื่อ `.cargo/config` พร้อมเนื้อหาดังนี้:

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

> คุณสามารถเยี่ยมชมที่เก็บ [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) อย่างเป็นทางการเพื่อดูตัวอย่างเพิ่มเติมเกี่ยวกับการใช้โมเดล Phi-3 กับ Rust และ Candle รวมถึงวิธีการทำ inference แบบทางเลือกอื่น ๆ ได้

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้