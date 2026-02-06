## RAG s PromptFlow a AISearch

V tomto příkladu implementujeme aplikaci Retrieval Augmented Generation (RAG) využívající Phi3 jako SLM, AI Search jako vectorDB a Prompt Flow jako low-code orchestrátor.

## Funkce

- Snadné nasazení pomocí Dockeru.
- Škálovatelná architektura pro zpracování AI workflow.
- Přístup s nízkým kódem pomocí Prompt Flow.

## Požadavky

Než začnete, ujistěte se, že splňujete následující požadavky:

- Docker nainstalovaný na vašem lokálním počítači.
- Azure účet s oprávněními pro vytváření a správu kontejnerových zdrojů.
- Instance Azure AI Studio a Azure AI Search.
- Embedding model pro vytvoření indexu (může to být Azure OpenAI embedding nebo OS model z katalogu).
- Python 3.8 nebo novější nainstalovaný na vašem lokálním počítači.
- Azure Container Registry (nebo jakýkoli registr podle vašeho výběru).

## Instalace

1. Vytvořte nový flow ve vašem Azure AI Studio projektu pomocí souboru flow.yaml.
2. Nasadťe Phi3 model z vašeho Azure AI model katalogu a vytvořte připojení k vašemu projektu. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Vytvořte vektorový index na Azure AI Search pomocí libovolného dokumentu dle vašeho výběru [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Nasadťe flow na spravovaný endpoint a použijte ho v souboru prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Naklonujte repozitář:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Vytvořte Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Nahrajte Docker image do Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Použití

1. Spusťte Docker kontejner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Přistupte k aplikaci ve vašem prohlížeči na adrese `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Celý článek: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.