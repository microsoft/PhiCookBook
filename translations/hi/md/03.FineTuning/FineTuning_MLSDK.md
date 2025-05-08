<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-08T05:13:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "hi"
}
-->
## Azure ML सिस्टम रजिस्ट्री से चैट-कंप्लीशन कंपोनेंट्स का उपयोग करके मॉडल को फाइन ट्यून कैसे करें

इस उदाहरण में, हम Phi-3-mini-4k-instruct मॉडल का फाइन ट्यूनिंग करेंगे ताकि ultrachat_200k डेटासेट का उपयोग करते हुए 2 लोगों के बीच बातचीत पूरी की जा सके।

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.hi.png)

यह उदाहरण आपको दिखाएगा कि कैसे Azure ML SDK और Python का उपयोग करके फाइन ट्यूनिंग की जाए और फिर फाइन ट्यून किए गए मॉडल को रियल टाइम इनफेरेंस के लिए ऑनलाइन एंडपॉइंट पर डिप्लॉय किया जाए।

### ट्रेनिंग डेटा

हम ultrachat_200k डेटासेट का उपयोग करेंगे। यह UltraChat डेटासेट का एक बहुत ही फिल्टर्ड वर्शन है और इसका उपयोग Zephyr-7B-β, एक अत्याधुनिक 7b चैट मॉडल को ट्रेन करने के लिए किया गया था।

### मॉडल

हम Phi-3-mini-4k-instruct मॉडल का उपयोग करेंगे ताकि दिखा सकें कि उपयोगकर्ता चैट-कंप्लीशन टास्क के लिए मॉडल को कैसे फाइन ट्यून कर सकता है। यदि आपने यह नोटबुक किसी विशेष मॉडल कार्ड से खोली है, तो उस मॉडल का नाम बदलना न भूलें।

### कार्य

- फाइन ट्यून के लिए एक मॉडल चुनें।
- ट्रेनिंग डेटा चुनें और एक्सप्लोर करें।
- फाइन ट्यूनिंग जॉब कॉन्फ़िगर करें।
- फाइन ट्यूनिंग जॉब चलाएं।
- ट्रेनिंग और मूल्यांकन मेट्रिक्स की समीक्षा करें।
- फाइन ट्यून किए गए मॉडल को रजिस्टर करें।
- फाइन ट्यून किए गए मॉडल को रियल टाइम इनफेरेंस के लिए डिप्लॉय करें।
- संसाधनों को साफ करें।

## 1. आवश्यकताएँ सेटअप करें

- निर्भरताएं इंस्टॉल करें
- AzureML Workspace से कनेक्ट करें। सेटअप SDK प्रमाणीकरण के बारे में अधिक जानें। नीचे <WORKSPACE_NAME>, <RESOURCE_GROUP> और <SUBSCRIPTION_ID> को बदलें।
- azureml सिस्टम रजिस्ट्री से कनेक्ट करें
- एक वैकल्पिक एक्सपेरिमेंट नाम सेट करें
- कंप्यूट चेक करें या बनाएं।

> [!NOTE]
> आवश्यकताएँ: एकल GPU नोड में कई GPU कार्ड हो सकते हैं। उदाहरण के लिए, Standard_NC24rs_v3 के एक नोड में 4 NVIDIA V100 GPUs होते हैं जबकि Standard_NC12s_v3 में 2 NVIDIA V100 GPUs होते हैं। इस जानकारी के लिए डॉक्स देखें। प्रत्येक नोड के GPU कार्ड की संख्या param gpus_per_node में सेट की जाती है। इसे सही सेट करने से नोड के सभी GPUs का उपयोग सुनिश्चित होगा। सुझाए गए GPU compute SKUs यहां और यहां मिल सकते हैं।

### Python लाइब्रेरीज़

नीचे सेल चलाकर निर्भरताएं इंस्टॉल करें। यदि नया वातावरण बना रहे हैं तो यह चरण आवश्यक है।

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML के साथ इंटरैक्शन

