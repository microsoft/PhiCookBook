<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:52:44+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hr"
}
-->
# Generiranje skupa podataka slika preuzimanjem DataSet-a s Hugging Face i pripadajućih slika


### Pregled

Ovaj skript priprema skup podataka za strojno učenje preuzimanjem potrebnih slika, filtriranjem redaka gdje preuzimanje slika ne uspije, te spremanjem skupa podataka kao CSV datoteke.

### Preduvjeti

Prije pokretanja ovog skripta, provjerite imate li instalirane sljedeće biblioteke: `Pandas`, `Datasets`, `requests`, `PIL` i `io`. Također, potrebno je zamijeniti `'Insert_Your_Dataset'` u liniji 2 s imenom vašeg skupa podataka s Hugging Face.

Potrebne biblioteke:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalnost

Skript izvodi sljedeće korake:

1. Preuzima skup podataka s Hugging Face koristeći funkciju `load_dataset()`.
2. Pretvara Hugging Face skup podataka u Pandas DataFrame radi lakše manipulacije koristeći metodu `to_pandas()`.
3. Kreira direktorije za spremanje skupa podataka i slika.
4. Filtrira retke gdje preuzimanje slike ne uspijeva tako da prolazi kroz svaki redak u DataFrame-u, preuzima sliku koristeći prilagođenu funkciju `download_image()`, te dodaje filtrirane retke u novi DataFrame nazvan `filtered_rows`.
5. Kreira novi DataFrame s filtriranim redcima i sprema ga na disk kao CSV datoteku.
6. Ispisuje poruku koja pokazuje gdje su skup podataka i slike spremljeni.

### Prilagođena funkcija

Funkcija `download_image()` preuzima sliku s URL-a i sprema je lokalno koristeći Pillow Image Library (PIL) i modul `io`. Vraća True ako je slika uspješno preuzeta, a False u suprotnom. Funkcija također baca iznimku s porukom o pogrešci ako zahtjev ne uspije.

### Kako to funkcionira

Funkcija download_image prima dva parametra: image_url, što je URL slike koja se preuzima, i save_path, što je putanja na kojoj će preuzeta slika biti spremljena.

Evo kako funkcija radi:

Počinje slanjem GET zahtjeva na image_url koristeći metodu requests.get. Time se dohvaćaju podaci slike s URL-a.

Linija response.raise_for_status() provjerava je li zahtjev bio uspješan. Ako statusni kod odgovora ukazuje na pogrešku (npr. 404 - Nije pronađeno), baca iznimku. Time se osigurava da se slika preuzima samo ako je zahtjev prošao bez grešaka.

Podaci slike zatim se prosljeđuju metodi Image.open iz PIL (Python Imaging Library) modula. Ova metoda stvara Image objekt iz podataka slike.

Linija image.save(save_path) sprema sliku na zadanu putanju save_path. Putanja treba uključivati željeno ime datoteke i ekstenziju.

Na kraju, funkcija vraća True kao znak da je slika uspješno preuzeta i spremljena. Ako tijekom procesa dođe do bilo kakve iznimke, funkcija hvata iznimku, ispisuje poruku o pogrešci koja označava neuspjeh i vraća False.

Ova funkcija je korisna za preuzimanje slika s URL-ova i njihovo lokalno spremanje. Rukuje mogućim pogreškama tijekom preuzimanja i pruža povratnu informaciju o uspješnosti preuzimanja.

Vrijedi napomenuti da se za HTTP zahtjeve koristi biblioteka requests, za rad sa slikama koristi se PIL, a klasa BytesIO služi za rukovanje podacima slike kao nizom bajtova.



### Zaključak

Ovaj skript pruža jednostavan način za pripremu skupa podataka za strojno učenje preuzimanjem potrebnih slika, filtriranjem redaka gdje preuzimanje slika ne uspije, te spremanjem skupa podataka kao CSV datoteke.

### Primjer skripte

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

### Primjer preuzimanja koda  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Primjer skupa podataka  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.