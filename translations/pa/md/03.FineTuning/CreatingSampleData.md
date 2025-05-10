<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:23:33+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "pa"
}
-->
# Hugging Face ਤੋਂ DataSet ਅਤੇ ਸੰਬੰਧਿਤ ਚਿੱਤਰਾਂ ਡਾਊਨਲੋਡ ਕਰਕੇ Image Data Set ਬਣਾਉਣਾ


### ਜਾਇਜ਼ਾ

ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਇੱਕ ਡਾਟਾਸੈੱਟ ਤਿਆਰ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿੱਥੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਫੇਲ ਹੁੰਦੇ ਹਨ ਉਹਨਾਂ ਕਤਾਰਾਂ ਨੂੰ ਫਿਲਟਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਡਾਟਾਸੈੱਟ ਨੂੰ CSV ਫਾਈਲ ਵਜੋਂ ਸੇਵ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### ਲੋੜੀਂਦੇ ਗੁਣ

ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਹਨ: `Pandas`, `Datasets`, `requests`, `PIL`, ਅਤੇ `io`। ਤੁਹਾਨੂੰ ਲਾਈਨ 2 ਵਿੱਚ `'Insert_Your_Dataset'` ਨੂੰ Hugging Face ਤੋਂ ਆਪਣੇ ਡਾਟਾਸੈੱਟ ਦੇ ਨਾਮ ਨਾਲ ਬਦਲਣਾ ਹੋਵੇਗਾ।

ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ:

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

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` ਫੰਕਸ਼ਨ Hugging Face ਤੋਂ ਡਾਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ। ਇਹ ਫੰਕਸ਼ਨ ਇੱਕ URL ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ Pillow Image Library (PIL) ਅਤੇ `io` ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸਨੂੰ ਲੋਕਲ ਸਟੋਰੇਜ ਵਿੱਚ ਸੇਵ ਕਰਦਾ ਹੈ। ਜੇ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਡਾਊਨਲੋਡ ਹੋ ਜਾਂਦਾ ਹੈ ਤਾਂ ਇਹ True ਵਾਪਸ ਕਰਦਾ ਹੈ, ਨਹੀਂ ਤਾਂ False। ਜੇਕਰ ਰਿਕਵੇਸਟ ਫੇਲ ਹੁੰਦੀ ਹੈ ਤਾਂ ਇਹ ਐਰਰ ਮੈਸੇਜ ਨਾਲ exception ਵੀ ਉਠਾਉਂਦਾ ਹੈ।

### ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

download_image ਫੰਕਸ਼ਨ ਦੋ ਪੈਰਾਮੀਟਰ ਲੈਂਦਾ ਹੈ: image_url, ਜੋ ਕਿ ਡਾਊਨਲੋਡ ਹੋਣ ਵਾਲੇ ਚਿੱਤਰ ਦਾ URL ਹੈ, ਅਤੇ save_path, ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਕੀਤਾ ਚਿੱਤਰ ਸੇਵ ਕੀਤਾ ਜਾਵੇਗਾ।

ਫੰਕਸ਼ਨ ਇਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦਾ ਹੈ:

ਇਹ requests.get ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ image_url 'ਤੇ GET ਰਿਕਵੇਸਟ ਭੇਜਦਾ ਹੈ। ਇਸ ਨਾਲ URL ਤੋਂ ਚਿੱਤਰ ਦਾ ਡੇਟਾ ਮਿਲਦਾ ਹੈ।

response.raise_for_status() ਲਾਈਨ ਜਾਂਚਦੀ ਹੈ ਕਿ ਰਿਕਵੇਸਟ ਸਫਲ ਸੀ ਜਾਂ ਨਹੀਂ। ਜੇ ਰਿਕਵੇਸਟ ਸਥਿਤੀ ਕੋਡ ਕਿਸੇ ਗਲਤੀ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ (ਜਿਵੇਂ 404 - Not Found), ਤਾਂ ਇਹ exception ਉਠਾ ਦੇਵੇਗਾ। ਇਸ ਨਾਲ ਯਕੀਨੀ ਬਣਦਾ ਹੈ ਕਿ ਅਸੀਂ ਸਿਰਫ ਸਫਲ ਰਿਕਵੇਸਟ ਦੀ ਸਥਿਤੀ ਵਿੱਚ ਹੀ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਾਂਗੇ।

ਚਿੱਤਰ ਦਾ ਡੇਟਾ ਫਿਰ PIL (Python Imaging Library) ਦੇ Image.open ਮੈਥਡ ਨੂੰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। ਇਹ ਮੈਥਡ ਚਿੱਤਰ ਡੇਟਾ ਤੋਂ ਇੱਕ Image ਆਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ।

image.save(save_path) ਲਾਈਨ ਚਿੱਤਰ ਨੂੰ ਦਿੱਤੇ ਗਏ save_path 'ਤੇ ਸੇਵ ਕਰਦੀ ਹੈ। save_path ਵਿੱਚ ਲੋੜੀਂਦਾ ਫਾਈਲ ਨਾਮ ਅਤੇ ਐਕਸਟੈਂਸ਼ਨ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।

ਅਖੀਰਕਾਰ, ਫੰਕਸ਼ਨ True ਵਾਪਸ ਕਰਦਾ ਹੈ ਇਹ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਡਾਊਨਲੋਡ ਅਤੇ ਸੇਵ ਹੋ ਗਿਆ। ਜੇਕਰ ਕਿਸੇ ਵੀ ਸਮੇਂ exception ਆਉਂਦੀ ਹੈ, ਤਾਂ ਇਹ exception ਨੂੰ ਕੈਚ ਕਰਕੇ ਫੇਲ੍ਹ ਹੋਣ ਦੀ ਜਾਣਕਾਰੀ ਦੇਣ ਵਾਲਾ ਐਰਰ ਮੈਸੇਜ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਅਤੇ False ਵਾਪਸ ਕਰਦਾ ਹੈ।

ਇਹ ਫੰਕਸ਼ਨ URL ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਲੋਕਲ ਸਟੋਰੇਜ ਵਿੱਚ ਸੇਵ ਕਰਨ ਲਈ ਬਹੁਤ ਲਾਭਦਾਇਕ ਹੈ। ਇਹ ਡਾਊਨਲੋਡ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਆ ਸਕਣ ਵਾਲੀਆਂ ਗਲਤੀਆਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ ਅਤੇ ਡਾਊਨਲੋਡ ਸਫਲ ਹੋਣ ਜਾਂ ਨਾ ਹੋਣ ਦੀ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ।

ਇੱਥੇ ਇਹ ਗੱਲ ਯਾਦ ਰੱਖਣਯੋਗ ਹੈ ਕਿ HTTP ਰਿਕਵੇਸਟ ਕਰਨ ਲਈ requests ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਚਿੱਤਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ PIL ਲਾਇਬ੍ਰੇਰੀ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ BytesIO ਕਲਾਸ ਚਿੱਤਰ ਡੇਟਾ ਨੂੰ ਬਾਈਟਸ ਦੇ ਸਟ੍ਰੀਮ ਵਜੋਂ ਸੰਭਾਲਣ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।



### ਨਤੀਜਾ

ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਡਾਟਾਸੈੱਟ ਤਿਆਰ ਕਰਨ ਦਾ ਸੌਖਾ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਫੇਲ ਹੁੰਦਾ ਹੈ ਉਹਨਾਂ ਕਤਾਰਾਂ ਨੂੰ ਹਟਾਇਆ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਡਾਟਾਸੈੱਟ ਨੂੰ CSV ਫਾਈਲ ਵਜੋਂ ਸੇਵ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

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

**ਇਨਕਾਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।