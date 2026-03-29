# AGENTS.md

## プロジェクト概要

PhiCookBookは、MicrosoftのPhiファミリーのスモールランゲージモデル（SLM）を扱うための実践的な例、チュートリアル、ドキュメントをまとめた総合的なクックブックリポジトリです。本リポジトリでは、推論、ファインチューニング、量子化、RAG実装、マルチモーダルアプリケーションなど、さまざまなプラットフォームとフレームワークを跨いだユースケースを示しています。

**主要技術:**
- **言語:** Python、C#/.NET、JavaScript/Node.js
- **フレームワーク:** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **プラットフォーム:** Microsoft Foundry、GitHub Models、Hugging Face、Ollama
- **モデルタイプ:** Phi-3、Phi-3.5、Phi-4（テキスト、ビジョン、マルチモーダル、推論バリアント）

**リポジトリ構成:**
- `/code/` - 実用的なコード例とサンプル実装
- `/md/` - 詳細なドキュメント、チュートリアル、ハウツーガイド  
- `/translations/` - 多言語翻訳（自動化ワークフローによる50以上の言語）
- `/.devcontainer/` - 開発コンテナ設定（Python 3.12＋Ollama）

## 開発環境のセットアップ

### GitHub CodespacesまたはDev Containersの使用（推奨）

1. GitHub Codespacesで開く（最速）:
   - READMEの「Open in GitHub Codespaces」バッジをクリック
   - Python 3.12 とPhi-3搭載Ollamaコンテナが自動構成されます

2. VS Code Dev Containersで開く:
   - READMEの「Open in Dev Containers」バッジを使用
   - ホストに最低16GBのメモリが必要です

### ローカルセットアップ

**前提条件:**
- Python 3.12以降
- .NET 8.0 SDK（C#例用）
- Node.js 18以上とnpm（JavaScript例用）
- 16GB以上のRAM推奨

**インストール:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python例の場合:**
各例ディレクトリに移動して依存パッケージをインストールしてください:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # requirements.txt が存在する場合
```

**.NET例の場合:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/ウェブ例の場合:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 開発サーバーを起動する
npm run build  # 本番用にビルドする
```

## リポジトリの構成

### コード例（`/code/`）

