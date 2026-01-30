# AGENTS.md

## Tổng quan dự án

PhiCookBook là một kho tài liệu nấu ăn toàn diện, chứa các ví dụ thực hành, hướng dẫn và tài liệu để làm việc với dòng mô hình ngôn ngữ nhỏ (SLMs) của Microsoft Phi. Kho tài liệu này trình bày các trường hợp sử dụng khác nhau bao gồm suy luận, tinh chỉnh, lượng hóa, triển khai RAG và ứng dụng đa phương tiện trên các nền tảng và khung làm việc khác nhau.

**Công nghệ chính:**
- **Ngôn ngữ:** Python, C#/.NET, JavaScript/Node.js
- **Khung làm việc:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Nền tảng:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Loại mô hình:** Phi-3, Phi-3.5, Phi-4 (biến thể văn bản, hình ảnh, đa phương tiện, lý luận)

**Cấu trúc kho tài liệu:**
- `/code/` - Các ví dụ mã hoạt động và triển khai mẫu
- `/md/` - Tài liệu chi tiết, hướng dẫn và cách thực hiện  
- `/translations/` - Bản dịch đa ngôn ngữ (hơn 50 ngôn ngữ thông qua quy trình tự động)
- `/.devcontainer/` - Cấu hình container phát triển (Python 3.12 với Ollama)

## Thiết lập môi trường phát triển

### Sử dụng GitHub Codespaces hoặc Dev Containers (Khuyến nghị)

1. Mở trong GitHub Codespaces (nhanh nhất):
   - Nhấp vào huy hiệu "Open in GitHub Codespaces" trong README
   - Container tự động cấu hình với Python 3.12 và Ollama với Phi-3

2. Mở trong VS Code Dev Containers:
   - Sử dụng huy hiệu "Open in Dev Containers" từ README
   - Container yêu cầu tối thiểu bộ nhớ 16GB trên máy chủ

### Thiết lập cục bộ

