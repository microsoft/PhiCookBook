## Azure ML سسٹم رجسٹری سے چیٹ-کمپلیشن کمپونینٹس کو ماڈل کی فائن ٹیوننگ کے لیے کیسے استعمال کریں

اس مثال میں ہم Phi-3-mini-4k-instruct ماڈل کی فائن ٹیوننگ کریں گے تاکہ دو افراد کے درمیان گفتگو مکمل کی جا سکے جس کے لیے ultrachat_200k ڈیٹا سیٹ استعمال کیا جائے گا۔

![MLFineTune](../../../../translated_images/ur/MLFineTune.928d4c6b3767dd35.webp)

یہ مثال آپ کو دکھائے گی کہ Azure ML SDK اور Python استعمال کرتے ہوئے فائن ٹیوننگ کیسے کی جاتی ہے اور پھر فائن ٹیون کیا ہوا ماڈل ایک آن لائن اینڈپوائنٹ پر ریئل ٹائم انفرنس کے لیے تعینات کیسے کیا جاتا ہے۔

### تربیتی ڈیٹا

ہم ultrachat_200k ڈیٹا سیٹ استعمال کریں گے۔ یہ UltraChat ڈیٹا سیٹ کا بہت زیادہ فلٹر شدہ ورژن ہے اور Zephyr-7B-β، جو کہ جدید ترین 7b چیٹ ماڈل ہے، کی تربیت کے لیے استعمال ہوا تھا۔

### ماڈل

ہم Phi-3-mini-4k-instruct ماڈل استعمال کریں گے تاکہ دکھایا جا سکے کہ صارف کس طرح چیٹ-کمپلیشن ٹاسک کے لیے ماڈل کی فائن ٹیوننگ کر سکتا ہے۔ اگر آپ نے یہ نوٹ بک کسی مخصوص ماڈل کارڈ سے کھولی ہے تو مخصوص ماڈل نام کو تبدیل کرنا نہ بھولیں۔

### ٹاسک

- فائن ٹیون کے لیے ماڈل منتخب کریں۔
- تربیتی ڈیٹا منتخب کریں اور دریافت کریں۔
- فائن ٹیوننگ جاب کی ترتیب دیں۔
- فائن ٹیوننگ جاب چلائیں۔
- تربیتی اور تشخیصی میٹرکس کا جائزہ لیں۔
- فائن ٹیون کیا ہوا ماڈل رجسٹر کریں۔
- ریئل ٹائم انفرنس کے لیے فائن ٹیون ماڈل تعینات کریں۔
- وسائل کی صفائی کریں۔

## 1. پیشگی ضروریات کا سیٹ اپ کریں

- انحصار انسٹال کریں
- AzureML ورک اسپیس سے کنیکٹ کریں۔ سیٹ اپ SDK تصدیق کے بارے میں مزید معلومات حاصل کریں۔ نیچے <WORKSPACE_NAME>، <RESOURCE_GROUP> اور <SUBSCRIPTION_ID> کو تبدیل کریں۔
- azureml سسٹم رجسٹری سے کنیکٹ کریں۔
- ایک اختیاری تجربے کا نام سیٹ کریں۔
- کمپیوٹ کو چیک یا بنائیں۔

> [!NOTE]
> ضرورت ایک سنگل GPU نوڈ ہو سکتی ہے جس میں کئی GPU کارڈز موجود ہوں۔ مثال کے طور پر، Standard_NC24rs_v3 ایک نوڈ میں 4 NVIDIA V100 GPUs ہوتے ہیں جبکہ Standard_NC12s_v3 میں 2 NVIDIA V100 GPUs ہوتے ہیں۔ مزید معلومات کے لیے ڈاکیومنٹس دیکھیں۔ فی نوڈ GPU کارڈز کی تعداد gpus_per_node پیرامیٹر میں سیٹ کی جاتی ہے۔ اس کی درست ترتیب یقینی بنانا تمام GPUs کے استعمال کو یقینی بناتا ہے۔ تجویز کردہ GPU کمپیوٹ SKUs یہاں اور یہاں دیکھے جا سکتے ہیں۔

### Python لائبریریز

نیچے دیے گئے سیل کو چلا کر انحصار انسٹال کریں۔ اگر نیا ماحول چل رہے ہو تو یہ اختیاری قدم نہیں ہے۔

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML کے ساتھ بات چیت

1. یہ Python اسکرپٹ Azure Machine Learning (Azure ML) سروس کے ساتھ بات چیت کے لیے استعمال ہوتا ہے۔ اس کا خلاصہ درج ذیل ہے:

    - یہ azure.ai.ml، azure.identity، اور azure.ai.ml.entities پیکیجز سے ضروری ماڈیولز امپورٹ کرتا ہے۔ اس کے علاوہ time ماڈیول بھی شامل ہے۔

    - یہ DefaultAzureCredential() کے ذریعے توثیق کی کوشش کرتا ہے، جو Azure کلاؤڈ میں ایپلی کیشنز تیزی سے بنانے کے لیے آسان تصدیق کا تجربہ فراہم کرتا ہے۔ اگر یہ ناکام ہوتی ہے تو InteractiveBrowserCredential() کی طرف رجوع کرتا ہے، جو ایک انٹرایکٹو لاگ ان پرامپٹ فراہم کرتا ہے۔

    - پھر from_config طریقہ استعمال کرتے ہوئے MLClient انسٹینس بنانے کی کوشش کرتا ہے، جو ڈیفالٹ کنفیگریشن فائل (config.json) سے ترتیبات پڑھتا ہے۔ اگر یہ ناکام ہوتا ہے تو سبسکرپشن_آئی ڈی، ریسورس_گروپ_نام، اور ورک اسپیس_نام کو دستی طور پر فراہم کرتے ہوئے MLClient بناتا ہے۔

    - ایک اور MLClient انسٹینس بناتا ہے، اس بار Azure ML رجسٹری کے لیے جس کا نام "azureml" ہے۔ یہ رجسٹری وہاں ماڈلز، فائن-ٹیوننگ پائپ لائنز، اور اینوائرنمنٹس محفوظ کیے جاتے ہیں۔

    - experiment_name کو "chat_completion_Phi-3-mini-4k-instruct" پر سیٹ کرتا ہے۔

    - ایک منفرد ٹائم سٹمپ بناتا ہے جو موجودہ وقت (ایپوک سے سیکنڈ میں، فلوٹنگ پوائنٹ نمبر) کو انٹیجر میں تبدیل کر کے اسٹرنگ میں بدلتا ہے۔ یہ ٹائم سٹمپ منفرد نام اور ورژنز بنانے کے لیے استعمال کیا جا سکتا ہے۔

    ```python
    # Azure ML اور Azure Identity سے ضروری ماڈیولز درآمد کریں
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # وقت ماڈیول درآمد کریں
    
    # DefaultAzureCredential کا استعمال کرتے ہوئے توثیق کی کوشش کریں
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # اگر DefaultAzureCredential ناکام ہو جائے، تو InteractiveBrowserCredential استعمال کریں
        credential = InteractiveBrowserCredential()
    
    # ڈیفالٹ کنفیگریشن فائل کا استعمال کرتے ہوئے MLClient کا ایک نمونہ بنانے کی کوشش کریں
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # اگر وہ ناکام ہو، تو تفصیلات دستی طور پر فراہم کرکے MLClient کا ایک نمونہ بنائیں
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" نامی Azure ML رجسٹری کے لیے ایک اور MLClient کا نمونہ بنائیں
    # یہ رجسٹری وہ جگہ ہے جہاں ماڈلز، فائن ٹوننگ پائپ لائنز، اور ماحول ذخیرہ ہوتے ہیں
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # تجربے کا نام مقرر کریں
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # ایک منفرد ٹائم اسٹیمپ تیار کریں جو ناموں اور ورژنز کے لیے استعمال کیا جا سکتا ہے جو منفرد ہونا ضروری ہیں
    timestamp = str(int(time.time()))
    ```

## 2. فائن ٹیون کے لیے بنیادی ماڈل منتخب کریں

1. Phi-3-mini-4k-instruct ایک 3.8B پیرا میٹرز والا، ہلکا پھلکا، جدید ترین اوپن ماڈل ہے جو Phi-2 کے استعمال شدہ ڈیٹا سیٹس پر مبنی ہے۔ یہ ماڈل Phi-3 ماڈل فیملی سے تعلق رکھتا ہے، اور منی ورژن کے دو ورائینٹس ہوتے ہیں 4K اور 128K جو اس کی کانٹیکسٹ لمبائی (ٹوکنز میں) بتاتے ہیں۔ اسے خاص مقصد کے لیے فائن ٹیون کرنے کی ضرورت ہے تاکہ استعمال کیا جا سکے۔ آپ AzureML اسٹوڈیو میں ماڈل کیٹلاگ میں ان ماڈلز کو چیٹ-کمپلیشن ٹاسک فلٹر لگا کر براؤز کر سکتے ہیں۔ اس مثال میں ہم Phi-3-mini-4k-instruct ماڈل استعمال کر رہے ہیں۔ اگر آپ نے یہ نوٹ بک کسی مختلف ماڈل کے لیے کھولی ہے، تو ماڈل کا نام اور ورژن accordingly تبدیل کریں۔

