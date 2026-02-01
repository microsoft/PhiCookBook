## Azure ML சிஸ்டம் பதிவேட்டிலிருந்து chat-completion கூறுகளை பயன்படுத்தி ஒரு மாதிரியை நயம்கொண்டு பயன்படுத்துவது எப்படி

இந்த எடுத்துக்காட்டில், இரண்டு நபர்களுக்கிடையிலான உரையாடலை முடிக்க Phi-3-mini-4k-instruct மாதிரியை ultrachat_200k தரவுத்தொகுப்பைப் பயன்படுத்தி நயம்கொண்டு பயன்படுத்துவோம்.

![MLFineTune](../../../../imgs/03/ft/MLFineTune.png)

இந்த எடுத்துக்காட்டில் Azure ML SDK மற்றும் Python-ஐப் பயன்படுத்தி நயம்கொண்டு பயன்படுத்துவது மற்றும் நயம்கொண்ட மாதிரியை நேரடி முடிவுகளுக்காக ஆன்லைன் முடிவிடத்தில் வெளியிடுவது எப்படி என்பதை காண்பிக்கிறது.

### பயிற்சி தரவுகள்

நாம் ultrachat_200k தரவுத்தொகுப்பைப் பயன்படுத்துவோம். இது UltraChat தரவுத்தொகுப்பின் மிகக் கடுமையாக வடிகட்டப்பட்ட பதிப்பாகும் மற்றும் Zephyr-7B-β, ஒரு முன்னணி 7b உரையாடல் மாதிரியை பயிற்சி செய்ய பயன்படுத்தப்பட்டது.

### மாதிரி

நாம் Phi-3-mini-4k-instruct மாதிரியைப் பயன்படுத்தி, chat-completion பணிக்காக ஒரு மாதிரியை நயம்கொண்டு பயன்படுத்துவது எப்படி என்பதை காண்பிக்கிறோம். நீங்கள் இந்த நோட்புக்கை ஒரு குறிப்பிட்ட மாதிரி கார்டிலிருந்து திறந்திருந்தால், குறிப்பிட்ட மாதிரி பெயரை மாற்ற மறக்க வேண்டாம்.

### பணிகள்

- நயம்கொண்டு பயன்படுத்த ஒரு மாதிரியைத் தேர்ந்தெடுக்கவும்.
- பயிற்சி தரவுகளைத் தேர்ந்தெடுத்து ஆராயவும்.
- நயம்கொண்டு பயன்படுத்தும் வேலைக்கு அமைப்புகளைச் செய்யவும்.
- நயம்கொண்டு பயன்படுத்தும் வேலைகளை இயக்கவும்.
- பயிற்சி மற்றும் மதிப்பீட்டு அளவுகோல்களை மதிப்பாய்வு செய்யவும்.
- நயம்கொண்ட மாதிரியைப் பதிவு செய்யவும்.
- நேரடி முடிவுகளுக்காக நயம்கொண்ட மாதிரியை வெளியிடவும்.
- வளங்களை சுத்தம் செய்யவும்.

## 1. முன் தேவைகளை அமைத்தல்

- தேவையானவை நிறுவவும்
- AzureML Workspace-க்கு இணைக்கவும். SDK அங்கீகாரத்தை அமைப்பது பற்றி மேலும் அறியவும். கீழே உள்ள <WORKSPACE_NAME>, <RESOURCE_GROUP> மற்றும் <SUBSCRIPTION_ID> ஐ மாற்றவும்.
- azureml system registry-க்கு இணைக்கவும்
- விருப்பமான ஒரு பரிசோதனை பெயரை அமைக்கவும்
- கணினியை சரிபார்க்கவும் அல்லது உருவாக்கவும்.

> [!NOTE]
> தேவைகள்: ஒரு GPU நோடில் பல GPU கார்டுகள் இருக்கலாம். உதாரணமாக, Standard_NC24rs_v3 இன் ஒரு நோடில் 4 NVIDIA V100 GPUகள் உள்ளன, Standard_NC12s_v3 இல் 2 NVIDIA V100 GPUகள் உள்ளன. இந்த தகவலுக்கான ஆவணங்களைப் பார்க்கவும். கீழே உள்ள gpus_per_node அளவுருவில் ஒரு நோடின் GPU கார்டுகளின் எண்ணிக்கை அமைக்கப்பட்டுள்ளது. இந்த மதிப்பை சரியாக அமைத்தால், நோடில் உள்ள அனைத்து GPUகளையும் பயன்படுத்த முடியும். பரிந்துரைக்கப்பட்ட GPU கணினி SKUs இங்கே மற்றும் இங்கே காணலாம்.

### Python நூலகங்கள்

பின்வரும் செல் இயக்குவதன் மூலம் தேவையானவற்றை நிறுவவும். புதிய சூழலில் இயக்கும்போது இது ஒரு விருப்பமான படி அல்ல.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML உடன் தொடர்பு கொள்ளுதல்

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning (Azure ML) சேவையுடன் தொடர்பு கொள்ள பயன்படுத்தப்படுகிறது. இதன் செயல்பாடுகள்:

    - azure.ai.ml, azure.identity மற்றும் azure.ai.ml.entities தொகுப்புகளில் இருந்து தேவையான மாட்யூல்களை இறக்குமதி செய்கிறது. மேலும் time மாட்யூலையும் இறக்குமதி செய்கிறது.

    - DefaultAzureCredential() மூலம் அங்கீகாரத்தை முயற்சிக்கிறது, இது Azure மேகத்தில் செயல்பட எளிய அனுபவத்தை வழங்குகிறது. இது தோல்வியடைந்தால், InteractiveBrowserCredential() மூலம் ஒரு இடைமுக உள்நுழைவு உத்தரவாதத்தை வழங்குகிறது.

    - பின்னர், from_config முறை மூலம் MLClient உதாரணத்தை உருவாக்க முயற்சிக்கிறது, இது இயல்புநிலை கட்டமைப்பு கோப்பிலிருந்து (config.json) தகவல்களைப் படிக்கிறது. இது தோல்வியடைந்தால், subscription_id, resource_group_name மற்றும் workspace_name ஆகியவற்றை கையால் வழங்கி MLClient உதாரணத்தை உருவாக்குகிறது.

    - "azureml" என்ற Azure ML பதிவேட்டிற்கான மற்றொரு MLClient உதாரணத்தை உருவாக்குகிறது. இந்த பதிவேட்டில் மாதிரிகள், நயம்கொண்டு பயன்படுத்தும் குழாய்கள் மற்றும் சூழல்கள் சேமிக்கப்படுகின்றன.

    - experiment_name ஐ "chat_completion_Phi-3-mini-4k-instruct" என அமைக்கிறது.

    - தற்போதைய நேரத்தை (இருப்பிடத்திலிருந்து விலகிய வினாடிகளில், ஒரு மிதமான புள்ளி எண்ணாக) முழு எண்ணாக மாற்றி பின்னர் ஒரு சரியாக மாற்றுவதன் மூலம் ஒரு தனித்துவமான நேரத்தை உருவாக்குகிறது. இந்த நேரத்தை தனித்துவமான பெயர்கள் மற்றும் பதிப்புகளை உருவாக்க பயன்படுத்தலாம்.

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

