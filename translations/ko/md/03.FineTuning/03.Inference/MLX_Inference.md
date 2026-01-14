<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-17T10:04:55+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "ko"
}
-->
# **Apple MLX 프레임워크로 Phi-3 추론하기**

## **MLX 프레임워크란?**

MLX는 Apple 실리콘에서 머신러닝 연구를 위해 Apple 머신러닝 연구팀이 만든 배열 프레임워크입니다.

MLX는 머신러닝 연구자들이 직접 설계한 프레임워크로, 사용자 친화적이면서도 모델 학습과 배포에 효율적이도록 만들어졌습니다. 프레임워크 자체의 설계도 개념적으로 단순합니다. 연구자들이 MLX를 쉽게 확장하고 개선할 수 있도록 하여 새로운 아이디어를 빠르게 탐색할 수 있게 하는 것이 목표입니다.

Apple 실리콘 기기에서 MLX를 통해 LLM을 가속화할 수 있으며, 모델을 로컬에서 매우 편리하게 실행할 수 있습니다.

## **MLX로 Phi-3-mini 추론하기**

### **1. MLX 환경 설정하기**

1. Python 3.11.x
2. MLX 라이브러리 설치


```bash

pip install mlx-lm

```

### **2. 터미널에서 MLX로 Phi-3-mini 실행하기**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

결과 (내 환경은 Apple M1 Max, 64GB) 는 다음과 같습니다.

![Terminal](../../../../../translated_images/ko/01.5cf57df8f7407cf9.png)

### **3. 터미널에서 MLX로 Phi-3-mini 양자화하기**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** 모델은 mlx_lm.convert를 통해 양자화할 수 있으며, 기본 양자화 방식은 INT4입니다. 이 예제에서는 Phi-3-mini를 INT4로 양자화합니다.

모델은 mlx_lm.convert를 통해 양자화할 수 있으며, 기본 양자화 방식은 INT4입니다. 이 예제는 Phi-3-mini를 INT4로 양자화하는 방법을 보여줍니다. 양자화 후 모델은 기본 디렉토리인 ./mlx_model에 저장됩니다.

터미널에서 MLX로 양자화된 모델을 테스트할 수 있습니다.


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

결과는 다음과 같습니다.

![INT4](../../../../../translated_images/ko/02.7b188681a8eadbc1.png)


### **4. Jupyter Notebook에서 MLX로 Phi-3-mini 실행하기**


![Notebook](../../../../../translated_images/ko/03.b9705a3a5aaa89f9.png)

***Note:*** 이 샘플은 [여기 클릭](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)해서 확인하세요.


## **자료**

1. Apple MLX 프레임워크 알아보기 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 저장소 [https://github.com/ml-explore](https://github.com/ml-explore)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.