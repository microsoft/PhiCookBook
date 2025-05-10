<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T20:57:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "bn"
}
-->
## Azure ML সিস্টেম রেজিস্ট্রি থেকে chat-completion কম্পোনেন্ট ব্যবহার করে মডেল ফাইন-টিউন করা

এই উদাহরণে আমরা Phi-3-mini-4k-instruct মডেল ফাইন-টিউন করব যাতে ২ জনের মধ্যে কথোপকথন সম্পন্ন করা যায় ultrachat_200k ডেটাসেট ব্যবহার করে।

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.bn.png)

এই উদাহরণটি দেখাবে কিভাবে Azure ML SDK এবং Python ব্যবহার করে ফাইন-টিউন করা যায় এবং তারপর ফাইন-টিউন করা মডেলটি অনলাইন এন্ডপয়েন্টে ডিপ্লয় করে রিয়েল টাইম ইনফারেন্সের জন্য ব্যবহার করা যায়।

### ট্রেনিং ডেটা

আমরা ultrachat_200k ডেটাসেট ব্যবহার করব। এটি UltraChat ডেটাসেটের একটি কঠোরভাবে ফিল্টার করা সংস্করণ এবং Zephyr-7B-β, একটি আধুনিক 7b চ্যাট মডেল ট্রেন করার জন্য ব্যবহৃত হয়েছে।

### মডেল

আমরা Phi-3-mini-4k-instruct মডেল ব্যবহার করব দেখানোর জন্য কিভাবে একজন ব্যবহারকারী চ্যাট-কমপ্লিশন টাস্কের জন্য মডেল ফাইন-টিউন করতে পারে। যদি আপনি এই নোটবুকটি কোনো নির্দিষ্ট মডেল কার্ড থেকে খুলে থাকেন, তাহলে নির্দিষ্ট মডেলের নাম প্রতিস্থাপন করতে ভুলবেন না।

### কাজসমূহ

- ফাইন-টিউনের জন্য একটি মডেল নির্বাচন করুন।
- ট্রেনিং ডেটা নির্বাচন ও অনুসন্ধান করুন।
- ফাইন-টিউনিং কাজের কনফিগারেশন করুন।
- ফাইন-টিউনিং কাজ চালান।
- ট্রেনিং এবং ইভ্যালুয়েশন মেট্রিক্স পর্যালোচনা করুন।
- ফাইন-টিউন করা মডেল রেজিস্টার করুন।
- রিয়েল টাইম ইনফারেন্সের জন্য ফাইন-টিউন করা মডেল ডিপ্লয় করুন।
- রিসোর্সগুলো পরিষ্কার করুন।

## ১. প্রয়োজনীয়তা সেটআপ

- ডিপেন্ডেন্সি ইনস্টল করুন
- AzureML ওয়ার্কস্পেসের সাথে সংযোগ করুন। set up SDK authentication এ আরও জানুন। নিচে <WORKSPACE_NAME>, <RESOURCE_GROUP> এবং <SUBSCRIPTION_ID> প্রতিস্থাপন করুন।
- azureml সিস্টেম রেজিস্ট্রির সাথে সংযোগ করুন
- একটি ঐচ্ছিক এক্সপেরিমেন্ট নাম সেট করুন
- কম্পিউট চেক বা তৈরি করুন।

> [!NOTE]
> একটি একক GPU নোডে একাধিক GPU কার্ড থাকতে পারে। উদাহরণস্বরূপ, Standard_NC24rs_v3 এর একটি নোডে ৪টি NVIDIA V100 GPU থাকে, আর Standard_NC12s_v3 এ ২টি NVIDIA V100 GPU। এই তথ্যের জন্য ডকুমেন্টেশন দেখুন। নোড প্রতি GPU কার্ডের সংখ্যা নিচের param gpus_per_node এ সেট করা হয়। সঠিক মান সেট করলে নোডের সব GPU ব্যবহার নিশ্চিত হয়। সুপারিশকৃত GPU কম্পিউট SKUs এখানে এবং এখানে পাওয়া যাবে।

### Python লাইব্রেরি

নিচের সেল রান করে ডিপেন্ডেন্সি ইনস্টল করুন। নতুন পরিবেশে এটি একটি বাধ্যতামূলক ধাপ।

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML এর সাথে ইন্টারঅ্যাকশন

