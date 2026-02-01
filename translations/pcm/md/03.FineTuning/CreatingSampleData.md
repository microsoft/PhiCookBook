# Make Image Data Set by downloading DataSet from Hugging Face and di images wey join am


### Overview

Dis script dey prepare dataset for machine learning by downloading di images wey e need, dey filter out rows wey image downloads fail, and dey save di dataset as CSV file.

### Prerequisites

Before you run dis script, make sure say you don install dis libraries: `Pandas`, `Datasets`, `requests`, `PIL`, and `io`. You go also need change `'Insert_Your_Dataset'` for line 2 to di name of your dataset from Hugging Face.

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

Di script dey do di following steps:

1. Download di dataset from Hugging Face using the `load_dataset()` function.
2. Convert di Hugging Face dataset to a Pandas DataFrame to make manipulation easier using the `to_pandas()` method.
3. Create directories to save di dataset and images.
4. Filter out rows wey image download fail by iterating through each row for di DataFrame, downloading the image using di custom `download_image()` function, and appending di filtered row to a new DataFrame wey dem call `filtered_rows`.
5. Make a new DataFrame with di filtered rows and save am to disk as a CSV file.
6. Print message wey dey indicate where dem don save di dataset and images.

### Custom Function

Di `download_image()` function dey download image from URL and save am locally using Pillow Image Library (PIL) and di `io` module. E return True if di image don download successfully, and False if e no. Di function fit also raise exception with error message when di request fail.

### How does this work

Di download_image function get two parameters: image_url, wey be di URL of di image wey you wan download, and save_path, wey be di path wey di downloaded image go save.

Na so di function dey work:

E start by making GET request to di image_url using di requests.get method. Dis one dey retrieve di image data from di URL.

Di response.raise_for_status() line dey check if di request successful. If di response status code show error (e.g., 404 - Not Found), e go raise exception. Dis one make sure say we go only continue to download di image if di request successful.

Di image data go then pass to di Image.open method from di PIL (Python Imaging Library) module. Dis method dey create Image object from di image data.

Di image.save(save_path) line go save di image to di specified save_path. Di save_path suppose include di desired file name and extension.

Finally, di function go return True to show say di image don successfully download and save. If any exception happen during di process, e go catch di exception, print error message wey indicate di failure, and return False.

Dis function good for downloading images from URLs and saving dem locally. E dey handle possible errors during di download process and dey give feedback on whether di download succeed or no.

Make you note say di requests library dey make HTTP requests, di PIL library dey work with images, and di BytesIO class dey handle di image data as stream of bytes.



### Conclusion

Dis script give convenient way to prepare dataset for machine learning by downloading di images wey e need, filtering out rows wey image downloads fail, and saving di dataset as a CSV file.

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
        response.raise_for_status()  # Check if di request don succeed
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download di dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert di Hugging Face dataset go Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save di dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows wey image download fail
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Make a new DataFrame with di filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save di updated dataset go disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### Sample Code Download 
[Script wey go generate new Data Set](../../../../code/04.Finetuning/generate_dataset.py)

### Sample Data Set
[Sample Data Set example wey come from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate use AI translation service wey dem dey call Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say machine translation fit get mistakes or no too correct. Make you consider the original document for im original language as di main authoritative source. If na important information, make you use professional human translation. We no go responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->