# **onnxruntime용 생성 AI 확장을 이용한 Phi 패밀리 양자화**

## **onnxruntime용 생성 AI 확장이란?**

이 확장은 ONNX Runtime([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai))과 함께 생성 AI를 실행할 수 있도록 도와줍니다. ONNX 모델을 위한 생성 AI 루프를 제공하며, 여기에는 ONNX Runtime을 통한 추론, 로짓 처리, 탐색 및 샘플링, KV 캐시 관리가 포함됩니다. 개발자는 고수준의 generate() 메서드를 호출하거나 모델의 각 이터레이션을 루프 내에서 실행하여 한 번에 한 토큰씩 생성하고 선택적으로 루프 내에서 생성 매개변수를 업데이트할 수 있습니다. 탐욕적/빔 탐색과 TopP, TopK 샘플링을 지원하여 토큰 시퀀스를 생성하며 반복 패널티 같은 내장 로짓 처리도 포함되어 있습니다. 또한 사용자 정의 점수 매기기를 쉽게 추가할 수 있습니다.

애플리케이션 수준에서는 onnxruntime용 생성 AI 확장을 사용해 C++/C#/Python으로 애플리케이션을 구축할 수 있고, 모델 수준에서는 미세 조정된 모델을 병합하고 관련 양자화 배포 작업을 수행할 수 있습니다.


## **onnxruntime용 생성 AI 확장을 이용한 Phi-3.5 양자화**

### **지원 모델**

onnxruntime용 생성 AI 확장은 Microsoft Phi, Google Gemma, Mistral, Meta LLaMA의 양자화 변환을 지원합니다。


### **onnxruntime용 생성 AI 확장의 모델 빌더**

모델 빌더는 ONNX Runtime의 generate() API와 함께 실행되는 최적화되고 양자화된 ONNX 모델을 만드는 작업을 대폭 가속화합니다.

모델 빌더를 통해 모델을 INT4, INT8, FP16, FP32로 양자화할 수 있고 CPU, CUDA, DirectML, Mobile 등 다양한 하드웨어 가속 방식을 결합할 수 있습니다.

모델 빌더를 사용하려면

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

설치 후, 터미널에서 모델 빌더 스크립트를 실행해 모델 포맷과 양자화 변환을 수행할 수 있습니다.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

관련 매개변수 이해하기

1. **model_name** Hugging Face의 모델명, 예를 들어 microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct 등이 있습니다. 모델 저장 경로일 수도 있습니다.

2. **path_to_output_folder** 양자화 변환 결과 저장 경로

3. **execution_provider** CPU, CUDA, DirectML 등 다양한 하드웨어 가속 지원

4. **cache_dir_to_save_hf_files** Hugging Face에서 모델을 다운로드해 로컬에 캐시하는 경로




***참고：*** <ul>onnxruntime용 생성 AI 확장은 아직 프리뷰 상태이지만 Microsoft Olive에 통합되어 있으며, Microsoft Olive를 통해 생성 AI 확장의 모델 빌더 기능도 호출할 수 있습니다.</ul>

## **모델 빌더를 사용해 Phi-3.5 양자화하는 방법**

현재 모델 빌더는 Phi-3.5 Instruct와 Phi-3.5-Vision ONNX 모델 양자화를 지원합니다.

### **Phi-3.5-Instruct**


**CPU 가속을 이용한 양자화 INT4 변환**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 가속을 이용한 양자화 INT4 변환**

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


4. 모델 폴더에 다음 파일 다운로드
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 터미널로 이동

    FP32 ONNX 지원으로 변환


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **참고：**

1. 모델 빌더는 현재 Phi-3.5-Instruct와 Phi-3.5-Vision 변환만 지원하며 Phi-3.5-MoE는 지원하지 않습니다.

2. ONNX 양자화 모델은 onnxruntime용 생성 AI 확장 SDK를 통해 사용할 수 있습니다.

3. 보다 책임감 있는 AI를 위해 모델 양자화 변환 후 더 효과적인 결과 테스트를 권장합니다.

4. CPU INT4 모델 양자화를 통해 Edge 디바이스에 배포할 수 있어 더 좋은 적용 사례가 있으며, 이에 따라 Phi-3.5-Instruct INT4 변환을 완료하였습니다.


## <strong>자료</strong>

1. onnxruntime용 생성 AI 확장에 대해 더 알아보기 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime용 생성 AI 확장 GitHub 저장소 [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->