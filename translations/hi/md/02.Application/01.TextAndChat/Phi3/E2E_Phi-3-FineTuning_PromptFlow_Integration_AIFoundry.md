# Microsoft Foundry में Prompt flow के साथ कस्टम Phi-3 मॉडल को फाइन-ट्यून और इंटीग्रेट करें

यह एंड-टू-एंड (E2E) नमूना माइक्रोसॉफ्ट टेक कम्युनिटी के गाइड "[Microsoft Foundry में Prompt Flow के साथ कस्टम Phi-3 मॉडल को फाइन-ट्यून और इंटीग्रेट करें](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" पर आधारित है। यह Microsoft Foundry में कस्टम Phi-3 मॉडल को फाइन-ट्यून करने, तैनात करने और Prompt flow के साथ इंटीग्रेट करने की प्रक्रियाओं का परिचय देता है।  
E2E नमूने के विपरीत, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", जिसमें कोड लोकल रूप से चलाना शामिल था, यह ट्यूटोरियल पूरी तरह से Azure AI / ML स्टूडियो में आपके मॉडल को फाइन-ट्यून और इंटीग्रेट करने पर केंद्रित है।

## अवलोकन

इस E2E नमूने में, आप Phi-3 मॉडल को फाइन-ट्यून करना और Microsoft Foundry में Prompt flow के साथ इसे इंटीग्रेट करना सीखेंगे। Azure AI / ML स्टूडियो का उपयोग करके, आप कस्टम AI मॉडल तैनात करने और उपयोग करने के लिए एक वर्कफ़्लो स्थापित करेंगे। यह E2E नमूना तीन परिदृश्यों में विभाजित है:

**परिदृश्य 1: Azure संसाधनों की स्थापना और फाइन-ट्यूनिंग के लिए तैयारी**

**परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में तैनात करें**

**परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Microsoft Foundry में अपने कस्टम मॉडल के साथ चैट करें**

यहाँ इस E2E नमूने का एक अवलोकन है।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/hi/00-01-architecture.198ba0f1ae6d841a.webp)

### सामग्री सारणी

