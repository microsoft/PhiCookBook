## **Phi-4-miniలో ఫంక్షన్ కాలింగ్**

ఫంక్షన్ కాలింగ్ మొదటగా Phi Family కుటుంబంలో కనిపించింది, మరియు ఇప్పుడు మీరు దాన్ని Phi-4-mini ద్వారా ఉపయోగించుకోవచ్చు.

ఈ ఉదాహరణ ప్రీమియర్ లీగ్ ఫలితాల సిమ్యులేషన్‌ను చూపిస్తుంది. లక్ష్యం Phi-4-mini ద్వారా రియల్-టైమ్ గేమ్ సమాచారం అందించడం. క్రింద నమూనా కోడ్ ఉంది:



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

# పరికరాలు json ఫార్మాట్‌లో నిల్వ చేయబడిన ఫంక్షన్‌ల జాబితాగా ఉండాలి
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

# ఫంక్షన్ అమలులు

def get_match_result(match: str) -> str:
    # ఇది ఒక వాతావరణ APIతో భర్తీ చేయబడుతుంది
    match_data = {
        "Arsenal vs ManCity": "1:1",
        "Chelsea vs ManUnited": "0:2"
    }
    return match_data.get(match, "I don't know")


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant",
        "tools": json.dumps(tools), # tools ఆర్గ్యుమెంట్ ఉపయోగించి పరికరాలను సిస్టమ్ సందేశానికి పంపండి
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
బాధ్యత మినహాయింపు ప్రకటన:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ అయిన [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వాన్ని లక్ష్యంగా పెట్టుకున్నప్పటికీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండవచ్చు. మూల పత్రాన్ని దాని స్థానిక భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, నిపుణులాచేయబడిన మానవ అనువాదం చేయించుకోవటంలా సిఫారసు చేయబడుతుంది. ఈ అనువాదంతో సంభవించే ఏవైనా అవగాహనా తప్పిదాలు లేదా తప్పుగా అర్థం చేసుకోవడాలపై మేము బాధ్యత్వం వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->