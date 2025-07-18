<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:08:32+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "el"
}
-->
## RAG με PromptFlow και AISearch

Σε αυτό το παράδειγμα, θα υλοποιήσουμε μια εφαρμογή Retrieval Augmented Generation (RAG) χρησιμοποιώντας το Phi3 ως SLM, το AI Search ως vectorDB και το Prompt Flow ως low-code orchestrator.

## Χαρακτηριστικά

- Εύκολη ανάπτυξη με χρήση Docker.
- Κλιμακούμενη αρχιτεκτονική για τη διαχείριση ροών εργασίας AI.
- Προσέγγιση με χαμηλό κώδικα χρησιμοποιώντας το Prompt Flow.

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε καλύψει τις παρακάτω προϋποθέσεις:

- Εγκατεστημένο Docker στον τοπικό σας υπολογιστή.
- Λογαριασμό Azure με δικαιώματα για δημιουργία και διαχείριση πόρων container.
- Περιπτώσεις Azure AI Studio και Azure AI Search.
- Ένα μοντέλο embedding για τη δημιουργία του ευρετηρίου σας (μπορεί να είναι είτε Azure OpenAI embedding είτε μοντέλο OS από τον κατάλογο).
- Εγκατεστημένο Python 3.8 ή νεότερη έκδοση στον τοπικό σας υπολογιστή.
- Ένα Azure Container Registry (ή οποιοδήποτε registry της επιλογής σας).

## Εγκατάσταση

1. Δημιουργήστε μια νέα ροή στο έργο σας Azure AI Studio χρησιμοποιώντας το αρχείο flow.yaml.
2. Αναπτύξτε ένα μοντέλο Phi3 από τον κατάλογο μοντέλων Azure AI και δημιουργήστε τη σύνδεση με το έργο σας. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Δημιουργήστε το vector index στο Azure AI Search χρησιμοποιώντας οποιοδήποτε έγγραφο επιθυμείτε [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Αναπτύξτε τη ροή σε ένα managed endpoint και χρησιμοποιήστε την στο αρχείο prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Κλωνοποιήστε το αποθετήριο:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Δημιουργήστε το Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Σπρώξτε το Docker image στο Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Χρήση

1. Εκτελέστε το Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Ανοίξτε την εφαρμογή στον περιηγητή σας στη διεύθυνση `http://localhost:8501`.

## Επικοινωνία

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Πλήρες Άρθρο: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.