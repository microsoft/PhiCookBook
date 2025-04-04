<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c7a7f2a07dc176c19e1ab9f249b548c9",
  "translation_date": "2025-04-04T11:37:18+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "ja"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## WebGPUとRAGパターンのデモ
Phi-3 Onnx Hostedモデルを使用したRAGパターンは、情報検索を強化した生成（Retrieval-Augmented Generation）アプローチを活用し、Phi-3モデルの能力をONNXホスティングと組み合わせることで効率的なAI展開を実現します。このパターンは、特定の分野向けタスクのモデルを微調整するために役立ち、品質、コスト効率、長い文脈の理解を融合させています。Azure AIのスイートの一部として、簡単に見つけて試し、利用できる幅広いモデルを提供し、さまざまな業界のカスタマイズニーズに対応します。Phi-3モデル（Phi-3-mini、Phi-3-small、Phi-3-medium）はAzure AI Model Catalogで利用可能で、自己管理型またはHuggingFaceやONNXなどのプラットフォームを通じて微調整と展開が可能です。これにより、Microsoftは誰もがアクセス可能で効率的なAIソリューションを提供することにコミットしています。

## WebGPUとは
WebGPUは、ウェブブラウザから直接デバイスのグラフィックス処理ユニット（GPU）に効率的にアクセスできるよう設計された最新のウェブグラフィックスAPIです。WebGLの後継として意図されており、以下の主要な改善点を提供します：

1. **最新GPUとの互換性**: WebGPUは、Vulkan、Metal、Direct3D 12などのシステムAPIを活用して、現代的なGPUアーキテクチャとシームレスに動作するように設計されています。
2. **パフォーマンスの向上**: 一般的なGPU計算や高速な操作をサポートしており、グラフィックスレンダリングだけでなく機械学習タスクにも適しています。
3. **高度な機能**: より高度なGPU機能へのアクセスを提供し、複雑で動的なグラフィックスや計算ワークロードを可能にします。
4. **JavaScriptの負荷軽減**: GPUに多くのタスクをオフロードすることで、JavaScriptの負荷を大幅に軽減し、より良いパフォーマンスと滑らかな体験を提供します。

WebGPUは現在、Google Chromeなどのブラウザでサポートされており、他のプラットフォームへの対応拡大が進行中です。

### 03.WebGPU
必要な環境:

**対応ブラウザ:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### WebGPUを有効にする:

- Chrome/Microsoft Edgeで 

`chrome://flags/#enable-unsafe-webgpu` フラグを有効にします。

#### ブラウザを開く:
Google ChromeまたはMicrosoft Edgeを起動します。

#### フラグページにアクセス:
アドレスバーに`chrome://flags`と入力し、Enterキーを押します。

#### フラグを検索:
ページ上部の検索ボックスに「enable-unsafe-webgpu」と入力します。

#### フラグを有効化:
検索結果のリストから#enable-unsafe-webgpuフラグを見つけます。

その横のドロップダウンメニューをクリックして「Enabled」を選択します。

#### ブラウザを再起動:
フラグを有効にした後、変更を適用するためにブラウザを再起動する必要があります。ページ下部に表示される「Relaunch」ボタンをクリックしてください。

- Linuxの場合、`--enable-features=Vulkan`でブラウザを起動します。
- Safari 18 (macOS 15)ではWebGPUがデフォルトで有効です。
- Firefox Nightlyでは、アドレスバーにabout:configを入力して`set dom.webgpu.enabled to true`します。

### Microsoft EdgeでGPUを設定する 

WindowsでMicrosoft Edgeの高性能GPUを設定する手順は以下の通りです:

- **設定を開く:** スタートメニューをクリックし、設定を選択します。
- **システム設定:** システムに移動し、ディスプレイを選択します。
- **グラフィックス設定:** 下にスクロールして「グラフィックス設定」をクリックします。
- **アプリを選択:** 「優先設定を設定するアプリを選択」の下でデスクトップアプリを選び、「参照」をクリックします。
- **Edgeを選択:** Edgeのインストールフォルダー（通常`C:\Program Files (x86)\Microsoft\Edge\Application`）に移動し、`msedge.exe`を選択します。
- **優先設定を設定:** 「オプション」をクリックし、「高性能」を選択して「保存」をクリックします。
これにより、Microsoft Edgeが高性能GPUを使用してより良いパフォーマンスを発揮するようになります。
- **再起動:** これらの設定を有効にするために、マシンを再起動してください。

### Codespaceを開く:
GitHubのリポジトリに移動します。
コードボタンをクリックし、「Open with Codespaces」を選択します。

Codespaceがまだない場合は、「New codespace」をクリックして作成できます。

**注:** CodespaceでNode環境をインストールする
GitHub Codespaceからnpmデモを実行することは、プロジェクトをテストおよび開発するための優れた方法です。以下は手順です：

### 環境をセットアップする:
Codespaceを開いたら、Node.jsとnpmがインストールされていることを確認してください。以下のコマンドを実行して確認できます：
```
node -v
```
```
npm -v
```

インストールされていない場合は、以下を使用してインストールできます：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### プロジェクトディレクトリに移動する:
ターミナルを使用してnpmプロジェクトがあるディレクトリに移動します：
```
cd path/to/your/project
```

### 依存関係をインストールする:
package.jsonファイルに記載されているすべての必要な依存関係をインストールするには、以下のコマンドを実行します：

```
npm install
```

### デモを実行する:
依存関係がインストールされたら、デモスクリプトを実行できます。通常、これはpackage.jsonのscriptsセクションに指定されています。例えば、デモスクリプトがstartという名前の場合、以下を実行します：

```
npm run build
```
```
npm run dev
```

### デモにアクセスする:
デモにウェブサーバーが含まれる場合、CodespacesはアクセスするためのURLを提供します。通知を確認するか、Portsタブを確認してURLを見つけてください。

**注:** モデルはブラウザにキャッシュされる必要があるため、読み込みに時間がかかる場合があります。

### RAGデモ
Markdownファイル `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` をアップロードします。

### ファイルを選択する:
「Choose File」というボタンをクリックして、アップロードするドキュメントを選択します。

### ドキュメントをアップロードする:
ファイルを選択した後、「Upload」ボタンをクリックして、RAG（情報検索を強化した生成）のためにドキュメントをロードします。

### チャットを開始する:
ドキュメントがアップロードされたら、その内容に基づいてRAGを使用したチャットセッションを開始できます。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な点が含まれる可能性があることにご注意ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じる誤解や誤解釈について、当社は責任を負いません。