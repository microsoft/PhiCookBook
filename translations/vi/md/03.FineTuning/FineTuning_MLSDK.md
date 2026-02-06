## Cách sử dụng các thành phần chat-completion từ hệ thống đăng ký Azure ML để tinh chỉnh mô hình

Trong ví dụ này, chúng ta sẽ thực hiện tinh chỉnh mô hình Phi-3-mini-4k-instruct để hoàn thành cuộc trò chuyện giữa 2 người sử dụng tập dữ liệu ultrachat_200k.

![MLFineTune](../../../../translated_images/vi/MLFineTune.928d4c6b3767dd35.webp)

Ví dụ sẽ chỉ bạn cách thực hiện tinh chỉnh sử dụng Azure ML SDK và Python, sau đó triển khai mô hình đã được tinh chỉnh tới một điểm cuối trực tuyến để suy luận thời gian thực.

### Dữ liệu huấn luyện

Chúng ta sẽ sử dụng tập dữ liệu ultrachat_200k. Đây là phiên bản được lọc kỹ của tập dữ liệu UltraChat và được sử dụng để huấn luyện Zephyr-7B-β, một mô hình chat 7b hiện đại hàng đầu.

### Mô hình

Chúng ta sẽ sử dụng mô hình Phi-3-mini-4k-instruct để minh họa cách người dùng có thể tinh chỉnh mô hình cho tác vụ chat-completion. Nếu bạn mở sổ tay này từ một thẻ mô hình cụ thể, nhớ thay thế tên mô hình tương ứng.

### Các nhiệm vụ

- Chọn một mô hình để tinh chỉnh.
- Chọn và khám phá dữ liệu huấn luyện.
- Cấu hình công việc tinh chỉnh.
- Chạy công việc tinh chỉnh.
- Xem lại các chỉ số huấn luyện và đánh giá.
- Đăng ký mô hình đã tinh chỉnh.
- Triển khai mô hình đã tinh chỉnh cho suy luận thời gian thực.
- Dọn dẹp tài nguyên.

## 1. Cài đặt các bước chuẩn bị

- Cài đặt các phụ thuộc
- Kết nối với AzureML Workspace. Tìm hiểu thêm tại thiết lập xác thực SDK. Thay thế <WORKSPACE_NAME>, <RESOURCE_GROUP> và <SUBSCRIPTION_ID> bên dưới.
- Kết nối với hệ thống đăng ký azureml
- Đặt tên thử nghiệm tùy chọn
- Kiểm tra hoặc tạo compute.

> [!NOTE]
> Yêu cầu là một nút GPU đơn có thể có nhiều card GPU. Ví dụ, trong một nút của Standard_NC24rs_v3 có 4 GPU NVIDIA V100 trong khi ở Standard_NC12s_v3 có 2 GPU NVIDIA V100. Tham khảo tài liệu để biết thông tin này. Số lượng card GPU trên mỗi nút được thiết lập trong tham số gpus_per_node bên dưới. Thiết lập giá trị này đúng sẽ đảm bảo sử dụng đầy đủ các GPU trong nút. Các SKU compute GPU được khuyến nghị có thể được tìm thấy tại đây và tại đây.

### Thư viện Python

Cài đặt các phụ thuộc bằng cách chạy ô lệnh dưới đây. Đây không phải bước tùy chọn nếu chạy trong môi trường mới.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Tương tác với Azure ML

1. Script Python này được dùng để tương tác với dịch vụ Azure Machine Learning (Azure ML). Dưới đây là phần giải thích:

    - Nó nhập các mô-đun cần thiết từ các gói azure.ai.ml, azure.identity, và azure.ai.ml.entities. Nó cũng nhập mô-đun time.

    - Nó cố gắng xác thực bằng DefaultAzureCredential(), cung cấp trải nghiệm xác thực đơn giản để nhanh chóng bắt đầu phát triển ứng dụng chạy trên đám mây Azure. Nếu không thành công, nó sẽ chuyển sang InteractiveBrowserCredential(), cung cấp lời nhắc đăng nhập tương tác.

    - Sau đó nó cố gắng tạo một thể hiện MLClient sử dụng phương thức from_config, đọc cấu hình từ tệp config mặc định (config.json). Nếu không thành công, nó tạo MLClient bằng cách cung cấp thủ công subscription_id, resource_group_name, và workspace_name.

    - Nó tạo thêm một thể hiện MLClient khác, lần này cho hệ thống đăng ký Azure ML có tên "azureml". Hệ thống đăng ký này là nơi lưu trữ các mô hình, pipeline tinh chỉnh và môi trường.

    - Nó đặt tên thử nghiệm experiment_name thành "chat_completion_Phi-3-mini-4k-instruct".

    - Nó tạo một dấu thời gian duy nhất bằng cách chuyển đổi thời gian hiện tại (tính bằng giây kể từ epoch, dưới dạng số thực) thành số nguyên rồi thành chuỗi. Dấu thời gian này có thể được dùng để tạo tên và phiên bản duy nhất.

    ```python
    # Nhập các mô-đun cần thiết từ Azure ML và Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Nhập mô-đun time
    
    # Thử xác thực bằng DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Nếu DefaultAzureCredential thất bại, sử dụng InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Thử tạo một thể hiện MLClient bằng cách sử dụng tệp cấu hình mặc định
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Nếu điều đó thất bại, tạo một thể hiện MLClient bằng cách cung cấp thủ công các chi tiết
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Tạo một thể hiện MLClient khác cho registry Azure ML có tên "azureml"
    # Registry này là nơi lưu trữ các mô hình, pipeline tinh chỉnh và môi trường
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Đặt tên cho experiment
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Tạo một dấu thời gian duy nhất có thể được sử dụng cho tên và phiên bản cần duy nhất
    timestamp = str(int(time.time()))
    ```

## 2. Chọn mô hình nền tảng để tinh chỉnh

1. Phi-3-mini-4k-instruct là mô hình nhẹ có 3.8 tỷ tham số, hiện đại, được xây dựng dựa trên các tập dữ liệu đã sử dụng cho Phi-2. Mô hình thuộc dòng Phi-3, và phiên bản Mini có hai biến thể 4K và 128K - là độ dài ngữ cảnh (tính theo token) mà nó có thể hỗ trợ, chúng ta cần tinh chỉnh mô hình cho mục đích cụ thể để sử dụng. Bạn có thể duyệt các mô hình này trong Model Catalog của AzureML Studio, lọc theo tác vụ chat-completion. Trong ví dụ này, chúng ta sử dụng mô hình Phi-3-mini-4k-instruct. Nếu bạn mở sổ tay này cho mô hình khác, hãy thay tên và phiên bản mô hình tương ứng.

