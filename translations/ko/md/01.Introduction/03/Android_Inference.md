<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-04T05:54:13+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "ko"
}
-->
# **Android에서 Phi-3 추론**

Android 기기에서 Phi-3-mini를 활용한 추론 방법을 알아보겠습니다. Phi-3-mini는 Microsoft의 새로운 모델 시리즈로, 대규모 언어 모델(LLM)을 엣지 기기 및 IoT 기기에서 배포할 수 있도록 지원합니다.

## Semantic Kernel과 추론

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)은 Azure OpenAI Service, OpenAI 모델, 로컬 모델과 호환되는 애플리케이션을 만들 수 있도록 돕는 애플리케이션 프레임워크입니다. Semantic Kernel이 처음이라면 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 참고하시길 추천합니다.

### Semantic Kernel을 사용하여 Phi-3-mini에 접근하기

Semantic Kernel에서 Hugging Face Connector와 결합하여 사용할 수 있습니다. [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

기본적으로 Hugging Face의 모델 ID와 연결됩니다. 하지만 로컬에서 빌드한 Phi-3-mini 모델 서버와 연결할 수도 있습니다.

### Ollama 또는 LlamaEdge를 사용한 양자화된 모델 호출

많은 사용자가 모델을 로컬에서 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com/)와 [LlamaEdge](https://llamaedge.com)는 개별 사용자가 다양한 양자화된 모델을 호출할 수 있도록 지원합니다:

#### Ollama

`ollama run Phi-3`를 직접 실행하거나 `.gguf` 파일 경로를 포함하는 `Modelfile`을 생성하여 오프라인에서 구성할 수 있습니다.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

클라우드와 엣지 기기에서 `.gguf` 파일을 동시에 사용하려면 LlamaEdge가 좋은 선택입니다. 시작하려면 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

### Android 휴대폰에 설치 및 실행

1. **MLC Chat 앱 다운로드** (무료) - Android 휴대폰용.
2. APK 파일(148MB)을 다운로드하여 기기에 설치합니다.
3. MLC Chat 앱을 실행합니다. Phi-3-mini를 포함한 AI 모델 목록이 표시됩니다.

요약하자면, Phi-3-mini는 엣지 기기에서 생성형 AI를 활용할 수 있는 흥미로운 가능성을 열어주며, Android에서 그 기능을 탐색해볼 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 최대한 정확성을 기하기 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 신뢰할 수 있는 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임지지 않습니다.