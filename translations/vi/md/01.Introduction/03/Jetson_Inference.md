<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:43:51+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "vi"
}
-->
# **Inference Phi-3 trên Nvidia Jetson**

Nvidia Jetson là một dòng bo mạch máy tính nhúng của Nvidia. Các mẫu Jetson TK1, TX1 và TX2 đều sử dụng bộ xử lý Tegra (hoặc SoC) của Nvidia tích hợp CPU kiến trúc ARM. Jetson là hệ thống tiêu thụ điện năng thấp và được thiết kế để tăng tốc các ứng dụng học máy. Nvidia Jetson được các nhà phát triển chuyên nghiệp sử dụng để tạo ra các sản phẩm AI đột phá trong nhiều ngành công nghiệp, đồng thời cũng là công cụ học tập thực hành AI cho sinh viên và những người đam mê, giúp họ tạo ra các dự án ấn tượng. SLM được triển khai trên các thiết bị edge như Jetson, giúp cải thiện việc ứng dụng AI sinh tạo trong công nghiệp.

## Triển khai trên NVIDIA Jetson:
Các nhà phát triển làm việc với robot tự hành và thiết bị nhúng có thể tận dụng Phi-3 Mini. Kích thước nhỏ gọn của Phi-3 rất phù hợp để triển khai ở edge. Các tham số đã được tinh chỉnh kỹ lưỡng trong quá trình huấn luyện, đảm bảo độ chính xác cao trong phản hồi.

### Tối ưu TensorRT-LLM:
Thư viện [TensorRT-LLM của NVIDIA](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) tối ưu hóa việc suy luận các mô hình ngôn ngữ lớn. Nó hỗ trợ cửa sổ ngữ cảnh dài của Phi-3 Mini, cải thiện cả thông lượng và độ trễ. Các kỹ thuật tối ưu bao gồm LongRoPE, FP8 và inflight batching.

### Khả năng tiếp cận và Triển khai:
Các nhà phát triển có thể khám phá Phi-3 Mini với cửa sổ ngữ cảnh 128K tại [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Phiên bản này được đóng gói dưới dạng NVIDIA NIM, một microservice với API chuẩn có thể triển khai ở bất cứ đâu. Ngoài ra, có thể tham khảo các [cài đặt TensorRT-LLM trên GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Chuẩn bị**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Chạy Phi-3 trên Jetson**

Chúng ta có thể chọn [Ollama](https://ollama.com) hoặc [LlamaEdge](https://llamaedge.com)

Nếu bạn muốn sử dụng gguf trên cả đám mây và thiết bị edge cùng lúc, LlamaEdge có thể được hiểu như WasmEdge (WasmEdge là một runtime WebAssembly nhẹ, hiệu năng cao và có khả năng mở rộng, phù hợp cho các ứng dụng đám mây gốc, edge và phi tập trung. Nó hỗ trợ các ứng dụng serverless, hàm nhúng, microservices, hợp đồng thông minh và thiết bị IoT). Bạn có thể triển khai mô hình lượng tử gguf lên thiết bị edge và đám mây thông qua LlamaEdge.

![llamaedge](../../../../../translated_images/vi/llamaedge.e9d6ff96dff11cf7.jpg)

Dưới đây là các bước sử dụng

1. Cài đặt và tải các thư viện, file liên quan

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Lưu ý**: llama-api-server.wasm và chatbot-ui cần nằm trong cùng thư mục

2. Chạy các script trong terminal

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Kết quả chạy như sau

![llamaedgerun](../../../../../translated_images/vi/llamaedgerun.bed921516c9a821c.png)

***Mã mẫu*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Tóm lại, Phi-3 Mini là bước tiến lớn trong mô hình ngôn ngữ, kết hợp hiệu quả, nhận thức ngữ cảnh và khả năng tối ưu của NVIDIA. Dù bạn đang xây dựng robot hay ứng dụng edge, Phi-3 Mini là công cụ mạnh mẽ đáng để bạn quan tâm.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.