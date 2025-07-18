<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:09:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "hi"
}
-->
## Azure ML सिस्टम रजिस्ट्री से चैट-कम्प्लीशन कंपोनेंट्स का उपयोग करके मॉडल को फाइन ट्यून कैसे करें

इस उदाहरण में हम Phi-3-mini-4k-instruct मॉडल का फाइन ट्यूनिंग करेंगे ताकि ultrachat_200k डेटासेट का उपयोग करके दो लोगों के बीच बातचीत पूरी की जा सके।

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.hi.png)

यह उदाहरण आपको दिखाएगा कि Azure ML SDK और Python का उपयोग करके फाइन ट्यूनिंग कैसे करें और फिर फाइन ट्यून किए गए मॉडल को रियल टाइम इनफेरेंस के लिए ऑनलाइन एंडपॉइंट पर कैसे डिप्लॉय करें।

### प्रशिक्षण डेटा

हम ultrachat_200k डेटासेट का उपयोग करेंगे। यह UltraChat डेटासेट का एक काफ़ी फ़िल्टर्ड संस्करण है और इसका उपयोग Zephyr-7B-β, एक अत्याधुनिक 7b चैट मॉडल को प्रशिक्षित करने के लिए किया गया था।

### मॉडल

हम Phi-3-mini-4k-instruct मॉडल का उपयोग करेंगे ताकि दिखा सकें कि उपयोगकर्ता चैट-कम्प्लीशन टास्क के लिए मॉडल को कैसे फाइन ट्यून कर सकता है। यदि आपने यह नोटबुक किसी विशेष मॉडल कार्ड से खोला है, तो कृपया उस मॉडल का नाम बदलना न भूलें।

### कार्य

- फाइन ट्यून करने के लिए एक मॉडल चुनें।
- प्रशिक्षण डेटा चुनें और एक्सप्लोर करें।
- फाइन ट्यूनिंग जॉब को कॉन्फ़िगर करें।
- फाइन ट्यूनिंग जॉब चलाएं।
- प्रशिक्षण और मूल्यांकन मेट्रिक्स की समीक्षा करें।
- फाइन ट्यून किए गए मॉडल को रजिस्टर करें।
- रियल टाइम इनफेरेंस के लिए फाइन ट्यून किए गए मॉडल को डिप्लॉय करें।
- संसाधनों की सफाई करें।

## 1. आवश्यकताएँ सेटअप करें

- डिपेंडेंसी इंस्टॉल करें
- AzureML वर्कस्पेस से कनेक्ट करें। अधिक जानने के लिए सेट अप SDK authentication देखें। नीचे <WORKSPACE_NAME>, <RESOURCE_GROUP> और <SUBSCRIPTION_ID> को बदलें।
- azureml सिस्टम रजिस्ट्री से कनेक्ट करें
- वैकल्पिक रूप से एक experiment नाम सेट करें
- कंप्यूट चेक करें या बनाएं।

> [!NOTE]
> आवश्यकताएँ: एक सिंगल GPU नोड में कई GPU कार्ड हो सकते हैं। उदाहरण के लिए, Standard_NC24rs_v3 के एक नोड में 4 NVIDIA V100 GPUs होते हैं जबकि Standard_NC12s_v3 में 2 NVIDIA V100 GPUs होते हैं। इस जानकारी के लिए डॉक्यूमेंट्स देखें। प्रति नोड GPU कार्ड की संख्या नीचे param gpus_per_node में सेट की जाती है। इसे सही सेट करने से नोड के सभी GPUs का उपयोग सुनिश्चित होगा। अनुशंसित GPU compute SKUs यहाँ और यहाँ देखे जा सकते हैं।

### Python लाइब्रेरीज़

नीचे दिए गए सेल को चलाकर डिपेंडेंसी इंस्टॉल करें। यदि आप नए वातावरण में काम कर रहे हैं तो यह वैकल्पिक कदम नहीं है।

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

    - यह DefaultAzureCredential() का उपयोग करके ऑथेंटिकेट करने की कोशिश करता है, जो Azure क्लाउड में एप्लिकेशन तेजी से विकसित करने के लिए सरल ऑथेंटिकेशन अनुभव प्रदान करता है। यदि यह विफल होता है, तो InteractiveBrowserCredential() का उपयोग करता है, जो इंटरैक्टिव लॉगिन प्रॉम्प्ट देता है।

    - फिर यह from_config मेथड का उपयोग करके MLClient इंस्टेंस बनाने की कोशिश करता है, जो डिफ़ॉल्ट कॉन्फ़िग फाइल (config.json) से कॉन्फ़िगरेशन पढ़ता है। यदि यह विफल होता है, तो यह मैन्युअली subscription_id, resource_group_name, और workspace_name प्रदान करके MLClient बनाता है।

    - यह एक और MLClient इंस्टेंस बनाता है, इस बार Azure ML रजिस्ट्री "azureml" के लिए। यह रजिस्ट्री वह जगह है जहाँ मॉडल, फाइन-ट्यूनिंग पाइपलाइंस, और एनवायरनमेंट्स स्टोर होते हैं।

    - यह experiment_name को "chat_completion_Phi-3-mini-4k-instruct" सेट करता है।

    - यह एक यूनिक टाइमस्टैम्प जनरेट करता है, जो वर्तमान समय (सेकंड में, फ्लोटिंग पॉइंट नंबर के रूप में) को इंटीजर में बदलकर और फिर स्ट्रिंग में कन्वर्ट करके बनाया जाता है। यह टाइमस्टैम्प यूनिक नाम और वर्शन बनाने के लिए उपयोग किया जा सकता है।

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

