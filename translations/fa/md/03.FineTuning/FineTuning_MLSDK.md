## نحوه استفاده از مؤلفه‌های chat-completion از رجیستری سیستم Azure ML برای آموزش دقیق مدل

در این مثال، ما آموزش دقیق مدل Phi-3-mini-4k-instruct را برای تکمیل یک مکالمه بین دو نفر با استفاده از دیتاست ultrachat_200k انجام خواهیم داد.

![MLFineTune](../../../../translated_images/fa/MLFineTune.928d4c6b3767dd35.webp)

این مثال به شما نشان می‌دهد چگونه می‌توانید با استفاده از Azure ML SDK و پایتون آموزش دقیق را انجام داده و سپس مدل آموزش‌دیده را برای استنباط بلادرنگ به یک نقطه انتهایی آنلاین مستقر کنید.

### داده‌های آموزش

ما از دیتاست ultrachat_200k استفاده خواهیم کرد. این نسخه‌ای بسیار فیلتر شده از دیتاست UltraChat است که برای آموزش Zephyr-7B-β، یک مدل چت پیشرفته 7 میلیارد پارامتری، استفاده شده است.

### مدل

ما از مدل Phi-3-mini-4k-instruct برای نشان دادن نحوه انجام آموزش دقیق مدل برای کار چت‌-کامپلیشن استفاده خواهیم کرد. اگر این نوت‌بوک را از یک کارت مدل خاص باز کرده‌اید، به یاد داشته باشید نام مدل خاص را جایگزین کنید.

### وظایف

- انتخاب مدلی برای آموزش دقیق.
- انتخاب و بررسی داده‌های آموزش.
- پیکربندی کار آموزش دقیق.
- اجرای کار آموزش دقیق.
- بررسی متریک‌های آموزش و ارزیابی.
- ثبت مدل آموزش‌دیده.
- استقرار مدل آموزش‌دیده برای استنباط بلادرنگ.
- پاکسازی منابع.

## 1. تنظیم پیش‌نیازها

- نصب وابستگی‌ها
- اتصال به AzureML Workspace. اطلاعات بیشتر در راه‌اندازی احراز هویت SDK. مقادیر <WORKSPACE_NAME>، <RESOURCE_GROUP> و <SUBSCRIPTION_ID> را در ادامه جایگزین کنید.
- اتصال به رجیستری سیستم azureml
- تعیین نام اختیاری آزمایش
- بررسی یا ایجاد محاسبات.

> [!NOTE]
> نیازمندی‌ها: یک نود GPU می‌تواند چند کارت GPU داشته باشد. برای مثال، در یک نود Standard_NC24rs_v3 چهار کارت NVIDIA V100 GPU وجود دارد، و در Standard_NC12s_v3 دو کارت NVIDIA V100 GPU موجود است. برای این اطلاعات به مستندات مراجعه کنید. تعداد کارت‌های GPU در هر نود در پارامتر gpus_per_node زیر تنظیم شده است. تنظیم صحیح این مقدار استفاده کامل از تمام GPUهای نود را تضمین می‌کند. SKUهای پیشنهادی GPU compute را می‌توانید اینجا و اینجا پیدا کنید.

### کتابخانه‌های پایتون

وابستگی‌ها را با اجرای سلول زیر نصب کنید. این مرحله در صورت اجرای در محیط جدید غیرقابل حذف است.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### تعامل با Azure ML

1. این اسکریپت پایتون برای تعامل با سرویس Azure Machine Learning (Azure ML) استفاده می‌شود. بررسی عملکرد آن به شرح زیر است:

    - ماژول‌های لازم از پکیج‌های azure.ai.ml، azure.identity و azure.ai.ml.entities را وارد می‌کند. همچنین ماژول time را وارد می‌کند.

    - تلاش می‌کند با استفاده از DefaultAzureCredential() احراز هویت انجام دهد که تجربه احراز هویت ساده‌شده برای شروع سریع توسعه برنامه‌هایی است که در فضای ابری Azure اجرا می‌شوند. اگر ناموفق باشد، از InteractiveBrowserCredential() یعنی ورود تعاملی مرورگر استفاده می‌کند.

    - سپس سعی می‌کند با استفاده از متد from_config، یک نمونه MLClient بسازد که تنظیمات را از فایل پیکربندی پیش‌فرض (config.json) می‌خواند. اگر این ناموفق باشد، به صورت دستی نمونه MLClient را با ارائه subscription_id، resource_group_name و workspace_name می‌سازد.

    - یک نمونه دیگر از MLClient می‌سازد، این بار برای رجیستری Azure ML به نام "azureml". این رجیستری جایی است که مدل‌ها، خطوط لوله آموزش دقیق و محیط‌ها ذخیره شده‌اند.

    - نام آزمایش را "chat_completion_Phi-3-mini-4k-instruct" تنظیم می‌کند.

    - یک زمان‌بندی یکتا (timestamp) ایجاد می‌کند که با تبدیل زمان فعلی (ثانیه‌های گذشته از epoch به صورت عدد اعشاری) به عدد صحیح و سپس به رشته ایجاد می‌شود. این timestamp می‌تواند برای ایجاد نام‌ها و نسخه‌های یکتا استفاده شود.

    ```python
    # وارد کردن ماژول‌های لازم از Azure ML و Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # وارد کردن ماژول time
    
    # تلاش برای احراز هویت با استفاده از DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # اگر DefaultAzureCredential ناموفق بود، استفاده از InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # تلاش برای ایجاد نمونه‌ای از MLClient با استفاده از فایل پیکربندی پیش‌فرض
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # اگر این روش موفق نبود، ایجاد نمونه‌ای از MLClient با وارد کردن دستی جزئیات
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # ایجاد نمونه دیگری از MLClient برای رجیستری Azure ML با نام "azureml"
    # این رجیستری جایی است که مدل‌ها، خطوط لوله تنظیم دقیق و محیط‌ها ذخیره می‌شوند
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # تنظیم نام آزمایش
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # تولید یک نشان‌گر زمانی یکتا که می‌تواند برای نام‌ها و نسخه‌های نیازمند یکتایی استفاده شود
    timestamp = str(int(time.time()))
    ```

## 2. انتخاب یک مدل پایه برای آموزش دقیق

1. Phi-3-mini-4k-instruct یک مدل سبک با 3.8 میلیارد پارامتر، پیشرفته و متن باز است که بر پایه دیتاست‌های مدل Phi-2 ساخته شده است. این مدل متعلق به خانواده مدل‌های Phi-3 است و نسخه Mini آن در دو واریانت 4K و 128K ارائه می‌شود که طول زمینه (تعداد توکن‌ها) پشتیبانی شده را نشان می‌دهد. برای استفاده از آن، باید مدل را برای هدف خاص خود آموزش دقیق دهیم. می‌توانید این مدل‌ها را در کاتالوگ مدل‌ها در AzureML Studio مشاهده کنید و بر اساس کار چت-کامپلیشن فیلتر کنید. در این مثال، از مدل Phi-3-mini-4k-instruct استفاده شده است. اگر این نوت‌بوک را برای مدل متفاوتی باز کرده‌اید، نام و نسخه مدل را متناسباً جایگزین کنید.

