<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:05:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "tl"
}
-->
# Phi-3.5-vision finetuning recipe

Ito ang opisyal na suporta para sa Phi-3.5-vision finetuning gamit ang huggingface libraries.  
Pakigamit ang `cd` papunta sa code directory na [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) bago patakbuhin ang mga sumusunod na utos.

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

Nagbibigay kami ng dalawang halimbawa ng finetuning scripts, isa para sa DocVQA at isa para sa hateful meme classification.

Minimal hardware na nasubukan ay 4x RTX8000 (48GB RAM bawat GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Opisyal nang sinusuportahan ng Phi-3.5-vision ang multi-image inputs. Narito ang halimbawa para sa finetuning ng NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

Depende sa hardware, maaaring pumili ang mga user ng iba't ibang finetuning strategies. Sinusuportahan namin ang full-finetuning (gamit ang Deepspeed Zero-2) na may opsyonal na frozen vision parameters, at LoRA (kasama ang 4bit QLoRA).  
Sa pangkalahatan, inirerekomenda naming gamitin ang full finetuning na may flash attention at bf16 kung maaari.

### Gabay sa pag-convert ng iyong custom dataset sa kinakailangang format

Gumagamit kami ng minimum video classification dataset (isang subset ng UCF-101) bilang end-to-end na halimbawa para ipakita kung paano i-convert ang iyong custom dataset sa kinakailangang format at i-finetune ang Phi-3.5-vision dito.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Ganito ang magiging hitsura ng na-convert na data:

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

Para sa `jsonl` na annotation, bawat linya ay dapat isang dictionary na ganito:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Tandaan na ang `conversations` ay isang listahan, kaya sinusuportahan ang multi-turn conversation kung mayroon ng ganoong data.

## Requesting Azure GPU Quota 

### Mga Kinakailangan

Isang Azure account na may Contributor role (o ibang role na may Contributor access).

Kung wala ka pang Azure account, gumawa ng [free account bago ka magsimula](https://azure.microsoft.com).

### Pagsusumite ng kahilingan para sa quota increase

Maaari kang magsumite ng kahilingan para sa pagtaas ng quota direkta mula sa My quotas. Sundin ang mga hakbang sa ibaba para humiling ng pagtaas ng quota. Sa halimbawang ito, maaari kang pumili ng anumang adjustable quota sa iyong subscription.

Mag-sign in sa [Azure portal](https://portal.azure.com).

I-type ang "quotas" sa search box, pagkatapos piliin ang Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Sa Overview page, piliin ang isang provider, tulad ng Compute o AML.

**Note** Para sa lahat ng providers maliban sa Compute, makikita mo ang Request increase column sa halip na Adjustable column na nakalarawan sa ibaba. Dito, maaari kang humiling ng pagtaas para sa isang partikular na quota, o gumawa ng support request para sa pagtaas.

Sa My quotas page, sa ilalim ng Quota name, piliin ang quota na nais mong taasan. Siguraduhing nakalagay ang Yes sa Adjustable column para sa quota na ito.

Malapit sa itaas ng pahina, piliin ang New Quota Request, pagkatapos piliin ang Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Sa New Quota Request pane, ilagay ang numerikal na halaga para sa iyong bagong quota limit, pagkatapos piliin ang Submit.

Susuriin ang iyong kahilingan, at ipapaalam sa iyo kung maaari itong matugunan. Karaniwan itong nangyayari sa loob ng ilang minuto.

Kung hindi matutugunan ang iyong kahilingan, makikita mo ang link para gumawa ng support request. Kapag ginamit mo ang link na ito, tutulungan ka ng support engineer sa iyong kahilingan para sa pagtaas.

## Azure Compute GPU machine SKU suggestions

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Narito ang ilang mga halimbawa:

### Kung may A100 o H100 GPUs ka

Kadalasang nagbibigay ng pinakamahusay na performance ang full finetuning. Maaari mong gamitin ang sumusunod na utos para i-finetune ang Phi-3-V sa hateful memes classification.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Kung may Standard_ND40rs_v2 8x V100-32GB GPUs ka

Posible pa rin na i-full finetune ang Phi-3-V sa hateful memes classification. Ngunit asahan ang mas mababang throughput kumpara sa A100 o H100 GPUs dahil sa kawalan ng flash attention support.  
Maaaring maapektuhan din ang accuracy dahil hindi sinusuportahan ang bf16 (gumagamit na lang ng fp16 mixed-precision training).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Kung wala kang access sa data center GPUs  
Maaaring LoRA lang ang iyong pagpipilian. Maaari mong gamitin ang sumusunod na utos para i-finetune ang Phi-3-V sa hateful memes classification.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Para sa Turing+ GPU, sinusuportahan ang QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Mga inirerekomendang hyperparameters at inaasahang accuracy  
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
Ang mga sumusunod na resulta para sa DocVQA at Hateful memes ay base sa naunang bersyon (Phi-3-vision).  
Ang mga bagong resulta gamit ang Phi-3.5-vision ay ia-update sa lalong madaling panahon.

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

Ang mga bagong benchmarking results gamit ang Phi-3.5-vision ay ia-update sa lalong madaling panahon.

Isinagawa ang speed benchmarking sa DocVQA dataset. Ang average sequence length ng dataset na ito ay 2443.23 tokens (gamit ang `num_crops=16` para sa image model).

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

- Hindi pwedeng patakbuhin ang flash attention gamit ang fp16 (palaging inirerekomenda ang bf16 kapag available, at lahat ng GPUs na sumusuporta sa flash attention ay sumusuporta rin sa bf16).  
- Hindi pa sinusuportahan ang pag-save ng intermediate checkpoints at pag-resume ng training.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.