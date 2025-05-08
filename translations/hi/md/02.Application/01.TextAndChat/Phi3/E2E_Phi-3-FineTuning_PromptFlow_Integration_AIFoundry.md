<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-08T05:48:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hi"
}
-->
# Azure AI Foundry में Prompt flow के साथ कस्टम Phi-3 मॉडल को फाइन-ट्यून और इंटीग्रेट करें

यह एंड-टू-एंड (E2E) उदाहरण Microsoft Tech Community के "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" गाइड पर आधारित है। यह कस्टम Phi-3 मॉडल को फाइन-ट्यून, डिप्लॉय और Azure AI Foundry में Prompt flow के साथ इंटीग्रेट करने की प्रक्रियाओं का परिचय देता है।  
इस E2E उदाहरण के विपरीत, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" जिसमें कोड लोकली चलाना शामिल था, यह ट्यूटोरियल पूरी तरह से Azure AI / ML Studio में आपके मॉडल को फाइन-ट्यून और इंटीग्रेट करने पर केंद्रित है।

## अवलोकन

इस E2E उदाहरण में, आप Phi-3 मॉडल को फाइन-ट्यून करना और इसे Azure AI Foundry में Prompt flow के साथ इंटीग्रेट करना सीखेंगे। Azure AI / ML Studio का उपयोग करके, आप कस्टम AI मॉडल को डिप्लॉय और उपयोग करने के लिए एक वर्कफ़्लो स्थापित करेंगे। यह E2E उदाहरण तीन परिदृश्यों में विभाजित है:

**परिदृश्य 1: Azure संसाधनों की सेटअप और फाइन-ट्यूनिंग की तैयारी**

**परिदृश्य 2: Phi-3 मॉडल का फाइन-ट्यून और Azure Machine Learning Studio में डिप्लॉयमेंट**

**परिदृश्य 3: Prompt flow के साथ इंटीग्रेशन और Azure AI Foundry में अपने कस्टम मॉडल के साथ चैट करना**

यहाँ इस E2E उदाहरण का एक संक्षिप्त परिचय है।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.hi.png)

### विषय सूची

