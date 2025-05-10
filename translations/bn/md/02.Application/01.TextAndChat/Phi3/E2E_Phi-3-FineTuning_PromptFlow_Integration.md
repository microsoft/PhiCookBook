<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:19:56+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "bn"
}
-->
# Fine-tune এবং Prompt flow এর সাথে কাস্টম Phi-3 মডেল ইন্টিগ্রেট করুন

এই end-to-end (E2E) স্যাম্পলটি Microsoft Tech Community থেকে "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" গাইডের উপর ভিত্তি করে। এটি fine-tuning, deploy এবং Prompt flow এর সাথে কাস্টম Phi-3 মডেল ইন্টিগ্রেট করার প্রক্রিয়াগুলো পরিচয় করিয়ে দেয়।

## ওভারভিউ

এই E2E স্যাম্পলে, আপনি শিখবেন কিভাবে Phi-3 মডেল fine-tune করতে হয় এবং Prompt flow এর সাথে ইন্টিগ্রেট করতে হয়। Azure Machine Learning এবং Prompt flow ব্যবহার করে আপনি একটি ওয়ার্কফ্লো স্থাপন করবেন কাস্টম AI মডেল ডিপ্লয় এবং ব্যবহার করার জন্য। এই E2E স্যাম্পলটি তিনটি সিনারিওতে ভাগ করা হয়েছে:

**সিনারিও ১: Azure রিসোর্স সেটআপ এবং fine-tuning এর প্রস্তুতি**

**সিনারিও ২: Phi-3 মডেল fine-tune এবং Azure Machine Learning Studio তে ডিপ্লয়**

**সিনারিও ৩: Prompt flow এর সাথে ইন্টিগ্রেট এবং আপনার কাস্টম মডেলের সাথে চ্যাট করুন**

এখানে এই E2E স্যাম্পলের একটি ওভারভিউ দেওয়া হলো।

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.bn.png)

### বিষয়সূচি