> [!NOTE]
> ماڈل کا id پراپرٹی۔ اسے فائن ٹیوننگ جاب میں ان پٹ کے طور پر دیا جائے گا۔ یہ AzureML اسٹوڈیو ماڈل کیٹلاگ میں ماڈل کی تفصیلات کے Asset ID فیلڈ میں بھی دستیاب ہے۔

2. یہ Python اسکرپٹ Azure Machine Learning (Azure ML) سروس کے ساتھ بات چیت کر رہا ہے۔ خلاصہ درج ذیل ہے:

    - یہ model_name کو "Phi-3-mini-4k-instruct" سیٹ کرتا ہے۔

    - registry_ml_client آبجیکٹ کے models پراپرٹی کے get طریقہ کو استعمال کرتے ہوئے Azure ML رجسٹری سے نامزد ماڈل کے تازہ ترین ورژن کو حاصل کرتا ہے۔ get طریقہ دو دلیلوں کے ساتھ کال کیا جاتا ہے: ماڈل کا نام اور ایک لیبل جو بتاتا ہے کہ تازہ ترین ورژن لینا ہے۔

    - کنسول پر پیغام پرنٹ کرتا ہے جو بتاتا ہے کہ کون سا ماڈل، ورژن، اور id فائن ٹیوننگ کے لیے استعمال ہوگا۔ سٹرنگ کی format میتھڈ استعمال کر کے ماڈل کا نام، ورژن اور id پیغام میں شامل کیا جاتا ہے۔ یہ properties foundation_model آبجیکٹ سے حاصل کی جاتی ہیں۔

    ```python
    # ماڈل کا نام سیٹ کریں
    model_name = "Phi-3-mini-4k-instruct"
    
    # ماڈل کا تازہ ترین ورژن Azure ML رجسٹری سے حاصل کریں
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # ماڈل کا نام، ورژن، اور شناخت پرنٹ کریں
    # یہ معلومات ٹریکنگ اور ڈیبگنگ کے لیے مفید ہے
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. جاب کے لیے کمپیوٹ بنائیں

فائن ٹیون جاب صرف GPU کمپیوٹ کے ساتھ کام کرتا ہے۔ کمپیوٹ کا سائز ماڈل کی جسامت پر منحصر ہوتا ہے اور اکثر صحیح کمپیوٹ کا انتخاب مشکل ہو جاتا ہے۔ اس سیل میں، صارف کو جاب کے لیے مناسب کمپیوٹ منتخب کرنے کی رہنمائی دی جاتی ہے۔

> [!NOTE]
> نیچے دیے گئے کمپیوٹس سب سے زیادہ آپٹمائزڈ کنفیگریشن کے ساتھ کام کرتے ہیں۔ کسی بھی قسم کی تبدیلی CUDA Out Of Memory ایرر کا باعث بن سکتی ہے۔ ایسی صورت میں کمپیوٹ کو بڑے سائز میں اپ گریڈ کریں۔

> [!NOTE]
> کمپیوٹ کلستر سائز منتخب کرتے وقت یقینی بنائیں کہ کمپیوٹ آپ کے ریسورس گروپ میں دستیاب ہو۔ اگر کوئی خاص کمپیوٹ دستیاب نہیں ہے تو کمپیوٹ ریسورسز کی رسائی کے لیے درخواست دے سکتے ہیں۔

### فائن ٹیوننگ کی حمایت کے لیے ماڈل کی جانچ

1. یہ Python اسکرپٹ Azure ML ماڈل کے ساتھ بات چیت کر رہا ہے۔ خلاصہ درج ذیل ہے:

    - ast ماڈیول امپورٹ کرتا ہے، جو Python کے abstract syntax grammar کے درختوں کو پروسیس کرنے کے لیے فنکشنز فراہم کرتا ہے۔

    - چیک کرتا ہے کہ آیا foundation_model (جو Azure ML میں ایک ماڈل کی نمائندگی کرتا ہے) کے ٹیگز میں finetune_compute_allow_list نام کا ٹیگ موجود ہے۔ Azure ML میں ٹیگز key-value پیئرز ہوتے ہیں جنہیں ماڈلز کے فلٹر اور ترتیب کے لیے بنایا جا سکتا ہے۔

    - اگر finetune_compute_allow_list ٹیگ موجود ہے، تو ast.literal_eval کے ذریعے اس ٹیگ کی ویلیو (جو ایک سٹرنگ ہوتی ہے) کو محفوظ طریقے سے Python فہرست میں تبدیل کرتا ہے اور اسے computes_allow_list ویری ایبل میں محفوظ کرتا ہے۔ پھر یہ بتاتا ہے کہ کمپیوٹ کی لسٹ سے کمپیوٹ بنانا چاہیے۔

    - اگر ٹیگ موجود نہیں، تو computes_allow_list کو None سیٹ کرتا ہے اور بتاتا ہے کہ فائن ٹیون کمپیوٹ الاؤ لسٹ ماڈل کے ٹیگز کا حصہ نہیں ہے۔

    - خلاصہ یہ کہ یہ اسکرپٹ ماڈل کی میٹا ڈیٹا میں مخصوص ٹیگ کی موجودگی چیک کرتا ہے، موجود ہونے پر ٹیگ کی ویلیو کو فہرست میں تبدیل کرتا ہے، اور صارف کو فیڈبیک دیتا ہے۔

    ```python
    # Python کے مجرد نحو کے درختوں کو پروسیس کرنے کے لیے فنکشنز فراہم کرنے والا ast ماڈیول درآمد کریں
    import ast
    
    # چیک کریں کہ ماڈل کے ٹیگز میں 'finetune_compute_allow_list' ٹیگ موجود ہے یا نہیں
    if "finetune_compute_allow_list" in foundation_model.tags:
        # اگر ٹیگ موجود ہو تو ast.literal_eval کا استعمال کرتے ہوئے ٹیگ کی قیمت (ایک سٹرنگ) کو محفوظ طریقے سے Python کی فہرست میں تبدیل کریں
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # سٹرنگ کو Python کی فہرست میں تبدیل کریں
        # ایک پیغام پرنٹ کریں جو ظاہر کرے کہ فہرست سے کمپیوٹ بنایا جانا چاہیے
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # اگر ٹیگ موجود نہ ہو تو computes_allow_list کو None پر سیٹ کریں
        computes_allow_list = None
        # ایک پیغام پرنٹ کریں جو ظاہر کرے کہ 'finetune_compute_allow_list' ٹیگ ماڈل کے ٹیگز کا حصہ نہیں ہے
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### کمپیوٹ انسٹانس چیک کرنا