## 2. நயம்கொண்டு பயன்படுத்த ஒரு அடிப்படை மாதிரியைத் தேர்ந்தெடுக்கவும்

1. Phi-3-mini-4k-instruct என்பது 3.8B அளவிலான, எளிய, முன்னணி திறந்த மாதிரி ஆகும், இது Phi-2 க்கான தரவுத்தொகுப்புகளை அடிப்படையாகக் கொண்டது. இந்த மாதிரி Phi-3 மாதிரி குடும்பத்தைச் சேர்ந்தது, மேலும் Mini பதிப்பு 4K மற்றும் 128K என இரண்டு மாறுபாடுகளில் வருகிறது, இது (தொகுதிகளில்) ஆதாரநிலையின் நீளத்தை ஆதரிக்க முடியும். இந்த மாதிரியை நம் குறிப்பிட்ட நோக்கத்திற்காக நயம்கொண்டு பயன்படுத்த வேண்டும். இந்த எடுத்துக்காட்டில், நாம் Phi-3-mini-4k-instruct மாதிரியைப் பயன்படுத்துகிறோம். நீங்கள் இந்த நோட்புக்கை வேறு மாதிரிக்காக திறந்திருந்தால், மாதிரி பெயர் மற்றும் பதிப்பை அதற்கேற்ப மாற்றவும்.

    > [!NOTE]
    > மாதிரியின் model id சொத்து. இது நயம்கொண்டு பயன்படுத்தும் வேலைக்கு உள்ளீடாக அனுப்பப்படும். இது AzureML Studio Model Catalog இல் Asset ID புலமாகவும் கிடைக்கிறது.

2. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning (Azure ML) சேவையுடன் தொடர்பு கொள்ள பயன்படுத்தப்படுகிறது. இதன் செயல்பாடுகள்:

    - model_name ஐ "Phi-3-mini-4k-instruct" என அமைக்கிறது.

    - registry_ml_client பொருளின் models சொத்தின் get முறையைப் பயன்படுத்தி, Azure ML பதிவேட்டிலிருந்து குறிப்பிட்ட பெயருடன் கூடிய மாதிரியின் சமீபத்திய பதிப்பை மீட்டெடுக்கிறது. get முறை இரண்டு வாதங்களுடன் அழைக்கப்படுகிறது: மாதிரியின் பெயர் மற்றும் மாதிரியின் சமீபத்திய பதிப்பை மீட்டெடுக்க ஒரு லேபிள்.

    - நயம்கொண்டு பயன்படுத்தப்படும் மாதிரியின் பெயர், பதிப்பு மற்றும் id ஆகியவற்றை console இல் ஒரு செய்தியாக அச்சிடுகிறது. மாதிரியின் பெயர், பதிப்பு மற்றும் id ஆகியவை foundation_model பொருளின் சொத்துகளாக அணுகப்படுகின்றன.

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

## 3. வேலைக்கு பயன்படுத்த ஒரு கணினியை உருவாக்கவும்

நயம்கொண்டு பயன்படுத்தும் வேலை GPU கணினியுடன் மட்டுமே செயல்படும். கணினியின் அளவு மாதிரியின் அளவுக்கு ஏற்ப மாறுபடும், மேலும் பெரும்பாலான சந்தர்ப்பங்களில் வேலைக்கு சரியான கணினியை அடையாளம் காண்பது சிக்கலாக இருக்கும். இந்த செல், வேலைக்கு சரியான கணினியைத் தேர்ந்தெடுக்க பயனருக்கு வழிகாட்டுகிறது.

> [!NOTE]
> கீழே பட்டியலிடப்பட்டுள்ள கணினிகள் மிகவும் மேம்பட்ட கட்டமைப்புடன் செயல்படுகின்றன. கட்டமைப்பில் எந்தவொரு மாற்றமும் Cuda Out Of Memory பிழைக்கு வழிவகுக்கலாம். இப்படிப்பட்ட சந்தர்ப்பங்களில், கணினியை பெரிய அளவுக்கு மேம்படுத்த முயற்சிக்கவும்.

> [!NOTE]
> கீழே உள்ள compute_cluster_size ஐத் தேர்ந்தெடுக்கும் போது, உங்கள் resource group இல் கணினி கிடைக்கிறதா என்பதை உறுதிப்படுத்தவும். ஒரு குறிப்பிட்ட கணினி கிடைக்கவில்லை என்றால், கணினி வளங்களை அணுகுவதற்கான கோரிக்கையைச் செய்யலாம்.

