## **ការដកស្រង់អត្ថបទពីអូឌីយោដោយប្រើ Phi-4-multimodal**

Phi-4-multimodal គឺជាម៉ូដែលពហុរបៀប (full-modal) ដែលអាចប្រើអូឌីយោ បន្ថែមលើអត្ថបទ និងរូបភាព។ យើងមកមើលពីរបៀបប្រើវា។


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
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយបញ្ញាសិប្បនិម្មិត (AI) [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខិតខំដើម្បីធ្វើឲ្យមានភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវបានបញ្ចូល។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកជាប្រភពយោងដែលមានអាទិភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឲ្យប្រើការបកប្រែដោយមនុស្សដែលមានវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកអត្ថន័យខុសណាមួយ ដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែមួយនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->