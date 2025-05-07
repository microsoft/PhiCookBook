<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-07T13:30:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ur"
}
-->
# **Lora کے ساتھ Phi-3 کو Fine-tune کرنا**

Microsoft کے Phi-3 Mini زبان کے ماڈل کو [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) کا استعمال کرتے ہوئے ایک کسٹم چیٹ انسٹرکشن ڈیٹاسیٹ پر Fine-tune کرنا۔

LORA بات چیت کی سمجھ اور جواب دینے کی صلاحیت کو بہتر بنانے میں مدد دے گا۔

## Phi-3 Mini کو Fine-tune کرنے کے مرحلہ وار طریقہ کار:

**Imports اور Setup**

loralib انسٹال کرنا

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ضروری لائبریریز جیسے datasets, transformers, peft, trl, اور torch کو import کرکے شروع کریں۔
ٹریننگ کے عمل کو ٹریک کرنے کے لیے logging سیٹ اپ کریں۔

آپ کچھ layers کو loralib میں موجود متبادل سے بدل کر adapt کر سکتے ہیں۔ فی الحال ہم صرف nn.Linear, nn.Embedding، اور nn.Conv2d کو سپورٹ کرتے ہیں۔ ہم MergedLinear کو بھی سپورٹ کرتے ہیں جہاں ایک nn.Linear ایک سے زیادہ layers کی نمائندگی کرتا ہے، جیسے کہ attention qkv projection کی کچھ implementations میں (مزید معلومات کے لیے Additional Notes دیکھیں)۔

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

ٹریننگ لوپ شروع ہونے سے پہلے صرف LoRA parameters کو trainable کے طور پر نشان زد کریں۔

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

چیک پوائنٹ محفوظ کرتے وقت، ایک state_dict تیار کریں جس میں صرف LoRA parameters شامل ہوں۔

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict کا استعمال کرتے ہوئے چیک پوائنٹ لوڈ کرتے وقت strict=False سیٹ کرنا یقینی بنائیں۔

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اب ٹریننگ معمول کے مطابق جاری رہ سکتی ہے۔

**Hyperparameters**

دو dictionaries define کریں: training_config اور peft_config۔ training_config میں ٹریننگ کے hyperparameters شامل ہیں، جیسے learning rate، batch size، اور logging کی ترتیبات۔

peft_config میں LoRA سے متعلق parameters شامل ہیں، جیسے rank، dropout، اور task type۔

**Model اور Tokenizer لوڈ کرنا**

پری ٹرینڈ Phi-3 ماڈل کا path بتائیں (مثلاً "microsoft/Phi-3-mini-4k-instruct")۔ ماڈل کی ترتیبات کنفیگر کریں، جن میں cache کا استعمال، data type (mixed precision کے لیے bfloat16)، اور attention implementation شامل ہیں۔

**Training**

Phi-3 ماڈل کو کسٹم چیٹ انسٹرکشن ڈیٹاسیٹ کے ساتھ Fine-tune کریں۔ مؤثر adaptation کے لیے peft_config سے LoRA کی ترتیبات استعمال کریں۔ ٹریننگ کی پیش رفت کو مخصوص logging strategy کے ذریعے مانیٹر کریں۔

Evaluation اور Saving: Fine-tuned ماڈل کا جائزہ لیں۔ ٹریننگ کے دوران چیک پوائنٹس محفوظ کریں تاکہ بعد میں استعمال ہو سکیں۔

**Samples**
- [اس sample notebook کے ذریعے مزید جانیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning Sample کی مثال](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA کے ساتھ Hugging Face Hub Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Card کی مثال - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA کے ساتھ Hugging Face Hub Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا کمی بیشی ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