> [!NOTE]
> Thuộc tính model id của mô hình. Thuộc tính này sẽ được chuyển làm đầu vào cho công việc tinh chỉnh. Nó cũng có sẵn dưới dạng trường Asset ID trong trang chi tiết mô hình tại AzureML Studio Model Catalog.

2. Script Python này tương tác với dịch vụ Azure Machine Learning (Azure ML). Dưới đây là giải thích:

    - Nó thiết lập biến model_name là "Phi-3-mini-4k-instruct".

    - Nó sử dụng phương thức get của thuộc tính models của đối tượng registry_ml_client để lấy phiên bản mới nhất của mô hình có tên chỉ định từ hệ thống đăng ký Azure ML. Phương thức get được gọi với hai đối số: tên mô hình và nhãn dùng để lấy phiên bản mới nhất của mô hình.

    - Nó in ra thông báo trên console chỉ tên, phiên bản, và id của mô hình sẽ được sử dụng để tinh chỉnh. Phương thức format của chuỗi được dùng để chèn tên, phiên bản, và id của mô hình vào thông báo. Các thuộc tính đó được truy cập trên đối tượng foundation_model.

    ```python
    # Đặt tên mô hình
    model_name = "Phi-3-mini-4k-instruct"
    
    # Lấy phiên bản mới nhất của mô hình từ đăng ký Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # In tên mô hình, phiên bản và id
    # Thông tin này hữu ích cho việc theo dõi và gỡ lỗi
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Tạo compute để sử dụng với công việc

Công việc tinh chỉnh CHỈ hoạt động với compute GPU. Kích thước compute phụ thuộc vào độ lớn của mô hình và trong nhiều trường hợp rất khó xác định compute phù hợp cho công việc. Trong ô này, chúng tôi hướng dẫn người dùng chọn compute phù hợp cho công việc.

> [!NOTE]
> Các compute dưới đây hoạt động với cấu hình tối ưu nhất. Bất kỳ thay đổi nào về cấu hình có thể dẫn đến lỗi Cuda Out Of Memory. Trong trường hợp đó, hãy thử nâng cấp compute lên kích thước lớn hơn.

> [!NOTE]
> Khi chọn compute_cluster_size bên dưới, hãy đảm bảo compute đó có sẵn trong nhóm tài nguyên của bạn. Nếu compute cụ thể không có sẵn, bạn có thể gửi yêu cầu để được truy cập tài nguyên compute.

### Kiểm tra hỗ trợ tinh chỉnh mô hình

1. Script Python này tương tác với mô hình Azure Machine Learning (Azure ML). Dưới đây là phần giải thích:

    - Nó nhập mô-đun ast, cung cấp các hàm để xử lý cây cú pháp trừu tượng Python.

    - Nó kiểm tra xem đối tượng foundation_model (biểu diễn một mô hình trong Azure ML) có thẻ (tag) tên finetune_compute_allow_list hay không. Các thẻ trong Azure ML là cặp khóa-giá trị mà bạn có thể tạo và dùng để lọc hoặc sắp xếp mô hình.

    - Nếu thẻ finetune_compute_allow_list tồn tại, nó sử dụng ast.literal_eval để phân tích an toàn giá trị của thẻ (một chuỗi) thành danh sách Python. Danh sách này được gán cho biến computes_allow_list. Sau đó in ra thông báo yêu cầu tạo một compute từ danh sách đó.

    - Nếu thẻ finetune_compute_allow_list không có, nó đặt computes_allow_list thành None và in ra thông báo cho biết thẻ này không nằm trong các thẻ của mô hình.

    - Tóm lại, script này kiểm tra một thẻ cụ thể trong metadata của mô hình, chuyển giá trị thẻ sang danh sách nếu có, và cung cấp phản hồi cho người dùng.

    ```python
    # Nhập mô-đun ast, cung cấp các hàm để xử lý cây cú pháp trừu tượng của Python
    import ast
    
    # Kiểm tra xem thẻ 'finetune_compute_allow_list' có trong các thẻ của mô hình hay không
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Nếu thẻ có mặt, sử dụng ast.literal_eval để phân tích an toàn giá trị của thẻ (một chuỗi) thành danh sách Python
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # chuyển chuỗi thành danh sách python
        # In thông báo cho biết rằng một compute nên được tạo từ danh sách
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Nếu thẻ không có mặt, đặt computes_allow_list là None
        computes_allow_list = None
        # In thông báo cho biết thẻ 'finetune_compute_allow_list' không phải là một phần của các thẻ của mô hình
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Kiểm tra Compute Instance

