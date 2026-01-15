<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:45:10+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "vi"
}
-->
# **Giới thiệu Dịch vụ Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) là dịch vụ đám mây giúp tăng tốc và quản lý vòng đời dự án học máy (ML).

Các chuyên gia ML, nhà khoa học dữ liệu và kỹ sư có thể sử dụng nó trong công việc hàng ngày để:

- Huấn luyện và triển khai mô hình.
- Quản lý các hoạt động học máy (MLOps).
- Bạn có thể tạo mô hình trong Azure Machine Learning hoặc sử dụng mô hình được xây dựng từ các nền tảng mã nguồn mở như PyTorch, TensorFlow hoặc scikit-learn.
- Các công cụ MLOps giúp bạn giám sát, huấn luyện lại và triển khai lại mô hình.

## Azure Machine Learning dành cho ai?

**Nhà khoa học dữ liệu và kỹ sư ML**

Họ có thể sử dụng các công cụ để tăng tốc và tự động hóa quy trình làm việc hàng ngày.
Azure ML cung cấp các tính năng về công bằng, giải thích, theo dõi và kiểm toán.

**Nhà phát triển ứng dụng**

Họ có thể tích hợp mô hình vào ứng dụng hoặc dịch vụ một cách liền mạch.

**Nhà phát triển nền tảng**

Họ có quyền truy cập vào bộ công cụ mạnh mẽ được hỗ trợ bởi các API Azure Resource Manager bền vững.
Những công cụ này cho phép xây dựng các công cụ ML tiên tiến.

**Doanh nghiệp**

Làm việc trên đám mây Microsoft Azure, doanh nghiệp được hưởng lợi từ bảo mật quen thuộc và kiểm soát truy cập dựa trên vai trò.
Thiết lập dự án để kiểm soát quyền truy cập dữ liệu được bảo vệ và các thao tác cụ thể.

## Nâng cao năng suất cho mọi thành viên trong nhóm

Dự án ML thường đòi hỏi một nhóm với nhiều kỹ năng đa dạng để xây dựng và duy trì.

Azure ML cung cấp các công cụ giúp bạn:
- Hợp tác với nhóm qua sổ tay chia sẻ, tài nguyên tính toán, tính toán không máy chủ, dữ liệu và môi trường.
- Phát triển mô hình với các yếu tố công bằng, giải thích, theo dõi và kiểm toán để đáp ứng yêu cầu về nguồn gốc và tuân thủ kiểm toán.
- Triển khai mô hình ML nhanh chóng và dễ dàng ở quy mô lớn, đồng thời quản lý và điều hành hiệu quả với MLOps.
- Chạy các tác vụ học máy ở bất cứ đâu với quản trị, bảo mật và tuân thủ tích hợp sẵn.

## Công cụ nền tảng tương thích chéo

Bất kỳ ai trong nhóm ML cũng có thể sử dụng công cụ ưa thích để hoàn thành công việc.
Dù bạn đang chạy các thí nghiệm nhanh, điều chỉnh siêu tham số, xây dựng pipeline hay quản lý suy luận, bạn có thể dùng các giao diện quen thuộc như:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

Khi bạn tinh chỉnh mô hình và hợp tác trong suốt chu trình phát triển, bạn có thể chia sẻ và tìm kiếm tài sản, tài nguyên và số liệu trong giao diện Azure Machine Learning studio.

## **LLM/SLM trong Azure ML**

Azure ML đã bổ sung nhiều chức năng liên quan đến LLM/SLM, kết hợp LLMOps và SLMOps để tạo ra nền tảng công nghệ trí tuệ nhân tạo tạo sinh trên quy mô doanh nghiệp.

### **Danh mục mô hình**

Người dùng doanh nghiệp có thể triển khai các mô hình khác nhau theo từng kịch bản kinh doanh thông qua Danh mục mô hình, và cung cấp dịch vụ dưới dạng Model as Service để các nhà phát triển hoặc người dùng doanh nghiệp truy cập.

![models](../../../../translated_images/vi/models.e6c7ff50a51806fd.webp)

