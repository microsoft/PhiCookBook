<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:46:12+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "vi"
}
-->
# Tinh chỉnh Phi3 bằng Olive

Trong ví dụ này, bạn sẽ sử dụng Olive để:

1. Tinh chỉnh một adapter LoRA để phân loại các cụm từ thành Buồn, Vui, Sợ, Ngạc nhiên.
1. Gộp trọng số adapter vào mô hình gốc.
1. Tối ưu và lượng tử hóa mô hình thành `int4`.

Chúng tôi cũng sẽ hướng dẫn bạn cách suy luận mô hình đã được tinh chỉnh bằng ONNX Runtime (ORT) Generate API.

> **⚠️ Để tinh chỉnh, bạn cần có GPU phù hợp – ví dụ như A10, V100, A100.**

## 💾 Cài đặt

Tạo một môi trường ảo Python mới (ví dụ, sử dụng `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Tiếp theo, cài đặt Olive và các phụ thuộc cho quy trình tinh chỉnh:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Tinh chỉnh Phi3 bằng Olive
[Tập tin cấu hình Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) chứa một *quy trình* với các *bước* sau:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Ở cấp độ tổng quan, quy trình này sẽ:

1. Tinh chỉnh Phi3 (trong 150 bước, bạn có thể thay đổi) sử dụng dữ liệu [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Gộp trọng số adapter LoRA vào mô hình gốc. Kết quả là bạn sẽ có một mô hình duy nhất ở định dạng ONNX.
1. Model Builder sẽ tối ưu mô hình cho ONNX runtime *và* lượng tử hóa mô hình thành `int4`.

Để chạy quy trình, thực thi:

```bash
olive run --config phrase-classification.json
```

Khi Olive hoàn thành, mô hình Phi3 đã được tinh chỉnh và tối ưu ở định dạng `int4` sẽ có tại: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Tích hợp Phi3 đã tinh chỉnh vào ứng dụng của bạn

Để chạy ứng dụng:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Phản hồi sẽ là một phân loại đơn giản cho cụm từ (Buồn/Vui/Sợ/Ngạc nhiên).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.