<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:10:34+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "sk"
}
-->
## RAG s PromptFlow a AISearch

V tomto príklade implementujeme aplikáciu Retrieval Augmented Generation (RAG) využívajúcu Phi3 ako SLM, AI Search ako vectorDB a Prompt Flow ako low-code orchestrátor.

## Funkcie

- Jednoduché nasadenie pomocou Dockeru.
- Škálovateľná architektúra pre spracovanie AI workflowov.
- Prístup s nízkym kódom pomocou Prompt Flow.

## Požiadavky

Pred začatím sa uistite, že spĺňate nasledujúce požiadavky:

- Docker nainštalovaný na vašom lokálnom počítači.
- Azure účet s oprávneniami na vytváranie a správu kontajnerových zdrojov.
- Inštancie Azure AI Studio a Azure AI Search.
- Embedding model na vytvorenie indexu (môže to byť Azure OpenAI embedding alebo OS model z katalógu).
- Python 3.8 alebo novší nainštalovaný na vašom lokálnom počítači.
- Azure Container Registry (alebo akýkoľvek iný registry podľa vášho výberu).

## Inštalácia

1. Vytvorte nový flow vo vašom Azure AI Studio projekte pomocou súboru flow.yaml.
2. Nasadte Phi3 model z vášho Azure AI model katalógu a vytvorte pripojenie k projektu. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Vytvorte vektorový index na Azure AI Search pomocou ľubovoľného dokumentu podľa vášho výberu [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Nasadte flow na spravovaný endpoint a použite ho v súbore prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Naklonujte repozitár:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Vytvorte Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Nahrajte Docker image do Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Použitie

1. Spustite Docker kontajner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pristúpte k aplikácii vo vašom prehliadači na adrese `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Celý článok: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.