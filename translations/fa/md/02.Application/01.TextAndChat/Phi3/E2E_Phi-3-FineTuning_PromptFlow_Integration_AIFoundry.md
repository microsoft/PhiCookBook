<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-07T14:11:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "fa"
}
-->
# تنظیم دقیق و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt flow در Azure AI Foundry

این نمونه انتها به انتها (E2E) بر اساس راهنمای "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" از Microsoft Tech Community تهیه شده است. این آموزش فرآیندهای تنظیم دقیق، استقرار و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt flow در Azure AI Foundry را معرفی می‌کند. بر خلاف نمونه E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" که شامل اجرای کد به صورت محلی بود، این آموزش کاملاً بر روی تنظیم دقیق و یکپارچه‌سازی مدل شما در داخل Azure AI / ML Studio تمرکز دارد.

## مرور کلی

در این نمونه E2E، شما یاد می‌گیرید چگونه مدل Phi-3 را تنظیم دقیق کنید و آن را با Prompt flow در Azure AI Foundry یکپارچه نمایید. با استفاده از Azure AI / ML Studio، یک جریان کاری برای استقرار و استفاده از مدل‌های هوش مصنوعی سفارشی ایجاد خواهید کرد. این نمونه E2E به سه سناریو تقسیم شده است:

**سناریو ۱: راه‌اندازی منابع Azure و آماده‌سازی برای تنظیم دقیق**

**سناریو ۲: تنظیم دقیق مدل Phi-3 و استقرار در Azure Machine Learning Studio**

**سناریو ۳: یکپارچه‌سازی با Prompt flow و گفتگو با مدل سفارشی خود در Azure AI Foundry**

در ادامه نمای کلی این نمونه E2E آورده شده است.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.fa.png)

### فهرست مطالب

