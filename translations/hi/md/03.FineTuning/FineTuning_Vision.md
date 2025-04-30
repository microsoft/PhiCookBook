<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dd1b570422a819b39b14a4c7be06c8fa",
  "translation_date": "2025-04-04T19:05:14+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Vision.md",
  "language_code": "hi"
}
-->
# Phi-3.5-vision फाइन-ट्यूनिंग प्रक्रिया

यह Phi-3.5-vision को फाइन-ट्यून करने के लिए हगिंगफेस लाइब्रेरी का आधिकारिक समर्थन है। कृपया `cd` कोड डायरेक्टरी [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) पर जाएं, और नीचे दिए गए कमांड्स को चलाने से पहले इसे सेट करें।

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

## त्वरित शुरुआत

हमने दो उदाहरण फाइन-ट्यूनिंग स्क्रिप्ट प्रदान की हैं: एक DocVQA के लिए और दूसरी hateful meme classification के लिए।

न्यूनतम हार्डवेयर: 4x RTX8000 (प्रत्येक GPU में 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision अब आधिकारिक तौर पर मल्टी-इमेज इनपुट्स को सपोर्ट करता है। NLVR2 पर फाइन-ट्यूनिंग का एक उदाहरण यहां दिया गया है:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## उपयोग गाइड

हार्डवेयर के आधार पर, उपयोगकर्ता विभिन्न फाइन-ट्यूनिंग रणनीतियों को चुन सकते हैं। हम पूर्ण फाइन-ट्यूनिंग (Deepspeed Zero-2 के साथ) का समर्थन करते हैं, जिसमें विज़न पैरामीटर को फ्रीज करने का विकल्प होता है, और LoRA (4bit QLoRA सहित) का भी समर्थन करते हैं। सामान्य तौर पर, हम फ्लैश अटेंशन और bf16 के साथ पूर्ण फाइन-ट्यूनिंग की सिफारिश करते हैं, जब भी संभव हो।

### आपके कस्टम डेटासेट को आवश्यक प्रारूप में बदलने के लिए गाइड

हम न्यूनतम वीडियो क्लासिफिकेशन डेटासेट (UCF-101 का एक उपसमूह) का उपयोग करते हैं, ताकि यह दिखाया जा सके कि अपने कस्टम डेटासेट को आवश्यक प्रारूप में कैसे बदलें और Phi-3.5-vision पर इसे फाइन-ट्यून करें।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

कन्वर्ट किया गया डेटा इस प्रकार दिखेगा:

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

`jsonl` एनोटेशन के लिए, प्रत्येक पंक्ति एक डिक्शनरी होनी चाहिए, जैसे:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ध्यान दें कि `conversations` एक सूची है, इसलिए यदि उपलब्ध हो, तो मल्टी-टर्न बातचीत का समर्थन किया जा सकता है।

## Azure GPU कोटा का अनुरोध करना

### आवश्यकताएँ

Contributor भूमिका (या Contributor एक्सेस वाली कोई अन्य भूमिका) के साथ एक Azure खाता।

यदि आपके पास Azure खाता नहीं है, तो [शुरू करने से पहले एक मुफ्त खाता बनाएं](https://azure.microsoft.com)।

### कोटा वृद्धि का अनुरोध करना

आप My quotas से सीधे कोटा वृद्धि का अनुरोध कर सकते हैं। नीचे दिए गए चरणों का पालन करें:

Azure पोर्टल में साइन इन करें: [Azure portal](https://portal.azure.com)।

सर्च बॉक्स में "quotas" दर्ज करें, और फिर Quotas चुनें।  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview पेज पर, एक प्रदाता चुनें, जैसे Compute या AML।

**Note**: Compute के अलावा अन्य सभी प्रदाताओं के लिए, आप Adjustable कॉलम के बजाय Request increase कॉलम देखेंगे। यहां, आप किसी विशिष्ट कोटा के लिए वृद्धि का अनुरोध कर सकते हैं या वृद्धि के लिए एक सपोर्ट अनुरोध बना सकते हैं।

My quotas पेज पर, Quota name के तहत, उस कोटा को चुनें जिसे आप बढ़ाना चाहते हैं। सुनिश्चित करें कि Adjustable कॉलम में Yes दिख रहा है।

पेज के शीर्ष पर, New Quota Request चुनें, फिर Enter a new limit चुनें।  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request पैन में, अपने नए कोटा लिमिट के लिए एक संख्यात्मक मान दर्ज करें, फिर Submit चुनें।

आपके अनुरोध की समीक्षा की जाएगी, और आपको सूचित किया जाएगा कि क्या इसे पूरा किया जा सकता है। आमतौर पर यह कुछ मिनटों में हो जाता है।

यदि आपका अनुरोध पूरा नहीं होता है, तो आपको एक लिंक दिखाई देगा जिससे आप एक सपोर्ट अनुरोध बना सकते हैं। इस लिंक का उपयोग करते समय, एक सपोर्ट इंजीनियर आपके वृद्धि अनुरोध में आपकी सहायता करेगा।

## Azure Compute GPU मशीन SKU सुझाव

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

### यदि आपके पास A100 या H100 GPUs हैं

पूर्ण फाइन-ट्यूनिंग आमतौर पर सर्वश्रेष्ठ प्रदर्शन देती है। आप नीचे दिए गए कमांड का उपयोग करके hateful memes classification के लिए Phi-3-V को फाइन-ट्यून कर सकते हैं:

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### यदि आपके पास Standard_ND40rs_v2 8x V100-32GB GPUs हैं

फिर भी, आप Phi-3-V को hateful memes classification के लिए पूरी तरह से फाइन-ट्यून कर सकते हैं। हालांकि, फ्लैश अटेंशन सपोर्ट की कमी के कारण थ्रूपुट अपेक्षाकृत कम होगा। bf16 सपोर्ट की कमी के कारण सटीकता पर भी प्रभाव पड़ सकता है (fp16 मिश्रित-सटीकता प्रशिक्षण का उपयोग किया जाता है)।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### यदि आपके पास डेटा सेंटर GPUs तक पहुंच नहीं है

LoRA शायद आपका एकमात्र विकल्प हो सकता है। आप नीचे दिए गए कमांड का उपयोग करके hateful memes classification के लिए Phi-3-V को फाइन-ट्यून कर सकते हैं:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU के लिए, QLoRA समर्थित है:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## सुझाए गए हाइपरपैरामीटर और अपेक्षित सटीकता

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
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results comming soon |  |  |  |  |  |  |  |  |

### नोट

नीचे दिए गए DocVQA और Hateful memes के परिणाम Phi-3-vision के पिछले संस्करण पर आधारित हैं। Phi-3.5-vision के साथ नए परिणाम जल्द ही अपडेट किए जाएंगे।

### DocVQA (नोट: Phi-3-vision)

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
frozen image model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frozen image model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (नोट: Phi-3-vision)

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
frozen image model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frozen image model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## स्पीड बेंचमार्किंग (नोट: Phi-3-vision)

Phi-3.5-vision के साथ नए बेंचमार्किंग परिणाम जल्द ही अपडेट किए जाएंगे।

स्पीड बेंचमार्किंग DocVQA डेटासेट पर की गई है। इस डेटासेट की औसत अनुक्रम लंबाई 2443.23 टोकन है (`num_crops=16` का उपयोग करके इमेज मॉडल के लिए)।

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
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
full-finetuning | 1 | 8 | | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## ज्ञात समस्याएँ

- fp16 के साथ फ्लैश अटेंशन नहीं चल सकता (bf16 हमेशा अनुशंसित है, और सभी GPUs जो फ्लैश अटेंशन का समर्थन करते हैं, bf16 का भी समर्थन करते हैं)।  
- अभी तक इंटरमीडिएट चेकपॉइंट्स को सहेजने और प्रशिक्षण को फिर से शुरू करने का समर्थन नहीं है।  

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में उपलब्ध दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।