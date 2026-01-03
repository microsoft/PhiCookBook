<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:20:59+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "ko"
}
-->
# **Azure AI Foundry에서 Phi-3 사용하기**

생성형 AI의 발전과 함께, 다양한 LLM과 SLM, 기업 데이터 통합, 파인튜닝/RAG 작업, 그리고 LLM과 SLM 통합 후 다양한 기업 비즈니스 평가를 하나의 통합 플랫폼에서 관리하여 생성형 AI 기반 스마트 애플리케이션을 더 잘 구현하고자 합니다. [Azure AI Foundry](https://ai.azure.com)는 기업용 생성형 AI 애플리케이션 플랫폼입니다.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93.ko.png)

Azure AI Foundry를 사용하면 대형 언어 모델(LLM) 응답을 평가하고, 프롬프트 플로우를 통해 프롬프트 애플리케이션 구성 요소를 조율하여 더 나은 성능을 낼 수 있습니다. 이 플랫폼은 개념 증명을 완전한 프로덕션으로 전환하는 데 필요한 확장성을 지원하며, 지속적인 모니터링과 개선을 통해 장기적인 성공을 돕습니다.

간단한 단계로 Azure AI Foundry에 Phi-3 모델을 빠르게 배포한 후, Playground/Chat, 파인튜닝, 평가 등 Phi-3 관련 작업을 Azure AI Foundry에서 수행할 수 있습니다.

## **1. 준비하기**

이미 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)가 설치되어 있다면, 새 디렉터리에서 이 템플릿을 실행하는 것만으로 간단히 시작할 수 있습니다.

## 수동 생성

Microsoft Azure AI Foundry 프로젝트와 허브를 생성하는 것은 AI 작업을 체계적으로 관리하는 좋은 방법입니다. 다음은 시작하는 단계별 가이드입니다:

### Azure AI Foundry에서 프로젝트 생성하기

1. **Azure AI Foundry 접속**: Azure AI Foundry 포털에 로그인합니다.
2. **프로젝트 생성**:
   - 이미 프로젝트 내에 있다면, 페이지 왼쪽 상단에서 "Azure AI Foundry"를 선택해 홈 페이지로 이동합니다.
   - "+ Create project"를 선택합니다.
   - 프로젝트 이름을 입력합니다.
   - 허브가 있다면 기본으로 선택됩니다. 여러 허브에 접근 권한이 있다면 드롭다운에서 다른 허브를 선택할 수 있습니다. 새 허브를 만들고 싶다면 "Create new hub"를 선택하고 이름을 입력합니다.
   - "Create"를 선택합니다.

### Azure AI Foundry에서 허브 생성하기

1. **Azure AI Foundry 접속**: Azure 계정으로 로그인합니다.
2. **허브 생성**:
   - 왼쪽 메뉴에서 관리 센터(Management center)를 선택합니다.
   - "All resources"를 선택한 후, "+ New project" 옆의 아래쪽 화살표를 클릭하고 "+ New hub"를 선택합니다.
   - "Create a new hub" 대화상자에서 허브 이름(예: contoso-hub)을 입력하고 원하는 다른 필드를 수정합니다.
   - "Next"를 선택하고 정보를 검토한 후 "Create"를 선택합니다.

자세한 내용은 공식 [Microsoft 문서](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)를 참고하세요.

성공적으로 생성한 후에는 [ai.azure.com](https://ai.azure.com/)을 통해 생성한 스튜디오에 접속할 수 있습니다.

하나의 AI Foundry에는 여러 프로젝트가 있을 수 있으니, AI Foundry에서 프로젝트를 생성해 준비하세요.

Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)도 참고하세요.

## **2. Azure AI Foundry에서 Phi 모델 배포하기**

프로젝트의 Explore 옵션을 클릭해 모델 카탈로그에 들어가 Phi-3를 선택합니다.

Phi-3-mini-4k-instruct를 선택합니다.

'Deploy'를 클릭해 Phi-3-mini-4k-instruct 모델을 배포합니다.

> [!NOTE]
>
> 배포 시 컴퓨팅 파워를 선택할 수 있습니다.

## **3. Azure AI Foundry에서 Playground Chat Phi 사용하기**

배포 페이지로 이동해 Playground를 선택한 후 Azure AI Foundry의 Phi-3와 채팅합니다.

## **4. Azure AI Foundry에서 모델 배포하기**

Azure 모델 카탈로그에서 모델을 배포하려면 다음 단계를 따르세요:

- Azure AI Foundry에 로그인합니다.
- Azure AI Foundry 모델 카탈로그에서 배포할 모델을 선택합니다.
- 모델 상세 페이지에서 Deploy를 선택한 후 Azure AI Content Safety가 포함된 Serverless API를 선택합니다.
- 모델을 배포할 프로젝트를 선택합니다. Serverless API를 사용하려면 작업 공간이 East US 2 또는 Sweden Central 지역에 있어야 합니다. 배포 이름을 사용자 지정할 수 있습니다.
- 배포 마법사에서 가격 및 이용 약관을 확인합니다.
- Deploy를 선택합니다. 배포가 준비되고 배포 페이지로 리디렉션될 때까지 기다립니다.
- Open in playground를 선택해 모델과 상호작용을 시작합니다.
- 배포 페이지로 돌아가 배포를 선택하면 호출에 사용할 수 있는 엔드포인트의 Target URL과 Secret Key를 확인할 수 있습니다.
- 언제든지 Build 탭에서 Components 섹션의 Deployments를 선택해 엔드포인트 세부 정보, URL, 액세스 키를 확인할 수 있습니다.

> [!NOTE]
> 이 단계를 수행하려면 계정에 리소스 그룹에 대한 Azure AI Developer 역할 권한이 있어야 합니다.

## **5. Azure AI Foundry에서 Phi API 사용하기**

Postman에서 https://{Your project name}.region.inference.ml.azure.com/swagger.json에 GET 요청을 보내고 Key와 함께 제공된 인터페이스를 확인할 수 있습니다.

요청 파라미터와 응답 파라미터를 매우 편리하게 확인할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.