1. **[সিনারিও ১: Azure রিসোর্স সেটআপ এবং fine-tuning এর প্রস্তুতি](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription এ GPU কোটা রিকোয়েস্ট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [রোল অ্যাসাইনমেন্ট যোগ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [প্রজেক্ট সেটআপ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [fine-tuning এর জন্য ডেটাসেট প্রস্তুত করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[সিনারিও ২: Phi-3 মডেল fine-tune এবং Azure Machine Learning Studio তে ডিপ্লয়](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI সেটআপ করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 মডেল fine-tune করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [fine-tuned মডেল ডিপ্লয় করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[সিনারিও ৩: Prompt flow এর সাথে ইন্টিগ্রেট এবং আপনার কাস্টম মডেলের সাথে চ্যাট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [কাস্টম Phi-3 মডেল Prompt flow এর সাথে ইন্টিগ্রেট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [আপনার কাস্টম মডেলের সাথে চ্যাট করুন](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## সিনারিও ১: Azure রিসোর্স সেটআপ এবং fine-tuning এর প্রস্তুতি

### Azure Machine Learning ওয়ার্কস্পেস তৈরি করুন

1. পোর্টাল পেজের উপরের **search bar** এ *azure machine learning* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Azure Machine Learning** সিলেক্ট করুন।

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.bn.png)

1. নেভিগেশন মেনু থেকে **+ Create** সিলেক্ট করুন।

1. নেভিগেশন মেনু থেকে **New workspace** সিলেক্ট করুন।

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.bn.png)

1. নিম্নলিখিত কাজগুলো সম্পাদন করুন:

    - আপনার Azure **Subscription** সিলেক্ট করুন।
    - ব্যবহার করার জন্য **Resource group** সিলেক্ট করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - **Workspace Name** দিন। এটি অবশ্যই ইউনিক হতে হবে।
    - আপনি যেই **Region** ব্যবহার করতে চান তা সিলেক্ট করুন।
    - ব্যবহার করার জন্য **Storage account** সিলেক্ট করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহার করার জন্য **Key vault** সিলেক্ট করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহার করার জন্য **Application insights** সিলেক্ট করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - ব্যবহার করার জন্য **Container registry** সিলেক্ট করুন (প্রয়োজনে নতুন তৈরি করুন)।

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.bn.png)

1. **Review + Create** সিলেক্ট করুন।

1. **Create** সিলেক্ট করুন।

### Azure Subscription এ GPU কোটা রিকোয়েস্ট করুন

এই E2E স্যাম্পলে, আপনি fine-tuning এর জন্য *Standard_NC24ads_A100_v4 GPU* ব্যবহার করবেন, যার জন্য কোটা রিকোয়েস্ট প্রয়োজন, এবং ডিপ্লয়ের জন্য *Standard_E4s_v3* CPU ব্যবহার করবেন, যার জন্য কোটা রিকোয়েস্টের দরকার নেই।

> [!NOTE]
>
> শুধুমাত্র Pay-As-You-Go সাবস্ক্রিপশন (স্ট্যান্ডার্ড সাবস্ক্রিপশন টাইপ) GPU বরাদ্দের জন্য যোগ্য; benefit সাবস্ক্রিপশনগুলো বর্তমানে সমর্থিত নয়।
>
> যারা benefit সাবস্ক্রিপশন (যেমন Visual Studio Enterprise Subscription) ব্যবহার করছেন অথবা দ্রুত fine-tuning ও ডিপ্লয়মেন্ট প্রক্রিয়া পরীক্ষা করতে চান, তাদের জন্য এই টিউটোরিয়াল CPU ব্যবহার করে ছোট ডেটাসেট নিয়ে fine-tuning করার নির্দেশনাও দেয়। তবে, বড় ডেটাসেট এবং GPU ব্যবহার করলে fine-tuning ফলাফল অনেক ভালো হয়।

1. যান [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)।

1. *Standard NCADSA100v4 Family* কোটা রিকোয়েস্ট করতে নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Quota** সিলেক্ট করুন।
    - ব্যবহার করার জন্য **Virtual machine family** সিলেক্ট করুন। উদাহরণস্বরূপ, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** সিলেক্ট করুন, যা *Standard_NC24ads_A100_v4* GPU অন্তর্ভুক্ত।
    - নেভিগেশন মেনু থেকে **Request quota** সিলেক্ট করুন।

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.bn.png)

    - Request quota পেজে, আপনি যে **New cores limit** চান তা লিখুন। উদাহরণস্বরূপ, ২৪।
    - Request quota পেজে, GPU কোটা রিকোয়েস্ট করার জন্য **Submit** সিলেক্ট করুন।

> [!NOTE]
> আপনার প্রয়োজন অনুযায়ী GPU বা CPU সিলেক্ট করতে [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) ডকুমেন্টেশন দেখুন।

### রোল অ্যাসাইনমেন্ট যোগ করুন

আপনার মডেল fine-tune এবং ডিপ্লয় করার জন্য, প্রথমে একটি User Assigned Managed Identity (UAI) তৈরি করতে হবে এবং এটি যথাযথ পারমিশন দিতে হবে। এই UAI ডিপ্লয়ের সময় authentication এর জন্য ব্যবহার হবে।

#### User Assigned Managed Identity (UAI) তৈরি করুন

1. পোর্টাল পেজের উপরের **search bar** এ *managed identities* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Managed Identities** সিলেক্ট করুন।

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.bn.png)

1. **+ Create** সিলেক্ট করুন।

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.bn.png)

1. নিম্নলিখিত কাজগুলো করুন:

    - আপনার Azure **Subscription** সিলেক্ট করুন।
    - ব্যবহার করার জন্য **Resource group** সিলেক্ট করুন (প্রয়োজনে নতুন তৈরি করুন)।
    - আপনি যে **Region** ব্যবহার করতে চান তা সিলেক্ট করুন।
    - **Name** দিন। এটি অবশ্যই ইউনিক হতে হবে।

1. **Review + create** সিলেক্ট করুন।

1. **+ Create** সিলেক্ট করুন।

#### Managed Identity তে Contributor রোল অ্যাসাইনমেন্ট যোগ করুন

1. আপনি যে Managed Identity তৈরি করেছেন সেখানে যান।

1. বাম পাশের ট্যাব থেকে **Azure role assignments** সিলেক্ট করুন।

1. নেভিগেশন মেনু থেকে **+Add role assignment** সিলেক্ট করুন।

1. Add role assignment পেজে নিম্নলিখিত কাজগুলো করুন:
    - **Scope** হিসেবে **Resource group** সিলেক্ট করুন।
    - আপনার Azure **Subscription** সিলেক্ট করুন।
    - ব্যবহার করার জন্য **Resource group** সিলেক্ট করুন।
    - **Role** হিসেবে **Contributor** সিলেক্ট করুন।

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.bn.png)

1. **Save** সিলেক্ট করুন।

#### Managed Identity তে Storage Blob Data Reader রোল অ্যাসাইনমেন্ট যোগ করুন

1. পোর্টাল পেজের উপরের **search bar** এ *storage accounts* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage accounts** সিলেক্ট করুন।

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.bn.png)

1. Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত Storage account সিলেক্ট করুন। উদাহরণস্বরূপ, *finetunephistorage*।

1. Add role assignment পেজে যাওয়ার জন্য নিম্নলিখিত কাজগুলো করুন:

    - আপনি যে Azure Storage account তৈরি করেছেন সেখানে যান।
    - বাম পাশের ট্যাব থেকে **Access Control (IAM)** সিলেক্ট করুন।
    - নেভিগেশন মেনু থেকে **+ Add** সিলেক্ট করুন।
    - নেভিগেশন মেনু থেকে **Add role assignment** সিলেক্ট করুন।

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.bn.png)

