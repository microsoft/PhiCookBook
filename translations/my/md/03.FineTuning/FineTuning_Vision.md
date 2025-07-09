<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-09T19:01:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "my"
}
-->
# Phi-3.5-vision finetuning recipe

ဤသည်မှာ huggingface libraries များကို အသုံးပြု၍ Phi-3.5-vision ကို finetuning ပြုလုပ်ရာတွင် တရားဝင်ထောက်ခံမှုဖြစ်ပါသည်။
အောက်ပါ command များကို run မပြုလုပ်မီ `cd` ဖြင့် code directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) သို့ ဝင်ရောက်ပါ။

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

DocVQA အတွက်နှင့် hateful meme classification အတွက် finetuning script နှစ်ခုကို ဥပမာအနေနှင့် ပံ့ပိုးပေးထားပါသည်။

အနည်းဆုံး hardware အနေဖြင့် 4x RTX8000 (GPU တစ်ခုလျှင် 48GB RAM) တွင် စမ်းသပ်ပြီးဖြစ်သည်။

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision သည် ယခု multi-image inputs ကို တရားဝင်ထောက်ခံပါသည်။ NLVR2 အတွက် finetuning ဥပမာကို အောက်တွင် ဖော်ပြထားပါသည်။

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

Hardware အလိုက် အသုံးပြုသူများသည် finetuning နည်းလမ်းများကို မတူညီစွာ ရွေးချယ်နိုင်ပါသည်။ ကျွန်ုပ်တို့သည်
full-finetuning (Deepspeed Zero-2 ဖြင့်) ကို vision parameters များကို အလိုအလျောက် freeze လုပ်နိုင်စွမ်းဖြင့်၊ နှင့် LoRA (4bit QLoRA အပါအဝင်) ကို ပံ့ပိုးပါသည်။
ယေဘုယျအားဖြင့် flash attention နှင့် bf16 ကို အသုံးပြု၍ full finetuning ပြုလုပ်ရန် အကြံပြုပါသည်။

### သင့် custom dataset ကို လိုအပ်သည့် format သို့ ပြောင်းလဲရန် လမ်းညွှန်ချက်

UCF-101 ၏ အပိုင်းအစဖြစ်သော အနည်းဆုံး video classification dataset ကို အသုံးပြု၍ သင့် custom dataset ကို လိုအပ်သည့် format သို့ ပြောင်းလဲခြင်းနှင့် Phi-3.5-vision ကို finetune ပြုလုပ်ခြင်းကို အဆုံးအဖြတ် ဥပမာအနေနှင့် ပြသထားပါသည်။

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ပြောင်းလဲပြီးသော data သည် အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မည်။

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

