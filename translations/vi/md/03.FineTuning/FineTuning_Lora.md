# **Tinh chỉnh Phi-3 với Lora**

Tinh chỉnh mô hình ngôn ngữ Phi-3 Mini của Microsoft bằng cách sử dụng [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) trên bộ dữ liệu hướng dẫn trò chuyện tùy chỉnh.

LORA sẽ giúp cải thiện khả năng hiểu hội thoại và tạo phản hồi.

## Hướng dẫn từng bước cách tinh chỉnh Phi-3 Mini:

**Nhập thư viện và Cài đặt**

Cài đặt loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Bắt đầu bằng cách nhập các thư viện cần thiết như datasets, transformers, peft, trl và torch. Thiết lập logging để theo dõi quá trình huấn luyện.

Bạn có thể chọn điều chỉnh một số lớp bằng cách thay thế chúng bằng các phiên bản tương ứng được triển khai trong loralib. Hiện tại chúng tôi chỉ hỗ trợ nn.Linear, nn.Embedding và nn.Conv2d. Chúng tôi cũng hỗ trợ MergedLinear cho các trường hợp một nn.Linear đại diện cho nhiều lớp, ví dụ như trong một số triển khai của phép chiếu qkv trong attention (xem phần Ghi chú bổ sung để biết thêm chi tiết).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Trước khi bắt đầu vòng lặp huấn luyện, chỉ đánh dấu các tham số LoRA là có thể huấn luyện.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Khi lưu checkpoint, tạo một state_dict chỉ chứa các tham số LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Khi tải checkpoint bằng load_state_dict, nhớ đặt strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Bây giờ quá trình huấn luyện có thể tiến hành như bình thường.

**Siêu tham số**

Định nghĩa hai dictionary: training_config và peft_config. training_config bao gồm các siêu tham số cho việc huấn luyện, như learning rate, kích thước batch và cài đặt logging.

peft_config chỉ định các tham số liên quan đến LoRA như rank, dropout và loại tác vụ.

**Tải mô hình và Tokenizer**

Chỉ định đường dẫn đến mô hình Phi-3 đã được huấn luyện trước (ví dụ: "microsoft/Phi-3-mini-4k-instruct"). Cấu hình các thiết lập mô hình, bao gồm việc sử dụng cache, kiểu dữ liệu (bfloat16 cho độ chính xác hỗn hợp) và cách triển khai attention.

**Huấn luyện**

Tinh chỉnh mô hình Phi-3 sử dụng bộ dữ liệu hướng dẫn trò chuyện tùy chỉnh. Sử dụng các thiết lập LoRA từ peft_config để thích ứng hiệu quả. Theo dõi tiến trình huấn luyện bằng chiến lược logging đã chỉ định.

Đánh giá và Lưu: Đánh giá mô hình sau khi tinh chỉnh. Lưu các checkpoint trong quá trình huấn luyện để sử dụng sau.

**Ví dụ**
- [Tìm hiểu thêm với notebook mẫu này](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ví dụ về mẫu FineTuning Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Ví dụ Fine Tuning trên Hugging Face Hub với LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ví dụ Model Card trên Hugging Face - Mẫu Fine Tuning LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Ví dụ Fine Tuning trên Hugging Face Hub với QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.