<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:10:17+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "hr"
}
-->
# Cross-platform inference with Rust

Ovaj vodič će nas provesti kroz proces izvođenja inferencije koristeći Rust i [Candle ML framework](https://github.com/huggingface/candle) iz HuggingFacea. Korištenje Rusta za inferenciju donosi nekoliko prednosti, posebno u usporedbi s drugim programskim jezicima. Rust je poznat po svojoj visokoj performansi, usporedivoj s C i C++. To ga čini izvrsnim izborom za zadatke inferencije, koji mogu biti računalno zahtjevni. Posebno je to moguće zahvaljujući zero-cost apstrakcijama i efikasnom upravljanju memorijom, bez opterećenja garbage collectora. Rustove cross-platform mogućnosti omogućuju razvoj koda koji radi na različitim operativnim sustavima, uključujući Windows, macOS i Linux, kao i mobilne operativne sustave, bez značajnih promjena u kodnoj bazi.

Preduvjet za praćenje ovog vodiča je [instalacija Rust](https://www.rust-lang.org/tools/install), koja uključuje Rust kompajler i Cargo, Rustov upravitelj paketa.

## Step 1: Create a New Rust Project

Za kreiranje novog Rust projekta, pokrenite sljedeću naredbu u terminalu:

```bash
cargo new phi-console-app
```

Ovo generira početnu strukturu projekta s datotekom `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Step 2: Configure Basic Parameters

U datoteci main.rs postavit ćemo početne parametre za našu inferenciju. Svi će biti hardkodirani radi jednostavnosti, ali ih možemo mijenjati po potrebi.

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

- **temperature**: Kontrolira nasumičnost procesa uzorkovanja.
- **sample_len**: Određuje maksimalnu duljinu generiranog teksta.
- **top_p**: Koristi se za nucleus sampling kako bi se ograničio broj tokena koji se razmatraju u svakom koraku.
- **repeat_last_n**: Kontrolira broj tokena na koje se primjenjuje penalizacija kako bi se spriječilo ponavljanje.
- **repeat_penalty**: Vrijednost penalizacije za ponovljene tokene.
- **seed**: Nasumični seed (možemo koristiti konstantnu vrijednost za bolju reproducibilnost).
- **prompt**: Početni tekst za generiranje. Primijetite da tražimo od modela da generira haiku o hokeju na ledu, te da ga omotavamo posebnim tokenima kako bismo označili dijelove razgovora korisnika i asistenta. Model zatim dovršava prompt haikuom.
- **device**: U ovom primjeru koristimo CPU za izračune. Candle podržava i rad na GPU-u s CUDA i Metal.

## Step 3: Download/Prepare Model and Tokenizer

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

Koristimo `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` datoteku za tokenizaciju ulaznog teksta. Nakon što se model preuzme, on se kešira, pa će prvo pokretanje biti sporo (jer preuzima 2.4GB modela), dok će sljedeća pokretanja biti brža.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Učitavamo kvantizirane težine modela u memoriju i inicijaliziramo Phi-3 model. Ovaj korak uključuje čitanje težina iz `gguf` datoteke i pripremu modela za inferenciju na specificiranom uređaju (ovdje CPU).

## Step 5: Process Prompt and Prepare for Inference

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

U ovom koraku tokeniziramo ulazni prompt i pripremamo ga za inferenciju pretvaranjem u niz ID-eva tokena. Također inicijaliziramo `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` vrijednosti. Svaki token se pretvara u tensor i prosljeđuje modelu kako bi se dobili logits.

Petlja obrađuje svaki token u promptu, ažurira logits procesor i priprema se za generiranje sljedećeg tokena.

## Step 6: Inference

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

U petlji inferencije generiramo tokene jedan po jedan dok ne dođemo do željene duljine ili dok ne naiđemo na token kraja sekvence. Sljedeći token se pretvara u tensor i prolazi kroz model, dok se logits obrađuju kako bi se primijenile penalizacije i uzorkovanje. Zatim se sljedeći token uzorkuje, dekodira i dodaje u niz.
Kako bismo izbjegli ponavljajući tekst, primjenjuje se penalizacija na ponovljene tokene na temelju parametara `repeat_last_n` and `repeat_penalty`.

Na kraju, generirani tekst se ispisuje u realnom vremenu kako se dekodira, omogućujući streaming izlaz.

## Step 7: Run the Application

Za pokretanje aplikacije, izvršite sljedeću naredbu u terminalu:

```bash
cargo run --release
```

Ovo bi trebalo ispisati haiku o hokeju na ledu generiran od strane Phi-3 modela. Nešto poput:

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

## Conclusion

Slijedeći ove korake, možemo generirati tekst koristeći Phi-3 model s Rustom i Candleom u manje od 100 linija koda. Kod rukuje učitavanjem modela, tokenizacijom i inferencijom, koristeći tensore i obradu logits za generiranje koherentnog teksta na temelju ulaznog prompta.

Ova konzolna aplikacija može se pokretati na Windowsu, Linuxu i Mac OS-u. Zbog Rustove prenosivosti, kod se također može prilagoditi kao biblioteka koja bi se koristila unutar mobilnih aplikacija (jer konzolne aplikacije tamo ne možemo pokretati).

## Appendix: full code

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

Napomena: kako biste ovaj kod pokrenuli na aarch64 Linuxu ili aarch64 Windowsu, dodajte datoteku nazvanu `.cargo/config` s sljedećim sadržajem:

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

> Za više primjera korištenja Phi-3 modela s Rustom i Candleom, uključujući alternativne pristupe inferenciji, možete posjetiti službeni [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitorij.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.