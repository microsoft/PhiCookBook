**Phi-3 کو QLoRA کے ساتھ فائن ٹیون کرنا**

Microsoft کے Phi-3 Mini زبان کے ماڈل کو [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) کے ذریعے فائن ٹیون کرنا۔

QLoRA مکالماتی سمجھ بوجھ اور جواب سازی کو بہتر بنانے میں مدد دے گا۔

transformers اور bitsandbytes کے ساتھ 4bits میں ماڈلز لوڈ کرنے کے لیے، آپ کو accelerate اور transformers کو سورس سے انسٹال کرنا ہوگا اور یہ یقینی بنانا ہوگا کہ bitsandbytes لائبریری کا تازہ ترین ورژن موجود ہو۔

**نمونے**
- [اس سیمپل نوٹ بک کے ساتھ مزید جانیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning سیمپل کی مثال](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub پر LORA کے ساتھ Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub پر QLORA کے ساتھ Fine Tuning کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