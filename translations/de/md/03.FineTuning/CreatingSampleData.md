<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-03-27T13:32:35+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "de"
}
-->
# Erstelle ein Bild-Datensatz durch Herunterladen eines Datensatzes von Hugging Face und zugehöriger Bilder

### Überblick

Dieses Skript bereitet einen Datensatz für maschinelles Lernen vor, indem es die benötigten Bilder herunterlädt, Zeilen herausfiltert, bei denen das Herunterladen der Bilder fehlschlägt, und den Datensatz als CSV-Datei speichert.

### Voraussetzungen

Bevor Sie dieses Skript ausführen, stellen Sie sicher, dass die folgenden Bibliotheken installiert sind: `Pandas`, `Datasets`, `requests`, `PIL` und `io`. Außerdem müssen Sie `'Insert_Your_Dataset'` in Zeile 2 durch den Namen Ihres Datensatzes von Hugging Face ersetzen.

Benötigte Bibliotheken:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktionalität

Das Skript führt die folgenden Schritte aus:

1. Lädt den Datensatz von Hugging Face herunter mit der Funktion `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Die Funktion `download_image()` lädt ein Bild von einer URL herunter und speichert es lokal mithilfe der Pillow-Bibliothek (PIL) und des `io` Moduls. Sie gibt True zurück, wenn das Bild erfolgreich heruntergeladen wurde, und False, wenn nicht. Die Funktion löst außerdem eine Ausnahme aus und gibt eine Fehlermeldung aus, falls die Anfrage fehlschlägt.

### Wie funktioniert das?

Die Funktion `download_image` nimmt zwei Parameter entgegen: `image_url`, die URL des herunterzuladenden Bildes, und `save_path`, den Pfad, unter dem das heruntergeladene Bild gespeichert werden soll.

So funktioniert die Funktion:

Sie beginnt mit einer GET-Anfrage an `image_url` mithilfe der Methode `requests.get`. Dadurch werden die Bilddaten von der URL abgerufen.

Die Zeile `response.raise_for_status()` überprüft, ob die Anfrage erfolgreich war. Falls der Statuscode der Antwort auf einen Fehler hinweist (z. B. 404 - Nicht gefunden), wird eine Ausnahme ausgelöst. Dadurch wird sichergestellt, dass der Bilddownload nur fortgesetzt wird, wenn die Anfrage erfolgreich war.

Die Bilddaten werden dann an die Methode `Image.open` aus dem PIL-Modul (Python Imaging Library) übergeben. Diese Methode erstellt ein Image-Objekt aus den Bilddaten.

Die Zeile `image.save(save_path)` speichert das Bild unter dem angegebenen `save_path`. Der `save_path` sollte den gewünschten Dateinamen und die Erweiterung enthalten.

Abschließend gibt die Funktion `True` zurück, um anzuzeigen, dass das Bild erfolgreich heruntergeladen und gespeichert wurde. Falls während des Prozesses eine Ausnahme auftritt, wird diese abgefangen, eine Fehlermeldung ausgegeben, die auf den Fehler hinweist, und die Funktion gibt `False` zurück.

Diese Funktion ist nützlich, um Bilder von URLs herunterzuladen und lokal zu speichern. Sie behandelt potenzielle Fehler während des Download-Prozesses und gibt Feedback darüber, ob der Download erfolgreich war oder nicht.

Es ist erwähnenswert, dass die `requests`-Bibliothek für HTTP-Anfragen verwendet wird, die PIL-Bibliothek für die Arbeit mit Bildern und die `BytesIO`-Klasse für die Verarbeitung der Bilddaten als Byte-Stream.

### Fazit

Dieses Skript bietet eine praktische Möglichkeit, einen Datensatz für maschinelles Lernen vorzubereiten, indem es die benötigten Bilder herunterlädt, Zeilen herausfiltert, bei denen das Herunterladen der Bilder fehlschlägt, und den Datensatz als CSV-Datei speichert.

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

### Beispiel-Code herunterladen
[Generiere ein neues Datensatz-Skript](../../../../code/04.Finetuning/generate_dataset.py)

### Beispiel-Datensatz
[Beispiel-Datensatz aus der Feinabstimmung mit LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.