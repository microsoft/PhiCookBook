<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:24:01+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "it"
}
-->
# Genera un set di dati di immagini scaricando il DataSet da Hugging Face e le immagini associate


### Panoramica

Questo script prepara un dataset per il machine learning scaricando le immagini necessarie, filtrando le righe in cui il download delle immagini fallisce e salvando il dataset in un file CSV.

### Prerequisiti

Prima di eseguire questo script, assicurati di avere installato le seguenti librerie: `Pandas`, `Datasets`, `requests`, `PIL` e `io`. Inoltre, dovrai sostituire `'Insert_Your_Dataset'` alla riga 2 con il nome del tuo dataset da Hugging Face.

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

1. Scarica il dataset da Hugging Face utilizzando la funzione `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` scarica un'immagine da un URL e la salva localmente usando la libreria Pillow Image (PIL) e il modulo `io`. Restituisce True se l'immagine è stata scaricata con successo, False altrimenti. La funzione solleva anche un'eccezione con il messaggio di errore in caso di fallimento della richiesta.

### Come funziona

La funzione download_image prende due parametri: image_url, che è l'URL dell'immagine da scaricare, e save_path, che è il percorso dove l'immagine scaricata verrà salvata.

Ecco come funziona la funzione:

Inizia effettuando una richiesta GET all'URL image_url usando il metodo requests.get. Questo recupera i dati dell'immagine dall'URL.

La riga response.raise_for_status() verifica se la richiesta è andata a buon fine. Se il codice di stato della risposta indica un errore (ad esempio 404 - Non trovato), solleverà un'eccezione. Questo garantisce che si proceda al download solo se la richiesta è stata corretta.

I dati dell'immagine vengono poi passati al metodo Image.open del modulo PIL (Python Imaging Library). Questo metodo crea un oggetto Image dai dati dell'immagine.

La riga image.save(save_path) salva l'immagine nel percorso save_path specificato. Il save_path deve includere il nome file desiderato e l'estensione.

Infine, la funzione restituisce True per indicare che l'immagine è stata scaricata e salvata con successo. Se si verifica un'eccezione durante il processo, questa viene catturata, viene stampato un messaggio di errore che indica il fallimento e la funzione restituisce False.

Questa funzione è utile per scaricare immagini da URL e salvarle localmente. Gestisce potenziali errori durante il download e fornisce un feedback sul successo o meno dell'operazione.

Vale la pena sottolineare che la libreria requests viene utilizzata per effettuare richieste HTTP, la libreria PIL per lavorare con le immagini, e la classe BytesIO per gestire i dati dell'immagine come flusso di byte.



### Conclusione

Questo script offre un modo semplice per preparare un dataset per il machine learning scaricando le immagini necessarie, filtrando le righe con download falliti e salvando il dataset in un file CSV.

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

### Download del codice di esempio  
[Genera uno script per un nuovo Data Set](../../../../code/04.Finetuning/generate_dataset.py)

### Data Set di esempio
[Esempio di Data Set da finetuning con LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.