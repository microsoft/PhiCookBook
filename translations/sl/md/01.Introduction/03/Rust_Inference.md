<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:34:36+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "sl"
}
-->
# Večplatformno sklepanje z Rustom

Ta vodič nas bo popeljal skozi postopek izvajanja sklepanja z uporabo Rust in [Candle ML framework](https://github.com/huggingface/candle) iz HuggingFace. Uporaba Rust za sklepanje prinaša več prednosti, še posebej v primerjavi z drugimi programskimi jeziki. Rust je znan po visoki zmogljivosti, primerljivi s C in C++. To ga naredi odlično izbiro za naloge sklepanja, ki so lahko računsko zahtevne. Posebej to omogočajo abstrakcije brez stroškov in učinkovito upravljanje z pomnilnikom, ki ne vključuje odpadkovne zbirke. Rustove večplatformne zmogljivosti omogočajo razvoj kode, ki teče na različnih operacijskih sistemih, vključno z Windows, macOS in Linux, pa tudi na mobilnih operacijskih sistemih, brez večjih sprememb v kodi.

Pogoj za sledenje temu vodiču je [namestitev Rust](https://www.rust-lang.org/tools/install), ki vključuje Rust prevajalnik in Cargo, upravljalnik paketov za Rust.

## Korak 1: Ustvarite nov Rust projekt

Za ustvarjanje novega Rust projekta zaženite naslednji ukaz v terminalu:

```bash
cargo new phi-console-app
```

To ustvari začetno strukturo projekta z datoteko `Cargo.toml` in mapo `src`, ki vsebuje datoteko `main.rs`.

Nato bomo dodali naše odvisnosti - `candle`, `hf-hub` in `tokenizers` crates - v datoteko `Cargo.toml`:

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

## Korak 2: Nastavite osnovne parametre

V datoteki main.rs bomo nastavili začetne parametre za naše sklepanje. Za preprostost bodo vsi trdo kodirani, vendar jih lahko po potrebi spremenimo.

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

- **temperature**: Nadzoruje naključnost procesa vzorčenja.
- **sample_len**: Določa največjo dolžino generiranega besedila.
- **top_p**: Uporablja se za jedrno vzorčenje, da omeji število tokenov, ki se upoštevajo pri vsakem koraku.
- **repeat_last_n**: Nadzoruje število tokenov, ki se upoštevajo za uporabo kazni, da preprečimo ponavljajoče se zaporedje.
- **repeat_penalty**: Vrednost kazni za odvračanje ponavljajočih se tokenov.
- **seed**: Naključna začetna vrednost (lahko uporabimo konstantno vrednost za boljšo ponovljivost).
- **prompt**: Začetno besedilo poziva za začetek generiranja. Opazite, da modelu naročimo, naj ustvari haiku o hokeju na ledu, in da ga ovijemo s posebnimi tokeni, ki označujejo dele pogovora uporabnika in asistenta. Model bo nato dokončal poziv s haiku.
- **device**: V tem primeru uporabljamo CPU za izračune. Candle podpira tudi izvajanje na GPU z CUDA in Metal.

## Korak 3: Prenesite/pripravite model in tokenizer

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

Uporabimo `hf_hub` API za prenos modela in datotek tokenizerja iz Hugging Face model hub-a. Datoteka `gguf` vsebuje kvantizirane uteži modela, medtem ko se datoteka `tokenizer.json` uporablja za tokenizacijo našega vhodnega besedila. Ko je model prenesen, se shrani v predpomnilnik, zato bo prvi zagon počasnejši (ker prenese 2,4 GB modela), naslednji pa hitrejši.

## Korak 4: Naložite model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Naložimo kvantizirane uteži modela v pomnilnik in inicializiramo model Phi-3. Ta korak vključuje branje uteži modela iz datoteke `gguf` in pripravo modela za sklepanje na določenem napravi (v tem primeru CPU).

## Korak 5: Obdelajte poziv in pripravite za sklepanje

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

V tem koraku tokeniziramo vhodni poziv in ga pripravimo za sklepanje tako, da ga pretvorimo v zaporedje ID-jev tokenov. Prav tako inicializiramo `LogitsProcessor`, ki upravlja proces vzorčenja (verjetnostno porazdelitev čez besednjak) glede na podane vrednosti `temperature` in `top_p`. Vsak token se pretvori v tensor in pošlje skozi model, da dobimo logite.

Zanka obdela vsak token v pozivu, posodablja procesor logitov in pripravlja naslednji token za generiranje.

## Korak 6: Sklepanje

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

V zanki sklepanja generiramo tokene enega za drugim, dokler ne dosežemo želene dolžine vzorca ali naletimo na konec zaporedja. Naslednji token se pretvori v tensor in pošlje skozi model, medtem ko se logiti obdelajo za uporabo kazni in vzorčenja. Nato se naslednji token vzorči, dekodira in doda v zaporedje.  
Da se izognemo ponavljajočemu se besedilu, se na ponovljene tokene uporabi kazen glede na parametra `repeat_last_n` in `repeat_penalty`.

Na koncu se generirano besedilo izpiše sproti, kar omogoča pretočni izhod v realnem času.

## Korak 7: Zaženite aplikacijo

Za zagon aplikacije izvedite naslednji ukaz v terminalu:

```bash
cargo run --release
```

To bi moralo izpisati haiku o hokeju na ledu, ki ga je ustvaril model Phi-3. Nekaj takega:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ali

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Zaključek

S sledenjem tem korakom lahko izvedemo generiranje besedila z modelom Phi-3 v Rustu in Candle v manj kot 100 vrsticah kode. Koda upravlja nalaganje modela, tokenizacijo in sklepanje, pri čemer uporablja tensore in obdelavo logitov za generiranje koherentnega besedila na podlagi vhodnega poziva.

Ta konzolna aplikacija lahko teče na Windows, Linux in Mac OS. Zaradi prenosljivosti Rust-a je kodo mogoče prilagoditi tudi v knjižnico, ki bi delovala znotraj mobilnih aplikacij (konzolnih aplikacij tam namreč ne moremo zagnati).

## Priloga: celotna koda

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

Opomba: za zagon te kode na aarch64 Linux ali aarch64 Windows dodajte datoteko z imenom `.cargo/config` z naslednjo vsebino:

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

> Za več primerov uporabe modela Phi-3 z Rust in Candle, vključno z alternativnimi pristopi k sklepanju, lahko obiščete uradni [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitorij.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.