# បង្កើតសំណុំទិន្នន័យរូបភាពដោយទាញយក DataSet ពី Hugging Face និងរូបភាពដែលទាក់ទង

### សង្ខេប

ស្គ្រីបនេះត្រៀមសំណុំទិន្នន័យសម្រាប់ការរៀនម៉ាស៊ីនដោយទាញយករូបភាពដែលត្រូវការ, បម្រាលបន្ទាត់ដែលការទាញយករូបភាពបរាជ័យ, ហើយរក្សាទុកសំណុំទិន្នន័យជាឯកសារ CSV។

### ផ្នែកដែលត្រូវមានជាមុន

មុនពេលរត់ស្គ្រីបនេះ, សូមប្រាកដថាអ្នកបានដំឡើងបណ្ណាល័យដូចខាងក្រោម៖ `Pandas`, `Datasets`, `requests`, `PIL`, និង `io`។ អ្នកត្រូវប្ដូរ `'Insert_Your_Dataset'` នៅជួរលេខ 2 ជាឈ្មោះសំណុំទិន្នន័យរបស់អ្នកពី Hugging Face។

បណ្ណាល័យដែលត្រូវការ៖

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### មុខងារ

ស្គ្រីបធ្វើការដូចតទៅ៖

1. ទាញយកសំណុំទិន្នន័យពី Hugging Face ដោយប្រើមុខងារ `load_dataset()`។
2. បំលែងសំណុំទិន្នន័យពី Hugging Face ទៅជា Pandas DataFrame សម្រាប់ការគ្រប់គ្រងដែលលែងខ្លាចដោយប្រើវិធីសាស្រ្ត `to_pandas()`។
3. បង្កើតថតឯកសារដើម្បីរក្សាសំណុំទិន្នន័យ និងរូបភាព។
4. បម្រាលបន្ទាត់ដែលការទាញយករូបភាពបរាជ័យដោយធ្វើសម្រង់ម្តងទៀតលើគ្រប់បន្ទាត់នៅក្នុង DataFrame, ទាញយករូបភាពដោយប្រើមុខងារ `download_image()` តែម្ដង, ហើយបន្ថែមបន្ទាត់ដែលត្រូវបានបម្រាលទៅ DataFrame ថ្មីហៅថា `filtered_rows`។
5. បង្កើត DataFrame ថ្មីមួយជាមួយបន្ទាត់ដែលបានបម្រាល ហើយរក្សាទុកទៅឯកសារដោយទ្រង់ទ្រាយ CSV។
6. បង្ហាញសារជូនដំណឹងថា សំណុំទិន្នន័យ និងរូបភាពត្រូវបានរក្សាទុកនៅកន្លែងណា។

### មុខងារផ្ទាល់ខ្លួន

មុខងារ `download_image()` ទាញយករូបភាពពី URL មួយ ហើយរក្សាទុកក្នុងកុំព្យូទ័រផ្ទាល់ដោយប្រើបណ្ណាល័យ Pillow Image Library (PIL) និងម៉ូឌុល `io`។ វាផ្តល់តម្លៃ True ប្រសិនបើការទាញយករូបភាពបានជោគជ័យ ហើយ False ប្រសិនបើបរាជ័យ។ មុខងារនេះក៏បង្ហាញករណីលើកលែងជាមួយសារបញ្ហាពេលការសំណូមពរបរាជ័យផងដែរ។

### វាជាដូចម្តេច

មុខងារ download_image ទទួលប៉ារ៉ាម៉ែត្រ​ពីរ៖ image_url ដែលជាអាសយដ្ឋាន URL នៃរូបភាពដែលត្រូវទាញយក និង save_path ដែលជាតំបន់ផ្លូវដែលរូបភាពនឹងត្រូវរក្សាទុក។

របៀបដំណើរការមុខងារ៖

វាបញ្ចូលដំណើរការដោយធ្វើសំណើ GET ទៅ image_url ដោយប្រើបច្ចេកវិទ្យា requests.get។ វាទាញយកទិន្នន័យរូបភាពពី URL។