1. Script Python này tương tác với dịch vụ Azure Machine Learning (Azure ML) và thực hiện một số kiểm tra trên một thể hiện compute. Dưới đây là phần giải thích:

    - Nó cố lấy thể hiện compute có tên lưu trong compute_cluster từ workspace Azure ML. Nếu trạng thái provisioning của compute đó là "failed", nó sẽ ném ra ValueError.

    - Nó kiểm tra nếu computes_allow_list không phải None. Nếu đúng, nó chuyển tất cả kích thước compute trong danh sách sang chữ thường và kiểm tra xem kích thước của compute hiện tại có trong danh sách hay không. Nếu không có, ném ra ValueError.

    - Nếu computes_allow_list là None, nó kiểm tra xem kích thước compute có trong danh sách kích thước GPU VM không được hỗ trợ hay không. Nếu có, ném ra ValueError.

    - Nó lấy danh sách tất cả kích thước compute có trong workspace. Sau đó duyệt qua danh sách, với mỗi kích thước, kiểm tra xem tên có trùng với kích thước compute hiện tại không. Nếu có, lấy số lượng GPU của kích thước đó và đặt gpu_count_found thành True.

    - Nếu gpu_count_found là True, in ra số lượng GPU trong compute. Nếu False, ném ra ValueError.

    - Tóm lại, script này thực hiện một số kiểm tra trên compute trong workspace Azure ML, bao gồm kiểm tra trạng thái provisioning, kích thước compute so với danh sách cho phép hoặc từ chối, và số lượng GPU.

    ```python
    # In ra thông điệp ngoại lệ
    print(e)
    # Ném ValueError nếu kích thước compute không có trong workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Lấy compute instance từ workspace Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Kiểm tra trạng thái cung cấp của compute instance có phải là "failed" hay không
    if compute.provisioning_state.lower() == "failed":
        # Ném ValueError nếu trạng thái cung cấp là "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Kiểm tra nếu computes_allow_list không phải là None
    if computes_allow_list is not None:
        # Chuyển tất cả kích thước compute trong computes_allow_list thành chữ thường
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Kiểm tra xem kích thước của compute instance có trong computes_allow_list_lower_case không
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Ném ValueError nếu kích thước của compute instance không có trong computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Định nghĩa danh sách các kích thước VM GPU không được hỗ trợ
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Kiểm tra xem kích thước của compute instance có trong unsupported_gpu_vm_list không
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Ném ValueError nếu kích thước của compute instance có trong unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Khởi tạo cờ để kiểm tra số lượng GPU trong compute instance đã được tìm thấy chưa
    gpu_count_found = False
    # Lấy danh sách tất cả các kích thước compute có sẵn trong workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Lặp qua danh sách các kích thước compute có sẵn
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Kiểm tra nếu tên kích thước compute bằng kích thước của compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # Nếu đúng, lấy số lượng GPU cho kích thước compute đó và đặt gpu_count_found thành True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Nếu gpu_count_found là True, in ra số lượng GPU trong compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Nếu gpu_count_found là False, ném ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Chọn tập dữ liệu để tinh chỉnh mô hình

1. Chúng ta dùng tập dữ liệu ultrachat_200k. Tập dữ liệu có bốn phần, phù hợp cho Supervised fine-tuning (sft).
Generation ranking (gen). Số mẫu cho mỗi phần được thể hiện như sau:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Các ô lệnh tiếp theo trình bày chuẩn bị dữ liệu cơ bản cho tinh chỉnh:

### Trực quan hóa một số dòng dữ liệu

Chúng ta muốn mẫu này chạy nhanh, nên lưu các file train_sft, test_sft chỉ chứa 5% số dòng đã được cắt gọn. Điều này nghĩa là mô hình tinh chỉnh sẽ có độ chính xác thấp hơn, vì vậy không nên dùng trong thực tế.
download-dataset.py được dùng để tải tập dữ liệu ultrachat_200k và chuyển đổi tập dữ liệu sang định dạng có thể dùng được trong pipeline tinh chỉnh. Do tập dữ liệu lớn, chúng ta chỉ có một phần dữ liệu ở đây.

1. Chạy đoạn script dưới đây chỉ tải 5% dữ liệu. Bạn có thể tăng lên bằng cách thay đổi tham số dataset_split_pc thành phần trăm mong muốn.

> [!NOTE]
> Một số mô hình ngôn ngữ có mã ngôn ngữ khác nhau và do đó tên cột trong tập dữ liệu cũng nên tương ứng.

1. Dưới đây là ví dụ dữ liệu cần có dạng như thế nào
Tập dữ liệu chat-completion được lưu ở định dạng parquet với mỗi mục có cấu trúc như sau:

    - Đây là tài liệu JSON (JavaScript Object Notation), một định dạng trao đổi dữ liệu phổ biến. Nó không phải mã thực thi mà là cách lưu và truyền dữ liệu. Dưới đây là phân tích cấu trúc:

    - "prompt": Khoá này chứa giá trị chuỗi đại diện cho nhiệm vụ hoặc câu hỏi được đặt ra cho trợ lý AI.

    - "messages": Khoá này chứa mảng các đối tượng. Mỗi đối tượng biểu diễn một tin nhắn trong cuộc hội thoại giữa người dùng và trợ lý AI. Mỗi đối tượng tin nhắn có hai khoá:

    - "content": chứa giá trị chuỗi biểu diễn nội dung tin nhắn.
    - "role": chứa giá trị chuỗi biểu thị vai trò của thực thể gửi tin nhắn, có thể là "user" hoặc "assistant".
    - "prompt_id": khoá chứa giá trị chuỗi đại diện cho định danh duy nhất của prompt.

1. Trong tài liệu JSON cụ thể này, một cuộc hội thoại được mô tả, trong đó người dùng yêu cầu trợ lý AI tạo ra nhân vật chính cho câu chuyện dystopian. Trợ lý trả lời, rồi người dùng lại hỏi thêm chi tiết. Trợ lý đồng ý cung cấp thêm chi tiết. Toàn bộ cuộc trò chuyện liên kết với một id prompt cụ thể.

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

1. Script Python này được dùng để tải tập dữ liệu bằng cách gọi script trợ giúp tên download-dataset.py. Dưới đây là phân tích:

    - Nó nhập mô-đun os, cung cấp cách sử dụng các chức năng phụ thuộc hệ điều hành.

    - Nó dùng hàm os.system để chạy script download-dataset.py trong shell với các tham số dòng lệnh cụ thể. Tham số chỉ định tập dữ liệu cần tải (HuggingFaceH4/ultrachat_200k), thư mục tải về (ultrachat_200k_dataset), và tỉ lệ phần trăm tập dữ liệu được phân tách (5). Hàm os.system trả về trạng thái thoát của lệnh đã thực thi; trạng thái này được lưu vào biến exit_status.

    - Nó kiểm tra nếu exit_status khác 0. Trong hệ điều hành kiểu Unix, trạng thái 0 nghĩa lệnh thành công, các số khác nghĩa lỗi. Nếu khác 0, nó ném ra Exception với thông báo lỗi khi tải tập dữ liệu.

    - Tóm lại, script này thực thi lệnh tải tập dữ liệu thông qua script trợ giúp, và ném lỗi nếu lệnh thất bại.

    ```python
    # Nhập module os, cung cấp cách sử dụng các chức năng phụ thuộc vào hệ điều hành
    import os
    
    # Sử dụng hàm os.system để chạy script download-dataset.py trong shell với các đối số dòng lệnh cụ thể
    # Các đối số chỉ định dataset cần tải về (HuggingFaceH4/ultrachat_200k), thư mục để tải về (ultrachat_200k_dataset), và tỷ lệ phần trăm của dataset để chia (5)
    # Hàm os.system trả về trạng thái thoát của lệnh đã thực thi; trạng thái này được lưu trong biến exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Kiểm tra nếu exit_status không bằng 0
    # Trong các hệ điều hành giống Unix, trạng thái thoát 0 thường chỉ ra rằng lệnh đã thành công, trong khi bất kỳ số nào khác đều chỉ ra lỗi
    # Nếu exit_status không bằng 0, tạo ra Exception với thông báo chỉ ra có lỗi khi tải dataset về
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Tải dữ liệu vào DataFrame

