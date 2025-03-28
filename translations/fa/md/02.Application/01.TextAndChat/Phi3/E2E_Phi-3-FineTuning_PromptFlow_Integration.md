<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-03-27T10:08:04+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "fa"
}
-->
# تنظیم و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow

این نمونه کامل (E2E) بر اساس راهنمای "[تنظیم و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow: راهنمای گام‌به‌گام](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" از Microsoft Tech Community است. این راهنما فرآیندهای تنظیم دقیق، استقرار و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow را معرفی می‌کند.

## مرور کلی

در این نمونه کامل، یاد خواهید گرفت که چگونه مدل Phi-3 را تنظیم کنید و آن را با Prompt Flow یکپارچه کنید. با استفاده از Azure Machine Learning و Prompt Flow، یک جریان کاری برای استقرار و استفاده از مدل‌های هوش مصنوعی سفارشی ایجاد خواهید کرد. این نمونه کامل به سه سناریو تقسیم شده است:

**سناریو 1: تنظیم منابع Azure و آماده‌سازی برای تنظیم دقیق**

**سناریو 2: تنظیم دقیق مدل Phi-3 و استقرار در Azure Machine Learning Studio**

**سناریو 3: یکپارچه‌سازی با Prompt Flow و گفتگو با مدل سفارشی شما**

در اینجا یک مرور کلی از این نمونه کامل ارائه شده است.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.fa.png)

### فهرست مطالب

