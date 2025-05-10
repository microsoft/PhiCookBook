<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T21:23:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "vi"
}
-->
## Cách sử dụng các thành phần chat-completion từ Azure ML system registry để tinh chỉnh mô hình

Trong ví dụ này, chúng ta sẽ tiến hành tinh chỉnh mô hình Phi-3-mini-4k-instruct để hoàn thành cuộc hội thoại giữa 2 người sử dụng bộ dữ liệu ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.vi.png)

Ví dụ sẽ hướng dẫn bạn cách thực hiện tinh chỉnh bằng Azure ML SDK và Python, sau đó triển khai mô hình đã tinh chỉnh lên endpoint trực tuyến để suy luận thời gian thực.

### Dữ liệu huấn luyện

Chúng ta sẽ sử dụng bộ dữ liệu ultrachat_200k. Đây là phiên bản đã được lọc kỹ của bộ UltraChat và đã được dùng để huấn luyện Zephyr-7B-β, một mô hình chat 7b tiên tiến nhất hiện nay.

### Mô hình

Chúng ta sẽ dùng mô hình Phi-3-mini-4k-instruct để minh họa cách người dùng có thể tinh chỉnh mô hình cho tác vụ chat-completion. Nếu bạn mở notebook này từ một thẻ mô hình cụ thể, nhớ thay thế tên mô hình tương ứng.

### Các nhiệm vụ

- Chọn mô hình để tinh chỉnh.
- Chọn và khám phá dữ liệu huấn luyện.
- Cấu hình công việc tinh chỉnh.
- Chạy công việc tinh chỉnh.
- Xem lại các chỉ số huấn luyện và đánh giá.
- Đăng ký mô hình đã tinh chỉnh.
- Triển khai mô hình đã tinh chỉnh cho suy luận thời gian thực.
- Dọn dẹp tài nguyên.

## 1. Thiết lập các yêu cầu trước

- Cài đặt các thư viện phụ thuộc
- Kết nối đến AzureML Workspace. Tìm hiểu thêm tại thiết lập xác thực SDK. Thay thế <WORKSPACE_NAME>, <RESOURCE_GROUP> và <SUBSCRIPTION_ID> bên dưới.
- Kết nối đến azureml system registry
- Thiết lập tên experiment tùy chọn
- Kiểm tra hoặc tạo compute.

> [!NOTE]
> Yêu cầu một node GPU có thể có nhiều card GPU. Ví dụ, một node Standard_NC24rs_v3 có 4 GPU NVIDIA V100 trong khi Standard_NC12s_v3 có 2 GPU NVIDIA V100. Tham khảo tài liệu để biết thêm thông tin. Số lượng card GPU trên mỗi node được thiết lập trong tham số gpus_per_node bên dưới. Thiết lập đúng giá trị này sẽ đảm bảo sử dụng hết các GPU trong node. Các SKU GPU được khuyến nghị có thể tìm thấy ở đây và đây.

### Thư viện Python

Cài đặt các phụ thuộc bằng cách chạy cell dưới đây. Đây không phải bước tùy chọn nếu bạn chạy trong môi trường mới.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Tương tác với Azure ML

1. Script Python này dùng để tương tác với dịch vụ Azure Machine Learning (Azure ML). Dưới đây là tóm tắt chức năng:

    - Import các module cần thiết từ azure.ai.ml, azure.identity, và azure.ai.ml.entities. Cũng import module time.

    - Cố gắng xác thực bằng DefaultAzureCredential(), cung cấp trải nghiệm xác thực đơn giản để nhanh chóng phát triển ứng dụng trên Azure cloud. Nếu thất bại, sẽ dùng InteractiveBrowserCredential(), hiển thị cửa sổ đăng nhập tương tác.

    - Tiếp theo cố gắng tạo đối tượng MLClient bằng phương thức from_config, đọc cấu hình từ file mặc định (config.json). Nếu thất bại, tạo MLClient bằng cách cung cấp thủ công subscription_id, resource_group_name, và workspace_name.

    - Tạo thêm một MLClient khác cho Azure ML registry tên "azureml". Registry này lưu trữ mô hình, pipeline tinh chỉnh và môi trường.

    - Thiết lập experiment_name là "chat_completion_Phi-3-mini-4k-instruct".

    - Tạo timestamp duy nhất bằng cách chuyển thời gian hiện tại (tính theo giây kể từ epoch, kiểu số thực) sang số nguyên rồi chuyển sang chuỗi. Timestamp này dùng để tạo tên và phiên bản duy nhất.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. Chọn mô hình nền tảng để tinh chỉnh

