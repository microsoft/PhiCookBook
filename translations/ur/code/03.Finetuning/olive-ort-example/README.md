<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T15:17:58+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "ur"
}
-->
# Olive کے ذریعے Phi3 کو Fine-tune کریں

اس مثال میں آپ Olive کا استعمال کریں گے تاکہ:

1. LoRA adapter کو phrases کو Sad، Joy، Fear، Surprise میں classify کرنے کے لیے fine-tune کریں۔
1. adapter کے وزن base model میں merge کریں۔
1. ماڈل کو `int4` میں optimize اور quantize کریں۔

ہم آپ کو یہ بھی دکھائیں گے کہ ONNX Runtime (ORT) Generate API کا استعمال کرتے ہوئے fine-tuned ماڈل سے inference کیسے کریں۔

> **⚠️ Fine-tuning کے لیے، آپ کے پاس ایک مناسب GPU ہونا چاہیے - مثلاً A10، V100، A100۔**

## 💾 انسٹال کریں

ایک نیا Python virtual environment بنائیں (مثال کے طور پر، `conda` کا استعمال کرتے ہوئے):

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
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) میں ایک *workflow* ہے جس میں درج ذیل *passes* شامل ہیں:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

عموماً، یہ workflow یہ کرے گا:

1. Phi3 کو fine-tune کرے گا (150 steps کے لیے، جسے آپ تبدیل کر سکتے ہیں) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ڈیٹا کا استعمال کرتے ہوئے۔
1. LoRA adapter کے وزن base model میں merge کرے گا۔ اس سے آپ کو ONNX فارمیٹ میں ایک واحد ماڈل artifact ملے گا۔
1. Model Builder ماڈل کو ONNX runtime کے لیے optimize کرے گا *اور* ماڈل کو `int4` میں quantize کرے گا۔

workflow کو چلانے کے لیے، یہ کمانڈ چلائیں:

```bash
olive run --config phrase-classification.json
```

جب Olive مکمل ہو جائے، تو آپ کا optimized `int4` fine-tuned Phi3 ماڈل اس جگہ دستیاب ہوگا: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`۔

## 🧑‍💻 اپنے application میں fine-tuned Phi3 کو شامل کریں

ایپ چلانے کے لیے:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

جوابی پیغام ایک لفظی classification ہوگا (Sad/Joy/Fear/Surprise)۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