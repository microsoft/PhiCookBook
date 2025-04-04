<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27cb0b952a2ef48c14b75dec13635acf",
  "translation_date": "2025-04-04T12:11:03+00:00",
  "source_file": "md\\01.Introduction\\03\\Vision_Inference.md",
  "language_code": "ja"
}
-->
# **ローカル環境でのPhi-3-Vision推論**

Phi-3-vision-128k-instructを使用すると、Phi-3は言語を理解するだけでなく、視覚的に世界を見ることができます。Phi-3-vision-128k-instructを通じて、OCR、表の解析、物体認識、画像の説明など、さまざまな視覚的な問題を解決することが可能です。以前は大量のデータトレーニングを必要としていたタスクを簡単に完了できます。以下は、Phi-3-vision-128k-instructによって引用された関連技術と応用シナリオです。

## **0. 準備**

使用する前に、以下のPythonライブラリがインストールされていることを確認してください（Python 3.10以上を推奨）。

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** を使用することを推奨し、flattenをインストールしてください。

```bash
pip install flash-attn --no-build-isolation
```

新しいNotebookを作成します。例を完了するには、以下の内容を先に作成することをお勧めします。

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

## **1. Phi-3-Visionで画像を解析する**

AIに画像の内容を解析し、関連する説明を生成させたい場合

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

Notebookで以下のスクリプトを実行することで、関連する回答を得ることができます。

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-VisionでのOCR**

画像を解析するだけでなく、画像から情報を抽出することも可能です。これはOCRのプロセスであり、以前は複雑なコードを書く必要がありました。

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

結果は以下の通りです。

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. 複数画像の比較**

Phi-3 Visionは複数画像の比較をサポートしています。このモデルを使用して、画像間の違いを見つけることができます。

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

結果は以下の通りです。

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤読について、当方は責任を負いません。