# **Sử dụng Phi-3 trong Azure AI Foundry**

Với sự phát triển của Generative AI, chúng ta mong muốn sử dụng một nền tảng thống nhất để quản lý các LLM và SLM khác nhau, tích hợp dữ liệu doanh nghiệp, thực hiện fine-tuning/RAG, và đánh giá các hoạt động kinh doanh sau khi tích hợp LLM và SLM, nhằm giúp các ứng dụng AI tạo sinh được triển khai thông minh hơn. [Azure AI Foundry](https://ai.azure.com) là nền tảng ứng dụng AI tạo sinh cấp doanh nghiệp.

![aistudo](../../../../translated_images/vi/aifoundry_home.f28a8127c96c7d93.webp)

Với Azure AI Foundry, bạn có thể đánh giá phản hồi của các mô hình ngôn ngữ lớn (LLM) và điều phối các thành phần ứng dụng prompt bằng prompt flow để nâng cao hiệu suất. Nền tảng này hỗ trợ mở rộng dễ dàng, giúp chuyển đổi các bằng chứng khái niệm thành sản phẩm hoàn chỉnh. Việc giám sát và tinh chỉnh liên tục giúp đảm bảo thành công lâu dài.

Chúng ta có thể nhanh chóng triển khai mô hình Phi-3 trên Azure AI Foundry qua các bước đơn giản, sau đó sử dụng Azure AI Foundry để hoàn thành các công việc liên quan đến Playground/Chat, Fine-tuning, đánh giá Phi-3.

## **1. Chuẩn bị**

Nếu bạn đã cài đặt [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) trên máy, việc sử dụng mẫu này rất đơn giản, chỉ cần chạy lệnh này trong thư mục mới.

## Tạo thủ công

Tạo một dự án và hub trong Microsoft Azure AI Foundry là cách tuyệt vời để tổ chức và quản lý công việc AI của bạn. Dưới đây là hướng dẫn từng bước để bạn bắt đầu:

### Tạo dự án trong Azure AI Foundry

1. **Truy cập Azure AI Foundry**: Đăng nhập vào cổng Azure AI Foundry.
2. **Tạo dự án**:
   - Nếu bạn đang trong một dự án, chọn "Azure AI Foundry" ở góc trên bên trái trang để về trang Chủ.
   - Chọn "+ Create project".
   - Nhập tên cho dự án.
   - Nếu bạn đã có hub, nó sẽ được chọn mặc định. Nếu bạn có quyền truy cập nhiều hub, bạn có thể chọn hub khác từ danh sách thả xuống. Nếu muốn tạo hub mới, chọn "Create new hub" và nhập tên.
   - Chọn "Create".

### Tạo hub trong Azure AI Foundry

1. **Truy cập Azure AI Foundry**: Đăng nhập bằng tài khoản Azure của bạn.
2. **Tạo hub**:
   - Chọn Trung tâm Quản lý (Management center) từ menu bên trái.
   - Chọn "All resources", sau đó nhấn mũi tên xuống bên cạnh "+ New project" và chọn "+ New hub".
   - Trong hộp thoại "Create a new hub", nhập tên cho hub của bạn (ví dụ: contoso-hub) và điều chỉnh các trường khác theo ý muốn.
   - Chọn "Next", xem lại thông tin, rồi chọn "Create".

Để biết hướng dẫn chi tiết hơn, bạn có thể tham khảo tài liệu chính thức của [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Sau khi tạo thành công, bạn có thể truy cập studio bạn đã tạo qua [ai.azure.com](https://ai.azure.com/)

Có thể có nhiều dự án trên một AI Foundry. Hãy tạo dự án trong AI Foundry để chuẩn bị.

Tạo Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Triển khai mô hình Phi trên Azure AI Foundry**

Nhấn vào tùy chọn Explore của dự án để vào Model Catalog và chọn Phi-3

Chọn Phi-3-mini-4k-instruct

Nhấn 'Deploy' để triển khai mô hình Phi-3-mini-4k-instruct

> [!NOTE]
>
> Bạn có thể chọn công suất tính toán khi triển khai

## **3. Playground Chat Phi trong Azure AI Foundry**

Vào trang triển khai, chọn Playground và trò chuyện với Phi-3 của Azure AI Foundry

## **4. Triển khai mô hình từ Azure AI Foundry**

Để triển khai mô hình từ Azure Model Catalog, bạn có thể làm theo các bước sau:

- Đăng nhập vào Azure AI Foundry.
- Chọn mô hình bạn muốn triển khai từ catalog mô hình của Azure AI Foundry.
- Trên trang Chi tiết mô hình, chọn Deploy rồi chọn Serverless API với Azure AI Content Safety.
- Chọn dự án mà bạn muốn triển khai mô hình. Để sử dụng Serverless API, workspace của bạn phải thuộc khu vực East US 2 hoặc Sweden Central. Bạn có thể tùy chỉnh tên Deployment.
- Trên trình hướng dẫn triển khai, chọn Pricing and terms để tìm hiểu về giá cả và điều khoản sử dụng.
- Chọn Deploy. Chờ đến khi triển khai hoàn tất và bạn được chuyển đến trang Deployments.
- Chọn Open in playground để bắt đầu tương tác với mô hình.
- Bạn có thể quay lại trang Deployments, chọn deployment và ghi lại Target URL của endpoint và Secret Key, dùng để gọi deployment và tạo kết quả.
- Bạn luôn có thể tìm thông tin chi tiết về endpoint, URL và khóa truy cập bằng cách vào tab Build và chọn Deployments trong phần Components.

> [!NOTE]
> Lưu ý rằng tài khoản của bạn phải có quyền Azure AI Developer trên Resource Group để thực hiện các bước này.

## **5. Sử dụng Phi API trong Azure AI Foundry**

Bạn có thể truy cập https://{Tên dự án của bạn}.region.inference.ml.azure.com/swagger.json qua Postman GET và kết hợp với Key để tìm hiểu các giao diện được cung cấp

Bạn có thể lấy tham số yêu cầu rất thuận tiện, cũng như các tham số phản hồi.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.