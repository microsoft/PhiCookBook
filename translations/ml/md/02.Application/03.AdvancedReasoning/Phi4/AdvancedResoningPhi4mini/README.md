<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1f21d34bca1fc59898ff97ca5c113edf",
  "translation_date": "2025-12-21T22:08:42+00:00",
  "source_file": "md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md",
  "language_code": "ml"
}
-->
## **Phi-4-mini-reasoning(3.8b) അല്ലെങ്കിൽ Phi-4-reasoning(14b) കാരണീയതാ വിദഗ്ധനായി ഉപയോഗിക്കൽ**

അതിന്റെയായ ശക്തമായ കാരണീയതാ കഴിവ് Phi-4-mini-reasoning അല്ലെങ്കിൽ Phi-4-mini-reasoning മുഖേന നോക്കാം.


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
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തന സേവനമായ Co-op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി പരിശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടായേക്കാമെന്നത് ദയവായി ശ്രദ്ധിക്കുക. മുഖ്യമാമായ ഭാഷയിലുള്ള മൂല രേഖയെ ഔദ്യോഗിക സ്രോതസ്സായി കണക്കാക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദേശിക്കുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിനാൽ ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->