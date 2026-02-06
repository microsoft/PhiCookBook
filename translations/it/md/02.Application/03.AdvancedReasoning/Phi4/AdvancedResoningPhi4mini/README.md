## **Usare Phi-4-mini-reasoning(3.8b) o Phi-4-reasoning(14b) come Esperto di Ragionamento**

Diamo un’occhiata alla sua forte capacità di ragionamento tramite Phi-4-mini-reasoning o Phi-4-mini-reasoning.


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
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.