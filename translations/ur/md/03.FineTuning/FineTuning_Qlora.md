<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-07T13:15:06+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ur"
}
-->
**Phi-3 کو QLoRA کے ساتھ فائن ٹیوننگ**

Microsoft کے Phi-3 Mini زبان کے ماڈل کو [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) کے ذریعے فائن ٹیون کرنا۔

QLoRA بات چیت کی سمجھ بوجھ اور جواب پیدا کرنے کی صلاحیت کو بہتر بنانے میں مدد دے گا۔

transformers اور bitsandbytes کے ساتھ 4bits میں ماڈلز لوڈ کرنے کے لیے، آپ کو accelerate اور transformers کو سورس سے انسٹال کرنا ہوگا اور یہ یقینی بنانا ہوگا کہ bitsandbytes لائبریری کا تازہ ترین ورژن موجود ہو۔

**نمونے**
- [اس سیمپل نوٹ بک کے ساتھ مزید جانیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning سیمپل کی مثال](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA کے ساتھ Hugging Face Hub Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA کے ساتھ Hugging Face Hub Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ہم ذمہ دار نہیں ہیں۔