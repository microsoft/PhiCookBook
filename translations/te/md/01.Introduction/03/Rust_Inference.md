<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-12-22T01:35:06+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "te"
}
-->
# రస్ట్‌తో సంకీర్తి-ప్లాట్‌ఫార్మ్ ఇన్ఫరెన్స్

ఈ ట్యూటోరియల్ రస్ట్ మరియు HuggingFace నుండి [Candle ML ఫ్రేమ్‌వర్క్](https://github.com/huggingface/candle) ఉపయోగించి ఇన్ఫరెన్స్ నిర్వహించే ప్రక్రియలో మమ్మల్ని దారి నడిపిస్తుంది. ఇన్ఫరెన్స్ కోసం రస్ట్ ఉపయోగించడం చాలా ప్రయోజనాలను అందిస్తుంది, ప్రత్యేకంగా ఇతర ప్రోగ్రామింగ్ భాషలతో సమానించగా. రస్ట్ C మరియు C++ లాంటి అధిక పనితీరుకు ప్రసిద్ధి చెందింది. ఇది గణనాత్మకంగా తీవ్రమైన ఇన్ఫరెన్స్ పనులకు అనుకూలమైన ఎంపికగా మారుతుంది. ముఖ్యంగా, ఇది జీరో-కాస్ట్ అభిజ్ఞలు మరియు సమర్థవంతమైన మెమరీ మేనేజ్‌మెంట్ ద్వారా నడుస్తుంది, దీానికి గార్బేజ్ కలెక్షన్ ఓవర్‌హెడ్ లేదు. రస్ట్ యొక్క క్రాస్-ప్లాట్‌ఫార్మ్ సామర్థ్యాలు Windows, macOS మరియు Linux సహా వివిధ ఆపరేటింగ్ సిస్టమ్‌లపై, అలాగే మొబైల్ ఆపరేటింగ్ సిస్టమ్‌లపై కూడా పెద్ద మార్పులు లేకుండానే కోడ్ నడపడానికి వీలు కల్పిస్తాయి.

ఈ ట్యూటోరియల్‌ను అనుసరించడానికి ముందస్తుగా [Rust ని ఇన్‌స్టాల్ చేయండి](https://www.rust-lang.org/tools/install) — ఇది రస్ట్ కంపైలర్ మరియు ప్యాకేజ్ మేనేజర్ Cargo ని కలిగి ఉంటుంది.

## Step 1: Create a New Rust Project

కొత్త రస్ట్ ప్రాజెక్ట్‌ను సృష్టించడానికి, టెర్మినల్‌లో క్రింది కమాండ్‌ను నడపండి:

```bash
cargo new phi-console-app
```

ఇది ఒక ప్రారంభ ప్రాజెక్ట్ నిర్మాణాన్ని ఉత్పత్తి చేస్తుంది, అందులో `Cargo.toml` ఫైల్ మరియు `src` డైరెక్టరీలో `main.rs` ఫైల్ ఉంటుంది.

తరువాత, మన డిపెండెన్సీలు — ప్రత్యేకంగా `candle`, `hf-hub` మరియు `tokenizers` క్రేట్స్ — ను `Cargo.toml` ఫైల్‌కు జోడిస్తాం:

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

`main.rs` ఫైల్ లో మన ఇన్ఫరెన్స్‌కు సారాంశ పారామీటర్లను సెటప్ చేస్తాము. సరళత్వానికి అవన్నీ హార్డ్‌కోడ్ చేయబడతాయి, కానీ అవసరమైతే మనం వాటిని మార్చుకోవచ్చు.

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

- **temperature**: సాంప్లింగ్ ప్రక్రియ యొక్క యాదృచ్ఛికతను నియంత్రిస్తుంది.
- **sample_len**: ఉత్పత్తి అయ్యే టెక్స్ట్ యొక్క గరిష్ట పొడవుని నిర్దేశిస్తుంది.
- **top_p**: ప్రతి దశలో పరిగణనలోకి తీసుకునే టోకెన్ల సంఖ్యను పరిమితం చేయడానికి nucleus sampling కోసం ఉపయోగించబడుతుంది.
- **repeat_last_n**: పునరావృత శృంఖలలను నిరోధించడానికి జరిపే పెనాల్టీకి పరిగణనలోకి తీసుకునే టోకెన్ల సంఖ్యను నియంత్రిస్తుంది.
- **repeat_penalty**: పునరావృత టోకెన్లను నిరుత్సాహపరచడానికి ఇచ్చే పెనాల్టీ విలువు.
- **seed**: రాండమ్ సీడ్ (మరింత పునఃఉత్పత్తిరహితత్వానికి కాంట్స్టెంట్ విలువ ఉపయోగించవచ్చు).
- **prompt**: జనరేషన్ ప్రారంభించడానికి ప్రారంభ ప్రాంప్ట్ టెక్స్ట్. మేము మోడల్‌ను ఐస్ హాకీ గురించి ఒక హైకూ (haiku) తయారుచేయమని అడుగుతామంటూ గమనించండి, మరియు సంభాషణలో యూజర్ మరియు అసిస్టెంట్ భాగాలను సూచించడానికి ప్రత్యేక టోకెన్లతో దాన్ని ర్యాప్ చేసాము. ఆ తర్వాత మోడల్ ఆ ప్రాంప్ట్‌ను ఒక హైకూతో పూర్తి చేస్తుంది.
- **device**: ఈ ఉదాహరణలో కంప్యూటేషన్కి CPUని ఉపయోగిస్తున్నాము. Candle CUDA మరియు Metal తో GPU మీద కూడా నడపడాన్ని మద్దతు ఇస్తుంది.

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

మేము `hf_hub` API ను ఉపయోగించి Hugging Face మోడల్ హబ్ నుండి మోడల్ మరియు టోకనైజర్ ఫైళ్లను డౌన్లోడ్ చేస్తాము. `gguf` ఫైల్‌లో క్వాంటైజ్డ్ మోడల్ వెయిట్స్ ఉంటాయి, కాగా `tokenizer.json` ఫైల్ మన ఇన్పుట్ టెక్స్ట్‌ను టోకనైజ్ చేయడానికి ఉపయోగించబడుతుంది. ఒకసారి డౌన్లోడ్ ఐన తర్వాత మోడల్ క్యాష్ అవుతుందని, కాబట్టి మొదటి అమలు స్లోగా ఉండవచ్చు (మోడల్ యొక్క 2.4GB ను డౌన్లోడ్ చేస్తుంది) కానీ తరువాతి అమల్స్ వేగంగా ఉంటాయి.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

మేము క్వాంటైజ్డ్ మోడల్ వెయిట్స్‌ను మెమరీలోలోడ్ చేసి Phi-3 మోడల్‌ను ప్రారంభిస్తాము. ఈ దశలో `gguf` ఫైల్ నుండి మోడల్ వెయిట్స్‌ను చదివి, పేర్కొన్న డివైస్ (ఈ కేసులో CPU) పై ఇన్ఫరెన్స్ కోసం మోడల్ సెట్ చేయడం జరుగుతుంది.

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

ఈ దశలో, మన ఇన్పుట్ ప్రాంప్ట్‌ను టోకనైజ్ చేసి దాన్ని టోకెన్ ఐడీల శ్రేణిగా మార్చి ఇన్ఫరెన్స్ కోసం సిద్ధం చేస్తాము. మనం కూడా sampling ప్రక్రియను నిర్వహించడానికి `LogitsProcessor` ను ప్రారంభిస్తాము (వాక్యాల పై probability distribution ను నిర్వహించడం) ఇవ్వబడిన `temperature` మరియు `top_p` విలువల ఆధారంగా. ప్రతి టోకెన్‌ను టెన్సర్‌గా మార్చి, మోడల్ ద్వారా లాజిట్స్ పొందడానికి పంపబడుతుంది.

లూప్ ప్రతి ప్రాంప్ట్ టోకెన్‌ను ప్రాసెస్ చేయగా, లాజిట్స్ ప్రాసెసర్‌ను అప్డేట్ చేసి తదుపరి టోకెన్ జనరేషన్‌కు సిద్ధం చేస్తుంది.

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

ఇన్ఫరెన్స్ లూప్‌లో, మనం కోరుకున్న sample length చేరేవరకు లేదా end-of-sequence టోకెన్ ఎటు వచ్చేవరకు టోకెన్స్‌ను ఒకదాని తర్వాత ఒకటి ఉత్పత్తి చేస్తాము. తదుపరి టోకెన్‌ను టెన్సర్‌గా మార్చి మోడల్‌కి పంపిస్తారు, మరియు లాజిట్స్‌కు పెనాల్టీలు మరియు శాంప్లింగ్ వర్తింపజేయడానికి లాజిట్స్ ప్రాసెసింగ్ చేయబడుతుంది. తరువాత తదుపరి టోకెన్ నమూనా చేయబడుతుంది, డీకోడు చేసి వరుసకు జోడించబడుతుంది.
పునరావృత టెక్స్ట్‌ను నివారించడానికి, `repeat_last_n` మరియు `repeat_penalty` పారామీటర్ల ఆధారంగా పునరావృత టోకెన్లపై పెనాల్టీ వర్తింపజేస్తారు.

చివరగా, ఉత్పత్తి అయిన టెక్స్ట్ డీకోడవుతుండగా ప్రింట్ చేయబడుతుంది, ఇది స్ట్రీమ్ చేయబడే రియల్-టైం అవుట్‌పుట్‌ను నిర్ధారిస్తుంది.

## Step 7: Run the Application

అప్లికేషన్‌ను నడపడానికి, టెర్మినల్‌లో క్రింది కమాండ్‌ను అమలు చేయండి:

```bash
cargo run --release
```

ఇది Phi-3 మోడల్ ద్వారా రూపొందించబడిన ఐస్ హాకీ గురించి ఒక హైకూ ను ప్రింట్ చేయాలి. దాంటోలాంటి ఏమైనా:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

లేదా

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

ఈ దశలను అనుసరించడం ద్వారా, రస్ట్ మరియు Candle ఉపయోగించి Phi-3 మోడల్‌తో టెక్స్ట్ జనరేషన్‌ను 100 లైన్ల లోపు కోడ్‌తో నిర్వహించవచ్చు. కోడ్ మోడల్ లోడింగ్, టోకనైజేషన్ మరియు ఇన్ఫరెన్స్‌ను హ్యాండిల్ చేస్తుంది, టెన్సర్లు మరియు లాజిట్స్ ప్రాసెసింగ్ని ఉపయోగించి ఇన్పుట్ ప్రాంప్ట్ ఆధారంగా సమగ్రమైన టెక్స్ట్‌ను రూపొందిస్తుంది.

ఈ కంసోల్ అప్లికేషన్ Windows, Linux మరియు Mac OS పై నడచవచ్చు. రస్ట్ యొక్క పోర్టబిలిటీ వల్ల, కోడ్‌ను మొబైల్ యాప్స్‌లో నడిచే లైబ్రరీగా కూడా అనుకూలపరచవచ్చు (మొబైల్‌లో కంసోల్ అప్లికేషన్లు నడపలేము, చివరికి).

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

గమనిక: ఈ కోడ్‌ను aarch64 Linux లేదా aarch64 Windows పై నడపడానికి, `.cargo/config` అనే ఫైల్‌ను క్రింది కంటెంట్‌తో జోడించండి:

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

> మీరు Phi-3 మోడల్‌ను రస్ట్ మరియు Candleతో ఎలా ఉపయోగించాలో వివిధ ప్రత్యామ్నాయ పద్ధతుల సహా మరిన్ని ఉదాహరణలకు అధికారిక [Candle ఉదాహరణలు](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) రిపోజిటరీని సందర్శించవచ్చు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యత మినహాయింపు:
ఈ పత్రం AI అనువాద seva [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వాన్ని సాధించడానికి ప్రయత్నిస్తున్నప్పటికీ, స్వయంచాలక అనువాదాల్లో తప్పులు లేదా పొరపాట్లు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. అసలు పత్రాన్ని దాని స్థానిక భాషలో ఉన్న రూపాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి, వృత్తిపరులైన మానవ అనువాదాన్ని ఉపయోగించాలని సూచించబడుతుంది. ఈ అనువాదం ఉపయోగించడం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థమయ్యే విషయాల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->