<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T12:59:46+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "fi"
}
-->
# Cross-platform inference with Rust

Tämä opas ohjaa meidät läpi inferenssin suorittamisen Rustilla ja HuggingFacen [Candle ML -kehikolla](https://github.com/huggingface/candle). Rustin käyttö inferenssissä tarjoaa useita etuja, erityisesti verrattuna muihin ohjelmointikieliin. Rust tunnetaan korkeasta suorituskyvystään, joka on verrattavissa C:n ja C++:n tasoon. Tämä tekee siitä erinomaisen valinnan inferenssitehtäviin, jotka voivat olla laskennallisesti vaativia. Erityisesti tämä johtuu nollakustannuksisista abstraktioista ja tehokkaasta muistinhallinnasta, jossa ei ole roskienkeruusta aiheutuvaa ylimääräistä kuormitusta. Rustin monialustaiset ominaisuudet mahdollistavat koodin kehittämisen, joka toimii eri käyttöjärjestelmissä, kuten Windowsissa, macOS:ssä ja Linuxissa, sekä mobiilikäyttöjärjestelmissä ilman merkittäviä muutoksia koodipohjaan.

Edellytyksenä tämän oppaan seuraamiselle on [Rustin asentaminen](https://www.rust-lang.org/tools/install), joka sisältää Rust-kääntäjän ja Cargo-pakettienhallinnan.

## Vaihe 1: Luo uusi Rust-projekti

Luo uusi Rust-projekti suorittamalla seuraava komento terminaalissa:

```bash
cargo new phi-console-app
```

Tämä luo alkuperäisen projektirakenteen sisältäen `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`-tiedoston:

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

## Vaihe 2: Määritä perusparametrit

`main.rs`-tiedostossa asetamme inferenssin alkuparametrit. Ne kovakoodataan yksinkertaisuuden vuoksi, mutta niitä voidaan muokata tarpeen mukaan.

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

- **temperature**: Ohjaa satunnaisuutta näytteistysprosessissa.
- **sample_len**: Määrittää luodun tekstin maksimipituuden.
- **top_p**: Käytetään ydin-näytteistykseen rajoittamaan kunkin vaiheen huomioitavien tokenien määrää.
- **repeat_last_n**: Hallitsee tokenien määrää, joihin toistuvuusrangaistus kohdistetaan toistuvien sekvenssien estämiseksi.
- **repeat_penalty**: Rangaistusarvo toistuvien tokenien vähentämiseksi.
- **seed**: Satunnainen siemen (voisimme käyttää vakioarvoa paremman toistettavuuden takaamiseksi).
- **prompt**: Alkuperäinen kehoteteksti generoinnin aloittamiseksi. Huomaa, että pyydämme mallia luomaan haikun jääkiekosta ja ympäröimme sen erityisillä tokeneilla osoittamaan käyttäjän ja avustajan osat keskustelussa. Malli täydentää kehotteen haikulla.
- **device**: Tässä esimerkissä käytämme laskentaan CPU:ta. Candle tukee myös GPU:n käyttöä CUDA:n ja Metalin kautta.

## Vaihe 3: Lataa/valmistele malli ja tokenisoija

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

Käytämme `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json`-tiedostoa syötteen tokenisointiin. Kun malli on ladattu, se välimuistitetaan, joten ensimmäinen suoritus on hidas (koska malli, joka on 2,4 Gt, ladataan), mutta myöhemmät suoritukset ovat nopeampia.

## Vaihe 4: Lataa malli

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Lataamme kvantisoidut mallipainot muistiin ja alustamme Phi-3-mallin. Tämä vaihe sisältää mallipainojen lukemisen `gguf`-tiedostosta ja mallin valmistelun inferenssiä varten määritetyllä laitteella (tässä tapauksessa CPU).

## Vaihe 5: Käsittele kehotetta ja valmistele inferenssiä varten

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

Tässä vaiheessa tokenisoimme syötekehotteen ja valmistelemme sen inferenssiä varten muuntamalla sen token-ID -sekvenssiksi. Alustamme myös `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` -arvot. Jokainen token muunnetaan tensoriksi ja syötetään malliin logitsien saamiseksi.

Silmukka käsittelee jokaisen kehotteen tokenin, päivittää logits-prosessorin ja valmistelee seuraavan tokenin generointia varten.

## Vaihe 6: Inferenssi

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

Inferenssisilmukassa generoit tokenit yksi kerrallaan, kunnes saavutetaan haluttu näytteen pituus tai törmätään sekvenssin lopputokeniin. Seuraava token muunnetaan tensoriksi ja syötetään malliin, samalla kun logitit käsitellään rangaistusten ja näytteistyksen soveltamiseksi. Tämän jälkeen seuraava token valitaan, dekoodataan ja lisätään sekvenssiin.

Toistuvien tekstien välttämiseksi toistuville tokeneille sovelletaan rangaistusta `repeat_last_n` and `repeat_penalty`-parametrien mukaisesti.

Lopuksi generoitu teksti tulostetaan sitä mukaa kun se dekoodataan, mahdollistaen reaaliaikaisen suoratoiston.

## Vaihe 7: Suorita sovellus

Suorita sovellus ajamalla seuraava komento terminaalissa:

```bash
cargo run --release
```

Tämän pitäisi tulostaa haiku jääkiekosta, jonka Phi-3-malli on luonut. Jotain tällaista:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

tai

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Yhteenveto

Näitä vaiheita seuraamalla voimme suorittaa tekstin generoinnin Phi-3-mallilla Rustilla ja Candlella alle 100 rivillä koodia. Koodi hoitaa mallin lataamisen, tokenisoinnin ja inferenssin, hyödyntäen tensoreita ja logits-käsittelyä johdonmukaisen tekstin tuottamiseksi syötekehotteen perusteella.

Tämä konsolisovellus toimii Windowsissa, Linuxissa ja Mac OS:ssä. Rustin siirrettävyyden ansiosta koodi voidaan myös mukauttaa kirjastoksi, joka toimisi mobiilisovelluksissa (konsolisovelluksia ei voi kuitenkaan ajaa siellä).

## Liite: koko koodi

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

Huomautus: jos haluat suorittaa tämän koodin aarch64 Linuxilla tai aarch64 Windowsilla, lisää tiedosto nimeltä `.cargo/config`, jonka sisältö on seuraava:

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

> Voit vierailla virallisessa [Candle-esimerkkien](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) arkistossa saadaksesi lisää esimerkkejä Phi-3-mallin käytöstä Rustin ja Candlen kanssa, mukaan lukien vaihtoehtoisia lähestymistapoja inferenssiin.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.