> [!NOTE]
> شناسه مدل (model id) ویژگی مهم آن است. این شناسه به عنوان ورودی به کار آموزش دقیق داده می‌شود. همچنین این شناسه در صفحه جزئیات مدل در کاتالوگ مدل AzureML Studio در بخش Asset ID موجود است.

2. این اسکریپت پایتون با سرویس Azure Machine Learning (Azure ML) تعامل دارد. شرح عملکرد:

    - مقدار متغیر model_name را "Phi-3-mini-4k-instruct" قرار می‌دهد.

    - از متد get متعلق به ویژگی models شی registry_ml_client استفاده می‌کند تا آخرین نسخه مدل با نام مشخص شده را از رجیستری Azure ML دریافت کند. متد get با دو آرگومان فراخوانی می‌شود: نام مدل و لیبلی که می‌گوید آخرین نسخه مدل باید گرفته شود.

    - یک پیام در کنسول چاپ می‌کند که نام، نسخه و شناسه مدلی که برای آموزش دقیق استفاده خواهد شد را نشان می‌دهد. متد format روی رشته برای درج نام، نسخه و شناسه مدل به کار می‌رود. خصوصیات نام، نسخه و شناسه مدل از شی foundation_model خوانده می‌شوند.

    ```python
    # نام مدل را تنظیم کنید
    model_name = "Phi-3-mini-4k-instruct"
    
    # آخرین نسخه مدل را از رجیستری Azure ML دریافت کنید
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # نام مدل، نسخه و شناسه را چاپ کنید
    # این اطلاعات برای پیگیری و اشکال‌زدایی مفید است
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. ایجاد یک Compute برای استفاده در کار

کار آموزش دقیق فقط با GPU compute کار می‌کند. اندازه compute بستگی به بزرگی مدل دارد و معمولا انتخاب compute مناسب مشکل است. در این سلول، کاربر راهنمایی می‌شود تا compute مناسب را انتخاب کند.

> [!NOTE]
> محاسبات فهرست شده در زیر با پیکربندی بهینه‌شده کار می‌کنند. هر تغییر در پیکربندی ممکن است منجر به خطای کمبود حافظه CUDA شود. در چنین مواردی، سعی کنید compute را به اندازه بزرگتر ارتقا دهید.

> [!NOTE]
> هنگام انتخاب compute_cluster_size در زیر، مطمئن شوید که compute در گروه منبع شما در دسترس است. اگر یک compute خاص در دسترس نیست، می‌توانید درخواست دسترسی به منابع compute را بدهید.

### بررسی پشتیبانی مدل برای آموزش دقیق

1. این اسکریپت پایتون با یک مدل Azure Machine Learning (Azure ML) تعامل دارد. شرح کارکرد:

    - ماژول ast را وارد می‌کند که برای پردازش درخت‌های گرامر انتزاعی پایتون کاربرد دارد.

    - بررسی می‌کند آیا شی foundation_model (که نمایانگر مدل در Azure ML است) برچسب (tag) با نام finetune_compute_allow_list دارد یا خیر. برچسب‌ها در Azure ML جفت‌های کلید-مقدار هستند که برای فیلتر و مرتب‌سازی مدل‌ها استفاده می‌شوند.

    - اگر برچسب finetune_compute_allow_list موجود باشد، مقدار رشته‌ای آن را با ast.literal_eval به صورت امن به یک لیست پایتون تبدیل می‌کند و این لیست را به متغیر computes_allow_list اختصاص می‌دهد. سپس پیامی چاپ می‌کند که یک compute باید از این لیست ایجاد شود.

    - اگر برچسب finetune_compute_allow_list موجود نباشد، متغیر computes_allow_list را None قرار می‌دهد و پیامی مبنی بر اینکه این برچسب در برچسب‌های مدل وجود ندارد چاپ می‌کند.

    - خلاصه اینکه، این اسکریپت به دنبال برچسب مشخصی در متادیتای مدل می‌گردد، در صورت وجود مقدار آن را به لیست تبدیل کرده و بازخورد مناسب به کاربر می‌دهد.

    ```python
    # وارد کردن ماژول ast، که توابعی برای پردازش درخت‌های دستور زبان انتزاعی پایتون فراهم می‌کند
    import ast
    
    # بررسی اینکه آیا برچسب 'finetune_compute_allow_list' در برچسب‌های مدل وجود دارد
    if "finetune_compute_allow_list" in foundation_model.tags:
        # اگر برچسب وجود داشت، از ast.literal_eval برای تجزیه مطمئن مقدار برچسب (یک رشته) به یک لیست پایتون استفاده کنید
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # تبدیل رشته به لیست پایتون
        # چاپ پیغامی که نشان می‌دهد باید یک محاسبه از لیست ایجاد شود
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # اگر برچسب وجود نداشت، متغیر computes_allow_list را برابر None قرار دهید
        computes_allow_list = None
        # چاپ پیغامی که نشان می‌دهد برچسب 'finetune_compute_allow_list' بخشی از برچسب‌های مدل نیست
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### بررسی Compute Instance

