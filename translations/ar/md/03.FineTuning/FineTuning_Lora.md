<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-03-27T13:59:50+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "ar"
}
-->
# **تخصيص Phi-3 باستخدام Lora**

تخصيص نموذج اللغة Phi-3 Mini من مايكروسوفت باستخدام [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) على مجموعة بيانات تعليمات دردشة مخصصة.

LORA ستساعد في تحسين فهم المحادثات وتوليد الردود.

## دليل خطوة بخطوة لتخصيص Phi-3 Mini:

**الاستيراد والإعداد**

تثبيت loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ابدأ باستيراد المكتبات اللازمة مثل datasets، transformers، peft، trl، وtorch. قم بإعداد تسجيل العمليات لتتبع عملية التدريب.

يمكنك اختيار تعديل بعض الطبقات عن طريق استبدالها بنظيراتها التي تم تنفيذها في loralib. نحن ندعم حاليًا nn.Linear، nn.Embedding، وnn.Conv2d فقط. كما ندعم MergedLinear للحالات التي يمثل فيها nn.Linear واحد أكثر من طبقة، مثل بعض تطبيقات إسقاط qkv في الانتباه (راجع الملاحظات الإضافية لمزيد من التفاصيل).

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

قبل بدء حلقة التدريب، قم بتحديد أن تكون فقط معلمات LoRA قابلة للتدريب.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

عند حفظ نقطة التحقق، قم بإنشاء state_dict يحتوي فقط على معلمات LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

عند تحميل نقطة التحقق باستخدام load_state_dict، تأكد من ضبط strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

الآن يمكن أن تستمر عملية التدريب كالمعتاد.

**البارامترات**

قم بتعريف قاموسين: training_config وpeft_config. يحتوي training_config على البارامترات الخاصة بالتدريب مثل معدل التعلم، حجم الدفعة، وإعدادات التسجيل.

peft_config يحدد البارامترات المتعلقة بـ LoRA مثل الرتبة، الإسقاط، ونوع المهمة.

**تحميل النموذج والمحول**

حدد المسار إلى نموذج Phi-3 المدرب مسبقًا (مثل "microsoft/Phi-3-mini-4k-instruct"). قم بتكوين إعدادات النموذج، بما في ذلك استخدام الكاش، نوع البيانات (bfloat16 للدقة المختلطة)، وتنفيذ الانتباه.

**التدريب**

قم بتخصيص نموذج Phi-3 باستخدام مجموعة بيانات تعليمات دردشة مخصصة. استخدم إعدادات LoRA من peft_config للتكيف بكفاءة. تابع تقدم التدريب باستخدام استراتيجية التسجيل المحددة.
التقييم والحفظ: قم بتقييم النموذج المخصص.
احفظ نقاط التحقق أثناء التدريب للاستخدام لاحقًا.

**أمثلة**
- [تعرف على المزيد مع هذا الدفتر التوضيحي](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [مثال على تخصيص النموذج باستخدام Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [مثال على تخصيص النموذج باستخدام LORA على Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [مثال على بطاقة نموذج Hugging Face - تخصيص باستخدام LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [مثال على تخصيص النموذج باستخدام QLORA على Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الرسمي. للحصول على معلومات حيوية، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.