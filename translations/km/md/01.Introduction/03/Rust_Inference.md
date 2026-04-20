# ការធ្វើសន្និដ្ឋាន​ច្រើន​វេទិកា​ជាមួយ Rust

ការបណ្តុះបណ្តាលនេះនឹងណែនាំយើងឆ្លងកាត់ដំណើរការនៃការធ្វើសន្និដ្ឋានដោយប្រើ Rust និង [ស៊្វ្រេមវ័រ Candle ML](https://github.com/huggingface/candle) ពី HuggingFace។ ការប្រើ Rust សម្រាប់ការធ្វើសន្និដ្ឋានផ្តល់អត្ថប្រយោជន៍ជាច្រើន ជាពិសេសពេលប្រៀបធៀបនឹងភាសាកម្មវិធីផ្សេងទៀត។ Rust ត្រូវបានស្គាល់ថាមានប្រសិទ្ធភាពខ្ពស់ ដែលប្រៀបបាននឹង C និង C++។ នេះធ្វើឱ្យវាជាជម្រើសល្អសម្រាប់ភារកិច្ចសន្និដ្ឋាន ដែលអាចត្រូវការគណនាាខ្លាំង។ ជាពិសេស នេះមានមូលដ្ឋានពីអាប់ស្រ្តាក់សុពលាមពេលគ្មានចំណាយ (zero-cost abstractions) និងការគ្រប់គ្រងចងចាំដែលមានប្រសិទ្ធភាព ដោយគ្មានពិចារណាការប្រមូលសំរាម (garbage collection)។ សមត្ថភាពច្រើន​វេទិការបស់ Rust អាចអនុញ្ញាតឱ្យអភិវឌ្ឍកូដដែលបើកដំណើរការលើប្រព័ន្ធប្រតិបត្តិការ ផ្សេងៗ រួមទាំង Windows, macOS និង Linux, និងប្រព័ន្ធចល័ត ដោយមិនប្តូរកូដយ៉ាងសំខាន់។

កំហិតទាមទារដើម្បីតាមដានសៀវភៅណែនាំនេះគឺ [ដំឡើង Rust](https://www.rust-lang.org/tools/install) ដែលរួមមានកូំពាស៊ីលឺ Rust និង Cargo ជាម៉េនេជ័របញ្ជាកញ្ចប់របស់ Rust។

## ជំហានទី 1: បង្កើតគម្រោង Rust ថ្មី

ដើម្បីបង្កើតគម្រោង Rust ថ្មី បើក Terminal ហើយរត់ពាក្យបញ្ជាខាងក្រោម៖

```bash
cargo new phi-console-app
```

នេះនឹងបង្កើតរចនាសម្ព័ន្ធគម្រោងដំបូងដែលមានឯកសារ `Cargo.toml` និងថត `src` ដែលមានឯកសារ `main.rs` ។

បន្ទាប់មក យើងនឹងបន្ថែមការពឹងផ្អែករបស់យើង — គឺ `candle`, `hf-hub` និង `tokenizers` crates — ទៅក្នុងឯកសារ `Cargo.toml` ៖

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

## ជំហានទី 2: កំណត់ប៉ារ៉ាម៉ែត្រ មូលដ្ឋាន

នៅក្នុងឯកសារ `main.rs` យើងនឹងដាក់ប៉ារ៉ាម៉ែត្រចាប់ផ្តើមសម្រាប់ការធ្វើសន្និដ្ឋាន។ ពួកវាទាំងអស់នឹងត្រូវបានកូដរឹង (hardcoded) ដើម្បីភាពងាយស្រួល ប៉ុន្តែយើងអាចកែប្រែវាបានតាមតម្រូវការ។

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

- **temperature**: គ្រប់គ្រងភាពចៃដន្យនៃដំណើរការគំរូការរើសតួអក្សរ។
- **sample_len**: បញ្ជាក់ប្រវែងអតិបរមានៃអត្ថបទដែលបានបង្កើត។
- **top_p**: ប្រើសម្រាប់ nucleus sampling ដើម្បីដាក់ដែនកំណត់ចំនួន token ដែលគិតប្រាជ្ញាសម្រាប់每ជំហាន។
- **repeat_last_n**: គ្រប់គ្រងចំនួន token ចុងក្រោយដែលគិតសម្រាប់ប្រើដាក់ទោសដើម្បីទប់ស្កាត់លំហាត់អាក្រក់។
- **repeat_penalty**: តម្លៃទោសដើម្បីទប់ស្កាត់ token តែមួយធ្វើឱ្យកើតឡើងម្តងទៀត។
- **seed**: គ្រាប់ចាប់ចៃដਨ្យ (យើងអាចប្រើតម្លៃថេរដើម្បីធ្វើឱ្យអាចស្ទាត់ឡើងវិញបានល្អ)។
- **prompt**: អត្ថបទចាប់ផ្តើមសម្រាប់ការបង្កើត។ សូមចំណាំថាយើងស្នើឱ្យម៉ូដែលបង្កើត haikuអំពី ice hockey ហើយយើងបញ្ចូលវាចូលជាមួយ token ពិសេសដើម្បីបង្ហាញផ្នែកអ្នកប្រើ និងជំនួយការ ក្នុងកុកសេបផ្តើមនោះ។ ម៉ូដែលនឹងបញ្ចប់ prompt ដោយ haiku។
- **device**: ក្នុងឧទាហរណ៍នេះ យើងប្រើ CPU សម្រាប់គណនា។ Candle ផ្ដល់ការគាំទ្រការរត់លើ GPU ជាមួយ CUDA និង Metal ផងដែរ។

## ជំហានទី 3: ទាញយក/រៀបចំម៉ូដែល និង Tokenizer

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

យើងប្រើ API `hf_hub` ដើម្បីទាញឯកសារម៉ូដែល និង tokenizer ពី Hugging Face model hub។ ឯកសារ `gguf` មានទម្ងន់ទម្ងន់ម៉ូដែលដែលបានបំពេញ (quantized model weights) ខណៈដែលឯកសារ `tokenizer.json` ត្រូវបានប្រើសម្រាប់ tokenizing អត្ថបទបញ្ចូលរបស់យើង។ បន្ទាប់ពីទាញរួច ម៉ូដែលនឹងត្រូវបានផ្ទុកក្នុង cache ដូច្នេះការប្រតិបត្តិដំបូងនឹងយឺត (ព្រោះវាត្រូវទាញ 2.4GB នៃម៉ូដែល) ប៉ុន្តាការប្រតិបត្តិបន្ទាប់នឹងលឿនជាងមុន។

## ជំហានទី 4: ផ្ទុកម៉ូដែល

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

យើងផ្ទុកទម្ងន់ម៉ូដែលដែលបាន quantize ទៅក្នុងអង្គចងចាំ ហើយផ្តើម Phi-3 ម៉ូដែល។ ជំហាននេះរួមបញ្ចូលការអានទម្ងន់ម៉ូដែលពីឯកសារ `gguf` និងដាក់បញ្ចូលម៉ូដែលសម្រាប់សន្និដ្ឋានលើឧបករណ៍ដែលបានកំណត់ (នៅក្នុងករណីនេះគឺ CPU)។

## ជំហានទី 5: ដំណើរការ Prompt និងរៀបចំពីសម្រាប់សន្និដ្ឋាន

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

នៅជំហាននេះ យើងធ្វើ tokenization លើ prompt បញ្ចូល ហើយរៀបចំវាសម្រាប់សន្និដ្ឋានដោយបម្លែងវាទៅជាលំដាប់ ID token។ យើងក៏ចាប់ផ្តើម `LogitsProcessor` ដើម្បីដោះស្រាយដំណើរការគំរូការរើស (ចែកចាយប្រតិបត្តិលើវាក្យសម្ព័ន្ធ) ដែលផ្អែកលើតម្លៃ `temperature` និង `top_p` ដែលបានផ្តល់។ តួនាទី token នីមួយៗត្រូវបានបម្លែងទៅ tensor ហើយផ្ញើតាមម៉ូដែលដើម្បីទទួល logits។

លំហង loop នីមួយនឹងដំណើរការតួច token ក្នុង prompt, បន្ថែមបច្ចុប្បន្នភាពលើ logits processor និងរៀបចំសម្រាប់ការបង្កើត token បន្ទាប់។

## ជំហានទី 6: សន្និដ្ឋាន

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

ក្នុង loop សន្និដ្ឋាន យើងបង្កើត token មួយៗតែម្តងរហូតដល់យើងឈានដល់ប្រវែង sample ទាមទារ ឬជួប token ចប់សន្ទស្សន៍ (end-of-sequence)។ token បន្ទាប់ត្រូវបានបម្លែងទៅជា tensor ហើយផ្ញើតាមម៉ូដែល ខណៈដែល logits ត្រូវបានដំណើរការ ដើម្បីអនុវត្តទោស និងការគំរូការរើស។ បន្ទាប់មក token បន្ទាប់ត្រូវបានគំរូ (sampled), ដកស្រង់ (decoded), ហើយភ្ជាប់ទៅលំដាប់។

ដើម្បីជៀសវាងអត្ថបទធ្វើឡើងម្ដងទៀត មានការអនុវត្តទោសលើ token កើតឡើងម្តងទៀត ដោយផ្អែកលើប៉ារ៉ាម៉ែត្រ `repeat_last_n` និង `repeat_penalty`។

ចុងបញ្ចប់ អត្ថបទដែលបានបង្កើតត្រូវបានបោះពុម្ភខណៈពេលវាត្រូវបានដកស្រង់ ដើម្បីធានាការចេញបង្ហាញជាស្ទ្រីមក្នុងពេលពិត។

## ជំហានទី 7: រត់កម្មវិធី

ដើម្បីរត់កម្មវិធី សូមបញ្ជា​ពាក្យបញ្ជាខាងក្រោមក្នុងTerminal៖

```bash
cargo run --release
```

នេះគួរបោះពុម្ភ haiku អំពី ice hockey ដែលបានបង្កើតដោយ Phi-3 ម៉ូដែល។ ឧទាហរណ៍ដូចជា៖

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

or

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## សេចក្តីសន្និដ្ឋាន

ដោយអនុវត្តតាមជំហានទាំងនេះ យើងអាចធ្វើការបង្កើតអត្ថបទដោយប្រើ Phi-3 ម៉ូដែល ជាមួយ Rust និង Candle ក្នុងក្រោម 100 ចំណតនៃកូដ។ កូដនេះគ្រប់គ្រងការផ្ទុកម៉ូដែល, tokenization, និងសន្និដ្ឋាន ដោយប្រើ tensors និងការដោះស្រាយ logits ដើម្បីបង្កើតអត្ថបទដែលសមនឹងផ្អែកលើ prompt បញ្ចូល។

កម្មវិធី console នេះអាចដំណើរការលើ Windows, Linux និង Mac OS បាន។ ដោយសារតែភាពចល័តបានរបស់ Rust កូដអាចត្រូវបានប្ដូរទៅជាបណ្ណាល័យដែលអាចដំណើរការក្នុងកម្មវិធីចល័ត (mobile apps) បានផង ដើម្បីយោង—ក្នុងករណីនោះ យើងមិនអាចរត់កម្មវិធី console មាននៅក្នុងពួកវាទេ។

## បន្ថែម៖ កូដ​ពេញលេញ

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

សម្គាល់ៈ ដើម្បីដំណើរការកូដនេះលើ aarch64 Linux ឬ aarch64 Windows សូមបន្ថែមឯកសារ `.cargo/config` ដែលមានមាតិកាខាងក្រោម៖

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

> អ្នកអាចទៅចូលមើល repository ផ្លូវការនៃ [ឧទាហរណ៍ Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) សម្រាប់ឧទាហរណ៍បន្ថែមអំពីរបៀបប្រើ Phi-3 ម៉ូដែល ជាមួយ Rust និង Candle រួមទាំងវិធីជំនួសផ្សេងៗសម្រាប់ការធ្វើសន្និដ្ឋាន។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវបានបញ្ចូល។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានគេចាត់ទុកជា​ប្រភពផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ យើងសូមអនុសាសន៍ឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបករណ៍ខុសដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->