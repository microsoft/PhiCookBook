<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-09T13:05:02+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "sw"
}
-->
# Uhakiki wa msalaba-jukwaa kwa kutumia Rust

Mafunzo haya yatatuongoza katika mchakato wa kufanya uhakiki kwa kutumia Rust na [Candle ML framework](https://github.com/huggingface/candle) kutoka HuggingFace. Kutumia Rust kwa uhakiki kuna faida kadhaa, hasa ikilinganishwa na lugha nyingine za programu. Rust inajulikana kwa utendaji wake wa juu, unaolinganishwa na C na C++. Hii inafanya kuwa chaguo bora kwa kazi za uhakiki, ambazo zinaweza kuwa na mzigo mkubwa wa kihesabu. Hii hasa inatokana na abstractions zisizo na gharama na usimamizi mzuri wa kumbukumbu, ambao hauhusishi mzigo wa ukusanyaji taka. Uwezo wa Rust wa kufanya kazi kwenye majukwaa mbalimbali unaruhusu kuendeleza msimbo unaoweza kuendesha kwenye mifumo tofauti ya uendeshaji, ikiwa ni pamoja na Windows, macOS, na Linux, pamoja na mifumo ya uendeshaji wa simu, bila mabadiliko makubwa kwenye msimbo.

Sharti la kufuata mafunzo haya ni [kufunga Rust](https://www.rust-lang.org/tools/install), ambayo inajumuisha compiler ya Rust na Cargo, meneja wa vifurushi vya Rust.

## Hatua ya 1: Tengeneza Mradi Mpya wa Rust

Ili kutengeneza mradi mpya wa Rust, endesha amri ifuatayo kwenye terminal:

```bash
cargo new phi-console-app
```

Hii itaunda muundo wa awali wa mradi ukiwa na faili la `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Hatua ya 2: Sanidi Vigezo Msingi

Ndani ya faili la main.rs, tutaweka vigezo vya awali kwa ajili ya uhakiki wetu. Vyote vitakuwa vimewekwa moja kwa moja kwa ajili ya urahisi, lakini tunaweza kuvibadilisha kadri inavyohitajika.

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

- **temperature**: Huidhibiti nasibu ya mchakato wa sampuli.
- **sample_len**: Inaeleza urefu wa juu wa maandishi yatakayozalishwa.
- **top_p**: Inatumika kwa sampuli ya nucleus kupunguza idadi ya tokeni zinazochunguzwa kwa kila hatua.
- **repeat_last_n**: Huidhibiti idadi ya tokeni zinazochunguzwa kwa ajili ya kuweka adhabu kuzuia mfululizo wa kurudiwa.
- **repeat_penalty**: Thamani ya adhabu kuzuia tokeni kurudiwa.
- **seed**: Mbegu ya nasibu (tunaweza kutumia thamani thabiti kwa urudufu bora).
- **prompt**: Maandishi ya awali ya kuanzisha uzalishaji. Angalia kuwa tunaomba modeli izalishe haiku kuhusu ice hockey, na tunazizunguka na tokeni maalum kuonyesha sehemu za mtumiaji na msaidizi katika mazungumzo. Modeli itakamilisha prompt na haiku.
- **device**: Katika mfano huu tunatumia CPU kwa ajili ya hesabu. Candle pia inaunga mkono kutumia GPU kwa CUDA na Metal.

## Hatua ya 3: Pakua/Tayarisha Modeli na Tokenizer

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

Tunatumia faili la `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` kwa ajili ya kugawanya maandishi yetu ya kuingiza. Mara baada ya kupakuliwa, modeli huhifadhiwa kwenye cache, hivyo utekelezaji wa kwanza utakuwa polepole (kwa sababu inapakua modeli yenye ukubwa wa 2.4GB) lakini utekelezaji unaofuata utakuwa haraka zaidi.

## Hatua ya 4: Pakia Modeli

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Tunapakia uzito wa modeli uliobadilishwa kuwa kidogo kwenye kumbukumbu na kuanzisha modeli ya Phi-3. Hatua hii inahusisha kusoma uzito wa modeli kutoka kwenye faili la `gguf` na kuandaa modeli kwa ajili ya uhakiki kwenye kifaa kilichobainishwa (CPU katika mfano huu).

## Hatua ya 5: Tumia Prompt na Andaa kwa ajili ya Uhakiki

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

Katika hatua hii, tunagawanya prompt ya kuingiza na kuandaa kwa uhakiki kwa kuibadilisha kuwa mfuatano wa tokeni za kitambulisho. Pia tunaanzisha thamani za `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Kila tokeni hubadilishwa kuwa tensor na kupitishwa kwenye modeli kupata logits.

Mzunguko huu unashughulikia kila tokeni kwenye prompt, ukiboresha processor ya logits na kuandaa kwa ajili ya uzalishaji wa tokeni inayofuata.

## Hatua ya 6: Uhakiki

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

Katika mzunguko wa uhakiki, tunazalisha tokeni moja baada ya nyingine hadi tufikie urefu wa sampuli uliohitajika au tukutane na tokeni ya mwisho wa mfuatano. Tokeni inayofuata hubadilishwa kuwa tensor na kupitishwa kwenye modeli, wakati logits zinashughulikiwa ili kuweka adhabu na sampuli. Kisha tokeni inayofuata huchaguliwa, kutafsiriwa, na kuongezwa kwenye mfuatano.
Ili kuepuka maandishi yanayojirudia, adhabu hutolewa kwa tokeni zinazojirudia kulingana na vigezo vya `repeat_last_n` and `repeat_penalty`.

Mwishowe, maandishi yaliyotengenezwa yamechapishwa kadri yanavyotafsiriwa, kuhakikisha utoaji wa moja kwa moja wa matokeo kwa wakati halisi.

## Hatua ya 7: Endesha Programu

Ili kuendesha programu, fanya amri ifuatayo kwenye terminal:

```bash
cargo run --release
```

Hii inapaswa kuchapisha haiku kuhusu ice hockey iliyozalishwa na modeli ya Phi-3. Kitu kama:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

au

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Hitimisho

Kwa kufuata hatua hizi, tunaweza kufanya uzalishaji wa maandishi kwa kutumia modeli ya Phi-3 kwa Rust na Candle chini ya mistari 100 ya msimbo. Msimbo unashughulikia upakiaji wa modeli, kugawanya maandishi, na uhakiki, ukitumia tensors na usindikaji wa logits kuunda maandishi yanayoeleweka kulingana na prompt ya kuingiza.

Programu hii ya console inaweza kuendeshwa kwenye Windows, Linux na Mac OS. Kutokana na usafirishaji wa Rust, msimbo pia unaweza kubadilishwa kuwa maktaba ambayo ingeweza kuendeshwa ndani ya programu za simu (hatuwezi kuendesha programu za console huko, baada ya yote).

## Kiambatisho: msimbo kamili

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

Kumbuka: ili kuendesha msimbo huu kwenye aarch64 Linux au aarch64 Windows, ongeza faili liitwalo `.cargo/config` lenye maudhui ifuatayo:

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

> Unaweza kutembelea hifadhidata rasmi ya [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) kwa mifano zaidi jinsi ya kutumia modeli ya Phi-3 kwa Rust na Candle, pamoja na mbinu mbadala za uhakiki.

**Kiasi cha Majadiliano**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya mtaalamu wa kibinadamu inapendekezwa. Hatubeba jukumu lolote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.