## Azure ML စနစ်မှ စနစ်မှတ်ပုံတင်ထားသော chat-completion အစိတ်အပိုင်းများကို အသုံးပြုပြီး မော်ဒယ်တစ်ခုကို fine tune ပြုလုပ်နည်း

ဥပမာ၌ Phi-3-mini-4k-instruct မော်ဒယ်ကို ultrachat_200k ဒေတာစုစည်းမှုကို အသုံးပြု၍ လူနှစ်ဦးအကြား စကားစမြည် ပြီးစီးအောင် fine tuning ပြုလုပ်မည်ဖြစ်သည်။

![MLFineTune](../../../../translated_images/my/MLFineTune.928d4c6b3767dd35.webp)

ဤဥပမာတွင် Azure ML SDK နှင့် Python ကို အသုံးပြု၍ fine tuning ပြုလုပ်သည့်နည်းလမ်းကို ပြသပေးမည်ဖြစ်ပြီး၊ fine tuned မော်ဒယ်ကို အချိန်နောက်ခံမှတ်တမ်းဆိုင်ရာ inference အတွက် အွန်လိုင်း endpoint တစ်ခုသို့ ဖြန့်ချိခြင်းလည်း ပြသမည်။

### လေ့ကျင့်သည့် ဒေတာ

ultrachat_200k ဒေတာစုစည်းမှုကို အသုံးပြုမည်ဖြစ်သည်။ ၎င်းသည် UltraChat ဒေတာစုစည်းမှု၏ စစ်ထုတ်ထားသော ဗားရှင်းဖြစ်ပြီး Zephyr-7B-β အတွက် လေ့ကျင့်မှုတွင် အသုံးပြုခဲ့သော 7b ဖော်မြူလာ၏လက်ရှိ နိဒါန်းဖြစ်သည်။

### မော်ဒယ်

chat-completion လုပ်ငန်းအတွက် ဖင်တည်းဖြစ်အောင် Phi-3-mini-4k-instruct မော်ဒယ်ကို အသုံးပြုမည်။ သင်ဤ notebook ကို ထူးခြားသော မော်ဒယ်ကဒ်မှဖွင့်လှစ်ကာ သုံးနေပါက မော်ဒယ်နာမည်ကို သင့်တော်စွာ ပြောင်းလဲပါ။

### အလုပ်များ

- fine tune ပြုလုပ်မည့် မော်ဒယ်ကို ရွေးချယ်ပါ။
- လေ့ကျင့်ဒေတာကို ရွေးချယ်၍ လေ့လာပါ။
- fine tuning အလုပ်ကို ဖွဲ့စည်းပါ။
- fine tuning အလုပ်ကို တက်လုပ်ပါ။
- လေ့ကျင့်မှုနှင့် အကဲဖြတ်မှု စံနှုန်းများကို ပြန်လည်သုံးသပ်ပါ။
- fine tuned မော်ဒယ်ကို စနစ် မှတ်တမ်းတင်ပါ။
- fine tuned မော်ဒယ်ကို အချိန်နောက်ခံမှတ်တမ်းဆိုင်ရာ inference အတွက် ဖြန့်ချိပါ။
- အရင်းအမြစ်များကို သန့်ရှင်းပါ။

## ၁။ မလိုအပ်သည်များကို ပြင်ဆင်ခြင်း

- အချည်းနှီးပစ္စည်းများ 설치 설치
- AzureML Workspace နှင့် ချိတ်ဆက်ပါ။ SDK authentication ချိန်ညှိခြင်းကို လေ့လာပါ။ <WORKSPACE_NAME>, <RESOURCE_GROUP>, <SUBSCRIPTION_ID> ကို အောက်တွင် ပြောင်းပေးပါ။
- azureml system registry နှင့် ချိတ်ဆက်ပါ။
- ရွေးချယ်စရာ experiment နာမည်တစ်ခု သတ်မှတ်ပါ။
- စစ်ဆေးရန် သို့မဟုတ် create compute.

> [!NOTE]
> တစ်ခုတည်းသော GPU node သည် များစွာသော GPU ကဒ်များရှိနိုင်သည်။ ဥပမာ- Standard_NC24rs_v3 တစ်ခုတွင် NVIDIA V100 GPUs ၄ လုံးရှိပြီး Standard_NC12s_v3 တစ်ခုတွင် NVIDIA V100 GPUs ၂ လုံးရှိသည်။ ယင်းအချက်အလက်များကို docs တွင်ကြည့်ပါ။ GPU ကဒ် အရေအတွက်ကို param gpus_per_node တွင် သတ်မှတ်သည်။ တိကျစွာ သတ်မှတ်ခြင်းဖြင့် node တွင်ရှိသော GPU များအားလုံးကို အသုံးပြုနိုင်မည်ဖြစ်သည်။ အကြံပြု GPU compute SKU များကို ဒီနေရာနှင့် ဒီနေရာတွင် ရှာဖွေကြည့်နိုင်သည်။

### Python လိုင်ဘရေးရီများ

အောက်ပါ cell ကို run ခြင်းဖြင့် လိုအပ်သော အကြံပြုချက်များကို install လုပ်ပါ။ အသစ်သော environment တွင် အဆိုပါ လုပ်ဆောင်မှုသည် မစွန့်လွှတ်သင့်ပါ။

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML နှင့် ဆက်သွယ်ခြင်း

၁။ ဤ Python script ကို Azure Machine Learning (Azure ML) ဝန်ဆောင်မှုနှင့် ဆက်သွယ်ရန် အသုံးပြုသည်။ လုပ်ဆောင်ချက်များမှာ -

- azure.ai.ml, azure.identity, နှင့် azure.ai.ml.entities package များမှ လိုအပ်သော module များကို import ပြုလုပ်သည်။ အပြင် time module ကိုလည်း import လုပ်သည်။

- DefaultAzureCredential() ဖြင့် authentication ပြုလုပ်ရန် ကြိုးစားသည်။ မအောင်မြင်ပါက၊ InteractiveBrowserCredential() ဖြင့် အပြန်အလှန် login များကို ဖော်ပြသည်။

- from_config method ကို အသုံးပြု၍ default config ဖိုင် (config.json) မှ configuration ကို ဖတ်၍ MLClient instance တစ်ခု ဖန်တီးရန် ကြိုးစားသည်။ မအောင်မြင်ပါက subscription_id, resource_group_name, workspace_name ကို manually ထည့်သွင်း၍ MLClient instance တစ်ခု ဖန်တီးသည်။

- "azureml" ဟု အမည်ပေးထားသော Azure ML registry အတွက် MLClient instance ကို တစ်ခု ဖန်တီးသည်။ ၎င်းမှာ မော်ဒယ်များ၊ fine-tuning pipelines နှင့် environments များကို သိမ်းဆည်းရာဖြစ်သည်။

- experiment_name ကို "chat_completion_Phi-3-mini-4k-instruct" ဟု သတ်မှတ်သည်။

- ယခုအချိန် (epoch များအရ စက္ကန့်အဖြစ် float ရှိ) ကို integer သို့ ပြောင်း၍ string အဖြစ် ပြောင်းထုတ်ကာ ယင်းကို သက်ဆိုင်ရာ နာမည်များ၊ ဗားရှင်းများ ဖန်တီးရာတွင် အသုံးပြုသည်။

    ```python
    # Azure ML နှင့် Azure Identity မှ လိုအပ်သော module များ import ပြုလုပ်ခြင်း
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # time module ကို import ပြုလုပ်ခြင်း
    
    # DefaultAzureCredential ကို အသုံးပြု၍ authentication လုပ်ရန် ကြိုးစားခြင်း
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # DefaultAzureCredential မအောင်မြင်ပါက InteractiveBrowserCredential ကို အသုံးပြုရန်
        credential = InteractiveBrowserCredential()
    
    # ပုံမှန် config ဖိုင်ကို အသုံးပြု၍ MLClient instance တစ်ခု ဖန်တီးရန် ကြိုးစားခြင်း
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # အဲဒါ မအောင်မြင်ပါက အသေးစိတ်ချက်များကို manually ဖြည့်သွင်း၍ MLClient instance တစ်ခု ဖန်တီးခြင်း
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" ဟု အမည်ပေးထားသော Azure ML registry အတွက် MLClient instance များ တစ်ခု ထပ်မံဖန်တီးခြင်း
    # ဤ registry တွင် မော်ဒယ်များ၊ fine-tuning pipeline များနှင့် ပတ်ဝန်းကျင်များကို သိမ်းဆည်းထားသည်
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # စမ်းသပ်မှုအမည် သတ်မှတ်ခြင်း
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # အမည်နှင့် ဗားရှင်းတို့အတွက် ထူးခြားသော timestamp တွက်ရန် ဖန်တီးခြင်း
    timestamp = str(int(time.time()))
    ```

## ၂။ fine tune ပြုလုပ်ရန် အခြေခံမော်ဒယ် ရွေးချယ်ခြင်း

၁။ Phi-3-mini-4k-instruct သည် 3.8B parameters, အလွယ်တကူ ရွှေ့ပြောင်းနိုင်သော၊ Phi-2 အတွက် သုံးခဲ့သော ဒေတာများအပေါ် အခြေခံထားသော ဖွံ့ဖြိုးတိုးတက်သော open မော်ဒယ်ဖြစ်သည်။ မော်ဒယ်သည် Phi-3 မော်ဒယ် မျိုးဆက်တွင်ပါဝင်ပြီး Mini ဗားရှင်းတွင် 4K နှင့် 128K context length (tokens အရေအတွက်) ရှိသည်။ သဘော: မော်ဒယ်ကို အသုံးပြုရန် သင့်ရည်ရွယ်ချက်အတွက် fine tune လုပ်ရန် လိုအပ်သည်။ သင်သည် AzureML Studio တွင် Model Catalog ဖြင့် chat-completion task အတွက် မော်ဒယ်များကို ရွေးချယ်နိုင်သည်။ ဤအချက် အစုတွင် Phi-3-mini-4k-instruct မော်ဒယ်ကို သုံးမည်။ မသင့်တော်သည့် မော်ဒယ်အတွက် notebook ဖွင့်ထားသူများသည် မော်ဒယ်နာမည်နှင့် ဗားရှင်းကို သင့်တော်စွာ ပြောင်းလဲပါ။

