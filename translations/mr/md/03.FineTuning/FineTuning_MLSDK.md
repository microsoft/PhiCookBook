<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T20:58:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "mr"
}
-->
## Azure ML सिस्टम रजिस्ट्रीमधील chat-completion कॉम्पोनंट्स वापरून मॉडेल फाइन-ट्यून कसे करावे

या उदाहरणात आपण Phi-3-mini-4k-instruct मॉडेलचे फाइन-ट्यूनिंग करणार आहोत जे 2 लोकांमधील संभाषण पूर्ण करण्यासाठी ultrachat_200k डेटासेट वापरते.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.mr.png)

हे उदाहरण Azure ML SDK आणि Python वापरून फाइन-ट्यूनिंग कसे करायचे आणि नंतर फाइन-ट्यून केलेले मॉडेल रिअल टाईम इन्फरन्ससाठी ऑनलाइन एन्डपॉइंटवर कसे डिप्लॉय करायचे हे दाखवेल.

### प्रशिक्षण डेटा

आपण ultrachat_200k डेटासेट वापरणार आहोत. हा UltraChat डेटासेटचा खूप फिल्टर केलेला आवृत्ती आहे आणि Zephyr-7B-β, एक अत्याधुनिक 7b चॅट मॉडेल, ट्रेन करण्यासाठी वापरला गेला होता.

### मॉडेल

आपण Phi-3-mini-4k-instruct मॉडेल वापरू ज्याद्वारे वापरकर्ता chat-completion टास्कसाठी मॉडेल फाइनट्यून कसे करू शकतो हे दाखवले जाईल. जर तुम्ही हा नोटबुक विशिष्ट मॉडेल कार्डमधून उघडला असेल, तर त्या विशिष्ट मॉडेलचे नाव बदला.

### टास्क

- फाइन-ट्यूनसाठी मॉडेल निवडा.
- प्रशिक्षण डेटा निवडा आणि एक्सप्लोर करा.
- फाइन-ट्यूनिंग जॉब कॉन्फिगर करा.
- फाइन-ट्यूनिंग जॉब चालवा.
- प्रशिक्षण आणि मूल्यांकन मेट्रिक्स तपासा.
- फाइन-ट्यून केलेले मॉडेल रजिस्टर करा.
- रिअल टाईम इन्फरन्ससाठी फाइन-ट्यून मॉडेल डिप्लॉय करा.
- संसाधने क्लीनअप करा.

## 1. पूर्वतयारी सेटअप करा

- अवलंबित्वे इन्स्टॉल करा
- AzureML वर्कस्पेसशी कनेक्ट करा. अधिक जाणून घेण्यासाठी set up SDK authentication पाहा. खाली <WORKSPACE_NAME>, <RESOURCE_GROUP> आणि <SUBSCRIPTION_ID> बदला.
- azureml सिस्टम रजिस्ट्रीशी कनेक्ट करा
- ऐच्छिक experiment नाव सेट करा
- कॉम्प्युट तपासा किंवा तयार करा.

> [!NOTE]
> आवश्यक आहे की एक GPU नोडमध्ये एकापेक्षा जास्त GPU कार्ड्स असू शकतात. उदाहरणार्थ, Standard_NC24rs_v3 च्या एका नोडमध्ये 4 NVIDIA V100 GPUs असतात तर Standard_NC12s_v3 मध्ये 2 NVIDIA V100 GPUs असतात. या माहितीसाठी docs पहा. प्रत्येक नोडमधील GPU कार्ड्सची संख्या param gpus_per_node मध्ये सेट केली जाते. योग्यरित्या सेट केल्यास नोडमधील सर्व GPUs चा वापर होतो. शिफारस केलेले GPU compute SKU येथे आणि येथे पाहू शकता.

### Python लायब्ररी

खालील सेल चालवून अवलंबित्वे इन्स्टॉल करा. नवीन एन्व्हायर्नमेंटमध्ये हे टप्पा ऐच्छिक नाही.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML सह संवाद साधणे

