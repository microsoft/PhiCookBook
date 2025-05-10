<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:09:29+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "sr"
}
-->
# Cross-platform inference sa Rust-om

Ovaj tutorijal će nas voditi kroz proces izvođenja inferencije koristeći Rust i [Candle ML framework](https://github.com/huggingface/candle) iz HuggingFace-a. Korišćenje Rusta za inferenciju donosi nekoliko prednosti, naročito u poređenju sa drugim programskim jezicima. Rust je poznat po visokoj performansi, uporedivoj sa C i C++. Zbog toga je odličan izbor za zadatke inferencije koji mogu biti zahtevni za procesor. Posebno je to omogućeno nultim troškovima apstrakcija i efikasnim upravljanjem memorijom, bez dodatnog opterećenja usled garbage collection-a. Rust-ove mogućnosti za cross-platform razvoj omogućavaju kreiranje koda koji radi na različitim operativnim sistemima, uključujući Windows, macOS i Linux, kao i na mobilnim operativnim sistemima, bez značajnih izmena u kodu.

Preduslov za praćenje ovog tutorijala je da [instalirate Rust](https://www.rust-lang.org/tools/install), što uključuje Rust kompajler i Cargo, upravljač paketima za Rust.

## Korak 1: Kreiranje novog Rust projekta

Da biste kreirali novi Rust projekat, pokrenite sledeću komandu u terminalu:

```bash
cargo new phi-console-app
```

Ovo generiše početnu strukturu projekta sa fajlom `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Korak 2: Konfigurisanje osnovnih parametara

Unutar fajla main.rs, postavićemo početne parametre za našu inferenciju. Svi će biti hardkodirani radi jednostavnosti, ali ih možemo menjati po potrebi.

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

- **temperature**: Kontroliše stepen nasumičnosti u procesu uzorkovanja.
- **sample_len**: Određuje maksimalnu dužinu generisanog teksta.
- **top_p**: Koristi se za nucleus sampling da ograniči broj tokena koji se razmatraju u svakom koraku.
- **repeat_last_n**: Kontroliše broj tokena koji se razmatraju za primenu kazne kako bi se sprečile ponavljajuće sekvence.
- **repeat_penalty**: Vrednost kazne koja se primenjuje da bi se obeshrabrilo ponavljanje tokena.
- **seed**: Nasumični seed (možemo koristiti konstantnu vrednost za bolju reproduktivnost).
- **prompt**: Početni tekst za generisanje. Obratite pažnju da tražimo od modela da generiše haiku o hokeju na ledu, i da ga obavijamo specijalnim tokenima koji označavaju delove konverzacije korisnika i asistenta. Model će zatim dopuniti prompt haikuom.
- **device**: U ovom primeru koristimo CPU za računanje. Candle podržava i rad na GPU-u preko CUDA i Metal tehnologija.

## Korak 3: Preuzimanje/priprema modela i tokenizatora

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

Koristimo `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` fajl za tokenizaciju ulaznog teksta. Nakon što se model preuzme, kešira se, tako da će prvo pokretanje biti sporije (jer se preuzimaju 2.4GB modela), dok će naredna pokretanja biti brža.

## Korak 4: Učitavanje modela

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Učitavamo kvantizovane težine modela u memoriju i inicijalizujemo Phi-3 model. Ovaj korak podrazumeva čitanje težina iz `gguf` fajla i pripremu modela za inferenciju na zadatom uređaju (u ovom slučaju CPU).

## Korak 5: Obrada prompta i priprema za inferenciju

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

U ovom koraku tokenizujemo ulazni prompt i pripremamo ga za inferenciju tako što ga pretvaramo u niz ID-jeva tokena. Takođe inicijalizujemo vrednosti `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Svaki token se pretvara u tenzor i prosleđuje kroz model da bi se dobili logits.

Petlja obrađuje svaki token u promptu, ažurira logits procesor i priprema se za generisanje sledećeg tokena.

## Korak 6: Inferencija

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

U petlji za inferenciju generišemo tokene jedan po jedan dok ne dostignemo željenu dužinu ili ne naiđemo na token za kraj sekvence. Sledeći token se pretvara u tenzor i prosleđuje modelu, dok se logits procesiraju da bi se primenile kazne i uzorkovanje. Zatim se sledeći token uzorkuje, dekodira i dodaje u niz.
Da bismo izbegli ponavljajući tekst, primenjuje se kazna na ponovljene tokene bazirano na parametrima `repeat_last_n` and `repeat_penalty`.

Na kraju, generisani tekst se štampa u realnom vremenu kako se dekodira, omogućavajući streaming izlaz.

## Korak 7: Pokretanje aplikacije

Da biste pokrenuli aplikaciju, izvršite sledeću komandu u terminalu:

```bash
cargo run --release
```

Ovo bi trebalo da ispiše haiku o hokeju na ledu koji je generisao Phi-3 model. Nešto poput:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ili

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Zaključak

Prateći ove korake, možemo generisati tekst koristeći Phi-3 model sa Rust-om i Candle-om u manje od 100 linija koda. Kod pokriva učitavanje modela, tokenizaciju i inferenciju, koristeći tenzore i obradu logits-a za generisanje koherentnog teksta na osnovu ulaznog prompta.

Ova konzolna aplikacija može da radi na Windows, Linux i Mac OS sistemima. Zbog Rust-ove prenosivosti, kod se može prilagoditi i kao biblioteka koja bi radila unutar mobilnih aplikacija (jer konzolne aplikacije tamo ne možemo pokretati).

## Dodatak: ceo kod

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

Napomena: da biste pokrenuli ovaj kod na aarch64 Linux-u ili aarch64 Windows-u, dodajte fajl nazvan `.cargo/config` sa sledećim sadržajem:

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

> Za više primera kako koristiti Phi-3 model sa Rust-om i Candle-om, uključujući alternativne pristupe inferenciji, možete posetiti zvanični [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitorijum.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати употребом овог превода.