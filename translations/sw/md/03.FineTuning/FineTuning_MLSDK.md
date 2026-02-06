## Jinsi ya kutumia vipengele vya chat-completion kutoka kwa rejista ya mfumo wa Azure ML kufanyia marekebisho model

Katika mfano huu tutaendesha upya urekebishaji wa model ya Phi-3-mini-4k-instruct kumaliza mazungumzo kati ya watu 2 kwa kutumia dataset ya ultrachat_200k.

![MLFineTune](../../../../translated_images/sw/MLFineTune.928d4c6b3767dd35.webp)

Mfano huu utaonyesha jinsi ya kufanya upya urekebishaji kwa kutumia Azure ML SDK na Python kisha kupeleka model iliyorekebishwa kwenye endpoint mtandaoni kwa ajili ya utambuzi wa wakati halisi.

### Data ya mafunzo

Tutatumia dataset ya ultrachat_200k. Hii ni toleo lililosafishwa sana la dataset ya UltraChat na ilitumika kufundisha Zephyr-7B-β, modeli ya hali ya juu yenye ujazo wa 7b kwa mazungumzo.

### Modeli

Tutatumia model ya Phi-3-mini-4k-instruct kuonyesha jinsi mtumiaji anavyoweza kurekebisha model kwa kazi ya chat-completion. Kama umefungua daftari hili kutoka kwa kadi ya model maalum, kumbuka kubadilisha jina hilo la model.

### Majukumu

- Chagua model ya kufanya fine tune.
- Chagua na chunguza data za mafunzo.
- Sanidi kazi ya fine tuning.
- Endesha kazi ya fine tuning.
- Kagua takwimu za mafunzo na tathmini.
- Sajili model iliyorekebishwa.
- Telekeza model inayorekebishwa kwa utambuzi wa wakati halisi.
- Safisha rasilimali.

## 1. Weka mambo ya msingi

- Sakinisha utegemezi
- Ungana na AzureML Workspace. Jifunze zaidi kuhusu kuweka uthibitishaji wa SDK. Badilisha <WORKSPACE_NAME>, <RESOURCE_GROUP> na <SUBSCRIPTION_ID> hapa chini.
- Ungana na rejista ya mfumo ya azureml
- Weka jina la jaribio kama hiari
- Kagua au tengeneza compute.

> [!NOTE]
> Mahitaji ni node moja ya GPU inaweza kuwa na kadi nyingi za GPU. Kwa mfano, kwenye node moja ya Standard_NC24rs_v3 kuna GPU 4 za NVIDIA V100 wakati kwenye Standard_NC12s_v3, kuna GPU 2 za NVIDIA V100. Rejelea hati kwa taarifa hii. Idadi ya kadi za GPU kwa node imewekwa kwenye param gpus_per_node hapa chini. Kuweka thamani hii kwa usahihi kutahakikisha matumizi ya GPU zote kwenye node. SKUs zinazopendekezwa za compute za GPU zinaweza kupatikana hapa na hapa.

### Maktaba za Python

Sakinisha utegemezi kwa kuendesha seli hapa chini. Hii si hatua ya hiari ikiwa unaendesha katika mazingira mapya.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Kuingiliana na Azure ML

1. Hii script ya Python hutumiwa kuingiliana na huduma ya Azure Machine Learning (Azure ML). Hapa ni muhtasari wa inavyofanya:

    - Inaingiza moduli muhimu kutoka kwa packages za azure.ai.ml, azure.identity, na azure.ai.ml.entities. Pia inaingiza moduli ya time.

    - Inajaribu kuthibitisha kwa kutumia DefaultAzureCredential(), ambayo hutoa uzoefu rahisi wa uthibitishaji kwa kuanza haraka kuendeleza programu zinazofanya kazi katika Azure cloud. Ikiwa hii itashindwa, hutumia InteractiveBrowserCredential(), ambayo hutoa kiolesura cha kuingiza nywila kiutumiaji.

    - Kisha inajaribu kuunda mfano wa MLClient kwa kutumia njia ya from_config, inayosoma usanidi kutoka kwa faili ya kawaida ya config (config.json). Ikiwa hii itashindwa, huunda MLClient kwa kutoa subscription_id, resource_group_name, na workspace_name kwa mkono.

    - Inaunda mfano mwingine wa MLClient, mara hii kwa rejista ya Azure ML inayoitwa "azureml". Rejista hii ni mahali ambapo model, njia za fine-tuning, na mazingira yamehifadhiwa.

    - Inaweka jina la jaribio kuwa "chat_completion_Phi-3-mini-4k-instruct".

    - Inazalisha alama za wakati za kipekee kwa kubadilisha wakati wa sasa (kwa sekunde tangu epoch, kama nambari ya mviringo) kuwa nambari kamili kisha kuwa string. Alama hizi zinaweza kutumika kwa kuunda majina na toleo la kipekee.

    ```python
    # Ingiza moduli muhimu kutoka Azure ML na Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Ingiza moduli ya wakati
    
    # Jaribu kuaminisha kwa kutumia DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Ikiwa DefaultAzureCredential itashindwa, tumia InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Jaribu kuunda mfano wa MLClient kwa kutumia faili ya usanidi wa default
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Ikiwa hiyo itashindwa, unda mfano wa MLClient kwa kutoa maelezo kwa mikono
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Unda mfano mwingine wa MLClient kwa rejista ya Azure ML iitwacho "azureml"
    # Rejista hii ni mahali ambapo mifano, pipeline za fine-tuning, na mazingira hifadhiwa
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Weka jina la jaribio
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Tengeneza wakati wa kipekee unaoweza kutumika kwa majina na toleo ambalo linahitaji kuwa la kipekee
    timestamp = str(int(time.time()))
    ```

## 2. Chagua model ya msingi ya kufanya fine tune

1. Phi-3-mini-4k-instruct ni modeli ya njia 3.8B za vigezo, nyepesi, ya hali ya juu iliyojengwa juu ya datasets zilizotumika kwa Phi-2. Modeli ni sehemu ya familia ya modeli za Phi-3, na toleo la Mini linakuja kwa aina mbili 4K na 128K ambayo ni urefu wa muktadha (kwa tokens) inayoweza kuhimili, tunahitaji kurekebisha modeli kwa madhumuni maalum ili kuitumia. Unaweza kuvinjari modeli hizi katika Katalogi ya Modeli katika AzureML Studio, kwa kuchuja kwa kazi ya chat-completion. Katika mfano huu, tunatumia model ya Phi-3-mini-4k-instruct. Ikiwa umefungua daftari hili kwa modeli tofauti, badilisha jina la modeli na toleo ipasavyo.

> [!NOTE]
> sifa ya id ya modeli. Hii itapitishwa kama ingizo kwa kazi ya fine tuning. Hii pia inapatikana kama Sehemu ya Asset ID kwenye ukurasa wa maelezo ya modeli katika Katalogi ya Modeli ya AzureML Studio.

