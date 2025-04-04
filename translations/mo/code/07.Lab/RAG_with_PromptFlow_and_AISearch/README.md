<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-04T11:35:38+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "mo"
}
-->
## RAG miaraka amin'ny PromptFlow sy AISearch

Amin'ity ohatra ity, hampihatra fampiharana Retrieval Augmented Generation (RAG) isika, mampiasa Phi3 ho SLM, AI Search ho vectorDB ary Prompt Flow ho mpandrindra low-code.

## Endri-javatra

- Fomba fametrahana mora amin'ny alàlan'ny Docker.
- Rafitra azo zatra mivelatra mba hitantanana ny fizotry ny asa AI.
- Fomba low-code mampiasa Prompt Flow.

## Fepetra takiana

Alohan'ny hanombohana dia ataovy azo antoka fa efa mahafeno ireto fepetra manaraka ireto ianao:

- Docker efa napetraka ao amin'ny solosainao.
- Kaonty Azure miaraka amin'ny fahazoan-dàlana hamorona sy hitantana loharano container.
- Azure AI Studio sy Azure AI Search efa misy.
- Modely embedding mba hamoronana index (afaka mampiasa Azure OpenAI embedding na modely OS avy amin'ny catalog).
- Python 3.8 na taty aoriana efa napetraka ao amin'ny solosainao.
- Azure Container Registry (na registry hafa tianao ampiasaina).

## Fametrahana

1. Mamorona flow vaovao ao amin'ny tetikasa Azure AI Studio mampiasa ny rakitra flow.yaml.
2. Alefaso ny Modely Phi3 avy amin'ny catalog modely Azure AI ary ampifandraiso amin'ny tetikasanao. [Deploy Phi-3 ho Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Mamorona vector index ao amin'ny Azure AI Search mampiasa antontan-taratasy izay tianao. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Alefaso ny flow amin'ny managed endpoint ary ampiasao ao amin'ny rakitra prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone ny repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Mamorona ny Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Atosika ny Docker image ao amin'ny Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Fampiasana

1. Alefaso ny Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Tsidiho ny fampiharana ao amin'ny navigateur amin'ny `http://localhost:8501`.

## Fifandraisana

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Lahatsoratra feno: [RAG miaraka amin'ny Phi-3-Medium ho Model as a Service avy amin'ny Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

It seems like you want the text translated into "mo." Could you clarify what "mo" refers to? Are you asking for a translation into a specific language or code? Let me know so I can assist you effectively!