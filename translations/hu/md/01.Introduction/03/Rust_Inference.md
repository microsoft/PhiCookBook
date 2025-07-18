<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:32:46+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "hu"
}
-->
# Többplatformos inferencia Rusttal

Ez a bemutató végigvezet minket az inferencia folyamatán Rust és a HuggingFace [Candle ML keretrendszer](https://github.com/huggingface/candle) használatával. A Rust használata az inferenciához több előnnyel jár, különösen más programozási nyelvekhez képest. A Rust híres a magas teljesítményéről, amely összehasonlítható a C és C++ nyelvekével. Ez kiváló választássá teszi az inferencia feladatokhoz, amelyek számításigényesek lehetnek. Különösen ennek alapja a nulla költségű absztrakciók és a hatékony memória-kezelés, amely nem igényel szemétgyűjtést. A Rust többplatformos képességei lehetővé teszik olyan kód fejlesztését, amely különböző operációs rendszereken fut, beleértve a Windowst, macOS-t és Linuxot, valamint mobil operációs rendszereket is, anélkül, hogy jelentős változtatásokat kellene végezni a kódbázison.

A bemutató követéséhez előfeltétel a [Rust telepítése](https://www.rust-lang.org/tools/install), amely tartalmazza a Rust fordítót és a Cargo csomagkezelőt.

## 1. lépés: Új Rust projekt létrehozása

Új Rust projekt létrehozásához futtassuk a következő parancsot a terminálban:

```bash
cargo new phi-console-app
```

Ez létrehoz egy kezdeti projektstruktúrát egy `Cargo.toml` fájllal és egy `src` könyvtárral, amely tartalmaz egy `main.rs` fájlt.

Ezután hozzáadjuk a függőségeinket – nevezetesen a `candle`, `hf-hub` és `tokenizers` crate-eket – a `Cargo.toml` fájlhoz:

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

## 2. lépés: Alapparaméterek beállítása

A main.rs fájlban beállítjuk az inferencia kezdeti paramétereit. Ezek egyszerűség kedvéért mind keménykódoltak lesznek, de szükség szerint módosíthatók.

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
- **top_p**: Nucleus mintavételhez használatos, korlátozza az egyes lépésekben figyelembe vett tokenek számát.
- **repeat_last_n**: Meghatározza, hány tokenre alkalmazzon büntetést az ismétlődések elkerülése érdekében.
- **repeat_penalty**: A büntetés értéke az ismétlődő tokenek visszaszorítására.
- **seed**: Véletlenszám-generátor mag (konstans érték is használható a jobb reprodukálhatóság érdekében).
- **prompt**: A generálás kezdeti szövege. Vegyük észre, hogy a modellt arra kérjük, hogy egy jégkorongról szóló haikut generáljon, és speciális tokenekkel jelöljük a felhasználó és az asszisztens részeit a beszélgetésben. A modell ezt követően befejezi a promptot egy haikuval.
- **device**: Ebben a példában a CPU-t használjuk a számításhoz. A Candle támogatja a futtatást GPU-n is CUDA és Metal segítségével.

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

Az `hf_hub` API-t használjuk a modell és a tokenizáló fájlok letöltésére a Hugging Face modell hubból. A `gguf` fájl tartalmazza a kvantált modell súlyokat, míg a `tokenizer.json` fájl a bemeneti szöveg tokenizálásához szükséges. A letöltés után a modell gyorsítótárazódik, így az első futtatás lassabb lesz (mivel letölti a 2,4 GB-os modellt), de a későbbi futtatások gyorsabbak lesznek.

## 4. lépés: Modell betöltése

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Betöltjük a kvantált modell súlyokat a memóriába, és inicializáljuk a Phi-3 modellt. Ez a lépés magában foglalja a modell súlyok beolvasását a `gguf` fájlból, és a modell előkészítését az inferenciára a megadott eszközön (jelen esetben CPU).

## 5. lépés: Prompt feldolgozása és előkészítés az inferenciához

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

Ebben a lépésben tokenizáljuk a bemeneti promptot, és előkészítjük az inferenciához úgy, hogy tokenazonosítók sorozatává alakítjuk. Inicializáljuk a `LogitsProcessor`-t is, amely kezeli a mintavételi folyamatot (valószínűségi eloszlás a szókészleten) a megadott `temperature` és `top_p` értékek alapján. Minden tokent tenzorrá alakítunk, és átvezetjük a modellen, hogy megkapjuk a logitokat.

A ciklus feldolgozza a prompt minden tokenjét, frissíti a logits processzort, és előkészíti a következő token generálását.

## 6. lépés: Inferencia

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

Az inferencia ciklusban tokeneket generálunk egyenként, amíg el nem érjük a kívánt mintahosszt vagy meg nem találjuk a szekvencia végét jelző tokent. A következő tokent tenzorrá alakítjuk, és átvezetjük a modellen, miközben a logitokat feldolgozzuk a büntetések és mintavétel alkalmazásához. Ezután a következő tokent mintavételezzük, dekódoljuk, és hozzáfűzzük a sorozathoz.
Az ismétlődő szöveg elkerülése érdekében büntetést alkalmazunk az ismétlődő tokenekre a `repeat_last_n` és `repeat_penalty` paraméterek alapján.

Végül a generált szöveget folyamatosan kiírjuk, biztosítva a valós idejű, folyamatos megjelenítést.

## 7. lépés: Az alkalmazás futtatása

Az alkalmazás futtatásához adjuk ki a következő parancsot a terminálban:

```bash
cargo run --release
```

Ez ki fog írni egy jégkorongról szóló haikut, amelyet a Phi-3 modell generált. Valami ilyesmit:

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

Ezeknek a lépéseknek a követésével kevesebb mint 100 sor kódban végezhetünk szöveggenerálást a Phi-3 modellel Rust és Candle segítségével. A kód kezeli a modell betöltését, tokenizálást és az inferenciát, kihasználva a tenzorokat és a logit feldolgozást, hogy koherens szöveget generáljon a bemeneti prompt alapján.

Ez a konzolos alkalmazás futtatható Windows, Linux és Mac OS rendszereken. A Rust hordozhatósága miatt a kód könnyen átalakítható olyan könyvtárrá, amely mobilalkalmazásokban is futtatható (hiszen konzolos alkalmazásokat ott nem futtathatunk).

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

Megjegyzés: a kód futtatásához aarch64 Linuxon vagy aarch64 Windowson adjunk hozzá egy `.cargo/config` nevű fájlt a következő tartalommal:

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

> További példákért a Phi-3 modell Rust és Candle használatára, beleértve alternatív inferencia megközelítéseket, látogassuk meg a hivatalos [Candle példák](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) tárolóját.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.