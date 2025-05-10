<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:44:44+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "pa"
}
-->
# **Lora ਨਾਲ Phi-3 ਦਾ ਫਾਈਨ-ਟਿਊਨਿੰਗ**

Microsoft ਦੇ Phi-3 Mini ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਕਸਟਮ ਚੈਟ ਨਿਰਦੇਸ਼ਨ ਡੇਟਾਸੈਟ 'ਤੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ।

LORA ਗੱਲਬਾਤ ਦੀ ਸਮਝ ਅਤੇ ਜਵਾਬ ਬਣਾਉਣ ਵਿੱਚ ਸੁਧਾਰ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ।

## Phi-3 Mini ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਲਈ ਕਦਮ-ਬਾਈ-ਕਦਮ ਗਾਈਡ:

**ਇੰਪੋਰਟ ਅਤੇ ਸੈਟਅਪ**

loralib ਇੰਸਟਾਲ ਕਰਨਾ

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਜਿਵੇਂ datasets, transformers, peft, trl, ਅਤੇ torch ਨੂੰ ਇੰਪੋਰਟ ਕਰਕੇ ਸ਼ੁਰੂ ਕਰੋ।  
ਟ੍ਰੇਨਿੰਗ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਟ੍ਰੈਕ ਕਰਨ ਲਈ ਲੋਗਿੰਗ ਸੈਟਅਪ ਕਰੋ।

ਤੁਸੀਂ ਕੁਝ ਲੇਅਰਾਂ ਨੂੰ loralib ਵਿੱਚ ਬਣਾਏ ਗਏ ਸਮਾਨ ਲੇਅਰਾਂ ਨਾਲ ਬਦਲ ਕੇ ਅਡੈਪਟ ਕਰ ਸਕਦੇ ਹੋ। ਇਸ ਸਮੇਂ ਸਾਡੀ ਸਹਾਇਤਾ ਸਿਰਫ nn.Linear, nn.Embedding, ਅਤੇ nn.Conv2d ਲਈ ਹੈ। ਅਸੀਂ ਇੱਕ MergedLinear ਵੀ ਸਹਾਇਤਾ ਕਰਦੇ ਹਾਂ ਜਿੱਥੇ ਇੱਕ nn.Linear ਕਈ ਲੇਅਰਾਂ ਦੀ ਨੁਮਾਇੰਦਗੀ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਕੁਝ attention qkv ਪ੍ਰੋਜੈਕਸ਼ਨ ਦੇ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਵਿੱਚ (ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ Additional Notes ਵੇਖੋ)।

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

ਟ੍ਰੇਨਿੰਗ ਲੂਪ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ, ਸਿਰਫ LoRA ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨਯੋਗ ਮਾਰਕ ਕਰੋ।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ਚੈਕਪੌਇੰਟ ਸੇਵ ਕਰਦੇ ਸਮੇਂ, ਸਿਰਫ LoRA ਪੈਰਾਮੀਟਰਾਂ ਵਾਲਾ state_dict ਬਣਾਓ।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ਵਰਤਦੇ ਸਮੇਂ strict=False ਸੈੱਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ਹੁਣ ਟ੍ਰੇਨਿੰਗ ਆਮ ਤਰ੍ਹਾਂ ਜਾਰੀ ਰੱਖੀ ਜਾ ਸਕਦੀ ਹੈ।

**ਹਾਈਪਰਪੈਰਾਮੀਟਰ**

ਦੋ ਡਿਕਸ਼ਨਰੀਆਂ ਬਣਾਓ: training_config ਅਤੇ peft_config। training_config ਵਿੱਚ ਟ੍ਰੇਨਿੰਗ ਲਈ ਹਾਈਪਰਪੈਰਾਮੀਟਰ ਹਨ, ਜਿਵੇਂ ਕਿ ਲਰਨਿੰਗ ਰੇਟ, ਬੈਚ ਸਾਈਜ਼, ਅਤੇ ਲੋਗਿੰਗ ਸੈਟਿੰਗਜ਼।

peft_config ਵਿੱਚ LoRA ਨਾਲ ਜੁੜੇ ਪੈਰਾਮੀਟਰ ਹਨ, ਜਿਵੇਂ rank, dropout, ਅਤੇ ਟਾਸਕ ਟਾਈਪ।

**ਮਾਡਲ ਅਤੇ ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰਨਾ**

ਪ੍ਰੀ-ਟ੍ਰੇਨ ਕੀਤੇ Phi-3 ਮਾਡਲ ਦਾ ਪਾਥ ਦਿਓ (ਜਿਵੇਂ "microsoft/Phi-3-mini-4k-instruct")। ਮਾਡਲ ਸੈਟਿੰਗਜ਼ ਕਨਫਿਗਰ ਕਰੋ, ਜਿਸ ਵਿੱਚ cache ਦੀ ਵਰਤੋਂ, ਡੇਟਾ ਟਾਈਪ (ਮਿਕਸਡ ਪ੍ਰਿਸੀਜ਼ਨ ਲਈ bfloat16), ਅਤੇ attention ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਸ਼ਾਮਿਲ ਹਨ।

**ਟ੍ਰੇਨਿੰਗ**

ਕਸਟਮ ਚੈਟ ਨਿਰਦੇਸ਼ਨ ਡੇਟਾਸੈਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ। ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਅਡੈਪਟੇਸ਼ਨ ਲਈ peft_config ਤੋਂ LoRA ਸੈਟਿੰਗਜ਼ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਟ੍ਰੇਨਿੰਗ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਨਿਰਧਾਰਿਤ ਲੋਗਿੰਗ ਰਣਨੀਤੀ ਨਾਲ ਮਾਨੀਟਰ ਕਰੋ।  
ਮੂਲਾਂਕਣ ਅਤੇ ਸੇਵਿੰਗ: ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਮੁਲਾਂਕਣ ਕਰੋ।  
ਟ੍ਰੇਨਿੰਗ ਦੌਰਾਨ ਚੈਕਪੌਇੰਟ ਸੇਵ ਕਰੋ ਤਾਂ ਜੋ ਬਾਅਦ ਵਿੱਚ ਵਰਤਿਆ ਜਾ ਸਕੇ।

**ਨਮੂਨੇ**  
- [ਇਸ ਸੈਂਪਲ ਨੋਟਬੁੱਕ ਨਾਲ ਹੋਰ ਸਿੱਖੋ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python FineTuning ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [LORA ਨਾਲ Hugging Face Hub Fine Tuning ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face ਮਾਡਲ ਕਾਰਡ ਦਾ ਉਦਾਹਰਨ - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [QLORA ਨਾਲ Hugging Face Hub Fine Tuning ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।