<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:27:15+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "bn"
}
-->
# রাষ্ট দিয়ে ক্রস-প্ল্যাটফর্ম ইনফারেন্স

এই টিউটোরিয়ালে আমরা রাষ্ট এবং HuggingFace এর [Candle ML framework](https://github.com/huggingface/candle) ব্যবহার করে ইনফারেন্স করার প্রক্রিয়া শিখব। রাষ্ট ব্যবহার করে ইনফারেন্স করার অনেক সুবিধা রয়েছে, বিশেষ করে অন্যান্য প্রোগ্রামিং ভাষার তুলনায়। রাষ্ট তার উচ্চ কর্মক্ষমতার জন্য পরিচিত, যা C এবং C++ এর সমতুল্য। এটি ইনফারেন্স কাজের জন্য একটি চমৎকার পছন্দ, যেগুলো সাধারণত গণনামূলকভাবে ভারী হয়। বিশেষ করে, এটি জিরো-কস্ট অ্যাবস্ট্রাকশন এবং দক্ষ মেমরি ব্যবস্থাপনার কারণে, যার ফলে কোনো গার্বেজ কালেকশন ওভারহেড থাকে না। রাষ্টের ক্রস-প্ল্যাটফর্ম ক্ষমতা বিভিন্ন অপারেটিং সিস্টেমে কোড চালানোর সুযোগ দেয়, যেমন Windows, macOS, এবং Linux, পাশাপাশি মোবাইল অপারেটিং সিস্টেমেও, কোডবেসে বড় পরিবর্তন ছাড়াই।

এই টিউটোরিয়াল অনুসরণ করার জন্য প্রয়োজন [Rust ইনস্টল করা](https://www.rust-lang.org/tools/install), যার মধ্যে রয়েছে Rust কম্পাইলার এবং Cargo, Rust প্যাকেজ ম্যানেজার।

## ধাপ ১: একটি নতুন Rust প্রজেক্ট তৈরি করুন

নতুন Rust প্রজেক্ট তৈরি করতে টার্মিনালে নিচের কমান্ডটি চালান:

```bash
cargo new phi-console-app
```

এটি একটি প্রাথমিক প্রজেক্ট স্ট্রাকচার তৈরি করবে, যার মধ্যে থাকবে `Cargo.toml` ফাইল এবং `src` ডিরেক্টরির মধ্যে `main.rs` ফাইল।

এরপর, আমরা আমাদের ডিপেন্ডেন্সিগুলো যোগ করব - যথা `candle`, `hf-hub` এবং `tokenizers` ক্রেটগুলো - `Cargo.toml` ফাইলে:

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

## ধাপ ২: মৌলিক প্যারামিটার কনফিগার করুন

`main.rs` ফাইলে আমরা ইনফারেন্সের জন্য প্রাথমিক প্যারামিটারগুলো সেট করব। সহজতার জন্য এগুলো হার্ডকোড করা থাকবে, তবে প্রয়োজনে পরিবর্তন করা যাবে।

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

- **temperature**: স্যাম্পলিং প্রক্রিয়ার র‍্যান্ডমনেস নিয়ন্ত্রণ করে।
- **sample_len**: তৈরি হওয়া টেক্সটের সর্বোচ্চ দৈর্ঘ্য নির্ধারণ করে।
- **top_p**: নিউক্লিয়াস স্যাম্পলিংয়ের জন্য ব্যবহৃত, প্রতিটি ধাপে বিবেচিত টোকেনের সংখ্যা সীমাবদ্ধ করে।
- **repeat_last_n**: পুনরাবৃত্তি রোধ করার জন্য কতগুলো টোকেন বিবেচনা করা হবে তা নিয়ন্ত্রণ করে।
- **repeat_penalty**: পুনরাবৃত্ত টোকেনের জন্য প্রয়োগকৃত পেনাল্টির মান।
- **seed**: একটি র‍্যান্ডম সিড (ভালো পুনরুত্পাদনের জন্য আমরা একটি ধ্রুবক মান ব্যবহার করতে পারি)।
- **prompt**: জেনারেশন শুরু করার জন্য প্রাথমিক প্রম্পট টেক্সট। লক্ষ্য করুন, আমরা মডেলকে আইস হকি সম্পর্কে একটি হাইকু তৈরি করতে বলেছি, এবং কথোপকথনের ইউজার ও অ্যাসিস্ট্যান্ট অংশ নির্দেশ করতে বিশেষ টোকেন দিয়ে ঘিরে রেখেছি। মডেল তারপর প্রম্পটটি হাইকু দিয়ে সম্পূর্ণ করবে।
- **device**: এই উদাহরণে আমরা CPU ব্যবহার করছি। Candle GPU তে CUDA এবং Metal সাপোর্ট করে।

## ধাপ ৩: মডেল এবং টোকেনাইজার ডাউনলোড/প্রস্তুত করুন

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

আমরা `hf_hub` API ব্যবহার করে Hugging Face মডেল হাব থেকে মডেল এবং টোকেনাইজার ফাইলগুলো ডাউনলোড করি। `gguf` ফাইলে কোয়ান্টাইজড মডেল ওয়েট থাকে, আর `tokenizer.json` ফাইলটি ইনপুট টেক্সট টোকেনাইজ করার জন্য ব্যবহৃত হয়। একবার ডাউনলোড হয়ে গেলে মডেল ক্যাশ হয়ে যায়, তাই প্রথমবার চালানো ধীর হবে (কারণ ২.৪GB মডেল ডাউনলোড হচ্ছে), কিন্তু পরবর্তী চালানো দ্রুত হবে।

## ধাপ ৪: মডেল লোড করুন

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

আমরা কোয়ান্টাইজড মডেল ওয়েট মেমরিতে লোড করি এবং Phi-3 মডেল ইনিশিয়ালাইজ করি। এই ধাপে `gguf` ফাইল থেকে মডেল ওয়েট পড়া হয় এবং নির্দিষ্ট ডিভাইসে (এই ক্ষেত্রে CPU) ইনফারেন্সের জন্য মডেল সেটআপ করা হয়।

## ধাপ ৫: প্রম্পট প্রক্রিয়াকরণ এবং ইনফারেন্সের জন্য প্রস্তুতি

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

এই ধাপে আমরা ইনপুট প্রম্পট টোকেনাইজ করি এবং টোকেন আইডির সিকোয়েন্সে রূপান্তর করে ইনফারেন্সের জন্য প্রস্তুত করি। আমরা `LogitsProcessor` ইনিশিয়ালাইজ করি, যা দেওয়া `temperature` এবং `top_p` মানের ভিত্তিতে স্যাম্পলিং প্রক্রিয়া (ভোকাবুলারির উপর সম্ভাব্যতা বন্টন) পরিচালনা করে। প্রতিটি টোকেন টেনসর এ রূপান্তরিত হয় এবং মডেলের মাধ্যমে পাঠানো হয় যাতে লগিটস পাওয়া যায়।

লুপটি প্রম্পটের প্রতিটি টোকেন প্রক্রিয়াকরণ করে, লগিটস প্রসেসর আপডেট করে এবং পরবর্তী টোকেন জেনারেশনের জন্য প্রস্তুতি নেয়।

## ধাপ ৬: ইনফারেন্স

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

ইনফারেন্স লুপে, আমরা টোকেনগুলো এক এক করে তৈরি করি যতক্ষণ না আমরা নির্ধারিত স্যাম্পল দৈর্ঘ্যে পৌঁছাই বা শেষ-অব-সিকোয়েন্স টোকেন পাই। পরবর্তী টোকেন টেনসর এ রূপান্তরিত হয় এবং মডেলের মাধ্যমে পাঠানো হয়, লগিটস প্রক্রিয়াকরণ করা হয় পেনাল্টি এবং স্যাম্পলিং প্রয়োগের জন্য। তারপর পরবর্তী টোকেন স্যাম্পল করা হয়, ডিকোড করা হয় এবং সিকোয়েন্সে যোগ করা হয়।  
পুনরাবৃত্তি এড়াতে, `repeat_last_n` এবং `repeat_penalty` প্যারামিটার অনুযায়ী পুনরাবৃত্ত টোকেনগুলোর উপর পেনাল্টি প্রয়োগ করা হয়।

অবশেষে, তৈরি হওয়া টেক্সট ডিকোড হওয়ার সাথে সাথেই প্রিন্ট করা হয়, যা স্ট্রিমিং রিয়েল-টাইম আউটপুট নিশ্চিত করে।

## ধাপ ৭: অ্যাপ্লিকেশন চালান

অ্যাপ্লিকেশন চালাতে টার্মিনালে নিচের কমান্ডটি চালান:

```bash
cargo run --release
```

এটি Phi-3 মডেল দ্বারা তৈরি আইস হকি সম্পর্কিত একটি হাইকু প্রিন্ট করবে। এরকম কিছু:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

অথবা

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## উপসংহার

এই ধাপগুলো অনুসরণ করে আমরা Phi-3 মডেল ব্যবহার করে Rust এবং Candle দিয়ে ১০০ লাইনের কম কোডে টেক্সট জেনারেশন করতে পারি। কোডটি মডেল লোডিং, টোকেনাইজেশন এবং ইনফারেন্স পরিচালনা করে, টেনসর এবং লগিটস প্রসেসিং ব্যবহার করে ইনপুট প্রম্পটের ভিত্তিতে সঙ্গতিপূর্ণ টেক্সট তৈরি করে।

এই কনসোল অ্যাপ্লিকেশন Windows, Linux এবং Mac OS এ চালানো যায়। রাষ্টের পোর্টেবিলিটির কারণে, কোডটি মোবাইল অ্যাপে রান করার জন্য একটি লাইব্রেরি হিসেবেও অভিযোজিত করা যেতে পারে (কারণ কনসোল অ্যাপস মোবাইলে চালানো যায় না)।

## পরিশিষ্ট: সম্পূর্ণ কোড

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

দ্রষ্টব্য: aarch64 Linux বা aarch64 Windows এ এই কোড চালানোর জন্য `.cargo/config` নামে একটি ফাইল যোগ করুন নিচের বিষয়বস্তু সহ:

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

> Phi-3 মডেল Rust এবং Candle দিয়ে কীভাবে ব্যবহার করবেন সে সম্পর্কে আরও উদাহরণের জন্য অফিসিয়াল [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) রিপোজিটরি দেখতে পারেন, যেখানে ইনফারেন্সের বিকল্প পদ্ধতিও রয়েছে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।