# **ਲੋਰਾ ਨਾਲ Phi-3 ਦਾ ਫਾਈਨ-ਟਿਊਨਿੰਗ**

ਮਾਈਕ੍ਰੋਸਾਫਟ ਦੇ Phi-3 ਮਿਨੀ ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਕਸਟਮ ਚੈਟ ਇੰਸਟ੍ਰਕਸ਼ਨ ਡੇਟਾਸੈੱਟ 'ਤੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ।

ਲੋਰਾ ਗੱਲਬਾਤ ਦੀ ਸਮਝ ਅਤੇ ਜਵਾਬ ਬਣਾਉਣ ਵਿੱਚ ਸੁਧਾਰ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ।

## Phi-3 ਮਿਨੀ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ:

**ਇੰਪੋਰਟ ਅਤੇ ਸੈਟਅਪ**

ਲੋਰਾਲਿਬ ਇੰਸਟਾਲ ਕਰਨਾ

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਜਿਵੇਂ datasets, transformers, peft, trl, ਅਤੇ torch ਨੂੰ ਇੰਪੋਰਟ ਕਰਕੇ ਸ਼ੁਰੂ ਕਰੋ।  
ਟ੍ਰੇਨਿੰਗ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਟ੍ਰੈਕ ਕਰਨ ਲਈ ਲੌਗਿੰਗ ਸੈਟਅਪ ਕਰੋ।

ਤੁਸੀਂ ਕੁਝ ਲੇਅਰਾਂ ਨੂੰ ਲੋਰਾਲਿਬ ਵਿੱਚ ਬਣਾਏ ਗਏ ਸਮਾਨ ਲੇਅਰਾਂ ਨਾਲ ਬਦਲ ਕੇ ਅਡੈਪਟ ਕਰ ਸਕਦੇ ਹੋ। ਅਸੀਂ ਇਸ ਸਮੇਂ ਸਿਰਫ nn.Linear, nn.Embedding, ਅਤੇ nn.Conv2d ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਾਂ। ਕੁਝ ਕੇਸਾਂ ਵਿੱਚ ਜਿੱਥੇ ਇੱਕ nn.Linear ਇੱਕ ਤੋਂ ਵੱਧ ਲੇਅਰਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਕੁਝ attention qkv ਪ੍ਰੋਜੈਕਸ਼ਨ ਦੇ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ (ਵਧੂ ਨੋਟਸ ਵੇਖੋ), ਅਸੀਂ MergedLinear ਨੂੰ ਵੀ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਾਂ।

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

ਟ੍ਰੇਨਿੰਗ ਲੂਪ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ, ਸਿਰਫ਼ LoRA ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਯੋਗ ਮਾਰਕ ਕਰੋ।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ਚੈਕਪੌਇੰਟ ਸੇਵ ਕਰਦੇ ਸਮੇਂ, ਇੱਕ state_dict ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਸਿਰਫ਼ LoRA ਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਹੋਣ।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ਵਰਤ ਕੇ ਚੈਕਪੌਇੰਟ ਲੋਡ ਕਰਦੇ ਸਮੇਂ, strict=False ਸੈੱਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ਹੁਣ ਟ੍ਰੇਨਿੰਗ ਆਮ ਤਰ੍ਹਾਂ ਜਾਰੀ ਰਹਿ ਸਕਦੀ ਹੈ।

**ਹਾਈਪਰਪੈਰਾਮੀਟਰ**

ਦੋ ਡਿਕਸ਼ਨਰੀਜ਼ define ਕਰੋ: training_config ਅਤੇ peft_config। training_config ਵਿੱਚ ਟ੍ਰੇਨਿੰਗ ਲਈ ਹਾਈਪਰਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਹਨ, ਜਿਵੇਂ ਲਰਨਿੰਗ ਰੇਟ, ਬੈਚ ਸਾਈਜ਼, ਅਤੇ ਲੌਗਿੰਗ ਸੈਟਿੰਗਜ਼।

peft_config ਵਿੱਚ LoRA ਨਾਲ ਸੰਬੰਧਿਤ ਪੈਰਾਮੀਟਰ ਜਿਵੇਂ rank, dropout, ਅਤੇ ਟਾਸਕ ਟਾਈਪ ਦਰਜ ਹਨ।

**ਮਾਡਲ ਅਤੇ ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰਨਾ**

ਪ੍ਰੀ-ਟ੍ਰੇਨਡ Phi-3 ਮਾਡਲ ਦਾ ਪਾਥ ਦਿਓ (ਜਿਵੇਂ "microsoft/Phi-3-mini-4k-instruct")। ਮਾਡਲ ਸੈਟਿੰਗਜ਼ ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ, ਜਿਸ ਵਿੱਚ cache ਵਰਤੋਂ, ਡੇਟਾ ਟਾਈਪ (ਮਿਕਸਡ ਪ੍ਰਿਸੀਜ਼ਨ ਲਈ bfloat16), ਅਤੇ attention ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਸ਼ਾਮਲ ਹਨ।

**ਟ੍ਰੇਨਿੰਗ**

ਕਸਟਮ ਚੈਟ ਇੰਸਟ੍ਰਕਸ਼ਨ ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ। ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਅਡੈਪਟੇਸ਼ਨ ਲਈ peft_config ਵਿੱਚ ਦਿੱਤੇ LoRA ਸੈਟਿੰਗਜ਼ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਟ੍ਰੇਨਿੰਗ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਦਿੱਤੀ ਲੌਗਿੰਗ ਰਣਨੀਤੀ ਨਾਲ ਮਾਨੀਟਰ ਕਰੋ।  
ਮੁਲਾਂਕਣ ਅਤੇ ਸੇਵਿੰਗ: ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਮੁਲਾਂਕਣ ਕਰੋ।  
ਟ੍ਰੇਨਿੰਗ ਦੌਰਾਨ ਚੈਕਪੌਇੰਟ ਸੇਵ ਕਰੋ ਤਾਂ ਜੋ ਬਾਅਦ ਵਿੱਚ ਵਰਤਿਆ ਜਾ ਸਕੇ।

**ਨਮੂਨੇ**  
- [ਇਸ ਨਮੂਨਾ ਨੋਟਬੁੱਕ ਨਾਲ ਹੋਰ ਸਿੱਖੋ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [ਪਾਇਥਨ ਫਾਈਨਟਿਊਨਿੰਗ ਨਮੂਨਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [ਲੋਰਾ ਨਾਲ Hugging Face ਹੱਬ ਫਾਈਨ ਟਿਊਨਿੰਗ ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face ਮਾਡਲ ਕਾਰਡ ਦਾ ਉਦਾਹਰਨ - ਲੋਰਾ ਫਾਈਨ ਟਿਊਨਿੰਗ ਨਮੂਨਾ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [QLORA ਨਾਲ Hugging Face ਹੱਬ ਫਾਈਨ ਟਿਊਨਿੰਗ ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।