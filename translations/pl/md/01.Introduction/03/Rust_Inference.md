# Wnioskowanie wieloplatformowe z Rust

Ten samouczek przeprowadzi nas przez proces wykonywania wnioskowania za pomocą Rust i [frameworka Candle ML](https://github.com/huggingface/candle) od HuggingFace. Użycie Rust do wnioskowania niesie ze sobą kilka zalet, szczególnie w porównaniu z innymi językami programowania. Rust jest znany z wysokiej wydajności, porównywalnej do C i C++. To czyni go doskonałym wyborem do zadań wnioskowania, które mogą być obliczeniowo wymagające. Szczególnie ważne są tutaj abstrakcje bezkosztowe oraz efektywne zarządzanie pamięcią, bez narzutu garbage collectora. Wieloplatformowość Rust pozwala na tworzenie kodu działającego na różnych systemach operacyjnych, w tym Windows, macOS i Linux, a także na systemach mobilnych, bez konieczności znaczących zmian w kodzie.

Warunkiem koniecznym do śledzenia tego samouczka jest [zainstalowanie Rust](https://www.rust-lang.org/tools/install), które obejmuje kompilator Rust oraz Cargo, menedżera pakietów Rust.

## Krok 1: Utwórz nowy projekt Rust

Aby utworzyć nowy projekt Rust, uruchom następujące polecenie w terminalu:

```bash
cargo new phi-console-app
```

To wygeneruje początkową strukturę projektu z plikiem `Cargo.toml` oraz katalogiem `src` zawierającym plik `main.rs`.

Następnie dodamy nasze zależności - mianowicie crate'y `candle`, `hf-hub` oraz `tokenizers` - do pliku `Cargo.toml`:

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

## Krok 2: Skonfiguruj podstawowe parametry

W pliku main.rs ustawimy początkowe parametry dla naszego wnioskowania. Wszystkie będą na stałe wpisane dla uproszczenia, ale możemy je modyfikować według potrzeb.

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

- **temperature**: Kontroluje losowość procesu próbkowania.
- **sample_len**: Określa maksymalną długość generowanego tekstu.
- **top_p**: Używany w próbkowaniu jądrowym, ogranicza liczbę tokenów branych pod uwagę na każdym kroku.
- **repeat_last_n**: Kontroluje liczbę tokenów branych pod uwagę przy nakładaniu kary, aby zapobiec powtarzającym się sekwencjom.
- **repeat_penalty**: Wartość kary mająca zniechęcić do powtarzania tokenów.
- **seed**: Ziarno losowe (możemy użyć stałej wartości dla lepszej powtarzalności).
- **prompt**: Początkowy tekst zachęty do rozpoczęcia generowania. Zauważ, że prosimy model o wygenerowanie haiku o hokeju na lodzie, a tekst otaczamy specjalnymi tokenami, które wskazują części rozmowy użytkownika i asystenta. Model uzupełni prompt haiku.
- **device**: W tym przykładzie używamy CPU do obliczeń. Candle obsługuje także uruchamianie na GPU z CUDA i Metal.

## Krok 3: Pobierz/Przygotuj model i tokenizer

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

Używamy API `hf_hub` do pobrania plików modelu i tokenizera z repozytorium modeli Hugging Face. Plik `gguf` zawiera skwantowane wagi modelu, natomiast plik `tokenizer.json` służy do tokenizacji naszego tekstu wejściowego. Po pobraniu model jest buforowany, więc pierwsze uruchomienie będzie wolniejsze (ponieważ pobiera 2,4 GB modelu), ale kolejne będą szybsze.

## Krok 4: Załaduj model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Ładujemy skwantowane wagi modelu do pamięci i inicjalizujemy model Phi-3. Ten krok polega na odczytaniu wag modelu z pliku `gguf` i przygotowaniu modelu do wnioskowania na określonym urządzeniu (w tym przypadku CPU).

## Krok 5: Przetwórz prompt i przygotuj do wnioskowania

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

W tym kroku tokenizujemy tekst wejściowy i przygotowujemy go do wnioskowania, konwertując na sekwencję identyfikatorów tokenów. Inicjalizujemy także `LogitsProcessor`, który obsługuje proces próbkowania (rozkład prawdopodobieństwa na słowniku) na podstawie podanych wartości `temperature` i `top_p`. Każdy token jest konwertowany na tensor i przekazywany przez model, aby uzyskać logity.

Pętla przetwarza każdy token w prompt, aktualizując procesor logitów i przygotowując się do generowania kolejnego tokena.

## Krok 6: Wnioskowanie

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

W pętli wnioskowania generujemy tokeny jeden po drugim, aż osiągniemy żądaną długość próbki lub napotkamy token końca sekwencji. Następny token jest konwertowany na tensor i przekazywany przez model, a logity są przetwarzane w celu nałożenia kar i próbkowania. Następnie token jest próbkowany, dekodowany i dodawany do sekwencji.
Aby uniknąć powtarzającego się tekstu, nakładana jest kara na powtarzające się tokeny na podstawie parametrów `repeat_last_n` i `repeat_penalty`.

Na koniec generowany tekst jest drukowany na bieżąco, zapewniając strumieniowy, rzeczywisty output.

## Krok 7: Uruchom aplikację

Aby uruchomić aplikację, wykonaj następujące polecenie w terminalu:

```bash
cargo run --release
```

Powinno to wydrukować haiku o hokeju na lodzie wygenerowane przez model Phi-3. Coś w stylu:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

lub

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Podsumowanie

Postępując według tych kroków, możemy wykonać generowanie tekstu za pomocą modelu Phi-3 w Rust i Candle w mniej niż 100 linijkach kodu. Kod obsługuje ładowanie modelu, tokenizację i wnioskowanie, wykorzystując tensory i przetwarzanie logitów do generowania spójnego tekstu na podstawie podanego promptu.

Ta aplikacja konsolowa może działać na Windows, Linux i Mac OS. Dzięki przenośności Rust, kod można również zaadaptować do biblioteki działającej w aplikacjach mobilnych (w końcu nie możemy tam uruchamiać aplikacji konsolowych).

## Dodatek: pełny kod

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

Uwaga: aby uruchomić ten kod na aarch64 Linux lub aarch64 Windows, dodaj plik o nazwie `.cargo/config` z następującą zawartością:

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

> Możesz odwiedzić oficjalne repozytorium [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) po więcej przykładów użycia modelu Phi-3 z Rust i Candle, w tym alternatywne podejścia do wnioskowania.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.