<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-12-21T15:47:45+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "kn"
}
-->
## RAG with PromptFlow and AISearch

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು Phi3 ಅನ್ನು SLM ಆಗಿ, AI Search ಅನ್ನು vectorDB ಆಗಿ ಮತ್ತು Prompt Flow ಅನ್ನು low-code orchestrator ಆಗಿ ಉಪಯೋಗಿಸುವ Retrieval Augmented Generation (RAG) ಅನ್ವಯಿಕೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತೇವೆ.

## Features

- Docker ಬಳಸಿ ಸುಲಭವಾಗಿ ನಿಯೋಜನೆ.
- AI ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ನಿರ್ವಹಿಸಲು масштаб ಮಾಡುವ معم架.
- Prompt Flow ಬಳಸಿ ಲೋ-ಕೋಡ್ ಉಪಾಯ

## Prerequisites

ಪ್ರಾರಂಭಿಸುವ ಮುನ್ನ, ದಯವಿಟ್ಟು ನೀವು ಕೆಳಗಿನ ಅವಶ್ಯತೆಗಳನ್ನು ಪೂರೈಸಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

- ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರದಲ್ಲಿ Docker ಸ್ಥಾಪಿತವಾಗಿದೆ.
- ಕಂಟೈನರ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸಲು ಮತ್ತು ನಿರ್ವಹಿಸಲು ಅನುಮತಿ ಇರುವ Azure ಖಾತೆ.
- Azure AI Studio ಮತ್ತು Azure AI Search ಇನ್‌ಸ್ಟಾನ್ಸ್‌ಗಳು
- ನಿಮ್ಮ ಸೂಚ್ಯಂಕವನ್ನು ರಚಿಸಲು ಒಂದು ಎంబೆದ್ದಿಂಗ್ ಮಾದರಿ (ಇದು Azure OpenAI embedding ಆಗಿರಬಹುದು ಅಥವಾ ಕ್ಯಾಟಲಾಗ್‌ನಿಂದ OS ಮಾದರಿ)
- ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರದಲ್ಲಿ Python 3.8 ಅಥವಾ ನಂತರದ ಸ್ವರೂಪ ಸ್ಥಾಪಿತವಾಗಿದೆ.
- ಒಂದು Azure Container Registry (ಅಥವಾ ನಿಮ್ಮ ಆಯ್ಕೆಯ ಯಾವುದೇ ರೆಜಿಸ್ಟ್ರಿ)

## Installation

1. flow.yaml ಫೈಲ್ ಬಳಸಿ ನಿಮ್ಮ Azure AI Studio Project ನಲ್ಲಿ ಹೊಸ flow ರಚಿಸಿ.
2. Azure AI model catalog ನಿಂದ Phi3 ಮಾದರಿಯನ್ನು ಡಿಪ್ಲಾಯ್ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಪPROJECT ಗೆ ಕನೆಕ್ಷನ್ ರಚಿಸಿ. [Phi-3 ಅನ್ನು Model as a Service ಆಗಿ ಡಿಪ್ಲಾಯ್ ಮಾಡಿ](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. ನಿಮ್ಮ ಆಯ್ಕೆಯ ಯಾವುದೇ ಡಾಕ್ಯುಮೆಂಟ್ ಬಳಸಿ Azure AI Search ನಲ್ಲಿ ವೆಕ್ಟರ್ ಸೂಚ್ಯಂಕವನ್ನು ರಚಿಸಿ [Azure AI Search ನಲ್ಲಿ ವೆಕ್ಟರ್ ಇಂಡೆಕ್ಸ್ ಸೃಜಿಸಿ](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. flow ಅನ್ನು ನಿರ್ವಹಿತ enpoint ಮೇಲೆ ಡಿಪ್ಲಾಯ್ ಮಾಡಿ ಮತ್ತು prompt-flow-frontend.py ಫೈಲ್‌ನಲ್ಲಿ ಅದನ್ನು ಬಳಸಿ. [ಆನ್ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನಲ್ಲಿ flow ಅನ್ನು ಡಿಪ್ಲಾಯ್ ಮಾಡಿ](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ರಿಪೊಸಿಟರಿ ಕ್ಲೋನ್ ಮಾಡಿ:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker ಇಮೇಜ್ ನಿರ್ಮಿಸಿ:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker ಇಮೇಜ್ ಅನ್ನು Azure Container Registry ಗೆ ಪುಷ್ ಮಾಡಿ:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. Docker ಕಂಟೈನರ್ ಅನ್ನು ಓಡಿಸಿ:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು `http://localhost:8501` ನಲ್ಲಿ ಪ್ರವೇಶಿಸಿ.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

ಸಂಪೂರ್ಣ ಲೇಖನ: [Azure Model Catalog ನಿಂದ Phi-3-Medium ಅನ್ನು Model as a Service ಆಗಿ ಬಳಸಿಕೊಂಡು RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ (Co-op Translator: https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅನಿಖ್ಯತತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿರಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಅವರನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅರ್ಥಭ್ರಾಂಶಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->