1. এই Python স্ক্রিপ্টটি Azure Machine Learning (Azure ML) সার্ভিসের সাথে ইন্টারঅ্যাক্ট করার জন্য ব্যবহৃত। এর কাজের সারাংশ:

    - azure.ai.ml, azure.identity, এবং azure.ai.ml.entities প্যাকেজ থেকে প্রয়োজনীয় মডিউলগুলো ইমপোর্ট করে। এছাড়া time মডিউলও ইমপোর্ট করে।

    - DefaultAzureCredential() ব্যবহার করে অথেনটিকেশন করার চেষ্টা করে, যা Azure ক্লাউডে দ্রুত ডেভেলপমেন্ট শুরু করার জন্য সরলীকৃত অথেনটিকেশন অভিজ্ঞতা দেয়। ব্যর্থ হলে InteractiveBrowserCredential() ব্যবহার করে ইন্টারঅ্যাকটিভ লগইন প্রম্পট দেখায়।

    - তারপর from_config মেথড ব্যবহার করে MLClient ইনস্ট্যান্স তৈরি করার চেষ্টা করে, যা ডিফল্ট কনফিগ ফাইল (config.json) থেকে কনফিগ পড়ে। ব্যর্থ হলে subscription_id, resource_group_name, এবং workspace_name ম্যানুয়ালি দিয়ে MLClient তৈরি করে।

    - Azure ML রেজিস্ট্রি "azureml" এর জন্য আরেকটি MLClient ইনস্ট্যান্স তৈরি করে। এই রেজিস্ট্রিতে মডেল, ফাইন-টিউনিং পাইপলাইন, এবং এনভায়রনমেন্ট থাকে।

    - experiment_name সেট করে "chat_completion_Phi-3-mini-4k-instruct"।

    - বর্তমান সময় থেকে একটি ইউনিক টাইমস্ট্যাম্প তৈরি করে, যা ইউনিক নাম এবং ভার্সন তৈরিতে ব্যবহৃত হবে।

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## ২. ফাইন-টিউনের জন্য একটি ফাউন্ডেশন মডেল নির্বাচন করুন

1. Phi-3-mini-4k-instruct হল ৩.৮ বিলিয়ন প্যারামিটার বিশিষ্ট, হালকা ও আধুনিক ওপেন মডেল যা Phi-2 এর জন্য ব্যবহৃত ডেটাসেটের ওপর নির্মিত। মডেলটি Phi-3 মডেল ফ্যামিলির অন্তর্ভুক্ত, এবং Mini ভার্সন ৪K ও ১২৮K (টোকেন হিসেবে) দুই ধরনের যা কনটেক্সট লেন্থ হিসেবে কাজ করে। আমাদের নির্দিষ্ট উদ্দেশ্যে ব্যবহার করার জন্য মডেলটি ফাইন-টিউন করতে হবে। আপনি AzureML স্টুডিওর মডেল ক্যাটালগে চ্যাট-কমপ্লিশন টাস্ক ফিল্টার করে এই মডেলগুলো ব্রাউজ করতে পারেন। এই উদাহরণে আমরা Phi-3-mini-4k-instruct মডেল ব্যবহার করছি। যদি আপনি অন্য মডেলের জন্য এই নোটবুকটি খুলে থাকেন, তাহলে মডেল নাম ও ভার্সন পরিবর্তন করুন।

    > [!NOTE]
    > মডেলের id প্রপার্টি ফাইন-টিউনিং জবের ইনপুট হিসেবে পাঠানো হবে। এটি AzureML স্টুডিও মডেল ক্যাটালগের মডেল ডিটেইল পেজের Asset ID ফিল্ডেও পাওয়া যায়।

2. এই Python স্ক্রিপ্টটি Azure Machine Learning (Azure ML) সার্ভিসের সাথে ইন্টারঅ্যাক্ট করছে। এর কাজের সারাংশ:

    - model_name সেট করে "Phi-3-mini-4k-instruct"।

    - registry_ml_client এর models প্রপার্টির get মেথড ব্যবহার করে নির্দিষ্ট নামের মডেলের সর্বশেষ ভার্সন Azure ML রেজিস্ট্রি থেকে নিয়ে আসে। get মেথড দুইটি আর্গুমেন্ট নেয়: মডেলের নাম এবং লেবেল যা সর্বশেষ ভার্সন নির্দেশ করে।

    - ফাইন-টিউনের জন্য ব্যবহৃত মডেলের নাম, ভার্সন এবং আইডি কনসোলে প্রিন্ট করে। string.format মেথড ব্যবহার করে এই তথ্য প্রবেশ করানো হয় foundation_model অবজেক্ট থেকে।

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## ৩. কাজের জন্য কম্পিউট তৈরি করুন

ফাইন-টিউন জব শুধুমাত্র GPU কম্পিউটের সাথে কাজ করে। কম্পিউটের সাইজ মডেলের আকারের ওপর নির্ভর করে এবং অনেক ক্ষেত্রে সঠিক কম্পিউট সাইজ নির্ধারণ করা কঠিন হয়। এই সেলে ব্যবহারকারীকে সঠিক কম্পিউট নির্বাচন করার নির্দেশনা দেয়া হয়েছে।

