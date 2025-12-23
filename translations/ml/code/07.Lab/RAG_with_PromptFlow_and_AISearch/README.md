<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-12-21T15:46:17+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "ml"
}
-->
## PromptFlowനും AISearchനും ഉപയോഗിച്ച് RAG

ഈ ഉദാഹരണത്തിൽ, Phi3 നെ SLM ആയി, AI Search നെ vectorDB ആയി, Prompt Flow നെ low-code orchestrator ആയി ഉപയോഗിച്ച് Retrieval Augmented Generation (RAG) അപ്ലിക്കേഷൻ നടപ്പിലാക്കുന്നതാണ് ഇവിടെ കാണിക്കുന്നത്.

## സവിശേഷതകൾ

- Docker ഉപയോഗിച്ച് എളുപ്പമുള്ള വിന്യസിക്കൽ.
- AI വർക്‌ഫ്ലോകൾ കൈകാര്യം ചെയ്യാൻ സ്കെയിലബിൾ ആർക്കിടെക്ചർ.
- Prompt Flow ഉപയോഗിച്ചുള്ള ലോ-കോഡ് സമീപനം

## ആവശ്യമായ കാര്യങ്ങൾ

തുടങ്ങുന്നതിന് മുമ്പ്, താഴെപ്പറയുന്ന ആവശ്യങ്ങൾ പൂർത്തിയാക്കിയിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:

- Docker നിങ്ങളുടെ ലോക്കൽ മെഷീനിൽ ഇൻസ്റ്റാൾ ചെയ്തிருக்கണം.
- കണ്ടെയ്‌നർ റിസോഴ്‌സുകൾ സൃഷ്ടിക്കുകയും മാനേജ് ചെയ്യുകയും ചെയ്യുന്നതിനുള്ള അനുമതികളുള്ള ഒരു Azure അക്കൗണ്ട്.
- Azure AI Studioയും Azure AI Search ഇൻസ്റ്റൻസുകളും
- നിങ്ങളുടെ ഇൻഡക്സ് സൃഷ്ടിക്കാനുള്ള ഒരു embedding മോഡൽ (Azure OpenAI embedding അല്ലെങ്കിൽ കാറ്റലോഗിലുള്ള ഒരു OS മോഡൽ ആയിരിക്കാം)
- Python 3.8 അല്ലെങ്കിൽ പിന്നീട് പതിപ്പ് നിങ്ങളുടെ ലോക്കൽ മെഷീനിൽ ഇൻസ്റ്റാൾ ചെയ്തിരിക്കണം.
- ഒരു Azure Container Registry (അഥവാ നിങ്ങളുടെ തിരഞ്ഞെടുപ്പിലുള്ള ഏതെങ്കിലും റെജിസ്ട്രി)

## ഇൻസ്റ്റലേഷൻ

1. flow.yaml ഫയൽ ഉപയോഗിച്ച് നിങ്ങളുടെ Azure AI Studio പ്രോജക്റ്റിൽ ഒരു പുതിയ flow സൃഷ്ടിക്കുക.
2. Azure AI മോഡൽ കാറ്റലോഗിൽ നിന്നുള്ള Phi3 മോഡൽ ഡിപ്ലോയ് ചെയ്ത് നിങ്ങളുടെ പ്രോജക്റ്റുമായി കണക്ഷൻ സൃഷ്ടിക്കുക. [Phi-3 നെ Model as a Service ആയി ഡിപ്ലോയ് ചെയ്യുക](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. നിങ്ങളുടെ ഇഷ്ടമുള്ള ഏത് ഡോക്യുമെന്റും ഉപയോഗിച്ച് Azure AI Search-ൽ vector index സൃഷ്ടിക്കുക [Azure AI Search-ൽ ഒരു vector index സൃഷ്ടിക്കുക](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. flow നെ ഒരു മാനേജഡ് എൻഡ്‌പോയിന്റിൽ ഡിപ്ലോയ് ചെയ്ത് അത് prompt-flow-frontend.py ഫയലിൽ ഉപയോഗിക്കുക. [ഓൺലൈനായ എൻഡ്‌പോയിന്റിൽ flow ഡിപ്ലോയ് ചെയ്യുക](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. റപ്പോസിറ്ററി ക്ലോൺ ചെയ്യുക:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker ഇമേജ് ബിൽഡ് ചെയ്യുക:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker ഇമേജ് Azure Container Registry-ലേക്ക് പുഷ് ചെയ്യുക:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ഉപയോഗം

1. Docker കണ്ടെയ്‌നർ റൺ ചെയ്യുക:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. നിങ്ങളുടെ ബ്രൗസറിൽ ആപ്ലിക്കേഷൻ താഴെ തന്നിരിക്കുന്ന വിലാസത്തിൽ ആക്‌സസ് ചെയ്യുക: `http://localhost:8501`.

## ബന്ധപ്പെടുക

Valentina Alto - [LinkedIn](https://www.linkedin.com/in/valentina-alto-6a0590148/)

പൂർണ്ണ ലേഖനം: [Azure Model Catalog-യിൽ നിന്നുള്ള Phi-3-Medium നെ Model as a Service ആയി ഉപയോഗിച്ച് RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:

ഈ ദസ്താവേജ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങള്‍ കൃത്യതയിലേക്ക് ശ്രമിച്ചിട്ടും, ഓട്ടോമാറ്റഡ് വിവർത്തനങ്ങളില്‍ പിശകുകളും തെറ്റായ വിവരങ്ങളും ഉണ്ടാകാം എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂല ദസ്താവേജ് അതിന്റെ മാതൃഭാഷയില്‍ ഉള്ള പതിപ്പാണ് പ്രാമാണികമായ ഉറവിടമെന്ന് കണക്കാക്കുക. നിര്‍ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണല്‍ മനുഷ്യ വിവര്‍ത്തനം ഉപദേശിക്കുന്നു. ഈ വിവര്‍ത്തനം ഉപയോഗിച്ചതില്‍നിന്നും ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകള്‍ക്കും വ്യാഖ്യാനഭേദങ്ങള്‍ക്കും ഞങ്ങള്‍ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->