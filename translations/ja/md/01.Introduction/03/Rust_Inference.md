<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-05-08T06:03:10+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ja"
}
-->
# Rustによるクロスプラットフォーム推論

このチュートリアルでは、RustとHuggingFaceの[Candle MLフレームワーク](https://github.com/huggingface/candle)を使った推論の方法を紹介します。Rustを推論に使うことにはいくつかの利点があり、特に他のプログラミング言語と比較した場合に際立ちます。RustはCやC++に匹敵する高いパフォーマンスで知られており、計算負荷の高い推論タスクに非常に適しています。特に、ゼロコスト抽象化や効率的なメモリ管理（ガベージコレクションのオーバーヘッドがない）がその理由です。Rustのクロスプラットフォーム対応により、Windows、macOS、Linuxだけでなく、モバイルOS上でも大きなコード変更なしに動作するコードを開発できます。

このチュートリアルを進めるには、RustコンパイラとパッケージマネージャCargoを含む[Rustのインストール](https://www.rust-lang.org/tools/install)が必要です。

## ステップ1: 新しいRustプロジェクトの作成

新しいRustプロジェクトを作成するには、ターミナルで以下のコマンドを実行します：

```bash
cargo new phi-console-app
```

これにより、`Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ファイルを含む初期プロジェクト構成が生成されます：

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

## ステップ2: 基本パラメータの設定

`main.rs` ファイル内で推論の初期パラメータを設定します。簡単のために全てハードコードしますが、必要に応じて変更可能です。

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

- **temperature**: サンプリングのランダム性を制御します。
- **sample_len**: 生成されるテキストの最大長を指定します。
- **top_p**: ニュークリアスサンプリングで、各ステップで考慮するトークン数を制限します。
- **repeat_last_n**: 繰り返しを防ぐためにペナルティを適用する際に考慮するトークン数を制御します。
- **repeat_penalty**: 繰り返しトークンを抑制するためのペナルティ値です。
- **seed**: ランダムシード（再現性を高めるために定数値を使うこともできます）。
- **prompt**: 生成開始のための初期プロンプトテキスト。ここではアイスホッケーについての俳句を生成するようモデルに指示しており、会話のユーザーとアシスタント部分を示す特別なトークンで囲んでいます。モデルはこのプロンプトを基に俳句を完成させます。
- **device**: この例ではCPUを使っています。CandleはCUDAやMetalを使ったGPU実行もサポートしています。

## ステップ3: モデルとトークナイザーのダウンロード／準備

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

`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` ファイルは入力テキストのトークナイズに使います。モデルは一度ダウンロードされるとキャッシュされるため、最初の実行は遅く（モデルサイズは2.4GB）、その後の実行は速くなります。

## ステップ4: モデルの読み込み

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

量子化されたモデルの重みをメモリに読み込み、Phi-3モデルを初期化します。このステップでは`gguf`ファイルからモデルの重みを読み込み、指定したデバイス（ここではCPU）で推論できるようにモデルをセットアップします。

## ステップ5: プロンプトの処理と推論準備

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

このステップでは、入力プロンプトをトークナイズし、トークンIDのシーケンスに変換して推論準備をします。また、`LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` の値を初期化します。各トークンはテンソルに変換され、モデルを通してロジットを取得します。

ループではプロンプト内の各トークンを処理し、ロジットプロセッサを更新しながら次のトークン生成の準備を進めます。

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

推論ループでは、指定した最大長に達するか終端トークンが出るまで、トークンを一つずつ生成します。次のトークンはテンソルに変換されモデルに入力され、ロジットはペナルティやサンプリング処理を受けます。その後、次のトークンがサンプリングされデコードされてシーケンスに追加されます。

繰り返しを避けるために、`repeat_last_n` and `repeat_penalty` のパラメータに基づき繰り返しトークンにペナルティが適用されます。

生成されたテキストはデコードされるたびに出力され、リアルタイムにストリーム表示されます。

## ステップ7: アプリケーションの実行

アプリケーションを実行するには、ターミナルで以下のコマンドを実行します：

```bash
cargo run --release
```

Phi-3モデルによって生成されたアイスホッケーの俳句が表示されるはずです。例えば：

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

これらのステップに従うことで、RustとCandleを使い100行未満のコードでPhi-3モデルによるテキスト生成を実現できます。コードはモデルの読み込み、トークナイズ、推論を処理し、テンソルとロジット処理を活用して入力プロンプトに基づく一貫したテキストを生成します。

このコンソールアプリケーションはWindows、Linux、Mac OSで動作します。Rustの移植性のおかげで、モバイルアプリ内で動作するライブラリにコードを適応することも可能です（コンソールアプリはモバイル上では動かせませんが）。

## 付録: 全コード

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

注意: aarch64 Linuxまたはaarch64 Windowsでこのコードを実行するには、以下の内容の`.cargo/config`ファイルを追加してください：

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

> Phi-3モデルをRustとCandleで使う方法や、推論の別のアプローチなど、より多くの例については公式の[Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)リポジトリをご覧ください。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の言語による文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。