<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:45:11+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ur"
}
-->
# Hugging Face سے DataSet اور متعلقہ تصاویر ڈاؤن لوڈ کرکے امیج ڈیٹا سیٹ تیار کریں


### جائزہ

یہ اسکرپٹ مشین لرننگ کے لیے ایک ڈیٹا سیٹ تیار کرتا ہے جس میں ضروری تصاویر ڈاؤن لوڈ کی جاتی ہیں، ان قطاروں کو فلٹر کیا جاتا ہے جہاں تصویر ڈاؤن لوڈ ناکام ہو، اور ڈیٹا سیٹ کو CSV فائل کے طور پر محفوظ کیا جاتا ہے۔

### ضروریات

اس اسکرپٹ کو چلانے سے پہلے، یقینی بنائیں کہ درج ذیل لائبریریاں انسٹال ہوں: `Pandas`, `Datasets`, `requests`, `PIL`, اور `io`۔ آپ کو لائن 2 میں `'Insert_Your_Dataset'` کو اپنے Hugging Face کے ڈیٹا سیٹ کے نام سے تبدیل کرنا ہوگا۔

ضروری لائبریریاں:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### فعالیت

اسکرپٹ درج ذیل مراحل انجام دیتا ہے:

1. `load_dataset()` فنکشن کے ذریعے Hugging Face سے ڈیٹا سیٹ ڈاؤن لوڈ کرتا ہے۔
2. `to_pandas()` طریقہ استعمال کرکے Hugging Face کے ڈیٹا سیٹ کو آسانی سے سنبھالنے کے لیے Pandas DataFrame میں تبدیل کرتا ہے۔
3. ڈیٹا سیٹ اور تصاویر کو محفوظ کرنے کے لیے ڈائریکٹریز بناتا ہے۔
4. DataFrame کی ہر قطار پر چل کر، اپنی مرضی کے مطابق `download_image()` فنکشن کے ذریعے تصویر ڈاؤن لوڈ کرتا ہے، اور جہاں تصویر ڈاؤن لوڈ ناکام ہو، ان قطاروں کو فلٹر کرکے `filtered_rows` نامی نئے DataFrame میں شامل کرتا ہے۔
5. فلٹر کی گئی قطاروں کے ساتھ نیا DataFrame بناتا ہے اور اسے CSV فائل کے طور پر ڈسک پر محفوظ کرتا ہے۔
6. ایک پیغام پرنٹ کرتا ہے جو بتاتا ہے کہ ڈیٹا سیٹ اور تصاویر کہاں محفوظ کی گئی ہیں۔

### اپنی مرضی کا فنکشن

`download_image()` فنکشن ایک URL سے تصویر ڈاؤن لوڈ کرتا ہے اور اسے مقامی طور پر Pillow Image Library (PIL) اور `io` ماڈیول کا استعمال کرتے ہوئے محفوظ کرتا ہے۔ اگر تصویر کامیابی سے ڈاؤن لوڈ ہو جائے تو یہ True واپس کرتا ہے، ورنہ False۔ اگر درخواست ناکام ہو تو یہ فنکشن ایرر میسج کے ساتھ ایک استثناء بھی پھینکتا ہے۔

### یہ کیسے کام کرتا ہے

`download_image` فنکشن دو پیرامیٹرز لیتا ہے: image_url، جو ڈاؤن لوڈ کی جانے والی تصویر کا URL ہے، اور save_path، جو وہ راستہ ہے جہاں ڈاؤن لوڈ کی گئی تصویر محفوظ کی جائے گی۔

فنکشن کا طریقہ کار کچھ یوں ہے:

یہ requests.get طریقہ استعمال کرتے ہوئے image_url پر GET درخواست بھیجتا ہے۔ اس سے URL سے تصویر کا ڈیٹا حاصل ہوتا ہے۔

`response.raise_for_status()` لائن چیک کرتی ہے کہ درخواست کامیاب ہوئی یا نہیں۔ اگر جواب کا اسٹیٹس کوڈ کوئی خرابی ظاہر کرے (مثلاً 404 - Not Found)، تو یہ ایک استثناء پھینکے گا۔ اس سے یہ یقینی بنتا ہے کہ ہم صرف اس صورت میں تصویر ڈاؤن لوڈ کریں جب درخواست کامیاب ہو۔

تصویر کا ڈیٹا پھر PIL (Python Imaging Library) کے `Image.open` طریقہ کو دیا جاتا ہے۔ یہ طریقہ تصویر کے ڈیٹا سے ایک Image آبجیکٹ بناتا ہے۔

`image.save(save_path)` لائن تصویر کو مخصوص save_path پر محفوظ کرتی ہے۔ save_path میں مطلوبہ فائل کا نام اور توسیع شامل ہونی چاہیے۔

آخر میں، فنکشن True واپس کرتا ہے تاکہ ظاہر ہو کہ تصویر کامیابی سے ڈاؤن لوڈ اور محفوظ ہو گئی ہے۔ اگر عمل کے دوران کوئی استثناء پیش آئے، تو یہ اسے پکڑ کر ناکامی کا پیغام پرنٹ کرتا ہے اور False واپس کرتا ہے۔

یہ فنکشن URLs سے تصاویر ڈاؤن لوڈ کرنے اور انہیں مقامی طور پر محفوظ کرنے کے لیے مفید ہے۔ یہ ڈاؤن لوڈ کے دوران ممکنہ غلطیوں کو سنبھالتا ہے اور بتاتا ہے کہ ڈاؤن لوڈ کامیاب ہوا یا نہیں۔

یہ بات قابل ذکر ہے کہ requests لائبریری HTTP درخواستیں بھیجنے کے لیے استعمال ہوتی ہے، PIL لائبریری تصاویر کے ساتھ کام کرنے کے لیے، اور BytesIO کلاس تصویر کے ڈیٹا کو بائٹس کے بہاؤ کے طور پر سنبھالنے کے لیے استعمال ہوتی ہے۔



### نتیجہ

یہ اسکرپٹ مشین لرننگ کے لیے ایک آسان طریقہ فراہم کرتا ہے جس میں ضروری تصاویر ڈاؤن لوڈ کی جاتی ہیں، ان قطاروں کو فلٹر کیا جاتا ہے جہاں تصویر ڈاؤن لوڈ ناکام ہو، اور ڈیٹا سیٹ کو CSV فائل کے طور پر محفوظ کیا جاتا ہے۔

### نمونہ اسکرپٹ

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

### نمونہ کوڈ ڈاؤن لوڈ کریں  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### نمونہ ڈیٹا سیٹ  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