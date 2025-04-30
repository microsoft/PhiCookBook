<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ed86d361ac6d4cc8bfb47428e6a2a247",
  "translation_date": "2025-04-04T18:18:48+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hi"
}
-->
# Azure AI Foundry में कस्टम Phi-3 मॉडल्स को फाइन-ट्यून और प्रॉम्प्ट फ्लो के साथ इंटीग्रेट करें

यह एंड-टू-एंड (E2E) सैंपल Microsoft Tech Community के गाइड "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" पर आधारित है। इसमें कस्टम Phi-3 मॉडल्स को फाइन-ट्यून, डिप्लॉय और Azure AI Foundry में प्रॉम्प्ट फ्लो के साथ इंटीग्रेट करने की प्रक्रिया बताई गई है।  
इस सैंपल से अलग, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", जिसमें कोड को लोकल रूप से रन किया गया था, यह ट्यूटोरियल पूरी तरह Azure AI / ML Studio में आपके मॉडल को फाइन-ट्यून और इंटीग्रेट करने पर केंद्रित है।

## अवलोकन

इस E2E सैंपल में, आप सीखेंगे कि Phi-3 मॉडल को फाइन-ट्यून कैसे करें और इसे Azure AI Foundry में प्रॉम्प्ट फ्लो के साथ कैसे इंटीग्रेट करें। Azure AI / ML Studio का उपयोग करके, आप कस्टम AI मॉडल्स को डिप्लॉय और उपयोग करने के लिए एक वर्कफ़्लो स्थापित करेंगे। यह E2E सैंपल तीन परिदृश्यों में विभाजित है:

**परिदृश्य 1: Azure संसाधन सेट करें और फाइन-ट्यूनिंग के लिए तैयार करें**

**परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में डिप्लॉय करें**

**परिदृश्य 3: प्रॉम्प्ट फ्लो के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल के साथ चैट करें**

यह E2E सैंपल का एक अवलोकन है।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.hi.png)

### सामग्री की सूची

