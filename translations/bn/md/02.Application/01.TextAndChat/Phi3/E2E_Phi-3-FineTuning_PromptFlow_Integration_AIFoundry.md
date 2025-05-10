<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T17:55:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "bn"
}
-->
# Fine-tune এবং Azure AI Foundry-তে Prompt flow এর সাথে কাস্টম Phi-3 মডেল একত্রিত করুন

এই end-to-end (E2E) স্যাম্পলটি Microsoft Tech Community এর "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" গাইডের উপর ভিত্তি করে তৈরি। এটি Azure AI Foundry-তে Prompt flow এর সাথে কাস্টম Phi-3 মডেল ফাইন-টিউনিং, ডিপ্লয়মেন্ট এবং ইন্টিগ্রেশনের প্রক্রিয়া তুলে ধরে।  
E2E স্যাম্পলের বিপরীতে, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" যেখানে কোড লোকালভাবে চালানো হয়েছিল, এই টিউটোরিয়ালটি সম্পূর্ণভাবে Azure AI / ML Studio-র মধ্যে মডেল ফাইন-টিউনিং এবং ইন্টিগ্রেশনের উপর কেন্দ্রীভূত।

## ওভারভিউ

এই E2E স্যাম্পলে, আপনি শিখবেন কীভাবে Phi-3 মডেল ফাইন-টিউন করতে হয় এবং Azure AI Foundry-তে Prompt flow এর সাথে একত্রিত করতে হয়। Azure AI / ML Studio ব্যবহার করে, আপনি কাস্টম AI মডেল ডিপ্লয় এবং ব্যবহারের জন্য একটি ওয়ার্কফ্লো তৈরি করবেন। এই E2E স্যাম্পল তিনটি দৃশ্যপট (scenario) এ ভাগ করা হয়েছে:

**দৃশ্যপট ১: Azure রিসোর্স সেটআপ এবং ফাইন-টিউনিং-এর জন্য প্রস্তুতি**  

**দৃশ্যপট ২: Phi-3 মডেল ফাইন-টিউন এবং Azure Machine Learning Studio-তে ডিপ্লয়**  

**দৃশ্যপট ৩: Prompt flow-এর সাথে ইন্টিগ্রেট এবং Azure AI Foundry-তে আপনার কাস্টম মডেলের সাথে চ্যাট করুন**  

নিচে এই E2E স্যাম্পলের একটি সারাংশ দেওয়া হলো।

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.bn.png)

### বিষয়বস্তু সূচি

