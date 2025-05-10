<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:58:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "vi"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo trình diễn WebGPU và Mẫu RAG

Mẫu RAG với mô hình Phi-3.5 Onnx Hosted tận dụng phương pháp Retrieval-Augmented Generation, kết hợp sức mạnh của các mô hình Phi-3.5 với việc lưu trữ ONNX để triển khai AI hiệu quả. Mẫu này rất quan trọng trong việc tinh chỉnh mô hình cho các nhiệm vụ chuyên ngành, mang lại sự kết hợp giữa chất lượng, chi phí hợp lý và khả năng hiểu ngữ cảnh dài. Đây là một phần trong bộ công cụ của Azure AI, cung cấp nhiều lựa chọn mô hình dễ tìm, dễ thử và dễ sử dụng, đáp ứng nhu cầu tùy chỉnh của nhiều ngành công nghiệp khác nhau.

## WebGPU là gì  
WebGPU là API đồ họa web hiện đại được thiết kế để cung cấp truy cập hiệu quả trực tiếp đến GPU (bộ xử lý đồ họa) của thiết bị từ trình duyệt web. Nó được xem là người kế nhiệm của WebGL, mang lại nhiều cải tiến quan trọng:

1. **Tương thích với GPU hiện đại**: WebGPU được xây dựng để hoạt động mượt mà với kiến trúc GPU hiện đại, tận dụng các API hệ thống như Vulkan, Metal và Direct3D 12.
2. **Hiệu suất cải thiện**: Hỗ trợ tính toán GPU đa mục đích và các thao tác nhanh hơn, phù hợp cho cả việc dựng hình đồ họa lẫn các tác vụ học máy.
3. **Tính năng nâng cao**: WebGPU cung cấp truy cập đến các khả năng GPU phức tạp hơn, cho phép xử lý đồ họa và tính toán động và phức tạp hơn.
4. **Giảm tải công việc cho JavaScript**: Bằng cách chuyển nhiều tác vụ sang GPU, WebGPU giảm đáng kể khối lượng công việc trên JavaScript, giúp hiệu suất tốt hơn và trải nghiệm mượt mà hơn.

Hiện tại, WebGPU được hỗ trợ trên các trình duyệt như Google Chrome, và đang được phát triển để mở rộng hỗ trợ sang các nền tảng khác.

### 03.WebGPU  
Môi trường yêu cầu:

**Trình duyệt hỗ trợ:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Bật WebGPU:

- Trên Chrome/Microsoft Edge  

Bật cờ `chrome://flags/#enable-unsafe-webgpu`.

#### Mở trình duyệt của bạn:  
Khởi chạy Google Chrome hoặc Microsoft Edge.

#### Truy cập trang Flags:  
Nhập `chrome://flags` vào thanh địa chỉ và nhấn Enter.

#### Tìm kiếm cờ:  
Trong hộp tìm kiếm phía trên cùng trang, nhập 'enable-unsafe-webgpu'

#### Bật cờ:  
Tìm cờ #enable-unsafe-webgpu trong danh sách kết quả.

Nhấn vào menu thả xuống bên cạnh và chọn Enabled.

#### Khởi động lại trình duyệt:  

Sau khi bật cờ, bạn cần khởi động lại trình duyệt để thay đổi có hiệu lực. Nhấn nút Relaunch xuất hiện ở cuối trang.

- Trên Linux, khởi chạy trình duyệt với `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) đã bật WebGPU mặc định.  
- Trên Firefox Nightly, nhập about:config vào thanh địa chỉ và `set dom.webgpu.enabled to true`.

### Cấu hình GPU cho Microsoft Edge  

Dưới đây là các bước thiết lập GPU hiệu suất cao cho Microsoft Edge trên Windows:

- **Mở Cài đặt:** Nhấn menu Start và chọn Settings.  
- **Cài đặt Hệ thống:** Vào System rồi chọn Display.  
- **Cài đặt Đồ họa:** Kéo xuống và nhấn Graphics settings.  
- **Chọn Ứng dụng:** Trong phần “Choose an app to set preference,” chọn Desktop app rồi nhấn Browse.  
- **Chọn Edge:** Điều hướng đến thư mục cài đặt Edge (thường là `C:\Program Files (x86)\Microsoft\Edge\Application`) và chọn `msedge.exe`.  
- **Thiết lập Ưu tiên:** Nhấn Options, chọn High performance, rồi nhấn Save.  
Điều này đảm bảo Microsoft Edge sẽ sử dụng GPU hiệu suất cao của bạn để tăng hiệu năng.  
- **Khởi động lại** máy tính để các thiết lập có hiệu lực.

### Mẫu thử: Vui lòng [click this link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.