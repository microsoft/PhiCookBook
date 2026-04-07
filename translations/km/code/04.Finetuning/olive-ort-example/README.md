# ប្រើ Olive ដើម្បីសម្រួល Phi3

ក្នុងឧទាហរណ៍នេះ អ្នកនឹងប្រើ Olive ដើម្បី៖

1. សម្រួល LoRA adapter ឲ្យចាត់ថ្នាក់ប្រយោគទៅជា Sad, Joy, Fear, Surprise។
1. បញ្ចូលទម្ងន់ adapter ទៅក្នុងម៉ូដែលមូលដ្ឋាន។
1. បន្ធាក់ និងធ្វើ Quantize ម៉ូដែលទៅជា `int4`។

យើងនឹងបង្ហាញអ្នកពីរបៀបប្រើម៉ូដែលដែលបានសម្រួលដោយប្រើ ONNX Runtime (ORT) Generate API ផងដែរ។

> **⚠️ សម្រាប់ការសម្រួល អ្នកត្រូវមាន GPU ដែលសាកសម - ឧទាហរណ៍ ដូចជា A10, V100, A100។**

## 💾 តំឡើង

បង្កើតបរិស្ថាន Python វីរុឌ (virtual environment) ថ្មី (ឧទាហរណ៍ ប្រើ `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

បន្ទាប់មក តំឡើង Olive និងការពឹងផ្អែកសម្រាប់បញ្ជីសម្រួល៖

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 សម្រួល Phi3 ដោយប្រើ Olive
ឯកសារកំណត់រចនាសម្ព័ន្ធ [Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) មាន *workflow* ដែលមាន *passes* ដូចតទៅ៖

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

នៅកម្រិតខ្ពស់ workflow នេះនឹង៖

1. សម្រួល Phi3 (សម្រាប់ជំហាន 150 ដែលអ្នកអាចផ្លាស់ប្តូរ) ប្រើទិន្នន័យ [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)។
1. បញ្ចូលទម្ងន់ adapter LoRA ទៅក្នុងម៉ូដែលមូលដ្ឋាន។ នេះនឹងផ្តល់ឱ្យអ្នកម៉ូដែលតែមួយជា artifacts នៅទ្រង់ទ្រាយ ONNX។
1. Model Builder នឹងធ្វើបច្ចុប្បន្នភាពម៉ូដែលសម្រាប់ ONNX runtime ហើយធ្វើ quantize ម៉ូដែលទៅជា `int4`។

ដើម្បីរត់ workflow សូមចាត់បញ្ជា៖

```bash
olive run --config phrase-classification.json
```

ពេល Olive បានបញ្ចប់ ម៉ូដែល Phi3 ដែលបានសម្រួល និងត្រូវបានបន្ធាក់ `int4` នឹងមាននៅក្នុង៖ `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`។

## 🧑‍💻 រួមបញ្ចូល Phi3 ដែលបានសម្រួលទៅក្នុងកម្មវិធីរបស់អ្នក

ដើម្បីរត់កម្មវិធី៖

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ចម្លើយនេះគួរតែជាចំណាត់ថ្នាក់ពាក្យតែមួយសម្រាប់ប្រយោគដែលបានផ្តល់ (Sad/Joy/Fear/Surprise)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងព្យាយាមរកភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការមិនត្រឹមត្រូវ។ ឯកសារដើមដែលមានក្នុងភាសាមាតុភូមិគួរត្រូវបានពិចារណាជាប្រភពដែលមានសិទ្ធិលើកញ្ចប់ព័ត៌មាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនិងការបកប្រែខុសៗណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->