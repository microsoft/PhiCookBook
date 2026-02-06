## Azure ML सिस्टम रजिस्ट्रीबाट च्याट-सम्पूर्णता कम्पोनेन्टहरू कसरी प्रयोग गर्ने मोडेललाई फाइन ट्विन गर्न

यस उदाहरणमा हामी Phi-3-mini-4k-instruct मोडेललाई दुई व्यक्तिबीचको संवाद पूरा गर्न ultrachat_200k डाटासेटको मद्दतले फाइन ट्विन गर्ने छौं।

![MLFineTune](../../../../translated_images/ne/MLFineTune.928d4c6b3767dd35.webp)

यो उदाहरणले तपाईंलाई Azure ML SDK र Python प्रयोग गरेर फाइन ट्विन कसरी गर्ने र त्यसपछि फाइन ट्विन गरिएको मोडेललाई वास्तविक समयमा अनुमानका लागि अनलाइन एन्डपोइन्टमा कसरी डिप्लोय गर्ने देखाउनेछ।

### प्रशिक्षण डेटा

हामी ultrachat_200k डाटासेट प्रयोग गर्नेछौं। यो UltraChat डाटासेटको धेरै छनोट गरिएको संस्करण हो र Zephyr-7B-β लाई प्रशिक्षण दिन प्रयोग गरिएको थियो, जुन अत्याधुनिक 7b च्याट मोडेल हो।

### मोडेल

अहिले हामी Phi-3-mini-4k-instruct मोडेल प्रयोग गर्नेछौं जसले उपयोगकर्तालाई च्याट-सम्पूर्णता कार्यका लागि मोडेल फाइन ट्विन गर्न कसरी गर्ने देखाउँछ। यदि तपाईंले यो नोटबुक कुनै विशिष्ट मोडेल कार्डबाट खोल्नुभएको हो भने, कृपया विशिष्ट मोडेल नाम परिवर्तन गर्नुस्।

### कार्यहरू

- फाइन ट्विन गर्ने मोडेल छान्नुहोस्।
- प्रशिक्षण डेटा छान्नुहोस् र अन्वेषण गर्नुहोस्।
- फाइन ट्विनिङ कार्य कन्फिगर गर्नुहोस्।
- फाइन ट्विनिङ कार्य चलाउनुहोस्।
- प्रशिक्षण र मूल्याङ्कन मेट्रिक्स समीक्षा गर्नुहोस्।
- फाइन ट्विन गरिएको मोडेल दर्ता गर्नुहोस्।
- वास्तविक समय अनुमानका लागि फाइन ट्विन गरिएको मोडेल डिप्लोय गर्नुहोस्।
- स्रोतहरू सफा गर्नुहोस्।

## १. पूर्व आवश्यकताहरू सेटअप गर्नुहोस्

- निर्भरता स्थापना गर्नुहोस्
- AzureML Workspace सँग जडान गर्नुहोस्। सेट अप SDK प्रमाणीकरण हेर्नुहोस्। तल <WORKSPACE_NAME>, <RESOURCE_GROUP> र <SUBSCRIPTION_ID> परिवर्तन गर्नुहोस्।
- azureml सिस्टम रजिस्ट्रीसँग जडान गर्नुहोस्
- वैकल्पिक रूपमा एउटा प्रयोग नमूना नाम सेट गर्नुहोस्
- कम्प्युट जाँच वा सिर्जना गर्नुहोस्।

> [!NOTE]
> आवश्यकता एकल GPU नोडसँग धेरै GPU कार्डहरू हुन सक्छन्। उदाहरणका लागि, Standard_NC24rs_v3 नोडमा ४ NVIDIA V100 GPU हरू छन् भने Standard_NC12s_v3 मा २ NVIDIA V100 GPU हरू छन्। थप जानकारीका लागि दस्तावेजहरू हेर्नुहोस्। प्रत्येक नोडको GPU कार्डहरूको संख्या तलको gpus_per_node प्यारामिटरमा सेट गरिएको छ। यो मान सही सेट गर्दा नोडका सबै GPU हरूको उपयोग सुनिश्चित हुन्छ। सिफारिस गरिएका GPU कम्प्युट SKU हरू यहाँ र यहाँ फेला पार्न सकिन्छ।

### Python पुस्तकालयहरू

तलको सेल चलाएर निर्भरता स्थापना गर्नुहोस्। नयाँ वातावरणमा चलाउँदा यो वैकल्पिक कदम होइन।

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML सँग अन्तरक्रिया गर्ने

1. यस Python स्क्रिप्टले Azure Machine Learning (Azure ML) सेवासँग अन्तरक्रिया गर्छ। यसको कार्यहरू निम्नानुसार छन्:

    - azure.ai.ml, azure.identity, र azure.ai.ml.entities प्याकेजबाट आवश्यक मोड्युलहरू आयात गर्छ। साथै time मोड्युल पनि आयात गर्दछ।

    - DefaultAzureCredential() प्रयोग गरेर प्रमाणिकरण गर्न प्रयास गर्छ, जुन Azure क्लाउडमा चलिरहेका अनुप्रयोगहरू तिब्र विकासका लागि सजिलो प्रमाणीकरण हो। असफल भएमा InteractiveBrowserCredential() प्रयोग गरी अन्तरक्रियात्मक लगइन प्रॉम्प्ट देखाउँछ।

    - त्यसपछि from_config विधि प्रयोग गरी MLClient उदाहरण सिर्जना गर्न प्रयास गर्छ, जुन default config फाइल (config.json) बाट कन्फिगरेसन पढ्छ। असफल भएमा, subscription_id, resource_group_name, र workspace_name म्यानुअली प्रदान गरेर MLClient सिर्जना गर्छ।

    - अर्को MLClient उदाहरण Azure ML रजिस्ट्री "azureml" को लागि सिर्जना गर्छ। यो रजिस्ट्री मोडेलहरू, फाइन-ट्युनिङ पाइपलाइनहरू, र वातावरणहरू राखिन्छ।

    - प्रयोग नमूना नाम "chat_completion_Phi-3-mini-4k-instruct" सेट गर्छ।

    - हालको समय (epoch को सेकेन्डमा, float मा) लाई पूर्णांक र त्यसपछि स्ट्रिङमा रूपान्तर गरी एक विशिष्ट टाइमस्ट्याम्प बनाउँछ। यो टाइमस्ट्याम्प अनौठो नाम र संस्करण बनाउन प्रयोग गर्न सकिन्छ।

    ```python
    # Azure ML र Azure Identity बाट आवश्यक मोड्युलहरू आयात गर्नुहोस्
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # समय मोड्युल आयात गर्नुहोस्
    
    # DefaultAzureCredential प्रयोग गरेर प्रमाणीकरण गर्ने प्रयास गर्नुहोस्
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # DefaultAzureCredential असफल भएमा, InteractiveBrowserCredential प्रयोग गर्नुहोस्
        credential = InteractiveBrowserCredential()
    
    # डिफल्ट कन्फिग फाइल प्रयोग गरेर MLClient उदाहरण बनाउन प्रयास गर्नुहोस्
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # यदि त्यो असफल भयो भने, विवरणहरू म्यानुअली दिँदै MLClient उदाहरण सिर्जना गर्नुहोस्
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" नामको Azure ML रजिष्ट्रीका लागि अर्को MLClient उदाहरण सिर्जना गर्नुहोस्
    # यो रजिष्ट्री मोडेलहरू, फाइन-ट्यूनिङ पाइपलाइनहरू, र वातावरणहरू राखिने स्थान हो
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # प्रयोगशाला नाम सेट गर्नुहोस्
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # अनौठो नाम र संस्करणहरूका लागि प्रयोग गर्न सकिने अनौठो टाइमस्टाम्प उत्पादन गर्नुहोस्
    timestamp = str(int(time.time()))
    ```

## २. फाइन ट्विनको लागि एक आधारभूत मोडेल छान्नुहोस्

1. Phi-3-mini-4k-instruct 3.8B प्यारामिटरको, हल्का, अत्याधुनिक खुला मोडेल हो जुन Phi-2 का लागि प्रयोग गरिएका डाटासेटहरूमा आधारित छ। यो मोडेल Phi-3 मोडेल परिवारको हो र Mini संस्करण 4K र 128K दुई भेरियन्टहरूमा आउँछ जुन सन्दर्भ लम्बाइ (टोकनहरूमा) सम्हाल्न सक्छ। हामीले यसलाई हाम्रो विशिष्ट प्रयोजनका लागि फाइन ट्विन गर्न आवश्यक छ। तपाईं AzureML Studio को मोडेल क्याटलगमा च्याट-सम्पूर्णता कार्य अनुसार फिल्टर गरेर यी मोडेलहरू ब्राउज गर्न सक्नुहुन्छ। यस उदाहरणमा, हामी Phi-3-mini-4k-instruct मोडेल प्रयोग गर्छौं। यदि तपाईंले यो नोटबुक कुनै अन्य मोडेलका लागि खोल्नुभएको छ भने मोडेल नाम र संस्करण परिवर्तन गर्नुहोस्।

