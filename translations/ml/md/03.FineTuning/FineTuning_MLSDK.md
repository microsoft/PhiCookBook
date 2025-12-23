<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-12-21T17:41:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "ml"
}
-->
## Azure ML സിസ്റ്റം രജിസ്ട്രിയിൽ നിന്ന് ചാറ്റ്-കമ്പ്ലീഷൻ ഘടകങ്ങൾ ഉപയോഗിച്ച് മോഡൽ ഫൈൻട്യൂൺ ചെയ്യുന്നത് എങ്ങനെ

ഈ ഉദാഹരണത്തിൽ നാം Phi-3-mini-4k-instruct മോഡലിന്റെ ഫൈൻട്യൂൺ നടത്തിപ്പിലൂടെ ultrachat_200k ഡാറ്റാസെറ്റ് ഉപയോഗിച്ച് രണ്ട് ആളുകളിലുള്ള സംവാദം പൂർത്തിയാക്കുന്നതാണ്.

![എംഎൽ ഫൈൻട്യൂൺ](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.ml.png)

ഈ ഉദാഹരണം Azure ML SDKയും Pythonഉം ഉപയോഗിച്ച് എങ്ങനെ ഫൈൻട്യൂൺ നടത്താമെന്ന് കാണിക്കുകയും തുടർന്ന് ഫൈൻട്യൂൺ ചെയ്ത മോഡൽ റിയൽ-ടൈം ഇൻഫറൻസിനായി ഓൺലൈൻ എൻഡ്‌പോയന്റിലേക്ക് എങ്ങനെ ഡിപ്പ്ലോ ചെയ്യാമെന്നു കാണിക്കുകയും ചെയ്യും.

### പരിശീലന ഡാറ്റ

ഞങ്ങൾ ultrachat_200k ഡാറ്റാസെറ്റ് ഉപയോഗിക്കും. ഇത് UltraChat ഡാറ്റസെറ്റിന്റെ മോശം ഫിൽറ്റർ ചെയ്ത പതിപ്പാണ് மற்றும் Zephyr-7B-β എന്ന state-of-the-art 7b ചാറ്റ് മോഡൽ ട്രെയ്ൻ ചെയ്യാൻ ഇത് ഉപയോഗിച്ചിരുന്നു.

### മോഡൽ

ചാറ്റ്-കമ്പ്ലീഷൻ ടാസ്‍ക്കിന് മോഡൽ ഫൈൻട്യൂൺ ചെയ്യുന്നതു എങ്ങനെ കാണിക്കാൻ Phi-3-mini-4k-instruct മോഡൽ ഞങ്ങൾ ഉപയോഗിക്കും. നിങ്ങൾ ഈ നോട്ട്‌ബുക്ക് ഒരു പ്രത്യേക മോഡൽ കാർഡിൽ നിന്ന് തുറന്നിട്ടുണ്ടെങ്കിൽ, ആ പ്രത്യേക മോഡൽ നാമം മാറ്റുന്നതു ഓർക്കുക.

### ടാസ്ക്കുകൾ

- ഫൈൻട്യൂൺ ചെയ്യാൻ ഒരു മോഡൽ തിരഞ്ഞെടുക്കുക.
- പരിശീലന ഡാറ്റ തിരഞ്ഞെടുക്കുകയും പരിശോധിക്കുകയും ചെയ്യുക.
- ഫൈൻട്യൂൺ ജോബ് കോൺഫിഗർ ചെയ്യുക.
- ഫൈൻട്യൂൺ ജോബ് നടത്തുക.
- ട്രെയിനിംഗ് మరియు മൂല്യനിർണയ മെട്രിക്ക്സ് അവലോകനം ചെയ്യുക.
- ഫൈൻട്യൂൺ ചെയ്ത മോഡൽ രജിസ്റ്റർ ചെയ്യുക.
- റിയൽ ടൈം ഇൻഫറൻസിന് ഫൈൻട്യൂൺ ചെയ്ത മോഡൽ ഡെപ്ലോ ചെയ്യുക.
- റിസോഴ്‌സുകൾ ക്ലീൻ അപ് ചെയ്യുക.

## 1. മുൻ‌അവശ്യങ്ങൾ സജ്ജമാക്കൽ

- ഡിപെൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക
- AzureML Workspace-കോട് ബന്ധിപ്പിക്കുക. കൂടുതൽ വിവരം set up SDK authentication ൽ കാണുക. താഴെ <WORKSPACE_NAME>, <RESOURCE_GROUP> and <SUBSCRIPTION_ID> മാറ്റുക.
- azureml സിസ്റ്റം രജിസ്ട്രിയുമായി കണക്ട് ചെയ്യുക
- ഒരു ഓപ്‌ഷണൽ എക്സ്‌പെരിമെന്റ് നാമം സജ്ജമാക്കുക
- കംപ്യൂട്ട് പരിശോധിക്കുക അല്ലെങ്കിൽ സൃഷ്ടിക്കുക.

> [!NOTE]
> Requirements a single GPU node can have multiple GPU cards. For example, in one node of Standard_NC24rs_v3 there are 4 NVIDIA V100 GPUs while in Standard_NC12s_v3, there are 2 NVIDIA V100 GPUs. Refer to the docs for this information. The number of GPU cards per node is set in the param gpus_per_node below. Setting this value correctly will ensure utilization of all GPUs in the node. The recommended GPU compute SKUs can be found here and here.

### Python ലൈബ്രറികൾ

താഴെയുള്ള സെൽ 실행ചെയ്യുന്നതിലൂടെ ആശ്രിതത്വങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക. പുതിയ എൻവയോൺമെന്റിൽ നടത്തുമ്പോൾ ഇത് ഐച്ഛിക ഘട്ടമല്ല.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML-നോടൊപ്പം ഇടപഴകൽ

1. ഈ Python സ്ക്രിപ്റ്റ് Azure Machine Learning (Azure ML) സേവനവുമായി ഇടപഴകാൻ ഉപയോഗിക്കുന്നു. ഇത് ചെയ്യുന്ന കാര്യങ്ങളുടെ വിഭജനം താഴെ നൽകിയിരിക്കുന്നു:

    - ഇത് azure.ai.ml, azure.identity, and azure.ai.ml.entities പാക്കേജുകളിൽ നിന്നുള്ള ആവശ്യമായ മോഡ്യൂളുകൾ ഇമ്പോർട്ട് ചെയ്യുന്നു. കൂടാതെ time മോഡ്യൂളും ഇമ്പോർട്ട് ചെയ്യുന്നു.

    - ഇത് DefaultAzureCredential() ഉപയോഗിച്ച് ഓതെന്റിക്കേറ്റ് ചെയ്യാൻ ശ്രമിക്കുന്നു, ഇത് Azure ക്ലൗഡിൽ പ്രവർത്തിക്കുന്ന ಅಪ്ലിക്കേഷനുകൾ വേഗത്തിൽ വികസിപ്പിക്കാൻ സഹായിക്കുന്ന ലളിതമായ ഓതെന്റിക്കേഷൻ അനുഭവം നൽകുന്നു. ഇത് പരാജയപ്പെടുകയാണെങ്കിൽ, InteractiveBrowserCredential() എന്നതിലേക്ക് ഫാൾബാക്ക് ചെയ്യുന്നു, ഇത് ഇന്ററാക്ടീവ് ലോഗിൻ പ്രേംപ്റ്റ് നൽകുന്ന രീതിയാണ്.

    - തുടർന്ന് ഇത് from_config രീതി ഉപയോഗിച്ച് MLClient ഇന്സ്റ്റൻസ് സൃഷ്ടിക്കാൻ ശ്രമിക്കുന്നു, ഇത് ഡീഫോൾട് കോൺഫിഗ് ഫയൽ(config.json) നിന്നുള്ള കോൺഫിഗറേഷൻ വായിക്കുന്നു. ഇത് പരാജയപ്പെടുകയാണെങ്കിൽ, subscription_id, resource_group_name, এবং workspace_name കൈമാറുന്ന വഴി MLClient ഇന്സ്റ്റൻസ് ക്രമീകരിക്കുന്നു.

    - പിന്നീട് ഇത് "azureml" എന്ന നാമമുള്ള Azure ML രജിസ്ട്രിക്ക് വേണ്ടി മറ്റൊരു MLClient ഇന്സ്റ്റൻസ് സൃഷ്ടിക്കുന്നു. ഈ രജിസ്ട്രിയിൽ മോഡലുകൾ, ഫൈൻട്യൂൺ пайപ്‌ലൈനുകൾ, എൻവയോൺമെന്റുകൾ എന്നിവ സംഭരിക്കുന്നതാണ്.

    - experiment_name "chat_completion_Phi-3-mini-4k-instruct" ആയി സെറ്റ് ചെയ്യുന്നു.

    - ഇപ്പോഴത്തെ ടൈംസ്റ്റാമ്പ് സെക്കൻഡുകൾ ആയി കൈക്കൊണ്ടു int ഒപ്പം string ആയി മാറ്റി ഒരു യൂണിക് ടൈംസ്റ്റാമ്പ് ജനറേറ്റ് ചെയ്യുന്നു. ഈ ടൈംസ്റ്റാമ്പ് ഐന്യു നിർമാണം നാമങ്ങൾക്കും വേർഷനുകൾക്കും ഉപയോഗിക്കാം.

    ```python
    # Azure ML-യും Azure Identity-യും നിന്നുള്ള ആവശ്യമായ മൊഡ്യൂളുകൾ ഇറക്കുമതി ചെയ്യുക
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # time മോഡ്യൂൾ ഇറക്കുമതി ചെയ്യുക
    
    # DefaultAzureCredential ഉപയോഗിച്ച് പ്രാമാണീകരിക്കാന്‍ ശ്രമിക്കുക
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # DefaultAzureCredential പരാജയപ്പെട്ടാൽ InteractiveBrowserCredential ഉപയോഗിക്കുക
        credential = InteractiveBrowserCredential()
    
    # ഡിഫോൾട്ട് കോൺഫിഗറേഷൻ ഫയൽ ഉപയോഗിച്ച് MLClient ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കാൻ ശ്രമിക്കുക
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # അത് പരാജയപ്പെട്ടാൽ, വിശദാംശങ്ങൾ മാനുവലായി നൽകി MLClient ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # azureml എന്ന പേരിലുള്ള Azure ML രജിസ്ട്രിക്ക് വേണ്ടി മറ്റൊരു MLClient ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
    # ഈ രജിസ്ട്രിയിൽ മോഡലുകൾ, ഫൈൻ-ട്യൂണിംഗ് പൈപ്പ്ലൈനുകൾ, എൻവയോൺമെന്റുകൾ എന്നിവ സൂക്ഷിച്ചിരിക്കുന്നു
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # എക്സ്പെരിമെന്റിന്റെ പേര് നിശ്ചയിക്കുക
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # വ്യത്യസ്തമായ നാമങ്ങൾക്കും പതിപ്പുകൾക്കും ഉപയോഗിക്കാവുന്ന ഒരു വ്യക്തമായ ടൈംസ്റ്റാമ്പ് (സമയമുദ്ര) സൃഷ്ടിക്കുക
    timestamp = str(int(time.time()))
    ```

