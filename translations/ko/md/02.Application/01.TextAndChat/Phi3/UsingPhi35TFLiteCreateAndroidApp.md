<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-08T05:42:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ko"
}
-->
# **Microsoft Phi-3.5 tflite를 사용해 Android 앱 만들기**

이 샘플은 Microsoft Phi-3.5 tflite 모델을 사용하는 Android 예제입니다.

## **📚 지식**

Android LLM Inference API는 Android 애플리케이션에서 대형 언어 모델(LLM)을 완전히 기기 내에서 실행할 수 있게 해주며, 이를 통해 텍스트 생성, 자연어 형태의 정보 검색, 문서 요약 등 다양한 작업을 수행할 수 있습니다. 이 작업은 여러 텍스트-투-텍스트 대형 언어 모델을 기본적으로 지원하여 최신 기기 내 생성 AI 모델을 Android 앱에 적용할 수 있습니다.

Googld AI Edge Torch는 PyTorch 모델을 .tflite 형식으로 변환하는 것을 지원하는 파이썬 라이브러리로, 변환된 모델은 TensorFlow Lite와 MediaPipe로 실행할 수 있습니다. 이를 통해 Android, iOS, IoT 기기에서 완전한 기기 내 모델 실행이 가능한 애플리케이션을 개발할 수 있습니다. AI Edge Torch는 광범위한 CPU 지원과 초기 GPU 및 NPU 지원을 제공하며, torch.export()를 기반으로 PyTorch와 밀접하게 통합되어 Core ATen 연산자도 잘 지원합니다.

## **🪬 가이드라인**

### **🔥 Microsoft Phi-3.5를 tflite로 변환 지원하기**

0. 이 샘플은 Android 14 이상에서 사용 가능합니다.

1. Python 3.10.12 설치

***추천:*** conda를 사용해 Python 환경을 설치하세요.

2. Ubuntu 20.04 / 22.04 (특히 [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)를 참고하세요)

***추천:*** Azure Linux VM 또는 타사 클라우드 VM을 이용해 환경을 구축하세요.

3. Linux bash에서 Python 라이브러리 설치

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face에서 Microsoft-3.5-Instruct 다운로드

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5를 tflite로 변환

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5를 Android Mediapipe 번들로 변환하기**

먼저 mediapipe를 설치하세요.

```bash

pip install mediapipe

```

이 코드는 [your notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)에서 실행하세요.

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 adb push로 모델을 Android 기기 경로에 복사하기**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android 코드 실행하기**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.ko.png)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서는 해당 언어의 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.