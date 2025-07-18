<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:11:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "vi"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo trình diễn WebGPU và Mẫu RAG

Mẫu RAG với mô hình Phi-3.5 Onnx Hosted tận dụng phương pháp Retrieval-Augmented Generation, kết hợp sức mạnh của các mô hình Phi-3.5 với việc lưu trữ ONNX để triển khai AI hiệu quả. Mẫu này rất hữu ích trong việc tinh chỉnh mô hình cho các nhiệm vụ chuyên ngành, mang lại sự kết hợp giữa chất lượng, chi phí hợp lý và khả năng hiểu ngữ cảnh dài. Đây là một phần trong bộ công cụ Azure AI, cung cấp nhiều lựa chọn mô hình dễ tìm, dễ thử và dễ sử dụng, đáp ứng nhu cầu tùy chỉnh của nhiều ngành công nghiệp khác nhau.

## WebGPU là gì  
WebGPU là một API đồ họa web hiện đại được thiết kế để cung cấp quyền truy cập hiệu quả vào bộ xử lý đồ họa (GPU) của thiết bị trực tiếp từ trình duyệt web. Nó được xem là người kế nhiệm của WebGL, mang lại một số cải tiến quan trọng:

1. **Tương thích với GPU hiện đại**: WebGPU được xây dựng để hoạt động mượt mà với các kiến trúc GPU hiện đại, tận dụng các API hệ thống như Vulkan, Metal và Direct3D 12.
2. **Hiệu năng nâng cao**: Hỗ trợ tính toán GPU đa mục đích và các thao tác nhanh hơn, phù hợp cho cả việc render đồ họa và các tác vụ học máy.
3. **Tính năng tiên tiến**: WebGPU cung cấp quyền truy cập vào các khả năng GPU phức tạp hơn, cho phép xử lý đồ họa và tính toán động phức tạp hơn.
4. **Giảm tải cho JavaScript**: Bằng cách chuyển nhiều tác vụ hơn sang GPU, WebGPU giảm đáng kể khối lượng công việc trên JavaScript, giúp cải thiện hiệu suất và trải nghiệm mượt mà hơn.

Hiện tại, WebGPU được hỗ trợ trên các trình duyệt như Google Chrome, với các nỗ lực mở rộng hỗ trợ sang các nền tảng khác.

### 03.WebGPU  
Môi trường yêu cầu:

**Trình duyệt được hỗ trợ:**  
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Kích hoạt WebGPU:

- Trên Chrome/Microsoft Edge

Bật cờ `chrome://flags/#enable-unsafe-webgpu`.

#### Mở trình duyệt của bạn:  
Khởi chạy Google Chrome hoặc Microsoft Edge.

#### Truy cập trang Flags:  
Gõ `chrome://flags` vào thanh địa chỉ và nhấn Enter.

#### Tìm kiếm cờ:  
Trong ô tìm kiếm ở đầu trang, nhập 'enable-unsafe-webgpu'

#### Bật cờ:  
Tìm cờ #enable-unsafe-webgpu trong danh sách kết quả.

Nhấn vào menu thả xuống bên cạnh và chọn Enabled.

#### Khởi động lại trình duyệt:  

Sau khi bật cờ, bạn cần khởi động lại trình duyệt để thay đổi có hiệu lực. Nhấn nút Relaunch xuất hiện ở cuối trang.

- Với Linux, khởi chạy trình duyệt với `--enable-features=Vulkan`.
- Safari 18 (macOS 15) đã bật WebGPU mặc định.
- Trên Firefox Nightly, nhập about:config vào thanh địa chỉ và đặt `dom.webgpu.enabled` thành true.

### Cấu hình GPU cho Microsoft Edge  

Dưới đây là các bước để thiết lập GPU hiệu năng cao cho Microsoft Edge trên Windows:

- **Mở Cài đặt:** Nhấn vào menu Start và chọn Settings.
- **Cài đặt Hệ thống:** Vào System rồi chọn Display.
- **Cài đặt Đồ họa:** Kéo xuống và nhấn vào Graphics settings.
- **Chọn Ứng dụng:** Trong phần “Choose an app to set preference,” chọn Desktop app rồi nhấn Browse.
- **Chọn Edge:** Điều hướng đến thư mục cài đặt Edge (thường là `C:\Program Files (x86)\Microsoft\Edge\Application`) và chọn `msedge.exe`.
- **Đặt ưu tiên:** Nhấn Options, chọn High performance, rồi nhấn Save.  
Điều này sẽ đảm bảo Microsoft Edge sử dụng GPU hiệu năng cao của bạn để cải thiện hiệu suất.  
- **Khởi động lại** máy tính để các thiết lập có hiệu lực.

### Mẫu thử: Vui lòng [nhấn vào liên kết này](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.