1. **[سناریو 1: تنظیم منابع Azure و آماده‌سازی برای تنظیم دقیق](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ایجاد یک Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [درخواست سهمیه GPU در اشتراک Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [افزودن نقش دسترسی](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [تنظیم پروژه](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [آماده‌سازی مجموعه داده برای تنظیم دقیق](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[سناریو 2: تنظیم دقیق مدل Phi-3 و استقرار در Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [تنظیم Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [تنظیم دقیق مدل Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [استقرار مدل تنظیم‌شده](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[سناریو 3: یکپارچه‌سازی با Prompt Flow و گفتگو با مدل سفارشی شما](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [یکپارچه‌سازی مدل سفارشی Phi-3 با Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [گفتگو با مدل سفارشی شما](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## سناریو 1: تنظیم منابع Azure و آماده‌سازی برای تنظیم دقیق

### ایجاد یک Azure Machine Learning Workspace

1. عبارت *azure machine learning* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Azure Machine Learning** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.fa.png)

1. از منوی ناوبری **+ Create** را انتخاب کنید.

1. از منوی ناوبری **New workspace** را انتخاب کنید.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.fa.png)

1. وظایف زیر را انجام دهید:

    - **اشتراک Azure** خود را انتخاب کنید.
    - **گروه منابع** را انتخاب کنید (در صورت نیاز یک گروه جدید ایجاد کنید).
    - **نام Workspace** را وارد کنید. این باید یک مقدار منحصر به فرد باشد.
    - **منطقه** مورد نظر خود را انتخاب کنید.
    - **حساب ذخیره‌سازی** مورد استفاده را انتخاب کنید (در صورت نیاز یک حساب جدید ایجاد کنید).
    - **Key vault** مورد استفاده را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).
    - **Application insights** مورد استفاده را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).
    - **Container registry** مورد استفاده را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.fa.png)

1. **Review + Create** را انتخاب کنید.

1. **Create** را انتخاب کنید.

### درخواست سهمیه GPU در اشتراک Azure

در این نمونه کامل، از *Standard_NC24ads_A100_v4 GPU* برای تنظیم دقیق استفاده خواهید کرد که نیاز به درخواست سهمیه دارد، و از *Standard_E4s_v3 CPU* برای استقرار استفاده خواهید کرد که نیاز به درخواست سهمیه ندارد.

> [!NOTE]
>
> تنها اشتراک‌های Pay-As-You-Go (نوع استاندارد اشتراک) واجد شرایط تخصیص GPU هستند؛ اشتراک‌های مزایا در حال حاضر پشتیبانی نمی‌شوند.
>
> برای کسانی که از اشتراک‌های مزایا (مانند Visual Studio Enterprise Subscription) استفاده می‌کنند یا کسانی که قصد دارند فرآیند تنظیم دقیق و استقرار را سریع آزمایش کنند، این آموزش راهنمایی‌هایی برای تنظیم دقیق با یک مجموعه داده کوچک با استفاده از CPU ارائه می‌دهد. با این حال، توجه داشته باشید که نتایج تنظیم دقیق با استفاده از GPU و مجموعه داده‌های بزرگ‌تر به طور قابل توجهی بهتر است.

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

1. وظایف زیر را برای درخواست سهمیه *Standard NCADSA100v4 Family* انجام دهید:

    - از تب سمت چپ **Quota** را انتخاب کنید.
    - **خانواده ماشین مجازی** مورد استفاده را انتخاب کنید. به عنوان مثال، **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** را انتخاب کنید که شامل *Standard_NC24ads_A100_v4 GPU* است.
    - از منوی ناوبری **Request quota** را انتخاب کنید.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.fa.png)

    - در صفحه Request quota، **محدودیت جدید هسته‌ها** مورد نظر خود را وارد کنید. به عنوان مثال، 24.
    - در صفحه Request quota، **Submit** را برای درخواست سهمیه GPU انتخاب کنید.

> [!NOTE]
> می‌توانید GPU یا CPU مناسب نیاز خود را با مراجعه به سند [اندازه‌های ماشین‌های مجازی در Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) انتخاب کنید.

### افزودن نقش دسترسی

برای تنظیم دقیق و استقرار مدل‌های خود، ابتدا باید یک User Assigned Managed Identity (UAI) ایجاد کنید و مجوزهای مناسب را به آن اختصاص دهید. این UAI برای احراز هویت در طول فرآیند استقرار استفاده خواهد شد.

#### ایجاد User Assigned Managed Identity(UAI)

1. عبارت *managed identities* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Managed Identities** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.fa.png)

1. **+ Create** را انتخاب کنید.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.fa.png)

1. وظایف زیر را انجام دهید:

    - **اشتراک Azure** خود را انتخاب کنید.
    - **گروه منابع** مورد استفاده را انتخاب کنید (در صورت نیاز یک گروه جدید ایجاد کنید).
    - **منطقه** مورد نظر خود را انتخاب کنید.
    - **نام** را وارد کنید. این باید یک مقدار منحصر به فرد باشد.

1. **Review + create** را انتخاب کنید.

1. **+ Create** را انتخاب کنید.

#### افزودن نقش Contributor به Managed Identity

1. به منبع Managed Identity که ایجاد کرده‌اید بروید.

1. از تب سمت چپ **Azure role assignments** را انتخاب کنید.

1. از منوی ناوبری **+Add role assignment** را انتخاب کنید.

1. در صفحه Add role assignment، وظایف زیر را انجام دهید:
    - **Scope** را به **Resource group** تنظیم کنید.
    - **اشتراک Azure** خود را انتخاب کنید.
    - **گروه منابع** مورد استفاده را انتخاب کنید.
    - **نقش** را به **Contributor** تنظیم کنید.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.fa.png)

1. **Save** را انتخاب کنید.

#### افزودن نقش Storage Blob Data Reader به Managed Identity

1. عبارت *storage accounts* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Storage accounts** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.fa.png)

1. حساب ذخیره‌سازی مرتبط با Azure Machine Learning workspace که ایجاد کرده‌اید را انتخاب کنید. به عنوان مثال، *finetunephistorage*.

1. وظایف زیر را برای رفتن به صفحه Add role assignment انجام دهید:

    - به حساب ذخیره‌سازی Azure که ایجاد کرده‌اید بروید.
    - از تب سمت چپ **Access Control (IAM)** را انتخاب کنید.
    - از منوی ناوبری **+ Add** را انتخاب کنید.
    - از منوی ناوبری **Add role assignment** را انتخاب کنید.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.fa.png)

1. در صفحه Add role assignment، وظایف زیر را انجام دهید:

    - در صفحه Role، عبارت *Storage Blob Data Reader* را در **نوار جستجو** تایپ کنید و **Storage Blob Data Reader** را از گزینه‌های ظاهر شده انتخاب کنید.
    - در صفحه Role، **Next** را انتخاب کنید.
    - در صفحه Members، **Assign access to** را به **Managed identity** تنظیم کنید.
    - در صفحه Members، **+ Select members** را انتخاب کنید.
    - در صفحه Select managed identities، **اشتراک Azure** خود را انتخاب کنید.
    - در صفحه Select managed identities، **Managed identity** را به **Manage Identity** تنظیم کنید.
    - در صفحه Select managed identities، Managed Identity که ایجاد کرده‌اید را انتخاب کنید. به عنوان مثال، *finetunephi-managedidentity*.
    - در صفحه Select managed identities، **Select** را انتخاب کنید.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.fa.png)