> [!NOTE]
> নিচের কম্পিউটগুলো সবচেয়ে অপ্টিমাইজড কনফিগারেশনে কাজ করে। কনফিগে কোনো পরিবর্তন করলে Cuda Out Of Memory এরর হতে পারে। এমন ক্ষেত্রে বড় কম্পিউট সাইজে আপগ্রেড করার চেষ্টা করুন।

> [!NOTE]
> compute_cluster_size নির্বাচন করার সময় নিশ্চিত করুন কম্পিউট আপনার রিসোর্স গ্রুপে উপলব্ধ। যদি না থাকে, কম্পিউট রিসোর্সে অ্যাক্সেসের জন্য অনুরোধ করতে পারেন।

### ফাইন-টিউন সাপোর্টের জন্য মডেল চেক করা

1. এই Python স্ক্রিপ্টটি Azure ML মডেলের সাথে ইন্টারঅ্যাক্ট করছে। এর কাজের সারাংশ:

    - ast মডিউল ইমপোর্ট করে, যা পাইথনের অ্যাবস্ট্রাক্ট সিনট্যাক্স ট্রি প্রক্রিয়াকরণের ফাংশন দেয়।

    - foundation_model অবজেক্টে finetune_compute_allow_list নামে ট্যাগ আছে কিনা চেক করে। Azure ML এ ট্যাগ হলো কী-ভ্যালু জোড়া যা মডেল ফিল্টার ও সাজানোর জন্য ব্যবহৃত হয়।

    - যদি finetune_compute_allow_list ট্যাগ থাকে, তাহলে ast.literal_eval দিয়ে ট্যাগের মান (স্ট্রিং) নিরাপদে পাইথন লিস্টে রূপান্তর করে computes_allow_list এ অ্যাসাইন করে। তারপর একটি মেসেজ প্রিন্ট করে বলে যে কম্পিউট তালিকা থেকে নির্বাচন করা উচিত।

    - ট্যাগ না থাকলে computes_allow_list কে None সেট করে এবং মডেলের ট্যাগে finetune_compute_allow_list নেই বলে মেসেজ দেয়।

    - সারমর্মে, স্ক্রিপ্টটি মডেলের মেটাডাটায় একটি নির্দিষ্ট ট্যাগ খুঁজে বের করে, সেটি থাকলে তার মান লিস্টে রূপান্তর করে এবং ব্যবহারকারীকে তথ্য দেয়।

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Compute Instance চেক করা

1. এই Python স্ক্রিপ্টটি Azure ML সার্ভিসের সাথে ইন্টারঅ্যাক্ট করে একটি কম্পিউট ইনস্ট্যান্সের বিভিন্ন চেক করে। এর কাজের সারাংশ:

    - compute_cluster নামের কম্পিউট ইনস্ট্যান্সটি ওয়ার্কস্পেস থেকে নিয়ে আসার চেষ্টা করে। যদি প্রোভিশনিং স্টেট "failed" হয়, তাহলে ValueError ছুঁড়ে।

    - যদি computes_allow_list None না হয়, তাহলে তালিকার সব কম্পিউট সাইজকে lowercase এ রূপান্তর করে চেক করে বর্তমান কম্পিউট সাইজ তালিকায় আছে কিনা। না থাকলে ValueError ছুঁড়ে।

    - যদি computes_allow_list None হয়, তাহলে কম্পিউট সাইজটি unsupported GPU VM সাইজের তালিকায় আছে কিনা চেক করে। থাকলে ValueError ছুঁড়ে।

    - ওয়ার্কস্পেসের সব উপলব্ধ কম্পিউট সাইজের তালিকা নিয়ে প্রতিটি সাইজের নাম বর্তমান কম্পিউট সাইজের সাথে মিলিয়ে GPU এর সংখ্যা বের করে gpu_count_found সেট করে।

    - gpu_count_found সত্য হলে কম্পিউট ইনস্ট্যান্সের GPU সংখ্যা প্রিন্ট করে, না হলে ValueError ছুঁড়ে।

    - সারমর্মে, স্ক্রিপ্টটি একটি Azure ML ওয়ার্কস্পেসের কম্পিউট ইনস্ট্যান্সের প্রোভিশনিং স্টেট, সাইজ এবং GPU সংখ্যা পরীক্ষা করে।

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## ৪. মডেল ফাইন-টিউনের জন্য ডেটাসেট নির্বাচন করুন

1. আমরা ultrachat_200k ডেটাসেট ব্যবহার করব। ডেটাসেটে চারটি ভাগ আছে, যা Supervised fine-tuning (sft) এর জন্য উপযুক্ত। Generation ranking (gen)। প্রতিটি ভাগে উদাহরণ সংখ্যা নিচে দেখানো হয়েছে:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. পরবর্তী কয়েকটি সেল ফাইন-টিউনের জন্য ডেটা প্রস্তুতির মৌলিক ধাপ দেখায়:

