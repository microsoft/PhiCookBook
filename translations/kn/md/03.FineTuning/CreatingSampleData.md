<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-12-21T18:01:15+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "kn"
}
-->
# Hugging Face ನಿಂದ ಡೇಟಾಸೆಟ್ ಮತ್ತು ಸಂಬಂಧಿತ ಚಿತ್ರಗಳನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ ಚಿತ್ರ ಡೇಟಾ ಸೆಟ್ ರಚನೆ


### ಅವಲೋಕನ

ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಅಗತ್ಯವಿರುವ ಚಿತ್ರಗಳನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡುವ ಮೂಲಕ, ಚಿತ್ರ ಡೌನ್ಲೋಡ್ ವಿಫಲವಾಗುವ ಸಾಲುಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡುವುದು ಮತ್ತು ಡೇಟಾಸೆಟ್ ಅನ್ನು CSV ಫೈಲ್ ಆಗಿ ಉಳಿಸುವ ಮೂಲಕ ಮೆಷಿನ್ ಲರ್ನಿಂಗ್‌ಗೆ ಡೇಟಾಸೆಟ್ ಅನ್ನು ತಯಾರಿಸುತ್ತದೆ.

### ಅಗತ್ಯವಿರುವ ವಸ್ತುಗಳು

ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಚಲಾಯಿಸುವ ಮೊದಲು ಕೆಳಕಂಡ ಗ್ರಂಥಾಲಯಗಳು ಸ್ಥಾಪನೆಗೊಂಡಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಂಡಿರಲಿ: `Pandas`, `Datasets`, `requests`, `PIL`, ಮತ್ತು `io`. ನೀವು Hugging Face ನಿಂದ ನಿಮ್ಮ ಡೇಟಾಸೆಟ್‌ನ ಹೆಸರನ್ನು ಕೊಡಲು 2ನೇ ಸಾಲಿನಲ್ಲಿ `'Insert_Your_Dataset'` ಅನ್ನು ಬದಲಾಯಿಸಬೇಕಾಗುತ್ತದೆ.

Required Libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### ಕಾರ್ಯಕ್ಷಮತೆ

ಸ್ಕ್ರಿಪ್ಟ್ ಕೆಳಕಂಡ ಹಂತಗಳನ್ನು ನೆರವೇರಿಸುತ್ತದೆ:

1. `load_dataset()` ಫังก್ಷನ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು Hugging Face ನಿಂದ ಡೇಟಾಸೆಟ್ ಅನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡುತ್ತದೆ.
2. ಸುಲಭ ನಿರ್ವಹಣೆಗೆ Hugging Face ಡೇಟಾಸೆಟ್ ಅನ್ನು `to_pandas()` ವಿಧಾನವನ್ನು ಬಳಸಿಕೊಂಡು Pandas DataFrame ಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.
3. ಡೇಟಾಸೆಟ್ ಮತ್ತು ಚಿತ್ರಗಳನ್ನು ಉಳಿಸಲು ಡೈರೆಕ್ಟರಿಗಳನ್ನು ರಚಿಸುತ್ತದೆ.
4. DataFrame ನ ಪ್ರತಿಯೊಂದು ಸಾಲಿನ ಮೂಲಕ ಓಡುತ್ತಿದ್ದಂತೆ ಚಿತ್ರ ಡೌನ್ಲೋಡ್ ವಿಫಲವಾಗುವ ಸಾಲುಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡುತ್ತದೆ: ಕಸ್ಟಮ್ `download_image()` ಫಂಕ್ಷನ್ ಅನ್ನು ಬಳಸಿ ಚಿತ್ರವನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ, ಫಿಲ್ಟರ್ ಮಾಡಿದ ಸಾಲನ್ನು `filtered_rows` ಎನ್ನುವ ಹೊಸ DataFrame ಗೆ ಸೇರಿಸುತ್ತದೆ.
5. ಫಿಲ್ಟರ್ ಮಾಡಿದ ಸಾಲುಗಳೊಂದಿಗೆ ಹೊಸ DataFrame ಅನ್ನು ರಚಿಸಿ ಅದನ್ನು ಡಿಸ್ಕ್‌ಗೆ CSV ಫೈಲ್ ಆಗಿ ಉಳಿಸುತ್ತದೆ.
6. ಡೇಟಾಸೆಟ್ ಮತ್ತು ಚಿತ್ರಗಳು ಎಲ್ಲಿ ಉಳಿಸಲಾಗಿದೆ ಎಂಬ ಸುದ್ದಿಯನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

### ಕಸ್ಟಮ್ ಫಂಕ್ಷನ್