1. **[سناریو ۱: راه‌اندازی منابع Azure و آماده‌سازی برای تنظیم دقیق](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ایجاد یک فضای کاری Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [درخواست سهمیه GPU در اشتراک Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [افزودن تخصیص نقش](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [راه‌اندازی پروژه](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [آماده‌سازی مجموعه داده برای تنظیم دقیق](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[سناریو ۲: تنظیم دقیق مدل Phi-3 و استقرار در Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [تنظیم دقیق مدل Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [استقرار مدل Phi-3 تنظیم دقیق شده](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[سناریو ۳: یکپارچه‌سازی با Prompt flow و گفتگو با مدل سفارشی خود در Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [یکپارچه‌سازی مدل سفارشی Phi-3 با Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [گفتگو با مدل سفارشی Phi-3 خود](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## سناریو ۱: راه‌اندازی منابع Azure و آماده‌سازی برای تنظیم دقیق

### ایجاد یک فضای کاری Azure Machine Learning

1. در **نوار جستجو** بالای صفحه پرتال، عبارت *azure machine learning* را تایپ کنید و از گزینه‌های ظاهر شده **Azure Machine Learning** را انتخاب کنید.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.fa.png)

2. از منوی ناوبری، گزینه **+ Create** را انتخاب کنید.

3. از منوی ناوبری، **New workspace** را انتخاب کنید.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.fa.png)

4. موارد زیر را انجام دهید:

    - اشتراک Azure خود را انتخاب کنید.
    - گروه منابع (Resource group) مورد نظر را انتخاب کنید (در صورت نیاز یک گروه جدید بسازید).
    - نام فضای کاری (Workspace Name) را وارد کنید. این نام باید منحصر به فرد باشد.
    - منطقه (Region) مورد نظر خود را انتخاب کنید.
    - حساب ذخیره‌سازی (Storage account) مورد استفاده را انتخاب کنید (در صورت نیاز یک حساب جدید بسازید).
    - مخزن کلید (Key vault) مورد استفاده را انتخاب کنید (در صورت نیاز یک مخزن جدید بسازید).
    - Application insights مورد استفاده را انتخاب کنید (در صورت نیاز یک نمونه جدید بسازید).
    - مخزن کانتینر (Container registry) مورد استفاده را انتخاب کنید (در صورت نیاز یک مخزن جدید بسازید).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.fa.png)

5. روی **Review + Create** کلیک کنید.

6. سپس **Create** را انتخاب کنید.

### درخواست سهمیه GPU در اشتراک Azure

در این آموزش، شما یاد می‌گیرید چگونه مدل Phi-3 را با استفاده از GPUها تنظیم دقیق و استقرار دهید. برای تنظیم دقیق، از GPU نوع *Standard_NC24ads_A100_v4* استفاده می‌کنید که نیاز به درخواست سهمیه دارد. برای استقرار نیز از GPU نوع *Standard_NC6s_v3* استفاده می‌شود که آن هم نیاز به درخواست سهمیه دارد.

> [!NOTE]
>
> فقط اشتراک‌های Pay-As-You-Go (نوع اشتراک استاندارد) برای تخصیص GPU واجد شرایط هستند؛ اشتراک‌های بهره‌مند در حال حاضر پشتیبانی نمی‌شوند.
>

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

1. برای درخواست سهمیه *Standard NCADSA100v4 Family* مراحل زیر را انجام دهید:

    - از تب سمت چپ **Quota** را انتخاب کنید.
    - خانواده ماشین مجازی مورد نظر را انتخاب کنید. به عنوان مثال، **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** که شامل GPU *Standard_NC24ads_A100_v4* است.
    - از منوی ناوبری، **Request quota** را انتخاب کنید.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.fa.png)

    - در صفحه درخواست سهمیه، مقدار **New cores limit** مورد نظر خود را وارد کنید، مثلاً ۲۴.
    - در همان صفحه، روی **Submit** کلیک کنید تا درخواست سهمیه GPU ثبت شود.

1. برای درخواست سهمیه *Standard NCSv3 Family* مراحل زیر را انجام دهید:

    - از تب سمت چپ **Quota** را انتخاب کنید.
    - خانواده ماشین مجازی مورد نظر را انتخاب کنید. به عنوان مثال، **Standard NCSv3 Family Cluster Dedicated vCPUs** که شامل GPU *Standard_NC6s_v3* است.
    - از منوی ناوبری، **Request quota** را انتخاب کنید.
    - مقدار **New cores limit** مورد نظر خود را وارد کنید، مثلاً ۲۴.
    - روی **Submit** کلیک کنید تا درخواست سهمیه GPU ثبت شود.

### افزودن تخصیص نقش

برای تنظیم دقیق و استقرار مدل‌های خود، ابتدا باید یک Managed Identity اختصاص داده شده به کاربر (User Assigned Managed Identity یا UAI) ایجاد کرده و مجوزهای لازم را به آن اختصاص دهید. این UAI برای احراز هویت در هنگام استقرار استفاده خواهد شد.

#### ایجاد User Assigned Managed Identity (UAI)

1. در **نوار جستجو** بالای صفحه پرتال، عبارت *managed identities* را تایپ کرده و از گزینه‌های ظاهر شده **Managed Identities** را انتخاب کنید.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.fa.png)

1. روی **+ Create** کلیک کنید.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.fa.png)

1. موارد زیر را انجام دهید:

    - اشتراک Azure خود را انتخاب کنید.
    - گروه منابع (Resource group) مورد نظر را انتخاب کنید (در صورت نیاز یک گروه جدید بسازید).
    - منطقه (Region) مورد نظر را انتخاب کنید.
    - نامی منحصر به فرد وارد کنید.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.fa.png)

1. روی **Review + create** کلیک کنید.

1. سپس **+ Create** را انتخاب کنید.

#### افزودن تخصیص نقش Contributor به Managed Identity

1. به منبع Managed Identity که ایجاد کرده‌اید بروید.

1. از تب سمت چپ، **Azure role assignments** را انتخاب کنید.

1. از منوی ناوبری، **+Add role assignment** را انتخاب کنید.

1. در صفحه افزودن تخصیص نقش، موارد زیر را انجام دهید:
    - **Scope** را روی **Resource group** تنظیم کنید.
    - اشتراک Azure خود را انتخاب کنید.
    - گروه منابع مورد استفاده را انتخاب کنید.
    - نقش (Role) را روی **Contributor** تنظیم کنید.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.fa.png)

2. روی **Save** کلیک کنید.

#### افزودن تخصیص نقش Storage Blob Data Reader به Managed Identity

1. در **نوار جستجو** بالای صفحه پرتال، عبارت *storage accounts* را تایپ کرده و از گزینه‌های ظاهر شده **Storage accounts** را انتخاب کنید.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.fa.png)

1. حساب ذخیره‌سازی مرتبط با فضای کاری Azure Machine Learning که ایجاد کرده‌اید را انتخاب کنید. برای مثال، *finetunephistorage*.

1. برای رفتن به صفحه افزودن تخصیص نقش، مراحل زیر را انجام دهید:

    - به حساب ذخیره‌سازی Azure که ایجاد کرده‌اید بروید.
    - از تب سمت چپ، **Access Control (IAM)** را انتخاب کنید.
    - از منوی ناوبری، **+ Add** را انتخاب کنید.
    - سپس **Add role assignment** را انتخاب کنید.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.fa.png)

1. در صفحه افزودن تخصیص نقش، موارد زیر را انجام دهید:

    - در صفحه نقش (Role)، عبارت *Storage Blob Data Reader* را در **نوار جستجو** وارد کرده و از گزینه‌های ظاهر شده **Storage Blob Data Reader** را انتخاب کنید.
    - روی **Next** کلیک کنید.
    - در صفحه اعضا (Members)، گزینه **Assign access to** را روی **Managed identity** تنظیم کنید.
    - روی **+ Select members** کلیک کنید.
    - در صفحه انتخاب Managed Identity، اشتراک Azure خود را انتخاب کنید.
    - Managed identity مورد نظر را انتخاب کنید.
    - Managed Identity که ایجاد کرده‌اید را انتخاب کنید. برای مثال، *finetunephi-managedidentity*.
    - روی **Select** کلیک کنید.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.fa.png)

