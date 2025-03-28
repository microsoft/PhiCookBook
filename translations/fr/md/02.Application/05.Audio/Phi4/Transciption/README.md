<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cba62af5dffbdc4eed3a3290f30949fd",
  "translation_date": "2025-03-27T13:05:59+00:00",
  "source_file": "md\\02.Application\\05.Audio\\Phi4\\Transciption\\README.md",
  "language_code": "fr"
}
-->
## **Extraction de transcriptions audio avec Phi-4-multimodal**

Phi-4-multimodal est un modèle multimodal complet qui peut utiliser l'audio en plus du texte et des images. Voyons comment l'utiliser.

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

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions de garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle effectuée par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.