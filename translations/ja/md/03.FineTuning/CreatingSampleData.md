<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-08T05:13:54+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ja"
}
-->
# Hugging Faceからデータセットと関連画像をダウンロードして画像データセットを生成する


### 概要

このスクリプトは、機械学習用のデータセットを準備するために必要な画像をダウンロードし、画像のダウンロードに失敗した行を除外して、データセットをCSVファイルとして保存します。

### 前提条件

このスクリプトを実行する前に、以下のライブラリがインストールされていることを確認してください: `Pandas`、`Datasets`、`requests`、`PIL`、および `io`。また、2行目の`'Insert_Your_Dataset'`をHugging Faceのデータセット名に置き換える必要があります。

必要なライブラリ:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 機能

スクリプトは以下の手順を実行します:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`関数は、URLから画像をダウンロードし、Pillow Image Library（PIL）と`io`モジュールを使ってローカルに保存します。画像が正常にダウンロードできればTrueを返し、そうでなければFalseを返します。リクエストが失敗した場合は、エラーメッセージを含む例外を発生させます。

### 仕組み

download_image関数は2つのパラメータを取ります。image_urlはダウンロードする画像のURL、save_pathはダウンロードした画像を保存するパスです。

関数の動作は以下の通りです:

まず、requests.getメソッドを使ってimage_urlにGETリクエストを送信し、画像データを取得します。

response.raise_for_status()はリクエストが成功したかどうかをチェックします。もしステータスコードがエラー（例: 404 - Not Found）であれば例外を発生させます。これにより、リクエストが成功した場合のみ画像のダウンロード処理が進みます。

取得した画像データはPIL（Python Imaging Library）モジュールのImage.openメソッドに渡され、Imageオブジェクトが生成されます。

image.save(save_path)で指定されたパスに画像を保存します。save_pathにはファイル名と拡張子を含める必要があります。

最後に、画像が正常にダウンロード・保存されたことを示すためにTrueを返します。処理中に例外が発生した場合は、例外をキャッチしてエラーメッセージを表示し、Falseを返します。

この関数はURLから画像をダウンロードしてローカルに保存するのに便利です。ダウンロード中のエラーを処理し、成功したかどうかをフィードバックします。

requestsライブラリはHTTPリクエストを行うために使われ、PILライブラリは画像処理に使われ、BytesIOクラスは画像データをバイトストリームとして扱うために使用されている点に注意してください。



### まとめ

このスクリプトは、機械学習用データセットを準備する際に必要な画像をダウンロードし、ダウンロードに失敗した行を除外して、CSVファイルとして保存する便利な方法を提供します。

### サンプルスクリプト

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

### サンプルコードダウンロード  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### サンプルデータセット  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。