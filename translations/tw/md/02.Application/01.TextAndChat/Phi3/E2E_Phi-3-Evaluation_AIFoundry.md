<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7799f9e2960966adc296d24cdf0d6486",
  "translation_date": "2025-04-04T06:15:23+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "tw"
}
-->
# 評估在 Azure AI Foundry 中微調的 Phi-3 / Phi-3.5 模型，聚焦於 Microsoft 的負責任 AI 原則

這個端到端（E2E）範例基於 Microsoft Tech Community 的指南 "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)"。

## 概述

### 如何在 Azure AI Foundry 中評估微調的 Phi-3 / Phi-3.5 模型的安全性和性能？

微調模型有時可能會導致意外或不希望的回應。為了確保模型的安全性和有效性，評估模型生成有害內容的可能性以及生成準確、相關和一致回應的能力是至關重要的。在本教程中，您將學習如何評估與 Azure AI Foundry 中的 Prompt flow 集成的微調 Phi-3 / Phi-3.5 模型的安全性和性能。

以下是 Azure AI Foundry 的評估流程。

![教程架構。](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tw.png)

*圖片來源: [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 欲了解更多詳細信息以及探索有關 Phi-3 / Phi-3.5 的額外資源，請訪問 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 先決條件

- [Python](https://www.python.org/downloads)
- [Azure 訂閱](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微調的 Phi-3 / Phi-3.5 模型

### 目錄

1. [**場景 1: Azure AI Foundry 的 Prompt flow 評估介紹**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [安全性評估介紹](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [性能評估介紹](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**場景 2: 在 Azure AI Foundry 中評估 Phi-3 / Phi-3.5 模型**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [開始之前](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [使用 Azure AI Foundry 的 Prompt flow 評估微調的 Phi-3 / Phi-3.5 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [恭喜！](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **場景 1: Azure AI Foundry 的 Prompt flow 評估介紹**

### 安全性評估介紹

為了確保您的 AI 模型是倫理且安全的，必須根據 Microsoft 的負責任 AI 原則對其進行評估。在 Azure AI Foundry 中，安全性評估允許您評估模型對破解攻擊的脆弱性以及生成有害內容的可能性，這與這些原則直接相關。

![安全性評估。](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.tw.png)

*圖片來源: [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft 的負責任 AI 原則

在開始技術步驟之前，了解 Microsoft 的負責任 AI 原則至關重要。這是一個倫理框架，用於指導 AI 系統的負責任開發、部署和運營。這些原則指導 AI 系統的負責任設計、開發和部署，確保 AI 技術以公平、透明和包容的方式構建。這些原則是評估 AI 模型安全性的基礎。

Microsoft 的負責任 AI 原則包括：

- **公平性和包容性**：AI 系統應公平對待每個人，避免對類似情況的人群造成不同影響。例如，當 AI 系統提供有關醫療建議、貸款申請或就業的指導時，它應對具有相似症狀、財務狀況或專業資格的所有人做出相同的建議。

- **可靠性和安全性**：為了建立信任，AI 系統需要可靠、安全且一致地運行。這些系統應能夠按照原始設計運行，安全應對意外情況，並抵禦有害操縱。其行為以及能處理的各種情況反映了開發人員在設計和測試過程中預期的情景和條件。

- **透明性**：當 AI 系統幫助做出對人們生活有重大影響的決定時，人們需要了解這些決定是如何產生的。例如，銀行可能使用 AI 系統來決定某人是否有信用資格。一家公司可能使用 AI 系統來確定最合格的招聘候選人。

- **隱私和安全性**：隨著 AI 的普及，保護隱私和安全個人及商業信息變得越來越重要和複雜。AI 需要密切關注隱私和數據安全，因為數據訪問對 AI 系統做出準確且有信息的預測和決定至關重要。

- **問責性**：設計和部署 AI 系統的人必須對其系統的運行方式負責。組織應參考行業標準制定問責規範。這些規範可以確保 AI 系統不成為影響人們生活的任何決定的最終權威，也可以確保人類保持對高度自主的 AI 系統的有意義控制。

![填充中心。](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.tw.png)

*圖片來源: [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> 欲了解更多有關 Microsoft 的負責任 AI 原則的信息，請訪問 [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)。

#### 安全性指標

在本教程中，您將使用 Azure AI Foundry 的安全性指標評估微調的 Phi-3 模型的安全性。這些指標幫助您評估模型生成有害內容的可能性及其對破解攻擊的脆弱性。安全性指標包括：

- **與自我傷害相關的內容**：評估模型是否有生成與自我傷害相關內容的傾向。
- **仇恨和不公平內容**：評估模型是否有生成仇恨或不公平內容的傾向。
- **暴力內容**：評估模型是否有生成暴力內容的傾向。
- **性相關內容**：評估模型是否有生成不適當性相關內容的傾向。

評估這些方面可確保 AI 模型不會生成有害或冒犯性內容，並與社會價值觀和監管標準保持一致。

![基於安全性評估。](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.tw.png)

### 性能評估介紹

為了確保您的 AI 模型表現如預期，評估其性能是至關重要的。在 Azure AI Foundry 中，性能評估允許您評估模型在生成準確、相關和一致回應方面的有效性。

![性能評估。](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.tw.png)

*圖片來源: [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 性能指標

在本教程中，您將使用 Azure AI Foundry 的性能指標評估微調的 Phi-3 / Phi-3.5 模型的性能。這些指標幫助您評估模型在生成準確、相關和一致回應方面的有效性。性能指標包括：

- **基礎性**：評估生成的答案與輸入源信息的對齊程度。
- **相關性**：評估生成回應與給定問題的相關程度。
- **一致性**：評估生成文本的流暢度、自然性及是否類似人類語言。
- **流利度**：評估生成文本的語言能力。
- **GPT 相似性**：將生成的回應與真實答案進行相似性比較。
- **F1 分數**：計算生成回應與源數據之間共享詞的比例。

這些指標幫助您評估模型在生成準確、相關和一致回應方面的有效性。

![基於性能評估。](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.tw.png)

## **場景 2: 在 Azure AI Foundry 中評估 Phi-3 / Phi-3.5 模型**

### 開始之前

本教程是之前博客文章的延續，"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" 和 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"。在這些文章中，我們詳細講解了如何在 Azure AI Foundry 中微調 Phi-3 / Phi-3.5 模型並與 Prompt flow 集成。

在本教程中，您將部署 Azure OpenAI 模型作為 Azure AI Foundry 中的評估器，並使用它來評估您的微調 Phi-3 / Phi-3.5 模型。

在開始本教程之前，請確保您已具備以下先決條件，這些條件在之前的教程中已描述：

1. 一個準備好的數據集，用於評估微調的 Phi-3 / Phi-3.5 模型。
1. 已微調並部署到 Azure 機器學習的 Phi-3 / Phi-3.5 模型。
1. 與 Azure AI Foundry 中的 Prompt flow 集成的微調 Phi-3 / Phi-3.5 模型。

> [!NOTE]
> 您將使用 *test_data.jsonl* 文件，該文件位於之前博客文章中下載的 **ULTRACHAT_200k** 數據集的數據文件夾中，作為評估微調 Phi-3 / Phi-3.5 模型的數據集。

#### 在 Azure AI Foundry 中集成自定義 Phi-3 / Phi-3.5 模型與 Prompt flow（以代碼為主的方法）

> [!NOTE]
> 如果您遵循 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" 中描述的低代碼方法，可以跳過此部分，直接進行下一步。
> 然而，如果您遵循 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" 中描述的以代碼為主的方法微調並部署您的 Phi-3 / Phi-3.5 模型，將模型與 Prompt flow 連接的過程會略有不同。您將在此部分學習這個過程。

要繼續，您需要將您的微調 Phi-3 / Phi-3.5 模型集成到 Azure AI Foundry 的 Prompt flow 中。

#### 創建 Azure AI Foundry Hub

在創建項目之前，您需要先創建 Hub。Hub 類似於資源組，允許您在 Azure AI Foundry 中組織和管理多個項目。

1. 登錄 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 從左側選擇 **所有 Hub**。

1. 從導航菜單中選擇 **+ 新 Hub**。

    ![創建 Hub。](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.tw.png)

1. 完成以下操作：

    - 輸入 **Hub 名稱**，必須是唯一值。
    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源組**（如果需要，創建一個新的）。
    - 選擇您想使用的 **位置**。
    - 選擇 **連接 Azure AI 服務**（如果需要，創建一個新的）。
    - 選擇 **連接 Azure AI 搜索** 並選擇 **跳過連接**。
![填寫 Hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.tw.png)

1. 選擇 **Next**。

#### 建立 Azure AI Foundry 專案

1. 在你建立的 Hub 中，從左側選項卡選擇 **All projects**。

1. 從導航選單中選擇 **+ New project**。

    ![選擇新專案.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.tw.png)

1. 輸入 **Project name**，必須是唯一的值。

    ![建立專案.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.tw.png)

1. 選擇 **Create a project**。

#### 為微調的 Phi-3 / Phi-3.5 模型新增自訂連線

若要將你的自訂 Phi-3 / Phi-3.5 模型整合至 Prompt flow，你需要在自訂連線中保存模型的端點和密鑰。此設置確保能在 Prompt flow 中存取你的自訂 Phi-3 / Phi-3.5 模型。

#### 設定微調 Phi-3 / Phi-3.5 模型的 API 密鑰和端點 URI

1. 造訪 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 前往你建立的 Azure Machine Learning 工作區。

1. 從左側選項卡選擇 **Endpoints**。

    ![選擇端點.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.tw.png)

1. 選擇你建立的端點。

    ![選擇已建立的端點.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.tw.png)

1. 從導航選單中選擇 **Consume**。

1. 複製你的 **REST endpoint** 和 **Primary key**。

    ![複製 API 密鑰和端點 URI.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.tw.png)

#### 新增自訂連線

1. 造訪 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 前往你建立的 Azure AI Foundry 專案。

1. 在你建立的專案中，從左側選項卡選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![選擇新連線.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.tw.png)

1. 從導航選單中選擇 **Custom keys**。

    ![選擇自訂密鑰.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.tw.png)

1. 執行以下操作：

    - 選擇 **+ Add key value pairs**。
    - 對於密鑰名稱，輸入 **endpoint**，並將你從 Azure ML Studio 複製的端點貼到值欄位。
    - 再次選擇 **+ Add key value pairs**。
    - 對於密鑰名稱，輸入 **key**，並將你從 Azure ML Studio 複製的密鑰貼到值欄位。
    - 新增密鑰後，選擇 **is secret** 以防止密鑰暴露。

    ![新增連線.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.tw.png)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

你已在 Azure AI Foundry 中新增了一個自訂連線。現在，讓我們使用以下步驟建立一個 Prompt flow，然後將此 Prompt flow 連接到自訂連線，以便在 Prompt flow 中使用微調的模型。

1. 前往你建立的 Azure AI Foundry 專案。

1. 從左側選項卡選擇 **Prompt flow**。

1. 從導航選單中選擇 **+ Create**。

    ![選擇 Prompt flow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.tw.png)

1. 從導航選單中選擇 **Chat flow**。

    ![選擇聊天流程.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.tw.png)

1. 輸入要使用的 **Folder name**。

    ![輸入名稱.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.tw.png)

1. 選擇 **Create**。

#### 設置 Prompt flow 與你的自訂 Phi-3 / Phi-3.5 模型聊天

你需要將微調的 Phi-3 / Phi-3.5 模型整合到 Prompt flow。然而，現有的 Prompt flow 無法支援此目的。因此，你必須重新設計 Prompt flow 以啟用自訂模型的整合。

1. 在 Prompt flow 中，執行以下操作以重建現有流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 文件中的所有現有程式碼。
    - 在 *flow.dag.yml* 文件中新增以下程式碼：

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

    ![選擇原始檔案模式.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.tw.png)

1. 在 *integrate_with_promptflow.py* 中新增以下程式碼，以在 Prompt flow 中使用自訂 Phi-3 / Phi-3.5 模型。

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

    ![貼上 Prompt flow 程式碼.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.tw.png)

> [!NOTE]
> 若要獲得有關在 Azure AI Foundry 中使用 Prompt flow 的更多詳細資訊，可參考 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input** 和 **Chat output** 以啟用與模型的聊天功能。

    ![選擇輸入輸出.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.tw.png)

1. 現在你已準備好與自訂 Phi-3 / Phi-3.5 模型聊天。在下一個練習中，你將學習如何啟動 Prompt flow 並使用它與微調的 Phi-3 / Phi-3.5 模型聊天。

> [!NOTE]
>
> 重建的流程應如下圖所示：
>
> ![流程範例](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.tw.png)
>

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![啟動計算會話.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.tw.png)

1. 選擇 **Validate and parse input** 以更新參數。

    ![驗證輸入.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.tw.png)

1. 選擇 **connection** 的 **Value**，連接到你建立的自訂連線。例如，*connection*。

    ![連線.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.tw.png)

#### 與你的自訂 Phi-3 / Phi-3.5 模型聊天

1. 選擇 **Chat**。

    ![選擇聊天.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.tw.png)

1. 以下是結果範例：現在你可以與你的自訂 Phi-3 / Phi-3.5 模型聊天。建議根據微調時使用的資料提出問題。

    ![使用 Prompt flow 聊天.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.tw.png)

### 部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型

若要在 Azure AI Foundry 中評估 Phi-3 / Phi-3.5 模型，你需要部署一個 Azure OpenAI 模型。此模型將用於評估 Phi-3 / Phi-3.5 模型的效能。

#### 部署 Azure OpenAI

1. 登錄 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 前往你建立的 Azure AI Foundry 專案。

    ![選擇專案.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tw.png)

1. 在你建立的專案中，從左側選項卡選擇 **Deployments**。

1. 從導航選單中選擇 **+ Deploy model**。

1. 選擇 **Deploy base model**。

    ![選擇部署.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.tw.png)

1. 選擇你希望使用的 Azure OpenAI 模型。例如，**gpt-4o**。

    ![選擇你希望使用的 Azure OpenAI 模型.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.tw.png)

1. 選擇 **Confirm**。

### 使用 Azure AI Foundry 的 Prompt flow 評估微調的 Phi-3 / Phi-3.5 模型

### 開始新的評估

1. 造訪 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 前往你建立的 Azure AI Foundry 專案。

    ![選擇專案.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tw.png)

1. 在你建立的專案中，從左側選項卡選擇 **Evaluation**。

1. 從導航選單中選擇 **+ New evaluation**。
![選擇評估。](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.tw.png)

1. 選擇 **Prompt flow** 評估。

    ![選擇 Prompt flow 評估。](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.tw.png)

1. 執行以下任務：

    - 輸入評估名稱，需為唯一值。
    - 選擇 **Question and answer without context** 作為任務類型。因為本教學使用的 **ULTRACHAT_200k** 資料集不包含上下文。
    - 選擇要評估的 Prompt flow。

    ![Prompt flow 評估。](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.tw.png)

1. 選擇 **Next**。

1. 執行以下任務：

    - 選擇 **Add your dataset** 上傳資料集。例如，可以上傳測試資料集檔案，例如 *test_data.json1*，該檔案包含於下載 **ULTRACHAT_200k** 資料集時。
    - 選擇與資料集匹配的 **Dataset column**。例如，使用 **ULTRACHAT_200k** 資料集時，選擇 **${data.prompt}** 作為資料集欄位。

    ![Prompt flow 評估。](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.tw.png)

1. 選擇 **Next**。

1. 執行以下任務以設定性能和質量指標：

    - 選擇要使用的性能和質量指標。
    - 選擇您建立用於評估的 Azure OpenAI 模型。例如，選擇 **gpt-4o**。

    ![Prompt flow 評估。](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.tw.png)

1. 執行以下任務以設定風險和安全指標：

    - 選擇要使用的風險和安全指標。
    - 選擇計算缺陷率的門檻值，例如 **Medium**。
    - 對於 **question**，選擇 **Data source** 為 **{$data.prompt}**。
    - 對於 **answer**，選擇 **Data source** 為 **{$run.outputs.answer}**。
    - 對於 **ground_truth**，選擇 **Data source** 為 **{$data.message}**。

    ![Prompt flow 評估。](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.tw.png)

1. 選擇 **Next**。

1. 選擇 **Submit** 開始評估。

1. 評估需要一些時間完成。您可以在 **Evaluation** 標籤中監控進度。

### 查看評估結果

> [!NOTE]
> 下列結果旨在展示評估過程。本教學使用的是基於相對較小資料集微調的模型，可能導致結果不理想。實際結果可能因資料集的大小、質量和多樣性，以及模型的具體配置而有顯著差異。

評估完成後，您可以查看性能和安全指標的結果。

1. 性能和質量指標：

    - 評估模型生成連貫、流暢且相關回應的效果。

    ![評估結果。](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.tw.png)

1. 風險和安全指標：

    - 確保模型的輸出安全，符合負責任 AI 原則，避免任何有害或冒犯性內容。

    ![評估結果。](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.tw.png)

1. 您可以向下滾動查看 **詳細指標結果**。

    ![評估結果。](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.tw.png)

1. 通過對自訂 Phi-3 / Phi-3.5 模型進行性能和安全指標的評估，您可以確認模型不僅具有效果，還遵循負責任 AI 實踐，為實際部署做好準備。

## 恭喜！

### 您已完成此教學

您已成功評估與 Azure AI Foundry 中 Prompt flow 整合的微調 Phi-3 模型。這是確保 AI 模型不僅性能良好，還符合 Microsoft 負責任 AI 原則的重要一步，幫助您建立值得信賴且可靠的 AI 應用。

![架構。](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tw.png)

## 清理 Azure 資源

清理您的 Azure 資源以避免額外費用。前往 Azure 入口網站並刪除以下資源：

- Azure 機器學習資源。
- Azure 機器學習模型端點。
- Azure AI Foundry 專案資源。
- Azure AI Foundry Prompt flow 資源。

### 下一步

#### 文件

- [使用負責任 AI 儀表板評估 AI 系統](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的評估和監控指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文件](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 訓練內容

- [Microsoft 負責任 AI 方法介紹](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry 介紹](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 參考

- [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Azure AI 宣佈新工具，幫助您建立更安全且值得信賴的生成式 AI 應用](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**免責聲明**：  
本文檔是使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。應以原文檔的原始語言版本作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。