1. Add role assignment পেজে নিম্নলিখিত কাজগুলো করুন:

    - Role পেজে, **search bar** এ *Storage Blob Data Reader* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Storage Blob Data Reader** সিলেক্ট করুন।
    - Role পেজে, **Next** সিলেক্ট করুন।
    - Members পেজে, **Assign access to** হিসেবে **Managed identity** সিলেক্ট করুন।
    - Members পেজে, **+ Select members** সিলেক্ট করুন।
    - Select managed identities পেজে, আপনার Azure **Subscription** সিলেক্ট করুন।
    - Select managed identities পেজে, **Managed identity** হিসেবে **Manage Identity** সিলেক্ট করুন।
    - Select managed identities পেজে, আপনি যে Managed Identity তৈরি করেছেন তা সিলেক্ট করুন। উদাহরণস্বরূপ, *finetunephi-managedidentity*।
    - Select managed identities পেজে, **Select** সিলেক্ট করুন।

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.bn.png)

1. **Review + assign** সিলেক্ট করুন।

#### Managed Identity তে AcrPull রোল অ্যাসাইনমেন্ট যোগ করুন

1. পোর্টাল পেজের উপরের **search bar** এ *container registries* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **Container registries** সিলেক্ট করুন।

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.bn.png)

1. Azure Machine Learning ওয়ার্কস্পেসের সাথে যুক্ত Container registry সিলেক্ট করুন। উদাহরণস্বরূপ, *finetunephicontainerregistries*

1. Add role assignment পেজে যাওয়ার জন্য নিম্নলিখিত কাজগুলো করুন:

    - বাম পাশের ট্যাব থেকে **Access Control (IAM)** সিলেক্ট করুন।
    - নেভিগেশন মেনু থেকে **+ Add** সিলেক্ট করুন।
    - নেভিগেশন মেনু থেকে **Add role assignment** সিলেক্ট করুন।

