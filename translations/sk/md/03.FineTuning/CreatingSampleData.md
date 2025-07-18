<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:51:48+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sk"
}
-->
# Generovanie dátovej sady obrázkov stiahnutím DataSetu z Hugging Face a súvisiacich obrázkov


### Prehľad

Tento skript pripravuje dátovú sadu pre strojové učenie tým, že stiahne potrebné obrázky, odfiltruje riadky, kde sťahovanie obrázkov zlyhá, a uloží dátovú sadu ako CSV súbor.

### Požiadavky

Pred spustením tohto skriptu sa uistite, že máte nainštalované nasledujúce knižnice: `Pandas`, `Datasets`, `requests`, `PIL` a `io`. Tiež je potrebné nahradiť `'Insert_Your_Dataset'` v riadku 2 názvom vašej dátovej sady z Hugging Face.

Požadované knižnice:

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

1. Stiahne dátovú sadu z Hugging Face pomocou funkcie `load_dataset()`.
2. Prevedie dátovú sadu z Hugging Face na Pandas DataFrame pre jednoduchšiu manipuláciu pomocou metódy `to_pandas()`.
3. Vytvorí adresáre na uloženie dátovej sady a obrázkov.
4. Odfiltruje riadky, kde sťahovanie obrázkov zlyhá, prechádzaním každého riadku v DataFrame, stiahnutím obrázka pomocou vlastnej funkcie `download_image()` a pridá filtrovaný riadok do nového DataFrame nazvaného `filtered_rows`.
5. Vytvorí nový DataFrame s filtrovanými riadkami a uloží ho na disk ako CSV súbor.
6. Vypíše správu, kde bola dátová sada a obrázky uložené.

### Vlastná funkcia

Funkcia `download_image()` stiahne obrázok z URL a uloží ho lokálne pomocou knižnice Pillow Image Library (PIL) a modulu `io`. Vráti True, ak sa obrázok úspešne stiahne, inak False. Funkcia tiež vyvolá výnimku s chybovou správou, ak požiadavka zlyhá.

### Ako to funguje

Funkcia download_image prijíma dva parametre: image_url, čo je URL obrázka na stiahnutie, a save_path, čo je cesta, kam sa stiahnutý obrázok uloží.

Takto funkcia funguje:

Najprv vykoná GET požiadavku na image_url pomocou metódy requests.get. Tým získa dáta obrázka z URL.

Riadok response.raise_for_status() overuje, či bola požiadavka úspešná. Ak stavový kód odpovede signalizuje chybu (napr. 404 - Nenájdené), vyvolá výnimku. Tým sa zabezpečí, že pokračujeme v sťahovaní obrázka len v prípade úspešnej požiadavky.

Dáta obrázka sa potom odovzdajú metóde Image.open z modulu PIL (Python Imaging Library). Táto metóda vytvorí objekt Image z dát obrázka.

Riadok image.save(save_path) uloží obrázok na určenú cestu save_path. Cesta save_path by mala obsahovať požadovaný názov súboru a príponu.

Nakoniec funkcia vráti True, čo znamená, že obrázok bol úspešne stiahnutý a uložený. Ak počas procesu nastane výnimka, tá sa zachytí, vypíše sa chybová správa o neúspechu a funkcia vráti False.

Táto funkcia je užitočná na sťahovanie obrázkov z URL a ich lokálne uloženie. Zvláda možné chyby počas sťahovania a poskytuje spätnú väzbu o úspešnosti sťahovania.

Je dôležité poznamenať, že knižnica requests sa používa na HTTP požiadavky, knižnica PIL na prácu s obrázkami a trieda BytesIO na spracovanie dát obrázka ako prúdu bajtov.



### Záver

Tento skript poskytuje jednoduchý spôsob, ako pripraviť dátovú sadu pre strojové učenie stiahnutím potrebných obrázkov, odfiltrovaním riadkov, kde sťahovanie zlyhá, a uložením dátovej sady ako CSV súbor.

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

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.