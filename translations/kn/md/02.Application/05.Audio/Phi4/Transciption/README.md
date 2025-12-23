<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cba62af5dffbdc4eed3a3290f30949fd",
  "translation_date": "2025-12-21T19:16:09+00:00",
  "source_file": "md/02.Application/05.Audio/Phi4/Transciption/README.md",
  "language_code": "kn"
}
-->
## **Phi-4-multimodal ಬಳಸಿ ಆಡಿಯೋ ಪ್ರತಿಲಿಪಿಗಳನ್ನು ಹೊರತೆಗೆಯುವುದು**

Phi-4-multimodal ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರಗಳ ಜೊತೆಗೆ ಆಡಿಯೋವನ್ನು ಕೂಡ ಬಳಸಲು ಸಾಧ್ಯವಾಗುವ ಸಂಪೂರ್ಣ-ಮೊಡಲ್ ಮಾದರಿಯಾಗಿದೆ. ಇದನ್ನು ಹೇಗೆ ಬಳಸುವುದು ನೋಡೋಣ.

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
ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯ ಕಡೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದೆಂದನ್ನು ದಯವಿಟ್ಟು ಗಮನಕ್ಕೆ ತೆಗೆದುಕೊಳ್ಳಿ. ಮೂಲ ಭಾಷೆಯುಳ್ಳ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕಾರಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ತೀವ್ರವಾಗಿ ಮಹತ್ವದ ಮಾಹಿತಿಗಳಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು드립니다. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗರ್ಭಿತತೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->