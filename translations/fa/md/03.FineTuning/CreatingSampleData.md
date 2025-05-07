<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-07T13:25:11+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "fa"
}
-->
# ایجاد مجموعه داده تصویری با دانلود داده‌ها از Hugging Face و تصاویر مرتبط


### مرور کلی

این اسکریپت با دانلود تصاویر مورد نیاز، حذف ردیف‌هایی که دانلود تصویر در آن‌ها ناموفق است و ذخیره مجموعه داده به صورت فایل CSV، یک مجموعه داده برای یادگیری ماشین آماده می‌کند.

### پیش‌نیازها

قبل از اجرای این اسکریپت، اطمینان حاصل کنید که کتابخانه‌های زیر نصب شده‌اند: `Pandas`، `Datasets`، `requests`، `PIL` و `io`. همچنین باید در خط ۲ مقدار `'Insert_Your_Dataset'` را با نام مجموعه داده خود از Hugging Face جایگزین کنید.

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

1. دانلود مجموعه داده از Hugging Face با استفاده از تابع `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` تصویری را از یک URL دانلود کرده و با استفاده از کتابخانه Pillow Image (PIL) و ماژول `io` به صورت محلی ذخیره می‌کند. اگر دانلود تصویر موفقیت‌آمیز باشد مقدار True و در غیر این صورت False برمی‌گرداند. همچنین در صورت شکست درخواست، با پیام خطا یک استثنا ایجاد می‌کند.

### چگونه این کار انجام می‌شود

تابع download_image دو پارامتر می‌گیرد: image_url که آدرس URL تصویر برای دانلود است و save_path که مسیر ذخیره تصویر دانلود شده را مشخص می‌کند.

نحوه عملکرد تابع به این صورت است:

ابتدا با استفاده از متد requests.get یک درخواست GET به image_url ارسال می‌کند تا داده‌های تصویر را دریافت کند.

خط response.raise_for_status() بررسی می‌کند که آیا درخواست موفق بوده است یا خیر. اگر کد وضعیت پاسخ نشان‌دهنده خطا (مثلاً ۴۰۴ - یافت نشد) باشد، استثنا ایجاد می‌کند. این اطمینان می‌دهد که فقط در صورت موفقیت درخواست، دانلود تصویر انجام شود.

داده‌های تصویر سپس به متد Image.open از کتابخانه PIL داده می‌شود تا یک شیء تصویر ساخته شود.

خط image.save(save_path) تصویر را در مسیر مشخص شده ذخیره می‌کند. مسیر save_path باید شامل نام فایل و پسوند مورد نظر باشد.

در نهایت، تابع مقدار True را بازمی‌گرداند تا نشان دهد تصویر با موفقیت دانلود و ذخیره شده است. اگر هرگونه استثنایی در طی فرآیند رخ دهد، آن را گرفته، پیام خطا را چاپ می‌کند و مقدار False را برمی‌گرداند.

این تابع برای دانلود تصاویر از URLها و ذخیره محلی آن‌ها مفید است. همچنین خطاهای احتمالی در هنگام دانلود را مدیریت کرده و بازخوردی درباره موفقیت یا شکست دانلود ارائه می‌دهد.

شایان ذکر است که کتابخانه requests برای ارسال درخواست‌های HTTP، کتابخانه PIL برای کار با تصاویر و کلاس BytesIO برای مدیریت داده‌های تصویر به صورت جریان بایت استفاده می‌شوند.



### نتیجه‌گیری

این اسکریپت راهی آسان برای آماده‌سازی مجموعه داده برای یادگیری ماشین فراهم می‌کند که شامل دانلود تصاویر مورد نیاز، حذف ردیف‌های ناموفق در دانلود تصویر و ذخیره مجموعه داده به صورت فایل CSV است.

### نمونه اسکریپت

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

### نمونه کد دانلود  
[اسکریپت ایجاد مجموعه داده جدید](../../../../code/04.Finetuning/generate_dataset.py)

### نمونه مجموعه داده  
[نمونه مجموعه داده از مثال finetuning با LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، استفاده از ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.