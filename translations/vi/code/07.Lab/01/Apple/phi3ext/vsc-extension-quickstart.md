<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:09:08+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "vi"
}
-->
# Chào mừng bạn đến với Extension VS Code của bạn

## Thư mục này có gì

* Thư mục này chứa tất cả các tệp cần thiết cho extension của bạn.
* `package.json` - đây là tệp manifest, nơi bạn khai báo extension và lệnh của mình.
  * Plugin mẫu đăng ký một lệnh và định nghĩa tiêu đề cùng tên lệnh. Với thông tin này, VS Code có thể hiển thị lệnh trong command palette. Lúc này chưa cần tải plugin.
* `src/extension.ts` - đây là tệp chính, nơi bạn sẽ cung cấp phần triển khai cho lệnh của mình.
  * Tệp này xuất ra một hàm duy nhất, `activate`, được gọi lần đầu tiên khi extension được kích hoạt (trong trường hợp này là khi thực thi lệnh). Bên trong hàm `activate`, chúng ta gọi `registerCommand`.
  * Chúng ta truyền hàm chứa phần triển khai lệnh làm tham số thứ hai cho `registerCommand`.

## Cài đặt

* cài đặt các extension được đề xuất (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, và dbaeumer.vscode-eslint)

## Bắt đầu ngay lập tức

* Nhấn `F5` để mở cửa sổ mới với extension của bạn đã được tải.
* Chạy lệnh của bạn từ command palette bằng cách nhấn (`Ctrl+Shift+P` hoặc `Cmd+Shift+P` trên Mac) và gõ `Hello World`.
* Đặt điểm dừng trong mã của bạn ở `src/extension.ts` để gỡ lỗi extension.
* Xem kết quả đầu ra từ extension trong cửa sổ debug console.

## Thay đổi

* Bạn có thể khởi động lại extension từ thanh công cụ debug sau khi thay đổi mã trong `src/extension.ts`.
* Bạn cũng có thể tải lại (`Ctrl+R` hoặc `Cmd+R` trên Mac) cửa sổ VS Code với extension của bạn để áp dụng thay đổi.

## Khám phá API

* Bạn có thể mở toàn bộ API của chúng tôi khi mở tệp `node_modules/@types/vscode/index.d.ts`.

## Chạy kiểm thử

* Cài đặt [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Chạy tác vụ "watch" thông qua lệnh **Tasks: Run Task**. Đảm bảo tác vụ này đang chạy, nếu không các kiểm thử có thể không được phát hiện.
* Mở giao diện Testing từ thanh hoạt động và nhấn nút Run Test, hoặc sử dụng phím tắt `Ctrl/Cmd + ; A`
* Xem kết quả kiểm thử trong cửa sổ Test Results.
* Thay đổi `src/test/extension.test.ts` hoặc tạo các tệp kiểm thử mới trong thư mục `test`.
  * Trình chạy kiểm thử chỉ xem các tệp có tên phù hợp với mẫu `**.test.ts`.
  * Bạn có thể tạo thư mục con trong `test` để tổ chức các kiểm thử theo ý muốn.

## Tiếp tục phát triển

* Giảm kích thước extension và cải thiện thời gian khởi động bằng cách [gói extension của bạn](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Phát hành extension của bạn](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) trên marketplace của VS Code.
* Tự động hóa quá trình build bằng cách thiết lập [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.