## 2. ഫൗണ്ടേഷൻ മോഡൽ ഫൈൻട്യൂൺ ചെയ്യാൻ തിരഞ്ഞെടുക്കുക

1. Phi-3-mini-4k-instruct ആണ് 3.8B പാരമീറ്ററുകൾ ഉള്ള, ലഘുവായ, state-of-the-art ഓപ്പൺ മോഡൽ, ഇത് Phi-2 ൽ ഉപയോഗിച്ച ഡാറ്റാസെറ്റുകൾ അടിസ്ഥാനമാക്കി നിർമ്മിച്ചിരിക്കുന്നു. മോഡൽ Phi-3 മോഡൽ കുടുംബത്തിൽ genetic ആണ്, Mini പതിപ്പ് 4K आणि 128K എന്ന വ്യതിയാനങ്ങളിലുണ്ട് — ഇതാണ് ഇത് പിന്തുണയ്ക്കുന്ന കോൺടെക്സ്റ്റ് ദൈর্ঘ്യം (ടോക്കൺസിൽ). നമുക്ക് ഇത് ഉപയോഗിക്കാൻ വീക്ഷണാനുസരിച്ച് മോഡൽ ഫൈൻട്യൂൺ ചെയ്യേണ്ടതുണ്ട്. AzureML Studio-യിലെ Model Catalogൽ ചാറ്റ്-കമ്പ്ലീഷൻ ടാസ്‌ക് ഫിൽട്ടർ ചെയ്ത് ഈ മോഡലുകളെ ബ്രൗസ് ചെയ്യാം. ഈ ഉദാഹരണത്തിൽ Phi-3-mini-4k-instruct മോഡൽ ഉപയോഗിക്കുന്നു. നിങ്ങൾ ഈ നോട്ട്‌ബുക്ക് വ്യത്യസ്ത മോഡലിനായി തുറന്നിട്ടുണ്ടെങ്കിൽ, മോഡൽ നാമവും വേർഷനും അനുയോജ്യമായി മാറ്റുക.

    > [!NOTE]
    > the model id property of the model. This will be passed as input to the fine tuning job. This is also available as the Asset ID field in model details page in AzureML Studio Model Catalog.

2. ഈ Python സ്ക്രിപ്റ്റ് Azure Machine Learning (Azure ML) സേവനവുമായി ഇടപഴകുന്നു. ഇതിന്റെ പ്രവർത്തനം താഴെ വിശദീകരിച്ചിട്ടുണ്ട്:

    - ഇത് model_name "Phi-3-mini-4k-instruct" ആയി സെറ്റ് ചെയ്യുന്നു.

    - registry_ml_client ഒബ്ജക്റ്റിന്റെ models പ്രോപ്പർട്ടിയുടെ get മെത്തഡ് ഉപയോഗിച്ച് നൽകിയ നാമമുള്ള മോഡലിന്റെ ലേറ്റസ്റ്റ് വേർഷൻ റജിസ്ട്രിയിൽ നിന്നും നേടുന്നു. get മെത്തഡ് രണ്ട് ആർഗുമെന്റുകൾ കൊണ്ട് വിളിക്കുന്നു: മോഡലിന്റെ നാമം மற்றும் അതിന്റെ ഏറ്റവും പുതിയ വേർഷൻ ലഭ്യമാക്കാൻ ഉപയോഗിക്കുന്ന ലേബൽ.

    - fine-tuning-യ്ക്ക് ഉപയോഗിക്കുന്ന മോഡല്ലുടെ നാമം, വേർഷൻ, id എന്നിവ കൺസോളിൽ പ്രിന്റ് ചെയ്യാൻ ഒരു മെസേജ് പ്രിന്റ് ചെയ്യുന്നു. സ്റ്റ്രിംഗ്.format മെത്തഡ് ഉപയോഗിച്ച് foundation_model ഒബ്ജക്റ്റിന്റെ name, version, id പ്രോപ്പർട്ടികൾ മെസേജിലേക്ക് ഇന്റർപൊളേറ്റ് ചെയ്യുന്നു.

    ```python
    # മോഡലിന്റെ പേര് സജ്ജമാക്കുക
    model_name = "Phi-3-mini-4k-instruct"
    
    # Azure ML റജിസ്ട്രിയിൽ നിന്നുള്ള മോഡലിന്റെ ഏറ്റവും പുതിയ പതിപ്പ് നേടുക
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # മോഡലിന്റെ പേര്, പതിപ്പ്, ഐഡി പ്രിന്റ് ചെയ്യുക
    # ട്രാക്കിംഗിനും ഡീബഗിംഗിനും ഈ വിവരങ്ങൾ ഉപകാരപ്പെടും
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. ജോബിനായി ഉപയോഗിക്കേണ്ട കംപ്യൂട്ട് സൃഷ്ടിക്കുക

ഫൈൻട്യൂൺ ജോബ് GPU കംപ്യൂട്ടിനോടെയാണ് മാത്രമുളളത്. കംപ്യൂട്ടിന്റെ വലുപ്പം മോഡലിന്റെ വലുപ്പത്തെ ആശ്രയിച്ചിരിക്കുന്നു, കൂടാതെ പലപ്പോഴെങ്കിലും ശരിയായ കംപ്യൂട്ട് കണ്ടെത്തുന്നത് സങ്കീർണമായിരിക്കും. ഈ സെലിൽ നാം ഉപയോക്താവിനെ ശരിയായ കംപ്യൂട്ട് തിരഞ്ഞെടുക്കുന്നതിന് മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു.

> [!NOTE]
> The computes listed below work with the most optimized configuration. Any changes to the configuration might lead to Cuda Out Of Memory error. In such cases, try to upgrade the compute to a bigger compute size.

> [!NOTE]
> While selecting the compute_cluster_size below, make sure the compute is available in your resource group. If a particular compute is not available you can make a request to get access to the compute resources.

### ഫൈൻട്യൂണിംഗിനുള്ള പിന്തുണയ്ക്ക് മോഡൽ പരിശോധിക്കൽ

1. ഈ Python സ്ക്രിപ്റ്റ് ఒక Azure Machine Learning മോഡലുമായി ഇടപഴകുന്നു. ഇതാണ് അതിന്റെ പ്രവർത്തനം:

    - ഇത് ast മോഡ്യൂൾ ഇമ്പോർട്ട് ചെയ്യുന്നു, Python-ന്റെ ആബ്‌ട്രാക്റ്റ് സിന്റാക്‌സ് ട്രീ പ്രോസസ് ചെയ്യുന്നതിനുള്ള ഫംഗ്ഷനുകൾ ഇത് നൽകുന്നു.

    - foundation_model ഒബ്ജക്റ്റിനു finetune_compute_allow_list എന്ന ടാഗ് ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു. Azure ML-ൽ ടാഗുകൾ കീ-വാല്യു പേറുകളാണ്, മോഡലുകൾ ഫിൽറ്റർ ചെയ്യാനും സോർട്ട് ചെയ്യാനും ഇവ ഉപയോഗിക്കുന്നു.

    - finetune_compute_allow_list ടാഗ് നിലവിലുണ്ടെങ്കിൽ, ast.literal_eval ഫംഗ്ഷൻ ഉപയോഗിച്ച് ടാഗിന്റെ മൂല്യം (ഒരു സ്ട്രിംഗ് ആയിരിക്കും) സുരക്ഷിതമായി Python ലിസ്റ്റായി പാർസ് ചെയ്യുന്നു. ആ ലിസ്റ്റ് computes_allow_list 변수 ആയി ഏൽക്കുന്നു. തുടർന്ന് ലിസ്റ്റിൽ നിന്നുള്ള ഒന്നിൽ നിന്നുള്ള compute സൃഷ്ടിക്കണമെന്ന് സൂചിപ്പിക്കുന്ന മെസേജ് പ്രിന്റ് ചെയ്യുന്നു.

    - finetune_compute_allow_list ടാഗ് നിലവിലില്ലെങ്കിൽ, computes_allow_list None ആയി സജ്ജമാക്കുന്നു և മോഡലിന്റെ ടാഗുകളിൽ finetune_compute_allow_list ഇല്ലെന്ന മെസേജ് പ്രിന്റ് ചെയ്യുന്നു.

    - ഖണ്ഡപരമായായി, ഈ സ്ക്രിപ്റ്റ് മോഡൽ മെടാഡാറ്റയിൽ ഒരു പ്രത്യേക ടാഗ് പരിശോധിക്കുന്നു, അതിന്റെ മൂല്യം ഉണ്ടെങ്കിൽ അവയെ ഒരു ലിസ്റ്റായി പരിവർത്തനം ചെയ്യുന്നു, അതിനുശേഷം ഉപയോക്താവിന് ഫീഡ്‌ബാക്ക് നൽകുന്നു.

    ```python
    # Python പദരചനയുടെ (abstract syntax grammar) വൃക്ഷങ്ങൾ പ്രോസസ് ചെയ്യുന്നതിനുള്ള ഫംഗ്ഷനുകൾ നൽകുന്ന ast മോഡ്യൂൾ ഇറക്കുമതി ചെയ്യുക
    import ast
    
    # മോഡലിന്റെ ടാഗുകളിൽ 'finetune_compute_allow_list' ടാഗ് നിലവിലുണ്ടോ എന്നത് പരിശോധിക്കുക
    if "finetune_compute_allow_list" in foundation_model.tags:
        # ടാഗ് ഉണ്ടായാൽ, ടാഗിന്റെ മൂല്യം (ഒരു സ്ട്രിംഗ്) സുരക്ഷിതമായി Python ലിസ്റ്റിലേക്ക് പാഴ്‌സ് ചെയ്യാൻ ast.literal_eval ഉപയോഗിക്കുക
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # സ്ട്രിംഗ് Python ലിസ്റ്റിലേക്ക് മാറ്റുക
        # ലിസ്റ്റിൽ നിന്ന് compute സൃഷ്ടിക്കണമെന്ന് സൂചിപ്പിക്കുന്ന ഒരു സന്ദേശം പ്രിന്റ് ചെയ്യുക
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # ടാഗ് ഇല്ലെങ്കിൽ computes_allow_list നെ None ആയി സജ്ജീകരിക്കുക
        computes_allow_list = None
        # മോഡലിന്റെ ടാഗുകളുടെ ഭാഗമായിട്ടില്ലാത്തതായി 'finetune_compute_allow_list' ടാഗ് ഇല്ലെന്ന് സൂചിപ്പിക്കുന്ന സന്ദേശം പ്രിന്റ് ചെയ്യുക
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### കംപ്യൂട്ട് ഇൻസ്റ്റൻസ് പരിശോധിക്കൽ

