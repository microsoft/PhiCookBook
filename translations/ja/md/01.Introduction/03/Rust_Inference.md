<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a7ad026d880c666db9739a17a2eb400",
  "translation_date": "2025-07-16T21:26:28+00:00",
  "source_file": "md/01.Introduction/03/Rust_Inference.md",
  "language_code": "ja"
}
-->
# Rustによるクロスプラットフォーム推論

このチュートリアルでは、RustとHuggingFaceの[Candle MLフレームワーク](https://github.com/huggingface/candle)を使って推論を行う方法を紹介します。Rustを推論に使うことにはいくつかの利点があり、特に他のプログラミング言語と比べて優れています。RustはCやC++に匹敵する高いパフォーマンスで知られており、計算負荷の高い推論タスクに最適です。これは、ゼロコスト抽象化や効率的なメモリ管理（ガベージコレクションのオーバーヘッドがない）によって実現されています。さらに、Rustのクロスプラットフォーム対応により、Windows、macOS、LinuxだけでなくモバイルOS上でも、コードベースを大きく変えずに動作するコードを開発できます。

このチュートリアルを進めるには、RustコンパイラとパッケージマネージャであるCargoを含む[Rustのインストール](https://www.rust-lang.org/tools/install)が必要です。

## ステップ1: 新しいRustプロジェクトの作成

新しいRustプロジェクトを作成するには、ターミナルで以下のコマンドを実行します。

```bash
cargo new phi-console-app
```

これにより、`Cargo.toml`ファイルと`src`ディレクトリ内の`main.rs`ファイルを含む初期プロジェクト構造が生成されます。

次に、依存関係として`candle`、`hf-hub`、`tokenizers`クレートを`Cargo.toml`ファイルに追加します。

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

`main.rs`ファイル内で推論の初期パラメータを設定します。簡単のためすべてハードコードしていますが、必要に応じて変更可能です。

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
- **repeat_last_n**: 繰り返しを防ぐためにペナルティを適用する際に考慮する直近のトークン数を制御します。
- **repeat_penalty**: 繰り返しトークンを抑制するためのペナルティ値です。
- **seed**: ランダムシード（再現性を高めるために定数値を使うことも可能です）。
- **prompt**: 生成開始のための初期プロンプトテキスト。ここではアイスホッケーに関する俳句を生成するようモデルに指示し、会話のユーザーとアシスタント部分を示す特殊トークンで囲んでいます。モデルはこのプロンプトを元に俳句を完成させます。
- **device**: この例ではCPUを使用しています。CandleはCUDAやMetalを使ったGPU実行もサポートしています。

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

`hf_hub` APIを使ってHugging Faceのモデルハブからモデルとトークナイザーファイルをダウンロードします。`gguf`ファイルには量子化されたモデルの重みが含まれ、`tokenizer.json`ファイルは入力テキストのトークナイズに使います。ダウンロード後はモデルがキャッシュされるため、初回実行は2.4GBのモデルをダウンロードするため遅くなりますが、以降の実行は高速になります。

## ステップ4: モデルの読み込み

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

量子化されたモデルの重みをメモリに読み込み、Phi-3モデルを初期化します。このステップでは`gguf`ファイルからモデル重みを読み込み、指定したデバイス（ここではCPU）で推論できるようにモデルをセットアップします。

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

このステップでは、入力プロンプトをトークナイズし、トークンIDのシーケンスに変換して推論準備を行います。また、`LogitsProcessor`を初期化し、与えられた`temperature`と`top_p`の値に基づいてサンプリング処理（語彙上の確率分布）を制御します。各トークンはテンソルに変換され、モデルに渡されてロジットを取得します。

ループはプロンプト内の各トークンを処理し、ロジットプロセッサを更新しながら次のトークン生成の準備を進めます。

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

推論ループでは、指定したサンプル長に達するか終端トークンに到達するまでトークンを1つずつ生成します。次のトークンはテンソルに変換されモデルに渡され、ロジットはペナルティやサンプリング処理を受けます。その後、次のトークンがサンプリングされデコードされてシーケンスに追加されます。
繰り返しテキストを避けるため、`repeat_last_n`と`repeat_penalty`のパラメータに基づいて繰り返しトークンにペナルティが適用されます。

最後に、生成されたテキストはデコードされるたびにリアルタイムでストリーム出力されます。

## ステップ7: アプリケーションの実行

アプリケーションを実行するには、ターミナルで以下のコマンドを実行します。

```bash
cargo run --release
```

これにより、Phi-3モデルが生成したアイスホッケーに関する俳句が表示されます。例えば：

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

## まとめ

これらの手順に従うことで、RustとCandleを使ってPhi-3モデルによるテキスト生成を100行未満のコードで実現できます。コードはモデルの読み込み、トークナイズ、推論を扱い、テンソルとロジット処理を活用して入力プロンプトに基づいた一貫性のあるテキストを生成します。

このコンソールアプリケーションはWindows、Linux、Mac OSで動作します。Rustの移植性により、モバイルアプリ内で動作するライブラリにコードを適応することも可能です（コンソールアプリはモバイル上では動作しませんが）。

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

注意: aarch64 Linuxやaarch64 Windowsでこのコードを実行するには、以下の内容の`.cargo/config`ファイルを追加してください。

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

> RustとCandleでPhi-3モデルを使う方法や推論の別アプローチを含む、より多くの例については公式の[Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)リポジトリをご覧ください。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。