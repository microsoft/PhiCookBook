# Generate Image Data Set sa pamamagitan ng pag-download ng DataSet mula sa Hugging Face at mga kaugnay na larawan


### Pangkalahatang-ideya

Inihahanda ng script na ito ang isang dataset para sa machine learning sa pamamagitan ng pag-download ng mga kinakailangang larawan, pagsasala ng mga hilera kung saan nabigo ang pag-download ng larawan, at pag-save ng dataset bilang isang CSV file.

### Mga Kinakailangan

Bago patakbuhin ang script na ito, siguraduhing naka-install ang mga sumusunod na library: `Pandas`, `Datasets`, `requests`, `PIL`, at `io`. Kailangan mo ring palitan ang `'Insert_Your_Dataset'` sa linya 2 ng pangalan ng iyong dataset mula sa Hugging Face.

Mga Kinakailangang Library:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Pag-andar

Isinasagawa ng script ang mga sumusunod na hakbang:

1. Dina-download ang dataset mula sa Hugging Face gamit ang `load_dataset()` function.
2. Kinokonvert ang Hugging Face dataset sa isang Pandas DataFrame para sa mas madaling pag-manipula gamit ang `to_pandas()` method.
3. Gumagawa ng mga direktoryo para i-save ang dataset at mga larawan.
4. Sinasala ang mga hilera kung saan nabigo ang pag-download ng larawan sa pamamagitan ng pag-ikot sa bawat hilera ng DataFrame, pagda-download ng larawan gamit ang custom na `download_image()` function, at pagdagdag ng na-salang hilera sa isang bagong DataFrame na tinatawag na `filtered_rows`.
5. Gumagawa ng bagong DataFrame gamit ang mga na-salang hilera at ini-save ito sa disk bilang isang CSV file.
6. Nagpi-print ng mensahe na nagsasaad kung saan na-save ang dataset at mga larawan.

### Custom na Function

Ang `download_image()` function ay nagda-download ng larawan mula sa isang URL at ini-save ito nang lokal gamit ang Pillow Image Library (PIL) at ang `io` module. Nagbabalik ito ng True kung matagumpay na na-download ang larawan, at False kung hindi. Nagbubunga rin ang function ng exception na may error message kapag nabigo ang request.

### Paano ito gumagana

Ang download_image function ay tumatanggap ng dalawang parameter: image_url, na siyang URL ng larawang ida-download, at save_path, na siyang path kung saan ise-save ang na-download na larawan.

Ganito ang takbo ng function:

Nagsisimula ito sa paggawa ng GET request sa image_url gamit ang requests.get method. Kinukuha nito ang data ng larawan mula sa URL.

Tinitiyak ng linya na response.raise_for_status() kung matagumpay ang request. Kung ang status code ng response ay nagpapakita ng error (halimbawa, 404 - Not Found), magbubunga ito ng exception. Pinipigilan nito na magpatuloy sa pag-download ng larawan kung hindi matagumpay ang request.

Ang data ng larawan ay ipinapasa sa Image.open method mula sa PIL (Python Imaging Library) module. Gumagawa ang method na ito ng Image object mula sa data ng larawan.

Ini-save ng image.save(save_path) ang larawan sa tinukoy na save_path. Dapat kasama sa save_path ang nais na pangalan ng file at extension.

Sa huli, nagbabalik ang function ng True bilang indikasyon na matagumpay na na-download at na-save ang larawan. Kung may anumang exception na mangyari sa proseso, hinuhuli nito ang exception, nagpi-print ng mensahe ng error na nagsasaad ng kabiguan, at nagbabalik ng False.

Kapaki-pakinabang ang function na ito para sa pag-download ng mga larawan mula sa mga URL at pag-save ng mga ito nang lokal. Hinahandle nito ang mga posibleng error sa proseso ng pag-download at nagbibigay ng feedback kung matagumpay o hindi ang pag-download.

Mahalagang tandaan na ginagamit ang requests library para gumawa ng HTTP requests, ang PIL library para magtrabaho sa mga larawan, at ang BytesIO class para hawakan ang data ng larawan bilang isang stream ng bytes.



### Konklusyon

Nagbibigay ang script na ito ng maginhawang paraan para ihanda ang isang dataset para sa machine learning sa pamamagitan ng pag-download ng mga kinakailangang larawan, pagsasala ng mga hilera kung saan nabigo ang pag-download ng larawan, at pag-save ng dataset bilang isang CSV file.

### Halimbawang Script

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

### Halimbawang Code Download 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Halimbawang Data Set
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.