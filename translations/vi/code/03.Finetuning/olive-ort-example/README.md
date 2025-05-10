<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:33:11+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "vi"
}
-->
# Tinh chỉnh Phi3 bằng Olive

Trong ví dụ này, bạn sẽ sử dụng Olive để:

1. Tinh chỉnh bộ điều hợp LoRA để phân loại các cụm từ thành Buồn, Vui, Sợ, Ngạc nhiên.
1. Hợp nhất trọng số bộ điều hợp vào mô hình gốc.
1. Tối ưu hóa và lượng tử hóa mô hình thành `int4`.

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
[File cấu hình Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) chứa một *workflow* với các *bước* sau:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Ở mức độ tổng quát, workflow này sẽ:

1. Tinh chỉnh Phi3 (trong 150 bước, bạn có thể thay đổi) sử dụng dữ liệu [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Hợp nhất trọng số bộ điều hợp LoRA vào mô hình gốc. Điều này sẽ tạo ra một artifact mô hình duy nhất ở định dạng ONNX.
1. Model Builder sẽ tối ưu hóa mô hình cho ONNX runtime *và* lượng tử hóa mô hình thành `int4`.

Để chạy workflow, sử dụng lệnh:

```bash
olive run --config phrase-classification.json
```

Khi Olive hoàn thành, mô hình Phi3 đã tinh chỉnh và tối ưu hóa ở định dạng `int4` sẽ có tại: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Tích hợp Phi3 đã tinh chỉnh vào ứng dụng của bạn

Để chạy ứng dụng:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Phản hồi sẽ là một phân loại đơn giản của cụm từ (Buồn/Vui/Sợ/Ngạc nhiên).

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.