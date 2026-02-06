# హగ్గింగ్ ఫేస్ నుండి డేటాసెట్ మరియు సంబంధిత చిత్రాలను డౌన్లోడ్ చేసి ఇమేజ్ డేటా సెట్ను రూపొందించడం

### అవలోకనం

ఈ స్క్రిప్ట్ అవసరమైన చిత్రాలను డౌన్లోడ్ చేసి, చిత్రాల డౌన్లోడ్ విఫలమైన వరుసలను ఫిల్టర్ చేసి, డేటాసెట్‌ను CSV ఫైల్‌గా సేవ్ చేయడం ద్వారా మెషీన్ లర్నింగ్ కోసం డేటాసెట్‌ను సిద్ధం చేస్తుంది.

### అవశ్యకతలు

ఈ స్క్రిప్ట్ నడిపేముందు క్రింది లైబ్రరీలను ఇన్‌స్టాల్ చేసినట్లు నిర్ధారించుకోండి: `Pandas`, `Datasets`, `requests`, `PIL`, మరియు `io`. మీరు Hugging Face నుండి మీ డేటాసెట్ పేరు తో లైన్ 2 లోని `'Insert_Your_Dataset'` ను కూడా మార్చాల్సి ఉంటుంది.

Required Libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### ఫంక్షనాలిటీ

ఈ స్క్రిప్ట్ క్రింది దశలను నిర్వహిస్తుంది:

1. Downloads the dataset from Hugging Face using the `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### కస్టమ్ ఫంక్షన్

The `download_image()` function downloads an image from a URL and saves it locally using the Pillow Image Library (PIL) and the `io` module. It returns True if the image is successfully downloaded, and False otherwise. The function also raises an exception with the error message when the request fails.

### ఇది ఎలా పనిచేస్తుంది

The download_image function takes two parameters: image_url, which is the URL of the image to be downloaded, and save_path, which is the path where the downloaded image will be saved.

Here's how the function works:

It starts by making a GET request to the image_url using the requests.get method. This retrieves the image data from the URL.

The response.raise_for_status() line checks if the request was successful. If the response status code indicates an error (e.g., 404 - Not Found), it will raise an exception. This ensures that we only proceed with downloading the image if the request was successful.

The image data is then passed to the Image.open method from the PIL (Python Imaging Library) module. This method creates an Image object from the image data.

The image.save(save_path) line saves the image to the specified save_path. The save_path should include the desired file name and extension.

Finally, the function returns True to indicate that the image was successfully downloaded and saved. If any exception occurs during the process, it catches the exception, prints an error message indicating the failure, and returns False.

This function is useful for downloading images from URLs and saving them locally. It handles potential errors during the download process and provides feedback on whether the download was successful or not.

It's worth noting that the requests library is used to make HTTP requests, the PIL library is used to work with images, and the BytesIO class is used to handle the image data as a stream of bytes.



### ముగింపు

ఈ స్క్రిప్ట్ అవసరమైన చిత్రాలను డౌన్లోడ్ చేయడం ద్వారా, చిత్రాల డౌన్లోడ్ విఫలమైన వరుసలను ఫిల్టర్ చేయడం ద్వారా మరియు డేటాసెట్‌ను CSV ఫైల్‌గా సేవ్ చేయడం ద్వారా మెషీన్ లర్నింగ్ కోసం డేటాసెట్‌ను తయారుచేయడానికి సౌకర్యవంతమైన మార్గం అందిస్తుంది.

### నమూనా స్క్రిప్ట్

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
        response.raise_for_status()  # అనురోధం విజయవంతమైనదో లేదో తనిఖీ చేయండి
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Hugging Face నుండి డేటాసెట్‌ను డౌన్‌లోడ్ చేయండి
dataset = load_dataset('Insert_Your_Dataset')


# Hugging Face డేటాసెట్‌ను Pandas DataFrame గా మార్చండి
df = dataset['train'].to_pandas()


# డేటాసెట్ మరియు చిత్రాలను సేవ్ చేయడానికి డైరెక్టరీలను సృష్టించండి
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# చిత్రం డౌన్‌లోడ్ విఫలమయ్యే వరుసలను ఫిల్టర్ చేయండి
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# ఫిల్టర్ చేసిన వరుసలతో ఒక కొత్త DataFrame సృష్టించండి
filtered_df = pd.DataFrame(filtered_rows)


# నవీకరించిన డేటాసెట్‌ను డిస్క్‌కు సేవ్ చేయండి
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### నమూనా కోడ్ డౌన్‌లోడ్ 
[కొత్త డేటా సెట్ స్క్రిప్ట్ ఉత్పత్తి చేయండి](../../../../code/04.Finetuning/generate_dataset.py)

### నమూనా డేటా సెట్
[LORA తో ఫైన్‌ట్యూనింగ్ నుండి నమూనా డేటా సెట్ ఉదాహరణ](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తామని చెప్పినప్పటికీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా అకర్మతలు ఉండవచ్చు. అసలైన పత్రాన్ని దాని మూల భాషలోని సంస్కరణను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం ప్రొఫెషనల్ మానవ అనువాదాన్ని సూచించబడుతుంది. ఈ అనువాదం ఉపయోగించడంతో సంభవించే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాల కోసం మేము బాధ్యులం కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->