1. ഈ Python സ്ക്രിപ്റ്റ് Azure Machine Learning (Azure ML) സേവനവുമായി ഇടപഴകുകയും ഒരു കംപ്യൂട്ട് ഇൻസ്റ്റൻസിൽ പല പരിശോധനകളും നടത്തുകയും ചെയ്യുന്നു. ഇതാണ് അതിന് പുലർത്തുന്ന വിശേഷണങ്ങൾ:

    - compute_cluster എന്ന നാമത്തിലുള്ള compute ഇൻസ്റ്റൻസ് Azure ML വർക്ക്‌സ്പേസിൽ നിന്ന് നേടാൻ ശ്രമിക്കുന്നു. compute ഇൻസ്റ്റൻസിന്റെ provisioning state "failed" ആണെങ്കിൽ ValueError ഉയര്‍ത്തുന്നു.

    - computes_allow_list None അല്ലെങ്കില്‍, ലിസ്റ്റിലുള്ള എല്ലാ compute സൈസുകളും lowercase ആയി മാറ്റി നിലവിലെ compute ഇൻസ്റ്റൻസിന്റെ size അത് ലിസ്റ്റിൽ ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു. ഇല്ലെങ്കിൽ ValueError ഉയർത്തുന്നു.

    - computes_allow_list None ആണെങ്കിൽ, compute ഇൻസ്റ്റൻസിന്റെ സൈസ് unsupported GPU VM sizes ലിസ്റ്റിൽ ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു. ഉണ്ടെങ്കിൽ ValueError ഉയർത്തപ്പെടും.

    - വർക്ക്‌സ്പേസിൽ ലഭ്യമായ എല്ലാ compute sizes ലിസ്റ്റ് നേടുന്നു. ശേഷം ആ ലിസ്റ്റ് iterate ചെയ്ത് ഓരോ compute size-ഉം പരിശോധിക്കുന്നു; അതിന്റെ name നിലവിലെ compute ഇൻസ്റ്റൻസിന്റെ size നെ അനുസരിപ്പിക്കുന്നുണ്ടെങ്കിൽ, ആ compute size-യുടെ GPUs എണ്ണം നേടുകയും gpu_count_found True ആയി സജ്ജമാക്കുകയും ചെയ്യുന്നു.

    - gpu_count_found True ആണെങ്കിൽ compute ഇൻസ്റ്റൻസിലുള്ള GPU-കളുടെ എണ്ണം പ്രിന്റ് ചെയ്യുന്നു. gpu_count_found False ആണെങ്കിൽ ValueError ഉയർത്തുന്നു.

    - സംക്ഷേപത്തിൽ, ഈ സ്ക്രിപ്റ്റ് Azure ML വർക്ക്‌സ്പേസിൽ ഒരു compute ഇൻസ്റ്റൻസിനെ കുറിച്ച് provisioning state, allow list/deny list അനുസരിച്ച് അതിന്റെ size എന്നീ നിലകളിൽ നിരവധി ചെക്കുകൾ നടത്തുന്നു, കൂടാതെ അതിലെ GPU-കളുടെ എണ്ണം പരിശോധിക്കുന്നു.
    
    ```python
    # എക്സെപ്ഷന്റെ സന്ദേശം പ്രിന്റ് ചെയ്യുക
    print(e)
    # വർക്ക്സ്പേസിൽ കമ്പ്യൂട്ട് സൈസ് ലഭ്യമല്ലെങ്കിൽ ValueError ഉയർത്തുക
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML വർക്ക്സ്പേസിൽ നിന്നുള്ള കമ്പ്യൂട്ട് ഇൻസ്റ്റൻസ് നേടുക
    compute = workspace_ml_client.compute.get(compute_cluster)
    # കമ്പ്യൂട്ട് ഇൻസ്റ്റൻസിന്റെ provisioning സ്റ്റേറ്റ് "failed" ആണോ എന്ന് പരിശോധിക്കുക
    if compute.provisioning_state.lower() == "failed":
        # provisioning സ്റ്റേറ്റ് "failed" ആണെങ്കിൽ ValueError ഉയർത്തുക
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # computes_allow_list None അല്ലെന്ന് പരിശോധിക്കുക
    if computes_allow_list is not None:
        # computes_allow_list-ഇൽ ഉള്ള എല്ലാ compute സൈസുകളും lowercase ആക്കുക
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # compute ഇൻസ്റ്റൻസിന്റെ സൈസ് computes_allow_list_lower_case-ൽഉള്ളതാണോ എന്ന് പരിശോധിക്കുക
        if compute.size.lower() not in computes_allow_list_lower_case:
            # compute ഇൻസ്റ്റൻസിന്റെ സൈസ് computes_allow_list_lower_case-ൽ ഇല്ലെങ്കിൽ ValueError ഉയർത്തുക
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # അസഹായകമായ GPU VM സൈസുകൾ ഉള്ള ഒരു ലിസ്റ്റ് നിർവചിക്കുക
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # compute ഇൻസ്റ്റൻസിന്റെ സൈസ് unsupported_gpu_vm_list-ലുണ്ടോ എന്ന് പരിശോധിക്കുക
        if compute.size.lower() in unsupported_gpu_vm_list:
            # compute ഇൻസ്റ്റൻസിന്റെ സൈസ് unsupported_gpu_vm_list-ലുണ്ടെങ്കിൽ ValueError ഉയർത്തുക
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # compute ഇൻസ്റ്റൻസിലെ GPU-കളുടെ എണ്ണം കണ്ടെത്തിയിട്ടുണ്ടോ എന്ന് പരിശോധിക്കാൻ ഒരു ഫ്ലാഗ് ഇൻഷ്യലൈസ് ചെയ്യുക
    gpu_count_found = False
    # വർക്ക്സ്പേസിൽ ലഭ്യമായ എല്ലാ compute സൈസുകളുടെ ലിസ്റ്റ് സ്വീകരിക്കുക
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # ലഭ്യമായ compute സൈസുകളുടെ ലിസ്റ്റിലൂടെ ആവർത്തിക്കുക
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # compute സൈസിന്റെ പേര് compute ഇൻസ്റ്റൻസിന്റെ സൈസുമായി പൊരുത്തപ്പെടുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക
        if compute_sku.name.lower() == compute.size.lower():
            # അത് പൊരുത്തപ്പെടുകയാണെങ്കിൽ ആ compute സൈസിന് ഉള്ള GPU-കളുടെ എണ്ണം നേടിയെടുക്കുകയും gpu_count_found നു True അസൈൻ ചെയ്യുകയും ചെയ്യുക
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # gpu_count_found True ആണെങ്കിൽ compute ഇൻസ്റ്റൻസിലെ GPU-കളുടെ എണ്ണം പ്രിന്റ് ചെയ്യുക
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # gpu_count_found False ആണെങ്കിൽ ValueError ഉയർത്തുക
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. മോഡൽ ഫൈൻട്യൂണിംഗിനായി ഡാറ്റാസെറ്റ് തിരഞ്ഞെടുക്കുക

1. ഞങ്ങൾ ultrachat_200k ഡാറ്റാസെറ്റ് ഉപയോഗിക്കുന്നു. ഡാറ്റാസെറ്റിന് നാല് സ്പ്ലിറ്റുകൾ ഉണ്ട്, Supervised fine-tuning (sft) ന് അനുയോജ്യമാണ്. Generation ranking (gen). ഓരോ സ്പ്ലിറ്റിനും ഉള്ള സാമ്പിളുകളുടെ എണ്ണം താഴെ കൊടുക്കുന്നിങ്ങനെ കാണിക്കുന്നു:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. അടുത്ത ഉള്ള സെലുകൾ ചില അടിസ്ഥാന ഡേറ്റാ തയ്യാറെടുപ്പുകൾ ഫൈൻട്യൂണിംഗിനായി കാണിക്കുന്നു:

### ചില ഡേറ്റാ റോകൾ വിസ്വലൈസ് ചെയ്യുക

ഈ സാമ്പിൾ വേഗത്തിൽ ഓടാൻ ഞങ്ങൾ train_sft, test_sft ഫയലുകൾ സംഭരിച്ച് അവയിൽ നിന്ന് ഇതിനകം ട്രിമ്മുചെയ്‌ത വരികളുടെ 5% മാത്രം ഉപയോഗിച്ച് സേവ് ചെയ്യാൻ ശ്രമിക്കുന്നു. അതിനാൽ ഫൈൻട്യൂൺ ചെയ്ത മോഡലിന്റെ അക്യൂറസി കുറവ് ആയിരിക്കുമെന്നും അതുകൊണ്ട് യാഥാർത്ഥ്യ ഉപയോഗത്തിന് ആ മോഡൽ ഉപയോഗിക്കരുതെന്നും മനസ്സിലാക്കുക.
download-dataset.py ultrachat_200k ഡാറ്റാസെറ്റ് ഡൗൺലോഡുചെയ്യാനും ഡാറ്റാസെറ്റ് ഫൈൻട്യൂൺ പൈപ്പ്‌ലൈനു അനുയോജ്യമായ ഫോർമാറ്റിലേക്ക് മാറ്റാനും ഉപയോഗിക്കുന്നു. ഡാറ്റാസെറ്റ് വലുതാണ്, അതുകൊണ്ടുതന്നെ ഇവിടെ ഞങ്ങൾക്ക് ഡാറ്റാസെറ്റിന്റെ മാത്രം ഭാഗം മാത്രമേ ഉണ്ടായിരിക്കൂ.

1. താഴെ നൽകിയ സ്ക്രിപ്റ്റ് റൺ ചെയ്യുന്നത് ഡാറ്റയുടെ 5% മാത്രം ഡൗൺലോഡ് ചെയ്യുന്നു. ഇത് dataset_split_pc പാരാമീറ്റർ ആവശ്യമായ ശതമാനത്തുകമായി മാറ്റി വർദ്ധിപ്പിക്കാൻ കഴിയും.

    > [!NOTE]
    > Some language models have different language codes and hence the column names in the dataset should reflect the same.

1. ഡാറ്റ എങ്ങനെ കാണിക്കണം എന്നതിന് ഒരു ഉദാഹരണം ഇനിപ്പറയുന്ന വിധമാണ്
ചാറ്റ്-കമ്പ്ലീഷൻ ഡാറ്റാസെറ്റ് parquet ഫോർമാറ്റിൽ സൂക്ഷിച്ചിരിക്കുന്നു, ഓരോ എൻട്രിയും താഴെ നൽകിയ സ്‌കീമ ഉപയോഗിക്കുന്നു:

    - ഇത് ഒരു JSON (JavaScript Object Notation) ഡോക്യുമെന്റാണ്, ഒരു സാധാരണ ഡാറ്റ ഇന്റർചേഞ്ച് ഫോർമാറ്റ്. ഇത് എക്സിക്യൂട്ടेबल കോഡ് അല്ല, പക്ഷേ ഡാറ്റ സ്റ്റോർ ചെയ്യാനും കൈമാറാനുമുള്ള ഒരു മാർഗ്ഗമാണ്. ഇതിന്റെ ഘടനയുടെ വിഭജനമേത് ചുവടെ കൊടുക്കുന്നു:

    - "prompt": ഈ കീ ഒരു സ്ട്രിംഗ് മൂല്യം കൈവശം വയ്ക്കുന്നു, അത് AI അസിസ്റ്റന്റിനോട് ചോദിക്കപ്പെടുന്ന ഒരു ടാസ്‌ക് അല്ലെങ്കിൽ ചോദ്യം പ്രതിനിധീകരിക്കുന്നു.

    - "messages": ഈ കീ ഒബ്ജക്റ്റുകളുടെ ഒരു അറേ കൈവശം വയ്ക്കുന്നു. ഓരോ ഒബ്ജക്റ്റും ഉപയോക്താവും AI അസിസ്റ്റന്റും തമ്മിലുള്ള ഒരു സംവാദത്തിലെ ഒരു സന്ദേശത്തെ പ്രതിനിധീകരിക്കുന്നു. ഓരോ message ഒബ്ജക്റ്റിന്റെയും രണ്ട് കീകൾ ഉണ്ട്:

    - "content": ഈ കീ ഒരു സ്ട്രിംഗ് മൂല്യം കൈവശം വെക്കുന്നു, ഇത് സന്ദേശത്തിന്റെ ഉള്ളടക്കം പ്രതിനിധീകരിക്കുന്നു.
    - "role": ഈ കീ ഒരു സ്ട്രിംഗ് മൂല്യം കൈവശം വെക്കുന്നു, ഇത് സന്ദേശം അയച്ചുള്ള ഐഡന്റിറ്റിയുടെ ഭുമിക (role) പ്രതിനിധീകരിക്കുന്നു. ഇത് "user" അല്ലെങ്കിൽ "assistant" ആകാമെന്നർത്ഥമാണ്.
    - "prompt_id": ഈ കീ ഒരു സ്ട്രിംഗ് മൂല്യം കൈവശം വെക്കുന്നു, ഇത് prompt ന്റെ یونീക് ഐഡന്റിഫയർ ആണ്.

1. ഈ പ്രത്യേക JSON ഡോക്യുമെന്റിൽ, ഒരു ഉപയോക്താവ് AI അസിസ്റ്റന്റിനോട് ഒരു ഡിസ്റ്റോപിയൻ കഥയ്ക്കുള്ള പ്രധാന കഥാപാത്രത്തെ സൃഷ്ടിക്കാൻ ചോദിക്കുന്നു എന്ന തരത്തിൽ സംവാദം പ്രതിനിധീകരിച്ചിരിക്കുന്നു. അസിസ്റ്റന്റ് പ്രതികരിക്കുകയും, പിന്നീട് ഉപയോക്താവ് കൂടുതൽ വിശദാംശങ്ങൾ ചോദിക്കുകയും ചെയ്യുന്നു. അസിസ്റ്റന്റ് കൂടുതൽ വിശദാംശങ്ങൾ നൽകാൻ സമ്മതിക്കുന്നു. സമ്പൂർണ്ണ സംവാദം ഒരു പ്രത്യേക prompt id-യുമായി ബന്ധിപ്പിച്ചിരിക്കുന്നു.

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

### ഡാറ്റ ഡൗൺലോഡ് ചെയ്യുക

1. ഈ Python സ്ക്രിപ്റ്റ് download-dataset.py എന്ന ഹെൽപ്പർ സ്ക്രിപ്റ്റ് ഉപയോഗിച്ച് ഒരു ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യാൻ ഉപയോഗിക്കുന്നു. ഇത് ചെയ്യുന്നതിന്റെ വിഭജനം ചുവടെ കൊടുത്തിരിക്കുന്നു:

    - ഇത് os മോഡ്യൂൾ ഇമ്പോർട്ട് ചെയ്യുന്നു, ഏറ്റവും സൗകര്യപ്രദമായ രീതിയിൽ ഓപ്പറേറ്റിംഗ് സിസ്റ്റം ആശ്രിത ഫംഗ്ഷനലിറ്റി ഉപയോഗിക്കാൻ ഇത് അവസരം നൽകുന്നു.

    - ഇത് os.system ഫംഗ്ഷൻ ഉപയോഗിച്ച് shell-ൽ download-dataset.py സ്ക്രിപ്റ്റ് നിർദിഷ്ട കോമാൻഡ്-ലൈൻ ആർഗ്യുമെന്റുകൾ ഉപയോഗിച്ച് നടത്തുന്നു. ആർഗ്യുമെന്റുകൾ ഡൗൺലോഡ് ചെയ്യാനുള്ള ഡാറ്റാസെറ്റ് (HuggingFaceH4/ultrachat_200k), ഡൗൺലോഡ് ചെയ്യാനുള്ള ഡയറക്ടറി (ultrachat_200k_dataset), және dataset_split percentage (5) എന്നിവ വ്യക്തമാക്കുന്നു. os.system കോൺമാന്റിന്റെ എക്സിറ്റ് സ്റ്റാറ്റസ് തിരികെയൊടുക്കുന്നു; ഈ സ്റ്റാറ്റസ് exit_status 변수യിൽ സൂക്ഷിക്കുന്നു.

    - exit_status 0 അല്ലെങ്കിൽ നന്നാവില്ലെങ്കിൽ, Unix-പോലുള്ള ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങളിലെ 0 സാധാരണമായി വിജയത്തെ സൂചിപ്പിക്കുന്നു; മറ്റെല്ലാ സംഖ്യകളും പിശകിനെ സൂചിപ്പിക്കുന്നു. exit_status 0 അല്ലെങ്കിൽ എങ്കിൽ ഇത് ഒരു Exception ഉയർത്തുന്നു, ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യുന്നതിൽ പിശക് സംഭവിച്ചുവെന്ന സന്ദേശത്തോടുകൂടി.

    - സംക്ഷേപത്തിൽ, ഈ സ്ക്രിപ്റ്റ് ഹെൽപ്പർ സ്ക്രിപ്റ്റ് ഉപയോഗിച്ച് ഒരു ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യുന്നതിന് ഒരു കളവു ഓർഡർ ഓടിക്കുന്നു, ആ കമാൻഡ് പരാജയപ്പെടുന്നില്ലെങ്കിൽ Exception ഉയർത്തുന്നു.
    
    ```python
    # os മോഡ്യൂൾ ഇറക്കുമതി ചെയ്യുക, ഇത് ഓപ്പറേറ്റിംഗ് സിസ്റ്റം ആശ്രയിച്ചുള്ള പ്രവർത്തനങ്ങൾ ഉപയോഗിക്കാൻ ഒരു മാർഗം നൽകുന്നു
    import os
    
    # os.system ഫംഗ്ഷൻ ഉപയോഗിച്ച് download-dataset.py സ്ക്രിപ്റ്റ് നിശ്ചിത കമാൻഡ്-ലൈൻ ആർഗ്യൂമന്റുകളോടെ ഷെല്ലിൽ നടത്തുക
    # ആർഗ്യൂമെന്റ്‌സുകൾ ഡౌൺലോഡ് ചെയ്യാനുള്ള ഡാറ്റാസെറ്റ് (HuggingFaceH4/ultrachat_200k), അത് ഡൗൺലോഡ് ചെയ്യാനുള്ള ഡയറക്ടറി (ultrachat_200k_dataset), കൂടാതെ ഡാറ്റാസെറ്റിന്റെ വിഭജിപ്പിന്റെ ശതമാനം (5) നിർവ്വചിക്കുന്നു
    # os.system ഫംഗ്ഷൻ അത് നടപ്പിലാക്കിയ കമാൻഡിന്റെ നിർഗമന നില റിട്ടേൺ ചെയ്യുന്നു; ഈ നില exit_status എന്ന വെരിയബിളിൽ സൂക്ഷിക്കുന്നു
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # exit_status 0 അല്ലാതെയാണോ എന്ന് പരിശോധിക്കുക
    # Unix പോലുള്ള ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങളില, എക്സിറ്റ് സ്റ്റാറ്റസ് 0 സാധാരണയായി ഒരു കമാൻഡ് വിജയിച്ചിരുന്നതാണ് സൂചിപ്പിക്കുന്നത്, മറ്റ് ഏതെങ്കിലും സംഖ്യ പിശക് സൂചിപ്പിക്കുന്നു
    # exit_status 0 അല്ലെങ്കിൽ, ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്തപ്പോൾ ഒരു പിശക് ഉണ്ടായതായി സൂചിപ്പിക്കുന്ന ഒരു സന്ദേശത്തോടെ Exception ഉയർത്തുക
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### pandas DataFrame-ലേക്ക് ഡാറ്റ ലോഡ് ചെയ്യുന്നത്

