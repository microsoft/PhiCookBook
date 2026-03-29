# Microsoft FoundryによるPhi-3のファインチューニング

Microsoft Foundryを使ってMicrosoftのPhi-3 Mini言語モデルをファインチューニングする方法を見てみましょう。ファインチューニングにより、Phi-3 Miniを特定のタスクに適応させ、さらに強力で文脈認識に優れたモデルにできます。

## 考慮事項

- **機能:** どのモデルがファインチューニング可能か？ベースモデルはどのようなことにファインチューニングできるか？
- **コスト:** ファインチューニングの料金体系は？
- **カスタマイズ性:** ベースモデルをどれくらい、どのように変更できるか？
- **利便性:** ファインチューニングは実際にどのように行うか？カスタムコードを書く必要はあるか？自前の計算リソースが必要か？
- **安全性:** ファインチューニングされたモデルは安全上のリスクが知られているが、不測の害を防ぐためのガードレールはあるか？

![AIFoundry Models](../../../../translated_images/ja/AIFoundryModels.0e1b16f7d0b09b73.webp)

## ファインチューニングの準備

### 前提条件

> [!NOTE]
> Phi-3ファミリのモデルについては、ペイアズユーゴー方式のファインチューニング提供は **East US 2** リージョンに作成されたハブでのみ利用可能です。

- Azureサブスクリプション。持っていない場合は、[有料のAzureアカウント](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go)を作成してください。

- [AI Foundryプロジェクト](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)。
- Microsoft Foundryでの操作アクセスはAzureの役割ベースアクセス制御（Azure RBAC）で付与されます。本記事の手順を実行するには、リソースグループに対して__Azure AI Developerロール__がユーザーアカウントに割り当てられている必要があります。

### サブスクリプションプロバイダー登録

サブスクリプションが `Microsoft.Network` リソースプロバイダーに登録されていることを確認します。

