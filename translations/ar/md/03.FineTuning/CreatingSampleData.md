<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-07T10:21:07+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ar"
}
-->
# إنشاء مجموعة بيانات الصور عن طريق تحميل DataSet من Hugging Face والصور المرتبطة بها

### نظرة عامة

يُعد هذا السكربت مجموعة بيانات لتعلم الآلة عن طريق تحميل الصور المطلوبة، وتصفيه الصفوف التي تفشل فيها عملية تحميل الصور، وحفظ مجموعة البيانات كملف CSV.

### المتطلبات المسبقة

قبل تشغيل هذا السكربت، تأكد من تثبيت المكتبات التالية: `Pandas`، `Datasets`، `requests`، `PIL`، و `io`. ستحتاج أيضًا إلى استبدال `'Insert_Your_Dataset'` في السطر 2 باسم مجموعة البيانات الخاصة بك من Hugging Face.

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

1. تحميل مجموعة البيانات من Hugging Face باستخدام الدالة `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` تقوم هذه الدالة بتحميل صورة من عنوان URL وحفظها محليًا باستخدام مكتبة Pillow Image (PIL) والوحدة `io`. تُعيد True إذا تم تحميل الصورة بنجاح، وFalse في حالة الفشل. كما تقوم الدالة برمي استثناء مع رسالة الخطأ عند فشل الطلب.

### كيف تعمل هذه الدالة

تأخذ دالة download_image معاملين: image_url، وهو عنوان URL للصورة التي سيتم تحميلها، وsave_path، وهو المسار الذي سيتم حفظ الصورة المحملة فيه.

إليك كيف تعمل الدالة:

تبدأ بإجراء طلب GET إلى image_url باستخدام طريقة requests.get. هذا يسترجع بيانات الصورة من العنوان.

السطر response.raise_for_status() يتحقق مما إذا كان الطلب ناجحًا. إذا كان رمز حالة الاستجابة يشير إلى خطأ (مثل 404 - غير موجود)، سيتم رفع استثناء. هذا يضمن أننا نستمر في تحميل الصورة فقط إذا كان الطلب ناجحًا.

يتم بعد ذلك تمرير بيانات الصورة إلى طريقة Image.open من وحدة PIL (مكتبة تصوير بايثون). هذه الطريقة تنشئ كائن Image من بيانات الصورة.

السطر image.save(save_path) يحفظ الصورة في المسار المحدد save_path. يجب أن يتضمن save_path اسم الملف والامتداد المطلوب.

أخيرًا، تُعيد الدالة True للدلالة على أن الصورة تم تحميلها وحفظها بنجاح. إذا حدث أي استثناء أثناء العملية، يتم التقاط الاستثناء، وطباعة رسالة خطأ تشير إلى الفشل، وإعادة False.

هذه الدالة مفيدة لتحميل الصور من عناوين URL وحفظها محليًا. تتعامل مع الأخطاء المحتملة أثناء عملية التحميل وتوفر ملاحظات حول نجاح أو فشل التحميل.

يجدر بالذكر أن مكتبة requests تُستخدم لإجراء طلبات HTTP، ومكتبة PIL تُستخدم للعمل مع الصور، وفئة BytesIO تُستخدم للتعامل مع بيانات الصورة كتيار من البايتات.

### الخاتمة

يوفر هذا السكربت طريقة ملائمة لتحضير مجموعة بيانات لتعلم الآلة عن طريق تحميل الصور المطلوبة، وتصفيه الصفوف التي تفشل فيها عملية تحميل الصور، وحفظ مجموعة البيانات كملف CSV.

### مثال على السكربت

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

### مثال على تحميل الكود  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### مثال على مجموعة البيانات  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.