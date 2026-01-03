<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:12:20+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "mr"
}
-->
## Azure ML सिस्टम रजिस्ट्रीमधील chat-completion घटकांचा वापर करून मॉडेल फाइन ट्यून कसे करावे

या उदाहरणात आपण ultrachat_200k डेटासेट वापरून Phi-3-mini-4k-instruct मॉडेलचे दोन लोकांमधील संभाषण पूर्ण करण्यासाठी फाइन ट्यूनिंग करू.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35.mr.png)

हे उदाहरण तुम्हाला Azure ML SDK आणि Python वापरून फाइन ट्यूनिंग कसे करायचे आणि नंतर फाइन ट्यून केलेले मॉडेल रिअल टाइम इन्फरन्ससाठी ऑनलाइन एंडपॉइंटवर कसे डिप्लॉय करायचे हे दाखवेल.

### प्रशिक्षण डेटा

आपण ultrachat_200k डेटासेट वापरणार आहोत. हा UltraChat डेटासेटचा खूपच फिल्टर केलेला आवृत्ती आहे आणि Zephyr-7B-β, एक अत्याधुनिक 7b चॅट मॉडेल, प्रशिक्षणासाठी वापरला गेला होता.

### मॉडेल

आपण Phi-3-mini-4k-instruct मॉडेल वापरून दाखवणार आहोत की वापरकर्ता कसा chat-completion टास्कसाठी मॉडेल फाइन ट्यून करू शकतो. जर तुम्ही हा नोटबुक एखाद्या विशिष्ट मॉडेल कार्डमधून उघडला असेल, तर त्या विशिष्ट मॉडेलचे नाव बदला.

### टास्क

- फाइन ट्यून करण्यासाठी मॉडेल निवडा.
- प्रशिक्षण डेटा निवडा आणि तपासा.
- फाइन ट्यूनिंग जॉब कॉन्फिगर करा.
- फाइन ट्यूनिंग जॉब चालवा.
- प्रशिक्षण आणि मूल्यांकन मेट्रिक्स पुनरावलोकन करा.
- फाइन ट्यून केलेले मॉडेल नोंदणी करा.
- रिअल टाइम इन्फरन्ससाठी फाइन ट्यून केलेले मॉडेल डिप्लॉय करा.
- संसाधने साफ करा.

## 1. पूर्वतयारी करा

- आवश्यक अवलंबित्वे इन्स्टॉल करा
- AzureML Workspace शी कनेक्ट व्हा. अधिक माहितीसाठी set up SDK authentication पहा. खाली <WORKSPACE_NAME>, <RESOURCE_GROUP> आणि <SUBSCRIPTION_ID> बदला.
- azureml system registry शी कनेक्ट व्हा
- ऐच्छिक experiment नाव सेट करा
- compute तपासा किंवा तयार करा.

> [!NOTE]
> आवश्यक आहे की एक GPU नोडमध्ये अनेक GPU कार्ड्स असू शकतात. उदाहरणार्थ, Standard_NC24rs_v3 च्या एका नोडमध्ये 4 NVIDIA V100 GPUs असतात तर Standard_NC12s_v3 मध्ये 2 NVIDIA V100 GPUs असतात. याबाबत अधिक माहितीसाठी docs पहा. प्रत्येक नोडसाठी GPU कार्ड्सची संख्या param gpus_per_node मध्ये सेट केली जाते. योग्यरित्या सेट केल्यास नोडमधील सर्व GPUs चा वापर होईल. शिफारस केलेले GPU compute SKUs येथे आणि येथे पाहू शकता.

### Python लायब्ररी

खालील सेल चालवून अवलंबित्वे इन्स्टॉल करा. नवीन वातावरणात चालवताना हा पर्यायी टप्पा नाही.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML शी संवाद साधणे

1. हा Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा सोबत संवाद साधण्यासाठी वापरला जातो. त्याचे काय कार्य आहे ते खालीलप्रमाणे:

    - azure.ai.ml, azure.identity, आणि azure.ai.ml.entities पॅकेजमधील आवश्यक मॉड्यूल्स इम्पोर्ट करतो. तसेच time मॉड्यूल इम्पोर्ट करतो.

    - DefaultAzureCredential() वापरून प्रमाणीकरण करण्याचा प्रयत्न करतो, जे Azure क्लाउडमध्ये जलद अॅप्लिकेशन्स विकसित करण्यासाठी सुलभ प्रमाणीकरण अनुभव देते. जर हे अयशस्वी झाले तर InteractiveBrowserCredential() वापरतो, जे इंटरॅक्टिव लॉगिन प्रॉम्प्ट देते.

    - नंतर from_config पद्धत वापरून MLClient चे उदाहरण तयार करण्याचा प्रयत्न करतो, जे डिफॉल्ट config फाइल (config.json) मधून कॉन्फिगरेशन वाचते. जर हे अयशस्वी झाले तर subscription_id, resource_group_name, आणि workspace_name मॅन्युअली देऊन MLClient चे उदाहरण तयार करतो.

    - दुसरे MLClient चे उदाहरण तयार करतो, जे Azure ML रजिस्ट्रीसाठी आहे ज्याचे नाव "azureml" आहे. या रजिस्ट्रीमध्ये मॉडेल्स, फाइन-ट्यूनिंग पाइपलाइन्स, आणि एन्व्हायर्नमेंट्स संग्रहित केले जातात.

    - experiment_name "chat_completion_Phi-3-mini-4k-instruct" सेट करतो.

    - सध्याचा वेळ (सेकंदांमध्ये, फ्लोटिंग पॉइंट नंबर म्हणून) पूर्णांकात आणि नंतर स्ट्रिंगमध्ये रूपांतरित करून एक अद्वितीय timestamp तयार करतो. हा timestamp युनिक नावे आणि आवृत्त्या तयार करण्यासाठी वापरला जाऊ शकतो.

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

