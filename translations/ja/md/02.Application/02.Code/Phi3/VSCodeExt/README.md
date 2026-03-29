# **Microsoft Phi-3 ファミリーで独自の Visual Studio Code GitHub Copilot Chat を構築する**

GitHub Copilot Chat のワークスペース エージェントを使ったことはありますか？自分のチーム専用のコードエージェントを作ってみたいですか？このハンズオンラボでは、オープンソースモデルを組み合わせてエンタープライズレベルのコードビジネスエージェント構築を目指します。

## <strong>基礎</strong>

### **なぜ Microsoft Phi-3 を選ぶのか**

Phi-3 は、テキスト生成、対話完了、コード生成のための異なるトレーニングパラメーターに基づく phi-3-mini、phi-3-small、phi-3-medium を含むファミリーシリーズです。Vision ベースの phi-3-vision もあります。企業や異なるチームがオフラインで生成AIソリューションを作るのに適しています。

こちらのリンクの閲覧を推奨します [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 拡張機能はチャットインターフェースを提供し、GitHub Copilot と対話しながら VS Code 上でコーディング関連の質問に直接回答を得ることができます。ドキュメントを移動したりオンラインフォーラムを検索したりする必要はありません。

Copilot Chat は生成された応答に対して構文ハイライトやインデントなどのフォーマット機能を利用し明瞭さを加えることがあります。ユーザーの質問の種類により、ソースコードファイルやドキュメントなどCopilotが応答生成に使ったコンテキストへのリンクや、VS Code機能を利用するためのボタンが応答に含まれることがあります。

- Copilot Chat は開発者の作業フローに統合され、必要な場所で支援を提供します:

- 編集画面やターミナルから直接インラインチャットを開始し、コーディング中のヘルプを得る

- チャットビューを使っていつでもAIアシスタントを傍らに置く

- クイックチャットを起動してすぐに質問し作業に戻る

GitHub Copilot Chat は以下のようなシナリオで使えます:

- 問題を解決するためのコーディング質問への回答

- 他人のコードの説明や改善案の提案

- コード修正の提案

- ユニットテストケースの生成

- コードドキュメントの生成

こちらのリンクの閲覧を推奨します [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat の @workspace**

Copilot Chat の **@workspace** を参照すると、コードベース全体について質問することが可能です。質問に基づき、Copilot は関連するファイルやシンボルを賢く検索し、リンクやコード例として回答内で参照します。

質問に答えるために、**@workspace** は開発者が VS Code でコードベースをナビゲートするときに使うのと同じ情報源から検索します:

- .gitignore ファイルで無視されていないワークスペース内のすべてのファイル

- 入れ子のフォルダーおよびファイル名を含むディレクトリ構造

- ワークスペースが GitHub リポジトリでありコードサーチでインデックスされている場合の GitHub コード検索インデックス

- ワークスペース内のシンボルと定義

- 現在選択されているテキストまたはアクティブエディターで可視のテキスト

注意: .gitignore に無視されているファイルを開いているか、選択内にテキストがある場合は無視されません。

こちらのリンクの閲覧を推奨します [https://code.visualstudio.com/docs/copilot/workspace-context](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)


## <strong>このラボについて</strong>

GitHub Copilot は企業のプログラミング効率を大幅に向上させており、各企業は GitHub Copilot の関連機能をカスタマイズしたいと考えています。多くの企業は自身のビジネスシナリオやオープンソースモデルに基づき、GitHub Copilot に類似したカスタマイズされた拡張機能を作成しています。企業にとってはカスタマイズされた拡張機能の方が管理しやすいですが、ユーザー体験に影響する場合があります。GitHub Copilot は一般的なシナリオ対応や専門性でより強力な機能を持っているため、体験を一貫させられれば、企業独自の拡張機能をカスタマイズする方が良いでしょう。GitHub Copilot Chat は企業がチャット体験を拡張できる関連APIを提供しています。一貫した体験を維持しつつカスタマイズ機能を持つことはより良いユーザー体験につながります。

このラボでは主に Phi-3 モデルとローカルNPUおよび Azure ハイブリッドを組み合わせて、GitHub Copilot Chat においてカスタムエージェント ***@PHI3*** を構築し、企業開発者のコード生成<strong><em>(@PHI3 /gen)</em></strong>や画像ベースのコード生成<strong><em>(@PHI3 /img)</em></strong>を支援します。

![PHI3](../../../../../../../translated_images/ja/cover.1017ebc9a7c46d09.webp)

### ***注意:*** 

本ラボは現在 Intel CPU と Apple Silicon 向けの AIPC で実装しています。今後 Qualcomm バージョンの NPU も更新予定です。


## <strong>ラボ</strong>


| 名称 | 説明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - インストール(✅) | 関連環境とインストールツールの設定とインストール | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini での Prompt flow 実行 (✅) | AIPC/Apple Silicon と連携し、ローカルNPUを使った Phi-3-mini によるコード生成作成 | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service での Phi-3-vision 展開(✅) | Azure Machine Learning Service のモデルカタログ - Phi-3-vision イメージを展開しコード生成 | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat で @phi-3 エージェント作成(✅)  | GitHub Copilot Chat にカスタムの Phi-3 エージェントを作り、コード生成、グラフ生成コード、RAG 等を完成させる | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| サンプルコード (✅)  | サンプルコードのダウンロード | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## <strong>リソース</strong>

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot の詳細 [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat の詳細 [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API の詳細 [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry の詳細 [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry のモデルカタログの詳細 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性に努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。原文のネイティブ言語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->