1. Script Python này tải một tập tin JSON Lines vào pandas DataFrame và hiển thị 5 dòng đầu tiên. Dưới đây là phần giải thích:

    - Nó nhập thư viện pandas, thư viện mạnh để xử lý và phân tích dữ liệu.

    - Nó đặt giới hạn chiều rộng tối đa của cột cho pandas ở 0. Điều này nghĩa là toàn bộ văn bản trong mỗi cột sẽ được hiển thị đầy đủ mà không bị rút gọn khi DataFrame được in ra.
    - Nó sử dụng hàm pd.read_json để tải file train_sft.jsonl từ thư mục ultrachat_200k_dataset vào một DataFrame. Tham số lines=True chỉ ra rằng file ở định dạng JSON Lines, nơi mỗi dòng là một đối tượng JSON riêng biệt.

    - Nó sử dụng phương thức head để hiển thị 5 dòng đầu tiên của DataFrame. Nếu DataFrame có ít hơn 5 dòng, nó sẽ hiển thị tất cả chúng.

    - Tóm lại, script này đang tải một file JSON Lines vào DataFrame và hiển thị 5 dòng đầu tiên với toàn bộ văn bản của các cột.
    
    ```python
    # Nhập thư viện pandas, là một thư viện mạnh mẽ để thao tác và phân tích dữ liệu
    import pandas as pd
    
    # Đặt độ rộng cột tối đa cho các tùy chọn hiển thị của pandas thành 0
    # Điều này có nghĩa là toàn bộ văn bản của mỗi cột sẽ được hiển thị mà không bị rút gọn khi DataFrame được in ra
    pd.set_option("display.max_colwidth", 0)
    
    # Sử dụng hàm pd.read_json để tải tệp train_sft.jsonl từ thư mục ultrachat_200k_dataset vào một DataFrame
    # Tham số lines=True cho biết tệp ở định dạng JSON Lines, trong đó mỗi dòng là một đối tượng JSON riêng biệt
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Sử dụng phương thức head để hiển thị 5 hàng đầu tiên của DataFrame
    # Nếu DataFrame có ít hơn 5 hàng, nó sẽ hiển thị tất cả các hàng đó
    df.head()
    ```

## 5. Gửi công việc tinh chỉnh sử dụng mô hình và dữ liệu làm đầu vào

Tạo công việc sử dụng thành phần pipeline chat-completion. Tìm hiểu thêm về tất cả các tham số được hỗ trợ cho việc tinh chỉnh.

### Định nghĩa các tham số tinh chỉnh

1. Các tham số tinh chỉnh có thể được nhóm thành 2 loại - tham số huấn luyện, tham số tối ưu hóa

1. Tham số huấn luyện định nghĩa các khía cạnh huấn luyện như -

    - Bộ tối ưu, bộ lập lịch sẽ sử dụng
    - Thước đo để tối ưu hóa việc tinh chỉnh
    - Số bước huấn luyện và kích thước lô, v.v...
    - Tham số tối ưu hóa giúp tối ưu bộ nhớ GPU và sử dụng hiệu quả tài nguyên tính toán.

1. Dưới đây là một vài tham số thuộc nhóm này. Tham số tối ưu hóa khác nhau cho từng mô hình và được đóng gói cùng với mô hình để xử lý các biến thể này.

    - Kích hoạt deepspeed và LoRA
    - Kích hoạt huấn luyện độ chính xác hỗn hợp
    - Kích hoạt huấn luyện đa nút

> [!NOTE]
> Huấn luyện có giám sát có thể dẫn đến mất cân chỉnh hoặc quên kiến thức thảm họa. Chúng tôi khuyên bạn nên kiểm tra vấn đề này và chạy giai đoạn cân chỉnh sau khi tinh chỉnh.

### Tham số Tinh chỉnh

