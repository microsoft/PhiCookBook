<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:07:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "ja"
}
-->
# Phi-3.5-Instruct WebGPU RAG チャットボット

## WebGPU と RAG パターンのデモ

Phi-3.5 Onnx ホストモデルを用いた RAG パターンは、Retrieval-Augmented Generation（検索強化生成）アプローチを活用し、Phi-3.5 モデルの力と ONNX ホスティングを組み合わせて効率的な AI 展開を実現します。このパターンは、ドメイン固有のタスクにモデルを微調整する際に役立ち、品質、コスト効率、長文コンテキストの理解を兼ね備えています。Azure AI の一部として、多様な業界のカスタマイズニーズに応えるため、見つけやすく試しやすい幅広いモデルを提供しています。

## WebGPU とは  
WebGPU は、ウェブブラウザからデバイスのグラフィックス処理装置（GPU）に効率的にアクセスするために設計された最新のウェブグラフィックス API です。WebGL の後継を目指しており、以下のような主な改善点があります：

1. **最新 GPU との互換性**：WebGPU は Vulkan、Metal、Direct3D 12 などのシステム API を活用し、現代の GPU アーキテクチャとシームレスに連携します。
2. **パフォーマンスの向上**：汎用 GPU 計算や高速な処理をサポートし、グラフィックスレンダリングだけでなく機械学習タスクにも適しています。
3. **高度な機能**：より複雑で動的なグラフィックスや計算処理を可能にする、より高度な GPU 機能にアクセスできます。
4. **JavaScript の負荷軽減**：より多くの処理を GPU にオフロードすることで、JavaScript の負荷を大幅に減らし、パフォーマンス向上とスムーズな体験を実現します。

現在、Google Chrome などのブラウザでサポートされており、他のプラットフォームへの対応も進められています。

### 03.WebGPU  
必要な環境：

**対応ブラウザ：**  
- Google Chrome 113 以上  
- Microsoft Edge 113 以上  
- Safari 18（macOS 15）  
- Firefox Nightly  

### WebGPU を有効にする方法：

- Chrome / Microsoft Edge の場合  

`chrome://flags/#enable-unsafe-webgpu` フラグを有効にします。

#### ブラウザを開く：  
Google Chrome または Microsoft Edge を起動します。

#### フラグページにアクセス：  
アドレスバーに `chrome://flags` と入力して Enter キーを押します。

#### フラグを検索：  
ページ上部の検索ボックスに「enable-unsafe-webgpu」と入力します。

#### フラグを有効化：  
検索結果の中から #enable-unsafe-webgpu フラグを見つけます。  
隣のドロップダウンメニューをクリックし、「Enabled」を選択します。

#### ブラウザを再起動：  
フラグを有効にした後、変更を反映させるためにブラウザを再起動します。  
ページ下部に表示される「Relaunch」ボタンをクリックしてください。

- Linux では、`--enable-features=Vulkan` オプションを付けてブラウザを起動します。  
- Safari 18（macOS 15）では WebGPU がデフォルトで有効になっています。  
- Firefox Nightly では、アドレスバーに about:config と入力し、`dom.webgpu.enabled` を true に設定します。

### Microsoft Edge での GPU 設定方法  

Windows で Microsoft Edge に高性能 GPU を割り当てる手順は以下の通りです：

- **設定を開く：** スタートメニューから「設定」を選択します。  
- **システム設定：** 「システム」→「ディスプレイ」に進みます。  
- **グラフィックス設定：** 下にスクロールして「グラフィックス設定」をクリックします。  
- **アプリの選択：** 「優先設定を設定するアプリを選ぶ」で「デスクトップアプリ」を選択し、「参照」をクリックします。  
- **Edge を選択：** Edge のインストールフォルダ（通常は `C:\Program Files (x86)\Microsoft\Edge\Application`）に移動し、`msedge.exe` を選択します。  
- **優先設定の指定：** 「オプション」をクリックし、「高パフォーマンス」を選択して「保存」をクリックします。  
これで Microsoft Edge が高性能 GPU を使用するようになり、パフォーマンスが向上します。  
- 設定を反映させるために **PC を再起動** してください。

### サンプル : [こちらのリンクをクリック](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。