# AGENTS.md

## プロジェクト概要

PhiCookBookは、MicrosoftのPhiファミリーの小型言語モデル（SLM）を活用するための実践的な例、チュートリアル、ドキュメントを含む包括的なレシピ集です。このリポジトリでは、推論、微調整、量子化、RAG実装、マルチモーダルアプリケーションなど、さまざまなプラットフォームやフレームワークでの利用例を示しています。

**主要技術:**
- **言語:** Python, C#/.NET, JavaScript/Node.js
- **フレームワーク:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **プラットフォーム:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **モデルタイプ:** Phi-3, Phi-3.5, Phi-4（テキスト、ビジョン、マルチモーダル、推論バリアント）

**リポジトリ構成:**
- `/code/` - 実際に動作するコード例とサンプル実装
- `/md/` - 詳細なドキュメント、チュートリアル、ハウツーガイド  
- `/translations/` - 自動化ワークフローによる多言語翻訳（50以上の言語）
- `/.devcontainer/` - 開発コンテナ構成（Python 3.12とOllama）

## 開発環境のセットアップ

### GitHub CodespacesまたはDev Containersの使用（推奨）

1. GitHub Codespacesで開く（最速）:
   - READMEの「Open in GitHub Codespaces」バッジをクリック
   - コンテナがPython 3.12とPhi-3を備えたOllamaで自動設定されます

2. VS Code Dev Containersで開く:
   - READMEの「Open in Dev Containers」バッジを使用
   - コンテナには最低16GBのホストメモリが必要です

### ローカルセットアップ

**前提条件:**
- Python 3.12以降
- .NET 8.0 SDK（C#の例用）
- Node.js 18以上とnpm（JavaScriptの例用）
- 最低16GB RAM推奨

**インストール:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pythonの例の場合:**
特定の例のディレクトリに移動し、依存関係をインストールします:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NETの例の場合:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Webの例の場合:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## リポジトリの構成

### コード例 (`/code/`)

