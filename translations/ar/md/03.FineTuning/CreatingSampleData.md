<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:44:47+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ar"
}
-->
# إنشاء مجموعة بيانات الصور عن طريق تنزيل DataSet من Hugging Face والصور المرتبطة بها


### نظرة عامة

يقوم هذا السكربت بتحضير مجموعة بيانات لتعلم الآلة من خلال تنزيل الصور المطلوبة، وتصفيه الصفوف التي تفشل فيها عملية تنزيل الصور، وحفظ مجموعة البيانات كملف CSV.

### المتطلبات الأساسية

قبل تشغيل هذا السكربت، تأكد من تثبيت المكتبات التالية: `Pandas`، `Datasets`، `requests`، `PIL`، و `io`. كما ستحتاج إلى استبدال `'Insert_Your_Dataset'` في السطر 2 باسم مجموعة البيانات الخاصة بك من Hugging Face.

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

1. تنزيل مجموعة البيانات من Hugging Face باستخدام الدالة `load_dataset()`.
2. تحويل مجموعة بيانات Hugging Face إلى Pandas DataFrame لتسهيل التعامل باستخدام الطريقة `to_pandas()`.
3. إنشاء مجلدات لحفظ مجموعة البيانات والصور.
4. تصفية الصفوف التي تفشل فيها عملية تنزيل الصور من خلال التكرار على كل صف في DataFrame، وتنزيل الصورة باستخدام الدالة المخصصة `download_image()`، وإضافة الصفوف المصفاة إلى DataFrame جديد يسمى `filtered_rows`.
5. إنشاء DataFrame جديد بالصفوف المصفاة وحفظه على القرص كملف CSV.
6. طباعة رسالة توضح مكان حفظ مجموعة البيانات والصور.

### الدالة المخصصة

تقوم الدالة `download_image()` بتنزيل صورة من عنوان URL وحفظها محليًا باستخدام مكتبة Pillow Image (PIL) ووحدة `io`. تعيد الدالة True إذا تم تنزيل الصورة بنجاح، و False خلاف ذلك. كما ترفع استثناء مع رسالة الخطأ عند فشل الطلب.

### كيف تعمل هذه الدالة

تأخذ دالة download_image معاملين: image_url، وهو عنوان URL للصورة المراد تنزيلها، و save_path، وهو المسار الذي سيتم حفظ الصورة التي تم تنزيلها فيه.

إليك كيف تعمل الدالة:

تبدأ بإجراء طلب GET إلى image_url باستخدام الطريقة requests.get. هذا يسترجع بيانات الصورة من العنوان.

يقوم السطر response.raise_for_status() بالتحقق مما إذا كان الطلب ناجحًا. إذا كان رمز حالة الاستجابة يشير إلى خطأ (مثل 404 - غير موجود)، فسيتم رفع استثناء. هذا يضمن أننا نستمر في تنزيل الصورة فقط إذا كان الطلب ناجحًا.

يتم تمرير بيانات الصورة بعد ذلك إلى الطريقة Image.open من وحدة PIL (مكتبة الصور في بايثون). هذه الطريقة تنشئ كائن Image من بيانات الصورة.

يقوم السطر image.save(save_path) بحفظ الصورة في المسار المحدد save_path. يجب أن يتضمن save_path اسم الملف والامتداد المطلوبين.

أخيرًا، تعيد الدالة True للدلالة على أن الصورة تم تنزيلها وحفظها بنجاح. إذا حدث أي استثناء أثناء العملية، فإنها تلتقط الاستثناء، وتطبع رسالة خطأ تشير إلى الفشل، وتعيد False.

تعتبر هذه الدالة مفيدة لتنزيل الصور من عناوين URL وحفظها محليًا. فهي تتعامل مع الأخطاء المحتملة أثناء عملية التنزيل وتوفر ملاحظات حول نجاح التنزيل أو فشله.

يجدر بالذكر أن مكتبة requests تُستخدم لإجراء طلبات HTTP، ومكتبة PIL تُستخدم للعمل مع الصور، وفئة BytesIO تُستخدم للتعامل مع بيانات الصورة كتيار من البايتات.



### الخلاصة

يوفر هذا السكربت طريقة مريحة لتحضير مجموعة بيانات لتعلم الآلة من خلال تنزيل الصور المطلوبة، وتصفيه الصفوف التي تفشل فيها عملية التنزيل، وحفظ مجموعة البيانات كملف CSV.

### سكربت نموذجي

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

### تحميل كود نموذجي  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### مجموعة بيانات نموذجية  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.