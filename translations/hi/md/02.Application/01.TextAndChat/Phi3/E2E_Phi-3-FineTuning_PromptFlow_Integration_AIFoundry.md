<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:13:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hi"
}
-->
# Azure AI Foundry में Prompt flow के साथ कस्टम Phi-3 मॉडल को फाइन-ट्यून और इंटीग्रेट करें

यह एंड-टू-एंड (E2E) उदाहरण Microsoft Tech Community के गाइड "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" पर आधारित है। यह कस्टम Phi-3 मॉडल को फाइन-ट्यून करने, डिप्लॉय करने और Azure AI Foundry में Prompt flow के साथ इंटीग्रेट करने की प्रक्रियाओं को प्रस्तुत करता है।  
E2E उदाहरण "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" के विपरीत, जिसमें कोड लोकली चलाया गया था, यह ट्यूटोरियल पूरी तरह से Azure AI / ML Studio के भीतर आपके मॉडल को फाइन-ट्यून और इंटीग्रेट करने पर केंद्रित है।

## अवलोकन

इस E2E उदाहरण में, आप Phi-3 मॉडल को फाइन-ट्यून करना और Azure AI Foundry में Prompt flow के साथ इंटीग्रेट करना सीखेंगे। Azure AI / ML Studio का उपयोग करके, आप कस्टम AI मॉडल को डिप्लॉय और उपयोग करने के लिए एक वर्कफ़्लो स्थापित करेंगे। यह E2E उदाहरण तीन परिदृश्यों में विभाजित है:

**परिदृश्य 1: Azure संसाधनों की सेटअप और फाइन-ट्यूनिंग की तैयारी**

**परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में डिप्लॉय करें**

**परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल के साथ चैट करें**

यहाँ इस E2E उदाहरण का एक संक्षिप्त अवलोकन है।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.hi.png)

### सामग्री तालिका

