<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:52:02+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ro"
}
-->
# Generare Set de Date pentru Imagini prin descărcarea DataSet-ului de pe Hugging Face și imaginile asociate


### Prezentare generală

Acest script pregătește un set de date pentru învățare automată prin descărcarea imaginilor necesare, filtrarea rândurilor unde descărcarea imaginilor eșuează și salvarea setului de date ca fișier CSV.

### Cerințe preliminare

Înainte de a rula acest script, asigură-te că ai instalat următoarele biblioteci: `Pandas`, `Datasets`, `requests`, `PIL` și `io`. De asemenea, va trebui să înlocuiești `'Insert_Your_Dataset'` de pe linia 2 cu numele setului tău de date de pe Hugging Face.

Biblioteci necesare:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funcționalitate

Scriptul execută următorii pași:

1. Descarcă setul de date de pe Hugging Face folosind funcția `load_dataset()`.
2. Convertește setul de date Hugging Face într-un DataFrame Pandas pentru o manipulare mai ușoară, folosind metoda `to_pandas()`.
3. Creează directoare pentru salvarea setului de date și a imaginilor.
4. Filtrează rândurile unde descărcarea imaginii eșuează, parcurgând fiecare rând din DataFrame, descărcând imaginea cu funcția personalizată `download_image()` și adăugând rândul filtrat într-un nou DataFrame numit `filtered_rows`.
5. Creează un nou DataFrame cu rândurile filtrate și îl salvează pe disc ca fișier CSV.
6. Afișează un mesaj care indică unde au fost salvate setul de date și imaginile.

### Funcție personalizată

Funcția `download_image()` descarcă o imagine de la o adresă URL și o salvează local folosind biblioteca Pillow Image (PIL) și modulul `io`. Returnează True dacă imaginea a fost descărcată cu succes și False în caz contrar. Funcția ridică o excepție cu mesajul de eroare atunci când cererea eșuează.

### Cum funcționează

Funcția download_image primește doi parametri: image_url, care este URL-ul imaginii ce trebuie descărcată, și save_path, care este calea unde imaginea descărcată va fi salvată.

Iată cum funcționează funcția:

Începe prin a face o cerere GET către image_url folosind metoda requests.get. Aceasta preia datele imaginii de la URL.

Linia response.raise_for_status() verifică dacă cererea a fost realizată cu succes. Dacă codul de stare al răspunsului indică o eroare (de exemplu, 404 - Nu a fost găsit), va ridica o excepție. Acest lucru asigură că descărcarea imaginii continuă doar dacă cererea a fost reușită.

Datele imaginii sunt apoi transmise metodei Image.open din modulul PIL (Python Imaging Library). Această metodă creează un obiect Image din datele imaginii.

Linia image.save(save_path) salvează imaginea la calea specificată prin save_path. save_path trebuie să includă numele fișierului dorit și extensia.

În final, funcția returnează True pentru a indica faptul că imaginea a fost descărcată și salvată cu succes. Dacă apare vreo excepție în timpul procesului, aceasta este prinsă, se afișează un mesaj de eroare care indică eșecul și se returnează False.

Această funcție este utilă pentru descărcarea imaginilor de la URL-uri și salvarea lor locală. Gestionează eventualele erori apărute în timpul procesului de descărcare și oferă feedback dacă descărcarea a fost reușită sau nu.

Este important de menționat că biblioteca requests este folosită pentru a face cereri HTTP, biblioteca PIL este folosită pentru a lucra cu imagini, iar clasa BytesIO este folosită pentru a gestiona datele imaginii ca un flux de octeți.



### Concluzie

Acest script oferă o metodă convenabilă de a pregăti un set de date pentru învățare automată prin descărcarea imaginilor necesare, filtrarea rândurilor unde descărcarea imaginilor eșuează și salvarea setului de date ca fișier CSV.

### Script exemplu

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

### Cod exemplu pentru descărcare  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Set de date exemplu  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.