### কিছু ডেটা রো ভিজুয়ালাইজ করুন

আমরা চাই এই স্যাম্পল দ্রুত রান করুক, তাই train_sft, test_sft ফাইলগুলোতে শুধুমাত্র ৫% পূর্বে ট্রিম করা রো রাখা হয়েছে। এর ফলে ফাইন-টিউন করা মডেলের সঠিকতা কম হবে, তাই বাস্তব ব্যবহারে ব্যবহার না করাই ভালো। download-dataset.py স্ক্রিপ্ট ultrachat_200k ডেটাসেট ডাউনলোড এবং ফাইনটিউন পাইপলাইন কম্পোনেন্টের জন্য ডেটা রূপান্তর করার জন্য ব্যবহৃত। ডেটাসেট বড় হওয়ায় এখানে শুধুমাত্র এর একটি অংশ আছে।

1. নিচের স্ক্রিপ্টটি মাত্র ৫% ডেটা ডাউনলোড করে। dataset_split_pc প্যারামিটার পরিবর্তন করে এটি বাড়ানো যাবে।

    > [!NOTE]
    > কিছু ভাষা মডেলের ভাষা কোড আলাদা, তাই ডেটাসেটের কলাম নামগুলোও সেই অনুযায়ী হওয়া উচিত।

1. ডেটার একটি উদাহরণ নিচে দেওয়া হলো  
চ্যাট-কমপ্লিশন ডেটাসেট পারকেট ফরম্যাটে সংরক্ষিত, যেখানে প্রতিটি এন্ট্রি নিচের স্কিমা অনুসরণ করে:

    - এটি একটি JSON (JavaScript Object Notation) ডকুমেন্ট, যা জনপ্রিয় ডেটা বিনিময় ফরম্যাট। এটি এক্সিকিউটেবল কোড নয়, ডেটা সংরক্ষণ ও পরিবহনের উপায়। এর গঠন:

    - "prompt": একটি স্ট্রিং যা AI সহকারীকে দেওয়া টাস্ক বা প্রশ্ন নির্দেশ করে।

    - "messages": অবজেক্টের অ্যারে। প্রতিটি অবজেক্ট একটি কথোপকথনের মেসেজ, যেখানে ব্যবহারকারী ও AI সহকারী অংশগ্রহণ করে। প্রতিটি মেসেজ অবজেক্টের দুটি কী:

    - "content": মেসেজের বিষয়বস্তু স্ট্রিং।
    - "role": মেসেজ প্রেরকের ভূমিকা, যেমন "user" বা "assistant"।
    - "prompt_id": প্রম্পটের ইউনিক আইডেন্টিফায়ার স্ট্রিং।

1. এই JSON ডকুমেন্টে একটি কথোপকথন দেখানো হয়েছে যেখানে ব্যবহারকারী AI সহকারীকে একটি ডিস্টোপিয়ান গল্পের প্রধান চরিত্র তৈরি করতে বলে। সহকারী উত্তর দেয়, পরে ব্যবহারকারী আরও বিস্তারিত জানতে চায়। সহকারী সম্মত হয়। পুরো কথোপকথন একটি নির্দিষ্ট প্রম্পট আইডির সাথে যুক্ত।

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### ডেটা ডাউনলোড করা

1. এই Python স্ক্রিপ্টটি download-dataset.py নামক হেল্পার স্ক্রিপ্ট ব্যবহার করে ডেটাসেট ডাউনলোড করে। এর কাজের সারাংশ:

    - os মডিউল ইমপোর্ট করে, যা অপারেটিং সিস্টেম নির্ভর কার্যক্রমের জন্য ব্যবহৃত।

    - os.system ফাংশন ব্যবহার করে শেলে download-dataset.py স্ক্রিপ্ট রান করে, আর্গুমেন্ট হিসেবে ডেটাসেটের নাম (HuggingFaceH4/ultrachat_200k), ডাউনলোড ডিরেক্টরি (ultrachat_200k_dataset), এবং ডেটাসেটের ভাগের শতাংশ (5) দেয়। os.system কমান্ডের এক্সিট স্ট্যাটাস রিটার্ন করে যা exit_status এ রাখা হয়।

    - exit_status 0 না হলে, অর্থাৎ কমান্ড ব্যর্থ হলে, Exception ছুঁড়ে ডেটাসেট ডাউনলোডে ত্রুটি হয়েছে বলে।

    - সারমর্মে, স্ক্রিপ্টটি হেল্পার স্ক্রিপ্ট ব্যবহার করে ডেটাসেট ডাউনলোড করে এবং ব্যর্থ হলে ত্রুটি দেখায়।

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### ডেটা DataFrame এ লোড করা

