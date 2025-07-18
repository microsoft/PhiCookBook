<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:32:32+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "sw"
}
-->
# Utabiri wa mtandao wa majukwaa mbalimbali kwa kutumia Rust

Mafunzo haya yatatuongoza kupitia mchakato wa kufanya utabiri kwa kutumia Rust na [mfumo wa Candle ML](https://github.com/huggingface/candle) kutoka HuggingFace. Kutumia Rust kwa utabiri kuna faida kadhaa, hasa ikilinganishwa na lugha nyingine za programu. Rust inajulikana kwa utendaji wake wa juu, unaolingana na ule wa C na C++. Hii inafanya kuwa chaguo bora kwa kazi za utabiri, ambazo zinaweza kuwa na mzigo mkubwa wa kihesabu. Hii hasa inatokana na utofauti wa gharama sifuri na usimamizi mzuri wa kumbukumbu, ambao hauhusishi mzigo wa ukusanyaji taka. Uwezo wa Rust wa kuendeshwa kwenye majukwaa mbalimbali unaruhusu maendeleo ya msimbo unaoweza kuendeshwa kwenye mifumo mbalimbali ya uendeshaji, ikiwa ni pamoja na Windows, macOS, na Linux, pamoja na mifumo ya uendeshaji ya simu, bila mabadiliko makubwa kwenye msimbo.

Sharti la kufuata mafunzo haya ni [kusakinisha Rust](https://www.rust-lang.org/tools/install), ambayo inajumuisha mkusanyaji wa Rust na Cargo, meneja wa vifurushi vya Rust.

## Hatua ya 1: Unda Mradi Mpya wa Rust

Ili kuunda mradi mpya wa Rust, tumia amri ifuatayo kwenye terminal:

```bash
cargo new phi-console-app
```

Hii itaunda muundo wa awali wa mradi wenye faili `Cargo.toml` na saraka ya `src` yenye faili `main.rs`.

Ifuatayo, tutaongeza utegemezi wetu - yaani crates `candle`, `hf-hub` na `tokenizers` - kwenye faili `Cargo.toml`:

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

Ndani ya faili `main.rs`, tutaweka vigezo vya awali kwa ajili ya utabiri wetu. Vyote vitakuwa vimeandikwa moja kwa moja kwa urahisi, lakini tunaweza kubadilisha kama inavyohitajika.

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

- **temperature**: Hudhibiti nasibu ya mchakato wa sampuli.
- **sample_len**: Inaeleza urefu wa juu wa maandishi yatakayozalishwa.
- **top_p**: Inatumika kwa sampuli ya nyuklia ili kupunguza idadi ya tokeni zinazochukuliwa kwa kila hatua.
- **repeat_last_n**: Hudhibiti idadi ya tokeni zinazochukuliwa kwa ajili ya kuweka adhabu ili kuzuia mfululizo wa kurudiwa.
- **repeat_penalty**: Thamani ya adhabu ili kuzuia tokeni kurudiwa.
- **seed**: Mchepuo wa nasibu (tunaweza kutumia thamani thabiti kwa urudufu bora).
- **prompt**: Maandishi ya awali ya kuanzisha uzalishaji. Angalia kwamba tunaomba mfano uzalishe haiku kuhusu ice hockey, na tunazizunguka na tokeni maalum kuonyesha sehemu za mtumiaji na msaidizi wa mazungumzo. Mfano kisha utakamilisha prompt na haiku.
- **device**: Tunatumia CPU kwa ajili ya hesabu katika mfano huu. Candle pia inaunga mkono kuendesha kwenye GPU kwa CUDA na Metal.

## Hatua ya 3: Pakua/Tayarisha Mfano na Tokenizer

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

Tunatumia API ya `hf_hub` kupakua faili za mfano na tokenizer kutoka kwenye hifadhi ya mfano ya Hugging Face. Faili la `gguf` lina uzito wa mfano uliopimwa, wakati faili la `tokenizer.json` linatumika kwa tokenizing ya maandishi yetu ya ingizo. Baada ya kupakuliwa, mfano huhifadhiwa kwenye cache, hivyo utekelezaji wa kwanza utakuwa polepole (kwa sababu unapakua GB 2.4 za mfano) lakini utekelezaji unaofuata utakuwa haraka zaidi.

## Hatua ya 4: Pakia Mfano

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Tunapakia uzito wa mfano uliopimwa kwenye kumbukumbu na kuanzisha mfano wa Phi-3. Hatua hii inahusisha kusoma uzito wa mfano kutoka faili la `gguf` na kuandaa mfano kwa ajili ya utabiri kwenye kifaa kilichobainishwa (CPU katika kesi hii).

## Hatua ya 5: Chakata Prompt na Andaa kwa Utabiri

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

Katika hatua hii, tunafanya tokenizing ya prompt ya ingizo na kuandaa kwa utabiri kwa kuibadilisha kuwa mfuatano wa vitambulisho vya tokeni. Pia tunaanzisha `LogitsProcessor` kushughulikia mchakato wa sampuli (mgawanyo wa uwezekano juu ya msamiati) kulingana na thamani za `temperature` na `top_p` zilizotolewa. Kila tokeni hubadilishwa kuwa tensor na kupitishwa kwenye mfano kupata logits.

Mzunguko unashughulikia kila tokeni katika prompt, ukiboresha processor ya logits na kuandaa uzalishaji wa tokeni inayofuata.

## Hatua ya 6: Utabiri

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

Katika mzunguko wa utabiri, tunazalisha tokeni moja baada ya nyingine hadi tufikie urefu wa sampuli unaotakiwa au tukutane na tokeni ya mwisho wa mfuatano. Tokeni inayofuata hubadilishwa kuwa tensor na kupitishwa kwenye mfano, wakati logits zinashughulikiwa ili kutumia adhabu na sampuli. Kisha tokeni inayofuata huchaguliwa, kutafsiriwa, na kuongezwa kwenye mfuatano.
Ili kuepuka maandishi yanayojirudia, adhabu hutumika kwa tokeni zinazojirudia kulingana na vigezo vya `repeat_last_n` na `repeat_penalty`.

Mwishowe, maandishi yaliyotengenezwa yachapishwe wakati yanapotafsiriwa, kuhakikisha utoaji wa moja kwa moja wa matokeo kwa wakati halisi.

## Hatua ya 7: Endesha Programu

Ili kuendesha programu, tumia amri ifuatayo kwenye terminal:

```bash
cargo run --release
```

Hii inapaswa kuchapisha haiku kuhusu ice hockey iliyozalishwa na mfano wa Phi-3. Kitu kama:

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

Kwa kufuata hatua hizi, tunaweza kufanya uzalishaji wa maandishi kwa kutumia mfano wa Phi-3 kwa Rust na Candle chini ya mistari 100 ya msimbo. Msimbo unashughulikia upakiaji wa mfano, tokenizing, na utabiri, ukitumia tensors na usindikaji wa logits kuzalisha maandishi yenye muktadha kulingana na prompt ya ingizo.

Programu hii ya console inaweza kuendeshwa kwenye Windows, Linux na Mac OS. Kwa sababu ya uhamaji wa Rust, msimbo pia unaweza kubadilishwa kuwa maktaba itakayoweza kuendeshwa ndani ya programu za simu (hatuwezi kuendesha programu za console hapo, kwa kweli).

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

Kumbuka: ili kuendesha msimbo huu kwenye aarch64 Linux au aarch64 Windows, ongeza faili liitwalo `.cargo/config` lenye maudhui yafuatayo:

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

> Unaweza kutembelea hifadhi rasmi ya [mifano ya Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) kwa mifano zaidi ya jinsi ya kutumia mfano wa Phi-3 kwa Rust na Candle, ikiwa ni pamoja na mbinu mbadala za utabiri.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.