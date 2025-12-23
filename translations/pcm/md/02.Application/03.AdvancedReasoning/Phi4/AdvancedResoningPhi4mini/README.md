<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1f21d34bca1fc59898ff97ca5c113edf",
  "translation_date": "2025-12-21T22:07:08+00:00",
  "source_file": "md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md",
  "language_code": "pcm"
}
-->
## **Make we use Phi-4-mini-reasoning(3.8b) or Phi-4-reasoning(14b) as Reasoning Expert**

Make we look how e strong for reasoning through Phi-4-mini-reasoning or Phi-4-mini-reasoning.


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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note:
Dis document dem don translate wit AI translation service Co‑op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automatic translations fit get errors or no 100% correct. The original document for hin original language na the official source you suppose rely on. For critical or important information, better make professional human translator check or do the translation. We no go responsible for any misunderstanding or wrong interpretation wey fit comot from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->