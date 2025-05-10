<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:01:19+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "vi"
}
-->
Bản demo này trình bày cách sử dụng một mô hình đã được huấn luyện sẵn để tạo mã Python dựa trên hình ảnh và đoạn văn bản đầu vào.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Dưới đây là giải thích từng bước:

1. **Imports và Thiết lập**:
   - Các thư viện và module cần thiết được import, bao gồm `requests`, `PIL` để xử lý hình ảnh, và `transformers` để quản lý mô hình và xử lý.

2. **Tải và Hiển thị Hình ảnh**:
   - Một file hình ảnh (`demo.png`) được mở bằng thư viện `PIL` và hiển thị.

3. **Định nghĩa Prompt**:
   - Một thông điệp được tạo ra bao gồm hình ảnh và yêu cầu tạo mã Python để xử lý hình ảnh và lưu lại bằng `plt` (matplotlib).

4. **Tải Processor**:
   - `AutoProcessor` được tải từ mô hình đã được huấn luyện sẵn trong thư mục `out_dir`. Processor này sẽ xử lý đầu vào văn bản và hình ảnh.

5. **Tạo Prompt**:
   - Phương thức `apply_chat_template` được sử dụng để định dạng thông điệp thành prompt phù hợp với mô hình.

6. **Xử lý Đầu vào**:
   - Prompt và hình ảnh được chuyển đổi thành tensor để mô hình có thể hiểu.

7. **Thiết lập Tham số Sinh mã**:
   - Các tham số cho quá trình sinh mã của mô hình được định nghĩa, bao gồm số lượng token mới tối đa và có nên lấy mẫu đầu ra hay không.

8. **Sinh Mã**:
   - Mô hình tạo mã Python dựa trên đầu vào và tham số sinh. `TextStreamer` được dùng để xử lý đầu ra, bỏ qua prompt và các token đặc biệt.

9. **Kết quả**:
   - Mã được tạo ra được in ra, bao gồm mã Python để xử lý hình ảnh và lưu lại như yêu cầu trong prompt.

Bản demo này minh họa cách tận dụng mô hình đã huấn luyện sẵn sử dụng OpenVino để tạo mã một cách động dựa trên đầu vào từ người dùng và hình ảnh.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.