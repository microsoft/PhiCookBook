<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:57:42+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "sv"
}
-->
# Cross-platform inference med Rust

Den här guiden visar hur vi kan utföra inferens med Rust och [Candle ML framework](https://github.com/huggingface/candle) från HuggingFace. Att använda Rust för inferens har flera fördelar, särskilt jämfört med andra programmeringsspråk. Rust är känt för sin höga prestanda, jämförbar med C och C++. Det gör det till ett utmärkt val för inferensuppgifter, som ofta är beräkningsintensiva. Detta drivs framför allt av zero-cost abstractions och effektiv minneshantering utan overhead från garbage collection. Rusts plattformsoberoende möjligheter gör det möjligt att utveckla kod som körs på olika operativsystem, inklusive Windows, macOS och Linux, samt mobila operativsystem, utan större ändringar i kodbasen.

Förutsättningen för att följa denna guide är att [installera Rust](https://www.rust-lang.org/tools/install), vilket inkluderar Rust-kompilatorn och Cargo, Rusts paketchef.

## Steg 1: Skapa ett nytt Rust-projekt

För att skapa ett nytt Rust-projekt, kör följande kommando i terminalen:

```bash
cargo new phi-console-app
```

Detta genererar en grundläggande projektstruktur med en `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`-fil:

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

## Steg 2: Konfigurera grundläggande parametrar

I filen main.rs sätter vi upp de initiala parametrarna för vår inferens. De kommer alla att vara hårdkodade för enkelhetens skull, men vi kan ändra dem vid behov.

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

- **temperature**: Styr slumpmässigheten i samplingprocessen.
- **sample_len**: Anger den maximala längden på den genererade texten.
- **top_p**: Används för nucleus-sampling för att begränsa antalet token som beaktas vid varje steg.
- **repeat_last_n**: Kontrollerar hur många token som beaktas för att applicera en straff för att undvika upprepningar.
- **repeat_penalty**: Straffvärdet för att avskräcka upprepade token.
- **seed**: En slumpmässig seed (vi kan använda ett konstant värde för bättre reproducerbarhet).
- **prompt**: Den initiala prompten för att starta genereringen. Observera att vi ber modellen generera en haiku om ishockey, och att vi omger den med specialtoken för att indikera användar- och assistentdelarna i konversationen. Modellen kommer sedan att komplettera prompten med en haiku.
- **device**: Vi använder CPU för beräkning i detta exempel. Candle stödjer även körning på GPU med CUDA och Metal.

## Steg 3: Ladda ner/förbered modell och tokenizer

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

Vi använder filen `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` för att tokenisera vår ingångstext. När modellen har laddats ner cachas den, så första körningen går långsamt (då 2,4 GB modell laddas ner) men efterföljande körningar går snabbare.

## Steg 4: Ladda modellen

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Vi laddar de kvantiserade modellvikterna i minnet och initierar Phi-3 modellen. Detta steg innebär att läsa modellvikterna från `gguf`-filen och ställa in modellen för inferens på den angivna enheten (CPU i detta fall).

## Steg 5: Bearbeta prompt och förbered för inferens

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

I detta steg tokeniserar vi input-prompten och förbereder den för inferens genom att konvertera den till en sekvens av token-ID:n. Vi initierar även `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`-värdena. Varje token konverteras till en tensor och skickas genom modellen för att få logits.

Loopen bearbetar varje token i prompten, uppdaterar logitsprocessorn och förbereder för nästa token-generering.

## Steg 6: Inferens

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

I inferensloopen genererar vi token ett i taget tills vi når önskad sample-längd eller stöter på end-of-sequence-token. Nästa token konverteras till en tensor och skickas genom modellen, medan logits bearbetas för att applicera straff och sampling. Sedan samplas nästa token, avkodas och läggs till sekvensen.
För att undvika repetitiv text appliceras ett straff på upprepade token baserat på parametrarna `repeat_last_n` and `repeat_penalty`.

Till sist skrivs den genererade texten ut allteftersom den avkodas, vilket säkerställer strömmat realtidsutdata.

## Steg 7: Kör applikationen

För att köra applikationen, kör följande kommando i terminalen:

```bash
cargo run --release
```

Detta bör skriva ut en haiku om ishockey genererad av Phi-3 modellen. Något i stil med:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

eller

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Slutsats

Genom att följa dessa steg kan vi generera text med Phi-3 modellen med Rust och Candle på under 100 kodrader. Koden hanterar modellinladdning, tokenisering och inferens, och använder tensorer och logitsbearbetning för att generera sammanhängande text baserat på ingångsprompten.

Denna konsolapplikation kan köras på Windows, Linux och Mac OS. Tack vare Rusts portabilitet kan koden också anpassas till ett bibliotek som kan köras i mobilappar (konsolappar kan vi ju inte köra där).

## Appendix: fullständig kod

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

Observera: för att köra denna kod på aarch64 Linux eller aarch64 Windows, lägg till en fil som heter `.cargo/config` med följande innehåll:

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

> Du kan besöka det officiella [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)-arkivet för fler exempel på hur man använder Phi-3 modellen med Rust och Candle, inklusive alternativa tillvägagångssätt för inferens.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.