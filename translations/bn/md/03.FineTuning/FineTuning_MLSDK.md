## কিভাবে Azure ML সিস্টেম রেজিস্ট্রি থেকে চ্যাট-কমপ্লিশন উপাদান ব্যবহার করে একটি মডেল ফাইন টিউন করবেন

এই উদাহরণে আমরা ultrachat_200k ডেটাসেট ব্যবহার করে Phi-3-mini-4k-instruct মডেলকে ২ জন ব্যক্তির মধ্যে কথোপকথন সম্পূর্ণ করার জন্য ফাইন টিউন করব।

![MLFineTune](../../../../translated_images/bn/MLFineTune.928d4c6b3767dd35.webp)

এই উদাহরণটি আপনাকে Azure ML SDK এবং পাইথন ব্যবহার করে কিভাবে ফাইন টিউন করবেন এবং পরে ফাইন টিউনকৃত মডেলটি রিয়েল টাইম ইনফারেন্সের জন্য একটি অনলাইন এন্ডপয়েন্টে ডিপ্লয় করবেন তা দেখাবে।

### ট্রেনিং ডেটা

আমরা ultrachat_200k ডেটাসেট ব্যবহার করব। এটি UltraChat ডেটাসেটের একটি ব্যাপকভাবে পরিশোধিত সংস্করণ এবং Zephyr-7B-β, একটি আধুনিক 7b চ্যাট মডেল, প্রশিক্ষণের জন্য ব্যবহৃত হয়।

### মডেল

আমরা Phi-3-mini-4k-instruct মডেল ব্যবহার করব দেখাতে কিভাবে ব্যবহারকারী চ্যাট-কমপ্লিশন টাস্কের জন্য একটি মডেল ফাইনটিউন করতে পারেন। আপনি যদি এই নোটবুকটি কোনও নির্দিষ্ট মডেল কার্ড থেকে খুলে থাকেন, তবে নির্দিষ্ট মডেল নামটি প্রতিস্থাপন করতে ভুলবেন না।

### টাস্কসমূহ

- ফাইন টিউনের জন্য একটি মডেল নির্বাচন করুন।
- ট্রেনিং ডেটা নির্বাচন ও অনুসন্ধান করুন।
- ফাইন টিউনিং জব কনফিগার করুন।
- ফাইন টিউনিং জব চালান।
- ট্রেনিং ও মূল্যায়ন মেট্রিক্স পর্যালোচনা করুন।
- ফাইন টিউনকৃত মডেল নিবন্ধন করুন।
- রিয়েল টাইম ইনফারেন্সের জন্য ফাইন টিউনকৃত মডেল ডিপ্লয় করুন।
- রিসোর্সগুলো পরিষ্কার করুন।

## ১। প্রয়োজনীয়তা সেটআপ করুন

- ডিপেন্ডেন্সি ইনস্টল করুন
- AzureML ওয়ার্কস্পেসের সাথে সংযোগ করুন। বেশি জানুন set up SDK authentication পৃষ্ঠায়। নিচের <WORKSPACE_NAME>, <RESOURCE_GROUP> এবং <SUBSCRIPTION_ID> প্রতিস্থাপন করুন।
- azureml সিস্টেম রেজিস্ট্রি সংযোগ করুন
- একটি ঐচ্ছিক এক্সপেরিমেন্ট নাম সেট করুন
- কম্পিউট চেক করুন বা তৈরি করুন।

> [!NOTE]
> প্রয়োজন একটি সিঙ্গল GPU নোড যা একাধিক GPU কার্ড থাকতে পারে। উদাহরণস্বরূপ, Standard_NC24rs_v3 এর একটি নোডে ৪টি NVIDIA V100 GPU থাকে, আর Standard_NC12s_v3 এ ২টি NVIDIA V100 GPU থাকে। এই তথ্যের জন্য ডকুমেন্টেশন দেখুন। প্রতিটি নোডে GPU কার্ডের সংখ্যা নিচের param gpus_per_node এ সেট করা হয়। সঠিক মান সেট করলে নোডের সমস্ত GPU-এর ব্যবহার নিশ্চিত হয়। সুপারিশকৃত GPU compute SKU গুলো এখানে এবং এখানে পাওয়া যাবে।

### পাইথন লাইব্রেরি

নিচের সেল রান করে ডিপেন্ডেন্সি ইনস্টল করুন। যদি নতুন পরিবেশে রান করেন, এটি একটি বাধ্যতামূলক ধাপ।

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML এর সাথে ইন্টারঅ্যাকশন

1. এই পাইথন স্ক্রিপ্ট Azure Machine Learning (Azure ML) সার্ভিসের সাথে ইন্টারঅ্যাকশন করার জন্য ব্যবহৃত। এটি কী করে তার সারাংশ:

    - azure.ai.ml, azure.identity, এবং azure.ai.ml.entities প্যাকেজ থেকে প্রয়োজনীয় মডিউল ইমপোর্ট করে। সঙ্গে time মডিউলও ইমপোর্ট করে।

    - DefaultAzureCredential() ব্যবহার করে অথেন্টিকেট করার চেষ্টা করে, যা Azure ক্লাউডে অ্যাপ্লিকেশন দ্রুত ডেভেলপ করতে সহজ অথেন্টিকেশন প্রদান করে। ব্যর্থ হলে InteractiveBrowserCredential() ব্যবহার করে ইন্টারেক্টিভ লগইন প্রম্পট দেয়।

    - পরে from_config পদ্ধতি ব্যবহার করে MLClient তৈরি করার চেষ্টা করে, যা ডিফল্ট কনফিগ ফাইল (config.json) থেকে কনফিগuration পড়ে। ব্যর্থ হলে subscription_id, resource_group_name, এবং workspace_name ম্যানুয়ালি দিয়ে MLClient তৈরি করে।

    - আরেকটি MLClient উদাহরণ তৈরি করে, এইবার Azure ML রেজিস্ট্রি "azureml" এর জন্য। এই রেজিস্ট্রিতেই মডেল, ফাইন-টিউনিং পাইপলাইন এবং এনভায়রনমেন্ট সংরক্ষিত থাকে।

    - experiment_name "chat_completion_Phi-3-mini-4k-instruct" সেট করে।

    - বর্তমানে সময় (সেকেন্ডে) থেকে অনন্য টাইমস্ট্যাম্প তৈরি করে, যা ইউনিক নাম এবং ভার্সন তৈরিতে ব্যবহৃত হতে পারে।

    ```python
    # Azure ML এবং Azure Identity থেকে প্রয়োজনীয় মডিউলগুলি আমদানি করুন
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # টাইম মডিউল আমদানি করুন
    
    # DefaultAzureCredential ব্যবহার করে প্রমাণীকরণ করার চেষ্টা করুন
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # যদি DefaultAzureCredential ব্যর্থ হয়, InteractiveBrowserCredential ব্যবহার করুন
        credential = InteractiveBrowserCredential()
    
    # ডিফল্ট কনফিগ ফাইল ব্যবহার করে MLClient ইনস্ট্যান্স তৈরি করার চেষ্টা করুন
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # যদি তা ব্যর্থ হয়, ম্যানুয়ালি বিবরণ সরবরাহ করে MLClient ইনস্ট্যান্স তৈরি করুন
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" নামের Azure ML রেজিস্ট্রির জন্য আরেকটি MLClient ইনস্ট্যান্স তৈরি করুন
    # এই রেজিস্ট্রি যেখানে মডেল, ফাইন-টিউনিং পাইপলাইন এবং এনভায়রনমেন্ট সংরক্ষিত থাকে
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # এক্সপেরিমেন্টের নাম সেট করুন
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # এমন একটি অনন্য টাইমস্ট্যাম্প তৈরি করুন যা নাম এবং সংস্করণের জন্য ব্যবহার করা যেতে পারে যা অনন্য হতে হবে
    timestamp = str(int(time.time()))
    ```

## ২। ফাইন টিউনের জন্য একটি ফাউন্ডেশন মডেল বেছে নিন

1. Phi-3-mini-4k-instruct হলো 3.8 বিলিয়ন প্যারামিটার বিশিষ্ট, হালকা ওজনের, অত্যাধুনিক ওপেন মডেল যা Phi-2 এর ডেটাসেটের উপর নির্মিত। এই মডেলটি Phi-3 মডেল পরিবারের অন্তর্ভুক্ত, এবং মিনি ভার্সনটির দুটি ভ্যারিয়েন্ট রয়েছে 4K ও 128K, যা প্রসঙ্গ দৈর্ঘ্য (টোকেন সংখ্যা) নির্দেশ করে, যেটি এটি সমর্থন করতে পারে। আমাদের নির্দিষ্ট কাজে এটি ব্যবহার করতে ফাইনটিউন করতে হবে। আপনি AzureML স্টুডিওর মডেল ক্যাটালগে চ্যাট-কমপ্লিশন টাস্ক ফিল্টার করে এই মডেলগুলো ব্রাউজ করতে পারেন। এই উদাহরণে Phi-3-mini-4k-instruct মডেল ব্যবহার করা হয়েছে। আপনি যদি অন্য কোন মডেলের জন্য নোটবুকটি খুলে থাকেন, তবে মডেল নাম ও ভার্সন যথাযথভাবে প্রতিস্থাপন করুন।

