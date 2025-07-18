<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:31:51+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "id"
}
-->
# Inferensi lintas platform dengan Rust

Tutorial ini akan memandu kita melalui proses melakukan inferensi menggunakan Rust dan [Candle ML framework](https://github.com/huggingface/candle) dari HuggingFace. Menggunakan Rust untuk inferensi menawarkan beberapa keuntungan, terutama jika dibandingkan dengan bahasa pemrograman lain. Rust dikenal dengan performanya yang tinggi, setara dengan C dan C++. Ini menjadikannya pilihan yang sangat baik untuk tugas inferensi, yang bisa sangat intensif secara komputasi. Hal ini terutama didorong oleh abstraksi tanpa biaya dan manajemen memori yang efisien, tanpa overhead pengumpulan sampah. Kemampuan lintas platform Rust memungkinkan pengembangan kode yang dapat dijalankan di berbagai sistem operasi, termasuk Windows, macOS, dan Linux, serta sistem operasi mobile, tanpa perubahan signifikan pada basis kode.

Prasyarat untuk mengikuti tutorial ini adalah [menginstal Rust](https://www.rust-lang.org/tools/install), yang mencakup compiler Rust dan Cargo, manajer paket Rust.

## Langkah 1: Buat Proyek Rust Baru

Untuk membuat proyek Rust baru, jalankan perintah berikut di terminal:

```bash
cargo new phi-console-app
```

Ini akan menghasilkan struktur proyek awal dengan file `Cargo.toml` dan direktori `src` yang berisi file `main.rs`.

Selanjutnya, kita akan menambahkan dependensi kita - yaitu crate `candle`, `hf-hub`, dan `tokenizers` - ke dalam file `Cargo.toml`:

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

## Langkah 2: Konfigurasikan Parameter Dasar

Di dalam file main.rs, kita akan mengatur parameter awal untuk inferensi kita. Semua parameter ini akan di-hardcode untuk kesederhanaan, tapi kita bisa mengubahnya sesuai kebutuhan.

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

- **temperature**: Mengontrol tingkat keacakan dalam proses sampling.
- **sample_len**: Menentukan panjang maksimum teks yang dihasilkan.
- **top_p**: Digunakan untuk nucleus sampling untuk membatasi jumlah token yang dipertimbangkan pada setiap langkah.
- **repeat_last_n**: Mengontrol jumlah token yang dipertimbangkan untuk menerapkan penalti agar menghindari urutan yang berulang.
- **repeat_penalty**: Nilai penalti untuk mengurangi kemunculan token yang berulang.
- **seed**: Seed acak (kita bisa menggunakan nilai konstan untuk reproduksibilitas yang lebih baik).
- **prompt**: Teks prompt awal untuk memulai generasi. Perhatikan bahwa kita meminta model untuk membuat haiku tentang hoki es, dan kita membungkusnya dengan token khusus untuk menandai bagian percakapan pengguna dan asisten. Model kemudian akan melengkapi prompt tersebut dengan haiku.
- **device**: Kita menggunakan CPU untuk komputasi dalam contoh ini. Candle juga mendukung penggunaan GPU dengan CUDA dan Metal.

## Langkah 3: Unduh/Siapkan Model dan Tokenizer

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

Kita menggunakan API `hf_hub` untuk mengunduh file model dan tokenizer dari Hugging Face model hub. File `gguf` berisi bobot model yang sudah dikuantisasi, sedangkan file `tokenizer.json` digunakan untuk melakukan tokenisasi pada teks input kita. Setelah diunduh, model akan disimpan dalam cache, sehingga eksekusi pertama akan lambat (karena mengunduh model sebesar 2,4GB), tapi eksekusi berikutnya akan lebih cepat.

## Langkah 4: Muat Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Kita memuat bobot model yang sudah dikuantisasi ke dalam memori dan menginisialisasi model Phi-3. Langkah ini melibatkan pembacaan bobot model dari file `gguf` dan menyiapkan model untuk inferensi pada perangkat yang ditentukan (dalam kasus ini CPU).

## Langkah 5: Proses Prompt dan Persiapan Inferensi

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

Pada langkah ini, kita melakukan tokenisasi pada prompt input dan menyiapkannya untuk inferensi dengan mengubahnya menjadi urutan ID token. Kita juga menginisialisasi `LogitsProcessor` untuk menangani proses sampling (distribusi probabilitas atas kosakata) berdasarkan nilai `temperature` dan `top_p` yang diberikan. Setiap token diubah menjadi tensor dan dilewatkan ke model untuk mendapatkan logits.

Loop ini memproses setiap token dalam prompt, memperbarui logits processor, dan menyiapkan untuk generasi token berikutnya.

## Langkah 6: Inferensi

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

Dalam loop inferensi, kita menghasilkan token satu per satu sampai mencapai panjang sampel yang diinginkan atau menemukan token akhir urutan. Token berikutnya diubah menjadi tensor dan dilewatkan ke model, sementara logits diproses untuk menerapkan penalti dan sampling. Kemudian token berikutnya diambil sampelnya, didekode, dan ditambahkan ke urutan.
Untuk menghindari teks yang berulang, penalti diterapkan pada token yang berulang berdasarkan parameter `repeat_last_n` dan `repeat_penalty`.

Akhirnya, teks yang dihasilkan dicetak saat didekode, memastikan output real-time yang mengalir.

## Langkah 7: Jalankan Aplikasi

Untuk menjalankan aplikasi, eksekusi perintah berikut di terminal:

```bash
cargo run --release
```

Ini akan mencetak haiku tentang hoki es yang dihasilkan oleh model Phi-3. Contohnya seperti:

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

Dengan mengikuti langkah-langkah ini, kita dapat melakukan generasi teks menggunakan model Phi-3 dengan Rust dan Candle dalam kurang dari 100 baris kode. Kode ini menangani pemuatan model, tokenisasi, dan inferensi, memanfaatkan tensor dan pemrosesan logits untuk menghasilkan teks yang koheren berdasarkan prompt input.

Aplikasi konsol ini dapat dijalankan di Windows, Linux, dan Mac OS. Karena portabilitas Rust, kode ini juga dapat diadaptasi menjadi pustaka yang dapat dijalankan di dalam aplikasi mobile (karena kita tidak bisa menjalankan aplikasi konsol di sana).

## Lampiran: kode lengkap

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

Catatan: untuk menjalankan kode ini di aarch64 Linux atau aarch64 Windows, tambahkan file bernama `.cargo/config` dengan isi berikut:

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

> Kamu bisa mengunjungi repositori resmi [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) untuk contoh lebih lanjut tentang cara menggunakan model Phi-3 dengan Rust dan Candle, termasuk pendekatan alternatif untuk inferensi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.