1. این اسکریپت پایتون با سرویس Azure Machine Learning (Azure ML) تعامل دارد و چندین بررسی روی یک نمونه compute انجام می‌دهد. شرح عملکرد:

    - سعی می‌کند نمونه compute با نام ذخیره شده در compute_cluster را از فضای کاری Azure ML بازیابی کند. اگر وضعیت provisioning نمونه "failed" باشد، خطای ValueError ایجاد می‌کند.

    - بررسی می‌کند اگر computes_allow_list مقدار None نیست. اگر نیست، تمام اندازه‌های compute در لیست را به حروف کوچک تبدیل می‌کند و می‌بیند آیا اندازه نمونه compute فعلی در این لیست هست یا خیر. در غیر این صورت خطای ValueError ایجاد می‌کند.

    - اگر computes_allow_list مقدار None باشد، بررسی می‌کند آیا اندازه نمونه compute در لیستی از اندازه‌های VM GPU پشتیبانی نشده است یا خیر. اگر باشد، خطای ValueError ایجاد می‌کند.

    - لیستی از همه اندازه‌های compute موجود در فضای کاری بازیابی می‌کند. سپس روی این لیست تکرار می‌کند و برای هر اندازه compute چک می‌کند آیا نام آن با اندازه نمونه compute فعلی مطابقت دارد یا نه. اگر بله، تعداد کارت‌های GPU آن اندازه را بازیابی کرده و متغیر gpu_count_found را True قرار می‌دهد.

    - اگر gpu_count_found برابر True باشد، تعداد کارت‌های GPU در نمونه compute را چاپ می‌کند. اگر False باشد، خطای ValueError ایجاد می‌شود.

    - به طور خلاصه، این اسکریپت چندین بررسی روی نمونه compute در فضای کاری Azure ML انجام می‌دهد، از جمله بررسی وضعیت provisioning، تطبیق اندازه نمونه با لیست مجاز یا ممنوع، و تعداد کارت‌های GPU.

    
    ```python
    # پیام استثناء را چاپ کن
    print(e)
    # اگر اندازه محاسبه در فضای کاری موجود نبود، یک ValueError ایجاد کن
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # نمونه محاسبه را از فضای کاری Azure ML بازیابی کن
    compute = workspace_ml_client.compute.get(compute_cluster)
    # بررسی کن که وضعیت تامین نمونه محاسبه "failed" است یا نه
    if compute.provisioning_state.lower() == "failed":
        # اگر وضعیت تامین "failed" بود، یک ValueError ایجاد کن
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # بررسی کن که computes_allow_list برابر با None نباشد
    if computes_allow_list is not None:
        # تمام اندازه‌های محاسبه در computes_allow_list را به حروف کوچک تبدیل کن
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # بررسی کن که اندازه نمونه محاسبه در computes_allow_list_lower_case باشد
        if compute.size.lower() not in computes_allow_list_lower_case:
            # اگر اندازه نمونه محاسبه در computes_allow_list_lower_case نبود، یک ValueError ایجاد کن
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # یک لیست از اندازه‌های VM GPU پشتیبانی نشده تعریف کن
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # بررسی کن که اندازه نمونه محاسبه در unsupported_gpu_vm_list باشد
        if compute.size.lower() in unsupported_gpu_vm_list:
            # اگر اندازه نمونه محاسبه در unsupported_gpu_vm_list بود، یک ValueError ایجاد کن
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # یک علامت برای بررسی اینکه تعداد GPUهای نمونه محاسبه پیدا شده است را مقداردهی اولیه کن
    gpu_count_found = False
    # یک لیست از تمام اندازه‌های محاسبه موجود در فضای کاری دریافت کن
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # روی لیست اندازه‌های محاسبه موجود تکرار کن
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # بررسی کن که نام اندازه محاسبه با اندازه نمونه محاسبه مطابقت دارد یا نه
        if compute_sku.name.lower() == compute.size.lower():
            # اگر مطابقت داشت، تعداد GPUها برای آن اندازه محاسبه را بازیابی کن و gpu_count_found را True کن
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # اگر gpu_count_found برابر با True بود، تعداد GPUهای نمونه محاسبه را چاپ کن
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # اگر gpu_count_found برابر با False بود، یک ValueError ایجاد کن
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. انتخاب دیتاست برای آموزش دقیق مدل

1. ما از دیتاست ultrachat_200k استفاده می‌کنیم. دیتاست شامل چهار بخش است، مناسب برای آموزش دقیق نظارت‌شده (Supervised fine-tuning یا sft) و رتبه‌بندی تولید (generation ranking یا gen). تعداد نمونه‌ها در هر بخش به شرح زیر است:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. سلول‌های بعدی آماده‌سازی پایه داده برای آموزش دقیق را نشان می‌دهند:

### مشاهده چند سطر داده

برای اینکه نمونه به سرعت اجرا شود، فایل‌های train_sft و test_sft را با ۵٪ از سطرهای از پیش کاهش یافته ذخیره می‌کنیم. این به معنای دقت کمتر مدل آموزش‌دیده است، بنابراین نباید برای استفاده واقعی گذاشته شود.
اسکریپت download-dataset.py برای دانلود دیتاست ultrachat_200k و تبدیل آن به فرمتی قابل مصرف توسط مؤلفه آموزش دقیق استفاده می‌شود. همچنین چون دیتاست بزرگ است، ما فقط بخشی از آن را در اینجا داریم.

1. اجرای اسکریپت زیر فقط ۵٪ از داده‌ها را دانلود می‌کند. این درصد می‌تواند با تغییر پارامتر dataset_split_pc به مقدار دلخواه افزایش یابد.

> [!NOTE]
> برخی مدل‌های زبان کدهای زبانی متفاوتی دارند و بنابراین نام ستون‌های دیتاست باید این تفاوت را بازتاب دهد.

1. مثالی از شکل داده‌ها:

دیتاست چت-کامپلیشن به صورت فرمت parquet ذخیره شده و هر ورودی از اسکیمای زیر پیروی می‌کند:

    - این یک سند JSON (JavaScript Object Notation) است که یک فرمت متداول تبادل داده‌هاست. کد اجرایی نیست، بلکه روشی برای ذخیره و انتقال داده است. شرح ساختار:

    - "prompt": این کلید مقداری رشته‌ای دارد که نشان‌دهنده یک وظیفه یا سوال مطرح شده به دستیار هوش مصنوعی است.

    - "messages": این کلید آرایه‌ای از اشیاء است. هر شئ نشان‌دهنده پیامی در مکالمه بین کاربر و دستیار هوش مصنوعی است. هر پیام دارای دو کلید است:

    - "content": این کلید محتوای پیام را به صورت رشته نگه می‌دارد.
    - "role": این کلید نقش موجودیت فرستنده پیام را مشخص می‌کند، مانند "user" یا "assistant".
    - "prompt_id": این کلید شناسه منحصر به فردی برای prompt دارد.

1. در این سند JSON خاص، مکالمه‌ای نمایش داده شده که در آن کاربر از دستیار هوش مصنوعی می‌خواهد یک قهرمان داستان دیستوپیایی بسازد. دستیار پاسخ می‌دهد و سپس کاربر درخواست جزئیات بیشتری می‌کند. دستیار موافقت می‌کند جزئیات بیشتری بدهد. کل مکالمه به یک شناسه prompt خاص مرتبط است.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### دانلود داده‌ها

1. این اسکریپت پایتون برای دانلود یک دیتاست با استفاده از اسکریپت کمکی download-dataset.py استفاده می‌شود. شرح عملکرد:

    - ماژول os را وارد می‌کند، که روش‌های قابل حملی برای استفاده از امکانات سیستم‌عامل فراهم می‌کند.

    - از تابع os.system برای اجرای اسکریپت download-dataset.py در شل با آرگومان‌های خط فرمان مشخص استفاده می‌کند. آرگومان‌ها دیتاست مورد نظر (HuggingFaceH4/ultrachat_200k)، دایرکتوری دانلود (ultrachat_200k_dataset) و درصد تقسیم دیتاست (5) را مشخص می‌کنند. تابع os.system وضعیت خروجی دستور اجرا شده را برمی‌گرداند و در متغیر exit_status ذخیره می‌شود.

    - بررسی می‌کند اگر exit_status صفر نباشد. در سیستم‌های یونیکس، صفر معمولا یعنی دستور موفق بوده و هر مقدار دیگر خطاست. اگر exit_status صفر نباشد، Exception با پیامی درباره خطا در دانلود دیتاست ایجاد می‌کند.

    - خلاصه اینکه این اسکریپت دستوری برای دانلود دیتاست با اسکریپت کمکی اجرا می‌کند و در صورت شکست خطا ایجاد می‌کند.
    
    ```python
    # ماژول os را وارد کنید، که روشی برای استفاده از قابلیت‌های وابسته به سیستم‌عامل فراهم می‌کند
    import os
    
    # از تابع os.system استفاده کنید تا اسکریپت download-dataset.py را در پوسته با آرگومان‌های خط فرمان خاص اجرا کنید
    # آرگومان‌ها مجموعه داده‌ای که باید دانلود شود (HuggingFaceH4/ultrachat_200k)، دایرکتوری مقصد دانلود (ultrachat_200k_dataset) و درصدی از مجموعه داده که باید تقسیم شود (5) را مشخص می‌کنند
    # تابع os.system وضعیت خروجی فرمان اجرا شده را برمی‌گرداند؛ این وضعیت در متغیر exit_status ذخیره می‌شود
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # بررسی کنید که آیا exit_status برابر با 0 نیست
    # در سیستم‌عامل‌های شبیه یونیکس، وضعیت خروجی 0 معمولاً نشان‌دهنده موفقیت فرمان است، در حالی که هر عدد دیگری نشان‌دهنده خطا است
    # اگر exit_status برابر با 0 نبود، یک Exception با پیامی که نشان‌دهنده خطا در دانلود مجموعه داده است پرتاب کنید
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### بارگذاری داده‌ها در DataFrame

