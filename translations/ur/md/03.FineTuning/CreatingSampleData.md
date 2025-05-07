<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-07T13:25:37+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ur"
}
-->
# Hugging Face سے DataSet اور متعلقہ تصاویر ڈاؤن لوڈ کرکے امیج ڈیٹا سیٹ بنائیں

### جائزہ

یہ اسکرپٹ مشین لرننگ کے لیے ایک ڈیٹا سیٹ تیار کرتا ہے جس میں ضروری تصاویر ڈاؤن لوڈ کی جاتی ہیں، ان قطاروں کو فلٹر کیا جاتا ہے جہاں تصاویر ڈاؤن لوڈ نہیں ہو پاتیں، اور ڈیٹا سیٹ کو CSV فائل کے طور پر محفوظ کیا جاتا ہے۔

### ضروریات

اس اسکرپٹ کو چلانے سے پہلے، یقینی بنائیں کہ درج ذیل لائبریریاں انسٹال ہوں: `Pandas`، `Datasets`، `requests`، `PIL`، اور `io`۔ آپ کو لائن 2 میں `'Insert_Your_Dataset'` کو اپنے Hugging Face کے ڈیٹا سیٹ کے نام سے تبدیل کرنا ہوگا۔

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

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` فنکشن Hugging Face سے ڈیٹا سیٹ ڈاؤن لوڈ کرتا ہے۔ یہ فنکشن URL سے تصویر ڈاؤن لوڈ کرتا ہے اور اسے Pillow Image Library (PIL) اور `io` ماڈیول کی مدد سے مقامی طور پر محفوظ کرتا ہے۔ اگر تصویر کامیابی سے ڈاؤن لوڈ ہو جائے تو یہ True واپس کرتا ہے، ورنہ False۔ اگر درخواست ناکام ہو جائے تو یہ ایرر میسج کے ساتھ ایک استثناء بھی پھینکتا ہے۔

### یہ کیسے کام کرتا ہے

download_image فنکشن دو پیرامیٹر لیتا ہے: image_url، جو ڈاؤن لوڈ کی جانے والی تصویر کا URL ہے، اور save_path، جو وہ راستہ ہے جہاں تصویر محفوظ کی جائے گی۔

فنکشن کی کام کرنے کی تفصیل:

یہ requests.get میتھڈ کے ذریعے image_url پر GET درخواست بھیج کر شروع ہوتا ہے۔ یہ URL سے تصویر کا ڈیٹا حاصل کرتا ہے۔

response.raise_for_status() لائن چیک کرتی ہے کہ درخواست کامیاب ہوئی یا نہیں۔ اگر ریسپانس کا اسٹیٹس کوڈ غلطی کی نشاندہی کرے (مثلاً 404 - Not Found)، تو یہ ایک استثناء پھینک دے گا۔ اس سے یقینی بنتا ہے کہ ہم صرف اس صورت میں تصویر ڈاؤن لوڈ کریں جب درخواست کامیاب ہو۔

تصویر کا ڈیٹا پھر PIL (Python Imaging Library) کے Image.open میتھڈ کو دیا جاتا ہے۔ یہ طریقہ تصویر کے ڈیٹا سے ایک Image آبجیکٹ بناتا ہے۔

image.save(save_path) لائن تصویر کو متعین save_path پر محفوظ کرتی ہے۔ save_path میں فائل کا مطلوبہ نام اور ایکسٹینشن شامل ہونا چاہیے۔

آخر میں، فنکشن True واپس کرتا ہے تاکہ یہ ظاہر ہو کہ تصویر کامیابی سے ڈاؤن لوڈ اور محفوظ ہو گئی ہے۔ اگر عمل کے دوران کوئی استثناء پیش آئے، تو اسے پکڑ کر ایک ایرر میسج پرنٹ کرتا ہے اور False واپس کرتا ہے۔

یہ فنکشن URL سے تصاویر ڈاؤن لوڈ کرنے اور انہیں مقامی طور پر محفوظ کرنے کے لیے مفید ہے۔ یہ ڈاؤن لوڈ کے دوران ممکنہ غلطیوں کو سنبھالتا ہے اور ڈاؤن لوڈ کی کامیابی یا ناکامی کی معلومات فراہم کرتا ہے۔

یہ بات قابل ذکر ہے کہ HTTP درخواستیں بنانے کے لیے requests لائبریری استعمال ہوتی ہے، تصاویر پر کام کرنے کے لیے PIL لائبریری استعمال ہوتی ہے، اور BytesIO کلاس تصویر کے ڈیٹا کو بائٹس کے سلسلے کے طور پر ہینڈل کرنے کے لیے استعمال ہوتی ہے۔

### نتیجہ

یہ اسکرپٹ مشین لرننگ کے لیے ڈیٹا سیٹ تیار کرنے کا ایک آسان طریقہ فراہم کرتا ہے جس میں ضروری تصاویر ڈاؤن لوڈ کی جاتی ہیں، ان قطاروں کو فلٹر کیا جاتا ہے جہاں تصاویر ڈاؤن لوڈ نہیں ہو پاتیں، اور ڈیٹا سیٹ کو CSV فائل کے طور پر محفوظ کیا جاتا ہے۔

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

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