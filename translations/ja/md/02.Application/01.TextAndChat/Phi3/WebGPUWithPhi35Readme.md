<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-08T05:43:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "ja"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPUとRAGパターンのデモ紹介

Phi-3.5 Onnxホストモデルを用いたRAGパターンは、Retrieval-Augmented Generationの手法を活用し、Phi-3.5モデルの力とONNXホスティングを組み合わせて効率的なAI展開を実現します。このパターンはドメイン特化タスクのためのモデル微調整に役立ち、品質、コスト効率、長文コンテキスト理解のバランスを提供します。Azure AIの一部として、多様な業界のカスタマイズニーズに応える、見つけやすく試しやすい豊富なモデル群を提供しています。

## WebGPUとは  
WebGPUは、ウェブブラウザから直接デバイスのグラフィックス処理装置（GPU）に効率的にアクセスできるよう設計された最新のウェブグラフィックスAPIです。WebGLの後継を目指しており、以下のような主要な改善点があります：

1. **最新GPUとの互換性**：WebGPUはVulkan、Metal、Direct3D 12などのシステムAPIを活用し、現代のGPUアーキテクチャとシームレスに連携します。
2. **パフォーマンス向上**：汎用GPU計算や高速処理に対応し、グラフィックスレンダリングだけでなく機械学習タスクにも適しています。
3. **高度な機能**：より複雑で動的なグラフィックスや計算ワークロードを可能にする、先進的なGPU機能にアクセスできます。
4. **JavaScriptの負荷軽減**：多くの処理をGPUにオフロードすることで、JavaScriptの負荷が大幅に減り、パフォーマンスとスムーズな体験が向上します。

現在、WebGPUはGoogle Chromeなどのブラウザでサポートされており、他のプラットフォームへの対応も進められています。

### 03.WebGPU  
必要な環境：

**対応ブラウザ：**  
- Google Chrome 113以上  
- Microsoft Edge 113以上  
- Safari 18（macOS 15）  
- Firefox Nightly  

### WebGPUを有効にする方法：

- Chrome/Microsoft Edgeの場合  

`chrome://flags/#enable-unsafe-webgpu` フラグを有効にしてください。

#### ブラウザを開く：  
Google ChromeまたはMicrosoft Edgeを起動します。

#### フラグページにアクセス：  
アドレスバーに `chrome://flags` と入力し、Enterキーを押します。

#### フラグを検索：  
ページ上部の検索ボックスに「enable-unsafe-webgpu」と入力します。

#### フラグを有効化：  
リストから #enable-unsafe-webgpu フラグを見つけます。  
その隣のドロップダウンメニューをクリックし、「Enabled」を選択します。

#### ブラウザを再起動：  
フラグを有効にした後、変更を反映させるためにブラウザを再起動する必要があります。ページ下部に表示される「Relaunch」ボタンをクリックしてください。

- Linuxの場合は `--enable-features=Vulkan` を使ってブラウザを起動してください。  
- Safari 18（macOS 15）はデフォルトでWebGPUが有効になっています。  
- Firefox Nightlyでは、アドレスバーに about:config と入力し、`set dom.webgpu.enabled to true` を実行してください。

### Microsoft EdgeでのGPU設定方法  

WindowsでMicrosoft Edgeの高性能GPUを設定する手順は以下の通りです：

- **設定を開く：** スタートメニューから設定を選択します。  
- **システム設定：** 「システム」→「ディスプレイ」に進みます。  
- **グラフィックス設定：** 下にスクロールして「グラフィックス設定」をクリックします。  
- **アプリの選択：** 「優先設定を設定するアプリを選ぶ」から「デスクトップアプリ」を選び、「参照」をクリックします。  
- **Edgeを選択：** Edgeのインストールフォルダー（通常は `C:\Program Files (x86)\Microsoft\Edge\Application`）に移動し、`msedge.exe` を選択します。  
- **優先設定を設定：** 「オプション」をクリックし、「高パフォーマンス」を選択して「保存」をクリックします。  
これにより、Microsoft Edgeが高性能GPUを使用するようになり、パフォーマンスが向上します。  
- 設定を反映させるために **PCを再起動** してください。

### サンプル : [こちらのリンクをクリックしてください](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。