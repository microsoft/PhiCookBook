<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-08T06:47:59+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "ja"
}
-->
Phi-3-mini WebGPU RAG チャットボット

## WebGPU と RAG パターンを紹介するデモ
Phi-3 Onnx ホストモデルを用いた RAG パターンは、Retrieval-Augmented Generation（検索強化生成）アプローチを活用し、Phi-3 モデルの力と ONNX ホスティングを組み合わせて効率的な AI 展開を実現します。このパターンはドメイン固有のタスクにモデルをファインチューニングする際に重要であり、品質、コスト効率、長文コンテキストの理解を両立します。Azure AI のスイートの一部として、多様な業界のカスタマイズニーズに応えるため、見つけやすく試しやすい幅広いモデルを提供しています。Phi-3-mini、Phi-3-small、Phi-3-medium を含む Phi-3 モデルは Azure AI Model Catalog で利用可能で、セルフマネージドや HuggingFace、ONNX といったプラットフォームを通じてファインチューニングやデプロイが可能であり、Microsoft のアクセスしやすく効率的な AI ソリューションへの取り組みを示しています。

## WebGPU とは何か
WebGPU は、ウェブブラウザからデバイスの GPU（グラフィックス処理装置）に効率的にアクセスできるよう設計された最新のウェブグラフィックス API です。WebGL の後継として位置づけられており、以下のような主要な改善点があります：

1. **最新 GPU との互換性**：WebGPU は Vulkan、Metal、Direct3D 12 といったシステム API を活用し、現代の GPU アーキテクチャとシームレスに動作します。
2. **パフォーマンスの向上**：汎用 GPU 計算や高速な処理をサポートし、グラフィックスレンダリングだけでなく機械学習タスクにも適しています。
3. **高度な機能**：より複雑で動的なグラフィックスや計算負荷の高いワークロードに対応できる先進的な GPU 機能へのアクセスを提供します。
4. **JavaScript の負荷軽減**：多くの処理を GPU にオフロードすることで、JavaScript の負荷を大幅に減らし、パフォーマンス向上と滑らかな体験を実現します。

WebGPU は現在、Google Chrome などのブラウザでサポートされており、他のプラットフォームへの対応も進められています。

### 03.WebGPU
必要な環境：

**対応ブラウザ:**  
- Google Chrome 113 以上  
- Microsoft Edge 113 以上  
- Safari 18（macOS 15）  
- Firefox Nightly  

### WebGPU を有効にする方法：

- Chrome / Microsoft Edge で

`chrome://flags/#enable-unsafe-webgpu` フラグを有効にしてください。

#### ブラウザを開く：
Google Chrome または Microsoft Edge を起動します。

#### フラグのページにアクセス：
アドレスバーに `chrome://flags` と入力し、Enter キーを押します。

#### フラグを検索：
ページ上部の検索ボックスに「enable-unsafe-webgpu」と入力します。

#### フラグを有効化：
結果一覧から #enable-unsafe-webgpu フラグを見つけます。

隣のドロップダウンメニューをクリックし、「Enabled」を選択します。

#### ブラウザを再起動：
フラグを有効にした後、変更を反映するためにブラウザを再起動してください。ページ下部に表示される「Relaunch」ボタンをクリックします。

- Linux では、`--enable-features=Vulkan` を使ってブラウザを起動します。  
- Safari 18（macOS 15）では WebGPU がデフォルトで有効になっています。  
- Firefox Nightly では、アドレスバーに about:config と入力し、`set dom.webgpu.enabled to true` を設定してください。

### Microsoft Edge で GPU を設定する方法

Windows で Microsoft Edge に高性能 GPU を割り当てる手順は以下の通りです：

- **設定を開く:** スタートメニューから設定を選択します。  
- **システム設定:** 「システム」→「ディスプレイ」に移動します。  
- **グラフィックス設定:** 下にスクロールして「グラフィックス設定」をクリックします。  
- **アプリの選択:** 「優先設定を設定するアプリを選ぶ」で「デスクトップアプリ」を選択し、「参照」をクリックします。  
- **Edge を選択:** Edge のインストールフォルダー（通常は `C:\Program Files (x86)\Microsoft\Edge\Application`）に移動し、`msedge.exe` を選択します。  
- **優先設定の設定:** 「オプション」をクリックし、「高パフォーマンス」を選択してから「保存」をクリックします。  

これで Microsoft Edge が高性能 GPU を使用するようになり、パフォーマンスが向上します。  
- 設定を反映させるために **PC を再起動** してください。

### Codespace を開く：
GitHub 上のリポジトリに移動します。  
「Code」ボタンをクリックし、「Open with Codespaces」を選択します。

まだ Codespace を持っていない場合は、「New codespace」をクリックして作成できます。

**注意** Codespace での Node 環境のインストールについて  
GitHub Codespace で npm デモを実行することは、プロジェクトのテストや開発に非常に便利です。以下のステップで始めましょう。

### 環境をセットアップする：
Codespace が開いたら、Node.js と npm がインストールされているか確認します。以下のコマンドを実行してください：  
```
node -v
```  
```
npm -v
```

インストールされていない場合は、以下のコマンドでインストールできます：  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### プロジェクトディレクトリに移動：
ターミナルで npm プロジェクトがあるディレクトリに移動します：  
```
cd path/to/your/project
```

### 依存関係をインストール：
package.json に記載された必要な依存関係をすべてインストールするには、次のコマンドを実行します：  
```
npm install
```

### デモを実行：
依存関係がインストールできたら、デモスクリプトを実行します。通常、package.json の scripts セクションに指定されています。例えば、デモスクリプト名が start なら、以下のように実行します：  
```
npm run build
```  
```
npm run dev
```

### デモにアクセス：
デモがウェブサーバーを伴う場合、Codespaces はアクセス用の URL を提供します。通知や Ports タブで URL を確認してください。

**注意:** モデルはブラウザにキャッシュされる必要があるため、読み込みに時間がかかる場合があります。

### RAG デモ
markdown ファイル `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` をアップロードしてください。

### ファイルを選択：
「Choose File」ボタンをクリックして、アップロードしたいドキュメントを選択します。

### ドキュメントをアップロード：
ファイルを選択したら、「Upload」ボタンをクリックして RAG（Retrieval-Augmented Generation）用にドキュメントを読み込みます。

### チャットを開始：
ドキュメントのアップロードが完了したら、その内容に基づいて RAG を使ったチャットセッションを開始できます。

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切責任を負いかねます。