> [!NOTE]
> মডেলের id প্রপার্টি। এটি ফাইন টিউনিং জবে ইনপুট হিসেবে পাঠানো হবে। AzureML স্টুডিও মডেল ক্যাটালগের মডেল ডিটেইলস পৃষ্ঠায় Asset ID নামে এই তথ্য পাওয়া যায়।

2. এই পাইথন স্ক্রিপ্ট Azure Machine Learning (Azure ML) সার্ভিসের সাথে ইন্টারঅ্যাকশন করছে। এর কার্যপদ্ধতির সারাংশ:

    - model_name "Phi-3-mini-4k-instruct" সেট করা হয়েছে।

    - registry_ml_client অবজেক্টের models প্রপার্টির get মেথড ব্যবহার করে Azure ML রেজিস্ট্রির নির্দিষ্ট নামের মডেলের সর্বশেষ ভার্সন আনা হচ্ছে। get মেথডে মডেল নাম এবং লেবেল (latest) প্যারামিটার হিসেবে দেয়া হয়েছে।

    - কনসোলে মেসেজ প্রিন্ট করে যে ফাইন-টিউনের জন্য কোন মডেলটি ব্যবহার হবে, তার নাম, ভার্সন এবং আইডি দেখানো হয়েছে। string.format মেথড দিয়ে mfoundation_model অবজেক্টের প্রপার্টি ব্যবহার করে এই তথ্য গুলো মেসেজে ঢুকানো হয়।

    ```python
    # মডেলের নাম সেট করুন
    model_name = "Phi-3-mini-4k-instruct"
    
    # Azure ML রেজিস্ট্রি থেকে মডেলের সর্বশেষ সংস্করণ পান
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # মডেলের নাম, সংস্করণ, এবং আইডি প্রিন্ট করুন
    # এই তথ্য ট্র্যাকিং এবং ডিবাগিংয়ের জন্য উপকারী
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## ৩। জবের জন্য একটি কম্পিউট তৈরি করুন

ফাইনটিউন জব শুধুমাত্র GPU কম্পিউটের সাথে কাজ করে। কম্পিউট সাইজ মডেলের আকারের ওপর নির্ভর করে এবং বেশিরভাগ ক্ষেত্রে সঠিক কম্পিউট নির্বাচন কঠিন হয়ে ওঠে। এই সেলে আমরা ব্যবহারকারীকে সঠিক কম্পিউট নির্বাচন করতে সহায়তা করব।

> [!NOTE]
> নিচের কম্পিউট গুলো সর্বোত্তম কনফিগারেশনে কাজ করে। কনফিগারেশনে যেকোনো পরিবর্তন CUDA Out Of Memory ত্রুটি দিতে পারে। এমন ক্ষেত্রে বড় কম্পিউট সাইজে আপগ্রেড করার চেষ্টা করুন।

> [!NOTE]
> কম্পিউট ক্লাস্টার সাইজ নির্বাচন করার সময় নিশ্চিত করুন যে কম্পিউটটি আপনার রিসোর্স গ্রুপে উপলব্ধ। যদি নির্দিষ্ট কম্পিউট না থাকে, তবে কম্পিউট রিসোর্সের অ্যাক্সেস পেতে অনুরোধ করতে পারেন।

### ফাইন টিউনের জন্য মডেলের সমর্থন যাচাই করা

1. এই পাইথন স্ক্রিপ্টটি Azure ML মডেলের সাথে ইন্টারঅ্যাকশন করছে। কার্যপদ্ধতির সারাংশ:

    - ast মডিউল ইমপোর্ট করা হয়েছে, যা পাইথনের অ্যাবস্ট্রাক্ট সিনট্যাক্স ট্রির প্রক্রিয়াকরণে ব্যবহৃত হয়।

    - foundation_model অবজেক্টের ট্যাগগুলোর মধ্যে finetune_compute_allow_list নামের ট্যাগ আছে কিনা পরীক্ষা করে। Azure ML ট্যাগগুলো key-value জোড়া যা মডেল ফিল্টার করার কাজে লাগে।

    - finetune_compute_allow_list থাকলে ast.literal_eval দিয়ে তার মানকে স্ট্রিং থেকে পাইথন লিস্টে রূপান্তরিত করে computes_allow_list ভেরিয়েবলে রাখে এবং একটি মেসেজ প্রিন্ট করে জানান দেয় যে লিস্ট থেকে কম্পিউট তৈরি করা উচিত।

    - finetune_compute_allow_list না থাকলে computes_allow_list কে None দেয় এবং মেসেজ প্রিন্ট করে জানায় যে এই ট্যাগ মডেলের ট্যাগে নেই।

    - সংক্ষেপে, এটি মডেলের মেটাডেটাতে নির্দিষ্ট ট্যাগের উপস্থিতি যাচাই করে, থাকলে তার মান লিস্ট রূপে রূপান্তরিত করে এবং ব্যবহারকারীকে ফিডব্যাক দেয়।

    ```python
    # Python অ্যাবস্ট্রাক্ট সিনট্যাক্স ব্যাকরণের গাছ প্রক্রিয়াকরণের জন্য ফাংশন সরবরাহ করে এমন ast মডিউলটি ইম্পোর্ট করুন
    import ast
    
    # মডেলের ট্যাগগুলিতে 'finetune_compute_allow_list' ট্যাগটি উপস্থিত আছে কিনা তা পরীক্ষা করুন
    if "finetune_compute_allow_list" in foundation_model.tags:
        # যদি ট্যাগ উপস্থিত থাকে, তাহলে ast.literal_eval ব্যবহার করে ট্যাগের মান (একটি স্ট্রিং) নিরাপদে একটি Python তালিকায় পার্স করুন
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # স্ট্রিংকে পাইথন তালিকায় রূপান্তর করুন
        # একটি বার্তা প্রিন্ট করুন যা নির্দেশ করে যে তালিকা থেকে একটি কম্পিউট তৈরি করা উচিত
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # যদি ট্যাগ উপস্থিত না থাকে, তাহলে computes_allow_list কে None সেট করুন
        computes_allow_list = None
        # একটি বার্তা প্রিন্ট করুন যা নির্দেশ করে যে 'finetune_compute_allow_list' ট্যাগটি মডেলের ট্যাগগুলির অংশ নয়
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### কম্পিউট ইনস্ট্যান্স যাচাই করা

