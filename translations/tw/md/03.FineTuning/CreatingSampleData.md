<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44a77501fe39a2eb2b776dfdf9953b67",
  "translation_date": "2025-04-04T06:55:43+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "tw"
}
-->
# 從 Hugging Face 下載資料集並生成影像數據集

### 概述

這段腳本用於準備機器學習所需的數據集，通過下載所需的影像，過濾掉下載失敗的行，並將數據集保存為 CSV 文件。

### 前置條件

在運行此腳本之前，請確保已安裝以下庫：`Pandas`, `Datasets`, `requests`, `PIL` 和 `io`。此外，需將第 2 行中的 `'Insert_Your_Dataset'` 替換為你從 Hugging Face 獲取的數據集名稱。

所需庫：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

腳本執行以下步驟：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函數從 Hugging Face 下載數據集並轉換為 pandas 格式，下載影像，並過濾掉下載失敗的行。
2. `download_image()` 函數使用 Pillow 影像庫 (PIL) 和 `io` 模塊，從 URL 下載影像並保存到本地。如果影像成功下載，返回 True；否則返回 False。如果請求失敗，該函數會拋出異常並返回錯誤信息。

### 運作方式

`download_image` 函數接收兩個參數：`image_url`（影像的 URL）和 `save_path`（保存影像的路徑）。

以下是該函數的運作方式：

- 首先使用 `requests.get` 方法向 `image_url` 發送 GET 請求，從 URL 獲取影像數據。
- `response.raise_for_status()` 用於檢查請求是否成功。如果返回的狀態碼表示錯誤（例如 404 - 未找到），則拋出異常。這確保只有在請求成功時才繼續下載影像。
- 影像數據通過 PIL 模塊中的 `Image.open` 方法處理，生成影像對象。
- 使用 `image.save(save_path)` 將影像保存到指定的 `save_path`，其中 `save_path` 包含所需的文件名和擴展名。
- 最後，函數返回 True，表示影像成功下載並保存。如果過程中發生異常，函數會捕獲異常，打印錯誤信息並返回 False。

此函數適用於從 URL 下載影像並保存到本地。它處理下載過程中的潛在錯誤，並提供下載是否成功的反饋。

需要注意的是，`requests` 庫用於發送 HTTP 請求，PIL 庫用於處理影像，而 `BytesIO` 類用於以字節流的形式處理影像數據。

### 結論

此腳本提供了一種方便的方法，用於準備機器學習數據集，通過下載所需影像、過濾掉下載失敗的行，並將數據集保存為 CSV 文件。

### 範例腳本

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

### 下載範例代碼 
[生成新數據集腳本](../../../../code/04.Finetuning/generate_dataset.py)

### 範例數據集
[使用 LORA 微調的範例數據集](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的原文應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤讀承擔責任。