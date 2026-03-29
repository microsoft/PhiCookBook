# الضبط الدقيق لـ Phi-3 بواسطة Microsoft Foundry

لنستكشف كيفية ضبط نموذج اللغة المصغر Phi-3 من مايكروسوفت باستخدام Microsoft Foundry. يتيح لك الضبط الدقيق تكييف Phi-3 Mini مع مهام محددة، مما يجعله أقوى وأكثر وعيًا بالسياق.

## الاعتبارات

- **القدرات:** أي النماذج يمكن ضبطها بدقة؟ ماذا يمكن أن يفعل النموذج الأساسي بعد الضبط؟
- **التكلفة:** ما هو نموذج التسعير للضبط الدقيق؟
- **القابلية للتعديل:** كم يمكنني تعديل النموذج الأساسي – وبأي طرق؟
- **الراحة:** كيف يتم الضبط الدقيق فعليًا – هل أحتاج إلى كتابة كود مخصص؟ هل أحتاج لجلب موارد الحوسبة بنفسي؟
- **الأمان:** النماذج المضبوطة تعرف بأنها تحمل مخاطر أمنية – هل توجد أية ضوابط تحمي من الأضرار غير المقصودة؟

![AIFoundry Models](../../../../translated_images/ar/AIFoundryModels.0e1b16f7d0b09b73.webp)

## التحضير للضبط الدقيق

### المتطلبات الأساسية

> [!NOTE]
> بالنسبة لنماذج عائلة Phi-3، فإن عرض الضبط الدقيق بنظام الدفع عند الاستخدام متاح فقط مع المراكز المنشأة في مناطق **East US 2**.

- اشتراك Azure. إذا لم يكن لديك اشتراك Azure، فأنشئ [حساب Azure مدفوع](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) للبدء.

