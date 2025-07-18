<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T06:58:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "ar"
}
-->
## كيفية استخدام مكونات chat-completion من سجل نظام Azure ML لضبط نموذج بدقة

في هذا المثال، سنقوم بضبط نموذج Phi-3-mini-4k-instruct لإكمال محادثة بين شخصين باستخدام مجموعة بيانات ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.ar.png)

سيُظهر المثال كيفية إجراء الضبط الدقيق باستخدام Azure ML SDK وPython ثم نشر النموذج المضبوط إلى نقطة نهاية عبر الإنترنت للاستدلال في الوقت الحقيقي.

### بيانات التدريب

سنستخدم مجموعة بيانات ultrachat_200k. هذه نسخة مُرشحة بشكل كبير من مجموعة بيانات UltraChat وقد استُخدمت لتدريب Zephyr-7B-β، وهو نموذج دردشة متقدم بحجم 7 مليارات معلمة.

### النموذج

سنستخدم نموذج Phi-3-mini-4k-instruct لعرض كيفية قيام المستخدم بضبط نموذج لمهمة إكمال الدردشة. إذا فتحت هذا الدفتر من بطاقة نموذج محددة، تذكر استبدال اسم النموذج المحدد.

### المهام

- اختيار نموذج لضبطه بدقة.
- اختيار واستكشاف بيانات التدريب.
- تكوين مهمة الضبط الدقيق.
- تشغيل مهمة الضبط الدقيق.
- مراجعة مقاييس التدريب والتقييم.
- تسجيل النموذج المضبوط.
- نشر النموذج المضبوط للاستدلال في الوقت الحقيقي.
- تنظيف الموارد.

## 1. إعداد المتطلبات المسبقة

- تثبيت التبعيات
- الاتصال بـ AzureML Workspace. تعرف على المزيد في إعداد مصادقة SDK. استبدل <WORKSPACE_NAME>، <RESOURCE_GROUP> و <SUBSCRIPTION_ID> أدناه.
- الاتصال بسجل نظام azureml
- تعيين اسم تجربة اختياري
- التحقق من وجود أو إنشاء حساب حوسبة.

> [!NOTE]
> المتطلبات: يمكن أن يحتوي عقدة GPU واحدة على عدة بطاقات GPU. على سبيل المثال، في عقدة واحدة من Standard_NC24rs_v3 هناك 4 بطاقات NVIDIA V100، بينما في Standard_NC12s_v3 هناك بطاقتان NVIDIA V100. راجع الوثائق لهذه المعلومات. يتم تعيين عدد بطاقات GPU لكل عقدة في المعامل gpus_per_node أدناه. تعيين هذه القيمة بشكل صحيح يضمن استخدام جميع بطاقات GPU في العقدة. يمكن العثور على SKU الحوسبة الموصى بها للـ GPU هنا وهنا.

### مكتبات Python

قم بتثبيت التبعيات بتشغيل الخلية أدناه. هذه خطوة غير اختيارية إذا كنت تعمل في بيئة جديدة.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### التفاعل مع Azure ML

1. هذا السكربت بلغة Python يُستخدم للتفاعل مع خدمة Azure Machine Learning (Azure ML). فيما يلي شرح لما يقوم به:

    - يستورد الوحدات اللازمة من حزم azure.ai.ml، azure.identity، وazure.ai.ml.entities. كما يستورد وحدة time.

    - يحاول المصادقة باستخدام DefaultAzureCredential()، التي توفر تجربة مصادقة مبسطة لبدء تطوير التطبيقات التي تعمل في سحابة Azure بسرعة. إذا فشل ذلك، ينتقل إلى InteractiveBrowserCredential()، التي توفر نافذة تسجيل دخول تفاعلية.

    - ثم يحاول إنشاء مثيل MLClient باستخدام طريقة from_config، التي تقرأ التكوين من ملف التكوين الافتراضي (config.json). إذا فشل ذلك، ينشئ مثيل MLClient يدوياً بتوفير subscription_id، resource_group_name، وworkspace_name.

    - ينشئ مثيل MLClient آخر، هذه المرة لسجل Azure ML المسمى "azureml". هذا السجل هو المكان الذي تُخزن فيه النماذج، خطوط أنابيب الضبط الدقيق، والبيئات.

    - يحدد experiment_name إلى "chat_completion_Phi-3-mini-4k-instruct".

    - يولد طابع زمني فريد بتحويل الوقت الحالي (بالثواني منذ العصر، كعدد عشري) إلى عدد صحيح ثم إلى سلسلة نصية. يمكن استخدام هذا الطابع الزمني لإنشاء أسماء وإصدارات فريدة.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. اختيار نموذج أساسي لضبطه بدقة