### நயம்கொண்டு பயன்படுத்தும் ஆதரவு மாதிரியைச் சரிபார்க்க

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning (Azure ML) மாதிரியுடன் தொடர்பு கொள்ளுகிறது. இதன் செயல்பாடுகள்:

    - ast மாட்யூலை இறக்குமதி செய்கிறது, இது Python abstract syntax grammar-ஐ செயலாக்க செயல்பாடுகளை வழங்குகிறது.

    - foundation_model பொருளில் finetune_compute_allow_list என்ற ஒரு குறிச்சொல் உள்ளதா என்பதை சரிபார்க்கிறது. Azure ML இல் குறிச்சொற்கள் முக்கிய-மதிப்பு ஜோடிகளாகும், அவற்றை உருவாக்கி மாதிரிகளை வடிகட்டி வரிசைப்படுத்த பயன்படுத்தலாம்.

    - finetune_compute_allow_list குறிச்சொல் இருந்தால், ast.literal_eval செயல்பாட்டைப் பயன்படுத்தி குறிச்சொல்லின் மதிப்பை (ஒரு சரம்) Python பட்டியலாக பாதுகாப்பாக மாற்றுகிறது. இந்த பட்டியல் computes_allow_list மாறியில் ஒதுக்கப்படுகிறது. பின்னர் பட்டியலிலிருந்து கணினியை உருவாக்க வேண்டும் என்று குறிப்பிட்டு ஒரு செய்தியை அச்சிடுகிறது.

    - finetune_compute_allow_list குறிச்சொல் இல்லாவிட்டால், computes_allow_list ஐ None ஆக அமைக்கிறது மற்றும் மாதிரியின் குறிச்சொற்களில் finetune_compute_allow_list குறிச்சொல் இல்லை என்று குறிப்பிட்டு ஒரு செய்தியை அச்சிடுகிறது.

    - மொத்தத்தில், இந்த ஸ்கிரிப்ட் மாதிரியின் மெட்டாடேட்டாவில் ஒரு குறிப்பிட்ட குறிச்சொல்லைச் சரிபார்க்கிறது, குறிச்சொல்லின் மதிப்பை பட்டியலாக மாற்றுகிறது, மற்றும் பயனருக்கு அதன்படி கருத்துக்களை வழங்குகிறது.

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

### கணினி நிகழ்வைச் சரிபார்க்க

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning (Azure ML) சேவையுடன் தொடர்பு கொண்டு ஒரு கணினி நிகழ்வில் பல சரிபார்ப்புகளைச் செய்கிறது. இதன் செயல்பாடுகள்:

    - compute_cluster இல் சேமிக்கப்பட்ட பெயருடன் Azure ML வேலைப்பகுதியில் இருந்து கணினி நிகழ்வை மீட்டெடுக்க முயற்சிக்கிறது. கணினி நிகழ்வின் provisioning state "failed" என்றால், ValueError எழுப்புகிறது.

    - computes_allow_list None அல்ல என்றால், பட்டியலிலுள்ள அனைத்து கணினி அளவுகளையும் lowercase ஆக மாற்றி, தற்போதைய கணினி நிகழ்வின் அளவு பட்டியலில் உள்ளதா என்பதைச் சரிபார்க்கிறது. இல்லையெனில், ValueError எழுப்புகிறது.

    - computes_allow_list None என்றால், தற்போதைய கணினி நிகழ்வின் அளவு ஆதரிக்கப்படாத GPU VM அளவுகளின் பட்டியலில் உள்ளதா என்பதைச் சரிபார்க்கிறது. இருந்தால், ValueError எழுப்புகிறது.

    - வேலைப்பகுதியில் உள்ள அனைத்து கிடைக்கக்கூடிய கணினி அளவுகளின் பட்டியலை மீட்டெடுக்கிறது. பின்னர் இந்த பட்டியலின் மீது மீண்டும் மீண்டும் செயல்படுகிறது, மேலும் ஒவ்வொரு கணினி அளவிற்கும், அதன் பெயர் தற்போதைய கணினி நிகழ்வின் அளவுடன் பொருந்துகிறதா என்பதைச் சரிபார்க்கிறது. பொருந்தினால், அந்த கணினி அளவுக்கான GPUகளின் எண்ணிக்கையை மீட்டெடுத்து gpu_count_found ஐ True ஆக அமைக்கிறது.

    - gpu_count_found True என்றால், கணினி நிகழ்வில் உள்ள GPUகளின் எண்ணிக்கையை அச்சிடுகிறது. gpu_count_found False என்றால், ValueError எழுப்புகிறது.

    - மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure ML வேலைப்பகுதியில் உள்ள ஒரு கணினி நிகழ்வில் பல சரிபார்ப்புகளைச் செய்கிறது, அதில் அதன் provisioning state, அளவு மற்றும் GPUகளின் எண்ணிக்கை ஆகியவை அடங்கும்.

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

## 4. மாதிரியை நயம்கொண்டு பயன்படுத்த தரவுத்தொகுப்பைத் தேர்ந்தெடுக்கவும்

1. நாம் ultrachat_200k தரவுத்தொகுப்பைப் பயன்படுத்துகிறோம். இந்த தரவுத்தொகுப்பில் நான்கு பிரிவுகள் உள்ளன, Supervised fine-tuning (sft) மற்றும் Generation ranking (gen) ஆகியவற்றுக்கு ஏற்றது. ஒவ்வொரு பிரிவிலும் உள்ள எடுத்துக்காட்டுகளின் எண்ணிக்கை பின்வருமாறு:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. நயம்கொண்டு பயன்படுத்துவதற்கான அடிப்படை தரவுகளைத் தயாரிக்க கீழே உள்ள சில செல்கள் காட்டுகின்றன:

### சில தரவுத்தொடர்களை காட்சிப்படுத்துதல்

இந்த மாதிரியை விரைவாக இயக்க விரும்புகிறோம், எனவே train_sft, test_sft கோப்புகளை 5% மட்டுமே உள்ளடக்கியதாக சேமிக்கிறோம். இதன் பொருள், நயம்கொண்ட மாதிரிக்கு குறைந்த துல்லியம் இருக்கும், எனவே இது உண்மையான உலகில் பயன்படுத்தப்படக்கூடாது. download-dataset.py ஸ்கிரிப்ட் ultrachat_200k தரவுத்தொகுப்பை பதிவிறக்கம் செய்யவும், தரவுத்தொகுப்பை நயம்கொண்டு பயன்படுத்தும் குழாய் கூறு வடிவத்திற்கு மாற்றவும் பயன்படுத்தப்படுகிறது. மேலும், தரவுத்தொகுப்பு பெரியதாக இருப்பதால், இங்கு தரவுத்தொகுப்பின் ஒரு பகுதியை மட்டுமே கொண்டுள்ளோம்.

