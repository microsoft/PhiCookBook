<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T21:59:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ne"
}
-->
# Phi-3.5-vision finetuning recipe

यो Phi-3.5-vision को finetuning को आधिकारिक समर्थन हो जुन huggingface लाइब्रेरीहरू प्रयोग गर्छ।
कृपया `cd` लाई कोड डाइरेक्टरी [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) मा जानुहोस् र त्यसपछि तलका आदेशहरू चलाउनुहोस्।

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

हामीले दुई उदाहरण finetuning स्क्रिप्टहरू प्रदान गरेका छौं, एउटा DocVQA का लागि र अर्को hateful meme classification का लागि।

कम्तिमा 4x RTX8000 (GPU प्रति 48GB RAM) मा परीक्षण गरिएको हार्डवेयर

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision अब आधिकारिक रूपमा बहु-छवि इनपुट समर्थन गर्छ। यहाँ NLVR2 को finetuning को लागि एउटा उदाहरण छ

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

हार्डवेयर अनुसार, प्रयोगकर्ताहरूले फरक finetuning रणनीतिहरू छनौट गर्न सक्छन्। हामी पूर्ण finetuning (Deepspeed Zero-2 सहित) र विकल्पस्वरूप vision प्यारामिटरहरूलाई फ्रोजन गरेर, साथै LoRA (4bit QLoRA सहित) समर्थन गर्छौं।
सामान्यतया, हामी flash attention र bf16 को साथ पूर्ण finetuning प्रयोग गर्न सिफारिस गर्छौं जहाँ सम्भव हो।

### आफ्नो कस्टम डेटासेटलाई आवश्यक ढाँचामा रूपान्तरण गर्ने मार्गदर्शन

हामीले न्यूनतम भिडियो वर्गीकरण डेटासेट (UCF-101 को एक उपसमूह) लाई एक अन्त्य-देखि-अन्त्य उदाहरणको रूपमा प्रयोग गरी देखाउँछौं कि कसरी आफ्नो कस्टम डेटासेटलाई आवश्यक ढाँचामा रूपान्तरण गर्ने र Phi-3.5-vision मा finetune गर्ने।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

रूपान्तरण गरिएको डाटा यसरी देखिन्छ:

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

`jsonl` एनोटेशनका लागि, प्रत्येक लाइन यस्तो डिक्सनरी हुनुपर्छ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ध्यान दिनुहोस् `conversations` एक सूची हो, त्यसैले बहु-टर्न संवाद समर्थन गर्न सकिन्छ यदि त्यस्तो डाटा उपलब्ध छ भने।

## Requesting Azure GPU Quota 

### आवश्यकताहरू

Azure खाता जुन Contributor भूमिका (वा Contributor पहुँच सहितको अन्य भूमिका) राख्छ।