1. نموذج Phi-3-mini-4k-instruct يحتوي على 3.8 مليار معلمة، وهو نموذج مفتوح خفيف الوزن ومتقدم مبني على مجموعات بيانات استُخدمت لنموذج Phi-2. ينتمي النموذج إلى عائلة نماذج Phi-3، والنسخة Mini تأتي بنسختين 4K و128K، وهو طول السياق (بعدد الرموز) الذي يمكنه دعمه. نحتاج لضبط النموذج بدقة لغرضنا المحدد لاستخدامه. يمكنك تصفح هذه النماذج في كتالوج النماذج في AzureML Studio، مع تصفية حسب مهمة إكمال الدردشة. في هذا المثال، نستخدم نموذج Phi-3-mini-4k-instruct. إذا فتحت هذا الدفتر لنموذج مختلف، استبدل اسم النموذج والإصدار وفقاً لذلك.

    > [!NOTE]
    > خاصية معرف النموذج (model id) للنموذج. سيتم تمريرها كمدخل لمهمة الضبط الدقيق. وهي متاحة أيضاً كحقل Asset ID في صفحة تفاصيل النموذج في كتالوج نماذج AzureML Studio.

2. هذا السكربت بلغة Python يتفاعل مع خدمة Azure Machine Learning (Azure ML). فيما يلي شرح لما يقوم به:

    - يحدد model_name إلى "Phi-3-mini-4k-instruct".

    - يستخدم طريقة get من خاصية models لكائن registry_ml_client لاسترجاع أحدث إصدار من النموذج بالاسم المحدد من سجل Azure ML. تُستدعى طريقة get بمعاملين: اسم النموذج ووسم يحدد أنه يجب استرجاع أحدث إصدار.

    - يطبع رسالة على وحدة التحكم تشير إلى اسم، إصدار، ومعرف النموذج الذي سيُستخدم للضبط الدقيق. تُستخدم طريقة format للسلسلة النصية لإدخال الاسم، الإصدار، والمعرف في الرسالة. يتم الوصول إلى هذه الخصائص من كائن foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. إنشاء حساب حوسبة لاستخدامه مع المهمة

تعمل مهمة الضبط الدقيق فقط مع حوسبة GPU. حجم الحوسبة يعتمد على حجم النموذج وفي معظم الحالات يصبح من الصعب تحديد الحوسبة المناسبة للمهمة. في هذه الخلية، نرشد المستخدم لاختيار الحوسبة المناسبة للمهمة.

> [!NOTE]
> الحواسيب المدرجة أدناه تعمل بأكثر التكوينات تحسيناً. أي تغييرات في التكوين قد تؤدي إلى خطأ Cuda Out Of Memory. في مثل هذه الحالات، حاول ترقية الحوسبة إلى حجم أكبر.

> [!NOTE]
> عند اختيار compute_cluster_size أدناه، تأكد من توفر الحوسبة في مجموعة الموارد الخاصة بك. إذا لم تكن حوسبة معينة متوفرة، يمكنك تقديم طلب للحصول على حق الوصول إلى موارد الحوسبة.

### التحقق من دعم النموذج للضبط الدقيق

1. هذا السكربت بلغة Python يتفاعل مع نموذج Azure Machine Learning (Azure ML). فيما يلي شرح لما يقوم به:

    - يستورد وحدة ast، التي توفر وظائف لمعالجة أشجار قواعد النحو المجردة للغة Python.

    - يتحقق مما إذا كان كائن foundation_model (الذي يمثل نموذجاً في Azure ML) يحتوي على وسم باسم finetune_compute_allow_list. الأوسمة في Azure ML هي أزواج مفتاح-قيمة يمكنك إنشاؤها واستخدامها لتصفية وفرز النماذج.

    - إذا كان وسم finetune_compute_allow_list موجوداً، يستخدم الدالة ast.literal_eval لتحليل قيمة الوسم (نص) بأمان إلى قائمة Python. تُعيّن هذه القائمة إلى المتغير computes_allow_list. ثم يطبع رسالة تشير إلى أنه يجب إنشاء حوسبة من القائمة.

    - إذا لم يكن وسم finetune_compute_allow_list موجوداً، يعين computes_allow_list إلى None ويطبع رسالة تشير إلى أن الوسم غير موجود ضمن أوسمة النموذج.

    - باختصار، هذا السكربت يتحقق من وجود وسم معين في بيانات النموذج الوصفية، ويحول قيمة الوسم إلى قائمة إذا وجدت، ويقدم ملاحظات للمستخدم بناءً على ذلك.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### التحقق من حالة حساب الحوسبة

