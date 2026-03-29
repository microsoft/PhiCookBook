# **Microsoft FoundryでのPhi-3の使用**

生成AIの開発に伴い、異なるLLMおよびSLM、企業データ統合、ファインチューニング/RAG操作、そしてLLMとSLMを統合した後のさまざまな企業ビジネスの評価などを一元管理するプラットフォームを活用し、生成AIをスマートアプリケーションにより良く実装できることを期待しています。[Microsoft Foundry](https://ai.azure.com)は企業レベルの生成AIアプリケーションプラットフォームです。

![aistudo](../../../../translated_images/ja/aifoundry_home.f28a8127c96c7d93.webp)

Microsoft Foundryを使うことで、大規模言語モデル（LLM）の応答を評価し、プロンプトフローでプロンプトアプリケーションコンポーネントをオーケストレーションし、より良いパフォーマンスを実現できます。このプラットフォームは、概念実証から本格的なプロダクションへのスムーズなスケーラビリティを促進します。継続的なモニタリングと改善により長期的な成功をサポートします。

簡単な手順でMicrosoft FoundryにPhi-3モデルを迅速にデプロイし、その後Microsoft Foundryを使ってPhi-3関連のPlayground/Chat、ファインチューニング、評価などの関連作業を完了できます。

## **1. 準備**

すでに[Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)がマシンにインストールされている場合、このテンプレートは新しいディレクトリでこのコマンドを実行するだけで簡単に利用できます。

## 手動での作成

Microsoft Foundryでプロジェクトとハブを作成することは、AIの作業を整理し管理するのに便利です。以下は開始するためのステップバイステップガイドです：

### Microsoft Foundryでのプロジェクト作成

1. **Microsoft Foundryにアクセス**: Microsoft Foundryポータルにサインインします。
2. <strong>プロジェクトを作成</strong>:
   - プロジェクト内にいる場合は、ページ左上の「Microsoft Foundry」を選びホームページに移動します。
   - 「+ Create project」を選択します。
   - プロジェクト名を入力します。
   - ハブがある場合、デフォルトで選択されます。複数のハブにアクセス可能な場合はドロップダウンから別のハブを選択できます。新しいハブを作成したい場合は「Create new hub」を選び名前を入力します。
   - 「Create」を選択します。

### Microsoft Foundryでのハブ作成

1. **Microsoft Foundryにアクセス**: Azureアカウントでサインインします。
2. <strong>ハブを作成</strong>:
   - 左メニューから管理センターを選択します。
   - 「すべてのリソース」を選択し、「+ New project」横の下矢印をクリックし「+ New hub」を選択します。
   - 「新しいハブを作成」ダイアログでハブ名を入力（例：contoso-hub）し、その他の項目を必要に応じて変更します。
   - 「Next」を選択し、情報を確認してから「Create」を選択します。

より詳細な説明は公式の[Microsoftドキュメント](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)を参照してください。

作成に成功したら、[ai.azure.com](https://ai.azure.com/)から作成したスタジオにアクセスできます。

1つのAI Foundryには複数のプロジェクトを作成可能です。AI Foundryでプロジェクトを作成して準備を整えましょう。

Microsoft Foundryの[QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)を作成してください。


## **2. Microsoft FoundryでPhiモデルをデプロイする**

プロジェクトの「Explore」オプションをクリックしてモデルカタログに入り、Phi-3を選択します。

Phi-3-mini-4k-instructを選択します。

「Deploy」をクリックしてPhi-3-mini-4k-instructモデルをデプロイします。

> [!NOTE]
>
> デプロイ時にコンピューティングパワーを選択できます

## **3. Microsoft FoundryでPlayground Chat Phiを使う**

デプロイページに行き、Playgroundを選択し、Microsoft FoundryのPhi-3とチャットします。

## **4. Microsoft Foundryからモデルをデプロイする**

Azure Model Catalogからモデルをデプロイするには、次の手順に従います：

- Microsoft Foundryにサインインします。
- Microsoft Foundryモデルカタログからデプロイしたいモデルを選択します。
- モデルの詳細ページで「Deploy」を選択し、「Serverless API with Azure AI Content Safety」を選択します。
- モデルをデプロイしたいプロジェクトを選択します。Serverless APIを使用するには、ワークスペースがEast US 2またはSweden Centralリージョンに属している必要があります。デプロイ名はカスタマイズ可能です。
- デプロイウィザードで料金および利用規約を選択し、料金と利用条件を確認します。
- 「Deploy」を選択します。デプロイが準備できるまで待ち、完了後にDeploymentsページにリダイレクトされます。
- 「Open in playground」を選択してモデルとの対話を開始できます。
- Deploymentsページに戻り、デプロイメントを選択してエンドポイントのTarget URLとSecret Keyを確認できます。これらを使ってデプロイメントを呼び出し、補完を生成できます。
- エンドポイントの詳細、URL、およびアクセスキーはいつでもBuildタブのComponentsセクションのDeploymentsから確認できます。

> [!NOTE]
> これらの手順を実行するには、アカウントにリソースグループのAzure AI Developerロールの権限が必要です。

## **5. Microsoft FoundryでPhi APIを使う**

PostmanのGETで https://{Your project name}.region.inference.ml.azure.com/swagger.json にアクセスし、Keyと組み合わせて提供されるインターフェイスを確認できます。

リクエストパラメーターやレスポンスパラメーターを非常に便利に取得できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性の向上に努めていますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文の母国語版が正式な情報源として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->