1. Script Python này thiết lập các tham số cho việc tinh chỉnh mô hình máy học. Đây là phân tích những gì nó làm:

    - Nó thiết lập các tham số huấn luyện mặc định như số epoch huấn luyện, kích thước lô cho huấn luyện và đánh giá, tốc độ học, và loại bộ lập lịch tốc độ học.

    - Nó thiết lập các tham số tối ưu mặc định như liệu có áp dụng Layer-wise Relevance Propagation (LoRa) và DeepSpeed, và giai đoạn DeepSpeed.

    - Nó kết hợp các tham số huấn luyện và tối ưu vào một dictionary duy nhất gọi là finetune_parameters.

    - Nó kiểm tra xem foundation_model có bất kỳ tham số mặc định riêng theo mô hình nào không. Nếu có, nó in thông báo cảnh báo và cập nhật dictionary finetune_parameters với các tham số mặc định theo mô hình đó. Hàm ast.literal_eval được dùng để chuyển đổi các tham số mặc định theo mô hình từ chuỗi sang dictionary Python.

    - Nó in ra bộ tham số tinh chỉnh cuối cùng sẽ được sử dụng cho lần chạy.

    - Tóm lại, script này thiết lập và hiển thị các tham số tinh chỉnh mô hình máy học, với khả năng ghi đè các tham số mặc định bằng các tham số riêng theo mô hình.

    ```python
    # Thiết lập các tham số huấn luyện mặc định như số epoch huấn luyện, kích thước batch cho huấn luyện và đánh giá, tốc độ học, và loại bộ lập lịch tốc độ học
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Thiết lập các tham số tối ưu hóa mặc định như có áp dụng Layer-wise Relevance Propagation (LoRa) và DeepSpeed hay không, và cấp độ DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Kết hợp các tham số huấn luyện và tối ưu hóa thành một từ điển duy nhất gọi là finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Kiểm tra xem foundation_model có bất kỳ tham số mặc định cụ thể cho mô hình nào không
    # Nếu có, in thông báo cảnh báo và cập nhật từ điển finetune_parameters với các tham số mặc định cụ thể cho mô hình đó
    # Hàm ast.literal_eval được sử dụng để chuyển đổi các tham số mặc định cụ thể cho mô hình từ chuỗi thành từ điển Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # chuyển đổi chuỗi thành từ điển python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # In tập hợp cuối cùng các tham số tinh chỉnh sẽ được sử dụng cho lần chạy
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline Huấn luyện

1. Script Python này định nghĩa một hàm để tạo tên hiển thị cho pipeline huấn luyện máy học, rồi gọi hàm đó để tạo và in tên hiển thị. Đây là phân tích những gì nó làm:

1. Hàm get_pipeline_display_name được định nghĩa. Hàm này tạo tên hiển thị dựa trên nhiều tham số liên quan đến pipeline huấn luyện.

1. Bên trong hàm, nó tính kích thước lô tổng bằng cách nhân kích thước lô trên mỗi thiết bị, số bước tích lũy gradient, số GPU trên mỗi node, và số node dùng cho việc tinh chỉnh.

1. Nó lấy các tham số khác như loại bộ lập lịch tốc độ học, liệu DeepSpeed có được áp dụng, giai đoạn DeepSpeed, liệu Layer-wise Relevance Propagation (LoRa) có được áp dụng, giới hạn số checkpoint mô hình được giữ lại, và độ dài tối đa chuỗi.

1. Nó xây dựng một chuỗi gồm tất cả các tham số này, ngăn cách bằng dấu gạch ngang. Nếu áp dụng DeepSpeed hoặc LoRa, chuỗi sẽ bao gồm "ds" kèm theo giai đoạn DeepSpeed hoặc "lora". Nếu không, nó sẽ gồm "nods" hoặc "nolora".

1. Hàm trả về chuỗi này, làm tên hiển thị cho pipeline huấn luyện.

1. Sau khi hàm được định nghĩa, nó được gọi để tạo tên hiển thị, rồi tên này được in ra.

1. Tóm lại, script này tạo tên hiển thị cho pipeline huấn luyện máy học dựa trên nhiều tham số, rồi in tên hiển thị đó.

    ```python
    # Định nghĩa một hàm để tạo tên hiển thị cho quy trình đào tạo
    def get_pipeline_display_name():
        # Tính tổng kích thước batch bằng cách nhân kích thước batch trên mỗi thiết bị, số bước tích lũy gradient, số GPU trên mỗi node, và số node được sử dụng để fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Lấy loại lịch trình tốc độ học
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Lấy xem có áp dụng DeepSpeed hay không
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Lấy giai đoạn DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Nếu áp dụng DeepSpeed, bao gồm "ds" theo sau là giai đoạn DeepSpeed trong tên hiển thị; nếu không, bao gồm "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Lấy xem có áp dụng Layer-wise Relevance Propagation (LoRa) hay không
        lora = finetune_parameters.get("apply_lora", "false")
        # Nếu áp dụng LoRa, bao gồm "lora" trong tên hiển thị; nếu không, bao gồm "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Lấy giới hạn số lượng checkpoint của mô hình cần giữ lại
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Lấy độ dài chuỗi tối đa
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Xây dựng tên hiển thị bằng cách nối tất cả các tham số này, cách nhau bởi dấu gạch ngang
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
    
    # Gọi hàm để tạo tên hiển thị
    pipeline_display_name = get_pipeline_display_name()
    # In tên hiển thị ra màn hình
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Cấu hình Pipeline

Script Python này định nghĩa và cấu hình một pipeline máy học sử dụng Azure Machine Learning SDK. Đây là phân tích những gì nó làm:

1. Nó nhập các module cần thiết từ Azure AI ML SDK.

1. Nó lấy một thành phần pipeline tên là "chat_completion_pipeline" từ registry.

1. Nó định nghĩa một công việc pipeline sử dụng decorator `@pipeline` và hàm `create_pipeline`. Tên pipeline được đặt là `pipeline_display_name`.

1. Bên trong hàm `create_pipeline`, nó khởi tạo thành phần pipeline lấy được với nhiều tham số, bao gồm đường dẫn mô hình, các cụm tính toán cho các giai đoạn khác nhau, các phần dữ liệu huấn luyện và kiểm thử, số lượng GPU dùng cho tinh chỉnh, và các tham số tinh chỉnh khác.

1. Nó ánh xạ đầu ra của công việc tinh chỉnh vào đầu ra của công việc pipeline. Việc này để mô hình tinh chỉnh dễ dàng được đăng ký, điều cần thiết để triển khai mô hình lên điểm cuối online hoặc batch.

1. Nó tạo đối tượng pipeline bằng cách gọi hàm `create_pipeline`.

1. Nó đặt thiết lập `force_rerun` của pipeline thành `True`, nghĩa là không dùng kết quả cache từ các công việc trước đó.

1. Nó đặt thiết lập `continue_on_step_failure` của pipeline thành `False`, nghĩa là pipeline sẽ dừng nếu bất kỳ bước nào thất bại.