2. Hii script ya Python inaingiliana na huduma ya Azure Machine Learning (Azure ML). Hapa ni muhtasari wa inavyofanya:

    - Inaweka model_name kuwa "Phi-3-mini-4k-instruct".

    - Inatumia njia ya get ya mali ya models ya kielekezi registry_ml_client kupata toleo la hivi karibuni la modeli yenye jina lililotajwa kutoka kwenye rejista ya Azure ML. Njia ya get inaitwa na hoja mbili: jina la modeli na lebo inayosema toleo la hivi karibuni la modeli linapaswa kupatikana.

    - Inachapisha ujumbe kwenye console unaoonyesha jina, toleo, na id ya modeli itakayotumika kwa fine-tuning. Njia ya format ya string hutumika kuingiza jina, toleo, na id ya modeli ndani ya ujumbe. Jina, toleo, na id ya modeli zinapatikana kama sifa za kitu cha foundation_model.

    ```python
    # Weka jina la modeli
    model_name = "Phi-3-mini-4k-instruct"
    
    # Pata toleo la hivi karibuni la modeli kutoka kwa rejista ya Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Chapisha jina la modeli, toleo, na kitambulisho
    # Taarifa hii ni muhimu kwa kufuatilia na kutatua matatizo
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Tengeneza compute itakayotumika na kazi

Kazi ya finetune inafanya kazi TU na GPU compute. Ukubwa wa compute unategemea ukubwa wa modeli na mara nyingi ni changamoto kubaini compute sahihi kwa kazi. Katika seli hii, tunaongoza mtumiaji kuchagua compute sahihi kwa kazi.

> [!NOTE]
> Compute zilizoorodheshwa hapa chini zinafanya kazi kwa usanidi ulioboreshwa zaidi. Mabadiliko yoyote ya usanidi yanaweza kusababisha kosa la Cuda Out Of Memory. Katika hali hivyo, jaribu kuboresha compute kwa ukubwa mkubwa.

> [!NOTE]
> Wakati wa kuchagua compute_cluster_size hapa chini, hakikisha compute ipo kwenye resource group yako. Ikiwa compute maalum haipatikani unaweza kuomba kupata ruhusa ya kupata rasilimali za compute.

### Kukagua Model kwa Msaada wa Fine Tuning

1. Hii script ya Python inaingiliana na model ya Azure Machine Learning (Azure ML). Hapa ni muhtasari wa inavyofanya:

    - Inaingiza moduli ya ast, ambayo hutoa kazi za kushughulikia miti ya sarufi ya Python.

    - Inakagua kama kitu cha foundation_model (kinachoonyesha modeli katika Azure ML) kina tag inayoitwa finetune_compute_allow_list. Tag katika Azure ML ni jozi za key-value unazoweza kuunda na kutumia kuchuja na kupanga modeli.

    - Ikiwa tag ya finetune_compute_allow_list ipo, inatumia ast.literal_eval kwa usalama kubadilisha thamani ya tag (kama string) kuwa orodha ya Python. Orodha hii huwekwa katika variable computes_allow_list. Kisha inachapisha ujumbe unaosema compute inapaswa kutengenezwa kutoka orodha hiyo.

    - Ikiwa tag ya finetune_compute_allow_list haipo, inafanya computes_allow_list kuwa None na inachapisha ujumbe unaosema tag hiyo si sehemu ya tag za modeli.

    - Kwa muhtasari, script hii inakagua tag maalum katika metadata ya modeli, kubadilisha thamani ya tag kuwa orodha ikiwa ipo, na kutoa maoni kwa mtumiaji ipasavyo.

    ```python
    # Ingiza moduli ya ast, ambayo hutoa kazi za kusindika miti ya sarufi ya syntax ya abstract ya Python
    import ast
    
    # Angalia ikiwa lebo ya 'finetune_compute_allow_list' ipo kwenye lebo za mfano
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Ikiwa lebo iko, tumia ast.literal_eval kusoma kwa usalama thamani ya lebo (kamba) kuwa orodha ya Python
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # geuza kamba kuwa orodha ya python
        # Chapisha ujumbe unaoonyesha kwamba compute inapaswa kuundwa kutoka kwa orodha
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ikiwa lebo haipo, weka computes_allow_list kuwa None
        computes_allow_list = None
        # Chapisha ujumbe unaoonyesha kwamba lebo ya 'finetune_compute_allow_list' si sehemu ya lebo za mfano
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Kukagua Compute Instance

