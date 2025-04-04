<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-04T06:06:27+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ko"
}
-->
# **Apple MLX 프레임워크를 사용한 Phi-3.5 양자화**

MLX는 Apple 실리콘에서 기계 학습 연구를 위한 배열 프레임워크로, Apple 기계 학습 연구팀이 제공합니다.

MLX는 기계 학습 연구자들을 위해 설계되었으며, 사용자 친화적이면서도 모델을 효율적으로 학습하고 배포할 수 있도록 만들어졌습니다. 이 프레임워크의 설계 자체는 개념적으로 간단하며, 연구자들이 MLX를 확장하고 개선하여 새로운 아이디어를 빠르게 탐구할 수 있도록 돕는 것을 목표로 합니다.

Apple Silicon 기기에서 MLX를 통해 LLM을 가속화할 수 있으며, 모델을 로컬에서 매우 편리하게 실행할 수 있습니다.

현재 Apple MLX 프레임워크는 Phi-3.5-Instruct(**Apple MLX Framework 지원**), Phi-3.5-Vision(**MLX-VLM Framework 지원**), 그리고 Phi-3.5-MoE(**Apple MLX Framework 지원**)의 양자화 변환을 지원합니다. 이제 다음을 시도해 보세요:

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

| 연구실    | 소개 | 이동 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX 프레임워크를 사용하여 Phi-3.5 Instruct를 사용하는 방법을 배워보세요   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX 프레임워크를 사용하여 이미지를 분석하는 Phi-3.5 Vision 사용 방법을 배워보세요     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX 프레임워크를 사용하여 Phi-3.5 MoE를 사용하는 방법을 배워보세요  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **자료**

1. Apple MLX 프레임워크에 대해 알아보기 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 저장소 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 저장소 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역은 오류나 부정확성을 포함할 수 있습니다. 원본 문서의 원어를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생할 수 있는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.