## 2. फाइन ट्यूनसाठी फाउंडेशन मॉडेल निवडा

1. Phi-3-mini-4k-instruct हा 3.8B पॅरामीटर्सचा, हलका, अत्याधुनिक ओपन मॉडेल आहे जो Phi-2 साठी वापरल्या गेलेल्या डेटासेटवर आधारित आहे. हा मॉडेल Phi-3 मॉडेल कुटुंबाचा भाग आहे, आणि Mini आवृत्ती दोन प्रकारांमध्ये येते: 4K आणि 128K, जे संदर्भ लांबी (टोकन्समध्ये) दर्शवते. आपल्याला हा मॉडेल आपल्या विशिष्ट उद्देशासाठी फाइन ट्यून करावा लागेल. तुम्ही AzureML Studio मधील Model Catalog मध्ये chat-completion टास्कनुसार हे मॉडेल्स ब्राउझ करू शकता. या उदाहरणात आपण Phi-3-mini-4k-instruct मॉडेल वापरत आहोत. जर तुम्ही हा नोटबुक वेगळ्या मॉडेलसाठी उघडला असेल, तर मॉडेलचे नाव आणि आवृत्ती तदनुसार बदला.

    > [!NOTE]
    > मॉडेल आयडी ही मॉडेलची एक मालमत्ता आहे. ही फाइन ट्यूनिंग जॉबसाठी इनपुट म्हणून दिली जाते. AzureML Studio Model Catalog मधील मॉडेल तपशील पृष्ठावर Asset ID फील्डमध्ये देखील उपलब्ध आहे.

2. हा Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा सोबत संवाद साधतो. त्याचे काय कार्य आहे ते खालीलप्रमाणे:

    - model_name "Phi-3-mini-4k-instruct" असे सेट करतो.

    - registry_ml_client ऑब्जेक्टच्या models प्रॉपर्टीचा get मेथड वापरून Azure ML रजिस्ट्रीमधून दिलेल्या नावाचा मॉडेलचा नवीनतम आवृत्ती मिळवतो. get मेथडला दोन आर्ग्युमेंट्स दिले जातात: मॉडेलचे नाव आणि लेबल ज्याद्वारे नवीनतम आवृत्ती मिळवायची आहे.

    - कन्सोलवर एक संदेश प्रिंट करतो ज्यात फाइन ट्यूनिंगसाठी वापरल्या जाणाऱ्या मॉडेलचे नाव, आवृत्ती, आणि आयडी दाखवलेले असते. स्ट्रिंगच्या format मेथडचा वापर करून हे मूल्ये संदेशात टाकले जातात. मॉडेलचे नाव, आवृत्ती, आणि आयडी foundation_model ऑब्जेक्टच्या प्रॉपर्टीज म्हणून मिळतात.

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

## 3. जॉबसाठी वापरण्यासाठी compute तयार करा

फाइनट्यून जॉब फक्त GPU compute सोबतच चालतो. compute ची आकार मॉडेलच्या आकारावर अवलंबून असते आणि बहुतेक वेळा योग्य compute निवडणे कठीण होते. या सेलमध्ये वापरकर्त्याला योग्य compute निवडण्याचे मार्गदर्शन केले आहे.

> [!NOTE]
> खालील compute सर्वात ऑप्टिमाइझ्ड कॉन्फिगरेशनसह काम करतात. कॉन्फिगरेशनमध्ये कोणतीही बदल Cuda Out Of Memory त्रुटी निर्माण करू शकतात. अशा परिस्थितीत compute मोठ्या आकारात अपग्रेड करण्याचा प्रयत्न करा.

> [!NOTE]
> compute_cluster_size निवडताना खात्री करा की compute तुमच्या resource group मध्ये उपलब्ध आहे. जर एखादा compute उपलब्ध नसेल तर compute संसाधनांसाठी प्रवेश मागणी करू शकता.

### फाइन ट्यूनिंगसाठी मॉडेलची सपोर्ट तपासणी

1. हा Python स्क्रिप्ट Azure Machine Learning (Azure ML) मॉडेलशी संवाद साधतो. त्याचे काय कार्य आहे ते खालीलप्रमाणे:

    - ast मॉड्यूल इम्पोर्ट करतो, जे Python च्या abstract syntax grammar चे ट्री प्रोसेस करण्यासाठी फंक्शन्स देते.

    - foundation_model ऑब्जेक्टमध्ये finetune_compute_allow_list नावाचा टॅग आहे का ते तपासतो. Azure ML मध्ये टॅग्स म्हणजे key-value जोड्या असतात ज्या मॉडेल्स फिल्टर आणि सॉर्ट करण्यासाठी वापरल्या जातात.

    - जर finetune_compute_allow_list टॅग असेल, तर ast.literal_eval फंक्शन वापरून त्या टॅगच्या मूल्याला (जो स्ट्रिंग आहे) सुरक्षितपणे Python लिस्टमध्ये रूपांतरित करतो. ही लिस्ट computes_allow_list व्हेरिएबलला दिली जाते. नंतर एक संदेश प्रिंट करतो की या लिस्टमधून compute तयार करावा.

    - जर finetune_compute_allow_list टॅग नसेल, तर computes_allow_list None सेट करतो आणि एक संदेश प्रिंट करतो की finetune_compute_allow_list टॅग मॉडेलच्या टॅग्समध्ये नाही.

    - सारांश, हा स्क्रिप्ट मॉडेलच्या मेटाडेटामध्ये विशिष्ट टॅग तपासतो, त्याचा मूल्य लिस्टमध्ये रूपांतरित करतो (जर असेल तर), आणि वापरकर्त्याला त्यानुसार माहिती देतो.

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

