<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:28:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ur"
}
-->
# **Lora کے ساتھ Phi-3 کی فائن ٹیوننگ**

Microsoft کے Phi-3 Mini زبان کے ماڈل کو [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) کے ذریعے ایک کسٹم چیٹ انسٹرکشن ڈیٹاسیٹ پر فائن ٹیون کرنا۔

LORA مکالماتی سمجھ بوجھ اور جواب کی تخلیق کو بہتر بنانے میں مدد دے گا۔

## Phi-3 Mini کو فائن ٹیون کرنے کا مرحلہ وار طریقہ:

**درآمدات اور سیٹ اپ**

loralib کی تنصیب

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ضروری لائبریریز جیسے datasets, transformers, peft, trl, اور torch کو درآمد کرنا شروع کریں۔  
ٹریننگ کے عمل کو ٹریک کرنے کے لیے لاگنگ سیٹ کریں۔

آپ کچھ layers کو loralib میں موجود متبادل سے تبدیل کر کے ایڈاپٹ کر سکتے ہیں۔ فی الحال ہم صرف nn.Linear, nn.Embedding, اور nn.Conv2d کو سپورٹ کرتے ہیں۔ ہم MergedLinear کو بھی سپورٹ کرتے ہیں جہاں ایک nn.Linear ایک سے زیادہ layers کی نمائندگی کرتا ہے، جیسا کہ attention qkv projection کی کچھ implementations میں ہوتا ہے (مزید معلومات کے لیے Additional Notes دیکھیں)۔

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

ٹریننگ لوپ شروع ہونے سے پہلے، صرف LoRA کے پیرامیٹرز کو trainable کے طور پر نشان زد کریں۔

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

چیک پوائنٹ محفوظ کرتے وقت، ایک state_dict بنائیں جس میں صرف LoRA کے پیرامیٹرز شامل ہوں۔

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict استعمال کرتے ہوئے چیک پوائنٹ لوڈ کرتے وقت، strict=False سیٹ کرنا یقینی بنائیں۔

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اب ٹریننگ معمول کے مطابق جاری رکھی جا سکتی ہے۔

**ہائپر پیرامیٹرز**

دو dictionaries define کریں: training_config اور peft_config۔ training_config میں ٹریننگ کے ہائپر پیرامیٹرز شامل ہیں، جیسے learning rate، batch size، اور logging کی ترتیبات۔

peft_config میں LoRA سے متعلق پیرامیٹرز شامل ہیں جیسے rank، dropout، اور task type۔

**ماڈل اور ٹوکنائزر لوڈ کرنا**

پری ٹرینڈ Phi-3 ماڈل کا راستہ بتائیں (مثلاً "microsoft/Phi-3-mini-4k-instruct")۔ ماڈل کی ترتیبات کو configure کریں، جن میں cache کا استعمال، data type (mixed precision کے لیے bfloat16)، اور attention کی implementation شامل ہیں۔

**ٹریننگ**

کسٹم چیٹ انسٹرکشن ڈیٹاسیٹ کے ساتھ Phi-3 ماڈل کو فائن ٹیون کریں۔ مؤثر adaptation کے لیے peft_config سے LoRA کی ترتیبات استعمال کریں۔ مخصوص لاگنگ حکمت عملی کے ذریعے ٹریننگ کی پیش رفت پر نظر رکھیں۔  
تشخیص اور محفوظ کرنا: فائن ٹیون شدہ ماڈل کا جائزہ لیں۔  
ٹریننگ کے دوران چیک پوائنٹس محفوظ کریں تاکہ بعد میں استعمال کیے جا سکیں۔

**نمونے**  
- [اس سیمپل نوٹ بک کے ساتھ مزید جانیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python FineTuning سیمپل کی مثال](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub پر LORA کے ساتھ Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face ماڈل کارڈ کی مثال - LORA Fine Tuning سیمپل](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub پر QLORA کے ساتھ Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