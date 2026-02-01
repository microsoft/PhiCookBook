# Phi-3.5-vision ഫൈൻട്യൂണിംഗ് റെസിപ്പി

This is the official support of Phi-3.5-vision finetuning using huggingface libraries.
Please `cd` to the code directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) before running the following commands.

## ഇൻസ്റ്റലേഷൻ

```bash
# പുതിയ conda പരിസ്ഥിതി സൃഷ്ടിക്കുക
conda create -n phi3v python=3.10
conda activate phi3v

# pytorch ഇൻസ്റ്റാൾ ചെയ്യുക
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# ഉദാഹരണ കോഡ് ഓടിക്കാൻ ആവശ്യമായ മറ്റ് ലൈബ്രറികൾ
pip install -r requirements.txt

# (ഐച്ഛികം) ഫ്ലാഷ് അറ്റൻഷൻ -- Ampere+ GPUകൾ (ഉദാഹരണത്തിന്, A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (ഐച്ഛികം) QLoRA -- Turing+ GPUകൾ (ഉദാഹരണത്തിന്, RTX 8000)
pip install bitsandbytes==0.43.1
```

## ക്വിക്ക് സ്റ്റാർട്ട്

നാം രണ്ട് ഉദാഹരണ ഫൈൻട്യൂണിംഗ് സ്ക്രിപ്റ്റുകൾ നൽകുന്നു, ഒന്ന് DocVQA-ക്കുള്ളതും മറ്റൊന്ന് hateful meme വർഗ്ഗീകരണത്തിനുള്ളതും.

കുറഞ്ഞതിലധികം ഹാർഡ്‌വെയർ പരിശോധിച്ചത് 4x RTX8000 (GPUപ്രതി 48GB RAM) ആണ്

```bash
# DocVQA-യുടെ മിനി-ട്രെയിൻ സ്പ്ലിറ്റിൽ ഒരു മിനിമൽ സ്ക്രിപ്റ്റ്
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ഇപ്പോൾ ഔദ്യോഗികമായി മൾട്ടി-ഇമേജ് ഇൻപുട്ടുകൾ പിന്തുണയ്ക്കുന്നു. NLVR2 ഫൈൻട്യൂണിംഗിന് ഒരു ഉദാഹരണം ഇവിടെ കാണാം

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ഉപയോഗ മാർഗ്ഗനിർദ്ദേശം

ഹാർഡ്‌വെയറിനനുസരിച്ച്, ഉപയോക്താക്കൾ വ്യത്യസ്ത ഫൈൻട്യൂണിംഗ് തന്ത്രങ്ങൾ തിരഞ്ഞെടുക്കാം. ഞങ്ങൾ പിന്തുണയ്ക്കുന്നത്
ഫുൾ-ഫൈൻട്യൂണിംഗ് (Deepspeed Zero-2 ഉപയോഗിച്ച്) ഓപ്‌ഷനായി വിസൻ പാർാമീറ്ററുകൾ ഫ്രീസ് ചെയ്ത നിലയിൽ, കൂടാതെ LoRA (4bit QLoRA ഉൾപ്പെടെ) ആണ്.
സാധ്യമായിടത്തോളം, flash attention និង bf16 ഉപയോഗിച്ച് ഫുൾ ഫൈൻട്യൂണിംഗ് ഉപയോഗിക്കാൻ ഞങ്ങൾ ശിപാർശ ചെയ്യുന്നു.

### നിങ്ങളുടെ കസ്റ്റം ഡാറ്റാസെറ്റ് ആവശ്യമായ ഫോർമാറ്റിലേക്ക് മാറ്റാനുള്ള ഗൈഡ്

നാം ഒരു കുറഞ്ഞ വീഡിയോ വർഗ്ഗീകരണ ഡാറ്റാസെറ്റ് (UCF-101-ന്റെ ഒരു സബ്സെറ്റ്) end-to-end ഉദാഹരണമായി ഉപയോഗിച്ച് നിങ്ങളുടെ കസ്റ്റം ഡാറ്റാസെറ്റ് ആവശ്യമായ ഫോർമാറ്റിലേക്ക് എങ്ങനെ പരിവർത്തനം ചെയ്യാമെന്നും Phi-3.5-vision-ൽ അത് എങ്ങനെ ഫൈൻട്യൂൺ ചെയ്യാമെന്നും കാണിക്കുന്നു.

```bash
# ഡാറ്റ പരിവർത്തനം ചെയ്യുക
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# പരിശീലനം
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

