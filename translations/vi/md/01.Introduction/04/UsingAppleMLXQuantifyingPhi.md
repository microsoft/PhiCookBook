<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:56:10+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "vi"
}
-->
# **Lượng tử hóa Phi-3.5 sử dụng Apple MLX Framework**

MLX là một framework mảng dành cho nghiên cứu máy học trên Apple silicon, được phát triển bởi nhóm nghiên cứu máy học của Apple.

MLX được thiết kế bởi các nhà nghiên cứu máy học dành cho các nhà nghiên cứu máy học. Framework này hướng tới sự thân thiện với người dùng, đồng thời vẫn đảm bảo hiệu quả trong việc huấn luyện và triển khai mô hình. Thiết kế của framework cũng rất đơn giản về mặt khái niệm. Chúng tôi mong muốn giúp các nhà nghiên cứu dễ dàng mở rộng và cải tiến MLX nhằm nhanh chóng khám phá các ý tưởng mới.

Các mô hình ngôn ngữ lớn (LLMs) có thể được tăng tốc trên các thiết bị Apple Silicon thông qua MLX, và các mô hình có thể chạy cục bộ một cách rất tiện lợi.

Hiện tại Apple MLX Framework hỗ trợ chuyển đổi lượng tử cho Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), và Phi-3.5-MoE (**Apple MLX Framework support**). Hãy cùng thử ngay sau đây:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Mẫu cho Phi-3.5 với Apple MLX**

| Labs    | Giới thiệu | Đi đến |
| -------- | ------- |  ------- |
| 🚀 Lab-Giới thiệu Phi-3.5 Instruct  | Tìm hiểu cách sử dụng Phi-3.5 Instruct với framework Apple MLX   |  [Đi đến](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Giới thiệu Phi-3.5 Vision (hình ảnh) | Tìm hiểu cách sử dụng Phi-3.5 Vision để phân tích hình ảnh với framework Apple MLX     |  [Đi đến](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Giới thiệu Phi-3.5 Vision (moE)   | Tìm hiểu cách sử dụng Phi-3.5 MoE với framework Apple MLX  |  [Đi đến](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Tài nguyên**

1. Tìm hiểu về Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.