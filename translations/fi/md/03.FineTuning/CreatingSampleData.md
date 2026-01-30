# Luo kuvadatajoukko lataamalla DataSet Hugging Facesta ja siihen liittyvät kuvat


### Yleiskatsaus

Tämä skripti valmistaa koneoppimista varten datan lataamalla tarvittavat kuvat, suodattamalla pois rivit, joissa kuvien lataus epäonnistuu, ja tallentaa datan CSV-tiedostona.

### Esivaatimukset

Ennen skriptin suorittamista varmista, että sinulla on asennettuna kirjastot: `Pandas`, `Datasets`, `requests`, `PIL` ja `io`. Lisäksi sinun tulee korvata rivillä 2 `'Insert_Your_Dataset'` omalla Hugging Face -datasi nimellä.

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

1. Lataa datan Hugging Facesta `load_dataset()`-funktiolla.
2. Muuntaa Hugging Face -datan Pandas DataFrameksi helpompaa käsittelyä varten `to_pandas()`-metodilla.
3. Luo kansiot datan ja kuvien tallentamista varten.
4. Suodattaa pois rivit, joissa kuvien lataus epäonnistuu, käymällä läpi jokaisen rivin DataFramessa, lataamalla kuvan käyttäen omaa `download_image()`-funktiota ja lisäämällä suodatetun rivin uuteen DataFrameen nimeltä `filtered_rows`.
5. Luo uuden DataFramen suodatetuista riveistä ja tallentaa sen levylle CSV-tiedostona.
6. Tulostaa viestin, joka kertoo, mihin data ja kuvat on tallennettu.

### Oma funktio

`download_image()`-funktio lataa kuvan URL-osoitteesta ja tallentaa sen paikallisesti käyttäen Pillow Image Librarya (PIL) ja `io`-moduulia. Se palauttaa True, jos kuvan lataus onnistuu, ja False muuten. Funktio myös nostaa poikkeuksen virheilmoituksella, jos pyyntö epäonnistuu.

### Miten tämä toimii

download_image-funktio ottaa kaksi parametria: image_url, joka on ladattavan kuvan URL, ja save_path, joka on polku, johon ladattu kuva tallennetaan.

Näin funktio toimii:

Se aloittaa tekemällä GET-pyynnön image_url-osoitteeseen käyttäen requests.get-metodia. Tämä hakee kuvatiedot URL-osoitteesta.

Rivi response.raise_for_status() tarkistaa, onnistuiko pyyntö. Jos vastauskoodi osoittaa virheen (esim. 404 - Ei löytynyt), se nostaa poikkeuksen. Tämä varmistaa, että jatkamme kuvan lataamista vain, jos pyyntö onnistui.

Kuvatiedot annetaan sitten PIL-kirjaston Image.open-metodille. Tämä luo Image-olion kuvatiedoista.

Rivi image.save(save_path) tallentaa kuvan määriteltyyn save_path-polkuun. Polun tulee sisältää haluttu tiedostonimi ja tiedostopääte.

Lopuksi funktio palauttaa True osoittaakseen, että kuvan lataus ja tallennus onnistuivat. Jos prosessin aikana tapahtuu poikkeus, se käsittelee poikkeuksen, tulostaa virheilmoituksen epäonnistumisesta ja palauttaa False.

Tämä funktio on hyödyllinen kuvien lataamiseen URL-osoitteista ja niiden tallentamiseen paikallisesti. Se käsittelee mahdolliset virheet latausprosessin aikana ja antaa palautteen latauksen onnistumisesta tai epäonnistumisesta.

On hyvä huomata, että requests-kirjastoa käytetään HTTP-pyyntöihin, PIL-kirjastoa kuvien käsittelyyn ja BytesIO-luokkaa kuvatietojen käsittelyyn tavujonona.



### Yhteenveto

Tämä skripti tarjoaa kätevän tavan valmistella data koneoppimista varten lataamalla tarvittavat kuvat, suodattamalla pois rivit, joissa kuvien lataus epäonnistuu, ja tallentamalla datan CSV-tiedostona.

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

### Esimerkkidatajoukko  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.