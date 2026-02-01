# Inference napříč platformami s Rustem

Tento tutoriál nás provede procesem inference pomocí Rustu a [Candle ML frameworku](https://github.com/huggingface/candle) od HuggingFace. Použití Rustu pro inference přináší několik výhod, zejména ve srovnání s jinými programovacími jazyky. Rust je známý svou vysokou výkonností, srovnatelnou s C a C++. Díky tomu je skvělou volbou pro úlohy inference, které mohou být výpočetně náročné. Hlavními faktory jsou zero-cost abstrakce a efektivní správa paměti bez režie garbage collectoru. Rust také umožňuje psát kód, který běží na různých operačních systémech, včetně Windows, macOS a Linuxu, stejně jako na mobilních platformách, aniž by bylo potřeba výrazně měnit zdrojový kód.

Předpokladem pro sledování tohoto tutoriálu je [instalace Rustu](https://www.rust-lang.org/tools/install), která zahrnuje Rust kompilátor a Cargo, správce balíčků pro Rust.

## Krok 1: Vytvoření nového Rust projektu

Pro vytvoření nového Rust projektu spusťte v terminálu následující příkaz:

```bash
cargo new phi-console-app
```

Tím se vygeneruje počáteční struktura projektu s `Cargo.toml` souborem a složkou `src`, která obsahuje soubor `main.rs`.

Dále přidáme naše závislosti – konkrétně crate `candle`, `hf-hub` a `tokenizers` – do souboru `Cargo.toml`:

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

## Krok 2: Nastavení základních parametrů

V souboru main.rs nastavíme počáteční parametry pro naši inferenci. Pro jednoduchost je všechny nastavíme přímo v kódu, ale můžeme je podle potřeby upravit.

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

- **temperature**: Řídí náhodnost procesu vzorkování.
- **sample_len**: Udává maximální délku generovaného textu.
- **top_p**: Používá se pro nucleus sampling, omezuje počet tokenů zvažovaných v každém kroku.
- **repeat_last_n**: Určuje počet tokenů, které se berou v úvahu při uplatňování penalizace za opakování.
- **repeat_penalty**: Hodnota penalizace, která snižuje pravděpodobnost opakovaných tokenů.
- **seed**: Náhodné semínko (můžeme použít konstantní hodnotu pro lepší reprodukovatelnost).
- **prompt**: Počáteční textový prompt pro spuštění generování. Všimněte si, že žádáme model o vytvoření haiku o ledním hokeji a prompt je obalen speciálními tokeny, které označují části konverzace uživatele a asistenta. Model pak prompt doplní haiku.
- **device**: V tomto příkladu používáme CPU pro výpočty. Candle podporuje také běh na GPU s CUDA a Metal.

## Krok 3: Stažení/Příprava modelu a tokenizeru

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

Používáme API `hf_hub` ke stažení modelu a tokenizeru z Hugging Face model hubu. Soubor `gguf` obsahuje kvantizované váhy modelu, zatímco `tokenizer.json` slouží k tokenizaci vstupního textu. Po stažení je model uložen do cache, takže první spuštění bude pomalejší (kvůli stažení 2,4 GB modelu), ale další běhy už budou rychlejší.

## Krok 4: Načtení modelu

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Načteme kvantizované váhy modelu do paměti a inicializujeme model Phi-3. Tento krok zahrnuje čtení vah z `gguf` souboru a přípravu modelu pro inferenci na zvoleném zařízení (v tomto případě CPU).

## Krok 5: Zpracování promptu a příprava na inferenci

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

V tomto kroku tokenizujeme vstupní prompt a připravíme ho pro inferenci převedením na sekvenci ID tokenů. Také inicializujeme `LogitsProcessor`, který bude řídit proces vzorkování (pravděpodobnostní rozdělení přes slovník) na základě nastavených hodnot `temperature` a `top_p`. Každý token je převeden na tensor a předán modelu pro získání logits.

Smyčka zpracovává každý token v promptu, aktualizuje logits processor a připravuje se na generování dalšího tokenu.

## Krok 6: Inference

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

V inferenční smyčce generujeme tokeny jeden po druhém, dokud nedosáhneme požadované délky nebo nenarazíme na token konce sekvence. Další token je převeden na tensor a předán modelu, logits jsou zpracovány s aplikací penalizací a vzorkování. Poté je token vybrán, dekódován a přidán do sekvence.
Abychom předešli opakujícím se textům, aplikuje se penalizace na opakované tokeny podle parametrů `repeat_last_n` a `repeat_penalty`.

Nakonec je generovaný text průběžně vytištěn, což zajišťuje výstup v reálném čase.

## Krok 7: Spuštění aplikace

Pro spuštění aplikace zadejte v terminálu následující příkaz:

```bash
cargo run --release
```

Mělo by se zobrazit haiku o ledním hokeji vygenerované modelem Phi-3. Něco jako:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

nebo

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Závěr

Díky těmto krokům můžeme generovat text pomocí modelu Phi-3 v Rustu a Candle v méně než 100 řádcích kódu. Kód se stará o načtení modelu, tokenizaci a inferenci, využívá tensory a zpracování logits k vytvoření koherentního textu na základě vstupního promptu.

Tato konzolová aplikace může běžet na Windows, Linuxu i Mac OS. Díky přenositelnosti Rustu lze kód také upravit na knihovnu, která poběží v mobilních aplikacích (koneckonců tam konzolové aplikace spustit nelze).

## Příloha: kompletní kód

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

Poznámka: pro spuštění tohoto kódu na aarch64 Linuxu nebo aarch64 Windows přidejte soubor `.cargo/config` s následujícím obsahem:

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

> Pro více příkladů, jak používat model Phi-3 s Rustem a Candle, včetně alternativních přístupů k inferenci, můžete navštívit oficiální repozitář [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.