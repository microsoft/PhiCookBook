# **Lượng tử hóa Phi Family sử dụng tiện ích mở rộng Generative AI cho onnxruntime**

## **Generative AI extensions for onnxruntime là gì**

Tiện ích mở rộng này giúp bạn chạy AI sinh tạo với ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Nó cung cấp vòng lặp AI sinh tạo cho các mô hình ONNX, bao gồm suy luận với ONNX Runtime, xử lý logits, tìm kiếm và lấy mẫu, cùng quản lý bộ nhớ đệm KV. Các nhà phát triển có thể gọi phương thức generate() cao cấp, hoặc chạy mỗi vòng lặp của mô hình trong một vòng lặp, sinh ra một token mỗi lần, và tùy chọn cập nhật các tham số sinh tạo bên trong vòng lặp. Nó hỗ trợ tìm kiếm greedy/beam và lấy mẫu TopP, TopK để tạo chuỗi token và xử lý logits tích hợp như phạt lặp lại. Bạn cũng có thể dễ dàng thêm điểm số tùy chỉnh.

Ở cấp ứng dụng, bạn có thể sử dụng Generative AI extensions for onnxruntime để xây dựng ứng dụng bằng C++/ C# / Python. Ở cấp mô hình, bạn có thể dùng nó để hợp nhất các mô hình được tinh chỉnh kỹ và làm các công việc triển khai định lượng liên quan.


## **Lượng tử hóa Phi-3.5 với Generative AI extensions for onnxruntime**

### **Mô hình hỗ trợ**

Generative AI extensions for onnxruntime hỗ trợ chuyển đổi lượng tử các mô hình Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Trình tạo mô hình trong Generative AI extensions for onnxruntime**

Trình tạo mô hình tăng tốc đáng kể việc tạo các mô hình ONNX tối ưu và lượng tử chạy với API generate() của ONNX Runtime.

Qua Model Builder, bạn có thể lượng tử mô hình thành INT4, INT8, FP16, FP32, và kết hợp các phương thức tăng tốc phần cứng khác nhau như CPU, CUDA, DirectML, Mobile, v.v.

Để sử dụng Model Builder, bạn cần cài đặt

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Sau khi cài đặt, bạn có thể chạy script Model Builder từ terminal để thực hiện chuyển đổi định dạng và lượng tử mô hình.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Hiểu các tham số liên quan

1. **model_name** Đây là mô hình trên Hugging face, như microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, v.v. Cũng có thể là đường dẫn nơi bạn lưu mô hình

2. **path_to_output_folder** Đường dẫn lưu file chuyển đổi lượng tử

3. **execution_provider** Hỗ trợ tăng tốc phần cứng khác nhau, như cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Chúng tôi tải mô hình từ Hugging face và lưu cache cục bộ




***Lưu ý：*** <ul>Dù Generative AI extensions for onnxruntime đang ở giai đoạn xem trước, nó đã được tích hợp vào Microsoft Olive, và bạn cũng có thể gọi các chức năng Model Builder của Generative AI extensions for onnxruntime thông qua Microsoft Olive.</ul>

## **Cách sử dụng Model Builder để lượng tử hóa Phi-3.5**

Model Builder hiện hỗ trợ lượng tử mô hình ONNX cho Phi-3.5 Instruct và Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Chuyển đổi lượng tử INT 4 tăng tốc CPU**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Chuyển đổi lượng tử INT 4 tăng tốc CUDA**

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

3. Vui lòng tải các file này vào thư mục Phi-3.5-vision-instruct của bạn

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Tải file này vào thư mục models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Vào terminal

    Chuyển đổi ONNX hỗ trợ FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Lưu ý：**

1. Model Builder hiện chỉ hỗ trợ chuyển đổi Phi-3.5-Instruct và Phi-3.5-Vision, chưa hỗ trợ Phi-3.5-MoE

2. Để sử dụng mô hình lượng tử của ONNX, bạn có thể dùng qua SDK Generative AI extensions for onnxruntime

3. Chúng ta cần cân nhắc AI có trách nhiệm hơn, nên sau chuyển đổi lượng tử mô hình, khuyến nghị tiến hành kiểm tra kết quả hiệu quả hơn

4. Bằng cách lượng tử hóa mô hình CPU INT4, chúng ta có thể triển khai trên thiết bị Edge, có nhiều kịch bản ứng dụng tốt hơn, do đó chúng tôi đã hoàn thành Phi-3.5-Instruct quanh INT 4


## **Tài nguyên**

1. Tìm hiểu thêm về Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repo GitHub của Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->