1. یہ Python اسکرپٹ Azure Machine Learning (Azure ML) سروس کے ساتھ بات چیت کرتا ہے اور کمپیوٹ انسٹانس پر کئی چیکس انجام دیتا ہے۔ خلاصہ درج ذیل ہے:

    - کوشش کرتا ہے کہ compute_cluster میں ذخیرہ شدہ نام کا کمپیوٹ انسٹانس Azure ML ورک اسپیس سے حاصل کرے۔ اگر کمپیوٹ کی provisioning state "failed" ہو تو ValueError پیدا کرتا ہے۔

    - چیک کرتا ہے اگر computes_allow_list None نہ ہو۔ اگر ایسا ہے تو فہرست میں موجود تمام کمپیوٹ سائزز کو لوئر کیس میں تبدیل کرتا ہے اور چیک کرتا ہے کہ موجودہ کمپیوٹ کا سائز اس فہرست میں ہو۔ اگر نہ ہو تو ValueError اٹھاتا ہے۔

    - اگر computes_allow_list None ہو، تو چیک کرتا ہے کہ کمپیوٹ کا سائز unsupported GPU VM سائزز کی فہرست میں نہ ہو۔ اگر ہو تو ValueError پھینکتا ہے۔

    - ورک اسپیس میں تمام دستیاب کمپیوٹ سائزز کی فہرست نکالتا ہے۔ پھر اس فہرست پر گردش کرتے ہوئے چیک کرتا ہے کہ کسی بھی کمپیوٹ سائز کا نام موجودہ کمپیوٹ کے سائز سے میل کھاتا ہے یا نہیں۔ اگر میل کھاتا ہے، تو اس کمپیوٹ سائز کے لیے GPU کی تعداد حاصل کرتا ہے اور gpu_count_found کو True کر دیتا ہے۔

    - اگر gpu_count_found True ہو تو کمپیوٹ انسٹانس میں GPU کی تعداد پرنٹ کرتا ہے۔ اگر False ہو تو ValueError پھینکتا ہے۔

    - خلاصہ یہ کہ یہ اسکرپٹ Azure ML ورک اسپیس میں کمپیوٹ انسٹانس کی متعدد جانچیں کرتا ہے، بشمول provisioning state، size کی allow یا deny لسٹ میں موجودگی، اور GPUs کی تعداد۔

    ```python
    # استثناء کا پیغام پرنٹ کریں
    print(e)
    # اگر compute size ورک اسپیس میں دستیاب نہیں ہے تو ValueError اٹھائیں
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML ورک اسپیس سے compute instance حاصل کریں
    compute = workspace_ml_client.compute.get(compute_cluster)
    # چیک کریں کہ compute instance کی provisioning state "failed" ہے یا نہیں
    if compute.provisioning_state.lower() == "failed":
        # اگر provisioning state "failed" ہو تو ValueError اٹھائیں
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # چیک کریں کہ computes_allow_list None نہ ہو
    if computes_allow_list is not None:
        # computes_allow_list میں موجود تمام compute sizes کو چھوٹے حروف میں تبدیل کریں
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # چیک کریں کہ compute instance کا سائز computes_allow_list_lower_case میں موجود ہے یا نہیں
        if compute.size.lower() not in computes_allow_list_lower_case:
            # اگر compute instance کا سائز computes_allow_list_lower_case میں نہیں ہے تو ValueError اٹھائیں
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # غیر معاون GPU VM سائزز کی ایک فہرست تعریف کریں
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # چیک کریں کہ compute instance کا سائز unsupported_gpu_vm_list میں موجود ہے یا نہیں
        if compute.size.lower() in unsupported_gpu_vm_list:
            # اگر compute instance کا سائز unsupported_gpu_vm_list میں ہے تو ValueError اٹھائیں
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # ایک فلگ initialize کریں تاکہ چیک کیا جا سکے کہ compute instance میں GPUs کی تعداد مل گئی ہے یا نہیں
    gpu_count_found = False
    # ورک اسپیس میں دستیاب تمام compute سائزز کی فہرست حاصل کریں
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # دستیاب compute سائزز کی فہرست پر iteration کریں
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # چیک کریں کہ compute size کا نام compute instance کے سائز سے میل کھاتا ہے یا نہیں
        if compute_sku.name.lower() == compute.size.lower():
            # اگر میل کھایا تو اس compute size کے لئے GPUs کی تعداد حاصل کریں اور gpu_count_found کو True پر سیٹ کریں
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # اگر gpu_count_found True ہے تو compute instance میں GPUs کی تعداد پرنٹ کریں
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # اگر gpu_count_found False ہے تو ValueError اٹھائیں
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. ماڈل کی فائن ٹیوننگ کے لیے ڈیٹا سیٹ منتخب کریں

1. ہم ultrachat_200k ڈیٹا سیٹ استعمال کرتے ہیں۔ اس ڈیٹا سیٹ میں چار سپلٹس ہیں، جو Supervised fine-tuning (sft) کے لیے مناسب ہیں۔
Generation ranking (gen). ہر سپلٹ میں موجود مثالوں کی تعداد درج ذیل ہے:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. اگلے چند سیلز میں فائن ٹیوننگ کے لیے بنیادی ڈیٹا تیاری دکھائی گئی ہے:

### کچھ ڈیٹا قطاریں دیکھیں

ہم چاہتے ہیں کہ یہ سیمپل جلدی چلے، اس لیے train_sft اور test_sft فائلیں محفوظ کریں جن میں پہلے سے فلٹر شدہ قطاروں کا 5% موجود ہو۔ اس کا مطلب ہے کہ فائن ٹیون ماڈل کی درستگی کم ہو گی، لہٰذا اسے حقیقی دنیا میں استعمال نہیں کرنا چاہیے۔
download-dataset.py ultrachat_200k ڈیٹا سیٹ ڈاؤن لوڈ کرنے اور اسے فائن ٹیون پائپ لائن کمپونینٹ کے مطابق تبدیل کرنے کے لیے استعمال ہوتا ہے۔ چونکہ ڈیٹا سیٹ بہت بڑا ہے، اس لیے یہاں صرف حصہ دیا گیا ہے۔

1. نیچے دیا گیا اسکرپٹ صرف 5% ڈیٹا ڈاؤن لوڈ کرتا ہے۔ اسے dataset_split_pc پیرا میٹر کو مطلوبہ فیصد میں تبدیل کر کے بڑھایا جا سکتا ہے۔

> [!NOTE]
> بعض زبان کے ماڈلز کی زبان کے مختلف کوڈ ہوتے ہیں لہٰذا ڈیٹا سیٹ میں کالم کے نام بھی اسی کے مطابق ہونے چاہییں۔

1. یہاں ایک مثال ہے کہ ڈیٹا کیسا دکھائی دے گا
چیٹ-کمپلیشن ڈیٹا سیٹ parquet فارمیٹ میں محفوظ ہے، ہر انٹری درج ذیل schema کو استعمال کرتی ہے:

    - یہ ایک JSON (جاوا اسکرپٹ آبجیکٹ نوٹیشن) دستاویز ہے، جو ایک مقبول ڈیٹا انٹرچینج فارمیٹ ہے۔ یہ قابلِ عمل کوڈ نہیں بلکہ ڈیٹا ذخیرہ کرنے اور منتقل کرنے کا ذریعہ ہے۔ اس کی ساخت کا خلاصہ درج ذیل ہے:

    - "prompt": یہ کلید ایک سٹرنگ ویلیو رکھتی ہے جو AI اسسٹنٹ کو دئیے گئے ٹاسک یا سوال کی نمائندگی کرتی ہے۔

    - "messages": یہ کلید اشیاء کی ایک ارے رکھتی ہے۔ ہر اشیاء گفتگو میں صارف اور AI اسسٹنٹ کے درمیان ایک پیغام کی نمائندگی کرتی ہے۔ ہر پیغام میں دو کلیدیں ہوتی ہیں:

    - "content": یہ کلید پیغام کے مواد کی سٹرنگ ویلیو رکھتی ہے۔
    - "role": یہ کلید اس شے کی سٹرنگ ویلیو رکھتی ہے جس نے پیغام بھیجا ہے، جو "user" یا "assistant" ہو سکتی ہے۔
    - "prompt_id": یہ کلید اس پرامپٹ کی منفرد شناختی ویلیو رکھتی ہے۔

1. اس مخصوص JSON دستاویز میں، ایک گفتگو ہو رہی ہے جہاں صارف AI اسسٹنٹ سے dystopian کہانی کے لیے ایک ہیرو بنانے کو کہتا ہے۔ اسسٹنٹ جواب دیتا ہے، پھر صارف مزید تفصیلات طلب کرتا ہے، اور اسسٹنٹ مزید تفصیلات فراہم کرنے پر راضی ہو جاتا ہے۔ پوری گفتگو مخصوص prompt_id کے ساتھ منسلک ہے۔

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

### ڈیٹا ڈاؤن لوڈ کریں

1. یہ Python اسکرپٹ download-dataset.py نامی معاون اسکرپٹ کے ذریعے ڈیٹا سیٹ ڈاؤن لوڈ کرنے کے لیے استعمال ہوتا ہے۔ خلاصہ درج ذیل ہے:

    - os ماڈیول امپورٹ کرتا ہے، جو آپریٹنگ سسٹم کی منحصر فعالیت کے لیے پورٹیبل طریقہ فراہم کرتا ہے۔

    - os.system فنکشن کا استعمال کرتے ہوئے download-dataset.py اسکرپٹ کو شیل میں مخصوص کمانڈ لائن دلائل کے ساتھ چلاتا ہے۔ دلائل میں ڈاؤن لوڈ کے لیے ڈیٹا سیٹ (HuggingFaceH4/ultrachat_200k)، اسے محفوظ کرنے کے لیے ڈائریکٹری (ultrachat_200k_dataset)، اور ڈیٹا سیٹ کے کتنے فیصد حصے کو الگ کرنا ہے (5) شامل ہے۔ os.system کمانڈ کے ایگزٹ اسٹیٹس کو واپس دیتا ہے جسے exit_status میں محفوظ کیا جاتا ہے۔

    - اگر exit_status صفر (0) نہ ہو، تو یہ Exception اٹھاتا ہے جس میں بتایا جاتا ہے کہ ڈیٹا سیٹ ڈاؤن لوڈ کرنے میں خرابی ہوئی۔

    - خلاصہ یہ کہ یہ اسکرپٹ معاون اسکرپٹ کا استعمال کرتے ہوئے ڈیٹا سیٹ ڈاؤن لوڈ کرنے کے لیے کمانڈ چلاتا ہے اور اگر کمانڈ ناکام ہو تو استثناء پھینکتا ہے۔

    ```python
    # os ماڈیول کو درآمد کریں، جو آپریٹنگ سسٹم پر منحصر فنکشنلٹی استعمال کرنے کا طریقہ فراہم کرتا ہے
    import os
    
    # os.system فنکشن استعمال کریں تاکہ download-dataset.py اسکرپٹ کو شیل میں مخصوص کمانڈ لائن آرگیومنٹس کے ساتھ چلایا جا سکے
    # آرگیومنٹس ڈیٹاسیٹ کو ڈاؤن لوڈ کرنے کے لیے مخصوص کرتے ہیں (HuggingFaceH4/ultrachat_200k)، ڈائریکٹری جہاں اسے ڈاؤن لوڈ کرنا ہے (ultrachat_200k_dataset)، اور ڈیٹاسیٹ کو تقسیم کرنے کی فیصد (5)
    # os.system فنکشن اس کمانڈ کا ایگزٹ اسٹیٹس واپس کرتا ہے جو اس نے چلائی؛ اس اسٹیٹس کو exit_status ویریئبل میں محفوظ کیا جاتا ہے
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # چیک کریں کہ آیا exit_status صفر نہیں ہے
    # یونکس طرز کے آپریٹنگ سسٹمز میں، ایگزٹ اسٹیٹس کا صفر ہونا عام طور پر یہ ظاہر کرتا ہے کہ کمانڈ کامیاب رہی، جبکہ کوئی بھی دوسرا نمبر غلطی کی نشاندہی کرتا ہے
    # اگر exit_status صفر نہیں ہے، تو ایک Exception اٹھائیں جس میں یہ پیغام ہو کہ ڈیٹاسیٹ ڈاؤن لوڈ کرنے میں غلطی ہوئی ہے
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### ڈیٹا کو DataFrame میں لوڈ کرنا

