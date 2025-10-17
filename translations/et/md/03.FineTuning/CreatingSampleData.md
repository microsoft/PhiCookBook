<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-10-11T11:45:07+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "et"
}
-->
# Loo pildikogum, laadides alla andmekogumi Hugging Face'ist ja seotud pildid

### Ülevaade

See skript valmistab ette masinõppe andmekogumi, laadides alla vajalikud pildid, filtreerides välja read, kus piltide allalaadimine ebaõnnestub, ja salvestades andmekogumi CSV-failina.

### Eeltingimused

Enne selle skripti käivitamist veendu, et sul on installitud järgmised teegid: `Pandas`, `Datasets`, `requests`, `PIL` ja `io`. Samuti pead asendama rea 2 `'Insert_Your_Dataset'` oma Hugging Face'i andmekogumi nimega.

Nõutavad teegid:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktsionaalsus

Skript täidab järgmisi samme:

1. Laadib andmekogumi Hugging Face'ist, kasutades funktsiooni `load_dataset()`.
2. Konverteerib Hugging Face'i andmekogumi Pandase DataFrame'iks lihtsamaks manipuleerimiseks, kasutades meetodit `to_pandas()`.
3. Loob kataloogid andmekogumi ja piltide salvestamiseks.
4. Filtreerib välja read, kus piltide allalaadimine ebaõnnestub, läbides iga DataFrame'i rea, laadides pildi alla kohandatud funktsiooni `download_image()` abil ja lisades filtreeritud rea uude DataFrame'i nimega `filtered_rows`.
5. Loob uue DataFrame'i filtreeritud ridadega ja salvestab selle CSV-failina.
6. Kuvab sõnumi, mis näitab, kuhu andmekogum ja pildid on salvestatud.

### Kohandatud funktsioon

Funktsioon `download_image()` laadib pildi URL-ilt alla ja salvestab selle kohapeal, kasutades Pillow pilditeeki (PIL) ja `io` moodulit. Funktsioon tagastab True, kui pilt on edukalt alla laaditud, ja False, kui mitte. Samuti viskab funktsioon erandi koos veateatega, kui päring ebaõnnestub.

### Kuidas see töötab

Funktsioon `download_image` võtab kaks parameetrit: `image_url`, mis on allalaaditava pildi URL, ja `save_path`, mis on tee, kuhu allalaaditud pilt salvestatakse.

Siin on, kuidas funktsioon töötab:

- See alustab GET-päringuga `image_url`-ile, kasutades meetodit `requests.get`. See toob URL-ilt pildiandmed.
- Rida `response.raise_for_status()` kontrollib, kas päring õnnestus. Kui vastuse olekukood viitab veale (nt 404 - Ei leitud), viskab see erandi. See tagab, et jätkame pildi allalaadimist ainult siis, kui päring õnnestus.
- Pildiandmed edastatakse seejärel meetodile `Image.open` PIL (Python Imaging Library) moodulist. See meetod loob pildiobjekti pildiandmetest.
- Rida `image.save(save_path)` salvestab pildi määratud `save_path`-i. `save_path` peaks sisaldama soovitud failinime ja laiendit.
- Lõpuks tagastab funktsioon True, et näidata, et pilt laaditi edukalt alla ja salvestati. Kui protsessi käigus tekib erand, püüab see erandi kinni, kuvab veateate, mis näitab ebaõnnestumist, ja tagastab False.

See funktsioon on kasulik piltide allalaadimiseks URL-idelt ja nende kohalikuks salvestamiseks. See käsitleb võimalikke vigu allalaadimisprotsessi ajal ja annab tagasisidet selle kohta, kas allalaadimine õnnestus või mitte.

Tasub märkida, et HTTP-päringute tegemiseks kasutatakse teeki `requests`, piltidega töötamiseks teeki `PIL` ja baitide voona pildiandmete käsitlemiseks klassi `BytesIO`.

### Kokkuvõte

See skript pakub mugavat viisi masinõppe andmekogumi ettevalmistamiseks, laadides alla vajalikud pildid, filtreerides välja read, kus piltide allalaadimine ebaõnnestub, ja salvestades andmekogumi CSV-failina.

### Näidisskript

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

### Näidiskoodi allalaadimine 
[Genereeri uus andmekogumi skript](../../../../code/04.Finetuning/generate_dataset.py)

### Näidisandmekogum
[Näidisandmekogum LORA peenhäälestuse näitest](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.