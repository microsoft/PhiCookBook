# Ustvarjanje nabora slikovnih podatkov z nalaganjem DataSet-a iz Hugging Face in pripadajočih slik


### Pregled

Ta skripta pripravi nabor podatkov za strojno učenje tako, da prenese potrebne slike, odstrani vrstice, kjer prenos slike ni uspel, in shrani nabor podatkov kot CSV datoteko.

### Zahteve

Pred zagonom te skripte poskrbite, da imate nameščene naslednje knjižnice: `Pandas`, `Datasets`, `requests`, `PIL` in `io`. Prav tako boste morali v vrstici 2 zamenjati `'Insert_Your_Dataset'` z imenom vašega nabora podatkov iz Hugging Face.

Zahtevane knjižnice:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalnost

Skripta izvede naslednje korake:

1. Prenese nabor podatkov iz Hugging Face z uporabo funkcije `load_dataset()`.
2. Pretvori Hugging Face nabor podatkov v Pandas DataFrame za lažje upravljanje z metodo `to_pandas()`.
3. Ustvari mape za shranjevanje nabora podatkov in slik.
4. Odstrani vrstice, kjer prenos slike ni uspel, tako da pregleda vsako vrstico v DataFrame, prenese sliko z uporabo prilagojene funkcije `download_image()` in filtrirano vrstico doda v nov DataFrame z imenom `filtered_rows`.
5. Ustvari nov DataFrame s filtriranimi vrsticami in ga shrani na disk kot CSV datoteko.
6. Izpiše sporočilo, kje so bili nabor podatkov in slike shranjeni.

### Prilagojena funkcija

Funkcija `download_image()` prenese sliko z URL-ja in jo shrani lokalno z uporabo knjižnice Pillow Image Library (PIL) in modula `io`. Vrne True, če je bila slika uspešno prenesena, sicer False. Funkcija ob neuspehu zahteve sproži izjemo z ustreznim sporočilom o napaki.

### Kako to deluje

Funkcija download_image prejme dva parametra: image_url, kar je URL slike za prenos, in save_path, kar je pot, kamor bo prenesena slika shranjena.

Tako deluje funkcija:

Najprej izvede GET zahtevo na image_url z metodo requests.get. S tem pridobi podatke slike z URL-ja.

Vrstica response.raise_for_status() preveri, ali je bila zahteva uspešna. Če statusna koda odgovora kaže na napako (npr. 404 - Ni najdeno), sproži izjemo. To zagotavlja, da nadaljujemo z nalaganjem slike le, če je bila zahteva uspešna.

Podatki slike se nato posredujejo metodi Image.open iz modula PIL (Python Imaging Library). Ta metoda ustvari Image objekt iz podatkov slike.

Vrstica image.save(save_path) shrani sliko na določeno pot save_path. Pot save_path mora vsebovati želeno ime datoteke in pripono.

Na koncu funkcija vrne True, kar pomeni, da je bila slika uspešno prenesena in shranjena. Če med postopkom pride do izjeme, jo funkcija ujame, izpiše sporočilo o napaki in vrne False.

Ta funkcija je uporabna za prenos slik z URL-jev in njihovo lokalno shranjevanje. Obvladuje morebitne napake med prenosom in zagotavlja povratno informacijo o uspešnosti prenosa.

Pomembno je vedeti, da knjižnica requests omogoča HTTP zahteve, knjižnica PIL omogoča delo s slikami, razred BytesIO pa omogoča obdelavo slikovnih podatkov kot toka bajtov.



### Zaključek

Ta skripta ponuja priročen način za pripravo nabora podatkov za strojno učenje z nalaganjem potrebnih slik, odstranjevanjem vrstic, kjer prenos slike ni uspel, in shranjevanjem nabora podatkov kot CSV datoteko.

### Primer skripte

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

### Primer prenosa kode  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Primer nabora podatkov  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.