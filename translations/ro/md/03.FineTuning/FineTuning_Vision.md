<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:54:47+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ro"
}
-->
# Rețetă de finetuning Phi-3.5-vision

Aceasta este suportul oficial pentru finetuning-ul Phi-3.5-vision folosind bibliotecile huggingface.  
Vă rugăm să faceți `cd` în directorul de cod [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) înainte de a rula comenzile următoare.

## Instalare

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

## Pornire rapidă

Oferim două scripturi exemplu pentru finetuning, unul pentru DocVQA și unul pentru clasificarea meme-urilor urâte.

Hardware minim testat: 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision suportă acum oficial inputuri cu mai multe imagini. Iată un exemplu pentru finetuning NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Ghid de utilizare

În funcție de hardware, utilizatorii pot alege diferite strategii de finetuning. Suportăm  
full-finetuning (cu Deepspeed Zero-2) cu parametri de viziune opțional înghețați, și LoRA (inclusiv QLoRA pe 4 biți).  
În general, recomandăm folosirea full finetuning cu flash attention și bf16 ori de câte ori este posibil.

### Ghid pentru convertirea dataset-ului personal în formatul cerut

Folosim un dataset minim de clasificare video (un subset din UCF-101) ca exemplu complet pentru a demonstra cum să convertiți dataset-ul personal în formatul cerut și să faceți finetuning pe Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Datele convertite vor arăta astfel:

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

Pentru adnotarea `jsonl`, fiecare linie trebuie să fie un dicționar de forma:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Rețineți că `conversations` este o listă, deci conversațiile cu mai multe runde pot fi suportate dacă astfel de date sunt disponibile.

## Solicitarea cotei GPU Azure

### Cerințe preliminare

Un cont Azure cu rolul Contributor (sau alt rol care include acces Contributor).

Dacă nu aveți un cont Azure, creați un [cont gratuit înainte de a începe](https://azure.microsoft.com).

### Solicitarea unei creșteri a cotei

Puteți trimite o cerere de creștere a cotei direct din My quotas. Urmați pașii de mai jos pentru a solicita o creștere a unei cote. Pentru acest exemplu, puteți selecta orice cotă ajustabilă din abonamentul dvs.

Conectați-vă la [portalul Azure](https://portal.azure.com).

Introduceți „quotas” în caseta de căutare, apoi selectați Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Pe pagina Overview, selectați un furnizor, cum ar fi Compute sau AML.

**Note** Pentru toți furnizorii în afară de Compute, veți vedea o coloană Request increase în loc de coloana Adjustable descrisă mai jos. Acolo puteți solicita o creștere pentru o cotă specifică sau puteți crea o cerere de suport pentru creștere.

Pe pagina My quotas, sub Quota name, selectați cota pe care doriți să o măriți. Asigurați-vă că în coloana Adjustable apare Yes pentru această cotă.

În partea de sus a paginii, selectați New Quota Request, apoi selectați Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

În panoul New Quota Request, introduceți o valoare numerică pentru noul dvs. limită de cotă, apoi selectați Submit.

Cererea dvs. va fi revizuită și veți fi notificat dacă poate fi aprobată. De obicei, acest lucru se întâmplă în câteva minute.

Dacă cererea nu este aprobată, veți vedea un link pentru a crea o cerere de suport. Folosind acest link, un inginer de suport vă va ajuta cu solicitarea de creștere.

## Sugestii pentru SKU-uri mașini GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Iată câteva exemple:

### Dacă aveți GPU-uri A100 sau H100

Full finetuning oferă de obicei cea mai bună performanță. Puteți folosi comanda următoare pentru a face finetuning pe Phi-3-V pentru clasificarea meme-urilor urâte.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Dacă aveți Standard_ND40rs_v2 cu 8x V100-32GB GPU-uri

Este totuși posibil să faceți full finetuning pe Phi-3-V pentru clasificarea meme-urilor urâte. Totuși, așteptați-vă la un throughput mult mai mic comparativ cu GPU-urile A100 sau H100 din cauza lipsei suportului pentru flash attention.  
Acuratețea poate fi de asemenea afectată din cauza lipsei suportului bf16 (se folosește antrenament cu precizie mixtă fp16 în schimb).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Dacă nu aveți acces la GPU-uri din centre de date

LoRA ar putea fi singura opțiune. Puteți folosi comanda următoare pentru a face finetuning pe Phi-3-V pentru clasificarea meme-urilor urâte.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pentru GPU-uri Turing+ este suportat QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hiperparametri sugerați și acuratețe așteptată

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

Metoda de antrenament | Model de viziune înghețat | tip date | rang LoRA | alpha LoRA | dimensiune batch | rată învățare | epoci | Acuratețe
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Rezultate LoRA în curând |  |  |  |  |  |  |  |  |

### NOTE  
Rezultatele de mai jos pentru DocVQA și Hateful memes sunt bazate pe versiunea anterioară (Phi-3-vision).  
Noile rezultate cu Phi-3.5-vision vor fi actualizate în curând.

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

Metoda de antrenament | tip date | rang LoRA | alpha LoRA | dimensiune batch | rată învățare | epoci | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
model imagine înghețat | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
model imagine înghețat | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Metoda de antrenament | tip date | rang LoRA | alpha LoRA | dimensiune batch | rată învățare | epoci | Acuratețe
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
model imagine înghețat | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
model imagine înghețat | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmark de viteză (NOTE: Phi-3-vision)

Noile rezultate de benchmark cu Phi-3.5-vision vor fi actualizate în curând.

Benchmark-ul de viteză este realizat pe dataset-ul DocVQA. Lungimea medie a secvenței în acest dataset  
este de 2443.23 tokeni (folosind `num_crops=16` pentru modelul de imagini).

### 8x A100-80GB (Ampere)

Metoda de antrenament | \# noduri | GPU-uri | flash attention | Dimensiune batch efectivă | Throughput (img/s) | Accelerare | Memorie GPU maximă (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
model imagine înghețat | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
model imagine înghețat | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Metoda de antrenament | \# noduri | GPU-uri | flash attention | Dimensiune batch efectivă | Throughput (img/s) | Accelerare | Memorie GPU maximă (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
model imagine înghețat | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Probleme cunoscute

- Nu se poate rula flash attention cu fp16 (bf16 este întotdeauna recomandat când este disponibil, iar toate GPU-urile care suportă flash attention suportă și bf16).  
- Nu se suportă încă salvarea checkpoint-urilor intermediare și reluarea antrenamentului.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.