1. **[परिदृश्य 1: Azure संसाधन सेट करें और फाइन-ट्यूनिंग के लिए तैयार करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace बनाएं](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription में GPU कोटा का अनुरोध करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [भूमिका असाइनमेंट जोड़ें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [प्रोजेक्ट सेट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 मॉडल को फाइन-ट्यून करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[परिदृश्य 3: प्रॉम्प्ट फ्लो के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल के साथ चैट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [कस्टम Phi-3 मॉडल को प्रॉम्प्ट फ्लो के साथ इंटीग्रेट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [अपने कस्टम Phi-3 मॉडल के साथ चैट करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## परिदृश्य 1: Azure संसाधन सेट करें और फाइन-ट्यूनिंग के लिए तैयार करें

### Azure Machine Learning Workspace बनाएं

1. पोर्टल पेज के टॉप पर **सर्च बार** में *azure machine learning* टाइप करें और दिखाई देने वाले विकल्पों में से **Azure Machine Learning** चुनें।

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.hi.png)

2. नेविगेशन मेनू से **+ Create** चुनें।

3. नेविगेशन मेनू से **New workspace** चुनें।

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.hi.png)

4. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।
    - उपयोग के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - **Workspace Name** दर्ज करें। यह एक यूनिक वैल्यू होनी चाहिए।
    - उपयोग के लिए **Region** चुनें।
    - उपयोग के लिए **Storage account** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - उपयोग के लिए **Key vault** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - उपयोग के लिए **Application insights** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - उपयोग के लिए **Container registry** चुनें (यदि आवश्यक हो तो नया बनाएं)।

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.hi.png)

5. **Review + Create** चुनें।

6. **Create** चुनें।

### Azure Subscription में GPU कोटा का अनुरोध करें

इस ट्यूटोरियल में, आप GPU का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून और डिप्लॉय करना सीखेंगे। फाइन-ट्यूनिंग के लिए, आप *Standard_NC24ads_A100_v4* GPU का उपयोग करेंगे, जिसके लिए कोटा अनुरोध की आवश्यकता होती है। डिप्लॉयमेंट के लिए, आप *Standard_NC6s_v3* GPU का उपयोग करेंगे, जिसके लिए भी कोटा अनुरोध की आवश्यकता होती है।

> [!NOTE]
>
> केवल Pay-As-You-Go सब्सक्रिप्शन (मानक सब्सक्रिप्शन प्रकार) GPU आवंटन के लिए पात्र हैं; बेनिफिट सब्सक्रिप्शन वर्तमान में समर्थित नहीं हैं।
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. *Standard NCADSA100v4 Family* कोटा का अनुरोध करने के लिए निम्नलिखित कार्य करें:

    - बाईं ओर टैब से **Quota** चुनें।
    - उपयोग के लिए **Virtual machine family** चुनें। उदाहरण के लिए, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** चुनें, जिसमें *Standard_NC24ads_A100_v4* GPU शामिल है।
    - नेविगेशन मेनू से **Request quota** चुनें।

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.hi.png)

    - Request quota पेज के अंदर, उपयोग के लिए **New cores limit** दर्ज करें। उदाहरण के लिए, 24।
    - Request quota पेज के अंदर, GPU कोटा का अनुरोध करने के लिए **Submit** चुनें।

1. *Standard NCSv3 Family* कोटा का अनुरोध करने के लिए निम्नलिखित कार्य करें:

    - बाईं ओर टैब से **Quota** चुनें।
    - उपयोग के लिए **Virtual machine family** चुनें। उदाहरण के लिए, **Standard NCSv3 Family Cluster Dedicated vCPUs** चुनें, जिसमें *Standard_NC6s_v3* GPU शामिल है।
    - नेविगेशन मेनू से **Request quota** चुनें।
    - Request quota पेज के अंदर, उपयोग के लिए **New cores limit** दर्ज करें। उदाहरण के लिए, 24।
    - Request quota पेज के अंदर, GPU कोटा का अनुरोध करने के लिए **Submit** चुनें।

### भूमिका असाइनमेंट जोड़ें

अपने मॉडल को फाइन-ट्यून और डिप्लॉय करने के लिए, आपको पहले एक User Assigned Managed Identity (UAI) बनानी होगी और इसे उपयुक्त अनुमतियां असाइन करनी होंगी। यह UAI डिप्लॉयमेंट के दौरान ऑथेंटिकेशन के लिए उपयोग की जाएगी।

#### User Assigned Managed Identity (UAI) बनाएं

1. पोर्टल पेज के टॉप पर **सर्च बार** में *managed identities* टाइप करें और दिखाई देने वाले विकल्पों में से **Managed Identities** चुनें।

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.hi.png)

1. **+ Create** चुनें।

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.hi.png)

1. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।
    - उपयोग के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - उपयोग के लिए **Region** चुनें।
    - **Name** दर्ज करें। यह एक यूनिक वैल्यू होनी चाहिए।

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.hi.png)

1. **Review + create** चुनें।

1. **+ Create** चुनें।

#### Managed Identity को Contributor भूमिका असाइन करें

1. आपने जो Managed Identity बनाई है, उस संसाधन पर जाएं।

1. बाईं ओर टैब से **Azure role assignments** चुनें।

1. नेविगेशन मेनू से **+Add role assignment** चुनें।

1. Add role assignment पेज के अंदर, निम्नलिखित कार्य करें:
    - **Scope** को **Resource group** पर सेट करें।
    - अपनी Azure **Subscription** चुनें।
    - उपयोग के लिए **Resource group** चुनें।
    - **Role** को **Contributor** पर सेट करें।

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.hi.png)

2. **Save** चुनें।

#### Managed Identity को Storage Blob Data Reader भूमिका असाइन करें

1. पोर्टल पेज के टॉप पर **सर्च बार** में *storage accounts* टाइप करें और दिखाई देने वाले विकल्पों में से **Storage accounts** चुनें।

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.hi.png)

1. उस स्टोरेज अकाउंट का चयन करें जो आपने Azure Machine Learning Workspace के साथ जोड़ा है। उदाहरण के लिए, *finetunephistorage*।