1. Phi-3-mini-4k-instruct là mô hình nhẹ, 3.8 tỷ tham số, tiên tiến được xây dựng trên các bộ dữ liệu của Phi-2. Mô hình thuộc họ Phi-3, phiên bản Mini có 2 biến thể 4K và 128K, tương ứng độ dài ngữ cảnh (token) hỗ trợ. Chúng ta cần tinh chỉnh mô hình cho mục đích cụ thể. Bạn có thể duyệt các mô hình này trong Model Catalog của AzureML Studio, lọc theo tác vụ chat-completion. Ở ví dụ này, ta dùng Phi-3-mini-4k-instruct. Nếu mở notebook cho mô hình khác, hãy thay tên và phiên bản cho phù hợp.

    > [!NOTE]
    > Thuộc tính model id của mô hình sẽ được truyền làm đầu vào cho công việc tinh chỉnh. Thuộc tính này cũng có thể xem tại trường Asset ID trên trang chi tiết mô hình trong Model Catalog của AzureML Studio.

2. Script Python này tương tác với dịch vụ Azure ML. Chức năng:

    - Thiết lập model_name là "Phi-3-mini-4k-instruct".

    - Dùng phương thức get của thuộc tính models của registry_ml_client để lấy phiên bản mới nhất của mô hình theo tên từ Azure ML registry. Phương thức get gọi với 2 tham số: tên mô hình và nhãn "latest" để lấy phiên bản mới nhất.

    - In ra console thông báo tên, phiên bản và id của mô hình sẽ dùng để tinh chỉnh. Phương thức format của chuỗi được dùng để chèn tên, phiên bản, id lấy từ thuộc tính của foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Tạo compute để sử dụng cho công việc

Công việc finetune chỉ hoạt động với compute GPU. Kích thước compute phụ thuộc vào độ lớn mô hình và thường khá khó chọn đúng compute phù hợp. Trong cell này, chúng ta hướng dẫn người dùng chọn compute phù hợp.

> [!NOTE]
> Các compute liệt kê dưới đây hoạt động với cấu hình tối ưu nhất. Thay đổi cấu hình có thể gây lỗi Cuda Out Of Memory. Trong trường hợp đó, hãy nâng cấp compute lên kích thước lớn hơn.

> [!NOTE]
> Khi chọn compute_cluster_size bên dưới, đảm bảo compute có sẵn trong nhóm tài nguyên của bạn. Nếu compute không có sẵn, bạn có thể gửi yêu cầu để được cấp quyền truy cập tài nguyên compute.

### Kiểm tra mô hình có hỗ trợ tinh chỉnh không

1. Script Python này tương tác với mô hình Azure ML. Chức năng:

    - Import module ast, cung cấp các hàm xử lý cây cú pháp Python.

    - Kiểm tra xem đối tượng foundation_model (mô hình Azure ML) có tag tên finetune_compute_allow_list hay không. Tag trong Azure ML là cặp key-value dùng để lọc và sắp xếp mô hình.

    - Nếu có tag finetune_compute_allow_list, dùng ast.literal_eval để phân tích giá trị tag (chuỗi) thành danh sách Python, gán vào biến computes_allow_list. In ra thông báo yêu cầu tạo compute từ danh sách này.

    - Nếu không có tag, gán computes_allow_list là None và in thông báo tag này không có trong tags của mô hình.

    - Tóm lại, script kiểm tra tag trong metadata mô hình, chuyển giá trị tag thành danh sách nếu có, và cung cấp phản hồi cho người dùng.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Kiểm tra Compute Instance