1. Phi-3-mini-4k-instruct एक 3.8B पैरामीटर्स वाला, हल्का, अत्याधुनिक ओपन मॉडल है जो Phi-2 के लिए उपयोग किए गए डेटासेट्स पर आधारित है। यह मॉडल Phi-3 मॉडल परिवार का हिस्सा है, और मिनी वर्शन दो प्रकारों में आता है: 4K और 128K, जो संदर्भ लंबाई (टोकन में) को दर्शाता है जिसे यह सपोर्ट कर सकता है। हमें इसे अपने विशेष उद्देश्य के लिए फाइन ट्यून करना होगा। आप AzureML स्टूडियो के मॉडल कैटलॉग में चैट-कम्प्लीशन टास्क के अनुसार इन मॉडलों को ब्राउज़ कर सकते हैं। इस उदाहरण में, हम Phi-3-mini-4k-instruct मॉडल का उपयोग कर रहे हैं। यदि आपने यह नोटबुक किसी अन्य मॉडल के लिए खोला है, तो मॉडल का नाम और वर्शन बदलें।

    > [!NOTE]
    > मॉडल की id प्रॉपर्टी। इसे फाइन ट्यूनिंग जॉब के इनपुट के रूप में पास किया जाएगा। यह AzureML स्टूडियो मॉडल कैटलॉग के मॉडल डिटेल्स पेज में Asset ID फील्ड के रूप में भी उपलब्ध है।

2. यह Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा के साथ इंटरैक्ट कर रही है। इसका विवरण इस प्रकार है:

    - यह model_name को "Phi-3-mini-4k-instruct" सेट करता है।

    - यह registry_ml_client ऑब्जेक्ट के models प्रॉपर्टी के get मेथड का उपयोग करके Azure ML रजिस्ट्री से निर्दिष्ट नाम वाले मॉडल का नवीनतम संस्करण प्राप्त करता है। get मेथड को दो आर्गुमेंट्स दिए जाते हैं: मॉडल का नाम और एक लेबल जो बताता है कि नवीनतम संस्करण प्राप्त करना है।

    - यह कंसोल में एक संदेश प्रिंट करता है जिसमें बताया जाता है कि फाइन-ट्यूनिंग के लिए कौन सा मॉडल नाम, वर्शन, और id उपयोग किया जाएगा। स्ट्रिंग के format मेथड का उपयोग करके मॉडल के नाम, वर्शन, और id को संदेश में डाला जाता है। ये प्रॉपर्टीज foundation_model ऑब्जेक्ट से ली जाती हैं।

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

फाइनट्यून जॉब केवल GPU कंप्यूट के साथ काम करता है। कंप्यूट का आकार इस बात पर निर्भर करता है कि मॉडल कितना बड़ा है और अधिकांश मामलों में सही कंप्यूट चुनना चुनौतीपूर्ण होता है। इस सेल में, हम उपयोगकर्ता को सही कंप्यूट चुनने में मार्गदर्शन करते हैं।

> [!NOTE]
> नीचे सूचीबद्ध कंप्यूट सबसे अनुकूलित कॉन्फ़िगरेशन के साथ काम करते हैं। कॉन्फ़िगरेशन में कोई भी बदलाव Cuda Out Of Memory त्रुटि का कारण बन सकता है। ऐसे मामलों में, कंप्यूट को बड़े आकार में अपग्रेड करने का प्रयास करें।

> [!NOTE]
> compute_cluster_size चुनते समय सुनिश्चित करें कि कंप्यूट आपके रिसोर्स ग्रुप में उपलब्ध हो। यदि कोई विशेष कंप्यूट उपलब्ध नहीं है, तो कंप्यूट संसाधनों तक पहुंच के लिए अनुरोध कर सकते हैं।

### फाइन ट्यूनिंग सपोर्ट के लिए मॉडल की जांच

1. यह Python स्क्रिप्ट Azure ML मॉडल के साथ इंटरैक्ट कर रही है। इसका विवरण इस प्रकार है:

    - यह ast मॉड्यूल इम्पोर्ट करता है, जो Python के abstract syntax grammar के ट्री को प्रोसेस करने के लिए फंक्शंस प्रदान करता है।

    - यह जांचता है कि foundation_model ऑब्जेक्ट (जो Azure ML में एक मॉडल का प्रतिनिधित्व करता है) में finetune_compute_allow_list नाम का टैग है या नहीं। Azure ML में टैग key-value जोड़े होते हैं जिन्हें आप मॉडल को फ़िल्टर और सॉर्ट करने के लिए बना सकते हैं।

    - यदि finetune_compute_allow_list टैग मौजूद है, तो यह ast.literal_eval फंक्शन का उपयोग करके टैग के मान (जो एक स्ट्रिंग है) को सुरक्षित रूप से Python लिस्ट में पार्स करता है। इस लिस्ट को computes_allow_list वेरिएबल में असाइन किया जाता है। फिर यह एक संदेश प्रिंट करता है कि कंप्यूट को इस लिस्ट से बनाना चाहिए।

    - यदि finetune_compute_allow_list टैग मौजूद नहीं है, तो यह computes_allow_list को None सेट करता है और एक संदेश प्रिंट करता है कि finetune_compute_allow_list टैग मॉडल के टैग्स का हिस्सा नहीं है।

    - संक्षेप में, यह स्क्रिप्ट मॉडल के मेटाडेटा में एक विशेष टैग की जांच कर रही है, यदि मौजूद हो तो टैग के मान को लिस्ट में बदल रही है, और उपयोगकर्ता को उपयुक्त फीडबैक दे रही है।

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