1. هذا السكربت بلغة Python يتفاعل مع خدمة Azure Machine Learning (Azure ML) ويجري عدة فحوصات على حساب حوسبة. فيما يلي شرح لما يقوم به:

    - يحاول استرجاع حساب الحوسبة بالاسم المخزن في compute_cluster من مساحة عمل Azure ML. إذا كانت حالة توفير الحوسبة "failed"، يرفع استثناء ValueError.

    - يتحقق مما إذا كانت computes_allow_list ليست None. إذا لم تكن كذلك، يحول جميع أحجام الحوسبة في القائمة إلى أحرف صغيرة ويتحقق مما إذا كان حجم حساب الحوسبة الحالي موجوداً في القائمة. إذا لم يكن كذلك، يرفع استثناء ValueError.

    - إذا كانت computes_allow_list هي None، يتحقق مما إذا كان حجم حساب الحوسبة موجوداً في قائمة أحجام VM الخاصة بـ GPU غير المدعومة. إذا كان كذلك، يرفع استثناء ValueError.

    - يسترجع قائمة بكل أحجام الحوسبة المتاحة في مساحة العمل. ثم يتكرر على هذه القائمة، ولكل حجم حوسبة، يتحقق مما إذا كان اسمه يطابق حجم حساب الحوسبة الحالي. إذا كان كذلك، يسترجع عدد بطاقات GPU لذلك الحجم ويعين gpu_count_found إلى True.

    - إذا كانت gpu_count_found True، يطبع عدد بطاقات GPU في حساب الحوسبة. إذا كانت False، يرفع استثناء ValueError.

    - باختصار، هذا السكربت يجري عدة فحوصات على حساب حوسبة في مساحة عمل Azure ML، بما في ذلك حالة التوفير، حجمه مقابل قائمة السماح أو المنع، وعدد بطاقات GPU التي يحتويها.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. اختيار مجموعة البيانات لضبط النموذج بدقة

1. نستخدم مجموعة بيانات ultrachat_200k. تحتوي مجموعة البيانات على أربعة تقسيمات، مناسبة للضبط الدقيق الخاضع للإشراف (sft). الترتيب التوليدي (gen). عدد الأمثلة لكل تقسيم موضح كما يلي:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. الخلايا التالية تعرض تحضير بيانات أساسي للضبط الدقيق:

### عرض بعض صفوف البيانات

نريد أن يعمل هذا العينة بسرعة، لذا نحفظ ملفات train_sft وtest_sft التي تحتوي على 5% من الصفوف المفلترة مسبقاً. هذا يعني أن النموذج المضبوط سيكون بدقة أقل، لذا لا ينبغي استخدامه في تطبيقات العالم الحقيقي.
يُستخدم السكربت download-dataset.py لتحميل مجموعة بيانات ultrachat_200k وتحويلها إلى صيغة يمكن لمكون خط أنابيب الضبط الدقيق استهلاكها. وبما أن مجموعة البيانات كبيرة، فنحن هنا نمتلك فقط جزءاً منها.

1. تشغيل السكربت أدناه يقوم فقط بتحميل 5% من البيانات. يمكن زيادة هذه النسبة بتغيير معامل dataset_split_pc إلى النسبة المرغوبة.

    > [!NOTE]
    > بعض نماذج اللغة لها رموز لغات مختلفة، لذا يجب أن تعكس أسماء الأعمدة في مجموعة البيانات ذلك.

1. هنا مثال على شكل البيانات
تُخزن مجموعة بيانات إكمال الدردشة بصيغة parquet مع كل إدخال يستخدم المخطط التالي:

    - هذا مستند JSON (JavaScript Object Notation)، وهو صيغة شائعة لتبادل البيانات. ليس كوداً قابلاً للتنفيذ، بل طريقة لتخزين ونقل البيانات. فيما يلي شرح هيكله:

    - "prompt": هذا المفتاح يحمل قيمة نصية تمثل مهمة أو سؤال موجه لمساعد ذكي.

    - "messages": هذا المفتاح يحمل مصفوفة من الكائنات. كل كائن يمثل رسالة في محادثة بين مستخدم ومساعد ذكي. كل كائن رسالة يحتوي على مفتاحين:

    - "content": هذا المفتاح يحمل قيمة نصية تمثل محتوى الرسالة.
    - "role": هذا المفتاح يحمل قيمة نصية تمثل دور الكيان الذي أرسل الرسالة. يمكن أن يكون "user" أو "assistant".
    - "prompt_id": هذا المفتاح يحمل قيمة نصية تمثل معرف فريد للموجه.

