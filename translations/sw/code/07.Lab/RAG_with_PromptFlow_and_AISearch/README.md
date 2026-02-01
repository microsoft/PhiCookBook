## RAG na PromptFlow na AISearch

Katika mfano huu, tutaweka matumizi ya Retrieval Augmented Generation (RAG) tukitumia Phi3 kama SLM, AI Search kama vectorDB na Prompt Flow kama mratibu wa low-code.

## Sifa

- Utekelezaji rahisi kwa kutumia Docker.
- Muundo unaoweza kupanuka kwa kushughulikia michakato ya AI.
- Njia ya low code kwa kutumia Prompt Flow

## Mahitaji

Kabla ya kuanza, hakikisha umezingatia mahitaji yafuatayo:

- Docker imewekwa kwenye kompyuta yako ya karibu.
- Akaunti ya Azure yenye ruhusa za kuunda na kusimamia rasilimali za kontena.
- Azure AI Studio na Azure AI Search
- Mfano wa embedding wa kuunda index yako (inaweza kuwa Azure OpenAI embedding au mfano wa OS kutoka kwenye katalogi)
- Python 3.8 au toleo jipya zaidi limewekwa kwenye kompyuta yako ya karibu.
- Azure Container Registry (au rejista yoyote unayochagua)

## Ufungaji

1. Unda flow mpya kwenye Mradi wako wa Azure AI Studio ukitumia faili la flow.yaml.
2. Weka Mfano wa Phi3 kutoka kwenye katalogi ya modeli za Azure AI na unda muunganisho kwa mradi wako. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Unda index ya vector kwenye Azure AI Search ukitumia hati yoyote unayopendelea [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Weka flow kwenye endpoint inayosimamiwa na uitumie kwenye faili la prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Nakili (clone) repository:

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

1. Endesha kontena la Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Fungua programu kwenye kivinjari chako kwa anwani `http://localhost:8501`.

## Mawasiliano

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Makala Kamili: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.