<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:00:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ar"
}
-->
# ضبط وتحسين نماذج Phi-3 المخصصة ودمجها مع Prompt flow في Azure AI Foundry

يعتمد هذا المثال الشامل (E2E) على الدليل "[ضبط وتحسين نماذج Phi-3 المخصصة مع Prompt Flow في Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" من مجتمع Microsoft Tech. يشرح هذا الدليل عمليات ضبط النماذج، نشرها، ودمج نماذج Phi-3 المخصصة مع Prompt flow في Azure AI Foundry.  
على عكس المثال الشامل "[ضبط وتحسين ودمج نماذج Phi-3 المخصصة مع Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" الذي تضمن تشغيل الكود محليًا، يركز هذا الدليل بالكامل على ضبط ودمج النموذج داخل Azure AI / ML Studio.

## نظرة عامة

في هذا المثال الشامل، ستتعلم كيفية ضبط نموذج Phi-3 ودمجه مع Prompt flow في Azure AI Foundry. من خلال الاستفادة من Azure AI / ML Studio، ستنشئ سير عمل لنشر واستخدام نماذج الذكاء الاصطناعي المخصصة. ينقسم هذا المثال إلى ثلاث سيناريوهات:

**السيناريو 1: إعداد موارد Azure والتحضير لعملية الضبط**

**السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio**

**السيناريو 3: الدمج مع Prompt flow والدردشة مع نموذجك المخصص في Azure AI Foundry**

فيما يلي نظرة عامة على هذا المثال الشامل.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.ar.png)

### جدول المحتويات

1. **[السيناريو 1: إعداد موارد Azure والتحضير لعملية الضبط](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [إنشاء مساحة عمل Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [طلب حصص GPU في اشتراك Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [إضافة تعيين دور](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [إعداد المشروع](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [تحضير مجموعة البيانات للضبط](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ضبط نموذج Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [نشر نموذج Phi-3 بعد الضبط](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[السيناريو 3: الدمج مع Prompt flow والدردشة مع نموذجك المخصص في Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [دمج نموذج Phi-3 المخصص مع Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [الدردشة مع نموذج Phi-3 المخصص الخاص بك](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## السيناريو 1: إعداد موارد Azure والتحضير لعملية الضبط

### إنشاء مساحة عمل Azure Machine Learning

1. اكتب *azure machine learning* في **شريط البحث** أعلى صفحة البوابة واختر **Azure Machine Learning** من الخيارات التي تظهر.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.ar.png)

2. اختر **+ Create** من قائمة التنقل.

3. اختر **New workspace** من قائمة التنقل.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.ar.png)

4. قم بالمهام التالية:

    - اختر **Subscription** الخاص بك في Azure.
    - اختر **Resource group** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - أدخل **Workspace Name**. يجب أن يكون اسمًا فريدًا.
    - اختر **Region** التي ترغب في استخدامها.
    - اختر **Storage account** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Key vault** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Application insights** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Container registry** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.ar.png)

5. اختر **Review + Create**.

6. اختر **Create**.

### طلب حصص GPU في اشتراك Azure

في هذا الدليل، ستتعلم كيفية ضبط ونشر نموذج Phi-3 باستخدام وحدات معالجة الرسومات (GPUs). لضبط النموذج، ستستخدم GPU من نوع *Standard_NC24ads_A100_v4*، والذي يتطلب طلب حصة. للنشر، ستستخدم GPU من نوع *Standard_NC6s_v3*، والذي يتطلب أيضًا طلب حصة.

> [!NOTE]
>
> فقط اشتراكات Pay-As-You-Go (نوع الاشتراك القياسي) مؤهلة للحصول على تخصيص GPU؛ الاشتراكات ذات الامتيازات غير مدعومة حاليًا.
>

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. قم بالمهام التالية لطلب حصة *Standard NCADSA100v4 Family*:

    - اختر **Quota** من القائمة الجانبية.
    - اختر **Virtual machine family** التي تريد استخدامها. على سبيل المثال، اختر **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**، والتي تشمل GPU من نوع *Standard_NC24ads_A100_v4*.
    - اختر **Request quota** من قائمة التنقل.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.ar.png)

    - في صفحة طلب الحصة، أدخل **New cores limit** التي ترغب في استخدامها. على سبيل المثال، 24.
    - في صفحة طلب الحصة، اختر **Submit** لتقديم طلب حصة GPU.

1. قم بالمهام التالية لطلب حصة *Standard NCSv3 Family*:

    - اختر **Quota** من القائمة الجانبية.
    - اختر **Virtual machine family** التي تريد استخدامها. على سبيل المثال، اختر **Standard NCSv3 Family Cluster Dedicated vCPUs**، والتي تشمل GPU من نوع *Standard_NC6s_v3*.
    - اختر **Request quota** من قائمة التنقل.
    - في صفحة طلب الحصة، أدخل **New cores limit** التي ترغب في استخدامها. على سبيل المثال، 24.
    - في صفحة طلب الحصة، اختر **Submit** لتقديم طلب حصة GPU.

### إضافة تعيين دور

لضبط ونشر نماذجك، يجب أولاً إنشاء هوية مُدارة مخصصة للمستخدم (User Assigned Managed Identity - UAI) ومنحها الأذونات المناسبة. ستُستخدم هذه الهوية للمصادقة أثناء النشر.

#### إنشاء هوية مُدارة مخصصة للمستخدم (UAI)

1. اكتب *managed identities* في **شريط البحث** أعلى صفحة البوابة واختر **Managed Identities** من الخيارات التي تظهر.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.ar.png)

1. اختر **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.ar.png)

1. قم بالمهام التالية:

    - اختر **Subscription** الخاص بك في Azure.
    - اختر **Resource group** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Region** التي ترغب في استخدامها.
    - أدخل **Name**. يجب أن يكون اسمًا فريدًا.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.ar.png)

1. اختر **Review + create**.

1. اختر **+ Create**.

#### إضافة تعيين دور Contributor إلى الهوية المُدارة

1. انتقل إلى مورد الهوية المُدارة الذي أنشأته.

1. اختر **Azure role assignments** من القائمة الجانبية.

1. اختر **+Add role assignment** من قائمة التنقل.

1. في صفحة إضافة تعيين الدور، قم بالمهام التالية:
    - اختر **Scope** إلى **Resource group**.
    - اختر **Subscription** الخاص بك في Azure.
    - اختر **Resource group** التي تريد استخدامها.
    - اختر **Role** إلى **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.ar.png)

2. اختر **Save**.

#### إضافة تعيين دور Storage Blob Data Reader إلى الهوية المُدارة

1. اكتب *storage accounts* في **شريط البحث** أعلى صفحة البوابة واختر **Storage accounts** من الخيارات التي تظهر.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.ar.png)

1. اختر حساب التخزين المرتبط بمساحة عمل Azure Machine Learning التي أنشأتها. على سبيل المثال، *finetunephistorage*.

1. قم بالمهام التالية للانتقال إلى صفحة إضافة تعيين الدور:

    - انتقل إلى حساب التخزين الذي أنشأته في Azure.
    - اختر **Access Control (IAM)** من القائمة الجانبية.
    - اختر **+ Add** من قائمة التنقل.
    - اختر **Add role assignment** من قائمة التنقل.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.ar.png)