### कंप्यूट इंस्टेंस की जांच

1. यह Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा के साथ इंटरैक्ट कर रही है और एक कंप्यूट इंस्टेंस पर कई जांच कर रही है। इसका विवरण इस प्रकार है:

    - यह Azure ML वर्कस्पेस से compute_cluster नाम के कंप्यूट इंस्टेंस को प्राप्त करने की कोशिश करता है। यदि कंप्यूट इंस्टेंस की provisioning state "failed" है, तो यह ValueError उठाता है।

    - यह जांचता है कि computes_allow_list None नहीं है। यदि ऐसा है, तो यह लिस्ट के सभी कंप्यूट साइज़ को लोअरकेस में बदलता है और देखता है कि वर्तमान कंप्यूट इंस्टेंस का साइज़ इस लिस्ट में है या नहीं। यदि नहीं, तो यह ValueError उठाता है।

    - यदि computes_allow_list None है, तो यह जांचता है कि कंप्यूट इंस्टेंस का साइज़ unsupported GPU VM साइज़ की लिस्ट में है या नहीं। यदि है, तो यह ValueError उठाता है।

    - यह वर्कस्पेस में उपलब्ध सभी कंप्यूट साइज़ की लिस्ट प्राप्त करता है। फिर इस लिस्ट पर इटरेट करता है, और प्रत्येक कंप्यूट साइज़ के लिए जांचता है कि क्या उसका नाम वर्तमान कंप्यूट इंस्टेंस के साइज़ से मेल खाता है। यदि हाँ, तो यह उस कंप्यूट साइज़ के GPU की संख्या प्राप्त करता है और gpu_count_found को True सेट करता है।

    - यदि gpu_count_found True है, तो यह कंप्यूट इंस्टेंस में GPU की संख्या प्रिंट करता है। यदि False है, तो यह ValueError उठाता है।

    - संक्षेप में, यह स्क्रिप्ट Azure ML वर्कस्पेस में एक कंप्यूट इंस्टेंस की provisioning स्थिति, साइज़ को allow या deny लिस्ट के खिलाफ जांचती है, और GPU की संख्या की पुष्टि करती है।

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

## 4. मॉडल के फाइन-ट्यूनिंग के लिए डेटासेट चुनें

1. हम ultrachat_200k डेटासेट का उपयोग करते हैं। इस डेटासेट में चार स्प्लिट्स हैं, जो Supervised fine-tuning (sft) के लिए उपयुक्त हैं। Generation ranking (gen)। प्रत्येक स्प्लिट में उदाहरणों की संख्या निम्नानुसार है:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. अगले कुछ सेल फाइन ट्यूनिंग के लिए बेसिक डेटा तैयारी दिखाते हैं:

### कुछ डेटा पंक्तियों का विज़ुअलाइज़ेशन

हम चाहते हैं कि यह सैंपल जल्दी चले, इसलिए train_sft, test_sft फाइलों में पहले से ट्रिम किए गए पंक्तियों का 5% सेव करें। इसका मतलब है कि फाइन ट्यून किया गया मॉडल कम सटीक होगा, इसलिए इसे वास्तविक दुनिया में उपयोग नहीं किया जाना चाहिए।  
download-dataset.py का उपयोग ultrachat_200k डेटासेट डाउनलोड करने और डेटासेट को फाइनट्यून पाइपलाइन कंपोनेंट के लिए उपयुक्त फॉर्मेट में ट्रांसफॉर्म करने के लिए किया जाता है। चूंकि डेटासेट बड़ा है, इसलिए यहाँ केवल इसका एक हिस्सा है।

1. नीचे दिया गया स्क्रिप्ट केवल 5% डेटा डाउनलोड करता है। इसे dataset_split_pc पैरामीटर को इच्छित प्रतिशत में बदलकर बढ़ाया जा सकता है।

    > [!NOTE]
    > कुछ भाषा मॉडल के अलग-अलग भाषा कोड होते हैं, इसलिए डेटासेट में कॉलम नामों को भी उसी के अनुसार होना चाहिए।

1. डेटा इस प्रकार दिखना चाहिए:  
चैट-कम्प्लीशन डेटासेट parquet फॉर्मेट में स्टोर होता है, जिसमें प्रत्येक एंट्री निम्नलिखित स्कीमा का उपयोग करती है:

    - यह एक JSON (JavaScript Object Notation) डॉक्यूमेंट है, जो एक लोकप्रिय डेटा इंटरचेंज फॉर्मेट है। यह executable कोड नहीं है, बल्कि डेटा स्टोर और ट्रांसपोर्ट करने का तरीका है। इसका विवरण इस प्रकार है:

    - "prompt": यह key एक स्ट्रिंग वैल्यू रखती है जो AI असिस्टेंट को दिया गया टास्क या प्रश्न दर्शाती है।

    - "messages": यह key ऑब्जेक्ट्स की एक एरे रखती है। प्रत्येक ऑब्जेक्ट एक बातचीत में एक संदेश का प्रतिनिधित्व करता है जो उपयोगकर्ता और AI असिस्टेंट के बीच होता है। प्रत्येक संदेश ऑब्जेक्ट में दो keys होती हैं:

    - "content": यह key संदेश की सामग्री को स्ट्रिंग के रूप में रखती है।  
    - "role": यह key उस इकाई की भूमिका को स्ट्रिंग के रूप में रखती है जिसने संदेश भेजा है। यह "user" या "assistant" हो सकता है।  
    - "prompt_id": यह key उस प्रॉम्प्ट का यूनिक पहचानकर्ता स्ट्रिंग के रूप में रखती है।