1. این اسکریپت پایتون یک فایل JSON Lines را در یک pandas DataFrame بارگذاری کرده و ۵ ردیف اول را نمایش می‌دهد. شرح کار:

    - کتابخانه pandas را وارد می‌کند که کتابخانه قدرتمند برای دستکاری و تحلیل داده‌ها است.

    - حداکثر عرض ستون برای نمایش pandas را به 0 تنظیم می‌کند. این یعنی متن کامل هر ستون در زمان چاپ DataFrame بدون کوتاه شدن نمایش داده می‌شود.
- این کد از تابع pd.read_json برای بارگذاری فایل train_sft.jsonl از پوشه ultrachat_200k_dataset به یک DataFrame استفاده می‌کند. آرگومان lines=True نشان می‌دهد که فایل در فرمت JSON Lines است، جایی که هر خط یک شیء JSON جداگانه است.

- از متد head برای نمایش ۵ ردیف اول DataFrame استفاده می‌کند. اگر تعداد ردیف‌های DataFrame کمتر از ۵ باشد، همه آنها نمایش داده می‌شوند.

- به طور خلاصه، این اسکریپت در حال بارگذاری یک فایل JSON Lines به یک DataFrame و نمایش ۵ ردیف اول با متن کامل ستون‌ها است.

    ```python
    # کتابخانه pandas را وارد کنید که یک کتابخانه قدرتمند برای دستکاری و تحلیل داده‌ها است
    import pandas as pd
    
    # حداکثر عرض ستون‌ها را برای گزینه‌های نمایش pandas روی ۰ تنظیم کنید
    # این به این معنی است که متن کامل هر ستون بدون کوتاه‌سازی هنگام چاپ DataFrame نمایش داده می‌شود
    pd.set_option("display.max_colwidth", 0)
    
    # از تابع pd.read_json برای بارگذاری فایل train_sft.jsonl از پوشه ultrachat_200k_dataset به یک DataFrame استفاده کنید
    # آرگومان lines=True نشان می‌دهد که فایل در فرمت JSON Lines است، که هر خط یک شیء JSON جداگانه است
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # از متد head برای نمایش ۵ ردیف اول DataFrame استفاده کنید
    # اگر DataFrame کمتر از ۵ ردیف داشته باشد، همه آن‌ها را نمایش می‌دهد
    df.head()
    ```

## ۵. ارسال کار آموزش دقیق با استفاده از مدل و داده‌ها به عنوان ورودی

ساختن کاری که از مؤلفه خط‌لوله چک‌کامپلشن استفاده می‌کند. درباره تمامی پارامترهای پشتیبانی شده برای آموزش دقیق بیشتر بدانید.

### تعریف پارامترهای آموزش دقیق

۱. پارامترهای آموزش دقیق می‌توانند به ۲ دسته تقسیم شوند - پارامترهای آموزش، پارامترهای بهینه‌سازی

۱. پارامترهای آموزش جنبه‌های آموزش را تعریف می‌کنند مانند -

- بهینه‌ساز و زمان‌بندی که باید استفاده شود
- متریک بهینه‌سازی آموزش دقیق
- تعداد گام‌های آموزش و اندازه دسته، و غیره
- پارامترهای بهینه‌سازی به بهینه‌سازی حافظه GPU و استفاده مؤثر از منابع محاسباتی کمک می‌کنند.

۱. در زیر چند مورد از پارامترهایی که به این دسته تعلق دارند آمده است. پارامترهای بهینه‌سازی برای هر مدل متفاوتند و همراه مدل بسته‌بندی شده‌اند تا این تفاوت‌ها را مدیریت کنند.

- فعال کردن deepspeed و LoRA
- فعال کردن آموزش با دقت مخلوط
- فعال کردن آموزش چند گره‌ای

> [!NOTE]
> آموزش دقیق نظارت شده ممکن است منجر به از دست دادن تطابق یا فراموشی فاجعه‌بار شود. پیشنهاد می‌کنیم این مشکل را بررسی کنید و بعد از آموزش دقیق یک مرحله تطابق اجرا کنید.

### پارامترهای آموزش دقیق

۱. این اسکریپت پایتون پارامترهایی برای آموزش دقیق یک مدل یادگیری ماشین تعیین می‌کند. در اینجا شرح آن آمده است:

- پارامترهای پیش‌فرض آموزش مانند تعداد دوره‌های آموزشی، اندازه دسته برای آموزش و ارزیابی، نرخ یادگیری و نوع زمان‌بند نرخ یادگیری را تنظیم می‌کند.

- پارامترهای پیش‌فرض بهینه‌سازی مانند اینکه آیا از Layer-wise Relevance Propagation (LoRa) و DeepSpeed استفاده شود و مرحله DeepSpeed را تنظیم می‌کند.

- پارامترهای آموزش و بهینه‌سازی را در یک دیکشنری به نام finetune_parameters ترکیب می‌کند.

- بررسی می‌کند که آیا foundation_model پارامترهای پیش‌فرض خاص مدلی دارد یا خیر. اگر دارد، پیام هشداری چاپ می‌کند و دیکشنری finetune_parameters را با مقادیر پیش‌فرض مدل به‌روزرسانی می‌کند. از تابع ast.literal_eval برای تبدیل این مقادیر از رشته به دیکشنری پایتون استفاده می‌شود.

- مجموعه نهایی پارامترهای آموزش دقیق که برای اجرا استفاده خواهند شد را چاپ می‌کند.