1. Add role assignment পেজে নিম্নলিখিত কাজগুলো করুন:

    - Role পেজে, **search bar** এ *AcrPull* টাইপ করুন এবং প্রদর্শিত অপশন থেকে **AcrPull** সিলেক্ট করুন।
    - Role পেজে, **Next** সিলেক্ট করুন।
    - Members পেজে, **Assign access to** হিসেবে **Managed identity** সিলেক্ট করুন।
    - Members পেজে, **+ Select members** সিলেক্ট করুন।
    - Select managed identities পেজে, আপনার Azure **Subscription** সিলেক্ট করুন।
    - Select managed identities পেজে, **Managed identity** হিসেবে **Manage Identity** সিলেক্ট করুন।
    - Select managed identities পেজে, আপনি যে Managed Identity তৈরি করেছেন তা সিলেক্ট করুন। উদাহরণস্বরূপ, *finetunephi-managedidentity*।
    - Select managed identities পেজে, **Select** সিলেক্ট করুন।
    - **Review + assign** সিলেক্ট করুন।

### প্রজেক্ট সেটআপ করুন

এখন, আপনি একটি ফোল্ডার তৈরি করবেন যেখানে কাজ করবেন এবং একটি ভার্চুয়াল এনভায়রনমেন্ট সেটআপ করবেন, যা ইউজারদের সাথে ইন্টারঅ্যাক্ট করে এবং Azure Cosmos DB থেকে সংরক্ষিত চ্যাট হিস্ট্রি ব্যবহার করে উত্তর তৈরি করবে।

#### কাজ করার জন্য একটি ফোল্ডার তৈরি করুন

1. একটি টার্মিনাল উইন্ডো খুলুন এবং ডিফল্ট পাথে *finetune-phi* নামে একটি ফোল্ডার তৈরি করতে নিচের কমান্ডটি টাইপ করুন।

    ```console
    mkdir finetune-phi
    ```

1. আপনার টার্মিনালে নিচের কমান্ডটি টাইপ করে তৈরি করা *finetune-phi* ফোল্ডারে যান।

    ```console
    cd finetune-phi
    ```

#### ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

1. আপনার টার্মিনালে নিচের কমান্ডটি টাইপ করে *.venv* নামে একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন।

    ```console
    python -m venv .venv
    ```

1. আপনার টার্মিনালে নিচের কমান্ডটি টাইপ করে ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> যদি সফল হয়, তাহলে কমান্ড প্রম্পটের আগে *(.venv)* দেখা যাবে।

#### প্রয়োজনীয় প্যাকেজগুলো ইনস্টল করুন

1. প্রয়োজনীয় প্যাকেজগুলো ইনস্টল করতে নিচের কমান্ডগুলো আপনার টার্মিনালে টাইপ করুন।

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### প্রজেক্ট ফাইল তৈরি করুন

এই অনুশীলনে, আপনি আমাদের প্রজেক্টের জন্য প্রয়োজনীয় ফাইলগুলো তৈরি করবেন। এই ফাইলগুলো ডেটাসেট ডাউনলোড, Azure Machine Learning এনভায়রনমেন্ট সেটআপ, Phi-3 মডেল fine-tune এবং fine-tuned মডেল ডিপ্লয়ের স্ক্রিপ্ট অন্তর্ভুক্ত করবে। এছাড়া fine-tuning এনভায়রনমেন্ট সেটআপ করার জন্য একটি *conda.yml* ফাইলও তৈরি করবেন।

এই অনুশীলনে আপনি:

- ডেটাসেট ডাউনলোড করার জন্য *download_dataset.py* ফাইল তৈরি করবেন।
- Azure Machine Learning এনভায়রনমেন্ট সেটআপ করার জন্য *setup_ml.py* ফাইল তৈরি করবেন।
- *finetuning_dir* ফোল্ডারে *fine_tune.py* ফাইল তৈরি করে ডেটাসেট ব্যবহার করে Phi-3 মডেল fine-tune করবেন।
- fine-tuning এনভায়রনমেন্ট সেটআপ করার জন্য *conda.yml* ফাইল তৈরি করবেন।
- fine-tuned মডেল ডিপ্লয়ের জন্য *deploy_model.py* ফাইল তৈরি করবেন।
- fine-tuned মডেল ইন্টিগ্রেট এবং Prompt flow ব্যবহার করে মডেল চালানোর জন্য *integrate_with_promptflow.py* ফাইল তৈরি করবেন।
- Prompt flow এর ওয়ার্কফ্লো স্ট্রাকচার সেটআপ করার জন্য *flow.dag.yml* ফাইল তৈরি করবেন।
- Azure তথ্য প্রবেশ করার জন্য *config.py* ফাইল তৈরি করবেন।

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

1. **Visual Studio Code** ওপেন করুন।

1. মেনুবার থেকে **File** সিলেক্ট করুন।

1. **Open Folder** সিলেক্ট করুন।

1. আপনি যে *finetune-phi* ফোল্ডার তৈরি করেছেন তা সিলেক্ট করুন, যা *C:\Users\yourUserName\finetune-phi* লোকেশনে অবস্থিত।

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.bn.png)

1. Visual Studio Code এর বাম পেনেলে রাইট-ক্লিক করে **New File** সিলেক্ট করে *download_dataset.py* নামে একটি নতুন ফাইল তৈরি করুন।

1. Visual Studio Code এর বাম পেনেলে রাইট-ক্লিক করে **
![সাবস্ক্রিপশন আইডি খুঁজুন।](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.bn.png)

1. Azure ওয়ার্কস্পেস নাম যোগ করতে নিম্নলিখিত কাজগুলো করুন:

    - আপনি যে Azure Machine Learning রিসোর্সটি তৈরি করেছেন সেখানে যান।
    - আপনার অ্যাকাউন্ট নাম *config.py* ফাইলে কপি করে পেস্ট করুন।

    ![Azure Machine Learning নাম খুঁজুন।](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.bn.png)

1. Azure Resource Group নাম যোগ করতে নিম্নলিখিত কাজগুলো করুন:

    - আপনি যে Azure Machine Learning রিসোর্সটি তৈরি করেছেন সেখানে যান।
    - আপনার Azure Resource Group নাম *config.py* ফাইলে কপি করে পেস্ট করুন।

    ![রিসোর্স গ্রুপ নাম খুঁজুন।](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.bn.png)

2. Azure Managed Identity নাম যোগ করতে নিম্নলিখিত কাজগুলো করুন:

    - আপনি যে Managed Identities রিসোর্সটি তৈরি করেছেন সেখানে যান।
    - আপনার Azure Managed Identity নাম *config.py* ফাইলে কপি করে পেস্ট করুন।

    ![UAI খুঁজুন।](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.bn.png)

### ফাইন-টিউনিংয়ের জন্য ডেটাসেট প্রস্তুত করুন

এই অনুশীলনে, আপনি *download_dataset.py* ফাইলটি চালিয়ে *ULTRACHAT_200k* ডেটাসেটগুলো আপনার লোকাল পরিবেশে ডাউনলোড করবেন। এরপর এই ডেটাসেটগুলো ব্যবহার করে Azure Machine Learning-এ Phi-3 মডেল ফাইন-টিউন করবেন।

#### *download_dataset.py* ব্যবহার করে আপনার ডেটাসেট ডাউনলোড করুন

1. Visual Studio Code-এ *download_dataset.py* ফাইলটি খুলুন।