1. ഈ Python സ്ക്രിപ്റ്റ് ഒരു JSON Lines ഫയൽ pandas DataFrame-ലേക്ക് ലോഡ് ചെയ്യുകയും ആദ്യ 5 മാറ്റുകൾ പ്രദർശിപ്പിക്കുകയും ചെയ്യുന്നു. ഇതിന്റെ പ്രവർത്തനങ്ങളുടെ വിഭജനം ചുവടെ കൊടുക്കുന്നു:

    - ഇത് pandas ലൈബ്രറി ഇമ്പോർട്ട് ചെയ്യുന്നു, ഇത് ശക്തമായ ഡാറ്റ മാനിപുലേഷൻ ആൻഡ് അനാലിറ്റിക്സ് ലൈബ്രറിയാണ്.

    - pandas' display options-ൽ മാക്സിമം കോളം വീതം 0 ആയി സജ്ജമാക്കുന്നു. ഇതുവഴി DataFrame പ്രിന്റ് ചെയ്യുമ്പോൾ ഓരോ കോളത്തിലെ മുഴുവൻ ടെക്സ്റ്റും മുറിക്കാതെ പ്രദർശിപ്പിക്കും.
    - It uses the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame. The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object.

    - It uses the head method to display the first 5 rows of the DataFrame. If the DataFrame has less than 5 rows, it will display all of them.

    - In summary, this script is loading a JSON Lines file into a DataFrame and displaying the first 5 rows with full column text.
    
    ```python
    # pandas ലൈബ്രറി ഇറക്കുമതി ചെയ്യുക; ഇത് ഡാറ്റ കൈകാര്യം ചെയ്യലിലും വിശകലനത്തിലും ശക്തിയുള്ള ഒരു ലൈബ്രറിയാണ്
    import pandas as pd
    
    # pandas ന്റെ പ്രദർശന ഓപ്ഷനുകളിൽ കോളത്തിന്റെ പരമാവധി വീതിയെ 0 ആയി സജ്ജമാക്കുക
    # ഇത്ന്നർത്ഥം DataFrame പ്രിന്റ് ചെയ്യുമ്പോൾ ഓരോ കോളത്തിന്റെയും മുഴുവൻ ടെക്സ്റ്റും ചെറുക്കലുകൾ ഇല്ലാതെ കാണിക്കും
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json ഫംഗ്ഷൻ ഉപയോഗിച്ച് ultrachat_200k_dataset ഡയറക്ടറിയിലുള്ള train_sft.jsonl ഫയൽ ഒരു DataFrame ആയി ലോഡ് ചെയ്യുക
    # lines=True എന്ന argument മൂടൽ ഫയൽ JSON Lines ഫോർമാറ്റിലാണ് എന്ന് സൂചിപ്പിക്കുന്നു; ആ ഫോർമാറ്റിൽ ഓരോ വരിയും ഒരു പ്രത്യേകം JSON ഒബ്‌ജക്റ്റായിരിക്കും
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # head മെതഡ് ഉപയോഗിച്ച് DataFrame-ന്റെ ആദ്യ 5 വരികൾ പ്രദർശിപ്പിക്കുക
    # DataFrame-ിൽ 5-ൽ കുറവ് വരികൾ ഉണ്ടെങ്കിൽ, അത് അവയെല്ലാം പ്രദർശിപ്പിക്കും
    df.head()
    ```

