<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:03:27+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "fi"
}
-->
# Phi-3.5-vision hienosäätöohje

Tämä on virallinen tuki Phi-3.5-vision hienosäädölle käyttäen huggingface-kirjastoja.  
Siirry `cd` koodihakemistoon [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ennen seuraavien komentojen suorittamista.

## Asennus

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

## Nopeasti käyntiin

Tarjoamme kaksi esimerkkiskriptiä hienosäätöön, yhden DocVQA:lle ja toisen vihamielisten meemien luokitteluun.

Minimilaitevaatimukset testattu 4x RTX8000 (48GB RAMia per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision tukee nyt virallisesti monikuvasyötteitä. Tässä esimerkki NLVR2:n hienosäädöstä

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Käyttöopas

Laitteistosta riippuen käyttäjät voivat valita eri hienosäätöstrategioita. Tuemme  
kokonaisvaltaista hienosäätöä (Deepspeed Zero-2:lla) ja valinnaisesti lukittuja visuaalisia parametreja sekä LoRA:ta (mukaan lukien 4bit QLoRA).  
Yleisesti suosittelemme käyttämään täyttä hienosäätöä flash attentionilla ja bf16:lla aina kun mahdollista.

### Opas oman datasetin muuntamiseen vaadittuun muotoon

Käytämme minimivideoluokitteludatasettiä (osa UCF-101:stä) esimerkkinä, joka näyttää miten muuntaa oma datasetti vaadittuun muotoon ja hienosäätää Phi-3.5-vision sitä vasten.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Muunnettu data näyttää tältä:

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

`jsonl`-annotaatiossa jokainen rivi on sanakirja, esimerkiksi:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Huomaa, että `conversations` on lista, joten monikierroksiset keskustelut ovat tuettuja, jos tällaisia tietoja on saatavilla.

## Azure GPU -kiintiön pyytäminen

### Esivaatimukset

Azure-tili, jolla on Contributor-rooli (tai muu rooli, johon sisältyy Contributor-oikeudet).

Jos sinulla ei ole Azure-tiliä, luo [ilmainen tili ennen aloittamista](https://azure.microsoft.com).

### Pyydä kiintiön korotusta

Voit lähettää pyynnön kiintiön korotuksesta suoraan My quotas -kohdasta. Seuraa alla olevia ohjeita pyytääksesi korotusta kiintiölle. Tässä esimerkissä voit valita minkä tahansa säädettävissä olevan kiintiön tilauksessasi.

Kirjaudu sisään [Azure-portaaliin](https://portal.azure.com).

Kirjoita hakukenttään "quotas" ja valitse Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Yleiskatsaus-sivulla valitse palveluntarjoaja, kuten Compute tai AML.

**Note** Muilla palveluntarjoajilla kuin Compute, näet Request increase -sarakkeen Adjustable-sarakkeen sijaan. Sieltä voit pyytää korotusta tietylle kiintiölle tai luoda tukipyynnön korotukselle.

My quotas -sivulla, Quota name -kohdasta valitse kiintiö, jota haluat korottaa. Varmista, että Adjustable-sarakkeessa lukee Yes kyseiselle kiintiölle.

Sivun yläosassa valitse New Quota Request ja sitten Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request -paneelissa syötä numeerinen arvo uudelle kiintiörajoituksellesi ja valitse Submit.

Pyyntösi tarkistetaan, ja saat ilmoituksen, jos pyyntö voidaan toteuttaa. Tämä tapahtuu yleensä muutaman minuutin sisällä.

Jos pyyntöä ei toteuteta, näet linkin tukipyynnön luomiseen. Käyttämällä tätä linkkiä tukihenkilö auttaa sinua kiintiön korotuspyynnössä.

## Azure Compute GPU -koneiden SKU-suositukset

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Tässä joitakin esimerkkejä:

### Jos sinulla on A100- tai H100-GPU:t

Täysi hienosäätö tarjoaa yleensä parhaan suorituskyvyn. Voit käyttää seuraavaa komentoa hienosäätääksesi Phi-3-V:tä vihamielisten meemien luokittelussa.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Jos sinulla on Standard_ND40rs_v2 8x V100-32GB GPU:t

Phi-3-V:n täydellinen hienosäätö vihamielisten meemien luokitteluun on edelleen mahdollista. Odota kuitenkin huomattavasti pienempää läpimenomäärää verrattuna A100- tai H100-GPU:ihin flash attention -tuesta johtuen.  
Myös tarkkuus voi heikentyä bf16-tuen puutteen vuoksi (käytössä on fp16 mixed-precision -koulutus).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Jos sinulla ei ole pääsyä datakeskuksen GPU:ihin

LoRA voi olla ainoa vaihtoehtosi. Voit käyttää seuraavaa komentoa hienosäätääksesi Phi-3-V:tä vihamielisten meemien luokittelussa.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU:lle QLoRA on tuettu

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Suositellut hyperparametrit ja odotettu tarkkuus

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

Koulutusmenetelmä | Lukittu visuaalimalli | tietotyyppi | LoRA rank | LoRA alpha | eräkoko | oppimisnopeus | epochit | Tarkkuus
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA-tulokset tulossa pian |  |  |  |  |  |  |  |  |

### NOTE  
Alla olevat DocVQA- ja Hateful memes -tulokset perustuvat aiempaan versioon (Phi-3-vision).  
Uudet tulokset Phi-3.5-visionilla päivittyvät pian.

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

Koulutusmenetelmä | tietotyyppi | LoRA rank | LoRA alpha | eräkoko | oppimisnopeus | epochit | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
lukittu kuvamalli | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
lukittu kuvamalli | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Koulutusmenetelmä | tietotyyppi | LoRA rank | LoRA alpha | eräkoko | oppimisnopeus | epochit | Tarkkuus
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
lukittu kuvamalli | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
lukittu kuvamalli | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Nopeustestaus (NOTE: Phi-3-vision)

Uudet nopeustestitulokset Phi-3.5-visionilla päivittyvät pian.

Nopeustestaus on tehty DocVQA-datasetillä. Datasetin keskimääräinen sekvenssin pituus on 2443.23 tokenia (käyttäen `num_crops=16` kuvamallille).

### 8x A100-80GB (Ampere)

Koulutusmenetelmä | \# solmuja | GPU:t | flash attention | Tehokas eräkoko | Läpäisy (kuvaa/s) | Nopeutus | Huippu GPU-muisti (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
lukittu kuvamalli | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
lukittu kuvamalli | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Koulutusmenetelmä | \# solmuja | GPU:t | flash attention | Tehokas eräkoko | Läpäisy (kuvaa/s) | Nopeutus | Huippu GPU-muisti (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
lukittu kuvamalli | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Tunnetut ongelmat

- Flash attentionia ei voi käyttää fp16:lla (bf16 on aina suositeltavaa, ja kaikki flash attentionia tukevat GPU:t tukevat myös bf16:ta).
- Välitallennusten tallentamista ja koulutuksen jatkamista ei vielä tueta.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.