1. في صفحة إضافة تعيين الدور، قم بالمهام التالية:

    - في صفحة الدور، اكتب *Storage Blob Data Reader* في **شريط البحث** واختر **Storage Blob Data Reader** من الخيارات التي تظهر.
    - في صفحة الدور، اختر **Next**.
    - في صفحة الأعضاء، اختر **Assign access to** إلى **Managed identity**.
    - في صفحة الأعضاء، اختر **+ Select members**.
    - في صفحة اختيار الهويات المُدارة، اختر **Subscription** الخاص بك في Azure.
    - في صفحة اختيار الهويات المُدارة، اختر **Managed identity** إلى **Manage Identity**.
    - في صفحة اختيار الهويات المُدارة، اختر الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - في صفحة اختيار الهويات المُدارة، اختر **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.ar.png)

1. اختر **Review + assign**.

#### إضافة تعيين دور AcrPull إلى الهوية المُدارة

1. اكتب *container registries* في **شريط البحث** أعلى صفحة البوابة واختر **Container registries** من الخيارات التي تظهر.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.ar.png)

1. اختر سجل الحاويات المرتبط بمساحة عمل Azure Machine Learning. على سبيل المثال، *finetunephicontainerregistry*

1. قم بالمهام التالية للانتقال إلى صفحة إضافة تعيين الدور:

    - اختر **Access Control (IAM)** من القائمة الجانبية.
    - اختر **+ Add** من قائمة التنقل.
    - اختر **Add role assignment** من قائمة التنقل.

