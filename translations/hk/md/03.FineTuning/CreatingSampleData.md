<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44a77501fe39a2eb2b776dfdf9953b67",
  "translation_date": "2025-04-04T18:47:38+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "hk"
}
-->
# 下載 Hugging Face 數據集並生成圖片數據集

### 概述

這個腳本透過下載所需的圖片、過濾掉下載失敗的行，並將數據集保存為 CSV 文件，為機器學習準備數據集。

### 前置條件

在運行此腳本之前，請確保已安裝以下庫：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。此外，需將第 2 行的 `'Insert_Your_Dataset'` 替換為你在 Hugging Face 上的數據集名稱。

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

此腳本執行以下步驟：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函數從 Hugging Face 下載數據集。`download_image()` 函數透過 Pillow 圖片庫 (PIL) 和 `io` 模塊，從 URL 下載圖片並保存到本地。如果圖片成功下載，返回 True，否則返回 False。如果請求失敗，該函數會拋出異常並提供錯誤信息。

### 如何運作

`download_image` 函數有兩個參數：`image_url` 是要下載的圖片 URL，`save_path` 是下載後保存圖片的路徑。

以下是該函數的運作方式：

- 首先，使用 `requests.get` 方法向 `image_url` 發送 GET 請求以獲取圖片數據。

- 使用 `response.raise_for_status()` 檢查請求是否成功。如果狀態碼顯示錯誤（例如 404 - 未找到），則拋出異常。這確保只有在請求成功時才進行圖片下載。

- 圖片數據接著通過 PIL 模塊的 `Image.open` 方法處理，該方法從數據中創建圖片對象。

- 使用 `image.save(save_path)` 將圖片保存到指定的路徑，路徑應包含所需的文件名和擴展名。

- 最後，該函數返回 True，表示圖片已成功下載並保存。如果過程中發生任何異常，則捕獲異常，打印失敗信息並返回 False。

這個函數適合從 URL 下載圖片並保存到本地。它處理下載過程中的潛在錯誤，並提供是否成功下載的反饋。

值得注意的是，`requests` 庫用於發送 HTTP 請求，PIL 庫用於處理圖片，而 `BytesIO` 類則用於以字節流形式處理圖片數據。

### 結論

這個腳本提供了一種便捷的方法，透過下載所需圖片、過濾掉下載失敗的行，並將數據集保存為 CSV 文件，為機器學習準備數據集。

### 示例腳本

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

### 示例代碼下載 
[生成新數據集腳本](../../../../code/04.Finetuning/generate_dataset.py)

### 示例數據集
[使用 LORA 微調的示例數據集](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議尋求專業的人類翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。