1. **[परिदृश्य 1: Azure संसाधनों की सेटअप और फाइन-ट्यूनिंग की तैयारी](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace बनाएँ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription में GPU कोटा के लिए अनुरोध करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [रोल असाइनमेंट जोड़ें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [प्रोजेक्ट सेटअप करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[परिदृश्य 2: Phi-3 मॉडल का फाइन-ट्यून और Azure Machine Learning Studio में डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 मॉडल को फाइन-ट्यून करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल के साथ चैट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [अपने कस्टम Phi-3 मॉडल के साथ चैट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## परिदृश्य 1: Azure संसाधनों की सेटअप और फाइन-ट्यूनिंग की तैयारी

### Azure Machine Learning Workspace बनाएँ

1. पोर्टल पेज के शीर्ष पर **search bar** में *azure machine learning* टाइप करें और दिखाई देने वाले विकल्पों में से **Azure Machine Learning** चुनें।

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.hi.png)

2. नेविगेशन मेनू से **+ Create** चुनें।

3. नेविगेशन मेनू से **New workspace** चुनें।

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.hi.png)

4. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।  
    - उपयोग के लिए **Resource group** चुनें (आवश्यक हो तो नया बनाएं)।  
    - **Workspace Name** दर्ज करें। यह एक अद्वितीय नाम होना चाहिए।  
    - उपयोग करने के लिए **Region** चुनें।  
    - उपयोग के लिए **Storage account** चुनें (आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Key vault** चुनें (आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Application insights** चुनें (आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Container registry** चुनें (आवश्यक हो तो नया बनाएं)।  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.hi.png)

5. **Review + Create** चुनें।

6. **Create** चुनें।

### Azure Subscription में GPU कोटा के लिए अनुरोध करें

इस ट्यूटोरियल में, आप GPUs का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून और डिप्लॉय करना सीखेंगे। फाइन-ट्यूनिंग के लिए, आप *Standard_NC24ads_A100_v4* GPU का उपयोग करेंगे, जिसके लिए कोटा अनुरोध आवश्यक है। डिप्लॉयमेंट के लिए, आप *Standard_NC6s_v3* GPU का उपयोग करेंगे, जिसके लिए भी कोटा अनुरोध करना होगा।

> [!NOTE]  
> केवल Pay-As-You-Go सब्सक्रिप्शन (मानक सब्सक्रिप्शन प्रकार) GPU आवंटन के लिए पात्र हैं; लाभ सब्सक्रिप्शन फिलहाल समर्थित नहीं हैं।  
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. *Standard NCADSA100v4 Family* कोटा के लिए अनुरोध करने हेतु निम्नलिखित करें:

    - बाएँ टैब से **Quota** चुनें।  
    - उपयोग के लिए **Virtual machine family** चुनें। उदाहरण के लिए, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs*, जिसमें *Standard_NC24ads_A100_v4* GPU शामिल है।  
    - नेविगेशन मेनू से **Request quota** चुनें।  

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.hi.png)

    - Request quota पेज में, उपयोग के लिए **New cores limit** दर्ज करें। उदाहरण के लिए, 24।  
    - Request quota पेज में, GPU कोटा के लिए **Submit** चुनें।  

1. *Standard NCSv3 Family* कोटा के लिए अनुरोध करने हेतु निम्नलिखित करें:

    - बाएँ टैब से **Quota** चुनें।  
    - उपयोग के लिए **Virtual machine family** चुनें। उदाहरण के लिए, *Standard NCSv3 Family Cluster Dedicated vCPUs*, जिसमें *Standard_NC6s_v3* GPU शामिल है।  
    - नेविगेशन मेनू से **Request quota** चुनें।  
    - Request quota पेज में, उपयोग के लिए **New cores limit** दर्ज करें। उदाहरण के लिए, 24।  
    - Request quota पेज में, GPU कोटा के लिए **Submit** चुनें।  

### रोल असाइनमेंट जोड़ें

अपने मॉडल को फाइन-ट्यून और डिप्लॉय करने के लिए, आपको पहले एक User Assigned Managed Identity (UAI) बनानी होगी और उसे उचित अनुमतियाँ देनी होंगी। यह UAI डिप्लॉयमेंट के दौरान प्रमाणीकरण के लिए उपयोग की जाएगी।

#### User Assigned Managed Identity (UAI) बनाएँ

1. पोर्टल पेज के शीर्ष पर **search bar** में *managed identities* टाइप करें और दिखाई देने वाले विकल्पों में से **Managed Identities** चुनें।

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.hi.png)

1. **+ Create** चुनें।

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.hi.png)

1. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।  
    - उपयोग के लिए **Resource group** चुनें (आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Region** चुनें।  
    - **Name** दर्ज करें। यह एक अद्वितीय नाम होना चाहिए।  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.hi.png)

1. **Review + create** चुनें।

1. **+ Create** चुनें।

#### Managed Identity को Contributor रोल असाइनमेंट जोड़ें

1. उस Managed Identity संसाधन पर जाएं जिसे आपने बनाया है।

1. बाएँ टैब से **Azure role assignments** चुनें।

1. नेविगेशन मेनू से **+Add role assignment** चुनें।

1. Add role assignment पेज में निम्नलिखित करें:  
    - **Scope** को **Resource group** पर सेट करें।  
    - अपनी Azure **Subscription** चुनें।  
    - उपयोग के लिए **Resource group** चुनें।  
    - **Role** को **Contributor** पर सेट करें।  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.hi.png)

2. **Save** चुनें।

#### Managed Identity को Storage Blob Data Reader रोल असाइनमेंट जोड़ें

1. पोर्टल पेज के शीर्ष पर **search bar** में *storage accounts* टाइप करें और दिखाई देने वाले विकल्पों में से **Storage accounts** चुनें।

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.hi.png)

1. उस storage account को चुनें जो आपके Azure Machine Learning workspace से जुड़ा है। उदाहरण के लिए, *finetunephistorage*।

1. Add role assignment पेज पर जाने के लिए निम्नलिखित करें:

    - Azure Storage account पर जाएं जो आपने बनाया है।  
    - बाएँ टैब से **Access Control (IAM)** चुनें।  
    - नेविगेशन मेनू से **+ Add** चुनें।  
    - नेविगेशन मेनू से **Add role assignment** चुनें।  

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.hi.png)

