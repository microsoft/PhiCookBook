# Phi-3.5-vision ফাইনটিউনিং রেসিপি

এটি Phi-3.5-vision ফাইনটিউনিংয়ের অফিসিয়াল সমর্থন যা huggingface লাইব্রেরি ব্যবহার করে।  
অনুগ্রহ করে নিচের কমান্ডগুলি চালানোর আগে কোড ডিরেক্টরিতে `cd` করুন [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning)।

## ইনস্টলেশন

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

## দ্রুত শুরু

আমরা দুটি উদাহরণ ফাইনটিউনিং স্ক্রিপ্ট প্রদান করি, একটি DocVQA এর জন্য এবং অন্যটি hateful meme classification এর জন্য।

সর্বনিম্ন হার্ডওয়্যার যা পরীক্ষা করা হয়েছে: 4x RTX8000 (প্রতি GPU 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision এখন অফিসিয়ালি মাল্টি-ইমেজ ইনপুট সমর্থন করে। এখানে NLVR2 এর ফাইনটিউনিং এর একটি উদাহরণ দেওয়া হলো

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ব্যবহারের নির্দেশিকা

হার্ডওয়্যারের উপর নির্ভর করে, ব্যবহারকারীরা বিভিন্ন ফাইনটিউনিং কৌশল বেছে নিতে পারেন। আমরা  
full-finetuning (Deepspeed Zero-2 সহ) সমর্থন করি, যেখানে ভিশন প্যারামিটারগুলো ঐচ্ছিকভাবে ফ্রোজেন রাখা যায়, এবং LoRA (4bit QLoRA সহ)।  
সাধারণত, আমরা পরামর্শ দিই full finetuning ব্যবহার করার জন্য flash attention এবং bf16 সহ যতটা সম্ভব।

### আপনার কাস্টম ডেটাসেটকে প্রয়োজনীয় ফরম্যাটে রূপান্তরের নির্দেশিকা

আমরা একটি ন্যূনতম ভিডিও ক্লাসিফিকেশন ডেটাসেট (UCF-101 এর একটি সাবসেট) ব্যবহার করে একটি এন্ড-টু-এন্ড উদাহরণ দিচ্ছি, যা দেখায় কিভাবে আপনার কাস্টম ডেটাসেটকে প্রয়োজনীয় ফরম্যাটে রূপান্তর করে Phi-3.5-vision এর উপর ফাইনটিউনিং করবেন।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

রূপান্তরিত ডেটা এরকম দেখাবে:

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

`jsonl` অ্যানোটেশনের জন্য, প্রতিটি লাইন একটি ডিকশনারির মতো হওয়া উচিত:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

দ্রষ্টব্য, `conversations` একটি তালিকা, তাই মাল্টি-টার্ন কথোপকথন সমর্থিত হতে পারে যদি এমন ডেটা থাকে।

## Azure GPU কোটা অনুরোধ

### পূর্বশর্ত

একটি Azure অ্যাকাউন্ট যার Contributor রোল আছে (অথবা অন্য কোনো রোল যা Contributor অ্যাক্সেস অন্তর্ভুক্ত করে)।

যদি আপনার Azure অ্যাকাউন্ট না থাকে, তাহলে [শুরু করার আগে একটি ফ্রি অ্যাকাউন্ট তৈরি করুন](https://azure.microsoft.com)।

### কোটা বৃদ্ধি অনুরোধ করুন

আপনি My quotas থেকে সরাসরি কোটা বৃদ্ধি অনুরোধ জমা দিতে পারেন। নিচের ধাপগুলো অনুসরণ করুন একটি কোটা বৃদ্ধির জন্য অনুরোধ করতে। এই উদাহরণে, আপনি আপনার সাবস্ক্রিপশনের যেকোনো সামঞ্জস্যযোগ্য কোটা নির্বাচন করতে পারেন।

[Azure portal](https://portal.azure.com) এ সাইন ইন করুন।

সার্চ বক্সে "quotas" লিখুন, তারপর Quotas নির্বাচন করুন।  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview পৃষ্ঠায়, একটি প্রোভাইডার নির্বাচন করুন, যেমন Compute বা AML।

**Note** Compute ছাড়া অন্য সব প্রোভাইডারের জন্য, আপনি Adjustable কলামের পরিবর্তে Request increase কলাম দেখতে পাবেন। সেখানে আপনি নির্দিষ্ট একটি কোটার জন্য বৃদ্ধি অনুরোধ করতে পারেন, অথবা বৃদ্ধি সংক্রান্ত সাপোর্ট রিকোয়েস্ট তৈরি করতে পারেন।

My quotas পৃষ্ঠায়, Quota name এর নিচে, আপনি যে কোটা বাড়াতে চান তা নির্বাচন করুন। নিশ্চিত করুন যে Adjustable কলামে এই কোটার জন্য Yes দেখাচ্ছে।

পৃষ্ঠার উপরের দিকে, New Quota Request নির্বাচন করুন, তারপর Enter a new limit নির্বাচন করুন।

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request প্যানেলে, আপনার নতুন কোটা সীমার জন্য একটি সংখ্যাসূচক মান লিখুন, তারপর Submit নির্বাচন করুন।

আপনার অনুরোধ পর্যালোচনা করা হবে, এবং আপনি জানানো হবে অনুরোধ পূরণযোগ্য কিনা। সাধারণত এটি কয়েক মিনিটের মধ্যে ঘটে।

যদি আপনার অনুরোধ পূরণ না হয়, তাহলে একটি সাপোর্ট রিকোয়েস্ট তৈরি করার লিঙ্ক দেখতে পাবেন। এই লিঙ্ক ব্যবহার করলে, একটি সাপোর্ট ইঞ্জিনিয়ার আপনার বৃদ্ধি অনুরোধে সাহায্য করবে।

## Azure Compute GPU মেশিন SKU প্রস্তাবনা

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

কিছু উদাহরণ নিচে দেওয়া হলো:

### যদি আপনার কাছে A100 বা H100 GPU থাকে

পূর্ণ ফাইনটিউনিং সাধারণত সেরা পারফরম্যান্স দেয়। আপনি hateful memes classification এর জন্য Phi-3-V ফাইনটিউন করতে নিচের কমান্ড ব্যবহার করতে পারেন।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### যদি আপনার কাছে Standard_ND40rs_v2 8x V100-32GB GPU থাকে

এখনো Phi-3-V কে hateful memes classification এ সম্পূর্ণ ফাইনটিউন করা সম্ভব। তবে, flash attention সমর্থনের অভাবে A100 বা H100 GPU এর তুলনায় অনেক কম থ্রুপুট আশা করুন।  
bf16 সমর্থনের অভাবে (fp16 মিক্সড-প্রিসিশন ট্রেনিং ব্যবহার করা হয়) সঠিকতাও প্রভাবিত হতে পারে।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### যদি আপনার কাছে ডেটা সেন্টার GPU অ্যাক্সেস না থাকে

তাহলে LoRA আপনার একমাত্র বিকল্প হতে পারে। hateful memes classification এর জন্য Phi-3-V ফাইনটিউন করতে নিচের কমান্ড ব্যবহার করুন।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU এর জন্য QLoRA সমর্থিত

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## প্রস্তাবিত হাইপারপ্যারামিটার এবং প্রত্যাশিত সঠিকতা

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

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### NOTE  
নিচের DocVQA এবং Hateful memes ফলাফলগুলি পূর্ববর্তী সংস্করণ (Phi-3-vision) এর উপর ভিত্তি করে।  
Phi-3.5-vision এর নতুন ফলাফল শীঘ্রই আপডেট করা হবে।

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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## স্পিড বেঞ্চমার্কিং (NOTE: Phi-3-vision)

Phi-3.5-vision এর নতুন বেঞ্চমার্কিং ফলাফল শীঘ্রই আপডেট করা হবে।

স্পিড বেঞ্চমার্কিং DocVQA ডেটাসেটে সম্পন্ন হয়েছে। এই ডেটাসেটের গড় সিকোয়েন্স দৈর্ঘ্য 2443.23 টোকেন (ইমেজ মডেলের জন্য `num_crops=16` ব্যবহার করে)।

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
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

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## পরিচিত সমস্যা

- fp16 দিয়ে flash attention চালানো যায় না (যখন bf16 পাওয়া যায় তখন সর্বদা bf16 ব্যবহার করার পরামর্শ দেওয়া হয়, এবং flash attention সমর্থনকারী সব GPU তেই bf16 সমর্থন থাকে)।  
- এখনও পর্যন্ত মধ্যবর্তী চেকপয়েন্ট সংরক্ষণ এবং ট্রেনিং পুনরায় শুরু করার সমর্থন নেই।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।