1. **[দৃশ্যপট ১: Azure রিসোর্স সেটআপ এবং ফাইন-টিউনিং-এর জন্য প্রস্তুতি](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Azure সাবস্ক্রিপশনে GPU কোটা অনুরোধ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [রোল অ্যাসাইনমেন্ট যোগ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [প্রজেক্ট সেটআপ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [ফাইন-টিউনিং-এর জন্য ডেটাসেট প্রস্তুত করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[দৃশ্যপট ২: Phi-3 মডেল ফাইন-টিউন এবং Azure Machine Learning Studio-তে ডিপ্লয়](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Phi-3 মডেল ফাইন-টিউন করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [ফাইন-টিউন করা Phi-3 মডেল ডিপ্লয় করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[দৃশ্যপট ৩: Prompt flow-এর সাথে ইন্টিগ্রেট এবং Azure AI Foundry-তে আপনার কাস্টম মডেলের সাথে চ্যাট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [কাস্টম Phi-3 মডেল Prompt flow-এর সাথে ইন্টিগ্রেট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## দৃশ্যপট ১: Azure রিসোর্স সেটআপ এবং ফাইন-টিউনিং-এর জন্য প্রস্তুতি

### Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন

1. পোর্টালের উপরের **সার্চ বার**-এ *azure machine learning* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Azure Machine Learning** নির্বাচন করুন।

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.bn.png)

2. ন্যাভিগেশন মেনু থেকে **+ Create** নির্বাচন করুন।

3. ন্যাভিগেশন মেনু থেকে **New workspace** নির্বাচন করুন।

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.bn.png)

4. নিম্নলিখিত কাজগুলো সম্পন্ন করুন:

    - আপনার Azure **Subscription** নির্বাচন করুন।  
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।  
    - **Workspace Name** লিখুন। এটি অবশ্যই ইউনিক হতে হবে।  
    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।  
    - ব্যবহার করার জন্য **Storage account** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।  
    - ব্যবহার করার জন্য **Key vault** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।  
    - ব্যবহার করার জন্য **Application insights** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।  
    - ব্যবহার করার জন্য **Container registry** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.bn.png)

5. **Review + Create** নির্বাচন করুন।

6. **Create** নির্বাচন করুন।

### Azure সাবস্ক্রিপশনে GPU কোটা অনুরোধ করুন

এই টিউটোরিয়ালে, আপনি Phi-3 মডেল ফাইন-টিউন এবং ডিপ্লয় করার জন্য GPU ব্যবহার করবেন। ফাইন-টিউনিং-এর জন্য *Standard_NC24ads_A100_v4* GPU ব্যবহার করবেন, যার জন্য কোটা অনুরোধ প্রয়োজন। ডিপ্লয়মেন্টের জন্য *Standard_NC6s_v3* GPU ব্যবহার করবেন, যার জন্যও কোটা অনুরোধ প্রয়োজন।

> [!NOTE]  
> শুধুমাত্র Pay-As-You-Go সাবস্ক্রিপশন (স্ট্যান্ডার্ড সাবস্ক্রিপশন টাইপ) GPU বরাদ্দের জন্য উপযুক্ত; বেনিফিট সাবস্ক্রিপশন বর্তমানে সমর্থিত নয়।  

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. *Standard NCADSA100v4 Family* কোটা অনুরোধ করতে নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Quota** নির্বাচন করুন।  
    - ব্যবহার করার জন্য **Virtual machine family** নির্বাচন করুন। যেমন, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* নির্বাচন করুন, যা *Standard_NC24ads_A100_v4* GPU অন্তর্ভুক্ত।  
    - ন্যাভিগেশন মেনু থেকে **Request quota** নির্বাচন করুন।  

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.bn.png)

    - Request quota পৃষ্ঠায়, আপনি যে **New cores limit** ব্যবহার করতে চান তা লিখুন। যেমন, ২৪।  
    - Request quota পৃষ্ঠায়, GPU কোটা অনুরোধ করতে **Submit** নির্বাচন করুন।  

1. *Standard NCSv3 Family* কোটা অনুরোধ করতে নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Quota** নির্বাচন করুন।  
    - ব্যবহার করার জন্য **Virtual machine family** নির্বাচন করুন। যেমন, *Standard NCSv3 Family Cluster Dedicated vCPUs* নির্বাচন করুন, যা *Standard_NC6s_v3* GPU অন্তর্ভুক্ত।  
    - ন্যাভিগেশন মেনু থেকে **Request quota** নির্বাচন করুন।  
    - Request quota পৃষ্ঠায়, আপনি যে **New cores limit** ব্যবহার করতে চান তা লিখুন। যেমন, ২৪।  
    - Request quota পৃষ্ঠায়, GPU কোটা অনুরোধ করতে **Submit** নির্বাচন করুন।  

### রোল অ্যাসাইনমেন্ট যোগ করুন

আপনার মডেল ফাইন-টিউন এবং ডিপ্লয় করার জন্য, প্রথমে একটি User Assigned Managed Identity (UAI) তৈরি করতে হবে এবং তাকে যথাযথ পারমিশন দিতে হবে। এই UAI ডিপ্লয়মেন্টের সময় প্রমাণীকরণের জন্য ব্যবহৃত হবে।

#### User Assigned Managed Identity (UAI) তৈরি করুন

1. পোর্টালের উপরের **সার্চ বার**-এ *managed identities* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Managed Identities** নির্বাচন করুন।

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.bn.png)

1. **+ Create** নির্বাচন করুন।

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.bn.png)

1. নিম্নলিখিত কাজগুলো করুন:

    - আপনার Azure **Subscription** নির্বাচন করুন।  
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।  
    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।  
    - **Name** লিখুন। এটি অবশ্যই ইউনিক হতে হবে।  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.bn.png)

1. **Review + create** নির্বাচন করুন।

1. **+ Create** নির্বাচন করুন।

#### Managed Identity-তে Contributor রোল অ্যাসাইন করুন

1. আপনি যে Managed Identity তৈরি করেছেন সেই রিসোর্সে যান।

1. বাম পাশের ট্যাব থেকে **Azure role assignments** নির্বাচন করুন।

1. ন্যাভিগেশন মেনু থেকে **+Add role assignment** নির্বাচন করুন।

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:  
    - **Scope** হিসেবে **Resource group** নির্বাচন করুন।  
    - আপনার Azure **Subscription** নির্বাচন করুন।  
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন।  
    - **Role** হিসেবে **Contributor** নির্বাচন করুন।  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.bn.png)