1. கீழே உள்ள ஸ்கிரிப்டை இயக்குவது தரவின் 5% ஐ மட்டுமே பதிவிறக்குகிறது. dataset_split_pc அளவுருவை விரும்பிய சதவீதமாக மாற்றுவதன் மூலம் இதை அதிகரிக்கலாம்.

    > [!NOTE]
    > சில மொழி மாதிரிகளுக்கு வெவ்வேறு மொழி குறியீடுகள் உள்ளன, எனவே தரவுத்தொகுப்பில் உள்ள நெடுவரிசை பெயர்கள் அதேபோல பிரதிபலிக்க வேண்டும்.

1. தரவுகள் எப்படி இருக்க வேண்டும் என்பதற்கான எடுத்துக்காட்டை இங்கே காணலாம்:
chat-completion தரவுத்தொகுப்பு ஒவ்வொரு பதிவையும் பின்வரும் அமைப்புடன் கொண்டுள்ள Parquet வடிவத்தில் சேமிக்கப்படுகிறது:

    - இது ஒரு JSON (JavaScript Object Notation) ஆவணம், இது பிரபலமான தரவுப் பரிமாற்ற வடிவமாகும். இது செயல்படுத்தக்கூடிய குறியீடு அல்ல, ஆனால் தரவுகளை சேமிக்கவும் பரிமாற்றவும் ஒரு வழியாகும். இதன் அமைப்பின் விவரங்கள்:

    - "prompt": இது AI உதவியாளருக்கு கேள்வி அல்லது பணியை பிரதிநிதித்துவப்படுத்தும் ஒரு சரம் மதிப்பைக் கொண்டுள்ளது.

    - "messages": இது ஒரு பொருட்களின் வரிசையை வைத்துள்ளது. ஒவ்வொரு பொருளும் ஒரு பயனர் மற்றும் AI உதவியாளருக்கிடையிலான உரையாடலின் ஒரு செய்தியை பிரதிநிதித்துவப்படுத்துகிறது. ஒவ்வொரு செய்தி பொருளுக்கும் இரண்டு முக்கியங்கள் உள்ளன:

    - "content": இது செய்தியின் உள்ளடக்கத்தை பிரதிநிதித்துவப்படுத்தும் ஒரு சரம் மதிப்பைக் கொண்டுள்ளது.
    - "role": இது செய்தியை அனுப்பியவரின் பங்கு என்ன என்பதை பிரதிநிதித்துவப்படுத்தும் ஒரு சரம் மதிப்பைக் கொண்டுள்ளது. இது "user" அல்லது "assistant" ஆக இருக்கலாம்.
    - "prompt_id": இது prompt க்கான தனித்துவமான அடையாளத்தை பிரதிநிதித்துவப்படுத்தும் ஒரு சரம் மதிப்பைக் கொண்டுள்ளது.

1. இந்த குறிப்பிட்ட JSON ஆவணத்தில், ஒரு பயனர் AI உதவியாளரிடம் ஒரு கதை நாயகனை உருவாக்க கேட்கும் உரையாடல் பிரதிநிதித்துவப்படுத்தப்பட்டுள்ளது. உதவியாளர் பதிலளிக்கிறார், பின்னர் பயனர் மேலும் விவரங்களை கேட்கிறார். உதவியாளர் மேலும் விவரங்களை வழங்க ஒப்புக்கொள்கிறார். இந்த முழு உரையாடல் ஒரு குறிப்பிட்ட prompt id உடன் தொடர்புடையது.

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

### தரவுகளை பதிவிறக்குதல்

1. இந்த Python ஸ்கிரிப்ட் download-dataset.py என்ற உதவியாளர் ஸ்கிரிப்டைப் பயன்படுத்தி ஒரு தரவுத்தொகுப்பை பதிவிறக்க பயன்படுத்தப்படுகிறது. இதன் செயல்பாடுகள்:

    - os மாட்யூலை இறக்குமதி செய்கிறது, இது இயக்க முறைமையின் சார்ந்த செயல்பாடுகளைப் பயன்படுத்த ஒரு தகுந்த வழியை வழங்குகிறது.

    - os.system செயல்பாட்டைப் பயன்படுத்தி download-dataset.py ஸ்கிரிப்டை குறிப்பிட்ட கட்டளைக் கோடுகளுடன் ஷெல்லில் இயக்குகிறது. கட்டளைக் கோடுகள் பதிவிறக்க வேண்டிய தரவுத்தொகுப்பை (HuggingFaceH4/ultrachat_200k), அதை பதிவிறக்க வேண்டிய அடைவை (ultrachat_200k_dataset), மற்றும் தரவுத்தொகுப்பை பிரிக்க வேண்டிய சதவீதத்தை (5) குறிப்பிடுகின்றன. os.system செயல்பாடு அது செயல்படுத்திய கட்டளையின் வெளியீட்டு நிலையை திருப்புகிறது; இந்த நிலை exit_status மாறியில் சேமிக்கப்படுகிறது.

    - exit_status 0 அல்ல என்று சரிபார்க்கிறது. Unix போன்ற இயக்க முறைமைகளில், 0 என்ற வெளியீட்டு நிலை ஒரு கட்டளை வெற்றிகரமாக முடிந்தது என்பதைப் பொதுவாகக் குறிக்கிறது, மற்ற எந்த எண்ணும் பிழையை குறிக்கிறது. exit_status 0 அல்ல என்றால், தரவுத்தொகுப்பை பதிவிறக்குவதில் பிழை ஏற்பட்டது என்று குறிப்பிட்டு ஒரு εξαίptionஐ எழுப்புகிறது.

    - மொத்தத்தில், இந்த ஸ்கிரிப்ட் ஒரு உதவியாளர் ஸ்கிரிப்டைப் பயன்படுத்தி ஒரு தரவுத்தொகுப்பை பதிவிறக்க ஒரு கட்டளையை இயக்குகிறது, மேலும் கட்டளை தோல்வியடைந்தால் εξαίptionஐ எழுப்புகிறது.

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

### தரவுகளை DataFrame-ல் ஏற்றுதல்

1. இந்த Python ஸ்கிரிப்ட் JSON Lines கோப்பை pandas DataFrame-ல் ஏற்றி முதல் 5 வரிசைகளை காட்சிப்படுத்துகிறது. இதன் செயல்பாடுகள்:


- இது pd.read_json செயல்பாட்டைப் பயன்படுத்தி ultrachat_200k_dataset கோப்பகத்தில் உள்ள train_sft.jsonl கோப்பை DataFrame-இல் ஏற்றுகிறது. lines=True ஆArgument JSON Lines வடிவத்தில் கோப்பை குறிக்கிறது, இதில் ஒவ்வொரு வரியும் தனித்த JSON பொருளாக இருக்கும்.

- இது DataFrame-இன் முதல் 5 வரிகளை காட்ட head முறைமையைப் பயன்படுத்துகிறது. DataFrame-இல் 5 வரிகளுக்கு குறைவாக இருந்தால், அனைத்தையும் காட்டும்.

- மொத்தத்தில், இந்த ஸ்கிரிப்ட் JSON Lines கோப்பை DataFrame-இல் ஏற்றி, முழு கால்‍முனை உரையுடன் முதல் 5 வரிகளை காட்டுகிறது.

## 5. மாடல் மற்றும் தரவுகளை உள்ளீடுகளாகக் கொண்டு fine tuning வேலைகளை சமர்ப்பிக்கவும்

chat-completion pipeline கூறுகளைப் பயன்படுத்தும் வேலைகளை உருவாக்கவும். fine tuning-க்கு ஆதரவு அளிக்கும் அனைத்து அளவுருக்களையும் பற்றி மேலும் அறிக.

### finetune அளவுருக்களை வரையறுக்கவும்

1. finetune அளவுருக்கள் 2 பிரிவுகளாகக் குழுவிடப்படலாம் - பயிற்சி அளவுருக்கள், மேம்படுத்தல் அளவுருக்கள்

1. பயிற்சி அளவுருக்கள் பயிற்சியின் அம்சங்களை வரையறுக்கின்றன, உதாரணமாக -

    - பயன்படுத்த வேண்டிய optimizer, scheduler
    - finetune-ஐ மேம்படுத்த metric
    - பயிற்சி படிகள் மற்றும் batch அளவுகள் மற்றும் இதர அம்சங்கள்
    - மேம்படுத்தல் அளவுருக்கள் GPU நினைவகத்தை மேம்படுத்தவும் கணினி வளங்களை பயனுள்ளதாகப் பயன்படுத்தவும் உதவுகின்றன.

1. கீழே இந்த பிரிவில் உள்ள சில அளவுருக்கள் உள்ளன. ஒவ்வொரு மாடலுக்கும் மேம்படுத்தல் அளவுருக்கள் மாறுபடுகின்றன மற்றும் இந்த மாறுபாடுகளை கையாள மாடலுடன் தொகுக்கப்படுகின்றன.

    - deepspeed மற்றும் LoRA-ஐ இயக்கவும்
    - mixed precision பயிற்சியை இயக்கவும்
    - multi-node பயிற்சியை இயக்கவும்

> [!NOTE]
> Supervised finetuning-ல் alignment அல்லது catastrophic forgetting இழப்பை ஏற்படுத்தலாம். இந்த பிரச்சினையைச் சரிபார்த்து, finetune செய்த பிறகு alignment நிலையை இயக்க பரிந்துரைக்கிறோம்.

### Fine Tuning அளவுருக்கள்

1. இந்த Python ஸ்கிரிப்ட் ஒரு இயந்திரக் கற்றல் மாடலுக்கான fine-tuning அளவுருக்களை அமைக்கிறது. இதோ அதன் விவரம்:

    - பயிற்சிக்கான default அளவுருக்களை அமைக்கிறது, உதாரணமாக பயிற்சி epochs, பயிற்சி மற்றும் மதிப்பீட்டு batch அளவுகள், learning rate மற்றும் learning rate scheduler வகை.

    - default மேம்படுத்தல் அளவுருக்களை அமைக்கிறது, உதாரணமாக Layer-wise Relevance Propagation (LoRa) மற்றும் DeepSpeed-ஐ பயன்படுத்த வேண்டுமா, DeepSpeed நிலை.

    - பயிற்சி மற்றும் மேம்படுத்தல் அளவுருக்களை finetune_parameters என்ற dictionary-யில் இணைக்கிறது.

    - foundation_model-ல் மாடல்-குறிப்பான default அளவுருக்கள் உள்ளதா என்பதைச் சரிபார்க்கிறது. இருந்தால், எச்சரிக்கை செய்தியை அச்சிடுகிறது மற்றும் finetune_parameters dictionary-யை மாடல்-குறிப்பான default-களுடன் புதுப்பிக்கிறது. ast.literal_eval செயல்பாடு மாடல்-குறிப்பான default-களை string-இலிருந்து Python dictionary-ஆக மாற்ற பயன்படுத்தப்படுகிறது.

    - இயக்கத்திற்குப் பயன்படுத்தப்படும் இறுதி fine-tuning அளவுருக்களை அச்சிடுகிறது.

    - மொத்தத்தில், இந்த ஸ்கிரிப்ட் ஒரு இயந்திரக் கற்றல் மாடலுக்கான fine-tuning அளவுருக்களை அமைத்து, மாடல்-குறிப்பான default-களுடன் override செய்யும் திறனுடன் அவற்றை காட்டுகிறது.

### பயிற்சி குழாய்

1. இந்த Python ஸ்கிரிப்ட் ஒரு இயந்திரக் கற்றல் பயிற்சி குழாய்க்கான display name-ஐ உருவாக்க ஒரு செயல்பாட்டை வரையறுக்கிறது, பின்னர் இந்த செயல்பாட்டை அழைத்து display name-ஐ உருவாக்கி அச்சிடுகிறது. இதோ அதன் விவரம்:

1. get_pipeline_display_name செயல்பாடு வரையறுக்கப்பட்டுள்ளது. இந்த செயல்பாடு பயிற்சி குழாய்க்கான display name-ஐ பல அளவுருக்களை அடிப்படையாகக் கொண்டு உருவாக்குகிறது.

1. செயல்பாட்டுக்குள், per-device batch size, gradient accumulation steps, GPUs per node மற்றும் fine-tuning-க்கு nodes எண்ணிக்கையைப் பெருக்கி மொத்த batch அளவை கணக்கிடுகிறது.

