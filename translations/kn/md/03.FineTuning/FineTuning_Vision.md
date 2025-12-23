<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-12-21T17:14:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "kn"
}
-->
# Phi-3.5-vision ಫೈನ್ಟ್ಯೂನಿಂಗ್ ರೆಸಿಪಿ

ಇದು huggingface ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು Phi-3.5-vision ಫೈನ್ಟ್ಯೂನಿಂಗ್‌ಗೆ ಅಧಿಕೃತ ಬೆಂಬಲವಾಗಿದೆ.
ದಯವಿಟ್ಟು ಕೆಳಗಿನ ಕಮಾಂಡ್‌ಗಳನ್ನು ಚಲಾವಣೆ ಮಾಡುವ ಮೊದಲೆ `cd` ಮಾಡಿ ಕೋಡ್ ಡೈರೆಕ್ಟರಿಯನ್ನು [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ಗೆ ತೆರಳಿರಿ.

## Installation

```bash
# ಹೊಸ conda ಪರಿಸರವನ್ನು ರಚಿಸಿ
conda create -n phi3v python=3.10
conda activate phi3v

# pytorch ಅನ್ನು ಸ್ಥಾಪಿಸಿ
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# ಉದಾಹರಣೆ ಕೋಡ್ ಅನ್ನು ಚಲಿಸಲು ಬೇಕಾಗುವ ಇತರ ಗ್ರಂಥಾಲಯಗಳು
pip install -r requirements.txt

# (ಐಚ್ಛಿಕ) flash attention -- Ampere+ GPU ಗಳು (ಉದಾಹರಣೆಗೆ, A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (ಐಚ್ಛಿಕ) QLoRA -- Turing+ GPU ಗಳು (ಉದಾಹರಣೆಗೆ, RTX 8000)
pip install bitsandbytes==0.43.1
```

## ತ್ವರಿತ ಪ್ರಾರಂಭ

ನಾವು ಎರಡು ಉದಾಹರಣೆ ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ನೀಡಿದ್ದೇವೆ, ಒಂದು DocVQA ಗಾಗಿ ಮತ್ತು ಮತ್ತೊಂದು hateful meme ವರ್ಗೀಕರಣಕ್ಕಾಗಿ.

ಕನಿಷ್ಠ ಹಾರ್ಡ್‌ವೇರ್ 4x RTX8000 (ಪ್ರತಿ GPU ಗೆ 48GB RAM) ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಲಾಗಿದೆ

```bash
# DocVQA ಯ ಮಿನಿ-ಟ್ರೇನ್ ವಿಭಾಗದ ಮೇಲೆ ಇರುವ ಕನಿಷ್ಠ ಸ್ಕ್ರಿಪ್ಟ್
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ಈಗ ಅಧಿಕೃತವಾಗಿ ಬಹು-ಚಿತ್ರ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. NLVR2 ಅನ್ನು ಫೈನ್ಟ್ಯೂನ್ ಮಾಡುವ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ಬಳಕೆದಾರ ಮಾರ್ಗದರ್ಶಿ

ಹಾರ್ಡ್‌ವೇರ್‌ ಅವಲಂಬಿಸಿ, ಬಳಕೆದಾರರು ವಿಭಿನ್ನ ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಯುಕ್ತಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಬಹುದು. ನಾವು
ಪೂರ್ಣ-ಫೈನ್ಟ್ಯೂನಿಂಗ್ (Deepspeed Zero-2 ಜೊತೆಗೆ) ಅನ್ನು ನೆರವೇರಿಸುತ್ತೇವೆ, ಐಚ್ಛಿಕವಾಗಿ ದೃಷ್ಟಿ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಫ್ರೋಜನ್ ಮಾಡಬಹುದಾಗಿದೆ, ಮತ್ತು LoRA (4bit QLoRA ಸೇರಿದಂತೆ).
ಸಾಮಾನ್ಯವಾಗಿ, ಸಾಧ್ಯವಾದರೆ flash attention ಮತ್ತು bf16 ಜೊತೆ ಪೂರ್ಣ ಫೈನ್‌ಟ್ಯೂನಿಂಗ್ ಬಳಸುವಂತೆ ನಾವು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ.

### ನಿಮ್ಮ ಕಸ್ಟಮ್ ಡೇಟಾಸೆಟ್ ಅನ್ನು ಅಗತ್ಯವಿರುವ ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವ ಮಾರ್ಗದರ್ಶಿ

ನಾವು ಕನಿಷ್ಠ ವಿಡಿಯೋ ವರ್ಗೀಕರಣ ಡೇಟಾಸೆಟ್ (UCF-101 ನ ಉಪಸೆಟ್) ಅನ್ನು end-to-end ಉದಾಹರಣೆಯಾಗಿ ಬಳಸಿಕೊಂಡು, ನಿಮ್ಮ ಕಸ್ಟಮ್ ಡೇಟಾಸೆಟ್ ಅನ್ನು ಅಗತ್ಯವಿರುವ ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಹೇಗೆ ಪರಿವರ್ತಿಸಲು ಮತ್ತು ಅದರ ಮೇಲೆ Phi-3.5-vision ಅನ್ನು ಹೇಗೆ ಫೈನ್ಟ್ಯೂನ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತೇವೆ.

```bash
# ಡೇಟಾ ಪರಿವರ್ತಿಸಿ
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# ಪ್ರಸಿಕ್ಷಣ
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ಪರಿವರ್ತಿತ ಡೇಟಾ ಈ ರೀತಿ ಕಾಣಿಸುತ್ತದೆ:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

`jsonl` ಅ್ಯಾನೋಟೇಷನ್‌ಗಾಗಿ, ಪ್ರತಿ ಸಾಲು ಕೆಳಗಿನಂತೆ ಒಂದು ಡಿಕ್ಷನರಿ ಆಗಿರಬೇಕು:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ಗಮನಿಸಿ `conversations` ಒಂದು ಪಟ್ಟಿಯಾಗಿದೆ, ಆದ್ದರಿಂದ ಬಹು-ತಿರುವಿ ಸಂಭಾಷಣೆ ಹಾಗಿನ ಡೇಟಾ ಲಭ್ಯವಿದ್ದರೆ ಬೆಂಬಲಿಸಬಹುದು.

## Azure GPU ಕ್ವೋಟಾ ವಿನಂತಿಸುವುದು

### ಪೂರ್ವಾಪೇಕ್ಷತೆಗಳು

Contributor ಪಾತ್ರ (ಅಥವಾ Contributor ಪ್ರವೇಶವನ್ನು ಒಳಗೊಂಡ अन्य ಪಾತ್ರ) ಇರುವ Azure ಖಾತೆ.

ನಿಮ್ಮ ಬಳಿ Azure ಖಾತೆ yokkAgilla ಎನಿಸಿದ್ದರೆ, [ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಿ](https://azure.microsoft.com).

### ಕ್ವೋಟಾ ಹೆಚ್ಚಾವಣೆಗೆ ವಿನಂತಿ ಸಲ್ಲಿಸುವುದು

ನೀವು My quotas ನಿಂದ ನೇರವಾಗಿ ಕ್ವೋಟಾ ಹೆಚ್ಚಾವಣೆಯ ವಿನಂತಿಯನ್ನು ಸಲ್ಲಿಸಬಹುದು. ಕ್ವೋಟಾ ಒಂದಕ್ಕೆ ಹೆಚ್ಚುವರಿ ವಿನಂತಿ ಮಾಡಲು ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ. ಈ ಉದಾಹರಣೆಗೆ, ನಿಮ್ಮ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್‌ನಲ್ಲಿ ಯಾವುದೇ adjustable quota ಅನ್ನು ಆಯ್ಕೆಮಾಡಬಹುದು.

[Azure portal](https://portal.azure.com) ಗೆ ಸೈನ್ ಇನ್ ಮಾಡಿ.

ಶೋಧನಾ ಬಾಕ್ಸ್‌ಗೆ "quotas" ಅನ್ನು ನಮೂದಿಸಿ, ನಂತರ Quotas ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.
![ಕ್ವೋಟಾ](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview ಪುಟದಲ್ಲಿ, Compute ಅಥವಾ AML ಹೆಸರಿನಂತಹ ಒಬ್ಬ ಪ್ರೊವೈಡರ್ ಆಯ್ಕೆಮಾಡಿ.

**ಗಮನಿಸಿ** Compute ಹೊರತಾಗಿರುವ ಎಲ್ಲಾ ಪ್ರೊವೈಡರ್‌ಗಳಿಗಾಗಿ, ಕೆಳಗೆ ವಿವರಿಸಿರುವ Adjustable ಕಾಲಮ್ ಬದಲು Request increase ಕಾಲಮ್ ಕಾಣಿಸಬಹುದು. ಅಲ್ಲಿ, ನೀವು ನಿರ್ದಿಷ್ಟ ಕ್ವೋಟಾ ಗಾಗಿ ಹೆಚ್ಚುವರಿ ವಿನಂತಿ ಮಾಡಬಹುದು, ಅಥವಾ ಹೆಚ್ಚುವರಿ ಪಡೆಯಲು ಸಪೋರ್ಟ್ ರಿಕ್ವೆಸ್ಟ್ ರಚಿಸಬಹುದು.

My quotas ಪುಟದಲ್ಲಿ, Quota name ಅಡಿ, ನೀವು ಹೆಚ್ಚಿಸಬೇಕೆಂದು ಮೀಸಲಿಟ್ಟಿರುವ ಕ್ವೋಟಾ ಆಯ್ಕೆಮಾಡಿ. ಈ ಕ್ವೋಟಾ ನಿಯಮಕ್ಕೆ Adjustable ಕಾಲಮ್ ಹೌದು ಎಂದು ತೋರಿಸುತ್ತಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿ.

ಪುಟದ ಮೇಲ್ಭಾಗದ ಸಮೀಪದಲ್ಲಿ, New Quota Request ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ, ನಂತರ Enter a new limit ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.

![ಕ್ವೋಟಾ ಹೆಚ್ಚಿಸಿ](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ಪೇನ್‌ನಲ್ಲಿ, ನಿಮ್ಮ ಹೊಸ ಕ್ವೋಟಾ ಮಿತಿಕ್ಕಾಗಿ ಸಂಖ್ಯಾತ್ಮಕ ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ, ನಂತರ Submit ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.

ನಿಮ್ಮ ವಿನಂತಿಯನ್ನು ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ, ಮತ್ತು ವಿನಂತಿ ಪೂರೈಸಬಹುದೇ ಎಂದು ನಿಮಗೆ ತಿಳಿಸಲಾಗುತ್ತದೆ. ಇದು ಸಾಮಾನ್ಯವಾಗಿ ಕೆಲವು ನಿಮಿಷಗಳಲ್ಲಿ ಸಂಭವಿಸುತ್ತದೆ.

ನಿಮ್ಮ ವಿನಂತಿ ಪೂರೈಸದಿದ್ದರೆ, ಸಪೋರ್ಟ್ ರಿಕ್ವೆಸ್ಟ್ ರಚಿಸಲು ಒಂದು ಲಿಂಕ್ ಕಾಣಿಸುತ್ತದೆ. ನೀವು ಈ ಲಿಂಕ್ ಅನ್ನು ಬಳಸಿದಾಗ, ಒಂದು ಸಪೋರ್ಟ್ ಎಂಜಿನಿಯರ್ ನಿಮ್ಮ ಹೆಚ್ಚುವರಿ ವಿನಂತಿಗೆ ಸಹಾಯ ಮಾಡುತ್ತಾರೆ.

## Azure Compute GPU ಯಂತ್ರ SKU ಶಿಫಾರಸುಗಳು

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ಕೆಳಗಿನವು ಕೆಲವು ಉದಾಹರಣೆಗಳಾಗಿವೆ:

### ನೀವು A100 ಅಥವಾ H100 GPUs ಹೊಂದಿದ್ದರೆ

ಪೂರ್ಣ ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಸಾಮಾನ್ಯವಾಗಿ ಉತ್ತಮ ಪ್ರದರ್ಶನ ನೀಡುತ್ತದೆ. hateful memes ವರ್ಗೀಕರಣದ ಮೇಲೆ Phi-3-V ಅನ್ನು ಫೈನ್ಟ್ಯೂನ್ ಮಾಡಲು ನೀವು ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಬಹುದು.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### ನೀವು Standard_ND40rs_v2 8x V100-32GB GPUs ಹೊಂದಿದ್ದರೆ

hateful memes ವರ್ಗೀಕರಣದ ಮೇಲೆ Phi-3-V ಅನ್ನು ಪೂರ್ಣವಾಗಿ ಫೈನ್ಟ್ಯೂನ್ ಮಾಡುವುದು ಇನ್ನೂ ಸಾಧ್ಯವಾಗಿದೆ. ಆದಾಗ್ಯೂ, flash attention ಬೆಂಬಲದ ಕೊರತೆಯ ಕಾರಣ A100 ಅಥವಾ H100 GPU ಗಳಿಗಿಂತ ಬಹಳ ಕಡಿಮೆ throughput ನಿರೀಕ್ಷಿಸಬೇಕು.
bf16 ಬೆಂಬಲದ ಕೊರತೆಯ ಕಾರಣದಿಂದ ನಿಖರತೆಯೂ ಪ್ರಭಾವಿತವಾಗಬಹುದು (fp16 ಮಿಶ್ರ-ಪ್ರಿಸಿಷನ್ ತರಬೇತಿ ಬದಲಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### ನಿಮ್ಮಿಗೆ ಡೇಟಾ ಸೆಂಟರ್ GPU ಗಳಿಗೆ ಪ್ರವೇಶವಿಲ್ಲದಿದ್ದರೆ
LoRA ನಿಮ್ಮ ಏಕೈಕ ಆಯ್ಕೆ ಆಗಿರಬಹುದು. hateful memes ವರ್ಗೀಕರಣದ ಮೇಲೆ Phi-3-V ಅನ್ನು ಫೈನ್ಟ್ಯೂನ್ ಮಾಡಲು ನೀವು ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಬಹುದು.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU ಗಾಗಿ, QLoRA ಬೆಂಬಲಿಸಲಾಗುತ್ತದೆ

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ಶಿಫಾರಸು ಮಾಡಿದ ಹೈಪರ್‌ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು ಮತ್ತು ನಿರೀಕ್ಷಿತ ನಿಖರತೆ
### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### ಗಮನಿಸಿ
ಕೆಳಗಿನ DocVQA ಮತ್ತು Hateful memes ಫಲಿತಾಂಶಗಳು ಹಿಂದಿನ ಸಂಚಿಕೆ (Phi-3-vision) ಆಧಾರಿತವಾಗಿವೆ.
Phi-3.5-vision ಹಾಗೂ ಹೊಸ ಫಲಿತಾಂಶಗಳನ್ನು ಶೀಘ್ರದಲ್ಲೇ ಅಪ್ಡೇಟ್ ಮಾಡಲಾಗುವುದು.

### DocVQA (ಗಮನಿಸಿ: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (ಗಮನಿಸಿ: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## ವೇಗದ ಬenchmarking (ಗಮನಿಸಿ: Phi-3-vision)

Phi-3.5-vision ಜೊತೆಗೆ ಹೊಸ benchmarking ಫಲಿತಾಂಶಗಳನ್ನು ಶೀಘ್ರದಲ್ಲೇ ಅಪ್ಡೇಟ್ ಮಾಡಲಾಗುತ್ತದೆ.

ವೇಗದ benchmarking ಅನ್ನು DocVQA ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ ನಡೆಸಲಾಗಿದೆ. ಈ ಡೇಟಾಸೆಟ್‌ನ ಸರಾಸರಿ ಕ್ರಮದ ಉದ್ದ 2443.23 ಟೋಕನ್ಗಳು (ಚಿತ್ರ ಮಾದರಿಗಾಗಿ `num_crops=16` ಬಳಸಿ) ಆಗಿದೆ.

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frozen image model | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## ತಿಳಿದಿರುವ ಸಮಸ್ಯೆಗಳು

- fp16 ಜೊತೆಗೆ flash attention ರನ್ ಮಾಡಲಾಗುವುದಿಲ್ಲ (ಉಪಲಭ್ಯವಿದ್ದರೆ bf16 ಅನ್ನು ಯಾವತ್ತೂ ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ, ಮತ್ತು flash attention‌ಗೆ ಬೆಂಬಲ ನೀಡುವ ಎಲ್ಲಾ GPU ಗಳು bf16 ಸಹ ಬೆಂಬಲಿಸುತ್ತವೆ).
- ಮಧ್ಯವರ್ತಿ ಚೆಕ್ಫ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಉಳಿಸಿ ತರಬೇತಿಯನ್ನು ಪುನರಾರಂಭಿಸುವುದನ್ನು ಇನ್ನೂ ಬೆಂಬಲಿಸದು.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯ ಮೇಲೆ ಪ್ರಯತ್ನಿಸಿದರೇ ಕೂಡ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದೆಂದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಾಖಲೆ ಅನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪಾದ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ದುರ್ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->