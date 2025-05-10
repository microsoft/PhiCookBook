<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T21:28:48+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "sw"
}
-->
## Jinsi ya kutumia vipengele vya chat-completion kutoka Azure ML system registry kufanyia mafunzo mfano

Katika mfano huu tutafanya mafunzo ya kuongeza usahihi (fine tuning) wa mfano wa Phi-3-mini-4k-instruct ili kukamilisha mazungumzo kati ya watu 2 tukitumia dataset ya ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.sw.png)

Mfano huu utaonyesha jinsi ya kufanya mafunzo ya kuongeza usahihi kwa kutumia Azure ML SDK na Python kisha kutuma mfano ulioboreshwa kwenye endpoint ya mtandaoni kwa ajili ya utambuzi wa wakati halisi.

### Data ya Mafunzo

Tutatumia dataset ya ultrachat_200k. Hii ni toleo lililosafishwa sana la dataset ya UltraChat na ilitumika kufundisha Zephyr-7B-β, mfano wa mazungumzo wa hali ya juu wa 7b.

### Mfano

Tutatumia mfano wa Phi-3-mini-4k-instruct kuonyesha jinsi mtumiaji anaweza kufanyia mafunzo mfano kwa kazi ya chat-completion. Ikiwa umefungua notebook hii kutoka kwenye kadi ya mfano maalum, kumbuka kubadilisha jina la mfano husika.

### Kazi

- Chagua mfano wa kufanyia mafunzo.
- Chagua na chunguza data ya mafunzo.
- Sanidi kazi ya mafunzo ya kuongeza usahihi.
- Endesha kazi ya mafunzo ya kuongeza usahihi.
- Kagua takwimu za mafunzo na tathmini.
- Sajili mfano ulioboreshwa.
- Tuma mfano ulioboreshwa kwa utambuzi wa wakati halisi.
- Safisha rasilimali.

## 1. Andaa mahitaji ya awali

- Sakinisha utegemezi
- Ungana na AzureML Workspace. Jifunze zaidi kuhusu kusanidi uthibitishaji wa SDK. Badilisha <WORKSPACE_NAME>, <RESOURCE_GROUP> na <SUBSCRIPTION_ID> hapo chini.
- Ungana na azureml system registry
- Weka jina la jaribio (experiment) kama hiari
- Angalia au tengeneza compute.

> [!NOTE]
> Mahitaji ni node moja ya GPU inaweza kuwa na kadi nyingi za GPU. Kwa mfano, kwenye node moja ya Standard_NC24rs_v3 kuna GPUs 4 za NVIDIA V100 wakati kwenye Standard_NC12s_v3 kuna GPUs 2 za NVIDIA V100. Rejelea nyaraka kwa taarifa hii. Idadi ya kadi za GPU kwa node imewekwa katika param gpus_per_node hapo chini. Kuweka thamani hii kwa usahihi kutahakikisha matumizi ya GPUs zote kwenye node. SKUs za GPU compute zinazopendekezwa zinaweza kupatikana hapa na hapa.

### Maktaba za Python

Sakinisha utegemezi kwa kuendesha seli ifuatayo. Hii si hatua ya hiari ikiwa unafanya kazi katika mazingira mapya.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Kuingiliana na Azure ML

