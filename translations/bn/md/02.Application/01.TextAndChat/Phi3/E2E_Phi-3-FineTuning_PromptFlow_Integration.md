<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:17:01+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "bn"
}
-->
# কাস্টম Phi-3 মডেল ফাইন-টিউন এবং Prompt flow এর সাথে ইন্টিগ্রেট করুন

এই end-to-end (E2E) স্যাম্পলটি Microsoft Tech Community থেকে "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" গাইডের উপর ভিত্তি করে তৈরি। এটি কাস্টম Phi-3 মডেল ফাইন-টিউন, ডিপ্লয় এবং Prompt flow এর সাথে ইন্টিগ্রেশনের প্রক্রিয়া পরিচয় করিয়ে দেয়।

## ওভারভিউ

এই E2E স্যাম্পলে, আপনি শিখবেন কিভাবে Phi-3 মডেল ফাইন-টিউন করতে হয় এবং Prompt flow এর সাথে ইন্টিগ্রেট করতে হয়। Azure Machine Learning এবং Prompt flow ব্যবহার করে, আপনি কাস্টম AI মডেল ডিপ্লয় এবং ব্যবহার করার জন্য একটি ওয়ার্কফ্লো তৈরি করবেন। এই E2E স্যাম্পলটি তিনটি সিনারিওতে বিভক্ত:

**সিনারিও ১: Azure রিসোর্স সেটআপ এবং ফাইন-টিউনের জন্য প্রস্তুতি**

**সিনারিও ২: Phi-3 মডেল ফাইন-টিউন এবং Azure Machine Learning Studio তে ডিপ্লয়**

**সিনারিও ৩: Prompt flow এর সাথে ইন্টিগ্রেট এবং আপনার কাস্টম মডেলের সাথে চ্যাট করুন**

এখানে এই E2E স্যাম্পলের একটি ওভারভিউ দেওয়া হলো।

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468cf3bbb3158cf273380cbdf7fcec042c7328e1559c6b2e2632.bn.png)

### বিষয়বস্তু সূচি