### Compute Instance तपासणी

1. हा Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा सोबत संवाद साधतो आणि compute instance वर अनेक तपासण्या करतो. त्याचे काय कार्य आहे ते खालीलप्रमाणे:

    - compute_cluster नावाने Azure ML workspace मधून compute instance मिळवण्याचा प्रयत्न करतो. जर compute instance ची provisioning state "failed" असेल तर ValueError उचलतो.

    - computes_allow_list None नसल्यास, लिस्टमधील सर्व compute आकार lowercase मध्ये रूपांतरित करतो आणि सध्याच्या compute instance चा आकार त्या लिस्टमध्ये आहे का ते तपासतो. नसल्यास ValueError उचलतो.

    - जर computes_allow_list None असेल, तर compute instance चा आकार unsupported GPU VM sizes च्या यादीत आहे का ते तपासतो. असल्यास ValueError उचलतो.

    - workspace मधील सर्व उपलब्ध compute आकारांची यादी मिळवतो. त्यानंतर प्रत्येक compute आकारासाठी तपासतो की त्याचे नाव सध्याच्या compute instance च्या आकाराशी जुळते का. जर जुळले तर त्या compute आकारासाठी GPU ची संख्या मिळवतो आणि gpu_count_found True सेट करतो.

    - gpu_count_found True असल्यास compute instance मधील GPU ची संख्या प्रिंट करतो. नसल्यास ValueError उचलतो.

    - सारांश, हा स्क्रिप्ट Azure ML workspace मधील compute instance ची provisioning state, आकार, आणि GPU संख्या तपासतो आणि आवश्यक असल्यास त्रुटी दाखवतो.

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

## 4. मॉडेल फाइन ट्यूनिंगसाठी डेटासेट निवडा

1. आपण ultrachat_200k डेटासेट वापरतो. या डेटासेटमध्ये चार स्प्लिट्स आहेत, जे Supervised fine-tuning (sft) साठी योग्य आहेत. Generation ranking (gen). प्रत्येक स्प्लिटमधील उदाहरणांची संख्या खालीलप्रमाणे आहे:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. पुढील काही सेल्समध्ये फाइन ट्यूनिंगसाठी मूलभूत डेटा तयारी दाखवली आहे:

### काही डेटा रांगा पाहा

आपण हा नमुना लवकर चालवू इच्छितो, म्हणून train_sft, test_sft फाइल्स ज्या आधीच ट्रिम केलेल्या रांगा पैकी 5% समाविष्ट करतात, त्या सेव्ह करा. याचा अर्थ फाइन ट्यून केलेल्या मॉडेलची अचूकता कमी असेल, त्यामुळे ते प्रत्यक्ष वापरासाठी योग्य नाही.
download-dataset.py स्क्रिप्ट ultrachat_200k डेटासेट डाउनलोड करण्यासाठी आणि डेटासेटला फाइनट्यून पाइपलाइन घटकासाठी योग्य स्वरूपात रूपांतरित करण्यासाठी वापरली जाते. तसेच डेटासेट मोठा असल्यामुळे येथे फक्त त्याचा एक भाग आहे.

1. खालील स्क्रिप्ट फक्त 5% डेटा डाउनलोड करते. dataset_split_pc पॅरामीटर बदलून हा टक्का वाढवता येतो.

    > [!NOTE]
    > काही भाषा मॉडेल्समध्ये वेगवेगळे भाषा कोड असतात, त्यामुळे डेटासेटमधील कॉलम नावे त्यानुसार असावीत.

1. डेटा कसा दिसायला हवा याचे उदाहरण खालीलप्रमाणे आहे
chat-completion डेटासेट parquet फॉरमॅटमध्ये संग्रहित आहे, ज्यामध्ये प्रत्येक नोंद खालील स्कीमाचा वापर करते:

    - हा JSON (JavaScript Object Notation) दस्तऐवज आहे, जो लोकप्रिय डेटा विनिमय फॉरमॅट आहे. हा executable कोड नाही, तर डेटा संग्रहित आणि ट्रान्सपोर्ट करण्याचा मार्ग आहे. त्याची रचना खालीलप्रमाणे आहे:

    - "prompt": हा की एक स्ट्रिंग मूल्य धारण करतो, जो AI सहाय्यकाला दिलेला टास्क किंवा प्रश्न दर्शवतो.

    - "messages": हा की ऑब्जेक्ट्सची एक अ‍ॅरे धारण करतो. प्रत्येक ऑब्जेक्ट वापरकर्ता आणि AI सहाय्यक यांच्यातील संभाषणातील एक संदेश दर्शवतो. प्रत्येक संदेश ऑब्जेक्टमध्ये दोन कीज असतात:

    - "content": हा की संदेशाचा मजकूर असलेला स्ट्रिंग मूल्य धारण करतो.
    - "role": हा की संदेश पाठवणाऱ्या घटकाची भूमिका दर्शवणारा स्ट्रिंग मूल्य धारण करतो. तो "user" किंवा "assistant" असू शकतो.
    - "prompt_id": हा की प्रॉम्प्टसाठी एक अद्वितीय ओळख दर्शवणारा स्ट्रिंग मूल्य धारण करतो.

