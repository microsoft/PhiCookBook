# 評估 Microsoft Foundry 中聚焦於 Microsoft 負責任 AI 原則的微調 Phi-3 / Phi-3.5 模型

本端到端（E2E）範例基於 Microsoft 技術社群的指南「[在 Microsoft Foundry 評估微調 Phi-3 / 3.5 模型，聚焦於 Microsoft 負責任 AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)」。

## 概述

### 如何在 Microsoft Foundry 評估微調 Phi-3 / Phi-3.5 模型的安全性和效能？

微調模型有時可能會導致意外或不期望的回應。為了確保模型保持安全有效，非常重要的是評估模型生成有害內容的潛在風險，以及其生成準確、相關且連貫回應的能力。在本教程中，您將學習如何評估微調後與 Prompt flow 整合的 Phi-3 / Phi-3.5 模型在 Microsoft Foundry 中的安全性和效能。

以下是 Microsoft Foundry 的評估流程。

![Architecture of tutorial.](../../../../../../translated_images/zh-MO/architecture.10bec55250f5d6a4.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 如需更詳細的資訊和探索 Phi-3 / Phi-3.5 的其他資源，請造訪 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 預備條件

- [Python](https://www.python.org/downloads)
- [Azure 訂閱](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微調後 Phi-3 / Phi-3.5 模型

### 目錄

1. [**情境 1：Microsoft Foundry 的 Prompt flow 評估介紹**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [安全性評估介紹](#安全性評估介紹)
    - [效能評估介紹](#效能評估介紹)

1. [**情境 2：在 Microsoft Foundry 評估 Phi-3 / Phi-3.5 模型**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [開始前準備](#開始前準備)
    - [部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [使用 Microsoft Foundry 的 Prompt flow 評估微調 Phi-3 / Phi-3.5 模型](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [恭喜！](#恭喜！)

## **情境 1：Microsoft Foundry 的 Prompt flow 評估介紹**

### 安全性評估介紹

為確保您的 AI 模型符合倫理且安全，至關重要的是根據 Microsoft 負責任 AI 原則進行評估。在 Microsoft Foundry 中，安全性評估可讓您評估模型對繞過防護攻擊的脆弱性及其生成有害內容的潛力，這與這些原則直接一致。

![Safaty evaluation.](../../../../../../translated_images/zh-MO/safety-evaluation.083586ec88dfa950.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft 的負責任 AI 原則

在開始技術步驟前，了解 Microsoft 負責任 AI 原則非常重要。這是一套設計用來指導 AI 系統負責任開發、部署與運作的道德框架。這些原則指引了 AI 系統的負責任設計、開發與部署，確保 AI 技術以公平、透明及包容的方式建立。這些原則是評估 AI 模型安全性的基礎。

Microsoft 的負責任 AI 原則包括：

- <strong>公平與包容</strong>：AI 系統應對所有人公平對待，避免以不同方式影響情況相似的群體。例如，當 AI 系統提供有關醫療治療、貸款申請或就業的建議時，應對具有相似症狀、財務狀況或職業資格的人提出相同建議。

- <strong>可靠性與安全性</strong>：要建立信任，AI 系統必須可靠、安全且穩定地運作。這些系統應能如設計時預期般運作，對非預期狀況安全回應，並抗拒有害操控。系統的行為及其可處理的多樣條件，反映了開發者在設計與測試過程中預見的情境範圍。

- <strong>透明性</strong>：當 AI 系統協助做出對人們生活有重大影響的決策時，人們必須了解該決策是如何產生的。例如，銀行可能使用 AI 系統判斷一名申請人是否信用良好。公司可能使用 AI 系統決定最合適的應聘人選。

- <strong>隱私與安全</strong>：隨著 AI 越來越普及，保護隱私及個人與商業資訊的安全變得更重要且複雜。AI 系統需特別關注隱私與數據安全，因系統必須取得資料，以便對人們做出準確且有依據的預測與決策。

- <strong>問責制</strong>：設計與部署 AI 系統的人必須對其系統的運作負責。組織應借鑒業界標準制定問責規範，確保 AI 系統不成為影響人們生活決策的最終權威，並確保人類持有對高度自主 AI 系統的實質控制權。

![Fill hub.](../../../../../../translated_images/zh-MO/responsibleai2.c07ef430113fad8c.webp)

*圖片來源：[什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> 如欲深入了解 Microsoft 的負責任 AI 原則，請參閱 [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)。

#### 安全度量

在本教程中，您將使用 Microsoft Foundry 的安全度量來評估微調後 Phi-3 模型的安全性。這些度量幫助您評估模型生成有害內容的可能性及其遭受繞過防護攻擊的脆弱性。安全度量包括：

- <strong>自我傷害相關內容</strong>：評估模型是否傾向產生自我傷害相關內容。
- <strong>仇恨及不公平內容</strong>：評估模型是否傾向產生仇恨或不公平內容。
- <strong>暴力內容</strong>：評估模型是否傾向產生暴力內容。
- <strong>性相關內容</strong>：評估模型是否傾向產生不當的性相關內容。

評估這些面向，確保 AI 模型不生成有害或冒犯性內容，與社會價值觀和規範標準保持一致。

![Evaluate based on safety.](../../../../../../translated_images/zh-MO/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### 效能評估介紹

為確保您的 AI 模型表現如預期，評估其效能指標非常重要。在 Microsoft Foundry 中，效能評估可讓您評估模型生成準確、相關且連貫回應的有效程度。

![Safaty evaluation.](../../../../../../translated_images/zh-MO/performance-evaluation.48b3e7e01a098740.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 效能度量

在本教程中，您將使用 Microsoft Foundry 的效能度量評估微調後的 Phi-3 / Phi-3.5 模型。這些度量幫助您評估模型生成準確、相關且連貫回答的效能。效能度量包括：

- <strong>可靠性</strong>：評估生成答案與輸入來源資訊的一致程度。
- <strong>相關性</strong>：評估生成回答對於給定問題的切題程度。
- <strong>連貫性</strong>：評估生成文本的流暢度、自然度及是否類似人類語言。
- <strong>流暢性</strong>：評估生成文本的語言表達能力。
- **與 GPT 相似度**：比較生成回答與真實標準答案的相似性。
- **F1 分數**：計算生成回答與來源資料間共用詞彙的比例。

這些度量幫助您判斷模型生成準確、相關且連貫回應的效力。

![Evaluate based on performance.](../../../../../../translated_images/zh-MO/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **情境 2：在 Microsoft Foundry 評估 Phi-3 / Phi-3.5 模型**

### 開始前準備

本教程為先前部落格文章「[使用 Prompt Flow 微調及整合自訂 Phi-3 模型：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」及「[在 Microsoft Foundry 使用 Prompt Flow 微調及整合自訂 Phi-3 模型](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」的後續。在這些文章中，我們詳細說明了在 Microsoft Foundry 中微調 Phi-3 / Phi-3.5 模型並與 Prompt flow 結合的過程。

本教程中，您將部署一個 Azure OpenAI 模型作為 Microsoft Foundry 的評估者，並用它來評估您微調的 Phi-3 / Phi-3.5 模型。

開始此教程前，請確保您已具備前述教學中描述的以下條件：

1. 用於評估微調 Phi-3 / Phi-3.5 模型的準備資料集。
1. 已微調並部署至 Azure Machine Learning 的 Phi-3 / Phi-3.5 模型。
1. 與微調後 Phi-3 / Phi-3.5 模型整合的 Microsoft Foundry 中的 Prompt flow。

> [!NOTE]
> 您將使用位於先前部落格下載的 **ULTRACHAT_200k** 資料夾中的 *test_data.jsonl* 檔案，作為評估微調 Phi-3 / Phi-3.5 模型的資料集。

#### 在 Microsoft Foundry 內使用程式碼優先方式整合自訂 Phi-3 / Phi-3.5 模型與 Prompt flow

> [!NOTE]
> 如果您依照「[在 Microsoft Foundry 使用 Prompt Flow 微調及整合自訂 Phi-3 模型](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」中描述的低程式碼方式操作，則可跳過本練習並繼續後續步驟。
> 但若您依「[使用 Prompt Flow 微調及整合自訂 Phi-3 模型：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」中說明的程式碼優先方式微調並部署 Phi-3 / Phi-3.5 模型，與 Prompt flow 連接的程序略有不同。本練習將介紹此流程。

請繼續，您需要將微調後的 Phi-3 / Phi-3.5 模型整合至 Microsoft Foundry 的 Prompt flow。

#### 建立 Microsoft Foundry Hub

在建立專案前，您需要先建立一個 Hub。Hub 類似於資源群組，能讓您組織並管理 Microsoft Foundry 中的多個專案。
1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 從左側標籤選擇 **All hubs**。

1. 從導航選單選擇 **+ New hub**。

    ![Create hub.](../../../../../../translated_images/zh-MO/create-hub.5be78fb1e21ffbf1.webp)

1. 執行以下操作：

    - 輸入 **Hub name**。此名稱必須是唯一值。
    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如有需要，請建立新的群組）。
    - 選擇您想使用的 **Location**。
    - 選擇要使用的 **Connect Azure AI Services**（如有需要，請建立新的服務）。
    - 選擇 **Connect Azure AI Search**，並選擇 **Skip connecting**。

    ![Fill hub.](../../../../../../translated_images/zh-MO/fill-hub.baaa108495c71e34.webp)

1. 選擇 **Next**。

#### 建立 Microsoft Foundry 專案

1. 在您所建立的 Hub 中，從左側標籤選擇 **All projects**。

1. 從導航選單選擇 **+ New project**。

    ![Select new project.](../../../../../../translated_images/zh-MO/select-new-project.cd31c0404088d7a3.webp)

1. 輸入 **Project name**。此名稱必須是唯一值。

    ![Create project.](../../../../../../translated_images/zh-MO/create-project.ca3b71298b90e420.webp)

1. 選擇 **Create a project**。

#### 為微調過的 Phi-3 / Phi-3.5 模型新增自訂連線

要在 Prompt flow 中整合微調過的 Phi-3 / Phi-3.5 模型，您需要將模型的端點與金鑰儲存在自訂連線中。此設定確保在 Prompt flow 中能夠存取您的微調模型。

#### 設定微調過的 Phi-3 / Phi-3.5 模型之 API 金鑰與端點 URI

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 移至您建立的 Azure 機器學習工作區。

1. 從左側標籤選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/zh-MO/select-endpoints.ee7387ecd68bd18d.webp)

1. 選擇您所建立的端點。

    ![Select endpoints.](../../../../../../translated_images/zh-MO/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. 從導航選單選擇 **Consume**。

1. 複製您的 **REST endpoint** 及 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/zh-MO/copy-endpoint-key.0650c3786bd646ab.webp)

#### 新增自訂連線

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 移至您建立的 Microsoft Foundry 專案。

1. 在該專案中，從左側標籤選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![Select new connection.](../../../../../../translated_images/zh-MO/select-new-connection.fa0f35743758a74b.webp)

1. 從導航選單選擇 **Custom keys**。

    ![Select custom keys.](../../../../../../translated_images/zh-MO/select-custom-keys.5a3c6b25580a9b67.webp)

1. 執行以下操作：

    - 選擇 **+ Add key value pairs**。
    - 鍵名稱輸入 **endpoint**，並在值欄位貼上您從 Azure ML Studio 複製的端點。
    - 再次選擇 **+ Add key value pairs**。
    - 鍵名稱輸入 **key**，並在值欄位貼上您從 Azure ML Studio 複製的金鑰。
    - 新增鍵值對後，勾選 **is secret** 以避免金鑰洩露。

    ![Add connection.](../../../../../../translated_images/zh-MO/add-connection.ac7f5faf8b10b0df.webp)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

您已在 Microsoft Foundry 新增自訂連線。現在，我們透過以下步驟建立 Prompt flow，接著將此 Prompt flow 與自訂連線連接，以在流程中使用微調模型。

1. 移至您建立的 Microsoft Foundry 專案。

1. 從左側標籤選擇 **Prompt flow**。

1. 從導航選單選擇 **+ Create**。

    ![Select Promptflow.](../../../../../../translated_images/zh-MO/select-promptflow.18ff2e61ab9173eb.webp)

1. 從導航選單選擇 **Chat flow**。

    ![Select chat flow.](../../../../../../translated_images/zh-MO/select-flow-type.28375125ec9996d3.webp)

1. 輸入要使用的 **Folder name**。

    ![Select chat flow.](../../../../../../translated_images/zh-MO/enter-name.02ddf8fb840ad430.webp)

1. 選擇 **Create**。

#### 設定 Prompt flow 與您的微調 Phi-3 / Phi-3.5 模型對話

您需要將微調的 Phi-3 / Phi-3.5 模型整合到 Prompt flow 中。但現有提供的 Prompt flow 並非設計用於此，因此必須重新設計流程以整合此自訂模型。

1. 在 Prompt flow 中，執行以下任務以重建現有流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 檔案中所有現有程式碼。
    - 將以下程式碼新增到 *flow.dag.yml*。

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

    - 選擇 **Save**。

    ![Select raw file mode.](../../../../../../translated_images/zh-MO/select-raw-file-mode.06c1eca581ce4f53.webp)

1. 將以下程式碼新增到 *integrate_with_promptflow.py*，用於在 Prompt flow 中使用自訂 Phi-3 / Phi-3.5 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 設定日誌記錄
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

        # 「connection」是自訂連線的名稱，「endpoint」、「key」是自訂連線中的鍵
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
            
            # 紀錄完整的 JSON 回應
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

    ![Paste prompt flow code.](../../../../../../translated_images/zh-MO/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> 有關在 Microsoft Foundry 中使用 Prompt flow 的更詳細資訊，請參考 [Microsoft Foundry 中的 Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input**、**Chat output** 啟用與模型的對話。

    ![Select Input Output.](../../../../../../translated_images/zh-MO/select-input-output.c187fc58f25fbfc3.webp)

1. 現在您已準備好與微調的 Phi-3 / Phi-3.5 模型對話。在下一個練習中，您將學習如何啟動 Prompt flow，並用它與您的微調模型聊天。

> [!NOTE]
>
> 重建後的流程應如下圖示例：
>
> ![Flow example](../../../../../../translated_images/zh-MO/graph-example.82fd1bcdd3fc545b.webp)
>

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![Start compute session.](../../../../../../translated_images/zh-MO/start-compute-session.9acd8cbbd2c43df1.webp)

1. 選擇 **Validate and parse input** 以更新參數。

    ![Validate input.](../../../../../../translated_images/zh-MO/validate-input.c1adb9543c6495be.webp)

1. 選擇 **connection** 的 **Value**，設為您所建立的自訂連線，例如 *connection*。

    ![Connection.](../../../../../../translated_images/zh-MO/select-connection.1f2b59222bcaafef.webp)

#### 與您的微調 Phi-3 / Phi-3.5 模型聊天

1. 選擇 **Chat**。

    ![Select chat.](../../../../../../translated_images/zh-MO/select-chat.0406bd9687d0c49d.webp)

1. 以下為結果範例：現在您可以與您的微調 Phi-3 / Phi-3.5 模型聊天。建議根據用於微調的資料提出問題。

    ![Chat with prompt flow.](../../../../../../translated_images/zh-MO/chat-with-promptflow.1cf8cea112359ada.webp)

### 部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型

要在 Microsoft Foundry 評估 Phi-3 / Phi-3.5 模型，您需要部署 Azure OpenAI 模型。此模型將用於評估 Phi-3 / Phi-3.5 模型的性能。

#### 部署 Azure OpenAI

1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 移至您所建立的 Microsoft Foundry 專案。

    ![Select Project.](../../../../../../translated_images/zh-MO/select-project-created.5221e0e403e2c9d6.webp)

1. 在該專案中，從左側標籤選擇 **Deployments**。

1. 從導航選單選擇 **+ Deploy model**。

1. 選擇 **Deploy base model**。

    ![Select Deployments.](../../../../../../translated_images/zh-MO/deploy-openai-model.95d812346b25834b.webp)

1. 選擇您想要使用的 Azure OpenAI 模型，例如 **gpt-4o**。

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/zh-MO/select-openai-model.959496d7e311546d.webp)

1. 選擇 **Confirm**。

### 使用 Microsoft Foundry 的 Prompt flow 評估微調的 Phi-3 / Phi-3.5 模型

### 開始新的評估

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 移至您所建立的 Microsoft Foundry 專案。

    ![Select Project.](../../../../../../translated_images/zh-MO/select-project-created.5221e0e403e2c9d6.webp)

1. 在該專案中，從左側標籤選擇 **Evaluation**。

1. 從導航選單選擇 **+ New evaluation**。

    ![Select evaluation.](../../../../../../translated_images/zh-MO/select-evaluation.2846ad7aaaca7f4f.webp)

1. 選擇 **Prompt flow** 評估。

    ![Select Prompt flow evaluation.](../../../../../../translated_images/zh-MO/promptflow-evaluation.cb9758cc19b4760f.webp)

1. 執行以下操作：

    - 輸入評估名稱。此名稱必須是唯一值。
    - 選擇 **Question and answer without context** 作為任務類型，因為本教學所使用的 **UlTRACHAT_200k** 資料集不包含上下文。
    - 選擇您想要評估的 Prompt flow。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-MO/evaluation-setting1.4aa08259ff7a536e.webp)

1. 選擇 **Next**。

1. 執行以下操作：

    - 選擇 **Add your dataset** 上傳資料集。例如，您可以上傳下載 **ULTRACHAT_200k** 資料集時含有的測試資料檔案，如 *test_data.json1*。
    - 選擇與您的資料集對應的 **Dataset column**。例如，若使用 **ULTRACHAT_200k** 資料集，請選擇 **${data.prompt}** 作為資料欄位。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-MO/evaluation-setting2.07036831ba58d64e.webp)

1. 選擇 **Next**。

1. 執行以下操作以設定效能與品質指標：

    - 選擇您想使用的效能與品質指標。
    - 選擇用於評估的 Azure OpenAI 模型。例如，選擇 **gpt-4o**。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-MO/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. 執行以下操作以設定風險與安全指標：

    - 選擇您想使用的風險與安全指標。
    - 選擇用於計算缺陷率的閾值，例如選擇 **Medium**。
    - 對於 **question**，將 **Data source** 設為 **{$data.prompt}**。
    - 對於 **answer**，將 **Data source** 設為 **{$run.outputs.answer}**。
    - 對於 **ground_truth**，將 **Data source** 設為 **{$data.message}**。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-MO/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. 選擇 **Next**。

1. 選擇 **Submit** 開始評估。

1. 評估將花費一些時間完成。您可以在 **Evaluation** 標籤中監控進度。

### 檢視評估結果

> [!NOTE]
> 以下呈現的結果僅用於說明評估流程。在此教學中，我們使用的小型資料集微調模型，可能導致結果不盡理想。實際結果會依據資料集大小、品質、多樣性以及模型的具體配置，產生顯著差異。

評估完成後，您可以檢視效能與安全指標的結果。
1. 性能及質量指標：

    - 評估模型在生成連貫、流暢及相關回應方面的效能。

    ![Evaluation result.](../../../../../../translated_images/zh-MO/evaluation-result-gpu.85f48b42dfb74254.webp)

1. 風險及安全指標：

    - 確保模型輸出安全，並符合負責任的 AI 原則，避免任何有害或冒犯的內容。

    ![Evaluation result.](../../../../../../translated_images/zh-MO/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. 您可以向下滾動瀏覽 <strong>詳細指標結果</strong>。

    ![Evaluation result.](../../../../../../translated_images/zh-MO/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. 透過針對性能及安全指標評估您自訂的 Phi-3 / Phi-3.5 模型，您可以確認該模型不僅有效，亦遵守負責任的 AI 實踐，準備好進行實際應用部署。

## 恭喜！

### 您已完成此教程

您已成功評估與 Prompt flow 整合的微軟 Foundry 的微調 Phi-3 模型。這是確保您的 AI 模型不僅表現良好，亦遵守微軟的負責任 AI 原則，幫助您建立值得信賴及可靠 AI 應用的重要步驟。

![Architecture.](../../../../../../translated_images/zh-MO/architecture.10bec55250f5d6a4.webp)

## 清理 Azure 資源

清理您的 Azure 資源以避免對帳戶產生額外費用。請前往 Azure 入口網站並刪除以下資源：

- Azure 機器學習資源。
- Azure 機器學習模型端點。
- Microsoft Foundry 專案資源。
- Microsoft Foundry Prompt flow 資源。

### 下一步

#### 文件

- [使用負責任 AI 儀表板評估 AI 系統](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的評估及監控指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文件](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 訓練內容

- [微軟負責任 AI 方法簡介](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 簡介](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 參考資料

- [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [宣佈 Azure AI 新工具，助您打造更安全及可靠的生成式 AI 應用](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。本公司不對因使用本翻譯所引起之任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->