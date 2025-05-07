<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-07T11:00:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ar"
}
-->
# ضبط وتكامل نماذج Phi-3 المخصصة مع Prompt flow في Azure AI Foundry

تعتمد هذه العينة الشاملة (E2E) على الدليل "[ضبط وتكامل نماذج Phi-3 المخصصة مع Prompt Flow في Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" من مجتمع Microsoft Tech. تقدم هذه العينة عمليات الضبط الدقيق، والنشر، والتكامل لنماذج Phi-3 المخصصة مع Prompt flow في Azure AI Foundry.
على عكس العينة الشاملة، "[ضبط وتكامل نماذج Phi-3 المخصصة مع Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)"، التي تضمنت تشغيل الكود محليًا، يركز هذا الدليل بالكامل على ضبط وتكامل النموذج الخاص بك داخل Azure AI / ML Studio.

## نظرة عامة

في هذه العينة الشاملة، ستتعلم كيفية ضبط نموذج Phi-3 ودمجه مع Prompt flow في Azure AI Foundry. من خلال الاستفادة من Azure AI / ML Studio، ستنشئ سير عمل لنشر واستخدام نماذج الذكاء الاصطناعي المخصصة. تنقسم هذه العينة إلى ثلاث سيناريوهات:

**السيناريو 1: إعداد موارد Azure والتحضير للضبط الدقيق**

**السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio**

**السيناريو 3: التكامل مع Prompt flow والدردشة مع نموذجك المخصص في Azure AI Foundry**

إليك نظرة عامة على هذه العينة الشاملة.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.ar.png)

### جدول المحتويات

