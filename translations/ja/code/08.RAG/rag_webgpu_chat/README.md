<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:14:28+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "ja"
}
-->
Phi-3-mini WebGPU RAG チャットボット

## WebGPU と RAG パターンのデモ紹介
Phi-3 Onnx ホストモデルを用いた RAG パターンは、Retrieval-Augmented Generation（検索強化生成）アプローチを活用し、Phi-3 モデルの力と ONNX ホスティングを組み合わせて効率的な AI 展開を実現します。このパターンは、ドメイン固有のタスクにモデルを微調整する際に重要であり、品質、コスト効率、長文コンテキストの理解を兼ね備えています。Azure AI のスイートの一部として、多様な業界のカスタマイズニーズに応えるため、見つけやすく試しやすい幅広いモデルを提供しています。Phi-3-mini、Phi-3-small、Phi-3-medium を含む Phi-3 モデルは Azure AI Model Catalog で利用可能で、自己管理または HuggingFace や ONNX などのプラットフォームを通じて微調整・展開が可能であり、Microsoft のアクセスしやすく効率的な AI ソリューションへの取り組みを示しています。

## WebGPU とは
WebGPU は、ウェブブラウザからデバイスのグラフィックス処理装置（GPU）に効率的にアクセスするために設計された最新のウェブグラフィックス API です。WebGL の後継として位置づけられており、以下のような主な改善点があります：

1. **最新 GPU との互換性**：WebGPU は Vulkan、Metal、Direct3D 12 などのシステム API を活用し、現代の GPU アーキテクチャとシームレスに連携します。
2. **パフォーマンスの向上**：汎用 GPU 計算や高速な処理をサポートし、グラフィックスレンダリングだけでなく機械学習タスクにも適しています。
3. **高度な機能**：より複雑で動的なグラフィックスや計算負荷の高い処理を可能にする先進的な GPU 機能にアクセスできます。
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
検索結果に表示される #enable-unsafe-webgpu フラグを見つけます。

隣のドロップダウンメニューをクリックし、「Enabled」を選択します。

#### ブラウザを再起動：
フラグを有効にした後、変更を反映させるためにブラウザを再起動します。ページ下部に表示される「Relaunch」ボタンをクリックしてください。

- Linux では、`--enable-features=Vulkan` オプションを付けてブラウザを起動します。  
- Safari 18（macOS 15）では WebGPU がデフォルトで有効になっています。  
- Firefox Nightly では、アドレスバーに about:config と入力し、`dom.webgpu.enabled` を true に設定します。

### Microsoft Edge での GPU 設定方法

Windows 上で Microsoft Edge に高性能 GPU を設定する手順は以下の通りです：

- **設定を開く：** スタートメニューをクリックし、「設定」を選択します。  
- **システム設定：** 「システム」から「ディスプレイ」に進みます。  
- **グラフィックス設定：** 下にスクロールして「グラフィックス設定」をクリックします。  
- **アプリの選択：** 「優先設定を設定するアプリを選ぶ」で「デスクトップアプリ」を選択し、「参照」をクリックします。  
- **Edge を選択：** Edge のインストールフォルダ（通常は `C:\Program Files (x86)\Microsoft\Edge\Application`）に移動し、`msedge.exe` を選択します。  
- **優先設定の指定：** 「オプション」をクリックし、「高パフォーマンス」を選択して「保存」をクリックします。  
これで Microsoft Edge が高性能 GPU を使用するようになり、パフォーマンスが向上します。  
- 設定を反映させるために **PC を再起動** してください。

### Codespace を開く：
GitHub のリポジトリに移動します。  
「Code」ボタンをクリックし、「Open with Codespaces」を選択します。

まだ Codespace を持っていない場合は、「New codespace」をクリックして作成できます。

**Note** Codespace に Node 環境をインストールする  
GitHub Codespace で npm デモを実行するのは、プロジェクトのテストや開発に最適な方法です。以下の手順で始めましょう：

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
ターミナルで npm プロジェクトのあるディレクトリに移動します：  
```
cd path/to/your/project
```

### 依存関係をインストール：
package.json に記載された必要な依存関係をすべてインストールするには、以下のコマンドを実行します：  
```
npm install
```

### デモを実行：
依存関係のインストールが完了したら、デモスクリプトを実行できます。通常、package.json の scripts セクションに指定されています。例えば、デモスクリプトが start という名前の場合は以下のように実行します：  
```
npm run build
```  
```
npm run dev
```

### デモにアクセス：
デモがウェブサーバーを含む場合、Codespaces はアクセス用の URL を提供します。通知や Ports タブを確認して URL を探してください。

**Note:** モデルはブラウザにキャッシュされる必要があるため、読み込みに時間がかかる場合があります。

### RAG デモ
RAG ソリューションを完成させるには、マークダウンファイル `intro_rag.md` をアップロードしてください。Codespaces を使用している場合は、`01.InferencePhi3/docs/` にあるファイルをダウンロードできます。

### ファイルを選択：
「Choose File」ボタンをクリックしてアップロードしたいドキュメントを選びます。

### ドキュメントをアップロード：
ファイルを選択したら、「Upload」ボタンをクリックして RAG（Retrieval-Augmented Generation）用にドキュメントを読み込みます。

### チャットを開始：
ドキュメントがアップロードされたら、その内容に基づいて RAG を使ったチャットセッションを開始できます。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。