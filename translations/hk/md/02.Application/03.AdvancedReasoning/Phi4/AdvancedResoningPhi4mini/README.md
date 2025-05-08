<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1f21d34bca1fc59898ff97ca5c113edf",
  "translation_date": "2025-05-08T05:54:38+00:00",
  "source_file": "md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md",
  "language_code": "hk"
}
-->
## **使用 Phi-4-mini-reasoning(3.8b) 或 Phi-4-reasoning(14b) 作為推理專家**

讓我們透過 Phi-4-mini-reasoning 或 Phi-4-mini-reasoning 來看看它強大的推理能力。


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

**免責聲明**：  
本文件係用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我哋致力保持準確，但請注意自動翻譯可能包含錯誤或不準確嘅地方。原文文件嘅母語版本應被視為權威來源。對於重要資訊，建議使用專業人手翻譯。我哋對因使用本翻譯而引致嘅任何誤解或誤釋概不負責。