Danh mục mô hình trong Azure Machine Learning studio là trung tâm để khám phá và sử dụng nhiều loại mô hình giúp bạn xây dựng các ứng dụng Generative AI. Danh mục mô hình có hàng trăm mô hình từ các nhà cung cấp như Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, bao gồm cả các mô hình được Microsoft huấn luyện. Các mô hình từ nhà cung cấp không phải Microsoft được gọi là Non-Microsoft Products, theo Điều khoản Sản phẩm của Microsoft, và chịu các điều khoản đi kèm với mô hình.

### **Pipeline công việc**

Cốt lõi của pipeline học máy là chia một nhiệm vụ học máy hoàn chỉnh thành một quy trình nhiều bước. Mỗi bước là một thành phần có thể quản lý, phát triển, tối ưu, cấu hình và tự động hóa riêng biệt. Các bước được kết nối qua các giao diện được định nghĩa rõ ràng. Dịch vụ pipeline của Azure Machine Learning tự động điều phối tất cả các phụ thuộc giữa các bước trong pipeline.

Khi tinh chỉnh SLM / LLM, chúng ta có thể quản lý dữ liệu, huấn luyện và quy trình tạo ra thông qua Pipeline.

![finetuning](../../../../translated_images/vi/finetuning.6559da198851fa52.webp)

### **Prompt flow**

Lợi ích khi sử dụng Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow mang lại nhiều lợi ích giúp người dùng chuyển từ ý tưởng sang thí nghiệm và cuối cùng là các ứng dụng LLM sẵn sàng sản xuất:

**Linh hoạt trong kỹ thuật prompt**

Trải nghiệm soạn thảo tương tác: Azure Machine Learning prompt flow cung cấp biểu diễn trực quan về cấu trúc luồng, giúp người dùng dễ dàng hiểu và điều hướng dự án. Nó cũng cung cấp trải nghiệm viết mã giống sổ tay để phát triển và gỡ lỗi luồng hiệu quả.  
Các biến thể để điều chỉnh prompt: Người dùng có thể tạo và so sánh nhiều biến thể prompt, hỗ trợ quá trình tinh chỉnh lặp đi lặp lại.

Đánh giá: Các luồng đánh giá tích hợp giúp người dùng đánh giá chất lượng và hiệu quả của prompt và luồng.

Tài nguyên toàn diện: Azure Machine Learning prompt flow bao gồm thư viện công cụ, mẫu và khuôn mẫu tích hợp sẵn làm điểm khởi đầu cho phát triển, kích thích sáng tạo và tăng tốc quá trình.

**Sẵn sàng cho doanh nghiệp với ứng dụng dựa trên LLM**

Hợp tác: Azure Machine Learning prompt flow hỗ trợ làm việc nhóm, cho phép nhiều người cùng tham gia dự án kỹ thuật prompt, chia sẻ kiến thức và duy trì kiểm soát phiên bản.

Nền tảng tất cả trong một: Azure Machine Learning prompt flow đơn giản hóa toàn bộ quy trình kỹ thuật prompt, từ phát triển, đánh giá đến triển khai và giám sát. Người dùng có thể dễ dàng triển khai luồng dưới dạng endpoint Azure Machine Learning và theo dõi hiệu suất theo thời gian thực, đảm bảo hoạt động tối ưu và cải tiến liên tục.

Giải pháp sẵn sàng doanh nghiệp của Azure Machine Learning: Prompt flow tận dụng các giải pháp sẵn sàng doanh nghiệp mạnh mẽ của Azure Machine Learning, cung cấp nền tảng an toàn, mở rộng và đáng tin cậy cho phát triển, thí nghiệm và triển khai luồng.

Với Azure Machine Learning prompt flow, người dùng có thể phát huy sự linh hoạt trong kỹ thuật prompt, hợp tác hiệu quả và tận dụng các giải pháp cấp doanh nghiệp để phát triển và triển khai ứng dụng dựa trên LLM thành công.

Kết hợp sức mạnh tính toán, dữ liệu và các thành phần khác của Azure ML, các nhà phát triển doanh nghiệp có thể dễ dàng xây dựng các ứng dụng trí tuệ nhân tạo riêng của mình.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.