<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:12:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "vi"
}
-->
# Tổng Quan Dự Án Phi-3-Vision-128K-Instruct

## Mô Hình

Phi-3-Vision-128K-Instruct, một mô hình đa phương tiện nhẹ và tiên tiến, là trung tâm của dự án này. Nó thuộc dòng mô hình Phi-3 và hỗ trợ độ dài ngữ cảnh lên đến 128.000 token. Mô hình được huấn luyện trên một tập dữ liệu đa dạng bao gồm dữ liệu tổng hợp và các trang web công khai được lọc kỹ lưỡng, tập trung vào nội dung chất lượng cao và đòi hỏi khả năng suy luận. Quá trình huấn luyện bao gồm tinh chỉnh có giám sát và tối ưu hóa ưu tiên trực tiếp để đảm bảo tuân thủ chính xác các hướng dẫn, cùng với các biện pháp an toàn vững chắc.

## Việc tạo dữ liệu mẫu rất quan trọng vì một số lý do sau:

1. **Kiểm thử**: Dữ liệu mẫu cho phép bạn kiểm thử ứng dụng trong nhiều tình huống khác nhau mà không ảnh hưởng đến dữ liệu thực. Điều này đặc biệt quan trọng trong giai đoạn phát triển và thử nghiệm.

2. **Tối ưu hiệu năng**: Với dữ liệu mẫu mô phỏng quy mô và độ phức tạp của dữ liệu thực, bạn có thể xác định các điểm nghẽn hiệu năng và tối ưu hóa ứng dụng phù hợp.

3. **Tạo nguyên mẫu**: Dữ liệu mẫu có thể được sử dụng để tạo nguyên mẫu và bản mô phỏng, giúp hiểu rõ yêu cầu người dùng và thu thập phản hồi.

4. **Phân tích dữ liệu**: Trong khoa học dữ liệu, dữ liệu mẫu thường được dùng để phân tích khám phá, huấn luyện mô hình và kiểm thử thuật toán.

5. **Bảo mật**: Sử dụng dữ liệu mẫu trong môi trường phát triển và kiểm thử giúp ngăn ngừa rò rỉ dữ liệu nhạy cảm từ dữ liệu thực.

6. **Học tập**: Nếu bạn đang học một công nghệ hoặc công cụ mới, làm việc với dữ liệu mẫu là cách thực tế để áp dụng kiến thức đã học.

Hãy nhớ rằng, chất lượng dữ liệu mẫu có thể ảnh hưởng lớn đến các hoạt động này. Dữ liệu nên càng gần với dữ liệu thực về cấu trúc và tính đa dạng càng tốt.

### Tạo Dữ Liệu Mẫu
[Generate DataSet Script](./CreatingSampleData.md)

## Tập Dữ Liệu

Một ví dụ tốt về tập dữ liệu mẫu là [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (có trên Huggingface).  
Tập dữ liệu mẫu về sản phẩm Burberry cùng với siêu dữ liệu về danh mục sản phẩm, giá cả và tiêu đề với tổng cộng 3.040 dòng, mỗi dòng đại diện cho một sản phẩm duy nhất. Tập dữ liệu này cho phép chúng ta kiểm thử khả năng của mô hình trong việc hiểu và diễn giải dữ liệu hình ảnh, tạo ra các mô tả văn bản chi tiết nắm bắt các đặc điểm hình ảnh tinh vi và đặc trưng riêng của thương hiệu.

**Note:** Bạn có thể sử dụng bất kỳ tập dữ liệu nào có bao gồm hình ảnh.

## Suy Luận Phức Tạp

Mô hình cần suy luận về giá cả và tên gọi chỉ dựa trên hình ảnh. Điều này đòi hỏi mô hình không chỉ nhận diện các đặc điểm hình ảnh mà còn hiểu được ý nghĩa của chúng về giá trị sản phẩm và thương hiệu. Bằng cách tổng hợp các mô tả văn bản chính xác từ hình ảnh, dự án làm nổi bật tiềm năng tích hợp dữ liệu hình ảnh để nâng cao hiệu suất và tính đa năng của mô hình trong các ứng dụng thực tế.

## Kiến Trúc Phi-3 Vision

Kiến trúc mô hình là phiên bản đa phương tiện của Phi-3. Nó xử lý cả dữ liệu văn bản và hình ảnh, tích hợp các đầu vào này thành một chuỗi thống nhất để thực hiện các nhiệm vụ hiểu và sinh tổng hợp. Mô hình sử dụng các lớp embedding riêng biệt cho văn bản và hình ảnh. Các token văn bản được chuyển đổi thành vector dày đặc, trong khi hình ảnh được xử lý qua mô hình CLIP vision để trích xuất embedding đặc trưng. Các embedding hình ảnh sau đó được chiếu để phù hợp với kích thước embedding văn bản, đảm bảo chúng có thể tích hợp liền mạch.

## Tích Hợp Embedding Văn Bản và Hình Ảnh

Các token đặc biệt trong chuỗi văn bản chỉ ra vị trí chèn embedding hình ảnh. Trong quá trình xử lý, các token đặc biệt này được thay thế bằng embedding hình ảnh tương ứng, cho phép mô hình xử lý văn bản và hình ảnh như một chuỗi duy nhất. Prompt cho tập dữ liệu của chúng ta được định dạng sử dụng token đặc biệt <|image|> như sau:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Mã Ví Dụ
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.