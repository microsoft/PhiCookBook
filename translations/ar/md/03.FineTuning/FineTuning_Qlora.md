<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-03-27T15:09:59+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "ar"
}
-->
**ضبط Phi-3 باستخدام QLoRA**

ضبط نموذج اللغة Phi-3 Mini الخاص بـ Microsoft باستخدام [QLoRA (التكيف الكمي منخفض الرتبة)](https://github.com/artidoro/qlora).

QLoRA سيساعد على تحسين فهم المحادثات وتوليد الردود.

لتحميل النماذج باستخدام 4bits مع transformers وbitsandbytes، تحتاج إلى تثبيت accelerate وtransformers من المصدر والتأكد من أنك تمتلك أحدث إصدار من مكتبة bitsandbytes.

**عينات**
- [تعرف على المزيد باستخدام هذا الدفتر التجريبي](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [مثال على ضبط النموذج باستخدام Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [مثال على ضبط النموذج باستخدام Hugging Face Hub وLORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [مثال على ضبط النموذج باستخدام Hugging Face Hub وQLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة ترجمة الذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حيوية، يُوصى بالاستعانة بخدمات ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة استخدام هذه الترجمة.