<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:23:23+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "vi"
}
-->
## **Cách sử dụng Model Builder để lượng tử hóa Phi-3.5**

Model Builder hiện hỗ trợ lượng tử hóa mô hình ONNX cho Phi-3.5 Instruct và Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Chuyển đổi lượng tử hóa INT4 tăng tốc bằng CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Chuyển đổi lượng tử hóa INT4 tăng tốc bằng CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Thiết lập môi trường trong terminal

```bash

mkdir models

cd models 

```

2. Tải microsoft/Phi-3.5-vision-instruct vào thư mục models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Vui lòng tải các file này về thư mục Phi-3.5-vision-instruct của bạn

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Tải file này về thư mục models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Vào terminal

    Chuyển đổi ONNX hỗ trợ với FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Lưu ý：**

1. Model Builder hiện chỉ hỗ trợ chuyển đổi Phi-3.5-Instruct và Phi-3.5-Vision, chưa hỗ trợ Phi-3.5-MoE

2. Để sử dụng mô hình lượng tử hóa ONNX, bạn có thể dùng thông qua SDK Generative AI extensions for onnxruntime

3. Cần cân nhắc về AI có trách nhiệm hơn, vì vậy sau khi chuyển đổi lượng tử hóa mô hình, nên tiến hành kiểm tra kết quả hiệu quả hơn

4. Bằng cách lượng tử hóa mô hình CPU INT4, chúng ta có thể triển khai trên thiết bị Edge, phù hợp với nhiều kịch bản ứng dụng hơn, do đó chúng tôi đã hoàn thành Phi-3.5-Instruct với lượng tử hóa INT4

## **Tài nguyên**

1. Tìm hiểu thêm về Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Kho GitHub Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.