1. روی **Review + assign** کلیک کنید.

#### افزودن تخصیص نقش AcrPull به Managed Identity

1. در **نوار جستجو** بالای صفحه پرتال، عبارت *container registries* را تایپ کرده و از گزینه‌های ظاهر شده **Container registries** را انتخاب کنید.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.fa.png)

1. مخزن کانتینری که مرتبط با فضای کاری Azure Machine Learning است را انتخاب کنید. برای مثال، *finetunephicontainerregistry*.

1. برای رفتن به صفحه افزودن تخصیص نقش، مراحل زیر را انجام دهید:

    - از تب سمت چپ، **Access Control (IAM)** را انتخاب کنید.
    - از منوی ناوبری، **+ Add** را انتخاب کنید.
    - سپس **Add role assignment** را انتخاب کنید.

1. در صفحه افزودن تخصیص نقش، موارد زیر را انجام دهید:

    - در صفحه نقش (Role)، عبارت *AcrPull* را در **نوار جستجو** وارد کرده و از گزینه‌های ظاهر شده **AcrPull** را انتخاب کنید.
    - روی **Next** کلیک کنید.
    - در صفحه اعضا (Members)، گزینه **Assign access to** را روی **Managed identity** تنظیم کنید.
    - روی **+ Select members** کلیک کنید.
    - اشتراک Azure خود را انتخاب کنید.
    - Managed identity مورد نظر را انتخاب کنید.
    - Managed Identity که ایجاد کرده‌اید را انتخاب کنید. برای مثال، *finetunephi-managedidentity*.
    - روی **Select** کلیک کنید.
    - روی **Review + assign** کلیک کنید.

### راه‌اندازی پروژه

برای دانلود مجموعه داده‌های مورد نیاز برای تنظیم دقیق، باید یک محیط محلی راه‌اندازی کنید.

در این تمرین، شما:

- یک پوشه برای کار ایجاد می‌کنید.
- یک محیط مجازی ایجاد می‌کنید.
- بسته‌های مورد نیاز را نصب می‌کنید.
- یک فایل *download_dataset.py* برای دانلود مجموعه داده ایجاد می‌کنید.

#### ایجاد پوشه‌ای برای کار

1. یک پنجره ترمینال باز کنید و دستور زیر را برای ایجاد پوشه‌ای به نام *finetune-phi* در مسیر پیش‌فرض وارد کنید.

    ```console
    mkdir finetune-phi
    ```

