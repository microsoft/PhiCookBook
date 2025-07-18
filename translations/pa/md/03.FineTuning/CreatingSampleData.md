<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:47:27+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "pa"
}
-->
# Hugging Face ਤੋਂ DataSet ਅਤੇ ਸੰਬੰਧਿਤ ਚਿੱਤਰਾਂ ਡਾਊਨਲੋਡ ਕਰਕੇ ਚਿੱਤਰ ਡਾਟਾ ਸੈੱਟ ਬਣਾਓ

### ਝਲਕ

ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਡਾਟਾਸੈੱਟ ਤਿਆਰ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿੱਥੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਫੇਲ ਹੁੰਦਾ ਹੈ ਉਹਨਾਂ ਕਤਾਰਾਂ ਨੂੰ ਛਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਡਾਟਾਸੈੱਟ ਨੂੰ CSV ਫਾਇਲ ਵਜੋਂ ਸੇਵ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### ਲੋੜੀਂਦੇ ਸਾਧਨ

ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਹਨ: `Pandas`, `Datasets`, `requests`, `PIL`, ਅਤੇ `io`। ਤੁਹਾਨੂੰ ਲਾਈਨ 2 ਵਿੱਚ `'Insert_Your_Dataset'` ਨੂੰ Hugging Face ਤੋਂ ਆਪਣੇ ਡਾਟਾਸੈੱਟ ਦੇ ਨਾਮ ਨਾਲ ਬਦਲਣਾ ਹੋਵੇਗਾ।

ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### ਕਾਰਜਕੁਸ਼ਲਤਾ

ਸਕ੍ਰਿਪਟ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮ ਕਰਦਾ ਹੈ:

1. `load_dataset()` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Hugging Face ਤੋਂ ਡਾਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ।
2. Hugging Face ਡਾਟਾਸੈੱਟ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਸੰਭਾਲਣ ਲਈ `to_pandas()` ਮੈਥਡ ਨਾਲ Pandas DataFrame ਵਿੱਚ ਬਦਲਦਾ ਹੈ।
3. ਡਾਟਾਸੈੱਟ ਅਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਸੇਵ ਕਰਨ ਲਈ ਡਾਇਰੈਕਟਰੀਆਂ ਬਣਾਉਂਦਾ ਹੈ।
4. DataFrame ਵਿੱਚ ਹਰ ਕਤਾਰ 'ਤੇ ਜਾ ਕੇ, ਕਸਟਮ `download_image()` ਫੰਕਸ਼ਨ ਨਾਲ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਫੇਲ ਹੁੰਦਾ ਹੈ ਉਹ ਕਤਾਰਾਂ ਨੂੰ ਛਾਣ ਕੇ ਨਵੇਂ DataFrame `filtered_rows` ਵਿੱਚ ਜੋੜਦਾ ਹੈ।
5. ਛਾਣੀਆਂ ਹੋਈਆਂ ਕਤਾਰਾਂ ਨਾਲ ਨਵਾਂ DataFrame ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਇਸ ਨੂੰ CSV ਫਾਇਲ ਵਜੋਂ ਡਿਸਕ 'ਤੇ ਸੇਵ ਕਰਦਾ ਹੈ।
6. ਇੱਕ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਜੋ ਦੱਸਦਾ ਹੈ ਕਿ ਡਾਟਾਸੈੱਟ ਅਤੇ ਚਿੱਤਰ ਕਿੱਥੇ ਸੇਵ ਕੀਤੇ ਗਏ ਹਨ।

### ਕਸਟਮ ਫੰਕਸ਼ਨ

`download_image()` ਫੰਕਸ਼ਨ ਇੱਕ URL ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ Pillow Image Library (PIL) ਅਤੇ `io` ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸਨੂੰ ਲੋਕਲ ਸੇਵ ਕਰਦਾ ਹੈ। ਜੇ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਡਾਊਨਲੋਡ ਹੋ ਜਾਂਦਾ ਹੈ ਤਾਂ ਇਹ True ਵਾਪਸ ਕਰਦਾ ਹੈ, ਨਹੀਂ ਤਾਂ False। ਜੇ ਡਾਊਨਲੋਡ ਦੌਰਾਨ ਕੋਈ ਗਲਤੀ ਆਉਂਦੀ ਹੈ ਤਾਂ ਇਹ ਗਲਤੀ ਦਾ ਸੁਨੇਹਾ ਦੇ ਕੇ exception ਉਠਾਉਂਦਾ ਹੈ।

### ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

`download_image` ਫੰਕਸ਼ਨ ਦੋ ਪੈਰਾਮੀਟਰ ਲੈਂਦਾ ਹੈ: image_url, ਜੋ ਚਿੱਤਰ ਦਾ URL ਹੈ ਜਿਸਨੂੰ ਡਾਊਨਲੋਡ ਕਰਨਾ ਹੈ, ਅਤੇ save_path, ਜੋ ਉਸ ਜਗ੍ਹਾ ਦਾ ਪਤਾ ਹੈ ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਕੀਤਾ ਚਿੱਤਰ ਸੇਵ ਕੀਤਾ ਜਾਵੇਗਾ।

