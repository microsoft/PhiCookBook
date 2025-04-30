<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "700b9a537ce4426de5a7ccfa8e96e581",
  "translation_date": "2025-04-04T07:19:58+00:00",
  "source_file": "md\\03.FineTuning\\03.Inference\\MLX_Inference.md",
  "language_code": "ko"
}
-->
# **Apple MLX 프레임워크로 Phi-3 추론하기**

## **MLX 프레임워크란 무엇인가**

MLX는 Apple 실리콘에서 머신 러닝 연구를 위한 배열 프레임워크로, Apple 머신 러닝 연구팀에서 제공합니다.

MLX는 머신 러닝 연구자를 위해 설계된 프레임워크로, 사용자 친화적이면서도 모델을 효율적으로 학습하고 배포할 수 있도록 만들어졌습니다. 프레임워크의 디자인 자체도 개념적으로 간단하며, 연구자들이 MLX를 확장하고 개선하여 새로운 아이디어를 빠르게 탐구할 수 있도록 돕는 것을 목표로 합니다.

Apple Silicon 장치에서 MLX를 사용하면 LLM을 가속화할 수 있으며, 모델을 로컬에서 매우 간편하게 실행할 수 있습니다.

## **MLX로 Phi-3-mini 추론하기**

### **1. MLX 환경 설정하기**

1. Python 3.11.x 설치
2. MLX 라이브러리 설치


```bash

pip install mlx-lm

```

### **2. 터미널에서 MLX로 Phi-3-mini 실행하기**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

결과 (내 환경은 Apple M1 Max, 64GB)는 다음과 같습니다.

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ko.png)

### **3. MLX로 터미널에서 Phi-3-mini 양자화하기**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***참고：*** 모델은 mlx_lm.convert를 통해 양자화할 수 있으며, 기본 양자화는 INT4입니다. 이 예시는 Phi-3-mini를 INT4로 양자화하는 과정입니다.

모델은 mlx_lm.convert를 통해 양자화할 수 있으며, 기본 양자화는 INT4입니다. 이 예시는 Phi-3-mini를 INT4로 양자화하는 과정입니다. 양자화 후 모델은 기본 디렉터리 ./mlx_model에 저장됩니다.

양자화된 모델을 터미널에서 MLX로 테스트할 수 있습니다.


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

결과는 다음과 같습니다.

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ko.png)


### **4. Jupyter Notebook에서 MLX로 Phi-3-mini 실행하기**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ko.png)

***참고:*** 이 샘플을 읽어보세요 [이 링크를 클릭하세요](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **리소스**

1. Apple MLX 프레임워크에 대해 알아보기 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 저장소 [https://github.com/ml-explore](https://github.com/ml-explore)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 최대한 정확한 번역을 제공하려고 노력하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.