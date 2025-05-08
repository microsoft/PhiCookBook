<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1f21d34bca1fc59898ff97ca5c113edf",
  "translation_date": "2025-05-07T14:27:35+00:00",
  "source_file": "md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md",
  "language_code": "mo"
}
-->
## **Phi-4-mini-reasoning(3.8b) သို့မဟုတ် Phi-4-reasoning(14b) ကို Reasoning Expert အဖြစ် အသုံးပြုခြင်း**

Phi-4-mini-reasoning သို့မဟုတ် Phi-4-mini-reasoning မှတဆင့် ၎င်း၏ အားသာချက် reasoning စွမ်းရည်ကို ကြည့်ကြရအောင်။


```python

import torch
from transformers import AutoTokenizer,pipeline

model_path = "Your Phi-4-mini-reasoning or Phi-4-reasoning location"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,

)

tokenizer = AutoTokenizer.from_pretrained(model_path)

messages = [{"role": "user", "content": "Explain the Pythagorean Theorem"}]

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_dict=True, return_tensors="pt")

outputs = model.generate(**inputs.to(model.device), max_new_tokens=32768)

outputs = tokenizer.batch_decode(outputs[:, inputs["input_ids"].shape[-1]:])

print(outputs[0])


```

**Disclaimer**:  
Thi documint haz bin translaited yusing AI translaition serviss [Co-op Translator](https://github.com/Azure/co-op-translator). Whil wi striv for akyurasy, pleez bi awair that otomaytid translaitions mei contain errurs or inakurysez. Thi orijinal documint in its naytiv langwaj shud bi considird thi autoritativ sours. For kritikal informayshun, profeshunal hyuman translaition is rekomended. Wi ar not laybil for eni misandurstandings or misinterpretayshuns arising from thi yus of this translaition.