> [!NOTE]
> မော်ဒယ်၏ id property ဖြစ်သော asset id ကို fine tuning job တွင် input အဖြစ် ပေးပို်မည်။ AzureML Studio Model Catalog ၏ မော်ဒယ်အသေးစိတ် စာမျက်နှာတွင် Asset ID အဖြစ်ပါဝင်သည်။

၂။ ဤ Python script သည် Azure Machine Learning (Azure ML) ဝန်ဆောင်မှုနှင့် ဆက်သွယ်ရာတွင် အသုံးပြုသည်။ လုပ်ဆောင်ချက်များမှာ -

- model_name ကို "Phi-3-mini-4k-instruct" ဟု သတ်မှတ်သည်။

- registry_ml_client ၏ models property ၏ get method ကို အသုံးပြုပြီး Azure ML registry မှ မော်ဒယ်နာမည်နှင့် label သတ်မှတ်ခြင်းဖြင့် မော်ဒယ်၏ နောက်ဆုံးဗားရှင်းကို ရယူသည်။

- consoleတွင် fine-tuning အတွက် အသုံးပြုမည့် မော်ဒယ်၏ name, version, id ကို စာသား မက်ဆေ့ခ်ျပုံစံဖြင့် print ပြုလုပ်သည်။ foundation_model ၏ properties များအား အသုံးပြု၍ ဖော်ပြသည်။

    ```python
    # မော်ဒယ်နာမည်သတ်မှတ်ပါ
    model_name = "Phi-3-mini-4k-instruct"
    
    # Azure ML မှာရှိတဲ့ မော်ဒယ်နောက်ဆုံးဗားရှင်းကိုရယူပါ
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # မော်ဒယ်နာမည်၊ ဗားရှင်းနဲ့ id ကိုပရင့်ထုတ်ပါ
    # ဒီသတင်းအချက်အလက်တွေက တိုက်ရိုက်စောင့်ကြည့်ခြင်းနဲ့ အမှားရှာဖွေနိုင်ဖို့ အသုံးဝင်ပါတယ်
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## ၃။ အလုပ်အတွက် compute တစ်ခုဖန်တီးခြင်း

finetune အလုပ်သည် GPU compute ဖြင့်သာ လည်ပတ်သည်။ compute ၏ အရွယ်အစားမှာ မော်ဒယ်၏ အရွယ်မူအပေါ်မူတည်ပြီး မတူညီနိုင်သည်။ ဒီ cell တွင် အသုံးပြုသူအား အလုပ်အတွက် သင့်တော်သော compute ကို ရွေးချယ်ရန် လမ်းညွှန်ပေးသည်။

> [!NOTE]
> အောက်ပါ compute များသည် အပေါင်းအဖေါ် ကောင်းမွန်စွာ ပြင်ဆင်ထားသည်။ ပြင်ဆင်ချက်များ ပြောင်းလဲပါက Cuda Out Of Memory မှားယွင်းမှု ဖြစ်နိုင်သည်။ ယင်းဖြစ်ပါက compute အရွယ်အစား ကြီးမားစေပါ။

> [!NOTE]
> compute_cluster_size ကို ရွေးသောအခါ သင်၏ resource group တွင် compute ရှိ/မရှိ စစ်ဆေးပါ။ အကယ်၍ ရှိမပါက compute resources အသုံးပြုခွင့် လျှောက်ထားနိုင်သည်။

### Fine Tuning ကို ထောက်ပံ့မှုရှိ/မရှိ စစ်ဆေးခြင်း

၁။ ဤ Python script သည် Azure Machine Learning (Azure ML) မော်ဒယ်နှင့် ဆက်သွယ်သည်။ လုပ်ဆောင်ချက်များမှာ -

- ast module ကို import ပြုလုပ်သည်။ ၎င်းသည် Python syntax tree များကို အလားတူ=သွားစစ်ဆေးနိုင်သည်။

- foundation_model object (Azure ML မော်ဒယ်ကို ကိုယ်စားပြုသည်) တွင် finetune_compute_allow_list ဟူသော tag ရှိ/မရှိစစ်ဆေးသည်။ Azure ML တွင် tag သည် key-value pairများဖြစ်ပြီး မော်ဒယ်များကို စစ်ထုတ်၊ စီတန်းရန် အသုံးပြုသည်။

- finetune_compute_allow_list tag ရှိပါက ast.literal_eval ဖြင့် သာမာန် string ကို Python list တခုအဖြစ် ပြောင်းသည်။ ၎င်းကို computes_allow_list အဖြစ်သတ်မှတ်သည်။ ပြီးသည့်နောက် စာသားကို print ပြသည်။

- finetune_compute_allow_list tag မရှိပါက computes_allow_list = None အဖြစ် သတ်မှတ်ပြီး ဆက်သွယ်မေးမြန်းချက်ကို print ပြသည်။

- နိဂုံးချုပ်အားဖြင့် မော်ဒယ် metadata တွင် သတ်မှတ်ထားသော tag များ ထဲမှ သက်ဆိုင်ရာ one ဖြစ်/မဟုတ်၊ ရှိလား မရှိလား စစ်ဆေးပြီး အသုံးပြုသူအား အသိပေးခြင်း ဖြစ်သည်။

    ```python
    # Python အကျဉ်းချုပ်သုံးသပ်语法သီးသန့်အပြန်အလှန်ဂျပ်များကို ပြုလုပ်ပါသော ast မော်ဂျူးကို ထည့်သွင်းပါ
    import ast
    
    # model ၏ tag များတွင် 'finetune_compute_allow_list' tag ပါရှိမရှိ စစ်ဆေးပါ
    if "finetune_compute_allow_list" in foundation_model.tags:
        # tag အနေနှင့် ပါရှိလျှင် ast.literal_eval ကိုအသုံးပြု၍ tag ၏တန်ဖိုး (string) ကို Python စာရင်းအဖြစ် ရေတွက်ပါ
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # string ကို python စာရင်းသို့ပြောင်းပါ
        # စာရင်းမှ compute တစ်ခုကို ဖန်တီးသင့်ကြောင်း စာမျက်နှာတွင် ဖော်ပြပါ
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # tag မပါရှိပါက computes_allow_list ကို None သတ်မှတ်ပါ
        computes_allow_list = None
        # 'finetune_compute_allow_list' tag သည် model ၏ tag အစိတ်အပိုင်းမဟုတ်ကြောင်း စာမျက်နှာတွင် ဖော်ပြပါ
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Compute Instance ကို စစ်ဆေးခြင်း

၁။ ဤ Python script သည် Azure Machine Learning (Azure ML) ဝန်ဆောင်မှုနှင့် ဆက်သွယ်ပြီး compute instance တစ်ခုအား စစ်ဆေးသည်။ လုပ်ဆောင်ချက်များမှာ -

- Azure ML workspace သို့ compute_cluster ထဲသည့် နာမည်ဖြင့် compute instance ရယူရန် ကြိုးစားသည်။ Provisioning state ပြဿနာဖြစ်ပါက ValueError ကို ရှင့့သည်။

- computes_allow_list သည် None မဟုတ်ပါက အဆိုပါ list ထဲရှိ compute size များအားလုံးကို lowercase ပြောင်းပြီး၊ လက်ရှိ compute instance ၏ size ကို စစ်ဆေး၏ list ထဲပါ/မပါ စစ်ဆေးသည်။ မပါလျှင် ValueError ကို ရှင့့သည်။

- computes_allow_list သည် None ဖြစ်ပါက လက်ရှိ compute instance size ကို unsupported GPU VM size များတွင်ရှိပါက ValueError ကို ရှင့့သည်။

- Workspace တွင် ရရှိနိုင်သော compute size များအား စုစည်းပြီး၊ လည်ပတ်သည့် for loop ဖြင့် လက်ရှိ compute instance size နှင့် မ်ှတမှုရှိသည်ကို စစ်ဆေးသည်။ ရှိပါက ထို compute size ၏ GPU ကဒ် အရေအတွက်ကို ရယူ၍ gpu_count_found ကို True သတ်မှတ်သည်။

- gpu_count_found True ဖြစ်ပါက GPU အရေအတွက်ကို console တွင် print ပြပြီး၊ မဟုတ်ပါက ValueError ဖြင့် ရှင့့သည်။

