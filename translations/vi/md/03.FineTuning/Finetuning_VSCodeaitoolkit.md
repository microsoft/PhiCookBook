<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:16:31+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "vi"
}
-->
## Chào mừng đến với AI Toolkit cho VS Code

[AI Toolkit cho VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) tập hợp nhiều mô hình từ Azure AI Studio Catalog và các catalog khác như Hugging Face. Bộ công cụ giúp đơn giản hóa các tác vụ phát triển phổ biến để xây dựng ứng dụng AI với các công cụ và mô hình AI tạo sinh thông qua:
- Bắt đầu với khám phá mô hình và playground.
- Tinh chỉnh mô hình và suy luận sử dụng tài nguyên tính toán cục bộ.
- Tinh chỉnh và suy luận từ xa sử dụng tài nguyên Azure.

[Cài đặt AI Toolkit cho VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/vi/Aitoolkit.7157953df04812dc.png)

**[Private Preview]** Cung cấp một cú nhấp chuột cho Azure Container Apps để chạy tinh chỉnh mô hình và suy luận trên đám mây.

Bây giờ hãy bắt đầu phát triển ứng dụng AI của bạn:

- [Chào mừng đến với AI Toolkit cho VS Code](../../../../md/03.FineTuning)
- [Phát triển cục bộ](../../../../md/03.FineTuning)
  - [Chuẩn bị](../../../../md/03.FineTuning)
  - [Kích hoạt Conda](../../../../md/03.FineTuning)
  - [Chỉ tinh chỉnh mô hình cơ bản](../../../../md/03.FineTuning)
  - [Tinh chỉnh và suy luận mô hình](../../../../md/03.FineTuning)
  - [Tinh chỉnh mô hình](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Mẫu và tài nguyên tinh chỉnh](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Phát triển từ xa](../../../../md/03.FineTuning)
  - [Yêu cầu trước](../../../../md/03.FineTuning)
  - [Thiết lập dự án phát triển từ xa](../../../../md/03.FineTuning)
  - [Cung cấp tài nguyên Azure](../../../../md/03.FineTuning)
  - [\[Tùy chọn\] Thêm Huggingface Token vào Azure Container App Secret](../../../../md/03.FineTuning)
  - [Chạy tinh chỉnh](../../../../md/03.FineTuning)
  - [Cung cấp điểm cuối suy luận](../../../../md/03.FineTuning)
  - [Triển khai điểm cuối suy luận](../../../../md/03.FineTuning)
  - [Sử dụng nâng cao](../../../../md/03.FineTuning)

## Phát triển cục bộ
### Chuẩn bị

1. Đảm bảo đã cài đặt driver NVIDIA trên máy chủ.
2. Chạy `huggingface-cli login` nếu bạn sử dụng HF để tận dụng dataset.
3. Giải thích các thiết lập khóa `Olive` liên quan đến việc thay đổi sử dụng bộ nhớ.

### Kích hoạt Conda
Vì chúng ta sử dụng môi trường WSL và nó được chia sẻ, bạn cần kích hoạt thủ công môi trường conda. Sau bước này, bạn có thể chạy tinh chỉnh hoặc suy luận.

```bash
conda activate [conda-env-name] 
```

### Chỉ tinh chỉnh mô hình cơ bản
Nếu bạn chỉ muốn thử mô hình cơ bản mà không tinh chỉnh, bạn có thể chạy lệnh này sau khi kích hoạt conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Tinh chỉnh và suy luận mô hình

Khi workspace được mở trong dev container, mở terminal (đường dẫn mặc định là thư mục gốc dự án), sau đó chạy lệnh dưới đây để tinh chỉnh một LLM trên dataset đã chọn.

```bash
python finetuning/invoke_olive.py 
```

Các checkpoint và mô hình cuối cùng sẽ được lưu trong thư mục `models`.

