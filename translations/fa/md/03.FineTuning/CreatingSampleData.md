<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-03-27T13:35:39+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "fa"
}
-->
# ایجاد مجموعه داده تصویری با دانلود مجموعه داده از Hugging Face و تصاویر مرتبط

### نمای کلی

این اسکریپت مجموعه داده‌ای را برای یادگیری ماشین آماده می‌کند. این کار با دانلود تصاویر مورد نیاز، حذف سطرهایی که دانلود تصاویر در آن‌ها ناموفق بوده، و ذخیره مجموعه داده به صورت فایل CSV انجام می‌شود.

### پیش‌نیازها

قبل از اجرای این اسکریپت، مطمئن شوید که کتابخانه‌های زیر نصب شده‌اند: `Pandas`، `Datasets`، `requests`، `PIL`، و `io`. همچنین لازم است `'Insert_Your_Dataset'` در خط ۲ با نام مجموعه داده شما از Hugging Face جایگزین شود.

کتابخانه‌های مورد نیاز:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### عملکرد

این اسکریپت مراحل زیر را انجام می‌دهد:

1. مجموعه داده را از Hugging Face با استفاده از `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` دانلود می‌کند. تابع `download_image()` تصویر را از یک URL دانلود کرده و به صورت محلی با استفاده از کتابخانه Pillow Image Library (PIL) و ماژول `io` ذخیره می‌کند. این تابع در صورتی که تصویر با موفقیت دانلود شود، مقدار True بازمی‌گرداند و در غیر این صورت مقدار False را بازمی‌گرداند. همچنین اگر درخواست دانلود ناموفق باشد، استثنایی با پیام خطا ایجاد می‌کند.

### چگونه کار می‌کند

تابع `download_image` دو پارامتر دریافت می‌کند: `image_url` که URL تصویر برای دانلود است، و `save_path` که مسیر ذخیره‌سازی تصویر دانلود شده را مشخص می‌کند.

نحوه عملکرد تابع به شرح زیر است:

ابتدا با استفاده از متد `requests.get` یک درخواست GET به `image_url` ارسال می‌کند تا داده‌های تصویر از URL دریافت شود.

خط `response.raise_for_status()` بررسی می‌کند که آیا درخواست موفق بوده است یا خیر. اگر کد وضعیت پاسخ نشان‌دهنده خطا باشد (مانند 404 - پیدا نشد)، استثنا ایجاد می‌شود. این خط اطمینان می‌دهد که فقط در صورت موفقیت‌آمیز بودن درخواست، فرآیند دانلود تصویر ادامه پیدا می‌کند.

داده‌های تصویر سپس به متد `Image.open` از ماژول PIL (کتابخانه تصویری پایتون) ارسال می‌شود. این متد یک شیء تصویر از داده‌های تصویر ایجاد می‌کند.

خط `image.save(save_path)` تصویر را در مسیر مشخص‌شده ذخیره می‌کند. مسیر ذخیره‌سازی باید شامل نام فایل و پسوند مورد نظر باشد.

در نهایت، تابع مقدار True را بازمی‌گرداند تا نشان دهد که تصویر با موفقیت دانلود و ذخیره شده است. اگر در طول فرآیند هرگونه استثنایی رخ دهد، آن را دریافت کرده، پیام خطایی چاپ می‌کند که نشان‌دهنده شکست است، و مقدار False بازمی‌گرداند.

این تابع برای دانلود تصاویر از URLها و ذخیره آن‌ها به صورت محلی مفید است. همچنین خطاهای احتمالی در فرآیند دانلود را مدیریت کرده و بازخوردی در مورد موفقیت یا شکست دانلود ارائه می‌دهد.

شایان ذکر است که کتابخانه `requests` برای ارسال درخواست‌های HTTP استفاده می‌شود، کتابخانه PIL برای کار با تصاویر به کار می‌رود، و کلاس `BytesIO` برای مدیریت داده‌های تصویر به عنوان جریان بایت استفاده می‌شود.

### نتیجه‌گیری

این اسکریپت راهی مناسب برای آماده‌سازی مجموعه داده برای یادگیری ماشین ارائه می‌دهد. این کار با دانلود تصاویر مورد نیاز، حذف سطرهایی که دانلود تصاویر در آن‌ها ناموفق بوده، و ذخیره مجموعه داده به صورت فایل CSV انجام می‌شود.

### اسکریپت نمونه

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

### دانلود کد نمونه
[اسکریپت ایجاد مجموعه داده جدید](../../../../code/04.Finetuning/generate_dataset.py)

### نمونه مجموعه داده
[نمونه مجموعه داده از مثال ریزتنظیم با LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت ترجمه را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌ها باشند. سند اصلی به زبان اصلی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.