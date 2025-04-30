<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-03T06:18:25+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ur"
}
-->
# اولیو کے ذریعے Phi3 کو فائن ٹیون کریں

اس مثال میں، آپ اولیو کا استعمال کریں گے:

1. LoRA ایڈاپٹر کو فائن ٹیون کریں تاکہ جملوں کو Sad, Joy, Fear, Surprise میں تقسیم کیا جا سکے۔
1. ایڈاپٹر کے وزن کو بیس ماڈل میں ضم کریں۔
1. ماڈل کو `int4` میں بہتر اور کوانٹائز کریں۔

ہم آپ کو یہ بھی دکھائیں گے کہ ONNX Runtime (ORT) Generate API کا استعمال کرتے ہوئے فائن ٹیونڈ ماڈل پر انفرینس کیسے کریں۔

> **⚠️ فائن ٹیوننگ کے لیے، آپ کو ایک مناسب GPU دستیاب ہونا ضروری ہے - جیسے A10, V100, A100۔**

## 💾 انسٹال کریں

ایک نیا Python ورچوئل ماحول بنائیں (مثال کے طور پر، `conda` استعمال کرتے ہوئے):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

اس کے بعد، اولیو اور فائن ٹیوننگ ورک فلو کے لیے ضروری ڈپینڈنسیز انسٹال کریں:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 اولیو کے ذریعے Phi3 کو فائن ٹیون کریں
[اولیو کنفیگریشن فائل](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) میں ایک *ورک فلو* موجود ہے جس میں درج ذیل *پاسز* شامل ہیں:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

اعلی سطح پر، یہ ورک فلو درج ذیل کام کرے گا:

1. Phi3 کو فائن ٹیون کرے گا (150 مراحل کے لیے، جسے آپ تبدیل کر سکتے ہیں) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) ڈیٹا کا استعمال کرتے ہوئے۔
1. LoRA ایڈاپٹر کے وزن کو بیس ماڈل میں ضم کرے گا۔ یہ آپ کو ONNX فارمیٹ میں ایک واحد ماڈل آرٹیفیکٹ فراہم کرے گا۔
1. ماڈل بلڈر ماڈل کو ONNX runtime کے لیے بہتر بنائے گا *اور* ماڈل کو `int4` میں کوانٹائز کرے گا۔

ورک فلو کو چلانے کے لیے، درج ذیل کمانڈ چلائیں:

```bash
olive run --config phrase-classification.json
```

جب اولیو مکمل ہو جائے گا، تو آپ کا بہتر `int4` فائن ٹیونڈ Phi3 ماڈل یہاں دستیاب ہوگا: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`۔

## 🧑‍💻 فائن ٹیونڈ Phi3 کو اپنی ایپلیکیشن میں شامل کریں 

ایپ چلانے کے لیے:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

یہ جواب جملے کی ایک واحد ورڈ کلاسفیکیشن ہونا چاہیے (Sad/Joy/Fear/Surprise)۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