1. **[সিনারিও ১: Azure রিসোর্স সেটআপ এবং ফাইন-টিউনের জন্য প্রস্তুতি](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure সাবস্ক্রিপশনে GPU কোটা অনুরোধ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [রোল অ্যাসাইনমেন্ট যোগ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [প্রজেক্ট সেটআপ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ফাইন-টিউনের জন্য ডেটাসেট প্রস্তুত করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[সিনারিও ২: Phi-3 মডেল ফাইন-টিউন এবং Azure Machine Learning Studio তে ডিপ্লয়](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI সেটআপ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 মডেল ফাইন-টিউন করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ফাইন-টিউন করা মডেল ডিপ্লয় করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[সিনারিও ৩: Prompt flow এর সাথে ইন্টিগ্রেট এবং আপনার কাস্টম মডেলের সাথে চ্যাট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [কাস্টম Phi-3 মডেল Prompt flow এর সাথে ইন্টিগ্রেট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [আপনার কাস্টম মডেলের সাথে চ্যাট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## সিনারিও ১: Azure রিসোর্স সেটআপ এবং ফাইন-টিউনের জন্য প্রস্তুতি

### Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন

1. পোর্টালের উপরের **search bar**-এ *azure machine learning* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Azure Machine Learning** নির্বাচন করুন।

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c600d87008fb78206d2cf90c0b920c231618a8ec8baaa6f46c3.bn.png)

1. নেভিগেশন মেনু থেকে **+ Create** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **New workspace** নির্বাচন করুন।

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4fbb808d1bbcd92962692b1fa687f4c5d3952f453177825bc.bn.png)

1. নিম্নলিখিত কাজগুলো করুন:

    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - **Workspace Name** লিখুন। এটি অবশ্যই ইউনিক হতে হবে।
    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।
    - ব্যবহার করার জন্য **Storage account** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহার করার জন্য **Key vault** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহার করার জন্য **Application insights** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহার করার জন্য **Container registry** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb141b9e8c16f31834e82e831275bd9faad0b70343f46255de.bn.png)

1. **Review + Create** নির্বাচন করুন।

1. **Create** নির্বাচন করুন।

### Azure সাবস্ক্রিপশনে GPU কোটা অনুরোধ করুন

এই E2E স্যাম্পলে, আপনি ফাইন-টিউনের জন্য *Standard_NC24ads_A100_v4 GPU* ব্যবহার করবেন, যার জন্য কোটা অনুরোধ প্রয়োজন, এবং ডিপ্লয়ের জন্য *Standard_E4s_v3* CPU ব্যবহার করবেন, যার জন্য কোটা অনুরোধের প্রয়োজন নেই।

> [!NOTE]
>
> শুধুমাত্র Pay-As-You-Go সাবস্ক্রিপশন (স্ট্যান্ডার্ড সাবস্ক্রিপশন টাইপ) GPU বরাদ্দের জন্য যোগ্য; বেনিফিট সাবস্ক্রিপশনগুলো বর্তমানে সমর্থিত নয়।
>
> যারা বেনিফিট সাবস্ক্রিপশন (যেমন Visual Studio Enterprise Subscription) ব্যবহার করছেন অথবা দ্রুত ফাইন-টিউন ও ডিপ্লয়মেন্ট প্রক্রিয়া পরীক্ষা করতে চান, তাদের জন্য এই টিউটোরিয়ালে CPU ব্যবহার করে ছোট ডেটাসেট দিয়ে ফাইন-টিউনের নির্দেশনাও দেওয়া হয়েছে। তবে লক্ষ্য রাখতে হবে, বড় ডেটাসেট এবং GPU ব্যবহার করলে ফাইন-টিউনের ফলাফল অনেক ভালো হয়।

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. *Standard NCADSA100v4 Family* কোটা অনুরোধ করতে নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Quota** নির্বাচন করুন।
    - ব্যবহার করার জন্য **Virtual machine family** নির্বাচন করুন। উদাহরণস্বরূপ, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** নির্বাচন করুন, যা *Standard_NC24ads_A100_v4* GPU অন্তর্ভুক্ত।
    - নেভিগেশন মেনু থেকে **Request quota** নির্বাচন করুন।

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab8348515fcfba9d0279114f04065df8bd6fb78e3d3704e627545.bn.png)

    - Request quota পৃষ্ঠায়, আপনি যে **New cores limit** ব্যবহার করতে চান তা লিখুন। উদাহরণস্বরূপ, ২৪।
    - Request quota পৃষ্ঠায়, GPU কোটা অনুরোধ করতে **Submit** নির্বাচন করুন।

> [!NOTE]
> আপনার প্রয়োজন অনুযায়ী GPU বা CPU নির্বাচন করতে [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) ডকুমেন্টটি দেখতে পারেন।

### রোল অ্যাসাইনমেন্ট যোগ করুন

আপনার মডেল ফাইন-টিউন এবং ডিপ্লয় করার জন্য, প্রথমে একটি User Assigned Managed Identity (UAI) তৈরি করতে হবে এবং তাকে যথাযথ অনুমতি দিতে হবে। এই UAI ডিপ্লয়মেন্টের সময় অথেনটিকেশনের জন্য ব্যবহৃত হবে।

#### User Assigned Managed Identity (UAI) তৈরি করুন

1. পোর্টালের উপরের **search bar**-এ *managed identities* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Managed Identities** নির্বাচন করুন।

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8a95d6e7762f1b087275a9634677f0a4e355717550ace3c02.bn.png)

1. **+ Create** নির্বাচন করুন।

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a8c70af922bf28a573c0744fb642f8228d62214b010a070d9.bn.png)

1. নিম্নলিখিত কাজগুলো করুন:

    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - আপনি যে **Region** ব্যবহার করতে চান তা নির্বাচন করুন।
    - **Name** লিখুন। এটি অবশ্যই ইউনিক হতে হবে।

1. **Review + create** নির্বাচন করুন।

1. **+ Create** নির্বাচন করুন।

#### Managed Identity-তে Contributor রোল অ্যাসাইনমেন্ট যোগ করুন

1. আপনি যে Managed Identity তৈরি করেছেন সেটিতে যান।

1. বাম পাশের ট্যাব থেকে **Azure role assignments** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+Add role assignment** নির্বাচন করুন।

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:
    - **Scope** হিসেবে **Resource group** নির্বাচন করুন।
    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহার করার জন্য **Resource group** নির্বাচন করুন।
    - **Role** হিসেবে **Contributor** নির্বাচন করুন।

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e008e224cf336687c04c9fe24740e47e34ce041b50b47e0ed1.bn.png)

1. **Save** নির্বাচন করুন।

#### Managed Identity-তে Storage Blob Data Reader রোল অ্যাসাইনমেন্ট যোগ করুন

