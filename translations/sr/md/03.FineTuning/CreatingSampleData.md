<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:52:29+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sr"
}
-->
# Генерисање скупа података слика преузимањем DataSet-а са Hugging Face и повезаних слика

### Преглед

Овај скрипт припрема скуп података за машинско учење преузимањем потребних слика, филтрирањем редова у којима преузимање слике није успело и чува скуп података као CSV фајл.

### Захтеви

Пре покретања овог скрипта, уверите се да имате инсталиране следеће библиотеке: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Такође, потребно је да у линији 2 замените `'Insert_Your_Dataset'` именом вашег скупа података са Hugging Face.

Потребне библиотеке:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функционалност

Скрипт извршава следеће кораке:

1. Преузима скуп података са Hugging Face користећи функцију `load_dataset()`.
2. Претвара Hugging Face скуп података у Pandas DataFrame ради лакше манипулације користећи методу `to_pandas()`.
3. Креира фасцикле за чување скупа података и слика.
4. Филтрира редове у којима преузимање слике није успело тако што пролази кроз сваки ред у DataFrame-у, преузима слику користећи прилагођену функцију `download_image()` и додаје филтриране редове у нови DataFrame под називом `filtered_rows`.
5. Креира нови DataFrame са филтрираним редовима и чува га на диск као CSV фајл.
6. Исписује поруку која указује где су скуп података и слике сачувани.

### Прилагођена функција

Функција `download_image()` преузима слику са URL-а и чува је локално користећи Pillow Image Library (PIL) и модул `io`. Враћа True ако је слика успешно преузета, а False у супротном. Функција такође баца изузетак са поруком о грешци ако захтев није успео.

### Како ово ради

Функција download_image узима два параметра: image_url, што је URL слике која се преузима, и save_path, што је путања на којој ће преузета слика бити сачувана.

Ево како функција ради:

Почиње тако што шаље GET захтев на image_url користећи метод requests.get. Ово преузима податке слике са URL-а.

Ред `response.raise_for_status()` проверава да ли је захтев био успешан. Ако статусни код одговора указује на грешку (нпр. 404 - Нема странице), биће бачен изузетак. Ово осигурава да настављамо са преузимањем слике само ако је захтев био успешан.

Податци слике се затим прослеђују методу Image.open из PIL (Python Imaging Library) модула. Ова метода креира Image објекат од података слике.

Ред `image.save(save_path)` чува слику на назначену путању save_path. save_path треба да садржи жељено име фајла и екстензију.

На крају, функција враћа True да означи да је слика успешно преузета и сачувана. Ако се током процеса догоди било каква грешка, изузетак се хвата, исписује се порука о грешци која указује на неуспех и враћа се False.

Ова функција је корисна за преузимање слика са URL-ова и њихово локално чување. Обрађује потенцијалне грешке током процеса преузимања и пружа повратну информацију о томе да ли је преузимање било успешно или не.

Вреди напоменути да се библиотека requests користи за слање HTTP захтева, PIL библиотека за рад са сликама, а класа BytesIO за руковање подацима слике као током бајтова.

### Закључак

Овај скрипт пружа једноставан начин за припрему скупа података за машинско учење преузимањем потребних слика, филтрирањем редова у којима преузимање слике није успело и чувањем скупа података као CSV фајл.

### Пример скрипта

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

### Пример преузимања кода  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Пример скупа података  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.