<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:35:05+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Đóng góp

Dự án này hoan nghênh các đóng góp và đề xuất. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Đóng góp (CLA) xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết chi tiết, vui lòng truy cập [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Khi bạn gửi pull request, một bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và đánh dấu PR phù hợp (ví dụ: kiểm tra trạng thái, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần thực hiện việc này một lần cho tất cả các kho lưu trữ sử dụng CLA của chúng tôi.

## Quy tắc ứng xử

Dự án này đã áp dụng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Để biết thêm thông tin, hãy đọc [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) hoặc liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có câu hỏi hoặc góp ý thêm.

## Lưu ý khi tạo issue

Vui lòng không mở issue trên GitHub cho các câu hỏi hỗ trợ chung vì danh sách GitHub nên được dùng cho các yêu cầu tính năng và báo lỗi. Cách này giúp chúng tôi dễ dàng theo dõi các vấn đề hoặc lỗi thực sự từ mã nguồn và giữ cho các cuộc thảo luận chung tách biệt với mã nguồn.

## Cách đóng góp

### Hướng dẫn Pull Request

Khi gửi pull request (PR) đến kho Phi-3 CookBook, vui lòng tuân theo các hướng dẫn sau:

- **Fork kho lưu trữ**: Luôn fork kho lưu trữ về tài khoản của bạn trước khi thực hiện chỉnh sửa.

- **Tách riêng các pull request (PR)**:
  - Gửi mỗi loại thay đổi trong một pull request riêng. Ví dụ, sửa lỗi và cập nhật tài liệu nên được gửi trong các PR riêng biệt.
  - Sửa lỗi chính tả và cập nhật tài liệu nhỏ có thể gộp chung trong một PR nếu phù hợp.

- **Xử lý xung đột khi merge**: Nếu pull request của bạn có xung đột khi merge, hãy cập nhật nhánh `main` cục bộ của bạn để đồng bộ với kho chính trước khi chỉnh sửa.

- **Gửi bản dịch**: Khi gửi PR bản dịch, đảm bảo thư mục bản dịch bao gồm bản dịch cho tất cả các tệp trong thư mục gốc.

### Hướng dẫn viết

Để đảm bảo sự nhất quán trên tất cả tài liệu, vui lòng tuân theo các hướng dẫn sau:

- **Định dạng URL**: Bao tất cả URL trong dấu ngoặc vuông, theo sau là dấu ngoặc tròn, không có khoảng trắng thừa bên trong hoặc xung quanh. Ví dụ: `[example](https://www.microsoft.com)`.

- **Liên kết tương đối**: Sử dụng `./` cho liên kết tương đối đến tệp hoặc thư mục trong thư mục hiện tại, và `../` cho thư mục cha. Ví dụ: `[example](../../path/to/file)` hoặc `[example](../../../path/to/file)`.

- **Không dùng locale theo quốc gia**: Đảm bảo liên kết của bạn không chứa locale theo quốc gia. Ví dụ, tránh dùng `/en-us/` hoặc `/en/`.

- **Lưu trữ hình ảnh**: Lưu tất cả hình ảnh trong thư mục `./imgs`.

- **Tên hình ảnh mô tả**: Đặt tên hình ảnh rõ ràng bằng ký tự tiếng Anh, số và dấu gạch ngang. Ví dụ: `example-image.jpg`.

## Quy trình làm việc trên GitHub

Khi bạn gửi pull request, các quy trình làm việc sau sẽ được kích hoạt để kiểm tra các thay đổi. Hãy làm theo hướng dẫn dưới đây để đảm bảo pull request của bạn vượt qua các kiểm tra:

- [Kiểm tra đường dẫn tương đối bị hỏng](../..)
- [Kiểm tra URL không chứa locale](../..)

### Kiểm tra đường dẫn tương đối bị hỏng

Quy trình này đảm bảo tất cả đường dẫn tương đối trong tệp của bạn là chính xác.

1. Để đảm bảo liên kết hoạt động đúng, thực hiện các bước sau trong VS Code:
    - Di chuột qua bất kỳ liên kết nào trong tệp.
    - Nhấn **Ctrl + Click** để điều hướng đến liên kết.
    - Nếu bạn nhấp vào liên kết mà không hoạt động trên máy cục bộ, quy trình sẽ được kích hoạt và liên kết sẽ không hoạt động trên GitHub.

1. Để sửa lỗi này, thực hiện các bước sau dựa trên gợi ý đường dẫn của VS Code:
    - Gõ `./` hoặc `../`.
    - VS Code sẽ gợi ý các tùy chọn dựa trên những gì bạn đã gõ.
    - Theo đường dẫn bằng cách nhấp vào tệp hoặc thư mục mong muốn để đảm bảo đường dẫn chính xác.

Sau khi thêm đường dẫn tương đối đúng, lưu và đẩy các thay đổi của bạn.

### Kiểm tra URL không chứa locale

Quy trình này đảm bảo bất kỳ URL web nào cũng không chứa locale theo quốc gia. Vì kho lưu trữ này có thể truy cập toàn cầu, nên cần đảm bảo URL không chứa locale quốc gia của bạn.

1. Để kiểm tra URL không chứa locale quốc gia, thực hiện các bước sau:

    - Kiểm tra xem có văn bản như `/en-us/`, `/en/` hoặc bất kỳ locale ngôn ngữ nào trong URL không.
    - Nếu không có, bạn sẽ vượt qua kiểm tra này.

1. Để sửa lỗi này, thực hiện các bước sau:
    - Mở tệp được quy trình làm việc đánh dấu.
    - Xóa locale quốc gia khỏi URL.

Sau khi xóa locale quốc gia, lưu và đẩy các thay đổi.

### Kiểm tra URL bị hỏng

Quy trình này đảm bảo bất kỳ URL web nào trong tệp của bạn đều hoạt động và trả về mã trạng thái 200.

1. Để kiểm tra URL hoạt động đúng, thực hiện các bước sau:
    - Kiểm tra trạng thái của các URL trong tệp.

2. Để sửa URL bị hỏng, thực hiện các bước sau:
    - Mở tệp chứa URL bị hỏng.
    - Cập nhật URL đúng.

Sau khi sửa URL, lưu và đẩy các thay đổi.

> [!NOTE]
>
> Có thể xảy ra trường hợp kiểm tra URL thất bại dù liên kết vẫn truy cập được. Điều này có thể do một số lý do, bao gồm:
>
> - **Hạn chế mạng:** Máy chủ GitHub actions có thể bị hạn chế mạng khiến không truy cập được một số URL.
> - **Lỗi timeout:** URL phản hồi chậm có thể gây lỗi timeout trong quy trình.
> - **Sự cố máy chủ tạm thời:** Máy chủ đôi khi ngừng hoạt động hoặc bảo trì khiến URL tạm thời không truy cập được trong quá trình kiểm tra.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.