1. পোর্টালের উপরের **search bar**-এ *storage accounts* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage accounts** নির্বাচন করুন।

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49bcd9cce3ffd1b6218afb6e5c3700b628da7b7c294be71b911.bn.png)

1. Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত স্টোরেজ অ্যাকাউন্ট নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephistorage*।

1. Add role assignment পৃষ্ঠায় যাওয়ার জন্য নিম্নলিখিত কাজগুলো করুন:

    - আপনি যে Azure Storage অ্যাকাউন্ট তৈরি করেছেন সেখানে যান।
    - বাম পাশের ট্যাব থেকে **Access Control (IAM)** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **+ Add** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **Add role assignment** নির্বাচন করুন।

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0ae84790d65dc5726a9b57c496d916b8700d41e0b3b468451.bn.png)

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:

    - Role পৃষ্ঠায়, **search bar**-এ *Storage Blob Data Reader* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage Blob Data Reader** নির্বাচন করুন।
    - Role পৃষ্ঠায়, **Next** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **Assign access to** হিসেবে **Managed identity** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **+ Select members** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনার Azure **Subscription** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, **Managed identity** হিসেবে **Manage Identity** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনি যে Managed Identity তৈরি করেছেন তা নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephi-managedidentity*।
    - Select managed identities পৃষ্ঠায়, **Select** নির্বাচন করুন।

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df788963e1dc0a68c39ee297363aabe979b487c60b3037662f.bn.png)

1. **Review + assign** নির্বাচন করুন।

#### Managed Identity-তে AcrPull রোল অ্যাসাইনমেন্ট যোগ করুন

1. পোর্টালের উপরের **search bar**-এ *container registries* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Container registries** নির্বাচন করুন।

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c64c0f778633c652ce08e4ac28f142a17afc10de81bb8c336.bn.png)

1. Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত container registry নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephicontainerregistries*।

1. Add role assignment পৃষ্ঠায় যাওয়ার জন্য নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Access Control (IAM)** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **+ Add** নির্বাচন করুন।
    - নেভিগেশন মেনু থেকে **Add role assignment** নির্বাচন করুন।

1. Add role assignment পৃষ্ঠায় নিম্নলিখিত কাজগুলো করুন:

    - Role পৃষ্ঠায়, **search bar**-এ *AcrPull* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **AcrPull** নির্বাচন করুন।
    - Role পৃষ্ঠায়, **Next** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **Assign access to** হিসেবে **Managed identity** নির্বাচন করুন।
    - Members পৃষ্ঠায়, **+ Select members** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনার Azure **Subscription** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, **Managed identity** হিসেবে **Manage Identity** নির্বাচন করুন।
    - Select managed identities পৃষ্ঠায়, আপনি যে Managed Identity তৈরি করেছেন তা নির্বাচন করুন। উদাহরণস্বরূপ, *finetunephi-managedidentity*।
    - Select managed identities পৃষ্ঠায়, **Select** নির্বাচন করুন।
    - **Review + assign** নির্বাচন করুন।

### প্রজেক্ট সেটআপ করুন

এখন, আপনি একটি ফোল্ডার তৈরি করবেন যেখানে কাজ করবেন এবং একটি ভার্চুয়াল এনভায়রনমেন্ট সেটআপ করবেন, যা ব্যবহারকারীদের সাথে ইন্টারঅ্যাক্ট করে এবং Azure Cosmos DB থেকে সংরক্ষিত চ্যাট ইতিহাস ব্যবহার করে উত্তর তৈরি করবে।

#### কাজ করার জন্য একটি ফোল্ডার তৈরি করুন

1. একটি টার্মিনাল উইন্ডো খুলুন এবং ডিফল্ট পাথে *finetune-phi* নামে একটি ফোল্ডার তৈরি করতে নিচের কমান্ডটি টাইপ করুন।

    ```console
    mkdir finetune-phi
    ```

1. টার্মিনালে নিচের কমান্ডটি টাইপ করে তৈরি করা *finetune-phi* ফোল্ডারে যান।

    ```console
    cd finetune-phi
    ```

#### ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

1. টার্মিনালে নিচের কমান্ডটি টাইপ করে *.venv* নামে একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন।

    ```console
    python -m venv .venv
    ```

1. টার্মিনালে নিচের কমান্ডটি টাইপ করে ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন।

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> যদি এটি সফল হয়, তাহলে কমান্ড প্রম্পটের আগে *(.venv)* দেখতে পাবেন।
#### প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

