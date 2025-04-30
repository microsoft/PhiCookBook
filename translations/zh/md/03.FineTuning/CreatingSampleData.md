<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44a77501fe39a2eb2b776dfdf9953b67",
  "translation_date": "2025-04-03T08:01:06+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "zh"
}
-->
# 通过从 Hugging Face 下载数据集和相关图片生成图像数据集

### 概述

此脚本通过下载所需图片、过滤下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

### 前提条件

在运行此脚本之前，请确保已安装以下库：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。此外，需将脚本第 2 行中的 `'Insert_Your_Dataset'` 替换为 Hugging Face 上数据集的名称。

所需库：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

此脚本执行以下步骤：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函数从 Hugging Face 下载数据集并处理成 Pandas 数据框。
2. `download_image()` 函数通过 Pillow 图像库 (PIL) 和 `io` 模块从 URL 下载图片并保存到本地。若图片成功下载，返回 True；否则返回 False。当请求失败时，该函数会抛出异常并返回错误信息。

### 工作原理

`download_image` 函数接收两个参数：`image_url`（图片下载的 URL）和 `save_path`（图片保存的路径）。

以下是该函数的工作流程：

1. 首先使用 `requests.get` 方法对 `image_url` 进行 GET 请求，从 URL 获取图片数据。
2. 使用 `response.raise_for_status()` 检查请求是否成功。如果响应状态码表明请求失败（例如 404 - 未找到），将抛出异常。这样可以确保只有在请求成功时才继续下载图片。
3. 然后将图片数据传递给 PIL 模块中的 `Image.open` 方法。此方法从图片数据中创建一个 Image 对象。
4. 使用 `image.save(save_path)` 将图片保存到指定的路径。`save_path` 应包含所需的文件名和扩展名。
5. 最后，函数返回 True，表示图片已成功下载并保存。如果过程中出现任何异常，函数会捕获异常，打印错误信息以指示失败，并返回 False。

此函数适用于从 URL 下载图片并保存到本地。它处理下载过程中的潜在错误，并反馈下载是否成功。

需要注意的是，`requests` 库用于发送 HTTP 请求，PIL 库用于处理图像，而 `BytesIO` 类用于将图像数据作为字节流进行处理。

### 结论

此脚本提供了一种方便的方法，通过下载所需图片、过滤下载失败的行并保存为 CSV 文件，为机器学习准备数据集。

### 示例脚本

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

### 示例代码下载 
[生成新数据集脚本](../../../../code/04.Finetuning/generate_dataset.py)

### 示例数据集
[使用 LORA 微调示例中的数据集样例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能会包含错误或不准确之处。应以原始语言的文件作为权威来源。对于重要信息，建议使用专业的人工翻译服务。我们对于因使用本翻译而导致的任何误解或误读不承担责任。