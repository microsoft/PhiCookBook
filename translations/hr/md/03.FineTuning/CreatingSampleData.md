<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:27:25+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hr"
}
-->
# Generiranje skupa podataka slika preuzimanjem DataSeta s Hugging Face i pridruženih slika

### Pregled

Ovaj skript priprema skup podataka za strojno učenje preuzimanjem potrebnih slika, filtriranjem redaka gdje preuzimanje slike ne uspije, te spremanjem skupa podataka kao CSV datoteke.

### Preduvjeti

Prije pokretanja ovog skripta, provjerite da imate instalirane sljedeće biblioteke: `Pandas`, `Datasets`, `requests`, `PIL` i `io`. Također ćete trebati zamijeniti `'Insert_Your_Dataset'` u liniji 2 imenom vašeg skupa podataka s Hugging Face.

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

Skripta izvodi sljedeće korake:

1. Preuzima skup podataka s Hugging Face koristeći `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funkcija preuzima sliku s URL-a i sprema je lokalno koristeći Pillow Image Library (PIL) i `io` modul. Funkcija vraća True ako je slika uspješno preuzeta, a False ako nije. Također baca iznimku s porukom o grešci kada zahtjev ne uspije.

### Kako to funkcionira

Funkcija download_image prima dva parametra: image_url, što je URL slike koja se preuzima, i save_path, što je putanja na kojoj će preuzeta slika biti spremljena.

Evo kako funkcija radi:

Počinje slanjem GET zahtjeva na image_url koristeći requests.get metodu. To dohvaća podatke slike s URL-a.

Linija response.raise_for_status() provjerava je li zahtjev bio uspješan. Ako statusni kod odgovora označava grešku (npr. 404 - Nije pronađeno), funkcija će baciti iznimku. Time se osigurava da nastavljamo s preuzimanjem slike samo ako je zahtjev uspješan.

Podaci slike zatim se prosljeđuju metodi Image.open iz PIL (Python Imaging Library) modula. Ova metoda stvara Image objekt iz podataka slike.

Linija image.save(save_path) sprema sliku na navedenu putanju save_path. Putanja treba uključivati željeno ime datoteke i ekstenziju.

Na kraju, funkcija vraća True kao znak da je slika uspješno preuzeta i spremljena. Ako tijekom procesa dođe do bilo kakve iznimke, funkcija hvata iznimku, ispisuje poruku o grešci koja označava neuspjeh i vraća False.

Ova funkcija je korisna za preuzimanje slika s URL-ova i njihovo lokalno spremanje. Ona upravlja potencijalnim greškama tijekom procesa preuzimanja i daje povratnu informaciju o tome je li preuzimanje bilo uspješno ili ne.

Važno je napomenuti da se requests biblioteka koristi za HTTP zahtjeve, PIL biblioteka za rad sa slikama, a klasa BytesIO za rukovanje podacima slike kao streamom bajtova.

### Zaključak

Ovaj skript pruža jednostavan način za pripremu skupa podataka za strojno učenje preuzimanjem potrebnih slika, filtriranjem redaka gdje preuzimanje slike ne uspije, i spremanjem skupa podataka kao CSV datoteke.

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
Ovaj dokument preveden je pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.