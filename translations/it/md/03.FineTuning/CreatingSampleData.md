<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:48:10+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "it"
}
-->
# Genera un Set di Dati Immagini scaricando il DataSet da Hugging Face e le immagini associate


### Panoramica

Questo script prepara un dataset per il machine learning scaricando le immagini necessarie, filtrando le righe in cui il download delle immagini fallisce, e salvando il dataset come file CSV.

### Prerequisiti

Prima di eseguire questo script, assicurati di avere installato le seguenti librerie: `Pandas`, `Datasets`, `requests`, `PIL` e `io`. Dovrai anche sostituire `'Insert_Your_Dataset'` alla riga 2 con il nome del tuo dataset da Hugging Face.

Librerie richieste:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funzionalità

Lo script esegue i seguenti passaggi:

1. Scarica il dataset da Hugging Face usando la funzione `load_dataset()`.
2. Converte il dataset di Hugging Face in un DataFrame Pandas per una manipolazione più semplice tramite il metodo `to_pandas()`.
3. Crea le directory per salvare il dataset e le immagini.
4. Filtra le righe in cui il download dell’immagine fallisce iterando su ogni riga del DataFrame, scaricando l’immagine con la funzione personalizzata `download_image()` e aggiungendo la riga filtrata a un nuovo DataFrame chiamato `filtered_rows`.
5. Crea un nuovo DataFrame con le righe filtrate e lo salva su disco come file CSV.
6. Stampa un messaggio che indica dove sono stati salvati il dataset e le immagini.

### Funzione Personalizzata

La funzione `download_image()` scarica un’immagine da un URL e la salva localmente usando la libreria Pillow (PIL) e il modulo `io`. Restituisce True se l’immagine viene scaricata con successo, altrimenti False. La funzione solleva anche un’eccezione con il messaggio di errore quando la richiesta fallisce.

### Come funziona

La funzione download_image prende due parametri: image_url, che è l’URL dell’immagine da scaricare, e save_path, che è il percorso dove salvare l’immagine scaricata.

Ecco come funziona la funzione:

Inizia effettuando una richiesta GET a image_url usando il metodo requests.get. Questo recupera i dati dell’immagine dall’URL.

La riga response.raise_for_status() verifica se la richiesta è andata a buon fine. Se il codice di stato della risposta indica un errore (ad esempio, 404 - Non trovato), solleverà un’eccezione. Questo garantisce che si proceda al download dell’immagine solo se la richiesta ha avuto successo.

I dati dell’immagine vengono poi passati al metodo Image.open del modulo PIL (Python Imaging Library). Questo metodo crea un oggetto Image dai dati dell’immagine.

La riga image.save(save_path) salva l’immagine nel percorso specificato da save_path. Il save_path deve includere il nome del file desiderato e l’estensione.

Infine, la funzione restituisce True per indicare che l’immagine è stata scaricata e salvata con successo. Se si verifica un’eccezione durante il processo, questa viene catturata, viene stampato un messaggio di errore che indica il fallimento e la funzione restituisce False.

Questa funzione è utile per scaricare immagini da URL e salvarle localmente. Gestisce eventuali errori durante il processo di download e fornisce un feedback sul successo o meno del download.

Vale la pena notare che la libreria requests viene usata per effettuare richieste HTTP, la libreria PIL per lavorare con le immagini, e la classe BytesIO per gestire i dati dell’immagine come flusso di byte.



### Conclusione

Questo script offre un modo semplice per preparare un dataset per il machine learning scaricando le immagini necessarie, filtrando le righe in cui il download delle immagini fallisce, e salvando il dataset come file CSV.

### Script di esempio

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

### Codice di esempio per il download  
[Genera uno script per un nuovo Data Set](../../../../code/04.Finetuning/generate_dataset.py)

### Data Set di esempio  
[Esempio di Data Set da finetuning con LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.