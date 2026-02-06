## **Phi-4-multimodal ఉపయోగించి ఆడియో ట్రాన్స్‌క్రిప్ట్‌లను పొందడం**

Phi-4-multimodal అనేది టెక్స్ట్ మరియు చిత్రాలతో పాటు ఆడియోను కూడా ఉపయోగించగల ఒక పూర్తి మోడల్. దీన్ని ఎలా ఉపయోగించాలో చూద్దాం.

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
బాధ్యత నిరాకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించాం. మేము ఖచ్చితత్వాన్ని లక్ష్యంగా పెట్టుకున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు, తప్పులు లేదా లోపాలు ఉండే అవకాశం ఉంది. మూల డాక్యుమెంట్‌ను దాని స్థానిక భాషలో ప్రామాణిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం సూచించబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడంవల్ల ఏర్పడిన ఏవైనా అవగాహనా లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->