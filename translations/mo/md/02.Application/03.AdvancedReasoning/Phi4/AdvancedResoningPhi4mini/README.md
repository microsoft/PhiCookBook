<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fdd22719901a23386b3c56bb02794e3",
  "translation_date": "2025-04-04T12:59:53+00:00",
  "source_file": "md\\02.Application\\03.AdvancedReasoning\\Phi4\\AdvancedResoningPhi4mini\\README.md",
  "language_code": "mo"
}
-->
## **Folosirea Phi-4-mini ca Expert în Raționament**

Una dintre principalele caracteristici ale Phi-4 este capacitatea sa puternică de raționament. Să analizăm această abilitate impresionantă prin Phi-4-mini.

```python

import torch
from transformers import AutoTokenizer,pipeline

model_path = "Your Phi-4-mini location"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="cuda",
    attn_implementation="flash_attention_2",
    torch_dtype="auto",
    trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": """I have $20,000 in my savings account, where I receive a 4% profit per year and payments twice a year. Can you please tell me how long it will take for me to become a millionaire? Thinks step by step carefully.
"""},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 4096,
    "return_full_text": False,
    "temperature": 0.00001,
    "top_p": 1.0,
    "do_sample": True,
}

output = pipe(messages, **generation_args)

print(output[0]['generated_text'])



```

It seems you are asking for a translation into "mo," but could you clarify what "mo" refers to? Are you referring to Maori, Mongolian, or another language? Let me know, and I'd be happy to assist!