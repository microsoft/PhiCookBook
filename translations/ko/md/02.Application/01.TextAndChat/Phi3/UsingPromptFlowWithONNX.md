<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20c7e34651318736a2606d351fcc37d0",
  "translation_date": "2025-04-04T06:33:13+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPromptFlowWithONNX.md",
  "language_code": "ko"
}
-->
# Windows GPU를 사용하여 Phi-3.5-Instruct ONNX 기반의 Prompt flow 솔루션 생성하기

이 문서는 Phi-3 모델을 기반으로 AI 애플리케이션을 개발하기 위해 ONNX(Open Neural Network Exchange)와 PromptFlow를 사용하는 방법을 예시로 제공합니다.

PromptFlow는 LLM(Large Language Model) 기반 AI 애플리케이션의 아이디어 구상, 프로토타이핑, 테스트 및 평가까지의 개발 사이클을 간소화하도록 설계된 개발 도구 모음입니다.

PromptFlow와 ONNX를 통합함으로써 개발자는 다음과 같은 이점을 얻을 수 있습니다:

- **모델 성능 최적화**: ONNX를 활용하여 효율적인 모델 추론 및 배포 가능.
- **개발 간소화**: PromptFlow를 사용하여 워크플로를 관리하고 반복 작업을 자동화.
- **협업 강화**: 통합된 개발 환경을 제공하여 팀 간 협업 향상.

**Prompt flow**는 LLM 기반 AI 애플리케이션의 아이디어 구상, 프로토타이핑, 테스트, 평가부터 프로덕션 배포 및 모니터링까지의 개발 사이클을 간소화하는 개발 도구 모음입니다. 이를 통해 프롬프트 엔지니어링을 훨씬 더 쉽게 만들고 프로덕션 품질의 LLM 애플리케이션을 구축할 수 있습니다.

Prompt flow는 OpenAI, Azure OpenAI Service, 그리고 Huggingface, 로컬 LLM/SLM과 같은 사용자 정의 모델에 연결할 수 있습니다. 우리는 Phi-3.5의 양자화된 ONNX 모델을 로컬 애플리케이션에 배포하고자 합니다. Prompt flow는 우리의 비즈니스 계획을 더 잘 수립하고 Phi-3.5 기반의 로컬 솔루션을 완성할 수 있도록 도움을 줍니다. 이 예제에서는 ONNX Runtime GenAI Library를 결합하여 Windows GPU를 기반으로 한 Prompt flow 솔루션을 완성할 것입니다.

## **설치**

### **Windows GPU용 ONNX Runtime GenAI**

Windows GPU용 ONNX Runtime GenAI 설정에 대한 가이드를 읽어보세요 [여기를 클릭](./ORTWindowGPUGuideline.md)

### **VSCode에서 Prompt flow 설정하기**

1. Prompt flow VS Code 확장 프로그램 설치

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.ko.png)

2. Prompt flow VS Code 확장 프로그램 설치 후, 확장을 클릭하고 **Installation dependencies**를 선택한 다음 이 가이드를 따라 Prompt flow SDK를 환경에 설치하세요.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.ko.png)

3. [샘플 코드 다운로드](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) 후 VS Code로 샘플을 열기

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.ko.png)

4. **flow.dag.yaml** 파일을 열어 Python 환경을 선택하세요.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.ko.png)

   **chat_phi3_ort.py** 파일을 열어 Phi-3.5-instruct ONNX 모델의 위치를 변경하세요.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.ko.png)

5. Prompt flow를 실행하여 테스트하기

**flow.dag.yaml** 파일을 열고 시각적 편집기를 클릭하세요.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.ko.png)

이후 클릭하여 실행하고 테스트하세요.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.ko.png)

1. 터미널에서 배치를 실행하여 추가 결과를 확인할 수 있습니다.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

기본 브라우저에서 결과를 확인할 수 있습니다.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.ko.png)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 최대한 정확성을 기하기 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원래 언어로 작성된 문서)를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용하는 과정에서 발생하는 오해나 잘못된 해석에 대해 당사는 책임지지 않습니다.