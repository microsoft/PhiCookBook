<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fdd22719901a23386b3c56bb02794e3",
  "translation_date": "2025-04-04T06:47:40+00:00",
  "source_file": "md\\02.Application\\03.AdvancedReasoning\\Phi4\\AdvancedResoningPhi4mini\\README.md",
  "language_code": "tw"
}
-->
## **使用 Phi-4-mini 作為推理專家**

Phi-4 的主要特點之一是其強大的推理能力。讓我們透過 Phi-4-mini 來看看它的卓越推理能力。

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

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文檔應被視為權威來源。對於重要信息，建議使用專業的人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀不承擔責任。