1. Add role assignment पेज पर जाने के लिए निम्नलिखित कार्य करें:

    - बनाए गए Azure Storage अकाउंट पर नेविगेट करें।
    - बाईं ओर टैब से **Access Control (IAM)** चुनें।
    - नेविगेशन मेनू से **+ Add** चुनें।
    - नेविगेशन मेनू से **Add role assignment** चुनें।

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.hi.png)

1. Add role assignment पेज के अंदर, निम्नलिखित कार्य करें:

    - Role पेज के अंदर, **Storage Blob Data Reader** टाइप करें और दिखाई देने वाले विकल्पों में से **Storage Blob Data Reader** चुनें।
    - Role पेज के अंदर, **Next** चुनें।
    - Members पेज के अंदर, **Assign access to** **Managed identity** चुनें।
    - Members पेज के अंदर, **+ Select members** चुनें।
    - Select managed identities पेज के अंदर, अपनी Azure **Subscription** चुनें।
    - Select managed identities पेज के अंदर, **Managed identity** को **Manage Identity** पर सेट करें।
    - Select managed identities पेज के अंदर, आपने जो Managed Identity बनाई है, उसे चुनें। उदाहरण के लिए, *finetunephi-managedidentity*।
    - Select managed identities पेज के अंदर, **Select** चुनें।

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.hi.png)

1. **Review + assign** चुनें।

#### Managed Identity को AcrPull भूमिका असाइन करें

1. पोर्टल पेज के टॉप पर **सर्च बार** में *container registries* टाइप करें और दिखाई देने वाले विकल्पों में से **Container registries** चुनें।

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.hi.png)

1. उस कंटेनर रजिस्ट्री का चयन करें जो Azure Machine Learning Workspace के साथ जुड़ी है। उदाहरण के लिए, *finetunephicontainerregistry*

1. Add role assignment पेज पर जाने के लिए निम्नलिखित कार्य करें:

    - बाईं ओर टैब से **Access Control (IAM)** चुनें।
    - नेविगेशन मेनू से **+ Add** चुनें।
    - नेविगेशन मेनू से **Add role assignment** चुनें।

1. Add role assignment पेज के अंदर, निम्नलिखित कार्य करें:

    - Role पेज के अंदर, **AcrPull** टाइप करें और दिखाई देने वाले विकल्पों में से **AcrPull** चुनें।
    - Role पेज के अंदर, **Next** चुनें।
    - Members पेज के अंदर, **Assign access to** **Managed identity** चुनें।
    - Members पेज के अंदर, **+ Select members** चुनें।
    - Select managed identities पेज के अंदर, अपनी Azure **Subscription** चुनें।
    - Select managed identities पेज के अंदर, **Managed identity** को **Manage Identity** पर सेट करें।
    - Select managed identities पेज के अंदर, आपने जो Managed Identity बनाई है, उसे चुनें। उदाहरण के लिए, *finetunephi-managedidentity*।
    - Select managed identities पेज के अंदर, **Select** चुनें।
    - **Review + assign** चुनें।

### प्रोजेक्ट सेट करें

फाइन-ट्यूनिंग के लिए आवश्यक डेटासेट डाउनलोड करने हेतु आप एक लोकल वातावरण सेट करेंगे।

इस अभ्यास में, आप:

- काम करने के लिए एक फ़ोल्डर बनाएंगे।
- एक वर्चुअल वातावरण बनाएंगे।
- आवश्यक पैकेज इंस्टॉल करेंगे।
- डेटासेट डाउनलोड करने के लिए *download_dataset.py* फ़ाइल बनाएंगे।

#### काम करने के लिए एक फ़ोल्डर बनाएँ

1. एक टर्मिनल विंडो खोलें और *finetune-phi* नाम का फ़ोल्डर बनाने के लिए निम्न कमांड टाइप करें।

    ```console
    mkdir finetune-phi
    ```

2. बनाए गए *finetune-phi* फ़ोल्डर पर नेविगेट करने के लिए टर्मिनल में निम्न कमांड टाइप करें।

    ```console
    cd finetune-phi
    ```

#### वर्चुअल वातावरण बनाएँ

1. टर्मिनल में निम्न कमांड टाइप करें ताकि *.venv* नाम का वर्चुअल वातावरण बन सके।

    ```console
    python -m venv .venv
    ```

