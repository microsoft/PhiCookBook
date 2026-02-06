## RAG wit PromptFlow an AISearch

For dis example, we go implement Retrieval Augmented Generation (RAG) application wey dey use Phi3 as SLM, AI Search as vectorDB an Prompt Flow as low-code orchestrator.

## Features

- Easy to deploy wit Docker.
- Architecture wey fit scale to handle AI workflows.
- Low-code way to use Prompt Flow

## Prerequisites

Before you start, make sure say you get these requirements:

- Docker don install for your local machine.
- One Azure account wey get permissions to create an manage container resources.
- Instances of Azure AI Studio an Azure AI Search.
- Embedding model to build your index (fit be either an Azure OpenAI embedding or an OS model from the catalog)
- Python 3.8 or later don install for your local machine.
- An Azure Container Registry (or any registry wey you prefer)

## Installation

1. Create a new flow on your Azure AI Studio Project using the flow.yaml file.
2. Deploy a Phi3 Model from your Azure AI model catalog an create di connection to your project. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Create the vector index on Azure AI Search using any document of your choice [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Deploy the flow on a managed enpoint and use it in the prompt-flow-frontend.py file. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone di repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Build di Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push di Docker image to Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. Run di Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Access di application in your browser at `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Full Article: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate by AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistake or wrong meaning. Di original dokument for im own language na di correct source. If na important matter, make you use professional human translator. We no go responsible for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->