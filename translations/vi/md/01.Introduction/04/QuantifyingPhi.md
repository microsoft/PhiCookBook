<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T08:53:27+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "vi"
}
-->
# **Định Lượng Họ Phi**

Định lượng mô hình là quá trình ánh xạ các tham số (như trọng số và giá trị kích hoạt) trong mô hình mạng nơ-ron từ phạm vi giá trị lớn (thường là phạm vi giá trị liên tục) sang phạm vi giá trị hữu hạn nhỏ hơn. Công nghệ này có thể giảm kích thước và độ phức tạp tính toán của mô hình, đồng thời cải thiện hiệu quả hoạt động của mô hình trong các môi trường hạn chế tài nguyên như thiết bị di động hoặc hệ thống nhúng. Định lượng mô hình đạt được sự nén bằng cách giảm độ chính xác của các tham số, nhưng cũng đồng thời làm mất đi một mức độ chính xác nhất định. Do đó, trong quá trình định lượng cần cân bằng giữa kích thước mô hình, độ phức tạp tính toán và độ chính xác. Các phương pháp định lượng phổ biến bao gồm định lượng số cố định, định lượng số dấu động, v.v. Bạn có thể chọn chiến lược định lượng phù hợp theo từng kịch bản và nhu cầu cụ thể.

Chúng tôi mong muốn triển khai mô hình GenAI lên các thiết bị biên và cho phép nhiều thiết bị hơn tham gia vào các kịch bản GenAI, chẳng hạn như thiết bị di động, AI PC/Copilot+PC, và các thiết bị IoT truyền thống. Thông qua mô hình định lượng, chúng ta có thể triển khai mô hình lên các thiết bị biên khác nhau dựa trên các thiết bị khác nhau. Kết hợp với khung tăng tốc mô hình và mô hình định lượng do các nhà sản xuất phần cứng cung cấp, chúng ta có thể xây dựng các kịch bản ứng dụng SLM tốt hơn.

Trong kịch bản định lượng, chúng ta có các độ chính xác khác nhau (INT4, INT8, FP16, FP32). Dưới đây là giải thích về các độ chính xác định lượng thường dùng.

### **INT4**

Định lượng INT4 là phương pháp định lượng quyết liệt, trong đó trọng số và giá trị kích hoạt của mô hình được định lượng thành số nguyên 4-bit. Định lượng INT4 thường dẫn đến mất chính xác lớn hơn do phạm vi biểu diễn nhỏ và độ chính xác thấp hơn. Tuy nhiên, so với định lượng INT8, định lượng INT4 có thể giảm thêm yêu cầu lưu trữ và độ phức tạp tính toán của mô hình. Cần lưu ý rằng định lượng INT4 ít phổ biến trong các ứng dụng thực tế, vì độ chính xác quá thấp có thể gây suy giảm đáng kể hiệu năng mô hình. Ngoài ra, không phải tất cả phần cứng đều hỗ trợ các phép toán INT4, nên cần cân nhắc khả năng tương thích phần cứng khi chọn phương pháp định lượng.

### **INT8**

Định lượng INT8 là quá trình chuyển đổi trọng số và giá trị kích hoạt của mô hình từ số dấu động sang số nguyên 8-bit. Mặc dù phạm vi số và độ chính xác được biểu diễn bởi số nguyên INT8 nhỏ hơn, nhưng định lượng này có thể giảm đáng kể yêu cầu lưu trữ và tính toán. Trong định lượng INT8, trọng số và giá trị kích hoạt của mô hình trải qua quá trình định lượng, bao gồm tỷ lệ và dịch, nhằm giữ nguyên thông tin dấu động ban đầu càng nhiều càng tốt. Trong quá trình suy luận, các giá trị đã định lượng này sẽ được giải định lượng trở lại số dấu động để tính toán, sau đó tiếp tục định lượng trở lại INT8 cho bước tiếp theo. Phương pháp này có thể cung cấp độ chính xác đủ trong hầu hết các ứng dụng đồng thời duy trì hiệu quả tính toán cao.

### **FP16**

Định dạng FP16, tức là số dấu động 16-bit (float16), giảm phân bổ bộ nhớ xuống một nửa so với số dấu động 32-bit (float32), đem lại lợi thế lớn trong các ứng dụng học sâu quy mô lớn. Định dạng FP16 cho phép tải các mô hình lớn hơn hoặc xử lý nhiều dữ liệu hơn trong giới hạn bộ nhớ GPU tương đương. Khi phần cứng GPU hiện đại ngày càng hỗ trợ các phép toán FP16, việc sử dụng định dạng FP16 cũng có thể mang lại cải thiện về tốc độ tính toán. Tuy nhiên, định dạng FP16 cũng có nhược điểm vốn có là độ chính xác thấp hơn, có thể dẫn đến bất ổn số hoặc mất chính xác trong một số trường hợp.

### **FP32**

Định dạng FP32 cung cấp độ chính xác cao hơn và có thể biểu diễn chính xác một phạm vi giá trị rộng. Trong các kịch bản thực hiện các phép toán toán học phức tạp hoặc yêu cầu kết quả độ chính xác cao, định dạng FP32 được ưu tiên sử dụng. Tuy nhiên, độ chính xác cao cũng đồng nghĩa với việc sử dụng nhiều bộ nhớ và thời gian tính toán lâu hơn. Đối với các mô hình học sâu quy mô lớn, đặc biệt khi có nhiều tham số mô hình và lượng dữ liệu khổng lồ, định dạng FP32 có thể gây ra thiếu hụt bộ nhớ GPU hoặc làm giảm tốc độ suy luận.

Trên các thiết bị di động hoặc thiết bị IoT, chúng ta có thể chuyển đổi các mô hình Phi-3.x sang INT4, trong khi AI PC / Copilot PC có thể sử dụng độ chính xác cao hơn như INT8, FP16, FP32.

Hiện nay, các nhà sản xuất phần cứng khác nhau có các khung hỗ trợ mô hình sinh khác nhau, ví dụ như OpenVINO của Intel, QNN của Qualcomm, MLX của Apple và CUDA của Nvidia, v.v., kết hợp với định lượng mô hình để hoàn thành triển khai cục bộ.

Về mặt kỹ thuật, chúng ta có các dạng hỗ trợ sau định lượng khác nhau như định dạng PyTorch / TensorFlow, GGUF và ONNX. Tôi đã thực hiện so sánh và kịch bản ứng dụng giữa GGUF và ONNX. Ở đây tôi khuyến nghị định dạng định lượng ONNX, vốn được hỗ trợ tốt từ khung mô hình đến phần cứng. Trong chương này, chúng ta sẽ tập trung vào ONNX Runtime cho GenAI, OpenVINO và Apple MLX để thực hiện định lượng mô hình (nếu bạn có cách tốt hơn, bạn cũng có thể gửi PR cho chúng tôi).

**Chương này bao gồm**

1. [Định lượng Phi-3.5 / 4 sử dụng llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Định lượng Phi-3.5 / 4 sử dụng phần mở rộng AI sinh học cho onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Định lượng Phi-3.5 / 4 sử dụng Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Định lượng Phi-3.5 / 4 sử dụng Khung Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn chính xác và chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->