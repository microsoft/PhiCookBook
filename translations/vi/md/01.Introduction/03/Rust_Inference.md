# Inference đa nền tảng với Rust

Hướng dẫn này sẽ giúp chúng ta thực hiện inference sử dụng Rust và [Candle ML framework](https://github.com/huggingface/candle) từ HuggingFace. Việc dùng Rust cho inference mang lại nhiều lợi thế, đặc biệt khi so sánh với các ngôn ngữ lập trình khác. Rust nổi tiếng với hiệu năng cao, tương đương với C và C++. Điều này làm cho Rust trở thành lựa chọn tuyệt vời cho các tác vụ inference, vốn có thể đòi hỏi tính toán nặng. Đặc biệt, điều này nhờ vào các trừu tượng không tốn chi phí và quản lý bộ nhớ hiệu quả, không có chi phí thu gom rác. Khả năng đa nền tảng của Rust cho phép phát triển mã chạy trên nhiều hệ điều hành khác nhau, bao gồm Windows, macOS và Linux, cũng như các hệ điều hành di động, mà không cần thay đổi nhiều trong mã nguồn.

Điều kiện tiên quyết để theo dõi hướng dẫn này là [cài đặt Rust](https://www.rust-lang.org/tools/install), bao gồm trình biên dịch Rust và Cargo, trình quản lý gói của Rust.

## Bước 1: Tạo dự án Rust mới

Để tạo một dự án Rust mới, chạy lệnh sau trong terminal:

```bash
cargo new phi-console-app
```

Lệnh này tạo ra cấu trúc dự án ban đầu với một file `Cargo.toml` và thư mục `src` chứa file `main.rs`.

Tiếp theo, chúng ta sẽ thêm các dependencies - cụ thể là các crate `candle`, `hf-hub` và `tokenizers` - vào file `Cargo.toml`:

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

Trong file main.rs, chúng ta sẽ thiết lập các tham số ban đầu cho quá trình inference. Tất cả sẽ được mã hóa cứng để đơn giản, nhưng có thể chỉnh sửa khi cần.

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

- **temperature**: Điều chỉnh độ ngẫu nhiên trong quá trình lấy mẫu.
- **sample_len**: Xác định độ dài tối đa của văn bản được tạo ra.
- **top_p**: Dùng cho nucleus sampling để giới hạn số token được xem xét ở mỗi bước.
- **repeat_last_n**: Kiểm soát số token được xem xét để áp dụng hình phạt nhằm tránh lặp lại chuỗi.
- **repeat_penalty**: Giá trị hình phạt để hạn chế token bị lặp lại.
- **seed**: Hạt giống ngẫu nhiên (có thể dùng giá trị cố định để tái tạo kết quả tốt hơn).
- **prompt**: Văn bản gợi ý ban đầu để bắt đầu tạo văn bản. Lưu ý rằng chúng ta yêu cầu mô hình tạo một bài haiku về khúc côn cầu trên băng, và chúng ta bao quanh nó bằng các token đặc biệt để chỉ phần người dùng và trợ lý trong cuộc hội thoại. Mô hình sẽ hoàn thành prompt bằng một bài haiku.
- **device**: Ở ví dụ này, chúng ta sử dụng CPU để tính toán. Candle cũng hỗ trợ chạy trên GPU với CUDA và Metal.

## Bước 3: Tải về/Chuẩn bị mô hình và tokenizer

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

Chúng ta sử dụng API `hf_hub` để tải các file mô hình và tokenizer từ Hugging Face model hub. File `gguf` chứa trọng số mô hình đã được lượng tử hóa, trong khi file `tokenizer.json` dùng để phân tách văn bản đầu vào thành token. Sau khi tải về, mô hình được lưu cache, nên lần chạy đầu tiên sẽ chậm (vì tải 2.4GB mô hình) nhưng các lần sau sẽ nhanh hơn.

## Bước 4: Tải mô hình

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Chúng ta tải trọng số mô hình đã lượng tử vào bộ nhớ và khởi tạo mô hình Phi-3. Bước này bao gồm việc đọc trọng số từ file `gguf` và thiết lập mô hình để inference trên thiết bị đã chỉ định (ở đây là CPU).

## Bước 5: Xử lý prompt và chuẩn bị cho inference

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

Ở bước này, chúng ta tokenize prompt đầu vào và chuẩn bị nó cho inference bằng cách chuyển đổi thành chuỗi ID token. Đồng thời khởi tạo `LogitsProcessor` để xử lý quá trình lấy mẫu (phân phối xác suất trên từ vựng) dựa trên các giá trị `temperature` và `top_p` đã cho. Mỗi token được chuyển thành tensor và đưa qua mô hình để lấy logits.

Vòng lặp xử lý từng token trong prompt, cập nhật logits processor và chuẩn bị cho việc tạo token tiếp theo.

## Bước 6: Inference

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

Trong vòng lặp inference, chúng ta tạo token từng cái một cho đến khi đạt độ dài mẫu mong muốn hoặc gặp token kết thúc chuỗi. Token tiếp theo được chuyển thành tensor và đưa qua mô hình, trong khi logits được xử lý để áp dụng hình phạt và lấy mẫu. Sau đó token tiếp theo được lấy mẫu, giải mã và thêm vào chuỗi.

Để tránh văn bản bị lặp lại, một hình phạt được áp dụng cho các token lặp dựa trên các tham số `repeat_last_n` và `repeat_penalty`.

Cuối cùng, văn bản được tạo ra được in ra ngay khi giải mã, đảm bảo đầu ra theo thời gian thực.

## Bước 7: Chạy ứng dụng

Để chạy ứng dụng, thực thi lệnh sau trong terminal:

```bash
cargo run --release
```

Lệnh này sẽ in ra một bài haiku về khúc côn cầu trên băng được tạo bởi mô hình Phi-3. Ví dụ như:

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

Bằng cách làm theo các bước trên, chúng ta có thể thực hiện tạo văn bản sử dụng mô hình Phi-3 với Rust và Candle chỉ trong chưa đầy 100 dòng mã. Mã xử lý việc tải mô hình, phân tách token và inference, tận dụng tensor và xử lý logits để tạo ra văn bản mạch lạc dựa trên prompt đầu vào.

Ứng dụng console này có thể chạy trên Windows, Linux và Mac OS. Nhờ tính di động của Rust, mã cũng có thể được điều chỉnh thành thư viện để chạy trong các ứng dụng di động (vì chúng ta không thể chạy ứng dụng console trực tiếp trên đó).

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

Lưu ý: để chạy mã này trên aarch64 Linux hoặc aarch64 Windows, thêm một file tên `.cargo/config` với nội dung sau:

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

> Bạn có thể truy cập kho [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) chính thức để xem thêm các ví dụ về cách sử dụng mô hình Phi-3 với Rust và Candle, bao gồm các phương pháp thay thế cho inference.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.