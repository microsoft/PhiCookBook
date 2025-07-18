<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:02:00+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "vi"
}
-->
# Sử dụng GPU Windows để tạo giải pháp Prompt flow với Phi-3.5-Instruct ONNX

Tài liệu dưới đây là ví dụ về cách sử dụng PromptFlow với ONNX (Open Neural Network Exchange) để phát triển các ứng dụng AI dựa trên các mô hình Phi-3.

PromptFlow là bộ công cụ phát triển được thiết kế để đơn giản hóa chu trình phát triển toàn diện các ứng dụng AI dựa trên LLM (Large Language Model), từ ý tưởng, tạo mẫu đến kiểm thử và đánh giá.

Bằng cách tích hợp PromptFlow với ONNX, các nhà phát triển có thể:

- Tối ưu hiệu suất mô hình: Tận dụng ONNX để suy luận và triển khai mô hình hiệu quả.
- Đơn giản hóa phát triển: Sử dụng PromptFlow để quản lý quy trình làm việc và tự động hóa các tác vụ lặp đi lặp lại.
- Tăng cường hợp tác: Hỗ trợ làm việc nhóm tốt hơn bằng cách cung cấp môi trường phát triển thống nhất.

**Prompt flow** là bộ công cụ phát triển giúp đơn giản hóa chu trình phát triển toàn diện các ứng dụng AI dựa trên LLM, từ ý tưởng, tạo mẫu, kiểm thử, đánh giá đến triển khai sản xuất và giám sát. Nó giúp việc thiết kế prompt trở nên dễ dàng hơn và cho phép bạn xây dựng các ứng dụng LLM với chất lượng sản xuất.

Prompt flow có thể kết nối với OpenAI, Azure OpenAI Service và các mô hình tùy chỉnh (Huggingface, LLM/SLM cục bộ). Chúng tôi hy vọng sẽ triển khai mô hình ONNX đã lượng tử hóa của Phi-3.5 cho các ứng dụng cục bộ. Prompt flow có thể giúp chúng ta lên kế hoạch kinh doanh tốt hơn và hoàn thiện các giải pháp cục bộ dựa trên Phi-3.5. Trong ví dụ này, chúng ta sẽ kết hợp ONNX Runtime GenAI Library để hoàn thiện giải pháp Prompt flow dựa trên GPU Windows.

## **Cài đặt**

### **ONNX Runtime GenAI cho GPU Windows**

Đọc hướng dẫn này để cài đặt ONNX Runtime GenAI cho GPU Windows [click vào đây](./ORTWindowGPUGuideline.md)

### **Thiết lập Prompt flow trong VSCode**

1. Cài đặt Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.vi.png)

2. Sau khi cài đặt Prompt flow VS Code Extension, nhấp vào phần mở rộng và chọn **Installation dependencies** theo hướng dẫn này để cài đặt Prompt flow SDK trong môi trường của bạn

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.vi.png)

3. Tải về [Mã mẫu](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) và dùng VS Code mở mẫu này

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.vi.png)

4. Mở **flow.dag.yaml** để chọn môi trường Python của bạn

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.vi.png)

   Mở **chat_phi3_ort.py** để thay đổi vị trí mô hình Phi-3.5-instruct ONNX của bạn

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.vi.png)

5. Chạy prompt flow để kiểm thử

Mở **flow.dag.yaml** và nhấp vào trình chỉnh sửa trực quan

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.vi.png)

sau khi nhấp, chạy để kiểm thử

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.vi.png)

1. Bạn có thể chạy theo lô trong terminal để xem thêm kết quả


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Bạn có thể xem kết quả trong trình duyệt mặc định của mình


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.vi.png)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.