## **Phi-4-mini-reasoning(3.8b) లేదా Phi-4-reasoning(14b) ను తార్కిక నిపుణుడిగా ఉపయోగించడం**

దాని శక్తివంతమైన తార్కిక సామర్థ్యాన్ని Phi-4-mini-reasoning లేదా Phi-4-mini-reasoning ద్వారా చూద్దాం。


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
నిరాకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండవచ్చు. మూల పత్రాన్ని దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించండి. కీలక సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సిఫారసు చేస్తున్నాము. ఈ అనువాదం ఉపయోగం వల్ల ఉద్భవించే ఏవైనా అపార్థాలు లేదా తప్పుడు వ్యాఖ్యానాల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->