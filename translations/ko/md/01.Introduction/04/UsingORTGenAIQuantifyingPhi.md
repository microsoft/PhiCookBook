<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-08T06:12:43+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ko"
}
-->
## **Model Builder를 사용하여 Phi-3.5 양자화하는 방법**

Model Builder는 현재 Phi-3.5 Instruct와 Phi-3.5-Vision의 ONNX 모델 양자화를 지원합니다.

### **Phi-3.5-Instruct**

**CPU 가속 양자화 INT4 변환**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 가속 양자화 INT4 변환**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 터미널에서 환경 설정

```bash

mkdir models

cd models 

```

2. models 폴더에 microsoft/Phi-3.5-vision-instruct 다운로드  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 다음 파일들을 Phi-3.5-vision-instruct 폴더에 다운로드하세요

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. models 폴더에 이 파일을 다운로드하세요  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 터미널로 이동하여

    FP32로 ONNX 지원 변환 실행

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **참고：**

1. Model Builder는 현재 Phi-3.5-Instruct와 Phi-3.5-Vision 변환만 지원하며 Phi-3.5-MoE는 지원하지 않습니다.

2. ONNX 양자화 모델을 사용하려면 Generative AI extensions for onnxruntime SDK를 통해 사용할 수 있습니다.

3. 책임 있는 AI를 위해 모델 양자화 변환 후에는 더욱 효과적인 결과 테스트가 권장됩니다.

4. CPU INT4 모델을 양자화하면 Edge Device에 배포할 수 있어 더 나은 응용 시나리오가 가능하므로 Phi-3.5-Instruct의 INT4 양자화를 완료했습니다.

## **리소스**

1. Generative AI extensions for onnxruntime에 대해 자세히 알아보기  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub 저장소  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서는 해당 언어의 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 당사가 책임지지 않습니다.