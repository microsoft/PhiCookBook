# **Android에서의 Phi-3 추론**

Android 기기에서 Phi-3-mini로 추론을 수행하는 방법을 알아봅시다. Phi-3-mini는 Microsoft의 새로운 모델 시리즈로, 엣지 디바이스 및 IoT 디바이스에서 대형 언어 모델(LLM)을 배포할 수 있게 해줍니다.

## 시맨틱 커널과 추론

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)은 Azure OpenAI 서비스, OpenAI 모델, 그리고 로컬 모델과 호환되는 애플리케이션을 만들 수 있는 프레임워크입니다. 시맨틱 커널이 처음이라면 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 참고하시길 권장합니다.

### Semantic Kernel을 통한 Phi-3-mini 접근 방법

Semantic Kernel의 Hugging Face 커넥터와 결합할 수 있습니다. 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)를 참조하세요.

기본적으로 Hugging Face의 모델 ID에 대응하지만, 로컬에서 구축한 Phi-3-mini 모델 서버와도 연결할 수 있습니다.

### Ollama 또는 LlamaEdge를 사용한 양자화 모델 호출

많은 사용자가 모델을 로컬에서 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com/)와 [LlamaEdge](https://llamaedge.com)는 개별 사용자가 다양한 양자화 모델을 호출할 수 있도록 합니다:

#### Ollama

`ollama run Phi-3`를 직접 실행하거나, `.gguf` 파일 경로를 가진 `Modelfile`를 생성하여 오프라인으로 구성할 수 있습니다.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

클라우드와 엣지 디바이스에서 동시에 `.gguf` 파일을 사용하고자 한다면, LlamaEdge가 훌륭한 선택입니다. 시작을 위해 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)를 참고할 수 있습니다.

### Android 휴대폰에 설치 및 실행하기

1. Android 휴대폰용으로 MLC Chat 앱(무료)을 다운로드하세요.
2. APK 파일(148MB)을 다운로드하여 기기에 설치하세요.
3. MLC Chat 앱을 실행하세요. Phi-3-mini를 포함한 AI 모델 목록을 볼 수 있습니다.

### LiteRT-LM으로 Phi-4-mini-reasoning 실행하기

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning)은 커뮤니티에서 변환한 int4 `.litertlm` 번들로 구글의 [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) 온디바이스 런타임용입니다. Android에서는 CPU 또는 GPU를 통해 [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) 앱(앱 내에서 Hugging Face에서 번들 임포트)이나 LiteRT-LM Kotlin API로 실행할 수 있으며, 동일한 번들은 iOS, macOS, Linux, Windows에서도 실행 가능합니다. 모델 카드에는 측정된 속도와 실행 명령어가 나와 있습니다.

요약하자면, Phi-3-mini는 엣지 디바이스에서 생성 AI에 대한 흥미로운 가능성을 열어주며 Android에서 그 기능을 탐험하기 시작할 수 있습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->