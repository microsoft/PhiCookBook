<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:05:53+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "hu"
}
-->
# Cross-platform következtetés Rust nyelven

Ez a bemutató végigvezet minket a Rust és a HuggingFace [Candle ML keretrendszerének](https://github.com/huggingface/candle) használatán a következtetés végrehajtásához. A Rust használata a következtetéshez több előnnyel jár, különösen más programozási nyelvekhez képest. A Rust híres a kiemelkedő teljesítményéről, amely összevethető a C és C++ nyelvekével. Ez kiváló választássá teszi a következtetési feladatokhoz, amelyek számításigényesek lehetnek. Különösen a nulla költségű absztrakciók és a hatékony memóriakezelés járul hozzá ehhez, hiszen nincs szemétgyűjtési overhead. A Rust platformok közötti képességei lehetővé teszik olyan kód fejlesztését, amely különböző operációs rendszereken fut, beleértve a Windowst, macOS-t és Linuxot, valamint mobil operációs rendszereket, anélkül, hogy jelentős változtatásokat kellene eszközölni a kódbázison.

A bemutató követéséhez előfeltétel a [Rust telepítése](https://www.rust-lang.org/tools/install), amely tartalmazza a Rust fordítót és a Cargo csomagkezelőt.

## 1. lépés: Új Rust projekt létrehozása

Új Rust projekt létrehozásához futtasd a következő parancsot a terminálban:

```bash
cargo new phi-console-app
```

Ez létrehoz egy alap projekt struktúrát egy `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` fájllal:

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

## 2. lépés: Alapvető paraméterek beállítása

A main.rs fájlban beállítjuk a következtetés kezdeti paramétereit. Ezek egyszerűség kedvéért mind keménykódoltak lesznek, de szükség szerint módosíthatók.

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

- **temperature**: Szabályozza a mintavétel véletlenszerűségét.
- **sample_len**: Meghatározza a generált szöveg maximális hosszát.
- **top_p**: Nucleus mintavételhez használatos, korlátozza az egy lépésben figyelembe vett tokenek számát.
- **repeat_last_n**: Meghatározza, hány token figyelhető meg az ismétlődések büntetéséhez.
- **repeat_penalty**: Az ismétlődő tokenek visszatartására szolgáló büntetési érték.
- **seed**: Véletlenszerű mag (konstans érték is használható a jobb reprodukálhatóság érdekében).
- **prompt**: A generálás kezdeti promptja. Észrevehető, hogy a modellt arra kérjük, hogy egy jégkorongról szóló haikut generáljon, és különleges tokenekkel jelöljük a felhasználó és az asszisztens beszélgetési részeit. A modell ezután kiegészíti a promptot a haikuval.
- **device**: Ebben a példában a CPU-t használjuk a számításhoz. A Candle támogatja a GPU-s futtatást CUDA és Metal segítségével is.

## 3. lépés: Modell és tokenizáló letöltése/előkészítése

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

A `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` fájlt használjuk a bemeneti szöveg tokenizálásához. A modell letöltése után az gyorsítótárba kerül, így az első futtatás lassabb lesz (mivel letölti a 2,4 GB-os modellt), de a további futtatások gyorsabbak lesznek.

## 4. lépés: Modell betöltése

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Betöltjük a kvantált modell súlyokat a memóriába, és inicializáljuk a Phi-3 modellt. Ez a lépés magában foglalja a modell súlyok beolvasását a `gguf` fájlból, és a modell előkészítését a megadott eszközön (jelen esetben CPU) történő következtetéshez.

## 5. lépés: Prompt feldolgozása és előkészítés a következtetéshez

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

Ebben a lépésben tokenizáljuk a bemeneti promptot, és előkészítjük a következtetéshez úgy, hogy tokenazonosítók sorozatává alakítjuk. Inicializáljuk továbbá a `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` értékeket. Minden token egy tenzorrá alakul, és a modellen keresztül fut, hogy megkapjuk a logitokat.

A ciklus feldolgozza a prompt minden tokenjét, frissíti a logit processzort, és előkészíti a következő token generálását.

## 6. lépés: Következtetés

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

A következtetési ciklusban tokeneket generálunk egyenként, amíg el nem érjük a kívánt mintahosszt vagy meg nem találjuk a szekvencia végét jelző tokent. A következő token tenzorrá alakul, és átmegy a modellen, miközben a logitokat feldolgozzuk, hogy büntetéseket és mintavételt alkalmazzunk. Ezután a következő tokent kiválasztjuk, dekódoljuk, és hozzáfűzzük a szekvenciához.  
Az ismétlődő szöveg elkerülése érdekében büntetést alkalmazunk az ismétlődő tokenekre a `repeat_last_n` and `repeat_penalty` paraméterek alapján.

Végül a generált szöveg folyamatosan kiírásra kerül, így valós idejű streamelt outputot kapunk.

## 7. lépés: Az alkalmazás futtatása

Az alkalmazás futtatásához írd be a következő parancsot a terminálba:

```bash
cargo run --release
```

Ennek egy jégkorongról szóló haikut kell kiírnia, amit a Phi-3 modell generált. Valami ilyesmit:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

vagy

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Összegzés

Ezeknek a lépéseknek a követésével szöveg generálást végezhetünk a Phi-3 modellel Rust és Candle segítségével kevesebb, mint 100 sor kódban. A kód kezeli a modell betöltését, tokenizálást és a következtetést, kihasználva a tenzorokat és a logit feldolgozást, hogy koherens szöveget generáljon a bemeneti prompt alapján.

Ez a konzolos alkalmazás Windows, Linux és Mac OS rendszereken futtatható. A Rust hordozhatóságának köszönhetően a kód könnyen adaptálható olyan könyvtárrá, amely mobil alkalmazásokban is futtatható (hiszen konzolos alkalmazásokat ott nem futtathatunk).

## Függelék: teljes kód

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

Megjegyzés: ahhoz, hogy ezt a kódot aarch64 Linuxon vagy aarch64 Windowson futtasd, adj hozzá egy `.cargo/config` nevű fájlt a következő tartalommal:

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

> További példákért a Phi-3 modell Rust és Candle használatára, beleértve alternatív következtetési módszereket, látogass el a hivatalos [Candle példák](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) tárházába.

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.