# Inferens rentas platform dengan Rust

Tutorial ini akan membimbing kita melalui proses melakukan inferens menggunakan Rust dan [rangka kerja ML Candle](https://github.com/huggingface/candle) dari HuggingFace. Menggunakan Rust untuk inferens menawarkan beberapa kelebihan, terutamanya jika dibandingkan dengan bahasa pengaturcaraan lain. Rust terkenal dengan prestasinya yang tinggi, setanding dengan C dan C++. Ini menjadikannya pilihan yang sangat baik untuk tugasan inferens yang boleh menjadi intensif dari segi pengiraan. Terutamanya, ini didorong oleh abstraksi tanpa kos dan pengurusan memori yang cekap, tanpa beban pengumpulan sampah. Keupayaan rentas platform Rust membolehkan pembangunan kod yang boleh dijalankan pada pelbagai sistem operasi, termasuk Windows, macOS, dan Linux, serta sistem operasi mudah alih, tanpa perubahan besar pada kod asas.

Prasyarat untuk mengikuti tutorial ini adalah untuk [memasang Rust](https://www.rust-lang.org/tools/install), yang merangkumi penyusun Rust dan Cargo, pengurus pakej Rust.

## Langkah 1: Cipta Projek Rust Baru

Untuk mencipta projek Rust baru, jalankan arahan berikut di terminal:

```bash
cargo new phi-console-app
```

Ini akan menjana struktur projek awal dengan fail `Cargo.toml` dan direktori `src` yang mengandungi fail `main.rs`.

Seterusnya, kita akan menambah kebergantungan kita - iaitu `candle`, `hf-hub` dan `tokenizers` crates - ke dalam fail `Cargo.toml`:

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

## Langkah 2: Konfigurasikan Parameter Asas

Di dalam fail main.rs, kita akan tetapkan parameter awal untuk inferens kita. Kesemuanya akan dikodkan secara keras untuk kesederhanaan, tetapi kita boleh mengubahnya mengikut keperluan.

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

- **temperature**: Mengawal kebarangkalian rawak dalam proses pensampelan.
- **sample_len**: Menentukan panjang maksimum teks yang dijana.
- **top_p**: Digunakan untuk pensampelan nukleus bagi mengehadkan bilangan token yang dipertimbangkan pada setiap langkah.
- **repeat_last_n**: Mengawal bilangan token yang dipertimbangkan untuk mengenakan penalti bagi mengelakkan urutan berulang.
- **repeat_penalty**: Nilai penalti untuk menghalang token yang berulang.
- **seed**: Benih rawak (kita boleh menggunakan nilai tetap untuk kebolehulangan yang lebih baik).
- **prompt**: Teks permulaan untuk memulakan penjanaan. Perhatikan bahawa kita meminta model menjana haiku tentang hoki ais, dan kita membungkusnya dengan token khas untuk menunjukkan bahagian pengguna dan pembantu dalam perbualan. Model kemudian akan melengkapkan prompt dengan haiku.
- **device**: Kita menggunakan CPU untuk pengiraan dalam contoh ini. Candle juga menyokong penggunaan GPU dengan CUDA dan Metal.

## Langkah 3: Muat Turun/Sediakan Model dan Tokenizer

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

Kita menggunakan API `hf_hub` untuk memuat turun fail model dan tokenizer dari pusat model Hugging Face. Fail `gguf` mengandungi berat model yang telah dikuantisasi, manakala fail `tokenizer.json` digunakan untuk men-token-kan teks input kita. Setelah dimuat turun, model akan disimpan dalam cache, jadi pelaksanaan pertama akan lambat (kerana memuat turun model sebesar 2.4GB) tetapi pelaksanaan seterusnya akan lebih pantas.

## Langkah 4: Muatkan Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Kita memuatkan berat model yang telah dikuantisasi ke dalam memori dan menginisialisasi model Phi-3. Langkah ini melibatkan pembacaan berat model dari fail `gguf` dan menyediakan model untuk inferens pada peranti yang ditetapkan (CPU dalam kes ini).

## Langkah 5: Proses Prompt dan Sediakan untuk Inferens

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

Dalam langkah ini, kita men-token-kan prompt input dan menyediakannya untuk inferens dengan menukarnya menjadi urutan ID token. Kita juga menginisialisasi `LogitsProcessor` untuk mengendalikan proses pensampelan (taburan kebarangkalian ke atas kosa kata) berdasarkan nilai `temperature` dan `top_p` yang diberikan. Setiap token ditukar menjadi tensor dan dihantar melalui model untuk mendapatkan logits.

Gelung ini memproses setiap token dalam prompt, mengemas kini pemproses logits dan menyediakan untuk penjanaan token seterusnya.

## Langkah 6: Inferens

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

Dalam gelung inferens, kita menjana token satu persatu sehingga mencapai panjang sampel yang dikehendaki atau menemui token tamat urutan. Token seterusnya ditukar menjadi tensor dan dihantar melalui model, manakala logits diproses untuk mengenakan penalti dan pensampelan. Kemudian token seterusnya dipilih, disahkod, dan ditambah ke dalam urutan.
Untuk mengelakkan teks berulang, penalti dikenakan ke atas token yang berulang berdasarkan parameter `repeat_last_n` dan `repeat_penalty`.

Akhirnya, teks yang dijana dicetak semasa ia disahkod, memastikan output masa nyata secara berterusan.

## Langkah 7: Jalankan Aplikasi

Untuk menjalankan aplikasi, laksanakan arahan berikut di terminal:

```bash
cargo run --release
```

Ini sepatutnya mencetak haiku tentang hoki ais yang dijana oleh model Phi-3. Sesuatu seperti:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

atau

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Kesimpulan

Dengan mengikuti langkah-langkah ini, kita boleh melakukan penjanaan teks menggunakan model Phi-3 dengan Rust dan Candle dalam kurang daripada 100 baris kod. Kod ini mengendalikan pemuatan model, pen-token-an, dan inferens, menggunakan tensor dan pemprosesan logits untuk menjana teks yang koheren berdasarkan prompt input.

Aplikasi konsol ini boleh dijalankan di Windows, Linux dan Mac OS. Disebabkan kebolehpindahan Rust, kod ini juga boleh diubah suai menjadi perpustakaan yang boleh dijalankan dalam aplikasi mudah alih (kita tidak boleh menjalankan aplikasi konsol di sana, selepas semua).

## Lampiran: kod penuh

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

Nota: untuk menjalankan kod ini pada aarch64 Linux atau aarch64 Windows, tambah fail bernama `.cargo/config` dengan kandungan berikut:

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

> Anda boleh melawat repositori rasmi [contoh Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) untuk lebih banyak contoh cara menggunakan model Phi-3 dengan Rust dan Candle, termasuk pendekatan alternatif untuk inferens.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.