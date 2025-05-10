<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:26:36+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "cs"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Genel Bakış

Bu script, makine öğrenimi için gerekli görüntüleri indirerek, indirme başarısız olan satırları filtreleyerek ve veri setini CSV dosyası olarak kaydederek bir veri seti hazırlar.

### Ön Koşullar

Bu scripti çalıştırmadan önce, aşağıdaki kütüphanelerin yüklü olduğundan emin olun: `Pandas`, `Datasets`, `requests`, `PIL` ve `io`. Ayrıca, 2. satırdaki `'Insert_Your_Dataset'` ifadesini Hugging Face üzerindeki veri setinizin adı ile değiştirmeniz gerekmektedir.

Gerekli Kütüphaneler:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### İşlevsellik

Script aşağıdaki adımları gerçekleştirir:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` fonksiyonu, bir URL’den görüntü indirir ve Pillow Image Library (PIL) ile `io` modülünü kullanarak yerel olarak kaydeder. Görüntü başarıyla indirildiyse True, aksi halde False döner. İstek başarısız olursa hata mesajı içeren bir istisna fırlatır.

### Nasıl Çalışır

download_image fonksiyonu iki parametre alır: image_url, indirilecek görüntünün URL’si ve save_path, indirilen görüntünün kaydedileceği yol.

Fonksiyonun çalışma mantığı şöyledir:

İlk olarak, requests.get metodu ile image_url adresine GET isteği gönderilir. Bu, URL’den görüntü verisini alır.

response.raise_for_status() satırı, isteğin başarılı olup olmadığını kontrol eder. Eğer durum kodu bir hata gösteriyorsa (örneğin 404 - Bulunamadı), bir istisna fırlatır. Bu sayede yalnızca istek başarılıysa indirme işlemine devam edilir.

Görüntü verisi, PIL (Python Imaging Library) modülündeki Image.open metoduna aktarılır. Bu metod, görüntü verisinden bir Image nesnesi oluşturur.

image.save(save_path) satırı, görüntüyü belirtilen save_path yoluna kaydeder. save_path, dosya adı ve uzantısını içermelidir.

Son olarak, fonksiyon görüntünün başarıyla indirildiğini belirtmek için True döner. İşlem sırasında herhangi bir istisna oluşursa, istisna yakalanır, hata mesajı yazdırılır ve False döner.

Bu fonksiyon, URL’den görüntü indirip yerel olarak kaydetmek için kullanışlıdır. İndirme sırasında oluşabilecek hataları yönetir ve indirme durumuyla ilgili geri bildirim sağlar.

requests kütüphanesi HTTP istekleri yapmak için, PIL kütüphanesi görüntülerle çalışmak için ve BytesIO sınıfı ise görüntü verisini byte akışı olarak işlemek için kullanılır.


### Sonuç

Bu script, makine öğrenimi için gerekli görüntüleri indirerek, indirme başarısız olan satırları filtreleyerek ve veri setini CSV dosyası olarak kaydederek veri seti hazırlamanın pratik bir yolunu sunar.

### Örnek Script

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

### Örnek Kod İndir 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Örnek Veri Seti
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné výklady vzniklé použitím tohoto překladu.