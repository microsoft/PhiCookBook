# Microsoft Foundry তে Prompt flow সহ কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করা

এই end-to-end (E2E) নমুনাটি Microsoft Tech Community থেকে "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" গাইডের উপর ভিত্তি করে তৈরি। এটি Microsoft Foundry তে Prompt flow সহ কাস্টম Phi-3 মডেল ফাইন-টিউন, ডিপ্লয় এবং ইন্টিগ্রেট করার প্রক্রিয়াগুলি পরিচয় করিয়ে দেয়। 
E2E নমুনার থেকে আলাদা, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", যা লোকাল কোড চালানোর উপর ভিত্তি করে ছিল, এই টিউটোরিয়ালটি সম্পূর্ণরূপে Azure AI / ML Studio তে আপনার মডেল ফাইন-টিউন এবং ইন্টিগ্রেশনের ওপর মনোযোগ দেয়।

## ওভারভিউ

এই E2E নমুনায়, আপনি শিখবেন কিভাবে Phi-3 মডেল ফাইন-টিউন করতে হয় এবং Microsoft Foundry তে Prompt flow এর সঙ্গে এটি ইন্টিগ্রেট করতে হয়। Azure AI / ML Studio ব্যবহার করে, আপনি কাস্টম AI মডেল ডিপ্লয় এবং ব্যবহারের জন্য একটি কর্মপ্রবাহ প্রতিষ্ঠা করবেন। এই E2E নমুনাটি তিনটি পরিপ্রেক্ষিতে ভাগ করা হয়েছে:

**পরিপ্রেক্ষিত ১: Azure রিসোর্স সেট আপ এবং ফাইন-টিউনিংয়ের প্রস্তুতি**

**পরিপ্রেক্ষিত ২: Phi-3 মডেল ফাইন-টিউন করা এবং Azure Machine Learning Studio তে ডিপ্লয় করা**

**পরিপ্রেক্ষিত ৩: Prompt flow এর সঙ্গে ইন্টিগ্রেট করা এবং Microsoft Foundry তে আপনার কাস্টম মডেলের সাথে চ্যাট করা**

এখানে এই E2E নমুনার একটি ওভারভিউ দেওয়া হল।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/bn/00-01-architecture.198ba0f1ae6d841a.webp)

### বিষয়সূচী