1. इस विशेष JSON डॉक्यूमेंट में, एक बातचीत दर्शाई गई है जहाँ उपयोगकर्ता AI असिस्टेंट से एक dystopian कहानी के लिए मुख्य पात्र बनाने को कहता है। असिस्टेंट जवाब देता है, और फिर उपयोगकर्ता अधिक विवरण मांगता है। असिस्टेंट अधिक विवरण देने के लिए सहमत होता है। पूरी बातचीत एक विशिष्ट prompt_id से जुड़ी होती है।

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

1. यह Python स्क्रिप्ट एक हेल्पर स्क्रिप्ट download-dataset.py का उपयोग करके डेटासेट डाउनलोड करने के लिए है। इसका विवरण इस प्रकार है:

    - यह os मॉड्यूल इम्पोर्ट करता है, जो ऑपरेटिंग सिस्टम पर निर्भर कार्यक्षमता का पोर्टेबल तरीका प्रदान करता है।

    - यह os.system फंक्शन का उपयोग करके shell में download-dataset.py स्क्रिप्ट को विशिष्ट कमांड-लाइन आर्गुमेंट्स के साथ चलाता है। आर्गुमेंट्स में डाउनलोड करने के लिए डेटासेट (HuggingFaceH4/ultrachat_200k), डाउनलोड डायरेक्टरी (ultrachat_200k_dataset), और डेटासेट को स्प्लिट करने का प्रतिशत (5) शामिल हैं। os.system कमांड के exit status को exit_status वेरिएबल में स्टोर करता है।

    - यह जांचता है कि exit_status 0 नहीं है। Unix जैसे ऑपरेटिंग सिस्टम में, 0 का exit status आमतौर पर सफलता दर्शाता है, जबकि कोई भी अन्य संख्या त्रुटि को। यदि exit_status 0 नहीं है, तो यह एक Exception उठाता है जिसमें डेटासेट डाउनलोड में त्रुटि का संदेश होता है।

    - संक्षेप में, यह स्क्रिप्ट एक हेल्पर स्क्रिप्ट का उपयोग करके डेटासेट डाउनलोड करने के लिए कमांड चलाती है, और यदि कमांड विफल होती है तो Exception उठाती है।

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

1. यह Python स्क्रिप्ट JSON Lines फाइल को pandas DataFrame में लोड कर रही है और पहले 5 पंक्तियाँ दिखा रही है। इसका विवरण इस प्रकार है:

    - यह pandas लाइब्रेरी इम्पोर्ट करता है, जो एक शक्तिशाली डेटा मैनिपुलेशन और विश्लेषण लाइब्रेरी है।

    - यह pandas के डिस्प्ले ऑप्शंस में अधिकतम कॉलम चौड़ाई को 0 सेट करता है। इसका मतलब है कि DataFrame प्रिंट करते समय प्रत्येक कॉलम का पूरा टेक्स्ट बिना कटाव के दिखेगा।

    - यह pd.read_json फंक्शन का उपयोग करके ultrachat_200k_dataset डायरेक्टरी से train_sft.jsonl फाइल को DataFrame में लोड करता है। lines=True आर्गुमेंट बताता है कि फाइल JSON Lines फॉर्मेट में है, जहाँ प्रत्येक लाइन एक अलग JSON ऑब्जेक्ट होती है।
- यह DataFrame की पहली 5 पंक्तियाँ दिखाने के लिए head मेथड का उपयोग करता है। यदि DataFrame में 5 से कम पंक्तियाँ हैं, तो यह सभी को दिखाएगा।

- संक्षेप में, यह स्क्रिप्ट एक JSON Lines फ़ाइल को DataFrame में लोड कर रही है और पहले 5 पंक्तियों को पूर्ण कॉलम टेक्स्ट के साथ प्रदर्शित कर रही है।

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

ऐसा जॉब बनाएं जो chat-completion पाइपलाइन कंपोनेंट का उपयोग करता हो। फाइन ट्यूनिंग के लिए समर्थित सभी पैरामीटर के बारे में अधिक जानें।

### फाइनट्यून पैरामीटर परिभाषित करें

1. फाइनट्यून पैरामीटर को दो श्रेणियों में बांटा जा सकता है - प्रशिक्षण पैरामीटर, अनुकूलन पैरामीटर

1. प्रशिक्षण पैरामीटर प्रशिक्षण के पहलुओं को परिभाषित करते हैं जैसे -

    - उपयोग करने वाला optimizer, scheduler
    - फाइनट्यून को optimize करने के लिए मेट्रिक
    - प्रशिक्षण चरणों की संख्या, बैच साइज आदि
    - अनुकूलन पैरामीटर GPU मेमोरी को अनुकूलित करने और कंप्यूट संसाधनों का प्रभावी उपयोग करने में मदद करते हैं।

1. नीचे कुछ पैरामीटर दिए गए हैं जो इस श्रेणी में आते हैं। अनुकूलन पैरामीटर प्रत्येक मॉडल के लिए भिन्न होते हैं और मॉडल के साथ पैकेज किए जाते हैं ताकि इन भिन्नताओं को संभाला जा सके।

    - deepspeed और LoRA को सक्षम करें
    - मिश्रित प्रिसिजन प्रशिक्षण सक्षम करें
    - मल्टी-नोड प्रशिक्षण सक्षम करें


