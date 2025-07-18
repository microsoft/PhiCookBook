<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:29:23+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "tr"
}
-->
# Rust ile Çok Platformlu Çıkarım

Bu eğitimde, Rust ve HuggingFace’in [Candle ML framework](https://github.com/huggingface/candle) kullanarak çıkarım yapma sürecini öğreneceğiz. Rust ile çıkarım yapmak, özellikle diğer programlama dilleriyle karşılaştırıldığında birçok avantaj sunar. Rust, C ve C++ ile karşılaştırılabilir yüksek performansıyla bilinir. Bu da hesaplama açısından yoğun olan çıkarım görevleri için mükemmel bir seçim olmasını sağlar. Özellikle sıfır maliyetli soyutlamalar ve çöp toplayıcı yükü olmayan verimli bellek yönetimi bunu mümkün kılar. Rust’ın çok platformlu yetenekleri, Windows, macOS ve Linux gibi çeşitli işletim sistemlerinde ve mobil işletim sistemlerinde kod tabanında büyük değişiklik yapmadan çalışabilen kod geliştirmeyi sağlar.

Bu eğitimi takip etmek için öncelikle [Rust’u kurmanız](https://www.rust-lang.org/tools/install) gerekir; bu kurulum Rust derleyicisi ve Rust paket yöneticisi Cargo’yu içerir.

## Adım 1: Yeni Bir Rust Projesi Oluşturun

Yeni bir Rust projesi oluşturmak için terminalde aşağıdaki komutu çalıştırın:

```bash
cargo new phi-console-app
```

Bu, `Cargo.toml` dosyası ve içinde `main.rs` dosyası bulunan `src` dizini ile birlikte başlangıç bir proje yapısı oluşturur.

Sonraki adımda, bağımlılıklarımızı — yani `candle`, `hf-hub` ve `tokenizers` crate’lerini — `Cargo.toml` dosyasına ekleyeceğiz:

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

## Adım 2: Temel Parametreleri Yapılandırın

`main.rs` dosyasının içinde çıkarım için başlangıç parametrelerini ayarlayacağız. Basitlik adına hepsi sabit kodlanacak, ancak ihtiyaç duydukça değiştirebiliriz.

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

- **temperature**: Örnekleme sürecinin rastgeleliğini kontrol eder.
- **sample_len**: Oluşturulacak metnin maksimum uzunluğunu belirtir.
- **top_p**: Her adımda dikkate alınacak token sayısını sınırlamak için nucleus sampling’de kullanılır.
- **repeat_last_n**: Tekrarlayan dizileri önlemek için ceza uygulanacak token sayısını kontrol eder.
- **repeat_penalty**: Tekrarlanan tokenları caydırmak için uygulanan ceza değeri.
- **seed**: Rastgelelik için kullanılan tohum (daha iyi tekrarlanabilirlik için sabit bir değer kullanılabilir).
- **prompt**: Oluşturmayı başlatmak için başlangıç metni. Modelden buz hokeyi hakkında bir haiku oluşturmasını istiyoruz ve konuşmanın kullanıcı ve asistan kısımlarını belirtmek için özel tokenlarla sarıyoruz. Model, ardından prompt’u bir haiku ile tamamlayacak.
- **device**: Bu örnekte hesaplama için CPU kullanıyoruz. Candle, CUDA ve Metal ile GPU üzerinde çalışmayı da destekler.

## Adım 3: Model ve Tokenizer’ı İndir/Hazırla

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

Model ve tokenizer dosyalarını Hugging Face model hub’dan indirmek için `hf_hub` API’sini kullanıyoruz. `gguf` dosyası kuantize edilmiş model ağırlıklarını içerirken, `tokenizer.json` dosyası giriş metnimizi token’lara ayırmak için kullanılır. İndirildikten sonra model önbelleğe alınır, bu yüzden ilk çalıştırma yavaş olur (modelin 2.4GB’lık kısmı indirildiği için), ancak sonraki çalıştırmalar daha hızlı olur.

## Adım 4: Modeli Yükle

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Kuantize edilmiş model ağırlıklarını belleğe yüklüyor ve Phi-3 modelini başlatıyoruz. Bu adım, `gguf` dosyasından model ağırlıklarının okunmasını ve belirtilen cihazda (bu örnekte CPU) çıkarım için modelin hazırlanmasını içerir.

## Adım 5: Prompt’u İşle ve Çıkarım İçin Hazırla

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

Bu adımda, giriş prompt’unu token’lara ayırıyor ve token ID dizisine dönüştürerek çıkarım için hazırlıyoruz. Ayrıca, verilen `temperature` ve `top_p` değerlerine göre örnekleme sürecini (kelime dağarcığı üzerindeki olasılık dağılımını) yönetmek için `LogitsProcessor`’ı başlatıyoruz. Her token tensöre dönüştürülüp modelden geçirilerek logits elde edilir.

Döngü, prompt’taki her token’ı işler, logits processor’ı günceller ve sonraki token oluşturma için hazırlık yapar.

## Adım 6: Çıkarım

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

Çıkarım döngüsünde, istenen örnek uzunluğuna ulaşana veya dizinin sonu token’ına rastlayana kadar token’lar tek tek oluşturulur. Sonraki token tensöre dönüştürülüp modelden geçirilirken, logits işlenerek ceza ve örnekleme uygulanır. Ardından bir sonraki token örneklenir, çözümlenir ve diziye eklenir.  
Tekrarlayan metni önlemek için, `repeat_last_n` ve `repeat_penalty` parametrelerine göre tekrarlanan tokenlara ceza uygulanır.

Son olarak, oluşturulan metin çözümlendikçe yazdırılır ve böylece gerçek zamanlı akış sağlanır.

## Adım 7: Uygulamayı Çalıştır

Uygulamayı çalıştırmak için terminalde aşağıdaki komutu yürütün:

```bash
cargo run --release
```

Bu, Phi-3 modeli tarafından oluşturulmuş buz hokeyi hakkında bir haiku yazdırmalıdır. Şöyle bir şey olabilir:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

veya

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Sonuç

Bu adımları takip ederek, Phi-3 modeli ile Rust ve Candle kullanarak 100 satırın altında kodla metin oluşturabiliriz. Kod, model yükleme, tokenizasyon ve çıkarımı yönetir; tensörler ve logits işleme kullanarak giriş prompt’una dayalı tutarlı metin üretir.

Bu konsol uygulaması Windows, Linux ve Mac OS üzerinde çalışabilir. Rust’ın taşınabilirliği sayesinde, kod mobil uygulamalar içinde çalışacak bir kütüphaneye de uyarlanabilir (sonuçta orada konsol uygulaması çalıştıramayız).

## Ek: Tam Kod

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

Not: Bu kodu aarch64 Linux veya aarch64 Windows üzerinde çalıştırmak için, `.cargo/config` adlı bir dosya oluşturup içine aşağıdaki içeriği ekleyin:

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

> Phi-3 modelini Rust ve Candle ile kullanmaya dair daha fazla örnek ve çıkarım için alternatif yaklaşımlar görmek isterseniz, resmi [Candle örnekleri](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) deposunu ziyaret edebilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.