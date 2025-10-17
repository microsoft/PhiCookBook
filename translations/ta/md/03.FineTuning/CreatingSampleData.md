<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-10-11T11:44:54+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ta"
}
-->
# Hugging Face-இல் இருந்து தரவுத்தொகுப்பை பதிவிறக்கம் செய்து, தொடர்புடைய படங்களைப் பயன்படுத்தி படத் தரவுத்தொகுப்பை உருவாக்குதல்

### கண்ணோட்டம்

இந்த ஸ்கிரிப்ட், தேவையான படங்களை பதிவிறக்கம் செய்து, படங்களை பதிவிறக்க முடியாத வரிசைகளை வடிகட்டி, தரவுத்தொகுப்பை CSV கோப்பாக சேமித்து, இயந்திரக் கற்றலுக்கான தரவுத்தொகுப்பை தயாரிக்கிறது.

### முன் தேவைகள்

இந்த ஸ்கிரிப்டை இயக்குவதற்கு முன், பின்வரும் நூலகங்கள் நிறுவப்பட்டிருக்க வேண்டும்: `Pandas`, `Datasets`, `requests`, `PIL`, மற்றும் `io`. மேலும், Hugging Face-இல் இருந்து உங்கள் தரவுத்தொகுப்பின் பெயரை `'Insert_Your_Dataset'` என வரி 2-ல் மாற்ற வேண்டும்.

தேவையான நூலகங்கள்:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```


### செயல்பாடு

ஸ்கிரிப்ட் பின்வரும் படிகளைச் செய்கிறது:

1. Hugging Face-இல் இருந்து `load_dataset()` செயல்பாட்டைப் பயன்படுத்தி தரவுத்தொகுப்பை பதிவிறக்குகிறது.
2. Hugging Face தரவுத்தொகுப்பை `to_pandas()` முறை மூலம் Pandas DataFrame-ஆக மாற்றுகிறது, இது எளிதாகக் கையாள உதவுகிறது.
3. தரவுத்தொகுப்பை மற்றும் படங்களைச் சேமிக்க டைரக்டரிகளை உருவாக்குகிறது.
4. DataFrame-இல் உள்ள ஒவ்வொரு வரிசையையும் மீண்டும் பார்க்கிறது, `download_image()` என்ற தனிப்பயன் செயல்பாட்டைப் பயன்படுத்தி படத்தை பதிவிறக்குகிறது, மற்றும் வடிகட்டப்பட்ட வரிசையை `filtered_rows` என்ற புதிய DataFrame-இல் சேர்க்கிறது.
5. வடிகட்டப்பட்ட வரிசைகளுடன் புதிய DataFrame-ஐ உருவாக்கி, அதை CSV கோப்பாக சேமிக்கிறது.
6. தரவுத்தொகுப்பும் படங்களும் எங்கு சேமிக்கப்பட்டுள்ளன என்பதைச் சுட்டிக்காட்டும் செய்தியை அச்சிடுகிறது.

### தனிப்பயன் செயல்பாடு

`download_image()` செயல்பாடு URL-இல் இருந்து ஒரு படத்தை பதிவிறக்கி, Pillow Image Library (PIL) மற்றும் `io` மொடியூலைப் பயன்படுத்தி உள்ளூரில் சேமிக்கிறது. படம் வெற்றிகரமாக பதிவிறக்கப்பட்டால் True-ஐ திருப்புகிறது, இல்லையெனில் False-ஐ திருப்புகிறது. கோரிக்கை தோல்வியடைந்தால், தவறான செய்தியுடன் ஒரு εξαிமாற்றத்தை எழுப்புகிறது.

### இது எப்படி வேலை செய்கிறது

`download_image()` செயல்பாடு இரண்டு அளவுருக்களை எடுத்துக்கொள்கிறது: `image_url`, இது பதிவிறக்க வேண்டிய படத்தின் URL, மற்றும் `save_path`, இது பதிவிறக்கப்பட்ட படம் சேமிக்கப்படும் பாதை.

செயல்பாடு எப்படி வேலை செய்கிறது:

- `requests.get` முறையைப் பயன்படுத்தி `image_url`-க்கு GET கோரிக்கையைச் செய்கிறது. இது URL-இல் இருந்து படத் தரவுகளைப் பெறுகிறது.
- `response.raise_for_status()` வரி கோரிக்கை வெற்றிகரமாக இருந்ததா என்பதைச் சரிபார்க்கிறது. கோரிக்கை தோல்வியடைந்தால் (எ.கா., 404 - கிடைக்கவில்லை), இது εξαிமாற்றத்தை எழுப்பும். கோரிக்கை வெற்றிகரமாக இருந்தால் மட்டுமே படத்தை பதிவிறக்க செயல்படுகிறது.
- படத் தரவுகள் PIL மொடியூலின் `Image.open` முறைக்கு அனுப்பப்படுகின்றன. இது படத் தரவுகளிலிருந்து ஒரு Image பொருளை உருவாக்குகிறது.
- `image.save(save_path)` வரி, படத்தை குறிப்பிட்ட `save_path`-இல் சேமிக்கிறது. `save_path`-இல் கோப்பின் பெயரும் நீட்டிப்பும் சேர்க்கப்பட்டிருக்க வேண்டும்.
- இறுதியாக, செயல்பாடு படம் வெற்றிகரமாக பதிவிறக்கப்பட்டு சேமிக்கப்பட்டது என்பதைச் சுட்டிக்காட்ட True-ஐ திருப்புகிறது. செயல்பாட்டின் போது ஏதேனும் தவறு ஏற்பட்டால், εξαிமாற்றத்தைப் பிடித்து, தோல்வியைச் சுட்டிக்காட்டும் ஒரு தவறான செய்தியை அச்சிடுகிறது மற்றும் False-ஐ திருப்புகிறது.

இந்த செயல்பாடு URL-களிலிருந்து படங்களை பதிவிறக்கி உள்ளூரில் சேமிக்க பயன்படுகிறது. பதிவிறக்க செயல்முறையின் போது ஏற்படும் தவறுகளை கையாளுகிறது மற்றும் பதிவிறக்கம் வெற்றிகரமாக இருந்ததா என்பதைப் பற்றிய கருத்தை வழங்குகிறது.

`requests` நூலகம் HTTP கோரிக்கைகளை செய்ய பயன்படுத்தப்படுகிறது, `PIL` நூலகம் படங்களைச் செயல்படுத்த பயன்படுத்தப்படுகிறது, மற்றும் `BytesIO` வகுப்பு படத் தரவுகளை பைட்களின் ஸ்ட்ரீமாக கையாள பயன்படுத்தப்படுகிறது.

### முடிவு

இந்த ஸ்கிரிப்ட், தேவையான படங்களை பதிவிறக்கி, பதிவிறக்க முடியாத வரிசைகளை வடிகட்டி, தரவுத்தொகுப்பை CSV கோப்பாக சேமித்து, இயந்திரக் கற்றலுக்கான தரவுத்தொகுப்பை தயாரிக்க ஒரு வசதியான வழியை வழங்குகிறது.

### மாதிரி ஸ்கிரிப்ட்

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


### மாதிரி கோப்பு பதிவிறக்கம்
[புதிய தரவுத்தொகுப்பு ஸ்கிரிப்டை உருவாக்கவும்](../../../../code/04.Finetuning/generate_dataset.py)

### மாதிரி தரவுத்தொகுப்பு
[LORA உதாரணத்துடன் finetuning-இன் மாதிரி தரவுத்தொகுப்பு](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.