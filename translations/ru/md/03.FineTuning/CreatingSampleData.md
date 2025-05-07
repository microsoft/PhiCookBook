<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-07T13:25:28+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ru"
}
-->
# Создание набора данных изображений путем загрузки DataSet с Hugging Face и связанных с ним изображений


### Обзор

Этот скрипт подготавливает набор данных для машинного обучения, загружая необходимые изображения, отфильтровывая строки, где загрузка изображений не удалась, и сохраняя набор данных в формате CSV.

### Требования

Перед запуском скрипта убедитесь, что у вас установлены следующие библиотеки: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Также необходимо заменить `'Insert_Your_Dataset'` во второй строке на название вашего набора данных с Hugging Face.

Требуемые библиотеки:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функционал

Скрипт выполняет следующие шаги:

1. Загружает набор данных с Hugging Face с помощью `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` функция скачивает изображение по URL и сохраняет его локально с помощью библиотеки Pillow (PIL) и модуля `io`. Возвращает True, если изображение успешно загружено, и False в противном случае. В случае ошибки запроса функция генерирует исключение с сообщением об ошибке.

### Как это работает

Функция download_image принимает два параметра: image_url — URL изображения для загрузки, и save_path — путь, по которому будет сохранено загруженное изображение.

Принцип работы функции:

Сначала она отправляет GET-запрос по адресу image_url с помощью метода requests.get. Это позволяет получить данные изображения с URL.

Строка response.raise_for_status() проверяет, успешно ли выполнен запрос. Если код ответа указывает на ошибку (например, 404 — Не найдено), будет сгенерировано исключение. Это гарантирует, что загрузка изображения продолжится только при успешном ответе.

Данные изображения передаются методу Image.open из модуля PIL (Python Imaging Library). Этот метод создает объект Image из данных изображения.

Строка image.save(save_path) сохраняет изображение по указанному пути save_path. Путь должен включать имя файла и расширение.

В конце функция возвращает True, чтобы указать на успешную загрузку и сохранение изображения. Если во время процесса возникает исключение, оно перехватывается, выводится сообщение об ошибке, и функция возвращает False.

Эта функция удобна для загрузки изображений по URL и их локального сохранения. Она обрабатывает возможные ошибки при загрузке и сообщает, была ли загрузка успешной.

Стоит отметить, что библиотека requests используется для выполнения HTTP-запросов, библиотека PIL — для работы с изображениями, а класс BytesIO — для обработки данных изображения в виде потока байтов.



### Заключение

Этот скрипт предоставляет удобный способ подготовки набора данных для машинного обучения, загружая необходимые изображения, отфильтровывая строки с неудачной загрузкой и сохраняя набор данных в CSV.

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

### Пример загрузки кода  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Пример набора данных  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, пожалуйста, учитывайте, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.