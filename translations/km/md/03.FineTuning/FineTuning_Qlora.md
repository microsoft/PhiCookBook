**ការបណ្តុះបណ្តាលឲ្យមានភាពម៉ឺងម៉ាត់ Phi-3 ជាមួយ QLoRA**

ការបណ្តុះបណ្តាលម៉ូដែលភាសា Phi-3 Mini របស់ Microsoft ដោយប្រើ [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)។

QLoRA នឹងជួយបង្កើនការយល់ដឹងក្នុងកិច្ចសន្ទនានិងការបង្កើតចម្លើយ។

ដើម្បីផ្ទុកម៉ូដែលនៅក្នុង 4bits ជាមួយ transformers និង bitsandbytes អ្នកត្រូវតែដំឡើង accelerate និង transformers ពីប្រភព ហើយធានាឱ្យមានកំណែថ្មីនៃបណ្ណាល័យ bitsandbytes។

**គំរូ**
- [សូម្បីតែដឹងបន្ថែមជាមួយសៀវភៅកំណត់ត្រាគំរូនេះ](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [គំរូ Python FineTuning ตัวอย่าง](../../../../code/03.Finetuning/FineTrainingScript.py)
- [គំរូ Hugging Face Hub គាំទ្រការបណ្តុះបណ្តាល LORA](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [គំរូ Hugging Face Hub គាំទ្រការបណ្តុះបណ្តាល QLORA](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបម្លែងភាសាជាភាសាខ្មែរដោយប្រើសេវាកម្មបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator) ។ ខណៈពេលដែលយើងខិតខំរកភាពច្បាស់លាស់ សូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬប្រហែលខុស។ ឯកសារដើមនៅក្នុងភាសាដែលមានដើមគួរត្រូវបានគេយកជាទិន្នន័យផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបម្លែងភាសាដោយអ្នកជំនាញមនុស្សខាងវិជ្ជាជីវៈត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសឡើងពីការប្រើប្រាស់ការបម្លែងភាសានេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->