പരിവർത്തിപ്പിച്ച ഡാറ്റ ഇങ്ങനെ കാണപ്പെടും:

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

`jsonl` അനോട്ടേഷനിനായി, ഓരോ വരിയും ഇത്തരത്തിലുള്ള ഒരു dictionary ആയിരിക്കണം:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ശ്രദ്ധിക്കുക: `conversations` ഒരു ലിസ്റ്റാണ്, അതിനാൽ ഇത്തരം ഡാറ്റ ലഭ്യമെങ്കിൽ മൾട്ടി-ടേൺ സംഭാഷണം പിന്തുണയ്ക്കാം.

## Azure GPU ക്വോട്ടാ അഭ്യർഥന

### മുന്‍നിബന്ധനകൾ

Contributor റോളോടു ചേർന്ന ഒരു Azure അക്കൗണ്ട് (അഥവാ Contributor ആക്‌സസ് ഉൾപ്പെടുന്ന മറ്റേതെങ്കിലും റോൾ) ഉണ്ടായിരിക്കണം.

നിങ്ങൾക്ക് Azure അക്കൗണ്ട് ഇല്ലെങ്കിൽ, ആരംഭിക്കുന്നതിന് മുൻപ് [ഒരു സൗജന്യ അക്കൗണ്ട് സൃഷ്ടിക്കുക](https://azure.microsoft.com).

### ക്വോട്ടാ വർദ്ധന അഭ്യർത്ഥിക്കുക

You can submit a request for a quota increase directly from My quotas. Follow the steps below to request an increase for a quota. For this example, you can select any adjustable quota in your subscription.

Sign in to the [Azure portal](https://portal.azure.com).

Enter "quotas" into the search box, and then select Quotas.
![ക്വോട്ടാ](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

On the Overview page, select a provider, such as Compute or AML.

**കുറിപ്പ്** Compute ഒഴികെയുള്ള എല്ലാ പ്രൊവൈഡറുകൾക്കും, താഴെ വിവരിച്ചിരിക്കുന്ന Adjustable കോളത്തിന്റെ പകരം Request increase കോളം കാണിക്കും. അവിടെ നിങ്ങൾ ഒരു പ്രത്യേക ക്വോട്ടയ്ക്ക് വർദ്ധന അഭ്യർത്ഥിക്കാം, അല്ലെങ്കിൽ increases-നുള്ള ഒരു support request സൃഷ്ടിക്കാം.

On the My quotas page, under Quota name, select the quota you want to increase. Make sure that the Adjustable column shows Yes for this quota.

Near the top of the page, select New Quota Request, then select Enter a new limit.

![ക്വോട്ടാ വർദ്ധിപ്പിക്കുക](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

In the New Quota Request pane, enter a numerical value for your new quota limit, then select Submit.

Your request will be reviewed, and you'll be notified if the request can be fulfilled. This usually happens within a few minutes.

If your request isn't fulfilled, you'll see a link to create a support request. When you use this link, a support engineer will assist you with your increase request.

## Azure Compute GPU machine SKU നിർദ്ദേശങ്ങൾ

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ഇവിടെ ചില ഉദാഹരണങ്ങളുണ്ട്:

### നിങ്ങളുടെ কাছে A100 അല്ലെങ്കിൽ H100 GPUകളുണ്ടെങ്കിൽ

ഫുൾ ഫൈൻട്യൂണിംഗ് സാധാരണയായി ഏറ്റവും മികച്ച പ്രകടനം നൽകും. Phi-3-V നെ hateful memes വർഗ്ഗീകരണത്തിന് ഫൈൻട്യൂൺ ചെയ്യാൻ നിങ്ങൾ താഴെ കൊടുത്തിരിക്കുന്ന കമാൻഡ് ഉപയോഗിക്കാം.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### നിങ്ങളുടെ কাছে Standard_ND40rs_v2 8x V100-32GB GPUകൾ ഉണ്ടെങ്കിൽ

Phi-3-V നെ hateful memes വർഗ്ഗീകരണത്തിൽ പൂർണ്ണമായി ഫൈൻട്യൂൺ ചെയ്യുന്നത് ഇപ്പോഴും സാധ്യമാണ്. എങ്കിലും, flash attention പിന്തുണയുടെ അഭാവം കാരണം A100 അല്ലെങ്കിൽ H100 GPUകളുമായി താരതമ്യമായി throughput വളരെ കുറവായിരിക്കും. bf16 പിന്തുണയുടെ അഭാവം കാരണം കൃത്യതക്കും ബാധിച്ചേക്കും (fp16 മിക്സ്-പ്രിസിഷൻ ട്രെയിനിംഗ് നിയന്ത്രണമായി ഉപയോഗിക്കുന്നു).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### നിങ്ങൾക്ക് ഡാറ്റാ സെന്റർ GPU-കളിലേക്ക് ആക്‌സസ് ഇല്ലെങ്കിൽ
LoRA നിങ്ങളുടെ ഏക אפשרയാകാം. Phi-3-V നെ hateful memes വർഗ്ഗീകരണത്തിന് ഫൈൻട്യൂൺ ചെയ്യാൻ നിങ്ങൾ താഴെ നൽകിയ കമാൻഡ് ഉപയോഗിക്കാം.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU-കൾക്കായി QLoRA പിന്തുണ ലഭ്യമാണ്

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ശുപാർശ ചെയ്ത ഹൈപ്പർപാരാമീറ്ററുകൾ మరియు പ്രതീക്ഷിച്ച കൃത്യത
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
ഫുൾ-ഫൈൻട്യൂണിംഗ് |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
ഫുൾ-ഫൈൻട്യൂണിംഗ് | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA ഫലങ്ങൾ ഉടൻ ഒരിവിടെ എത്തും |  |  |  |  |  |  |  |  |

### കുറിപ്പ്
താഴെ കാണിക്കുന്ന DocVQAയും Hateful memes ഫലങ്ങളും മുന്‍ പതിപ്പായ Phi-3-vision അടിസ്ഥാനത്തിലാണ്.
Phi-3.5-vision-നുള്ള പുതിയ ഫലങ്ങൾ ഉടൻ അപ്ഡേറ്റ് ചെയ്യപ്പെടും.

### DocVQA (കുറിപ്പ്: Phi-3-vision)

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
ഫുൾ-ഫൈൻട്യൂണിംഗ് | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
ഫുൾ-ഫൈൻട്യൂണിംഗ് | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (കുറിപ്പ്: Phi-3-vision)

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
ഫുൾ-ഫൈൻട്യൂണിംഗ് | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
ഫുൾ-ഫൈൻട്യൂണിംഗ് | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## സ്പീഡ്ബെഞ്ച്മാർക്കിംഗ് (കുറിപ്പ്: Phi-3-vision)

Phi-3.5-vision-നൊപ്പം പുതിയ ബെഞ്ച്മാർക്ക് ഫലങ്ങൾ ഉടൻ അപ്‌ഡേറ്റ് ചെയ്യും.

സ്പീഡ് ബെഞ്ച്മാർക്കിംഗ് DocVQA ഡാറ്റാസെറ്റിൽ നടത്തപ്പെടുന്നു. ഈ ഡാറ്റാസെറ്റിന്റെ ശരാശരി സീക്വൻസ് ദൈർഘ്യം 2443.23 ടോക്കണുകളാണ് (`num_crops=16` ഇമേജ് മോഡലിനായി ഉപയോഗിച്ച്).

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 1 | 8 |  | 64 | 5.041 |  1x | ~42
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 1 | 8 | | 64 | 2.462 |  1x | ~32
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
ഫുൾ-ഫൈൻട്യൂണിംഗ് | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
ഫ്രീസ്ഡ് ഇമേജ് മോഡൽ | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## അറിയപ്പെടുന്ന പ്രശ്നങ്ങൾ

- fp16 ഉപയോഗിച്ച് flash attention പ്രവർത്തിപ്പിക്കാൻ കഴിയില്ല (ലഭ്യമായപ്പോൾ bf16 ആക്കർഷികമായി ശിപാർശ ചെയ്യപ്പെടുന്നു, flash attention പിന്തുണയുള്ള എല്ലാ GPUകളും bf16-ഉം പിന്തുണയ്ക്കുന്നു).
- ഇടക്കാല ചെക്ക്പോയിന്റുകൾ സംരക്ഷിച്ച് പരിശീലനം പുതുക്കി ആരംഭിക്കുന്നതിനു ഇപ്പോഴുവരെ പിന്തുണയില്ല.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അറിയിപ്പ്:
ഈ രേഖ എഐ പരിഭാഷാ സേവനം Co-op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തത് ആണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, യാന്ത്രിക വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ അശുദ്ധതകൾ ഉണ്ടാകാവുന്നതാണ്. മാതൃഭാഷയിലെ യഥാർത്ഥ രേഖ അധികൃത ഉറവിടമായി പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാവുന്ന οποιεδήποτε തെറ്റുധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കുമ 우리는 ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->