1. [Azure portal](https://portal.azure.com) にサインインします。
1. 左メニューから <strong>サブスクリプション</strong> を選択します。
1. 利用したいサブスクリプションを選択します。
1. 左メニューの **AI プロジェクト設定** > <strong>リソースプロバイダー</strong> を選択します。
1. **Microsoft.Network** がリストにあるかを確認し、なければ追加します。

### データ準備

モデルのファインチューニングに使用するトレーニングデータと検証データを準備します。トレーニングデータと検証データセットには、モデルにどう動作してほしいかの入出力例を用意します。

すべてのトレーニング例が推論で期待されるフォーマットに準拠していることを確認してください。効果的なファインチューニングには、バランスの取れた多様なデータセットが必要です。

これはデータのバランスを保ち、様々なシナリオを含め、定期的にトレーニングデータを現実の期待に合わせて洗練することを含み、最終的により正確でバランスの良いモデル応答につながります。

モデルのタイプによって必要なトレーニングデータのフォーマットは異なります。

### チャットコンプリーション

使用するトレーニングおよび検証データは<strong>必ず</strong>JSON Lines (JSONL)形式でフォーマットしてください。`Phi-3-mini-128k-instruct`の場合、ファインチューニング用データセットはChat completions APIで使われる会話形式である必要があります。

### 例ファイルフォーマット

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

対応しているファイルタイプはJSON Linesです。ファイルはデフォルトのデータストアにアップロードされ、プロジェクト内で利用可能になります。

## Microsoft FoundryによるPhi-3のファインチューニング

Microsoft Foundryはファインチューニングと呼ばれるプロセスを利用して、大規模言語モデルを個人のデータセットに合わせて調整できます。ファインチューニングは特定のタスクやアプリケーション向けにカスタマイズと最適化を可能にし、大きな価値を提供します。これによりパフォーマンス向上、コスト効率、レイテンシ低減、そしてカスタマイズされた出力が得られます。

![Finetune AI Foundry](../../../../translated_images/ja/AIFoundryfinetune.193aaddce48d553c.webp)

### 新しいプロジェクトを作成する

1. [Microsoft Foundry](https://ai.azure.com) にサインインします。

1. **+New project** を選択してMicrosoft Foundryで新しいプロジェクトを作成します。

    ![FineTuneSelect](../../../../translated_images/ja/select-new-project.cd31c0404088d7a3.webp)

1. 以下のタスクを実行します：

    - プロジェクトの<strong>Hub名</strong>。一意の値にする必要があります。
    - 使用する<strong>Hub</strong>を選択（必要なら新規作成）。

    ![FineTuneSelect](../../../../translated_images/ja/create-project.ca3b71298b90e420.webp)

1. 新しいハブを作成するために以下を行います：

    - <strong>Hub名</strong>を入力。一意の値にしてください。
    - Azureの<strong>サブスクリプション</strong>を選択。
    - 使用する<strong>リソースグループ</strong>を選択（必要なら新規作成）。
    - 使用したい<strong>リージョン</strong>を選択。
    - 使用したい<strong>Azure AI Servicesの接続</strong>を選択（必要なら新規作成）。
    - <strong>Connect Azure AI Search</strong>は<strong>接続しない</strong>を選択。

    ![FineTuneSelect](../../../../translated_images/ja/create-hub.49e53d235e80779e.webp)

1. <strong>Next</strong>を選択。
1. <strong>Create a project</strong>を選択。

### データ準備

ファインチューニングの前に、チャット指示、質問応答ペア、その他関連するテキストデータなど、タスクに関連するデータセットを集めるか作成します。ノイズの除去、欠損値の処理、テキストのトークン化など、データのクリーンアップと前処理を行ってください。

### Microsoft FoundryでPhi-3モデルをファインチューニングする

> [!NOTE]
> Phi-3モデルのファインチューニングは現時点ではEast US 2リージョンにあるプロジェクトでサポートされています。

1. 左側のタブから **Model catalog** を選択。

1. <strong>検索バー</strong>に<em>phi-3</em>と入力し、使用したいphi-3モデルを選択。

    ![FineTuneSelect](../../../../translated_images/ja/select-model.60ef2d4a6a3cec57.webp)

1. <strong>Fine-tune</strong>を選択。

    ![FineTuneSelect](../../../../translated_images/ja/select-finetune.a976213b543dd9d8.webp)

1. <strong>Fine-tuned model name</strong>を入力。

    ![FineTuneSelect](../../../../translated_images/ja/finetune1.c2b39463f0d34148.webp)

1. <strong>Next</strong>を選択。

1. 次のタスクを実施：

    - <strong>task type</strong>を<strong>Chat completion</strong>に設定。
    - 使用する<strong>Training data</strong>を選択。Microsoft Foundryのデータからかローカル環境からアップロード可能。

    ![FineTuneSelect](../../../../translated_images/ja/finetune2.43cb099b1a94442d.webp)

1. <strong>Next</strong>を選択。

1. 使用したい<strong>Validation data</strong>をアップロード、もしくは<strong>Automatic split of training data</strong>を選択。

    ![FineTuneSelect](../../../../translated_images/ja/finetune3.fd96121b67dcdd92.webp)

1. <strong>Next</strong>を選択。

1. 以下の項目を選択：

    - 使用したい<strong>Batch size multiplier</strong>。
    - 使用したい<strong>Learning rate</strong>。
    - 使用したい<strong>Epochs</strong>。

    ![FineTuneSelect](../../../../translated_images/ja/finetune4.e18b80ffccb5834a.webp)

1. ファインチューニングプロセスを開始するために<strong>Submit</strong>を選択。

    ![FineTuneSelect](../../../../translated_images/ja/select-submit.0a3802d581bac271.webp)

1. モデルがファインチューニングされると、ステータスが<strong>Completed</strong>となります。以下の画像のように表示されます。これでモデルをデプロイし、自身のアプリケーション、プレイグラウンド、プロンプトフローなどで利用可能です。詳細は[Microsoft FoundryでPhi-3ファミリ小型言語モデルをデプロイする方法](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)をご覧ください。

    ![FineTuneSelect](../../../../translated_images/ja/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3のファインチューニングに関する詳細情報は[Microsoft FoundryでのPhi-3モデルファインチューニング](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)をご覧ください。

## ファインチューニングモデルのクリーンアップ

[Microsoft Foundry](https://ai.azure.com)のファインチューニングモデル一覧またはモデル詳細ページからファインチューニングモデルを削除できます。ファインチューニングページで削除したいモデルを選択し、「Delete」ボタンを押して削除してください。

> [!NOTE]
> 既にデプロイメントがあるカスタムモデルは削除できません。モデル削除の前に、モデルのデプロイメントを先に削除する必要があります。

## コストとクォータ

### サービスとしてファインチューニングされたPhi-3モデルのコストとクォータ

サービスとしてファインチューニングされたPhiモデルはMicrosoftが提供し、Microsoft Foundryに統合されています。モデルの[デプロイ](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)やファインチューニング時に、デプロイメントウィザードのPricing and termsタブで料金体系を確認できます。

## コンテンツフィルタリング

ペイアズユーゴー方式でサービスとしてデプロイされたモデルはAzure AI Content Safetyによって保護されています。リアルタイムエンドポイントにデプロイする際にこの機能をオプトアウト可能です。Azure AI Content Safetyを有効にすると、プロンプトとコンプリーションの両方が有害な内容の出力を検知し防止する分類モデルのアンサンブルを通過します。コンテンツフィルタリングシステムは入力プロンプトと出力コンプリーションの双方において潜在的に有害な特定カテゴリを検知し、対応措置を取ります。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)について詳しく学べます。

<strong>ファインチューニング構成</strong>

ハイパーパラメータ：学習率、バッチサイズ、トレーニングエポック数などを定義。

<strong>損失関数</strong>

タスクに適した損失関数を選択（例：クロスエントロピー）。

<strong>オプティマイザー</strong>

トレーニング中の勾配更新に用いるオプティマイザーを選択（例：Adam）。

<strong>ファインチューニングプロセス</strong>

- 事前学習済みモデルのロード：Phi-3 Miniのチェックポイントをロード。
- カスタムレイヤーの追加：タスク特化レイヤー（例：チャット指示用の分類ヘッド）を追加。

<strong>モデルのトレーニング</strong>
用意したデータセットでモデルをファインチューニング。トレーニング進捗を監視し、必要に応じてハイパーパラメータを調整。

<strong>評価と検証</strong>

検証セット：データをトレーニングセットと検証セットに分割。

<strong>パフォーマンス評価</strong>

精度、F1スコア、パープレキシティなどの指標でモデル性能を評価。

## ファインチューニングモデルの保存

<strong>チェックポイント</strong>
将来の利用に備えて、ファインチューニング済みモデルのチェックポイントを保存。

## デプロイ

- Webサービスとしてデプロイ：Microsoft Foundryでファインチューニング済みモデルをウェブサービスとしてデプロイ。
- エンドポイントのテスト：デプロイ済みエンドポイントにテストクエリを送り機能を検証。

## 反復と改善

反復：パフォーマンスが満足いかない場合は、ハイパーパラメータの調整、データ追加、さらなるエポックでのファインチューニングなどを繰り返し実施。

## 監視と洗練

モデルの挙動を継続的に監視し、必要に応じて洗練。

## カスタマイズと拡張

カスタムタスク：Phi-3 Miniはチャット指示以外の様々なタスクにもファインチューニング可能。ほかのユースケースも探索しよう！
実験：異なるアーキテクチャやレイヤー構成、手法を試し性能を向上させよう。

> [!NOTE]
> ファインチューニングは反復的なプロセスです。実験し、学び、適応して、特定のタスクに最適な結果を出しましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性に努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->