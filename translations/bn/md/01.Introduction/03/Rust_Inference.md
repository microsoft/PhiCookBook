<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:48:45+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "bn"
}
-->
# রস্ট দিয়ে ক্রস-প্ল্যাটফর্ম ইনফারেন্স

এই টিউটোরিয়ালে আমরা রস্ট এবং HuggingFace এর [Candle ML ফ্রেমওয়ার্ক](https://github.com/huggingface/candle) ব্যবহার করে ইনফারেন্স করার প্রক্রিয়া শিখব। রস্ট ব্যবহার করে ইনফারেন্স করার কিছু বিশেষ সুবিধা রয়েছে, বিশেষ করে অন্যান্য প্রোগ্রামিং ভাষার তুলনায়। রস্ট তার উচ্চ পারফরম্যান্সের জন্য পরিচিত, যা C এবং C++ এর সমতুল্য। এটি ইনফারেন্স টাস্কের জন্য একটি চমৎকার পছন্দ, কারণ এগুলো সাধারণত গাণিতিকভাবে জটিল হয়। বিশেষ করে, এটি জিরো-কস্ট অ্যাবস্ট্রাকশন এবং দক্ষ মেমরি ম্যানেজমেন্টের মাধ্যমে কাজ করে, যার ফলে গার্বেজ কালেকশন ওভারহেড থাকে না। রস্টের ক্রস-প্ল্যাটফর্ম ক্ষমতা বিভিন্ন অপারেটিং সিস্টেমে যেমন Windows, macOS, Linux এবং মোবাইল অপারেটিং সিস্টেমেও কোড পরিবর্তন ছাড়াই চালানোর সুযোগ দেয়।

এই টিউটোরিয়াল অনুসরণ করার জন্য প্রয়োজন [Rust ইনস্টল করা](https://www.rust-lang.org/tools/install), যার মধ্যে রয়েছে Rust কম্পাইলার এবং Cargo, রস্ট প্যাকেজ ম্যানেজার।

## ধাপ ১: নতুন রস্ট প্রজেক্ট তৈরি করা

নতুন একটি রস্ট প্রজেক্ট তৈরি করতে টার্মিনালে নিচের কমান্ডটি চালান:

```bash
cargo new phi-console-app
```

এটি একটি প্রাথমিক প্রজেক্ট স্ট্রাকচার তৈরি করবে, যার মধ্যে `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ফাইল থাকবে:

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

## ধাপ ২: মৌলিক প্যারামিটার কনফিগার করা

main.rs ফাইলে আমরা আমাদের ইনফারেন্সের জন্য প্রাথমিক প্যারামিটারগুলো সেট করব। এগুলো সবই সরলতার জন্য হার্ডকোড করা থাকবে, তবে প্রয়োজন অনুযায়ী পরিবর্তন করা যাবে।

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
- **top_p**: নিউক্লিয়াস স্যাম্পলিংয়ে প্রতিটি ধাপে বিবেচিত টোকেনের সংখ্যা সীমাবদ্ধ করতে ব্যবহৃত হয়।
- **repeat_last_n**: পুনরাবৃত্তিমূলক সিকোয়েন্স প্রতিরোধে পেনাল্টি প্রয়োগের জন্য বিবেচিত টোকেনের সংখ্যা নিয়ন্ত্রণ করে।
- **repeat_penalty**: পুনরাবৃত্ত টোকেনের বিরুদ্ধে প্রয়োগকৃত পেনাল্টির মান।
- **seed**: র‍্যান্ডম সিড (ভালো পুনরুৎপাদনের জন্য একটি ধ্রুবক মান ব্যবহার করা যেতে পারে)।
- **prompt**: জেনারেশনের শুরুতে ব্যবহৃত প্রাথমিক প্রম্পট টেক্সট। লক্ষ্য করুন, আমরা মডেলকে আইস হকি নিয়ে একটি হাইকু তৈরি করতে বলছি, এবং আলাপচারিতার ইউজার ও অ্যাসিস্ট্যান্ট অংশ নির্দেশ করতে বিশেষ টোকেন ব্যবহার করছি। মডেল প্রম্পট সম্পূর্ণ করে একটি হাইকু তৈরি করবে।
- **device**: এই উদাহরণে আমরা CPU ব্যবহার করছি। Candle GPU তে CUDA এবং Metal সহ চলার সুবিধাও দেয়।

## ধাপ ৩: মডেল এবং টোকেনাইজার ডাউনলোড/প্রস্তুত করা

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

আমরা `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` ফাইল ব্যবহার করে ইনপুট টেক্সট টোকেনাইজ করব। একবার মডেল ডাউনলোড হয়ে ক্যাশে হয়ে গেলে প্রথম রান ধীরগতির হবে (কারণ মডেলটির আকার ২.৪ জিবি), কিন্তু পরবর্তী রানগুলো দ্রুত হবে।

## ধাপ ৪: মডেল লোড করা

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

আমরা কোয়ান্টাইজড মডেল ওয়েট মেমরিতে লোড করব এবং Phi-3 মডেল ইনিশিয়ালাইজ করব। এই ধাপে `gguf` ফাইল থেকে মডেল ওয়েট পড়া হয় এবং নির্দিষ্ট ডিভাইসে (এখানে CPU) ইনফারেন্সের জন্য মডেল প্রস্তুত করা হয়।

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

এই ধাপে আমরা ইনপুট প্রম্পট টোকেনাইজ করে টোকেন আইডির সিকোয়েন্সে রূপান্তর করব। পাশাপাশি `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` মানগুলো ইনিশিয়ালাইজ করব। প্রতিটি টোকেন টেনসর আকারে মডেলে পাঠানো হয় এবং লজিটস পাওয়া হয়।

লুপটি প্রম্পটের প্রতিটি টোকেন প্রক্রিয়া করে, লজিটস প্রসেসর আপডেট করে এবং পরবর্তী টোকেন জেনারেশনের জন্য প্রস্তুত হয়।

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

ইনফারেন্স লুপে আমরা টোকেন একে একে জেনারেট করব যতক্ষণ না নির্ধারিত sample_len পৌঁছায় অথবা end-of-sequence টোকেন পাওয়া যায়। পরবর্তী টোকেন টেনসর আকারে মডেলে পাঠানো হয়, লজিটস পেনাল্টি ও স্যাম্পলিংয়ের জন্য প্রক্রিয়াজাত করা হয়। এরপর টোকেন স্যাম্পল করে ডিকোড করা হয় এবং সিকোয়েন্সে যোগ করা হয়।

পুনরাবৃত্তি এড়াতে `repeat_last_n` and `repeat_penalty` প্যারামিটার অনুযায়ী পেনাল্টি প্রয়োগ করা হয়।

শেষে, ডিকোড হওয়া টেক্সট স্ট্রিমিং আউটপুট হিসেবে প্রিন্ট করা হয়।

## ধাপ ৭: অ্যাপ্লিকেশন চালানো

অ্যাপ্লিকেশন চালাতে টার্মিনালে নিচের কমান্ডটি রান করুন:

```bash
cargo run --release
```

এটি Phi-3 মডেল দ্বারা তৈরি আইস হকি সম্পর্কিত একটি হাইকু প্রিন্ট করবে। উদাহরণস্বরূপ:

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

এই ধাপগুলো অনুসরণ করে আমরা Phi-3 মডেল ব্যবহার করে রস্ট ও Candle এর মাধ্যমে ১০০ লাইনের কম কোডে টেক্সট জেনারেশন করতে পারি। কোডটি মডেল লোডিং, টোকেনাইজেশন এবং ইনফারেন্স পরিচালনা করে, টেনসর ও লজিটস প্রসেসিং ব্যবহার করে ইনপুট প্রম্পটের ভিত্তিতে সঙ্গতিপূর্ণ টেক্সট তৈরি করে।

এই কনসোল অ্যাপ্লিকেশন Windows, Linux এবং Mac OS-এ চলতে পারে। রস্টের পোর্টেবিলিটির কারণে, কোডটি মোবাইল অ্যাপে লাইব্রেরি হিসেবে ব্যবহার করার জন্যও অভিযোজিত করা যেতে পারে (কারণ কনসোল অ্যাপ মোবাইলে চলানো যায় না)।

## সংযোজন: সম্পূর্ণ কোড

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

নোট: aarch64 Linux বা aarch64 Windows-এ কোড চালানোর জন্য `.cargo/config` নামে একটি ফাইল তৈরি করে নিচের বিষয়বস্তু যুক্ত করুন:

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

> Phi-3 মডেল রস্ট ও Candle দিয়ে ব্যবহার করার আরও উদাহরণ এবং ইনফারেন্সের বিকল্প পদ্ধতির জন্য অফিসিয়াল [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) রিপোজিটরি দেখতে পারেন।

**দ্রষ্টব্য**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজ ভাষায় সর্বোত্তম এবং কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।