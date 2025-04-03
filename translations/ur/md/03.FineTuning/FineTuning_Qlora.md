<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f0858a9f2cc1889ab0e90cb9c63c044",
  "translation_date": "2025-04-03T08:19:54+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "ur"
}
-->
**Phi-3 کو QLoRA کے ساتھ بہتر بنانا**

Microsoft کے Phi-3 Mini لینگویج ماڈل کو [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) کے ذریعے بہتر بنانا۔

QLoRA گفتگو کو سمجھنے اور جواب دینے کی صلاحیت کو بہتر بنانے میں مدد کرے گا۔

ماڈلز کو 4bits میں transformers اور bitsandbytes کے ساتھ لوڈ کرنے کے لیے، آپ کو accelerate اور transformers کو سورس سے انسٹال کرنا ہوگا اور یہ یقینی بنانا ہوگا کہ آپ کے پاس bitsandbytes لائبریری کا جدید ترین ورژن موجود ہو۔

**نمونے**
- [اس نمونہ نوٹ بک کے ساتھ مزید جانیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning کا مثال](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub پر LORA کے ساتھ Fine Tuning کا مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub پر QLORA کے ساتھ Fine Tuning کا مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہوسکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