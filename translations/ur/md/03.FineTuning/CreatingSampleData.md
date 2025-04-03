<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44a77501fe39a2eb2b776dfdf9953b67",
  "translation_date": "2025-04-03T08:00:36+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "ur"
}
-->
# ہگنگ فیس سے ڈیٹا سیٹ اور متعلقہ تصاویر ڈاؤنلوڈ کرکے امیج ڈیٹا سیٹ تیار کریں

### جائزہ

یہ اسکرپٹ مشین لرننگ کے لیے ڈیٹا سیٹ تیار کرنے کے لیے ضروری تصاویر ڈاؤنلوڈ کرتا ہے، ان قطاروں کو فلٹر کرتا ہے جہاں تصاویر ڈاؤنلوڈ نہیں ہوتیں، اور ڈیٹا سیٹ کو CSV فائل کے طور پر محفوظ کرتا ہے۔

### ضروری شرائط

اس اسکرپٹ کو چلانے سے پہلے، درج ذیل لائبریریوں کا انسٹال ہونا ضروری ہے: `Pandas`، `Datasets`، `requests`، `PIL`، اور `io`۔ آپ کو لائن 2 میں `'Insert_Your_Dataset'` کو ہگنگ فیس سے اپنے ڈیٹا سیٹ کے نام سے تبدیل کرنا ہوگا۔

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

اس اسکرپٹ میں درج ذیل اقدامات شامل ہیں:

1. ہگنگ فیس سے `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` فنکشن کا استعمال کرتے ہوئے ڈیٹا سیٹ ڈاؤنلوڈ کرنا۔  
2. `download_image()` فنکشن کسی URL سے تصویر ڈاؤنلوڈ کرتا ہے اور اسے مقامی طور پر Pillow Image Library (PIL) اور `io` ماڈیول کے ذریعے محفوظ کرتا ہے۔ اگر تصویر کامیابی سے ڈاؤنلوڈ ہو جائے تو یہ True واپس کرتا ہے، ورنہ False۔ اگر درخواست ناکام ہو تو فنکشن ایک استثنیٰ کے ساتھ غلطی کا پیغام بھی ظاہر کرتا ہے۔

### یہ کیسے کام کرتا ہے

`download_image` فنکشن دو پیرامیٹرز لیتا ہے: `image_url`، جو تصویر کے ڈاؤنلوڈ ہونے کا URL ہے، اور `save_path`، جہاں ڈاؤنلوڈ شدہ تصویر محفوظ کی جائے گی۔

فنکشن کی کام کرنے کی وضاحت:

1. یہ `requests.get` طریقہ استعمال کرتے ہوئے `image_url` پر ایک GET درخواست کرتا ہے۔ یہ URL سے تصویر کا ڈیٹا حاصل کرتا ہے۔  
2. `response.raise_for_status()` چیک کرتا ہے کہ آیا درخواست کامیاب رہی۔ اگر جواب کی اسٹیٹس کوڈ میں کوئی غلطی ہو (مثلاً، 404 - نہ ملا)، تو یہ استثنیٰ پیدا کرتا ہے۔ یہ یقینی بناتا ہے کہ تصویر کو ڈاؤنلوڈ کرنے کا عمل صرف کامیاب درخواست کی صورت میں جاری رہے۔  
3. تصویر کا ڈیٹا PIL ماڈیول کے `Image.open` طریقے کو منتقل کیا جاتا ہے، جو تصویر کا ایک آبجیکٹ بناتا ہے۔  
4. `image.save(save_path)` لائن تصویر کو دیے گئے `save_path` پر محفوظ کرتی ہے، جو مطلوبہ فائل کا نام اور ایکسٹینشن شامل کرے۔  
5. آخر میں، فنکشن True واپس کرتا ہے تاکہ ظاہر کرے کہ تصویر کامیابی سے ڈاؤنلوڈ اور محفوظ ہوئی۔ اگر عمل کے دوران کوئی استثنیٰ پیدا ہو، تو یہ اسے پکڑتا ہے، ناکامی کا پیغام ظاہر کرتا ہے، اور False واپس کرتا ہے۔

یہ فنکشن URLs سے تصاویر ڈاؤنلوڈ کرنے اور انہیں مقامی طور پر محفوظ کرنے کے لیے مفید ہے۔ یہ ڈاؤنلوڈ کے عمل کے دوران ممکنہ غلطیوں کو سنبھالتا ہے اور یہ بتاتا ہے کہ آیا ڈاؤنلوڈ کامیاب ہوا یا نہیں۔

یہ قابل ذکر ہے کہ `requests` لائبریری HTTP درخواستیں کرنے کے لیے استعمال ہوتی ہے، PIL لائبریری تصاویر کے ساتھ کام کرنے کے لیے استعمال ہوتی ہے، اور `BytesIO` کلاس تصویر کے ڈیٹا کو بائٹس کے سلسلے کے طور پر ہینڈل کرتی ہے۔

### نتیجہ

یہ اسکرپٹ مشین لرننگ کے لیے ڈیٹا سیٹ تیار کرنے کا ایک آسان طریقہ فراہم کرتا ہے، جس میں ضروری تصاویر ڈاؤنلوڈ کرنا، ان قطاروں کو فلٹر کرنا جہاں تصویر ڈاؤنلوڈ نہ ہو، اور ڈیٹا سیٹ کو CSV فائل کے طور پر محفوظ کرنا شامل ہے۔

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

### کوڈ ڈاؤنلوڈ کا نمونہ
[نیا ڈیٹا سیٹ اسکرپٹ تیار کریں](../../../../code/04.Finetuning/generate_dataset.py)

### ڈیٹا سیٹ کا نمونہ
[فائن ٹیوننگ کے ساتھ لورا مثال سے ڈیٹا سیٹ کا نمونہ](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