1. learning rate scheduler வகை, DeepSpeed பயன்படுத்தப்பட்டதா, DeepSpeed நிலை, Layer-wise Relevance Propagation (LoRa) பயன்படுத்தப்பட்டதா, மாடல் checkpoints எண்ணிக்கைக்கு வரம்பு மற்றும் அதிகபட்ச வரிசை நீளம் போன்ற பல அளவுருக்களை பெறுகிறது.

1. இந்த அளவுருக்களை எல்லாம் hyphens-ஆல் பிரிக்கப்பட்ட string-ஆக உருவாக்குகிறது. DeepSpeed அல்லது LoRa பயன்படுத்தப்பட்டால், string-ல் "ds" DeepSpeed நிலையைத் தொடர்ந்து அல்லது "lora" சேர்க்கப்படும். பயன்படுத்தப்படவில்லை என்றால், "nods" அல்லது "nolora" சேர்க்கப்படும்.

1. இந்த string-ஐ return செய்கிறது, இது பயிற்சி குழாய்க்கான display name ஆக செயல்படுகிறது.

1. செயல்பாடு வரையறுக்கப்பட்ட பிறகு, display name-ஐ உருவாக்க அழைக்கப்படுகிறது, பின்னர் அச்சிடப்படுகிறது.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் பல அளவுருக்களை அடிப்படையாகக் கொண்டு ஒரு இயந்திரக் கற்றல் பயிற்சி குழாய்க்கான display name-ஐ உருவாக்கி, பின்னர் அதை அச்சிடுகிறது.

### குழாயை அமைத்தல்

இந்த Python ஸ்கிரிப்ட் Azure Machine Learning SDK-ஐப் பயன்படுத்தி ஒரு இயந்திரக் கற்றல் குழாயை வரையறுத்து அமைக்கிறது. இதோ அதன் விவரம்:

1. Azure AI ML SDK-இலிருந்து தேவையான modules-ஐ import செய்கிறது.

1. "chat_completion_pipeline" என்ற குழாய் கூறை registry-இலிருந்து fetch செய்கிறது.

1. `@pipeline` decorator மற்றும் `create_pipeline` செயல்பாட்டைப் பயன்படுத்தி குழாய் வேலைகளை வரையறுக்கிறது. குழாயின் பெயர் `pipeline_display_name` ஆக அமைக்கப்பட்டுள்ளது.

1. `create_pipeline` செயல்பாட்டுக்குள், மாடல் பாதை, பயிற்சி மற்றும் சோதனைக்கான கணினி குழுக்கள், fine-tuning-க்கு GPUs எண்ணிக்கை மற்றும் பிற fine-tuning அளவுருக்கள் போன்ற பல அளவுருக்களுடன் fetch செய்யப்பட்ட குழாய் கூறத்தை ஆரம்பிக்கிறது.

1. fine-tuning வேலைகளின் output-ஐ குழாய் வேலைகளின் output-க்கு map செய்கிறது. இது fine-tuned மாடலை எளிதாக பதிவு செய்ய உதவுகிறது, இது மாடலை online அல்லது batch endpoint-க்கு deploy செய்ய தேவையானது.

1. `create_pipeline` செயல்பாட்டை அழைத்து குழாய் instance-ஐ உருவாக்குகிறது.

1. குழாயின் `force_rerun` அமைப்பை `True` ஆக அமைக்கிறது, இது முந்தைய வேலைகளின் cache செய்யப்பட்ட முடிவுகளைப் பயன்படுத்தாது.

1. குழாயின் `continue_on_step_failure` அமைப்பை `False` ஆக அமைக்கிறது, இது எந்த ஒரு படியும் தோல்வியடைந்தால் குழாய் நிறுத்தப்படும்.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure Machine Learning SDK-ஐப் பயன்படுத்தி chat completion task-க்கு ஒரு இயந்திரக் கற்றல் குழாயை வரையறுத்து அமைக்கிறது.

### வேலைகளை சமர்ப்பிக்கவும்

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning workspace-க்கு ஒரு இயந்திரக் கற்றல் குழாய் வேலைகளை சமர்ப்பித்து, பின்னர் வேலை முடிவடைய காத்திருக்கிறது. இதோ அதன் விவரம்:

    - workspace_ml_client-இல் jobs object-இன் create_or_update முறைமையை அழைத்து குழாய் வேலைகளை சமர்ப்பிக்கிறது. இயக்கப்பட வேண்டிய குழாய் pipeline_object மூலம் குறிப்பிடப்படுகிறது, மற்றும் வேலை இயக்கப்படும் experiment experiment_name மூலம் குறிப்பிடப்படுகிறது.

    - பின்னர் workspace_ml_client-இல் jobs object-இன் stream முறைமையை அழைத்து குழாய் வேலை முடிவடைய காத்திருக்கிறது. காத்திருக்க வேண்டிய வேலை pipeline_job object-இன் name attribute மூலம் குறிப்பிடப்படுகிறது.

    - மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure Machine Learning workspace-க்கு ஒரு இயந்திரக் கற்றல் குழாய் வேலைகளை சமர்ப்பித்து, பின்னர் வேலை முடிவடைய காத்திருக்கிறது.

## 6. Workspace-இல் fine tuned மாடலை பதிவு செய்யவும்

fine tuning வேலைகளின் output-இலிருந்து மாடலை பதிவு செய்வோம். இது fine tuned மாடல் மற்றும் fine tuning வேலைகளுக்கு இடையிலான வரிசையைப் பின்தொடரும். fine tuning வேலைகள், மேலும், foundation model, data மற்றும் training code-க்கு வரிசையைப் பின்தொடர்கின்றன.

