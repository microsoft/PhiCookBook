<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:28:54+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "it"
}
-->
# Inferenza multipiattaforma con Rust

Questo tutorial ci guiderà nel processo di eseguire inferenza utilizzando Rust e il [framework Candle ML](https://github.com/huggingface/candle) di HuggingFace. Usare Rust per l'inferenza offre diversi vantaggi, soprattutto se confrontato con altri linguaggi di programmazione. Rust è noto per le sue alte prestazioni, comparabili a quelle di C e C++. Questo lo rende una scelta eccellente per compiti di inferenza, che possono essere computazionalmente intensivi. In particolare, ciò è dovuto alle astrazioni a costo zero e alla gestione efficiente della memoria, senza overhead di garbage collection. Le capacità multipiattaforma di Rust permettono di sviluppare codice che gira su vari sistemi operativi, inclusi Windows, macOS e Linux, così come su sistemi operativi mobili, senza modifiche significative al codice.

Il prerequisito per seguire questo tutorial è [installare Rust](https://www.rust-lang.org/tools/install), che include il compilatore Rust e Cargo, il gestore di pacchetti Rust.

## Passo 1: Creare un nuovo progetto Rust

Per creare un nuovo progetto Rust, esegui il seguente comando nel terminale:

```bash
cargo new phi-console-app
```

Questo genera una struttura iniziale del progetto con un file `Cargo.toml` e una cartella `src` contenente un file `main.rs`.

Successivamente, aggiungeremo le nostre dipendenze - ovvero i crate `candle`, `hf-hub` e `tokenizers` - al file `Cargo.toml`:

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

## Passo 2: Configurare i parametri di base

All’interno del file main.rs, imposteremo i parametri iniziali per la nostra inferenza. Saranno tutti hardcoded per semplicità, ma potremo modificarli secondo necessità.

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

- **temperature**: Controlla la casualità del processo di campionamento.
- **sample_len**: Specifica la lunghezza massima del testo generato.
- **top_p**: Usato per il campionamento nucleus per limitare il numero di token considerati ad ogni passo.
- **repeat_last_n**: Controlla il numero di token considerati per applicare una penalità e prevenire sequenze ripetitive.
- **repeat_penalty**: Il valore della penalità per scoraggiare token ripetuti.
- **seed**: Un seme casuale (potremmo usare un valore costante per una migliore riproducibilità).
- **prompt**: Il testo iniziale per avviare la generazione. Nota che chiediamo al modello di generare un haiku sull’hockey su ghiaccio, e che lo avvolgiamo con token speciali per indicare le parti di utente e assistente della conversazione. Il modello completerà quindi il prompt con un haiku.
- **device**: In questo esempio usiamo la CPU per il calcolo. Candle supporta anche l’esecuzione su GPU con CUDA e Metal.

## Passo 3: Scaricare/Preparare modello e tokenizer

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

Usiamo l’API `hf_hub` per scaricare i file del modello e del tokenizer dal model hub di Hugging Face. Il file `gguf` contiene i pesi quantizzati del modello, mentre il file `tokenizer.json` serve per tokenizzare il testo di input. Una volta scaricato, il modello viene memorizzato nella cache, quindi la prima esecuzione sarà lenta (poiché scarica i 2.4GB del modello), ma le esecuzioni successive saranno più veloci.

## Passo 4: Caricare il modello

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Carichiamo i pesi quantizzati del modello in memoria e inizializziamo il modello Phi-3. Questo passaggio comporta la lettura dei pesi dal file `gguf` e la configurazione del modello per l’inferenza sul dispositivo specificato (in questo caso la CPU).

## Passo 5: Processare il prompt e prepararsi per l’inferenza

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

In questo passaggio, tokenizziamo il prompt di input e lo prepariamo per l’inferenza convertendolo in una sequenza di ID token. Inizializziamo anche il `LogitsProcessor` per gestire il processo di campionamento (distribuzione di probabilità sul vocabolario) basato sui valori di `temperature` e `top_p` forniti. Ogni token viene convertito in un tensore e passato attraverso il modello per ottenere i logits.

Il ciclo elabora ogni token del prompt, aggiornando il logits processor e preparando la generazione del token successivo.

## Passo 6: Inferenza

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

Nel ciclo di inferenza, generiamo i token uno alla volta finché non raggiungiamo la lunghezza desiderata o incontriamo il token di fine sequenza. Il token successivo viene convertito in tensore e passato attraverso il modello, mentre i logits vengono processati per applicare penalità e campionamento. Successivamente il token successivo viene campionato, decodificato e aggiunto alla sequenza.
Per evitare testi ripetitivi, viene applicata una penalità ai token ripetuti basata sui parametri `repeat_last_n` e `repeat_penalty`.

Infine, il testo generato viene stampato man mano che viene decodificato, garantendo un output in tempo reale e in streaming.

## Passo 7: Eseguire l’applicazione

Per eseguire l’applicazione, digita il seguente comando nel terminale:

```bash
cargo run --release
```

Questo dovrebbe stampare un haiku sull’hockey su ghiaccio generato dal modello Phi-3. Qualcosa come:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

oppure

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusione

Seguendo questi passaggi, possiamo eseguire la generazione di testo usando il modello Phi-3 con Rust e Candle in meno di 100 righe di codice. Il codice gestisce il caricamento del modello, la tokenizzazione e l’inferenza, sfruttando tensori e la gestione dei logits per generare testo coerente basato sul prompt di input.

Questa applicazione da console può girare su Windows, Linux e Mac OS. Grazie alla portabilità di Rust, il codice può anche essere adattato a una libreria da utilizzare all’interno di app mobili (dopotutto non possiamo eseguire app da console su dispositivi mobili).

## Appendice: codice completo

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

Nota: per eseguire questo codice su Linux aarch64 o Windows aarch64, aggiungi un file chiamato `.cargo/config` con il seguente contenuto:

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

> Puoi visitare il repository ufficiale degli [esempi Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) per ulteriori esempi su come usare il modello Phi-3 con Rust e Candle, inclusi approcci alternativi all’inferenza.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.