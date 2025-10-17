<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-10-11T11:42:48+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ta"
}
-->
# Phi-3.5-vision நுண்ணிய அமைப்புக்கான வழிகாட்டி

இது huggingface நூலகங்களைப் பயன்படுத்தி Phi-3.5-vision நுண்ணிய அமைப்புக்கான அதிகாரப்பூர்வ ஆதரவு ஆகும். கீழே உள்ள கட்டளைகளை இயக்குவதற்கு முன் [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) என்ற கோப்பு அடைவிற்கு `cd` செய்யவும்.

## நிறுவல்

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

## விரைவான தொடக்கம்

DocVQA மற்றும் hateful meme வகைப்பாட்டிற்கான இரண்டு உதாரண நுண்ணிய அமைப்பு ஸ்கிரிப்ட்களை நாங்கள் வழங்குகிறோம்.

குறைந்தபட்சமாக 4x RTX8000 (ஒரு GPUக்கு 48GB RAM) ஹார்ட்வேர் சோதிக்கப்பட்டது.

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision இப்போது பல பட உள்ளீடுகளை அதிகாரப்பூர்வமாக ஆதரிக்கிறது. NLVR2 க்கான நுண்ணிய அமைப்புக்கான ஒரு உதாரணம் இதோ:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## பயன்பாட்டு வழிகாட்டி

ஹார்ட்வேர் அடிப்படையில், பயனர்கள் வெவ்வேறு நுண்ணிய அமைப்பு உத்திகளைத் தேர்ந்தெடுக்கலாம். Deepspeed Zero-2 உடன் முழு நுண்ணிய அமைப்பை (தனித்துவமாக காட்சி அளவுருக்களை உறையவைத்து) மற்றும் LoRA (4bit QLoRA உட்பட) ஆதரிக்கிறோம். பொதுவாக, flash attention மற்றும் bf16 உடன் முழு நுண்ணிய அமைப்பை wherever சாத்தியமானது பயன்படுத்த பரிந்துரைக்கிறோம்.

### உங்கள் தனிப்பயன் தரவுத்தொகுப்பை தேவையான வடிவத்திற்கு மாற்றுவதற்கான வழிகாட்டி

உங்கள் தனிப்பயன் தரவுத்தொகுப்பை தேவையான வடிவத்திற்கு மாற்றி, அதில் Phi-3.5-vision ஐ நுண்ணிய அமைப்புடன் fine-tune செய்ய எப்படி என்பதை விளக்க, குறைந்தபட்ச வீடியோ வகைப்பாட்டு தரவுத்தொகுப்பை (UCF-101 இன் ஒரு துண்டு) ஒரு முடிவுக்கு முடிவு செய்யும் உதாரணமாக பயன்படுத்துகிறோம்.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

மாற்றியமைக்கப்பட்ட தரவுகள் இவ்வாறு இருக்கும்:

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