2. **Save** নির্বাচন করুন।

#### Managed Identity-তে Storage Blob Data Reader রোল অ্যাসাইন করুন

1. পোর্টালের উপরের **সার্চ বার**-এ *storage accounts* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage accounts** নির্বাচন করুন।

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.bn.png)

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেস তৈরি করেছেন তার সাথে যুক্ত স্টোরেজ অ্যাকাউন্ট নির্বাচন করুন। যেমন, *finetunephistorage*।

1. Add role assignment পৃষ্ঠায় যেতে নিম্নলিখিত কাজগুলো করুন:

    - আপনার তৈরি করা Azure Storage অ্যাকাউন্টে যান।  
    - বাম পাশের ট্যাব থেকে **Access Control (IAM)** নির্বাচন করুন।  
    - ন্যাভিগেশন মেনু থেকে **+ Add** নির্বাচন করুন।  
    - ন্যাভিগেশন মেনু থেকে **Add role assignment** নির্বাচন করুন।  

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.bn.png)

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:

    - Role পৃষ্ঠায়, সার্চ বক্সে *Storage Blob Data Reader* লিখুন এবং প্রদর্শিত অপশন থেকে **Storage Blob Data Reader** নির্বাচন করুন।  
    - Role পৃষ্ঠায় **Next** নির্বাচন করুন।  
    - Members পৃষ্ঠায়, **Assign access to** হিসেবে **Managed identity** নির্বাচন করুন।  
    - Members পৃষ্ঠায় **+ Select members** নির্বাচন করুন।  
    - Select managed identities পৃষ্ঠায় আপনার Azure **Subscription** নির্বাচন করুন।  
    - Select managed identities পৃষ্ঠায় **Managed identity** হিসেবে **Manage Identity** নির্বাচন করুন।  
    - Select managed identities পৃষ্ঠায় আপনি যে Managed Identity তৈরি করেছেন তা নির্বাচন করুন। যেমন, *finetunephi-managedidentity*।  
    - Select managed identities পৃষ্ঠায় **Select** নির্বাচন করুন।  

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.bn.png)

1. **Review + assign** নির্বাচন করুন।

#### Managed Identity-তে AcrPull রোল অ্যাসাইন করুন

1. পোর্টালের উপরের **সার্চ বার**-এ *container registries* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Container registries** নির্বাচন করুন।

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.bn.png)

1. Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত container registry নির্বাচন করুন। যেমন, *finetunephicontainerregistry*।

1. Add role assignment পৃষ্ঠায় যেতে নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Access Control (IAM)** নির্বাচন করুন।  
    - ন্যাভিগেশন মেনু থেকে **+ Add** নির্বাচন করুন।  
    - ন্যাভিগেশন মেনু থেকে **Add role assignment** নির্বাচন করুন।  

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:

    - Role পৃষ্ঠায়, সার্চ বক্সে *AcrPull* লিখুন এবং প্রদর্শিত অপশন থেকে **AcrPull** নির্বাচন করুন।  
    - Role পৃষ্ঠায় **Next** নির্বাচন করুন।  
    - Members পৃষ্ঠায়, **Assign access to** হিসেবে **Managed identity** নির্বাচন করুন।  
    - Members পৃষ্ঠায় **+ Select members** নির্বাচন করুন।  
    - Select managed identities পৃষ্ঠায় আপনার Azure **Subscription** নির্বাচন করুন।  
    - Select managed identities পৃষ্ঠায় **Managed identity** হিসেবে **Manage Identity** নির্বাচন করুন।  
    - Select managed identities পৃষ্ঠায় আপনি যে Managed Identity তৈরি করেছেন তা নির্বাচন করুন। যেমন, *finetunephi-managedidentity*।  
    - Select managed identities পৃষ্ঠায় **Select** নির্বাচন করুন।  
    - **Review + assign** নির্বাচন করুন।

