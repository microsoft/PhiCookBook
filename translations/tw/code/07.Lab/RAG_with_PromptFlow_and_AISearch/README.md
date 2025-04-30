<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-04T05:32:42+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "tw"
}
-->
## 使用 PromptFlow 和 AISearch 的 RAG

在這個範例中，我們將實作一個檢索增強生成（RAG）應用，結合 Phi3 作為 SLM，AI Search 作為向量資料庫，以及 Prompt Flow 作為低代碼編排工具。

## 功能特色

- 使用 Docker 進行簡易部署。
- 可擴展的架構以處理 AI 工作流。
- 使用 Prompt Flow 的低代碼方法。

## 先決條件

在開始之前，請確保您已滿足以下需求：

- 本地機器已安裝 Docker。
- 擁有 Azure 帳戶並具備建立及管理容器資源的權限。
- Azure AI Studio 和 Azure AI Search 實例。
- 用於建立索引的嵌入模型（可以是 Azure OpenAI 的嵌入模型或目錄中的開源模型）。
- 本地機器已安裝 Python 3.8 或更新版本。
- Azure Container Registry（或任何您選擇的容器註冊表）。

## 安裝步驟

1. 使用 flow.yaml 文件在 Azure AI Studio 專案中建立新的流程。
2. 從 Azure AI 模型目錄部署 Phi3 模型並與您的專案建立連結。[部署 Phi-3 作為模型即服務](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用任意文件在 Azure AI Search 上建立向量索引。[在 Azure AI Search 上建立向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 在受管理的端點上部署流程並在 prompt-flow-frontend.py 文件中使用它。[在線端點上部署流程](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆儲存庫：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 建立 Docker 映像檔：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 將 Docker 映像檔推送至 Azure Container Registry：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. 執行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 在瀏覽器中訪問應用程式：`http://localhost:8501`。

## 聯絡方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[使用 Azure 模型目錄中的 Phi-3-Medium 作為模型即服務的 RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**:  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力追求翻譯的準確性，但請注意，機器翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或錯誤解釋承擔責任。