1. Script Python này tương tác với dịch vụ Azure ML và thực hiện kiểm tra trên compute instance. Chức năng:

    - Cố gắng lấy compute instance có tên lưu trong compute_cluster từ workspace Azure ML. Nếu trạng thái provisioning của compute là "failed", ném lỗi ValueError.

    - Kiểm tra nếu computes_allow_list không phải None, chuyển tất cả kích thước compute trong danh sách sang chữ thường, rồi kiểm tra kích thước compute hiện tại có nằm trong danh sách hay không. Nếu không, ném ValueError.

    - Nếu computes_allow_list là None, kiểm tra kích thước compute có thuộc danh sách các kích thước GPU VM không được hỗ trợ hay không. Nếu có, ném ValueError.

    - Lấy danh sách tất cả kích thước compute có sẵn trong workspace. Duyệt danh sách này, nếu tên kích thước trùng với kích thước compute hiện tại, lấy số lượng GPU của kích thước đó và đánh dấu gpu_count_found là True.

    - Nếu tìm thấy số GPU, in ra số lượng GPU của compute instance. Nếu không, ném ValueError.

    - Tóm lại, script thực hiện các kiểm tra về trạng thái provisioning, kích thước compute so với danh sách cho phép hoặc cấm, và số lượng GPU trên compute instance trong workspace Azure ML.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Chọn bộ dữ liệu để tinh chỉnh mô hình

1. Chúng ta dùng bộ dữ liệu ultrachat_200k. Bộ dữ liệu có bốn phần, phù hợp cho Supervised fine-tuning (sft).
Generation ranking (gen). Số lượng ví dụ trong mỗi phần như sau:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Một vài cell tiếp theo thể hiện chuẩn bị dữ liệu cơ bản cho tinh chỉnh:

### Trực quan một số dòng dữ liệu

Chúng ta muốn mẫu này chạy nhanh, nên lưu các file train_sft, test_sft chứa 5% số dòng đã được lọc sẵn. Điều này nghĩa là mô hình tinh chỉnh sẽ có độ chính xác thấp hơn, nên không nên dùng trong thực tế.
download-dataset.py dùng để tải bộ dữ liệu ultrachat_200k và chuyển đổi dữ liệu sang định dạng phù hợp cho pipeline tinh chỉnh. Vì bộ dữ liệu lớn, nên ta chỉ dùng một phần nhỏ.

1. Chạy script dưới đây chỉ tải 5% dữ liệu. Có thể tăng tỉ lệ bằng cách thay đổi tham số dataset_split_pc theo phần trăm mong muốn.

    > [!NOTE]
    > Một số mô hình ngôn ngữ có mã ngôn ngữ khác nhau nên tên cột trong bộ dữ liệu cần phản ánh điều đó.

1. Đây là ví dụ về cách dữ liệu trông như thế nào
Bộ dữ liệu chat-completion được lưu ở định dạng parquet với mỗi mục theo cấu trúc:

    - Đây là tài liệu JSON (JavaScript Object Notation), định dạng trao đổi dữ liệu phổ biến. Không phải mã thực thi, mà là cách lưu và truyền dữ liệu. Cấu trúc gồm:

    - "prompt": chứa chuỗi mô tả tác vụ hoặc câu hỏi gửi đến trợ lý AI.

    - "messages": chứa mảng các đối tượng. Mỗi đối tượng đại diện cho một tin nhắn trong cuộc hội thoại giữa người dùng và trợ lý AI. Mỗi tin nhắn có hai trường:

    - "content": chuỗi nội dung tin nhắn.
    - "role": chuỗi xác định vai trò người gửi tin nhắn, có thể là "user" hoặc "assistant".
    - "prompt_id": chuỗi định danh duy nhất cho prompt.

1. Trong tài liệu JSON này, cuộc hội thoại thể hiện người dùng yêu cầu trợ lý AI tạo nhân vật chính cho câu chuyện dystopian. Trợ lý trả lời, rồi người dùng hỏi thêm chi tiết. Trợ lý đồng ý cung cấp thêm chi tiết. Toàn bộ hội thoại gắn với prompt id cụ thể.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Tải dữ liệu

