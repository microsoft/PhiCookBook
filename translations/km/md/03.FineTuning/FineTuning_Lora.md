# **ការប្រឹងប្រែង Phi-3 ជាមួយ Lora**

ការប្រឹងប្រែងម៉ូឌែលភាសា Phi-3 Mini របស់ Microsoft ដោយប្រើ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) លើឃូរដែតាប្រដាប់សម្រាប់ការណែនាំជជែកប្តូរ។

LORA នឹងជួយធ្វើឱ្យការយល់ដឹងនិងការបង្កើតចម្លើយក្នុងការជជែកកាន់តែប្រសើរ។

## មគ្គុទេសក៍ជំហានដោយជំហានពីរប كيفية fine-tune Phi-3 Mini:

**ការនាំចូលនិងការតំលើង**

ការដំឡើង loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```


ចាប់ផ្តើមដោយនាំចូលបណ្ណាល័យដែលចាំបាច់ដូចជា datasets, transformers, peft, trl, និង torch។
រៀបចំការចុះបញ្ជីដើម្បីតាមដានដំណើរការបណ្ដុះបណ្ដាល។

អ្នកអាចជ្រើសរើសបម្លែងស្រទាប់ខ្លះដោយប្ដូរ​ពួកវាជាមួយសមាសភាគដែលអនុវត្តន៍ក្នុង loralib។ យើងគាំទ្រ​តែ nn.Linear, nn.Embedding, និង nn.Conv2d នៅពេលនេះប៉ុណ្ណោះ។ យើងក៏គាំទ្រ MergedLinear សម្រាប់ករណីដែល nn.Linear តែមួយតំណាងឱ្យស្រទាប់ច្រើនជាងមួយ ដូចជា ក្នុងការអនុវត្ត qkv projection នៅក្នុង បញ្ហាទំនាក់ទំនង (មើល ការណែនាំបន្ថែមសម្រាប់ព័ត៌មានបន្ថែម)។

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

មុនចាប់ផ្តើមរំលោភកំណត់ពេលបណ្ដុះ បញ្ជាក់ថាប៉ារ៉ាម៉ែត្រ LoRA តែប៉ុណ្ណោះគឺអាចបណ្ដុះបាន។

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ពេលរក្សាទុក checkpoint សូមបង្កើត state_dict ដែលមានតែប៉ារ៉ាម៉ែត្រ LoRA ផ่านั้น។

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

ពេលបញ្ចូល checkpoint ដោយប្រើ load_state_dict សូមធ្វើការ set strict=False។

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ឥឡូវនេះ ការបណ្ដុះអាចបន្តដូចធម្មតា។

**Hyperparameters**

កំណត់ពីរម៉ាប់បញ្ជីៈ training_config និង peft_config។ training_config មាន hyperparameters សម្រាប់ការបណ្ដុះបណ្តាល ដូចជា អត្រាសិក្សា, ទំហំបញ្ចប់, និងការកំណត់ logging។

peft_config បញ្ជាក់ប៉ារ៉ាម៉ែត្រ LoRA ដូចជា rank, dropout, និងប្រភេទភារកិច្ច។

**ការចូលម៉ូឌែលនិង Tokenizer**

បញ្ជាក់ផ្លូវទៅម៉ូឌែល Phi-3 ដែលបានបណ្ដុះរួច (ឧ. "microsoft/Phi-3-mini-4k-instruct")។ កំណត់ការកំណត់ម៉ូឌែល រួមទាំងការប្រើ cache, ប្រភេទទិន្នន័យ (bfloat16 សម្រាប់ precision зміxed), និងការអនុវត្តអារម្មណ៍។

**ការបណ្ដុះ**

បណ្ដុះ Phi-3 ជាមួយឃូរដែតាប្រដាប់សម្រាប់ការណែនាំជជែកផ្ទាល់ខ្លួន។ ប្រើការកំណត់ LoRA ពី peft_config សម្រាប់ការបំលែងមានប្រសិទ្ធភាព។ តាមដានដំណើរការបណ្ដុះដោយប្រើយុទ្ធសាស្រ្ត logging ដែលបានកំណត់។
ការវាយតម្លៃ និងការរក្សាទុក៖ វាយតម្លៃម៉ូឌែលបានបណ្ដុះរួច។
រក្សាទុក checkpoint នៅពេលបណ្ដុះសម្រាប់ការប្រើប្រាស់ក្រោយ។

**គំរូ**
- [រៀនបន្ថែមជាមួយសៀវភៅគំរូនេះ](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [គំរូ Python FineTuning សម្រាប់ការសាកល្បង](../../../../code/03.Finetuning/FineTrainingScript.py)
- [គំរូ Hugging Face Hub Fine Tuning ជាមួយ LORA](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [គំរូ Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [គំរូ Hugging Face Hub Fine Tuning ជាមួយ QLORA](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខំប្រឹងព្យាយាមរកភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬការមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាមាតុភូមិគួរត្រូវបានគេពិចារណាថាជាទ្រព្យសម្បត្តិដើមដែលមានអាជ្ញា។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរត្រូវបានចិត្តយកការបកប្រែដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសទេសចរណ៍ណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->