1. প্রয়োজনীয় প্যাকেজ ইনস্টল করতে টার্মিনালে নিচের কমান্ডগুলো টাইপ করুন।

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### প্রজেক্ট ফাইল তৈরি করুন

এই অনুশীলনে, আপনি আমাদের প্রজেক্টের জন্য প্রয়োজনীয় ফাইলগুলো তৈরি করবেন। এই ফাইলগুলোর মধ্যে রয়েছে ডেটাসেট ডাউনলোড করার স্ক্রিপ্ট, Azure Machine Learning পরিবেশ সেটআপ, Phi-3 মডেল ফাইন-টিউনিং, এবং ফাইন-টিউন করা মডেল ডিপ্লয়মেন্টের স্ক্রিপ্ট। এছাড়াও, আপনি ফাইন-টিউনিং পরিবেশ সেটআপের জন্য একটি *conda.yml* ফাইল তৈরি করবেন।

এই অনুশীলনে আপনি:

- ডেটাসেট ডাউনলোড করার জন্য *download_dataset.py* ফাইল তৈরি করবেন।
- Azure Machine Learning পরিবেশ সেটআপের জন্য *setup_ml.py* ফাইল তৈরি করবেন।
- *finetuning_dir* ফোল্ডারে *fine_tune.py* ফাইল তৈরি করবেন, যা ডেটাসেট ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করবে।
- ফাইন-টিউনিং পরিবেশ সেটআপের জন্য *conda.yml* ফাইল তৈরি করবেন।
- ফাইন-টিউন করা মডেল ডিপ্লয় করার জন্য *deploy_model.py* ফাইল তৈরি করবেন।
- ফাইন-টিউন করা মডেলকে Prompt flow এর মাধ্যমে ইন্টিগ্রেট এবং চালানোর জন্য *integrate_with_promptflow.py* ফাইল তৈরি করবেন।
- Prompt flow এর ওয়ার্কফ্লো স্ট্রাকচার সেটআপের জন্য *flow.dag.yml* ফাইল তৈরি করবেন।
- Azure তথ্য প্রবেশ করানোর জন্য *config.py* ফাইল তৈরি করবেন।

> [!NOTE]
>
> সম্পূর্ণ ফোল্ডার স্ট্রাকচার:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. **Visual Studio Code** খুলুন।

1. মেনুবার থেকে **File** নির্বাচন করুন।

1. **Open Folder** নির্বাচন করুন।

1. আপনি যে *finetune-phi* ফোল্ডার তৈরি করেছেন, সেটি নির্বাচন করুন, যা *C:\Users\yourUserName\finetune-phi* এ অবস্থিত।

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639c12e7da258ac8b3deca260786edb07598e206725cd1593ce.bn.png)

1. Visual Studio Code এর বাম প্যানেলে রাইট-ক্লিক করে **New File** নির্বাচন করে *download_dataset.py* নামে একটি নতুন ফাইল তৈরি করুন।

1. একইভাবে *setup_ml.py* নামে একটি নতুন ফাইল তৈরি করুন।

1. একইভাবে *deploy_model.py* নামে একটি নতুন ফাইল তৈরি করুন।

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a398766a39eac9f15240a9a4da566bd8dca86f471e78eadc69e.bn.png)

1. Visual Studio Code এর বাম প্যানেলে রাইট-ক্লিক করে **New Folder** নির্বাচন করে *finetuning_dir* নামে একটি নতুন ফোল্ডার তৈরি করুন।

1. *finetuning_dir* ফোল্ডারে *fine_tune.py* নামে একটি নতুন ফাইল তৈরি করুন।

#### *conda.yml* ফাইল তৈরি ও কনফিগার করুন

1. Visual Studio Code এর বাম প্যানেলে রাইট-ক্লিক করে **New File** নির্বাচন করে *conda.yml* নামে একটি নতুন ফাইল তৈরি করুন।

1. *conda.yml* ফাইলে নিচের কোড যোগ করুন, যা Phi-3 মডেলের ফাইন-টিউনিং পরিবেশ সেটআপ করবে।

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### *config.py* ফাইল তৈরি ও কনফিগার করুন

1. Visual Studio Code এর বাম প্যানেলে রাইট-ক্লিক করে **New File** নির্বাচন করে *config.py* নামে একটি নতুন ফাইল তৈরি করুন।

1. *config.py* ফাইলে আপনার Azure তথ্য যোগ করতে নিচের কোডটি লিখুন।

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Azure পরিবেশ ভেরিয়েবল যোগ করুন

