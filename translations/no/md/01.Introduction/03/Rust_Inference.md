<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:30:38+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "no"
}
-->
# Kryssplattform inferens med Rust

Denne veiledningen tar oss gjennom prosessen med å utføre inferens ved hjelp av Rust og [Candle ML-rammeverket](https://github.com/huggingface/candle) fra HuggingFace. Å bruke Rust til inferens gir flere fordeler, spesielt sammenlignet med andre programmeringsspråk. Rust er kjent for sin høye ytelse, på nivå med C og C++. Dette gjør det til et utmerket valg for inferensoppgaver, som ofte kan være beregningsintensive. Dette skyldes særlig nullkostnadsabstraksjoner og effektiv minnehåndtering, uten overhead fra søppelrydding. Rusts kryssplattformmuligheter gjør det mulig å utvikle kode som kjører på ulike operativsystemer, inkludert Windows, macOS og Linux, samt mobile operativsystemer, uten store endringer i kodebasen.

Forutsetningen for å følge denne veiledningen er å [installere Rust](https://www.rust-lang.org/tools/install), som inkluderer Rust-kompilatoren og Cargo, Rusts pakkebehandler.

## Steg 1: Opprett et nytt Rust-prosjekt

For å opprette et nytt Rust-prosjekt, kjør følgende kommando i terminalen:

```bash
cargo new phi-console-app
```

Dette genererer en grunnleggende prosjektstruktur med en `Cargo.toml`-fil og en `src`-mappe som inneholder en `main.rs`-fil.

Deretter legger vi til avhengighetene våre – nemlig `candle`, `hf-hub` og `tokenizers` crates – i `Cargo.toml`-filen:

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

I `main.rs`-filen setter vi opp de innledende parameterne for inferensen. De vil alle være hardkodet for enkelhets skyld, men vi kan endre dem etter behov.

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

- **temperature**: Styrer tilfeldigheten i utvalgsprosessen.
- **sample_len**: Angir maksimal lengde på den genererte teksten.
- **top_p**: Brukes for nucleus sampling for å begrense antall tokens som vurderes i hvert steg.
- **repeat_last_n**: Styrer antall tokens som vurderes for å påføre en straff for å unngå repeterende sekvenser.
- **repeat_penalty**: Straffeverdi for å motvirke gjentatte tokens.
- **seed**: En tilfeldig seed (vi kan bruke en konstant verdi for bedre reproduserbarhet).
- **prompt**: Startteksten for genereringen. Merk at vi ber modellen generere et haiku om ishockey, og at vi pakker det inn med spesialtokens for å indikere bruker- og assistentdelen av samtalen. Modellen fullfører deretter prompten med et haiku.
- **device**: Vi bruker CPU for beregning i dette eksempelet. Candle støtter også kjøring på GPU med CUDA og Metal.

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

Vi bruker `hf_hub` API-et for å laste ned modell- og tokenizer-filer fra Hugging Face model hub. `gguf`-filen inneholder de kvantiserte modellvektene, mens `tokenizer.json`-filen brukes til å tokenisere inndataene våre. Når modellen er lastet ned, blir den bufret, så første kjøring vil være treg (siden den laster ned 2,4 GB med modell), men påfølgende kjøringer går raskere.

## Steg 4: Last inn modell

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Vi laster de kvantiserte modellvektene inn i minnet og initialiserer Phi-3-modellen. Dette steget innebærer å lese modellvektene fra `gguf`-filen og sette opp modellen for inferens på den angitte enheten (CPU i dette tilfellet).

## Steg 5: Behandle prompt og forbered til inferens

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

I dette steget tokeniserer vi inndata-prompten og forbereder den for inferens ved å konvertere den til en sekvens av token-IDer. Vi initialiserer også `LogitsProcessor` for å håndtere utvalgsprosessen (sannsynlighetsfordeling over vokabularet) basert på de gitte `temperature` og `top_p` verdiene. Hver token konverteres til en tensor og sendes gjennom modellen for å hente logits.

Løkken behandler hver token i prompten, oppdaterer logits-prosessoren og forbereder neste token-generering.

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

I inferensløkken genererer vi tokens én etter én til vi når ønsket lengde eller støter på end-of-sequence-token. Neste token konverteres til en tensor og sendes gjennom modellen, mens logits behandles for å påføre straffer og sampling. Deretter samples neste token, dekodes og legges til sekvensen.  
For å unngå repeterende tekst påføres en straff på gjentatte tokens basert på `repeat_last_n` og `repeat_penalty` parametrene.

Til slutt skrives den genererte teksten ut fortløpende etter hvert som den dekodes, for å sikre sanntidsstrømming.

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

Ved å følge disse stegene kan vi utføre tekstgenerering med Phi-3-modellen ved hjelp av Rust og Candle på under 100 linjer kode. Koden håndterer lasting av modell, tokenisering og inferens, og utnytter tensorer og logits-prosessering for å generere sammenhengende tekst basert på inndata-prompten.

Denne konsollapplikasjonen kan kjøre på Windows, Linux og Mac OS. På grunn av Rusts portabilitet kan koden også tilpasses til et bibliotek som kan kjøre inne i mobilapper (vi kan tross alt ikke kjøre konsollapper der).

## Vedlegg: fullstendig kode

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

Merk: for å kjøre denne koden på aarch64 Linux eller aarch64 Windows, legg til en fil kalt `.cargo/config` med følgende innhold:

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

> Du kan besøke det offisielle [Candle-eksempel](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) arkivet for flere eksempler på hvordan du bruker Phi-3-modellen med Rust og Candle, inkludert alternative tilnærminger til inferens.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.