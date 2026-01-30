# **Local တွင် Phi-3-Vision ဖြင့် အနုညာတစစ်ဆေးခြင်း**

Phi-3-vision-128k-instruct သည် Phi-3 ကို ဘာသာစကားကိုသာမက ကမ္ဘာကို မြင်မြင်သာသာနားလည်နိုင်စေသည်။ Phi-3-vision-128k-instruct မှတဆင့် OCR, ဇယားခွဲခြမ်းစိတ်ဖြာခြင်း၊ အရာဝတ္ထုအသိအမှတ်ပြုခြင်း၊ ပုံဖော်ပြခြင်း စသည့် မျက်မြင်ဆိုင်ရာ ပြဿနာများကို ဖြေရှင်းနိုင်သည်။ ယခင်က အချက်အလက်များစွာဖြင့် လေ့ကျင့်ရသော အလုပ်များကိုလည်း လွယ်ကူစွာ ပြီးမြောက်စေနိုင်သည်။ အောက်တွင် Phi-3-vision-128k-instruct မှ ကိုးကားထားသော နည်းပညာများနှင့် အသုံးပြုမှုအခြေအနေများကို ဖော်ပြထားသည်။

## **0. ပြင်ဆင်မှု**

အသုံးပြုမည့်အချိန်မတိုင်မီ အောက်ပါ Python စာကြည့်တိုက်များကို ထည့်သွင်းထားကြောင်း သေချာစေပါ (Python 3.10+ ကို အကြံပြုသည်)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ကို အသုံးပြုရန်နှင့် flatten ကို ထည့်သွင်းရန် အကြံပြုသည်

```bash
pip install flash-attn --no-build-isolation
```

Notebook အသစ်တစ်ခု ဖန်တီးပါ။ ဥပမာများကို ပြီးမြောက်စေရန် အောက်ပါ အကြောင်းအရာများကို ပထမဦးစွာ ဖန်တီးရန် အကြံပြုသည်။

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

## **1. Phi-3-Vision ဖြင့် ပုံကို ခွဲခြမ်းစိတ်ဖြာခြင်း**

AI သည် ကျွန်ုပ်တို့၏ ပုံများ၏ အကြောင်းအရာကို ခွဲခြမ်းစိတ်ဖြာပြီး သက်ဆိုင်ရာ ဖော်ပြချက်များ ပေးနိုင်စေရန် ဆန္ဒရှိသည်

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

Notebook တွင် အောက်ပါ script ကို အကောင်အထည်ဖော်ခြင်းဖြင့် သက်ဆိုင်ရာ ဖြေကြားချက်များ ရရှိနိုင်သည်

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ဖြင့် OCR**

ပုံကို ခွဲခြမ်းစိတ်ဖြာခြင်းအပြင် ပုံမှ အချက်အလက်များကို ထုတ်ယူနိုင်သည်။ ယင်းသည် ယခင်က ရေးသားရခက်ခဲသော ကုဒ်များဖြင့် ပြီးမြောက်ခဲ့သည့် OCR လုပ်ငန်းစဉ်ဖြစ်သည်။

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

ရလဒ်မှာ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. ပုံများစွာကို နှိုင်းယှဉ်ခြင်း**

Phi-3 Vision သည် ပုံများစွာကို နှိုင်းယှဉ်နိုင်သည်။ ဤမော်ဒယ်ကို အသုံးပြု၍ ပုံများအကြား ကွာခြားချက်များကို ရှာဖွေနိုင်သည်။

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

ရလဒ်မှာ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။