<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-08T05:51:00+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ja"
}
-->
# Azure AI FoundryでMicrosoftの責任あるAI原則に焦点を当てたファインチューニング済みPhi-3 / Phi-3.5モデルの評価

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。

## 概要

### Azure AI Foundryでファインチューニング済みPhi-3 / Phi-3.5モデルの安全性とパフォーマンスをどのように評価できますか？

モデルのファインチューニングは、時に意図しない、または望ましくない応答を引き起こすことがあります。モデルが安全かつ効果的であることを保証するためには、有害なコンテンツを生成する可能性や、正確で関連性が高く一貫性のある応答を生成する能力を評価することが重要です。このチュートリアルでは、Azure AI Foundryに統合されたPrompt flowを使用して、ファインチューニング済みPhi-3 / Phi-3.5モデルの安全性とパフォーマンスの評価方法を学びます。

以下はAzure AI Foundryの評価プロセスです。

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.ja.png)

*画像出典: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5に関するより詳細な情報や追加リソースについては、[Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)をご覧ください。

### 前提条件

- [Python](https://www.python.org/downloads)
- [Azureサブスクリプション](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- ファインチューニング済みPhi-3 / Phi-3.5モデル

### 目次

1. [**シナリオ1：Azure AI FoundryのPrompt flow評価の紹介**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [安全性評価の紹介](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [パフォーマンス評価の紹介](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**シナリオ2：Azure AI FoundryでのPhi-3 / Phi-3.5モデルの評価**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [始める前に](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5モデルを評価するためのAzure OpenAIのデプロイ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI FoundryのPrompt flow評価を使ったファインチューニング済みPhi-3 / Phi-3.5モデルの評価](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [おめでとうございます！](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **シナリオ1：Azure AI FoundryのPrompt flow評価の紹介**

### 安全性評価の紹介

AIモデルが倫理的かつ安全であることを保証するためには、Microsoftの責任あるAI原則に基づいて評価することが重要です。Azure AI Foundryの安全性評価では、モデルの脱獄攻撃に対する脆弱性や有害なコンテンツを生成する可能性を評価でき、これらは責任あるAI原則と直接連動しています。

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.ja.png)

*画像出典: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftの責任あるAI原則

技術的な手順に入る前に、Microsoftの責任あるAI原則について理解することが不可欠です。これはAIシステムの責任ある開発、展開、運用を導く倫理的枠組みであり、公平性、透明性、包括性を備えたAI技術の構築を促します。これらの原則はAIモデルの安全性評価の基盤となります。

Microsoftの責任あるAI原則は以下の通りです：

- **公平性と包括性**：AIシステムはすべての人を公平に扱い、類似した状況にあるグループを異なる方法で扱うことを避けるべきです。例えば、医療処置、ローン申請、雇用に関するガイダンスを提供する際、同様の症状や財務状況、資格を持つ人々に同じ推奨を行うべきです。

- **信頼性と安全性**：信頼構築のため、AIシステムは設計通りに安定して安全に動作し、予期しない状況にも安全に対応し、有害な操作に耐える必要があります。これらの挙動は設計およびテスト時に想定された状況の範囲を反映します。

- **透明性**：AIシステムが人々の生活に大きな影響を与える決定に寄与する場合、その決定がどのように行われたかを人々が理解できることが重要です。例えば、銀行が信用評価にAIを用いる場合や、企業が採用候補者の選定にAIを利用する場合などです。

- **プライバシーとセキュリティ**：AIの普及に伴い、個人情報やビジネス情報の保護がますます重要かつ複雑になっています。AIでは正確な予測や意思決定にデータアクセスが不可欠なため、プライバシーとデータセキュリティに特に注意が必要です。

- **説明責任**：AIシステムの設計および展開に携わる人々は、そのシステムの動作に対して責任を負うべきです。組織は業界標準を参考に説明責任の基準を策定し、AIシステムが人々の生活に影響を与える決定の最終権限とならないようにし、高度に自律的なAIシステムでも人間が意味のある制御を保持できるようにする必要があります。

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.ja.png)

*画像出典: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoftの責任あるAI原則についてさらに詳しく知りたい方は、[What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)をご覧ください。

#### 安全性指標

このチュートリアルでは、Azure AI Foundryの安全性指標を用いてファインチューニング済みPhi-3モデルの安全性を評価します。これらの指標は、モデルが有害なコンテンツを生成する可能性や脱獄攻撃に対する脆弱性を評価するのに役立ちます。安全性指標には以下が含まれます：

- **自己傷害関連コンテンツ**：モデルが自己傷害に関する内容を生成しやすいかどうかを評価します。
- **憎悪的・不公平なコンテンツ**：モデルが憎悪や不公平な内容を生成しやすいかどうかを評価します。
- **暴力的コンテンツ**：モデルが暴力的な内容を生成しやすいかどうかを評価します。
- **性的コンテンツ**：モデルが不適切な性的内容を生成しやすいかどうかを評価します。

これらの評価により、AIモデルが有害または攻撃的なコンテンツを生成しないことを保証し、社会的価値観や規制基準に適合させます。

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.ja.png)

### パフォーマンス評価の紹介

AIモデルが期待通りに機能していることを確認するためには、パフォーマンス指標に基づく評価が重要です。Azure AI Foundryのパフォーマンス評価では、モデルが正確で関連性が高く一貫性のある応答を生成する効果を評価できます。

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.ja.png)

*画像出典: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### パフォーマンス指標

このチュートリアルでは、Azure AI Foundryのパフォーマンス指標を用いてファインチューニング済みPhi-3 / Phi-3.5モデルのパフォーマンスを評価します。これらの指標は、モデルが正確で関連性が高く一貫性のある応答を生成する効果を評価するのに役立ちます。パフォーマンス指標には以下が含まれます：

- **根拠性（Groundedness）**：生成された回答が入力情報とどれほど整合しているかを評価します。
- **関連性（Relevance）**：生成された応答が与えられた質問にどれほど適切かを評価します。
- **一貫性（Coherence）**：生成されたテキストの流れが滑らかで自然に読めるか、人間らしい言語に近いかを評価します。
- **流暢さ（Fluency）**：生成されたテキストの言語能力を評価します。
- **GPT類似度（GPT Similarity）**：生成された応答と正解データとの類似度を比較します。
- **F1スコア**：生成された応答とソースデータ間で共有される単語の比率を計算します。

これらの指標により、モデルが正確で関連性が高く一貫性のある応答を生成する能力を評価できます。

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.ja.png)

## **シナリオ2：Azure AI FoundryでのPhi-3 / Phi-3.5モデルの評価**

### 始める前に

このチュートリアルは、以前のブログ投稿「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」および「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」の続編です。これらの投稿では、Azure AI FoundryでのPhi-3 / Phi-3.5モデルのファインチューニングとPrompt flowとの統合手順を紹介しました。

このチュートリアルでは、Azure OpenAIモデルをAzure AI Foundryの評価者としてデプロイし、それを使ってファインチューニング済みPhi-3 / Phi-3.5モデルを評価します。

このチュートリアルを始める前に、前述のチュートリアルで説明されている以下の前提条件を満たしていることを確認してください：

1. ファインチューニング済みPhi-3 / Phi-3.5モデルを評価するための準備済みデータセット。
1. ファインチューニングされAzure Machine Learningにデプロイ済みのPhi-3 / Phi-3.5モデル。
1. Azure AI Foundryでファインチューニング済みPhi-3 / Phi-3.5モデルと統合されたPrompt flow。

> [!NOTE]
> 前回のブログ投稿でダウンロードした**ULTRACHAT_200k**データセットのdataフォルダーにある*test_data.jsonl*ファイルを、ファインチューニング済みPhi-3 / Phi-3.5モデルを評価するためのデータセットとして使用します。

#### Azure AI FoundryでのPrompt flowとのカスタムPhi-3 / Phi-3.5モデルの統合（コードファーストアプローチ）

> [!NOTE]
> 「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」で説明されているローコードアプローチに従った場合は、この演習はスキップして次に進んでください。
> しかし、「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」で説明されているコードファーストアプローチに従ってPhi-3 / Phi-3.5モデルをファインチューニングおよびデプロイした場合は、モデルをPrompt flowに接続する方法が若干異なります。この演習でその方法を学びます。

続行するには、ファインチューニング済みPhi-3 / Phi-3.5モデルをAzure AI FoundryのPrompt flowに統合する必要があります。

#### Azure AI Foundry Hubの作成

Projectを作成する前にHubを作成する必要があります。Hubはリソースグループのような役割を果たし、Azure AI Foundry内で複数のProjectを整理・管理できます。

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)にサインインします。

1. 左側のタブから**All hubs**を選択します。

1. ナビゲーションメニューから**+ New hub**を選択します。

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.ja.png)

