<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "vi"
}
-->
**Tinh chỉnh Phi-3 với QLoRA**

Tinh chỉnh mô hình ngôn ngữ Phi-3 Mini của Microsoft bằng cách sử dụng [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA sẽ giúp cải thiện khả năng hiểu hội thoại và tạo phản hồi.

Để tải các mô hình ở dạng 4bit với transformers và bitsandbytes, bạn cần cài đặt accelerate và transformers từ mã nguồn và đảm bảo bạn có phiên bản mới nhất của thư viện bitsandbytes.

**Mẫu**
- [Tìm hiểu thêm với sổ tay mẫu này](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ví dụ về mẫu Tinh chỉnh Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Ví dụ Tinh chỉnh trên Hugging Face Hub với LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ví dụ Tinh chỉnh trên Hugging Face Hub với QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.