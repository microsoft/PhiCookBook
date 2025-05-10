<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:03:33+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ms"
}
-->
# Inferenz plattformübergreifend mit Rust

Dieses Tutorial führt uns durch den Prozess der Inferenz mit Rust und dem [Candle ML Framework](https://github.com/huggingface/candle) von HuggingFace. Die Verwendung von Rust für Inferenz bietet mehrere Vorteile, insbesondere im Vergleich zu anderen Programmiersprachen. Rust ist bekannt für seine hohe Leistung, vergleichbar mit der von C und C++. Das macht es zu einer ausgezeichneten Wahl für Inferenzaufgaben, die oft rechenintensiv sind. Besonders hervorzuheben sind die zero-cost Abstraktionen und das effiziente Speichermanagement ohne Garbage Collection. Die plattformübergreifenden Fähigkeiten von Rust ermöglichen die Entwicklung von Code, der auf verschiedenen Betriebssystemen wie Windows, macOS und Linux sowie auf mobilen Betriebssystemen läuft, ohne dass größere Änderungen am Code notwendig sind.

Voraussetzung für dieses Tutorial ist die [Installation von Rust](https://www.rust-lang.org/tools/install), die den Rust-Compiler und Cargo, den Paketmanager von Rust, beinhaltet.

## Schritt 1: Neues Rust-Projekt erstellen

Um ein neues Rust-Projekt zu erstellen, führen Sie folgenden Befehl im Terminal aus:

```bash
cargo new phi-console-app
```

Dadurch wird eine Grundstruktur mit einer `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` Datei erzeugt:

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

Innerhalb der main.rs-Datei legen wir die Anfangsparameter für unsere Inferenz fest. Diese werden der Einfachheit halber fest kodiert, können aber bei Bedarf angepasst werden.

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
- **top_p**: Wird beim Nucleus Sampling verwendet, um die Anzahl der berücksichtigten Tokens pro Schritt zu begrenzen.
- **repeat_last_n**: Bestimmt, wie viele Tokens für die Anwendung einer Strafe zur Vermeidung von Wiederholungen berücksichtigt werden.
- **repeat_penalty**: Der Strafwert, der wiederholte Tokens entmutigt.
- **seed**: Ein Zufallswert (für bessere Reproduzierbarkeit kann ein konstanter Wert genutzt werden).
- **prompt**: Der Anfangstext für die Generierung. Beachten Sie, dass wir das Modell bitten, ein Haiku über Eishockey zu erzeugen und diesen mit speziellen Tokens versehen, die die Benutzer- und Assistententeile des Gesprächs markieren. Das Modell ergänzt dann den Prompt mit einem Haiku.
- **device**: In diesem Beispiel nutzen wir die CPU für die Berechnung. Candle unterstützt auch GPU-Berechnung mit CUDA und Metal.

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

Die Datei `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` wird für die Tokenisierung unseres Eingabetextes verwendet. Nach dem Download wird das Modell zwischengespeichert, daher ist die erste Ausführung langsamer (da 2,4 GB Modelldaten heruntergeladen werden), spätere Ausführungen laufen dann schneller.

## Schritt 4: Modell laden

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Wir laden die quantisierten Modellgewichte in den Speicher und initialisieren das Phi-3 Modell. Dieser Schritt beinhaltet das Einlesen der Modellgewichte aus der `gguf`-Datei und die Vorbereitung des Modells für die Inferenz auf dem angegebenen Gerät (hier CPU).

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

In diesem Schritt tokenisieren wir den Eingabe-Prompt und bereiten ihn für die Inferenz vor, indem wir ihn in eine Sequenz von Token-IDs umwandeln. Außerdem initialisieren wir die `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` Werte. Jeder Token wird in einen Tensor umgewandelt und durch das Modell geschickt, um die Logits zu erhalten.

Die Schleife verarbeitet jeden Token im Prompt, aktualisiert den Logits-Processor und bereitet die Generierung des nächsten Tokens vor.

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

In der Inferenz-Schleife generieren wir Token einzeln, bis die gewünschte Sample-Länge erreicht oder ein End-of-Sequence-Token gefunden wird. Der nächste Token wird in einen Tensor umgewandelt und durch das Modell geschickt, während die Logits verarbeitet werden, um Strafen und Sampling anzuwenden. Anschließend wird der nächste Token ausgewählt, dekodiert und zur Sequenz hinzugefügt.
Um Wiederholungen zu vermeiden, wird basierend auf den Parametern `repeat_last_n` and `repeat_penalty` eine Strafe auf wiederholte Tokens angewendet.

Schließlich wird der generierte Text während der Dekodierung ausgegeben, um eine gestreamte Echtzeit-Ausgabe zu gewährleisten.

## Schritt 7: Anwendung ausführen

Um die Anwendung zu starten, führen Sie folgenden Befehl im Terminal aus:

```bash
cargo run --release
```

Dies sollte ein Haiku über Eishockey ausgeben, das vom Phi-3 Modell generiert wurde. Zum Beispiel:

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

Mit diesen Schritten können wir Textgenerierung mit dem Phi-3 Modell in Rust und Candle in weniger als 100 Codezeilen durchführen. Der Code kümmert sich um das Laden des Modells, die Tokenisierung und die Inferenz, nutzt Tensoren und Logits-Verarbeitung, um kohärenten Text basierend auf dem Eingabe-Prompt zu erzeugen.

Diese Konsolenanwendung läuft unter Windows, Linux und Mac OS. Aufgrund der Portabilität von Rust kann der Code auch zu einer Bibliothek umgewandelt werden, die in mobilen Apps läuft (Konsolenanwendungen sind dort schließlich nicht möglich).

## Anhang: kompletter Code

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

> Weitere Beispiele zur Verwendung des Phi-3 Modells mit Rust und Candle, einschließlich alternativer Inferenzansätze, finden Sie im offiziellen [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) Repository.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.