1. **[السيناريو 1: إعداد موارد Azure والتحضير للضبط الدقيق](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [إنشاء مساحة عمل Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [طلب حصص GPU في اشتراك Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [إضافة تعيين دور](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [إعداد المشروع](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [تحضير مجموعة البيانات للضبط الدقيق](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ضبط نموذج Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [نشر نموذج Phi-3 المضبوط](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[السيناريو 3: التكامل مع Prompt flow والدردشة مع نموذجك المخصص في Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [تكامل نموذج Phi-3 المخصص مع Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [الدردشة مع نموذج Phi-3 المخصص الخاص بك](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## السيناريو 1: إعداد موارد Azure والتحضير للضبط الدقيق

### إنشاء مساحة عمل Azure Machine Learning

1. اكتب *azure machine learning* في **شريط البحث** أعلى صفحة البوابة واختر **Azure Machine Learning** من الخيارات التي تظهر.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.ar.png)

2. اختر **+ إنشاء** من قائمة التنقل.

3. اختر **مساحة عمل جديدة** من قائمة التنقل.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.ar.png)

4. قم بالمهام التالية:

    - اختر **الاشتراك** الخاص بك في Azure.
    - اختر **مجموعة الموارد** التي تريد استخدامها (أنشئ واحدة جديدة إذا لزم الأمر).
    - أدخل **اسم مساحة العمل**. يجب أن يكون قيمة فريدة.
    - اختر **المنطقة** التي ترغب في استخدامها.
    - اختر **حساب التخزين** الذي تريد استخدامه (أنشئ واحدًا جديدًا إذا لزم الأمر).
    - اختر **مخزن المفاتيح** الذي تريد استخدامه (أنشئ واحدًا جديدًا إذا لزم الأمر).
    - اختر **Application insights** الذي تريد استخدامه (أنشئ واحدًا جديدًا إذا لزم الأمر).
    - اختر **سجل الحاويات** الذي تريد استخدامه (أنشئ واحدًا جديدًا إذا لزم الأمر).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.ar.png)

5. اختر **مراجعة + إنشاء**.

6. اختر **إنشاء**.

### طلب حصص GPU في اشتراك Azure

في هذا الدليل، ستتعلم كيفية ضبط ونشر نموذج Phi-3 باستخدام وحدات معالجة الرسوميات (GPUs). للضبط الدقيق، ستستخدم GPU من نوع *Standard_NC24ads_A100_v4*، والذي يتطلب طلب حصة. للنشر، ستستخدم GPU من نوع *Standard_NC6s_v3*، والذي يتطلب أيضًا طلب حصة.

> [!NOTE]
>
> الاشتراكات من نوع Pay-As-You-Go فقط (نوع الاشتراك القياسي) مؤهلة لتخصيص GPU؛ الاشتراكات ذات الفوائد غير مدعومة حاليًا.
>

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. قم بالمهام التالية لطلب حصة *Standard NCADSA100v4 Family*:

    - اختر **الحصص** من علامة التبويب الجانبية.
    - اختر **عائلة الأجهزة الافتراضية** التي تريد استخدامها. على سبيل المثال، اختر **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**، والتي تتضمن GPU من نوع *Standard_NC24ads_A100_v4*.
    - اختر **طلب الحصة** من قائمة التنقل.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.ar.png)

    - في صفحة طلب الحصة، أدخل **الحد الجديد للنوى** الذي ترغب في استخدامه. على سبيل المثال، 24.
    - في صفحة طلب الحصة، اختر **إرسال** لطلب حصة GPU.

1. قم بالمهام التالية لطلب حصة *Standard NCSv3 Family*:

    - اختر **الحصص** من علامة التبويب الجانبية.
    - اختر **عائلة الأجهزة الافتراضية** التي تريد استخدامها. على سبيل المثال، اختر **Standard NCSv3 Family Cluster Dedicated vCPUs**، والتي تتضمن GPU من نوع *Standard_NC6s_v3*.
    - اختر **طلب الحصة** من قائمة التنقل.
    - في صفحة طلب الحصة، أدخل **الحد الجديد للنوى** الذي ترغب في استخدامه. على سبيل المثال، 24.
    - في صفحة طلب الحصة، اختر **إرسال** لطلب حصة GPU.

### إضافة تعيين دور

لضبط ونشر نماذجك، يجب أولاً إنشاء هوية مُدارة مخصصة للمستخدم (UAI) ومنحها الأذونات المناسبة. ستُستخدم هذه الهوية المُدارة للمصادقة أثناء النشر.

#### إنشاء هوية مُدارة مخصصة للمستخدم (UAI)

1. اكتب *managed identities* في **شريط البحث** أعلى صفحة البوابة واختر **Managed Identities** من الخيارات التي تظهر.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.ar.png)

1. اختر **+ إنشاء**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.ar.png)

1. قم بالمهام التالية:

    - اختر **الاشتراك** الخاص بك في Azure.
    - اختر **مجموعة الموارد** التي تريد استخدامها (أنشئ واحدة جديدة إذا لزم الأمر).
    - اختر **المنطقة** التي ترغب في استخدامها.
    - أدخل **الاسم**. يجب أن يكون قيمة فريدة.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.ar.png)

1. اختر **مراجعة + إنشاء**.

1. اختر **+ إنشاء**.

#### إضافة تعيين دور Contributor إلى الهوية المُدارة

1. انتقل إلى مورد الهوية المُدارة الذي أنشأته.

1. اختر **تعيينات أدوار Azure** من علامة التبويب الجانبية.

1. اختر **+ إضافة تعيين دور** من قائمة التنقل.

1. في صفحة إضافة تعيين دور، قم بالمهام التالية:
    - اختر **النطاق** إلى **مجموعة الموارد**.
    - اختر **الاشتراك** الخاص بك في Azure.
    - اختر **مجموعة الموارد** التي تريد استخدامها.
    - اختر **الدور** إلى **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.ar.png)

2. اختر **حفظ**.

#### إضافة تعيين دور Storage Blob Data Reader إلى الهوية المُدارة

1. اكتب *storage accounts* في **شريط البحث** أعلى صفحة البوابة واختر **Storage accounts** من الخيارات التي تظهر.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.ar.png)

1. اختر حساب التخزين المرتبط بمساحة عمل Azure Machine Learning التي أنشأتها. على سبيل المثال، *finetunephistorage*.

1. قم بالمهام التالية للانتقال إلى صفحة إضافة تعيين دور:

    - انتقل إلى حساب تخزين Azure الذي أنشأته.
    - اختر **التحكم في الوصول (IAM)** من علامة التبويب الجانبية.
    - اختر **+ إضافة** من قائمة التنقل.
    - اختر **إضافة تعيين دور** من قائمة التنقل.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.ar.png)