Tiếp theo, chạy suy luận với mô hình đã được tinh chỉnh thông qua chat trong `console`, `trình duyệt web` hoặc `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Để sử dụng `prompt flow` trong VS Code, vui lòng tham khảo [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Tinh chỉnh mô hình

Tiếp theo, tải mô hình phù hợp tùy theo việc thiết bị của bạn có GPU hay không.

Để bắt đầu phiên tinh chỉnh cục bộ sử dụng QLoRA, chọn một mô hình bạn muốn tinh chỉnh từ catalog của chúng tôi.
| Nền tảng | Có GPU | Tên mô hình | Kích thước (GB) |
|---------|---------|--------|--------|
| Windows | Có | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Có | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Không | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Lưu ý_** Bạn không cần tài khoản Azure để tải mô hình.

Mô hình Phi3-mini (int4) có kích thước khoảng 2GB-3GB. Tùy tốc độ mạng, việc tải xuống có thể mất vài phút.

Bắt đầu bằng cách chọn tên dự án và vị trí lưu.
Tiếp theo, chọn mô hình từ catalog. Bạn sẽ được nhắc tải mẫu dự án. Sau đó, bạn có thể nhấn "Configure Project" để điều chỉnh các thiết lập.

### Microsoft Olive

Chúng tôi sử dụng [Olive](https://microsoft.github.io/Olive/why-olive.html) để chạy tinh chỉnh QLoRA trên mô hình PyTorch từ catalog. Tất cả các thiết lập được đặt sẵn với giá trị mặc định nhằm tối ưu hóa quá trình tinh chỉnh cục bộ với việc sử dụng bộ nhớ hiệu quả, nhưng bạn có thể điều chỉnh theo tình huống của mình.

### Mẫu và tài nguyên tinh chỉnh

- [Hướng dẫn bắt đầu tinh chỉnh](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Tinh chỉnh với Dataset HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Tinh chỉnh với Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Phát triển từ xa

### Yêu cầu trước

1. Để chạy tinh chỉnh mô hình trong môi trường Azure Container App từ xa, đảm bảo subscription của bạn có đủ dung lượng GPU. Gửi [phiếu hỗ trợ](https://azure.microsoft.com/support/create-ticket/) để yêu cầu dung lượng cần thiết cho ứng dụng của bạn. [Tìm hiểu thêm về dung lượng GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Nếu bạn sử dụng dataset riêng tư trên HuggingFace, đảm bảo bạn có [tài khoản HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) và [tạo token truy cập](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Bật tính năng Remote Fine-tuning and Inference trong AI Toolkit cho VS Code
   1. Mở Cài đặt VS Code bằng cách chọn *File -> Preferences -> Settings*.
   2. Điều hướng đến *Extensions* và chọn *AI Toolkit*.
   3. Chọn tùy chọn *"Enable Remote Fine-tuning And Inference"*.
   4. Tải lại VS Code để áp dụng thay đổi.

- [Tinh chỉnh từ xa](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Thiết lập dự án phát triển từ xa
1. Thực thi bảng lệnh `AI Toolkit: Focus on Resource View`.
2. Điều hướng đến *Model Fine-tuning* để truy cập catalog mô hình. Đặt tên cho dự án và chọn vị trí lưu trên máy của bạn. Sau đó, nhấn nút *"Configure Project"*.
3. Cấu hình dự án
    1. Tránh bật tùy chọn *"Fine-tune locally"*.
    2. Các thiết lập Olive sẽ hiển thị với giá trị mặc định đã đặt sẵn. Vui lòng điều chỉnh và điền các cấu hình theo yêu cầu.
    3. Tiếp tục với *Generate Project*. Bước này sử dụng WSL và thiết lập môi trường Conda mới, chuẩn bị cho các cập nhật tương lai bao gồm Dev Containers.
4. Nhấn *"Relaunch Window In Workspace"* để mở dự án phát triển từ xa.

> **Lưu ý:** Dự án hiện chỉ hoạt động cục bộ hoặc từ xa trong AI Toolkit cho VS Code. Nếu bạn chọn *"Fine-tune locally"* khi tạo dự án, nó sẽ chỉ chạy trong WSL mà không có khả năng phát triển từ xa. Ngược lại, nếu không bật *"Fine-tune locally"*, dự án sẽ bị giới hạn trong môi trường Azure Container App từ xa.

### Cung cấp tài nguyên Azure
Để bắt đầu, bạn cần cung cấp tài nguyên Azure cho việc tinh chỉnh từ xa. Thực hiện bằng cách chạy lệnh `AI Toolkit: Provision Azure Container Apps job for fine-tuning` từ bảng lệnh.

Theo dõi tiến trình cung cấp qua liên kết hiển thị trong kênh đầu ra.

### [Tùy chọn] Thêm Huggingface Token vào Azure Container App Secret
Nếu bạn sử dụng dataset riêng tư trên HuggingFace, hãy đặt token HuggingFace của bạn làm biến môi trường để tránh phải đăng nhập thủ công trên Hugging Face Hub.
Bạn có thể làm điều này bằng lệnh `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Với lệnh này, bạn có thể đặt tên bí mật là [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) và sử dụng token Hugging Face của bạn làm giá trị bí mật.

