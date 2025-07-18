<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:51:12+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "sw"
}
-->
# Tengeneza Seti ya Data ya Picha kwa kupakua DataSet kutoka Hugging Face na picha zinazohusiana

### Muhtasari

Script hii huandaa seti ya data kwa ajili ya mashine kujifunza kwa kupakua picha zinazohitajika, kuchuja mistari ambapo upakuaji wa picha unashindwa, na kuhifadhi seti ya data kama faili la CSV.

### Mahitaji

Kabla ya kuendesha script hii, hakikisha umeweka maktaba zifuatazo: `Pandas`, `Datasets`, `requests`, `PIL`, na `io`. Pia utahitaji kubadilisha `'Insert_Your_Dataset'` kwenye mstari wa 2 na jina la seti yako ya data kutoka Hugging Face.

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

1. Inapakua seti ya data kutoka Hugging Face kwa kutumia kazi ya `load_dataset()`.
2. Inageuza seti ya data ya Hugging Face kuwa Pandas DataFrame kwa urahisi wa usindikaji kwa kutumia njia ya `to_pandas()`.
3. Inaunda folda za kuhifadhi seti ya data na picha.
4. Inachuja mistari ambapo upakuaji wa picha unashindwa kwa kupitia kila mstari katika DataFrame, kupakua picha kwa kutumia kazi maalum ya `download_image()`, na kuongeza mstari uliosafishwa kwenye DataFrame mpya iitwayo `filtered_rows`.
5. Inaunda DataFrame mpya yenye mistari iliyochujwa na kuihifadhi kwenye diski kama faili la CSV.
6. Inachapisha ujumbe unaoonyesha mahali seti ya data na picha zimehifadhiwa.

### Kazi Maalum

Kazi ya `download_image()` hupakua picha kutoka kwenye URL na kuihifadhi kwa ndani kwa kutumia Maktaba ya Pillow Image (PIL) na moduli ya `io`. Inarudisha True ikiwa picha imesafirishwa kwa mafanikio, na False vinginevyo. Kazi hii pia hutupa kosa lenye ujumbe wa makosa wakati ombi linaposhindwa.

### Jinsi inavyofanya kazi

Kazi ya download_image inachukua vigezo viwili: image_url, ambayo ni URL ya picha inayopakuliwa, na save_path, ambayo ni njia ambapo picha iliyopakuliwa itahifadhiwa.

Hivi ndivyo kazi inavyofanya kazi:

Inaanza kwa kutuma ombi la GET kwa image_url kwa kutumia njia ya requests.get. Hii inapata data ya picha kutoka kwenye URL.

Mstari wa response.raise_for_status() unahakikisha kama ombi lilifanikiwa. Ikiwa msimbo wa hali ya jibu unaonyesha kosa (mfano, 404 - Haipatikani), itatoa kosa. Hii inahakikisha kuwa tunaendelea kupakua picha tu ikiwa ombi lilifanikiwa.

Data ya picha kisha hupitishwa kwa njia ya Image.open kutoka moduli ya PIL (Python Imaging Library). Njia hii huunda kitu cha Image kutoka kwa data ya picha.

Mstari wa image.save(save_path) unaweka picha kwenye save_path iliyotajwa. Save_path inapaswa kujumuisha jina la faili na kiendelezi kinachotakiwa.

Mwishowe, kazi inarudisha True kuonyesha kuwa picha imesafirishwa na kuhifadhiwa kwa mafanikio. Ikiwa kosa lolote litatokea wakati wa mchakato, linakamatwa, linachapisha ujumbe wa kosa unaoonyesha kushindwa, na kurudisha False.

Kazi hii ni muhimu kwa kupakua picha kutoka URL na kuzihifadhi kwa ndani. Inashughulikia makosa yanayoweza kutokea wakati wa upakuaji na kutoa mrejesho kama upakuaji ulifanikiwa au la.

Ni vyema kutambua kuwa maktaba ya requests hutumika kutuma maombi ya HTTP, maktaba ya PIL hutumika kufanya kazi na picha, na darasa la BytesIO hutumika kushughulikia data ya picha kama mtiririko wa bytes.

### Hitimisho

Script hii inatoa njia rahisi ya kuandaa seti ya data kwa mashine kujifunza kwa kupakua picha zinazohitajika, kuchuja mistari ambapo upakuaji wa picha unashindwa, na kuhifadhi seti ya data kama faili la CSV.

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

### Mfano wa Kupakua Msimbo  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Mfano wa Seti ya Data  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.