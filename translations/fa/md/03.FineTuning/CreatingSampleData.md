# ایجاد مجموعه داده تصویری با دانلود DataSet از Hugging Face و تصاویر مرتبط


### مرور کلی

این اسکریپت یک مجموعه داده برای یادگیری ماشین آماده می‌کند با دانلود تصاویر مورد نیاز، حذف ردیف‌هایی که دانلود تصویر در آن‌ها موفقیت‌آمیز نبوده و ذخیره مجموعه داده به صورت فایل CSV.

### پیش‌نیازها

قبل از اجرای این اسکریپت، مطمئن شوید که کتابخانه‌های `Pandas`، `Datasets`، `requests`، `PIL` و `io` نصب شده‌اند. همچنین باید در خط ۲ مقدار `'Insert_Your_Dataset'` را با نام مجموعه داده خود از Hugging Face جایگزین کنید.

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

1. مجموعه داده را با استفاده از تابع `load_dataset()` از Hugging Face دانلود می‌کند.
2. مجموعه داده Hugging Face را به یک DataFrame از Pandas تبدیل می‌کند تا کار با آن آسان‌تر شود با استفاده از متد `to_pandas()`.
3. دایرکتوری‌هایی برای ذخیره مجموعه داده و تصاویر ایجاد می‌کند.
4. ردیف‌هایی که دانلود تصویر در آن‌ها موفق نبوده را با پیمایش هر ردیف در DataFrame، دانلود تصویر با استفاده از تابع سفارشی `download_image()` و افزودن ردیف‌های فیلتر شده به DataFrame جدیدی به نام `filtered_rows` حذف می‌کند.
5. یک DataFrame جدید با ردیف‌های فیلتر شده ایجاد کرده و آن را به صورت فایل CSV روی دیسک ذخیره می‌کند.
6. پیامی چاپ می‌کند که نشان می‌دهد مجموعه داده و تصاویر در کجا ذخیره شده‌اند.

### تابع سفارشی

تابع `download_image()` یک تصویر را از یک URL دانلود کرده و به صورت محلی با استفاده از کتابخانه Pillow (PIL) و ماژول `io` ذخیره می‌کند. اگر تصویر با موفقیت دانلود شود، مقدار True را برمی‌گرداند و در غیر این صورت False. همچنین اگر درخواست با خطا مواجه شود، یک استثنا با پیام خطا ایجاد می‌کند.

### این چگونه کار می‌کند

تابع download_image دو پارامتر می‌گیرد: image_url که آدرس URL تصویر برای دانلود است و save_path که مسیر ذخیره تصویر دانلود شده است.

نحوه عملکرد تابع به این صورت است:

ابتدا با استفاده از متد requests.get یک درخواست GET به image_url ارسال می‌کند. این داده‌های تصویر را از URL دریافت می‌کند.

خط response.raise_for_status() بررسی می‌کند که آیا درخواست موفقیت‌آمیز بوده است یا خیر. اگر کد وضعیت پاسخ نشان‌دهنده خطا باشد (مثلاً ۴۰۴ - پیدا نشد)، یک استثنا ایجاد می‌کند. این تضمین می‌کند که فقط در صورت موفقیت درخواست، دانلود تصویر انجام شود.

داده‌های تصویر سپس به متد Image.open از ماژول PIL (کتابخانه تصویربرداری پایتون) داده می‌شود. این متد یک شیء Image از داده‌های تصویر می‌سازد.

خط image.save(save_path) تصویر را در مسیر مشخص شده ذخیره می‌کند. save_path باید شامل نام فایل و پسوند مورد نظر باشد.

در نهایت، تابع مقدار True را برمی‌گرداند تا نشان دهد تصویر با موفقیت دانلود و ذخیره شده است. اگر در طول فرآیند هر استثنایی رخ دهد، آن را گرفته، پیام خطایی مبنی بر شکست چاپ می‌کند و مقدار False را برمی‌گرداند.

این تابع برای دانلود تصاویر از URLها و ذخیره آن‌ها به صورت محلی مفید است. همچنین خطاهای احتمالی در فرآیند دانلود را مدیریت کرده و بازخوردی درباره موفقیت یا عدم موفقیت دانلود ارائه می‌دهد.

شایان ذکر است که کتابخانه requests برای ارسال درخواست‌های HTTP استفاده می‌شود، کتابخانه PIL برای کار با تصاویر به کار می‌رود و کلاس BytesIO برای مدیریت داده‌های تصویر به صورت جریان بایت‌ها استفاده می‌شود.



### نتیجه‌گیری

این اسکریپت روشی آسان برای آماده‌سازی مجموعه داده برای یادگیری ماشین فراهم می‌کند با دانلود تصاویر مورد نیاز، حذف ردیف‌هایی که دانلود تصویر در آن‌ها موفق نبوده و ذخیره مجموعه داده به صورت فایل CSV.

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
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.