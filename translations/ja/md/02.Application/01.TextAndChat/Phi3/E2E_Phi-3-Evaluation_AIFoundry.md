# Microsoftの責任あるAI原則に焦点を当てたMicrosoft Foundryにおけるファインチューニング済みPhi-3 / Phi-3.5モデルの評価

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。

## 概要

### Microsoft Foundryにおいてファインチューニング済みPhi-3 / Phi-3.5モデルの安全性と性能をどのように評価できますか？

モデルをファインチューニングすると、意図しないまたは望ましくない応答が生じることがあります。モデルが安全かつ効果的であることを保証するために、有害なコンテンツを生成する可能性や正確で関連性があり、一貫性のある応答を生成できる能力を評価することが重要です。このチュートリアルでは、Microsoft Foundryに統合されたPrompt flowを使ってファインチューニング済みPhi-3 / Phi-3.5モデルの安全性と性能を評価する方法を学びます。

以下はMicrosoft Foundryの評価プロセスです。

![Architecture of tutorial.](../../../../../../translated_images/ja/architecture.10bec55250f5d6a4.webp)

*画像出典: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5に関する詳細情報や追加リソースについては、[Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)をご覧ください。

### 前提条件

- [Python](https://www.python.org/downloads)
- [Azure サブスクリプション](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- ファインチューニング済みPhi-3 / Phi-3.5モデル

### 目次

1. [**シナリオ1: Microsoft FoundryのPrompt flow評価の紹介**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [安全性評価の紹介](#安全性評価の紹介)
    - [性能評価の紹介](#性能評価の紹介)

1. [**シナリオ2: Microsoft FoundryでのPhi-3 / Phi-3.5モデルの評価**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [はじめる前に](#はじめる前に)
    - [Phi-3 / Phi-3.5モデルを評価するためのAzure OpenAIのデプロイ](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft FoundryのPrompt flow評価によるファインチューニング済みPhi-3 / Phi-3.5モデルの評価](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [おめでとうございます！](#おめでとうございます！)

## **シナリオ1: Microsoft FoundryのPrompt flow評価の紹介**

### 安全性評価の紹介

AIモデルが倫理的で安全であることを保証するために、Microsoftの責任あるAI原則に沿ってモデルを評価することが重要です。Microsoft Foundryでは、安全性評価によりモデルのジェイルブレイク攻撃への脆弱性や有害コンテンツの生成可能性を評価できます。これはこれらの原則と直接的に連携しています。

![Safaty evaluation.](../../../../../../translated_images/ja/safety-evaluation.083586ec88dfa950.webp)

*画像出典: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftの責任あるAI原則

技術的な手順に入る前に、Microsoftの責任あるAI原則について理解することが重要です。これは、AIシステムの責任ある開発、展開、および運用を導く倫理的フレームワークです。これらの原則は、AI技術が公平、透明、かつ包括的な方法で構築されるように設計、開発、展開をガイドします。これらの原則はAIモデルの安全性評価の基盤です。

Microsoftの責任あるAI原則には以下が含まれます：

- <strong>公平性と包括性</strong>: AIシステムはすべての人を公平に扱い、同様の状況にある人々のグループに異なる影響を与えないことが重要です。例えば、医療治療やローン申請、雇用に関するオススメをAIシステムが行う場合、同じ症状や財務状況、職業資格を持つすべての人に同じ推奨を行うべきです。

- <strong>信頼性と安全性</strong>: 信頼を築くために、AIシステムは信頼性があり、安全かつ一貫して動作する必要があります。これらのシステムは設計どおりに動作し、予期しない状況にも安全に対応し、有害な操作に抵抗する必要があります。動作と対応可能な状況のバリエーションは、開発者が設計とテストで想定した状況の範囲を反映します。

- <strong>透明性</strong>: AIシステムが人々の生活に大きな影響を与える決定を補助する際、決定がどのように行われたかを人々が理解することが重要です。例えば、銀行が個人の信用力を判断するためにAIシステムを用いる場合や、企業が最も適格な候補者を選ぶためにAIシステムを用いる場合などです。

- <strong>プライバシーとセキュリティ</strong>: AIが広がるにつれて、プライバシーの保護と個人情報および企業情報のセキュリティ保護の重要性と複雑さが増しています。AIでは、データへのアクセスが正確で情報に基づく予測や決定に不可欠であるため、プライバシーとデータセキュリティに特別な注意が必要です。

- <strong>説明責任</strong>: AIシステムの設計と展開を行う人は、そのシステムの動作に対して説明責任を負う必要があります。組織は業界標準を参考にして説明責任の基準を設定すべきです。これらの基準はAIシステムが人々の生活に影響を与える決定の最終権限にならないようにし、人間が高度に自律的なAIシステムであっても意味のあるコントロールを保持できるようにします。

![Fill hub.](../../../../../../translated_images/ja/responsibleai2.c07ef430113fad8c.webp)

*画像出典: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoftの責任あるAI原則について詳しく知るには、[What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) をご覧ください。

#### 安全性指標

このチュートリアルでは、Microsoft Foundryの安全性指標を使用してファインチューニング済みPhi-3モデルの安全性を評価します。これらの指標は、モデルの有害コンテンツ生成傾向やジェイルブレイク攻撃への脆弱性を評価するのに役立ちます。安全性指標は以下のとおりです：

- <strong>自己傷害関連コンテンツ</strong>: モデルが自己傷害に関するコンテンツを生成する傾向があるかを評価します。
- <strong>憎悪的および不公平なコンテンツ</strong>: モデルが憎悪や不公平な内容を生成する傾向があるかを評価します。
- <strong>暴力的コンテンツ</strong>: モデルが暴力的な内容を生成する傾向があるかを評価します。
- <strong>性的コンテンツ</strong>: モデルが不適切な性的内容を生成する傾向があるかを評価します。

これらの側面を評価することで、AIモデルが有害または攻撃的なコンテンツを生成しないようにし、社会的価値観や法規制に準拠させることができます。

![Evaluate based on safety.](../../../../../../translated_images/ja/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### 性能評価の紹介

AIモデルが期待どおりに動作しているかを保証するために、性能指標に基づく評価が重要です。Microsoft Foundryでは、性能評価により正確で関連性があり、整合性のある応答を生成するモデルの効果を評価できます。

![Safaty evaluation.](../../../../../../translated_images/ja/performance-evaluation.48b3e7e01a098740.webp)

*画像出典: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 性能指標

このチュートリアルでは、Microsoft Foundryの性能指標を使用してファインチューニング済みPhi-3 / Phi-3.5モデルの性能を評価します。これらの指標は、モデルが正確で関連性があり、一貫性のある応答を生成する効果を評価するために役立ちます。性能指標は以下です：

- **基盤性（Groundedness）**: 生成された回答が入力ソースの情報とどれだけ一致しているかを評価します。
- <strong>関連性</strong>: 生成された応答が与えられた質問にどの程度関連しているかを評価します。
- **整合性（Coherence）**: 生成されたテキストがどれだけ滑らかで自然に読みやすく、人間らしい言語に似ているかを評価します。
- **流暢さ（Fluency）**: 生成されたテキストの言語運用能力を評価します。
- **GPT類似度**: 生成された応答と正解（グラウンドトゥルース）を比較し類似度を算出します。
- **F1スコア**: 生成応答とソースデータ間の共通単語割合を計算します。

これらの指標により、モデルの正確性、関連性、一貫性の効果を評価できます。

![Evaluate based on performance.](../../../../../../translated_images/ja/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **シナリオ2: Microsoft FoundryでのPhi-3 / Phi-3.5モデルの評価**

### はじめる前に

このチュートリアルは、前回のブログ記事「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」および「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」の続きです。これらの記事では、Microsoft FoundryでPhi-3 / Phi-3.5モデルのファインチューニングとPrompt flow統合の手順を紹介しました。

本チュートリアルでは、評価者としてAzure OpenAIモデルをMicrosoft Foundryにデプロイし、ファインチューニング済みPhi-3 / Phi-3.5モデルの評価に使用します。

このチュートリアルを始める前に、前のチュートリアルで説明された次の前提条件がそろっていることを確認してください：

1. ファインチューニング済みPhi-3 / Phi-3.5モデルを評価するための準備済みデータセット。
1. Azure Machine Learningにファインチューニングとデプロイ済みのPhi-3 / Phi-3.5モデル。
1. Microsoft Foundryでファインチューニング済みPhi-3 / Phi-3.5モデルと統合されたPrompt flow。

> [!NOTE]
> 前回のブログ記事でダウンロードした<strong>ULTRACHAT_200k</strong>データセットのdataフォルダにある<em>test_data.jsonl</em>ファイルを、ファインチューニング済みPhi-3 / Phi-3.5モデルの評価用データセットとして使用します。

#### Microsoft FoundryでカスタムPhi-3 / Phi-3.5モデルをPrompt flowに統合する（コードファーストアプローチ）

> [!NOTE]
> 「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」のローコードアプローチを実施した場合は、このエクササイズはスキップして次に進んでください。
> しかし、「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」のコードファーストアプローチでファインチューニングおよびデプロイされた場合、モデルのPrompt flowへの接続手順は若干異なります。このエクササイズでその方法を学びます。

続行するには、Microsoft FoundryのPrompt flowにファインチューニング済みPhi-3 / Phi-3.5モデルを統合する必要があります。

#### Microsoft Foundry Hubの作成

プロジェクトを作成する前にHubを作成する必要があります。Hubはリソースグループのような役割を果たし、Microsoft Foundry内で複数のプロジェクトを整理・管理できます。
1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にサインインします。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Create hub.](../../../../../../translated_images/ja/create-hub.5be78fb1e21ffbf1.webp)

1. 次の作業を行います：

    - **Hub name** を入力します。一意の値である必要があります。
    - Azure の **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新規作成してください）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新規作成してください）。
    - **Connect Azure AI Search** は **Skip connecting** を選択します。

    ![Fill hub.](../../../../../../translated_images/ja/fill-hub.baaa108495c71e34.webp)

1. **Next** を選択します。

#### Microsoft Foundry プロジェクトの作成

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../../../translated_images/ja/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** を入力します。一意の値である必要があります。

    ![Create project.](../../../../../../translated_images/ja/create-project.ca3b71298b90e420.webp)

1. **Create a project** を選択します。

#### ファインチューニングした Phi-3 / Phi-3.5 モデル用のカスタム接続の追加

カスタム Phi-3 / Phi-3.5 モデルを Prompt flow に統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow 内でカスタムモデルのアクセスが可能になります。

#### ファインチューニングした Phi-3 / Phi-3.5 モデルの API キーとエンドポイント URI の設定

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../../../translated_images/ja/select-endpoints.ee7387ecd68bd18d.webp)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../../../translated_images/ja/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ja/copy-endpoint-key.0650c3786bd646ab.webp)

#### カスタム接続の追加

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Microsoft Foundry プロジェクトに移動します。

1. 作成したプロジェクトで左側のタブから **Settings** を選択します。

1. **+ New connection** を選択します。

    ![Select new connection.](../../../../../../translated_images/ja/select-new-connection.fa0f35743758a74b.webp)

1. ナビゲーションメニューから **Custom keys** を選択します。

    ![Select custom keys.](../../../../../../translated_images/ja/select-custom-keys.5a3c6b25580a9b67.webp)

1. 次の作業を行います：

    - **+ Add key value pairs** を選択します。
    - キー名に **endpoint** を入力し、Azure ML Studio からコピーしたエンドポイントを値欄に貼り付けます。
    - 再度 **+ Add key value pairs** を選択します。
    - キー名に **key** を入力し、Azure ML Studio からコピーしたキーを値欄に貼り付けます。
    - キーの追加が終わったら、キーが露出しないように **is secret** を選択します。

    ![Add connection.](../../../../../../translated_images/ja/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** を選択します。

#### Prompt flow の作成

Microsoft Foundry でカスタム接続を追加しました。次に、以下の手順で Prompt flow を作成し、この Prompt flow をカスタム接続に接続してファインチューニングしたモデルを利用できるようにします。

1. 作成した Microsoft Foundry プロジェクトに移動します。

1. 左側のタブから **Prompt flow** を選択します。

1. ナビゲーションメニューから **+ Create** を選択します。

    ![Select Promptflow.](../../../../../../translated_images/ja/select-promptflow.18ff2e61ab9173eb.webp)

1. ナビゲーションメニューから **Chat flow** を選択します。

    ![Select chat flow.](../../../../../../translated_images/ja/select-flow-type.28375125ec9996d3.webp)

1. 使用する **Folder name** を入力します。

    ![Select chat flow.](../../../../../../translated_images/ja/enter-name.02ddf8fb840ad430.webp)

1. **Create** を選択します。

#### カスタム Phi-3 / Phi-3.5 モデルとチャットできるように Prompt flow の設定

ファインチューニング済み Phi-3 / Phi-3.5 モデルを Prompt flow に統合するには、既存の Prompt flow を再設計する必要があります。既存の Prompt flow はそのままではカスタムモデルの統合に対応していません。

1. Prompt flow で以下の手順に従い、既存のフローを作り直します：

    - **Raw file mode** を選択します。
    - *flow.dag.yml* ファイルの既存コードをすべて削除します。
    - 次のコードを *flow.dag.yml* に追加します。

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

    ![Select raw file mode.](../../../../../../translated_images/ja/select-raw-file-mode.06c1eca581ce4f53.webp)

1. 次のコードを *integrate_with_promptflow.py* に追加し、Prompt flow でカスタム Phi-3 / Phi-3.5 モデルを使用できるようにします。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ロギングの設定
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

        # 「connection」はカスタム接続の名前で、「endpoint」と「key」はカスタム接続内のキーです
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
            
            # 完全なJSONレスポンスをログに記録する
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

    ![Paste prompt flow code.](../../../../../../translated_images/ja/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry で Prompt flow を利用する詳細については、[Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) を参照してください。

1. モデルとのチャットを有効にするために、**Chat input** と **Chat output** を選択します。

    ![Select Input Output.](../../../../../../translated_images/ja/select-input-output.c187fc58f25fbfc3.webp)

1. これでカスタム Phi-3 / Phi-3.5 モデルとのチャット準備が整いました。次の演習では、Prompt flow の起動方法とファインチューニング済みモデルとのチャット方法を学びます。

> [!NOTE]
>
> 再構築したフローは以下の画像のようになります：
>
> ![Flow example](../../../../../../translated_images/ja/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow の開始

1. **Start compute sessions** を選択して Prompt flow を開始します。

    ![Start compute session.](../../../../../../translated_images/ja/start-compute-session.9acd8cbbd2c43df1.webp)

1. **Validate and parse input** を選択してパラメーターを更新します。

    ![Validate input.](../../../../../../translated_images/ja/validate-input.c1adb9543c6495be.webp)

1. 作成したカスタム接続の **connection** の **Value** を選択します。たとえば *connection*。

    ![Connection.](../../../../../../translated_images/ja/select-connection.1f2b59222bcaafef.webp)

#### カスタム Phi-3 / Phi-3.5 モデルとチャット

1. **Chat** を選択します。

    ![Select chat.](../../../../../../translated_images/ja/select-chat.0406bd9687d0c49d.webp)

1. こちらは結果の例です：これでファインチューニング済みのカスタム Phi-3 / Phi-3.5 モデルとチャットできます。ファインチューニングに使用したデータに基づく質問をすることをお勧めします。

    ![Chat with prompt flow.](../../../../../../translated_images/ja/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 モデルを評価するための Azure OpenAI のデプロイ

Microsoft Foundry で Phi-3 / Phi-3.5 モデルを評価するには、Azure OpenAI モデルをデプロイする必要があります。このモデルを使って Phi-3 / Phi-3.5 モデルの性能評価を行います。

#### Azure OpenAI のデプロイ

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にサインインします。

1. 作成した Microsoft Foundry プロジェクトに移動します。

    ![Select Project.](../../../../../../translated_images/ja/select-project-created.5221e0e403e2c9d6.webp)

1. 作成したプロジェクトで左側のタブから **Deployments** を選択します。

1. ナビゲーションメニューから **+ Deploy model** を選択します。

1. **Deploy base model** を選択します。

    ![Select Deployments.](../../../../../../translated_images/ja/deploy-openai-model.95d812346b25834b.webp)

1. 使用したい Azure OpenAI モデルを選択します。例として **gpt-4o**。

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ja/select-openai-model.959496d7e311546d.webp)

1. **Confirm** を選択します。

### Microsoft Foundry の Prompt flow 評価を使って、ファインチューニング済み Phi-3 / Phi-3.5 モデルを評価する

### 新しい評価の開始

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Microsoft Foundry プロジェクトに移動します。

    ![Select Project.](../../../../../../translated_images/ja/select-project-created.5221e0e403e2c9d6.webp)

1. 作成したプロジェクトで左側のタブから **Evaluation** を選択します。

1. ナビゲーションメニューから **+ New evaluation** を選択します。

    ![Select evaluation.](../../../../../../translated_images/ja/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** 評価を選択します。

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ja/promptflow-evaluation.cb9758cc19b4760f.webp)

1. 次の作業を行います：

    - 評価名を入力します。一意の値である必要があります。
    - タスクタイプには **Question and answer without context** を選択します。本チュートリアルで使用する **UlTRACHAT_200k** データセットはコンテキストを含まないためです。
    - 評価したい Prompt flow を選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/ja/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** を選択します。

1. 次の作業を行います：

    - **Add your dataset** を選択してデータセットをアップロードします。例：**ULTRACHAT_200k** データセットに含まれるテストデータファイル *test_data.json1* をアップロードできます。
    - データセットに合った **Dataset column** を選択します。例として、**ULTRACHAT_200k** データセットを使用する場合は **${data.prompt}** を選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/ja/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** を選択します。

1. パフォーマンスと品質のメトリクス設定を行います：

    - 使用したいパフォーマンスおよび品質メトリクスを選択します。
    - 評価用に作成した Azure OpenAI モデルを選択します。例：**gpt-4o**。

    ![Prompt flow evaluation.](../../../../../../translated_images/ja/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. リスクと安全性のメトリクス設定を行います：

    - 使用したいリスクおよび安全性メトリクスを選択します。
    - 欠陥率計算のしきい値を選択します。例として **Medium** を選択します。
    - **question** のデータソースには **{$data.prompt}** を選択します。
    - **answer** のデータソースには **{$run.outputs.answer}** を選択します。
    - **ground_truth** のデータソースには **{$data.message}** を選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/ja/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** を選択します。

1. **Submit** を選択して評価を開始します。

1. 評価の完了には時間がかかります。**Evaluation** タブで進捗を確認できます。

### 評価結果の確認

> [!NOTE]
> 以下に示す結果は評価手順の例示を目的としています。本チュートリアルでは比較的小規模なデータセットでファインチューニングしたモデルを使用しているため、必ずしも最適な結果とは限りません。実際の結果は、使用データセットの規模、品質、多様性、さらにはモデル構成に大きく依存して大きく異なることがあります。

評価が完了すると、パフォーマンスと安全性の両方のメトリクス結果を確認できます。
1. パフォーマンスおよび品質指標:

    - モデルが一貫性があり、流暢で関連性の高い応答を生成する効果を評価します。

    ![Evaluation result.](../../../../../../translated_images/ja/evaluation-result-gpu.85f48b42dfb74254.webp)

1. リスクおよび安全性指標:

    - モデルの出力が安全であり、責任あるAI原則に沿っていることを確認し、有害または攻撃的な内容を回避します。

    ![Evaluation result.](../../../../../../translated_images/ja/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. 下にスクロールして <strong>詳細な指標結果</strong> をご覧いただけます。

    ![Evaluation result.](../../../../../../translated_images/ja/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. パフォーマンスと安全性の両方の指標でカスタムPhi-3 / Phi-3.5モデルを評価することで、モデルが効果的であるだけでなく、責任あるAIの実践にも準拠していることを確認し、実際の運用に適した状態にできます。

## おめでとうございます！

### チュートリアルを完了しました

Microsoft FoundryのPrompt flowと統合されたファインチューニング済みのPhi-3モデルの評価に成功しました。これは、AIモデルが高性能であるだけでなく、Microsoftの責任あるAI原則を順守し、信頼性の高いAIアプリケーション構築に役立つことを保証する重要なステップです。

![Architecture.](../../../../../../translated_images/ja/architecture.10bec55250f5d6a4.webp)

## Azureリソースのクリーンアップ

アカウントへの追加料金を回避するためにAzureリソースをクリーンアップしてください。Azureポータルにアクセスし、以下のリソースを削除します：

- Azure Machine Learning リソース。
- Azure Machine Learning モデルエンドポイント。
- Microsoft Foundry プロジェクトリソース。
- Microsoft Foundry Prompt flow リソース。

### 次のステップ

#### ドキュメント

- [Responsible AI ダッシュボードを使ったAIシステムの評価](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成AIの評価および監視指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundryのドキュメント](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flowのドキュメント](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### トレーニングコンテンツ

- [Microsoftの責任あるAIアプローチ入門](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry入門](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 参考資料

- [責任あるAIとは何か？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [より安全で信頼できる生成AIアプリケーション構築を支援するAzure AIの新ツール発表](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成AIアプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご理解ください。原文の言語による文書が正式な情報源とみなされます。重要な情報については、専門の人間翻訳を推奨します。本翻訳の使用に伴う誤解や誤訳について、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->