1. Script hii ya Python hutumika kuingiliana na huduma ya Azure Machine Learning (Azure ML). Hapa ni muhtasari wa inavyofanya:

    - Inaingiza moduli muhimu kutoka azure.ai.ml, azure.identity, na azure.ai.ml.entities. Pia inaingiza moduli ya time.

    - Inajaribu kuthibitisha kwa kutumia DefaultAzureCredential(), ambayo hutoa njia rahisi ya uthibitishaji kwa kuanza haraka kuendeleza programu zinazotumia Azure cloud. Ikiwa hii itashindwa, inarudi kwenye InteractiveBrowserCredential(), ambayo hutoa dirisha la kuingia kwa mkato.

    - Kisha inajaribu kuunda mfano wa MLClient kwa kutumia njia ya from_config, inayosoma usanidi kutoka kwa faili ya chaguo-msingi (config.json). Ikiwa hii itashindwa, inaunda MLClient kwa kutoa subscription_id, resource_group_name, na workspace_name kwa mkono.

    - Inaunda mfano mwingine wa MLClient, kwa sasa kwa registry ya Azure ML inayoitwa "azureml". Registry hii ndio mahali ambapo mifano, njia za mafunzo ya kuongeza usahihi, na mazingira huhifadhiwa.

    - Inaweka jina la jaribio (experiment_name) kuwa "chat_completion_Phi-3-mini-4k-instruct".

    - Inazalisha alama ya kipekee ya wakati kwa kubadilisha wakati wa sasa (kwa sekunde tangu epoch, kama nambari ya desimali) kuwa nambari kamili kisha kuwa string. Alama hii inaweza kutumika kuunda majina na matoleo ya kipekee.

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

## 2. Chagua mfano wa msingi wa kufanyia mafunzo

1. Phi-3-mini-4k-instruct ni mfano mwepesi wa parameters 3.8B, wa kisasa wa wazi uliojengwa kwa kutumia datasets zilizotumika kwa Phi-2. Mfano huu ni sehemu ya familia ya modeli za Phi-3, na toleo la Mini linakuja katika aina mbili 4K na 128K ambazo ni urefu wa muktadha (kwa tokens) unaoweza kuhimili. Tunahitaji kufanyia mfano mafunzo maalum kwa ajili ya matumizi yetu. Unaweza kuvinjari mifano hii katika Katalogi ya Modeli katika AzureML Studio, ukichuja kwa kazi ya chat-completion. Katika mfano huu, tunatumia mfano wa Phi-3-mini-4k-instruct. Ikiwa umefungua notebook hii kwa mfano tofauti, badilisha jina la mfano na toleo ipasavyo.

    > [!NOTE]
    > sifa ya model id ya mfano. Hii itapitishwa kama ingizo kwa kazi ya mafunzo ya kuongeza usahihi. Inapatikana pia kama uwanja wa Asset ID katika ukurasa wa maelezo ya mfano katika AzureML Studio Model Catalog.

2. Script hii ya Python inaingiliana na huduma ya Azure Machine Learning (Azure ML). Hapa ni muhtasari wa inavyofanya:

    - Inaweka model_name kuwa "Phi-3-mini-4k-instruct".

    - Inatumia njia ya get ya mali ya models ya registry_ml_client kupata toleo la hivi karibuni la mfano wenye jina lililotajwa kutoka kwa registry ya Azure ML. Njia ya get inaitwa kwa hoja mbili: jina la mfano na lebo inayobainisha kwamba toleo la hivi karibuni linapaswa kupatikana.

    - Inachapisha ujumbe kwenye console unaoonyesha jina, toleo, na id ya mfano utakao tumika kwa mafunzo ya kuongeza usahihi. Njia ya format ya string hutumika kuingiza jina, toleo, na id ya mfano kwenye ujumbe. Jina, toleo, na id ya mfano hupatikana kama mali za foundation_model.

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

## 3. Tengeneza compute itakayotumika na kazi

Kazi ya finetune inafanya kazi TU na GPU compute. Ukubwa wa compute unategemea ukubwa wa mfano na mara nyingi huwa changamoto kuchagua compute sahihi kwa kazi. Katika seli hii, tunaelekeza mtumiaji jinsi ya kuchagua compute sahihi kwa kazi.

> [!NOTE]
> Compute zilizoorodheshwa hapa chini zinafanya kazi na usanidi ulioboreshwa zaidi. Mabadiliko yoyote kwenye usanidi yanaweza kusababisha kosa la Cuda Out Of Memory. Katika hali kama hizo, jaribu kuboresha compute kuwa kubwa zaidi.