1. Script Python này dùng để tải bộ dữ liệu bằng script phụ trợ download-dataset.py. Chức năng:

    - Import module os, cung cấp cách sử dụng các chức năng hệ điều hành.

    - Dùng os.system để chạy script download-dataset.py trong shell với các tham số chỉ định bộ dữ liệu cần tải (HuggingFaceH4/ultrachat_200k), thư mục tải về (ultrachat_200k_dataset), và tỉ lệ chia bộ dữ liệu (5). Trả về trạng thái thoát của lệnh được lưu trong biến exit_status.

    - Kiểm tra nếu exit_status khác 0 (0 thường nghĩa là thành công trên hệ Unix), nếu không thì ném Exception báo lỗi khi tải dữ liệu.

    - Tóm lại, script chạy lệnh tải dữ liệu bằng script phụ trợ, và ném lỗi nếu quá trình tải thất bại.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Nạp dữ liệu vào DataFrame

1. Script Python này nạp file JSON Lines vào pandas DataFrame và hiển thị 5 dòng đầu tiên. Chức năng:

    - Import thư viện pandas, thư viện mạnh để xử lý và phân tích dữ liệu.

    - Thiết lập độ rộng cột tối đa cho pandas là 0, nghĩa là hiển thị đầy đủ nội dung cột khi in DataFrame.

    - Dùng pd.read_json để nạp file train_sft.jsonl từ thư mục ultrachat_200k_dataset. Tham số lines=True cho biết file ở định dạng JSON Lines, mỗi dòng là một đối tượng JSON riêng biệt.

    - Dùng phương thức head để hiển thị 5 dòng đầu của DataFrame. Nếu DataFrame ít hơn 5 dòng thì hiển thị hết.

    - Tóm lại, script nạp file JSON Lines vào DataFrame và hiển thị 5 dòng đầu với đầy đủ nội dung cột.

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. Gửi công việc tinh chỉnh sử dụng mô hình và dữ liệu làm đầu vào

Tạo công việc sử dụng thành phần pipeline chat-completion. Tìm hiểu thêm về tất cả các tham số hỗ trợ tinh chỉnh.

### Định nghĩa các tham số tinh chỉnh

1. Các tham số tinh chỉnh có thể chia thành 2 nhóm - tham số huấn luyện, tham số tối ưu hóa

1. Tham số huấn luyện định nghĩa các khía cạnh huấn luyện như -

    - Bộ tối ưu, bộ điều chỉnh học (scheduler) sử dụng
    - Chỉ số để tối ưu hóa tinh chỉnh
    - Số bước huấn luyện, kích thước batch, v.v.
    - Tham số tối ưu hóa giúp tối ưu bộ nhớ GPU và sử dụng hiệu quả tài nguyên compute.

1. Dưới đây là một số tham số thuộc nhóm này. Tham số tối ưu hóa khác nhau với từng mô hình và được đóng gói cùng mô hình để xử lý sự khác biệt.

    - Bật deepspeed và LoRA
    - Bật huấn luyện với độ chính xác hỗn hợp (mixed precision)
    - Bật huấn luyện đa node

> [!NOTE]
> Huấn luyện có giám sát có thể dẫn đến mất đồng bộ hoặc quên kiến thức (catastrophic forgetting). Chúng tôi khuyến nghị kiểm tra vấn đề này và chạy giai đoạn căn chỉnh (alignment) sau khi tinh chỉnh.

### Tham số tinh chỉnh

1. Script Python này thiết lập các tham số cho quá trình tinh chỉnh mô hình học máy. Chức năng:

    - Thiết lập tham số huấn luyện mặc định như số epoch, kích thước batch huấn luyện và đánh giá, tốc độ học, loại bộ điều chỉnh tốc độ học.

    - Thiết lập tham số tối ưu hóa mặc định như bật Layer-wise Relevance Propagation (LoRa) và DeepSpeed, cùng giai đoạn DeepSpeed.

    - Kết hợp tham số huấn luyện và tối ưu hóa vào dictionary finetune_parameters.

    - Kiểm tra xem foundation_model có tham số mặc định riêng không. Nếu có, in cảnh báo và cập nhật finetune_parameters bằng các tham số mặc định riêng của mô hình. Dùng ast.literal_eval để chuyển tham số từ chuỗi sang dictionary Python.

    - In ra tập tham số tinh chỉnh cuối cùng sẽ dùng cho chạy.

    - Tóm lại, script thiết lập và hiển thị tham số tinh chỉnh mô hình học máy, có thể ghi đè tham số mặc định bằng tham số riêng của mô hình.

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline huấn luyện

