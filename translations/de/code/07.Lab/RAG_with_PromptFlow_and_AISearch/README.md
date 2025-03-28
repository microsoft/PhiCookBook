<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-03-27T04:42:48+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "de"
}
-->
## RAG mit PromptFlow und AISearch

In diesem Beispiel implementieren wir eine Retrieval Augmented Generation (RAG)-Anwendung, die Phi3 als SLM, AI Search als VectorDB und Prompt Flow als Low-Code-Orchestrator verwendet.

## Funktionen

- Einfache Bereitstellung mit Docker.
- Skalierbare Architektur zur Verarbeitung von KI-Workflows.
- Low-Code-Ansatz mit Prompt Flow.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Anforderungen erfüllen:

- Docker ist auf Ihrem lokalen Rechner installiert.
- Ein Azure-Konto mit Berechtigungen zum Erstellen und Verwalten von Container-Ressourcen.
- Instanzen von Azure AI Studio und Azure AI Search.
- Ein Embedding-Modell zur Erstellung Ihres Index (entweder ein Azure OpenAI Embedding oder ein OS-Modell aus dem Katalog).
- Python 3.8 oder höher ist auf Ihrem lokalen Rechner installiert.
- Ein Azure Container Registry (oder ein beliebiges Registry Ihrer Wahl).

## Installation

1. Erstellen Sie einen neuen Flow in Ihrem Azure AI Studio-Projekt mit der Datei flow.yaml.
2. Stellen Sie ein Phi3-Modell aus dem Azure AI-Modellkatalog bereit und verbinden Sie es mit Ihrem Projekt. [Phi-3 als Modell-as-a-Service bereitstellen](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Erstellen Sie den Vektorindex in Azure AI Search mit einem Dokument Ihrer Wahl. [Einen Vektorindex in Azure AI Search erstellen](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Stellen Sie den Flow auf einem verwalteten Endpunkt bereit und nutzen Sie ihn in der Datei prompt-flow-frontend.py. [Einen Flow auf einem Online-Endpunkt bereitstellen](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonen Sie das Repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Erstellen Sie das Docker-Image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Pushen Sie das Docker-Image in das Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Verwendung

1. Starten Sie den Docker-Container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Greifen Sie über Ihren Browser auf die Anwendung unter `http://localhost:8501` zu.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Vollständiger Artikel: [RAG mit Phi-3-Medium als Modell-as-a-Service aus dem Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.