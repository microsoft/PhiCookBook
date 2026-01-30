# **ഇൻഫറൻസ് Phi-3-Vision ലോക്കലിൽ**

Phi-3-vision-128k-instruct Phi-3-നെ ഭാഷ മനസ്സിലാക്കുന്നത് മാത്രമല്ല, ലോകത്തെ ദൃശ്യമായി കാണാനുള്ള ശക്തിയും നൽകുന്നു. Phi-3-vision-128k-instruct വഴിയാണ് നാം OCR, പട്ടിക വിശകലനം, വസ്തു തിരിച്ചറിവ്, ചിത്ര വിവരണം എന്നിവ പോലുള്ള വിവിധ ദൃശ്യ പ്രശ്‌നങ്ങൾ പരിഹരിക്കാവുന്നത്. മുൻപ് വലിയ അളവിൽ ഡാറ്റ ട്രെയിനിംഗ് ആവശ്യമുണ്ടായിരുന്ന ജോലി എന്നീ കാര്യങ്ങൾ നാം എളുപ്പത്തിൽ പൂർത്തിയാക്കാൻ കഴിയും. താഴെ Phi-3-vision-128k-instruct ഉദ്ധരിച്ച ബന്ധപ്പെട്ട സാങ്കേതികവിദ്യകളും ഉപയോഗ സാഹചര്യങ്ങളും നൽകിയിരിക്കുന്നു

## **0. തയാറെടുപ്പ്**

വിനിയோகത്തിന് മുമ്പായി താഴെയുള്ള Python ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ദയവായി ഉറപ്പാക്കുക (Python 3.10+ ശുപാർശ ചെയ്യപ്പെടുന്നു)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ഉപയോഗിക്കാൻ ശുപാർശ ചെയ്യപ്പെടുന്നു കൂടാതെ flatten ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install flash-attn --no-build-isolation
```

ഒരു പുതിയ Notebook സൃഷ്‌ടിക്കുക. ഉദാഹരണങ്ങൾ പൂർത്തിയാക്കാൻ, ആദ്യം താഴെ കാണുന്ന ഉള്ളടക്കം സൃഷ്‌ടിക്കാൻ ശുപാർശ ചെയ്യപ്പെടുന്നു.

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

## **1. Phi-3-Vision ഉപയോഗിച്ച് ചിത്രം വിശകലനം ചെയ്യുക**

ഞങ്ങൾ ആഗ്രഹിക്കുന്നത് AI നമ്മുടെ ചിത്രങ്ങളുടെ ഉള്ളടക്കം വിശകലനം ചെയ്ത് അനുയോജ്യമായ വിവരണം നൽകാൻ കഴിയുക എന്നതാണ്

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

നാം Notebook-ൽ താഴെയുള്ള സ്ക്രിപ്റ്റ് പ്രവർത്തിപ്പിച്ചാൽ ബന്ധപ്പെട്ട ഉത്തരങ്ങൾ ലഭിക്കും

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ഉപയോഗിച്ച് OCR**

ചിത്രം വിശകലനം ചെയ്യുന്നതിന് പുറമേ, നമ്മുടെ ചിത്രം മുതൽ വിവരങ്ങൾ പുറത്തെടുക്കുകയും ചെയ്യാം. ഇത് മുൻപ് പൂർത്തിയാക്കാൻ നമുക്ക് സങ്കീർണമായ കോഡ് എഴുതേണ്ടി വന്ന OCR പ്രക്രിയയാണ്.

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

ഫലം

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. പല ചിത്രങ്ങളുടെ താരതമ്യം**

Phi-3 Vision പല ചിത്രങ്ങളുടെ താരതമ്യം പിന്തുണയ്ക്കുന്നു. ഈ മോഡൽ ഉപയോഗിച്ച് ചിത്രങ്ങൾ തമ്മിലുള്ള വ്യത്യാസങ്ങൾ കണ്ടെത്താൻ കഴിയും.

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

ഫലം

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അസൂചനം:
ഈ രേഖ AI തർജ്ജമ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജമിച്ചതാണ്. ഞങ്ങൾ കൃത്യതയിൽ പരിശ്രമിച്ചെങ്കിലും ഓട്ടോമേറ്റഡ് തർജ്ജമകളിൽ പിശകുകൾ അല്ലെങ്കിൽ അപൂര്‍ണ്ണതകൾ ഉണ്ടാകാനുള്ള സാധ്യതയുണ്ട് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂല ഭാഷയിലുള്ള രേഖയെയാണ് അധികാരപരമായ ഉറവിടമായി കരുതേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ തർജ്ജമ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ തർജ്ജമയുടെ ഉപയോഗത്താൽ ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->