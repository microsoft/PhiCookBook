<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-12-22T01:37:38+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ml"
}
-->
# റസ്റ്റ് ഉപയോഗിച്ചുള്ള ക്രോസ്-പ്ലാറ്റ്ഫോം ഇൻഫറൻസ്

ഈ ട്യൂട്ടോറിയൽ നമ്മുക്ക് HuggingFace-ൽ നിന്നുള്ള [Candle ML framework](https://github.com/huggingface/candle) ഉപയോഗിച്ച് Rust ഉപയോഗിച്ച് ഇൻഫറൻസ് നിർവഹിക്കാനുള്ള പ്രക്രിയ വഴി നയിക്കും. ഇൻഫറൻസിനായി Rust ഉപയോഗിക്കുന്നത് മറ്റു പ്രോഗ്രാമിംഗ് ഭാഷകളുമായി താരതമ്യപ്പെടുത്തുകയാണെങ്കിൽ പ്രത്യേകമായി നിരവധിതായുള്ള നേട്ടങ്ങൾ നൽകുന്നു. Rust C மற்றும் C++-നെക്കാൾ താരതമ്യമായ ഉയർന്ന പ്രകടനശേഷിക്ക് പേരുകേട്ട് അറിയപ്പെടുന്നു. ഇത് കണക്കുകൂട്ടൽ-ബന്ധപ്പെട്ട_INFINITY_. ഈ പ്രകടനശേഷി പ്രത്യേകിച്ച് ജീറോ-കോസ്റ്റ് അബ്സ്റ്റ്രാക്ഷനുകളും കാര്യക്ഷമമായ മെമ്മറി മാനേജ്മെന്റും (ഗാർബേജ് കലക്ഷനു പ്രശ്നമില്ലാതെ) നയിക്കുന്നു. Rust-ന്റെ ക്രോസ്-പ്ലാറ്റ്ഫോം ശേഷികൾ കോഡ് ഒരു വലിയ മാറ്റമെំពന്നില്ലാതെ Windows, macOS, Linux എന്നിവ ഉൾപ്പെടെയുള്ള വിവിധ ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങളിൽ, കൂടാതെ മൊബൈൽ ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങളിലുമാണ് പ്രവർത്തിപ്പിക്കാൻ അനുവദിക്കുന്നത്.

ഈ ട്യൂട്ടോറിയൽ പിന്തുടരാൻ മുൻ‌ആവശ്യമായത് [Rust ഇൻസ്റ്റാൾ ചെയ്യൽ](https://www.rust-lang.org/tools/install) ആണ്, ഇതിൽ Rust കമ്പൈലർ കൂടാതെ Rust പാക്കേജ് മാനേജറായ Cargo ഉൾപ്പെടുന്നുണ്ട്.

## ഘട്ടം 1: ഒരു പുതിയ Rust പ്രോജക്ട് സൃഷ്ടിക്കുക

ഒരു പുതിയ Rust പ്രോജക്ട് സൃഷ്ടിക്കാൻ ടെർമിനലിൽ താഴെയുള്ള കമാൻഡ് പ്രവർത്തിപ്പിക്കുക:

```bash
cargo new phi-console-app
```

ഇത് ഒരു പ്ര бастап് പ്രോജക്ട് ഘടന സൃഷ്ടിക്കും, അതിൽ `Cargo.toml` ഫയലും `src` ഡയരക്ടറിയും, അതിൽ `main.rs` ഫയലും ഉൾപ്പെടും.

അടുത്തതായി, ഞങ്ങൾ ഞങ്ങളുടെ ഡിപ്പണ്ടൻസികൾ — അതായത് `candle`, `hf-hub` എന്നിവയും `tokenizers` ക്രേറ്റും — `Cargo.toml` ഫയലിൽ ചേർക്കും:

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

## ഘട്ടം 2: അടിസ്ഥാന പാരാമീറ്ററുകൾ ക്രമീകരിക്കുക

`main.rs` ഫയലിനുള്ളിൽ, ഇൻഫറൻസിനുള്ള ആരംഭ പാരാമീറ്ററുകൾ നാം സജ്ജമാക്കും. സൌകര്യത്തിനായി ഇവ എല്ലാം ഹാർഡ്‌കോഡുചെയ്തിരിക്കും, പക്ഷേ ആവശ്യമെങ്കിൽ നാം അവ മാറ്റിക്കൊള്ളാം.

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

- **temperature**: സാമ്പിളിംഗ് പ്രക്രിയയുടെ യാദൃച്ഛികതയെ നിയന്ത്രിക്കുന്നു.
- **sample_len**: ഉൽപാദിപ്പിച്ച ടെക്സ്റ്റിന്റെ പരമാവധി നീളം നിർവ്വചിക്കുന്നു.
- **top_p**: ന്യുക്ലിയസ് സാമ്പിളിംഗിന് ഉപയോഗിച്ച് ഓരോ ഘട്ടത്തിലും പരിഗണിക്കാവുന്ന ടോക്കണുകളുടെ എണ്ണം പരിധി വരുത്താൻ ഉപയോഗിക്കുന്നു.
- **repeat_last_n**: ആവർത്തന സീരിയകൾ ഒഴിവാക്കാൻ പിഴവ് പ്രയോഗിക്കാൻ പരിഗണിക്കുന്ന അവസാന N ടോക്കണുകളുടെ എണ്ണം നിയന്ത്രിക്കുന്നു.
- **repeat_penalty**: ആവർത്തിച്ച ടോക്കൺകളെ നിരസിക്കാൻ ഉപയോഗിക്കുന്ന പിഴവിന്റെ മൂല്യം.
- **seed**: ഒരു റാൻഡം സീഡ് (മികച്ച ആവർത്തനശേഷിക്ക് നിശ്ചിത മൂല്യം ഉപയോഗിക്കാവുന്നതാണ്).
- **prompt**: ജനറേഷൻ ആരംഭിക്കാൻ ഉപയോഗിച്ച ആദ്യിക പ്രോപം ടെക്സ്റ്റ്. ഇവിടെ ഞങ്ങൾ മോഡലിനോട് ഐസ് ഹോക്കി туралы haiku ഒരു കവിത സൃഷ്ടിക്കാൻ പറഞ്ഞിരിക്കുന്നു, കൂടാതെ സംവാദത്തിലെ ഉപയോക്താവിനെയും അസിസ്റ്റന്റിനെയും സൂചിപ്പിക്കാൻ പ്രത്യേക ടോക്കണുകൾ ഉപയോഗിച്ച് അത് ചുറ്റിപ്പറ്റിയിട്ടുണ്ട്. മോഡൽ പിന്നീട് ആ പ്രോംപ്റ്റ് haiku-വോടെ പൂർത്തിയാക്കും.
- **device**: ഈ ഉദാഹരണത്തിൽ കണക്കുകൾക്കായി CPU ഉപയോഗിക്കുന്നു. Candle GPU-യിൽ CUDA மற்றும் Metal ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കലും പിന്തുണയ്ക്കുന്നു.

## ഘട്ടം 3: മോഡൽയും ടോക്കനൈസറും ഡൗൺലോഡ്/തയ്യാറില്ലാക്കുക

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

നാം Hugging Face മോഡൽ ഹബിൽ നിന്ന് മോഡലിന്റെയും ടോക്കനൈസറിന്റെയും ഫയലുകളും ഡൗൺലോഡ് ചെയ്യാനായി `hf_hub` API ഉപയോഗിക്കുന്നു. `gguf` ഫയൽ ക്വാണ്ടൈസ്ഡ് മോഡൽ വെയ്റ്റുകൾ ഉൾക്കൊള്ളുന്നു, בעוד `tokenizer.json` ഫയൽ ഞങ്ങളുടെ ഇൻപുട്ട് ടെക്സ്റ്റ് ടോക്കനൈസ് ചെയ്യാൻ ഉപയോഗിക്കുന്നു. ഒരു തവണ ഡൗൺലോഡ് ചെയ്താൽ മോഡൽ കാഷേ ചെയ്യപ്പെടും, അതുകൊണ്ട് ആദ്യ 실행ം മോഡൽയുടെ 2.4GB ഡൗൺലോഡ് ചെയ്യുന്നതുകൊണ്ട് മന്ദമാകും, പക്ഷേ തുടർന്ന് 실행ങ്ങൾ വേഗത്തിലും നടക്കും.

## ഘട്ടം 4: മോഡൽ ലോഡ് ചെയ്യുക

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

നാം ക്വാണ്ടൈസ്ഡ് മോഡൽ വെയ്റ്റുകൾ മെമ്മറിയിൽ ലോഡ് ചെയ്ത് Phi-3 മോഡൽініഷ്യലൈസ് ചെയ്യുന്നു. ഈ ഘട്ടം `gguf` ഫയലിൽ നിന്ന് മോഡൽ വെയ്റ്റുകൾ വായിക്കുകയും നിർദ്ദിഷ്ട ഡിവൈസിൽ (ഈ ഉദാഹരണത്തിൽ CPU) ഇൻഫറൻസിന് മോഡൽ സജ്ജീകരിക്കുകയും ചെയ്യുന്നതിൽ ഉൾപ്പെടുന്നു.

## ഘട്ടം 5: പ്രോംപ്റ്റ് പ്രോസസ് ചെയ്ത് ഇൻഫറൻസിനുള്ള ഒരുക്കം

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

ഈ ഘട്ടത്തിൽ, നാം ഇൻപുട്ട് പ്രോംപ്റ്റ് ടോക്കനൈസ് ചെയ്ത് അത് ടോക്കൺ ID-കളുടെ കായിക്രമമാക്കി ഇൻഫറൻസിനുള്ള തയ്യാറെടുപ്പിൽ മാറ്റുന്നു. നാം നൽകിയ `temperature` మరియు `top_p` മൂല്യങ്ങളെങ്കിലെ അടിസ്ഥാനത്തിൽ സാമ്പിളിംഗ് പ്രക്രിയ കൈകാര്യം ചെയ്യാൻ `LogitsProcessor` ആമുഖീകരിക്കുന്നു. ഓരോ ടോക്കൺയും ഒരു ടെൻസറാക്കി മാറ്റി മോഡലിലേക്കു പാസ്സ് ചെയ്ത് ലോജിറ്റുകൾ നേടുന്നു.

ലൂപ് പ്രോംപ്റ്റിലുള്ള ഓരോ ടോക്കണെയും പ്രോസസ്സ് ചെയ്ത് ലോജിറ്റ്സ് പ്രോസസറിനെ അപ്‌ഡേറ്റ് ചെയ്യുകയും അടുത്ത ടോക്കൺ ജനറേഷനു തയ്യാറാക്കുകയും ചെയ്യുന്നു.

## ഘട്ടം 6: ഇൻഫറൻസ്

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

ഇൻഫറൻസ് ലൂപ്പിൽ, നാം ആവശ്യമായ sample_len എത്തുന്നതുവരെ അല്ലെങ്കിൽ end-of-sequence ടോക്കൺ കാണുന്നത് വരെ ടോക്കണുകൾ ഒന്ന് ഒന്ന് ജനറേറ്റ് ചെയ്യുന്നു. അടുത്ത ടോക്കൺ ഒരു ടെൻസറാക്കി മാറ്റി മോഡലിലേക്കു പാസ്സ് ചെയ്യപ്പെടുന്നു, അതേസമയം ലോജിറ്റുകൾ പിഴവുകൾയും സാമ്പിലിംഗും പ്രയോഗിക്കാൻ പ്രോസസ് ചെയ്യപ്പെടുന്നു. തുടർന്ന് അടുത്ത ടോക്കൺ സാമ്പിൾ ചെയ്ത് ഡീകോഡ് ചെയ്ത് ശ്രേണിയിൽ ചേർക്കപ്പെടുന്നു.
ആവർത്തനപരമായ ടെക്സ്റ്റ് ഒഴിവാക്കുന്നതിനായി `repeat_last_n` અને `repeat_penalty` പാരാമീറ്ററുകളുടെ അടിസ്ഥാനത്തിൽ ആവർത്തിച്ച ടോക്കണുകൾക്ക് പിഴവ് പ്രയോഗിക്കുന്നു.

അവസാനമായി, ജനറേറ്റ് ചെയ്ത ടെക്സ്റ്റ് ഡീകോഡ് ചെയ്യുന്ന പോലെ തന്നെ പ്രിന്റ് ചെയ്യപ്പെടുന്നു, ഈ രീതിയിൽ സ്ട്രീമിങായി റിയൽ-ടൈം ഔട്ട്പുട്ട് ഉറപ്പാക്കുന്നു.

## ഘട്ടം 7: ആപ്ലിക്കേഷൻ ഓടിക്കുക

ആപ്ലിക്കേഷൻ ഓടിക്കാൻ, ടെർമിനലിൽ താഴെയുള്ള കമാൻഡ് പ്രവർത്തിപ്പിക്കുക:

```bash
cargo run --release
```

ഇത് Phi-3 മോഡൽ ഉപയോഗിച്ച് ഐസ് ഹോക്കിയെക്കുറിച്ചുള്ള haiku ഒരു കവിത പ്രിന്റ് ചെയ്യണം. ഏതെങ്കിലും ഇത്തരമൊരു ഔട്ട്‌പുട്ടായി പ്രതീക്ഷിക്കാമെന്നുള്ളത്:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

അഥവാ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## നിഗമനം

ഈ ഘട്ടങ്ങൾ പിന്തുടർന്ന്, നാം Rustയും Candle ഉം ഉപയോഗിച്ച് Phi-3 മോഡലിലൂടെ 100 ലൈനുകൾക്കുള്ളിൽ ടെക്സ്റ്റ് ജനറേഷൻ നിർവഹിക്കാം. കോഡ് മോഡൽ ലോഡിംഗ്, ടോക്കനൈസേഷൻ, ഇൻഫറൻസ് എന്നിവ കൈകാര്യം ചെയ്യുന്നു, ഇൻപുട്ട് പ്രോംപ്റ്റിന്റെ അടിസ്ഥാനത്തിൽ സുസ്ഥിരമായ ടെക്സ്റ്റ് ജനറേറ്റ് ചെയ്യാൻ ടെൻസറുകളും ലോജിറ്റ്സ് പ്രോസസ്സിംഗും ഉപയോഗിക്കുന്നു.

ഈ കൺസോൾ ആപ്ലിക്കേഷൻ Windows, Linux, Mac OS എന്നിവയിൽ പ്രവർത്തിക്കാൻ കഴിയും. Rust-ന്റെ പോർട്ടബിലിറ്റിയുടെ കാരണം, കോഡ് മൊബൈൽ ആപ്പുകളിൽ നടപ്പിലാകുന്ന ലൈബ്രറിയായി മാറ്റുകയും ചെയ്യാം (അവിടെ കണ്ടസോൾ ആപ്ലിക്കേഷനുകൾ ഓടിക്കാനാകില്ല, അതുകൊണ്ട്).

## അനുബന്ധം: പൂർണ്ണ കോഡ്

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

ശ്രദ്ധിക്കുക: aarch64 Linux അല്ലെങ്കിൽ aarch64 Windows-ൽ ഈ കോഡ് ഓടിക്കാൻ, `.cargo/config` എന്നു പേരുള്ള ഒരു ഫയൽ ചേർത്തുകൊണ്ട് താഴെ കാണുന്ന ഉള്ളടക്കം ഉൾപ്പെടുത്തുക:

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

> You can visit the official [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository for more examples on how to use the Phi-3 model with Rust and Candle, including alternative approaches to inference.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തനസേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യത മുൻനിരയിൽ വയ്ക്കുന്നുവെങ്കിലും, യന്ത്ര വിവർത്തനങ്ങളിൽ പിഴവുകളും അകിക്ഷതകളും ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. യഥാർത്ഥ പ്രമാണം അതിന്റെ നാട്ടഭാഷയിലുള്ള പതിപ്പായാണ് അധികാരപരമായി മാനിക്കേണ്ടത്. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തെത്തുടർന്ന് ഉണ്ടാക്കിയേക്കാവുന്ന എന്തെങ്കിലും തെറ്റിദ്ധാരണങ്ങളിലും തെറ്റായ വ്യാഖ്യാനങ്ങളിലും ഞങ്ങൾ ബാധ്യസ്ഥരല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->