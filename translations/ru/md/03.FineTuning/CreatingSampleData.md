<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-03-27T13:33:36+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "ru"
}
-->
# Создание набора данных изображений путем загрузки DataSet с Hugging Face и связанных изображений

### Обзор

Этот скрипт готовит набор данных для машинного обучения, загружая необходимые изображения, отфильтровывая строки, где загрузка изображений не удалась, и сохраняет набор данных в формате CSV.

### Предварительные требования

Перед запуском скрипта убедитесь, что установлены следующие библиотеки: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Также необходимо заменить `'Insert_Your_Dataset'` на строке 2 названием вашего набора данных из Hugging Face.

Необходимые библиотеки:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функциональность

Скрипт выполняет следующие шаги:

1. Загружает набор данных с Hugging Face с помощью `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Функция `download_image()` загружает изображение из URL и сохраняет его локально с использованием библиотеки Pillow Image Library (PIL) и модуля `io`. Она возвращает True, если изображение успешно загружено, и False в противном случае. Функция также вызывает исключение с сообщением об ошибке, если запрос не удался.

### Как это работает

Функция `download_image` принимает два параметра: `image_url` — URL изображения для загрузки, и `save_path` — путь, где будет сохранено загруженное изображение.

Вот как работает функция:

Она начинает с выполнения GET-запроса к `image_url` с использованием метода `requests.get`. Это позволяет получить данные изображения из URL.

Строка `response.raise_for_status()` проверяет, был ли запрос успешным. Если код состояния ответа указывает на ошибку (например, 404 — Не найдено), будет вызвано исключение. Это гарантирует, что мы продолжаем загрузку изображения только в случае успешного запроса.

Данные изображения затем передаются методу `Image.open` из модуля PIL (Python Imaging Library). Этот метод создает объект изображения из данных изображения.

Строка `image.save(save_path)` сохраняет изображение по указанному пути `save_path`. `save_path` должен включать желаемое имя файла и расширение.

Наконец, функция возвращает True, чтобы указать, что изображение успешно загружено и сохранено. Если в процессе возникает какое-либо исключение, оно перехватывается, выводится сообщение об ошибке, указывающее на сбой, и возвращается False.

Эта функция полезна для загрузки изображений из URL и их локального сохранения. Она обрабатывает потенциальные ошибки во время процесса загрузки и предоставляет обратную связь о том, была ли загрузка успешной.

Стоит отметить, что библиотека `requests` используется для выполнения HTTP-запросов, библиотека PIL используется для работы с изображениями, а класс `BytesIO` используется для обработки данных изображения как потока байтов.

### Заключение

Этот скрипт предоставляет удобный способ подготовки набора данных для машинного обучения путем загрузки необходимых изображений, фильтрации строк, где загрузка изображений не удалась, и сохранения набора данных в формате CSV.

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

### Загрузка примера кода 
[Скрипт для создания нового набора данных](../../../../code/04.Finetuning/generate_dataset.py)

### Пример набора данных
[Пример набора данных из финетюнинга с использованием LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на то, что мы стремимся к точности, имейте в виду, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.