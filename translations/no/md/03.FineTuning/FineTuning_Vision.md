<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:03:06+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "no"
}
-->
# Phi-3.5-vision finjusteringsoppskrift

Dette er den offisielle støtten for finjustering av Phi-3.5-vision ved bruk av huggingface-biblioteker.  
Vennligst `cd` til kodekatalogen [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) før du kjører følgende kommandoer.

## Installasjon

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

## Rask start

Vi tilbyr to eksempelskript for finjustering, ett for DocVQA og ett for klassifisering av hatefulle memes.

Minimal maskinvare testet på 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision støtter nå offisielt multi-bilde input. Her er et eksempel på finjustering for NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Brukerveiledning

Avhengig av maskinvaren kan brukere velge forskjellige finjusteringsstrategier. Vi støtter  
full finjustering (med Deepspeed Zero-2) med valgfritt frosne visuelle parametere, og LoRA (inkludert 4bit QLoRA).  
Generelt anbefaler vi å bruke full finjustering med flash attention og bf16 når det er mulig.

### Veiledning for å konvertere ditt eget datasett til ønsket format

Vi bruker et minimalt videoklassifiseringsdatasett (et delsett av UCF-101) som et ende-til-ende eksempel for å vise hvordan du konverterer ditt eget datasett til ønsket format og finjusterer Phi-3.5-vision på det.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

De konverterte dataene vil se slik ut:

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

For `jsonl`-annotasjonen skal hver linje være et ordbokslignende objekt som dette:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Merk at `conversations` er en liste, så fleromgangssamtaler kan støttes hvis slik data er tilgjengelig.

## Søke om Azure GPU-kvote

### Forutsetninger

En Azure-konto med Contributor-rollen (eller en annen rolle som inkluderer Contributor-tilgang).

Hvis du ikke har en Azure-konto, opprett en [gratis konto før du begynner](https://azure.microsoft.com).

### Be om økning av kvote

Du kan sende inn en forespørsel om kvoteøkning direkte fra Mine kvoter. Følg trinnene nedenfor for å be om en økning for en kvote. For dette eksempelet kan du velge hvilken som helst justerbar kvote i abonnementet ditt.

Logg inn på [Azure-portalen](https://portal.azure.com).

Skriv "quotas" i søkeboksen, og velg deretter Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

På Oversikt-siden velger du en leverandør, som Compute eller AML.

**Merk** For alle leverandører unntatt Compute, vil du se en kolonne for Request increase i stedet for Adjustable-kolonnen som er beskrevet nedenfor. Der kan du be om økning for en spesifikk kvote, eller opprette en supportforespørsel for økningen.

På siden Mine kvoter, under Kvotenavn, velg kvoten du ønsker å øke. Sørg for at Adjustable-kolonnen viser Ja for denne kvoten.

Nær toppen av siden, velg Ny kvoteforspørsel, og deretter Velg Angi en ny grense.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

I panelet Ny kvoteforspørsel, skriv inn en numerisk verdi for din nye kvotegrense, og velg deretter Send inn.

Forespørselen din vil bli gjennomgått, og du vil bli varslet hvis den kan innfris. Dette skjer vanligvis innen få minutter.

Hvis forespørselen ikke blir innfridd, vil du se en lenke for å opprette en supportforespørsel. Når du bruker denne lenken, vil en supportingeniør hjelpe deg med økningsforespørselen.

## Forslag til Azure Compute GPU-maskin SKU

[ND A100 v4-serie](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serie](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Her er noen eksempler:

### Hvis du har A100 eller H100 GPUer

Full finjustering gir vanligvis best ytelse. Du kan bruke følgende kommando for å finjustere Phi-3-V på hatefulle memes-klassifisering.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Hvis du har Standard_ND40rs_v2 med 8x V100-32GB GPUer

Det er fortsatt mulig å fullfinjustere Phi-3-V på hatefulle memes-klassifisering. Forvent imidlertid mye lavere gjennomstrømning sammenlignet med A100 eller H100 GPUer på grunn av manglende støtte for flash attention.  
Nøyaktigheten kan også påvirkes på grunn av manglende bf16-støtte (fp16 blandet presisjonstrening brukes i stedet).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Hvis du ikke har tilgang til datasenter-GPUer

LoRA kan være ditt eneste alternativ. Du kan bruke følgende kommando for å finjustere Phi-3-V på hatefulle memes-klassifisering.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

For Turing+ GPUer støttes QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Foreslåtte hyperparametere og forventet nøyaktighet  
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

Treningsmetode | Frosset visjonsmodell | datatype | LoRA-rang | LoRA alfa | batchstørrelse | læringsrate | epoker | Nøyaktighet  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA-resultater kommer snart |  |  |  |  |  |  |  |  |

### MERK  
Resultatene for DocVQA og Hateful memes nedenfor er basert på forrige versjon (Phi-3-vision).  
De nye resultatene med Phi-3.5-vision vil bli oppdatert snart.

### DocVQA (MERK: Phi-3-vision)

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

Treningsmetode | datatype | LoRA-rang | LoRA alfa | batchstørrelse | læringsrate | epoker | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
frosset bildemodell | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frosset bildemodell | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (MERK: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Treningsmetode | datatype | LoRA-rang | LoRA alfa | batchstørrelse | læringsrate | epoker | Nøyaktighet  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
frosset bildemodell | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frosset bildemodell | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Hastighetsbenchmarking (MERK: Phi-3-vision)

Nye benchmarkresultater med Phi-3.5-vision vil bli oppdatert snart.

Hastighetsbenchmarking er utført på DocVQA-datasettet. Gjennomsnittlig sekvenslengde i dette datasettet  
er 2443.23 tokens (ved bruk av `num_crops=16` for bildemodellen).

### 8x A100-80GB (Ampere)

Treningsmetode | \# noder | GPUer | flash attention | Effektiv batchstørrelse | Gjennomstrømning (bilder/s) | Hastighetsøkning | Maks GPU-minne (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
frosset bildemodell | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
frosset bildemodell | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Treningsmetode | \# noder | GPUer | flash attention | Effektiv batchstørrelse | Gjennomstrømning (bilder/s) | Hastighetsøkning | Maks GPU-minne (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frosset bildemodell | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Kjente problemer

- Kan ikke kjøre flash attention med fp16 (bf16 anbefales alltid når det er tilgjengelig, og alle GPUer som støtter flash attention støtter også bf16).  
- Støtter foreløpig ikke lagring av mellomliggende sjekkpunkter eller gjenopptakelse av trening.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.