2. دستور زیر را در ترمینال وارد کنید تا به پوشه *finetune-phi* که ایجاد کرده‌اید بروید.

    ```console
    cd finetune-phi
    ```

#### ایجاد محیط مجازی

1. دستور زیر را در ترمینال وارد کنید تا محیط مجازی‌ای به نام *.venv* ایجاد شود.

    ```console
    python -m venv .venv
    ```

2. دستور زیر را برای فعال‌سازی محیط مجازی وارد کنید.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> اگر موفق بود، باید *(.venv)* قبل از خط فرمان نمایش داده شود.

#### نصب بسته‌های مورد نیاز

1. دستورات زیر را در ترمینال وارد کنید تا بسته‌های مورد نیاز نصب شوند.

    ```console
    pip install datasets==2.19.1
    ```

#### ایجاد `download_dataset.py`

> [!NOTE]
> ساختار کامل پوشه:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** را باز کنید.

1. از نوار منو، **File** را انتخاب کنید.

1. گزینه **Open Folder** را انتخاب کنید.

1. پوشه *finetune-phi* که ایجاد کرده‌اید را انتخاب کنید، که معمولاً در مسیر *C:\Users\yourUserName\finetune-phi* قرار دارد.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.fa.png)

1. در پنل سمت چپ Visual Studio Code، راست‌کلیک کرده و **New File** را انتخاب کنید تا فایل جدیدی به نام *download_dataset.py* ایجاد شود.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.fa.png)

### آماده‌سازی مجموعه داده برای تنظیم دقیق

در این تمرین، فایل *download_dataset.py* را اجرا می‌کنید تا مجموعه داده‌های *ultrachat_200k* را به محیط محلی خود دانلود کنید. سپس از این مجموعه داده‌ها برای تنظیم دقیق مدل Phi-3 در Azure Machine Learning استفاده خواهید کرد.

در این تمرین، شما:

- کد لازم را به فایل *download_dataset.py* اضافه می‌کنید تا مجموعه داده‌ها دانلود شوند.
- فایل *download_dataset.py* را اجرا می‌کنید تا مجموعه داده‌ها به محیط محلی شما منتقل شوند.

#### دانلود مجموعه داده با استفاده از *download_dataset.py*

1. فایل *download_dataset.py* را در Visual Studio Code باز کنید.

1. کد زیر را در فایل *download_dataset.py* وارد کنید.

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

1. دستور زیر را در ترمینال وارد کنید تا اسکریپت اجرا شده و مجموعه داده به محیط محلی شما دانلود شود.

    ```console
    python download_dataset.py
    ```

1. مطمئن شوید که مجموعه داده‌ها با موفقیت در دایرکتوری محلی *finetune-phi/data* ذخیره شده‌اند.

> [!NOTE]
>
> #### نکته درباره حجم مجموعه داده و زمان تنظیم دقیق
>
> در این آموزش، تنها از ۱٪ مجموعه داده استفاده می‌کنید (`split='train[:1%]'`). این کار حجم داده‌ها را به طور قابل توجهی کاهش می‌دهد و سرعت آپلود و فرآیند تنظیم دقیق را افزایش می‌دهد. می‌توانید درصد را تنظیم کنید تا تعادل مناسبی بین زمان آموزش و عملکرد مدل پیدا کنید. استفاده از زیرمجموعه کوچکتر از داده‌ها، زمان مورد نیاز برای تنظیم دقیق را کاهش می‌دهد و این فرآیند را برای آموزش قابل مدیریت‌تر می‌کند.

## سناریو ۲: تنظیم دقیق مدل Phi-3 و استقرار در Azure Machine Learning Studio

### تنظیم دقیق مدل Phi-3

در این تمرین، مدل Phi-3 را در Azure Machine Learning Studio تنظیم دقیق خواهید کرد.

در این تمرین، شما:

- خوشه کامپیوتری برای تنظیم دقیق ایجاد می‌کنید.
- مدل Phi-3 را در Azure Machine Learning Studio تنظیم دقیق می‌کنید.

#### ایجاد خوشه کامپیوتری برای تنظیم دقیق
۱. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

۱. از تب سمت چپ، **Compute** را انتخاب کنید.