1. Script Python này định nghĩa hàm tạo tên hiển thị cho pipeline huấn luyện mô hình, rồi gọi hàm để tạo và in tên hiển thị. Chức năng:

    1. Định nghĩa hàm get_pipeline_display_name. Hàm này tạo tên hiển thị dựa trên các tham số liên quan đến pipeline huấn luyện.

    2. Trong hàm, tính tổng kích thước batch bằng cách nhân kích thước batch trên mỗi thiết bị, số bước tích lũy gradient, số GPU trên mỗi node và số node dùng để tinh chỉnh.

    3. Lấy các tham số khác như loại bộ điều chỉnh tốc độ học, có dùng DeepSpeed hay không, giai đoạn DeepSpeed, có dùng LoRa hay không, giới hạn số checkpoint mô hình lưu giữ, và độ dài tối đa chuỗi.

    4. Tạo chuỗi chứa tất cả tham số này, phân tách bằng dấu gạch ngang. Nếu dùng DeepSpeed hoặc LoRa thì chuỗi có thêm "ds" kèm giai đoạn DeepSpeed hoặc "lora". Nếu không thì có "nods" hoặc "nolora".

    5. Hàm trả về chuỗi này làm tên hiển thị cho pipeline huấn luyện.

    6. Sau khi định nghĩa, gọi hàm để tạo tên hiển thị và in ra.

    7. Tóm lại, script tạo tên hiển thị cho pipeline huấn luyện mô hình học máy.
training pipeline dựa trên nhiều tham số khác nhau, sau đó in tên hiển thị này ra. ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Cấu hình Pipeline

Script Python này đang định nghĩa và cấu hình một pipeline machine learning sử dụng Azure Machine Learning SDK. Dưới đây là phân tích những gì nó thực hiện:

