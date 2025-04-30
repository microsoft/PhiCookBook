<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "faa063cfc6d50047bbfdb58a90d520ad",
  "translation_date": "2025-04-04T12:46:26+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "ja"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPUとRAGパターンのデモ

Phi-3.5 Onnx Hostedモデルを使用したRAGパターンは、Retrieval-Augmented Generationアプローチを活用し、Phi-3.5モデルの力とONNXホスティングを組み合わせて効率的なAI展開を実現します。このパターンは、ドメイン固有のタスク向けにモデルを微調整するために重要であり、品質、コスト効率、長いコンテキスト理解を融合させています。Azure AIのスイートの一部として、さまざまな業界のカスタマイズニーズに応えるために、簡単に見つけて試し、使用できるモデルの幅広い選択肢を提供しています。

## WebGPUとは
WebGPUは、ウェブブラウザからデバイスのグラフィックス処理ユニット（GPU）に直接効率的にアクセスするために設計された最新のウェブグラフィックスAPIです。WebGLの後継として意図されており、以下のような主要な改善点を提供します：

1. **最新GPUとの互換性**: WebGPUは、現代のGPUアーキテクチャとシームレスに動作するように構築されており、Vulkan、Metal、Direct3D 12などのシステムAPIを活用します。
2. **性能向上**: 汎用的なGPU計算や高速な操作をサポートし、グラフィックスレンダリングだけでなく機械学習タスクにも適しています。
3. **高度な機能**: より複雑で動的なグラフィックスや計算ワークロードを可能にする、より高度なGPU機能へのアクセスを提供します。
4. **JavaScriptの負荷軽減**: GPUにより多くのタスクをオフロードすることで、JavaScriptの負荷を大幅に軽減し、より良い性能と滑らかな体験を実現します。

WebGPUは現在、Google Chromeなどのブラウザでサポートされており、他のプラットフォームへのサポート拡大が進行中です。

### 03.WebGPU
必要な環境：

**対応ブラウザ:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### WebGPUを有効化する方法:

- Chrome/Microsoft Edgeの場合 

`chrome://flags/#enable-unsafe-webgpu`フラグを有効にします。

#### ブラウザを開く:
Google ChromeまたはMicrosoft Edgeを起動します。

#### フラグページにアクセス:
アドレスバーに`chrome://flags`と入力し、Enterキーを押します。

#### フラグを検索:
ページ上部の検索ボックスに「enable-unsafe-webgpu」と入力します。

#### フラグを有効化:
検索結果一覧から#enable-unsafe-webgpuフラグを見つけます。

その横のドロップダウンメニューをクリックし、「Enabled」を選択します。

#### ブラウザを再起動:
フラグを有効化した後、変更を反映させるためにブラウザを再起動する必要があります。ページ下部に表示される「Relaunch」ボタンをクリックしてください。

- Linuxの場合は、ブラウザを`--enable-features=Vulkan`で起動します。
- Safari 18 (macOS 15)ではWebGPUがデフォルトで有効になっています。
- Firefox Nightlyでは、アドレスバーにabout:configと入力して`set dom.webgpu.enabled to true`を行います。

### Microsoft EdgeでGPUを設定する方法

WindowsでMicrosoft Edgeに高性能GPUを設定する手順は以下の通りです：

- **設定を開く:** スタートメニューをクリックして「設定」を選択します。
- **システム設定:** 「システム」から「ディスプレイ」に進みます。
- **グラフィックス設定:** 下にスクロールして「グラフィックス設定」をクリックします。
- **アプリを選択:** 「アプリの設定の優先順位を選択」欄で「デスクトップアプリ」を選択し、「参照」をクリックします。
- **Edgeを選択:** Edgeのインストールフォルダ（通常`C:\Program Files (x86)\Microsoft\Edge\Application`）に移動し、`msedge.exe`を選択します。
- **優先設定をセット:** 「オプション」をクリックし、「高性能」を選択して「保存」をクリックします。
これにより、Microsoft Edgeが高性能GPUを使用してより良いパフォーマンスを発揮するようになります。
- **再起動:** 設定を反映させるためにマシンを再起動します。

### サンプル : [こちらのリンク](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)をご覧ください

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文（元の言語で記載された文書）が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じる誤解や誤解釈について、当方は一切の責任を負いません。