<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:52:24+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "sw"
}
-->
# Phi-3.5-vision finetuning recipe

Hii ni msaada rasmi wa finetuning ya Phi-3.5-vision kwa kutumia maktaba za huggingface. Tafadhali `cd` kwenda kwenye saraka ya msimbo [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) kabla ya kuendesha amri zifuatazo.

## Ufungaji

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

## Anza haraka

Tunatoa mifano miwili ya skripti za finetuning, moja kwa DocVQA na nyingine kwa uainishaji wa meme za chuki.

Vifaa vya chini kabisa vilivyotumika ni 4x RTX8000 (48GB RAM kwa kila GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision sasa inasaidia rasmi pembejeo za picha nyingi. Hapa kuna mfano wa finetuning NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Mwongozo wa matumizi

Kulingana na vifaa, watumiaji wanaweza kuchagua mikakati tofauti ya finetuning. Tunasaidia
full-finetuning (kwa Deepspeed Zero-2) na chaguo la kuzuia mabadiliko ya vigezo vya kuona, na LoRA (pamoja na 4bit QLoRA).
Kwa ujumla, tunapendekeza kutumia full finetuning na flash attention na bf16 inapowezekana.

### mwongozo wa kubadilisha dataset yako maalum kuwa muundo unaohitajika

Tunatumia dataset ndogo ya uainishaji wa video (sehemu ya UCF-101) kama mfano wa mwisho-ku-mwisho kuonyesha jinsi ya kubadilisha dataset yako maalum kuwa muundo unaohitajika na kufinetune Phi-3.5-vision juu yake.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Data iliyobadilishwa itaonekana kama hii:

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

Kwa maelezo ya `jsonl`, kila mstari unapaswa kuwa kamusi kama ifuatavyo:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Kumbuka kuwa `conversations` ni orodha, hivyo mazungumzo yenye mizunguko mingi yanaweza kuungwa mkono ikiwa data kama hiyo ipo.

## Kuomba Kiwango cha GPU cha Azure

### Masharti ya awali

Akaunti ya Azure yenye jukumu la Contributor (au jukumu jingine linalojumuisha upatikanaji wa Contributor).

Kama huna akaunti ya Azure, tengeneza [akaunti ya bure kabla ya kuanza](https://azure.microsoft.com).

### Omba ongezeko la kiwango

Unaweza kuwasilisha ombi la ongezeko la kiwango moja kwa moja kutoka My quotas. Fuata hatua zilizo hapa chini kuomba ongezeko la kiwango. Kwa mfano huu, unaweza kuchagua kiwango chochote kinachoweza kubadilishwa katika usajili wako.

Ingia kwenye [Azure portal](https://portal.azure.com).

Andika "quotas" kwenye kisanduku cha utafutaji, kisha chagua Quotas.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Kwenye ukurasa wa Muhtasari, chagua mtoa huduma, kama Compute au AML.

**Note** Kwa watoa huduma wote isipokuwa Compute, utaona safu ya Request increase badala ya safu ya Adjustable kama ilivyoelezwa hapa chini. Huko, unaweza kuomba ongezeko la kiwango fulani, au kuunda ombi la msaada kwa ajili ya ongezeko hilo.

Kwenye ukurasa wa My quotas, chini ya Jina la Kiwango, chagua kiwango unachotaka kuongeza. Hakikisha safu ya Adjustable inaonyesha Ndiyo kwa kiwango hiki.

Karibu juu ya ukurasa, chagua New Quota Request, kisha chagua Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Kwenye dirisha la New Quota Request, ingiza thamani ya nambari kwa kikomo chako kipya cha kiwango, kisha chagua Submit.

Ombi lako litapitiwa, na utajulishwa kama ombi linaweza kutimizwa. Hii kawaida hutokea ndani ya dakika chache.

Kama ombi lako halitatimizwa, utaona kiungo cha kuunda ombi la msaada. Unapotumia kiungo hiki, mhandisi wa msaada atakusaidia na ombi lako la ongezeko.

## Mapendekezo ya SKU za Mashine za Azure Compute GPU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Hapa kuna mifano kadhaa:

### Ikiwa una GPU za A100 au H100

Full finetuning kawaida hutoa utendaji bora zaidi. Unaweza kutumia amri ifuatayo kufinetune Phi-3-V kwenye uainishaji wa meme za chuki.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ikiwa una Standard_ND40rs_v2 8x V100-32GB GPUs

Bado inawezekana kufinetune kikamilifu Phi-3-V kwenye uainishaji wa meme za chuki. Hata hivyo, tarajia
kupata throughput ya chini sana ikilinganishwa na GPU za A100 au H100 kutokana na ukosefu wa msaada wa flash attention.
Usahihi pia unaweza kuathiriwa kutokana na ukosefu wa msaada wa bf16 (mafunzo ya mchanganyiko wa fp16 hutumika badala yake).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ikiwa huna upatikanaji wa GPU za kituo cha data
Lora inaweza kuwa chaguo lako pekee. Unaweza kutumia amri ifuatayo kufinetune Phi-3-V kwenye uainishaji wa meme za chuki.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Kwa GPU za Turing+ QLoRA inasaidiwa

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Vigezo vilivyopendekezwa na usahihi unaotarajiwa
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

Njia ya mafunzo | Frozen vision model | aina ya data | LoRA rank | LoRA alpha | ukubwa wa batch | kiwango cha kujifunza | vipindi | Usahihi
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Matokeo ya LoRA yatakuja hivi karibuni |  |  |  |  |  |  |  |  |

### NOTE
Matokeo ya DocVQA na meme za chuki yaliyo hapa chini yanatokana na toleo la awali (Phi-3-vision).
Matokeo mapya na Phi-3.5-vision yatasasishwa hivi karibuni.

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

Njia ya mafunzo | aina ya data | LoRA rank | LoRA alpha | ukubwa wa batch | kiwango cha kujifunza | vipindi | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Meme za chuki (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Njia ya mafunzo | aina ya data | LoRA rank | LoRA alpha | ukubwa wa batch | kiwango cha kujifunza | vipindi | Usahihi
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Kupima kasi (NOTE: Phi-3-vision)

Matokeo mapya ya kupima kasi na Phi-3.5-vision yatasasishwa hivi karibuni.

Kupima kasi kunafanywa kwenye dataset ya DocVQA. Urefu wa wastani wa mfuatano wa dataset hii ni
2443.23 tokens (kutumia `num_crops=16` kwa mfano wa picha).

### 8x A100-80GB (Ampere)

Njia ya mafunzo | \# nodes | GPUs | flash attention | Ukubwa wa batch unaofanya kazi | Throughput (picha/s) | Kuongeza kasi | Kumbukumbu ya juu ya GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Njia ya mafunzo | \# nodes | GPUs | flash attention | Ukubwa wa batch unaofanya kazi | Throughput (picha/s) | Kuongeza kasi | Kumbukumbu ya juu ya GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Masuala yanayojulikana

- Haiwezi kuendesha flash attention na fp16 (bf16 daima inapendekezwa inapopatikana, na GPU zote zinazounga mkono flash attention pia zinaunga mkono bf16).
- Haina msaada wa kuhifadhi checkpoints za kati na kuendelea na mafunzo bado.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.