1. Hii script ya Python inaingiliana na huduma ya Azure Machine Learning (Azure ML) na kufanya ukaguzi kadhaa juu ya compute instance. Hapa ni muhtasari wa inavyofanya:

    - Inajaribu kupata compute instance yenye jina lililohifadhiwa katika compute_cluster kutoka kwa Azure ML workspace. Ikiwa hali ya utoaji wa compute instance ni "failed", inarudi kosa la ValueError.

    - Inakagua kama computes_allow_list si None. Ikiwa si None, inabadilisha ukubwa wote wa compute katika orodha kuwa herufi ndogo na kukagua kama ukubwa wa compute instance uliopo uko katika orodha. Ikiwa haupo, inarudi kosa la ValueError.

    - Ikiwa computes_allow_list ni None, inakagua kama ukubwa wa compute instance uko katika orodha ya ukubwa wa VM za GPU zisizoungwa mkono. Ikiwa iko, inarudi kosa la ValueError.

    - Inapata orodha ya ukubwa wote wa compute zinazopatikana katika workspace. Kisha inazunguka orodha hii, na kwa kila ukubwa wa compute, inakagua kama jina linazosikana na ukubwa wa compute instance iliyopo. Ikiwa ndivyo, inapata idadi ya GPUs kwa ukubwa huo wa compute na kuweka gpu_count_found kuwa True.

    - Ikiwa gpu_count_found ni True, inachapisha idadi ya GPUs katika compute instance. Ikiwa ni False, inarudi kosa la ValueError.

    - Kwa muhtasari, script hii inafanya ukaguzi kadhaa juu ya compute instance katika Azure ML workspace, ikiwa ni pamoja na ukaguzi wa hali ya utoaji, ukubwa dhidi ya orodha ya kuruhusu au kuruhusu, na idadi ya GPUs inayo.

    ```python
    # Chapisha ujumbe wa ubaguzi
    print(e)
    # Inua ValueError kama ukubwa wa kompyuta haupatikani kwenye eneo la kazi
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Pata kifaa cha kompyuta kutoka kwa eneo la kazi la Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Angalia kama hali ya utoaji ya kifaa cha kompyuta ni "imeshindwa"
    if compute.provisioning_state.lower() == "failed":
        # Inua ValueError ikiwa hali ya utoaji ni "imeshindwa"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Angalia kama orodha ya inaruhusiwa ya kompyuta haiko tupu
    if computes_allow_list is not None:
        # Badilisha ukubwa wote wa kompyuta katika orodha ya inaruhusiwa ya kompyuta kuwa herufi ndogo
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Angalia kama ukubwa wa kifaa cha kompyuta uko katika orodha ya inaruhusiwa ya kompyuta yenye herufi ndogo
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Inua ValueError ikiwa ukubwa wa kifaa cha kompyuta haupo katika orodha ya inaruhusiwa ya kompyuta yenye herufi ndogo
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Fafanua orodha ya ukubwa wa VM za GPU zisizochukuliwa
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Angalia kama ukubwa wa kifaa cha kompyuta uko katika orodha ya VM za GPU zisizochukuliwa
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Inua ValueError ikiwa ukubwa wa kifaa cha kompyuta uko katika orodha ya VM za GPU zisizochukuliwa
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Anzisha bendera ya kuangalia kama idadi ya GPU katika kifaa cha kompyuta imetambuliwa
    gpu_count_found = False
    # Pata orodha ya ukubwa wote wa kompyuta zinazopatikana katika eneo la kazi
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Pitisha juu ya orodha ya ukubwa wa kompyuta zinazopatikana
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Angalia kama jina la ukubwa wa kompyuta linakubaliana na ukubwa wa kifaa cha kompyuta
        if compute_sku.name.lower() == compute.size.lower():
            # Ikiwa linakubaliana, pata idadi ya GPU kwa ukubwa huo wa kompyuta na weka gpu_count_found kuwa Kweli
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Ikiwa gpu_count_found ni Kweli, chapisha idadi ya GPU katika kifaa cha kompyuta
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Ikiwa gpu_count_found ni Sawa, inua ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Chagua dataset kwa fine-tuning ya modeli

1. Tunatumia dataset ya ultrachat_200k. Dataset ina mgawanyo nne, unaofaa kwa Supervised fine-tuning (sft).
Kutawanya kizazi (gen). Idadi ya mifano kwa kila mgawanyo inaonyeshwa kama ifuatavyo:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Seli chache zifuatazo zinaonyesha maandalizi ya data ya msingi kwa fine tuning:

### Angalia baadhi ya mistari ya data

Tunataka sampuli hii ifanye kazi kwa haraka, hivyo hifadhi train_sft, test_sft faili zilizo na 5% ya mistari iliyokatwa tayari. Hii inamaanisha model iliyorekebishwa itakuwa na usahihi mdogo, kwa hiyo haipaswi kutumika katika matumizi halisi.
download-dataset.py hutumiwa kupakua dataset ya ultrachat_200k na kubadilisha dataset hiyo kuwa muundo unaoweza kutumiwa na sehemu ya fine tune pipeline. Pia kwa kuwa dataset ni kubwa, tunayo sehemu tu ya dataset hapa.

1. Kuendesha script ifuatayo hupakua tu 5% ya data. Hii inaweza kuongezwa kwa kubadilisha parameter dataset_split_pc hadi asilimia unayotaka.

> [!NOTE]
> Baadhi ya modeli za lugha zina codes tofauti za lugha na kwa hiyo majina ya safu katika dataset yanapaswa kuendana na hayo.

1. Huu ni mfano wa jinsi data inavyopaswa kuonekana
Dataset ya chat-completion imehifadhiwa katika muundo wa parquet kwa kila kipengele kinatumia skimu ifuatayo:

    - Huu ni hati ya JSON (JavaScript Object Notation), ambayo ni muundo maarufu wa kubadilishana data. Sio msimbo unaotekelezwa, bali ni njia ya kuhifadhi na kusafirisha data. Hapa ni muhtasari wa muundo wake:

    - "prompt": Hili ni ufunguo unaoshikilia thamani ya string inayowakilisha kazi au swali lililotolewa kwa msaidizi wa AI.

    - "messages": Hili ni ufunguo unaoshikilia safu ya vitu. Kila kitu kinawakilisha ujumbe katika mazungumzo kati ya mtumiaji na msaidizi wa AI. Kila kitu cha ujumbe kina vifunguo viwili:

    - "content": Hili ni ufunguo unaoshikilia thamani ya string inayowakilisha maudhui ya ujumbe.
    - "role": Hili ni ufunguo unaoshikilia thamani ya string inayowakilisha nafasi ya kiumbe aliyetuma ujumbe. Inaweza kuwa "user" au "assistant".
    - "prompt_id": Hili ni ufunguo unaoshikilia thamani ya string inayotambulisha kwa kipekee prompt.

1. Katika hati hii ya JSON, mazungumzo yanaonyeshwa ambapo mtumiaji anauliza msaidizi wa AI kuunda mhusika mkuu kwa hadithi ya dystopian. Msaidizi anajibu, na mtumiaji anaomba maelezo zaidi. Msaidizi anakubali kutoa maelezo zaidi. Mazungumzo yote yanaambatana na prompt id maalum.

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

1. Script hii ya Python hutumiwa kupakua dataset kwa kutumia script ya msaidizi inayoitwa download-dataset.py. Hapa ni muhtasari wa inavyofanya:

    - Inaingiza moduli ya os, ambayo hutoa njia rahisi ya kutumia vipengele vya mfumo wa uendeshaji.

    - Inatumia os.system kuendesha script ya download-dataset.py kwenye shell kwa hoja maalum za mstari wa amri. Hoja zinabainisha dataset ya kupakua (HuggingFaceH4/ultrachat_200k), saraka ya kupakulia (ultrachat_200k_dataset), na asilimia ya dataset kugawanywa (5). Kazi ya os.system inarejesha hali ya kutoka ya amri iliyotekelezwa; hali hii huhifadhiwa kwenye variable exit_status.

    - Inakagua kama exit_status si 0. Katika mifumo ya kazi kama Unix, hali ya kutoka 0 kawaida inaonyesha kuwa amri imetekelezwa kwa mafanikio, na nambari nyingine yoyote inaonyesha kosa. Ikiwa exit_status si 0, inatoa Exception yenye ujumbe wa kosa kuhusu tatizo la kupakua dataset.

    - Kwa muhtasari, script hii inaendesha amri ya kupakua dataset kwa kutumia script ya msaidizi, na kutoa kosa kama amri inashindwa.

    ```python
    # Ingiza moduli ya os, ambayo hutoa njia ya kutumia utendakazi unaotegemea mfumo wa uendeshaji
    import os
    
    # Tumia kazi ya os.system kuendesha script ya download-dataset.py katika shell kwa hoja maalum za mstari wa amri
    # Hoja hizi zinaonyesha dataset ya kupakua (HuggingFaceH4/ultrachat_200k), saraka ya kuipakulia (ultrachat_200k_dataset), na asilimia ya dataset ya kugawanya (5)
    # Kazi ya os.system hurudisha hali ya kutoka ya amri iliyoendeshwa; hali hii huhifadhiwa katika kigezo cha exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Angalia ikiwa exit_status si 0
    # Katika mifumo ya uendeshaji kama Unix, hali ya kutoka ya 0 mara nyingi inaonyesha kwamba amri imefaulu, wakati nambari nyingine yoyote inaonyesha hitilafu
    # Ikiwa exit_status si 0, elekeza Exception yenye ujumbe unaoonyesha kuwa kulikua na hitilafu katika kupakua dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Kupakia Data katika DataFrame