- به طور خلاصه، این اسکریپت پارامترهای آموزش دقیق یک مدل یادگیری ماشین را تنظیم و نمایش می‌دهد و امکان جایگزینی پارامترهای پیش‌فرض با پارامترهای خاص مدل را فراهم می‌کند.

    ```python
    # تنظیم پارامترهای پیش‌فرض آموزش مانند تعداد اپوک‌های آموزش، اندازه دسته‌ها برای آموزش و ارزیابی، نرخ یادگیری، و نوع زمان‌بندی نرخ یادگیری
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # تنظیم پارامترهای پیش‌فرض بهینه‌سازی مانند اینکه آیا Layer-wise Relevance Propagation (LoRa) و DeepSpeed اعمال شود و مرحله DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # ترکیب پارامترهای آموزش و بهینه‌سازی در یک دیکشنری واحد به نام finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # بررسی اینکه آیا مدل پایه (foundation_model) پارامترهای پیش‌فرض خاص مدل دارد
    # در صورت وجود، چاپ پیام هشدار و به‌روزرسانی دیکشنری finetune_parameters با این پارامترهای پیش‌فرض خاص مدل
    # تابع ast.literal_eval برای تبدیل پارامترهای پیش‌فرض خاص مدل از رشته به دیکشنری پایتون استفاده می‌شود
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # تبدیل رشته به دیکشنری پایتون
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # چاپ مجموعه نهایی پارامترهای فاین‌تیونینگ که برای اجرا استفاده خواهند شد
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### خط‌لوله آموزش

۱. این اسکریپت پایتون تابعی را برای تولید نام نمایشی خط‌لوله آموزش یادگیری ماشین تعریف کرده و سپس این تابع را برای ایجاد و چاپ نام نمایشی فراخوانی می‌کند. شرح عملکرد آن:

۱. تابع get_pipeline_display_name تعریف شده است. این تابع یک نام نمایشی بر اساس پارامترهای مختلف مربوط به خط‌لوله آموزش تولید می‌کند.

۱. درون تابع، اندازه کل دسته با ضرب اندازه دسته هر دستگاه، تعداد گام‌های انباشت گرادیان، تعداد GPU در هر گره و تعداد گره‌هایی که برای آموزش دقیق استفاده می‌شوند محاسبه می‌شود.

۱. سایر پارامترها مانند نوع زمان‌بند نرخ یادگیری، اینکه آیا DeepSpeed اعمال شده، مرحله DeepSpeed، اینکه Layer-wise Relevance Propagation (LoRa) اعمال شده، محدودیت تعداد نقاط چک مدل برای نگهداری و طول دنباله حداکثر بازیابی می‌شود.

۱. رشته‌ای ساخته می‌شود که شامل همه این پارامترهاست که با خط فاصله جدا شده‌اند. اگر DeepSpeed یا LoRa اعمال شده باشند، رشته شامل "ds" به دنبال آن مرحله DeepSpeed یا "lora" خواهد بود. در غیر این صورت "nods" یا "nolora" خواهد بود.

۱. تابع این رشته را برمی‌گرداند که به عنوان نام نمایشی خط‌لوله آموزش خدمت می‌کند.

۱. بعد از تعریف تابع، آن را فراخوانی می‌کند تا نام نمایشی ایجاد شود و سپس آن را چاپ می‌کند.

۱. به طور خلاصه، این اسکریپت نام نمایشی برای خط‌لوله آموزش یادگیری ماشین بر اساس پارامترهای مختلف ایجاد می‌کند و آن نام را چاپ می‌کند.

    ```python
    # تعریف یک تابع برای تولید یک نام نمایشی برای خط لوله آموزش
    def get_pipeline_display_name():
        # محاسبه اندازه کل بچ با ضرب اندازه بچ به ازای هر دستگاه، تعداد مراحل انباشت گرادیان، تعداد GPU ها به ازای هر نود و تعداد نودهای استفاده شده برای تنظیم دقیق
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # بازیابی نوع زمان‌بندی یادگیری
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # بازیابی اینکه آیا DeepSpeed اعمال شده است
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # بازیابی مرحله DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # اگر DeepSpeed اعمال شده باشد، در نام نمایشی "ds" به همراه مرحله DeepSpeed را درج کنید؛ در غیر این صورت، "nods" را درج کنید
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # بازیابی اینکه آیا لایه‌ای مربوط به پراکندگی ارتباط (LoRa) اعمال شده است
        lora = finetune_parameters.get("apply_lora", "false")
        # اگر LoRa اعمال شده باشد، "lora" را در نام نمایشی درج کنید؛ در غیر این صورت، "nolora" را درج کنید
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # بازیابی محدودیت تعداد چک‌پوینت‌های مدل برای نگهداری
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # بازیابی حداکثر طول دنباله
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # ساخت نام نمایشی با اتصال تمام این پارامترها با جداکننده خط تیره
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # فراخوانی تابع برای تولید نام نمایشی
    pipeline_display_name = get_pipeline_display_name()
    # چاپ نام نمایشی
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### پیکربندی خط‌لوله

این اسکریپت پایتون یک خط‌لوله یادگیری ماشین را با استفاده از Azure Machine Learning SDK تعریف و پیکربندی می‌کند. شرح آن به شرح زیر است:

۱. ماژول‌های لازم از Azure AI ML SDK وارد می‌شوند.

۱. یک مؤلفه خط‌لوله به نام "chat_completion_pipeline" از رجیستری فراخوانی می‌شود.

۱. با استفاده از دکوراتور `@pipeline` و تابع `create_pipeline`، یک شغل خط‌لوله تعریف می‌شود. نام خط‌لوله به `pipeline_display_name` تنظیم می‌شود.

۱. درون تابع `create_pipeline`، مؤلفه خط‌لوله فراخوانی شده با پارامترهای مختلفی مانند مسیر مدل، خوشه‌های محاسباتی برای مراحل مختلف، تقسیم‌بندی داده‌ها برای آموزش و آزمون، تعداد GPUهای استفاده شده برای آموزش دقیق و سایر پارامترهای آموزش دقیق مقداردهی می‌شود.

۱. خروجی شغل آموزش دقیق به خروجی شغل خط‌لوله نگاشت می‌شود، تا مدل آموزش‌دیده به راحتی ثبت شود که برای استقرار مدل به یک نقطه انتهایی آنلاین یا دسته‌ای لازم است.

۱. نمونه‌ای از خط‌لوله با فراخوانی تابع `create_pipeline` ساخته می‌شود.

۱. تنظیم `force_rerun` خط‌لوله به `True` تنظیم می‌شود، به این معنی که نتایج کش شده از شغل‌های قبلی استفاده نخواهد شد.

۱. تنظیم `continue_on_step_failure` خط‌لوله به `False` تنظیم می‌شود، به این معنی که خط‌لوله در صورت شکست هر مرحله متوقف خواهد شد.

۱. خلاصه اینکه این اسکریپت خط‌لوله یادگیری ماشین برای وظیفه چت تکمیل را با استفاده از Azure Machine Learning SDK تعریف و پیکربندی می‌کند.

    ```python
    # وارد کردن ماژول‌های لازم از Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # گرفتن مؤلفه خط لوله با نام "chat_completion_pipeline" از رجیستری
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # تعریف کار خط لوله با استفاده از دکوراتور @pipeline و تابع create_pipeline
    # نام خط لوله به pipeline_display_name تنظیم شده است
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # مقداردهی اولیه مؤلفه خط لوله گرفته شده با پارامترهای مختلف
        # این شامل مسیر مدل، خوشه‌های محاسباتی برای مراحل مختلف، تقسیم‌بندی‌های مجموعه داده برای آموزش و تست، تعداد GPUهای مورد استفاده برای تنظیم دقیق و سایر پارامترهای تنظیم دقیق است
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # نگاشت تقسیم‌بندی‌های مجموعه داده به پارامترها
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # تنظیمات آموزش
            number_of_gpu_to_use_finetuning=gpus_per_node,  # تنظیم شده به تعداد GPUهای موجود در محاسبات
            **finetune_parameters
        )
        return {
            # نگاشت خروجی کار تنظیم دقیق به خروجی کار خط لوله
            # این کار انجام شده تا بتوانیم مدل تنظیم شده دقیق را به‌راحتی ثبت کنیم
            # ثبت مدل برای استقرار مدل در نقطه انتهایی آنلاین یا دسته‌ای لازم است
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # ایجاد یک نمونه از خط لوله با فراخوانی تابع create_pipeline
    pipeline_object = create_pipeline()
    
    # از نتایج کش شده از کارهای قبلی استفاده نکنید
    pipeline_object.settings.force_rerun = True
    
    # مقدار continue on step failure را به False تنظیم کنید
    # این بدان معناست که خط لوله در صورت شکست هر مرحله متوقف خواهد شد
    pipeline_object.settings.continue_on_step_failure = False
    ```

