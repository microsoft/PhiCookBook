<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:17:01+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "vi"
}
-->
# **Giới thiệu Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) là một công cụ tự động hóa quy trình làm việc trực quan, cho phép người dùng tạo các quy trình tự động sử dụng các mẫu có sẵn và kết nối tùy chỉnh. Nó được thiết kế để giúp các nhà phát triển và chuyên viên phân tích kinh doanh nhanh chóng xây dựng các quy trình tự động cho các nhiệm vụ như quản lý dữ liệu, hợp tác và tối ưu hóa quy trình. Với Prompt Flow, người dùng có thể dễ dàng kết nối các dịch vụ, ứng dụng và hệ thống khác nhau, đồng thời tự động hóa các quy trình kinh doanh phức tạp.

Microsoft Prompt Flow được thiết kế nhằm đơn giản hóa toàn bộ chu trình phát triển ứng dụng AI dựa trên các Mô hình Ngôn ngữ Lớn (LLMs). Dù bạn đang lên ý tưởng, tạo mẫu, thử nghiệm, đánh giá hay triển khai các ứng dụng dựa trên LLM, Prompt Flow giúp quá trình này trở nên dễ dàng và cho phép bạn xây dựng các ứng dụng LLM với chất lượng sản xuất.

## Dưới đây là những tính năng và lợi ích chính khi sử dụng Microsoft Prompt Flow:

**Trải nghiệm soạn thảo tương tác**

Prompt Flow cung cấp hình ảnh trực quan về cấu trúc luồng của bạn, giúp bạn dễ dàng hiểu và điều hướng dự án.
Nó mang đến trải nghiệm viết mã giống như sổ tay giúp phát triển và gỡ lỗi luồng hiệu quả.

**Các biến thể Prompt và điều chỉnh**

Tạo và so sánh nhiều biến thể prompt để hỗ trợ quá trình tinh chỉnh lặp đi lặp lại. Đánh giá hiệu suất của các prompt khác nhau và chọn ra những prompt hiệu quả nhất.

**Luồng đánh giá tích hợp sẵn**

Đánh giá chất lượng và hiệu quả của prompt và luồng bằng các công cụ đánh giá tích hợp sẵn.
Hiểu được mức độ hoạt động của các ứng dụng dựa trên LLM của bạn.

**Tài nguyên toàn diện**

Prompt Flow bao gồm thư viện công cụ, mẫu và khuôn mẫu tích hợp sẵn. Những tài nguyên này giúp bạn có điểm khởi đầu cho việc phát triển, truyền cảm hứng sáng tạo và tăng tốc quá trình.

**Hợp tác và sẵn sàng cho doanh nghiệp**

Hỗ trợ làm việc nhóm bằng cách cho phép nhiều người dùng cùng làm việc trên các dự án kỹ thuật prompt.
Duy trì kiểm soát phiên bản và chia sẻ kiến thức hiệu quả. Đơn giản hóa toàn bộ quy trình kỹ thuật prompt, từ phát triển, đánh giá đến triển khai và giám sát.

## Đánh giá trong Prompt Flow

Trong Microsoft Prompt Flow, đánh giá đóng vai trò quan trọng trong việc xác định hiệu suất của các mô hình AI. Hãy cùng khám phá cách bạn có thể tùy chỉnh các luồng đánh giá và các chỉ số trong Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.vi.png)

**Hiểu về đánh giá trong Prompt Flow**

Trong Prompt Flow, một luồng đại diện cho chuỗi các nút xử lý đầu vào và tạo ra đầu ra. Các luồng đánh giá là các luồng đặc biệt được thiết kế để đánh giá hiệu suất của một lần chạy dựa trên các tiêu chí và mục tiêu cụ thể.

**Các tính năng chính của luồng đánh giá**

Chúng thường chạy sau luồng đang được kiểm tra, sử dụng đầu ra của luồng đó. Chúng tính toán điểm số hoặc các chỉ số để đo hiệu quả của luồng được kiểm tra. Các chỉ số có thể bao gồm độ chính xác, điểm liên quan, hoặc bất kỳ thước đo phù hợp nào khác.

### Tùy chỉnh Luồng Đánh giá

**Định nghĩa đầu vào**

Các luồng đánh giá cần nhận đầu ra của lần chạy đang được kiểm tra. Định nghĩa đầu vào tương tự như các luồng thông thường.
Ví dụ, nếu bạn đánh giá luồng QnA, đặt tên đầu vào là "answer". Nếu đánh giá luồng phân loại, đặt tên đầu vào là "category". Có thể cần cả đầu vào dữ liệu chuẩn (ví dụ: nhãn thực tế).

**Đầu ra và chỉ số**

Các luồng đánh giá tạo ra kết quả đo lường hiệu suất của luồng được kiểm tra. Các chỉ số có thể được tính toán bằng Python hoặc LLM (Mô hình Ngôn ngữ Lớn). Sử dụng hàm log_metric() để ghi lại các chỉ số liên quan.

**Sử dụng Luồng Đánh giá Tùy chỉnh**

Phát triển luồng đánh giá riêng phù hợp với các nhiệm vụ và mục tiêu cụ thể của bạn. Tùy chỉnh các chỉ số dựa trên mục tiêu đánh giá.
Áp dụng luồng đánh giá tùy chỉnh này cho các lần chạy theo lô để kiểm tra quy mô lớn.

## Các phương pháp đánh giá tích hợp sẵn

Prompt Flow cũng cung cấp các phương pháp đánh giá tích hợp sẵn.
Bạn có thể gửi các lần chạy theo lô và sử dụng các phương pháp này để đánh giá hiệu suất luồng với bộ dữ liệu lớn.
Xem kết quả đánh giá, so sánh các chỉ số và lặp lại khi cần thiết.
Hãy nhớ rằng, đánh giá là điều thiết yếu để đảm bảo các mô hình AI của bạn đáp ứng các tiêu chí và mục tiêu đề ra. Tham khảo tài liệu chính thức để biết hướng dẫn chi tiết về cách phát triển và sử dụng các luồng đánh giá trong Microsoft Prompt Flow.

Tóm lại, Microsoft Prompt Flow giúp các nhà phát triển tạo ra các ứng dụng LLM chất lượng cao bằng cách đơn giản hóa kỹ thuật prompt và cung cấp môi trường phát triển mạnh mẽ. Nếu bạn đang làm việc với LLM, Prompt Flow là công cụ đáng để khám phá. Tham khảo [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) để có hướng dẫn chi tiết về phát triển và sử dụng các luồng đánh giá trong Microsoft Prompt Flow.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính xác và có thẩm quyền. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.