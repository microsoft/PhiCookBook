<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-07T10:21:21+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "de"
}
-->
# Datensatz für Bilderzeugung durch Herunterladen von DataSet von Hugging Face und zugehörigen Bildern


### Übersicht

Dieses Skript bereitet einen Datensatz für maschinelles Lernen vor, indem es die benötigten Bilder herunterlädt, Zeilen herausfiltert, bei denen der Bilddownload fehlschlägt, und den Datensatz als CSV-Datei speichert.

### Voraussetzungen

Bevor Sie dieses Skript ausführen, stellen Sie sicher, dass die folgenden Bibliotheken installiert sind: `Pandas`, `Datasets`, `requests`, `PIL` und `io`. Außerdem müssen Sie `'Insert_Your_Dataset'` in Zeile 2 durch den Namen Ihres Datensatzes von Hugging Face ersetzen.

Erforderliche Bibliotheken:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktionsweise

Das Skript führt die folgenden Schritte aus:

1. Lädt den Datensatz von Hugging Face mit der Funktion `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` herunter. Die Funktion download_image() lädt ein Bild von einer URL herunter und speichert es lokal mit der Pillow Image Library (PIL) und dem `io` Modul. Sie gibt True zurück, wenn das Bild erfolgreich heruntergeladen wurde, andernfalls False. Bei einem Fehler während der Anfrage wird eine Ausnahme mit der Fehlermeldung ausgelöst.

### Wie funktioniert das

Die Funktion download_image nimmt zwei Parameter entgegen: image_url, die URL des herunterzuladenden Bildes, und save_path, den Pfad, unter dem das heruntergeladene Bild gespeichert wird.

So funktioniert die Funktion:

Sie startet mit einer GET-Anfrage an die image_url mittels requests.get. Dadurch werden die Bilddaten von der URL abgerufen.

Die Zeile response.raise_for_status() überprüft, ob die Anfrage erfolgreich war. Wenn der Statuscode der Antwort einen Fehler anzeigt (z. B. 404 - Nicht gefunden), wird eine Ausnahme ausgelöst. So wird sichergestellt, dass das Bild nur heruntergeladen wird, wenn die Anfrage erfolgreich war.

Die Bilddaten werden anschließend an die Methode Image.open aus dem PIL (Python Imaging Library) Modul übergeben. Diese Methode erstellt ein Image-Objekt aus den Bilddaten.

Die Zeile image.save(save_path) speichert das Bild am angegebenen save_path. Der save_path sollte den gewünschten Dateinamen und die Dateiendung enthalten.

Zum Schluss gibt die Funktion True zurück, um anzuzeigen, dass das Bild erfolgreich heruntergeladen und gespeichert wurde. Tritt während des Prozesses eine Ausnahme auf, wird diese abgefangen, eine Fehlermeldung ausgegeben und False zurückgegeben.

Diese Funktion ist nützlich, um Bilder von URLs herunterzuladen und lokal zu speichern. Sie behandelt mögliche Fehler während des Downloads und gibt Rückmeldung, ob der Download erfolgreich war oder nicht.

Es sei erwähnt, dass die requests-Bibliothek für HTTP-Anfragen verwendet wird, die PIL-Bibliothek für die Bildverarbeitung zuständig ist und die BytesIO-Klasse dazu dient, die Bilddaten als Bytestrom zu verarbeiten.


### Fazit

Dieses Skript bietet eine praktische Möglichkeit, einen Datensatz für maschinelles Lernen vorzubereiten, indem es die benötigten Bilder herunterlädt, Zeilen mit fehlgeschlagenem Bilddownload herausfiltert und den Datensatz als CSV-Datei speichert.

### Beispielskript

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

### Beispielcode Download  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Beispiel-Datensatz  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.