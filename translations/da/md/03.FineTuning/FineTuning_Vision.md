<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:47:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "da"
}
-->
# Phi-3.5-vision finjusteringsopskrift

Dette er den officielle support til finjustering af Phi-3.5-vision ved brug af huggingface-biblioteker.  
Skift venligst til kodebiblioteket [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) med `cd`, før du kører følgende kommandoer.

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

## Hurtig start

Vi tilbyder to eksempler på finjusteringsscripts, et til DocVQA og et til klassificering af hatefulde memes.

Minimal hardware testet på 4x RTX8000 (48GB RAM pr. GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision understøtter nu officielt multi-billede input. Her er et eksempel på finjustering af NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Brugervejledning

Afhængigt af hardwaren kan brugere vælge forskellige finjusteringsstrategier. Vi understøtter  
full-finetuning (med Deepspeed Zero-2) med valgfrit frosne vision-parametre, samt LoRA (inklusive 4bit QLoRA).  
Generelt anbefaler vi at bruge fuld finjustering med flash attention og bf16, når det er muligt.

### Vejledning til konvertering af dit eget datasæt til det krævede format

Vi bruger et minimalt videoklassifikationsdatasæt (et subset af UCF-101) som et end-to-end eksempel for at demonstrere, hvordan du konverterer dit eget datasæt til det krævede format og finjusterer Phi-3.5-vision på det.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

De konverterede data vil se sådan ud:

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

For `jsonl` annotationen skal hver linje være et dictionary som:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Bemærk, at `conversations` er en liste, så multi-turn samtaler kan understøttes, hvis sådanne data er tilgængelige.

## Anmodning om Azure GPU-kvote

### Forudsætninger

En Azure-konto med Contributor-rollen (eller en anden rolle, der inkluderer Contributor-adgang).

Hvis du ikke har en Azure-konto, kan du oprette en [gratis konto før du begynder](https://azure.microsoft.com).

### Anmod om kvoteforhøjelse

Du kan indsende en anmodning om kvoteforhøjelse direkte fra My quotas. Følg nedenstående trin for at anmode om en forhøjelse af en kvote. I dette eksempel kan du vælge en hvilken som helst justerbar kvote i dit abonnement.

Log ind på [Azure-portalen](https://portal.azure.com).

Indtast "quotas" i søgefeltet, og vælg derefter Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

På oversigtssiden vælger du en udbyder, såsom Compute eller AML.

**Note** For alle udbydere undtagen Compute vil du se en kolonne med Request increase i stedet for Adjustable-kolonnen beskrevet nedenfor. Her kan du anmode om en forhøjelse for en specifik kvote eller oprette en supportsag for forhøjelsen.

På siden My quotas, under Quota name, vælg den kvote, du ønsker at forhøje. Sørg for, at kolonnen Adjustable viser Yes for denne kvote.

Næsten øverst på siden vælger du New Quota Request, og derefter Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

I panelet New Quota Request indtaster du en numerisk værdi for din nye kvotegrænse og vælger derefter Submit.

Din anmodning vil blive gennemgået, og du vil blive underrettet, hvis anmodningen kan imødekommes. Dette sker normalt inden for få minutter.

Hvis din anmodning ikke imødekommes, vil du se et link til at oprette en supportsag. Når du bruger dette link, vil en supportingeniør hjælpe dig med din anmodning om forhøjelse.

## Forslag til Azure Compute GPU-maskine SKU'er

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Her er nogle eksempler:

### Hvis du har A100 eller H100 GPU'er

Fuld finjustering giver som regel den bedste ydeevne. Du kan bruge følgende kommando til at finjustere Phi-3-V på klassificering af hatefulde memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Hvis du har Standard_ND40rs_v2 8x V100-32GB GPU'er

Det er stadig muligt at fuld finjustere Phi-3-V på klassificering af hatefulde memes. Forvent dog  
meget lavere gennemløb sammenlignet med A100 eller H100 GPU'er på grund af manglende support for flash attention.  
Nøjagtigheden kan også blive påvirket på grund af manglende bf16-support (fp16 mixed-precision træning bruges i stedet).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Hvis du ikke har adgang til datacenter-GPU'er

LoRA kan være dit eneste valg. Du kan bruge følgende kommando til at finjustere Phi-3-V på klassificering af hatefulde memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

For Turing+ GPU'er understøttes QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Foreslåede hyperparametre og forventet nøjagtighed

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

Træningsmetode | Frosset visionmodel | datatype | LoRA-rang | LoRA alpha | batchstørrelse | læringsrate | epoker | Nøjagtighed  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20  
LoRA resultater kommer snart |  |  |  |  |  |  |  |  |

### NOTE  
De nedenstående DocVQA og Hateful memes resultater er baseret på den tidligere version (Phi-3-vision).  
De nye resultater med Phi-3.5-vision opdateres snart.

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

Træningsmetode | datatype | LoRA-rang | LoRA alpha | batchstørrelse | læringsrate | epoker | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60  
frosset billedmodel | bf16 | - | - | 64 | 1e-4 | 2 | 79.19  
frosset billedmodel | fp16 | - | - | 64 | 1e-4 | 2 | 78.74  
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

Træningsmetode | datatype | LoRA-rang | LoRA alpha | batchstørrelse | læringsrate | epoker | Nøjagtighed  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4  
frosset billedmodel | bf16 | - | - | 64 | 1e-4 | 3 | 79.4  
frosset billedmodel | fp16 | - | - | 64 | 1e-4 | 3 | 78.6  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8  

## Hastighedsbenchmarking (NOTE: Phi-3-vision)

Nye benchmarkresultater med Phi-3.5-vision opdateres snart.

Hastighedsbenchmarking er udført på DocVQA-datasættet. Den gennemsnitlige sekvenslængde i dette datasæt  
er 2443.23 tokens (ved brug af `num_crops=16` for billedmodellen).

### 8x A100-80GB (Ampere)

Træningsmetode | \# noder | GPU'er | flash attention | Effektiv batchstørrelse | Gennemløb (billeder/s) | Hastighedsforøgelse | Maks GPU-mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
frosset billedmodel | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
frosset billedmodel | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Træningsmetode | \# noder | GPU'er | flash attention | Effektiv batchstørrelse | Gennemløb (billeder/s) | Hastighedsforøgelse | Maks GPU-mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frosset billedmodel | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Kendte problemer

- Kan ikke køre flash attention med fp16 (bf16 anbefales altid, når det er tilgængeligt, og alle GPU'er, der understøtter flash attention, understøtter også bf16).  
- Understøtter endnu ikke at gemme mellemliggende checkpoints og genoptage træning.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.