1. यह Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा के साथ इंटरैक्ट करने के लिए है। इसका विवरण इस प्रकार है:

    - यह azure.ai.ml, azure.identity, और azure.ai.ml.entities पैकेज से आवश्यक मॉड्यूल इम्पोर्ट करता है। साथ ही time मॉड्यूल भी इम्पोर्ट करता है।

    - यह DefaultAzureCredential() का उपयोग करके ऑथेंटिकेट करने की कोशिश करता है, जो Azure क्लाउड में एप्लिकेशन विकसित करने के लिए सरल प्रमाणीकरण अनुभव प्रदान करता है। यदि यह विफल होता है, तो InteractiveBrowserCredential() का उपयोग करता है, जो इंटरैक्टिव लॉगिन प्रॉम्प्ट देता है।

    - फिर यह from_config मेथड से MLClient इंस्टेंस बनाने की कोशिश करता है, जो डिफ़ॉल्ट config.json फ़ाइल से कॉन्फ़िगरेशन पढ़ता है। विफल होने पर, मैन्युअली subscription_id, resource_group_name, और workspace_name प्रदान करके MLClient बनाता है।

    - यह Azure ML रजिस्ट्री "azureml" के लिए एक और MLClient बनाता है, जहां मॉडल, फाइन-ट्यूनिंग पाइपलाइंस और एनवायरनमेंट्स स्टोर होते हैं।

    - experiment_name को "chat_completion_Phi-3-mini-4k-instruct" सेट करता है।

    - एक यूनिक टाइमस्टैम्प बनाता है जो वर्तमान समय (सेकंड में) को इंटीजर में बदलकर स्ट्रिंग में कन्वर्ट करता है। इसका उपयोग यूनिक नाम और वर्जन बनाने में किया जा सकता है।

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

## 2. फाइन ट्यून के लिए एक फाउंडेशन मॉडल चुनें

1. Phi-3-mini-4k-instruct एक 3.8B पैरामीटर्स वाला, हल्का, अत्याधुनिक ओपन मॉडल है जो Phi-2 के लिए उपयोग किए गए डेटासेट्स पर बनाया गया है। यह Phi-3 मॉडल परिवार का हिस्सा है, और मिनी वर्शन दो प्रकारों में आता है: 4K और 128K, जो संदर्भ लंबाई (टोकन में) दर्शाता है। हमें इसे अपने खास उपयोग के लिए फाइन ट्यून करना होगा। आप AzureML Studio के मॉडल कैटलॉग में चैट-कंप्लीशन टास्क से फ़िल्टर करके इन मॉडलों को देख सकते हैं। इस उदाहरण में, हम Phi-3-mini-4k-instruct मॉडल का उपयोग कर रहे हैं। यदि आपने यह नोटबुक किसी अन्य मॉडल के लिए खोली है, तो मॉडल नाम और वर्जन को उसी के अनुसार बदलें।

    > [!NOTE]
    > मॉडल का id प्रॉपर्टी, जिसे फाइन ट्यूनिंग जॉब में इनपुट के रूप में दिया जाएगा। यह AzureML Studio मॉडल कैटलॉग के मॉडल विवरण पेज में Asset ID के रूप में भी उपलब्ध है।

2. यह Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा के साथ इंटरैक्ट कर रही है। इसका विवरण:

    - model_name को "Phi-3-mini-4k-instruct" सेट करती है।

    - registry_ml_client के models प्रॉपर्टी के get मेथड का उपयोग करके Azure ML रजिस्ट्री से इस नाम के मॉडल का नवीनतम वर्जन प्राप्त करती है। get मेथड को दो आर्गुमेंट्स के साथ कॉल किया जाता है: मॉडल का नाम और लेबल जो बताता है कि नवीनतम वर्जन चाहिए।

    - कंसोल में एक संदेश प्रिंट करती है जो बताता है कि फाइन ट्यूनिंग के लिए कौन सा नाम, वर्जन और id वाला मॉडल उपयोग होगा। स्ट्रिंग के format मेथड से ये मान डाला जाता है।

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

## 3. जॉब के लिए कंप्यूट बनाएं

फाइनट्यून जॉब केवल GPU कंप्यूट के साथ काम करता है। कंप्यूट का आकार मॉडल के आकार पर निर्भर करता है और अक्सर सही कंप्यूट चुनना मुश्किल होता है। इस सेल में, हम उपयोगकर्ता को सही कंप्यूट चुनने में मार्गदर्शन करते हैं।

> [!NOTE]
> नीचे सूचीबद्ध कंप्यूट सबसे अनुकूलित कॉन्फ़िगरेशन के साथ काम करते हैं। कॉन्फ़िगरेशन में कोई भी बदलाव Cuda Out Of Memory त्रुटि का कारण बन सकता है। ऐसी स्थिति में कंप्यूट को बड़ा आकार देने का प्रयास करें।

> [!NOTE]
> compute_cluster_size चुनते समय सुनिश्चित करें कि कंप्यूट आपके रिसोर्स ग्रुप में उपलब्ध हो। यदि कोई कंप्यूट उपलब्ध नहीं है, तो कंप्यूट संसाधनों के लिए एक्सेस का अनुरोध कर सकते हैं।

