<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:07:09+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "sk"
}
-->
# Phi-3.5-vision recept na doladenie

Toto je oficiálna podpora doladenia Phi-3.5-vision pomocou knižníc huggingface.  
Pred spustením nasledujúcich príkazov, prosím `cd` do adresára s kódom [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Inštalácia

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

## Rýchly štart

Poskytujeme dva príklady skriptov na doladenie, jeden pre DocVQA a druhý pre klasifikáciu nenávistných meme.

Minimálny testovaný hardvér: 4x RTX8000 (48GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision teraz oficiálne podporuje vstupy s viacerými obrázkami. Tu je príklad doladenia na NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Používateľský návod

V závislosti od hardvéru si používatelia môžu vybrať rôzne stratégie doladenia. Podporujeme  
full-finetuning (s Deepspeed Zero-2) s voliteľne zamrznutými parametrami vision a LoRA (vrátane 4bit QLoRA).  
Vo všeobecnosti odporúčame používať full finetuning s flash attention a bf16 vždy, keď je to možné.

### Návod na konverziu vlastného datasetu do požadovaného formátu

Používame minimálny dataset na klasifikáciu videí (podmnožina UCF-101) ako end-to-end príklad, ktorý ukazuje, ako previesť vlastný dataset do požadovaného formátu a doladiť na ňom Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Konvertované dáta budú vyzerať takto:

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

Pre `jsonl` anotáciu by mal byť každý riadok slovník v tvare:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Upozorňujeme, že `conversations` je zoznam, takže je podporovaná viackolová konverzácia, ak sú takéto dáta dostupné.

## Žiadosť o Azure GPU kvótu

### Predpoklady

Azure účet s rolou Contributor (alebo inou rolou, ktorá obsahuje prístup Contributor).

Ak ešte nemáte Azure účet, vytvorte si [bezplatný účet pred začatím](https://azure.microsoft.com).

### Požiadajte o zvýšenie kvóty

Žiadosť o zvýšenie kvóty môžete podať priamo cez My quotas. Postupujte podľa nižšie uvedených krokov na žiadosť o zvýšenie kvóty. Pre tento príklad môžete vybrať ľubovoľnú nastaviteľnú kvótu vo vašom predplatnom.

Prihláste sa do [Azure portálu](https://portal.azure.com).

Do vyhľadávacieho poľa zadajte "quotas" a vyberte Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stránke Overview vyberte poskytovateľa, napríklad Compute alebo AML.

**Note** Pre všetkých poskytovateľov okrem Compute uvidíte stĺpec Request increase namiesto stĺpca Adjustable popísaného nižšie. Tam môžete požiadať o zvýšenie konkrétnej kvóty alebo vytvoriť požiadavku na podporu.

Na stránke My quotas, pod Quota name, vyberte kvótu, ktorú chcete zvýšiť. Uistite sa, že stĺpec Adjustable pre túto kvótu zobrazuje Áno.

Blízko vrchu stránky vyberte New Quota Request, potom vyberte Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

V paneli New Quota Request zadajte číselnú hodnotu pre nový limit kvóty a potom kliknite na Submit.

Vaša žiadosť bude preskúmaná a budete informovaný, či je možné ju splniť. Zvyčajne sa tak stane do niekoľkých minút.

Ak vaša žiadosť nebude splnená, uvidíte odkaz na vytvorenie požiadavky na podporu. Použitím tohto odkazu vám podporný inžinier pomôže s vašou žiadosťou o zvýšenie.

## Odporúčané SKU strojov Azure Compute GPU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Tu sú niektoré príklady:

### Ak máte GPU A100 alebo H100

Full finetuning zvyčajne poskytuje najlepší výkon. Na doladenie Phi-3-V na klasifikáciu nenávistných meme môžete použiť nasledujúci príkaz.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ak máte Standard_ND40rs_v2 8x V100-32GB GPU

Stále je možné plne doladiť Phi-3-V na klasifikáciu nenávistných meme. Očakávajte však oveľa nižší výkon v porovnaní s GPU A100 alebo H100 kvôli absencii podpory flash attention. Presnosť môže byť tiež ovplyvnená kvôli absencii podpory bf16 (používa sa namiesto toho zmiešaná presnosť fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ak nemáte prístup k dátovým centrám s GPU

LoRA môže byť vaša jediná možnosť. Na doladenie Phi-3-V na klasifikáciu nenávistných meme môžete použiť nasledujúci príkaz.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pre GPU Turing+ je podporovaný QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Odporúčané hyperparametre a očakávaná presnosť

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

Tréningová metóda | Zamrznutý vision model | dátový typ | LoRA rank | LoRA alpha | batch size | learning rate | epochy | Presnosť  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA výsledky čoskoro |  |  |  |  |  |  |  |  |  

### NOTE  
Nasledujúce výsledky pre DocVQA a Hateful memes sú založené na predchádzajúcej verzii (Phi-3-vision).  
Nové výsledky pre Phi-3.5-vision budú čoskoro aktualizované.

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

Tréningová metóda | dátový typ | LoRA rank | LoRA alpha | batch size | learning rate | epochy | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrznutý obrazový model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrznutý obrazový model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
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

Tréningová metóda | dátový typ | LoRA rank | LoRA alpha | batch size | learning rate | epochy | Presnosť  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrznutý obrazový model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrznutý obrazový model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Benchmark rýchlosti (NOTE: Phi-3-vision)

Nové benchmarky pre Phi-3.5-vision budú čoskoro aktualizované.

Benchmark rýchlosti sa vykonáva na datasete DocVQA. Priemerná dĺžka sekvencie v tomto datasete je 2443.23 tokenov (pri použití `num_crops=16` pre obrazový model).

### 8x A100-80GB (Ampere)

Tréningová metóda | \# uzlov | GPU | flash attention | Efektívny batch size | Priepustnosť (obr/s) | Zrýchlenie | Max GPU pamäť (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42 |  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 |  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 |  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 |  
zamrznutý obrazový model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29 |  
zamrznutý obrazový model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 |  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50 |  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 |  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32 |  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 |  

### 8x V100-32GB (Volta)

Tréningová metóda | \# uzlov | GPU | flash attention | Efektívny batch size | Priepustnosť (obr/s) | Zrýchlenie | Max GPU pamäť (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32 |  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32 |  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32 |  
zamrznutý obrazový model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27 |  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30 |  

## Známe problémy

- Nie je možné spustiť flash attention s fp16 (bf16 sa vždy odporúča, keď je dostupné, a všetky GPU podporujúce flash attention tiež podporujú bf16).  
- Zatiaľ nie je podporované ukladanie medzistavov a obnovenie tréningu.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.