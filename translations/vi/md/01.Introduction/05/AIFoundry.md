<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-05-09T15:00:58+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "vi"
}
-->
# **Sử dụng Azure AI Foundry để đánh giá**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.vi.png)

Cách đánh giá ứng dụng AI tạo sinh của bạn bằng [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Dù bạn đang đánh giá các cuộc hội thoại một lượt hay nhiều lượt, Azure AI Foundry cung cấp các công cụ để đánh giá hiệu suất và độ an toàn của mô hình.

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.vi.png)

## Cách đánh giá ứng dụng AI tạo sinh với Azure AI Foundry
Để biết hướng dẫn chi tiết, xem [Tài liệu Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Dưới đây là các bước để bắt đầu:

## Đánh giá Mô hình AI Tạo sinh trong Azure AI Foundry

**Yêu cầu trước**

- Một bộ dữ liệu thử nghiệm ở định dạng CSV hoặc JSON.
- Một mô hình AI tạo sinh đã được triển khai (như Phi-3, GPT 3.5, GPT 4, hoặc các mô hình Davinci).
- Một runtime với một compute instance để chạy quá trình đánh giá.

## Các Chỉ số Đánh giá Tích hợp

Azure AI Foundry cho phép bạn đánh giá cả các cuộc hội thoại một lượt và phức tạp nhiều lượt.
Đối với các kịch bản Retrieval Augmented Generation (RAG), nơi mô hình dựa trên dữ liệu cụ thể, bạn có thể đánh giá hiệu suất bằng các chỉ số đánh giá tích hợp sẵn.
Ngoài ra, bạn cũng có thể đánh giá các kịch bản trả lời câu hỏi một lượt chung (không phải RAG).

## Tạo một Lần Chạy Đánh giá

Từ giao diện Azure AI Foundry, điều hướng đến trang Evaluate hoặc trang Prompt Flow.
Theo hướng dẫn tạo đánh giá để thiết lập một lần chạy đánh giá. Bạn có thể đặt tên tùy chọn cho lần đánh giá của mình.
Chọn kịch bản phù hợp với mục tiêu của ứng dụng.
Chọn một hoặc nhiều chỉ số đánh giá để đánh giá kết quả mô hình.

## Quy trình Đánh giá Tùy chỉnh (Tùy chọn)

Để linh hoạt hơn, bạn có thể thiết lập một quy trình đánh giá tùy chỉnh. Tùy chỉnh quá trình đánh giá dựa trên yêu cầu riêng của bạn.

## Xem Kết quả

Sau khi chạy đánh giá, ghi lại, xem và phân tích các chỉ số đánh giá chi tiết trong Azure AI Foundry. Hiểu rõ hơn về khả năng và giới hạn của ứng dụng của bạn.

**Note** Azure AI Foundry hiện đang trong giai đoạn xem trước công khai, vì vậy hãy sử dụng cho mục đích thử nghiệm và phát triển. Đối với các khối lượng công việc sản xuất, hãy cân nhắc các lựa chọn khác. Tham khảo [tài liệu AI Foundry chính thức](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) để biết thêm chi tiết và hướng dẫn từng bước.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.