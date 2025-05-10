<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:26:26+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hu"
}
-->
# Képadatbázis létrehozása a Hugging Face-ről letöltött DataSet és a hozzá tartozó képek alapján


### Áttekintés

Ez a script egy gépi tanuláshoz használható adatbázist készít elő azáltal, hogy letölti a szükséges képeket, kiszűri azokat a sorokat, ahol a kép letöltése nem sikerült, majd elmenti az adatbázist CSV fájlként.

### Előfeltételek

A script futtatása előtt győződj meg róla, hogy a következő könyvtárak telepítve vannak: `Pandas`, `Datasets`, `requests`, `PIL` és `io`. A 2. sorban található `'Insert_Your_Dataset'` helyére cseréld ki a Hugging Face-en található adatbázisod nevét.

Szükséges könyvtárak:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalitás

A script a következő lépéseket hajtja végre:

1. Letölti az adatbázist a Hugging Face-ről a `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` függvény segítségével. A download_image()` function, and appending the filtered row to a new DataFrame called ` függvény egy URL-ről tölti le a képet, és helyileg menti a Pillow Image Library (PIL) és az `io` modul segítségével. True értéket ad vissza, ha a kép sikeresen letöltődött, különben False-t. Ha a kérés sikertelen, a függvény kivételt dob a hibaüzenettel.

### Hogyan működik ez

A download_image függvény két paramétert vár: image_url, ami a letöltendő kép URL-je, és save_path, ami a letöltött kép mentési útvonala.

A függvény működése a következő:

Először egy GET kérést indít az image_url címre a requests.get metódussal, így lekéri a kép adatait az URL-ről.

A response.raise_for_status() sor ellenőrzi, hogy a kérés sikeres volt-e. Ha a válasz státuszkódja hibát jelez (pl. 404 - Nem található), kivételt dob. Ez biztosítja, hogy csak akkor folytatódjon a kép letöltése, ha a kérés sikeres volt.

A kép adatait ezután átadja a PIL (Python Imaging Library) Image.open metódusának, amely létrehoz egy Image objektumot a kép adataiból.

Az image.save(save_path) sor elmenti a képet a megadott save_path helyre. A save_path tartalmazza a kívánt fájlnevet és kiterjesztést.

Végül a függvény True értéket ad vissza, jelezve, hogy a kép sikeresen letöltődött és elmentésre került. Ha bármilyen kivétel lép fel a folyamat során, elkapja a kivételt, kiír egy hibaüzenetet a sikertelenségről, és False-t ad vissza.

Ez a függvény hasznos URL-ekről történő képletöltéshez és helyi mentéshez. Kezeli a letöltés közbeni esetleges hibákat, és visszajelzést ad a letöltés sikerességéről.

Érdemes megjegyezni, hogy a requests könyvtár HTTP kérések indítására szolgál, a PIL könyvtár képek kezelésére, a BytesIO osztály pedig az képadatokat bájtsorozatként kezeli.



### Összefoglalás

Ez a script kényelmes megoldást nyújt egy gépi tanuláshoz használható adatbázis előkészítésére azáltal, hogy letölti a szükséges képeket, kiszűri azokat a sorokat, ahol a kép letöltése nem sikerült, és elmenti az adatbázist CSV fájlként.

### Minta Script

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

### Minta Kód Letöltése  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Minta Adatbázis  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Nyilatkozat:**  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.