# Microsoft Foundry मध्ये Prompt flow सह सानुकूल Phi-3 मॉडेल्स फीन्स ट्यून आणि एकत्रित करा

ह्या End-to-end (E2E) नमुन्यावर Microsoft Tech Community मधील "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" मार्गदर्शकावर आधारित आहे. हे Microsoft Foundry मध्ये Prompt flow सह सानुकूल Phi-3 मॉडेल्स फीन्स ट्यून, तैनात करणे आणि एकत्रित करण्याच्या प्रक्रियांना ओळखून देतो.
E2E नमुन्याच्या विरुद्ध, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ज्यात स्थानिक पातळीवर कोड चालवणे होते, हा ट्यूटोरियल पूर्णपणे Azure AI / ML Studio मध्ये आपल्या मॉडेलचा फीन्स ट्यून आणि एकत्रितीकरणावर केंद्रित आहे.

## आढावा

या E2E नमुन्यात, आपण Phi-3 मॉडेल कसे फीन्स ट्यून करायचे आणि ते Microsoft Foundry मधील Prompt flow सह कसे एकत्रित करायचे हे शिकाल. Azure AI / ML Studio चा उपयोग करून, आपण सानुकूल AI मॉडेल्स तैनात आणि वापरण्यासाठी एक कार्यप्रवाह स्थापित कराल. हा E2E नमुना तीन परिस्थितींमध्ये विभागलेला आहे:

**परिस्थिती 1: Azure संसाधने सेट करा आणि फीन्स ट्यूनिंगसाठी तयार व्हा**

**परिस्थिती 2: Phi-3 मॉडेल फीन्स ट्यून करा आणि Azure मशीन लर्निंग स्टुडिओमध्ये तैनात करा**

**परिस्थिती 3: Prompt flow सह एकत्रित करा आणि Microsoft Foundry मधील आपल्या सानुकूल मॉडेलसह संवाद साधा**

हे या E2E नमुन्याचे एक आढावा आहे.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/mr/00-01-architecture.198ba0f1ae6d841a.webp)

### अनुक्रमणिका

