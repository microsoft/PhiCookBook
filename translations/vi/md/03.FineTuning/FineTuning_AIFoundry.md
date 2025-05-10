<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-05-09T20:34:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "vi"
}
-->
# Tinh chỉnh Phi-3 với Azure AI Foundry

Hãy cùng khám phá cách tinh chỉnh mô hình ngôn ngữ Phi-3 Mini của Microsoft bằng Azure AI Foundry. Tinh chỉnh giúp bạn điều chỉnh Phi-3 Mini cho các nhiệm vụ cụ thể, làm cho nó mạnh mẽ hơn và hiểu ngữ cảnh tốt hơn.

## Những điều cần lưu ý

- **Khả năng:** Những mô hình nào có thể tinh chỉnh? Mô hình gốc có thể được tinh chỉnh để làm gì?
- **Chi phí:** Mô hình giá cho việc tinh chỉnh như thế nào?
- **Tùy chỉnh:** Tôi có thể chỉnh sửa mô hình gốc đến mức nào – và bằng cách nào?
- **Tiện lợi:** Quá trình tinh chỉnh diễn ra ra sao – tôi có cần viết mã riêng không? Tôi có cần cung cấp tài nguyên tính toán không?
- **An toàn:** Mô hình tinh chỉnh có thể gặp rủi ro về an toàn – có các biện pháp bảo vệ nào để tránh gây hại không mong muốn không?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.vi.png)

## Chuẩn bị cho việc tinh chỉnh

### Yêu cầu trước

> [!NOTE]
> Đối với các mô hình thuộc họ Phi-3, dịch vụ tinh chỉnh theo mô hình trả theo mức sử dụng chỉ khả dụng với các hub tạo tại khu vực **East US 2**.

- Một tài khoản Azure. Nếu bạn chưa có, hãy tạo một [tài khoản Azure trả phí](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) để bắt đầu.

- Một [dự án AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure sử dụng kiểm soát truy cập dựa trên vai trò (Azure RBAC) để cấp quyền cho các thao tác trong Azure AI Foundry. Để thực hiện các bước trong bài viết này, tài khoản người dùng của bạn cần được gán __vai trò Azure AI Developer__ trên nhóm tài nguyên.

### Đăng ký nhà cung cấp dịch vụ đăng ký

Xác nhận đăng ký của bạn đã đăng ký nhà cung cấp tài nguyên `Microsoft.Network`.

1. Đăng nhập vào [cổng Azure](https://portal.azure.com).
1. Chọn **Subscriptions** từ menu bên trái.
1. Chọn đăng ký bạn muốn sử dụng.
1. Chọn **AI project settings** > **Resource providers** từ menu bên trái.
1. Xác nhận rằng **Microsoft.Network** có trong danh sách nhà cung cấp tài nguyên. Nếu chưa có, hãy thêm vào.

### Chuẩn bị dữ liệu

Chuẩn bị dữ liệu huấn luyện và kiểm tra để tinh chỉnh mô hình. Bộ dữ liệu huấn luyện và kiểm tra gồm các ví dụ đầu vào và đầu ra thể hiện cách bạn muốn mô hình hoạt động.

Đảm bảo tất cả ví dụ huấn luyện tuân theo định dạng mong đợi để suy luận. Để tinh chỉnh hiệu quả, hãy đảm bảo bộ dữ liệu cân bằng và đa dạng.

Điều này bao gồm duy trì sự cân bằng dữ liệu, bao gồm nhiều kịch bản khác nhau, và định kỳ tinh chỉnh dữ liệu huấn luyện để phù hợp với thực tế, giúp mô hình trả lời chính xác và cân bằng hơn.

Các loại mô hình khác nhau yêu cầu định dạng dữ liệu huấn luyện khác nhau.

### Hoàn thành Chat

Dữ liệu huấn luyện và kiểm tra bạn sử dụng **phải** được định dạng dưới dạng JSON Lines (JSONL). Với `Phi-3-mini-128k-instruct`, bộ dữ liệu tinh chỉnh phải theo định dạng hội thoại mà API Chat completions sử dụng.

### Ví dụ định dạng file

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Loại file được hỗ trợ là JSON Lines. File được tải lên kho dữ liệu mặc định và có sẵn trong dự án của bạn.

## Tinh chỉnh Phi-3 với Azure AI Foundry

Azure AI Foundry cho phép bạn tùy chỉnh các mô hình ngôn ngữ lớn dựa trên bộ dữ liệu cá nhân thông qua quá trình gọi là tinh chỉnh. Tinh chỉnh mang lại giá trị lớn bằng cách cho phép tùy biến và tối ưu hóa cho các nhiệm vụ và ứng dụng cụ thể. Kết quả là hiệu suất cải thiện, tiết kiệm chi phí, giảm độ trễ và đầu ra được cá nhân hóa.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.vi.png)

### Tạo dự án mới

1. Đăng nhập vào [Azure AI Foundry](https://ai.azure.com).

1. Chọn **+New project** để tạo dự án mới trong Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.vi.png)

1. Thực hiện các bước sau:

    - Tên **Hub name** của dự án. Phải là giá trị duy nhất.
    - Chọn **Hub** để sử dụng (tạo mới nếu cần).

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.vi.png)

