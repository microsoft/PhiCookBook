<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-07T10:33:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ar"
}
-->
**ضبط دقيق لـ Phi-3 باستخدام QLoRA**

ضبط دقيق لنموذج اللغة Phi-3 Mini من مايكروسوفت باستخدام [QLoRA (التكيف الكمومي منخفض الرتبة)](https://github.com/artidoro/qlora).

QLoRA ستساعد في تحسين فهم المحادثات وتوليد الردود.

لتحميل النماذج بدقة 4 بت باستخدام transformers و bitsandbytes، يجب عليك تثبيت accelerate و transformers من المصدر والتأكد من أن لديك أحدث إصدار من مكتبة bitsandbytes.

**عينات**
- [تعرف أكثر من خلال هذا الدفتر التفاعلي](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [مثال على عينة ضبط دقيق بلغة Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [مثال على ضبط دقيق من Hugging Face Hub باستخدام LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [مثال على ضبط دقيق من Hugging Face Hub باستخدام QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. بالنسبة للمعلومات الحساسة، يُنصح بالترجمة الاحترافية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.