1. **[परिस्थिती 1: Azure संसाधने सेट करा आणि फीन्स ट्यूनिंगसाठी तयार व्हा](#परिस्थिती-1-azure-संसाधने-सेट-करा-आणि-फीन्स-ट्यूनिंगसाठी-तयार-व्हा)**
    - [Azure मशीन लर्निंग वर्कस्पेस तयार करा](#azure-मशीन-लर्निंग-वर्कस्पेस-तयार-करा)
    - [Azure सबस्क्रिप्शनमध्ये GPU कोटा विनंती करा](#azure-subscription-मध्ये-gpu-कोटा-विनंती-करा)
    - [भूमिका असाइनमेंट जोडा](#भूमिका-असाइनमेंट-जोडा)
    - [प्रोजेक्ट सेट करा](#प्रोजेक्ट-सेट-करा)
    - [फीन्स ट्यूनिंगसाठी डेटासेट तयार करा](#फाइन-ट्यूनिंगसाठी-डेटासेट-तयार-करा)

1. **[परिस्थिती 2: Phi-3 मॉडेल फीन्स ट्यून करा आणि Azure मशीन लर्निंग स्टुडिओमध्ये तैनात करा](#परिदृश्य-2-phi-3-मॉडेल-फाइन-ट्यून-करा-आणि-azure-मशीन-लर्निंग-स्टुडिओमध्ये-डिप्लॉय-करा)**
    - [Phi-3 मॉडेल फीन्स ट्यून करा](#phi-3-मॉडेल-फाइन-ट्यून-करा)
    - [फीन्स ट्यून केलेले Phi-3 मॉडेल तैनात करा](#फाइन-ट्यून-केलेला-phi-3-मॉडेल-डिप्लॉय-करा)

1. **[परिस्थिती 3: Prompt flow सह एकत्रित करा आणि Microsoft Foundry मध्ये आपल्या सानुकूल मॉडेलसह संवाद साधा](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [सानुकूल Phi-3 मॉडेल Prompt flow सह एकत्रित करा](#कस्टम-phi-3-मॉडेल-prompt-flow-सोबत-एकत्रित-करा)
    - [आपल्या सानुकूल Phi-3 मॉडेलसोबत संवाद साधा](#तुमच्या-कस्टम-phi-3-मॉडेलसोबत-चॅट-करा)

## परिस्थिती 1: Azure संसाधने सेट करा आणि फीन्स ट्यूनिंगसाठी तयार व्हा

### Azure मशीन लर्निंग वर्कस्पेस तयार करा

1. पोर्टल पृष्ठाच्या वरच्या भागात असलेल्या **शोध बार** मध्ये *azure machine learning* टाइप करा आणि दिसलेल्या पर्यायांमधून **Azure Machine Learning** निवडा.

    ![Type azure machine learning.](../../../../../../translated_images/mr/01-01-type-azml.acae6c5455e67b4b.webp)

2. नेव्हिगेशन मेनूमधून **+ Create** निवडा.

3. नेव्हिगेशन मेनूमधून **New workspace** निवडा.

    ![Select new workspace.](../../../../../../translated_images/mr/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. पुढील कार्य करा:

    - आपला Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा (गरज असल्यास नवीन तयार करा).
    - **Workspace Name** टाका. हा एक अद्वितीय मूल्य असणे आवश्यक आहे.
    - आपण वापरणार **Region** निवडा.
    - वापरण्यासाठी **Storage account** निवडा (गरज असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Key vault** निवडा (गरज असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Application insights** निवडा (गरज असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Container registry** निवडा (गरज असल्यास नवीन तयार करा).

    ![Fill azure machine learning.](../../../../../../translated_images/mr/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** निवडा.

6. **Create** वर क्लिक करा.

### Azure Subscription मध्ये GPU कोटा विनंती करा

या ट्यूटोरियलमध्ये, आपण GPUs वापरून Phi-3 मॉडेल कसा फीन्स ट्यून आणि तैनात करायचा ते शिकाल. फीन्स ट्यूनिंगसाठी आपण *Standard_NC24ads_A100_v4* GPU वापरणार आहात, ज्यासाठी कोटा विनंती आवश्यक आहे. तैनातीसाठी आपण *Standard_NC6s_v3* GPU वापरणार आहात, ज्यासाठी देखील कोटा विनंती आवश्यक आहे.

> [!NOTE]
>
> फक्त Pay-As-You-Go सबस्क्रिप्शन (मानक सबस्क्रिप्शन प्रकार) साठी GPU वाटप पात्र आहे; लाभ सबस्क्रिप्शन्स सध्या समर्थित नाहीत.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ला भेट द्या.

1. *Standard NCADSA100v4 Family* कोटासाठी विनंती करण्यासाठी खालील कामे करा:

    - डाव्या बाजूतील टॅबमधून **Quota** निवडा.
    - वापरायच्या **Virtual machine family** निवडा. उदा., **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** निवडा, ज्यामध्ये *Standard_NC24ads_A100_v4* GPU समाविष्ट आहे.
    - नेव्हिगेशन मेनूमधून **Request quota** निवडा.

        ![Request quota.](../../../../../../translated_images/mr/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota पृष्ठावर, आपल्याला वापरायच्या **New cores limit** ची संख्या टाका. उदा., 24.
    - Request quota पृष्ठावर, GPU कोटासाठी **Submit** निवडा.

1. *Standard NCSv3 Family* कोटासाठी विनंती करण्यासाठी खालील कामे करा:

    - डाव्या बाजूतील टॅबमधून **Quota** निवडा.
    - वापरायच्या **Virtual machine family** निवडा. उदा., **Standard NCSv3 Family Cluster Dedicated vCPUs**, ज्यामध्ये *Standard_NC6s_v3* GPU आहे.
    - नेव्हिगेशन मेनूमधून **Request quota** निवडा.
    - Request quota पृष्ठावर, आपल्याला वापरायच्या **New cores limit** ची संख्या टाका. उदा., 24.
    - Request quota पृष्ठावर, GPU कोटासाठी **Submit** निवडा.

### भूमिका असाइनमेंट जोडा

आपले मॉडेल्स फीन्स ट्यून आणि तैनात करण्यासाठी, प्रथम आपल्याला User Assigned Managed Identity (UAI) तयार करणे आणि त्याला योग्य परवानग्या देणे आवश्यक आहे. हे UAI तैनात करताना प्रमाणीकरणासाठी वापरले जाईल.

#### User Assigned Managed Identity (UAI) तयार करा

1. पोर्टल पृष्ठाच्या वरच्या शोध बारमध्ये *managed identities* टाइप करा आणि दिसलेल्या पर्यायांमधून **Managed Identities** निवडा.

    ![Type managed identities.](../../../../../../translated_images/mr/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** निवडा.

    ![Select create.](../../../../../../translated_images/mr/03-02-select-create.92bf8989a5cd98f2.webp)

1. पुढील कामे करा:

    - आपला Azure **Subscription** निवडा.
    - वापरायचा **Resource group** निवडा (गरज असल्यास नवीन तयार करा).
    - आपण वापरणार **Region** निवडा.
    - **Name** टाका. हे अद्वितीय असणे आवश्यक आहे.

    ![Select create.](../../../../../../translated_images/mr/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** निवडा.

1. **+ Create** क्लिक करा.

#### Managed Identity ला Contributor भूमिका असाइन करा

1. आपण तयार केलेल्या Managed Identity रिसोर्सवर जा.

1. डाव्या बाजूच्या टॅबमधून **Azure role assignments** निवडा.

1. नेव्हिगेशन मेनूमधून **+Add role assignment** निवडा.

1. Add role assignment पृष्ठावर, पुढील कामे करा:
    - **Scope** म्हणून **Resource group** निवडा.
    - आपला Azure **Subscription** निवडा.
    - वापरायचा **Resource group** निवडा.
    - भूमिका **Contributor** निवडा.

    ![Fill contributor role.](../../../../../../translated_images/mr/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** वर क्लिक करा.

#### Managed Identity ला Storage Blob Data Reader भूमिका असाइन करा

1. पोर्टल पृष्ठाच्या वरच्या शोध बारमध्ये *storage accounts* टाइप करा आणि दिसलेल्या पर्यायांमधून **Storage accounts** निवडा.

    ![Type storage accounts.](../../../../../../translated_images/mr/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. आपण तयार केलेल्या Azure Machine Learning वर्कस्पेसशी संबंधित स्टोरेज अकाउंट निवडा. उदा., *finetunephistorage*.

1. Add role assignment पृष्ठावर जाण्यासाठी खालील कार्य करा:

    - आपण तयार केलेल्या Azure Storage अकाउंटवर जा.
    - डाव्या टॅबमधून **Access Control (IAM)** निवडा.
    - नेव्हिगेशन मेनूमधून **+ Add** निवडा.
    - नेव्हिगेशन मेनूमधून **Add role assignment** निवडा.

    ![Add role.](../../../../../../translated_images/mr/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment पृष्ठावर पुढील कार्य करा:

    - भूमिका पृष्ठावर, शोध बारमध्ये *Storage Blob Data Reader* टाइप करा आणि दिसलेल्या पर्यायांमधून **Storage Blob Data Reader** निवडा.
    - भूमिका पृष्ठावर **Next** निवडा.
    - सदस्य पृष्ठावर, **Assign access to** म्हणून **Managed identity** निवडा.
    - सदस्य पृष्ठावर **+ Select members** निवडा.
    - Select managed identities पृष्ठावर, आपला Azure **Subscription** निवडा.
    - Select managed identities पृष्ठावर, **Managed identity** म्हणून **Manage Identity** निवडा.
    - Select managed identities पृष्ठावर, आपण तयार केलेले Manage Identity निवडा. उदा., *finetunephi-managedidentity*.
    - Select managed identities पृष्ठावर **Select** निवडा.

    ![Select managed identity.](../../../../../../translated_images/mr/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** निवडा.

#### Managed Identity ला AcrPull भूमिका असाइन करा

1. पोर्टल पृष्ठाच्या वरच्या शोध बारमध्ये *container registries* टाइप करा आणि दिसलेल्या पर्यायांमधून **Container registries** निवडा.

    ![Type container registries.](../../../../../../translated_images/mr/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning वर्कस्पेसशी संबंधित कंटेनर रजिस्ट्री निवडा. उदा., *finetunephicontainerregistry*

1. Add role assignment पृष्ठावर जाण्यासाठी खालील काम करा:

    - डाव्या बाजूच्या टॅबमधून **Access Control (IAM)** निवडा.
    - नेव्हिगेशन मेनूमधून **+ Add** निवडा.
    - नेव्हिगेशन मेनूमधून **Add role assignment** निवडा.

1. Add role assignment पृष्ठावर खालील काम करा:

    - भूमिका पृष्ठावर, शोध बारमध्ये *AcrPull* टाइप करा आणि दिसलेल्या पर्यायांमधून **AcrPull** निवडा.
    - भूमिका पृष्ठावर **Next** निवडा.
    - सदस्य पृष्ठावर, **Assign access to** म्हणून **Managed identity** निवडा.
    - सदस्य पृष्ठावर **+ Select members** निवडा.
    - Select managed identities पृष्ठावर, आपला Azure **Subscription** निवडा.
    - Select managed identities पृष्ठावर, **Managed identity** म्हणून **Manage Identity** निवडा.
    - Select managed identities पृष्ठावर, आपण तयार केलेले Manage Identity निवडा. उदा., *finetunephi-managedidentity*.
    - Select managed identities पृष्ठावर **Select** निवडा.
    - **Review + assign** निवडा.

### प्रोजेक्ट सेट करा

फीन्स ट्यूनिंगसाठी आवश्यक डेटासेट डाउनलोड करण्यासाठी, आपण स्थानिक पर्यावरण सेट कराल.

ह्या व्यायामात, आपण

- कामासाठी एक फोल्डर तयार कराल.
- एक व्हर्च्युअल एन्व्हायर्नमेंट तयार कराल.
- आवश्यक पॅकेजेस इन्स्टॉल कराल.
- डेटासेट डाउनलोड करण्यासाठी *download_dataset.py* फाइल तयार कराल.

#### कामासाठी फोल्डर तयार करा

1. टर्मिनल विंडो उघडा आणि डिफॉल्ट पाथ मध्ये *finetune-phi* नावाचा फोल्डर तयार करण्यासाठी खालील आदेश टाइप करा.

    ```console
    mkdir finetune-phi
    ```

2. आपल्या टर्मिनलमध्ये खालील आदेश टाकून तयार केलेल्या *finetune-phi* फोल्डरमध्ये जा.

    ```console
    cd finetune-phi
    ```

#### व्हर्च्युअल एन्व्हायर्नमेंट तयार करा

1. आपल्या टर्मिनलमध्ये *venv* नावाचा व्हर्च्युअल एन्व्हायर्नमेंट तयार करण्यासाठी खालील आदेश टाइप करा.
    ```console
    python -m venv .venv
    ```

2. वर्च्युअल वातावरण सक्रिय करण्यासाठी आपल्या टर्मिनलमध्ये खालील कमांड टाइप करा.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> जर ते यशस्वी झाले, तर कमांड प्रॉम्प्टच्या आधी *(.venv)* दिसू लागले पाहिजे.

#### आवश्यक पॅकेजेस स्थापित करा

1. आवश्यक पॅकेजेस स्थापित करण्यासाठी आपल्या टर्मिनलमध्ये खालील कमांड टाइप करा.

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` तयार करा

> [!NOTE]
> पूर्ण फोल्डर संरचना:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** उघडा.

1. मेनू बारमधून **File** निवडा.

1. **Open Folder** निवडा.

1. आपण तयार केलेला *finetune-phi* फोल्डर निवडा, जो *C:\Users\yourUserName\finetune-phi* येथे आहे.

    ![तुम्ही तयार केलेला फोल्डर निवडा.](../../../../../../translated_images/mr/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code च्या डाव्या पॅनेलमध्ये उजवीक्लिक करा आणि *download_dataset.py* नावाचा नवीन फाइल तयार करण्यासाठी **New File** निवडा.

    ![नवीन फाइल तयार करा.](../../../../../../translated_images/mr/04-02-create-new-file.cf9a330a3a9cff92.webp)

### फाइन-ट्यूनिंगसाठी डेटासेट तयार करा

या अभ्यासात, आपण *download_dataset.py* फाइल चालवून *ultrachat_200k* डेटासेट्स आपल्या स्थानिक वातावरणात डाउनलोड कराल. नंतर आपण ह्या डेटासेट्सचा वापर Azure मशीन लर्निंगमध्ये Phi-3 मॉडेल फाइन-ट्यून करण्यासाठी कराल.

या अभ्यासात, आपण:

- *download_dataset.py* फाइलबाबत कोड जोडा ज्याद्वारे डेटासेट डाउनलोड होतील.
- *download_dataset.py* फाइल चालवून डेटासेट स्थानिक वातावरणात डाउनलोड करा.

#### *download_dataset.py* वापरून तुमचे डेटासेट डाउनलोड करा

1. Visual Studio Code मध्ये *download_dataset.py* फाइल उघडा.

1. *download_dataset.py* फाइलमध्ये खालील कोड जोडा.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # निर्दिष्ट नाव, संरचना, आणि विभागणी प्रमाणासह डेटासेट लोड करा
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # डेटासेटला ट्रेन आणि टेस्ट सेट्समध्ये विभागा (८०% ट्रेन, २०% टेस्ट)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # निर्देशिका अस्तित्वात नसेल तर तयार करा
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # फाईल लेखन मोडमध्ये उघडा
        with open(filepath, 'w', encoding='utf-8') as f:
            # डेटासेटमधील प्रत्येक रेकॉर्डवर पुनरावृत्ती करा
            for record in dataset:
                # रेकॉर्ड JSON ऑब्जेक्ट म्हणून डंप करा आणि फाईलमध्ये लिहा
                json.dump(record, f)
                # रेकॉर्ड वेगळे करण्यासाठी नवीन ओळ कॅरेक्टर लिहा
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # विशिष्ट संरचना आणि विभागणी प्रमाणासह ULTRACHAT_200k डेटासेट लोड आणि विभाजित करा
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # विभागणीमधून ट्रेन आणि टेस्ट डेटासेट काढा
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ट्रेन डेटासेट JSONL फाईलमध्ये जतन करा
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # टेस्ट डेटासेट वेगळी JSONL फाईलमध्ये जतन करा
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. स्क्रिप्ट चालवून डेटासेट स्थानिक वातावरणात डाउनलोड करण्यासाठी टर्मिनलमध्ये खालील कमांड टाइप करा.

    ```console
    python download_dataset.py
    ```

1. डेटासेट यशस्वीपणे आपल्या स्थानिक *finetune-phi/data* निर्देशिकेत जतन झाले आहेत का ते तपासा.

> [!NOTE]
>
> #### डेटासेट आकार आणि फाइन-ट्यूनिंग वेळाविषयी नोंद
>
> या ट्युटोरियलमध्ये, आपण फक्त 1% डेटासेट वापरत आहात (`split='train[:1%]'`). यामुळे डेटा प्रमाण मोठ्या प्रमाणात कमी होतो आणि अपलोड तसेच फाइन-ट्यूनिंग प्रक्रिया वेगाने पूर्ण होतात. आपण प्रशिक्षण वेळ आणि मॉडेलच्या कामगिरी दरम्यान संतुलनासाठी टक्केवारी समायोजित करू शकता. डेटासेटच्या लहान भागाचा वापर केल्याने फाइन-ट्यूनिंगसाठी लागणारा वेळ कमी होतो, ज्यामुळे ट्युटोरियल अधिक सोपा होतो.

## परिदृश्य 2: Phi-3 मॉडेल फाइन-ट्यून करा आणि Azure मशीन लर्निंग स्टुडिओमध्ये डिप्लॉय करा

### Phi-3 मॉडेल फाइन-ट्यून करा

या अभ्यासात, आपण Azure मशीन लर्निंग स्टुडिओमध्ये Phi-3 मॉडेल फाइन-ट्यून कराल.

या अभ्यासात, आपण:

- फाइन-ट्यूनिंगसाठी कम्प्युटर क्लस्टर तयार करा.
- Azure मशीन लर्निंग स्टुडिओमध्ये Phi-3 मॉडेल फाइन-ट्यून करा.

#### फाइन-ट्यूनिंगसाठी कम्प्युटर क्लस्टर तयार करा

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) येथे जा.

1. डाव्या बाजूच्या टॅबमधून **Compute** निवडा.

1. नेव्हिगेशन मेनूमधून **Compute clusters** निवडा.

1. **+ New** निवडा.

    ![Compute निवडा.](../../../../../../translated_images/mr/06-01-select-compute.a29cff290b480252.webp)

1. खालील कार्य करा:

    - वापरायचा **Region** निवडा.
    - **Virtual machine tier** ला **Dedicated** निवडा.
    - **Virtual machine type** ला **GPU** निवडा.
    - **Virtual machine size** फिल्टरमध्ये **Select from all options** निवडा.
    - **Virtual machine size** म्हणून **Standard_NC24ads_A100_v4** निवडा.

    ![क्लस्टर तयार करा.](../../../../../../translated_images/mr/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** निवडा.

1. खालील कार्य करा:

    - **Compute name** प्रविष्ट करा. ही एक अनोखी किंमत असावी.
    - **Minimum number of nodes** ला **0** निवडा.
    - **Maximum number of nodes** ला **1** निवडा.
    - **Idle seconds before scale down** ला **120** निवडा.

    ![क्लस्टर तयार करा.](../../../../../../translated_images/mr/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** निवडा.

#### Phi-3 मॉडेल फाइन-ट्यून करा

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) येथे जा.

1. आपण तयार केलेला Azure मशीन लर्निंग कार्यक्षेत्र निवडा.

    ![तुम्ही तयार केलेला कार्यक्षेत्र निवडा.](../../../../../../translated_images/mr/06-04-select-workspace.a92934ac04f4f181.webp)

1. खालील कार्य करा:

    - डाव्या बाजूच्या टॅबमधून **Model catalog** निवडा.
    - **search bar** मध्ये *phi-3-mini-4k* टाइप करा आणि दिसणाऱ्या पर्यायांमधून **Phi-3-mini-4k-instruct** निवडा.

    ![phi-3-mini-4k टाइप करा.](../../../../../../translated_images/mr/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. नेव्हिगेशन मेनूमधून **Fine-tune** निवडा.

    ![फाइन-ट्यून निवडा.](../../../../../../translated_images/mr/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. खालील कार्य करा:

    - **Select task type** मध्ये **Chat completion** निवडा.
    - **+ Select data** वर क्लिक करून **Training data** अपलोड करा.
    - तपासणी डेटाची प्रकार निवडा **Provide different validation data**.
    - **+ Select data** वर क्लिक करून **Validation data** अपलोड करा.

    ![फाइन-ट्यूनिंग पृष्ठ भरा.](../../../../../../translated_images/mr/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> तुम्ही **Advanced settings** निवडून **learning_rate** आणि **lr_scheduler_type** सारख्या सेटिंग्ज सानुकूलित करू शकता ज्यामुळे तुमच्या गरजेनुसार फाइन-ट्यूनिंग प्रक्रिया ऑप्टिमाइझ होईल.

1. **Finish** निवडा.

1. या अभ्यासात, तुम्ही Azure मशीन लर्निंग वापरून Phi-3 मॉडेल यशस्वीपणे फाइन-ट्यून केले आहे. कृपया लक्षात ठेवा की फाइन-ट्यूनिंगसाठी वेळ लागू शकतो. फाइन-ट्यूनिंग जॉब चालवल्यानंतर पूर्ण होईपर्यंत प्रतीक्षा करावी लागेल. तुम्ही Azure मशीन लर्निंग कार्यक्षेत्राच्या डाव्या बाजूच्या Jobs टॅबवर जाऊन फाइन-ट्यूनिंग जॉबची स्थिती पाहू शकता. पुढील सत्रात, तुम्ही फाइन-ट्यून केलेल्या मॉडेलचा डिप्लॉयमेंट कराल आणि ते Prompt flow सोबत एकत्रित कराल.

    ![फाइनट्यूनिंग जॉब पहा.](../../../../../../translated_images/mr/06-08-output.2bd32e59930672b1.webp)

### फाइन-ट्यून केलेला Phi-3 मॉडेल डिप्लॉय करा

Prompt flow सोबत फाइन-ट्यून केलेला Phi-3 मॉडेल एकत्रित करण्यासाठी, तुम्हाला मॉडेल डिप्लॉय करावे लागेल ज्यामुळे रिअल-टाइम इनफरन्ससाठी तो उपलब्ध होईल. यामध्ये मॉडेल नोंदणी, ऑनलाइन एंडपॉइंट तयार करणे आणि मॉडेल डिप्लॉय करणे यांचा समावेश आहे.

या अभ्यासात, तुम्ही:

- Azure मशीन लर्निंग कार्यक्षेत्रात फाइन-ट्यून मॉडेल नोंदणी कराल.
- ऑनलाइन एंडपॉइंट तयार कराल.
- नोंदणीकृत फाइन-ट्यून Phi-3 मॉडेल डिप्लॉय कराल.

#### फाइन-ट्यून केलेला मॉडेल नोंदणी करा

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) येथे जा.

1. आपण तयार केलेला Azure मशीन लर्निंग कार्यक्षेत्र निवडा.

    ![तुम्ही तयार केलेला कार्यक्षेत्र निवडा.](../../../../../../translated_images/mr/06-04-select-workspace.a92934ac04f4f181.webp)

1. डाव्या बाजूच्या टॅबमध्ये **Models** निवडा.
1. **+ Register** निवडा.
1. **From a job output** निवडा.

    ![मॉडेल नोंदणी करा.](../../../../../../translated_images/mr/07-01-register-model.ad1e7cc05e4b2777.webp)

1. तुम्ही तयार केलेला जॉब निवडा.

    ![जॉब निवडा.](../../../../../../translated_images/mr/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** निवडा.

1. **Model type** मध्ये **MLflow** निवडा.

1. सुनिश्चित करा की **Job output** निवडलेले आहे; ते आपोआप निवडले जाईल.

    ![आउटपुट निवडा.](../../../../../../translated_images/mr/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** निवडा.

3. **Register** निवडा.

    ![नोंदणी करा.](../../../../../../translated_images/mr/07-04-register.fd82a3b293060bc7.webp)

4. तुमचे नोंदणीकृत मॉडेल डाव्या बाजूच्या टॅबमधील **Models** मेनूमधून पाहू शकता.

    ![नोंदणीकृत मॉडेल.](../../../../../../translated_images/mr/07-05-registered-model.7db9775f58dfd591.webp)

#### फाइन-ट्यून मॉडेल डिप्लॉय करा

1. तयार केलेल्या Azure मशीन लर्निंग कार्यक्षेत्रात जा.

1. डाव्या बाजूच्या टॅबमधून **Endpoints** निवडा.

1. नेव्हिगेशन मेनूमधून **Real-time endpoints** निवडा.

    ![एंडपॉइंट तयार करा.](../../../../../../translated_images/mr/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** निवडा.

1. तुमचा नोंदणीकृत मॉडेल निवडा.

    ![नोंदणीकृत मॉडेल निवडा.](../../../../../../translated_images/mr/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** निवडा.

1. खालील कार्य करा:

    - **Virtual machine** ला *Standard_NC6s_v3* निवडा.
    - वापरायची **Instance count** निवडा. उदाहरणार्थ, *1*.
    - **Endpoint** ला **New** निवडा नवीन एंडपॉइंट तयार करण्यासाठी.
    - **Endpoint name** प्रविष्ट करा. ही एक अनोखी किंमत असावी.
    - **Deployment name** प्रविष्ट करा. ही एक अनोखी किंमत असावी.

    ![डिप्लॉयमेंट सेटिंग भरा.](../../../../../../translated_images/mr/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** निवडा.

> [!WARNING]
> तुमच्या खात्यावर अतिरिक्त शुल्क येऊ नये यासाठी, तयार केलेला एंडपॉइंट Azure मशीन लर्निंग कार्यक्षेत्रातून हटवा.
>

#### Azure मशीन लर्निंग कार्यक्षेत्रातील डिप्लॉयमेंट स्थिती तपासा

1. तयार केलेल्या Azure मशीन लर्निंग कार्यक्षेत्रात जा.

1. डाव्या बाजूच्या टॅबमधून **Endpoints** निवडा.

1. तयार केलेला एंडपॉइंट निवडा.

    ![एंडपॉइंट्स निवडा](../../../../../../translated_images/mr/07-09-check-deployment.325d18cae8475ef4.webp)

1. या पृष्ठावर तुम्ही डिप्लॉयमेंटदरम्यान एंडपॉइंट्स व्यवस्थापित करू शकता.

> [!NOTE]
> डिप्लॉयमेंट पूर्ण झाल्यानंतर, खात्री करा की **Live traffic** **100%** वर सेट केले आहे. जर तसे नसेल, तर ट्रॅफिक सेटिंग्ज समायोजित करण्यासाठी **Update traffic** निवडा. लक्षात ठेवा की ट्रॅफिक 0% असल्यास तुम्ही मॉडेल चाचणी करू शकत नाही.
>
> ![ट्रॅफिक सेट करा.](../../../../../../translated_images/mr/07-10-set-traffic.085b847e5751ff3d.webp)
>

## परिदृश्य 3: Prompt flow सोबत एकत्रित करा आणि Microsoft Foundry मध्ये तुमच्या कस्टम मॉडेलसोबत चॅट करा

### कस्टम Phi-3 मॉडेल Prompt flow सोबत एकत्रित करा

तुमचा फाइन-ट्यून केलेला मॉडेल यशस्वीपणे डिप्लॉय केल्यानंतर, तुम्ही आता तो Prompt Flow सोबत एकत्रित करू शकता ज्यामुळे तुम्ही तुमच्या कस्टम Phi-3 मॉडेलसह रिअल-टाइम अॅप्लिकेशन्समध्ये विविध संवादात्मक कार्ये करू शकता.

या अभ्यासात, तुम्ही:

- Microsoft Foundry Hub तयार कराल.
- Microsoft Foundry प्रकल्प तयार कराल.
- Prompt flow तयार कराल.
- फाइन-ट्यून Phi-3 मॉडेलसाठी कस्टम कनेक्शन जोडलं जाईल.
- तुमच्या कस्टम Phi-3 मॉडेलसोबत चॅट करण्यासाठी Prompt flow सेटअप कराल.

> [!NOTE]
> तुम्ही Azure ML Studio वापरूनही Promptflow सह एकत्रिकरण करू शकता. Azure ML Studio मध्ये देखील समान एकत्रीकरण प्रक्रिया लागू होऊ शकते.

#### Microsoft Foundry Hub तयार करा

तुम्हाला प्रकल्प तयार करण्यापूर्वी Hub तयार करावा लागेल. Hub हे एक रिसोर्स ग्रुपसारखे काम करते ज्यामुळे तुम्ही Microsoft Foundry मधील अनेक प्रकल्पांचे आयोजन आणि व्यवस्थापन करू शकता.
1. भेट द्या [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. डाव्या बाजूच्या टॅबवरून **All hubs** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New hub** निवडा.

    ![Create hub.](../../../../../../translated_images/mr/08-01-create-hub.8f7dd615bb8d9834.webp)

1. खालील कामे करा:

    - **Hub name** भरा. हे एक अद्वितीय मूल्य असणे आवश्यक आहे.
    - तुमचा Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा (गरज असल्यास नवीन तयार करा).
    - तुम्हाला वापरायची **Location** निवडा.
    - वापरण्यासाठी **Connect Azure AI Services** निवडा (गरज असल्यास नवीन तयार करा).
    - **Connect Azure AI Search** साठी **Skip connecting** निवडा.

    ![Fill hub.](../../../../../../translated_images/mr/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** निवडा.

#### Microsoft Foundry प्रोजेक्ट तयार करा

1. तुम्ही तयार केलेल्या हबमध्ये, डाव्या बाजूच्या टॅबवरून **All projects** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New project** निवडा.

    ![Select new project.](../../../../../../translated_images/mr/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** भरा. हे एक अद्वितीय मूल्य असणे आवश्यक आहे.

    ![Create project.](../../../../../../translated_images/mr/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** निवडा.

#### फाइन-ट्यून केलेल्या Phi-3 मॉडेलसाठी कस्टम कनेक्शन जोडा

तुमच्या कस्टम Phi-3 मॉडेलला Prompt flow सोबत इंटीग्रेट करण्यासाठी, तुम्हाला मॉडेलच्या endpoint आणि key कस्टम कनेक्शनमध्ये जतन करणे आवश्यक आहे. या सेटअपमुळे तुम्हाला Prompt flow मध्ये तुमच्या कस्टम Phi-3 मॉडेलचा प्रवेश मिळतो.

#### फाइन-ट्यून केलेल्या Phi-3 मॉडेलचा api key आणि endpoint uri सेट करा

1. भेट द्या [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. तुम्ही तयार केलेल्या Azure मशीन लर्निंग वर्कस्पेसकडे जा.

1. डाव्या बाजूच्या टॅबवरून **Endpoints** निवडा.

    ![Select endpoints.](../../../../../../translated_images/mr/08-06-select-endpoints.aff38d453bcf9605.webp)

1. तुम्ही तयार केलेला endpoint निवडा.

    ![Select endpoints.](../../../../../../translated_images/mr/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. नेव्हिगेशन मेनूमधून **Consume** निवडा.

1. तुमचा **REST endpoint** आणि **Primary key** कॉपी करा.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/mr/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### कस्टम कनेक्शन जोडा

1. भेट द्या [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. तुम्ही तयार केलेल्या Microsoft Foundry प्रोजेक्टमध्ये जा.

1. तुम्ही तयार केलेल्या प्रोजेक्टमध्ये, डाव्या बाजूच्या टॅबवरून **Settings** निवडा.

1. **+ New connection** निवडा.

    ![Select new connection.](../../../../../../translated_images/mr/08-09-select-new-connection.02eb45deadc401fc.webp)

1. नेव्हिगेशन मेनूमधून **Custom keys** निवडा.

    ![Select custom keys.](../../../../../../translated_images/mr/08-10-select-custom-keys.856f6b2966460551.webp)

1. खालील कामे करा:

    - **+ Add key value pairs** निवडा.
    - key नावासाठी **endpoint** टाका आणि Azure ML Studio मधून कॉपी केलेला endpoint value फील्डमध्ये पेस्ट करा.
    - पुन्हा **+ Add key value pairs** निवडा.
    - key नावासाठी **key** टाका आणि Azure ML Studio मधून कॉपी केलेली key value फील्डमध्ये पेस्ट करा.
    - keys जोडल्यावर, key उघड होऊ नये म्हणून **is secret** निवडा.

    ![Add connection.](../../../../../../translated_images/mr/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** निवडा.

#### Prompt flow तयार करा

Microsoft Foundry मध्ये तुम्ही एक कस्टम कनेक्शन जोडले आहे. आता, पुढील स्टेप्स वापरून Prompt flow तयार करा. त्यानंतर, तुम्ही या Prompt flow ला कस्टम कनेक्शनशी कनेक्ट कराल जेणेकरून तुम्ही Prompt flow मध्ये फाइन-ट्यून केलेला मॉडेल वापरू शकता.

1. तुम्ही तयार केलेल्या Microsoft Foundry प्रोजेक्टमध्ये जा.

1. डाव्या बाजूच्या टॅबवरून **Prompt flow** निवडा.

1. नेव्हिगेशन मेनूमधून **+ Create** निवडा.

    ![Select Promptflow.](../../../../../../translated_images/mr/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. नेव्हिगेशन मेनूमधून **Chat flow** निवडा.

    ![Select chat flow.](../../../../../../translated_images/mr/08-13-select-flow-type.2ec689b22da32591.webp)

1. वापरण्यासाठी **Folder name** भरा.

    ![Enter name.](../../../../../../translated_images/mr/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** निवडा.

#### तुमच्या कस्टम Phi-3 मॉडेलसह Prompt flow सेट करा

तुम्हाला फाइन-ट्यून केलेला Phi-3 मॉडेल Prompt flow मध्ये इंटीग्रेट करायचा आहे. मात्र, सध्याचा Prompt flow यासाठी डिझाइन केलेला नाही. त्यामुळे, तुम्हाला Prompt flow पुनर्निर्मित करावे लागेल जेणेकरून कस्टम मॉडेल इंटीग्रेट होईल.

1. Prompt flow मध्ये विद्यमान फ्लोला पुन्हा बांधण्यासाठी खालील कामे करा:

    - **Raw file mode** निवडा.
    - *flow.dag.yml* फाईलमधील सर्व विद्यमान कोड हटवा.
    - खालील कोड *flow.dag.yml* फाईलमध्ये जोडा.

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

    - **Save** निवडा.

    ![Select raw file mode.](../../../../../../translated_images/mr/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Prompt flow मध्ये कस्टम Phi-3 मॉडेल वापरण्यासाठी *integrate_with_promptflow.py* फाईलमध्ये खालील कोड जोडा.

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

        # "connection" हा कस्टम कनेक्शनचा नाव आहे, "endpoint", "key" हे कस्टम कनेक्शनमधील कीज आहेत
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
            
            # पूर्ण JSON प्रतिसाद लॉग करा
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

    ![Paste prompt flow code.](../../../../../../translated_images/mr/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry मध्ये Prompt flow वापरण्याबाबत अधिक सविस्तर माहिती साठी, तुम्ही [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) पहाऊ शकता.

1. तुमच्या मॉडेलसोबत चॅट करण्यासाठी **Chat input**, **Chat output** निवडा.

    ![Input Output.](../../../../../../translated_images/mr/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. आता तुम्ही तुमच्या कस्टम Phi-3 मॉडेलसोबत चॅट करण्यासाठी तयार आहात. पुढील व्यायामात, तुम्ही Prompt flow सुरू करणे आणि फाइन-ट्यून केलेल्या Phi-3 मॉडेलसोबत चॅट कसे करायचे ते शिकाल.

> [!NOTE]
>
> पुनर्निर्मित फ्लो खालील प्रतिमेसारखा दिसावा:
>
> ![Flow example.](../../../../../../translated_images/mr/08-18-graph-example.d6457533952e690c.webp)
>

### तुमच्या कस्टम Phi-3 मॉडेलसोबत चॅट करा

आता जेव्हा तुम्ही तुमचे कस्टम Phi-3 मॉडेल फाइन-ट्यून करून Prompt flow मध्ये इंटीग्रेट केले आहे, तेव्हा तुम्ही त्याच्याशी संवाद साधण्यासाठी तयार आहात. हा व्यायाम तुम्हाला मॉडेलशी संवाद सुरू करण्यासाठी आणि Prompt flow वापरण्याच्या प्रक्रियेचे मार्गदर्शन करेल. या स्टेप्सचे पालन करून, तुम्ही तुमच्या फाइन-ट्यून केलेल्या Phi-3 मॉडेलच्या विविध कामांसाठी आणि संवादांसाठी पूर्ण क्षमतांचा वापर करू शकाल.

- Prompt flow वापरून तुमच्या कस्टम Phi-3 मॉडेलसोबत चॅट करा.

#### Prompt flow सुरू करा

1. Prompt flow सुरू करण्यासाठी **Start compute sessions** निवडा.

    ![Start compute session.](../../../../../../translated_images/mr/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. पॅरामीटर्स रिन्यू करण्यासाठी **Validate and parse input** निवडा.

    ![Validate input.](../../../../../../translated_images/mr/09-02-validate-input.317c76ef766361e9.webp)

1. तुम्ही तयार केलेल्या कस्टम कनेक्शनच्या **connection** चे **Value** निवडा. उदाहरणार्थ, *connection*.

    ![Connection.](../../../../../../translated_images/mr/09-03-select-connection.99bdddb4b1844023.webp)

#### तुमच्या कस्टम मॉडेलसोबत चॅट करा

1. **Chat** निवडा.

    ![Select chat.](../../../../../../translated_images/mr/09-04-select-chat.61936dce6612a1e6.webp)

1. खालीलप्रमाणे परिणामांचे उदाहरण आहे: आता तुम्ही तुमच्या कस्टम Phi-3 मॉडेलसह चॅट करू शकता. फाइन-ट्यूनिंगसाठी वापरलेल्या डेटावर आधारित प्रश्न विचारणे शिफारसीय आहे.

    ![Chat with prompt flow.](../../../../../../translated_images/mr/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असल्याने, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा असत्यता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवाद सुचविला जातो. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->