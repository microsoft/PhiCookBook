<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-08T06:11:25+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ko"
}
-->
# **llama.cpp를 이용한 Phi 패밀리 양자화**

## **llama.cpp란?**

llama.cpp는 주로 C++로 작성된 오픈소스 소프트웨어 라이브러리로, Llama와 같은 다양한 대형 언어 모델(LLM)에 대한 추론을 수행합니다. 이 라이브러리의 주요 목적은 최소한의 설정으로 다양한 하드웨어에서 최첨단 성능을 제공하는 것입니다. 또한, 텍스트 완성을 위한 고수준 API와 OpenAI 호환 웹 서버를 제공하는 Python 바인딩도 함께 제공됩니다.

llama.cpp의 핵심 목표는 로컬 및 클라우드 환경에서 최소한의 설정으로 다양한 하드웨어에서 최첨단 LLM 추론을 가능하게 하는 것입니다.

- 의존성 없는 순수 C/C++ 구현
- Apple 실리콘에 최적화되어 ARM NEON, Accelerate, Metal 프레임워크 활용
- x86 아키텍처용 AVX, AVX2, AVX512 지원
- 1.5비트, 2비트, 3비트, 4비트, 5비트, 6비트, 8비트 정수 양자화를 통해 추론 속도 향상 및 메모리 사용 감소
- NVIDIA GPU에서 LLM 실행을 위한 맞춤형 CUDA 커널 (AMD GPU는 HIP 지원)
- Vulkan 및 SYCL 백엔드 지원
- VRAM 용량을 초과하는 대형 모델을 부분 가속하는 CPU+GPU 하이브리드 추론

## **llama.cpp를 이용한 Phi-3.5 양자화**

Phi-3.5-Instruct 모델은 llama.cpp를 통해 양자화할 수 있지만, Phi-3.5-Vision과 Phi-3.5-MoE는 아직 지원되지 않습니다. llama.cpp가 변환하는 포맷은 gguf로, 가장 널리 사용되는 양자화 포맷이기도 합니다.

Hugging Face에는 양자화된 GGUF 포맷 모델이 많이 있습니다. AI Foundry, Ollama, LlamaEdge가 llama.cpp를 기반으로 하고 있어 GGUF 모델이 자주 활용됩니다.

### **GGUF란?**

GGUF는 모델의 빠른 로딩과 저장에 최적화된 바이너리 포맷으로, 추론 효율성이 매우 높습니다. GGUF는 GGML 및 기타 실행기와 함께 사용하도록 설계되었습니다. GGUF는 llama.cpp의 개발자인 @ggerganov가 만들었으며, PyTorch와 같은 프레임워크에서 개발된 모델을 GGUF 포맷으로 변환해 해당 엔진에서 사용할 수 있습니다.

### **ONNX와 GGUF 비교**

ONNX는 전통적인 머신러닝/딥러닝 포맷으로, 다양한 AI 프레임워크에서 잘 지원되며 엣지 디바이스에서 활용도가 높습니다. 반면 GGUF는 llama.cpp 기반으로 GenAI 시대에 맞게 만들어졌다고 할 수 있습니다. 두 포맷은 유사한 용도로 사용됩니다. 임베디드 하드웨어 및 애플리케이션 레이어에서 더 나은 성능을 원한다면 ONNX가 적합할 수 있고, llama.cpp 파생 프레임워크와 기술을 사용한다면 GGUF가 더 나을 수 있습니다.

### **llama.cpp를 이용한 Phi-3.5-Instruct 양자화**

**1. 환경 설정**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. 양자화**

llama.cpp를 사용해 Phi-3.5-Instruct를 FP16 GGUF로 변환


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5를 INT4로 양자화


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. 테스트**

llama-cpp-python 설치


```bash

pip install llama-cpp-python -U

```

***참고***

Apple Silicon을 사용할 경우 다음과 같이 llama-cpp-python을 설치하세요


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

테스트 실행


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **자료**

1. llama.cpp에 대해 더 알아보기 [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime에 대해 더 알아보기 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF에 대해 더 알아보기 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.