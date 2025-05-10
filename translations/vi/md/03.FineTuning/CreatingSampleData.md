<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:25:42+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "vi"
}
-->
# Tạo Bộ Dữ Liệu Hình Ảnh bằng cách tải DataSet từ Hugging Face và các hình ảnh liên quan


### Tổng quan

Script này chuẩn bị một bộ dữ liệu cho học máy bằng cách tải các hình ảnh cần thiết, lọc bỏ các dòng mà việc tải hình ảnh thất bại, và lưu bộ dữ liệu dưới dạng file CSV.

### Yêu cầu

Trước khi chạy script này, hãy đảm bảo đã cài đặt các thư viện sau: `Pandas`, `Datasets`, `requests`, `PIL`, và `io`. Bạn cũng cần thay thế `'Insert_Your_Dataset'` ở dòng 2 bằng tên bộ dữ liệu của bạn từ Hugging Face.

Các thư viện cần thiết:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Chức năng

Script thực hiện các bước sau:

1. Tải bộ dữ liệu từ Hugging Face sử dụng `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` hàm download_image() tải hình ảnh từ URL và lưu trữ cục bộ bằng thư viện Pillow Image (PIL) và module `io`. Hàm trả về True nếu hình ảnh được tải thành công, ngược lại trả về False. Hàm cũng ném ngoại lệ với thông báo lỗi khi yêu cầu tải hình ảnh thất bại.

### Cách hoạt động

Hàm download_image nhận hai tham số: image_url, là URL của hình ảnh cần tải, và save_path, là đường dẫn nơi hình ảnh tải về sẽ được lưu.

Cách hàm hoạt động như sau:

Nó bắt đầu bằng việc gửi một yêu cầu GET tới image_url bằng phương thức requests.get. Điều này lấy dữ liệu hình ảnh từ URL.

Dòng response.raise_for_status() kiểm tra xem yêu cầu có thành công hay không. Nếu mã trạng thái trả về là lỗi (ví dụ: 404 - Không tìm thấy), nó sẽ ném ngoại lệ. Điều này đảm bảo chỉ tiếp tục tải hình ảnh khi yêu cầu thành công.

Dữ liệu hình ảnh sau đó được truyền vào phương thức Image.open từ module PIL (Python Imaging Library). Phương thức này tạo một đối tượng Image từ dữ liệu hình ảnh.

Dòng image.save(save_path) lưu hình ảnh vào đường dẫn save_path đã chỉ định. save_path nên bao gồm tên file và phần mở rộng mong muốn.

Cuối cùng, hàm trả về True để báo hiệu hình ảnh đã được tải và lưu thành công. Nếu có bất kỳ ngoại lệ nào xảy ra trong quá trình này, nó sẽ bắt ngoại lệ đó, in ra thông báo lỗi cho biết việc tải thất bại, và trả về False.

Hàm này rất hữu ích để tải hình ảnh từ URL và lưu chúng cục bộ. Nó xử lý các lỗi có thể xảy ra trong quá trình tải và cung cấp phản hồi về việc tải có thành công hay không.

Cần lưu ý rằng thư viện requests được sử dụng để gửi các yêu cầu HTTP, thư viện PIL dùng để làm việc với hình ảnh, và lớp BytesIO được sử dụng để xử lý dữ liệu hình ảnh dưới dạng luồng byte.



### Kết luận

Script này cung cấp một cách tiện lợi để chuẩn bị bộ dữ liệu cho học máy bằng cách tải các hình ảnh cần thiết, lọc bỏ các dòng mà việc tải hình ảnh thất bại, và lưu bộ dữ liệu dưới dạng file CSV.

### Ví dụ Script

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

### Tải Mẫu Code  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Bộ Dữ Liệu Mẫu  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được xem là nguồn chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.