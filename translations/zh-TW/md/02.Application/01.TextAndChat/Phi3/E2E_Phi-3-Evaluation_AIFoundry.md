# 在 Microsoft Foundry 評估微調後的 Phi-3 / Phi-3.5 模型，重點落在微軟的負責任 AI 原則

此端對端 (E2E) 範例基於 Microsoft Tech Community 的指南「[在 Microsoft Foundry 中評估微調後的 Phi-3 / 3.5 模型，聚焦於微軟的負責任 AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)」。

## 概述

### 如何在 Microsoft Foundry 評估微調後的 Phi-3 / Phi-3.5 模型的安全性和效能？

模型微調有時可能導致非預期或不理想的回應。為確保模型保持安全且有效，評估模型產生有害內容的潛力以及生成準確、相關且連貫回應的能力非常重要。本教學將教你如何評估在 Microsoft Foundry 中結合 Prompt flow 的微調 Phi-3 / Phi-3.5 模型的安全性與效能。

以下為 Microsoft Foundry 的評估流程。

![教學架構圖。](../../../../../../translated_images/zh-TW/architecture.10bec55250f5d6a4.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 若想獲得更詳細資訊及探索關於 Phi-3 / Phi-3.5 的更多資源，請造訪 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 預備知識

- [Python](https://www.python.org/downloads)
- [Azure 訂閱](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微調後的 Phi-3 / Phi-3.5 模型

### 目錄

1. [**情境 1：Microsoft Foundry 的 Prompt flow 評估介紹**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [安全性評估介紹](#安全性評估介紹)
    - [效能評估介紹](#效能評估介紹)

1. [**情境 2：在 Microsoft Foundry 評估 Phi-3 / Phi-3.5 模型**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [開始之前](#開始之前)
    - [部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [使用 Microsoft Foundry 的 Prompt flow 評估微調後的 Phi-3 / Phi-3.5 模型](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [恭喜你！](#恭喜！)

## **情境 1：Microsoft Foundry 的 Prompt flow 評估介紹**

### 安全性評估介紹

為確保你的 AI 模型具備倫理性與安全性，評估該模型是否符合微軟的負責任 AI 原則是關鍵。在 Microsoft Foundry 中，安全性評估能讓你檢視模型對破解攻擊的脆弱性以及產生有害內容的潛力，這與這些原則直接相符。

![安全性評估。](../../../../../../translated_images/zh-TW/safety-evaluation.083586ec88dfa950.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 微軟的負責任 AI 原則

在開始技術步驟之前，理解微軟的負責任 AI 原則非常重要，這是一套指導 AI 系統負責任開發、部署和運作的倫理框架。這些原則指引 AI 系統的負責任設計、開發和部署，確保 AI 技術以公平、透明及包容的方式建立。這些原則是評估 AI 模型安全性的基礎。

微軟的負責任 AI 原則包括：

- <strong>公平性與包容性</strong>：AI 系統應公平對待所有人，並避免對處境相似的人群採取不同方式的影響。例如，當 AI 系統提供醫療治療、貸款申請或就業建議時，應對所有具備相似症狀、財務狀況或專業資格的人給出相同建議。

- <strong>可靠性與安全性</strong>：為建立信任，AI 系統必須可靠、安全且持續一致地運作。這些系統應能依設計運作，對預期之外的狀況以安全方式反應，並能抵抗有害的操控。其行為與可處理的狀況範圍反映出開發者於設計與測試階段預期的各種情境。

- <strong>透明性</strong>：當 AI 系統協助作出對人民生活有深遠影響的決策時，讓人理解決策過程相當重要。例如，銀行可能使用 AI 系統判斷個人是否具有信用；公司可能用 AI 系統篩選最合適的應徵者人選。

- <strong>隱私與安全</strong>：隨著 AI 普及，保護隱私與個人及企業資訊安全變得越來越重要且複雜。對於 AI 來說，隱私與資料安全需特別注意，因為 AI 系統需接觸資料才能做出精確且有根據的預測與決策。

- <strong>問責制</strong>：設計與部署 AI 系統的人必須對系統運作負責。組織應依產業標準建立問責規範。此規範可確保 AI 系統不成為決定人民生活重要事項的最終權威，也確保人在高度自主的 AI 系統中維持實質的控制權。

![完整示意圖。](../../../../../../translated_images/zh-TW/responsibleai2.c07ef430113fad8c.webp)

*圖片來源：[什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> 想了解更多微軟的負責任 AI 原則，請造訪 [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)。

#### 安全性指標

在此教學中，你將使用 Microsoft Foundry 的安全性指標來評估微調後的 Phi-3 模型的安全性。這些指標可幫助評估模型產生有害內容的潛力以及其對破解攻擊的脆弱性。安全性指標包括：

- <strong>與自我傷害相關的內容</strong>：評估模型是否傾向生成與自我傷害相關的內容。
- <strong>仇恨與不公平內容</strong>：評估模型是否傾向生成仇恨或不公平的內容。
- <strong>暴力內容</strong>：評估模型是否傾向生成暴力內容。
- <strong>性暗示內容</strong>：評估模型是否傾向生成不當的性暗示內容。

評估這些方面可確保 AI 模型不會產生有害或冒犯的內容，使其符合社會價值觀與監管標準。

![基於安全性的評估。](../../../../../../translated_images/zh-TW/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### 效能評估介紹

為確保你的 AI 模型達到預期效能，重要的是對其效能進行評估。在 Microsoft Foundry 中，效能評估讓你檢視模型在生成準確、相關且連貫的回應方面的有效性。

![效能評估。](../../../../../../translated_images/zh-TW/performance-evaluation.48b3e7e01a098740.webp)

*圖片來源：[生成式 AI 應用評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 效能指標

在此教學中，你將使用 Microsoft Foundry 的效能指標評估微調後的 Phi-3 / Phi-3.5 模型的效能。這些指標幫助你評估模型在生成準確、相關且連貫回應方面的有效性。效能指標包括：

- <strong>基於事實性</strong>：評估生成的答案與輸入資訊的一致性程度。
- <strong>相關性</strong>：評估生成回應與給定問題的相關程度。
- <strong>連貫性</strong>：評估生成文字的流暢度、自然性及類人語言的程度。
- <strong>流暢度</strong>：評估生成文字的語言熟練度。
- **GPT 相似度**：比較生成回應與真實答案的相似性。
- **F1 分數**：計算生成回應與來源資料間共享詞彙的比例。

這些指標幫助評估模型在產出準確、相關且連貫回應方面的效能。

![基於效能的評估。](../../../../../../translated_images/zh-TW/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **情境 2：在 Microsoft Foundry 評估 Phi-3 / Phi-3.5 模型**

### 開始之前

本教學接續之前的部落格文章「[微調並結合客製化 Phi-3 模型與 Prompt Flow：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」及「[在 Microsoft Foundry 中微調並結合客製化 Phi-3 模型與 Prompt Flow](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」。在這些文章中，我們說明如何在 Microsoft Foundry 中微調 Phi-3 / Phi-3.5 模型並與 Prompt flow 整合。

本教學將帶你部署 Azure OpenAI 模型作為評估者，並用其評估你微調後的 Phi-3 / Phi-3.5 模型。

開始本教學前，請確認你擁有先前教學中所述的以下前置條件：

1. 用於評估微調後 Phi-3 / Phi-3.5 模型的準備好資料集。
1. 已微調並部署到 Azure 機器學習的 Phi-3 / Phi-3.5 模型。
1. 在 Microsoft Foundry 中與微調後 Phi-3 / Phi-3.5 模型整合的 Prompt flow。

> [!NOTE]
> 你將使用先前部落格文章下載的 **ULTRACHAT_200k** 資料夾中名為 *test_data.jsonl* 的檔案，作為評估微調後 Phi-3 / Phi-3.5 模型的資料集。

#### 在 Microsoft Foundry 中將自訂 Phi-3 / Phi-3.5 模型整合到 Prompt flow（以程式碼優先的方法）

> [!NOTE]
> 如果你採用了「[在 Microsoft Foundry 中微調並結合客製化 Phi-3 模型與 Prompt Flow](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」中描述的低程式碼方式，可以跳過此練習，直接進入下一部分。
> 不過，若你依照「[微調並結合客製化 Phi-3 模型與 Prompt Flow：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」中程式碼優先的方法進行微調與部署，連接模型與 Prompt flow 的流程會略有不同。你將在本練習中學習此流程。

要繼續，需將微調後的 Phi-3 / Phi-3.5 模型整合進 Microsoft Foundry 中的 Prompt flow。

#### 建立 Microsoft Foundry Hub

你需要先建立 Hub 才能建立專案。Hub 類似於資源群組，讓你在 Microsoft Foundry 中組織與管理多個專案。

1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 從左側面板選擇 **所有 Hub**。

1. 從導覽選單選擇 **+ 新增 Hub**。

    ![建立 Hub。](../../../../../../translated_images/zh-TW/create-hub.5be78fb1e21ffbf1.webp)

1. 執行以下動作：

    - 輸入 **Hub 名稱**，此名稱必須唯一。
    - 選擇你的 Azure <strong>訂閱</strong>。

    - 選擇要使用的 <strong>資源群組</strong>（如有需要，請建立新的資源群組）。
    - 選擇您想使用的 <strong>區域</strong>。
    - 選擇要使用的 **連線 Azure AI 服務**（如有需要，請建立新的連線）。
    - 選擇 **連線 Azure AI 搜尋** 並選擇 <strong>跳過連線</strong>。

    ![填寫中心。](../../../../../../translated_images/zh-TW/fill-hub.baaa108495c71e34.webp)

1. 選擇 <strong>下一步</strong>。

#### 建立 Microsoft Foundry 專案

1. 在您建立的中心中，從左側選單選擇 <strong>所有專案</strong>。

1. 從導航選單中選擇 **+ 新增專案**。

    ![選擇新專案。](../../../../../../translated_images/zh-TW/select-new-project.cd31c0404088d7a3.webp)

1. 輸入 <strong>專案名稱</strong>。此名稱必須是唯一的。

    ![建立專案。](../../../../../../translated_images/zh-TW/create-project.ca3b71298b90e420.webp)

1. 選擇 <strong>建立專案</strong>。

#### 為微調的 Phi-3 / Phi-3.5 模型新增自訂連線

要將您的自訂 Phi-3 / Phi-3.5 模型整合到 Prompt flow 中，您需要將模型的端點和金鑰儲存在自訂連線中。此設定確保可以在 Prompt flow 中存取您的自訂 Phi-3 / Phi-3.5 模型。

#### 設定微調的 Phi-3 / Phi-3.5 模型的 API 金鑰與端點 URI

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Azure 機器學習工作區。

1. 從左側標籤中選擇 <strong>端點</strong>。

    ![選擇端點。](../../../../../../translated_images/zh-TW/select-endpoints.ee7387ecd68bd18d.webp)

1. 選擇您建立的端點。

    ![選擇已建立的端點。](../../../../../../translated_images/zh-TW/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. 從導航選單中選擇 <strong>使用</strong>。

1. 複製您的 **REST 端點** 及 <strong>主要金鑰</strong>。

    ![複製 API 金鑰與端點 URI。](../../../../../../translated_images/zh-TW/copy-endpoint-key.0650c3786bd646ab.webp)

#### 新增自訂連線

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽到您建立的 Microsoft Foundry 專案。

1. 在您建立的專案中，從左側標籤選擇 <strong>設定</strong>。

1. 選擇 **+ 新增連線**。

    ![選擇新連線。](../../../../../../translated_images/zh-TW/select-new-connection.fa0f35743758a74b.webp)

1. 從導航選單中選擇 <strong>自訂金鑰</strong>。

    ![選擇自訂金鑰。](../../../../../../translated_images/zh-TW/select-custom-keys.5a3c6b25580a9b67.webp)

1. 執行以下步驟：

    - 選擇 **+ 新增鍵值對**。
    - 鍵名輸入 **endpoint**，並在值欄位貼上您從 Azure ML Studio 複製的端點。
    - 再次選擇 **+ 新增鍵值對**。
    - 鍵名輸入 **key**，並在值欄位貼上您從 Azure ML Studio 複製的金鑰。
    - 新增完鍵值後，選擇 <strong>是機密</strong>，以防止金鑰被揭露。

    ![新增連線。](../../../../../../translated_images/zh-TW/add-connection.ac7f5faf8b10b0df.webp)

1. 選擇 <strong>新增連線</strong>。

#### 建立 Prompt flow

您已在 Microsoft Foundry 新增自訂連線。接下來，讓我們依照以下步驟建立 Prompt flow。然後您將會把此 Prompt flow 連接到自訂連線，以在 Prompt flow 中使用微調模型。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 從左側標籤選擇 **Prompt flow**。

1. 從導航選單中選擇 **+ 建立**。

    ![選擇 Promptflow。](../../../../../../translated_images/zh-TW/select-promptflow.18ff2e61ab9173eb.webp)

1. 從導航選單選擇 <strong>聊天流程</strong>。

    ![選擇聊天流程。](../../../../../../translated_images/zh-TW/select-flow-type.28375125ec9996d3.webp)

1. 輸入要使用的 <strong>資料夾名稱</strong>。

    ![輸入名稱。](../../../../../../translated_images/zh-TW/enter-name.02ddf8fb840ad430.webp)

1. 選擇 <strong>建立</strong>。

#### 設定 Prompt flow 與您的自訂 Phi-3 / Phi-3.5 模型聊天

您需要將微調的 Phi-3 / Phi-3.5 模型整合到 Prompt flow 中。但現有提供的 Prompt flow 並非為此目的設計，因此您必須重新設計 Prompt flow，使其能與自訂模型整合。

1. 在 Prompt flow 中，執行以下步驟重建現有流程：

    - 選擇 <strong>原始檔模式</strong>。
    - 刪除 *flow.dag.yml* 檔案中的所有現有程式碼。
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

    - 選擇 <strong>儲存</strong>。

    ![選擇原始檔模式。](../../../../../../translated_images/zh-TW/select-raw-file-mode.06c1eca581ce4f53.webp)

1. 將下列程式碼新增至 *integrate_with_promptflow.py*，以在 Prompt flow 使用自訂的 Phi-3 / Phi-3.5 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 日誌設置
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

        # "connection" 是自訂連線的名稱，"endpoint" 和 "key" 是自訂連線中的鍵
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

    ![貼上 Prompt flow 程式碼。](../../../../../../translated_images/zh-TW/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> 關於在 Microsoft Foundry 中使用 Prompt flow 的更詳細資訊，請參閱 [Microsoft Foundry 中的 Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 <strong>聊天輸入</strong>、<strong>聊天輸出</strong> 以啟用與您的模型聊天功能。

    ![選擇輸入輸出。](../../../../../../translated_images/zh-TW/select-input-output.c187fc58f25fbfc3.webp)

1. 現在您已準備與您的自訂 Phi-3 / Phi-3.5 模型聊天。在接下來的練習中，您將學習如何啟動 Prompt flow 並使用它與您的微調 Phi-3 / Phi-3.5 模型聊天。

> [!NOTE]
>
> 重建的流程應該如下圖所示：
>
> ![流程範例](../../../../../../translated_images/zh-TW/graph-example.82fd1bcdd3fc545b.webp)
>

#### 啟動 Prompt flow

1. 選擇 <strong>開始計算工作階段</strong> 以啟動 Prompt flow。

    ![開始計算工作階段。](../../../../../../translated_images/zh-TW/start-compute-session.9acd8cbbd2c43df1.webp)

1. 選擇 <strong>驗證並解析輸入</strong> 以更新參數。

    ![驗證輸入。](../../../../../../translated_images/zh-TW/validate-input.c1adb9543c6495be.webp)

1. 選擇 <strong>連線</strong> 的 <strong>值</strong>，即您建立的自訂連線。例如，*connection*。

    ![連線。](../../../../../../translated_images/zh-TW/select-connection.1f2b59222bcaafef.webp)

#### 與您的自訂 Phi-3 / Phi-3.5 模型聊天

1. 選擇 <strong>聊天</strong>。

    ![選擇聊天。](../../../../../../translated_images/zh-TW/select-chat.0406bd9687d0c49d.webp)

1. 以下是結果範例：現在您可以與您的自訂 Phi-3 / Phi-3.5 模型聊天。建議根據用於微調的資料提問。

    ![與 Prompt flow 聊天。](../../../../../../translated_images/zh-TW/chat-with-promptflow.1cf8cea112359ada.webp)

### 部署 Azure OpenAI 評估 Phi-3 / Phi-3.5 模型

若要在 Microsoft Foundry 中評估 Phi-3 / Phi-3.5 模型，您需要部署 Azure OpenAI 模型。此模型將用來評估 Phi-3 / Phi-3.5 模型的效能。

#### 部署 Azure OpenAI

1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

    ![選擇專案。](../../../../../../translated_images/zh-TW/select-project-created.5221e0e403e2c9d6.webp)

1. 在您建立的專案中，從左側標籤選擇 <strong>部署</strong>。

1. 從導航選單中選擇 **+ 部署模型**。

1. 選擇 <strong>部署基礎模型</strong>。

    ![選擇部署。](../../../../../../translated_images/zh-TW/deploy-openai-model.95d812346b25834b.webp)

1. 選擇您想使用的 Azure OpenAI 模型。例如，**gpt-4o**。

    ![選擇要使用的 Azure OpenAI 模型。](../../../../../../translated_images/zh-TW/select-openai-model.959496d7e311546d.webp)

1. 選擇 <strong>確認</strong>。

### 使用 Microsoft Foundry 的 Prompt flow 評估微調的 Phi-3 / Phi-3.5 模型

### 開始新評估

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

    ![選擇專案。](../../../../../../translated_images/zh-TW/select-project-created.5221e0e403e2c9d6.webp)

1. 在您建立的專案中，從左側標籤選擇 <strong>評估</strong>。

1. 從導航選單中選擇 **+ 新增評估**。

    ![選擇評估。](../../../../../../translated_images/zh-TW/select-evaluation.2846ad7aaaca7f4f.webp)

1. 選擇 **Prompt flow** 評估。

    ![選擇 Prompt flow 評估。](../../../../../../translated_images/zh-TW/promptflow-evaluation.cb9758cc19b4760f.webp)

1. 執行以下步驟：

    - 輸入評估名稱。此名稱必須是唯一的。
    - 選擇任務類型為 <strong>無上下文的問答</strong>。因為本教學使用的 **ULTRACHAT_200k** 資料集不包含上下文。
    - 選擇您想要評估的 Prompt flow。

    ![Prompt flow 評估。](../../../../../../translated_images/zh-TW/evaluation-setting1.4aa08259ff7a536e.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下步驟：

    - 選擇 <strong>新增您的資料集</strong> 以上傳資料集。例如，您可以上傳測試資料集檔案，如 *test_data.json1*，此檔案包含在您下載的 **ULTRACHAT_200k** 資料集中。
    - 選擇符合您資料集的適當 <strong>資料集欄位</strong>。例如，若您使用 **ULTRACHAT_200k** 資料集，請選擇 **${data.prompt}** 作為資料集欄位。

    ![Prompt flow 評估。](../../../../../../translated_images/zh-TW/evaluation-setting2.07036831ba58d64e.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下步驟設定效能與品質指標：

    - 選擇您想使用的效能與品質指標。
    - 選擇您建立用於評估的 Azure OpenAI 模型。例如，選擇 **gpt-4o**。

    ![Prompt flow 評估。](../../../../../../translated_images/zh-TW/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. 執行以下步驟設定風險與安全指標：

    - 選擇您想使用的風險與安全指標。
    - 選擇計算缺陷率所用的閾值。例如，選擇 <strong>中等</strong>。
    - 對於 <strong>問題</strong>，將 <strong>資料來源</strong> 設為 **{$data.prompt}**。
    - 對於 <strong>答案</strong>，將 <strong>資料來源</strong> 設為 **{$run.outputs.answer}**。
    - 對於 <strong>正確答案</strong>，將 <strong>資料來源</strong> 設為 **{$data.message}**。

    ![Prompt flow 評估。](../../../../../../translated_images/zh-TW/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. 選擇 <strong>下一步</strong>。

1. 選擇 <strong>提交</strong> 以啟動評估。

1. 評估將花費一些時間完成。您可以在 <strong>評估</strong> 標籤中監控進度。

### 檢視評估結果

> [!NOTE]
> 以下呈現的結果旨在說明評估流程。在本教學中，我們使用的模型是基於相對較小的資料集進行微調，可能導致次佳結果。實際結果將依據資料集的大小、品質、多樣性以及模型的具體設定而有大幅差異。

評估完成後，您可以檢視效能和安全指標的結果。

1. 效能與品質指標：

    - 評估模型產生連貫、流暢且相關回應的能力。

    ![評估結果。](../../../../../../translated_images/zh-TW/evaluation-result-gpu.85f48b42dfb74254.webp)

1. 風險與安全指標：

    - 確保模型輸出是安全的，並符合負責任 AI 原則，避免任何有害或冒犯性內容。

    ![評估結果。](../../../../../../translated_images/zh-TW/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. 您可以向下捲動查看 <strong>詳細指標結果</strong>。

    ![評估結果。](../../../../../../translated_images/zh-TW/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. 透過評估您的自訂 Phi-3 / Phi-3.5 模型在效能與安全指標上的表現，您可以確認該模型不僅有效，還符合負責任 AI 操作，準備好進行實際部署。

## 恭喜！

### 您已完成本教程


您已成功評估整合於 Microsoft Foundry 之 Prompt flow 的微調 Phi-3 模型。這是確保您的 AI 模型不僅表現優異，同時遵守微軟的負責任 AI 原則，幫助您構建值得信賴且可靠的 AI 應用程式的重要步驟。

![Architecture.](../../../../../../translated_images/zh-TW/architecture.10bec55250f5d6a4.webp)

## 清理 Azure 資源

請清理您的 Azure 資源以避免產生額外帳單。前往 Azure 入口網站並刪除以下資源：

- Azure 機器學習資源。
- Azure 機器學習模型端點。
- Microsoft Foundry 專案資源。
- Microsoft Foundry Prompt flow 資源。

### 後續步驟

#### 文件

- [使用負責任 AI 儀表板評估 AI 系統](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的評估與監控指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文件](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 訓練內容

- [微軟負責任 AI 方法簡介](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 簡介](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 參考資料

- [什麼是負責任的 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [宣佈 Azure AI 新工具，助您打造更安全且值得信賴的生成式 AI 應用](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->