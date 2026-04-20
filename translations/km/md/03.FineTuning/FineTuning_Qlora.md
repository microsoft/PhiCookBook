**ការតម្លើង Phi-3 ជាថ្មីដោយប្រើ QLoRA**

ការតម្លើងម៉ូដែលភាសា Phi-3 Mini របស់ Microsoft ដោយប្រើ [QLoRA (ការកែប្រែ Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)។

QLoRA នឹងជួយបង្កើនការយល់ដឹងនៃការជជែកសន្ទនា និងការផលិតឆ្លើយតប។

ដើម្បីផ្ទុកម៉ូដែលជាលេខ 4bits ជាមួយ transformers និង bitsandbytes អ្នកត្រូវតែដំឡើង accelerate និង transformers ពីប្រភព និងធានាថាអ្នកមានកំណែថ្មីបំផុតនៃបណ្ណាល័យ bitsandbytes។

**គំរូ**
- [សិក្សាបន្ថែមជាមួយកំណត់ត្រាគំរូនេះ](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [ឧទាហរណ៍នៃគំរូ Python FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [ឧទាហរណ៍នៃការតម្លើង Fine Tuning ជាមួយ LORA នៅលើ Hugging Face Hub](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [ឧទាហរណ៍នៃការតម្លើង Fine Tuning ជាមួយ QLORA នៅលើ Hugging Face Hub](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំប្រាថ្នារកនៅភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វយ័តអាចមានកំហុស ឬការមិនត្រឹមត្រូវ។ ឯកសារដើមនៅភាសាម្ចាស់របស់វាគួរត្រូវបានគេសង្កេតប្រភពដែលមានសុពលភាពអភិបាល។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សអ្នកជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសខាតណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->