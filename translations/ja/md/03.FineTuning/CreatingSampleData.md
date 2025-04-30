<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44a77501fe39a2eb2b776dfdf9953b67",
  "translation_date": "2025-04-04T13:08:23+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "ja"
}
-->
# Hugging Faceからデータセットと関連画像をダウンロードして画像データセットを生成する

### 概要

このスクリプトは、必要な画像をダウンロードし、ダウンロードに失敗した行をフィルタリングして、データセットをCSVファイルとして保存することで、機械学習用のデータセットを準備します。

### 前提条件

このスクリプトを実行する前に、以下のライブラリをインストールしておいてください: `Pandas`, `Datasets`, `requests`, `PIL`, `io`。また、2行目の`'Insert_Your_Dataset'`をHugging Faceから取得したデータセットの名前に置き換える必要があります。

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

このスクリプトは以下の手順を実行します:

1. Hugging Faceからデータセットを`load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`関数を使用してダウンロードします。
2. ダウンロードに失敗した画像を含む行をフィルタリングします。
3. フィルタリングされたデータセットをCSVファイルとして保存します。

`download_image()`関数は、Pillow Image Library (PIL) と `io` モジュールを使用して、URLから画像をダウンロードしてローカルに保存します。この関数は画像が正常にダウンロードされた場合はTrueを返し、失敗した場合はFalseを返します。また、リクエストが失敗した場合は例外を発生させ、エラーメッセージを表示します。

### 動作の仕組み

`download_image`関数は2つのパラメータを取ります:  
- `image_url` はダウンロード対象の画像のURL  
- `save_path` はダウンロードした画像を保存するパス  

関数の動作は以下の通りです:

1. `requests.get`メソッドを使用して`image_url`にGETリクエストを送信し、URLから画像データを取得します。
2. `response.raise_for_status()`でリクエストが成功したかどうかを確認します。ステータスコードがエラーを示している場合（例: 404 - Not Found）、例外を発生させます。これにより、リクエストが成功した場合のみ画像のダウンロードを進めます。
3. 画像データをPILモジュールの`Image.open`メソッドに渡し、画像データからImageオブジェクトを作成します。
4. `image.save(save_path)`で画像を指定された`save_path`に保存します。`save_path`には、希望するファイル名と拡張子を含める必要があります。
5. 最終的に、画像が正常にダウンロードおよび保存されたことを示すためにTrueを返します。プロセス中に例外が発生した場合は例外をキャッチし、失敗を示すエラーメッセージを表示してFalseを返します。

この関数は、URLから画像をダウンロードしてローカルに保存する際に便利です。ダウンロードプロセス中の潜在的なエラーを処理し、ダウンロードが成功したかどうかのフィードバックを提供します。

なお、HTTPリクエストには`requests`ライブラリ、画像操作には`PIL`ライブラリ、画像データのバイトストリーム処理には`BytesIO`クラスが使用されています。

### 結論

このスクリプトは、必要な画像をダウンロードし、ダウンロードに失敗した行をフィルタリングして、データセットをCSVファイルとして保存することで、機械学習用のデータセットを簡単に準備する方法を提供します。

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

### サンプルコードのダウンロード 
[新しいデータセット生成スクリプト](../../../../code/04.Finetuning/generate_dataset.py)

### サンプルデータセット
[サンプルデータセット例（LORAを使用した微調整例から）](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で作成された文書が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。