1. یہ Python اسکرپٹ JSON Lines فائل کو pandas DataFrame میں لوڈ کر رہا ہے اور پہلے 5 قطاریں دکھا رہا ہے۔ خلاصہ درج ذیل ہے:

    - pandas لائبریری امپورٹ کرتا ہے، جو طاقتور ڈیٹا مینیپولیشن اور تجزیے کی لائبریری ہے۔

    - pandas کی display options میں زیادہ سے زیادہ کالم چوڑائی کو 0 سیٹ کرتا ہے۔ اس کا مطلب ہے کہ DataFrame پرنٹ کرتے وقت ہر کالم کا پورا متن بغیر کٹاو کے دکھایا جائے گا۔
- یہ pd.read_json فنکشن کا استعمال کرتا ہے تاکہ ultrachat_200k_dataset ڈائریکٹری سے train_sft.jsonl فائل کو DataFrame میں لوڈ کیا جا سکے۔ lines=True آرگیومنٹ ظاہر کرتا ہے کہ فائل JSON Lines فارمیٹ میں ہے، جہاں ہر لائن ایک الگ JSON آبجیکٹ ہوتا ہے۔

- یہ head طریقہ استعمال کرتا ہے تاکہ DataFrame کی پہلی 5 قطاریں دکھا سکے۔ اگر DataFrame میں 5 سے کم قطاریں ہوں تو یہ سب دکھائے گا۔

- خلاصہ کے طور پر، یہ اسکرپٹ ایک JSON Lines فائل کو DataFrame میں لوڈ کر رہا ہے اور مکمل کالم کے متن کے ساتھ پہلی 5 قطاریں دکھا رہا ہے۔
    
    ```python
    # pandas لائبریری کو درآمد کریں جو ایک طاقتور ڈیٹا کی تبدیلی اور تجزیہ کی لائبریری ہے
    import pandas as pd
    
    # pandas کی ڈسپلے آپشنز کے لئے زیادہ سے زیادہ کالم چوڑائی 0 پر مقرر کریں
    # اس کا مطلب ہے کہ ہر کالم کا مکمل متن بغیر کٹاؤ کے ظاہر کیا جائے گا جب DataFrame چھاپا جائے گا
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json فنکشن استعمال کریں تاکہ ultrachat_200k_dataset ڈائریکٹری سے train_sft.jsonl فائل کو DataFrame میں لوڈ کیا جا سکے
    # lines=True دلیل ظاہر کرتی ہے کہ فائل JSON لائنز فارمیٹ میں ہے، جہاں ہر لائن ایک علیحدہ JSON آبجیکٹ ہے
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # head میتھڈ استعمال کریں تاکہ DataFrame کی پہلی 5 قطاریں دکھائی جا سکیں
    # اگر DataFrame میں 5 سے کم قطاریں ہوں، تو یہ سب کو ظاہر کرے گا
    df.head()
    ```

## 5۔ ماڈل اور ڈیٹا کو ان پٹ کے طور پر استعمال کرتے ہوئے فائن ٹیوننگ جاب جمع کروائیں

چاہٹ-تکمیل پایپ لائن کمپونینٹ استعمال کرنے والی جاب بنائیں۔ فائن ٹیوننگ کے لیے سپورٹ کردہ تمام پیرامیٹرز کے بارے میں مزید جانیں۔

### فائن ٹیون پیرامیٹرز کی تعریف کریں

1۔ فائن ٹیون پیرامیٹرز دو زمروں میں تقسیم کیے جا سکتے ہیں - تربیتی پیرامیٹرز، اصلاحی پیرامیٹرز

1۔ تربیتی پیرامیٹرز تربیت کے پہلوؤں کی تعریف کرتے ہیں جیسے -

    - استعمال کرنے والا اوپٹیمائزر، شیڈیولر
    - فائن ٹیون کی اصلاح کے لیے میٹرک
    - تربیتی مراحل کی تعداد، بیچ سائز وغیرہ
    - اصلاحی پیرامیٹرز GPU میموری کی اصلاح اور کمپیوٹ وسائل کے مؤثر استعمال میں مدد دیتے ہیں۔

1۔ ذیل میں کچھ ایسے پیرامیٹرز ہیں جو اس زمرے سے تعلق رکھتے ہیں۔ اصلاحی پیرامیٹرز ہر ماڈل کے لیے مختلف ہوتے ہیں اور ماڈل کے ساتھ پیک کیے جاتے ہیں تاکہ ان تبدیلیوں کو سنبھالا جا سکے۔

    - deepspeed اور LoRA کو فعال کریں
    - مخلوط درستگی کی تربیت کو فعال کریں
    - ملٹی نوڈ تربیت کو فعال کریں

> [!NOTE]
> نگرانی شدہ فائن ٹیوننگ الائنمنٹ کھونے یا تباہ کن فراموشی کا سبب بن سکتی ہے۔ ہم اس مسئلے کی جانچ کرنے اور فائن ٹیون کرنے کے بعد الائنمنٹ مرحلہ چلانے کی سفارش کرتے ہیں۔

### فائن ٹیوننگ پیرامیٹرز

