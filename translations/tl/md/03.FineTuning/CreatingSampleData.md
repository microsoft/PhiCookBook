<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:26:08+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "tl"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Overview

Inihahanda ng script na ito ang isang dataset para sa machine learning sa pamamagitan ng pag-download ng mga kinakailangang larawan, pagtanggal ng mga hilera kung saan nabigo ang pag-download ng larawan, at pag-save ng dataset bilang isang CSV file.

### Prerequisites

Bago patakbuhin ang script na ito, siguraduhing naka-install ang mga sumusunod na library: `Pandas`, `Datasets`, `requests`, `PIL`, at `io`. Kailangan mo ring palitan ang `'Insert_Your_Dataset'` sa linya 2 ng pangalan ng iyong dataset mula sa Hugging Face.

Required Libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Functionality

Isinasagawa ng script ang mga sumusunod na hakbang:

1. Dina-download ang dataset mula sa Hugging Face gamit ang `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` function na nagda-download ng larawan mula sa isang URL at sine-save ito nang lokal gamit ang Pillow Image Library (PIL) at ang `io` module. Nagbabalik ito ng True kung matagumpay ang pag-download ng larawan, at False kung hindi. Nagbubunga rin ang function ng exception na may error message kapag nabigo ang request.

### How does this work

Ang download_image function ay tumatanggap ng dalawang parameter: image_url, na URL ng larawang ida-download, at save_path, na ang path kung saan ise-save ang na-download na larawan.

Ganito gumagana ang function:

Nagsisimula ito sa paggawa ng GET request sa image_url gamit ang requests.get method. Nakukuha nito ang data ng larawan mula sa URL.

Sinusuri ng response.raise_for_status() kung matagumpay ang request. Kung may error ang status code ng response (hal. 404 - Not Found), magtataas ito ng exception. Tinitiyak nito na magpapatuloy lang tayo sa pag-download kung matagumpay ang request.

Pinapasa ang image data sa Image.open method mula sa PIL (Python Imaging Library) module. Lumilikha ito ng Image object mula sa image data.

Ise-save ng image.save(save_path) ang larawan sa tinukoy na save_path. Dapat kasama sa save_path ang nais na pangalan ng file at extension.

Sa huli, nagbabalik ang function ng True bilang tanda na matagumpay na na-download at na-save ang larawan. Kung may exception na mangyari habang proseso, huliin nito ang exception, ipi-print ang error message na nagsasaad ng pagkabigo, at magbabalik ng False.

Kapaki-pakinabang ang function na ito para mag-download ng mga larawan mula sa mga URL at i-save ang mga ito nang lokal. Hinahandle nito ang mga posibleng error sa proseso ng pag-download at nagbibigay ng feedback kung matagumpay ba ang pag-download o hindi.

Mahalagang tandaan na ginagamit ang requests library para sa HTTP requests, ang PIL library para sa pagproseso ng mga larawan, at ang BytesIO class para hawakan ang image data bilang stream ng bytes.


### Conclusion

Nagbibigay ang script na ito ng madaling paraan para ihanda ang dataset para sa machine learning sa pamamagitan ng pag-download ng kinakailangang mga larawan, pagtanggal ng mga hilera kung saan nabigo ang pag-download ng larawan, at pag-save ng dataset bilang CSV file.

### Sample Script

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

### Sample Code Download 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Sample Data Set
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami na maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.