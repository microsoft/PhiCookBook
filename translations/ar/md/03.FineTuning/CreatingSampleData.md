<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-03-27T13:34:37+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "ar"
}
-->
# إنشاء مجموعة بيانات الصور عن طريق تنزيل مجموعة البيانات من Hugging Face والصور المرتبطة بها

### نظرة عامة

يُعد هذا السكربت مجموعة بيانات لتعلم الآلة عن طريق تنزيل الصور المطلوبة، تصفية الصفوف التي تفشل فيها عمليات تنزيل الصور، وحفظ مجموعة البيانات كملف CSV.

### المتطلبات الأساسية

قبل تشغيل هذا السكربت، تأكد من تثبيت المكتبات التالية: `Pandas`، `Datasets`، `requests`، `PIL`، و`io`. ستحتاج أيضًا إلى استبدال `'Insert_Your_Dataset'` في السطر 2 باسم مجموعة البيانات الخاصة بك من Hugging Face.

المكتبات المطلوبة:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### الوظائف

يقوم السكربت بالخطوات التالية:

1. تنزيل مجموعة البيانات من Hugging Face باستخدام `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.
2. تصفية الصفوف التي فشلت فيها عملية تنزيل الصور.
3. حفظ مجموعة البيانات النهائية كملف CSV.

### كيف يعمل هذا السكربت

تأخذ وظيفة download_image وسيطين: image_url، وهو رابط URL للصورة المراد تنزيلها، وsave_path، وهو المسار الذي سيتم حفظ الصورة فيه.

إليك كيفية عمل الوظيفة:

- تبدأ بإجراء طلب GET إلى image_url باستخدام طريقة requests.get. يقوم هذا بجلب بيانات الصورة من الرابط.
- يتحقق السطر response.raise_for_status() مما إذا كان الطلب ناجحًا. إذا أشار رمز الحالة إلى وجود خطأ (مثل 404 - لم يتم العثور على المورد)، سيتم إثارة استثناء. يضمن هذا أننا نتابع تنزيل الصورة فقط إذا كان الطلب ناجحًا.
- يتم تمرير بيانات الصورة بعد ذلك إلى طريقة Image.open من مكتبة PIL (Python Imaging Library). تقوم هذه الطريقة بإنشاء كائن صورة من بيانات الصورة.
- يحفظ السطر image.save(save_path) الصورة في المسار المحدد save_path. يجب أن يتضمن save_path اسم الملف المرغوب وامتداده.
- أخيرًا، تُرجع الوظيفة True للإشارة إلى أن الصورة تم تنزيلها وحفظها بنجاح. إذا حدث أي استثناء أثناء العملية، يتم التقاط الاستثناء، وطباعة رسالة خطأ تشير إلى الفشل، وتُرجع الوظيفة False.

هذه الوظيفة مفيدة لتنزيل الصور من الروابط وحفظها محليًا. تتعامل مع الأخطاء المحتملة أثناء عملية التنزيل وتوفر تغذية راجعة حول نجاح التنزيل.

من الجدير بالذكر أن مكتبة requests تُستخدم لإجراء الطلبات HTTP، ومكتبة PIL تُستخدم للتعامل مع الصور، وفئة BytesIO تُستخدم للتعامل مع بيانات الصورة كتيار من البايتات.

### الخاتمة

يوفر هذا السكربت طريقة مريحة لإعداد مجموعة بيانات لتعلم الآلة عن طريق تنزيل الصور المطلوبة، تصفية الصفوف التي تفشل فيها عمليات تنزيل الصور، وحفظ مجموعة البيانات كملف CSV.

### سكربت تجريبي

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

### تنزيل الكود التجريبي
[إنشاء سكربت مجموعة بيانات جديدة](../../../../code/04.Finetuning/generate_dataset.py)

### مجموعة بيانات تجريبية
[مثال على مجموعة بيانات من التجربة الخاصة بـ LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**إخلاء مسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.