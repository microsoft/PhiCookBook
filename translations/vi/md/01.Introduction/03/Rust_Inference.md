<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:02:03+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "vi"
}
-->
# Inference đa nền tảng với Rust

Hướng dẫn này sẽ dẫn bạn qua quá trình thực hiện inference sử dụng Rust và [Candle ML framework](https://github.com/huggingface/candle) từ HuggingFace. Việc sử dụng Rust cho inference mang lại nhiều lợi thế, đặc biệt khi so sánh với các ngôn ngữ lập trình khác. Rust nổi tiếng với hiệu năng cao, tương đương với C và C++. Điều này khiến nó trở thành lựa chọn tuyệt vời cho các tác vụ inference, vốn có thể rất tốn tài nguyên tính toán. Cụ thể, điều này nhờ vào các trừu tượng không tốn chi phí và quản lý bộ nhớ hiệu quả, không có overhead của garbage collection. Khả năng đa nền tảng của Rust cho phép phát triển mã chạy trên nhiều hệ điều hành khác nhau, bao gồm Windows, macOS và Linux, cũng như các hệ điều hành di động, mà không cần thay đổi đáng kể mã nguồn.

Điều kiện tiên quyết để theo dõi hướng dẫn này là [cài đặt Rust](https://www.rust-lang.org/tools/install), bao gồm trình biên dịch Rust và Cargo, trình quản lý gói của Rust.

## Bước 1: Tạo dự án Rust mới

Để tạo một dự án Rust mới, chạy lệnh sau trong terminal:

```bash
cargo new phi-console-app
```

Lệnh này tạo cấu trúc dự án ban đầu với file `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Bước 2: Cấu hình các tham số cơ bản

Trong file main.rs, chúng ta sẽ thiết lập các tham số ban đầu cho inference. Tất cả sẽ được hardcode để đơn giản, nhưng bạn có thể chỉnh sửa theo nhu cầu.

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

- **temperature**: Điều chỉnh độ ngẫu nhiên trong quá trình sampling.
- **sample_len**: Xác định độ dài tối đa của văn bản được sinh ra.
- **top_p**: Dùng cho nucleus sampling để giới hạn số lượng token được xét tại mỗi bước.
- **repeat_last_n**: Kiểm soát số lượng token được xét để áp dụng penalty tránh lặp lại.
- **repeat_penalty**: Giá trị penalty để hạn chế token bị lặp lại.
- **seed**: Hạt giống ngẫu nhiên (có thể dùng giá trị cố định để tái tạo kết quả).
- **prompt**: Văn bản đầu vào để bắt đầu quá trình sinh. Lưu ý rằng ta yêu cầu model tạo một bài haiku về khúc côn cầu trên băng, đồng thời bọc nó bằng các token đặc biệt để chỉ phần người dùng và trợ lý trong hội thoại. Model sẽ hoàn thành prompt bằng một bài haiku.
- **device**: Ở ví dụ này ta dùng CPU để tính toán. Candle cũng hỗ trợ chạy trên GPU với CUDA và Metal.

## Bước 3: Tải/Chuẩn bị Model và Tokenizer

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

Chúng ta sử dụng file `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` để token hóa văn bản đầu vào. Sau khi tải về, model sẽ được cache lại, nên lần chạy đầu tiên sẽ hơi chậm (vì phải tải model 2.4GB), nhưng các lần sau sẽ nhanh hơn nhiều.

## Bước 4: Nạp Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Chúng ta nạp trọng số model đã được lượng tử hóa vào bộ nhớ và khởi tạo model Phi-3. Bước này bao gồm việc đọc trọng số từ file `gguf` và thiết lập model để inference trên thiết bị đã chọn (ở đây là CPU).

## Bước 5: Xử lý Prompt và Chuẩn bị cho Inference

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

Ở bước này, ta token hóa prompt đầu vào và chuẩn bị cho inference bằng cách chuyển đổi nó thành chuỗi các ID token. Đồng thời khởi tạo các giá trị `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Mỗi token được chuyển thành tensor và đưa qua model để lấy logits.

Vòng lặp xử lý từng token trong prompt, cập nhật logits processor và chuẩn bị cho việc sinh token tiếp theo.

## Bước 6: Thực hiện Inference

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

Trong vòng lặp inference, ta sinh token từng cái một cho đến khi đạt độ dài mẫu mong muốn hoặc gặp token kết thúc chuỗi. Token tiếp theo được chuyển thành tensor và đưa qua model, trong khi logits được xử lý để áp dụng penalty và sampling. Sau đó token được chọn, giải mã và thêm vào chuỗi.

Để tránh văn bản bị lặp lại, ta áp dụng penalty lên các token đã xuất hiện dựa trên tham số `repeat_last_n` and `repeat_penalty`.

Cuối cùng, văn bản được sinh ra sẽ được in ra từng phần khi giải mã, đảm bảo xuất ra theo thời gian thực.

## Bước 7: Chạy ứng dụng

Để chạy ứng dụng, thực thi lệnh sau trong terminal:

```bash
cargo run --release
```

Lệnh này sẽ in ra một bài haiku về khúc côn cầu trên băng do model Phi-3 tạo ra. Ví dụ như:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

hoặc

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Kết luận

Bằng cách làm theo các bước trên, chúng ta có thể thực hiện sinh văn bản sử dụng model Phi-3 với Rust và Candle chỉ trong chưa đến 100 dòng mã. Mã nguồn xử lý việc nạp model, token hóa và inference, tận dụng tensor và xử lý logits để tạo ra văn bản mạch lạc dựa trên prompt đầu vào.

Ứng dụng console này có thể chạy trên Windows, Linux và Mac OS. Nhờ tính di động của Rust, mã cũng có thể được chuyển đổi thành thư viện chạy trong các ứng dụng di động (console app thì không chạy được trên đó).

## Phụ lục: mã nguồn đầy đủ

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

Lưu ý: để chạy mã này trên aarch64 Linux hoặc aarch64 Windows, hãy thêm file `.cargo/config` với nội dung sau:

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

> Bạn có thể truy cập kho [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) chính thức để xem thêm các ví dụ về cách sử dụng model Phi-3 với Rust và Candle, bao gồm các phương pháp khác nhau cho inference.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.