1. في صفحة إضافة تعيين الدور، قم بالمهام التالية:

    - في صفحة الدور، اكتب *AcrPull* في **شريط البحث** واختر **AcrPull** من الخيارات التي تظهر.
    - في صفحة الدور، اختر **Next**.
    - في صفحة الأعضاء، اختر **Assign access to** إلى **Managed identity**.
    - في صفحة الأعضاء، اختر **+ Select members**.
    - في صفحة اختيار الهويات المُدارة، اختر **Subscription** الخاص بك في Azure.
    - في صفحة اختيار الهويات المُدارة، اختر **Managed identity** إلى **Manage Identity**.
    - في صفحة اختيار الهويات المُدارة، اختر الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - في صفحة اختيار الهويات المُدارة، اختر **Select**.
    - اختر **Review + assign**.

### إعداد المشروع

لتنزيل مجموعات البيانات اللازمة للضبط، ستقوم بإعداد بيئة محلية.

في هذا التمرين، ستقوم بـ

- إنشاء مجلد للعمل بداخله.
- إنشاء بيئة افتراضية.
- تثبيت الحزم المطلوبة.
- إنشاء ملف *download_dataset.py* لتنزيل مجموعة البيانات.

#### إنشاء مجلد للعمل بداخله

1. افتح نافذة طرفية واكتب الأمر التالي لإنشاء مجلد باسم *finetune-phi* في المسار الافتراضي.

    ```console
    mkdir finetune-phi
    ```

2. اكتب الأمر التالي في الطرفية للانتقال إلى مجلد *finetune-phi* الذي أنشأته.
#### إنشاء بيئة افتراضية

1. اكتب الأمر التالي داخل الطرفية لإنشاء بيئة افتراضية باسم *.venv*.

    ```console
    python -m venv .venv
    ```

2. اكتب الأمر التالي داخل الطرفية لتفعيل البيئة الافتراضية.

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

#### إنشاء `donload_dataset.py`

> [!NOTE]
> الهيكل الكامل للمجلد:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. افتح **Visual Studio Code**.

1. اختر **File** من شريط القوائم.

1. اختر **Open Folder**.

1. اختر مجلد *finetune-phi* الذي أنشأته، والموجود في *C:\Users\yourUserName\finetune-phi*.

    ![اختر المجلد الذي أنشأته.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.ar.png)

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New File** لإنشاء ملف جديد باسم *download_dataset.py*.

    ![إنشاء ملف جديد.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.ar.png)

### تحضير مجموعة البيانات للتدريب الدقيق

في هذا التمرين، ستقوم بتشغيل ملف *download_dataset.py* لتحميل مجموعات بيانات *ultrachat_200k* إلى بيئتك المحلية. ثم ستستخدم هذه المجموعات لتدريب نموذج Phi-3 بدقة في Azure Machine Learning.

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

1. تحقق من أن مجموعات البيانات تم حفظها بنجاح في مجلد *finetune-phi/data* المحلي.

> [!NOTE]
>
> #### ملاحظة حول حجم مجموعة البيانات ووقت التدريب الدقيق
>
> في هذا الدرس، تستخدم فقط 1% من مجموعة البيانات (`split='train[:1%]'`). هذا يقلل بشكل كبير من حجم البيانات، مما يسرع من عمليات الرفع والتدريب الدقيق. يمكنك تعديل النسبة لإيجاد التوازن المناسب بين وقت التدريب وأداء النموذج. استخدام جزء أصغر من مجموعة البيانات يقلل من الوقت المطلوب للتدريب الدقيق، مما يجعل العملية أكثر سهولة في سياق الدروس.

## السيناريو 2: تدريب نموذج Phi-3 بدقة ونشره في Azure Machine Learning Studio

### تدريب نموذج Phi-3 بدقة

في هذا التمرين، ستقوم بتدريب نموذج Phi-3 بدقة في Azure Machine Learning Studio.

في هذا التمرين، ستقوم بـ:

- إنشاء مجموعة حوسبة للتدريب الدقيق.
- تدريب نموذج Phi-3 بدقة في Azure Machine Learning Studio.

#### إنشاء مجموعة حوسبة للتدريب الدقيق

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر **Compute** من القائمة الجانبية.

1. اختر **Compute clusters** من قائمة التنقل.

1. اختر **+ New**.

    ![اختر الحوسبة.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.ar.png)

