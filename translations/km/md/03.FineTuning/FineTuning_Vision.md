# រូបមន្តបង្ហាត់បន្ត Phi-3.5-vision

នេះគឺជាការគាំទ្រផ្លូវការសម្រាប់ការបង្ហាត់បន្ត Phi-3.5-vision ដោយប្រើបណ្ណាល័យ huggingface។  
សូម `cd` ទៅកាន់ថតកូដ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) មុនពេលដំណើរការកំហុសបន្ទាប់។

## ការដំឡើង

```bash
# បង្កើតបរិយាកាស conda ថ្មី
conda create -n phi3v python=3.10
conda activate phi3v

# តំឡើង pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# បណ្ណាល័យផ្សេងទៀតដែលត្រូវការដើម្បីដំណើរកូដឧទាហរណ៍
pip install -r requirements.txt

# (ជាជម្រើស) flash attention -- កាតចល័ត Ampere+ (ឧ. A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (ជាជម្រើស) QLoRA -- កាតចល័ត Turing+ (ឧ. RTX 8000)
pip install bitsandbytes==0.43.1
```

## ការចាប់ផ្តើមរហ័ស

យើងផ្តល់ឱ្យមានស្គ្រីបបង្ហាត់បន្តពីរគំរូមួយសម្រាប់ DocVQA និងមួយសម្រាប់ការជម្រাহীមេមដែលកំពុងភ័យខ្លាំង។

ឧបករណ៍អតិភាពបានតេស្តលើ 4x RTX8000 (48GB RAM ក្នុងមួយ GPU)

```bash
# ស្រោបស្ដើងលើការបំបែកលើការបណ្តុះបណ្តាលតូចរបស់ DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ឥឡូវនេះគាំទ្របញ្ចូលរូបភាពច្រើន។ ខាងក្រោមនេះជាគំរូបង្ហាត់បន្ត NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## មគ្គុទេសក៍ប្រើប្រាស់

អាស្រ័យលើយន្តហោះខ្នាតដូចម្តេច អ្នកប្រើប្រាស់អាចជ្រើសរើសយុទ្ធសាស្ត្របង្ហាត់បន្តផ្សេងៗគ្នា។ យើងគាំទ្រ  
ការបង្ហាត់បន្តពេញ (ជាមួយ Deepspeed Zero-2) ដែលអាចត្រៀមខ្លួនមើលទស្សនវិស័យបាន និង LoRA (រួមទាំង QLoRA 4bit)។  
ជាទូទៅ យើងផ្តល់អនុសាសន៍ឱ្យប្រើការបង្ហាត់បន្តពេញជាមួយ flash attention និង bf16 នៅពេលអាចធ្វើបាន។

### មគ្គុទេសក៍សម្រាប់បម្លែងទិន្នន័យផ្ទាល់ខ្លួនរបស់អ្នកទៅទ្រង់ទ្រាយដែលត្រូវការ

យើងប្រើឧទាហរណ៍ទិន្នន័យចាត់ថ្នាក់វីដេអូអប្បបរមា (ជាផ្នែកមួយនៃ UCF-101) ដើម្បីបង្ហាញពីរបៀបដែលអ្នកអាចបម្លែងទិន្នន័យផ្ទាល់ខ្លួនរបស់អ្នកទៅទ្រង់ទ្រាយត្រូវការ ហើយបង្ហាត់បន្ត Phi-3.5-vision លើវា។

```bash
# បម្លែងទិន្នន័យ
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# ការបណ្តុះបណ្តាល
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ទិន្នន័យបម្លែងនឹងមានរូបរាងដូចនេះ៖

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

សម្រាប់ការកំណត់ `jsonl` តួអក្សរនៅមួយជួរនីមួយៗគួរតែជាដិកស្នារីដូចតទៅ៖

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

សូមចំណាំថា `conversations` គឺជាបញ្ជី ដូច្នេះការសន្ទនាច្រើនជំរើសអាចគាំទ្របាន ប្រសិនបើមានទិន្នន័យបែបនេះ។

## សំណើរបង្កើនកម្រិត Azure GPU Quota

### លក្ខខណ្ឌតម្រូវការ

គណនី Azure ដែលមានតួនាទីជាអ្នករួមចំណែក (Contributor) (ឬតួនាទីផ្សេងទៀតដែលមានសិទ្ធិរួមចំណែក)។

