<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:27:01+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "vi"
}
-->
# Lab. Tối ưu hóa mô hình AI cho suy luận trên thiết bị

## Giới thiệu

> [!IMPORTANT]  
> Bài lab này yêu cầu **GPU Nvidia A10 hoặc A100** cùng với driver và bộ công cụ CUDA (phiên bản 12+) được cài đặt.

> [!NOTE]  
> Đây là một bài lab **35 phút** giúp bạn làm quen thực tế với các khái niệm cốt lõi về tối ưu hóa mô hình cho suy luận trên thiết bị sử dụng OLIVE.

## Mục tiêu học tập

Sau khi hoàn thành bài lab này, bạn sẽ có thể sử dụng OLIVE để:

- Lượng tử hóa mô hình AI bằng phương pháp lượng tử AWQ.
- Tinh chỉnh mô hình AI cho một nhiệm vụ cụ thể.
- Tạo adapter LoRA (mô hình đã tinh chỉnh) để suy luận hiệu quả trên thiết bị bằng ONNX Runtime.

### Olive là gì

Olive (*O*NNX *live*) là bộ công cụ tối ưu hóa mô hình kèm CLI đi kèm, cho phép bạn triển khai mô hình trên ONNX runtime +++https://onnxruntime.ai+++ với chất lượng và hiệu suất cao.

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.vi.png)

Đầu vào của Olive thường là mô hình PyTorch hoặc Hugging Face, đầu ra là mô hình ONNX đã được tối ưu, chạy trên thiết bị (mục tiêu triển khai) sử dụng ONNX runtime. Olive tối ưu mô hình cho bộ tăng tốc AI của mục tiêu triển khai (NPU, GPU, CPU) do các nhà cung cấp phần cứng như Qualcomm, AMD, Nvidia hoặc Intel cung cấp.

Olive thực thi một *workflow*, là chuỗi các tác vụ tối ưu hóa mô hình riêng biệt gọi là *passes* - ví dụ các passes gồm: nén mô hình, ghi lại đồ thị, lượng tử hóa, tối ưu đồ thị. Mỗi pass có tập tham số có thể điều chỉnh để đạt được các chỉ số tốt nhất, ví dụ độ chính xác và độ trễ, được đánh giá bởi bộ đánh giá tương ứng. Olive sử dụng chiến lược tìm kiếm với thuật toán tìm kiếm để tự động điều chỉnh từng pass một hoặc nhóm passes cùng lúc.

#### Lợi ích của Olive

- **Giảm bớt sự phiền toái và thời gian** thử nghiệm thủ công kiểu thử-và-sai với các kỹ thuật tối ưu hóa đồ thị, nén và lượng tử hóa khác nhau. Đặt ra yêu cầu về chất lượng và hiệu suất, Olive sẽ tự động tìm mô hình tốt nhất cho bạn.
- **Hơn 40 thành phần tối ưu hóa mô hình tích hợp sẵn** bao gồm các kỹ thuật tiên tiến về lượng tử hóa, nén, tối ưu đồ thị và tinh chỉnh.
- **CLI dễ sử dụng** cho các tác vụ tối ưu hóa mô hình phổ biến. Ví dụ: olive quantize, olive auto-opt, olive finetune.
- Tích hợp sẵn đóng gói và triển khai mô hình.
- Hỗ trợ tạo mô hình cho **Multi LoRA serving**.
- Xây dựng workflow bằng YAML/JSON để điều phối các tác vụ tối ưu hóa và triển khai mô hình.
- Tích hợp với **Hugging Face** và **Azure AI**.
- Cơ chế **cache** tích hợp giúp **tiết kiệm chi phí**.

## Hướng dẫn lab

> [!NOTE]  
> Hãy đảm bảo bạn đã tạo Azure AI Hub và Project, đồng thời thiết lập A100 compute theo Lab 1.

### Bước 0: Kết nối với Azure AI Compute

Bạn sẽ kết nối với Azure AI compute qua tính năng remote trong **VS Code**.

1. Mở ứng dụng **VS Code** trên máy tính:
2. Mở **command palette** bằng tổ hợp phím **Shift+Ctrl+P**
3. Trong command palette, tìm kiếm **AzureML - remote: Connect to compute instance in New Window**.
4. Làm theo hướng dẫn trên màn hình để kết nối với Compute. Bạn sẽ chọn Subscription Azure, Resource Group, Project và tên Compute đã tạo trong Lab 1.
5. Khi kết nối thành công với Azure ML Compute node, thông tin sẽ hiển thị ở **góc dưới bên trái của Visual Code** `><Azure ML: Compute Name`