1. في هذا المستند JSON المحدد، تمثل المحادثة حيث يطلب المستخدم من المساعد الذكي إنشاء بطل لقصة ديستوبية. يرد المساعد، ثم يطلب المستخدم المزيد من التفاصيل. يوافق المساعد على تقديم المزيد من التفاصيل. ترتبط المحادثة كلها بمعرف موجه محدد.

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

### تحميل البيانات

1. هذا السكربت بلغة Python يُستخدم لتحميل مجموعة بيانات باستخدام سكربت مساعد اسمه download-dataset.py. فيما يلي شرح لما يقوم به:

    - يستورد وحدة os، التي توفر طريقة محمولة لاستخدام وظائف نظام التشغيل.

    - يستخدم دالة os.system لتشغيل سكربت download-dataset.py في الصدفة مع معاملات سطر الأوامر المحددة. المعاملات تحدد مجموعة البيانات التي سيتم تحميلها (HuggingFaceH4/ultrachat_200k)، الدليل الذي سيتم التحميل إليه (ultrachat_200k_dataset)، ونسبة تقسيم مجموعة البيانات (5). تعيد دالة os.system حالة الخروج من الأمر الذي نفذته؛ تُخزن هذه الحالة في المتغير exit_status.

    - يتحقق مما إذا كانت exit_status ليست 0. في أنظمة التشغيل الشبيهة بـ Unix، تعني حالة خروج 0 عادة نجاح الأمر، وأي رقم آخر يشير إلى خطأ. إذا لم تكن exit_status 0، يرفع استثناء مع رسالة تشير إلى وجود خطأ في تحميل مجموعة البيانات.

    - باختصار، هذا السكربت يشغل أمر تحميل مجموعة بيانات باستخدام سكربت مساعد، ويرفع استثناء إذا فشل الأمر.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### تحميل البيانات في DataFrame

1. هذا السكربت بلغة Python يقوم بتحميل ملف JSON Lines إلى DataFrame باستخدام pandas ويعرض أول 5 صفوف. فيما يلي شرح لما يقوم به:

    - يستورد مكتبة pandas، وهي مكتبة قوية لمعالجة وتحليل البيانات.

    - يحدد الحد الأقصى لعرض الأعمدة في خيارات عرض pandas إلى 0. هذا يعني أن النص الكامل لكل عمود سيُعرض بدون اقتطاع عند طباعة DataFrame. 

    - يستخدم دالة pd.read_json لتحميل ملف train_sft.jsonl من دليل ultrachat_200k_dataset إلى DataFrame. الوسيط lines=True يشير إلى أن الملف بصيغة JSON Lines، حيث كل سطر هو كائن JSON منفصل.
- يستخدم طريقة head لعرض أول 5 صفوف من DataFrame. إذا كان DataFrame يحتوي على أقل من 5 صفوف، فسيعرضها كلها.

- باختصار، يقوم هذا السكربت بتحميل ملف JSON Lines إلى DataFrame ويعرض أول 5 صفوف مع النص الكامل للأعمدة.

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. إرسال مهمة الضبط الدقيق باستخدام النموذج والبيانات كمدخلات

أنشئ المهمة التي تستخدم مكون خط أنابيب chat-completion. تعرّف على المزيد حول جميع المعاملات المدعومة للضبط الدقيق.

### تعريف معلمات الضبط الدقيق

1. يمكن تصنيف معلمات الضبط الدقيق إلى فئتين - معلمات التدريب، ومعلمات التحسين

1. تحدد معلمات التدريب جوانب التدريب مثل -

    - المحسن، وجدول التوقيت المستخدم
    - المقياس الذي يتم تحسينه أثناء الضبط الدقيق
    - عدد خطوات التدريب وحجم الدُفعة وهكذا
    - تساعد معلمات التحسين في تحسين استخدام ذاكرة GPU واستخدام موارد الحوسبة بشكل فعال.

