<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:45:56+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "tw"
}
-->
# 透過從 Hugging Face 下載資料集及相關圖片來生成影像資料集


### 概覽

此腳本透過下載所需圖片、過濾下載失敗的資料列，並將資料集儲存為 CSV 檔案，來準備機器學習用的資料集。

### 前置條件

執行此腳本前，請確保已安裝以下函式庫：`Pandas`、`Datasets`、`requests`、`PIL` 及 `io`。同時，請將第 2 行的 `'Insert_Your_Dataset'` 替換成你在 Hugging Face 上的資料集名稱。

所需函式庫：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能說明

此腳本執行以下步驟：

1. 使用 `load_dataset()` 函式從 Hugging Face 下載資料集。
2. 利用 `to_pandas()` 方法將 Hugging Face 資料集轉換成 Pandas DataFrame，方便操作。
3. 建立資料集及圖片的儲存目錄。
4. 透過遍歷 DataFrame 中的每一列，使用自訂的 `download_image()` 函式下載圖片，並過濾掉下載失敗的列，將成功的列加入新的 DataFrame `filtered_rows`。
5. 以過濾後的資料建立新的 DataFrame，並將其儲存為 CSV 檔案。
6. 印出訊息，告知資料集及圖片的儲存位置。

### 自訂函式

`download_image()` 函式會從 URL 下載圖片，並使用 Pillow Image Library (PIL) 及 `io` 模組將圖片儲存至本地。若圖片成功下載，回傳 True，否則回傳 False。當請求失敗時，函式會拋出包含錯誤訊息的例外。

### 運作原理

`download_image` 函式接受兩個參數：`image_url`（欲下載圖片的 URL）及 `save_path`（下載後圖片的儲存路徑）。

函式運作流程如下：

首先，使用 `requests.get` 方法對 `image_url` 發出 GET 請求，取得圖片資料。

`response.raise_for_status()` 會檢查請求是否成功。如果回應狀態碼顯示錯誤（例如 404 - 找不到資源），會拋出例外。這確保只有在請求成功時才繼續下載圖片。

接著，將圖片資料傳入 PIL 模組的 `Image.open` 方法，建立 Image 物件。

`image.save(save_path)` 會將圖片儲存到指定的 `save_path`，該路徑需包含檔名及副檔名。

最後，函式回傳 True，表示圖片成功下載並儲存。若過程中發生任何例外，會捕捉例外並印出錯誤訊息，然後回傳 False。

此函式適合用來從 URL 下載圖片並儲存至本地，能處理下載過程中的潛在錯誤，並回饋下載是否成功。

值得一提的是，`requests` 函式庫用於發送 HTTP 請求，`PIL` 用於處理圖片，而 `BytesIO` 類別則用來將圖片資料當作位元組串流處理。



### 結論

此腳本提供一個方便的方式，透過下載所需圖片、過濾下載失敗的資料列，並將資料集儲存為 CSV 檔案，來準備機器學習用的資料集。

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

### 範例程式碼下載
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### 範例資料集
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。