1۔ یہ پائتھن اسکرپٹ مشین لرننگ ماڈل کی فائن ٹیوننگ کے لیے پیرامیٹرز مرتب کر رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ تربیتی پیرامیٹرز کی ڈیفالٹ سیٹنگز سیٹ کرتا ہے، جیسے تربیت کے ادوار کی تعداد، تربیت اور تشخیص کے لیے بیچ سائز، لرننگ ریٹ، اور لرننگ ریٹ شیڈیولر کی قسم۔

    - یہ اصلاحی پیرامیٹرز کی ڈیفالٹ سیٹنگز سیٹ کرتا ہے، جیسے کہ Layer-wise Relevance Propagation (LoRa) اور DeepSpeed کو لگایا جائے یا نہیں، اور DeepSpeed کا مرحلہ۔

    - یہ تربیتی اور اصلاحی پیرامیٹرز کو ایک ہی لغت میں جمع کرتا ہے جسے finetune_parameters کہتے ہیں۔

    - یہ چیک کرتا ہے کہ foundation_model کے پاس کوئی ماڈل مخصوص ڈیفالٹ پیرامیٹرز ہیں یا نہیں۔ اگر ہیں، تو ایک وارننگ پیغام پرنٹ کرتا ہے اور finetune_parameters لغت کو ان ماڈل مخصوص ڈیفالٹس سے اپ ڈیٹ کرتا ہے۔ ast.literal_eval فنکشن اسٹریگ کو پائتھن لغت میں تبدیل کرنے کے لیے استعمال ہوتا ہے۔

    - یہ فائن ٹیوننگ کے لیے آخری پیرامیٹرز پرنٹ کرتا ہے جو رن کے لیے استعمال ہوں گے۔

    - خلاصہ کے طور پر، یہ اسکرپٹ مشین لرننگ ماڈل کی فائن ٹیوننگ کے پیرامیٹرز ترتیب دے رہا ہے اور دکھا رہا ہے، جس میں ماڈل مخصوص ڈیفالٹس کے ساتھ ڈیفالٹ پیرامیٹرز کو اوور رائڈ کرنے کی صلاحیت ہے۔

    ```python
    # ڈیفالٹ تربیتی پیرامیٹرز جیسے تربیتی ایپوک کی تعداد، تربیت اور جانچ کے لئے بیچ سائز، لرننگ ریٹ، اور لرننگ ریٹ شیڈولر کی قسم سیٹ کریں
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # ڈیفالٹ آپٹیمائزیشن پیرامیٹرز سیٹ کریں جیسے کہ Layer-wise Relevance Propagation (LoRa) اور DeepSpeed کو لاگو کرنا ہے یا نہیں، اور DeepSpeed کا اسٹیج
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # تربیتی اور آپٹیمائزیشن پیرامیٹرز کو ایک واحد لغت میں جوڑیں جسے finetune_parameters کہا جاتا ہے
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # چیک کریں کہ foundation_model کے پاس کوئی ماڈل مخصوص ڈیفالٹ پیرامیٹرز ہیں یا نہیں
    # اگر ہیں تو ایک وارننگ پیغام پرنٹ کریں اور finetune_parameters لغت کو ان ماڈل مخصوص ڈیفالٹس کے ساتھ اپ ڈیٹ کریں
    # ast.literal_eval فنکشن ماڈل مخصوص ڈیفالٹس کو ایک سٹرنگ سے Python لغت میں تبدیل کرنے کے لئے استعمال ہوتا ہے
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # سٹرنگ کو python dict میں تبدیل کریں
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # فائن-ٹیوننگ کے حتمی پیرامیٹرز پرنٹ کریں جو رن کے لئے استعمال ہوں گے
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### تربیتی پایپ لائن

1۔ یہ پائتھن اسکرپٹ ایک فنکشن کی تعریف کر رہا ہے جو مشین لرننگ تربیتی پایپ لائن کے لیے ڈسپلے نام تیار کرتا ہے، پھر اس فنکشن کو کال کر کے ڈسپلے نام تیار کر کے پرنٹ کرتا ہے۔ ذیل میں اس کا تجزیہ ہے:

1۔ get_pipeline_display_name فنکشن کی تعریف کی گئی ہے۔ یہ فنکشن تربیتی پایپ لائن سے متعلق مختلف پیرامیٹرز کی بنیاد پر ڈسپلے نام تیار کرتا ہے۔

1۔ فنکشن کے اندر، یہ کل بیچ سائز کا حساب لگاتا ہے جو فی ڈیوائس بیچ سائز، گریڈینٹ جمع کرنے کے مراحل کی تعداد، فی نوڈ GPU کی تعداد، اور فائن ٹیوننگ کے لیے استعمال ہونے والے نوڈز کی تعداد کو ضرب دے کر حاصل ہوتا ہے۔

1۔ یہ لرننگ ریٹ شیڈیولر کی قسم، DeepSpeed کے استعمال کی صورت، DeepSpeed کا مرحلہ، Layer-wise Relevance Propagation (LoRa) کے استعمال کی صورت، ماڈل چیک پوائنٹس رکھنے کی حد، اور میکسیمم سیکوینس لمبائی جیسے مختلف دیگر پیرامیٹرز حاصل کرتا ہے۔

1۔ یہ ان تمام پیرامیٹرز کو ہائفن سے جدا کرتے ہوئے ایک سٹرنگ بناتا ہے۔ اگر DeepSpeed یا LoRa لگایا گیا ہو، تو سٹرنگ میں بالترتیب "ds" اور DeepSpeed مرحلہ یا "lora" شامل ہوتا ہے۔ اگر نہیں، تو "nods" یا "nolora" شامل ہوتا ہے۔

1۔ فنکشن یہ سٹرنگ واپس کرتا ہے جو تربیتی پایپ لائن کے لیے ڈسپلے نام کے طور پر کام کرتی ہے۔

1۔ فنکشن کی تعریف کے بعد، اسے کال کر کے ڈسپلے نام تیار کیا جاتا ہے اور پرنٹ کیا جاتا ہے۔

1۔ خلاصہ کے طور پر، یہ اسکرپٹ مختلف پیرامیٹرز کی بنیاد پر مشین لرننگ تربیتی پایپ لائن کے لیے ڈسپلے نام تیار کر رہا ہے اور پھر اسے پرنٹ کر رہا ہے۔

    ```python
    # ٹریننگ پائپ لائن کے لیے ڈسپلے نام بنانے کے لیے ایک فنکشن تعریف کریں
    def get_pipeline_display_name():
        # فی ڈیوائس بیچ سائز، گرادیئنٹ اکومیولیشن کے اقدامات کی تعداد، فی نوڈ جی پی یوز کی تعداد، اور فائن ٹوننگ کے لیے استعمال ہونے والے نوڈز کی تعداد کو ضرب دے کر کل بیچ سائز کا حساب لگائیں
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # لرننگ ریٹ شیڈیولر کی قسم حاصل کریں
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # یہ معلوم کریں کہ آیا ڈیپ اسپیڈ لاگو کیا گیا ہے
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # ڈیپ اسپیڈ مرحلہ حاصل کریں
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # اگر ڈیپ اسپیڈ لاگو ہے تو ڈسپلے نام میں "ds" کے بعد ڈیپ اسپیڈ مرحلہ شامل کریں؛ اگر نہیں، تو "nods" شامل کریں
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # یہ معلوم کریں کہ آیا لیئر وائز ریلیونس پروپیگیشن (LoRa) لاگو ہے
        lora = finetune_parameters.get("apply_lora", "false")
        # اگر LoRa لاگو ہے تو ڈسپلے نام میں "lora" شامل کریں؛ اگر نہیں، تو "nolora" شامل کریں
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # ماڈل چیک پوائنٹس کی محدود تعداد کو برقرار رکھنے کی حد حاصل کریں
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # زیادہ سے زیادہ سیکوئنس لمبائی حاصل کریں
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # تمام ان پیرامیٹرز کو ہائفن سے الگ کرتے ہوئے جوڑ کر ڈسپلے نام تشکیل دیں
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
    
    # ڈسپلے نام بنانے کے لیے فنکشن کو کال کریں
    pipeline_display_name = get_pipeline_display_name()
    # ڈسپلے نام پرنٹ کریں
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### پایپ لائن کی تشکیل

یہ پائتھن اسکرپٹ Azure Machine Learning SDK کا استعمال کرتے ہوئے مشین لرننگ پایپ لائن کی تعریف اور ترتیب دے رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

1۔ یہ Azure AI ML SDK سے ضروری ماڈیولز درآمد کرتا ہے۔

1۔ یہ رجسٹری سے "chat_completion_pipeline" نامی پایپ لائن کمپونینٹ حاصل کرتا ہے۔

1۔ یہ @pipeline ڈیکوریٹر اور create_pipeline فنکشن کا استعمال کرتے ہوئے پایپ لائن جاب کی تعریف کرتا ہے۔ پایپ لائن کا نام pipeline_display_name سیٹ کیا گیا ہے۔

1۔ create_pipeline فنکشن کے اندر، حاصل کردہ پایپ لائن کمپونینٹ کو مختلف پیرامیٹرز کے ساتھ انیشیئلائز کیا گیا ہے، بشمول ماڈل کا راستہ، مختلف مراحل کے لیے کمپیوٹ کلسٹرز، تربیت اور جانچ کے لیے ڈیٹا سیٹ اسپلیٹس، فائن ٹیوننگ کے لیے GPU کی تعداد، اور دیگر فائن ٹیوننگ پیرامیٹرز۔

1۔ فائن ٹیوننگ جاب کے آؤٹ پٹ کو پایپ لائن جاب کے آؤٹ پٹ سے میپ کیا گیا ہے۔ اس کا مقصد یہ ہے کہ فائن ٹیون کیے گئے ماڈل کو آسانی سے رجسٹر کیا جا سکے، جو آن لائن یا بیچ اینڈ پوائنٹ میں ماڈل کی تعیناتی کے لیے ضروری ہے۔

1۔ پایپ لائن کی ایک مثال create_pipeline فنکشن کال کر کے بنائی گئی ہے۔

1۔ پایپ لائن کی force_rerun سیٹنگ کو True پر مقرر کیا گیا ہے، جس کا مطلب ہے کہ پچھلی جابز کے کیشڈ نتائج استعمال نہیں ہوں گے۔

1۔ پایپ لائن کی continue_on_step_failure سیٹنگ کو False پر مقرر کیا گیا ہے، جس کا مطلب ہے کہ اگر کسی بھی مرحلے میں ناکامی ہو تو پایپ لائن رک جائے گی۔

1۔ خلاصہ کے طور پر، یہ اسکرپٹ Azure Machine Learning SDK استعمال کرتے ہوئے چیٹ کمپلیشن ٹاسک کے لیے ایک مشین لرننگ پایپ لائن کی تعریف اور ترتیب دے رہا ہے۔

    ```python
    # درکار ماڈیولز کو Azure AI ML SDK سے درآمد کریں
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # ریجسٹری سے "chat_completion_pipeline" نامی پائپ لائن جزو حاصل کریں
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline ڈیکوریٹر اور create_pipeline فنکشن کا استعمال کرتے ہوئے پائپ لائن جاب کی تعریف کریں
    # پائپ لائن کا نام pipeline_display_name پر سیٹ کیا گیا ہے
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # حاصل کردہ پائپ لائن جزو کو مختلف پیرامیٹرز کے ساتھ شروع کریں
        # ان میں ماڈل کا راستہ، مختلف مراحل کے لیے کمپیوٹ کلسٹرز، تربیت اور جانچ کے لیے ڈیٹا سیٹ کی تقسیم، فائن ٹیوننگ کے لیے استعمال ہونے والے GPUs کی تعداد، اور دیگر فائن ٹیوننگ کے پیرامیٹرز شامل ہیں
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # ڈیٹا سیٹ کی تقسیم کو پیرامیٹرز کے ساتھ میپ کریں
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # تربیتی ترتیبات
            number_of_gpu_to_use_finetuning=gpus_per_node,  # کمپیوٹ میں دستیاب GPUs کی تعداد پر سیٹ کریں
            **finetune_parameters
        )
        return {
            # فائن ٹیوننگ جاب کے آؤٹ پٹ کو پائپ لائن جاب کے آؤٹ پٹ سے میپ کریں
            # یہ اس لیے کیا جاتا ہے تاکہ ہم آسانی سے فائن ٹیونڈ ماڈل کو رجسٹر کر سکیں
            # ماڈل کو رجسٹر کرنا آن لائن یا بیچ اینڈ پوائنٹ پر ماڈل کو تعینات کرنے کے لیے ضروری ہے
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline فنکشن کو کال کرکے پائپ لائن کا ایک انسٹنس بنائیں
    pipeline_object = create_pipeline()
    
    # پچھلے جابز کے کیش شدہ نتائج استعمال نہ کریں
    pipeline_object.settings.force_rerun = True
    
    # سٹیپ کی ناکامی پر جاری رکھنے کی سیٹنگ کو False پر سیٹ کریں
    # اس کا مطلب ہے کہ اگر کوئی بھی مرحلہ فیل ہو جائے تو پائپ لائن رک جائے گی
    pipeline_object.settings.continue_on_step_failure = False
    ```