1. فيما يلي بعض المعلمات التي تنتمي إلى هذه الفئة. تختلف معلمات التحسين لكل نموذج ويتم تضمينها مع النموذج للتعامل مع هذه الاختلافات.

    - تفعيل deepspeed و LoRA
    - تفعيل التدريب بدقة مختلطة
    - تفعيل التدريب متعدد العقد

> [!NOTE]
> قد يؤدي الضبط الدقيق الموجه إلى فقدان التوافق أو النسيان الكارثي. نوصي بالتحقق من هذه المشكلة وتشغيل مرحلة التوافق بعد الانتهاء من الضبط الدقيق.

### معلمات الضبط الدقيق

1. يقوم هذا السكربت بلغة بايثون بإعداد معلمات لضبط نموذج تعلم آلي. إليك تفصيل لما يقوم به:

    - يحدد معلمات التدريب الافتراضية مثل عدد العصور التدريبية، أحجام الدُفعات للتدريب والتقييم، معدل التعلم، ونوع جدول معدل التعلم.

    - يحدد معلمات التحسين الافتراضية مثل ما إذا كان سيتم تطبيق Layer-wise Relevance Propagation (LoRa) و DeepSpeed، ومرحلة DeepSpeed.

    - يجمع معلمات التدريب والتحسين في قاموس واحد يسمى finetune_parameters.

    - يتحقق مما إذا كان foundation_model يحتوي على معلمات افتراضية خاصة بالنموذج. إذا كان كذلك، يطبع رسالة تحذير ويحدث قاموس finetune_parameters بهذه المعلمات الخاصة بالنموذج. تُستخدم الدالة ast.literal_eval لتحويل المعلمات الخاصة بالنموذج من نص إلى قاموس بايثون.

    - يطبع مجموعة المعلمات النهائية للضبط الدقيق التي ستُستخدم في التشغيل.

    - باختصار، يقوم هذا السكربت بإعداد وعرض معلمات الضبط الدقيق لنموذج تعلم آلي، مع إمكانية تجاوز المعلمات الافتراضية بمعلمات خاصة بالنموذج.

```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### خط أنابيب التدريب

1. يقوم هذا السكربت بلغة بايثون بتعريف دالة لإنشاء اسم عرض لخط أنابيب تدريب تعلم آلي، ثم يستدعي هذه الدالة لإنشاء وطباعة اسم العرض. إليك تفصيل لما يقوم به:

1. تم تعريف دالة get_pipeline_display_name. هذه الدالة تنشئ اسم عرض بناءً على معلمات مختلفة تتعلق بخط أنابيب التدريب.

1. داخل الدالة، يتم حساب حجم الدُفعة الكلي بضرب حجم الدُفعة لكل جهاز، وعدد خطوات تراكم التدرج، وعدد وحدات GPU لكل عقدة، وعدد العقد المستخدمة للضبط الدقيق.

1. يسترجع معلمات أخرى مثل نوع جدول معدل التعلم، ما إذا كان DeepSpeed مفعلًا، مرحلة DeepSpeed، ما إذا كان Layer-wise Relevance Propagation (LoRa) مفعلًا، الحد الأقصى لعدد نقاط التحقق من النموذج التي سيتم الاحتفاظ بها، والطول الأقصى للتسلسل.

1. ينشئ سلسلة نصية تتضمن كل هذه المعلمات مفصولة بشرطات. إذا كان DeepSpeed أو LoRa مفعلًا، تتضمن السلسلة "ds" متبوعة بمرحلة DeepSpeed، أو "lora" على التوالي. وإذا لم تكن مفعلة، تتضمن "nods" أو "nolora" على التوالي.

1. تعيد الدالة هذه السلسلة النصية، والتي تُستخدم كاسم عرض لخط أنابيب التدريب.

1. بعد تعريف الدالة، يتم استدعاؤها لإنشاء اسم العرض، ثم يتم طباعته.

1. باختصار، يقوم هذا السكربت بإنشاء اسم عرض لخط أنابيب تدريب تعلم آلي بناءً على معلمات مختلفة، ثم يطبع هذا الاسم.

```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
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
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### تكوين خط الأنابيب

يقوم هذا السكربت بلغة بايثون بتعريف وتكوين خط أنابيب تعلم آلي باستخدام Azure Machine Learning SDK. إليك تفصيل لما يقوم به:

1. يستورد الوحدات اللازمة من Azure AI ML SDK.

1. يستدعي مكون خط أنابيب باسم "chat_completion_pipeline" من السجل.

