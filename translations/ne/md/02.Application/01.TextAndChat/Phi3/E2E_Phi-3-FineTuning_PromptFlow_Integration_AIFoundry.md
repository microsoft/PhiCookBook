# Fine-tune र Microsoft Foundry मा Prompt flow सँग कस्टम Phi-3 मोडेलहरू एकीकृत गर्नुहोस्

यो अन्त्य-देखि-अन्त (E2E) नमुना Microsoft Tech Community बाट "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" मार्गदर्शनमा आधारित छ। यसले Microsoft Foundry मा Prompt flow सँग कस्टम Phi-3 मोडेलहरूलाई fine-tuning, deployment, र एकीकरण गर्ने प्रक्रियाहरू प्रस्तुत गर्दछ। स्थानीय रूपमा कोड चलाउने "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" E2E नमुनाको विपरीत, यो ट्युटोरियल Azure AI / ML Studio भित्र तपाईंको मोडेललाई पूरा रूपले fine-tune र एकीकृत गर्न केन्द्रित छ।

## अवलोकन

यस E2E नमुनामा, तपाईं Phi-3 मोडेललाई fine-tune गर्ने र Microsoft Foundry मा Prompt flow सँग एकीकृत गर्ने तरिका सिक्नुहुनेछ। Azure AI / ML Studio को उपयोग गरेर, तपाईंले कस्टम AI मोडेलहरूको deploy र प्रयोगका लागि workflow स्थापना गर्नुहुनेछ। यो E2E नमुना तीन परिदृश्यमा विभाजित गरिएको छ:

**परिदृश्य 1: Azure स्रोतहरू सेट अप गर्नुहोस् र fine-tuning को लागि तयार गर्नुहोस्**

**परिदृश्य 2: Phi-3 मोडेललाई fine-tune गर्नुहोस् र Azure Machine Learning Studio मा Deploy गर्नुहोस्**

**परिदृश्य 3: Prompt flow सँग एकीकृत गर्नुहोस् र Microsoft Foundry मा तपाईंको कस्टम मोडेलसँग कुराकानी गर्नुहोस्**

यहाँ यस E2E नमुनाको अवलोकन छ।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ne/00-01-architecture.198ba0f1ae6d841a.webp)

### सामग्री तालिका