1. Thực hiện các bước sau để tạo một hub mới:

    - Nhập **Hub name**. Phải là giá trị duy nhất.
    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Location** bạn muốn sử dụng.
    - Chọn **Connect Azure AI Services** để sử dụng (tạo mới nếu cần).
    - Chọn **Connect Azure AI Search** và chọn **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.vi.png)

1. Chọn **Next**.
1. Chọn **Create a project**.

### Chuẩn bị dữ liệu

Trước khi tinh chỉnh, hãy thu thập hoặc tạo bộ dữ liệu phù hợp với nhiệm vụ của bạn, như hướng dẫn chat, cặp câu hỏi-trả lời hoặc các dữ liệu văn bản liên quan khác. Làm sạch và tiền xử lý dữ liệu bằng cách loại bỏ nhiễu, xử lý giá trị thiếu và phân tách từ.

### Tinh chỉnh mô hình Phi-3 trong Azure AI Foundry

> [!NOTE]
> Việc tinh chỉnh mô hình Phi-3 hiện chỉ hỗ trợ trong các dự án đặt tại khu vực East US 2.

1. Chọn **Model catalog** từ tab bên trái.

1. Gõ *phi-3* trong **thanh tìm kiếm** và chọn mô hình phi-3 bạn muốn sử dụng.

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.vi.png)

1. Chọn **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.vi.png)

1. Nhập **Fine-tuned model name**.

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.vi.png)

1. Chọn **Next**.

1. Thực hiện các bước sau:

    - Chọn **task type** là **Chat completion**.
    - Chọn **Training data** bạn muốn sử dụng. Bạn có thể tải lên qua dữ liệu của Azure AI Foundry hoặc từ máy tính cá nhân.

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.vi.png)

1. Chọn **Next**.

1. Tải lên **Validation data** bạn muốn dùng, hoặc chọn **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.vi.png)

1. Chọn **Next**.

1. Thực hiện các bước sau:

    - Chọn **Batch size multiplier** bạn muốn dùng.
    - Chọn **Learning rate** bạn muốn dùng.
    - Chọn **Epochs** bạn muốn dùng.

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.vi.png)

1. Chọn **Submit** để bắt đầu quá trình tinh chỉnh.

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.vi.png)

1. Khi mô hình đã được tinh chỉnh, trạng thái sẽ hiển thị là **Completed**, như hình dưới. Bây giờ bạn có thể triển khai mô hình và sử dụng nó trong ứng dụng của bạn, trong playground, hoặc trong prompt flow. Để biết thêm chi tiết, xem [Cách triển khai họ mô hình ngôn ngữ nhỏ Phi-3 với Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.vi.png)