> [!NOTE]
> मोडेल id सम्पत्ति, जुन फाइन ट्विनिङ कार्यको इनपुटका रूपमा दिइनेछ। AzureML Studio Model Catalog मा मोडेल विवरण पृष्ठमा यो Asset ID फिल्डमा पनि उपलब्ध छ।

2. यस Python स्क्रिप्टले Azure Machine Learning (Azure ML) सँग अन्तरक्रिया गर्छ। यसका कार्यहरू:

    - model_name लाई "Phi-3-mini-4k-instruct" सेट गर्छ।

    - registry_ml_client को models सम्पत्तिको get विधि प्रयोग गरेर Azure ML रजिस्ट्रीबाट निर्दिष्ट मोडेलको नवीनतम संस्करण प्राप्त गर्छ। get मेथडलाई दुई तर्क: मोडेलको नाम र लेबल जुन नवीनतम संस्करण बुलाउन प्रयोग हुन्छ।

    - फाइन ट्विनिङका लागि प्रयोग हुने मोडेलको नाम, संस्करण, र id कन्सोलमा प्रिन्ट गर्छ।

    ```python
    # मोडेल नाम सेट गर्नुहोस्
    model_name = "Phi-3-mini-4k-instruct"
    
    # Azure ML रजिष्ट्रि बाट मोडेलको नवीनतम संस्करण प्राप्त गर्नुहोस्
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # मोडेल नाम, संस्करण, र आईडी प्रिन्ट गर्नुहोस्
    # यी जानकारी ट्र्याकिङ र डिबगिङको लागि उपयोगी छन्
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## ३. कार्यसँग प्रयोग गर्न कम्प्युट सिर्जना गर्नुहोस्

फाइनट्यून कार्य GPU कम्प्युटमा मात्र काम गर्छ। कम्प्युटको आकार मोडेल कतिको ठूलो छ त्यसमा निर्भर गर्दछ र अधिकांश अवस्थामा उपयुक्त कम्प्युट पत्ता लगाउन गाह्रो हुन्छ। यस सेलले प्रयोगकर्तालाई उपयुक्त कम्प्युट छान्न मार्गनिर्देशन गर्छ।

> [!NOTE]
> तल सूचीबद्ध कम्प्युटहरू सबै भन्दा अनुकूलित कन्फिगरेसनमा काम गर्छन्। कन्फिगरेसनमा कुनै पनि परिवर्तनले Cuda Out Of Memory त्रुटि दिन सक्छ। यस्ता अवस्थामा, कम्प्युटलाई ठूलो आकारमा अपग्रेड गर्न प्रयास गर्नुहोस्।

> [!NOTE]
> तल कम्प्युट_cluster_size छान्दा तपाईंको स्रोत समूहमा कम्प्युट उपलब्ध छ कि छैन जाँच गर्नुहोस्। यदि कुनै कम्प्युट उपलब्ध छैन भने, कम्प्युट स्रोतहरूमा पहुँचको लागि अनुरोध गर्न सक्नुहुन्छ।

### फाइन ट्विन समर्थनको लागि मोडेल जाँच

1. यो Python स्क्रिप्टले Azure ML मोडेलसँग अन्तरक्रिया गर्छ। यसको विवरण:

    - ast मोड्युल आयात गरिन्छ, जुन Python को abstract syntax grammar को रूखहरू प्रक्रियाकरण गर्न प्रयोग हुन्छ।

    - foundation_model वस्तुमा finetune_compute_allow_list नामको ट्याग छ कि छैन भनी जाँच गर्छ। Azure ML मा ट्यागहरू key-value जोडी हुन् जसले मोडेलहरू फिल्टर र क्रमबद्ध गर्न मद्दत गर्छ।

    - यदि finetune_compute_allow_list ट्याग छ भने, ast.literal_eval प्रयोग गरी ट्यागको मान (स्ट्रिङ) सुरक्षित रूपमा Python सूचीमा रूपान्तर गरी computes_allow_list भेरिएबलमा राख्छ। त्यसपछि कम्प्युट लिस्टबाट कम्प्युट सिर्जना गर्ने सन्देश प्रिन्ट गर्छ।

    - ट्याग छैन भने computes_allow_list लाई None सेट गरी ट्याग मोडेलका ट्यागहरूमध्ये छैन भन्ने सन्देश देखाउँछ।

    - सारांशमा, यो स्क्रिप्ट मोडेल मेटाडेटामा विशेष ट्याग भनी जाँच गर्छ र त्यसको मानलाई सूचीमा रूपान्तर गरी प्रयोगकर्तालाई जानकारी दिन्छ।

    ```python
    # ast मोड्युल आयात गर्नुहोस्, जसले Python सारांश व्याकरणका रूखहरू प्रक्रिया गर्नका लागि फंक्शनहरू प्रदान गर्छ
    import ast
    
    # मोडेलका ट्यागहरूमा 'finetune_compute_allow_list' ट्याग छ कि छैन जाँच्नुहोस्
    if "finetune_compute_allow_list" in foundation_model.tags:
        # यदि ट्याग छ भने, ast.literal_eval प्रयोग गरी ट्यागको मान (एक स्ट्रिंग)लाई सुरक्षित रूपमा Python सूचीमा पार्स गर्नुहोस्
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # स्ट्रिंगलाई python सूचीमा परिणत गर्नुहोस्
        # सूचिबाट compute सिर्जना गर्नुपर्ने सन्देश प्रिन्ट गर्नुहोस्
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # यदि ट्याग छैन भने, computes_allow_list लाई None मा सेट गर्नुहोस्
        computes_allow_list = None
        # 'finetune_compute_allow_list' ट्याग मोडेलका ट्यागहरूको हिस्सा नभएको सन्देश प्रिन्ट गर्नुहोस्
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### कम्प्युट इन्स्ट्यान्स जाँच

