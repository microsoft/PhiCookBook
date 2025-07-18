<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:04:47+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "vi"
}
-->
# Tinh chỉnh Phi3 bằng Olive

Trong ví dụ này, bạn sẽ sử dụng Olive để:

1. Tinh chỉnh một bộ điều chỉnh LoRA để phân loại các cụm từ thành Buồn, Vui, Sợ, Ngạc nhiên.
1. Hợp nhất trọng số bộ điều chỉnh vào mô hình gốc.
1. Tối ưu và lượng tử hóa mô hình thành `int4`.

Chúng tôi cũng sẽ hướng dẫn bạn cách suy luận mô hình đã tinh chỉnh bằng ONNX Runtime (ORT) Generate API.

> **⚠️ Để tinh chỉnh, bạn cần có GPU phù hợp - ví dụ như A10, V100, A100.**

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
[File cấu hình Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) chứa một *quy trình làm việc* với các *bước* sau:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Ở cấp độ tổng quát, quy trình này sẽ:

1. Tinh chỉnh Phi3 (trong 150 bước, bạn có thể thay đổi) sử dụng dữ liệu từ [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Hợp nhất trọng số bộ điều chỉnh LoRA vào mô hình gốc. Kết quả là bạn sẽ có một mô hình duy nhất ở định dạng ONNX.
1. Model Builder sẽ tối ưu mô hình cho ONNX runtime *và* lượng tử hóa mô hình thành `int4`.

Để chạy quy trình, thực hiện:

```bash
olive run --config phrase-classification.json
```

Khi Olive hoàn thành, mô hình Phi3 đã tinh chỉnh và tối ưu `int4` sẽ có tại: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Tích hợp Phi3 đã tinh chỉnh vào ứng dụng của bạn

Để chạy ứng dụng:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Phản hồi sẽ là một từ duy nhất phân loại cụm từ (Buồn/Vui/Sợ/Ngạc nhiên).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.