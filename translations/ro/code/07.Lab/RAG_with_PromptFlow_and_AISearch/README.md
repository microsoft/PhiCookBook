## RAG cu PromptFlow și AISearch

În acest exemplu, vom implementa o aplicație Retrieval Augmented Generation (RAG) folosind Phi3 ca SLM, AI Search ca vectorDB și Prompt Flow ca orchestrator low-code.

## Funcționalități

- Implementare ușoară folosind Docker.
- Arhitectură scalabilă pentru gestionarea fluxurilor de lucru AI.
- Abordare low-code cu Prompt Flow.

## Cerințe preliminare

Înainte de a începe, asigură-te că ai îndeplinit următoarele condiții:

- Docker instalat pe mașina ta locală.
- Un cont Azure cu permisiuni pentru a crea și gestiona resurse de containere.
- Instanțe Azure AI Studio și Azure AI Search.
- Un model de embedding pentru a crea indexul (poate fi fie un embedding Azure OpenAI, fie un model OS din catalog).
- Python 3.8 sau o versiune ulterioară instalată pe mașina ta locală.
- Un Azure Container Registry (sau orice alt registru preferat).

## Instalare

1. Creează un nou flow în proiectul tău Azure AI Studio folosind fișierul flow.yaml.
2. Desfășoară un model Phi3 din catalogul tău de modele Azure AI și creează conexiunea către proiectul tău. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Creează indexul vectorial pe Azure AI Search folosind orice document dorești. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Desfășoară flow-ul pe un endpoint gestionat și folosește-l în fișierul prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clonează repository-ul:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Construiește imaginea Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Trimite imaginea Docker către Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Utilizare

1. Rulează containerul Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Accesează aplicația în browser la adresa `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Articol complet: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.