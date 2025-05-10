<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:42:10+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Contributing

Dự án này hoan nghênh các đóng góp và đề xuất. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Đóng góp (CLA) xác nhận rằng bạn có quyền, và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết chi tiết, hãy truy cập [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Khi bạn gửi một pull request, bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA và trang trí PR cho phù hợp (ví dụ: kiểm tra trạng thái, bình luận). Chỉ cần làm theo hướng dẫn do bot cung cấp. Bạn chỉ cần thực hiện việc này một lần cho tất cả các kho dùng CLA của chúng tôi.

## Code of Conduct

Dự án này đã áp dụng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Để biết thêm thông tin, đọc [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) hoặc liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có câu hỏi hoặc ý kiến bổ sung.

## Cautions for creating issues

Vui lòng không mở các issue trên GitHub cho các câu hỏi hỗ trợ chung vì danh sách GitHub nên được dùng cho các yêu cầu tính năng và báo lỗi. Bằng cách này, chúng ta có thể dễ dàng theo dõi các vấn đề hoặc lỗi thực sự từ mã và giữ cuộc thảo luận chung tách biệt với mã nguồn.

## How to Contribute

### Pull Requests Guidelines

Khi gửi pull request (PR) đến kho Phi-3 CookBook, vui lòng sử dụng các hướng dẫn sau:

- **Fork Repository**: Luôn fork kho về tài khoản của bạn trước khi thực hiện các chỉnh sửa.

- **Tách riêng các pull request (PR)**:
  - Gửi mỗi loại thay đổi trong một pull request riêng. Ví dụ, sửa lỗi và cập nhật tài liệu nên được gửi trong các PR riêng biệt.
  - Các sửa lỗi chính tả và cập nhật tài liệu nhỏ có thể được gộp vào một PR khi phù hợp.

- **Xử lý xung đột merge**: Nếu pull request của bạn có xung đột merge, hãy cập nhật nhánh `main` cục bộ của bạn để đồng bộ với kho chính trước khi chỉnh sửa.

- **Gửi bản dịch**: Khi gửi PR bản dịch, đảm bảo thư mục bản dịch bao gồm bản dịch cho tất cả các file trong thư mục gốc.

### Translation Guidelines

> [!IMPORTANT]
>
> Khi dịch văn bản trong kho này, không sử dụng dịch máy. Chỉ nhận dịch những ngôn ngữ mà bạn thành thạo.

Nếu bạn thành thạo một ngôn ngữ không phải tiếng Anh, bạn có thể giúp dịch nội dung. Làm theo các bước dưới đây để đảm bảo đóng góp dịch được tích hợp đúng cách, vui lòng sử dụng các hướng dẫn sau:

- **Tạo thư mục dịch**: Điều hướng đến thư mục phần thích hợp và tạo thư mục dịch cho ngôn ngữ bạn đóng góp. Ví dụ:
  - Với phần introduction: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Với phần quick start: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Tiếp tục tương tự với các phần khác (03.Inference, 04.Finetuning, v.v.)

- **Cập nhật đường dẫn tương đối**: Khi dịch, điều chỉnh cấu trúc thư mục bằng cách thêm `../../` vào đầu các đường dẫn tương đối trong file markdown để đảm bảo các liên kết hoạt động chính xác. Ví dụ, thay đổi:
  - `(../../imgs/01/phi3aisafety.png)` thành `(../../../../imgs/01/phi3aisafety.png)`

- **Tổ chức bản dịch**: Mỗi file dịch nên được đặt trong thư mục dịch tương ứng với phần. Ví dụ, nếu bạn dịch phần introduction sang tiếng Tây Ban Nha, bạn sẽ tạo như sau:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Gửi PR hoàn chỉnh**: Đảm bảo tất cả file dịch cho một phần đều được bao gồm trong một PR. Chúng tôi không chấp nhận bản dịch một phần cho một phần. Khi gửi PR dịch, đảm bảo thư mục dịch bao gồm bản dịch cho tất cả file trong thư mục gốc.

### Writing Guidelines

Để đảm bảo tính nhất quán trên tất cả tài liệu, vui lòng sử dụng các hướng dẫn sau:

- **Định dạng URL**: Bao tất cả URL trong dấu ngoặc vuông, theo sau là dấu ngoặc tròn, không có khoảng trắng thừa bên trong hoặc xung quanh. Ví dụ: `[example](https://www.microsoft.com)`.

- **Liên kết tương đối**: Sử dụng `./` cho liên kết tương đối trỏ tới file hoặc thư mục trong thư mục hiện tại, và `../` cho liên kết tới thư mục cha. Ví dụ: `[example](../../path/to/file)` hoặc `[example](../../../path/to/file)`.

- **Không dùng locale theo quốc gia**: Đảm bảo liên kết của bạn không bao gồm locale theo quốc gia. Ví dụ, tránh `/en-us/` hoặc `/en/`.

- **Lưu trữ hình ảnh**: Lưu tất cả hình ảnh trong thư mục `./imgs`.

- **Đặt tên hình ảnh mô tả**: Đặt tên hình ảnh bằng các ký tự tiếng Anh, số và dấu gạch ngang. Ví dụ: `example-image.jpg`.

## GitHub Workflows

Khi bạn gửi pull request, các workflow sau sẽ được kích hoạt để kiểm tra các thay đổi. Làm theo hướng dẫn dưới đây để đảm bảo pull request của bạn vượt qua các kiểm tra workflow:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Workflow này đảm bảo tất cả đường dẫn tương đối trong file của bạn đều chính xác.

1. Để chắc chắn các liên kết hoạt động đúng, thực hiện các bước sau bằng VS Code:
    - Di chuột qua bất kỳ liên kết nào trong file.
    - Nhấn **Ctrl + Click** để điều hướng đến liên kết.
    - Nếu bạn nhấp vào liên kết mà không hoạt động trên máy cục bộ, workflow sẽ kích hoạt và liên kết sẽ không hoạt động trên GitHub.

1. Để sửa lỗi này, thực hiện các bước sau dựa trên gợi ý đường dẫn của VS Code:
    - Gõ `./` hoặc `../`.
    - VS Code sẽ gợi ý các lựa chọn dựa trên những gì bạn đã gõ.
    - Theo dõi đường dẫn bằng cách nhấp vào file hoặc thư mục mong muốn để đảm bảo đường dẫn chính xác.

Sau khi thêm đúng đường dẫn tương đối, lưu và đẩy thay đổi của bạn.

### Check URLs Don't Have Locale

Workflow này đảm bảo bất kỳ URL web nào cũng không bao gồm locale theo quốc gia. Vì kho này truy cập toàn cầu, nên cần đảm bảo URL không chứa locale quốc gia của bạn.

1. Để kiểm tra URL không có locale quốc gia, thực hiện các bước sau:

    - Kiểm tra các đoạn văn bản như `/en-us/`, `/en/` hoặc bất kỳ locale ngôn ngữ nào trong URL.
    - Nếu không có trong URL, bạn sẽ vượt qua kiểm tra này.

1. Để sửa lỗi, thực hiện các bước sau:
    - Mở file được workflow đánh dấu.
    - Xóa locale quốc gia khỏi URL.

Sau khi xóa locale quốc gia, lưu và đẩy thay đổi của bạn.

### Check Broken Urls

Workflow này đảm bảo bất kỳ URL web nào trong file của bạn đều hoạt động và trả về mã trạng thái 200.

1. Để kiểm tra URL hoạt động đúng, thực hiện các bước sau:
    - Kiểm tra trạng thái của các URL trong file.

2. Để sửa URL hỏng, thực hiện các bước sau:
    - Mở file chứa URL hỏng.
    - Cập nhật URL thành đúng.

Sau khi sửa URL, lưu và đẩy thay đổi của bạn.

> [!NOTE]
>
> Có thể có trường hợp kiểm tra URL thất bại dù liên kết vẫn truy cập được. Điều này có thể do một số nguyên nhân, bao gồm:
>
> - **Hạn chế mạng:** Máy chủ GitHub Actions có thể bị hạn chế mạng không truy cập được một số URL.
> - **Lỗi timeout:** URL phản hồi chậm có thể gây lỗi timeout trong workflow.
> - **Sự cố máy chủ tạm thời:** Đôi khi máy chủ bảo trì hoặc ngừng hoạt động tạm thời khiến URL không truy cập được trong quá trình kiểm tra.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn thông tin chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.