**Yêu cầu:**
- Python 3.12 hoặc mới hơn
- .NET 8.0 SDK (cho các ví dụ C#)
- Node.js 18+ và npm (cho các ví dụ JavaScript)
- Khuyến nghị tối thiểu 16GB RAM

**Cài đặt:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Đối với các ví dụ Python:**
Đi đến các thư mục ví dụ cụ thể và cài đặt các phụ thuộc:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Đối với các ví dụ .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Đối với các ví dụ JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Tổ chức kho tài liệu

### Ví dụ mã (`/code/`)

- **01.Introduce/** - Giới thiệu cơ bản và các mẫu bắt đầu
- **03.Finetuning/** và **04.Finetuning/** - Các ví dụ tinh chỉnh với nhiều phương pháp khác nhau
- **03.Inference/** - Các ví dụ suy luận trên phần cứng khác nhau (AIPC, MLX)
- **06.E2E/** - Các mẫu ứng dụng từ đầu đến cuối
- **07.Lab/** - Các triển khai thí nghiệm/phòng thí nghiệm
- **08.RAG/** - Các mẫu tạo nội dung dựa trên truy xuất
- **09.UpdateSamples/** - Các mẫu được cập nhật mới nhất

### Tài liệu (`/md/`)

- **01.Introduction/** - Hướng dẫn giới thiệu, thiết lập môi trường, hướng dẫn nền tảng
- **02.Application/** - Các mẫu ứng dụng được tổ chức theo loại (Văn bản, Mã, Hình ảnh, Âm thanh, v.v.)
- **02.QuickStart/** - Hướng dẫn bắt đầu nhanh cho Azure AI Foundry và GitHub Models
- **03.FineTuning/** - Tài liệu và hướng dẫn tinh chỉnh
- **04.HOL/** - Phòng thí nghiệm thực hành (bao gồm các ví dụ .NET)

### Định dạng tệp

- **Jupyter Notebooks (`.ipynb`)** - Hướng dẫn Python tương tác được đánh dấu bằng 📓 trong README
- **Python Scripts (`.py`)** - Các ví dụ Python độc lập
- **C# Projects (`.csproj`, `.sln`)** - Các ứng dụng và mẫu .NET
- **JavaScript (`.js`, `package.json`)** - Các ví dụ dựa trên web và Node.js
- **Markdown (`.md`)** - Tài liệu và hướng dẫn

## Làm việc với các ví dụ

### Chạy Jupyter Notebooks

Hầu hết các ví dụ được cung cấp dưới dạng Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Chạy Scripts Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Chạy các ví dụ .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Hoặc xây dựng toàn bộ giải pháp:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Chạy các ví dụ JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Kiểm tra

Kho tài liệu này chứa mã ví dụ và hướng dẫn thay vì một dự án phần mềm truyền thống với các bài kiểm tra đơn vị. Việc xác thực thường được thực hiện bằng cách:

1. **Chạy các ví dụ** - Mỗi ví dụ nên chạy mà không có lỗi
2. **Xác minh đầu ra** - Kiểm tra rằng phản hồi của mô hình là phù hợp
3. **Thực hiện theo hướng dẫn** - Các hướng dẫn từng bước nên hoạt động như đã được mô tả

**Phương pháp xác thực phổ biến:**
- Kiểm tra việc thực thi ví dụ trong môi trường mục tiêu
- Xác minh các phụ thuộc được cài đặt đúng cách
- Kiểm tra rằng mô hình được tải xuống/tải thành công
- Xác nhận hành vi mong đợi phù hợp với tài liệu

## Phong cách mã và quy ước

### Hướng dẫn chung

- Các ví dụ nên rõ ràng, được chú thích tốt và mang tính giáo dục
- Tuân theo các quy ước cụ thể của ngôn ngữ (PEP 8 cho Python, tiêu chuẩn C# cho .NET)
- Giữ các ví dụ tập trung vào việc trình bày các khả năng cụ thể của mô hình Phi
- Bao gồm các chú thích giải thích các khái niệm chính và tham số cụ thể của mô hình

### Tiêu chuẩn tài liệu

**Định dạng URL:**
- Sử dụng định dạng `[text](../../url)` mà không có khoảng trắng thừa
- Liên kết tương đối: Sử dụng `./` cho thư mục hiện tại, `../` cho thư mục cha
- Không sử dụng các địa phương cụ thể trong URL (tránh `/en-us/`, `/en/`)

**Hình ảnh:**
- Lưu tất cả hình ảnh trong thư mục `/imgs/`
- Sử dụng tên mô tả với các ký tự tiếng Anh, số và dấu gạch ngang
- Ví dụ: `phi-3-architecture.png`

**Tệp Markdown:**
- Tham chiếu các ví dụ hoạt động thực tế trong thư mục `/code/`
- Giữ tài liệu đồng bộ với các thay đổi mã
- Sử dụng biểu tượng 📓 để đánh dấu liên kết Jupyter notebook trong README

### Tổ chức tệp

- Các ví dụ mã trong `/code/` được tổ chức theo chủ đề/tính năng
- Tài liệu trong `/md/` phản ánh cấu trúc mã khi có thể
- Giữ các tệp liên quan (notebooks, scripts, configs) cùng nhau trong các thư mục con

## Hướng dẫn Pull Request

### Trước khi gửi

1. **Fork kho tài liệu** vào tài khoản của bạn
2. **Tách PR theo loại:**
   - Sửa lỗi trong một PR
   - Cập nhật tài liệu trong một PR khác
   - Các ví dụ mới trong các PR riêng biệt
   - Sửa lỗi chính tả có thể được kết hợp

3. **Xử lý xung đột hợp nhất:**
   - Cập nhật nhánh `main` cục bộ của bạn trước khi thực hiện thay đổi
   - Đồng bộ hóa với upstream thường xuyên

4. **PR dịch thuật:**
   - Phải bao gồm bản dịch cho TẤT CẢ các tệp trong thư mục
   - Duy trì cấu trúc nhất quán với ngôn ngữ gốc

### Kiểm tra bắt buộc

PRs tự động chạy các quy trình làm việc của GitHub để xác thực:

1. **Xác thực đường dẫn tương đối** - Tất cả các liên kết nội bộ phải hoạt động
   - Kiểm tra liên kết cục bộ: Ctrl+Click trong VS Code
   - Sử dụng gợi ý đường dẫn từ VS Code (`./` hoặc `../`)

2. **Kiểm tra địa phương URL** - Các URL web không được chứa mã ngôn ngữ quốc gia
   - Loại bỏ `/en-us/`, `/en/`, hoặc các mã ngôn ngữ khác
   - Sử dụng URL quốc tế chung

3. **Kiểm tra URL hỏng** - Tất cả URL phải trả về trạng thái 200
   - Xác minh các liên kết có thể truy cập trước khi gửi
   - Lưu ý: Một số lỗi có thể do hạn chế mạng

### Định dạng tiêu đề PR

```
[component] Brief description
```

Ví dụ:
- `[docs] Thêm hướng dẫn suy luận Phi-4`
- `[code] Sửa ví dụ tích hợp ONNX Runtime`
- `[translation] Thêm bản dịch tiếng Nhật cho hướng dẫn giới thiệu`

## Mẫu phát triển phổ biến

### Làm việc với các mô hình Phi

**Tải mô hình:**
- Các ví dụ sử dụng nhiều khung làm việc: Transformers, ONNX Runtime, MLX, OpenVINO
- Các mô hình thường được tải xuống từ Hugging Face, Azure hoặc GitHub Models
- Kiểm tra khả năng tương thích của mô hình với phần cứng của bạn (CPU, GPU, NPU)

**Mẫu suy luận:**
- Tạo văn bản: Hầu hết các ví dụ sử dụng các biến thể chat/instruct
- Hình ảnh: Phi-3-vision và Phi-4-multimodal để hiểu hình ảnh
- Âm thanh: Phi-4-multimodal hỗ trợ đầu vào âm thanh
- Lý luận: Các biến thể Phi-4-reasoning cho các tác vụ lý luận nâng cao

### Ghi chú cụ thể theo nền tảng

**Azure AI Foundry:**
- Yêu cầu đăng ký Azure và khóa API
- Xem `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Có sẵn gói miễn phí để thử nghiệm
- Xem `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Suy luận cục bộ:**
- ONNX Runtime: Suy luận tối ưu, đa nền tảng
- Ollama: Quản lý mô hình cục bộ dễ dàng (được cấu hình sẵn trong container phát triển)
- Apple MLX: Tối ưu hóa cho Apple Silicon

## Xử lý sự cố

### Các vấn đề thường gặp

**Vấn đề bộ nhớ:**
- Các mô hình Phi yêu cầu RAM lớn (đặc biệt là các biến thể hình ảnh/đa phương tiện)
- Sử dụng các mô hình lượng hóa cho môi trường hạn chế tài nguyên
- Xem `/md/01.Introduction/04/QuantifyingPhi.md`

**Xung đột phụ thuộc:**
- Các ví dụ Python có thể yêu cầu phiên bản cụ thể
- Sử dụng môi trường ảo cho mỗi ví dụ
- Kiểm tra các tệp `requirements.txt` riêng lẻ

**Lỗi tải xuống mô hình:**
- Các mô hình lớn có thể bị hết thời gian chờ trên kết nối chậm
- Cân nhắc sử dụng môi trường đám mây (Codespaces, Azure)
- Kiểm tra bộ nhớ cache Hugging Face: `~/.cache/huggingface/`

**Vấn đề dự án .NET:**
- Đảm bảo .NET 8.0 SDK được cài đặt
- Sử dụng `dotnet restore` trước khi xây dựng
- Một số dự án có cấu hình cụ thể cho CUDA (Debug_Cuda)

**Ví dụ JavaScript/Web:**
- Sử dụng Node.js 18+ để đảm bảo tương thích
- Xóa `node_modules` và cài đặt lại nếu gặp vấn đề
- Kiểm tra bảng điều khiển trình duyệt để tìm vấn đề tương thích WebGPU

### Nhận hỗ trợ

- **Discord:** Tham gia cộng đồng Discord của Azure AI Foundry
- **GitHub Issues:** Báo cáo lỗi và vấn đề trong kho tài liệu
- **GitHub Discussions:** Đặt câu hỏi và chia sẻ kiến thức

## Ngữ cảnh bổ sung

### AI có trách nhiệm

Tất cả việc sử dụng mô hình Phi nên tuân theo các nguyên tắc AI có trách nhiệm của Microsoft:
- Công bằng, đáng tin cậy, an toàn
- Quyền riêng tư và bảo mật  
- Tính bao trùm, minh bạch, trách nhiệm
- Sử dụng Azure AI Content Safety cho các ứng dụng sản xuất
- Xem `/md/01.Introduction/01/01.AISafety.md`

### Dịch thuật

- Hỗ trợ hơn 50 ngôn ngữ thông qua GitHub Action tự động
- Các bản dịch nằm trong thư mục `/translations/`
- Được duy trì bởi quy trình làm việc co-op-translator
- Không chỉnh sửa thủ công các tệp đã dịch (tự động tạo)

### Đóng góp

- Tuân theo hướng dẫn trong `CONTRIBUTING.md`
- Đồng ý với Thỏa thuận cấp phép của người đóng góp (CLA)
- Tuân thủ Quy tắc ứng xử mã nguồn mở của Microsoft
- Không để lộ thông tin bảo mật và thông tin đăng nhập trong các lần commit

### Hỗ trợ đa ngôn ngữ

Đây là một kho tài liệu đa ngôn ngữ với các ví dụ trong:
- **Python** - Quy trình làm việc ML/AI, Jupyter notebooks, tinh chỉnh
- **C#/.NET** - Ứng dụng doanh nghiệp, tích hợp ONNX Runtime
- **JavaScript** - AI dựa trên web, suy luận trên trình duyệt với WebGPU

Chọn ngôn ngữ phù hợp nhất với trường hợp sử dụng và mục tiêu triển khai của bạn.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.