<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cba62af5dffbdc4eed3a3290f30949fd",
  "translation_date": "2025-12-21T19:15:43+00:00",
  "source_file": "md/02.Application/05.Audio/Phi4/Transciption/README.md",
  "language_code": "ml"
}
-->
## **Phi-4-multimodal ഉപയോഗിച്ച് ഓഡിയോ ട്രാൻസ്‌ക്രിപ്റ്റുകൾ എടുക്കൽ**

Phi-4-multimodal ടെക്സ്റ്റ്, ചിത്രങ്ങൾ എന്നിവയ്ക്കൊപ്പം ഓഡിയോയും ഉപയോഗിക്കാൻ കഴിയുന്ന ഒരു ഫുൾ-മോഡൽ ആണ്. ഇത് എങ്ങനെ ഉപയോഗിക്കാമെന്ന് നോക്കാം.


```python

import requests
import torch
import soundfile
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-multimodal location'

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

speech_prompt = "Based on the attached audio, generate a comprehensive text transcription of the spoken content."
prompt = f'{user_prompt}<|audio_1|>{speech_prompt}{prompt_suffix}{assistant_prompt}'

audio = soundfile.read('./ignite.wav')

inputs = processor(text=prompt, audios=[audio], return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=1200,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)


```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
നിരാകരണ കുറിപ്പ്:
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തിരിക്കുന്നു. ഞങ്ങൾ ശരിയായ വിവർത്തനത്തിനായി ശ്രമിച്ചിരിക്കുമ്പോഴും, യാന്ത്രിക വിവർത്തനങ്ങളിൽ തെറ്റുകൾ അല്ലെങ്കിൽ അസ്ഥിരതകൾ ഉണ്ടാകാമെന്നത് ദയവായി ശ്രദ്ധിക്കുക. ഈ രേഖയുടെ മൂലഭാഷയിൽ ഉള്ള പ്രസ്താവന ആധികാരിക ഉറവിടമായിരിക്കണം. അത്യാവശ്യ/inഗം വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദേശം ചെയ്യുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗം മൂലം ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണങ്ങളിലും തെറ്റായ വ്യാഖ്യാനങ്ങളിലും ഞങ്ങൾക്ക് ഉത്തരവാദിത്വം ഇല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->