- နိဂုံးချုပ်အားဖြင့် Azure ML workspace အတွင်းရှိ compute instance ၏ provisioning state, size, allowance list နှင့် GPU အရေအတွက်များကို စစ်ဆေးခြင်းဖြစ်သည်။

    ```python
    # အမွားစာချက်ကို ပုံနှိပ်ပါ
    print(e)
    # workspace တွင် compute size မရရှိပါက ValueError ကို ထုတ်ပေးပါ
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML workspace မှ compute instance ကို ရယူပါ
    compute = workspace_ml_client.compute.get(compute_cluster)
    # compute instance ၏ provisioning state သည် "failed" ဖြစ်ပါက စစ်ဆေးပါ
    if compute.provisioning_state.lower() == "failed":
        # provisioning state သည် "failed" ဖြစ်ပါက ValueError ကို ထုတ်ပေးပါ
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # computes_allow_list သည် None မဟုတ်ကြောင်း စစ်ဆေးပါ
    if computes_allow_list is not None:
        # computes_allow_list တွင်ရှိသော compute size များအားလုံးကို သေးငယ်သော အက္ခရာများသို့ ပြောင်းပါ
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # compute instance ၏ size သည် computes_allow_list_lower_case တွင် ရှိကြောင်း စစ်ဆေးပါ
        if compute.size.lower() not in computes_allow_list_lower_case:
            # compute instance ၏ size သည် computes_allow_list_lower_case တွင် မရှိပါက ValueError ကို ထုတ်ပေးပါ
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # မထောက်ခံသော GPU VM အရွယ်အစားများ စာရင်းကို သတ်မှတ်ပါ
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # compute instance ၏ size သည် unsupported_gpu_vm_list တွင် ရှိကြောင်း စစ်ဆေးပါ
        if compute.size.lower() in unsupported_gpu_vm_list:
            # compute instance ၏ size သည် unsupported_gpu_vm_list တွင် ရှိပါက ValueError ကို ထုတ်ပေးပါ
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # compute instance တွင် GPU အရေအတွက်ကို တွေ့ရှိမှု အားစစ်ဆေးရန် အမှတ်အသားကို စတင်သတ်မှတ်ပါ
    gpu_count_found = False
    # workspace တွင် ရနိုင်သော compute size များ စာရင်းကို ရယူပါ
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # ရနိုင်သော compute size များ စာရင်းကို လှည့်ကြည့်ပါ
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # compute size ၏ နာမည်သည် compute instance ၏ size နှင့် တူညီကြောင်း စစ်ဆေးပါ
        if compute_sku.name.lower() == compute.size.lower():
            # တူညီပါက ထို compute size ၏ GPU အရေအတွက်ကို ရယူပြီး gpu_count_found ကို True ဟုပြောင်းပါ
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # gpu_count_found သည် True ဖြစ်ပါက compute instance ၏ GPU အရေအတွက်ကို ပုံနှိပ်ပါ
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # gpu_count_found သည် False ဖြစ်ပါက ValueError ကို ထုတ်ပေးပါ
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## ၄။ မော်ဒယ် fine tuning အတွက် ဒေတာစုစည်းမှု ရွေးချယ်ခြင်း

၁။ ultrachat_200k ဒေတာစုစည်းမှုကို သုံးသည်။ ဒေတာအပိုင်း၄ခုရှိပြီး Supervised fine-tuning (sft) အတွက် သင့်တော်သည်။
Generation ranking (gen) ဖြစ်သည်။ split တစ်ခုချင်းစီ၏ နမူနာအရေအတွက်မှာ အောက်ပါအတိုင်း ဖြစ်သည်-

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

၁။ အောက်ပါ few cells တွင် fine tuning အတွက် အခြေခံ ဒေတာပြင်ဆင်မှု ပြသထားသည်-

### ဒေတာ အတန်းများကို ကြည့်ရှုခြင်း

မြန်ဆန်စွာ အလုပ်လုပ်သည်အောင် train_sft နှင့် test_sft ဖိုင်များတွင် ရှင်းလင်းပြီး အလယ်ပိုင်းသတ်မှတ်ထားသော အတန်း ၅% ကို သိမ်းဆည်းပါသည်။ ၎င်းကြောင့် fine tuned မော်ဒယ်၏ တိကျမှန်ကန်မှုနည်းပါးပြီး အမှန်တကယ် အသုံးပြုရန် မသင့်တော်ပါ။
download-dataset.py ကို အထောက်အကူပြု စာရွက်သားအနေနဲ့ ultrachat_200k dataset ကို ရယူပြီး finetune pipeline component အသုံးပြုနိုင်သည့်ပုံစံသို့ ပြောင်းလဲပေးသည်။ ဒေတာကြီးသောကြောင့် ကျွန်ုပ်တို့အား ရှင်းလင်းနိုင်သည့် ဒေတာပမာဏသည် အနည်းငယ်သာ ပါရှိသည်။

၁။ အောက်ပါ script တွင် အချို့ များက data ၏ ၅% ကို download ပြုလုပ်သည်။ dataset_split_pc parameter ကို ပြောင်းလဲ၍ တိုးမြှင့်နိုင်သည်။

> [!NOTE]
> ဘာသာစကားမော်ဒယ်အချို့တွင် ဘာသာရေးCode များကွဲပြားသည်၊ ဒါကြောင့် dataset column နာမည်များမှလည်း ထိုလိုက်ဖက်မှုရှိရမည်။

၁။ ဒေတာ ပုံစံ ဥပမာ-

chat-completion dataset ကို parquet ပုံစံဖြင့် သိမ်းဆည်း၍ စာရင်းတစ်ခုစီသည် အောက်ပါ schema နဲ့ဖွဲ့စည်းထားသည်-

- JSON (JavaScript Object Notation) အချက်တစ်ရပ်ဖြစ်သည်။ ဒါဟာ code မဟုတ်ပေမယ့် data သယ်ဆောင်မှုနဲ့ သိမ်းဆည်းမှု အတွက် ရေပန်းစားတဲ့ ပုံစံဖြစ်သည်။ ပုံစံကို အောက်ပါအတိုင်း ခွဲခြမ်းစိတ်ဖြာထားသည်-

- "prompt" - AI အကူအညီမှ တောင်းဆိုထားသည့် task သို့မဟုတ် ကိစ္စ တစ်ခုအဖြစ် စာသားတစ်ရပ်ပါရှိသည်။

- "messages" - user နှင့် AI အကူအညီ တို့ကြား စကားသတင်းများ array တစ်ခုအဖြစ် ပါဝင်သည်။ message object တစ်ခုစီတွင် အောက်ပါ key နှစ်ခုပါရှိသည်-

    - "content" -"message" ၏ အကြောင်းအရာစာသားဖြစ်သည်။

    - "role" - message ပေးပို့သူ၏ အခန်းကဏ္ဍဖြစ်ပြီး "user" သို့မဟုတ် "assistant" ဖြစ်နိုင်သည်။

- "prompt_id" - prompt တစ်ခု အတိအကျသိရှိရန် unique ဝိသေသလက္ခဏာ string တစ်ခု။

၁။ ဤ JSON မှာ user နှင့် AI assistant တို့ကြား dystopian အကြောင်းအရာအတွက် ဇာတ်ကောင် တစ်ဦးဖန်တီးစေလိုခြင်း၊ အထောက်အကူပြုသူ၏တုံ့ပြန်မှုများနှင့် ပို၍အသေးစိတ် မေးမြန်းမှုတို့ပါဝင်သည်။ ပြောဆိုချိန်စကားလုံးအားလုံးသည် prompt id တစ်ခုနှင့် ဆက်စပ်သည်။

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

### ဒေတာဒေါင်းလုပ်လုပ်ခြင်း

၁။ ဤ Python script မှ download-dataset.py helper script ကို အသုံးပြုပြီး ဒေတာ စုစည်းမှုကို ဒေါင်းလုပ်ပြုလုပ်သည်။ လုပ်ဆောင်ချက်များမှာ -

- os module ကို import ပြုလုပ်သည်၊ operating system များနှင့် ဆက်ဆံမှုတွေကို လွယ်ကူစွာ လုပ်ဆောင်နိုင်စေသည်။

- os.system function ကို အသုံးပြု၍ shell မှ download-dataset.py script ကို ခေါ်ပြီး command line arguments ဖြင့် သူ၏ မူရင်းဒေတာစုစည်းမှု (HuggingFaceH4/ultrachat_200k), ဒေါင်းလုပ် သိမ်းဆည်းမည့် directory (ultrachat_200k_dataset), ခုလို dataset ကောင်တာချိန်ခွဲ (5%) တို့ကို သတ်မှတ်သည်။ os.system ဟာ shell command ရဲ့ exit status များ (0 သည်အောင်မြင်မှုကို ဆိုလိုသည်) ကို ပြန်အမ်းပြီး exit_status မှာ သိမ်းဆည်းထားသည်။

- exit_status 0 မဟုတ်ပါက ဒေတာဒေါင်းလုပ်တွင် ပြဿနာဖြစ်ကြောင်း Exception ကို raise ပြုလုပ်သည်။

- တိုတောင်းစွာ script သည် ဒေတာဒေါင်းလုပ် helper script ကို run ပြီး အောင်မြင်/မအောင်မြင်အား စစ်ဆေးသည်။

    ```python
    # အချိန်ဆက်နွယ်မှုအတွက် လုပ်ငန်းစဉ်စနစ်မူပိုင်ခွင့် လုပ်ဆောင်ချက်များကို အသုံးပြုနိုင်ရန် os မော်ဂျူးကို ထည့်သွင်းပါ
    import os
    
    # သတ်မှတ်ထားသော command-line အချက်အလက်များနဲ့ download-dataset.py script ကို shell မှာ os.system function ကို အသုံးပြုပြီး လည်ပတ်ပါ
    # အချက်အလက်များ သတ်မှတ်ချက်မှာ ဒဏ်ဆိုဒ်ကိုဒေါင်းလုပ်လုပ်ရန် (HuggingFaceH4/ultrachat_200k)၊ ဒေါင်းလုပ်ကြောင်း သိမ်းဆည်းရန်ဆိုတဲ့ ဒါရိုက်တာ (ultrachat_200k_dataset) နှင့် ဒဏ်ဆိုဒ်ကိုခွဲစိတ်ရာရာခိုင်နှုန်း (5) ဖြစ်ပါသည်
    # os.system function သည် လည်ပတ်ခဲ့သော command ၏ ထွက်မှုအခြေအနေကို ပြန်လည်ပေးပို့ပြီး exit_status ကိုယ်စားလှယ်တွင် သိမ်းဆည်းပါသည်
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # exit_status က 0 မဟုတ်တာကို စစ်ဆေးပါ
    # Unix ပုံစံ စနစ်များတွင် exit status 0 ဆိုသည်မှာ ပုံမှန်အောင်မြင်မှုကို ပြသပြီး အခြားနံပါတ်တစ်ခုဖြစ်ပါက အမှားတစ်ခု ဖြစ်ကြောင်း သီအိုရား ရှိသည်
    # exit_status သည် 0 မဟုတ်ပါက ဒဏ်ဆိုဒ်ဒေါင်းလုပ်လုပ်ရာတွင် အမှား ဖြစ်ကြောင်း ပြသသော Exception ကို ထုတ်ပေးပါ
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### ဒေတာကို DataFrame ထဲသို့ load ပြုလုပ်ခြင်း

