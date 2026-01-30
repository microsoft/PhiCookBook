# **Lượng tử hóa Phi-3.5 sử dụng Intel OpenVINO**

Intel là nhà sản xuất CPU truyền thống với nhiều người dùng. Với sự phát triển của học máy và học sâu, Intel cũng đã tham gia vào cuộc đua tăng tốc AI. Đối với suy luận mô hình, Intel không chỉ sử dụng GPU và CPU mà còn sử dụng NPU.

Chúng tôi hy vọng triển khai Phi-3.x Family ở phía thiết bị cuối, mong muốn trở thành phần quan trọng nhất của AI PC và Copilot PC. Việc tải mô hình ở phía thiết bị cuối phụ thuộc vào sự hợp tác của các nhà sản xuất phần cứng khác nhau. Chương này chủ yếu tập trung vào kịch bản ứng dụng của Intel OpenVINO như một mô hình lượng tử hóa.

## **OpenVINO là gì**

OpenVINO là bộ công cụ mã nguồn mở để tối ưu hóa và triển khai các mô hình học sâu từ đám mây đến thiết bị biên. Nó tăng tốc suy luận học sâu trong nhiều trường hợp sử dụng khác nhau, như AI tạo sinh, video, âm thanh và ngôn ngữ với các mô hình từ các framework phổ biến như PyTorch, TensorFlow, ONNX và nhiều hơn nữa. Chuyển đổi và tối ưu hóa mô hình, đồng thời triển khai trên nhiều phần cứng và môi trường Intel®, tại chỗ hoặc trên thiết bị, trong trình duyệt hoặc trên đám mây.

Giờ đây với OpenVINO, bạn có thể nhanh chóng lượng tử hóa mô hình GenAI trên phần cứng Intel và tăng tốc tham chiếu mô hình.

Hiện OpenVINO hỗ trợ chuyển đổi lượng tử hóa Phi-3.5-Vision và Phi-3.5 Instruct.

### **Cài đặt môi trường**

Vui lòng đảm bảo các phụ thuộc môi trường sau đã được cài đặt, đây là file requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Lượng tử hóa Phi-3.5-Instruct sử dụng OpenVINO**

Trong Terminal, vui lòng chạy script này

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Lượng tử hóa Phi-3.5-Vision sử dụng OpenVINO**

Vui lòng chạy script này trong Python hoặc Jupyter lab

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Mẫu cho Phi-3.5 với Intel OpenVINO**

| Labs    | Giới thiệu | Vào |
| -------- | ------- |  ------- |
| 🚀 Lab-Giới thiệu Phi-3.5 Instruct  | Tìm hiểu cách sử dụng Phi-3.5 Instruct trên AI PC của bạn    |  [Vào](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Giới thiệu Phi-3.5 Vision (hình ảnh) | Tìm hiểu cách sử dụng Phi-3.5 Vision để phân tích hình ảnh trên AI PC của bạn      |  [Vào](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Giới thiệu Phi-3.5 Vision (video)   | Tìm hiểu cách sử dụng Phi-3.5 Vision để phân tích video trên AI PC của bạn    |  [Vào](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Tài nguyên**

1. Tìm hiểu thêm về Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.