### جاب جمع کرائیں

1۔ یہ پائتھن اسکرپٹ Azure Machine Learning ورک اسپیس میں ایک مشین لرننگ پایپ لائن جاب جمع کروا رہا ہے اور پھر جاب کے مکمل ہونے کا انتظار کر رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ workspace_ml_client میں jobs آبجیکٹ کی create_or_update میتھڈ کال کرکے پایپ لائن جاب جمع کروا رہا ہے۔ چلانے والی پایپ لائن pipeline_object سے مخصوص کی گئی ہے، اور جاب جس تجربے کے تحت چلتی ہے وہ experiment_name ہے۔

    - پھر یہ workspace_ml_client میں jobs آبجیکٹ کی stream میتھڈ کال کرتا ہے تاکہ پایپ لائن جاب کے مکمل ہونے کا انتظار کرے۔ انتظار کرنے والی جاب pipeline_job کے name اٹریبیوٹ سے مخصوص کی گئی ہے۔

    - خلاصہ کے طور پر، یہ اسکرپٹ Azure Machine Learning ورک اسپیس میں ایک مشین لرننگ پایپ لائن جاب جمع کروا رہا ہے اور پھر جاب کے مکمل ہونے کا انتظار کر رہا ہے۔

    ```python
    # پائپ لائن جاب کو Azure مشین لرننگ ورک اسپیس میں سبمٹ کریں
    # چلانے کے لیے پائپ لائن pipeline_object سے مشخص ہے
    # وہ تجربہ جس کے تحت جاب چلائی جاتی ہے experiment_name سے مشخص ہے
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # پائپ لائن جاب کے مکمل ہونے کا انتظار کریں
    # انتظار کرنے والی جاب pipeline_job آبجیکٹ کی name پراپرٹی سے مشخص ہے
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6۔ فائن ٹیون ماڈل کو ورک اسپیس میں رجسٹر کریں

ہم فائن ٹیوننگ جاب کے آؤٹ پٹ سے ماڈل کو رجسٹر کریں گے۔ یہ فائن ٹیون ماڈل اور فائن ٹیوننگ جاب کے درمیان لائنئج کو ٹریک کرے گا۔ فائن ٹیوننگ جاب مزید بنیاد ماڈل، ڈیٹا اور تربیتی کوڈ کی لائنئج کو بھی ٹریک کرتا ہے۔

### مشین لرننگ ماڈل کی رجسٹریشن

1۔ یہ پائتھن اسکرپٹ Azure Machine Learning پایپ لائن میں تربیت یافتہ مشین لرننگ ماڈل کو رجسٹر کر رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ Azure AI ML SDK سے ضروری ماڈیولز درآمد کرتا ہے۔

    - یہ چیک کرتا ہے کہ تربیت یافتہ ماڈل کا آؤٹ پٹ پایپ لائن جاب سے دستیاب ہے یا نہیں، اس کے لیے workspace_ml_client میں jobs آبجیکٹ کی get میتھڈ کال کرکے اور اس کے outputs اٹریبیوٹ تک رسائی حاصل کرکے۔

    - یہ پایپ لائن جاب کے نام اور آؤٹ پٹ ("trained_model") کے نام سے ایک راستہ بناتا ہے۔

    - یہ فائن ٹیون شدہ ماڈل کے لیے ایک نام متعین کرتا ہے جو ماڈل کے اصل نام میں "-ultrachat-200k" جوڑ کر بنایا جاتا ہے اور کسی بھی سلیش کو ہائفن سے بدل دیتا ہے۔

    - یہ ماڈل رجسٹر کرنے کی تیاری کرتا ہے، ایک Model آبجیکٹ بنا کر جس میں ماڈل کا راستہ، ماڈل کی قسم (MLflow ماڈل)، ماڈل کا نام اور ورژن، اور ماڈل کی تشریح شامل ہے۔

    - یہ ماڈل کو workspace_ml_client میں models آبجیکٹ کی create_or_update میتھڈ کال کر کے رجسٹر کرتا ہے۔

    - یہ رجسٹر شدہ ماڈل کو پرنٹ کرتا ہے۔

1۔ خلاصہ کے طور پر، یہ اسکرپٹ Azure Machine Learning پایپ لائن میں تربیت یافتہ مشین لرننگ ماڈل کو رجسٹر کر رہا ہے۔
    
    ```python
    # Azure AI ML SDK سے ضروری ماڈیولز درآمد کریں
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # چیک کریں کہ کیا pipeline job سے `trained_model` آؤٹ پٹ دستیاب ہے
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # pipeline job کے نام اور آؤٹ پٹ ("trained_model") کے نام کے ساتھ ایک سٹرنگ فارمیٹ کرکے تربیت یافتہ ماڈل کا راستہ بنائیں
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # اصلی ماڈل کے نام کے آخر میں "-ultrachat-200k" جوڑ کر اور کسی بھی سلیش کو ہائفن سے بدل کر فائن ٹیون شدہ ماڈل کے لیے نام مقرر کریں
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # مختلف پیرامیٹرز کے ساتھ ایک Model آبجیکٹ بنا کر ماڈل کو رجسٹر کرنے کی تیاری کریں
    # ان میں ماڈل کا راستہ، ماڈل کی قسم (MLflow ماڈل)، ماڈل کا نام اور ورژن، اور ماڈل کی تفصیل شامل ہیں
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # ورژن کے تنازع سے بچنے کے لیے ٹائم اسٹیمپ کو ورژن کے طور پر استعمال کریں
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # ماڈل آبجیکٹ کو دلیل کے طور پر استعمال کرتے ہوئے workspace_ml_client میں models آبجیکٹ کی create_or_update میتھڈ کو کال کر کے ماڈل کو رجسٹر کریں
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # رجسٹر کیا گیا ماڈل پرنٹ کریں
    print("registered model: \n", registered_model)
    ```

## 7۔ فائن ٹیون ماڈل کو آن لائن اینڈپوائنٹ پر تعینات کریں

آن لائن اینڈپوائنٹس ایک پائیدار REST API فراہم کرتے ہیں جسے ایسی ایپلیکیشنز میں انضمام کے لیے استعمال کیا جا سکتا ہے جنہیں ماڈل استعمال کرنا ہو۔

### اینڈپوائنٹ کا انتظام کریں

1۔ یہ پائتھن اسکرپٹ Azure Machine Learning میں رجسٹر کیے گئے ماڈل کے لیے ایک منیجڈ آن لائن اینڈپوائنٹ بنا رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ Azure AI ML SDK سے ضروری ماڈیولز درآمد کرتا ہے۔

    - یہ "ultrachat-completion-" سٹرنگ کے ساتھ ایک ٹائم اسٹیمپ جوڑ کر آن لائن اینڈپوائنٹ کے لیے ایک منفرد نام متعین کرتا ہے۔

    - یہ آن لائن اینڈپوائنٹ بنانے کی تیاری کرتا ہے، ManagedOnlineEndpoint آبجیکٹ بنا کر جس میں اینڈپوائنٹ کا نام، اس کی تشریح، اور تصدیقی طریقہ ("key") شامل ہے۔

    - یہ workspace_ml_client کی begin_create_or_update میتھڈ کال کر کے آن لائن اینڈپوائنٹ بناتا ہے، پھر wait میتھڈ کال کرکے تخلیقی عمل مکمل ہونے کا انتظار کرتا ہے۔

1۔ خلاصہ کے طور پر، یہ اسکرپٹ Azure Machine Learning میں رجسٹر کیے گئے ماڈل کے لیے ایک منیج شدہ آن لائن اینڈپوائنٹ بنا رہا ہے۔

    ```python
    # لازمی ماڈیولز کو Azure AI ML SDK سے درآمد کریں
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" کے ساتھ وقت کا نشان جوڑ کر آن لائن اینڈ پوائنٹ کے لیے منفرد نام مقرر کریں
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # ManagedOnlineEndpoint آبجیکٹ بنا کر مختلف پیرامیٹرز کے ساتھ آن لائن اینڈ پوائنٹ بنانے کی تیاری کریں
    # ان میں اینڈ پوائنٹ کا نام، اینڈ پوائنٹ کی تفصیل، اور توثیقی طریقہ ("key") شامل ہیں
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint آبجیکٹ کو آرگیومنٹ کے طور پر ورک اسپیس_ml_client کے begin_create_or_update طریقہ کو کال کرکے آن لائن اینڈ پوائنٹ بنائیں
    # پھر تخلیقی عمل مکمل ہونے کے لیے wait طریقہ کال کرکے انتظار کریں
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> یہاں آپ کو تعیناتی کے لیے سپورٹ شدہ SKU کی فہرست ملے گی - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### مشین لرننگ ماڈل کی تعیناتی