1. Azure Subscription ID যোগ করতে নিচের ধাপগুলো অনুসরণ করুন:

    - পোর্টাল পেজের উপরের **search bar** এ *subscriptions* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Subscriptions** নির্বাচন করুন।
    - আপনি যে Azure Subscription ব্যবহার করছেন তা নির্বাচন করুন।
    - আপনার Subscription ID কপি করে *config.py* ফাইলে পেস্ট করুন।

    ![Find subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637e01163bfdd2a606e7d06f05455ab56e05cb5107e938e7a90.bn.png)

1. Azure Workspace Name যোগ করতে:

    - আপনি যে Azure Machine Learning রিসোর্স তৈরি করেছেন সেখানে যান।
    - আপনার অ্যাকাউন্টের নাম কপি করে *config.py* ফাইলে পেস্ট করুন।

    ![Find Azure Machine Learning name.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a702b1bb5e9d8e9f5e5424abe066a0ff310da980582e65721f.bn.png)

1. Azure Resource Group Name যোগ করতে:

    - Azure Machine Learning রিসোর্সে যান।
    - আপনার Azure Resource Group Name কপি করে *config.py* ফাইলে পেস্ট করুন।

    ![Find resource group name.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a399243d7c94d5aabd86070ab6535d3cf2ec38c78538626666.bn.png)

2. Azure Managed Identity নাম যোগ করতে:

    - আপনি যে Managed Identities রিসোর্স তৈরি করেছেন সেখানে যান।
    - আপনার Azure Managed Identity নাম কপি করে *config.py* ফাইলে পেস্ট করুন।

    ![Find UAI.](../../../../../../translated_images/01-17-find-uai.3529464f534998271ea7c5aebafa887051567417f3b4244ff58fdd443192b6d7.bn.png)

### ফাইন-টিউনিংয়ের জন্য ডেটাসেট প্রস্তুত করুন

এই অনুশীলনে, আপনি *download_dataset.py* ফাইল চালিয়ে *ULTRACHAT_200k* ডেটাসেট আপনার লোকাল পরিবেশে ডাউনলোড করবেন। এরপর এই ডেটাসেট ব্যবহার করে Azure Machine Learning এ Phi-3 মডেল ফাইন-টিউন করবেন।

#### *download_dataset.py* ব্যবহার করে ডেটাসেট ডাউনলোড করুন

1. Visual Studio Code এ *download_dataset.py* ফাইল খুলুন।

1. *download_dataset.py* ফাইলে নিচের কোড যোগ করুন।

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

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
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **কম ডেটাসেট ব্যবহার করে CPU দিয়ে ফাইন-টিউনিং করার নির্দেশনা**
>
> যদি আপনি CPU ব্যবহার করে ফাইন-টিউন করতে চান, তবে এই পদ্ধতিটি উপযুক্ত যারা বেনিফিট সাবস্ক্রিপশন (যেমন Visual Studio Enterprise Subscription) ব্যবহার করেন অথবা দ্রুত ফাইন-টিউনিং ও ডিপ্লয়মেন্ট পরীক্ষা করতে চান।
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` এর পরিবর্তে ব্যবহার করুন `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. টার্মিনালে নিচের কমান্ড টাইপ করে স্ক্রিপ্ট চালান এবং ডেটাসেট লোকাল পরিবেশে ডাউনলোড করুন।

    ```console
    python download_data.py
    ```

1. নিশ্চিত করুন যে ডেটাসেট সফলভাবে আপনার লোকাল *finetune-phi/data* ডিরেক্টরিতে সেভ হয়েছে।

> [!NOTE]
>
> **ডেটাসেটের আকার এবং ফাইন-টিউনিং সময়**
>
> এই E2E স্যাম্পলে, আপনি ডেটাসেটের মাত্র ১% (`train_sft[:1%]`) ব্যবহার করছেন। এটি ডেটার পরিমাণ অনেক কমিয়ে দেয়, ফলে আপলোড এবং ফাইন-টিউনিং উভয় প্রক্রিয়া দ্রুত হয়। আপনি আপনার প্রয়োজন অনুযায়ী শতাংশ পরিবর্তন করে ট্রেনিং সময় এবং মডেল পারফরম্যান্সের মধ্যে সঠিক ভারসাম্য খুঁজে পেতে পারেন। ছোট ডেটাসেট ব্যবহার করলে ফাইন-টিউনিংয়ের সময় কমে যায়, যা E2E স্যাম্পলের জন্য সুবিধাজনক।

