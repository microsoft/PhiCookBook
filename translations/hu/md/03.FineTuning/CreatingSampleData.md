<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:51:24+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hu"
}
-->
# Képadatbázis létrehozása a Hugging Face-ről letöltött DataSet és a hozzá tartozó képek segítségével


### Áttekintés

Ez a szkript egy gépi tanuláshoz használható adatbázist készít elő azáltal, hogy letölti a szükséges képeket, kiszűri azokat a sorokat, ahol a kép letöltése sikertelen, majd az adatbázist CSV fájlként menti el.

### Előfeltételek

A szkript futtatása előtt győződj meg róla, hogy a következő könyvtárak telepítve vannak: `Pandas`, `Datasets`, `requests`, `PIL` és `io`. A 2. sorban cseréld ki az `'Insert_Your_Dataset'` részt a Hugging Face-en található adatbázisod nevére.

Szükséges könyvtárak:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkciók

A szkript a következő lépéseket hajtja végre:

1. Letölti az adatbázist a Hugging Face-ről a `load_dataset()` függvény segítségével.
2. Átalakítja a Hugging Face adatbázist Pandas DataFrame-é a könnyebb kezelhetőség érdekében a `to_pandas()` metódussal.
3. Létrehozza a mappákat az adatbázis és a képek mentéséhez.
4. Kiszűri azokat a sorokat, ahol a kép letöltése sikertelen, úgy, hogy végigiterál a DataFrame minden során, letölti a képet a saját `download_image()` függvénnyel, majd a szűrt sorokat egy új DataFrame-hez, `filtered_rows`-hoz adja hozzá.
5. Új DataFrame-et hoz létre a szűrt sorokból, és elmenti azt CSV fájlként.
6. Kiír egy üzenetet, amely jelzi, hogy hova mentette az adatbázist és a képeket.

### Egyedi függvény

A `download_image()` függvény egy URL-ről letölt egy képet, és helyileg elmenti a Pillow Image Library (PIL) és az `io` modul segítségével. Ha a kép sikeresen letöltődött, True értéket ad vissza, egyébként False-t. Ha a kérés sikertelen, kivételt dob a hibaüzenettel.

### Hogyan működik ez

A download_image függvény két paramétert vár: image_url, ami a letöltendő kép URL-je, és save_path, ami az a hely, ahová a letöltött képet menteni fogja.

A függvény működése a következő:

Először egy GET kérést küld az image_url-re a requests.get metódussal. Ez lekéri a kép adatait az URL-ről.

A response.raise_for_status() sor ellenőrzi, hogy a kérés sikeres volt-e. Ha a válasz státuszkód hibát jelez (pl. 404 - Nem található), kivételt dob. Ez biztosítja, hogy csak akkor folytatjuk a kép letöltését, ha a kérés sikeres volt.

A kép adatokat ezután átadja a PIL (Python Imaging Library) Image.open metódusának. Ez létrehoz egy Image objektumot a kép adataiból.

Az image.save(save_path) sor elmenti a képet a megadott save_path helyre. A save_path tartalmazza a kívánt fájlnevet és kiterjesztést.

Végül a függvény True értéket ad vissza, jelezve, hogy a kép sikeresen letöltődött és elmentésre került. Ha bármilyen kivétel történik a folyamat során, elkapja azt, kiír egy hibaüzenetet a sikertelenségről, és False-t ad vissza.

Ez a függvény hasznos képek URL-ről történő letöltéséhez és helyi mentéséhez. Kezeli a letöltés közbeni esetleges hibákat, és visszajelzést ad arról, hogy a letöltés sikeres volt-e vagy sem.

Érdemes megjegyezni, hogy a requests könyvtár HTTP kérések küldésére szolgál, a PIL könyvtár képek kezelésére, a BytesIO osztály pedig a kép adatokat bájtsorozatként kezeli.



### Összegzés

Ez a szkript kényelmes módot biztosít egy gépi tanuláshoz használható adatbázis előkészítésére azáltal, hogy letölti a szükséges képeket, kiszűri a sikertelen letöltésű sorokat, és az adatbázist CSV fájlként menti el.

### Minta szkript

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

### Minta kód letöltése  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Minta adatbázis  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.