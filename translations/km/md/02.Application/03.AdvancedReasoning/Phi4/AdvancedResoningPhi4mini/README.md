## **ការប្រើប្រាស់ Phi-4-mini-reasoning(3.8b) ឬ Phi-4-reasoning(14b) ជាអ្នកជំនាញក្នុងការសម្រេចចិត្ត**

និយាយអំពីសមត្ថភាពសម្រេចចិត្តដ៏ខ្លាំងរបស់វាតាមរយៈ Phi-4-mini-reasoning ឬ Phi-4-mini-reasoning។


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
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបំលែងភាសាដោយប្រើសេវាកម្មបំលែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងបានខំប្រឹងប្រែងដើម្បីបានភាពត្រឹមត្រូវ ក៏សូមដឹងថាការបំលែងភាសាដោយស្វ័យប្រវត្តិក្នុងរូបភាពនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាដើមត្រូវបានរាប់បញ្ចូលជាតំណត់ត្រាសម quyền។ សម្រាប់ព័ត៌មានសំខាន់ សូមផ្តល់អនុសាសន៍អោយបំលែងភាសាប្រកបដោយវិជ្ជាជីវៈដោយមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការប្រាប់ប្រាសពីការប្រើប្រាស់ការបំលែងភាសានេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->