<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-10-11T11:43:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "et"
}
-->
# Phi-3.5-vision peenhäälestamise juhend

See on ametlik tugi Phi-3.5-vision peenhäälestamiseks, kasutades Huggingface'i teeke. Enne järgmiste käskude käivitamist liikuge kataloogi [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Paigaldamine

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

## Kiire alustamine

Pakume kahte näidispeenhäälestamise skripti: üks DocVQA jaoks ja teine vihkavate meemide klassifitseerimiseks.

Minimaalsed testitud riistvaranõuded: 4x RTX8000 (48GB RAM iga GPU kohta)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision toetab nüüd ametlikult mitme pildi sisendeid. Siin on näide NLVR2 peenhäälestamiseks.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Kasutusjuhend

Sõltuvalt riistvarast võivad kasutajad valida erinevaid peenhäälestamise strateegiaid. Toetame täispeenhäälestamist (Deepspeed Zero-2-ga) koos võimalusega külmutada visiooniparameetrid, samuti LoRA-d (sealhulgas 4bit QLoRA). Üldiselt soovitame kasutada täispeenhäälestamist koos flash attentioni ja bf16-ga, kui see on võimalik.

### Juhend oma kohandatud andmestiku konverteerimiseks nõutud formaati

Kasutame minimaalset videoklassifikatsiooni andmestikku (UCF-101 alamhulk) näitena, et demonstreerida, kuidas konverteerida oma kohandatud andmestik nõutud formaati ja peenhäälestada Phi-3.5-vision sellel.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Konverteeritud andmed näevad välja sellised:

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

`jsonl` annotatsiooni puhul peaks iga rida olema sõnastik, näiteks:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Pange tähele, et `conversations` on loend, seega saab toetada mitme pöördega vestlusi, kui sellised andmed on saadaval.

## Azure GPU kvoodi taotlemine 

### Eeltingimused

Azure'i konto koos Contributor rolliga (või mõne muu rolliga, mis sisaldab Contributor ligipääsu).

Kui teil pole Azure'i kontot, looge [tasuta konto enne alustamist](https://azure.microsoft.com).

### Kvoodi suurendamise taotlemine

Kvoodi suurendamise taotluse saab esitada otse Minu kvoodid lehelt. Järgige alltoodud samme, et taotleda kvoodi suurendamist. Näiteks võite valida mis tahes reguleeritava kvoodi oma tellimuses.