> [!NOTE]
> Để biết thông tin chi tiết hơn về tinh chỉnh Phi-3, vui lòng truy cập [Tinh chỉnh mô hình Phi-3 trong Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Xóa các mô hình đã tinh chỉnh

Bạn có thể xóa một mô hình đã tinh chỉnh từ danh sách mô hình tinh chỉnh trong [Azure AI Foundry](https://ai.azure.com) hoặc từ trang chi tiết mô hình. Chọn mô hình đã tinh chỉnh muốn xóa trên trang Fine-tuning, rồi chọn nút Delete để xóa mô hình đó.

> [!NOTE]
> Bạn không thể xóa một mô hình tùy chỉnh nếu nó đang có triển khai. Bạn phải xóa triển khai mô hình trước khi có thể xóa mô hình tùy chỉnh.

## Chi phí và hạn mức

### Cân nhắc chi phí và hạn mức cho các mô hình Phi-3 tinh chỉnh như dịch vụ

Các mô hình Phi được tinh chỉnh như dịch vụ do Microsoft cung cấp và tích hợp với Azure AI Foundry để sử dụng. Bạn có thể xem giá khi [triển khai](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) hoặc tinh chỉnh mô hình trong tab Pricing and terms trên trình hướng dẫn triển khai.

## Lọc nội dung

Các mô hình triển khai dưới dạng dịch vụ trả theo mức sử dụng được bảo vệ bởi Azure AI Content Safety. Khi triển khai trên các endpoint thời gian thực, bạn có thể chọn không sử dụng tính năng này. Khi bật Azure AI Content Safety, cả prompt và kết quả trả về đều được kiểm tra qua một tập hợp các mô hình phân loại nhằm phát hiện và ngăn chặn nội dung có hại. Hệ thống lọc nội dung phát hiện và xử lý các loại nội dung có khả năng gây hại trong cả prompt đầu vào và kết quả trả về. Tìm hiểu thêm về [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Cấu hình tinh chỉnh**

Các siêu tham số: Định nghĩa các siêu tham số như tốc độ học, kích thước batch, và số epoch huấn luyện.

**Hàm mất mát**

Chọn hàm mất mát phù hợp cho nhiệm vụ của bạn (ví dụ: cross-entropy).

**Bộ tối ưu**

Chọn bộ tối ưu (ví dụ: Adam) để cập nhật gradient trong quá trình huấn luyện.

**Quy trình tinh chỉnh**

- Tải mô hình đã được huấn luyện trước: Tải checkpoint Phi-3 Mini.
- Thêm lớp tùy chỉnh: Thêm các lớp đặc thù cho nhiệm vụ (ví dụ: lớp phân loại cho hướng dẫn chat).

**Huấn luyện mô hình**

Tinh chỉnh mô hình sử dụng bộ dữ liệu đã chuẩn bị. Theo dõi tiến trình huấn luyện và điều chỉnh siêu tham số khi cần.

**Đánh giá và xác thực**

Bộ kiểm tra: Chia dữ liệu thành bộ huấn luyện và bộ kiểm tra.

**Đánh giá hiệu suất**

Sử dụng các chỉ số như độ chính xác, điểm F1, hoặc perplexity để đánh giá hiệu suất mô hình.

## Lưu mô hình đã tinh chỉnh

**Checkpoint**

Lưu checkpoint mô hình đã tinh chỉnh để sử dụng sau này.

## Triển khai

- Triển khai dưới dạng dịch vụ web: Triển khai mô hình đã tinh chỉnh như dịch vụ web trong Azure AI Foundry.
- Kiểm tra endpoint: Gửi các truy vấn thử nghiệm đến endpoint đã triển khai để xác minh chức năng.

## Lặp lại và cải thiện

Lặp lại: Nếu hiệu suất chưa đạt yêu cầu, hãy điều chỉnh siêu tham số, thêm dữ liệu, hoặc tinh chỉnh thêm các epoch.

## Giám sát và tinh chỉnh

Theo dõi liên tục hành vi của mô hình và tinh chỉnh khi cần thiết.

## Tùy chỉnh và mở rộng

Nhiệm vụ tùy chỉnh: Phi-3 Mini có thể được tinh chỉnh cho nhiều nhiệm vụ khác ngoài hướng dẫn chat. Hãy khám phá các trường hợp sử dụng khác!
Thử nghiệm: Thử các kiến trúc khác nhau, kết hợp các lớp và kỹ thuật để nâng cao hiệu suất.

> [!NOTE]
> Tinh chỉnh là một quá trình lặp đi lặp lại. Hãy thử nghiệm, học hỏi và điều chỉnh mô hình để đạt kết quả tốt nhất cho nhiệm vụ cụ thể của bạn!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.