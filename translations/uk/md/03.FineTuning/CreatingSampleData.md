# Генерація набору даних зображень шляхом завантаження DataSet з Hugging Face та відповідних зображень


### Огляд

Цей скрипт готує набір даних для машинного навчання, завантажуючи необхідні зображення, відфільтровуючи рядки, де завантаження зображень не вдалося, та зберігає набір даних у форматі CSV.

### Вимоги

Перед запуском цього скрипта переконайтеся, що встановлені такі бібліотеки: `Pandas`, `Datasets`, `requests`, `PIL` та `io`. Також потрібно замінити `'Insert_Your_Dataset'` у рядку 2 на назву вашого набору даних з Hugging Face.

Необхідні бібліотеки:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функціонал

Скрипт виконує такі кроки:

1. Завантажує набір даних з Hugging Face за допомогою функції `load_dataset()`.
2. Конвертує набір даних Hugging Face у Pandas DataFrame для зручнішої обробки за допомогою методу `to_pandas()`.
3. Створює директорії для збереження набору даних та зображень.
4. Відфільтровує рядки, де завантаження зображень не вдалося, перебираючи кожен рядок DataFrame, завантажуючи зображення за допомогою кастомної функції `download_image()` та додаючи відфільтровані рядки до нового DataFrame під назвою `filtered_rows`.
5. Створює новий DataFrame з відфільтрованими рядками та зберігає його на диск у форматі CSV.
6. Виводить повідомлення про те, де збережено набір даних та зображення.

### Кастомна функція

Функція `download_image()` завантажує зображення за URL та зберігає його локально, використовуючи бібліотеку Pillow (PIL) та модуль `io`. Вона повертає True, якщо зображення успішно завантажено, і False в іншому випадку. У разі помилки запиту функція викликає виняток з повідомленням про помилку.

### Як це працює

Функція download_image приймає два параметри: image_url — URL зображення для завантаження, та save_path — шлях, за яким зображення буде збережено.

Ось як працює ця функція:

Спочатку вона робить GET-запит до image_url за допомогою методу requests.get. Це отримує дані зображення з URL.

Рядок response.raise_for_status() перевіряє, чи був запит успішним. Якщо код статусу відповіді вказує на помилку (наприклад, 404 - Не знайдено), буде викликано виняток. Це гарантує, що ми продовжимо завантаження зображення лише у разі успішного запиту.

Дані зображення передаються методу Image.open з модуля PIL (Python Imaging Library). Цей метод створює об’єкт Image з отриманих даних.

Рядок image.save(save_path) зберігає зображення за вказаним шляхом save_path. Шлях повинен включати бажане ім’я файлу та розширення.

Наприкінці функція повертає True, щоб вказати, що зображення було успішно завантажено та збережено. Якщо під час процесу виникає виняток, він перехоплюється, виводиться повідомлення про помилку, і функція повертає False.

Ця функція корисна для завантаження зображень з URL та їх локального збереження. Вона обробляє можливі помилки під час завантаження та надає зворотний зв’язок про успішність операції.

Варто зазначити, що бібліотека requests використовується для HTTP-запитів, PIL — для роботи із зображеннями, а клас BytesIO — для обробки даних зображення як потоку байтів.



### Висновок

Цей скрипт забезпечує зручний спосіб підготувати набір даних для машинного навчання, завантажуючи необхідні зображення, відфільтровуючи рядки з помилками завантаження та зберігаючи набір даних у форматі CSV.

### Приклад скрипта

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

### Приклад завантаження коду  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Приклад набору даних  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.