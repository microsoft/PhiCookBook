# Generate Image Data Set dengan mengunduh DataSet dari Hugging Face dan gambar terkait


### Ikhtisar

Script ini menyiapkan dataset untuk machine learning dengan mengunduh gambar yang dibutuhkan, menyaring baris yang gagal mengunduh gambar, dan menyimpan dataset sebagai file CSV.

### Prasyarat

Sebelum menjalankan script ini, pastikan sudah menginstal library berikut: `Pandas`, `Datasets`, `requests`, `PIL`, dan `io`. Anda juga perlu mengganti `'Insert_Your_Dataset'` pada baris ke-2 dengan nama dataset Anda dari Hugging Face.

Library yang dibutuhkan:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Fungsionalitas

Script ini melakukan langkah-langkah berikut:

1. Mengunduh dataset dari Hugging Face menggunakan fungsi `load_dataset()`.
2. Mengonversi dataset Hugging Face ke Pandas DataFrame agar lebih mudah dimanipulasi menggunakan metode `to_pandas()`.
3. Membuat direktori untuk menyimpan dataset dan gambar.
4. Menyaring baris yang gagal mengunduh gambar dengan cara mengiterasi setiap baris di DataFrame, mengunduh gambar menggunakan fungsi kustom `download_image()`, dan menambahkan baris yang lolos filter ke DataFrame baru bernama `filtered_rows`.
5. Membuat DataFrame baru dengan baris yang sudah disaring dan menyimpannya ke disk sebagai file CSV.
6. Mencetak pesan yang menunjukkan lokasi penyimpanan dataset dan gambar.

### Fungsi Kustom

Fungsi `download_image()` mengunduh gambar dari URL dan menyimpannya secara lokal menggunakan Pillow Image Library (PIL) dan modul `io`. Fungsi ini mengembalikan True jika gambar berhasil diunduh, dan False jika gagal. Fungsi ini juga akan melemparkan exception dengan pesan error jika permintaan gagal.

### Bagaimana cara kerjanya

Fungsi download_image menerima dua parameter: image_url, yaitu URL gambar yang akan diunduh, dan save_path, yaitu jalur tempat gambar yang diunduh akan disimpan.

Berikut cara kerja fungsi ini:

Fungsi dimulai dengan melakukan permintaan GET ke image_url menggunakan metode requests.get. Ini mengambil data gambar dari URL tersebut.

Baris response.raise_for_status() memeriksa apakah permintaan berhasil. Jika kode status respons menunjukkan error (misalnya, 404 - Not Found), maka akan melempar exception. Ini memastikan kita hanya melanjutkan mengunduh gambar jika permintaan berhasil.

Data gambar kemudian diteruskan ke metode Image.open dari modul PIL (Python Imaging Library). Metode ini membuat objek Image dari data gambar tersebut.

Baris image.save(save_path) menyimpan gambar ke jalur save_path yang ditentukan. save_path harus mencakup nama file dan ekstensi yang diinginkan.

Terakhir, fungsi mengembalikan True untuk menandakan gambar berhasil diunduh dan disimpan. Jika terjadi exception selama proses, fungsi akan menangkap exception tersebut, mencetak pesan error yang menunjukkan kegagalan, dan mengembalikan False.

Fungsi ini berguna untuk mengunduh gambar dari URL dan menyimpannya secara lokal. Fungsi ini menangani kemungkinan error selama proses pengunduhan dan memberikan umpan balik apakah pengunduhan berhasil atau tidak.

Perlu dicatat bahwa library requests digunakan untuk melakukan permintaan HTTP, library PIL digunakan untuk bekerja dengan gambar, dan kelas BytesIO digunakan untuk menangani data gambar sebagai aliran byte.


### Kesimpulan

Script ini menyediakan cara yang praktis untuk menyiapkan dataset untuk machine learning dengan mengunduh gambar yang dibutuhkan, menyaring baris yang gagal mengunduh gambar, dan menyimpan dataset sebagai file CSV.

### Contoh Script

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

### Contoh Kode Download  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Contoh Data Set  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.