`download_image()` ಫಂಕ್ಷನ್ ಒಂದು URL ನಿಂದ ಚಿತ್ರವನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ Pillow Image Library (PIL) ಮತ್ತು `io` ಮòd್ಯೂಲ್ ಬಳಸಿ ಸ್ಥಳೀಯವಾಗಿ ಉಳಿಸುತ್ತದೆ. ಚಿತ್ರ ಯಶಸ್ವಿಯಾಗಿ ಡೌನ್ಲೋಡ್ ಆದರೆ ಅದು True ಅನ್ನು ಮರಳಿ ನೀಡುತ್ತದೆ, ಇಲ್ಲದಿದ್ದಲ್ಲಿ False ಅನ್ನು ನೀಡುತ್ತದೆ. ವಿನಂತಿ ವಿಫಲವಾದಲ್ಲಿ ಇದು ತಪ್ಪು ಸಂದೇಶದೊಂದಿಗೆ исключೆಪ್‌ಶನ್ ಅನ್ನು ಉದ್ದೀಪಿಸುತ್ತವೆ.

### ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ

download_image ಫಂಕ್ಷನ್ ಎರಡು ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ: image_url, ಅದು ಡೌನ್ಲೋಡ್ ಮಾಡಲು ಇರುವ ಚಿತ್ರದ URL ಆಗಿದ್ದು, ಮತ್ತು save_path, ಅದು ಡೌನ್ಲೋಡ್ ಮಾಡಲಾದ ಚಿತ್ರ ಉಳಿಯಲಿರುವ ಪಥವಾಗಿದೆ.

ಇದನ್ನು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂದರೆ:

ಶುರುವಾಗಿಸುವಾಗ requests.get ವಿಧಾನವನ್ನು ಬಳಸಿಕೊಂಡು image_url ಗೆ GET ವಿನಂತಿ ಮಾಡುತ್ತದೆ. ಇದು URL ನಿಂದ ಚಿತ್ರ ಡೇಟಾವನ್ನು ಪಡೆಯುತ್ತದೆ.

response.raise_for_status() ಸಾಲು ವಿನಂತಿ ಯಶಸ್ವಿ ಆಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಉತ್ತರದ ಸ್ಥಿತಿ ಕೋಡ್ ದೋಷವನ್ನ ಸೂಚಿಸಿದರೆ (ಉದಾಹರಣೆಗಾಗಿ 404 - Not Found), ಅದು исключೆಪ್‌ಶನ್ ಎಸ್ಕ್ರೋ ಆಗುತ್ತದೆ. ಇದು ನಾವು ಚಿತ್ರವನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡುವಾಗ ಮಾತ್ರ ಮುಂದುವರಿಯುವುದನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ.

ಚಿತ್ರ ಡೇಟಾವನ್ನು ನಂತರ PIL ನ Image.open ವಿಧಾನಕ್ಕೆ ಪಾಸ್ ಮಾಡಲಾಗುತ್ತದೆ. ಇದು ಚಿತ್ರ ಡೇಟಾದಿಂದ Image ವಸ್ತುವನ್ನು ರಚಿಸುತ್ತದೆ.

image.save(save_path) ಸಾಲು ಸೂಚಿಸಿದ save_path ಗೆ ಚಿತ್ರವನ್ನು ಉಳಿಸುತ್ತದೆ. save_path ನಲ್ಲಿ ಹಾಜರಿನ ಫೈಲ್ ಹೆಸರು ಮತ್ತು ವಿಸ್ತರಣೆ ಸೇರಿರಬೇಕು.

ಅಂತಿಮವಾಗಿ, ಫಂಕ್ಷನ್ ಚಿತ್ರ ಯಶಸ್ವಿಯಾಗಿ ಡೌನ್ಲೋಡ್ ಆಗಿ ಉಳಿಸಲ್ಪಟ್ಟುದನ್ನು ಸೂಚಿಸಲು True ಅನ್ನು ಮರಳಿ ನೀಡುತ್ತದೆ. ಪ್ರಕ್ರಿಯೆಯ ವೇಳೆ ಯಾವುದೇ исключೆಪ್‌ಶನ್ ಸಂಭವಿಸಿದರೆ, ಅದು исключೆಪ್‌ಶನ್ ಅನ್ನು ಹಿಡಿದಿಟ್ಟುಕೊಂಡು ವೈಫಲ್ಯವನ್ನು ಸೂಚಿಸುವ ದೋಷ ಸಂದೇಶವನ್ನು ಮುದ್ರಿಸಿ False ಅನ್ನು ಮರಳಿ ನೀಡುತ್ತದೆ.

