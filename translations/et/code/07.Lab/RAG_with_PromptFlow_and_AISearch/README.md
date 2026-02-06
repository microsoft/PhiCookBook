## RAG PromptFlowi ja AISearchiga

Selles näites rakendame Retrieval Augmented Generation (RAG) rakendust, kasutades Phi3 SLM-ina, AI Searchi vektorandmebaasina ja Prompt Flow'd madala koodiga orkestreerijana.

## Omadused

- Lihtne juurutamine Dockeriga.
- Skaalautuv arhitektuur AI töövoogude haldamiseks.
- Madala koodiga lähenemine Prompt Flow abil.

## Eeltingimused

Enne alustamist veendu, et oled täitnud järgmised nõuded:

- Docker on sinu arvutisse installitud.
- Azure'i konto, millel on õigused konteinerressursside loomiseks ja haldamiseks.
- Azure AI Studio ja Azure AI Search instantsid.
- Embedding-mudel indeksi loomiseks (võib olla kas Azure OpenAI embedding või kataloogist pärit OS mudel).
- Python 3.8 või uuem versioon on sinu arvutisse installitud.
- Azure Container Registry (või mõni muu sinu valitud register).

## Paigaldamine

1. Loo uus voog oma Azure AI Studio projektis, kasutades flow.yaml faili.
2. Juuruta Phi3 mudel oma Azure AI mudelikataloogist ja loo ühendus oma projektiga. [Juuruta Phi-3 kui teenusmudel](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Loo vektorindeks Azure AI Searchis, kasutades mõnda enda valitud dokumenti. [Loo vektorindeks Azure AI Searchis](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Juuruta voog hallatavale lõpp-punktile ja kasuta seda failis prompt-flow-frontend.py. [Juuruta voog veebipõhisele lõpp-punktile](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klooni repositoorium:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Ehita Docker-pilt:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Lükka Docker-pilt Azure Container Registry'sse:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Kasutamine

1. Käivita Docker-konteiner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Ava rakendus oma brauseris aadressil `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Täisartikkel: [RAG Phi-3-Mediumiga kui teenusmudel Azure'i mudelikataloogist](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.