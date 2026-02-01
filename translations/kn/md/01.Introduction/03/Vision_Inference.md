# **ಸ್ಥಳೀಯವಾಗಿ Phi-3-Vision ನಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್**

Phi-3-vision-128k-instruct Phi-3 ಗೆ ಕೇವಲ ಭಾಷೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಮಾತ್ರವಲ್ಲದೆ, ಜಗತ್ತನ್ನು ದೃಶ್ಯವಾಗಿ ನೋಡಲು ಸಹ ಅನುಮತಿಸುತ್ತದೆ. Phi-3-vision-128k-instruct ಮೂಲಕ ನಾವು OCR, ಟೇಬಲ್ ವಿಶ್ಲೇಷಣೆ, ವಸ್ತು ಗುರುತಿಸುವಿಕೆ, ಚಿತ್ರ ವರ್ಣನೆ ಮುಂತಾದ ವಿಭಿನ್ನ ದೃಶ್ಯ ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಹರಿಸಬಹುದು. ಪೂರ್ವಕೆ ಹೆಚ್ಚು ಡೇಟಾ ತರಬೇತಿ ಬೇಕಾಗಿದ್ದ ಕಾರ್ಯಗಳನ್ನು ನಾವು ಸುಲಭವಾಗಿ ಪೂರ್ಣಗೊಳಿಸಬಹುದು. ಕೆಳಗಿನವುಗಳು Phi-3-vision-128k-instruct ಮೂಲಕ ಉಲ್ಲೇಖಿಸಲಾದ ಸಂಬಂಧಿತ ತಂತ್ರಗಳು ಮತ್ತು ಅನ್ವಯದ ಪರಿಸ್ಥಿತಿಗಳು

## **0. ಸಿದ್ಧತೆ**

ದಯವಿಟ್ಟು ಕೆಳಗಿನ Python ಗ್ರಂಥಾಲಯಗಳು ಬಳಕೆಗೆ ಮುನ್ನ ಸ್ಥಾಪಿತವಾಗಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ (Python 3.10+ ಅನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ಬಳಸಲು ಮತ್ತು flatten ಅನ್ನು ಸ್ಥಾಪಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ

```bash
pip install flash-attn --no-build-isolation
```

ಹೊಸ ನೋಟ್‌ಬುಕ್ ರಚಿಸಿ. ಉದಾಹರಣೆಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ಮೊದಲು ಕೆಳಗಿನ ವಿಷಯವನ್ನು ರಚಿಸುವುದು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ.

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

## **1. Phi-3-Vision ಮೂಲಕ ಚಿತ್ರವನ್ನು ವಿಶ್ಲೇಷಿಸುವುದು**

ನಮ್ಮ ಚಿತ್ರಗಳ ವಿಷಯವನ್ನು AI ವಿಶ್ಲೇಷಿಸಿ ಸಂಬಂಧಿತ ವಿವರಣೆಗಳನ್ನು ನೀಡಲು ಸಾಧ್ಯವಾಗಲಿ ಎಂದು ನಾವು ಬಯಸುತ್ತೇವೆ

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

ನೋಟ್ಬುಕ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು 실행ಿಸುವ ಮೂಲಕ ನಾವು ಸಂಬಂಧಿತ ಉತ್ತರಗಳನ್ನು ಪಡೆಯಬಹುದು

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ಮೂಲಕ OCR**

ಚಿತ್ರವನ್ನು ವಿಶ್ಲೇಷಿಸುವುದೋಲ್ಲದೆ, ಚಿತ್ರದಿಂದ ಮಾಹಿತಿಯನ್ನು ಹೊರಹಾಕಬಹುದು. ಇದು ನಮಗೆ ಮೊದಲು ಸಂಕೀರ್ಣ ಕೋಡ್ ಬರೆಯಬೇಕಾಗಿದ್ದ OCR ಪ್ರಕ್ರಿಯೆ.

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

ಫಲಿತಾಂಶವು

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. ಹಲವಾರು ಚಿತ್ರಗಳ ಹೋಲಿಕೆ**

Phi-3 Vision ಬಹುಚಿತ್ರಗಳ ಹೋಲಿಕೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ನಾವು ಈ ಮಾದರಿಯನ್ನು ಚಿತ್ರಗಳ ನಡುವಿನ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಕಂಡುಹಿಡಿಯಲು ಬಳಸಬಹುದು.

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

ಫಲಿತಾಂಶವು

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಆಧಾರಿತ ಅನುವಾದ ಸೇವೆಯ ಮೂಲಕ ಅನುವದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯ ಮೇಲೊಂದು ಪ್ರಯತ್ನ ಮಾಡುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ఉండಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಹಾಗೂ ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅಸಮಜ್ಞತೆಗಳು ಅಥವಾ ತಪ್ಪಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲಾಗುವ ಪ್ರಕರಣಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->