1. এই পাইথন স্ক্রিপ্টটি Azure ML সার্ভিসের কম্পিউট ইনস্ট্যান্স নিয়ে বিভিন্ন যাচাই করছে। কার্যপদ্ধতির সারাংশ:

    - compute_cluster নামের কম্পিউট ইনস্ট্যান্স Azure ML ওয়ার্কস্পেস থেকে আনার চেষ্টা করে। যদি তার provisioning state "failed" হয়, ValueError ফেলে।

    - computes_allow_list None না হলে, লিস্টের সব কম্পিউট সাইজ ছোট হাতের ক্যারেক্টারে রূপান্তর করে এবং বর্তমান কম্পিউট ইনস্ট্যান্সের সাইজ লিস্টে আছে কিনা যাচাই করে। না থাকলে ValueError দেয়।

    - computes_allow_list None হলে, কম্পিউট সাইজ একটি নির্দিষ্ট অসমর্থিত GPU VM সাইজের তালিকায় আছে কিনা চেক করে। থাকলে ValueError দেয়।

    - ওয়ার্কস্পেসের সকল উপলব্ধ কম্পিউট সাইজের তালিকা আনে। তারপরে প্রতিটি কম্পিউট সাইজের নাম মিলে গেলে ঐ কম্পিউট সাইজের GPU সংখ্যা নিয়ে gpu_count_found=True সেট করে।

    - gpu_count_found সত্য হলে, কম্পিউটে GPU সংখ্যাটি প্রিন্ট করে। অন্যথায় ValueError ফেলে।

    - সংক্ষেপে, এটি একটি Azure ML ওয়ার্কস্পেসের কম্পিউট ইনস্ট্যান্সের provisioning state, সাইজ তার অনুমোদিত তালিকা বা নিষিদ্ধ তালিকার বিরুদ্ধে যাচাই এবং GPU সংখ্যা নির্ণয় করে।

    
    ```python
    # ব্যতিক্রম বার্তা প্রিন্ট করুন
    print(e)
    # ওয়ার্কস্পেসে কম্পিউট সাইজ উপলব্ধ না থাকলে ValueError ত্রুটি উত্থাপন করুন
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML ওয়ার্কস্পেস থেকে কম্পিউট ইনস্ট্যান্স পুনরুদ্ধার করুন
    compute = workspace_ml_client.compute.get(compute_cluster)
    # কম্পিউট ইনস্ট্যান্সের provisioning অবস্থা "failed" কিনা পরীক্ষা করুন
    if compute.provisioning_state.lower() == "failed":
        # provisioning অবস্থা "failed" হলে ValueError ত্রুটি উত্থাপন করুন
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # পরীক্ষা করুন যে computes_allow_list None নয়
    if computes_allow_list is not None:
        # computes_allow_list এর সব কম্পিউট সাইজকে ছোট হাতের অক্ষরে রূপান্তর করুন
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # পরীক্ষা করুন যে কম্পিউট ইনস্ট্যান্সের সাইজটি computes_allow_list_lower_case তে আছে কিনা
        if compute.size.lower() not in computes_allow_list_lower_case:
            # কম্পিউট ইনস্ট্যান্সের সাইজটি computes_allow_list_lower_case তে না থাকলে ValueError ত্রুটি উত্থাপন করুন
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # অসমর্থিত GPU VM সাইজের একটি তালিকা সংজ্ঞায়িত করুন
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # পরীক্ষা করুন যে কম্পিউট ইনস্ট্যান্সের সাইজটি unsupported_gpu_vm_list এ আছে কিনা
        if compute.size.lower() in unsupported_gpu_vm_list:
            # কম্পিউট ইনস্ট্যান্সের সাইজটি unsupported_gpu_vm_list এ থাকলে ValueError ত্রুটি উত্থাপন করুন
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # কম্পিউট ইনস্ট্যান্সে GPU এর সংখ্যা খুঁজে পাওয়া হয়েছে কিনা তা পরীক্ষা করার জন্য একটি ফ্ল্যাগ শুরু করুন
    gpu_count_found = False
    # ওয়ার্কস্পেসে উপলব্ধ সব কম্পিউট সাইজের একটি তালিকা পুনরুদ্ধার করুন
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # উপলব্ধ কম্পিউট সাইজের তালিকায় পুনরাবৃত্তি করুন
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # পরীক্ষা করুন যে কম্পিউট সাইজের নাম কম্পিউট ইনস্ট্যান্সের সাইজের সাথে মেলে কিনা
        if compute_sku.name.lower() == compute.size.lower():
            # যদি মেলে, তাহলে ঐ কম্পিউট সাইজের জন্য GPU এর সংখ্যা পুনরুদ্ধার করুন এবং gpu_count_found কে True সেট করুন
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # যদি gpu_count_found True হয়, তাহলে কম্পিউট ইনস্ট্যান্সে GPU এর সংখ্যা প্রিন্ট করুন
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # যদি gpu_count_found False হয়, তাহলে ValueError ত্রুটি উত্থাপন করুন
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## ৪। ফাইন টিউনের জন্য ডেটাসেট নির্বাচন করুন

1. আমরা ultrachat_200k ডেটাসেট ব্যবহার করব। ডেটাসেটটির চারটি ভাগ আছে, যা সুপারভাইজড ফাইন-টিউনিং (sft) এর জন্য উপযোগী। জেনারেশন র‍্যাংকিং (gen)। প্রতিটি ভাগের নমুনার সংখ্যা নিচে দেখানো হলো:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. পরবর্তী কয়েকটি সেল ফাইনটিউনিং-এর জন্য প্রাথমিক ডেটা প্রস্তুতি দেখায়:

### কিছু ডেটা সারি ভিজ্যুয়ালাইজ করুন

আমরা এই স্যাম্পলটি দ্রুত চালাতে চাই, তাই train_sft, test_sft ফাইলগুলোতে ইতিমধ্যে ট্রিমকৃত সারির ৫% তথ্য সংরক্ষণ করা হবে। এর মানে ফাইন টিউনকৃত মডেলের সঠিকতা কম থাকবে, সুতরাং এটি বাস্তব ব্যবহারে ব্যবহার করা উচিত নয়। download-dataset.py স্ক্রিপ্টটি ultrachat_200k ডেটাসেট ডাউনলোড করে এবং ডেটাসেটকে ফাইনটিউন পাইপলাইন কম্পোনেন্টে ব্যবহারের উপযোগী ফর্ম্যাটে রূপান্তর করে। চूंकि ডেটাসেট বড়, তাই এখানে শুধু ডেটাসেটের একটি অংশ আছে।

1. নিচের স্ক্রিপ্টটি রান করলে মাত্র ৫% ডেটা ডাউনলোড হবে। dataset_split_pc প্যারামিটার পরিবর্তন করে এটি বাড়ানো যেতে পারে।

> [!NOTE]
> কিছু ভাষা মডেলের ভাষা কোড ভিন্ন হতে পারে, তাই ডেটাসেটের কলাম নামও সেই অনুযায়ী থাকা উচিত।

1. এখানে একটি উদাহরণ রয়েছে ডেটার কেমন হওয়া উচিত তা দেখানোর জন্য:
চ্যাট-কমপ্লিশন ডেটাসেট প্যারকেট ফরম্যাটে সংরক্ষিত, যেখানে প্রতিটি এন্ট্রি নিচের স্কিমা অনুসারে থাকে:

    - এটি একটি JSON (JavaScript Object Notation) ডকুমেন্ট, যা একটি জনপ্রিয় ডেটা বিনিময় ফরম্যাট। এটি এক্সিকিউটেবল কোড নয়, বরং ডেটা সংরক্ষণ ও পরিবহনের উপায়। এর কাঠামোর বিশ্লেষণ:

    - "prompt": এই কীটির মান একটি স্ট্রিং যা AI অ্যাসিস্ট্যান্টকে দেওয়া টাস্ক বা প্রশ্ন নির্দেশ করে।

    - "messages": এই কীটির মান একটি অবজেক্টের অ্যারে, যেখানে প্রতিটি অবজেক্ট একটি কথোপকথনের মেসেজ নির্দেশ করে, যেটি ব্যবহারকারী ও AI অ্যাসিস্ট্যান্টের মধ্যে হয়। প্রতিটি মেসেজ অবজেক্টে দুটি কী থাকে:

    - "content": এই কীয়ের মান মেসেজের বিষয়বস্তু স্ট্রিং হিসেবে আছে।
    - "role": এই কীয়ের মান স্ট্রিং এবং পাঠানো পক্ষের ভূমিকা নির্দেশ করে; এটি "user" বা "assistant" হতে পারে।
    - "prompt_id": এটি একটি স্ট্রিং মান যা প্রম্পটের অনন্য আইডি নির্দেশ করে।

1. এই JSON ডকুমেন্টে একটি কথোপকথন দেখানো হয়েছে যেখানে ব্যবহারকারী একটি ডাইস্টোপিয়ান গল্পের প্রধান চরিত্র তৈরি করার অনুরোধ করে। অ্যাসিস্ট্যান্ট উত্তর দেয়, পরে ব্যবহারকারী আরও বিস্তারিত চায় এবং অ্যাসিস্ট্যান্ট আরও বিস্তারিত দেওয়ার সম্মতি দেয়। পুরো কথোপকথন একটি নির্দিষ্ট প্রম্পট আইডির সাথে যুক্ত।

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

### ডেটা ডাউনলোড করুন

1. এই পাইথন স্ক্রিপ্ট একটি হেল্পার স্ক্রিপ্ট download-dataset.py ব্যবহার করে ডেটাসেট ডাউনলোড করতে ব্যবহৃত। এর কার্যপদ্ধতির সারাংশ:

    - os মডিউল ইমপোর্ট করে, যা অপারেটিং সিস্টেম-নির্ভর কার্যকারিতার জন্য ব্যবহৃত।

    - os.system ফাংশন ব্যবহার করে download-dataset.py স্ক্রিপ্ট শেল থেকে চালায়, কমান্ড লাইনে কিছু আর্গুমেন্ট দিয়ে। আর্গুমেন্টে ডেটাসেটের নাম (HuggingFaceH4/ultrachat_200k), ডাউনলোড ফোল্ডার (ultrachat_200k_dataset), এবং ডেটাসেট স্প্লিটের শতাংশ (5) উল্লেখ আছে। os.system রান শেষে যা রিটার্ন করে সেটি exit_status ভেরিয়েবলে রাখা হয়।

    - exit_status 0 না হলে এটি একটি Exception ছুড়ে দেয় যে ডেটাসেট ডাউনলোডের সময় ত্রুটি হয়েছে।

    - সংক্ষেপে, এটি একটি হেল্পার স্ক্রিপ্টের মাধ্যমে ডেটাসেট ডাউনলোডের কমান্ড রান করায় এবং ব্যর্থ হলে ত্রুটি দেয়।

    
    ```python
    # os মডিউল ইমপোর্ট করুন, যা অপারেটিং সিস্টেম নির্ভর কার্যকারিতা ব্যবহারের একটি উপায় প্রদান করে
    import os
    
    # নির্দিষ্ট কমান্ড-লাইন আর্গুমেন্টসহ শেলে download-dataset.py স্ক্রিপ্ট চালানোর জন্য os.system ফাংশন ব্যবহার করুন
    # আর্গুমেন্টগুলি ডাউনলোড করার জন্য ডেটাসেট নির্দিষ্ট করে (HuggingFaceH4/ultrachat_200k), ডাউনলোড করার ডিরেক্টরি (ultrachat_200k_dataset), এবং ডেটাসেট ভাগ করার শতাংশ (5)
    # os.system ফাংশন যেই কমান্ডটি চালিয়েছে তার exit status ফেরত দেয়; এই স্ট্যাটাস exit_status ভেরিয়েবলে সংরক্ষিত হয়
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # পরীক্ষা করুন exit_status 0 নয় কিনা
    # ইউনিক্স-সদৃশ অপারেটিং সিস্টেমে, exit status 0 সাধারণত নির্দেশ করে যে একটি কমান্ড সফল হয়েছে, অন্য যেকোন সংখ্যাই ত্রুটি নির্দেশ করে
    # যদি exit_status 0 না হয়, তাহলে একটি Exception উঠান একটি বার্তা সহ যা নির্দেশ করে যে ডেটাসেট ডাউনলোড করার সময় ত্রুটি হয়েছে
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### ডেটা একটি ডেটাফ্রেমে লোড করা