ਫੰਕਸ਼ਨ ਇਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦਾ ਹੈ:

ਇਹ requests.get ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ image_url 'ਤੇ GET ਰਿਕਵੇਸਟ ਭੇਜਦਾ ਹੈ। ਇਸ ਨਾਲ URL ਤੋਂ ਚਿੱਤਰ ਦਾ ਡਾਟਾ ਮਿਲਦਾ ਹੈ।

response.raise_for_status() ਲਾਈਨ ਜਾਂਚਦੀ ਹੈ ਕਿ ਰਿਕਵੇਸਟ ਸਫਲ ਸੀ ਜਾਂ ਨਹੀਂ। ਜੇ ਸਟੇਟਸ ਕੋਡ ਵਿੱਚ ਕੋਈ ਗਲਤੀ ਹੈ (ਜਿਵੇਂ 404 - Not Found), ਤਾਂ ਇਹ exception ਉਠਾ ਦੇਵੇਗਾ। ਇਸ ਨਾਲ ਇਹ ਯਕੀਨੀ ਬਣਦਾ ਹੈ ਕਿ ਸਿਰਫ ਸਫਲ ਰਿਕਵੇਸਟ 'ਤੇ ਹੀ ਅੱਗੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕੀਤਾ ਜਾਵੇ।

ਚਿੱਤਰ ਦਾ ਡਾਟਾ ਫਿਰ PIL (Python Imaging Library) ਦੇ Image.open ਮੈਥਡ ਨੂੰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ, ਜੋ ਚਿੱਤਰ ਡਾਟਾ ਤੋਂ ਇੱਕ Image ਆਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ।

image.save(save_path) ਲਾਈਨ ਚਿੱਤਰ ਨੂੰ ਦਿੱਤੇ ਗਏ save_path 'ਤੇ ਸੇਵ ਕਰਦੀ ਹੈ। save_path ਵਿੱਚ ਫਾਇਲ ਦਾ ਨਾਮ ਅਤੇ ਐਕਸਟੈਂਸ਼ਨ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

ਅਖੀਰ ਵਿੱਚ, ਫੰਕਸ਼ਨ True ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਦੱਸਦਾ ਹੈ ਕਿ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਡਾਊਨਲੋਡ ਅਤੇ ਸੇਵ ਹੋ ਗਿਆ। ਜੇ ਕਿਸੇ ਵੀ ਸਮੇਂ exception ਆਉਂਦੀ ਹੈ, ਤਾਂ ਇਹ exception ਨੂੰ ਕੈਚ ਕਰਦਾ ਹੈ, ਗਲਤੀ ਦਾ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਅਤੇ False ਵਾਪਸ ਕਰਦਾ ਹੈ।

ਇਹ ਫੰਕਸ਼ਨ URLs ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਲੋਕਲ ਸੇਵ ਕਰਨ ਲਈ ਬਹੁਤ ਲਾਭਦਾਇਕ ਹੈ। ਇਹ ਡਾਊਨਲੋਡ ਦੌਰਾਨ ਆ ਸਕਣ ਵਾਲੀਆਂ ਗਲਤੀਆਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ ਅਤੇ ਡਾਊਨਲੋਡ ਸਫਲ ਹੋਣ ਜਾਂ ਨਾ ਹੋਣ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ।

ਇਹ ਯਾਦ ਰੱਖਣ ਯੋਗ ਹੈ ਕਿ requests ਲਾਇਬ੍ਰੇਰੀ HTTP ਰਿਕਵੇਸਟ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, PIL ਲਾਇਬ੍ਰੇਰੀ ਚਿੱਤਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਹੈ, ਅਤੇ BytesIO ਕਲਾਸ ਚਿੱਤਰ ਡਾਟਾ ਨੂੰ ਬਾਈਟਸ ਦੇ ਸਟ੍ਰੀਮ ਵਜੋਂ ਸੰਭਾਲਣ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

### ਨਤੀਜਾ

ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਡਾਟਾਸੈੱਟ ਤਿਆਰ ਕਰਨ ਦਾ ਆਸਾਨ ਤਰੀਕਾ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਫੇਲ ਹੁੰਦਾ ਹੈ ਉਹਨਾਂ ਕਤਾਰਾਂ ਨੂੰ ਛਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਡਾਟਾਸੈੱਟ ਨੂੰ CSV ਫਾਇਲ ਵਜੋਂ ਸੇਵ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### ਨਮੂਨਾ ਸਕ੍ਰਿਪਟ

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### ਨਮੂਨਾ ਕੋਡ ਡਾਊਨਲੋਡ  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### ਨਮੂਨਾ ਡਾਟਾ ਸੈੱਟ  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।