1. Script hii ya Python inapakua faili la JSON Lines ndani ya pandas DataFrame na kuonyesha mistari 5 ya kwanza. Hapa ni muhtasari wa inavyofanya:

    - Inaingiza maktaba ya pandas, ambayo ni maktaba yenye nguvu ya usindikaji na uchambuzi wa data.

    - Inaweka upana wa safu wa juu zaidi kwa chaguo la pandas kuonyesha kwa 0. Hii ina maana maandishi kamili ya kila safu yataonyeshwa bila kukatwa wakati DataFrame inachapishwa.
    - Inatumia kazi ya pd.read_json kupakia faili la train_sft.jsonl kutoka kwenye saraka ya ultrachat_200k_dataset ndani ya DataFrame. Hoja ya lines=True inaonyesha kwamba faili iko katika muundo wa JSON Lines, ambapo kila mstari ni kitu tofauti cha JSON.

    - Inatumia mbinu ya head kuonyesha mistari 5 ya kwanza ya DataFrame. Ikiwa DataFrame ina mistari chini ya 5, itaonyesha yote.

    - Kwa muhtasari, script hii inapakia faili la JSON Lines ndani ya DataFrame na kuonyesha mistari 5 ya kwanza na maandishi kamili ya safu.
    
    ```python
    # Ingiza maktaba ya pandas, ambayo ni maktaba yenye nguvu ya usindikaji na uchambuzi wa data
    import pandas as pd
    
    # Weka upana wa safu wa juu kabisa kwa chaguo za onyesho za pandas kuwa 0
    # Hii ina maana kwamba maandishi kamili ya kila safu yataonyeshwa bila kukatwa wakati DataFrame inachapishwa
    pd.set_option("display.max_colwidth", 0)
    
    # Tumia kazi ya pd.read_json kupakia faili la train_sft.jsonl kutoka saraka ya ultrachat_200k_dataset ndani ya DataFrame
    # Hoja lines=True inaonyesha kuwa faili iko katika muundo wa JSON Lines, ambapo kila mstari ni kitu tofauti cha JSON
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Tumia njia ya head kuonyesha mistari 5 ya kwanza ya DataFrame
    # Ikiwa DataFrame ina mistari chini ya 5, itaonyesha yote yote
    df.head()
    ```

## 5. Wasilisha kazi ya mafunzo ya ziada kwa kutumia model na data kama ingizo

Unda kazi inayotumia kipengele cha mchakato wa chat-completion. Jifunze zaidi kuhusu vigezo vyote vinavyounga mkono mafunzo ya ziada.

### Tambua vigezo vya finetune

1. Vigezo vya finetune vinaweza kugawanywa katika makundi 2 - vigezo vya mafunzo, vigezo vya uboreshaji

1. Vigezo vya mafunzo hufafanua vipengele vya mafunzo kama vile -

    - Optimizer, ratiba ya kutumia
    - Kipimo cha kuboresha finetune
    - Idadi ya hatua za mafunzo na ukubwa wa kundi na kadhalika
    - Vigezo vya uboreshaji husaidia katika kuboresha kumbukumbu ya GPU na kutumia rasilimali za kompyuta kwa ufanisi.

1. Hapa chini ni baadhi ya vigezo vinavyohusiana na kundi hili. Vigezo vya uboreshaji hutofautiana kwa kila modeli na vinatolewa pamoja na modeli kushughulikia tofauti hizi.

    - Washa deepspeed na LoRA
    - Washa mafunzo ya mchanganyiko wa usahihi
    - Washa mafunzo ya nodi nyingi

> [!NOTE]
> Mafunzo ya ziada yaliyoongozwa yanaweza kusababisha kupoteza kulingana au kusahau kwa mbaya sana (catastrophic forgetting). Tunapendekeza kukagua tatizo hili na kuendesha hatua ya kulinganisha baada ya kufanya finetune.

### Vigezo vya Fine Tuning

