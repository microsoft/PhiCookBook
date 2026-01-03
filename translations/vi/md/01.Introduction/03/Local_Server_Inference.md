<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:58:16+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "vi"
}
-->
# **Triển khai Phi-3 trên Máy chủ Cục bộ**

Chúng ta có thể triển khai Phi-3 trên một máy chủ cục bộ. Người dùng có thể chọn các giải pháp như [Ollama](https://ollama.com) hoặc [LM Studio](https://llamaedge.com), hoặc tự viết mã của riêng họ. Bạn có thể kết nối dịch vụ cục bộ của Phi-3 thông qua [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) hoặc [Langchain](https://www.langchain.com/) để xây dựng các ứng dụng Copilot.

## **Sử dụng Semantic Kernel để truy cập Phi-3-mini**

Trong ứng dụng Copilot, chúng ta tạo ứng dụng thông qua Semantic Kernel / LangChain. Loại khung ứng dụng này thường tương thích với Azure OpenAI Service / các mô hình OpenAI, đồng thời cũng hỗ trợ các mô hình mã nguồn mở trên Hugging Face và các mô hình cục bộ. Vậy nếu muốn sử dụng Semantic Kernel để truy cập Phi-3-mini thì làm thế nào? Lấy ví dụ với .NET, chúng ta có thể kết hợp nó với Hugging Face Connector trong Semantic Kernel. Theo mặc định, nó sẽ tương ứng với model id trên Hugging Face (lần đầu sử dụng, mô hình sẽ được tải xuống từ Hugging Face, mất khá nhiều thời gian). Bạn cũng có thể kết nối với dịch vụ cục bộ đã được xây dựng sẵn. So với hai cách, chúng tôi khuyên bạn nên dùng cách sau vì nó có tính tự chủ cao hơn, đặc biệt trong các ứng dụng doanh nghiệp.

![sk](../../../../../translated_images/sk.d03785c25edc6d44.vi.png)

Từ hình trên, việc truy cập dịch vụ cục bộ qua Semantic Kernel có thể dễ dàng kết nối với máy chủ mô hình Phi-3-mini tự xây dựng. Dưới đây là kết quả chạy thử:

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca20.vi.png)

***Mã mẫu*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.