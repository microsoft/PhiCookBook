# Generowanie zestawu danych obrazów poprzez pobranie DataSet z Hugging Face oraz powiązanych obrazów


### Przegląd

Ten skrypt przygotowuje zestaw danych do uczenia maszynowego, pobierając wymagane obrazy, filtrując wiersze, w których pobranie obrazu się nie powiodło, oraz zapisując zestaw danych jako plik CSV.

### Wymagania wstępne

Przed uruchomieniem tego skryptu upewnij się, że masz zainstalowane następujące biblioteki: `Pandas`, `Datasets`, `requests`, `PIL` oraz `io`. Należy również zastąpić `'Insert_Your_Dataset'` w linii 2 nazwą swojego zestawu danych z Hugging Face.

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

1. Pobiera zestaw danych z Hugging Face za pomocą funkcji `load_dataset()`.
2. Konwertuje zestaw danych Hugging Face na Pandas DataFrame, aby ułatwić manipulację, używając metody `to_pandas()`.
3. Tworzy katalogi do zapisu zestawu danych i obrazów.
4. Filtruje wiersze, w których pobranie obrazu się nie powiodło, iterując przez każdy wiersz DataFrame, pobierając obraz za pomocą niestandardowej funkcji `download_image()` i dodając przefiltrowany wiersz do nowego DataFrame o nazwie `filtered_rows`.
5. Tworzy nowy DataFrame z przefiltrowanymi wierszami i zapisuje go na dysku jako plik CSV.
6. Wyświetla komunikat informujący, gdzie zostały zapisane zestaw danych i obrazy.

### Niestandardowa funkcja

Funkcja `download_image()` pobiera obraz z URL i zapisuje go lokalnie, korzystając z biblioteki Pillow (PIL) oraz modułu `io`. Zwraca True, jeśli obraz został pobrany pomyślnie, a False w przeciwnym wypadku. Funkcja zgłasza również wyjątek z komunikatem o błędzie, gdy żądanie się nie powiedzie.

### Jak to działa

Funkcja download_image przyjmuje dwa parametry: image_url, czyli adres URL obrazu do pobrania, oraz save_path, czyli ścieżkę, gdzie pobrany obraz zostanie zapisany.

Oto jak działa ta funkcja:

Zaczyna od wykonania żądania GET do image_url za pomocą metody requests.get. Pobiera to dane obrazu z podanego adresu URL.

Linia response.raise_for_status() sprawdza, czy żądanie zakończyło się sukcesem. Jeśli kod statusu odpowiedzi wskazuje na błąd (np. 404 - Nie znaleziono), zostanie zgłoszony wyjątek. Zapewnia to, że pobieranie obrazu będzie kontynuowane tylko wtedy, gdy żądanie zakończy się powodzeniem.

Dane obrazu są następnie przekazywane do metody Image.open z modułu PIL (Python Imaging Library). Metoda ta tworzy obiekt Image na podstawie danych obrazu.

Linia image.save(save_path) zapisuje obraz pod wskazaną ścieżką save_path. Ścieżka ta powinna zawierać nazwę pliku oraz rozszerzenie.

Na koniec funkcja zwraca True, aby wskazać, że obraz został pomyślnie pobrany i zapisany. Jeśli podczas procesu wystąpi jakikolwiek wyjątek, zostanie on przechwycony, wyświetlony zostanie komunikat o błędzie informujący o niepowodzeniu, a funkcja zwróci False.

Ta funkcja jest przydatna do pobierania obrazów z adresów URL i zapisywania ich lokalnie. Obsługuje potencjalne błędy podczas pobierania i informuje, czy pobranie zakończyło się sukcesem.

Warto zauważyć, że biblioteka requests służy do wykonywania żądań HTTP, biblioteka PIL do pracy z obrazami, a klasa BytesIO do obsługi danych obrazu jako strumienia bajtów.



### Podsumowanie

Ten skrypt oferuje wygodny sposób przygotowania zestawu danych do uczenia maszynowego poprzez pobranie wymaganych obrazów, odfiltrowanie wierszy, w których pobranie obrazu się nie powiodło, oraz zapisanie zestawu danych jako plik CSV.

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
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.