1. Script hii ya Python inatayarisha vigezo kwa ajili ya kufinya upya (fine-tuning) ya modeli ya mashine ya kujifunza. Hapa ni muhtasari wa kile inachofanya:

    - Inaweka vigezo chaguo-msingi vya mafunzo kama vile idadi ya vipindi vya mafunzo, ukubwa wa makundi kwa mafunzo na tathmini, kiwango cha kujifunza, na aina ya ratiba ya kiwango cha kujifunza.

    - Inaweka vigezo vya chaguo-msingi vya uboreshaji kama vile kama Layer-wise Relevance Propagation (LoRa) na DeepSpeed zitumike, na hatua ya DeepSpeed.

    - Inachanganya vigezo vya mafunzo na uboreshaji katika kamusi moja iitwayo finetune_parameters.

    - Inakagua ikiwa foundation_model ina vigezo vya chaguo-msingi maalum vya modeli. Ikiwa ipo, inaonyesha onyo na kusasisha kamusi ya finetune_parameters na vigezo hivi maalum vya modeli. Kazi ya ast.literal_eval hutumiwa kubadilisha vigezo maalum vya modeli kutoka kwa mfuatano wa maandishi kuwa kamusi ya Python.

    - Inaonyesha seti ya mwisho ya vigezo vya fine-tuning vitakavyotumika kwa mzunguko huu.

    - Kwa muhtasari, script hii inatayarisha na kuonyesha vigezo vya fine-tuning ya modeli ya mashine ya kujifunza, ikiwa na uwezo wa kubadilisha vigezo vya chaguo-msingi na vya modeli maalum.

    ```python
    # Weka vigezo vya mafunzo cha msingi kama vile idadi ya vipindi vya mafunzo, ukubwa wa kundi kwa mafunzo na tathmini, kiwango cha ujifunzaji, na aina ya ratiba ya kiwango cha ujifunzaji
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Weka vigezo vya usanifu cha msingi kama vile kama kutumia Layer-wise Relevance Propagation (LoRa) na DeepSpeed, na hatua ya DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Changanya vigezo vya mafunzo na usanifu katika kamusi moja iitwayo finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Angalia kama foundation_model ina vigezo maalum vya mfano vya kawaida
    # Ikiwa ipo, chapisha ujumbe wa onyo na sasisha kamusi ya finetune_parameters na vigezo hivi maalum vya mfano
    # Kazi ya ast.literal_eval hutumika kubadilisha vigezo maalum vya mfano kutoka mnyororo kuwa kamusi ya Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # badilisha mnyororo kuwa kamusi ya python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Chapisha seti ya mwisho ya vigezo vya fine-tuning vitakavyotumika kwa mchakato huo
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Mchakato wa Mafunzo (Training Pipeline)

1. Script hii ya Python inafafanua kazi ya kuunda jina la kuonyesha kwa mchakato wa mafunzo ya mashine ya kujifunza, kisha kuita kazi hii kuunda na kuchapisha jina la kuonyesha. Hapa ni muhtasari wa kile inachofanya:

1. Kazi get_pipeline_display_name imefafanuliwa. Kazi hii huunda jina la kuonyesha kulingana na vigezo mbalimbali vinavyohusiana na mchakato wa mafunzo.

1. Ndani ya kazi, huhesabu jumla ya ukubwa wa kundi kwa kuzidisha ukubwa wa kundi kwa kifaa, idadi ya hatua za ukusanyaji wa gradient, idadi ya GPUs kwa nodi, na idadi ya nodi zinazotumiwa kwa fine-tuning.

1. Inapata vigezo vingine kama vile aina ya ratiba ya kiwango cha kujifunza, kama DeepSpeed inatumika, hatua ya DeepSpeed, kama Layer-wise Relevance Propagation (LoRa) inatumika, kikomo cha idadi ya pointi za kuhifadhi modeli, na urefu wa mstari wa juu kabisa.

1. Inajenga mfuatano wa maneno unaojumuisha vigezo hivi vyote, vimegawanywa kwa vipande vigumu (-). Ikiwa DeepSpeed au LoRa zinatumika, mfuatano unajumuisha "ds" ikifuatiwa na hatua ya DeepSpeed, au "lora", mtawalia. Ikiwa sivyo, unajumuisha "nods" au "nolora" mtawalia.

1. Kazi inarudisha mfuatano huu wa maneno, ambao hutumika kama jina la kuonyesha kwa mchakato wa mafunzo.

1. Baada ya kazi kufafanuliwa, inaitwa kuunda jina la kuonyesha, ambalo halafu linachapishwa.

1. Kwa muhtasari, script hii inaunda jina la kuonyesha kwa mchakato wa mafunzo ya mashine ya kujifunza kulingana na vigezo mbalimbali, kisha linachapishwa.

    ```python
    # Fafanua kazi ya kuzalisha jina la kuonyesha kwa pipeline ya mafunzo
    def get_pipeline_display_name():
        # Hesabu ukubwa wa kundi lote kwa kuzidisha ukubwa wa kundi kwa kifaa, idadi ya hatua za mkusanyiko wa mteremko, idadi ya GPU kwa node, na idadi ya nodes zinazotumika kwa fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Pata aina ya ratiba ya kasi ya kujifunza
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Pata kama DeepSpeed inatumiwa
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Pata hatua ya DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Ikiwa DeepSpeed inatumiwa, jumuisha "ds" ikifuatiwa na hatua ya DeepSpeed katika jina la kuonyesha; ikiwa sivyo, jumuisha "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Pata kama Layer-wise Relevance Propagation (LoRa) inatumiwa
        lora = finetune_parameters.get("apply_lora", "false")
        # Ikiwa LoRa inatumiwa, jumuisha "lora" katika jina la kuonyesha; ikiwa sivyo, jumuisha "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Pata kikomo cha idadi ya titikio za mfano za kuhifadhi
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Pata urefu wa mlolongo wa juu kabisa
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Tengeneza jina la kuonyesha kwa kuunganisha vigezo vyote hivi, vikigawanyika kwa vifunga
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
    
    # Ita kazi kuunda jina la kuonyesha
    pipeline_display_name = get_pipeline_display_name()
    # Chapisha jina la kuonyesha
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Kusanidi Mchakato (Configuring Pipeline)

Script hii ya Python inafafanua na kusanidi mchakato wa mashine ya kujifunza kwa kutumia Azure Machine Learning SDK. Hapa ni muhtasari wa kile inachofanya:

1. Inaingiza moduli muhimu kutoka Azure AI ML SDK.

1. Inachukua kipengele cha mchakato kinachoitwa "chat_completion_pipeline" kutoka kwenye rejista.

1. Inafafanua kazi ya mchakato kwa kutumia kipendele cha `@pipeline` na kazi ya `create_pipeline`. Jina la mchakato limewekwa kuwa `pipeline_display_name`.

1. Ndani ya kazi ya `create_pipeline`, inanzisha kipengele cha mchakato kilichopatikana na vigezo mbalimbali, ikiwa ni pamoja na njia ya modeli, vikundi vya kompyuta kwa hatua tofauti, mgawanyo wa data za mafunzo na mtihani, idadi ya GPUs zinazotumiwa kwa fine-tuning, na vigezo vingine vya fine-tuning.

1. Inaunganisha matokeo ya kazi ya fine-tuning na matokeo ya kazi ya mchakato. Hii inafanywa ili modeli iliyofinywa upya iweze kusajiliwa kwa urahisi, jambo ambalo linahitajika kupeleka modeli kwenye njia ya mtandao au kundi.

1. Inaunda mfano wa mchakato kwa kuitisha kazi ya `create_pipeline`.

1. Inaweka mipangilio ya `force_rerun` ya mchakato kuwa `True`, maana yake matokeo yaliyohifadhiwa awali hayatatumika.

1. Inaweka mipangilio ya `continue_on_step_failure` ya mchakato kuwa `False`, maana yake mchakato utaacha ikiwa hatua yoyote itashindwa.