ಈ ಫಂಕ್ಷನ್ URL ಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ ಸ್ಥಳೀಯವಾಗಿ ಉಳಿಸಲು ಉಪಯುಕ್ತವಾಗಿದೆ. ಇದು ಡೌನ್ಲೋಡ್ ಪ್ರಕ್ರಿಯೆಯ ಸಮಯದಲ್ಲಿ ಸಂಭವಿಸಬಹುದಾದ ದೋಷಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಡೌನ್ಲೋಡ್ ಯಶಸ್ವಿಯಾಗಿದೆ ಅಥವಾ ಇಲ್ಲವೆ ಎಂದರೇನು ಎಂಬ ಬಗ್ಗೆ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುತ್ತದೆ.

ಗಮನಿಸಲು ತಕ್ಕದ್ದು: requests ಗ್ರಂಥಾಲಯ HTTP ವಿನಂತಿಗಳನ್ನು ಮಾಡಲು ಬಳಸಲ್ಪಡುತ್ತದೆ, PIL ಗ್ರಂಥಾಲಯ ಚಿತ್ರಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು ಬಳಸಲ್ಪಡುತ್ತದೆ, ಮತ್ತು BytesIO ಕ್ಲಾಸ್ ಚಿತ್ರ ಡೇಟಾನ್ನು ಬೈಟ್‌ಗಳ ಸ್ಟ್ರೀಮ್ ಆಗಿ ನಿರ್ವಹಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.



### ನಿಷ್ಕರ್ಷ

ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಅಗತ್ಯವಿರುವ ಚಿತ್ರಗಳನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡುವ ಮೂಲಕ, ಚಿತ್ರ ಡೌನ್ಲೋಡ್ ವಿಫಲವಾಗುವ ಸಾಲುಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡುವ ಮೂಲಕ, ಮತ್ತು ಡೇಟಾಸೆಟ್ ಅನ್ನು CSV ಫೈಲ್ ಆಗಿ ಉಳಿಸುವ ಮೂಲಕ ಮೆಷಿನ್ ಲರ್ನಿಂಗ್‌ಗೆ ಡೇಟಾಸೆಟ್ ತಯಾರಿಸಲು ಅನುಕೂಲಕರ ಮಾರ್ಗವನ್ನು ಒದಗಿಸುತ್ತದೆ.

### ಉದಾಹರಣೆ ಸ್ಕ್ರಿಪ್ಟ್

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
        response.raise_for_status()  # ಬೇಡಿಕೆ ಯಶಸ್ವಿಯಾಗಿದೆಯೆಂದು ಪರಿಶೀಲಿಸಿ
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Hugging Face‌ನಿಂದ ಡೇಟಾಸೆಟ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
dataset = load_dataset('Insert_Your_Dataset')


# Hugging Face ಡೇಟಾಸೆಟ್ ಅನ್ನು Pandas DataFrameಗೆ ಪರಿವರ್ತಿಸಿ
df = dataset['train'].to_pandas()


# ಡೇಟಾಸೆಟ್ ಮತ್ತು ಚಿತ್ರಗಳನ್ನು ಉಳಿಸಲು ಡೈರೆಕ್ಟರಿಗಳನ್ನು ರಚಿಸಿ
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# ಚಿತ್ರ ಡೌನ್‌ಲೋಡ್ ವಿಫಲವಾಗುವ ಸಾಲುಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಿ
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# ಫಿಲ್ಟರ್ ಮಾಡಿದ ಸಾಲುಗಳೊಂದಿಗೆ ಹೊಸ DataFrame ರಚಿಸಿ
filtered_df = pd.DataFrame(filtered_rows)


# ಅಪ್‌ಡೇಟ್ ಮಾಡಿದ ಡೇಟಾಸೆಟ್ ಅನ್ನು ಡಿಸ್ಕ್‌ಗೆ ಉಳಿಸಿ
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### ಉದಾಹರಣಾ ಕೇಡ್ ಡೌನ್‌ಲೋಡ್ 
[ಹೊಸ ಡೇಟಾ ಸೆಟ್ ಸ್ಕ್ರಿಪ್ಟ್ ರಚನೆ](../../../../code/04.Finetuning/generate_dataset.py)

### ಉದಾಹರಣಾ ಡೇಟಾ ಸೆಟ್
[LORA ಫೈನ್‌ಟ್ಯೂನಿಂಗ್‌ನಿಂದ ಉದಾಹರಣಾ ಡೇಟಾ ಸೆಟ್](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮರ್ಪಕತೆಗಳು ಇರಬಹೆಯೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕಾರಪ್ರಧಾನ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ಅಭಿಪ್ರಾಯ ಭಿನ್ನತೆಯ ಕುರಿತು ನಾವು ಜವಾಬ್ದಾರಿಗಳಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->