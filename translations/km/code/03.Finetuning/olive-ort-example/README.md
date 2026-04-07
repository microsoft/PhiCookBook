# បង្រួមបង្រួល Phi3 ប្រើ Olive

នៅក្នុងឧទាហរណ៍នេះ អ្នក​នឹងប្រើ Olive ដើម្បី៖

1. បង្រួមបង្រួល LoRA adapter ដើម្បីចាត់ថ្នាក់ប្រយោគទៅជា Sad, Joy, Fear, Surprise។
1. លាយបញ្ចូលទម្ងន់ adapter ទៅក្នុងម៉ូឌែលមូលដ្ឋាន។
1. បំពាក់ និងបញ្ចូលគណករណ៍ដល់ម៉ូឌែលជា `int4`។

យើងក៏នឹងបង្ហាញអ្នកពីរបៀបប្រើម៉ូឌែលដែលបានបង្រួមបង្រួលជាមួយ ONNX Runtime (ORT) Generate API។

> **⚠️ សម្រាប់ការបង្រួមបង្រួល អ្នកត្រូវតែមាន GPU ដែលសមរម្យ - លើកដូចជា A10, V100, A100។**

## 💾 ដំឡើង

បង្កើតបរិវេណ Python ថ្មី (ឧត្តមករណ៍ `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

បន្ទាប់មក ដំឡើង Olive និងផ្នែកអាស័យដ្ឋានសម្រាប់ដំណើរការបង្រួមបង្រួល៖

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 បង្រួមបង្រួល Phi3 ប្រើ Olive
[ឯកសារកំណត់រចនាសម្ព័ន្ធ Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) មាន *workflow* ជាមួយនឹង *passes* ខាងក្រោម៖

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

នៅជាន់ខ្ពស់ ការប្រតិបត្តិការនេះនឹង៖

1. បង្រួមបង្រួល Phi3 (សម្រាប់ជំហាន 150 ដែលអ្នកអាចកែប្រែបាន) ប្រើទិន្នន័យ [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json)។
1. លាយបញ្ចូលទម្ងន់ adapter LoRA ទៅម៉ូឌែលមូលដ្ឋាន។ នេះនឹងផ្តល់ឲ្យអ្នកនូវមួយម៉ូឌែល ONNX តែមួយគត់។
1. Model Builder នឹងបង្កើតម៉ូឌែលឲ្យមានប្រសិទ្ធភាពសម្រាប់ ONNX runtime *និង* បញ្ចូលគណករណ៍ទៅ `int4`។

ដើម្បីបើកដំណើរការ workflow សូមរត់៖

```bash
olive run --config phrase-classification.json
```

ពេលដែល Olive បានបញ្ចប់ ម៉ូឌែល Phi3 បង្រួមបង្រួល `int4` មាននៅក្នុង៖ `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`។

## 🧑‍💻 បញ្ចូល Phi3 ដែលបានបង្រួមបង្រួលទៅក្នុងកម្មវិធីរបស់អ្នក

ដើម្បីបើកកម្មវិធី៖

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ការឆ្លើយតបនេះគួរឱ្យមានកម្រិតការចាត់ថ្នាក់ពាក្យតែមួយ (Sad/Joy/Fear/Surprise)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**ៈ  
ឯកសារនេះបានប្រែសម្រួលដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំព្យាយាមឲ្យបានត្រឹមត្រូវ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការខកខានខ្លះៗ។ ឯកសារដើមជាភាសាទ្រព្យសម្បត្តិគួរត្រូវបានគេមើលឃើញថាជា ប្រភពផ្ដល់ព័ត៌មានប្រកបដោយសំខាន់។ សម្រាប់ព័ត៌មានសំខាន់ៗ នេះត្រូវបนะนำឲ្យបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបញ្ចេញភាពខុសឆ្គងណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->