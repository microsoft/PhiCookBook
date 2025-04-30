<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-04T11:36:05+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "ja"
}
-->
## RAG with PromptFlowとAISearch

この例では、Phi3をSLMとして活用し、AI SearchをvectorDBとして使用し、Prompt Flowをローコードオーケストレーターとして活用するRetrieval Augmented Generation (RAG)アプリケーションを実装します。

## 特徴

- Dockerを使用した簡単なデプロイ。
- AIワークフローを処理するためのスケーラブルなアーキテクチャ。
- Prompt Flowを使用したローコードアプローチ。

## 前提条件

始める前に、以下の要件を満たしていることを確認してください：

- ローカルマシンにDockerがインストールされていること。
- コンテナリソースを作成および管理する権限を持つAzureアカウント。
- Azure AI StudioとAzure AI Searchインスタンス。
- インデックスを作成するための埋め込みモデル（Azure OpenAI埋め込みまたはカタログのOSモデルのいずれか）。
- ローカルマシンにPython 3.8以降がインストールされていること。
- Azure Container Registry（または任意のレジストリ）。

## インストール

1. flow.yamlファイルを使用してAzure AI Studioプロジェクトに新しいフローを作成します。
2. Azure AIモデルカタログからPhi3モデルをデプロイし、プロジェクトへの接続を作成します。 [Phi-3をモデルとしてデプロイする](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 任意のドキュメントを使用してAzure AI Searchでベクターインデックスを作成します。 [Azure AI Searchでベクターインデックスを作成する](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. マネージドエンドポイントにフローをデプロイし、prompt-flow-frontend.pyファイルで使用します。 [オンラインエンドポイントにフローをデプロイする](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
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

## 使用方法

1. Dockerコンテナを実行します：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ブラウザで`http://localhost:8501`にアクセスしてアプリケーションを開きます。

## 問い合わせ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

全文記事: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で作成された文書が正式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用により生じる誤解や誤認について、当社は一切の責任を負いません。