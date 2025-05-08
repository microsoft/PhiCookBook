<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-08T05:13:46+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hk"
}
-->
# 透過由 Hugging Face 下載 DataSet 及相關圖片來生成圖像數據集

### 概覽

呢個 script 係準備機器學習用嘅數據集，方法係下載所需嘅圖片，篩選出下載圖片失敗嘅行，然後將數據集保存成 CSV 文件。

### 先決條件

喺執行呢個 script 前，請確保已安裝以下庫：`Pandas`、`Datasets`、`requests`、`PIL` 同 `io`。你仲需要喺第 2 行將 `'Insert_Your_Dataset'` 換成你喺 Hugging Face 嘅數據集名稱。

所需庫：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能說明

呢個 script 會做以下步驟：

1. 用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函數由 Hugging Face 下載數據集。`download_image()` 函數會從 URL 下載圖片並用 Pillow Image Library (PIL) 同 `io` 模組將圖片儲存到本地。如果圖片成功下載會回傳 True，失敗就回傳 False。當請求失敗時，函數會拋出帶有錯誤訊息嘅異常。

### 運作原理

download_image 函數有兩個參數：image_url，代表要下載嘅圖片 URL；save_path，代表下載後圖片嘅儲存路徑。

函數嘅運作方式如下：

首先用 requests.get 方法對 image_url 發出 GET 請求，從 URL 取得圖片數據。

response.raise_for_status() 會檢查請求是否成功。如果狀態碼顯示有錯誤（例如 404 - 找唔到），就會拋出異常。咁樣確保只有請求成功先會繼續下載圖片。

圖片數據會傳畀 PIL（Python Imaging Library）嘅 Image.open 方法，將數據轉成 Image 物件。

image.save(save_path) 會將圖片儲存到指定嘅 save_path，路徑應該包括檔案名同副檔名。

最後函數會回傳 True 表示圖片成功下載同儲存。如果過程中有任何異常，會捕捉異常，打印錯誤訊息提示失敗，並回傳 False。

呢個函數方便用嚟從 URL 下載圖片並儲存本地，處理下載過程中可能出現嘅錯誤，並提供下載成功與否嘅反饋。

值得留意嘅係，requests 庫用嚟發 HTTP 請求，PIL 庫用嚟處理圖片，而 BytesIO 類用嚟將圖片數據當作位元組流處理。

### 總結

呢個 script 提供咗一個方便嘅方法，幫助準備機器學習用嘅數據集，透過下載所需圖片、篩選下載失敗嘅行，最後將數據集保存成 CSV 文件。

### 範例 Script

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

### 範例代碼下載  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### 範例數據集  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。因使用此翻譯而引致嘅任何誤解或誤釋，我哋概不負責。