1. हा Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा सोबत संवाद साधण्यासाठी वापरला जातो. त्याचे काय कार्य आहे याचे स्पष्टीकरण:

    - azure.ai.ml, azure.identity, आणि azure.ai.ml.entities पॅकेजमधील आवश्यक मॉड्युल्स इम्पोर्ट करतो. तसेच time मॉड्युल इम्पोर्ट करतो.

    - DefaultAzureCredential() वापरून ऑथेंटिकेशन करण्याचा प्रयत्न करतो, जे Azure क्लाउडमध्ये अॅप्लिकेशन्स जलद डेव्हलप करण्यासाठी सुलभ ऑथेंटिकेशन देते. जर हे अयशस्वी झाले तर InteractiveBrowserCredential() वापरतो, जे इंटरॅक्टिव लॉगिन प्रॉम्प्ट देते.

    - नंतर from_config पद्धत वापरून MLClient इन्स्टन्स तयार करण्याचा प्रयत्न करतो, जी डिफॉल्ट config फाईल (config.json) मधून कॉन्फिगरेशन वाचते. जर अयशस्वी झाले तर subscription_id, resource_group_name, आणि workspace_name मॅन्युअली देऊन MLClient तयार करतो.

    - "azureml" नावाच्या Azure ML रजिस्ट्रीसाठी आणखी एक MLClient तयार करतो. या रजिस्ट्रीमध्ये मॉडेल्स, फाइन-ट्यूनिंग पाइपलाईन्स, आणि एन्व्हायर्नमेंट्स संग्रहित असतात.

    - experiment_name "chat_completion_Phi-3-mini-4k-instruct" सेट करतो.

    - सध्याचा वेळ (epoch पासून सेकंदांमध्ये, फ्लोटिंग पॉइंट नंबर) पूर्णांकात आणि नंतर स्ट्रिंगमध्ये रूपांतरित करून युनिक टाइमस्टॅम्प जनरेट करतो. हा टाइमस्टॅम्प युनिक नावं आणि आवृत्त्या तयार करण्यासाठी वापरता येतो.

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

## 2. फाउंडेशन मॉडेल निवडा फाइन ट्यूनसाठी

1. Phi-3-mini-4k-instruct हा 3.8B पॅरामिटर्स असलेला, हलका, अत्याधुनिक ओपन मॉडेल आहे जो Phi-2 साठी वापरलेल्या डेटासेटवर आधारित आहे. हा मॉडेल Phi-3 मॉडेल कुटुंबाचा आहे आणि Mini आवृत्ती 4K आणि 128K या दोन प्रकारांत येते, ज्यामध्ये संदर्भ लांबी (टोकनमध्ये) आहे. आपल्याला त्यासाठी फाइनट्यून करावे लागेल जेणेकरून आपण तो वापरू शकू. तुम्ही AzureML Studio मधील Model Catalog मध्ये चॅट-कम्प्लीशन टास्कने फिल्टर करून हे मॉडेल्स ब्राउझ करू शकता. या उदाहरणात Phi-3-mini-4k-instruct मॉडेल वापरले आहे. जर तुम्ही हा नोटबुक वेगळ्या मॉडेलसाठी उघडला असेल तर मॉडेलचे नाव आणि आवृत्ती तदनुसार बदला.

    > [!NOTE]
    > मॉडेलची id प्रॉपर्टी ही फाइन ट्यूनिंग जॉबसाठी इनपुट म्हणून दिली जाते. AzureML Studio Model Catalog मधील मॉडेल तपशील पानावर Asset ID फील्ड म्हणून देखील उपलब्ध आहे.

