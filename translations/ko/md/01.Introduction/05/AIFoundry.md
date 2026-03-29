# **Microsoft Foundry를 사용한 평가**

![aistudo](../../../../../translated_images/ko/AIFoundry.9e0b513e999a1c5a.webp)

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)를 사용하여 생성 AI 애플리케이션을 평가하는 방법입니다. 단일 턴 대화이든 다중 턴 대화이든, Microsoft Foundry는 모델 성능과 안전성을 평가할 수 있는 도구를 제공합니다. 

![aistudo](../../../../../translated_images/ko/AIPortfolio.69da59a8e1eaa70f.webp)

## Microsoft Foundry로 생성 AI 앱 평가하기
자세한 안내는 [Microsoft Foundry 문서](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

시작하는 단계는 다음과 같습니다:

## Microsoft Foundry에서 생성 AI 모델 평가하기

**사전 준비 사항**

- CSV 또는 JSON 형식의 테스트 데이터셋.
- Phi-3, GPT 3.5, GPT 4, 또는 Davinci 모델과 같은 배포된 생성 AI 모델.
- 평가를 실행할 컴퓨팅 인스턴스가 포함된 런타임.

## 내장 평가 지표

Microsoft Foundry는 단일 턴 및 복잡한 다중 턴 대화 모두 평가할 수 있습니다.
모델이 특정 데이터에 기반한 검색 증강 생성(RAG) 시나리오의 경우, 내장된 평가 지표를 사용하여 성능을 평가할 수 있습니다.
또한 일반적인 단일 턴 질문 응답 시나리오(비-RAG)도 평가할 수 있습니다.

## 평가 실행 생성하기

Microsoft Foundry UI에서 Evaluate 페이지 또는 Prompt Flow 페이지로 이동하십시오.
평가 생성 마법사를 따라 평가 실행을 설정합니다. 평가에 선택적으로 이름을 지정할 수 있습니다.
애플리케이션 목표에 맞는 시나리오를 선택합니다.
모델 출력 결과를 평가하기 위한 하나 이상의 평가 지표를 선택합니다.

## 사용자 정의 평가 흐름 (선택 사항)

더 큰 유연성을 위해 맞춤형 평가 흐름을 설정할 수 있습니다. 특정 요구 사항에 따라 평가 프로세스를 사용자 정의하세요.

## 결과 보기

평가를 실행한 후 Microsoft Foundry에서 상세 평가 지표를 기록, 조회 및 분석할 수 있습니다. 애플리케이션의 능력과 한계에 대한 인사이트를 얻으세요.

**Note** Microsoft Foundry는 현재 공개 미리보기 상태이므로 실험 및 개발 목적으로 사용하세요. 운영 환경에는 다른 옵션을 고려해야 합니다. 자세한 내용과 단계별 지침은 공식 [AI Foundry 문서](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 오인에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->