2. वर्चुअल वातावरण को सक्रिय करने के लिए टर्मिनल में निम्न कमांड टाइप करें।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> यदि यह सफल होता है, तो कमांड प्रॉम्प्ट से पहले *(.venv)* दिखाई देगा।

#### आवश्यक पैकेज इंस्टॉल करें

1. आवश्यक पैकेज इंस्टॉल करने के लिए टर्मिनल में निम्न कमांड्स टाइप करें।

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` बनाएँ

> [!NOTE]
> पूर्ण फ़ोल्डर संरचना:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** खोलें।

1. मेनू बार से **File** चुनें।

1. **Open Folder** चुनें।

1. *finetune-phi* फ़ोल्डर चुनें, जो *C:\Users\yourUserName\finetune-phi* पर स्थित है।

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.hi.png)

1. Visual Studio Code के बाएँ पैन में, राइट-क्लिक करें और **New File** चुनें ताकि *download_dataset.py* नाम की नई फ़ाइल बनाई जा सके।

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.hi.png)

### फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें

इस अभ्यास में, आप *download_dataset.py* फ़ाइल को रन करेंगे ताकि *ultrachat_200k* डेटासेट्स को अपने लोकल वातावरण में डाउनलोड किया जा सके। फिर आप इस डेटासेट का उपयोग Azure Machine Learning में Phi-3 मॉडल को फाइन-ट्यून करने के लिए करेंगे।

इस अभ्यास में, आप:

- डेटासेट डाउनलोड करने के लिए *download_dataset.py* फ़ाइल में कोड जोड़ेंगे।
- डेटासेट को अपने लोकल वातावरण में डाउनलोड करने के लिए *download_dataset.py* फ़ाइल को रन करेंगे।

#### *download_dataset.py* का उपयोग करके अपना डेटासेट डाउनलोड करें

1. Visual Studio Code में *download_dataset.py* फ़ाइल खोलें।

1. *download_dataset.py* फ़ाइल में निम्न कोड जोड़ें।

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

1. स्क्रिप्ट को रन करने और डेटासेट को अपने लोकल वातावरण में डाउनलोड करने के लिए टर्मिनल में निम्न कमांड टाइप करें।

    ```console
    python download_dataset.py
    ```

1. सुनिश्चित करें कि डेटासेट्स सफलतापूर्वक आपके लोकल *finetune-phi/data* डायरेक्टरी में सेव हो गए हैं।

>
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. बाईं ओर टैब से **Compute** चुनें।

1. नेविगेशन मेनू से **Compute clusters** चुनें।

1. **+ New** पर क्लिक करें।

    ![कंप्यूट चुनें।](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.hi.png)

1. निम्नलिखित कार्य करें:

    - वह **Region** चुनें जिसे आप उपयोग करना चाहते हैं।
    - **Virtual machine tier** को **Dedicated** पर सेट करें।
    - **Virtual machine type** को **GPU** पर सेट करें।
    - **Virtual machine size** फ़िल्टर को **Select from all options** पर सेट करें।
    - **Virtual machine size** को **Standard_NC24ads_A100_v4** पर सेट करें।

    ![क्लस्टर बनाएं।](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.hi.png)

1. **Next** चुनें।

1. निम्नलिखित कार्य करें:

    - **Compute name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - **Minimum number of nodes** को **0** पर सेट करें।
    - **Maximum number of nodes** को **1** पर सेट करें।
    - **Idle seconds before scale down** को **120** पर सेट करें।

    ![क्लस्टर बनाएं।](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.hi.png)

1. **Create** चुनें।

#### Phi-3 मॉडल को फाइन-ट्यून करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. वह Azure Machine Learning workspace चुनें जिसे आपने बनाया है।

    ![वह workspace चुनें जिसे आपने बनाया है।](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hi.png)

1. निम्नलिखित कार्य करें:

    - बाईं ओर टैब से **Model catalog** चुनें।
    - **search bar** में *phi-3-mini-4k* टाइप करें और दिखाई देने वाले विकल्पों में से **Phi-3-mini-4k-instruct** चुनें।

    ![phi-3-mini-4k टाइप करें।](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.hi.png)

1. नेविगेशन मेनू से **Fine-tune** चुनें।

    ![फाइन ट्यून चुनें।](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.hi.png)

1. निम्नलिखित कार्य करें:

    - **Select task type** को **Chat completion** पर सेट करें।
    - **+ Select data** चुनें और **Training data** अपलोड करें।
    - Validation data अपलोड प्रकार को **Provide different validation data** पर सेट करें।
    - **+ Select data** चुनें और **Validation data** अपलोड करें।

    ![फाइन-ट्यूनिंग पेज भरें।](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.hi.png)

    > [!TIP]
    >
    > आप **Advanced settings** चुन सकते हैं ताकि **learning_rate** और **lr_scheduler_type** जैसी कॉन्फ़िगरेशन को अनुकूलित किया जा सके और आपकी विशिष्ट आवश्यकताओं के अनुसार फाइन-ट्यूनिंग प्रक्रिया को ऑप्टिमाइज़ किया जा सके।

1. **Finish** चुनें।

1. इस अभ्यास में, आपने Azure Machine Learning का उपयोग करके सफलतापूर्वक Phi-3 मॉडल को फाइन-ट्यून किया। कृपया ध्यान दें कि फाइन-ट्यूनिंग प्रक्रिया में काफी समय लग सकता है। फाइन-ट्यूनिंग जॉब चलाने के बाद, आपको इसके पूरा होने की प्रतीक्षा करनी होगी। आप अपने Azure Machine Learning Workspace के बाईं ओर **Jobs** टैब पर जाकर फाइन-ट्यूनिंग जॉब की स्थिति की निगरानी कर सकते हैं। अगली श्रृंखला में, आप फाइन-ट्यून किए गए मॉडल को डिप्लॉय करेंगे और इसे Prompt Flow के साथ इंटीग्रेट करेंगे।

    ![फाइन-ट्यूनिंग जॉब देखें।](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.hi.png)

### फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करें

फाइन-ट्यून किए गए Phi-3 मॉडल को Prompt Flow के साथ इंटीग्रेट करने के लिए, आपको मॉडल को रियल-टाइम इन्फ्रेंस के लिए सुलभ बनाने के लिए डिप्लॉय करना होगा। इस प्रक्रिया में मॉडल को रजिस्टर करना, एक ऑनलाइन एंडपॉइंट बनाना, और मॉडल को डिप्लॉय करना शामिल है।

इस अभ्यास में, आप:

- फाइन-ट्यून किए गए मॉडल को Azure Machine Learning Workspace में रजिस्टर करेंगे।
- एक ऑनलाइन एंडपॉइंट बनाएंगे।
- रजिस्टर किए गए फाइन-ट्यून किए गए Phi-3 मॉडल को डिप्लॉय करेंगे।

#### फाइन-ट्यून किए गए मॉडल को रजिस्टर करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. वह Azure Machine Learning Workspace चुनें जिसे आपने बनाया है।

    ![वह workspace चुनें जिसे आपने बनाया है।](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hi.png)

1. बाईं ओर टैब से **Models** चुनें।
1. **+ Register** चुनें।
1. **From a job output** चुनें।

    ![मॉडल रजिस्टर करें।](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.hi.png)

1. वह जॉब चुनें जिसे आपने बनाया है।

    ![जॉब चुनें।](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.hi.png)

1. **Next** चुनें।

1. **Model type** को **MLflow** पर सेट करें।

1. सुनिश्चित करें कि **Job output** चुना हुआ है; यह स्वतः चुना हुआ होना चाहिए।

    ![आउटपुट चुनें।](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.hi.png)

2. **Next** चुनें।

3. **Register** चुनें।

    ![रजिस्टर चुनें।](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.hi.png)

4. आप अपने रजिस्टर किए गए मॉडल को बाईं ओर टैब से **Models** मेनू में जाकर देख सकते हैं।

    ![रजिस्टर किया गया मॉडल।](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.hi.png)

#### फाइन-ट्यून किए गए मॉडल को डिप्लॉय करें

1. उस Azure Machine Learning Workspace में जाएं जिसे आपने बनाया है।

1. बाईं ओर टैब से **Endpoints** चुनें।

1. नेविगेशन मेनू से **Real-time endpoints** चुनें।

    ![एंडपॉइंट बनाएं।](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.hi.png)

1. **Create** चुनें।

1. वह रजिस्टर किया गया मॉडल चुनें जिसे आपने बनाया है।

    ![रजिस्टर किया गया मॉडल चुनें।](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.hi.png)

1. **Select** चुनें।

1. निम्नलिखित कार्य करें:

    - **Virtual machine** को *Standard_NC6s_v3* पर सेट करें।
    - वह **Instance count** चुनें जिसे आप उपयोग करना चाहते हैं। उदाहरण के लिए, *1*।
    - **Endpoint** को **New** पर सेट करें ताकि एक नया एंडपॉइंट बनाया जा सके।
    - **Endpoint name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - **Deployment name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।

    ![डिप्लॉयमेंट सेटिंग भरें।](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.hi.png)

1. **Deploy** चुनें।

> [!WARNING]
> अपने खाते पर अतिरिक्त शुल्क से बचने के लिए, सुनिश्चित करें कि आपने Azure Machine Learning Workspace में बनाया गया एंडपॉइंट हटा दिया है।
>

#### Azure Machine Learning Workspace में डिप्लॉयमेंट स्थिति की जांच करें

1. उस Azure Machine Learning Workspace में जाएं जिसे आपने बनाया है।

1. बाईं ओर टैब से **Endpoints** चुनें।

1. वह एंडपॉइंट चुनें जिसे आपने बनाया है।

    ![एंडपॉइंट्स चुनें।](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.hi.png)

1. इस पेज पर, आप डिप्लॉयमेंट प्रक्रिया के दौरान एंडपॉइंट्स को प्रबंधित कर सकते हैं।

> [!NOTE]
> एक बार डिप्लॉयमेंट पूरा हो जाने के बाद, सुनिश्चित करें कि **Live traffic** को **100%** पर सेट किया गया है। यदि ऐसा नहीं है, तो **Update traffic** चुनें ताकि ट्रैफिक सेटिंग को समायोजित किया जा सके। ध्यान दें कि यदि ट्रैफिक 0% पर सेट है तो आप मॉडल का परीक्षण नहीं कर सकते।
>
> ![ट्रैफिक सेट करें।](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.hi.png)
>

## परिदृश्य 3: Prompt Flow के साथ इंटीग्रेट करें और Azure AI Foundry में अपने कस्टम मॉडल से चैट करें

### कस्टम Phi-3 मॉडल को Prompt Flow के साथ इंटीग्रेट करें

अपना फाइन-ट्यून किया हुआ मॉडल सफलतापूर्वक डिप्लॉय करने के बाद, आप इसे Prompt Flow के साथ इंटीग्रेट कर सकते हैं ताकि अपने मॉडल का उपयोग रियल-टाइम एप्लिकेशन में किया जा सके, जिससे अपने कस्टम Phi-3 मॉडल के साथ इंटरैक्टिव टास्क की सुविधा मिल सके।

इस अभ्यास में, आप:

- Azure AI Foundry Hub बनाएंगे।
- Azure AI Foundry Project बनाएंगे।
- Prompt Flow बनाएंगे।
- फाइन-ट्यून किए गए Phi-3 मॉडल के लिए एक कस्टम कनेक्शन जोड़ेंगे।
- अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए Prompt Flow सेट करेंगे।

> [!NOTE]
> आप Azure ML Studio का उपयोग करके भी Prompt Flow के साथ इंटीग्रेट कर सकते हैं। वही इंटीग्रेशन प्रक्रिया Azure ML Studio पर लागू की जा सकती है।

#### Azure AI Foundry Hub बनाएं

Project बनाने से पहले आपको एक Hub बनाना होगा। Hub एक Resource Group की तरह कार्य करता है, जिससे आप Azure AI Foundry के भीतर कई Projects को व्यवस्थित और प्रबंधित कर सकते हैं।

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. बाईं ओर टैब से **All hubs** चुनें।

1. नेविगेशन मेनू से **+ New hub** चुनें।

    ![Hub बनाएं।](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.hi.png)

1. निम्नलिखित कार्य करें:

    - **Hub name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - अपना Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (आवश्यक हो तो नया बनाएं)।
    - वह **Location** चुनें जिसे आप उपयोग करना चाहते हैं।
    - **Connect Azure AI Services** चुनें (आवश्यक हो तो नया बनाएं)।
    - **Connect Azure AI Search** को **Skip connecting** पर सेट करें।

    ![Hub भरें।](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.hi.png)

1. **Next** चुनें।

#### Azure AI Foundry Project बनाएं

1. उस Hub में जिसे आपने बनाया है, बाईं ओर टैब से **All projects** चुनें।

1. नेविगेशन मेनू से **+ New project** चुनें।

    ![नया प्रोजेक्ट चुनें।](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.hi.png)

1. **Project name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।

    ![प्रोजेक्ट बनाएं।](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.hi.png)

1. **Create a project** चुनें।

#### फाइन-ट्यून किए गए Phi-3 मॉडल के लिए कस्टम कनेक्शन जोड़ें

अपने कस्टम Phi-3 मॉडल को Prompt Flow के साथ इंटीग्रेट करने के लिए, आपको मॉडल के एंडपॉइंट और key को कस्टम कनेक्शन में सेव करना होगा। यह सेटअप Prompt Flow में आपके कस्टम Phi-3 मॉडल तक पहुंच सुनिश्चित करता है।

#### फाइन-ट्यून किए गए Phi-3 मॉडल का api key और endpoint uri सेट करें

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. उस Azure Machine Learning Workspace में जाएं जिसे आपने बनाया है।

1. बाईं ओर टैब से **Endpoints** चुनें।

    ![एंडपॉइंट्स चुनें।](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.hi.png)

1. वह एंडपॉइंट चुनें जिसे आपने बनाया है।

    ![बनाए गए एंडपॉइंट को चुनें।](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.hi.png)

1. नेविगेशन मेनू से **Consume** चुनें।

1. अपना **REST endpoint** और **Primary key** कॉपी करें।
![API कुंजी और एंडपॉइंट URI कॉपी करें।](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.hi.png)

#### कस्टम कनेक्शन जोड़ें

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) पर जाएं।

1. उस Azure AI Foundry प्रोजेक्ट पर जाएं जिसे आपने बनाया है।

1. अपने बनाए गए प्रोजेक्ट में, बाईं ओर टैब से **Settings** चुनें।

1. **+ New connection** चुनें।

    ![नया कनेक्शन चुनें।](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.hi.png)

1. नेविगेशन मेनू से **Custom keys** चुनें।

    ![कस्टम कुंजी चुनें।](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.hi.png)

1. निम्न कार्य करें:

    - **+ Add key value pairs** चुनें।
    - कुंजी नाम के लिए, **endpoint** दर्ज करें और Azure ML Studio से कॉपी किए गए एंडपॉइंट को वैल्यू फ़ील्ड में पेस्ट करें।
    - फिर से **+ Add key value pairs** चुनें।
    - कुंजी नाम के लिए, **key** दर्ज करें और Azure ML Studio से कॉपी की गई कुंजी को वैल्यू फ़ील्ड में पेस्ट करें।
    - कुंजियाँ जोड़ने के बाद, **is secret** चुनें ताकि कुंजी को एक्सपोज़ होने से बचाया जा सके।

    ![कनेक्शन जोड़ें।](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.hi.png)

1. **Add connection** चुनें।

#### Prompt flow बनाएं

आपने Azure AI Foundry में एक कस्टम कनेक्शन जोड़ लिया है। अब, निम्न चरणों का उपयोग करके एक Prompt flow बनाएं। इसके बाद, आप इस Prompt flow को कस्टम कनेक्शन से जोड़ेंगे ताकि आप Prompt flow के भीतर फाइन-ट्यून किए गए मॉडल का उपयोग कर सकें।

1. उस Azure AI Foundry प्रोजेक्ट पर जाएं जिसे आपने बनाया है।

1. बाईं ओर टैब से **Prompt flow** चुनें।

1. नेविगेशन मेनू से **+ Create** चुनें।

    ![Promptflow चुनें।](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.hi.png)

1. नेविगेशन मेनू से **Chat flow** चुनें।

    ![Chat flow चुनें।](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.hi.png)

1. उपयोग करने के लिए **Folder name** दर्ज करें।

    ![नाम दर्ज करें।](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.hi.png)

2. **Create** चुनें।

#### अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए Prompt flow सेट करें

आपको फाइन-ट्यून किए गए Phi-3 मॉडल को Prompt flow में एकीकृत करना होगा। हालांकि, मौजूदा Prompt flow इस उद्देश्य के लिए डिज़ाइन नहीं किया गया है। इसलिए, आपको कस्टम मॉडल को एकीकृत करने के लिए Prompt flow को फिर से डिज़ाइन करना होगा।

1. Prompt flow में, मौजूदा फ्लो को पुनर्निर्मित करने के लिए निम्न कार्य करें:

    - **Raw file mode** चुनें।
    - *flow.dag.yml* फ़ाइल में मौजूदा कोड को हटा दें।
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

    ![Raw file mode चुनें।](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.hi.png)

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

    ![Prompt flow कोड पेस्ट करें।](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.hi.png)

> [!NOTE]
> Azure AI Foundry में Prompt flow का उपयोग करने पर अधिक विस्तृत जानकारी के लिए, आप [Azure AI Foundry में Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) देख सकते हैं।

1. **Chat input**, **Chat output** चुनें ताकि आप अपने मॉडल के साथ चैट कर सकें।

    ![इनपुट आउटपुट।](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.hi.png)

1. अब आप अपने कस्टम Phi-3 मॉडल के साथ चैट करने के लिए तैयार हैं। अगले अभ्यास में, आप सीखेंगे कि Prompt flow शुरू करें और इसका उपयोग करके अपने फाइन-ट्यून किए गए Phi-3 मॉडल के साथ चैट करें।

> [!NOTE]
>
> पुनर्निर्मित फ्लो नीचे दी गई छवि जैसा दिखना चाहिए:
>
> ![फ्लो उदाहरण।](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.hi.png)
>

### अपने कस्टम Phi-3 मॉडल के साथ चैट करें

अब जब आपने अपने कस्टम Phi-3 मॉडल को फाइन-ट्यून और Prompt flow के साथ एकीकृत कर लिया है, तो आप इसके साथ बातचीत शुरू करने के लिए तैयार हैं। यह अभ्यास आपको Prompt flow का उपयोग करके अपने मॉडल के साथ चैट सेटअप और शुरू करने की प्रक्रिया के माध्यम से मार्गदर्शन करेगा। इन चरणों का पालन करके, आप अपने फाइन-ट्यून किए गए Phi-3 मॉडल की क्षमताओं का पूरी तरह से उपयोग कर सकते हैं।

- Prompt flow का उपयोग करके अपने कस्टम Phi-3 मॉडल के साथ चैट करें।

#### Prompt flow शुरू करें

1. Prompt flow शुरू करने के लिए **Start compute sessions** चुनें।

    ![कंप्यूट सत्र शुरू करें।](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.hi.png)

1. पैरामीटर को नवीनीकृत करने के लिए **Validate and parse input** चुनें।

    ![इनपुट मान्य करें।](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.hi.png)

1. बनाए गए कस्टम कनेक्शन से **connection** का **Value** चुनें। उदाहरण के लिए, *connection*।

    ![कनेक्शन।](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.hi.png)

#### अपने कस्टम मॉडल के साथ चैट करें

1. **Chat** चुनें।

    ![चैट चुनें।](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.hi.png)

1. यहाँ परिणामों का एक उदाहरण है: अब आप अपने कस्टम Phi-3 मॉडल के साथ चैट कर सकते हैं। यह अनुशंसा की जाती है कि आप फाइन-ट्यूनिंग के लिए उपयोग किए गए डेटा के आधार पर प्रश्न पूछें।

    ![Prompt flow के साथ चैट करें।](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.hi.png)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या गलतियाँ हो सकती हैं। मूल भाषा में उपलब्ध दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।