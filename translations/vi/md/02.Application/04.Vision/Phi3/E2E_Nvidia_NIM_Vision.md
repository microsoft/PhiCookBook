<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:57:26+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "vi"
}
-->
### Kịch Bản Ví Dụ

Hãy tưởng tượng bạn có một hình ảnh (`demo.png`) và bạn muốn tạo mã Python để xử lý hình ảnh này và lưu lại phiên bản mới của nó (`phi-3-vision.jpg`).

Đoạn mã trên tự động hóa quy trình này bằng cách:

1. Thiết lập môi trường và các cấu hình cần thiết.
2. Tạo một prompt hướng dẫn mô hình tạo mã Python cần thiết.
3. Gửi prompt đến mô hình và thu thập mã được tạo ra.
4. Trích xuất và chạy mã đã tạo.
5. Hiển thị hình ảnh gốc và hình ảnh đã xử lý.

Cách tiếp cận này tận dụng sức mạnh của AI để tự động hóa các tác vụ xử lý hình ảnh, giúp bạn thực hiện mục tiêu nhanh hơn và dễ dàng hơn.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Hãy cùng phân tích từng bước của toàn bộ đoạn mã:

1. **Cài Đặt Gói Cần Thiết**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Lệnh này cài đặt gói `langchain_nvidia_ai_endpoints`, đảm bảo rằng bạn có phiên bản mới nhất.

2. **Nhập Các Module Cần Thiết**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Các import này đưa vào các module cần thiết để tương tác với các endpoint AI của NVIDIA, xử lý mật khẩu một cách an toàn, tương tác với hệ điều hành, và mã hóa/giải mã dữ liệu theo định dạng base64.

3. **Thiết Lập API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Đoạn mã này kiểm tra xem biến môi trường `NVIDIA_API_KEY` đã được thiết lập chưa. Nếu chưa, nó sẽ yêu cầu người dùng nhập API key một cách bảo mật.

4. **Định Nghĩa Model và Đường Dẫn Hình Ảnh**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Đoạn này thiết lập model sẽ sử dụng, tạo một thể hiện của `ChatNVIDIA` với model đã chỉ định, và định nghĩa đường dẫn đến file hình ảnh.

5. **Tạo Prompt Văn Bản**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Đoạn này định nghĩa một prompt văn bản hướng dẫn mô hình tạo mã Python để xử lý hình ảnh.

6. **Mã Hóa Hình Ảnh Dưới Dạng Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Đoạn mã này đọc file hình ảnh, mã hóa nó dưới dạng base64, và tạo một thẻ hình ảnh HTML với dữ liệu đã mã hóa.

7. **Kết Hợp Văn Bản và Hình Ảnh Thành Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Đoạn này kết hợp prompt văn bản và thẻ hình ảnh HTML thành một chuỗi duy nhất.

8. **Tạo Mã Bằng ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Đoạn mã này gửi prompt đến mô hình `ChatNVIDIA` và thu thập mã được tạo ra theo từng phần, in ra và nối từng phần vào biến `code`.

9. **Trích Xuất Mã Python Từ Nội Dung Được Tạo**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Đoạn này trích xuất mã Python thực tế từ nội dung được tạo ra bằng cách loại bỏ định dạng markdown.

10. **Chạy Mã Đã Tạo**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Đoạn này chạy mã Python đã trích xuất dưới dạng một subprocess và thu thập kết quả đầu ra.

11. **Hiển Thị Hình Ảnh**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Các dòng này hiển thị hình ảnh bằng cách sử dụng module `IPython.display`.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.