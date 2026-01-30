## Chào mừng đến với các phòng thí nghiệm Phi sử dụng C#

Có một loạt các phòng thí nghiệm trình bày cách tích hợp các phiên bản mạnh mẽ khác nhau của các mô hình Phi trong môi trường .NET.

## Yêu cầu trước

Trước khi chạy mẫu, hãy đảm bảo bạn đã cài đặt các phần sau:

**.NET 9:** Đảm bảo bạn đã cài đặt [phiên bản .NET mới nhất](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) trên máy của mình.

**(Tùy chọn) Visual Studio hoặc Visual Studio Code:** Bạn sẽ cần một IDE hoặc trình soạn thảo mã có khả năng chạy các dự án .NET. Khuyến nghị sử dụng [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) hoặc [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Sử dụng git** để clone về máy một trong các phiên bản Phi-3, Phi3.5 hoặc Phi-4 có sẵn từ [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Tải xuống các mô hình Phi-4 ONNX** về máy của bạn:

### điều hướng đến thư mục lưu trữ các mô hình

```bash
cd c:\phi\models
```

### thêm hỗ trợ cho lfs

```bash
git lfs install 
```

### clone và tải xuống mô hình Phi-4 mini instruct và mô hình Phi-4 đa phương tiện

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Tải xuống các mô hình Phi-3 ONNX** về máy của bạn:

### clone và tải xuống mô hình Phi-3 mini 4K instruct và mô hình Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Quan trọng:** Các bản demo hiện tại được thiết kế để sử dụng các phiên bản ONNX của mô hình. Các bước trên sẽ clone các mô hình sau.

## Về các phòng thí nghiệm

Giải pháp chính có một số phòng thí nghiệm mẫu thể hiện khả năng của các mô hình Phi sử dụng C#.

| Dự án | Mô hình | Mô tả |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 hoặc Phi-3.5 | Mẫu chat console cho phép người dùng đặt câu hỏi. Dự án tải mô hình ONNX Phi-3 cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 hoặc Phi-3.5 | Mẫu chat console cho phép người dùng đặt câu hỏi. Dự án tải mô hình ONNX Phi-3 cục bộ sử dụng thư viện `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 hoặc Phi-3.5 | Đây là dự án mẫu sử dụng mô hình phi3 vision cục bộ để phân tích hình ảnh. Dự án tải mô hình ONNX Phi-3 Vision cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 hoặc Phi-3.5 | Đây là dự án mẫu sử dụng mô hình phi3 vision cục bộ để phân tích hình ảnh. Dự án tải mô hình ONNX Phi-3 Vision cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntime`. Dự án cũng cung cấp menu với các tùy chọn khác nhau để tương tác với người dùng. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Mẫu chat console cho phép người dùng đặt câu hỏi. Dự án tải mô hình ONNX Phi-4 cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Mẫu chat console cho phép người dùng đặt câu hỏi. Dự án tải mô hình ONNX Phi-4 cục bộ sử dụng thư viện `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Mẫu chat console cho phép người dùng đặt câu hỏi. Dự án tải mô hình ONNX Phi-4 cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntimeGenAI` và triển khai `IChatClient` từ `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Mẫu chat console cho phép người dùng đặt câu hỏi. Chat có triển khai bộ nhớ. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Đây là dự án mẫu sử dụng mô hình Phi-4 cục bộ để phân tích hình ảnh và hiển thị kết quả trên console. Dự án tải mô hình Phi-4-`multimodal-instruct-onnx` cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Đây là dự án mẫu sử dụng mô hình Phi-4 cục bộ để phân tích file âm thanh, tạo bản ghi âm và hiển thị kết quả trên console. Dự án tải mô hình Phi-4-`multimodal-instruct-onnx` cục bộ sử dụng thư viện `Microsoft.ML.OnnxRuntime`. |

## Cách chạy các dự án

Để chạy các dự án, làm theo các bước sau:

1. Clone repository về máy của bạn.

1. Mở terminal và điều hướng đến dự án mong muốn. Ví dụ, chạy `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Chạy dự án với lệnh

    ```bash
    dotnet run
    ```

1. Dự án mẫu sẽ yêu cầu nhập liệu từ người dùng và trả lời sử dụng mô hình cục bộ.

   Bản demo khi chạy sẽ tương tự như sau:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.