1. Tóm lại, script này định nghĩa và cấu hình pipeline máy học cho nhiệm vụ hoàn thành chat sử dụng Azure Machine Learning SDK.

    ```python
    # Nhập các mô-đun cần thiết từ Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Lấy thành phần pipeline có tên "chat_completion_pipeline" từ registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Định nghĩa công việc pipeline sử dụng decorator @pipeline và hàm create_pipeline
    # Tên của pipeline được đặt thành pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Khởi tạo thành phần pipeline đã lấy với các tham số khác nhau
        # Bao gồm đường dẫn mô hình, cụm tính toán cho các giai đoạn khác nhau, phân chia bộ dữ liệu cho đào tạo và kiểm tra, số lượng GPU sử dụng để tinh chỉnh, và các tham số tinh chỉnh khác
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Ánh xạ các phân chia bộ dữ liệu thành các tham số
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Cài đặt huấn luyện
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Đặt bằng số lượng GPU có sẵn trong cụm tính toán
            **finetune_parameters
        )
        return {
            # Ánh xạ đầu ra của công việc tinh chỉnh sang đầu ra của công việc pipeline
            # Việc này giúp chúng ta dễ dàng đăng ký mô hình đã được tinh chỉnh
            # Việc đăng ký mô hình là cần thiết để triển khai mô hình đến điểm cuối trực tuyến hoặc batch
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Tạo một thể hiện của pipeline bằng cách gọi hàm create_pipeline
    pipeline_object = create_pipeline()
    
    # Không sử dụng kết quả lưu trong bộ nhớ đệm từ các công việc trước
    pipeline_object.settings.force_rerun = True
    
    # Đặt tiếp tục khi bước thất bại là False
    # Điều này có nghĩa là pipeline sẽ dừng nếu bất kỳ bước nào bị lỗi
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Gửi công việc

1. Script Python này gửi một công việc pipeline máy học đến workspace Azure Machine Learning rồi chờ công việc hoàn thành. Đây là phân tích những gì nó làm:

    - Nó gọi phương thức create_or_update của đối tượng jobs trong workspace_ml_client để gửi công việc pipeline. Pipeline chạy được chỉ định bởi pipeline_object, và phiên thí nghiệm chạy công việc được chỉ định bởi experiment_name.

    - Sau đó, nó gọi phương thức stream của đối tượng jobs trong workspace_ml_client để chờ công việc pipeline hoàn thành. Công việc chờ được chỉ định bởi thuộc tính name của đối tượng pipeline_job.

    - Tóm lại, script này gửi công việc pipeline máy học đến workspace Azure Machine Learning, rồi chờ công việc hoàn thành.

    ```python
    # Gửi công việc pipeline đến workspace Azure Machine Learning
    # Pipeline để chạy được xác định bởi pipeline_object
    # Thí nghiệm mà công việc được chạy thuộc về được xác định bởi experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Chờ công việc pipeline hoàn thành
    # Công việc cần chờ được xác định bởi thuộc tính name của đối tượng pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Đăng ký mô hình đã tinh chỉnh với workspace

Chúng ta sẽ đăng ký mô hình xuất ra từ kết quả công việc tinh chỉnh. Việc này sẽ theo dõi dòng dữ liệu giữa mô hình tinh chỉnh và công việc tinh chỉnh. Công việc tinh chỉnh cũng theo dõi dòng dữ liệu với mô hình nền tảng, dữ liệu và mã huấn luyện.

### Đăng ký mô hình ML

1. Script Python này đăng ký một mô hình máy học được huấn luyện trong pipeline Azure Machine Learning. Đây là phân tích những gì nó làm:

    - Nó nhập các module cần thiết từ Azure AI ML SDK.

    - Nó kiểm tra xem đầu ra trained_model có sẵn từ công việc pipeline không bằng cách gọi phương thức get của đối tượng jobs trong workspace_ml_client và truy cập thuộc tính outputs.

    - Nó xây dựng đường dẫn đến mô hình huấn luyện bằng cách định dạng chuỗi với tên công việc pipeline và tên đầu ra ("trained_model").

    - Nó định nghĩa tên cho mô hình đã tinh chỉnh bằng cách thêm "-ultrachat-200k" vào tên mô hình gốc và thay thế các dấu gạch chéo bằng dấu gạch ngang.

    - Nó chuẩn bị đăng ký mô hình bằng cách tạo một đối tượng Model với nhiều tham số, bao gồm đường dẫn đến mô hình, loại mô hình (mô hình MLflow), tên và phiên bản mô hình, và mô tả mô hình.

    - Nó đăng ký mô hình bằng cách gọi phương thức create_or_update của đối tượng models trong workspace_ml_client với đối tượng Model làm tham số.

    - Nó in ra mô hình đã đăng ký.

1. Tóm lại, script này đăng ký một mô hình máy học được huấn luyện trong pipeline Azure Machine Learning.
    
    ```python
    # Nhập các mô-đun cần thiết từ Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Kiểm tra xem đầu ra `trained_model` có sẵn từ pipeline job hay không
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Tạo đường dẫn đến mô hình đã huấn luyện bằng cách định dạng chuỗi với tên của pipeline job và tên của đầu ra ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Định nghĩa tên cho mô hình đã tinh chỉnh bằng cách thêm "-ultrachat-200k" vào tên mô hình gốc và thay thế tất cả dấu gạch chéo bằng dấu gạch ngang
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Chuẩn bị đăng ký mô hình bằng cách tạo một đối tượng Model với nhiều tham số khác nhau
    # Bao gồm đường dẫn đến mô hình, loại mô hình (mô hình MLflow), tên và phiên bản của mô hình, cũng như mô tả về mô hình
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Sử dụng timestamp làm phiên bản để tránh xung đột phiên bản
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Đăng ký mô hình bằng cách gọi phương thức create_or_update của đối tượng models trong workspace_ml_client với đối tượng Model làm đối số
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # In mô hình đã được đăng ký
    print("registered model: \n", registered_model)
    ```

## 7. Triển khai mô hình đã tinh chỉnh lên điểm cuối trực tuyến

Điểm cuối trực tuyến cung cấp API REST bền vững có thể tích hợp với các ứng dụng cần sử dụng mô hình.

### Quản lý Điểm cuối

1. Script Python này tạo một điểm cuối trực tuyến được quản lý trong Azure Machine Learning cho một mô hình đã đăng ký. Đây là phân tích những gì nó làm:

    - Nó nhập các module cần thiết từ Azure AI ML SDK.

    - Nó định nghĩa tên duy nhất cho điểm cuối trực tuyến bằng cách thêm dấu thời gian vào chuỗi "ultrachat-completion-".

    - Nó chuẩn bị tạo điểm cuối trực tuyến bằng cách tạo một đối tượng ManagedOnlineEndpoint với các tham số như tên điểm cuối, mô tả điểm cuối, và chế độ xác thực ("key").

    - Nó tạo điểm cuối trực tuyến bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng ManagedOnlineEndpoint làm tham số. Sau đó chờ thao tác tạo hoàn tất bằng phương thức wait.

