<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98eb289883c5e181a74e72a59e1ddc6d",
  "translation_date": "2025-04-03T08:06:58+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "ur"
}
-->
# **Phi-3 کو لورا کے ساتھ فائن ٹیون کرنا**

مائیکروسافٹ کے Phi-3 Mini لینگویج ماڈل کو [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) کا استعمال کرتے ہوئے کسٹم چیٹ انسٹرکشن ڈیٹاسیٹ پر فائن ٹیون کرنا۔

لورا گفتگو کو سمجھنے اور جواب دینے کی صلاحیت کو بہتر بنانے میں مدد کرے گا۔

## Phi-3 Mini کو فائن ٹیون کرنے کے لیے مرحلہ وار گائیڈ:

**امپورٹس اور سیٹ اپ**

loralib انسٹال کرنا

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ضروری لائبریریاں جیسے کہ datasets، transformers، peft، trl، اور torch کو امپورٹ کرنے سے شروع کریں۔ ٹریننگ پروسیس کو ٹریک کرنے کے لیے لاگنگ سیٹ کریں۔

آپ کچھ لیئرز کو ایڈجسٹ کرنے کا انتخاب کر سکتے ہیں، انہیں لورا لائبریری میں دی گئی متبادل کے ساتھ تبدیل کر کے۔ فی الحال ہم صرف nn.Linear، nn.Embedding، اور nn.Conv2d کو سپورٹ کرتے ہیں۔ ہم MergedLinear کو بھی سپورٹ کرتے ہیں، جو ان کیسز میں استعمال ہوتا ہے جہاں ایک nn.Linear ایک سے زیادہ لیئرز کو ظاہر کرتا ہے، جیسے کہ کچھ attention qkv پروجیکشن کی امپلیمنٹیشن میں (مزید معلومات کے لیے Additional Notes دیکھیں)۔

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

ٹریننگ لوپ شروع ہونے سے پہلے، صرف LoRA پیرامیٹرز کو ٹرین ایبل کے طور پر مارک کریں۔

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

چیک پوائنٹ محفوظ کرتے وقت، ایسا state_dict بنائیں جو صرف LoRA پیرامیٹرز کو شامل کرے۔

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

چیک پوائنٹ لوڈ کرتے وقت، load_state_dict کا استعمال کریں اور strict=False سیٹ کریں۔

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اب ٹریننگ معمول کے مطابق جاری رہ سکتی ہے۔

**ہائپر پیرامیٹرز**

دو ڈکشنریز ڈیفائن کریں: training_config اور peft_config۔ training_config میں ٹریننگ کے لیے ہائپر پیرامیٹرز شامل ہوتے ہیں، جیسے کہ learning rate، batch size، اور logging سیٹنگز۔

peft_config میں LoRA سے متعلق پیرامیٹرز شامل ہوتے ہیں، جیسے کہ rank، dropout، اور task type۔

**ماڈل اور ٹوکنائزر لوڈ کرنا**

پری ٹرینڈ Phi-3 ماڈل کا راستہ بتائیں (مثال کے طور پر، "microsoft/Phi-3-mini-4k-instruct")۔ ماڈل سیٹنگز کو کنفیگر کریں، جن میں cache کا استعمال، data type (mixed precision کے لیے bfloat16)، اور attention امپلیمنٹیشن شامل ہیں۔

**ٹریننگ**

Phi-3 ماڈل کو کسٹم چیٹ انسٹرکشن ڈیٹاسیٹ کا استعمال کرتے ہوئے فائن ٹیون کریں۔ peft_config سے LoRA سیٹنگز کا استعمال کریں تاکہ موثر ایڈاپٹیشن حاصل ہو سکے۔ ٹریننگ پروسیس کو دی گئی لاگنگ اسٹریٹیجی کے ذریعے مانیٹر کریں۔

**ایویلیوایشن اور محفوظ کرنا**

فائن ٹیون کیے گئے ماڈل کا ایویلیوایشن کریں۔ ٹریننگ کے دوران چیک پوائنٹس محفوظ کریں تاکہ بعد میں استعمال ہو سکیں۔

**نمونے**
- [اس نمونہ نوٹ بک کے ذریعے مزید سیکھیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python فائن ٹیوننگ کا مثال](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub پر لورا کے ساتھ فائن ٹیوننگ کا مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face ماڈل کارڈ - لورا فائن ٹیوننگ کا مثال](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub پر QLORA کے ساتھ فائن ٹیوننگ کا مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہوسکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