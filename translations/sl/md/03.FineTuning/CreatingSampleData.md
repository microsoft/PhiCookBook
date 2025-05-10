<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:27:35+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sl"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Overview

Ta skripta pripravi podatkovni niz za strojno učenje tako, da prenese potrebne slike, odstrani vrstice, kjer prenos slike ni uspel, in shrani podatkovni niz kot CSV datoteko.

### Prerequisites

Pred zagonom te skripte poskrbite, da imate nameščene naslednje knjižnice: `Pandas`, `Datasets`, `requests`, `PIL` in `io`. Prav tako morate v vrstici 2 zamenjati `'Insert_Your_Dataset'` z imenom vašega podatkovnega niza iz Hugging Face.

Required Libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Functionality

Skripta izvede naslednje korake:

1. Prenese podatkovni niz iz Hugging Face z uporabo `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funkcija prenese sliko z URL-ja in jo shrani lokalno z uporabo knjižnice Pillow Image (PIL) in modula `io`. Funkcija vrne True, če je bila slika uspešno prenesena, sicer False. V primeru neuspeha pri zahtevi funkcija sproži izjemo z ustreznim sporočilom o napaki.

### How does this work

Funkcija download_image sprejme dva parametra: image_url, kar je URL slike za prenos, in save_path, kar je pot, kamor bo prenesena slika shranjena.

Tako deluje funkcija:

Najprej izvede GET zahtevo na image_url z metodo requests.get. S tem pridobi podatke slike s URL-ja.

Vrstica response.raise_for_status() preveri, ali je bila zahteva uspešna. Če statusna koda odgovora kaže na napako (npr. 404 - Ni najdeno), bo sprožila izjemo. To zagotavlja, da nadaljujemo z nalaganjem slike samo, če je bila zahteva uspešna.

Podatki slike se nato posredujejo metodi Image.open iz PIL (Python Imaging Library) modula. Ta metoda ustvari Image objekt iz podatkov slike.

Vrstica image.save(save_path) shrani sliko na določeno pot save_path. Pot mora vključevati želeno ime datoteke in pripono.

Na koncu funkcija vrne True, da označi, da je bila slika uspešno prenesena in shranjena. Če med postopkom pride do izjeme, jo ujame, izpiše sporočilo o napaki in vrne False.

Ta funkcija je uporabna za prenos slik z URL-jev in njihovo lokalno shranjevanje. Obvladuje morebitne napake med prenosom in poda povratno informacijo o uspešnosti prenosa.

Pomembno je vedeti, da knjižnica requests služi za HTTP zahteve, PIL za delo s slikami, razred BytesIO pa za upravljanje podatkov slike kot toka bajtov.


### Conclusion

Ta skripta omogoča enostavno pripravo podatkovnega niza za strojno učenje z nalaganjem potrebnih slik, odstranjevanjem vrstic z neuspešnim prenosom in shranjevanjem podatkovnega niza kot CSV datoteko.

### Sample Script

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

### Sample Code Download 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Sample Data Set
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.