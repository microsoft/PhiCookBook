# Phi-3.5-vision pritaikymo receptas

Tai oficiali Phi-3.5-vision pritaikymo palaikymo dokumentacija, naudojant huggingface bibliotekas. Prieš vykdydami šiuos komandas, pereikite į kodų katalogą [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Įdiegimas

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

## Greitas startas

Pateikiame du pritaikymo scenarijų pavyzdžius: vieną DocVQA ir kitą neapykantos memų klasifikavimui.

Minimalūs techninės įrangos reikalavimai: 4x RTX8000 (48GB RAM kiekvienai GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision dabar oficialiai palaiko kelių vaizdų įvestis. Štai NLVR2 pritaikymo pavyzdys:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Naudojimo vadovas

Priklausomai nuo techninės įrangos, vartotojai gali pasirinkti skirtingas pritaikymo strategijas. Palaikome pilną pritaikymą (su Deepspeed Zero-2), galimai užšaldant vaizdo parametrus, ir LoRA (įskaitant 4bit QLoRA). Paprastai rekomenduojame naudoti pilną pritaikymą su flash attention ir bf16, kai tik įmanoma.

### Vadovas, kaip konvertuoti savo pasirinktą duomenų rinkinį į reikiamą formatą

Naudojame minimalų vaizdo klasifikavimo duomenų rinkinį (UCF-101 dalį) kaip pavyzdį, kad parodytume, kaip konvertuoti savo duomenų rinkinį į reikiamą formatą ir pritaikyti Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Konvertuoti duomenys atrodys taip:

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

`jsonl` anotacijoje kiekviena eilutė turėtų būti žodynas, pavyzdžiui:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Atkreipkite dėmesį, kad `conversations` yra sąrašas, todėl galima palaikyti daugiapakopį pokalbį, jei tokie duomenys yra prieinami.

## Azure GPU kvotos prašymas

### Būtinos sąlygos

Azure paskyra su Contributor vaidmeniu (arba kitu vaidmeniu, kuris apima Contributor prieigą).

Jei neturite Azure paskyros, sukurkite [nemokamą paskyrą prieš pradėdami](https://azure.microsoft.com).

### Kvotos padidinimo prašymas

Kvotos padidinimo prašymą galite pateikti tiesiogiai iš My quotas. Sekite žemiau pateiktus veiksmus, kad pateiktumėte prašymą padidinti kvotą. Šiame pavyzdyje galite pasirinkti bet kurią reguliuojamą kvotą savo prenumeratoje.

Prisijunkite prie [Azure portalo](https://portal.azure.com).

Įveskite „quotas“ paieškos laukelyje ir pasirinkite Quotas.
![Kvota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Pagrindiniame puslapyje pasirinkite tiekėją, pvz., Compute arba AML.

**Pastaba** Visuose tiekėjuose, išskyrus Compute, matysite Request increase stulpelį, o ne Adjustable stulpelį, aprašytą žemiau. Ten galite prašyti padidinti konkrečią kvotą arba sukurti palaikymo prašymą dėl padidinimo.

My quotas puslapyje, po Quota name, pasirinkite kvotą, kurią norite padidinti. Įsitikinkite, kad Adjustable stulpelyje rodoma Yes šiai kvotai.

Puslapio viršuje pasirinkite New Quota Request, tada Enter a new limit.

![Padidinti kvotą](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Naujame Quota Request lange įveskite skaitinę vertę savo naujai kvotos ribai, tada pasirinkite Submit.

Jūsų prašymas bus peržiūrėtas, ir jūs būsite informuoti, ar prašymas gali būti patenkintas. Tai paprastai įvyksta per kelias minutes.

Jei jūsų prašymas nebus patenkintas, matysite nuorodą sukurti palaikymo prašymą. Naudodami šią nuorodą, palaikymo inžinierius padės jums su padidinimo prašymu.

## Azure Compute GPU mašinų SKU pasiūlymai

[ND A100 v4-serija](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serija](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Štai keletas pavyzdžių:

### Jei turite A100 arba H100 GPU

Pilnas pritaikymas paprastai suteikia geriausią našumą. Galite naudoti šią komandą pritaikyti Phi-3-V neapykantos memų klasifikavimui.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Jei turite Standard_ND40rs_v2 8x V100-32GB GPU

Vis dar įmanoma pilnai pritaikyti Phi-3-V neapykantos memų klasifikavimui. Tačiau tikėkitės daug mažesnio našumo, palyginti su A100 ar H100 GPU, dėl flash attention palaikymo trūkumo. Tikslumas taip pat gali būti paveiktas dėl bf16 palaikymo trūkumo (vietoj to naudojamas fp16 mišrios precizijos mokymas).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Jei neturite prieigos prie duomenų centro GPU
Lora gali būti jūsų vienintelis pasirinkimas. Galite naudoti šią komandą pritaikyti Phi-3-V neapykantos memų klasifikavimui.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU atveju palaikomas QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Rekomenduojami hiperparametrai ir tikėtinas tikslumas
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

Mokymo metodas | Užšaldytas vaizdo modelis | duomenų tipas | LoRA rangas | LoRA alfa | partijos dydis | mokymosi greitis | epochos | Tikslumas
--- | --- | --- | --- | --- | --- | --- | --- | --- |
pilnas pritaikymas |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
pilnas pritaikymas | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA rezultatai netrukus |  |  |  |  |  |  |  |  |

### PASTABA
Žemiau pateikti DocVQA ir neapykantos memų rezultatai yra pagrįsti ankstesne versija (Phi-3-vision).
Nauji rezultatai su Phi-3.5-vision bus atnaujinti netrukus.

### DocVQA (PASTABA: Phi-3-vision)

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

Mokymo metodas | duomenų tipas | LoRA rangas | LoRA alfa | partijos dydis | mokymosi greitis | epochos | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
pilnas pritaikymas | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
pilnas pritaikymas | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
užšaldytas vaizdo modelis| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
užšaldytas vaizdo modelis| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Neapykantos memai (PASTABA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Mokymo metodas | duomenų tipas | LoRA rangas | LoRA alfa | partijos dydis | mokymosi greitis | epochos | Tikslumas
--- | --- | --- | --- | --- | --- | --- | --- |
pilnas pritaikymas | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
pilnas pritaikymas | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
užšaldytas vaizdo modelis| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
užšaldytas vaizdo modelis| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Greičio testavimas (PASTABA: Phi-3-vision)

Nauji greičio testavimo rezultatai su Phi-3.5-vision bus atnaujinti netrukus.

Greitis testuojamas naudojant DocVQA duomenų rinkinį. Vidutinis šio duomenų rinkinio sekos ilgis yra 2443.23 žodžių (naudojant `num_crops=16` vaizdo modeliui).

### 8x A100-80GB (Ampere)

Mokymo metodas | \# mazgų | GPU | flash attention | Efektyvus partijos dydis | Perduodamumas (vaizdai/s) | Greičio padidėjimas | Maksimali GPU atmintis (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
pilnas pritaikymas | 1 | 8 |  | 64 | 5.041 |  1x | ~42
pilnas pritaikymas | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
pilnas pritaikymas | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
pilnas pritaikymas | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
užšaldytas vaizdo modelis | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
užšaldytas vaizdo modelis | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Mokymo metodas | \# mazgų | GPU | flash attention | Efektyvus partijos dydis | Perduodamumas (vaizdai/s) | Greičio padidėjimas | Maksimali GPU atmintis (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
pilnas pritaikymas | 1 | 8 | | 64 | 2.462 |  1x | ~32
pilnas pritaikymas | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
pilnas pritaikymas | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
užšaldytas vaizdo modelis | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Žinomos problemos

- Negalima vykdyti flash attention su fp16 (bf16 visada rekomenduojamas, kai tik įmanoma, ir visi GPU, palaikantys flash attention, taip pat palaiko bf16).
- Dar nepalaikomas tarpinių kontrolinių taškų išsaugojimas ir mokymo tęstinumas.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.