### ارسال شغل

۱. این اسکریپت پایتون یک شغل خط‌لوله یادگیری ماشین را به یک فضای کاری Azure Machine Learning ارسال می‌کند و سپس منتظر اتمام شغل می‌ماند. شرح عملکرد آن:

- متد create_or_update از شی jobs در workspace_ml_client برای ارسال شغل خط‌لوله فراخوانی می‌شود. خط‌لوله‌ای که باید اجرا شود توسط pipeline_object مشخص شده است، و آزمایشی که زیر آن شغل اجرا می‌شود با experiment_name مشخص شده است.

- سپس متد stream از شی jobs در workspace_ml_client برای انتظار اتمام شغل خط‌لوله فراخوانی می‌شود. شغلی که باید انتظار کشیده شود توسط ویژگی name از pipeline_job مشخص شده است.

- خلاصه اینکه این اسکریپت یک شغل خط‌لوله یادگیری ماشین را به Azure Machine Learning workspace ارسال کرده و سپس منتظر اتمام آن می‌ماند.

    ```python
    # ارسال کار پایپلاین به فضای کاری Azure Machine Learning
    # پایپلاینی که باید اجرا شود توسط pipeline_object مشخص شده است
    # آزمایشی که کار تحت آن اجرا می‌شود توسط experiment_name مشخص شده است
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # منتظر بمانید تا کار پایپلاین تکمیل شود
    # کاری که باید منتظر آن بمانید توسط ویژگی name شیء pipeline_job مشخص شده است
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## ۶. ثبت مدل آموزش‌دیده دقیق در workspace

مدل را از خروجی شغل آموزش دقیق ثبت خواهیم کرد. این کار ردپای رابطه بین مدل آموزش‌دیده دقیق و شغل آموزش دقیق را پیگیری می‌کند. شغل آموزش دقیق، به نوبه خود، ردپای رابطه به مدل بنیاد، داده و کد آموزش را ثبت می‌کند.

### ثبت مدل یادگیری ماشین

۱. این اسکریپت پایتون مدلی را که در خط‌لوله یادگیری ماشین Azure آموزش دیده ثبت می‌کند. شرح آن:

- ماژول‌های لازم از Azure AI ML SDK وارد می‌شوند.

- چک می‌کند که آیا خروجی trained_model از شغل خط‌لوله در دسترس است با استفاده از متد get از شی jobs در workspace_ml_client و دسترسی به ویژگی outputs آن.

- مسیر به مدل آموزش‌دیده را با قالب‌بندی رشته‌ای با نام شغل خط‌لوله و نام خروجی ("trained_model") می‌سازد.

- نامی برای مدل آموزش‌دیده دقیق تعریف می‌کند که با اضافه کردن "-ultrachat-200k" به نام مدل اصلی و جایگزین کردن هر اسلش با خط تیره ساخته شده است.

- با ایجاد یک شی Model با پارامترهای گوناگون، مانند مسیر مدل، نوع مدل (مدل MLflow)، نام و نسخه مدل، و توضیح مدل برای ثبت آماده می‌شود.

- با فراخوانی متد create_or_update از شی models در workspace_ml_client با شی Model به عنوان آرگومان، مدل را ثبت می‌کند.

- مدل ثبت شده را چاپ می‌کند.

۱. به طور خلاصه، این اسکریپت مدلی را که در یک خط‌لوله یادگیری ماشین Azure آموزش دیده ثبت می‌کند.

    ```python
    # وارد کردن ماژول‌های لازم از Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # بررسی اینکه آیا خروجی `trained_model` از کار خط لوله در دسترس است
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # ساخت مسیر به مدل آموزش‌دیده شده با قالب‌بندی یک رشته شامل نام کار خط لوله و نام خروجی ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # تعریف نامی برای مدل تنظیم‌شده با اضافه کردن "-ultrachat-200k" به نام مدل اصلی و جایگزینی هر اسلش با خط تیره
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # آماده‌سازی برای ثبت مدل با ایجاد یک شی Model با پارامترهای مختلف
    # این‌ها شامل مسیر مدل، نوع مدل (مدل MLflow)، نام و نسخه مدل، و توضیحی درباره مدل هستند
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # استفاده از timestamp به عنوان نسخه برای جلوگیری از تضاد نسخه
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # ثبت مدل با فراخوانی متد create_or_update از شی models در workspace_ml_client با شی Model به عنوان آرگومان
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # چاپ مدل ثبت‌شده
    print("registered model: \n", registered_model)
    ```

## ۷. استقرار مدل آموزش‌دیده دقیق در نقطه انتهایی آنلاین

نقاط انتهایی آنلاین یک API REST دائمی ارائه می‌دهند که می‌توان برای ادغام با برنامه‌هایی که نیاز به استفاده از مدل دارند استفاده کرد.

### مدیریت نقطه انتهایی

۱. این اسکریپت پایتون نقطه انتهایی آنلاین مدیریت شده‌ای در Azure Machine Learning برای یک مدل ثبت شده ایجاد می‌کند. شرح آن:

- ماژول‌های لازم از Azure AI ML SDK وارد می‌شوند.

- نام منحصربه‌فردی برای نقطه انتهایی آنلاین با اضافه کردن یک timestamp به رشته "ultrachat-completion-" تعریف می‌کند.

- برای ایجاد نقطه انتهایی آنلاین، یک شی ManagedOnlineEndpoint با پارامترهای مختلف از جمله نام نقطه انتهایی، توضیح نقطه انتهایی و حالت احراز هویت ("key") می‌سازد.

- نقطه انتهایی آنلاین را با فراخوانی متد begin_create_or_update از workspace_ml_client با شی ManagedOnlineEndpoint ایجاد می‌کند و سپس با فراخوانی متد wait منتظر اتمام عملیات می‌ماند.

۱. خلاصه اینکه این اسکریپت یک نقطه انتهایی آنلاین مدیریت شده را در Azure Machine Learning برای یک مدل ثبت شده ایجاد می‌کند.

    ```python
    # وارد کردن ماژول‌های لازم از SDK هوش مصنوعی Azure AI ML
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # تعریف یک نام منحصر به فرد برای نقطه پایانی آنلاین با افزودن یک زمان‌بندی به رشته "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # آماده‌سازی برای ایجاد نقطه پایانی آنلاین با ایجاد یک شی ManagedOnlineEndpoint با پارامترهای مختلف
    # این موارد شامل نام نقطه پایانی، توضیحی در مورد نقطه پایانی، و حالت احراز هویت ("key") می‌شود
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ایجاد نقطه پایانی آنلاین با فراخوانی متد begin_create_or_update از workspace_ml_client با شی ManagedOnlineEndpoint به عنوان آرگومان
    # سپس صبر کنید تا عملیات ایجاد کامل شود با فراخوانی متد wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> در اینجا می‌توانید فهرست SKUهای پشتیبانی شده برای استقرار را مشاهده کنید - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### استقرار مدل یادگیری ماشین