> [!NOTE]
> Unapochagua compute_cluster_size hapa chini, hakikisha compute inapatikana katika resource group yako. Ikiwa compute fulani haipatikani unaweza kuomba ruhusa ya kupata rasilimali za compute.

### Kukagua Mfano kwa Msaada wa Mafunzo ya Kuongeza Usahihi

1. Script hii ya Python inaingiliana na mfano wa Azure Machine Learning (Azure ML). Hapa ni muhtasari wa inavyofanya:

    - Inaingiza moduli ya ast, inayotoa kazi za kushughulikia miti ya sarufi ya Python.

    - Inakagua kama foundation_model (ambayo ni mfano katika Azure ML) ina tag iitwayo finetune_compute_allow_list. Tags katika Azure ML ni jozi za key-value unazoweza kuunda na kutumia kuchuja na kupanga mifano.

    - Ikiwa tag ya finetune_compute_allow_list ipo, inatumia ast.literal_eval kwa usalama kuchambua thamani ya tag (kama string) kuwa orodha ya Python. Orodha hii inahifadhiwa katika computes_allow_list. Kisha inachapisha ujumbe unaoonyesha compute inapaswa kuundwa kutoka kwenye orodha hiyo.

    - Ikiwa tag ya finetune_compute_allow_list haipo, inaweka computes_allow_list kuwa None na inachapisha ujumbe unaoonyesha tag hiyo haipo kwenye tags za mfano.

    - Kwa kifupi, script hii inakagua tag maalum katika metadata ya mfano, inageuza thamani ya tag kuwa orodha ikiwa ipo, na kutoa mrejesho kwa mtumiaji.

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

### Kukagua Compute Instance

1. Script hii ya Python inaingiliana na huduma ya Azure Machine Learning (Azure ML) na kufanya ukaguzi kadhaa kwenye compute instance. Hapa ni muhtasari wa inavyofanya:

    - Inajaribu kupata compute instance yenye jina lililo kwenye compute_cluster kutoka Azure ML workspace. Ikiwa hali ya upangaji wa compute instance ni "failed", inarudisha ValueError.

    - Inakagua kama computes_allow_list si None. Ikiwa siyo, hubadilisha ukubwa wa compute zote kwenye orodha kuwa herufi ndogo na kuangalia kama ukubwa wa compute instance ya sasa upo kwenye orodha. Ikiwa haupo, inarudisha ValueError.

    - Ikiwa computes_allow_list ni None, inakagua kama ukubwa wa compute instance upo kwenye orodha ya ukubwa wa GPU VM zisizotumiwa. Ikiwa upo, inarudisha ValueError.

    - Inapata orodha ya ukubwa wote wa compute zinazopatikana kwenye workspace. Kisha inazizunguka orodha hii, na kwa kila ukubwa wa compute, inakagua kama jina lake linafanana na ukubwa wa compute instance ya sasa. Ikiwa linafanana, inapata idadi ya GPUs kwa ukubwa huo wa compute na kuweka gpu_count_found kuwa True.

    - Ikiwa gpu_count_found ni True, inachapisha idadi ya GPUs kwenye compute instance. Ikiwa ni False, inarudisha ValueError.

    - Kwa kifupi, script hii inafanya ukaguzi kadhaa kwenye compute instance katika Azure ML workspace, ikijumuisha ukaguzi wa hali ya upangaji, ukubwa dhidi ya orodha ya kuruhusu au kukanusha, na idadi ya GPUs iliyo nayo.

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

## 4. Chagua dataset kwa ajili ya mafunzo ya kuongeza usahihi ya mfano

1. Tunatumia dataset ya ultrachat_200k. Dataset ina sehemu nne, zinazofaa kwa Supervised fine-tuning (sft).
Generation ranking (gen). Idadi ya mifano kwa kila sehemu inaonyeshwa kama ifuatavyo:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Seliseli kadhaa zinazofuata zinaonyesha maandalizi ya msingi ya data kwa ajili ya mafunzo ya kuongeza usahihi:

### Onyesha baadhi ya mistari ya data

