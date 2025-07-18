<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-17T08:28:37+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "vi"
}
-->
## Các Kịch Bản Tinh Chỉnh

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.3d0cec8ae693e094c38c72575e63f2c9bf1cf980ab90f1388e102709f9c979e5.vi.png)

**Nền tảng** Bao gồm nhiều công nghệ khác nhau như Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito và ONNX Runtime.

**Hạ tầng** Bao gồm CPU và FPGA, những thành phần thiết yếu cho quá trình tinh chỉnh. Hãy để tôi giới thiệu các biểu tượng cho từng công nghệ này.

**Công cụ & Framework** Bao gồm ONNX Runtime và ONNX Runtime. Hãy để tôi giới thiệu các biểu tượng cho từng công nghệ này.  
[Chèn biểu tượng cho ONNX Runtime và ONNX Runtime]

Quá trình tinh chỉnh với các công nghệ của Microsoft bao gồm nhiều thành phần và công cụ khác nhau. Bằng cách hiểu và sử dụng các công nghệ này, chúng ta có thể tinh chỉnh ứng dụng một cách hiệu quả và tạo ra các giải pháp tốt hơn.

## Mô Hình như một Dịch Vụ

Tinh chỉnh mô hình bằng cách sử dụng fine-tuning được lưu trữ, không cần phải tạo và quản lý tài nguyên tính toán.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.3eee4630607aff0d0a137b16ab79ec5977ece923cd1fdd89557a2655c632669d.vi.png)

Tinh chỉnh serverless có sẵn cho các mô hình Phi-3-mini và Phi-3-medium, giúp các nhà phát triển nhanh chóng và dễ dàng tùy chỉnh mô hình cho các kịch bản đám mây và edge mà không cần phải chuẩn bị tài nguyên tính toán. Chúng tôi cũng đã công bố rằng Phi-3-small hiện có sẵn thông qua dịch vụ Models-as-a-Service, giúp các nhà phát triển bắt đầu phát triển AI nhanh chóng và dễ dàng mà không phải quản lý hạ tầng bên dưới.

## Mô Hình như một Nền Tảng

Người dùng tự quản lý tài nguyên tính toán để tinh chỉnh mô hình của mình.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.fd3829c1122f5d1c4a6a91593ebc348548410e162acda34f18034384e3b3816a.vi.png)

[Mẫu Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Các Kịch Bản Tinh Chỉnh

| | | | | | | |
|-|-|-|-|-|-|-|
|Kịch bản|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Điều chỉnh các LLM đã được huấn luyện trước cho các nhiệm vụ hoặc lĩnh vực cụ thể|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh cho các nhiệm vụ NLP như phân loại văn bản, nhận dạng thực thể có tên và dịch máy|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh cho các nhiệm vụ hỏi đáp (QA)|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh để tạo phản hồi giống con người trong chatbot|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh để tạo nhạc, nghệ thuật hoặc các hình thức sáng tạo khác|Có|Có|Có|Có|Có|Có|
|Giảm chi phí tính toán và tài chính|Có|Có|Không|Có|Có|Không|
|Giảm sử dụng bộ nhớ|Không|Có|Không|Có|Có|Có|
|Sử dụng ít tham số hơn để tinh chỉnh hiệu quả|Không|Có|Có|Không|Không|Có|
|Hình thức song song dữ liệu tiết kiệm bộ nhớ cho phép truy cập bộ nhớ GPU tổng hợp của tất cả các thiết bị GPU có sẵn|Không|Không|Không|Có|Có|Có|

## Ví Dụ Về Hiệu Suất Tinh Chỉnh

![Finetuning Performance](../../../../translated_images/Finetuningexamples.a9a41214f8f5afc186adb16a413b1c17e2f43a89933ba95feb5aee84b0b24add.vi.png)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.