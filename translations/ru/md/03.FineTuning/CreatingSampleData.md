# Создание набора данных изображений путем загрузки DataSet с Hugging Face и связанных изображений


### Обзор

Этот скрипт подготавливает набор данных для машинного обучения, загружая необходимые изображения, отфильтровывая строки, в которых загрузка изображений не удалась, и сохраняя набор данных в формате CSV.

### Требования

Перед запуском скрипта убедитесь, что установлены следующие библиотеки: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Также необходимо заменить `'Insert_Your_Dataset'` во второй строке на название вашего набора данных с Hugging Face.

Необходимые библиотеки:

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

1. Загружает набор данных с Hugging Face с помощью функции `load_dataset()`.
2. Преобразует набор данных Hugging Face в Pandas DataFrame для удобства обработки с помощью метода `to_pandas()`.
3. Создает директории для сохранения набора данных и изображений.
4. Отфильтровывает строки, в которых не удалось загрузить изображение, проходя по каждой строке DataFrame, загружая изображение с помощью пользовательской функции `download_image()` и добавляя отфильтрованные строки в новый DataFrame под названием `filtered_rows`.
5. Создает новый DataFrame с отфильтрованными строками и сохраняет его на диск в формате CSV.
6. Выводит сообщение с указанием места сохранения набора данных и изображений.

### Пользовательская функция

Функция `download_image()` загружает изображение по URL и сохраняет его локально с помощью библиотеки Pillow (PIL) и модуля `io`. Она возвращает True, если изображение успешно загружено, и False в противном случае. В случае ошибки при запросе функция выбрасывает исключение с сообщением об ошибке.

### Как это работает

Функция download_image принимает два параметра: image_url — URL изображения для загрузки, и save_path — путь, по которому будет сохранено загруженное изображение.

Принцип работы функции:

Сначала она выполняет GET-запрос к image_url с помощью метода requests.get. Это позволяет получить данные изображения по URL.

Строка response.raise_for_status() проверяет, был ли запрос успешным. Если код ответа указывает на ошибку (например, 404 - Не найдено), будет выброшено исключение. Это гарантирует, что загрузка изображения продолжится только при успешном запросе.

Данные изображения передаются в метод Image.open из модуля PIL (Python Imaging Library). Этот метод создает объект Image из полученных данных.

Строка image.save(save_path) сохраняет изображение по указанному пути save_path. Путь должен включать имя файла и расширение.

В конце функция возвращает True, чтобы указать, что изображение успешно загружено и сохранено. Если во время процесса возникает исключение, оно перехватывается, выводится сообщение об ошибке, и функция возвращает False.

Эта функция полезна для загрузки изображений по URL и их локального сохранения. Она обрабатывает возможные ошибки во время загрузки и сообщает, была ли загрузка успешной.

Стоит отметить, что библиотека requests используется для выполнения HTTP-запросов, PIL — для работы с изображениями, а класс BytesIO — для обработки данных изображения как потока байтов.



### Заключение

Этот скрипт предоставляет удобный способ подготовки набора данных для машинного обучения, загружая необходимые изображения, отфильтровывая строки с неудачной загрузкой изображений и сохраняя набор данных в формате CSV.

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
[Скрипт создания нового набора данных](../../../../code/04.Finetuning/generate_dataset.py)

### Пример набора данных  
[Пример набора данных из примера дообучения с LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.