1. **[परिदृश्य 1: Azure संसाधनों की सेटअप और फाइन-ट्यूनिंग की तैयारी](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace बनाएं](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription में GPU कोटा का अनुरोध करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [रोल असाइनमेंट जोड़ें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [प्रोजेक्ट सेटअप करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 मॉडल को फाइन-ट्यून करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल के साथ चैट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [अपने कस्टम Phi-3 मॉडल के साथ चैट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## परिदृश्य 1: Azure संसाधनों की सेटअप और फाइन-ट्यूनिंग की तैयारी

### Azure Machine Learning Workspace बनाएं

1. पोर्टल पेज के शीर्ष पर **search bar** में *azure machine learning* टाइप करें और दिखाई देने वाले विकल्पों में से **Azure Machine Learning** चुनें।

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.hi.png)

2. नेविगेशन मेनू से **+ Create** चुनें।

3. नेविगेशन मेनू से **New workspace** चुनें।

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.hi.png)

4. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।  
    - उपयोग के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।  
    - **Workspace Name** दर्ज करें। यह एक अनूठा नाम होना चाहिए।  
    - उपयोग के लिए **Region** चुनें।  
    - उपयोग के लिए **Storage account** चुनें (यदि आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Key vault** चुनें (यदि आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Application insights** चुनें (यदि आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Container registry** चुनें (यदि आवश्यक हो तो नया बनाएं)।  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.hi.png)

5. **Review + Create** चुनें।

6. **Create** चुनें।

### Azure Subscription में GPU कोटा का अनुरोध करें

इस ट्यूटोरियल में, आप GPUs का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून और डिप्लॉय करना सीखेंगे। फाइन-ट्यूनिंग के लिए, आप *Standard_NC24ads_A100_v4* GPU का उपयोग करेंगे, जिसके लिए कोटा अनुरोध आवश्यक है। डिप्लॉयमेंट के लिए, आप *Standard_NC6s_v3* GPU का उपयोग करेंगे, जिसके लिए भी कोटा अनुरोध करना होगा।

> [!NOTE]
>
> केवल Pay-As-You-Go सब्सक्रिप्शन (मानक सब्सक्रिप्शन प्रकार) GPU आवंटन के लिए पात्र हैं; लाभ सब्सक्रिप्शन वर्तमान में समर्थित नहीं हैं।
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. *Standard NCADSA100v4 Family* कोटा का अनुरोध करने के लिए निम्नलिखित करें:

    - बाएं साइड टैब से **Quota** चुनें।  
    - उपयोग के लिए **Virtual machine family** चुनें। उदाहरण के लिए, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, जिसमें *Standard_NC24ads_A100_v4* GPU शामिल है।  
    - नेविगेशन मेनू से **Request quota** चुनें।  

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.hi.png)

    - Request quota पेज में, आप जितने कोर उपयोग करना चाहते हैं वह **New cores limit** में दर्ज करें। उदाहरण के लिए, 24।  
    - Request quota पेज में, GPU कोटा का अनुरोध करने के लिए **Submit** चुनें।  

1. *Standard NCSv3 Family* कोटा का अनुरोध करने के लिए निम्नलिखित करें:

    - बाएं साइड टैब से **Quota** चुनें।  
    - उपयोग के लिए **Virtual machine family** चुनें। उदाहरण के लिए, **Standard NCSv3 Family Cluster Dedicated vCPUs**, जिसमें *Standard_NC6s_v3* GPU शामिल है।  
    - नेविगेशन मेनू से **Request quota** चुनें।  
    - Request quota पेज में, आप जितने कोर उपयोग करना चाहते हैं वह **New cores limit** में दर्ज करें। उदाहरण के लिए, 24।  
    - Request quota पेज में, GPU कोटा का अनुरोध करने के लिए **Submit** चुनें।  

### रोल असाइनमेंट जोड़ें

अपने मॉडल को फाइन-ट्यून और डिप्लॉय करने के लिए, आपको पहले एक User Assigned Managed Identity (UAI) बनानी होगी और उसे उचित अनुमतियाँ देनी होंगी। यह UAI डिप्लॉयमेंट के दौरान प्रमाणीकरण के लिए उपयोग की जाएगी।

#### User Assigned Managed Identity (UAI) बनाएं

1. पोर्टल पेज के शीर्ष पर **search bar** में *managed identities* टाइप करें और दिखाई देने वाले विकल्पों में से **Managed Identities** चुनें।

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.hi.png)

1. **+ Create** चुनें।

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.hi.png)

1. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।  
    - उपयोग के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।  
    - उपयोग के लिए **Region** चुनें।  
    - **Name** दर्ज करें। यह एक अनूठा नाम होना चाहिए।  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.hi.png)

1. **Review + create** चुनें।

1. **+ Create** चुनें।

#### Managed Identity को Contributor रोल असाइनमेंट जोड़ें

1. उस Managed Identity संसाधन पर जाएं जिसे आपने बनाया है।

1. बाएं साइड टैब से **Azure role assignments** चुनें।

1. नेविगेशन मेनू से **+Add role assignment** चुनें।

1. Add role assignment पेज में निम्नलिखित करें:  
    - **Scope** को **Resource group** पर सेट करें।  
    - अपनी Azure **Subscription** चुनें।  
    - उपयोग के लिए **Resource group** चुनें।  
    - **Role** को **Contributor** पर सेट करें।  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.hi.png)

2. **Save** चुनें।

#### Managed Identity को Storage Blob Data Reader रोल असाइनमेंट जोड़ें

1. पोर्टल पेज के शीर्ष पर **search bar** में *storage accounts* टाइप करें और दिखाई देने वाले विकल्पों में से **Storage accounts** चुनें।

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.hi.png)

1. उस स्टोरेज अकाउंट को चुनें जो आपने Azure Machine Learning workspace के साथ जोड़ा है। उदाहरण के लिए, *finetunephistorage*।

1. Add role assignment पेज पर जाने के लिए निम्नलिखित करें:

    - उस Azure Storage अकाउंट पर जाएं जिसे आपने बनाया है।  
    - बाएं साइड टैब से **Access Control (IAM)** चुनें।  
    - नेविगेशन मेनू से **+ Add** चुनें।  
    - नेविगेशन मेनू से **Add role assignment** चुनें।  

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.hi.png)

