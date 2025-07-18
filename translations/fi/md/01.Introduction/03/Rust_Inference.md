<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:30:53+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "fi"
}
-->
# Ristiinalustainen päättely Rustilla

Tämä opas ohjaa meitä suorittamaan päättelyn Rustilla ja HuggingFacen [Candle ML -kehikolla](https://github.com/huggingface/candle). Rustin käyttäminen päättelyssä tarjoaa useita etuja, erityisesti verrattuna muihin ohjelmointikieliin. Rust tunnetaan korkeasta suorituskyvystään, joka on verrattavissa C:n ja C++:n tasoon. Tämä tekee siitä erinomaisen valinnan päättelytehtäviin, jotka voivat olla laskennallisesti vaativia. Erityisesti tämä perustuu nollakustannuksellisiin abstraktioihin ja tehokkaaseen muistinhallintaan, jossa ei ole roskienkeruusta aiheutuvaa ylikuormitusta. Rustin ristiinalustaiset ominaisuudet mahdollistavat koodin kehittämisen, joka toimii eri käyttöjärjestelmissä, kuten Windowsissa, macOS:ssä ja Linuxissa, sekä mobiilikäyttöjärjestelmissä ilman merkittäviä muutoksia koodipohjaan.

Tämän oppaan seuraamisen edellytys on [Rustin asentaminen](https://www.rust-lang.org/tools/install), joka sisältää Rust-kääntäjän ja Cargo-pakettienhallinnan.

## Vaihe 1: Luo uusi Rust-projekti

Luo uusi Rust-projekti suorittamalla seuraava komento terminaalissa:

```bash
cargo new phi-console-app
```

Tämä luo alkuperäisen projektirakenteen, jossa on `Cargo.toml`-tiedosto ja `src`-hakemisto, joka sisältää `main.rs`-tiedoston.

Seuraavaksi lisäämme riippuvuudet — nimittäin `candle`, `hf-hub` ja `tokenizers` -kirjastot — `Cargo.toml`-tiedostoon:

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

`main.rs`-tiedostossa asetamme päättelyn alkuparametrit. Ne kovakoodataan yksinkertaisuuden vuoksi, mutta niitä voi muokata tarpeen mukaan.

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

- **temperature**: Ohjaa satunnaisuuden määrää näytteistysprosessissa.
- **sample_len**: Määrittää luodun tekstin maksimipituuden.
- **top_p**: Käytetään ydinotannassa rajoittamaan kunkin askeleen tokenien määrää.
- **repeat_last_n**: Määrittää tokenien määrän, joita käytetään rangaistuksen soveltamiseen toistuvien sekvenssien estämiseksi.
- **repeat_penalty**: Rangaistusarvo toistuvien tokenien vähentämiseksi.
- **seed**: Satunnaissiementä (voisimme käyttää vakioarvoa paremman toistettavuuden vuoksi).
- **prompt**: Alkuperäinen kehoteteksti generaation aloittamiseksi. Huomaa, että pyydämme mallia luomaan haikun jääkiekosta, ja ympäröimme sen erityisillä tokeneilla osoittaaksemme käyttäjän ja avustajan osat keskustelussa. Malli täydentää sitten kehotteen haikulla.
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

Käytämme `hf_hub`-API:a ladataksemme mallin ja tokenisoijan tiedostot Hugging Facen mallivarastosta. `gguf`-tiedosto sisältää kvantisoidut mallipainot, kun taas `tokenizer.json`-tiedostoa käytetään syötteen tokenisointiin. Kun malli on ladattu, se välimuistitetaan, joten ensimmäinen suoritus on hidas (koska malli, jonka koko on 2,4 Gt, ladataan), mutta seuraavat suoritukset ovat nopeampia.

## Vaihe 4: Lataa malli

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Lataamme kvantisoidut mallipainot muistiin ja alustamme Phi-3-mallin. Tämä vaihe sisältää mallipainojen lukemisen `gguf`-tiedostosta ja mallin valmistelun päättelyä varten määritetyllä laitteella (tässä tapauksessa CPU).

## Vaihe 5: Käsittele kehotetta ja valmistaudu päättelyyn

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

Tässä vaiheessa tokenisoimme syötekehotteen ja valmistelemme sen päättelyä varten muuntamalla sen token-ID-jonoksi. Alustamme myös `LogitsProcessor`-olion hallitsemaan näytteistysprosessia (todennäköisyysjakauma sanastosta) annettujen `temperature`- ja `top_p`-arvojen perusteella. Jokainen token muunnetaan tensoriin ja syötetään mallin läpi saadakseen logits-arvot.

Silmukka käsittelee jokaisen kehotteen tokenin, päivittää logits-prosessorin ja valmistelee seuraavan tokenin generointia varten.

## Vaihe 6: Päättely

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

Päättelysilmukassa generoimme tokeneita yksi kerrallaan, kunnes saavutamme halutun näytteen pituuden tai törmäämme loppusekvenssitokeniin. Seuraava token muunnetaan tensoriin ja syötetään mallin läpi, samalla kun logits-arvoja käsitellään rangaistusten ja näytteistyksen soveltamiseksi. Tämän jälkeen seuraava token valitaan, dekoodataan ja lisätään sekvenssiin.
Toistuvan tekstin välttämiseksi toistuville tokeneille sovelletaan rangaistusta `repeat_last_n`- ja `repeat_penalty`-parametrien perusteella.

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

Noudattamalla näitä vaiheita voimme suorittaa tekstin generoinnin Phi-3-mallilla Rustilla ja Candlella alle 100 rivillä koodia. Koodi hoitaa mallin lataamisen, tokenisoinnin ja päättelyn hyödyntäen tensoreita ja logits-käsittelyä tuottaakseen johdonmukaista tekstiä syötekehotteen perusteella.

Tämä konsolisovellus toimii Windowsissa, Linuxissa ja Mac OS:ssä. Rustin siirrettävyyden ansiosta koodi voidaan myös mukauttaa kirjastoksi, joka toimisi mobiilisovelluksissa (konsolisovelluksia ei siellä kuitenkaan voi ajaa).

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

Huomautus: jotta tämä koodi toimii aarch64 Linuxissa tai aarch64 Windowsissa, lisää tiedosto nimeltä `.cargo/config`, jonka sisältö on seuraava:

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

> Voit vierailla virallisessa [Candle-esimerkit](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) -varastossa saadaksesi lisää esimerkkejä Phi-3-mallin käytöstä Rustin ja Candlen kanssa, mukaan lukien vaihtoehtoisia lähestymistapoja päättelyyn.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.