1. 以下の項目を入力または選択します：

    - **Hub name**を入力します。ユニークな値である必要があります。
    - Azureの**Subscription**を選択します。
    - 使用する**Resource group**を選択します（必要に応じて新規作成）。
    - 利用したい**Location**を選択します。
    - 使用する**Connect Azure AI Services**を選択します（必要に応じて新規作成）。
    - **Connect Azure AI Search**は**Skip connecting**を選択します。
![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.ja.png)

1. **Next** を選択します。

#### Azure AI Foundry プロジェクトの作成

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.ja.png)

1. **Project name** を入力します。一意の値である必要があります。

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.ja.png)

1. **Create a project** を選択します。

#### ファインチューニング済みの Phi-3 / Phi-3.5 モデル用のカスタム接続を追加する

カスタム Phi-3 / Phi-3.5 モデルを Prompt flow と連携させるには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。これにより、Prompt flow でカスタムモデルにアクセスできるようになります。

#### ファインチューニング済みの Phi-3 / Phi-3.5 モデルの api key と endpoint uri を設定する

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.ja.png)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.ja.png)

#### カスタム接続を追加する

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから **Settings** を選択します。

1. **+ New connection** を選択します。

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.ja.png)

1. ナビゲーションメニューから **Custom keys** を選択します。

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.ja.png)