2. हा Python स्क्रिप्ट Azure Machine Learning (Azure ML) सेवा सोबत संवाद साधतो. त्याचे काय कार्य आहे याचे स्पष्टीकरण:

    - model_name "Phi-3-mini-4k-instruct" सेट करतो.

    - registry_ml_client च्या models प्रॉपर्टीचा get मेथड वापरून Azure ML रजिस्ट्रीमधून या नावाचा नवीनतम आवृत्तीचा मॉडेल मिळवतो. get मेथड दोन आर्ग्युमेंट्ससह कॉल केली जाते: मॉडेलचे नाव आणि लेबल ज्याद्वारे नवीनतम आवृत्ती मिळवायची आहे.

    - कन्सोलवर एक संदेश प्रिंट करतो ज्यात वापरासाठी निवडलेले मॉडेलचे नाव, आवृत्ती आणि id दाखवले जाते. स्ट्रिंगच्या format मेथडचा वापर करून हे मूल्ये संदेशात घातले जातात. foundation_model ऑब्जेक्टच्या प्रॉपर्टीज म्हणून नाव, आवृत्ती आणि id मिळवले जातात.

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

## 3. जॉबसाठी कॉम्प्युट तयार करा

फाइनट्यून जॉब फक्त GPU कॉम्प्युटसह चालतो. कॉम्प्युटचा आकार मॉडेलच्या आकारावर अवलंबून असतो आणि योग्य कॉम्प्युट निवडणे अनेकदा अवघड होते. या सेलमध्ये वापरकर्त्याला योग्य कॉम्प्युट निवडण्याचा मार्गदर्शन दिले जाते.

> [!NOTE]
> खालील कॉम्प्युट्स सर्वात ऑप्टिमाइझ्ड कॉन्फिगरेशनसह कार्य करतात. कॉन्फिगरेशनमध्ये बदल केल्यास Cuda Out Of Memory त्रुटी येऊ शकते. अशा परिस्थितीत कॉम्प्युट मोठ्या आकारात अपग्रेड करण्याचा प्रयत्न करा.

> [!NOTE]
> खाली compute_cluster_size निवडताना खात्री करा की कॉम्प्युट तुमच्या resource group मध्ये उपलब्ध आहे. जर एखादा कॉम्प्युट उपलब्ध नसेल तर त्यासाठी प्रवेश मिळवण्यासाठी विनंती करू शकता.

### फाइन ट्यूनिंगसाठी मॉडेलची सपोर्ट तपासणी

1. हा Python स्क्रिप्ट Azure ML मॉडेलशी संवाद साधतो. त्याचे काय कार्य आहे याचे स्पष्टीकरण:

    - ast मॉड्युल इम्पोर्ट करतो, जे Python च्या syntax grammar च्या ट्री प्रोसेसिंगसाठी फंक्शन्स देते.

    - foundation_model ऑब्जेक्टमध्ये finetune_compute_allow_list नावाचा टॅग आहे का ते तपासतो. Azure ML मध्ये टॅग्स key-value जोडी असतात ज्याचा वापर मॉडेल्स फिल्टर आणि सॉर्ट करण्यासाठी होतो.

    - जर finetune_compute_allow_list टॅग असेल, तर ast.literal_eval वापरून त्या टॅगच्या व्हॅल्यूस (स्ट्रिंग) ला सुरक्षितपणे Python लिस्टमध्ये रूपांतरित करतो. ही लिस्ट computes_allow_list मध्ये assign केली जाते. नंतर संदेश प्रिंट करतो की यादीतील कॉम्प्युटमधून कॉम्प्युट तयार करा.

    - जर टॅग नसेल, तर computes_allow_list None सेट करतो आणि एक संदेश प्रिंट करतो की finetune_compute_allow_list हा टॅग मॉडेलच्या टॅग्समध्ये नाही.

    - सारांशात, हा स्क्रिप्ट मॉडेलच्या मेटाडेटामध्ये विशिष्ट टॅग तपासतो, त्याचा व्हॅल्यूस लिस्टमध्ये रूपांतरित करतो जर तो असेल, आणि वापरकर्त्यास त्याबाबत माहिती देतो.

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

### कॉम्प्युट इन्स्टन्स तपासणी

