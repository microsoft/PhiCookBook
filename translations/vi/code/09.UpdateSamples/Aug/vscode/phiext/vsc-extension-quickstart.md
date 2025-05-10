<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:40:05+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "vi"
}
-->
# Chào mừng bạn đến với VS Code Extension của bạn

## Những gì có trong thư mục

* Thư mục này chứa tất cả các tệp cần thiết cho extension của bạn.
* `package.json` - đây là tệp manifest nơi bạn khai báo extension và lệnh của mình.
  * Plugin mẫu đăng ký một lệnh và định nghĩa tiêu đề cùng tên lệnh. Với thông tin này, VS Code có thể hiển thị lệnh trong bảng lệnh. Nó chưa cần tải plugin ngay.
* `src/extension.ts` - đây là tệp chính nơi bạn sẽ cung cấp phần triển khai cho lệnh của mình.
  * Tệp này xuất ra một hàm, `activate`, được gọi lần đầu tiên khi extension của bạn được kích hoạt (trong trường hợp này bằng cách thực thi lệnh). Bên trong hàm `activate`, chúng ta gọi `registerCommand`.
  * Chúng ta truyền hàm chứa phần triển khai lệnh làm tham số thứ hai cho `registerCommand`.

## Cài đặt

* cài đặt các extension được khuyến nghị (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, và dbaeumer.vscode-eslint)


## Bắt đầu ngay lập tức

* Nhấn `F5` để mở một cửa sổ mới với extension của bạn đã được tải.
* Chạy lệnh của bạn từ bảng lệnh bằng cách nhấn (`Ctrl+Shift+P` hoặc `Cmd+Shift+P` trên Mac) và gõ `Hello World`.
* Đặt breakpoint trong mã của bạn bên trong `src/extension.ts` để gỡ lỗi extension.
* Xem kết quả đầu ra từ extension trong bảng điều khiển gỡ lỗi.

## Thay đổi

* Bạn có thể khởi động lại extension từ thanh công cụ gỡ lỗi sau khi thay đổi mã trong `src/extension.ts`.
* Bạn cũng có thể tải lại (`Ctrl+R` hoặc `Cmd+R` trên Mac) cửa sổ VS Code với extension của bạn để áp dụng thay đổi.


## Khám phá API

* Bạn có thể mở toàn bộ bộ API của chúng tôi khi mở tệp `node_modules/@types/vscode/index.d.ts`.

## Chạy kiểm thử

* Cài đặt [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Chạy tác vụ "watch" qua lệnh **Tasks: Run Task**. Đảm bảo tác vụ này đang chạy, nếu không kiểm thử có thể không được phát hiện.
* Mở giao diện Testing từ thanh hoạt động và nhấn nút "Run Test", hoặc dùng phím tắt `Ctrl/Cmd + ; A`
* Xem kết quả kiểm thử trong giao diện Test Results.
* Thay đổi `src/test/extension.test.ts` hoặc tạo các tệp kiểm thử mới trong thư mục `test`.
  * Trình chạy kiểm thử chỉ xem các tệp khớp với mẫu tên `**.test.ts`.
  * Bạn có thể tạo thư mục bên trong `test` để tổ chức các kiểm thử theo ý muốn.

## Tiến xa hơn

* Giảm kích thước extension và cải thiện thời gian khởi động bằng cách [gộp extension của bạn](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Xuất bản extension của bạn](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) trên marketplace của VS Code.
* Tự động hóa quá trình build bằng cách thiết lập [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.