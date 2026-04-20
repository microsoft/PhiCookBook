# កំណត់ត្រា Phi3 ជាមួយ Olive

នៅក្នុងឧទាហរណ៍នេះ អ្នកនឹងប្រើ Olive ដើម្បី៖

1. កំណត់ត្រា LoRA adapter ដើម្បីចាត់ថ្នាក់ឃ្លា ទៅជា Sad, Joy, Fear, Surprise។
1. បញ្ចូលទំងន់ adapter ទៅក្នុងម៉ូឌែលមូលដ្ឋាន។
1. បង្កើតសមត្ថភាព និង បំលែងម៉ូឌែលទៅជា `int4`។

យើងនឹងបង្ហាញអ្នកថា តើធ្វើដូចម្តេចដើម្បីធ្វើ inference លើម៉ូឌែលកំណត់ត្រា ដោយប្រើ ONNX Runtime (ORT) Generate API។

> **⚠️ សម្រាប់ការកំណត់ត្រា អ្នកត្រូវតែមាន GPU សមរម្យមួយចំនួន - ឧទាហរណ៍ A10, V100, A100។**

## 💾 ដំឡើង

បង្កើតបរិយាកាស Python virtual ថ្មីមួយ (ឧទាហរណ៍ ដោយប្រើ `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

បន្ទាប់ពីនេះតំឡើង Olive និងការពឹងផ្អែកសម្រាប់ដំណើរការកំណត់ត្រា៖

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 កំណត់ត្រា Phi3 ជាមួយ Olive
[ឯកសារ ការកំណត់កំណត់រចនាសម្ព័ន្ធ Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) មាន *workflow* ដែលមាន *passes* ដូចខាងក្រោម៖

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

នៅទ្រង់ទ្រាយខ្ពស់ Workflow នេះនឹង៖

1. កំណត់ត្រា Phi3 (សម្រាប់ជំហាន 150 ដែលអ្នកអាចផ្លាស់ប្តូរបាន) ដោយប្រើទិន្នន័យ [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json)។
1. បញ្ចូលទំងន់ LoRA adapter ទៅក្នុងម៉ូឌែលមូលដ្ឋាន។ នេះនឹងផ្តល់ឱ្យអ្នកនូវ single model artifact ទ្រង់ទ្រង់ ONNX។
1. Model Builder នឹងបង្កើតសមត្ថភាពម៉ូឌែលសម្រាប់ ONNX runtime *និង* បំលែងម៉ូឌែលទៅជា `int4`។

ដើម្បីរត់ workflow, បញ្ចូលពាក្យបញ្ជា៖

```bash
olive run --config phrase-classification.json
```

នៅពេលដែល Olive បានបញ្ចប់ នេះម៉ូឌែល Phi3 កំណត់ត្រា `int4` ដែលបានបង្កើតសមត្ថភាពរួចហើយ មាននៅ៖ `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`។

## 🧑‍💻 បញ្ចូល Phi3 កំណត់ត្រា ចូលក្នុងកម្មវិធីរបស់អ្នក 

ដើម្បីរត់កម្មវិធី៖

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ចម្លើយនេះគួរតែក្លាយជាការចាត់ថ្នាក់ពាក្យតែមួយ (Sad/Joy/Fear/Surprise)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងព្យាយាមរក្សាភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវបាន។ ឯកសារដើមជាភាសាទីមួយគឺគួរត្រូវបានចាត់ទុកជា ប្រភពអាជ្ញាធរ។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឲ្យមានការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->