## দৃশ্যপট ২: Phi-3 মডেল ফাইন-টিউন এবং Azure Machine Learning Studio তে ডিপ্লয় করুন

### Azure CLI সেটআপ করুন

আপনার পরিবেশকে অথেন্টিকেট করার জন্য Azure CLI সেটআপ করতে হবে। Azure CLI আপনাকে কমান্ড লাইন থেকে সরাসরি Azure রিসোর্স ম্যানেজ করার সুযোগ দেয় এবং Azure Machine Learning এর জন্য প্রয়োজনীয় ক্রেডেনশিয়াল সরবরাহ করে। শুরু করতে [Azure CLI ইনস্টল করুন](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. একটি টার্মিনাল উইন্ডো খুলুন এবং Azure অ্যাকাউন্টে লগইন করতে নিচের কমান্ড টাইপ করুন।

    ```console
    az login
    ```

1. আপনার Azure অ্যাকাউন্ট নির্বাচন করুন।

1. আপনার Azure সাবস্ক্রিপশন নির্বাচন করুন।

    ![Find resource group name.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a8792c687d36e4fc4f4ee37fd76640e6e4e5aed3329513f2328.bn.png)

> [!TIP]
>
> যদি Azure-তে সাইন ইন করতে সমস্যা হয়, তাহলে ডিভাইস কোড ব্যবহার করে চেষ্টা করুন। একটি টার্মিনাল উইন্ডো খুলুন এবং Azure অ্যাকাউন্টে সাইন ইন করতে নিচের কমান্ডটি টাইপ করুন:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 মডেল ফাইন-টিউন করুন

এই অনুশীলনে, আপনি প্রদত্ত ডেটাসেট ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করবেন। প্রথমে *fine_tune.py* ফাইলে ফাইন-টিউনিং প্রক্রিয়া সংজ্ঞায়িত করবেন। এরপর *setup_ml.py* ফাইল চালিয়ে Azure Machine Learning পরিবেশ কনফিগার এবং ফাইন-টিউনিং শুরু করবেন। এই স্ক্রিপ্টটি নিশ্চিত করে যে ফাইন-টিউনিং Azure Machine Learning পরিবেশে হবে।

*setup_ml.py* চালিয়ে আপনি Azure Machine Learning পরিবেশে ফাইন-টিউনিং প্রক্রিয়া শুরু করবেন।

#### *fine_tune.py* ফাইলে কোড যোগ করুন

1. *finetuning_dir* ফোল্ডারে যান এবং Visual Studio Code এ *fine_tune.py* ফাইল খুলুন।

1. *fine_tune.py* ফাইলে নিচের কোড যোগ করুন।

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. ফাইলটি সেভ করে বন্ধ করুন।

> [!TIP]
> **Phi-3.5 মডেল ফাইন-টিউন করতে পারেন**
>
> *fine_tune.py* ফাইলে `pretrained_model_name` এর মান `"microsoft/Phi-3-mini-4k-instruct"` থেকে আপনার পছন্দমত মডেলে পরিবর্তন করতে পারেন। উদাহরণস্বরূপ, যদি আপনি `"microsoft/Phi-3.5-mini-instruct"` ব্যবহার করেন, তাহলে Phi-3.5-mini-instruct মডেল ফাইন-টিউন হবে। আপনার পছন্দের মডেল নাম খুঁজে পেতে [Hugging Face](https://huggingface.co/) এ যান, মডেল সার্চ করুন এবং নাম কপি করে `pretrained_model_name` ফিল্ডে পেস্ট করুন।
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### *setup_ml.py* ফাইলে কোড যোগ করুন

1. Visual Studio Code এ *setup_ml.py* ফাইল খুলুন।

1. *setup_ml.py* ফাইলে নিচের কোড যোগ করুন।

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, এবং `LOCATION` আপনার নির্দিষ্ট তথ্য দিয়ে প্রতিস্থাপন করুন।

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **কম ডেটাসেট ব্যবহার করে CPU দিয়ে ফাইন-টিউনিং করার নির্দেশনা**
>
> যদি CPU ব্যবহার করে ফাইন-টিউন করতে চান, তবে এই পদ্ধতিটি উপযুক্ত যারা বেনিফিট সাবস্ক্রিপশন (যেমন Visual Studio Enterprise Subscription) ব্যবহার করেন অথবা দ্রুত ফাইন-টিউনিং ও ডিপ্লয়মেন্ট পরীক্ষা করতে চান।
>
> 1. *setup_ml* ফাইল খুলুন।
> 2. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, এবং `DOCKER_IMAGE_NAME` নিচের মতো প্রতিস্থাপন করুন। যদি আপনার *Standard_E16s_v3* অ্যাক্সেস না থাকে, তাহলে সমতুল্য CPU ইনস্ট্যান্স ব্যবহার করুন অথবা নতুন কোটা অনুরোধ করুন।
> 3. `LOCATION` আপনার নির্দিষ্ট তথ্য দিয়ে প্রতিস্থাপন করুন।
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. *setup_ml.py* স্ক্রিপ্ট চালাতে নিচের কমান্ড টাইপ করুন এবং Azure Machine Learning এ ফাইন-টিউনিং শুরু করুন।

    ```python
    python setup_ml.py
    ```

1. এই অনুশীলনে, আপনি সফলভাবে Azure Machine Learning ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করেছেন। *setup_ml.py* স্ক্রিপ্ট চালিয়ে আপনি Azure Machine Learning পরিবেশ সেটআপ এবং *fine_tune.py* ফাইলে সংজ্ঞায়িত ফাইন-টিউনিং প্রক্রিয়া শুরু করেছেন। ফাইন-টিউনিং প্রক্রিয়া সম্পন্ন হতে কিছু সময় লাগতে পারে। `python setup_ml.py` কমান্ড চালানোর পর প্রক্রিয়া শেষ হওয়া পর্যন্ত অপেক্ষা করুন। টার্মিনালে প্রদত্ত লিঙ্ক থেকে Azure Machine Learning পোর্টালে গিয়ে ফাইন-টিউনিং জবের অবস্থা মনিটর করতে পারেন।

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871ee8ba32fa508cc4018c0f04e51ad14b95c421ad77151f768f.bn.png)

### ফাইন-টিউন করা মডেল ডিপ্লয় করুন

ফাইন-টিউন করা Phi-3 মডেলকে Prompt Flow এর সাথে ইন্টিগ্রেট করতে, মডেলটি রিয়েল-টাইম ইনফারেন্সের জন্য অ্যাক্সেসযোগ্য করতে হবে। এই প্রক্রিয়ায় মডেল রেজিস্টার করা, অনলাইন এন্ডপয়েন্ট তৈরি করা এবং মডেল ডিপ্লয় করা অন্তর্ভুক্ত।

#### ডিপ্লয়মেন্টের জন্য মডেল নাম, এন্ডপয়েন্ট নাম, এবং ডিপ্লয়মেন্ট নাম সেট করুন

1. *config.py* ফাইল খুলুন।

1. `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` এর পরিবর্তে আপনার মডেলের পছন্দমত নাম দিন।

1. `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` এর পরিবর্তে আপনার এন্ডপয়েন্টের পছন্দমত নাম দিন।

1. `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` এর পরিবর্তে আপনার ডিপ্লয়মেন্টের পছন্দমত নাম দিন।

#### *deploy_model.py* ফাইলে কোড যোগ করুন

*deploy_model.py* ফাইল চালালে পুরো ডিপ্লয়মেন্ট প্রক্রিয়া স্বয়ংক্রিয়ভাবে সম্পন্ন হয়। এটি মডেল রেজিস্টার করে, এন্ডপয়েন্ট তৈরি করে এবং *config.py* ফাইলে নির্ধারিত সেটিংস অনুযায়ী ডিপ্লয়মেন্ট সম্পাদন করে, যার মধ্যে মডেল নাম, এন্ডপয়েন্ট নাম এবং ডিপ্লয়মেন্ট নাম অন্তর্ভুক্ত।

1. Visual Studio Code এ *deploy_model.py* ফাইল খুলুন।

1. *deploy_model.py* ফাইলে নিচের কোড যোগ করুন।

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. `JOB_NAME` পেতে নিচের ধাপগুলো অনুসরণ করুন:

    - আপনি যে Azure Machine Learning রিসোর্স তৈরি করেছেন সেখানে যান।
    - **Studio web URL** নির্বাচন করে Azure Machine Learning ওয়ার্কস্পেস খুলুন।
    - বাম পাশের ট্যাব থেকে **Jobs** নির্বাচন করুন।
    - ফাইন-টিউনিং এর জন্য যে এক্সপেরিমেন্ট তৈরি করেছেন তা নির্বাচন করুন, যেমন *finetunephi*।
    - আপনি যে জব তৈরি করেছেন তা নির্বাচন করুন।
- আপনার কাজের নাম `JOB_NAME = "your-job-name"` এ *deploy_model.py* ফাইলে কপি করে পেস্ট করুন।

1. `COMPUTE_INSTANCE_TYPE` আপনার নির্দিষ্ট তথ্য দিয়ে প্রতিস্থাপন করুন।

1. Azure Machine Learning-এ ডিপ্লয়মেন্ট প্রক্রিয়া শুরু করতে *deploy_model.py* স্ক্রিপ্ট চালানোর জন্য নিচের কমান্ডটি টাইপ করুন।

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> আপনার অ্যাকাউন্টে অতিরিক্ত চার্জ এড়াতে, Azure Machine Learning ওয়ার্কস্পেসে তৈরি করা এন্ডপয়েন্টটি মুছে ফেলতে ভুলবেন না।
>

#### Azure Machine Learning ওয়ার্কস্পেসে ডিপ্লয়মেন্টের অবস্থা পরীক্ষা করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেস তৈরি করেছেন সেখানে যান।

1. Azure Machine Learning ওয়ার্কস্পেস খুলতে **Studio web URL** নির্বাচন করুন।

1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff109f3b7a6b6e4e9689f99b2d7bf021b057f6c0ecbd1ba90c0.bn.png)

2. আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4b726505fcfb7d262b0510de029dcbaf36422bb75b77f25dd.bn.png)

3. এই পৃষ্ঠায়, আপনি ডিপ্লয়মেন্ট প্রক্রিয়ার সময় তৈরি করা এন্ডপয়েন্টগুলি পরিচালনা করতে পারবেন।

## দৃশ্যপট ৩: Prompt flow-এর সাথে ইন্টিগ্রেট করুন এবং আপনার কাস্টম মডেলের সাথে চ্যাট করুন

### কাস্টম Phi-3 মডেল Prompt flow-এর সাথে ইন্টিগ্রেট করুন

আপনার ফাইন-টিউন করা মডেল সফলভাবে ডিপ্লয় করার পর, এখন আপনি এটি Prompt flow-এর সাথে ইন্টিগ্রেট করতে পারেন, যাতে আপনার মডেলটি রিয়েল-টাইম অ্যাপ্লিকেশনগুলোতে ব্যবহার করা যায় এবং আপনার কাস্টম Phi-3 মডেলের সাথে বিভিন্ন ইন্টারেক্টিভ কাজ করা সম্ভব হয়।

#### ফাইন-টিউন করা Phi-3 মডেলের api key এবং endpoint uri সেট করুন

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেস তৈরি করেছেন সেখানে যান।
1. বাম পাশের ট্যাব থেকে **Endpoints** নির্বাচন করুন।
1. আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।
1. নেভিগেশন মেনু থেকে **Consume** নির্বাচন করুন।
1. আপনার **REST endpoint** কপি করে *config.py* ফাইলে `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` এর জায়গায় পেস্ট করুন।
1. আপনার **Primary key** কপি করে *config.py* ফাইলে `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` এর জায়গায় পেস্ট করুন।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53bf44401e184f65a0a088daa76a65f5df5eb4489ae40b890f6.bn.png)

#### *flow.dag.yml* ফাইলে কোড যোগ করুন

1. Visual Studio Code-এ *flow.dag.yml* ফাইলটি খুলুন।

1. *flow.dag.yml* ফাইলে নিচের কোডটি যোগ করুন।

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

#### *integrate_with_promptflow.py* ফাইলে কোড যোগ করুন

1. Visual Studio Code-এ *integrate_with_promptflow.py* ফাইলটি খুলুন।

1. *integrate_with_promptflow.py* ফাইলে নিচের কোডটি যোগ করুন।

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### আপনার কাস্টম মডেলের সাথে চ্যাট করুন

1. Azure Machine Learning-এ ডিপ্লয়মেন্ট প্রক্রিয়া শুরু করতে *deploy_model.py* স্ক্রিপ্ট চালানোর জন্য নিচের কমান্ডটি টাইপ করুন।

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. ফলাফলের একটি উদাহরণ এখানে দেওয়া হলো: এখন আপনি আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করতে পারবেন। ফাইন-টিউনিংয়ের জন্য ব্যবহৃত ডেটার ভিত্তিতে প্রশ্ন করা সুপারিশ করা হয়।

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6412447c9786c562be969a8c3b19791eadffce725fa84f014.bn.png)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।