1. **Review + assign** را انتخاب کنید.

#### افزودن نقش AcrPull به Managed Identity

1. عبارت *container registries* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Container registries** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.fa.png)

1. Container registry مرتبط با Azure Machine Learning workspace را انتخاب کنید. به عنوان مثال، *finetunephicontainerregistries*

1. وظایف زیر را برای رفتن به صفحه Add role assignment انجام دهید:

    - از تب سمت چپ **Access Control (IAM)** را انتخاب کنید.
    - از منوی ناوبری **+ Add** را انتخاب کنید.
    - از منوی ناوبری **Add role assignment** را انتخاب کنید.

1. در صفحه Add role assignment، وظایف زیر را انجام دهید:

    - در صفحه Role، عبارت *AcrPull* را در **نوار جستجو** تایپ کنید و **AcrPull** را از گزینه‌های ظاهر شده انتخاب کنید.
    - در صفحه Role، **Next** را انتخاب کنید.
    - در صفحه Members، **Assign access to** را به **Managed identity** تنظیم کنید.
    - در صفحه Members، **+ Select members** را انتخاب کنید.
    - در صفحه Select managed identities، **اشتراک Azure** خود را انتخاب کنید.
    - در صفحه Select managed identities، **Managed identity** را به **Manage Identity** تنظیم کنید.
    - در صفحه Select managed identities، Managed Identity که ایجاد کرده‌اید را انتخاب کنید. به عنوان مثال، *finetunephi-managedidentity*.
    - در صفحه Select managed identities، **Select** را انتخاب کنید.
    - **Review + assign** را انتخاب کنید.

### تنظیم پروژه

اکنون، یک پوشه برای کار ایجاد خواهید کرد و یک محیط مجازی برای توسعه برنامه‌ای که با کاربران تعامل دارد و از تاریخچه چت ذخیره‌شده در Azure Cosmos DB برای پاسخ‌های خود استفاده می‌کند، تنظیم خواهید کرد.

#### ایجاد یک پوشه برای کار داخل آن

1. یک پنجره ترمینال باز کنید و دستور زیر را برای ایجاد یک پوشه به نام *finetune-phi* در مسیر پیش‌فرض تایپ کنید.

    ```console
    mkdir finetune-phi
    ```

1. دستور زیر را در ترمینال خود تایپ کنید تا به پوشه *finetune-phi* که ایجاد کرده‌اید، بروید.

    ```console
    cd finetune-phi
    ```

#### ایجاد یک محیط مجازی

1. دستور زیر را در ترمینال خود تایپ کنید تا یک محیط مجازی به نام *.venv* ایجاد کنید.

    ```console
    python -m venv .venv
    ```

1. دستور زیر را در ترمینال خود تایپ کنید تا محیط مجازی را فعال کنید.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> اگر موفقیت‌آمیز بود، باید *(.venv)* را قبل از خط فرمان ببینید.

#### نصب بسته‌های مورد نیاز

1. دستورات زیر را در ترمینال خود تایپ کنید تا بسته‌های مورد نیاز را نصب کنید.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### ایجاد فایل‌های پروژه

در این تمرین، فایل‌های ضروری پروژه خود را ایجاد خواهید کرد. این فایل‌ها شامل اسکریپت‌هایی برای دانلود مجموعه داده، تنظیم محیط Azure Machine Learning، تنظیم دقیق مدل Phi-3، و استقرار مدل تنظیم‌شده هستند. همچنین یک فایل *conda.yml* برای تنظیم محیط تنظیم دقیق ایجاد خواهید کرد.

در این تمرین، موارد زیر را انجام خواهید داد:

- ایجاد یک فایل *download_dataset.py* برای دانلود مجموعه داده.
- ایجاد یک فایل *setup_ml.py* برای تنظیم محیط Azure Machine Learning.
- ایجاد یک فایل *fine_tune.py* در پوشه *finetuning_dir* برای تنظیم دقیق مدل Phi-3 با استفاده از مجموعه داده.
- ایجاد یک فایل *conda.yml* برای تنظیم محیط تنظیم دقیق.
- ایجاد یک فایل *deploy_model.py* برای استقرار مدل تنظیم‌شده.
- ایجاد یک فایل *integrate_with_promptflow.py* برای یکپارچه‌سازی مدل تنظیم‌شده و اجرای مدل با استفاده از Prompt Flow.
- ایجاد یک فایل flow.dag.yml برای تنظیم ساختار جریان کاری برای Prompt Flow.
- ایجاد یک فایل *config.py* برای وارد کردن اطلاعات Azure.

