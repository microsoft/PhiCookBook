# Hugging Face'den Veri Seti ve İlgili Görselleri İndirerek Görsel Veri Seti Oluşturma


### Genel Bakış

Bu betik, makine öğrenimi için gerekli görselleri indirerek, görsel indirme işlemi başarısız olan satırları filtreleyerek ve veri setini CSV dosyası olarak kaydederek bir veri seti hazırlar.

### Gereksinimler

Bu betiği çalıştırmadan önce, `Pandas`, `Datasets`, `requests`, `PIL` ve `io` kütüphanelerinin yüklü olduğundan emin olun. Ayrıca, 2. satırdaki `'Insert_Your_Dataset'` ifadesini Hugging Face'deki veri setinizin adıyla değiştirmeniz gerekmektedir.

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

Betik aşağıdaki adımları gerçekleştirir:

1. `load_dataset()` fonksiyonunu kullanarak veri setini Hugging Face'den indirir.
2. Hugging Face veri setini, `to_pandas()` yöntemi ile daha kolay işlenebilmesi için Pandas DataFrame'e dönüştürür.
3. Veri seti ve görselleri kaydetmek için klasörler oluşturur.
4. DataFrame'deki her satırı dolaşarak, özel `download_image()` fonksiyonunu kullanıp görseli indirir ve görsel indirme başarısız olan satırları filtreleyerek `filtered_rows` adlı yeni bir DataFrame'e ekler.
5. Filtrelenmiş satırlardan oluşan yeni DataFrame'i oluşturur ve diske CSV dosyası olarak kaydeder.
6. Veri setinin ve görsellerin nerede kaydedildiğini belirten bir mesaj yazdırır.

### Özel Fonksiyon

`download_image()` fonksiyonu, bir URL'den görsel indirir ve Pillow Image Library (PIL) ile `io` modülünü kullanarak yerel olarak kaydeder. Görsel başarıyla indirildiyse True, aksi takdirde False döner. İstek başarısız olursa hata mesajı ile birlikte bir istisna fırlatır.

### Nasıl Çalışır

download_image fonksiyonu iki parametre alır: indirilecek görselin URL'si olan image_url ve indirilen görselin kaydedileceği yol olan save_path.

Fonksiyonun çalışma şekli şöyledir:

İlk olarak, requests.get yöntemiyle image_url adresine GET isteği yapar. Bu, URL'den görsel verisini alır.

response.raise_for_status() satırı, isteğin başarılı olup olmadığını kontrol eder. Eğer yanıt durumu bir hata (örneğin 404 - Bulunamadı) gösteriyorsa, bir istisna fırlatır. Bu sayede yalnızca istek başarılıysa görsel indirme işlemine devam edilir.

Görsel verisi, PIL (Python Imaging Library) modülünden Image.open metoduna aktarılır. Bu metod, görsel verisinden bir Image nesnesi oluşturur.

image.save(save_path) satırı, görseli belirtilen save_path konumuna kaydeder. save_path, istenen dosya adı ve uzantısını içermelidir.

Son olarak, fonksiyon görselin başarıyla indirildiğini ve kaydedildiğini belirtmek için True döner. İşlem sırasında herhangi bir istisna oluşursa, bu yakalanır, başarısızlığı belirten bir hata mesajı yazdırılır ve False döner.

Bu fonksiyon, URL'lerden görsel indirip yerel olarak kaydetmek için kullanışlıdır. İndirme sürecindeki olası hataları yönetir ve indirme işleminin başarılı olup olmadığını bildirir.

requests kütüphanesi HTTP istekleri yapmak için, PIL kütüphanesi görsellerle çalışmak için ve BytesIO sınıfı görsel verisini bayt akışı olarak işlemek için kullanılır.



### Sonuç

Bu betik, makine öğrenimi için gerekli görselleri indirerek, görsel indirme işlemi başarısız olan satırları filtreleyerek ve veri setini CSV dosyası olarak kaydederek veri seti hazırlamak için pratik bir yöntem sunar.

### Örnek Betik

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
[Yeni Veri Seti Oluşturma betiği](../../../../code/04.Finetuning/generate_dataset.py)

### Örnek Veri Seti
[LORA ile ince ayar örneğinden Örnek Veri Seti](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.