- مشروع [AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- تُستخدم ضوابط الوصول بناءً على الأدوار لـ Azure (Azure RBAC) لمنح الوصول إلى العمليات في Microsoft Foundry. لأداء الخطوات في هذه المقالة، يجب تعيين __دور مطور Azure AI__ لحساب المستخدم الخاص بك في مجموعة الموارد.

### تسجيل مزود الاشتراك

تحقق من تسجيل الاشتراك لدى مزود الموارد `Microsoft.Network`.

1. سجّل الدخول إلى [بوابة Azure](https://portal.azure.com).
2. اختر **الاشتراكات** من القائمة اليسرى.
3. اختر الاشتراك الذي تريد استخدامه.
4. اختر **إعدادات مشروع AI** > **مزودو الموارد** من القائمة اليسرى.
5. تأكد أن **Microsoft.Network** مدرج في قائمة مزودي الموارد، وإلا قم بإضافته.

### تحضير البيانات

جهز بيانات التدريب والاختبار لضبط النموذج. تتكون مجموعات بياناتك من أمثلة إدخال وإخراج تعكس كيف ترغب أن يعمل النموذج.

تأكد أن جميع أمثلة التدريب تتبع التنسيق المتوقع للاستدلال. لضبط النماذج بفعالية، ضمن توافر مجموعة بيانات متوازنة ومتنوعة.

يتطلب ذلك الحفاظ على توازن البيانات، واحتواء سيناريوهات متنوعة، وتنقيح بيانات التدريب دوريًا لتتوافق مع توقعات الحياة الواقعية، مما يؤدي إلى استجابات نموذج أكثر دقة وتوازنًا.

تتطلب أنواع النماذج المختلفة تنسيقات مختلفة من بيانات التدريب.

### إكمال الدردشة

يجب أن تكون بيانات التدريب والاختبار التي تستخدمها **منسقة** كمستند JSON Lines (JSONL). بالنسبة لـ `Phi-3-mini-128k-instruct` يجب أن يكون مجموعة بيانات الضبط الدقيق منسقة بصيغة المحادثة المستخدمة في واجهة برمجة تطبيقات إكمال الدردشة.

### مثال تنسيق الملف

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

نوع الملف المدعوم هو JSON Lines. تُحمّل الملفات إلى مستودع البيانات الافتراضي وتتوفر في مشروعك.

## ضبط دقيق لـ Phi-3 بواسطة Microsoft Foundry

يتيح لك Microsoft Foundry تخصيص نماذج اللغة الكبيرة باستخدام مجموعات بياناتك الشخصية عبر عملية تعرف بالضبط الدقيق. يوفر الضبط الدقيق قيمة كبيرة من خلال تمكين التخصيص والتحسين لمهام وتطبيقات محددة. يؤدي ذلك إلى تحسين الأداء، وكفاءة التكلفة، وتقليل زمن الاستجابة، وإخراج مخصص.

![Finetune AI Foundry](../../../../translated_images/ar/AIFoundryfinetune.193aaddce48d553c.webp)

### إنشاء مشروع جديد

1. سجّل الدخول إلى [Microsoft Foundry](https://ai.azure.com).

2. اختر **+مشروع جديد** لإنشاء مشروع جديد في Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/ar/select-new-project.cd31c0404088d7a3.webp)

3. نفذ المهام التالية:

    - اسم **Hub** الخاص بالمشروع. يجب أن يكون قيمة فريدة.
    - اختر **Hub** لاستخدامه (أنشئ واحدًا جديدًا إذا لزم).

    ![FineTuneSelect](../../../../translated_images/ar/create-project.ca3b71298b90e420.webp)

4. أنشئ Hub جديد عبر المهام التالية:

    - أدخل **اسم Hub**. يجب أن يكون فريدًا.
    - اختر اشتراك Azure الخاص بك.
    - اختر **مجموعة الموارد** (أنشئ جديدة إذا لزم).
    - حدد الموقع الذي ترغب في استخدامه.
    - اختر خدمات Azure AI التي تريد ربطها (أنشئ واحدة جديدة إذا لزم).
    - اختر **تخطي الاتصال** لخدمة Azure AI Search.

    ![FineTuneSelect](../../../../translated_images/ar/create-hub.49e53d235e80779e.webp)

5. اختر **التالي**.
6. اختر **إنشاء مشروع**.

### تحضير البيانات

قبل الضبط الدقيق، اجمع أو أنشئ مجموعة بيانات مناسبة لمهمتك، مثل تعليمات الدردشة، أزواج سؤال وجواب، أو أي بيانات نصية ذات صلة. نظف البيانات وعالجها مسبقًا عبر إزالة الضوضاء، معالجة القيم المفقودة، وتفكيك النص.

### ضبط نماذج Phi-3 داخل Microsoft Foundry

> [!NOTE]
> يدعم الضبط الدقيق لنماذج Phi-3 حاليًا في المشاريع الواقعة في المنطقة East US 2.

1. اختر **كتالوج النماذج** من التبويب الأيسر.

2. اكتب *phi-3* في **شريط البحث** واختر نموذج phi-3 الذي تريد استخدامه.

    ![FineTuneSelect](../../../../translated_images/ar/select-model.60ef2d4a6a3cec57.webp)

3. اختر **ضبط دقيق**.

    ![FineTuneSelect](../../../../translated_images/ar/select-finetune.a976213b543dd9d8.webp)

4. أدخل اسم **النموذج المضبوط**.

    ![FineTuneSelect](../../../../translated_images/ar/finetune1.c2b39463f0d34148.webp)

5. اختر **التالي**.

6. أنجز المهام التالية:

    - اختر نوع **المهمة** كـ **إكمال محادثة**.
    - اختر **بيانات التدريب** التي تريد استخدامها. يمكنك تحميلها من بيانات Microsoft Foundry أو من بيئتك المحلية.

    ![FineTuneSelect](../../../../translated_images/ar/finetune2.43cb099b1a94442d.webp)

7. اختر **التالي**.

8. حمّل بيانات **الاختبار** التي تريد استخدامها، أو اختر **التقسيم التلقائي لبيانات التدريب**.

    ![FineTuneSelect](../../../../translated_images/ar/finetune3.fd96121b67dcdd92.webp)

9. اختر **التالي**.

10. قم بما يلي:

    - اختر مضاعف **حجم الدُفعة** الذي ترغب باستخدامه.
    - اختر **معدل التعلم** الذي تريده.
    - اختر عدد **الدورات الزمنية** (Epochs) التي ترغب بها.

    ![FineTuneSelect](../../../../translated_images/ar/finetune4.e18b80ffccb5834a.webp)

11. اختر **إرسال** لبدء عملية الضبط الدقيق.

    ![FineTuneSelect](../../../../translated_images/ar/select-submit.0a3802d581bac271.webp)

12. بمجرد إتمام الضبط الدقيق، ستظهر الحالة كـ **مكتمل** كما هو موضح أدناه. يمكنك الآن نشر النموذج واستخدامه في تطبيقك الخاص، في بيئة اللعب، أو في تدفق التعليمات. لمزيد من المعلومات، اطلع على [كيفية نشر عائلة نماذج اللغة الصغيرة Phi-3 باستخدام Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/ar/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> لمزيد من المعلومات المفصلة عن الضبط الدقيق لنماذج Phi-3، يرجى زيارة [ضبط نماذج Phi-3 في Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## تنظيف نماذجك المضبوطة دقيقًا

يمكنك حذف نموذج مضبوطة دقيقًا من قائمة نماذج الضبط الدقيق في [Microsoft Foundry](https://ai.azure.com) أو من صفحة تفاصيل النموذج. اختر النموذج المضبوط للحذف من صفحة الضبط الدقيق، ثم اختر زر الحذف.

> [!NOTE]
> لا يمكنك حذف نموذج مخصص إذا كان لديه نشر قائم. يجب أولًا حذف نشر النموذج قبل أن تتمكن من حذف النموذج المخصص.

## التكلفة والحصص

### اعتبارات التكلفة والحصص لنماذج Phi-3 المضبوطة كخدمة

النماذج Phi المعدلة كخدمة تقدمها مايكروسوفت ومتكاملة مع Microsoft Foundry للاستخدام. يمكنك معرفة الأسعار عند [النشر](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) أو الضبط الدقيق للنماذج ضمن علامة التبويب "التسعير والشروط" في معالج النشر.

## تصفية المحتوى

النماذج المُنشأة كخدمة بنظام الدفع حسب الاستخدام محمية بواسطة أمان محتوى Azure AI. عند النشر على نقاط نهاية الوقت الحقيقي، يمكنك اختيار عدم تفعيل هذه الخاصية. مع تمكين أمان محتوى Azure AI، تمر كل من التعليمات والنواتج عبر مجموعة من نماذج التصنيف تهدف إلى الكشف عن المحتوى الضار ومنعه. يكتشف نظام تصفية المحتوى ويتخذ إجراءات ضد فئات محددة من المحتوى المحتمل أن يكون ضارًا في كل من التعليمات الواردة والنواتج. تعرّف على المزيد عن [أمان محتوى Azure AI](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**تكوين الضبط الدقيق**

المعلمات الفائقة: حدد معلمات مثل معدل التعلم، حجم الدُفعة، وعدد دورات التدريب.

**دالة الخسارة**

اختر دالة خسارة مناسبة لمهمتك (مثل التقاطعات المتبادلة).

**المحسن**

اختر محسنًا (مثل Adam) لتحديثات التدرج أثناء التدريب.

**عملية الضبط الدقيق**

- تحميل نموذج مدرب مسبقًا: تحميل نقطة تحقق Phi-3 Mini.
- إضافة طبقات مخصصة: إضافة طبقات مخصصة للمهمة (مثل رأس تصنيف لتعليمات الدردشة).

**تدريب النموذج**

اضبط النموذج باستخدام مجموعة البيانات التي أعددتها. راقب تقدم التدريب واضبط المعلمات حسب الحاجة.

**التقييم والتحقق**

مجموعة التحقق: قم بتقسيم بياناتك إلى مجموعات تدريب وتحقق.

**قياس الأداء**

استخدم مقاييس مثل الدقة، F1-score، أو التعقيد (Perplexity) لتقييم أداء النموذج.

## حفظ النموذج المضبوط

**نقطة التوقف**

احفظ نقطة توقف النموذج المضبوط لاستخدام مستقبلي.

## النشر

- نشر كنموذج خدمة ويب: انشر نموذجك المضبوط كنموذج خدمة ويب في Microsoft Foundry.
- اختبار نقطة النهاية: أرسل استفسارات اختبار للنقطة المنشورة للتحقق من وظيفتها.

## التكرار والتحسين

كرر: إذا لم يكن الأداء مرضيًا، قم بتكرار العملية عبر تعديل المعلمات، إضافة المزيد من البيانات، أو الاستمرار في الضبط لعدد دورات إضافية.

## المراقبة والتنقيح

راقب سلوك النموذج باستمرار ونقح حسب الحاجة.

## التخصيص والتوسيع

مهام مخصصة: يمكن ضبط Phi-3 Mini لمهام مختلفة تتجاوز تعليمات الدردشة. استكشف حالات استخدام أخرى!
التجربة: جرب بنى مختلفة، مجموعات طبقية، وتقنيات لتحسين الأداء.

> [!NOTE]
> الضبط الدقيق هو عملية تكرارية. جرب، تعلم، وكيّف نموذجك لتحقيق أفضل النتائج لمهمتك الخاصة!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنبيه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. بالنسبة للمعلومات الحرجة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->