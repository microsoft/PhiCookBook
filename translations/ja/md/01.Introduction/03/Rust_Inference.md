<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2fa1ead890e358cc560ed4f9b3cf219a",
  "translation_date": "2025-04-04T12:10:03+00:00",
  "source_file": "md\\01.Introduction\\03\\Rust_Inference.md",
  "language_code": "ja"
}
-->
# Rustでクロスプラットフォームの推論

このチュートリアルでは、HuggingFaceの[Candle MLフレームワーク](https://github.com/huggingface/candle)を使用してRustで推論を行う手順を説明します。Rustを使用した推論には、特に他のプログラミング言語と比較していくつかの利点があります。Rustは高いパフォーマンスで知られており、CやC++に匹敵する性能を持っています。これは計算負荷の高い推論タスクに非常に適しています。特に、ゼロコスト抽象化や効率的なメモリ管理によって、ガベージコレクションのオーバーヘッドがないことが大きな要因です。また、Rustのクロスプラットフォーム機能により、Windows、macOS、Linux、さらにはモバイルOSを含むさまざまなオペレーティングシステムで、コードベースに大きな変更を加えることなく動作するコードを開発することができます。

このチュートリアルを進める前提条件として、[Rustのインストール](https://www.rust-lang.org/tools/install)が必要です。これにはRustコンパイラとCargo（Rustのパッケージマネージャ）が含まれます。

## ステップ1: 新しいRustプロジェクトを作成

新しいRustプロジェクトを作成するには、ターミナルで以下のコマンドを実行します:

```bash
cargo new phi-console-app
```

これにより、`Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`ファイルを含む初期プロジェクト構造が生成されます:

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

## ステップ2: 基本パラメータを設定

main.rsファイル内で、推論の初期パラメータを設定します。これらは簡単さを優先してハードコーディングされますが、必要に応じて変更可能です。

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

- **temperature**: サンプリングプロセスのランダム性を制御します。
- **sample_len**: 生成されるテキストの最大長を指定します。
- **top_p**: ヌクレアスサンプリングに使用され、各ステップで考慮されるトークンの数を制限します。
- **repeat_last_n**: 繰り返しを防ぐためのペナルティを適用する際に考慮されるトークン数を制御します。
- **repeat_penalty**: 繰り返しトークンを抑制するためのペナルティ値。
- **seed**: ランダムシード（再現性を高めるために一定値を使用することができます）。
- **prompt**: テキスト生成を開始するための初期プロンプト。今回はアイスホッケーに関する俳句を生成するようモデルに依頼し、会話のユーザーとアシスタント部分を示す特別なトークンでラップしています。モデルはプロンプトを基に俳句を完成させます。
- **device**: この例ではCPUを使用します。CandleはCUDAやMetalを使用したGPUでの実行もサポートしています。

## ステップ3: モデルとトークナイザーをダウンロード/準備

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

入力テキストのトークナイズには`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json`ファイルを使用します。モデルをダウンロードするとキャッシュされるため、初回実行は遅く（モデルの2.4GBをダウンロードするため）なりますが、2回目以降の実行は高速になります。

## ステップ4: モデルをロード

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

量子化されたモデルの重みをメモリにロードし、Phi-3モデルを初期化します。このステップでは、`gguf`ファイルからモデルの重みを読み取り、指定されたデバイス（この場合はCPU）での推論に向けてモデルを設定します。

## ステップ5: プロンプトを処理して推論の準備をする

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

このステップでは、入力プロンプトをトークナイズし、トークンIDのシーケンスに変換して推論の準備をします。また、`LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`値を初期化します。各トークンはテンソルに変換され、モデルを通してロジットを取得します。

ループ内では、プロンプト内の各トークンを処理し、ロジットプロセッサを更新し、次のトークン生成の準備をします。

## ステップ6: 推論

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

推論ループでは、指定されたサンプル長に到達するか、終了トークンに出会うまで、トークンを1つずつ生成します。次のトークンはテンソルに変換され、モデルを通して処理されます。一方で、ロジットにはペナルティやサンプリングが適用されます。そして次のトークンがサンプリングされ、デコードされ、シーケンスに追加されます。

繰り返しを防ぐため、`repeat_last_n` and `repeat_penalty`パラメータに基づいて繰り返しトークンにペナルティが適用されます。

最後に、生成されたテキストがデコードされ、ストリーム形式でリアルタイム出力として表示されます。

## ステップ7: アプリケーションを実行する

アプリケーションを実行するには、ターミナルで以下のコマンドを実行します:

```bash
cargo run --release
```

これにより、Phi-3モデルによって生成されたアイスホッケーに関する俳句が表示されます。例えば:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

または

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 結論

これらの手順を実行することで、Phi-3モデルを使用してRustとCandleでテキスト生成を100行未満のコードで行うことができます。このコードは、モデルのロード、トークナイズ、推論を処理し、テンソルとロジット処理を活用して入力プロンプトに基づいた整合性のあるテキストを生成します。

このコンソールアプリケーションはWindows、Linux、Mac OSで実行できます。Rustの移植性により、コードをライブラリとして適応させることで、モバイルアプリ内でも動作させることが可能です（コンソールアプリはモバイルでは実行できませんが）。

## 付録: 完全なコード

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

注: aarch64 Linuxまたはaarch64 Windowsでこのコードを実行するには、`.cargo/config`という名前のファイルを作成し、以下の内容を追加してください:

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

> 公式の[Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)リポジトリを訪れることで、RustとCandleを使用したPhi-3モデルの利用方法に関するその他の例や、推論への代替アプローチを確認することができます。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の文書（原文）を信頼できる情報源としてご利用ください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の利用によって生じた誤解や誤訳について、当社は一切責任を負いません。