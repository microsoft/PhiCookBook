<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-04T07:12:09+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "ar"
}
-->
# ضبط دقيق ودمج نماذج Phi-3 المخصصة مع Prompt flow

هذا المثال الشامل (E2E) مبني على الدليل "[دليل خطوة بخطوة لضبط دقيق ودمج نماذج Phi-3 المخصصة مع Prompt Flow](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" من Microsoft Tech Community. يقدّم العمليات الخاصة بالضبط الدقيق والنشر ودمج نماذج Phi-3 المخصصة مع Prompt flow.

## نظرة عامة

في هذا المثال الشامل (E2E)، ستتعلم كيفية ضبط نموذج Phi-3 بدقة ودمجه مع Prompt flow. من خلال الاستفادة من Azure Machine Learning وPrompt flow ستنشئ سير عمل لنشر واستخدام نماذج الذكاء الاصطناعي المخصصة. ينقسم هذا المثال إلى ثلاث سيناريوهات:

**السيناريو 1: إعداد موارد Azure والاستعداد للضبط الدقيق**

**السيناريو 2: ضبط نموذج Phi-3 بدقة ونشره في Azure Machine Learning Studio**

**السيناريو 3: الدمج مع Prompt flow والدردشة مع نموذجك المخصص**

إليك نظرة عامة على هذا المثال الشامل.

![نظرة عامة على دمج وضبط Phi-3 مع Prompt Flow](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.ar.png)

### جدول المحتويات

