<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:08:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "sr"
}
-->
# Phi-3.5-vision recept za fino podešavanje

Ovo je zvanična podrška za fino podešavanje Phi-3.5-vision koristeći huggingface biblioteke.  
Pre pokretanja sledećih komandi, molimo vas da `cd` u direktorijum sa kodom [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Instalacija

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

## Brzi početak

Dostavljamo dva primera skripti za fino podešavanje, jedan za DocVQA i jedan za klasifikaciju uvredljivih memova.

Minimalni hardver testiran na 4x RTX8000 (48GB RAM po GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision sada zvanično podržava višeslike kao ulaz. Evo primera za fino podešavanje NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Uputstvo za korišćenje

U zavisnosti od hardvera, korisnici mogu izabrati različite strategije fino podešavanja. Podržavamo  
full-finetuning (sa Deepspeed Zero-2) sa opciono zamrznutim parametrima vida, i LoRA (uključujući 4bit QLoRA).  
Generalno, preporučujemo korišćenje full finetuninga sa flash attention i bf16 kad god je to moguće.

### uputstvo za konvertovanje vašeg prilagođenog skupa podataka u potreban format

Koristimo minimalni video klasifikacioni skup podataka (podskup UCF-101) kao primer od početka do kraja da pokažemo kako da konvertujete svoj prilagođeni skup podataka u potreban format i fino podesite Phi-3.5-vision na njemu.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Konvertovani podaci će izgledati ovako:

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

Za `jsonl` anotaciju, svaki red treba da bude rečnik poput:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Imajte na umu da je `conversations` lista, što znači da je moguće podržati višekratne razgovore ukoliko takvi podaci postoje.

## Zahtev za Azure GPU kvotu

### Preduslovi

Azure nalog sa ulogom Contributor (ili nekom drugom ulogom koja uključuje pristup Contributor).

Ako nemate Azure nalog, napravite [besplatan nalog pre nego što počnete](https://azure.microsoft.com).

### Zahtev za povećanje kvote

Možete poslati zahtev za povećanje kvote direktno iz My quotas. Pratite korake ispod da zatražite povećanje kvote. Za ovaj primer, možete izabrati bilo koju podesivu kvotu u vašoj pretplati.

Prijavite se na [Azure portal](https://portal.azure.com).

Ukucajte "quotas" u polje za pretragu, zatim izaberite Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stranici Overview izaberite provajdera, na primer Compute ili AML.

**Note** Za sve provajdere osim Compute, videćete kolonu Request increase umesto kolone Adjustable opisane dole. Tamo možete zatražiti povećanje određene kvote ili kreirati zahtev za podršku za povećanje.

Na stranici My quotas, pod Quota name, izaberite kvotu koju želite da povećate. Proverite da kolona Adjustable pokazuje Yes za tu kvotu.

Blizu vrha stranice izaberite New Quota Request, zatim Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

U panelu New Quota Request unesite numeričku vrednost za novu granicu kvote, zatim izaberite Submit.

Vaš zahtev će biti pregledan i bićete obavešteni da li je moguće ispuniti zahtev. Ovo obično traje nekoliko minuta.

Ako vaš zahtev nije ispunjen, videćete link za kreiranje zahteva za podršku. Kada koristite taj link, inženjer za podršku će vam pomoći sa vašim zahtevom za povećanje.

## Preporučene SKU mašina sa Azure Compute GPU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Evo nekoliko primera:

### Ako imate A100 ili H100 GPU-ove

Full finetuning obično daje najbolje performanse. Možete koristiti sledeću komandu za fino podešavanje Phi-3-V na klasifikaciji uvredljivih memova.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ako imate Standard_ND40rs_v2 8x V100-32GB GPU-ove

I dalje je moguće u potpunosti fino podesiti Phi-3-V na klasifikaciji uvredljivih memova. Međutim, očekujte  
znatno niži protok u poređenju sa A100 ili H100 GPU-ovima zbog nedostatka podrške za flash attention.  
Preciznost takođe može biti pogođena zbog nedostatka bf16 podrške (koristi se fp16 mešovita preciznost).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ako nemate pristup GPU-ovima u data centru  
LoRA može biti vaš jedini izbor. Možete koristiti sledeću komandu za fino podešavanje Phi-3-V na klasifikaciji uvredljivih memova.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Za Turing+ GPU, QLoRA je podržan

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Preporučeni hiperparametri i očekivana preciznost  
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

Metod treniranja | Zamrznuti model vida | tip podataka | LoRA rank | LoRA alpha | veličina batch-a | stopa učenja | epohe | Preciznost  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA rezultati uskoro |  |  |  |  |  |  |  |  |

### NOTE  
Rezultati za DocVQA i Hateful memes ispod su zasnovani na prethodnoj verziji (Phi-3-vision).  
Novi rezultati sa Phi-3.5-vision biće uskoro ažurirani.

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

Metod treniranja | tip podataka | LoRA rank | LoRA alpha | veličina batch-a | stopa učenja | epohe | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrznuti model slike | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrznuti model slike | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
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

Metod treniranja | tip podataka | LoRA rank | LoRA alpha | veličina batch-a | stopa učenja | epohe | Preciznost  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrznuti model slike | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrznuti model slike | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmark brzine (NOTE: Phi-3-vision)

Novi rezultati benchmarka sa Phi-3.5-vision biće uskoro ažurirani.

Benchmark brzine je urađen na DocVQA skupu podataka. Prosečna dužina sekvence ovog skupa  
je 2443.23 tokena (koristeći `num_crops=16` za model slike).

### 8x A100-80GB (Ampere)

Metod treniranja | \# čvorova | GPU-ova | flash attention | Efektivna veličina batch-a | Protok (slika/s) | Ubrzanje | Maksimalna GPU memorija (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrznuti model slike | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrznuti model slike | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Metod treniranja | \# čvorova | GPU-ova | flash attention | Efektivna veličina batch-a | Protok (slika/s) | Ubrzanje | Maksimalna GPU memorija (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrznuti model slike | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Poznati problemi

- Ne može se koristiti flash attention sa fp16 (bf16 se uvek preporučuje kada je dostupan, a svi GPU-ovi koji podržavaju flash attention takođe podržavaju bf16).  
- Još uvek nije podržano čuvanje privremenih checkpoint-a i nastavljanje treniranja.

**Ограничење одговорности**:  
Овај документ је преведен помоћу AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.