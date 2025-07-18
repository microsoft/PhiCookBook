<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:10:45+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "vi"
}
-->
# **Lượng tử hóa Phi Family sử dụng llama.cpp**

## **llama.cpp là gì**

llama.cpp là một thư viện phần mềm mã nguồn mở chủ yếu được viết bằng C++ dùng để thực hiện suy luận trên các Mô hình Ngôn ngữ Lớn (LLMs) khác nhau, chẳng hạn như Llama. Mục tiêu chính của nó là cung cấp hiệu suất hàng đầu cho việc suy luận LLM trên nhiều loại phần cứng với thiết lập tối thiểu. Ngoài ra, thư viện này còn có các binding Python, cung cấp API cấp cao cho hoàn thành văn bản và một máy chủ web tương thích với OpenAI.

Mục tiêu chính của llama.cpp là cho phép suy luận LLM với thiết lập tối thiểu và hiệu suất hàng đầu trên nhiều loại phần cứng - cả cục bộ và trên đám mây.

- Triển khai thuần C/C++ không phụ thuộc vào thư viện nào khác
- Apple silicon được ưu tiên hàng đầu - tối ưu qua ARM NEON, Accelerate và Metal frameworks
- Hỗ trợ AVX, AVX2 và AVX512 cho kiến trúc x86
- Lượng tử hóa số nguyên 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit và 8-bit giúp suy luận nhanh hơn và giảm sử dụng bộ nhớ
- Kernel CUDA tùy chỉnh để chạy LLM trên GPU NVIDIA (hỗ trợ GPU AMD qua HIP)
- Hỗ trợ backend Vulkan và SYCL
- Suy luận lai CPU+GPU để tăng tốc một phần các mô hình lớn hơn tổng dung lượng VRAM

## **Lượng tử hóa Phi-3.5 với llama.cpp**

Mô hình Phi-3.5-Instruct có thể được lượng tử hóa bằng llama.cpp, nhưng Phi-3.5-Vision và Phi-3.5-MoE hiện chưa được hỗ trợ. Định dạng được chuyển đổi bởi llama.cpp là gguf, cũng là định dạng lượng tử hóa được sử dụng rộng rãi nhất.

Có rất nhiều mô hình định dạng GGUF đã được lượng tử hóa trên Hugging face. AI Foundry, Ollama và LlamaEdge dựa vào llama.cpp, vì vậy các mô hình GGUF cũng thường được sử dụng.

### **GGUF là gì**

GGUF là một định dạng nhị phân được tối ưu để tải và lưu mô hình nhanh chóng, giúp rất hiệu quả cho mục đích suy luận. GGUF được thiết kế để sử dụng với GGML và các trình thực thi khác. GGUF được phát triển bởi @ggerganov, cũng là người phát triển llama.cpp, một framework suy luận LLM phổ biến viết bằng C/C++. Các mô hình ban đầu phát triển trong các framework như PyTorch có thể được chuyển đổi sang định dạng GGUF để sử dụng với các engine đó.

### **ONNX và GGUF**

ONNX là một định dạng truyền thống cho máy học/máy học sâu, được hỗ trợ tốt trong nhiều Framework AI khác nhau và có nhiều kịch bản sử dụng trên các thiết bị biên. Còn GGUF dựa trên llama.cpp và có thể coi là sản phẩm của thời đại GenAI. Hai định dạng này có mục đích sử dụng tương tự nhau. Nếu bạn muốn hiệu suất tốt hơn trên phần cứng nhúng và tầng ứng dụng, ONNX có thể là lựa chọn của bạn. Nếu bạn sử dụng framework và công nghệ phát sinh từ llama.cpp, thì GGUF có thể phù hợp hơn.

### **Lượng tử hóa Phi-3.5-Instruct sử dụng llama.cpp**

**1. Cấu hình môi trường**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Lượng tử hóa**

Sử dụng llama.cpp để chuyển Phi-3.5-Instruct sang FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Lượng tử hóa Phi-3.5 sang INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Kiểm tra**

Cài đặt llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Lưu ý*** 

Nếu bạn dùng Apple Silicon, hãy cài đặt llama-cpp-python như sau


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Kiểm tra


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Tài nguyên**

1. Tìm hiểu thêm về llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Tìm hiểu thêm về onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Tìm hiểu thêm về GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.