> [!NOTE]
> सुपरवाइज्ड फाइनट्यूनिंग से संरेखण खोने या गंभीर भूलने की समस्या हो सकती है। हम इस समस्या की जांच करने और फाइनट्यूनिंग के बाद एक संरेखण चरण चलाने की सलाह देते हैं।

### फाइन ट्यूनिंग पैरामीटर

1. यह Python स्क्रिप्ट मशीन लर्निंग मॉडल के फाइन-ट्यूनिंग के लिए पैरामीटर सेट कर रही है। इसका सारांश इस प्रकार है:

    - यह डिफ़ॉल्ट प्रशिक्षण पैरामीटर सेट करता है जैसे प्रशिक्षण epochs की संख्या, प्रशिक्षण और मूल्यांकन के लिए बैच साइज, लर्निंग रेट, और लर्निंग रेट शेड्यूलर का प्रकार।

    - यह डिफ़ॉल्ट अनुकूलन पैरामीटर सेट करता है जैसे Layer-wise Relevance Propagation (LoRa) और DeepSpeed को लागू करना है या नहीं, और DeepSpeed स्टेज।

    - यह प्रशिक्षण और अनुकूलन पैरामीटर को एक साथ finetune_parameters नामक डिक्शनरी में मिलाता है।

    - यह जांचता है कि foundation_model के पास कोई मॉडल-विशिष्ट डिफ़ॉल्ट पैरामीटर हैं या नहीं। यदि हैं, तो यह एक चेतावनी संदेश प्रिंट करता है और finetune_parameters डिक्शनरी को इन मॉडल-विशिष्ट डिफ़ॉल्ट्स से अपडेट करता है। ast.literal_eval फ़ंक्शन का उपयोग मॉडल-विशिष्ट डिफ़ॉल्ट्स को स्ट्रिंग से Python डिक्शनरी में बदलने के लिए किया जाता है।

    - यह फाइन-ट्यूनिंग के लिए उपयोग किए जाने वाले अंतिम पैरामीटर सेट को प्रिंट करता है।

    - संक्षेप में, यह स्क्रिप्ट मशीन लर्निंग मॉडल के फाइन-ट्यूनिंग के पैरामीटर सेट कर रही है और दिखा रही है, साथ ही डिफ़ॉल्ट पैरामीटर को मॉडल-विशिष्ट पैरामीटर से ओवरराइड करने की सुविधा देती है।

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

### प्रशिक्षण पाइपलाइन

1. यह Python स्क्रिप्ट एक फ़ंक्शन परिभाषित कर रही है जो मशीन लर्निंग प्रशिक्षण पाइपलाइन के लिए डिस्प्ले नाम उत्पन्न करता है, और फिर इस फ़ंक्शन को कॉल करके डिस्प्ले नाम उत्पन्न कर प्रिंट करता है। इसका सारांश इस प्रकार है:

1. get_pipeline_display_name फ़ंक्शन परिभाषित किया गया है। यह फ़ंक्शन प्रशिक्षण पाइपलाइन से संबंधित विभिन्न पैरामीटर के आधार पर डिस्प्ले नाम बनाता है।

1. फ़ंक्शन के अंदर, यह कुल बैच साइज की गणना करता है, जो प्रति-डिवाइस बैच साइज, ग्रेडिएंट एक्यूमुलेशन स्टेप्स की संख्या, प्रति नोड GPU की संख्या, और फाइन-ट्यूनिंग के लिए उपयोग किए गए नोड्स की संख्या को गुणा करके निकाली जाती है।

1. यह अन्य पैरामीटर प्राप्त करता है जैसे लर्निंग रेट शेड्यूलर का प्रकार, DeepSpeed लागू है या नहीं, DeepSpeed स्टेज, LoRa लागू है या नहीं, मॉडल चेकपॉइंट्स की संख्या की सीमा, और अधिकतम अनुक्रम लंबाई।

1. यह एक स्ट्रिंग बनाता है जिसमें ये सभी पैरामीटर हाइफ़न से अलग किए गए होते हैं। यदि DeepSpeed या LoRa लागू है, तो स्ट्रिंग में क्रमशः "ds" के बाद DeepSpeed स्टेज या "lora" शामिल होता है। यदि नहीं, तो "nods" या "nolora" शामिल होता है।

1. फ़ंक्शन इस स्ट्रिंग को लौटाता है, जो प्रशिक्षण पाइपलाइन के लिए डिस्प्ले नाम के रूप में काम करता है।

1. फ़ंक्शन परिभाषित होने के बाद, इसे कॉल किया जाता है ताकि डिस्प्ले नाम उत्पन्न हो और फिर इसे प्रिंट किया जाता है।

1. संक्षेप में, यह स्क्रिप्ट विभिन्न पैरामीटर के आधार पर मशीन लर्निंग प्रशिक्षण पाइपलाइन के लिए डिस्प्ले नाम उत्पन्न कर रही है और उसे प्रिंट कर रही है।

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

### पाइपलाइन कॉन्फ़िगर करना

यह Python स्क्रिप्ट Azure Machine Learning SDK का उपयोग करके एक मशीन लर्निंग पाइपलाइन परिभाषित और कॉन्फ़िगर कर रही है। इसका सारांश इस प्रकार है:

1. यह Azure AI ML SDK से आवश्यक मॉड्यूल इम्पोर्ट करता है।

1. यह रजिस्ट्री से "chat_completion_pipeline" नामक पाइपलाइन कंपोनेंट प्राप्त करता है।