1. यस Python स्क्रिप्टले Azure ML सेवा सँग कम्प्युट इन्स्ट्यान्स जाँच गर्दछ। कार्यहरू:

    - compute_cluster मा रहेको कम्प्युट इन्स्ट्यान्सको नामबाट Azure ML कार्यक्षेत्रबाट कम्प्युट इन्स्ट्यान्स प्राप्त गर्न प्रयास गर्छ। provisioning state "failed" भएमा ValueError उकास्छ।

    - computes_allow_list None नभएमा, सूचीका सबै कम्प्युट साइजहरूलाई lower case मा परिवर्तन गरी हालको कम्प्युट साइज सूचीमा छ कि छैन जाँच्छ। छैन भने ValueError उकास्छ।

    - computes_allow_list None भएमा कम्प्युट साइजलाई GPU VM size को असमर्थित सूचीमा जाँच्छ र पायेमा ValueError उकास्छ।

    - कार्यक्षेत्रमा उपलब्ध सम्पूर्ण कम्प्युट साइजहरूको सूची ल्याउँछ। प्रत्येक साइजमा लुटेर हालको कम्प्युट साइजसँग मेल खाए GPU को संख्या निकाल्छ र gpu_count_found True बनाउँछ।

    - gpu_count_found True भए GPU संख्या प्रिन्ट गर्छ, नभए ValueError उकास्छ।

    - सारांशमा, यो स्क्रिप्ट कम्प्युट इन्स्ट्यान्सको provisioning state, साइज अनुमति सूची वा अस्वीकार सूचीमा रहेको, र GPU संख्या जाँच गर्छ।

    ```python
    # अपवाद सन्देश प्रिन्ट गर्नुहोस्
    print(e)
    # यदि गणना आकार कार्यक्षेत्रमा उपलब्ध छैन भने ValueError उचाल्नुहोस्
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML कार्यक्षेत्रबाट गणना उदाहरण प्राप्त गर्नुहोस्
    compute = workspace_ml_client.compute.get(compute_cluster)
    # जाँच गर्नुहोस् कि गणना उदाहरणको provisioning अवस्था "失败" छ कि छैन
    if compute.provisioning_state.lower() == "failed":
        # provisioning अवस्था "失败" भएमा ValueError उचाल्नुहोस्
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # जाँच गर्नुहोस् कि computes_allow_list None होइन
    if computes_allow_list is not None:
        # computes_allow_list मा सबै गणना आकारहरूलाई सान्दर्भिक अक्षरमा परिणत गर्नुहोस्
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # जाँच गर्नुहोस् कि गणना उदाहरणको आकार computes_allow_list_lower_case मा छ कि छैन
        if compute.size.lower() not in computes_allow_list_lower_case:
            # यदि गणना उदाहरणको आकार computes_allow_list_lower_case मा छैन भने ValueError उचाल्नुहोस्
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # असमर्थित GPU VM आकारहरूको सूची परिभाषित गर्नुहोस्
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # जाँच गर्नुहोस् कि गणना उदाहरणको आकार unsupported_gpu_vm_list मा छ कि छैन
        if compute.size.lower() in unsupported_gpu_vm_list:
            # यदि गणना उदाहरणको आकार unsupported_gpu_vm_list मा छ भने ValueError उचाल्नुहोस्
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # गणना उदाहरणमा GPU को संख्या भेट्टाइएको छ कि छैन भनेर साँचो गर्नुको लागि झण्डा आरम्भ गर्नुहोस्
    gpu_count_found = False
    # कार्यक्षेत्रमा उपलब्ध सबै गणना आकारहरूको सूची प्राप्त गर्नुहोस्
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # उपलब्ध गणना आकारहरूको सूचीमाथि पुनरावृति गर्नुहोस्
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # जाँच गर्नुहोस् कि गणना आकारको नाम गणना उदाहरणको आकारसँग मेल खान्छ कि छैन
        if compute_sku.name.lower() == compute.size.lower():
            # यदि मेल खान्छ भने, त्यस गणना आकारका लागि GPU को संख्या प्राप्त गर्नुहोस् र gpu_count_found लाई साँचोमा सेट गर्नुहोस्
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # यदि gpu_count_found साँचो छ भने, गणना उदाहरणमा GPU को संख्या प्रिन्ट गर्नुहोस्
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # यदि gpu_count_found गलत छ भने ValueError उचाल्नुहोस्
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## ४. फाइन ट्विनको लागि डाटासेट छान्नुहोस्

1. हामी ultrachat_200k डाटासेट प्रयोग गर्छौं। यस डाटासेटमा चार स्प्लिटहरू छन् जुन सुपरवाइज्ड फाइन-ट्युनिङ (sft) लागि उपयुक्त छन्।
    जेनेरेसन र्याङ्किङ (gen)। प्रति स्प्लिट उदाहरणहरूको संख्या तल देखाइएको छ:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. आगामी केही सेलले फाइन ट्युनिङका लागि आधारभूत डाटा तयारी देखाउँछन्:

### केहि डेटा पंक्तिहरू दृश्यांकन गर्नुहोस्

यो नमुना छिटो चलोस भन्नका लागि train_sft, test_sft फाइलहरूमा पहिलेदेखि नै सानो अंश (५%) बचत गर्छौं। यसले फाइन ट्विन गरिएको मोडेलको सटीकता कम हुन्छ, त्यसैले यसलाई वास्तविक-जीवन प्रयोगमा नराख्नुपर्ने छ।
download-dataset.py स्क्रिप्ट प्रयोग गरी ultrachat_200k डाटासेट डाउनलोड र फाइनट्यून पाइपलाइन कम्पोनेन्टले उपभोग गर्न मिल्ने अवस्थामा परिणत गरिन्छ। डाटासेट ठूलो भएकाले हामीसँग यहाँ डाटासेटको केही भाग मात्र छ।

1. तलको स्क्रिप्टले डाटाको केवल ५% मात्र डाउनलोड गर्छ। dataset_split_pc प्यारामिटर परिवर्तन गरेर यो प्रतिशत बढाउन सकिन्छ।

> [!NOTE]
> कतिपय भाषा मोडेलमा भाषा कोड फरक हुन्छन् र यसैले डाटासेटको कालन नामहरू पनि सोही अनुसार हुनु पर्छ।

1. डेटा यस प्रकार देखिनु पर्छ
च्याट-सम्पूर्णता डाटासेट parquet ढाँचामा संग्रह गरिएको छ, प्रत्येक इंट्री निम्न स्कीमालाई प्रयोग गर्दछ:

    - यो JSON (JavaScript Object Notation) दस्तावेज हो, जुन लोकप्रिय डाटा अन्तरप्रेषण ढाँचा हो। यो कार्यान्वयनयोग्य कोड होइन, तर डाटा संग्रह र स्थानान्तरणको माध्यम हो। यसको संरचना यस प्रकार छ:

    - "prompt": यो कुञ्जीले स्ट्रिङ मान राख्छ जुन AI सहायकलाई सोधिएको कार्य वा प्रश्न हो।

    - "messages": यो कुञ्जीले वस्तुहरूको एरे हो। प्रत्येक वस्तुले प्रयोगकर्ता र AI सहायक बीचको संवादमा सन्देश प्रतिनिधित्व गर्छ। प्रत्येक सन्देश वस्तुमा दुई कुञ्जी हुन्छन्:

    - "content": सन्देशको सामग्री (स्ट्रिङ मान)।
    - "role": सन्देश पठाउने इकाईको भूमिका (स्ट्रिङ मान), जुन "user" वा "assistant" हुन सक्छ।
    - "prompt_id": विशिष्ट प्रॉम्प्टको अनौठो पहिचानकर्ता (स्ट्रिङ मान)।

1. यस विशेष JSON दस्तावेजमा, प्रयोगकर्ताले AI सहायकलाई एउटा डिस्टोपियन कथाका लागि नायक सिर्जना गर्न आग्रह गरेको संवाद छ। सहायकले जवाफ दिन्छ र प्रयोगकर्ता थप विवरण माग्छ। सहायकले थप विवरण दिने सहमति जनाउँछ। सम्पूर्ण संवाद एउटा विशिष्ट prompt id सँग सम्बन्धित छ।

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

### डेटा डाउनलोड गर्नुहोस्

1. यस Python स्क्रिप्टले download-dataset.py नामक सहायक स्क्रिप्ट चलाएर डाटासेट डाउनलोड गर्छ। यसका कार्यहरू:

    - os मोड्युल आयात गर्छ, जुन अपरेटिङ सिस्टम निर्भर कार्यहरू गर्न प्रयोग हुन्छ।

    - os.system प्रयोग गरेर shell मा download-dataset.py स्क्रिप्ट चलाउँछ, जसमा HuggingFaceH4/ultrachat_200k डाटासेट डाउनलोड गर्ने, ultrachat_200k_dataset डिरेक्टरीमा राख्ने, र डाटासेट ५% मात्र स्प्लिट गर्ने तर्कहरू छन्। os.system ले कमाण्डको exit स्थिति फर्काउँछ, जुन exit_status मा राखिन्छ।

    - exit_status 0 होइन भने, डाटासेट डाउनलोडमा त्रुटि भएको Exception उठाउँछ।

    - सारांशमा, यो स्क्रिप्ट सहायक स्क्रिप्ट प्रयोग गरी डाटासेट डाउनलोड गर्छ र त्रुटि भएमा जानकारी दिन्छ।

    ```python
    # अपरेटिङ सिस्टम निर्भर कार्यक्षमता प्रयोग गर्ने तरीका प्रदान गर्ने os मोड्युल आयात गर्नुहोस्
    import os
    
    # विशिष्ट कमाण्ड लाइन तर्कहरूसहित शेलमा download-dataset.py स्क्रिप्ट चलाउन os.system फंक्शन प्रयोग गर्नुहोस्
    # तर्कहरूले डाउनलोड गर्न dataset (HuggingFaceH4/ultrachat_200k), डाउनलोड गर्ने डिरेक्टरी (ultrachat_200k_dataset), र dataset विभाजन प्रतिशत (5) निर्दिष्ट गर्छन्
    # os.system फंक्शनले चलाएको आदेशको exit स्थिति फर्काउँछ; यो स्थिति exit_status भेरिएबलमा भण्डारण गरिन्छ
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # exit_status 0 होइन भने जाँच गर्नुहोस्
    # युनिक्स-जस्ता अपरेटिङ सिस्टमहरूमा, exit स्थिति 0 हुँदा प्रायः आदेश सफल भएको जनाउँछ, र अन्य कुनै पनि अंक त्रुटि जनाउँछ
    # यदि exit_status 0 होइन भने, dataset डाउनलोड गर्नमा त्रुटि भएको सङ्केत गर्दै Exception उठाउनुहोस्
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### डेटा DataFrame मा लोड गर्नुहोस्