1. Kwa muhtasari, script hii inafafanua na kusanidi mchakato wa mashine ya kujifunza kwa kazi ya chat completion kwa kutumia Azure Machine Learning SDK.

    ```python
    # Ingiza moduli zinazohitajika kutoka kwa Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Pata sehemu ya bomba lenye jina "chat_completion_pipeline" kutoka kwenye rejista
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Eleza kazi ya bomba kwa kutumia @pipeline decorator na kazi ya create_pipeline
    # Jina la bomba limewekwa kuwa pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Anzisha sehemu ya bomba iliyo pata kwa vigezo mbalimbali
        # Hii ni pamoja na njia ya mfano, vikundi vya kompyuta kwa hatua tofauti, mgawanyiko wa seti za data kwa mafunzo na majaribio, idadi ya GPU za kutumia kwa urekebishaji, na vigezo vingine vya urekebishaji
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Ramani mgawanyiko wa seti za data kwa vigezo
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Mipangilio ya mafunzo
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Wekwa kwenye idadi ya GPU zilizopo kwenye kompyuta
            **finetune_parameters
        )
        return {
            # Ramani matokeo ya kazi ya urekebishaji kwa matokeo ya kazi ya bomba
            # Hii inafanywa ili tuweze kusajili kwa urahisi mfano uliorekebishwa
            # Kusajili mfano ni muhimu ili kupeleka mfano kwenye endpoint mtandaoni au wa kundi
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Tengeneza mfano wa bomba kwa kuita kazi ya create_pipeline
    pipeline_object = create_pipeline()
    
    # Usitumie matokeo ya zamani yaliyohifadhiwa kutoka kazi zilizopita
    pipeline_object.settings.force_rerun = True
    
    # Weka endelea kama hatua itashindwa kuwa False
    # Hii ina maana kuwa bomba litakoma ikiwa hatua yoyote itashindwa
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Wasilisha Kazi

1. Script hii ya Python inawasili kazi ya mchakato wa mashine ya kujifunza kwa Azure Machine Learning workspace na kusubiri kazi kukamilika. Hapa ni muhtasari wa kile inachofanya:

    - Inaita njia ya create_or_update kwa kitu cha jobs kwenye workspace_ml_client kuwasilisha kazi ya mchakato. Mchakato unaoendeshwa umeelezwa na pipeline_object, na jaribio lililo chini ya kazi limeelezwa na experiment_name.

    - Kisha inaita njia ya stream kwa kitu cha jobs kwenye workspace_ml_client kusubiri kazi ya mchakato kukamilika. Kazi inayosubiriwa imeelezwa na sifa ya name ya kitu cha pipeline_job.

    - Kwa muhtasari, script hii inawasili kazi ya mchakato wa mashine ya kujifunza kwa Azure Machine Learning workspace, kisha kusubiri kazi kukamilika.

    ```python
    # Tuma kazi ya pipeline kwenye eneo la kazi la Azure Machine Learning
    # Pipeline itakayotekelezwa imetajwa na pipeline_object
    # Jaribio ambalo kazi inaendeshwa liko limeainishwa na experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Subiri kazi ya pipeline kukamilika
    # Kazi ya kusubiri imetajwa kwa sifa ya jina ya object ya pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Sajili modeli iliyofinywa kwa workspace

Tutamsajili modeli kutoka matokeo ya kazi ya fine tuning. Hii itafuatilia uhusiano kati ya modeli iliyofinywa na kazi ya fine tuning. Kazi ya fine tuning, zaidi yake, inafuatilia uhusiano wa modeli ya msingi, data na msimbo wa mafunzo.

### Kusajili Modeli ya ML

1. Script hii ya Python inasajili modeli ya mashine ya kujifunza iliyofunzwa katika mchakato wa Azure Machine Learning. Hapa ni muhtasari wa kile inachofanya:

    - Inaingiza moduli muhimu kutoka Azure AI ML SDK.

    - Inakagua kama trained_model inapatikana kutoka matokeo ya kazi ya mchakato kwa kutumia njia ya get ya kitu cha jobs kwenye workspace_ml_client na kupata mali zake outputs.

    - Inajenga njia ya modeli iliyofunzwa kwa kuunda mfuatano wa maandishi na jina la kazi ya mchakato pamoja na jina la matokeo ("trained_model").

    - Inafafanua jina kwa modeli iliyofinywa kwa kuongeza "-ultrachat-200k" kwa jina la awali la modeli na kubadilisha sehemu zozote za slash kuwa hyphen.

    - Inajitayarisha kusajili modeli kwa kuunda kitu cha Model na vigezo mbalimbali, ikiwa ni pamoja na njia ya modeli, aina ya modeli (MLflow model), jina na toleo la modeli, na maelezo ya modeli.

    - Inasajili modeli kwa kuitisha njia ya create_or_update ya kitu cha models kwenye workspace_ml_client na kitu cha Model kama hoja.

    - Inachapisha modeli iliyosajiliwa.

1. Kwa muhtasari, script hii inasajili modeli ya mashine ya kujifunza iliyofunzwa katika mchakato wa Azure Machine Learning.
    
    ```python
    # Ingiza moduli muhimu kutoka kwa Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Angalia kama ukusanyo wa `trained_model` unapatikana kutoka kwa kazi ya pipeline
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Tengeneza njia ya kusafirisha modeli iliyofunzwa kwa kuunda muundo wa mfuatano wa jina la kazi ya pipeline na jina la matokeo ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Eleza jina la modeli iliyofunzwa kwa kuongeza "-ultrachat-200k" kwa jina la modeli ya asili na kubadilisha mikato yoyote kuwa mabano
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Andaa kusajili modeli kwa kuunda kitu cha Model na vigezo mbalimbali
    # Hii inajumuisha njia ya faili ya modeli, aina ya modeli (modeli ya MLflow), jina na toleo la modeli, na maelezo ya modeli
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Tumia alama ya wakati kama toleo ili kuepuka mgongano wa matoleo
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Sajili modeli kwa kuita njia ya create_or_update ya vitu vya models katika workspace_ml_client na chinhu cha Model kama hoja
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Chapisha modeli iliyosajiliwa
    print("registered model: \n", registered_model)
    ```

## 7. Peleka modeli iliyofinywa kwa endpoint ya mtandaoni

Endpoints za mtandaoni hutoa REST API ya kudumu inayoweza kutumika kuunganisha na programu zinazohitaji kutumia modeli.

### Simamia Endpoint

1. Script hii ya Python inaunda endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning kwa modeli iliyosajiliwa. Hapa ni muhtasari wa kile inachofanya:

    - Inaingiza moduli muhimu kutoka Azure AI ML SDK.

    - Inafafanua jina la kipekee kwa endpoint ya mtandaoni kwa kuongeza alama ya wakati (timestamp) kwenye maandishi "ultrachat-completion-".

    - Inajitayarisha kuunda endpoint ya mtandaoni kwa kuunda kitu cha ManagedOnlineEndpoint na vigezo mbalimbali, ikiwa ni pamoja na jina la endpoint, maelezo ya endpoint, na hali ya uthibitisho ("key").

    - Inaunda endpoint ya mtandaoni kwa kuitisha njia ya begin_create_or_update ya workspace_ml_client na kitu cha ManagedOnlineEndpoint kama hoja. Kisha inasubiri kazi ya kuunda kukamilika kwa kutumia njia ya wait.

