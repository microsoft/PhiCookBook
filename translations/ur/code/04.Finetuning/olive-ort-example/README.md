<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T15:15:17+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ur"
}
-->
# Olive کے ذریعے Phi3 کو Fine-tune کریں

اس مثال میں آپ Olive استعمال کریں گے تاکہ:

1. LoRA adapter کو fine-tune کریں تاکہ جملوں کو Sad, Joy, Fear, Surprise میں classify کیا جا سکے۔
1. adapter کے وزنوں کو base model میں merge کریں۔
1. ماڈل کو optimize اور Quantize کریں `int4` میں۔

ہم آپ کو دکھائیں گے کہ fine-tuned ماڈل کو ONNX Runtime (ORT) Generate API کے ذریعے کیسے inference کیا جائے۔

> **⚠️ Fine-tuning کے لیے، آپ کے پاس مناسب GPU ہونا ضروری ہے - مثلاً A10, V100, A100۔**

## 💾 انسٹال کریں

ایک نیا Python virtual environment بنائیں (مثلاً `conda` استعمال کرتے ہوئے):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

اس کے بعد، Olive اور fine-tuning workflow کی dependencies انسٹال کریں:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive کے ذریعے Phi3 کو Fine-tune کریں
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) میں ایک *workflow* شامل ہے جس میں درج ذیل *passes* ہیں:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

مجموعی طور پر، یہ workflow یہ کرے گا:

1. Phi3 کو fine-tune کرے گا (150 steps کے لیے، جسے آپ تبدیل کر سکتے ہیں) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) ڈیٹا استعمال کرتے ہوئے۔
1. LoRA adapter کے وزن base model میں merge کرے گا۔ اس سے آپ کو ONNX فارمیٹ میں ایک واحد ماڈل artifact ملے گا۔
1. Model Builder ماڈل کو ONNX runtime کے لیے optimize کرے گا *اور* ماڈل کو `int4` میں quantize کرے گا۔

Workflow چلانے کے لیے، یہ کمانڈ چلائیں:

```bash
olive run --config phrase-classification.json
```

جب Olive مکمل ہو جائے، تو آپ کا optimized `int4` fine-tuned Phi3 ماڈل اس جگہ دستیاب ہوگا: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`۔

## 🧑‍💻 اپنے ایپلیکیشن میں fine-tuned Phi3 کو شامل کریں

ایپ چلانے کے لیے:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

جوابی جواب جملے کی ایک لفظی درجہ بندی ہوگی (Sad/Joy/Fear/Surprise)۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