# Kryžminė platformų inferencija su Rust

Šiame vadove sužinosime, kaip atlikti inferenciją naudojant Rust ir [Candle ML framework](https://github.com/huggingface/candle) iš HuggingFace. Rust naudojimas inferencijai suteikia keletą privalumų, ypač lyginant su kitomis programavimo kalbomis. Rust garsėja savo aukštu našumu, kuris yra panašus į C ir C++. Tai daro jį puikiu pasirinkimu inferencijos užduotims, kurios gali būti skaičiavimo intensyvios. Ypač tai pasiekiama dėl nulinių kaštų abstrakcijų ir efektyvaus atminties valdymo, kuris neturi šiukšlių surinkimo našumo sąnaudų. Rust kryžminės platformos galimybės leidžia kurti kodą, kuris veikia įvairiose operacinėse sistemose, įskaitant Windows, macOS ir Linux, taip pat mobiliose operacinėse sistemose, be reikšmingų kodo pakeitimų.

Norint sekti šį vadovą, būtina [įdiegti Rust](https://www.rust-lang.org/tools/install), kuris apima Rust kompiliatorių ir Cargo, Rust paketų valdymo įrankį.

## 1 žingsnis: Sukurkite naują Rust projektą

Norėdami sukurti naują Rust projektą, terminale paleiskite šią komandą:

```bash
cargo new phi-console-app
```

Tai sugeneruos pradinę projekto struktūrą su `Cargo.toml` failu ir `src` direktorija, kurioje yra `main.rs` failas.

Toliau pridėsime priklausomybes - būtent `candle`, `hf-hub` ir `tokenizers` bibliotekas - į `Cargo.toml` failą:

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

## 2 žingsnis: Konfigūruokite pagrindinius parametrus

Failo `main.rs` viduje nustatysime pradinius parametrus inferencijai. Jie bus užkoduoti paprastumo dėlei, tačiau prireikus galime juos pakeisti.

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

- **temperature**: Valdo atsitiktinumą generavimo procese.
- **sample_len**: Nurodo maksimalų generuojamo teksto ilgį.
- **top_p**: Naudojamas branduolio atrankai, kad apribotų kiekviename žingsnyje svarstomų žodžių skaičių.
- **repeat_last_n**: Valdo žodžių skaičių, kurie svarstomi taikant baudos mechanizmą, kad būtų išvengta pasikartojimų.
- **repeat_penalty**: Baudos vertė, skirta atgrasyti nuo pasikartojančių žodžių.
- **seed**: Atsitiktinis sėklos skaičius (galime naudoti pastovią vertę geresniam atkuriamumui).
- **prompt**: Pradinis tekstas, skirtas generavimui pradėti. Atkreipkite dėmesį, kad prašome modelio sukurti haiku apie ledo ritulį ir apgaubiame jį specialiais ženklais, kad nurodytume vartotojo ir asistento pokalbio dalis. Modelis užbaigs šį tekstą haiku.
- **device**: Šiame pavyzdyje naudojame CPU skaičiavimams. Candle palaiko vykdymą GPU su CUDA ir Metal.

## 3 žingsnis: Atsisiųskite/Pasiruoškite modelį ir tokenizatorių

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

Naudojame `hf_hub` API, kad atsisiųstume modelio ir tokenizatoriaus failus iš Hugging Face modelių centro. `gguf` failas turi kvantizuotus modelio svorius, o `tokenizer.json` failas naudojamas mūsų įvesties teksto tokenizavimui. Kai failai atsisiunčiami, modelis yra talpinamas, todėl pirmasis vykdymas bus lėtas (nes atsisiunčiami 2.4GB modelio duomenys), tačiau vėlesni vykdymai bus greitesni.

## 4 žingsnis: Įkelkite modelį

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Įkeliame kvantizuotus modelio svorius į atmintį ir inicializuojame Phi-3 modelį. Šis žingsnis apima modelio svorių skaitymą iš `gguf` failo ir modelio paruošimą inferencijai nurodytame įrenginyje (šiuo atveju CPU).

## 5 žingsnis: Apdorokite pradinį tekstą ir pasiruoškite inferencijai

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

Šiame žingsnyje tokenizuojame įvesties tekstą ir paruošiame jį inferencijai, konvertuodami jį į žodžių ID seką. Taip pat inicializuojame `LogitsProcessor`, kuris tvarko atrankos procesą (tikimybių pasiskirstymą per žodyną) pagal nurodytas `temperature` ir `top_p` reikšmes. Kiekvienas žodis konvertuojamas į tensorą ir perduodamas per modelį, kad gautume logitus.

Ciklas apdoroja kiekvieną tekstą žodį, atnaujina logitų procesorių ir ruošiasi kitam žodžio generavimui.

## 6 žingsnis: Inferencija

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

Inferencijos cikle generuojame žodžius po vieną, kol pasiekiame norimą teksto ilgį arba susiduriame su sekos pabaigos žodžiu. Kitas žodis konvertuojamas į tensorą ir perduodamas per modelį, o logitai apdorojami, kad būtų taikomos baudos ir atranka. Tada kitas žodis yra atrenkamas, dekoduojamas ir pridedamas prie sekos.
Kad išvengtume pasikartojančio teksto, bauda taikoma pasikartojantiems žodžiams pagal `repeat_last_n` ir `repeat_penalty` parametrus.

Galiausiai generuojamas tekstas spausdinamas, kai jis dekoduojamas, užtikrinant realaus laiko srautą.

## 7 žingsnis: Paleiskite programą

Norėdami paleisti programą, terminale vykdykite šią komandą:

```bash
cargo run --release
```

Tai turėtų atspausdinti haiku apie ledo ritulį, sukurtą Phi-3 modelio. Pavyzdžiui:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

arba

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Išvada

Sekdami šiuos žingsnius, galime generuoti tekstą naudodami Phi-3 modelį su Rust ir Candle mažiau nei 100 eilučių kodo. Kodas apima modelio įkėlimą, tokenizaciją ir inferenciją, pasinaudodamas tensorais ir logitų apdorojimu, kad generuotų nuoseklų tekstą pagal įvesties tekstą.

Ši konsolės programa gali veikti Windows, Linux ir Mac OS. Dėl Rust portabilumo kodas taip pat gali būti pritaikytas bibliotekai, kuri veiktų mobiliose programose (konsolės programų ten paleisti negalime).

## Priedas: visas kodas

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

Pastaba: norint paleisti šį kodą aarch64 Linux arba aarch64 Windows, pridėkite failą pavadinimu `.cargo/config` su šiuo turiniu:

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

> Galite apsilankyti oficialiame [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitorijoje, kur rasite daugiau pavyzdžių, kaip naudoti Phi-3 modelį su Rust ir Candle, įskaitant alternatyvius inferencijos metodus.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.