1. Add role assignment पेज में निम्नलिखित करें:

    - Role पेज में, **search bar** में *Storage Blob Data Reader* टाइप करें और विकल्पों में से **Storage Blob Data Reader** चुनें।  
    - Role पेज में, **Next** चुनें।  
    - Members पेज में, **Assign access to** के रूप में **Managed identity** चुनें।  
    - Members पेज में, **+ Select members** चुनें।  
    - Select managed identities पेज में, अपनी Azure **Subscription** चुनें।  
    - Select managed identities पेज में, **Managed identity** के लिए **Manage Identity** चुनें।  
    - Select managed identities पेज में, आपने जो Managed Identity बनाई है उसे चुनें। उदाहरण के लिए, *finetunephi-managedidentity*।  
    - Select managed identities पेज में, **Select** चुनें।  

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.hi.png)

1. **Review + assign** चुनें।

#### Managed Identity को AcrPull रोल असाइनमेंट जोड़ें

1. पोर्टल पेज के शीर्ष पर **search bar** में *container registries* टाइप करें और दिखाई देने वाले विकल्पों में से **Container registries** चुनें।

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.hi.png)

1. उस container registry को चुनें जो आपके Azure Machine Learning workspace से जुड़ा है। उदाहरण के लिए, *finetunephicontainerregistry*

1. Add role assignment पेज पर जाने के लिए निम्नलिखित करें:

    - बाएँ टैब से **Access Control (IAM)** चुनें।  
    - नेविगेशन मेनू से **+ Add** चुनें।  
    - नेविगेशन मेनू से **Add role assignment** चुनें।  

1. Add role assignment पेज में निम्नलिखित करें:

    - Role पेज में, **search bar** में *AcrPull* टाइप करें और विकल्पों में से **AcrPull** चुनें।  
    - Role पेज में, **Next** चुनें।  
    - Members पेज में, **Assign access to** के रूप में **Managed identity** चुनें।  
    - Members पेज में, **+ Select members** चुनें।  
    - Select managed identities पेज में, अपनी Azure **Subscription** चुनें।  
    - Select managed identities पेज में, **Managed identity** के लिए **Manage Identity** चुनें।  
    - Select managed identities पेज में, आपने जो Managed Identity बनाई है उसे चुनें। उदाहरण के लिए, *finetunephi-managedidentity*।  
    - Select managed identities पेज में, **Select** चुनें।  
    - **Review + assign** चुनें।  

### प्रोजेक्ट सेटअप करें

फाइन-ट्यूनिंग के लिए आवश्यक डेटासेट डाउनलोड करने के लिए, आप एक लोकल एनवायरनमेंट सेटअप करेंगे।

इस अभ्यास में, आप:

- काम करने के लिए एक फोल्डर बनाएंगे।  
- एक वर्चुअल एनवायरनमेंट बनाएंगे।  
- आवश्यक पैकेज इंस्टॉल करेंगे।  
- डेटासेट डाउनलोड करने के लिए *download_dataset.py* फाइल बनाएंगे।  

#### काम करने के लिए फोल्डर बनाएँ

1. टर्मिनल विंडो खोलें और डिफ़ॉल्ट पथ में *finetune-phi* नामक फोल्डर बनाने के लिए निम्न कमांड टाइप करें।

    ```console
    mkdir finetune-phi
    ```

2. टर्मिनल में निम्न कमांड टाइप करके *finetune-phi* फोल्डर में जाएं।

    ```console
    cd finetune-phi
    ```

#### वर्चुअल एनवायरनमेंट बनाएँ

1. टर्मिनल में निम्न कमांड टाइप करके *.venv* नामक वर्चुअल एनवायरनमेंट बनाएँ।

    ```console
    python -m venv .venv
    ```

2. टर्मिनल में निम्न कमांड टाइप करके वर्चुअल एनवायरनमेंट को सक्रिय करें।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> यदि यह सफल रहा, तो कमांड प्रॉम्प्ट के पहले *(.venv)* दिखाई देगा।

#### आवश्यक पैकेज इंस्टॉल करें