၁။ ဤ Python script သည် JSON Lines ဖိုင်တစ်ခုကို pandas DataFrame ထဲသို့ load ပြီး ပထမဆုံး ၅ ထိဝင်သော အတန်းများကို ပြသသည်။ လုပ်ဆောင်ချက်များမှာ -

- pandas library ကို import လုပ်သည်- ဒေတာ ကို လွယ်ကူစွာ ချုပ်ဆို၊ စစ်ဆေးနှင့် ချပြရန် အသုံးပြုသော library ဖြစ်သည်။

- pandas display options မှာ column data များကို ပိတ်မထားဘဲ အပြည့်အစုံကြည့်ရှုနိုင်ရန် maximum column width ကို 0 အဖြစ် သတ်မှတ်သည်။
    - ultrachat_200k_dataset ဖိုလ်ဒါထဲက train_sft.jsonl ဖိုင်ကို pd.read_json function ကို အသုံးပြု၍ DataFrame အနေနဲ့ ဖတ်ယူသည်။ lines=True ဆိုတဲ့ argument က ဖိုင်ဟာ JSON Lines ဖော်မတ်ဖြစ်ပြီး တစ်ကြောင်းချင်းစီက JSON object တစ်ခုဖြစ်ကြောင်း ပြသည်။

    - head method ကို အသုံးပြု၍ DataFrame ရဲ့ ပထမ ၅ ကြောင်းကို ပြသသည်။ DataFrame ထဲက တော်တော်နည်းရင် အားလုံးကို ပြသပါမည်။

    - အကျဉ်းချုပ် အနေနဲ့ ဒီ script က JSON Lines ဖိုင်ကို DataFrame ထဲသို့ loading ပြုလုပ်ပြီး ကော်လံရှိ စာသားများ အပြည့်အစုံဖြင့် ပထမ ၅ ကြောင်းကို ပြသနေပါသည်။
    
    ```python
    # အင်္ဂါရပ်ကြွယ်ဝပြီး ဒေတာကို မူကြမ်းပြုလုပ်ခြင်းနှင့် စိစစ်ခြင်းလုပ်ငန်းများအတွက် pandas ไลဘ်ရယ်ကို သွင်းပါ
    import pandas as pd
    
    # pandas ပြသမှု ရွေးချယ်မှုများအတွက် အကောင်းဆုံး ကော်လံ အနံကို 0 သတ်မှတ်ပါ
    # ဒါကတော့ DataFrame ကို ပုံနှိပ်သောအခါ ကော်လံတိုင်း၏ စာသား အပြည့်အစုံကို ဖြတ်မတောက်ဘဲ ပြသမည်ဆိုလိုသည်
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json function ကို အသုံးပြု၍ ultrachat_200k_dataset ဖိုလ်ဒါမှ train_sft.jsonl ဖိုင်ကို DataFrame ထဲသို့ ထည့်ပါ
    # lines=True အချက်မှာ ဖိုင်သည် JSON Lines ဖော်แมတ်ဖြစ်ပြီး လိုင်း တစ်ခုချင်းစီသည် JSON အရာဝတ္တုပဲ ဖြစ်ကြောင်း ပြပါသည်
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # head method ကို အသုံးပြု၍ DataFrame ၏ ပထမ ၅ လိုင်းကို ပြပါ
    # DataFrame တွင် ၅ လိုင်းအောက်သာ ရှိပါက လိုင်းအားလုံးကို ပြပါလိမ့်မည်
    df.head()
    ```

## 5. fine tuning အလုပ်ကို မော်ဒယ်နဲ့ ဒေတာကို input အဖြစ် အသုံးပြု၍ တင်ပြခြင်း

chat-completion pipeline component ကို အသုံးပြုသည့် job တစ်ခု ဖန်တီးပါ။ fine tuning အတွက် ပံ့ပိုးပေးသည့် parameter သတ်မှတ်ချက်များကို အလုပ်သင်ယူပါ။

### finetune parameters ကို သတ်မှတ်ခြင်း

1. Finetune parameters များကို training parameters နှင့် optimization parameters ဆိုပြီး အမျိုးအစား ၂ မျိုးခွဲနိုင်သည်။

1. Training parameters အနေနဲ့ သင်ကြားမှုနဲ့ဆိုင်သော အချက်အလက်များအား မှတ်သားသည်၊ ဥပမာ -

    - အသုံးပြုလိုသော optimizer၊ scheduler
    - finetune အထိထိရောက်ဆုံးနှင့်ပြုလုပ်ရန် metric
    - သင်ကြားမှု လုပ်ဆောင်ရန် အဆင့်အရေအတွက်နှင့် batch အရွယ်အစား စသည်တို့
    - Optimization parameters ကို GPU မေမရီ အသုံးများမှု ထိန်းသိမ်းရန် နဲ့ စွမ်းဆောင်ရည် ထိရောက်စွာ အသုံးပြုရန် ကူညီပေးသည်။

1. အောက်ပါ parameter များသည် optimization parameters အမျိုးအစားဖြစ်ပြီး မော်ဒယ်အလိုက် မတူညီသည့် သတ်မှတ်ချက်များ ပါဝင်၍ အဆိုပါ မော်ဒယ်နှင့် ကျောမှပကိန်းထားသည်။

    - deepspeed နဲ့ LoRA ကို ဖွင့်နိုင်ခြင်း
    - mixed precision training ကို ဖွင့်နိုင်ခြင်း
    - multi-node training ကို ဖွင့်နိုင်ခြင်း

> [!NOTE]
> supervised finetuning အဖြစ် alignment ကျရှုံးခြင်း သို့မဟုတ် catastrophic forgetting ဖြစ်နိုင်ပါသည်။ ဒီပြဿနာရှိမရှိ စစ်ဆေးပြီး finetuning ပြီးနောက် အလားတူ alignment အဆင့် လုပ်ဆောင်ရန် အကြံပြုပါသည်။

### Fine Tuning Parameters