### প্রজেক্ট সেটআপ করুন

ফাইন-টিউনিং-এর জন্য প্রয়োজনীয় ডেটাসেট ডাউনলোড করতে, আপনি একটি লোকাল পরিবেশ সেটআপ করবেন।

এই অনুশীলনে, আপনি:

- কাজ করার জন্য একটি ফোল্ডার তৈরি করবেন।  
- একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করবেন।  
- প্রয়োজনীয় প্যাকেজসমূহ ইনস্টল করবেন।  
- ডেটাসেট ডাউনলোড করার জন্য *download_dataset.py* ফাইল তৈরি করবেন।  

#### কাজ করার জন্য একটি ফোল্ডার তৈরি করুন

1. একটি টার্মিনাল উইন্ডো খুলুন এবং ডিফল্ট পাথে *finetune-phi* নামে একটি ফোল্ডার তৈরি করতে নিম্নলিখিত কমান্ড টাইপ করুন।

    ```console
    mkdir finetune-phi
    ```

2. আপনার টার্মিনালে নিম্নলিখিত কমান্ড টাইপ করে তৈরি করা *finetune-phi* ফোল্ডারে যান।

    ```console
    cd finetune-phi
    ```

#### ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

1. আপনার টার্মিনালে নিম্নলিখিত কমান্ড টাইপ করে *.venv* নামে একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন।

    ```console
    python -m venv .venv
    ```

2. আপনার টার্মিনালে নিম্নলিখিত কমান্ড টাইপ করে ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> যদি সফল হয়, তাহলে কমান্ড প্রম্পটের আগে *(.venv)* দেখতে পাবেন।

#### প্রয়োজনীয় প্যাকেজসমূহ ইনস্টল করুন

