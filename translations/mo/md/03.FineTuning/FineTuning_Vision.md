<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-07T13:36:29+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "mo"
}
-->
# Phi-3.5-vision finetuning recipe

នេះគឺជាការគាំទ្រផ្លូវការសម្រាប់ការបង្រួមបង្រួម Phi-3.5-vision ដោយប្រើបណ្ណាល័យ huggingface។
សូម `cd` ទៅកាន់ថតកូដ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) មុនពេលដំណើរការបញ្ជា ខាងក្រោម។

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

យើងផ្ដល់ជូនស្គ្រីបបង្រួមបង្រួមពីរដែលជាឧទាហរណ៍ មួយសម្រាប់ DocVQA និងមួយសម្រាប់ចាត់ថ្នាក់ hateful meme។

ឧបករណ៍ធ្វើតេស្តអប្បបរមា 4x RTX8000 (48GB RAM ក្នុងមួយ GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ឥឡូវគាំទ្រពហុរូបភាពជាផ្លូវការហើយ។ នេះជាឧទាហរណ៍សម្រាប់បង្រួមបង្រួម NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

អាស្រ័យលើឧបករណ៍របស់អ្នក អ្នកប្រើអាចជ្រើសយុទ្ធសាស្ត្របង្រួមបង្រួមខុសគ្នា។ យើងគាំទ្រការបង្រួមបង្រួមពេញលេញ (ជាមួយ Deepspeed Zero-2) ដែលអាចជាប់ប្លុក vision parameters ឬមិនបានជាប់, និង LoRA (រួមមាន 4bit QLoRA)។
ជាទូទៅ យើងផ្ដល់អនុសាសន៍ឲ្យប្រើការបង្រួមបង្រួមពេញលេញជាមួយ flash attention និង bf16 នៅពេលអាចធ្វើបាន។

### ការណែនាំសម្រាប់បម្លែង dataset ផ្ទាល់ខ្លួនរបស់អ្នកទៅទ្រង់ទ្រាយត្រូវការ

យើងប្រើ dataset ចំណាត់ថ្នាក់វីដេអូអប្បបរមា (ជាផ្នែកតូចនៃ UCF-101) ជាឧទាហរណ៍ពីដើមដល់ចុង ដើម្បីបង្ហាញពីវិធីបម្លែង dataset ផ្ទាល់ខ្លួនរបស់អ្នកទៅទ្រង់ទ្រាយត្រូវការ និងបង្រួមបង្រួម Phi-3.5-vision លើវា។

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ទិន្នន័យបម្លែងនឹងមានរូបរាងដូចខាងក្រោម៖

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

សម្រាប់អនុសាសន៍ `jsonl` រៀងរាល់បន្ទាត់គួរតែជាភាសាដាក់បញ្ជីដូចជា:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

សូមចំណាំថា `conversations` គឺជាបញ្ជី មុនដូច្នេះអាចគាំទ្រការសន្ទនាច្រើនជំហាន ប្រសិនបើមានទិន្នន័យដូច្នេះ។

## Requesting Azure GPU Quota 

### Prerequisites

គណនី Azure ដែលមានតួនាទី Contributor (ឬតួនាទីផ្សេងទៀតដែលរួមបញ្ចូលការចូលដំណើរការជា Contributor)។

បើអ្នកមិនមានគណនី Azure សូមបង្កើត [គណនីឥតគិតថ្លៃមុនចាប់ផ្តើម](https://azure.microsoft.com)។

### Request a quota increase

អ្នកអាចដាក់សំណើសុំបន្ថែមគុណភាពដោយផ្ទាល់ពី My quotas។ អនុវត្តតាមជំហានខាងក្រោមដើម្បីស្នើសុំបន្ថែមគុណភាព។ សម្រាប់ឧទាហរណ៍នេះ អ្នកអាចជ្រើសគុណភាពដែលអាចកែប្រែបានណាមួយក្នុងការជាវរបស់អ្នក។

ចូលទៅកាន់ [Azure portal](https://portal.azure.com)។

វាយ "quotas" ក្នុងប្រអប់ស្វែងរក បន្ទាប់មកជ្រើស Quotas។
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

នៅលើទំព័រ Overview ជ្រើសអ្នកផ្គត់ផ្គង់មួយដូចជា Compute ឬ AML។

**Note** សម្រាប់អ្នកផ្គត់ផ្គង់ទាំងអស់ក្រៅពី Compute អ្នកនឹងឃើញជួរឈរមួយឈ្មោះ Request increase ជំនួសជួរឈរដែលអាចកែប្រែបានដែលបានពិពណ៌នាខាងក្រោម។ នៅទីនោះ អ្នកអាចស្នើសុំបន្ថែមសម្រាប់គុណភាពជាក់លាក់ ឬបង្កើតសំណើសុំគាំទ្រសម្រាប់ការបន្ថែម។

នៅលើទំព័រ My quotas ក្រោម Quota name ជ្រើសគុណភាពដែលអ្នកចង់បន្ថែម។ ប្រាកដថាជួរឈរដែលអាចកែប្រែបានបង្ហាញ Yes សម្រាប់គុណភាពនេះ។

នៅជិតផ្នែកខាងលើនៃទំព័រ ជ្រើស New Quota Request បន្ទាប់មកជ្រើស Enter a new limit។

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

នៅក្នុងផ្ទាំង New Quota Request វាយតម្លៃជាចំនួនសម្រាប់កំណត់គុណភាពថ្មីរបស់អ្នក បន្ទាប់មកជ្រើស Submit។

សំណើរបស់អ្នកនឹងត្រូវបានពិនិត្យ និងអ្នកនឹងទទួលបានការជូនដំណឹងបើសំណើអាចបំពេញបាន។ វាជាទូទៅកើតឡើងក្នុងរយៈពេលប៉ុន្មាននាទី។

បើសំណើរបស់អ្នកមិនត្រូវបានបំពេញ អ្នកនឹងឃើញតំណភ្ជាប់សម្រាប់បង្កើតសំណើសុំគាំទ្រ។ នៅពេលអ្នកប្រើតំណនេះ វិស្វករគាំទ្រនឹងជួយអ្នកក្នុងការស្នើសុំបន្ថែមនេះ។

## Azure Compute GPU machine SKU suggestions

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

នេះជាឧទាហរណ៍ខ្លះៗ៖

### ប្រសិនបើអ្នកមាន GPU A100 ឬ H100

ការបង្រួមបង្រួមពេញលេញជាទូទៅផ្តល់សមត្ថភាពល្អបំផុត។ អ្នកអាចប្រើបញ្ជា ខាងក្រោមដើម្បីបង្រួមបង្រួម Phi-3-V សម្រាប់ចាត់ថ្នាក់ hateful memes។

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### ប្រសិនបើអ្នកមាន Standard_ND40rs_v2 8x V100-32GB GPUs

វានៅតែអាចបង្រួមបង្រួមពេញលេញ Phi-3-V សម្រាប់ចាត់ថ្នាក់ hateful memes បាន។ ទោះជាយ៉ាងណា សូមរំពឹងថាមាន throughput ទាបជាងយ៉ាងខ្លាំង ប្រៀបធៀបនឹង GPU A100 ឬ H100 ដោយសារមិនគាំទ្រការប្រើ flash attention។ ការពិតប្រាកដក៏អាចមានផលប៉ះពាល់ផង ដោយសារមិនគាំទ្រប្រភេទ bf16 (ប្រើការបណ្តុះបណ្តាល fp16 mixed-precision ជំនួស)។

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### ប្រសិនបើអ្នកមិនអាចប្រើ GPU នៅ data center បាន

LoRA ប្រហែលជាជម្រើសតែមួយរបស់អ្នក។ អ្នកអាចប្រើបញ្ជា ខាងក្រោមដើម្បីបង្រួមបង្រួម Phi-3-V សម្រាប់ចាត់ថ្នាក់ hateful memes។

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

សម្រាប់ GPU Turing+ គាំទ្រ QLoRA

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
លទ្ធផល DocVQA និង Hateful memes ខាងក្រោមផ្អែកលើកំណែចាស់ (Phi-3-vision)។
លទ្ធផលថ្មីជាមួយ Phi-3.5-vision នឹងត្រូវបានធ្វើបច្ចុប្បន្នភាពឆាប់ៗនេះ។

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

លទ្ធផលប៉ាន់ប្រមាណល្បឿនថ្មីជាមួយ Phi-3.5-vision នឹងត្រូវបានធ្វើបច្ចុប្បន្នភាពឆាប់ៗនេះ។

ការប៉ាន់ប្រមាណល្បឿនត្រូវបានអនុវត្តលើ dataset DocVQA។ ប្រវែងជួរដំណើរការមធ្យមនៃ dataset នេះគឺ 2443.23 tokens (ប្រើ `num_crops=16` សម្រាប់ម៉ូដែលរូបភាព)។

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

- មិនអាចប្រើ flash attention ជាមួយ fp16 បាន (bf16 តែងតែត្រូវបានផ្ដល់អាទិភាពនៅពេលមាន, ហើយ GPU ទាំងអស់ដែលគាំទ្រការប្រើ flash attention ក៏គាំទ្រការប្រើ bf16 ផងដែរ)។
- មិនគាំទ្រការសន្សំ checkpoint មធ្យម និងបន្តបណ្តុះបណ្តាលនៅឡើយទេ។

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

Could you please clarify what language or code "mo" refers to? There are several possibilities (e.g., Moldovan, a constructed language, or something else). This will help me provide an accurate translation.