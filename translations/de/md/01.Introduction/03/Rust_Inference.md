# Plattformübergreifende Inferenz mit Rust

Dieses Tutorial führt uns durch den Prozess der Inferenz mit Rust und dem [Candle ML Framework](https://github.com/huggingface/candle) von HuggingFace. Die Verwendung von Rust für Inferenz bietet mehrere Vorteile, insbesondere im Vergleich zu anderen Programmiersprachen. Rust ist bekannt für seine hohe Leistung, vergleichbar mit der von C und C++. Das macht es zu einer ausgezeichneten Wahl für Inferenzaufgaben, die oft rechenintensiv sind. Besonders hervorzuheben sind die zero-cost Abstraktionen und das effiziente Speichermanagement ohne Garbage Collection. Die plattformübergreifenden Fähigkeiten von Rust ermöglichen die Entwicklung von Code, der auf verschiedenen Betriebssystemen läuft, darunter Windows, macOS und Linux sowie mobile Betriebssysteme, ohne dass größere Änderungen am Code nötig sind.

Voraussetzung für dieses Tutorial ist die [Installation von Rust](https://www.rust-lang.org/tools/install), die den Rust-Compiler und Cargo, den Rust-Paketmanager, beinhaltet.

## Schritt 1: Neues Rust-Projekt erstellen

Um ein neues Rust-Projekt zu erstellen, führen Sie folgenden Befehl im Terminal aus:

```bash
cargo new phi-console-app
```

Dies erzeugt eine erste Projektstruktur mit einer `Cargo.toml`-Datei und einem `src`-Verzeichnis, das eine `main.rs`-Datei enthält.

Als Nächstes fügen wir unsere Abhängigkeiten – nämlich die Crates `candle`, `hf-hub` und `tokenizers` – zur `Cargo.toml`-Datei hinzu:

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

## Schritt 2: Grundlegende Parameter konfigurieren

In der Datei main.rs richten wir die Anfangsparameter für unsere Inferenz ein. Diese werden der Einfachheit halber fest codiert, können aber bei Bedarf angepasst werden.

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

- **temperature**: Steuert die Zufälligkeit des Sampling-Prozesses.
- **sample_len**: Gibt die maximale Länge des generierten Textes an.
- **top_p**: Wird für Nucleus Sampling verwendet, um die Anzahl der für jeden Schritt betrachteten Tokens zu begrenzen.
- **repeat_last_n**: Bestimmt, wie viele Tokens für die Anwendung einer Strafe zur Vermeidung von Wiederholungen berücksichtigt werden.
- **repeat_penalty**: Der Strafwert, um wiederholte Tokens zu entmutigen.
- **seed**: Ein Zufallssamen (für bessere Reproduzierbarkeit könnte ein konstanter Wert verwendet werden).
- **prompt**: Der Anfangstext, mit dem die Generierung startet. Beachten Sie, dass wir das Modell bitten, ein Haiku über Eishockey zu generieren, und dass wir es mit speziellen Tokens umgeben, um die Benutzer- und Assistentenanteile des Gesprächs zu kennzeichnen. Das Modell vervollständigt dann den Prompt mit einem Haiku.
- **device**: In diesem Beispiel verwenden wir die CPU für die Berechnung. Candle unterstützt auch die Ausführung auf GPU mit CUDA und Metal.

## Schritt 3: Modell und Tokenizer herunterladen/vorbereiten

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

Wir verwenden die `hf_hub` API, um die Modell- und Tokenizer-Dateien vom Hugging Face Model Hub herunterzuladen. Die `gguf`-Datei enthält die quantisierten Modellgewichte, während die `tokenizer.json`-Datei für die Tokenisierung unseres Eingabetextes genutzt wird. Nach dem Download wird das Modell zwischengespeichert, sodass der erste Durchlauf langsam ist (da 2,4 GB Modell heruntergeladen werden), aber die folgenden Ausführungen schneller sind.

## Schritt 4: Modell laden

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Wir laden die quantisierten Modellgewichte in den Speicher und initialisieren das Phi-3 Modell. Dieser Schritt beinhaltet das Einlesen der Modellgewichte aus der `gguf`-Datei und das Einrichten des Modells für die Inferenz auf dem angegebenen Gerät (hier CPU).

## Schritt 5: Prompt verarbeiten und für Inferenz vorbereiten

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

In diesem Schritt tokenisieren wir den Eingabeprompt und bereiten ihn für die Inferenz vor, indem wir ihn in eine Sequenz von Token-IDs umwandeln. Außerdem initialisieren wir den `LogitsProcessor`, der den Sampling-Prozess (Wahrscheinlichkeitsverteilung über den Wortschatz) basierend auf den angegebenen `temperature`- und `top_p`-Werten steuert. Jeder Token wird in einen Tensor umgewandelt und durch das Modell geleitet, um die Logits zu erhalten.

Die Schleife verarbeitet jeden Token im Prompt, aktualisiert den LogitsProcessor und bereitet die Generierung des nächsten Tokens vor.

## Schritt 6: Inferenz

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

In der Inferenzschleife generieren wir Tokens einzeln, bis die gewünschte Sample-Länge erreicht ist oder ein End-of-Sequence-Token auftaucht. Der nächste Token wird in einen Tensor umgewandelt und durch das Modell geleitet, während die Logits verarbeitet werden, um Strafen und Sampling anzuwenden. Anschließend wird der nächste Token ausgewählt, decodiert und an die Sequenz angehängt.
Um Wiederholungen zu vermeiden, wird eine Strafe auf wiederholte Tokens angewendet, basierend auf den Parametern `repeat_last_n` und `repeat_penalty`.

Schließlich wird der generierte Text während der Decodierung ausgegeben, um eine gestreamte Echtzeitausgabe zu gewährleisten.

## Schritt 7: Anwendung ausführen

Um die Anwendung auszuführen, geben Sie folgenden Befehl im Terminal ein:

```bash
cargo run --release
```

Dies sollte ein Haiku über Eishockey ausgeben, das vom Phi-3 Modell generiert wurde. Etwa so:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

oder

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Fazit

Mit diesen Schritten können wir Textgenerierung mit dem Phi-3 Modell in Rust und Candle in weniger als 100 Zeilen Code durchführen. Der Code übernimmt das Laden des Modells, die Tokenisierung und die Inferenz und nutzt Tensoren sowie Logits-Verarbeitung, um kohärenten Text basierend auf dem Eingabeprompt zu erzeugen.

Diese Konsolenanwendung läuft unter Windows, Linux und Mac OS. Aufgrund der Portabilität von Rust kann der Code auch zu einer Bibliothek angepasst werden, die in mobilen Apps läuft (Konsolenanwendungen sind dort schließlich nicht ausführbar).

## Anhang: vollständiger Code

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

Hinweis: Um diesen Code auf aarch64 Linux oder aarch64 Windows auszuführen, fügen Sie eine Datei namens `.cargo/config` mit folgendem Inhalt hinzu:

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

> Weitere Beispiele zur Verwendung des Phi-3 Modells mit Rust und Candle, einschließlich alternativer Ansätze zur Inferenz, finden Sie im offiziellen [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) Repository.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.