# AGENTS.md

## Tổng quan dự án

PhiCookBook là một kho lưu trữ sách hướng dẫn toàn diện chứa các ví dụ thực hành, bài hướng dẫn và tài liệu làm việc với dòng mô hình Ngôn Ngữ Nhỏ (SLMs) Phi của Microsoft. Kho lưu trữ minh họa nhiều trường hợp sử dụng khác nhau bao gồm suy luận, điều chỉnh tinh chỉnh, lượng tử hóa, triển khai RAG và các ứng dụng đa phương thức trên nhiều nền tảng và framework khác nhau.

**Công nghệ chính:**
- **Ngôn ngữ:** Python, C#/.NET, JavaScript/Node.js
- **Framework:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Nền tảng:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Loại mô hình:** Phi-3, Phi-3.5, Phi-4 (các biến thể text, vision, đa phương thức, suy luận)

**Cấu trúc kho lưu trữ:**
- `/code/` - Mã ví dụ hoạt động và cài đặt mẫu
- `/md/` - Tài liệu chi tiết, bài hướng dẫn và hướng dẫn sử dụng  
- `/translations/` - Dịch đa ngôn ngữ (hơn 50 ngôn ngữ qua quy trình tự động)
- `/.devcontainer/` - Cấu hình container phát triển (Python 3.12 với Ollama)

## Thiết lập môi trường phát triển

### Sử dụng GitHub Codespaces hoặc Dev Containers (Khuyến nghị)

1. Mở trong GitHub Codespaces (nhanh nhất):
   - Nhấn vào huy hiệu "Open in GitHub Codespaces" trong README
   - Container tự động cấu hình với Python 3.12 và Ollama kèm Phi-3

2. Mở trong VS Code Dev Containers:
   - Dùng huy hiệu "Open in Dev Containers" từ README
   - Container yêu cầu tối thiểu 16GB bộ nhớ máy chủ

### Thiết lập cục bộ