1. এই Python স্ক্রিপ্টটি একটি JSON Lines ফাইল pandas DataFrame এ লোড করে এবং প্রথম ৫টি রো প্রদর্শন করে। এর কাজের সারাংশ:

    - pandas লাইব্রেরি ইমপোর্ট করে, যা শক্তিশালী ডেটা ম্যানিপুলেশন ও বিশ্লেষণের জন্য ব্যবহৃত।

    - pandas এর ডিসপ্লে অপশনে সর্বোচ্চ কলাম প্রস্থ ০ সেট করে, যার মানে পুরো টেক্সট ট্রাঙ্কেশন ছাড়াই দেখা যাবে।

    - pd.read_json ফাংশন ব্যবহার করে ultrachat_200k_dataset ডিরেক্টরির train_sft.jsonl ফাইল লোড করে DataFrame এ। lines=True মানে ফাইলটি JSON Lines ফরম্যাটে।

    - head মেথড দিয়ে প্রথম ৫টি রো দেখায়। রো কম হলে সব দেখানো হয়।

    - সারমর্মে, স্ক্রিপ্টটি JSON Lines ফাইল DataFrame এ লোড করে পূর্ণ কলাম টেক্সট সহ প্রথম ৫টি রো প্রদর্শন করে।

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## ৫. মডেল এবং ডেটা ইনপুট হিসেবে ব্যবহার করে ফাইন-টিউনিং জব সাবমিট করুন

চ্যাট-কমপ্লিশন পাইপলাইন কম্পোনেন্ট ব্যবহার করে জব তৈরি করুন। ফাইন-টিউনের জন্য সমর্থিত সব প্যারামিটার সম্পর্কে আরও জানুন।

### ফাইনটিউন প্যারামিটার নির্ধারণ

1. ফাইনটিউন প্যারামিটার দুইটি বিভাগে ভাগ করা যায় - ট্রেনিং প্যারামিটার, অপ্টিমাইজেশন প্যারামিটার

1. ট্রেনিং প্যারামিটার ট্রেনিংয়ের দিকনির্দেশনা দেয় যেমন -

    - কোন optimizer, scheduler ব্যবহার হবে
    - কোন মেট্রিক অপ্টিমাইজ করা হবে
    - ট্রেনিং স্টেপ ও ব্যাচ সাইজ ইত্যাদি
    - অপ্টিমাইজেশন প্যারামিটার GPU মেমোরি অপ্টিমাইজ এবং কম্পিউট রিসোর্স কার্যকর ব্যবহারে সাহায্য করে।

1. নিচে কয়েকটি অপ্টিমাইজেশন প্যারামিটার দেওয়া হলো। মডেলভেদে এগুলো ভিন্ন হতে পারে এবং মডেলের সাথে প্যাকেজ করা থাকে।

    - deepspeed এবং LoRA সক্রিয় করা
    - মিক্সড প্রিসিশন ট্রেনিং চালু করা
    - মাল্টি-নোড ট্রেনিং চালু করা

> [!NOTE]
> Supervised finetuning এর ফলে alignment হারানো বা catastrophic forgetting ঘটতে পারে। তাই ফাইনটিউনের পর alignment স্টেজ চালানোর পরামর্শ দেওয়া হয়।

### ফাইন টিউনিং প্যারামিটার

1. এই Python স্ক্রিপ্টটি মেশিন লার্নিং ম
training pipeline বিভিন্ন প্যারামিটারের উপর ভিত্তি করে তৈরি করা হচ্ছে, এবং তারপর এই display name প্রিন্ট করা হচ্ছে। ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Pipeline কনফিগার করা

এই Python স্ক্রিপ্টটি Azure Machine Learning SDK ব্যবহার করে একটি মেশিন লার্নিং পাইপলাইন ডিফাইন এবং কনফিগার করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

1. এটি Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলো ইমপোর্ট করে।

1. এটি রেজিস্ট্রি থেকে "chat_completion_pipeline" নামের একটি পাইপলাইন কম্পোনেন্ট নিয়ে আসে।

1. এটি `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False` ব্যবহার করে একটি পাইপলাইন জব ডিফাইন করে, যার মানে হলো যদি কোনো স্টেপ ব্যর্থ হয় তাহলে পুরো পাইপলাইন বন্ধ হয়ে যাবে।

1. সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning SDK ব্যবহার করে একটি চ্যাট কমপ্লিশন টাস্কের জন্য মেশিন লার্নিং পাইপলাইন ডিফাইন এবং কনফিগার করছে।

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### জব সাবমিট করা

