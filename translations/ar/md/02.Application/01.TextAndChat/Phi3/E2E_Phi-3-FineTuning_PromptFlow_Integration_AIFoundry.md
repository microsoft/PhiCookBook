# ضبط وتكامل نماذج Phi-3 المخصصة باستخدام Prompt flow في Microsoft Foundry

تعتمد هذه العينة الشاملة (E2E) على الدليل "[ضبط وتكامل نماذج Phi-3 المخصصة باستخدام Prompt Flow في Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" من مجتمع Microsoft التقني. يقدم هذا الدليل عمليات الضبط، النشر، وتكامل نماذج Phi-3 المخصصة مع Prompt flow في Microsoft Foundry.
على عكس العينة الشاملة (E2E)، "[ضبط وتكامل نماذج Phi-3 المخصصة باستخدام Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)"، التي تضمنت تشغيل الشيفرة محليًا، يركز هذا البرنامج التعليمي بالكامل على ضبط وتكامل النموذج الخاص بك داخل Azure AI / ML Studio.

## نظرة عامة

في هذه العينة الشاملة (E2E)، ستتعلم كيفية ضبط نموذج Phi-3 وتكامله مع Prompt flow في Microsoft Foundry. باستخدام Azure AI / ML Studio، ستقوم بإنشاء سير عمل لنشر واستخدام نماذج الذكاء الاصطناعي المخصصة. تنقسم هذه العينة الشاملة إلى ثلاثة سيناريوهات:

**السيناريو 1: إعداد موارد Azure والاستعداد للضبط الدقيق**

**السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio**

**السيناريو 3: التكامل مع Prompt flow والدردشة مع نموذجك المخصص في Microsoft Foundry**

فيما يلي لمحة عامة عن هذه العينة الشاملة.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ar/00-01-architecture.198ba0f1ae6d841a.webp)

### جدول المحتويات