`jsonl` annotation အတွက်၊ တစ်ကြောင်းစီသည် dictionary အဖြစ် ရေးသားရမည်။

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations` သည် list ဖြစ်သောကြောင့် multi-turn conversation များကို ထောက်ပံ့နိုင်ပါသည်၊ ထိုကဲ့သို့သော data ရှိပါကသာဖြစ်သည်။

## Azure GPU Quota တောင်းဆိုခြင်း

### မတိုင်မီ လိုအပ်ချက်များ

Contributor role (သို့) Contributor access ပါဝင်သော အခြား role တစ်ခုပါဝင်သော Azure account တစ်ခု။

Azure account မရှိပါက [စတင်ရန် အခမဲ့အကောင့် ဖန်တီးပါ](https://azure.microsoft.com)။

### Quota တိုးမြှင့်ရန် တောင်းဆိုခြင်း

My quotas မှ တိုက်ရိုက် quota တိုးမြှင့်ရန် တောင်းဆိုနိုင်ပါသည်။ Quota တိုးမြှင့်ရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။ ဤဥပမာတွင် သင့် subscription တွင် adjustable ဖြစ်သော quota မည်သည့်အရာကိုမဆို ရွေးချယ်နိုင်ပါသည်။

[Azure portal](https://portal.azure.com) တွင် ဝင်ရောက်ပါ။

ရှာဖွေရန်ဘောက်စ်တွင် "quotas" ဟု ရိုက်ထည့်ပြီး Quotas ကို ရွေးချယ်ပါ။
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview စာမျက်နှာတွင် Compute သို့မဟုတ် AML ကဲ့သို့သော provider တစ်ခုကို ရွေးချယ်ပါ။

**Note** Compute အပြင် အခြား provider များအတွက် Request increase ကော်လံကို Adjustable ကော်လံအစား မြင်ရမည်ဖြစ်ပြီး၊ ထိုနေရာတွင် သတ်မှတ်ထားသော quota တစ်ခုအတွက် တိုးမြှင့်ရန် တောင်းဆိုနိုင်သည်၊ သို့မဟုတ် တိုးမြှင့်မှုအတွက် support request တစ်ခု ဖန်တီးနိုင်ပါသည်။

My quotas စာမျက်နှာတွင် Quota name အောက်မှ တိုးမြှင့်လိုသော quota ကို ရွေးချယ်ပါ။ ဤ quota အတွက် Adjustable ကော်လံတွင် Yes ဟု ပြထားရမည်။

စာမျက်နှာအပေါ်ဆုံးတွင် New Quota Request ကို နှိပ်ပြီး Enter a new limit ကို ရွေးချယ်ပါ။

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ပန်းနားတွင် သင့် quota limit အသစ်အတွက် ကိန်းဂဏန်းတန်ဖိုးကို ထည့်သွင်းပြီး Submit ကို နှိပ်ပါ။

သင့်တောင်းဆိုမှုကို ပြန်လည်သုံးသပ်ပြီး ပြည့်မှီနိုင်ပါက သတင်းပို့မည်ဖြစ်သည်။ ယေဘုယျအားဖြင့် မိနစ်အနည်းငယ်အတွင်း ဖြစ်ပေါ်ပါသည်။

တောင်းဆိုမှု မပြည့်မှီပါက support request ဖန်တီးရန် လင့်ခ်ကို မြင်ရမည်ဖြစ်ပြီး၊ ထိုလင့်ခ်ကို အသုံးပြုပါက support engineer တစ်ဦးက သင့်တိုးမြှင့်မှု တောင်းဆိုမှုကို ကူညီပေးပါမည်။

## Azure Compute GPU machine SKU အကြံပြုချက်များ

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

အောက်တွင် ဥပမာအချို့ကို ဖော်ပြထားပါသည်။

### A100 သို့မဟုတ် H100 GPU များရှိပါက

Full finetuning သည် ပုံမှန်အားဖြင့် အကောင်းဆုံး စွမ်းဆောင်ရည် ပေးနိုင်ပါသည်။ hateful memes classification အတွက် Phi-3-V ကို finetune ပြုလုပ်ရန် အောက်ပါ command ကို အသုံးပြုနိုင်ပါသည်။

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPU များရှိပါက

Phi-3-V ကို hateful memes classification အတွက် အပြည့်အဝ finetune ပြုလုပ်နိုင်သေးပါသည်။ သို့သော် flash attention ကို မထောက်ပံ့သောကြောင့် A100 သို့မဟုတ် H100 GPU များနှင့် နှိုင်းယှဉ်လျှင် throughput သာမက အရည်အသွေးလည်း နည်းပါးနိုင်သည်။ bf16 ကို မထောက်ပံ့သောကြောင့် (fp16 mixed-precision training ကို အသုံးပြုသည်) တိကျမှုလည်း သက်ရောက်နိုင်ပါသည်။

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Data center GPU မရရှိပါက

LoRA သာ သင့်ရွေးချယ်စရာ ဖြစ်နိုင်ပါသည်။ hateful memes classification အတွက် Phi-3-V ကို finetune ပြုလုပ်ရန် အောက်ပါ command ကို အသုံးပြုနိုင်ပါသည်။

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU များအတွက် QLoRA ကို ထောက်ပံ့ပါသည်။

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## အကြံပြု hyperparameters များနှင့် မျှော်မှန်းထားသော တိကျမှု

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
အောက်ပါ DocVQA နှင့် Hateful memes ရလဒ်များမှာ ယခင်ဗားရှင်း (Phi-3-vision) အပေါ် မူတည်ပါသည်။
Phi-3.5-vision ဖြင့် ရရှိမည့် ရလဒ်အသစ်များကို မကြာမီ အပ်ဒိတ် ပြုလုပ်သွားမည်ဖြစ်သည်။

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

Phi-3.5-vision ဖြင့် အသစ်ထွက်ရှိမည့် benchmarking ရလဒ်များကို မကြာမီ အပ်ဒိတ် ပြုလုပ်သွားမည်ဖြစ်သည်။

Speed benchmarking ကို DocVQA dataset ပေါ်တွင် ပြုလုပ်ထားသည်။ ဤ dataset ၏ ပျမ်းမျှ sequence length သည် 2443.23 tokens ဖြစ်ပြီး (image model အတွက် `num_crops=16` ကို အသုံးပြုသည်)။

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

## သိရှိထားသော ပြဿနာများ

- fp16 ဖြင့် flash attention ကို မရနိုင်ပါ (bf16 ကို ရနိုင်ပါက အမြဲတမ်း အကြံပြုပါသည်၊ flash attention ကို ထောက်ပံ့သော GPU များအားလုံးသည် bf16 ကိုလည်း ထောက်ပံ့ပါသည်)။
- အလယ်အလတ် checkpoint များကို သိမ်းဆည်းခြင်းနှင့် training ကို ပြန်စတင်ခြင်းကို မထောက်ပံ့သေးပါ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။