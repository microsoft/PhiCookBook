<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-08T06:10:38+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ko"
}
-->
# **Apple MLX Framework를 이용한 Phi-3.5 양자화**

MLX는 Apple 실리콘에서 머신러닝 연구를 위해 Apple 머신러닝 연구진이 개발한 배열 프레임워크입니다.

MLX는 머신러닝 연구자들이 직접 설계한 프레임워크로, 사용자 친화적이면서도 모델을 효율적으로 학습하고 배포할 수 있도록 만들어졌습니다. 프레임워크 자체의 설계도 개념적으로 단순합니다. 연구자들이 MLX를 쉽게 확장하고 개선할 수 있도록 하여 새로운 아이디어를 빠르게 탐구하는 것을 목표로 합니다.

Apple 실리콘 장치에서는 MLX를 통해 LLM을 가속화할 수 있으며, 모델을 로컬에서 매우 편리하게 실행할 수 있습니다.

현재 Apple MLX Framework는 Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), 그리고 Phi-3.5-MoE(**Apple MLX Framework support**)의 양자화 변환을 지원합니다. 이제 직접 시도해 봅시다:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```


### **🤖 Apple MLX와 함께하는 Phi-3.5 샘플**

| Labs    | 소개 | 이동 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX 프레임워크와 함께 Phi-3.5 Instruct를 사용하는 방법 배우기   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX 프레임워크로 Phi-3.5 Vision을 이용해 이미지 분석하는 방법 배우기     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX 프레임워크와 함께 Phi-3.5 MoE를 사용하는 방법 배우기  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **자료**

1. Apple MLX Framework에 대해 알아보기 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 저장소 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 저장소 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 당사가 책임지지 않습니다.