### फाइन ट्यूनिंग सपोर्ट के लिए मॉडल जांचना

1. यह Python स्क्रिप्ट Azure ML मॉडल के साथ इंटरैक्ट करती है। इसका विवरण:

    - ast मॉड्यूल इम्पोर्ट करती है, जो Python के abstract syntax trees को प्रोसेस करने के लिए फंक्शन प्रदान करता है।

    - foundation_model ऑब्जेक्ट में finetune_compute_allow_list नाम का टैग है या नहीं, यह जांचती है। Azure ML में टैग key-value जोड़े होते हैं जिनसे मॉडल को फिल्टर और सॉर्ट किया जा सकता है।

    - यदि finetune_compute_allow_list टैग मौजूद है, तो ast.literal_eval का उपयोग करके टैग के मान (स्ट्रिंग) को सुरक्षित रूप से Python लिस्ट में बदलती है और इसे computes_allow_list में असाइन करती है। फिर एक संदेश प्रिंट करती है कि कंप्यूट को इस सूची से बनाना चाहिए।

    - यदि टैग मौजूद नहीं है, तो computes_allow_list को None सेट करती है और बताती है कि finetune_compute_allow_list टैग मॉडल के टैग्स में नहीं है।

    - संक्षेप में, यह स्क्रिप्ट मॉडल के मेटाडेटा में एक खास टैग की जांच करती है, यदि मौजूद हो तो उसे लिस्ट में कन्वर्ट करती है और उपयोगकर्ता को सूचित करती है।

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

### कंप्यूट इंस्टेंस जांचना

1. यह Python स्क्रिप्ट Azure ML सेवा के साथ कंप्यूट इंस्टेंस पर कई जांच करता है। इसका विवरण:

    - compute_cluster नाम के कंप्यूट इंस्टेंस को Azure ML वर्कस्पेस से प्राप्त करने की कोशिश करता है। यदि कंप्यूट का provisioning state "failed" है, तो ValueError उठाता है।

    - जांचता है कि computes_allow_list None नहीं है। यदि नहीं, तो सूची के सभी कंप्यूट साइज़ को लोअरकेस में बदलकर देखता है कि वर्तमान कंप्यूट का साइज़ सूची में है या नहीं। यदि नहीं, तो ValueError उठाता है।

    - यदि computes_allow_list None है, तो जांचता है कि कंप्यूट साइज़ unsupported GPU VM साइज़ की सूची में तो नहीं है। यदि है, तो ValueError उठाता है।

    - वर्कस्पेस में उपलब्ध सभी कंप्यूट साइज़ की सूची प्राप्त करता है। फिर प्रत्येक साइज़ पर जाकर देखता है कि उसका नाम वर्तमान कंप्यूट साइज़ से मेल खाता है या नहीं। यदि हाँ, तो उस कंप्यूट साइज़ के GPU की संख्या प्राप्त करता है और gpu_count_found को True सेट करता है।

    - यदि gpu_count_found True है, तो कंप्यूट इंस्टेंस में GPU की संख्या प्रिंट करता है। अन्यथा, ValueError उठाता है।

    - संक्षेप में, यह स्क्रिप्ट Azure ML वर्कस्पेस में कंप्यूट इंस्टेंस की provisioning स्थिति, साइज़ की वैधता, और GPU की संख्या की जांच करता है।

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

## 4. फाइन ट्यूनिंग के लिए डेटासेट चुनें

1. हम ultrachat_200k डेटासेट का उपयोग करते हैं। इस डेटासेट के चार स्प्लिट हैं, जो Supervised fine-tuning (sft) के लिए उपयुक्त हैं। जनरेशन रैंकिंग (gen)। प्रत्येक स्प्लिट में उदाहरणों की संख्या नीचे दी गई है:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. अगले कुछ सेल फाइन ट्यूनिंग के लिए बुनियादी डेटा तैयारी दिखाते हैं:

### कुछ डेटा पंक्तियों का विज़ुअलाइज़ेशन

हम चाहते हैं कि यह नमूना जल्दी चले, इसलिए train_sft, test_sft फाइलें सेव करें जिनमें पहले से ट्रिम किए गए पंक्तियों का 5% हिस्सा हो। इसका मतलब है कि फाइन ट्यून किया गया मॉडल कम सटीक होगा, इसलिए इसे वास्तविक दुनिया में उपयोग नहीं करना चाहिए।