1. **[परिदृश्य 1: Azure स्रोतहरू सेट अप गर्नुहोस् र fine-tuning को लागि तयार गर्नुहोस्](#परिदृश्य-1-azure-स्रोतहरू-सेट-अप-गर्नुहोस्-र-fine-tuning-को-लागि-तयार-गर्नुहोस्)**
    - [Azure Machine Learning Workspace सिर्जना गर्नुहोस्](#azure-machine-learning-workspace-सिर्जना-गर्नुहोस्)
    - [Azure Subscription मा GPU कोटा अनुरोध गर्नुहोस्](#azure-subscription-मा-gpu-कोटा-अनुरोध-गर्नुहोस्)
    - [भूमिका असाइनमेन्ट थप्नुहोस्](#भूमिका-असाइनमेन्ट-थप्नुहोस्)
    - [प्रोजेक्ट सेट अप गर्नुहोस्](#प्रोजेक्ट-सेट-अप-गर्नुहोस्)
    - [fine-tuning को लागि dataset तयार गर्नुहोस्](#फाइन-ट्यूनिंगका-लागि-डाटासेट-तयार-गर्नुहोस्)

1. **[परिदृश्य 2: Phi-3 मोडेललाई fine-tune गर्नुहोस् र Azure Machine Learning Studio मा Deploy गर्नुहोस्](#परिदृश्य-२-phi-3-मोडेल-फाइन-ट्युन-गर्नुहोस्-र-azure-machine-learning-studio-मा-तैनाथी-गर्नुहोस्)**
    - [Phi-3 मोडेललाई fine-tune गर्नुहोस्](#phi-3-मोडेल-फाइन-ट्युन-गर्नुहोस्)
    - [fine-tuned Phi-3 मोडेल deploy गर्नुहोस्](#फाइन-ट्युन-गरिएको-phi-3-मोडेल-तैनाथी-गर्नुहोस्)

1. **[परिदृश्य 3: Prompt flow सँग एकीकृत गर्नुहोस् र Microsoft Foundry मा तपाईंको कस्टम मोडेलसँग कुराकानी गर्नुहोस्](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [कस्टम Phi-3 मोडेललाई Prompt flow सँग एकीकृत गर्नुहोस्](#कस्टम-phi-3-मोडेललाई-prompt-flow-सँग-एकीकृत-गर्नुहोस्)
    - [तपाईंको कस्टम Phi-3 मोडेलसँग कुराकानी गर्नुहोस्](#तपाईंको-अनुकूलित-phi-3-मोडेलसँग-कुरा-गर्नुहोस्)

## परिदृश्य 1: Azure स्रोतहरू सेट अप गर्नुहोस् र fine-tuning को लागि तयार गर्नुहोस्

### Azure Machine Learning Workspace सिर्जना गर्नुहोस्

1. पोर्टल पृष्ठको शीर्षमा रहेको **search bar** मा *azure machine learning* टाइप गर्नुहोस् र देखिएका विकल्पहरूबाट **Azure Machine Learning** चयन गर्नुहोस्।

    ![Type azure machine learning.](../../../../../../translated_images/ne/01-01-type-azml.acae6c5455e67b4b.webp)

2. नेभिगेशन मेनुबाट **+ Create** चयन गर्नुहोस्।

3. नेभिगेशन मेनुबाट **New workspace** चयन गर्नुहोस्।

    ![Select new workspace.](../../../../../../translated_images/ne/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. तलका कार्यहरू गर्नुहोस्:

    - तपाईंको Azure **Subscription** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Resource group** चयन गर्नुहोस् (आवश्यक भए नयाँ बनाउनुहोस्)।
    - **Workspace Name** प्रविष्ट गर्नुहोस्। यो एक अद्वितीय मान हुनु आवश्यक छ।
    - प्रयोग गर्न चाहेको **Region** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Storage account** चयन गर्नुहोस् (आवश्यक भए नयाँ बनाउनुहोस्)।
    - प्रयोग गर्नको लागि **Key vault** चयन गर्नुहोस् (आवश्यक भए नयाँ बनाउनुहोस्)।
    - प्रयोग गर्नको लागि **Application insights** चयन गर्नुहोस् (आवश्यक भए नयाँ बनाउनुहोस्)।
    - प्रयोग गर्नको लागि **Container registry** चयन गर्नुहोस् (आवश्यक भए नयाँ बनाउनुहोस्)।

    ![Fill azure machine learning.](../../../../../../translated_images/ne/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** चयन गर्नुहोस्।

6. **Create** चयन गर्नुहोस्।

### Azure Subscription मा GPU कोटा अनुरोध गर्नुहोस्

यस ट्युटोरियलमा, तपाईं GPUs को उपयोग गरेर Phi-3 मोडेललाई fine-tune र deploy गर्ने तरिका सिक्नुहुनेछ। Fine-tuning को लागि *Standard_NC24ads_A100_v4* GPU प्रयोग गर्नुहुनेछ, जसको कोटा अनुरोध आवश्यक छ। Deployment को लागि *Standard_NC6s_v3* GPU प्रयोग गर्नुहुनेछ, जसको पनि कोटा अनुरोध आवश्यक छ।

> [!NOTE]
>
> केवल Pay-As-You-Go सब्स्क्रिप्शनहरू (मानक सब्स्क्रिप्शन प्रकार) GPU आबंटनको लागि योग्य छन्; लाभ सब्स्क्रिप्शनहरू हाल समर्थित छैनन्।
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) मा जानुहोस्।

1. *Standard NCADSA100v4 Family* कोटा अनुरोध गर्न तलका कार्यहरू गर्नुहोस्:

    - बायाँपट्टि रहेको ट्याबबाट **Quota** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Virtual machine family** चयन गर्नुहोस्। उदाहरणका लागि, *Standard_NC24ads_A100_v4* GPU समावेश गरेको **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** चयन गर्नुहोस्।
    - नेभिगेशन मेनुबाट **Request quota** चयन गर्नुहोस्।

        ![Request quota.](../../../../../../translated_images/ne/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota पृष्ठभित्र, तपाईंले प्रयोग गर्न चाहेको **New cores limit** प्रविष्ट गर्नुहोस्। उदाहरणका लागि, 24।
    - Request quota पृष्ठभित्र, GPU कोटा अनुरोध गर्न **Submit** चयन गर्नुहोस्।

1. *Standard NCSv3 Family* कोटा अनुरोध गर्न तलका कार्यहरू गर्नुहोस्:

    - बायाँपट्टि ट्याबबाट **Quota** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Virtual machine family** चयन गर्नुहोस्। उदाहरणका लागि, *Standard_NC6s_v3* GPU समावेश गरेको **Standard NCSv3 Family Cluster Dedicated vCPUs** चयन गर्नुहोस्।
    - नेभिगेशन मेनुबाट **Request quota** चयन गर्नुहोस्।
    - Request quota पृष्ठमा, तपाईंले प्रयोग गर्न चाहेको **New cores limit** प्रविष्ट गर्नुहोस्। उदाहरणका लागि, 24।
    - Request quota पृष्ठभित्र, GPU कोटा अनुरोध गर्न **Submit** चयन गर्नुहोस्।

### भूमिका असाइनमेन्ट थप्नुहोस्

तपाईंका मोडेलहरू fine-tune र deploy गर्नका लागि, पहिला User Assigned Managed Identity (UAI) सिर्जना गर्नुपर्छ र यसलाई उपयुक्त अनुमति दिनुपर्छ। यो UAI deployment को Authentication मा प्रयोग हुनेछ।

#### User Assigned Managed Identity(UAI) सिर्जना गर्नुहोस्

1. पोर्टल पृष्ठको शीर्षमा रहेको **search bar** मा *managed identities* टाइप गर्नुहोस् र देखिएका विकल्पहरूबाट **Managed Identities** चयन गर्नुहोस्।

    ![Type managed identities.](../../../../../../translated_images/ne/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** चयन गर्नुहोस्।

    ![Select create.](../../../../../../translated_images/ne/03-02-select-create.92bf8989a5cd98f2.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - तपाईंको Azure **Subscription** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Resource group** चयन गर्नुहोस् (आवश्यक भए नयाँ बनाउनुहोस्)।
    - प्रयोग गर्न चाहेको **Region** चयन गर्नुहोस्।
    - **Name** प्रविष्ट गर्नुहोस्। यो अनौंठो मान हुन आवश्यक छ।

    ![Select create.](../../../../../../translated_images/ne/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** चयन गर्नुहोस्।

1. **+ Create** चयन गर्नुहोस्।

#### Managed Identity लाई Contributor भूमिका असाइन गर्नुहोस्

1. तपाईंले सिर्जना गरेको Managed Identity स्रोतमा जानुहोस्।

1. बायाँपट्टि ट्याबबाट **Azure role assignments** चयन गर्नुहोस्।

1. नेभिगेशन मेनुबाट **+Add role assignment** चयन गर्नुहोस्।

1. Add role assignment पृष्ठमा तलका कार्यहरू गर्नुहोस्:
    - **Scope** लाई **Resource group** मा सेट गर्नुहोस्।
    - तपाईंको Azure **Subscription** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Resource group** चयन गर्नुहोस्।
    - **Role** लाई **Contributor** मा सेट गर्नुहोस्।

    ![Fill contributor role.](../../../../../../translated_images/ne/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** चयन गर्नुहोस्।

#### Managed Identity लाई Storage Blob Data Reader भूमिका असाइन गर्नुहोस्

1. पोर्टल पृष्ठको शीर्षमा रहेको **search bar** मा *storage accounts* टाइप गर्नुहोस् र देखिएका विकल्पहरूबाट **Storage accounts** चयन गर्नुहोस्।

    ![Type storage accounts.](../../../../../../translated_images/ne/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. तपाईंले सिर्जना गरेको Azure Machine Learning workspace सँग सम्बद्ध storage account चयन गर्नुहोस्। उदाहरणका लागि, *finetunephistorage*।

1. Add role assignment पृष्ठमा जान तलका कार्यहरू गर्नुहोस्:

    - तपाईंले सिर्जना गरेको Azure Storage account मा जानुहोस्।
    - बायाँपट्टि ट्याबबाट **Access Control (IAM)** चयन गर्नुहोस्।
    - नेभिगेशन मेनुबाट **+ Add** चयन गर्नुहोस्।
    - नेभिगेशन मेनुबाट **Add role assignment** चयन गर्नुहोस्।

    ![Add role.](../../../../../../translated_images/ne/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment पृष्ठमा तलका कार्यहरू गर्नुहोस्:

    - भूमिका पृष्ठमा, **search bar** मा *Storage Blob Data Reader* टाइप गर्नुहोस् र विकल्पहरूबाट **Storage Blob Data Reader** चयन गर्नुहोस्।
    - भूमिका पृष्ठमा, **Next** चयन गर्नुहोस्।
    - सदस्यहरू पृष्ठमा, **Assign access to** मा **Managed identity** चयन गर्नुहोस्।
    - सदस्यहरू पृष्ठमा, **+ Select members** चयन गर्नुहोस्।
    - चयनित Managed identities पृष्ठमा, तपाईंको Azure **Subscription** चयन गर्नुहोस्।
    - चयनित Managed identities पृष्ठमा, **Managed identity** लाई **Manage Identity** मा सेट गर्नुहोस्।
    - तपाईंले सिर्जना गरेको Manage Identity चयन गर्नुहोस्। उदाहरणका लागि, *finetunephi-managedidentity*।
    - चयनित Managed identities पृष्ठमा, **Select** चयन गर्नुहोस्।

    ![Select managed identity.](../../../../../../translated_images/ne/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** चयन गर्नुहोस्।

#### Managed Identity लाई AcrPull भूमिका असाइन गर्नुहोस्

1. पोर्टल पृष्ठको शीर्षमा रहेको **search bar** मा *container registries* टाइप गर्नुहोस् र देखिएका विकल्पहरूबाट **Container registries** चयन गर्नुहोस्।

    ![Type container registries.](../../../../../../translated_images/ne/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning workspace सँग सम्बद्ध container registry चयन गर्नुहोस्। उदाहरणका लागि, *finetunephicontainerregistry*।

1. Add role assignment पृष्ठमा जान तलका कार्यहरू गर्नुहोस्:

    - बायाँपट्टि ट्याबबाट **Access Control (IAM)** चयन गर्नुहोस्।
    - नेभिगेशन मेनुबाट **+ Add** चयन गर्नुहोस्।
    - नेभिगेशन मेनुबाट **Add role assignment** चयन गर्नुहोस्।

1. Add role assignment पृष्ठमा तलका कार्यहरू गर्नुहोस्:

    - भूमिका पृष्ठमा, **search bar** मा *AcrPull* टाइप गर्नुहोस् र विकल्पहरूबाट **AcrPull** चयन गर्नुहोस्।
    - भूमिका पृष्ठमा, **Next** चयन गर्नुहोस्।
    - सदस्यहरू पृष्ठमा, **Assign access to** मा **Managed identity** चयन गर्नुहोस्।
    - सदस्यहरू पृष्ठमा, **+ Select members** चयन गर्नुहोस्।
    - चयनित Managed identities पृष्ठमा, तपाईंको Azure **Subscription** चयन गर्नुहोस्।
    - चयनित Managed identities पृष्ठमा, **Managed identity** लाई **Manage Identity** मा सेट गर्नुहोस्।
    - तपाईंले सिर्जना गरेको Manage Identity चयन गर्नुहोस्। उदाहरणका लागि, *finetunephi-managedidentity*।
    - चयनित Managed identities पृष्ठमा, **Select** चयन गर्नुहोस्।
    - **Review + assign** चयन गर्नुहोस्।

### प्रोजेक्ट सेट अप गर्नुहोस्

fine-tuning का लागि आवश्यक dataset डाउनलोड गर्न, तपाईँले स्थानीय वातावरण सेट अप गर्नु हुनेछ।

यस अभ्यासमा, तपाईं:

- काम गर्नको लागि एउटा फोल्डर सिर्जना गर्नुहुनेछ।
- भर्चुअल वातावरण सिर्जना गर्नुहुनेछ।
- आवश्यक प्याकेजहरू स्थापना गर्नुहुनेछ।
- dataset डाउनलोड गर्न *download_dataset.py* फाइल सिर्जना गर्नुहुनेछ।

#### काम गर्नको लागि फोल्डर सिर्जना गर्नुहोस्

1. टर्मिनल विन्डो खोल्नुहोस् र डिफल्ट पथमा *finetune-phi* नामक फोल्डर सिर्जना गर्न तलको कमाण्ड टाइप गर्नुहोस्।

    ```console
    mkdir finetune-phi
    ```

2. तपाईंले सिर्जना गरेको *finetune-phi* फोल्डरमा जान तलको कमाण्ड टर्मिनलमा टाइप गर्नुहोस्।

    ```console
    cd finetune-phi
    ```

#### भर्चुअल वातावरण सिर्जना गर्नुहोस्

1. आफ्नो टर्मिनलमा *.venv* नामक भर्चुअल वातावरण सिर्जना गर्न तलको कमाण्ड टाइप गर्नुहोस्।
    ```console
    python -m venv .venv
    ```

2. आफ्नो टर्मिनल भित्र भर्चुअल वातावरण सक्रिय गर्न तलको कमाण्ड टाइप गर्नुहोस्।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> यदि यो काम गर्यो भने, कमाण्ड प्रम्ट अघि *(.venv)* देखाउनु पर्छ।

#### आवश्यक प्याकेजहरू स्थापना गर्नुहोस्

1. आवश्यक प्याकेजहरू स्थापना गर्न तलका कमाण्डहरू आफ्नो टर्मिनलमा टाइप गर्नुहोस्।

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` सिर्जना गर्नुहोस्

> [!NOTE]
> पूर्ण फोल्डर संरचना:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** खोल्नुहोस्।

1. मेनु बारबाट **File** चयन गर्नुहोस्।

1. **Open Folder** चयन गर्नुहोस्।

1. तपाईंले सिर्जना गर्नुभएको *finetune-phi* फोल्डर चयन गर्नुहोस्, जुन *C:\Users\yourUserName\finetune-phi* मा अवस्थित छ।

    ![तपाईंले सिर्जना गर्नुभएको फोल्डर चयन गर्नुहोस्।](../../../../../../translated_images/ne/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code को बायाँ पट्टि प्यानलमा, राइट-क्लिक गरी **New File** चयन गरेर *download_dataset.py* नामक नयाँ फाइल बनाउनुहोस्।

    ![नयाँ फाइल बनाउनुहोस्।](../../../../../../translated_images/ne/04-02-create-new-file.cf9a330a3a9cff92.webp)

### फाइन-ट्यूनिंगका लागि डाटासेट तयार गर्नुहोस्

यस अभ्यासमा, तपाईंले *download_dataset.py* फाइल चलाएर *ultrachat_200k* डाटासेटहरू आफ्नो स्थानीय वातावरणमा डाउनलोड गर्नुहुनेछ। त्यसपछि यो डाटासेटहरू Azure Machine Learning मा Phi-3 मोडेललाई फाइन-ट्यून गर्न प्रयोग गर्नुहुनेछ।

यस अभ्यासमा, तपाईंले:

- *download_dataset.py* फाइलमा कोड थपेर डाटासेटहरू डाउनलोड गर्नुहोस्।
- *download_dataset.py* फाइल चलाएर डाटासेटहरू आफ्नो स्थानीय वातावरणमा डाउनलोड गर्नुहोस्।

#### *download_dataset.py* प्रयोग गरेर डाटासेट डाउनलोड गर्नुहोस्

1. Visual Studio Code मा *download_dataset.py* फाइल खोल्नुहोस्।

1. तलको कोड *download_dataset.py* फाइलमा थप्नुहोस्।

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # निर्दिष्ट नाम, कन्फिगरेसन, र विभाजन अनुपातसहित डेटासेट लोड गर्नुहोस्
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # डेटासेटलाई ट्रेन र टेस्ट सेटमा विभाजन गर्नुहोस् (८०% ट्रेन, २०% टेस्ट)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # फोल्डर अवस्थित नभए उत्पन्न गर्नुहोस्
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # फाइललाई लेख्न मोडमा खोल्नुहोस्
        with open(filepath, 'w', encoding='utf-8') as f:
            # डेटासेटका हरेक रेकर्डमा पुनरावृत्ति गर्नुहोस्
            for record in dataset:
                # रेकर्डलाई JSON वस्तुका रूपमा डम्प गरेर फाइलमा लेख्नुहोस्
                json.dump(record, f)
                # रेकर्डहरू अलग गर्न न्यूलाइन क्यारेक्टर लेख्नुहोस्
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ULTRACHAT_200k डेटासेट निर्दिष्ट कन्फिगरेसन र विभाजन अनुपातसहित लोड र विभाजन गर्नुहोस्
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # विभाजनबाट ट्रेन र टेस्ट डेटासेट निकालनुहोस्
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ट्रेन डेटासेटलाई JSONL फाइलमा बचत गर्नुहोस्
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # टेस्ट डेटासेटलाई अलग JSONL फाइलमा बचत गर्नुहोस्
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. स्क्रिप्ट चलाएर डाटासेट तपाईंको स्थानीय वातावरणमा डाउनलोड गर्न तलको कमाण्ड आफ्नो टर्मिनलमा टाइप गर्नुहोस्।

    ```console
    python download_dataset.py
    ```

1. डाटासेटहरू सफलतापूर्वक तपाईंको स्थानीय *finetune-phi/data* निर्देशिकामा सहेजिएको छ कि छैन भनि जाँच गर्नुहोस्।

> [!NOTE]
>
> #### डाटासेटको आकार र फाइन-ट्युनिंग समय सम्बन्धी नोट
>
> यस ट्युटोरियलमा, तपाईंले डाटासेटको केवल 1% (`split='train[:1%]'`) मात्र प्रयोग गर्नुहुन्छ। यसले डाटाको मात्रा निकै कम गर्छ, जसले अपलोड र फाइन-ट्युनिंग दुवै प्रक्रिया छिटो बनाउँछ। तपाईं प्रशिक्षण समय र मोडेल प्रदर्शन बीच सही सन्तुलन खोज्न प्रतिशत समायोजन गर्न सक्नुहुन्छ। डाटासेटको सानो उपसेट प्रयोग गर्दा फाइन-ट्युनिंग समय कम हुन्छ, जसले ट्युटोरियललाई अधिक व्यवस्थापनयोग्य बनाउँछ।

## परिदृश्य २: Phi-3 मोडेल फाइन-ट्युन गर्नुहोस् र Azure Machine Learning Studio मा तैनाथी गर्नुहोस्

### Phi-3 मोडेल फाइन-ट्युन गर्नुहोस्

यस अभ्यासमा, तपाईं Azure Machine Learning Studio मा Phi-3 मोडेल फाइन-ट्युन गर्नुहुनेछ।

यस अभ्यासमा, तपाईंले:

- फाइन-ट्युनिंगका लागि कम्प्युटर क्लस्टर सिर्जना गर्नुहोस्।
- Azure Machine Learning Studio मा Phi-3 मोडेल फाइन-ट्युन गर्नुहोस्।

#### फाइन-ट्युनिंगका लागि कम्प्युटर क्लस्टर सिर्जना गर्नुहोस्

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) भ्रमण गर्नुहोस्।

1. बाँया पट्टि ट्याबबाट **Compute** चयन गर्नुहोस्।

1. नेभिगेसन मेनुबाट **Compute clusters** चयन गर्नुहोस्।

1. **+ New** चयन गर्नुहोस्।

    ![Compute चयन गर्नुहोस्।](../../../../../../translated_images/ne/06-01-select-compute.a29cff290b480252.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - तपाईं प्रयोग गर्न चाहानुभएको **Region** चयन गर्नुहोस्।
    - **Virtual machine tier** लाई **Dedicated** चयन गर्नुहोस्।
    - **Virtual machine type** लाई **GPU** चयन गर्नुहोस्।
    - **Virtual machine size** फिल्टरमा **Select from all options** चयन गर्नुहोस्।
    - **Virtual machine size** लाई **Standard_NC24ads_A100_v4** चयन गर्नुहोस्।

    ![क्लस्टर सिर्जना गर्नुहोस्।](../../../../../../translated_images/ne/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** चयन गर्नुहोस्।

1. तलका कार्यहरू गर्नुहोस्:

    - **Compute name** प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।
    - **Minimum number of nodes** लाई **0** चयन गर्नुहोस्।
    - **Maximum number of nodes** लाई **1** चयन गर्नुहोस्।
    - **Idle seconds before scale down** लाई **120** चयन गर्नुहोस्।

    ![क्लस्टर सिर्जना गर्नुहोस्।](../../../../../../translated_images/ne/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** चयन गर्नुहोस्।

#### Phi-3 मोडेल फाइन-ट्युन गर्नुहोस्

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) भ्रमण गर्नुहोस्।

1. तपाईंले सिर्जना गर्नुभएको Azure Machine Learning Workspace चयन गर्नुहोस्।

    ![तपाईंले सिर्जना गर्नुभएको Workspace चयन गर्नुहोस्।](../../../../../../translated_images/ne/06-04-select-workspace.a92934ac04f4f181.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - बाँया पट्टि ट्याबबाट **Model catalog** चयन गर्नुहोस्।
    - **search bar** मा *phi-3-mini-4k* टाइप गर्नुहोस् र देखिएका विकल्पहरूमध्ये **Phi-3-mini-4k-instruct** चयन गर्नुहोस्।

    ![phi-3-mini-4k टाइप गर्नुहोस्।](../../../../../../translated_images/ne/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. नेभिगेसन मेनुबाट **Fine-tune** चयन गर्नुहोस्।

    ![Fine-tune चयन गर्नुहोस्।](../../../../../../translated_images/ne/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - **Select task type** लाई **Chat completion** चयन गर्नुहोस्।
    - **+ Select data** चयन गरेर **Training data** अपलोड गर्नुहोस्।
    - Validation data अपलोडको प्रकारलाई **Provide different validation data** मा सेट गर्नुहोस्।
    - **+ Select data** चयन गरेर **Validation data** अपलोड गर्नुहोस्।

    ![फाइन-ट्युनिङ पेज भर्नुहोस्।](../../../../../../translated_images/ne/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> तपाईं **Advanced settings** चयन गरेर **learning_rate** र **lr_scheduler_type** जस्ता कन्फिगरेसनहरू अनुकूलन गरी फाइन-ट्युनिङ प्रक्रिया आफैंअनुसार सुधार गर्न सक्नुहुन्छ।

1. **Finish** चयन गर्नुहोस्।

1. यस अभ्यासमा, तपाईंले Azure Machine Learning प्रयोग गरी सफलतापूर्वक Phi-3 मोडेल फाइन-ट्युन गर्नुभयो। कृपया ध्यान दिनुहोस् कि फाइन-ट्युनिंग प्रक्रियामा केही समय लाग्न सक्छ। फाइन-ट्युनिङ काम चलाएपछि, यसलाई पूरा हुन पर्खनु आवश्यक छ। तपाईं Azure Machine Learning Workspace को बाँया पट्टि रहेको Jobs ट्याबमा गएर फाइन-ट्युनिङ कामको स्थितिलाई अनुगमन गर्न सक्नुहुन्छ। अर्को सर्गीमा, तपाईं फाइन-ट्युन गरिएको मोडेललाई तैनाथी गरी Prompt flow सँग एकीकृत गर्नुहुनेछ।

    ![फाइन-ट्युनिङ काम हेर्नुहोस्।](../../../../../../translated_images/ne/06-08-output.2bd32e59930672b1.webp)

### फाइन-ट्युन गरिएको Phi-3 मोडेल तैनाथी गर्नुहोस्

फाइन-ट्युन गरेको Phi-3 मोडेललाई Prompt flow सँग एकीकृत गर्न तपाईंले रीयल-टाइम इन्फरेन्सका लागि मोडेल तैनाथी गर्न आवश्यक छ। यस प्रक्रियाले मोडेल दर्ता, अनलाइन एन्डपोइन्ट सिर्जना, र मोडेल तैनाथी समावेश गर्दछ।

यस अभ्यासमा, तपाईंले:

- Azure Machine Learning Workspace मा फाइन-ट्युन गरिएको मोडेल दर्ता गर्नुहोस्।
- अनलाइन एन्डपोइन्ट सिर्जना गर्नुहोस्।
- दर्ता गरिएको फाइन-ट्युन गरिएको Phi-3 मोडेल तैनाथी गर्नुहोस्।

#### फाइन-ट्युन गरिएको मोडेल दर्ता गर्नुहोस्

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) भ्रमण गर्नुहोस्।

1. तपाईंले सिर्जना गर्नुभएको Azure Machine Learning Workspace चयन गर्नुहोस्।

    ![तपाईंले सिर्जना गर्नुभएको Workspace चयन गर्नुहोस्।](../../../../../../translated_images/ne/06-04-select-workspace.a92934ac04f4f181.webp)

1. बाँया पट्टि ट्याबबाट **Models** चयन गर्नुहोस्।
1. **+ Register** चयन गर्नुहोस्।
1. **From a job output** चयन गर्नुहोस्।

    ![मोडेल दर्ता गर्नुहोस्।](../../../../../../translated_images/ne/07-01-register-model.ad1e7cc05e4b2777.webp)

1. तपाईंले सिर्जना गरेको काम चयन गर्नुहोस्।

    ![काम चयन गर्नुहोस्।](../../../../../../translated_images/ne/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** चयन गर्नुहोस्।

1. **Model type** लाई **MLflow** चयन गर्नुहोस्।

1. **Job output** चयन गरिएको छ भनि सुनिश्चित गर्नुहोस्; यो स्वचालित रुपमा चयन हुनु पर्छ।

    ![आउटपुट चयन गर्नुहोस्।](../../../../../../translated_images/ne/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** चयन गर्नुहोस्।

3. **Register** चयन गर्नुहोस्।

    ![दर्ता गर्नुहोस्।](../../../../../../translated_images/ne/07-04-register.fd82a3b293060bc7.webp)

4. दर्ता गरिएको मोडेललाई तपाईं बाँया पट्टि ट्याबबाट **Models** मेनुमा गएर हेर्न सक्नुहुन्छ।

    ![दर्ता गरिएको मोडेल।](../../../../../../translated_images/ne/07-05-registered-model.7db9775f58dfd591.webp)

#### फाइन-ट्युन गरिएको मोडेल तैनाथी गर्नुहोस्

1. तपाईंले सिर्जना गरेको Azure Machine Learning Workspace मा जानुहोस्।

1. बाँया पट्टि ट्याबबाट **Endpoints** चयन गर्नुहोस्।

1. नेभिगेसन मेनुबाट **Real-time endpoints** चयन गर्नुहोस्।

    ![एन्डपोइन्ट सिर्जना गर्नुहोस्।](../../../../../../translated_images/ne/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** चयन गर्नुहोस्।

1. तपाईंले दर्ता गरेको मोडेल चयन गर्नुहोस्।

    ![दर्ता गरिएको मोडेल चयन गर्नुहोस्।](../../../../../../translated_images/ne/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** चयन गर्नुहोस्।

1. तलका कार्यहरू गर्नुहोस्:

    - **Virtual machine** लाई *Standard_NC6s_v3* चयन गर्नुहोस्।
    - तपाईं प्रयोग गर्न चाहनुभएको **Instance count** चयन गर्नुहोस्। उदाहरणका लागि, *1*।
    - **Endpoint** लाई नयाँ सिर्जना गर्न **New** चयन गर्नुहोस्।
    - **Endpoint name** प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।
    - **Deployment name** प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।

    ![तैनाथी सेटिङहरू भर्नुहोस्।](../../../../../../translated_images/ne/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** चयन गर्नुहोस्।

> [!WARNING]
> तपाईंको खातामा अतिरिक्त शुल्क लाग्नबाट बच्न, कृपया Azure Machine Learning Workspace मा सिर्जित एन्डपोइन्ट मेटाउन नभुल्नुहोस्।
>

#### Azure Machine Learning Workspace मा तैनाथी स्थिति जाँच गर्नुहोस्

1. तपाईंले सिर्जना गरेको Azure Machine Learning Workspace मा जानुहोस्।

1. बाँया पट्टि ट्याबबाट **Endpoints** चयन गर्नुहोस्।

1. तपाईंले सिर्जना गरेको एन्डपोइन्ट चयन गर्नुहोस्।

    ![एन्डपोइन्टहरू चयन गर्नुहोस्](../../../../../../translated_images/ne/07-09-check-deployment.325d18cae8475ef4.webp)

1. यस पृष्ठमा, तपाईं तैनाथी प्रक्रियाको दौरान एन्डपोइन्टहरू व्यवस्थापन गर्न सक्नुहुन्छ।

> [!NOTE]
> एकपटक तैनाथी प्रक्रिया पूरा भएपछि, सुनिश्चित गर्नुहोस् कि **Live traffic** लाई **100%** मा सेट गरिएको छ। यदि छैन भने, **Update traffic** चयन गरेर ट्राफिक सेटिङहरू समायोजन गर्नुहोस्। ट्राफिक 0% मा सेट भएको खण्डमा तपाईं मोडेल परीक्षण गर्न सक्नुहुन्न।
>
> ![ट्राफिक सेट गर्नुहोस्।](../../../../../../translated_images/ne/07-10-set-traffic.085b847e5751ff3d.webp)
>

## परिदृश्य ३: Prompt flow सँग एकीकृत गरेर Microsoft Foundry मा आफ्नो कस्टम मोडेलसँग च्याट गर्नुहोस्

### कस्टम Phi-3 मोडेललाई Prompt flow सँग एकीकृत गर्नुहोस्

तपाईंको फाइन-ट्युन गरिएको मोडेल सफलतापूर्वक तैनाथी गरेपछि, अब यसलाई Prompt Flow सँग एकीकृत गरेर तपाईंको मोडेललाई रियल-टाइम प्रयोगहरूमा प्रयोग गर्न सक्नुहुन्छ, जसले तपाईंको कस्टम Phi-3 मोडेलसँग विभिन्न अन्तरक्रियात्मक कार्यहरू सम्भव बनाउँछ।

यस अभ्यासमा, तपाईंले:

- Microsoft Foundry Hub सिर्जना गर्नुहोस्।
- Microsoft Foundry Project सिर्जना गर्नुहोस्।
- Prompt flow सिर्जना गर्नुहोस्।
- फाइन-ट्युन गरिएको Phi-3 मोडेलको लागि कस्टम कनेक्शन थप्नुहोस्।
- तपाईंको कस्टम Phi-3 मोडेलसँग च्याट गर्न Prompt flow सेटअप गर्नुहोस्।

> [!NOTE]
> तपाईं Azure ML Studio प्रयोग गरेर पनि Promptflow सँग एकीकृत गर्न सक्नुहुन्छ। एउटै एकीकरण प्रक्रिया Azure ML Studio लाई पनि लागु गर्न सकिन्छ।

#### Microsoft Foundry Hub सिर्जना गर्नुहोस्

Project सिर्जना गर्नु अघि तपाईंले Hub सिर्जना गर्नु आवश्यक छ। Hub रिसोर्स ग्रुप जस्तो काम गर्दछ, जसले Microsoft Foundry भित्र बहु Project हरूलाई व्यवस्थित र व्यवस्थापन गर्न अनुमति दिन्छ।
1. भ्रमण गर्नुहोस् [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) मा।

1. बायाँपट्टि ट्याबबाट **All hubs** चयन गर्नुहोस्।

1. नेभिगेसन मेनूबाट **+ New hub** चयन गर्नुहोस्।

    ![Create hub.](../../../../../../translated_images/ne/08-01-create-hub.8f7dd615bb8d9834.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - **Hub name** प्रविष्ट गर्नुहोस्। यो एक अद्वितीय मान हुनुपर्छ।
    - आफ्नो Azure **Subscription** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Resource group** चयन गर्नुहोस् (आवश्यक परे नयाँ बनाउनुस्)।
    - तपाईंले प्रयोग गर्न चाहेको **Location** चयन गर्नुहोस्।
    - प्रयोग गर्नको लागि **Connect Azure AI Services** चयन गर्नुहोस् (आवश्यक परे नयाँ बनाउनुस्)।
    - **Connect Azure AI Search** मा **Skip connecting** चयन गर्नुहोस्।

    ![Fill hub.](../../../../../../translated_images/ne/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** चयन गर्नुहोस्।

#### Microsoft Foundry परियोजना सिर्जना गर्नुहोस्

1. तपाईंले सिर्जना गरेको Hub मा, बायाँपट्टि ट्याबबाट **All projects** चयन गर्नुहोस्।

1. नेभिगेसन मेनूबाट **+ New project** चयन गर्नुहोस्।

    ![Select new project.](../../../../../../translated_images/ne/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** प्रविष्ट गर्नुहोस्। यो एक अद्वितीय मान हुनुपर्छ।

    ![Create project.](../../../../../../translated_images/ne/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** चयन गर्नुहोस्।

#### Fine-tuned Phi-3 मोडेलका लागि अनुकूलन गरिएको कनेक्शन थप्नुहोस्

तपाईंको अनुकूलित Phi-3 मोडेललाई Prompt flow सँग एकीकृत गर्न, मोडेलको endpoint र key लाई अनुकूलन गरिएको कनेक्शनमा सुरक्षित गर्न आवश्यक छ। यसले Prompt flow मा तपाईंको अनुकूलित Phi-3 मोडेल पहुँच सुनिश्चित गर्दछ।

#### Fine-tuned Phi-3 मोडेलको api key र endpoint uri सेट गर्नुहोस्

1. भ्रमण गर्नुहोस् [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) मा।

1. तपाईंले सिर्जना गर्नुभएको Azure Machine learning workspace मा जानुहोस्।

1. बायाँपट्टि ट्याबबाट **Endpoints** चयन गर्नुहोस्।

    ![Select endpoints.](../../../../../../translated_images/ne/08-06-select-endpoints.aff38d453bcf9605.webp)

1. तपाईंले सिर्जना गर्नुभएको endpoint चयन गर्नुहोस्।

    ![Select endpoints.](../../../../../../translated_images/ne/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. नेभिगेसन मेनूबाट **Consume** चयन गर्नुहोस्।

1. तपाईंको **REST endpoint** र **Primary key** कपी गर्नुहोस्।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ne/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### अनुकूलन गरिएको कनेक्शन थप्नुहोस्

1. भ्रमण गर्नुहोस् [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) मा।

1. तपाईंले सिर्जना गरेको Microsoft Foundry परियोजनामा जानुहोस्।

1. तपाईंले सिर्जना गरेको परियोजनामा, बायाँपट्टि ट्याबबाट **Settings** चयन गर्नुहोस्।

1. **+ New connection** चयन गर्नुहोस्।

    ![Select new connection.](../../../../../../translated_images/ne/08-09-select-new-connection.02eb45deadc401fc.webp)

1. नेभिगेसन मेनूबाट **Custom keys** चयन गर्नुहोस्।

    ![Select custom keys.](../../../../../../translated_images/ne/08-10-select-custom-keys.856f6b2966460551.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - **+ Add key value pairs** चयन गर्नुहोस्।
    - की नामका लागि **endpoint** प्रविष्ट गर्नुहोस् र Azure ML Studio बाट कपी गरेको endpoint लाई मान फिल्डमा टाँस्नुहोस्।
    - पुन: **+ Add key value pairs** चयन गर्नुहोस्।
    - की नामका लागि **key** प्रविष्ट गर्नुहोस् र Azure ML Studio बाट कपी गरेको key लाई मान फिल्डमा टाँस्नुहोस्।
    - कीहरू थपेपछि, कीलाई खुलाउन नदिनको लागि **is secret** चयन गर्नुहोस्।

    ![Add connection.](../../../../../../translated_images/ne/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** चयन गर्नुहोस्।

#### Prompt flow सिर्जना गर्नुहोस्

तपाईंले Microsoft Foundry मा अनुकूलन गरिएको कनेक्शन थप्नुभयो। अब, तलका चरणहरू प्रयोग गरी Prompt flow सिर्जना गरौं। त्यसपछि, तपाईंले यस Prompt flow लाई अनुकूलन गरिएको कनेक्शनसँग जडान गर्नुहुनेछ ताकि तपाईं Prompt flow भित्र अनुकूलित मोडेल प्रयोग गर्न सक्नुहुनेछ।

1. तपाईंले सिर्जना गरेको Microsoft Foundry परियोजनामा जानुहोस्।

1. बायाँपट्टि ट्याबबाट **Prompt flow** चयन गर्नुहोस्।

1. नेभिगेसन मेनूबाट **+ Create** चयन गर्नुहोस्।

    ![Select Promptflow.](../../../../../../translated_images/ne/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. नेभिगेसन मेनूबाट **Chat flow** चयन गर्नुहोस्।

    ![Select chat flow.](../../../../../../translated_images/ne/08-13-select-flow-type.2ec689b22da32591.webp)

1. प्रयोग गर्नको लागि **Folder name** प्रविष्ट गर्नुहोस्।

    ![Enter name.](../../../../../../translated_images/ne/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** चयन गर्नुहोस्।

#### तपाईंको अनुकूलित Phi-3 मोडेलसँग कुरा गर्न Prompt flow सेटअप गर्नुहोस्

तपाईंले आफ्नो अनुकूलित Phi-3 मोडेललाई Prompt flow मा एकीकृत गर्न आवश्यक छ। तथापि, उपलब्ध वर्तमान Prompt flow यस उद्देश्यका लागि डिजाइन गरिएको छैन। त्यसैले, तपाईंले अनुकूलित मोडेललाई एकीकृत गर्न Prompt flow पुनः डिजाइन गर्नुपर्नेछ।

1. Prompt flow भित्र, वर्तमान फ्लो पुनर्निर्माण गर्न तलका कार्यहरू गर्नुहोस्:

    - **Raw file mode** चयन गर्नुहोस्।
    - *flow.dag.yml* फाइलभित्र सबै वर्तमान कोड मेटाउनुहोस्।
    - तलको कोड *flow.dag.yml* फाइलमा थप्नुहोस्।

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

    - **Save** चयन गर्नुहोस्।

    ![Select raw file mode.](../../../../../../translated_images/ne/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. *integrate_with_promptflow.py* फाइलमा तलको कोड थप्नुहोस् ताकि Prompt flow मा अनुकूलित Phi-3 मोडेल प्रयोग गर्न सकियोस्।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # लगिङ सेटअप
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

        # "connection" कस्टम कनेक्शनको नाम हो, "endpoint", "key" कस्टम कनेक्शनमा रहेका कुञ्जीहरू हुन्
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
            
            # पूर्ण JSON प्रतिक्रिया लग गर्नुहोस्
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

    ![Paste prompt flow code.](../../../../../../translated_images/ne/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry मा Prompt flow को प्रयोग सम्बन्धी थप विस्तृत जानकारीका लागि, तपाईं [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) हेर्न सक्नुहुन्छ।

1. **Chat input**, **Chat output** चयन गरेर आफ्नो मोडेलसँग कुरा सक्षम गर्नुहोस्।

    ![Input Output.](../../../../../../translated_images/ne/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. अब तपाईं आफ्नो अनुकूलित Phi-3 मोडेलसँग कुरा गर्न तयार हुनुहुन्छ। अर्को अभ्यासमा, तपाईंले कसरी Prompt flow सुरु गर्ने र यसलाई आफ्नो fine-tuned Phi-3 मोडेलसँग कसरी प्रयोग गर्ने भन्ने सिक्नुहुनेछ।

> [!NOTE]
>
> पुनर्निर्मित फ्लो तलको तस्वीर जस्तै देखिनुपर्छ:
>
> ![Flow example.](../../../../../../translated_images/ne/08-18-graph-example.d6457533952e690c.webp)
>

### तपाईंको अनुकूलित Phi-3 मोडेलसँग कुरा गर्नुहोस्

अब तपाईंले आफ्नो अनुकूलित Phi-3 मोडेललाई fine-tune गरी Prompt flow सँग एकीकृत गर्नुभयो, तपाईं यसको साथ कुराकानी सुरु गर्न तयार हुनुहुन्छ। यो अभ्यासले तपाईंलाई आफ्नो मोडेलसँग कसरी सेटअप र कुराकानी सुरु गर्ने चरणहरूमा मार्गदर्शन गर्नेछ। यी चरणहरू पछ्याएर, तपाईं आफ्नो fine-tuned Phi-3 मोडेलका विविध कार्य र संवादहरू पूरा रूपमा उपयोग गर्न सक्नुहुनेछ।

- Prompt flow मार्फत तपाईंको अनुकूलित Phi-3 मोडेलसँग कुरा गर्नुहोस्।

#### Prompt flow सुरु गर्नुहोस्

1. Prompt flow सुरु गर्न **Start compute sessions** चयन गर्नुहोस्।

    ![Start compute session.](../../../../../../translated_images/ne/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. प्यारेमिटरहरू नवीकरण गर्न **Validate and parse input** चयन गर्नुहोस्।

    ![Validate input.](../../../../../../translated_images/ne/09-02-validate-input.317c76ef766361e9.webp)

1. तपाईंले सिर्जना गरेको अनुकूलन गरिएको कनेक्शनको **connection** को मान चयन गर्नुहोस्। उदाहरणको लागि, *connection*।

    ![Connection.](../../../../../../translated_images/ne/09-03-select-connection.99bdddb4b1844023.webp)

#### तपाईंको अनुकूलित मोडेलसँग कुरा गर्नुहोस्

1. **Chat** चयन गर्नुहोस्।

    ![Select chat.](../../../../../../translated_images/ne/09-04-select-chat.61936dce6612a1e6.webp)

1. यहाँ परिणामहरूको उदाहरण छ: अब तपाईं आफ्नो अनुकूलित Phi-3 मोडेलसँग कुरा गर्न सक्नुहुन्छ। fine-tuning को लागि प्रयोग गरिएको डाटामा आधारित प्रश्नहरू सोध्न सिफारिस गरिन्छ।

    ![Chat with prompt flow.](../../../../../../translated_images/ne/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो कागजात AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा गलतफहमी हुन सक्छ। मूल कागजातलाई यसको मातृ भाषामा अधिकारिक स्रोत मानिनुपर्दछ। महत्त्वपूर्ण सूचनाका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->