# Cross-platform inference with Rust

មេរៀននេះនឹងណែនាំយើងឲ្យធ្វើដំណើរការ inference ដោយប្រើ Rust និង [Candle ML framework](https://github.com/huggingface/candle) ពី HuggingFace។ ការប្រើ Rust សម្រាប់ inference មានអត្ថប្រយោជន៍ជាច្រើន ជាពិសេសប្រៀបធៀបនឹងភាសាកម្មវិធីផ្សេងៗ។ Rust ត្រូវបានគេស្គាល់ថាមានប្រសិទ្ធភាពខ្ពស់ ដែលស្មើនឹង C និង C++។ នេះធ្វើឲ្យវា​ជា​ជម្រើសដ៏ល្អសម្រាប់ភារកិច្ច inference ដែលទាមទារគណនា​ខ្លាំង។ ជាពិសេស វាត្រូវបានជ្រុញចេញដោយ abstractions ដែលមិនមានថ្លៃ (zero-cost abstractions) និងការគ្រប់គ្រងចងចាំខ្លាំង ដែលគ្មាន overhead នៃ garbage collection។ សមត្ថភាពឆ្លងវេទិកาของ Rust អនុញ្ញាតឲ្យអភិវឌ្ឍកូដដែលដំណើរការលើប្រព័ន្ធប្រតិបត្តិការផ្សេងៗ រួមទាំង Windows, macOS, និង Linux លើកដដែលនឹងប្រព័ន្ធប្រតិបត្តិការទូរស័ព្ទ ដោយមិនចាំបាច់ផ្លាស់ប្តូរខ្លាំងទៅលើ codebase។

ការទាមទារដើម្បីអនុវត្តមេរៀននេះគឺ [install Rust](https://www.rust-lang.org/tools/install) ដែលរួមមានកុងប៊ីឡឺរ Rust និង Cargo ដែលជាអ្នកគ្រប់គ្រងកញ្ចប់របស់ Rust។

## Step 1: Create a New Rust Project

ដើម្បីបង្កើតគម្រោង Rust ថ្មី សូមរត់ពាក្យបញ្ជាខាងក្រោមនៅក្នុង terminal:

```bash
cargo new phi-console-app
```

នេះនឹងបង្កើតរចនាសម្ព័ន្ធគម្រោងដើមមួយដែលមានឯកសារ `Cargo.toml` និងថត `src` ដែលមានឯកសារ `main.rs`។

បន្ទាប់មក យើងនឹងបន្ថែមការពឹងផ្អែក (dependencies) របស់យើង — គឺ `candle`, `hf-hub` និង `tokenizers` crates — ទៅក្នុងឯកសារ `Cargo.toml`:

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

## Step 2: Configure Basic Parameters

ខាងក្នុងឯកសារ main.rs យើងនឹងកំណត់ប៉ារ៉ាម៉ែត្រចាប់ផ្តើមសម្រាប់ inference។ ទាំងអស់នឹងត្រូវបាន hardcoded សម្រាប់ភាពថ្មោងសាមញ្ញ ប៉ុន្តាយើងអាចផ្លាស់ប្តូរពួកវាបានពេលចាំបាច់។

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

- **temperature**: គ្រប់គ្រងភាពចៃដន្យនៃកម្រៃ sampling។
- **sample_len**: បញ្ជាក់ប្រវែងអតិបរមានៃអត្ថបទដែលបានបង្កើត។
- **top_p**: ប្រើសម្រាប់ nucleus sampling ដើម្បីកំណត់ចំនួន token ដែលគិតសម្រាប់រាល់ជំហាន។
- **repeat_last_n**: គ្រប់គ្រងចំនួន token ដែលគិតសម្រាប់អនុវត្តន៍ពិន័យដើម្បីទប់ស្កាត់រលល់មួយៗដែលឡើងវិញ។
- **repeat_penalty**: តម្លៃពិន័យដើម្បីយប់យក token ដែលមកម្តងទៀត។
- **seed**: គ្រាប់អំបៅចៃដន្យ (យើងអាចប្រើតម្លៃថេរដើម្បីធ្វើឲ្យអាចស្ដារ​ឡើងវិញបានល្អขึ้น)។
- **prompt**: អត្ថបទផ្ដើមសម្រាប់ចាប់ផ្តើមការបង្កើត។ សូមចំណាំថាយើងស្នើឲ្យម៉ូដែលបង្កើត haiku អំពី ice hockey ហើយយើងបានថែមសញ្ញាពិសេសដើម្បីបង្ហាញផ្នែក user និង assistant នៃការសន្ទនា។ ម៉ូដែលនឹងបញ្ចប់ prompt នោះជាមួយ haiku។
- **device**: ក្នុងឧទាហរណ៍នេះយើងប្រើ CPU សម្រាប់កំណត់គណនា។ Candle គាំទ្រការរត់លើ GPU ជាមួយ CUDA និង Metal ផងដែរ។

## Step 3: Download/Prepare Model and Tokenizer

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

យើងប្រើ API `hf_hub` ដើម្បីទាញយកឯកសារម៉ូដែលនិង tokenizer ពី Hugging Face model hub។ ឯកសារ `gguf` មានទំងន់ទំរង់ម៉ូដែលដែលបាន quantize ខណៈដែលឯកសារ `tokenizer.json` ត្រូវបានប្រើសម្រាប់ tokenize អត្ថបទបញ្ចូលរបស់យើង។ ក្រោយពេលទាញយក ម៉ូដែលនឹងត្រូវបាន cache ដូច្នេះការប្រតិបត្ដិដំបូងនឹងយឺត (ដោយសារទាញយកម៉ូដែល 2.4GB) ប៉ុន្តាការប្រតិបត្ដិបន្ទាប់នឹងរហាន់ជាងមុន។

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

យើងផ្ទុកទម្ងន់ម៉ូដែលដែលបាន quantize ចូលទៅក្នុងចងចាំ និងចាប់ផ្តើមម៉ូដែល Phi-3។ ជំហាននេះពាក់ព័ន្ធនឹងការអានទំងន់ម៉ូដែលពីឯកសារ `gguf` និងរៀបចំម៉ូដែលសម្រាប់ inference លើ device ដែលបានកំណត់ (CPU ក្នុងករណីនេះ)។

## Step 5: Process Prompt and Prepare for Inference

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

ក្នុងជំហាននេះ យើង tokenize prompt បញ្ចូល និងរៀបចំវាសម្រាប់ inference ដោយបម្លែងវាទៅជាលំដាប់ ID token។ យើងក៏初始化 `LogitsProcessor` ដើម្បីដោះស្រាយដំណើរការ sampling (ចែកធ្វើយ概率លើវាក្យសព្ទ) ដោយផ្អែកលើតម្លៃ `temperature` និង `top_p` ដែលបានផ្ដល់។ រាល់ token ត្រូវបានបម្លែងទៅ tensor ហើយផ្ញើតាមម៉ូដែលដើម្បីទទួល logits។

លုပ္ឡប់នេះដែលដំណើរការ token ទាំងអស់នៅក្នុង prompt កំពុងអាប់ដេត logits processor និងរៀបចំសម្រាប់ការបង្កើត token បន្ទាប់។

## Step 6: Inference

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

ក្នុងល្បង inference យើងបង្កើត token មួយៗទៅមួយរហូតដល់ឈានដល់ប្រវែង sample ដែលចង់បាន ឬជួប token បញ្ចប់សំណាត់ (end-of-sequence)។ Token បន្ទាប់ត្រូវបានបម្លែងទៅ tensor ហើយផ្ញើតាមម៉ូដែល ខណៈពេលដែល logits ត្រូវបានដំណើរការ ដើម្បីអនុវត្តពិន័យ និង sampling។ បន្ទាប់មក token បន្ទាប់ត្រូវបាន sample, decode, និងបន្ថែមចូលទៅក្នុងលំដាប់។
ដើម្បីជៀសវាងអត្ថបទដែលមើលទៅជាដើមឡើងវិញ ត្រូវបានអនុវត្តពិន័យលើ token ដែលខណៈដែលឡើងវិញ ដោយផ្អែកលើ `repeat_last_n` និង `repeat_penalty`។

ចុងក្រោយ អត្ថបទដែលបានបង្កើតត្រូវបានបោះពុម្ពនៅពេលវាចេញជាភាសាដែលបាន decode ដើម្បីធានាការបង្ហាញបានជាក់ស្តែងក្នុងពេលពិត (streamed real-time output)។

## Step 7: Run the Application

ដើម្បីរត់កម្មវិធី សូមអនុវត្តពាក្យបញ្ជាខាងក្រោមនៅក្នុង terminal:

```bash
cargo run --release
```

នេះគួរតែបោះពុម្ព haiku អំពី ice hockey ដែលបានបង្កើតដោយម៉ូដែល Phi-3។ ប្រហែលជា​ដូចជា៖

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ឬ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

ដោយអនុវត្តតាមជំហានទាំងនេះ យើងអាចធ្វើការបង្កើតអត្ថបទដោយប្រើម៉ូដែល Phi-3 ជាមួយ Rust និង Candle ក្នុងខ្ទង់ក្រោម 100 ជួរដេកកូដ។ កូដទាំងអស់គ្រប់គ្រងការផ្ទុកម៉ូដែល, tokenization, និង inference ដោយប្រើ tensors និង logits processing ដើម្បីបង្កើតអត្ថបទសម្រួលល្អ ដោយផ្អែកលើ prompt បញ្ចូល។

កម្មវិធី console នេះអាចដំណើរការ​លើ Windows, Linux និង Mac OS។ ដោយសារតែការផ្ទេរបានរបស់ Rust កូដក៏អាចត្រូវបានកែសម្រួលទៅជាបណ្ណាល័យដែលអាចដំណើរការផ្នែកក្នុងកម្មវិធីទូរស័ព្ទ (毕竟យើងមិនអាចរត់កម្មវិធី console នៅទីនោះបាន)។

## Appendix: full code

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

ចំណាំ៖ ដើម្បីរត់កូដនេះលើ aarch64 Linux ឬ aarch64 Windows សូមបន្ថែមឯកសារមួយឈ្មោះ `.cargo/config` ដែលមានខ្លឹមសារ​ខាងក្រោម៖

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

> អ្នកអាចចូលទៅកាន់ repository ផ្លូវការនៃ [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) សម្រាប់ឧទាហរណ៍បន្ថែមអំពីរបៀបប្រើម៉ូដែល Phi-3 ជាមួយ Rust និង Candle រួមទាំងវិធីសាស្រ្តជំនួសសម្រាប់ inference។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**សេចក្តីបញ្ជាក់**:
ឯកសារ​នេះ​ត្រូវ​បាន​បកប្រែ​ដោយ​ប្រើសេវាសម្រួលបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបី​យើងខិតខំ​ស្ដែងភាពត្រឹមត្រូវក្តីក៏ដោយ សូមយល់ឲ្យបានថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកថាជាប្រភពផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមពិចារណាវិភាគដោយការបកប្រែដោយអ្នកបកប្រែវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយ ដែលមានឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->