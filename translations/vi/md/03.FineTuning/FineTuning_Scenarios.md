## Kịch bản Tinh Chỉnh

![FineTuning với Dịch vụ MS](../../../../translated_images/vi/FinetuningwithMS.3d0cec8ae693e094.webp)

Phần này cung cấp tổng quan về các kịch bản tinh chỉnh trong Microsoft Foundry và môi trường Azure, bao gồm các mô hình triển khai, các lớp hạ tầng và các kỹ thuật tối ưu hóa phổ biến.

**Nền tảng**  
Điều này bao gồm các dịch vụ được quản lý như Microsoft Foundry (trước đây là Microsoft Foundry) và Azure Machine Learning, cung cấp quản lý mô hình, điều phối, theo dõi thí nghiệm và quy trình triển khai.

**Hạ tầng**  
Tinh chỉnh yêu cầu tài nguyên tính toán có thể mở rộng. Trong môi trường Azure, điều này thường bao gồm các máy ảo dựa trên GPU và tài nguyên CPU cho các công việc nhẹ, cùng với lưu trữ mở rộng cho bộ dữ liệu và điểm kiểm tra.

**Công cụ & Khung làm việc**  
Quy trình tinh chỉnh thường dựa vào các khung làm việc và thư viện tối ưu hóa như Hugging Face Transformers, DeepSpeed và PEFT (Tinh Chỉnh Hiệu Quả Tham Số).

Quá trình tinh chỉnh với công nghệ Microsoft trải rộng qua dịch vụ nền tảng, hạ tầng tính toán và khung đào tạo. Bằng cách hiểu cách các thành phần này hoạt động cùng nhau, các nhà phát triển có thể hiệu quả điều chỉnh các mô hình nền tảng cho các tác vụ và kịch bản sản xuất cụ thể.

## Mô hình như một Dịch vụ

Tinh chỉnh mô hình sử dụng tinh chỉnh được lưu trữ, không cần tạo và quản lý tài nguyên tính toán.

![Tinh chỉnh MaaS](../../../../translated_images/vi/MaaSfinetune.3eee4630607aff0d.webp)

Tinh chỉnh không máy chủ hiện có sẵn cho các dòng mô hình Phi-3, Phi-3.5 và Phi-4, cho phép các nhà phát triển nhanh chóng và dễ dàng tùy chỉnh mô hình cho các kịch bản đám mây và cạnh mà không cần sắp xếp tài nguyên tính toán.

## Mô hình như một Nền tảng

Người dùng tự quản lý tài nguyên tính toán để tinh chỉnh mô hình của họ.

![Tinh chỉnh MaaP](../../../../translated_images/vi/MaaPFinetune.fd3829c1122f5d1c.webp)

[Mẫu Tinh Chỉnh](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## So sánh Kỹ thuật Tinh Chỉnh

|Kịch bản|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Điều chỉnh các LLM đã được huấn luyện trước cho các tác vụ hoặc miền cụ thể|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh cho các tác vụ NLP như phân loại văn bản, nhận dạng thực thể đặt tên và dịch máy|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh cho các tác vụ Hỏi Đáp|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh để tạo phản hồi giống người trong chatbot|Có|Có|Có|Có|Có|Có|
|Tinh chỉnh để tạo nhạc, nghệ thuật hoặc các hình thức sáng tạo khác|Có|Có|Có|Có|Có|Có|
|Giảm chi phí tính toán và tài chính|Có|Có|Có|Có|Có|Có|
|Giảm sử dụng bộ nhớ|Có|Có|Có|Có|Có|Có|
|Sử dụng ít tham số hơn cho tinh chỉnh hiệu quả|Có|Có|Có|Không|Không|Có|
|Hình thức song song dữ liệu tiết kiệm bộ nhớ cho phép truy cập bộ nhớ GPU tổng hợp của tất cả các thiết bị GPU có sẵn|Không|Không|Không|Có|Có|Không|

> [!NOTE]
> LoRA, QLoRA, PEFT và DoRA là các phương pháp tinh chỉnh hiệu quả tham số, trong khi DeepSpeed và ZeRO tập trung vào đào tạo phân tán và tối ưu hóa bộ nhớ.

## Ví dụ Hiệu suất Tinh Chỉnh

![Hiệu suất Tinh Chỉnh](../../../../translated_images/vi/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính xác và có thẩm quyền. Đối với những thông tin quan trọng, nên sử dụng bản dịch do con người chuyên nghiệp thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->