<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:46:19+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ko"
}
-->
# Hugging Face에서 데이터셋과 관련 이미지를 다운로드하여 이미지 데이터셋 생성하기


### 개요

이 스크립트는 머신러닝용 데이터셋을 준비하기 위해 필요한 이미지를 다운로드하고, 이미지 다운로드에 실패한 행을 필터링한 후, 데이터셋을 CSV 파일로 저장합니다.

### 사전 준비 사항

이 스크립트를 실행하기 전에 `Pandas`, `Datasets`, `requests`, `PIL`, `io` 라이브러리가 설치되어 있어야 합니다. 또한 2번째 줄에 있는 `'Insert_Your_Dataset'`을 Hugging Face에서 사용할 데이터셋 이름으로 바꿔야 합니다.

필요한 라이브러리:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 기능 설명

스크립트는 다음 단계를 수행합니다:

1. `load_dataset()` 함수를 사용해 Hugging Face에서 데이터셋을 다운로드합니다.
2. `to_pandas()` 메서드를 사용해 Hugging Face 데이터셋을 Pandas DataFrame으로 변환하여 다루기 쉽게 만듭니다.
3. 데이터셋과 이미지를 저장할 디렉토리를 생성합니다.
4. DataFrame의 각 행을 순회하며 커스텀 함수 `download_image()`로 이미지를 다운로드하고, 이미지 다운로드에 실패한 행은 제외하여 `filtered_rows`라는 새 DataFrame에 추가합니다.
5. 필터링된 행들로 새 DataFrame을 만들고 이를 CSV 파일로 저장합니다.
6. 데이터셋과 이미지가 저장된 위치를 출력합니다.

### 커스텀 함수

`download_image()` 함수는 URL에서 이미지를 다운로드하여 Pillow Image Library(PIL)와 `io` 모듈을 사용해 로컬에 저장합니다. 이미지가 성공적으로 다운로드되면 True를 반환하고, 실패하면 False를 반환합니다. 요청이 실패할 경우에는 에러 메시지와 함께 예외를 발생시킵니다.

### 작동 원리

`download_image` 함수는 두 개의 매개변수를 받습니다: 다운로드할 이미지의 URL인 image_url과 다운로드한 이미지를 저장할 경로인 save_path입니다.

함수 작동 방식은 다음과 같습니다:

먼저 requests.get 메서드를 사용해 image_url에 GET 요청을 보냅니다. 이를 통해 URL에서 이미지 데이터를 가져옵니다.

`response.raise_for_status()`는 요청이 성공했는지 확인합니다. 만약 응답 상태 코드가 오류(예: 404 - Not Found)를 나타내면 예외를 발생시킵니다. 이로써 요청이 성공했을 때만 이미지 다운로드를 진행하게 됩니다.

이미지 데이터는 PIL(Python Imaging Library)의 Image.open 메서드에 전달되어 Image 객체로 생성됩니다.

`image.save(save_path)`는 이미지를 지정한 save_path에 저장합니다. save_path에는 원하는 파일명과 확장자가 포함되어야 합니다.

마지막으로 함수는 이미지가 성공적으로 다운로드되고 저장되었음을 나타내기 위해 True를 반환합니다. 과정 중 예외가 발생하면 예외를 잡아내고 실패 메시지를 출력한 뒤 False를 반환합니다.

이 함수는 URL에서 이미지를 다운로드해 로컬에 저장할 때 유용하며, 다운로드 과정에서 발생할 수 있는 오류를 처리하고 성공 여부를 알려줍니다.

참고로 requests 라이브러리는 HTTP 요청을 보내는 데 사용되고, PIL 라이브러리는 이미지 작업에, BytesIO 클래스는 이미지 데이터를 바이트 스트림으로 다루는 데 사용됩니다.



### 결론

이 스크립트는 필요한 이미지를 다운로드하고, 이미지 다운로드에 실패한 행을 걸러내며, 최종적으로 데이터셋을 CSV 파일로 저장하여 머신러닝용 데이터셋을 손쉽게 준비할 수 있도록 도와줍니다.

### 샘플 스크립트

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

### 샘플 코드 다운로드  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### 샘플 데이터셋  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.