<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:25:24+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "nl"
}
-->
# Genereer een afbeeldingsdataset door DataSet te downloaden van Hugging Face en bijbehorende afbeeldingen


### Overzicht

Dit script bereidt een dataset voor machine learning voor door de benodigde afbeeldingen te downloaden, rijen te filteren waar het downloaden van afbeeldingen mislukt, en de dataset op te slaan als een CSV-bestand.

### Vereisten

Voordat je dit script uitvoert, zorg ervoor dat de volgende libraries geïnstalleerd zijn: `Pandas`, `Datasets`, `requests`, `PIL`, en `io`. Je moet ook `'Insert_Your_Dataset'` in regel 2 vervangen door de naam van je dataset van Hugging Face.

Vereiste libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Functionaliteit

Het script voert de volgende stappen uit:

1. Downloadt de dataset van Hugging Face met behulp van de `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` functie download_image() haalt een afbeelding op van een URL en slaat deze lokaal op met behulp van de Pillow Image Library (PIL) en de `io` module. De functie geeft True terug als de afbeelding succesvol is gedownload, en False als dat niet het geval is. Bij een mislukte aanvraag wordt een uitzondering met de foutmelding opgegooid.

### Hoe werkt dit

De functie download_image neemt twee parameters: image_url, de URL van de afbeelding die gedownload moet worden, en save_path, het pad waar de gedownloade afbeelding wordt opgeslagen.

Zo werkt de functie:

Eerst wordt een GET-verzoek gedaan naar image_url met de requests.get methode. Hiermee wordt de afbeeldingsdata opgehaald van de URL.

De regel response.raise_for_status() controleert of het verzoek succesvol was. Als de statuscode van de response een fout aangeeft (bijvoorbeeld 404 - Niet gevonden), wordt er een uitzondering opgegooid. Dit zorgt ervoor dat we alleen doorgaan met downloaden als het verzoek gelukt is.

De afbeeldingsdata wordt vervolgens doorgegeven aan de Image.open methode van de PIL (Python Imaging Library) module. Deze methode maakt een Image-object aan van de data.

Met image.save(save_path) wordt de afbeelding opgeslagen op het opgegeven save_path. Het pad moet de gewenste bestandsnaam en extensie bevatten.

Tot slot geeft de functie True terug om aan te geven dat de afbeelding succesvol is gedownload en opgeslagen. Als er tijdens het proces een uitzondering optreedt, wordt deze opgevangen, wordt er een foutmelding getoond, en wordt False teruggegeven.

Deze functie is handig om afbeeldingen van URLs te downloaden en lokaal op te slaan. Hij gaat om met mogelijke fouten tijdens het downloaden en geeft feedback over het succes van het downloaden.

Het is goed om te weten dat de requests library wordt gebruikt voor HTTP-verzoeken, de PIL library voor het werken met afbeeldingen, en de BytesIO klasse om de afbeeldingsdata als een stroom van bytes te verwerken.



### Conclusie

Dit script biedt een handige manier om een dataset voor machine learning voor te bereiden door benodigde afbeeldingen te downloaden, rijen waar het downloaden mislukt te filteren, en de dataset op te slaan als CSV-bestand.

### Voorbeeldscript

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

### Voorbeeldcode Download  
[Genereer een nieuw Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Voorbeeld Data Set  
[Voorbeeld Data Set uit finetuning met LORA voorbeeld](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.