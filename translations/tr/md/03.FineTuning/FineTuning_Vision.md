<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:44:52+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "tr"
}
-->
# Phi-3.5-vision ince ayar tarifi

Bu, huggingface kütüphaneleri kullanılarak Phi-3.5-vision ince ayarının resmi desteğidir.  
Aşağıdaki komutları çalıştırmadan önce lütfen kod dizinine `cd` yapın: [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Kurulum

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

## Hızlı başlangıç

DocVQA ve nefret söylemi içeren meme sınıflandırması için iki örnek ince ayar betiği sağlıyoruz.

Minimum donanım olarak 4x RTX8000 (her GPU için 48GB RAM) test edilmiştir.

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision artık resmi olarak çoklu görsel girişlerini destekliyor. İşte NLVR2 için ince ayar örneği:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Kullanım kılavuzu

Donanıma bağlı olarak kullanıcılar farklı ince ayar stratejileri seçebilir.  
Biz, isteğe bağlı olarak donmuş görsel parametrelerle birlikte Deepspeed Zero-2 destekli tam ince ayar ve LoRA (4bit QLoRA dahil) destekliyoruz.  
Genel olarak, mümkün olduğunda flash attention ve bf16 ile tam ince ayar kullanmanızı öneririz.

### Özel veri setinizi gereken formata dönüştürme rehberi

Özel veri setinizi gereken formata nasıl dönüştüreceğinizi ve Phi-3.5-vision üzerinde nasıl ince ayar yapacağınızı göstermek için minimum bir video sınıflandırma veri seti (UCF-101'in bir alt kümesi) kullanıyoruz.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Dönüştürülmüş veri şu şekilde görünecektir:

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

`jsonl` açıklaması için, her satır şu şekilde bir sözlük olmalıdır:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Dikkat edin, `conversations` bir liste olduğu için, böyle bir veri mevcutsa çok turlu sohbetler desteklenebilir.

## Azure GPU Kota Talebi

### Önkoşullar

Contributor rolüne (veya Contributor erişimini içeren başka bir role) sahip bir Azure hesabı.

Azure hesabınız yoksa, başlamadan önce [ücretsiz bir hesap oluşturun](https://azure.microsoft.com).

### Kota artışı talep etme

Kota artışı talebinizi doğrudan My quotas üzerinden gönderebilirsiniz. Aşağıdaki adımları izleyerek kota artışı talebinde bulunun. Bu örnek için aboneliğinizdeki herhangi bir ayarlanabilir kotayı seçebilirsiniz.

[Azure portal](https://portal.azure.com)'a giriş yapın.

Arama kutusuna "quotas" yazın ve ardından Quotas seçeneğini seçin.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Genel Bakış sayfasında, Compute veya AML gibi bir sağlayıcı seçin.

**Not** Compute dışındaki tüm sağlayıcılar için, aşağıda açıklanan Adjustable sütunu yerine Request increase sütunu görünecektir. Buradan belirli bir kota için artış talep edebilir veya artış için destek talebi oluşturabilirsiniz.

My quotas sayfasında, Quota name altında artırmak istediğiniz kotayı seçin. Bu kotanın Adjustable sütununda Evet olduğundan emin olun.

Sayfanın üst kısmına yakın yerde, New Quota Request seçeneğini seçin, ardından Enter a new limit seçeneğini seçin.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request panelinde, yeni kota limitiniz için sayısal bir değer girin ve ardından Submit seçeneğini seçin.

Talebiniz incelenecek ve talebin karşılanıp karşılanamayacağı size bildirilecektir. Bu genellikle birkaç dakika içinde gerçekleşir.

Talebiniz karşılanmazsa, destek talebi oluşturmak için bir bağlantı göreceksiniz. Bu bağlantıyı kullandığınızda, bir destek mühendisi artış talebinizde size yardımcı olacaktır.

## Azure Compute GPU makine SKU önerileri

[ND A100 v4-serisi](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serisi](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

İşte bazı örnekler:

### A100 veya H100 GPU'larınız varsa

Tam ince ayar genellikle en iyi performansı verir. Aşağıdaki komutu kullanarak Phi-3-V'yi nefret söylemi içeren meme sınıflandırması için ince ayar yapabilirsiniz.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPU'larınız varsa

Phi-3-V'yi nefret söylemi içeren meme sınıflandırması için tam olarak ince ayar yapmak hala mümkündür. Ancak, flash attention desteği olmadığı için A100 veya H100 GPU'lara kıyasla çok daha düşük verim bekleyin.  
Ayrıca, bf16 desteği olmadığı için doğruluk da etkilenebilir (yerine fp16 karışık hassasiyet eğitimi kullanılır).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Veri merkezi GPU'larına erişiminiz yoksa

LoRA muhtemelen tek seçeneğinizdir. Aşağıdaki komutu kullanarak Phi-3-V'yi nefret söylemi içeren meme sınıflandırması için ince ayar yapabilirsiniz.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU için QLoRA desteklenmektedir.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Önerilen hiperparametreler ve beklenen doğruluk

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

Eğitim yöntemi | Donmuş görsel model | veri tipi | LoRA rank | LoRA alpha | batch boyutu | öğrenme hızı | epoch sayısı | Doğruluk
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA sonuçları yakında geliyor |  |  |  |  |  |  |  |  |

### NOT

Aşağıdaki DocVQA ve Nefret söylemi içeren meme sonuçları önceki sürüm (Phi-3-vision) baz alınarak verilmiştir.  
Phi-3.5-vision ile yeni sonuçlar yakında güncellenecektir.

### DocVQA (NOT: Phi-3-vision)

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

Eğitim yöntemi | veri tipi | LoRA rank | LoRA alpha | batch boyutu | öğrenme hızı | epoch sayısı | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
donmuş görsel model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
donmuş görsel model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Nefret söylemi içeren memeler (NOT: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Eğitim yöntemi | veri tipi | LoRA rank | LoRA alpha | batch boyutu | öğrenme hızı | epoch sayısı | Doğruluk
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
donmuş görsel model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
donmuş görsel model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Hız karşılaştırması (NOT: Phi-3-vision)

Phi-3.5-vision ile yeni karşılaştırma sonuçları yakında güncellenecektir.

Hız karşılaştırması DocVQA veri seti üzerinde yapılmıştır. Bu veri setinin ortalama dizi uzunluğu 2443.23 token’dır (`num_crops=16` kullanılarak görsel modeli için).

### 8x A100-80GB (Ampere)

Eğitim yöntemi | \# düğüm | GPU sayısı | flash attention | Etkili batch boyutu | İşlem hızı (img/s) | Hız artışı | Maks GPU bellek (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
donmuş görsel model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
donmuş görsel model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Eğitim yöntemi | \# düğüm | GPU sayısı | flash attention | Etkili batch boyutu | İşlem hızı (img/s) | Hız artışı | Maks GPU bellek (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
donmuş görsel model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Bilinen sorunlar

- fp16 ile flash attention çalıştırılamıyor (bf16 her zaman mevcutsa önerilir ve flash attention destekleyen tüm GPU’lar aynı zamanda bf16’yı da destekler).  
- Ara kontrol noktalarının kaydedilmesi ve eğitimin devam ettirilmesi henüz desteklenmiyor.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.