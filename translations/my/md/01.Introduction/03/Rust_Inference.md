<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-09T20:06:22+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "my"
}
-->
# Rust ဖြင့် Cross-platform Inference

ဒီသင်ခန်းစာမှာတော့ Rust နဲ့ HuggingFace ရဲ့ [Candle ML framework](https://github.com/huggingface/candle) ကို အသုံးပြုပြီး inference လုပ်နည်းကို လမ်းညွှန်ပေးမှာ ဖြစ်ပါတယ်။ Rust ကို inference အတွက် အသုံးပြုခြင်းမှာ အခြား programming language တွေနဲ့ နှိုင်းယှဉ်လျှင် အားသာချက်များစွာ ရှိပါတယ်။ Rust ဟာ C နဲ့ C++ တို့လို မြန်နှုန်းမြင့်တဲ့ performance ကို ပေးနိုင်တဲ့ programming language ဖြစ်ပြီး၊ computationally intensive ဖြစ်တဲ့ inference လုပ်ငန်းများအတွက် အထူးသင့်တော်ပါတယ်။ အထူးသဖြင့် zero-cost abstraction တွေနဲ့ memory ကို ထိရောက်စွာ စီမံခန့်ခွဲပေးတာကြောင့် garbage collection overhead မရှိပါဘူး။ Rust ရဲ့ cross-platform လုပ်ဆောင်နိုင်မှုကြောင့် Windows, macOS, Linux နဲ့ မိုဘိုင်း operating system များမှာလည်း codebase အများကြီး ပြောင်းလဲစရာမလိုဘဲ အလုပ်လုပ်နိုင်ပါတယ်။

ဒီသင်ခန်းစာကို လိုက်နာဖို့အတွက် [Rust ကို 설치](https://www.rust-lang.org/tools/install) ထားဖို့ လိုအပ်ပြီး၊ Rust compiler နဲ့ Rust package manager ဖြစ်တဲ့ Cargo ပါ ပါဝင်ပါတယ်။

## အဆင့် ၁: Rust Project အသစ် တည်ဆောက်ခြင်း

Rust project အသစ် တည်ဆောက်ဖို့ terminal မှာ အောက်ပါ command ကို ရိုက်ထည့်ပါ။

```bash
cargo new phi-console-app
```

ဒါက `Cargo.toml` ဖိုင်နဲ့ `src` ဖိုလ်ဒါထဲမှာ `main.rs` ဖိုင်ပါရှိတဲ့ စတင် project ဖွဲ့စည်းမှုကို ဖန်တီးပေးပါလိမ့်မယ်။

နောက်တစ်ဆင့်မှာတော့ `Cargo.toml` ဖိုင်ထဲမှာ `candle`, `hf-hub` နဲ့ `tokenizers` crates တွေကို dependency အဖြစ် ထည့်သွင်းပါမယ်။

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

## အဆင့် ၂: အခြေခံ Parameters များ ပြင်ဆင်ခြင်း

`main.rs` ဖိုင်အတွင်းမှာ inference အတွက် အခြေခံ parameters များကို သတ်မှတ်ပါမယ်။ ရိုးရှင်းအောင် hardcoded ထားပေမယ့် လိုအပ်သလို ပြင်ဆင်နိုင်ပါတယ်။

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

- **temperature**: sampling လုပ်ရာ randomness ကို ထိန်းချုပ်ပေးသည်။
- **sample_len**: ဖန်တီးမည့် စာသားရဲ့ အမြင့်ဆုံး အရှည်ကို သတ်မှတ်သည်။
- **top_p**: nucleus sampling အတွက် တစ်ဆင့်စီမှာ စဉ်းစားမည့် token အရေအတွက်ကို ကန့်သတ်ရန် အသုံးပြုသည်။
- **repeat_last_n**: စာသားထပ်ခါထပ်ခါ ထွက်ပေါ်မှုကို တားဆီးရန် penalty ပေးမည့် token အရေအတွက်ကို ထိန်းချုပ်သည်။
- **repeat_penalty**: ထပ်ခါထပ်ခါ token များကို တားဆီးရန် penalty တန်ဖိုး။
- **seed**: random seed (ပြန်လည်ထုတ်လုပ်နိုင်မှုအတွက် constant တန်ဖိုး အသုံးပြုနိုင်သည်)။
- **prompt**: စာသားဖန်တီးမှု စတင်ရန် အစပိုင်း prompt စာသား။ ဒီမှာ ice hockey အကြောင်း haiku တစ်ပုဒ် ဖန်တီးဖို့ မော်ဒယ်ကို တောင်းဆိုထားပြီး၊ user နဲ့ assistant အပိုင်းတွေကို ဖော်ပြဖို့ special token တွေနဲ့ ဝိုင်းထားပါတယ်။ မော်ဒယ်ကတော့ ဒီ prompt ကို အပြီးသတ် haiku နဲ့ ဖြည့်စွက်ပေးပါလိမ့်မယ်။
- **device**: ဒီဥပမာမှာ CPU ကို အသုံးပြုထားပါတယ်။ Candle က GPU တွေမှာ CUDA နဲ့ Metal ကိုလည်း support လုပ်ပါတယ်။

## အဆင့် ၃: မော်ဒယ်နဲ့ Tokenizer ကို ဒေါင်းလုပ်/ပြင်ဆင်ခြင်း

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

`hf_hub` API ကို အသုံးပြုပြီး Hugging Face model hub မှ မော်ဒယ်နဲ့ tokenizer ဖိုင်တွေကို ဒေါင်းလုပ်ဆွဲပါမယ်။ `gguf` ဖိုင်မှာ quantized model weights တွေ ပါဝင်ပြီး၊ `tokenizer.json` ဖိုင်က input စာသားကို tokenize လုပ်ဖို့ အသုံးပြုပါတယ်။ ဒေါင်းလုပ်ပြီးနောက် မော်ဒယ်ကို cache ထားသဖြင့် ပထမဆုံး run မှာသာ နည်းနည်း နှေးကွေးပြီး (2.4GB မော်ဒယ်ကို ဒေါင်းလုပ်ဆွဲတာကြောင့်) နောက်ထပ် run တွေမှာ မြန်ဆန်ပါလိမ့်မယ်။

## အဆင့် ၄: မော်ဒယ်ကို Load လုပ်ခြင်း

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Quantized model weights ကို memory ထဲသို့ load လုပ်ပြီး Phi-3 မော်ဒယ်ကို initialize လုပ်ပါမယ်။ ဒီအဆင့်မှာ `gguf` ဖိုင်ထဲက model weights ကို ဖတ်ပြီး သတ်မှတ်ထားတဲ့ device (ဒီဥပမာမှာ CPU) ပေါ်မှာ inference အတွက် မော်ဒယ်ကို ပြင်ဆင်ပေးပါသည်။

## အဆင့် ၅: Prompt ကို ပြုလုပ်ပြီး Inference အတွက် ပြင်ဆင်ခြင်း

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

ဒီအဆင့်မှာ input prompt ကို tokenize လုပ်ပြီး token ID စဉ်လိုက်အဖြစ် ပြောင်းပြီး inference အတွက် ပြင်ဆင်ပါမယ်။ ထို့အပြင် `LogitsProcessor` ကို initialize လုပ်ပြီး sampling လုပ်ရာမှာ temperature နဲ့ top_p တန်ဖိုးများအရ probability distribution ကို ထိန်းချုပ်ပါမယ်။ token တစ်ခုချင်းစီကို tensor အဖြစ် ပြောင်းပြီး မော်ဒယ်ထဲသို့ ဖြတ်သွားကာ logits ကို ရယူပါသည်။

loop က prompt ထဲရှိ token တစ်ခုချင်းစီကို process လုပ်ပြီး logits processor ကို update လုပ်ကာ နောက် token ဖန်တီးရန် ပြင်ဆင်ပေးပါသည်။

## အဆင့် ၆: Inference လုပ်ခြင်း

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

Inference loop မှာ token တစ်ခုချင်းစီကို ဖန်တီးသွားပြီး sample length ရောက်သွားသည်အထိ သို့မဟုတ် end-of-sequence token တွေ့သည်အထိ ဆက်လက်လုပ်ဆောင်ပါသည်။ နောက် token ကို tensor အဖြစ် ပြောင်းပြီး မော်ဒယ်ထဲသို့ ဖြတ်သွားကာ logits ကို penalty နဲ့ sampling လုပ်ပါသည်။ ထို့နောက် နောက် token ကို sample လုပ် decode လုပ်ပြီး စာကြောင်းထဲ ထည့်သွင်းပါသည်။

စာသားထပ်ခါထပ်ခါ ထွက်ပေါ်မှုကို ကာကွယ်ရန် repeat_last_n နဲ့ repeat_penalty parameter များအရ penalty ကို ထည့်သွင်းထားပါသည်။

နောက်ဆုံး generated စာသားကို decode လုပ်ပြီး တိုက်ရိုက် output ပေးရန် print လုပ်ပါသည်။

## အဆင့် ၇: Application ကို Run ချခြင်း

Application ကို run ဖို့ terminal မှာ အောက်ပါ command ကို ရိုက်ထည့်ပါ။

```bash
cargo run --release
```

ဒါက Phi-3 မော်ဒယ်နဲ့ ဖန်တီးထားတဲ့ ice hockey အကြောင်း haiku တစ်ပုဒ်ကို print ထုတ်ပေးပါလိမ့်မယ်။ ဥပမာ -

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

သို့မဟုတ်

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## နိဂုံးချုပ်

ဒီအဆင့်တွေကို လိုက်နာခြင်းဖြင့် Phi-3 မော်ဒယ်ကို Rust နဲ့ Candle အသုံးပြုပြီး ၁၀၀ လိုင်းအောက်မှာ စာသားဖန်တီးနိုင်ပါသည်။ မော်ဒယ် load လုပ်ခြင်း၊ tokenization နဲ့ inference ကို tensor နဲ့ logits processing ကို အသုံးပြုပြီး input prompt အပေါ် မူတည်၍ စာသားကို သေချာ ဖန်တီးပေးနိုင်ပါတယ်။

ဒီ console application ကို Windows, Linux နဲ့ Mac OS ပေါ်မှာ run လို့ရပြီး Rust ရဲ့ portability ကြောင့် မိုဘိုင်း app တွေထဲမှာ အသုံးပြုနိုင်တဲ့ library အဖြစ်လည်း ပြောင်းလဲရေးသားနိုင်ပါတယ် (console app များကို မိုဘိုင်းမှာ တိုက်ရိုက် run မရပါဘူး)။

## ပူးတွဲ: အပြည့်အစုံ code

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

မှတ်ချက် - aarch64 Linux သို့မဟုတ် aarch64 Windows ပေါ်မှာ ဒီ code ကို run ဖို့ `.cargo/config` ဆိုတဲ့ ဖိုင်ကို အောက်ပါအတိုင်း ထည့်သွင်းပါ။

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

> Phi-3 မော်ဒယ်ကို Rust နဲ့ Candle အသုံးပြုပြီး inference လုပ်နည်းနဲ့ ပတ်သက်ပြီး နောက်ထပ် နမူနာများကို ကြည့်ရှုလိုပါက [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ရဲ့ အတည်ပြု repository ကို သွားရောက်ကြည့်ရှုနိုင်ပါသည်။ Alternative inference နည်းလမ်းများပါ ပါဝင်ပါတယ်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။