۱. از منوی ناوبری، **Compute clusters** را انتخاب کنید.

۱. روی **+ New** کلیک کنید.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.fa.png)

۱. کارهای زیر را انجام دهید:

    - منطقه (**Region**) مورد نظر خود را انتخاب کنید.
    - سطح ماشین مجازی (**Virtual machine tier**) را روی **Dedicated** تنظیم کنید.
    - نوع ماشین مجازی (**Virtual machine type**) را روی **GPU** تنظیم کنید.
    - فیلتر اندازه ماشین مجازی (**Virtual machine size**) را روی **Select from all options** تنظیم کنید.
    - اندازه ماشین مجازی (**Virtual machine size**) را روی **Standard_NC24ads_A100_v4** انتخاب کنید.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.fa.png)

۱. روی **Next** کلیک کنید.

۱. کارهای زیر را انجام دهید:

    - نام کامپیوتر (**Compute name**) را وارد کنید. باید یکتا باشد.
    - حداقل تعداد نودها (**Minimum number of nodes**) را روی **0** تنظیم کنید.
    - حداکثر تعداد نودها (**Maximum number of nodes**) را روی **1** تنظیم کنید.
    - زمان بیکاری قبل از کاهش مقیاس (**Idle seconds before scale down**) را روی **120** تنظیم کنید.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.fa.png)

۱. روی **Create** کلیک کنید.

#### تنظیم دقیق مدل Phi-3

۱. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

۱. فضای کاری Azure Machine Learning که ایجاد کرده‌اید را انتخاب کنید.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.fa.png)

۱. کارهای زیر را انجام دهید:

    - از تب سمت چپ، **Model catalog** را انتخاب کنید.
    - عبارت *phi-3-mini-4k* را در **نوار جستجو** تایپ کرده و گزینه **Phi-3-mini-4k-instruct** را انتخاب کنید.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.fa.png)

۱. از منوی ناوبری، **Fine-tune** را انتخاب کنید.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.fa.png)

۱. کارهای زیر را انجام دهید:

    - نوع کار (**Select task type**) را روی **Chat completion** تنظیم کنید.
    - روی **+ Select data** کلیک کرده و **داده‌های آموزش** را بارگذاری کنید.
    - نوع بارگذاری داده‌های اعتبارسنجی (**Validation data upload type**) را روی **Provide different validation data** تنظیم کنید.
    - روی **+ Select data** کلیک کرده و **داده‌های اعتبارسنجی** را بارگذاری کنید.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.fa.png)

    > [!TIP]
    >
    > می‌توانید با انتخاب **Advanced settings**، تنظیماتی مانند **learning_rate** و **lr_scheduler_type** را به دلخواه تغییر دهید تا فرایند تنظیم دقیق بهینه شود.

۱. روی **Finish** کلیک کنید.

۱. در این تمرین، مدل Phi-3 را با موفقیت با استفاده از Azure Machine Learning تنظیم دقیق کردید. توجه داشته باشید که فرایند تنظیم دقیق ممکن است زمان قابل توجهی طول بکشد. پس از اجرای کار تنظیم دقیق، باید منتظر بمانید تا تکمیل شود. می‌توانید وضعیت کار تنظیم دقیق را با مراجعه به تب Jobs در سمت چپ فضای کاری Azure Machine Learning خود پیگیری کنید. در سری بعدی، مدل تنظیم شده را مستقر کرده و آن را با Prompt flow یکپارچه خواهید کرد.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.fa.png)

### استقرار مدل Phi-3 تنظیم شده

برای ادغام مدل Phi-3 تنظیم شده با Prompt flow، باید مدل را مستقر کنید تا برای استنتاج در زمان واقعی قابل دسترسی باشد. این فرایند شامل ثبت مدل، ایجاد یک نقطه انتهایی آنلاین و استقرار مدل است.

در این تمرین، شما:

- مدل تنظیم شده را در فضای کاری Azure Machine Learning ثبت می‌کنید.
- یک نقطه انتهایی آنلاین ایجاد می‌کنید.
- مدل Phi-3 تنظیم شده ثبت شده را مستقر می‌کنید.

#### ثبت مدل تنظیم شده

۱. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