1. यस Python स्क्रिप्टले JSON Lines फाइल pandas DataFrame मा लोड गरी पहिलो ५ पंक्ति देखाउँछ। यसका कार्यहरू:

    - pandas लाइब्रेरी आयात गर्छ, जसले डेटा हेरफेर र विश्लेषणमा मद्दत गर्दछ।

    - pandas को प्रदर्शन विकल्पमा स्तम्भको अधिकतम चौडाइ 0 सेट गर्छ, जसले प्रत्येक स्तम्भको पुरै पाठ truncation बिना प्रदर्शन गर्न अनुमति दिन्छ।
    - यसले pd.read_json फंक्शन प्रयोग गरेर ultrachat_200k_dataset डाइरेक्टरीबाट train_sft.jsonl फाइललाई DataFrame मा लोड गर्छ। lines=True आर्गुमेन्टले जनाउँछ कि फाइल JSON Lines ढाँचामा छ, जहाँ प्रत्येक लाइन अलग JSON वस्तु हुन्छ।

    - यसले head मेथड प्रयोग गरेर DataFrame का पहिलो 5 पङ्क्तिहरू देखाउँछ। यदि DataFrame मा 5 भन्दा कम पङ्क्तिहरू छन् भने, यसले सबै देखाउनेछ।

    - सारांशमा, यो स्क्रिप्टले JSON Lines फाइललाई DataFrame मा लोड गर्दैछ र पहिलो 5 पङ्क्तिहरू पूरा स्तम्भ पाठ सहित देखाउँदैछ।
    
    ```python
    # pandas पुस्तकालय आयात गर्नुहोस्, जुन एक शक्तिशाली डेटा हेरफेर र विश्लेषण पुस्तकालय हो
    import pandas as pd
    
    # pandas को प्रदर्शन विकल्पहरूमाथि अधिकतम स्तम्भ चौड़ाई 0 सेट गर्नुहोस्
    # यसको मतलब हो कि DataFrame मुद्रित गर्दा प्रत्येक स्तम्भको पूर्ण पाठ truncation बिना प्रदर्शन गरिनेछ
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json फंक्शन प्रयोग गरेर ultrachat_200k_dataset निर्देशिकाबाट train_sft.jsonl फाइललाई DataFrame मा लोड गर्नुहोस्
    # lines=True तर्कले सूचित गर्दछ कि फाइल JSON Lines ढाँचामा छ, जहाँ प्रत्येक लाइन अलग JSON वस्तु हो
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # head विधि प्रयोग गरेर DataFrame का पहिलो 5 पङ्क्तिहरू प्रदर्शन गर्नुहोस्
    # यदि DataFrame मा 5 भन्दा कम पङ्क्तिहरू छन् भने, ती सबै प्रदर्शन गरिनेछ
    df.head()
    ```

## 5. मोडेल र डाटा इनपुटहरू प्रयोग गरेर फ्रिनेट्यूनिङ काम बुझाउने

chat-completion पाइपलाइन कम्पोनेन्ट प्रयोग गर्ने काम सिर्जना गर्नुहोस्। फ्रिनेट्यूनिङका लागि समर्थित सबै प्यारामिटरहरूबारे थप जान्नुहोस्।

### फ्रिनेट्यून प्यारामिटरहरू परिभाषित गर्नुहोस्

१. फ्रिनेट्यून प्यारामिटरहरूलाई २ वर्गमा विभाजन गर्न सकिन्छ - प्रशिक्षण प्यारामिटरहरू, अप्टिमाइजेसन प्यारामिटरहरू

१. प्रशिक्षण प्यारामिटरहरूले प्रशिक्षण पक्षहरू परिभाषित गर्छन् जस्तै -

    - अप्टिमाइजर, शेड्युलर प्रयोग गर्ने
    - फ्रिनेट्यून सुधार गर्न मेट्रिक
    - प्रशिक्षण चरणहरूको संख्या र ब्याच साइज आदि
    - अप्टिमाइजेसन प्यारामिटरहरूले GPU मेमोरी अप्टिमाइज गराउन र कम्प्युट स्रोतहरू प्रभावकारी रूपमा प्रयोग गर्न मद्दत गर्छन्।

१. तलको केही प्यारामिटरहरू यस वर्गमा पर्छन्। अप्टिमाइजेसन प्यारामिटरहरू प्रत्येक मोडेलका लागि फरक हुन्छन् र यी भिन्नताहरूलाई सम्हाल्न मोडेलसँग प्याक गरिएको हुन्छ।

    - deepspeed र LoRA सक्षम पार्नुहोस्
    - मिश्रित प्रेसिजन प्रशिक्षण सक्षम गर्नुहोस्
    - बहु-नोड प्रशिक्षण सक्षम गर्नुहोस्

> [!NOTE]
> सुपरभाइज्ड फ्रिनेट्यूनिङले संरेखण गुमाउने वा विनाशकारी भूल हुन सक्छ। हामी यो समस्या जाँच गर्न र फ्रिनेट्यून पछि संरेखण चरण चलाउन सल्लाह दिन्छौं।

### फ्रिनेट्यूनिङ प्यारामिटरहरू

१. यो Python स्क्रिप्टले मेसिन लर्निङ मोडेलको फ्रिनेट्यूनिङ प्यारामिटरहरू सेट गर्दैछ। यसको विश्लेषण यस प्रकार छ:

    - यसले डिफल्ट प्रशिक्षण प्यारामिटरहरू सेट गर्छ जस्तै प्रशिक्षण इपोक्स संख्या, प्रशिक्षण र मूल्यांकनका लागि ब्याच साइजहरू, लर्निङ रेट, र लर्निङ रेट शेड्युलर प्रकार।

    - यसले डिफल्ट अप्टिमाइजेसन प्यारामिटरहरू सेट गर्छ जस्तै Layer-wise Relevance Propagation (LoRa) र DeepSpeed लागू गर्ने कि नगर्ने, र DeepSpeed चरण।

    - यसले प्रशिक्षण र अप्टिमाइजेसन प्यारामिटरहरूलाई एकै डिक्शनरी finetune_parameters मा समाहित गर्छ।

    - यसले जाँच गर्छ कि foundation_model सँग कुनै मोडेल-विशेष डिफल्ट प्यारामिटरहरू छन् कि छैनन्। भएमा, त्यसले चेतावनी सन्देश देखाउँछ र यी मोडेल-विशेष डिफल्टहरू finetune_parameters मा अपडेट गर्छ। ast.literal_eval फंक्शनले मोडेल-विशेष डिफल्टहरू स्ट्रिङबाट Python डिक्शनरीमा परिणत गर्न प्रयोग हुन्छ।

    - यसले अन्तिम फ्रिनेट्यूनिङ प्यारामिटरहरू प्रिन्ट गर्छ जुन रनमा प्रयोग हुनेछन्।

    - सारांशमा, यो स्क्रिप्टले मेसिन लर्निङ मोडेलको फ्रिनेट्यूनिङ प्यारामिटरहरू सेट र प्रदर्शन गर्दैछ, जसले मोडेल-विशेष डिफल्टहरू प्रयोग गर्न सक्ने सुविधा दिन्छ।

    ```python
    # प्रशिक्षण समयावधि, प्रशिक्षण र मूल्याङ्कनको लागि ब्याच साइजहरू, सिकाइ दर, र सिकाइ दर शेड्युलर प्रकार जस्ता पूर्वनिर्धारित प्रशिक्षण प्यारामिटरहरू सेट गर्नुहोस्
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # लेयर-वार सम्बन्ध प्रोपगेशन (LoRa) र DeepSpeed लागू गर्ने हो कि होइन, र DeepSpeed चरण जस्ता पूर्वनिर्धारित अनुकूलन प्यारामिटरहरू सेट गर्नुहोस्
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # प्रशिक्षण र अनुकूलन प्यारामिटरहरूलाई finetune_parameters भनिने एकल शब्दकोशमा संयोजन गर्नुहोस्
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # आधारभूत मोडेलसँग कुनै मोडेल-विशिष्ट पूर्वनिर्धारित प्यारामिटरहरू छन् कि छैनन् जाँच गर्नुहोस्
    # भएमा, चेतावनी सन्देश प्रिन्ट गर्नुहोस् र यी मोडेल-विशिष्ट पूर्वनिर्धारितहरूसित finetune_parameters शब्दकोश अपडेट गर्नुहोस्
    # ast.literal_eval फंक्शन मोडेल-विशिष्ट पूर्वनिर्धारितहरू स्ट्रिङबाट Python शब्दकोशमा रूपान्तरण गर्न प्रयोग गरिन्छ
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # स्ट्रिङलाई python dict मा रूपान्तरण गर्नुहोस्
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # रनका लागि प्रयोग गरिने अन्तिम फाइन-ट्यूनिङ प्यारामिटरहरूको सेट प्रिन्ट गर्नुहोस्
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### प्रशिक्षण पाइपलाइन

१. यो Python स्क्रिप्टले मेसिन लर्निङ प्रशिक्षण पाइपलाइनको डिस्प्ले नाम उत्पन्न गर्ने फंक्शन परिभाषित गर्छ र त्यसपछिको नाम उत्पन्न गरेर प्रिन्ट गर्छ। यसको विश्लेषण यस प्रकार छ:

१. get_pipeline_display_name function परिभाषित गरिएको छ। यो फंक्शनले प्रशिक्षण पाइपलाइनसँग सम्बन्धित विभिन्न प्यारामिटरहरूका आधारमा डिस्प्ले नाम उत्पन्न गर्छ।

१. फंक्शन भित्र, कुल ब्याच साइज गणना गरिन्छ जसमा प्रति-डिभाइस ब्याच साइज, ग्रेडियन्ट एक्युम्युलेशन चरण संख्या, प्रति नोड GPUs संख्या, र फ्रिनेट्यूनिङका लागि प्रयोग हुने नोडहरूको संख्या समावेश हुन्छ।

१. यसले अन्य विभिन्न प्यारामिटरहरू प्राप्त गर्छ जस्तै लर्निङ रेट शेड्युलर प्रकार, DeepSpeed लागू छ कि छैन, DeepSpeed चरण, Layer-wise Relevance Propagation (LoRa) लागू छ कि छैन, राख्नुपर्ने मोडेल चेकप्वाइंटहरूको सीमा, र अधिकतम अनुक्रम लामोई।

१. यसले यी सबै प्यारामिटरहरूलाई हाइफनले छुट्टिएका स्ट्रिङको रूपमा बनाउँछ। यदि DeepSpeed वा LoRa लागू छ भने, स्ट्रिङमा क्रमशः "ds"सहित DeepSpeed चरण वा "lora" समावेश हुन्छ। नत्र त्यसमा "nods" वा "nolora" समावेश हुन्छ।

१. फंक्शनले यो स्ट्रिङ फर्काउँछ, जुन प्रशिक्षण पाइपलाइनको डिस्प्ले नामको रूपमा काम गर्छ।

१. फंक्शन परिभाषित भएपछि, यसलाई कल गरेर डिस्प्ले नाम उत्पन्न गरी प्रिन्ट गरिन्छ।

१. सारांशमा, यो स्क्रिप्टले मेसिन लर्निङ प्रशिक्षण पाइपलाइनको विभिन्न प्यारामिटरहरूका आधारमा डिस्प्ले नाम जनाउँछ र त्यसलाई प्रिन्ट गर्छ।

    ```python
    # तालिम पाइपलाइनको लागि प्रदर्शन नाम उत्पादन गर्नको लागि एउटा फंक्शन परिभाषित गर्नुहोस्
    def get_pipeline_display_name():
        # प्रति-यन्त्र ब्याच साइज, ग्रेडियेन्ट सङ्कलन चरणहरूको संख्या, प्रति नोड GPUहरूको संख्या, र फाइन-टेर्निङको लागि प्रयोग गरिएका नोडहरूको संख्या गुणा गरेर कुल ब्याच साइज गणना गर्नुहोस्
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # सिक्ने दर अनुसूचक प्रकार प्राप्त गर्नुहोस्
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # DeepSpeed प्रयोग भइरहेको छ कि छैन प्राप्त गर्नुहोस्
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # DeepSpeed चरण प्राप्त गर्नुहोस्
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # यदि DeepSpeed प्रयोग भइरहेको छ भने, प्रदर्शन नाममा DeepSpeed चरणसँग "ds" समावेश गर्नुहोस्; नभएमा "nods" समावेश गर्नुहोस्
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Layer-wise Relevance Propagation (LoRa) प्रयोग भइरहेको छ कि छैन प्राप्त गर्नुहोस्
        lora = finetune_parameters.get("apply_lora", "false")
        # यदि LoRa प्रयोग भइरहेको छ भने, प्रदर्शन नाममा "lora" समावेश गर्नुहोस्; नभएमा "nolora" समावेश गर्नुहोस्
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # राख्नुपर्ने मोडल चेकपोइन्टहरूको संख्या सीमा प्राप्त गर्नुहोस्
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # अधिकतम अनुक्रम लम्बाइ प्राप्त गर्नुहोस्
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # सबै यी प्यारामिटरहरूलाई हाइफेनले छुट्याएर जोडेर प्रदर्शन नाम बनाउनुहोस्
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
    
    # प्रदर्शन नाम उत्पादन गर्न फंक्शन कल गर्नुहोस्
    pipeline_display_name = get_pipeline_display_name()
    # प्रदर्शन नाम छाप्नुहोस्
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### पाइपलाइन कन्फिगर गर्दै

