# Phi-3.5-vision recept za fino nastavljanje

To je uradna podpora za fino nastavljanje Phi-3.5-vision z uporabo knjižnic huggingface.  
Pred zagonom naslednjih ukazov se prosim premaknite v imenik s kodo [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Namestitev

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

## Hiter začetek

Ponujamo dva primerna skripta za fino nastavljanje, enega za DocVQA in enega za klasifikacijo sovražnih memov.

Minimalna testirana strojna oprema: 4x RTX8000 (48GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision sedaj uradno podpira več slik kot vhod. Tukaj je primer za fino nastavljanje NLVR2.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Navodila za uporabo

Glede na strojno opremo lahko uporabniki izberejo različne strategije fino nastavljanja. Podpiramo  
polno fino nastavljanje (z Deepspeed Zero-2) z opcijsko zamrznjenimi parametri vida, ter LoRA (vključno s 4bit QLoRA).  
Na splošno priporočamo uporabo polnega fino nastavljanja z flash attention in bf16, kadar je to mogoče.

### Navodila za pretvorbo lastnega nabora podatkov v zahtevan format

Kot primer od začetka do konca uporabljamo minimalni video klasifikacijski nabor podatkov (podnabor UCF-101), da pokažemo, kako pretvoriti svoj nabor podatkov v zahtevan format in na njem fino nastaviti Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Pretvorjeni podatki bodo izgledali takole:

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

Za `jsonl` anotacijo naj bo vsaka vrstica slovar, kot je:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Upoštevajte, da je `conversations` seznam, zato je podprta tudi večkratna izmenjava pogovora, če so takšni podatki na voljo.

## Zahteva za Azure GPU kvoto

### Predpogoji

Azure račun z vlogo Contributor (ali drugo vlogo, ki vključuje dostop Contributor).

Če še nimate Azure računa, si ustvarite [brezplačen račun pred začetkom](https://azure.microsoft.com).

### Zahteva za povečanje kvote

Zahtevo za povečanje kvote lahko oddate neposredno iz My quotas. Sledite spodnjim korakom za zahtevo povečanja kvote. Za ta primer lahko izberete katerokoli prilagodljivo kvoto v svoji naročnini.

Prijavite se v [Azure portal](https://portal.azure.com).

V iskalno polje vpišite "quotas" in izberite Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na strani Overview izberite ponudnika, na primer Compute ali AML.

**Opomba** Za vse ponudnike razen Compute boste videli stolpec Request increase namesto stolpca Adjustable, kot je opisano spodaj. Tam lahko zahtevate povečanje določene kvote ali ustvarite podporno zahtevo za povečanje.

Na strani My quotas pod Quota name izberite kvoto, ki jo želite povečati. Prepričajte se, da stolpec Adjustable za to kvoto prikazuje Da.

Na vrhu strani izberite New Quota Request, nato Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

V oknu New Quota Request vnesite številčno vrednost za novo omejitev kvote in izberite Submit.

Vaša zahteva bo pregledana in obveščeni boste, če je mogoče zahtevo izpolniti. To običajno traja nekaj minut.

Če zahteva ni izpolnjena, boste videli povezavo za ustvarjanje podporne zahteve. Ko uporabite to povezavo, vam bo podporni inženir pomagal pri vaši zahtevi za povečanje.

## Priporočene SKU za Azure Compute GPU stroje

[ND A100 v4-serija](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serija](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Tukaj je nekaj primerov:

### Če imate A100 ali H100 GPU-je

Polno fino nastavljanje običajno prinese najboljše rezultate. Za fino nastavljanje Phi-3-V na klasifikacijo sovražnih memov lahko uporabite naslednji ukaz.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Če imate Standard_ND40rs_v2 8x V100-32GB GPU-je

Še vedno je mogoče popolnoma fino nastaviti Phi-3-V na klasifikacijo sovražnih memov. Vendar pričakujte  
much nižjo prepustnost v primerjavi z A100 ali H100 GPU-ji zaradi pomanjkanja podpore za flash attention.  
Natančnost je lahko prav tako prizadeta zaradi pomanjkanja podpore za bf16 (namesto tega se uporablja fp16 mešano natančnost).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Če nimate dostopa do GPU-jev v podatkovnem centru

LoRA je morda vaša edina možnost. Za fino nastavljanje Phi-3-V na klasifikacijo sovražnih memov lahko uporabite naslednji ukaz.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Za Turing+ GPU-je je podprt QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Priporočeni hiperparametri in pričakovana natančnost

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

Metoda učenja | Zamrznjen model vida | tip podatkov | LoRA rang | LoRA alfa | velikost serije | hitrost učenja | epoh | Natančnost  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Rezultati LoRA kmalu |  |  |  |  |  |  |  |  |

### OPOMBA  
Spodnji rezultati za DocVQA in sovražne meme temeljijo na prejšnji različici (Phi-3-vision).  
Novi rezultati s Phi-3.5-vision bodo kmalu posodobljeni.

### DocVQA (OPOMBA: Phi-3-vision)

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

Metoda učenja | tip podatkov | LoRA rang | LoRA alfa | velikost serije | hitrost učenja | epoh | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrznjen model slike | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrznjen model slike | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Sovražni memi (OPOMBA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda učenja | tip podatkov | LoRA rang | LoRA alfa | velikost serije | hitrost učenja | epoh | Natančnost  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrznjen model slike | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrznjen model slike | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Merjenje hitrosti (OPOMBA: Phi-3-vision)

Novi rezultati merjenja hitrosti s Phi-3.5-vision bodo kmalu posodobljeni.

Merjenje hitrosti je izvedeno na naboru podatkov DocVQA. Povprečna dolžina sekvence tega nabora je  
2443.23 tokenov (uporabljen `num_crops=16` za slikovni model).

### 8x A100-80GB (Ampere)

Metoda učenja | \# vozlišč | GPU-ji | flash attention | Učinkovita velikost serije | Prepustnost (slik/s) | Pospešek | Največji pomnilnik GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrznjen model slike | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrznjen model slike | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Metoda učenja | \# vozlišč | GPU-ji | flash attention | Učinkovita velikost serije | Prepustnost (slik/s) | Pospešek | Največji pomnilnik GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrznjen model slike | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Znane težave

- Flash attention ni mogoče zagnati z fp16 (bf16 je vedno priporočljiv, kadar je na voljo, in vsi GPU-ji, ki podpirajo flash attention, podpirajo tudi bf16).  
- Trenutno ni podprto shranjevanje vmesnih kontrolnih točk in nadaljevanje učenja.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.