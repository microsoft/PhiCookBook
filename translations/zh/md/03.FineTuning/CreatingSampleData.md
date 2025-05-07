<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-07T13:25:47+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "zh"
}
-->
# 通过从 Hugging Face 下载数据集及相关图片生成图像数据集


### 概述

此脚本通过下载所需图片、过滤下载失败的行，并将数据集保存为 CSV 文件，来准备机器学习的数据集。

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

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函数从 Hugging Face 下载数据集。`download_image()` 函数通过 Pillow Image 库（PIL）和 `io` 模块从 URL 下载图片并保存到本地。如果图片下载成功，返回 True；否则返回 False。当请求失败时，该函数会抛出带有错误信息的异常。

### 工作原理

download_image 函数接受两个参数：image_url，即要下载图片的 URL；save_path，即保存下载图片的路径。

函数的工作流程如下：

首先，使用 requests.get 方法对 image_url 发起 GET 请求，从 URL 获取图片数据。

response.raise_for_status() 用于检查请求是否成功。如果响应状态码表示错误（例如 404 - 未找到），它会抛出异常。这样确保只有在请求成功时才继续下载图片。

接着，将图片数据传给 PIL（Python Imaging Library）模块的 Image.open 方法，该方法会创建一个 Image 对象。

image.save(save_path) 将图片保存到指定的 save_path，save_path 应包含文件名和扩展名。

最后，函数返回 True，表示图片成功下载并保存。如果过程中出现任何异常，函数会捕获异常，打印错误信息，并返回 False。

该函数适合从 URL 下载图片并保存到本地，能处理下载过程中的潜在错误，并反馈下载是否成功。

需要注意的是，requests 库用于发起 HTTP 请求，PIL 库用于处理图片，BytesIO 类用于将图片数据作为字节流处理。



### 总结

此脚本通过下载所需图片、过滤下载失败的行，并将数据集保存为 CSV 文件，提供了一种便捷的机器学习数据集准备方法。

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
[LORA 微调示例中的数据集示例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免责声明**：  
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始语言的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。