1. قم بالمهام التالية:

    - اختر **Region** التي ترغب في استخدامها.
    - اختر **Virtual machine tier** إلى **Dedicated**.
    - اختر **Virtual machine type** إلى **GPU**.
    - اختر فلتر **Virtual machine size** إلى **Select from all options**.
    - اختر **Virtual machine size** إلى **Standard_NC24ads_A100_v4**.

    ![إنشاء المجموعة.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.ar.png)

1. اختر **Next**.

1. قم بالمهام التالية:

    - أدخل **Compute name**. يجب أن يكون قيمة فريدة.
    - اختر **Minimum number of nodes** إلى **0**.
    - اختر **Maximum number of nodes** إلى **1**.
    - اختر **Idle seconds before scale down** إلى **120**.

    ![إنشاء المجموعة.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.ar.png)

1. اختر **Create**.

#### تدريب نموذج Phi-3 بدقة

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة عمل Azure Machine Learning التي أنشأتها.

    ![اختر مساحة العمل التي أنشأتها.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.ar.png)

1. قم بالمهام التالية:

    - اختر **Model catalog** من القائمة الجانبية.
    - اكتب *phi-3-mini-4k* في **شريط البحث** واختر **Phi-3-mini-4k-instruct** من الخيارات التي تظهر.

    ![اكتب phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.ar.png)

1. اختر **Fine-tune** من قائمة التنقل.

    ![اختر التدريب الدقيق.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.ar.png)

1. قم بالمهام التالية:

    - اختر **Select task type** إلى **Chat completion**.
    - اختر **+ Select data** لرفع **بيانات التدريب**.
    - اختر نوع رفع بيانات التحقق إلى **Provide different validation data**.
    - اختر **+ Select data** لرفع **بيانات التحقق**.

    ![املأ صفحة التدريب الدقيق.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.ar.png)

    > [!TIP]
    >
    > يمكنك اختيار **Advanced settings** لتخصيص الإعدادات مثل **learning_rate** و **lr_scheduler_type** لتحسين عملية التدريب الدقيق حسب احتياجاتك الخاصة.

1. اختر **Finish**.

1. في هذا التمرين، نجحت في تدريب نموذج Phi-3 بدقة باستخدام Azure Machine Learning. يرجى ملاحظة أن عملية التدريب الدقيق قد تستغرق وقتًا طويلاً. بعد تشغيل مهمة التدريب الدقيق، عليك الانتظار حتى تكتمل. يمكنك متابعة حالة المهمة من خلال التوجه إلى تبويب Jobs في الجانب الأيسر من مساحة عمل Azure Machine Learning الخاصة بك. في السلسلة التالية، ستقوم بنشر النموذج المدرب ودمجه مع Prompt flow.

    ![عرض مهمة التدريب الدقيق.](../../../../../../translated_images/06-08-output.2bd32e59930672b1.ar.png)

### نشر نموذج Phi-3 المدرب بدقة

لدمج نموذج Phi-3 المدرب بدقة مع Prompt flow، تحتاج إلى نشر النموذج ليكون متاحًا للاستدلال في الوقت الحقيقي. تتضمن هذه العملية تسجيل النموذج، إنشاء نقطة نهاية عبر الإنترنت، ونشر النموذج.

في هذا التمرين، ستقوم بـ:

- تسجيل النموذج المدرب في مساحة عمل Azure Machine Learning.
- إنشاء نقطة نهاية عبر الإنترنت.
- نشر نموذج Phi-3 المدرب المسجل.

#### تسجيل النموذج المدرب

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. اختر مساحة عمل Azure Machine Learning التي أنشأتها.

    ![اختر مساحة العمل التي أنشأتها.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.ar.png)

1. اختر **Models** من القائمة الجانبية.
1. اختر **+ Register**.
1. اختر **From a job output**.

    ![تسجيل النموذج.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.ar.png)

1. اختر المهمة التي أنشأتها.

    ![اختر المهمة.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.ar.png)

1. اختر **Next**.

1. اختر **Model type** إلى **MLflow**.

1. تأكد من اختيار **Job output**؛ يجب أن يكون محددًا تلقائيًا.

    ![اختر المخرجات.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.ar.png)

2. اختر **Next**.

3. اختر **Register**.

    ![اختر التسجيل.](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.ar.png)

4. يمكنك عرض النموذج المسجل من خلال الانتقال إلى قائمة **Models** من القائمة الجانبية.

    ![النموذج المسجل.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.ar.png)

#### نشر النموذج المدرب

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **Endpoints** من القائمة الجانبية.

1. اختر **Real-time endpoints** من قائمة التنقل.

    ![إنشاء نقطة نهاية.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.ar.png)

