<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:41:57+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "vi"
}
-->
# **Xây dựng Visual Studio Code GitHub Copilot Chat của riêng bạn với Microsoft Phi-3 Family**

Bạn đã từng sử dụng workspace agent trong GitHub Copilot Chat chưa? Bạn có muốn tạo một agent mã nguồn cho nhóm của mình? Lab thực hành này hy vọng kết hợp mô hình mã nguồn mở để xây dựng một agent kinh doanh mã nguồn cấp doanh nghiệp.

## **Nền tảng**

### **Tại sao chọn Microsoft Phi-3**

Phi-3 là một dòng sản phẩm, bao gồm phi-3-mini, phi-3-small và phi-3-medium dựa trên các tham số huấn luyện khác nhau cho việc tạo văn bản, hoàn thành hội thoại và tạo mã. Ngoài ra còn có phi-3-vision dựa trên Vision. Nó phù hợp cho các doanh nghiệp hoặc các nhóm khác nhau để tạo ra các giải pháp AI sinh tạo ngoại tuyến.

Khuyến nghị đọc liên kết này [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Tiện ích mở rộng GitHub Copilot Chat cung cấp cho bạn giao diện trò chuyện cho phép bạn tương tác với GitHub Copilot và nhận câu trả lời cho các câu hỏi liên quan đến lập trình ngay trong VS Code, mà không cần phải tìm kiếm tài liệu hay diễn đàn trực tuyến.

Copilot Chat có thể sử dụng tô màu cú pháp, thụt lề và các tính năng định dạng khác để làm rõ câu trả lời được tạo ra. Tùy thuộc vào loại câu hỏi từ người dùng, kết quả có thể bao gồm các liên kết đến ngữ cảnh mà Copilot đã sử dụng để tạo câu trả lời, như các tệp mã nguồn hoặc tài liệu, hoặc các nút để truy cập chức năng của VS Code.

- Copilot Chat tích hợp vào quy trình phát triển của bạn và hỗ trợ bạn khi cần:

- Bắt đầu cuộc trò chuyện trực tiếp ngay trong trình soạn thảo hoặc terminal để được trợ giúp khi đang viết mã

- Sử dụng chế độ Chat để có một trợ lý AI bên cạnh giúp bạn bất cứ lúc nào

- Khởi chạy Quick Chat để hỏi nhanh một câu hỏi và quay lại công việc của bạn ngay lập tức

Bạn có thể sử dụng GitHub Copilot Chat trong nhiều tình huống, chẳng hạn như:

- Trả lời các câu hỏi về lập trình để tìm cách giải quyết vấn đề tốt nhất

- Giải thích mã của người khác và đề xuất cải tiến

- Đề xuất sửa lỗi mã

- Tạo các trường hợp kiểm thử đơn vị

- Tạo tài liệu mã nguồn

Khuyến nghị đọc liên kết này [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Tham chiếu **@workspace** trong Copilot Chat cho phép bạn đặt câu hỏi về toàn bộ mã nguồn của mình. Dựa trên câu hỏi, Copilot sẽ thông minh tìm kiếm các tệp và ký hiệu liên quan, sau đó tham chiếu chúng trong câu trả lời dưới dạng các liên kết và ví dụ mã.

Để trả lời câu hỏi của bạn, **@workspace** tìm kiếm qua các nguồn giống như một nhà phát triển khi duyệt mã trong VS Code:

- Tất cả các tệp trong workspace, ngoại trừ các tệp bị bỏ qua bởi tệp .gitignore

- Cấu trúc thư mục với các thư mục và tên tệp lồng nhau

- Chỉ mục tìm kiếm mã của GitHub, nếu workspace là một kho GitHub và được lập chỉ mục bởi code search

- Các ký hiệu và định nghĩa trong workspace

- Văn bản đang được chọn hoặc văn bản hiển thị trong trình soạn thảo đang hoạt động

Lưu ý: .gitignore sẽ bị bỏ qua nếu bạn đang mở tệp hoặc chọn văn bản trong tệp bị bỏ qua.

Khuyến nghị đọc liên kết này [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Tìm hiểu thêm về Lab này**

GitHub Copilot đã cải thiện đáng kể hiệu suất lập trình của các doanh nghiệp, và mỗi doanh nghiệp đều mong muốn tùy chỉnh các chức năng liên quan của GitHub Copilot. Nhiều doanh nghiệp đã tùy chỉnh các Extension tương tự GitHub Copilot dựa trên các kịch bản kinh doanh riêng và mô hình mã nguồn mở. Đối với doanh nghiệp, các Extension tùy chỉnh dễ kiểm soát hơn, nhưng điều này cũng ảnh hưởng đến trải nghiệm người dùng. Rốt cuộc, GitHub Copilot có chức năng mạnh mẽ hơn trong việc xử lý các kịch bản chung và tính chuyên nghiệp. Nếu trải nghiệm có thể được giữ nhất quán, việc tùy chỉnh Extension riêng của doanh nghiệp sẽ tốt hơn. GitHub Copilot Chat cung cấp các API liên quan để doanh nghiệp mở rộng trải nghiệm Chat. Duy trì trải nghiệm nhất quán và có các chức năng tùy chỉnh là trải nghiệm người dùng tốt hơn.

Lab này chủ yếu sử dụng mô hình Phi-3 kết hợp với NPU cục bộ và Azure hybrid để xây dựng một Agent tùy chỉnh trong GitHub Copilot Chat ***@PHI3*** nhằm hỗ trợ các nhà phát triển doanh nghiệp hoàn thành việc tạo mã ***(@PHI3 /gen)*** và tạo mã dựa trên hình ảnh ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.vi.png)

### ***Lưu ý:***

Lab này hiện được triển khai trên AIPC của Intel CPU và Apple Silicon. Chúng tôi sẽ tiếp tục cập nhật phiên bản NPU của Qualcomm.

## **Lab**

| Tên | Mô tả | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Cài đặt(✅) | Cấu hình và cài đặt môi trường liên quan và công cụ cài đặt | [Đi đến](./HOL/AIPC/01.Installations.md) |[Đi đến](./HOL/Apple/01.Installations.md) |
| Lab1 - Chạy Prompt flow với Phi-3-mini (✅) | Kết hợp với AIPC / Apple Silicon, sử dụng NPU cục bộ để tạo mã qua Phi-3-mini | [Đi đến](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Đi đến](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Triển khai Phi-3-vision trên Azure Machine Learning Service(✅) | Tạo mã bằng cách triển khai Model Catalog của Azure Machine Learning Service - hình ảnh Phi-3-vision | [Đi đến](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Đi đến](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Tạo agent @phi-3 trong GitHub Copilot Chat(✅)  | Tạo agent Phi-3 tùy chỉnh trong GitHub Copilot Chat để hoàn thành tạo mã, tạo mã đồ họa, RAG, v.v. | [Đi đến](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Đi đến](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Mã mẫu (✅)  | Tải mã mẫu | [Đi đến](../../../../../../../code/07.Lab/01/AIPC) | [Đi đến](../../../../../../../code/07.Lab/01/Apple) |

## **Tài nguyên**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Tìm hiểu thêm về GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Tìm hiểu thêm về GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Tìm hiểu thêm về GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Tìm hiểu thêm về Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Tìm hiểu thêm về Model Catalog của Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.