1. في صفحة إضافة تعيين دور، قم بالمهام التالية:

    - في صفحة الدور، اكتب *Storage Blob Data Reader* في **شريط البحث** واختر **Storage Blob Data Reader** من الخيارات التي تظهر.
    - في صفحة الدور، اختر **التالي**.
    - في صفحة الأعضاء، اختر **تعيين الوصول إلى** **Managed identity**.
    - في صفحة الأعضاء، اختر **+ تحديد الأعضاء**.
    - في صفحة تحديد الهويات المُدارة، اختر **الاشتراك** الخاص بك في Azure.
    - في صفحة تحديد الهويات المُدارة، اختر **الهوية المُدارة** إلى **Manage Identity**.
    - في صفحة تحديد الهويات المُدارة، اختر الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - في صفحة تحديد الهويات المُدارة، اختر **تحديد**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.ar.png)

1. اختر **مراجعة + تعيين**.

#### إضافة تعيين دور AcrPull إلى الهوية المُدارة

1. اكتب *container registries* في **شريط البحث** أعلى صفحة البوابة واختر **Container registries** من الخيارات التي تظهر.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.ar.png)

1. اختر سجل الحاويات المرتبط بمساحة عمل Azure Machine Learning. على سبيل المثال، *finetunephicontainerregistry*

1. قم بالمهام التالية للانتقال إلى صفحة إضافة تعيين دور:

    - اختر **التحكم في الوصول (IAM)** من علامة التبويب الجانبية.
    - اختر **+ إضافة** من قائمة التنقل.
    - اختر **إضافة تعيين دور** من قائمة التنقل.

1. في صفحة إضافة تعيين دور، قم بالمهام التالية:

    - في صفحة الدور، اكتب *AcrPull* في **شريط البحث** واختر **AcrPull** من الخيارات التي تظهر.
    - في صفحة الدور، اختر **التالي**.
    - في صفحة الأعضاء، اختر **تعيين الوصول إلى** **Managed identity**.
    - في صفحة الأعضاء، اختر **+ تحديد الأعضاء**.
    - في صفحة تحديد الهويات المُدارة، اختر **الاشتراك** الخاص بك في Azure.
    - في صفحة تحديد الهويات المُدارة، اختر **الهوية المُدارة** إلى **Manage Identity**.
    - في صفحة تحديد الهويات المُدارة، اختر الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - في صفحة تحديد الهويات المُدارة، اختر **تحديد**.
    - اختر **مراجعة + تعيين**.

### إعداد المشروع

لتحميل مجموعات البيانات اللازمة للضبط الدقيق، ستقوم بإعداد بيئة محلية.

في هذا التمرين، ستقوم بـ

- إنشاء مجلد للعمل بداخله.
- إنشاء بيئة افتراضية.
- تثبيت الحزم المطلوبة.
- إنشاء ملف *download_dataset.py* لتحميل مجموعة البيانات.

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

2. اكتب الأمر التالي داخل الطرفية لتنشيط البيئة الافتراضية.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> إذا نجح الأمر، يجب أن ترى *(.venv)* قبل موجه الأوامر.

#### تثبيت الحزم المطلوبة

1. اكتب الأوامر التالية داخل الطرفية لتثبيت الحزم المطلوبة.

    ```console
    pip install datasets==2.19.1
    ```

#### إنشاء `download_dataset.py`

> [!NOTE]
> الهيكل الكامل للمجلد:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. افتح **Visual Studio Code**.

1. اختر **ملف** من شريط القوائم.

1. اختر **فتح مجلد**.

1. اختر مجلد *finetune-phi* الذي أنشأته، الموجود في *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.ar.png)

1. في اللوحة اليسرى في Visual Studio Code، انقر بزر الماوس الأيمن واختر **ملف جديد** لإنشاء ملف جديد باسم *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.ar.png)

