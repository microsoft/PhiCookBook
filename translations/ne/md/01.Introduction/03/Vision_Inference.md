<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-07-16T21:37:23+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "ne"
}
-->
# **स्थानीयमा Inference Phi-3-Vision**

Phi-3-vision-128k-instruct ले Phi-3 लाई केवल भाषा बुझ्न मात्र होइन, दृश्य रूपमा संसार हेर्न पनि सक्षम बनाउँछ। Phi-3-vision-128k-instruct मार्फत, हामी विभिन्न दृश्य समस्याहरू समाधान गर्न सक्छौं, जस्तै OCR, तालिका विश्लेषण, वस्तु पहिचान, तस्वीर वर्णन आदि। पहिले धेरै डाटा प्रशिक्षण आवश्यक पर्ने कार्यहरू अब सजिलै पूरा गर्न सकिन्छ। तल Phi-3-vision-128k-instruct द्वारा उद्धृत सम्बन्धित प्रविधिहरू र अनुप्रयोग परिदृश्यहरू छन्।

## **0. तयारी**

कृपया प्रयोग गर्नु अघि तलका Python पुस्तकालयहरू स्थापना गरिएको छ भनी सुनिश्चित गर्नुहोस् (Python 3.10+ सिफारिस गरिएको छ)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** प्रयोग गर्न सिफारिस गरिन्छ र flatten स्थापना गर्नुहोस्

```bash
pip install flash-attn --no-build-isolation
```

नयाँ Notebook सिर्जना गर्नुहोस्। उदाहरणहरू पूरा गर्न, तलको सामग्री पहिले तयार गर्नु सिफारिस गरिन्छ।

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

## **1. Phi-3-Vision सँग तस्वीर विश्लेषण**

हामी चाहन्छौं कि AI ले हाम्रो तस्वीरहरूको सामग्री विश्लेषण गर्न र सम्बन्धित विवरणहरू दिन सकोस्

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

Notebook मा तलको स्क्रिप्ट चलाएर सम्बन्धित उत्तरहरू प्राप्त गर्न सकिन्छ

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision सँग OCR**

तस्वीर विश्लेषण बाहेक, हामी तस्वीरबाट जानकारी पनि निकाल्न सक्छौं। यो OCR प्रक्रिया हो जुन पहिले जटिल कोड लेखेर मात्र पूरा गर्न सकिन्थ्यो।

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

परिणाम यस्तो हुन्छ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. धेरै तस्वीरहरूको तुलना**

Phi-3 Vision ले धेरै तस्वीरहरूको तुलना समर्थन गर्दछ। हामी यस मोडेललाई तस्वीरहरू बीचको भिन्नता पत्ता लगाउन प्रयोग गर्न सक्छौं।

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

परिणाम यस्तो हुन्छ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।