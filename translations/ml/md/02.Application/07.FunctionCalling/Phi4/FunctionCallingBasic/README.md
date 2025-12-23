<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b7078bd9f16589c50139fbba8674de82",
  "translation_date": "2025-12-21T21:52:52+00:00",
  "source_file": "md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md",
  "language_code": "ml"
}
-->
## **Phi-4-mini-ൽ ഫംഗ്ഷൻ കോൾ ചെയ്യൽ**

ഫംഗ്ഷൻ കോൾ ചെയ്യൽ ആദ്യമായി Phi Family കുടുംബത്തിൽ പ്രത്യക്ഷപ്പെട്ടു, ഇപ്പോൾ നിങ്ങൾ അത് Phi-4-mini മുഖാന്തിരം ഉപയോഗിക്കാം.

ഈ ഉദാഹരണം Premier League ഫലങ്ങളുടെ സിമുലേഷൻ കാണിക്കുന്നു. ലക്ഷ്യം Phi-4-mini കളിയുടെ തത്സമയ വിവരങ്ങൾ നൽകുക എന്നതാണ്. താഴെ സാമ്പിൾ കോഡ്:

```python

import torch
import json
import random
import string
import re
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = "Your Phi-4-mini location"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="cuda",
    attn_implementation="flash_attention_2",
    torch_dtype="auto",
    trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# ടൂളുകൾ json ഫോർമാറ്റിൽ സൂക്ഷിച്ചിട്ടുള്ള ഫങ്ഷനുകളുടെ ഒരു ലിസ്റ്റ് ആയിരിക്കണം
tools = [
    {
        "name": "get_match_result",
        "description": "get match result",
        "parameters": {
            "match": {
                "description": "The name of the match",
                "type": "str",
                "default": "Arsenal vs ManCity"
            }
        }
    },
]

# ഫങ്ഷനുകളുടെ നടപ്പാക്കലുകൾ

def get_match_result(match: str) -> str:
    # ഇത് ഒരു കാലാവസ്ഥ API ഉപയോഗിച്ച് മാറ്റിപ്പിടിക്കും
    match_data = {
        "Arsenal vs ManCity": "1:1",
        "Chelsea vs ManUnited": "0:2"
    }
    return match_data.get(match, "I don't know")


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant",
        "tools": json.dumps(tools), # tools എന്ന argument ഉപയോഗിച്ച് ടൂളുകൾ സിസ്റ്റം മെസേജിലേക്ക് പാസാക്കുക
    },
    {
        "role": "user",
        "content": "What is the result of Arsenal vs ManCity today?"
    }
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_dict=True, return_tensors="pt")

inputs = {k: v.to(model.device) for k, v in inputs.items()}
output = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(output[0][len(inputs["input_ids"][0]):]))

tokenizer.batch_decode(output)

response = tokenizer.decode(output[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)

tool_call_id = ''.join(random.choices(string.ascii_letters + string.digits, k=9))

messages.append({"role": "assistant", "tool_calls": [{"type": "function", "id": tool_call_id, "function": response}]})

try :
    tool_call = json.loads(response)[0]

except :
    json_part = re.search(r'\[.*\]', response, re.DOTALL).group(0)

    tool_call = json.loads(json_part)[0]


function_name = tool_call["name"]   

arguments = tool_call["arguments"]

result = get_match_result(**arguments) 

messages.append({"role": "tool", "tool_call_id": tool_call_id, "name": "get_match_result", "content": str(result)})

print(messages)

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ രേഖ AI തർജ്ജമാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജമ ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യത ഉറപ്പാക്കാൻ ശ്രമിച്ചെങ്കിലും, ഓട്ടോമേറ്റഡ് തർജ്ജമകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാമെന്നത് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ സ്വഭാഷയിലെ മൂല രേഖ പ്രാമാണിക ഉറവിടമായി പരിഗണിക്കപ്പെടണം. നിർണായകമായ വിവരങ്ങൾക്ക്, ഒരു വിദഗ്ധ മനുഷ്യൻ നിർവഹിച്ചു തർജ്മ ചെയ്യുന്നത് ശുപാർശനീയമാണ്. ഈ തർജ്മ ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാവുന്ന ഏതൊരു തെറ്റിദ്ധാരണക്കും അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനത്തിനും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->