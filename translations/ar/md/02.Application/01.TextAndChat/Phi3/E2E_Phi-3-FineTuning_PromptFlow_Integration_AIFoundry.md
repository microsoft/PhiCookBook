<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-03-27T10:29:08+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ar"
}
-->
# تحسين وضبط نماذج Phi-3 المخصصة مع Prompt Flow في Azure AI Foundry

هذه العينة الشاملة تعتمد على الدليل "[تحسين وضبط نماذج Phi-3 المخصصة مع Prompt Flow في Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" من مجتمع Microsoft Tech. يُقدم هذا الدليل خطوات تحسين وضبط، نشر، ودمج نماذج Phi-3 المخصصة باستخدام Prompt Flow في Azure AI Foundry.  
على عكس العينة الشاملة "[تحسين وضبط نماذج Phi-3 المخصصة مع Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" التي تعتمد على تشغيل الكود محليًا، يركز هذا الدليل على تحسين وضبط ودمج النموذج بالكامل داخل Azure AI / ML Studio.

## نظرة عامة

في هذه العينة الشاملة، ستتعلم كيفية تحسين وضبط نموذج Phi-3 ودمجه مع Prompt Flow في Azure AI Foundry. باستخدام Azure AI / ML Studio، ستنشئ سير عمل لنشر واستخدام نماذج الذكاء الاصطناعي المخصصة. هذه العينة الشاملة مقسمة إلى ثلاثة سيناريوهات:

**السيناريو الأول: إعداد موارد Azure والتحضير لتحسين النموذج**

**السيناريو الثاني: تحسين وضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio**

**السيناريو الثالث: دمج النموذج مع Prompt Flow والتفاعل معه داخل Azure AI Foundry**

إليك نظرة عامة على هذه العينة الشاملة:

![نظرة عامة على تحسين وضبط ودمج Phi-3 مع Prompt Flow.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ar.png)

### جدول المحتويات

