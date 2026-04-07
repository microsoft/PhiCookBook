# មេរៀនផ្គូត Phi-3.5-vision

នេះគឺជាការគាំទ្រផ្លូវការនៃការផ្គូត Phi-3.5-vision ដោយប្រើបណ្ណាល័យ huggingface។
សូម `cd` ទៅថតកូដ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) មុនពេលរត់ពាក្យបញ្ជាខាងក្រោម។

## ការដំឡើង

```bash
# បង្កើតបរិស្ថាន conda ថ្មី
conda create -n phi3v python=3.10
conda activate phi3v

# តម្លើង pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# បណ្ណាល័យផ្សេងទៀតដែលត្រូវការដើម្បីរត់កូដឧទាហរណ៍
pip install -r requirements.txt

# (ជាជម្រើស) flash attention -- កាតក្រាហ្វិក Ampere+ (ឧ. A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (ជាជម្រើស) QLoRA -- កាតក្រាហ្វិក Turing+ (ឧ. RTX 8000)
pip install bitsandbytes==0.43.1
```

## ចាប់ផ្តើមរហ័ស

យើងផ្តល់នូវស្គ្រីបផ្គូតពីរឧទាហរណ៍មួយ សម្រាប់ DocVQA និងមួយសម្រាប់ចាត់ថ្នាក់មីម៌ហិង្សា។

ឧបករណ៍អប្បបរមា ដែលបានសាកល្បងលើ 4x RTX8000 (ម៉emory RAM 48GB ក្នុងមួយ GPU)

```bash
# ស្គ្រីបតិចតួចសម្រាប់ការបំបែកបណ្តោយខ្សែរថភ្លើងតូចរបស់ DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ឥឡូវបានគាំទ្រពហុរូបភាព។ នេះជាឧទាហរណ៍សម្រាប់ផ្គូត NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## បញ្ជីណែនាំការប្រើប្រាស់

អាស្រ័យលើឧបករណ៍ ប្រើប្រាស់អាចជ្រើសយុទ្ធសាស្ត្រផ្គូតផ្សេងៗគ្នា។ យើងគាំទ្រការផ្គូតពេញលេញ (ជាមួយ Deepspeed Zero-2) នូវការតំណប្រាណរូបភាពដែលអាចត្រូវរួច និង LoRA (រួមទាំង QLoRA 4bit)។
ជាធម្មតា យើងណែនាំឲ្យប្រើការផ្គូតពេញលេញជាមួយ flash attention និង bf16 នៅពេលដែលអាចធ្វើបាន។

### តំណាងសម្រាប់បម្លែងខ្ទង់ទិន្នន័យផ្ទាល់ខ្លួនរបស់អ្នកទៅទ្រង់ទ្រាយដែលត្រូវការ

យើងប្រើឧទាហរណ៍ទិន្នន័យចាត់ថ្នាក់វីដេអូអប្បបរមា (ជាទម្រង់តូចមួយនៃ UCF-101) ដើម្បីបង្ហាញពីរបៀបបម្លែងទិន្នន័យផ្ទាល់ខ្លួនរបស់អ្នកទៅទ្រង់ទ្រាយត្រូវការ និងបង្វឹក Phi-3.5-vision លើវា។

```bash
# បម្លែងទិន្នន័យ
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# បណ្តុះបណ្តាល
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ទិន្នន័យបម្លែងនឹងមើលទៅដូចនេះ៖

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

សម្រាប់ការកំណត់ត្រា `jsonl` រៀបរាប់ជាស្រីតេអាក់មួយដូចជា៖

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

សូមចំណាំថា `conversations` គឺជាបញ្ជី មូលហេតុហេតុដែលការសន្ទនាពហុជំនាន់អាចត្រូវបានគាំទ្របើទិន្នន័យនោះមាន។

## សំណើសុំចំនួន Azure GPU

### លក្ខខណ្ឌជាមុន

គណនី Azure ដែលមានតួនាទី Contributor (ឬតួនាទីផ្សេងទៀតដែលរួមបញ្ចូលការចូលដំណើរការជា Contributor)។