۱. فضای کاری Azure Machine Learning که ایجاد کرده‌اید را انتخاب کنید.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.fa.png)

۱. از تب سمت چپ، **Models** را انتخاب کنید.
۱. روی **+ Register** کلیک کنید.
۱. گزینه **From a job output** را انتخاب کنید.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.fa.png)

۱. کاری که ایجاد کرده‌اید را انتخاب کنید.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.fa.png)

۱. روی **Next** کلیک کنید.

۱. نوع مدل (**Model type**) را روی **MLflow** تنظیم کنید.

۱. اطمینان حاصل کنید که **Job output** انتخاب شده است؛ این گزینه به صورت خودکار انتخاب می‌شود.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.fa.png)

۲. روی **Next** کلیک کنید.

۳. روی **Register** کلیک کنید.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.fa.png)

۴. می‌توانید مدل ثبت شده خود را با مراجعه به منوی **Models** در تب سمت چپ مشاهده کنید.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.fa.png)

#### استقرار مدل تنظیم شده

۱. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید مراجعه کنید.

۱. از تب سمت چپ، **Endpoints** را انتخاب کنید.

۱. از منوی ناوبری، **Real-time endpoints** را انتخاب کنید.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.fa.png)

۱. روی **Create** کلیک کنید.

۱. مدل ثبت شده‌ای که ایجاد کرده‌اید را انتخاب کنید.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.fa.png)

۱. روی **Select** کلیک کنید.

۱. کارهای زیر را انجام دهید:

    - ماشین مجازی (**Virtual machine**) را روی *Standard_NC6s_v3* تنظیم کنید.
    - تعداد نمونه‌ها (**Instance count**) مورد نظر خود را انتخاب کنید؛ مثلاً *1*.
    - نقطه انتهایی (**Endpoint**) را روی **New** تنظیم کنید تا یک نقطه انتهایی جدید ایجاد شود.
    - نام نقطه انتهایی (**Endpoint name**) را وارد کنید. باید یکتا باشد.
    - نام استقرار (**Deployment name**) را وارد کنید. باید یکتا باشد.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.fa.png)

۱. روی **Deploy** کلیک کنید.

> [!WARNING]
> برای جلوگیری از هزینه‌های اضافی در حساب خود، حتماً نقطه انتهایی ایجاد شده را در فضای کاری Azure Machine Learning حذف کنید.
>

#### بررسی وضعیت استقرار در فضای کاری Azure Machine Learning

۱. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید مراجعه کنید.

۱. از تب سمت چپ، **Endpoints** را انتخاب کنید.

۱. نقطه انتهایی که ایجاد کرده‌اید را انتخاب کنید.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.fa.png)

۱. در این صفحه می‌توانید نقطه‌های انتهایی را در طول فرایند استقرار مدیریت کنید.

> [!NOTE]
> پس از اتمام استقرار، مطمئن شوید که **Live traffic** روی **100%** تنظیم شده است. اگر اینطور نیست، روی **Update traffic** کلیک کنید تا تنظیمات ترافیک را اصلاح کنید. توجه داشته باشید که اگر ترافیک روی ۰٪ باشد، نمی‌توانید مدل را تست کنید.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.fa.png)
>

## سناریو ۳: ادغام با Prompt flow و گفتگو با مدل سفارشی شما در Azure AI Foundry

### ادغام مدل سفارشی Phi-3 با Prompt flow

پس از استقرار موفق مدل تنظیم شده، اکنون می‌توانید آن را با Prompt Flow ادغام کنید تا از مدل خود در برنامه‌های زمان واقعی استفاده کنید و انواع وظایف تعاملی را با مدل سفارشی Phi-3 خود انجام دهید.

در این تمرین، شما:

- ایجاد Azure AI Foundry Hub.
- ایجاد پروژه Azure AI Foundry.
- ایجاد Prompt flow.
- افزودن اتصال سفارشی برای مدل Phi-3 تنظیم شده.
- راه‌اندازی Prompt flow برای گفتگو با مدل سفارشی Phi-3 خود.

> [!NOTE]
> همچنین می‌توانید با استفاده از Azure ML Studio با Promptflow ادغام شوید. همان فرایند ادغام را می‌توان در Azure ML Studio نیز به کار برد.

