<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:14:14+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "sw"
}
-->
## RAG na PromptFlow na AISearch

Katika mfano huu, tutatekeleza programu ya Retrieval Augmented Generation (RAG) tukitumia Phi3 kama SLM, AI Search kama vectorDB na Prompt Flow kama mratibu wa low-code.

## Sifa

- Uwekaji rahisi kwa kutumia Docker.
- Msingi unaoweza kupanuka kwa ajili ya kushughulikia michakato ya AI.
- Njia ya low code kwa kutumia Prompt Flow.

## Mahitaji

Kabla ya kuanza, hakikisha umezingatia mahitaji yafuatayo:

- Docker imewekwa kwenye kompyuta yako ya nyumbani.
- Akaunti ya Azure yenye ruhusa za kuunda na kusimamia rasilimali za container.
- Azure AI Studio na Azure AI Search.
- Mfano wa embedding wa kuunda index yako (inaweza kuwa Azure OpenAI embedding au mfano wa OS kutoka kwenye katalogi).
- Python 3.8 au zaidi imewekwa kwenye kompyuta yako.
- Azure Container Registry (au rejista yoyote unayotaka).

## Ufungaji

1. Unda flow mpya kwenye Azure AI Studio Project yako ukitumia faili la flow.yaml.
2. Weka Phi3 Model kutoka kwenye katalogi ya AI modeli ya Azure na unda muunganisho kwa project yako. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Unda vector index kwenye Azure AI Search ukitumia hati yoyote unayotaka [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Weka flow kwenye managed endpoint na uitumie kwenye faili ya prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Nakili repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Tengeneza picha ya Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Sogeza picha ya Docker kwenye Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Matumizi

1. Endesha container ya Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Fungua programu kwenye kivinjari chako kwa kwenda `http://localhost:8501`.

## Mawasiliano

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Makala Kamili: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Kasi ya kuwajibika**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.