1. يعرف مهمة خط أنابيب باستخدام المزخرف `@pipeline` والدالة `create_pipeline`. يتم تعيين اسم خط الأنابيب إلى `pipeline_display_name`.

1. داخل دالة `create_pipeline`، يقوم بتهيئة مكون خط الأنابيب المستدعى مع معلمات مختلفة، بما في ذلك مسار النموذج، مجموعات الحوسبة لمراحل مختلفة، تقسيمات مجموعة البيانات للتدريب والاختبار، عدد وحدات GPU المستخدمة للضبط الدقيق، ومعلمات الضبط الدقيق الأخرى.

1. يربط مخرجات مهمة الضبط الدقيق بمخرجات مهمة خط الأنابيب. يتم ذلك لتسهيل تسجيل النموذج المضبوط، وهو مطلوب لنشر النموذج على نقطة نهاية عبر الإنترنت أو دفعة.

1. ينشئ نسخة من خط الأنابيب عن طريق استدعاء دالة `create_pipeline`.

1. يضبط إعداد `force_rerun` لخط الأنابيب إلى `True`، مما يعني أنه لن يتم استخدام النتائج المخزنة من المهام السابقة.

1. يضبط إعداد `continue_on_step_failure` لخط الأنابيب إلى `False`، مما يعني أن خط الأنابيب سيتوقف إذا فشلت أي خطوة.

1. باختصار، يقوم هذا السكربت بتعريف وتكوين خط أنابيب تعلم آلي لمهمة إكمال الدردشة باستخدام Azure Machine Learning SDK.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### إرسال المهمة

1. يقوم هذا السكربت بلغة بايثون بإرسال مهمة خط أنابيب تعلم آلي إلى مساحة عمل Azure Machine Learning ثم ينتظر حتى تكتمل المهمة. إليك تفصيل لما يقوم به:

    - يستدعي طريقة create_or_update لكائن jobs في workspace_ml_client لإرسال مهمة خط الأنابيب. يتم تحديد خط الأنابيب الذي سيتم تشغيله بواسطة pipeline_object، والتجربة التي تُشغل تحتها المهمة بواسطة experiment_name.

    - ثم يستدعي طريقة stream لكائن jobs في workspace_ml_client للانتظار حتى تكتمل مهمة خط الأنابيب. يتم تحديد المهمة التي ينتظرها بواسطة خاصية name لكائن pipeline_job.

    - باختصار، يقوم هذا السكربت بإرسال مهمة خط أنابيب تعلم آلي إلى مساحة عمل Azure Machine Learning، ثم ينتظر حتى تكتمل المهمة.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. تسجيل النموذج المضبوط في مساحة العمل

سنسجل النموذج من مخرجات مهمة الضبط الدقيق. هذا سيتتبع العلاقة بين النموذج المضبوط ومهمة الضبط الدقيق. كما تتتبع مهمة الضبط الدقيق العلاقة مع النموذج الأساسي، والبيانات، وكود التدريب.

### تسجيل نموذج التعلم الآلي

1. يقوم هذا السكربت بلغة بايثون بتسجيل نموذج تعلم آلي تم تدريبه في خط أنابيب Azure Machine Learning. إليك تفصيل لما يقوم به:

    - يستورد الوحدات اللازمة من Azure AI ML SDK.

    - يتحقق مما إذا كان مخرج trained_model متاحًا من مهمة خط الأنابيب عن طريق استدعاء طريقة get لكائن jobs في workspace_ml_client والوصول إلى خاصية outputs.

    - ينشئ مسارًا للنموذج المدرب عن طريق تنسيق سلسلة نصية باستخدام اسم مهمة خط الأنابيب واسم المخرج ("trained_model").

    - يحدد اسمًا للنموذج المضبوط بإضافة "-ultrachat-200k" إلى اسم النموذج الأصلي واستبدال أي شرطات مائلة بشرطات عادية.

    - يستعد لتسجيل النموذج بإنشاء كائن Model مع معلمات مختلفة، بما في ذلك مسار النموذج، نوع النموذج (نموذج MLflow)، اسم وإصدار النموذج، ووصف النموذج.

    - يسجل النموذج عن طريق استدعاء طريقة create_or_update لكائن models في workspace_ml_client مع كائن Model كوسيط.

    - يطبع النموذج المسجل.

1. باختصار، يقوم هذا السكربت بتسجيل نموذج تعلم آلي تم تدريبه في خط أنابيب Azure Machine Learning.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. نشر النموذج المضبوط إلى نقطة نهاية عبر الإنترنت