`jsonl` குறிப்பு, ஒவ்வொரு வரியும் ஒரு அகராதியாக இருக்க வேண்டும்:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations` என்பது ஒரு பட்டியல், எனவே பல முறை உரையாடல்களையும் ஆதரிக்க முடியும், அத்தகைய தரவுகள் கிடைத்தால்.

## Azure GPU கோட்டா கோரிக்கை

### முன்னேற்பாடுகள்

Contributor பங்கு (அல்லது Contributor அணுகலை உள்ளடக்கிய மற்றொரு பங்கு) கொண்ட Azure கணக்கு.

Azure கணக்கு இல்லையெனில், [இலவச கணக்கை உருவாக்கவும்](https://azure.microsoft.com).

### கோட்டா அதிகரிக்க கோரிக்கை

My quotas இல் நேரடியாக ஒரு கோட்டா அதிகரிக்க கோரிக்கையை சமர்ப்பிக்கலாம். உங்கள் சந்தாவில் எந்தவொரு சரிசெய்யக்கூடிய கோட்டாவையும் தேர்ந்தெடுக்க கீழே உள்ள படிகளைப் பின்பற்றவும்.

[Azure portal](https://portal.azure.com) இல் உள்நுழைக.

தேடல் பெட்டியில் "quotas" என உள்ளீடு செய்து, பின்னர் Quotas ஐத் தேர்ந்தெடுக்கவும்.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview பக்கத்தில், Compute அல்லது AML போன்ற ஒரு வழங்குநரைத் தேர்ந்தெடுக்கவும்.

**குறிப்பு** Compute தவிர மற்ற அனைத்து வழங்குநர்களுக்கும், கீழே விவரிக்கப்பட்ட Adjustable பத்தி பதிலாக Request increase பத்தியை காணலாம். அங்கு, ஒரு குறிப்பிட்ட கோட்டாவுக்கு அதிகரிக்க கோரிக்கையைச் செய்யலாம் அல்லது அதிகரிக்க கோரிக்கைக்காக ஒரு ஆதரவு கோரிக்கையை உருவாக்கலாம்.

My quotas பக்கத்தில், Quota name கீழ், நீங்கள் அதிகரிக்க விரும்பும் கோட்டாவைத் தேர்ந்தெடுக்கவும். இந்த கோட்டாவுக்கு Adjustable பத்தியில் Yes என்று காட்டப்படுகிறதா என்பதை உறுதிசெய்யவும்.

பக்கத்தின் மேல் பகுதியில், New Quota Request ஐத் தேர்ந்தெடுத்து, பின்னர் Enter a new limit ஐத் தேர்ந்தெடுக்கவும்.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request பக்கத்தில், உங்கள் புதிய கோட்டா வரம்புக்கான எண் மதிப்பை உள்ளீடு செய்து, பின்னர் Submit ஐத் தேர்ந்தெடுக்கவும்.

உங்கள் கோரிக்கை பரிசீலிக்கப்படும், மேலும் கோரிக்கையை நிறைவேற்ற முடியுமா என்பதை உங்களுக்கு அறிவிக்கப்படும். இது பொதுவாக சில நிமிடங்களில் நடக்கிறது.

உங்கள் கோரிக்கையை நிறைவேற்ற முடியாவிட்டால், அதிகரிக்க கோரிக்கைக்காக ஆதரவு கோரிக்கையை உருவாக்க ஒரு இணைப்பை காணலாம். இந்த இணைப்பைப் பயன்படுத்தும்போது, ஒரு ஆதரவு பொறியாளர் உங்கள் கோரிக்கையை அதிகரிக்க உதவுவார்.

## Azure Compute GPU இயந்திர SKU பரிந்துரைகள்

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

இதோ சில உதாரணங்கள்:

### உங்களிடம் A100 அல்லது H100 GPUs இருந்தால்

முழு நுண்ணிய அமைப்பு பொதுவாக சிறந்த செயல்திறனை வழங்கும். Hateful memes வகைப்பாட்டிற்கான Phi-3-V ஐ நுண்ணிய அமைப்புடன் fine-tune செய்ய நீங்கள் பின்வரும் கட்டளையைப் பயன்படுத்தலாம்.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### உங்களிடம் Standard_ND40rs_v2 8x V100-32GB GPUs இருந்தால்

Hateful memes வகைப்பாட்டிற்கான Phi-3-V ஐ முழுமையாக நுண்ணிய அமைப்புடன் fine-tune செய்வது இன்னும் சாத்தியமாகும். ஆனால், flash attention ஆதரவு இல்லாததால், A100 அல்லது H100 GPUs உடன் ஒப்பிடும்போது மிகவும் குறைந்த திறன் எதிர்பார்க்கலாம். bf16 ஆதரவு இல்லாததால் (fp16 mixed-precision பயிற்சி பதிலாக பயன்படுத்தப்படுகிறது) துல்லியத்திலும் பாதிப்பு ஏற்படலாம்.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### உங்களிடம் தரவுத்தொகுப்பு மைய GPU கள் கிடைக்காவிட்டால்
LoRA உங்கள் ஒரே தேர்வாக இருக்கலாம். Hateful memes வகைப்பாட்டிற்கான Phi-3-V ஐ நுண்ணிய அமைப்புடன் fine-tune செய்ய நீங்கள் பின்வரும் கட்டளையைப் பயன்படுத்தலாம்.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU க்கான QLoRA ஆதரிக்கப்படுகிறது.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## பரிந்துரைக்கப்பட்ட ஹைப்பர்பாராமீட்டர்கள் மற்றும் எதிர்பார்க்கப்படும் துல்லியம்
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

பயிற்சி முறை | உறைந்த காட்சி மாதிரி | தரவின் வகை | LoRA rank | LoRA alpha | தொகுப்பு அளவு | கற்றல் வீதம் | காலங்கள் | துல்லியம்
--- | --- | --- | --- | --- | --- | --- | --- | --- |
முழு நுண்ணிய அமைப்பு |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
முழு நுண்ணிய அமைப்பு | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA முடிவுகள் விரைவில் வரும் |  |  |  |  |  |  |  |  |

### குறிப்பு
கீழே உள்ள DocVQA மற்றும் Hateful memes முடிவுகள் முந்தைய பதிப்பின் (Phi-3-vision) அடிப்படையில் உள்ளன. Phi-3.5-vision உடன் புதிய முடிவுகள் விரைவில் புதுப்பிக்கப்படும்.

### DocVQA (குறிப்பு: Phi-3-vision)

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

பயிற்சி முறை | தரவின் வகை | LoRA rank | LoRA alpha | தொகுப்பு அளவு | கற்றல் வீதம் | காலங்கள் | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
முழு நுண்ணிய அமைப்பு | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
முழு நுண்ணிய அமைப்பு | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
உறைந்த காட்சி மாதிரி| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
உறைந்த காட்சி மாதிரி| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (குறிப்பு: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

பயிற்சி முறை | தரவின் வகை | LoRA rank | LoRA alpha | தொகுப்பு அளவு | கற்றல் வீதம் | காலங்கள் | துல்லியம்
--- | --- | --- | --- | --- | --- | --- | --- |
முழு நுண்ணிய அமைப்பு | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
முழு நுண்ணிய அமைப்பு | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
உறைந்த காட்சி மாதிரி| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
உறைந்த காட்சி மாதிரி| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## வேக அளவீடு (குறிப்பு: Phi-3-vision)

Phi-3.5-vision உடன் புதிய வேக அளவீட்டு முடிவுகள் விரைவில் புதுப்பிக்கப்படும்.

வேக அளவீடு DocVQA தரவுத்தொகுப்பில் செய்யப்பட்டது. இந்த தரவுத்தொகுப்பின் சராசரி வரிசை நீளம் 2443.23 டோக்கன்கள் (காட்சி மாதிரிக்காக `num_crops=16` பயன்படுத்தப்பட்டது).

### 8x A100-80GB (Ampere)

பயிற்சி முறை | \# nodes | GPUs | flash attention | செயல்பாட்டு தொகுப்பு அளவு | Throughput (img/s) | வேக உயர்வு | உச்ச GPU நினைவகம் (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
முழு நுண்ணிய அமைப்பு | 1 | 8 |  | 64 | 5.041 |  1x | ~42
முழு நுண்ணிய அமைப்பு | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
முழு நுண்ணிய அமைப்பு | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
முழு நுண்ணிய அமைப்பு | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
உறைந்த காட்சி மாதிரி | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
உறைந்த காட்சி மாதிரி | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

பயிற்சி முறை | \# nodes | GPUs | flash attention | செயல்பாட்டு தொகுப்பு அளவு | Throughput (img/s) | வேக உயர்வு | உச்ச GPU நினைவகம் (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
முழு நுண்ணிய அமைப்பு | 1 | 8 | | 64 | 2.462 |  1x | ~32
முழு நுண்ணிய அமைப்பு | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
முழு நுண்ணிய அமைப்பு | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
உறைந்த காட்சி மாதிரி | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## அறியப்பட்ட பிரச்சினைகள்

- fp16 உடன் flash attention இயங்க முடியாது (bf16 கிடைக்கும் போது எப்போதும் பரிந்துரைக்கப்படுகிறது, மேலும் flash attention ஐ ஆதரிக்கும் அனைத்து GPUs களும் bf16 ஐ ஆதரிக்கின்றன).  
- இடைநிலை சேமிப்பு புள்ளிகளைச் சேமித்து பயிற்சியை மீண்டும் தொடங்குவதற்கு இன்னும் ஆதரவு இல்லை.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.