1. এই পাইথন স্ক্রিপ্ট একটি JSON Lines ফাইলকে pandas DataFrame এ লোড করে এবং প্রথম ৫টি সারি দেখায়। এর কার্যপদ্ধতির সারাংশ:

    - pandas লাইব্রেরি ইমপোর্ট করে, যা ডেটা ম্যানিপুলেশন ও বিশ্লেষণের জন্য শক্তিশালী একটি টুল।

    - pandas এর ডিসপ্লে অপশনে max column width 0 করে দেয়, অর্থাৎ প্রতিটি কলামের পূর্ণ টেক্সট প্রিন্ট হবে truncation ছাড়া।


- এটি pd.read_json ফাংশনটি ব্যবহার করে ultrachat_200k_dataset ডিরেক্টরির train_sft.jsonl ফাইলটি একটি DataFrame-এ লোড করে। lines=True আর্গুমেন্টটি নির্দেশ করে যে ফাইলটি JSON Lines ফরম্যাটে আছে, যেখানে প্রতিটি লাইন একটি আলাদা JSON অবজেক্ট।

- এটি head মেথডটি ব্যবহার করে DataFrame-এর প্রথম ৫টি সারি প্রদর্শন করে। যদি DataFrame-এ ৫টির কম সারি থাকে, তাহলে সেগুলো সবই প্রদর্শন করা হবে।

- সংক্ষেপে, এই স্ক্রিপ্টটি একটি JSON Lines ফাইল DataFrame-এ লোড করছে এবং প্রথম ৫টি সারি সম্পূর্ণ কলামের টেক্সটসহ প্রদর্শন করছে।
    
    ```python
    # pandas লাইব্রেরি ইমপোর্ট করুন, যা একটি শক্তিশালী ডেটা ম্যানিপুলেশন এবং বিশ্লেষণ লাইব্রেরি
    import pandas as pd
    
    # pandas-এর ডিসপ্লে অপশনগুলির জন্য সর্বোচ্চ কলামের প্রস্থ 0 সেট করুন
    # এর অর্থ হল যখন DataFrame প্রিন্ট করা হবে তখন প্রতিটি কলামের সম্পূর্ণ টেক্সট ছাঁটাই ছাড়াই প্রদর্শিত হবে
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json ফাংশন ব্যবহার করে ultrachat_200k_dataset ডিরেক্টরির train_sft.jsonl ফাইলটি একটি DataFrame-এ লোড করুন
    # lines=True আর্গুমেন্টটি নির্দেশ করে যে ফাইলটি JSON Lines ফরম্যাটে আছে, যেখানে প্রতিটি লাইন একটি পৃথক JSON অবজেক্ট
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # head মেথড ব্যবহার করে DataFrame-এর প্রথম ৫টি সারি প্রদর্শন করুন
    # যদি DataFrame-এর সারির সংখ্যা ৫-এর কম হয়, তবে সবগুলোই প্রদর্শিত হবে
    df.head()
    ```

## ৫। মডেল এবং ডেটা ইনপুট হিসেবে ব্যবহার করে ফাইন টিউনিং জব সাবমিট করা

চ্যাট-কমপ্লিশন পাইপলাইন কম্পোনেন্ট ব্যবহার করে জব তৈরি করুন। ফাইন টিউনিংয়ের জন্য সাপোর্টকৃত সব প্যারামিটার সম্পর্কে আরও জানুন।

### ফাইনটিউন প্যারামিটার সংজ্ঞায়িত করা

১। ফাইনটিউন প্যারামিটার দুইটি শ্রেণিতে বিভক্ত - ট্রেনিং প্যারামিটার, অপটিমাইজেশন প্যারামিটার

১। ট্রেনিং প্যারামিটারগুলি ট্রেনিংয়ের দিকনির্দেশনা দেয় যেমন -

   - কোন অপটিমাইজার, স্কেজুলার ব্যবহার করা হবে
   - ফাইনটিউনের জন্য কোন মেট্রিক অপটিমাইজ করা হবে
   - ট্রেনিংয়ের ধাপ সংখ্যা, ব্যাচ সাইজ ইত্যাদি
   - অপটিমাইজেশন প্যারামিটার GPU মেমোরি অপ্টিমাইজ এবং কম্পিউট সম্পদ কার্যকরভাবে ব্যবহার করতে সাহায্য করে।

১। নিচে কিছু অপটিমাইজেশন প্যারামিটার দেখানো হলো যা এই শ্রেণির, মডেল অনুযায়ী অপটিমাইজেশন প্যারামিটার ভিন্ন হয়ে থাকে এবং মডেলের সাথে প্যাকেজ করা থাকে।

   - Deepspeed এবং LoRA সক্রিয় করা
   - মিক্সড প্রিসিশন ট্রেনিং সক্রিয় করা
   - মাল্টি-নোড ট্রেনিং সক্রিয় করা

> [!NOTE]
> সুপারভাইজড ফাইনটিউনিংয়ে এলাইনমেন্ট হারানোর বা জটিল ভুলে যাওয়ার সমস্যা হতে পারে। আমরা এটি চেক করার এবং আপনার ফাইনটিউন করার পর এলাইনমেন্ট স্টেজ চালানোর পরামর্শ দিই।

### ফাইন টিউনিং প্যারামিটারসমূহ

