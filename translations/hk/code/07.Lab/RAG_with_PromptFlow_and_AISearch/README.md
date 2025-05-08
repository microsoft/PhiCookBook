<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-08T06:41:59+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "hk"
}
-->
## RAG 同 PromptFlow 同 AISearch

呢個例子會示範點樣用 Phi3 做 SLM，用 AI Search 做 vectorDB，同用 Prompt Flow 做低碼編排，去實現 Retrieval Augmented Generation (RAG) 應用。

## 功能

- 用 Docker 輕鬆部署。
- 可擴展嘅架構，適合處理 AI 工作流程。
- 用 Prompt Flow 嘅低碼方法。

## 先決條件

開始之前，請確保你符合以下要求：

- 本地機有安裝 Docker。
- 有 Azure 帳戶，並有權限去建立同管理容器資源。
- 有 Azure AI Studio 同 Azure AI Search 實例。
- 有一個用嚟建立索引嘅 embedding 模型（可以係 Azure OpenAI embedding，或者目錄入面嘅開源模型）。
- 本地機安裝咗 Python 3.8 或以上版本。
- 有 Azure Container Registry（或者你自己選擇嘅 registry）。

## 安裝

1. 用 flow.yaml 檔喺你嘅 Azure AI Studio Project 裡面建立一個新嘅 flow。
2. 從你嘅 Azure AI 模型目錄部署一個 Phi3 Model，並同你嘅 project 建立連接。[Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 喺 Azure AI Search 用你揀嘅任何文件建立 vector 索引。[Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 喺管理嘅 endpoint 上部署 flow，然後喺 prompt-flow-frontend.py 檔使用佢。[Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone 呢個 repository：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 建立 Docker 映像檔：

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

2. 喺瀏覽器打開 `http://localhost:8501` 使用應用程式。

## 聯絡

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。