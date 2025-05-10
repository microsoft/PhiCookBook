<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:25:15+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "fi"
}
-->
# Generoi kuvadatajoukko lataamalla DataSet Hugging Facesta ja siihen liittyvät kuvat


### Yleiskatsaus

Tämä skripti valmistaa koneoppimista varten datan lataamalla tarvittavat kuvat, suodattamalla pois rivit, joilla kuvien lataus epäonnistuu, ja tallentamalla datan CSV-tiedostona.

### Esivaatimukset

Ennen tämän skriptin suorittamista varmista, että seuraavat kirjastot ovat asennettuna: `Pandas`, `Datasets`, `requests`, `PIL` ja `io`. Sinun tulee myös korvata `'Insert_Your_Dataset'` rivillä 2 omalla Hugging Face -datasetin nimelläsi.

Vaaditut kirjastot:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Toiminnallisuus

Skripti suorittaa seuraavat vaiheet:

1. Lataa datasetin Hugging Facesta käyttäen `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`-funktiota, joka lataa kuvan URL-osoitteesta ja tallentaa sen paikallisesti käyttäen Pillow Image Librarya (PIL) ja `io`-moduulia. Funktio palauttaa True, jos kuvan lataus onnistuu, ja False muuten. Funktio myös heittää poikkeuksen virheilmoituksella, jos pyyntö epäonnistuu.

### Miten tämä toimii

download_image-funktio ottaa kaksi parametria: image_url, joka on ladattavan kuvan URL, ja save_path, joka on polku, johon ladattu kuva tallennetaan.

Näin funktio toimii:

Se aloittaa tekemällä GET-pyynnön image_url-osoitteeseen käyttäen requests.get-metodia. Tämä hakee kuvatiedot URL-osoitteesta.

Rivi response.raise_for_status() tarkistaa, onnistuiko pyyntö. Jos vastauksen tilakoodi osoittaa virheen (esim. 404 - Ei löydy), se heittää poikkeuksen. Tämä varmistaa, että jatkamme kuvan lataamista vain, jos pyyntö onnistui.

Kuvatiedot välitetään sitten PIL (Python Imaging Library) -moduulin Image.open-metodille. Tämä metodi luo Image-olion kuvatiedoista.

Rivi image.save(save_path) tallentaa kuvan määritettyyn save_path-polkuun. save_pathin tulee sisältää haluttu tiedostonimi ja tiedostopääte.

Lopuksi funktio palauttaa True ilmaistakseen, että kuvan lataus ja tallennus onnistuivat. Jos prosessin aikana tapahtuu poikkeus, funktio käsittelee sen, tulostaa virheilmoituksen epäonnistumisesta ja palauttaa False.

Tämä funktio on hyödyllinen kuvien lataamiseen URL-osoitteista ja niiden tallentamiseen paikallisesti. Se käsittelee mahdolliset virheet latausprosessin aikana ja antaa palautetta siitä, onnistuiko lataus vai ei.

On hyvä huomioida, että requests-kirjastoa käytetään HTTP-pyyntöjen tekemiseen, PIL-kirjastoa kuvien käsittelyyn ja BytesIO-luokkaa kuvatietojen käsittelyyn tavujonona.


### Yhteenveto

Tämä skripti tarjoaa kätevän tavan valmistella datasetti koneoppimista varten lataamalla tarvittavat kuvat, suodattamalla pois rivit, joilla kuvien lataus epäonnistuu, ja tallentamalla datasetin CSV-tiedostona.

### Esimerkkiskripti

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

### Esimerkkikoodin lataus  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Esimerkkidatasetti  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.