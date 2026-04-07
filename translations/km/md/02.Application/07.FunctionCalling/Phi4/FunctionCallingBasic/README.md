## **ការហៅមុខងារ ក្នុង Phi-4-mini**

ការហៅមុខងារបានបង្ហាញជាលើកដំបូងនៅក្នុងគ្រួសារ Phi Family ហើយឥឡូវនេះអ្នកអាចប្រើវាតាមរយៈ Phi-4-mini។

ឧទាហរណ៍នេះបង្ហាញពីការត្រួតពិនិត្យលទ្ធផល Premier League។ គោលបំណងគឺសម្រាប់ Phi-4-mini ដើម្បីផ្តល់ព័ត៌មានលេងហ្គេមពេលវេលាពិត។ ខាងក្រោមជាកូដគំរូ៖



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

# ឧបករណ៍គួរតែជាបញ្ជីនៃមុខងារដែលបានរក្សាទុកក្នុងទ្រង់ទ្រាយ json
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

# ការអនុវត្តមុខងារ

def get_match_result(match: str) -> str:
    # នេះនឹងត្រូវបានជំនួសដោយ APIអាកាសធាតុ
    match_data = {
        "Arsenal vs ManCity": "1:1",
        "Chelsea vs ManUnited": "0:2"
    }
    return match_data.get(match, "I don't know")


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant",
        "tools": json.dumps(tools), # បញ្ជូនឧបករណ៍ទៅក្នុងសារប្រព័ន្ធដោយប្រើអ៉ាហ្គឺម៉ង់ tools
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
**ការបំពាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាប្រែសម្រួល AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការប្រែសម្រួលដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសារបស់ខ្លួនគួរត្រូវបានចាត់ទុកជារមូររាក់ទាក់ផ្លូវការរបស់ព័ត៌មាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្ដល់អាទិភាពការប្រែសម្រួលដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសឆ្គងណាមួយដែលកើតមានចេញពីការប្រើប្រាស់ការប្រែសម្រួលនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->