১। এই পাইথন স্ক্রিপ্টটি মেশিন লার্নিং মডেলের ফাইনটিউনিংয়ের প্যারামিটার সেট করছে। নিচে তার সংক্ষিপ্ত ব্যাখ্যা রয়েছে:

   - এটি ডিফল্ট ট্রেনিং প্যারামিটার যেমন ট্রেনিংয়ের ইপোক সংখ্যা, ট্রেন ও ইভ্যালুয়েশনের ব্যাচ সাইজ, লার্নিং রেট, লার্নিং রেট স্কেজুলার টাইপ সেট করছে।

   - এটি ডিফল্ট অপটিমাইজেশন প্যারামিটার যেমন লেয়ার-ওয়াইজ রিলেভেন্স প্রোপাগেশন (LoRa) এবং DeepSpeed প্রয়োগের বিষয়, DeepSpeed স্টেজ সেট করছে।

   - ট্রেনিং ও অপটিমাইজেশন প্যারামিটারগুলোকে finetune_parameters নামের একটি ডিকশনারিতে মিলিয়ে নিচ্ছে।

   - foundation_model-এ যদি মডেল-স্পেসিফিক কোনো ডিফল্ট প্যারামিটার থাকে, তবে একটি ওয়ার্নিং মেসেজ প্রিন্ট করে এবং finetune_parameters ডিকশনারি আপডেট করে থাকেন সেই মডেল-স্পেসিফিক ডিফল্ট দিয়ে। ast.literal_eval ফাংশন স্ট্রিং থেকে পাইথন ডিকশনারিতে পরিণত করতে ব্যবহৃত হয়।

   - চলার জন্য ব্যবহার করা হবে এমন ফাইন-টিউনিং প্যারামিটারগুলোর ফাইনাল সেট প্রিন্ট করে।

   - সংক্ষেপে, এই স্ক্রিপ্টটি মডেলের ফাইনটিউনিংয়ের প্যারামিটারসেট আপডেট ও প্রদর্শন করছে, যেখানে মডেল-স্পেসিফিক প্যারামিটার দিয়ে ডিফল্ট ওভাররাইড করা সম্ভব।

    ```python
    # ডিফল্ট প্রশিক্ষণ পরামিতি সেট আপ করুন যেমন প্রশিক্ষণের এপোকের সংখ্যা, প্রশিক্ষণ এবং মূল্যায়নের জন্য ব্যাচ সাইজ, শেখার হার, এবং শেখার হার শিডিউলার এর ধরন
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # ডিফল্ট অপ্টিমাইজেশন পরামিতি সেট আপ করুন যেমন Layer-wise Relevance Propagation (LoRa) এবং DeepSpeed প্রয়োগ করা হবে কিনা, এবং DeepSpeed এর স্তর
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # প্রশিক্ষণ এবং অপ্টিমাইজেশন পরামিতিগুলো একটি একক ডিকশনারি finetune_parameters এ সংযুক্ত করুন
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # foundation_model এর কোনও মডেল-নির্দিষ্ট ডিফল্ট পরামিতি আছে কিনা পরীক্ষা করুন
    # যদি থাকে, একটি সতর্কতা বার্তা মুদ্রণ করুন এবং finetune_parameters ডিকশনারি এই মডেল-নির্দিষ্ট ডিফল্ট পরামিতি দিয়ে আপডেট করুন
    # ast.literal_eval ফাংশনটি মডেল-নির্দিষ্ট ডিফল্টগুলোকে স্ট্রিং থেকে পাইথন ডিকশনারিতে রূপান্তর করার জন্য ব্যবহৃত হয়
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # স্ট্রিং থেকে পাইথন ডিকশনারিতে রূপান্তর করুন
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # রান করার জন্য ব্যবহার করা হবে এমন চূড়ান্ত ফাইন-টিউনিং পরামিতি সেট মুদ্রণ করুন
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### ট্রেনিং পাইপলাইন

১। এই পাইথন স্ক্রিপ্ট একটি মেশিন লার্নিং ট্রেনিং পাইপলাইনের ডিসপ্লে নাম তৈরি করার ফাংশন সংজ্ঞায়িত করছে এবং তারপর এই নাম তৈরি করে প্রিন্ট করছে। নিচে এর কার্যপদ্ধতির সংক্ষিপ্ত বিবরণ আছে:

১। get_pipeline_display_name ফাংশন সংজ্ঞায়িত হয়েছে। এটা ট্রেনিং পাইপলাইনের বিভিন্ন প্যারামিটার নির্ভর একটি ডিসপ্লে নাম তৈরি করে।

১। ফাংশনের ভিতরে এটি মোট ব্যাচ সাইজ হিসাব করে যা প্রতি-ডিভাইস ব্যাচ সাইজ, গ্রেডিয়েন্ট অ্যাকিউমুলেশন স্টেপসের সংখ্যা, প্রতি-নোড GPU সংখ্যা এবং ফাইনটিউনিংয়ের জন্য ব্যবহৃত নোড সংখ্যার গুণফল।

১। অন্য প্যারামিটারগুলো নেয় যেমন লার্নিং রেট স্কেজুলার টাইপ, DeepSpeed প্রয়োগ হয়েছে কিনা, DeepSpeed স্টেজ, Layer-wise Relevance Propagation (LoRa) ব্যবহার হয়েছে কিনা, মডেল চেকপয়েন্ট সংরক্ষণের সীমা, সর্বোচ্চ সিকোয়েন্স দৈর্ঘ্য।

১। একটি স্ট্রিং তৈরি করে যার মধ্যে এই সব প্যারামিটার থাকে, হাইফেন দিয়ে আলাদা। DeepSpeed বা LoRa প্রয়োগ হলে স্ট্রিংয়ে "ds" ও DeepSpeed স্টেজ অথবা "lora" থাকবে। না হলে "nods" বা "nolora" থাকবে।

১। ফাংশনটি সেই স্ট্রিং রিটার্ন করে যা ট্রেনিং পাইপলাইনের ডিসপ্লে নাম হিসেবে কাজ করে।

১। ফাংশন সংজ্ঞায়িত হওয়ার পর সেটি কল করে ডিসপ্লে নাম তৈরি করা হয় এবং প্রিন্ট করা হয়।

১। সংক্ষেপে, এই স্ক্রিপ্টটি বিভিন্ন ট্রেনিং প্যারামিটার বুঝে ট্রেনিং পাইপলাইনের ডিসপ্লে নাম তৈরি করে এবং প্রিন্ট করে।

    ```python
    # ট্রেনিং পাইপলাইনের জন্য একটি ডিসপ্লে নাম তৈরি করার জন্য একটি ফাংশন সংজ্ঞায়িত করুন
    def get_pipeline_display_name():
        # প্রতি-ডিভাইস ব্যাচ সাইজ, গ্রেডিয়েন্ট অ্যাকুমুলেশন স্টেপের সংখ্যা, প্রতি নোডের GPU এর সংখ্যা এবং ফাইন-টিউনিং এর জন্য ব্যবহৃত নোডের সংখ্যা গুণ করে মোট ব্যাচ সাইজ গণনা করুন
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # লার্নিং রেট শিডিউলার টাইপ রিট্রিভ করুন
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # DeepSpeed প্রয়োগ করা হয়েছে কিনা তা রিট্রিভ করুন
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # DeepSpeed এর স্টেজ রিট্রিভ করুন
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # যদি DeepSpeed প্রয়োগ করা হয়, ডিসপ্লে নামের মধ্যে "ds" এবং DeepSpeed স্টেজ অন্তর্ভুক্ত করুন; যদি না হয়, "nods" অন্তর্ভুক্ত করুন
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Layer-wise Relevance Propagation (LoRa) প্রয়োগ করা হয়েছে কিনা তা রিট্রিভ করুন
        lora = finetune_parameters.get("apply_lora", "false")
        # যদি LoRa প্রয়োগ করা হয়, ডিসপ্লে নামের মধ্যে "lora" অন্তর্ভুক্ত করুন; যদি না হয়, "nolora" অন্তর্ভুক্ত করুন
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # রাখা মডেল চেকপয়েন্টের সর্বোচ্চ সীমা রিট্রিভ করুন
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # সর্বোচ্চ সিকোয়েন্স লেন্থ রিট্রিভ করুন
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # সমস্ত এই প্যারামিটারকে হাইফেন দিয়ে পৃথক করে डिसপ্লে নাম গঠন করুন
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
    
    # ডিসপ্লে নাম তৈরি করার জন্য ফাংশন কল করুন
    pipeline_display_name = get_pipeline_display_name()
    # ডিসপ্লে নাম প্রিন্ট করুন
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### পাইপলাইন কনফিগার করা

এই পাইথন স্ক্রিপ্টটি Azure Machine Learning SDK ব্যবহার করে একটি মেশিন লার্নিং পাইপলাইন সংজ্ঞায়িত ও কনফিগার করছে। নিচে এর কার্যবিবরণ:

১। প্রয়োজনীয় মডিউলগুলো Azure AI ML SDK থেকে ইমপোর্ট করা হচ্ছে।

১। রেজিস্ট্রি থেকে “chat_completion_pipeline” নামের একটি পাইপলাইন কম্পোনেন্ট ফেচ করা হচ্ছে।

১। `@pipeline` ডেকোরেটর এবং `create_pipeline` ফাংশন ব্যবহার করে একটি পাইপলাইন জব সংজ্ঞায়িত করা হয়েছে। পাইপলাইনের নাম সেট করা হয়েছে `pipeline_display_name`।

১। `create_pipeline` ফাংশনের ভিতরে ফেচ করা কম্পোনেন্টটি বিভিন্ন প্যারামিটার দিয়ে ইনিশিয়ালাইজ করা হয়েছে, যার মধ্যে মডেল পাথ, ভিন্ন ধাপের জন্য কম্পিউট ক্লাস্টার, ট্রেনিং ও টেস্টিং ডেটাসেট স্প্লিট, ফাইনটিউনিংয়ের জন্য GPU সংখ্যা, এবং অন্যান্য ফাইনটিউনিং প্যারামিটার রয়েছে।

১। ফাইনটিউনিং জবের আউটপুটকে পাইপলাইন জবের আউটপুটের সাথে ম্যাপ করা হয়েছে। এতে ফাইনটিউন করা মডেলটি সহজে রেজিস্টার করা সম্ভব হয়, যা মডেল অনলাইন বা ব্যাচ এন্ডপয়েন্টে ডিপ্লয়ের জন্য দরকার।

১। `create_pipeline` ফাংশন কল করে পাইপলাইনের একটি ইন্সটেন্স তৈরি করা হয়েছে।

১। পাইপলাইনের `force_rerun` সেটিং `True` করা হয়েছে, অর্থাৎ পূর্বের কাজের ক্যাশ করা ফলাফল ব্যবহার করা হবে না।

১। পাইপলাইনের `continue_on_step_failure` সেটিং `False` করা হয়েছে, অর্থাৎ কোনো ধাপ ব্যর্থ হলে পাইপলাইন বন্ধ হবে।

১। সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning SDK ব্যবহার করে চ্যাট কমপ্লিশন টাস্কের জন্য একটি মেশিন লার্নিং পাইপলাইন সংজ্ঞায়িত ও কনফিগার করছে।

    ```python
    # Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলি ইম্পোর্ট করুন
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # রেজিস্ট্রি থেকে "chat_completion_pipeline" নামে পাইপলাইন কম্পোনেন্টটি আনুন
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline ডেকোরেটর এবং create_pipeline ফাংশন ব্যবহার করে পাইপলাইন কাজটি সংজ্ঞায়িত করুন
    # পাইপলাইনের নাম pipeline_display_name এ সেট করা হয়েছে
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # নানা প্যারামিটার দিয়ে আনুনকৃত পাইপলাইন কম্পোনেন্টটি ইনিশিয়ালাইজ করুন
        # এর মধ্যে রয়েছে মডেল পাথ, বিভিন্ন স্টেজের জন্য কম্পিউট ক্লাস্টার, প্রশিক্ষণ এবং পরীক্ষার জন্য ডেটাসেট বিভাজন, ফাইন-টিউনিংয়ের জন্য ব্যবহৃত GPU সংখ্যা এবং অন্যান্য ফাইন-টিউনিং প্যারামিটার
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # ডেটাসেট বিভাজনগুলো প্যারামিটারগুলোর সাথে ম্যাপ করুন
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # প্রশিক্ষণ সেটিংস
            number_of_gpu_to_use_finetuning=gpus_per_node,  # কম্পিউটে উপলব্ধ GPU সংখ্যায় সেট করুন
            **finetune_parameters
        )
        return {
            # ফাইন-টিউনিং কাজের আউটপুটকে পাইপলাইন কাজের আউটপুটের সাথে ম্যাপ করুন
            # এটি করা হয়েছে যাতে আমরা সহজেই ফাইন-টিউন করা মডেলটি রেজিস্টার করতে পারি
            # অনলাইন অথবা ব্যাচ এন্ডপয়েন্টে মডেল ডিপ্লয় করতে মডেল রেজিস্টার করা আবশ্যক
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline ফাংশন কল করে পাইপলাইনের একটি ইনস্ট্যান্স তৈরি করুন
    pipeline_object = create_pipeline()
    
    # আগের কাজগুলোর ক্যাশড ফলাফল ব্যবহার করবেন না
    pipeline_object.settings.force_rerun = True
    
    # স্টেপ ব্যর্থ হলে চালিয়ে যাওয়ার অপশন False সেট করুন
    # এর মানে হচ্ছে যেকোনো স্টেপ ব্যর্থ হলে পাইপলাইন বন্ধ হয়ে যাবে
    pipeline_object.settings.continue_on_step_failure = False
    ```

### জব সাবমিট করা

১। এই পাইথন স্ক্রিপ্টটি একটি Azure Machine Learning ওয়ার্কস্পেসে মেশিন লার্নিং পাইপলাইন জব সাবমিট করছে এবং জব সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করছে। নিচে তার কার্যবিবরণ:

   - এটি ওয়ার্কস্পেস_ml_client এর jobs অবজেক্টের create_or_update মেথড কল করে পাইপলাইন জব সাবমিট করে। চালাতে হবে এমন পাইপলাইন নির্দিষ্ট করা হয় pipeline_object দিয়ে, আর যেই পরীক্ষার অধীনে জব চলবে তা experiment_name দ্বারা।

   - এরপর jobs অবজেক্টের stream মেথড কল করে পাইপলাইন জব শেষ হওয়া পর্যন্ত অপেক্ষা করে। অপেক্ষা করার জবটি pipeline_job অবজেক্টের name অ্যাট্রিবিউট দ্বারা নির্ধারিত।

   - সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning ওয়ার্কস্পেসে একটি মেশিন লার্নিং পাইপলাইন জব সাবমিট করে এবং তার সমাপ্তি পর্যন্ত অপেক্ষা করে।

    ```python
    # Azure মেশিন লার্নিং ওয়ার্কস্পেসে পাইপলাইন কাজ জমা দিন
    # চালানোর জন্য পাইপলাইন pipeline_object দ্বারা নির্দিষ্ট করা হয়েছে
    # যে পরীক্ষা অধীনে কাজটি চালানো হয় তা experiment_name দ্বারা নির্দিষ্ট করা হয়েছে
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # পাইপলাইন কাজ সম্পন্ন হওয়ার জন্য অপেক্ষা করুন
    # অপেক্ষা করার কাজ pipeline_job অবজেক্টের name বৈশিষ্ট্য দ্বারা নির্দিষ্ট করা হয়েছে
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## ৬। ফাইন টিউন করা মডেল ওয়ার্কস্পেসে রেজিস্টার করা

আমরা ফাইন টিউনিং জবের আউটপুট থেকে মডেল রেজিস্টার করব। এতে ফাইন টিউন করা মডেল এবং জবের মধ্যে লাইনেজ ট্র্যাক হবে। ফাইন টিউনিং জব ফাউন্ডেশন মডেল, ডেটা এবং ট্রেনিং কোডের লাইনেজও ট্র্যাক করে।

### এমএল মডেল রেজিস্টার করা

১। এই পাইথন স্ক্রিপ্ট একটি Azure Machine Learning পাইপলাইনে ট্রেন করা মেশিন লার্নিং মডেল রেজিস্টার করছে। নিচে কার্যক্রমের সংক্ষিপ্ত বিবরণ:

   - এটি Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলো ইমপোর্ট করে।

   - পাইপলাইন জব থেকে trained_model আউটপুট পাওয়া যাচ্ছে কিনা তা যাচাই করতে workspace_ml_client এর jobs অবজেক্টের get মেথড কল করে এবং তার outputs অ্যাট্রিবিউটে অ্যাক্সেস নেয়।

   - একটি পাথ তৈরি করে যেখানে ট্রেন করা মডেল আছে, এটি পাথ ফরম্যাট করে পাইপলাইন জবের নাম এবং আউটপুটের নাম ("trained_model") দিয়ে।

   - ফাইন টিউন করা মডেলের নাম সংজ্ঞায়িত করছে, যেখানে মূল মডেলের নামের সাথে "-ultrachat-200k" যুক্ত করে এবং স্ল্যাশ গুলো হাইফেন দিয়ে প্রতিস্থাপন করে।

   - মডেল রেজিস্টার করতে Model অবজেক্ট তৈরি করছে বিভিন্ন প্যারামিটারসহ, যেমন মডেলের পাথ, মডেলের ধরন (MLflow মডেল), মডেলের নাম এবং ভার্সন, এবং মডেলের বিবরণ।

   - workspace_ml_client এর models অবজেক্টের create_or_update মেথড কল করে Model অবজেক্ট দিয়ে মডেলটি রেজিস্টার করছে।

   - রেজিস্টার করা মডেলটি প্রিন্ট করছে।

১। সংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning পাইপলাইনে ট্রেন করা একটি মেশিন লার্নিং মডেল রেজিস্টার করছে।
    
    ```python
    # Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলি আমদানি করুন
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # চেক করুন যে পাইপলাইন জব থেকে `trained_model` আউটপুটটি পাওয়া গেছে কিনা
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # পাইপলাইন জবের নাম এবং আউটপুটের নাম ("trained_model") দিয়ে একটি স্ট্রিং ফরম্যাট করে ট্রেইন্ড মডেলের পথ তৈরি করুন
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # মূল মডেলের নামের সাথে "-ultrachat-200k" যোগ করে এবং যেকোনো স্ল্যাশকে হাইফেনে পরিবর্তন করে ফাইন-টিউনড মডেলের জন্য একটি নাম নির্ধারণ করুন
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # বিভিন্ন প্যারামিটার সহ একটি Model অবজেক্ট তৈরি করে মডেলটি রেজিস্টার করার জন্য প্রস্তুতি নিন
    # এর মধ্যে আছে মডেলের পথ, মডেলের ধরন (MLflow মডেল), মডেলের নাম এবং সংস্করণ, এবং মডেলের বর্ণনা
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # সংস্করণের সংঘর্ষ এড়াতে টাইমস্ট্যাম্পকে সংস্করণ হিসেবে ব্যবহার করুন
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Model অবজেক্টটি আর্গুমেন্ট হিসাবে নিয়ে workspace_ml_client এর models অবজেক্টের create_or_update মেথড কল করে মডেল রেজিস্টার করুন
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # রেজিস্টারকৃত মডেলটি প্রিন্ট করুন
    print("registered model: \n", registered_model)
    ```

## ৭। ফাইন টিউন করা মডেল অনলাইন এন্ডপয়েন্টে ডিপ্লয় করা

অনলাইন এন্ডপয়েন্ট একটি স্থায়ী REST API প্রদান করে যা মডেল ব্যবহার করতে চাওয়া অ্যাপ্লিকেশনগুলোর সাথে ইন্টিগ্রেশনের জন্য ব্যবহৃত হয়।

### এন্ডপয়েন্ট পরিচালনা

১। এই পাইথন স্ক্রিপ্ট একটি রেজিস্টারকৃত মডেলের জন্য Azure Machine Learning-এ একটি Managed Online Endpoint তৈরি করছে। কার্যবিবরণ:

   - Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলো ইমপোর্ট করা।

   - অনলাইন এন্ডপয়েন্টের জন্য একটি ইউনিক নাম সংজ্ঞায়িত করা, "ultrachat-completion-" স্ট্রিংয়ের সাথে টাইমস্ট্যাম্প যোগ করে।

   - ManagedOnlineEndpoint অবজেক্ট তৈরি করে অনলাইন এন্ডপয়েন্ট তৈরির প্রস্তুতি নিচ্ছে যার মধ্যে এন্ডপয়েন্টের নাম, বিবরণ, এবং অথেন্টিকেশন মোড ("key") আছে।

   - workspace_ml_client এর begin_create_or_update মেথড কল করে ManagedOnlineEndpoint অবজেক্ট দিয়ে এন্ডপয়েন্ট তৈরি করছে এবং wait মেথড দিয়ে অপারেশনটি সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করছে।

১। সংক্ষেপে, এই স্ক্রিপ্ট একটি রেজিস্টারকৃত মডেলের জন্য Azure Machine Learning-এ managed online endpoint তৈরি করছে।

    ```python
    # Azure AI ML SDK থেকে প্রয়োজনীয় মডিউলগুলি আমদানি করুন
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" স্ট্রিংটির সাথে একটি টাইমস্ট্যাম্প যুক্ত করে অনলাইন এন্ডপয়েন্টের একটি অনন্য নাম নির্ধারণ করুন
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # বিভিন্ন প্যারামিটার সহ একটি ManagedOnlineEndpoint অবজেক্ট তৈরি করে অনলাইন এন্ডপয়েন্ট তৈরি করার প্রস্তুতি নিন
    # এর মধ্যে এন্ডপয়েন্টের নাম, এন্ডপয়েন্টের বিবরণ, এবং প্রমাণীকরণ পদ্ধতি ("key") অন্তর্ভুক্ত রয়েছে
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint অবজেক্টকে আর্গুমেন্ট হিসেবে নিয়ে workspace_ml_client এর begin_create_or_update মেথড কল করে অনলাইন এন্ডপয়েন্ট তৈরি করুন
    # তারপর wait মেথড কল করে তৈরি করার অপারেশন সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করুন
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> আপনি এখানে দেখতে পারেন ডিপ্লয়মেন্টের জন্য সাপোর্টকৃত SKU এর তালিকা - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### এমএল মডেল ডিপ্লয় করা