> [!NOTE]
>
> ساختار کامل پوشه:
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

1. **Visual Studio Code** را باز کنید.

1. از نوار منوی بالا **File** را انتخاب کنید.

1. **Open Folder** را انتخاب کنید.

1. پوشه *finetune-phi* که ایجاد کرده‌اید را انتخاب کنید، که در مسیر *C:\Users\yourUserName\finetune-phi* قرار دارد.

    ![Open project folder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.fa.png)

1. در پانل سمت چپ Visual Studio Code، کلیک راست کنید و **New File** را انتخاب کنید تا یک فایل جدید به نام *download_dataset.py* ایجاد کنید.

1. در پانل سمت چپ Visual Studio Code، کلیک راست کنید و **New File** را انتخاب کنید تا یک فایل جدید به نام *setup_ml.py* ایجاد کنید.

1. در پانل سمت چپ Visual Studio Code، کلیک راست کنید و **New File** را انتخاب کنید تا یک فایل جدید به نام *deploy_model.py* ایجاد کنید.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.fa.png)

1. در پانل سمت چپ Visual Studio Code، کلیک راست کنید و **New Folder** را انتخاب کنید تا یک پوشه جدید به نام *finetuning_dir* ایجاد کنید.

1. در پوشه *finetuning_dir*، یک فایل جدید به نام *fine_tune.py* ایجاد کنید.

#### ایجاد و تنظیم فایل *conda.yml*

1. در پانل سمت چپ Visual Studio Code، کلیک راست کنید و **New File** را انتخاب کنید تا یک فایل جدید به نام *conda.yml* ایجاد کنید.

1. کد زیر را به فایل *conda.yml* اضافه کنید تا محیط تنظیم دقیق برای مدل Phi-3 تنظیم شود.

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

#### ایجاد و تنظیم فایل *config.py*

1. در پانل سمت چپ Visual Studio Code، کلیک راست کنید و **New File** را انتخاب کنید تا یک فایل جدید به نام *config.py* ایجاد کنید.

1. کد زیر را به فایل *config.py* اضافه کنید تا اطلاعات Azure شما را شامل شود.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### افزودن متغیرهای محیط Azure

1. وظایف زیر را برای افزودن Subscription ID Azure انجام دهید:

    - عبارت *subscriptions* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Subscriptions** را از گزینه‌های ظاهر شده انتخاب کنید.
    - Subscription Azure که در حال حاضر استفاده می‌کنید را انتخاب کنید.
    - Subscription ID خود را کپی کرده و در فایل *config.py* قرار دهید.
![شناسه اشتراک را پیدا کنید.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.fa.png)

1. مراحل زیر را برای افزودن نام Azure Workspace انجام دهید:

    - به منبع Azure Machine Learning که ایجاد کرده‌اید بروید.
    - نام حساب خود را کپی کرده و در فایل *config.py* قرار دهید.

    ![نام Azure Machine Learning را پیدا کنید.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.fa.png)

1. مراحل زیر را برای افزودن نام گروه منابع Azure انجام دهید:

    - به منبع Azure Machine Learning که ایجاد کرده‌اید بروید.
    - نام گروه منابع Azure خود را کپی کرده و در فایل *config.py* قرار دهید.

    ![نام گروه منابع را پیدا کنید.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.fa.png)

2. مراحل زیر را برای افزودن نام Azure Managed Identity انجام دهید:

    - به منبع Managed Identities که ایجاد کرده‌اید بروید.
    - نام Azure Managed Identity خود را کپی کرده و در فایل *config.py* قرار دهید.

    ![UAI را پیدا کنید.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.fa.png)

### آماده‌سازی مجموعه داده برای تنظیم دقیق

در این تمرین، فایل *download_dataset.py* را اجرا خواهید کرد تا مجموعه داده‌های *ULTRACHAT_200k* را به محیط محلی خود دانلود کنید. سپس از این مجموعه داده‌ها برای تنظیم دقیق مدل Phi-3 در Azure Machine Learning استفاده خواهید کرد.

#### دانلود مجموعه داده با استفاده از *download_dataset.py*