1. ဒီ Python script က machine learning မော်ဒယ် တစ်ခုကို fine-tuning အတွက် parameter များ သတ်မှတ်နေသည်။ လုပ်ဆောင်ချက်အချို့ကို ဖေါ်ပြပါ-

    - နေရာတိုင်းသို့ သင်ကြားရန် epochs အရေအတွက်၊ training နှင့် evaluation အတွက် batch size များ၊ learning rate၊ နှင့် learning rate scheduler အမျိုးအစားများ Default အဖြစ် သတ်မှတ်ခြင်း။

    - Layer-wise Relevance Propagation (LoRa) နှင့် DeepSpeed ကို အသုံးပြုမည်ဟုတ်မဟုတ်၊ DeepSpeed အဆင့် သတ်မှတ်ချက်များ Default အဖြစ် သတ်မှတ်ခြင်း။

    - training နှင့် optimization parameter များကို finetune_parameters ဆိုသော dictionary တစ်ခုအဖြစ် ပေါင်းစပ်ခြင်း။

    - foundation_model တွင် မော်ဒယ်အလိုက် သတ်မှတ်ထားသော Default parameter များရှိပါက အသိပေးသတင်းပို့ပြီး finetune_parameters ကို အဆိုပါ parameter များဖြင့် update ပြုလုပ်ခြင်း၊ ast.literal_eval function ကို သုံး၍ string မှ Python dictionary အဖြစ်ပြောင်းခြင်း။

    - မိမိထားလိုက်သော fine-tune parameter များကို နောက်ဆုံးအနေဖြင့် ထုတ်ပြခြင်း။

    - အကျဉ်းချုပ် အနေနဲ့ မော်ဒယ်တစ်ခုကို fine-tuning ပြုလုပ်ရာ parameter များ သတ်မှတ် သည့် script ဖြစ်ပြီး မော်ဒယ်အလိုက် Default မဟုတ်သည့် parameter များကို override လုပ်နိုင်ပါသည်။

    ```python
    # ပုံမှန် သင်ကြားမှု ပရာမီတာများကို သတ်မှတ်ပါ၊ ဥပမာအားဖြင့် သင်ကြားမှု epoch အရေအတွက်၊ သင်ကြားမှုနှင့် သုံးသပ်မှုအတွက် batch အရွယ်အစားများ၊ သင်ယူနှုန်းနှင့် သင်ယူနှုန်း စီမံခန့်ခွဲမှု အမျိုးအစား
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # ပုံမှန် optimization ပရာမီတာများကို သတ်မှတ်ပါ၊ ဥပမာ Layer-wise Relevance Propagation (LoRa) နှင့် DeepSpeed ကို အသုံးပြုမည်ဟုတ်မဟုတ်၊ နောက် DeepSpeed အဆင့်
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # သင်ကြားမှုနှင့် optimization ပရာမီတာများကို finetune_parameters ဟုခေါ်သော တစ်ခုတည်းသော dictionary ထဲတွင် ပေါင်းစပ်ပါ
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # foundation_model တွင် မူလပုံစံသတ်မှတ်ချက်များ ရှိမရှိ စစ်ဆေးပါ
    # ရှိပါက သတိပေးမက်စေ့ချ် တစ်စောင်ကို ပုံနှိပ်ပြီး finetune_parameters dictionary ကို မူလပုံစံသတ်မှတ်ချက်များဖြင့် ညှိနှိုင်းပါ
    # ast.literal_eval function ကို မူလပုံစံသတ်မှတ်ချက်များကို string မှ Python dictionary သို့ ပြောင်းရန် အသုံးပြုသည်
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # string ကို python dict သို့ ပြောင်းသည်
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # သွားလုပ်မည့် fine-tuning ပရာမီတာများ၏ နောက်ဆုံးအစုကို ပုံနှိပ်ပြပါ
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Training Pipeline

1. ဒီ Python script က machine learning training pipeline အတွက် display name ဖန်တီးပေးမည့် function တစ်ခု အဓိက သတ်မှတ်ပြီး ထို function ကို ဖိတ်ခေါ်၍ display name ထုတ်ပေးသည်။ လုပ်ဆောင်ချက် အချက်တွေကို ဖော်ပြပါ-

1. get_pipeline_display_name function ကို သတ်မှတ်ထားသည်။ training pipeline ဆွဲဆောင်မှုနှင့်ဆိုင်သော parameter များ အပေါ် အခြေခံ၍ display name တစ်ခုကို ဖန်တီးသည်။

1. function အတွင်းမှာ per-device batch size, gradient accumulation steps အရေအတွက်, node တစ်ခုချင်းစီတွင် GPU အရေအတွက်, fine-tuning အတွက် အသုံးပြု node အရေအတွက်တို့ကို သင့်တော်စွာ မြောက်လိုက်ကာ မျိုးစုံသော parameter များကို ရယူသည်။

1. learning rate scheduler အမျိုးအစား, DeepSpeed အသုံးပြုမှုရှိမရှိ, DeepSpeed အဆင့်, LoRa အသုံးပြုမှု, model checkpoint များ သိမ်းဆည်းရန် ဟန်ချက်၊ အများဆုံး sequence ရှည်လျားမှု စတော့ parameter များကိုလည်း ရယူသည်။

1. parameter များကို ဒါတွေထဲက string တစ်ခုအနေဖြင့် hyphen ဖြင့် ခွဲခြားပြီး ဖန်တီးသည်။ DeepSpeed သို့မဟုတ် LoRa အသုံးပြုသောအခါ "ds" နှင့် အဆင့် သို့မဟုတ် "lora" ဆိုပြီး ထည့်သွင်းမည်။ မဟုတ်ရင် "nods" သို့မဟုတ် "nolora" ဟု ပါဝင်မည်။

1. function မှ string ကို ပြန်လည် return ပြုလုပ်ပြီး training pipeline ၏ display name အဖြစ် အသုံးပြုသည်။

1. function ကို ဖော်ပြပြီးနောက် ဖိတ်ခေါ်၍ display name ထုတ်ပေးပြီး print ထုတ်သည်။

1. အကျဉ်းချုပ် - training pipeline အတွက် parameter အခြေခံပြီး display name ဖန်တီး ထုတ်ပေးတဲ့ script ဖြစ်သည်။

    ```python
    # သင်ကြားမှု pipeline အတွက် ပြသမည့်နာမည်ကို ဖန်တီးရန် function တစ်ခု သတ်မှတ်ပါ
    def get_pipeline_display_name():
        # တစ် DEVICE လျှင် batch အရွယ်အစားကို gradient စုပေါင်းခြေလှမ်း အရေအတွက်၊ node တစ်ခုလျှင် GPU အရေအတွက်နှင့် fine-tuning အတွက် အသုံးပြုထားသော node အရေအတွက်ဖြင့် မြှောက်ပြီး စုစုပေါင်း batch အရွယ်အစားကိုတွက်ချက်ပါ
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # သင်ယူမှုနှုန်း စီစဉ်သူအမျိုးအစားကို ရယူပါ
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # DeepSpeed အသုံးပြုထားသလား ဆိုတာကို ရယူပါ
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # DeepSpeed အဆင့်ကို ရယူပါ
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # DeepSpeed အသုံးပြုထားပါက၊ ပြသမည့်နာမည်တွင် "ds" နှင့် DeepSpeed အဆင့်ကို ပါဝင်စေရန် ပါဝင်သည်; မဟုတ်ပါက "nods" ကို ပါဝင်စေပါ
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Layer-wise Relevance Propagation (LoRa) ကို အသုံးပြုထားသလားဆိုတာ ရယူပါ
        lora = finetune_parameters.get("apply_lora", "false")
        # LoRa အသုံးပြုထားပါက၊ ပြသမည့်နာမည်တွင် "lora" ပါဝင်စေရန်; မဟုတ်ပါက "nolora" ပါဝင်စေပါ
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # ထိန်းသိမ်းထားမည့် model checkpoint အရေအတွက် ဆက်တင်ကို ရယူပါ
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # အများဆုံး စာကြောင်း အရှည်ကို ရယူပါ
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # ဒီ parameter အားလုံးကို hyphen ဖြင့် ခွဲ၍ ပြသမည့်နာမည်ကို ဖန်တီးပါ
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
    
    # ပြသမည့်နာမည်ကို ဖန်တီးရန် function ကို ခေါ်ပါ
    pipeline_display_name = get_pipeline_display_name()
    # ပြသမည့်နာမည်ကို ပုံနှိပ်ပါ
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Pipeline အား configure ပြုလုပ်ခြင်း

ဒီ Python script က Azure Machine Learning SDK အသုံးပြု၍ machine learning pipeline ကို သတ်မှတ် configure လုပ်နေသည်၊ လုပ်ဆောင်ချက် အချက်အလက်များ -

1. Azure AI ML SDK မှ အသုံးလိုအပ်သော module များကို import ပြုလုပ်သည်။

1. registry ထဲမှ "chat_completion_pipeline" pipeline component ကို ရယူသည်။

1. `@pipeline` decorator နှင့် `create_pipeline` function ဖြင့် pipeline job တစ်ခုအား သတ်မှတ်သည်။ pipeline အမည်ကို `pipeline_display_name` ဟု သတ်မှတ်ထားသည်။

1. `create_pipeline` function အတွင်း fetched pipeline component ကို model path, သီးခြားလမ်းကြောင်းသုံး cluster များ (training, testing), fine-tune အတွက် အသုံးပြု GPU အရေအတွက် နှင့် အခြား fine-tuning parameter များ ဖြင့် initialize ပြုလုပ်သည်။

1. fine-tuning job ရလဒ်ကို pipeline job ၏ output နှင့် ပေါင်းတင်ထားသည်။ fine-tuned model ကို parameter ထည့်သုံး(Register)၍ online လုပ်ငန်းသို့ အလွယ်တကူ တင်ပို့နိုင်ရန်သည်။

1. `create_pipeline` function ကိုခေါ်၍ pipeline instance ဖန်တီးသည်။

1. pipeline ၏ `force_rerun` ကို True သတ်မှတ်ထားပြီး ယခင် အလုပ်ဖြင့် သိမ်းဆည်းထားသော cache များကို အသုံးမပြုပါ။

1. pipeline ၏ `continue_on_step_failure` ကို False သတ်မှတ်ပြီး အဆင့်တစ်ခုခု fail ဖြစ်မည်ဆို pipeline ရပ်စဲမည်။

1. အကျဉ်းချုပ် - Azure Machine Learning SDK ကို အသုံးပြု chat completion အလုပ်လုပ်သော machine learning pipeline ကို သတ်မှတ် configure ပြုလုပ်ထားပါသည်။

    ```python
    # Azure AI ML SDK မှ လိုအပ်သော မော်ဂျူးများကို တင်သွင်းသည်
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # registry မှ "chat_completion_pipeline" ဟု အမည်ရသော pipeline component ကို ရယူသည်
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline decorator နှင့် create_pipeline function ကို အသုံးပြု၍ pipeline job ကို သတ်မှတ်သည်
    # pipeline အမည်ကို pipeline_display_name ဟု သတ်မှတ်ထားသည်
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # ရယူထားသော pipeline component ကို parameter များစွာဖြင့် စတင်တပ်ဆင်သည်
        # ၎င်းတွင် မော်ဒယ်လ်လမ်းကြောင်း၊ အဆင့်အလိုက် compute cluster များ၊ လေ့ကျင့်မှုနှင့် စမ်းသပ်မှုအတွက် dataset ခွဲများ၊ fine-tuning အတွက် အသုံးပြုမည့် GPU အရေအတွက်နှင့် အခြား fine-tuning parameter များ ပါ၀င်သည်
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # dataset ခွဲများကို parameter များနှင့် တွဲပြသည်
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # လေ့ကျင့်မှု ဆက်တင်များ
            number_of_gpu_to_use_finetuning=gpus_per_node,  # compute တွင် ရရှိနိုင်သော GPU အရေအတွက် သတ်မှတ်သည်
            **finetune_parameters
        )
        return {
            # fine tuning အလုပ်၏ output ကို pipeline job ၏ output နှင့် တွဲဖက်ပြသည်
            # ဤကိစ္စက fine tuned model ကို လွယ်ကူစွာ မှတ်ပုံတင်နိုင်ရန် ဖြစ်သည်
            # မော်ဒယ်လ်ကို online သို့မဟုတ် batch endpoint တွင် ထည့်သွင်းရန် model မှတ်ပုံတင်ခြင်း လိုအပ်သည်
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline function ကို ခေါ်၍ pipeline ၏ instance ကို ဖန်တီးသည်
    pipeline_object = create_pipeline()
    
    # ယခင်အလုပ်များမှ cache ရလဒ်များကို မသုံးပါနှင့်
    pipeline_object.settings.force_rerun = True
    
    # စတင်မှုမအောင်မြင်ပါက ဆက်လက်လုပ်ကိုင်မှုကို False သတ်မှတ်သည်
    # ၎င်းသည် pipeline တွင် အဆင့်တစ်ခုမှ မအောင်မြင်ပါက အလုပ်ရပ်နားမည်ဟု ဆိုလိုသည်
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Job တင်သွင်းခြင်း

1. ဒီ Python script က Azure Machine Learning workspace သို့ machine learning pipeline job တင်သွင်းပြီး အလုပ်ပြီးဆုံးရန် စောင့်ဆိုင်းနေသည်။ လုပ်ဆောင်ချက်များ -

    - workspace_ml_client ရှိ jobs object ၏ create_or_update method ကို အသုံးပြု၍ pipeline job အတွက် pipeline_object ကို သတ်မှတ်ပြီး experiment_name အောက်တွင် job ကို တင်သွင်းသည်။

    - အလုပ်ပြီးဆုံးရန် workspace_ml_client ၏ jobs object ၏ stream method ကို ခေါ်၍ pipeline_job ၏ name attribute ကို အသုံးပြုပြီး စောင့်ဆိုင်းသည်။

    - အကျဉ်းချုပ် - Azure Machine Learning workspace သို့ machine learning pipeline job တင်သွင်းပြီး အလုပ်ပြီးဆုံးစောင့်ဆိုင်းခြင်းဖြစ်ပါသည်။

    ```python
    # Azure Machine Learning စက်ပစ္စည်းသင်ယူ workspace သို့ pipeline အလုပ်အကိုင်တင်ပို့ပါ
    # အသုံးပြုမည့် pipeline ကို pipeline_object ဖြင့် သတ်မှတ်ထားသည်
    # အလုပ်အကိုင်ကို လည်ပတ်မည့် experiment ကို experiment_name ဖြင့် သတ်မှတ်ထားသည်
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # pipeline အလုပ်အကိုင် ပြီးစီးမှုအတွက် စောင့်ဆိုင်းပါ
    # စောင့်ဆိုင်းရန်အလုပ်အကိုင်မှာ pipeline_job အရာဝတ္တု၏ name attribute ဖြင့် သတ်မှတ်ထားသည်
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. fine tuned မော်ဒယ်ကို workspace တွင် မှတ်ပုံတင်ခြင်း

