Bản demo này trình bày cách sử dụng một mô hình đã được huấn luyện trước để tạo mã Python dựa trên hình ảnh và lời nhắc văn bản.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Dưới đây là giải thích từng bước:

1. **Nhập khẩu và Thiết lập**:
   - Các thư viện và module cần thiết được nhập, bao gồm `requests`, `PIL` để xử lý hình ảnh, và `transformers` để quản lý mô hình và xử lý.

2. **Tải và Hiển thị Hình ảnh**:
   - Một tệp hình ảnh (`demo.png`) được mở bằng thư viện `PIL` và hiển thị.

3. **Định nghĩa Lời nhắc**:
   - Một thông điệp được tạo ra bao gồm hình ảnh và yêu cầu tạo mã Python để xử lý hình ảnh và lưu lại bằng `plt` (matplotlib).

4. **Tải Bộ Xử lý**:
   - `AutoProcessor` được tải từ mô hình đã huấn luyện trước được chỉ định bởi thư mục `out_dir`. Bộ xử lý này sẽ xử lý đầu vào văn bản và hình ảnh.

5. **Tạo Lời nhắc**:
   - Phương thức `apply_chat_template` được sử dụng để định dạng thông điệp thành lời nhắc phù hợp với mô hình.

6. **Xử lý Đầu vào**:
   - Lời nhắc và hình ảnh được xử lý thành tensor mà mô hình có thể hiểu.

7. **Thiết lập Tham số Sinh mã**:
   - Các tham số cho quá trình sinh mã của mô hình được định nghĩa, bao gồm số lượng token mới tối đa cần tạo và có nên lấy mẫu đầu ra hay không.

8. **Sinh Mã**:
   - Mô hình tạo mã Python dựa trên đầu vào và tham số sinh mã. `TextStreamer` được sử dụng để xử lý đầu ra, bỏ qua lời nhắc và các token đặc biệt.

9. **Kết quả**:
   - Mã được tạo ra được in ra, bao gồm mã Python để xử lý hình ảnh và lưu lại như đã yêu cầu trong lời nhắc.

Bản demo này minh họa cách tận dụng mô hình đã huấn luyện trước sử dụng OpenVino để tạo mã một cách linh hoạt dựa trên đầu vào của người dùng và hình ảnh.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.