### Chạy tinh chỉnh
Để bắt đầu công việc tinh chỉnh từ xa, thực thi lệnh `AI Toolkit: Run fine-tuning`.

Để xem nhật ký hệ thống và console, bạn có thể truy cập cổng Azure qua liên kết trong bảng đầu ra (xem thêm tại [Xem và truy vấn nhật ký trên Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Hoặc, bạn có thể xem nhật ký console trực tiếp trong bảng đầu ra VSCode bằng cách chạy lệnh `AI Toolkit: Show the running fine-tuning job streaming logs`.
> **Lưu ý:** Công việc có thể bị xếp hàng do thiếu tài nguyên. Nếu nhật ký không hiển thị, hãy chạy lệnh `AI Toolkit: Show the running fine-tuning job streaming logs`, chờ một lúc rồi chạy lại lệnh để kết nối lại với luồng nhật ký.

Trong quá trình này, QLoRA sẽ được sử dụng để tinh chỉnh, tạo các adapter LoRA cho mô hình dùng trong suy luận.
Kết quả tinh chỉnh sẽ được lưu trữ trong Azure Files.

### Cung cấp điểm cuối suy luận
Sau khi các adapter được huấn luyện trong môi trường từ xa, sử dụng ứng dụng Gradio đơn giản để tương tác với mô hình.
Tương tự như quá trình tinh chỉnh, bạn cần thiết lập tài nguyên Azure cho suy luận từ xa bằng cách chạy lệnh `AI Toolkit: Provision Azure Container Apps for inference` từ bảng lệnh.

Mặc định, subscription và nhóm tài nguyên cho suy luận nên trùng với những cái đã dùng cho tinh chỉnh. Suy luận sẽ sử dụng cùng môi trường Azure Container App và truy cập mô hình cùng adapter mô hình được lưu trong Azure Files, được tạo ra trong bước tinh chỉnh.

### Triển khai điểm cuối suy luận
Nếu bạn muốn chỉnh sửa mã suy luận hoặc tải lại mô hình suy luận, hãy thực thi lệnh `AI Toolkit: Deploy for inference`. Lệnh này sẽ đồng bộ mã mới nhất của bạn với Azure Container App và khởi động lại bản sao.

Khi triển khai thành công, bạn có thể truy cập API suy luận bằng cách nhấn nút "*Go to Inference Endpoint*" hiển thị trong thông báo VSCode. Hoặc, điểm cuối API web có thể được tìm thấy trong `ACA_APP_ENDPOINT` tại `./infra/inference.config.json` và trong bảng đầu ra. Bạn đã sẵn sàng để đánh giá mô hình qua điểm cuối này.

### Sử dụng nâng cao
Để biết thêm thông tin về phát triển từ xa với AI Toolkit, tham khảo tài liệu [Tinh chỉnh mô hình từ xa](https://aka.ms/ai-toolkit/remote-provision) và [Suy luận với mô hình đã tinh chỉnh](https://aka.ms/ai-toolkit/remote-inference).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.