১। এই পাইথন স্ক্রিপ্ট একটি রেজিস্টারকৃত মডেলকে Azure Machine Learning এর managed online endpoint-এ ডিপ্লয় করছে। কার্যবিবরণ:

   - এটি ast মডিউল ইমপোর্ট করে, যা পাইথনের অ্যাবস্ট্রাক্ট সিনট্যাক্স গ্রামার ট্রি প্রক্রিয়া করার ফাংশন দেয়।

   - ডিপ্লয়মেন্টের জন্য ইনস্ট্যান্স টাইপ "Standard_NC6s_v3" সেট করছে।

   - foundation_model এর মধ্যে inference_compute_allow_list ট্যাগ আছে কিনা পরীক্ষা করছে। থাকলে ট্যাগটি স্ট্রিং থেকে পাইথন লিস্টে রূপান্তর করে inference_computes_allow_list-এ রাখে, না থাকলে None সেট করে।

   - নির্দিষ্ট ইনস্ট্যান্স টাইপটি allow list-এ আছে কিনা যাচাই করে। না থাকলে ইউজারকে একটি ম্যাসেজ প্রিন্ট করে বলে allow list- থেকে ইনস্ট্যান্স টাইপ নির্বাচন করতে।

   - ManagedOnlineDeployment অবজেক্ট তৈরি করে ডিপ্লয়মেন্টের প্রস্তুতি নিচ্ছে, যার মধ্যে ডিপ্লয়মেন্টের নাম, এন্ডপয়েন্টের নাম, মডেলের আইডি, ইনস্ট্যান্স টাইপ ও কাউন্ট, লিভনেস প্রোব সেটিংস এবং রিকোয়েস্ট সেটিংস আছে।

   - workspace_ml_client এর begin_create_or_update মেথড কল করে ডিপ্লয়মেন্ট তৈরি করছে এবং wait মেথড দিয়ে অপেক্ষা করছে।

   - এন্ডপয়েন্টের ট্রাফিক সেট করে ১০০% ট্রাফিক "demo" ডিপ্লয়মেন্টের দিকে নির্দেশ করে।

   - এন্ডপয়েন্ট আপডেট করতে begin_create_or_update মেথড আবার কল করে এবং result মেথড দিয়ে অপেক্ষা করে।

