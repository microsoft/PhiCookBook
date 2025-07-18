<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:50:51+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ms"
}
-->
# Jana Set Data Imej dengan memuat turun DataSet dari Hugging Face dan imej berkaitan


### Gambaran Keseluruhan

Skrip ini menyediakan set data untuk pembelajaran mesin dengan memuat turun imej yang diperlukan, menapis baris di mana muat turun imej gagal, dan menyimpan set data sebagai fail CSV.

### Prasyarat

Sebelum menjalankan skrip ini, pastikan perpustakaan berikut telah dipasang: `Pandas`, `Datasets`, `requests`, `PIL`, dan `io`. Anda juga perlu menggantikan `'Insert_Your_Dataset'` pada baris 2 dengan nama set data anda dari Hugging Face.

Perpustakaan Diperlukan:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Fungsi

Skrip ini melaksanakan langkah-langkah berikut:

1. Memuat turun set data dari Hugging Face menggunakan fungsi `load_dataset()`.
2. Menukar set data Hugging Face kepada DataFrame Pandas untuk memudahkan manipulasi menggunakan kaedah `to_pandas()`.
3. Membuat direktori untuk menyimpan set data dan imej.
4. Menapis baris di mana muat turun imej gagal dengan mengulangi setiap baris dalam DataFrame, memuat turun imej menggunakan fungsi khusus `download_image()`, dan menambah baris yang ditapis ke DataFrame baru bernama `filtered_rows`.
5. Membuat DataFrame baru dengan baris yang ditapis dan menyimpannya ke cakera sebagai fail CSV.
6. Mencetak mesej yang menunjukkan lokasi set data dan imej telah disimpan.

### Fungsi Khusus

Fungsi `download_image()` memuat turun imej dari URL dan menyimpannya secara tempatan menggunakan Perpustakaan Imej Pillow (PIL) dan modul `io`. Ia mengembalikan True jika imej berjaya dimuat turun, dan False jika tidak. Fungsi ini juga akan membangkitkan pengecualian dengan mesej ralat apabila permintaan gagal.

### Bagaimana ia berfungsi

Fungsi download_image mengambil dua parameter: image_url, iaitu URL imej yang hendak dimuat turun, dan save_path, iaitu laluan di mana imej yang dimuat turun akan disimpan.

Berikut adalah cara fungsi ini berfungsi:

Ia bermula dengan membuat permintaan GET ke image_url menggunakan kaedah requests.get. Ini mengambil data imej dari URL tersebut.

Baris response.raise_for_status() memeriksa sama ada permintaan berjaya. Jika kod status respons menunjukkan ralat (contohnya, 404 - Tidak Dijumpai), ia akan membangkitkan pengecualian. Ini memastikan kita hanya meneruskan muat turun imej jika permintaan berjaya.

Data imej kemudian dihantar ke kaedah Image.open dari modul PIL (Python Imaging Library). Kaedah ini mencipta objek Image daripada data imej tersebut.

Baris image.save(save_path) menyimpan imej ke save_path yang ditetapkan. save_path harus termasuk nama fail dan sambungan yang dikehendaki.

Akhir sekali, fungsi mengembalikan True untuk menunjukkan imej berjaya dimuat turun dan disimpan. Jika sebarang pengecualian berlaku semasa proses, ia akan menangkap pengecualian tersebut, mencetak mesej ralat yang menunjukkan kegagalan, dan mengembalikan False.

Fungsi ini berguna untuk memuat turun imej dari URL dan menyimpannya secara tempatan. Ia mengendalikan kemungkinan ralat semasa proses muat turun dan memberikan maklum balas sama ada muat turun berjaya atau tidak.

Perlu diingat bahawa perpustakaan requests digunakan untuk membuat permintaan HTTP, perpustakaan PIL digunakan untuk bekerja dengan imej, dan kelas BytesIO digunakan untuk mengendalikan data imej sebagai aliran bait.



### Kesimpulan

Skrip ini menyediakan cara mudah untuk menyediakan set data bagi pembelajaran mesin dengan memuat turun imej yang diperlukan, menapis baris di mana muat turun imej gagal, dan menyimpan set data sebagai fail CSV.

### Skrip Contoh

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

### Muat Turun Kod Contoh  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Set Data Contoh
[Contoh Set Data dari finetuning dengan contoh LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.