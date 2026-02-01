# **Phi-3 ಅನ್ನು Lora ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಮಾಡುವುದು**

Microsoft-ನ Phi-3 Mini ಭಾಷಾ ಮಾದರಿಯನ್ನು ಕಸ್ಟಮ್ ಚಾಟ್ ಸೂಚನೆ ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ [LoRA (ಕೀಳ್ವರ್ಗ ಹೊಂದಿಕರಣೆ)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಮಾಡುವುದು.

LoRA ಸಂಭಾಷಣಾತ್ಮಕ ಅರ್ಥಮಾಡಿಕೆ ಮತ್ತು ಪ್ರತಿಕ್ರিয়া ತಯಾರಿಯನ್ನು ಸುಧಾರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

## Phi-3 Mini ಅನ್ನು ಹೇಗೆ ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುವುದು — ಹಂತದ ಮೂಲಕ ಮಾರ್ಗದರ್ಶನ:

**ಆಮದುಗಳು ಮತ್ತು ಸೆಟ್‌ಅಪ್**

Installing loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ಅವಶ್ಯಕ ಲೈಬ್ರರಿಗಳು (ಉದಾಹರಣೆಗೆ datasets, transformers, peft, trl, ಮತ್ತು torch) ಅನ್ನು ಆಮದು ಮಾಡುವುದರಿಂದ ಪ್ರಾರಂಭಿಸಿ. ತರಬೇತಿ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಲು ಲಾಗಿಂಗ್ ಸೆಟ್ ಅಪ್ ಮಾಡಿ.

ನೀವು ಕೆಲವು ಲೇಯರ್‌ಗಳನ್ನು loralib ನಲ್ಲಿ ಅನುಷ್ಠಾನಗೊಳಿಸಲಾದ ಸಮಕಕ್ಷ compañents ಮೂಲಕ ಬದಲಾಯಿಸಿ ಅನುಕೂಲಗೊಳಿಸಬಹುದು. ಪ್ರಸ್ತುತ ನಾವು nn.Linear, nn.Embedding, ಮತ್ತು nn.Conv2d ಅನ್ನು ಮಾತ್ರ ಬೆಂಬಲಿಸುತ್ತೇವೆ. ಒಂದೇ nn.Linear ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಲೇಯರ್‌ಗಳನ್ನು ಪ್ರತಿನಿಧಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ, ಉದಾಹರಣೆಗೆ ಕೆಲವು perhatian qkv ಪ್ರೊಜೆಕ್ಷನ್ ಅನುಷ್ಠಾನಗಳಲ್ಲಿ (ಹೆಚ್ಚಿನ ವಿವರಗಳಿಗಾಗಿ Additional Notes ನೋಡಿ), ನಾವು MergedLinear ಅನ್ನು ಸಹ ಬೆಂಬಲಿಸುತ್ತೇವೆ.

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

ತರಬೇತಿ ಲೂಪ್ ಪ್ರಾರಂಭವಾಗುವುದಕ್ಕೆ ಮೊದಲು, ಕೇವಲ LoRA ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಮಾತ್ರ ತೆನ್‍ರೇಬಲ್ ಎಂದು ಗುರುತಿಸಿ.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ಚೆಕ್ಪಾಯಿಂಟ್ ಸಂರಕ್ಷಿಸುವಾಗ, ಕೇವಲ LoRA ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಮಾತ್ರ ಒಳಗೊಂಡಿರುವ state_dict ಅನ್ನು ರಚಿಸಿ.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ಬಳಸಿ ಚೆಕ್ಪಾಯಿಂಟ್ ಅನ್ನು ಲೋಡ್ ಮಾಡುತ್ತಿರುವಾಗ, strict=False ಅನ್ನು ಹೊಂದಿಸಲು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ಈಗ ತರಬೇತಿ ಸಹಜವಾಗಿ ಮುಂದುವರಿಯಬಹುದು.

**ಹೈಪರ್‌ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು**

ಎರಡೂ ಡಿಕ್ಷನರಿ‌ಗಳನ್ನು ನಿರ್ಧರಿಸಿ: training_config ಮತ್ತು peft_config. training_config ನಲ್ಲಿ ಕೌಶಲ್ಯ ಶ್ರೇಣಿ (learning rate), ಬ್ಯಾಚ್ ಗಾತ್ರ (batch size), ಮತ್ತು ಲಾಗಿಂಗ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಮುಂತಾದ ತರಬೇತಿ ಸಂಬಂಧಿ ಹೈಪರ್‌ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು ಸೇರಿವೆ.

peft_config ನಲ್ಲಿ rank, dropout, ಮತ್ತು task type వంటి LoRA-ಸಂಬಂಧಿತ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಲಾಗುತ್ತದೆ.

**ಮಾದರಿ ಮತ್ತು ಟೋಕನೈಝರ್ ಲೋಡಿಂಗ್**

ಪೂರ್ವ-ಪ್ರಶಿಕ್ಷಿತ Phi-3 ಮಾದರಿಯ ಪಥವನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಿ (ಉದಾ., "microsoft/Phi-3-mini-4k-instruct"). ಕ್ಯಾಶೆ ಬಳಕೆ, ಡೇಟಾ ಟೈಪ್ (ಮಿಶ್ರ ಪ್ರಿಸಿಷನ್‌ಗಾಗಿ bfloat16), ಮತ್ತು attention ಅನುಷ್ಠಾನ ಸೇರಿದಂತೆ ಮಾದರಿ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಸಂರಚಿಸಿ.

**ಪ್ರಶಿಕ್ಷಣ**

ಕಸ್ಟಮ್ ಚಾಟ್ ಸೂಚನೆ ಡೇಟಾಸೆಟ್ ಬಳಸಿ Phi-3 ಮಾದರಿಯನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಿ. ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಹೊಂದಿಕೊಳ್ಳಲು peft_config ನ LoRA ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಿ. ನಿಗದಿತ ಲಾಗಿಂಗ್ ಸ್ಟ್ರ್ಯಾಟಜಿ ಬಳಸಿ ತರಬೇತಿ ಪ್ರಗತಿಯನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ.
ಮೌಲ್ಯಮಾಪನ ಮತ್ತು ಉಳಿಸುವಿಕೆ: ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ.
ನಂತರ ಉಪಯೋಗಕ್ಕಾಗಿ ತರಬೇತಿ ಸಮಯದಲ್ಲಿ ಚೆಕ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಉಳಿಸಿ.

**ಉದಾಹರಣೆಗಳು**
- [ಈ ಮಾದರಿ ನೋಟ್ಬುಕ್ ಮೂಲಕ ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಮಾದರಿಯ ಉದಾಹರಣೆ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LoRA ಬಳಸಿ Hugging Face Hub ಮೇಲೆ ಫೈನ್ ಟೂನಿಂಗ್ ಉದಾಹರಣೆ](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face ಮಾದರಿ ಕಾರ್ಡ್ ಉದಾಹರಣೆ - LoRA ಫೈನ್ ಟೂನಿಂಗ್ ಮಾದರಿ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA ಬಳಸಿ Hugging Face Hub ಮೇಲೆ ಫೈನ್ ಟೂನಿಂಗ್ ಉದಾಹರಣೆ](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅನಿಖರತೆಗಳು ಇರಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿರಿಸಿ. ಮೂಲಭಾಷೆಯಲ್ಲಿರುವ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಭಾಷಾಂತರವನ್ನು ಬಳಸಿದರಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪಾದ ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->