1. यह `@pipeline` डेकोरेटर और `create_pipeline` फ़ंक्शन का उपयोग करके एक पाइपलाइन जॉब परिभाषित करता है। पाइपलाइन का नाम `pipeline_display_name` सेट किया गया है।

1. `create_pipeline` फ़ंक्शन के अंदर, यह प्राप्त पाइपलाइन कंपोनेंट को विभिन्न पैरामीटर के साथ इनिशियलाइज़ करता है, जिनमें मॉडल पाथ, विभिन्न चरणों के लिए compute क्लस्टर, प्रशिक्षण और परीक्षण के लिए dataset स्प्लिट्स, फाइन-ट्यूनिंग के लिए GPU की संख्या, और अन्य फाइन-ट्यूनिंग पैरामीटर शामिल हैं।

1. यह फाइन-ट्यूनिंग जॉब के आउटपुट को पाइपलाइन जॉब के आउटपुट से मैप करता है ताकि फाइन-ट्यून मॉडल को आसानी से रजिस्टर किया जा सके, जो मॉडल को ऑनलाइन या बैच एंडपॉइंट पर डिप्लॉय करने के लिए आवश्यक है।

1. यह `create_pipeline` फ़ंक्शन को कॉल करके पाइपलाइन का एक इंस्टेंस बनाता है।

1. यह पाइपलाइन की `force_rerun` सेटिंग को `True` पर सेट करता है, जिसका मतलब है कि पिछले जॉब के कैश्ड परिणाम उपयोग नहीं किए जाएंगे।

1. यह पाइपलाइन की `continue_on_step_failure` सेटिंग को `False` पर सेट करता है, जिसका मतलब है कि यदि कोई भी स्टेप फेल होता है तो पाइपलाइन रुक जाएगी।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning SDK का उपयोग करके चैट कंप्लीशन टास्क के लिए एक मशीन लर्निंग पाइपलाइन परिभाषित और कॉन्फ़िगर कर रही है।

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

### जॉब सबमिट करें

1. यह Python स्क्रिप्ट Azure Machine Learning वर्कस्पेस में एक मशीन लर्निंग पाइपलाइन जॉब सबमिट कर रही है और फिर जॉब के पूरा होने का इंतजार कर रही है। इसका सारांश इस प्रकार है:

    - यह workspace_ml_client के jobs ऑब्जेक्ट की create_or_update मेथड को कॉल करता है ताकि पाइपलाइन जॉब सबमिट किया जा सके। चलाने के लिए पाइपलाइन pipeline_object द्वारा निर्दिष्ट है, और जॉब किस experiment के अंतर्गत चलेगा, वह experiment_name द्वारा निर्दिष्ट है।

    - इसके बाद यह workspace_ml_client के jobs ऑब्जेक्ट की stream मेथड को कॉल करता है ताकि पाइपलाइन जॉब के पूरा होने तक इंतजार किया जा सके। इंतजार करने वाला जॉब pipeline_job ऑब्जेक्ट के name एट्रिब्यूट द्वारा निर्दिष्ट है।

    - संक्षेप में, यह स्क्रिप्ट Azure Machine Learning वर्कस्पेस में एक मशीन लर्निंग पाइपलाइन जॉब सबमिट कर रही है और फिर जॉब के पूरा होने का इंतजार कर रही है।

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

## 6. फाइन ट्यून किए गए मॉडल को वर्कस्पेस में रजिस्टर करें

हम फाइन ट्यूनिंग जॉब के आउटपुट से मॉडल को रजिस्टर करेंगे। यह फाइन ट्यून किए गए मॉडल और फाइन ट्यूनिंग जॉब के बीच lineage को ट्रैक करेगा। फाइन ट्यूनिंग जॉब, आगे, फाउंडेशन मॉडल, डेटा और प्रशिक्षण कोड के साथ lineage को ट्रैक करता है।

### ML मॉडल रजिस्टर करना

1. यह Python स्क्रिप्ट Azure Machine Learning पाइपलाइन में प्रशिक्षित एक मशीन लर्निंग मॉडल को रजिस्टर कर रही है। इसका सारांश इस प्रकार है:

    - यह Azure AI ML SDK से आवश्यक मॉड्यूल इम्पोर्ट करता है।

    - यह जांचता है कि pipeline जॉब से trained_model आउटपुट उपलब्ध है या नहीं, workspace_ml_client के jobs ऑब्जेक्ट की get मेथड को कॉल करके और उसके outputs एट्रिब्यूट को एक्सेस करके।

    - यह pipeline जॉब के नाम और आउटपुट ("trained_model") के नाम के साथ एक पाथ बनाता है।

    - यह फाइन-ट्यून किए गए मॉडल के लिए एक नाम परिभाषित करता है, जो मूल मॉडल नाम के बाद "-ultrachat-200k" जोड़कर और किसी भी स्लैश को हाइफ़न से बदलकर बनाया जाता है।

    - यह मॉडल को रजिस्टर करने के लिए Model ऑब्जेक्ट बनाता है, जिसमें मॉडल का पाथ, मॉडल का प्रकार (MLflow मॉडल), मॉडल का नाम और संस्करण, और मॉडल का विवरण शामिल हैं।

    - यह workspace_ml_client के models ऑब्जेक्ट की create_or_update मेथड को कॉल करके मॉडल को रजिस्टर करता है।

    - यह रजिस्टर किए गए मॉडल को प्रिंट करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning पाइपलाइन में प्रशिक्षित एक मशीन लर्निंग मॉडल को रजिस्टर कर रही है।

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

