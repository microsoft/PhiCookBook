<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-12-22T00:46:02+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "te"
}
-->
# **లోకల్‌లో Phi-3-Vision ఇన్ఫరెన్స్**

Phi-3-vision-128k-instruct ద్వారా Phi-3 కేవలం భాషను మాత్రమే అర్థం చేసుకోవడం కాదు, ప్రపంచాన్ని దృశ్యంగా కూడా చూడగలుగుతుంది. Phi-3-vision-128k-instruct ద్వారా మేము OCR, పట్టిక విశ్లేషణ, వస్తు గుర్తింపు, చిత్రం వివరణ వంటి వివిధ దృశ్య సమస్యలను పరిష్కరించగలము. ముందుగా పెద్ద మొత్తంలో డేటా ట్రైనింగ్ అవసరమవుతున్న పనులను ఇప్పుడు సులభంగా పూర్తి చేయవచ్చు. కింద ఇచ్చినవి Phi-3-vision-128k-instruct సూచించిన సంబంధిత సాంకేతికతలు మరియు అనువర్తన సందర్భాలు.

## **0. సిద్ధత**

దయచేసి వాడకానికి ముందుగా క్రిందివి Python లైబ్రరీలు ఇన్‌స్టాల్ చేసినట్లు నిర్ధారించుకోండి (Python 3.10+ సూచించబడింది)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ఉపయోగించడం సూచించబడుతుంది మరియు flatten ఇన్‌స్టాల్ చేయండి

```bash
pip install flash-attn --no-build-isolation
```

కొత్త Notebook సృష్టించండి. ఉదాహరణలను పూర్తి చేయడానికి, ముందుగా మీరు క్రింది విషయం/కంటెంట్‌ను సృష్టించడం సూచించబడుతుంది.

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

## **1. Phi-3-Visionతో చిత్రం విశ్లేషణ**

మేము AI మా చిత్రాల విషయాన్ని విశ్లేషించి సంబంధిత వివరణలు ఇవ్వగలగాలని కోరుకుంటున్నాము

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

Notebookలో క్రింద ఇచ్చిన స్క్రిప్ట్‌ను అమలు చేయడం ద్వారా సంబంధిత సమాధానాలను పొందవచ్చు

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Visionతో OCR**

చిత్రాన్ని విశ్లేషించడం కాకుండా, చిత్రంలో నుండి సమాచారాన్ని కూడా వెలికి తీసుకోవచ్చు. ఇది OCR ప్రక్రియ, దీన్ని పూర్తి చేయడానికి మునుపటి కాలంలో క్లిష్టమైన కోడ్ రాయాల్సి వాలేదని విధంగా ఉండేది.

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

ఫలితం

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. బహుళ చిత్రాల పోలిక**

Phi-3 Vision అనేక చిత్రాల పోలికకు మద్దతు ఇస్తుంది. చిత్రాల మధ్య తేడాలను కనుగొనడానికి మేము ఈ మోడల్‌ను ఉపయోగించవచ్చు.

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

ఫలితం

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించారు. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలిత అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండవచ్చు. మూల భాషలో ఉన్న అసలైన పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరులైన మానవ అనువాదాన్ని పొందాలని సూచిస్తాం. ఈ అనువాదం ఉపయోగం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యులం కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->