### تحضير مجموعة البيانات للضبط الدقيق

في هذا التمرين، ستشغل ملف *download_dataset.py* لتحميل مجموعات بيانات *ultrachat_200k* إلى بيئتك المحلية. ثم ستستخدم هذه المجموعات لضبط نموذج Phi-3 في Azure Machine Learning.

في هذا التمرين، ستقوم بـ:

- إضافة كود إلى ملف *download_dataset.py* لتحميل مجموعات البيانات.
- تشغيل ملف *download_dataset.py* لتحميل مجموعات البيانات إلى بيئتك المحلية.

#### تحميل مجموعة البيانات باستخدام *download_dataset.py*

1. افتح ملف *download_dataset.py* في Visual Studio Code.

1. أضف الكود التالي داخل ملف *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. اكتب الأمر التالي داخل الطرفية لتشغيل السكريبت وتحميل مجموعة البيانات إلى بيئتك المحلية.

    ```console
    python download_dataset.py
    ```

1. تحقق من أن مجموعات البيانات تم حفظها بنجاح في دليل *finetune-phi/data* المحلي الخاص بك.

> [!NOTE]
>
> #### ملاحظة حول حجم مجموعة البيانات ووقت الضبط الدقيق
>
> في هذا الدليل، تستخدم فقط 1% من مجموعة البيانات (`split='train[:1%]'`). هذا يقلل بشكل كبير من حجم البيانات، مما يسرع كل من عملية الرفع والضبط الدقيق. يمكنك تعديل النسبة لإيجاد التوازن المناسب بين وقت التدريب وأداء النموذج. استخدام جزء أصغر من مجموعة البيانات يقلل من الوقت المطلوب للضبط الدقيق، مما يجعل العملية أكثر قابلية للإدارة في سياق الدليل.

## السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio

### ضبط نموذج Phi-3

في هذا التمرين، ستقوم بضبط نموذج Phi-3 في Azure Machine Learning Studio.

في هذا التمرين، ستقوم بـ:

- إنشاء عنقود حوسبة للضبط الدقيق.
- ضبط نموذج Phi-3 في Azure Machine Learning Studio.

#### إنشاء عنقود حوسبة للضبط الدقيق
1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر **Compute** من علامة التبويب على الجانب الأيسر.

1. اختر **Compute clusters** من قائمة التنقل.

1. اختر **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.ar.png)

1. قم بالمهام التالية:

    - اختر **Region** التي ترغب في استخدامها.
    - اختر **Virtual machine tier** إلى **Dedicated**.
    - اختر **Virtual machine type** إلى **GPU**.
    - اختر فلتر **Virtual machine size** إلى **Select from all options**.
    - اختر **Virtual machine size** إلى **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.ar.png)

1. اختر **Next**.

1. قم بالمهام التالية:

    - أدخل **Compute name**. يجب أن يكون قيمة فريدة.
    - اختر **Minimum number of nodes** إلى **0**.
    - اختر **Maximum number of nodes** إلى **1**.
    - اختر **Idle seconds before scale down** إلى **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.ar.png)

1. اختر **Create**.

#### ضبط نموذج Phi-3 بدقة

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة عمل Azure Machine Learning التي أنشأتها.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ar.png)

1. قم بالمهام التالية:

    - اختر **Model catalog** من علامة التبويب على الجانب الأيسر.
    - اكتب *phi-3-mini-4k* في **شريط البحث** واختر **Phi-3-mini-4k-instruct** من الخيارات التي تظهر.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.ar.png)

1. اختر **Fine-tune** من قائمة التنقل.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.ar.png)

1. قم بالمهام التالية:

    - اختر **Select task type** إلى **Chat completion**.
    - اختر **+ Select data** لتحميل **Traning data**.
    - اختر نوع تحميل بيانات التحقق إلى **Provide different validation data**.
    - اختر **+ Select data** لتحميل **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.ar.png)

    > [!TIP]
    >
    > يمكنك اختيار **Advanced settings** لتخصيص الإعدادات مثل **learning_rate** و **lr_scheduler_type** لتحسين عملية الضبط الدقيق حسب احتياجاتك الخاصة.