## 7. फाइन ट्यून किए गए मॉडल को ऑनलाइन एंडपॉइंट पर डिप्लॉय करें

ऑनलाइन एंडपॉइंट एक स्थायी REST API प्रदान करते हैं, जिसका उपयोग उन एप्लिकेशन के साथ इंटीग्रेट करने के लिए किया जा सकता है जिन्हें मॉडल का उपयोग करना होता है।

### एंडपॉइंट प्रबंधित करें

1. यह Python स्क्रिप्ट Azure Machine Learning में एक रजिस्टर्ड मॉडल के लिए एक प्रबंधित ऑनलाइन एंडपॉइंट बना रही है। इसका सारांश इस प्रकार है:

    - यह Azure AI ML SDK से आवश्यक मॉड्यूल इम्पोर्ट करता है।

    - यह "ultrachat-completion-" स्ट्रिंग के बाद एक टाइमस्टैम्प जोड़कर ऑनलाइन एंडपॉइंट के लिए एक यूनिक नाम परिभाषित करता है।

    - यह ManagedOnlineEndpoint ऑब्जेक्ट बनाकर ऑनलाइन एंडपॉइंट बनाने की तैयारी करता है, जिसमें एंडपॉइंट का नाम, विवरण, और ऑथेंटिकेशन मोड ("key") शामिल हैं।

    - यह workspace_ml_client की begin_create_or_update मेथड को कॉल करके ऑनलाइन एंडपॉइंट बनाता है और फिर wait मेथड को कॉल करके निर्माण प्रक्रिया के पूरा होने का इंतजार करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning में एक रजिस्टर्ड मॉडल के लिए एक प्रबंधित ऑनलाइन एंडपॉइंट बना रही है।

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
> आप यहाँ पर डिप्लॉयमेंट के लिए समर्थित SKU की सूची पा सकते हैं - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML मॉडल डिप्लॉय करना

1. यह Python स्क्रिप्ट Azure Machine Learning में एक रजिस्टर्ड मशीन लर्निंग मॉडल को प्रबंधित ऑनलाइन एंडपॉइंट पर डिप्लॉय कर रही है। इसका सारांश इस प्रकार है:

    - यह ast मॉड्यूल इम्पोर्ट करता है, जो Python के abstract syntax grammar के ट्री को प्रोसेस करने के लिए फ़ंक्शन प्रदान करता है।

    - यह डिप्लॉयमेंट के लिए instance type को "Standard_NC6s_v3" सेट करता है।

    - यह जांचता है कि foundation_model में inference_compute_allow_list टैग मौजूद है या नहीं। यदि है, तो यह टैग के मान को स्ट्रिंग से Python लिस्ट में बदलकर inference_computes_allow_list में असाइन करता है। यदि नहीं, तो इसे None सेट करता है।

    - यह जांचता है कि निर्दिष्ट instance type allow list में है या नहीं। यदि नहीं, तो यह उपयोगकर्ता को allow list से कोई instance type चुनने के लिए कहता है।

    - यह ManagedOnlineDeployment ऑब्जेक्ट बनाकर डिप्लॉयमेंट बनाने की तैयारी करता है, जिसमें डिप्लॉयमेंट का नाम, एंडपॉइंट का नाम, मॉडल का ID, instance type और count, लिवनेस प्रॉब सेटिंग्स, और रिक्वेस्ट सेटिंग्स शामिल हैं।

    - यह workspace_ml_client की begin_create_or_update मेथड को कॉल करके डिप्लॉयमेंट बनाता है और फिर wait मेथड को कॉल करके निर्माण प्रक्रिया के पूरा होने का इंतजार करता है।

    - यह एंडपॉइंट के ट्रैफिक को 100% "demo" डिप्लॉयमेंट की ओर डायरेक्ट करता है।

    - यह workspace_ml_client की begin_create_or_update मेथड को कॉल करके एंडपॉइंट को अपडेट करता है और फिर result मेथड को कॉल करके अपडेट के पूरा होने का इंतजार करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning में एक रजिस्टर्ड मशीन लर्निंग मॉडल को प्रबंधित ऑनलाइन एंडपॉइंट पर डिप्लॉय कर रही है।

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

## 8. नमूना डेटा के साथ एंडपॉइंट का परीक्षण करें

हम टेस्ट डेटासेट से कुछ नमूना डेटा लेंगे और इनफेरेंस के लिए ऑनलाइन एंडपॉइंट को सबमिट करेंगे। फिर हम स्कोर किए गए लेबल को ग्राउंड ट्रूथ लेबल के साथ दिखाएंगे।

### परिणाम पढ़ना

1. यह Python स्क्रिप्ट एक JSON Lines फ़ाइल को pandas DataFrame में पढ़ रही है, एक रैंडम सैंपल ले रही है, और इंडेक्स रीसेट कर रही है। इसका सारांश इस प्रकार है:

    - यह ./ultrachat_200k_dataset/test_gen.jsonl फ़ाइल को pandas DataFrame में पढ़ती है। read_json फ़ंक्शन को lines=True आर्गुमेंट के साथ उपयोग किया गया है क्योंकि फ़ाइल JSON Lines फॉर्मेट में है, जहाँ प्रत्येक लाइन एक अलग JSON ऑब्जेक्ट होती है।

    - यह DataFrame से 1 पंक्ति का रैंडम सैंपल लेती है। sample फ़ंक्शन को n=1 आर्गुमेंट के साथ उपयोग किया गया है ताकि एक रैंडम पंक्ति चुनी जा सके।

    - यह DataFrame का इंडेक्स रीसेट करती है। reset_index फ़ंक्शन को drop=True आर्गुमेंट के साथ उपयोग किया गया है ताकि मूल इंडेक्स हटाकर डिफ़ॉल्ट पूर्णांक इंडेक्स लगाया जा सके।

    - यह DataFrame की पहली 2 पंक्तियाँ head फ़ंक्शन के साथ 2 आर्गुमेंट देकर दिखाती है। हालांकि, चूंकि सैंपलिंग के बाद DataFrame में केवल एक पंक्ति है, इसलिए केवल वह एक पंक्ति दिखाई जाएगी।