1. এই Python স্ক্রিপ্টটি একটি মেশিন লার্নিং পাইপলাইন জব Azure Machine Learning ওয়ার্কস্পেসে সাবমিট করছে এবং তারপর জবটি সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি workspace_ml_client এর jobs অবজেক্টের create_or_update মেথড কল করে পাইপলাইন জব সাবমিট করে। চালানোর জন্য পাইপলাইন pipeline_object দ্বারা নির্দিষ্ট, এবং যে এক্সপেরিমেন্টের অধীনে জবটি চলবে তা experiment_name দ্বারা নির্ধারিত।

- এরপর এটি jobs অবজেক্টের stream মেথড কল করে পাইপলাইন জব শেষ হওয়া পর্যন্ত অপেক্ষা করে। অপেক্ষার জন্য নির্দিষ্ট জবের নাম pipeline_job অবজেক্টের name অ্যাট্রিবিউট থেকে নেয়া হয়।

- সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning ওয়ার্কস্পেসে একটি মেশিন লার্নিং পাইপলাইন জব সাবমিট করছে এবং জবটি শেষ হওয়া পর্যন্ত অপেক্ষা করছে।

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## ৬. ফাইন টিউন করা মডেলটি ওয়ার্কস্পেসে রেজিস্টার করা

আমরা ফাইন টিউনিং জবের আউটপুট থেকে মডেলটি রেজিস্টার করব। এটি ফাইন টিউন করা মডেল এবং ফাইন টিউনিং জবের মধ্যে lineage ট্র্যাক করবে। ফাইন টিউনিং জবটি আরও ফাউন্ডেশন মডেল, ডেটা এবং ট্রেনিং কোডের lineage ট্র্যাক করে।

### ML মডেল রেজিস্টার করা

1. এই Python স্ক্রিপ্টটি Azure Machine Learning পাইপলাইনে ট্রেইন করা একটি মেশিন লার্নিং মডেল রেজিস্টার করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলো ইমপোর্ট করে।

- এটি pipeline job থেকে trained_model আউটপুট পাওয়া যাচ্ছে কিনা পরীক্ষা করে, workspace_ml_client এর jobs অবজেক্টের get মেথড কল করে এবং outputs অ্যাট্রিবিউট অ্যাক্সেস করে।

- এটি pipeline job এর নাম এবং আউটপুটের নাম ("trained_model") ব্যবহার করে ট্রেইন করা মডেলের পথ তৈরি করে।

- এটি মূল মডেলের নামের সাথে "-ultrachat-200k" যোগ করে এবং স্ল্যাশ থাকলে হাইফেন দিয়ে রিপ্লেস করে ফাইন-টিউন করা মডেলের নাম নির্ধারণ করে।

- এটি Model অবজেক্ট তৈরি করে মডেল রেজিস্টার করার জন্য প্রস্তুত হয়, যেখানে মডেলের পথ, মডেলের ধরন (MLflow মডেল), মডেলের নাম ও ভার্সন, এবং মডেলের বর্ণনা সহ বিভিন্ন প্যারামিটার থাকে।

- এটি workspace_ml_client এর models অবজেক্টের create_or_update মেথড কল করে Model অবজেক্ট পাস করে মডেলটি রেজিস্টার করে।

- এটি রেজিস্টার করা মডেলটি প্রিন্ট করে।

1. সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning পাইপলাইনে ট্রেইন করা একটি মেশিন লার্নিং মডেল রেজিস্টার করছে।

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## ৭. ফাইন টিউন করা মডেলটি অনলাইন এন্ডপয়েন্টে ডিপ্লয় করা

অনলাইন এন্ডপয়েন্ট একটি স্থায়ী REST API প্রদান করে যা মডেল ব্যবহার করতে চাওয়া অ্যাপ্লিকেশনগুলোর সাথে ইন্টিগ্রেশনের জন্য ব্যবহৃত হয়।

### এন্ডপয়েন্ট ম্যানেজ করা

1. এই Python স্ক্রিপ্টটি Azure Machine Learning এ একটি রেজিস্টার করা মডেলের জন্য একটি ম্যানেজড অনলাইন এন্ডপয়েন্ট তৈরি করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলো ইমপোর্ট করে।

- এটি "ultrachat-completion-" স্ট্রিংয়ের সাথে একটি টাইমস্ট্যাম্প যোগ করে অনলাইন এন্ডপয়েন্টের জন্য একটি ইউনিক নাম নির্ধারণ করে।

- এটি ManagedOnlineEndpoint অবজেক্ট তৈরি করে এন্ডপয়েন্ট তৈরি করার জন্য প্রস্তুত হয়, যেখানে এন্ডপয়েন্টের নাম, বর্ণনা এবং অথেন্টিকেশন মোড ("key") সহ বিভিন্ন প্যারামিটার থাকে।

