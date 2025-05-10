<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T21:58:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "mr"
}
-->
# Phi-3.5-vision finetuning recipe

हे Phi-3.5-vision finetuning साठी huggingface लायब्ररीजचा अधिकृत सपोर्ट आहे. पुढील कमांड्स चालवण्यापूर्वी कृपया `cd` करून code directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) मध्ये जा.

## Installation

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

## Quick start

आम्ही दोन उदाहरण finetuning स्क्रिप्ट्स दिल्या आहेत, एक DocVQA साठी आणि दुसरी hateful meme classification साठी.

कमी हार्डवेअरवर चाचणी 4x RTX8000 (प्रत्येक GPU ला 48GB RAM) वर केली आहे.

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision आता मल्टी-इमेज इनपुट्सना अधिकृतपणे सपोर्ट करतो. NLVR2 साठी finetuning चे एक उदाहरण खाली दिले आहे.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

हार्डवेअर नुसार वापरकर्ते वेगवेगळ्या finetuning स्ट्रॅटेजी निवडू शकतात. आम्ही full-finetuning (Deepspeed Zero-2 सह) सपोर्ट करतो ज्यात व्हिजन पॅरामीटर्स फ्रीज करता येतात, तसेच LoRA (4bit QLoRA सह) देखील आहे. सामान्यतः, शक्य तितक्या वेळी flash attention आणि bf16 सह full finetuning वापरण्याचा सल्ला दिला जातो.

### तुमच्या कस्टम dataset ला आवश्यक फॉरमॅटमध्ये कसे कन्व्हर्ट करायचे यासाठी मार्गदर्शक

आम्ही UCF-101 च्या एका सबसेटवर आधारित मिनिमम व्हिडिओ क्लासिफिकेशन dataset वापरून दाखवतो की तुमच्या कस्टम dataset ला आवश्यक फॉरमॅटमध्ये कसे रूपांतरित करावे आणि त्यावर Phi-3.5-vision कसे finetune करावे.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

रूपांतरित डेटा असाच दिसेल:

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

`jsonl` अ‍ॅनोटेशनसाठी, प्रत्येक ओळ dictionary सारखी असावी:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

लक्षात ठेवा की `conversations` ही यादी आहे, त्यामुळे जर अशा डेटा उपलब्ध असेल तर मल्टी-टर्न संवादांना सपोर्ट आहे.

## Azure GPU Quota साठी विनंती कशी करावी

### पूर्वअटी

Azure account असणे आवश्यक आहे ज्यात Contributor रोल (किंवा Contributor access असलेला अन्य रोल) आहे.

जर तुमच्याकडे Azure account नसेल, तर [free account तयार करा](https://azure.microsoft.com) आणि नंतर पुढे जा.

### Quota वाढविण्यासाठी विनंती करा

तुम्ही My quotas मधून थेट quota वाढीची विनंती करू शकता. खालील स्टेप्स फॉलो करा. या उदाहरणासाठी, तुमच्या subscription मधील कोणताही adjustable quota निवडू शकता.

[Azure portal](https://portal.azure.com) मध्ये साइन इन करा.

सर्च बॉक्समध्ये "quotas" टाका आणि Quotas निवडा.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview पेजवर, Compute किंवा AML सारखा provider निवडा.

**Note** Compute वगळता इतर सर्व providers साठी Request increase कॉलम दिसेल, जिथे तुम्ही विशिष्ट quota साठी वाढीची विनंती करू शकता किंवा सपोर्ट रिक्वेस्ट तयार करू शकता.

My quotas पेजवर, Quota name खाली तुम्हाला वाढवायचा quota निवडा. Adjustable कॉलम मध्ये हो (Yes) असल्याची खात्री करा.

पेजच्या वरच्या भागात New Quota Request निवडा, नंतर Enter a new limit निवडा.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request पॅनलमध्ये नवीन quota मर्यादेसाठी संख्या टाका आणि Submit करा.

तुमची विनंती तपासली जाईल आणि मंजूर झाली की तुम्हाला कळवले जाईल. हे सहसा काही मिनिटांत होते.

जर विनंती मंजूर झाली नाही तर सपोर्ट रिक्वेस्ट तयार करण्याचा लिंक दिसेल. त्यावर क्लिक केल्यास सपोर्ट इंजिनियर तुमच्या विनंतीस मदत करेल.

## Azure Compute GPU मशीन SKU सुचना

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

काही उदाहरणे:

### जर तुमच्याकडे A100 किंवा H100 GPUs असतील

Full finetuning सहसा सर्वोत्तम कामगिरी देते. hateful memes classification साठी Phi-3-V finetune करण्यासाठी खालील कमांड वापरा.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### जर तुमच्याकडे Standard_ND40rs_v2 8x V100-32GB GPUs असतील

Phi-3-V hateful memes classification वर पूर्णपणे finetune करणे शक्य आहे. पण A100 किंवा H100 GPUs च्या तुलनेत throughput खूप कमी अपेक्षित आहे कारण flash attention सपोर्ट नाही. तसेच bf16 सपोर्ट नसल्यामुळे (fp16 mixed-precision training वापरले जाते) अचूकतेवर परिणाम होऊ शकतो.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### जर तुमच्याकडे data center GPUs नसतील

तर LoRA तुमचा एकमेव पर्याय असू शकतो. hateful memes classification साठी Phi-3-V finetune करण्यासाठी खालील कमांड वापरा.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU साठी QLoRA सपोर्ट आहे.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## सुचवलेले हायपरपॅरामिटर्स आणि अपेक्षित अचूकता
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
खालील DocVQA आणि Hateful memes चे निकाल मागील आवृत्तीवर आधारित आहेत (Phi-3-vision).
Phi-3.5-vision सोबत नवीन निकाल लवकरच अपडेट केले जातील.

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

## Speed benchmarking (NOTE: Phi-3-vision)

Phi-3.5-vision सह नवीन benchmarking निकाल लवकरच अपडेट केले जातील.

Speed benchmarking DocVQA dataset वर केली आहे. या dataset ची सरासरी sequence length 2443.23 tokens आहे (`num_crops=16` वापरून image model साठी).

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

## Known issues

- fp16 सह flash attention चालवता येत नाही (bf16 उपलब्ध असल्यास नेहमी bf16 वापरण्याचा सल्ला दिला जातो, आणि flash attention सपोर्ट करणाऱ्या सर्व GPUs मध्ये bf16 सपोर्ट देखील असतो).
- सध्या इंटरमिडिएट checkpoints सेव्ह करणे आणि training resume करणे सपोर्ट करत नाही.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती असल्यास व्यावसायिक मानवी भाषांतर करण्याचा सल्ला दिला जातो. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.