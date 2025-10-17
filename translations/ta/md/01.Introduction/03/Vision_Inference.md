<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-10-11T12:20:28+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "ta"
}
-->
# **Inference Phi-3-Vision in Local**

Phi-3-vision-128k-instruct மூலம் Phi-3 மொழியைப் புரிந்துகொள்வதுடன், உலகத்தை காட்சியாகவும் பார்க்க முடியும். Phi-3-vision-128k-instruct மூலம், OCR, அட்டவணை பகுப்பாய்வு, பொருள் அடையாளம், படம் விவரிக்குதல் போன்ற பல்வேறு காட்சிப் பிரச்சினைகளை தீர்க்க முடியும். முந்தைய காலங்களில் அதிக அளவிலான தரவுப் பயிற்சியைத் தேவைப்படுத்திய பணிகளை எளிதாக முடிக்க முடியும். Phi-3-vision-128k-instruct மேற்கோள் காட்டிய தொடர்புடைய தொழில்நுட்பங்கள் மற்றும் பயன்பாட்டு சூழல்களை கீழே காணலாம்.

## **0. தயாரிப்பு**

பயன்படுத்துவதற்கு முன், பின்வரும் Python நூலகங்கள் நிறுவப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும் (Python 3.10+ பரிந்துரைக்கப்படுகிறது)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** பயன்படுத்த பரிந்துரைக்கப்படுகிறது மற்றும் flatten நிறுவவும்

```bash
pip install flash-attn --no-build-isolation
```

ஒரு புதிய Notebook உருவாக்கவும். எடுத்துக்காட்டுகளை முடிக்க, முதலில் பின்வரும் உள்ளடக்கத்தை உருவாக்க பரிந்துரைக்கப்படுகிறது.

```python
from PIL import Image
import requests
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoProcessor

model_id = "microsoft/Phi-3-vision-128k-instruct"

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype="auto").cuda()

user_prompt = '<|user|>\n'
assistant_prompt = '<|assistant|>\n'
prompt_suffix = "<|end|>\n"
```

## **1. Phi-3-Vision மூலம் படத்தை பகுப்பாய்வு செய்யவும்**

AI எங்கள் படங்களின் உள்ளடக்கத்தை பகுப்பாய்வு செய்து தொடர்புடைய விளக்கங்களை வழங்க வேண்டும்.

```python
prompt = f"{user_prompt}<|image_1|>\nCould you please introduce this stock to me?{prompt_suffix}{assistant_prompt}"


url = "https://g.foolcdn.com/editorial/images/767633/nvidiadatacenterrevenuefy2017tofy2024.png"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=True, 
                                  clean_up_tokenization_spaces=False)[0]
```

Notebook-ல் பின்வரும் ஸ்கிரிப்டை இயக்குவதன் மூலம் தொடர்புடைய பதில்களைப் பெறலாம்.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision மூலம் OCR**

படத்தை பகுப்பாய்வு செய்வதற்கு கூடுதலாக, படத்திலிருந்து தகவல்களை எடுக்கவும் முடியும். இது OCR செயல்முறை, இதற்கு முன்பு சிக்கலான குறியீடுகளை எழுத வேண்டியிருந்தது.

```python
prompt = f"{user_prompt}<|image_1|>\nHelp me get the title and author information of this book?{prompt_suffix}{assistant_prompt}"

url = "https://marketplace.canva.com/EAFPHUaBrFc/1/0/1003w/canva-black-and-white-modern-alone-story-book-cover-QHBKwQnsgzs.jpg"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=False, 
                                  clean_up_tokenization_spaces=False)[0]

```

முடிவுகள்:

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. பல படங்களின் ஒப்பீடு**

Phi-3 Vision பல படங்களை ஒப்பீடு செய்ய ஆதரிக்கிறது. இந்த மாதிரியைப் பயன்படுத்தி படங்களுக்கிடையேயான வேறுபாடுகளை கண்டறியலாம்.

```python
prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n What is difference in this two images?{prompt_suffix}{assistant_prompt}"

print(f">>> Prompt\n{prompt}")

url = "https://hinhnen.ibongda.net/upload/wallpaper/doi-bong/2012/11/22/arsenal-wallpaper-free.jpg"

image_1 = Image.open(requests.get(url, stream=True).raw)

url = "https://assets-webp.khelnow.com/d7293de2fa93b29528da214253f1d8d0/news/uploads/2021/07/Arsenal-1024x576.jpg.webp"

image_2 = Image.open(requests.get(url, stream=True).raw)

images = [image_1, image_2]

inputs = processor(prompt, images, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

முடிவுகள்:

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.