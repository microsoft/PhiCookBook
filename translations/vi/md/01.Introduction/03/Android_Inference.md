<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:14:49+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "vi"
}
-->
# **Inference Phi-3 trên Android**

Hãy cùng tìm hiểu cách bạn có thể thực hiện inference với Phi-3-mini trên các thiết bị Android. Phi-3-mini là dòng mô hình mới từ Microsoft, cho phép triển khai các Large Language Models (LLMs) trên các thiết bị edge và thiết bị IoT.

## Semantic Kernel và Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) là một framework ứng dụng giúp bạn tạo ra các ứng dụng tương thích với Azure OpenAI Service, các mô hình OpenAI, và thậm chí cả các mô hình cục bộ. Nếu bạn mới làm quen với Semantic Kernel, chúng tôi khuyên bạn nên xem qua [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Truy cập Phi-3-mini bằng Semantic Kernel

Bạn có thể kết hợp nó với Hugging Face Connector trong Semantic Kernel. Tham khảo [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Mặc định, nó tương ứng với model ID trên Hugging Face. Tuy nhiên, bạn cũng có thể kết nối với server mô hình Phi-3-mini được xây dựng cục bộ.

### Gọi các mô hình đã được lượng tử hóa với Ollama hoặc LlamaEdge

Nhiều người dùng thích sử dụng các mô hình đã được lượng tử hóa để chạy mô hình cục bộ. [Ollama](https://ollama.com/) và [LlamaEdge](https://llamaedge.com) cho phép người dùng cá nhân gọi các mô hình lượng tử hóa khác nhau:

#### Ollama

Bạn có thể chạy trực tiếp `ollama run Phi-3` hoặc cấu hình offline bằng cách tạo một `Modelfile` với đường dẫn đến file `.gguf` của bạn.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Nếu bạn muốn sử dụng file `.gguf` trên cả đám mây và các thiết bị edge cùng lúc, LlamaEdge là lựa chọn tuyệt vời. Bạn có thể tham khảo [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) để bắt đầu.

### Cài đặt và chạy trên điện thoại Android

1. **Tải ứng dụng MLC Chat** (Miễn phí) cho điện thoại Android.
2. Tải file APK (148MB) và cài đặt trên thiết bị của bạn.
3. Mở ứng dụng MLC Chat. Bạn sẽ thấy danh sách các mô hình AI, bao gồm Phi-3-mini.

Tóm lại, Phi-3-mini mở ra nhiều cơ hội thú vị cho AI tạo sinh trên các thiết bị edge, và bạn có thể bắt đầu khám phá khả năng của nó trên Android.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.