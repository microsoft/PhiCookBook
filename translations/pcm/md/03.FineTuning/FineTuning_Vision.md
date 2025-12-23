<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-12-21T17:07:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "pcm"
}
-->
# Phi-3.5-vision finetuning recipe

This na di official support for Phi-3.5-vision finetuning using huggingface libraries.
Abeg `cd` to di code directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) before you run di commands wey dey below.

## Installation

```bash
# make new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# oda libraries wey you need make di example code run
pip install -r requirements.txt

# (optional) flash attention -- Ampere GPUs and above (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing GPUs and above (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Quick start

We provide two example finetuning scripts, one for DocVQA and one for hateful meme classification.

Minimal hardware wey we don test on: 4x RTX8000 (48GB RAM per GPU)

```bash
# small script wey dey run for one mini-train split for DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision don officially support multi-image inputs. Na example for finetuning NLVR2 dey below

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

Depending on di hardware, users fit choose different finetuning strategies. We support
full-finetuning (with Deepspeed Zero-2) with option to freeze vision parameters, and LoRA (including 4bit QLoRA).
For general use, we recommend make you use full finetuning with flash attention and bf16 anytime wey e possible.

### guide for converting your custom dataset to the required format

We go use small video classification dataset (subset of UCF-101) as end-to-end example to show how to convert your custom dataset to di required format and fine-tune Phi-3.5-vision on top.

```bash
# convert di data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# trainin
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Di converted data go look like this:

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

For di `jsonl` annotation, every line suppose be one dictionary like:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Note say `conversations` na list, so multi-turn conversation fit dey supported if such data dey available.

## Requesting Azure GPU Quota 

### Prerequisites

You need Azure account wey get di Contributor role (or any other role wey include Contributor access).

If you never get Azure account, create a [free account before you begin](https://azure.microsoft.com).

### Request a quota increase

You fit submit request for quota increase straight from My quotas. Follow di steps wey dey below to request increase for quota. For dis example, you fit select any adjustable quota for your subscription.

Sign in to the [Azure portal](https://portal.azure.com).

Enter "quotas" for di search box, then select Quotas.
![Kwuota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

For di Overview page, select provider like Compute or AML.

**Note** For all providers wey no be Compute, you go see Request increase column instead of di Adjustable column wey dem describe below. For there, you fit request increase for particular quota, or create support request for di increase.

For di My quotas page, under Quota name, select di quota wey you wan increase. Make sure say di Adjustable column show Yes for dis quota.

Near di top of di page, select New Quota Request, then select Enter a new limit.

![Increase Kwuota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

For di New Quota Request pane, enter numerical value for your new quota limit, then select Submit.

Dem go review your request, and dem go notify you if dem fit fulfill am. Normally dis one dey happen within small minutes.

If dem no fulfill your request, you go see link to create support request. If you use dat link, support engineer go assist you with your increase request.

## Azure Compute GPU machine SKU suggestions

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Here na some examples:

### If you get A100 or H100 GPUs

Full finetuning normally dey give di best performance. You fit use di following command to finetune Phi-3-V on hateful memes classification.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### If you get Standard_ND40rs_v2 8x V100-32GB GPUs

E still possible to fully finetune Phi-3-V on hateful memes classification. But, expect
much lower throughput compared to A100 or H100 GPUs because dem no support flash attention.
Accuracy fit still dey affected because dem no get bf16 support (we go use fp16 mixed-precision training instead).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### If you no get access to data center GPUs
LoRA fit be your only choice. You fit use di following command to finetune Phi-3-V on hateful memes classification.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

For Turing+ GPU, QLoRA dey supported

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
full-finetuning | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### NOTE
Di DocVQA and Hateful memes results wey dey below base on di previous version (Phi-3-vision).
Di new results with Phi-3.5-vision go dey updated soon.

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

New benchmarking results with Phi-3.5-vision go dey updated soon.

Speed benchmarking dem do am on di DocVQA dataset. Di average sequence length for dis dataset na 2443.23 tokens (we use `num_crops=16` for di image model).

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
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

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Known issues

- You no fit run flash attention with fp16 (bf16 always recommended when e dey available, and all GPUs wey support flash attention also support bf16).
- We no yet support saving intermediate checkpoints and resuming training.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Make you sabi:
Dis document na AI translation service Co-op Translator (https://github.com/Azure/co-op-translator) don translate. Even though we dey try make am correct, make you sabi say automatic translations fit get mistakes or wrong parts. Di original document for e original language suppose be di main authoritative source. If na important mata, better make professional human translator do di translation. We no go responsible for any misunderstanding or wrong interpretation wey fit come from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->