यो Python स्क्रिप्टले Azure Machine Learning SDK प्रयोग गरी मेसिन लर्निङ पाइपलाइन परिभाषित र कन्फिगर गर्दैछ। यसको विश्लेषण यस प्रकार छ:

१. Azure AI ML SDK बाट आवश्यक मोड्युलहरू इम्पोर्ट गर्दैछ।

१. "chat_completion_pipeline" नामक पाइपलाइन कम्पोनेन्ट रजिट्रीबाट ल्याउँदैछ।

१. `@pipeline` डेकोरेटर र `create_pipeline` फंक्शन प्रयोग गरेर पाइपलाइन काम परिभाषित गर्दैछ। पाइपलाइनको नाम `pipeline_display_name` सेट गरिएको छ।

१. `create_pipeline` फंक्शन भित्र, ल्याइएको पाइपलाइन कम्पोनेन्टलाई विभिन्न प्यारामिटरहरूका साथ इनिशियलाइज गर्दैछ, जसमध्ये मोडेल पथ, फरक चरणका कम्प्युट क्लस्टरहरू, प्रशिक्षण र परीक्षणका लागि डाटासेट स्प्लिटहरू, फ्रिनेट्यूनिङको लागि GPUs संख्या, र अन्य फ्रिनेट्यूनिङ प्यारामिटरहरू छन्।

१. फ्रिनेट्यूनिङ कामको आउटपुटलाई पाइपलाइन कामको आउटपुटसँग म्याप गर्दैछ। यसले फ्रिनेट्यून गरिएको मोडेल सजिलै रजिष्टर गर्न मद्दत गर्छ, जुन मोडेललाई अनलाइन वा ब्याच एण्डपोइन्टमा डिप्लोय गर्न आवश्यक हुन्छ।

१. `create_pipeline` फंक्शन कल गरेर पाइपलाइनको एक उदाहरण बनाउँदैछ।

१. पाइपलाइनको `force_rerun` सेटिङ True मा राखेको छ, जसको अर्थ अघिल्ला कामका क्यासेड नतिजाहरू प्रयोग नहुनेछन्।

१. पाइपलाइनको `continue_on_step_failure` सेटिङ False मा राखेको छ, जसको अर्थ कुनै पनि चरण असफल भए फस्टाउनेछ।

१. सारांशमा, यो स्क्रिप्टले Azure Machine Learning SDK प्रयोग गरी च्याट कम्प्लिशन कार्यका लागि मेसिन लर्निङ पाइपलाइन परिभाषित र कन्फिगर गर्दैछ।

    ```python
    # Azure AI ML SDK बाट आवश्यक मोड्युलहरू आयात गर्नुहोस्
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # रजिष्ट्रिमा रहेको "chat_completion_pipeline" नामक पाइपलाइन कम्पोनेन्ट ल्याउनुहोस्
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline डेकोरेटर र create_pipeline फंक्शन प्रयोग गरी पाइपलाइन जागिर परिभाषित गर्नुहोस्
    # पाइपलाइनको नाम pipeline_display_name मा सेट गरिएको छ
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # ल्याइएको पाइपलाइन कम्पोनेन्टलाई विभिन्न प्यारामिटरहरूसहित आरम्भ गर्नुहोस्
        # यसमा मोडेल पथ, विभिन्न चरणहरूको लागि कम्प्युट क्लस्टरहरू, प्रशिक्षण र परीक्षणका लागि डाटासेट विभाजनहरू, फाइन-ट्युनिङका लागि GPU को संख्या, र अन्य फाइन-ट्युनिङ प्यारामिटरहरू समावेश छन्
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # डाटासेट विभाजनहरूलाई प्यारामिटरमा मिलाउनुहोस्
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # प्रशिक्षण सेटिङहरू
            number_of_gpu_to_use_finetuning=gpus_per_node,  # कम्प्युटमा उपलब्ध GPU को सङ्ख्यामा सेट गर्नुहोस्
            **finetune_parameters
        )
        return {
            # फाइन ट्युनिङ जागिरको आउटपुटलाई पाइपलाइन जागिरको आउटपुटसँग मिलाउनुहोस्
            # यसो गर्दा हामी सजिलै फाइन ट्युन गरिएको मोडेल दर्ता गर्न सक्छौं
            # मोडेललाई अनलाइन वा ब्याच अन्तबिन्दुमा तैनाथ गर्न मोडेल दर्ता गर्नु आवश्यक छ
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline फंक्शन बोलाएर पाइपलाइनको एक उदाहरण बनाउनुहोस्
    pipeline_object = create_pipeline()
    
    # अघिल्ला जागिरहरूका क्याच गरिएको नतिजाहरू प्रयोग नगर्नुहोस्
    pipeline_object.settings.force_rerun = True
    
    # चरण विफल भएमा जारी राख्ने सेटिङ False मा राख्नुहोस्
    # यसको मतलब यदि कुनै पनि चरण असफल भयो भने पाइपलाइन रोकिनेछ
    pipeline_object.settings.continue_on_step_failure = False
    ```