1. Nó nhập các module cần thiết từ Azure AI ML SDK.
1. Nó lấy một thành phần pipeline có tên "chat_completion_pipeline" từ registry.
1. Nó định nghĩa một pipeline job sử dụng `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, nghĩa là pipeline sẽ dừng nếu bất kỳ bước nào thất bại.
1. Tóm lại, script này đang định nghĩa và cấu hình một pipeline machine learning cho nhiệm vụ hoàn thành chat sử dụng Azure Machine Learning SDK.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Gửi Job

1. Script Python này đang gửi một job pipeline machine learning tới workspace Azure Machine Learning và chờ job hoàn thành. Dưới đây là phân tích những gì nó thực hiện:

- Nó gọi phương thức create_or_update của đối tượng jobs trong workspace_ml_client để gửi job pipeline. Pipeline được chạy được chỉ định bởi pipeline_object, và thí nghiệm dưới đó job được chạy được chỉ định bởi experiment_name.

- Sau đó nó gọi phương thức stream của đối tượng jobs trong workspace_ml_client để chờ job pipeline hoàn thành. Job được chờ là job có tên được lấy từ thuộc tính name của pipeline_job.

- Tóm lại, script này gửi một job pipeline machine learning tới workspace Azure Machine Learning, rồi chờ job hoàn thành.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Đăng ký mô hình fine tuned với workspace

Chúng ta sẽ đăng ký mô hình từ kết quả đầu ra của job fine tuning. Việc này sẽ theo dõi mối quan hệ dòng chảy giữa mô hình fine tuned và job fine tuning. Job fine tuning cũng theo dõi dòng chảy đến mô hình nền tảng, dữ liệu và mã huấn luyện.

### Đăng ký mô hình ML

1. Script Python này đang đăng ký một mô hình machine learning đã được huấn luyện trong pipeline Azure Machine Learning. Dưới đây là phân tích những gì nó thực hiện:

- Nó nhập các module cần thiết từ Azure AI ML SDK.

- Nó kiểm tra xem đầu ra trained_model có sẵn từ pipeline job hay không bằng cách gọi phương thức get của đối tượng jobs trong workspace_ml_client và truy cập thuộc tính outputs.

- Nó tạo đường dẫn tới mô hình đã huấn luyện bằng cách định dạng chuỗi với tên pipeline job và tên đầu ra ("trained_model").

- Nó định nghĩa tên cho mô hình fine tuned bằng cách thêm "-ultrachat-200k" vào tên mô hình gốc và thay thế các dấu gạch chéo bằng dấu gạch ngang.

- Nó chuẩn bị đăng ký mô hình bằng cách tạo một đối tượng Model với các tham số khác nhau, bao gồm đường dẫn tới mô hình, loại mô hình (MLflow model), tên và phiên bản của mô hình, cùng mô tả cho mô hình.

- Nó đăng ký mô hình bằng cách gọi phương thức create_or_update của đối tượng models trong workspace_ml_client với đối tượng Model làm đối số.

- Nó in ra mô hình đã được đăng ký.

1. Tóm lại, script này đăng ký một mô hình machine learning đã được huấn luyện trong pipeline Azure Machine Learning.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. Triển khai mô hình fine tuned tới endpoint online

Các endpoint online cung cấp API REST bền vững, có thể tích hợp với các ứng dụng cần sử dụng mô hình.

### Quản lý Endpoint

1. Script Python này đang tạo một managed online endpoint trong Azure Machine Learning cho mô hình đã đăng ký. Dưới đây là phân tích những gì nó thực hiện:

- Nó nhập các module cần thiết từ Azure AI ML SDK.

- Nó định nghĩa một tên duy nhất cho endpoint online bằng cách thêm dấu thời gian vào chuỗi "ultrachat-completion-".

- Nó chuẩn bị tạo endpoint online bằng cách tạo một đối tượng ManagedOnlineEndpoint với các tham số khác nhau, bao gồm tên endpoint, mô tả endpoint và chế độ xác thực ("key").

- Nó tạo endpoint online bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng ManagedOnlineEndpoint làm đối số. Sau đó chờ quá trình tạo hoàn thành bằng cách gọi phương thức wait.

1. Tóm lại, script này đang tạo một managed online endpoint trong Azure Machine Learning cho mô hình đã đăng ký.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Bạn có thể tìm danh sách SKU được hỗ trợ để triển khai tại đây - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Triển khai mô hình ML

1. Script Python này đang triển khai một mô hình machine learning đã đăng ký tới một managed online endpoint trong Azure Machine Learning. Dưới đây là phân tích những gì nó thực hiện:

    - Nó nhập module ast, cung cấp các hàm để xử lý cây cú pháp trừu tượng của Python.

    - Nó đặt loại instance cho việc triển khai là "Standard_NC6s_v3".

    - Nó kiểm tra xem tag inference_compute_allow_list có trong mô hình nền tảng hay không. Nếu có, nó chuyển giá trị tag từ chuỗi sang danh sách Python và gán cho inference_computes_allow_list. Nếu không có, nó đặt inference_computes_allow_list thành None.

    - Nó kiểm tra xem loại instance được chỉ định có nằm trong danh sách cho phép hay không. Nếu không, nó in thông báo yêu cầu người dùng chọn loại instance từ danh sách cho phép.

    - Nó chuẩn bị tạo deployment bằng cách tạo một đối tượng ManagedOnlineDeployment với các tham số khác nhau, bao gồm tên deployment, tên endpoint, ID của mô hình, loại instance và số lượng, cấu hình kiểm tra trạng thái sống (liveness probe), và các thiết lập yêu cầu.

    - Nó tạo deployment bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng ManagedOnlineDeployment làm đối số. Sau đó chờ quá trình tạo hoàn thành bằng cách gọi phương thức wait.

    - Nó đặt lưu lượng truy cập của endpoint để chuyển 100% lưu lượng tới deployment "demo".

    - Nó cập nhật endpoint bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng endpoint làm đối số. Sau đó chờ quá trình cập nhật hoàn thành bằng cách gọi phương thức result.

1. Tóm lại, script này đang triển khai một mô hình machine learning đã đăng ký tới một managed online endpoint trong Azure Machine Learning.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Kiểm thử endpoint với dữ liệu mẫu

Chúng ta sẽ lấy một số dữ liệu mẫu từ bộ dữ liệu test và gửi tới endpoint online để suy luận. Sau đó sẽ hiển thị nhãn dự đoán cùng với nhãn thực tế.

### Đọc kết quả

1. Script Python này đang đọc một file JSON Lines vào một pandas DataFrame, lấy một mẫu ngẫu nhiên, và đặt lại chỉ số. Dưới đây là phân tích những gì nó thực hiện:

    - Nó đọc file ./ultrachat_200k_dataset/test_gen.jsonl vào pandas DataFrame. Hàm read_json được sử dụng với đối số lines=True vì file có định dạng JSON Lines, mỗi dòng là một đối tượng JSON riêng biệt.

    - Nó lấy một mẫu ngẫu nhiên gồm 1 dòng từ DataFrame. Hàm sample được dùng với đối số n=1 để chỉ định số dòng ngẫu nhiên lấy ra.

    - Nó đặt lại chỉ số của DataFrame. Hàm reset_index được dùng với đối số drop=True để loại bỏ chỉ số cũ và thay thế bằng chỉ số mới kiểu số nguyên mặc định.

    - Nó hiển thị 2 dòng đầu tiên của DataFrame bằng hàm head với đối số 2. Tuy nhiên, vì DataFrame chỉ có một dòng sau khi lấy mẫu, nên chỉ dòng đó sẽ được hiển thị.

1. Tóm lại, script này đọc file JSON Lines vào pandas DataFrame, lấy một mẫu ngẫu nhiên gồm 1 dòng, đặt lại chỉ số và hiển thị dòng đầu tiên.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### Tạo đối tượng JSON

1. Script Python này đang tạo một đối tượng JSON với các tham số cụ thể và lưu nó vào file. Dưới đây là phân tích những gì nó thực hiện:

    - Nó nhập module json, cung cấp các hàm làm việc với dữ liệu JSON.

    - Nó tạo một dictionary parameters với các khóa và giá trị đại diện cho tham số cho mô hình machine learning. Các khóa là "temperature", "top_p", "do_sample" và "max_new_tokens", với các giá trị tương ứng là 0.6, 0.9, True và 200.

    - Nó tạo một dictionary khác test_json với hai khóa: "input_data" và "params". Giá trị của "input_data" là một dictionary khác với các khóa "input_string" và "parameters". Giá trị của "input_string" là một danh sách chứa tin nhắn đầu tiên từ DataFrame test_df. Giá trị của "parameters" là dictionary parameters đã tạo trước đó. Giá trị của "params" là một dictionary rỗng.

    - Nó mở file có tên sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### Gọi Endpoint

1. Script Python này đang gọi một endpoint online trong Azure Machine Learning để chấm điểm một file JSON. Dưới đây là phân tích những gì nó thực hiện:

    - Nó gọi phương thức invoke của thuộc tính online_endpoints của đối tượng workspace_ml_client. Phương thức này dùng để gửi yêu cầu tới endpoint online và nhận phản hồi.

    - Nó chỉ định tên endpoint và deployment với các tham số endpoint_name và deployment_name. Trong trường hợp này, tên endpoint được lưu trong biến online_endpoint_name và tên deployment là "demo".

    - Nó chỉ định đường dẫn tới file JSON cần chấm điểm với tham số request_file. Ở đây file là ./ultrachat_200k_dataset/sample_score.json.

    - Nó lưu phản hồi từ endpoint vào biến response.

    - Nó in ra phản hồi thô.

1. Tóm lại, script này gọi một endpoint online trong Azure Machine Learning để chấm điểm file JSON và in phản hồi.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Xóa endpoint online

1. Đừng quên xóa endpoint online, nếu không bạn sẽ tiếp tục bị tính phí cho tài nguyên compute mà endpoint sử dụng. Dòng code Python này đang xóa một endpoint online trong Azure Machine Learning. Dưới đây là phân tích những gì nó thực hiện:

    - Nó gọi phương thức begin_delete của thuộc tính online_endpoints của workspace_ml_client. Phương thức này dùng để bắt đầu quá trình xóa một endpoint online.

    - Nó chỉ định tên endpoint cần xóa với tham số name. Ở đây tên endpoint được lưu trong biến online_endpoint_name.

    - Nó gọi phương thức wait để chờ quá trình xóa hoàn tất. Đây là thao tác chặn, nghĩa là script sẽ không tiếp tục cho tới khi xóa xong.

    - Tóm lại, dòng code này bắt đầu quá trình xóa một endpoint online trong Azure Machine Learning và chờ cho quá trình hoàn tất.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.