# 在 Microsoft Foundry 中評估微調後的 Phi-3 / Phi-3.5 模型，重點關注 Microsoft 的負責任 AI 原則

此端對端 (E2E) 範例基於 Microsoft 技術社區的指南「[在 Microsoft Foundry 中評估微調的 Phi-3 / 3.5 模型，重點關注 Microsoft 的負責任 AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)」。

## 概述

### 如何在 Microsoft Foundry 中評估微調後的 Phi-3 / Phi-3.5 模型的安全性與性能？

微調模型有時可能導致未預期或不理想的回應。為確保模型保持安全與有效，評估模型生成有害內容的潛力及其產生準確、相關且連貫回應的能力非常重要。在本教學中，您將學習如何評估整合于 Microsoft Foundry 中的 Prompt flow 的微調後 Phi-3 / Phi-3.5 模型的安全性與性能。

以下是 Microsoft Foundry 的評估流程。

![Architecture of tutorial.](../../../../../../translated_images/zh-HK/architecture.10bec55250f5d6a4.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 欲了解更多關於 Phi-3 / Phi-3.5 的詳細資訊及相關資源，請參閱 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 前置條件

- [Python](https://www.python.org/downloads)
- [Azure 訂閱](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微調後的 Phi-3 / Phi-3.5 模型

### 目錄

1. [**情境 1：Microsoft Foundry 的 Prompt flow 評估簡介**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [安全性評估簡介](#安全性評估簡介)
    - [性能評估簡介](#性能評估簡介)

1. [**情境 2：在 Microsoft Foundry 中評估 Phi-3 / Phi-3.5 模型**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [開始之前](#開始之前)
    - [部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [使用 Microsoft Foundry 的 Prompt flow 評估微調後的 Phi-3 / Phi-3.5 模型](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [恭喜完成！](#恭喜！)

## **情境 1：Microsoft Foundry 的 Prompt flow 評估簡介**

### 安全性評估簡介

為確保您的 AI 模型合乎道德且安全，有必要依據 Microsoft 的負責任 AI 原則來評估模型。在 Microsoft Foundry 中，安全評估讓您評估模型面對繞過防護攻擊（jailbreak）時的脆弱性以及生成有害內容的可能性，這與負責任 AI 原則直接相關。

![Safaty evaluation.](../../../../../../translated_images/zh-HK/safety-evaluation.083586ec88dfa950.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft 的負責任 AI 原則

在開始技術步驟前，務必了解 Microsoft 的負責任 AI 原則，這是指導負責任開發、部署及運作 AI 系統的倫理框架。這些原則指導 AI 的負責任設計、開發和部署，確保 AI 技術以公平、透明且包容的方式建構，也是評估 AI 模型安全性的基礎。

Microsoft 的負責任 AI 原則包括：

- <strong>公平與包容</strong>：AI 系統應公平對待所有人，避免對處境類似的人群採取不同對待。例如，當 AI 系統提供醫療治療、貸款申請或就業指引時，應對症狀相似、財務狀況相似或專業資格相當的人提出相同建議。

- <strong>可靠性與安全性</strong>：建立信任的關鍵在於 AI 系統必須可靠、安全且穩定運作。系統應能按照原設計運行，對未預期狀況做出安全回應，並抵抗有害操縱。其行為與能處理的情況範圍反映開發者在設計和測試階段所預見的情境與條件。

- <strong>透明度</strong>：當 AI 系統協助做出對人生命有巨大影響的決策時，人們必須理解這些決策是如何作出的。例如，銀行使用 AI 判斷信用評分；公司使用 AI 來挑選最合適的求職者。

- <strong>隱私與安全</strong>：隨著 AI 的普及，保護隱私及個人與商業資料安全的重要性與複雜性日增。AI 對資料的存取關係到其能否做出準確且有根據的預測與決策，隱私和資料安全因此更需被重視。

- <strong>問責制</strong>：設計與部署 AI 系統的人必須對系統運作負責。組織應利用業界標準設立問責規範，確保 AI 系統不成為影響人生命決策的最終權威，並確保人類對高度自治的 AI 系統維持實質控制。

![Fill hub.](../../../../../../translated_images/zh-HK/responsibleai2.c07ef430113fad8c.webp)

*圖片來源：[什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> 欲深入了解 Microsoft 的負責任 AI 原則，請參考 [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)。

#### 安全指標

在本教學中，您將使用 Microsoft Foundry 的安全指標評估微調後的 Phi-3 模型安全性。這些指標幫助您評估模型生成有害內容的潛力及其防範繞過防護（jailbreak）攻擊的能力。安全指標包括：

- <strong>自我傷害相關內容</strong>：評估模型是否傾向產生與自我傷害相關的內容。
- <strong>仇恨及不公平內容</strong>：評估模型是否傾向產生仇恨或不公平內容。
- <strong>暴力內容</strong>：評估模型是否傾向產生暴力內容。
- <strong>性內容</strong>：評估模型是否傾向產生不適當的性相關內容。

評估這些面向可確保 AI 模型不會產生有害或冒犯性內容，並符合社會價值與法規標準。

![Evaluate based on safety.](../../../../../../translated_images/zh-HK/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### 性能評估簡介

為確保 AI 模型如預期運作，重要的是根據性能指標評估其表現。在 Microsoft Foundry 中，性能評估讓您評估模型在產生準確、相關且連貫回應上的效能。

![Safaty evaluation.](../../../../../../translated_images/zh-HK/performance-evaluation.48b3e7e01a098740.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 性能指標

在本教學中，您將使用 Microsoft Foundry 的性能指標評估微調後的 Phi-3 / Phi-3.5 模型。這些指標幫助您評估模型產生準確、相關且連貫回應的效能。性能指標包括：

- **根據性（Groundedness）**：評估生成回應與輸入資訊的契合度。
- **相關性（Relevance）**：評估生成回應對於題目的相關性。
- **連貫性（Coherence）**：評估生成文字的流暢度、自然度和類似人類語言的程度。
- **流利度（Fluency）**：評估生成文字的語言能力。
- **GPT 相似度（GPT Similarity）**：比較生成回應與真實答案的相似度。
- **F1 分數**：計算生成回應和來源資料詞彙的重疊比例。

這些指標幫助您評估模型在產生準確、相關且連貫回應上的有效性。

![Evaluate based on performance.](../../../../../../translated_images/zh-HK/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **情境 2：在 Microsoft Foundry 中評估 Phi-3 / Phi-3.5 模型**

### 開始之前

本教學是先前兩篇部落格文章「[使用 Prompt Flow 微調及整合自訂 Phi-3 模型：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」及「[在 Microsoft Foundry 中使用 Prompt Flow 微調及整合自訂 Phi-3 模型](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」的延續。在這些文章中，我們展示了如何在 Microsoft Foundry 中微調 Phi-3 / Phi-3.5 模型並整合至 Prompt flow。

在本教學中，您將部署 Azure OpenAI 模型作為評估者於 Microsoft Foundry，並用它來評估您的微調 Phi-3 / Phi-3.5 模型。

開始本教學前，請確保您已完成前述教學中提及的下列前置條件：

1. 已準備好評估微調 Phi-3 / Phi-3.5 模型的資料集。
1. 已微調且部署至 Azure Machine Learning 的 Phi-3 / Phi-3.5 模型。
1. 已在 Microsoft Foundry 中整合微調後 Phi-3 / Phi-3.5 模型的 Prompt flow。

> [!NOTE]
> 您將使用先前部落格文章中下載的 **ULTRACHAT_200k** 資料夾中的 *test_data.jsonl* 檔案作為評估微調 Phi-3 / Phi-3.5 模型的資料集。

#### 在 Microsoft Foundry 中將自訂 Phi-3 / Phi-3.5 模型整合至 Prompt flow（程式碼優先方法）

> [!NOTE]
> 若您採用「[在 Microsoft Foundry 中使用 Prompt Flow 微調及整合自訂 Phi-3 模型](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」所描述的低碼方法，您可以跳過此練習，直接進入下一步。
> 不過，若您使用「[使用 Prompt Flow 微調及整合自訂 Phi-3 模型：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」所述的程式碼優先方法來微調並部署您的 Phi-3 / Phi-3.5 模型，連接模型至 Prompt flow 的流程會略有不同，您將在此練習中學習該流程。

接下來，您需要將微調後的 Phi-3 / Phi-3.5 模型整合至 Microsoft Foundry 的 Prompt flow。

#### 創建 Microsoft Foundry Hub

在建立 Project 之前，您需要先創建 Hub。Hub 類似資源群組，方便您在 Microsoft Foundry 中組織與管理多個 Project。
1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 從左側分頁選擇 **All hubs**。

1. 從導覽選單選擇 **+ New hub**。

    ![Create hub.](../../../../../../translated_images/zh-HK/create-hub.5be78fb1e21ffbf1.webp)

1. 執行以下操作：

    - 輸入 **Hub name**。此名稱必須是唯一值。
    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如有需要，請建立新的）。
    - 選擇您想使用的 **Location**。
    - 選擇要連接的 **Azure AI Services**（如有需要，請建立新的）。
    - 在 **Connect Azure AI Search** 中選擇 **Skip connecting**。

    ![Fill hub.](../../../../../../translated_images/zh-HK/fill-hub.baaa108495c71e34.webp)

1. 選擇 **Next**。

#### 建立 Microsoft Foundry 專案

1. 在您建立的 Hub 中，從左側分頁選擇 **All projects**。

1. 從導覽選單選擇 **+ New project**。

    ![Select new project.](../../../../../../translated_images/zh-HK/select-new-project.cd31c0404088d7a3.webp)

1. 輸入 **Project name**。此名稱必須是唯一值。

    ![Create project.](../../../../../../translated_images/zh-HK/create-project.ca3b71298b90e420.webp)

1. 選擇 **Create a project**。

#### 新增自訂連線以連接微調後的 Phi-3 / Phi-3.5 模型

要在 Prompt flow 中整合您的自訂 Phi-3 / Phi-3.5 模型，您需要將模型的端點和金鑰儲存在自訂連線中。此設定用以確保在 Prompt flow 中能使用您的自訂 Phi-3 / Phi-3.5 模型。

#### 設定微調後 Phi-3 / Phi-3.5 模型的 api key 和 endpoint uri

1. 前往 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Azure 機器學習工作區。

1. 從左側分頁選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/zh-HK/select-endpoints.ee7387ecd68bd18d.webp)

1. 選擇您建立的端點。

    ![Select endpoints.](../../../../../../translated_images/zh-HK/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. 從導覽選單選擇 **Consume**。

1. 複製您的 **REST endpoint** 與 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/zh-HK/copy-endpoint-key.0650c3786bd646ab.webp)

#### 新增自訂連線

1. 前往 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 在您建立的專案中，從左側分頁選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![Select new connection.](../../../../../../translated_images/zh-HK/select-new-connection.fa0f35743758a74b.webp)

1. 從導覽選單選擇 **Custom keys**。

    ![Select custom keys.](../../../../../../translated_images/zh-HK/select-custom-keys.5a3c6b25580a9b67.webp)

1. 執行以下操作：

    - 選擇 **+ Add key value pairs**。
    - 在鍵名稱輸入 **endpoint**，並將您從 Azure ML Studio 複製的端點貼到值欄位。
    - 再次選擇 **+ Add key value pairs**。
    - 在鍵名稱輸入 **key**，並將您從 Azure ML Studio 複製的金鑰貼到值欄位。
    - 新增金鑰後，勾選 **is secret** 以免金鑰外露。

    ![Add connection.](../../../../../../translated_images/zh-HK/add-connection.ac7f5faf8b10b0df.webp)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

您已在 Microsoft Foundry 新增自訂連線。接著，請使用以下步驟建立 Prompt flow，然後將此 Prompt flow 連結至自訂連線，以便在 Prompt flow 中使用微調模型。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 從左側分頁選擇 **Prompt flow**。

1. 從導覽選單選擇 **+ Create**。

    ![Select Promptflow.](../../../../../../translated_images/zh-HK/select-promptflow.18ff2e61ab9173eb.webp)

1. 從導覽選單選擇 **Chat flow**。

    ![Select chat flow.](../../../../../../translated_images/zh-HK/select-flow-type.28375125ec9996d3.webp)

1. 輸入要使用的 **Folder name**。

    ![Select chat flow.](../../../../../../translated_images/zh-HK/enter-name.02ddf8fb840ad430.webp)

1. 選擇 **Create**。

#### 設定 Prompt flow 與您的自訂 Phi-3 / Phi-3.5 模型對話

您需要將微調後的 Phi-3 / Phi-3.5 模型整合至 Prompt flow 中。現有的 Prompt flow 不是為此用途設計，因此，您必須重新設計 Prompt flow 以實現自訂模型的整合。

1. 在 Prompt flow 中，進行以下步驟以重建現有流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 檔案中的所有既有程式碼。
    - 將以下程式碼新增至 *flow.dag.yml*。

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

    ![Select raw file mode.](../../../../../../translated_images/zh-HK/select-raw-file-mode.06c1eca581ce4f53.webp)

1. 在 *integrate_with_promptflow.py* 檔案新增以下程式碼，以在 Prompt flow 中使用自訂 Phi-3 / Phi-3.5 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 記錄設置
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

        # 「connection」是自訂連接的名稱，「endpoint」、「key」是自訂連接中的關鍵字
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
            
            # 記錄完整的 JSON 回應
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

    ![Paste prompt flow code.](../../../../../../translated_images/zh-HK/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> 如需 Microsoft Foundry 中使用 Prompt flow 的更多詳細資訊，請參閱 [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input** 和 **Chat output** 以啟用與模型的對話。

    ![Select Input Output.](../../../../../../translated_images/zh-HK/select-input-output.c187fc58f25fbfc3.webp)

1. 現在，您已準備好與自訂的 Phi-3 / Phi-3.5 模型對話。在下一個練習中，您將學習如何啟動 Prompt flow 並使用它與您的微調 Phi-3 / Phi-3.5 模型進行對話。

> [!NOTE]
>
> 重新建構的流程應如以下圖片所示：
>
> ![Flow example](../../../../../../translated_images/zh-HK/graph-example.82fd1bcdd3fc545b.webp)
>

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![Start compute session.](../../../../../../translated_images/zh-HK/start-compute-session.9acd8cbbd2c43df1.webp)

1. 選擇 **Validate and parse input** 以更新參數。

    ![Validate input.](../../../../../../translated_images/zh-HK/validate-input.c1adb9543c6495be.webp)

1. 選擇 **connection** 的 **Value**，並設定為您建立的自訂連線。例如，*connection*。

    ![Connection.](../../../../../../translated_images/zh-HK/select-connection.1f2b59222bcaafef.webp)

#### 與您的自訂 Phi-3 / Phi-3.5 模型聊天

1. 選擇 **Chat**。

    ![Select chat.](../../../../../../translated_images/zh-HK/select-chat.0406bd9687d0c49d.webp)

1. 以下是結果範例：您現在可以與您自訂的 Phi-3 / Phi-3.5 模型聊天。建議根據用於微調的資料提問。

    ![Chat with prompt flow.](../../../../../../translated_images/zh-HK/chat-with-promptflow.1cf8cea112359ada.webp)

### 部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型

要在 Microsoft Foundry 中評估 Phi-3 / Phi-3.5 模型，您需要部署 Azure OpenAI 模型。此模型將用於評估 Phi-3 / Phi-3.5 模型的效能。

#### 部署 Azure OpenAI

1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

    ![Select Project.](../../../../../../translated_images/zh-HK/select-project-created.5221e0e403e2c9d6.webp)

1. 在您建立的專案中，從左側分頁選擇 **Deployments**。

1. 從導覽選單選擇 **+ Deploy model**。

1. 選擇 **Deploy base model**。

    ![Select Deployments.](../../../../../../translated_images/zh-HK/deploy-openai-model.95d812346b25834b.webp)

1. 選擇您想使用的 Azure OpenAI 模型。例如，**gpt-4o**。

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/zh-HK/select-openai-model.959496d7e311546d.webp)

1. 選擇 **Confirm**。

### 使用 Microsoft Foundry 的 Prompt flow 評估微調後 Phi-3 / Phi-3.5 模型

### 啟動新的評估

1. 前往 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

    ![Select Project.](../../../../../../translated_images/zh-HK/select-project-created.5221e0e403e2c9d6.webp)

1. 在您建立的專案中，從左側分頁選擇 **Evaluation**。

1. 從導覽選單選擇 **+ New evaluation**。

    ![Select evaluation.](../../../../../../translated_images/zh-HK/select-evaluation.2846ad7aaaca7f4f.webp)

1. 選擇 **Prompt flow** 評估。

    ![Select Prompt flow evaluation.](../../../../../../translated_images/zh-HK/promptflow-evaluation.cb9758cc19b4760f.webp)

1. 執行以下操作：

    - 輸入評估名稱。必須是唯一值。
    - 選擇任務類型為 **Question and answer without context**，因為本教學使用的 **ULTRACHAT_200k** 資料集不含上下文。
    - 選擇您想評估的 Prompt flow。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-HK/evaluation-setting1.4aa08259ff7a536e.webp)

1. 選擇 **Next**。

1. 執行以下操作：

    - 選擇 **Add your dataset** 以上傳資料集。例如，您可以上傳包含於 **ULTRACHAT_200k** 資料集下載包中的測試資料檔案，如 *test_data.json1*。
    - 選擇符合您資料集的<strong>Dataset column</strong>。例如，使用 **ULTRACHAT_200k** 資料集時，選擇 **${data.prompt}** 作為資料欄。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-HK/evaluation-setting2.07036831ba58d64e.webp)

1. 選擇 **Next**。

1. 執行以下設定，配置效能與品質指標：

    - 選擇您希望使用的效能與品質指標。
    - 選擇您為評估建立的 Azure OpenAI 模型。例如，選擇 **gpt-4o**。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-HK/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. 執行以下設定，配置風險與安全指標：

    - 選擇您希望使用的風險與安全指標。
    - 選擇用於計算缺陷率的閾值。例如，選擇 **Medium**。
    - 對於 **question**，將 **Data source** 設定為 **{$data.prompt}**。
    - 對於 **answer**，將 **Data source** 設定為 **{$run.outputs.answer}**。
    - 對於 **ground_truth**，將 **Data source** 設定為 **{$data.message}**。

    ![Prompt flow evaluation.](../../../../../../translated_images/zh-HK/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. 選擇 **Next**。

1. 選擇 **Submit** 以開始評估。

1. 評估將花費一些時間完成。您可以在 **Evaluation** 分頁中監控進度。

### 檢視評估結果

> [!NOTE]
> 以下結果僅用於說明評估流程。在本教學中，我們使用的是以相對較小資料集微調的模型，因此結果可能不理想。實際結果會根據資料集的規模、品質、多樣性與模型的具體設定而有顯著差異。

評估完成後，您可以檢視效能與安全指標的結果。
1. 性能和質量指標：

    - 評估模型在生成連貫、流暢及相關回應方面的效能。

    ![Evaluation result.](../../../../../../translated_images/zh-HK/evaluation-result-gpu.85f48b42dfb74254.webp)

1. 風險和安全指標：

    - 確保模型的輸出是安全的，並符合負責任 AI 原則，避免任何有害或冒犯性內容。

    ![Evaluation result.](../../../../../../translated_images/zh-HK/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. 你可以向下滾動查看 <strong>詳細指標結果</strong>。

    ![Evaluation result.](../../../../../../translated_images/zh-HK/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. 透過評估你自訂的 Phi-3 / Phi-3.5 模型在性能和安全指標上的表現，你可以確認該模型不僅有效，還遵守負責任 AI 實踐，準備好用於現實世界部署。

## 恭喜！

### 你已完成本教學

你已成功評估整合於 Microsoft Foundry 中、經過微調的 Phi-3 模型。這是確保你的 AI 模型不僅效能優異，還遵守微軟負責任 AI 原則的重要步驟，能幫助你構建可信賴且可靠的 AI 應用程式。

![Architecture.](../../../../../../translated_images/zh-HK/architecture.10bec55250f5d6a4.webp)

## 清理 Azure 資源

請清理你的 Azure 資源，以避免產生額外費用。前往 Azure 入口網站並刪除以下資源：

- Azure 機器學習資源。
- Azure 機器學習模型端點。
- Microsoft Foundry 項目資源。
- Microsoft Foundry Prompt flow 資源。

### 下一步

#### 文件資源

- [使用負責任 AI 儀表板評估 AI 系統](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的評估與監控指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文件](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 培訓內容

- [微軟負責任 AI 方法介紹](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 簡介](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 參考資料

- [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [宣佈 Azure AI 中的新工具，協助你構建更安全且可靠的生成式 AI 應用程式](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不承擔因使用此翻譯而引起的任何誤解或誤釋之責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->