1. اختر **Create**.

1. اختر النموذج المسجل الذي أنشأته.

    ![اختر النموذج المسجل.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.ar.png)

1. اختر **Select**.

1. قم بالمهام التالية:

    - اختر **Virtual machine** إلى *Standard_NC6s_v3*.
    - اختر عدد النسخ التي ترغب في استخدامها، مثلاً *1*.
    - اختر **Endpoint** إلى **New** لإنشاء نقطة نهاية جديدة.
    - أدخل **Endpoint name**. يجب أن يكون قيمة فريدة.
    - أدخل **Deployment name**. يجب أن يكون قيمة فريدة.

    ![املأ إعدادات النشر.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.ar.png)

1. اختر **Deploy**.

> [!WARNING]
> لتجنب رسوم إضافية على حسابك، تأكد من حذف نقطة النهاية التي أنشأتها في مساحة عمل Azure Machine Learning.
>

#### التحقق من حالة النشر في مساحة عمل Azure Machine Learning

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **Endpoints** من القائمة الجانبية.

1. اختر نقطة النهاية التي أنشأتها.

    ![اختر نقاط النهاية](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.ar.png)

1. في هذه الصفحة، يمكنك إدارة نقاط النهاية أثناء عملية النشر.

> [!NOTE]
> بمجرد اكتمال النشر، تأكد من أن **Live traffic** مضبوط على **100%**. إذا لم يكن كذلك، اختر **Update traffic** لتعديل إعدادات المرور. لاحظ أنه لا يمكنك اختبار النموذج إذا كان المرور مضبوطًا على 0%.
>
> ![ضبط المرور.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.ar.png)
>

## السيناريو 3: الدمج مع Prompt flow والدردشة مع نموذجك المخصص في Azure AI Foundry

### دمج نموذج Phi-3 المخصص مع Prompt flow

بعد نشر نموذجك المدرب بنجاح، يمكنك الآن دمجه مع Prompt Flow لاستخدامه في التطبيقات الحية، مما يتيح مجموعة متنوعة من المهام التفاعلية مع نموذج Phi-3 المخصص الخاص بك.

في هذا التمرين، ستقوم بـ:

- إنشاء Azure AI Foundry Hub.
- إنشاء مشروع Azure AI Foundry.
- إنشاء Prompt flow.
- إضافة اتصال مخصص لنموذج Phi-3 المدرب.
- إعداد Prompt flow للدردشة مع نموذج Phi-3 المخصص الخاص بك.
> [!NOTE]
> يمكنك أيضًا الدمج مع Promptflow باستخدام Azure ML Studio. يمكن تطبيق نفس عملية الدمج على Azure ML Studio.
#### إنشاء مركز Azure AI Foundry

يجب عليك إنشاء مركز قبل إنشاء المشروع. يعمل المركز مثل مجموعة موارد، مما يتيح لك تنظيم وإدارة عدة مشاريع داخل Azure AI Foundry.

1. قم بزيارة [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. اختر **All hubs** من القائمة الجانبية.

1. اختر **+ New hub** من قائمة التنقل.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.ar.png)

1. قم بالمهام التالية:

    - أدخل **Hub name**. يجب أن يكون قيمة فريدة.
    - اختر اشتراك Azure الخاص بك **Subscription**.
    - اختر **Resource group** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Location** التي تود استخدامها.
    - اختر **Connect Azure AI Services** التي تريد استخدامها (يمكنك إنشاء واحدة جديدة إذا لزم الأمر).
    - اختر **Connect Azure AI Search** ثم **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.ar.png)

1. اختر **Next**.

#### إنشاء مشروع Azure AI Foundry

1. في المركز الذي أنشأته، اختر **All projects** من القائمة الجانبية.

1. اختر **+ New project** من قائمة التنقل.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.ar.png)

1. أدخل **Project name**. يجب أن يكون قيمة فريدة.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.ar.png)

1. اختر **Create a project**.

#### إضافة اتصال مخصص لنموذج Phi-3 المحسن

لدمج نموذج Phi-3 المخصص مع Prompt flow، تحتاج إلى حفظ نقطة النهاية والمفتاح الخاص بالنموذج في اتصال مخصص. هذا الإعداد يضمن الوصول إلى نموذج Phi-3 المخصص داخل Prompt flow.

#### تعيين مفتاح API وعنوان نقطة النهاية لنموذج Phi-3 المحسن

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مساحة عمل Azure Machine learning التي أنشأتها.

