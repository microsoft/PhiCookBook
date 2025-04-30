<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-04T05:32:59+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "ko"
}
-->
## PromptFlow와 AISearch를 활용한 RAG

이 예제에서는 SLM으로 Phi3, 벡터DB로 AI Search, 그리고 저코드 오케스트레이터로 Prompt Flow를 활용하여 Retrieval Augmented Generation (RAG) 애플리케이션을 구현합니다.

## 주요 기능

- Docker를 사용한 간편한 배포
- AI 워크플로를 처리할 수 있는 확장 가능한 아키텍처
- Prompt Flow를 활용한 저코드 접근 방식

## 사전 요구 사항

시작하기 전에 다음 요구 사항을 충족했는지 확인하세요:

- 로컬 머신에 Docker가 설치되어 있어야 합니다.
- 컨테이너 리소스를 생성하고 관리할 수 있는 권한이 있는 Azure 계정
- Azure AI Studio 및 Azure AI Search 인스턴스
- 인덱스를 생성하기 위한 임베딩 모델 (Azure OpenAI 임베딩 또는 카탈로그에서 제공되는 OS 모델 중 하나를 선택 가능)
- 로컬 머신에 Python 3.8 이상 설치
- Azure Container Registry (또는 선택한 다른 레지스트리)

## 설치 방법

1. flow.yaml 파일을 사용하여 Azure AI Studio 프로젝트에서 새 플로우를 생성하세요.
2. Azure AI 모델 카탈로그에서 Phi3 모델을 배포하고 프로젝트와 연결을 생성하세요. [Phi-3를 모델로 배포하기](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 원하는 문서를 사용하여 Azure AI Search에서 벡터 인덱스를 생성하세요. [Azure AI Search에서 벡터 인덱스 생성하기](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 관리 엔드포인트에 플로우를 배포하고 prompt-flow-frontend.py 파일에서 사용하세요. [온라인 엔드포인트에 플로우 배포하기](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 레포지토리를 클론하세요:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker 이미지를 빌드하세요:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker 이미지를 Azure Container Registry에 푸시하세요:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 사용 방법

1. Docker 컨테이너를 실행하세요:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 브라우저에서 `http://localhost:8501`로 애플리케이션에 접속하세요.

## 문의

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

전체 글: [Azure 모델 카탈로그에서 제공하는 Phi-3-Medium을 활용한 RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원문이 작성된 언어의 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.