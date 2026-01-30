# Generera bilddataset genom att ladda ner DataSet från Hugging Face och tillhörande bilder

### Översikt

Detta skript förbereder ett dataset för maskininlärning genom att ladda ner nödvändiga bilder, filtrera bort rader där bildnedladdning misslyckas, och spara datasetet som en CSV-fil.

### Förutsättningar

Innan du kör detta skript, se till att följande bibliotek är installerade: `Pandas`, `Datasets`, `requests`, `PIL` och `io`. Du behöver också byta ut `'Insert_Your_Dataset'` på rad 2 mot namnet på ditt dataset från Hugging Face.

Nödvändiga bibliotek:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktionalitet

Skriptet utför följande steg:

1. Laddar ner datasetet från Hugging Face med funktionen `load_dataset()`.
2. Konverterar Hugging Face-datasetet till en Pandas DataFrame för enklare hantering med metoden `to_pandas()`.
3. Skapar kataloger för att spara datasetet och bilderna.
4. Filtrerar bort rader där bildnedladdning misslyckas genom att iterera över varje rad i DataFrame, ladda ner bilden med den anpassade funktionen `download_image()`, och lägga till de filtrerade raderna i en ny DataFrame som kallas `filtered_rows`.
5. Skapar en ny DataFrame med de filtrerade raderna och sparar den på disk som en CSV-fil.
6. Skriver ut ett meddelande som visar var datasetet och bilderna har sparats.

### Anpassad funktion

Funktionen `download_image()` laddar ner en bild från en URL och sparar den lokalt med hjälp av Pillow Image Library (PIL) och `io`-modulen. Den returnerar True om bilden laddas ner framgångsrikt, annars False. Funktionen kastar också ett undantag med felmeddelande om förfrågan misslyckas.

### Hur fungerar detta

Funktionen download_image tar två parametrar: image_url, som är URL:en till bilden som ska laddas ner, och save_path, som är sökvägen där den nedladdade bilden ska sparas.

Så här fungerar funktionen:

Den börjar med att göra en GET-förfrågan till image_url med metoden requests.get. Detta hämtar bilddata från URL:en.

Raden response.raise_for_status() kontrollerar om förfrågan lyckades. Om statuskoden indikerar ett fel (t.ex. 404 - Ej hittad) kastas ett undantag. Detta säkerställer att vi bara fortsätter med nedladdningen om förfrågan var framgångsrik.

Bilddata skickas sedan till metoden Image.open från PIL (Python Imaging Library). Denna metod skapar ett Image-objekt från bilddatan.

Raden image.save(save_path) sparar bilden till den angivna save_path. save_path bör inkludera önskat filnamn och filändelse.

Slutligen returnerar funktionen True för att indikera att bilden laddades ner och sparades framgångsrikt. Om något undantag uppstår under processen fångas det, ett felmeddelande skrivs ut som visar att nedladdningen misslyckades, och funktionen returnerar False.

Denna funktion är användbar för att ladda ner bilder från URL:er och spara dem lokalt. Den hanterar potentiella fel under nedladdningen och ger feedback om nedladdningen lyckades eller inte.

Det är värt att notera att requests-biblioteket används för att göra HTTP-förfrågningar, PIL-biblioteket används för att arbeta med bilder, och BytesIO-klassen används för att hantera bilddatan som en byte-ström.

### Slutsats

Detta skript erbjuder ett smidigt sätt att förbereda ett dataset för maskininlärning genom att ladda ner nödvändiga bilder, filtrera bort rader där bildnedladdning misslyckas, och spara datasetet som en CSV-fil.

### Exempelskript

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

### Exempel på kod för nedladdning  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Exempel på dataset  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.