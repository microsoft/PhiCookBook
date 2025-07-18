<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:29:18+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ko"
}
-->
# **LoRA를 이용한 Phi-3 미니 파인튜닝**

Microsoft의 Phi-3 Mini 언어 모델을 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)를 사용해 맞춤형 채팅 지침 데이터셋으로 파인튜닝하는 방법입니다.

LoRA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움을 줍니다.

## Phi-3 Mini 파인튜닝 단계별 가이드:

**임포트 및 설정**

loralib 설치

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl, torch 등 필요한 라이브러리를 임포트하는 것부터 시작하세요.  
학습 과정을 추적하기 위해 로깅을 설정합니다.

일부 레이어를 loralib로 구현된 대응 레이어로 교체하여 적응시킬 수 있습니다. 현재는 nn.Linear, nn.Embedding, nn.Conv2d만 지원합니다. 또한, 단일 nn.Linear가 여러 레이어를 대표하는 경우(예: 일부 어텐션 qkv 프로젝션 구현)에는 MergedLinear도 지원합니다(추가 참고 사항 참조).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

학습 루프가 시작되기 전에 LoRA 파라미터만 학습 가능하도록 표시하세요.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

체크포인트를 저장할 때는 LoRA 파라미터만 포함하는 state_dict를 생성합니다.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict로 체크포인트를 불러올 때는 strict=False로 설정하는 것을 잊지 마세요.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

이제 평소처럼 학습을 진행할 수 있습니다.

**하이퍼파라미터**

training_config와 peft_config 두 개의 딕셔너리를 정의합니다.  
training_config에는 학습률, 배치 크기, 로깅 설정 등 학습 관련 하이퍼파라미터가 포함됩니다.

peft_config는 rank, dropout, 작업 유형 등 LoRA 관련 파라미터를 지정합니다.

**모델 및 토크나이저 로딩**

사전학습된 Phi-3 모델 경로(예: "microsoft/Phi-3-mini-4k-instruct")를 지정합니다.  
캐시 사용, 데이터 타입(bfloat16 혼합 정밀도), 어텐션 구현 방식 등 모델 설정을 구성합니다.

**학습**

맞춤형 채팅 지침 데이터셋을 사용해 Phi-3 모델을 파인튜닝합니다.  
효율적인 적응을 위해 peft_config의 LoRA 설정을 활용하세요.  
지정한 로깅 전략으로 학습 진행 상황을 모니터링합니다.  
평가 및 저장: 파인튜닝된 모델을 평가하고, 학습 중간에 체크포인트를 저장해 나중에 사용할 수 있습니다.

**샘플**
- [이 샘플 노트북으로 더 알아보기](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 파인튜닝 샘플 예제](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub에서 LoRA로 파인튜닝하는 예제](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 모델 카드 예제 - LoRA 파인튜닝 샘플](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub에서 QLORA로 파인튜닝하는 예제](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.