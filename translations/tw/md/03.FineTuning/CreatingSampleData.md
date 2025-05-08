<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-08T05:14:03+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "tw"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Overview

這個腳本透過下載所需的圖片，過濾掉下載失敗的列，並將資料集存成 CSV 檔，來準備機器學習用的資料集。

### Prerequisites

執行此腳本前，請確認已安裝以下函式庫：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。你也需要將第 2 行的 `'Insert_Your_Dataset'` 替換成你從 Hugging Face 下載的資料集名稱。

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

腳本會執行以下步驟：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函式從 Hugging Face 下載資料集。`download_image()` 函式會從 URL 下載圖片並使用 Pillow Image Library (PIL) 及 `io` 模組將圖片儲存在本地。若圖片成功下載，會回傳 True，否則回傳 False。當請求失敗時，該函式也會丟出帶有錯誤訊息的例外。

### How does this work

download_image 函式接受兩個參數：image_url 是要下載的圖片 URL，save_path 是下載後圖片要儲存的路徑。

函式運作方式如下：

首先使用 requests.get 方法對 image_url 發出 GET 請求，取得圖片資料。

response.raise_for_status() 這行會檢查請求是否成功。如果回應狀態碼顯示錯誤（例如 404 - 找不到），就會丟出例外。這確保只有在請求成功時才會繼續下載圖片。

接著將圖片資料傳給 PIL (Python Imaging Library) 模組的 Image.open 方法，建立 Image 物件。

image.save(save_path) 會把圖片存到指定的 save_path，該路徑應包含檔名及副檔名。

最後，函式會回傳 True，表示圖片成功下載並儲存。若過程中發生任何例外，會捕捉例外並印出錯誤訊息，然後回傳 False。

這個函式適合用來從 URL 下載圖片並儲存到本地，能處理下載過程中可能發生的錯誤，並回饋下載是否成功。

值得一提的是，requests 函式庫用來發出 HTTP 請求，PIL 函式庫用來處理圖片，而 BytesIO 類別則用來將圖片資料當作位元組串流處理。



### Conclusion

這個腳本提供一個方便的方式，透過下載所需圖片、過濾下載失敗的列，並將資料集存成 CSV，來準備機器學習用的資料集。

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

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。