1. या विशिष्ट JSON दस्तऐवजात, एक संभाषण दाखवले आहे जिथे वापरकर्ता AI सहाय्यकाला dystopian कथा साठी नायक तयार करण्यास सांगतो. सहाय्यक प्रतिसाद देतो, आणि नंतर वापरकर्ता अधिक तपशील मागतो. सहाय्यक अधिक तपशील देण्यास सहमत होतो. संपूर्ण संभाषण विशिष्ट prompt_id शी संबंधित आहे.

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

### डेटा डाउनलोड करा

1. हा Python स्क्रिप्ट download-dataset.py नावाच्या सहाय्यक स्क्रिप्टचा वापर करून डेटासेट डाउनलोड करण्यासाठी वापरला जातो. त्याचे काय कार्य आहे ते खालीलप्रमाणे:

    - os मॉड्यूल इम्पोर्ट करतो, जे ऑपरेटिंग सिस्टमवर अवलंबून कार्य करण्याचा पोर्टेबल मार्ग देते.

    - os.system फंक्शन वापरून download-dataset.py स्क्रिप्ट शेलमध्ये विशिष्ट कमांड-लाइन आर्ग्युमेंट्ससह चालवतो. आर्ग्युमेंट्समध्ये डाउनलोड करायचा डेटासेट (HuggingFaceH4/ultrachat_200k), डाउनलोड करण्यासाठी डायरेक्टरी (ultrachat_200k_dataset), आणि डेटासेटचा किती टक्का स्प्लिट करायचा (5) यांचा समावेश आहे. os.system फंक्शनने चालवलेल्या कमांडचा exit status परत करतो; हा exit_status व्हेरिएबलमध्ये साठवला जातो.

    - exit_status 0 नसल्यास, म्हणजे कमांड अयशस्वी झाल्यास, Exception उचलतो ज्यात डेटासेट डाउनलोड करताना त्रुटी असल्याचा संदेश असतो.

    - सारांश, हा स्क्रिप्ट सहाय्यक स्क्रिप्ट वापरून डेटासेट डाउनलोड करण्याचा आदेश देतो आणि कमांड अयशस्वी झाल्यास त्रुटी दाखवतो.

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

### डेटा DataFrame मध्ये लोड करणे

1. हा Python स्क्रिप्ट JSON Lines फाइल pandas DataFrame मध्ये लोड करतो आणि पहिल्या 5 रांगा दाखवतो. त्याचे काय कार्य आहे ते खालीलप्रमाणे:

    - pandas लायब्ररी इम्पोर्ट करतो, जी डेटा मॅनिप्युलेशन आणि विश्लेषणासाठी शक्तिशाली लायब्ररी आहे.

    - pandas च्या display पर्यायांमध्ये कमाल कॉलम रुंदी 0 सेट करतो. याचा अर्थ DataFrame प्रिंट करताना प्रत्येक कॉलमचा पूर्ण मजकूर कट न होता दाखवला जाईल.

    - pd.read_json फंक्शन वापरून ultrachat_200k_dataset डायरेक्टरीमधील train_sft.jsonl फाइल DataFrame मध्ये लोड करतो. lines=True हे दर्शवते की फाइल JSON Lines फॉरमॅटमध्ये आहे, जिथे प्रत्येक ओळ स्वतंत्र JSON ऑब्जेक्ट आहे.
- हे DataFrame च्या पहिल्या 5 रकान्या दाखवण्यासाठी head मेथड वापरते. जर DataFrame मध्ये 5 पेक्षा कमी रकाने असतील, तर ते सर्व दाखवेल.

- सारांश म्हणून, हा स्क्रिप्ट JSON Lines फाइल DataFrame मध्ये लोड करत आहे आणि पहिल्या 5 रकान्यांसह पूर्ण कॉलम मजकूर दाखवत आहे.

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

## 5. मॉडेल आणि डेटा इनपुट म्हणून वापरून फाइन ट्यूनिंग जॉब सबमिट करा

chat-completion पाइपलाइन कॉम्पोनंट वापरणारा जॉब तयार करा. फाइन ट्यूनिंगसाठी समर्थित सर्व पॅरामीटर्सबद्दल अधिक जाणून घ्या.

### फाइनट्यून पॅरामीटर्स परिभाषित करा

1. फाइनट्यून पॅरामीटर्स दोन वर्गांमध्ये विभागले जाऊ शकतात - प्रशिक्षण पॅरामीटर्स, ऑप्टिमायझेशन पॅरामीटर्स

1. प्रशिक्षण पॅरामीटर्स प्रशिक्षणाच्या बाबी परिभाषित करतात जसे की -

    - वापरायचा ऑप्टिमायझर, शेड्युलर
    - फाइनट्यूनसाठी ऑप्टिमायझेशनसाठी मेट्रिक
    - प्रशिक्षण स्टेप्सची संख्या, बॅच साईज इत्यादी
    - ऑप्टिमायझेशन पॅरामीटर्स GPU मेमरी ऑप्टिमायझेशन आणि संगणकीय संसाधनांचा प्रभावी वापर करण्यास मदत करतात.

