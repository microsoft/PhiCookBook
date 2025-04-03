<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "550f504a78659133aa4c5757a6d875ce",
  "translation_date": "2025-04-03T07:55:16+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi4\\CreateFrontend\\README.md",
  "language_code": "ur"
}
-->
## **Phi-4-multimodal کا استعمال کرتے ہوئے تصاویر پڑھیں اور کوڈ تیار کریں**

Phi-4-multimodal میں تصاویر کو پڑھنے کی زبردست صلاحیتیں موجود ہیں۔ آئیے Python کا استعمال کرتے ہوئے درج ذیل فنکشنز کو نافذ کرنے کی کوشش کرتے ہیں۔ تصویر ایک ChatGPT صفحہ ہے۔

![demo](../../../../../../../translated_images/demo.415266e14de58ca0799f56584dec6684be4bf8d78ab882a38c7a635830f445f4.ur.png)

### **نمونہ کوڈ**  

```python

import requests
import torch
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

prompt = f'{user_prompt}Can you generate HTML + JS code about this image <|image_1|> ? Please step by step {prompt_suffix}{assistant_prompt}'

image = Image.open("./demo.png")

inputs = processor(text=prompt, images=[image], return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=4096,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقصانات ہو سکتے ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