Tunataka sampuli hii ifanye kazi kwa haraka, hivyo hifadhi faili za train_sft, test_sft zenye 5% ya mistari iliyosafishwa tayari. Hii inamaanisha mfano ulioboreshwa utakuwa na usahihi mdogo, kwa hivyo haupaswi kutumika kwa matumizi halisi.
download-dataset.py hutumika kupakua dataset ya ultrachat_200k na kuibadilisha kuwa muundo unaoweza kutumiwa na sehemu ya pipeline ya mafunzo ya kuongeza usahihi. Pia kwa kuwa dataset ni kubwa, hapa tunakuwa na sehemu tu ya dataset.

1. Kuendesha script ifuatayo kunapakua tu 5% ya data. Hii inaweza kuongezwa kwa kubadilisha parameter ya dataset_split_pc hadi asilimia inayotaka.

    > [!NOTE]
    > Baadhi ya mifano ya lugha ina misimbo tofauti ya lugha na kwa hivyo majina ya safu kwenye dataset yanapaswa kuendana na hayo.

1. Hapa kuna mfano wa jinsi data inavyopaswa kuonekana
Dataset ya chat-completion imehifadhiwa kwa muundo wa parquet na kila kipengele kinatumia skema ifuatayo:

    - Huu ni hati ya JSON (JavaScript Object Notation), ambayo ni muundo maarufu wa kubadilishana data. Si msimbo unaotekelezwa, bali ni njia ya kuhifadhi na kusafirisha data. Hapa ni muhtasari wa muundo wake:

    - "prompt": Hii ni ufunguo unaoshikilia thamani ya string inayowakilisha kazi au swali lililotolewa kwa msaidizi wa AI.

    - "messages": Huu ni safu ya vitu. Kila kitu kinawakilisha ujumbe katika mazungumzo kati ya mtumiaji na msaidizi wa AI. Kila kitu cha ujumbe kina funguo mbili:

    - "content": Funguo hii ina thamani ya string inayowakilisha maudhui ya ujumbe.
    - "role": Funguo hii ina thamani ya string inayowakilisha nafasi ya mtu aliyepeleka ujumbe. Inaweza kuwa "user" au "assistant".
    - "prompt_id": Funguo hii ina thamani ya string inayowakilisha kitambulisho cha kipekee cha prompt.

1. Katika hati hii maalum ya JSON, mazungumzo yanaonyeshwa ambapo mtumiaji anaomba msaidizi wa AI kuunda mhusika mkuu wa hadithi ya dystopian. Msaidizi anajibu, kisha mtumiaji anaomba maelezo zaidi. Msaidizi anakubali kutoa maelezo zaidi. Mazungumzo yote yanaambatana na prompt id maalum.

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

### Pakua Data

1. Script hii ya Python hutumika kupakua dataset kwa kutumia script ya msaada iitwayo download-dataset.py. Hapa ni muhtasari wa inavyofanya:

    - Inaingiza moduli ya os, inayotoa njia ya kutumia vipengele vinavyotegemea mfumo wa uendeshaji.

    - Inatumia os.system kuendesha script ya download-dataset.py kwenye shell na hoja maalum za mstari wa amri. Hoja zinaelezea dataset ya kupakua (HuggingFaceH4/ultrachat_200k), saraka ya kuipakulia (ultrachat_200k_dataset), na asilimia ya dataset kugawanywa (5). os.system inarudisha hali ya kutoka kwa amri iliyotekelezwa; hali hii huhifadhiwa katika exit_status.

    - Inakagua kama exit_status si 0. Katika mifumo ya uendeshaji kama Unix, hali ya kutoka 0 kawaida inaashiria amri imefanikiwa, vinginevyo inaashiria kosa. Ikiwa exit_status si 0, inarudisha Exception yenye ujumbe unaoonyesha kulikuwa na kosa la kupakua dataset.

    - Kwa muhtasari, script hii inaendesha amri ya kupakua dataset kwa kutumia script ya msaada, na inarudisha kosa ikiwa amri itashindwa.

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