توفر نقاط النهاية عبر الإنترنت واجهة REST API دائمة يمكن استخدامها للتكامل مع التطبيقات التي تحتاج إلى استخدام النموذج.

### إدارة نقطة النهاية

1. يقوم هذا السكربت بلغة بايثون بإنشاء نقطة نهاية عبر الإنترنت مُدارة في Azure Machine Learning لنموذج مسجل. إليك تفصيل لما يقوم به:

    - يستورد الوحدات اللازمة من Azure AI ML SDK.

    - يحدد اسمًا فريدًا لنقطة النهاية عبر الإنترنت بإضافة طابع زمني إلى السلسلة "ultrachat-completion-".

    - يستعد لإنشاء نقطة النهاية عبر الإنترنت بإنشاء كائن ManagedOnlineEndpoint مع معلمات مختلفة، بما في ذلك اسم نقطة النهاية، وصف نقطة النهاية، ووضع المصادقة ("key").

    - ينشئ نقطة النهاية عبر الإنترنت عن طريق استدعاء طريقة begin_create_or_update لكائن workspace_ml_client مع كائن ManagedOnlineEndpoint كوسيط. ثم ينتظر حتى تكتمل عملية الإنشاء عن طريق استدعاء طريقة wait.

1. باختصار، يقوم هذا السكربت بإنشاء نقطة نهاية عبر الإنترنت مُدارة في Azure Machine Learning لنموذج مسجل.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> يمكنك العثور هنا على قائمة SKU المدعومة للنشر - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### نشر نموذج التعلم الآلي

1. يقوم هذا السكربت بلغة بايثون بنشر نموذج تعلم آلي مسجل إلى نقطة نهاية عبر الإنترنت مُدارة في Azure Machine Learning. إليك تفصيل لما يقوم به:

    - يستورد وحدة ast، التي توفر دوال لمعالجة شجرة القواعد النحوية المجردة للبايثون.

    - يحدد نوع المثيل للنشر إلى "Standard_NC6s_v3".

    - يتحقق مما إذا كانت العلامة inference_compute_allow_list موجودة في foundation model. إذا كانت موجودة، يحول قيمة العلامة من نص إلى قائمة بايثون ويعينها إلى inference_computes_allow_list. إذا لم تكن موجودة، يعين inference_computes_allow_list إلى None.

    - يتحقق مما إذا كان نوع المثيل المحدد موجودًا في قائمة السماح. إذا لم يكن كذلك، يطبع رسالة تطلب من المستخدم اختيار نوع مثيل من قائمة السماح.

    - يستعد لإنشاء النشر بإنشاء كائن ManagedOnlineDeployment مع معلمات مختلفة، بما في ذلك اسم النشر، اسم نقطة النهاية، معرف النموذج، نوع وعدد المثيلات، إعدادات فحص الحيوية، وإعدادات الطلب.

    - ينشئ النشر عن طريق استدعاء طريقة begin_create_or_update لكائن workspace_ml_client مع كائن ManagedOnlineDeployment كوسيط. ثم ينتظر حتى تكتمل عملية الإنشاء عن طريق استدعاء طريقة wait.

    - يضبط حركة المرور لنقطة النهاية لتوجيه 100% من الحركة إلى نشر "demo".

    - يحدث نقطة النهاية عن طريق استدعاء طريقة begin_create_or_update لكائن workspace_ml_client مع كائن endpoint كوسيط. ثم ينتظر حتى تكتمل عملية التحديث عن طريق استدعاء طريقة result.

1. باختصار، يقوم هذا السكربت بنشر نموذج تعلم آلي مسجل إلى نقطة نهاية عبر الإنترنت مُدارة في Azure Machine Learning.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. اختبار نقطة النهاية ببيانات عينة

سنجلب بعض البيانات العينة من مجموعة بيانات الاختبار ونرسلها إلى نقطة النهاية عبر الإنترنت للاستدلال. ثم سنعرض التسميات المتوقعة جنبًا إلى جنب مع التسميات الحقيقية.

### قراءة النتائج

