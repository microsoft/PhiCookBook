# **Sử dụng Phi-3 trong Microsoft Foundry**

Với sự phát triển của Generative AI, chúng ta hy vọng sử dụng một nền tảng thống nhất để quản lý các LLM và SLM khác nhau, tích hợp dữ liệu doanh nghiệp, các hoạt động fine-tuning/RAG, và đánh giá các lĩnh vực kinh doanh doanh nghiệp sau khi tích hợp LLM và SLM, v.v., để các ứng dụng AI tạo sinh được triển khai một cách thông minh hơn. [Microsoft Foundry](https://ai.azure.com) là nền tảng ứng dụng AI tạo sinh cấp doanh nghiệp.

![aistudo](../../../../translated_images/vi/aifoundry_home.f28a8127c96c7d93.webp)

Với Microsoft Foundry, bạn có thể đánh giá phản hồi của mô hình ngôn ngữ lớn (LLM) và sắp xếp các thành phần ứng dụng prompt với prompt flow để đạt hiệu suất tốt hơn. Nền tảng này hỗ trợ khả năng mở rộng để chuyển đổi các bằng chứng khái niệm thành sản xuất hoàn chỉnh một cách dễ dàng. Việc giám sát liên tục và cải tiến hỗ trợ thành công lâu dài.

Chúng ta có thể nhanh chóng triển khai mô hình Phi-3 trên Microsoft Foundry thông qua các bước đơn giản, rồi sử dụng Microsoft Foundry để hoàn thành các công việc liên quan đến Playground/Chat, fine-tuning, đánh giá Phi-3.

## **1. Chuẩn bị**

Nếu bạn đã cài đặt [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) trên máy của mình, việc sử dụng mẫu này đơn giản chỉ là chạy lệnh này trong một thư mục mới.

## Tạo thủ công

Tạo một dự án và hub trên Microsoft Foundry là cách tuyệt vời để tổ chức và quản lý công việc AI của bạn. Dưới đây là hướng dẫn từng bước để bạn bắt đầu:

### Tạo Dự án trong Microsoft Foundry

1. **Đăng nhập Microsoft Foundry**: Đăng nhập vào cổng thông tin Microsoft Foundry.
2. **Tạo một Dự án**:
   - Nếu đang ở trong một dự án, chọn "Microsoft Foundry" ở góc trên bên trái trang để về trang chủ.
   - Chọn "+ Create project".
   - Nhập tên cho dự án.
   - Nếu bạn có một hub, nó sẽ được chọn mặc định. Nếu bạn có quyền truy cập nhiều hơn một hub, bạn có thể chọn hub khác từ danh sách thả xuống. Nếu muốn tạo một hub mới, chọn "Create new hub" và điền tên.
   - Chọn "Create".

### Tạo một Hub trong Microsoft Foundry

1. **Đăng nhập Microsoft Foundry**: Đăng nhập bằng tài khoản Azure của bạn.
2. **Tạo một Hub**:
   - Chọn Trung tâm Quản lý từ menu bên trái.
   - Chọn "All resources", sau đó mũi tên xuống bên cạnh "+ New project" và chọn "+ New hub".
   - Trong hộp thoại "Create a new hub", nhập tên cho hub của bạn (ví dụ: contoso-hub) và sửa các trường khác theo ý muốn.
   - Chọn "Next", xem lại thông tin, rồi chọn "Create".

Để biết thêm hướng dẫn chi tiết, bạn có thể tham khảo tài liệu chính thức của [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Sau khi tạo thành công, bạn có thể truy cập studio bạn tạo qua [ai.azure.com](https://ai.azure.com/)

Có thể có nhiều dự án trên một AI Foundry. Hãy tạo dự án trong AI Foundry để chuẩn bị.

Tạo Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Triển khai mô hình Phi trong Microsoft Foundry**

Nhấn chọn Explore của dự án để vào Model Catalog và chọn Phi-3

Chọn Phi-3-mini-4k-instruct

Nhấn 'Deploy' để triển khai mô hình Phi-3-mini-4k-instruct

> [!NOTE]
>
> Bạn có thể chọn công suất tính toán khi triển khai

## **3. Playground Chat Phi trong Microsoft Foundry**

Đi đến trang triển khai, chọn Playground, và trò chuyện với Phi-3 của Microsoft Foundry

## **4. Triển khai Mô hình từ Microsoft Foundry**

Để triển khai một mô hình từ Azure Model Catalog, bạn có thể làm theo các bước sau:

- Đăng nhập Microsoft Foundry.
- Chọn mô hình bạn muốn triển khai từ danh mục mô hình Microsoft Foundry.
- Ở trang Chi tiết của mô hình, chọn Deploy rồi chọn Serverless API với Azure AI Content Safety.
- Chọn dự án bạn muốn triển khai mô hình. Để sử dụng dịch vụ Serverless API, workspace của bạn phải thuộc khu vực East US 2 hoặc Sweden Central. Bạn có thể tùy chỉnh tên Deployment.
- Trên trình hướng dẫn triển khai, chọn Pricing and terms để tìm hiểu về giá cả và điều khoản sử dụng.
- Chọn Deploy. Chờ cho đến khi triển khai xong và bạn được chuyển đến trang Deployments.
- Chọn Open in playground để bắt đầu tương tác với mô hình.
- Bạn có thể quay lại trang Deployments, chọn triển khai, và lấy URL đích cùng Khóa bí mật, bạn có thể dùng chúng để gọi triển khai và tạo kết quả.
- Bạn luôn có thể xem chi tiết endpoint, URL, và khóa truy cập bằng cách chuyển tới tab Build và chọn Deployments trong phần Components.

> [!NOTE]
> Vui lòng lưu ý bạn phải có quyền Azure AI Developer trên Resource Group để thực hiện các bước này.

## **5. Sử dụng Phi API trong Microsoft Foundry**

Bạn có thể truy cập https://{Tên dự án của bạn}.region.inference.ml.azure.com/swagger.json thông qua Postman GET và kết hợp với Key để tìm hiểu về các giao diện được cung cấp

Bạn có thể lấy tham số yêu cầu rất tiện lợi, cũng như tham số phản hồi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên Bố Miễn Trách Nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ mẹ đẻ của nó nên được coi là nguồn chính xác nhất. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hay diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->