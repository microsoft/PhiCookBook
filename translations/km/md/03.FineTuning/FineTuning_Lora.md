# **ការសម្រួល Phi-3 ជាមួយ Lora**

ការសម្រួលម៉ូដែលភាសា Phi-3 Mini របស់ Microsoft ដោយប្រើ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) លើសំណុំព័ត៌មានអប់រំការសន្ទនាផ្ទាល់ខ្លួន។

LORA នឹងជួយបង្កើនការយល់ដឹងអំពីការសន្ទនានិងការបង្កើតមុខងារឆ្លើយតប។

## មធ្យោបាយជំហានដោយជំហានសម្រាប់ការសម្រួល Phi-3 Mini៖

**ការនាំចូល និង ការតំឡើង** 

ការតំឡើង loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ចាប់ផ្តើមដោយនាំចូលបណ្ណាល័យចាំបាច់ដូចជា datasets, transformers, peft, trl និង torch។
រៀបចំការចុះបញ្ជីដើម្បីតាមដានដំណើរការបណ្តុះបណ្តាល។

អ្នកអាចជ្រើសរើសដែលនឹងបំលែងស្រទាប់ខ្លះៗដោយជំនួសពួកវាជាមួយគ្រឿងផ្សំដែលបង្កើតឡើងក្នុង loralib។ យើងគាំទ្រ nn.Linear, nn.Embedding និង nn.Conv2d តែប៉ុណ្ណោះសម្រាប់ពេលនេះ។ យើងក៏គាំទ្រម៉ូឌុល MergedLinear សម្រាប់ករណីដែល nn.Linear តែមួយតំណាងឱ្យស្រទាប់ច្រើនជាងមួយ ដូចជា នៅក្នុងការអនុវត្តខ្លះៗនៃការប្រមូលផ្តុំនៃការយកចេញ qkv (មើលចំណាំបន្ថែមសម្រាប់ព័ត៌មានបន្ថែម)។

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

មុនពេលចាប់ផ្តើមវដ្តបណ្តុះបណ្តាល សម្គាល់ថាគ្រឿងបន្លាស់ LoRA តែប៉ុណ្ណោះដែលអាចបណ្តុះបាន។

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ពេលរក្សាទុក checkpoint បង្កើត state_dict ដែលមានគ្រឿងបន្លាស់ LoRA តែប៉ុណ្ណោះ។

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

ពេលបញ្ចូល checkpoint ដោយប្រើ load_state_dict សូមប្រាកដថា បានកំណត់ strict=False។

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ឥឡូវនេះការបណ្តុះបណ្តាលអាចដំណើរការប្រក្រតី។

**ពិស្ដារ Hyperparameters** 

កំណត់ស until ប្រែឈ្មោះពីរចំនួន៖ training_config និង peft_config។ training_config រួមបញ្ចូល hyperparameters សម្រាប់ការបណ្តុះបណ្តាល ដូចជា អត្រារៀន, ទំហំបញ្ជាក់, និងកំណត់លក្ខណៈចុះបញ្ជី។

peft_config បញ្ជាក់ប៉ារ៉ាម៉ែត្រ​ដែលទាក់ទងនឹង LoRA ដូចជា rank, dropout, និងប្រភេទភារកិច្ច។

**ការផ្ទុកម៉ូដែល និង Tokenizer** 

បញ្ជាក់ផ្លូវទៅម៉ូដែល Phi-3 ដែលបានបណ្តុះរួច (ឧទាហរណ៍ "microsoft/Phi-3-mini-4k-instruct")។ កំណត់ការកម្មវិធីម៉ូដែល រួមទាំងការ​ប្រើ cache, ប្រភេទទិន្នន័យ (bfloat16 សម្រាប់ភាពច្បាស់លាស់ចម្រុះ), និងការអនុវត្តការយកចិត្តទុកដាក់។

**ការបណ្តុះបណ្តាល** 

សម្រួលម៉ូដែល Phi-3 ដោយប្រើសំណុំទិន្នន័យការសន្ទនាផ្ទាល់ខ្លួន។ ប្រើការកំណត់ LoRA ពី peft_config សម្រាប់ការប្ដូរប្រែមានប្រសិទ្ធភាព។ តាមដានដំណើរការបណ្តុះបណ្តាលដោយប្រើយុទ្ធសាស្ត្រចុះបញ្ជីដែលបានកំណត់។
ការវាយតម្លៃ និងការសន្សំ៖ វាយតម្លៃម៉ូដែលដែលបានសម្រួលរួច។
រក្សាទុក checkpoint ពេលបណ្តុះបណ្តាលសម្រាប់ការប្រើប្រាស់ក្រោយ។

**គំរូ**
- [សិក្សាបន្ថែមជាមួយសៀវភៅកំណត់ត្រាគំរូនេះ](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [ឧទាហរណ៍នៃគំរូ Python FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [ឧទាហរណ៍នៃ Hugging Face Hub Fine Tuning ជាមួយ LORA](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [ឧទាហរណ៍នៃកាតម៉ូដែល Hugging Face - គំរូ LORA Fine Tuning](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [ឧទាហរណ៍នៃ Hugging Face Hub Fine Tuning ជាមួយ QLORA](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្រៅពីការខិតខំរបស់យើងក្នុងការត្រូវតាមភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវផ្សេងៗ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានគិតថាជា ប្រភពផ្លូវការទីមួយ។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្តល់អាទិភាពក្នុងការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនមានការទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកពច្រឡំណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->