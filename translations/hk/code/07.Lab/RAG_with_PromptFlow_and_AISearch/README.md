<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-04T17:22:31+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "hk"
}
-->
## 用 PromptFlow 同 AISearch 做 RAG

呢個例子會示範點樣用 Phi3 做 SLM，AI Search 做 vectorDB，同埋 Prompt Flow 作低代碼編排，去實現一個 Retrieval Augmented Generation (RAG) 應用。

## 功能特點

- 用 Docker 輕鬆部署。
- 可擴展架構，方便處理 AI 工作流。
- 用 Prompt Flow 做低代碼開發。

## 先決條件

開始之前，請確保你已滿足以下要求：

- 已經喺本地機安裝 Docker。
- 有一個 Azure 帳戶，並擁有建立及管理容器資源嘅權限。
- Azure AI Studio 同 Azure AI Search 嘅實例。
- 用嚟建立索引嘅嵌入模型（可以係 Azure OpenAI embedding 或者目錄入面嘅 OS 模型）。
- 喺本地機安裝 Python 3.8 或以上版本。
- Azure Container Registry（或者任何你選擇嘅容器註冊表）。

## 安裝步驟

1. 用 flow.yaml 文件喺你嘅 Azure AI Studio Project 裏面創建一個新嘅 flow。
2. 喺 Azure AI 模型目錄部署一個 Phi3 模型，並且建立同你嘅項目嘅連接。[部署 Phi-3 作為 Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 喺 Azure AI Search 裏面用任何你選擇嘅文件建立向量索引。[喺 Azure AI Search 建立向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 喺管理端點部署 flow，並喺 prompt-flow-frontend.py 文件裏面使用。[喺線上端點部署 flow](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆倉庫：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 建立 Docker 映像：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 將 Docker 映像推送到 Azure Container Registry：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. 運行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 喺瀏覽器打開 `http://localhost:8501` 訪問應用。

## 聯絡方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**:  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於關鍵信息，建議使用專業的人力翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。