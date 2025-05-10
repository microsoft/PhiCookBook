<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:14:22+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "hu"
}
-->
## RAG a PromptFlow és az AISearch segítségével

Ebben a példában egy Retrieval Augmented Generation (RAG) alkalmazást valósítunk meg, amely a Phi3-at használja SLM-ként, az AI Search-t vektor adatbázisként, és a Prompt Flow-t alacsony kódú vezérlőként.

## Jellemzők

- Egyszerű telepítés Docker használatával.
- Skálázható architektúra az AI munkafolyamatok kezelésére.
- Alacsony kódú megközelítés a Prompt Flow segítségével.

## Előfeltételek

Mielőtt elkezdenéd, győződj meg róla, hogy a következő feltételek teljesülnek:

- Docker telepítve van a helyi gépeden.
- Azure fiók, amely jogosultsággal rendelkezik konténer erőforrások létrehozására és kezelésére.
- Azure AI Studio és Azure AI Search példányok.
- Egy beágyazó modell az index létrehozásához (lehet Azure OpenAI beágyazás vagy egy OS modell a katalógusból).
- Python 3.8 vagy újabb telepítve a helyi gépen.
- Egy Azure Container Registry (vagy bármilyen választott registry).

## Telepítés

1. Hozz létre egy új folyamatot az Azure AI Studio projektedben a flow.yaml fájl segítségével.
2. Telepíts egy Phi3 modellt az Azure AI modell katalógusodból, és hozd létre a kapcsolatot a projekteddel. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Hozd létre a vektor indexet az Azure AI Search-ben bármely általad választott dokumentum alapján. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Telepítsd a folyamatot egy kezelt végpontra, és használd a prompt-flow-frontend.py fájlban. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klónozd a repozitóriumot:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Építsd meg a Docker képet:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Töltsd fel a Docker képet az Azure Container Registry-be:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Használat

1. Indítsd el a Docker konténert:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Érd el az alkalmazást a böngésződben a `http://localhost:8501` címen.

## Kapcsolat

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Teljes cikk: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt szakmai, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.