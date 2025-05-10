<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:27:14+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sr"
}
-->
# Generisanje skupa podataka za slike preuzimanjem DataSet-a sa Hugging Face-a i pripadajućih slika


### Pregled

Ovaj skript priprema skup podataka za mašinsko učenje tako što preuzima potrebne slike, filtrira redove gde preuzimanje slike nije uspelo i čuva skup podataka kao CSV fajl.

### Preduslovi

Pre pokretanja ovog skripta, proverite da imate instalirane sledeće biblioteke: `Pandas`, `Datasets`, `requests`, `PIL` i `io`. Takođe, potrebno je da zamenite `'Insert_Your_Dataset'` u liniji 2 imenom vašeg skupa podataka sa Hugging Face-a.

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

Skript izvodi sledeće korake:

1. Preuzima skup podataka sa Hugging Face-a koristeći `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funkcija preuzima sliku sa URL-a i čuva je lokalno koristeći Pillow Image Library (PIL) i `io` modul. Vraća True ako je slika uspešno preuzeta, a False u suprotnom. Funkcija takođe baca izuzetak sa porukom o grešci kada zahtev ne uspe.

### Kako ovo funkcioniše

Funkcija download_image prima dva parametra: image_url, što je URL slike koja se preuzima, i save_path, što je putanja gde će preuzeta slika biti sačuvana.

Evo kako funkcija radi:

Počinje slanjem GET zahteva na image_url koristeći metodu requests.get. Ovo preuzima podatke slike sa URL-a.

Linija response.raise_for_status() proverava da li je zahtev bio uspešan. Ako statusni kod odgovora ukazuje na grešku (npr. 404 - Nije pronađeno), biće bačen izuzetak. Ovo osigurava da nastavljamo sa preuzimanjem slike samo ako je zahtev uspeo.

Podaci slike se zatim prosleđuju metodi Image.open iz PIL (Python Imaging Library) modula. Ova metoda kreira Image objekat iz podataka slike.

Linija image.save(save_path) čuva sliku na naznačenoj putanji save_path. Putanja treba da uključuje željeno ime fajla i ekstenziju.

Na kraju, funkcija vraća True da označi da je slika uspešno preuzeta i sačuvana. Ako dođe do bilo kakvog izuzetka tokom procesa, on se hvata, štampa se poruka o grešci koja označava neuspeh, i funkcija vraća False.

Ova funkcija je korisna za preuzimanje slika sa URL-ova i njihovo lokalno čuvanje. Rukuje potencijalnim greškama tokom procesa preuzimanja i pruža povratnu informaciju da li je preuzimanje bilo uspešno ili ne.

Vredno je napomenuti da se biblioteka requests koristi za HTTP zahteve, PIL biblioteka za rad sa slikama, a klasa BytesIO za rukovanje podacima slike kao tok bajtova.



### Zaključak

Ovaj skript pruža praktičan način za pripremu skupa podataka za mašinsko učenje tako što preuzima potrebne slike, filtrira redove gde preuzimanje slike nije uspelo i čuva skup podataka kao CSV fajl.

### Primer skripta

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

### Primer preuzimanja koda  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Primer skupa podataka  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Ограничење одговорности**:  
Овај документ је преведен помоћу АИ преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране стручног лекара. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.