fine tuning job ၏ output မှ မော်ဒယ်ကို မှတ်ပုံတင်မည်။ ဒီအတိုင်း fine tuned model နှင့် fine tuning job ကြားတွင် lineage ထိန်းသိမ်းနိုင်မည်။ fine tuning job မှ foundation model, data နှင့် training code ဆီသို့ lineage အလှည့်တွဲ လိုက်ပါသွားမည်။

### ML Model မှတ်ပုံတင်ခြင်း

1. ဒီ Python script က Azure Machine Learning pipeline ထဲမှာ သင်ကြားပြီးသား machine learning မော်ဒယ် တစ်ခုကို မှတ်ပုံတင်နေသည်။ လုပ်ဆောင်ချက်များ -

    - Azure AI ML SDK မှ လိုအပ်သော modules ကို import ပြုလုပ်သည်။

    - pipeline job မှ trained_model output ရှိမရှိ workspace_ml_client ရှိ jobs object ၏ get method ဖြင့် စစ်ဆေးပြီး outputs attribute ထဲမှ ရယူသည်။

    - pipeline job ၏ name နှင့် output အမည် ("trained_model") ကို အသုံးပြု၍ မော်ဒယ်လမ်းကြောင်း တည်ဆောက်သည်။

    - original model name တွင် "-"ultrachat-200k" ကို ဆက်ထပ်ပြီး slash များကို hyphen ဖြင့် အစားထိုးပြီး fine tuned model အမည်သတ်မှတ်သည်။

    - Model object တစ်ခု ဖန်တီး၍ မော်ဒယ်လမ်းကြောင်း၊ type (MLflow model), မော်ဒယ်အမည်၊ ဗားရှင်းနှင့် ဖော်ပြချက် စသည်ဖြင့် အချက်အလက်များ ပြင်ဆင်၍ မှတ်ပုံတင်ရန် ပြင်ဆင်သည်။

    - workspace_ml_client ၏ models object ၏ create_or_update method ကို ခေါ်ပြီး Model object ဖြင့် မှတ်ပုံတင်သည်။

    - မှတ်ပုံတင်ပြီးသော မော်ဒယ်ကို print ထုတ်သည်။

1. အကျဉ်းချုပ် - Azure Machine Learning pipeline မှ သင်ကြားပြီး မော်ဒယ်ကို မှတ်ပုံတင်ခြင်းဖြစ်သည်။
    
    ```python
    # Azure AI ML SDK မှ လိုအပ်သော module များကို သွင်းခြင်း
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # `trained_model` output သည် pipeline job မှ ရနိုင်ကြောင်း စစ်ဆေးခြင်း
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # pipeline job နာမည်နှင့် output ("trained_model") နာမည်အား ဖြည့်စွက်၍ သင်ကြားပြီးသော model အတွက် လမ်းကြောင်း တည်ဆောက်ခြင်း
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # မူလ model နာမည်၏ slug များအား hyphen ဖြင့် အစားထိုးပြီး "-ultrachat-200k" ကို ထပ်ဖြည့်၍ fine-tuned model အတွက် နာမည် သတ်မှတ်ခြင်း
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Model object တစ်ခုကို အမျိုးမျိုးသော ပARAMETERS များဖြင့် ဖန်တီး၍ model ကို မှတ်ပုံတင်ရန် ပြင်ဆင်ခြင်း
    # ဤ parameters များတွင် model ၏ လမ်းကြောင်း၊ model အမျိုးအစား (MLflow model), model နာမည် နှင့် ဗားရှင်း၊ model ရဲ့ ဖော်ပြချက် ပါဝင်သည်
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # ဗားရှင်း မတူညီမှု မဖြစ်ဖို့အတွက် timestamp ကို ဗားရှင်းအဖြစ် အသုံးပြုခြင်း
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # workspace_ml_client ရဲ့ models object မှ create_or_update method ကို Model object ကိုအ_arguments အဖြစ် ပေးပို့၍ model ကို မှတ်ပုံတင်ခြင်း
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # မှတ်ပုံတင်ပြီးသော model ကို ပရင့်ထုတ်ပြခြင်း
    print("registered model: \n", registered_model)
    ```

## 7. fine tuned မော်ဒယ်ကို online endpoint သို့ တင်သွင်းခြင်း

Online endpoint များက ခိုင်မာပြီး တည်တံ့သော REST API ဖြစ်သဖြင့် မော်ဒယ် အသုံးပြု လုပ်ဆောင်မှုများနှင့် ပေါင်းစည်းဖောင့် အဆင်ပြေစေသည်။

### Endpoint ကို စီမံခန့်ခွဲခြင်း

1. ဒီ Python script က Azure Machine Learning မှာ registered model အတွက် managed online endpoint တစ်ခု ဖန်တီးနေသည်။ လုပ်ဆောင်ချက်များ -

    - Azure AI ML SDK မှလိုအပ်သော modules ကို import ပြုလုပ်သည်။

    - online endpoint အမည်ကို "ultrachat-completion-" string အောက်တွင် timestamp ထပ်ဆောင်းပြီး သီးခြားစနစ်ဖြင့် သတ်မှတ်သည်။

    - ManagedOnlineEndpoint object တစ်ခု ဖန်တီး၍ endpoint အမည်၊ ဖော်ပြချက်နှင့် authentication mode ("key") ပါသော parameter များ ဖြည့်စွက်ပြီး online endpoint ဖန်တီးရန် ပြင်ဆင်သည်။

    - workspace_ml_client ၏ begin_create_or_update method ကို အသုံးပြု၍ managed online endpoint ဖန်တီးပြီး wait method ဖြင့် ဖန်တီးခြင်း ပြီးဆုံးရန် စောင့်ဆိုင်းသည်။