1. Kwa muhtasari, script hii inaunda endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning kwa modeli iliyosajiliwa.

    ```python
    # Ingiza moduli muhimu kutoka Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Eleza jina la kipekee kwa endpoint mtandaoni kwa kuongeza alama ya wakati kwenye string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Jiandae kuunda endpoint mtandaoni kwa kuunda kitu cha ManagedOnlineEndpoint chenye vigezo mbalimbali
    # Hivi ni pamoja na jina la endpoint, maelezo ya endpoint, na njia ya uthibitishaji ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Unda endpoint mtandaoni kwa kuita njia ya begin_create_or_update ya workspace_ml_client ukiwa na kitu cha ManagedOnlineEndpoint kama hoja
    # Kisha subiri operesheni ya uundaji kukamilika kwa kuita njia ya wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Unaweza kupata hapa orodha ya SKU zinazoungwa mkono kwa ajili ya uenezaji - [Orodha ya SKU za endpoints zinazosimamiwa mtandaoni](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Kueneza Modeli ya ML

1. Script hii ya Python inapeleka modeli ya mashine ya kujifunza iliyosajiliwa kwa endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning. Hapa ni muhtasari wa kile inachofanya:

    - Inaingiza moduli ya ast, ambayo hutoa kazi za kuchambua miti ya sarufi ya muhtasari wa Python.

    - Inaweka aina ya kifaa kwa ajili ya uenezaji kuwa "Standard_NC6s_v3".

    - Inakagua kama alama ya inference_compute_allow_list ipo katika foundation model. Ikiwa ipo, hubadilisha thamani ya alama kutoka maandishi kuwa orodha ya Python na kuiweka katika inference_computes_allow_list. Ikiwa haipo, huweka inference_computes_allow_list kuwa None.

    - Inakagua ikiwa aina ya kifaa iliyowekwa iko katika orodha inayoaruhusu. Ikiwa siyo, inachapisha ujumbe unaomwomba mtumiaji kuchagua aina ya kifaa kutoka kwenye orodha hiyo.

    - Inajitayarisha kuunda uenezaji kwa kuunda kitu cha ManagedOnlineDeployment na vigezo mbalimbali, ikiwa ni pamoja na jina la uenezaji, jina la endpoint, kitambulisho cha modeli, aina na idadi ya kifaa, mipangilio ya liveness probe, na mipangilio ya maombi.

    - Inaunda uenezaji kwa kuitisha njia ya begin_create_or_update ya workspace_ml_client na kitu cha ManagedOnlineDeployment kama hoja. Kisha inasubiri uendeshaji wa kuunda ukamilike kwa kutumia njia ya wait.

    - Inaweka trafiki ya endpoint kuelekeza asilimia 100 ya trafiki kwa uenezaji wa "demo".

    - Inasasisha endpoint kwa kuitisha njia ya begin_create_or_update ya workspace_ml_client na kitu cha endpoint kama hoja. Kisha inasubiri mchakato wa sasisho kwa kutumia njia ya result.

1. Kwa muhtasari, script hii inapeleka modeli ya mashine ya kujifunza iliyosajiliwa kwa endpoint ya mtandaoni inayosimamiwa katika Azure Machine Learning.

    ```python
    # Ingiza moduli ya ast, ambayo hutoa kazi za kushughulikia miti ya sarufi ya syntax ya abstraction ya Python
    import ast
    
    # Weka aina ya mfano kwa ajili ya utoaji
    instance_type = "Standard_NC6s_v3"
    
    # Angalia kama lebo ya `inference_compute_allow_list` ipo katika mfano wa msingi
    if "inference_compute_allow_list" in foundation_model.tags:
        # Ikiwa ipo, badilisha thamani ya lebo kutoka kwa maandishi hadi orodha ya Python na uiweke kwa `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ikiwa haipo, weka `inference_computes_allow_list` kuwa `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Angalia kama aina ya mfano iliyotajwa iko katika orodha ya kuruhusiwa
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Jiandae kuunda utoaji kwa kuunda kitu cha `ManagedOnlineDeployment` chenye vigezo mbalimbali
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Unda utoaji kwa kuita njia ya `begin_create_or_update` ya `workspace_ml_client` ukiwa na kitu cha `ManagedOnlineDeployment` kama hoja
    # Kisha subiri mchakato wa kuunda ukamilike kwa kuita njia ya `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Weka trafiki ya sehemu ya mwisho kuielekeza trafiki yote 100% kwa utoaji wa "demo"
    endpoint.traffic = {"demo": 100}
    
    # Sasisha sehemu ya mwisho kwa kuita njia ya `begin_create_or_update` ya `workspace_ml_client` ukiwa na kitu cha `endpoint` kama hoja
    # Kisha subiri mchakato wa sasisho ukamilike kwa kuita njia ya `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Jaribu endpoint na data ya mfano

Tutachukua baadhi ya data ya mfano kutoka dataset ya mtihani na kuwasilisha kwa endpoint ya mtandaoni kwa ajili ya uchambuzi. Kisha tutaonyesha lebo zilizopimwa pamoja na lebo za ukweli.

### Kusoma Matokeo

1. Script hii ya Python inasoma faili la JSON Lines hadi pandas DataFrame, kuchukua sampuli ya nasibu, na kuweka upya fahirisi. Hapa ni muhtasari wa kile inachofanya:

    - Inasoma faili ./ultrachat_200k_dataset/test_gen.jsonl ndani ya pandas DataFrame. Kazi ya read_json inatumika kwa hoja lines=True kwa sababu faili iko katika muundo wa JSON Lines, ambapo kila mstari ni kitu tofauti cha JSON.

    - Inachukua sampuli ya nasibu ya mstari 1 kutoka DataFrame. Kazi ya sample inatumia hoja n=1 kubainisha idadi ya mistari ya nasibu kuchaguliwa.

    - Inaweka upya fahirisi ya DataFrame. Kazi ya reset_index inatumia hoja drop=True kuoza fahirisi ya awali na kuiweka na fahirisi mpya ya nambari za kawaida.

    - Inaonyesha mistari 2 ya kwanza ya DataFrame kwa kutumia kazi ya head na hoja 2. Hata hivyo, kwa kuwa DataFrame ina mstari mmoja tu baada ya sampuli, hii itaonyesha mstari huo mmoja tu.

1. Kwa muhtasari, script hii inasoma faili la JSON Lines ndani ya pandas DataFrame, kuchukua sampuli ya nasibu ya mstari 1, kuweka upya fahirisi, na kuonyesha mstari wa kwanza.
    
    ```python
    # Ingiza maktaba ya pandas
    import pandas as pd
    
    # Soma faili la JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' kwenye DataFrame ya pandas
    # Hoja 'lines=True' inaonyesha kuwa faili iko katika muundo wa JSON Lines, ambapo kila mstari ni kitu tofauti cha JSON
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Chukua sampuli nasibu ya safu 1 kutoka kwa DataFrame
    # Hoja 'n=1' inaelezea idadi ya mistari ya nasibu kuchaguliwa
    test_df = test_df.sample(n=1)
    
    # Weka upya index ya DataFrame
    # Hoja 'drop=True' inaonyesha kuwa index ya awali inapaswa kuondolewa na kuchukuliwa nafasi na index mpya ya nambari za kawaida
    # Hoja 'inplace=True' inaonyesha kuwa DataFrame inapaswa kubadilishwa mahali pake (bila kuunda kitu kipya)
    test_df.reset_index(drop=True, inplace=True)
    
    # Onyesha mistari 2 ya kwanza ya DataFrame
    # Hata hivyo, kwa kuwa DataFrame ina mstari mmoja tu baada ya kuchukua sampuli, hii itaonyesha mstari huo mmoja tu
    test_df.head(2)
    ```

