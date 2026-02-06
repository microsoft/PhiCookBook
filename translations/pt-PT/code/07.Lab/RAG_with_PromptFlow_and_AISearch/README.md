## RAG com PromptFlow e AISearch

Neste exemplo, vamos implementar uma aplicação de Retrieval Augmented Generation (RAG) utilizando o Phi3 como SLM, AI Search como vectorDB e Prompt Flow como orquestrador low-code.

## Funcionalidades

- Implementação fácil usando Docker.
- Arquitetura escalável para gerir fluxos de trabalho de IA.
- Abordagem low-code com Prompt Flow.

## Pré-requisitos

Antes de começar, certifique-se de que cumpre os seguintes requisitos:

- Docker instalado na sua máquina local.
- Uma conta Azure com permissões para criar e gerir recursos de containers.
- Instâncias de Azure AI Studio e Azure AI Search.
- Um modelo de embedding para criar o seu índice (pode ser um embedding Azure OpenAI ou um modelo OS do catálogo).
- Python 3.8 ou superior instalado na sua máquina local.
- Um Azure Container Registry (ou qualquer outro registo da sua preferência).

## Instalação

1. Crie um novo flow no seu projeto Azure AI Studio usando o ficheiro flow.yaml.
2. Faça o deploy de um Modelo Phi3 a partir do seu catálogo de modelos Azure AI e crie a ligação ao seu projeto. [Deploy Phi-3 como Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Crie o índice vetorial no Azure AI Search usando qualquer documento à sua escolha [Criar um índice vetorial no Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Faça o deploy do flow num endpoint gerido e utilize-o no ficheiro prompt-flow-frontend.py. [Deploy de um flow num endpoint online](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone o repositório:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Construa a imagem Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Envie a imagem Docker para o Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Utilização

1. Execute o container Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Aceda à aplicação no seu navegador em `http://localhost:8501`.

## Contacto

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Artigo completo: [RAG com Phi-3-Medium como Model as a Service do Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.