### काम बुझाउने

१. यो Python स्क्रिप्टले Azure Machine Learning वर्कस्पेसमा मेसिन लर्निङ पाइपलाइन काम बुझाउँदैछ र त्यसपछि काम सम्पन्न हुने कुराको प्रतीक्षा गर्दैछ। यसको विश्लेषण यस प्रकार छ:

    - यसले workspace_ml_client मा jobs वस्तुको create_or_update मेथड कल गरी पाइपलाइन काम बुझाउँछ। चलाउनुपर्ने पाइपलाइन pipeline_object द्वारा निर्दिष्ट हुन्छ, र कामको अन्तर्गत प्रयोग हुने प्रयोग प्रयोग experiment_name द्वारा जनाइन्छ।

    - पछि, यसले workspace_ml_client मा jobs वस्तुको stream मेथड कल गरी पाइपलाइन काम समाप्त हुने प्रतीक्षा गर्छ। प्रतीक्षा गर्नुपर्ने कामको नाम pipeline_job वस्तुको name एट्रिब्युटबाट लिइन्छ।

    - सारांशमा, यो स्क्रिप्टले Azure Machine Learning वर्कस्पेसमा मेसिन लर्निङ पाइपलाइन काम बुझाउँछ र काम सम्पन्न हुने प्रतीक्षा गर्छ।

    ```python
    # Azure Machine Learning कार्यक्षेत्रमा पाइपलाइन कार्य पेश गर्नुहोस्
    # चलाउनको लागि पाइपलाइन pipeline_object द्वारा निर्दिष्ट गरिएको छ
    # यस अन्तर्गत चलाइएको प्रयोग experiment_name द्वारा निर्दिष्ट गरिएको छ
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # पाइपलाइन कार्य पूरा हुन पर्खनुहोस्
    # पर्खनुपर्ने कार्य pipeline_job वस्तुको name विशेषता द्वारा निर्दिष्ट गरिएको छ
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. फ्रिनेट्यून गरिएको मोडेल वर्कस्पेसमा दर्ता गर्ने

हामी फ्रिनेट्यूनिङ कामको आउटपुटबाट मोडेल दर्ता गर्नेछौं। यसले फ्रिनेट्यून गरिएको मोडेल र फ्रिनेट्यूनिङ काम बीच रेखाङ्कन ट्रयाक गर्छ। फ्रिनेट्यूनिङ कामले थपfoundation model, डाटा र प्रशिक्षण कोडसँग रेखाङ्कन ट्रयाक गर्छ।

### ML मोडेल दर्ता गर्दै

१. यो Python स्क्रिप्टले Azure Machine Learning पाइपलाइनमा तालिम दिइएको मेसिन लर्निङ मोडेल दर्ता गर्दैछ। यसको विश्लेषण यस प्रकार छ:

    - Azure AI ML SDK बाट आवश्यक मोड्युलहरू इम्पोर्ट गर्छ।

    - pipeline कामबाट trained_model आउटपुट उपलब्ध छ कि छैन भनेर workspace_ml_client को jobs वस्तुको get मेथड कल गरी र त्यसको outputs एट्रिब्युटमा पहुँच गर्दै जाँच्छ।

    - पाइपलाइन कामको नाम र आउटपुट नाम ("trained_model") प्रयोग गरी तालिम दिइएको मोडेलको पथ निर्माण गर्छ।

    - फ्रिनेट्यून गरिएको मोडेलको नामको लागि "-ultrachat-200k" जोडेर र स्ल्यासहरूलाई हाइफनमा परिवर्तन गरी नाम परिभाषित गर्छ।

    - Model वस्तु सिर्जना गरेर मोडेल दर्ता गर्न तयारी गर्छ, जसले मोडेलको पथ, मोडेल प्रकार (MLflow मोडेल), मोडेलको नाम र संस्करण, र मोडेलको विवरण समावेश गर्छ।

    - workspace_ml_client मा models वस्तुको create_or_update मेथड कल गरी Model वस्तु पास गरेर मोडेल दर्ता गर्छ।

    - दर्ता गरिएको मोडेल प्रिन्ट गर्छ।

१. सारांशमा, यो स्क्रिप्ट Azure Machine Learning पाइपलाइनमा तालिम दिएको मेसिन लर्निङ मोडेल दर्ता गर्दैछ।
    
    ```python
    # Azure AI ML SDK बाट आवश्यक मोड्युलहरू आयात गर्नुहोस्
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # पाइपलाइन कामबाट `trained_model` आउटपुट उपलब्ध छ कि छैन जाँच्नुहोस्
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # पाइपलाइन कामको नाम र आउटपुटको नाम ("trained_model") प्रयोग गरेर स्ट्रिङ स्वरूपमा तालिम प्राप्त मोडेलको मार्ग निर्माण गर्नुहोस्
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # मौलिक मोडेल नाममा "-ultrachat-200k" जोडेर र कुनै पनि स्ल्यासलाई हाइफनले प्रतिस्थापन गरेर फाइन-ट्यून गरिएको मोडेलको नाम परिभाषित गर्नुहोस्
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # विभिन्न पेरामिटरहरूसँग Model वस्तु सिर्जना गरेर मोडेल दर्ता गर्न तयारी गर्नुहोस्
    # यसमा मोडेल मार्ग, मोडेल प्रकार (MLflow मोडेल), मोडेलको नाम र संस्करण, र मोडेलको विवरण समावेश छन्
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # संस्करण द्वन्द्वरबाट बच्न टाइमस्ट्याम्पलाई संस्करणको रूपमा प्रयोग गर्नुहोस्
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Model वस्तु लाई आर्गुमेन्टको रूपमा लिएर workspace_ml_client को models वस्तुको create_or_update मेथड कल गरेर मोडेल दर्ता गर्नुहोस्
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # दर्ता गरिएको मोडेललाई प्रिन्ट गर्नुहोस्
    print("registered model: \n", registered_model)
    ```

## 7. फ्रिनेट्यून गरिएको मोडेललाई अनलाइन एन्डपोइन्टमा डिप्लोय गर्ने

अनलाइन एन्डपोइन्टहरूले दिर्घकालीन REST API दिन्छन् जसलाई मोडेल प्रयोग गर्न आवश्यक एप्लिकेसनहरूसँग एकीकृत गर्न सकिन्छ।

### एन्डपोइन्ट व्यवस्थापन

१. यो Python स्क्रिप्टले Azure Machine Learning मा दर्ता गरिएको मोडेलका लागि व्यवस्थापन अनलाइन एन्डपोइन्ट सिर्जना गर्दैछ। यसको विश्लेषण यस प्रकार छ:

    - Azure AI ML SDK बाट आवश्यक मोड्युलहरू इम्पोर्ट गर्छ।

    - अनलाइन एन्डपोइन्टको लागि अद्वितीय नाम परिभाषित गर्छ, जुन "ultrachat-completion-" स्ट्रिङमा टाइमस्ट्याम्प जोडेर बनाइएको छ।

    - ManagedOnlineEndpoint वस्तु सिर्जना गरी अनलाइन एन्डपोइन्ट निर्माणको तयारी गर्छ, जसमा एन्डपोइन्टको नाम, विवरण, र प्रमाणीकरण मोड ("key") समावेश हुन्छ।

    - workspace_ml_client को begin_create_or_update मेथड कल गरी ManagedOnlineEndpoint वस्तु पास गरेर अनलाइन एन्डपोइन्ट सिर्जना गर्छ। त्यसपछि wait मेथड कल गरेर सिर्जना प्रक्रिया पूरा हुन प्रतीक्षा गर्छ।

१. सारांशमा, यो स्क्रिप्ट Azure Machine Learning मा दर्ता गरिएको मोडेलका लागि व्यवस्थापन अनलाइन एन्डपोइन्ट सिर्जना गर्दैछ।

    ```python
    # Azure AI ML SDK बाट आवश्यक मोड्युलहरू आयात गर्नुहोस्
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" स्ट्रिङसँग टाइमस्ट्याम्प जोडेर अनलाइन इन्डपोइन्टको अनौठो नाम परिभाषित गर्नुहोस्
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # विभिन्न प्यारामिटरहरूसँग ManagedOnlineEndpoint वस्तु सिर्जना गरेर अनलाइन इन्डपोइन्ट बनाउन तयार हुनुहोस्
    # यसमा इन्डपोइन्टको नाम, इन्डपोइन्टको विवरण, र प्रमाणीकरण मोड ("key") समावेश छन्
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint वस्तुलाई आर्गुमेन्टका रूपमा राख्दै workspace_ml_client को begin_create_or_update मेथड कल गरेर अनलाइन इन्डपोइन्ट सिर्जना गर्नुहोस्
    # त्यसपछि wait मेथड कल गरेर सिर्जना अपरेशन पूरा हुन पर्खनुहोस्
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> तपाईंले यहाँ डिप्लोयमेन्टका लागि समर्थित SKUहरूको सूची पाउन सक्नुहुन्छ - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML मोडेल डिप्लोयमेन्ट

