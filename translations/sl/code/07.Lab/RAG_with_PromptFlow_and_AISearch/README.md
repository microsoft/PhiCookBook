<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:11:13+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "sl"
}
-->
## RAG z PromptFlow in AISearch

V tem primeru bomo implementirali aplikacijo Retrieval Augmented Generation (RAG), ki uporablja Phi3 kot SLM, AI Search kot vectorDB in Prompt Flow kot orodje za nizko-kodno orkestracijo.

## Značilnosti

- Enostavna namestitev z uporabo Dockerja.
- Razširljiva arhitektura za upravljanje AI delovnih tokov.
- Pristop z nizko kodo z uporabo Prompt Flow.

## Zahteve

Preden začnete, se prepričajte, da izpolnjujete naslednje pogoje:

- Docker nameščen na vašem lokalnem računalniku.
- Azure račun z dovoljenji za ustvarjanje in upravljanje kontejnerskih virov.
- Primerki Azure AI Studio in Azure AI Search.
- Model za vdelavo (embedding), s katerim boste ustvarili indeks (lahko je Azure OpenAI embedding ali odprtokodni model iz kataloga).
- Python 3.8 ali novejši nameščen na vašem lokalnem računalniku.
- Azure Container Registry (ali katerikoli register po vaši izbiri).

## Namestitev

1. Ustvarite nov flow v vašem Azure AI Studio projektu z uporabo datoteke flow.yaml.
2. Namestite Phi3 model iz vašega Azure AI model kataloga in vzpostavite povezavo s projektom. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Ustvarite vektorski indeks na Azure AI Search z uporabo poljubnega dokumenta. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Namestite flow na upravljani endpoint in ga uporabite v datoteki prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonirajte repozitorij:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Zgradite Docker sliko:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Potisnite Docker sliko v Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Uporaba

1. Zaženite Docker kontejner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Dostopajte do aplikacije v brskalniku na `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Celoten članek: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.