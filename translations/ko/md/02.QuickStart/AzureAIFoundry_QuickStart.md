# **Microsoft Foundry에서 Phi-3 사용하기**

생성 AI의 발전과 함께, 우리는 다양한 LLM 및 SLM, 기업 데이터 통합, 미세 조정/RAG 작업, LLM 및 SLM 통합 후 다양한 기업 비즈니스 평가 등을 관리할 수 있는 통합 플랫폼을 사용하여 생성 AI가 스마트 애플리케이션으로 더 잘 구현될 수 있기를 희망합니다. [Microsoft Foundry](https://ai.azure.com)는 기업용 생성 AI 애플리케이션 플랫폼입니다.

![aistudo](../../../../translated_images/ko/aifoundry_home.f28a8127c96c7d93.webp)

Microsoft Foundry를 사용하면 대형 언어 모델(LLM) 응답을 평가하고 프롬프트 플로우를 통해 프롬프트 애플리케이션 구성요소를 조정하여 더 나은 성능을 얻을 수 있습니다. 이 플랫폼은 개념 증명을 완전한 프로덕션으로 쉽게 전환할 수 있도록 확장성을 지원합니다. 지속적인 모니터링과 개선은 장기적인 성공을 지원합니다.

우리는 간단한 단계로 Phi-3 모델을 Microsoft Foundry에 빠르게 배포한 후, Microsoft Foundry를 사용하여 Phi-3 관련 Playground/Chat, 미세 조정, 평가 등의 작업을 완료할 수 있습니다.

## **1. 준비**

이미 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)를 컴퓨터에 설치한 경우, 이 템플릿을 사용하는 것은 새 디렉터리에서 이 명령을 실행하는 것만큼 간단합니다.

## 수동 생성

Microsoft Foundry 프로젝트와 허브를 생성하는 것은 AI 작업을 구성하고 관리하는 좋은 방법입니다. 시작하는 단계별 가이드는 다음과 같습니다.

### Microsoft Foundry에서 프로젝트 생성하기

1. **Microsoft Foundry로 이동**: Microsoft Foundry 포털에 로그인합니다.
2. **프로젝트 생성**:
   - 프로젝트 내에 있다면, 페이지 왼쪽 상단의 "Microsoft Foundry"를 선택하여 홈 페이지로 이동합니다.
   - "+ 프로젝트 생성"을 선택합니다.
   - 프로젝트 이름을 입력합니다.
   - 허브가 있다면 기본으로 선택됩니다. 여러 허브에 접근 권한이 있다면 드롭다운에서 다른 허브를 선택할 수 있습니다. 새 허브를 생성하려면 "새 허브 생성"을 선택하고 이름을 입력합니다.
   - "생성"을 선택합니다.

### Microsoft Foundry에서 허브 생성하기

1. **Microsoft Foundry로 이동**: Azure 계정으로 로그인합니다.
2. **허브 생성**:
   - 왼쪽 메뉴에서 관리 센터를 선택합니다.
   - "모든 리소스"를 선택한 다음 "+ 새 프로젝트" 옆의 아래쪽 화살표를 눌러 "+ 새 허브"를 선택합니다.
   - "새 허브 생성" 대화 상자에서 허브 이름(예: contoso-hub)을 입력하고 원하는 다른 필드를 수정합니다.
   - "다음"을 선택하고 정보를 검토한 후 "생성"을 선택합니다.

자세한 지침은 공식 [Microsoft 문서](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)를 참조하세요.

성공적으로 생성된 후에는 [ai.azure.com](https://ai.azure.com/)을 통해 생성한 스튜디오에 접속할 수 있습니다.

한 AI Foundry 내에는 여러 프로젝트가 있을 수 있습니다. AI Foundry에서 프로젝트를 생성해 준비하세요.

Microsoft Foundry [빠른 시작](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code) 안내도 참고하세요.


## **2. Microsoft Foundry에서 Phi 모델 배포하기**

프로젝트의 탐색 옵션을 클릭하여 모델 카탈로그에 들어가 Phi-3를 선택합니다.

Phi-3-mini-4k-instruct를 선택합니다.

'배포'를 클릭하여 Phi-3-mini-4k-instruct 모델을 배포합니다.

> [!NOTE]
>
> 배포 시 컴퓨팅 파워를 선택할 수 있습니다.

## **3. Microsoft Foundry에서 Phi 플레이그라운드 채팅**

배포 페이지로 이동하여 Playground를 선택한 후 Microsoft Foundry의 Phi-3와 채팅합니다.

## **4. Microsoft Foundry에서 모델 배포**

Azure 모델 카탈로그에서 모델을 배포하려면 다음 단계를 따르세요:

- Microsoft Foundry에 로그인합니다.
- Microsoft Foundry 모델 카탈로그에서 배포할 모델을 선택합니다.
- 모델 세부 정보 페이지에서 '배포'를 선택한 후 'Serverless API with Azure AI Content Safety'를 선택합니다.
- 모델을 배포할 프로젝트를 선택합니다. Serverless API 이용 시 워크스페이스가 East US 2 또는 Sweden Central 지역에 있어야 합니다. 배포 이름은 사용자 지정 가능합니다.
- 배포 마법사에서 가격 및 이용 약관을 확인합니다.
- '배포'를 선택합니다. 배포가 완료되고 배포 페이지로 리디렉션될 때까지 기다립니다.
- '플레이그라운드에서 열기'를 선택하여 모델과 상호작용을 시작합니다.
- 배포 페이지로 돌아가 배포를 선택한 다음, 호출 및 완료 생성을 위해 사용할 엔드포인트의 대상 URL 및 비밀 키를 확인할 수 있습니다.
- 언제든지 빌드 탭으로 이동하여 컴포넌트 섹션의 배포를 선택하면 엔드포인트 세부 정보, URL 및 액세스 키를 확인할 수 있습니다.

> [!NOTE]
> 해당 단계를 수행하려면 리소스 그룹에 대해 Azure AI 개발자 역할 권한이 있어야 합니다.

## **5. Microsoft Foundry에서 Phi API 사용하기**

Postman GET을 통해 https://{Your project name}.region.inference.ml.azure.com/swagger.json 에 접근하고 키와 결합하여 제공되는 인터페이스를 확인할 수 있습니다.

요청 파라미터와 응답 파라미터를 매우 편리하게 확인할 수 있습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역은 오류나 부정확성이 포함될 수 있음을 유의해 주십시오. 원본 문서의 원어본이 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오용에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->