<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:45+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ar"
}
-->
**تخصيص نموذج Phi-3 باستخدام QLoRA**

تخصيص نموذج اللغة Phi-3 Mini من مايكروسوفت باستخدام [QLoRA (التكيف الكمي منخفض الرتبة)](https://github.com/artidoro/qlora).

سيساعد QLoRA في تحسين فهم المحادثات وتوليد الردود.

لتحميل النماذج بدقة 4 بت باستخدام transformers و bitsandbytes، يجب تثبيت accelerate و transformers من المصدر والتأكد من أن لديك أحدث إصدار من مكتبة bitsandbytes.

**عينات**
- [تعرف أكثر من خلال هذا الدفتر التفاعلي](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [مثال على تخصيص باستخدام بايثون](../../../../code/03.Finetuning/FineTrainingScript.py)
- [مثال على تخصيص من خلال Hugging Face Hub باستخدام LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [مثال على تخصيص من خلال Hugging Face Hub باستخدام QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.