<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b7078bd9f16589c50139fbba8674de82",
  "translation_date": "2025-12-21T21:54:14+00:00",
  "source_file": "md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md",
  "language_code": "kn"
}
-->
## **Phi-4-mini ನಲ್ಲಿ ಫಂಕ್ಷನ್ ಕರೆ**

ಫಂಕ್ಷನ್ ಕರೆ ಮೊದಲು Phi Family family ನಲ್ಲಿ ಕಾಣಿಸಿಕೊಂಡಿತು, ಮತ್ತು ಈಗ ನೀವು ಅದನ್ನನ್ನು Phi-4-mini ಮೂಲಕ ಬಳಸಬಹುದು.

ಈ ಉದಾಹರಣೆ Premier League ಫಲಿತಾಂಶಗಳ ಅನುಕರಣೆಯನ್ನು ತೋರಿಸುತ್ತದೆ. ಉದ್ದೇಶವೆಂದರೆ Phi-4-mini ರಿಯಲ್-ಟೈಮ್ ಆಟದ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸುವುದು. ಕೆಳಗೆ ಉದಾಹರಣಾ ಕೋಡ್ ನೀಡಲಾಗಿದೆ:

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

# ಉಪಕರಣಗಳು json ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾದ ಫಂಕ್ಷನ್‌ಗಳ ಪಟ್ಟಿಯಾಗಿರಬೇಕು
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

# ಫಂಕ್ಷನ್ ಅನುಷ್ಠಾನಗಳು

def get_match_result(match: str) -> str:
    # ಇದನ್ನು ಹವಾಮಾನ API ನಿಂದ ಬದಲಿಸಲಾಗುತ್ತದೆ
    match_data = {
        "Arsenal vs ManCity": "1:1",
        "Chelsea vs ManUnited": "0:2"
    }
    return match_data.get(match, "I don't know")


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant",
        "tools": json.dumps(tools), # tools ಆರ್ಗ್ಯೂಮೆಂಟ್ ಬಳಸಿ ಉಪಕರಣಗಳನ್ನು ಸಿಸ್ಟಮ್ ಸಂದೇಶಕ್ಕೆ ಪಾಸ್ ಮಾಡಿ
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
ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ AI ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿಕೊಂಡು ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ಅನುಕೂಲಕರವಾದ ಅನುವಾದಕ್ಕಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಕ್ರಿಯ (ಸ್ವಯಂಚಾಲಿತ) ಭಾಷಾಂತರಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಅನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರದ ಬಳಕೆಯಿಂದ ಉಂಟಾದ ಯಾವುದೇ ಅಸಮಜ್ಞತೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->