1. **[السيناريو الأول: إعداد موارد Azure والتحضير لتحسين النموذج](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [إنشاء Workspace لـ Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [طلب حصص GPU في اشتراك Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [إضافة تعيين الدور](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [إعداد المشروع](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [تحضير مجموعة البيانات لتحسين النموذج](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[السيناريو الثاني: تحسين وضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [تحسين وضبط نموذج Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [نشر نموذج Phi-3 المحسن](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[السيناريو الثالث: دمج النموذج مع Prompt Flow والتفاعل معه داخل Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [دمج نموذج Phi-3 المخصص مع Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [التفاعل مع نموذج Phi-3 المخصص](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## السيناريو الأول: إعداد موارد Azure والتحضير لتحسين النموذج

### إنشاء Workspace لـ Azure Machine Learning

1. اكتب *azure machine learning* في **شريط البحث** أعلى صفحة البوابة، ثم اختر **Azure Machine Learning** من الخيارات التي تظهر.

    ![اكتب azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ar.png)

2. اختر **+ Create** من قائمة التنقل.

3. اختر **New workspace** من قائمة التنقل.

    ![اختر workspace جديد.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ar.png)

4. قم بالمهام التالية:

    - اختر **Subscription** الخاص بك في Azure.  
    - اختر **Resource group** الذي ترغب باستخدامه (قم بإنشاء جديد إذا لزم الأمر).  
    - أدخل **Workspace Name**. يجب أن يكون اسمًا فريدًا.  
    - اختر **Region** الذي ترغب باستخدامه.  
    - اختر **Storage account** الذي ترغب باستخدامه (قم بإنشاء جديد إذا لزم الأمر).  
    - اختر **Key vault** الذي ترغب باستخدامه (قم بإنشاء جديد إذا لزم الأمر).  
    - اختر **Application insights** الذي ترغب باستخدامه (قم بإنشاء جديد إذا لزم الأمر).  
    - اختر **Container registry** الذي ترغب باستخدامه (قم بإنشاء جديد إذا لزم الأمر).  

    ![املأ معلومات Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ar.png)

5. اختر **Review + Create**.

6. اختر **Create**.

### طلب حصص GPU في اشتراك Azure

في هذا الدليل، ستتعلم كيفية تحسين وضبط ونشر نموذج Phi-3 باستخدام وحدات GPU. لتحسين النموذج، ستستخدم GPU من نوع *Standard_NC24ads_A100_v4*، الذي يتطلب طلب حصة. وللنشر، ستستخدم GPU من نوع *Standard_NC6s_v3*، الذي يتطلب أيضًا طلب حصة.

> [!NOTE]
>
> فقط الاشتراكات من نوع الدفع حسب الاستخدام (Pay-As-You-Go) مؤهلة للحصول على GPU؛ الاشتراكات ذات الامتيازات غير مدعومة حاليًا.

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. قم بالمهام التالية لطلب حصة *Standard NCADSA100v4 Family*:

    - اختر **Quota** من الشريط الجانبي.  
    - اختر **Virtual machine family** الذي ترغب باستخدامه. على سبيل المثال، اختر **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**، الذي يشمل GPU من نوع *Standard_NC24ads_A100_v4*.  
    - اختر **Request quota** من قائمة التنقل.  

        ![طلب الحصة.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ar.png)

    - داخل صفحة طلب الحصة، أدخل **New cores limit** الذي ترغب باستخدامه. على سبيل المثال، 24.  
    - داخل صفحة طلب الحصة، اختر **Submit** لطلب حصة GPU.

1. قم بالمهام التالية لطلب حصة *Standard NCSv3 Family*:

    - اختر **Quota** من الشريط الجانبي.  
    - اختر **Virtual machine family** الذي ترغب باستخدامه. على سبيل المثال، اختر **Standard NCSv3 Family Cluster Dedicated vCPUs**، الذي يشمل GPU من نوع *Standard_NC6s_v3*.  
    - اختر **Request quota** من قائمة التنقل.  
    - داخل صفحة طلب الحصة، أدخل **New cores limit** الذي ترغب باستخدامه. على سبيل المثال، 24.  
    - داخل صفحة طلب الحصة، اختر **Submit** لطلب حصة GPU.

### إضافة تعيين الدور

لتحسين وضبط ونشر نماذجك، يجب أولاً إنشاء هوية مُدارة (UAI) وتعيين الأذونات المناسبة لها. سيتم استخدام هذه الهوية المُدارة للمصادقة أثناء عملية النشر.

#### إنشاء هوية مُدارة (UAI)

1. اكتب *managed identities* في **شريط البحث** أعلى صفحة البوابة، ثم اختر **Managed Identities** من الخيارات التي تظهر.

    ![اكتب managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ar.png)

1. اختر **+ Create**.

    ![اختر إنشاء.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ar.png)

1. قم بالمهام التالية:

    - اختر **Subscription** الخاص بك في Azure.  
    - اختر **Resource group** الذي ترغب باستخدامه (قم بإنشاء جديد إذا لزم الأمر).  
    - اختر **Region** الذي ترغب باستخدامه.  
    - أدخل **Name**. يجب أن يكون اسمًا فريدًا.  

    ![املأ معلومات الهوية المُدارة.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ar.png)

1. اختر **Review + create**.

1. اختر **+ Create**.

#### إضافة تعيين دور Contributor إلى الهوية المُدارة

1. انتقل إلى مورد الهوية المُدارة الذي أنشأته.

1. اختر **Azure role assignments** من الشريط الجانبي.

1. اختر **+Add role assignment** من قائمة التنقل.

1. داخل صفحة إضافة تعيين الدور، قم بالمهام التالية:
    - اختر **Scope** إلى **Resource group**.  
    - اختر **Subscription** الخاص بك في Azure.  
    - اختر **Resource group** الذي ترغب باستخدامه.  
    - اختر **Role** إلى **Contributor**.  

    ![املأ معلومات الدور Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ar.png)

2. اختر **Save**.

#### إضافة تعيين دور Storage Blob Data Reader إلى الهوية المُدارة

1. اكتب *storage accounts* في **شريط البحث** أعلى صفحة البوابة، ثم اختر **Storage accounts** من الخيارات التي تظهر.

    ![اكتب storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ar.png)

1. اختر حساب التخزين المرتبط بـ Azure Machine Learning workspace الذي أنشأته. على سبيل المثال، *finetunephistorage*.  
...
1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر **الحوسبة** من علامة التبويب الجانبية اليسرى.

1. اختر **مجموعات الحوسبة** من قائمة التنقل.

1. اختر **+ جديد**.

    ![اختر الحوسبة.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ar.png)

1. قم بتنفيذ المهام التالية:

    - اختر **المنطقة** التي ترغب في استخدامها.
    - اختر **طبقة الجهاز الافتراضي** إلى **مخصص**.
    - اختر **نوع الجهاز الافتراضي** إلى **GPU**.
    - اختر **مرشح حجم الجهاز الافتراضي** إلى **اختر من جميع الخيارات**.
    - اختر **حجم الجهاز الافتراضي** إلى **Standard_NC24ads_A100_v4**.

    ![إنشاء مجموعة.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ar.png)

1. اختر **التالي**.

1. قم بتنفيذ المهام التالية:

    - أدخل **اسم الحوسبة**. يجب أن يكون قيمة فريدة.
    - اختر **الحد الأدنى لعدد العقد** إلى **0**.
    - اختر **الحد الأقصى لعدد العقد** إلى **1**.
    - اختر **الثواني الخاملة قبل التوسع للأسفل** إلى **120**.

    ![إنشاء مجموعة.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ar.png)

1. اختر **إنشاء**.

#### ضبط نموذج Phi-3

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة العمل الخاصة بـ Azure Machine Learning التي قمت بإنشائها.

    ![اختر مساحة العمل التي أنشأتها.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ar.png)

1. قم بتنفيذ المهام التالية:

    - اختر **كتالوج النماذج** من علامة التبويب الجانبية اليسرى.
    - اكتب *phi-3-mini-4k* في **شريط البحث** واختر **Phi-3-mini-4k-instruct** من الخيارات التي تظهر.

    ![اكتب phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ar.png)

1. اختر **ضبط** من قائمة التنقل.

    ![اختر ضبط.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ar.png)

1. قم بتنفيذ المهام التالية:

    - اختر **نوع المهمة** إلى **إكمال المحادثة**.
    - اختر **+ اختيار البيانات** لتحميل **بيانات التدريب**.
    - اختر نوع تحميل بيانات التحقق إلى **توفير بيانات تحقق مختلفة**.
    - اختر **+ اختيار البيانات** لتحميل **بيانات التحقق**.

    ![املأ صفحة الضبط.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ar.png)

    > [!TIP]
    >
    > يمكنك اختيار **الإعدادات المتقدمة** لتخصيص التكوينات مثل **معدل التعلم** و **نوع جدولة معدل التعلم** لتحسين عملية الضبط وفقًا لاحتياجاتك المحددة.

1. اختر **إنهاء**.

1. في هذا التمرين، قمت بضبط نموذج Phi-3 بنجاح باستخدام Azure Machine Learning. يرجى ملاحظة أن عملية الضبط قد تستغرق وقتًا طويلاً. بعد تشغيل مهمة الضبط، ستحتاج إلى الانتظار حتى تكتمل. يمكنك مراقبة حالة مهمة الضبط من خلال الانتقال إلى علامة تبويب المهام في الجانب الأيسر من مساحة عمل Azure Machine Learning الخاصة بك. في السلسلة التالية، ستقوم بنشر النموذج المضبوط ودمجه مع Prompt Flow.

    ![عرض مهمة الضبط.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ar.png)

### نشر نموذج Phi-3 المضبوط

لدمج نموذج Phi-3 المضبوط مع Prompt Flow، تحتاج إلى نشر النموذج ليكون متاحًا للتنبؤ في الوقت الفعلي. تتضمن هذه العملية تسجيل النموذج، وإنشاء نقطة نهاية عبر الإنترنت، ونشر النموذج.

في هذا التمرين، ستقوم بـ:

- تسجيل النموذج المضبوط في مساحة عمل Azure Machine Learning.
- إنشاء نقطة نهاية عبر الإنترنت.
- نشر نموذج Phi-3 المضبوط المسجل.

#### تسجيل النموذج المضبوط

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة العمل الخاصة بـ Azure Machine Learning التي قمت بإنشائها.

    ![اختر مساحة العمل التي أنشأتها.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ar.png)

1. اختر **النماذج** من علامة التبويب الجانبية اليسرى.
1. اختر **+ تسجيل**.
1. اختر **من مخرجات المهمة**.

    ![تسجيل النموذج.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ar.png)

1. اختر المهمة التي قمت بإنشائها.

    ![اختر المهمة.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ar.png)

1. اختر **التالي**.

1. اختر **نوع النموذج** إلى **MLflow**.

1. تأكد من أن **مخرجات المهمة** محددة؛ يجب أن تكون محددة تلقائيًا.

    ![اختر المخرجات.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ar.png)

2. اختر **التالي**.

3. اختر **تسجيل**.

    ![اختر تسجيل.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ar.png)

4. يمكنك عرض النموذج المسجل الخاص بك من خلال الانتقال إلى قائمة **النماذج** من علامة التبويب الجانبية اليسرى.

    ![النموذج المسجل.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ar.png)

#### نشر النموذج المضبوط

1. انتقل إلى مساحة عمل Azure Machine Learning التي قمت بإنشائها.

1. اختر **النقاط النهائية** من علامة التبويب الجانبية اليسرى.

1. اختر **نقاط النهاية في الوقت الفعلي** من قائمة التنقل.

    ![إنشاء نقطة نهاية.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ar.png)

1. اختر **إنشاء**.

1. اختر النموذج المسجل الذي قمت بإنشائه.

    ![اختر النموذج المسجل.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ar.png)

1. اختر **اختيار**.

1. قم بتنفيذ المهام التالية:

    - اختر **الجهاز الافتراضي** إلى *Standard_NC6s_v3*.
    - اختر **عدد النسخ** التي ترغب في استخدامها. على سبيل المثال، *1*.
    - اختر **نقطة النهاية** إلى **جديدة** لإنشاء نقطة نهاية.
    - أدخل **اسم نقطة النهاية**. يجب أن تكون قيمة فريدة.
    - أدخل **اسم النشر**. يجب أن تكون قيمة فريدة.

    ![املأ إعدادات النشر.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ar.png)

1. اختر **نشر**.

> [!WARNING]
> لتجنب تكاليف إضافية على حسابك، تأكد من حذف نقطة النهاية التي تم إنشاؤها في مساحة عمل Azure Machine Learning.
>

#### التحقق من حالة النشر في مساحة عمل Azure Machine Learning

1. انتقل إلى مساحة عمل Azure Machine Learning التي قمت بإنشائها.

1. اختر **النقاط النهائية** من علامة التبويب الجانبية اليسرى.

1. اختر نقطة النهاية التي قمت بإنشائها.

    ![اختر النقاط النهائية.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ar.png)

1. في هذه الصفحة، يمكنك إدارة النقاط النهائية أثناء عملية النشر.

> [!NOTE]
> بمجرد اكتمال النشر، تأكد من أن **حركة المرور المباشرة** مضبوطة على **100%**. إذا لم تكن كذلك، اختر **تحديث حركة المرور** لتعديل إعدادات حركة المرور. لاحظ أنه لا يمكنك اختبار النموذج إذا كانت حركة المرور مضبوطة على 0%.
>
> ![ضبط حركة المرور.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ar.png)
>

## السيناريو 3: التكامل مع Prompt Flow والتفاعل مع النموذج المخصص في Azure AI Foundry

### دمج نموذج Phi-3 المخصص مع Prompt Flow

بعد نشر النموذج المضبوط بنجاح، يمكنك الآن دمجه مع Prompt Flow لاستخدام النموذج الخاص بك في التطبيقات التفاعلية في الوقت الفعلي، مما يتيح مجموعة متنوعة من المهام التفاعلية مع نموذج Phi-3 المخصص الخاص بك.

في هذا التمرين، ستقوم بـ:

- إنشاء مركز Azure AI Foundry.
- إنشاء مشروع Azure AI Foundry.
- إنشاء Prompt Flow.
- إضافة اتصال مخصص للنموذج المضبوط Phi-3.
- إعداد Prompt Flow للتفاعل مع النموذج المخصص Phi-3 الخاص بك.

> [!NOTE]
> يمكنك أيضًا التكامل مع Prompt Flow باستخدام Azure ML Studio. يمكن تطبيق نفس عملية التكامل على Azure ML Studio.

#### إنشاء مركز Azure AI Foundry

ستحتاج إلى إنشاء مركز قبل إنشاء المشروع. يعمل المركز كمجموعة موارد، مما يتيح لك تنظيم وإدارة مشاريع متعددة داخل Azure AI Foundry.

1. قم بزيارة [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. اختر **جميع المراكز** من علامة التبويب الجانبية اليسرى.

1. اختر **+ مركز جديد** من قائمة التنقل.

    ![إنشاء مركز.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ar.png)

1. قم بتنفيذ المهام التالية:

    - أدخل **اسم المركز**. يجب أن يكون قيمة فريدة.
    - اختر **الاشتراك** الخاص بك في Azure.
    - اختر **مجموعة الموارد** التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **الموقع** الذي ترغب في استخدامه.
    - اختر **اتصال خدمات Azure AI** التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **اتصال Azure AI Search** إلى **تخطي الاتصال**.

    ![املأ المركز.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ar.png)

1. اختر **التالي**.

#### إنشاء مشروع Azure AI Foundry

1. في المركز الذي قمت بإنشائه، اختر **جميع المشاريع** من علامة التبويب الجانبية اليسرى.

1. اختر **+ مشروع جديد** من قائمة التنقل.

    ![اختر مشروع جديد.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ar.png)

1. أدخل **اسم المشروع**. يجب أن يكون قيمة فريدة.

    ![إنشاء مشروع.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ar.png)

1. اختر **إنشاء مشروع**.

#### إضافة اتصال مخصص للنموذج المضبوط Phi-3

لدمج النموذج المخصص Phi-3 مع Prompt Flow، تحتاج إلى حفظ نقطة النهاية ومفتاح النموذج في اتصال مخصص. يضمن هذا الإعداد الوصول إلى النموذج المخصص Phi-3 في Prompt Flow.

#### إعداد مفتاح API وURI لنقطة النهاية للنموذج المضبوط Phi-3

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مساحة العمل الخاصة بـ Azure Machine Learning التي قمت بإنشائها.

1. اختر **النقاط النهائية** من علامة التبويب الجانبية اليسرى.

    ![اختر النقاط النهائية.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ar.png)

1. اختر نقطة النهاية التي قمت بإنشائها.

    ![اختر النقاط النهائية.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ar.png)

1. اختر **الاستهلاك** من قائمة التنقل.

1. انسخ **نقطة النهاية REST** و **المفتاح الأساسي**.
![نسخ مفتاح API وواجهة النهاية.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ar.png)

#### إضافة الاتصال المخصص

1. قم بزيارة [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مشروع Azure AI Foundry الذي أنشأته.

1. في المشروع الذي أنشأته، اختر **الإعدادات** من علامة التبويب الجانبية اليسرى.

1. اختر **+ اتصال جديد**.

    ![اختر اتصال جديد.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ar.png)

1. اختر **مفاتيح مخصصة** من قائمة التنقل.

    ![اختر مفاتيح مخصصة.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ar.png)

1. قم بتنفيذ المهام التالية:

    - اختر **+ إضافة أزواج مفتاح وقيمة**.
    - بالنسبة لاسم المفتاح، أدخل **endpoint** والصق واجهة النهاية التي نسختها من Azure ML Studio في حقل القيمة.
    - اختر **+ إضافة أزواج مفتاح وقيمة** مرة أخرى.
    - بالنسبة لاسم المفتاح، أدخل **key** والصق المفتاح الذي نسخته من Azure ML Studio في حقل القيمة.
    - بعد إضافة المفاتيح، اختر **is secret** لمنع المفتاح من أن يكون مكشوفًا.

    ![إضافة الاتصال.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ar.png)

1. اختر **إضافة اتصال**.

#### إنشاء Prompt flow

لقد أضفت اتصالًا مخصصًا في Azure AI Foundry. الآن، لنقم بإنشاء Prompt flow باستخدام الخطوات التالية. بعد ذلك، ستقوم بربط هذا Prompt flow بالاتصال المخصص بحيث يمكنك استخدام النموذج المحسن داخل Prompt flow.

1. انتقل إلى مشروع Azure AI Foundry الذي أنشأته.

1. اختر **Prompt flow** من علامة التبويب الجانبية اليسرى.

1. اختر **+ إنشاء** من قائمة التنقل.

    ![اختر Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ar.png)

1. اختر **Chat flow** من قائمة التنقل.

    ![اختر Chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ar.png)

1. أدخل **اسم المجلد** الذي ترغب باستخدامه.

    ![أدخل الاسم.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ar.png)

2. اختر **إنشاء**.

#### إعداد Prompt flow للدردشة مع نموذج Phi-3 المخصص

تحتاج إلى دمج نموذج Phi-3 المحسن في Prompt flow. ومع ذلك، فإن Prompt flow الحالي غير مصمم لهذا الغرض. لذلك، يجب إعادة تصميم Prompt flow لتمكين التكامل مع النموذج المخصص.

1. في Prompt flow، قم بتنفيذ المهام التالية لإعادة بناء التدفق الحالي:

    - اختر **وضع الملف الخام**.
    - احذف كل التعليمات البرمجية الموجودة في ملف *flow.dag.yml*.
    - أضف التعليمات البرمجية التالية إلى ملف *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - اختر **حفظ**.

    ![اختر وضع الملف الخام.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ar.png)

1. أضف التعليمات البرمجية التالية إلى ملف *integrate_with_promptflow.py* لاستخدام نموذج Phi-3 المخصص في Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![الصق كود Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ar.png)

> [!NOTE]
> لمزيد من المعلومات التفصيلية حول استخدام Prompt flow في Azure AI Foundry، يمكنك الرجوع إلى [Prompt flow في Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. اختر **مدخلات الدردشة** و **مخرجات الدردشة** لتمكين الدردشة مع النموذج الخاص بك.

    ![المدخلات والمخرجات.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ar.png)

1. الآن أصبحت جاهزًا للدردشة مع نموذج Phi-3 المخصص الخاص بك. في التمرين التالي، ستتعلم كيفية بدء Prompt flow واستخدامه للدردشة مع نموذج Phi-3 المحسن الخاص بك.

> [!NOTE]
>
> يجب أن يبدو التدفق المعاد بناؤه كما في الصورة أدناه:
>
> ![مثال على التدفق.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ar.png)
>

### الدردشة مع نموذج Phi-3 المخصص الخاص بك

الآن بعد أن قمت بتحسين ودمج نموذج Phi-3 المخصص الخاص بك مع Prompt flow، أصبحت جاهزًا لبدء التفاعل معه. سيرشدك هذا التمرين خلال عملية إعداد وبدء محادثة مع النموذج الخاص بك باستخدام Prompt flow. باتباع هذه الخطوات، ستتمكن من الاستفادة الكاملة من إمكانيات نموذج Phi-3 المحسن الخاص بك لمهام ومحادثات مختلفة.

- قم بالدردشة مع نموذج Phi-3 المخصص الخاص بك باستخدام Prompt flow.

#### بدء Prompt flow

1. اختر **بدء جلسات الحوسبة** لبدء Prompt flow.

    ![بدء جلسة الحوسبة.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ar.png)

1. اختر **التحقق من صحة المدخلات وتحليلها** لتحديث المعلمات.

    ![التحقق من صحة المدخلات.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ar.png)

1. اختر **القيمة** الخاصة بـ **الاتصال** للاتصال المخصص الذي أنشأته. على سبيل المثال، *connection*.

    ![الاتصال.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ar.png)

#### الدردشة مع النموذج المخصص الخاص بك

1. اختر **الدردشة**.

    ![اختر الدردشة.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ar.png)

1. إليك مثال على النتائج: الآن يمكنك الدردشة مع نموذج Phi-3 المخصص الخاص بك. يوصى بطرح أسئلة بناءً على البيانات المستخدمة في تحسين النموذج.

    ![الدردشة مع Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ar.png)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.