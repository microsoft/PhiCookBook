<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:27:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ar"
}
-->
# **تخصيص نموذج Phi-3 باستخدام Lora**

تخصيص نموذج اللغة Phi-3 Mini من مايكروسوفت باستخدام [LoRA (التكيف منخفض الرتبة)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) على مجموعة بيانات تعليمات دردشة مخصصة.

سيساعد LORA في تحسين فهم المحادثات وتوليد الردود.

## دليل خطوة بخطوة لكيفية تخصيص Phi-3 Mini:

**الاستيراد والإعداد**

تثبيت loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ابدأ باستيراد المكتبات اللازمة مثل datasets و transformers و peft و trl و torch. قم بإعداد تسجيل الأحداث لمتابعة عملية التدريب.

يمكنك اختيار تعديل بعض الطبقات عن طريق استبدالها بنظائرها المنفذة في loralib. ندعم حالياً فقط nn.Linear و nn.Embedding و nn.Conv2d. كما ندعم MergedLinear للحالات التي يمثل فيها nn.Linear واحد أكثر من طبقة، مثل بعض تطبيقات إسقاط qkv في الانتباه (راجع الملاحظات الإضافية للمزيد).

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

قبل بدء حلقة التدريب، قم بتحديد معلمات LoRA فقط كقابلة للتدريب.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

عند حفظ نقطة تحقق، أنشئ state_dict يحتوي فقط على معلمات LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

عند تحميل نقطة تحقق باستخدام load_state_dict، تأكد من تعيين strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

الآن يمكن متابعة التدريب كالمعتاد.

**المعلمات الفائقة**

حدد قاموسين: training_config و peft_config. يحتوي training_config على المعلمات الفائقة للتدريب مثل معدل التعلم، حجم الدُفعة، وإعدادات التسجيل.

يحدد peft_config معلمات LoRA مثل الرتبة، التسرب، ونوع المهمة.

**تحميل النموذج والمُرمّز**

حدد مسار نموذج Phi-3 المدرب مسبقاً (مثلاً "microsoft/Phi-3-mini-4k-instruct"). قم بضبط إعدادات النموذج، بما في ذلك استخدام التخزين المؤقت، نوع البيانات (bfloat16 للدقة المختلطة)، وتنفيذ الانتباه.

**التدريب**

قم بتخصيص نموذج Phi-3 باستخدام مجموعة بيانات تعليمات الدردشة المخصصة. استخدم إعدادات LoRA من peft_config للتكيف الفعال. راقب تقدم التدريب باستخدام استراتيجية التسجيل المحددة.

التقييم والحفظ: قيّم النموذج بعد التخصيص. احفظ نقاط التحقق أثناء التدريب للاستخدام لاحقاً.

**عينات**
- [تعلم المزيد مع هذا الدفتر النموذجي](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [مثال على تخصيص بايثون](../../../../code/03.Finetuning/FineTrainingScript.py)
- [مثال على تخصيص Hugging Face Hub باستخدام LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [مثال على بطاقة نموذج Hugging Face - عينة تخصيص LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [مثال على تخصيص Hugging Face Hub باستخدام QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.