1. हा Python स्क्रिप्ट Azure ML सेवा वापरून कॉम्प्युट इन्स्टन्सवर अनेक तपासण्या करतो. त्याचे काय कार्य आहे याचे स्पष्टीकरण:

    - compute_cluster नावाच्या कॉम्प्युट इन्स्टन्सला Azure ML वर्कस्पेसमधून मिळवण्याचा प्रयत्न करतो. जर provisioning state "failed" असेल तर ValueError उचलतो.

    - जर computes_allow_list None नसेल, तर लिस्टमधील सर्व कॉम्प्युट साइज लोअरकेसमध्ये रूपांतरित करतो आणि तपासतो की सध्याच्या कॉम्प्युटचा साइज त्या लिस्टमध्ये आहे का. नसेल तर ValueError उचलतो.

    - जर computes_allow_list None असेल, तर कॉम्प्युट साइज unsupported GPU VM साइज लिस्टमध्ये आहे का ते तपासतो. असल्यास ValueError उचलतो.

    - वर्कस्पेसमधील उपलब्ध सर्व कॉम्प्युट साइजची यादी मिळवतो. प्रत्येक साइजवर फिरून तपासतो की त्याचे नाव सध्याच्या कॉम्प्युटच्या साइजशी जुळते का. जर होय, तर त्या कॉम्प्युट साइजसाठी GPU ची संख्या मिळवतो आणि gpu_count_found True करतो.

    - gpu_count_found True असल्यास कॉम्प्युटमधील GPU ची संख्या प्रिंट करतो. अन्यथा ValueError उचलतो.

    - सारांशात, हा स्क्रिप्ट Azure ML वर्कस्पेसमधील कॉम्प्युट इन्स्टन्सची provisioning state, साइज, आणि GPU संख्या तपासतो.

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

## 4. फाइन-ट्यूनिंगसाठी डेटासेट निवडा

1. आपण ultrachat_200k डेटासेट वापरतो. या डेटासेटमध्ये चार स्प्लिट्स आहेत, जे Supervised fine-tuning (sft) साठी योग्य आहेत. Generation ranking (gen). प्रत्येक स्प्लिटमध्ये उदाहरणांची संख्या खालीलप्रमाणे आहे:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. पुढील काही सेल्समध्ये फाइन ट्यूनिंगसाठी बेसिक डेटा तयारी दाखवली आहे:

### काही डेटा रows दृश्य करा

आपण हा सॅम्पल लवकर चालवू इच्छितो, म्हणून train_sft, test_sft फाइल्स जतन करा ज्यात आधीपासून ट्रिम केलेल्या रowsपैकी 5% आहेत. याचा अर्थ फाइन ट्यून केलेल्या मॉडेलची अचूकता कमी असेल, त्यामुळे ते प्रत्यक्ष वापरासाठी योग्य नाही.
download-dataset.py स्क्रिप्ट ultrachat_200k डेटासेट डाउनलोड करण्यासाठी आणि फाइनट्यून पाइपलाईन कॉम्पोनंटसाठी योग्य स्वरूपात डेटासेट ट्रान्सफॉर्म करण्यासाठी वापरला जातो. डेटासेट मोठा असल्यामुळे येथे फक्त त्याचा काही भाग आहे.

1. खालील स्क्रिप्ट फक्त डेटाच्या 5% डाउनलोड करते. dataset_split_pc पॅरामीटर बदलून हा टक्का वाढवता येतो.

    > [!NOTE]
    > काही भाषा मॉडेल्सचे वेगवेगळे भाषा कोड्स असतात, त्यामुळे डेटासेटमधील कॉलम नावे त्यानुसार असावीत.

1. डेटा कसा दिसावा याचे उदाहरण येथे आहे
चॅट-कम्प्लीशन डेटासेट parquet फॉरमॅटमध्ये संग्रहित आहे ज्यात प्रत्येक एंट्री खालील स्कीमा वापरते:

    - हे JSON (JavaScript Object Notation) डॉक्युमेंट आहे, जे लोकप्रिय डेटा इंटरचेंज फॉरमॅट आहे. हे executable code नाही, तर डेटा स्टोअर आणि ट्रान्सपोर्ट करण्याचा मार्ग आहे. याची रचना खालीलप्रमाणे आहे:

    - "prompt": या कीमध्ये एक स्ट्रिंग व्हॅल्यू असते जी AI सहाय्यकाला दिलेली टास्क किंवा प्रश्न दर्शवते.

    - "messages": या कीमध्ये ऑब्जेक्ट्सची एक अ‍ॅरे असते. प्रत्येक ऑब्जेक्ट वापरकर्ता आणि AI सहाय्यक यांच्यातील संभाषणातील संदेश दर्शवतो. प्रत्येक संदेश ऑब्जेक्टमध्ये दोन कीज असतात:

    - "content": संदेशाचा मजकूर असतो.
    - "role": संदेश पाठवणाऱ्या घटकाची भूमिका असते, "user" किंवा "assistant" असू शकते.
    - "prompt_id": प्रत्येक प्रॉम्प्टसाठी युनिक आयडी असतो.