download-dataset.py स्क्रिप्ट ultrachat_200k डेटासेट डाउनलोड करने और इसे फाइनट्यून पाइपलाइन कंपोनेंट के लिए उपयुक्त फॉर्मेट में बदलने के लिए उपयोग होती है। चूंकि डेटासेट बड़ा है, इसलिए यहां केवल इसका एक हिस्सा है।

1. नीचे दिया गया स्क्रिप्ट केवल 5% डेटा डाउनलोड करता है। इसे बढ़ाने के लिए dataset_split_pc पैरामीटर को इच्छित प्रतिशत में बदलें।

    > [!NOTE]
    > कुछ भाषा मॉडल के अलग-अलग भाषा कोड होते हैं, इसलिए डेटासेट में कॉलम नाम उसी के अनुसार होने चाहिए।

1. डेटा इस तरह दिखना चाहिए:
चैट-कंप्लीशन डेटासेट parquet फॉर्मेट में संग्रहित है, जिसमें प्रत्येक एंट्री निम्नलिखित स्कीमा का उपयोग करती है:

    - यह JSON (JavaScript Object Notation) दस्तावेज़ है, जो डेटा आदान-प्रदान का लोकप्रिय फॉर्मेट है। यह निष्पादनीय कोड नहीं है, बल्कि डेटा स्टोर और ट्रांसपोर्ट करने का तरीका है। इसका विवरण:

    - "prompt": यह कुंजी एक स्ट्रिंग मान रखती है जो AI सहायक को दिया गया कार्य या प्रश्न दर्शाती है।

    - "messages": यह कुंजी ऑब्जेक्ट्स की एक एरे रखती है। प्रत्येक ऑब्जेक्ट एक वार्तालाप में एक संदेश को दर्शाता है, जो उपयोगकर्ता और AI सहायक के बीच होता है। प्रत्येक संदेश ऑब्जेक्ट में दो कुंजी होती हैं:

    - "content": संदेश की सामग्री को दर्शाने वाला स्ट्रिंग मान।
    - "role": संदेश भेजने वाले की भूमिका, जो "user" या "assistant" हो सकती है।
    - "prompt_id": एक यूनिक पहचानकर्ता जो प्रॉम्प्ट को दर्शाता है।

1. इस विशेष JSON दस्तावेज़ में एक बातचीत है जिसमें उपयोगकर्ता AI सहायक से एक डिस्टोपियन कहानी के नायक को बनाने के लिए कहता है। सहायक जवाब देता है, फिर उपयोगकर्ता अधिक विवरण मांगता है। सहायक सहमत होकर अधिक विवरण प्रदान करता है। पूरी बातचीत एक विशिष्ट prompt id से जुड़ी होती है।

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

### डेटा डाउनलोड करें

1. यह Python स्क्रिप्ट download-dataset.py नामक हेल्पर स्क्रिप्ट का उपयोग करके डेटासेट डाउनलोड करती है। इसका विवरण:

    - यह os मॉड्यूल इम्पोर्ट करता है, जो ऑपरेटिंग सिस्टम पर निर्भर कार्य करने के लिए पोर्टेबल तरीका प्रदान करता है।

    - os.system फंक्शन का उपयोग करके download-dataset.py स्क्रिप्ट को शेल में कमांड लाइन आर्गुमेंट्स के साथ चलाता है। आर्गुमेंट्स में डेटासेट का नाम (HuggingFaceH4/ultrachat_200k), डाउनलोड डायरेक्टरी (ultrachat_200k_dataset), और स्प्लिट प्रतिशत (5) शामिल हैं। os.system कमांड के एग्जिट स्टेटस को exit_status में स्टोर करता है।

    - यदि exit_status 0 नहीं है (जिसका मतलब कमांड सफल नहीं था), तो Exception उठाता है कि डेटासेट डाउनलोड करने में त्रुटि हुई।

    - संक्षेप में, यह स्क्रिप्ट हेल्पर स्क्रिप्ट का उपयोग करके डेटासेट डाउनलोड करती है और विफलता पर एक्सेप्शन फेंकती है।

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

### डेटा को DataFrame में लोड करना

