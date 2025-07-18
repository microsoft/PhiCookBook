<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:48:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "nl"
}
-->
# Phi-3.5-vision finetuning recept

Dit is de officiële ondersteuning voor Phi-3.5-vision finetuning met behulp van huggingface libraries.  
Ga eerst naar de code directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) voordat je de volgende commando's uitvoert.

## Installatie

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

## Snel aan de slag

We bieden twee voorbeeldscripts voor finetuning, één voor DocVQA en één voor classificatie van hatelijke memes.

Minimale hardware getest op 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ondersteunt nu officieel multi-image inputs. Hier is een voorbeeld voor finetuning van NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Gebruiksaanwijzing

Afhankelijk van de hardware kunnen gebruikers verschillende finetuning strategieën kiezen. We ondersteunen  
full-finetuning (met Deepspeed Zero-2) met optioneel bevroren vision parameters, en LoRA (inclusief 4bit QLoRA).  
Over het algemeen raden we aan om full finetuning te gebruiken met flash attention en bf16 waar mogelijk.

### gids voor het omzetten van je eigen dataset naar het vereiste formaat

We gebruiken een minimale video-classificatie dataset (een subset van UCF-101) als een end-to-end voorbeeld om te laten zien hoe je je eigen dataset kunt omzetten naar het vereiste formaat en Phi-3.5-vision daarop kunt finetunen.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

De geconverteerde data ziet er als volgt uit:

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

Voor de `jsonl` annotatie moet elke regel een dictionary zijn zoals:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Let op dat `conversations` een lijst is, waardoor multi-turn gesprekken ondersteund kunnen worden als dergelijke data beschikbaar is.

## Azure GPU Quota aanvragen

### Vereisten

Een Azure-account met de rol Contributor (of een andere rol die Contributor-toegang bevat).

Als je nog geen Azure-account hebt, maak dan een [gratis account aan voordat je begint](https://azure.microsoft.com).

### Vraag een verhoging van je quota aan

Je kunt een verzoek indienen voor een verhoging van je quota rechtstreeks via Mijn quota. Volg onderstaande stappen om een verhoging aan te vragen. Voor dit voorbeeld kun je elke aanpasbare quota in je abonnement selecteren.

Meld je aan bij de [Azure portal](https://portal.azure.com).

Typ "quotas" in het zoekvak en selecteer vervolgens Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Selecteer op de overzichtspagina een provider, zoals Compute of AML.

**Note** Voor alle providers behalve Compute zie je een kolom Request increase in plaats van de kolom Adjustable zoals hieronder beschreven. Daar kun je een verhoging aanvragen voor een specifieke quota, of een supportverzoek indienen voor de verhoging.

Op de pagina Mijn quota, selecteer onder Quota name de quota die je wilt verhogen. Zorg ervoor dat in de kolom Adjustable voor deze quota Ja staat.

Selecteer bovenaan de pagina New Quota Request en kies vervolgens Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Voer in het paneel New Quota Request een numerieke waarde in voor je nieuwe quota limiet en klik op Submit.

Je verzoek wordt beoordeeld en je ontvangt een melding of het verzoek kan worden ingewilligd. Dit gebeurt meestal binnen enkele minuten.

Als je verzoek niet wordt ingewilligd, zie je een link om een supportverzoek aan te maken. Wanneer je deze link gebruikt, helpt een support engineer je met je verhogingsverzoek.

## Azure Compute GPU machine SKU suggesties

[ND A100 v4-serie](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serie](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Hier zijn enkele voorbeelden:

### Als je A100 of H100 GPU's hebt

Full finetuning levert meestal de beste prestaties. Je kunt het volgende commando gebruiken om Phi-3-V te finetunen op classificatie van hatelijke memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Als je Standard_ND40rs_v2 8x V100-32GB GPU's hebt

Het is nog steeds mogelijk om Phi-3-V volledig te finetunen op classificatie van hatelijke memes. Verwacht echter  
veel lagere doorvoer vergeleken met A100 of H100 GPU's vanwege het ontbreken van ondersteuning voor flash attention.  
De nauwkeurigheid kan ook beïnvloed worden door het ontbreken van bf16-ondersteuning (in plaats daarvan wordt fp16 mixed-precision training gebruikt).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Als je geen toegang hebt tot datacenter GPU's

LoRA is dan waarschijnlijk je enige optie. Je kunt het volgende commando gebruiken om Phi-3-V te finetunen op classificatie van hatelijke memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Voor Turing+ GPU's wordt QLoRA ondersteund

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Aanbevolen hyperparameters en verwachte nauwkeurigheid

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

Trainingsmethode | Bevroren vision model | datatype | LoRA rank | LoRA alpha | batchgrootte | leersnelheid | epochs | Nauwkeurigheid
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA resultaten volgen binnenkort |  |  |  |  |  |  |  |  |

### NOTE  
De onderstaande DocVQA en Hateful memes resultaten zijn gebaseerd op de vorige versie (Phi-3-vision).  
De nieuwe resultaten met Phi-3.5-vision worden binnenkort bijgewerkt.

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

Trainingsmethode | datatype | LoRA rank | LoRA alpha | batchgrootte | leersnelheid | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
bevroren beeldmodel | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
bevroren beeldmodel | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Trainingsmethode | datatype | LoRA rank | LoRA alpha | batchgrootte | leersnelheid | epochs | Nauwkeurigheid
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
bevroren beeldmodel | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
bevroren beeldmodel | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Snelheidsbenchmark (NOTE: Phi-3-vision)

Nieuwe benchmarkresultaten met Phi-3.5-vision worden binnenkort bijgewerkt.

De snelheidsbenchmark is uitgevoerd op de DocVQA dataset. De gemiddelde sequentielengte van deze dataset  
is 2443.23 tokens (met `num_crops=16` voor het beeldmodel).

### 8x A100-80GB (Ampere)

Trainingsmethode | \# nodes | GPU's | flash attention | Effectieve batchgrootte | Doorvoer (img/s) | Versnelling | Max GPU geheugen (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
bevroren beeldmodel | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
bevroren beeldmodel | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Trainingsmethode | \# nodes | GPU's | flash attention | Effectieve batchgrootte | Doorvoer (img/s) | Versnelling | Max GPU geheugen (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
bevroren beeldmodel | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Bekende problemen

- Flash attention werkt niet met fp16 (bf16 wordt altijd aanbevolen wanneer beschikbaar, en alle GPU's die flash attention ondersteunen, ondersteunen ook bf16).  
- Het is nog niet mogelijk om tussentijdse checkpoints op te slaan en training te hervatten.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.