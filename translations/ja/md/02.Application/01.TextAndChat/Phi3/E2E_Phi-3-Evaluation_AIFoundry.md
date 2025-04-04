<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7799f9e2960966adc296d24cdf0d6486",
  "translation_date": "2025-04-04T12:25:16+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ja"
}
-->
# Azure AI FoundryにおけるMicrosoftの責任あるAI原則に基づいたFine-tuned Phi-3 / Phi-3.5モデルの評価

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Azure AI FoundryでのPhi-3 / 3.5モデルの評価：Microsoftの責任あるAI原則に焦点を当てて](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。

## 概要

### Azure AI FoundryでFine-tuned Phi-3 / Phi-3.5モデルの安全性と性能をどのように評価できますか？

モデルをファインチューニングする際、意図しない、または望ましくない応答が発生する可能性があります。モデルが安全かつ効果的であることを保証するためには、モデルが有害なコンテンツを生成する可能性や、正確で関連性があり一貫性のある応答を生成する能力を評価することが重要です。このチュートリアルでは、Azure AI FoundryでPrompt flowを使用して統合されたFine-tuned Phi-3 / Phi-3.5モデルの安全性と性能を評価する方法を学びます。

以下はAzure AI Foundryの評価プロセスです。

![チュートリアルのアーキテクチャ](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ja.png)

*画像出典: [生成AIアプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5に関するより詳細な情報や追加リソースについては、[Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)をご覧ください。

### 前提条件

- [Python](https://www.python.org/downloads)
- [Azureサブスクリプション](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5モデル

### 目次

1. [**シナリオ1: Azure AI FoundryのPrompt flow評価の概要**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [安全性評価の概要](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [性能評価の概要](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**シナリオ2: Azure AI FoundryでPhi-3 / Phi-3.5モデルを評価する**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [始める前に](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure OpenAIをデプロイしてPhi-3 / Phi-3.5モデルを評価する](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI FoundryのPrompt flow評価を使用してFine-tuned Phi-3 / Phi-3.5モデルを評価する](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [おめでとうございます！](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **シナリオ1: Azure AI FoundryのPrompt flow評価の概要**

### 安全性評価の概要

AIモデルが倫理的かつ安全であることを保証するためには、Microsoftの責任あるAI原則に基づいて評価することが重要です。Azure AI Foundryでは、安全性評価により、モデルの脆弱性（例: jailbreak攻撃）や有害なコンテンツを生成する可能性を評価することができます。これらはMicrosoftの責任あるAI原則と直接連携しています。

![安全性評価](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.ja.png)

*画像出典: [生成AIアプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftの責任あるAI原則

技術的なステップに進む前に、Microsoftの責任あるAI原則について理解することが重要です。これらはAIシステムの責任ある開発、展開、運用を導くための倫理的な枠組みです。これらの原則は、公平性、透明性、包括性を確保するためにAI技術がどのように構築されるべきかを示します。これらはAIモデルの安全性を評価する基盤となります。

Microsoftの責任あるAI原則には以下が含まれます：

- **公平性と包括性**: AIシステムは全ての人々を公平に扱い、類似した状況にあるグループ間で異なる影響を与えないようにする必要があります。例えば、AIシステムが医療指導、ローン申請、または雇用に関するアドバイスを提供する場合、同じ症状、経済状況、または資格を持つ全ての人に同じ推奨を行うべきです。

- **信頼性と安全性**: 信頼を築くためには、AIシステムが信頼性が高く、安全で、一貫して動作することが重要です。これらのシステムは、設計時に意図された通りに動作し、予期しない状況に安全に対応し、有害な操作に抵抗する能力を持つべきです。

- **透明性**: AIシステムが人々の生活に大きな影響を与える意思決定を支援する場合、人々がその意思決定のプロセスを理解することが重要です。

- **プライバシーとセキュリティ**: AIが普及するにつれて、プライバシーの保護と個人情報のセキュリティ確保がますます重要かつ複雑になっています。

- **説明責任**: AIシステムを設計し展開する人々は、そのシステムの動作に対して説明責任を負うべきです。

![責任あるAIハブ](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.ja.png)

*画像出典: [責任あるAIとは？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoftの責任あるAI原則について詳しくは、[責任あるAIとは？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)をご覧ください。

#### 安全性指標

このチュートリアルでは、Azure AI Foundryの安全性指標を使用してFine-tuned Phi-3モデルの安全性を評価します。これらの指標は、モデルが有害なコンテンツを生成する可能性や、jailbreak攻撃に対する脆弱性を評価するのに役立ちます。安全性指標には以下が含まれます：

- **自傷行為関連のコンテンツ**: モデルが自傷行為に関連するコンテンツを生成する傾向を評価します。
- **憎悪的または不公平なコンテンツ**: モデルが憎悪的または不公平なコンテンツを生成する傾向を評価します。
- **暴力的なコンテンツ**: モデルが暴力的なコンテンツを生成する傾向を評価します。
- **性的なコンテンツ**: モデルが不適切な性的コンテンツを生成する傾向を評価します。

これらの評価を通じて、AIモデルが有害または不快なコンテンツを生成しないことを確認し、社会的価値観や規制基準に沿ったものとなることを保証します。

![安全性に基づく評価](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.ja.png)

### 性能評価の概要

AIモデルが期待通りに動作していることを確認するためには、性能指標に基づいて評価することが重要です。Azure AI Foundryでは、性能評価を通じて、モデルが正確で関連性があり、一貫性のある応答を生成する能力を評価できます。

![性能評価](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.ja.png)

*画像出典: [生成AIアプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 性能指標

このチュートリアルでは、Azure AI Foundryの性能指標を使用してFine-tuned Phi-3 / Phi-3.5モデルの性能を評価します。これらの指標は、モデルが正確で関連性があり、一貫性のある応答を生成する能力を評価するのに役立ちます。性能指標には以下が含まれます：

- **根拠性**: 生成された回答が入力ソースの情報とどれだけ一致しているかを評価します。
- **関連性**: 生成された応答が与えられた質問にどれだけ関連しているかを評価します。
- **一貫性**: 生成されたテキストがどれだけ滑らかで自然に読め、人間らしい言語に似ているかを評価します。
- **流暢さ**: 生成されたテキストの言語能力を評価します。
- **GPT類似性**: 生成された応答を正解データと比較して類似性を評価します。
- **F1スコア**: 生成された応答とソースデータ間で共有される単語の割合を計算します。

これらの指標を使用することで、モデルが正確で関連性があり、一貫性のある応答を生成する能力を評価できます。

![性能に基づく評価](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.ja.png)

## **シナリオ2: Azure AI FoundryでPhi-3 / Phi-3.5モデルを評価する**

### 始める前に

このチュートリアルは、以前のブログ投稿「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」および「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」の続きです。これらの投稿では、Azure AI FoundryでPhi-3 / Phi-3.5モデルをファインチューニングし、Prompt flowと統合するプロセスを説明しました。

このチュートリアルでは、Azure AI FoundryでAzure OpenAIモデルを評価者としてデプロイし、それを使用してFine-tuned Phi-3 / Phi-3.5モデルを評価します。

このチュートリアルを始める前に、以下の前提条件を確認してください。これらは以前のチュートリアルで説明されています：

1. Fine-tuned Phi-3 / Phi-3.5モデルを評価するための準備されたデータセット。
1. ファインチューニングされ、Azure Machine LearningにデプロイされたPhi-3 / Phi-3.5モデル。
1. Azure AI FoundryでPrompt flowと統合されたFine-tuned Phi-3 / Phi-3.5モデル。

> [!NOTE]
> 前回のブログ投稿でダウンロードした**ULTRACHAT_200k**データセットのデータフォルダーにある*test_data.jsonl*ファイルを、Fine-tuned Phi-3 / Phi-3.5モデルの評価用データセットとして使用します。

#### Azure AI FoundryでPrompt flowを使用してカスタムPhi-3 / Phi-3.5モデルを統合する（コードファーストアプローチ）

> [!NOTE]
> もし「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」で説明されているローコードアプローチに従った場合、この演習をスキップして次に進んでください。
> しかし、「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」で説明されているコードファーストアプローチに従ってPhi-3 / Phi-3.5モデルをファインチューニングおよびデプロイした場合、Prompt flowにモデルを接続するプロセスが少し異なります。この演習では、そのプロセスを学びます。

次に進むには、Fine-tuned Phi-3 / Phi-3.5モデルをAzure AI FoundryのPrompt flowに統合する必要があります。

#### Azure AI Foundryハブの作成

プロジェクトを作成する前に、ハブを作成する必要があります。ハブはリソースグループのような役割を果たし、Azure AI Foundry内で複数のプロジェクトを整理および管理することができます。

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)にサインインします。

1. 左側のタブから**All hubs**を選択します。

1. ナビゲーションメニューから**+ New hub**を選択します。

    ![ハブの作成](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.ja.png)

1. 以下のタスクを実行します：

    - **Hub name**を入力します。一意の値である必要があります。
    - Azureの**Subscription**を選択します。
    - 使用する**Resource group**を選択します（必要に応じて新規作成）。
    - 使用したい**Location**を選択します。
    - 使用する**Connect Azure AI Services**を選択します（必要に応じて新規作成）。
    - **Connect Azure AI Search**を**Skip connecting**に設定します。
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.ja.png)

1. **次へ** を選択します。

#### Azure AI Foundry プロジェクトを作成する

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![新しいプロジェクトを選択。](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.ja.png)

1. **Project name** を入力します。一意の値である必要があります。

    ![プロジェクトを作成。](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.ja.png)

1. **Create a project** を選択します。

#### Phi-3 / Phi-3.5 モデルの微調整版用のカスタム接続を追加する

カスタム Phi-3 / Phi-3.5 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow 内でカスタム Phi-3 / Phi-3.5 モデルにアクセスできるようになります。

#### 微調整版 Phi-3 / Phi-3.5 モデルの API キーとエンドポイント URI を設定する

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![エンドポイントを選択。](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.ja.png)

1. 作成したエンドポイントを選択します。

    ![作成したエンドポイントを選択。](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。

    ![API キーとエンドポイント URI をコピー。](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.ja.png)

#### カスタム接続を追加する

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから **Settings** を選択します。

1. **+ New connection** を選択します。

    ![新しい接続を選択。](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.ja.png)

1. ナビゲーションメニューから **Custom keys** を選択します。

    ![カスタムキーを選択。](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.ja.png)

1. 以下の手順を実行します：

    - **+ Add key value pairs** を選択します。
    - キー名に **endpoint** を入力し、Azure ML Studio からコピーしたエンドポイントを値フィールドに貼り付けます。
    - 再度 **+ Add key value pairs** を選択します。
    - キー名に **key** を入力し、Azure ML Studio からコピーしたキーを値フィールドに貼り付けます。
    - キーを追加した後、**is secret** を選択してキーが公開されないようにします。

    ![接続を追加。](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.ja.png)

1. **Add connection** を選択します。

#### Prompt flow を作成する

Azure AI Foundry にカスタム接続を追加しました。次に以下の手順で Prompt flow を作成します。この Prompt flow をカスタム接続に接続して、微調整されたモデルを使用できるようにします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 左側のタブから **Prompt flow** を選択します。

1. ナビゲーションメニューから **+ Create** を選択します。

    ![Prompt flow を選択。](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.ja.png)

1. ナビゲーションメニューから **Chat flow** を選択します。

    ![チャットフローを選択。](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.ja.png)

1. 使用する **Folder name** を入力します。

    ![チャットフローを選択。](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.ja.png)

1. **Create** を選択します。

#### カスタム Phi-3 / Phi-3.5 モデルと対話するための Prompt flow を設定する

微調整された Phi-3 / Phi-3.5 モデルを Prompt flow に統合する必要があります。ただし、提供されている既存の Prompt flow はこの目的に適していません。そのため、カスタムモデルを統合できるように Prompt flow を再設計する必要があります。

1. Prompt flow で以下の手順を実行して既存のフローを再構築します：

    - **Raw file mode** を選択します。
    - *flow.dag.yml* ファイル内の既存のコードをすべて削除します。
    - 以下のコードを *flow.dag.yml* に追加します。

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** を選択します。

    ![Raw file mode を選択。](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.ja.png)

1. カスタム Phi-3 / Phi-3.5 モデルを Prompt flow 内で使用するために、以下のコードを *integrate_with_promptflow.py* に追加します。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow のコードを貼り付け。](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.ja.png)

> [!NOTE]
> Azure AI Foundry 内で Prompt flow を使用する詳細情報については、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) を参照してください。

1. **Chat input** と **Chat output** を選択して、モデルとの対話を有効にします。

    ![入力と出力を選択。](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.ja.png)

1. これでカスタム Phi-3 / Phi-3.5 モデルと対話する準備が整いました。次の演習では、Prompt flow を開始し、微調整された Phi-3 / Phi-3.5 モデルと対話する方法を学びます。

> [!NOTE]
>
> 再構築されたフローは以下の画像のようになります：
>
> ![フローの例](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.ja.png)
>

#### Prompt flow を開始する

1. **Start compute sessions** を選択して Prompt flow を開始します。

    ![コンピュートセッションを開始。](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.ja.png)

1. **Validate and parse input** を選択してパラメータを更新します。

    ![入力を検証。](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.ja.png)

1. 作成したカスタム接続の **connection** の **Value** を選択します。例えば、*connection*。

    ![接続を選択。](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.ja.png)

#### カスタム Phi-3 / Phi-3.5 モデルと対話する

1. **Chat** を選択します。

    ![チャットを選択。](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.ja.png)

1. 以下は結果の例です：これでカスタム Phi-3 / Phi-3.5 モデルと対話できるようになります。微調整に使用したデータに基づいて質問することをお勧めします。

    ![Prompt flow とのチャット。](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.ja.png)

### Phi-3 / Phi-3.5 モデルを評価するために Azure OpenAI をデプロイする

Azure AI Foundry で Phi-3 / Phi-3.5 モデルを評価するには、Azure OpenAI モデルをデプロイする必要があります。このモデルは Phi-3 / Phi-3.5 モデルの性能を評価するために使用されます。

#### Azure OpenAI をデプロイする

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にサインインします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

    ![プロジェクトを選択。](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ja.png)

1. 作成したプロジェクトで、左側のタブから **Deployments** を選択します。

1. ナビゲーションメニューから **+ Deploy model** を選択します。

1. **Deploy base model** を選択します。

    ![デプロイメントを選択。](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.ja.png)

1. 使用する Azure OpenAI モデルを選択します。例えば、**gpt-4o**。

    ![使用する Azure OpenAI モデルを選択。](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.ja.png)

1. **Confirm** を選択します。

### Azure AI Foundry の Prompt flow 評価を使用して微調整された Phi-3 / Phi-3.5 モデルを評価する

### 新しい評価を開始する

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

    ![プロジェクトを選択。](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ja.png)

1. 作成したプロジェクトで、左側のタブから **Evaluation** を選択します。

1. ナビゲーションメニューから **+ New evaluation** を選択します。
![評価を選択します。](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.ja.png)

1. **Prompt flow** 評価を選択します。

    ![Prompt flow 評価を選択します。](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.ja.png)

1. 以下のタスクを実行します：

    - 評価名を入力します。一意の値である必要があります。
    - タスクタイプとして **Question and answer without context** を選択します。このチュートリアルで使用する **ULTRACHAT_200k** データセットにはコンテキストが含まれていないためです。
    - 評価する Prompt flow を選択します。

    ![Prompt flow 評価。](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.ja.png)

1. **Next** を選択します。

1. 以下のタスクを実行します：

    - **Add your dataset** を選択してデータセットをアップロードします。たとえば、**ULTRACHAT_200k** データセットをダウンロードすると含まれる *test_data.json1* などのテストデータセットファイルをアップロードできます。
    - データセットに対応する適切な **Dataset column** を選択します。たとえば、**ULTRACHAT_200k** データセットを使用している場合は、**${data.prompt}** をデータセット列として選択します。

    ![Prompt flow 評価。](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.ja.png)

1. **Next** を選択します。

1. パフォーマンスと品質の指標を設定するために以下のタスクを実行します：

    - 使用するパフォーマンスと品質指標を選択します。
    - 評価のために作成した Azure OpenAI モデルを選択します。たとえば、**gpt-4o** を選択します。

    ![Prompt flow 評価。](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.ja.png)

1. リスクと安全性の指標を設定するために以下のタスクを実行します：

    - 使用するリスクと安全性指標を選択します。
    - 欠陥率を計算するために使用する閾値を選択します。たとえば、**Medium** を選択します。
    - **question** には **Data source** を **{$data.prompt}** に設定します。
    - **answer** には **Data source** を **{$run.outputs.answer}** に設定します。
    - **ground_truth** には **Data source** を **{$data.message}** に設定します。

    ![Prompt flow 評価。](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.ja.png)

1. **Next** を選択します。

1. **Submit** を選択して評価を開始します。

1. 評価の完了には時間がかかる場合があります。**Evaluation** タブで進行状況を確認できます。

### 評価結果を確認する

> [!NOTE]
> 以下に示す結果は評価プロセスを説明するための例です。このチュートリアルでは比較的小規模なデータセットで微調整されたモデルを使用しているため、結果が最適でない可能性があります。実際の結果は使用するデータセットのサイズ、品質、多様性、およびモデルの具体的な設定によって大きく異なる場合があります。

評価が完了すると、パフォーマンスと安全性の指標の結果を確認できます。

1. パフォーマンスと品質指標：

    - モデルが一貫性があり流暢で関連性の高い応答を生成する能力を評価します。

    ![評価結果。](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.ja.png)

1. リスクと安全性指標：

    - モデルの出力が安全で、責任あるAIの原則に沿っており、有害または攻撃的なコンテンツを回避することを確認します。

    ![評価結果。](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.ja.png)

1. **Detailed metrics result** をスクロールして確認できます。

    ![評価結果。](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.ja.png)

1. カスタム Phi-3 / Phi-3.5 モデルをパフォーマンスと安全性の指標に基づいて評価することで、モデルが効果的であるだけでなく、責任あるAIの実践に準拠していることを確認し、実際の運用に向けた準備が整っていることを確認できます。

## おめでとうございます！

### チュートリアルを完了しました

Azure AI Foundry の Prompt flow と統合された微調整 Phi-3 モデルの評価を成功裏に完了しました。これにより、AIモデルが優れたパフォーマンスを発揮するだけでなく、Microsoftの責任あるAIの原則に従い、信頼性の高いAIアプリケーションを構築する準備が整いました。

![アーキテクチャ。](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ja.png)

## Azure リソースのクリーンアップ

Azure リソースをクリーンアップして、アカウントに追加料金が発生しないようにします。Azure ポータルに移動して、以下のリソースを削除してください：

- Azure Machine learning リソース。
- Azure Machine learning モデルエンドポイント。
- Azure AI Foundry プロジェクトリソース。
- Azure AI Foundry Prompt flow リソース。

### 次のステップ

#### ドキュメント

- [責任あるAIダッシュボードを使用してAIシステムを評価する](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成AIの評価と監視指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry ドキュメント](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow ドキュメント](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### トレーニングコンテンツ

- [Microsoftの責任あるAIアプローチの紹介](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry の紹介](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 参考資料

- [責任あるAIとは？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [より安全で信頼性の高い生成AIアプリケーションを構築するための新しいツールの発表](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成AIアプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳を推奨いたします。この翻訳の使用に起因する誤解や誤解釈について、当方は一切責任を負いません。