1. यह Python स्क्रिप्ट JSON Lines फाइल को pandas DataFrame में लोड करती है और पहली 5 पंक्तियां दिखाती है। इसका विवरण:

    - pandas लाइब्रेरी इम्पोर्ट करती है, जो डेटा मैनिपुलेशन और विश्लेषण के लिए शक्तिशाली है।

    - pandas के डिस्प्ले ऑप्शंस में मैक्स कॉलम चौड़ाई 0 सेट करती है, जिससे पूरा टेक्स्ट बिना कटे दिखाई देता है।

    - pd.read_json का उपयोग करके ultrachat_200k_dataset डायरेक्टरी से train_sft.jsonl फाइल को लोड करती है। lines=True का मतलब है कि फाइल JSON Lines फॉर्मेट में है, जहां प्रत्येक लाइन एक अलग JSON ऑब्जेक्ट है।

    - head मेथड से पहली 5 पंक्तियां दिखाती है। यदि कुल पंक्तियां 5 से कम हैं तो सारी दिखाएगी।

    - संक्षेप में, यह स्क्रिप्ट JSON Lines फाइल को DataFrame में लोड करती है और पहले 5 पंक्तियों को पूरा टेक्स्ट दिखाते हुए प्रदर्शित करती है।

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

## 5. मॉडल और डेटा को इनपुट के रूप में उपयोग करके फाइन ट्यूनिंग जॉब सबमिट करें

चैट-कंप्लीशन पाइपलाइन कंपोनेंट का उपयोग करने वाला जॉब बनाएं। फाइन ट्यूनिंग के लिए समर्थित सभी पैरामीटरों के बारे में अधिक जानें।

### फाइनट्यून पैरामीटर परिभाषित करें

1. फाइनट्यून पैरामीटर दो श्रेणियों में बांटे जा सकते हैं - ट्रेनिंग पैरामीटर और ऑप्टिमाइजेशन पैरामीटर।

1. ट्रेनिंग पैरामीटर ट्रेनिंग के पहलुओं को परिभाषित करते हैं जैसे -

    - उपयोग करने वाला ऑप्टिमाइज़र, शेड्यूलर
    - फाइनट्यून के लिए ऑप्टिमाइज़ करने वाला मेट्रिक
    - ट्रेनिंग स्टेप्स की संख्या, बैच साइज आदि
    - ऑप्टिमाइजेशन पैरामीटर GPU मेमोरी को बेहतर उपयोग करने और कंप्यूट संसाधनों का कुशलतापूर्वक उपयोग करने में मदद करते हैं।

1. नीचे कुछ पैरामीटर हैं जो इस श्रेणी में आते हैं। ऑप्टिमाइजेशन पैरामीटर हर मॉडल के लिए अलग होते हैं और मॉडल के साथ पैकेज्ड होते हैं ताकि इन भिन्नताओं को संभाला जा सके।

    - Deepspeed और LoRA सक्षम करें
    - मिक्स्ड प्रिसिजन ट्रेनिंग सक्षम करें
    - मल्टी-नोड ट्रेनिंग सक्षम करें

> [!NOTE]
> सुपरवाइज्ड फाइनट्यूनिंग से अलाइनमेंट खोने या कैटास्ट्रॉफिक फॉरगेटिंग हो सकता है। हम सलाह देते हैं कि इस समस्या की जांच करें और फाइनट्यूनिंग के बाद एक अलाइनमेंट चरण चलाएं।

### फाइन ट्यूनिंग पैरामीटर

1. यह Python स्क्रिप्ट मशीन लर्निंग मॉडल के फाइन-ट्यूनिंग के लिए पैरामीटर सेट कर रही है। इसका विवरण:

    - यह डिफ़ॉल्ट ट्रेनिंग पैरामीटर सेट करती है जैसे ट्रेनिंग epochs की संख्या, ट्रेनिंग और इवैल्युएशन के लिए बैच साइज, लर्निंग रेट, और लर्निंग रेट शेड्यूलर टाइप।

    - डिफ़ॉल्ट ऑप्टिमाइजेशन पैरामीटर सेट करती है जैसे Layer-wise Relevance Propagation (LoRa) और DeepSpeed को लागू करना, और DeepSpeed स्टेज।

    - ट्रेनिंग और
