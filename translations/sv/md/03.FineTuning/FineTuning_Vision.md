<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:46:38+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "sv"
}
-->
# Phi-3.5-vision finjusteringsrecept

Detta är det officiella stödet för finjustering av Phi-3.5-vision med hjälp av huggingface-bibliotek.
Var vänlig `cd` till kodmappen [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) innan du kör följande kommandon.

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

## Kom igång snabbt

Vi tillhandahåller två exempel på finjusteringsskript, ett för DocVQA och ett för klassificering av hatfyllda memes.

Minimal hårdvara testad på 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision stödjer nu officiellt multi-bildsindata. Här är ett exempel på finjustering av NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Användarguide

Beroende på hårdvaran kan användare välja olika finjusteringsstrategier. Vi stödjer
fullständig finjustering (med Deepspeed Zero-2) med valfritt frysta vision-parametrar, samt LoRA (inklusive 4bit QLoRA).
Generellt rekommenderar vi att använda fullständig finjustering med flash attention och bf16 när det är möjligt.

### guide för att konvertera din egen dataset till det kräva formatet

Vi använder en minimal videoklassificeringsdataset (en delmängd av UCF-101) som ett end-to-end-exempel för att visa hur du konverterar din egen dataset till det kräva formatet och finjusterar Phi-3.5-vision på den.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Den konverterade datan kommer att se ut så här:

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

För `jsonl`-annoteringen ska varje rad vara en ordbok som:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Observera att `conversations` är en lista, vilket innebär att flerstegs-konversationer kan stödjas om sådan data finns tillgänglig.

## Begära Azure GPU-kvot

### Förutsättningar

Ett Azure-konto med rollen Contributor (eller en annan roll som inkluderar Contributor-åtkomst).

Om du inte har ett Azure-konto, skapa ett [gratis konto innan du börjar](https://azure.microsoft.com).

### Begär en kvötsökning

Du kan skicka en begäran om kvotökning direkt från Mina kvoter. Följ stegen nedan för att begära en ökning av en kvot. För detta exempel kan du välja vilken justerbar kvot som helst i din prenumeration.

Logga in på [Azure-portalen](https://portal.azure.com).

Skriv "quotas" i sökrutan och välj sedan Quotas.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

På översiktssidan väljer du en leverantör, som Compute eller AML.

**Note** För alla leverantörer utom Compute ser du en kolumn Request increase istället för kolumnen Adjustable som beskrivs nedan. Där kan du begära en ökning för en specifik kvot eller skapa en supportförfrågan för ökningen.

På sidan Mina kvoter, under Kvotnamn, välj den kvot du vill öka. Kontrollera att kolumnen Adjustable visar Yes för denna kvot.

Nära toppen av sidan, välj New Quota Request och sedan Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

I rutan New Quota Request anger du ett numeriskt värde för din nya kvotgräns och väljer sedan Submit.

Din begäran kommer att granskas och du får besked om den kan godkännas. Detta sker vanligtvis inom några minuter.

Om din begäran inte godkänns ser du en länk för att skapa en supportförfrågan. När du använder denna länk kommer en supportingenjör att hjälpa dig med din begäran om ökning.

## Förslag på Azure Compute GPU-maskin SKU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Här är några exempel:

### Om du har A100 eller H100 GPU:er

Fullständig finjustering ger vanligtvis bäst prestanda. Du kan använda följande kommando för att finjustera Phi-3-V på klassificering av hatfyllda memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Om du har Standard_ND40rs_v2 8x V100-32GB GPU:er

Det är fortfarande möjligt att fullständigt finjustera Phi-3-V på klassificering av hatfyllda memes. Förvänta dig dock
mycket lägre genomströmning jämfört med A100 eller H100 GPU:er på grund av brist på stöd för flash attention.
Noggrannheten kan också påverkas på grund av brist på bf16-stöd (fp16 mixed-precision träning används istället).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Om du inte har tillgång till datacenter-GPU:er
LoRA kan vara ditt enda alternativ. Du kan använda följande kommando för att finjustera Phi-3-V på klassificering av hatfyllda memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

För Turing+ GPU:er stöds QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Föreslagna hyperparametrar och förväntad noggrannhet
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

Träningsmetod | Fryst visionmodell | datatyp | LoRA-rank | LoRA-alpha | batchstorlek | inlärningshastighet | epoker | Noggrannhet
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA-resultat kommer snart |  |  |  |  |  |  |  |  |

### NOTE
Nedanstående DocVQA och Hateful memes-resultat baseras på föregående version (Phi-3-vision).
De nya resultaten med Phi-3.5-vision kommer att uppdateras snart.

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

Träningsmetod | datatyp | LoRA-rank | LoRA-alpha | batchstorlek | inlärningshastighet | epoker | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
fryst bildmodell| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
fryst bildmodell| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Träningsmetod | datatyp | LoRA-rank | LoRA-alpha | batchstorlek | inlärningshastighet | epoker | Noggrannhet
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
fryst bildmodell| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
fryst bildmodell| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Hastighetsbenchmarking (NOTE: Phi-3-vision)

Nya benchmarkresultat med Phi-3.5-vision kommer att uppdateras snart.

Hastighetsbenchmarking utförs på DocVQA-datasetet. Den genomsnittliga sekvenslängden för denna dataset
är 2443.23 tokens (med `num_crops=16` för bildmodellen).

### 8x A100-80GB (Ampere)

Träningsmetod | \# noder | GPU:er | flash attention | Effektiv batchstorlek | Genomströmning (bild/s) | Acceleration | Max GPU-minne (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
fryst bildmodell | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
fryst bildmodell | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Träningsmetod | \# noder | GPU:er | flash attention | Effektiv batchstorlek | Genomströmning (bild/s) | Acceleration | Max GPU-minne (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
fryst bildmodell | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Kända problem

- Kan inte köra flash attention med fp16 (bf16 rekommenderas alltid när det finns tillgängligt, och alla GPU:er som stödjer flash attention stödjer också bf16).
- Stöder ännu inte att spara mellanliggande checkpoints och återuppta träning.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.