<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:51:01+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ms"
}
-->
# Resipi penalaan halus Phi-3.5-vision

Ini adalah sokongan rasmi untuk penalaan halus Phi-3.5-vision menggunakan perpustakaan huggingface.  
Sila `cd` ke direktori kod [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) sebelum menjalankan arahan berikut.

## Pemasangan

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

## Mula dengan cepat

Kami menyediakan dua skrip contoh penalaan halus, satu untuk DocVQA dan satu untuk klasifikasi meme kebencian.

Perkakasan minimum yang diuji menggunakan 4x RTX8000 (48GB RAM setiap GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision kini secara rasmi menyokong input berbilang imej. Berikut adalah contoh untuk penalaan halus NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Panduan penggunaan

Bergantung pada perkakasan, pengguna boleh memilih strategi penalaan halus yang berbeza. Kami menyokong  
penalaan halus penuh (dengan Deepspeed Zero-2) dengan pilihan parameter visi yang dibekukan, dan LoRA (termasuk 4bit QLoRA).  
Secara umum, kami mengesyorkan menggunakan penalaan halus penuh dengan flash attention dan bf16 bila boleh.

### panduan untuk menukar dataset tersuai anda ke format yang diperlukan

Kami menggunakan dataset klasifikasi video minimum (subset UCF-101) sebagai contoh menyeluruh untuk menunjukkan cara menukar dataset tersuai anda ke format yang diperlukan dan menala halus Phi-3.5-vision ke atasnya.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Data yang telah ditukar akan kelihatan seperti ini:

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

Untuk anotasi `jsonl`, setiap baris harus berupa kamus seperti:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Perlu diingat bahawa `conversations` adalah senarai, jadi perbualan berbilang giliran boleh disokong jika data sebegini tersedia.

## Memohon Kuota GPU Azure

### Prasyarat

Akaun Azure dengan peranan Contributor (atau peranan lain yang termasuk akses Contributor).

Jika anda belum mempunyai akaun Azure, buat [akaun percuma sebelum anda mula](https://azure.microsoft.com).

### Memohon peningkatan kuota

Anda boleh menghantar permohonan untuk peningkatan kuota terus dari My quotas. Ikuti langkah di bawah untuk memohon peningkatan kuota. Untuk contoh ini, anda boleh memilih mana-mana kuota yang boleh disesuaikan dalam langganan anda.

Log masuk ke [portal Azure](https://portal.azure.com).

Masukkan "quotas" dalam kotak carian, kemudian pilih Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Pada halaman Overview, pilih penyedia, seperti Compute atau AML.

**Note** Untuk semua penyedia selain Compute, anda akan melihat lajur Request increase dan bukannya lajur Adjustable seperti yang diterangkan di bawah. Di sana, anda boleh memohon peningkatan untuk kuota tertentu, atau membuat permintaan sokongan untuk peningkatan tersebut.

Pada halaman My quotas, di bawah Quota name, pilih kuota yang anda ingin tingkatkan. Pastikan lajur Adjustable menunjukkan Yes untuk kuota ini.

Di bahagian atas halaman, pilih New Quota Request, kemudian pilih Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Dalam panel New Quota Request, masukkan nilai nombor untuk had kuota baru anda, kemudian pilih Submit.

Permohonan anda akan disemak, dan anda akan diberitahu jika permohonan boleh dipenuhi. Ini biasanya berlaku dalam beberapa minit.

Jika permohonan anda tidak dipenuhi, anda akan melihat pautan untuk membuat permintaan sokongan. Apabila anda menggunakan pautan ini, jurutera sokongan akan membantu anda dengan permohonan peningkatan anda.

## Cadangan SKU mesin GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Berikut adalah beberapa contoh:

### Jika anda mempunyai GPU A100 atau H100

Penalaan halus penuh biasanya memberikan prestasi terbaik. Anda boleh menggunakan arahan berikut untuk menala halus Phi-3-V pada klasifikasi meme kebencian.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Jika anda mempunyai Standard_ND40rs_v2 8x V100-32GB GPUs

Masih boleh menala halus penuh Phi-3-V pada klasifikasi meme kebencian. Namun, jangkaan  
kelajuan jauh lebih rendah berbanding GPU A100 atau H100 kerana tiada sokongan flash attention.  
Ketepatan juga mungkin terjejas kerana tiada sokongan bf16 (latihan presisi campuran fp16 digunakan sebagai gantinya).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Jika anda tidak mempunyai akses ke GPU pusat data

LoRA mungkin satu-satunya pilihan anda. Anda boleh menggunakan arahan berikut untuk menala halus Phi-3-V pada klasifikasi meme kebencian.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Untuk GPU Turing+ , QLoRA disokong

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hiperparameter yang dicadangkan dan ketepatan dijangka

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

Kaedah latihan | Model visi dibekukan | jenis data | pangkat LoRA | alpha LoRA | saiz batch | kadar pembelajaran | epoch | Ketepatan  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Keputusan LoRA akan datang tidak lama lagi |  |  |  |  |  |  |  |  |

### NOTE  
Keputusan DocVQA dan meme kebencian di bawah adalah berdasarkan versi sebelumnya (Phi-3-vision).  
Keputusan baru dengan Phi-3.5-vision akan dikemas kini tidak lama lagi.

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

Kaedah latihan | jenis data | pangkat LoRA | alpha LoRA | saiz batch | kadar pembelajaran | epoch | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
model imej dibekukan | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
model imej dibekukan | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Meme kebencian (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Kaedah latihan | jenis data | pangkat LoRA | alpha LoRA | saiz batch | kadar pembelajaran | epoch | Ketepatan  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
model imej dibekukan | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
model imej dibekukan | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Penanda aras kelajuan (NOTE: Phi-3-vision)

Keputusan penanda aras baru dengan Phi-3.5-vision akan dikemas kini tidak lama lagi.

Penanda aras kelajuan dijalankan pada dataset DocVQA. Purata panjang urutan dataset ini  
adalah 2443.23 token (menggunakan `num_crops=16` untuk model imej).

### 8x A100-80GB (Ampere)

Kaedah latihan | \# nod | GPU | flash attention | Saiz batch berkesan | Kelajuan (img/s) | Peningkatan kelajuan | Memori GPU maksimum (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
model imej dibekukan | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
model imej dibekukan | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Kaedah latihan | \# nod | GPU | flash attention | Saiz batch berkesan | Kelajuan (img/s) | Peningkatan kelajuan | Memori GPU maksimum (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
model imej dibekukan | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Isu yang diketahui

- Tidak boleh menjalankan flash attention dengan fp16 (bf16 sentiasa disyorkan jika tersedia, dan semua GPU yang menyokong flash attention juga menyokong bf16).  
- Tidak menyokong penyimpanan checkpoint sementara dan menyambung semula latihan buat masa ini.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.