1. खाली काही पॅरामीटर्स आहेत जे या वर्गात येतात. ऑप्टिमायझेशन पॅरामीटर्स प्रत्येक मॉडेलसाठी वेगळे असतात आणि मॉडेलसह पॅकेज केलेले असतात जेणेकरून या फरकांना हाताळता येईल.

    - deepspeed आणि LoRA सक्षम करा
    - मिक्स्ड प्रिसिजन प्रशिक्षण सक्षम करा
    - मल्टी-नोड प्रशिक्षण सक्षम करा


> [!NOTE]
> सुपरवाइज्ड फाइनट्यूनिंगमुळे संरेखन गमावले जाऊ शकते किंवा गंभीर विसर पडू शकतो. आम्ही या समस्येची तपासणी करण्याची आणि फाइनट्यूनिंगनंतर संरेखन टप्पा चालवण्याची शिफारस करतो.

### फाइन ट्यूनिंग पॅरामीटर्स

1. हा Python स्क्रिप्ट मशीन लर्निंग मॉडेलसाठी फाइन-ट्यूनिंग पॅरामीटर्स सेट करत आहे. त्याचे तपशील पुढीलप्रमाणे:

    - तो डिफॉल्ट प्रशिक्षण पॅरामीटर्स सेट करतो जसे की प्रशिक्षण एपॉक्सची संख्या, प्रशिक्षण आणि मूल्यांकनासाठी बॅच साईज, लर्निंग रेट, आणि लर्निंग रेट शेड्युलर प्रकार.

    - तो डिफॉल्ट ऑप्टिमायझेशन पॅरामीटर्स सेट करतो जसे की Layer-wise Relevance Propagation (LoRa) आणि DeepSpeed लागू करायचे की नाही, आणि DeepSpeed स्टेज.

    - तो प्रशिक्षण आणि ऑप्टिमायझेशन पॅरामीटर्स एकत्र करून finetune_parameters नावाचा एक डिक्शनरी तयार करतो.

    - तो तपासतो की foundation_model कडे कोणतेही मॉडेल-विशिष्ट डिफॉल्ट पॅरामीटर्स आहेत का. असल्यास, तो एक चेतावणी संदेश छापतो आणि finetune_parameters डिक्शनरीमध्ये हे मॉडेल-विशिष्ट डिफॉल्ट्स अपडेट करतो. ast.literal_eval फंक्शन वापरून मॉडेल-विशिष्ट डिफॉल्ट्स स्ट्रिंगमधून Python डिक्शनरीमध्ये रूपांतरित केले जातात.

    - तो फाइन-ट्यूनिंगसाठी वापरल्या जाणाऱ्या अंतिम पॅरामीटर्स छापतो.

    - सारांश म्हणून, हा स्क्रिप्ट मशीन लर्निंग मॉडेलसाठी फाइन-ट्यूनिंग पॅरामीटर्स सेट करतो आणि दर्शवतो, ज्यात डिफॉल्ट पॅरामीटर्स मॉडेल-विशिष्ट पॅरामीटर्सने ओव्हरराईड करता येतात.

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

1. हा Python स्क्रिप्ट मशीन लर्निंग प्रशिक्षण पाइपलाइनसाठी डिस्प्ले नाव तयार करण्यासाठी फंक्शन परिभाषित करतो आणि नंतर ते कॉल करून डिस्प्ले नाव तयार करतो आणि छापतो. त्याचे तपशील पुढीलप्रमाणे:

1. get_pipeline_display_name फंक्शन परिभाषित केले आहे. हे फंक्शन प्रशिक्षण पाइपलाइनशी संबंधित विविध पॅरामीटर्सवर आधारित डिस्प्ले नाव तयार करते.

1. फंक्शनमध्ये, तो एकूण बॅच साईज कॅल्क्युलेट करतो ज्यासाठी प्रति-डिव्हाइस बॅच साईज, ग्रेडियंट अ‍ॅक्युम्युलेशन स्टेप्सची संख्या, प्रति नोड GPU ची संख्या, आणि फाइन-ट्यूनिंगसाठी वापरल्या जाणाऱ्या नोड्सची संख्या यांचा गुणाकार करतो.

1. तो इतर पॅरामीटर्स मिळवतो जसे की लर्निंग रेट शेड्युलर प्रकार, DeepSpeed लागू आहे का, DeepSpeed स्टेज, Layer-wise Relevance Propagation (LoRa) लागू आहे का, मॉडेल चेकपॉइंट्सची मर्यादा, आणि कमाल सिक्वेन्स लांबी.

1. तो एक स्ट्रिंग तयार करतो ज्यात हे सर्व पॅरामीटर्स हायफनने वेगळे केलेले असतात. जर DeepSpeed किंवा LoRa लागू असेल, तर स्ट्रिंगमध्ये "ds" आणि DeepSpeed स्टेज किंवा "lora" समाविष्ट असते. नसल्यास "nods" किंवा "nolora" समाविष्ट असते.

1. फंक्शन हा स्ट्रिंग परत करतो, जो प्रशिक्षण पाइपलाइनसाठी डिस्प्ले नाव म्हणून वापरला जातो.

1. फंक्शन परिभाषित केल्यानंतर, ते कॉल करून डिस्प्ले नाव तयार केले जाते आणि ते छापले जाते.

1. सारांश म्हणून, हा स्क्रिप्ट विविध पॅरामीटर्सवर आधारित मशीन लर्निंग प्रशिक्षण पाइपलाइनसाठी डिस्प्ले नाव तयार करतो आणि ते छापतो.

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

### पाइपलाइन कॉन्फिगर करणे