1. *download_dataset.py* ফাইলে নিম্নলিখিত কোড যোগ করুন।

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
> **কম ডেটাসেট ব্যবহার করে CPU দিয়ে ফাইন-টিউনিং করার নির্দেশনা**
>
> যদি আপনি CPU ব্যবহার করে ফাইন-টিউন করতে চান, তবে এই পদ্ধতিটি সুবিধাজনক সাবস্ক্রিপশন (যেমন Visual Studio Enterprise Subscription) থাকা ব্যবহারকারীদের জন্য বা দ্রুত ফাইন-টিউনিং ও ডিপ্লয়মেন্ট প্রক্রিয়া পরীক্ষা করার জন্য উপযুক্ত।
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')` দ্বারা প্রতিস্থাপন করুন।
>

1. টার্মিনালে নিচের কমান্ডটি টাইপ করে স্ক্রিপ্টটি চালান এবং ডেটাসেটটি আপনার লোকাল পরিবেশে ডাউনলোড করুন।

    ```console
    python download_data.py
    ```

1. নিশ্চিত করুন যে ডেটাসেটগুলো সফলভাবে আপনার লোকাল *finetune-phi/data* ডিরেক্টরিতে সংরক্ষিত হয়েছে।

> [!NOTE]
>
> **ডেটাসেটের আকার এবং ফাইন-টিউনিং সময়**
>
> এই E2E নমুনায়, আপনি ডেটাসেটের মাত্র ১% (`train_sft[:1%]`) ব্যবহার করছেন। এটি ডেটার পরিমাণ অনেক কমিয়ে দেয়, ফলে আপলোড এবং ফাইন-টিউনিং প্রক্রিয়া দ্রুত হয়। আপনি প্রশিক্ষণের সময় এবং মডেলের কার্যকারিতার মধ্যে সঠিক ভারসাম্য খুঁজে পেতে শতাংশ পরিবর্তন করতে পারেন। ছোট ডেটাসেট ব্যবহার করলে ফাইন-টিউনিংয়ের সময় কমে, যা E2E নমুনার জন্য সুবিধাজনক।
>

## দৃশ্যপট ২: Phi-3 মডেল ফাইন-টিউন এবং Azure Machine Learning Studio-তে ডিপ্লয় করুন

### Azure CLI সেটআপ করুন

আপনার পরিবেশে প্রমাণীকরণের জন্য Azure CLI সেটআপ করতে হবে। Azure CLI কমান্ড লাইন থেকে সরাসরি Azure রিসোর্স ম্যানেজ করার সুযোগ দেয় এবং Azure Machine Learning-কে এই রিসোর্সে অ্যাক্সেসের জন্য প্রয়োজনীয় ক্রেডেনশিয়াল সরবরাহ করে। শুরু করতে [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) ইনস্টল করুন।

1. একটি টার্মিনাল উইন্ডো খুলুন এবং আপনার Azure অ্যাকাউন্টে লগইন করতে নিচের কমান্ডটি টাইপ করুন।

    ```console
    az login
    ```

1. ব্যবহার করতে আপনার Azure অ্যাকাউন্ট নির্বাচন করুন।

1. ব্যবহার করতে আপনার Azure সাবস্ক্রিপশন নির্বাচন করুন।

    ![রিসোর্স গ্রুপ নাম খুঁজুন।](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.bn.png)

> [!TIP]
>
> যদি Azure-তে সাইন ইন করতে সমস্যা হয়, তাহলে ডিভাইস কোড ব্যবহার করে চেষ্টা করুন। একটি টার্মিনাল উইন্ডো খুলুন এবং Azure অ্যাকাউন্টে সাইন ইন করতে নিচের কমান্ডটি টাইপ করুন:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 মডেল ফাইন-টিউন করুন

এই অনুশীলনে, আপনি প্রদত্ত ডেটাসেট ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করবেন। প্রথমে *fine_tune.py* ফাইলে ফাইন-টিউনিং প্রক্রিয়া নির্ধারণ করবেন। এরপর Azure Machine Learning পরিবেশ কনফিগার করে *setup_ml.py* ফাইল চালিয়ে ফাইন-টিউনিং শুরু করবেন। এই স্ক্রিপ্ট নিশ্চিত করে যে ফাইন-টিউনিং Azure Machine Learning পরিবেশে হয়।