**Yêu cầu:**
- Python 3.12 trở lên
- .NET 8.0 SDK (cho ví dụ C#)
- Node.js 18+ và npm (cho ví dụ JavaScript)
- Khuyến nghị tối thiểu 16GB RAM

**Cài đặt:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Đối với ví dụ Python:**
Đi tới thư mục ví dụ cụ thể và cài đặt phụ thuộc:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # nếu tồn tại requirements.txt
```

**Đối với ví dụ .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Đối với ví dụ JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Khởi động máy chủ phát triển
npm run build  # Xây dựng cho sản xuất
```

## Tổ chức kho lưu trữ

### Ví dụ mã (`/code/`)

- **01.Introduce/** - Giới thiệu cơ bản và mẫu bắt đầu
- **03.Finetuning/** và **04.Finetuning/** - Ví dụ tinh chỉnh với các phương pháp khác nhau
- **03.Inference/** - Ví dụ suy luận trên phần cứng khác nhau (AIPC, MLX)
- **06.E2E/** - Mẫu ứng dụng đầu-cuối
- **07.Lab/** - Cài đặt thí nghiệm/phòng lab
- **08.RAG/** - Mẫu Truy xuất Tăng cường Sinh
- **09.UpdateSamples/** - Mẫu cập nhật mới nhất

### Tài liệu (`/md/`)

- **01.Introduction/** - Hướng dẫn giới thiệu, thiết lập môi trường, hướng dẫn nền tảng
- **02.Application/** - Mẫu ứng dụng theo loại (Text, Code, Vision, Audio, v.v.)
- **02.QuickStart/** - Hướng dẫn bắt đầu nhanh với Microsoft Foundry và GitHub Models
- **03.FineTuning/** - Tài liệu và bài hướng dẫn tinh chỉnh
- **04.HOL/** - Phòng lab thực hành (bao gồm ví dụ .NET)

### Định dạng tập tin

- **Jupyter Notebooks (`.ipynb`)** - Bài hướng dẫn Python tương tác, đánh dấu bằng 📓 trong README
- **Python Scripts (`.py`)** - Ví dụ Python độc lập
- **Dự án C# (`.csproj`, `.sln`)** - Ứng dụng và mẫu .NET
- **JavaScript (`.js`, `package.json`)** - Ví dụ web và Node.js
- **Markdown (`.md`)** - Tài liệu và hướng dẫn

## Làm việc với các ví dụ

### Chạy Jupyter Notebooks

Hầu hết ví dụ được cung cấp dưới dạng notebook Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Mở giao diện trình duyệt
# Điều hướng đến tệp .ipynb mong muốn
```

### Chạy Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Chạy ví dụ .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Hoặc build toàn bộ solution:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Chạy ví dụ JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Phát triển với nạp lại nóng
```

## Kiểm thử

Kho lưu trữ này chứa mã ví dụ và bài hướng dẫn thay vì dự án phần mềm truyền thống với unit test. Việc xác thực thường được thực hiện bằng:

1. **Chạy các ví dụ** - Mỗi ví dụ phải chạy không lỗi
2. **Kiểm tra đầu ra** - Xác nhận phản hồi mô hình phù hợp
3. **Theo dõi bài hướng dẫn** - Hướng dẫn từng bước phải hoạt động như tài liệu

**Phương pháp xác thực phổ biến:**
- Kiểm tra chạy ví dụ trong môi trường mục tiêu
- Xác minh cài đặt phụ thuộc đúng
- Kiểm tra tải về/bộ nhớ mô hình thành công
- Xác nhận hành vi mong đợi khớp tài liệu

## Quy tắc về phong cách và quy ước mã

### Hướng dẫn chung

- Ví dụ rõ ràng, có chú thích đầy đủ và mang tính giáo dục
- Tuân thủ quy ước ngôn ngữ cụ thể (PEP 8 cho Python, chuẩn C# cho .NET)
- Giữ ví dụ tập trung thể hiện năng lực mô hình Phi cụ thể
- Bao gồm chú giải giải thích các khái niệm chính và tham số mô hình

### Tiêu chuẩn tài liệu

**Định dạng URL:**
- Dùng định dạng `[text](../../url)` không thêm khoảng trắng
- Liên kết tương đối: Dùng `./` cho thư mục hiện tại, `../` cho thư mục cha
- Không có locale quốc gia trong URL (tránh `/en-us/`, `/en/`)

**Hình ảnh:**
- Lưu tất cả hình trong thư mục `/imgs/`
- Dùng tên mô tả bằng ký tự tiếng Anh, số và dấu gạch ngang
- Ví dụ: `phi-3-architecture.png`

**Tập tin Markdown:**
- Tham chiếu ví dụ thực tế trong thư mục `/code/`
- Đồng bộ tài liệu với thay đổi mã
- Dùng emoji 📓 để đánh dấu link Jupyter notebook trong README

### Tổ chức tập tin

- Ví dụ mã trong `/code/` tổ chức theo chủ đề/tính năng
- Tài liệu trong `/md/` phản ánh cấu trúc mã khi áp dụng
- Giữ các tập tin liên quan (notebook, script, config) cùng thư mục con

## Hướng dẫn gửi Pull Request

### Trước khi gửi

1. **Fork kho lưu trữ** về tài khoản của bạn
2. **Tách PR theo loại:**
   - Sửa lỗi trong một PR
   - Cập nhật tài liệu trong PR khác
   - Ví dụ mới trong PR riêng
   - Sửa lỗi chính tả có thể gộp chung

3. **Xử lý xung đột merge:**
   - Cập nhật nhánh `main` cục bộ trước khi thay đổi
   - Đồng bộ với upstream thường xuyên

4. **PR dịch thuật:**
   - Phải bao gồm bản dịch cho TẤT CẢ tập tin trong thư mục
   - Giữ cấu trúc nhất quán với ngôn ngữ gốc

### Kiểm tra bắt buộc

PR tự động chạy workflow GitHub để xác thực:

1. **Kiểm tra đường dẫn tương đối** - Tất cả liên kết nội bộ phải hoạt động
   - Kiểm thử link cục bộ: Ctrl+Click trong VS Code
   - Dùng đề xuất đường dẫn của VS Code (`./` hoặc `../`)

2. **Kiểm tra locale URL** - URL web không được chứa locale quốc gia
   - Loại bỏ `/en-us/`, `/en/` và mã ngôn ngữ khác
   - Dùng URL quốc tế chung

3. **Kiểm tra URL bị gãy** - Tất cả URL phải trả về trạng thái 200
   - Kiểm tra link truy cập được trước khi gửi
   - Lưu ý: Một số lỗi có thể do giới hạn mạng

### Định dạng tiêu đề PR

```
[component] Brief description
```

Ví dụ:
- `[docs] Thêm bài hướng dẫn suy luận Phi-4`
- `[code] Sửa ví dụ tích hợp ONNX Runtime`
- `[translation] Thêm bản dịch tiếng Nhật cho hướng dẫn intro`

## Mẫu phát triển phổ biến

### Làm việc với mô hình Phi

**Tải mô hình:**
- Ví dụ dùng nhiều framework khác nhau: Transformers, ONNX Runtime, MLX, OpenVINO
- Mô hình thường tải từ Hugging Face, Azure hoặc GitHub Models
- Kiểm tra mô hình tương thích với phần cứng của bạn (CPU, GPU, NPU)

**Mẫu suy luận:**
- Sinh văn bản: Hầu hết dùng biến thể chat/instruct
- Thị giác: Phi-3-vision và Phi-4-multimodal cho hiểu ảnh
- Âm thanh: Phi-4-multimodal hỗ trợ đầu vào âm thanh
- Suy luận: Biến thể Phi-4-reasoning cho tác vụ suy luận nâng cao

### Ghi chú nền tảng cụ thể

**Microsoft Foundry:**
- Cần đăng ký Azure và key API
- Xem `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Có tầng miễn phí để thử nghiệm
- Xem `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Suy luận cục bộ:**
- ONNX Runtime: đa nền tảng, suy luận tối ưu
- Ollama: quản lý mô hình cục bộ dễ dàng (đã cấu hình sẵn trong dev container)
- Apple MLX: tối ưu cho Apple Silicon

## Khắc phục sự cố

### Vấn đề phổ biến

**Vấn đề bộ nhớ:**
- Mô hình Phi cần RAM lớn (đặc biệt biến thể vision/đa phương thức)
- Dùng mô hình lượng tử cho môi trường hạn chế tài nguyên
- Xem `/md/01.Introduction/04/QuantifyingPhi.md`

**Xung đột phụ thuộc:**
- Ví dụ Python có thể yêu cầu phiên bản riêng
- Dùng môi trường ảo cho mỗi ví dụ
- Kiểm tra tập tin `requirements.txt` từng ví dụ

**Lỗi tải mô hình:**
- Mô hình lớn có thể timeout kết nối chậm
- Cân nhắc dùng môi trường cloud (Codespaces, Azure)
- Kiểm tra cache Hugging Face: `~/.cache/huggingface/`

**Vấn đề dự án .NET:**
- Đảm bảo đã cài .NET 8.0 SDK
- Dùng `dotnet restore` trước khi build
- Một số dự án cấu hình riêng cho CUDA (Debug_Cuda)

**Ví dụ JavaScript/Web:**
- Dùng Node.js 18+ để tương thích
- Xoá thư mục `node_modules` rồi cài lại nếu lỗi
- Kiểm tra console trình duyệt với lỗi tương thích WebGPU

### Trợ giúp

- **Discord:** Tham gia Microsoft Foundry Community Discord
- **GitHub Issues:** Báo lỗi và sự cố trong kho lưu trữ
- **GitHub Discussions:** Hỏi đáp và chia sẻ kiến thức

## Bối cảnh bổ sung

### Trách nhiệm AI

Mọi sử dụng mô hình Phi phải tuân theo nguyên tắc Trách nhiệm AI của Microsoft:
- Công bằng, tin cậy, an toàn
- Riêng tư và bảo mật  
- Bao trùm, minh bạch, trách nhiệm
- Dùng Azure AI Content Safety cho ứng dụng sản xuất
- Xem `/md/01.Introduction/01/01.AISafety.md`

### Dịch thuật

- Hỗ trợ hơn 50 ngôn ngữ qua GitHub Action tự động
- Bản dịch trong thư mục `/translations/`
- Quản lý bởi quy trình co-op-translator
- Không chỉnh sửa thủ công các tập tin dịch (tự sinh)

### Đóng góp

- Tuân theo hướng dẫn trong `CONTRIBUTING.md`
- Đồng ý Thỏa thuận Giấy phép Người đóng góp (CLA)
- Tuân thủ Quy tắc Ứng xử mã nguồn mở của Microsoft
- Giữ bảo mật và thông tin đăng nhập ngoài các commit

### Hỗ trợ đa ngôn ngữ

Đây là kho đa ngôn ngữ với các ví dụ trong:
- **Python** - Quy trình ML/AI, notebook Jupyter, tinh chỉnh
- **C#/.NET** - Ứng dụng doanh nghiệp, tích hợp ONNX Runtime
- **JavaScript** - AI web, suy luận trình duyệt với WebGPU

Chọn ngôn ngữ phù hợp nhất với mục đích sử dụng và môi trường triển khai của bạn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Trong khi chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính xác và uy tín nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->