1. टर्मिनल में निम्न कमांड टाइप करके आवश्यक पैकेज इंस्टॉल करें।

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` बनाएँ

> [!NOTE]  
> पूर्ण फोल्डर संरचना:  
>  
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** खोलें।

1. मेनू बार से **File** चुनें।

1. **Open Folder** चुनें।

1. उस *finetune-phi* फोल्डर को चुनें जो आपने बनाया है, जो *C:\Users\yourUserName\finetune-phi* में स्थित है।

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.hi.png)

1. Visual Studio Code के बाएँ पेन में, राइट-क्लिक करें और **New File** चुनें, फिर *download_dataset.py* नामक नई फाइल बनाएं।

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.hi.png)

### फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें

इस अभ्यास में, आप *download_dataset.py* फाइल चलाकर *ultrachat_200k* डेटासेट को अपने लोकल एनवायरनमेंट में डाउनलोड करेंगे। फिर आप इस डेटासेट का उपयोग Azure Machine Learning में Phi-3 मॉडल को फाइन-ट्यून करने के लिए करेंगे।

इस अभ्यास में, आप:

- *download_dataset.py* फाइल में कोड जोड़ेंगे ताकि डेटासेट डाउनलोड हो सके।  
- *download_dataset.py* फाइल चलाकर डेटासेट को अपने लोकल एनवायरनमेंट में डाउनलोड करेंगे।  

#### *download_dataset.py* का उपयोग करके डेटासेट डाउनलोड करें

1. Visual Studio Code में *download_dataset.py* फाइल खोलें।

1. *download_dataset.py* फाइल में निम्नलिखित कोड जोड़ें।

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. टर्मिनल में निम्न कमांड टाइप करके स्क्रिप्ट चलाएं और डेटासेट अपने लोकल एनवायरनमेंट में डाउनलोड करें।

    ```console
    python download_dataset.py
    ```

1. सुनिश्चित करें कि डेटासेट सफलतापूर्वक आपके लोकल *finetune-phi/data* डायरेक्टरी में सेव हो गया है।

> [!NOTE]  
> #### डेटासेट साइज और फाइन-ट्यूनिंग समय पर नोट  

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. बाईं तरफ के टैब से **Compute** चुनें।

1. नेविगेशन मेनू से **Compute clusters** चुनें।

1. **+ New** चुनें।

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.hi.png)

1. निम्न कार्य करें:

    - उस **Region** को चुनें जिसे आप उपयोग करना चाहते हैं।
    - **Virtual machine tier** को **Dedicated** पर सेट करें।
    - **Virtual machine type** को **GPU** पर सेट करें।
    - **Virtual machine size** फ़िल्टर को **Select from all options** पर सेट करें।
    - **Virtual machine size** को **Standard_NC24ads_A100_v4** चुनें।

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.hi.png)

1. **Next** चुनें।

1. निम्न कार्य करें:

    - **Compute name** दर्ज करें। यह एक अनूठा नाम होना चाहिए।
    - **Minimum number of nodes** को **0** पर सेट करें।
    - **Maximum number of nodes** को **1** पर सेट करें।
    - **Idle seconds before scale down** को **120** पर सेट करें।

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.hi.png)

1. **Create** चुनें।

#### Phi-3 मॉडल का फाइन-ट्यून करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. उस Azure Machine Learning workspace को चुनें जिसे आपने बनाया था।

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hi.png)

1. निम्न कार्य करें:

    - बाईं तरफ के टैब से **Model catalog** चुनें।
    - **search bar** में *phi-3-mini-4k* टाइप करें और दिखाई देने वाले विकल्पों में से **Phi-3-mini-4k-instruct** चुनें।

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.hi.png)

1. नेविगेशन मेनू से **Fine-tune** चुनें।

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.hi.png)

1. निम्न कार्य करें:

    - **Select task type** को **Chat completion** पर सेट करें।
    - **+ Select data** पर क्लिक करके **Traning data** अपलोड करें।
    - Validation data अपलोड प्रकार को **Provide different validation data** पर सेट करें।
    - **+ Select data** पर क्लिक करके **Validation data** अपलोड करें।

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.hi.png)

    > [!TIP]
    >
    > आप **Advanced settings** चुनकर **learning_rate** और **lr_scheduler_type** जैसी सेटिंग्स को कस्टमाइज़ कर सकते हैं ताकि फाइन-ट्यूनिंग प्रक्रिया को अपनी आवश्यकताओं के अनुसार बेहतर बनाया जा सके।

1. **Finish** चुनें।

1. इस अभ्यास में, आपने सफलतापूर्वक Azure Machine Learning का उपयोग करके Phi-3 मॉडल का फाइन-ट्यून किया है। कृपया ध्यान दें कि फाइन-ट्यूनिंग प्रक्रिया में काफी समय लग सकता है। फाइन-ट्यूनिंग जॉब चलाने के बाद, इसे पूरा होने तक प्रतीक्षा करें। आप अपने Azure Machine Learning Workspace के बाईं तरफ के Jobs टैब में जाकर फाइन-ट्यूनिंग जॉब की स्थिति मॉनिटर कर सकते हैं। अगले भाग में, आप फाइन-ट्यून किए गए मॉडल को डिप्लॉय करेंगे और इसे Prompt flow के साथ इंटीग्रेट करेंगे।

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.hi.png)

### फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करें

फाइन-ट्यून किए गए Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करने के लिए, आपको मॉडल को डिप्लॉय करना होगा ताकि वह रियल-टाइम इनफेरेंस के लिए उपलब्ध हो सके। इस प्रक्रिया में मॉडल का रजिस्ट्रेशन, एक ऑनलाइन एंडपॉइंट बनाना, और मॉडल को डिप्लॉय करना शामिल है।

इस अभ्यास में, आप:

- Azure Machine Learning workspace में फाइन-ट्यून किए गए मॉडल को रजिस्टर करेंगे।
- एक ऑनलाइन एंडपॉइंट बनाएंगे।
- रजिस्टर किए गए फाइन-ट्यून Phi-3 मॉडल को डिप्लॉय करेंगे।

#### फाइन-ट्यून किए गए मॉडल को रजिस्टर करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. उस Azure Machine Learning workspace को चुनें जिसे आपने बनाया था।

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hi.png)

1. बाईं तरफ के टैब से **Models** चुनें।
1. **+ Register** चुनें।
1. **From a job output** चुनें।

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.hi.png)

1. उस जॉब को चुनें जिसे आपने बनाया था।

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.hi.png)

1. **Next** चुनें।

1. **Model type** को **MLflow** पर सेट करें।

1. सुनिश्चित करें कि **Job output** चयनित है; यह स्वचालित रूप से चुना जाना चाहिए।

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.hi.png)

2. **Next** चुनें।

3. **Register** चुनें।

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.hi.png)

4. आप अपने रजिस्टर किए गए मॉडल को बाईं तरफ के टैब में **Models** मेनू से देख सकते हैं।

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.hi.png)

#### फाइन-ट्यून किए गए मॉडल को डिप्लॉय करें

1. उस Azure Machine Learning workspace पर जाएं जिसे आपने बनाया था।

1. बाईं तरफ के टैब से **Endpoints** चुनें।

1. नेविगेशन मेनू से **Real-time endpoints** चुनें।

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.hi.png)

1. **Create** चुनें।

1. अपने रजिस्टर किए गए मॉडल को चुनें।

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.hi.png)

1. **Select** चुनें।

1. निम्न कार्य करें:

    - **Virtual machine** को *Standard_NC6s_v3* पर सेट करें।
    - उपयोग करने के लिए **Instance count** चुनें, जैसे *1*।
    - **Endpoint** को **New** पर सेट करें ताकि नया एंडपॉइंट बनाया जा सके।
    - **Endpoint name** दर्ज करें। यह अनूठा होना चाहिए।
    - **Deployment name** दर्ज करें। यह भी अनूठा होना चाहिए।

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.hi.png)

1. **Deploy** चुनें।

> [!WARNING]
> अपने खाते पर अतिरिक्त शुल्क से बचने के लिए, कृपया Azure Machine Learning workspace में बनाए गए एंडपॉइंट को डिलीट करना न भूलें।
>

#### Azure Machine Learning Workspace में डिप्लॉयमेंट की स्थिति जांचें

1. उस Azure Machine Learning workspace पर जाएं जिसे आपने बनाया था।

1. बाईं तरफ के टैब से **Endpoints** चुनें।

1. उस एंडपॉइंट को चुनें जिसे आपने बनाया था।

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.hi.png)

1. इस पेज पर, आप डिप्लॉयमेंट प्रक्रिया के दौरान एंडपॉइंट्स का प्रबंधन कर सकते हैं।

> [!NOTE]
> डिप्लॉयमेंट पूरा होने के बाद, सुनिश्चित करें कि **Live traffic** **100%** पर सेट है। यदि नहीं है, तो ट्रैफ़िक सेटिंग्स को समायोजित करने के लिए **Update traffic** चुनें। ध्यान दें कि यदि ट्रैफ़िक 0% पर है, तो आप मॉडल का परीक्षण नहीं कर सकते।
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.hi.png)
>

## परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल से चैट करें

### कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करें

अपने फाइन-ट्यून किए गए मॉडल को सफलतापूर्वक डिप्लॉय करने के बाद, अब आप इसे Prompt Flow के साथ इंटीग्रेट कर सकते हैं ताकि आप अपने मॉडल का रियल-टाइम एप्लिकेशन में उपयोग कर सकें, जिससे आपके कस्टम Phi-3 मॉडल के साथ विभिन्न इंटरैक्टिव टास्क संभव हो सकें।

इस अभ्यास में, आप:

- Azure AI Foundry Hub बनाएंगे।
- Azure AI Foundry प्रोजेक्ट बनाएंगे।
- Prompt flow बनाएंगे।
- फाइन-ट्यून किए गए Phi-3 मॉडल के लिए कस्टम कनेक्शन जोड़ेंगे।
- अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए Prompt flow सेटअप करेंगे।

> [!NOTE]
> आप Azure ML Studio का उपयोग करके भी Promptflow के साथ इंटीग्रेशन कर सकते हैं। यह इंटीग्रेशन प्रक्रिया Azure ML Studio पर भी समान रूप से लागू होती है।

#### Azure AI Foundry Hub बनाएँ

प्रोजेक्ट बनाने से पहले आपको एक Hub बनाना होगा। Hub एक Resource Group की तरह काम करता है, जो Azure AI Foundry के भीतर कई प्रोजेक्ट्स को व्यवस्थित और प्रबंधित करने की सुविधा देता है।

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. बाईं तरफ के टैब से **All hubs** चुनें।

1. नेविगेशन मेनू से **+ New hub** चुनें।

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.hi.png)

1. निम्न कार्य करें:

    - **Hub name** दर्ज करें। यह एक अनूठा नाम होना चाहिए।
    - अपनी Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - उपयोग करने के लिए **Location** चुनें।
    - उपयोग करने के लिए **Connect Azure AI Services** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - **Connect Azure AI Search** को **Skip connecting** पर सेट करें।

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.hi.png)

1. **Next** चुनें।

#### Azure AI Foundry प्रोजेक्ट बनाएँ

1. आपने जो Hub बनाया है, उसमें बाईं तरफ के टैब से **All projects** चुनें।

1. नेविगेशन मेनू से **+ New project** चुनें।

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.hi.png)

1. **Project name** दर्ज करें। यह अनूठा होना चाहिए।

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.hi.png)

1. **Create a project** चुनें।

#### फाइन-ट्यून किए गए Phi-3 मॉडल के लिए कस्टम कनेक्शन जोड़ें

अपने कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करने के लिए, आपको मॉडल के एंडपॉइंट और की को एक कस्टम कनेक्शन में सेव करना होगा। यह सेटअप Prompt flow में आपके कस्टम Phi-3 मॉडल तक पहुँच सुनिश्चित करता है।

#### फाइन-ट्यून किए गए Phi-3 मॉडल की api key और endpoint uri सेट करें

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. उस Azure Machine Learning workspace में नेविगेट करें जिसे आपने बनाया था।

1. बाईं तरफ के टैब से **Endpoints** चुनें।

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.hi.png)

1. उस एंडपॉइंट को चुनें जिसे आपने बनाया था।

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.hi.png)

1. नेविगेशन मेनू से **Consume** चुनें।

1. अपना **REST endpoint** और **Primary key** कॉपी करें।
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.hi.png)

#### कस्टम कनेक्शन जोड़ें

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. उस Azure AI Foundry प्रोजेक्ट पर नेविगेट करें जिसे आपने बनाया है।

1. अपने बनाए गए प्रोजेक्ट में, बाएँ साइड टैब से **Settings** चुनें।

1. **+ New connection** चुनें।

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.hi.png)

1. नेविगेशन मेनू से **Custom keys** चुनें।

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.hi.png)

1. निम्न कार्य करें:

    - **+ Add key value pairs** चुनें।
    - key नाम के लिए **endpoint** दर्ज करें और Azure ML Studio से कॉपी किया गया endpoint value फ़ील्ड में पेस्ट करें।
    - फिर से **+ Add key value pairs** चुनें।
    - key नाम के लिए **key** दर्ज करें और Azure ML Studio से कॉपी किया गया key value फ़ील्ड में पेस्ट करें।
    - keys जोड़ने के बाद, key को एक्सपोज़ होने से रोकने के लिए **is secret** चुनें।

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.hi.png)

1. **Add connection** चुनें।

#### Prompt flow बनाएं

आपने Azure AI Foundry में एक कस्टम कनेक्शन जोड़ दिया है। अब, निम्न चरणों का पालन करके एक Prompt flow बनाएं। फिर, आप इस Prompt flow को कस्टम कनेक्शन से जोड़ेंगे ताकि आप fine-tuned मॉडल का उपयोग Prompt flow के भीतर कर सकें।

1. उस Azure AI Foundry प्रोजेक्ट पर जाएं जिसे आपने बनाया है।

1. बाएँ साइड टैब से **Prompt flow** चुनें।

1. नेविगेशन मेनू से **+ Create** चुनें।

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.hi.png)

1. नेविगेशन मेनू से **Chat flow** चुनें।

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.hi.png)

1. उपयोग के लिए **Folder name** दर्ज करें।

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.hi.png)

2. **Create** चुनें।

#### अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए Prompt flow सेट करें

आपको fine-tuned Phi-3 मॉडल को Prompt flow में इंटीग्रेट करना होगा। हालांकि, मौजूदा Prompt flow इस उद्देश्य के लिए डिज़ाइन नहीं किया गया है। इसलिए, आपको कस्टम मॉडल को इंटीग्रेट करने के लिए Prompt flow को फिर से डिज़ाइन करना होगा।

1. Prompt flow में, मौजूदा flow को पुनर्निर्मित करने के लिए निम्न कार्य करें:

    - **Raw file mode** चुनें।
    - *flow.dag.yml* फ़ाइल में मौजूद सभी कोड हटा दें।
    - *flow.dag.yml* फ़ाइल में निम्न कोड जोड़ें।

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

    - **Save** चुनें।

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.hi.png)

1. कस्टम Phi-3 मॉडल को Prompt flow में उपयोग करने के लिए *integrate_with_promptflow.py* फ़ाइल में निम्न कोड जोड़ें।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.hi.png)

> [!NOTE]
> Azure AI Foundry में Prompt flow का उपयोग करने के लिए अधिक विस्तृत जानकारी के लिए, आप [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) देख सकते हैं।

1. अपने मॉडल के साथ चैट सक्षम करने के लिए **Chat input**, **Chat output** चुनें।

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.hi.png)

1. अब आप अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए तैयार हैं। अगले अभ्यास में, आप सीखेंगे कि Prompt flow कैसे शुरू करें और इसका उपयोग अपने fine-tuned Phi-3 मॉडल के साथ चैट करने के लिए कैसे करें।

> [!NOTE]
>
> पुनर्निर्मित flow नीचे दी गई छवि जैसा दिखना चाहिए:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.hi.png)
>

### अपने कस्टम Phi-3 मॉडल के साथ चैट करें

अब जब आपने अपने कस्टम Phi-3 मॉडल को fine-tune और Prompt flow के साथ इंटीग्रेट कर लिया है, तो आप इसके साथ बातचीत शुरू करने के लिए तैयार हैं। यह अभ्यास आपको Prompt flow का उपयोग करके अपने मॉडल के साथ चैट सेटअप और शुरू करने की प्रक्रिया में मार्गदर्शन करेगा। इन चरणों का पालन करके, आप अपने fine-tuned Phi-3 मॉडल की क्षमताओं का पूर्ण उपयोग विभिन्न कार्यों और संवादों के लिए कर सकेंगे।

- Prompt flow का उपयोग करके अपने कस्टम Phi-3 मॉडल के साथ चैट करें।

#### Prompt flow शुरू करें

1. Prompt flow शुरू करने के लिए **Start compute sessions** चुनें।

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.hi.png)

1. पैरामीटर नवीनीकरण के लिए **Validate and parse input** चुनें।

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.hi.png)

1. आपने जो कस्टम कनेक्शन बनाया है, उसे **connection** के **Value** में चुनें। उदाहरण के लिए, *connection*।

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.hi.png)

#### अपने कस्टम मॉडल के साथ चैट करें

1. **Chat** चुनें।

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.hi.png)

1. यहाँ परिणामों का एक उदाहरण है: अब आप अपने कस्टम Phi-3 मॉडल के साथ चैट कर सकते हैं। सुझाव दिया जाता है कि fine-tuning के लिए उपयोग किए गए डेटा के आधार पर प्रश्न पूछें।

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.hi.png)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।