1. အကျဉ်းချုပ် - Azure Machine Learning မှာ registered model အတွက် managed online endpoint ဖန်တီးမှုဖြစ်သည်။

    ```python
    # Azure AI ML SDK မှ လိုအပ်သော module များကို import လုပ်ပါ
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" string အပြီးတွင် timestamp ကပ်၍ online endpoint အတွက် အထူးတစ်ခုသော အမည်ကို သတ်မှတ်ပါ
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # နောက်တစ်ဆင့် ManagedOnlineEndpoint object ကို parameter မျိုးစုံနှင့်တကွ ဖန်တီး၍ online endpoint ဖန်တီးရန် ပြင်ဆင်ပါ
    # ၎င်းတွင် endpoint အမည်၊ endpoint ဖော်ပြချက် နှင့် authentication mode ("key") ပါဝင်သည်
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint object ကို argument အဖြစ် သုံးပြီး workspace_ml_client ၏ begin_create_or_update method ကို ခေါ်သုံးကာ online endpoint ကို ဖန်တီးပါ
    # ထို့နောက် creation လုပ်ငန်းကို ပြီးမြောက်ရန် wait method ကို ခေါ်ပြီး စောင့်ပါ
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Deploy လုပ်ရာတွင် ပံ့ပိုးပေးသည့် SKU များစာရင်းကို ဒီနေရာတွင်တွေ့နိုင်ပါသည် - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML Model ကို တင်သွင်းခြင်း

1. ဒီ Python script က Azure Machine Learning မှာ registered မော်ဒယ်ကို managed online endpoint သို့ deploy လုပ်နေသည်။ လုပ်ဆောင်ချက်များ -

    - Python abstract syntax grammar tree များ ကို ခွဲထုတ်ရန်အတွက် ast module ကို import ပြုလုပ်သည်။

    - deployment အတွက် instance type ကို "Standard_NC6s_v3" ဟု သတ်မှတ်ထားသည်။

    - foundation model တွင် inference_compute_allow_list tag ရှိမရှိ စစ်ဆေးပြီး ရှိပါက string မှ Python list အဖြစ် ပြောင်းပြီး inference_computes_allow_list သို့ သတ်မှတ်သည်။ မရှိပါက None ထားသည်။

    - သတ်မှတ်ထားသော instance type သည် allow list ထဲ မပါပါက အသုံးပြုသူအား allow list ထဲမှ instance type တစ်ခုရွေးရန် ဆက်သွယ်စာ ထုတ်ပြသည်။

    - ManagedOnlineDeployment object တစ်ခု ဖန်တီး၍ deployment နာမည်၊ endpoint နာမည်၊ model ID၊ instance type/အရေအတွက်၊ liveness probe နှင့် request settings ထည့်သွင်း ပြင်ဆင်သည်။

    - begin_create_or_update method ဖြင့် deployment တည်ဆောက်ပြီး wait method ဖြင့် ဖန်တီးမှု ပြီးဆုံးရန် စောင့်ဆိုင်းသည်။

    - endpoint traffic ကို "demo" deployment သို့ ၁၀၀% တိုက်ရိုက် ဆင်းရဲချသည်။

    - workspace_ml_client begin_create_or_update method ဖြင့် endpoint update ပြုလုပ်ပြီး result method ဖြင့် အတည်ပြုသည်။

1. အကျဉ်းချုပ် - registered model ကို managed online endpoint သို့ deploy လုပ်ခြင်းဖြစ်သည်။

    ```python
    # Python အဆောက်အအုံသက်ဆိုင်ရာ သဒ္ဒါသိပ္ပံဥပဒေသစ်သည် ရှေ့ပြေးနည်းစနစ်အတန်းအစားကို ဆန့်ကျင်သစ်ဖွဲ့စည်းထားသော သစ်တောများကို လုပ်ဆောင်ရန် အတတ်ပညာပေးသော ast မော်ဂျူးကို တင်သွင်းသည်
    import ast
    
    # ဖြန့်ချိမှုအတွက် အရေးအသား ပုံစံကို သတ်မှတ်ပါ
    instance_type = "Standard_NC6s_v3"
    
    # အခြေခံမော်ဒယ်တွင် `inference_compute_allow_list` တံဆိပ်ထားရှိမရှိ စစ်ဆေးပါ
    if "inference_compute_allow_list" in foundation_model.tags:
        # ရှိပါက တံဆိပ်တန်ဖိုးကို string မှ Python list သို့ပြောင်းပြီး `inference_computes_allow_list` သို့ သတ်မှတ်ပါ
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # မရှိပါက `inference_computes_allow_list` ကို `None` သတ်မှတ်ပါ
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # ဖော်ပြထားသော အရေးအသားပုံစံသည် ခွင့်ပြုစာရင်းတွင် ပါဝင်နေသည်ကို စစ်ဆေးပါ
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # အမျိုးမျိုးသော ပါရာမီတာများဖြင့် `ManagedOnlineDeployment` အရာဝတ္ထု တည်ဆောက်ပြီး ဖြန့်ချိမှု ပြုလုပ်ရန် ပြင်ဆင်ပါ
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `ManagedOnlineDeployment` အရာဝတ္ထုကို အချက်အလက်အဖြစ် အသုံးပြုကာ `workspace_ml_client` ၏ `begin_create_or_update` နည်းလမ်းနှင့် ဖြန့်ချိမှုကို ဖန်တီးပါ
    # ထို့နောက် ဖန်တီးရေး လုပ်ငန်းစဉ်ပြီးဆုံး হওန် အခန်းနှင့် `wait` နည်းလမ်းကို ခေါ်ယူ၍ စောင့်ဆိုင်းပါ
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # endpoint ၏ traffic ကို "demo" ဖြန့်ချိမှုသို့ ၁၀၀% တည်မြဲစွာ လမ်းညွှန်ထားပါ
    endpoint.traffic = {"demo": 100}
    
    # `endpoint` အရာဝတ္ထုပေါ်တွင် `workspace_ml_client` ၏ `begin_create_or_update` နည်းလမ်းကို ခေါ်ယူကာ endpoint ကို ပြန်လည်အပ်ဒိတ်လုပ်ပါ
    # ထို့နောက် အပ်ဒိတ်လုပ်ငန်းစဉ်ပြီးဆုံးမှုအထိ `result` နည်းလမ်းအား ခေါ်ယူ၍ စောင့်ဆိုင်းပါ
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. sample data ဖြင့် endpoint စမ်းသပ်ခြင်း

test dataset မှ စမ်းသပ်မှု data ကို ရယူ၍ online endpoint တွင် inference အတွက် တင်သွင်းမည်။ ဆုချရန် label နှင့် ground truth label များကို ပြသပေးမည်။

### ရလဒ်များ ဖတ်ရှုခြင်း

1. ဒီ Python script က JSON Lines ဖိုင်ကို pandas DataFrame အဖြစ် ဖတ်ပြီး မျွှင့်တော် random sample စုဆောင်းပြီး index ပြန်စတင်ထားသည်။ လုပ်ဆောင်ချက်များ -

    - ./ultrachat_200k_dataset/test_gen.jsonl ဖိုင်ကို pandas DataFrame အဖြစ် ဖတ်သည်။ JSON Lines format အနေဖြင့် lines=True argument ကို အသုံးပြုသည်။

    - DataFrame မှ random sample ၁ ကြောင်း ရယူသည်။ sample function တွင် n=1 ကို အသုံးပြုသည်။

    - DataFrame index ကို reset လုပ်စဉ် drop=True ဖြင့် မူလ index ကို ဖယ်ရှားပြီး default integer index ပြန်သတ်မှတ်သည်။

    - head function ၂ ကြောင်း တွင် ဒေတာပြသရာတွင် sample ရပြီး လက်ရှိ DataFrame တွင် ၁ ကြောင်းသာ ပါသောကြောင့် တစ်ကြောင်းသာ ပြသည်။

1. အကျဉ်းချုပ် - JSON Lines ဖိုင်ကို pandas DataFrame အဖြစ် ဖတ်၍ random sample ၁ ကြောင်း ရယူပြီး index ပြန်စတင် ထားကာ ပထမကြောင်းကို ပြသခြင်း ဖြစ်သည်။
    
    ```python
    # pandas စာကြည့်တိုက်ကို တင်သွင်းပါ
    import pandas as pd
    
    # './ultrachat_200k_dataset/test_gen.jsonl' JSON Lines ဖိုင်ကို pandas DataFrame အဖြစ် ဖတ်ပါ
    # 'lines=True' ဆိုသည်မှာ ဖိုင်မှာ JSON Lines အမျိုးအစားဖြစ်ပြီး၊ တစ်ကြောင်းစီတိုင်းက JSON အရာဝတ္ထုတစ်ခုဖြစ်ကြောင်းကို မှတ်သားပါ
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame မှ စိတ်တိုင်းကျ ၁ စာကြောင်း ရွေးပါ
    # 'n=1' ဆိုသည်မှာ ရွေးချယ်မည့် စိတ်တိုင်းကျ စာကြောင်း အရေအတွက်ကို ဖေါ်ပြသည်
    test_df = test_df.sample(n=1)
    
    # DataFrame ၏ အညွှန်းတန်းကို ပြန်ဆက်တင်ပါ
    # 'drop=True' ဆိုသည်မှာ မူလ အညွှန်းတန်းကို ဖယ်ရှားပြီး ပုံမှန် အနည်းငယ် စာရင်းအလိုက် နံပါတ်အသစ်ဖြင့် အစားထိုးမှာ ဖြစ်သည်
    # 'inplace=True' ဆိုသည်မှာ DataFrame ကို နေရာတွင် တည်းဖြတ်မည်ဖြစ်ပြီး (အရာအသစ် ဖန်တီးခြင်းမရှိ) စနစ်ဖြစ်သည်
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame ၏ ပထမ ၂ စာကြောင်းကို ပြသပါ
    # သို့သော် စိတ်တိုင်းကျ ရွေးချယ်ခြင်းနောက် DataFrame မှာ စာကြောင်း ၁ စာသာ ပါသောကြောင့် တစ်ဆယ်တည်းကိုသာ ပြသမည် ဖြစ်သည်
    test_df.head(2)
    ```

### JSON Object ဖန်တီးခြင်း

1. ဒီ Python script က အထူးသတ်မှတ်ချက်များဖြင့် JSON object တစ်ခု ဖန်တီးပြီး ဖိုင်ထဲသို့ သိမ်းဆည်းနေသည်။ လုပ်ဆောင်ချက်များ -

    - JSON data ကို နှောင့်နှေးပြုလုပ်နိုင်သော ပံ့ပိုးမှုများ ပေးသည့် json module ကို import ပြုလုပ်သည်။
- ၎င်းသည် machine learning မော်ဒယ်အတွက် parameters ကို ကိုယ်စားပြုသော key များနှင့် value များပါသော dictionary parameters ကိုဖန်တီးသည်။ key များမှာ "temperature", "top_p", "do_sample", နှင့် "max_new_tokens" ဖြစ်ပြီး အဲ့ဒီတို့နှင့် ကိုက်ညီသည့် value များမှာ 0.6, 0.9, True, နှင့် 200 ဖြစ်သည်။

- ၎င်းသည် input_data နှင့် params ဆိုသော key နှစ်ခုပါသော test_json ဆိုသော အခြား dictionary ကိုဖန်တီးသည်။ "input_data" ၏ value သည် "input_string" နှင့် "parameters" ဆိုသော key များပါသော dictionary တစ်ခုဖြစ်သည်။ "input_string" ၏ value သည် test_df DataFrame ထဲမှ ပထမဆုံးသော စာတမ်းကို ပါဝင်သည့် list တစ်ခုဖြစ်သည်။ "parameters" ၏ value သည် အထက်ဖန်တီးခဲ့သော parameters dictionary ဖြစ်သည်။ "params" ၏ value သည် ဖွင့်လို့မရသော dictionary ဖြစ်သည်။

