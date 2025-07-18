<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1f21d34bca1fc59898ff97ca5c113edf",
  "translation_date": "2025-07-17T04:49:39+00:00",
  "source_file": "md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md",
  "language_code": "br"
}
-->
## **Usando Phi-4-mini-reasoning(3.8b) ou Phi-4-reasoning(14b) como Especialista em Raciocínio**

Vamos dar uma olhada na sua forte capacidade de raciocínio através do Phi-4-mini-reasoning ou Phi-4-mini-reasoning.


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

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.