training pipeline विभिन्न पैरामीटरों के आधार पर बनाया गया है, और फिर इस display name को प्रिंट किया जा रहा है। ```python
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

### Pipeline को कॉन्फ़िगर करना

यह Python स्क्रिप्ट Azure Machine Learning SDK का उपयोग करके एक मशीन लर्निंग pipeline को परिभाषित और कॉन्फ़िगर कर रही है। इसका विवरण इस प्रकार है:

1. यह Azure AI ML SDK से आवश्यक मॉड्यूल इम्पोर्ट करता है।
2. यह registry से "chat_completion_pipeline" नामक pipeline component प्राप्त करता है।
3. यह `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False` का उपयोग करके pipeline job को परिभाषित करता है, जिसका मतलब है कि pipeline किसी भी step के फेल होने पर रुक जाएगा।
4. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning SDK का उपयोग करके chat completion टास्क के लिए एक मशीन लर्निंग pipeline को परिभाषित और कॉन्फ़िगर कर रही है।

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

### Job सबमिट करना

1. यह Python स्क्रिप्ट Azure Machine Learning workspace में एक मशीन लर्निंग pipeline job सबमिट कर रही है और फिर job के पूरा होने का इंतजार कर रही है। इसका विवरण इस प्रकार है:

- यह workspace_ml_client के jobs ऑब्जेक्ट के create_or_update मेथड को कॉल करता है ताकि pipeline job सबमिट किया जा सके। pipeline_object उस pipeline को दर्शाता है जिसे चलाया जाना है, और experiment_name उस experiment को दर्शाता है जिसके अंतर्गत job चलाया जाता है।
- फिर यह workspace_ml_client के jobs ऑब्जेक्ट के stream मेथड को कॉल करता है ताकि pipeline job के पूरा होने तक इंतजार किया जा सके। इंतजार करने वाला job pipeline_job ऑब्जेक्ट के name attribute द्वारा निर्दिष्ट होता है।
- संक्षेप में, यह स्क्रिप्ट Azure Machine Learning workspace में एक मशीन लर्निंग pipeline job सबमिट कर रही है और फिर job के पूरा होने का इंतजार कर रही है।

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

## 6. Fine tuned मॉडल को workspace में रजिस्टर करना

हम fine tuning job के आउटपुट से मॉडल को रजिस्टर करेंगे। यह fine tuned मॉडल और fine tuning job के बीच lineage को ट्रैक करेगा। fine tuning job आगे foundation मॉडल, डेटा और training कोड के साथ lineage को ट्रैक करता है।

### ML मॉडल रजिस्टर करना

1. यह Python स्क्रिप्ट Azure Machine Learning pipeline में प्रशिक्षित मशीन लर्निंग मॉडल को रजिस्टर कर रही है। इसका विवरण इस प्रकार है:

- यह Azure AI ML SDK से आवश्यक मॉड्यूल इम्पोर्ट करता है।
- यह pipeline job से trained_model आउटपुट उपलब्ध है या नहीं, यह workspace_ml_client के jobs ऑब्जेक्ट के get मेथड को कॉल करके और उसके outputs attribute को एक्सेस करके जांचता है।
- यह pipeline job के नाम और आउटपुट ("trained_model") के नाम को फॉर्मेट करके प्रशिक्षित मॉडल का पथ बनाता है।
- यह fine-tuned मॉडल के लिए एक नाम परिभाषित करता है, जिसमें मूल मॉडल के नाम के बाद "-ultrachat-200k" जोड़ा जाता है और किसी भी स्लैश को हाइफ़न से बदल दिया जाता है।
- यह Model ऑब्जेक्ट बनाकर मॉडल को रजिस्टर करने की तैयारी करता है, जिसमें मॉडल का पथ, मॉडल का प्रकार (MLflow मॉडल), मॉडल का नाम और संस्करण, और मॉडल का विवरण शामिल है।
- यह workspace_ml_client के models ऑब्जेक्ट के create_or_update मेथड को कॉल करके मॉडल को रजिस्टर करता है।
- यह रजिस्टर्ड मॉडल को प्रिंट करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning pipeline में प्रशिक्षित मशीन लर्निंग मॉडल को रजिस्टर कर रही है।

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

## 7. Fine tuned मॉडल को ऑनलाइन endpoint पर डिप्लॉय करना

ऑनलाइन endpoints एक स्थायी REST API प्रदान करते हैं जिसका उपयोग उन एप्लिकेशन के साथ इंटीग्रेट करने के लिए किया जा सकता है जिन्हें मॉडल का उपयोग करना होता है।

### Endpoint प्रबंधन

1. यह Python स्क्रिप्ट Azure Machine Learning में रजिस्टर्ड मॉडल के लिए एक मैनेज्ड ऑनलाइन endpoint बना रही है। इसका विवरण इस प्रकार है:

- यह Azure AI ML SDK से आवश्यक मॉड्यूल इम्पोर्ट करता है।
- यह "ultrachat-completion-" स्ट्रिंग के साथ एक timestamp जोड़कर ऑनलाइन endpoint के लिए एक यूनिक नाम परिभाषित करता है।
- यह ManagedOnlineEndpoint ऑब्जेक्ट बनाकर ऑनलाइन endpoint बनाने की तैयारी करता है, जिसमें endpoint का नाम, विवरण, और authentication मोड ("key") शामिल हैं।
- यह workspace_ml_client के begin_create_or_update मेथड को कॉल करके ऑनलाइन endpoint बनाता है और फिर wait मेथड को कॉल करके निर्माण प्रक्रिया के पूरा होने तक इंतजार करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning में रजिस्टर्ड मॉडल के लिए एक मैनेज्ड ऑनलाइन endpoint बना रही है।

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
> आप यहाँ deployment के लिए समर्थित SKU की सूची देख सकते हैं - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML मॉडल डिप्लॉय करना

1. यह Python स्क्रिप्ट Azure Machine Learning में एक मैनेज्ड ऑनलाइन endpoint पर रजिस्टर्ड मशीन लर्निंग मॉडल को डिप्लॉय कर रही है। इसका विवरण इस प्रकार है:

- यह ast मॉड्यूल इम्पोर्ट करता है, जो Python के abstract syntax grammar के पेड़ों को प्रोसेस करने के लिए फंक्शन प्रदान करता है।
- यह डिप्लॉयमेंट के लिए instance type को "Standard_NC6s_v3" पर सेट करता है।
- यह foundation मॉडल में inference_compute_allow_list टैग मौजूद है या नहीं, यह जांचता है। यदि है, तो यह टैग के मान को स्ट्रिंग से Python सूची में कन्वर्ट करता है और उसे inference_computes_allow_list में असाइन करता है। यदि नहीं है, तो इसे None सेट करता है।
- यह जांचता है कि निर्दिष्ट instance type allow list में है या नहीं। यदि नहीं, तो यह उपयोगकर्ता को allow list से instance type चुनने का संदेश प्रिंट करता है।
- यह ManagedOnlineDeployment ऑब्जेक्ट बनाकर डिप्लॉयमेंट बनाने की तैयारी करता है, जिसमें डिप्लॉयमेंट का नाम, endpoint का नाम, मॉडल का ID, instance type और count, liveness probe सेटिंग्स, और request सेटिंग्स शामिल हैं।
- यह workspace_ml_client के begin_create_or_update मेथड को कॉल करके डिप्लॉयमेंट बनाता है और फिर wait मेथड को कॉल करके निर्माण प्रक्रिया के पूरा होने तक इंतजार करता है।
- यह endpoint के ट्रैफिक को सेट करता है ताकि 100% ट्रैफिक "demo" डिप्लॉयमेंट को जाए।
- यह workspace_ml_client के begin_create_or_update मेथड को कॉल करके endpoint को अपडेट करता है और फिर result मेथड को कॉल करके अपडेट प्रक्रिया के पूरा होने तक इंतजार करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning में एक मैनेज्ड ऑनलाइन endpoint पर रजिस्टर्ड मशीन लर्निंग मॉडल को डिप्लॉय कर रही है।

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

## 8. Sample डेटा के साथ endpoint का परीक्षण करना

हम test dataset से कुछ sample डेटा लेंगे और inference के लिए ऑनलाइन endpoint को सबमिट करेंगे। फिर हम स्कोर किए गए लेबल्स को ground truth लेबल्स के साथ दिखाएंगे।

### परिणाम पढ़ना

1. यह Python स्क्रिप्ट एक JSON Lines फाइल को pandas DataFrame में पढ़ रही है, एक रैंडम सैंपल ले रही है, और इंडेक्स रीसेट कर रही है। इसका विवरण इस प्रकार है:

- यह ./ultrachat_200k_dataset/test_gen.jsonl फाइल को pandas DataFrame में पढ़ता है। read_json फंक्शन को lines=True आर्गुमेंट के साथ उपयोग किया जाता है क्योंकि फाइल JSON Lines फॉर्मेट में है, जहां हर लाइन एक अलग JSON ऑब्जेक्ट होती है।
- यह DataFrame से 1 रैंडम रो का सैंपल लेता है। sample फंक्शन को n=1 आर्गुमेंट के साथ उपयोग किया जाता है ताकि एक रैंडम रो चुनी जा सके।
- यह DataFrame का इंडेक्स रीसेट करता है। reset_index फंक्शन को drop=True आर्गुमेंट के साथ उपयोग किया जाता है ताकि मूल इंडेक्स हटाकर नया डिफ़ॉल्ट पूर्णांक इंडेक्स बनाया जा सके।
- यह head फंक्शन के साथ 2 रो दिखाता है, लेकिन चूंकि सैंपलिंग के बाद DataFrame में केवल एक रो होती है, इसलिए यह केवल उस एक रो को ही दिखाएगा।

1. संक्षेप में, यह स्क्रिप्ट एक JSON Lines फाइल को pandas DataFrame में पढ़ रही है, एक रो का रैंडम सैंपल ले रही है, इंडेक्स रीसेट कर रही है, और पहली रो को दिखा रही है।

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

### JSON ऑब्जेक्ट बनाना

1. यह Python स्क्रिप्ट विशेष पैरामीटरों के साथ एक JSON ऑब्जेक्ट बना रही है और उसे फाइल में सेव कर रही है। इसका विवरण इस प्रकार है:

- यह json मॉड्यूल इम्पोर्ट करता है, जो JSON डेटा के साथ काम करने के लिए फंक्शन प्रदान करता है।
- यह parameters नामक एक dictionary बनाता है, जिसमें मशीन लर्निंग मॉडल के पैरामीटर होते हैं। keys हैं "temperature", "top_p", "do_sample", और "max_new_tokens", जिनके मान क्रमशः 0.6, 0.9, True, और 200 हैं।
- यह एक और dictionary test_json बनाता है, जिसमें दो keys हैं: "input_data" और "params"। "input_data" का मान एक dictionary है जिसमें "input_string" और "parameters" keys हैं। "input_string" में test_df DataFrame के पहले संदेश की एक सूची होती है। "parameters" में पहले बनाए गए parameters dictionary होता है। "params" एक खाली dictionary है।
- यह sample_score.json नामक फाइल खोलता है।

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

### Endpoint को कॉल करना

1. यह Python स्क्रिप्ट Azure Machine Learning में एक ऑनलाइन endpoint को कॉल करके JSON फाइल को स्कोर कर रही है। इसका विवरण इस प्रकार है:

- यह workspace_ml_client ऑब्जेक्ट के online_endpoints प्रॉपर्टी के invoke मेथड को कॉल करता है। यह मेथड ऑनलाइन endpoint को अनुरोध भेजने और प्रतिक्रिया प्राप्त करने के लिए उपयोग किया जाता है।
- यह endpoint का नाम और डिप्लॉयमेंट नाम endpoint_name और deployment_name आर्गुमेंट्स के रूप में निर्दिष्ट करता है। इस मामले में, endpoint का नाम online_endpoint_name वेरिएबल में स्टोर है और डिप्लॉयमेंट का नाम "demo" है।
- यह स्कोर करने के लिए JSON फाइल का पथ request_file आर्गुमेंट के रूप में देता है। इस मामले में फाइल ./ultrachat_200k_dataset/sample_score.json है।
- यह endpoint से प्रतिक्रिया response वेरिएबल में स्टोर करता है।
- यह raw response को प्रिंट करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning में एक ऑनलाइन endpoint को कॉल करके JSON फाइल को स्कोर कर रही है और प्रतिक्रिया प्रिंट कर रही है।

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

## 9. ऑनलाइन endpoint को डिलीट करना

1. ऑनलाइन endpoint को डिलीट करना न भूलें, अन्यथा endpoint द्वारा उपयोग किए गए compute के लिए बिलिंग चालू रहेगी। यह Python कोड Azure Machine Learning में एक ऑनलाइन endpoint को डिलीट कर रहा है। इसका विवरण इस प्रकार है:

- यह workspace_ml_client ऑब्जेक्ट के online_endpoints प्रॉपर्टी के begin_delete मेथड को कॉल करता है। यह मेथड ऑनलाइन endpoint को डिलीट करने की प्रक्रिया शुरू करता है।
- यह डिलीट किए जाने वाले endpoint का नाम name आर्गुमेंट के रूप में निर्दिष्ट करता है। इस मामले में, endpoint का नाम online_endpoint_name वेरिएबल में स्टोर है।
- यह wait मेथड को कॉल करता है ताकि डिलीट ऑपरेशन के पूरा होने तक इंतजार किया जा सके। यह एक blocking ऑपरेशन है, यानी स्क्रिप्ट तब तक आगे नहीं बढ़ेगी जब तक डिलीट पूरा नहीं हो जाता।
- संक्षेप में, यह कोड Azure Machine Learning में एक ऑनलाइन endpoint को डिलीट करने की प्रक्रिया शुरू करता है और ऑपरेशन के पूरा होने तक इंतजार करता है।

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। हम सटीकता के लिए प्रयासरत हैं, लेकिन कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।