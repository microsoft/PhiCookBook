<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:49:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "vi"
}
-->
# Tổng Quan Dự Án Phi-3-Vision-128K-Instruct

## Mô Hình

Phi-3-Vision-128K-Instruct, một mô hình đa phương tiện nhẹ và tiên tiến, là cốt lõi của dự án này. Nó thuộc dòng mô hình Phi-3 và hỗ trợ độ dài ngữ cảnh lên đến 128.000 token. Mô hình được huấn luyện trên bộ dữ liệu đa dạng bao gồm dữ liệu tổng hợp và các trang web công khai được lọc kỹ lưỡng, tập trung vào nội dung chất lượng cao, yêu cầu tư duy phức tạp. Quá trình huấn luyện bao gồm tinh chỉnh có giám sát và tối ưu hóa ưu tiên trực tiếp nhằm đảm bảo tuân thủ chính xác hướng dẫn, cùng với các biện pháp an toàn vững chắc.

## Việc tạo dữ liệu mẫu rất quan trọng vì nhiều lý do:

1. **Kiểm thử**: Dữ liệu mẫu giúp bạn kiểm thử ứng dụng trong nhiều tình huống khác nhau mà không ảnh hưởng đến dữ liệu thật. Điều này đặc biệt quan trọng trong giai đoạn phát triển và thử nghiệm.

2. **Tối ưu hiệu năng**: Với dữ liệu mẫu mô phỏng quy mô và độ phức tạp của dữ liệu thật, bạn có thể phát hiện các điểm nghẽn hiệu năng và tối ưu hóa ứng dụng cho phù hợp.

3. **Phát triển nguyên mẫu**: Dữ liệu mẫu có thể được sử dụng để tạo nguyên mẫu và bản mô phỏng, giúp hiểu rõ yêu cầu người dùng và thu thập phản hồi.

4. **Phân tích dữ liệu**: Trong khoa học dữ liệu, dữ liệu mẫu thường được dùng để phân tích khám phá, huấn luyện mô hình và thử nghiệm thuật toán.

5. **Bảo mật**: Sử dụng dữ liệu mẫu trong môi trường phát triển và kiểm thử giúp ngăn ngừa rò rỉ dữ liệu thật nhạy cảm.

6. **Học tập**: Nếu bạn đang học một công nghệ hay công cụ mới, làm việc với dữ liệu mẫu là cách thực tế để áp dụng kiến thức đã học.

Hãy nhớ rằng, chất lượng dữ liệu mẫu có thể ảnh hưởng lớn đến các hoạt động trên. Nó nên càng giống dữ liệu thật về cấu trúc và sự đa dạng càng tốt.

### Tạo Dữ Liệu Mẫu
[Generate DataSet Script](./CreatingSampleData.md)

## Bộ Dữ Liệu

Một ví dụ tốt về bộ dữ liệu mẫu là [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (có trên Huggingface).  
Bộ dữ liệu mẫu về sản phẩm Burberry cùng với metadata về loại sản phẩm, giá cả và tiêu đề, gồm tổng cộng 3.040 dòng, mỗi dòng đại diện cho một sản phẩm duy nhất. Bộ dữ liệu này giúp chúng ta kiểm thử khả năng của mô hình trong việc hiểu và diễn giải dữ liệu hình ảnh, tạo ra văn bản mô tả chi tiết những đặc điểm hình ảnh phức tạp và đặc trưng riêng của thương hiệu.

**Note:** Bạn có thể sử dụng bất kỳ bộ dữ liệu nào có hình ảnh.

## Tư Duy Phức Tạp

Mô hình cần suy luận về giá cả và tên gọi chỉ dựa trên hình ảnh. Điều này đòi hỏi mô hình không chỉ nhận diện các đặc điểm hình ảnh mà còn hiểu được ý nghĩa của chúng về giá trị sản phẩm và thương hiệu. Bằng cách tổng hợp các mô tả văn bản chính xác từ hình ảnh, dự án thể hiện tiềm năng tích hợp dữ liệu hình ảnh để nâng cao hiệu suất và tính đa năng của mô hình trong các ứng dụng thực tế.

## Kiến Trúc Phi-3 Vision

Kiến trúc mô hình là phiên bản đa phương tiện của Phi-3. Nó xử lý cả dữ liệu văn bản và hình ảnh, kết hợp các đầu vào này thành một chuỗi thống nhất để hiểu và sinh tạo toàn diện. Mô hình sử dụng các lớp nhúng riêng biệt cho văn bản và hình ảnh. Token văn bản được chuyển thành vector đặc, trong khi hình ảnh được xử lý qua mô hình CLIP vision để trích xuất các vector đặc trưng. Các vector nhúng hình ảnh sau đó được chiếu để phù hợp với kích thước vector nhúng văn bản, đảm bảo có thể tích hợp mượt mà.

## Tích Hợp Nhúng Văn Bản và Hình Ảnh

Các token đặc biệt trong chuỗi văn bản chỉ vị trí chèn nhúng hình ảnh. Trong quá trình xử lý, các token đặc biệt này được thay thế bằng các vector nhúng hình ảnh tương ứng, cho phép mô hình xử lý văn bản và hình ảnh như một chuỗi duy nhất. Lời nhắc cho bộ dữ liệu của chúng ta được định dạng sử dụng token đặc biệt <|image|> như sau:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Mẫu Mã Nguồn
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.