បើអ្នកមិនមានគណនី Azure សូមបង្កើត [គណនីឥតគិតថ្លៃមុនចាប់ផ្តើម](https://azure.microsoft.com)។

### ស្នើរសុំបន្ថែមកំណត់ចំនួន

អ្នកអាចដាក់ស្នើរសុំបន្ថែមកំណត់ចំនួនដោយផ្ទាល់ពី My quotas។ អនុវត្តតាមជំហានខាងក្រោមដើម្បីស្នើរសុំបន្ថែមកំណត់ចំនួន។ សម្រាប់ឧទាហរណ៍នេះ អ្នកអាចជ្រើសរើសកំណត់ចំនួនណាមួយដែលអាចកែប្រែបានក្នុងការជាវរបស់អ្នក។

ចូលទៅកាន់ [Azure portal](https://portal.azure.com)។

វាយ "quotas" ទៅក្នុងប្រអប់ស្វែងរក ហើយជ្រើស Quotas។
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

នៅលើទំព័រ Overview ជ្រើសអ្នកផ្គត់ផ្គង់មួយ ដូចជា Compute ឬ AML។

**ចំណាំ** សម្រាប់អ្នកផ្គត់ផ្គង់ទាំងអស់ក្រៅពី Compute អ្នកនឹងឃើញកូឡំហ៏ Request increase ជំនួសកូឡំហ៏ Adjustable ដែលបានពិពណ៌នាខាងក្រោម។ នៅទីនោះ អ្នកអាចស្នើរពន្លឿនកំណត់ចំនួន ឬបង្កើតសំណើគាំទ្រសម្រាប់ការពន្លឿន។

នៅលើទំព័រ My quotas នៅក្រោម Quota name ជ្រើសកំណត់ចំនួនដែលអ្នកចង់បន្ថែម។ ត្រូវប្រាកដថាកូឡំហ៏ Adjustable បង្ហាញ Yes សម្រាប់កំណត់ចំនួននេះ។

នៅជិតខាងលើនៃទំព័រ ជ្រើស New Quota Request បន្ទាប់មកជ្រើស Enter a new limit។

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

នៅក្នុងផ្ទាំង New Quota Request បញ្ចូលតម្លៃ លេខសម្រាប់កំណត់ចំនួនកំណត់ថ្មី រួចជ្រើស Submit។

សំណើររបស់អ្នកនឹងត្រូវពិនិត្យ ហើយអ្នកនឹងបានជម្រាបអំពីការអាចបំពេញសំណើ។ ធម្មតានេះកើតឡើងនៅក្នុងរយៈពេលប៉ុន្មាននាទី។

បើសំណើររបស់អ្នកមិនត្រូវបានបំពេញ អ្នកនឹងឃើញតំណភ្ជាប់ដើម្បីបង្កើតសំណើគាំទ្រ។ នៅពេលអ្នកប្រើតំណនេះ វិស្វករគាំទ្រនឹងជួយអ្នកក្នុងសំណើបន្ថែម។

## ការផ្តល់អនុសាសន៍ម៉ាស៊ីន Azure Compute GPU SKU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

នេះជាឧទាហរណ៍ខ្លះៗ៖

### បើអ្នកមាន GPU A100 ឬ H100

ការផ្គូតពេញលេញភាគច្រើនផ្តល់នូវប្រសិទ្ធភាពល្អបំផុត។ អ្នកអាចប្រើពាក្យបញ្ជាខាងក្រោមក្នុងការផ្គូត Phi-3-V លើការចាត់ថ្នាក់មីម៌ហិង្សា។

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### បើអ្នកមាន Standard_ND40rs_v2 8x V100-32GB GPUs

វាពីរបីមែនដើម្បីផ្គូត Phi-3-V បានពេញលេញលើការចាត់ថ្នាក់មីម៌ហិង្សា។ ប៉ុន្តែ សូមរំពឹងថាការផលិតទាបជាងបរិមាណ A100 ឬ H100 GPU ពីព្រោះគ្មានការគាំទ្រចំពោះ flash attention។
ភាពច្បាស់អាចត្រូវរងគ្រោះដោយសារខ្វះការគាំទ្រ bf16 (មានការប្រើប្រាស់ការបណ្ដុះបណ្ដាល fp16 mixed-precision ទំនេរជំនួស)។

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### បើអ្នកមិនមានចូលដំណើរការទៅ GPU នៅមជ្ឈមណ្ឌលទិន្នន័យ

Lora អាចជាជម្រើសតែមួយរបស់អ្នក។ អ្នកអាចប្រើពាក្យបញ្ជាខាងក្រោមដើម្បីផ្គូត Phi-3-V លើការចាត់ថ្នាក់មីម៌ហិង្សា។

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

សម្រាប់ GPU Turing+ គាំទ្រការប្រើ QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ប៉ារ៉ាម៉ែត្រ និងភាពច្បាស់ដែលបានផ្ដល់អនុសាសន៍

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

វិធីសាស្រ្តបណ្តុះបណ្តាល | ម៉ូឌែលទស្សនាដែលបានរឹតបន្តឹង | ប្រភេទទិន្នន័យ | ជួរលំដាប់ LoRA | alpha LoRA | ទំហំបាឡូ | អត្រាសិក្សា | លំដាប់ | ភាពច្បាស់
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
លទ្ធផល LoRA បង្ហាញឆាប់ៗនេះ |  |  |  |  |  |  |  |  |

### សម្គាល់

លទ្ធផល DocVQA និង Hateful memes ខាងក្រោម គឺផ្អែកលើជំនាន់មុន (Phi-3-vision)។
លទ្ធផលថ្មីជាមួយ Phi-3.5-vision នឹងត្រូវបានបន្ថែមឆាប់ៗនេះ។

### DocVQA (សម្គាល់ៈ Phi-3-vision)

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

វិធីសាស្រ្តបណ្តុះបណ្តាល | ប្រភេទទិន្នន័យ | ជួរលំដាប់ LoRA | alpha LoRA | ទំហំបាឡូ | អត្រាសិក្សា | លំដាប់ | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
ម៉ូឌែលរូបភាពដែលបានរឹតបន្តឹង| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
ម៉ូឌែលរូបភាពដែលបានរឹតបន្តឹង| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (សម្គាល់ៈ Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

វិធីសាស្រ្តបណ្តុះបណ្តាល | ប្រភេទទិន្នន័យ | ជួរលំដាប់ LoRA | alpha LoRA | ទំហំបាឡូ | អត្រាសិក្សា | លំដាប់ | ភាពច្បាស់
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
ម៉ូឌែលរូបភាពដែលបានរឹតបន្តឹង| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
ម៉ូឌែលរូបភាពដែលបានរឹតបន្តឹង| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## សាកល្បងល្បឿន (សម្គាល់ៈ Phi-3-vision)

លទ្ធផលសាកល្បងថ្មីជាមួយ Phi-3.5-vision នឹងត្រូវបានបន្ថែមឆាប់ៗនេះ។

សាកល្បងល្បឿនត្រូវបានបង្វែកលើទិន្នន័យ DocVQA។ កម្ពស់ជួរចងខ្សែសម្រាប់ទិន្នន័យនេះ
គឺ 2443.23 token (ប្រើ `num_crops=16` សម្រាប់ម៉ូឌែលរូបភាព)។

### 8x A100-80GB (Ampere)

វិធីសាស្រ្តបណ្តុះបណ្តាល | \# គោល | GPU | flash attention | ទំហំបាឡូមានប្រសិទ្ធភាព | ល្បឿនចេញ (រូប/វិនាទី) | ល្បឿនបន្ថែម | ចំណាស់ម៉ោន GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
ម៉ូឌែលរូបភាពរឹតបន្តឹង | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
ម៉ូឌែលរូបភាពរឹតបន្តឹង | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

វិធីសាស្រ្តបណ្តុះបណ្តាល | \# គោល | GPU | flash attention | ទំហំបាឡូមានប្រសិទ្ធភាព | ល្បឿនចេញ (រូប/វិនាទី) | ល្បឿនបន្ថែម | ចំណាស់ម៉ោន GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
ម៉ូឌែលរូបភាពរឹតបន្តឹង | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## បញ្ហាបានដឹង

- មិនអាចរត់ flash attention ជាមួយ fp16 បានទេ (bf16 តែងតែបានណែនាំនៅពេលមាន អ្នកគាំទ្រទាំងអស់ដែលគាំទ្រដល់ flash attention ក៏គាំទ្រ bf16 ផងដែរ)។
- មិនគាំទ្រការរក្សាទុក checkpoint មធ្យម និងបន្តបណ្តុះបណ្តាលទេ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការជៀសវាងការទទួលខុសត្រូវ**៖  
ឯកសារនេះត្រូវបានបំបែកបកប្រែដោយប្រើសេវាបកប្រែក្នុងប្រព័ន្ធ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំរក្សារជាក់លាក់ក៏ដោយ សូមយល់ថាការបកប្រែដោយយន្តអាចមានកំហុសឬមិនត្រឹមត្រូវបាន។ ឯកសារដើមនៅក្នុងភាសាជាដើមគួរត្រូវបានចាត់ទុកជាក្បួនដ៏ពិតប្រាកដ។ សម្រាប់ព័ត៌មានដែលមានសារសំខាន់ មនុស្សដោយជំនាញបកប្រែមានការផ្ដល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបំភ្លេចណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->