1۔ یہ پائتھن اسکرپٹ Azure Machine Learning میں منیجڈ آن لائن اینڈپوائنٹ پر رجسٹر شدہ مشین لرننگ ماڈل کو تعینات کر رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ ast ماڈیول درآمد کرتا ہے، جو پائتھن کے تجریدی نحو کے درختوں کو پروسیس کرنے کے فنکشنز فراہم کرتا ہے۔

    - یہ تعیناتی کے لیے انسٹینس کی قسم "Standard_NC6s_v3" سیٹ کرتا ہے۔

    - یہ چیک کرتا ہے کہ foundation model میں inference_compute_allow_list ٹیگ موجود ہے یا نہیں۔ اگر موجود ہے تو اس کا اسٹرنگ ویلیو پائتھن کی فہرست میں تبدیل کرتا ہے اور اسے inference_computes_allow_list میں محفوظ کرتا ہے۔ اگر نہیں، تو اسے None سیٹ کرتا ہے۔

    - یہ چیک کرتا ہے کہ مخصوص انسٹینس کی قسم اجازت یافتہ فہرست میں ہے یا نہیں۔ اگر نہیں، تو صارف کو ایک پیغام پرنٹ کرتا ہے جس میں اس سے اجازت یافتہ فہرست میں سے انسٹینس کی قسم منتخب کرنے کو کہا جاتا ہے۔

    - یہ تعیناتی کی تیاری کرتا ہے، ManagedOnlineDeployment آبجیکٹ بنا کر جس میں تعیناتی کا نام، اینڈپوائنٹ کا نام، ماڈل کا ID، انسٹینس کی قسم اور تعداد، لائیونس پروب کی ترتیبات، اور ریکویسٹ سیٹنگز شامل ہیں۔

    - یہ workspace_ml_client کی begin_create_or_update میتھڈ کال کر کے تعیناتی بناتا ہے، پھر wait میتھڈ کال کرکے تخلیقی عمل کا انتظار کرتا ہے۔

    - یہ اینڈپوائنٹ کے ٹریفک کو 100% "demo" تعیناتی کی طرف بھیجنے کے لیے سیٹ کرتا ہے۔

    - یہ begin_create_or_update میتھڈ کال کر کے اینڈپوائنٹ کو اپ ڈیٹ کرتا ہے اور result میتھڈ کال کر کے اپ ڈیٹ کے مکمل ہونے کا انتظار کرتا ہے۔

1۔ خلاصہ کے طور پر، یہ اسکرپٹ Azure Machine Learning میں منیجڈ آن لائن اینڈپوائنٹ پر رجسٹر شدہ مشین لرننگ ماڈل کو تعینات کر رہا ہے۔

    ```python
    # پائتھن کے آبسٹریکٹ سنٹیکس گرائمر کے درختوں کو پروسیس کرنے کے لیے فنکشن فراہم کرنے والا ast ماڈیول امپورٹ کریں
    import ast
    
    # ڈپلائمنٹ کے لیے انسٹانس کی قسم سیٹ کریں
    instance_type = "Standard_NC6s_v3"
    
    # چیک کریں کہ فاؤنڈیشن ماڈل میں `inference_compute_allow_list` ٹیگ موجود ہے یا نہیں
    if "inference_compute_allow_list" in foundation_model.tags:
        # اگر ہے، تو ٹیگ کی قیمت کو سٹرنگ سے پائتھن کی لسٹ میں تبدیل کریں اور اسے `inference_computes_allow_list` کو تفویض کریں
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # اگر نہیں ہے، تو `inference_computes_allow_list` کو `None` پر سیٹ کریں
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # چیک کریں کہ متعین شدہ انسٹانس کی قسم اجازت کی لسٹ میں ہے یا نہیں
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # مختلف پیرامیٹرز کے ساتھ `ManagedOnlineDeployment` آبجیکٹ بنا کر ڈپلائمنٹ تخلیق کرنے کی تیاری کریں
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `workspace_ml_client` کے `begin_create_or_update` میتھڈ کو `ManagedOnlineDeployment` آبجیکٹ کے ساتھ کال کرکے ڈپلائمنٹ بنائیں
    # پھر تخلیق کے عمل کے مکمل ہونے کے لیے `wait` میتھڈ کو کال کریں
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # اینڈ پوائنٹ کا ٹریفک اس طرح سیٹ کریں کہ 100% ٹریفک "demo" ڈپلائمنٹ کی طرف جائے
    endpoint.traffic = {"demo": 100}
    
    # `workspace_ml_client` کے `begin_create_or_update` میتھڈ کو `endpoint` آبجیکٹ کے ساتھ کال کرکے اینڈ پوائنٹ کو اپ ڈیٹ کریں
    # پھر اپ ڈیٹ کے عمل کے مکمل ہونے کے لیے `result` میتھڈ کو کال کریں
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8۔ اینڈپوائنٹ کو نمونہ ڈیٹا کے ساتھ آزمانا

ہم ٹیسٹ ڈیٹا سیٹ سے کچھ نمونہ ڈیٹا لیں گے اور آن لائن اینڈپوائنٹ کو انفرنس کے لیے جمع کروائیں گے۔ پھر ہم سکور شدہ لیبلز کو گراؤنڈ ٹروتھ لیبلز کے ساتھ دکھائیں گے۔

### نتائج پڑھنا

1۔ یہ پائتھن اسکرپٹ ایک JSON Lines فائل کو pandas DataFrame میں پڑھ رہا ہے، ایک تصادفی نمونہ لے رہا ہے، اور انڈیکس کو ری سیٹ کر رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ ./ultrachat_200k_dataset/test_gen.jsonl فائل کو pandas DataFrame میں پڑھ رہا ہے۔ read_json فنکشن lines=True آرگیومنٹ کے ساتھ استعمال ہوتا ہے کیونکہ فائل JSON Lines فارمیٹ میں ہے جہاں ہر لائن ایک الگ JSON آبجیکٹ ہوتی ہے۔

    - یہ DataFrame سے 1 قطار کا تصادفی نمونہ لیتا ہے۔ sample فنکشن n=1 آرگیومنٹ کے ساتھ استعمال ہوتا ہے تاکہ منتخب کی جانے والی قطاروں کی تعداد بتائی جا سکے۔

    - یہ DataFrame کا انڈیکس ری سیٹ کرتا ہے۔ reset_index فنکشن drop=True آرگیومنٹ کے ساتھ استعمال ہوتا ہے تاکہ اصل انڈیکس کو چھوڑ کر نئی ڈیفالٹ انٹیجر انڈیکس لگائی جا سکے۔

    - یہ head فنکشن کے آرگیومنٹ 2 کے ساتھ DataFrame کی پہلی 2 قطاریں دکھاتا ہے۔ تاہم چونکہ نمونے کے بعد صرف ایک قطار ہے، تو صرف وہی ایک قطار دکھائی جائے گی۔

1۔ خلاصہ کے طور پر، یہ اسکرپٹ JSON Lines فائل کو pandas DataFrame میں پڑھ رہا ہے، 1 قطار کا تصادفی نمونہ لے رہا ہے، انڈیکس ری سیٹ کر رہا ہے، اور پہلی قطار دکھا رہا ہے۔
    
    ```python
    # پینڈاز لائبریری درآمد کریں
    import pandas as pd
    
    # JSON Lines فائل './ultrachat_200k_dataset/test_gen.jsonl' کو پینڈاز ڈیٹا فریم میں پڑھیں
    # 'lines=True' دلیل ظاہر کرتی ہے کہ فائل JSON Lines فارمیٹ میں ہے، جہاں ہر لائن ایک الگ JSON آبجیکٹ ہے
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # ڈیٹا فریم سے 1 قطار کا بے ترتیب نمونہ لیں
    # 'n=1' دلیل بے ترتیب قطاروں کی تعداد کو متعین کرتی ہے
    test_df = test_df.sample(n=1)
    
    # ڈیٹا فریم کے انڈیکس کو ری سیٹ کریں
    # 'drop=True' دلیل ظاہر کرتی ہے کہ اصل انڈیکس حذف کر کے نئے ڈیفالٹ عددی انڈیکس سے بدل دیا جائے
    # 'inplace=True' دلیل ظاہر کرتی ہے کہ ڈیٹا فریم کو اصل جگہ پر (نیا آبجیکٹ بنائے بغیر) تبدیل کیا جائے
    test_df.reset_index(drop=True, inplace=True)
    
    # ڈیٹا فریم کی پہلی 2 قطاریں دکھائیں
    # تاہم، چونکہ سیمپلنگ کے بعد ڈیٹا فریم میں صرف ایک قطار ہے، اس لیے صرف وہی ایک قطار دکھائی جائے گی
    test_df.head(2)
    ```

### JSON آبجیکٹ تیار کریں

1۔ یہ پائتھن اسکرپٹ مخصوص پیرامیٹرز کے ساتھ JSON آبجیکٹ بنا رہا ہے اور اسے فائل میں محفوظ کر رہا ہے۔ ذیل میں اس کا تجزیہ ہے:

    - یہ json ماڈیول درآمد کر رہا ہے، جو JSON ڈیٹا کے ساتھ کام کرنے کے لیے فنکشنز فراہم کرتا ہے۔
- یہ ایک dictionary parameters بناتا ہے جس کی keys اور values ایسے parameters کی نمائندگی کرتی ہیں جو ایک مشین لرننگ ماڈل کے لیے ہیں۔ keys "temperature"، "top_p"، "do_sample"، اور "max_new_tokens" ہیں، اور ان کی متعلقہ values بالترتیب 0.6، 0.9، True، اور 200 ہیں۔

- یہ ایک اور dictionary test_json بناتا ہے جس میں دو keys ہیں: "input_data" اور "params"۔ "input_data" کی value ایک اور dictionary ہے جس میں "input_string" اور "parameters" keys ہیں۔ "input_string" کی value ایک list ہے جس میں test_df DataFrame کا پہلا پیغام موجود ہے۔ "parameters" کی value پہلے بنائی گئی parameters dictionary ہے۔ "params" کی value ایک خالی dictionary ہے۔

- یہ sample_score.json نامی فائل کھولتا ہے

    ```python
    # json ماڈیول کو درآمد کریں، جو JSON ڈیٹا کے ساتھ کام کرنے کے لئے فنکشن فراہم کرتا ہے
    import json
    
    # ایک لغت `parameters` بنائیں جس میں کلیدیں اور قدریں شامل ہوں جو مشین لرننگ ماڈل کے پیرامیٹرز کی نمائندگی کرتی ہوں
    # کلیدیں "temperature"، "top_p"، "do_sample"، اور "max_new_tokens" ہیں، اور ان کی متعلقہ قدریں بالترتیب 0.6، 0.9، True، اور 200 ہیں
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # ایک اور لغت `test_json` بنائیں جس میں دو کلیدیں ہوں: "input_data" اور "params"
    # "input_data" کی قیمت ایک اور لغت ہے جس میں کلیدیں "input_string" اور "parameters" شامل ہیں
    # "input_string" کی قیمت ایک فہرست ہے جس میں `test_df` DataFrame کا پہلا پیغام شامل ہے
    # "parameters" کی قیمت وہ `parameters` لغت ہے جو پہلے بنائی گئی تھی
    # "params" کی قیمت ایک خالی لغت ہے
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` ڈائریکٹری میں `sample_score.json` نامی فائل کو لکھنے کے موڈ میں کھولیں
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `test_json` لغت کو JSON فارمیٹ میں `json.dump` فنکشن کا استعمال کرتے ہوئے فائل میں لکھیں
        json.dump(test_json, f)
    ```

