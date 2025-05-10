<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:26:17+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sw"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Muhtasari

Script hii huandaa dataset kwa ajili ya mashine kujifunza kwa kupakua picha zinazohitajika, kuchuja mistari ambapo upakuaji wa picha umefaulu, na kuhifadhi dataset kama faili la CSV.

### Mahitaji

Kabla ya kuendesha script hii, hakikisha umeweka maktaba zifuatazo: `Pandas`, `Datasets`, `requests`, `PIL`, na `io`. Pia utahitaji kubadilisha `'Insert_Your_Dataset'` katika mstari wa 2 na jina la dataset yako kutoka Hugging Face.

Maktaba Zinazohitajika:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Utendaji

Script hufanya hatua zifuatazo:

1. Inapakua dataset kutoka Hugging Face kwa kutumia `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` kazi inayopakua picha kutoka URL na kuihifadhi kwa ndani kwa kutumia Pillow Image Library (PIL) na moduli ya `io`. Inarudisha True ikiwa picha imeshapakuliwa kwa mafanikio, na False vinginevyo. Kazi pia hutupa exception ikiwa ombi limekosea.

### Jinsi Hii Inavyofanya Kazi

Kazi ya download_image inachukua vigezo viwili: image_url, ambayo ni URL ya picha inayopakuliwa, na save_path, ambayo ni njia ambapo picha iliyopakuliwa itahifadhiwa.

Hivi ndivyo kazi inavyofanya kazi:

Inaanzia kwa kutuma ombi la GET kwa image_url kwa kutumia requests.get. Hii inapata data ya picha kutoka URL.

Mstari wa response.raise_for_status() unahakikisha kama ombi limefanikiwa. Ikiwa status code ya jibu inaonyesha hitilafu (mfano, 404 - Haipatikani), itatoa exception. Hii inahakikisha tunapakia picha tu ikiwa ombi limefanikiwa.

Data ya picha kisha hupitishwa kwa Image.open kutoka moduli ya PIL (Python Imaging Library). Hii hutengeneza kitu cha Image kutoka kwa data ya picha.

Mstari wa image.save(save_path) unahifadhi picha kwenye save_path iliyotajwa. save_path inapaswa kujumuisha jina la faili na kiambatisho kinachotakiwa.

Mwishowe, kazi inarudisha True kuonyesha kuwa picha imeshapakuliwa na kuhifadhiwa kwa mafanikio. Ikiwa kuna exception yoyote wakati wa mchakato, inakamata exception, kuchapisha ujumbe wa kosa unaoonyesha kushindwa, na kurudisha False.

Kazi hii ni muhimu kwa kupakua picha kutoka URL na kuzihifadhi kwa ndani. Inashughulikia makosa yanayoweza kutokea wakati wa upakuaji na kutoa mrejesho kama upakuaji umefanikiwa au la.

Ni muhimu kutambua kuwa maktaba ya requests hutumika kutuma ombi za HTTP, maktaba ya PIL hutumika kushughulikia picha, na darasa la BytesIO hutumika kushughulikia data ya picha kama mtiririko wa bytes.


### Hitimisho

Script hii inatoa njia rahisi ya kuandaa dataset kwa mashine kujifunza kwa kupakua picha zinazohitajika, kuchuja mistari ambapo upakuaji wa picha haukufanikiwa, na kuhifadhi dataset kama faili la CSV.

### Mfano wa Script

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

### Mfano wa Pakua Msimbo  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Mfano wa Data Set  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Kiasi cha Majukumu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inashauriwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.