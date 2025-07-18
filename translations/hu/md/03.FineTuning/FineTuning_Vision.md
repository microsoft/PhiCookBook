<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:52:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "hu"
}
-->
# Phi-3.5-vision finomhangolási recept

Ez a hivatalos támogatás a Phi-3.5-vision finomhangolásához a huggingface könyvtárak használatával.  
Kérjük, futtatás előtt lépj be a kód könyvtárba: [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Telepítés

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

## Gyors kezdés

Két példa finomhangolási szkriptet biztosítunk, egyet a DocVQA-hoz és egyet a gyűlöletkeltő mémek osztályozásához.

Minimálisan tesztelt hardver: 4x RTX8000 (48GB RAM GPU-nként)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

A Phi-3.5-vision most már hivatalosan támogatja a többkép-bemeneteket is. Íme egy példa az NLVR2 finomhangolására.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Használati útmutató

A hardvertől függően a felhasználók különböző finomhangolási stratégiákat választhatnak. Támogatjuk a  
teljes finomhangolást (Deepspeed Zero-2-vel), opcionálisan lefagyasztott látási paraméterekkel, valamint a LoRA-t (beleértve a 4bit QLoRA-t is).  
Általánosságban javasoljuk a teljes finomhangolás használatát flash attention-nel és bf16-tal, amikor csak lehetséges.

### Útmutató egyedi adatkészleted átalakításához a szükséges formátumra

Egy minimális videóosztályozó adatkészletet (az UCF-101 egy részhalmazát) használunk végponttól végpontig példaként, hogy bemutassuk, hogyan alakíthatod át az egyedi adatkészleted a szükséges formátumra, és hogyan finomhangolhatod rajta a Phi-3.5-vision-t.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Az átalakított adatok így fognak kinézni:

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

A `jsonl` annotáció esetén minden sor egy szótár legyen, például:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Fontos megjegyezni, hogy a `conversations` egy lista, így többfordulós beszélgetések is támogatottak, ha ilyen adatok rendelkezésre állnak.

## Azure GPU kvóta igénylése

### Előfeltételek

Egy Azure fiók, amely rendelkezik Contributor szerepkörrel (vagy más, Contributor hozzáférést tartalmazó szerepkörrel).

Ha még nincs Azure fiókod, hozz létre egy [ingyenes fiókot a kezdés előtt](https://azure.microsoft.com).

### Kvóta növelés igénylése

Kvóta növelési kérelmet közvetlenül a My quotas felületről is beadhatsz. Az alábbi lépéseket követve kérhetsz növelést egy kvótára. Ebben a példában bármelyik állítható kvótát kiválaszthatod az előfizetésedben.

Jelentkezz be az [Azure portálra](https://portal.azure.com).

Írd be a keresőmezőbe, hogy "quotas", majd válaszd a Quotas menüpontot.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Az Áttekintő oldalon válassz egy szolgáltatót, például Compute vagy AML.

**Megjegyzés:** Minden más szolgáltatónál, mint a Compute, a Request increase oszlopot fogod látni az Adjustable oszlop helyett. Itt kérhetsz növelést egy adott kvótára, vagy létrehozhatsz támogatási kérelmet a növeléshez.

A My quotas oldalon, a Quota name alatt válaszd ki a növelni kívánt kvótát. Győződj meg róla, hogy az Adjustable oszlopban Igen szerepel ennél a kvótánál.

Az oldal tetején válaszd az Új kvóta kérelem (New Quota Request) lehetőséget, majd az Új limit megadása (Enter a new limit) opciót.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Az Új kvóta kérelem panelen add meg az új kvóta limit numerikus értékét, majd kattints a Beküldésre (Submit).

A kérelmedet felülvizsgálják, és értesítenek, ha teljesíthető. Ez általában néhány percen belül megtörténik.

Ha a kérelmed nem teljesül, egy linket fogsz látni támogatási kérelem létrehozásához. Ezen keresztül egy támogatási mérnök segít a növelési igényedben.

## Azure Compute GPU gép SKU javaslatok

[ND A100 v4-sorozat](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-sorozat](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Íme néhány példa:

### Ha A100 vagy H100 GPU-d van

A teljes finomhangolás általában a legjobb teljesítményt nyújtja. Az alábbi parancs segítségével finomhangolhatod a Phi-3-V-t a gyűlöletkeltő mémek osztályozására.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ha Standard_ND40rs_v2 8x V100-32GB GPU-d van

Még mindig lehetséges a Phi-3-V teljes finomhangolása gyűlöletkeltő mémek osztályozására. Azonban számíts jóval alacsonyabb áteresztőképességre az A100 vagy H100 GPU-khoz képest a flash attention támogatás hiánya miatt.  
A pontosság is csökkenhet a bf16 támogatás hiánya miatt (helyette fp16 kevert precizitású tréninget használnak).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ha nincs hozzáférésed adatközponti GPU-khoz

A LoRA lehet az egyetlen választásod. Az alábbi parancs segítségével finomhangolhatod a Phi-3-V-t a gyűlöletkeltő mémek osztályozására.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU-k esetén a QLoRA támogatott.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Javasolt hiperparaméterek és várható pontosság

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

Tréning módszer | Lefagyasztott látási modell | adattípus | LoRA rang | LoRA alfa | batch méret | tanulási ráta | epochok | Pontosság  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA eredmények hamarosan |  |  |  |  |  |  |  |  |

### MEGJEGYZÉS  
Az alábbi DocVQA és Gyűlöletkeltő mémek eredmények a korábbi verzióra (Phi-3-vision) vonatkoznak.  
Az új eredmények a Phi-3.5-vision-nal hamarosan frissülnek.

### DocVQA (MEGJEGYZÉS: Phi-3-vision)

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

Tréning módszer | adattípus | LoRA rang | LoRA alfa | batch méret | tanulási ráta | epochok | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
lefagyasztott képi modell | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
lefagyasztott képi modell | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Gyűlöletkeltő mémek (MEGJEGYZÉS: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Tréning módszer | adattípus | LoRA rang | LoRA alfa | batch méret | tanulási ráta | epochok | Pontosság  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
lefagyasztott képi modell | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
lefagyasztott képi modell | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Sebességteszt (MEGJEGYZÉS: Phi-3-vision)

Az új sebességtesztek eredményei a Phi-3.5-vision-nal hamarosan elérhetők lesznek.

A sebességteszt a DocVQA adatkészleten történt. Ennek az adatkészletnek az átlagos szekvencia hossza 2443.23 token (a képi modellhez `num_crops=16` használatával).

### 8x A100-80GB (Ampere)

Tréning módszer | \# csomópont | GPU-k | flash attention | Effektív batch méret | Áteresztőképesség (kép/s) | Gyorsulás | Maximális GPU memória (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42 |  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 |  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 |  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 |  
lefagyasztott képi modell | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29 |  
lefagyasztott képi modell | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 |  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50 |  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 |  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32 |  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 |

### 8x V100-32GB (Volta)

Tréning módszer | \# csomópont | GPU-k | flash attention | Effektív batch méret | Áteresztőképesség (kép/s) | Gyorsulás | Maximális GPU memória (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32 |  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32 |  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32 |  
lefagyasztott képi modell | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27 |  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30 |

## Ismert problémák

- Nem futtatható flash attention fp16-tal (bf16 használata mindig ajánlott, ha elérhető, és minden flash attention-t támogató GPU támogatja a bf16-ot is).  
- Jelenleg nem támogatott a köztes ellenőrzőpontok mentése és a tréning folytatása.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.