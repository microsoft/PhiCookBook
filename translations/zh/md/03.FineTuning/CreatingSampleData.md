<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:45:24+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "zh"
}
-->
# 通过从 Hugging Face 下载数据集及相关图片生成图像数据集


### 概述

该脚本通过下载所需图片，过滤掉下载失败的行，并将数据集保存为 CSV 文件，从而准备机器学习所需的数据集。

### 前提条件

运行此脚本前，请确保已安装以下库：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。你还需要将第 2 行的 `'Insert_Your_Dataset'` 替换为你在 Hugging Face 上的数据集名称。

所需库：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能说明

脚本执行以下步骤：

1. 使用 `load_dataset()` 函数从 Hugging Face 下载数据集。
2. 使用 `to_pandas()` 方法将 Hugging Face 数据集转换为 Pandas DataFrame，便于操作。
3. 创建目录以保存数据集和图片。
4. 遍历 DataFrame 中的每一行，使用自定义的 `download_image()` 函数下载图片，过滤掉下载失败的行，并将成功的行添加到新的 DataFrame `filtered_rows` 中。
5. 使用过滤后的行创建新的 DataFrame，并将其保存为 CSV 文件。
6. 打印提示信息，告知数据集和图片的保存位置。

### 自定义函数

`download_image()` 函数从 URL 下载图片并使用 Pillow 图像库（PIL）和 `io` 模块将其保存到本地。若图片成功下载，返回 True；否则返回 False。当请求失败时，函数会抛出带有错误信息的异常。

### 工作原理

`download_image` 函数接受两个参数：`image_url`，即要下载的图片 URL；`save_path`，即下载后图片的保存路径。

函数的工作流程如下：

首先，使用 `requests.get` 方法对 `image_url` 发起 GET 请求，获取图片数据。

`response.raise_for_status()` 用于检查请求是否成功。如果响应状态码表示错误（例如 404 - 未找到），则会抛出异常。这样确保只有在请求成功时才继续下载图片。

接着，将图片数据传递给 PIL（Python Imaging Library）模块的 `Image.open` 方法，创建一个 Image 对象。

`image.save(save_path)` 将图片保存到指定的 `save_path`，该路径应包含文件名和扩展名。

最后，函数返回 True，表示图片已成功下载并保存。如果过程中发生异常，函数会捕获异常，打印错误信息提示下载失败，并返回 False。

该函数适用于从 URL 下载图片并保存到本地，能够处理下载过程中的潜在错误，并反馈下载是否成功。

需要注意的是，`requests` 库用于发起 HTTP 请求，`PIL` 库用于处理图片，`BytesIO` 类用于将图片数据作为字节流处理。



### 总结

该脚本提供了一种便捷方式，通过下载所需图片，过滤下载失败的行，并将数据集保存为 CSV 文件，来准备机器学习所需的数据集。

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
[来自 LORA 微调示例的数据集示例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。