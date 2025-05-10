<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:04:30+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "vi"
}
-->
# Phi-3.5-vision finetuning recipe

Đây là hỗ trợ chính thức cho việc finetuning Phi-3.5-vision sử dụng thư viện huggingface.  
Vui lòng `cd` đến thư mục code [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) trước khi chạy các lệnh dưới đây.

## Installation

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Quick start

Chúng tôi cung cấp hai script finetuning mẫu, một cho DocVQA và một cho phân loại hateful meme.

Phần cứng tối thiểu đã thử nghiệm trên 4x RTX8000 (48GB RAM mỗi GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision hiện chính thức hỗ trợ đầu vào nhiều hình ảnh. Dưới đây là ví dụ finetuning NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

Tùy thuộc vào phần cứng, người dùng có thể chọn các chiến lược finetuning khác nhau. Chúng tôi hỗ trợ  
full-finetuning (với Deepspeed Zero-2) với tùy chọn đóng băng các tham số vision, và LoRA (bao gồm cả 4bit QLoRA).  
Nói chung, chúng tôi khuyên dùng full finetuning với flash attention và bf16 khi có thể.

### Hướng dẫn chuyển đổi dataset tùy chỉnh sang định dạng yêu cầu

Chúng tôi dùng một dataset phân loại video tối giản (một phần của UCF-101) làm ví dụ từ đầu đến cuối để minh họa cách chuyển dataset tùy chỉnh sang định dạng yêu cầu và finetune Phi-3.5-vision trên đó.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Dữ liệu đã chuyển đổi sẽ trông như sau:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

Với annotation `jsonl`, mỗi dòng nên là một dictionary như sau:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Lưu ý rằng `conversations` là một danh sách, do đó có thể hỗ trợ hội thoại nhiều lượt nếu dữ liệu như vậy có sẵn.

## Requesting Azure GPU Quota 

### Prerequisites

Một tài khoản Azure với vai trò Contributor (hoặc vai trò khác có quyền Contributor).

Nếu bạn chưa có tài khoản Azure, hãy tạo [tài khoản miễn phí trước khi bắt đầu](https://azure.microsoft.com).

### Request a quota increase

Bạn có thể gửi yêu cầu tăng quota trực tiếp từ My quotas. Làm theo các bước dưới đây để yêu cầu tăng quota. Ví dụ này bạn có thể chọn bất kỳ quota có thể điều chỉnh trong subscription của mình.

Đăng nhập vào [Azure portal](https://portal.azure.com).

Nhập "quotas" vào ô tìm kiếm, sau đó chọn Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Ở trang Overview, chọn một nhà cung cấp, ví dụ Compute hoặc AML.

**Note** Với tất cả nhà cung cấp ngoài Compute, bạn sẽ thấy cột Request increase thay vì cột Adjustable như mô tả bên dưới. Tại đây, bạn có thể yêu cầu tăng quota cụ thể hoặc tạo yêu cầu hỗ trợ cho việc tăng.

Ở trang My quotas, dưới Quota name, chọn quota bạn muốn tăng. Đảm bảo cột Adjustable hiển thị Yes cho quota đó.

Gần đầu trang, chọn New Quota Request, sau đó chọn Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Trong bảng New Quota Request, nhập giá trị số cho giới hạn quota mới, sau đó chọn Submit.

Yêu cầu của bạn sẽ được xem xét và bạn sẽ nhận được thông báo nếu yêu cầu được chấp thuận. Thường quá trình này diễn ra trong vài phút.

Nếu yêu cầu không được chấp thuận, bạn sẽ thấy liên kết để tạo yêu cầu hỗ trợ. Khi sử dụng liên kết này, kỹ sư hỗ trợ sẽ giúp bạn với yêu cầu tăng quota.

## Azure Compute GPU machine SKU suggestions

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Dưới đây là một số ví dụ:

### Nếu bạn có GPU A100 hoặc H100

Full finetuning thường cho hiệu suất tốt nhất. Bạn có thể dùng lệnh sau để finetune Phi-3-V trên phân loại hateful memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Nếu bạn có Standard_ND40rs_v2 8x V100-32GB GPUs

Bạn vẫn có thể full finetune Phi-3-V trên phân loại hateful memes. Tuy nhiên, hãy chuẩn bị  
hiệu suất thấp hơn nhiều so với GPU A100 hoặc H100 do không hỗ trợ flash attention.  
Độ chính xác cũng có thể bị ảnh hưởng do không hỗ trợ bf16 (thay vào đó dùng fp16 mixed-precision training).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Nếu bạn không có quyền truy cập GPU trong data center

LoRA có thể là lựa chọn duy nhất của bạn. Bạn có thể dùng lệnh sau để finetune Phi-3-V trên phân loại hateful memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Với GPU Turing+ thì QLoRA được hỗ trợ

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Suggested hyperparameters and expected accuracy

### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Phương pháp huấn luyện | Đóng băng mô hình vision | loại dữ liệu | LoRA rank | LoRA alpha | kích thước batch | learning rate | epochs | Độ chính xác  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Kết quả LoRA sẽ sớm được cập nhật |  |  |  |  |  |  |  |  |

### NOTE  
Kết quả DocVQA và Hateful memes bên dưới dựa trên phiên bản trước (Phi-3-vision).  
Kết quả mới với Phi-3.5-vision sẽ được cập nhật sớm.

### DocVQA (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Phương pháp huấn luyện | loại dữ liệu | LoRA rank | LoRA alpha | kích thước batch | learning rate | epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
Đóng băng mô hình ảnh| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
Đóng băng mô hình ảnh| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Phương pháp huấn luyện | loại dữ liệu | LoRA rank | LoRA alpha | kích thước batch | learning rate | epochs | Độ chính xác  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
Đóng băng mô hình ảnh| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
Đóng băng mô hình ảnh| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Speed benchmarking (NOTE: Phi-3-vision)

Kết quả benchmark mới với Phi-3.5-vision sẽ được cập nhật sớm.

Benchmark tốc độ được thực hiện trên dataset DocVQA. Độ dài chuỗi trung bình của dataset này là 2443.23 tokens (sử dụng `num_crops=16` cho mô hình ảnh).

### 8x A100-80GB (Ampere)

Phương pháp huấn luyện | \# nodes | GPUs | flash attention | Kích thước batch hiệu quả | Throughput (img/s) | Tăng tốc | Bộ nhớ GPU đỉnh (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
Đóng băng mô hình ảnh | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
Đóng băng mô hình ảnh | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Phương pháp huấn luyện | \# nodes | GPUs | flash attention | Kích thước batch hiệu quả | Throughput (img/s) | Tăng tốc | Bộ nhớ GPU đỉnh (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
Đóng băng mô hình ảnh | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Known issues

- Không thể chạy flash attention với fp16 (luôn khuyến nghị dùng bf16 khi có, và tất cả GPU hỗ trợ flash attention cũng hỗ trợ bf16).  
- Hiện chưa hỗ trợ lưu checkpoint trung gian và tiếp tục huấn luyện.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.