### اینڈپوائنٹ کو کال کرنا

1. یہ Python اسکرپٹ Azure Machine Learning میں ایک آن لائن اینڈپوائنٹ کو کال کر رہا ہے تاکہ ایک JSON فائل کو اسکور کیا جا سکے۔ یہ اس بات کا خلاصہ ہے کہ یہ کیا کرتا ہے:

- یہ workspace_ml_client آبجیکٹ کی online_endpoints پراپرٹی کے invoke طریقہ کو کال کرتا ہے۔ یہ طریقہ ایک آن لائن اینڈپوائنٹ کو درخواست بھیجنے اور جواب حاصل کرنے کے لیے استعمال ہوتا ہے۔

- یہ endpoint_name اور deployment_name دلائل کے ساتھ اینڈپوائنٹ اور اس کی تعیناتی کے نام کی وضاحت کرتا ہے۔ اس معاملے میں، اینڈپوائنٹ کا نام online_endpoint_name متغیر میں محفوظ ہے اور تعیناتی کا نام "demo" ہے۔

- یہ request_file دلیل کے ساتھ اس JSON فائل کا راستہ بتاتا ہے جسے اسکور کرنا ہے۔ اس معاملے میں، فائل ./ultrachat_200k_dataset/sample_score.json ہے۔

- یہ اینڈپوائنٹ سے موصولہ جواب response متغیر میں رکھتا ہے۔

- یہ خام جواب پرنٹ کرتا ہے۔

1. خلاصہ یہ کہ یہ اسکرپٹ Azure Machine Learning میں ایک آن لائن اینڈپوائنٹ کو کال کر رہا ہے تاکہ ایک JSON فائل کو اسکور کیا جا سکے اور جواب پرنٹ کر رہا ہے۔

    ```python
    # Azure Machine Learning میں آن لائن اینڈ پوائنٹ کو کال کریں تاکہ `sample_score.json` فائل کو اسکور کیا جا سکے
    # `workspace_ml_client` آبجیکٹ کی `online_endpoints` پراپرٹی کا `invoke` طریقہ آن لائن اینڈ پوائنٹ کو درخواست بھیجنے اور جواب حاصل کرنے کے لیے استعمال ہوتا ہے
    # `endpoint_name` دلیل اینڈ پوائنٹ کا نام بتاتی ہے، جو `online_endpoint_name` متغیر میں محفوظ ہے
    # `deployment_name` دلیل تعیناتی کا نام بتاتی ہے، جو "demo" ہے
    # `request_file` دلیل JSON فائل کے راستے کی وضاحت کرتی ہے جسے اسکور کیا جانا ہے، یعنی `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # اینڈ پوائنٹ سے موصول خام جواب کو پرنٹ کریں
    print("raw response: \n", response, "\n")
    ```

## 9. آن لائن اینڈپوائنٹ حذف کریں

1. آن لائن اینڈپوائنٹ کو حذف کرنا نہ بھولیں، ورنہ آپ وہ بلنگ میٹر چلاتے رہیں گے جو اینڈپوائنٹ کی استعمال کردہ کمپیوٹ کے لیے ہے۔ یہ Python کوڈ کا ایک سطر Azure Machine Learning میں ایک آن لائن اینڈپوائنٹ کو حذف کر رہا ہے۔ یہ اس کا خلاصہ ہے کہ یہ کیا کرتا ہے:

- یہ workspace_ml_client آبجیکٹ کی online_endpoints پراپرٹی کے begin_delete طریقہ کو کال کرتا ہے۔ یہ طریقہ آن لائن اینڈپوائنٹ کی حذف کاری شروع کرنے کے لیے استعمال ہوتا ہے۔

- یہ name دلیل کے ساتھ اس اینڈپوائنٹ کا نام بتاتا ہے جسے حذف کرنا ہے۔ اس معاملے میں، اینڈپوائنٹ کا نام online_endpoint_name متغیر میں محفوظ ہے۔

- یہ wait طریقہ کو کال کرتا ہے تاکہ حذف کاری کے عمل کے مکمل ہونے تک انتظار کرے۔ یہ ایک blocking آپریشن ہے، یعنی یہ اس وقت تک اسکرپٹ کو آگے بڑھنے نہیں دیتا جب تک حذف کاری مکمل نہ ہو جائے۔

- خلاصہ یہ کہ یہ کوڈ کی لائن Azure Machine Learning میں ایک آن لائن اینڈپوائنٹ کی حذف کاری شروع کر رہی ہے اور عمل کے مکمل ہونے تک انتظار کر رہی ہے۔

    ```python
    # ایزور مشین لرننگ میں آن لائن اینڈپوائنٹ کو حذف کریں
    # `workspace_ml_client` آبجیکٹ کی `online_endpoints` پراپرٹی کے `begin_delete` طریقہ کار کا استعمال آن لائن اینڈپوائنٹ کی حذف کاری شروع کرنے کے لیے کیا جاتا ہے
    # `name` دلیل اینڈپوائنٹ کے نام کی وضاحت کرتی ہے جسے حذف کیا جانا ہے، جو `online_endpoint_name` متغیر میں محفوظ ہے
    # حذف کاری کے مکمل ہونے تک انتظار کرنے کے لیے `wait` طریقہ کار کو کال کیا جاتا ہے۔ یہ ایک بلاکنگ آپریشن ہے، یعنی یہ اسکرپٹ کو جاری رکھنے سے روکے گا جب تک کہ حذف کاری مکمل نہ ہو جائے
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**انذار نوشتہ**:
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم صحت ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں غالب ماخذ تصور کی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ سفارش کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیرات کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->