<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:59:06+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "no"
}
-->
# Plattformuavhengig inferens med Rust

Denne veiledningen vil lede oss gjennom prosessen med å utføre inferens ved hjelp av Rust og [Candle ML-rammeverket](https://github.com/huggingface/candle) fra HuggingFace. Å bruke Rust til inferens gir flere fordeler, spesielt sammenlignet med andre programmeringsspråk. Rust er kjent for sin høye ytelse, sammenlignbar med C og C++. Dette gjør det til et utmerket valg for inferensoppgaver, som ofte kan være beregningsintensive. Dette skyldes særlig de kostnadsfrie abstraksjonene og effektiv minnehåndtering uten overhead fra garbage collection. Rusts plattformuavhengige egenskaper muliggjør utvikling av kode som kan kjøre på ulike operativsystemer, inkludert Windows, macOS og Linux, samt mobile operativsystemer, uten vesentlige endringer i kodebasen.

Forutsetningen for å følge denne veiledningen er å [installere Rust](https://www.rust-lang.org/tools/install), som inkluderer Rust-kompilatoren og Cargo, Rusts pakkebehandler.

## Steg 1: Opprett et nytt Rust-prosjekt

For å opprette et nytt Rust-prosjekt, kjør følgende kommando i terminalen:

```bash
cargo new phi-console-app
```

Dette genererer en grunnleggende prosjektstruktur med en `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Steg 2: Konfigurer grunnleggende parametere

Inne i main.rs-filen setter vi opp de innledende parameterne for vår inferens. De blir alle hardkodet for enkelhets skyld, men vi kan endre dem etter behov.

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

- **temperature**: Styrer hvor tilfeldig samplingprosessen er.
- **sample_len**: Angir maksimal lengde på den genererte teksten.
- **top_p**: Brukes for nucleus-sampling for å begrense antall tokens som vurderes for hvert steg.
- **repeat_last_n**: Styrer hvor mange tokens som vurderes for å påføre en straff for å unngå repeterende sekvenser.
- **repeat_penalty**: Straffeverdi for å motvirke gjentatte tokens.
- **seed**: Et tilfeldig frø (vi kan bruke en konstant verdi for bedre reproduserbarhet).
- **prompt**: Den innledende teksten som starter genereringen. Merk at vi ber modellen om å generere et haiku om ishockey, og at vi pakker det inn med spesielle tokens for å indikere bruker- og assistent-delen av samtalen. Modellen vil så fullføre prompten med et haiku.
- **device**: Vi bruker CPU for beregning i dette eksemplet. Candle støtter også kjøring på GPU med CUDA og Metal.

## Steg 3: Last ned/forbered modell og tokenizer

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

Vi bruker `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json`-filen for å tokenisere vår inputtekst. Når modellen er lastet ned, blir den bufret, så første kjøring vil være treg (siden den laster ned 2,4 GB med modell) men påfølgende kjøringer vil gå raskere.

## Steg 4: Last inn modell

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Vi laster de kvantiserte modellvektene inn i minnet og initialiserer Phi-3-modellen. Dette steget innebærer å lese modellvektene fra `gguf`-filen og sette opp modellen for inferens på den angitte enheten (her CPU).

## Steg 5: Behandle prompt og forbered for inferens

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

I dette steget tokeniserer vi input-prompten og forbereder den for inferens ved å konvertere den til en sekvens av token-IDer. Vi initialiserer også `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`-verdiene. Hver token konverteres til en tensor og sendes gjennom modellen for å hente logits.

Løkken behandler hver token i prompten, oppdaterer logits-prosessoren og forbereder neste token for generering.

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

I inferensløkken genererer vi tokens én etter én til vi når ønsket sample-lengde eller støter på end-of-sequence-token. Neste token konverteres til en tensor og sendes gjennom modellen, mens logits behandles for å påføre straffer og sampling. Deretter samples neste token, dekodes og legges til sekvensen. For å unngå repeterende tekst, påføres en straff på gjentatte tokens basert på `repeat_last_n` and `repeat_penalty`-parameterne.

Til slutt printes den genererte teksten fortløpende etter hvert som den dekodes, noe som sikrer strømmet sanntidsutdata.

## Steg 7: Kjør applikasjonen

For å kjøre applikasjonen, utfør følgende kommando i terminalen:

```bash
cargo run --release
```

Dette skal skrive ut et haiku om ishockey generert av Phi-3-modellen. Noe som:

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

## Konklusjon

Ved å følge disse stegene kan vi utføre tekstgenerering ved hjelp av Phi-3-modellen med Rust og Candle på under 100 linjer kode. Koden håndterer modellinnlasting, tokenisering og inferens, og benytter tensorer og logits-prosessering for å generere sammenhengende tekst basert på input-prompten.

Denne konsollapplikasjonen kan kjøre på Windows, Linux og Mac OS. På grunn av Rusts portabilitet kan koden også tilpasses til et bibliotek som kan kjøre inne i mobilapper (konsollapper kan vi tross alt ikke kjøre der).

## Vedlegg: full kode

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

Merk: for å kjøre denne koden på aarch64 Linux eller aarch64 Windows, legg til en fil med navnet `.cargo/config` med følgende innhold:

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

> Du kan besøke det offisielle [Candle-eksemplene](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)-arkivet for flere eksempler på hvordan du bruker Phi-3-modellen med Rust og Candle, inkludert alternative tilnærminger til inferens.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på det opprinnelige språket bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.