### ML மாடலை பதிவு செய்தல்

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning குழாயில் பயிற்சி செய்யப்பட்ட ஒரு இயந்திரக் கற்றல் மாடலை பதிவு செய்கிறது. இதோ அதன் விவரம்:

    - Azure AI ML SDK-இலிருந்து தேவையான modules-ஐ import செய்கிறது.

    - workspace_ml_client-இல் jobs object-இன் get முறைமையை அழைத்து அதன் outputs attribute-ஐ அணுகுவதன் மூலம் pipeline வேலைகளிலிருந்து trained_model output கிடைக்கிறதா என்பதைச் சரிபார்க்கிறது.

    - pipeline வேலைகளின் பெயர் மற்றும் output ("trained_model") பெயரை format செய்து trained model-க்கு ஒரு பாதையை உருவாக்குகிறது.

    - original மாடல் பெயருக்கு "-ultrachat-200k" சேர்த்து, எந்த slashes-ஐயும் hyphens-ஆக மாற்றி fine-tuned மாடலுக்கு ஒரு பெயரை வரையறுக்கிறது.

    - மாடலை பதிவு செய்ய Model object-ஐ உருவாக்குகிறது, இதில் மாடலின் பாதை, மாடலின் வகை (MLflow model), மாடலின் பெயர் மற்றும் version மற்றும் மாடலின் விளக்கம் போன்ற பல அளவுருக்கள் உள்ளன.

    - workspace_ml_client-இல் models object-இன் create_or_update முறைமையை Model object-ஐ argument ஆகக் கொண்டு அழைத்து மாடலை பதிவு செய்கிறது.

    - பதிவு செய்யப்பட்ட மாடலை அச்சிடுகிறது.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure Machine Learning குழாயில் பயிற்சி செய்யப்பட்ட ஒரு இயந்திரக் கற்றல் மாடலை பதிவு செய்கிறது.

## 7. fine tuned மாடலை online endpoint-க்கு deploy செய்யவும்

Online endpoints REST API-ஐ வழங்குகிறது, இது மாடலைப் பயன்படுத்த தேவையான பயன்பாடுகளுடன் ஒருங்கிணைக்க உதவுகிறது.

### Endpoint-ஐ நிர்வகிக்கவும்

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning-இல் ஒரு பதிவு செய்யப்பட்ட மாடலுக்கான managed online endpoint-ஐ உருவாக்குகிறது. இதோ அதன் விவரம்:

    - Azure AI ML SDK-இலிருந்து தேவையான modules-ஐ import செய்கிறது.

    - "ultrachat-completion-" string-க்கு timestamp-ஐ சேர்த்து online endpoint-க்கு ஒரு தனித்த பெயரை வரையறுக்கிறது.

    - ManagedOnlineEndpoint object-ஐ உருவாக்கி online endpoint-ஐ உருவாக்க தயாராகிறது, இதில் endpoint-ஐ name, description மற்றும் authentication mode ("key") போன்ற பல அளவுருக்கள் உள்ளன.

    - workspace_ml_client-இல் ManagedOnlineEndpoint object-ஐ argument ஆகக் கொண்டு begin_create_or_update முறைமையை அழைத்து online endpoint-ஐ உருவாக்குகிறது. பின்னர் wait முறைமையை அழைத்து உருவாக்கல் செயல்பாடு முடிவடைய காத்திருக்கிறது.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure Machine Learning-இல் ஒரு பதிவு செய்யப்பட்ட மாடலுக்கான managed online endpoint-ஐ உருவாக்குகிறது.

> [!NOTE]
> deployment-க்கு ஆதரவு அளிக்கும் SKU-க்களின் பட்டியலை இங்கே காணலாம் - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML மாடலை deploy செய்தல்

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning-இல் ஒரு பதிவு செய்யப்பட்ட இயந்திரக் கற்றல் மாடலை managed online endpoint-க்கு deploy செய்கிறது. இதோ அதன் விவரம்:

    - Python abstract syntax grammar-இன் trees-ஐ process செய்ய functions-ஐ வழங்கும் ast module-ஐ import செய்கிறது.

    - deployment-க்கு instance வகையை "Standard_NC6s_v3" ஆக அமைக்கிறது.

    - foundation model-இல் inference_compute_allow_list tag உள்ளது என்பதைச் சரிபார்க்கிறது. இருந்தால், tag value-ஐ string-இலிருந்து Python list-ஆக மாற்றி inference_computes_allow_list-க்கு assign செய்கிறது. இல்லையெனில், inference_computes_allow_list-ஐ None-ஆக அமைக்கிறது.

    - குறிப்பிடப்பட்ட instance வகை allow list-இல் உள்ளதா என்பதைச் சரிபார்க்கிறது. இல்லையெனில், allow list-இல் இருந்து instance வகையைத் தேர்ந்தெடுக்க பயனரிடம் கேட்கும் message-ஐ அச்சிடுகிறது.

    - ManagedOnlineDeployment object-ஐ உருவாக்கி deployment-ஐ உருவாக்க தயாராகிறது, இதில் deployment name, endpoint name, model ID, instance type மற்றும் count, liveness probe settings மற்றும் request settings போன்ற பல அளவுருக்கள் உள்ளன.

    - workspace_ml_client-இல் ManagedOnlineDeployment object-ஐ argument ஆகக் கொண்டு begin_create_or_update முறைமையை அழைத்து deployment-ஐ உருவாக்குகிறது. பின்னர் wait முறைமையை அழைத்து உருவாக்கல் செயல்பாடு முடிவடைய காத்திருக்கிறது.

    - endpoint traffic-ஐ "demo" deployment-க்கு 100% traffic-ஐ நேரடியாக மாற்ற அமைக்கிறது.

    - endpoint-ஐ update செய்ய workspace_ml_client-இல் endpoint object-ஐ argument ஆகக் கொண்டு begin_create_or_update முறைமையை அழைக்கிறது. பின்னர் update operation முடிவடைய result முறைமையை அழைக்கிறது.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure Machine Learning-இல் ஒரு பதிவு செய்யப்பட்ட இயந்திரக் கற்றல் மாடலை managed online endpoint-க்கு deploy செய்கிறது.

## 8. endpoint-ஐ மாதிரி தரவுடன் சோதிக்கவும்

சோதனை dataset-இலிருந்து சில மாதிரி தரவுகளை fetch செய்து online endpoint-க்கு inference-க்கு சமர்ப்பிக்கிறோம். பின்னர் scored labels-ஐ ground truth labels-க்கு அருகில் காட்டுவோம்.

### முடிவுகளைப் படிக்கவும்