1. या JSON डॉक्युमेंटमध्ये एक संभाषण आहे जिथे वापरकर्ता AI सहाय्यकाला dystopian कथा साठी नायक तयार करण्यास सांगतो. सहाय्यक प्रतिसाद देतो, आणि नंतर वापरकर्ता अधिक तपशील विचारतो. सहाय्यक अधिक तपशील देण्यास तयार आहे. संपूर्ण संभाषण विशिष्ट प्रॉम्प्ट आयडीशी संबंधित आहे.

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

1. हा Python स्क्रिप्ट download-dataset.py नावाच्या हेल्पर स्क्रिप्टचा वापर करून डेटासेट डाउनलोड करतो. त्याचे काय कार्य आहे याचे स्पष्टीकरण:

    - os मॉड्युल इम्पोर्ट करतो, जे ऑपरेटिंग सिस्टमशी संबंधित कार्यांसाठी पोर्टेबल मार्ग देते.

    - os.system फंक्शन वापरून shell मध्ये download-dataset.py स्क्रिप्ट चालवतो ज्यात कमांड-लाइन आर्ग्युमेंट्स दिलेले आहेत: डाउनलोड करायचा डेटासेट (HuggingFaceH4/ultrachat_200k), डाउनलोड डायरेक्टरी (ultrachat_200k_dataset), आणि डेटासेटचा किती टक्का स्प्लिट करायचा (5). os.system कमांडचा exit status परत करते, जो exit_status मध्ये ठेवला जातो.

    - exit_status 0 नसल्यास, म्हणजे कमांड अयशस्वी झाल्यास, Exception उचलतो ज्यात डेटासेट डाउनलोड करताना त्रुटी असल्याचे सांगितले आहे.

    - सारांशात, हा स्क्रिप्ट हेल्पर स्क्रिप्ट वापरून डेटासेट डाउनलोड करतो आणि जर कमांड फेल झाली तर अपवाद उचलतो.

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

1. हा Python स्क्रिप्ट JSON Lines फाइल pandas DataFrame मध्ये लोड करतो आणि पहिल्या 5 रows प्रदर्शित करतो. त्याचे काय कार्य आहे याचे स्पष्टीकरण:

    - pandas लायब्ररी इम्पोर्ट करतो, जी डेटा मॅनिप्युलेशन आणि विश्लेषणासाठी शक्तिशाली आहे.

    - pandas च्या डिस्प्ले ऑप्शन्समध्ये max column width 0 सेट करतो, म्हणजे प्रत्येक कॉलमचा पूर्ण मजकूर ट्रंकेट न होता दिसेल.

    - pd.read_json वापरून ultrachat_200k_dataset डायरेक्टरीमधील train_sft.jsonl फाइल JSON Lines स्वरूपात लोड करतो (lines=True).

    - head मेथड वापरून पहिल्या 5 रows प्रदर्शित करतो. जर DataFrame मध्ये 5 पेक्षा कमी रows असतील तर सर्व रows दाखवतो.

    - सारांशात, हा स्क्रिप्ट JSON Lines फाइल DataFrame मध्ये लोड करतो आणि पहिल्या 5 रows पूर्ण मजकूरासह दाखवतो.

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

## 5. मॉडेल आणि डेटाचा वापर करून फाइन ट्यूनिंग जॉब सबमिट करा