1. **[परिदृश्य 1: Azure संसाधनों की स्थापना और फाइन-ट्यूनिंग के लिए तैयारी](#परिदृश्य-1-azure-संसाधनों-की-स्थापना-और-फाइन-ट्यूनिंग-के-लिए-तैयारी)**
    - [Azure Machine Learning वर्कस्पेस बनाएं](#azure-machine-learning-वर्कस्पेस-बनाएं)
    - [Azure सब्सक्रिप्शन में GPU कोटा का अनुरोध करें](#azure-सब्सक्रिप्शन-में-gpu-कोटा-का-अनुरोध-करें)
    - [भूमिका असाइनमेंट जोड़ें](#भूमिका-असाइनमेंट-जोड़ें)
    - [परियोजना सेट अप करें](#परियोजना-सेट-अप-करें)
    - [फाइन-ट्यूनिंग के लिए डेटासेट तैयार करें](#फाइन-ट्यूनिंग-के-लिए-डेटा-सेट-तैयार-करें)

1. **[परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में तैनात करें](#परिदृश्य-2-phi-3-मॉडल-को-फाइन-ट्यून-करें-और-azure-machine-learning-studio-में-तैनात-करें)**
    - [Phi-3 मॉडल को फाइन-ट्यून करें](#phi-3-मॉडल-को-फाइन-ट्यून-करें)
    - [फाइन-ट्यून किए गए Phi-3 मॉडल को तैनात करें](#फाइन-ट्यून-किए-गए-phi-3-मॉडल-को-तैनात-करें)

1. **[परिदृश्य 3: Prompt flow के साथ इंटीग्रेट करें और Microsoft Foundry में अपने कस्टम मॉडल के साथ चैट करें](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [कस्टम Phi-3 मॉडल को Prompt flow के साथ इंटीग्रेट करें](#कस्टम-phi-3-मॉडल-को-prompt-flow-के-साथ-एकीकृत-करें)
    - [अपने कस्टम Phi-3 मॉडल के साथ चैट करें](#अपने-कस्टम-phi-3-मॉडल-के-साथ-चैट-करें)

## परिदृश्य 1: Azure संसाधनों की स्थापना और फाइन-ट्यूनिंग के लिए तैयारी

### Azure Machine Learning वर्कस्पेस बनाएं

1. पोर्टल पेज के ऊपर के **खोज बार** में *azure machine learning* टाइप करें और प्रकट होने वाले विकल्पों में से **Azure Machine Learning** चुनें।

    ![Type azure machine learning.](../../../../../../translated_images/hi/01-01-type-azml.acae6c5455e67b4b.webp)

2. नेविगेशन मेनू से **+ Create** चुनें।

3. नेविगेशन मेनू से **New workspace** चुनें।

    ![Select new workspace.](../../../../../../translated_images/hi/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (जरूरत पड़ने पर नया बनाएं)।
    - **Workspace Name** दर्ज करें। यह एक अनूठा मान होना चाहिए।
    - अपना पसंदीदा **Region** चुनें।
    - उपयोग करने के लिए **Storage account** चुनें (जरूरत पड़ने पर नया बनाएं)।
    - उपयोग करने के लिए **Key vault** चुनें (जरूरत पड़ने पर नया बनाएं)।
    - उपयोग करने के लिए **Application insights** चुनें (जरूरत पड़ने पर नया बनाएं)।
    - उपयोग करने के लिए **Container registry** चुनें (जरूरत पड़ने पर नया बनाएं)।

    ![Fill azure machine learning.](../../../../../../translated_images/hi/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** चुनें।

6. **Create** चुनें।

### Azure सब्सक्रिप्शन में GPU कोटा का अनुरोध करें

इस ट्यूटोरियल में, आप GPUs का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून और तैनात करना सीखेंगे। फाइन-ट्यूनिंग के लिए, आप *Standard_NC24ads_A100_v4* GPU का उपयोग करेंगे, जिसके लिए कोटा अनुरोध आवश्यक है। तैनाती के लिए, आप *Standard_NC6s_v3* GPU का उपयोग करेंगे, जिसके लिए भी कोटा अनुरोध आवश्यक है।

> [!NOTE]
>
> केवल Pay-As-You-Go सब्सक्रिप्शन (मानक सब्सक्रिप्शन प्रकार) GPU आवंटन के लिए पात्र हैं; लाभ सब्सक्रिप्शन वर्तमान में समर्थित नहीं हैं।
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. *Standard NCADSA100v4 Family* कोटा का अनुरोध करने के लिए निम्न कार्य करें:

    - बाएं टैब में **Quota** चुनें।
    - उपयोग करने के लिए **Virtual machine family** चुनें। उदाहरण के लिए, *Standard_NC24ads_A100_v4* GPU वाला **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** चुनें।
    - नेविगेशन मेनू में **Request quota** चुनें।

        ![Request quota.](../../../../../../translated_images/hi/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota पेज में, आप उपयोग करना चाहते हैं इतना **New cores limit** दर्ज करें। उदाहरण के लिए, 24।
    - Request quota पेज में, GPU कोटा के लिए **Submit** चुनें।

1. *Standard NCSv3 Family* कोटा का अनुरोध करने के लिए निम्न कार्य करें:

    - बाएं टैब में **Quota** चुनें।
    - उपयोग करने के लिए **Virtual machine family** चुनें। उदाहरण के लिए, *Standard_NC6s_v3* GPU वाला **Standard NCSv3 Family Cluster Dedicated vCPUs** चुनें।
    - नेविगेशन मेनू में **Request quota** चुनें।
    - Request quota पेज में, आप उपयोग करना चाहते हैं इतना **New cores limit** दर्ज करें। उदाहरण के लिए, 24।
    - Request quota पेज में, GPU कोटा के लिए **Submit** चुनें।

### भूमिका असाइनमेंट जोड़ें

अपने मॉडल को फाइन-ट्यून और तैनात करने के लिए, आपको पहले एक User Assigned Managed Identity (UAI) बनानी होगी और उसे उपयुक्त अनुमति असाइन करनी होगी। यह UAI तैनाती के दौरान प्रमाणीकरण के लिए उपयोग की जाएगी।

#### User Assigned Managed Identity (UAI) बनाएं

1. पोर्टल पेज के ऊपर के **खोज बार** में *managed identities* टाइप करें और प्रकट होने वाले विकल्पों में से **Managed Identities** चुनें।

    ![Type managed identities.](../../../../../../translated_images/hi/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** चुनें।

    ![Select create.](../../../../../../translated_images/hi/03-02-select-create.92bf8989a5cd98f2.webp)

1. निम्नलिखित कार्य करें:

    - अपनी Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (जरूरत पड़ने पर नया बनाएं)।
    - पसंदीदा **Region** चुनें।
    - **Name** दर्ज करें। यह एक अनूठा मान होना चाहिए।

    ![Select create.](../../../../../../translated_images/hi/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** चुनें।

1. **+ Create** चुनें।

#### Managed Identity को Contributor भूमिका असाइन करें

1. उस Managed Identity संसाधन पर जाएं जिसे आपने बनाया है।

1. बाएं टैब से **Azure role assignments** चुनें।

1. नेविगेशन मेनू से **+Add role assignment** चुनें।

1. Add role assignment पेज में निम्नलिखित कार्य करें:
    - **Scope** को **Resource group** चुनें।
    - अपनी Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें।
    - **Role** को **Contributor** चुनें।

    ![Fill contributor role.](../../../../../../translated_images/hi/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** चुनें।

#### Managed Identity को Storage Blob Data Reader भूमिका असाइन करें

1. पोर्टल पेज के ऊपर के **खोज बार** में *storage accounts* टाइप करें और प्रकट होने वाले विकल्पों में से **Storage accounts** चुनें।

    ![Type storage accounts.](../../../../../../translated_images/hi/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. उस स्टोरेज अकाउंट का चयन करें जो आपने Azure Machine Learning वर्कस्पेस के साथ जोड़ा है। उदाहरण के लिए, *finetunephistorage*।

1. Add role assignment पेज पर जाने के लिए निम्नलिखित कार्य करें:

    - Azure Storage अकाउंट पर नेविगेट करें जो आपने बनाया है।
    - बाएं टैब से **Access Control (IAM)** चुनें।
    - नेविगेशन मेनू से **+ Add** चुनें।
    - नेविगेशन मेनू से **Add role assignment** चुनें।

    ![Add role.](../../../../../../translated_images/hi/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment पेज में निम्न कार्य करें:

    - Role पेज में, **search bar** में *Storage Blob Data Reader* टाइप करें और प्रकट होने वाले विकल्पों में से **Storage Blob Data Reader** चुनें।
    - Role पेज में, **Next** चुनें।
    - Members पेज में, **Assign access to** के तहत **Managed identity** चुनें।
    - Members पेज में, **+ Select members** चुनें।
    - Select managed identities पेज में, अपनी Azure **Subscription** चुनें।
    - Select managed identities पेज में, **Managed identity** के रूप में **Manage Identity** चुनें।
    - Select managed identities पेज में, वह Managed Identity चुनें जो आपने बनाया है। उदाहरण के लिए, *finetunephi-managedidentity*।
    - Select managed identities पेज में, **Select** चुनें।

    ![Select managed identity.](../../../../../../translated_images/hi/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** चुनें।

#### Managed Identity को AcrPull भूमिका असाइन करें

1. पोर्टल पेज के ऊपर के **खोज बार** में *container registries* टाइप करें और प्रकट होने वाले विकल्पों में से **Container registries** चुनें।

    ![Type container registries.](../../../../../../translated_images/hi/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. उस कंटेनर रजिस्ट्रि का चयन करें जो Azure Machine Learning वर्कस्पेस के साथ जुड़ा है। उदाहरण के लिए, *finetunephicontainerregistry*

1. Add role assignment पेज पर जाने के लिए निम्नलिखित कार्य करें:

    - बाएं टैब से **Access Control (IAM)** चुनें।
    - नेविगेशन मेनू से **+ Add** चुनें।
    - नेविगेशन मेनू से **Add role assignment** चुनें।

1. Add role assignment पेज में निम्न कार्य करें:

    - Role पेज में, **search bar** में *AcrPull* टाइप करें और प्रकट होने वाले विकल्पों में से **AcrPull** चुनें।
    - Role पेज में, **Next** चुनें।
    - Members पेज में, **Assign access to** के तहत **Managed identity** चुनें।
    - Members पेज में, **+ Select members** चुनें।
    - Select managed identities पेज में, अपनी Azure **Subscription** चुनें।
    - Select managed identities पेज में, **Managed identity** को **Manage Identity** चुनें।
    - Select managed identities पेज में, वह Manage Identity चुनें जो आपने बनाया है। उदाहरण के लिए, *finetunephi-managedidentity*।
    - Select managed identities पेज में, **Select** चुनें।
    - **Review + assign** चुनें।

### परियोजना सेट अप करें

फाइन-ट्यूनिंग के लिए आवश्यक डेटासेट डाउनलोड करने हेतु आप एक स्थानीय वातावरण सेट अप करेंगे।

इस अभ्यास में, आप

- काम करने के लिए एक फ़ोल्डर बनाएंगे।
- एक वर्चुअल वातावरण बनाएंगे।
- आवश्यक पैकेजों को इंस्टॉल करेंगे।
- डेटासेट डाउनलोड करने के लिए *download_dataset.py* फ़ाइल बनाएंगे।

#### काम करने के लिए एक फ़ोल्डर बनाएँ

1. एक टर्मिनल विंडो खोलें और डिफ़ॉल्ट पथ में *finetune-phi* नामक फ़ोल्डर बनाने के लिए निम्न कमांड टाइप करें।

    ```console
    mkdir finetune-phi
    ```

2. अपने टर्मिनल में निम्न कमांड टाइप करें ताकि आप बनाए गए *finetune-phi* फ़ोल्डर में नेविगेट कर सकें।

    ```console
    cd finetune-phi
    ```

#### एक वर्चुअल वातावरण बनाएं

1. अपने टर्मिनल में निम्न कमांड टाइप करें ताकि *.venv* नामक एक वर्चुअल वातावरण बनाया जा सके।
    ```console
    python -m venv .venv
    ```

2. वर्चुअल एनवायरनमेंट को सक्रिय करने के लिए अपने टर्मिनल के अंदर निम्न कमांड टाइप करें।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> यदि यह काम कर गया, तो आपको कमांड प्रॉम्प्ट से पहले *(.venv)* दिखाई देगा।

#### आवश्यक पैकेज इंस्टॉल करें

1. आवश्यक पैकेज इंस्टॉल करने के लिए अपने टर्मिनल के अंदर निम्न कमांड टाइप करें।

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` बनाएं

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

1. उस *finetune-phi* फ़ोल्डर को चुनें जिसे आपने बनाया है, जो *C:\Users\yourUserName\finetune-phi* पर स्थित है।

    ![अपना बनाया हुआ फ़ोल्डर चुनें।](../../../../../../translated_images/hi/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code के बाएँ पेन में, राइट-क्लिक करें और **New File** चुनें ताकि *download_dataset.py* नाम की एक नई फ़ाइल बनाई जा सके।

    ![नई फ़ाइल बनाएं।](../../../../../../translated_images/hi/04-02-create-new-file.cf9a330a3a9cff92.webp)

### फाइन-ट्यूनिंग के लिए डेटा सेट तैयार करें

इस अभ्यास में, आप *download_dataset.py* फ़ाइल चलाकर *ultrachat_200k* डेटा सेट को अपने स्थानीय पर्यावरण में डाउनलोड करेंगे। फिर आप इस डेटा सेट का उपयोग Azure Machine Learning में Phi-3 मॉडल को फाइन-ट्यून करने के लिए करेंगे।

इस अभ्यास में, आप:

- *download_dataset.py* फ़ाइल में कोड जोड़ेंगे ताकि डेटा सेट डाउनलोड हो सके।
- *download_dataset.py* फ़ाइल चलाकर डेटा सेट को अपने स्थानीय पर्यावरण में डाउनलोड करेंगे।

#### *download_dataset.py* का उपयोग करके अपना डेटा सेट डाउनलोड करें

1. Visual Studio Code में *download_dataset.py* फ़ाइल खोलें।

1. *download_dataset.py* फ़ाइल में निम्नलिखित कोड जोड़ें।

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # निर्दिष्ट नाम, कॉन्फ़िगरेशन, और विभाजन अनुपात के साथ डेटासेट लोड करें
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # डेटासेट को ट्रेन और टेस्ट सेट में विभाजित करें (80% ट्रेन, 20% टेस्ट)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # यदि निर्देशिका मौजूद नहीं है तो उसे बनाएँ
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # फ़ाइल को लिखने के मोड में खोलें
        with open(filepath, 'w', encoding='utf-8') as f:
            # डेटासेट के प्रत्येक रिकॉर्ड पर पुनरावृत्ति करें
            for record in dataset:
                # रिकॉर्ड को JSON ऑब्जेक्ट के रूप में डंप करें और इसे फ़ाइल में लिखें
                json.dump(record, f)
                # रिकॉर्ड को अलग करने के लिए एक नई लाइन कैरेक्टर लिखें
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ULTRACHAT_200k डेटासेट को एक विशिष्ट कॉन्फ़िगरेशन और विभाजन अनुपात के साथ लोड और विभाजित करें
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # विभाजन से ट्रेन और टेस्ट डेटासेट निकालें
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ट्रेन डेटासेट को JSONL फ़ाइल में सहेजें
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # टेस्ट डेटासेट को अलग JSONL फ़ाइल में सहेजें
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. टर्मिनल के अंदर निम्न कमांड टाइप करें ताकि स्क्रिप्ट चलाकर डेटा सेट को अपने स्थानीय पर्यावरण में डाउनलोड किया जा सके।

    ```console
    python download_dataset.py
    ```

1. सत्यापित करें कि डेटा सेट सफलतापूर्वक आपके स्थानीय *finetune-phi/data* निर्देशिका में सहेजे गए हैं।

> [!NOTE]
>
> #### डेटा सेट आकार और फाइन-ट्यूनिंग समय पर नोट
>
> इस ट्यूटोरियल में, आप केवल डेटा सेट का 1% उपयोग कर रहे हैं (`split='train[:1%]'`)। यह डेटा की मात्रा को काफी घटा देता है, जिससे अपलोड और फाइन-ट्यूनिंग दोनों प्रक्रिया तेज हो जाती है। आप प्रशिक्षण समय और मॉडल प्रदर्शन के बीच सही संतुलन खोजने के लिए प्रतिशत समायोजित कर सकते हैं। डेटा सेट के छोटे हिस्से का उपयोग करने से फाइन-ट्यूनिंग के लिए आवश्यक समय कम हो जाता है, जिससे ट्यूटोरियल के लिए प्रक्रिया अधिक प्रबंधनीय हो जाती है।

## परिदृश्य 2: Phi-3 मॉडल को फाइन-ट्यून करें और Azure Machine Learning Studio में तैनात करें

### Phi-3 मॉडल को फाइन-ट्यून करें

इस अभ्यास में, आप Azure Machine Learning Studio में Phi-3 मॉडल को फाइन-ट्यून करेंगे।

इस अभ्यास में, आप:

- फाइन-ट्यूनिंग के लिए कंप्यूटर क्लस्टर बनाएंगे।
- Azure Machine Learning Studio में Phi-3 मॉडल को फाइन-ट्यून करेंगे।

#### फाइन-ट्यूनिंग के लिए कंप्यूटर क्लस्टर बनाएं

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. बाईं तरफ के टैब में **Compute** चुनें।

1. नेविगेशन मेनू में से **Compute clusters** चुनें।

1. **+ New** चुनें।

    ![कंप्यूट चुनें।](../../../../../../translated_images/hi/06-01-select-compute.a29cff290b480252.webp)

1. निम्न कार्य करें:

    - उस **Region** का चयन करें जिसे आप उपयोग करना चाहते हैं।
    - **Virtual machine tier** को **Dedicated** चुनें।
    - **Virtual machine type** को **GPU** चुनें।
    - **Virtual machine size** फ़िल्टर को **Select from all options** चुनें।
    - **Virtual machine size** को **Standard_NC24ads_A100_v4** चुनें।

    ![क्लस्टर बनाएं।](../../../../../../translated_images/hi/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** चुनें।

1. निम्न कार्य करें:

    - **Compute name** दर्ज करें। यह एक अनूठा मान होना चाहिए।
    - **Minimum number of nodes** को **0** चुनें।
    - **Maximum number of nodes** को **1** चुनें।
    - **Idle seconds before scale down** को **120** सेट करें।

    ![क्लस्टर बनाएं।](../../../../../../translated_images/hi/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** चुनें।

#### Phi-3 मॉडल को फाइन-ट्यून करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. उस Azure Machine Learning वर्कस्पेस को चुनें जिसे आपने बनाया था।

    ![अपने बनाए हुए वर्कस्पेस का चयन करें।](../../../../../../translated_images/hi/06-04-select-workspace.a92934ac04f4f181.webp)

1. निम्न कार्य करें:

    - बाईं ओर की पट्टी में से **Model catalog** चुनें।
    - **search bar** में *phi-3-mini-4k* टाइप करें और दिखाई देने वाले विकल्पों में से **Phi-3-mini-4k-instruct** चुनें।

    ![phi-3-mini-4k टाइप करें।](../../../../../../translated_images/hi/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. नेविगेशन मेनू से **Fine-tune** चुनें।

    ![Fine tune चुनें।](../../../../../../translated_images/hi/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. निम्न कार्य करें:

    - **Select task type** को **Chat completion** चुनें।
    - **+ Select data** चुनकर **Training data** अपलोड करें।
    - Validation data अपलोड प्रकार को **Provide different validation data** चुनें।
    - **+ Select data** चुनकर **Validation data** अपलोड करें।

    ![फाइन-ट्यूनिंग पेज भरें।](../../../../../../translated_images/hi/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> आप **Advanced settings** का चयन करके कॉन्फ़िगरेशन जैसे कि **learning_rate** और **lr_scheduler_type** को अपनी आवश्यकताओं के अनुसार अनुकूलित कर सकते हैं ताकि फाइन-ट्यूनिंग प्रक्रिया को बेहतर बनाया जा सके।

1. **Finish** चुनें।

1. इस अभ्यास में, आपने सफलतापूर्वक Azure Machine Learning का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून किया। कृपया ध्यान दें कि फाइन-ट्यूनिंग प्रक्रिया में काफी समय लग सकता है। फाइन-ट्यूनिंग जॉब चलाने के बाद, आपको इसके पूरा होने तक प्रतीक्षा करनी होगी। आप Azure Machine Learning वर्कस्पेस के बाईं ओर के टैब में Jobs सेक्शन में जाकर फाइन-ट्यूनिंग जॉब की स्थिति देख सकते हैं। अगले सेक्शन में, आप फाइन-ट्यून किए गए मॉडल को तैनात करेंगे और इसे Prompt flow के साथ एकीकृत करेंगे।

    ![फाइनट्यूनिंग जॉब देखें।](../../../../../../translated_images/hi/06-08-output.2bd32e59930672b1.webp)

### फाइन-ट्यून किए गए Phi-3 मॉडल को तैनात करें

फाइन-ट्यून किए गए Phi-3 मॉडल को Prompt flow के साथ एकीकृत करने के लिए, आपको मॉडल को तैनात करना होगा ताकि यह रियल-टाइम इनफेरेंस के लिए उपलब्ध हो सके। इस प्रक्रिया में मॉडल का पंजीकरण, ऑनलाइन एंडपॉइंट बनाना और मॉडल का तैनाती शामिल है।

इस अभ्यास में, आप:

- Azure Machine Learning वर्कस्पेस में फाइन-ट्यून किए गए मॉडल को रजिस्टर करेंगे।
- एक ऑनलाइन एंडपॉइंट बनाएंगे।
- पंजीकृत फाइन-ट्यून किए गए Phi-3 मॉडल को तैनात करेंगे।

#### फाइन-ट्यून किए गए मॉडल को रजिस्टर करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. उस Azure Machine Learning वर्कस्पेस को चुनें जिसे आपने बनाया था।

    ![अपने बनाए हुए वर्कस्पेस का चयन करें।](../../../../../../translated_images/hi/06-04-select-workspace.a92934ac04f4f181.webp)

1. बाईं ओर के टैब में से **Models** चुनें।
1. **+ Register** चुनें।
1. **From a job output** चुनें।

    ![मॉडल रजिस्टर करें।](../../../../../../translated_images/hi/07-01-register-model.ad1e7cc05e4b2777.webp)

1. उस जॉब का चयन करें जिसे आपने बनाया था।

    ![जॉब चुनें।](../../../../../../translated_images/hi/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** चुनें।

1. **Model type** को **MLflow** चुनें।

1. सुनिश्चित करें कि **Job output** चुना गया हो; यह स्वचालित रूप से चुना जाना चाहिए।

    ![आउटपुट चुनें।](../../../../../../translated_images/hi/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** चुनें।

3. **Register** चुनें।

    ![रजिस्टर चुनें।](../../../../../../translated_images/hi/07-04-register.fd82a3b293060bc7.webp)

4. आप अपने रजिस्टर्ड मॉडल को बाईं ओर के टैब में **Models** मेनू पर जाकर देख सकते हैं।

    ![रजिस्टर्ड मॉडल।](../../../../../../translated_images/hi/07-05-registered-model.7db9775f58dfd591.webp)

#### फाइन-ट्यून किए गए मॉडल को तैनात करें

1. उस Azure Machine Learning वर्कस्पेस पर जाएं जिसे आपने बनाया था।

1. बाईं ओर के टैब में से **Endpoints** चुनें।

1. नेविगेशन मेनू में से **Real-time endpoints** चुनें।

    ![एंडपॉइंट बनाएं।](../../../../../../translated_images/hi/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** चुनें।

1. उस पंजीकृत मॉडल का चयन करें जिसे आपने बनाया था।

    ![पंजीकृत मॉडल चुनें।](../../../../../../translated_images/hi/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** चुनें।

1. निम्न कार्य करें:

    - **Virtual machine** को *Standard_NC6s_v3* चुनें।
    - अपने उपयोग के लिए **Instance count** चुनें। उदाहरण के लिए, *1*।
    - **Endpoint** को **New** चुनें ताकि नया एंडपॉइंट बनाया जा सके।
    - **Endpoint name** दर्ज करें। यह एक अनूठा मान होना चाहिए।
    - **Deployment name** दर्ज करें। यह एक अनूठा मान होना चाहिए।

    ![तैनाती सेटिंग भरें।](../../../../../../translated_images/hi/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** चुनें।

> [!WARNING]
> अपने खाते में अतिरिक्त शुल्क से बचने के लिए, कृपया Azure Machine Learning वर्कस्पेस में बनाए गए एंडपॉइंट को हटा दें।
>

#### Azure Machine Learning वर्कस्पेस में तैनाती की स्थिति जांचें

1. Azure Machine Learning वर्कस्पेस पर जाएं जिसे आपने बनाया था।

1. बाईं ओर के टैब में से **Endpoints** चुनें।

1. उस एंडपॉइंट का चयन करें जिसे आपने बनाया था।

    ![एंडपॉइंट चुनें](../../../../../../translated_images/hi/07-09-check-deployment.325d18cae8475ef4.webp)

1. इस पेज पर, आप तैनाती प्रक्रिया के दौरान एंडपॉइंट्स को प्रबंधित कर सकते हैं।

> [!NOTE]
> तैनाती पूरी होने के बाद, सुनिश्चित करें कि **Live traffic** को **100%** पर सेट किया गया है। यदि ऐसा नहीं है, तो ट्रैफ़िक सेटिंग समायोजित करने के लिए **Update traffic** चुनें। ध्यान दें कि यदि ट्रैफ़िक 0% पर सेट है, तो आप मॉडल का परीक्षण नहीं कर सकते।
>
> ![ट्रैफ़िक सेट करें।](../../../../../../translated_images/hi/07-10-set-traffic.085b847e5751ff3d.webp)
>

## परिदृश्य 3: Prompt flow के साथ एकीकृत करें और Microsoft Foundry में अपने कस्टम मॉडल के साथ चैट करें

### कस्टम Phi-3 मॉडल को Prompt flow के साथ एकीकृत करें

अपना फाइन-ट्यून किया हुआ मॉडल सफलतापूर्वक तैनात करने के बाद, आप अब इसे Prompt Flow के साथ एकीकृत कर सकते हैं ताकि आप अपने मॉडल का रियल-टाइम एप्लिकेशन में उपयोग कर सकें, जिससे आपके कस्टम Phi-3 मॉडल के साथ विभिन्न इंटरैक्टिव कार्य संभव हो सकें।

इस अभ्यास में, आप:

- Microsoft Foundry Hub बनाएंगे।
- Microsoft Foundry प्रोजेक्ट बनाएंगे।
- Prompt flow बनाएंगे।
- फाइन-ट्यून किए गए Phi-3 मॉडल के लिए एक कस्टम कनेक्शन जोड़ेंगे।
- Prompt flow को सेटअप करेंगे ताकि आप अपने कस्टम Phi-3 मॉडल के साथ चैट कर सकें।

> [!NOTE]
> आप Azure ML Studio का उपयोग करके भी Promptflow के साथ एकीकरण कर सकते हैं। एक ही एकीकरण प्रक्रिया Azure ML Studio पर लागू की जा सकती है।

#### Microsoft Foundry Hub बनाएं

प्रोजेक्ट बनाने से पहले आपको एक हब बनाना होगा। हब एक संसाधन समूह की तरह काम करता है, जो Microsoft Foundry में कई प्रोजेक्ट्स को व्यवस्थित और प्रबंधित करने की अनुमति देता है।
1. Visit करें [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)।

1. बाईं ओर के टैब से **All hubs** चुनें।

1. नेविगेशन मेन्यू से **+ New hub** चुनें।

    ![Create hub.](../../../../../../translated_images/hi/08-01-create-hub.8f7dd615bb8d9834.webp)

1. निम्नलिखित कार्य करें:

    - **Hub name** दर्ज करें। यह एक अनूठा मान होना चाहिए।
    - अपना Azure **Subscription** चुनें।
    - उपयोग के लिए **Resource group** चुनें (आवश्यक होने पर नया बनाएं)।
    - वह **Location** चुनें जिसका आप उपयोग करना चाहते हैं।
    - उपयोग के लिए **Connect Azure AI Services** चुनें (आवश्यक होने पर नया बनाएं)।
    - **Connect Azure AI Search** को **Skip connecting** चुनें।

    ![Fill hub.](../../../../../../translated_images/hi/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** चुनें।

#### Microsoft Foundry प्रोजेक्ट बनाएं

1. आपने जो Hub बनाया है उसमें, बाईं ओर के टैब से **All projects** चुनें।

1. नेविगेशन मेन्यू से **+ New project** चुनें।

    ![Select new project.](../../../../../../translated_images/hi/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** दर्ज करें। यह एक अनूठा मान होना चाहिए।

    ![Create project.](../../../../../../translated_images/hi/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** चुनें।

#### फाइन-ट्यून किए गए Phi-3 मॉडल के लिए कस्टम कनेक्शन जोड़ें

अपने कस्टम Phi-3 मॉडल को Prompt flow के साथ एकीकृत करने के लिए, आपको मॉडल के endpoint और key को एक कस्टम कनेक्शन में सेव करना होगा। यह सेटअप आपके कस्टम Phi-3 मॉडल तक Prompt flow में पहुँच सुनिश्चित करता है।

#### फाइन-ट्यून किए गए Phi-3 मॉडल की api key और endpoint uri सेट करें

1. Visit करें [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)।

1. आपने जो Azure Machine learning workspace बनाया है, वहां नेविगेट करें।

1. बाईं ओर के टैब से **Endpoints** चुनें।

    ![Select endpoints.](../../../../../../translated_images/hi/08-06-select-endpoints.aff38d453bcf9605.webp)

1. आपने जो endpoint बनाया है उसे चुनें।

    ![Select endpoints.](../../../../../../translated_images/hi/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. नेविगेशन मेन्यू से **Consume** चुनें।

1. अपनी **REST endpoint** और **Primary key** कॉपी करें।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/hi/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### कस्टम कनेक्शन जोड़ें

1. Visit करें [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)।

1. आपने जो Microsoft Foundry प्रोजेक्ट बनाया है, वहां नेविगेट करें।

1. आपने जो प्रोजेक्ट बनाया है उसमें, बाईं ओर के टैब से **Settings** चुनें।

1. **+ New connection** चुनें।

    ![Select new connection.](../../../../../../translated_images/hi/08-09-select-new-connection.02eb45deadc401fc.webp)

1. नेविगेशन मेन्यू से **Custom keys** चुनें।

    ![Select custom keys.](../../../../../../translated_images/hi/08-10-select-custom-keys.856f6b2966460551.webp)

1. निम्नलिखित कार्य करें:

    - **+ Add key value pairs** चुनें।
    - Key नाम के लिए, **endpoint** दर्ज करें और Azure ML Studio से कॉपी किया गया endpoint मान फ़ील्ड में पेस्ट करें।
    - फिर से **+ Add key value pairs** चुनें।
    - Key नाम के लिए, **key** दर्ज करें और Azure ML Studio से कॉपी किया गया key मान फ़ील्ड में पेस्ट करें।
    - Keys जोड़ने के बाद, **is secret** को चुनें ताकि key सार्वजनिक न हो।

    ![Add connection.](../../../../../../translated_images/hi/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** चुनें।

#### Prompt flow बनाएं

आपने Microsoft Foundry में एक कस्टम कनेक्शन जोड़ दिया है। अब, निम्नलिखित चरणों का उपयोग करके एक Prompt flow बनाएं। फिर, इस Prompt flow को कस्टम कनेक्शन से जोड़ेंगे ताकि आप फाइन-ट्यून किए गए मॉडल को Prompt flow के भीतर इस्तेमाल कर सकें।

1. आपने जो Microsoft Foundry प्रोजेक्ट बनाया है, वहां नेविगेट करें।

1. बाईं ओर के टैब से **Prompt flow** चुनें।

1. नेविगेशन मेन्यू से **+ Create** चुनें।

    ![Select Promptflow.](../../../../../../translated_images/hi/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. नेविगेशन मेन्यू से **Chat flow** चुनें।

    ![Select chat flow.](../../../../../../translated_images/hi/08-13-select-flow-type.2ec689b22da32591.webp)

1. उपयोग के लिए **Folder name** दर्ज करें।

    ![Enter name.](../../../../../../translated_images/hi/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** चुनें।

#### अपने कस्टम Phi-3 मॉडल के साथ Prompt flow से चैट सेट करें

आपको फाइन-ट्यून किए गए Phi-3 मॉडल को Prompt flow में एकीकृत करना होगा। हालाँकि, उपलब्ध Prompt flow इस उद्देश्य के लिए डिज़ाइन नहीं है। इसलिए, आपको कस्टम मॉडल की एकीकरण सक्षम करने के लिए Prompt flow को पुनः डिज़ाइन करना होगा।

1. Prompt flow में, मौजूदा flow को पुनर्निर्मित करने के लिए निम्न कार्य करें:

    - **Raw file mode** चुनें।
    - *flow.dag.yml* फ़ाइल में मौजूद सभी कोड हटाएँ।
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

    ![Select raw file mode.](../../../../../../translated_images/hi/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Prompt flow में अपने कस्टम Phi-3 मॉडल का उपयोग करने के लिए *integrate_with_promptflow.py* फ़ाइल में निम्न कोड जोड़ें।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # लॉगिंग सेटअप
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

        # "connection" कस्टम कनेक्शन का नाम है, "endpoint", "key" कस्टम कनेक्शन में कुंजी हैं
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
            
            # पूर्ण JSON प्रतिक्रिया लॉग करें
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

    ![Paste prompt flow code.](../../../../../../translated_images/hi/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry में Prompt flow के उपयोग के बारे में अधिक विस्तृत जानकारी के लिए, आप देख सकते हैं [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)।

1. अपने मॉडल से चैट सक्षम करने के लिए **Chat input**, **Chat output** चुनें।

    ![Input Output.](../../../../../../translated_images/hi/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. अब आप अपने कस्टम Phi-3 मॉडल से चैट करने के लिए तैयार हैं। अगले अभ्यास में, आप सीखेंगे कि Prompt flow कैसे शुरू करें और इसे अपने फाइन-ट्यून किए गए Phi-3 मॉडल के साथ चैट करने के लिए कैसे उपयोग करें।

> [!NOTE]
>
> पुनर्निर्मित flow नीचे दी गई छवि की तरह दिखना चाहिए:
>
> ![Flow example.](../../../../../../translated_images/hi/08-18-graph-example.d6457533952e690c.webp)
>

### अपने कस्टम Phi-3 मॉडल के साथ चैट करें

अब जब आपने अपने कस्टम Phi-3 मॉडल को फाइन-ट्यून और Prompt flow के साथ एकीकृत कर लिया है, तो आप इसके साथ इंटरैक्ट करना शुरू करने के लिए तैयार हैं। यह अभ्यास आपको अपने मॉडल के साथ चैट सेटअप और प्रारंभ करने की प्रक्रिया में मार्गदर्शन करेगा। इन चरणों का पालन करके, आप अपने फाइन-ट्यून किए गए Phi-3 मॉडल की क्षमताओं का पूरी तरह से उपयोग कर पाएंगे, विभिन्न कार्यों और संवादों के लिए।

- Prompt flow का उपयोग करके अपने कस्टम Phi-3 मॉडल के साथ चैट करें।

#### Prompt flow शुरू करें

1. Prompt flow शुरू करने के लिए **Start compute sessions** चुनें।

    ![Start compute session.](../../../../../../translated_images/hi/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. पैरामीटर नवीनीकृत करने के लिए **Validate and parse input** चुनें।

    ![Validate input.](../../../../../../translated_images/hi/09-02-validate-input.317c76ef766361e9.webp)

1. आपने जो कस्टम कनेक्शन बनाया था, उसके **connection** के **Value** को चुनें। उदाहरण के लिए, *connection*।

    ![Connection.](../../../../../../translated_images/hi/09-03-select-connection.99bdddb4b1844023.webp)

#### अपने कस्टम मॉडल के साथ चैट करें

1. **Chat** चुनें।

    ![Select chat.](../../../../../../translated_images/hi/09-04-select-chat.61936dce6612a1e6.webp)

1. परिणामों का एक उदाहरण यहाँ है: अब आप अपने कस्टम Phi-3 मॉडल से चैट कर सकते हैं। यह सुझाव दिया जाता है कि आप फाइन-ट्यूनिंग में उपयोग किए गए डेटा के आधार पर प्रश्न पूछें।

    ![Chat with prompt flow.](../../../../../../translated_images/hi/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->