1. Add role assignment पेज में निम्नलिखित करें:

    - Role पेज में, **search bar** में *Storage Blob Data Reader* टाइप करें और विकल्पों में से **Storage Blob Data Reader** चुनें।  
    - Role पेज में, **Next** चुनें।  
    - Members पेज में, **Assign access to** के लिए **Managed identity** चुनें।  
    - Members पेज में, **+ Select members** चुनें।  
    - Select managed identities पेज में, अपनी Azure **Subscription** चुनें।  
    - Select managed identities पेज में, **Managed identity** के लिए **Manage Identity** चुनें।  
    - Select managed identities पेज में, आपने जो Managed Identity बनाई है उसे चुनें। उदाहरण के लिए, *finetunephi-managedidentity*।  
    - Select managed identities पेज में, **Select** चुनें।  

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.hi.png)

1. **Review + assign** चुनें।

#### Managed Identity को AcrPull रोल असाइनमेंट जोड़ें

1. पोर्टल पेज के शीर्ष पर **search bar** में *container registries* टाइप करें और दिखाई देने वाले विकल्पों में से **Container registries** चुनें।

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.hi.png)

1. उस कंटेनर रजिस्ट्री को चुनें जो Azure Machine Learning workspace के साथ जुड़ा है। उदाहरण के लिए, *finetunephicontainerregistry*

1. Add role assignment पेज पर जाने के लिए निम्नलिखित करें:

    - बाएं साइड टैब से **Access Control (IAM)** चुनें।  
    - नेविगेशन मेनू से **+ Add** चुनें।  
    - नेविगेशन मेनू से **Add role assignment** चुनें।  

1. Add role assignment पेज में निम्नलिखित करें:

    - Role पेज में, **search bar** में *AcrPull* टाइप करें और विकल्पों में से **AcrPull** चुनें।  
    - Role पेज में, **Next** चुनें।  
    - Members पेज में, **Assign access to** के लिए **Managed identity** चुनें।  
    - Members पेज में, **+ Select members** चुनें।  
    - Select managed identities पेज में, अपनी Azure **Subscription** चुनें।  
    - Select managed identities पेज में, **Managed identity** के लिए **Manage Identity** चुनें।  
    - Select managed identities पेज में, आपने जो Managed Identity बनाई है उसे चुनें। उदाहरण के लिए, *finetunephi-managedidentity*।  
    - Select managed identities पेज में, **Select** चुनें।  
    - **Review + assign** चुनें।

### प्रोजेक्ट सेटअप करें

फाइन-ट्यूनिंग के लिए आवश्यक डेटासेट डाउनलोड करने के लिए, आप एक लोकल वातावरण सेटअप करेंगे।

इस अभ्यास में, आप

- काम करने के लिए एक फोल्डर बनाएंगे।  
- एक वर्चुअल एनवायरनमेंट बनाएंगे।  
- आवश्यक पैकेज इंस्टॉल करेंगे।  
- डेटासेट डाउनलोड करने के लिए *download_dataset.py* फाइल बनाएंगे।

#### काम करने के लिए एक फोल्डर बनाएं

1. एक टर्मिनल विंडो खोलें और डिफ़ॉल्ट पथ में *finetune-phi* नाम का फोल्डर बनाने के लिए निम्न कमांड टाइप करें।

    ```console
    mkdir finetune-phi
    ```

2. टर्मिनल में निम्न कमांड टाइप करके *finetune-phi* फोल्डर में जाएं जो आपने बनाया है।
#### वर्चुअल एनवायरनमेंट बनाएं

1. अपने टर्मिनल में निम्न कमांड टाइप करें ताकि *.venv* नाम का वर्चुअल एनवायरनमेंट बनाया जा सके।

    ```console
    python -m venv .venv
    ```

2. अपने टर्मिनल में निम्न कमांड टाइप करें ताकि वर्चुअल एनवायरनमेंट सक्रिय हो सके।

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> यदि यह सफल रहा, तो कमांड प्रॉम्प्ट से पहले *(.venv)* दिखाई देगा।