1. اختر **Finish**.

1. في هذا التمرين، قمت بضبط نموذج Phi-3 بدقة باستخدام Azure Machine Learning بنجاح. يرجى ملاحظة أن عملية الضبط الدقيق قد تستغرق وقتًا طويلاً. بعد تشغيل مهمة الضبط الدقيق، تحتاج إلى الانتظار حتى تكتمل. يمكنك مراقبة حالة مهمة الضبط الدقيق من خلال الانتقال إلى علامة التبويب Jobs على الجانب الأيسر من مساحة عمل Azure Machine Learning الخاصة بك. في السلسلة التالية، ستقوم بنشر النموذج المضبوط ودمجه مع Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.ar.png)

### نشر نموذج Phi-3 المضبوط

لدمج نموذج Phi-3 المضبوط مع Prompt flow، تحتاج إلى نشر النموذج لجعله متاحًا للاستدلال في الوقت الحقيقي. تتضمن هذه العملية تسجيل النموذج، إنشاء نقطة نهاية عبر الإنترنت، ونشر النموذج.

في هذا التمرين، ستقوم بـ:

- تسجيل النموذج المضبوط في مساحة عمل Azure Machine Learning.
- إنشاء نقطة نهاية عبر الإنترنت.
- نشر نموذج Phi-3 المضبوط المسجل.

#### تسجيل النموذج المضبوط

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة عمل Azure Machine Learning التي أنشأتها.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ar.png)

1. اختر **Models** من علامة التبويب على الجانب الأيسر.
1. اختر **+ Register**.
1. اختر **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.ar.png)

1. اختر المهمة التي أنشأتها.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.ar.png)

1. اختر **Next**.

1. اختر **Model type** إلى **MLflow**.

1. تأكد من اختيار **Job output**؛ يجب أن يكون محددًا تلقائيًا.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.ar.png)

2. اختر **Next**.

3. اختر **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.ar.png)

4. يمكنك عرض النموذج المسجل من خلال الانتقال إلى قائمة **Models** من علامة التبويب على الجانب الأيسر.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.ar.png)

#### نشر النموذج المضبوط

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **Endpoints** من علامة التبويب على الجانب الأيسر.

1. اختر **Real-time endpoints** من قائمة التنقل.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.ar.png)

1. اختر **Create**.

1. اختر النموذج المسجل الذي أنشأته.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.ar.png)

1. اختر **Select**.

1. قم بالمهام التالية:

    - اختر **Virtual machine** إلى *Standard_NC6s_v3*.
    - اختر عدد **Instance count** الذي ترغب في استخدامه. على سبيل المثال، *1*.
    - اختر **Endpoint** إلى **New** لإنشاء نقطة نهاية جديدة.
    - أدخل **Endpoint name**. يجب أن يكون قيمة فريدة.
    - أدخل **Deployment name**. يجب أن يكون قيمة فريدة.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.ar.png)

1. اختر **Deploy**.

> [!WARNING]
> لتجنب رسوم إضافية على حسابك، تأكد من حذف نقطة النهاية التي أنشأتها في مساحة عمل Azure Machine Learning.
>

#### التحقق من حالة النشر في مساحة عمل Azure Machine Learning

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **Endpoints** من علامة التبويب على الجانب الأيسر.

1. اختر نقطة النهاية التي أنشأتها.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.ar.png)

1. في هذه الصفحة، يمكنك إدارة نقاط النهاية أثناء عملية النشر.

> [!NOTE]
> بمجرد اكتمال النشر، تأكد من ضبط **Live traffic** إلى **100%**. إذا لم يكن كذلك، اختر **Update traffic** لضبط إعدادات حركة المرور. لاحظ أنه لا يمكنك اختبار النموذج إذا كانت حركة المرور مضبوطة على 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.ar.png)
>

## السيناريو 3: الدمج مع Prompt flow والدردشة مع نموذجك المخصص في Azure AI Foundry

### دمج نموذج Phi-3 المخصص مع Prompt flow

