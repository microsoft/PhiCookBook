<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-08T06:42:15+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "tw"
}
-->
## RAG with PromptFlow and AISearch

在這個範例中，我們將實作一個結合 Phi3 作為 SLM、AI Search 作為向量資料庫，以及 Prompt Flow 作為低程式碼協調器的 Retrieval Augmented Generation (RAG) 應用。

## Features

- 使用 Docker 輕鬆部署。
- 可擴充的架構以處理 AI 工作流程。
- 使用 Prompt Flow 的低程式碼方式。

## Prerequisites

開始之前，請確認您已符合以下需求：

- 本機已安裝 Docker。
- 擁有可建立及管理容器資源的 Azure 帳號權限。
- 已建立 Azure AI Studio 及 Azure AI Search 實例。
- 用於建立索引的嵌入模型（可以是 Azure OpenAI 嵌入模型或目錄中的開源模型）。
- 本機已安裝 Python 3.8 或以上版本。
- 一個 Azure Container Registry（或您選擇的任何註冊表）。

## Installation

1. 使用 flow.yaml 檔案在您的 Azure AI Studio 專案中建立新的流程。
2. 從您的 Azure AI 模型目錄部署 Phi3 模型，並建立與專案的連線。[Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用您選擇的文件，在 Azure AI Search 上建立向量索引。[Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 將流程部署到管理端點，並在 prompt-flow-frontend.py 檔案中使用。[Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 複製此程式碼庫：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 建置 Docker 映像檔：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 將 Docker 映像檔推送到 Azure Container Registry：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. 執行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 在瀏覽器中透過 `http://localhost:8501` 訪問應用程式。

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。