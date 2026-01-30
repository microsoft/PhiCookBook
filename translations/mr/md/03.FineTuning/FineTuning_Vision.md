# Phi-3.5-vision finetuning रेसिपी

हे huggingface लायब्ररी वापरून Phi-3.5-vision finetuning चे अधिकृत समर्थन आहे.  
कृपया पुढील कमांड्स चालवण्यापूर्वी `cd` करून कोड डायरेक्टरी [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) मध्ये जा.

## इंस्टॉलेशन

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

## जलद प्रारंभ

आम्ही दोन उदाहरण finetuning स्क्रिप्ट्स पुरवतो, एक DocVQA साठी आणि एक hateful meme वर्गीकरणासाठी.

किमान हार्डवेअर 4x RTX8000 (प्रत्येक GPU साठी 48GB RAM) वर तपासलेले

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision आता अधिकृतपणे मल्टी-इमेज इनपुट्सना समर्थन देते. NLVR2 साठी finetuning चे उदाहरण खाली दिले आहे

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## वापर मार्गदर्शक

हार्डवेअरनुसार, वापरकर्ते वेगवेगळ्या finetuning धोरणांची निवड करू शकतात. आम्ही  
पूर्ण finetuning (Deepspeed Zero-2 सह) ज्यात दृष्टीचे पॅरामीटर्स फ्रीज करण्याचा पर्याय आहे, आणि LoRA (4bit QLoRA सह) यांना समर्थन देतो.  
सामान्यतः, शक्य असल्यास flash attention आणि bf16 सह पूर्ण finetuning वापरण्याची शिफारस करतो.

### तुमचा कस्टम डेटासेट आवश्यक स्वरूपात रूपांतर करण्यासाठी मार्गदर्शक

आम्ही UCF-101 च्या उपसमुहावर आधारित किमान व्हिडिओ वर्गीकरण डेटासेट वापरून एक एंड-टू-एंड उदाहरण देतो, ज्याद्वारे तुम्ही तुमचा कस्टम डेटासेट आवश्यक स्वरूपात कसा रूपांतरित करायचा आणि त्यावर Phi-3.5-vision कसे finetune करायचे हे दाखवले आहे.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

रूपांतरित डेटा असे दिसेल:

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

`jsonl` अ‍ॅनोटेशनसाठी, प्रत्येक ओळ ही अशी dictionary असावी:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

लक्षात ठेवा की `conversations` ही यादी आहे, त्यामुळे बहु-टर्न संभाषणासाठी समर्थन उपलब्ध आहे जर अशा प्रकारचा डेटा असेल.

## Azure GPU कोटा विनंती

### पूर्वअट

Contributor भूमिका असलेले Azure खाते (किंवा Contributor प्रवेश असलेली इतर भूमिका).

