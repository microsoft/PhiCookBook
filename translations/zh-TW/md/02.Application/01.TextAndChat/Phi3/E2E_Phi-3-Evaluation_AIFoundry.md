# 在 Microsoft Foundry 中評估微調後的 Phi-3 / Phi-3.5 模型，聚焦於微軟的負責任 AI 原則

此端對端（E2E）範例基於 Microsoft 技術社群的指南「[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)」。

## 概述

### 如何在 Microsoft Foundry 中評估微調後的 Phi-3 / Phi-3.5 模型的安全性與效能？

微調模型有時可能導致意外或不期望的回應。為確保模型保持安全且有效，重要的是評估模型產生有害內容的潛力及產生準確、相關且連貫回應的能力。在本教學中，您將學習如何評估整合於 Microsoft Foundry 中 Prompt flow 的微調 Phi-3 / Phi-3.5 模型的安全性與效能。

以下為 Microsoft Foundry 的評估流程。

![Architecture of tutorial.](../../../../../../translated_images/zh-TW/architecture.10bec55250f5d6a4.webp)

*圖片來源：[Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 欲了解關於 Phi-3 / Phi-3.5 更深入的資訊並探索更多資源，請造訪 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 前置條件

- [Python](https://www.python.org/downloads)
- [Azure 訂閱](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微調後的 Phi-3 / Phi-3.5 模型

### 目錄

1. [**情境 1：Microsoft Foundry 的 Prompt flow 評估介紹**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [安全性評估介紹](#安全性評估介紹)
    - [效能評估介紹](#為微調過的-phi-3-phi-35-模型新增自訂連線)

1. [**情境 2：在 Microsoft Foundry 評估 Phi-3 / Phi-3.5 模型**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [開始之前](#建立-prompt-flow)
    - [部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [使用 Microsoft Foundry 的 Prompt flow 評估微調後的 Phi-3 / Phi-3.5 模型](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [恭喜！](#congratulations)

## **情境 1：Microsoft Foundry 的 Prompt flow 評估介紹**

### 安全性評估介紹

為確保您的 AI 模型合乎道德且安全，評估模型是否符合微軟負責任 AI 原則至關重要。在 Microsoft Foundry 中，安全性評估允許您評估模型面臨越獄攻擊的脆弱性及產生有害內容的潛力，這與原則直接契合。

![Safaty evaluation.](../../../../../../translated_images/zh-TW/safety-evaluation.083586ec88dfa950.webp)

*圖片來源：[Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 微軟負責任 AI 原則

在開始技術步驟之前，理解微軟的負責任 AI 原則非常重要。該倫理框架旨在指導 AI 系統的負責任開發、部署與運作。這些原則為 AI 系統的設計、開發和部署提供指引，確保 AI 技術的建構公正、透明且具包容性。這些原則為評估 AI 模型安全性的基礎。

微軟負責任 AI 原則包括：

- <strong>公平性與包容性</strong>：AI 系統應公平對待每個人，避免對相似處境群體產生不同影響。例如，當 AI 系統提供醫療治療建議、貸款申請或就業指導時，對具有相似症狀、經濟狀況或專業資格的人應提供相同建議。

- <strong>可靠性與安全性</strong>：為建立信任，AI 系統必須可靠、安全且一致地運作。此類系統應能依照設計運作，安全回應不可預期狀況，且抵抗有害操作。其行為及可處理的條件反映開發者在設計與測試時所預見的情境範圍。

- <strong>透明性</strong>：當 AI 系統協助做出對人生命產生巨大影響的決策時，理解決策過程至關重要。例如，銀行可能使用 AI 系統判斷個人是否具信用資格，公司可能使用 AI 系統篩選最合格候選人。

- <strong>隱私與安全</strong>：隨著 AI 越來越普及，保護隱私及個人與企業資訊安全變得更重要且複雜。因為 AI 系統必須存取資料來提供準確且有依據的預測與決策，隱私與資料安全需嚴密關注。

1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 從左側索引標籤選擇 <strong>所有中樞</strong>。

1. 從導覽選單選擇 **+ 新增中樞**。

    ![建立中樞。](../../../../../../translated_images/zh-TW/create-hub.5be78fb1e21ffbf1.webp)

1. 執行下列工作：

    - 輸入 <strong>中樞名稱</strong>。此名稱必須唯一。
    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如果需要，請新增一個）。
    - 選擇您想使用的 <strong>位置</strong>。
    - 選擇要使用的 **連接 Azure AI 服務**（如果需要，請新增一個）。
    - 選擇 **連接 Azure AI 搜尋** 並選擇 <strong>略過連接</strong>。

    ![填寫中樞。](../../../../../../translated_images/zh-TW/fill-hub.baaa108495c71e34.webp)

1. 選擇 <strong>下一步</strong>。

#### 建立 Microsoft Foundry 專案

1. 在您建立的中樞中，從左側索引標籤選擇 <strong>所有專案</strong>。

1. 從導覽選單選擇 **+ 新增專案**。

    ![選擇新專案。](../../../../../../translated_images/zh-TW/select-new-project.cd31c0404088d7a3.webp)

1. 輸入 <strong>專案名稱</strong>。此名稱必須唯一。

    ![建立專案。](../../../../../../translated_images/zh-TW/create-project.ca3b71298b90e420.webp)

1. 選擇 <strong>建立專案</strong>。

#### 為微調過的 Phi-3 / Phi-3.5 模型新增自訂連線

要將您的自訂 Phi-3 / Phi-3.5 模型整合到 Prompt flow，您需要將模型的端點與金鑰儲存在自訂連線中。此設定將確保在 Prompt flow 中可以存取您的自訂 Phi-3 / Phi-3.5 模型。

#### 設定微調過的 Phi-3 / Phi-3.5 模型的 API 金鑰與端點 URI

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Azure 機器學習工作區。

1. 從左側索引標籤選擇 <strong>端點</strong>。

    ![選擇端點。](../../../../../../translated_images/zh-TW/select-endpoints.ee7387ecd68bd18d.webp)

1. 選擇您建立的端點。

    ![選擇已建立的端點。](../../../../../../translated_images/zh-TW/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. 從導覽選單選擇 <strong>使用</strong>。

1. 複製您的 **REST 端點** 和 <strong>主要金鑰</strong>。

    ![複製 API 金鑰與端點 URI。](../../../../../../translated_images/zh-TW/copy-endpoint-key.0650c3786bd646ab.webp)

#### 新增自訂連線

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 在您建立的專案中，從左側索引標籤選擇 <strong>設定</strong>。

1. 選擇 **+ 新增連線**。

    ![選擇新增連線。](../../../../../../translated_images/zh-TW/select-new-connection.fa0f35743758a74b.webp)

1. 從導覽選單選擇 <strong>自訂金鑰</strong>。

    ![選擇自訂金鑰。](../../../../../../translated_images/zh-TW/select-custom-keys.5a3c6b25580a9b67.webp)

1. 執行下列工作：

    - 選擇 **+ 新增金鑰數值對**。
    - 於金鑰名稱輸入 **endpoint**，並將您從 Azure ML Studio 複製的端點貼上至數值欄位。
    - 再次選擇 **+ 新增金鑰數值對**。
    - 於金鑰名稱輸入 **key**，並將您從 Azure ML Studio 複製的金鑰貼上至數值欄位。
    - 新增金鑰後，勾選 <strong>為密碼</strong>，以防止金鑰被揭露。

    ![新增連線。](../../../../../../translated_images/zh-TW/add-connection.ac7f5faf8b10b0df.webp)

1. 選擇 <strong>新增連線</strong>。

#### 建立 Prompt flow

您已在 Microsoft Foundry 新增了自訂連線。接著，使用以下步驟建立一個 Prompt flow。然後，您將把此 Prompt flow 連結到自訂連線，以便在 Prompt flow 中使用微調模型。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 從左側索引標籤選擇 **Prompt flow**。

1. 從導覽選單選擇 **+ 建立**。

    ![選擇 Promptflow。](../../../../../../translated_images/zh-TW/select-promptflow.18ff2e61ab9173eb.webp)

1. 從導覽選單選擇 <strong>聊天流程</strong>。

    ![選擇聊天流程。](../../../../../../translated_images/zh-TW/select-flow-type.28375125ec9996d3.webp)

1. 輸入要使用的 <strong>資料夾名稱</strong>。

    ![輸入名稱。](../../../../../../translated_images/zh-TW/enter-name.02ddf8fb840ad430.webp)

1. 選擇 <strong>建立</strong>。

#### 設定 Prompt flow 與您的自訂 Phi-3 / Phi-3.5 模型聊天

您需要將微調過的 Phi-3 / Phi-3.5 模型整合到 Prompt flow 中。然而，目前提供的 Prompt flow 並非為此目的設計，因此您必須重新設計 Prompt flow，使其能夠整合自訂模型。

1. 在 Prompt flow 中，執行下列工作來重建現有流程：

    - 選擇 <strong>原始檔案模式</strong>。
    - 刪除 *flow.dag.yml* 檔案中所有現有程式碼。
    - 將以下程式碼加入 *flow.dag.yml*。

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

    ![選擇原始檔案模式。](../../../../../../translated_images/zh-TW/select-raw-file-mode.06c1eca581ce4f53.webp)

1. 將以下程式碼加入 *integrate_with_promptflow.py* 中，以便在 Prompt flow 使用自訂的 Phi-3 / Phi-3.5 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 日誌設定
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

    ![貼上 prompt flow 程式碼。](../../../../../../translated_images/zh-TW/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> 有關在 Microsoft Foundry 中使用 Prompt flow 的更多詳細資訊，您可以參考 [Microsoft Foundry 中的 Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 <strong>聊天輸入</strong>、<strong>聊天輸出</strong> 以啟用與模型的聊天。

    ![選擇輸入輸出。](../../../../../../translated_images/zh-TW/select-input-output.c187fc58f25fbfc3.webp)

1. 現在，您已準備好與您的自訂 Phi-3 / Phi-3.5 模型聊天。下一個練習中，您將學習如何啟動 Prompt flow 並使用它與您的微調 Phi-3 / Phi-3.5 模型聊天。

> [!NOTE]
>
> 重新建構的流程應該看起來如以下圖片所示：
>
> ![流程範例](../../../../../../translated_images/zh-TW/graph-example.82fd1bcdd3fc545b.webp)
>

#### 啟動 Prompt flow

1. 選擇 <strong>啟動計算階段</strong> 以啟動 Prompt flow。

    ![啟動計算階段。](../../../../../../translated_images/zh-TW/start-compute-session.9acd8cbbd2c43df1.webp)

1. 選擇 <strong>驗證並解析輸入</strong> 以更新參數。

    ![驗證輸入。](../../../../../../translated_images/zh-TW/validate-input.c1adb9543c6495be.webp)

1. 選擇 <strong>連線</strong> 的 <strong>值</strong>，連到您建立的自訂連線。範例：*connection*。

    ![連線。](../../../../../../translated_images/zh-TW/select-connection.1f2b59222bcaafef.webp)

#### 與您的自訂 Phi-3 / Phi-3.5 模型聊天

1. 選擇 <strong>聊天</strong>。

    ![選擇聊天。](../../../../../../translated_images/zh-TW/select-chat.0406bd9687d0c49d.webp)

1. 以下是結果範例：現在您可以與您的自訂 Phi-3 / Phi-3.5 模型聊天。建議您根據用於微調的資料提出問題。

    ![與 prompt flow 聊天。](../../../../../../translated_images/zh-TW/chat-with-promptflow.1cf8cea112359ada.webp)

### 部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型

要在 Microsoft Foundry 中評估 Phi-3 / Phi-3.5 模型，您需要部署一個 Azure OpenAI 模型。此模型將用於評估 Phi-3 / Phi-3.5 模型的表現。

#### 部署 Azure OpenAI

1. 登入 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

    ![選擇專案。](../../../../../../translated_images/zh-TW/select-project-created.5221e0e403e2c9d6.webp)

1. 在您建立的專案中，從左側索引標籤選擇 <strong>部署</strong>。

1. 從導覽選單選擇 **+ 部署模型**。

1. 選擇 <strong>部署基礎模型</strong>。

    ![選擇部署。](../../../../../../translated_images/zh-TW/deploy-openai-model.95d812346b25834b.webp)

1. 選擇您想使用的 Azure OpenAI 模型。例如，**gpt-4o**。

    ![選擇您想使用的 Azure OpenAI 模型。](../../../../../../translated_images/zh-TW/select-openai-model.959496d7e311546d.webp)

1. 選擇 <strong>確認</strong>。

### 使用 Microsoft Foundry 的 Prompt flow 評估微調過的 Phi-3 / Phi-3.5 模型

### 啟動新評估

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導覽至您建立的 Microsoft Foundry 專案。

    ![選擇專案。](../../../../../../translated_images/zh-TW/select-project-created.5221e0e403e2c9d6.webp)

1. 在您建立的專案中，從左側索引標籤選擇 <strong>評估</strong>。

1. 從導覽選單選擇 **+ 新增評估**。

    ![選擇評估。](../../../../../../translated_images/zh-TW/select-evaluation.2846ad7aaaca7f4f.webp)

1. 選擇 **Prompt flow** 評估。

    ![選擇 Prompt flow 評估。](../../../../../../translated_images/zh-TW/promptflow-evaluation.cb9758cc19b4760f.webp)

1. 執行下列工作：

    - 輸入評估名稱。必須是唯一值。
    - 選擇任務類型為 <strong>無上下文問答</strong>，因為本教學中使用的 **ULTRACHAT_200k** 資料集不包含上下文。
    - 選擇您想要評估的 Prompt flow。

    ![Prompt flow 評估設定。](../../../../../../translated_images/zh-TW/evaluation-setting1.4aa08259ff7a536e.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行下列工作：

    - 選擇 <strong>新增您的資料集</strong> 上傳資料集。例如，您可以上傳 **ULTRACHAT_200k** 資料集下載包內的測試資料集檔案，如 *test_data.json1*。
    - 選擇符合您資料集的 <strong>資料集欄位</strong>。例如，若您使用的是 **ULTRACHAT_200k** 資料集，則選擇 **${data.prompt}** 作為資料集欄位。

    ![Prompt flow 評估設定。](../../../../../../translated_images/zh-TW/evaluation-setting2.07036831ba58d64e.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行下列工作來配置績效與品質指標：

    - 選擇您想使用的績效與品質指標。
    - 選擇您建立用於評估的 Azure OpenAI 模型。例如，選擇 **gpt-4o**。

    ![Prompt flow 評估設定。](../../../../../../translated_images/zh-TW/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. 執行下列工作來配置風險與安全指標：

    - 選擇您要使用的風險與安全指標。
    - 選擇計算缺陷率所使用的閾值，例如選擇 <strong>中等</strong>。
    - 對於 **question**，將 <strong>資料來源</strong> 設為 **{$data.prompt}**。
    - 對於 **answer**，將 <strong>資料來源</strong> 設為 **{$run.outputs.answer}**。
    - 對於 **ground_truth**，將 <strong>資料來源</strong> 設為 **{$data.message}**。

    ![Prompt flow 評估設定。](../../../../../../translated_images/zh-TW/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. 選擇 <strong>下一步</strong>。

1. 選擇 <strong>送出</strong> 以開始評估。

1. 評估將花一些時間完成。您可以在 <strong>評估</strong> 索引標籤監控進度。

### 檢視評估結果

> [!NOTE]
> 以下呈現的結果是為了示範評估過程。在本教學中，我們使用相對較小資料集微調的模型，這可能導致結果不理想。實際結果將根據資料集的大小、品質、多樣性以及模型的具體配置有顯著差異。

完成評估後，您可以檢視績效與安全指標的評估結果。
1. 效能與品質指標：

    - 評估模型生成連貫、流暢且相關回應的效果。

    ![Evaluation result.](../../../../../../translated_images/zh-TW/evaluation-result-gpu.85f48b42dfb74254.webp)

1. 風險與安全指標：

    - 確保模型輸出安全且符合負責任 AI 原則，避免任何有害或冒犯性內容。

    ![Evaluation result.](../../../../../../translated_images/zh-TW/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. 你可以向下捲動查看<strong>詳細指標結果</strong>。

    ![Evaluation result.](../../../../../../translated_images/zh-TW/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. 透過對自訂 Phi-3 / Phi-3.5 模型評估效能與安全指標，你可以確認模型不僅有效，且遵循負責任 AI 實踐，準備好進行實際部署。

## 恭喜！

### 你已完成本教學

你已成功評估在 Microsoft Foundry 中整合 Prompt flow 的微調 Phi-3 模型。這是確保你的 AI 模型不僅具有良好表現，且遵守 Microsoft 的負責任 AI 原則，協助你打造值得信賴且可靠的 AI 應用程式的重要步驟。

![Architecture.](../../../../../../translated_images/zh-TW/architecture.10bec55250f5d6a4.webp)

## 清理 Azure 資源

請清理你的 Azure 資源以避免產生額外費用。前往 Azure 入口網站刪除以下資源：

- Azure 機器學習資源。
- Azure 機器學習模型端點。
- Microsoft Foundry 專案資源。
- Microsoft Foundry Prompt flow 資源。

### 下一步

#### 文件

- [使用負責任 AI 儀表板評估 AI 系統](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的評估與監控指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文件](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 訓練內容

- [Microsoft 負責任 AI 方法介紹](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 入門](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 參考資料

- [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [宣布 Azure AI 新工具，助你打造更安全且值得信賴的生成式 AI 應用程式](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 應用程式的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威資料。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->