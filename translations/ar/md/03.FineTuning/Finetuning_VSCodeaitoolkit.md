<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:01:16+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "ar"
}
-->
## مرحبًا بك في AI Toolkit لـ VS Code

يجمع [AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) بين نماذج مختلفة من كتالوج Azure AI Studio وكتالوجات أخرى مثل Hugging Face. يسهل هذا الأدوات المهام الشائعة لتطوير تطبيقات الذكاء الاصطناعي باستخدام أدوات ونماذج الذكاء الاصطناعي التوليدية من خلال:
- البدء باكتشاف النماذج وتجربة اللعب.
- ضبط النماذج واستنتاجها باستخدام موارد الحوسبة المحلية.
- ضبط النماذج واستنتاجها عن بُعد باستخدام موارد Azure.

[تثبيت AI Toolkit لـ VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/ar/Aitoolkit.7157953df04812dc.png)

**[Private Preview]** توفير بنقرة واحدة لتطبيقات Azure Container Apps لتشغيل ضبط النماذج واستنتاجها في السحابة.

لنبدأ الآن في تطوير تطبيق الذكاء الاصطناعي الخاص بك:

- [مرحبًا بك في AI Toolkit لـ VS Code](../../../../md/03.FineTuning)
- [التطوير المحلي](../../../../md/03.FineTuning)
  - [التحضيرات](../../../../md/03.FineTuning)
  - [تفعيل Conda](../../../../md/03.FineTuning)
  - [ضبط النموذج الأساسي فقط](../../../../md/03.FineTuning)
  - [ضبط النموذج والاستنتاج](../../../../md/03.FineTuning)
  - [ضبط النموذج](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [عينات وموارد الضبط الدقيق](../../../../md/03.FineTuning)
- [**\[Private Preview\]** التطوير عن بُعد](../../../../md/03.FineTuning)
  - [المتطلبات الأساسية](../../../../md/03.FineTuning)
  - [إعداد مشروع تطوير عن بُعد](../../../../md/03.FineTuning)
  - [توفير موارد Azure](../../../../md/03.FineTuning)
  - [\[اختياري\] إضافة رمز Huggingface إلى سر تطبيق Azure Container](../../../../md/03.FineTuning)
  - [تشغيل الضبط الدقيق](../../../../md/03.FineTuning)
  - [توفير نقطة نهاية الاستنتاج](../../../../md/03.FineTuning)
  - [نشر نقطة نهاية الاستنتاج](../../../../md/03.FineTuning)
  - [الاستخدام المتقدم](../../../../md/03.FineTuning)

## التطوير المحلي
### التحضيرات

1. تأكد من تثبيت برنامج تشغيل NVIDIA على الجهاز المضيف.
2. شغّل `huggingface-cli login` إذا كنت تستخدم HF لاستغلال مجموعة البيانات.
3. شرح إعدادات مفتاح `Olive` لأي شيء يؤثر على استخدام الذاكرة.

### تفعيل Conda
نظرًا لأننا نستخدم بيئة WSL وهي مشتركة، تحتاج إلى تفعيل بيئة conda يدويًا. بعد هذه الخطوة يمكنك تشغيل الضبط الدقيق أو الاستنتاج.

```bash
conda activate [conda-env-name] 
```

### ضبط النموذج الأساسي فقط
لتجربة النموذج الأساسي فقط بدون ضبط دقيق، يمكنك تشغيل هذا الأمر بعد تفعيل conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### ضبط النموذج والاستنتاج

بمجرد فتح مساحة العمل في حاوية التطوير، افتح الطرفية (المسار الافتراضي هو جذر المشروع)، ثم شغّل الأمر أدناه لضبط نموذج LLM على مجموعة البيانات المختارة.

```bash
python finetuning/invoke_olive.py 
```

سيتم حفظ نقاط التحقق والنموذج النهائي في مجلد `models`.

بعد ذلك، شغّل الاستنتاج باستخدام النموذج المضبوط من خلال المحادثات في `console` أو `web browser` أو `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

لاستخدام `prompt flow` في VS Code، يرجى الرجوع إلى هذا [البدء السريع](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### ضبط النموذج

بعد ذلك، قم بتنزيل النموذج المناسب حسب توفر GPU على جهازك.

لبدء جلسة الضبط الدقيق المحلية باستخدام QLoRA، اختر نموذجًا ترغب في ضبطه من كتالوجنا.
| النظام | توفر GPU | اسم النموذج | الحجم (جيجابايت) |
|---------|---------|--------|--------|
| Windows | نعم | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | نعم | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | لا | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_ملاحظة_** لا تحتاج إلى حساب Azure لتنزيل النماذج.

نموذج Phi3-mini (int4) حجمه تقريبًا بين 2GB و3GB. حسب سرعة الشبكة، قد يستغرق التنزيل بضع دقائق.

ابدأ باختيار اسم المشروع والموقع.
بعدها اختر نموذجًا من كتالوج النماذج. سيُطلب منك تنزيل قالب المشروع. يمكنك بعدها الضغط على "Configure Project" لضبط الإعدادات المختلفة.

### Microsoft Olive

نستخدم [Olive](https://microsoft.github.io/Olive/why-olive.html) لتشغيل ضبط QLoRA على نموذج PyTorch من كتالوجنا. جميع الإعدادات معدة مسبقًا بالقيم الافتراضية لتحسين تشغيل عملية الضبط محليًا مع استخدام محسّن للذاكرة، لكن يمكن تعديلها حسب حالتك.

### عينات وموارد الضبط الدقيق

- [دليل البدء في الضبط الدقيق](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [الضبط الدقيق باستخدام مجموعة بيانات HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [الضبط الدقيق باستخدام مجموعة بيانات بسيطة](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** التطوير عن بُعد

### المتطلبات الأساسية

1. لتشغيل ضبط النموذج في بيئة Azure Container App البعيدة، تأكد من أن اشتراكك يحتوي على سعة GPU كافية. قدّم [تذكرة دعم](https://azure.microsoft.com/support/create-ticket/) لطلب السعة المطلوبة لتطبيقك. [مزيد من المعلومات عن سعة GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. إذا كنت تستخدم مجموعة بيانات خاصة على HuggingFace، تأكد من أن لديك [حساب HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) و[أنشئ رمز وصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. فعّل ميزة الضبط الدقيق والاستنتاج عن بُعد في AI Toolkit لـ VS Code
   1. افتح إعدادات VS Code باختيار *File -> Preferences -> Settings*.
   2. انتقل إلى *Extensions* واختر *AI Toolkit*.
   3. فعّل خيار *"Enable Remote Fine-tuning And Inference"*.
   4. أعد تحميل VS Code لتطبيق التغييرات.

- [الضبط الدقيق عن بُعد](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### إعداد مشروع تطوير عن بُعد
1. نفّذ أمر لوحة الأوامر `AI Toolkit: Focus on Resource View`.
2. انتقل إلى *Model Fine-tuning* للوصول إلى كتالوج النماذج. عيّن اسمًا لمشروعك واختر موقعه على جهازك. ثم اضغط على زر *"Configure Project"*.
3. إعداد المشروع
    1. تجنب تفعيل خيار *"Fine-tune locally"*.
    2. ستظهر إعدادات Olive مع القيم الافتراضية المسبقة. يرجى تعديل وملء هذه الإعدادات حسب الحاجة.
    3. انتقل إلى *Generate Project*. هذه المرحلة تستخدم WSL وتتضمن إعداد بيئة Conda جديدة، استعدادًا للتحديثات المستقبلية التي تشمل حاويات التطوير.
4. اضغط على *"Relaunch Window In Workspace"* لفتح مشروع التطوير عن بُعد.

> **ملاحظة:** يعمل المشروع حاليًا إما محليًا أو عن بُعد ضمن AI Toolkit لـ VS Code. إذا اخترت *"Fine-tune locally"* أثناء إنشاء المشروع، سيعمل فقط في WSL بدون قدرات تطوير عن بُعد. أما إذا لم تفعل ذلك، فسيقتصر المشروع على بيئة Azure Container App البعيدة.

### توفير موارد Azure
لبدء العمل، تحتاج إلى توفير موارد Azure للضبط الدقيق عن بُعد. قم بذلك عبر تشغيل أمر `AI Toolkit: Provision Azure Container Apps job for fine-tuning` من لوحة الأوامر.

تابع تقدم التوفير من خلال الرابط المعروض في قناة الإخراج.

### [اختياري] إضافة رمز Huggingface إلى سر تطبيق Azure Container
إذا كنت تستخدم مجموعة بيانات خاصة من HuggingFace، قم بتعيين رمز HuggingFace كمتغير بيئي لتجنب الحاجة لتسجيل الدخول يدويًا في Hugging Face Hub.
يمكنك فعل ذلك باستخدام أمر `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. مع هذا الأمر، يمكنك تعيين اسم السر إلى [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) واستخدام رمز Hugging Face كقيمة السر.

### تشغيل الضبط الدقيق
لبدء مهمة الضبط الدقيق عن بُعد، نفّذ أمر `AI Toolkit: Run fine-tuning`.

لعرض سجلات النظام والطرفية، يمكنك زيارة بوابة Azure عبر الرابط في لوحة الإخراج (خطوات إضافية في [عرض واستعلام السجلات على Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). أو يمكنك عرض سجلات الطرفية مباشرة في لوحة الإخراج في VSCode عبر تشغيل الأمر `AI Toolkit: Show the running fine-tuning job streaming logs`.
> **ملاحظة:** قد تكون المهمة في قائمة الانتظار بسبب نقص الموارد. إذا لم تظهر السجلات، نفّذ أمر `AI Toolkit: Show the running fine-tuning job streaming logs`، انتظر قليلاً ثم نفّذ الأمر مرة أخرى لإعادة الاتصال بسجل البث.

خلال هذه العملية، سيتم استخدام QLoRA للضبط الدقيق، وسيتم إنشاء محولات LoRA للنموذج لاستخدامها أثناء الاستنتاج.
سيتم تخزين نتائج الضبط الدقيق في Azure Files.

### توفير نقطة نهاية الاستنتاج
بعد تدريب المحولات في البيئة البعيدة، استخدم تطبيق Gradio بسيط للتفاعل مع النموذج.
مثل عملية الضبط الدقيق، تحتاج إلى إعداد موارد Azure للاستنتاج عن بُعد عبر تنفيذ أمر `AI Toolkit: Provision Azure Container Apps for inference` من لوحة الأوامر.

افتراضيًا، يجب أن تتطابق الاشتراك ومجموعة الموارد للاستنتاج مع تلك المستخدمة في الضبط الدقيق. سيستخدم الاستنتاج نفس بيئة Azure Container App ويصل إلى النموذج ومحول النموذج المخزن في Azure Files، والتي تم إنشاؤها خلال خطوة الضبط الدقيق.

### نشر نقطة نهاية الاستنتاج
إذا رغبت في تعديل كود الاستنتاج أو إعادة تحميل نموذج الاستنتاج، يرجى تنفيذ أمر `AI Toolkit: Deploy for inference`. سيؤدي ذلك إلى مزامنة أحدث كود مع Azure Container App وإعادة تشغيل النسخة.

بمجرد اكتمال النشر بنجاح، يمكنك الوصول إلى واجهة برمجة تطبيقات الاستنتاج بالنقر على زر "*Go to Inference Endpoint*" المعروض في إشعار VSCode. أو يمكنك العثور على نقطة نهاية واجهة الويب تحت `ACA_APP_ENDPOINT` في `./infra/inference.config.json` وفي لوحة الإخراج. أنت الآن جاهز لتقييم النموذج باستخدام هذه النقطة.

### الاستخدام المتقدم
لمزيد من المعلومات حول التطوير عن بُعد باستخدام AI Toolkit، راجع وثائق [الضبط الدقيق عن بُعد](https://aka.ms/ai-toolkit/remote-provision) و[الاستنتاج باستخدام النموذج المضبوط](https://aka.ms/ai-toolkit/remote-inference).

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.