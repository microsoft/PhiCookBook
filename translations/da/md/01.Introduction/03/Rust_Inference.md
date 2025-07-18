<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:30:21+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "da"
}
-->
# Cross-platform inferens med Rust

Denne vejledning vil guide os gennem processen med at udføre inferens ved hjælp af Rust og [Candle ML framework](https://github.com/huggingface/candle) fra HuggingFace. At bruge Rust til inferens giver flere fordele, især sammenlignet med andre programmeringssprog. Rust er kendt for sin høje ydeevne, der kan sammenlignes med C og C++. Det gør det til et fremragende valg til inferensopgaver, som kan være beregningsintensive. Dette skyldes især zero-cost abstraction og effektiv hukommelsesstyring uden overhead fra garbage collection. Rusts cross-platform kapabiliteter gør det muligt at udvikle kode, der kører på forskellige operativsystemer, herunder Windows, macOS og Linux, samt mobile operativsystemer, uden væsentlige ændringer i kodebasen.

Forudsætningen for at følge denne vejledning er at [installere Rust](https://www.rust-lang.org/tools/install), som inkluderer Rust-kompilatoren og Cargo, Rusts pakkehåndtering.

## Trin 1: Opret et nyt Rust-projekt

For at oprette et nyt Rust-projekt, kør følgende kommando i terminalen:

```bash
cargo new phi-console-app
```

Dette genererer en grundlæggende projektstruktur med en `Cargo.toml` fil og en `src` mappe, der indeholder en `main.rs` fil.

Dernæst tilføjer vi vores afhængigheder - nemlig `candle`, `hf-hub` og `tokenizers` crates - til `Cargo.toml` filen:

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

## Trin 2: Konfigurer grundlæggende parametre

Inde i main.rs-filen opsætter vi de indledende parametre for vores inferens. De bliver alle hardkodet for enkelhedens skyld, men vi kan ændre dem efter behov.

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

- **temperature**: Styrer tilfældigheden i sampling-processen.
- **sample_len**: Angiver den maksimale længde af den genererede tekst.
- **top_p**: Bruges til nucleus sampling for at begrænse antallet af tokens, der overvejes ved hvert trin.
- **repeat_last_n**: Styrer antallet af tokens, der overvejes for at anvende en straf for at undgå gentagne sekvenser.
- **repeat_penalty**: Strafværdien for at modvirke gentagne tokens.
- **seed**: Et tilfældigt seed (vi kunne bruge en konstant værdi for bedre reproducerbarhed).
- **prompt**: Den indledende prompttekst til at starte genereringen. Bemærk, at vi beder modellen om at generere et haiku om ishockey, og at vi omslutter det med specielle tokens for at indikere bruger- og assistentdelen af samtalen. Modellen vil derefter fuldføre prompten med et haiku.
- **device**: Vi bruger CPU’en til beregning i dette eksempel. Candle understøtter også kørsel på GPU med CUDA og Metal.

## Trin 3: Download/forbered model og tokenizer

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

Vi bruger `hf_hub` API’en til at downloade model- og tokenizer-filerne fra Hugging Face model hub. `gguf` filen indeholder de kvantiserede modelvægtninger, mens `tokenizer.json` filen bruges til at tokenisere vores inputtekst. Når modellen er downloadet, bliver den cachet, så første kørsel vil være langsom (da den downloader 2,4 GB modeldata), men efterfølgende kørsel vil være hurtigere.

## Trin 4: Indlæs model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Vi indlæser de kvantiserede modelvægtninger i hukommelsen og initialiserer Phi-3 modellen. Dette trin involverer at læse modelvægtningerne fra `gguf` filen og sætte modellen op til inferens på den angivne enhed (CPU i dette tilfælde).

## Trin 5: Behandl prompt og forbered til inferens

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

I dette trin tokeniserer vi inputprompten og forbereder den til inferens ved at konvertere den til en sekvens af token-ID’er. Vi initialiserer også `LogitsProcessor` til at håndtere sampling-processen (sandsynlighedsfordeling over ordforrådet) baseret på de givne `temperature` og `top_p` værdier. Hvert token konverteres til en tensor og føres gennem modellen for at få logits.

Løkken behandler hvert token i prompten, opdaterer logits-processoren og forbereder næste token-generering.

## Trin 6: Inferens

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

I inferens-løkken genererer vi tokens ét ad gangen, indtil vi når den ønskede sample-længde eller støder på end-of-sequence token. Det næste token konverteres til en tensor og føres gennem modellen, mens logits behandles for at anvende straf og sampling. Derefter samples det næste token, dekodes og tilføjes til sekvensen.  
For at undgå gentagende tekst anvendes en straf på gentagne tokens baseret på `repeat_last_n` og `repeat_penalty` parametrene.

Til sidst printes den genererede tekst løbende, så output vises i realtid.

## Trin 7: Kør applikationen

For at køre applikationen, udfør følgende kommando i terminalen:

```bash
cargo run --release
```

Dette skulle printe et haiku om ishockey genereret af Phi-3 modellen. Noget i stil med:

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

## Konklusion

Ved at følge disse trin kan vi udføre tekstgenerering med Phi-3 modellen ved hjælp af Rust og Candle på under 100 linjer kode. Koden håndterer modelindlæsning, tokenisering og inferens, og udnytter tensors og logits-behandling til at generere sammenhængende tekst baseret på inputprompten.

Denne konsolapplikation kan køre på Windows, Linux og Mac OS. På grund af Rusts portabilitet kan koden også tilpasses til et bibliotek, der kan køre inde i mobilapps (vi kan trods alt ikke køre konsolapps der).

## Appendiks: fuld kode

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

Bemærk: for at køre denne kode på aarch64 Linux eller aarch64 Windows, tilføj en fil med navnet `.cargo/config` med følgende indhold:

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

> Du kan besøge det officielle [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository for flere eksempler på, hvordan man bruger Phi-3 modellen med Rust og Candle, inklusive alternative tilgange til inferens.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.