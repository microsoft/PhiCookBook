<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98eb289883c5e181a74e72a59e1ddc6d",
  "translation_date": "2025-04-04T07:01:08+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "ko"
}
-->
# **Lora를 활용한 Phi-3 미니 모델 미세 조정**

[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)을 사용하여 Microsoft의 Phi-3 Mini 언어 모델을 사용자 지정 채팅 지침 데이터셋으로 미세 조정합니다.

LoRA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움을 줍니다.

## Phi-3 Mini를 미세 조정하는 단계별 가이드:

**임포트 및 설정**

loralib 설치

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

필요한 라이브러리(datasets, transformers, peft, trl, torch 등)를 임포트하는 것으로 시작합니다.  
훈련 과정을 추적하기 위해 로깅을 설정합니다.

일부 레이어를 loralib에서 구현된 대응 레이어로 대체하여 적응시킬 수 있습니다. 현재 nn.Linear, nn.Embedding, nn.Conv2d만 지원하며, 추가적으로 MergedLinear도 지원합니다. MergedLinear는 단일 nn.Linear가 여러 레이어를 나타내는 경우(예: attention qkv projection 구현의 일부) 사용됩니다. 자세한 내용은 추가 참고 사항을 확인하세요.

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

loralib를 임포트합니다.

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

훈련 루프가 시작되기 전에 LoRA 파라미터만 학습 가능으로 표시합니다.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

체크포인트를 저장할 때, LoRA 파라미터만 포함된 state_dict를 생성합니다.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict를 사용하여 체크포인트를 로드할 때는 strict=False로 설정하세요.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

이제 일반적인 훈련을 진행할 수 있습니다.

**하이퍼파라미터**

training_config와 peft_config 두 개의 딕셔너리를 정의합니다.  
training_config에는 학습률, 배치 크기, 로깅 설정 등 훈련에 필요한 하이퍼파라미터가 포함됩니다.

peft_config는 rank, dropout, task type 등 LoRA 관련 파라미터를 지정합니다.

**모델 및 토크나이저 로딩**

사전 훈련된 Phi-3 모델 경로를 지정합니다(예: "microsoft/Phi-3-mini-4k-instruct").  
캐시 사용, 데이터 타입(bfloat16을 활용한 혼합 정밀도), 어텐션 구현 등 모델 설정을 구성합니다.

**훈련**

사용자 지정 채팅 지침 데이터셋을 사용하여 Phi-3 모델을 미세 조정합니다.  
peft_config의 LoRA 설정을 활용하여 효율적으로 적응합니다.  
지정된 로깅 전략을 통해 훈련 진행 상황을 모니터링합니다.

**평가 및 저장**

미세 조정된 모델을 평가합니다.  
훈련 중 체크포인트를 저장하여 나중에 사용할 수 있도록 합니다.

**샘플**
- [이 샘플 노트북에서 더 알아보기](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 미세 조정 샘플 예제](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub에서 LORA를 활용한 미세 조정 예제](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 모델 카드 - LORA 미세 조정 샘플 예제](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub에서 QLORA를 활용한 미세 조정 예제](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 포함될 수 있습니다. 원본 문서의 원어 버전이 신뢰할 수 있는 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.