1. يقوم هذا السكربت بلغة بايثون بقراءة ملف JSON Lines إلى pandas DataFrame، وأخذ عينة عشوائية، وإعادة تعيين الفهرس. إليك تفصيل لما يقوم به:

    - يقرأ الملف ./ultrachat_200k_dataset/test_gen.jsonl إلى pandas DataFrame. تُستخدم دالة read_json مع الوسيط lines=True لأن الملف بصيغة JSON Lines، حيث كل سطر هو كائن JSON منفصل.

    - يأخذ عينة عشوائية من صف واحد من DataFrame. تُستخدم دالة sample مع الوسيط n=1 لتحديد عدد الصفوف العشوائية المختارة.

    - يعيد تعيين فهرس DataFrame. تُستخدم دالة reset_index مع الوسيط drop=True لحذف الفهرس الأصلي واستبداله بفهرس جديد من أعداد صحيحة افتراضية.

    - يعرض أول صفين من DataFrame باستخدام دالة head مع الوسيط 2. ولكن بما أن DataFrame يحتوي على صف واحد فقط بعد أخذ العينة، فسيعرض هذا الصف فقط.

1. باختصار، يقوم هذا السكربت بقراءة ملف JSON Lines إلى pandas DataFrame، وأخذ عينة عشوائية من صف واحد، وإعادة تعيين الفهرس، وعرض الصف الأول.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### إنشاء كائن JSON

1. يقوم هذا السكربت بلغة بايثون بإنشاء كائن JSON بمعلمات محددة وحفظه في ملف. إليك تفصيل لما يقوم به:

    - يستورد وحدة json، التي توفر دوال للعمل مع بيانات JSON.

    - ينشئ قاموس parameters يحتوي على مفاتيح وقيم تمثل معلمات لنموذج تعلم آلي. المفاتيح هي "temperature"، "top_p"، "do_sample"، و "max_new_tokens"، والقيم المقابلة لها هي 0.6، 0.9، True، و 200 على التوالي.

    - ينشئ قاموسًا آخر test_json يحتوي على مفتاحين: "input_data" و "params". قيمة "input_data" هي قاموس آخر يحتوي على المفاتيح "input_string" و "parameters". قيمة "input_string" هي قائمة تحتوي على الرسالة الأولى من DataFrame test_df. قيمة "parameters" هي القاموس parameters الذي تم إنشاؤه سابقًا. قيمة "params" هي قاموس فارغ.
- يفتح ملفًا باسم sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### استدعاء نقطة النهاية

1. يقوم هذا السكربت بلغة بايثون باستدعاء نقطة نهاية عبر الإنترنت في Azure Machine Learning لتقييم ملف JSON. إليك شرح لما يقوم به:

    - يستدعي دالة invoke الخاصة بخصيصة online_endpoints لكائن workspace_ml_client. تُستخدم هذه الدالة لإرسال طلب إلى نقطة نهاية عبر الإنترنت والحصول على استجابة.

    - يحدد اسم نقطة النهاية واسم النشر باستخدام الوسيطين endpoint_name و deployment_name. في هذه الحالة، يتم تخزين اسم نقطة النهاية في المتغير online_endpoint_name واسم النشر هو "demo".

    - يحدد مسار ملف JSON الذي سيتم تقييمه باستخدام الوسيط request_file. في هذه الحالة، الملف هو ./ultrachat_200k_dataset/sample_score.json.

    - يخزن الاستجابة من نقطة النهاية في المتغير response.

    - يطبع الاستجابة الخام.

1. باختصار، يقوم هذا السكربت باستدعاء نقطة نهاية عبر الإنترنت في Azure Machine Learning لتقييم ملف JSON ويطبع الاستجابة.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. حذف نقطة النهاية عبر الإنترنت

1. لا تنس حذف نقطة النهاية عبر الإنترنت، وإلا ستستمر فاتورة الاستخدام في العمل على الموارد الحاسوبية المستخدمة من قبل نقطة النهاية. هذا السطر من كود بايثون يقوم بحذف نقطة نهاية عبر الإنترنت في Azure Machine Learning. إليك شرح لما يقوم به:

    - يستدعي دالة begin_delete الخاصة بخصيصة online_endpoints لكائن workspace_ml_client. تُستخدم هذه الدالة لبدء عملية حذف نقطة نهاية عبر الإنترنت.

    - يحدد اسم نقطة النهاية التي سيتم حذفها باستخدام الوسيط name. في هذه الحالة، يتم تخزين اسم نقطة النهاية في المتغير online_endpoint_name.

    - يستدعي دالة wait للانتظار حتى تكتمل عملية الحذف. هذه عملية حظر، مما يعني أنها تمنع السكربت من الاستمرار حتى تنتهي عملية الحذف.

    - باختصار، يبدأ هذا السطر من الكود عملية حذف نقطة نهاية عبر الإنترنت في Azure Machine Learning وينتظر حتى تكتمل العملية.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.