1. இந்த Python ஸ்கிரிப்ட் JSON Lines கோப்பை pandas DataFrame-இல் படிக்கிறது, ஒரு random sample-ஐ எடுக்கிறது மற்றும் index-ஐ reset செய்கிறது. இதோ அதன் விவரம்:

    - ./ultrachat_200k_dataset/test_gen.jsonl கோப்பை pandas DataFrame-இல் படிக்கிறது. read_json செயல்பாடு lines=True argument-ஐப் பயன்படுத்துகிறது, ஏனெனில் கோப்பு JSON Lines வடிவத்தில் உள்ளது, இதில் ஒவ்வொரு வரியும் தனித்த JSON பொருளாக இருக்கும்.

    - DataFrame-இல் இருந்து 1 வரியின் random sample-ஐ எடுக்கிறது. sample செயல்பாடு n=1 argument-ஐப் பயன்படுத்துகிறது, தேர்ந்தெடுக்க வேண்டிய random வரிகளின் எண்ணிக்கையை குறிப்பிட.

    - DataFrame-இன் index-ஐ reset செய்கிறது. reset_index செயல்பாடு drop=True argument-ஐப் பயன்படுத்துகிறது, original index-ஐ drop செய்து default integer values-இன் புதிய index-ஐ மாற்ற.

    - DataFrame-இன் முதல் 2 வரிகளை head செயல்பாட்டைப் பயன்படுத்தி argument 2-ஐக் கொண்டு காட்டுகிறது. ஆனால், DataFrame-இல் sampling பிறகு ஒரு வரி மட்டுமே உள்ளதால், இது அந்த ஒரு வரியை மட்டுமே காட்டும்.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் JSON Lines கோப்பை pandas DataFrame-இல் படிக்கிறது, 1 வரியின் random sample-ஐ எடுக்கிறது, index-ஐ reset செய்கிறது மற்றும் முதல் வரியை காட்டுகிறது.

### JSON பொருளை உருவாக்கவும்

1. இந்த Python ஸ்கிரிப்ட் குறிப்பிட்ட அளவுருக்களுடன் JSON பொருளை உருவாக்கி ஒரு கோப்பில் சேமிக்கிறது. இதோ அதன் விவரம்:

    - JSON தரவுடன் வேலை செய்ய functions-ஐ வழங்கும் json module-ஐ import செய்கிறது.
- இது "temperature", "top_p", "do_sample", மற்றும் "max_new_tokens" என்ற முக்கியங்கள் மற்றும் அவற்றின் மதிப்புகளைக் கொண்ட dictionary parameters ஐ உருவாக்குகிறது. அவற்றின் மதிப்புகள் முறையே 0.6, 0.9, True, மற்றும் 200 ஆகும்.

- இது test_json என்ற dictionary ஐ உருவாக்குகிறது, இதில் இரண்டு முக்கியங்கள் உள்ளன: "input_data" மற்றும் "params". "input_data" இன் மதிப்பு மற்றொரு dictionary ஆகும், இதில் "input_string" மற்றும் "parameters" என்ற முக்கியங்கள் உள்ளன. "input_string" இன் மதிப்பு test_df DataFrame இல் முதல் செய்தியை கொண்ட ஒரு பட்டியல் ஆகும். "parameters" இன் மதிப்பு முன்பே உருவாக்கப்பட்ட parameters dictionary ஆகும். "params" இன் மதிப்பு காலியாக உள்ளது.

- இது sample_score.json என்ற கோப்பை திறக்கிறது.

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

### Endpoint ஐ அழைப்பது

1. இந்த Python ஸ்கிரிப்ட் Azure Machine Learning இல் உள்ள ஒரு online endpoint ஐ அழைத்து JSON கோப்பை மதிப்பீடு செய்கிறது. இதன் செயல்பாடுகளைப் பார்ப்போம்:

   - workspace_ml_client பொருளின் online_endpoints சொத்தின் invoke முறை அழைக்கப்படுகிறது. இந்த முறை ஒரு online endpoint க்கு கோரிக்கையை அனுப்பி பதிலை பெற பயன்படுத்தப்படுகிறது.

   - endpoint_name மற்றும் deployment_name arguments மூலம் endpoint மற்றும் deployment பெயர்களை குறிப்பிடுகிறது. இங்கு endpoint பெயர் online_endpoint_name மாறியில் சேமிக்கப்பட்டுள்ளது, deployment பெயர் "demo" ஆகும்.

   - request_file argument மூலம் மதிப்பீடு செய்ய வேண்டிய JSON கோப்பின் பாதையை குறிப்பிடுகிறது. இங்கு கோப்பு ./ultrachat_200k_dataset/sample_score.json ஆகும்.

   - endpoint இல் இருந்து பெறப்பட்ட பதிலை response மாறியில் சேமிக்கிறது.

   - crude response ஐ அச்சிடுகிறது.

1. மொத்தத்தில், இந்த ஸ்கிரிப்ட் Azure Machine Learning இல் உள்ள online endpoint ஐ அழைத்து JSON கோப்பை மதிப்பீடு செய்து பதிலை அச்சிடுகிறது.

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

## 9. Online Endpoint ஐ நீக்குதல்

1. Online endpoint ஐ மறக்காமல் நீக்க வேண்டும், இல்லையெனில் endpoint பயன்படுத்தும் கணினி விலை மீட்டர் இயங்கிக் கொண்டிருக்கும். இந்த Python கோடு Azure Machine Learning இல் உள்ள online endpoint ஐ நீக்குகிறது. இதன் செயல்பாடுகளைப் பார்ப்போம்:

   - workspace_ml_client பொருளின் online_endpoints சொத்தின் begin_delete முறை அழைக்கப்படுகிறது. இந்த முறை online endpoint ஐ நீக்க தொடங்க பயன்படுத்தப்படுகிறது.

   - name argument மூலம் நீக்க வேண்டிய endpoint இன் பெயரை குறிப்பிடுகிறது. இங்கு endpoint பெயர் online_endpoint_name மாறியில் சேமிக்கப்பட்டுள்ளது.

   - wait முறை அழைக்கப்படுகிறது, இது நீக்கல் செயல்பாடு முடியும் வரை காத்திருக்கிறது. இது blocking operation ஆகும், அதாவது நீக்கல் முடியும் வரை ஸ்கிரிப்ட் தொடராது.

   - மொத்தத்தில், இந்த கோடு Azure Machine Learning இல் உள்ள online endpoint ஐ நீக்க தொடங்கி, செயல்பாடு முடியும் வரை காத்திருக்கிறது.

    ```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.