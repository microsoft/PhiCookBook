<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:19:26+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "vi"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo trình diễn WebGPU và Mô hình RAG
Mô hình RAG với Phi-3 Onnx Hosted tận dụng phương pháp Retrieval-Augmented Generation, kết hợp sức mạnh của các mô hình Phi-3 với việc lưu trữ ONNX để triển khai AI hiệu quả. Mô hình này rất hữu ích trong việc tinh chỉnh các mô hình cho các nhiệm vụ chuyên ngành, mang lại sự kết hợp giữa chất lượng, chi phí hợp lý và khả năng hiểu ngữ cảnh dài. Đây là một phần trong bộ công cụ Azure AI, cung cấp nhiều lựa chọn mô hình dễ dàng tìm kiếm, thử nghiệm và sử dụng, đáp ứng nhu cầu tùy chỉnh của nhiều ngành công nghiệp khác nhau. Các mô hình Phi-3, bao gồm Phi-3-mini, Phi-3-small và Phi-3-medium, có sẵn trên Azure AI Model Catalog và có thể được tinh chỉnh và triển khai tự quản lý hoặc qua các nền tảng như HuggingFace và ONNX, thể hiện cam kết của Microsoft về các giải pháp AI dễ tiếp cận và hiệu quả.

## WebGPU là gì
WebGPU là một API đồ họa web hiện đại được thiết kế để cung cấp truy cập hiệu quả đến bộ xử lý đồ họa (GPU) của thiết bị trực tiếp từ trình duyệt web. Nó được xem là người kế nhiệm của WebGL, với nhiều cải tiến quan trọng:

1. **Tương thích với GPU hiện đại**: WebGPU được xây dựng để hoạt động mượt mà với các kiến trúc GPU hiện đại, tận dụng các API hệ thống như Vulkan, Metal và Direct3D 12.
2. **Hiệu năng nâng cao**: Hỗ trợ tính toán GPU đa mục đích và các thao tác nhanh hơn, phù hợp cho cả việc render đồ họa và các tác vụ học máy.
3. **Tính năng tiên tiến**: WebGPU cung cấp quyền truy cập vào các khả năng GPU phức tạp hơn, cho phép xử lý đồ họa và tính toán động phức tạp hơn.
4. **Giảm tải công việc cho JavaScript**: Bằng cách chuyển nhiều tác vụ hơn sang GPU, WebGPU giảm đáng kể khối lượng công việc trên JavaScript, mang lại hiệu suất tốt hơn và trải nghiệm mượt mà hơn.

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

- Trên Linux, khởi chạy trình duyệt với `--enable-features=Vulkan`.
- Safari 18 (macOS 15) đã bật WebGPU mặc định.
- Trên Firefox Nightly, nhập about:config vào thanh địa chỉ và đặt `dom.webgpu.enabled` thành true.

### Cấu hình GPU cho Microsoft Edge

Dưới đây là các bước để thiết lập GPU hiệu năng cao cho Microsoft Edge trên Windows:

- **Mở Cài đặt:** Nhấn vào menu Start và chọn Settings.
- **Cài đặt Hệ thống:** Vào System rồi chọn Display.
- **Cài đặt Đồ họa:** Kéo xuống và nhấn vào Graphics settings.
- **Chọn Ứng dụng:** Dưới “Choose an app to set preference,” chọn Desktop app rồi nhấn Browse.
- **Chọn Edge:** Điều hướng đến thư mục cài đặt Edge (thường là `C:\Program Files (x86)\Microsoft\Edge\Application`) và chọn `msedge.exe`.
- **Đặt ưu tiên:** Nhấn Options, chọn High performance, rồi nhấn Save.  
Điều này sẽ đảm bảo Microsoft Edge sử dụng GPU hiệu năng cao của bạn để cải thiện hiệu suất.  
- **Khởi động lại** máy tính để các thiết lập có hiệu lực.

### Mở Codespace của bạn:
Đi đến kho lưu trữ trên GitHub của bạn.  
Nhấn nút Code và chọn Open with Codespaces.

Nếu bạn chưa có Codespace, có thể tạo mới bằng cách nhấn New codespace.

**Lưu ý** Cài đặt môi trường Node trong codespace của bạn  
Chạy demo npm từ GitHub Codespace là cách tuyệt vời để kiểm thử và phát triển dự án. Dưới đây là hướng dẫn từng bước để bắt đầu:

### Thiết lập môi trường:
Khi Codespace đã mở, đảm bảo bạn đã cài Node.js và npm. Kiểm tra bằng cách chạy:  
```
node -v
```  
```
npm -v
```

Nếu chưa cài, bạn có thể cài bằng lệnh:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Điều hướng đến thư mục dự án:
Dùng terminal để vào thư mục chứa dự án npm của bạn:  
```
cd path/to/your/project
```

### Cài đặt các phụ thuộc:
Chạy lệnh sau để cài tất cả các phụ thuộc cần thiết trong file package.json:  

```
npm install
```

### Chạy demo:
Sau khi cài xong phụ thuộc, bạn có thể chạy script demo. Thường script này được định nghĩa trong phần scripts của package.json. Ví dụ, nếu script demo tên là start, bạn chạy:  

```
npm run build
```  
```
npm run dev
```

### Truy cập demo:
Nếu demo của bạn có máy chủ web, Codespaces sẽ cung cấp URL để truy cập. Hãy tìm thông báo hoặc kiểm tra tab Ports để lấy URL.

**Lưu ý:** Mô hình cần được lưu trong bộ nhớ đệm trình duyệt, nên có thể mất một chút thời gian để tải.

### Demo RAG
Tải lên file markdown `intro_rag.md` để hoàn thành giải pháp RAG. Nếu dùng codespaces, bạn có thể tải file trong thư mục `01.InferencePhi3/docs/`

### Chọn file của bạn:
Nhấn nút “Choose File” để chọn tài liệu bạn muốn tải lên.

### Tải tài liệu lên:
Sau khi chọn file, nhấn nút “Upload” để tải tài liệu cho RAG (Retrieval-Augmented Generation).

### Bắt đầu trò chuyện:
Khi tài liệu đã được tải lên, bạn có thể bắt đầu phiên chat sử dụng RAG dựa trên nội dung tài liệu đó.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.