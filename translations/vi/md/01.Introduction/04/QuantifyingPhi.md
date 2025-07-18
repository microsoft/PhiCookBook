<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:48:31+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "vi"
}
-->
# **Định lượng Phi Family**

Định lượng mô hình là quá trình ánh xạ các tham số (như trọng số và giá trị kích hoạt) trong mô hình mạng nơ-ron từ một phạm vi giá trị lớn (thường là phạm vi giá trị liên tục) sang một phạm vi giá trị hữu hạn nhỏ hơn. Công nghệ này giúp giảm kích thước và độ phức tạp tính toán của mô hình, đồng thời nâng cao hiệu quả hoạt động của mô hình trong các môi trường hạn chế tài nguyên như thiết bị di động hoặc hệ thống nhúng. Định lượng mô hình đạt được việc nén bằng cách giảm độ chính xác của các tham số, nhưng đồng thời cũng gây ra một mức độ mất mát về độ chính xác. Do đó, trong quá trình định lượng, cần cân bằng giữa kích thước mô hình, độ phức tạp tính toán và độ chính xác. Các phương pháp định lượng phổ biến bao gồm định lượng điểm cố định, định lượng dấu phẩy động, v.v. Bạn có thể lựa chọn chiến lược định lượng phù hợp dựa trên kịch bản và nhu cầu cụ thể.

Chúng tôi mong muốn triển khai mô hình GenAI lên các thiết bị biên và cho phép nhiều thiết bị hơn tham gia vào các kịch bản GenAI, như thiết bị di động, AI PC/Copilot+PC, và các thiết bị IoT truyền thống. Thông qua mô hình định lượng, chúng ta có thể triển khai trên các thiết bị biên khác nhau tùy theo từng thiết bị. Kết hợp với khung tăng tốc mô hình và mô hình định lượng do các nhà sản xuất phần cứng cung cấp, chúng ta có thể xây dựng các kịch bản ứng dụng SLM tốt hơn.

Trong kịch bản định lượng, chúng ta có các độ chính xác khác nhau (INT4, INT8, FP16, FP32). Dưới đây là giải thích về các độ chính xác định lượng thường dùng.

### **INT4**

Định lượng INT4 là phương pháp định lượng mạnh mẽ, chuyển đổi trọng số và giá trị kích hoạt của mô hình thành số nguyên 4-bit. Định lượng INT4 thường dẫn đến mất mát độ chính xác lớn hơn do phạm vi biểu diễn nhỏ hơn và độ chính xác thấp hơn. Tuy nhiên, so với định lượng INT8, INT4 có thể giảm đáng kể yêu cầu lưu trữ và độ phức tạp tính toán của mô hình. Cần lưu ý rằng định lượng INT4 khá hiếm trong thực tế vì độ chính xác quá thấp có thể gây suy giảm hiệu năng mô hình đáng kể. Ngoài ra, không phải phần cứng nào cũng hỗ trợ các phép toán INT4, nên cần cân nhắc khả năng tương thích phần cứng khi chọn phương pháp định lượng.

### **INT8**

Định lượng INT8 là quá trình chuyển đổi trọng số và giá trị kích hoạt của mô hình từ số dấu phẩy động sang số nguyên 8-bit. Mặc dù phạm vi số và độ chính xác của số nguyên INT8 nhỏ hơn, phương pháp này giúp giảm đáng kể yêu cầu lưu trữ và tính toán. Trong định lượng INT8, trọng số và giá trị kích hoạt trải qua quá trình định lượng bao gồm tỉ lệ và bù để giữ lại thông tin dấu phẩy động gốc càng nhiều càng tốt. Khi suy luận, các giá trị đã định lượng sẽ được giải định lượng trở lại số dấu phẩy động để tính toán, sau đó lại được định lượng về INT8 cho bước tiếp theo. Phương pháp này cung cấp độ chính xác đủ dùng trong hầu hết các ứng dụng đồng thời duy trì hiệu quả tính toán cao.

### **FP16**

Định dạng FP16, tức là số dấu phẩy động 16-bit (float16), giảm một nửa dung lượng bộ nhớ so với số dấu phẩy động 32-bit (float32), mang lại lợi thế lớn trong các ứng dụng học sâu quy mô lớn. Định dạng FP16 cho phép tải các mô hình lớn hơn hoặc xử lý nhiều dữ liệu hơn trong giới hạn bộ nhớ GPU tương đương. Khi phần cứng GPU hiện đại ngày càng hỗ trợ các phép toán FP16, việc sử dụng định dạng FP16 cũng có thể cải thiện tốc độ tính toán. Tuy nhiên, FP16 cũng có nhược điểm cố hữu là độ chính xác thấp hơn, có thể gây ra sự không ổn định về số học hoặc mất mát độ chính xác trong một số trường hợp.

### **FP32**

Định dạng FP32 cung cấp độ chính xác cao hơn và có thể biểu diễn chính xác một phạm vi giá trị rộng. Trong các kịch bản thực hiện các phép toán phức tạp hoặc yêu cầu kết quả độ chính xác cao, định dạng FP32 được ưu tiên sử dụng. Tuy nhiên, độ chính xác cao cũng đồng nghĩa với việc sử dụng nhiều bộ nhớ hơn và thời gian tính toán lâu hơn. Với các mô hình học sâu quy mô lớn, đặc biệt khi có nhiều tham số và lượng dữ liệu khổng lồ, định dạng FP32 có thể gây ra tình trạng thiếu bộ nhớ GPU hoặc giảm tốc độ suy luận.

Trên các thiết bị di động hoặc thiết bị IoT, chúng ta có thể chuyển đổi các mô hình Phi-3.x sang INT4, trong khi AI PC / Copilot PC có thể sử dụng độ chính xác cao hơn như INT8, FP16, FP32.

Hiện nay, các nhà sản xuất phần cứng khác nhau có các khung hỗ trợ mô hình sinh khác nhau, như OpenVINO của Intel, QNN của Qualcomm, MLX của Apple, và CUDA của Nvidia, kết hợp với định lượng mô hình để hoàn thành việc triển khai cục bộ.

Về mặt công nghệ, chúng ta có các định dạng hỗ trợ khác nhau sau khi định lượng, như định dạng PyTorch / Tensorflow, GGUF, và ONNX. Tôi đã thực hiện so sánh định dạng và kịch bản ứng dụng giữa GGUF và ONNX. Ở đây tôi khuyến nghị định dạng định lượng ONNX, vì nó được hỗ trợ tốt từ khung mô hình đến phần cứng. Trong chương này, chúng ta sẽ tập trung vào ONNX Runtime cho GenAI, OpenVINO, và Apple MLX để thực hiện định lượng mô hình (nếu bạn có cách tốt hơn, cũng có thể gửi PR cho chúng tôi).

**Chương này bao gồm**

1. [Định lượng Phi-3.5 / 4 sử dụng llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Định lượng Phi-3.5 / 4 sử dụng Generative AI extensions cho onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Định lượng Phi-3.5 / 4 sử dụng Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Định lượng Phi-3.5 / 4 sử dụng Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.