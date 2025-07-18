<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:51:36+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "cs"
}
-->
# Generování datové sady obrázků stažením DataSetu z Hugging Face a souvisejících obrázků


### Přehled

Tento skript připravuje datovou sadu pro strojové učení stažením potřebných obrázků, odstraněním řádků, kde se stahování obrázků nezdařilo, a uložením datové sady jako CSV soubor.

### Požadavky

Před spuštěním tohoto skriptu se ujistěte, že máte nainstalované následující knihovny: `Pandas`, `Datasets`, `requests`, `PIL` a `io`. Také je potřeba v řádku 2 nahradit `'Insert_Your_Dataset'` názvem vaší datové sady z Hugging Face.

Požadované knihovny:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkčnost

Skript provádí následující kroky:

1. Stáhne datovou sadu z Hugging Face pomocí funkce `load_dataset()`.
2. Převede datovou sadu z Hugging Face na Pandas DataFrame pro snadnější manipulaci pomocí metody `to_pandas()`.
3. Vytvoří složky pro uložení datové sady a obrázků.
4. Odfiltruje řádky, kde se stahování obrázku nezdařilo, tím, že projde každý řádek v DataFrame, stáhne obrázek pomocí vlastní funkce `download_image()` a přidá filtrovaný řádek do nového DataFrame nazvaného `filtered_rows`.
5. Vytvoří nový DataFrame s filtrovanými řádky a uloží ho na disk jako CSV soubor.
6. Vypíše zprávu, kde byla datová sada a obrázky uloženy.

### Vlastní funkce

Funkce `download_image()` stáhne obrázek z URL a uloží ho lokálně pomocí knihovny Pillow (PIL) a modulu `io`. Vrací True, pokud se obrázek úspěšně stáhne, a False v opačném případě. Funkce také vyvolá výjimku s chybovou zprávou, pokud požadavek selže.

### Jak to funguje

Funkce download_image přijímá dva parametry: image_url, což je URL obrázku ke stažení, a save_path, což je cesta, kam se obrázek uloží.

Funkce funguje takto:

Nejprve provede GET požadavek na image_url pomocí metody requests.get. Tím získá data obrázku z URL.

Řádek response.raise_for_status() ověřuje, zda byl požadavek úspěšný. Pokud stavový kód odpovědi signalizuje chybu (např. 404 - Nenalezeno), vyvolá výjimku. Tím zajistíme, že budeme pokračovat ve stahování obrázku pouze v případě úspěšného požadavku.

Data obrázku jsou následně předána metodě Image.open z modulu PIL (Python Imaging Library). Tato metoda vytvoří objekt Image z dat obrázku.

Řádek image.save(save_path) uloží obrázek na zadanou cestu save_path. Cesta by měla obsahovat požadovaný název souboru a příponu.

Nakonec funkce vrátí True, což znamená, že obrázek byl úspěšně stažen a uložen. Pokud během procesu dojde k výjimce, funkce ji zachytí, vypíše chybovou zprávu o neúspěchu a vrátí False.

Tato funkce je užitečná pro stahování obrázků z URL a jejich lokální ukládání. Zpracovává možné chyby během stahování a poskytuje zpětnou vazbu o úspěšnosti stahování.

Je třeba poznamenat, že knihovna requests se používá pro HTTP požadavky, knihovna PIL pro práci s obrázky a třída BytesIO pro zpracování dat obrázku jako proudu bytů.



### Závěr

Tento skript nabízí pohodlný způsob, jak připravit datovou sadu pro strojové učení stažením potřebných obrázků, odstraněním řádků, kde se stahování obrázků nezdařilo, a uložením datové sady jako CSV soubor.

### Ukázkový skript

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

### Ukázkový kód ke stažení  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Ukázková datová sada  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.