1. **[السيناريو 1: إعداد موارد Azure والاستعداد للضبط الدقيق](#السيناريو-1-إعداد-موارد-azure-والاستعداد-للضبط-الدقيق)**
    - [إنشاء مساحة عمل Azure Machine Learning](#إنشاء-مساحة-عمل-azure-machine-learning)
    - [طلب حصص GPU في اشتراك Azure](#طلب-حصص-gpu-في-اشتراك-azure)
    - [إضافة تعيين الدور](#إضافة-تعيين-دور)
    - [إعداد المشروع](#إعداد-المشروع)
    - [تحضير مجموعة البيانات للضبط الدقيق](#تحضير-مجموعة-البيانات-لضبط-النموذج-بدقة)

1. **[السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio](#السيناريو-2-ضبط-نموذج-phi-3-بدقة-ونشره-في-azure-machine-learning-studio)**
    - [ضبط نموذج Phi-3](#ضبط-نموذج-phi-3-بدقة)
    - [نشر نموذج Phi-3 المضبوط](#نشر-نموذج-phi-3-المضبوط)

1. **[السيناريو 3: التكامل مع Prompt flow والدردشة مع نموذجك المخصص في Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [تكامل نموذج Phi-3 المخصص مع Prompt flow](#دمج-نموذج-phi-3-المخصص-مع-prompt-flow)
    - [الدردشة مع نموذج Phi-3 المخصص](#الدردشة-مع-نموذج-phi-3-المخصص-الخاص-بك)

## السيناريو 1: إعداد موارد Azure والاستعداد للضبط الدقيق

### إنشاء مساحة عمل Azure Machine Learning

1. اكتب *azure machine learning* في **شريط البحث** في أعلى صفحة البوابة واختر **Azure Machine Learning** من الخيارات التي تظهر.

    ![Type azure machine learning.](../../../../../../translated_images/ar/01-01-type-azml.acae6c5455e67b4b.webp)

2. اختر **+ Create** من قائمة التنقل.

3. اختر **New workspace** من قائمة التنقل.

    ![Select new workspace.](../../../../../../translated_images/ar/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. قم بتنفيذ المهام التالية:

    - اختر اشتراك Azure الخاص بك **Subscription**.
    - اختر **مجموعة الموارد** Resource group التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - أدخل **اسم مساحة العمل** Workspace Name. يجب أن يكون قيمة فريدة.
    - اختر **المنطقة** Region التي ترغب في استخدامها.
    - اختر **حساب التخزين** Storage account الذي تريد استخدامه (قم بإنشاء واحد جديد إذا لزم الأمر).
    - اختر **خزانة المفاتيح** Key vault التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **رؤى التطبيقات** Application insights التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **سجل الحاويات** Container registry الذي تريد استخدامه (قم بإنشاء واحد جديد إذا لزم الأمر).

    ![Fill azure machine learning.](../../../../../../translated_images/ar/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. اختر **Review + Create**.

6. اختر **Create**.

### طلب حصص GPU في اشتراك Azure

في هذا الدرس، سوف تتعلم كيفية ضبط ونشر نموذج Phi-3 باستخدام وحدات معالجة الرسومات (GPUs). للضبط الدقيق، ستستخدم وحدة GPU من نوع *Standard_NC24ads_A100_v4*، والتي تتطلب طلب حصة. للنشر، ستستخدم وحدة GPU من نوع *Standard_NC6s_v3*، والتي تتطلب أيضًا طلب حصة.

> [!NOTE]
>
> الاشتراكات من نوع الدفع عند الاستخدام فقط (نوع الاشتراك القياسي) مؤهلة لتخصيص GPU؛ الاشتراكات التفضيلية غير مدعومة حاليًا.
>

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. قم بتنفيذ المهام التالية لطلب حصة *Standard NCADSA100v4 Family*:

    - اختر **Quota** من علامة التبويب على الجانب الأيسر.
    - اختر **عائلة الأجهزة الافتراضية** Virtual machine family التي تريد استخدامها. على سبيل المثال، اختر **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**، التي تشمل وحدة GPU من نوع *Standard_NC24ads_A100_v4*.
    - اختر **طلب الحصة** Request quota من قائمة التنقل.

        ![Request quota.](../../../../../../translated_images/ar/02-02-request-quota.c0428239a63ffdd5.webp)

    - داخل صفحة طلب الحصة، أدخل **حد النوى الجديد** New cores limit الذي ترغب في استخدامه. على سبيل المثال، 24.
    - داخل صفحة طلب الحصة، اختر **إرسال** Submit لطلب حصة GPU.

1. قم بتنفيذ المهام التالية لطلب حصة *Standard NCSv3 Family*:

    - اختر **Quota** من علامة التبويب على الجانب الأيسر.
    - اختر **عائلة الأجهزة الافتراضية** Virtual machine family التي تريد استخدامها. على سبيل المثال، اختر **Standard NCSv3 Family Cluster Dedicated vCPUs**، التي تشمل وحدة GPU من نوع *Standard_NC6s_v3*.
    - اختر **طلب الحصة** Request quota من قائمة التنقل.
    - داخل صفحة طلب الحصة، أدخل **حد النوى الجديد** New cores limit الذي ترغب في استخدامه. على سبيل المثال، 24.
    - داخل صفحة طلب الحصة، اختر **إرسال** Submit لطلب حصة GPU.

### إضافة تعيين دور

لضبط ونشر نماذجك، يجب أولاً إنشاء هوية مُدارة مُخصصة (User Assigned Managed Identity - UAI) ومنحها الأذونات المناسبة. سيتم استخدام هذه الهوية المُدارة للمصادقة أثناء النشر.

#### إنشاء هوية مُدارة مُخصصة (UAI)

1. اكتب *managed identities* في **شريط البحث** في أعلى صفحة البوابة واختر **Managed Identities** من الخيارات التي تظهر.

    ![Type managed identities.](../../../../../../translated_images/ar/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. اختر **+ Create**.

    ![Select create.](../../../../../../translated_images/ar/03-02-select-create.92bf8989a5cd98f2.webp)

1. قم بتنفيذ المهام التالية:

    - اختر اشتراك Azure الخاص بك **Subscription**.
    - اختر **مجموعة الموارد** Resource group التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **المنطقة** Region التي ترغب في استخدامها.
    - أدخل **الاسم** Name. يجب أن يكون قيمة فريدة.

    ![Select create.](../../../../../../translated_images/ar/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. اختر **Review + create**.

1. اختر **+ Create**.

#### إضافة تعيين دور "المساهم" إلى الهوية المُدارة

1. انتقل إلى مورد الهوية المُدارة التي قمت بإنشائها.

1. اختر **تعيينات أدوار Azure** Azure role assignments من علامة التبويب على الجانب الأيسر.

1. اختر **+ إضافة تعيين دور** +Add role assignment من قائمة التنقل.

1. داخل صفحة إضافة تعيين الدور، قم بتنفيذ المهام التالية:
    - اختر **النطاق** Scope إلى **مجموعة الموارد** Resource group.
    - اختر اشتراك Azure الخاص بك **Subscription**.
    - اختر **مجموعة الموارد** Resource group التي تريد استخدامها.
    - اختر **الدور** Role إلى **المساهم** Contributor.

    ![Fill contributor role.](../../../../../../translated_images/ar/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. اختر **حفظ** Save.

#### إضافة تعيين دور قارئ بيانات تخزين Blob إلى الهوية المُدارة

1. اكتب *storage accounts* في **شريط البحث** في أعلى صفحة البوابة واختر **Storage accounts** من الخيارات التي تظهر.

    ![Type storage accounts.](../../../../../../translated_images/ar/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. اختر حساب التخزين المرتبط بمساحة عمل Azure Machine Learning التي أنشأتها. على سبيل المثال، *finetunephistorage*.

1. قم بتنفيذ المهام التالية للتنقل إلى صفحة إضافة تعيين الدور:

    - انتقل إلى حساب تخزين Azure الذي أنشأته.
    - اختر **التحكم في الوصول (IAM)** Access Control (IAM) من علامة التبويب على الجانب الأيسر.
    - اختر **+ إضافة** + Add من قائمة التنقل.
    - اختر **إضافة تعيين دور** Add role assignment من قائمة التنقل.

    ![Add role.](../../../../../../translated_images/ar/03-06-add-role.353ccbfdcf0789c2.webp)

1. داخل صفحة إضافة تعيين الدور، قم بتنفيذ المهام التالية:

    - داخل صفحة الدور، اكتب *Storage Blob Data Reader* في **شريط البحث** واختر **Storage Blob Data Reader** من الخيارات التي تظهر.
    - داخل صفحة الدور، اختر **التالي** Next.
    - داخل صفحة الأعضاء، اختر **تعيين الوصول إلى** **هوية مُدارة** Managed identity.
    - داخل صفحة الأعضاء، اختر **+ تحديد الأعضاء** + Select members.
    - داخل صفحة تحديد الهويات المُدارة، اختر اشتراك Azure الخاص بك **Subscription**.
    - داخل صفحة تحديد الهويات المُدارة، اختر **الهوية المُدارة** Managed identity.
    - داخل صفحة تحديد الهويات المُدارة، اختر الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - داخل صفحة تحديد الهويات المُدارة، اختر **تحديد** Select.

    ![Select managed identity.](../../../../../../translated_images/ar/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. اختر **مراجعة + تعيين** Review + assign.

#### إضافة تعيين دور AcrPull إلى الهوية المُدارة

1. اكتب *container registries* في **شريط البحث** في أعلى صفحة البوابة واختر **Container registries** من الخيارات التي تظهر.

    ![Type container registries.](../../../../../../translated_images/ar/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. اختر سجل الحاويات المرتبط بمساحة عمل Azure Machine Learning. على سبيل المثال، *finetunephicontainerregistry*

1. قم بتنفيذ المهام التالية للتنقل إلى صفحة إضافة تعيين الدور:

    - اختر **التحكم في الوصول (IAM)** Access Control (IAM) من علامة التبويب على الجانب الأيسر.
    - اختر **+ إضافة** + Add من قائمة التنقل.
    - اختر **إضافة تعيين دور** Add role assignment من قائمة التنقل.

1. داخل صفحة إضافة تعيين الدور، قم بتنفيذ المهام التالية:

    - داخل صفحة الدور، اكتب *AcrPull* في **شريط البحث** واختر **AcrPull** من الخيارات التي تظهر.
    - داخل صفحة الدور، اختر **التالي** Next.
    - داخل صفحة الأعضاء، اختر **تعيين الوصول إلى** **هوية مُدارة** Managed identity.
    - داخل صفحة الأعضاء، اختر **+ تحديد الأعضاء** + Select members.
    - داخل صفحة تحديد الهويات المُدارة، اختر اشتراك Azure الخاص بك **Subscription**.
    - داخل صفحة تحديد الهويات المُدارة، اختر **الهوية المُدارة** Managed identity.
    - داخل صفحة تحديد الهويات المُدارة، اختر الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - داخل صفحة تحديد الهويات المُدارة، اختر **تحديد** Select.
    - اختر **مراجعة + تعيين** Review + assign.

### إعداد المشروع

لتنزيل مجموعات البيانات اللازمة للضبط الدقيق، ستقوم بإعداد بيئة محلية.

في هذا التمرين، ستقوم بـ

- إنشاء مجلد للعمل بداخله.
- إنشاء بيئة افتراضية.
- تثبيت الحزم المطلوبة.
- إنشاء ملف *download_dataset.py* لتنزيل مجموعة البيانات.

#### إنشاء مجلد للعمل بداخله

1. افتح نافذة الطرفية واكتب الأمر التالي لإنشاء مجلد باسم *finetune-phi* في المسار الافتراضي.

    ```console
    mkdir finetune-phi
    ```

2. اكتب الأمر التالي داخل الطرفية للانتقال إلى مجلد *finetune-phi* الذي أنشأته.

    ```console
    cd finetune-phi
    ```

#### إنشاء بيئة افتراضية

1. اكتب الأمر التالي داخل الطرفية لإنشاء بيئة افتراضية باسم *.venv*.
    ```console
    python -m venv .venv
    ```

2. اكتب الأمر التالي داخل الطرفية الخاصة بك لتنشيط البيئة الافتراضية.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> إذا نجحت العملية، يجب أن ترى *(.venv)* قبل موجه الأوامر.

#### تثبيت الحزم المطلوبة

1. اكتب الأوامر التالية في الطرفية لديك لتثبيت الحزم المطلوبة.

    ```console
    pip install datasets==2.19.1
    ```

#### إنشاء `donload_dataset.py`

> [!NOTE]
> بنية المجلد الكاملة:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. افتح **Visual Studio Code**.

1. اختر **ملف** من شريط القائمة.

1. اختر **فتح مجلد**.

1. اختر مجلد *finetune-phi* الذي أنشأته، والموجود في *C:\Users\yourUserName\finetune-phi*.

    ![اختر المجلد الذي أنشأته.](../../../../../../translated_images/ar/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. في اللوحة اليسرى من Visual Studio Code، انقر بزر الفأرة الأيمن واختر **ملف جديد** لإنشاء ملف جديد باسم *download_dataset.py*.

    ![إنشاء ملف جديد.](../../../../../../translated_images/ar/04-02-create-new-file.cf9a330a3a9cff92.webp)

### تحضير مجموعة البيانات لضبط النموذج بدقة

في هذا التمرين، ستشغّل ملف *download_dataset.py* لتحميل مجموعات بيانات *ultrachat_200k* إلى بيئتك المحلية. ثم ستستخدم هذه المجموعات لضبط نموذج Phi-3 بدقة في Azure Machine Learning.

في هذا التمرين، ستقوم بـ:

- إضافة كود إلى ملف *download_dataset.py* لتحميل مجموعات البيانات.
- تشغيل ملف *download_dataset.py* لتحميل المجموعات إلى بيئتك المحلية.

#### تحميل مجموعة البيانات باستخدام *download_dataset.py*

1. افتح ملف *download_dataset.py* في Visual Studio Code.

1. أضف الكود التالي إلى ملف *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # تحميل مجموعة البيانات بالاسم والتكوين ونسبة التقسيم المحددة
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # تقسيم مجموعة البيانات إلى مجموعات تدريب واختبار (80٪ تدريب، 20٪ اختبار)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # إنشاء الدليل إذا لم يكن موجودًا
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # فتح الملف في وضع الكتابة
        with open(filepath, 'w', encoding='utf-8') as f:
            # التكرار على كل سجل في مجموعة البيانات
            for record in dataset:
                # تفريغ السجل ككائن JSON وكتابته إلى الملف
                json.dump(record, f)
                # كتابة حرف سطر جديد لفصل السجلات
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # تحميل وتقسيم مجموعة بيانات ULTRACHAT_200k مع تكوين ونسبة تقسيم محددة
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # استخراج مجموعات بيانات التدريب والاختبار من التقسيم
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # حفظ مجموعة بيانات التدريب في ملف JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # حفظ مجموعة بيانات الاختبار في ملف JSONL منفصل
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. اكتب الأمر التالي داخل الطرفية لديك لتشغيل السكريبت وتحميل مجموعة البيانات إلى بيئتك المحلية.

    ```console
    python download_dataset.py
    ```

1. تحقق من أن مجموعات البيانات تم حفظها بنجاح في دليل *finetune-phi/data* المحلي لديك.

> [!NOTE]
>
> #### ملاحظة عن حجم مجموعة البيانات ووقت الضبط الدقيق
>
> في هذا الدرس، تستخدم فقط 1% من مجموعة البيانات (`split='train[:1%]'`). هذا يقلل بشكل كبير من حجم البيانات، مما يسرّع من عمليات الرفع والضبط الدقيق. يمكنك تعديل النسبة لإيجاد التوازن المناسب بين وقت التدريب وأداء النموذج. استخدام مجموعة فرعية أصغر يقلل الوقت المطلوب للضبط، مما يجعل العملية أكثر قابلية للإدارة في الدروس التعليمية.

## السيناريو 2: ضبط نموذج Phi-3 بدقة ونشره في Azure Machine Learning Studio

### ضبط نموذج Phi-3 بدقة

في هذا التمرين، ستقوم بضبط نموذج Phi-3 بدقة في Azure Machine Learning Studio.

في هذا التمرين، ستقوم بـ:

- إنشاء مجموعة حوسبة لضبط النموذج.
- ضبط نموذج Phi-3 بدقة في Azure Machine Learning Studio.

#### إنشاء مجموعة حوسبة لضبط النموذج

1. زر [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر **الحوسبة** من علامة التبويب الجانبية اليسرى.

1. اختر **مجموعات الحوسبة** من قائمة التنقل.

1. اختر **+ جديد**.

    ![اختر الحوسبة.](../../../../../../translated_images/ar/06-01-select-compute.a29cff290b480252.webp)

1. قم بالمهام التالية:

    - اختر **المنطقة** التي تود استخدامها.
    - حدد **نوع آلة افتراضية** إلى **مخصصة**.
    - اختر **نوع الآلة الافتراضية** إلى **GPU**.
    - عيّن فلتر **حجم الآلة الافتراضية** إلى **اختر من كل الخيارات**.
    - اختر **حجم الآلة الافتراضية** إلى **Standard_NC24ads_A100_v4**.

    ![إنشاء مجموعة.](../../../../../../translated_images/ar/06-02-create-cluster.f221b65ae1221d4e.webp)

1. اختر **التالي**.

1. قم بالمهام التالية:

    - أدخل **اسم الحوسبة**. يجب أن يكون قيمة فريدة.
    - حدد **الحد الأدنى لعدد العقد** إلى **0**.
    - حدد **الحد الأقصى لعدد العقد** إلى **1**.
    - حدد **ثواني الخمول قبل تقليل الحجم** إلى **120**.

    ![إنشاء مجموعة.](../../../../../../translated_images/ar/06-03-create-cluster.4a54ba20914f3662.webp)

1. اختر **إنشاء**.

#### ضبط نموذج Phi-3 بدقة

1. زر [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة عمل Azure Machine Learning التي أنشأتها.

    ![اختر مساحة العمل التي أنشأتها.](../../../../../../translated_images/ar/06-04-select-workspace.a92934ac04f4f181.webp)

1. قم بالمهام التالية:

    - اختر **كتالوج النماذج** من علامة التبويب الجانبية.
    - اكتب *phi-3-mini-4k* في **شريط البحث** واختر **Phi-3-mini-4k-instruct** من الخيارات التي تظهر.

    ![اكتب phi-3-mini-4k.](../../../../../../translated_images/ar/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. اختر **ضبط دقيق** من قائمة التنقل.

    ![اختر الضبط الدقيق.](../../../../../../translated_images/ar/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. قم بالمهام التالية:

    - حدد **نوع المهمة** إلى **إكمال محادثة**.
    - اختر **+ اختيار بيانات** لرفع **بيانات التدريب**.
    - حدد نوع رفع بيانات التحقق إلى **توفير بيانات تحقق مختلفة**.
    - اختر **+ اختيار بيانات** لرفع **بيانات التحقق**.

    ![املأ صفحة الضبط الدقيق.](../../../../../../translated_images/ar/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> يمكنك اختيار **الإعدادات المتقدمة** لتخصيص إعدادات مثل **learning_rate** و **lr_scheduler_type** لتحسين عملية الضبط الدقيق حسب احتياجاتك الخاصة.

1. اختر **إنهاء**.

1. في هذا التمرين، قمت بضبط نموذج Phi-3 بدقة بنجاح باستخدام Azure Machine Learning. يرجى ملاحظة أن عملية الضبط الدقيق يمكن أن تستغرق وقتاً طويلاً. بعد تشغيل مهمة الضبط الدقيق، تحتاج إلى الانتظار حتى تكتمل. يمكنك مراقبة حالة المهمة من خلال الانتقال إلى علامة التبويب "المهام" على الجانب الأيسر من مساحة عمل Azure Machine Learning. في السلسلة التالية، ستقوم بنشر النموذج المضبوط ودمجه مع Prompt flow.

    ![شاهد مهمة الضبط.](../../../../../../translated_images/ar/06-08-output.2bd32e59930672b1.webp)

### نشر نموذج Phi-3 المضبوط

لدمج نموذج Phi-3 المضبوط مع Prompt flow، تحتاج إلى نشر النموذج لجعله متاحًا للاستدلال في الوقت الحقيقي. تتضمن هذه العملية تسجيل النموذج، إنشاء نقطة نهاية عبر الإنترنت، ونشر النموذج.

في هذا التمرين، ستقوم بـ:

- تسجيل النموذج المضبوط في مساحة عمل Azure Machine Learning.
- إنشاء نقطة نهاية عبر الإنترنت.
- نشر نموذج Phi-3 المضبوط المسجل.

#### تسجيل النموذج المضبوط

1. زور [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة عمل Azure Machine Learning التي أنشأتها.

    ![اختر مساحة العمل التي أنشأتها.](../../../../../../translated_images/ar/06-04-select-workspace.a92934ac04f4f181.webp)

1. اختر **النماذج** من علامة التبويب الجانبية.
1. اختر **+ تسجيل**.
1. اختر **من مخرجات المهمة**.

    ![تسجيل النموذج.](../../../../../../translated_images/ar/07-01-register-model.ad1e7cc05e4b2777.webp)

1. اختر المهمة التي أنشأتها.

    ![اختر المهمة.](../../../../../../translated_images/ar/07-02-select-job.3e2e1144cd6cd093.webp)

1. اختر **التالي**.

1. حدد **نوع النموذج** إلى **MLflow**.

1. تأكد من اختيار **مخرجات المهمة**؛ يجب أن يكون محددًا تلقائيًا.

    ![اختر المخرجات.](../../../../../../translated_images/ar/07-03-select-output.4cf1a0e645baea1f.webp)

2. اختر **التالي**.

3. اختر **تسجيل**.

    ![اختر التسجيل.](../../../../../../translated_images/ar/07-04-register.fd82a3b293060bc7.webp)

4. يمكنك عرض النموذج الذي سجلته من خلال الانتقال إلى قائمة **النماذج** في القائمة الجانبية.

    ![النموذج المسجل.](../../../../../../translated_images/ar/07-05-registered-model.7db9775f58dfd591.webp)

#### نشر النموذج المضبوط

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **نقاط النهاية** من علامة التبويب الجانبية.

1. اختر **نقاط النهاية في الوقت الحقيقي** من قائمة التنقل.

    ![إنشاء نقطة نهاية.](../../../../../../translated_images/ar/07-06-create-endpoint.1ba865c606551f09.webp)

1. اختر **إنشاء**.

1. اختر النموذج المسجل الذي أنشأته.

    ![اختر النموذج المسجل.](../../../../../../translated_images/ar/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. اختر **اختيار**.

1. قم بالمهام التالية:

    - اختر **الآلة الافتراضية** إلى *Standard_NC6s_v3*.
    - حدد عدد **النسخ** التي ترغب باستخدامها. مثلاً، *1*.
    - اختر **النقطة النهائية** إلى **جديد** لإنشاء نقطة نهاية.
    - أدخل **اسم النقطة النهائية**. يجب أن تكون قيمة فريدة.
    - أدخل **اسم النشر**. يجب أن يكون قيمة فريدة.

    ![املأ إعدادات النشر.](../../../../../../translated_images/ar/07-08-deployment-setting.43ddc4209e673784.webp)

1. اختر **نشر**.

> [!WARNING]
> لتجنب رسوم إضافية على حسابك، تأكد من حذف نقطة النهاية التي أنشأتها في مساحة عمل Azure Machine Learning.
>

#### تحقق من حالة النشر في مساحة عمل Azure Machine Learning

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **نقاط النهاية** من علامة التبويب الجانبية.

1. اختر نقطة النهاية التي أنشأتها.

    ![اختر نقاط النهاية](../../../../../../translated_images/ar/07-09-check-deployment.325d18cae8475ef4.webp)

1. في هذه الصفحة، يمكنك إدارة نقاط النهاية أثناء عملية النشر.

> [!NOTE]
> بمجرد اكتمال النشر، تأكد من تعيين **حركة المرور الحية** إلى **100%**. إذا لم تكن كذلك، اختر **تحديث حركة المرور** لتعديل الإعدادات. لاحظ أنه لا يمكنك اختبار النموذج إذا كانت حركة المرور مضبوطة إلى 0%.
>
> ![عيّن حركة المرور.](../../../../../../translated_images/ar/07-10-set-traffic.085b847e5751ff3d.webp)
>

## السيناريو 3: التكامل مع Prompt flow والمحادثة مع نموذجك المخصص في Microsoft Foundry

### دمج نموذج Phi-3 المخصص مع Prompt flow

بعد نشر نموذجك المضبوط بنجاح، يمكنك الآن دمجه مع Prompt Flow لاستخدام نموذجك في تطبيقات الوقت الحقيقي، مما يمكّنك من تنفيذ مهام تفاعلية متنوعة باستخدام نموذج Phi-3 المخصص لديك.

في هذا التمرين، ستقوم بـ:

- إنشاء Microsoft Foundry Hub.
- إنشاء مشروع Microsoft Foundry.
- إنشاء Prompt flow.
- إضافة اتصال مخصص لنموذج Phi-3 المضبوط.
- إعداد Prompt flow للمحادثة مع نموذج Phi-3 المخصص.

> [!NOTE]
> يمكنك أيضًا الدمج مع Promptflow باستخدام Azure ML Studio. نفس عملية الدمج يمكن تطبيقها على Azure ML Studio.

#### إنشاء Microsoft Foundry Hub

يجب عليك إنشاء Hub قبل إنشاء المشروع. يعمل الـ Hub كـ Resource Group، مما يتيح لك تنظيم وإدارة عدة مشاريع داخل Microsoft Foundry.
1. زر [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. اختر **جميع المحاور** من علامة التبويب الجانبية.

1. اختر **+ محور جديد** من قائمة التنقل.

    ![إنشاء المحور.](../../../../../../translated_images/ar/08-01-create-hub.8f7dd615bb8d9834.webp)

1. قم بالمهام التالية:

    - أدخل **اسم المحور**. يجب أن يكون قيمة فريدة.
    - اختر **الاشتراك** الخاص بك في Azure.
    - اختر **مجموعة الموارد** التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **الموقع** الذي ترغب في استخدامه.
    - اختر **الاتصال بخدمات Azure AI** التي تريد استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **الاتصال بـ Azure AI Search** إلى **تخطي الاتصال**.

    ![املأ المحور.](../../../../../../translated_images/ar/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. اختر **التالي**.

#### إنشاء مشروع Microsoft Foundry

1. في المحور الذي أنشأته، اختر **جميع المشاريع** من علامة التبويب الجانبية.

1. اختر **+ مشروع جديد** من قائمة التنقل.

    ![اختر مشروع جديد.](../../../../../../translated_images/ar/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. أدخل **اسم المشروع**. يجب أن يكون قيمة فريدة.

    ![إنشاء المشروع.](../../../../../../translated_images/ar/08-05-create-project.4d97f0372f03375a.webp)

1. اختر **إنشاء مشروع**.

#### إضافة اتصال مخصص لنموذج Phi-3 الذي تم ضبطه بدقة

لدمج نموذج Phi-3 المخصص مع Prompt flow، تحتاج إلى حفظ نقطة النهاية والمفتاح الخاص بالنموذج في اتصال مخصص. هذا الإعداد يضمن الوصول إلى نموذج Phi-3 المخصص في Prompt flow.

#### تعيين مفتاح api وعنوان نقطة النهاية لنموذج Phi-3 الذي تم ضبطه بدقة

1. زر [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مساحة عمل Azure Machine learning التي أنشأتها.

1. اختر **نقاط النهاية** من علامة التبويب الجانبية.

    ![اختر نقاط النهاية.](../../../../../../translated_images/ar/08-06-select-endpoints.aff38d453bcf9605.webp)

1. اختر نقطة النهاية التي أنشأتها.

    ![اختر نقطة النهاية المنشأة.](../../../../../../translated_images/ar/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. اختر **استهلاك** من قائمة التنقل.

1. انسخ **نقطة النهاية REST** و **المفتاح الرئيسي** الخاصين بك.

    ![انسخ مفتاح api وعنوان نقطة النهاية.](../../../../../../translated_images/ar/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### أضف الاتصال المخصص

1. زر [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مشروع Microsoft Foundry الذي أنشأته.

1. في المشروع الذي أنشأته، اختر **الإعدادات** من علامة التبويب الجانبية.

1. اختر **+ اتصال جديد**.

    ![اختر اتصال جديد.](../../../../../../translated_images/ar/08-09-select-new-connection.02eb45deadc401fc.webp)

1. اختر **مفاتيح مخصصة** من قائمة التنقل.

    ![اختر مفاتيح مخصصة.](../../../../../../translated_images/ar/08-10-select-custom-keys.856f6b2966460551.webp)

1. قم بالمهام التالية:

    - اختر **+ إضافة أزواج مفتاح وقيمة**.
    - لاسم المفتاح، أدخل **endpoint** والصق نقطة النهاية التي نسختها من Azure ML Studio في حقل القيمة.
    - اختر **+ إضافة أزواج مفتاح وقيمة** مرة أخرى.
    - لاسم المفتاح، أدخل **key** والصق المفتاح الذي نسخته من Azure ML Studio في حقل القيمة.
    - بعد إضافة المفاتيح، اختر **is secret** لمنع تعرض المفتاح.

    ![أضف الاتصال.](../../../../../../translated_images/ar/08-11-add-connection.785486badb4d2d26.webp)

1. اختر **إضافة اتصال**.

#### إنشاء Prompt flow

لقد أضفت اتصالاً مخصصًا في Microsoft Foundry. الآن، لنقم بإنشاء Prompt flow باستخدام الخطوات التالية. ثم ستقوم بتوصيل هذا الـ Prompt flow بالاتصال المخصص لكي تتمكن من استخدام النموذج المضبوط بدقة داخل Prompt flow.

1. انتقل إلى مشروع Microsoft Foundry الذي أنشأته.

1. اختر **Prompt flow** من علامة التبويب الجانبية.

1. اختر **+ إنشاء** من قائمة التنقل.

    ![اختر Promptflow.](../../../../../../translated_images/ar/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. اختر **تدفق الدردشة** من قائمة التنقل.

    ![اختر تدفق الدردشة.](../../../../../../translated_images/ar/08-13-select-flow-type.2ec689b22da32591.webp)

1. أدخل **اسم المجلد** الذي تريد استخدامه.

    ![أدخل الاسم.](../../../../../../translated_images/ar/08-14-enter-name.ff9520fefd89f40d.webp)

2. اختر **إنشاء**.

#### إعداد Prompt flow للدردشة مع نموذج Phi-3 المخصص الخاص بك

تحتاج إلى دمج نموذج Phi-3 المضبوط بدقة في Prompt flow. ومع ذلك، فإن Prompt flow الموجود حاليًا ليس مصممًا لهذا الغرض، لذا يجب إعادة تصميمه لتمكين دمج النموذج المخصص.

1. في Prompt flow، قم بالمهام التالية لإعادة بناء التدفق الحالي:

    - اختر **وضع الملف الخام**.
    - احذف كل الأكواد الموجودة في ملف *flow.dag.yml*.
    - أضف الكود التالي إلى ملف *flow.dag.yml*.

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

    ![اختر وضع الملف الخام.](../../../../../../translated_images/ar/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. أضف الكود التالي إلى ملف *integrate_with_promptflow.py* لاستخدام نموذج Phi-3 المخصص في Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # إعداد التسجيل
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

        # "connection" هو اسم الاتصال المخصص، "endpoint"، "key" هي المفاتيح في الاتصال المخصص
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
            
            # سجّل الاستجابة الكاملة بصيغة JSON
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

    ![الصق كود prompt flow.](../../../../../../translated_images/ar/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!ملاحظة]
> لمزيد من المعلومات التفصيلية حول استخدام Prompt flow في Microsoft Foundry، يمكنك الرجوع إلى [Prompt flow في Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. اختر **إدخال الدردشة**، **إخراج الدردشة** لتمكين الدردشة مع نموذجك.

    ![إدخال وإخراج.](../../../../../../translated_images/ar/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. الآن أنت جاهز للدردشة مع نموذج Phi-3 المخصص الخاص بك. في التمرين التالي، ستتعلم كيفية بدء Prompt flow واستخدامه للدردشة مع نموذج Phi-3 المضبوط بدقة.

> [!ملاحظة]
>
> يجب أن يبدو التدفق المعاد بناؤه كما في الصورة أدناه:
>
> ![مثال على التدفق.](../../../../../../translated_images/ar/08-18-graph-example.d6457533952e690c.webp)
>

### الدردشة مع نموذج Phi-3 المخصص الخاص بك

بعد أن قمت بضبط نموذج Phi-3 المخصص ودمجه مع Prompt flow، أنت جاهز الآن لبدء التفاعل معه. سيرشدك هذا التمرين خلال عملية إعداد وبدء محادثة مع نموذجك باستخدام Prompt flow. باتباع هذه الخطوات، ستتمكن من الاستفادة الكاملة من قدرات نموذج Phi-3 المضبوط لمهام مختلفة ومحادثات متنوعة.

- دردش مع نموذج Phi-3 المخصص باستخدام Prompt flow.

#### بدء Prompt flow

1. اختر **بدء جلسات الحوسبة** لبدء Prompt flow.

    ![بدء جلسة الحوسبة.](../../../../../../translated_images/ar/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. اختر **التحقق من صحة وتحليل الإدخال** لتجديد المعلمات.

    ![تحقق من صحة الإدخال.](../../../../../../translated_images/ar/09-02-validate-input.317c76ef766361e9.webp)

1. اختر **القيمة** الخاصة بـ **الاتصال** للاتصال المخصص الذي أنشأته. على سبيل المثال، *connection*.

    ![الاتصال.](../../../../../../translated_images/ar/09-03-select-connection.99bdddb4b1844023.webp)

#### الدردشة مع نموذجك المخصص

1. اختر **الدردشة**.

    ![اختر الدردشة.](../../../../../../translated_images/ar/09-04-select-chat.61936dce6612a1e6.webp)

1. فيما يلي مثال على النتائج: يمكنك الآن الدردشة مع نموذج Phi-3 المخصص الخاص بك. يُنصح بطرح أسئلة بناءً على البيانات المستخدمة في الضبط الدقيق.

    ![الدردشة مع prompt flow.](../../../../../../translated_images/ar/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالحصول على ترجمة مهنية من قبل مترجم بشري. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->