१. यो Python स्क्रिप्टले Azure Machine Learning मा दर्ता गरिएको मेसिन लर्निङ मोडेल व्यवस्थापन अनलाइन एन्डपोइन्टमा डिप्लोय गरिरहेको छ। यसको विश्लेषण यस प्रकार छ:

    - यसले ast मोड्युल इम्पोर्ट गर्छ, जुन Python को abstract syntax grammar को रूखहरू प्रशोधन गर्न फंक्शनहरू प्रदान गर्छ।

    - डिप्लोयमेन्टको लागि इन्स्ट्यान्स प्रकार "Standard_NC6s_v3" सेट गर्छ।

    - foundation model मा inference_compute_allow_list ट्याग छ कि छैन जाँच्छ। भएमा, यसले ट्याग मानलाई स्ट्रिङबाट Python सूचीमा रूपान्तरण गरी inference_computes_allow_list मा राख्छ। नभए, यसलाई None सेट गर्छ।

    - निर्दिष्ट इन्स्ट्यान्स प्रकार allow list मा छ कि छैन जाँच्छ। नभए, प्रयोगकर्तालाई allow list बाट एउटा इन्स्ट्यान्स प्रकार चयन गर्न सन्देश प्रिन्ट गर्छ।

    - ManagedOnlineDeployment वस्तु सिर्जना गरी डिप्लोयमेन्ट बनाउने तयारी गर्छ, जसमा डिप्लोयमेन्टको नाम, एन्डपोइन्टको नाम, मोडेलको ID, इन्स्ट्यान्स प्रकार र संख्या, लाईभनेस प्रोब सेटिङहरू र अनुरोध सेटिङहरू समावेश छन्।

    - workspace_ml_client को begin_create_or_update मेथड कल गरी ManagedOnlineDeployment वस्तु पास गरेर डिप्लोयमेन्ट सिर्जना गर्छ। त्यसपछि wait मेथड कल गरी सिर्जना प्रक्रिया पूरा हुन प्रतीक्षा गर्छ।

    - एन्डपोइन्टको ट्राफिक "demo" डिप्लोयमेन्टमा १००% डाइरेक्ट गर्छ।

    - workspace_ml_client को begin_create_or_update मेथड कल गरी अपडेट गरिएको एन्डपोइन्ट पास गरेर एन्डपोइन्ट अपडेट गर्छ। त्यसपछि result मेथड कल गरी अपडेट प्रक्रिया पूरा हुन्छ भनेर पर्खन्छ।

