<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:29:36+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "el"
}
-->
# Cross-platform inference with Rust

Αυτό το σεμινάριο θα μας καθοδηγήσει στη διαδικασία εκτέλεσης inference χρησιμοποιώντας Rust και το [Candle ML framework](https://github.com/huggingface/candle) από το HuggingFace. Η χρήση του Rust για inference προσφέρει αρκετά πλεονεκτήματα, ειδικά σε σύγκριση με άλλες γλώσσες προγραμματισμού. Το Rust είναι γνωστό για την υψηλή απόδοσή του, συγκρίσιμη με αυτή των C και C++. Αυτό το καθιστά εξαιρετική επιλογή για εργασίες inference, οι οποίες μπορεί να είναι υπολογιστικά απαιτητικές. Συγκεκριμένα, αυτό οφείλεται στις zero-cost abstractions και στην αποδοτική διαχείριση μνήμης, χωρίς το κόστος συλλογής απορριμμάτων (garbage collection). Οι δυνατότητες cross-platform του Rust επιτρέπουν την ανάπτυξη κώδικα που τρέχει σε διάφορα λειτουργικά συστήματα, όπως Windows, macOS και Linux, καθώς και σε κινητά λειτουργικά συστήματα, χωρίς σημαντικές αλλαγές στον κώδικα.

Η προϋπόθεση για να ακολουθήσετε αυτό το σεμινάριο είναι να [εγκαταστήσετε το Rust](https://www.rust-lang.org/tools/install), που περιλαμβάνει τον compiler του Rust και το Cargo, τον διαχειριστή πακέτων του Rust.

## Βήμα 1: Δημιουργία νέου έργου Rust

Για να δημιουργήσετε ένα νέο έργο Rust, εκτελέστε την παρακάτω εντολή στο τερματικό:

```bash
cargo new phi-console-app
```

Αυτό δημιουργεί μια αρχική δομή έργου με ένα αρχείο `Cargo.toml` και έναν φάκελο `src` που περιέχει το αρχείο `main.rs`.

Στη συνέχεια, θα προσθέσουμε τις εξαρτήσεις μας - συγκεκριμένα τα crates `candle`, `hf-hub` και `tokenizers` - στο αρχείο `Cargo.toml`:

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

## Βήμα 2: Ρύθμιση βασικών παραμέτρων

Μέσα στο αρχείο main.rs, θα ορίσουμε τις αρχικές παραμέτρους για το inference. Όλες θα είναι σκληροκωδικοποιημένες για απλότητα, αλλά μπορούμε να τις τροποποιήσουμε ανάλογα με τις ανάγκες.

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

- **temperature**: Ελέγχει την τυχαιότητα της διαδικασίας δειγματοληψίας.
- **sample_len**: Καθορίζει το μέγιστο μήκος του παραγόμενου κειμένου.
- **top_p**: Χρησιμοποιείται για nucleus sampling ώστε να περιορίσει τον αριθμό των tokens που λαμβάνονται υπόψη σε κάθε βήμα.
- **repeat_last_n**: Ελέγχει τον αριθμό των tokens που λαμβάνονται υπόψη για την επιβολή ποινής ώστε να αποτραπούν επαναλαμβανόμενες ακολουθίες.
- **repeat_penalty**: Η τιμή ποινής για να αποθαρρυνθούν τα επαναλαμβανόμενα tokens.
- **seed**: Μια τυχαία τιμή seed (μπορούμε να χρησιμοποιήσουμε μια σταθερή τιμή για καλύτερη αναπαραγωγιμότητα).
- **prompt**: Το αρχικό κείμενο προτροπής για να ξεκινήσει η παραγωγή. Σημειώστε ότι ζητάμε από το μοντέλο να δημιουργήσει ένα haiku για το ice hockey, και το περικλείουμε με ειδικά tokens για να υποδείξουμε τα μέρη του χρήστη και του βοηθού στη συνομιλία. Το μοντέλο στη συνέχεια ολοκληρώνει την προτροπή με ένα haiku.
- **device**: Σε αυτό το παράδειγμα χρησιμοποιούμε την CPU για τους υπολογισμούς. Το Candle υποστηρίζει επίσης εκτέλεση σε GPU με CUDA και Metal.

## Βήμα 3: Κατέβασμα/Προετοιμασία μοντέλου και tokenizer

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

Χρησιμοποιούμε το API `hf_hub` για να κατεβάσουμε τα αρχεία του μοντέλου και του tokenizer από το Hugging Face model hub. Το αρχείο `gguf` περιέχει τα κβαντισμένα βάρη του μοντέλου, ενώ το αρχείο `tokenizer.json` χρησιμοποιείται για την τοκενικοποίηση του εισαγόμενου κειμένου. Μόλις κατέβει, το μοντέλο αποθηκεύεται στην cache, οπότε η πρώτη εκτέλεση θα είναι αργή (καθώς κατεβάζει τα 2.4GB του μοντέλου), αλλά οι επόμενες εκτελέσεις θα είναι πιο γρήγορες.

## Βήμα 4: Φόρτωση μοντέλου

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Φορτώνουμε τα κβαντισμένα βάρη του μοντέλου στη μνήμη και αρχικοποιούμε το μοντέλο Phi-3. Αυτό το βήμα περιλαμβάνει την ανάγνωση των βαρών από το αρχείο `gguf` και τη ρύθμιση του μοντέλου για inference στη συγκεκριμένη συσκευή (CPU σε αυτή την περίπτωση).

## Βήμα 5: Επεξεργασία προτροπής και προετοιμασία για inference

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

Σε αυτό το βήμα, τοκενίζουμε την εισαγόμενη προτροπή και την προετοιμάζουμε για inference μετατρέποντάς την σε ακολουθία αναγνωριστικών tokens. Επίσης, αρχικοποιούμε τον `LogitsProcessor` για να διαχειριστεί τη διαδικασία δειγματοληψίας (κατανομή πιθανοτήτων πάνω στο λεξιλόγιο) βάσει των τιμών `temperature` και `top_p`. Κάθε token μετατρέπεται σε tensor και περνάει μέσα από το μοντέλο για να πάρουμε τα logits.

Ο βρόχος επεξεργάζεται κάθε token στην προτροπή, ενημερώνοντας τον logits processor και προετοιμάζοντας για την παραγωγή του επόμενου token.

## Βήμα 6: Inference

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

Στον βρόχο inference, παράγουμε tokens ένα-ένα μέχρι να φτάσουμε στο επιθυμητό μήκος δείγματος ή να συναντήσουμε το token τέλους ακολουθίας. Το επόμενο token μετατρέπεται σε tensor και περνάει μέσα από το μοντέλο, ενώ τα logits επεξεργάζονται για να εφαρμοστούν ποινές και δειγματοληψία. Στη συνέχεια, το επόμενο token δειγματοληπτείται, αποκωδικοποιείται και προστίθεται στην ακολουθία.  
Για να αποφευχθεί η επανάληψη κειμένου, εφαρμόζεται ποινή στα επαναλαμβανόμενα tokens βάσει των παραμέτρων `repeat_last_n` και `repeat_penalty`.

Τέλος, το παραγόμενο κείμενο εκτυπώνεται καθώς αποκωδικοποιείται, εξασφαλίζοντας ροή εξόδου σε πραγματικό χρόνο.

## Βήμα 7: Εκτέλεση της εφαρμογής

Για να εκτελέσετε την εφαρμογή, δώστε την παρακάτω εντολή στο τερματικό:

```bash
cargo run --release
```

Αυτό θα εκτυπώσει ένα haiku για το ice hockey που δημιουργήθηκε από το μοντέλο Phi-3. Κάτι σαν:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ή

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Συμπέρασμα

Ακολουθώντας αυτά τα βήματα, μπορούμε να πραγματοποιήσουμε παραγωγή κειμένου χρησιμοποιώντας το μοντέλο Phi-3 με Rust και Candle σε λιγότερες από 100 γραμμές κώδικα. Ο κώδικας διαχειρίζεται τη φόρτωση μοντέλου, την τοκενικοποίηση και το inference, αξιοποιώντας tensors και επεξεργασία logits για να δημιουργήσει συνεκτικό κείμενο βάσει της εισαγόμενης προτροπής.

Αυτή η κονσολική εφαρμογή μπορεί να τρέξει σε Windows, Linux και Mac OS. Λόγω της φορητότητας του Rust, ο κώδικας μπορεί επίσης να προσαρμοστεί σε βιβλιοθήκη που θα τρέχει μέσα σε εφαρμογές κινητών (καθώς δεν μπορούμε να τρέξουμε κονσολικές εφαρμογές εκεί).

## Παράρτημα: πλήρης κώδικας

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

Σημείωση: για να τρέξετε αυτόν τον κώδικα σε aarch64 Linux ή aarch64 Windows, προσθέστε ένα αρχείο με όνομα `.cargo/config` με το παρακάτω περιεχόμενο:

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

> Μπορείτε να επισκεφθείτε το επίσημο αποθετήριο [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) για περισσότερα παραδείγματα σχετικά με τη χρήση του μοντέλου Phi-3 με Rust και Candle, συμπεριλαμβανομένων εναλλακτικών προσεγγίσεων για το inference.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.