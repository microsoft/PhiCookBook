<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:25:06+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "no"
}
-->
# Generer bildedatasett ved å laste ned DataSet fra Hugging Face og tilhørende bilder


### Oversikt

Dette skriptet forbereder et datasett for maskinlæring ved å laste ned nødvendige bilder, filtrere ut rader der nedlasting av bilder feiler, og lagre datasettet som en CSV-fil.

### Forutsetninger

Før du kjører dette skriptet, sørg for å ha følgende biblioteker installert: `Pandas`, `Datasets`, `requests`, `PIL`, og `io`. Du må også erstatte `'Insert_Your_Dataset'` i linje 2 med navnet på datasettet ditt fra Hugging Face.

Nødvendige biblioteker:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funksjonalitet

Skriptet utfører følgende steg:

1. Laster ned datasettet fra Hugging Face ved hjelp av `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funksjonen laster ned et bilde fra en URL og lagrer det lokalt ved hjelp av Pillow Image Library (PIL) og `io`-modulen. Den returnerer True hvis bildet lastes ned vellykket, og False ellers. Funksjonen kaster også et unntak med feilmeldingen hvis forespørselen feiler.

### Hvordan fungerer dette

download_image-funksjonen tar to parametere: image_url, som er URL-en til bildet som skal lastes ned, og save_path, som er stien der det nedlastede bildet skal lagres.

Slik fungerer funksjonen:

Den starter med å gjøre en GET-forespørsel til image_url ved hjelp av requests.get-metoden. Dette henter bildedata fra URL-en.

Linjen response.raise_for_status() sjekker om forespørselen var vellykket. Hvis statuskoden indikerer en feil (f.eks. 404 - Ikke funnet), vil den kaste et unntak. Dette sikrer at vi kun fortsetter med å laste ned bildet hvis forespørselen var vellykket.

Bildedataene sendes deretter til Image.open-metoden fra PIL (Python Imaging Library)-modulen. Denne metoden oppretter et Image-objekt fra bildedataene.

Linjen image.save(save_path) lagrer bildet til den angitte save_path. save_path bør inkludere ønsket filnavn og filtype.

Til slutt returnerer funksjonen True for å indikere at bildet ble lastet ned og lagret vellykket. Hvis det oppstår et unntak under prosessen, fanges det, en feilmelding printes som indikerer at nedlastingen feilet, og funksjonen returnerer False.

Denne funksjonen er nyttig for å laste ned bilder fra URL-er og lagre dem lokalt. Den håndterer potensielle feil under nedlastingsprosessen og gir tilbakemelding på om nedlastingen var vellykket eller ikke.

Det er verdt å merke seg at requests-biblioteket brukes til å gjøre HTTP-forespørsler, PIL-biblioteket brukes for å jobbe med bilder, og BytesIO-klassen brukes til å håndtere bildedata som en byte-strøm.



### Konklusjon

Dette skriptet gir en enkel måte å forberede et datasett for maskinlæring ved å laste ned nødvendige bilder, filtrere ut rader der nedlasting av bilder feiler, og lagre datasettet som en CSV-fil.

### Eksempelskript

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

### Eksempelkode for nedlasting  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Eksempeldatasett  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.