### Kupakia Data katika DataFrame

1. Script hii ya Python inapakia faili ya JSON Lines katika DataFrame ya pandas na kuonyesha mistari 5 ya kwanza. Hapa ni muhtasari wa inavyofanya:

    - Inaingiza maktaba ya pandas, ambayo ni maktaba yenye nguvu ya usindikaji na uchambuzi wa data.

    - Inaweka upana wa juu wa safu kwa chaguo za pandas kuonyesha data bila kukata maandishi.

    - Inatumia pd.read_json kupakia faili la train_sft.jsonl kutoka saraka ya ultrachat_200k_dataset kuwa DataFrame. Hoja lines=True inaonyesha faili ni katika muundo wa JSON Lines, ambapo kila mstari ni kitu tofauti cha JSON.

    - Inatumia njia ya head kuonyesha mistari 5 ya kwanza ya DataFrame. Ikiwa DataFrame ina chini ya mistari 5, itaonyesha yote.

    - Kwa muhtasari, script hii inapakia faili ya JSON Lines katika DataFrame na kuonyesha mistari 5 ya kwanza na maandishi kamili ya safu.

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

## 5. Tuma kazi ya mafunzo ya kuongeza usahihi ukitumia mfano na data kama ingizo

Tengeneza kazi inayotumia pipeline component ya chat-completion. Jifunze zaidi kuhusu vigezo vyote vinavyoungwa mkono kwa mafunzo ya kuongeza usahihi.

### Tambua vigezo vya finetune

1. Vigezo vya finetune vinaweza kugawanywa katika makundi 2 - vigezo vya mafunzo, vigezo vya uboreshaji

1. Vigezo vya mafunzo vinaeleza vipengele vya mafunzo kama -

    - Optimizer, scheduler ya kutumia
    - Kipimo cha kuboresha finetune
    - Idadi ya hatua za mafunzo na ukubwa wa batch na kadhalika
    - Vigezo vya uboreshaji husaidia kuboresha matumizi ya kumbukumbu ya GPU na kutumia rasilimali za compute kwa ufanisi.

1. Hapa chini ni baadhi ya vigezo vinavyojumuishwa katika kundi hili. Vigezo vya uboreshaji hutofautiana kwa kila mfano na huambatanishwa na mfano kushughulikia tofauti hizi.

    - Washa deepspeed na LoRA
    - Washa mafunzo ya mchanganyiko wa usahihi (mixed precision)
    - Washa mafunzo ya nodi nyingi

> [!NOTE]
> Supervised finetuning inaweza kusababisha kupoteza muafaka au kusahau kabisa (catastrophic forgetting). Tunapendekeza kuangalia tatizo hili na kuendesha awamu ya muafaka baada ya kufanyia mafunzo.

### Vigezo vya Fine Tuning

1. Script hii ya Python inaweka vigezo vya mafunzo ya kuongeza usahihi ya mfano wa machine learning. Hapa ni muhtasari wa inavyofanya:

    - Inaweka vigezo vya msingi vya mafunzo kama idadi ya vipindi vya mafunzo (epochs), ukubwa wa batch kwa mafunzo na tathmini, kiwango cha kujifunza (learning rate), na aina ya ratiba ya kiwango cha kujifunza.

    - Ina