- sample_score.json အမည်ရှိ ဖိုင်ကိုဖွင့်သည်။

    ```python
    # JSON ဒေတာနှင့် အလုပ်လုပ်ရန် ကူညီသော function များကို ပေးသော json module ကို မိတ်ဆက်ပါ
    import json
    
    # machine learning မော်ဒယ်အတွက် ပါရာမီတာများကို ကိုယ်စားပြုသော key များနှင့် value များပါသော dictionary `parameters` ကို ဖန်တီးပါ
    # key များမှာ "temperature", "top_p", "do_sample", နှင့် "max_new_tokens" ဖြစ်ပြီး၊ ၎င်းတို့၏ သက်ဆိုင်ရာ value များမှာ 0.6, 0.9, True, နှင့် 200 ဖြစ်သည်
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # key နှစ်ခု "input_data" နှင့် "params" ပါသော dictionary တစ်ခု `test_json` ကို ဖန်တီးပါ
    # "input_data" ၏ value သည် "input_string" နှင့် "parameters" ဆိုသော key များပါရှိသည့် dictionary တစ်ခု ဖြစ်သည်
    # "input_string" ၏ value သည် `test_df` DataFrame မှ ပထမဆုံး message ကို ပါသည့် list တစ်ခု ဖြစ်သည်
    # "parameters" ၏ value သည် ယခင်ဖန်တီးခဲ့သော `parameters` dictionary ဖြစ်သည်
    # "params" ၏ value သည် အာဏာရွှေ့ထားသော dictionary အသစ်ဖြစ်သည်
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` ဖိုလ်ဒါအတွင်းရှိ `sample_score.json` ဖိုင်ကိုရေးရန် mode ဖြင့် ဖွင့်ပါ
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` function ကို အသုံးပြု၍ `test_json` dictionary ကို JSON ပုံစံဖြင့် ဖိုင်ထဲသို့ ရေးပါ
        json.dump(test_json, f)
    ```

### Endpoint ကို ခေါ်ယူခြင်း

1. ဒီ Python script မှာ Azure Machine Learning မှာရှိတဲ့ online endpoint တစ်ခုကို JSON ဖိုင်ကို score တင်ရန် ခေါ်ယူနေသည်။ ၎င်း၏ လုပ်ဆောင်ချက်ကို အောက်ပါအတိုင်း ခွဲခြမ်းတင်ပြပါသည်။

    - workspace_ml_client object ၏ online_endpoints property ၏ invoke method ကို ခေါ်သုံးသည်။ ဤ method သည် online endpoint ထံမှ ပြန်တောင်းခံချက် တင်ရန်နှင့် ပြန်လာသော response ကိုရယူရန် အသုံးပြုသည်။

    - endpoint နှင့် deployment အမည်များအား endpoint_name နှင့် deployment_name argument များဖြင့် သတ်မှတ်သည်။ ဤကိစ္စတွင် endpoint အမည်ကို online_endpoint_name variable ထဲသို့သိမ်းဆည်းပြီး deployment အမည်ကို "demo" ဟု သတ်မှတ်ထားသည်။

    - request_file argument ဖြင့် score တင်မည့် JSON ဖိုင် လမ်းကြောင်းအား သတ်မှတ်သည်။ ဤကိစ္စတွင် ဖိုင်သည် ./ultrachat_200k_dataset/sample_score.json ဖြစ်သည်။

    - endpoint မှ ပြန်လာသော response ကို response variable ထဲသို့ သိမ်းဆည်းသည်။

    - raw response ကို ပေါ်ပြ ပုံစံဖြင့် ပုံနှိပ်သည်။

1. အကျဉ်းချုပ်အားဖြင့် ဒီ script သည် Azure Machine Learning မှ online endpoint ကို ခေါ်ယူ၍ JSON ဖိုင်ကို score တင်ပြီး ပြန်လာသော response ကို ပုံနှိပ်သည်။

    ```python
    # Azure Machine Learning တွင် အွန်လိုင်း endpoint ကိုခေါ်ယူ၍ `sample_score.json` ဖိုင်ကို အမှတ်ပေးပါ
    # `workspace_ml_client` အရာဝတ္တု၏ `online_endpoints` ပိုင်ဆိုင်မှု၏ `invoke` နည်းလမ်းကို အသုံးပြုကာ အွန်လိုင်း endpoint သို့ တောင်းဆိုမှု ပို့၍ တုံ့ပြန်ချက် ရယူသည်
    # `endpoint_name` အချက်အလက်သည် မြှုပ်နှံ စက်တင်၏ အမည်ကို ဖော်ပြပြီး၊ ၎င်းကို `online_endpoint_name` မတိုင်မီကွဲထဲတွင် သိမ်းဆည်းထားသည်
    # `deployment_name` အချက်အလက်သည် မြှုပ်နှံမှု၏ အမည်ကို ဖော်ပြကာ၊ ၎င်းမှာ "demo" ဖြစ်သည်
    # `request_file` အချက်အလက်သည် အမှတ်ပေးရန် JSON ဖိုင်၏ လမ်းကြောင်းကို ဖော်ပြပြီး၊ ၎င်းမှာ `./ultrachat_200k_dataset/sample_score.json` ဖြစ်သည်
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Endpoint မှ ရရှိသော မီးမောင်းတိကျသော တုံ့ပြန်ချက်ကို ပုံနှိပ်ပါ
    print("raw response: \n", response, "\n")
    ```

## ၉။ online endpoint ကို ဖျက်ပစ်ခြင်း

1. online endpoint ကို ဖျက်ပစ်ရန် မမေ့ပါနှင့်၊ မဟုတ်လျှင် endpoint အသုံးပြုသည့် စျေးနှုန်း တိုင်းတာမှု မရှိမဖြစ် ဆက်လက်ပြေးဆဲ ဖြစ်နေပါလိမ့်မည်။ ဒီ Python code တစ်ကြောင်းသည် Azure Machine Learning အတွက် online endpoint တစ်ခုကို ဖျက်ပစ်နေသည်။ ၎င်း၏ လုပ်ဆောင်ချက်ကို အောက်ပါအတိုင်း ခွဲခြမ်းထားပါသည်။

    - workspace_ml_client object ၏ online_endpoints property ၏ begin_delete method ကို ခေါ်သည်။ ဤ method သည် online endpoint ဖျက်ပစ်ခြင်း စတင်ရန် အသုံးပြုသည်။

    - ဖျက်ပစ်မည့် endpoint အမည်ကို name argument ဖြင့် သတ်မှတ်သည်။ ဤကိစ္စတွင် endpoint အမည်ကို online_endpoint_name variable ထဲသို့ သိမ်းဆည်းထားသည်။

    - ဖျက်ပစ်ခြင်း လုပ်ငန်းဆောင်တာ ပြီးဆုံးရန် စောင့်ဆိုင်းရန် wait method ကို ခေါ်သည်။ ၎င်းသည် blocking operation ဖြစ်ပြီး ဖျက်ခြင်း ပြီးဆုံးသည်အထိ script မတိုးမပြေး နေပါ။

    - အကျဉ်းချုပ်အားဖြင့် ဒီ code မှာ Azure Machine Learning မှာရှိတဲ့ online endpoint ဖျက်ပစ်ခြင်း စတင်ပြီး လုပ်ငန်းဆောင်တာ ပြီးဆုံးရန် စောင့်ဆိုင်းနေသည်။

    ```python
    # Azure Machine Learning တွင် အွန်လိုင်း အဆုံးအပိုင်းကို ဖျက်ပါ
    # `workspace_ml_client` အရာဝတ္ထု၏ `online_endpoints` ပိုင်ဆိုင်မှု၏ `begin_delete` နည်းလမ်းကို အသုံးပြု၍ အွန်လိုင်း အဆုံးအပိုင်း ဖျက်ခြင်း စတင်သည်
    # `name` အကြောင်းအရာသည် ဖျက်မည့် အဆုံးအပိုင်း၏ နာမည်ကို ဖော်ပြပြီး၊ ၎င်းသည် `online_endpoint_name` အမျိုးအစားတွင် သိမ်းဆည်းထားသည်
    # ဖျက်ခြင်း လုပ်ငန်းစဉ်ပြီးဆုံးရန် အတွက် `wait` နည်းလမ်းကို ခေါ်သည်။ ဤသည်မှာ ခြုံငုံတားဆီးသော လုပ်ငန်းစဉ်ဖြစ်ပြီး၊ ဖျက်ခြင်း ပြီးဆုံးသည်အထိ စက္ကူ၏ ဆက်လုပ်ခြင်းကို တားမြစ်မည်ဖြစ်သည်
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**မှတ်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝဘ်ဆိုဒ် [Co-op Translator](https://github.com/Azure/co-op-translator) မှ အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်တော်တို့သည်မှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျှောက်ဘာသာပြန်မှုတွင် မှားယွင်းချက်များ သို့မဟုတ် မှန်ကန်မှုမပြည့်သည့် အချက်များပါဝင်နိုင်ကြောင်း သိရှိထားပေးကြပါရန် တိုက်တွန်းပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ ယုံကြည်စွာ ကိုးကားသင့်ပါသည်။ အရေးကြီးသည့် အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များ၏ ဘာသာပြန်ချက်ကို သင့်လျော်ပါသည်။ ဤဘာသာပြန်ချက် အသုံးပြုမှုမှ ဖြစ်ပေါ်နိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းဖော်ပြချက်များအတွက် ကျွန်တော်တို့ သက်ဆိုင်ချက်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->