1. **[السيناريو 1: إعداد موارد Azure والاستعداد للضبط الدقيق](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [إنشاء مساحة عمل Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [طلب حصص GPU في اشتراك Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [إضافة تعيين دور](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [إعداد المشروع](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [تحضير مجموعة البيانات للضبط الدقيق](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[السيناريو 2: ضبط نموذج Phi-3 بدقة ونشره في Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [إعداد Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ضبط نموذج Phi-3 بدقة](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [نشر النموذج المضبوط بدقة](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[السيناريو 3: الدمج مع Prompt flow والدردشة مع نموذجك المخصص](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [دمج نموذج Phi-3 المخصص مع Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [الدردشة مع نموذجك المخصص](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## السيناريو 1: إعداد موارد Azure والاستعداد للضبط الدقيق

### إنشاء مساحة عمل Azure Machine Learning

1. اكتب *azure machine learning* في **شريط البحث** في أعلى صفحة البوابة وحدد **Azure Machine Learning** من الخيارات التي تظهر.

    ![اكتب azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.ar.png)

1. حدد **+ إنشاء** من قائمة التنقل.

1. حدد **مساحة عمل جديدة** من قائمة التنقل.

    ![حدد مساحة عمل جديدة](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.ar.png)

1. قم بالمهام التالية:

    - حدد **الاشتراك** الخاص بك في Azure.
    - حدد **مجموعة الموارد** التي ستستخدمها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - أدخل **اسم مساحة العمل**. يجب أن يكون قيمة فريدة.
    - حدد **المنطقة** التي ترغب باستخدامها.
    - حدد **حساب التخزين** للاستخدام (قم بإنشاء واحد جديد إذا لزم الأمر).
    - حدد **المخزن الرئيسي (Key vault)** للاستخدام (قم بإنشاء واحد جديد إذا لزم الأمر).
    - حدد **Application insights** للاستخدام (قم بإنشاء واحد جديد إذا لزم الأمر).
    - حدد **سجل الحاويات (Container registry)** للاستخدام (قم بإنشاء واحد جديد إذا لزم الأمر).

    ![املأ إعدادات Azure ML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.ar.png)

1. حدد **مراجعة + إنشاء**.

1. حدد **إنشاء**.

### طلب حصص GPU في اشتراك Azure

في هذا المثال الشامل، ستستخدم *Standard_NC24ads_A100_v4 GPU* للضبط الدقيق، والذي يتطلب طلب حصة، و*Standard_E4s_v3* CPU للنشر، والذي لا يتطلب طلب حصة.

> [!NOTE]
>
> Only Pay-As-You-Go subscriptions (the standard subscription type) are eligible for GPU allocation; benefit subscriptions are not currently supported.
>
> For those using benefit subscriptions (such as Visual Studio Enterprise Subscription) or those looking to quickly test the fine-tuning and deployment process, this tutorial also provides guidance for fine-tuning with a minimal dataset using a CPU. However, it is important to note that fine-tuning results are significantly better when using a GPU with larger datasets.

1. زر [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. قم بالمهام التالية لطلب حصة *Standard NCADSA100v4 Family*:

    - حدد **الحصة (Quota)** من علامة التبويب الجانبية.
    - حدد **عائلة الآلات الافتراضية (Virtual machine family)** التي تريد استخدامها. على سبيل المثال، حدد **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**، والتي تتضمن *Standard_NC24ads_A100_v4* GPU.
    - حدد **طلب حصة (Request quota)** من قائمة التنقل.

        ![طلب الحصة.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.ar.png)

    - داخل صفحة طلب الحصة، أدخل **الحد الجديد للنوى (New cores limit)** الذي ترغب استخدامه. على سبيل المثال، 24.
    - داخل صفحة طلب الحصة، حدد **إرسال** لطلب حصة GPU.

> [!NOTE]
> يمكنك تحديد GPU أو CPU المناسب لاحتياجاتك بالرجوع إلى وثيقة [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### إضافة تعيين دور

لضبط ونشر نماذجك، يجب أولاً إنشاء هوية مُدارة مخصصة للمستخدم (User Assigned Managed Identity - UAI) ومنحها الأذونات المناسبة. ستُستخدم هذه الهوية المُدارة للمصادقة أثناء النشر.

#### إنشاء User Assigned Managed Identity (UAI)

1. اكتب *managed identities* في **شريط البحث** في أعلى صفحة البوابة وحدد **Managed Identities** من الخيارات التي تظهر.

    ![اكتب managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.ar.png)

1. حدد **+ إنشاء**.

    ![حدد إنشاء.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.ar.png)

1. قم بالمهام التالية:

    - حدد **الاشتراك** الخاص بك في Azure.
    - حدد **مجموعة الموارد** التي ستستخدمها (قم بإنشاء واحدة جديدة إذا لزم الأمر).
    - حدد **المنطقة** التي ترغب استخدامها.
    - أدخل **الاسم**. يجب أن يكون قيمة فريدة.

1. حدد **مراجعة + إنشاء**.

1. حدد **+ إنشاء**.

#### إضافة تعيين دور Contributor إلى الهوية المُدارة

1. انتقل إلى مورد الهوية المُدارة الذي قمت بإنشائه.

1. حدد **تعيينات أدوار Azure (Azure role assignments)** من علامة التبويب الجانبية.

1. حدد **+إضافة تعيين دور** من قائمة التنقل.

1. داخل صفحة إضافة تعيين الدور، قم بالمهام التالية:
    - حدد **نطاق (Scope)** إلى **مجموعة الموارد (Resource group)**.
    - حدد **الاشتراك** الخاص بك في Azure.
    - حدد **مجموعة الموارد** التي ستستخدمها.
    - حدد **الدور (Role)** إلى **Contributor**.

    ![املأ دور المساهم.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.ar.png)

1. حدد **حفظ**.

#### إضافة تعيين دور Storage Blob Data Reader إلى الهوية المُدارة

1. اكتب *storage accounts* في **شريط البحث** في أعلى صفحة البوابة وحدد **Storage accounts** من الخيارات التي تظهر.

    ![اكتب storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.ar.png)

1. حدد حساب التخزين المرتبط بمساحة عمل Azure Machine Learning التي أنشأتها. على سبيل المثال، *finetunephistorage*.

1. قم بالمهام التالية للتنقل إلى صفحة إضافة تعيين دور:

    - انتقل إلى حساب التخزين في Azure الذي أنشأته.
    - حدد **Access Control (IAM)** من علامة التبويب الجانبية.
    - حدد **+ إضافة** من قائمة التنقل.
    - حدد **إضافة تعيين دور** من قائمة التنقل.

    ![أضف دور.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.ar.png)

1. داخل صفحة إضافة تعيين دور، قم بالمهام التالية:

    - داخل صفحة الدور، اكتب *Storage Blob Data Reader* في **شريط البحث** واختر **Storage Blob Data Reader** من الخيارات التي تظهر.
    - داخل صفحة الدور، حدد **التالي**.
    - داخل صفحة الأعضاء، حدد **تعيين الوصول إلى** **Managed identity**.
    - داخل صفحة الأعضاء، حدد **+ تحديد أعضاء**.
    - داخل صفحة تحديد الهويات المُدارة، حدد **الاشتراك** الخاص بك في Azure.
    - داخل صفحة تحديد الهويات المُدارة، حدد **الهوية المُدارة** إلى **Manage Identity**.
    - داخل صفحة تحديد الهويات المُدارة، حدد الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - داخل صفحة تحديد الهويات المُدارة، حدد **تحديد**.

    ![حدد الهوية المُدارة.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.ar.png)

1. حدد **مراجعة + تعيين**.

#### إضافة تعيين دور AcrPull إلى الهوية المُدارة

1. اكتب *container registries* في **شريط البحث** في أعلى صفحة البوابة وحدد **Container registries** من الخيارات التي تظهر.

    ![اكتب container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.ar.png)

1. حدد سجل الحاويات المرتبط بمساحة عمل Azure Machine Learning. على سبيل المثال، *finetunephicontainerregistries*

1. قم بالمهام التالية للتنقل إلى صفحة إضافة تعيين دور:

    - حدد **Access Control (IAM)** من علامة التبويب الجانبية.
    - حدد **+ إضافة** من قائمة التنقل.
    - حدد **إضافة تعيين دور** من قائمة التنقل.

1. داخل صفحة إضافة تعيين دور، قم بالمهام التالية:

    - داخل صفحة الدور، اكتب *AcrPull* في **شريط البحث** واختر **AcrPull** من الخيارات التي تظهر.
    - داخل صفحة الدور، حدد **التالي**.
    - داخل صفحة الأعضاء، حدد **تعيين الوصول إلى** **Managed identity**.
    - داخل صفحة الأعضاء، حدد **+ تحديد أعضاء**.
    - داخل صفحة تحديد الهويات المُدارة، حدد **الاشتراك** الخاص بك في Azure.
    - داخل صفحة تحديد الهويات المُدارة، حدد **الهوية المُدارة** إلى **Manage Identity**.
    - داخل صفحة تحديد الهويات المُدارة، حدد الهوية المُدارة التي أنشأتها. على سبيل المثال، *finetunephi-managedidentity*.
    - داخل صفحة تحديد الهويات المُدارة، حدد **تحديد**.
    - حدد **مراجعة + تعيين**.

### إعداد المشروع

الآن، ستنشئ مجلداً للعمل فيه وتعد بيئة افتراضية لتطوير برنامج يتفاعل مع المستخدمين ويستخدم محفوظات الدردشة المخزنة في Azure Cosmos DB لإثراء استجاباته.

#### إنشاء مجلد للعمل بداخله

1. افتح نافذة طرفية واكتب الأمر التالي لإنشاء مجلد باسم *finetune-phi* في المسار الافتراضي.

    ```console
    mkdir finetune-phi
    ```

1. اكتب الأمر التالي داخل الطرفية للتنقل إلى مجلد *finetune-phi* الذي أنشأته.

    ```console
    cd finetune-phi
    ```

#### إنشاء بيئة افتراضية

1. اكتب الأمر التالي داخل الطرفية لإنشاء بيئة افتراضية باسم *.venv*.

    ```console
    python -m venv .venv
    ```

1. اكتب الأمر التالي داخل الطرفية لتفعيل البيئة الافتراضية.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> If it worked, you should see *(.venv)* before the command prompt.

#### تثبيت الحزم المطلوبة

1. اكتب الأوامر التالية داخل الطرفية لتثبيت الحزم المطلوبة.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### إنشاء ملفات المشروع
في هذا التمرين، ستقوم بإنشاء الملفات الأساسية لمشروعنا. تتضمن هذه الملفات سكربتات لتنزيل مجموعة البيانات، وإعداد بيئة Azure Machine Learning، وضبط نموذج Phi-3 (fine-tuning)، ونشر النموذج المضبوط. ستقوم أيضًا بإنشاء ملف *conda.yml* لإعداد بيئة الضبط الدقيقة.

في هذا التمرين، سوف:

- إنشاء ملف *download_dataset.py* لتنزيل مجموعة البيانات.
- إنشاء ملف *setup_ml.py* لإعداد بيئة Azure Machine Learning.
- إنشاء ملف *fine_tune.py* داخل مجلد *finetuning_dir* لضبط نموذج Phi-3 باستخدام مجموعة البيانات.
- إنشاء ملف *conda.yml* لإعداد بيئة الضبط الدقيقة.
- إنشاء ملف *deploy_model.py* لنشر النموذج المضبوط.
- إنشاء ملف *integrate_with_promptflow.py*، لدمج النموذج المُحسّن وتشغيله باستخدام Prompt flow.
- إنشاء ملف flow.dag.yml، لإعداد بنية سير العمل لـ Prompt flow.
- إنشاء ملف *config.py* لإدخال معلومات Azure الخاصة بك.

> [!NOTE]
>
> بنية المجلد المكتملة:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. افتح **Visual Studio Code**.

1. اختر **File** من شريط القوائم.

1. اختر **Open Folder**.

1. اختر المجلد *finetune-phi* الذي قمت بإنشائه، الموجود في *C:\Users\yourUserName\finetune-phi*.

    ![فتح مجلد المشروع.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.ar.png)

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New File** لإنشاء ملف جديد باسم *download_dataset.py*.

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New File** لإنشاء ملف جديد باسم *setup_ml.py*.

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New File** لإنشاء ملف جديد باسم *deploy_model.py*.

    ![إنشاء ملف جديد.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.ar.png)

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New Folder** لإنشاء مجلد جديد باسم *finetuning_dir*.

1. في مجلد *finetuning_dir*، قم بإنشاء ملف جديد باسم *fine_tune.py*.

#### إنشاء وتكوين ملف *conda.yml*

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New File** لإنشاء ملف جديد باسم *conda.yml*.

1. أضف الكود التالي إلى ملف *conda.yml* لإعداد بيئة الضبط الدقيقة لنموذج Phi-3.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### إنشاء وتكوين ملف *config.py*

1. في الجزء الأيسر من Visual Studio Code، انقر بزر الماوس الأيمن واختر **New File** لإنشاء ملف جديد باسم *config.py*.

1. أضف الكود التالي إلى ملف *config.py* لإدراج معلومات Azure الخاصة بك.

    ```python
    # إعدادات Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "مجموعة الاختبار"

    # إعدادات Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-مساحة العمل"

    # إعدادات الهوية المُدارة في Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-الهوية المُدارة"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # مسارات ملفات مجموعة البيانات
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # إعدادات النموذج المُحسّن
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-النموذج"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-نقطة النهاية"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-النشر"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### إضافة متغيرات بيئة Azure

1. قم بالمهام التالية لإضافة معرف اشتراك Azure (Subscription ID):

    - اكتب *subscriptions* في **search bar** أعلى صفحة البوابة وحدد **Subscriptions** من الخيارات الظاهرة.
    - حدد اشتراك Azure الذي تستخدمه حاليًا.
    - انسخ والصق Subscription ID الخاص بك في ملف *config.py*.

    ![العثور على معرف الاشتراك.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.ar.png)

1. قم بالمهام التالية لإضافة اسم Workspace الخاص بـ Azure:

    - انتقل إلى مورد Azure Machine Learning الذي قمت بإنشائه.
    - انسخ والصق اسم حسابك في ملف *config.py*.

    ![العثور على اسم Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.ar.png)

1. قم بالمهام التالية لإضافة اسم مجموعة موارد Azure (Resource Group Name):

    - انتقل إلى مورد Azure Machine Learning الذي قمت بإنشائه.
    - انسخ والصق اسم مجموعة موارد Azure في ملف *config.py*.

    ![العثور على اسم مجموعة الموارد.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.ar.png)

2. قم بالمهام التالية لإضافة اسم Managed Identity الخاص بـ Azure

    - انتقل إلى مورد Managed Identities الذي قمت بإنشائه.
    - انسخ والصق اسم Managed Identity الخاص بك في ملف *config.py*.

    ![العثور على UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.ar.png)

### إعداد مجموعة البيانات للضبط الدقيق

في هذا التمرين، ستشغّل ملف *download_dataset.py* لتنزيل مجموعات البيانات *ULTRACHAT_200k* إلى بيئتك المحلية. ثم ستستخدم هذه المجموعات لضبط نموذج Phi-3 في Azure Machine Learning.

#### تنزيل مجموعة البيانات باستخدام *download_dataset.py*

1. افتح ملف *download_dataset.py* في Visual Studio Code.

1. أضف الكود التالي داخل *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

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
        # تحميل وتقسيم مجموعة بيانات ULTRACHAT_200k بتكوين ونسبة تقسيم محددة
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # استخراج مجموعات التدريب والاختبار من التقسيم
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # حفظ مجموعة بيانات التدريب في ملف JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # حفظ مجموعة بيانات الاختبار في ملف JSONL منفصل
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **إرشادات للضبط الدقيق باستخدام مجموعة بيانات صغيرة على وحدة CPU**
>
> إذا أردت استخدام وحدة CPU للضبط الدقيق، فهذه الطريقة مناسبة لمن لديهم اشتراكات مزايا (مثل Visual Studio Enterprise Subscription) أو لاختبار عملية الضبط والنشر سريعًا.
>
> استبدل `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` بـ `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. اكتب الأمر التالي داخل جهاز الطرفية (terminal) لتشغيل السكربت وتنزيل مجموعة البيانات إلى بيئتك المحلية.

    ```console
    python download_data.py
    ```

1. تحقق من أنه تم حفظ مجموعات البيانات بنجاح في الدليل المحلي *finetune-phi/data*.

> [!NOTE]
>
> **حجم مجموعة البيانات ووقت الضبط الدقيق**
>
> في هذا المثال الشامل (E2E)، تستخدم فقط 1% من مجموعة البيانات (`train_sft[:1%]`). هذا يقلل بشكل كبير من كمية البيانات، مما يسرع كلًّا من عملية التحميل وعملية الضبط الدقيق. يمكنك ضبط النسبة لإيجاد التوازن المناسب بين وقت التدريب وأداء النموذج. استخدام جزء أصغر من مجموعة البيانات يقلل من الوقت المطلوب للضبط الدقيق، مما يجعل العملية أكثر قابلية للإدارة في مثال E2E.

## السيناريو 2: ضبط نموذج Phi-3 ونشره في Azure Machine Learning Studio

### إعداد Azure CLI

تحتاج إلى إعداد Azure CLI للمصادقة على بيئتك. يتيح لك Azure CLI إدارة موارد Azure مباشرة من سطر الأوامر ويوفر الاعتمادات اللازمة لـ Azure Machine Learning للوصول إلى هذه الموارد. للبدء، قم بتثبيت [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. افتح نافذة طرفية واكتب الأمر التالي لتسجيل الدخول إلى حساب Azure الخاص بك.

    ```console
    az login
    ```

1. حدد حساب Azure الذي تريد استخدامه.

1. حدد اشتراك Azure الذي تريد استخدامه.

    ![العثور على اسم مجموعة الموارد.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.ar.png)

> [!TIP]
>
> إذا واجهت صعوبة في تسجيل الدخول إلى Azure، جرّب استخدام رمز الجهاز (device code). افتح نافذة طرفية واكتب الأمر التالي لتسجيل الدخول إلى حساب Azure الخاص بك:
>
> ```console
> az login --use-device-code
> ```
>

### ضبط نموذج Phi-3

في هذا التمرين، ستقوم بضبط نموذج Phi-3 باستخدام مجموعة البيانات المقدمة. أولًا، ستقوم بتعريف عملية الضبط الدقيق في ملف *fine_tune.py*. ثم، ستقوم بتكوين بيئة Azure Machine Learning وبدء عملية الضبط عن طريق تشغيل ملف *setup_ml.py*. يضمن هذا السكربت أن يتم تنفيذ الضبط الدقيق داخل بيئة Azure Machine Learning.

بتشغيل *setup_ml.py*، ستشغّل عملية الضبط الدقيق في بيئة Azure Machine Learning.

#### إضافة الكود إلى ملف *fine_tune.py*

1. انتقل إلى مجلد *finetuning_dir* وافتح ملف *fine_tune.py* في Visual Studio Code.

1. أضف الكود التالي داخل *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # لتجنب حدوث خطأ INVALID_PARAMETER_VALUE في MLflow، قم بتعطيل تكامل MLflow
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # إعداد التسجيل
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # اسم_النموذج_المدرَّب_مسبقًا = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. احفظ وأغلق ملف *fine_tune.py*.

> [!TIP]
> **يمكنك ضبط نموذج Phi-3.5**
>
> في ملف *fine_tune.py*، يمكنك تغيير قيمة `pretrained_model_name` من `"microsoft/Phi-3-mini-4k-instruct"` إلى أي نموذج ترغب في ضبطه. على سبيل المثال، إذا قمت بتغييره إلى `"microsoft/Phi-3.5-mini-instruct"`، فستستخدم نموذج Phi-3.5-mini-instruct للضبط الدقيق. للعثور على اسم النموذج الذي تفضله واستخدامه، زر موقع [Hugging Face](https://huggingface.co/)، وابحث عن النموذج الذي تهتم به، ثم انسخ وألصق اسمه في حقل `pretrained_model_name` في السكربت الخاص بك.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="تخصيص التدريب لـ Phi-3.5.">
>

#### إضافة الكود إلى ملف *setup_ml.py*

1. افتح ملف *setup_ml.py* في Visual Studio Code.

1. أضف الكود التالي داخل *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # ثوابت

    # قم بإلغاء تعليق الأسطر التالية لاستخدام مثيل وحدة المعالجة المركزية (CPU) للتدريب
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # وحدة المعالجة المركزية (CPU)
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # قم بإلغاء تعليق الأسطر التالية لاستخدام مثيل وحدة معالجة الرسومات (GPU) للتدريب
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # استبدل بموقع عنقود الحوسبة الخاص بك
    FINETUNING_DIR = "./finetuning_dir" # مسار سكربت الضبط الدقيق
    TRAINING_ENV_NAME = "phi-3-training-environment" # اسم بيئة التدريب
    MODEL_OUTPUT_DIR = "./model_output" # مسار مجلد إخراج النموذج في Azure ML

    # إعداد السجلات لتتبع العملية
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # صورة Docker للبيئة
            conda_file=CONDA_FILE,  # ملف بيئة Conda
            name=TRAINING_ENV_NAME,  # اسم البيئة
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # فئة عنقود الحوسبة
                min_instances=0,  # الحد الأدنى لعدد المثيلات
                max_instances=1  # الحد الأقصى لعدد المثيلات
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # انتظر حتى يتم إنشاء العنقود
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # مسار ملف fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # بيئة التدريب
            compute=compute_name,  # عنقود الحوسبة المستخدم
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # مسار ملف بيانات التدريب
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # مسار ملف بيانات التقييم
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # تهيئة عميل ML
        ml_client = get_ml_client()

        # إنشاء بيئة
        env = create_or_get_environment(ml_client)
        
        # إنشاء عنقود حوسبة أو الحصول على الموجود بالفعل
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # إنشاء وإرسال مهمة الضبط الدقيق
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # إرسال المهمة
        ml_client.jobs.stream(returned_job.name)  # بث سجلات المهمة
        
        # التقاط اسم المهمة
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. استبدل `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, و `LOCATION` بتفاصيلك الخاصة.

    ```python
   # أزل التعليقات عن الأسطر التالية لاستخدام مثيل GPU أثناء التدريب
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # استبدل بموقع مجموعة الحوسبة الخاصة بك
    ```

> [!TIP]
>
> **إرشادات للضبط الدقيق باستخدام مجموعة بيانات صغيرة على وحدة CPU**
>
> إذا أردت استخدام وحدة CPU للضبط الدقيق، فهذه الطريقة مناسبة لمن لديهم اشتراكات مزايا (مثل Visual Studio Enterprise Subscription) أو لاختبار عملية الضبط والنشر سريعًا.
>
> 1. افتح ملف *setup_ml*.
> 1. استبدل `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, و `DOCKER_IMAGE_NAME` بما يلي. إذا لم يكن لديك وصول إلى *Standard_E16s_v3*، يمكنك استخدام مثيل CPU مكافئ أو طلب حصة جديدة.
> 1. استبدل `LOCATION` بتفاصيلك الخاصة.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. اكتب الأمر التالي لتشغيل سكربت *setup_ml.py* وبدء عملية الضبط الدقيق في Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. في هذا التمرين، قمت بضبط نموذج Phi-3 بنجاح باستخدام Azure Machine Learning. عبر تشغيل سكربت *setup_ml.py*، قمت بإعداد بيئة Azure Machine Learning وبدأت عملية الضبط الدقيق المعرفة في ملف *fine_tune.py*. يرجى ملاحظة أن عملية الضبط الدقيق قد تستغرق وقتًا طويلًا. بعد تشغيل الأمر `python setup_ml.py`، تحتاج إلى الانتظار حتى تكتمل العملية. يمكنك مراقبة حالة مهمة الضبط عن طريق متابعة الرابط المقدم في الطرفية إلى بوابة Azure Machine Learning.

    ![عرض مهمة الضبط.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.ar.png)

### نشر النموذج المُحسّن

لدمج نموذج Phi-3 المُحسّن مع Prompt Flow، تحتاج إلى نشر النموذج لجعله متاحًا للاستدلال في الوقت الحقيقي. تتضمن هذه العملية تسجيل النموذج، وإنشاء endpoint عبر الإنترنت، ونشر النموذج.

#### تعيين اسم النموذج، واسم الـ endpoint، واسم النشر

1. افتح ملف *config.py*.

1. استبدل `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` بالاسم المطلوب لنموذجك.

1. استبدل `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` بالاسم المطلوب لنقطة النهاية (endpoint).

1. استبدل `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` بالاسم المطلوب لنشر النموذج.

#### إضافة الكود إلى ملف *deploy_model.py*

تشغيل ملف *deploy_model.py* يؤتمت عملية النشر بأكملها. يقوم بتسجيل النموذج، وإنشاء endpoint، وتنفيذ النشر وفقًا للإعدادات المحددة في ملف config.py، والذي يتضمن اسم النموذج واسم الـ endpoint واسم النشر.

1. افتح ملف *deploy_model.py* في Visual Studio Code.

1. أضف الكود التالي إلى *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # استيرادات التكوين
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # ثوابت
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # إعداد التسجيل
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # جلب تفاصيل نقطة النهاية الحالية
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # تسجيل تخصيص حركة المرور الحالي لأغراض التصحيح
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # تعيين تخصيص حركة المرور للنشر
            endpoint.traffic = {deployment_name: 100}
            
            # تحديث نقطة النهاية بتخصيص حركة المرور الجديد
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # تسجيل تخصيص حركة المرور المحدث لتصحيح الأخطاء
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # تسجيل أي أخطاء تحدث أثناء العملية
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. قم بالمهام التالية للحصول على قيمة `JOB_NAME`:

    - انتقل إلى مورد Azure Machine Learning الذي قمت بإنشائه.
    - حدد **Studio web URL** لفتح مساحة عمل Azure Machine Learning.
    - حدد **Jobs** من علامة التبويب الجانبية.
    - حدد التجربة الخاصة بالضبط الدقيق. على سبيل المثال، *finetunephi*.
    - حدد المهمة (job) التي قمت بإنشائها.
    - انسخ والصق اسم وظيفتك في `JOB_NAME = "your-job-name"` في ملف *deploy_model.py*.

1. استبدل `COMPUTE_INSTANCE_TYPE` بتفاصيلك المحددة.

1. اكتب الأمر التالي لتشغيل سكربت *deploy_model.py* وبدء عملية النشر في Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> لتجنب رسوم إضافية على حسابك، تأكد من حذف نقطة النهاية التي تم إنشاؤها في مساحة عمل Azure Machine Learning.
>

#### Check deployment status in Azure Machine Learning Workspace

1. قم بزيارة [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. حدد **Studio web URL** لفتح مساحة عمل Azure Machine Learning.

1. حدد **Endpoints** من علامة التبويب على الجانب الأيسر.

    ![حدد نقاط النهاية.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.ar.png)

2. حدد نقطة النهاية التي قمت بإنشائها.

    ![حدد نقطة النهاية التي قمت بإنشائها.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.ar.png)

3. في هذه الصفحة، يمكنك إدارة نقاط النهاية التي تم إنشاؤها أثناء عملية النشر.

## Scenario 3: Integrate with Prompt flow and Chat with your custom model

### Integrate the custom Phi-3 model with Prompt flow

بعد نشر نموذجك الذي تم تحسينه بنجاح، يمكنك الآن دمجه مع Prompt flow لاستخدامه في تطبيقات الزمن الحقيقي، مما يتيح مجموعة متنوعة من المهام التفاعلية مع نموذج Phi-3 المخصص الخاص بك.

#### Set api key and endpoint uri of the fine-tuned Phi-3 model

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.
1. حدد **Endpoints** من علامة التبويب على الجانب الأيسر.
1. حدد نقطة النهاية التي قمت بإنشائها.
1. حدد **Consume** من قائمة التنقل.
1. انسخ والصق **REST endpoint** الخاص بك في ملف *config.py*، مع استبدال `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` بـ **REST endpoint** الخاص بك.
1. انسخ والصق **Primary key** الخاص بك في ملف *config.py*، مع استبدال `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` بـ **Primary key** الخاص بك.

    ![انسخ مفتاح API وURI نقطة النهاية.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.ar.png)

#### Add code to the *flow.dag.yml* file

1. افتح ملف *flow.dag.yml* في Visual Studio Code.

1. أضف الكود التالي إلى *flow.dag.yml*.

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

#### Add code to the *integrate_with_promptflow.py* file

1. افتح ملف *integrate_with_promptflow.py* في Visual Studio Code.

1. أضف الكود التالي إلى *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # إعداد السجلات
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Chat with your custom model

1. اكتب الأمر التالي لتشغيل سكربت *deploy_model.py* وبدء عملية النشر في Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. فيما يلي مثال على النتائج: الآن يمكنك الدردشة مع نموذج Phi-3 المخصص الخاص بك. يُنصح بطرح أسئلة مستندة إلى البيانات المستخدمة في التحسين.

    ![مثال على Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.ar.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء المسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى ملاحظة أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر المعتمد. للمعلومات الحرجة، يُنصح بالاستعانة بمترجم بشري محترف. نحن لا نتحمل أي مسؤولية عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->