1. **[পরিপ্রেক্ষিত ১: Azure রিসোর্স সেট আপ এবং ফাইন-টিউনিংয়ের প্রস্তুতি](#পরিপ্রেক্ষিত-১-azure-রিসোর্স-সেট-আপ-এবং-ফাইন-টিউনিংয়ের-প্রস্তুতি)**
    - [Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন](#azure-machine-learning-ওয়ার্কস্পেস-তৈরি-করুন)
    - [Azure সাবস্ক্রিপশনে GPU কোটা অনুরোধ করুন](#azure-সাবস্ক্রিপশনে-gpu-কোটা-অনুরোধ-করুন)
    - [রোল অ্যাসাইনমেন্ট যোগ করুন](#রোল-অ্যাসাইনমেন্ট-যোগ-করুন)
    - [প্রকল্প সেট আপ করুন](#প্রকল্প-সেট-আপ-করুন)
    - [ফাইন-টিউনিংয়ের জন্য ডেটাসেট প্রস্তুত করুন](#ফাইন-টিউনিংয়ের-জন্য-ডেটাসেট-প্রস্তুত-করুন)

1. **[পরিপ্রেক্ষিত ২: Phi-3 মডেল ফাইন-টিউন করুন এবং Azure Machine Learning Studio তে ডিপ্লয় করুন](#পরিস্থিতি-২-phi-3-মডেল-ফাইন-টিউন-করুন-এবং-azure-machine-learning-studio-তে-ডিপ্লয়-করুন)**
    - [Phi-3 মডেল ফাইন-টিউন করুন](#phi-3-মডেল-ফাইন-টিউন-করা)
    - [ফাইন-টিউন করা Phi-3 মডেল ডিপ্লয় করুন](#ফাইন-টিউনকৃত-phi-3-মডেল-ডিপ্লয়-করুন)

1. **[পরিপ্রেক্ষিত ৩: Prompt flow এর সঙ্গে ইন্টিগ্রেট করুন এবং Microsoft Foundry তে আপনার কাস্টম মডেলের সাথে চ্যাট করুন](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [কাস্টম Phi-3 মডেল Prompt flow এর সঙ্গে ইন্টিগ্রেট করুন](#কাস্টম-phi-3-মডেল-prompt-flow-এর-সাথে-ইন্টিগ্রেট-করা)
    - [আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করুন](#আপনার-কাস্টম-phi-3-মডেলের-সাথে-চ্যাট-করুন)

## পরিপ্রেক্ষিত ১: Azure রিসোর্স সেট আপ এবং ফাইন-টিউনিংয়ের প্রস্তুতি

### Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন

1. পোর্টাল পেজের উপরের **সার্চ বার** এ *azure machine learning* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Azure Machine Learning** নির্বাচন করুন।

    ![Type azure machine learning.](../../../../../../translated_images/bn/01-01-type-azml.acae6c5455e67b4b.webp)

2. নেভিগেশন মেনু থেকে **+ Create** নির্বাচন করুন।

3. নেভিগেশন মেনু থেকে **New workspace** নির্বাচন করুন।

    ![Select new workspace.](../../../../../../translated_images/bn/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. নিম্নলিখিত কাজগুলো সম্পাদন করুন:

    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহারের জন্য **Resource group** নির্বাচন করুন (প্রয়োজন হলে নতুন তৈরি করুন)।
    - **Workspace Name** প্রবেশ করান। এটি অবশ্যই ইউনিক হতে হবে।
    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।
    - ব্যবহারের জন্য **Storage account** নির্বাচন করুন (প্রয়োজন হলে নতুন তৈরি করুন)।
    - ব্যবহারের জন্য **Key vault** নির্বাচন করুন (প্রয়োজন হলে নতুন তৈরি করুন)।
    - ব্যবহারের জন্য **Application insights** নির্বাচন করুন (প্রয়োজন হলে নতুন তৈরি করুন)।
    - ব্যবহারের জন্য **Container registry** নির্বাচন করুন (প্রয়োজন হলে নতুন তৈরি করুন)।

    ![Fill azure machine learning.](../../../../../../translated_images/bn/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** নির্বাচন করুন।

6. **Create** নির্বাচন করুন।

### Azure সাবস্ক্রিপশনে GPU কোটা অনুরোধ করুন

এই টিউটোরিয়ালে, আপনি Phi-3 মডেল ফাইন-টিউন এবং ডিপ্লয়ের জন্য GPU ব্যবহার করতে শিখবেন। ফাইন-টিউনিংয়ের জন্য আপনি *Standard_NC24ads_A100_v4* GPU ব্যবহার করবেন, যা কোটা অনুরোধ প্রয়োজন। ডিপ্লয়ের জন্য আপনি *Standard_NC6s_v3* GPU ব্যবহার করবেন, যেটির জন্যও কোটা অনুরোধ প্রয়োজন।

> [!NOTE]
>
> শুধুমাত্র Pay-As-You-Go সাবস্ক্রিপশন (স্ট্যান্ডার্ড সাবস্ক্রিপশন টাইপ) GPU বরাদ্দের জন্য যোগ্য; বেনিফিট সাবস্ক্রিপশনগুলো বর্তমানে সমর্থিত নয়।
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. *Standard NCADSA100v4 Family* কোটা অনুরোধের জন্য নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশে ট্যাব থেকে **Quota** নির্বাচন করুন।
    - ব্যবহারের জন্য **Virtual machine family** নির্বাচন করুন। উদাহরণস্বরূপ, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* নির্বাচন করুন, যার মধ্যে *Standard_NC24ads_A100_v4* GPU অন্তর্ভুক্ত।
    - নেভিগেশন মেনু থেকে **Request quota** নির্বাচন করুন।

        ![Request quota.](../../../../../../translated_images/bn/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota পৃষ্ঠায়, আপনি ব্যবহার করতে চান এমন **New cores limit** প্রবেশ করান। উদাহরণস্বরূপ, ২৪।
    - Request quota পৃষ্ঠায়, GPU কোটা অনুরোধ করতে **Submit** নির্বাচন করুন।

1. *Standard NCSv3 Family* কোটা অনুরোধের জন্য নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশে ট্যাব থেকে **Quota** নির্বাচন করুন।
    - ব্যবহারের জন্য **Virtual machine family** নির্বাচন করুন। উদাহরণস্বরূপ, *Standard NCSv3 Family Cluster Dedicated vCPUs* নির্বাচন করুন, যার মধ্যে *Standard_NC6s_v3* GPU অন্তর্ভুক্ত।
    - নেভিগেশন মেনু থেকে **Request quota** নির্বাচন করুন।
    - Request quota পৃষ্ঠায়, আপনি ব্যবহার করতে চান এমন **New cores limit** প্রবেশ করান। উদাহরণস্বরূপ, ২৪।
    - Request quota পৃষ্ঠায়, GPU কোটা অনুরোধ করতে **Submit** নির্বাচন করুন।

### রোল অ্যাসাইনমেন্ট যোগ করুন

আপনার মডেলগুলি ফাইন-টিউন এবং ডিপ্লয়ের জন্য প্রথমে একটি User Assigned Managed Identity (UAI) তৈরি করতে হবে এবং যথাযথ পারমিশন অ্যাসাইন করতে হবে। ডিপ্লয়ের সময় এই UAI ব্যবহার করা হবে অথেন্টিকেশনের জন্য।

#### User Assigned Managed Identity (UAI) তৈরি করুন

1. পোর্টাল পেজের উপরের **সার্চ বার** এ *managed identities* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Managed Identities** নির্বাচন করুন।

    ![Type managed identities.](../../../../../../translated_images/bn/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** নির্বাচন করুন।

    ![Select create.](../../../../../../translated_images/bn/03-02-select-create.92bf8989a5cd98f2.webp)

1. নিম্নলিখিত কাজগুলো সম্পাদন করুন:

    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহারের জন্য **Resource group** নির্বাচন করুন (প্রয়োজন হলে নতুন তৈরি করুন)।
    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।
    - **Name** প্রবেশ করান। এটি অবশ্যই ইউনিক হতে হবে।

    ![Select create.](../../../../../../translated_images/bn/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** নির্বাচন করুন।

1. **+ Create** নির্বাচন করুন।

#### Managed Identity তে Contributor রোল অ্যাসাইনমেন্ট যোগ করুন

1. আপনি যে Managed Identity তৈরি করেছেন সেই রিসোর্সে যান।

1. বাম পাশে ট্যাব থেকে **Azure role assignments** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+Add role assignment** নির্বাচন করুন।

1. Add role assignment পৃষ্ঠায়, নিম্নলিখিত কাজগুলি করুন:
    - **Scope** হিসেবে **Resource group** নির্বাচন করুন।
    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহারের জন্য **Resource group** নির্বাচন করুন।
    - **Role** হিসেবে **Contributor** নির্বাচন করুন।

    ![Fill contributor role.](../../../../../../translated_images/bn/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** নির্বাচন করুন।

#### Managed Identity তে Storage Blob Data Reader রোল অ্যাসাইনমেন্ট যোগ করুন

1. পোর্টাল পেজের উপরের **সার্চ বার** এ *storage accounts* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage accounts** নির্বাচন করুন।

    ![Type storage accounts.](../../../../../../translated_images/bn/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. আপনার তৈরি করা Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত স্টোরেজ অ্যাকাউন্ট নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephistorage*।

1. Add role assignment পৃষ্ঠায় নেভিগেট করতে নিম্নলিখিত কাজগুলো করুন:

    - আপনি যে Azure Storage অ্যাকাউন্ট তৈরি করেছেন সেখানে যান।
    - বাম পাশে ট্যাব থেকে **Access Control (IAM)** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **+ Add** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **Add role assignment** নির্বাচন করুন।

    ![Add role.](../../../../../../translated_images/bn/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:

    - Role পৃষ্ঠায়, **search bar** এ *Storage Blob Data Reader* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage Blob Data Reader** নির্বাচন করুন।
    - Role পৃষ্ঠায়, **Next** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **Assign access to** হিসেবে **Managed identity** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **+ Select members** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনার Azure **Subscription** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, **Managed identity** হিসেবে **Manage Identity** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনি যে Managed Identity তৈরি করেছেন তা নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephi-managedidentity*।
    - Select managed identities পৃষ্ঠায়, **Select** নির্বাচন করুন।

    ![Select managed identity.](../../../../../../translated_images/bn/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** নির্বাচন করুন।

#### Managed Identity তে AcrPull রোল অ্যাসাইনমেন্ট যোগ করুন

1. পোর্টাল পেজের উপরের **সার্চ বার** এ *container registries* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Container registries** নির্বাচন করুন।

    ![Type container registries.](../../../../../../translated_images/bn/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত যে container registry রয়েছে তা নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephicontainerregistry*

1. Add role assignment পৃষ্ঠায় নেভিগেট করতে নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশে ট্যাব থেকে **Access Control (IAM)** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **+ Add** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **Add role assignment** নির্বাচন করুন।

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:

    - Role পৃষ্ঠায়, **search bar** এ *AcrPull* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **AcrPull** নির্বাচন করুন।
    - Role পৃষ্ঠায়, **Next** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **Assign access to** হিসেবে **Managed identity** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **+ Select members** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনার Azure **Subscription** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, **Managed identity** হিসেবে **Manage Identity** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনি যে Managed Identity তৈরি করেছেন তা নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephi-managedidentity*।
    - Select managed identities পৃষ্ঠায়, **Select** নির্বাচন করুন।
    - **Review + assign** নির্বাচন করুন।

### প্রকল্প সেট আপ করুন

ফাইন-টিউনিংয়ের জন্য প্রয়োজনীয় ডেটাসেট ডাউনলোড করতে, আপনি একটি লোকাল পরিবেশ সেট আপ করবেন।

এই অনুশীলনে, আপনি

- কাজ করার জন্য একটি ফোল্ডার তৈরি করবেন।
- একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করবেন।
- প্রয়োজনীয় প্যাকেজসমূহ ইনস্টল করবেন।
- ডেটাসেট ডাউনলোড করার জন্য *download_dataset.py* ফাইল তৈরি করবেন।

#### কাজ করার জন্য একটি ফোল্ডার তৈরি করুন

1. একটি টার্মিনাল উইন্ডো খুলুন এবং নিম্নলিখিত কমান্ডটি টাইপ করে ডিফল্ট পাথে *finetune-phi* নামে একটি ফোল্ডার তৈরি করুন।

    ```console
    mkdir finetune-phi
    ```

2. আপনার টার্মিনালে নিম্নলিখিত কমান্ডটি টাইপ করুন যাতে আপনি তৈরি করা *finetune-phi* ফোল্ডারে নেভিগেট করতে পারেন।

    ```console
    cd finetune-phi
    ```

#### ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

1. আপনার টার্মিনালে নিম্নলিখিত কমান্ডটি টাইপ করুন যাতে *.venv* নামে একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি হয়।
    ```console
    python -m venv .venv
    ```

2. ভার্চুয়াল পরিবেশ সক্রিয় করতে আপনার টার্মিনালে নিচের কমান্ডটি টাইপ করুন।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> যদি এটি কাজ করে, তবে আপনার কমান্ড প্রম্পটের আগে *(.venv)* দেখতে পাবেন।

#### প্রয়োজনীয় প্যাকেজসমূহ ইনস্টল করুন

1. প্রয়োজনীয় প্যাকেজসমূহ ইনস্টল করতে আপনার টার্মিনালে নিচের কমান্ডগুলো টাইপ করুন।

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` তৈরি করুন

> [!NOTE]
> সম্পূর্ণ ফোল্ডার স্ট্রাকচার:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** খুলুন।

1. মেনু বার থেকে **File** নির্বাচন করুন।

1. **Open Folder** নির্বাচন করুন।

1. *finetune-phi* ফোল্ডারটি নির্বাচন করুন যা আপনি তৈরি করেছিলেন, এটি অবস্থিত *C:\Users\yourUserName\finetune-phi* এ।

    ![আপনি যে ফোল্ডারটি তৈরি করেছেন তা নির্বাচন করুন।](../../../../../../translated_images/bn/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code-এর বাম পাশের প্যানেলে, রাইট-ক্লিক করে **New File** নির্বাচন করুন এবং *download_dataset.py* নামে একটি নতুন ফাইল তৈরি করুন।

    ![একটি নতুন ফাইল তৈরি করুন।](../../../../../../translated_images/bn/04-02-create-new-file.cf9a330a3a9cff92.webp)

### ফাইন-টিউনিংয়ের জন্য ডেটাসেট প্রস্তুত করুন

এই ব্যায়ামে, আপনি *download_dataset.py* ফাইল রান করে *ultrachat_200k* ডেটাসেটগুলো আপনার স্থানীয় পরিবেশে ডাউনলোড করবেন। এরপর আপনি এই ডেটাসেট ব্যবহার করে Azure Machine Learning-এ Phi-3 মডেল ফাইন-টিউন করবেন।

এই ব্যায়ামে, আপনি:

- *download_dataset.py* ফাইলে কোড যোগ করবেন যাতে ডেটাসেট ডাউনলোড করা যায়।
- *download_dataset.py* ফাইল রান করবেন এবং ডেটাসেট আপনার স্থানীয় পরিবেশে ডাউনলোড করবেন।

#### *download_dataset.py* ব্যবহার করে আপনার ডেটাসেট ডাউনলোড করুন

1. Visual Studio Code-এ *download_dataset.py* ফাইল খুলুন।

1. নিচের কোড *download_dataset.py* ফাইলে যোগ করুন।

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # নির্দিষ্ট নাম, কনফিগারেশন, এবং বিভাজন অনুপাতে ডেটাসেট লোড করুন
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # ডেটাসেটকে ট্রেন এবং টেস্ট সেটে ভাগ করুন (৮০% ট্রেন, ২০% টেস্ট)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # ডিরেক্টরি না থাকলে সেটি তৈরি করুন
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # ফাইলটি লেখার মোডে খুলুন
        with open(filepath, 'w', encoding='utf-8') as f:
            # ডেটাসেটের প্রতিটি রেকর্ডের উপর পুনরাবৃত্তি করুন
            for record in dataset:
                # রেকর্ডটি JSON অবজেক্ট হিসেবে ডাম্প করুন এবং ফাইলে লিখুন
                json.dump(record, f)
                # রেকর্ড আলাদা করার জন্য একটি নতুন লাইন ক্যারেক্টার লিখুন
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # একটি নির্দিষ্ট কনফিগারেশন এবং বিভাজন অনুপাতে ULTRACHAT_200k ডেটাসেট লোড এবং ভাগ করুন
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # বিভাজন থেকে ট্রেন এবং টেস্ট ডেটাসেট বের করুন
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ট্রেন ডেটাসেটকে একটি JSONL ফাইলে সংরক্ষণ করুন
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # টেস্ট ডেটাসেটকে একটি আলাদা JSONL ফাইলে সংরক্ষণ করুন
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. স্ক্রিপ্ট রান করে ডেটাসেট আপনার স্থানীয় পরিবেশে ডাউনলোড করতে টার্মিনালে নিচের কমান্ড টাইপ করুন।

    ```console
    python download_dataset.py
    ```

1. যাচাই করুন ডেটাসেটগুলো সফলভাবে আপনার স্থানীয় *finetune-phi/data* ডিরেক্টরিতে সেভ হয়েছে।

> [!NOTE]
>
> #### ডেটাসেটের আকার ও ফাইন-টিউনিংয়ের সময় সম্পর্কে নোট
>
> এই টিউটোরিয়ালে, আপনি শুধু ডেটাসেটের ১% (`split='train[:1%]'`) ব্যবহার করেছেন। এটি ডেটার পরিমাণ অনেক কমিয়ে দেয়, যা আপলোড ও ফাইন-টিউনিং সময়কে দ্রুত করে। আপনি প্রশিক্ষণের সময় ও মডেল পারফরম্যান্সের সঠিক সমন্বয় খুঁজে পেতে শতাংশটি সামঞ্জস্য করতে পারেন। ডেটাসেটের ছোট একটি অংশ ব্যবহার করলে ফাইন-টিউনিংয়ের জন্য দরকারি সময় কমে, ফলে টিউটোরিয়ালের জন্য প্রক্রিয়াটি সহজ হয়।

## পরিস্থিতি ২: Phi-3 মডেল ফাইন-টিউন করুন এবং Azure Machine Learning Studio-তে ডিপ্লয় করুন

### Phi-3 মডেল ফাইন-টিউন করা

এই ব্যায়ামে, আপনি Azure Machine Learning Studio-তে Phi-3 মডেল ফাইন-টিউন করবেন।

এই ব্যায়ামে, আপনি:

- ফাইন-টিউনিংয়ের জন্য কম্পিউটার ক্লাস্টার তৈরি করবেন।
- Azure Machine Learning Studio-তে Phi-3 মডেল ফাইন-টিউন করবেন।

#### ফাইন-টিউনিংয়ের জন্য কম্পিউটার ক্লাস্টার তৈরি করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ভিজিট করুন।

1. বাম পাশের ট্যাব থেকে **Compute** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **Compute clusters** নির্বাচন করুন।

1. **+ New** নির্বাচন করুন।

    ![কম্পিউট নির্বাচন করুন।](../../../../../../translated_images/bn/06-01-select-compute.a29cff290b480252.webp)

1. নিচের কাজগুলি সম্পাদন করুন:

    - আপনি যেই **Region** ব্যবহার করতে চান সেটি নির্বাচন করুন।
    - **Virtual machine tier** হিসেবে **Dedicated** নির্বাচন করুন।
    - **Virtual machine type** হিসেবে **GPU** নির্বাচন করুন।
    - **Virtual machine size** ফিল্টারকে **Select from all options** সেট করুন।
    - **Virtual machine size** হিসাবে **Standard_NC24ads_A100_v4** নির্বাচন করুন।

    ![ক্লাস্টার তৈরি করুন।](../../../../../../translated_images/bn/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** নির্বাচন করুন।

1. নিচের কাজগুলি সম্পাদন করুন:

    - **Compute name** লিখুন। এটি অবশ্যই অনন্য হতে হবে।
    - **Minimum number of nodes** হিসেবে **0** নির্বাচন করুন।
    - **Maximum number of nodes** হিসেবে **1** নির্বাচন করুন।
    - **Idle seconds before scale down** হিসেবে **120** নির্বাচন করুন।

    ![ক্লাস্টার তৈরি করুন।](../../../../../../translated_images/bn/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** নির্বাচন করুন।

#### Phi-3 মডেল ফাইন-টিউন করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ভিজিট করুন।

1. যে Azure Machine Learning ওয়ার্কস্পেস আপনি তৈরি করেছেন সেটি নির্বাচন করুন।

    ![আপনি যে ওয়ার্কস্পেস তৈরি করেছেন তা নির্বাচন করুন।](../../../../../../translated_images/bn/06-04-select-workspace.a92934ac04f4f181.webp)

1. নিচের কাজগুলি সম্পাদন করুন:

    - বাম পাশের ট্যাব থেকে **Model catalog** নির্বাচন করুন।
    - **search bar**-এ *phi-3-mini-4k* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Phi-3-mini-4k-instruct** নির্বাচন করুন।

    ![phi-3-mini-4k টাইপ করুন।](../../../../../../translated_images/bn/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. নেভিগেশন মেনু থেকে **Fine-tune** নির্বাচন করুন।

    ![Fine-tune নির্বাচন করুন।](../../../../../../translated_images/bn/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. নিচের কাজগুলি সম্পাদন করুন:

    - **Select task type** হিসেবে **Chat completion** নির্বাচন করুন।
    - **+ Select data** নির্বাচন করে **Training data** আপলোড করুন।
    - ভ্যালিডেশন ডেটা আপলোড টাইপ হিসেবে **Provide different validation data** নির্বাচন করুন।
    - **+ Select data** নির্বাচন করে **Validation data** আপলোড করুন।

    ![Fine-tuning পাতা পূরণ করুন।](../../../../../../translated_images/bn/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> আপনি **Advanced settings** নির্বাচন করে কাস্টমাইজেশন করতে পারেন যেমন **learning_rate** এবং **lr_scheduler_type** যাতে ফাইন-টিউনিং প্রক্রিয়া আপনার নির্দিষ্ট চাহিদা অনুযায়ী অপটিমাইজ করা যায়।

1. **Finish** নির্বাচন করুন।

1. এই ব্যায়ামে, আপনি সফলভাবে Azure Machine Learning ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করেছেন। মনে রাখবেন ফাইন-টিউনিং প্রক্রিয়া নির্দিষ্ট সময় নিতে পারে। ফাইন-টিউনিং কাজ রান করার পর আপনাকে অপেক্ষা করতে হবে শেষ হওয়ার জন্য। আপনি Azure Machine Learning ওয়ার্কস্পেসের বাম পাশে Jobs ট্যাবে গিয়ে কাজের স্ট্যাটাস মনিটর করতে পারেন। পরবর্তী ধাপগুলোতে আপনি ফাইন-টিউন করা মডেল ডিপ্লয় করবেন এবং এটিকে Prompt flow-র সাথে ইন্টিগ্রেট করবেন।

    ![ফাইনটিউনিং কাজ দেখুন।](../../../../../../translated_images/bn/06-08-output.2bd32e59930672b1.webp)

### ফাইন-টিউনকৃত Phi-3 মডেল ডিপ্লয় করুন

Prompt flow-এর সাথে ফাইন-টিউনকৃত Phi-3 মডেল ইন্টিগ্রেশন করার জন্য আপনাকে মডেলটি ডিপ্লয় করতে হবে যাতে এটি রিয়েল-টাইম ইনফারেন্সের জন্য ব্যবহৃত হতে পারে। এই প্রক্রিয়ায় মডেল রেজিস্ট্রেশন, অনলাইন এন্ডপয়েন্ট তৈরি এবং মডেল ডিপ্লয়মেন্ট অন্তর্ভুক্ত।

এই ব্যায়ামে, আপনি:

- Azure Machine Learning ওয়ার্কস্পেসে ফাইন-টিউনকৃত মডেল রেজিস্টার করবেন।
- একটি অনলাইন এন্ডপয়েন্ট তৈরি করবেন।
- রেজিস্টারকৃত ফাইন-টিউনকৃত Phi-3 মডেল ডিপ্লয় করবেন।

#### ফাইন-টিউনকৃত মডেল রেজিস্টার করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ভিজিট করুন।

1. আপনি তৈরি করা Azure Machine Learning ওয়ার্কস্পেস নির্বাচন করুন।

    ![আপনি যে ওয়ার্কস্পেস তৈরি করেছেন তা নির্বাচন করুন।](../../../../../../translated_images/bn/06-04-select-workspace.a92934ac04f4f181.webp)

1. বাম পাশের ট্যাব থেকে **Models** নির্বাচন করুন।
1. **+ Register** নির্বাচন করুন।
1. **From a job output** নির্বাচন করুন।

    ![মডেল রেজিস্টার করুন।](../../../../../../translated_images/bn/07-01-register-model.ad1e7cc05e4b2777.webp)

1. আপনি যে কাজটি তৈরি করেছেন তা নির্বাচন করুন।

    ![কাজ নির্বাচন করুন।](../../../../../../translated_images/bn/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** নির্বাচন করুন।

1. **Model type** হিসেবে **MLflow** নির্বাচন করুন।

1. নিশ্চিত করুন **Job output** নির্বাচন করা আছে; এটি স্বয়ংক্রিয়ভাবে নির্বাচিত হওয়া উচিত।

    ![আউটপুট নির্বাচন করুন।](../../../../../../translated_images/bn/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** নির্বাচন করুন।

3. **Register** নির্বাচন করুন।

    ![রেজিস্টার নির্বাচন করুন।](../../../../../../translated_images/bn/07-04-register.fd82a3b293060bc7.webp)

4. আপনি বাম পাশে **Models** মেনুতে গিয়ে রেজিস্টারকৃত মডেল দেখতে পারবেন।

    ![রেজিস্টারকৃত মডেল।](../../../../../../translated_images/bn/07-05-registered-model.7db9775f58dfd591.webp)

#### ফাইন-টিউনকৃত মডেল ডিপ্লয় করুন

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেস তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **Real-time endpoints** নির্বাচন করুন।

    ![এন্ডপয়েন্ট তৈরি করুন।](../../../../../../translated_images/bn/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** নির্বাচন করুন।

1. আপনি যে রেজিস্টারকৃত মডেল তৈরি করেছেন তা নির্বাচন করুন।

    ![রেজিস্টারকৃত মডেল নির্বাচন করুন।](../../../../../../translated_images/bn/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** নির্বাচন করুন।

1. নিচের কাজগুলো সম্পাদন করুন:

    - **Virtual machine** হিসেবে *Standard_NC6s_v3* নির্বাচন করুন।
    - আপনি যে **Instance count** ব্যবহার করতে চান সেটি নির্বাচন করুন। উদাহরণস্বরূপ, *1*।
    - **Endpoint** হিসেবে **New** নির্বাচন করুন একটি এন্ডপয়েন্ট তৈরি করার জন্য।
    - **Endpoint name** লিখুন। এটি অবশ্যই অনন্য হতে হবে।
    - **Deployment name** লিখুন। এটি অবশ্যই অনন্য হতে হবে।

    ![ডিপ্লয়মেন্ট সেটিং পূরণ করুন।](../../../../../../translated_images/bn/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** নির্বাচন করুন।

> [!WARNING]
> আপনার অ্যাকাউন্টে অতিরিক্ত চার্জ এড়াতে, Azure Machine Learning ওয়ার্কস্পেসে তৈরি করা এন্ডপয়েন্টটি মুছে ফেলতে ভুলবেন না।
>

#### Azure Machine Learning ওয়ার্কস্পেসে ডিপ্লয়মেন্ট অবস্থা পরীক্ষা করুন

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেস তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

1. আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।

    ![এন্ডপয়েন্ট নির্বাচন করুন](../../../../../../translated_images/bn/07-09-check-deployment.325d18cae8475ef4.webp)

1. এই পৃষ্ঠায়, আপনি ডিপ্লয়মেন্ট প্রক্রিয়ার সময় এন্ডপয়েন্ট পরিচালনা করতে পারবেন।

> [!NOTE]
> ডিপ্লয়মেন্ট সম্পন্ন হলে নিশ্চিত করুন **Live traffic** **100%** এ সেট করা আছে। যদি না থাকে, ট্রাফিক সেটিংস সামঞ্জস্য করতে **Update traffic** নির্বাচন করুন। ট্রাফিক 0% এ থাকলে মডেল পরীক্ষা করা যাবে না।
>
> ![ট্রাফিক সেট করুন।](../../../../../../translated_images/bn/07-10-set-traffic.085b847e5751ff3d.webp)
>

## পরিস্থিতি ৩: Prompt flow-এর সাথে ইন্টিগ্রেট করুন এবং Microsoft Foundry-তে আপনার কাস্টম মডেলের সাথে চ্যাট করুন

### কাস্টম Phi-3 মডেল Prompt flow-এর সাথে ইন্টিগ্রেট করা

আপনি সফলভাবে আপনার ফাইন-টিউন করা মডেল ডিপ্লয় করার পর, এখন আপনি এটিকে Prompt Flow-এর সাথে ইন্টিগ্রেট করতে পারবেন যাতে আপনার মডেলটি রিয়েল-টাইম অ্যাপ্লিকেশনগুলোতে ব্যবহৃত হতে পারে এবং আপনার কাস্টম Phi-3 মডেলের সাথে বিভিন্ন ইন্টারেক্টিভ কাজ করা যাবে।

এই ব্যায়ামে, আপনি:

- Microsoft Foundry Hub তৈরি করবেন।
- Microsoft Foundry Project তৈরি করবেন।
- Prompt flow তৈরি করবেন।
- ফাইন-টিউনকৃত Phi-3 মডেলের জন্য একটি কাস্টম সংযোগ যোগ করবেন।
- আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করার জন্য Prompt flow সেট আপ করবেন।

> [!NOTE]
> আপনি Azure ML Studio ব্যবহার করেও Promptflow-এর সাথে ইন্টিগ্রেট করতে পারেন। একই ধরনের ইন্টিগ্রেশন প্রক্রিয়া Azure ML Studio-তেও প্রযোজ্য।

#### Microsoft Foundry Hub তৈরি করুন

Project তৈরি করার আগে আপনাকে একটি Hub তৈরি করতে হবে। একটি Hub একটি Resource Group-এর মতো কাজ করে, যা Microsoft Foundry-তে একাধিক Project সংগঠিত ও পরিচালনা করার সুযোগ দেয়।
1. পরিদর্শন করুন [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)।

1. বাম পাশে ট্যাব থেকে **All hubs** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New hub** নির্বাচন করুন।

    ![Create hub.](../../../../../../translated_images/bn/08-01-create-hub.8f7dd615bb8d9834.webp)

1. নিম্নলিখিত কাজগুলি করুন:

    - **Hub name** লিখুন। এটি অবশ্যই একটি অনন্য মান হতে হবে।
    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহারের জন্য **Location** নির্বাচন করুন।
    - ব্যবহারের জন্য **Connect Azure AI Services** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - **Connect Azure AI Search** থেকে **Skip connecting** নির্বাচন করুন।

    ![Fill hub.](../../../../../../translated_images/bn/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** নির্বাচন করুন।

#### Microsoft Foundry প্রজেক্ট তৈরি করুন

1. আপনি যে Hub তৈরি করেছেন সেখানে, বাম পাশে ট্যাব থেকে **All projects** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New project** নির্বাচন করুন।

    ![Select new project.](../../../../../../translated_images/bn/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** লিখুন। এটি অবশ্যই একটি অনন্য মান হতে হবে।

    ![Create project.](../../../../../../translated_images/bn/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** নির্বাচন করুন।

#### fine-tuned Phi-3 মডেলের জন্য একটি কাস্টম সংযোগ যোগ করুন

আপনার কাস্টম Phi-3 মডেলকে Prompt flow এর সাথে ইন্টিগ্রেশনের জন্য, আপনাকে মডেলের endpoint এবং key একটি কাস্টম সংযোগে সংরক্ষণ করতে হবে। এই সেটআপ নিশ্চিত করে আপনার কাস্টম Phi-3 মডেল Prompt flow এ অ্যাক্সেস করা যাবে।

#### fine-tuned Phi-3 মডেলের api key এবং endpoint uri সেট করুন

1. পরিদর্শন করুন [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)।

1. আপনি যে Azure Machine learning workspace তৈরি করেছেন সেখানে নেভিগেট করুন।

1. বাম পাশে ট্যাব থেকে **Endpoints** নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/bn/08-06-select-endpoints.aff38d453bcf9605.webp)

1. আপনি যে endpoint তৈরি করেছেন সেটি নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/bn/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. নেভিগেশন মেনু থেকে **Consume** নির্বাচন করুন।

1. আপনার **REST endpoint** এবং **Primary key** কপি করুন।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/bn/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### কাস্টম সংযোগ যোগ করুন

1. পরিদর্শন করুন [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)।

1. আপনি যে Microsoft Foundry প্রজেক্ট তৈরি করেছেন সেখানে নেভিগেট করুন।

1. আপনি যে প্রজেক্ট তৈরি করেছেন সেখানে, বাম পাশে ট্যাব থেকে **Settings** নির্বাচন করুন।

1. **+ New connection** নির্বাচন করুন।

    ![Select new connection.](../../../../../../translated_images/bn/08-09-select-new-connection.02eb45deadc401fc.webp)

1. নেভিগেশন মেনু থেকে **Custom keys** নির্বাচন করুন।

    ![Select custom keys.](../../../../../../translated_images/bn/08-10-select-custom-keys.856f6b2966460551.webp)

1. নিম্নলিখিত কাজগুলি করুন:

    - **+ Add key value pairs** নির্বাচন করুন।
    - কী নাম হিসাবে **endpoint** লিখুন এবং Azure ML Studio থেকে কপি করা endpoint মানটি value ফিল্ডে পেস্ট করুন।
    - আবার **+ Add key value pairs** নির্বাচন করুন।
    - কী নাম হিসাবে **key** লিখুন এবং Azure ML Studio থেকে কপি করা key মানটি value ফিল্ডে পেস্ট করুন।
    - কী গুলো যোগ করার পর, কী এক্সপোজ হওয়া থেকে রোধ করতে **is secret** নির্বাচন করুন।

    ![Add connection.](../../../../../../translated_images/bn/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** নির্বাচন করুন।

#### Prompt flow তৈরি করুন

আপনি Microsoft Foundry এ একটি কাস্টম সংযোগ যোগ করেছেন। এখন, নিম্নলিখিত ধাপগুলো অনুসরণ করে একটি Prompt flow তৈরি করুন। তারপর, আপনি এই Prompt flow কে কাস্টম সংযোগের সাথে সংযোগ করবেন যাতে আপনি fine-tuned মডেলটি Prompt flow এর মধ্যে ব্যবহার করতে পারেন।

1. আপনি যে Microsoft Foundry প্রজেক্ট তৈরি করেছেন সেখানে নেভিগেট করুন।

1. বাম পাশে ট্যাব থেকে **Prompt flow** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ Create** নির্বাচন করুন।

    ![Select Promptflow.](../../../../../../translated_images/bn/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. নেভিগেশন মেনু থেকে **Chat flow** নির্বাচন করুন।

    ![Select chat flow.](../../../../../../translated_images/bn/08-13-select-flow-type.2ec689b22da32591.webp)

1. ব্যবহারের জন্য **Folder name** লিখুন।

    ![Enter name.](../../../../../../translated_images/bn/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** নির্বাচন করুন।

#### আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করার জন্য Prompt flow সেট আপ করুন

আপনাকে fine-tuned Phi-3 মডেলটিকে Prompt flow তে ইন্টিগ্রেট করতে হবে। যদিও প্রদত্ত বিদ্যমান Prompt flow এই উদ্দেশ্যে তৈরি হয়নি। তাই, আপনাকে Prompt flow পুনর্নির্মাণ করতে হবে যা কাস্টম মডেল ইন্টিগ্রেশনের জন্য উপযুক্ত।

1. Prompt flow এ, বিদ্যমান ফ্লো পুনর্নির্মাণের জন্য নিম্নলিখিত কাজগুলি করুন:

    - **Raw file mode** নির্বাচন করুন।
    - *flow.dag.yml* ফাইলের সমস্ত বিদ্যমান কোড মুছে দিন।
    - *flow.dag.yml* ফাইলে নিম্নলিখিত কোড যোগ করুন।

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

    - **Save** নির্বাচন করুন।

    ![Select raw file mode.](../../../../../../translated_images/bn/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Prompt flow এ কাস্টম Phi-3 মডেল ব্যবহারের জন্য *integrate_with_promptflow.py* ফাইলে নিম্নলিখিত কোড যোগ করুন।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # লগ সেটআপ
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

        # "connection" হল কাস্টম কানেকশনের নাম, "endpoint", "key" হল কাস্টম কানেকশনের কী গুলো
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
            
            # সম্পূর্ণ JSON উত্তর লগ করুন
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

    ![Paste prompt flow code.](../../../../../../translated_images/bn/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry তে Prompt flow ব্যবহারের আরও বিস্তারিত তথ্যের জন্য দেখতে পারেন [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)।

1. আপনার মডেলের সাথে চ্যাট সক্ষম করতে **Chat input**, **Chat output** নির্বাচন করুন।

    ![Input Output.](../../../../../../translated_images/bn/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. এখন আপনি আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট শুরু করতে প্রস্তুত। পরবর্তী অনুশীলনে, আপনি শিখবেন কীভাবে Prompt flow শুরু করতে হয় এবং এটি ব্যবহার করে fine-tuned Phi-3 মডেলের সাথে চ্যাট করতে হয়।

> [!NOTE]
>
> পুনর্নির্মিত ফ্লো নিচের ছবির মতো হওয়া উচিত:
>
> ![Flow example.](../../../../../../translated_images/bn/08-18-graph-example.d6457533952e690c.webp)
>

### আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করুন

এখন যেহেতু আপনি আপনার কাস্টম Phi-3 মডেলটি fine-tune করে Prompt flow এর সাথে ইন্টিগ্রেট করেছেন, আপনি এটি ব্যবহার করে ইন্টারঅ্যাক্ট করতে প্রস্তুত। এই অনুশীলন আপনাকে Prompt flow ব্যবহার করে আপনার মডেলের সাথে চ্যাট শুরু এবং সেটআপ করার প্রক্রিয়া শেখাবে। এই ধাপগুলো অনুসরণ করে, আপনি বিভিন্ন কাজ এবং কথোপকথনের জন্য আপনার fine-tuned Phi-3 মডেলের সামর্থ্য পুরোপুরি ব্যবহার করতে পারবেন।

- Prompt flow ব্যবহার করে আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করুন।

#### Prompt flow শুরু করুন

1. Prompt flow শুরু করতে **Start compute sessions** নির্বাচন করুন।

    ![Start compute session.](../../../../../../translated_images/bn/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. প্যারামিটারগুলি রিনিউ করতে **Validate and parse input** নির্বাচন করুন।

    ![Validate input.](../../../../../../translated_images/bn/09-02-validate-input.317c76ef766361e9.webp)

1. আপনি যে কাস্টম সংযোগ তৈরি করেছেন, তার **connection** এর **Value** নির্বাচন করুন, যেমন *connection*।

    ![Connection.](../../../../../../translated_images/bn/09-03-select-connection.99bdddb4b1844023.webp)

#### আপনার কাস্টম মডেলের সাথে চ্যাট করুন

1. **Chat** নির্বাচন করুন।

    ![Select chat.](../../../../../../translated_images/bn/09-04-select-chat.61936dce6612a1e6.webp)

1. ফলাফলের উদাহরণ এখানে: এখন আপনি আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করতে পারেন। fine-tuning এর জন্য ব্যবহার করা ডেটার ভিত্তিতে প্রশ্ন করার পরামর্শ দেওয়া হয়।

    ![Chat with prompt flow.](../../../../../../translated_images/bn/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বিজ্ঞপ্তি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য নির্ভুলতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অশুদ্ধতা থাকতে পারে। মূল নথিটির নিজস্ব ভাষার নথিটিকেই প্রামাণিক সূত্র হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে সৃষ্ট কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->