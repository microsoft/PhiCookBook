<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:12:03+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ko"
}
-->
# **Android에서 Phi-3 추론하기**

Android 기기에서 Phi-3-mini로 추론을 수행하는 방법을 살펴보겠습니다. Phi-3-mini는 Microsoft에서 새롭게 선보인 모델 시리즈로, 엣지 디바이스와 IoT 기기에서 대형 언어 모델(LLM)을 배포할 수 있게 해줍니다.

## Semantic Kernel과 추론

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)은 Azure OpenAI 서비스, OpenAI 모델, 그리고 로컬 모델과 호환되는 애플리케이션을 만들 수 있는 프레임워크입니다. Semantic Kernel을 처음 접한다면 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 참고하는 것을 추천합니다.

### Semantic Kernel을 이용해 Phi-3-mini 접근하기

Semantic Kernel의 Hugging Face Connector와 결합해서 사용할 수 있습니다. 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

기본적으로 Hugging Face의 모델 ID에 대응하지만, 로컬에서 구축한 Phi-3-mini 모델 서버에도 연결할 수 있습니다.

### Ollama 또는 LlamaEdge로 양자화된 모델 호출하기

많은 사용자가 로컬에서 모델을 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com/)와 [LlamaEdge](https://llamaedge.com)는 개인 사용자가 다양한 양자화 모델을 호출할 수 있게 해줍니다.

#### Ollama

`ollama run Phi-3` 명령어로 직접 실행하거나, `.gguf` 파일 경로를 포함한 `Modelfile`을 만들어 오프라인으로 설정할 수 있습니다.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

클라우드와 엣지 디바이스에서 동시에 `.gguf` 파일을 사용하고 싶다면 LlamaEdge가 좋은 선택입니다. 시작하려면 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

### Android 휴대폰에 설치하고 실행하기

1. Android 휴대폰용 MLC Chat 앱(무료)을 다운로드하세요.  
2. APK 파일(148MB)을 다운로드하여 기기에 설치합니다.  
3. MLC Chat 앱을 실행하면 Phi-3-mini를 포함한 AI 모델 목록이 표시됩니다.

요약하자면, Phi-3-mini는 엣지 디바이스에서 생성형 AI의 새로운 가능성을 열어주며, Android에서 그 기능을 직접 체험해볼 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.