بعد نشر نموذجك المضبوط بنجاح، يمكنك الآن دمجه مع Prompt Flow لاستخدام نموذجك في التطبيقات الحية، مما يتيح مجموعة متنوعة من المهام التفاعلية مع نموذج Phi-3 المخصص الخاص بك.

في هذا التمرين، ستقوم بـ:

- إنشاء Azure AI Foundry Hub.
- إنشاء مشروع Azure AI Foundry.
- إنشاء Prompt flow.
- إضافة اتصال مخصص لنموذج Phi-3 المضبوط.
- إعداد Prompt flow للدردشة مع نموذج Phi-3 المخصص الخاص بك.

> [!NOTE]
> يمكنك أيضًا الدمج مع Promptflow باستخدام Azure ML Studio. يمكن تطبيق نفس عملية الدمج على Azure ML Studio.

#### إنشاء Azure AI Foundry Hub

تحتاج إلى إنشاء Hub قبل إنشاء المشروع. يعمل الـ Hub كمجموعة موارد، مما يتيح لك تنظيم وإدارة مشاريع متعددة داخل Azure AI Foundry.

1. قم بزيارة [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. اختر **All hubs** من علامة التبويب على الجانب الأيسر.

1. اختر **+ New hub** من قائمة التنقل.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.ar.png)

1. قم بالمهام التالية:

    - أدخل **Hub name**. يجب أن يكون قيمة فريدة.
    - اختر اشتراك Azure الخاص بك **Subscription**.
    - اختر **Resource group** التي ترغب في استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Location** التي ترغب في استخدامها.
    - اختر **Connect Azure AI Services** التي ترغب في استخدامها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Connect Azure AI Search** إلى **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.ar.png)

1. اختر **Next**.

#### إنشاء مشروع Azure AI Foundry

1. في الـ Hub الذي أنشأته، اختر **All projects** من علامة التبويب على الجانب الأيسر.

1. اختر **+ New project** من قائمة التنقل.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.ar.png)

1. أدخل **Project name**. يجب أن يكون قيمة فريدة.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.ar.png)

1. اختر **Create a project**.

#### إضافة اتصال مخصص لنموذج Phi-3 المضبوط

لدمج نموذج Phi-3 المخصص مع Prompt flow، تحتاج إلى حفظ نقطة النهاية والمفتاح الخاص بالنموذج في اتصال مخصص. هذا الإعداد يضمن الوصول إلى نموذج Phi-3 المخصص في Prompt flow.

#### تعيين مفتاح API وعنوان URI لنقطة النهاية لنموذج Phi-3 المضبوط

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **Endpoints** من علامة التبويب على الجانب الأيسر.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.ar.png)

1. اختر نقطة النهاية التي أنشأتها.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.ar.png)

1. اختر **Consume** من قائمة التنقل.

1. انسخ **REST endpoint** و **Primary key** الخاصين بك.
![انسخ مفتاح api وعنوان نقطة النهاية.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.ar.png)

#### إضافة الاتصال المخصص