1. Tóm lại, script này tạo một điểm cuối trực tuyến được quản lý trong Azure Machine Learning cho một mô hình đã đăng ký.

    ```python
    # Nhập các mô-đun cần thiết từ Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Định nghĩa một tên duy nhất cho điểm cuối trực tuyến bằng cách thêm dấu thời gian vào chuỗi "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Chuẩn bị tạo điểm cuối trực tuyến bằng cách tạo một đối tượng ManagedOnlineEndpoint với các tham số khác nhau
    # Bao gồm tên điểm cuối, mô tả điểm cuối và chế độ xác thực ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Tạo điểm cuối trực tuyến bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng ManagedOnlineEndpoint làm đối số
    # Sau đó chờ thao tác tạo hoàn thành bằng cách gọi phương thức wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Bạn có thể tìm danh sách SKU được hỗ trợ để triển khai tại đây - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Triển khai mô hình ML

1. Script Python này triển khai một mô hình máy học đã đăng ký đến một điểm cuối trực tuyến được quản lý trong Azure Machine Learning. Đây là phân tích những gì nó làm:

    - Nó nhập module ast, cung cấp các hàm xử lý cấu trúc cú pháp trừu tượng (AST) của Python.

    - Nó thiết lập loại máy chủ (instance type) cho việc triển khai là "Standard_NC6s_v3".

    - Nó kiểm tra nếu tag inference_compute_allow_list có trong mô hình nền tảng. Nếu có, nó chuyển giá trị tag từ chuỗi sang danh sách Python và gán vào inference_computes_allow_list. Nếu không, nó đặt inference_computes_allow_list là None.

    - Nó kiểm tra xem loại máy chủ chỉ định có trong danh sách cho phép không. Nếu không có, nó in thông báo yêu cầu người dùng chọn loại máy chủ từ danh sách cho phép.

    - Nó chuẩn bị tạo triển khai bằng cách tạo một đối tượng ManagedOnlineDeployment với các tham số như tên triển khai, tên điểm cuối, ID mô hình, loại máy chủ và số lượng, thiết lập kiểm tra liveness, và các thiết lập yêu cầu.

    - Nó tạo triển khai bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng ManagedOnlineDeployment làm tham số. Sau đó chờ thao tác tạo hoàn tất bằng phương thức wait.

    - Nó đặt lưu lượng của điểm cuối để chuyển 100% lưu lượng đến triển khai "demo".

    - Nó cập nhật điểm cuối bằng cách gọi phương thức begin_create_or_update của workspace_ml_client với đối tượng endpoint làm tham số. Sau đó chờ thao tác cập nhật hoàn tất bằng phương thức result.

1. Tóm lại, script này triển khai một mô hình máy học đã đăng ký đến điểm cuối trực tuyến được quản lý trong Azure Machine Learning.

    ```python
    # Nhập mô-đun ast, cung cấp các hàm để xử lý cây ngữ pháp trừu tượng của Python
    import ast
    
    # Đặt loại phiên bản cho triển khai
    instance_type = "Standard_NC6s_v3"
    
    # Kiểm tra xem thẻ `inference_compute_allow_list` có trong mô hình nền tảng hay không
    if "inference_compute_allow_list" in foundation_model.tags:
        # Nếu có, chuyển đổi giá trị thẻ từ chuỗi sang danh sách Python và gán nó cho `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Nếu không, đặt `inference_computes_allow_list` thành `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Kiểm tra xem loại phiên bản được chỉ định có trong danh sách cho phép hay không
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Chuẩn bị tạo triển khai bằng cách tạo một đối tượng `ManagedOnlineDeployment` với các tham số khác nhau
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Tạo triển khai bằng cách gọi phương thức `begin_create_or_update` của `workspace_ml_client` với đối tượng `ManagedOnlineDeployment` làm đối số
    # Sau đó chờ cho thao tác tạo hoàn tất bằng cách gọi phương thức `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Đặt lưu lượng của điểm cuối để chuyển 100% lưu lượng đến triển khai "demo"
    endpoint.traffic = {"demo": 100}
    
    # Cập nhật điểm cuối bằng cách gọi phương thức `begin_create_or_update` của `workspace_ml_client` với đối tượng `endpoint` làm đối số
    # Sau đó chờ cho thao tác cập nhật hoàn tất bằng cách gọi phương thức `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Kiểm tra điểm cuối với dữ liệu mẫu

Chúng ta sẽ lấy một số dữ liệu mẫu từ tập kiểm thử và gửi đến điểm cuối trực tuyến để dự đoán. Sau đó sẽ hiển thị nhãn dự đoán cùng với nhãn thật.

### Đọc kết quả

1. Script Python này đọc một file JSON Lines vào DataFrame pandas, lấy mẫu ngẫu nhiên, và đặt lại chỉ số. Đây là phân tích những gì nó làm:

    - Nó đọc file ./ultrachat_200k_dataset/test_gen.jsonl vào một DataFrame pandas. Hàm read_json được dùng với tham số lines=True vì file ở định dạng JSON Lines, mỗi dòng là một đối tượng JSON riêng.

    - Nó lấy một mẫu ngẫu nhiên 1 dòng từ DataFrame. Hàm sample dùng với tham số n=1 để chỉ định số dòng ngẫu nhiên cần lấy.

    - Nó đặt lại chỉ số của DataFrame. Hàm reset_index dùng với tham số drop=True để loại bỏ chỉ mục cũ và thay bằng chỉ số mặc định là số nguyên.

    - Nó hiển thị 2 dòng đầu tiên của DataFrame dùng hàm head với đối số 2. Tuy nhiên, do DataFrame chỉ có một dòng sau bước lấy mẫu, nên sẽ chỉ hiển thị một dòng đó.

1. Tóm lại, script này đọc một file JSON Lines vào một DataFrame pandas, lấy mẫu ngẫu nhiên 1 dòng, đặt lại chỉ số, và hiển thị dòng đầu tiên.
    
    ```python
    # Nhập thư viện pandas
    import pandas as pd
    
    # Đọc tệp JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' vào DataFrame của pandas
    # Đối số 'lines=True' chỉ ra rằng tệp ở định dạng JSON Lines, trong đó mỗi dòng là một đối tượng JSON riêng biệt
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Lấy một mẫu ngẫu nhiên 1 dòng từ DataFrame
    # Đối số 'n=1' chỉ định số dòng ngẫu nhiên cần chọn
    test_df = test_df.sample(n=1)
    
    # Đặt lại chỉ mục của DataFrame
    # Đối số 'drop=True' chỉ ra rằng chỉ mục gốc nên bị loại bỏ và thay thế bằng chỉ mục mới với giá trị số nguyên mặc định
    # Đối số 'inplace=True' chỉ ra rằng DataFrame nên được sửa đổi tại chỗ (không tạo đối tượng mới)
    test_df.reset_index(drop=True, inplace=True)
    
    # Hiển thị 2 dòng đầu tiên của DataFrame
    # Tuy nhiên, vì DataFrame chỉ chứa một dòng sau khi lấy mẫu, điều này sẽ chỉ hiển thị một dòng đó thôi
    test_df.head(2)
    ```

