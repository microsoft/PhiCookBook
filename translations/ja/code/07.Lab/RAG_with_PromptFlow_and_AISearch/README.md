<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-08T06:42:07+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "ja"
}
-->
## RAG with PromptFlow and AISearch

この例では、Phi3をSLMとして、AI SearchをベクトルDBとして、Prompt Flowをローコードオーケストレーターとして活用したRetrieval Augmented Generation（RAG）アプリケーションを実装します。

## Features

- Dockerを使った簡単なデプロイ。
- AIワークフローを処理するためのスケーラブルなアーキテクチャ。
- Prompt Flowを使ったローコードアプローチ。

## Prerequisites

始める前に、以下の要件を満たしていることを確認してください：

- ローカルマシンにDockerがインストールされていること。
- コンテナリソースの作成と管理権限を持つAzureアカウント。
- Azure AI StudioとAzure AI Searchのインスタンス。
- インデックス作成用の埋め込みモデル（Azure OpenAIの埋め込みモデルまたはカタログのOSモデルのいずれか）。
- ローカルマシンにPython 3.8以降がインストールされていること。
- Azure Container Registry（または任意のレジストリ）。

## Installation

1. flow.yamlファイルを使って、Azure AI Studioプロジェクトに新しいフローを作成します。
2. Azure AIモデルカタログからPhi3モデルをデプロイし、プロジェクトとの接続を作成します。[Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 任意のドキュメントを使ってAzure AI Search上にベクトルインデックスを作成します。[Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. マネージドエンドポイントにフローをデプロイし、prompt-flow-frontend.pyファイルで使用します。[Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. リポジトリをクローンします：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Dockerイメージをビルドします：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. DockerイメージをAzure Container Registryにプッシュします：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. Dockerコンテナを起動します：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ブラウザで`http://localhost:8501`にアクセスしてアプリケーションを利用します。

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

全文記事: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語でのオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。