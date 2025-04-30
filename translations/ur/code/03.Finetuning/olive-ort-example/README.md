<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-03T06:15:53+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ur"
}
-->
# فائن ٹیون Phi3 اولیو کے ذریعے

اس مثال میں آپ اولیو استعمال کریں گے:

1. LoRA ایڈاپٹر کو فائن ٹیون کریں تاکہ جملوں کو Sad، Joy، Fear، Surprise میں تقسیم کیا جا سکے۔
1. ایڈاپٹر کے وزن کو بیس ماڈل میں ضم کریں۔
1. ماڈل کو `int4` میں آپٹمائز اور کوانٹائز کریں۔

ہم آپ کو یہ بھی دکھائیں گے کہ ONNX Runtime (ORT) Generate API کا استعمال کرتے ہوئے فائن ٹیون شدہ ماڈل پر کیسے انفیرینس کریں۔

> **⚠️ فائن ٹیوننگ کے لیے، آپ کو ایک مناسب GPU دستیاب ہونا چاہیے - مثال کے طور پر، A10، V100، A100۔**

## 💾 انسٹال کریں

ایک نیا Python ورچوئل ماحول بنائیں (مثال کے طور پر، `conda` استعمال کرتے ہوئے):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

اس کے بعد، اولیو اور فائن ٹیوننگ ورک فلو کے لیے ضروری ڈپینڈینسیز انسٹال کریں:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 اولیو کے ذریعے Phi3 فائن ٹیون کریں
[اولیو کنفیگریشن فائل](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ایک *ورک فلو* پر مشتمل ہے جس میں درج ذیل *پاسز* ہیں:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

اعلی سطح پر، یہ ورک فلو درج ذیل کام کرے گا:

1. Phi3 کو فائن ٹیون کریں (150 قدموں کے لیے، جسے آپ تبدیل کر سکتے ہیں) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ڈیٹا استعمال کرتے ہوئے۔
1. LoRA ایڈاپٹر کے وزن کو بیس ماڈل میں ضم کریں۔ اس سے آپ کو ONNX فارمیٹ میں ایک سنگل ماڈل آرٹیفیکٹ ملے گا۔
1. ماڈل بلڈر ماڈل کو ONNX runtime کے لیے آپٹمائز کرے گا *اور* ماڈل کو `int4` میں کوانٹائز کرے گا۔

ورک فلو کو چلانے کے لیے، درج ذیل کمانڈ چلائیں:

```bash
olive run --config phrase-classification.json
```

جب اولیو مکمل ہو جائے، تو آپ کا آپٹمائزڈ `int4` فائن ٹیون شدہ Phi3 ماڈل یہاں دستیاب ہوگا: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`۔

## 🧑‍💻 فائن ٹیون شدہ Phi3 کو اپنی ایپلیکیشن میں شامل کریں 

ایپ چلانے کے لیے:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

یہ رسپانس جملے کی سنگل ورڈ کلاسیفیکیشن ہوگی (Sad/Joy/Fear/Surprise)۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