Logige sisse [Azure'i portaali](https://portal.azure.com).

Sisestage otsingukasti "quotas" ja valige Quotas.
![Kvoot](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Ülevaate lehel valige pakkuja, näiteks Compute või AML.

**Märkus** Kõigi pakkujate puhul peale Compute'i näete veerus Request increase veergu, mitte reguleeritavat veergu, mida allpool kirjeldatakse. Seal saate taotleda konkreetse kvoodi suurendamist või luua suurendamise taotluse jaoks tugitaotluse.

Minu kvoodid lehel valige kvoot, mida soovite suurendada. Veenduge, et reguleeritav veerg näitab selle kvoodi puhul Jah.

Lehe ülaosas valige New Quota Request ja seejärel Enter a new limit.

![Suurenda kvooti](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Uue kvoodi taotluse paneelil sisestage oma uue kvoodi limiidi jaoks numbriline väärtus ja valige Submit.

Teie taotlust vaadatakse läbi ja teid teavitatakse, kas taotlust saab täita. Tavaliselt juhtub see mõne minuti jooksul.

Kui teie taotlust ei täideta, näete linki tugitaotluse loomiseks. Selle lingi kasutamisel aitab tugiteenuse insener teid suurendamise taotlusega.

## Azure Compute GPU masinate SKU soovitused

[ND A100 v4-seeria](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-seeria](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Siin on mõned näited:

### Kui teil on A100 või H100 GPU-d

Täispeenhäälestamine annab tavaliselt parima jõudluse. Võite kasutada järgmist käsku, et peenhäälestada Phi-3-V vihkavate meemide klassifitseerimiseks.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Kui teil on Standard_ND40rs_v2 8x V100-32GB GPU-d

Phi-3-V peenhäälestamine vihkavate meemide klassifitseerimiseks on endiselt võimalik. Kuid oodake palju madalamat läbilaskevõimet võrreldes A100 või H100 GPU-dega flash attentioni toe puudumise tõttu. Täpsus võib samuti olla mõjutatud bf16 toe puudumise tõttu (fp16 segatäpsusega treenimist kasutatakse selle asemel).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Kui teil pole juurdepääsu andmekeskuse GPU-dele
LoRA võib olla teie ainus valik. Võite kasutada järgmist käsku, et peenhäälestada Phi-3-V vihkavate meemide klassifitseerimiseks.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU-de puhul toetatakse QLoRA-d.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Soovitatud hüperparameetrid ja oodatav täpsus
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

Treeningmeetod | Külmutatud visioonimudel | andmetüüp | LoRA rank | LoRA alpha | partii suurus | õppekiirus | epohhid | Täpsus
--- | --- | --- | --- | --- | --- | --- | --- | --- |
täispeenhäälestamine |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
täispeenhäälestamine | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA tulemused tulekul |  |  |  |  |  |  |  |  |

### MÄRKUS
Allpool olevad DocVQA ja vihkavate meemide tulemused põhinevad eelmisel versioonil (Phi-3-vision). Uued tulemused Phi-3.5-visioniga uuendatakse peagi.

### DocVQA (MÄRKUS: Phi-3-vision)

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

Treeningmeetod | andmetüüp | LoRA rank | LoRA alpha | partii suurus | õppekiirus | epohhid | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
täispeenhäälestamine | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
täispeenhäälestamine | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
külmutatud pildimudel| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
külmutatud pildimudel| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Vihkavad meemid (MÄRKUS: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Treeningmeetod | andmetüüp | LoRA rank | LoRA alpha | partii suurus | õppekiirus | epohhid | Täpsus
--- | --- | --- | --- | --- | --- | --- | --- |
täispeenhäälestamine | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
täispeenhäälestamine | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
külmutatud pildimudel| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
külmutatud pildimudel| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Kiiruse võrdlus (MÄRKUS: Phi-3-vision)

Uued võrdlustulemused Phi-3.5-visioniga uuendatakse peagi.

Kiiruse võrdlus tehti DocVQA andmestikul. Selle andmestiku keskmine järjestuse pikkus on 2443.23 tokenit (kasutades `num_crops=16` pildimudeli jaoks).

### 8x A100-80GB (Ampere)

Treeningmeetod | \# sõlmed | GPU-d | flash attention | Efektiivne partii suurus | Läbilaskevõime (pilt/s) | Kiirendus | Maksimaalne GPU mälu (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
täispeenhäälestamine | 1 | 8 |  | 64 | 5.041 |  1x | ~42
täispeenhäälestamine | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
täispeenhäälestamine | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
täispeenhäälestamine | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
külmutatud pildimudel | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
külmutatud pildimudel | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Treeningmeetod | \# sõlmed | GPU-d | flash attention | Efektiivne partii suurus | Läbilaskevõime (pilt/s) | Kiirendus | Maksimaalne GPU mälu (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
täispeenhäälestamine | 1 | 8 | | 64 | 2.462 |  1x | ~32
täispeenhäälestamine | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
täispeenhäälestamine | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
külmutatud pildimudel | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Tuntud probleemid

- Ei saa käivitada flash attentioni fp16-ga (bf16 on alati soovitatav, kui saadaval, ja kõik GPU-d, mis toetavad flash attentioni, toetavad ka bf16).
- Ei toeta vahepealsete kontrollpunktide salvestamist ja treeningu jätkamist.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.