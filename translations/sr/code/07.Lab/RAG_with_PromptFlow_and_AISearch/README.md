<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:15:08+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "sr"
}
-->
## RAG sa PromptFlow i AISearch

U ovom primeru implementiraćemo aplikaciju za Retrieval Augmented Generation (RAG) koristeći Phi3 kao SLM, AI Search kao vectorDB i Prompt Flow kao low-code orkestrator.

## Karakteristike

- Jednostavna implementacija pomoću Dockera.
- Skalabilna arhitektura za rukovanje AI tokovima rada.
- Low-code pristup koristeći Prompt Flow

## Preduslovi

Pre nego što počnete, proverite da li ispunjavate sledeće zahteve:

- Docker instaliran na vašem lokalnom računaru.
- Azure nalog sa dozvolama za kreiranje i upravljanje kontejnerskim resursima.
- Azure AI Studio i Azure AI Search instance
- Model za ugradnju (embedding) za kreiranje indeksa (može biti Azure OpenAI embedding ili OS model iz kataloga)
- Python 3.8 ili noviji instaliran na vašem lokalnom računaru.
- Azure Container Registry (ili bilo koji registar po vašem izboru)

## Instalacija

1. Kreirajte novi flow na vašem Azure AI Studio projektu koristeći flow.yaml fajl.
2. Deploy-ujte Phi3 model iz vašeg Azure AI model kataloga i uspostavite konekciju sa projektom. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Kreirajte vektorski indeks na Azure AI Search koristeći bilo koji dokument po vašem izboru [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Deploy-ujte flow na managed endpoint i koristite ga u prompt-flow-frontend.py fajlu. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonirajte repozitorijum:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Kreirajte Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Pošaljite Docker image na Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Korišćenje

1. Pokrenite Docker kontejner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pristupite aplikaciji u vašem pregledaču na adresi `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Kompletan članak: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења која произлазе из коришћења овог превода.