#### ایجاد Azure AI Foundry Hub

قبل از ایجاد پروژه، باید یک Hub بسازید. Hub مانند یک Resource Group عمل می‌کند و به شما امکان می‌دهد چندین پروژه را در Azure AI Foundry سازماندهی و مدیریت کنید.

۱. به [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) مراجعه کنید.

۱. از تب سمت چپ، **All hubs** را انتخاب کنید.

۱. از منوی ناوبری، روی **+ New hub** کلیک کنید.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.fa.png)

۱. کارهای زیر را انجام دهید:

    - نام هاب (**Hub name**) را وارد کنید. باید یکتا باشد.
    - اشتراک Azure خود را انتخاب کنید.
    - گروه منابع (**Resource group**) مورد نظر را انتخاب کنید (در صورت نیاز یک گروه جدید ایجاد کنید).
    - منطقه (**Location**) مورد نظر خود را انتخاب کنید.
    - سرویس‌های Azure AI مورد اتصال را انتخاب کنید (در صورت نیاز یک اتصال جدید ایجاد کنید).
    - اتصال Azure AI Search را روی **Skip connecting** تنظیم کنید.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.fa.png)

۱. روی **Next** کلیک کنید.

#### ایجاد پروژه Azure AI Foundry

۱. در هاب ایجاد شده، از تب سمت چپ، **All projects** را انتخاب کنید.

۱. از منوی ناوبری، روی **+ New project** کلیک کنید.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.fa.png)

۱. نام پروژه (**Project name**) را وارد کنید. باید یکتا باشد.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.fa.png)

۱. روی **Create a project** کلیک کنید.

#### افزودن اتصال سفارشی برای مدل Phi-3 تنظیم شده

برای ادغام مدل سفارشی Phi-3 با Prompt flow، باید نقطه انتهایی و کلید مدل را در یک اتصال سفارشی ذخیره کنید. این تنظیم دسترسی به مدل سفارشی Phi-3 شما در Prompt flow را ممکن می‌سازد.

#### تنظیم api key و آدرس endpoint مدل Phi-3 تنظیم شده

۱. به [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) مراجعه کنید.

۱. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.

۱. از تب سمت چپ، **Endpoints** را انتخاب کنید.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.fa.png)

۱. نقطه انتهایی که ایجاد کرده‌اید را انتخاب کنید.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.fa.png)

۱. از منوی ناوبری، **Consume** را انتخاب کنید.

۱. **REST endpoint** و **Primary key** خود را کپی کنید.
![کپی کلید API و آدرس endpoint.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.fa.png)

#### افزودن اتصال سفارشی

1. به [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) مراجعه کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

1. در پروژه‌ای که ایجاد کرده‌اید، از تب سمت چپ **Settings** را انتخاب کنید.

1. گزینه **+ New connection** را انتخاب کنید.

    ![انتخاب اتصال جدید.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.fa.png)

1. از منوی ناوبری، **Custom keys** را انتخاب کنید.

    ![انتخاب کلیدهای سفارشی.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.fa.png)

1. کارهای زیر را انجام دهید:

    - گزینه **+ Add key value pairs** را انتخاب کنید.
    - برای نام کلید، **endpoint** را وارد کنید و آدرس endpoint که از Azure ML Studio کپی کرده‌اید را در فیلد مقدار بچسبانید.
    - دوباره **+ Add key value pairs** را انتخاب کنید.
    - برای نام کلید، **key** را وارد کنید و کلیدی که از Azure ML Studio کپی کرده‌اید را در فیلد مقدار بچسبانید.
    - پس از افزودن کلیدها، گزینه **is secret** را فعال کنید تا کلیدها مخفی بمانند و نمایش داده نشوند.

    ![افزودن اتصال.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.fa.png)

1. گزینه **Add connection** را انتخاب کنید.

#### ایجاد Prompt flow

شما یک اتصال سفارشی در Azure AI Foundry اضافه کرده‌اید. حالا بیایید با مراحل زیر یک Prompt flow ایجاد کنیم. سپس این Prompt flow را به اتصال سفارشی متصل می‌کنید تا بتوانید از مدل فاین‌تیون‌شده در داخل Prompt flow استفاده کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

