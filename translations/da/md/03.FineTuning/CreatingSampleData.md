<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:24:56+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "da"
}
-->
# Generate Image Data Set ved at downloade DataSet fra Hugging Face og tilhørende billeder


### Oversigt

Dette script forbereder et datasæt til maskinlæring ved at downloade nødvendige billeder, filtrere rækker hvor billeddownload fejler, og gemme datasættet som en CSV-fil.

### Forudsætninger

Inden du kører dette script, skal du sikre dig, at følgende biblioteker er installeret: `Pandas`, `Datasets`, `requests`, `PIL`, og `io`. Du skal også erstatte `'Insert_Your_Dataset'` på linje 2 med navnet på dit datasæt fra Hugging Face.

Nødvendige biblioteker:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktionalitet

Scriptet udfører følgende trin:

1. Downloader datasættet fra Hugging Face ved hjælp af `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funktionen downloader et billede fra en URL og gemmer det lokalt ved hjælp af Pillow Image Library (PIL) og `io` modulet. Den returnerer True, hvis billedet bliver downloadet succesfuldt, og False ellers. Funktionen kaster også en undtagelse med fejlbeskeden, hvis forespørgslen fejler.

### Hvordan fungerer det

download_image funktionen tager to parametre: image_url, som er URL’en til billedet der skal downloades, og save_path, som er stien hvor det downloadede billede gemmes.

Sådan fungerer funktionen:

Den starter med at lave en GET-forespørgsel til image_url ved hjælp af requests.get metoden. Dette henter billeddata fra URL’en.

Linjen response.raise_for_status() tjekker om forespørgslen var succesfuld. Hvis statuskoden indikerer en fejl (f.eks. 404 - Ikke fundet), vil den kaste en undtagelse. Dette sikrer, at vi kun fortsætter med at downloade billedet, hvis forespørgslen lykkedes.

Billeddataene bliver derefter sendt til Image.open metoden fra PIL (Python Imaging Library) modulet. Denne metode opretter et Image-objekt ud fra billeddataene.

Linjen image.save(save_path) gemmer billedet på den angivne save_path. save_path bør inkludere det ønskede filnavn og filtype.

Til sidst returnerer funktionen True for at indikere, at billedet blev downloadet og gemt med succes. Hvis der opstår en undtagelse under processen, fanges den, en fejlbesked udskrives, og funktionen returnerer False.

Denne funktion er nyttig til at downloade billeder fra URL’er og gemme dem lokalt. Den håndterer potentielle fejl under downloadprocessen og giver feedback på, om downloadet lykkedes eller ej.

Det er værd at bemærke, at requests biblioteket bruges til at lave HTTP-forespørgsler, PIL biblioteket bruges til at arbejde med billeder, og BytesIO klassen bruges til at håndtere billeddata som en strøm af bytes.



### Konklusion

Dette script giver en nem måde at forberede et datasæt til maskinlæring ved at downloade nødvendige billeder, filtrere rækker hvor billeddownload fejler, og gemme datasættet som en CSV-fil.

### Eksempel på script

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

### Eksempel på kode download  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Eksempel på datasæt  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.