- **01.Introduce/** - 基本的な紹介と開始サンプル
- **03.Finetuning/** および **04.Finetuning/** - さまざまな方法による微調整例
- **03.Inference/** - 異なるハードウェア（AIPC、MLX）での推論例
- **06.E2E/** - エンドツーエンドのアプリケーションサンプル
- **07.Lab/** - 実験的な実装
- **08.RAG/** - 検索強化生成（RAG）のサンプル
- **09.UpdateSamples/** - 最新の更新サンプル

### ドキュメント (`/md/`)

- **01.Introduction/** - 導入ガイド、環境設定、プラットフォームガイド
- **02.Application/** - テキスト、コード、ビジョン、オーディオなどのタイプ別に整理されたアプリケーションサンプル
- **02.QuickStart/** - Azure AI FoundryとGitHub Modelsのクイックスタートガイド
- **03.FineTuning/** - 微調整のドキュメントとチュートリアル
- **04.HOL/** - ハンズオンラボ（.NETの例を含む）

### ファイル形式

- **Jupyterノートブック (`.ipynb`)** - READMEで📓でマークされたインタラクティブなPythonチュートリアル
- **Pythonスクリプト (`.py`)** - スタンドアロンのPython例
- **C#プロジェクト (`.csproj`, `.sln`)** - .NETアプリケーションとサンプル
- **JavaScript (`.js`, `package.json`)** - WebベースおよびNode.jsの例
- **Markdown (`.md`)** - ドキュメントとガイド

## 例の使用方法

### Jupyterノートブックの実行

ほとんどの例はJupyterノートブックとして提供されています:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Pythonスクリプトの実行

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NETの例の実行

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

または、ソリューション全体をビルド:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Webの例の実行

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## テスト

このリポジトリは、ユニットテストを含む従来のソフトウェアプロジェクトではなく、例コードとチュートリアルを提供します。検証は通常以下の方法で行われます:

1. **例を実行する** - 各例がエラーなく実行されること
2. **出力を確認する** - モデルの応答が適切であることを確認
3. **チュートリアルに従う** - ガイドが記載通りに動作すること

**一般的な検証方法:**
- 対象環境で例を実行してテスト
- 依存関係が正しくインストールされることを確認
- モデルが正常にダウンロード/ロードされることを確認
- ドキュメントに記載された期待される動作と一致することを確認

## コードスタイルと規約

### 一般的なガイドライン

- 例は明確で、コメントが充実しており、教育的であるべき
- 言語固有の規約に従う（PythonはPEP 8、.NETはC#標準）
- 例はPhiモデルの特定の機能を示すことに集中
- 重要な概念やモデル固有のパラメータを説明するコメントを含める

### ドキュメント標準

**URLフォーマット:**
- `[text](../../url)`形式を使用し、余分なスペースを入れない
- 相対リンク: 現在のディレクトリには`./`、親ディレクトリには`../`を使用
- URLに国別ロケールを含めない（`/en-us/`、`/en/`を避ける）

**画像:**
- すべての画像を`/imgs/`ディレクトリに保存
- 英数字とダッシュを使用した説明的な名前を付ける
- 例: `phi-3-architecture.png`

**Markdownファイル:**
- `/code/`ディレクトリ内の実際の動作例を参照
- ドキュメントをコードの変更と同期させる
- READMEでJupyterノートブックリンクを📓でマーク

### ファイル構成

- `/code/`内のコード例はトピック/機能別に整理
- `/md/`内のドキュメントは可能な限りコード構造を反映
- 関連ファイル（ノートブック、スクリプト、設定ファイル）はサブディレクトリ内にまとめる

## プルリクエストガイドライン

### 提出前

1. **リポジトリをフォーク**して自分のアカウントにコピー
2. **PRをタイプ別に分ける:**
   - バグ修正は1つのPRにまとめる
   - ドキュメント更新は別のPRに
   - 新しい例は別々のPRに
   - タイポ修正はまとめてもOK

3. **マージコンフリクトの処理:**
   - 変更を加える前にローカルの`main`ブランチを更新
   - 頻繁にアップストリームと同期

4. **翻訳PR:**
   - フォルダ内のすべてのファイルの翻訳を含める必要あり
   - 元の言語と一貫した構造を維持

### 必須チェック

PRはGitHubワークフローによって自動的に検証されます:

1. **相対パス検証** - すべての内部リンクが機能すること
   - ローカルでリンクをテスト: VS CodeでCtrl+クリック
   - VS Codeのパス提案を使用（`./`または`../`）

2. **URLロケールチェック** - Web URLに国別ロケールが含まれていないこと
   - `/en-us/`、`/en/`などの言語コードを削除
   - 一般的な国際URLを使用

3. **URLの破損チェック** - すべてのURLが200ステータスを返すこと
   - 提出前にリンクがアクセス可能であることを確認
   - 注意: ネットワーク制限による失敗がある場合も

### PRタイトル形式

```
[component] Brief description
```

例:
- `[docs] Phi-4推論チュートリアルを追加`
- `[code] ONNX Runtime統合例を修正`
- `[translation] 導入ガイドの日本語翻訳を追加`

## 一般的な開発パターン

### Phiモデルの使用

**モデルのロード:**
- 例ではTransformers、ONNX Runtime、MLX、OpenVINOなどのフレームワークを使用
- モデルは通常Hugging Face、Azure、GitHub Modelsからダウンロード
- ハードウェア（CPU、GPU、NPU）との互換性を確認

**推論パターン:**
- テキスト生成: ほとんどの例はチャット/インストラクトバリアントを使用
- ビジョン: Phi-3-visionおよびPhi-4-multimodalで画像理解
- オーディオ: Phi-4-multimodalは音声入力をサポート
- 推論: Phi-4-reasoningバリアントで高度な推論タスク

### プラットフォーム固有の注意点

**Azure AI Foundry:**
- AzureサブスクリプションとAPIキーが必要
- `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`を参照

**GitHub Models:**
- テスト用の無料プランあり
- `/md/02.QuickStart/GitHubModel_QuickStart.md`を参照

**ローカル推論:**
- ONNX Runtime: クロスプラットフォームで最適化された推論
- Ollama: 簡単なローカルモデル管理（開発コンテナで事前設定済み）
- Apple MLX: Apple Silicon向けに最適化

## トラブルシューティング

### よくある問題

**メモリ問題:**
- Phiモデルは大量のRAMを必要とします（特にビジョン/マルチモーダルバリアント）
- リソース制約のある環境では量子化モデルを使用
- `/md/01.Introduction/04/QuantifyingPhi.md`を参照

**依存関係の競合:**
- Pythonの例は特定のバージョン要件がある場合があります
- 各例に仮想環境を使用
- 個別の`requirements.txt`ファイルを確認

**モデルダウンロードの失敗:**
- 大型モデルは遅い接続でタイムアウトする可能性あり
- クラウド環境（Codespaces、Azure）の使用を検討
- Hugging Faceキャッシュを確認: `~/.cache/huggingface/`

**.NETプロジェクトの問題:**
- .NET 8.0 SDKがインストールされていることを確認
- ビルド前に`dotnet restore`を使用
- 一部のプロジェクトはCUDA固有の構成（Debug_Cuda）を持つ

**JavaScript/Webの例:**
- Node.js 18+を使用して互換性を確保
- `node_modules`をクリアして再インストール
- ブラウザコンソールでWebGPU互換性の問題を確認

### ヘルプの取得

- **Discord:** Azure AI Foundry Community Discordに参加
- **GitHub Issues:** リポジトリ内でバグや問題を報告
- **GitHub Discussions:** 質問をしたり知識を共有

## 追加のコンテキスト

### 責任あるAI

すべてのPhiモデルの使用はMicrosoftの責任あるAI原則に従う必要があります:
- 公平性、信頼性、安全性
- プライバシーとセキュリティ  
- 包摂性、透明性、説明責任
- 本番アプリケーションにはAzure AI Content Safetyを使用
- `/md/01.Introduction/01/01.AISafety.md`を参照

### 翻訳

- 自動化されたGitHub Actionによる50以上の言語対応
- `/translations/`ディレクトリ内の翻訳
- co-op-translatorワークフローによって維持
- 翻訳ファイルを手動で編集しない（自動生成）

### コントリビューション

- `CONTRIBUTING.md`のガイドラインに従う
- Contributor License Agreement（CLA）に同意
- Microsoft Open Source Code of Conductを遵守
- コミットにセキュリティ情報や資格情報を含めない

### 多言語対応

このリポジトリは以下の言語で例を提供しています:
- **Python** - ML/AIワークフロー、Jupyterノートブック、微調整
- **C#/.NET** - エンタープライズアプリケーション、ONNX Runtime統合
- **JavaScript** - WebベースのAI、WebGPUを使用したブラウザ推論

使用ケースやデプロイメントターゲットに最適な言語を選択してください。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。