ប្រសិនបើអ្នកមិនមានគណនី Azure សូមបង្កើត [គណនីឥតគិតថ្លៃមុនចាប់ផ្តើម](https://azure.microsoft.com)។

### សំណើរបង្កើនកម្រិត Quota

អ្នកអាចដាក់សំណើបង្កើនកម្រិត quota ដោយផ្ទាល់ពី My quotas។ សូមអនុវត្តន៍ជំហានខាងក្រោមដើម្បីស្នើសុំបង្កើន quota។ សម្រាប់ឧទាហរណ៍នេះ អ្នកអាចជ្រើសរើស quota គ្រប់យ៉ាងដែលអាចកែប្រែបានក្នុងការជាវរបស់អ្នក។

ចូលទៅគេហទំព័រ [Azure portal](https://portal.azure.com)។

វាយពាក្យ "quotas" ក្នុងប្រអប់ស្វែងរក បន្ទាប់មកជ្រើសរើស Quotas។  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

នៅលើទំព័រ Overview ជ្រើសរើសអ្នកផ្គត់ផ្គង់មួយដូចជា Compute ឬ AML។

**ចំណាំ** សម្រាប់អ្នកផ្គត់ផ្គង់ទាំងអស់ក្រៅពី Compute អ្នកនឹងឃើញជួរឈរជា Request increase ជំនួសពីជួរឈរ Adjustable ដែលពិពណ៌នាខាងក្រោម។ នៅទីនោះ អ្នកអាចស្នើសុំបង្កើន quota ពិសេស ឬបង្កើតសំណើសុំការគាំទ្រដើម្បីបង្កើន។

នៅលើទំព័រ My quotas នៅក្រោម Quota name ជ្រើសរើស quota ដែលអ្នកចង់បង្កើន។ សូមប្រាកដថាជួរឈរ Adjustable បង្ហាញ YES សម្រាប់ quota នេះ។

នៅចំពូលទំព័រ ជ្រើសរើស New Quota Request បន្ទាប់មកជ្រើសរើស Enter a new limit។

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

នៅក្នុងផ្ទាំង New Quota Request វាយតម្លៃជាលេខសម្រាប់ដែនកំណត់ quota ថ្មី រួចជ្រើស Submit។

សំណើររបស់អ្នកនឹងត្រូវបានពិនិត្យ ហើយអ្នកនឹងទទួលបានការជូនដំណឹងបើសំណើអាចទទួលបានការសម្រេច។ ធម្មតានេះនឹងកើតឡើងក្នុងរយៈពេលពីរបីនាទី។

បើសំណើរបស់អ្នកមិនបានទទួលសម្រេច អ្នកនឹងឃើញតំណភ្លើងសម្រាប់បង្កើតសំណើសុំការគាំទ្រ។ នៅពេលអ្នកប្រើតំណភ្លើងនេះ ជួយដំណោះស្រាយពីវិស្វករគាំទ្រនឹងជួយអ្នកនូវសំណើបង្កើននេះ។

## ការផ្តល់អនុសាសន៍ម៉ាសុីន GPU សម្រាប់ Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ខាងក្រោមជាឧទាហរណ៍ខ្លះៗ៖

### ប្រសិនបើអ្នកមាន GPU A100 ឬ H100

ការបង្ហាត់បន្តពេញជារឿយៗផ្តល់ផលល្អបំផុត។ អ្នកអាចប្រើពាក្យបញ្ជាតូចនេះ ដើម្បីបង្ហាត់បន្ត Phi-3-V លើការជម្រាះមេមដែលកំពុងភ័យខ្លាំង។

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

ការបង្ហាត់បន្តពេញនៅតែអាចធ្វើបានលើ Phi-3-V សម្រាប់ការជម្រាះមេមដែលកំពុងភ័យខ្លាំង។ ទោះជាយ៉ាងណា សូមរំពឹងថាតាចល័តនឹងទាបជាង GPU A100 ឬ H100 ដោយសារមិនមានការគាំទ្រចំពោះ flash attention។  
ភាពត្រឹមត្រូវក៏អាចមានផលប៉ះពាល់ដោយសារមិនគាំទ្រដល់ bf16 (ការបង្រៀនចំលែកលំនឹង fp16 ត្រូវបានប្រើជំនួស)។

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### ប្រសិនបើអ្នកមិនមានការចូលប្រើ GPU នៅមជ្ឈមណ្ឌលទិន្នន័យ

Lora អាចជជ្រើសរើសតែមួយនៃអ្នក។ អ្នកអាចប្រើពាក្យបញ្ជាតូចខាងក្រោមហើយបង្ហាត់បន្ត Phi-3-V លើការជម្រាះមេមដែលកំពុងភ័យខ្លាំង។

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

សម្រាប់ GPU Turing+ មានការគាំទ្រ QLoRA។

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ភាពល្អប៉ុន្មានដែលបានផ្ដល់អោយ និងភាពត្រឹមត្រូវដែលរំពឹងទុក

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

របៀបបង្ហាត់ | ម៉ូដែលទស្សនាវិស័យត្រូវបានត្រៀម | ប្រភេទទិន្នន័យ | ជួរលំដាប់ LoRA | អាល់ហ្វា LoRA | ទំហំកញ្ចប់ | អត្រាសិក្សា | ចំនួនសប្តាហ៍ | ភាពត្រឹមត្រូវ
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### ចំណាំ

លទ្ធផល DocVQA និង Hateful memes ខាងក្រោមនេះផ្អែកលើកំណែកុនមុន (Phi-3-vision)។  
លទ្ធផលថ្មីជាមួយ Phi-3.5-vision នឹងត្រូវបានធ្វើបច្ចុប្បន្នភាពឆាប់ៗនេះ។

### DocVQA (ចំណាំ៖ Phi-3-vision)

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

របៀបបង្ហាត់ | ប្រភេទទិន្នន័យ | ជួរលំដាប់ LoRA | អាល់ហ្វា LoRA | ទំហំកញ្ចប់ | អត្រាសិក្សា | ចំនួនសប្តាហ៍ | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (ចំណាំ៖ Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

របៀបបង្ហាត់ | ប្រភេទទិន្នន័យ | ជួរលំដាប់ LoRA | អាល់ហ្វា LoRA | ទំហំកញ្ចប់ | អត្រាសិក្សា | ចំនួនសប្តាហ៍ | ភាពត្រឹមត្រូវ
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## ការបង្រៀនល្បឿនស្ទង់មតិ (ចំណាំ៖ Phi-3-vision)

លទ្ធផលស្ទង់មតិបច្ចុប្បន្នជាមួយ Phi-3.5-vision នឹងត្រូវបានធ្វើបច្ចុប្បន្នភាពឆាប់ៗនេះ។

ការបង្រៀនល្បឿនបានអនុវត្តលើទិន្នន័យ DocVQA។ ប្រវែងជួររបស់សេរីនៅលើទិន្នន័យនេះ  
គឺ 2443.23 ដំណាក់កាល (tokens) (ដោយប្រើ `num_crops=16` សម្រាប់ម៉ូដែលរូបភាព)។

### 8x A100-80GB (Ampere)

របៀបបង្ហាត់ | \# nodes | GPUs | flash attention | ទំហំបញ្ចូលមានប្រសិទ្ធភាព | Throughput (រូប/វិនាទី) | ល្បឿន បូក | ទំហំម៉ាស៊ីន GPU លើកកំពូល (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frozen image model | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

របៀបបង្ហាត់ | \# nodes | GPUs | flash attention | ទំហំបញ្ចូលមានប្រសិទ្ធភាព | Throughput (រូប/វិនាទី) | ល្បឿន បូក | ទំហំម៉ាស៊ីន GPU លើកកំពូល (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## បញ្ហាដែលបានស្គាល់

- មិនអាចដំណើរការ flash attention ជាមួយ fp16 បានទេ (bf16 ត្រូវបានណែនាំរហៈនៅពេលអាចធ្វើបាន ហើយ GPU ទាំងអស់ដែលគាំទ្រប Flash attention ស៊ីធីទាំងគាំទ្រ bf16 ផងដែរ)។  
- មិនគាំទ្រការសន្សំពិន្ទុចន្លោះ និងការបន្តបង្ហាត់នៅឡើយទេ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំព្យាយាមរកភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមដែលមានភាសាជាតិនឹងត្រូវបានពិចារណาว่า​ជា​ប្រភព​តំណាង​ផ្ទាល់ខ្លួន។ សម្រាប់ព័ត៌មានសំខាន់​ គួរតែប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->