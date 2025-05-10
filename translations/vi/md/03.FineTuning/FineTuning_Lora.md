<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:00+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "vi"
}
-->
# **Tinh chỉnh Phi-3 với Lora**

Tinh chỉnh mô hình ngôn ngữ Phi-3 Mini của Microsoft sử dụng [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) trên bộ dữ liệu hướng dẫn chat tùy chỉnh.

LORA sẽ giúp cải thiện khả năng hiểu hội thoại và tạo phản hồi.

## Hướng dẫn từng bước để tinh chỉnh Phi-3 Mini:

**Imports và Thiết lập**

Cài đặt loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Bắt đầu bằng cách import các thư viện cần thiết như datasets, transformers, peft, trl và torch. Thiết lập logging để theo dõi quá trình huấn luyện.

Bạn có thể chọn tinh chỉnh một số lớp bằng cách thay thế chúng bằng các bản triển khai trong loralib. Hiện tại chúng tôi chỉ hỗ trợ nn.Linear, nn.Embedding và nn.Conv2d. Chúng tôi cũng hỗ trợ MergedLinear cho các trường hợp một nn.Linear đại diện cho nhiều lớp, ví dụ như trong một số triển khai của attention qkv projection (xem phần Ghi chú thêm để biết chi tiết).

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

Trước khi bắt đầu vòng lặp huấn luyện, đánh dấu chỉ các tham số LoRA là có thể huấn luyện.

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

Khi tải checkpoint dùng load_state_dict, nhớ đặt strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Bây giờ quá trình huấn luyện có thể tiếp tục như bình thường.

**Siêu tham số**

Định nghĩa hai dictionary: training_config và peft_config. training_config bao gồm các siêu tham số cho việc huấn luyện, như learning rate, kích thước batch và cài đặt logging.

peft_config chỉ định các tham số liên quan đến LoRA như rank, dropout và loại tác vụ.

**Tải Model và Tokenizer**

Chỉ định đường dẫn đến mô hình Phi-3 đã được huấn luyện sẵn (ví dụ: "microsoft/Phi-3-mini-4k-instruct"). Cấu hình các thiết lập model, bao gồm sử dụng cache, kiểu dữ liệu (bfloat16 cho mixed precision), và cách triển khai attention.

**Huấn luyện**

Tinh chỉnh mô hình Phi-3 sử dụng bộ dữ liệu hướng dẫn chat tùy chỉnh. Dùng các thiết lập LoRA từ peft_config để thích ứng hiệu quả. Giám sát tiến trình huấn luyện bằng chiến lược logging đã chỉ định.

Đánh giá và Lưu: Đánh giá mô hình sau khi tinh chỉnh. Lưu các checkpoint trong quá trình huấn luyện để sử dụng sau.

**Ví dụ**
- [Tìm hiểu thêm với notebook mẫu này](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ví dụ Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Ví dụ Hugging Face Hub Fine Tuning với LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ví dụ Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Ví dụ Hugging Face Hub Fine Tuning với QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính xác nhất. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.