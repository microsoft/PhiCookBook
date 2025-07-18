<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:33:17+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "sk"
}
-->
# Inference naprieč platformami s Rustom

Tento tutoriál nás prevedie procesom vykonávania inference pomocou Rustu a [Candle ML frameworku](https://github.com/huggingface/candle) od HuggingFace. Použitie Rustu na inference prináša niekoľko výhod, najmä v porovnaní s inými programovacími jazykmi. Rust je známy svojím vysokým výkonom, porovnateľným s C a C++. To z neho robí vynikajúcu voľbu pre úlohy inference, ktoré môžu byť výpočtovo náročné. Najmä je to spôsobené zero-cost abstrakciami a efektívnym manažmentom pamäte, ktorý nevyžaduje garbage collection. Rustove multiplatformové schopnosti umožňujú vývoj kódu, ktorý beží na rôznych operačných systémoch, vrátane Windows, macOS a Linux, ako aj na mobilných operačných systémoch, bez výrazných zmien v kóde.

Predpokladom na sledovanie tohto tutoriálu je [inštalácia Rustu](https://www.rust-lang.org/tools/install), ktorá zahŕňa Rust kompilátor a Cargo, správcu balíčkov pre Rust.

## Krok 1: Vytvorenie nového Rust projektu

Na vytvorenie nového Rust projektu spustite v termináli nasledujúci príkaz:

```bash
cargo new phi-console-app
```

Tým sa vygeneruje počiatočná štruktúra projektu s `Cargo.toml` súborom a adresárom `src`, ktorý obsahuje súbor `main.rs`.

Ďalej pridáme naše závislosti - konkrétne crates `candle`, `hf-hub` a `tokenizers` - do súboru `Cargo.toml`:

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

## Krok 2: Nastavenie základných parametrov

V súbore main.rs nastavíme počiatočné parametre pre našu inferenciu. Všetky budú pre jednoduchosť pevne zakódované, ale môžeme ich podľa potreby upraviť.

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

- **temperature**: Riadi náhodnosť procesu vzorkovania.
- **sample_len**: Určuje maximálnu dĺžku generovaného textu.
- **top_p**: Používa sa pre nucleus sampling na obmedzenie počtu tokenov zvažovaných v každom kroku.
- **repeat_last_n**: Určuje počet tokenov, ktoré sa berú do úvahy pri uplatňovaní penalizácie na zabránenie opakovaniu sekvencií.
- **repeat_penalty**: Hodnota penalizácie na odrádzanie od opakovaných tokenov.
- **seed**: Náhodné semeno (môžeme použiť konštantnú hodnotu pre lepšiu reprodukovateľnosť).
- **prompt**: Počiatočný text promptu na začatie generovania. Všimnite si, že žiadame model, aby vygeneroval haiku o ľadovom hokeji, a že ho obalíme špeciálnymi tokenmi na označenie častí konverzácie používateľa a asistenta. Model potom doplní prompt haiku.
- **device**: V tomto príklade používame CPU na výpočty. Candle podporuje aj beh na GPU s CUDA a Metal.

## Krok 3: Stiahnutie/príprava modelu a tokenizéra

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

Používame API `hf_hub` na stiahnutie súborov modelu a tokenizéra z Hugging Face model hubu. Súbor `gguf` obsahuje kvantizované váhy modelu, zatiaľ čo súbor `tokenizer.json` sa používa na tokenizáciu vstupného textu. Po stiahnutí je model uložený v cache, takže prvé spustenie bude pomalšie (keďže sa sťahuje 2,4 GB modelu), ale následné spustenia budú rýchlejšie.

## Krok 4: Načítanie modelu

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Načítame kvantizované váhy modelu do pamäte a inicializujeme model Phi-3. Tento krok zahŕňa čítanie váh modelu zo súboru `gguf` a nastavenie modelu na inferenciu na zvolenom zariadení (v tomto prípade CPU).

## Krok 5: Spracovanie promptu a príprava na inferenciu

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

V tomto kroku tokenizujeme vstupný prompt a pripravíme ho na inferenciu konverziou na sekvenciu ID tokenov. Tiež inicializujeme `LogitsProcessor`, ktorý spracováva sampling (pravdepodobnostné rozdelenie nad slovníkom) na základe zadaných hodnôt `temperature` a `top_p`. Každý token sa konvertuje na tensor a prejde modelom, aby sme získali logits.

Slučka spracováva každý token v prompte, aktualizuje logits processor a pripravuje sa na generovanie ďalšieho tokenu.

## Krok 6: Inferencia

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

V inferenčnej slučke generujeme tokeny jeden po druhom, až kým nedosiahneme požadovanú dĺžku vzorky alebo nenarazíme na token konca sekvencie. Nasledujúci token sa konvertuje na tensor a prejde modelom, pričom logits sa spracujú na aplikovanie penalizácií a vzorkovania. Potom sa ďalší token vyberie, dekóduje a pridá do sekvencie.
Aby sme predišli opakovaniu textu, aplikuje sa penalizácia na opakované tokeny na základe parametrov `repeat_last_n` a `repeat_penalty`.

Nakoniec sa generovaný text vypisuje počas dekódovania, čím sa zabezpečí výstup v reálnom čase.

## Krok 7: Spustenie aplikácie

Na spustenie aplikácie vykonajte v termináli nasledujúci príkaz:

```bash
cargo run --release
```

Malo by sa vytlačiť haiku o ľadovom hokeji vygenerované modelom Phi-3. Niečo ako:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

alebo

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Záver

Dodržiavaním týchto krokov môžeme vykonať generovanie textu pomocou modelu Phi-3 s Rustom a Candle v menej než 100 riadkoch kódu. Kód sa stará o načítanie modelu, tokenizáciu a inferenciu, využívajúc tensory a spracovanie logits na generovanie zrozumiteľného textu na základe vstupného promptu.

Táto konzolová aplikácia môže bežať na Windows, Linux a Mac OS. Vďaka prenosnosti Rustu môže byť kód tiež upravený na knižnicu, ktorá by bežala v mobilných aplikáciách (konzolové aplikácie tam predsa len nemôžeme spustiť).

## Príloha: kompletný kód

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

Poznámka: aby ste mohli tento kód spustiť na aarch64 Linux alebo aarch64 Windows, pridajte súbor s názvom `.cargo/config` s nasledujúcim obsahom:

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

> Pre viac príkladov, ako používať model Phi-3 s Rustom a Candle vrátane alternatívnych prístupov k inferencii, môžete navštíviť oficiálne [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitár.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.