## 5. മോഡലും ഡാറ്റയും ഇൻപുട്ടായാക്കി ഫൈൻ‑ട്യൂൺ ജോബ് സമർപ്പിക്കുക

chat-completion pipeline component ഉപയോഗിക്കുന്ന ജോബ് സൃഷ്ടിക്കുക. ഫൈൻ‑ട്യൂണിംഗിനായി പിന്തുണയുള്ള എല്ലാ പാരാമീറ്ററുകളും കൂടുതൽ അറിയാൻ വായിക്കുക.

### Fine­tune പരാമീറ്ററുകൾ നിർവചിക്കുക

1. Finetune parameters രണ്ട് വിഭാഗങ്ങളായി ക്രമീകരിക്കാവുന്നതാണ് - training parameters, optimization parameters

1. Training parameters പരിശീലനക്ഷമതകൾ നിർവചിക്കുന്നു, ഉദാഹരണത്തിന് -

    - ഏത് optimizer, scheduler ഉപയോഗിക്കണമെന്ന്
    - ഫൈൻ‑ട്യൂൺ മെത്രിക്ക് ഏത് വികസിപ്പിക്കണമെന്ന്
    - പരിശീലന നടപടികളുടെ എണ്ണം, batch size മുതലായവ
    - Optimization parameters GPU മെമ്മറി ഓപ്റ്റിമൈസുചെയ്യാനും compute resources ഫലപ്രദമായി ഉപയോഗിക്കാനും സഹായിക്കുന്നു. 

1. താഴെ ഈ വിഭാഗത്തിൽപ്പെട്ട ചില പാരാമീറ്ററുകൾ നൽകിയിരിക്കുന്നു. optimization parameters ഓരോ മോഡലിനും വ്യത്യസ്തമാണ് და ഈ വ്യത്യാസങ്ങൾ കൈകാര്യം ചെയ്യാൻ മോഡലോടൊപ്പം പാക്കുചെയ്യപ്പെടുന്നു.

    - deepspeed and LoRA ενεργപ്പെടുത്തുക
    - mixed precision training ενεργപ്പെടുത്തുക
    - multi-node training ενεργപ്പെടുത്തുക

> [!NOTE]
> Supervised finetuning may result in loosing alignment or catastrophic forgetting. We recommend checking for this issue and running an alignment stage after you finetune.

### Fine Tuning Parameters

1. This Python script is setting up parameters for fine-tuning a machine learning model. Here's a breakdown of what it does:

    - It sets up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type.

    - It sets up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage.

    - It combines the training and optimization parameters into a single dictionary called finetune_parameters.

    - It checks if the foundation_model has any model-specific default parameters. If it does, it prints a warning message and updates the finetune_parameters dictionary with these model-specific defaults. The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary.

    - It prints the final set of fine-tuning parameters that will be used for the run.

    - In summary, this script is setting up and displaying the parameters for fine-tuning a machine learning model, with the ability to override the default parameters with model-specific ones.

    ```python
    # ഡിഫോൾട്ട് ട്രെയിനിംഗ് പാരാമീറ്ററുകൾ ക്രമീകരിക്കുക, ഉദാ. ട്രെയിനിംഗ് എപ്പോക്കുകളുടെ എണ്ണം, ട്രെയിൻ ചെയ്യുന്നതിനും മൂല്യമാറ്റത്തിനും ഉള്ള ബാച്ച് സൈസുകൾ, ലേണിംഗ് റേറ്റ്, ലേണിംഗ് റേറ്റ് ഷെഡ്യൂളറിന്റെ തരം
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Layer-wise Relevance Propagation (LoRa) പ്രയോഗിക്കണമോ DeepSpeed ഉപയോഗിക്കണമോ എന്നിവയും DeepSpeed സ്റ്റേജും ഉൾപ്പെടെ ഡിഫോൾട്ട് ഓപ്റ്റിമൈസേഷൻ പാരാമീറ്ററുകൾ സൂചിപ്പിക്കുക
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # training-യും optimization-ഉം സംബന്ധിച്ച പാരാമീറ്ററുകൾ finetune_parameters എന്നു പേരായ ഒരു ഒറ്റ ഡിക്ഷണറിയിൽ സംയോജിപ്പിക്കുക
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # foundation_model-ക്കു മോഡൽ-നിർദ്ദിഷ്ടമായ ഏതെങ്കിലും ഡിഫോൾട്ട് പാരാമീറ്ററുകൾ ഉണ്ടോ എന്ന് പരിശോധിക്കുക
    # എങ്കിൽ ഒരു മുന്നറിയിപ്പ് സന്ദേശം പ്രിന്റ് ചെയ്തുകൊണ്ട് ഈ മോഡൽ-നിർദ്ദിഷ്ട ഡിഫോൾട്ടുകൾ finetune_parameters ഡിക്ഷണറിയിൽ അപ്ഡേറ്റ് ചെയ്യുക
    # മോഡൽ-നിർദ്ദിഷ്ട ഡിഫോൾട്ടുകൾ സ്ട്രിംഗിൽ നിന്നു Python ഡിക്ഷണറിയിലേക്ക് മാറ്റാൻ ast.literal_eval ഫംഗ്ഷൻ ഉപയോഗിക്കുന്നു
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # സ്ട്രിംഗ് Python ഡിക്ഷണറിയായി മാറ്റുക
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # റൺ ചെയ്യുന്നതിനായി ഉപയോഗിക്കേണ്ട അന്തിമ ഫൈൻ-ട്യൂണിംഗ് പാരാമീറ്ററുകളുടെ സെറ്റ് പ്രിന്റ് ചെയ്യുക
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Training Pipeline

1. This Python script is defining a function to generate a display name for a machine learning training pipeline, and then calling this function to generate and print the display name. Here's a breakdown of what it does:

1. The get_pipeline_display_name function is defined. This function generates a display name based on various parameters related to the training pipeline.

1. Inside the function, it calculates the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning.

1. It retrieves various other parameters such as the learning rate scheduler type, whether DeepSpeed is applied, the DeepSpeed stage, whether Layer-wise Relevance Propagation (LoRa) is applied, the limit on the number of model checkpoints to keep, and the maximum sequence length.

1. It constructs a string that includes all these parameters, separated by hyphens. If DeepSpeed or LoRa is applied, the string includes "ds" followed by the DeepSpeed stage, or "lora", respectively. If not, it includes "nods" or "nolora", respectively.

1. The function returns this string, which serves as the display name for the training pipeline.

1. After the function is defined, it is called to generate the display name, which is then printed.

1. In summary, this script is generating a display name for a machine learning training pipeline based on various parameters, and then printing this display name.

    ```python
    # ട്രെയ്നിംഗ് പൈപ്പ്‌ലൈനിന് വേണ്ടി ഡിസ്‌പ്ലേ പേര് സൃഷ്ടിക്കാൻ ഒരു ഫംഗ്ഷൻ നിർവചിക്കുക
    def get_pipeline_display_name():
        # പ്രതി-ഡിവൈസ് ബാച്ച് സൈസ്, ഗ്രേഡിയന്റ് ആക്യൂമുലേഷൻ ഘട്ടങ്ങളുടെ എണ്ണം, ഓരോ നോഡിലേയും GPUകളുടെ എണ്ണം, ഫൈൻ-ട്യൂണിങിന് ഉപയോഗിച്ച നോഡുകളുടെ എണ്ണം എന്നിവ ഗുണിച്ച് മൊത്തം ബാച്ച് സൈസ് കണക്കാക്കുക
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # ലേണിംഗ് റേറ്റ് ഷെഡ്യൂള്ളറിന്റെ തരം ലഭ്യമാക്കുക
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # DeepSpeed പ്രയോഗിച്ചിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # DeepSpeed ഘട്ടം (സ്റ്റേജ്) നേടുക
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # DeepSpeed പ്രയോഗിച്ചാൽ ഡിസ്‌പ്ലേ നാമത്തിൽ DeepSpeed ഘട്ടം അനുസരിച്ച് "ds" ഉൾപ്പെടുത്തുക; അല്ലെങ്കിൽ "nods" ഉൾപ്പെടുത്തുക
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Layer-wise Relevance Propagation (LoRa) പ്രയോഗിച്ചിട്ടുണ്ടോ എന്ന് കണ്ടെത്തുക
        lora = finetune_parameters.get("apply_lora", "false")
        # LoRa പ്രയോഗിച്ചാൽ ഡിസ്‌പ്ലേ നാമത്തിൽ "lora" ഉൾപ്പെടുത്തുക; അല്ലെങ്കിൽ "nolora" ഉൾപ്പെടുത്തുക
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # സംരക്ഷിക്കാൻ വിന്യസിക്കുന്ന മോഡൽ ചെക്ക്പോയിന്റുകളുടെ പരമാവധി പരിധി നേടുക
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # പരമാവധി സീക്വൻസ് നീളം നേടുക
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # ഈ എല്ലാ പാരാമീറ്ററുകളും ഹൈഫൻ(−) ഉപയോഗിച്ച് വേർതിരിച്ച് ചേർത്ത് ഡിസ്‌പ്ലേ നാമം രൂപപ്പെടുത്തുക
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
    
    # ഡിസ്‌പ്ലേ പേര് സൃഷ്ടിക്കാൻ ഫംഗ്ഷൻ വിളിക്കുക
    pipeline_display_name = get_pipeline_display_name()
    # ഡിസ്‌പ്ലേ പേര് പ്രിന്റ് ചെയ്യുക
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configuring Pipeline

This Python script is defining and configuring a machine learning pipeline using the Azure Machine Learning SDK. Here's a breakdown of what it does:

1. It imports necessary modules from the Azure AI ML SDK.

1. It fetches a pipeline component named "chat_completion_pipeline" from the registry.