हा Python स्क्रिप्ट Azure Machine Learning SDK वापरून मशीन लर्निंग पाइपलाइन परिभाषित आणि कॉन्फिगर करतो. त्याचे तपशील पुढीलप्रमाणे:

1. तो Azure AI ML SDK मधील आवश्यक मॉड्यूल्स इम्पोर्ट करतो.

1. तो रजिस्ट्रीमधून "chat_completion_pipeline" नावाचा पाइपलाइन कॉम्पोनंट प्राप्त करतो.

1. `@pipeline` डेकोरेटर आणि `create_pipeline` फंक्शन वापरून पाइपलाइन जॉब परिभाषित करतो. पाइपलाइनचे नाव `pipeline_display_name` असे सेट केले आहे.

1. `create_pipeline` फंक्शनमध्ये, तो प्राप्त केलेल्या पाइपलाइन कॉम्पोनंटला विविध पॅरामीटर्ससह इनिशियलाइझ करतो, ज्यात मॉडेल पथ, विविध टप्प्यांसाठी कम्प्युट क्लस्टर्स, प्रशिक्षण आणि चाचणीसाठी डेटासेट स्प्लिट्स, फाइन-ट्यूनिंगसाठी GPU ची संख्या, आणि इतर फाइन-ट्यूनिंग पॅरामीटर्स यांचा समावेश आहे.

1. तो फाइन-ट्यूनिंग जॉबचा आउटपुट पाइपलाइन जॉबच्या आउटपुटशी मॅप करतो. यामुळे फाइन-ट्यून केलेले मॉडेल सहज नोंदणी करता येते, जे ऑनलाइन किंवा बॅच एंडपॉइंटवर मॉडेल डिप्लॉय करण्यासाठी आवश्यक आहे.

1. तो `create_pipeline` फंक्शन कॉल करून पाइपलाइनची एक उदाहरण तयार करतो.

1. तो पाइपलाइनचा `force_rerun` सेटिंग `True` करतो, म्हणजे मागील जॉब्सचे कॅश केलेले निकाल वापरले जाणार नाहीत.

1. तो पाइपलाइनचा `continue_on_step_failure` सेटिंग `False` करतो, म्हणजे कोणताही टप्पा अयशस्वी झाल्यास पाइपलाइन थांबेल.

1. सारांश म्हणून, हा स्क्रिप्ट Azure Machine Learning SDK वापरून चॅट कंप्लीशन टास्कसाठी मशीन लर्निंग पाइपलाइन परिभाषित आणि कॉन्फिगर करतो.

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

### जॉब सबमिट करा

1. हा Python स्क्रिप्ट Azure Machine Learning वर्कस्पेसमध्ये मशीन लर्निंग पाइपलाइन जॉब सबमिट करतो आणि नंतर जॉब पूर्ण होईपर्यंत थांबतो. त्याचे तपशील पुढीलप्रमाणे:

    - तो workspace_ml_client मधील jobs ऑब्जेक्टचा create_or_update मेथड कॉल करून पाइपलाइन जॉब सबमिट करतो. चालवायची पाइपलाइन pipeline_object ने निर्दिष्ट केली आहे, आणि जॉब चालवण्याचा प्रयोग experiment_name ने निर्दिष्ट केला आहे.

    - नंतर तो workspace_ml_client मधील jobs ऑब्जेक्टचा stream मेथड कॉल करून पाइपलाइन जॉब पूर्ण होईपर्यंत थांबतो. थांबायचा जॉब pipeline_job ऑब्जेक्टच्या name अ‍ॅट्रिब्यूटने निर्दिष्ट केला आहे.

    - सारांश म्हणून, हा स्क्रिप्ट Azure Machine Learning वर्कस्पेसमध्ये मशीन लर्निंग पाइपलाइन जॉब सबमिट करतो आणि नंतर जॉब पूर्ण होईपर्यंत थांबतो.

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

## 6. फाइन ट्यून केलेले मॉडेल वर्कस्पेसमध्ये नोंदणी करा

फाइन ट्यूनिंग जॉबच्या आउटपुटमधून मॉडेल नोंदणी करू. यामुळे फाइन ट्यून केलेल्या मॉडेल आणि फाइन ट्यूनिंग जॉब यांच्यातील संबंध ट्रॅक होईल. फाइन ट्यूनिंग जॉब पुढे फाउंडेशन मॉडेल, डेटा आणि प्रशिक्षण कोडशी संबंध ट्रॅक करतो.

### ML मॉडेल नोंदणी

1. हा Python स्क्रिप्ट Azure Machine Learning पाइपलाइनमध्ये प्रशिक्षित केलेले मशीन लर्निंग मॉडेल नोंदणी करतो. त्याचे तपशील पुढीलप्रमाणे:

    - तो Azure AI ML SDK मधील आवश्यक मॉड्यूल्स इम्पोर्ट करतो.

    - तो तपासतो की pipeline जॉबमधून trained_model आउटपुट उपलब्ध आहे का, workspace_ml_client मधील jobs ऑब्जेक्टचा get मेथड कॉल करून आणि त्याच्या outputs अ‍ॅट्रिब्यूटमध्ये प्रवेश करून.

    - तो pipeline जॉबचे नाव आणि आउटपुटचे नाव ("trained_model") वापरून प्रशिक्षित मॉडेलचा पथ तयार करतो.

    - तो फाइन-ट्यून केलेल्या मॉडेलसाठी नाव परिभाषित करतो, मूळ मॉडेल नावाच्या शेवटी "-ultrachat-200k" जोडून आणि कोणतेही स्लॅशेस हायफन्सने बदलून.

    - तो Model ऑब्जेक्ट तयार करून मॉडेल नोंदणीसाठी तयार होतो, ज्यात मॉडेलचा पथ, मॉडेलचा प्रकार (MLflow मॉडेल), मॉडेलचे नाव आणि आवृत्ती, आणि मॉडेलचे वर्णन यांचा समावेश आहे.

    - तो workspace_ml_client मधील models ऑब्जेक्टचा create_or_update मेथड कॉल करून मॉडेल नोंदणी करतो.

    - तो नोंदणीकृत मॉडेल छापतो.

