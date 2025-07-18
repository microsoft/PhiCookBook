<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:06:58+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "ko"
}
-->
## RAG with PromptFlow and AISearch

이 예제에서는 Phi3를 SLM으로, AI Search를 vectorDB로, Prompt Flow를 로우코드 오케스트레이터로 활용한 Retrieval Augmented Generation(RAG) 애플리케이션을 구현합니다.

## Features

- Docker를 이용한 간편한 배포.
- AI 워크플로우 처리를 위한 확장 가능한 아키텍처.
- Prompt Flow를 활용한 로우코드 접근법.

## Prerequisites

시작하기 전에 다음 요구 사항을 충족했는지 확인하세요:

- 로컬 머신에 Docker가 설치되어 있어야 합니다.
- 컨테이너 리소스를 생성 및 관리할 수 있는 권한이 있는 Azure 계정.
- Azure AI Studio 및 Azure AI Search 인스턴스.
- 인덱스 생성을 위한 임베딩 모델 (Azure OpenAI 임베딩 또는 카탈로그의 OS 모델 중 하나).
- 로컬 머신에 Python 3.8 이상이 설치되어 있어야 합니다.
- Azure Container Registry(또는 원하는 레지스트리).

## Installation

1. flow.yaml 파일을 사용하여 Azure AI Studio 프로젝트에 새 플로우를 만듭니다.
2. Azure AI 모델 카탈로그에서 Phi3 모델을 배포하고 프로젝트와 연결을 만듭니다. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 원하는 문서를 사용해 Azure AI Search에서 벡터 인덱스를 생성합니다. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 관리형 엔드포인트에 플로우를 배포하고 prompt-flow-frontend.py 파일에서 사용합니다. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 저장소를 클론합니다:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker 이미지를 빌드합니다:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker 이미지를 Azure Container Registry에 푸시합니다:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. Docker 컨테이너를 실행합니다:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 브라우저에서 `http://localhost:8501`로 애플리케이션에 접속합니다.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

전체 기사: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.