۱. این اسکریپت پایتون مدلی ثبت شده را در یک نقطه انتهایی آنلاین مدیریت شده در Azure Machine Learning مستقر می‌کند. شرح آن:

- ماژول ast را وارد می‌کند، که توابعی برای پردازش درخت‌های گرامر انتزاعی پایتون فراهم می‌کند.

- نوع نمونه برای استقرار را به "Standard_NC6s_v3" تنظیم می‌کند.

- چک می‌کند که آیا برچسب inference_compute_allow_list در مدل بنیاد وجود دارد یا خیر. اگر وجود داشته باشد، مقدار برچسب را از رشته به لیست پایتون تبدیل کرده و به inference_computes_allow_list اختصاص می‌دهد. در غیر این صورت، مقدار آن را None تنظیم می‌کند.

- بررسی می‌کند که آیا نوع نمونه مشخص شده در لیست مجاز است یا خیر. اگر نباشد، پیامی چاپ می‌کند که از کاربر می‌خواهد نوع نمونه را از لیست مجاز انتخاب کند.

- برای ایجاد استقرار آماده می‌شود به وسیله ایجاد شی ManagedOnlineDeployment با پارامترهای مختلف شامل نام استقرار، نام نقطه انتهایی، شناسه مدل، نوع و تعداد نمونه، تنظیمات پروب زنده بودن (liveness probe) و تنظیمات درخواست.

- استقرار را با فراخوانی متد begin_create_or_update از workspace_ml_client با شی ManagedOnlineDeployment ایجاد می‌کند و سپس با فراخوانی متد wait منتظر اتمام عملیات می‌ماند.

- ترافیک نقطه انتهایی را طوری تنظیم می‌کند که ۱۰۰٪ ترافیک به استقرار "demo" هدایت شود.

- نقطه انتهایی را با فراخوانی متد begin_create_or_update با شیء نقطه انتهایی در workspace_ml_client به‌روزرسانی می‌کند و سپس با فراخوانی متد result منتظر اتمام عملیات به‌روزرسانی می‌ماند.

