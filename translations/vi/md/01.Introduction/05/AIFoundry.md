# **Sử dụng Microsoft Foundry để đánh giá**

![aistudo](../../../../../translated_images/vi/AIFoundry.9e0b513e999a1c5a.webp)

Cách đánh giá ứng dụng AI tạo sinh của bạn bằng [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Cho dù bạn đang đánh giá các cuộc trò chuyện một lần hay nhiều lần, Microsoft Foundry cung cấp các công cụ để đánh giá hiệu suất và độ an toàn của mô hình.

![aistudo](../../../../../translated_images/vi/AIPortfolio.69da59a8e1eaa70f.webp)

## Cách đánh giá ứng dụng AI tạo sinh với Microsoft Foundry
Để xem hướng dẫn chi tiết hơn, tham khảo [Tài liệu Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Dưới đây là các bước để bắt đầu:

## Đánh giá Mô hình AI tạo sinh trong Microsoft Foundry

**Yêu cầu tiên quyết**

- Một bộ dữ liệu kiểm thử ở định dạng CSV hoặc JSON.
- Một mô hình AI tạo sinh đã được triển khai (như Phi-3, GPT 3.5, GPT 4, hoặc các mô hình Davinci).
- Một runtime có một phiên bản tính toán để chạy đánh giá.

## Các Chỉ số Đánh giá Được tích hợp sẵn

Microsoft Foundry cho phép bạn đánh giá cả các cuộc trò chuyện một lượt lẫn các cuộc trò chuyện phức tạp, nhiều lượt.
Đối với các tình huống Retrieval Augmented Generation (RAG), nơi mô hình được nền tảng hóa trên dữ liệu cụ thể, bạn có thể đánh giá hiệu suất bằng các chỉ số đánh giá tích hợp sẵn.
Ngoài ra, bạn cũng có thể đánh giá các tình huống hỏi đáp một lượt chung (không RAG).

## Tạo một Lần chạy Đánh giá

Từ giao diện người dùng Microsoft Foundry, điều hướng đến trang Evaluate hoặc trang Prompt Flow.
Làm theo trình hướng dẫn tạo đánh giá để thiết lập một lần chạy đánh giá. Cung cấp tên tùy chọn cho lần đánh giá của bạn.
Chọn kịch bản phù hợp với mục tiêu của ứng dụng bạn.
Chọn một hoặc nhiều chỉ số đánh giá để đánh giá đầu ra của mô hình.

## Luồng Đánh giá Tùy chỉnh (Tùy chọn)

Để linh hoạt hơn, bạn có thể thiết lập một luồng đánh giá tùy chỉnh. Tùy chỉnh quá trình đánh giá dựa trên yêu cầu cụ thể của bạn.

## Xem Kết quả

Sau khi chạy đánh giá, ghi lại, xem và phân tích các chỉ số đánh giá chi tiết trong Microsoft Foundry. Nhận thông tin chi tiết về năng lực và giới hạn của ứng dụng bạn.

**Note** Microsoft Foundry hiện đang ở bản xem trước công khai, vì vậy hãy sử dụng nó cho mục đích thử nghiệm và phát triển. Với các khối lượng công việc sản xuất, hãy cân nhắc các lựa chọn khác. Khám phá tài liệu chính thức [AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) để biết thêm chi tiết và hướng dẫn từng bước.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ nguyên bản được xem là nguồn chính xác và đáng tin cậy nhất. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->