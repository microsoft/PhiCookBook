<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:32:08+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "vi"
}
-->
# **Định lượng họ Phi**

Định lượng mô hình đề cập đến quá trình ánh xạ các tham số (như trọng số và giá trị kích hoạt) trong một mô hình mạng nơ-ron từ một phạm vi giá trị lớn (thường là phạm vi giá trị liên tục) sang một phạm vi giá trị hữu hạn nhỏ hơn. Công nghệ này giúp giảm kích thước và độ phức tạp tính toán của mô hình, đồng thời cải thiện hiệu suất vận hành của mô hình trong các môi trường có tài nguyên hạn chế như thiết bị di động hoặc hệ thống nhúng. Định lượng mô hình đạt được việc nén thông qua việc giảm độ chính xác của các tham số, nhưng đồng thời cũng gây ra một số mất mát về độ chính xác. Do đó, trong quá trình định lượng, cần cân bằng giữa kích thước mô hình, độ phức tạp tính toán và độ chính xác. Các phương pháp định lượng phổ biến bao gồm định lượng điểm cố định, định lượng dấu phẩy động, v.v. Bạn có thể lựa chọn chiến lược định lượng phù hợp tùy theo kịch bản và nhu cầu cụ thể.

Chúng tôi mong muốn triển khai mô hình GenAI lên các thiết bị biên và cho phép nhiều thiết bị hơn tham gia vào các kịch bản GenAI, như thiết bị di động, AI PC/Copilot+PC, và các thiết bị IoT truyền thống. Thông qua mô hình định lượng, chúng ta có thể triển khai trên các thiết bị biên khác nhau dựa trên từng loại thiết bị. Kết hợp với khung tăng tốc mô hình và mô hình định lượng do các nhà sản xuất phần cứng cung cấp, chúng ta có thể xây dựng các kịch bản ứng dụng SLM tốt hơn.

Trong kịch bản định lượng, chúng ta có các mức độ chính xác khác nhau (INT4, INT8, FP16, FP32). Dưới đây là giải thích về các mức độ chính xác định lượng thường dùng.

### **INT4**

Định lượng INT4 là phương pháp định lượng mạnh mẽ, chuyển đổi trọng số và giá trị kích hoạt của mô hình thành số nguyên 4-bit. Định lượng INT4 thường dẫn đến mất mát độ chính xác lớn hơn do phạm vi biểu diễn nhỏ hơn và độ chính xác thấp hơn. Tuy nhiên, so với định lượng INT8, INT4 có thể giảm đáng kể yêu cầu lưu trữ và độ phức tạp tính toán của mô hình. Cần lưu ý rằng định lượng INT4 khá hiếm trong các ứng dụng thực tế, vì độ chính xác quá thấp có thể làm giảm đáng kể hiệu năng mô hình. Bên cạnh đó, không phải phần cứng nào cũng hỗ trợ các phép toán INT4, nên cần cân nhắc tính tương thích phần cứng khi chọn phương pháp định lượng.

### **INT8**

Định lượng INT8 là quá trình chuyển đổi trọng số và giá trị kích hoạt của mô hình từ số dấu phẩy động sang số nguyên 8-bit. Mặc dù phạm vi số được biểu diễn bởi số nguyên INT8 nhỏ hơn và ít chính xác hơn, nhưng nó giúp giảm đáng kể yêu cầu lưu trữ và tính toán. Trong định lượng INT8, trọng số và giá trị kích hoạt của mô hình trải qua quá trình định lượng, bao gồm tỉ lệ hóa và dịch chuyển, nhằm giữ lại thông tin dấu phẩy động gốc càng nhiều càng tốt. Trong quá trình suy luận, các giá trị đã định lượng này sẽ được giải định lượng trở lại thành số dấu phẩy động để tính toán, rồi sau đó lại được định lượng trở lại thành INT8 cho bước tiếp theo. Phương pháp này có thể cung cấp độ chính xác đủ dùng trong hầu hết các ứng dụng đồng thời duy trì hiệu quả tính toán cao.

### **FP16**

Định dạng FP16, tức là số dấu phẩy động 16-bit (float16), giảm một nửa dung lượng bộ nhớ so với số dấu phẩy động 32-bit (float32), điều này mang lại lợi thế đáng kể trong các ứng dụng học sâu quy mô lớn. Định dạng FP16 cho phép tải các mô hình lớn hơn hoặc xử lý nhiều dữ liệu hơn trong cùng giới hạn bộ nhớ GPU. Khi phần cứng GPU hiện đại ngày càng hỗ trợ các phép toán FP16, việc sử dụng định dạng FP16 cũng có thể cải thiện tốc độ tính toán. Tuy nhiên, định dạng FP16 cũng có nhược điểm cố hữu là độ chính xác thấp hơn, có thể gây ra bất ổn về số học hoặc mất độ chính xác trong một số trường hợp.

### **FP32**

Định dạng FP32 cung cấp độ chính xác cao hơn và có thể biểu diễn chính xác một phạm vi giá trị rộng. Trong các kịch bản thực hiện các phép toán toán học phức tạp hoặc cần kết quả có độ chính xác cao, định dạng FP32 được ưu tiên sử dụng. Tuy nhiên, độ chính xác cao cũng đồng nghĩa với việc sử dụng nhiều bộ nhớ hơn và thời gian tính toán lâu hơn. Với các mô hình học sâu quy mô lớn, đặc biệt khi có nhiều tham số mô hình và lượng dữ liệu khổng lồ, định dạng FP32 có thể gây ra tình trạng thiếu bộ nhớ GPU hoặc làm giảm tốc độ suy luận.

Trên các thiết bị di động hoặc thiết bị IoT, chúng ta có thể chuyển đổi mô hình Phi-3.x sang INT4, trong khi AI PC / Copilot PC có thể sử dụng độ chính xác cao hơn như INT8, FP16, FP32.

Hiện tại, các nhà sản xuất phần cứng khác nhau có các khung làm việc hỗ trợ mô hình sinh, như OpenVINO của Intel, QNN của Qualcomm, MLX của Apple, và CUDA của Nvidia, kết hợp với định lượng mô hình để hoàn thiện việc triển khai cục bộ.

Về mặt công nghệ, chúng ta có các định dạng hỗ trợ khác nhau sau định lượng, như định dạng PyTorch / Tensorflow, GGUF và ONNX. Tôi đã thực hiện so sánh định dạng và các kịch bản ứng dụng giữa GGUF và ONNX. Ở đây tôi khuyến nghị định dạng định lượng ONNX, vốn có sự hỗ trợ tốt từ khung mô hình đến phần cứng. Trong chương này, chúng ta sẽ tập trung vào ONNX Runtime cho GenAI, OpenVINO và Apple MLX để thực hiện định lượng mô hình (nếu bạn có cách làm tốt hơn, cũng có thể gửi PR cho chúng tôi).

**Chương này bao gồm**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính xác nhất. Đối với các thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.