۱. خلاصه اینکه این اسکریپت مدلی ثبت شده را در یک نقطه انتهایی آنلاین مدیریت شده در Azure Machine Learning مستقر می‌کند.

    ```python
    # ماژول ast را وارد کنید که توابعی برای پردازش درخت‌های گرامر نحو انتزاعی پایتون فراهم می‌کند
    import ast
    
    # نوع نمونه را برای استقرار تنظیم کنید
    instance_type = "Standard_NC6s_v3"
    
    # بررسی کنید که برچسب `inference_compute_allow_list` در مدل بنیاد وجود دارد یا نه
    if "inference_compute_allow_list" in foundation_model.tags:
        # اگر وجود داشت، مقدار برچسب را از رشته به لیست پایتون تبدیل کرده و به `inference_computes_allow_list` اختصاص دهید
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # اگر نبود، `inference_computes_allow_list` را روی `None` تنظیم کنید
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # بررسی کنید که نوع نمونه مشخص شده در لیست مجاز وجود دارد یا خیر
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # برای ایجاد استقرار آماده شوید با ایجاد یک شیء `ManagedOnlineDeployment` با پارامترهای مختلف
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # استقرار را با فراخوانی متد `begin_create_or_update` در `workspace_ml_client` با شیء `ManagedOnlineDeployment` به عنوان آرگومان ایجاد کنید
    # سپس برای کامل شدن عملیات ایجاد با فراخوانی متد `wait` صبر کنید
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # ترافیک نقطه انتهایی را تنظیم کنید تا ۱۰۰٪ ترافیک را به استقرار "demo" هدایت کند
    endpoint.traffic = {"demo": 100}
    
    # نقطه انتهایی را با فراخوانی متد `begin_create_or_update` در `workspace_ml_client` با شیء `endpoint` به عنوان آرگومان به‌روزرسانی کنید
    # سپس برای تمام شدن عملیات به‌روزرسانی با فراخوانی متد `result` صبر کنید
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## ۸. آزمایش نقطه انتهایی با داده نمونه

داده نمونه‌ای از مجموعه داده تست استخراج کرده و برای استنتاج به نقطه انتهایی آنلاین ارسال می‌کنیم. سپس برچسب‌های امتیازدهی شده را در کنار برچسب‌های حقیقت زمینه‌ای نمایش خواهیم داد.

### خواندن نتایج

۱. این اسکریپت پایتون یک فایل JSON Lines را به DataFrame پاندا خوانده، نمونه‌ای تصادفی می‌گیرد و اندیس‌ها را بازنشانی می‌کند. شرح آن:

- فایل ./ultrachat_200k_dataset/test_gen.jsonl را به DataFrame پاندا می‌خواند. تابع read_json با آرگومان lines=True استفاده می‌شود چون فایل در فرمت JSON Lines است، جایی که هر خط یک شیء JSON جداگانه است.

- نمونه‌ای تصادفی به اندازه ۱ ردیف از DataFrame می‌گیرد. تابع sample با آرگومان n=1 برای تعیین تعداد ردیف‌های تصادفی استفاده می‌شود.

- اندیس DataFrame را با تابع reset_index با آرگومان drop=True بازنشانی می‌کند تا اندیس اصلی حذف و با اندیس‌های عدد صحیح پیش‌فرض جایگزین شود.

- با استفاده از تابع head و آرگومان ۲، دو ردیف اول DataFrame را نمایش می‌دهد. اما چون نمونه فقط یک ردیف است، تنها همان یک ردیف نمایش داده می‌شود.

۱. خلاصه اینکه این اسکریپت یک فایل JSON Lines را به DataFrame پاندا می‌خواند، نمونه‌ای تصادفی یک ردیف گرفته، اندیس را بازنشانی می‌کند و ردیف اول را نمایش می‌دهد.

    ```python
    # وارد کردن کتابخانه pandas
    import pandas as pd
    
    # خواندن فایل JSON Lines به نام './ultrachat_200k_dataset/test_gen.jsonl' به یک DataFrame از pandas
    # آرگومان 'lines=True' نشان می‌دهد که فایل در فرمت JSON Lines است، جایی که هر خط یک شیء JSON جداگانه است
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # گرفتن نمونه تصادفی ۱ سطر از DataFrame
    # آرگومان 'n=1' تعداد سطرهای تصادفی انتخاب شده را مشخص می‌کند
    test_df = test_df.sample(n=1)
    
    # بازنشانی شاخص DataFrame
    # آرگومان 'drop=True' نشان می‌دهد که شاخص اصلی حذف شده و با یک شاخص جدید با مقادیر عدد صحیح پیش‌فرض جایگزین شود
    # آرگومان 'inplace=True' نشان می‌دهد که DataFrame باید به صورت درجا (بدون ایجاد یک شیء جدید) تغییر یابد
    test_df.reset_index(drop=True, inplace=True)
    
    # نمایش دو سطر اول DataFrame
    # با این حال، چون DataFrame بعد از نمونه‌برداری فقط یک سطر دارد، این فقط آن یک سطر را نمایش می‌دهد
    test_df.head(2)
    ```

### ایجاد شیء JSON

۱. این اسکریپت پایتون شیء JSON با پارامترهای مشخصی ایجاد کرده و آن را در فایلی ذخیره می‌کند. شرح آن:

- ماژول json را وارد می‌کند که توابعی برای کار با داده‌های JSON فراهم می‌کند.
- این یک دیکشنری به نام parameters ایجاد می‌کند که کلیدها و مقادیری را نشان می‌دهد که پارامترهایی برای یک مدل یادگیری ماشین هستند. کلیدها "temperature"، "top_p"، "do_sample" و "max_new_tokens" هستند و مقادیر متناظر آن‌ها به ترتیب 0.6، 0.9، True و 200 است.

- یک دیکشنری دیگر به نام test_json ایجاد می‌کند که دو کلید دارد: "input_data" و "params". مقدار "input_data" یک دیکشنری دیگر است با کلیدهای "input_string" و "parameters". مقدار "input_string" یک لیست است که شامل اولین پیام از دیتافریم test_df می‌باشد. مقدار "parameters" همان دیکشنری parameters است که قبلاً ایجاد شده بود. مقدار "params" یک دیکشنری خالی است.

- یک فایل به نام sample_score.json را باز می‌کند

    ```python
    # وارد کردن ماژول json که توابعی برای کار با داده‌های JSON فراهم می‌کند
    import json
    
    # ایجاد یک دیکشنری `parameters` با کلیدها و مقادیری که پارامترهای مدل یادگیری ماشین را نشان می‌دهند
    # کلیدها "temperature"، "top_p"، "do_sample" و "max_new_tokens" هستند و مقادیر متناظر آن‌ها به ترتیب ۰.۶، ۰.۹، درست (True) و ۲۰۰ هستند
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # ایجاد دیکشنری دیگری به نام `test_json` با دو کلید: "input_data" و "params"
    # مقدار "input_data" یک دیکشنری دیگر با کلیدهای "input_string" و "parameters" است
    # مقدار "input_string" یک لیست حاوی اولین پیام از DataFrame به نام `test_df` است
    # مقدار "parameters" دیکشنری `parameters` است که قبلاً ایجاد شده بود
    # مقدار "params" یک دیکشنری خالی است
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # باز کردن فایلی به نام `sample_score.json` در مسیر `./ultrachat_200k_dataset` در حالت نوشتن
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # نوشتن دیکشنری `test_json` به فایل به فرمت JSON با استفاده از تابع `json.dump`
        json.dump(test_json, f)
    ```

### فراخوانی Endpoint

1. این اسکریپت پایتون، یک endpoint آنلاین در Azure Machine Learning را برای امتیازدهی به یک فایل JSON فراخوانی می‌کند. در اینجا شرح عملکرد آن آمده است:

   - متد invoke را از ویژگی online_endpoints شی workspace_ml_client فراخوانی می‌کند. این متد برای ارسال یک درخواست به یک endpoint آنلاین و دریافت پاسخ استفاده می‌شود.

   - نام endpoint و استقرار (deployment) را با آرگومان‌های endpoint_name و deployment_name مشخص می‌کند. در این مورد، نام endpoint در متغیر online_endpoint_name ذخیره شده است و نام استقرار "demo" است.

   - مسیر فایل JSON برای امتیازدهی را با آرگومان request_file مشخص می‌کند. در این مورد، فایل مسیر ./ultrachat_200k_dataset/sample_score.json است.

   - پاسخ دریافتی از endpoint را در متغیر response ذخیره می‌کند.

   - پاسخ خام را چاپ می‌کند.

1. در خلاصه، این اسکریپت یک endpoint آنلاین در Azure Machine Learning را برای امتیازدهی یک فایل JSON فراخوانی کرده و پاسخ را چاپ می‌کند.

    ```python
    # فراخوانی نقطه پایانی آنلاین در Azure Machine Learning برای ارزیابی فایل `sample_score.json`
    # روش `invoke` از ویژگی `online_endpoints` شیء `workspace_ml_client` برای ارسال درخواست به یک نقطه پایانی آنلاین و دریافت پاسخ استفاده می‌شود
    # آرگومان `endpoint_name` نام نقطه پایانی را مشخص می‌کند که در متغیر `online_endpoint_name` ذخیره شده است
    # آرگومان `deployment_name` نام استقرار را مشخص می‌کند، که "demo" است
    # آرگومان `request_file` مسیر فایل JSON برای ارزیابی را مشخص می‌کند، که `./ultrachat_200k_dataset/sample_score.json` است
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # چاپ پاسخ خام از نقطه پایانی
    print("raw response: \n", response, "\n")
    ```

## 9. حذف endpoint آنلاین

1. فراموش نکنید که endpoint آنلاین را حذف کنید، در غیر این صورت متر هزینه برای محاسبات استفاده شده توسط endpoint ادامه خواهد داشت. این خط کد پایتون در حال حذف یک endpoint آنلاین در Azure Machine Learning است. شرح عملکرد آن چنین است:

   - متد begin_delete را از ویژگی online_endpoints شی workspace_ml_client فراخوانی می‌کند. این متد برای شروع حذف یک endpoint آنلاین استفاده می‌شود.

   - نام endpoint که باید حذف شود را با آرگومان name مشخص می‌کند. در این مورد، نام endpoint در متغیر online_endpoint_name ذخیره شده است.

   - متد wait را فراخوانی می‌کند تا منتظر بماند عملیات حذف کامل شود. این یک عملیات مسدودکننده است، به این معنی که مانع ادامه اجرای اسکریپت تا پایان حذف می‌شود.

   - در خلاصه، این خط کد شروع حذف یک endpoint آنلاین در Azure Machine Learning را انجام داده و منتظر می‌ماند عملیات کامل شود.

    ```python
    # حذف نقطه پایانی آنلاین در Azure Machine Learning
    # متد `begin_delete` از خاصیت `online_endpoints` در شیء `workspace_ml_client` برای شروع حذف یک نقطه پایانی آنلاین استفاده می‌شود
    # آرگومان `name` نام نقطه پایانی که باید حذف شود را مشخص می‌کند که در متغیر `online_endpoint_name` ذخیره شده است
    # متد `wait` برای انتظار تا اتمام عملیات حذف فراخوانی می‌شود. این عملیات مسدودکننده است، به این معنی که مانع ادامه اجرای اسکریپت تا پایان حذف خواهد شد
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مادری خود منبع معتبر محسوب می‌شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئولیتی در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->