- এটি workspace_ml_client এর begin_create_or_update মেথড কল করে ManagedOnlineEndpoint অবজেক্ট পাস করে এন্ডপয়েন্ট তৈরি করে এবং wait মেথড কল করে তৈরি হওয়ার অপেক্ষা করে।

1. সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning এ একটি রেজিস্টার করা মডেলের জন্য একটি ম্যানেজড অনলাইন এন্ডপয়েন্ট তৈরি করছে।

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> আপনি এখানে ডিপ্লয়মেন্টের জন্য সমর্থিত SKU এর তালিকা পাবেন - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML মডেল ডিপ্লয় করা

1. এই Python স্ক্রিপ্টটি Azure Machine Learning এ একটি রেজিস্টার করা মেশিন লার্নিং মডেল একটি ম্যানেজড অনলাইন এন্ডপয়েন্টে ডিপ্লয় করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি ast মডিউল ইমপোর্ট করে, যা Python এর অ্যাবস্ট্রাক্ট সিনট্যাক্স ট্রি প্রক্রিয়াকরণের জন্য ফাংশন সরবরাহ করে।

- এটি ডিপ্লয়মেন্টের জন্য ইনস্ট্যান্স টাইপ "Standard_NC6s_v3" সেট করে।

- এটি foundation মডেলে inference_compute_allow_list ট্যাগ আছে কিনা পরীক্ষা করে। থাকলে, ট্যাগের মানকে স্ট্রিং থেকে Python লিস্টে রূপান্তর করে এবং inference_computes_allow_list এ সেট করে। না থাকলে, এটি None সেট করে।

- এটি চেক করে নির্দিষ্ট ইনস্ট্যান্স টাইপটি allow list এ আছে কিনা। না থাকলে, ব্যবহারকারীকে allow list থেকে ইনস্ট্যান্স টাইপ বেছে নিতে বলার জন্য একটি মেসেজ প্রিন্ট করে।

- এটি ManagedOnlineDeployment অবজেক্ট তৈরি করে ডিপ্লয়মেন্টের জন্য প্রস্তুত হয়, যেখানে ডিপ্লয়মেন্টের নাম, এন্ডপয়েন্টের নাম, মডেলের আইডি, ইনস্ট্যান্স টাইপ ও সংখ্যা, লাইভনেস প্রোব সেটিংস, এবং রিকোয়েস্ট সেটিংস সহ বিভিন্ন প্যারামিটার থাকে।

- এটি workspace_ml_client এর begin_create_or_update মেথড কল করে ManagedOnlineDeployment অবজেক্ট পাস করে ডিপ্লয়মেন্ট তৈরি করে এবং wait মেথড কল করে তৈরি হওয়ার অপেক্ষা করে।

- এটি এন্ডপয়েন্টের ট্রাফিক ১০০% "demo" ডিপ্লয়মেন্টে নির্দেশ করে।

- এটি begin_create_or_update মেথড কল করে এন্ডপয়েন্ট আপডেট করে এবং result মেথড কল করে আপডেট সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করে।

1. সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning এ একটি রেজিস্টার করা মডেল একটি ম্যানেজড অনলাইন এন্ডপয়েন্টে ডিপ্লয় করছে।

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## ৮. স্যাম্পল ডেটা দিয়ে এন্ডপয়েন্ট পরীক্ষা করা

আমরা টেস্ট ডেটাসেট থেকে কিছু স্যাম্পল ডেটা নিয়ে অনলাইন এন্ডপয়েন্টে ইনফারেন্সের জন্য সাবমিট করব। তারপর স্কোর করা লেবেলগুলো আসল লেবেলের সাথে দেখাবো।

### ফলাফল পড়া

1. এই Python স্ক্রিপ্টটি একটি JSON Lines ফাইল pandas DataFrame এ পড়ছে, র্যান্ডম স্যাম্পল নিচ্ছে, এবং ইন্ডেক্স রিসেট করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি ./ultrachat_200k_dataset/test_gen.jsonl ফাইলটি pandas DataFrame এ পড়ছে। read_json ফাংশনে lines=True ব্যবহার করা হয়েছে কারণ ফাইলটি JSON Lines ফরম্যাটে, যেখানে প্রতিটি লাইন আলাদা JSON অবজেক্ট।

- এটি DataFrame থেকে ১টি র্যান্ডম সারি স্যাম্পল করছে। sample ফাংশনে n=1 ব্যবহার করা হয়েছে।

- এটি DataFrame এর ইন্ডেক্স রিসেট করছে। reset_index ফাংশনে drop=True ব্যবহার করে মূল ইন্ডেক্স বাদ দিয়ে নতুন ডিফল্ট ইন্টিজার ইন্ডেক্স তৈরি করছে।