1. 以下の操作を行います：

    - **+ Add key value pairs** を選択します。
    - キー名に **endpoint** と入力し、Azure ML Studio からコピーしたエンドポイントを値の欄に貼り付けます。
    - 再度 **+ Add key value pairs** を選択します。
    - キー名に **key** と入力し、コピーしたキーを値の欄に貼り付けます。
    - キーを追加した後、キーが漏洩しないように **is secret** を選択します。

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.ja.png)

1. **Add connection** を選択します。

#### Prompt flow の作成

Azure AI Foundry にカスタム接続を追加しました。次に、以下の手順で Prompt flow を作成します。その後、この Prompt flow をカスタム接続に接続し、ファインチューニング済みモデルを Prompt flow 内で使用できるようにします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 左側のタブから **Prompt flow** を選択します。

1. ナビゲーションメニューから **+ Create** を選択します。

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.ja.png)

1. ナビゲーションメニューから **Chat flow** を選択します。

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.ja.png)

1. 使用する **Folder name** を入力します。

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.ja.png)

1. **Create** を選択します。

#### ファインチューニング済みの Phi-3 / Phi-3.5 モデルとチャットするための Prompt flow の設定

ファインチューニング済みの Phi-3 / Phi-3.5 モデルを Prompt flow に統合する必要があります。ただし、既存の Prompt flow はこの目的に対応していないため、カスタムモデルを統合できるように Prompt flow を再設計する必要があります。

1. Prompt flow 内で、既存のフローを再構築するために以下の操作を行います：

    - **Raw file mode** を選択します。
    - *flow.dag.yml* ファイル内の既存コードをすべて削除します。
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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.ja.png)

1. 以下のコードを *integrate_with_promptflow.py* に追加し、Prompt flow でカスタム Phi-3 / Phi-3.5 モデルを使用できるようにします。

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.ja.png)

> [!NOTE]
> Azure AI Foundry での Prompt flow の詳細な使い方については、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) を参照してください。

1. **Chat input**、**Chat output** を選択して、モデルとのチャットを有効にします。

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.ja.png)

1. これでカスタム Phi-3 / Phi-3.5 モデルとチャットする準備が整いました。次の演習では、Prompt flow を開始して、ファインチューニング済みの Phi-3 / Phi-3.5 モデルとチャットする方法を学びます。

> [!NOTE]
>
> 再構築したフローは以下の画像のようになります：
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.ja.png)
>

#### Prompt flow の開始

1. **Start compute sessions** を選択して、Prompt flow を開始します。

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.ja.png)

1. **Validate and parse input** を選択してパラメーターを更新します。

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.ja.png)

1. 作成したカスタム接続の **connection** の **Value** を選択します。例：*connection*

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.ja.png)

#### カスタム Phi-3 / Phi-3.5 モデルとチャットする

1. **Chat** を選択します。

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.ja.png)

1. 結果の例は以下の通りです。これでカスタム Phi-3 / Phi-3.5 モデルとチャットが可能になりました。ファインチューニングに使用したデータに基づいた質問をすることをお勧めします。

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.ja.png)

### Phi-3 / Phi-3.5 モデルの評価のために Azure OpenAI をデプロイする

Azure AI Foundry で Phi-3 / Phi-3.5 モデルを評価するには、Azure OpenAI モデルをデプロイする必要があります。このモデルは Phi-3 / Phi-3.5 モデルの性能評価に使用されます。