1. सारांश म्हणून, हा स्क्रिप्ट Azure Machine Learning पाइपलाइनमध्ये प्रशिक्षित केलेले मशीन लर्निंग मॉडेल नोंदणी करतो.

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

## 7. फाइन ट्यून केलेले मॉडेल ऑनलाइन एंडपॉइंटवर डिप्लॉय करा

ऑनलाइन एंडपॉइंट्स एक टिकाऊ REST API देतात जे अशा अ‍ॅप्लिकेशन्ससह एकत्रित करता येते ज्यांना मॉडेल वापरायचे असते.

### एंडपॉइंट व्यवस्थापन

1. हा Python स्क्रिप्ट Azure Machine Learning मध्ये नोंदणीकृत मॉडेलसाठी मॅनेज्ड ऑनलाइन एंडपॉइंट तयार करतो. त्याचे तपशील पुढीलप्रमाणे:

    - तो Azure AI ML SDK मधील आवश्यक मॉड्यूल्स इम्पोर्ट करतो.

    - तो ऑनलाइन एंडपॉइंटसाठी एक अद्वितीय नाव परिभाषित करतो, ज्यात "ultrachat-completion-" या स्ट्रिंगनंतर टाइमस्टॅम्प जोडलेला असतो.

    - तो ManagedOnlineEndpoint ऑब्जेक्ट तयार करून ऑनलाइन एंडपॉइंट तयार करण्यासाठी तयार होतो, ज्यात एंडपॉइंटचे नाव, वर्णन, आणि ऑथेंटिकेशन मोड ("key") यांचा समावेश आहे.

    - तो workspace_ml_client मधील begin_create_or_update मेथड कॉल करून ऑनलाइन एंडपॉइंट तयार करतो आणि नंतर wait मेथड कॉल करून तयार होईपर्यंत थांबतो.

1. सारांश म्हणून, हा स्क्रिप्ट Azure Machine Learning मध्ये नोंदणीकृत मॉडेलसाठी मॅनेज्ड ऑनलाइन एंडपॉइंट तयार करतो.

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
> येथे तुम्हाला डिप्लॉयमेंटसाठी समर्थित SKU ची यादी मिळेल - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML मॉडेल डिप्लॉय करणे

1. हा Python स्क्रिप्ट Azure Machine Learning मध्ये नोंदणीकृत मशीन लर्निंग मॉडेल मॅनेज्ड ऑनलाइन एंडपॉइंटवर डिप्लॉय करतो. त्याचे तपशील पुढीलप्रमाणे:

    - तो ast मॉड्यूल इम्पोर्ट करतो, जे Python च्या अमूर्त व्याकरणाच्या झाडांवर प्रक्रिया करण्यासाठी फंक्शन्स पुरवतो.

    - तो डिप्लॉयमेंटसाठी instance type "Standard_NC6s_v3" सेट करतो.

    - तो तपासतो की foundation_model मध्ये inference_compute_allow_list टॅग आहे का. असल्यास, तो टॅगचे मूल्य स्ट्रिंगमधून Python लिस्टमध्ये रूपांतरित करतो आणि inference_computes_allow_list मध्ये ठेवतो. नसल्यास, inference_computes_allow_list None सेट करतो.

    - तो तपासतो की दिलेला instance type allow list मध्ये आहे का. नसल्यास, वापरकर्त्याला allow list मधील instance type निवडण्याचा संदेश छापतो.

    - तो ManagedOnlineDeployment ऑब्जेक्ट तयार करून डिप्लॉयमेंट तयार करण्यासाठी तयार होतो, ज्यात डिप्लॉयमेंटचे नाव, एंडपॉइंटचे नाव, मॉडेल आयडी, instance type आणि count, लिव्हनेस प्रॉब सेटिंग्ज, आणि रिक्वेस्ट सेटिंग्ज यांचा समावेश आहे.

    - तो workspace_ml_client मधील begin_create_or_update मेथड कॉल करून डिप्लॉयमेंट तयार करतो आणि नंतर wait मेथड कॉल करून तयार होईपर्यंत थांबतो.

    - तो एंडपॉइंटचा ट्रॅफिक 100% "demo" डिप्लॉयमेंटकडे निर्देशित करतो.

    - तो workspace_ml_client मधील begin_create_or_update मेथड कॉल करून एंडपॉइंट अपडेट करतो आणि नंतर result मेथड कॉल करून अपडेट पूर्ण होईपर्यंत थांबतो.

1. सारांश म्हणून, हा स्क्रिप्ट Azure Machine Learning मध्ये नोंदणीकृत मशीन लर्निंग मॉडेल मॅनेज्ड ऑनलाइन एंडपॉइंटवर डिप्लॉय करतो.

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

## 8. नमुना डेटासह एंडपॉइंटची चाचणी करा