### Unda Kitu cha JSON

1. Script hii ya Python inaunda kitu cha JSON chenye vigezo maalum na kuihifadhi katika faili. Hapa ni muhtasari wa kile inachofanya:

    - Inaingiza moduli ya json, ambayo hutoa kazi za kufanya kazi na data za JSON.
    - Inaunda kamusi ya parameters yenye funguo na thamani zinazoashiria vigezo vya mfano wa kujifunza kwa mashine. Funguo ni "temperature", "top_p", "do_sample", na "max_new_tokens", na thamani zao zinafanana na 0.6, 0.9, Kweli, na 200 mtawaliwa.

    - Inaunda kamusi nyingine ya test_json yenye funguo mbili: "input_data" na "params". Thamani ya "input_data" ni kamusi nyingine yenye funguo "input_string" na "parameters". Thamani ya "input_string" ni orodha yenye ujumbe wa kwanza kutoka kwenye DataFrame ya test_df. Thamani ya "parameters" ni kamusi ya parameters iliyoundwa hapo awali. Thamani ya "params" ni kamusi tupu.

    - Inafungua faili linaloitwa sample_score.json
    
    ```python
    # Ingiza moduli ya json, ambayo hutoa kazi za kufanya kazi na data za JSON
    import json
    
    # Tengeneza kamusi `parameters` yenye funguo na thamani zinazowakilisha vigezo kwa mfano wa kujifunza mashine
    # Funguo ni "temperature", "top_p", "do_sample", na "max_new_tokens", na thamani zao zinazolingana ni 0.6, 0.9, True, na 200 mtawaliwa
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Tengeneza kamusi nyingine `test_json` yenye funguo mbili: "input_data" na "params"
    # Thamani ya "input_data" ni kamusi nyingine yenye funguo "input_string" na "parameters"
    # Thamani ya "input_string" ni orodha inayojumuisha ujumbe wa kwanza kutoka DataFrame `test_df`
    # Thamani ya "parameters" ni kamusi ya `parameters` iliyotengenezwa awali
    # Thamani ya "params" ni kamusi tupu
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Fungua faili lenye jina `sample_score.json` kwenye saraka `./ultrachat_200k_dataset` kwa hali ya kuandika
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Andika kamusi ya `test_json` kwenye faili kwa fomati ya JSON kwa kutumia kazi ya `json.dump`
        json.dump(test_json, f)
    ```

### Kuitisha Endpoint

1. Hii script ya Python inaitisha endpoint mtandaoni katika Azure Machine Learning ili kufanya upimaji wa faili ya JSON. Hapa kuna muhtasari wa kile inachofanya:

    - Inaita njia ya invoke ya sifa ya online_endpoints ya kitu cha workspace_ml_client. Njia hii hutumika kutuma ombi kwa endpoint mtandaoni na kupata majibu.

    - Inabainisha jina la endpoint na usambazaji kwa vigezo vya endpoint_name na deployment_name. Katika kesi hii, jina la endpoint limehifadhiwa katika tofauti ya online_endpoint_name na jina la usambazaji ni "demo".

    - Inabainisha njia ya faili ya JSON inayopaswa kupimwa kwa kutumia kigezo cha request_file. Katika kesi hii, faili ni ./ultrachat_200k_dataset/sample_score.json.

    - Inahifadhi jibu kutoka kwa endpoint kwenye tofauti ya response.

    - Inachapisha jibu halisi.

1. Kwa muhtasari, script hii inaitisha endpoint mtandaoni katika Azure Machine Learning ili kupima faili la JSON na kuchapisha jibu.

    ```python
    # Ita kiungo mtandaoni katika Azure Machine Learning ili upime faili la `sample_score.json`
    # Njia ya `invoke` ya mali ya `online_endpoints` ya kitu cha `workspace_ml_client` hutumika kutuma ombi kwa kiungo mtandaoni na kupata majibu
    # Hoja ya `endpoint_name` inaonyesha jina la kiungo, ambalo limehifadhiwa katika tofauti ya `online_endpoint_name`
    # Hoja ya `deployment_name` inaonyesha jina la usambazaji, ambalo ni "demo"
    # Hoja ya `request_file` inaonyesha njia ya faili la JSON ambalo litapimwa, ambalo ni `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Chapisha jibu halisi kutoka kwa kiungo
    print("raw response: \n", response, "\n")
    ```

## 9. Futa endpoint mtandaoni

1. Usisahau kufuta endpoint mtandaoni, vinginevyo utaacha mita ya bili ikendeshwa kwa ajili ya kompyuta inayotumiwa na endpoint. Mstari huu wa msimbo wa Python unafuta endpoint mtandaoni katika Azure Machine Learning. Hapa kuna muhtasari wa kile inachofanya:

    - Inaita njia ya begin_delete ya sifa ya online_endpoints ya kitu cha workspace_ml_client. Njia hii hutumika kuanza kufuta endpoint mtandaoni.

    - Inabainisha jina la endpoint inayofutwa kwa kigezo cha name. Katika kesi hii, jina la endpoint limehifadhiwa katika tofauti ya online_endpoint_name.

    - Inaita njia ya wait kusubiri mchakato wa kufuta ukamilike. Hii ni operesheni inayozuia, ikimaanisha itazuia script kuendelea hadi kufutwa kumalizike.

    - Kwa muhtasari, mstari huu wa msimbo unaanza kufuta endpoint mtandaoni katika Azure Machine Learning na kusubiri operesheni kumalizika.

    ```python
    # Futa kiungo mtandaoni katika Azure Machine Learning
    # Njia ya `begin_delete` ya mali ya `online_endpoints` ya kitu `workspace_ml_client` hutumika kuanza kufuta kiungo mtandaoni
    # Hoja ya `name` inaelezea jina la kiungo kinachotakiwa kufutwa, ambacho huhifadhiwa katika tofauti ya `online_endpoint_name`
    # Njia ya `wait` inaitwa kusubiri operesheni ya ufutaji kumalizika. Hii ni operesheni ya kuzuia, inayomaanisha kwamba itazuia script kuendelea hadi ufutaji ukamilike
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Hatia ya kuwajibika**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya kutafsiri kwa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au yasiyo sahihi. Nyaraka ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia utafsiri wa kitaalamu wa binadamu. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->