1. اختر **Endpoints** من القائمة الجانبية.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.ar.png)

1. اختر نقطة النهاية التي أنشأتها.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.ar.png)

1. اختر **Consume** من قائمة التنقل.

1. انسخ **REST endpoint** و **Primary key** الخاصين بك.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.ar.png)

#### إضافة الاتصال المخصص

1. قم بزيارة [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. انتقل إلى مشروع Azure AI Foundry الذي أنشأته.

1. في المشروع الذي أنشأته، اختر **Settings** من القائمة الجانبية.

1. اختر **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.ar.png)

1. اختر **Custom keys** من قائمة التنقل.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.ar.png)

1. قم بالمهام التالية:

    - اختر **+ Add key value pairs**.
    - في خانة اسم المفتاح، أدخل **endpoint** والصق نقطة النهاية التي نسختها من Azure ML Studio في خانة القيمة.
    - اختر **+ Add key value pairs** مرة أخرى.
    - في خانة اسم المفتاح، أدخل **key** والصق المفتاح الذي نسخته من Azure ML Studio في خانة القيمة.
    - بعد إضافة المفاتيح، اختر **is secret** لمنع كشف المفتاح.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.ar.png)

1. اختر **Add connection**.

#### إنشاء Prompt flow

لقد أضفت اتصالًا مخصصًا في Azure AI Foundry. الآن، دعنا ننشئ Prompt flow باستخدام الخطوات التالية. بعد ذلك، ستربط هذا الـ Prompt flow بالاتصال المخصص حتى تتمكن من استخدام النموذج المحسن داخل Prompt flow.

1. انتقل إلى مشروع Azure AI Foundry الذي أنشأته.

1. اختر **Prompt flow** من القائمة الجانبية.

1. اختر **+ Create** من قائمة التنقل.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.ar.png)

1. اختر **Chat flow** من قائمة التنقل.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.ar.png)

1. أدخل **Folder name** التي تريد استخدامها.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.ar.png)

2. اختر **Create**.

#### إعداد Prompt flow للدردشة مع نموذج Phi-3 المخصص

تحتاج إلى دمج نموذج Phi-3 المحسن في Prompt flow. ومع ذلك، فإن Prompt flow الحالي غير مصمم لهذا الغرض. لذلك، يجب إعادة تصميم Prompt flow لتمكين دمج النموذج المخصص.

1. في Prompt flow، قم بالمهام التالية لإعادة بناء التدفق الحالي:

    - اختر **Raw file mode**.
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

    - اختر **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.ar.png)

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.ar.png)

> [!NOTE]
> لمزيد من المعلومات التفصيلية حول استخدام Prompt flow في Azure AI Foundry، يمكنك الرجوع إلى [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. اختر **Chat input** و **Chat output** لتمكين الدردشة مع نموذجك.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.ar.png)

1. الآن أنت جاهز للدردشة مع نموذج Phi-3 المخصص. في التمرين التالي، ستتعلم كيفية بدء Prompt flow واستخدامه للدردشة مع نموذج Phi-3 المحسن.

> [!NOTE]
>
> يجب أن يبدو التدفق المعاد بناؤه كما في الصورة أدناه:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.ar.png)
>

### الدردشة مع نموذج Phi-3 المخصص

الآن بعد أن قمت بتحسين ودمج نموذج Phi-3 المخصص مع Prompt flow، أنت جاهز لبدء التفاعل معه. سيرشدك هذا التمرين خلال عملية إعداد وبدء الدردشة مع نموذجك باستخدام Prompt flow. باتباع هذه الخطوات، ستتمكن من الاستفادة الكاملة من قدرات نموذج Phi-3 المحسن لمهام ومحادثات متنوعة.

- دردش مع نموذج Phi-3 المخصص باستخدام Prompt flow.

#### بدء Prompt flow

1. اختر **Start compute sessions** لبدء Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.ar.png)

1. اختر **Validate and parse input** لتحديث المعلمات.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.ar.png)

1. اختر **Value** الخاص بـ **connection** للاتصال المخصص الذي أنشأته. على سبيل المثال، *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.ar.png)

#### الدردشة مع النموذج المخصص

1. اختر **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.ar.png)

1. إليك مثال على النتائج: الآن يمكنك الدردشة مع نموذج Phi-3 المخصص. يُنصح بطرح أسئلة بناءً على البيانات المستخدمة في تحسين النموذج.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.ar.png)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.