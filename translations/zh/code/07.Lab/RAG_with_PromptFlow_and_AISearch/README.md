<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-03T06:27:32+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "zh"
}
-->
## 使用 PromptFlow 和 AISearch 实现 RAG

在这个示例中，我们将实现一个基于检索增强生成（RAG）的应用程序，利用 Phi3 作为 SLM，AI Search 作为向量数据库，并使用 Prompt Flow 作为低代码编排工具。

## 功能

- 使用 Docker 轻松部署。
- 可扩展的架构，用于处理 AI 工作流。
- 通过 Prompt Flow 采用低代码方法。

## 前提条件

在开始之前，请确保满足以下要求：

- 在本地机器上安装了 Docker。
- 拥有一个 Azure 账户，并具有创建和管理容器资源的权限。
- 拥有 Azure AI Studio 和 Azure AI Search 实例。
- 一个用于创建索引的嵌入模型（可以是 Azure OpenAI 嵌入模型或目录中的开源模型）。
- 在本地机器上安装了 Python 3.8 或更高版本。
- 一个 Azure 容器注册表（或您选择的任何注册表）。

## 安装

1. 使用 flow.yaml 文件在 Azure AI Studio 项目中创建一个新的流。
2. 从 Azure AI 模型目录中部署一个 Phi3 模型，并将其连接到您的项目。[部署 Phi-3 作为模型服务](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用任意文档在 Azure AI Search 中创建向量索引。[在 Azure AI Search 中创建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 在托管端点上部署流，并在 prompt-flow-frontend.py 文件中使用它。[在在线端点上部署流](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆代码库：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 构建 Docker 镜像：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 将 Docker 镜像推送到 Azure 容器注册表：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. 运行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 在浏览器中访问应用程序：`http://localhost:8501`。

## 联系方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免责声明**：  
本文档通过AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文档为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而导致的任何误解或错误解释不承担责任。