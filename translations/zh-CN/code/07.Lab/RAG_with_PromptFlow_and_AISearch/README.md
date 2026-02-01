## 使用 PromptFlow 和 AISearch 的 RAG

在本示例中，我们将实现一个检索增强生成（RAG）应用，利用 Phi3 作为 SLM，AI Search 作为向量数据库，Prompt Flow 作为低代码编排工具。

## 功能

- 使用 Docker 轻松部署。
- 可扩展架构，支持 AI 工作流处理。
- 使用 Prompt Flow 实现低代码开发。

## 前提条件

开始之前，请确保满足以下要求：

- 本地机器已安装 Docker。
- 拥有可创建和管理容器资源权限的 Azure 账户。
- Azure AI Studio 和 Azure AI Search 实例。
- 用于创建索引的嵌入模型（可以是 Azure OpenAI 嵌入模型或目录中的开源模型）。
- 本地机器已安装 Python 3.8 或更高版本。
- Azure 容器注册表（或您选择的任何注册表）。

## 安装

1. 使用 flow.yaml 文件在 Azure AI Studio 项目中创建一个新流程。
2. 从 Azure AI 模型目录部署 Phi3 模型，并将其连接到您的项目。[将 Phi-3 部署为模型即服务](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用任意文档在 Azure AI Search 上创建向量索引。[在 Azure AI Search 上创建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 在托管端点上部署流程，并在 prompt-flow-frontend.py 文件中使用它。[在在线端点上部署流程](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
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

2. 在浏览器中访问 `http://localhost:8501` 使用该应用。

## 联系方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[使用 Azure 模型目录中的 Phi-3-Medium 作为模型即服务的 RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。