आम्ही चाचणी डेटासेटमधून काही नमुना डेटा घेऊन ऑनलाइन एंडपॉइंटवर इन्फरन्ससाठी सबमिट करू. नंतर आम्ही स्कोअर केलेले लेबल्स आणि ग्राउंड ट्रूथ लेबल्स एकत्र दाखवू.

### निकाल वाचणे

1. हा Python स्क्रिप्ट JSON Lines फाइल pandas DataFrame मध्ये वाचतो, यादृच्छिक नमुना घेतो, आणि इंडेक्स रीसेट करतो. त्याचे तपशील पुढीलप्रमाणे:

    - तो ./ultrachat_200k_dataset/test_gen.jsonl फाइल pandas DataFrame मध्ये वाचतो. read_json फंक्शन lines=True आर्ग्युमेंटसह वापरले आहे कारण फाइल JSON Lines फॉरमॅटमध्ये आहे, जिथे प्रत्येक ओळ स्वतंत्र JSON ऑब्जेक्ट आहे.

    - तो DataFrame मधून 1 यादृच्छिक रकाना निवडतो. sample फंक्शन n=1 आर्ग्युमेंटसह वापरले आहे.

    - तो DataFrame चा इंडेक्स रीसेट करतो. reset_index फंक्शन drop=True आर्ग्युमेंटसह वापरले आहे ज्यामुळे मूळ इंडेक्स हटवून नवीन डिफॉल्ट पूर्णांक इंडेक्स तयार होतो.

    - तो head फंक्शन 2 आर्ग्युमेंटसह वापरून DataFrame च्या पहिल्या 2 रकान्या दाखवतो. मात्र, नमुना घेतल्यानंतर DataFrame मध्ये फक्त 1 रकाना असल्यामुळे फक्त तोच रकाना दाखवला जाईल.

1. सारांश म्हणून, हा स्क्रिप्ट JSON Lines फाइल pandas DataFrame मध्ये वाचतो, 1 यादृच्छिक रकाना घेतो, इंडेक्स रीसेट करतो, आणि पहिला रकाना दाखवतो.

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

### JSON ऑब्जेक्ट तयार करा

1. हा Python स्क्रिप्ट विशिष्ट पॅरामीटर्ससह JSON ऑब्जेक्ट तयार करतो आणि तो फाइल
- हे sample_score.json नावाचे फाइल उघडते

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

### एंडपॉइंट कॉल करणे

1. हा Python स्क्रिप्ट Azure Machine Learning मधील ऑनलाइन एंडपॉइंट कॉल करून JSON फाइलचे स्कोअरिंग करतो. त्याचे तपशील पुढीलप्रमाणे आहेत:

    - workspace_ml_client ऑब्जेक्टच्या online_endpoints प्रॉपर्टीचा invoke मेथड कॉल करतो. हा मेथड ऑनलाइन एंडपॉइंटला विनंती पाठवण्यासाठी आणि प्रतिसाद मिळवण्यासाठी वापरला जातो.

    - endpoint_name आणि deployment_name आर्ग्युमेंट्सद्वारे एंडपॉइंटचे नाव आणि डिप्लॉयमेंट निर्दिष्ट करतो. या प्रकरणात, एंडपॉइंटचे नाव online_endpoint_name व्हेरिएबलमध्ये आहे आणि डिप्लॉयमेंटचे नाव "demo" आहे.

    - request_file आर्ग्युमेंटद्वारे स्कोअर करायच्या JSON फाइलचा पथ निर्दिष्ट करतो. या प्रकरणात, फाइलचा पथ ./ultrachat_200k_dataset/sample_score.json आहे.

    - एंडपॉइंटकडून मिळालेला प्रतिसाद response व्हेरिएबलमध्ये साठवतो.

    - कच्चा प्रतिसाद प्रिंट करतो.

1. सारांश म्हणून, हा स्क्रिप्ट Azure Machine Learning मधील ऑनलाइन एंडपॉइंट कॉल करून JSON फाइलचे स्कोअरिंग करतो आणि प्रतिसाद प्रिंट करतो.

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

## 9. ऑनलाइन एंडपॉइंट हटवा

1. ऑनलाइन एंडपॉइंट हटवायला विसरू नका, अन्यथा एंडपॉइंटद्वारे वापरल्या गेलेल्या कम्प्युटसाठी बिलिंग चालू राहील. हा Python कोड Azure Machine Learning मधील ऑनलाइन एंडपॉइंट हटवतो. त्याचे तपशील पुढीलप्रमाणे आहेत:

    - workspace_ml_client ऑब्जेक्टच्या online_endpoints प्रॉपर्टीचा begin_delete मेथड कॉल करतो. हा मेथड ऑनलाइन एंडपॉइंट हटवण्याची प्रक्रिया सुरू करण्यासाठी वापरला जातो.

    - name आर्ग्युमेंटद्वारे हटवायच्या एंडपॉइंटचे नाव निर्दिष्ट करतो. या प्रकरणात, एंडपॉइंटचे नाव online_endpoint_name व्हेरिएबलमध्ये आहे.

    - wait मेथड कॉल करून हटवण्याची प्रक्रिया पूर्ण होईपर्यंत थांबतो. ही एक ब्लॉकिंग ऑपरेशन आहे, म्हणजे हटवण्याची प्रक्रिया पूर्ण होईपर्यंत स्क्रिप्ट पुढे चालणार नाही.

    - सारांश म्हणून, हा कोड Azure Machine Learning मधील ऑनलाइन एंडपॉइंट हटवण्याची प्रक्रिया सुरू करतो आणि ती पूर्ण होईपर्यंत थांबतो.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.