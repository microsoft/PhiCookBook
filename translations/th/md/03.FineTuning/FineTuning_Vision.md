<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:46:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "th"
}
-->
# Phi-3.5-vision สูตรการปรับแต่งแบบละเอียด

นี่คือการสนับสนุนอย่างเป็นทางการสำหรับการปรับแต่งแบบละเอียด Phi-3.5-vision โดยใช้ไลบรารี huggingface  
โปรด `cd` ไปยังไดเรกทอรีโค้ด [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ก่อนรันคำสั่งด้านล่าง

## การติดตั้ง

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

## เริ่มต้นอย่างรวดเร็ว

เรามีสคริปต์ตัวอย่างสำหรับการปรับแต่งแบบละเอียดสองตัวอย่าง ตัวหนึ่งสำหรับ DocVQA และอีกตัวสำหรับการจำแนก hateful meme

ฮาร์ดแวร์ขั้นต่ำที่ทดสอบคือ 4x RTX8000 (48GB RAM ต่อ GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ตอนนี้รองรับการป้อนข้อมูลภาพหลายภาพอย่างเป็นทางการ นี่คือตัวอย่างสำหรับการปรับแต่ง NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## คู่มือการใช้งาน

ขึ้นอยู่กับฮาร์ดแวร์ ผู้ใช้สามารถเลือกกลยุทธ์การปรับแต่งแบบละเอียดที่แตกต่างกันได้ เรารองรับ  
full-finetuning (ด้วย Deepspeed Zero-2) โดยสามารถเลือกแช่แข็งพารามิเตอร์ของ vision ได้ และ LoRA (รวมถึง 4bit QLoRA)  
โดยทั่วไป เราแนะนำให้ใช้ full finetuning พร้อม flash attention และ bf16 เมื่อเป็นไปได้

### คู่มือการแปลงชุดข้อมูลของคุณให้อยู่ในรูปแบบที่ต้องการ

เราใช้ชุดข้อมูลวิดีโอจำแนกประเภทขั้นต่ำ (เป็นส่วนย่อยของ UCF-101) เป็นตัวอย่างแบบครบวงจรเพื่อแสดงวิธีแปลงชุดข้อมูลของคุณให้อยู่ในรูปแบบที่ต้องการและปรับแต่ง Phi-3.5-vision บนชุดข้อมูลนั้น

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

สำหรับการอธิบาย `jsonl` แต่ละบรรทัดควรเป็นพจนานุกรมแบบนี้:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

โปรดทราบว่า `conversations` เป็นรายการ ดังนั้นจึงรองรับการสนทนาแบบหลายรอบได้หากมีข้อมูลดังกล่าว

## การขอเพิ่มโควต้า Azure GPU

### ข้อกำหนดเบื้องต้น

บัญชี Azure ที่มีบทบาท Contributor (หรือบทบาทอื่นที่รวมการเข้าถึง Contributor)

หากคุณยังไม่มีบัญชี Azure ให้สร้าง [บัญชีฟรีก่อนเริ่มต้น](https://azure.microsoft.com)

### การขอเพิ่มโควต้า

คุณสามารถส่งคำขอเพิ่มโควต้าได้โดยตรงจาก My quotas ทำตามขั้นตอนด้านล่างเพื่อขอเพิ่มโควต้า สำหรับตัวอย่างนี้ คุณสามารถเลือกโควต้าที่ปรับได้ใดก็ได้ใน subscription ของคุณ

เข้าสู่ระบบที่ [Azure portal](https://portal.azure.com)

พิมพ์ "quotas" ในช่องค้นหา แล้วเลือก Quotas  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

ในหน้า Overview เลือกผู้ให้บริการ เช่น Compute หรือ AML

**Note** สำหรับผู้ให้บริการอื่นนอกจาก Compute คุณจะเห็นคอลัมน์ Request increase แทนคอลัมน์ Adjustable ที่อธิบายไว้ด้านล่าง ที่นั่นคุณสามารถขอเพิ่มโควต้าที่เฉพาะเจาะจง หรือสร้างคำขอสนับสนุนเพื่อขอเพิ่มโควต้าได้

ในหน้า My quotas ภายใต้ Quota name เลือกโควต้าที่คุณต้องการเพิ่ม ตรวจสอบให้แน่ใจว่าคอลัมน์ Adjustable แสดง Yes สำหรับโควต้าตัวนี้

ใกล้ด้านบนของหน้า เลือก New Quota Request แล้วเลือก Enter a new limit

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

ในแผง New Quota Request ป้อนค่าตัวเลขสำหรับขีดจำกัดโควต้าที่ต้องการ จากนั้นเลือก Submit

คำขอของคุณจะถูกตรวจสอบ และคุณจะได้รับแจ้งหากคำขอสามารถดำเนินการได้ โดยปกติจะใช้เวลาไม่กี่นาที

หากคำขอของคุณไม่สำเร็จ คุณจะเห็นลิงก์สำหรับสร้างคำขอสนับสนุน เมื่อใช้ลิงก์นี้ วิศวกรสนับสนุนจะช่วยเหลือคุณในการขอเพิ่มโควต้า

## คำแนะนำ SKU เครื่อง Azure Compute GPU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ตัวอย่างบางส่วน:

### หากคุณมี GPU A100 หรือ H100

การปรับแต่งแบบละเอียดเต็มรูปแบบมักให้ประสิทธิภาพดีที่สุด คุณสามารถใช้คำสั่งด้านล่างเพื่อปรับแต่ง Phi-3-V สำหรับการจำแนก hateful memes

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

ยังสามารถปรับแต่งแบบละเอียดเต็มรูปแบบ Phi-3-V สำหรับการจำแนก hateful memes ได้ แต่คาดว่าจะมีอัตราการประมวลผลต่ำกว่ามากเมื่อเทียบกับ GPU A100 หรือ H100 เนื่องจากไม่มีการรองรับ flash attention  
ความแม่นยำอาจได้รับผลกระทบเนื่องจากไม่มีการรองรับ bf16 (ใช้การฝึกแบบผสม fp16 แทน)

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### หากคุณไม่มีการเข้าถึง GPU ในศูนย์ข้อมูล

LoRA อาจเป็นทางเลือกเดียวของคุณ คุณสามารถใช้คำสั่งด้านล่างเพื่อปรับแต่ง Phi-3-V สำหรับการจำแนก hateful memes

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

สำหรับ GPU รุ่น Turing+ รองรับ QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ค่าพารามิเตอร์แนะนำและความแม่นยำที่คาดหวัง

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

วิธีการฝึก | แช่แข็งโมเดล vision | ชนิดข้อมูล | LoRA rank | LoRA alpha | ขนาดแบตช์ | อัตราการเรียนรู้ | จำนวนรอบ | ความแม่นยำ  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20  
ผลลัพธ์ LoRA กำลังจะมา |  |  |  |  |  |  |  |  

### NOTE  
ผลลัพธ์ DocVQA และ Hateful memes ด้านล่างนี้มาจากเวอร์ชันก่อนหน้า (Phi-3-vision)  
ผลลัพธ์ใหม่กับ Phi-3.5-vision จะอัปเดตเร็วๆ นี้

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

วิธีการฝึก | ชนิดข้อมูล | LoRA rank | LoRA alpha | ขนาดแบตช์ | อัตราการเรียนรู้ | จำนวนรอบ | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60  
frozen image model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19  
frozen image model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  

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

วิธีการฝึก | ชนิดข้อมูล | LoRA rank | LoRA alpha | ขนาดแบตช์ | อัตราการเรียนรู้ | จำนวนรอบ | ความแม่นยำ  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4  
frozen image model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4  
frozen image model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8  

## การทดสอบความเร็ว (NOTE: Phi-3-vision)

ผลการทดสอบใหม่กับ Phi-3.5-vision จะอัปเดตเร็วๆ นี้

การทดสอบความเร็วทำบนชุดข้อมูล DocVQA ความยาวลำดับเฉลี่ยของชุดข้อมูลนี้คือ 2443.23 โทเค็น (ใช้ `num_crops=16` สำหรับโมเดลภาพ)

### 8x A100-80GB (Ampere)

วิธีการฝึก | \# โหนด | GPUs | flash attention | ขนาดแบตช์ที่มีประสิทธิภาพ | อัตราการประมวลผล (ภาพ/วินาที) | ความเร็วเพิ่มขึ้น | หน่วยความจำ GPU สูงสุด (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
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

วิธีการฝึก | \# โหนด | GPUs | flash attention | ขนาดแบตช์ที่มีประสิทธิภาพ | อัตราการประมวลผล (ภาพ/วินาที) | ความเร็วเพิ่มขึ้น | หน่วยความจำ GPU สูงสุด (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## ปัญหาที่ทราบ

- ไม่สามารถใช้ flash attention กับ fp16 ได้ (แนะนำให้ใช้ bf16 เสมอเมื่อมี และ GPU ที่รองรับ flash attention ทั้งหมดก็รองรับ bf16 ด้วย)  
- ยังไม่รองรับการบันทึก checkpoint ระหว่างกลางและการฝึกซ้ำจากจุดหยุดพัก

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้