1. संक्षेप में, यह स्क्रिप्ट JSON Lines फ़ाइल को pandas DataFrame में पढ़ रही है, 1 पंक्ति का रैंडम सैंपल ले रही है, इंडेक्स रीसेट कर रही है, और पहली पंक्ति दिखा रही है।

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

1. यह Python स्क्रिप्ट विशिष्ट पैरामीटर के साथ एक JSON ऑब्जेक्ट बना रही है और उसे एक फ़ाइल में सेव कर रही है। इसका सारांश इस प्रकार है:

    - यह json मॉड्यूल इम्पोर्ट करता है, जो JSON डेटा के साथ काम करने के लिए फ़ंक्शन प्रदान करता है।

    - यह parameters नामक एक डिक्शनरी बनाता है जिसमें मशीन लर्निंग मॉडल के पैरामीटर होते हैं। कुंजी हैं "temperature", "top_p", "do_sample", और "max_new_tokens", जिनके मान क्रमशः 0.6, 0.9, True, और 200 हैं।

    - यह एक और डिक्शनरी test_json बनाता है जिसमें दो कुंजी हैं: "input_data" और "params"। "input_data" का मान एक और डिक्शनरी है जिसमें "input_string" और "parameters" कुंजी हैं। "input_string" का मान test_df DataFrame के पहले संदेश की एक सूची है। "parameters" का मान पहले बनाए गए parameters डिक्शनरी है। "params" का मान एक खाली डिक्शनरी है।
- यह sample_score.json नाम की एक फ़ाइल खोलता है

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

### एंडपॉइंट को कॉल करना

1. यह Python स्क्रिप्ट Azure Machine Learning में एक ऑनलाइन एंडपॉइंट को कॉल कर रही है ताकि JSON फ़ाइल को स्कोर किया जा सके। इसका विवरण इस प्रकार है:

    - यह workspace_ml_client ऑब्जेक्ट की online_endpoints प्रॉपर्टी के invoke मेथड को कॉल करता है। इस मेथड का उपयोग ऑनलाइन एंडपॉइंट को अनुरोध भेजने और प्रतिक्रिया प्राप्त करने के लिए किया जाता है।

    - यह endpoint_name और deployment_name आर्गुमेंट्स के साथ एंडपॉइंट और डिप्लॉयमेंट का नाम निर्दिष्ट करता है। इस मामले में, एंडपॉइंट का नाम online_endpoint_name वेरिएबल में स्टोर है और डिप्लॉयमेंट का नाम "demo" है।

    - यह request_file आर्गुमेंट के साथ स्कोर की जाने वाली JSON फ़ाइल का पथ निर्दिष्ट करता है। इस मामले में, फ़ाइल का पथ ./ultrachat_200k_dataset/sample_score.json है।

    - यह एंडपॉइंट से प्राप्त प्रतिक्रिया को response वेरिएबल में स्टोर करता है।

    - यह कच्ची प्रतिक्रिया को प्रिंट करता है।

1. संक्षेप में, यह स्क्रिप्ट Azure Machine Learning में एक ऑनलाइन एंडपॉइंट को कॉल कर JSON फ़ाइल को स्कोर करती है और प्रतिक्रिया को प्रिंट करती है।

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

## 9. ऑनलाइन एंडपॉइंट को हटाएं

1. ऑनलाइन एंडपॉइंट को हटाना न भूलें, अन्यथा आप उस कंप्यूट के लिए बिलिंग मीटर चालू छोड़ देंगे जो एंडपॉइंट द्वारा उपयोग किया जा रहा है। यह Python कोड Azure Machine Learning में एक ऑनलाइन एंडपॉइंट को हटा रहा है। इसका विवरण इस प्रकार है:

    - यह workspace_ml_client ऑब्जेक्ट की online_endpoints प्रॉपर्टी के begin_delete मेथड को कॉल करता है। इस मेथड का उपयोग ऑनलाइन एंडपॉइंट को हटाने की प्रक्रिया शुरू करने के लिए किया जाता है।

    - यह name आर्गुमेंट के साथ हटाए जाने वाले एंडपॉइंट का नाम निर्दिष्ट करता है। इस मामले में, एंडपॉइंट का नाम online_endpoint_name वेरिएबल में स्टोर है।

    - यह wait मेथड को कॉल करता है ताकि हटाने की प्रक्रिया पूरी होने तक इंतजार किया जा सके। यह एक ब्लॉकिंग ऑपरेशन है, जिसका मतलब है कि स्क्रिप्ट तब तक आगे नहीं बढ़ेगी जब तक हटाना पूरा नहीं हो जाता।

    - संक्षेप में, यह कोड Azure Machine Learning में एक ऑनलाइन एंडपॉइंट को हटाने की प्रक्रिया शुरू करता है और ऑपरेशन के पूरा होने तक इंतजार करता है।

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।