ជួរដេក response.raise_for_status() ពិនិត្យមើលថា សំណើបានជោគជ័យមែនឬទេ។ ប្រសិនបើលេខកូដស្ថានភាពថាសំណើបញ្ហា (ឧ. 404 - មិនមាន), វានឹងលើកករណីលើកលែង។ វាជាការធានាថាយើងត្រូវបន្តទាញយករូបភាពបើសិនជាសំណើបានជោគជ័យប៉ុណ្ណោះ។

ទិន្នន័យរូបភាពបន្ទាប់ពីនោះត្រូវបានផ្ញើទៅវិធីសាស្រ្ត Image.open ពីម៉ូឌុល PIL (Python Imaging Library)។ វាបង្កើតអតិថិជន Image មួយពីទិន្នន័យរូបភាព។

ជួរដេក image.save(save_path) រក្សារូបភាពទៅតំបន់ផ្លូវ save_path ដែលត្រូវបានបញ្ជាក់។ save_path គួរសម្រួលឈ្មោះឯកសារនិងទ្រង់ទ្រាយ។

ចុងបញ្ចប់ មុខងារត្រឡប់តម្លៃ True ទាំងស្រុង ដើម្បីបញ្ជាក់ថារូបភាពត្រូវបានទាញយក និងរក្សាទុកដោយជោគជ័យ។ ប្រសិនបើមានករណីលើកលែងណាមួយកើតឡើង ក្នុងដំណើរការនេះ វាកាន់ករណីលើកលែង បោះពុម្ពសារបញ្ហា បញ្ជាក់ការបរាជ័យ ហើយត្រលប់តម្លៃ False។

មុខងារនេះមានប្រយោជន៍សម្រាប់ទាញយករូបភាពពី URL ហើយរក្សាទុកក្នុងកុំព្យូទ័រផ្ទាល់។ វាដោះស្រាយករណីកំហុសផ្សេងៗនៅពេលទាញយក ហើយផ្តល់មតិយោបល់ថាតើការទាញយកបានជោគជ័យឬអត់។

សម្គាល់ថាបណ្ណាល័យ requests ត្រូវបានប្រើសម្រាប់ធ្វើសំណើ HTTP, បណ្ណាល័យ PIL ត្រូវបានប្រើសម្រាប់ដំណើរការជាមួយរូបភាព និង BytesIO ត្រូវបានប្រើសម្រាប់គ្រប់គ្រងទិន្នន័យរូបភាពជា stream នៃបៃ។

### សេចក្ដីសន្និដ្ឋាន

ស្គ្រីបនេះផ្តល់នូវវិធីងាយស្រួលក្នុងការត្រៀមសំណុំទិន្នន័យសម្រាប់ការរៀនម៉ាស៊ីន ដោយទាញយករូបភាពដែលត្រូវការ, បម្រាលបន្ទាត់ដែលការទាញយករូបភាពបរាជ័យ, ហើយរក្សាទុកសំណុំទិន្នន័យជាឯកសារ CSV។

### ឧទាហរណ៍ស្គ្រីប

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
        response.raise_for_status()  # ពិនិត្យមើលថាតើសំណើបានជោគជ័យឬទេ
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# ដោនឡូដឃ្លាំងទិន្នន័យពី Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# បម្លែងឃ្លាំងទិន្នន័យ Hugging Face ទៅជា Pandas DataFrame
df = dataset['train'].to_pandas()


# បង្កើតថតឯកសារ សម្រាប់រក្សាទុកឃ្លាំងទិន្នន័យ និង រូបភាព
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# ត្រងជួរដេកដែលការទាញយករូបភាពបរាជ័យ
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# បង្កើត DataFrame ថ្មីជាមួយជួរដេកដែលបានត្រង
filtered_df = pd.DataFrame(filtered_rows)


# រក្សាទុកឃ្លាំងទិន្នន័យដែលបានធ្វើបច្ចុប្បន្នភាពទៅឯកសារ
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### កូដឧទាហរណ៍ទាញយក  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### ឧទាហរណ៍សំណុំទិន្នន័យ  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ចំណាំ**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំក្នុងការថែរក្សាសម្រួលភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវតិ្តអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសដើមគួរតែត្រូវបានគេពិចារណថាជាឆ្នាប់តំណាងផ្លូវការសម្រាប់ព័ត៍មាន។ សម្រាប់ព័ត៌មានសំខាន់ យើងសូមផ្តល់អនុសាសន៍ឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយមិនត្រូវដែលបានកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->