<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:52:16+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "bg"
}
-->
# Генериране на набор от данни с изображения чрез изтегляне на DataSet от Hugging Face и свързаните изображения


### Преглед

Този скрипт подготвя набор от данни за машинно обучение, като изтегля необходимите изображения, филтрира редовете, при които изтеглянето на изображение неуспешно, и запазва набора от данни като CSV файл.

### Предварителни изисквания

Преди да стартирате този скрипт, уверете се, че имате инсталирани следните библиотеки: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Също така трябва да замените `'Insert_Your_Dataset'` на ред 2 с името на вашия набор от данни от Hugging Face.

Необходими библиотеки:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функционалност

Скриптът изпълнява следните стъпки:

1. Изтегля набора от данни от Hugging Face чрез функцията `load_dataset()`.
2. Преобразува набора от данни от Hugging Face в Pandas DataFrame за по-лесна обработка чрез метода `to_pandas()`.
3. Създава директории за запазване на набора от данни и изображенията.
4. Филтрира редовете, при които изтеглянето на изображение неуспешно, като преминава през всеки ред в DataFrame, изтегля изображението с помощта на персонализираната функция `download_image()` и добавя филтрирания ред в нов DataFrame, наречен `filtered_rows`.
5. Създава нов DataFrame с филтрираните редове и го записва на диск като CSV файл.
6. Извежда съобщение, указващо къде са запазени наборът от данни и изображенията.

### Персонализирана функция

Функцията `download_image()` изтегля изображение от URL и го запазва локално, използвайки библиотеката Pillow Image Library (PIL) и модула `io`. Връща True, ако изображението е успешно изтеглено, и False в противен случай. Функцията също така хвърля изключение с описанието на грешката, ако заявката не успее.

### Как работи това

Функцията download_image приема два параметъра: image_url, който е URL адресът на изображението за изтегляне, и save_path, който е пътят, където изтегленото изображение ще бъде запазено.

Ето как работи функцията:

Започва с изпращане на GET заявка към image_url чрез метода requests.get. Това извлича данните на изображението от URL адреса.

Редът response.raise_for_status() проверява дали заявката е успешна. Ако статус кодът на отговора показва грешка (например 404 - Не е намерено), ще бъде хвърлено изключение. Това гарантира, че продължаваме с изтеглянето на изображението само ако заявката е успешна.

Данните на изображението се подават на метода Image.open от модула PIL (Python Imaging Library). Този метод създава обект Image от данните на изображението.

Редът image.save(save_path) запазва изображението на посочения save_path. save_path трябва да включва желаното име на файла и разширението.

Накрая функцията връща True, за да покаже, че изображението е успешно изтеглено и запазено. Ако възникне някакво изключение по време на процеса, то се улавя, извежда се съобщение за грешка, указващо неуспеха, и функцията връща False.

Тази функция е полезна за изтегляне на изображения от URL адреси и запазването им локално. Тя обработва потенциални грешки по време на изтеглянето и предоставя обратна връзка дали изтеглянето е било успешно или не.

Струва си да се отбележи, че библиотеката requests се използва за HTTP заявки, библиотеката PIL за работа с изображения, а класът BytesIO се използва за обработка на данните на изображението като поток от байтове.



### Заключение

Този скрипт предоставя удобен начин за подготовка на набор от данни за машинно обучение чрез изтегляне на необходимите изображения, филтриране на редове с неуспешно изтегляне и запазване на набора от данни като CSV файл.

### Примерен скрипт

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

### Примерен код за изтегляне  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Примерен набор от данни  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия първичен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.