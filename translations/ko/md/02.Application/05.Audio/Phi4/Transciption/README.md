<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cba62af5dffbdc4eed3a3290f30949fd",
  "translation_date": "2025-07-17T05:11:12+00:00",
  "source_file": "md/02.Application/05.Audio/Phi4/Transciption/README.md",
  "language_code": "ko"
}
-->
## **Phi-4-multimodal을 사용한 오디오 전사 추출**

Phi-4-multimodal은 텍스트와 이미지뿐만 아니라 오디오도 활용할 수 있는 풀모달 모델입니다. 어떻게 사용하는지 살펴보겠습니다.


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

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.