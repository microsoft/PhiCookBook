<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:01:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "th"
}
-->
# Phi-3.5-vision finetuning recipe

นี่คือการสนับสนุนอย่างเป็นทางการของ Phi-3.5-vision finetuning โดยใช้ไลบรารี huggingface  
โปรด `cd` ไปยังไดเรกทอรีโค้ด [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ก่อนรันคำสั่งด้านล่างนี้

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

เรามีสคริปต์ finetuning ตัวอย่างสองตัว หนึ่งสำหรับ DocVQA และอีกหนึ่งสำหรับการจำแนก hateful meme

ฮาร์ดแวร์ขั้นต่ำที่ทดสอบคือ 4x RTX8000 (48GB RAM ต่อ GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ตอนนี้รองรับการป้อนภาพหลายภาพอย่างเป็นทางการ นี่คือตัวอย่างสำหรับการ finetune NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

ขึ้นอยู่กับฮาร์ดแวร์ ผู้ใช้สามารถเลือกกลยุทธ์การ finetuning ที่แตกต่างกันได้ เรารองรับ  
full-finetuning (พร้อม Deepspeed Zero-2) โดยสามารถเลือกแช่แข็งพารามิเตอร์ vision ได้ และ LoRA (รวมถึง 4bit QLoRA)  
โดยทั่วไป เราแนะนำให้ใช้ full finetuning พร้อม flash attention และ bf16 เมื่อเป็นไปได้

### คู่มือการแปลงชุดข้อมูลของคุณให้เป็นฟอร์แมตรูปแบบที่ต้องการ

เราใช้ชุดข้อมูลวิดีโอจำแนกประเภทขั้นต่ำ (ซับเซ็ตของ UCF-101) เป็นตัวอย่างแบบครบวงจรเพื่อแสดงวิธีแปลงชุดข้อมูลของคุณให้เป็นฟอร์แมตที่ต้องการและ finetune Phi-3.5-vision บนชุดข้อมูลนั้น

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ข้อมูลที่แปลงแล้วจะมีลักษณะดังนี้:

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

สำหรับ annotation แบบ `jsonl` แต่ละบรรทัดควรเป็นดิกชันนารีในรูปแบบ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

โปรดทราบว่า `conversations` เป็นลิสต์ ดังนั้นจึงรองรับการสนทนาแบบหลายรอบหากมีข้อมูลประเภทนี้

## Requesting Azure GPU Quota 

### Prerequisites

บัญชี Azure ที่มีบทบาท Contributor (หรือบทบาทอื่นที่รวมสิทธิ์ Contributor)

ถ้าคุณยังไม่มีบัญชี Azure ให้สร้าง [บัญชีฟรีก่อนเริ่มต้น](https://azure.microsoft.com)

### Request a quota increase

คุณสามารถส่งคำขอเพิ่มโควต้าได้โดยตรงจาก My quotas ทำตามขั้นตอนด้านล่างเพื่อขอเพิ่มโควต้า สำหรับตัวอย่างนี้ คุณสามารถเลือกโควต้าที่ปรับได้ใดก็ได้ใน subscription ของคุณ

เข้าสู่ระบบที่ [Azure portal](https://portal.azure.com)

พิมพ์ "quotas" ในช่องค้นหา แล้วเลือก Quotas  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

ในหน้า Overview เลือกผู้ให้บริการ เช่น Compute หรือ AML

**Note** สำหรับผู้ให้บริการทุกตัวนอกจาก Compute คุณจะเห็นคอลัมน์ Request increase แทนคอลัมน์ Adjustable ที่อธิบายไว้ด้านล่าง ที่นั่นคุณสามารถขอเพิ่มโควต้าที่เฉพาะเจาะจง หรือสร้างคำขอสนับสนุนเพื่อขอเพิ่มโควต้า

ในหน้า My quotas ภายใต้ Quota name เลือกโควต้าที่คุณต้องการเพิ่ม ตรวจสอบให้แน่ใจว่าคอลัมน์ Adjustable แสดง Yes สำหรับโควต้านั้น

ใกล้ด้านบนของหน้า เลือก New Quota Request แล้วเลือก Enter a new limit

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

ในแผง New Quota Request ให้ป้อนค่าตัวเลขสำหรับขีดจำกัดโควต้าใหม่ของคุณ จากนั้นเลือก Submit

คำขอของคุณจะถูกตรวจสอบ และคุณจะได้รับแจ้งหากคำขอสามารถดำเนินการได้ โดยปกติจะใช้เวลาภายในไม่กี่นาที

ถ้าคำขอของคุณไม่สำเร็จ คุณจะเห็นลิงก์เพื่อสร้างคำขอสนับสนุน เมื่อใช้ลิงก์นี้ วิศวกรสนับสนุนจะช่วยคุณในการขอเพิ่มโควต้า

## Azure Compute GPU machine SKU suggestions

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ตัวอย่างเช่น:

### หากคุณมี GPU A100 หรือ H100

การ finetuning แบบเต็มมักให้ประสิทธิภาพดีที่สุด คุณสามารถใช้คำสั่งด้านล่างเพื่อ finetune Phi-3-V บนการจำแนก hateful memes

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### หากคุณมี Standard_ND40rs_v2 8x V100-32GB GPUs

ยังสามารถ finetune Phi-3-V แบบเต็มบนการจำแนก hateful memes ได้ แต่คาดว่าจะมีอัตราการประมวลผลต่ำกว่ามากเมื่อเทียบกับ A100 หรือ H100 เนื่องจากไม่มีการรองรับ flash attention  
ความแม่นยำอาจได้รับผลกระทบเนื่องจากไม่มีการรองรับ bf16 (ใช้การฝึกแบบ fp16 mixed-precision แทน)

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### หากคุณไม่มีสิทธิ์เข้าถึง GPU ใน data center

LoRA อาจเป็นตัวเลือกเดียวของคุณ คุณสามารถใช้คำสั่งด้านล่างเพื่อ finetune Phi-3-V บนการจำแนก hateful memes

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

สำหรับ Turing+ GPU รองรับ QLoRA

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

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### NOTE
ผลลัพธ์ DocVQA และ Hateful memes ด้านล่างนี้มาจากเวอร์ชันก่อนหน้า (Phi-3-vision)  
ผลลัพธ์ใหม่กับ Phi-3.5-vision จะอัปเดตในเร็วๆ นี้

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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Speed benchmarking (NOTE: Phi-3-vision)

ผลการทดสอบประสิทธิภาพใหม่กับ Phi-3.5-vision จะอัปเดตเร็วๆ นี้

การทดสอบประสิทธิภาพทำบนชุดข้อมูล DocVQA ความยาวเฉลี่ยของลำดับในชุดข้อมูลนี้คือ 2443.23 โทเค็น (ใช้ `num_crops=16` สำหรับโมเดลภาพ)

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Known issues

- ไม่สามารถรัน flash attention กับ fp16 ได้ (แนะนำให้ใช้ bf16 เสมอเมื่อมี และ GPU ที่รองรับ flash attention ทั้งหมดก็รองรับ bf16 ด้วย)
- ยังไม่รองรับการบันทึก checkpoint ระหว่างทางและการฝึกซ้ำ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้องสูงสุด โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยมืออาชีพที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้