#### आवश्यक पैकेज इंस्टॉल करें

1. अपने टर्मिनल में निम्न कमांड टाइप करें ताकि आवश्यक पैकेज इंस्टॉल हो सकें।

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` बनाएं

> [!NOTE]
> पूरा फोल्डर स्ट्रक्चर:
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

    ![अपने बनाए हुए फोल्डर को चुनें।](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.hi.png)

1. Visual Studio Code के बाएं पैनल में, राइट-क्लिक करें और **New File** चुनें ताकि *download_dataset.py* नाम की नई फाइल बनाई जा सके।

    ![नई फाइल बनाएं।](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.hi.png)

### फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें

इस अभ्यास में, आप *download_dataset.py* फाइल चलाकर *ultrachat_200k* डेटासेट को अपने लोकल एनवायरनमेंट में डाउनलोड करेंगे। फिर आप इस डेटासेट का उपयोग Azure Machine Learning में Phi-3 मॉडल को फाइन-ट्यून करने के लिए करेंगे।

इस अभ्यास में, आप:

- *download_dataset.py* फाइल में कोड जोड़ेंगे ताकि डेटासेट डाउनलोड हो सके।
- *download_dataset.py* फाइल चलाकर डेटासेट को अपने लोकल एनवायरनमेंट में डाउनलोड करेंगे।

#### *download_dataset.py* का उपयोग करके अपना डेटासेट डाउनलोड करें

1. Visual Studio Code में *download_dataset.py* फाइल खोलें।

1. *download_dataset.py* फाइल में निम्न कोड जोड़ें।

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

1. अपने टर्मिनल में निम्न कमांड टाइप करें ताकि स्क्रिप्ट चले और डेटासेट आपके लोकल एनवायरनमेंट में डाउनलोड हो जाए।

    ```console
    python download_dataset.py
    ```

1. सुनिश्चित करें कि डेटासेट सफलतापूर्वक आपके लोकल *finetune-phi/data* डायरेक्टरी में सेव हो गया है।

> [!NOTE]
>
> #### डेटासेट के आकार और फाइन-ट्यूनिंग समय पर नोट
>
> इस ट्यूटोरियल में, आप केवल डेटासेट का 1% (`split='train[:1%]'`) उपयोग करते हैं। इससे डेटा की मात्रा काफी कम हो जाती है, जिससे अपलोड और फाइन-ट्यूनिंग दोनों प्रक्रियाएं तेज़ हो जाती हैं। आप प्रशिक्षण समय और मॉडल प्रदर्शन के बीच सही संतुलन खोजने के लिए प्रतिशत को समायोजित कर सकते हैं। डेटासेट के छोटे हिस्से का उपयोग करने से फाइन-ट्यूनिंग का समय कम हो जाता है, जिससे यह ट्यूटोरियल के लिए अधिक प्रबंधनीय हो जाता है।

## परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में डिप्लॉय करें

### Phi-3 मॉडल को फाइन-ट्यून करें

इस अभ्यास में, आप Azure Machine Learning Studio में Phi-3 मॉडल को फाइन-ट्यून करेंगे।

इस अभ्यास में, आप:

- फाइन-ट्यूनिंग के लिए कंप्यूटर क्लस्टर बनाएंगे।
- Azure Machine Learning Studio में Phi-3 मॉडल को फाइन-ट्यून करेंगे।

#### फाइन-ट्यूनिंग के लिए कंप्यूटर क्लस्टर बनाएं

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. बाएं साइड टैब से **Compute** चुनें।

1. नेविगेशन मेनू से **Compute clusters** चुनें।

1. **+ New** चुनें।

    ![Compute चुनें।](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.hi.png)

1. निम्न कार्य करें:

    - वह **Region** चुनें जिसे आप उपयोग करना चाहते हैं।
    - **Virtual machine tier** को **Dedicated** पर सेट करें।
    - **Virtual machine type** को **GPU** पर सेट करें।
    - **Virtual machine size** फिल्टर को **Select from all options** पर सेट करें।
    - **Virtual machine size** को **Standard_NC24ads_A100_v4** चुनें।

    ![क्लस्टर बनाएं।](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.hi.png)

1. **Next** चुनें।

1. निम्न कार्य करें:

    - **Compute name** दर्ज करें। यह एक अनूठा नाम होना चाहिए।
    - **Minimum number of nodes** को **0** पर सेट करें।
    - **Maximum number of nodes** को **1** पर सेट करें।
    - **Idle seconds before scale down** को **120** पर सेट करें।

    ![क्लस्टर बनाएं।](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.hi.png)

1. **Create** चुनें।

#### Phi-3 मॉडल को फाइन-ट्यून करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. उस Azure Machine Learning वर्कस्पेस को चुनें जिसे आपने बनाया है।

    ![अपने बनाए हुए वर्कस्पेस को चुनें।](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.hi.png)

1. निम्न कार्य करें:

    - बाएं साइड टैब से **Model catalog** चुनें।
    - **search bar** में *phi-3-mini-4k* टाइप करें और दिखाई देने वाले विकल्पों में से **Phi-3-mini-4k-instruct** चुनें।

    ![phi-3-mini-4k टाइप करें।](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.hi.png)

1. नेविगेशन मेनू से **Fine-tune** चुनें।

    ![Fine tune चुनें।](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.hi.png)

1. निम्न कार्य करें:

    - **Select task type** को **Chat completion** पर सेट करें।
    - **+ Select data** पर क्लिक करके **Training data** अपलोड करें।
    - Validation data अपलोड प्रकार को **Provide different validation data** पर सेट करें।
    - **+ Select data** पर क्लिक करके **Validation data** अपलोड करें।

    ![फाइन-ट्यूनिंग पेज भरें।](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.hi.png)

    > [!TIP]
    >
    > आप **Advanced settings** चुनकर **learning_rate** और **lr_scheduler_type** जैसी सेटिंग्स को कस्टमाइज़ कर सकते हैं ताकि फाइन-ट्यूनिंग प्रक्रिया को अपनी आवश्यकताओं के अनुसार बेहतर बनाया जा सके।

1. **Finish** चुनें।

1. इस अभ्यास में, आपने सफलतापूर्वक Azure Machine Learning का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून किया। कृपया ध्यान दें कि फाइन-ट्यूनिंग प्रक्रिया में काफी समय लग सकता है। फाइन-ट्यूनिंग जॉब चलाने के बाद, आपको इसके पूरा होने का इंतजार करना होगा। आप Azure Machine Learning वर्कस्पेस के बाएं साइड में Jobs टैब पर जाकर फाइन-ट्यूनिंग जॉब की स्थिति देख सकते हैं। अगले चरण में, आप फाइन-ट्यून किए गए मॉडल को डिप्लॉय करेंगे और इसे Prompt flow के साथ इंटीग्रेट करेंगे।

    ![फाइनट्यूनिंग जॉब देखें।](../../../../../../translated_images/06-08-output.2bd32e59930672b1.hi.png)

### फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करें

फाइन-ट्यून किए गए Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करने के लिए, आपको मॉडल को डिप्लॉय करना होगा ताकि यह रियल-टाइम इन्फरेंस के लिए उपलब्ध हो सके। इस प्रक्रिया में मॉडल को रजिस्टर करना, ऑनलाइन एंडपॉइंट बनाना और मॉडल को डिप्लॉय करना शामिल है।

इस अभ्यास में, आप:

- Azure Machine Learning वर्कस्पेस में फाइन-ट्यून किए गए मॉडल को रजिस्टर करेंगे।
- एक ऑनलाइन एंडपॉइंट बनाएंगे।
- रजिस्टर किए गए फाइन-ट्यून मॉडल को डिप्लॉय करेंगे।

#### फाइन-ट्यून किए गए मॉडल को रजिस्टर करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. उस Azure Machine Learning वर्कस्पेस को चुनें जिसे आपने बनाया है।

    ![अपने बनाए हुए वर्कस्पेस को चुनें।](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.hi.png)

1. बाएं साइड टैब से **Models** चुनें।

1. **+ Register** चुनें।

1. **From a job output** चुनें।

    ![मॉडल रजिस्टर करें।](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.hi.png)

1. उस जॉब को चुनें जिसे आपने बनाया है।

    ![जॉब चुनें।](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.hi.png)

1. **Next** चुनें।

1. **Model type** को **MLflow** पर सेट करें।

1. सुनिश्चित करें कि **Job output** चुना हुआ है; यह स्वचालित रूप से चुना जाना चाहिए।

    ![आउटपुट चुनें।](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.hi.png)

2. **Next** चुनें।

3. **Register** चुनें।

    ![रजिस्टर चुनें।](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.hi.png)

4. आप बाएं साइड टैब के **Models** मेनू में जाकर अपने रजिस्टर किए गए मॉडल को देख सकते हैं।

    ![रजिस्टर किया गया मॉडल।](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.hi.png)

#### फाइन-ट्यून किए गए मॉडल को डिप्लॉय करें

1. उस Azure Machine Learning वर्कस्पेस पर जाएं जिसे आपने बनाया है।

1. बाएं साइड टैब से **Endpoints** चुनें।

1. नेविगेशन मेनू से **Real-time endpoints** चुनें।

    ![एंडपॉइंट बनाएं।](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.hi.png)

1. **Create** चुनें।

1. अपने बनाए हुए रजिस्टर किए गए मॉडल को चुनें।

    ![रजिस्टर किए गए मॉडल को चुनें।](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.hi.png)

1. **Select** चुनें।

1. निम्न कार्य करें:

    - **Virtual machine** को *Standard_NC6s_v3* पर सेट करें।
    - आप जितने इंस्टेंस उपयोग करना चाहते हैं, वह **Instance count** चुनें। उदाहरण के लिए, *1*।
    - **Endpoint** को **New** पर सेट करें ताकि नया एंडपॉइंट बनाया जा सके।
    - **Endpoint name** दर्ज करें। यह एक अनूठा नाम होना चाहिए।
    - **Deployment name** दर्ज करें। यह भी एक अनूठा नाम होना चाहिए।

    ![डिप्लॉयमेंट सेटिंग भरें।](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.hi.png)

1. **Deploy** चुनें।

> [!WARNING]
> अपने खाते पर अतिरिक्त शुल्क से बचने के लिए, कृपया Azure Machine Learning वर्कस्पेस में बनाए गए एंडपॉइंट को डिलीट करना न भूलें।
>

#### Azure Machine Learning वर्कस्पेस में डिप्लॉयमेंट स्थिति जांचें

1. उस Azure Machine Learning वर्कस्पेस पर जाएं जिसे आपने बनाया है।

1. बाएं साइड टैब से **Endpoints** चुनें।

1. उस एंडपॉइंट को चुनें जिसे आपने बनाया है।

    ![Endpoints चुनें](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.hi.png)

1. इस पेज पर, आप डिप्लॉयमेंट प्रक्रिया के दौरान एंडपॉइंट्स का प्रबंधन कर सकते हैं।

> [!NOTE]
> डिप्लॉयमेंट पूरा होने के बाद, सुनिश्चित करें कि **Live traffic** को **100%** पर सेट किया गया है। यदि ऐसा नहीं है, तो ट्रैफिक सेटिंग्स को समायोजित करने के लिए **Update traffic** चुनें। ध्यान दें कि यदि ट्रैफिक 0% पर सेट है, तो आप मॉडल का परीक्षण नहीं कर सकते।
>
> ![ट्रैफिक सेट करें।](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.hi.png)
>

## परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल से चैट करें

### कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करें

अपने फाइन-ट्यून किए गए मॉडल को सफलतापूर्वक डिप्लॉय करने के बाद, अब आप इसे Prompt Flow के साथ इंटीग्रेट कर सकते हैं ताकि आप अपने मॉडल का उपयोग रियल-टाइम एप्लिकेशन में कर सकें, जिससे आपके कस्टम Phi-3 मॉडल के साथ विभिन्न इंटरैक्टिव कार्य संभव हो सकें।

इस अभ्यास में, आप:

- Azure AI Foundry Hub बनाएंगे।
- Azure AI Foundry प्रोजेक्ट बनाएंगे।
- Prompt flow बनाएंगे।
- फाइन-ट्यून किए गए Phi-3 मॉडल के लिए एक कस्टम कनेक्शन जोड़ेंगे।
- अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए Prompt flow सेटअप करेंगे।
> [!NOTE]
> आप Azure ML Studio का उपयोग करके Promptflow के साथ भी एकीकरण कर सकते हैं। वही एकीकरण प्रक्रिया Azure ML Studio पर भी लागू होती है।
#### Azure AI Foundry Hub बनाएं

प्रोजेक्ट बनाने से पहले आपको एक Hub बनाना होगा। Hub एक Resource Group की तरह काम करता है, जो आपको Azure AI Foundry के भीतर कई Projects को व्यवस्थित और प्रबंधित करने की सुविधा देता है।

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. बाएं साइड टैब से **All hubs** चुनें।

1. नेविगेशन मेनू से **+ New hub** चुनें।

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.hi.png)

1. निम्नलिखित कार्य करें:

    - **Hub name** दर्ज करें। यह एक अनोखा नाम होना चाहिए।
    - अपनी Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - अपनी पसंद की **Location** चुनें।
    - उपयोग करने के लिए **Connect Azure AI Services** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - **Connect Azure AI Search** के लिए **Skip connecting** चुनें।

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.hi.png)

1. **Next** चुनें।

#### Azure AI Foundry Project बनाएं

1. आपने जो Hub बनाया है, उसमें बाएं साइड टैब से **All projects** चुनें।

1. नेविगेशन मेनू से **+ New project** चुनें।

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.hi.png)

1. **Project name** दर्ज करें। यह एक अनोखा नाम होना चाहिए।

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.hi.png)

1. **Create a project** चुनें।

#### Fine-tuned Phi-3 मॉडल के लिए कस्टम कनेक्शन जोड़ें

अपने कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करने के लिए, आपको मॉडल के endpoint और key को एक कस्टम कनेक्शन में सेव करना होगा। यह सेटअप Prompt flow में आपके कस्टम Phi-3 मॉडल तक पहुंच सुनिश्चित करता है।

#### Fine-tuned Phi-3 मॉडल की api key और endpoint uri सेट करें

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. उस Azure Machine learning workspace पर जाएं जिसे आपने बनाया है।

1. बाएं साइड टैब से **Endpoints** चुनें।

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.hi.png)

1. आपने जो endpoint बनाया है, उसे चुनें।

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.hi.png)

1. नेविगेशन मेनू से **Consume** चुनें।

1. अपनी **REST endpoint** और **Primary key** कॉपी करें।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.hi.png)

#### कस्टम कनेक्शन जोड़ें

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. उस Azure AI Foundry प्रोजेक्ट पर जाएं जिसे आपने बनाया है।

1. आपने जो प्रोजेक्ट बनाया है, उसमें बाएं साइड टैब से **Settings** चुनें।

1. **+ New connection** चुनें।

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.hi.png)

1. नेविगेशन मेनू से **Custom keys** चुनें।

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.hi.png)

1. निम्नलिखित कार्य करें:

    - **+ Add key value pairs** चुनें।
    - key नाम के लिए **endpoint** दर्ज करें और Azure ML Studio से कॉपी किया गया endpoint value फील्ड में पेस्ट करें।
    - फिर से **+ Add key value pairs** चुनें।
    - key नाम के लिए **key** दर्ज करें और Azure ML Studio से कॉपी किया गया key value फील्ड में पेस्ट करें।
    - keys जोड़ने के बाद, key को एक्सपोज़ होने से रोकने के लिए **is secret** चुनें।

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.hi.png)

1. **Add connection** चुनें।

#### Prompt flow बनाएं

आपने Azure AI Foundry में एक कस्टम कनेक्शन जोड़ दिया है। अब, निम्नलिखित चरणों का पालन करके एक Prompt flow बनाएं। फिर, आप इस Prompt flow को कस्टम कनेक्शन से कनेक्ट करेंगे ताकि आप अपने fine-tuned मॉडल का उपयोग Prompt flow के भीतर कर सकें।

1. उस Azure AI Foundry प्रोजेक्ट पर जाएं जिसे आपने बनाया है।

1. बाएं साइड टैब से **Prompt flow** चुनें।

1. नेविगेशन मेनू से **+ Create** चुनें।

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.hi.png)

1. नेविगेशन मेनू से **Chat flow** चुनें।

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.hi.png)

1. उपयोग के लिए **Folder name** दर्ज करें।

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.hi.png)

2. **Create** चुनें।

#### अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए Prompt flow सेट करें

आपको fine-tuned Phi-3 मॉडल को Prompt flow में इंटीग्रेट करना होगा। हालांकि, मौजूदा Prompt flow इस उद्देश्य के लिए डिज़ाइन नहीं किया गया है। इसलिए, आपको कस्टम मॉडल के इंटीग्रेशन के लिए Prompt flow को फिर से डिजाइन करना होगा।

1. Prompt flow में, मौजूदा flow को पुनर्निर्मित करने के लिए निम्नलिखित कार्य करें:

    - **Raw file mode** चुनें।
    - *flow.dag.yml* फाइल में मौजूद सभी कोड को हटा दें।
    - *flow.dag.yml* फाइल में निम्नलिखित कोड जोड़ें।

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.hi.png)

1. Prompt flow में कस्टम Phi-3 मॉडल का उपयोग करने के लिए *integrate_with_promptflow.py* फाइल में निम्नलिखित कोड जोड़ें।

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.hi.png)

> [!NOTE]
> Azure AI Foundry में Prompt flow के उपयोग के बारे में अधिक जानकारी के लिए, आप [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) देख सकते हैं।

1. अपने मॉडल के साथ चैट सक्षम करने के लिए **Chat input**, **Chat output** चुनें।

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.hi.png)

1. अब आप अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए तैयार हैं। अगले अभ्यास में, आप सीखेंगे कि Prompt flow को कैसे शुरू करें और इसे अपने fine-tuned Phi-3 मॉडल के साथ चैट करने के लिए कैसे उपयोग करें।

> [!NOTE]
>
> पुनर्निर्मित flow इस चित्र की तरह दिखना चाहिए:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.hi.png)
>

### अपने कस्टम Phi-3 मॉडल के साथ चैट करें

अब जब आपने अपने कस्टम Phi-3 मॉडल को fine-tune और Prompt flow के साथ इंटीग्रेट कर लिया है, तो आप इसके साथ बातचीत शुरू करने के लिए तैयार हैं। यह अभ्यास आपको Prompt flow का उपयोग करके अपने मॉडल के साथ चैट सेटअप और शुरू करने की प्रक्रिया में मार्गदर्शन करेगा। इन चरणों का पालन करके, आप अपने fine-tuned Phi-3 मॉडल की क्षमताओं का विभिन्न कार्यों और संवादों के लिए पूरा उपयोग कर पाएंगे।

- Prompt flow का उपयोग करके अपने कस्टम Phi-3 मॉडल के साथ चैट करें।

#### Prompt flow शुरू करें

1. Prompt flow शुरू करने के लिए **Start compute sessions** चुनें।

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.hi.png)

1. पैरामीटर को रिन्यू करने के लिए **Validate and parse input** चुनें।

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.hi.png)

1. आपने जो कस्टम कनेक्शन बनाया है, उसके **connection** के **Value** को चुनें। उदाहरण के लिए, *connection*।

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.hi.png)

#### अपने कस्टम मॉडल के साथ चैट करें

1. **Chat** चुनें।

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.hi.png)

1. परिणामों का एक उदाहरण यहां है: अब आप अपने कस्टम Phi-3 मॉडल के साथ चैट कर सकते हैं। सुझाव दिया जाता है कि आप fine-tuning के लिए उपयोग किए गए डेटा के आधार पर प्रश्न पूछें।

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.hi.png)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।