### Tạo đối tượng JSON

1. Script Python này tạo một đối tượng JSON với các tham số cụ thể và lưu nó vào file. Đây là phân tích những gì nó làm:

    - Nó nhập module json, cung cấp các hàm xử lý dữ liệu JSON.
    - Nó tạo một dictionary parameters với các khóa và giá trị đại diện cho các tham số cho một mô hình học máy. Các khóa là "temperature", "top_p", "do_sample", và "max_new_tokens", và các giá trị tương ứng là 0.6, 0.9, True, và 200.

    - Nó tạo một dictionary khác test_json với hai khóa: "input_data" và "params". Giá trị của "input_data" là một dictionary khác với các khóa "input_string" và "parameters". Giá trị của "input_string" là một danh sách chứa tin nhắn đầu tiên từ DataFrame test_df. Giá trị của "parameters" là dictionary parameters được tạo ở trên. Giá trị của "params" là một dictionary rỗng.

    - Nó mở một file có tên sample_score.json
    
    ```python
    # Nhập mô-đun json, cung cấp các hàm để làm việc với dữ liệu JSON
    import json
    
    # Tạo một từ điển `parameters` với các khóa và giá trị đại diện cho các tham số của mô hình học máy
    # Các khóa là "temperature", "top_p", "do_sample", và "max_new_tokens", với các giá trị tương ứng lần lượt là 0.6, 0.9, True, và 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Tạo một từ điển khác `test_json` với hai khóa: "input_data" và "params"
    # Giá trị của "input_data" là một từ điển khác với các khóa "input_string" và "parameters"
    # Giá trị của "input_string" là một danh sách chứa tin nhắn đầu tiên từ DataFrame `test_df`
    # Giá trị của "parameters" là từ điển `parameters` được tạo trước đó
    # Giá trị của "params" là một từ điển rỗng
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Mở một tệp có tên `sample_score.json` trong thư mục `./ultrachat_200k_dataset` ở chế độ ghi
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Ghi từ điển `test_json` vào tệp theo định dạng JSON sử dụng hàm `json.dump`
        json.dump(test_json, f)
    ```

### Gọi Endpoint

1. Script Python này đang gọi một endpoint trực tuyến trong Azure Machine Learning để chấm điểm một file JSON. Đây là phân tích các bước nó thực hiện:

    - Nó gọi phương thức invoke của online_endpoints thuộc tính của đối tượng workspace_ml_client. Phương thức này được sử dụng để gửi một yêu cầu tới endpoint trực tuyến và nhận phản hồi.

    - Nó chỉ định tên của endpoint và bản triển khai với các đối số endpoint_name và deployment_name. Trong trường hợp này, tên endpoint được lưu trong biến online_endpoint_name và tên triển khai là "demo".

    - Nó chỉ định đường dẫn đến file JSON cần chấm điểm với đối số request_file. Trong trường hợp này, file là ./ultrachat_200k_dataset/sample_score.json.

    - Nó lưu phản hồi từ endpoint vào biến response.

    - Nó in ra phản hồi thô.

1. Tóm lại, script này gọi một endpoint trực tuyến trong Azure Machine Learning để chấm điểm một file JSON và in ra phản hồi.

    ```python
    # Gọi điểm cuối trực tuyến trong Azure Machine Learning để chấm điểm file `sample_score.json`
    # Phương thức `invoke` của thuộc tính `online_endpoints` của đối tượng `workspace_ml_client` được sử dụng để gửi yêu cầu đến điểm cuối trực tuyến và nhận phản hồi
    # Đối số `endpoint_name` chỉ định tên của điểm cuối, được lưu trong biến `online_endpoint_name`
    # Đối số `deployment_name` chỉ định tên của bản triển khai, là "demo"
    # Đối số `request_file` chỉ định đường dẫn đến file JSON cần chấm điểm, đó là `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # In ra phản hồi thô từ điểm cuối
    print("raw response: \n", response, "\n")
    ```

## 9. Xóa endpoint trực tuyến

1. Đừng quên xóa endpoint trực tuyến, nếu không bạn sẽ để đồng hồ tính phí chạy cho tài nguyên tính toán được sử dụng bởi endpoint. Dòng lệnh Python này xóa một endpoint trực tuyến trong Azure Machine Learning. Đây là phân tích các bước nó thực hiện:

    - Nó gọi phương thức begin_delete của online_endpoints thuộc tính của đối tượng workspace_ml_client. Phương thức này được sử dụng để bắt đầu việc xóa một endpoint trực tuyến.

    - Nó chỉ định tên của endpoint sẽ bị xóa với đối số name. Trong trường hợp này, tên endpoint được lưu trong biến online_endpoint_name.

    - Nó gọi phương thức wait để chờ thao tác xóa hoàn tất. Đây là một thao tác chặn, nghĩa là nó sẽ ngăn kịch bản tiếp tục cho đến khi việc xóa hoàn thành.

    - Tóm lại, dòng lệnh này bắt đầu việc xóa một endpoint trực tuyến trong Azure Machine Learning và chờ cho đến khi thao tác hoàn tất.

    ```python
    # Xóa điểm cuối trực tuyến trong Azure Machine Learning
    # Phương thức `begin_delete` của thuộc tính `online_endpoints` của đối tượng `workspace_ml_client` được sử dụng để bắt đầu việc xóa điểm cuối trực tuyến
    # Đối số `name` chỉ định tên của điểm cuối cần xóa, được lưu trong biến `online_endpoint_name`
    # Phương thức `wait` được gọi để chờ cho thao tác xóa hoàn tất. Đây là một thao tác chặn, có nghĩa là nó sẽ ngăn kịch bản tiếp tục cho đến khi việc xóa kết thúc
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa vẫn được coi là nguồn chính xác nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->