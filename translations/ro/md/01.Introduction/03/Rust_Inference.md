<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:08:04+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ro"
}
-->
# Cross-platform inference with Rust

Acest tutorial ne va ghida prin procesul de realizare a inferenței folosind Rust și [Candle ML framework](https://github.com/huggingface/candle) de la HuggingFace. Utilizarea Rust pentru inferență oferă mai multe avantaje, în special în comparație cu alte limbaje de programare. Rust este cunoscut pentru performanța sa ridicată, comparabilă cu cea a limbajelor C și C++. Acest lucru îl face o alegere excelentă pentru sarcini de inferență, care pot fi intensive din punct de vedere computațional. În special, acest lucru se datorează abstracțiilor fără costuri suplimentare și gestionării eficiente a memoriei, fără suprasarcină de garbage collection. Capacitățile cross-platform ale Rust permit dezvoltarea de cod care rulează pe diverse sisteme de operare, inclusiv Windows, macOS și Linux, precum și pe sisteme de operare mobile, fără modificări semnificative ale bazei de cod.

Prerequisitul pentru a urma acest tutorial este să [instalați Rust](https://www.rust-lang.org/tools/install), care include compilatorul Rust și Cargo, managerul de pachete Rust.

## Step 1: Create a New Rust Project

Pentru a crea un nou proiect Rust, executați următoarea comandă în terminal:

```bash
cargo new phi-console-app
```

Aceasta generează o structură inițială a proiectului cu un fișier `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`:

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

În fișierul main.rs, vom seta parametrii inițiali pentru inferența noastră. Toți vor fi hardcodați pentru simplitate, dar îi putem modifica după cum este necesar.

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

- **temperature**: Controlează gradul de aleatorietate al procesului de eșantionare.
- **sample_len**: Specifică lungimea maximă a textului generat.
- **top_p**: Folosit pentru nucleus sampling pentru a limita numărul de tokeni considerați la fiecare pas.
- **repeat_last_n**: Controlează numărul de tokeni luați în considerare pentru aplicarea unei penalizări pentru a preveni secvențele repetitive.
- **repeat_penalty**: Valoarea penalizării pentru a descuraja tokenii repetați.
- **seed**: O sămânță aleatorie (am putea folosi o valoare constantă pentru o reproducibilitate mai bună).
- **prompt**: Textul inițial al promptului pentru a începe generarea. Observați că îi cerem modelului să genereze un haiku despre hochei pe gheață și că îl închidem între tokeni speciali pentru a indica părțile utilizatorului și asistentului în conversație. Modelul va completa promptul cu un haiku.
- **device**: În acest exemplu folosim CPU-ul pentru calcul. Candle suportă rularea pe GPU cu CUDA și Metal de asemenea.

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

Folosim fișierul `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` pentru a tokeniza textul de intrare. Odată descărcat, modelul este stocat în cache, astfel că prima execuție va fi lentă (deoarece descarcă cei 2.4GB ai modelului), dar execuțiile următoare vor fi mai rapide.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Încărcăm greutățile cuantificate ale modelului în memorie și inițializăm modelul Phi-3. Această etapă implică citirea greutăților modelului din fișierul `gguf` și configurarea modelului pentru inferență pe dispozitivul specificat (CPU în acest caz).

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

În această etapă, tokenizăm promptul de intrare și îl pregătim pentru inferență, convertindu-l într-o secvență de ID-uri de tokeni. De asemenea, inițializăm valorile `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Fiecare token este convertit într-un tensor și trecut prin model pentru a obține logits.

Buclează prin fiecare token din prompt, actualizând procesorul de logits și pregătind generarea următorului token.

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

În bucla de inferență, generăm tokeni unul câte unul până când atingem lungimea dorită a eșantionului sau întâlnim tokenul de sfârșit de secvență. Tokenul următor este convertit într-un tensor și trecut prin model, iar logits sunt procesați pentru aplicarea penalizărilor și eșantionării. Apoi tokenul următor este eșantionat, decodat și adăugat la secvență.
Pentru a evita textul repetitiv, se aplică o penalizare tokenilor repetați pe baza parametrilor `repeat_last_n` and `repeat_penalty`.

În final, textul generat este afișat pe măsură ce este decodat, asigurând o ieșire în timp real.

## Step 7: Run the Application

Pentru a rula aplicația, executați următoarea comandă în terminal:

```bash
cargo run --release
```

Aceasta ar trebui să afișeze un haiku despre hochei pe gheață generat de modelul Phi-3. Ceva de genul:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

sau

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

Urmând acești pași, putem realiza generarea de text folosind modelul Phi-3 cu Rust și Candle în mai puțin de 100 de linii de cod. Codul gestionează încărcarea modelului, tokenizarea și inferența, folosind tensori și procesarea logits pentru a genera un text coerent pe baza promptului de intrare.

Această aplicație de consolă poate rula pe Windows, Linux și Mac OS. Datorită portabilității Rust, codul poate fi adaptat și într-o bibliotecă care să ruleze în aplicații mobile (nu putem rula aplicații de consolă acolo, până la urmă).

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

Notă: pentru a rula acest cod pe aarch64 Linux sau aarch64 Windows, adăugați un fișier numit `.cargo/config` cu următorul conținut:

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

> Puteți vizita depozitul oficial [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) pentru mai multe exemple despre cum să folosiți modelul Phi-3 cu Rust și Candle, inclusiv abordări alternative pentru inferență.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.