1. از تب سمت چپ، **Prompt flow** را انتخاب کنید.

1. از منوی ناوبری، **+ Create** را انتخاب کنید.

    ![انتخاب Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.fa.png)

1. از منوی ناوبری، **Chat flow** را انتخاب کنید.

    ![انتخاب chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.fa.png)

1. نام پوشه‌ای که می‌خواهید استفاده کنید را وارد کنید.

    ![وارد کردن نام.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.fa.png)

2. گزینه **Create** را انتخاب کنید.

#### تنظیم Prompt flow برای چت با مدل سفارشی Phi-3 شما

شما باید مدل فاین‌تیون‌شده Phi-3 را در یک Prompt flow ادغام کنید. با این حال، Prompt flow موجود برای این منظور طراحی نشده است. بنابراین باید Prompt flow را بازطراحی کنید تا بتوانید مدل سفارشی را در آن بگنجانید.

1. در Prompt flow، کارهای زیر را برای بازسازی جریان موجود انجام دهید:

    - گزینه **Raw file mode** را انتخاب کنید.
    - تمام کدهای موجود در فایل *flow.dag.yml* را حذف کنید.
    - کد زیر را در فایل *flow.dag.yml* اضافه کنید.

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

    - گزینه **Save** را انتخاب کنید.

    ![انتخاب حالت فایل خام.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.fa.png)

1. کد زیر را در فایل *integrate_with_promptflow.py* اضافه کنید تا مدل سفارشی Phi-3 را در Prompt flow استفاده کنید.

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

    ![چسباندن کد prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.fa.png)

> [!NOTE]
> برای اطلاعات دقیق‌تر درباره استفاده از Prompt flow در Azure AI Foundry، می‌توانید به [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) مراجعه کنید.

1. گزینه‌های **Chat input** و **Chat output** را انتخاب کنید تا چت با مدل شما فعال شود.

    ![ورودی و خروجی.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.fa.png)

1. حالا آماده‌اید تا با مدل سفارشی Phi-3 خود چت کنید. در تمرین بعدی، یاد می‌گیرید چگونه Prompt flow را راه‌اندازی کنید و از آن برای چت با مدل فاین‌تیون‌شده Phi-3 خود استفاده کنید.

> [!NOTE]
>
> جریان بازسازی‌شده باید مشابه تصویر زیر باشد:
>
> ![نمونه جریان.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.fa.png)
>

### چت با مدل سفارشی Phi-3 شما

حالا که مدل سفارشی Phi-3 خود را فاین‌تیون و در Prompt flow ادغام کرده‌اید، آماده‌اید تا با آن تعامل داشته باشید. این تمرین شما را در روند راه‌اندازی و شروع چت با مدل خود از طریق Prompt flow راهنمایی می‌کند. با دنبال کردن این مراحل، می‌توانید از قابلیت‌های مدل فاین‌تیون‌شده Phi-3 برای انجام وظایف و مکالمات مختلف به طور کامل بهره‌مند شوید.

- با مدل سفارشی Phi-3 خود از طریق Prompt flow چت کنید.

#### شروع Prompt flow

1. گزینه **Start compute sessions** را انتخاب کنید تا Prompt flow آغاز شود.

    ![شروع جلسه محاسباتی.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.fa.png)

1. گزینه **Validate and parse input** را انتخاب کنید تا پارامترها به‌روزرسانی شوند.

    ![اعتبارسنجی ورودی.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.fa.png)

1. مقدار **connection** را به اتصال سفارشی که ایجاد کرده‌اید انتخاب کنید. برای مثال، *connection*.

    ![اتصال.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.fa.png)

#### چت با مدل سفارشی شما

1. گزینه **Chat** را انتخاب کنید.

    ![انتخاب چت.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.fa.png)

1. اینجا یک نمونه از نتایج است: اکنون می‌توانید با مدل سفارشی Phi-3 خود چت کنید. توصیه می‌شود سوالات خود را بر اساس داده‌های استفاده شده برای فاین‌تیون مطرح کنید.

    ![چت با prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.fa.png)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ‌گونه سوءتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.