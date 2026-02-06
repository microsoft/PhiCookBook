# **Phi-3 ஐ Lora உடன் Fine-tuning செய்யுதல்**

Microsoft இன் Phi-3 Mini மொழி மாதிரியை [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) பயன்படுத்தி தனிப்பயன் உரையாடல் வழிகாட்டல் தரவுத்தொகுப்பில் Fine-tuning செய்யுதல்.

LORA உரையாடல் புரிதல் மற்றும் பதில் உருவாக்கத்தை மேம்படுத்த உதவும்.

## Phi-3 Mini ஐ Fine-tuning செய்யும் வழிமுறைகள்:

**இறக்குமதி மற்றும் அமைப்பு**

loralib ஐ நிறுவுதல்

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

முதலில் datasets, transformers, peft, trl, மற்றும் torch போன்ற தேவையான நூலகங்களை இறக்குமதி செய்யுங்கள். பயிற்சி செயல்முறையை கண்காணிக்க பதிவு அமைப்பை அமைக்கவும்.

loralib இல் செயல்படுத்தப்பட்ட மாற்று அடுக்குகளை பயன்படுத்த சில அடுக்குகளை மாற்ற முடியும். தற்போது nn.Linear, nn.Embedding, மற்றும் nn.Conv2d மட்டுமே ஆதரிக்கப்படுகிறது. மேலும், கவனத்தின் qkv projection போன்ற செயல்பாடுகளில் ஒரு nn.Linear பல அடுக்குகளை பிரதிநிதித்துவப்படுத்தும் சந்தர்ப்பங்களில் MergedLinear ஐ ஆதரிக்கிறோம் (கூடுதல் குறிப்புகளைப் பார்க்கவும்).

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

பயிற்சி சுற்று தொடங்குவதற்கு முன், LoRA அளவுருக்களை மட்டுமே பயிற்சிக்க தகுதியானவையாக குறிக்கவும்.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

சோதனைப் புள்ளியைச் சேமிக்கும் போது, LoRA அளவுருக்களை மட்டுமே கொண்ட state_dict ஐ உருவாக்கவும்.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ஐ பயன்படுத்தி சோதனைப் புள்ளியை ஏற்றும்போது strict=False என அமைக்க உறுதிப்படுத்தவும்.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

இப்போது வழக்கமான பயிற்சி செயல்முறை தொடரலாம்.

**Hyperparameters**

training_config மற்றும் peft_config என இரண்டு அகராதிகளை வரையறுக்கவும். training_config பயிற்சிக்கான learning rate, batch size, மற்றும் logging அமைப்புகள் போன்ற hyperparameters ஐ உள்ளடக்கியது.

peft_config LoRA தொடர்பான rank, dropout, மற்றும் task type போன்ற அளவுருக்களை குறிப்பிடுகிறது.

**மாதிரி மற்றும் Tokenizer ஏற்றுதல்**

முன்பே பயிற்சி செய்யப்பட்ட Phi-3 மாதிரியின் பாதையை குறிப்பிடவும் (எ.கா., "microsoft/Phi-3-mini-4k-instruct"). மாதிரி அமைப்புகளை, cache பயன்பாடு, தரவின் வகை (mixed precision க்கான bfloat16), மற்றும் கவனத்தின் செயல்பாட்டை உள்ளடக்கவும்.

**பயிற்சி**

தனிப்பயன் உரையாடல் வழிகாட்டல் தரவுத்தொகுப்பைப் பயன்படுத்தி Phi-3 மாதிரியை Fine-tune செய்யுங்கள். peft_config இல் உள்ள LoRA அமைப்புகளை பயன்படுத்தி பயிற்சியை திறமையாகச் செய்யுங்கள். குறிப்பிட்ட logging உத்தியைப் பயன்படுத்தி பயிற்சி முன்னேற்றத்தை கண்காணிக்கவும்.

**மதிப்பீடு மற்றும் சேமித்தல்:** Fine-tuned மாதிரியை மதிப்பீடு செய்யுங்கள். பயிற்சியின் போது சோதனைப் புள்ளிகளை சேமித்து பின்னர் பயன்படுத்தவும்.

**மாதிரிகள்**
- [இந்த மாதிரி நோட்புக்குடன் மேலும் அறிக](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning மாதிரி உதாரணம்](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub Fine Tuning உதாரணம் - LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Card உதாரணம் - LORA Fine Tuning](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub Fine Tuning உதாரணம் - QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.