जर तुमच्याकडे Azure खाते नसेल, तर [सुरू करण्यापूर्वी मोफत खाते तयार करा](https://azure.microsoft.com).

### कोटा वाढीची विनंती करा

तुम्ही My quotas मधून थेट कोटा वाढीची विनंती करू शकता. खालील पायऱ्या वापरून कोटा वाढीसाठी विनंती करा. या उदाहरणासाठी, तुम्ही तुमच्या सबस्क्रिप्शनमधील कोणताही समायोज्य कोटा निवडू शकता.

[Azure portal](https://portal.azure.com) मध्ये साइन इन करा.

शोध बॉक्समध्ये "quotas" टाका आणि नंतर Quotas निवडा.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview पृष्ठावर, Compute किंवा AML सारखा प्रदाता निवडा.

**टीप** Compute वगळता इतर सर्व प्रदात्यांसाठी, तुम्हाला Adjustable कॉलमऐवजी Request increase कॉलम दिसेल. तिथे तुम्ही विशिष्ट कोटासाठी वाढीची विनंती करू शकता किंवा वाढीसाठी सपोर्ट विनंती तयार करू शकता.

My quotas पृष्ठावर, Quota name अंतर्गत, तुम्हाला वाढवायचा कोटा निवडा. खात्री करा की Adjustable कॉलममध्ये त्या कोटासाठी Yes दाखवले आहे.

पृष्ठाच्या वरच्या भागाजवळ, New Quota Request निवडा, नंतर Enter a new limit निवडा.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request पॅनमध्ये, तुमच्या नवीन कोटा मर्यादेसाठी संख्यात्मक मूल्य टाका, नंतर Submit निवडा.

तुमची विनंती तपासली जाईल आणि ती पूर्ण होऊ शकते का याची तुम्हाला माहिती दिली जाईल. हे सहसा काही मिनिटांत होते.

जर तुमची विनंती पूर्ण झाली नाही, तर तुम्हाला सपोर्ट विनंती तयार करण्याचा दुवा दिसेल. हा दुवा वापरल्यास, सपोर्ट अभियंता तुमच्या वाढीच्या विनंतीस मदत करेल.

## Azure Compute GPU मशीन SKU शिफारसी

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

खाली काही उदाहरणे दिली आहेत:

### तुमच्याकडे A100 किंवा H100 GPUs असल्यास

पूर्ण finetuning सहसा सर्वोत्तम कामगिरी देते. hateful memes वर्गीकरणासाठी Phi-3-V finetune करण्यासाठी खालील कमांड वापरू शकता.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### तुमच्याकडे Standard_ND40rs_v2 8x V100-32GB GPUs असल्यास

hateful memes वर्गीकरणासाठी Phi-3-V पूर्णपणे finetune करणे शक्य आहे. मात्र, flash attention समर्थन नसल्यामुळे A100 किंवा H100 GPUs च्या तुलनेत throughput खूप कमी अपेक्षित आहे.  
bf16 समर्थन नसल्यामुळे (fp16 मिश्रित-प्रिसिजन प्रशिक्षण वापरले जाते) अचूकतेवरही परिणाम होऊ शकतो.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### जर तुमच्याकडे डेटा सेंटर GPUs ची प्रवेश नाही

तर LoRA तुमचा एकमेव पर्याय असू शकतो. hateful memes वर्गीकरणासाठी Phi-3-V finetune करण्यासाठी खालील कमांड वापरा.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU साठी QLoRA समर्थित आहे

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## शिफारस केलेले हायपरपॅरामीटर्स आणि अपेक्षित अचूकता

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

| प्रशिक्षण पद्धत | फ्रीज केलेला दृष्टी मॉडेल | डेटा प्रकार | LoRA रँक | LoRA अल्फा | बॅच साईज | शिक्षण दर | एपॉक्स | अचूकता |
|---|---|---|---|---|---|---|---|---|
| full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
| full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
| LoRA परिणाम लवकरच येत आहेत |  |  |  |  |  |  |  |  |

### टीप  
खालील DocVQA आणि Hateful memes चे निकाल मागील आवृत्तीवर आधारित आहेत (Phi-3-vision).  
Phi-3.5-vision सह नवीन निकाल लवकरच अपडेट केले जातील.

### DocVQA (टीप: Phi-3-vision)

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

| प्रशिक्षण पद्धत | डेटा प्रकार | LoRA रँक | LoRA अल्फा | बॅच साईज | शिक्षण दर | एपॉक्स | ANLS |
|---|---|---|---|---|---|---|---|
| full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
| full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
| frozen image model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
| frozen image model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
| LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
| LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
| QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
| QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (टीप: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

| प्रशिक्षण पद्धत | डेटा प्रकार | LoRA रँक | LoRA अल्फा | बॅच साईज | शिक्षण दर | एपॉक्स | अचूकता |
|---|---|---|---|---|---|---|---|
| full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
| full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
| frozen image model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
| frozen image model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
| LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
| LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
| QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
| QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## गती मापन (टीप: Phi-3-vision)

Phi-3.5-vision सह नवीन गती मापन निकाल लवकरच अपडेट केले जातील.

गती मापन DocVQA डेटासेटवर केले गेले आहे. या डेटासेटची सरासरी सिक्वेन्स लांबी 2443.23 टोकन्स आहे (`num_crops=16` वापरून इमेज मॉडेलसाठी).

### 8x A100-80GB (Ampere)

| प्रशिक्षण पद्धत | \# नोड्स | GPUs | flash attention | प्रभावी बॅच साईज | थ्रूपुट (img/s) | गती वाढ | पीक GPU मेम (GB) |
|---|---|---|---|---|---|---|---|
| full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42 |
| full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 |
| full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 |
| full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 |
| frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29 |
| frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 |
| LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50 |
| LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 |
| QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32 |
| QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 |

### 8x V100-32GB (Volta)

| प्रशिक्षण पद्धत | \# नोड्स | GPUs | flash attention | प्रभावी बॅच साईज | थ्रूपुट (img/s) | गती वाढ | पीक GPU मेम (GB) |
|---|---|---|---|---|---|---|---|
| full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32 |
| full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32 |
| full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32 |
| frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27 |
| LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30 |

## ज्ञात समस्या

- fp16 सह flash attention चालवता येत नाही (bf16 उपलब्ध असल्यास नेहमी शिफारस केली जाते, आणि flash attention समर्थित सर्व GPUs bf16 देखील समर्थन करतात).
- अद्याप मध्यवर्ती चेकपॉइंट्स जतन करणे आणि प्रशिक्षण पुन्हा सुरू करणे समर्थित नाही.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.