*setup_ml.py* চালিয়ে আপনি Azure Machine Learning পরিবেশে ফাইন-টিউনিং প্রক্রিয়া চালাবেন।

#### *fine_tune.py* ফাইলে কোড যোগ করুন

1. *finetuning_dir* ফোল্ডারে যান এবং Visual Studio Code-এ *fine_tune.py* ফাইলটি খুলুন।

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

1. *fine_tune.py* ফাইলটি সেভ করে বন্ধ করুন।

> [!TIP]
> **Phi-3.5 মডেলও ফাইন-টিউন করতে পারেন**
>
> *fine_tune.py* ফাইলে, `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` ক্ষেত্রটি আপনার স্ক্রিপ্টে পরিবর্তন করতে পারেন।
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 ফাইন-টিউন।":::
>

#### *setup_ml.py* ফাইলে কোড যোগ করুন

1. Visual Studio Code-এ *setup_ml.py* ফাইলটি খুলুন।

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

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` আপনার নির্দিষ্ট তথ্য দিয়ে প্রতিস্থাপন করুন।

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **কম ডেটাসেট ব্যবহার করে CPU দিয়ে ফাইন-টিউনিং করার নির্দেশনা**
>
> যদি CPU দিয়ে ফাইন-টিউন করতে চান, তাহলে এই পদ্ধতিটি সুবিধাজনক সাবস্ক্রিপশন (যেমন Visual Studio Enterprise Subscription) থাকা ব্যবহারকারীদের জন্য বা দ্রুত ফাইন-টিউনিং ও ডিপ্লয়মেন্ট পরীক্ষা করার জন্য উপযুক্ত।
>
> 1. *setup_ml* ফাইলটি খুলুন।
> 1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` আপনার নির্দিষ্ট তথ্য দিয়ে প্রতিস্থাপন করুন।
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Azure Machine Learning-এ ফাইন-টিউনিং শুরু করতে *setup_ml.py* স্ক্রিপ্টটি চালাতে নিচের কমান্ডটি টাইপ করুন।

    ```python
    python setup_ml.py
    ```

1. এই অনুশীলনে, আপনি সফলভাবে Azure Machine Learning ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করেছেন। *setup_ml.py* স্ক্রিপ্ট চালিয়ে আপনি Azure Machine Learning পরিবেশ সেটআপ করেছেন এবং *fine_tune.py* ফাইলে নির্ধারিত ফাইন-টিউনিং প্রক্রিয়া শুরু করেছেন। দয়া করে মনে রাখবেন ফাইন-টিউনিং প্রক্রিয়াটি বেশ সময় নিতে পারে। `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.bn.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` কমান্ডটি আপনার ডিপ্লয়মেন্টের জন্য প্রয়োজনীয় নাম সহ চালান।

#### *deploy_model.py* ফাইলে কোড যোগ করুন

*deploy_model.py* ফাইল চালালে পুরো ডিপ্লয়মেন্ট প্রক্রিয়া স্বয়ংক্রিয় হয়। এটি মডেল রেজিস্টার করে, একটি এন্ডপয়েন্ট তৈরি করে, এবং config.py ফাইলে নির্ধারিত সেটিংস (মডেল নাম, এন্ডপয়েন্ট নাম, ডিপ্লয়মেন্ট নাম) অনুযায়ী ডিপ্লয়মেন্ট সম্পন্ন করে।

1. Visual Studio Code-এ *deploy_model.py* ফাইলটি খুলুন।

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

1. `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` আপনার নির্দিষ্ট তথ্য দিয়ে প্রতিস্থাপন করুন।

