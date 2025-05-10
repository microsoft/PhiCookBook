<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:24:09+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "pl"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Przegląd

Ten skrypt przygotowuje zestaw danych do uczenia maszynowego, pobierając wymagane obrazy, filtrując wiersze, w których pobranie obrazów się nie powiodło, oraz zapisując zestaw danych jako plik CSV.

### Wymagania wstępne

Przed uruchomieniem tego skryptu upewnij się, że masz zainstalowane następujące biblioteki: `Pandas`, `Datasets`, `requests`, `PIL` oraz `io`. Będziesz także musiał zastąpić `'Insert_Your_Dataset'` w linii 2 nazwą swojego zestawu danych z Hugging Face.

Wymagane biblioteki:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcjonalność

Skrypt wykonuje następujące kroki:

1. Pobiera zestaw danych z Hugging Face za pomocą `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funkcja download_image() pobiera obraz z URL i zapisuje go lokalnie, korzystając z biblioteki Pillow Image (PIL) oraz modułu `io`. Zwraca True, jeśli obraz został pobrany pomyślnie, a False w przeciwnym razie. Funkcja zgłasza również wyjątek z komunikatem o błędzie, gdy żądanie się nie powiedzie.

### Jak to działa

Funkcja download_image przyjmuje dwa parametry: image_url, czyli URL obrazu do pobrania, oraz save_path, czyli ścieżkę, gdzie pobrany obraz zostanie zapisany.

Oto jak działa ta funkcja:

Zaczyna od wykonania żądania GET do image_url za pomocą metody requests.get. Pobiera to dane obrazu z URL.

Linia response.raise_for_status() sprawdza, czy żądanie zakończyło się sukcesem. Jeśli kod statusu odpowiedzi wskazuje na błąd (np. 404 - Nie znaleziono), zostanie zgłoszony wyjątek. Zapewnia to, że pobieranie obrazu jest kontynuowane tylko wtedy, gdy żądanie się powiodło.

Dane obrazu są następnie przekazywane do metody Image.open z modułu PIL (Python Imaging Library). Ta metoda tworzy obiekt Image z danych obrazu.

Linia image.save(save_path) zapisuje obraz pod określoną ścieżką save_path. Ścieżka save_path powinna zawierać żądaną nazwę pliku oraz rozszerzenie.

Na koniec funkcja zwraca True, aby wskazać, że obraz został pomyślnie pobrany i zapisany. Jeśli podczas procesu wystąpi jakikolwiek wyjątek, jest on przechwytywany, wyświetlany jest komunikat o błędzie wskazujący na niepowodzenie, a funkcja zwraca False.

Ta funkcja jest przydatna do pobierania obrazów z URL i zapisywania ich lokalnie. Obsługuje potencjalne błędy podczas pobierania oraz dostarcza informacje zwrotne o powodzeniu lub niepowodzeniu pobrania.

Warto zauważyć, że biblioteka requests jest używana do wykonywania żądań HTTP, biblioteka PIL do pracy z obrazami, a klasa BytesIO służy do obsługi danych obrazu jako strumienia bajtów.



### Podsumowanie

Ten skrypt zapewnia wygodny sposób przygotowania zestawu danych do uczenia maszynowego poprzez pobranie wymaganych obrazów, odfiltrowanie wierszy, w których pobranie obrazów się nie powiodło, oraz zapisanie zestawu danych jako pliku CSV.

### Przykładowy skrypt

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

### Przykładowy kod do pobrania 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Przykładowy zestaw danych
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło wiarygodne. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.