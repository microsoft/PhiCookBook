<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-04T06:09:55+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ko"
}
-->
# **Generative AI extensions for onnxruntime을 활용한 Phi 패밀리 양자화**

## **Generative AI extensions for onnxruntime란 무엇인가**

이 확장은 ONNX Runtime([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai))을 사용하여 생성적 AI를 실행할 수 있도록 돕습니다. 이 확장은 ONNX 모델을 위한 생성적 AI 루프를 제공하며, ONNX Runtime을 사용한 추론, 로짓 처리, 검색 및 샘플링, 그리고 KV 캐시 관리 등을 포함합니다. 개발자는 고수준의 `generate()` 메서드를 호출하거나 모델의 각 반복을 루프 내에서 실행하여 한 번에 하나의 토큰을 생성하고, 필요에 따라 루프 내에서 생성 매개변수를 업데이트할 수 있습니다. 이 확장은 탐욕적 검색/빔 검색 및 TopP, TopK 샘플링을 지원하여 토큰 시퀀스를 생성하며, 반복 페널티와 같은 내장 로짓 처리를 제공합니다. 또한 사용자 지정 점수를 쉽게 추가할 수 있습니다.

애플리케이션 레벨에서는 Generative AI extensions for onnxruntime을 사용하여 C++/C#/Python을 활용한 애플리케이션을 구축할 수 있습니다. 모델 레벨에서는 미세 조정된 모델을 병합하거나 관련된 양자화 배포 작업을 수행할 수 있습니다.

## **Generative AI extensions for onnxruntime을 활용한 Phi-3.5 양자화**

### **지원 모델**

Generative AI extensions for onnxruntime은 Microsoft Phi, Google Gemma, Mistral, Meta LLaMA의 양자화 변환을 지원합니다.

### **Generative AI extensions for onnxruntime의 모델 빌더**

모델 빌더는 ONNX Runtime의 `generate()` API를 활용하여 최적화되고 양자화된 ONNX 모델을 생성하는 작업을 크게 가속화합니다.

모델 빌더를 통해 INT4, INT8, FP16, FP32로 모델을 양자화할 수 있으며, CPU, CUDA, DirectML, Mobile 등 다양한 하드웨어 가속 방법을 결합할 수 있습니다.

모델 빌더를 사용하려면 다음을 설치해야 합니다:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

설치 후, 터미널에서 모델 빌더 스크립트를 실행하여 모델 형식 및 양자화 변환을 수행할 수 있습니다.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

관련 매개변수 이해하기:

1. **model_name** Hugging Face의 모델 이름입니다. 예: `microsoft/Phi-3.5-mini-instruct`, `microsoft/Phi-3.5-vision-instruct` 등. 또는 모델이 저장된 경로일 수 있습니다.

2. **path_to_output_folder** 양자화 변환 결과 저장 경로입니다.

3. **execution_provider** CPU, CUDA, DirectML 등 다양한 하드웨어 가속 지원을 의미합니다.

4. **cache_dir_to_save_hf_files** Hugging Face에서 모델을 다운로드하여 로컬에 캐시합니다.

***참고：***

## **Model Builder를 활용한 Phi-3.5 양자화 방법**

모델 빌더는 이제 Phi-3.5 Instruct와 Phi-3.5 Vision의 ONNX 모델 양자화를 지원합니다.

### **Phi-3.5-Instruct**

**CPU 가속을 활용한 INT 4 양자화 변환**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 가속을 활용한 INT 4 양자화 변환**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 터미널에서 환경 설정하기

```bash

mkdir models

cd models 

```

2. 모델 폴더에 `microsoft/Phi-3.5-vision-instruct` 다운로드하기  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 아래 파일들을 Phi-3.5-vision-instruct 폴더에 다운로드하세요:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 아래 파일을 모델 폴더에 다운로드하세요:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 터미널에서 실행하기  

   FP32를 지원하는 ONNX로 변환

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **참고：**

1. 모델 빌더는 현재 Phi-3.5-Instruct와 Phi-3.5-Vision의 변환만 지원하며, Phi-3.5-MoE는 지원하지 않습니다.

2. ONNX의 양자화 모델은 Generative AI extensions for onnxruntime SDK를 통해 사용할 수 있습니다.

3. 더 책임감 있는 AI를 고려해야 하므로, 모델 양자화 변환 후 더 효과적인 결과 테스트를 수행하는 것이 권장됩니다.

4. CPU INT4 모델을 양자화하면 엣지 디바이스에 배포할 수 있어 더 나은 애플리케이션 시나리오를 제공합니다. 따라서 INT 4를 중심으로 Phi-3.5-Instruct를 완료했습니다.

## **리소스**

1. Generative AI extensions for onnxruntime에 대해 더 알아보기  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역은 오류나 부정확성을 포함할 수 있습니다. 원본 문서의 모국어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.