1. Azure Machine Learning-এ ডিপ্লয়মেন্ট শুরু করতে *deploy_model.py* স্ক্রিপ্টটি চালাতে নিচের কমান্ডটি টাইপ করুন।

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> আপনার অ্যাকাউন্টে অতিরিক্ত চার্জ এড়াতে, Azure Machine Learning ওয়ার্কস্পেসে তৈরি করা এন্ডপয়েন্টটি অবশ্যই মুছে ফেলুন।
>

#### Azure Machine Learning ওয়ার্কস্পেসে ডিপ্লয়মেন্টের অবস্থা পরীক্ষা করুন

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ যান।

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেসটি তৈরি করেছেন সেখানে যান।

1. Azure Machine Learning ওয়ার্কস্পেস খুলতে **Studio web URL** নির্বাচন করুন।

1. বাম দিকের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

    ![এন্ডপয়েন্ট নির্বাচন করুন।](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.bn.png)

2. আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।

    ![আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.bn.png)

3. এই পৃষ্ঠায় আপনি ডিপ্লয়মেন্ট প্রক্রিয়ায় তৈরি হওয়া এন্ডপয়েন্টগুলো পরিচালনা করতে পারবেন।

## দৃশ্যপট ৩: Prompt flow-এর সাথে ইন্টিগ্রেট করুন এবং আপনার কাস্টম মডেলের সাথে চ্যাট করুন

### কাস্টম Phi-3 মডেল Prompt flow-এর সাথে ইন্টিগ্রেট করুন

আপনার ফাইন-টিউন করা মডেল সফলভাবে ডিপ্লয় করার পর, আপনি এখন এটিকে Prompt flow-এর সাথে সংযুক্ত করতে পারেন যাতে রিয়েল-টাইম অ্যাপ্লিকেশনগুলোতে আপনার মডেল ব্যবহার করতে পারেন এবং বিভিন্ন ইন্টারেক্টিভ কাজ করতে পারেন আপনার কাস্টম Phi-3 মডেলের মাধ্যমে।

#### ফাইন-টিউন করা Phi-3 মডেলের API কী এবং এন্ডপয়েন্ট URI সেট করুন

1. আপনি যে Azure Machine Learning ওয়ার্কস্পেসটি তৈরি করেছেন সেখানে যান।
1. বাম দিকের ট্যাব থেকে **Endpoints** নির্বাচন করুন।
1. আপনি যে এন্ডপয়েন্ট তৈরি করেছেন তা নির্বাচন করুন।
1. নেভিগেশন মেনু থেকে **Consume** নির্বাচন করুন।
1. আপনার **REST endpoint** কপি করে *config.py* ফাইলে পেস্ট করুন, যেখানে `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` প্রতিস্থাপন করুন আপনার **Primary key** দিয়ে।

    ![API কী এবং এন্ডপয়েন্ট URI কপি করুন।](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.bn.png)

#### *flow.dag.yml* ফাইলে কোড যোগ করুন

1. Visual Studio Code-এ *flow.dag.yml* ফাইলটি খুলুন।

1. *flow.dag.yml* ফাইলে নিচের কোড যোগ করুন।

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

1. *integrate_with_promptflow.py* ফাইলে নিচের কোড যোগ করুন।

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

1. Azure Machine Learning-এ ডিপ্লয়মেন্ট শুরু করতে *deploy_model.py* স্ক্রিপ্টটি চালাতে নিচের কমান্ডটি টাইপ করুন।

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. এখানে একটি ফলাফলের উদাহরণ দেওয়া হলো: এখন আপনি আপনার কাস্টম Phi-3 মডেলের সাথে চ্যাট করতে পারেন। ফাইন-টিউনিংয়ের জন্য ব্যবহৃত ডেটার ওপর ভিত্তি করে প্রশ্ন করা উত্তম।

    ![Prompt flow উদাহরণ।](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.bn.png)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অশুদ্ধি থাকতে পারে। মূল নথিটি তার নিজ ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।