১। সংক্ষেপে, এই স্ক্রিপ্ট একটি রেজিস্টারকৃত মডেলকে Azure Machine Learning এ managed online endpoint-এ ডিপ্লয় করছে।

    ```python
    # ast মডিউল আমদানি করুন, যা পাইথনের আবস্ট্রাক্ট সিনট্যাক্স ব্যাকরণের গাছ প্রক্রিয়াকরণের ফাংশন সরবরাহ করে
    import ast
    
    # ডিপ্লয়মেন্টের জন্য ইনস্ট্যান্স টাইপ সেট করুন
    instance_type = "Standard_NC6s_v3"
    
    # ফাউন্ডেশন মডেলে `inference_compute_allow_list` ট্যাগটি আছে কিনা পরীক্ষা করুন
    if "inference_compute_allow_list" in foundation_model.tags:
        # যদি থাকে, ট্যাগের মানকে স্ট্রিং থেকে পাইথন তালিকায় রূপান্তর করুন এবং `inference_computes_allow_list` তে অ্যাসাইন করুন
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # যদি না থাকে, `inference_computes_allow_list` কে `None` সেট করুন
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # নির্দিষ্ট ইনস্ট্যান্স টাইপটি অনুমোদিত তালিকায় আছে কিনা পরীক্ষা করুন
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # বিভিন্ন প্যারামিটার দিয়ে একটি `ManagedOnlineDeployment` অবজেক্ট তৈরি করে ডিপ্লয়মেন্ট তৈরির প্রস্তুতি নিন
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `ManagedOnlineDeployment` অবজেক্টকে আর্গুমেন্ট হিসেবে দিয়ে `workspace_ml_client` এর `begin_create_or_update` মেথড কল করে ডিপ্লয়মেন্ট তৈরি করুন
    # তারপর `wait` মেথড কল করে ডিপ্লয়মেন্ট তৈরির অপারেশন শেষ হওয়া পর্যন্ত অপেক্ষা করুন
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # এন্ডপয়েন্টের ট্র্যাফিক সেট করুন যাতে ১০০% ট্র্যাফিক "demo" ডিপ্লয়মেন্টে যায়
    endpoint.traffic = {"demo": 100}
    
    # `endpoint` অবজেক্ট দিয়ে `workspace_ml_client` এর `begin_create_or_update` মেথড কল করে এন্ডপয়েন্ট আপডেট করুন
    # তারপর `result` মেথড কল করে আপডেট অপারেশন সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করুন
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## ৮। স্যাম্পল ডেটা দিয়ে এন্ডপয়েন্ট পরীক্ষা

আমরা টেস্ট ডেটাসেট থেকে কিছু স্যাম্পল ডেটা নিয়ে অনলাইন এন্ডপয়েন্টে ইনফারেন্সের জন্য সাবমিট করব। তারপর স্কোর করা লেবেলগুলো এবং গ্রাউন্ড ট্রুথ লেবেলগুলো দেখাবো।

### রেজাল্ট পড়া

১। এই পাইথন স্ক্রিপ্টটি একটি JSON Lines ফাইল pandas DataFrame-এ পড়ে, একটি র্যান্ডম স্যাম্পল নেয় এবং ইনডেক্স রিসেট করে। কার্যক্রমের সংক্ষিপ্ত বিবরণ:

   - এটি ./ultrachat_200k_dataset/test_gen.jsonl ফাইলটি pandas DataFrame-এ পড়ে। read_json ফাংশন lines=True আর্গুমেন্টের সাথে ব্যবহার করা হয়েছে কারণ ফাইলটি JSON Lines ফরম্যাটে, যেখানে প্রতিটি লাইন একটি আলাদা JSON অবজেক্ট।

   - DataFrame থেকে একটি র্যান্ডম স্যাম্পল নেয় ১টি সারি। sample ফাংশনে n=1 আর্গুমেন্ট দেওয়া হয়।

   - DataFrame-এর ইনডেক্স রিসেট করে। reset_index ফাংশনে drop=True ব্যবহার করে মূল ইনডেক্স বাদ দিয়ে একটি নতুন ডিফল্ট পূর্ণসংখ্যার ইনডেক্স তৈরি হয়।

   - head ফাংশনের মাধ্যমে DataFrame-এর প্রথম ২টি সারি প্রদর্শন করে। যেহেতু স্যাম্পল নেওয়ার পর মাত্র এক সারি আছে, তাই শুধু ঐ এক সারি প্রদর্শিত হবে।

১। সংক্ষেপে, এই স্ক্রিপ্ট একটি JSON Lines ফাইল pandas DataFrame-এ পড়ে, একটি র্যান্ডম ১ সারির স্যাম্পল নেয়, ইনডেক্স রিসেট করে এবং প্রথম সারিটি প্রদর্শন করে।
    
    ```python
    # pandas লাইব্রেরি ইমপোর্ট করুন
    import pandas as pd
    
    # JSON Lines ফাইল './ultrachat_200k_dataset/test_gen.jsonl' একটি pandas DataFrame এ পড়ুন
    # 'lines=True' আর্গুমেন্টটি নির্দেশ করে যে ফাইলটি JSON Lines ফরম্যাটে, যেখানে প্রতিটি লাইন একটি আলাদা JSON অবজেক্ট
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame থেকে ১টি র্যান্ডম সারি নিন
    # 'n=1' আর্গুমেন্টটি র্যান্ডমভাবে নির্বাচন করার জন্য সারির সংখ্যা নির্দেশ করে
    test_df = test_df.sample(n=1)
    
    # DataFrame এর ইনডেক্স রিসেট করুন
    # 'drop=True' আর্গুমেন্টটি নির্দেশ করে যে মূল ইনডেক্সটি ফেলে দিয়ে একটি নতুন ডিফল্ট পূর্ণসংখ্যার ইনডেক্স ব্যবহার করা হবে
    # 'inplace=True' আর্গুমেন্টটি নির্দেশ করে যে DataFrame সরাসরি পরিবর্তিত হবে (নতুন অবজেক্ট তৈরি না করে)
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame এর প্রথম ২টি সারি প্রদর্শন করুন
    # তবে, যেহেতু স্যাম্পলিংয়ের পর DataFrame শুধুমাত্র একটি সারি রয়েছে, এটি শুধুমাত্র ওই একটি সারি দেখাবে
    test_df.head(2)
    ```

### JSON অবজেক্ট তৈরি করা

১। এই পাইথন স্ক্রিপ্ট নির্দিষ্ট প্যারামিটারসহ একটি JSON অবজেক্ট তৈরি করছে এবং সেটি একটি ফাইলে সংরক্ষণ করছে। কার্যবিবরণ:

   - এটি json মডিউল ইমপোর্ট করে, যা JSON ডেটা নিয়ে কাজ করার ফাংশন সরবরাহ করে।
    - এটি একটি dictionary তৈরি করে যার কী এবং মান মেশিন লার্নিং মডেলের জন্য প্যারামিটার উপস্থাপন করে। কী গুলো হলো "temperature", "top_p", "do_sample", এবং "max_new_tokens", এবং তাদের যথাক্রম মান হলো 0.6, 0.9, True, এবং 200।

    - এটি আরেকটি dictionary তৈরি করে যার নাম test_json এবং দুইটি কী রয়েছে: "input_data" এবং "params"। "input_data" এর মান আরেকটি dictionary যা কী "input_string" এবং "parameters" ধারণ করে। "input_string" এর মান হলো প্রথম বার্তা যা test_df DataFrame থেকে নেয়া হয়েছে। "parameters" এর মান হলো পূর্বে তৈরিকৃত parameters dictionary। "params" এর মান একটি খালি dictionary।

    - এটি sample_score.json নামে একটি ফাইল খুলে
    
    ```python
    # json মডিউল ইম্পোর্ট করুন, যা JSON ডেটার সাথে কাজ করার জন্য ফাংশন সরবরাহ করে
    import json
    
    # একটি ডিকশনারি `parameters` তৈরি করুন যার কী এবং মানগুলি একটি মেশিন লার্নিং মডেলের প্যারামিটার প্রতিনিধিত্ব করে
    # কীগুলি হল "temperature", "top_p", "do_sample", এবং "max_new_tokens", এবং তাদের সংশ্লিষ্ট মানগুলি যথাক্রমে 0.6, 0.9, True, এবং 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # আরেকটি ডিকশনারি `test_json` তৈরি করুন যার দুইটি কী: "input_data" এবং "params"
    # "input_data" এর মান অন্য একটি ডিকশনারি যার কীগুলি "input_string" এবং "parameters"
    # "input_string" এর মান একটি তালিকা যা `test_df` DataFrame থেকে প্রথম মেসেজটি ধারণ করে
    # "parameters" এর মান হল পূর্বে তৈরি করা `parameters` ডিকশনারি
    # "params" এর মান একটি খালি ডিকশনারি
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` ডিরেক্টরিতে `sample_score.json` নামের একটি ফাইল লেখার মোডে খুলুন
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` ফাংশন ব্যবহার করে `test_json` ডিকশনারিটি JSON ফরম্যাটে ফাইলে লিখুন
        json.dump(test_json, f)
    ```

### Endpoint কল করা

1. এই পাইথন স্ক্রিপ্টটি একটি অনলাইন এন্ডপয়েন্টকে Azure Machine Learning এ JSON ফাইল স্কোর করার জন্য কল করছে। এর কাজের একটি বিবরণ:

    - এটি workspace_ml_client অবজেক্টের online_endpoints প্রোপার্টির invoke মেথড কল করে। এই মেথড অনলাইন এন্ডপয়েন্টে রিকোয়েস্ট পাঠাতে এবং রেসপন্স পেতে ব্যবহৃত হয়।

    - এটি endpoint_name এবং deployment_name আর্গুমেন্টের মাধ্যমে এন্ডপয়েন্ট এবং ডিপ্লয়মেন্টের নাম নির্দিষ্ট করে। এখানে, এন্ডপয়েন্টের নাম online_endpoint_name ভেরিয়েবলে রাখা হয়েছে এবং ডিপ্লয়মেন্টের নাম "demo"।

    - এটি request_file আর্গুমেন্টের মাধ্যমে স্কোর করার JSON ফাইলটির পাথ নির্দিষ্ট করে। এই ক্ষেত্রে, ফাইলটির পাথ হলো ./ultrachat_200k_dataset/sample_score.json।

    - এটি এন্ডপয়েন্ট থেকে প্রাপ্ত রেসপন্স response ভেরিয়েবলে সংরক্ষণ করে।

    - এটি কাঁচা রেসপন্স প্রিন্ট করে।

1. সারসংক্ষেপে, এই স্ক্রিপ্টটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্টকে JSON ফাইল স্কোর করার জন্য কল করছে এবং রেসপন্স প্রিন্ট করছে।

    ```python
    # Azure Machine Learning এ অনলাইন এন্ডপয়েন্ট কল করুন `sample_score.json` ফাইল স্কোর করার জন্য
    # `workspace_ml_client` অবজেক্টের `online_endpoints` প্রপার্টির `invoke` মেথড ব্যবহার করে অনলাইন এন্ডপয়েন্টে রিকোয়েস্ট পাঠানো হয় এবং রেসপন্স পাওয়া যায়
    # `endpoint_name` আর্গুমেন্ট এন্ডপয়েন্টের নাম নির্দিষ্ট করে, যেটি `online_endpoint_name` ভেরিয়েবলে সংরক্ষিত
    # `deployment_name` আর্গুমেন্ট ডিপ্লয়মেন্টের নাম নির্দিষ্ট করে, যেটি "demo"
    # `request_file` আর্গুমেন্ট সেই JSON ফাইলের পথ নির্দিষ্ট করে যা স্কোর করা হবে, যেটি `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # এন্ডপয়েন্ট থেকে প্রাপ্ত কাঁচা রেসপন্স প্রিন্ট করুন
    print("raw response: \n", response, "\n")
    ```

## 9. অনলাইন এন্ডপয়েন্ট মুছে ফেলা

1. অনলাইন এন্ডপয়েন্টটি মুছে ফেলতে ভুলবেন না, নাহলে এন্ডপয়েন্ট দ্বারা ব্যবহৃত কম্পিউটের জন্য বিলিং চলতে থাকবে। এই পাইথন কোডটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্ট মুছে ফেলার জন্য ব্যবহৃত হয়। এর কাজের বিবরণ:

    - এটি workspace_ml_client অবজেক্টের online_endpoints প্রোপার্টির begin_delete মেথড কল করে। এই মেথড অনলাইন এন্ডপয়েন্ট মুছে ফেলার প্রক্রিয়া শুরু করার জন্য ব্যবহৃত হয়।

    - এটি name আর্গুমেন্টের মাধ্যমে যে এন্ডপয়েন্টটি মুছে ফেলতে হবে তার নাম নির্দিষ্ট করে। এখানে, এন্ডপয়েন্টের নাম online_endpoint_name ভেরিয়েবলে রাখা হয়েছে।

    - এটি wait মেথড কল করে মুছে ফেলার প্রক্রিয়া সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করে। এটি একটি ব্লকিং অপারেশন, অর্থাৎ মুছে ফেলা শেষ না হওয়া পর্যন্ত স্ক্রিপ্ট চালু থাকবে না।

    - সারসংক্ষেপে, এই লাইন কোডটি Azure Machine Learning এ একটি অনলাইন এন্ডপয়েন্ট মুছে ফেলার প্রক্রিয়া শুরু করছে এবং অপারেশন সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করছে।

    ```python
    # Azure Machine Learning এ অনলাইন এন্ডপয়েন্ট মোছা হচ্ছে
    # `workspace_ml_client` অবজেক্টের `online_endpoints` প্রপার্টির `begin_delete` মেথড ব্যবহার করে একটি অনলাইন এন্ডপয়েন্ট মোছার প্রক্রিয়া শুরু করা হয়
    # `name` আর্গুমেন্টটি মোছার জন্য এন্ডপয়েন্টের নাম নির্দিষ্ট করে, যা `online_endpoint_name` ভেরিয়েবলে সংরক্ষিত থাকে
    # `wait` মেথড কল করা হয় মোছার অপারেশন শেষ হওয়ার জন্য অপেক্ষা করতে। এটি একটি ব্লকিং অপারেশন, অর্থাৎ মোছা শেষ না হওয়া পর্যন্ত স্ক্রিপ্ট চালিয়ে যেতে পারে না
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বস্টববাক্য**:  
এটি একটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত ডকুমেন্ট। আমরা সঠিকতার জন্য চেষ্টা করি, কিন্তু স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথির নিজস্ব ভাষার রূপটি সর্বজন গ্রহণযোগ্য উৎস হিসেবে গণ্য করাই উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা অপব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->