# **Xây dựng Visual Studio Code GitHub Copilot Chat của riêng bạn với Microsoft Phi-3 Family**

Bạn đã từng sử dụng workspace agent trong GitHub Copilot Chat chưa? Bạn có muốn xây dựng một agent code cho nhóm của riêng mình? Lab thực hành này hy vọng kết hợp mô hình mã nguồn mở để xây dựng một agent kinh doanh mã cấp doanh nghiệp.

## **Cơ sở**

### **Tại sao chọn Microsoft Phi-3**

Phi-3 là một chuỗi dòng họ, bao gồm phi-3-mini, phi-3-small và phi-3-medium dựa trên các tham số huấn luyện khác nhau cho sinh văn bản, hoàn thành đối thoại và sinh mã. Còn có phi-3-vision dựa trên Vision. Nó phù hợp cho các doanh nghiệp hoặc các nhóm khác nhau để tạo các giải pháp AI sinh ngoại tuyến.

Khuyến nghị đọc liên kết này [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Tiện ích mở rộng GitHub Copilot Chat cung cấp cho bạn một giao diện chat cho phép bạn tương tác với GitHub Copilot và nhận câu trả lời cho các câu hỏi liên quan đến lập trình trực tiếp trong VS Code, mà không cần phải điều hướng tài liệu hay tìm kiếm trên các diễn đàn trực tuyến.

Copilot Chat có thể sử dụng tô sáng cú pháp, thụt lề và các tính năng định dạng khác để làm rõ câu trả lời được tạo ra. Tùy thuộc vào loại câu hỏi từ người dùng, kết quả có thể chứa các liên kết đến ngữ cảnh mà Copilot đã sử dụng để tạo câu trả lời, chẳng hạn như tệp mã nguồn hoặc tài liệu, hoặc các nút để truy cập chức năng của VS Code.

- Copilot Chat tích hợp trong luồng làm việc của nhà phát triển và hỗ trợ bạn khi cần:

- Bắt đầu một cuộc trò chuyện trực tiếp từ trình soạn thảo hoặc terminal để được giúp đỡ khi bạn đang lập trình

- Sử dụng chế độ Chat để có trợ lý AI bên cạnh giúp bạn bất cứ lúc nào

- Khởi chạy Quick Chat để hỏi nhanh một câu hỏi và trở lại công việc của bạn ngay

Bạn có thể sử dụng GitHub Copilot Chat trong nhiều trường hợp khác nhau, như:

- Trả lời các câu hỏi lập trình về cách giải quyết vấn đề tốt nhất

- Giải thích mã của người khác và đề xuất cải tiến

- Đề xuất sửa lỗi mã

- Sinh các trường hợp kiểm thử đơn vị

- Tạo tài liệu cho mã

Khuyến nghị đọc liên kết này [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Tham chiếu **@workspace** trong Copilot Chat cho phép bạn đặt câu hỏi về toàn bộ cơ sở mã của mình. Dựa vào câu hỏi, Copilot sẽ thông minh lấy các tệp và ký hiệu liên quan, sau đó tham chiếu chúng trong câu trả lời dưới dạng liên kết và ví dụ mã.

Để trả lời câu hỏi của bạn, **@workspace** tìm kiếm qua các nguồn tương tự như một nhà phát triển khi điều hướng mã trong VS Code:

- Tất cả các tệp trong workspace, ngoại trừ các tệp bị bỏ qua bởi tệp .gitignore

- Cấu trúc thư mục với các thư mục và tên tệp lồng nhau

- Chỉ mục tìm kiếm mã của GitHub, nếu workspace là kho lưu trữ GitHub và được chỉ mục bởi tìm kiếm mã

- Các ký hiệu và định nghĩa trong workspace

- Văn bản đang được chọn hoặc văn bản hiển thị trong trình soạn thảo đang hoạt động

Lưu ý: .gitignore sẽ bị bỏ qua nếu bạn mở một tệp hoặc có văn bản được chọn trong tệp bị bỏ qua.

Khuyến nghị đọc liên kết này [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Tìm hiểu thêm về Lab này**

GitHub Copilot đã cải thiện đáng kể hiệu quả lập trình của doanh nghiệp, và mỗi doanh nghiệp đều hy vọng tùy chỉnh các chức năng liên quan của GitHub Copilot. Nhiều doanh nghiệp đã tùy chỉnh Extensions tương tự GitHub Copilot dựa trên các kịch bản kinh doanh và mô hình mã nguồn mở của riêng họ. Với doanh nghiệp, Extensions tùy chỉnh dễ kiểm soát hơn, nhưng điều này cũng ảnh hưởng đến trải nghiệm người dùng. Rốt cuộc, GitHub Copilot có chức năng mạnh mẽ hơn trong xử lý các kịch bản chung và chuyên nghiệp. Nếu trải nghiệm có thể được giữ nhất quán, tùy chỉnh Extension riêng của doanh nghiệp sẽ tốt hơn. GitHub Copilot Chat cung cấp các API liên quan để doanh nghiệp mở rộng trải nghiệm Chat. Duy trì trải nghiệm nhất quán và có các chức năng tùy chỉnh sẽ mang lại trải nghiệm người dùng tốt hơn.

Lab này chủ yếu sử dụng mô hình Phi-3 kết hợp với NPU cục bộ và hybrid Azure để xây dựng Agent tùy chỉnh trong GitHub Copilot Chat ***@PHI3*** hỗ trợ các nhà phát triển doanh nghiệp hoàn thành sinh mã ***(@PHI3 /gen)*** và sinh mã dựa trên hình ảnh ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/vi/cover.1017ebc9a7c46d09.webp)

### ***Lưu ý:***

Lab hiện được triển khai trên AIPC của CPU Intel và Apple Silicon. Chúng tôi sẽ tiếp tục cập nhật phiên bản Qualcomm của NPU.


## **Lab**


| Tên | Mô tả | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Cài đặt (✅) | Cấu hình và cài đặt các môi trường và công cụ liên quan | [Đi đến](./HOL/AIPC/01.Installations.md) |[Đi đến](./HOL/Apple/01.Installations.md) |
| Lab1 - Chạy Prompt flow với Phi-3-mini (✅) | Kết hợp với AIPC / Apple Silicon, sử dụng NPU cục bộ để tạo sinh mã qua Phi-3-mini | [Đi đến](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Đi đến](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Triển khai Phi-3-vision trên Azure Machine Learning Service(✅) | Sinh mã bằng cách triển khai Model Catalog của Azure Machine Learning Service - hình ảnh Phi-3-vision | [Đi đến](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Đi đến](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Tạo agent @phi-3 trong GitHub Copilot Chat(✅)  | Tạo agent Phi-3 tùy chỉnh trong GitHub Copilot Chat để hoàn thành sinh mã, sinh mã đồ họa, RAG, v.v. | [Đi đến](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Đi đến](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Mã mẫu (✅)  | Tải về mã mẫu | [Đi đến](../../../../../../../code/07.Lab/01/AIPC) | [Đi đến](../../../../../../../code/07.Lab/01/Apple) |


## **Tài nguyên**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Tìm hiểu thêm về GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Tìm hiểu thêm về GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Tìm hiểu thêm về GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Tìm hiểu thêm về Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Tìm hiểu thêm về Model Catalog của Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo tính chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->