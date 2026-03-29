# **Microsoft Phi-3 패밀리로 나만의 Visual Studio Code GitHub Copilot Chat 구축하기**

GitHub Copilot Chat에서 워크스페이스 에이전트를 사용해 보셨나요? 나만의 팀 코드 에이전트를 만들고 싶으신가요? 이 핸즈온 랩은 오픈 소스 모델을 결합하여 엔터프라이즈 수준의 코드 비즈니스 에이전트를 구축하는 것을 목표로 합니다.

## <strong>기초</strong>

### **왜 Microsoft Phi-3를 선택하는가**

Phi-3는 phi-3-mini, phi-3-small, phi-3-medium 등 다양한 텍스트 생성, 대화 완료, 코드 생성용 훈련 파라미터에 따른 패밀리 시리즈를 포함합니다. Vision 기반의 phi-3-vision도 있습니다. 이는 기업 또는 다양한 팀이 오프라인 생성 AI 솔루션을 만드는 데 적합합니다.

다음 링크를 읽어보시길 권장합니다 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 확장 기능은 VS Code 내에서 문서 탐색이나 온라인 포럼 검색 없이 직접 코딩 관련 질문을 할 수 있는 채팅 인터페이스를 제공합니다.

Copilot Chat은 생성된 응답의 명확성을 높이기 위해 구문 강조, 들여쓰기 및 기타 서식 기능을 사용할 수 있습니다. 사용자의 질문 유형에 따라 코드를 생성할 때 참조한 소스 코드 파일이나 문서에 대한 링크, 또는 VS Code 기능에 접근할 수 있는 버튼이 포함될 수 있습니다.

- Copilot Chat은 개발자의 작업 흐름에 통합되어 필요한 곳에 도움을 줍니다:

- 코딩 중에 에디터 또는 터미널에서 직접 인라인 채팅을 시작

- 언제든지 측면에서 AI 어시스턴트를 사용할 수 있는 채팅 뷰 이용

- 빠른 질문과 답변을 위한 Quick Chat 실행

GitHub Copilot Chat은 다음과 같은 다양한 시나리오에서 사용할 수 있습니다:

- 문제를 가장 잘 해결하는 방법에 대한 코딩 질문 답변

- 타인의 코드를 설명하고 개선 제안

- 코드 수정 제안

- 단위 테스트 케이스 생성

- 코드 문서 생성

다음 링크를 읽어보시길 권장합니다 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat에서 <strong>@workspace</strong>를 참조하면 전체 코드베이스에 대해 질문할 수 있습니다. 질문에 따라 Copilot은 관련 파일과 심볼을 지능적으로 검색하고, 이를 링크 및 코드 예제 형태로 답변에 참조합니다.

질문에 답하기 위해 <strong>@workspace</strong>는 VS Code에서 개발자가 코드베이스를 탐색할 때 사용하는 동일한 소스를 검색합니다:

- .gitignore 파일에 의해 무시되지 않은 워크스페이스 내 모든 파일

- 중첩된 폴더와 파일명을 포함한 디렉터리 구조

- 워크스페이스가 GitHub 저장소이고 코드 검색으로 인덱싱된 경우 GitHub의 코드 검색 인덱스

- 워크스페이스 내의 심볼 및 정의

- 현재 선택한 텍스트 또는 활성 편집기에 표시 중인 텍스트

참고: .gitignore에 의해 무시되는 파일을 열었거나 텍스트를 선택한 경우 무시되지 않습니다.

다음 링크를 읽어보시길 권장합니다 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **이 랩에 대해 더 알아보기**

GitHub Copilot은 기업의 프로그래밍 효율을 크게 향상시켰으며, 각 기업은 GitHub Copilot의 관련 기능을 맞춤화하기를 희망합니다. 많은 기업은 자사 비즈니스 시나리오와 오픈 소스 모델을 기반으로 GitHub Copilot과 유사한 맞춤형 확장 기능을 개발했습니다. 기업에 있어 맞춤형 확장 기능은 관리가 더 쉽지만, 사용자 경험에 영향을 미치기도 합니다. 결국 GitHub Copilot은 일반적인 시나리오와 전문성에 강력한 기능이 있습니다. 경험을 일관되게 유지하면서 기업의 맞춤형 확장 기능을 만드는 것이 더 좋습니다. GitHub Copilot Chat은 기업이 채팅 경험을 확장할 수 있는 관련 API를 제공합니다. 일관된 경험 유지와 맞춤형 기능 추가는 더 나은 사용자 경험을 의미합니다.

이 랩은 주로 Phi-3 모델과 로컬 NPU, Azure 하이브리드를 결합해 GitHub Copilot Chat에서 맞춤형 에이전트 <strong><em>@PHI3</em></strong>를 구축하여 엔터프라이즈 개발자들의 코드 생성 완료<strong><em>(@PHI3 /gen)</em></strong> 및 이미지 기반 코드 생성 <strong><em>(@PHI3 /img)</em></strong>을 지원합니다.

![PHI3](../../../../../../../translated_images/ko/cover.1017ebc9a7c46d09.webp)

### ***참고:*** 

이 랩은 현재 Intel CPU 및 Apple Silicon 기반 AIPC에서 구현됩니다. Qualcomm 버전 NPU는 계속 업데이트할 예정입니다.


## <strong>랩</strong>

| 이름 | 설명 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - 설치(✅) | 관련 환경 및 설치 도구 구성 및 설치 | [가기](./HOL/AIPC/01.Installations.md) |[가기](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini로 Prompt flow 실행 (✅) | AIPC / Apple Silicon과 결합해 로컬 NPU를 사용하여 Phi-3-mini로 코드 생성 | [가기](./HOL/AIPC/02.PromptflowWithNPU.md) |  [가기](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service에 Phi-3-vision 배포(✅) | Azure Machine Learning Service의 모델 카탈로그 - Phi-3-vision 이미지 배포로 코드 생성 | [가기](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[가기](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat에서 @phi-3 에이전트 생성(✅)  | GitHub Copilot Chat에 맞춤형 Phi-3 에이전트 생성하여 코드 생성, 그래프 생성 코드, RAG 등 수행 | [가기](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [가기](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| 샘플 코드 (✅)  | 샘플 코드 다운로드 | [가기](../../../../../../../code/07.Lab/01/AIPC) | [가기](../../../../../../../code/07.Lab/01/Apple) |


## <strong>자료</strong>

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot 더 알아보기 [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat 더 알아보기 [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API 더 알아보기 [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry 더 알아보기 [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry의 모델 카탈로그 더 알아보기 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 양지해 주시기 바랍니다. 원본 문서는 해당 언어로 된 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우에는 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 어떠한 오해나 잘못된 해석에 대해서도 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->