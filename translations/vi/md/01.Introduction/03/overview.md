<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:28:53+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "vi"
}
-->
Trong bối cảnh của Phi-3-mini, inference đề cập đến quá trình sử dụng mô hình để đưa ra dự đoán hoặc tạo ra kết quả dựa trên dữ liệu đầu vào. Hãy để tôi cung cấp thêm chi tiết về Phi-3-mini và khả năng inference của nó.

Phi-3-mini là một phần của dòng mô hình Phi-3 được Microsoft phát hành. Những mô hình này được thiết kế để định nghĩa lại những gì có thể với các Small Language Models (SLMs).

Dưới đây là một số điểm chính về Phi-3-mini và khả năng inference của nó:

## **Tổng quan về Phi-3-mini:**
- Phi-3-mini có kích thước tham số là 3.8 tỷ.
- Nó có thể chạy không chỉ trên các thiết bị tính toán truyền thống mà còn trên các thiết bị biên như thiết bị di động và thiết bị IoT.
- Việc phát hành Phi-3-mini giúp cá nhân và doanh nghiệp triển khai SLM trên nhiều thiết bị phần cứng khác nhau, đặc biệt trong các môi trường có hạn chế về tài nguyên.
- Nó hỗ trợ nhiều định dạng mô hình khác nhau, bao gồm định dạng PyTorch truyền thống, phiên bản lượng tử hóa của định dạng gguf, và phiên bản lượng tử hóa dựa trên ONNX.

## **Truy cập Phi-3-mini:**
Để truy cập Phi-3-mini, bạn có thể sử dụng [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) trong ứng dụng Copilot. Semantic Kernel tương thích chung với Azure OpenAI Service, các mô hình mã nguồn mở trên Hugging Face, và các mô hình cục bộ.
Bạn cũng có thể sử dụng [Ollama](https://ollama.com) hoặc [LlamaEdge](https://llamaedge.com) để gọi các mô hình đã lượng tử hóa. Ollama cho phép người dùng cá nhân gọi các mô hình lượng tử hóa khác nhau, trong khi LlamaEdge cung cấp khả năng sử dụng đa nền tảng cho các mô hình GGUF.

## **Các mô hình lượng tử hóa:**
Nhiều người dùng ưu tiên sử dụng các mô hình lượng tử hóa cho inference cục bộ. Ví dụ, bạn có thể chạy trực tiếp Ollama run Phi-3 hoặc cấu hình nó ngoại tuyến bằng cách sử dụng Modelfile. Modelfile xác định đường dẫn tệp GGUF và định dạng prompt.

## **Khả năng của AI sinh tạo:**
Việc kết hợp các SLM như Phi-3-mini mở ra nhiều khả năng mới cho AI sinh tạo. Inference chỉ là bước đầu tiên; những mô hình này có thể được sử dụng cho nhiều tác vụ khác nhau trong các tình huống hạn chế tài nguyên, giới hạn độ trễ, và hạn chế chi phí.

## **Mở khóa AI sinh tạo với Phi-3-mini: Hướng dẫn về Inference và Triển khai**  
Tìm hiểu cách sử dụng Semantic Kernel, Ollama/LlamaEdge, và ONNX Runtime để truy cập và inference các mô hình Phi-3-mini, đồng thời khám phá các khả năng của AI sinh tạo trong nhiều kịch bản ứng dụng khác nhau.

**Tính năng**  
Inference mô hình phi3-mini trong:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Tóm lại, Phi-3-mini cho phép các nhà phát triển khám phá nhiều định dạng mô hình khác nhau và tận dụng AI sinh tạo trong nhiều kịch bản ứng dụng đa dạng.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.