1. আপনার টার্মিনালে নিম্নলিখিত কমান্ডসমূহ টাইপ করে প্রয়োজনীয় প্যাকেজসমূহ ইনস্টল করুন।

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` তৈরি করুন

> [!NOTE]  
> সম্পূর্ণ ফোল্ডার স্ট্রাকচার:  
>  
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** খুলুন।

1. মেনুবার থেকে **File** নির্বাচন করুন।

1. **Open Folder** নির্বাচন করুন।

1. আপনি যে *finetune-phi* ফোল্ডার তৈরি করেছেন তা নির্বাচন করুন, যা *C:\Users\yourUserName\finetune-phi* অবস্থানে রয়েছে।

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.bn.png)

1. Visual Studio Code-এর বাম প্যানে রাইট-ক্লিক করে **New File** নির্বাচন করুন এবং *download_dataset.py* নামে একটি নতুন ফাইল তৈরি করুন।

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.bn.png)

### ফাইন-টিউনিং-এর জন্য ডেটাসেট প্রস্তুত করুন

এই অনুশীলনে, আপনি *download_dataset.py* ফাইল চালিয়ে *ultrachat_200k* ডেটাসেট আপনার লোকাল পরিবেশে ডাউনলোড করবেন। এরপর এই ডেটাসেট ব্যবহার করে Azure Machine Learning-এ Phi-3 মডেল ফাইন-টিউন করবেন।

এই অনুশীলনে, আপনি:

- *download_dataset.py* ফাইলে ডেটাসেট ডাউনলোড করার কোড যোগ করবেন।  
- *download_dataset.py* ফাইল চালিয়ে ডেটাসেট আপনার লোকাল পরিবেশে
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. বাম পাশের ট্যাব থেকে **Compute** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **Compute clusters** নির্বাচন করুন।

1. **+ New** নির্বাচন করুন।

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.bn.png)

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:

    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।
    - **Virtual machine tier** নির্বাচন করুন **Dedicated** হিসেবে।
    - **Virtual machine type** নির্বাচন করুন **GPU** হিসেবে।
    - **Virtual machine size** ফিল্টার নির্বাচন করুন **Select from all options** হিসেবে।
    - **Virtual machine size** নির্বাচন করুন **Standard_NC24ads_A100_v4** হিসেবে।

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.bn.png)

1. **Next** নির্বাচন করুন।

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:

    - **Compute name** লিখুন। এটি একটি অনন্য মান হতে হবে।
    - **Minimum number of nodes** নির্বাচন করুন **0** হিসেবে।
    - **Maximum number of nodes** নির্বাচন করুন **1** হিসেবে।
    - **Idle seconds before scale down** নির্বাচন করুন **120** হিসেবে।

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.bn.png)

1. **Create** নির্বাচন করুন।

#### Phi-3 মডেল ফাইন-টিউন করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. আপনি যে Azure Machine Learning workspace তৈরি করেছেন তা নির্বাচন করুন।

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.bn.png)

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:

    - বাম পাশের ট্যাব থেকে **Model catalog** নির্বাচন করুন।
    - **search bar** এ *phi-3-mini-4k* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Phi-3-mini-4k-instruct** নির্বাচন করুন।

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.bn.png)

1. নেভিগেশন মেনু থেকে **Fine-tune** নির্বাচন করুন।

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.bn.png)

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:

    - **Select task type** নির্বাচন করুন **Chat completion** হিসেবে।
    - **+ Select data** নির্বাচন করে **Traning data** আপলোড করুন।
    - Validation data আপলোড টাইপ নির্বাচন করুন **Provide different validation data** হিসেবে।
    - **+ Select data** নির্বাচন করে **Validation data** আপলোড করুন।

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.bn.png)

    > [!TIP]
    >
    > আপনি **Advanced settings** নির্বাচন করে **learning_rate** এবং **lr_scheduler_type** এর মতো কনফিগারেশন কাস্টমাইজ করতে পারেন, যাতে ফাইন-টিউনিং প্রক্রিয়াটি আপনার নির্দিষ্ট প্রয়োজন অনুযায়ী অপ্টিমাইজ করা যায়।

1. **Finish** নির্বাচন করুন।

1. এই অনুশীলনে, আপনি সফলভাবে Azure Machine Learning ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করেছেন। দয়া করে মনে রাখবেন, ফাইন-টিউনিং প্রক্রিয়াটি কিছুটা সময় নিতে পারে। ফাইন-টিউনিং কাজ চালানোর পরে, সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করতে হবে। Azure Machine Learning Workspace এর বাম পাশের Jobs ট্যাবে গিয়ে আপনি ফাইন-টিউনিং কাজের অবস্থা পর্যবেক্ষণ করতে পারেন। পরবর্তী সিরিজে, আপনি ফাইন-টিউন করা মডেলটি ডিপ্লয় করবেন এবং Prompt flow এর সাথে ইন্টিগ্রেট করবেন।

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.bn.png)

### ফাইন-টিউন করা Phi-3 মডেল ডিপ্লয় করুন

ফাইন-টিউন করা Phi-3 মডেলকে Prompt flow এর সাথে ইন্টিগ্রেট করতে, আপনাকে মডেলটি ডিপ্লয় করতে হবে যাতে এটি রিয়েল-টাইম ইনফারেন্সের জন্য অ্যাক্সেসযোগ্য হয়। এই প্রক্রিয়ায় মডেল রেজিস্টার করা, অনলাইন এন্ডপয়েন্ট তৈরি করা এবং মডেল ডিপ্লয় করা অন্তর্ভুক্ত।

এই অনুশীলনে, আপনি:

- Azure Machine Learning workspace এ ফাইন-টিউন করা মডেল রেজিস্টার করবেন।
- একটি অনলাইন এন্ডপয়েন্ট তৈরি করবেন।
- রেজিস্টার করা ফাইন-টিউন করা Phi-3 মডেল ডিপ্লয় করবেন।

#### ফাইন-টিউন করা মডেল রেজিস্টার করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. আপনি যে Azure Machine Learning workspace তৈরি করেছেন তা নির্বাচন করুন।

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.bn.png)

1. বাম পাশের ট্যাব থেকে **Models** নির্বাচন করুন।

1. **+ Register** নির্বাচন করুন।

1. **From a job output** নির্বাচন করুন।

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.bn.png)

1. আপনি যে কাজটি তৈরি করেছেন তা নির্বাচন করুন।

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.bn.png)

1. **Next** নির্বাচন করুন।

1. **Model type** নির্বাচন করুন **MLflow** হিসেবে।

1. নিশ্চিত করুন যে **Job output** নির্বাচিত আছে; এটি স্বয়ংক্রিয়ভাবে নির্বাচিত হওয়া উচিত।

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.bn.png)

2. **Next** নির্বাচন করুন।

3. **Register** নির্বাচন করুন।

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.bn.png)

4. আপনি আপনার রেজিস্টার করা মডেল দেখতে পারবেন বাম পাশের ট্যাব থেকে **Models** মেনুতে গিয়ে।

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.bn.png)

#### ফাইন-টিউন করা মডেল ডিপ্লয় করুন

1. আপনি যে Azure Machine Learning workspace তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **Real-time endpoints** নির্বাচন করুন।

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.bn.png)

1. **Create** নির্বাচন করুন।

1. আপনি যে রেজিস্টার করা মডেলটি তৈরি করেছেন তা নির্বাচন করুন।

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.bn.png)

1. **Select** নির্বাচন করুন।

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:

    - **Virtual machine** নির্বাচন করুন *Standard_NC6s_v3* হিসেবে।
    - আপনি যে **Instance count** ব্যবহার করতে চান তা নির্বাচন করুন, উদাহরণস্বরূপ *1*।
    - **Endpoint** নির্বাচন করুন **New** হিসেবে নতুন এন্ডপয়েন্ট তৈরি করার জন্য।
    - **Endpoint name** লিখুন। এটি একটি অনন্য মান হতে হবে।
    - **Deployment name** লিখুন। এটি একটি অনন্য মান হতে হবে।

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.bn.png)

1. **Deploy** নির্বাচন করুন।

> [!WARNING]
> আপনার অ্যাকাউন্টে অতিরিক্ত চার্জ এড়াতে, Azure Machine Learning workspace এ তৈরি করা এন্ডপয়েন্টটি মুছে ফেলা নিশ্চিত করুন।
>

#### Azure Machine Learning Workspace এ ডিপ্লয়মেন্ট স্ট্যাটাস চেক করুন

1. আপনি যে Azure Machine Learning workspace তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

1. আপনি যে এন্ডপয়েন্টটি তৈরি করেছেন তা নির্বাচন করুন।

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.bn.png)

1. এই পৃষ্ঠায়, আপনি ডিপ্লয়মেন্ট প্রক্রিয়ার সময় এন্ডপয়েন্টগুলি পরিচালনা করতে পারেন।

> [!NOTE]
> ডিপ্লয়মেন্ট সম্পন্ন হলে, নিশ্চিত করুন যে **Live traffic** সেট করা আছে **100%** এ। যদি না থাকে, তবে ট্রাফিক সেটিংস সামঞ্জস্য করার জন্য **Update traffic** নির্বাচন করুন। মনে রাখবেন, ট্রাফিক 0% হলে মডেল টেস্ট করা যাবে না।
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.bn.png)
>

## সিনারিও ৩: Prompt flow এর সাথে ইন্টিগ্রেট করুন এবং Azure AI Foundry তে আপনার কাস্টম মডেলের সাথে চ্যাট করুন

### Prompt flow এর সাথে কাস্টম Phi-3 মডেল ইন্টিগ্রেট করুন

আপনার ফাইন-টিউন করা মডেল সফলভাবে ডিপ্লয় করার পর, এখন আপনি এটি Prompt Flow এর সাথে ইন্টিগ্রেট করতে পারেন যাতে আপনার মডেলটি রিয়েল-টাইম অ্যাপ্লিকেশনগুলোতে ব্যবহার করা যায়, এবং আপনার কাস্টম Phi-3 মডেলের সাথে বিভিন্ন ইন্টারেক্টিভ কাজ করতে পারেন।

এই অনুশীলনে, আপনি:

- Azure AI Foundry Hub তৈরি করবেন।
- Azure AI Foundry Project তৈরি করবেন।
- Prompt flow তৈরি করবেন।
- ফাইন-টিউন করা Phi-3 মডেলের জন্য একটি কাস্টম কানেকশন যোগ করবেন।
- আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করার জন্য Prompt flow সেটআপ করবেন।

> [!NOTE]
> আপনি Azure ML Studio ব্যবহার করেও Promptflow এর সাথে ইন্টিগ্রেট করতে পারেন। একই ইন্টিগ্রেশন প্রক্রিয়া Azure ML Studio তেও প্রযোজ্য।

#### Azure AI Foundry Hub তৈরি করুন

প্রজেক্ট তৈরি করার আগে একটি Hub তৈরি করতে হবে। একটি Hub একটি Resource Group এর মত কাজ করে, যা Azure AI Foundry এর মধ্যে একাধিক প্রজেক্টকে সংগঠিত ও পরিচালনা করতে সাহায্য করে।

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) এ যান।

1. বাম পাশের ট্যাব থেকে **All hubs** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New hub** নির্বাচন করুন।

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.bn.png)

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:

    - **Hub name** লিখুন। এটি একটি অনন্য মান হতে হবে।
    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - আপনি যে **Location** ব্যবহার করতে চান তা নির্বাচন করুন।
    - ব্যবহার করার জন্য **Connect Azure AI Services** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - **Connect Azure AI Search** নির্বাচন করুন **Skip connecting** হিসেবে।

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.bn.png)

1. **Next** নির্বাচন করুন।

#### Azure AI Foundry Project তৈরি করুন

1. আপনি যে Hub তৈরি করেছেন সেখানে বাম পাশের ট্যাব থেকে **All projects** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New project** নির্বাচন করুন।

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.bn.png)

1. **Project name** লিখুন। এটি একটি অনন্য মান হতে হবে।

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.bn.png)

1. **Create a project** নির্বাচন করুন।

#### ফাইন-টিউন করা Phi-3 মডেলের জন্য একটি কাস্টম কানেকশন যোগ করুন

আপনার কাস্টম Phi-3 মডেলকে Prompt flow এর সাথে ইন্টিগ্রেট করতে, আপনাকে মডেলের এন্ডপয়েন্ট এবং কী কাস্টম কানেকশনে সংরক্ষণ করতে হবে। এই সেটআপ নিশ্চিত করে যে Prompt flow থেকে আপনার কাস্টম Phi-3 মডেলে অ্যাক্সেস পাওয়া যায়।

#### ফাইন-টিউন করা Phi-3 মডেলের api key এবং endpoint uri সেট করুন

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) এ যান।

1. আপনি যে Azure Machine Learning workspace তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.bn.png)

1. আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.bn.png)

1. নেভিগেশন মেনু থেকে **Consume** নির্বাচন করুন।

1. আপনার **REST endpoint** এবং **Primary key** কপি করুন।
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.bn.png)

#### কাস্টম কানেকশন যোগ করুন

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) এ যান।

1. আপনি যে Azure AI Foundry প্রকল্প তৈরি করেছেন সেটিতে যান।

1. আপনি যে প্রকল্পটি তৈরি করেছেন, সেখানে বাম পাশের ট্যাব থেকে **Settings** নির্বাচন করুন।

1. **+ New connection** নির্বাচন করুন।

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.bn.png)

1. নেভিগেশন মেনু থেকে **Custom keys** নির্বাচন করুন।

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.bn.png)

1. নিম্নলিখিত কাজগুলি করুন:

    - **+ Add key value pairs** নির্বাচন করুন।
    - কী নাম হিসেবে **endpoint** লিখুন এবং Azure ML Studio থেকে কপি করা endpoint টি value ফিল্ডে পেস্ট করুন।
    - আবার **+ Add key value pairs** নির্বাচন করুন।
    - কী নাম হিসেবে **key** লিখুন এবং Azure ML Studio থেকে কপি করা key টি value ফিল্ডে পেস্ট করুন।
    - কী গুলো যোগ করার পর, কী গুলো লুকানোর জন্য **is secret** নির্বাচন করুন।

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.bn.png)

1. **Add connection** নির্বাচন করুন।

#### Prompt flow তৈরি করুন

আপনি Azure AI Foundry-তে একটি কাস্টম কানেকশন যোগ করেছেন। এখন, নিচের ধাপগুলো অনুসরণ করে একটি Prompt flow তৈরি করুন। এরপর, এই Prompt flow-কে কাস্টম কানেকশনের সাথে সংযুক্ত করবেন যাতে আপনি Prompt flow-এর মধ্যে fine-tuned মডেল ব্যবহার করতে পারেন।

1. আপনি যে Azure AI Foundry প্রকল্প তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Prompt flow** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ Create** নির্বাচন করুন।

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.bn.png)

1. নেভিগেশন মেনু থেকে **Chat flow** নির্বাচন করুন।

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.bn.png)

1. ব্যবহার করার জন্য **Folder name** লিখুন।

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.bn.png)

2. **Create** নির্বাচন করুন।

#### আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করার জন্য Prompt flow সেটআপ করুন

আপনাকে fine-tuned Phi-3 মডেলটি একটি Prompt flow-র সাথে ইন্টিগ্রেট করতে হবে। তবে, বিদ্যমান Prompt flow এই উদ্দেশ্যে তৈরি নয়। তাই, আপনাকে Prompt flow পুনরায় ডিজাইন করতে হবে যাতে কাস্টম মডেল ইন্টিগ্রেশন সম্ভব হয়।

1. Prompt flow-তে বিদ্যমান ফ্লো পুনর্নির্মাণের জন্য নিম্নলিখিত কাজগুলি করুন:

    - **Raw file mode** নির্বাচন করুন।
    - *flow.dag.yml* ফাইলে থাকা সমস্ত কোড মুছে ফেলুন।
    - *flow.dag.yml* ফাইলে নিচের কোডটি যোগ করুন।

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.bn.png)

1. Prompt flow-তে কাস্টম Phi-3 মডেল ব্যবহার করার জন্য *integrate_with_promptflow.py* ফাইলে নিচের কোডটি যোগ করুন।

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.bn.png)

> [!NOTE]
> Azure AI Foundry-তে Prompt flow ব্যবহারের আরও বিস্তারিত তথ্যের জন্য, আপনি [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) দেখতে পারেন।

1. আপনার মডেলের সাথে চ্যাট সক্ষম করতে **Chat input**, **Chat output** নির্বাচন করুন।

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.bn.png)

1. এখন আপনি আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করার জন্য প্রস্তুত। পরবর্তী অনুশীলনে, আপনি শিখবেন কীভাবে Prompt flow শুরু করতে হয় এবং fine-tuned Phi-3 মডেলের সাথে চ্যাট করতে হয়।

> [!NOTE]
>
> পুনর্নির্মিত ফ্লো নিচের ছবির মতো হওয়া উচিত:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.bn.png)
>

### আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করুন

এখন যেহেতু আপনি আপনার কাস্টম Phi-3 মডেলটি fine-tune করে Prompt flow-র সাথে ইন্টিগ্রেট করেছেন, আপনি এটি ব্যবহার করে চ্যাট শুরু করতে প্রস্তুত। এই অনুশীলনটি আপনাকে মডেলটির সাথে চ্যাট সেটআপ এবং শুরু করার ধাপগুলো দেখাবে। এই ধাপগুলো অনুসরণ করে আপনি আপনার fine-tuned Phi-3 মডেলের পূর্ণ ক্ষমতা বিভিন্ন কাজ ও কথোপকথনের জন্য ব্যবহার করতে পারবেন।

- Prompt flow ব্যবহার করে আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করুন।

#### Prompt flow শুরু করুন

1. Prompt flow শুরু করতে **Start compute sessions** নির্বাচন করুন।

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.bn.png)

1. প্যারামিটার রিফ্রেশ করতে **Validate and parse input** নির্বাচন করুন।

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.bn.png)

1. আপনি যে কাস্টম কানেকশন তৈরি করেছেন তার **connection** এর **Value** নির্বাচন করুন। যেমন, *connection*।

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.bn.png)

#### আপনার কাস্টম মডেলের সাথে চ্যাট করুন

1. **Chat** নির্বাচন করুন।

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.bn.png)

1. ফলাফলের একটি উদাহরণ: এখন আপনি আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করতে পারবেন। fine-tuning এর জন্য ব্যবহৃত ডেটার ওপর ভিত্তি করে প্রশ্ন করা উত্তম।

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.bn.png)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় সর্বোত্তম এবং নির্ভরযোগ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।