chat-completion पाइपलाईन कॉम्पोनंट वापरून जॉब तयार करा. फाइन ट्यूनिंगसाठी समर्थित सर्व पॅरामीटर्सबद्दल अधिक जाणून घ्या.

### फाइनट्यून पॅरामीटर्स परिभाषित करा

1. फाइनट्यून पॅरामीटर्स दोन प्रकारांत विभागले जाऊ शकतात - प्रशिक्षण पॅरामीटर्स, ऑप्टिमायझेशन पॅरामीटर्स

1. प्रशिक्षण पॅरामीटर्समध्ये खालील बाबी येतात -

    - वापराय
training pipeline विविध पॅरामीटर्सवर आधारित आहे, आणि नंतर हा display name प्रिंट करत आहे. ```python
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

### Pipeline सेटअप करणे
हा Python स्क्रिप्ट Azure Machine Learning SDK वापरून एक मशीन लर्निंग pipeline define आणि configure करत आहे. यामध्ये काय काय होते ते खालीलप्रमाणे:
1. Azure AI ML SDK मधील आवश्यक modules import केले जातात.
2. Registry मधून "chat_completion_pipeline" नावाचा pipeline component fetch केला जातो.
3. `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False` वापरून pipeline job define केली जाते, म्हणजे pipeline मधील कोणताही step fail झाला तर pipeline थांबेल.
4. सारांशात, हा स्क्रिप्ट Azure Machine Learning SDK वापरून chat completion task साठी एक मशीन लर्निंग pipeline define आणि configure करत आहे.

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

### Job सबमिट करणे
1. हा Python स्क्रिप्ट Azure Machine Learning workspace मध्ये एक मशीन लर्निंग pipeline job submit करत आहे आणि नंतर job पूर्ण होईपर्यंत थांबतो. यामध्ये काय होते ते खालीलप्रमाणे:
- workspace_ml_client च्या jobs object चा create_or_update method कॉल करून pipeline job submit केला जातो. pipeline_object मध्ये चालवायचा pipeline दिलेला आहे आणि experiment_name मध्ये job कुठल्या experiment अंतर्गत चालवायचा आहे ते दिलेले आहे.
- नंतर workspace_ml_client च्या jobs object चा stream method कॉल करून pipeline job पूर्ण होईपर्यंत थांबले जाते. pipeline_job च्या name attribute द्वारे job specify केला जातो.
- सारांशात, हा स्क्रिप्ट Azure Machine Learning workspace मध्ये pipeline job submit करतो आणि job पूर्ण होईपर्यंत थांबतो.

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

## 6. Fine tuned model workspace मध्ये register करणे
आपण fine tuning job च्या output मधून model register करू. यामुळे fine tuned model आणि fine tuning job यामध्ये lineage track होईल. fine tuning job foundation model, data आणि training code शी देखील lineage track करतो.

### ML Model Register करणे
1. हा Python स्क्रिप्ट Azure Machine Learning pipeline मध्ये train केलेला मशीन लर्निंग model register करत आहे. यामध्ये काय होते ते खालीलप्रमाणे:
- Azure AI ML SDK मधील आवश्यक modules import करतो.
- pipeline job च्या output मधून trained_model उपलब्ध आहे का ते workspace_ml_client च्या jobs object चा get method कॉल करून आणि outputs attribute access करून तपासतो.
- pipeline job चं नाव आणि output नाव ("trained_model") वापरून trained model चा path तयार करतो.
- मूळ model नावाच्या शेवटी "-ultrachat-200k" जोडून आणि स्लॅशेस हायफनने बदलून fine-tuned model साठी नाव define करतो.
- Model object तयार करून विविध पॅरामीटर्ससह, जसे की model path, model type (MLflow model), नाव, version आणि description, model register करण्यासाठी तयार होतो.
- workspace_ml_client च्या models object चा create_or_update method कॉल करून model register करतो.
- नोंदणीकृत model print करतो.
1. सारांशात, हा स्क्रिप्ट Azure Machine Learning pipeline मध्ये train केलेला मशीन लर्निंग model register करतो.

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

## 7. Fine tuned model ऑनलाइन endpoint वर deploy करणे
ऑनलाइन endpoints टिकाऊ REST API देतात ज्याचा वापर applications मध्ये model वापरण्यासाठी केला जातो.

### Endpoint व्यवस्थापन
1. हा Python स्क्रिप्ट Azure Machine Learning मध्ये registered model साठी managed online endpoint तयार करत आहे. यामध्ये काय होते ते खालीलप्रमाणे:
- Azure AI ML SDK मधील आवश्यक modules import करतो.
- "ultrachat-completion-" या स्ट्रिंगच्या शेवटी timestamp जोडून online endpoint साठी unique नाव define करतो.
- ManagedOnlineEndpoint object तयार करून endpoint नाव, description आणि authentication mode ("key") यांसह online endpoint तयार करण्यासाठी तयार होतो.
- workspace_ml_client च्या begin_create_or_update method कॉल करून online endpoint तयार करतो आणि wait method वापरून तयार होईपर्यंत थांबतो.
1. सारांशात, हा स्क्रिप्ट Azure Machine Learning मध्ये registered model साठी managed online endpoint तयार करतो.

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
> तुम्हाला येथे deployment साठी supported SKU ची यादी मिळेल - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML Model Deploy करणे

1. हा Python स्क्रिप्ट Azure Machine Learning मध्ये registered मशीन लर्निंग model managed online endpoint वर deploy करत आहे. यामध्ये काय होते ते खालीलप्रमाणे:

    - ast module import करतो, ज्यात Python abstract syntax grammar च्या trees process करण्यासाठी functions असतात.

    - deployment साठी instance type "Standard_NC6s_v3" सेट करतो.

    - foundation model मध्ये inference_compute_allow_list tag आहे का ते तपासतो. असल्यास, त्या tag चा value string मधून Python list मध्ये convert करतो आणि inference_computes_allow_list मध्ये assign करतो. नसेल तर, inference_computes_allow_list None सेट करतो.

    - specified instance type allow list मध्ये आहे का ते तपासतो. नसेल तर वापरकर्त्याला allow list मधून instance type निवडण्याचा संदेश print करतो.

    - ManagedOnlineDeployment object तयार करून deployment नाव, endpoint नाव, model ID, instance type आणि count, liveness probe settings, आणि request settings यांसह deployment तयार करण्यासाठी तयार होतो.

    - workspace_ml_client च्या begin_create_or_update method कॉल करून deployment तयार करतो आणि wait method वापरून तयार होईपर्यंत थांबतो.

    - endpoint चा traffic 100% "demo" deployment कडे directs करतो.

    - workspace_ml_client च्या begin_create_or_update method कॉल करून endpoint update करतो आणि result method वापरून update पूर्ण होईपर्यंत थांबतो.

1. सारांशात, हा स्क्रिप्ट Azure Machine Learning मध्ये registered model managed online endpoint वर deploy करतो.

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

## 8. Sample data वापरून endpoint चाचणी करणे

आपण test dataset मधून काही sample data fetch करू आणि online endpoint वर inference साठी submit करू. नंतर scored labels आणि ground truth labels एकत्र दाखवू.

### परिणाम वाचणे

1. हा Python स्क्रिप्ट JSON Lines फाइल pandas DataFrame मध्ये वाचतो, random sample घेतो आणि index reset करतो. यामध्ये काय होते ते खालीलप्रमाणे:

    - ./ultrachat_200k_dataset/test_gen.jsonl फाइल pandas DataFrame मध्ये वाचतो. read_json फंक्शन lines=True argument सोबत वापरतो कारण फाइल JSON Lines फॉर्मॅटमध्ये आहे, जिथे प्रत्येक ओळ स्वतंत्र JSON ऑब्जेक्ट आहे.

    - DataFrame मधून random 1 row निवडतो. sample फंक्शन n=1 argument सोबत वापरतो.

    - DataFrame चा index reset करतो. reset_index फंक्शन drop=True argument सोबत वापरतो ज्यामुळे मूळ index हटवून नवीन default integer index तयार होतो.

    - DataFrame च्या पहिल्या 2 rows head फंक्शनने दाखवतो. पण sample नंतर DataFrame मध्ये फक्त 1 row असल्यामुळे फक्त तीच एक ओळ दाखवेल.

1. सारांशात, हा स्क्रिप्ट JSON Lines फाइल pandas DataFrame मध्ये वाचतो, 1 row चा random sample घेतो, index reset करतो आणि पहिली ओळ दाखवतो.

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

### JSON ऑब्जेक्ट तयार करणे

1. हा Python स्क्रिप्ट विशिष्ट पॅरामीटर्ससह JSON ऑब्जेक्ट तयार करतो आणि ते फाइलमध्ये सेव्ह करतो. यामध्ये काय होते ते खालीलप्रमाणे:

    - json module import करतो, ज्यात JSON डेटा हाताळण्यासाठी फंक्शन्स असतात.

    - parameters नावाचा dictionary तयार करतो ज्यात मशीन लर्निंग मॉडेलसाठी पॅरामीटर्स आहेत. keys आहेत "temperature", "top_p", "do_sample", आणि "max_new_tokens", ज्यांचे values अनुक्रमे 0.6, 0.9, True, आणि 200 आहेत.

    - दुसरा dictionary test_json तयार करतो ज्यात दोन keys आहेत: "input_data" आणि "params". "input_data" चा value दुसऱ्या dictionary मध्ये आहे ज्यात "input_string" आणि "parameters" keys आहेत. "input_string" मध्ये test_df DataFrame मधील पहिला message list स्वरूपात आहे. "parameters" मध्ये वर तयार केलेला parameters dictionary आहे. "params" चा value रिक्त dictionary आहे.

    - sample_score.json नावाची फाइल उघडतो

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

### Endpoint invoke करणे

1. हा Python स्क्रिप्ट Azure Machine Learning मधील online endpoint invoke करून JSON फाइल score करतो. यामध्ये काय होते ते खालीलप्रमाणे:

    - workspace_ml_client च्या online_endpoints property चा invoke method कॉल करतो. हा method online endpoint ला request पाठवण्यासाठी आणि response मिळवण्यासाठी वापरला जातो.

    - endpoint आणि deployment चे नाव endpoint_name आणि deployment_name arguments मध्ये specify करतो. येथे endpoint नाव online_endpoint_name मध्ये आहे आणि deployment नाव "demo" आहे.

    - score करायची JSON फाइल request_file argument मध्ये specify करतो. येथे फाइल आहे ./ultrachat_200k_dataset/sample_score.json.

    - endpoint कडून response response variable मध्ये साठवतो.

    - raw response print करतो.

1. सारांशात, हा स्क्रिप्ट Azure Machine Learning मधील online endpoint invoke करून JSON फाइल score करतो आणि response print करतो.

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

## 9. ऑनलाइन endpoint delete करणे

1. ऑनलाइन endpoint delete करायला विसरू नका, नाहीतर endpoint वापरलेल्या compute साठी billing चालू राहील. हा Python code Azure Machine Learning मधील online endpoint delete करतो. यामध्ये काय होते ते खालीलप्रमाणे:

    - workspace_ml_client च्या online_endpoints property चा begin_delete method कॉल करतो. हा method online endpoint delete करण्यासाठी सुरुवात करतो.

    - delete करायच्या endpoint चे नाव name argument मध्ये specify करतो. येथे endpoint नाव online_endpoint_name मध्ये आहे.

    - wait method कॉल करून delete operation पूर्ण होईपर्यंत थांबतो. हा blocking operation आहे, म्हणजे delete पूर्ण होईपर्यंत स्क्रिप्ट पुढे चालणार नाही.

    - सारांशात, हा code Azure Machine Learning मधील online endpoint delete करण्यास सुरुवात करतो आणि operation पूर्ण होईपर्यंत थांबतो.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी भाषांतर शिफारस केली जाते. या भाषांतराच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थनिर्णयांसाठी आम्ही जबाबदार नाही.