- এটি head ফাংশন দিয়ে প্রথম ২টি সারি দেখাচ্ছে, কিন্তু যেহেতু স্যাম্পল নেওয়ার পর মাত্র ১টি সারি আছে, তাই শুধু সেই ১টি সারি প্রদর্শিত হবে।

1. সংক্ষেপে, এই স্ক্রিপ্টটি একটি JSON Lines ফাইল pandas DataFrame এ পড়ছে, ১টি র্যান্ডম স্যাম্পল নিচ্ছে, ইন্ডেক্স রিসেট করছে এবং প্রথম সারি প্রদর্শন করছে।

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### JSON অবজেক্ট তৈরি করা

1. এই Python স্ক্রিপ্টটি নির্দিষ্ট প্যারামিটারসহ একটি JSON অবজেক্ট তৈরি করে এবং সেটি একটি ফাইলে সেভ করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি json মডিউল ইমপোর্ট করে, যা JSON ডেটা নিয়ে কাজ করার ফাংশন সরবরাহ করে।

- এটি parameters নামের একটি ডিকশনারি তৈরি করে, যার কী ও ভ্যালুগুলো মেশিন লার্নিং মডেলের প্যারামিটার নির্দেশ করে। কী গুলো হলো "temperature", "top_p", "do_sample", এবং "max_new_tokens", এবং তাদের মান যথাক্রমে ০.৬, ০.৯, True, এবং ২০০।

- এটি আরেকটি ডিকশনারি test_json তৈরি করে, যার দুটি কী আছে: "input_data" এবং "params"। "input_data" এর মান আরেকটি ডিকশনারি, যার কী গুলো হলো "input_string" এবং "parameters"। "input_string" হলো test_df DataFrame থেকে প্রথম মেসেজের একটি লিস্ট, এবং "parameters" হলো আগের parameters ডিকশনারি। "params" হলো একটি খালি ডিকশনারি।

- এটি sample_score.json নামের একটি ফাইল ওপেন করে...

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### এন্ডপয়েন্ট কল করা

1. এই Python স্ক্রিপ্টটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্ট কল করে একটি JSON ফাইল স্কোর করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি workspace_ml_client অবজেক্টের online_endpoints প্রপার্টির invoke মেথড কল করে। এই মেথড অনলাইন এন্ডপয়েন্টে রিকোয়েস্ট পাঠাতে এবং রেসপন্স পেতে ব্যবহৃত হয়।

- এটি endpoint_name এবং deployment_name আর্গুমেন্ট দিয়ে এন্ডপয়েন্ট এবং ডিপ্লয়মেন্টের নাম নির্দিষ্ট করে। এখানে এন্ডপয়েন্টের নাম online_endpoint_name ভেরিয়েবলে রাখা হয়েছে এবং ডিপ্লয়মেন্টের নাম "demo"।

- এটি request_file আর্গুমেন্টে স্কোর করার JSON ফাইলের পথ দেয়, যা ./ultrachat_200k_dataset/sample_score.json।

- এটি এন্ডপয়েন্ট থেকে পাওয়া রেসপন্স response ভেরিয়েবলে রাখে।

- এটি রেসপন্সের র কাঁচা আউটপুট প্রিন্ট করে।

1. সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্ট কল করে একটি JSON ফাইল স্কোর করছে এবং রেসপন্স প্রিন্ট করছে।

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## ৯. অনলাইন এন্ডপয়েন্ট ডিলিট করা

1. অনলাইন এন্ডপয়েন্ট ডিলিট করতে ভুলবেন না, না হলে এন্ডপয়েন্টের ব্যবহৃত কম্পিউটের জন্য বিলিং চলতেই থাকবে। এই Python কোডটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্ট ডিলিট করছে। এর কাজের সংক্ষিপ্ত বিবরণ নিচে দেওয়া হলো:

- এটি workspace_ml_client অবজেক্টের online_endpoints প্রপার্টির begin_delete মেথড কল করে। এই মেথড অনলাইন এন্ডপয়েন্ট ডিলিট করার প্রক্রিয়া শুরু করে।

- এটি name আর্গুমেন্টে ডিলিট করার এন্ডপয়েন্টের নাম দেয়, যা এখানে online_endpoint_name ভেরিয়েবলে রাখা আছে।

- এটি wait মেথড কল করে ডিলিট অপারেশন শেষ হওয়ার জন্য অপেক্ষা করে। এটি একটি ব্লকিং অপারেশন, অর্থাৎ ডিলিট শেষ না হওয়া পর্যন্ত স্ক্রিপ্ট চলবে না।

- সংক্ষেপে, এই কোডটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্ট ডিলিট করার প্রক্রিয়া শুরু করছে এবং অপারেশন শেষ হওয়ার জন্য অপেক্ষা করছে।

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজ ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ব্যাখ্যার জন্য আমরা দায়ী নই।