1. It defines a pipeline job using the `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, meaning that the pipeline will stop if any step fails.

1. In summary, this script is defining and configuring a machine learning pipeline for a chat completion task using the Azure Machine Learning SDK.

    ```python
    # Azure AI ML SDK-യിൽ നിന്നും ആവശ്യമായ മാഡ്യൂളുകൾ ഇറക്കുമതി ചെയ്യുക
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # റജിസ്ട്രിയിൽ നിന്നുള്ള "chat_completion_pipeline" എന്ന പേരുള്ള പൈപ്പ്ലൈൻ ഘടകം നേടുക
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline ഡെക്കറേറ്ററും create_pipeline ഫംഗ്ഷനും ഉപയോഗിച്ച് പൈപ്പ്ലൈൻ ജോബ് നിർവ്വചിക്കുക
    # പൈപ്പ്ലൈന്റെ പേര് pipeline_display_name ആയി സജ്ജമാക്കിയിരിക്കുന്നു
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # എറണെടുത്ത പൈപ്പ്ലൈൻ ഘടകത്തെ വിവിധ പാരാമീറ്ററുകളോടെ ആരംഭിക്കുക
        # ഇതിൽ മോഡൽ പാത്ത്, വ്യത്യസ്ത ഘട്ടങ്ങൾക്ക് compute ക്ലസ്റ്ററുകൾ, ട്രെയിനിംഗിനും ടെസ്റ്റിംഗിനും dataset വിഭജനങ്ങൾ, ഫൈന്ട്യൂണിംഗിനുള്ള GPUകളുടെ എണ്ണം, മറ്റ് ഫൈന്ട്യൂണിംഗ് പാരാമീറ്ററുകൾ എന്നിവ ഉൾപ്പെടുന്നു
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # dataset വിഭജനങ്ങളെ പാരാമീറ്ററുകളോട് മാപ്പ് ചെയ്യുക
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # ട്രെയിനിംഗ് ക്രമീകരണങ്ങൾ
            number_of_gpu_to_use_finetuning=gpus_per_node,  # compute-ൽ ലഭ്യമായ GPUകളുടെ എണ്ണമായി സജ്ജമാക്കുക
            **finetune_parameters
        )
        return {
            # ഫൈന്ട്യൂണിംഗ് ജോബിന്റെ ഔട്ട്പുട്ടിനെ പൈപ്പ്ലൈൻ ജോബിന്റെ ഔട്ട്പുട്ടുമായി മാപ്പ് ചെയ്യുക
            # ഫൈന്ട്യൂൺ ചെയ്ത മോഡൽ എളുപ്പത്തിൽ രജിസ്റ്റർ ചെയ്യാൻ ഇത് ചെയ്യുന്നു
            # മോഡൽ ഓൺലൈൻ അല്ലെങ്കിൽ ബാച്ച് എൻഡ്‌പോയിന്റിലേക്ക് ഡിപ്ലോയുചെയ്യാൻ രജിസ്‌ട്രേഷൻ ആവശ്യമാണ്
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline ഫംഗ്ഷൻ വിളിച്ച് പൈപ്പ്ലൈന്റെ ഒരു ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
    pipeline_object = create_pipeline()
    
    # മുൻ ജോബുകളിൽ നിന്നുള്ള കാഷെ ഫലങ്ങൾ ഉപയോഗിക്കരുത്
    pipeline_object.settings.force_rerun = True
    
    # ഒരു സ്റ്റെപ്പ് പരാജയപ്പെട്ടാൽ തുടരുക എന്ന ക്രമീകരണം False ആയി സജ്ജമാക്കുക
    # ഇതിന്റെ അർത്ഥം എന്തെന്നാൽ ഏതെങ്കിലും ഒരു സ്റ്റെപ്പ് പരാജയപ്പെട്ടാൽ പൈപ്പ്ലൈൻ നിർത്തപ്പെടും
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Submit the Job

1. This Python script is submitting a machine learning pipeline job to an Azure Machine Learning workspace and then waiting for the job to complete. Here's a breakdown of what it does:

    - It calls the create_or_update method of the jobs object in the workspace_ml_client to submit the pipeline job. The pipeline to be run is specified by pipeline_object, and the experiment under which the job is run is specified by experiment_name.

    - It then calls the stream method of the jobs object in the workspace_ml_client to wait for the pipeline job to complete. The job to wait for is specified by the name attribute of the pipeline_job object.

    - In summary, this script is submitting a machine learning pipeline job to an Azure Machine Learning workspace, and then waiting for the job to complete.

    ```python
    # പൈപ്പ്‌ലൈൻ ജോബിനെ Azure Machine Learning വർക്ക്സ്പെയ്‌സിലേക്ക് സമർപ്പിക്കുക
    # ഓടിക്കാനുള്ള പൈപ്പ്‌ലൈൻ pipeline_object ഉപയോഗിച്ച് വ്യക്തമാക്കിയിരിക്കുന്നു
    # ജോബ് ഓടുന്ന പരീക്ഷണം experiment_name എന്നതിലൂടെ നിർദ്ദേശിച്ചിരിക്കുന്നു
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # പൈപ്പ്‌ലൈൻ ജോബ് പൂർത്തിയാവുന്നതുവരെ കാത്തിരിക്കുക
    # കാത്തിരിക്കേണ്ട ജോബ് pipeline_job ഒബ്ജക്റ്റിന്റെ name ആട്രിബ്യൂട്ടിലൂടെ നിർദ്ദേശിച്ചിരിക്കുന്നു
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. ഫൈൻ‑ട്യൂൺ ചെയ്ത മോഡൽ വർക്ക്സ്പേസിൽ രജിസ്റ്റർ ചെയ്യുക

ഫൈൻ‑ട്യൂണിംഗ് ജോബിന്റെ ഔട്ട്പുട്ടിൽ നിന്നുള്ള മോഡൽ രജിസ്റ്റർ ചെയ്യും. ഇത് ഫൈൻ‑ട്യൂൺ ചെയ്ത മോഡലും ഫൈൻ‑ട്യൂൺ ജോബുമുകൾ തമ്മിലുള്ള lineage ട്രാക്ക് ചെയ്യാൻ സഹായിക്കും. ഫൈൻ‑ട്യൂൺ ജോബ് വീണ്ടും foundation model, data, training code എന്നിവയിലേക്കുള്ള lineage ട്രാക്ക് ചെയ്യും.

### ML മോഡൽ രജിസ്റ്റർ ചെയ്യൽ

1. This Python script is registering a machine learning model that was trained in an Azure Machine Learning pipeline. Here's a breakdown of what it does:

    - It imports necessary modules from the Azure AI ML SDK.

    - It checks if the trained_model output is available from the pipeline job by calling the get method of the jobs object in the workspace_ml_client and accessing its outputs attribute.

    - It constructs a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model").

    - It defines a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens.

    - It prepares to register the model by creating a Model object with various parameters, including the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model.

    - It registers the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument.

    - It prints the registered model.

1. In summary, this script is registering a machine learning model that was trained in an Azure Machine Learning pipeline.
    
    ```python
    # Azure AI ML SDK-ൽ നിന്നുള്ള ആവശ്യമായ മോഡ്യൂളുകൾ ഇമ്പോർട്ട് ചെയ്യുക
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # pipeline job-ൽ നിന്നുള്ള `trained_model` output ലഭ്യമാണോ എന്ന് പരിശോധിക്കുക
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # pipeline job-ന്റെ പേര് ಮತ್ತು ഔട്ട്പുട്ട് നാമം ("trained_model") ഉപയോഗിച്ച് ഒരു സ്ട്രിംഗ് ഫോർമാറ്റ് ചെയ്ത് ട്രെയിൻ ചെയ്ത മോഡലിലേക്ക് ഒരു പാത്ത് നിർമ്മിക്കുക
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # മൂല മോഡൽ നാമത്തിന് "-ultrachat-200k" ചേർത്ത് സ്ലാഷുകൾ ഹൈഫൻകൾ ആയി മാറ്റുകയും അതിലൂടെ ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡലിന് ഒരു പേര് നിർവചിക്കുക
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # വിവിധ പാരാമീറ്ററുകൾ ഉപയോഗിച്ച് ഒരു Model ഒബ്ജക്ട് സൃഷ്ടിച്ച് മോഡൽ രജിസ്റ്റർ ചെയ്യാൻ തയ്യാറെടുക്കുക
    # ഇതിൽ മോഡലിന്റെ പാത്ത്, മോഡലിന്റെ തരം (MLflow മോഡൽ), മോഡലിന്റെ പേര്, പതിപ്പ്, കൂടാതെ മോഡലിന്റെ വിവരണം എന്നിവ ഉൾപ്പെടുന്നു
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # പതിപ്പ് തർക്കം ഒഴിവാക്കാൻ പതിപ്പായി ടൈംസ്റ്റാമ്പ് ഉപയോഗിക്കുക
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Model ഒബ്ജക്ടിനെ ആർഗ്യൂമെന്റായി നൽകി workspace_ml_client-യിലെ models ഒബ്ജക്ടിന്റെ create_or_update മെതഡ് വിളിച്ച് മോഡൽ രജിസ്റ്റർ ചെയ്യുക
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # രജിസ്റ്റർചെയ്‌ത മോഡൽ പ്രിന്റ് ചെയ്യുക
    print("registered model: \n", registered_model)
    ```

## 7. ഫൈൻ‑ട്യൂൺ ചെയ്ത മോഡൽ ഓൺലൈൻ എന്റ്പോയ്ൻറായി ഡിപ്പ്ലോയ് ചെയ്യുക

ഓൺലൈൻ എന്റ്പോയിന്റുകൾ സ്ഥിരതയുള്ള REST API നൽകുന്നു, ആപ്‌ലിക്കേഷനുകളുമായി സംയോജിപ്പിക്കാൻ ഇത് ഉപയോഗിക്കാവുന്നതാണ്.

### Endpoint കൈകാര്യം ചെയ്യൽ

1. This Python script is creating a managed online endpoint in Azure Machine Learning for a registered model. Here's a breakdown of what it does:

    - It imports necessary modules from the Azure AI ML SDK.

    - It defines a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-".

    - It prepares to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters, including the name of the endpoint, a description of the endpoint, and the authentication mode ("key").

    - It creates the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument. It then waits for the creation operation to complete by calling the wait method.

1. In summary, this script is creating a managed online endpoint in Azure Machine Learning for a registered model.

    ```python
    # Azure AI ML SDK-ൽ നിന്നുള്ള ആവശ്യമായ മോഡ്യൂളുകൾ ഇറക്കുമതി ചെയ്യുക
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # ടൈംസ്റാമ്പ് ചേർത്ത് "ultrachat-completion-" എന്ന സ്ട്രിംഗ് ചേർത്ത് ഓൺലൈൻ എൻഡ്‌പോയിന്റിന് ഒരു അനന്യമായ പേര് നിർവ്വചിക്കുക
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # വിവിധ പാരാമീറ്ററുകളോടെ ManagedOnlineEndpoint ഓബ്ജക്ട് സൃഷ്ടിച്ച് ഓൺലൈൻ എൻഡ്‌പോയിന്റ് സൃഷ്ടിക്കാൻ തയ്യാറെടുക്കുക
    # ഇതിൽ എൻഡ്‌പോയിന്റിന്റെ പേര്, എൻഡ്‌പോയിന്റിന്റെ വിവരണം, ഒപ്പം പ്രാമാണീകരണ മോഡ് ("key") ഉൾപ്പെടുന്നു
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint ഓബ്ജക്ടിനെ ആർഗ്യുമെന്റ് ആയി നൽകി workspace_ml_client-യുടെ begin_create_or_update മെതഡ് വിളിച്ച് ഓൺലൈൻ എൻഡ്‌പോയിന്റ് സൃഷ്ടിക്കുക
    # തുടർന്ന് wait മെതഡ്Invocation വിളിച്ച് സൃഷ്ടി പ്രവർത്തനം പൂർത്തിയായെന്ന് വരെയൊഴുക്ക് വരെ കാത്തിരിക്കുക
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> You can find here the list of SKU's supported for deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML മോഡൽ ഡിപ്പ്ലോയ്മെന്റ്

1. This Python script is deploying a registered machine learning model to a managed online endpoint in Azure Machine Learning. Here's a breakdown of what it does:

    - It imports the ast module, which provides functions to process trees of the Python abstract syntax grammar.

    - It sets the instance type for the deployment to "Standard_NC6s_v3".

    - It checks if the inference_compute_allow_list tag is present in the foundation model. If it is, it converts the tag value from a string to a Python list and assigns it to inference_computes_allow_list. If it's not, it sets inference_computes_allow_list to None.

    - It checks if the specified instance type is in the allow list. If it's not, it prints a message asking the user to select an instance type from the allow list.

    - It prepares to create the deployment by creating a ManagedOnlineDeployment object with various parameters, including the name of the deployment, the name of the endpoint, the ID of the model, the instance type and count, the liveness probe settings, and the request settings.

    - It creates the deployment by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineDeployment object as the argument. It then waits for the creation operation to complete by calling the wait method.

    - It sets the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment.

    - It updates the endpoint by calling the begin_create_or_update method of the workspace_ml_client with the endpoint object as the argument. It then waits for the update operation to complete by calling the result method.

1. In summary, this script is deploying a registered machine learning model to a managed online endpoint in Azure Machine Learning.

    ```python
    # Python-യിലെ അബ്സ്ട്രാക്റ്റ് സിന്താക്‌സ് വ്യാകരണത്തിന്റെ ട്രീകൾ പ്രോസസ് ചെയ്യാനുള്ള ഫംഗ്ഷനുകൾ നൽകുന്ന ast മോഡ്യൂൾ ഇറക്കുമതിയാക്കുക
    import ast
    
    # ഡിപ്ലോയ്‌മെന്റിനായുള്ള ഇൻസ്റ്റൻസ് തരം നിശ്ചയിക്കുക
    instance_type = "Standard_NC6s_v3"
    
    # ഫൗണ്ടേഷൻ മോഡലിൽ `inference_compute_allow_list` ടാഗ് ഉണ്ടായിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക
    if "inference_compute_allow_list" in foundation_model.tags:
        # അത് ഉണ്ടെങ്കിൽ, ടാഗ് മൂല്യം സ്ട്രിങ്ങിൽ നിന്നു Python ലിസ്റ്റിലേക്ക് പരിവർത്തനം ചെയ്ത് `inference_computes_allow_list`-ലേക്ക് നിയോഗിക്കുക
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # അതല്ലെങ്കിൽ, `inference_computes_allow_list`-നെ `None` ആയി സജ്ജമാക്കുക
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # നിർദ്ദിഷ്ട ഇൻസ്റ്റൻസ് തരം അനുവദനലിസ്റ്റിൽ ഉണ്ടോ എന്ന് പരിശോധിക്കുക
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # വിവിധ പാരാമീറ്ററുകളോടെ `ManagedOnlineDeployment` ഒബ്ജക്റ്റ് സൃഷ്ടിച്ച് ഡിപ്ലോയ്മെന്റ് സൃഷ്ടിക്കാൻ തയ്യാറെടുക്കുക
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `ManagedOnlineDeployment` ഒബ്ജക്റ്റ് argument ആയി നൽകി `workspace_ml_client`-ന്റെ `begin_create_or_update` മെത്തഡ് വിളിച്ച് ഡിപ്ലോയ്മെന്റ് സൃഷ്ടിക്കുക
    # പിന്നെയെ സൃഷ്ടി ഓപ്പറേഷൻ പൂർത്തിയാവുന്നത് വരെ `wait` മെത്തഡ് വിളിച്ച് കാത്തിരിക്കുക
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # എൻഡ്‌പോയിന്റിന്റെ ട്രാഫിക് 100% 'demo' ഡിപ്ലോയ്മെന്റിലേക്ക് നേരിട്ട് അയക്കിവെക്കുക
    endpoint.traffic = {"demo": 100}
    
    # `endpoint` ഒബ്ജക്റ്റ് argument ആയി നൽകി `workspace_ml_client`-ന്റെ `begin_create_or_update` മെത്തഡ് വിളിച്ച് എൻഡ്‌പോയിന്റ് അപ്‌ഡേറ്റ് ചെയ്യുക
    # പിന്നെ അപ്‌ഡേറ്റ് ഓപ്പറേഷൻ പൂർത്തിയാവുന്നത് വരെ `result` മെത്തഡ് വിളിച്ച് കാത്തിരിക്കുക
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. സാമ്പിൾ ഡാറ്റ ഉപയോഗിച്ച് എന്റ്ഡ്പോയിന്റ് ടെസ്റ്റ് ചെയ്യുക

ടെസ്റ്റ് ഡാറ്റാസെറ്റിൽ നിന്നുള്ള ചില സാമ്പിൾ ഡാറ്റയെ ഓൺലൈൻ എന്റ്പോയിന്റ്‌ക്കു ഇന്ഫെറൻസ്‌ക്കായി സമർപ്പിക്കും. തുടർന്ന് സ്കോർ ചെയ്ത ലേബലുകൾ ഗ്രൗണ്ട്‑ട്രൂത്ത് ലേബലുകളോട് ചേർത്തുതരുന്നത് കാണിക്കും.

### ഫലം വായിക്കുക

1. This Python script is reading a JSON Lines file into a pandas DataFrame, taking a random sample, and resetting the index. Here's a breakdown of what it does:

    - It reads the file ./ultrachat_200k_dataset/test_gen.jsonl into a pandas DataFrame. The read_json function is used with the lines=True argument because the file is in JSON Lines format, where each line is a separate JSON object.

    - It takes a random sample of 1 row from the DataFrame. The sample function is used with the n=1 argument to specify the number of random rows to select.

    - It resets the index of the DataFrame. The reset_index function is used with the drop=True argument to drop the original index and replace it with a new index of default integer values.

    - It displays the first 2 rows of the DataFrame using the head function with the argument 2. However, since the DataFrame only contains one row after the sampling, this will only display that one row.

1. In summary, this script is reading a JSON Lines file into a pandas DataFrame, taking a random sample of 1 row, resetting the index, and displaying the first row.
    
    ```python
    # pandas ലൈബ്രറി ഇംപോർട്ട് ചെയ്യുക
    import pandas as pd
    
    # JSON Lines ഫയൽ './ultrachat_200k_dataset/test_gen.jsonl' pandas DataFrame ആയി വായിക്കുക
    # 'lines=True' ആർഗ്യുമെന്റ് ഫയൽ JSON Lines ഫോർമാറ്റിലാണ് എന്ന് സൂചിപ്പിക്കുന്നു, ഇവിടെ ഓരോ ലൈനും ഒരു പ്രത്യേക JSON ഒബ്ജക്റ്റാണ്
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame-ൽ നിന്ന് 1 വരിയുടെ റാൻഡം സാമ്പിൾ എടുക്കുക
    # 'n=1' ആർഗ്യുമെന്റ് തിരഞ്ഞെടുക്കാവുന്ന യാദൃച്ഛിക വരികളുടെ എണ്ണം നിർണ്ണയിക്കുന്നു
    test_df = test_df.sample(n=1)
    
    # DataFrame-ന്റെ ഇൻഡക്സ് റീസെറ്റ് ചെയ്യുക
    # 'drop=True' ആർഗ്യുമെന്റ് പഴയ ഇൻഡക്സ് നീക്കം ചെയ്ത് അതിന്റെ സ്ഥാനത്ത് ഡിഫോൾട്ട് പൂർണ്ണസംഖ്യകൾ ഉള്ള പുതിയ ഇൻഡക്സ് ഉപയോഗിക്കുന്നതായി സൂചിപ്പിക്കുന്നു
    # 'inplace=True' ആർഗ്യുമെന്റ് DataFrame ഒരു പുതിയ ഒബ്ജക്റ്റ് സൃഷ്ടിക്കാതെ തന്നെ അതിൽ നേരിട്ട് മാറ്റങ്ങൾ നടത്തണമെന്ന് സൂചിപ്പിക്കുന്നു
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame-ന്റെ ആദ്യ 2 വരികൾ പ്രദർശിപ്പിക്കുക
    # എന്നിരുന്നാലും, സാമ്പിളിംഗ് കഴിഞ്ഞപ്പോൾ DataFrame-ൽ ഒരു വരി മാത്രമേ ഉണ്ടായിരിക്കൂ എന്ന് കൊണ്ടത് ആ ഒറ്റ വരി മാത്രം പ്രദർശിപ്പിക്കും
    test_df.head(2)
    ```

### JSON ഒബ്രജക്ട് സൃഷ്ടിക്കുക

1. This Python script is creating a JSON object with specific parameters and saving it to a file. Here's a breakdown of what it does:

    - It imports the json module, which provides functions to work with JSON data.
    - ഇത് machine learning മോഡലിന് പാരാമീറ്ററുകൾ പ്രതിനിധീകരിക്കുന്ന കീകളും മൂല്യങ്ങളും ഉള്ള ഒരു dictionary parameters സൃഷ്ടിക്കുന്നു. കീകൾ "temperature", "top_p", "do_sample", "max_new_tokens" എന്നിവയാകുന്നു, അവയുടെ കീപ്രകാരം മൂല്യങ്ങൾ ക്രമംപ്രകാരം 0.6, 0.9, True, 200 ആണ്.

    - ഇത് മറ്റൊരു dictionary test_json സൃഷ്ടിക്കുന്നു, അതിന് "input_data"യും "params"ഉം എന്ന രണ്ട് കീകൾ ഉണ്ട്. "input_data"യുടെ മൂല്യം മറ്റൊരു dictionary ആണ്, അതിന് "input_string"യും "parameters"ഉം എന്ന കീകൾ ഉണ്ട്. "input_string"യുടെ മൂല്യം test_df DataFrame-ൽ നിന്നുള്ള ആദ്യ സന്ദേശം അടങ്ങിയ ഒരു ലിസ്റ്റാണ്. "parameters"യുടെ മൂല്യം മുൻപ് സൃഷ്ടിച്ച parameters എന്ന ഡിക്ഷണറിയാണ്. "params"യുടെ മൂല്യം ശൂന്യമായ ഒരു ഡിക്ഷണറിയാണ്.

    - ഇത് sample_score.json എന്ന പേരിൽ ഒരു ഫയൽ തുറക്കുന്നു

    ```python
    # JSON ഡാറ്റയുമായി പ്രവർത്തിക്കാൻ ഫംഗ്ഷനുകൾ നൽകുന്ന json മോഡ്യൂൾ ഇമ്പോർട്ട് ചെയ്യുക
    import json
    
    # യന്ത്ര പഠന മോഡലിന്റെ പാരാമീറ്ററുകളെ പ്രതിനിധീകരിക്കുന്ന കീകളും മൂല്യങ്ങളും ഉള്ള `parameters` എന്ന ഡിക്ഷനറി സൃഷ്ടിക്കുക
    # കീകൾ "temperature", "top_p", "do_sample", "max_new_tokens" എന്നിവയാണ്, അവയുടെ അനുയോജ്യമായ മൂല്യങ്ങൾ യഥാക്രമം 0.6, 0.9, True, 200 ആണ്
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # "input_data" എന്നതും "params" എന്നതും എന്ന രണ്ട് കീകളുള്ള മറ്റൊരു ഡിക്ഷനറി `test_json` സൃഷ്ടിക്കുക
    # "input_data" എന്നതിന്റെ മൂല്യം "input_string" এবং "parameters" എന്ന കീകളുള്ള മറ്റൊരു ഡിക്ഷനറിയാണ്
    # "input_string" എന്നതിന്റെ മൂല്യം `test_df` ഡാറ്റാ ഫ്രെയിമിലെ ആദ്യ സന്ദേശം അടങ്ങിയിരിക്കുന്ന ഒരു ലിസ്റ്റാണ്
    # "parameters" എന്നതിന്റെ മൂല്യം മുമ്പ് സൃഷ്ടിച്ച `parameters` ഡിക്ഷനറിയാണ്
    # "params" എന്നതിന്റെ മൂല്യം ശൂന്യമായ ഒരു ഡിക്ഷനറിയാണ്
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` ഡയറക്ടറിയിലുള്ള `sample_score.json` എന്ന ഫയൽ എഴുത്ത് മോഡിൽ തുറക്കുക
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` ഫംഗ്ഷൻ ഉപയോഗിച്ച് `test_json` ഡിക്ഷനറി ഫയലിലേക്ക് JSON ഫോർമാറ്റിൽ എഴുതുക
        json.dump(test_json, f)
    ```

### എൻഡ്‌പോയിന്റ് വിളിക്കൽ

1. ഈ Python സ്ക്രിപ്റ്റ് JSON ഫയൽ സ്കോർ ചെയ്യുന്നതിനായി Azure Machine Learning-യിലെ ഒരു ഓൺലൈൻ എൻഡ്‌പോയിന്റിനെ വിളിക്കുന്നു. ഇതാ ഇത് ചെയ്യുന്നതിന്റെ വിശദീകരണം:

    - ഇത് workspace_ml_client object-ന്റെ online_endpoints പ്രോപ്പർട്ടിയുടെ invoke മെതഡ് വിളിക്കുന്നു. ഈ മെതഡ് ഒരു ഓൺലൈൻ എൻഡ്‌പോയിന്റിലേക്ക് ഒരു അഭ്യർഥന അയച്ച് പ്രതികരണം നേടാൻ ഉപയോഗിക്കുന്നു.

    - ഇത് endpoint_name ಮತ್ತು deployment_name ആർഗ്യൂമെന്റുകൾ ഉപയോഗിച്ച് എൻഡ്‌പോയിന്റിന്റെ പേര് കൂടാതെ ഡിപ്ലോയ്മെന്റും വ്യക്തമാക്കുന്നു. ഈ കാര്യത്തിൽ എൻഡ്‌പോയിന്റ് പേര് online_endpoint_name എന്ന വേരിയബിളിൽ സൂക്ഷിച്ചിരിക്കുന്നു, ഡിപ്ലോയ്മെന്റ് പേര് "demo" ആണ്.

    - ഇത് request_file ആർഗ്യുമെന്റിലൂടെ സ്കോർ ചെയ്യേണ്ട JSON ഫയലിന്റെ പാത വ്യക്തമാക്കുന്നു. ഈ കേസിൽ ഫയൽ ./ultrachat_200k_dataset/sample_score.json ആണ്.

    - ഇത് എൻഡ്‌പോയിന്റിൽ നിന്നുള്ള പ്രതികരണം response എന്ന വേരിയബിളിൽ സൂക്ഷിക്കുന്നു.

    - ഇത് raw response പ്രിന്റ് ചെയ്യുന്നു.

1. സംക്ഷേപത്തിൽ, ഈ സ്ക്രിപ്റ്റ് JSON ഫയൽ സ്കോർ ചെയ്യാൻ Azure Machine Learning-ലെ ഒരു ഓൺലൈൻ എൻഡ്‌പോയിന്റിനെ വിളിക്കുന്നു һәм response അച്ചടിക്കുന്നു.

    ```python
    # Azure Machine Learning-ൽ ഉള്ള ഓൺലൈൻ എൻഡ്പോയിന്റ് വിളിച്ച് `sample_score.json` ഫയൽ സ്‌കോർ ചെയ്യുക
    # `workspace_ml_client` ഒബ്ജക്റ്റിന്റെ `online_endpoints` പ്രോപ്പർടിയിലെ `invoke` മെത്തഡ് ഒരു ഓൺലൈൻ എൻഡ്പോയിന്റിന് അഭ്യർത്ഥന അയയ്ക്കാനും പ്രതികരണം ലഭിക്കാനുമാണ് ഉപയോഗിക്കുന്നത്
    # `endpoint_name` ആർഗുമെന്റ് എൻഡ്പോയിന്റിന്റെ പേര് സൂചിപ്പിക്കുന്നു, അത് `online_endpoint_name` വേരിയബിളിൽ സംഭരിച്ചിരിക്കുന്നു
    # `deployment_name` ആർഗുമെന്റ് ഡിപ്പ്ലോയ്മെന്റിന്റെ പേര് സൂചിപ്പിക്കുന്നു, അത് "demo" ആണ്
    # `request_file` ആർഗുമെന്റ് സ്‌കോർ ചെയ്യാനുള്ള JSON ഫയലിന്റെ പാത സൂചിപ്പിക്കുന്നു, അത് `./ultrachat_200k_dataset/sample_score.json` ആണ്
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # എൻഡ്പോയിന്റിൽ നിന്നുള്ള rå (raw) പ്രതികരണം പ്രിന്റ് ചെയ്യുക
    print("raw response: \n", response, "\n")
    ```

## 9. ഓൺലൈൻ എൻഡ്‌പോയിന്റ് നീക്കം ചെയ്യുക

1. ഓൺലൈൻ എൻഡ്‌പോയിന്റ് ഇല്ലാതാക്കുന്നത് മറക്കരുത്, അല്ലെങ്കിൽ എൻഡ്‌പോയിന്റ് ഉപയോഗിക്കുന്ന കംപ്യൂട്ടിന്റെ ബില്ലിംഗ് മീറ്റർ ഓടിക്കൂടി നില്ക്കും. ഈ Python കോഡ് ലൈൻ Azure Machine Learning-ിലെ ഒരു ഓൺലൈൻ എൻഡ്‌പോയിന്റ് നീക്കുകയാണ്. ഇതാ ഇത് ചെയ്യുന്നതിന്റെ വിശദീകരണം:

    - ഇത് workspace_ml_client object-ന്റെ online_endpoints പ്രോപ്പർട്ടിയുടെ begin_delete മെതഡ് വിളിക്കുന്നു. ഈ മെതഡ് ഒരു ഓൺലൈൻ എൻഡ്‌പോയിന്റിന്റെ നീക്കം ആരംഭിക്കാൻ ഉപയോഗിക്കുന്നു.

    - ഇത് name ആർഗ്യുമെന്റ് ഉപയോഗിച്ച് നീക്കേണ്ട എൻഡ്‌പോയിന്റിന്റെ പേര് വ്യക്തമാക്കുന്നു. ഈ കേസിൽ എൻഡ്‌പോയിന്റിന്റെ പേര് online_endpoint_name എന്ന വേരിയബിളിൽ സൂക്ഷിച്ചിരിക്കുന്നു.

    - ഇത് wait മെതഡ് വിളിച്ച് നീക്ക പ്രവർത്തി പൂർത്തിയാവുന്നതുവരെ കാത്തിരിക്കാൻ ഉപയോഗിക്കുന്നു. ഇത് ഒരു blocking ഓപ്പറേഷനാണ്, അതായത് നീക്കം പൂർത്തിയായെത്തുംവരെ സ്ക്രിപ്റ്റ് തുടരാൻ അനുവദിക്കാത്തതായിരിക്കും.

    - സംക്ഷേപത്തിൽ, ഈ കോഡ് ലൈൻ Azure Machine Learning-ൽ ഒരു ഓൺലൈൻ എൻഡ്‌പോയിന്റിന്റെ നീക്കം ആരംഭിക്കുകയും ആ പ്രവർത്തി പൂർത്തിയാവുന്നതുവരെ കാത്തിരിക്കുകയും ചെയ്യുന്നു.

    ```python
    # Azure Machine Learning-ൽ ഓൺലൈൻ എൻഡ്പോയിന്റ് ഇല്ലാതാക്കുക
    # workspace_ml_client ഒബ്ജക്റ്റിന്റെ `online_endpoints` പ്രോപ്പർട്ടിയിലെ `begin_delete` മെതഡ് ഓൺലൈൻ എൻഡ്പോയിന്റ് ഇല്ലാതാക്കൽ ആരംഭിക്കാൻ ഉപയോഗിക്കുന്നു
    # `name` ആർഗുമെന്റ് ഇല്ലാതാക്കേണ്ട എൻഡ്പോയിന്റിന്റെ പേര് നിർണയിക്കുന്നു, അത് `online_endpoint_name` വേരിയബിളിൽ സൂക്ഷിച്ചിരിക്കുന്നു
    # `wait` മെതഡ് ഡിലീഷൻ ഓപ്പറേഷൻ പൂർത്തിയാകുന്നത് വരെ കാത്തിരിക്കാനായി വിളിക്കപ്പെടുന്നു. ഇത് ഒരു ബ്ലോക്കിംഗ് ഓപ്പറേഷൻ ആണ്, അതായത് ഡിലീഷൻ പൂർത്തിയാകുന്നത് വരെ സ്‌ക്രിപ്റ്റ് മുന്നോട്ട് തുടരുന്നത് ഇത് തടയും
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിംർ:
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷാ സേവനായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നാം കൃത്യതയ്ക്ക് പരിശ്രമിച്ചിരുന്നുവെങ്കിലും ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിശകുകളും അപൂര്‍ണ്ണതകളും ഉണ്ടായിരിക്കാവുന്നതാണ് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ ഡോക്യുമെന്റ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗ_Resultantly ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും വ്യാഖ്യാന பിശകുകൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->