- **01.Introduce/** - 基本的な紹介と入門サンプル
- **03.Finetuning/** と **04.Finetuning/** - 様々な手法によるファインチューニング例
- **03.Inference/** - 各種ハードウェア（AIPC、MLX）での推論例
- **06.E2E/** - エンドツーエンドのアプリケーションサンプル
- **07.Lab/** - ラボ/実験的実装
- **08.RAG/** - 検索強化生成（RAG）サンプル
- **09.UpdateSamples/** - 最新の更新済みサンプル

### ドキュメント（`/md/`）

- **01.Introduction/** - 入門ガイド、環境セットアップ、プラットフォームガイド
- **02.Application/** - 種類別のアプリケーションサンプル（テキスト、コード、ビジョン、オーディオ等）
- **02.QuickStart/** - Microsoft Foundry及びGitHub Modelsのクイックスタートガイド
- **03.FineTuning/** - ファインチューニングのドキュメントとチュートリアル
- **04.HOL/** - ハンズオンラボ（.NET例含む）

### ファイル形式

- **Jupyterノートブック（`.ipynb`）** - インタラクティブPythonチュートリアル、READMEに📓マークあり
- **Pythonスクリプト（`.py`）** - 単独で動くPython例
- **C#プロジェクト（`.csproj`, `.sln`）** - .NETアプリケーションとサンプル
- **JavaScript（`.js`, `package.json`）** - Webベース、Node.js例
- **Markdown（`.md`）** - ドキュメントとガイド

## 例の実行方法

### Jupyterノートブックの実行

ほとんどの例はJupyterノートブック形式で提供されています:
```bash
pip install jupyter notebook
jupyter notebook  # ブラウザインターフェースを開きます
# 希望の .ipynb ファイルに移動します
```

### Pythonスクリプトの実行

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET例の実行

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

またはソリューション全体のビルド:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/ウェブ例の実行

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ホットリロードによる開発
```

## テスト

本リポジトリはユニットテストではなくサンプルコードとチュートリアルの集合です。検証は通常以下で行います:

1. <strong>例を実行すること</strong> - 各例がエラーなく動作すること
2. <strong>出力の確認</strong> - モデル応答が適切であることを確認
3. <strong>チュートリアルに従うこと</strong> - 手順どおりに動作することを確認

**一般的な検証方法:**
- 対象環境で例の実行テスト
- 依存関係が正しくインストールされることを確認
- モデルのダウンロード/読み込みが成功することをチェック
- 期待動作がドキュメントと一致することを確かめる

## コードスタイルと規約

### 一般的な指針

- 例は分かりやすく、コメント付きで教育的に
- 言語固有の標準に従う（PythonはPEP 8、.NETはC#標準など）
- Phiモデルの特定機能を示すことに集中する
- 主要な概念やモデル固有パラメータをコメントで説明

### ドキュメント基準

**URLフォーマット:**
- `[text](../../url)`形式で空白なし
- 相対リンクは `./`（現ディレクトリ）、`../`（親ディレクトリ）使用
- URL内に国別ロケールを含めない（`/en-us/`, `/en/`等を避ける）

**画像:**
- すべての画像は `/imgs/` ディレクトリに保存
- 英数字とダッシュを用いた説明的な名前をつける
- 例: `phi-3-architecture.png`

**Markdownファイル:**
- 実際に動作する例は必ず `/code/` を参照
- ドキュメントをコード変更と同期
- README内のJupyterノートブックリンクに📓絵文字を使用

### ファイル整理

- `/code/`に機能・トピック別にコード例を整理
- `/md/`は可能な限りコード構成に同期させる
- 関連ファイル（ノートブック、スクリプト、設定）はサブディレクトリにまとめる

## プルリクエストガイドライン

### 提出前に

1. <strong>リポジトリをフォーク</strong>し、自分のアカウントで作業
2. **PRはタイプ別に分ける**:
   - バグ修正は別PRに
   - ドキュメント更新は別PRに
   - 新規例はそれぞれ別PRに
   - タイポ修正はまとめても良い

3. **マージコンフリクトの対処:**
   - 変更前にローカルの`main`を最新に更新
   - 頻繁にアップストリームと同期

4. **翻訳PRの場合:**
   - フォルダ内のすべてのファイルに翻訳が含まれていること
   - 元言語と構造を一貫して保つ

### 必須チェック

PRはGitHubワークフローで自動検証されます:

1. <strong>相対パスの検証</strong> - すべての内部リンクが機能していること
   - ローカルでVS CodeのCtrl+クリックでテスト可能
   - VS Codeのパス提案（`./`や`../`）を利用

2. **URLロケールチェック** - Web URLに国別ロケールが入っていないこと
   - `/en-us/`や`/en/`など言語コードを除去
   - 国際的な汎用URLを用いる

3. **壊れたURLチェック** - すべてのURLがステータス200を返すこと
   - 提出前にリンクの到達性を確認
   - 一部の失敗はネットワーク制限による場合あり

### PRタイトル形式

```
[component] Brief description
```

例:
- `[docs] Phi-4推論チュートリアル追加`
- `[code] ONNX Runtime統合例の修正`
- `[translation] 入門ガイドの日本語翻訳追加`

## 一般的な開発パターン

### Phiモデルの利用

**モデル読み込み:**
- Transformers、ONNX Runtime、MLX、OpenVINOなど多様なフレームワーク例あり
- モデルは主にHugging Face、Azure、GitHub Modelsからダウンロード
- ハードウェアとの互換性を確認（CPU、GPU、NPU）

**推論パターン:**
- テキスト生成：多くの例はチャット/指示型バリアントを使用
- ビジョン：Phi-3-visionおよびPhi-4-multimodalを画像理解に利用
- オーディオ：Phi-4-multimodalは音声入力対応
- 推論：Phi-4-reasoningバリアントは高度な推論用途

### プラットフォーム別の注意点

**Microsoft Foundry:**
- AzureサブスクリプションとAPIキーが必要
- `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`を参照

**GitHub Models:**
- テスト用に無料枠あり
- `/md/02.QuickStart/GitHubModel_QuickStart.md`を参照

**ローカル推論:**
- ONNX Runtime：クロスプラットフォーム、高速推論
- Ollama：ローカルモデル管理が容易（devコンテナにプリセット）
- Apple MLX：Apple Silicon最適化

## トラブルシューティング

### よくある問題

**メモリ問題:**
- Phiモデルは特にビジョン・マルチモーダルで大量のRAMを要する
- リソース制約環境では量子化モデルの利用推奨
- `/md/01.Introduction/04/QuantifyingPhi.md`を参照

**依存関係の競合:**
- Python例では特定バージョンを要求する場合あり
- 各例で仮想環境使用を推奨
- 個別の`requirements.txt`も参照

**モデルダウンロード失敗:**
- 大規模モデルは低速接続でタイムアウトすることがある
- クラウド環境（Codespaces、Azure）の利用を検討
- Hugging Faceキャッシュは`~/.cache/huggingface/`

**.NETプロジェクト問題:**
- .NET 8.0 SDKがインストールされていることを確認
- ビルド前に`dotnet restore`を実行
- 一部はCUDA専用設定あり（Debug_Cuda）

**JavaScript/ウェブ例:**
- Node.js 18以上の利用推奨
- 問題発生時は`node_modules`をクリアして再インストール
- WebGPUの互換性はブラウザコンソールで確認

### サポートを得るには

- **Discord:** Microsoft Foundry Community Discordに参加
- **GitHub Issues:** バグ報告や問題報告を行う
- **GitHub Discussions:** 質問や知識共有の場

## 追加情報

### 責任あるAI

すべてのPhiモデル利用はMicrosoftの責任あるAI原則に準拠:
- 公正性、信頼性、安全性
- プライバシーとセキュリティ  
- 包摂性、透明性、説明責任
- 本番環境にはAzure AI Content Safetyを利用推奨
- `/md/01.Introduction/01/01.AISafety.md`を参照

### 翻訳

- 自動GitHub Actionによる50以上の言語対応
- 翻訳ファイルは`/translations/`に格納
- co-op-translatorワークフローで管理
- 翻訳ファイルを手動編集しないでください（自動生成）

### コントリビューティング

- `CONTRIBUTING.md`のガイドラインに従うこと
- Contributor License Agreement（CLA）に同意すること
- Microsoft Open Source Code of Conductに準拠
- セキュリティ情報や資格情報はコミットに含めない

### 多言語サポート

当リポジトリは複数言語での例を含みます:
- **Python** - ML/AIワークフロー、Jupyterノートブック、ファインチューニング
- **C#/.NET** - エンタープライズアプリケーション、ONNX Runtime統合
- **JavaScript** - WebベースAI、ブラウザ推論（WebGPU）

用途と展開先に最適な言語を選択してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性の確保に努めていますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の母国語版が正式な情報源として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤訳に関して、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->