यदि तपाईंको Azure खाता छैन भने, [सुरू गर्नु अघि निःशुल्क खाता बनाउनुहोस्](https://azure.microsoft.com)।

### कोटा वृद्धि अनुरोध गर्नुहोस्

तपाईं My quotas बाट सिधै कोटा वृद्धि अनुरोध गर्न सक्नुहुन्छ। तलका चरणहरू पालना गरेर कोटा वृद्धि अनुरोध गर्नुहोस्। यस उदाहरणमा, तपाईं आफ्नो सदस्यतामा कुनै पनि समायोज्य कोटा चयन गर्न सक्नुहुन्छ।

[Azure portal](https://portal.azure.com) मा साइन इन गर्नुहोस्।

खोज बक्समा "quotas" टाइप गर्नुहोस् र Quotas चयन गर्नुहोस्।
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview पृष्ठमा, Compute वा AML जस्ता प्रदायक चयन गर्नुहोस्।

**Note** Compute बाहेकका सबै प्रदायकहरूमा, तपाईंले Adjustable स्तम्भको सट्टा Request increase स्तम्भ देख्नुहुनेछ। त्यहाँ तपाईं विशिष्ट कोटाको लागि वृद्धि अनुरोध गर्न वा समर्थन अनुरोध सिर्जना गर्न सक्नुहुन्छ।

My quotas पृष्ठमा, Quota name अन्तर्गत, तपाईंले वृद्धि गर्न चाहेको कोटा चयन गर्नुहोस्। सुनिश्चित गर्नुहोस् कि Adjustable स्तम्भमा यस कोटाको लागि Yes देखिन्छ।

पृष्ठको माथिल्लो भागमा, New Quota Request चयन गर्नुहोस्, त्यसपछि Enter a new limit चयन गर्नुहोस्।

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request प्यानमा, नयाँ कोटा सीमा को लागि संख्यात्मक मान प्रविष्ट गर्नुहोस् र Submit चयन गर्नुहोस्।

तपाईंको अनुरोध समीक्षा गरिनेछ र अनुरोध पूरा गर्न सकिन्छ भने तपाईंलाई सूचित गरिनेछ। यो सामान्यतया केही मिनेट भित्र हुन्छ।

यदि तपाईंको अनुरोध पूरा भएन भने, तपाईंलाई समर्थन अनुरोध सिर्जना गर्न लिंक देखिनेछ। यस लिंक प्रयोग गर्दा, समर्थन इन्जिनियरले तपाईंलाई वृद्धि अनुरोधमा सहयोग गर्नेछन्।

## Azure Compute GPU machine SKU सुझावहरू

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

यहाँ केही उदाहरणहरू छन्:

### यदि तपाईं सँग A100 वा H100 GPU छ भने

पूर्ण finetuning सामान्यतया सबैभन्दा राम्रो प्रदर्शन दिन्छ। तपाईंले hateful memes classification मा Phi-3-V लाई finetune गर्न तलको आदेश प्रयोग गर्न सक्नुहुन्छ।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### यदि तपाईं सँग Standard_ND40rs_v2 8x V100-32GB GPU छ भने

अझै पनि Phi-3-V लाई hateful memes classification मा पूर्ण रूपमा finetune गर्न सकिन्छ। तर flash attention समर्थन नहुनाले A100 वा H100 GPU को तुलनामा थ्रूपुट धेरै कम हुनेछ। bf16 समर्थन नहुनाले (fp16 मिश्रित-प्रिसिजन प्रशिक्षण प्रयोग गरिन्छ) सटीकतामा पनि असर पर्न सक्छ।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### यदि तपाईंलाई डेटा सेन्टर GPU पहुँच छैन भने

LoRA मात्र विकल्प हुन सक्छ। तपाईंले hateful memes classification मा Phi-3-V लाई finetune गर्न तलको आदेश प्रयोग गर्न सक्नुहुन्छ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU का लागि, QLoRA समर्थित छ

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## सुझाव गरिएका हाइपरप्यारामिटरहरू र अपेक्षित सटीकता
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
तलका DocVQA र Hateful memes का नतिजाहरू पुरानो संस्करण (Phi-3-vision) मा आधारित छन्।
Phi-3.5-vision का नयाँ नतिजा चाँडै अपडेट गरिनेछ।

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

Phi-3.5-vision को नयाँ benchmarking नतिजा चाँडै अपडेट गरिनेछ।

Speed benchmarking DocVQA डेटासेटमा गरिएको छ। यस डेटासेटको औसत सिक्वेन्स लम्बाइ 2443.23 टोकन छ (`num_crops=16` प्रयोग गरेर छवि मोडलका लागि)।

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

- fp16 सँग flash attention चलाउन सकिंदैन (bf16 उपलब्ध हुँदा सधैं सिफारिस गरिन्छ, र flash attention समर्थन गर्ने सबै GPU ले bf16 पनि समर्थन गर्छन्)।
- हालसम्म बीच-बीचमा checkpoints बचत गर्ने र प्रशिक्षण पुनः सुरु गर्ने सुविधा समर्थन गरिएको छैन।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असंगतिहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।