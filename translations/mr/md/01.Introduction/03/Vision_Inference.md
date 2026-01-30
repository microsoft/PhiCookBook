# **स्थानिक पातळीवर Phi-3-Vision चे इनफरन्स**

Phi-3-vision-128k-instruct मुळे Phi-3 केवळ भाषा समजून घेऊ शकत नाही, तर तो जगाला दृष्टीकोनातूनही पाहू शकतो. Phi-3-vision-128k-instruct च्या माध्यमातून, आपण विविध दृष्टीसंबंधी समस्या सोडवू शकतो, जसे की OCR, टेबल विश्लेषण, ऑब्जेक्ट ओळख, चित्राचे वर्णन इत्यादी. पूर्वी ज्यासाठी मोठ्या प्रमाणात डेटा प्रशिक्षणाची गरज होती, ते आता सहजपणे पूर्ण करता येते. खाली Phi-3-vision-128k-instruct द्वारे संदर्भित तंत्रज्ञान आणि वापराच्या परिस्थिती दिल्या आहेत.

## **0. तयारी**

कृपया वापरण्यापूर्वी खालील Python लायब्ररी इन्स्टॉल केल्या आहेत याची खात्री करा (Python 3.10+ वापरण्याची शिफारस केली जाते)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** वापरण्याची आणि flatten इन्स्टॉल करण्याची शिफारस केली जाते

```bash
pip install flash-attn --no-build-isolation
```

नवीन Notebook तयार करा. उदाहरणे पूर्ण करण्यासाठी, प्रथम खालील सामग्री तयार करणे शिफारसीय आहे.

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

## **1. Phi-3-Vision ने प्रतिमा विश्लेषण करा**

आपण हवे आहे की AI आपल्या चित्रांच्या सामग्रीचे विश्लेषण करू शकेल आणि संबंधित वर्णने देऊ शकेल

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

Notebook मध्ये खालील स्क्रिप्ट चालवून आपण संबंधित उत्तरं मिळवू शकतो

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision सह OCR**

प्रतिमा विश्लेषण करण्याशिवाय, आपण प्रतिमेतून माहितीही काढू शकतो. हा OCR प्रक्रिया आहे, ज्यासाठी पूर्वी आपल्याला गुंतागुंतीचा कोड लिहावा लागायचा.

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

परिणाम असा आहे

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. अनेक प्रतिमांची तुलना**

Phi-3 Vision अनेक प्रतिमांची तुलना करण्यास समर्थन देते. आपण या मॉडेलचा वापर करून प्रतिमांमधील फरक शोधू शकतो.

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

परिणाम असा आहे

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.