<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aacf82e3da702afd8469bba99b662509",
  "translation_date": "2025-04-04T12:59:11+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi4\\GenProjectCode\\README.md",
  "language_code": "ja"
}
-->
## **Phi-4-mini-mmを使ったコード生成**

Phi-4-miniはPhiファミリーの強力なコーディング能力を継続しています。Promptを使ってコーディングに関する質問をすることができます。もちろん、強力な推論能力を追加したことで、より強力なコーディング能力を持つようになり、例えば要求に応じてプロジェクトを生成することが可能です。以下のように、要求に基づいてプロジェクトを生成する例があります。

### **要求**

ショッピングカートアプリを作成する

- 以下のメソッドを含むAPI Restを作成する:
    - ページオフセットとリミットを使用してビールのリストを取得する。
    - IDでビールの詳細を取得する。
    - 名前、説明、タグライン、フードペアリング、価格でビールを検索する。
- メインページに製品のリストを作成する。
    - 製品をフィルターするための検索バーを作成する。
    - ユーザーが製品をクリックすると詳細ページに移動する。
- （オプション）価格で製品をフィルターするためのスライサーを作成する。
- ショッピングカートを作成する。
    - 製品をカートに追加する。
    - 製品をカートから削除する。
    - カート内の製品の合計金額を計算する。

### **サンプルコード - Python**

```python

import requests
import torch
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-mini-mm-instruct'

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

requirement = """

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Get a list of beers using page offset and limit.
    - Get beer details by id.
    - Search for beer by name, description, tagline, food pairings, and price.
- Create a list of products on the main page.
    - Create a search bar to filter products.
    - Navigate to the description page when the user clicks on a product.
- (Optional) Slicer to filter products by price.
- Create a shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products in the cart."""

note = """ 

            Note:

            1. Use Python Flask to create a Repository pattern based on the following structure to generate the files

            ｜- models
            ｜- controllers
            ｜- repositories
            ｜- views

            2. For the view page, please use SPA + VueJS + TypeScript to build

            3. Firstly use markdown to output the generated project structure (including directories and files), and then generate the  file names and corresponding codes step by step, output like this 

               ## Project Structure

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Frontend
                 
                   #### `templates/index.html`
                   ```html

                   ```
                   ......."""

prompt = f'{user_prompt}Please create a project with Python and Flask according to the following requirements：\n{requirement}{note}{prompt_suffix}{assistant_prompt}'

inputs = processor(prompt, images=None, return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=2048,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。原文（元の言語で記載された文書）を信頼できる情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用に起因する誤解や誤認について、当方は一切責任を負いません。