1. فایل *download_dataset.py* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *download_dataset.py* اضافه کنید.

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
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **راهنمایی برای تنظیم دقیق با یک مجموعه داده کوچک با استفاده از CPU**
>
> اگر می‌خواهید از CPU برای تنظیم دقیق استفاده کنید، این روش برای کسانی که اشتراک‌های مزایایی (مانند اشتراک Visual Studio Enterprise) دارند یا برای آزمایش سریع فرآیند تنظیم دقیق و استقرار مناسب است.
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. دستور زیر را در ترمینال خود وارد کنید تا اسکریپت اجرا شده و مجموعه داده به محیط محلی شما دانلود شود.

    ```console
    python download_data.py
    ```

1. اطمینان حاصل کنید که مجموعه داده‌ها به درستی در دایرکتوری محلی *finetune-phi/data* ذخیره شده‌اند.

> [!NOTE]
>
> **اندازه مجموعه داده و زمان تنظیم دقیق**
>
> در این نمونه E2E، تنها از 1% مجموعه داده (`train_sft[:1%]`) استفاده می‌کنید. این کار مقدار داده را به طور قابل توجهی کاهش می‌دهد و فرآیند آپلود و تنظیم دقیق را سریع‌تر می‌کند. می‌توانید درصد را تنظیم کنید تا تعادل مناسبی بین زمان آموزش و عملکرد مدل پیدا کنید. استفاده از یک زیرمجموعه کوچک‌تر از مجموعه داده زمان لازم برای تنظیم دقیق را کاهش داده و فرآیند را برای نمونه E2E قابل مدیریت‌تر می‌کند.

## سناریو 2: تنظیم دقیق مدل Phi-3 و استقرار در Azure Machine Learning Studio

### تنظیم Azure CLI

برای احراز هویت محیط خود نیاز به تنظیم Azure CLI دارید. Azure CLI به شما امکان مدیریت منابع Azure را مستقیماً از خط فرمان می‌دهد و اعتبارنامه‌های لازم برای دسترسی Azure Machine Learning به این منابع را فراهم می‌کند. برای شروع، [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) را نصب کنید.

1. یک پنجره ترمینال باز کنید و دستور زیر را برای ورود به حساب Azure خود وارد کنید.

    ```console
    az login
    ```

1. حساب Azure خود را انتخاب کنید.

1. اشتراک Azure خود را انتخاب کنید.

    ![نام گروه منابع را پیدا کنید.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.fa.png)

> [!TIP]
>
> اگر در ورود به Azure مشکل دارید، می‌توانید از کد دستگاه استفاده کنید. یک پنجره ترمینال باز کنید و دستور زیر را برای ورود به حساب Azure خود وارد کنید:
>
> ```console
> az login --use-device-code
> ```
>

### تنظیم دقیق مدل Phi-3

در این تمرین، مدل Phi-3 را با استفاده از مجموعه داده ارائه شده تنظیم دقیق خواهید کرد. ابتدا فرآیند تنظیم دقیق را در فایل *fine_tune.py* تعریف خواهید کرد. سپس محیط Azure Machine Learning را پیکربندی کرده و فرآیند تنظیم دقیق را با اجرای فایل *setup_ml.py* آغاز خواهید کرد. این اسکریپت تضمین می‌کند که تنظیم دقیق در محیط Azure Machine Learning انجام می‌شود.

با اجرای *setup_ml.py*، فرآیند تنظیم دقیق در محیط Azure Machine Learning انجام خواهد شد.

#### افزودن کد به فایل *fine_tune.py*

1. به پوشه *finetuning_dir* بروید و فایل *fine_tune.py* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *fine_tune.py* اضافه کنید.

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

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
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

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
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

1. فایل *fine_tune.py* را ذخیره کرده و ببندید.

> [!TIP]
> **می‌توانید مدل Phi-3.5 را تنظیم دقیق کنید**
>
> در فایل *fine_tune.py*، می‌توانید فیلد `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` را در اسکریپت خود تغییر دهید.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="تنظیم دقیق Phi-3.5.":::
>

#### افزودن کد به فایل *setup_ml.py*

1. فایل *setup_ml.py* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *setup_ml.py* اضافه کنید.

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

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
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
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
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
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` را با جزئیات خاص خود جایگزین کنید.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **راهنمایی برای تنظیم دقیق با یک مجموعه داده کوچک با استفاده از CPU**
>
> اگر می‌خواهید از CPU برای تنظیم دقیق استفاده کنید، این روش برای کسانی که اشتراک‌های مزایایی (مانند اشتراک Visual Studio Enterprise) دارند یا برای آزمایش سریع فرآیند تنظیم دقیق و استقرار مناسب است.
>
> 1. فایل *setup_ml* را باز کنید.
> 1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` را با جزئیات خاص خود جایگزین کنید.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. دستور زیر را برای اجرای اسکریپت *setup_ml.py* و آغاز فرآیند تنظیم دقیق در Azure Machine Learning وارد کنید.

    ```python
    python setup_ml.py
    ```

