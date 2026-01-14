<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:29:42+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "ko"
}
-->
# **Azure AI Foundry를 사용한 평가 방법**

![aistudo](../../../../../translated_images/ko/AIFoundry.9e0b513e999a1c5a.png)

[Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)를 사용하여 생성형 AI 애플리케이션을 평가하는 방법입니다. 단일 대화 또는 다중 대화를 평가하든, Azure AI Foundry는 모델 성능과 안전성을 평가할 수 있는 도구를 제공합니다.

![aistudo](../../../../../translated_images/ko/AIPortfolio.69da59a8e1eaa70f.png)

## Azure AI Foundry로 생성형 AI 앱 평가하기
자세한 내용은 [Azure AI Foundry 문서](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

시작하는 단계는 다음과 같습니다:

## Azure AI Foundry에서 생성형 AI 모델 평가하기

**사전 준비 사항**

- CSV 또는 JSON 형식의 테스트 데이터셋
- 배포된 생성형 AI 모델 (예: Phi-3, GPT 3.5, GPT 4, Davinci 모델 등)
- 평가를 실행할 수 있는 컴퓨트 인스턴스가 포함된 런타임

## 내장 평가 지표

Azure AI Foundry는 단일 대화와 복잡한 다중 대화 모두를 평가할 수 있습니다.  
특정 데이터에 기반한 Retrieval Augmented Generation(RAG) 시나리오에서는 내장된 평가 지표를 사용해 성능을 측정할 수 있습니다.  
또한, 일반적인 단일 대화 질문 응답 시나리오(비-RAG)도 평가할 수 있습니다.

## 평가 실행 생성하기

Azure AI Foundry UI에서 Evaluate 페이지 또는 Prompt Flow 페이지로 이동하세요.  
평가 생성 마법사를 따라 평가 실행을 설정합니다. 평가에 대한 선택적 이름을 지정할 수 있습니다.  
애플리케이션 목표에 맞는 시나리오를 선택하세요.  
모델 출력을 평가할 하나 이상의 평가 지표를 선택합니다.

## 맞춤 평가 흐름 (선택 사항)

더 큰 유연성을 원한다면, 맞춤 평가 흐름을 설정할 수 있습니다.  
특정 요구사항에 맞게 평가 과정을 조정하세요.

## 결과 확인하기

평가 실행 후, Azure AI Foundry에서 상세한 평가 지표를 기록하고 확인하며 분석할 수 있습니다.  
애플리케이션의 강점과 한계를 파악하는 데 도움이 됩니다.

**Note** Azure AI Foundry는 현재 공개 프리뷰 단계이므로 실험 및 개발 목적으로 사용하세요.  
운영 환경에서는 다른 옵션을 고려하는 것이 좋습니다.  
자세한 내용과 단계별 안내는 공식 [AI Foundry 문서](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.