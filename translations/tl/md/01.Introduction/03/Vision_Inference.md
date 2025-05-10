<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-05-09T13:17:05+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "tl"
}
-->
# **Local na Pagsasagawa ng Inference ng Phi-3-Vision**

Pinapahintulutan ng Phi-3-vision-128k-instruct ang Phi-3 na hindi lang maintindihan ang wika, kundi makita rin ang mundo nang biswal. Sa pamamagitan ng Phi-3-vision-128k-instruct, kaya nating lutasin ang iba't ibang visual na problema, tulad ng OCR, pagsusuri ng talahanayan, pagkilala ng mga bagay, paglalarawan ng larawan, atbp. Madali nating matatapos ang mga gawain na dati ay nangangailangan ng maraming data training. Narito ang mga kaugnay na teknolohiya at mga senaryo ng aplikasyon na binanggit ng Phi-3-vision-128k-instruct

## **0. Paghahanda**

Siguraduhing naka-install na ang mga sumusunod na Python libraries bago gamitin (inirerekomenda ang Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Inirerekomenda ang paggamit ng ***CUDA 11.6+*** at pag-install ng flatten

```bash
pip install flash-attn --no-build-isolation
```

Gumawa ng bagong Notebook. Para makumpleto ang mga halimbawa, mas mainam na gawin mo muna ang mga sumusunod na nilalaman.

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

## **1. Pagsusuri ng larawan gamit ang Phi-3-Vision**

Nais nating matulungan ang AI na ma-analisa ang nilalaman ng ating mga larawan at magbigay ng kaugnay na paglalarawan

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

Makukuha natin ang mga kaugnay na sagot sa pamamagitan ng pagpapatakbo ng sumusunod na script sa Notebook

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR gamit ang Phi-3-Vision**

Bukod sa pagsusuri ng larawan, maaari rin nating kunin ang impormasyon mula sa larawan. Ito ang proseso ng OCR na dati ay kailangan nating sumulat ng komplikadong code para matapos.

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

Ang resulta ay

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Paghahambing ng maramihang larawan**

Sinusuportahan ng Phi-3 Vision ang paghahambing ng maraming larawan. Maaari nating gamitin ang modelong ito para makita ang mga pagkakaiba sa pagitan ng mga larawan.

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

Ang resulta ay

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Pagtatanggol**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinagmulan ng katotohanan. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.