१. सारांशमा, यो स्क्रिप्ट Azure Machine Learning मा दर्ता गरिएको मेसिन लर्निङ मोडेल व्यवस्थापन अनलाइन एन्डपोइन्टमा डिप्लोय गर्दैछ।

    ```python
    # Python सार ग्र्यामरका रूखहरू प्रक्रिया गर्नको लागि कार्यसम्पादनहरू प्रदान गर्ने ast मोड्युल आयात गर्नुहोस्
    import ast
    
    # तैनातीको लागि उदाहरण प्रकार सेट गर्नुहोस्
    instance_type = "Standard_NC6s_v3"
    
    # आधार मोडेलमा `inference_compute_allow_list` ट्याग छ कि छैन जाँच गर्नुहोस्
    if "inference_compute_allow_list" in foundation_model.tags:
        # यदि छ भने, ट्याग मानलाई स्ट्रिङबाट Python सूचीमा रूपान्तरण गरी `inference_computes_allow_list` मा असाइन गर्नुहोस्
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # यदि छैन भने, `inference_computes_allow_list` लाई `None` मा सेट गर्नुहोस्
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # निर्दिष्ट गरिएको उदाहरण प्रकार अनुमति सूचीमा छ कि छैन जाँच गर्नुहोस्
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # विभिन्न प्यारामिटरहरूसँग `ManagedOnlineDeployment` वस्तु सिर्जना गरेर तैनाती तयार गर्नुहोस्
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `ManagedOnlineDeployment` वस्तु लाई तर्कको रूपमा लिएर `workspace_ml_client` को `begin_create_or_update` विधि बोलाएर तैनाती सिर्जना गर्नुहोस्
    # त्यसपछि `wait` विधि बोलाएर सिर्जना अपरेशन पूरा हुन कुर्नुहोस्
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # अन्तबिन्दुको ट्राफिकलाई "demo" तैनातीमा १००% ट्राफिक निर्देशन गर्न सेट गर्नुहोस्
    endpoint.traffic = {"demo": 100}
    
    # `endpoint` वस्तु लाई तर्कको रूपमा लिएर `workspace_ml_client` को `begin_create_or_update` विधि बोलाएर अन्तबिन्दु अपडेट गर्नुहोस्
    # त्यसपछि `result` विधि बोलाएर अपडेट अपरेशन पूरा हुन कुर्नुहोस्
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## ८. नमुना डाटासँग एन्डपोइन्ट परीक्षण गर्ने

हामी परीक्षण डाटासेटबाट केही नमुना डेटा ल्याउनेछौं र अनलाइन एन्डपोइन्टमा इन्फरन्सका लागि बुझाउनेछौं। त्यसपछि हामी स्कोर गरिएका लेबेलहरू र वास्तविक लेबेलहरू सँगै देखाउनेछौं।

### नतिजा पढ्दै

१. यो Python स्क्रिप्टले JSON Lines फाइललाई pandas DataFrame मा पढ्दैछ, एक यादृच्छिक नमुना लिइरहेको छ, र इन्डेक्स रिसेट गर्दैछ। यसको विश्लेषण यस प्रकार छ:

    - यसले ./ultrachat_200k_dataset/test_gen.jsonl फाइललाई pandas DataFrame मा पढ्छ। read_json फंक्शन lines=True आर्गुमेन्टसँग प्रयोग गरिएको छ किनभने फाइल JSON Lines ढाँचामा छ, जहाँ प्रत्येक लाइन अलग JSON वस्तु हो।

    - यसले DataFrame बाट यादृच्छिक रूपमा १ पङ्क्ति छनोट गर्छ। sample फंक्शन n=1 आर्गुमेन्टसँग प्रयोग गरिएको छ जुन चयन गर्नुपर्ने यादृच्छिक पङ्क्तिहरूको संख्या जनाउँछ।

    - यसले DataFrame को इन्डेक्स रिसेट गर्छ। reset_index फंक्शन drop=True आर्गुमेन्टसँग प्रयोग गरिएको छ जसले पुरानो इन्डेक्स हटाएर नयाँ डिफल्ट पूर्णाङ्क इन्डेक्स राख्छ।

    - यसले head फंक्शन २ आर्गुमेन्टसहित प्रयोग गरी DataFrame का पहिलो २ पङ्क्तिहरू देखाउँछ। तर, प्याचमा एक मात्रै पङ्क्ति छ त्यसैले एकै पङ्क्ति देखाउनेछ।

१. सारांशमा, यो स्क्रिप्टले JSON Lines फाइललाई pandas DataFrame मा पढ्ने, १ पङ्क्ति यादृच्छिक नमुना लिने, इन्डेक्स रिसेट गर्ने, र पहिलो पङ्क्ति देखाउने काम गर्छ।
    
    ```python
    # pandas पुस्तकालय आयात गर्नुहोस्
    import pandas as pd
    
    # JSON लाइन्स फाइल './ultrachat_200k_dataset/test_gen.jsonl' लाई pandas DataFrame मा पढ्नुहोस्
    # 'lines=True' argumento ले सूचित गर्छ कि फाइल JSON लाइन्स ढाँचामा छ, जहाँ प्रत्येक लाइन एउटा पृथक JSON वस्तु हो
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame बाट 1 पङ्क्तिको यादृच्छिक नमूना लिनुहोस्
    # 'n=1' argumento ले चयन गर्ने यादृच्छिक पङ्क्तिहरूको संख्या निर्दिष्ट गर्छ
    test_df = test_df.sample(n=1)
    
    # DataFrame को सूचकांक रिसेट गर्नुहोस्
    # 'drop=True' argumento ले सूचित गर्छ कि मौलिक सूचकांक हटाएर डिफल्ट पूर्णांक मानहरूको नयाँ सूचकांकले प्रतिस्थापन गर्नुपर्छ
    # 'inplace=True' argumento ले सूचित गर्छ कि DataFrame लाई सिधै संशोधित गर्नुपर्छ (नयाँ वस्तु सिर्जना नगरी)
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame को पहिलो 2 पङ्क्तिहरू देखाउनुहोस्
    # यद्यपि, नमूना लिँदा DataFrame मा केवल एउटा पङ्क्ति मात्र हुन्छ, त्यसैले यसले त्यो एक पङ्क्ति मात्र देखाउनेछ
    test_df.head(2)
    ```

### JSON वस्तु सिर्जना गर्ने

१. यो Python स्क्रिप्टले विशिष्ट प्यारामिटरहरू सहित JSON वस्तु सिर्जना गरी फाइलमा बचत गर्दैछ। यसको विश्लेषण यस प्रकार छ:

    - json मोड्युल इम्पोर्ट गर्दैछ, जुन JSON डाटासँग काम गर्नका लागि फंक्शनहरू प्रदान गर्छ।
    - यसले मेशिन लर्निङ मोडेलको लागि प्यारामिटरहरू जनाउने कुञ्जी र मानहरूसहित parameters नामक एक डिक्सनरी सिर्जना गर्दछ। कुञ्जीहरू "temperature", "top_p", "do_sample", र "max_new_tokens" हुन्, र तिनीहरूको सम्बन्धित मानहरू क्रमशः ०.६, ०.९, सत्य, र २०० हुन्।

    - यसले अर्को डिक्सनरी test_json सिर्जना गर्दछ जसमा दुई कुञ्जीहरू छन्: "input_data" र "params"। "input_data" को मान अर्को डिक्सनरी हो जसमा कुञ्जीहरू "input_string" र "parameters" छन्। "input_string" को मान test_df डाटाफ्रेमको पहिलो सन्देश समावेश गरेको सूची हो। "parameters" को मान पहिल्यै सिर्जना गरिएको parameters डिक्सनरी हो। "params" को मान खाली डिक्सनरी हो।

    - यसले sample_score.json नामक फाइल खोल्दछ।
    
    ```python
    # JSON डाटा सँग काम गर्नका लागि सुविधा प्रदान गर्ने json मोड्युल आयात गर्नुहोस्
    import json
    
    # मेशिन लर्निंग मोडेलका लागि प्यारामिटरहरू प्रतिनिधित्व गर्ने कुञ्जी र मानहरू सहितको `parameters` शब्दकोश बनाउनुस्
    # कुञ्जीहरू "temperature", "top_p", "do_sample", र "max_new_tokens" हुन्, र तिनीहरूको सम्बन्धित मानहरू क्रमशः 0.6, 0.9, True, र 200 छन्
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # "input_data" र "params" दुई कुञ्जीहरू भएको अर्को शब्दकोश `test_json` सिर्जना गर्नुहोस्
    # "input_data" को मान अर्को शब्दकोश हो जसमा "input_string" र "parameters" कुञ्जीहरू छन्
    # "input_string" को मान `test_df` डाटाफ्रेमबाट पहिलो सन्देश समावेश गर्ने सूची हो
    # "parameters" को मान पहिला सिर्जना गरिएको `parameters` शब्दकोश हो
    # "params" को मान खाली शब्दकोश हो
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` निर्देशिका भित्र `sample_score.json` नामको फाइल लेख्ने मोडमा खोल्नुहोस्
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` फङ्सन प्रयोग गरी JSON ढाँचामा `test_json` शब्दकोश फाइलमा लेख्नुहोस्
        json.dump(test_json, f)
    ```

### अन्त बिन्दु कल गर्ने तरिका

1. यो Python स्क्रिप्टले Azure Machine Learning मा अनलाइन अन्त बिन्दु कल गरेर JSON फाइल स्कोर गर्दछ। यसको विवरण यस प्रकार छ:

    - यसले workspace_ml_client वस्तुको online_endpoints को invoke विधि कल गर्दछ। यो विधि अनलाइन अन्त बिन्दुमा अनुरोध पठाउन र प्रतिक्रिया प्राप्त गर्न प्रयोग गरिन्छ।

    - यसले अन्त बिन्दुको नाम र डिप्लोयमेन्टको नाम endpoint_name र deployment_name तर्कहरूसँग निर्दिष्ट गर्दछ। यस अवस्थामा, अन्त बिन्दुको नाम online_endpoint_name चरमा भण्डारण गरिएको छ र डिप्लोयमेन्टको नाम "demo" हो।

    - यसले स्कोर गर्नुपर्ने JSON फाइलको पथ request_file तर्कमार्फत निर्दिष्ट गर्दछ। यस अवस्थामा, फाईल ./ultrachat_200k_dataset/sample_score.json हो।

    - यसले अन्त बिन्दुद्वारा फर्काइएका प्रतिक्रिया response चरमा भण्डारण गर्दछ।

    - यसले कच्चा प्रतिक्रिया मुद्रण गर्दछ।

1. सारांशमा, यो स्क्रिप्ट Azure Machine Learning मा अनलाइन अन्त बिन्दु कल गरेर JSON फाइल स्कोर गर्दछ र प्रतिक्रिया मुद्रण गर्दछ।

    ```python
    # Azure Machine Learning मा अनलाइन एन्डपोइन्टलाई `sample_score.json` फाइल स्कोर गर्न कल गर्नुहोस्
    # `workspace_ml_client` वस्तुको `online_endpoints` सम्पत्तिको `invoke` विधि अनलाइन एन्डपोइन्टमा अनुरोध पठाउन र प्रतिक्रिया प्राप्त गर्न प्रयोग गरिन्छ
    # `endpoint_name` तर्कले एन्डपोइन्टको नाम निर्दिष्ट गर्दछ, जुन `online_endpoint_name` भेरिएबलमा भण्डारण गरिएको छ
    # `deployment_name` तर्कले तैनातीको नाम निर्दिष्ट गर्दछ, जुन "demo" हो
    # `request_file` तर्कले स्कोर गर्नुपर्ने JSON फाइलको पथ निर्दिष्ट गर्दछ, जुन `./ultrachat_200k_dataset/sample_score.json` हो
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # एन्डपोइन्टबाट कच्चा प्रतिक्रिया प्रिन्ट गर्नुहोस्
    print("raw response: \n", response, "\n")
    ```

## ९. अनलाइन अन्त बिन्दु मेटाउने

1. अन्त बिन्दु मेटाउन नबिर्सनुहोस्, नभए तपाईँले अन्त बिन्दुले प्रयोग गरेको कम्प्युटको बिलिङ मिटर चलिरहेको छोड्नु हुनेछ। यो Python कोडको लाइनले Azure Machine Learning मा अनलाइन अन्त बिन्दु मेटाउँछ। यसको विवरण यस प्रकार छ:

    - यसले workspace_ml_client वस्तुको online_endpoints को begin_delete विधि कल गर्दछ। यो विधि अनलाइन अन्त बिन्दुको मेटाउने प्रक्रिया सुरु गर्न प्रयोग गरिन्छ।

    - यसले मेटाउनुपर्ने अन्त बिन्दुको नाम name तर्कमार्फत निर्दिष्ट गर्दछ। यस अवस्थामा, अन्त बिन्दुको नाम online_endpoint_name चरमा भण्डारण गरिएको छ।

    - यसले मेटाउने अपरेशन पूरा नहुन्जेल सम्म पर्खन wait विधि कल गर्दछ। यो ब्लकिङ अपरेशन हो, जसको अर्थ यो स्क्रिप्टलाई अगाडि बढ्नबाट रोकिन्छ जबसम्म मेटाउने प्रक्रिया समाप्त हुँदैन।

    - सारांशमा, यो कोडको लाइनले Azure Machine Learning मा अनलाइन अन्त बिन्दु मेटाउने प्रक्रिया सुरु गर्दछ र त्यस अपरेशन पूरा हुन पर्खन्छ।

    ```python
    # Azure Machine Learning मा अनलाइन अन्तबिन्दु मेटाउनुहोस्
    # `workspace_ml_client` वस्तुको `online_endpoints` सम्पत्तिको `begin_delete` विधि अनलाइन अन्तबिन्दुको मेटाउने प्रक्रिया सुरु गर्न प्रयोग गरिन्छ
    # `name` तर्कले मेटाउनुपर्ने अन्तबिन्दुको नाम निर्दिष्ट गर्दछ, जुन `online_endpoint_name` भेरिएबलमा भण्डारण गरिएको छ
    # मेटाउने अपरेशन पूरा नभएसम्म पर्खन `wait` विधि बोलाइन्छ। यो एक अवरोधक अपरेशन हो, जसको अर्थ स्क्रिप्ट अगाडि बढ्न रोकिन्छ जबसम्म मेटाउने प्रक्रिया समाप्त हुँदैन
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यस दस्तावेज़लाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकता सुनिश्चित गर्न प्रयासरत छौं, तर कृपया जानकारि लिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा गलत बुझाइ हुन सक्छ। मूल दस्तावेज़लाई यसको मातृभाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा गलत व्याख्यामा हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->