1. در این تمرین، شما مدل Phi-3 را با موفقیت با استفاده از Azure Machine Learning تنظیم دقیق کرده‌اید. با اجرای اسکریپت *setup_ml.py*، محیط Azure Machine Learning را تنظیم کرده و فرآیند تنظیم دقیق تعریف شده در فایل *fine_tune.py* را آغاز کرده‌اید. لطفاً توجه داشته باشید که فرآیند تنظیم دقیق ممکن است زمان قابل توجهی طول بکشد. پس از اجرای `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.fa.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` با نام دلخواه برای استقرار خود.

#### افزودن کد به فایل *deploy_model.py*

اجرای فایل *deploy_model.py* کل فرآیند استقرار را خودکار می‌کند. این فایل مدل را ثبت می‌کند، یک endpoint ایجاد می‌کند و استقرار را بر اساس تنظیمات مشخص شده در فایل config.py، که شامل نام مدل، نام endpoint و نام استقرار است، اجرا می‌کند.

1. فایل *deploy_model.py* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *deploy_model.py* اضافه کنید.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
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

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
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
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
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

1. مراحل زیر را برای دریافت `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` با جزئیات خاص خود انجام دهید.

1. دستور زیر را برای اجرای اسکریپت *deploy_model.py* و آغاز فرآیند استقرار در Azure Machine Learning وارد کنید.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> برای جلوگیری از هزینه‌های اضافی در حساب خود، مطمئن شوید که endpoint ایجاد شده در فضای کاری Azure Machine Learning را حذف کنید.
>

#### بررسی وضعیت استقرار در فضای کاری Azure Machine Learning

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) بروید.

1. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.

1. **Studio web URL** را انتخاب کنید تا فضای کاری Azure Machine Learning باز شود.

1. از تب سمت چپ **Endpoints** را انتخاب کنید.

    ![Endpoints را انتخاب کنید.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.fa.png)

2. Endpoint ایجاد شده را انتخاب کنید.

    ![Endpoint ایجاد شده را انتخاب کنید.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.fa.png)

3. در این صفحه، می‌توانید Endpoint‌های ایجاد شده در طول فرآیند استقرار را مدیریت کنید.

## سناریو 3: ادغام با Prompt flow و گفتگو با مدل سفارشی خود

### ادغام مدل سفارشی Phi-3 با Prompt flow

پس از استقرار موفقیت‌آمیز مدل تنظیم دقیق شده، اکنون می‌توانید آن را با Prompt flow ادغام کنید تا از مدل خود در برنامه‌های بلادرنگ استفاده کنید و انواع وظایف تعاملی را با مدل سفارشی Phi-3 خود انجام دهید.

#### تنظیم کلید API و آدرس endpoint مدل تنظیم دقیق شده Phi-3

1. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.
1. از تب سمت چپ **Endpoints** را انتخاب کنید.
1. Endpoint ایجاد شده را انتخاب کنید.
1. از منوی ناوبری **Consume** را انتخاب کنید.
1. **REST endpoint** خود را کپی کرده و در فایل *config.py* قرار دهید و `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` را با **Primary key** خود جایگزین کنید.

    ![کلید API و آدرس endpoint را کپی کنید.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.fa.png)

#### افزودن کد به فایل *flow.dag.yml*

1. فایل *flow.dag.yml* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *flow.dag.yml* اضافه کنید.

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

#### افزودن کد به فایل *integrate_with_promptflow.py*

1. فایل *integrate_with_promptflow.py* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *integrate_with_promptflow.py* اضافه کنید.

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

    # Logging setup
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

### گفتگو با مدل سفارشی خود

1. دستور زیر را برای اجرای اسکریپت *deploy_model.py* و آغاز فرآیند استقرار در Azure Machine Learning وارد کنید.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. در اینجا یک مثال از نتایج آورده شده است: اکنون می‌توانید با مدل سفارشی Phi-3 خود گفتگو کنید. توصیه می‌شود سوالاتی بر اساس داده‌های استفاده شده برای تنظیم دقیق بپرسید.

    ![مثال Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.fa.png)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌هایی باشد. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ‌گونه مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.