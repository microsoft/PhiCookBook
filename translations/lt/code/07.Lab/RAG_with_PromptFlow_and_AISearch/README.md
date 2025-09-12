<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-09-12T15:01:57+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "lt"
}
-->
## RAG su PromptFlow ir AISearch

Šiame pavyzdyje įgyvendinsime Retrieval Augmented Generation (RAG) programą, naudodami Phi3 kaip SLM, AI Search kaip vectorDB ir Prompt Flow kaip mažo kodo orkestratorių.

## Funkcijos

- Paprastas diegimas naudojant Docker.
- Skalaujama architektūra AI darbo eigoms valdyti.
- Mažo kodo metodas naudojant Prompt Flow.

## Reikalavimai

Prieš pradėdami, įsitikinkite, kad atitinkate šiuos reikalavimus:

- Jūsų kompiuteryje įdiegtas Docker.
- Azure paskyra su teisėmis kurti ir valdyti konteinerių išteklius.
- Azure AI Studio ir Azure AI Search instancijos.
- Įterpimo modelis jūsų indeksui sukurti (gali būti Azure OpenAI įterpimo modelis arba OS modelis iš katalogo).
- Jūsų kompiuteryje įdiegtas Python 3.8 ar naujesnė versija.
- Azure Container Registry (ar bet kuris jūsų pasirinktas registras).

## Diegimas

1. Sukurkite naują srautą savo Azure AI Studio projekte, naudodami flow.yaml failą.
2. Diegkite Phi3 modelį iš Azure AI modelių katalogo ir sukurkite ryšį su savo projektu. [Diegti Phi-3 kaip Modelį kaip Paslaugą](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Sukurkite vektorinį indeksą Azure AI Search naudodami bet kurį jūsų pasirinktą dokumentą. [Sukurti vektorinį indeksą Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Diegkite srautą valdomame galutiniame taške ir naudokite jį prompt-flow-frontend.py faile. [Diegti srautą internetiniame galutiniame taške](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Nukopijuokite saugyklą:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Sukurkite Docker atvaizdą:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Įkelkite Docker atvaizdą į Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Naudojimas

1. Paleiskite Docker konteinerį:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pasiekite programą savo naršyklėje adresu `http://localhost:8501`.

## Kontaktai

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Pilnas straipsnis: [RAG su Phi-3-Medium kaip Modeliu kaip Paslauga iš Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.