# Phi-3.5-vision recept na doladění

Toto je oficiální podpora doladění Phi-3.5-vision pomocí knihoven huggingface.  
Před spuštěním následujících příkazů prosím přejděte do adresáře s kódem [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Instalace

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

## Rychlý start

Poskytujeme dva příkladové skripty pro doladění, jeden pro DocVQA a druhý pro klasifikaci nenávistných memů.

Minimální testovaný hardware: 4x RTX8000 (48GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision nyní oficiálně podporuje vstupy s více obrázky. Zde je příklad doladění na NLVR2.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Průvodce použitím

V závislosti na hardwaru si uživatelé mohou zvolit různé strategie doladění. Podporujeme  
full-finetuning (s Deepspeed Zero-2) s volitelně zamrzlými parametry vidění a LoRA (včetně 4bit QLoRA).  
Obecně doporučujeme používat full finetuning s flash attention a bf16, kdykoli je to možné.

### Průvodce převodem vlastního datasetu do požadovaného formátu

Používáme minimální dataset pro klasifikaci videa (podmnožina UCF-101) jako příklad end-to-end, který ukazuje, jak převést vlastní dataset do požadovaného formátu a doladit na něm Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Převedená data budou vypadat takto:

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

Pro anotaci ve formátu `jsonl` by měl být každý řádek slovník ve tvaru:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Všimněte si, že `conversations` je seznam, takže je možné podporovat vícetahové konverzace, pokud jsou taková data k dispozici.

## Žádost o kvótu GPU na Azure

### Požadavky

Účet Azure s rolí Contributor (nebo jinou rolí, která zahrnuje přístup Contributor).

Pokud účet Azure nemáte, vytvořte si [zdarma účet před začátkem](https://azure.microsoft.com).

### Žádost o zvýšení kvóty

Žádost o zvýšení kvóty můžete podat přímo v sekci My quotas. Postupujte podle níže uvedených kroků pro žádost o zvýšení kvóty. Pro tento příklad můžete vybrat jakoukoli upravitelnou kvótu ve vaší předplatném.

Přihlaste se do [Azure portálu](https://portal.azure.com).

Do vyhledávacího pole zadejte „quotas“ a poté vyberte Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stránce Přehled vyberte poskytovatele, například Compute nebo AML.

**Poznámka** Pro všechny poskytovatele kromě Compute uvidíte sloupec Request increase místo sloupce Adjustable, jak je popsáno níže. Tam můžete požádat o zvýšení konkrétní kvóty nebo vytvořit podporu žádosti o zvýšení.

Na stránce My quotas vyberte pod názvem kvóty tu, kterou chcete zvýšit. Ujistěte se, že ve sloupci Adjustable je u této kvóty uvedeno Yes.

Nahoře na stránce vyberte New Quota Request a poté Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

V panelu New Quota Request zadejte číselnou hodnotu pro nový limit kvóty a poté klikněte na Submit.

Vaše žádost bude posouzena a budete informováni, zda může být vyřízena. Obvykle to trvá několik minut.

Pokud vaše žádost nebude vyřízena, zobrazí se odkaz pro vytvoření podpůrné žádosti. Po kliknutí na tento odkaz vám podpora pomůže s vaší žádostí o zvýšení.

## Doporučené SKU GPU strojů Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Zde je několik příkladů:

### Pokud máte GPU A100 nebo H100

Full finetuning obvykle přináší nejlepší výkon. Pro doladění Phi-3-V na klasifikaci nenávistných memů můžete použít následující příkaz.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Pokud máte Standard_ND40rs_v2 s 8x V100-32GB GPU

Je stále možné plně doladit Phi-3-V na klasifikaci nenávistných memů. Nicméně očekávejte  
podstatně nižší propustnost ve srovnání s GPU A100 nebo H100 kvůli absenci podpory flash attention.  
Přesnost může být také ovlivněna kvůli absenci podpory bf16 (místo toho se používá trénink s fp16 smíšenou přesností).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Pokud nemáte přístup k datovým centrům s GPU

LoRA může být vaše jediná volba. Pro doladění Phi-3-V na klasifikaci nenávistných memů můžete použít následující příkaz.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pro GPU Turing+ je podporován QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Doporučené hyperparametry a očekávaná přesnost

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

Metoda tréninku | Zamrzlý model vidění | datový typ | LoRA rank | LoRA alpha | velikost batch | učící rychlost | epochy | Přesnost  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20  
Výsledky LoRA brzy |  |  |  |  |  |  |  |  |

### POZNÁMKA  
Níže uvedené výsledky pro DocVQA a Hateful memes jsou založeny na předchozí verzi (Phi-3-vision).  
Nové výsledky s Phi-3.5-vision budou brzy aktualizovány.

### DocVQA (POZNÁMKA: Phi-3-vision)

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

Metoda tréninku | datový typ | LoRA rank | LoRA alpha | velikost batch | učící rychlost | epochy | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60  
zamrzlý model obrázku | bf16 | - | - | 64 | 1e-4 | 2 | 79.19  
zamrzlý model obrázku | fp16 | - | - | 64 | 1e-4 | 2 | 78.74  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  

### Hateful memes (POZNÁMKA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda tréninku | datový typ | LoRA rank | LoRA alpha | velikost batch | učící rychlost | epochy | Přesnost  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4  
zamrzlý model obrázku | bf16 | - | - | 64 | 1e-4 | 3 | 79.4  
zamrzlý model obrázku | fp16 | - | - | 64 | 1e-4 | 3 | 78.6  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8  

## Měření rychlosti (POZNÁMKA: Phi-3-vision)

Nové výsledky benchmarku s Phi-3.5-vision budou brzy aktualizovány.

Měření rychlosti bylo provedeno na datasetu DocVQA. Průměrná délka sekvence tohoto datasetu je 2443,23 tokenů (při použití `num_crops=16` pro model obrázku).

### 8x A100-80GB (Ampere)

Metoda tréninku | \# uzlů | GPU | flash attention | Efektivní velikost batch | Propustnost (obrázků/s) | Zrychlení | Maximální paměť GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrzlý model obrázku | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrzlý model obrázku | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Metoda tréninku | \# uzlů | GPU | flash attention | Efektivní velikost batch | Propustnost (obrázků/s) | Zrychlení | Maximální paměť GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrzlý model obrázku | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Známé problémy

- Nelze spustit flash attention s fp16 (doporučuje se vždy bf16, pokud je dostupné, a všechny GPU podporující flash attention také podporují bf16).  
- Zatím není podpora ukládání mezilehlých checkpointů a pokračování v tréninku.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.