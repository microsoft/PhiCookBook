<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:26:45+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sk"
}
-->
# Generovanie dátovej sady obrázkov stiahnutím DataSetu z Hugging Face a súvisiacich obrázkov

### Prehľad

Tento skript pripravuje dátovú sadu pre strojové učenie tým, že stiahne potrebné obrázky, odfiltruje riadky, kde sťahovanie obrázkov zlyhá, a uloží dátovú sadu vo formáte CSV.

### Požiadavky

Pred spustením tohto skriptu sa uistite, že máte nainštalované nasledujúce knižnice: `Pandas`, `Datasets`, `requests`, `PIL` a `io`. Tiež budete musieť v riadku 2 nahradiť `'Insert_Your_Dataset'` názvom vašej dátovej sady z Hugging Face.

Povinné knižnice:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalita

Skript vykonáva nasledujúce kroky:

1. Stiahne dátovú sadu z Hugging Face pomocou funkcie `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`, ktorá stiahne obrázok z URL a uloží ho lokálne pomocou knižnice Pillow Image Library (PIL) a modulu `io`. Funkcia vráti True, ak sa obrázok úspešne stiahne, a False v opačnom prípade. V prípade chyby počas požiadavky vyvolá výnimku s chybovou správou.

### Ako to funguje

Funkcia download_image prijíma dva parametre: image_url, čo je URL obrázka, ktorý sa má stiahnuť, a save_path, čo je cesta, kam sa stiahnutý obrázok uloží.

Funkcia funguje nasledovne:

Najprv vykoná GET požiadavku na image_url pomocou metódy requests.get. Tým získa dáta obrázka z URL.

Riadok response.raise_for_status() overuje, či bola požiadavka úspešná. Ak stavový kód odpovede signalizuje chybu (napr. 404 - Nenájdené), vyvolá výnimku. Tým zabezpečíme, že obrázok sa bude sťahovať iba v prípade úspešnej odpovede.

Dáta obrázka sa potom odovzdajú metóde Image.open z modulu PIL (Python Imaging Library). Táto metóda vytvorí Image objekt z obrázkových dát.

Riadok image.save(save_path) uloží obrázok na určenú cestu save_path. Táto cesta by mala obsahovať požadovaný názov súboru a príponu.

Nakoniec funkcia vráti True, čím indikuje, že obrázok bol úspešne stiahnutý a uložený. Ak počas procesu nastane akákoľvek výnimka, funkcia ju zachytí, vypíše chybovú správu o neúspechu a vráti False.

Táto funkcia je užitočná na sťahovanie obrázkov z URL a ich lokálne uloženie. Rieši možné chyby počas sťahovania a poskytuje spätnú väzbu o tom, či bolo sťahovanie úspešné alebo nie.

Stojí za zmienku, že knižnica requests sa používa na HTTP požiadavky, knižnica PIL na prácu s obrázkami a trieda BytesIO na spracovanie obrázkových dát ako prúdu bajtov.

### Záver

Tento skript poskytuje jednoduchý spôsob, ako pripraviť dátovú sadu pre strojové učenie stiahnutím potrebných obrázkov, odfiltrovaním riadkov s neúspešným sťahovaním a uložením dátovej sady vo formáte CSV.

### Ukážkový skript

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

### Ukážkový kód na stiahnutie  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Ukážková dátová sada  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.