# Platvormidevaheline järeldamine Rustiga

See juhend aitab meil läbi viia järeldamist, kasutades Rusti ja [Candle ML raamistikku](https://github.com/huggingface/candle) HuggingFace'ist. Rusti kasutamine järeldamiseks pakub mitmeid eeliseid, eriti võrreldes teiste programmeerimiskeeltega. Rust on tuntud oma kõrge jõudluse poolest, mis on võrreldav C ja C++-ga. See teeb sellest suurepärase valiku järeldamistöödeks, mis võivad olla arvutuslikult intensiivsed. Eelkõige on see tingitud nullkulu abstraktsioonidest ja tõhusast mäluhaldusest, millel puudub prügikogumise koormus. Rusti platvormidevahelised võimalused võimaldavad arendada koodi, mis töötab erinevatel operatsioonisüsteemidel, sealhulgas Windowsil, macOS-il ja Linuxil, samuti mobiilsetel operatsioonisüsteemidel, ilma et oleks vaja koodibaasi oluliselt muuta.

Selle juhendi järgimiseks on vajalik [Rust'i installimine](https://www.rust-lang.org/tools/install), mis sisaldab Rusti kompilaatorit ja pakihaldurit Cargo.

## Samm 1: Loo uus Rusti projekt

Uue Rusti projekti loomiseks käivita terminalis järgmine käsk:

```bash
cargo new phi-console-app
```

See genereerib algse projekti struktuuri koos `Cargo.toml` failiga ja `src` kataloogiga, mis sisaldab `main.rs` faili.

Järgmisena lisame oma sõltuvused - nimelt `candle`, `hf-hub` ja `tokenizers` teegid - `Cargo.toml` faili:

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

## Samm 2: Konfigureeri põhiparameetrid

`main.rs` failis seadistame algsed parameetrid järeldamiseks. Need kõik on lihtsuse huvides kõvakodeeritud, kuid neid saab vajadusel muuta.

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

- **temperature**: Kontrollib valimisprotsessi juhuslikkust.
- **sample_len**: Määrab genereeritud teksti maksimaalse pikkuse.
- **top_p**: Kasutatakse tuuma valimisel, et piirata iga sammu jaoks arvesse võetavate tokenite arvu.
- **repeat_last_n**: Kontrollib tokenite arvu, mida arvestatakse korduste vältimiseks karistuse rakendamisel.
- **repeat_penalty**: Karistusväärtus, mis takistab korduvate tokenite kasutamist.
- **seed**: Juhuslik seeme (võime kasutada konstantset väärtust parema reprodutseeritavuse jaoks).
- **prompt**: Algne sisendtekst, mille põhjal genereerimine algab. Pange tähele, et palume mudelil luua haiku jäähokist ja et me ümbritseme selle spetsiaalsete tokenitega, et näidata vestluse kasutaja ja assistendi osi. Mudel lõpetab seejärel sisendi haikuga.
- **device**: Kasutame arvutamiseks CPU-d. Candle toetab GPU kasutamist CUDA ja Metaliga.

## Samm 3: Laadi alla/valmista mudel ja tokeniseerija

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

Kasutame `hf_hub` API-d, et laadida mudeli ja tokeniseerija failid Hugging Face mudelihubist. `gguf` fail sisaldab kvantiseeritud mudeli kaalusid, samas kui `tokenizer.json` fail on mõeldud meie sisendteksti tokeniseerimiseks. Kui mudel on alla laaditud, salvestatakse see vahemällu, nii et esimene käivitamine on aeglane (kuna alla laaditakse 2,4 GB mudel), kuid järgnevad käivitamised on kiiremad.

## Samm 4: Laadi mudel

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Laadime kvantiseeritud mudeli kaalud mällu ja initsialiseerime Phi-3 mudeli. See samm hõlmab mudeli kaalude lugemist `gguf` failist ja mudeli seadistamist järeldamiseks määratud seadmel (antud juhul CPU).

## Samm 5: Töötle sisend ja valmista ette järeldamiseks

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

Selles etapis tokeniseerime sisendi ja valmistame selle ette järeldamiseks, muutes selle tokenite ID-de järjestuseks. Samuti initsialiseerime `LogitsProcessor`-i, et hallata valimisprotsessi (tõenäosusjaotus sõnavara üle) antud `temperature` ja `top_p` väärtuste põhjal. Iga token muudetakse tensoriks ja edastatakse mudelile, et saada logitid.

Tsükkel töötleb iga tokenit sisendis, uuendades logitide töötlejat ja valmistades ette järgmise tokeni genereerimist.

## Samm 6: Järeldamine

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

Järeldamise tsüklis genereerime tokenid ükshaaval, kuni jõuame soovitud näidise pikkuseni või kohtame järjestuse lõputokenit. Järgmine token muudetakse tensoriks ja edastatakse mudelile, samal ajal kui logitid töödeldakse karistuste ja valimise rakendamiseks. Seejärel valitakse järgmine token, dekodeeritakse ja lisatakse järjestusse.
Korduva teksti vältimiseks rakendatakse karistus korduvatele tokenitele, lähtudes `repeat_last_n` ja `repeat_penalty` parameetritest.

Lõpuks prinditakse genereeritud tekst dekodeerimise käigus, tagades voogesituse reaalajas väljundi.

## Samm 7: Rakenduse käivitamine

Rakenduse käivitamiseks käivita terminalis järgmine käsk:

```bash
cargo run --release
```

See peaks printima haiku jäähokist, mille genereerib Phi-3 mudel. Midagi sellist:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

või

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Kokkuvõte

Järgides neid samme, saame genereerida teksti Phi-3 mudeli abil Rusti ja Candle'iga vähem kui 100 koodirea jooksul. Kood hõlmab mudeli laadimist, tokeniseerimist ja järeldamist, kasutades tensoreid ja logitide töötlemist, et genereerida sidusat teksti sisendi põhjal.

See konsoolirakendus töötab Windowsil, Linuxil ja Mac OS-il. Rusti teisaldatavuse tõttu saab koodi kohandada ka teegiks, mis töötaks mobiilirakendustes (konsoolirakendusi seal ju käivitada ei saa).

## Lisa: täiskood

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

Märkus: selle koodi käitamiseks aarch64 Linuxil või aarch64 Windowsil lisa fail nimega `.cargo/config` järgmise sisuga:

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

> Külastage ametlikku [Candle näidete](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repositooriumi, et näha rohkem näiteid Phi-3 mudeli kasutamise kohta Rusti ja Candle'iga, sealhulgas alternatiivseid lähenemisi järeldamisele.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.