training pipeline kulingana na vigezo mbalimbali, kisha kuchapisha jina hili la onyesho. ```python
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
    ``` ### Kusanidi Pipeline Hii script ya Python inafafanua na kusanidi pipeline ya mashine ya kujifunza kwa kutumia Azure Machine Learning SDK. Hapa kuna muhtasari wa inavyofanya: 1. Inaingiza moduli muhimu kutoka Azure AI ML SDK. 1. Inapata sehemu ya pipeline iitwayo "chat_completion_pipeline" kutoka kwenye rejista. 1. Inafafanua kazi ya pipeline kwa kutumia `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, ambayo ina maana pipeline itasimama ikiwa hatua yoyote itashindwa. 1. Kwa muhtasari, script hii inafafanua na kusanidi pipeline ya mashine ya kujifunza kwa ajili ya kazi ya chat completion kwa kutumia Azure Machine Learning SDK. ```python
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
    ``` ### Kuwasilisha Kazi 1. Hii script ya Python inawasilisha kazi ya pipeline ya mashine ya kujifunza kwa Azure Machine Learning workspace na kusubiri kazi hiyo kukamilika. Hapa kuna muhtasari wa inavyofanya: - Inaita njia ya create_or_update ya kitu cha jobs katika workspace_ml_client kuwasilisha kazi ya pipeline. Pipeline inayotekelezwa imeainishwa na pipeline_object, na jaribio ambalo kazi inafanyika chini yake limeainishwa na experiment_name. - Kisha inaita njia ya stream ya kitu cha jobs katika workspace_ml_client kusubiri kazi ya pipeline ikamilike. Kazi inayosubiriwa imeainishwa na sifa ya name ya pipeline_job. - Kwa muhtasari, script hii inawasilisha kazi ya pipeline ya mashine ya kujifunza kwa Azure Machine Learning workspace, kisha inasubiri kazi hiyo ikamilike. ```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ``` ## 6. Sajili model iliyoboreshwa na workspace Tutasajili model kutoka kwa matokeo ya kazi ya fine tuning. Hii itafuatilia uhusiano kati ya model iliyoboreshwa na kazi ya fine tuning. Kazi ya fine tuning, zaidi ya hayo, inafuatilia uhusiano na model ya msingi, data na msimbo wa mafunzo. ### Kusajili Model ya ML 1. Hii script ya Python inasajili model ya mashine ya kujifunza ambayo ilifundishwa katika pipeline ya Azure Machine Learning. Hapa kuna muhtasari wa inavyofanya: - Inaingiza moduli muhimu kutoka Azure AI ML SDK. - Inakagua kama output ya trained_model inapatikana kutoka kwa kazi ya pipeline kwa kuita njia ya get ya kitu cha jobs katika workspace_ml_client na kufikia sifa yake ya outputs. - Inaunda njia ya model iliyofundishwa kwa kutengeneza mfuatano wa maandishi na jina la kazi ya pipeline na jina la output ("trained_model"). - Inafafanua jina la model iliyoboreshwa kwa kuongeza "-ultrachat-200k" kwenye jina la model asili na kubadilisha mikanda yoyote kuwa vibonye. - Inajiandaa kusajili model kwa kuunda kitu cha Model na vigezo mbalimbali, ikiwa ni pamoja na njia ya model, aina ya model (MLflow model), jina na toleo la model, na maelezo ya model. - Inasajili model kwa kuita njia ya create_or_update ya kitu cha models katika workspace_ml_client na Model kama hoja. - Inachapisha model iliyosajiliwa. 1. Kwa muhtasari, script hii inasajili model ya mashine ya kujifunza ambayo ilifundishwa katika pipeline ya Azure Machine Learning. ```python
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
    ``` ## 7. Weka model iliyoboreshwa kwenye endpoint ya mtandaoni Endpoint za mtandaoni hutoa API thabiti ya REST ambayo inaweza kutumika kuunganishwa na programu zinazohitaji kutumia model. ### Kusimamia Endpoint 1. Hii script ya Python inaunda endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning kwa model iliyosajiliwa. Hapa kuna muhtasari wa inavyofanya: - Inaingiza moduli muhimu kutoka Azure AI ML SDK. - Inafafanua jina la kipekee la endpoint ya mtandaoni kwa kuongeza alama ya wakati kwenye mfuatano "ultrachat-completion-". - Inajiandaa kuunda endpoint ya mtandaoni kwa kuunda kitu cha ManagedOnlineEndpoint na vigezo mbalimbali, ikiwa ni pamoja na jina la endpoint, maelezo ya endpoint, na hali ya uthibitishaji ("key"). - Inaunda endpoint ya mtandaoni kwa kuita njia ya begin_create_or_update ya workspace_ml_client na kitu cha ManagedOnlineEndpoint kama hoja. Kisha inasubiri operesheni ya uundaji kukamilika kwa kuita njia ya wait. 1. Kwa muhtasari, script hii inaunda endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning kwa model iliyosajiliwa. ```python
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
    ``` > [!NOTE]
> Unaweza kupata hapa orodha ya SKU zinazoungwa mkono kwa ajili ya uanzishaji - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Kuweka Model ya ML

1. Hii script ya Python inapeleka model iliyosajiliwa ya mashine ya kujifunza kwenye endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning. Hapa kuna muhtasari wa inavyofanya:

    - Inaingiza moduli ya ast, ambayo hutoa kazi za kushughulikia miti ya sarufi ya muundo wa Python.

    - Inaweka aina ya kifaa cha kuanzisha kuwa "Standard_NC6s_v3".

    - Inakagua kama tag ya inference_compute_allow_list ipo kwenye model ya msingi. Ikiwa ipo, hubadilisha thamani ya tag kutoka kwenye maandishi hadi orodha ya Python na kuiweka kwenye inference_computes_allow_list. Ikiwa haipo, inaweka inference_computes_allow_list kuwa None.

    - Inakagua kama aina ya kifaa kilichoainishwa kiko kwenye orodha ya kuruhusiwa. Ikiwa hakipo, inachapisha ujumbe ikimwomba mtumiaji kuchagua aina ya kifaa kutoka kwenye orodha ya kuruhusiwa.

    - Inajiandaa kuunda uanzishaji kwa kuunda kitu cha ManagedOnlineDeployment na vigezo mbalimbali, ikiwa ni pamoja na jina la uanzishaji, jina la endpoint, ID ya model, aina na idadi ya kifaa, mipangilio ya liveness probe, na mipangilio ya maombi.

    - Inaunda uanzishaji kwa kuita njia ya begin_create_or_update ya workspace_ml_client na kitu cha ManagedOnlineDeployment kama hoja. Kisha inasubiri operesheni ya uundaji kukamilika kwa kuita njia ya wait.

    - Inaweka trafiki ya endpoint kupeleka asilimia 100 ya trafiki kwa uanzishaji wa "demo".

    - Inasasisha endpoint kwa kuita njia ya begin_create_or_update ya workspace_ml_client na kitu cha endpoint kama hoja. Kisha inasubiri operesheni ya sasisho kukamilika kwa kuita njia ya result.

1. Kwa muhtasari, script hii inapeleka model iliyosajiliwa ya mashine ya kujifunza kwenye endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning.

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

## 8. Jaribu endpoint na data ya mfano

Tutachukua baadhi ya data za mfano kutoka kwenye dataset ya majaribio na kuziwasilisha kwa endpoint ya mtandaoni kwa ajili ya utabiri. Kisha tutaonyesha alama zilizopimwa pamoja na alama halisi.

### Kusoma matokeo

1. Hii script ya Python inasoma faili ya JSON Lines ndani ya pandas DataFrame, kuchukua sampuli ya bahati nasibu, na kuweka upya index. Hapa kuna muhtasari wa inavyofanya:

    - Inasoma faili ./ultrachat_200k_dataset/test_gen.jsonl ndani ya pandas DataFrame. Kazi ya read_json inatumiwa na hoja lines=True kwa sababu faili iko katika muundo wa JSON Lines, ambapo kila mstari ni kitu tofauti cha JSON.

    - Inachukua sampuli ya bahati nasibu ya mistari 1 kutoka DataFrame. Kazi ya sample inatumiwa na hoja n=1 kuonyesha idadi ya mistari ya bahati nasibu kuchaguliwa.

    - Inarejesha index ya DataFrame. Kazi ya reset_index inatumiwa na hoja drop=True kuondoa index ya awali na kuibadilisha na index mpya ya nambari za kawaida.

    - Inaonyesha mistari 2 ya kwanza ya DataFrame kwa kutumia kazi ya head na hoja 2. Hata hivyo, kwa kuwa DataFrame ina mstari mmoja tu baada ya sampuli, hii itaonyesha mstari huo mmoja tu.

1. Kwa muhtasari, script hii inasoma faili ya JSON Lines ndani ya pandas DataFrame, kuchukua sampuli ya bahati nasibu ya mstari 1, kuweka upya index, na kuonyesha mstari wa kwanza.

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

### Tengeneza Kitu cha JSON

1. Hii script ya Python inaunda kitu cha JSON kwa vigezo maalum na kuihifadhi kwenye faili. Hapa kuna muhtasari wa inavyofanya:

    - Inaingiza moduli ya json, ambayo hutoa kazi za kushughulikia data za JSON.

    - Inaunda kamusi parameters yenye funguo na thamani zinazowakilisha vigezo vya model ya mashine ya kujifunza. Funguo ni "temperature", "top_p", "do_sample", na "max_new_tokens", na thamani zao ni 0.6, 0.9, True, na 200 mtawalia.

    - Inaunda kamusi nyingine test_json yenye funguo mbili: "input_data" na "params". Thamani ya "input_data" ni kamusi nyingine yenye funguo "input_string" na "parameters". Thamani ya "input_string" ni orodha yenye ujumbe wa kwanza kutoka DataFrame ya test_df. Thamani ya "parameters" ni kamusi parameters iliyoundwa awali. Thamani ya "params" ni kamusi tupu.

    - Inafungua faili iitwayo sample_score.json

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

### Kupiga Endpoint

1. Hii script ya Python inapiga endpoint ya mtandaoni katika Azure Machine Learning ili kupima faili ya JSON. Hapa kuna muhtasari wa inavyofanya:

    - Inaita njia ya invoke ya mali ya online_endpoints ya kitu workspace_ml_client. Njia hii hutumiwa kutuma ombi kwa endpoint ya mtandaoni na kupata jibu.

    - Inaelezea jina la endpoint na uanzishaji kwa hoja za endpoint_name na deployment_name. Katika kesi hii, jina la endpoint limehifadhiwa katika variable online_endpoint_name na jina la uanzishaji ni "demo".

    - Inaelezea njia ya faili ya JSON itakayopimwa kwa hoja request_file. Katika kesi hii, faili ni ./ultrachat_200k_dataset/sample_score.json.

    - Inahifadhi jibu kutoka kwa endpoint katika variable response.

    - Inachapisha jibu halisi.

1. Kwa muhtasari, script hii inapiga endpoint ya mtandaoni katika Azure Machine Learning kupima faili ya JSON na kuchapisha jibu.

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

## 9. Futa endpoint ya mtandaoni

1. Usisahau kufuta endpoint ya mtandaoni, vinginevyo utaacha mita ya bili ikitumia kwa ajili ya kompyuta inayotumika na endpoint. Mstari huu wa msimbo wa Python unafuta endpoint ya mtandaoni katika Azure Machine Learning. Hapa kuna muhtasari wa inavyofanya:

    - Inaita njia ya begin_delete ya mali ya online_endpoints ya kitu workspace_ml_client. Njia hii hutumiwa kuanzisha kufuta endpoint ya mtandaoni.

    - Inaelezea jina la endpoint itakayofutwa kwa hoja ya name. Katika kesi hii, jina la endpoint limehifadhiwa katika variable online_endpoint_name.

    - Inaita njia ya wait kusubiri operesheni ya kufuta ikamilike. Hii ni operesheni ya kuzuia, ikimaanisha itazuia script kuendelea hadi kufutwa kumalizike.

    - Kwa muhtasari, mstari huu wa msimbo unaanza kufuta endpoint ya mtandaoni katika Azure Machine Learning na kusubiri operesheni ikamilike.

    ```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Kifunuo cha Majukumu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya binadamu inapendekezwa. Hatubebei lawama kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.