### Bước 1: Clone repo này

Trong VS Code, mở terminal mới với **Ctrl+J** và clone repo này:

Trong terminal bạn sẽ thấy dấu nhắc lệnh

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone the solution

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Bước 2: Mở thư mục trong VS Code

Để mở VS Code trong thư mục liên quan, chạy lệnh sau trong terminal, lệnh này sẽ mở cửa sổ mới:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Ngoài ra, bạn cũng có thể mở thư mục bằng cách chọn **File** > **Open Folder**.

### Bước 3: Cài đặt phụ thuộc

Mở terminal trong VS Code trên Azure AI Compute Instance của bạn (mẹo: **Ctrl+J**) và chạy các lệnh sau để cài đặt các phụ thuộc:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Quá trình cài đặt các phụ thuộc sẽ mất khoảng ~5 phút.

Trong bài lab này bạn sẽ tải xuống và tải lên các mô hình vào Azure AI Model catalog. Để truy cập catalog, bạn cần đăng nhập vào Azure bằng:

```bash
az login
```

> [!NOTE]  
> Khi đăng nhập, bạn sẽ được yêu cầu chọn subscription. Hãy chắc chắn chọn đúng subscription được cung cấp cho bài lab này.

### Bước 4: Thực thi các lệnh Olive

Mở terminal trong VS Code trên Azure AI Compute Instance (mẹo: **Ctrl+J**) và đảm bảo môi trường conda `olive-ai` đã được kích hoạt:

```bash
conda activate olive-ai
```

Tiếp theo, thực thi các lệnh Olive sau trên dòng lệnh.

1. **Kiểm tra dữ liệu:** Trong ví dụ này, bạn sẽ tinh chỉnh mô hình Phi-3.5-Mini để nó chuyên về trả lời các câu hỏi liên quan đến du lịch. Đoạn mã dưới đây hiển thị một vài bản ghi đầu tiên của bộ dữ liệu, ở định dạng JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Lượng tử hóa mô hình:** Trước khi huấn luyện mô hình, bạn sẽ lượng tử hóa với lệnh sau sử dụng kỹ thuật gọi là Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ lượng tử hóa trọng số mô hình dựa trên các kích hoạt được tạo ra trong quá trình suy luận. Điều này có nghĩa quá trình lượng tử hóa tính đến phân bố dữ liệu thực tế trong các kích hoạt, giúp giữ được độ chính xác mô hình tốt hơn so với các phương pháp lượng tử hóa trọng số truyền thống.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Quá trình lượng tử hóa AWQ mất khoảng **~8 phút**, sẽ **giảm kích thước mô hình từ ~7.5GB xuống ~2.5GB**.

    Trong bài lab này, chúng tôi hướng dẫn bạn cách nhập mô hình từ Hugging Face (ví dụ: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` lệnh sẽ tinh chỉnh mô hình đã lượng tử hóa. Lượng tử hóa mô hình *trước* khi tinh chỉnh thay vì sau giúp cải thiện độ chính xác vì quá trình tinh chỉnh bù đắp phần mất mát do lượng tử hóa.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    Quá trình tinh chỉnh mất khoảng **~6 phút** (với 100 bước).

1. **Tối ưu hóa:** Sau khi mô hình được huấn luyện, bạn tối ưu mô hình sử dụng lệnh `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` của Olive - nhưng trong bài lab này chúng ta sẽ dùng CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    Quá trình tối ưu mất khoảng **~5 phút**.

### Bước 5: Kiểm tra nhanh suy luận mô hình

Để kiểm tra suy luận mô hình, tạo một file Python trong thư mục của bạn có tên **app.py** và sao chép đoạn mã sau:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Chạy mã bằng lệnh:

```bash
python app.py
```

### Bước 6: Tải mô hình lên Azure AI

Tải mô hình lên kho lưu trữ mô hình Azure AI giúp chia sẻ mô hình với các thành viên khác trong nhóm phát triển và quản lý phiên bản mô hình. Để tải mô hình lên, chạy lệnh sau:

> [!NOTE]  
> Cập nhật `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` và tên Azure AI Project, rồi chạy lệnh sau

```
az ml workspace show
```

Hoặc truy cập +++ai.azure.com+++ và chọn **management center** > **project** > **overview**

Cập nhật các chỗ `{}` bằng tên Resource Group và tên Azure AI Project của bạn.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Bạn có thể xem mô hình đã tải lên và triển khai mô hình tại https://ml.azure.com/model/list

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.