#### Azure OpenAI のデプロイ

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にサインインします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.ja.png)

1. 作成したプロジェクトで、左側のタブから **Deployments** を選択します。

1. ナビゲーションメニューから **+ Deploy model** を選択します。

1. **Deploy base model** を選択します。

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.ja.png)

1. 使用したい Azure OpenAI モデルを選択します。例：**gpt-4o**

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.ja.png)

1. **Confirm** を選択します。

### Azure AI Foundry の Prompt flow 評価を使ってファインチューニング済み Phi-3 / Phi-3.5 モデルを評価する

### 新しい評価を開始する

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.ja.png)

1. 作成したプロジェクトで、左側のタブから **Evaluation** を選択します。

1. ナビゲーションメニューから **+ New evaluation** を選択します。
![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.ja.png)

1. **Prompt flow** の評価を選択します。

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.ja.png)

1. 次の作業を行います：

    - 評価名を入力します。一意の値である必要があります。
    - タスクタイプとして **Question and answer without context** を選択します。このチュートリアルで使用する **UlTRACHAT_200k** データセットにはコンテキストが含まれていないためです。
    - 評価したいプロンプトフローを選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.ja.png)

1. **Next** を選択します。

1. 次の作業を行います：

    - **Add your dataset** を選択してデータセットをアップロードします。例えば、**ULTRACHAT_200k** データセットをダウンロードした際に含まれる *test_data.json1* のようなテストデータセットファイルをアップロードできます。
    - データセットに対応する適切な **Dataset column** を選択します。例えば、**ULTRACHAT_200k** データセットを使用している場合は、**${data.prompt}** をデータセット列として選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.ja.png)

1. **Next** を選択します。

1. パフォーマンスと品質の指標を設定するために次の作業を行います：

    - 使用したいパフォーマンスおよび品質の指標を選択します。
    - 評価用に作成した Azure OpenAI モデルを選択します。例えば、**gpt-4o** を選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.ja.png)

1. リスクおよび安全性の指標を設定するために次の作業を行います：

    - 使用したいリスクおよび安全性の指標を選択します。
    - 欠陥率を計算するためのしきい値を選択します。例えば、**Medium** を選択します。
    - **question** には **Data source** として **{$data.prompt}** を選択します。
    - **answer** には **Data source** として **{$run.outputs.answer}** を選択します。
    - **ground_truth** には **Data source** として **{$data.message}** を選択します。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.ja.png)

1. **Next** を選択します。

1. **Submit** を選択して評価を開始します。

1. 評価の完了にはしばらく時間がかかります。進捗は **Evaluation** タブで確認できます。

### 評価結果の確認

> [!NOTE]
> 以下に示す結果は評価プロセスの説明を目的としています。このチュートリアルでは比較的小規模なデータセットでファインチューニングしたモデルを使用しているため、最適な結果とは限りません。実際の結果は、使用するデータセットのサイズ、品質、多様性、およびモデルの具体的な設定によって大きく異なる場合があります。

評価が完了したら、パフォーマンスと安全性の両方の指標について結果を確認できます。

1. パフォーマンスと品質の指標：

    - モデルが一貫性があり流暢で関連性の高い応答を生成できるかを評価します。

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.ja.png)

1. リスクと安全性の指標：

    - モデルの出力が安全であり、責任あるAIの原則に沿って有害または不快な内容を避けているかを確認します。

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.ja.png)

1. 下にスクロールして **Detailed metrics result** を表示できます。

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.ja.png)

1. パフォーマンスと安全性の両方の指標でカスタムの Phi-3 / Phi-3.5 モデルを評価することで、モデルが効果的であるだけでなく、責任あるAIの実践にも準拠していることを確認でき、実運用に適した状態であることがわかります。

## おめでとうございます！

### チュートリアルを完了しました

Azure AI Foundry に統合されたファインチューニング済みの Phi-3 モデルの評価に成功しました。これは、AIモデルが高性能であるだけでなく、Microsoft の責任あるAIの原則に従い、信頼性の高いAIアプリケーションを構築するための重要なステップです。

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.ja.png)

## Azure リソースのクリーンアップ

追加の料金発生を防ぐために、Azure ポータルにアクセスして以下のリソースを削除してください：

- Azure Machine learning リソース
- Azure Machine learning モデルエンドポイント
- Azure AI Foundry プロジェクトリソース
- Azure AI Foundry Prompt flow リソース

### 次のステップ

#### ドキュメント

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### トレーニングコンテンツ

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 参考

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や誤訳についても、一切の責任を負いかねますのでご了承ください。