1. قم بزيارة [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مشروع Azure AI Foundry الذي أنشأته.

1. في المشروع الذي أنشأته، اختر **الإعدادات** من علامة التبويب الجانبية اليسرى.

1. اختر **+ اتصال جديد**.

    ![اختر اتصال جديد.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.ar.png)

1. اختر **مفاتيح مخصصة** من قائمة التنقل.

    ![اختر المفاتيح المخصصة.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.ar.png)

1. قم بالمهام التالية:

    - اختر **+ إضافة أزواج قيم المفتاح**.
    - بالنسبة لاسم المفتاح، أدخل **endpoint** والصق نقطة النهاية التي نسختها من Azure ML Studio في حقل القيمة.
    - اختر **+ إضافة أزواج قيم المفتاح** مرة أخرى.
    - بالنسبة لاسم المفتاح، أدخل **key** والصق المفتاح الذي نسخته من Azure ML Studio في حقل القيمة.
    - بعد إضافة المفاتيح، اختر **is secret** لمنع الكشف عن المفتاح.

    ![إضافة الاتصال.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.ar.png)

1. اختر **إضافة الاتصال**.

#### إنشاء Prompt flow

لقد أضفت اتصالًا مخصصًا في Azure AI Foundry. الآن، دعنا ننشئ Prompt flow باستخدام الخطوات التالية. ثم، ستقوم بربط هذا Prompt flow بالاتصال المخصص حتى تتمكن من استخدام النموذج المُحسّن داخل Prompt flow.

1. انتقل إلى مشروع Azure AI Foundry الذي أنشأته.

1. اختر **Prompt flow** من علامة التبويب الجانبية اليسرى.

1. اختر **+ إنشاء** من قائمة التنقل.

    ![اختر Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.ar.png)

1. اختر **تدفق الدردشة** من قائمة التنقل.

    ![اختر تدفق الدردشة.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.ar.png)

1. أدخل **اسم المجلد** الذي تريد استخدامه.

    ![أدخل الاسم.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.ar.png)

2. اختر **إنشاء**.

#### إعداد Prompt flow للدردشة مع نموذج Phi-3 المخصص الخاص بك

تحتاج إلى دمج نموذج Phi-3 المحسّن داخل Prompt flow. مع ذلك، فإن Prompt flow الحالي المقدم غير مصمم لهذا الغرض. لذلك، يجب إعادة تصميم Prompt flow لتمكين دمج النموذج المخصص.

1. في Prompt flow، قم بالمهام التالية لإعادة بناء التدفق الحالي:

    - اختر **وضع الملف الخام**.
    - احذف كل الكود الموجود في ملف *flow.dag.yml*.
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

    ![اختر وضع الملف الخام.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.ar.png)

1. أضف الكود التالي إلى ملف *integrate_with_promptflow.py* لاستخدام نموذج Phi-3 المخصص في Prompt flow.

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

    ![الصق كود prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.ar.png)

> [!NOTE]
> لمزيد من المعلومات التفصيلية حول استخدام Prompt flow في Azure AI Foundry، يمكنك الرجوع إلى [Prompt flow في Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. اختر **مدخلات الدردشة**، **مخرجات الدردشة** لتمكين الدردشة مع نموذجك.

    ![المدخلات والمخرجات.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.ar.png)

1. الآن أنت جاهز للدردشة مع نموذج Phi-3 المخصص الخاص بك. في التمرين التالي، ستتعلم كيفية بدء Prompt flow واستخدامه للدردشة مع نموذج Phi-3 المحسّن.

> [!NOTE]
>
> يجب أن يبدو التدفق المعاد بناؤه مثل الصورة أدناه:
>
> ![مثال على التدفق.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.ar.png)
>

### الدردشة مع نموذج Phi-3 المخصص الخاص بك

الآن بعد أن قمت بتحسين ودمج نموذج Phi-3 المخصص مع Prompt flow، أنت جاهز لبدء التفاعل معه. سيرشدك هذا التمرين خلال عملية إعداد وبدء الدردشة مع نموذجك باستخدام Prompt flow. باتباع هذه الخطوات، ستتمكن من الاستفادة الكاملة من قدرات نموذج Phi-3 المحسّن لمهام ومحادثات متنوعة.

- دردش مع نموذج Phi-3 المخصص باستخدام Prompt flow.

#### بدء Prompt flow

1. اختر **بدء جلسات الحوسبة** لبدء Prompt flow.

    ![بدء جلسة الحوسبة.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.ar.png)

1. اختر **التحقق وتحليل المدخلات** لتحديث المعلمات.

    ![تحقق من المدخلات.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.ar.png)

1. اختر **قيمة** الـ **connection** للاتصال المخصص الذي أنشأته. على سبيل المثال، *connection*.

    ![الاتصال.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.ar.png)

#### الدردشة مع نموذجك المخصص

1. اختر **الدردشة**.

    ![اختر الدردشة.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.ar.png)

1. إليك مثال على النتائج: الآن يمكنك الدردشة مع نموذج Phi-3 المخصص الخاص بك. يُنصح بطرح الأسئلة بناءً على البيانات المستخدمة في تحسين النموذج.

    ![الدردشة مع prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.ar.png)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحساسة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.