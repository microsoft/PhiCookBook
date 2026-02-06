## Azure ML సిస్టమ్ రిజిస్ట్రి నుండి చాట్-కంప్లీషన్ కంపోనెంట్స్‌ను ఉపయోగించి మోడల్‌నుఫైన్ ట్యూన్ చేయడం ఎలా

ఈ ఉదాహరణలో, మేము ultrachat_200k డేటాసెట్‌ను ఉపయోగించి 2 మంది మధ్య సంభాషణను పూర్తిచేయడానికి Phi-3-mini-4k-instruct మోడల్‌ను ఫైన్ ట్యూన్ చేస్తాము.

![MLFineTune](../../../../translated_images/te/MLFineTune.928d4c6b3767dd35.webp)

ఈ ఉదాహరణ Azure ML SDK మరియు Python ఉపయోగించి ఫైన్ ట్యూన్ ఎలా చేయాలో మరియు ఆ తరువాత రియల్ టైంలో సూచన కోసం ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు ఫైన్ ట్యూన్ చేసిన మోడల్‌ను ఎలా డిప్లాయ్ చేయాలో చూపిస్తుంది.

### శిక్షణ డేటా

మేము ultrachat_200k డేటాసెట్‌ను ఉపయోగిస్తాము. ఇది UltraChat డేటాసెట్ యొక్క తీవ్రమైన ఫిల్టర్ చేయబడిన వెర్షన్ మరియు Zephyr-7B-β శిక్షణ కోసం ఉపయోగించారు, ఇది అత్యాధునిక 7b చాట్ మోడల్.

### మోడల్

మేము Phi-3-mini-4k-instruct మోడల్‌ను ఉపయోగిస్తాము, దీని ద్వారా వినియోగదారుడు చాట్-కంప్లీషన్ పని కోసం మోడల్‌ను ఎలా ఫైన్ ట్యూన్ చేయాలో చూపించాలి. మీరు ఈ నోట్బుక్‌ను ఒక నిర్దిష్ట మోడల్ కార్డ్ నుండి తెరిచినట్లయితే, దయచేసి ఆ నిర్దిష్ట మోడల్ పేరును మార్చుకోండి.

### పనులు

- ఫైన్ ట్యూన్ చేయడానికి ఒక మోడల్ ను ఎంచుకోండి.
- శిక్షణ డేటాను ఎంచుకుని అన్వేషించండి.
- ఫైన్ ట్యూనింగ్ జాబ్‌ను కాన్ఫిగర్ చేయండి.
- ఫైన్ ట్యూనింగ్ జాబ్‌ను నడపండి.
- శిక్షణ మరియు మూల్యాంకన మీట్రిక్స్‌ను సమీక్షించండి.
- ఫైన్ ట్యూన్ చేసిన మోడల్‌ను రిజిస్టర్ చేయండి.
- రియల్ టైం సూచన కోసం ఫైన్ ట్యూన్ చేసిన మోడల్‌ను డిప్లాయ్ చేయండి.
- వనరులను క్లియర్ చేయండి.

## 1. ముందస్తు అవసరాలను సెటప్ చేయండి

- డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి
- AzureML వర్క్‌స్పేస్‌కు కనెక్ట్ అవ్వండి. మరింత తెలుసుకోడానికి SDK ఆథెంటికేషన్ సెటప్ చూడు. క్రింద <WORKSPACE_NAME>, <RESOURCE_GROUP> మరియు <SUBSCRIPTION_ID> మార్పిడి చేయండి.
- azureml సిస్టమ్ రిజిస్ట్రి కి కనెక్ట్ అవ్వండి
- ఆప్షనల్ ఎక్స్‌పీరిమెంట్ పేరును సెట్ చేయండి
- కంప్యూట్‌ను చెక్ లేదా క్రియేట్ చేయండి.

> [!NOTE]
> అవసరాలకు ఒక GPU నోడ్‌లో ఒకటి కంటే ఎక్కువ GPU కార్డులు ఉండవచ్చు. ఉదాహరణకు, Standard_NC24rs_v3 లో ఒక నోడ్ వద్ద 4 NVIDIA V100 GPUs ఉంటాయి, Standard_NC12s_v3లో 2 NVIDIA V100 GPUs ఉంటాయి. ఈ సమాచారానికి డాక్స్ చూడండి. ఒక నోడ్‌కి GPU కార్డుల సంఖ్య క్రింద ఉన్న gpus_per_node ప్యారామీటర్‌లో సెట్ చేస్తారు. సరియైన విలువ సెట్ చేయడం నోడ్‌లో సమస్త GPUs వాడుకకు సహాయపడుతుంది. సిఫార్సు చేయబడిన GPU కంప్యూట్ SKUs ఇక్కడ మరియు ఇక్కడ చూడండి.

### Python లైబ్రరరీలు

క్రింద ఉన్న సెల్‌ను రన్ చేసి డిపెండెన్సీలను ఇన్‌స్టాల్ చేసుకోండి. ఇది కొత్త ఎన్‌విరాన్మెంట్‌లో నడిపితే తప్పనిసరి దశ.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure MLతో ఇంటర్రాక్ట్ చేయడం

1. ఈ Python స్క్రిప్ట్ Azure Machine Learning (Azure ML) సేవతో ఇంటర్రాక్ట్ చేయడానికి ఉపయోగిస్తారు. దీని వివరణ ఇపుడు ఇవ్వబడుతోంది:

    - అవసరమైన మాడ్యూల్స్ azure.ai.ml, azure.identity, మరియు azure.ai.ml.entities నుండి దిగుమతి చేసుకుంటుంది. అలాగే time మాడ్యూల్‌ను కూడా దిగుమతి చేసుకుంటుంది.

    - DefaultAzureCredential() ఉపయోగించి ఆథెంటికేట్ చేయడానికి ప్రయత్నిస్తుందని, ఇది Azure క్లౌడ్‌లో రన్ అయ్యే అప్లికేషన్లను త్వరగా అభివృద్ధి చేయడానికి సులభమైన ఆథెంటికేషన్‌ను అందిస్తుంది. ఇది విఫలమైతే, InteractiveBrowserCredential() ఉపయోగించి ఇంటరాక్టివ్ లాగిన్ ప్రాంప్ట్ ప్రదర్శిస్తుంది.

    - తరువాత MLClient_INSTANCE ను from_config పద్ధతితో సృష్టించడానికి ప్రయత్నిస్తుంది, ఇది డిఫాల్ట్ కాన్ఫిగరేషన్ ఫైల్(config.json) నుండి కాన్ఫిగరేషన్ చదుతుంది. విఫలమైతే, subscription_id, resource_group_name, మరియు workspace_name ను మాన్యువల్‌గా అందిస్తూ MLClient_Instance ను సృష్టిస్తుంది.

    - "azureml" అనే Azure ML రిజిస్ట్రి కోసం మరో MLClient INSTANCE సృష్టిస్తుంది. ఈ రిజిస్ట్రీలో మోడల్స్, ఫైన్-ట్యూనింగ్ పైప్‌లైన్లు మరియు ఎన్విరోన్మెంట్లు నిల్వ ఉంటాయి.

    - experiment_name ను "chat_completion_Phi-3-mini-4k-instruct" గా సెట్ చేస్తుంది.

    - ప్రస్తుత సమయాన్ని (epoch నుండి సెకన్లలో, ఫ్లోటింగ్ పాయింట్ సంఖ్యగా) పూర్తిసంఖ్యగా మలచి స్ట్రింగ్‌కు మార్చుతూ ఒక ప్రత్యేక టైమ్‌స్టాంప్ ఉత్పత్తి చేస్తుంది. ఈ టైమ్‌స్టాంప్ ప్రత్యేక పేర్లు మరియు వెర్షన్ల కోసం ఉపయోగపడుతుంది.

    ```python
    # Azure ML మరియు Azure Identity నుండి అవసరం modules ను దిగుమతి చేయండి
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # time module ను దిగుమతి చేయండి
    
    # DefaultAzureCredential ఉపయోగించి authenticate చేయడానికి ప్రయత్నించండి
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # DefaultAzureCredential విఫలమైతే, InteractiveBrowserCredential ఉపయోగించండి
        credential = InteractiveBrowserCredential()
    
    # డిఫాల్ట్ config ఫైల్ ఉపయోగించి MLClient instance సృష్టించడానికి ప్రయత్నించండి
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # అది విఫలమైతే, వివరాలను మాన్యువలీ ఇవ్వడం ద్వారా MLClient instance సృష్టించండి
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" అనే Azure ML registry కోసం మరో MLClient instance సృష్టించండి
    # ఈ registry లో మోడల్స్, fine-tuning pipelines, మరియు environments నిల్వ ఉంటాయి
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # experiment పేరు సెట్ చేయండి
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # ప్రత్యేకమైన పేర్లు మరియు versionలకు ఉపయోగించే ఒక ప్రత్యేక timestamp ఉత్పత్తి చేయండి
    timestamp = str(int(time.time()))
    ```

## 2. ఫైన్ ట్యూన్ చేయవలసిన ఫౌండేషన్ మోడల్ ఎంచుకోండి

1. Phi-3-mini-4k-instruct అనేది 3.8 బిలియన్లు పరిమాణాలు కలిగిన, తేలికపాటి, ఆధునిక ఓపెన్ మోడల్, ఇది Phi-2 కోసం ఉపయోగించిన డేటాసెట్లపై ఆధారపడి ఉంటుంది. ఈ మోడల్ Phi-3 మోడల్ కుటుంబానికి చెందినది మరియు Mini వెర్షన్ రెండు వేరియంట్లలో ఉంది: 4K మరియు 128K, ఇది మద్దతు ఇచ్చే కాంటెక్స్ట్ లెన్త్ (టోకెన్లలో). మన ఉద్దేశ్యంలో ఉపయోగించడానికి ఈ మోడల్‌ను ఫైన్ ట్యూన్ చేయాలి. మీరు ఈ నోట్బుక్‌ను వేరే మోడల్ కోసం ఓపెన్ చేసినట్లయితే, దయచేసి మోడల్ పేరు మరియు వెర్షన్‌ను తగు ప్రకారం మార్చుకోండి.

> [!NOTE]
> మోడల్ id ప్రాపర్టీ ఫైన్ ట్యూనింగ్ జాబ్‌లో ఇన్పుట్‌గా పంపించబడుతుంది. ఇది AzureML స్టూడియో మోడల్ క్యాటలాగ్‌లోని మోడల్ వివరాల పేజీలో కూడా Asset ID ఫీల్డ్‌గా లభిస్తుంది.

2. ఈ Python స్క్రిప్ట్ Azure Machine Learning (Azure ML) సేవతో ఇంటర్రాక్ట్ చేస్తోంది. దీని వివరణ:

    - model_name ను "Phi-3-mini-4k-instruct" గా సెట్ చేస్తుంది.

    - registry_ml_client ఆబ్జెక్ట్ లోని models ప్రాపర్టీలో get పద్ధతిని ఉపయోగించి, సూచించిన పేరుతో AzureML రిజిస్ట్రి నుండి తాజా మోడల్ వెర్షన్‌ను పొందుతుంది. get పద్ధతికి రెండు ఆర్గ్యుమెంట్లు త్వరగా పిలవబడతాయి: మోడల్ పేరు మరియు తాజా వెర్షన్ తీసుకోవాలని సూచించే లేబుల్.

    - ఫైన్ ట్యూనింగ్ కోసం ఏ మోడల్ ఉపయోగించబడుతుందో, దాని పేరు, వెర్షన్ మరియు id ద్వారా కన్సోల్‌లో ఒక సందేశం ప్రింట్ చేస్తుంది. స్ర్టింగ్ ఫార్మాట్ పద్ధతిని ఉపయోగించి ఈ విలువలు సందేశంలో చేర్చబడతాయి.

    ```python
    # మోడల్ పేరు సెట్ చేయండి
    model_name = "Phi-3-mini-4k-instruct"
    
    # Azure ML రిజిస్ట్రీ నుండి మోడల్ యొక్క తాజా సంచికను పొందండి
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # మోడల్ పేరు, సంచిక, మరియు ID ను మುದ్రించండి
    # ఈ సమాచారం ట్రాకింగ్ మరియు డీబగింగ్ కి ఉపయోగపడుతుంది
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. జాబ్ కోసం ఉపయోగించే కంప్యూట్‌ను సృష్టించండి

ఫైన్ ట్యూన్ జాబ్ GPU కంప్యూట్‌తోనే పనిచేస్తుంది. కంప్యూట్ పరిమాణం మోడల్ ఎంత పెద్దదో ఆధారపడి ఉంటుంది మరియు చాలా సందర్భాల్లో సరైన కంప్యూట్‌ను గుర్తించడం కష్టం. ఈ సెల్ లో యూజర్‌ను సరైన కంప్యూట్ ఎంచుకోవడానికి గైడ్ చేస్తుంది.

> [!NOTE]
> క్రింద ఇచ్చిన computes అత్యుత్తమ కాన్ఫిగరేషన్‌తో పనిచేస్తాయి. కాన్ఫిగరేషన్‌లలో ఏవైనా మార్పులు CUDA Out Of Memory దోషానికి దారితీయవచ్చు. అట్టవంటి పరిస్థితుల్లో, కంప్యూట్‌ను పెద్ద పరిమాణంలోకి అప్‌గ్రేడ్ చేయండి.

> [!NOTE]
> compute_cluster_size ఎంచుకునేటప్పుడు దయచేసి మీ resource group లో ఆ compute అందుబాటులో ఉన్నదో చూసుకోండి. ఒక compute అందుబాటులో లేకపోతే compute వనరులు పొందడానికి అభ్యర్థన చేయవచ్చు.

### ఫైన్ ట్యూనింగ్ మద్దతు కోసం మోడల్ తనిఖీ

1. ఈ Python స్క్రిప్ట్ Azure ML లోని ఒక మోడల్‌తో ఇంటర్రాక్ట్ చేస్తోంది. వివరణ:

    - ast మాడ్యూల్ ను దిగుమతి చేస్తోంది, ఇది Python ఆబ్స్ట్రాక్ట్ సింటాక్స్ ట్రీలను ప్రాసెస్ చేసే ఫంక్షన్లు అందిస్తుంది.

    - foundation_model ఆబ్జెక్ట్ (Azure ML లోని మోడల్ ప్రతినిధి) finetune_compute_allow_list అనే ట్యాగ్ ఉన్నదో లేదో తనిఖీ చేస్తోంది. Azure ML లో ట్యాగ్లు key-value జంటలు, వాటిని మోడల్స్ ను ఫిల్టర్ చేయడానికి మరియు క్రమబద్ధీకరించడానికి ఉపయోగిస్తారు.

    - finetune_compute_allow_list ట్యాగ్ ఉన్నట్లయితే, ast.literal_eval() ఉపయోగించి ట్యాగ్ విలువను (స్ట్రింగ్) సురక్షితంగా Python లిస్టుగా మార్చి computes_allow_list కి జమ చేస్తుంది. తరువాత కంప్యూట్‌లు ఆ లిస్ట్లో నుంచి ఎంచుకోవాలని సందేశం ప్రింట్ చేస్తుంది.

    - finetune_compute_allow_list ట్యాగ్ లేకపోతే, computes_allow_list ను None గా సెట్ చేసి ఆ ట్యాగ్ మోడల్ ట్యాగ్స్‌లో లేదు అని సూచించే సందేశం ప్రింట్ చేస్తుంది.

    - ముస్లిగా, ఈ స్క్రిప్ట్ మోడల్ మెటాడేటాలో ఒక నిర్దిష్ట ట్యాగ్ కోసం తనిఖీ చేసి, ఆ ట్యాగ్ విలువను లిస్టుగా మార్చి వినియోగదారుకు సూచనలు ఇస్తుంది.

    ```python
    # Python అసాంఖ్యిక శాస్త్ర వ్యాకరణ వృక్షాలను ప్రాసెస్ చేయడానికి ఫంక్షన్లను అందించే ast మాడ్యూల్‌ను దిగుమతి చేయండి
    import ast
    
    # మోడల్ ట్యాగ్‌లలో 'finetune_compute_allow_list' ట్యాగ్ ఉందో లేదో తనిఖీ చేయండి
    if "finetune_compute_allow_list" in foundation_model.tags:
        # ట్యాగ్ ఉంటే, ast.literal_eval ఉపయోగించి ట్యాగ్ విలువ (స్ట్రింగ్) ను సురక్షితంగా Python జాబితాగా పార్స్ చేయండి
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # స్ట్రింగ్ ను python జాబితాగా మార్చండి
        # జాబితా నుండి కంప్యూట్ సృష్టించాలనే సందేశం ముద్రించండి
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # ట్యాగ్ లేకపోతే, computes_allow_list ను None గా సెట్ చేయండి
        computes_allow_list = None
        # 'finetune_compute_allow_list' ట్యాగ్ మోడల్ ట్యాగ్‌ల్లో భాగం కాదు అని సందేశం ముద్రించండి
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### కంప్యూట్ ఇన్‌స్టాన్స్ తనిఖీ

1. ఈ Python స్క్రిప్ట్ Azure ML కంప్యూట్ ఇన్‌స్టాన్స్‌పై పలు తనిఖీలను చేస్తుంది. వివరణ:

    - compute_cluster లో ఉన్న పేరుతో కంప్యూట్ ఇన్‌స్టాన్స్‌ను Azure ML వర్క్‌స్పేస్ నుండి పొందడానికి ప్రయత్నిస్తుంది. కంప్యూట్ ఇన్‌స్టాన్స్ యొక్క provisioning స్టేట్ "failed" అయితే ValueError ను తీస్తుంది.

    - computes_allow_list None కాకపోతే, ఆ లిస్టులో ఉన్న అన్ని కంప్యూట్ పరిమాణాలను లోయర్‌కేస్‌గా మార్చి, ప్రస్తుత కంప్యూట్ పరిమాణం ఆ లిస్టులో ఉందో లేదో తనిఖీ చేస్తుంది. లేకపోతే ValueError ను తీస్తుంది.

    - computes_allow_list None అయితే, కంప్యూట్ పరిమాణం అనుగుణంగా లేని GPU VM పరిమాణాల లిస్టులో ఉన్నదో లేదో తనిఖీ చేస్తుంది. ఉన్నట్లయితే ValueError తీస్తుంది.

    - వర్క్‌స్పేస్‌లో అందుబాటులో ఉన్న కంప్యూట్ పరిమాణాల జాబితాను పొందుతుంది. ఆ జాబితాలో ప్రతి పరిమాణం పేరుతో ప్రస్తుత కంప్యూట్ పరిమాణం తగులుతుందో లేదో చూసి, దానికి సంబంధించిన GPU కౌంట్‌ను పొందుతుంది మరియు gpu_count_found ను True గా సెట్ చేస్తుంది.

    - gpu_count_found True అయితే కంప్యూట్ ఇన్‌స్టాన్స్‌లో GPUల సంఖ్యను ప్రింట్ చేస్తుంది. లేకపోతే ValueError తీస్తుంది.

    - క్రింద చూపించడం కంటే, ఈ స్క్రిప్ట్ Azure ML కంప్యూట్ ఇన్‌స్టాన్స్‌ను provisioning స్థితి, పరిమాణం అనుమతుల జాబితా, మరియు GPUల సంఖ్య పరంగా తనిఖీ చేస్తుంది.

    ```python
    # ఎక్సెప్షన్ సందేశాన్ని ప్రింట్ చేయండి
    print(e)
    # వర్క్‌స్పేస్‌లో కంప్యూట్ సైజ్ అందుబాటులో లేకపోతే ValueError ను ఉత్పత్తి చేయండి
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML వర్క్‌స్పేస్ నుండి కంప్యూట్ ఇంస్టాన్స్‌ని ఎలా రికవరీ చేయాలి
    compute = workspace_ml_client.compute.get(compute_cluster)
    # కంప్యూట్ ఇంస్టాన్స్ యొక్క ప్రావిజనింగ్ స్థితి "విఫలమైంది" లేదా కాదో తనిఖీ చేయండి
    if compute.provisioning_state.lower() == "failed":
        # ప్రావిజనింగ్ స్థితి "విఫలమైంది" అయితే ValueError ను ఉత్పత్తి చేయండి
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # computes_allow_list None కాదా అనే దాన్ని తనిఖీ చేయండి
    if computes_allow_list is not None:
        # computes_allow_list లోని అన్ని కంప్యూట్ సైజ్‌లను చిన్న అక్షరాలలోకి మార్చండి
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # కంప్యూట్ ఇంస్టాన్స్ సైజ్ computes_allow_list_lower_case లో ఉందా అని తనిఖీ చేయండి
        if compute.size.lower() not in computes_allow_list_lower_case:
            # కంప్యూట్ ఇంస్టాన్స్ సైజ్ computes_allow_list_lower_case లో లేకపోతే ValueError ను ఉత్పత్తి చేయండి
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # మద్దతు లేని GPU VM సైజుల జాబితాను నిర్వచించండి
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # కంప్యూట్ ఇంస్టాన్స్ సైజ్ unsupported_gpu_vm_list లో ఉందా అని తనిఖీ చేయండి
        if compute.size.lower() in unsupported_gpu_vm_list:
            # కంప్యూట్ ఇంస్టాన్స్ సైజ్ unsupported_gpu_vm_list లో ఉంటే ValueError ను ఉత్పత్తి చేయండి
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # కంప్యూట్ ఇంస్టాన్స్‌లో GPU ల సంఖ్య గుర్తింపు కోసం ఒక ఫ్లాగ్‌ను ప్రారంభించండి
    gpu_count_found = False
    # వర్క్‌స్పేస్‌లో అందుబాటులో ఉన్న అన్ని కంప్యూట్ సైజుల జాబితాని తీసుకోండి
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # అందుబాటులో ఉన్న కంప్యూట్ సైజుల జాబితా మీద లూప్ చేయండి
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # కంప్యూట్ సైజ్ పేరుతో కంప్యూట్ ఇంస్టాన్స్ సైజ్ సరిపోతుందా అని తనిఖీ చేయండి
        if compute_sku.name.lower() == compute.size.lower():
            # సరిపోతే, ఆ కంప్యూట్ సైజ్ యొక్క GPU ల సంఖ్యను తీసుకొని gpu_count_found ను True గా సెట్ చేయండి
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # gpu_count_found True అయితే, కంప్యూట్ ఇంస్టాన్స్‌లో GPU ల సంఖ్యను ప్రింట్ చేయండి
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # gpu_count_found False అయితే, ValueError ను ఉత్పత్తి చేయండి
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. మోడల్‌ను ఫైన్ ట్యూనింగ్ కోసం డేటాసెట్ ఎంచుకోండి

1. మేము ultrachat_200k డేటాసెట్‌ను ఉపయోగిస్తాము. ఈ డేటాసెట్ నాలుగు స్ప్లిట్లను కలిగి ఉంది, ఇది Supervised fine-tuning (sft)కి తగినది.
Generation ranking (gen). ప్రతి స్ప్లిట్‌కు ఉదాహరణల సంఖ్య క్రింది విధంగా చూపబడింది:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. తదుపరి కొన్ని సెల్స్ ఫైన్ ట్యూనింగ్ కోసం ప్రాథమిక డేటా సిద్ధతను చూపిస్తాయి:

### కొంత డేటా సారివివరాలను వీక్షించండి

ఈ నమూనా త్వరగా నడవాలి కనుక, train_sft, test_sft ఫైళ్లు ఇప్పటికే కాపాడిన వరుసల 5%తో సేవ్ చేస్తాము. అంటే ఫైన్ ట్యూన్ చేసిన మోడల్ తక్కువ ఖచ్చితత్వం కలిగి ఉంటుంది, అందువలన దీన్ని నిజ జీవిత వినియోగానికి ఉపయోగించకూడదు.
download-dataset.py స్ప్రిప్ట్ ultrachat_200k డేటాసెట్‌ను డౌన్‌లోడ్ చేసి, డేటాసెట్‌ను ఫైన్ ట్యూన్ పైప్‌లైన్ కంపోనెంట్ వినియోగించే ఫార్మాట్‌గా మార్చడానికి ఉపయోగిస్తారు. డేటాసెట్ పెద్దదిగా ఉండటంతో, మేము ఇక్కడ డేటాసెట్ ఒక భాగాన్ని మాత్రమే కలిగి ఉన్నాము.

1. క్రింద చూపిన స్క్రిప్ట్ 5% డేటా మాత్రమే డౌన్‌లోడ్ చేస్తుంది. dataset_split_pc పేరామీటర్‌ను కావలిసిన శాతం మార్చడం ద్వారా దీనిని పెంచుకోవచ్చు.

> [!NOTE]
> కొన్ని భాషా మోడల్స్ వేర్వేరు భాషా కోడ్లను కలిగి ఉంటారు, అందువల్ల డేటాసెట్‌లో కాలమ్ పేర్లూ ఆ భాషా కోడ్లను ప్రతిబింబించాలి.

1. డేటా ఎలా ఉండాలో ఒక ఉదాహరణ ఇది:
చాట్-కంప్లీషన్ డేటాసెట్ parquet ఫార్మాట్‌లో నిల్వ ఉంటుంది, ప్రతి ఎంట్రీ క్రింద చూపిన స్కీమ్‌ను అనుసరిస్తుంది:

    - ఇది JSON (JavaScript Object Notation) డాక్యుమెంట్, ఇది ప్రసిద్ధ డేటా మార్పిడి ఫార్మాట్. ఇది రన్ అయ్యే కోడ్ కాదు, డేటాను నిల్వ చేయడానికి మరియు మార్చుకోవడానికి మార్గం. దాని నిర్మాణం ఇదీ:

    - "prompt": ఇది ఒక స్ట్రింగ్ విలువను కలిగి ఉంటుంది, ఇది AI అసిస్టెంట్‌కు ఇచ్చే పని లేదా ప్రశ్నను సూచిస్తుంది.

    - "messages": ఇది ఒక ఆబ్జెక్టుల NSArrayను కలిగి ఉంటుంది. ప్రతి ఆబ్జెక్ట్ ఒక సంభాషణ సందేశాన్ని సూచిస్తుంది, వినియోగదారు మరియు AI అసిస్టెంట్ మధ్య జరిగే. ప్రతి సందేశ ఆబ్జెక్ట్ దగ్గర రెండు కీలు ఉంటాయి:

    - "content": సందేశం యొక్క విషయాన్ని సూచించే స్ట్రింగ్ విలువు.
    - "role": సందేశాన్ని పంపిన పాత్రను సూచించే స్ట్రింగ్ విలువ. ఇది "user" లేదా "assistant" కావచ్చు.
    - "prompt_id": ప్రత్యేక గుర్తింపుకు స్పష్టమైన స్ట్రింగ్ విలువ.

1. ఈ JSON డాక్యుమెంట్ స్పష్టంగా చూపుతోంది, ఒక సంభాషణ ఉన్నది, ఇందులో వినియోగదారు AI అసిస్టెంట్పై డిస్ట్రోపియన్ స్టోరీకి ప్రోటాగొనిస్ట్ సృష్టించమని అడుగుతుంది. అసిస్టెంట్ స్పందించి, వినియోగదారు మరిన్ని వివరాలు అడుగుతాడు. అసిస్టెంట్ అందించడానికి ఒప్పుకుంటాడు. మొత్తం సంభాషణ ఒక ప్రత్యేక ప్రాంప్ట్ id కి సంబంధించినది.

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

### డేటాను డౌన్లోడ్ చేయడం

1. ఈ Python స్క్రిప్ట్ download-dataset.py అని పేరైన హెల్పర్ స్క్రిప్ట్ ఉపయోగించి డేటాసెట్‌ను డౌన్లోడ్ చేయడానికి ఉపయోగిస్తారు. దీని వివరణ:

    - os మాడ్యూల్‌ను దిగుమతి చేస్తుంది, ఇది ఆపరేటింగ్ సిస్టమ్ ఆధారిత ఫంక్షనాలిటీకి పోర్టబుల్ మార్గాన్ని అందిస్తుంది.

    - os.system పద్ధతిని ఉపయోగించి shell లో download-dataset.py ను ఒక ప్రత్యేక కమాండ్‌లైన్ ఆర్గ్యుమెంట్లతో నడపుతుంది. ఆ ఆర్గ్యుమెంట్లలో డేటాసెట్ పేరు (HuggingFaceH4/ultrachat_200k), డౌన్లోడ్ డైరెక్టరీ (ultrachat_200k_dataset), మరియు డేటాసెట్ స్ప్లిట్ శాతం (5) ఉన్నాయి. os.system కమాండ్ యాక్సిట్ స్టేటస్‌ను exit_status లో నిల్వ చేస్తుంది.

    - exit_status 0 కాకపోతే (0 సాధారణంగా కమాండ్ విజయానికి సంకేతం), డేటాసెట్ డౌన్లోడ్ లోపం ఉన్నట్లు చూపిస్తూ Exception ను రచిస్తుంది.

    - సారాంశంగా, డేటాసెట్ డౌన్లోడ్ చేయడానికి ఒక హెల్పర్ స్క్రిప్ట్‌ను నడిపిస్తూ, తప్పు ఐతే అపवादాన్ని ఎగురవేస్తుంది.

    ```python
    # ఆపరేటింగ్ సిస్టమ్ ఆధారిత ఫంక్షనాలిటీనును ఉపయోగించే విధానాన్ని అందించే os మాడ్యూల్‌ను ఆించు
    import os
    
    # os.system ఫంక్షన్‌ను ఉపయోగించి ప్రత్యేకమైన కమాండ్-లైన్ ఆర్జ్యుమెంట్లతో డౌన్‌లోడ్-డాటాసెట్.py స్క్రిప్ట్‌ను షెల్‌లో నడపండి
    # ఆర్జ్యుమెంట్లు డౌన్‌లోడ్ చేయవలసిన డాటాసెట్‌ను (HuggingFaceH4/ultrachat_200k), దానిని డౌన్‌లోడ్ చేయవలసిన డైరెక్టరీ (ultrachat_200k_dataset), మరియు డాటాసెట్‌ను విడగొట్టాల్సిన శాతం (5) ను సూచిస్తాయి
    # os.system ఫంక్షన్ నడిపించిన కమాండ్ యొక్క ఎగ్జిట్ స్టేటస్‌ను ఇచ్చుతుంది; ఈ స్టేటస్ exit_status వేరియబుల్‌లో నిల్వ చేయబడుతూ ఉంటుంది
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # exit_status 0 కాకపోతే తనిఖీ చేయండి
    # యూనిక్స్ లాంటి ఆపరేటింగ్ సిస్టంలలో, exit status 0 అంటే సాధారణంగా ఒక కమాండ్ విజయవంతమైంది అని సూచిస్తుంది, మరెవరైనా సంఖ్య పొరపాటు అని సూచిస్తుంది
    # exit_status 0 కాకపోతే, డాటాసెట్ డౌన్‌లోడ్ లో పొరపాటు ఏర్పడిందని సూచిస్తూ Exception ను లేపు
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### డేటాన్‌ను DataFrame లో లోడ్ చేయడం

1. ఈ Python స్క్రిప్ట్ JSON Lines ఫైల్‌ను pandas DataFrame గా లోడ్ చేసి మొదటి 5 వరుసలను ప్రదర్శిస్తుంది. వివరణ:

    - pandas లైబ్రరీని దిగుమతి చేస్తుంది, ఇది శక్తివంతమైన డేటా విశ్లేషణ మరియు నిర్వహణ కోసం.

    - pandas డిస్‌ప్లే ఎంపికలలో గరిష్ట కాలమ్ వెడల్పుని 0 గా సెట్ చేస్తుంది. దీని అర్ధం ప్రతి కాలమ్ పూర్తి టెక్స్ట్‌ను కట్ చేయకుండా ప్రదర్శన చేస్తుంది.
    - ఇది pd.read_json ఫంక్షన్ ను ఉపయోగించి ultrachat_200k_dataset డైరెక్టరీలోని train_sft.jsonl ఫైల్ ను DataFrame గా లోడ్ చేస్తుంది. lines=True ఆర్గుమెంట్ సూచించడం అంటే ఫైల్ JSON లైన్స్ ఫార్మాట్‌లో ఉంది, దాదాపుగా ప్రతీ లైన్ వేరు JSON ఆబ్జెక్ట్.

    - ఇది head మెథడ్ ఉపయోగించి DataFrame యొక్క మొదటి 5 వరుసలను ప్రదర్శిస్తుంది. DataFrame లో 5 కంటే తక్కువ వరుసలు ఉంటే, అందన్నీ ప్రదర్శిస్తుంది.

    - సారాంశంగా, ఈ స్క్రిప్ట్ JSON లైన్స్ ఫైల్‌ను DataFrame లో లోడ్ చేసి, మొదటి 5 వరుసలను పూర్తి కాలమ్ టెక్స్ట్‌తో ప్రదర్శిస్తుంది.
    
    ```python
    # డేటా మానిప్యులేషన్ మరియు విశ్లేషణ కోసం శక్తివంతమైన లైబ్రరీ అయిన pandas లైబ్రరీని దిగుమతి చేసుకోండి
    import pandas as pd
    
    # pandas యొక్క ప్రదర్శన ఎంపికల కోసం గరిష్ట కాలమ్ వెడల్పును 0 గా సెట్ చేయండి
    # దీని అర్థం DataFrame ముద్రిత సమయంలో ప్రతి కాలమ్ యొక్క పూర్తి టెక్స్ట్ మినహాయింపు లేకుండా చూపించబడతుందని ఉంది
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json ఫంక్షన్ ఉపయోగించి ultrachat_200k_dataset డైరెక్టరీలోని train_sft.jsonl ఫైల్ ను DataFrame గా లోడ్ చేయండి
    # lines=True ఆర్గ్యుమెంట్ ఫైల్ JSON లైన్స్ ఫార్మాట్ లో ఉందని సూచిస్తుంది, ఇక్కడ ప్రతి లైన్ ఒక ప్రత్యేక JSON ఆబ్జెక్ట్
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # DataFrame యొక్క మొదటి 5 పంక్తులను చూపించడానికి head విధానాన్ని ఉపయోగించండి
    # DataFrame లో 5 కంటే తక్కువ పంక్తులు ఉంటే, అవన్నీ చూపిస్తాయి
    df.head()
    ```

## 5. మోడల్ మరియు డేటాను ఇన్‌పుట్‌లుగా ఉపయోగించి ఫైన్ ట్యూనింగ్ జాబ్ సమర్పించండి

chat-completion పైప్లైన్ భాగాన్ని ఉపయోగించే జాబ్‌ను సృష్టించండి. ఫైన్ ట్యూనింగ్ కోసం మద్దతు ఇస్తున్న అన్ని పారామీటర్ల గురించి మరింత తెలుసుకోండి.

### ఫైన్‌ట్యూన్ పారామీటర్ల నిర్వచనం

1. ఫైన్‌ట్యూన్ పారామీటర్లు 2 వర్గాలుగా విభజించవచ్చు - శిక్షణ పారామీటర్లు, ఆప్టిమైజేషన్ పారామీటర్లు

1. శిక్షణ పారామీటర్లు శిక్షణ అంశాలను నిర్వచిస్తాయి, ఉదా -

    - ఉపయోగించవలసిన ఆప్టిమైజర్, షెడ్యూలర్
    - ఫైన్‌ట్యూన్‌ను ఆప్టిమైజ్ చేయడానికి మెట్రిక్
    - శిక్షణ దశల సంఖ్య, బాచ్ సైజ్ మొదలైనవి
    - ఆప్టిమైజేషన్ పారామీటర్లు GPU మేమరీని ఆప్టిమైజ్ చేయడంలో మరియు కంప్యూటింగ్ వనరులను సమర్థవంతంగా ఉపయోగించడంలో సహాయపడతాయి.

1. ఈ వర్గానికి చెందిన కొన్ని పారామీటర్లు క్రింది విధంగా ఉంటాయి. ఆప్టిమైజేషన్ పారామీటర్లు ప్రతి మోడల్‌కు తేడా ఉంటాయి మరియు ఆ తేడాల్ని నిర్వహించడానికి మోడల్‌తో ప్యాకేజ్డ్‌గా ఉంటాయి.

    - deepspeed మరియు LoRA ను ఎనేబుల్ చేయండి
    - మిక్స్డ్ ప్రిసిషన్ శిక్షణను ఎనేబుల్ చేయండి
    - మల్టీ-నోడ్ శిక్షణను ఎనేబుల్ చేయండి

> [!NOTE]
> సూపర్వైజ్డ్ ఫైన్‌ట్యూనింగ్ ఆలైన్‌మెంట్ కోల్పోవడం లేదా ప్రమాదకరమైన మరవడం చేయవచ్చు. ఈ సమస్య కోసం తనిఖీ చేసి, ఫైన్‌ట్యూన్ తర్వాత ఆలైన్‌మెంట్ స్టేజ్ ను ఆడించమని మేము సిఫార్సు చేస్తున్నాము.

### ఫైన్ ట్యూనింగ్ పారామీటర్లు

1. ఈ Python స్క్రిప్ట్ ఒక మిషన్ లెర్నింగ్ మోడల్ ఫైన్ ట్యూనింగ్‌కు పారామీటర్లను సెటప్ చేస్తోంది. దీని వివరాలు ఇక్కడ ఉన్నాయి:

    - ఇది శిక్షణ ఎపోక్స్ సంఖ్య, శిక్షణ మరియు మూల్యాంకన బాచ్ సైజులు, లెర్నింగ్ రేట్, మరియు లెర్నింగ్ రేట్ షెడ్యూలర్ రకం వంటి డిఫాల్ట్ శిక్షణ పారామీటర్లను సెటప్ చేస్తుంది.

    - ఇది Layer-wise Relevance Propagation (LoRa) మరియు DeepSpeed ని వర్తింపజేయాలా, DeepSpeed దశ వంటి డిఫాల్ట్ ఆప్టిమైజేషన్ పారామీటర్లను సెటప్ చేస్తుంది.

    - శిక్షణ మరియు ఆప్టిమైజేషన్ పారామీటర్లను finetune_parameters అనే ఒక డిక్షనరీలో కలపుతుంది.

    - foundation_model కు మోడల్-స్పెసిఫిక్ డిఫాల్ట్ పారామీటర్లు ఉంటే, ఒక హెచ్చరిక సందేశాన్ని ప్రింట్ చేస్తుంది మరియు వాటిని finetune_parameters లోకి నవీకరిస్తుంది. ast.literal_eval ఫంక్షన్ స్ట్రింగ్ నుంచి Python డిక్షనరీగా మార్చడానికి ఉపయోగించబడుతుంది.

    - రన్ కోసం ఉపయోగించబోయే తుది ఫైన్ ట్యూనింగ్ పారామీటర్లను ప్రింట్ చేస్తుంది.

    - సారాంశంగా, ఈ స్క్రిప్ట్ ఫైన్ ట్యూనింగ్ కోసం పారామీటర్లను సెటప్ చేసి ప్రదర్శిస్తుంది, మరియు డిఫాల్ట్ పారామీటర్లను మోడల్-స్పెసిఫిక్ వారితో ఓవర్‌రైడ్ చేసే సామర్థ్యం కలిగి ఉంటుంది.

    ```python
    # శిక్షణ epochs సంఖ్య, శిక్షణ మరియు మూల్యాంకన బాచుల పరిమాణాలు, లెర్నింగ్ రేట్, మరియు లెర్నింగ్ రేట్ షెడ్యూలర్ రకం వంటి డిఫాల్ట్ శిక్షణ పారామితులను సెట్ చేయండి
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # లేయర్-వైజ్ రిలెవెన్స్ ప్రాపగేషన్ (LoRa) మరియు DeepSpeed ని ఉపయోగించాలా లేదా, మరియు DeepSpeed స్టేజ్ వంటి డిఫాల్ట్ ఆప్టిమైజేషన్ పారామితులను సెట్ చేయండి
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # శిక్షణ మరియు ఆప్టిమైజేషన్ పారామితులను finetune_parameters అనే ఒకే డిక్షనరీగా కలపండి
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # foundation_model కి ఏదైనా మోడల్-ప్రత్యేక డిఫాల్ట్ పారామితులు ఉన్నాయా చూడండి
    # ఉంటే, హెచ్చరిక సందేశం ప్రింట్ చేసి finetune_parameters డిక్షనరీని ఆ మోడల్-ప్రత్యేక డిఫాల్ట్స్‌తో అప్డేట్ చేయండి
    # మోడల్-ప్రత్యేక డిఫాల్ట్స్‌ని స్ట్రింగ్ నుండి పైథాన్ డిక్షనరీగా మార్చడానికి ast.literal_eval ఫంక్షన్ ఉపయోగించబడుతుంది
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # స్ట్రింగ్ ను పైథాన్ డిక్షనరీగా మార్చండి
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # రన్ కోసం ఉపయోగించబడే తుది ఫైన్-ట్యూనింగ్ పారామితుల సెట్‌ను ప్రింట్ చేయండి
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### శిక్షణ పైప్లైన్

1. ఈ Python స్క్రిప్ట్ ఒక మిషన్ లెర్నింగ్ శిక్షణ పైప్లైన్ కోసం ప్రదర్శన పేరును ఉత్పత్తి చేసే ఫంక్షన్ ను నిర్వచిస్తోంది, తర్వాత ఆ ఫంక్షన్‌ను పిలిచి ప్రదర్శన పేరును ఉత్పత్తి చేసి ముద్రిస్తోంది. దీని వివరణ క్రింది విధంగా ఉంది:

1. get_pipeline_display_name ఫంక్షన్ నిర్వచించబడింది. ఈ ఫంక్షన్ శిక్షణ పైప్లైన్‌కు సంబంధించిన వివిధ పారామీటర్ల ఆధారంగా ప్రదర్శన పేరు ఉత్పత్తి చేస్తుంది.

1. ఫంక్షన్ లోపల, మొత్తం బాచ్ సైజ్‌ను per-device బాచ్ సైజ్, గ్రేడియంట్ సేకరణ దశల సంఖ్య, ప్రతి నోడ్‌కు GPUల సంఖ్య, మరియు ఫైన్ ట్యూనింగ్ కోసం ఉపయోగించే నోడ్‌ల సంఖ్యను గుణించి లెక్కిస్తుంది.

1. ఇతర వివిధ పారామీటర్లు తీసుకుంటుంది — లెర్నింగ్ రేట్ షెడ్యూలర్ రకం, DeepSpeed వర్తింపబడుతోందా, DeepSpeed దశ, Layer-wise Relevance Propagation (LoRa) అమలవుతుందా, నిల్వకి ఉన్న మోడల్ చెక్పాయింట్లు పరిమితి, మరియు గరిష్ఠ శ్రేణి పొడవు.

1. ఈ పారామీటర్లను హైఫెన్లతో వేరుచేసి ఒక స్ట్రింగ్ రూపొందిస్తుంది. DeepSpeed లేదా LoRa అమలైతే, స్ట్రింగ్ "ds" తో DeepSpeed దశ లేదా "lora" కలిగి ఉంటుంది. లేకపోతే "nods" లేదా "nolora" ఉంటుంది.

1. ఫంక్షన్ ఆ స్ట్రింగ్‌ను తిరిగి అందిస్తుంది, ఇది శిక్షణ పైప్లైన్ యొక్క ప్రదర్శన పేరుగా ఉపయోగపడుతుంది.

1. ఫంక్షన్ నిర్వచించిన తర్వాత, దాన్ని పిలిచి ప్రదర్శన పేరును ఉత్పత్తి చేసి, ప్రింట్ చేస్తుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ వివిధ పారామీటర్ల ఆధారంగా శిక్షణ పైప్లైన్‌కు ప్రదర్శన పేరును ఉత్పత్తి చేసి ప్రింట్ చేస్తుంది.

    ```python
    # శిక్షణ పైప్‌లైన్ కోసం ప్రదర్శన పేరును ఉత్పత్తి చేసే ఫంక్షన్‌ను నిర్వచించండి
    def get_pipeline_display_name():
        # పరికరం ప్రామాణిక బ్యాచ్ సైజ్, గ్రేడియెంట్ సేకరణ దశల సంఖ్య, నోడ్‌కు GPUల సంఖ్య, ఫైన్-ట్యూనింగ్ కోసం ఉపయోగించే నోడ్ల సంఖ్యను గుణించి మొత్తం బ్యాచ్ సైజ్‌ను లెక్కించండి
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # లెర్నింగ్ రేట్ షెడ్యూలర్ రకాన్ని పొందండి
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # డీప్‌స్పీడ్ ఉపయోగిస్తున్నదా అని పొందండి
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # డీప్‌స్పీడ్ దశను పొందండి
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # డీప్‌స్పీడ్ ఉపయోగిస్తే, ప్రదర్శన పేరులో "ds" మరియు డీప్‌స్పీడ్ దశను చేర్చండి; లేకపోతే "nods" చేర్చండి
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # లేయర్-వైజ్ రిలవెన్స్ ప్రొపగేషన్ (LoRa) ఉపయోగిస్తున్నదా అని పొందండి
        lora = finetune_parameters.get("apply_lora", "false")
        # LoRa ఉపయోగిస్తే, ప్రదర్శన పేరులో "lora" చేర్చండి; లేకపోతే "nolora" చేర్చండి
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # నిలిపివేయవలసిన నమూనా చెక్పాయింట్‌ల పరిమితిని పొందండి
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # గరిష్ట సీక్వెన్స్ పొడవు పొందండి
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # హైఫన్లతో వేరు చేసిన ఈ అన్ని పారామీటర్లను సంగ్రహించి ప్రదర్శన పేరు తయారు చేయండి
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
    
    # ప్రదర్శన పేరు రూపొందించడానికి ఫంక్షన్‌ను పిలవండి
    pipeline_display_name = get_pipeline_display_name()
    # ప్రదర్శన పేరును ముద్రించండి
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### పైప్లైన్ కన్ఫిగరేషన్

ఈ Python స్క్రిప్ట్ Azure Machine Learning SDK ఉపయోగించి ఒక మిషన్ లెర్నింగ్ పైప్లైన్‌ను నిర్వచించి కన్ఫిగర్ చేస్తోంది. దీనిలో ఏమి జరుగుతుందో క్రింద ఉంది:

1. Azure AI ML SDK నుండి అవసరమైన మాడ్యూల్‌లను దిగుమతి తీసుకుంటుంది.

1. రిజిస్ట్రి నుంచి "chat_completion_pipeline" అని పేరుతో ఒక పైప్లైన్ భాగాన్ని తెస్తుంది.

1. `@pipeline` డెకొరేటర్ మరియు `create_pipeline` ఫంక్షన్ ఉపయోగించి పైప్లైన్ జాబ్ నిర్వచిస్తుంది. పైప్లైన్ పేరు `pipeline_display_name`‌గా సెట్ చేయబడింది.

1. `create_pipeline` ఫంక్షన్ లోపల, తెచ్చిన పైప్లైన్ భాగాన్ని వివిధ పారామీటర్లతో ప్రారంభిస్తుంది, ఇందులో మోడల్ పాత్, వివిధ దశల కోసం కంప్యూట్ క్లస్ట్‌ర్లు, శిక్షణ మరియు పరీక్ష datasets స్ప్లిట్లు, ఫైన్ ట్యూనింగ్ కోసం GPUల సంఖ్య మరియు ఇతర ఫైన్ ట్యూనింగ్ పారామీటర్లు ఉన్నాయి.

1. ఫైన్ ట్యూనింగ్ జాబ్ అవుట్పుట్‌ను పైప్లైన్ జాబ్ అవుట్పుట్‌కు మ్యాప్ చేస్తుంది. ఇది ఫైన్‌ట్యూన్ చేసిన మోడల్‌ను సులభంగా రిజిస్టర్ చేయడానికి అవసరం, అది ఆన్‌లైన్ లేదా బ్యాచ్ ఎండ్‌పాయింట్‌కి మోడల్‌ను పంపిణీ చేయడానికి అవసరం.

1. `create_pipeline` ఫంక్షన్ పిలవబడి పైప్లైన్ ఇన్స్టాన్సు సృష్టించబడుతుంది.

1. పైప్లైన్ యొక్క `force_rerun` సెట్టింగ్‌ను `True`గా సెట్ చేస్తుంది, అంటే పూర్వపు జాబ్స్ నుండి క్యాష్ ఫలితాలు ఉపయోగించబడవు.

1. పైప్లైన్ యొక్క `continue_on_step_failure` సెట్టింగ్‌ను `False`గా సెట్ చేస్తుంది, అంటే ఎటువంటి స్టెప్ విఫలమైతే పైప్లైన్ ఆగుతుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ Azure Machine Learning SDK ఉపయోగించి చాట్ కంప్లీషన్ టాస్క్ కోసం మిషన్ లెర్నింగ్ పైప్లైన్‌ను నిర్వచించి కన్ఫిగర్ చేస్తోంది.

    ```python
    # Azure AI ML SDK నుండి అవసరమైన మాడ్యూల్స్‌ను దిగుమతి చేయండి
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # రిజిస్ట్రిం నుండి "chat_completion_pipeline" అనే పైప్‌లైన్ భాగాన్ని తెచ్చుకోండి
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline డెకరేటర్ మరియు create_pipeline ఫంక్షన్ ఉపయోగించి పైప్‌లైన్ జాబ్‌ను నిర్వచించండి
    # పైప్‌లైన్ పేరును pipeline_display_nameగా సెట్ చేయబడింది
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # తెచ్చుకున్న పైప్‌లైన్ భాగాన్ని వివిధ పారామితులతో ఇనిషియలైజ్ చేయండి
        # ఇవి మోడల్ పథం, వివిధ దశల కోసం కంప్యూట్ క్లస్టర్లు, శిక్షణ మరియు పరీక్షలకు dataset విడివిడిగా, ఫైన్-ట్యూనింగ్ కోసం GPU ల సంఖ్య మరియు ఇతర ఫైన్-ట్యూనింగ్ పరామితులు
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # dataset విడివిడిని పారామితులకు మ్యాప్ చేయండి
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # శిక్షణ సెట్టింగులు
            number_of_gpu_to_use_finetuning=gpus_per_node,  # కంప్యూట్‌లో లభ్యమయ్యే GPU ల సంఖ్యకు సెట్ చేయండి
            **finetune_parameters
        )
        return {
            # ఫైన్ ట్యూనింగ్ జాబ్ అవుట్పుట్‌ను పైప్‌లైన్ జాబ్ అవుట్పుట్‌కు మ్యాప్ చేయండి
            # దీని వల్ల మనం సులభంగా ఫైన్ ట్యూన్ చేసిన మోడల్‌ను రిజిస్టర్ చేయవచ్చు
            # మోడల్‌ను ఆన్‌లైన్ లేదా బ్యాచ్ ఎండ్పాయింట్‌కు డిప్లాయ్ చేయడానికి మోడల్ రిజిస్టర్ చేయడం అవసరం
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline ఫంక్షన్‌ను పిలిచి పైప్‌లైన్ ఒక ప్రతిని సృష్టించండి
    pipeline_object = create_pipeline()
    
    # మునుపటి జాబ్స్ నుండి క్యాచ్డ్ ఫలితాలను ఉపయోగించవద్దు
    pipeline_object.settings.force_rerun = True
    
    # స్టెప్ విఫలం అయినా కొనసాగించకుండా False గా సెట్ చేయండి
    # అంటే ఏదైనా స్టెప్ విఫలమైతే పైప్‌లైన్ ఆగిపోతోంది
    pipeline_object.settings.continue_on_step_failure = False
    ```

### జాబ్ సమర్పణ

1. ఈ Python స్క్రిప్ట్ Azure Machine Learning వర్క్‌ఛేప్‌లో ఒక మిషన్ లెర్నింగ్ పైప్లైన్ జాబ్‌ను సమర్పించి, ఆ జాబ్ పూర్తి కావడానికి ఎదురు చూస్తోంది. దీని వివరణ ఈ విధంగా ఉంది:

    - workspace_ml_client లోని jobs ఆబ్జెక్ట్ యొక్క create_or_update మెథడ్ పిలిచి పైప్లైన్ జాబ్‌ను సమర్పిస్తుంది. అమలు చేయవలసిన పైప్లైన్ pipeline_object ద్వారా మరియు ఈ జాబ్ అమలు అయ్యే ప్రయోగం experiment_name ద్వారా సూచించబడుతుంది.

    - ఆపై workspace_ml_client లో jobs ఆబ్జెక్ట్ యొక్క stream మెథడ్ పిలిచి పైప్లైన్ జాబ్ పూర్తి కావడానికి ఎదురు చూస్తుంది. ఎదురుచూడవలసిన జాబ్ pipeline_job ఆబ్జెక్ట్ యొక్క name అట్రిబ్యూట్ ద్వారా నిర్దేశించబడుతుంది.

    - సారాంశంగా, ఈ స్క్రిప్ట్ ఒక మిషన్ లెర్నింగ్ పైప్లైన్ జాబ్‌ను Azure Machine Learning వర్క్‌ఛేప్‌కి సమర్పించి, ఆ జాబ్ పూర్తి కావడానికి ఎదురు చూస్తోంది.

    ```python
    # Azure Machine Learning వర్క్‌స్పేస్‌కు పైప్‌లైన్ ജോబ్‌ను సమర్పించండి
    # అమలు చేయాల్సిన పైప్‌లైన్ pipeline_object క్షేత్రం ద్వారా పేర్కొనబడింది
    # పని నిర్వహించబడుతున్న ప్రయోగం experiment_name ద్వారా పేర్కొనబడింది
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # పైప్‌లైన్ జాబ్ ముగిసేంతవరకు వేచి ఉండండి
    # వేచిఉండాల్సిన పని pipeline_job అబ్జెక్ట్ యొక్క పేరు లక్షణం ద్వారా పేర్కొనబడింది
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. ఫైన్‌ట్యూన్ చేసిన మోడల్‌ను వర్క్‌ఛేప్‌తో రిజిస్టర్ చేయండి

ఫైన్ ట్యూనింగ్ జాబ్ అవుట్పుట్ నుండి మేము మోడల్‌ను రిజిస్టర్ చేస్తాము. ఇది ఫైన్ ట్యూన్ చేసిన మోడల్ మరియు ఫైన్ ట్యూనింగ్ జాబ్ మధ్య లైనేజ్‌ను ట్రాక్ చేస్తుంది. ఫైన్ ట్యూనింగ్ జాబ్ మరింతగా ఫౌండేషన్ మోడల్, డేటా మరియు శిక్షణ కోడ్‌తో లైనేజ్‌ను ట్రాక్ చేస్తుంది.

### ML మోడల్ రిజిస్టర్ చేయడం

1. ఈ Python స్క్రిప్ట్ Azure Machine Learning పైప్లైన్‌లో శిక్షణ పొందిన ఒక మిషన్ లెర్నింగ్ మోడల్‌ను రిజిస్టర్ చేస్తోంది. దీని వివరం ఇక్కడ ఉంది:

    - Azure AI ML SDK నుండి అవసరమైన మాడ్యూల్‌లను దిగుమతి చేసుకుంటుంది.

    - pipeline జాబ్ నుండి trained_model అవుట్పుట్ అందుబాటులో ఉందో లేదో workspace_ml_client లో jobs ఆబ్జెక్ట్ యొక్క get మెథడ్ పిలిచి మరియు దాని outputs అట్రిబ్యూట్ ను యాక్సెస్ చేసి తనిఖీ చేస్తుంది.

    - pipeline జాబ్ పేరు మరియు అవుట్పుట్ పేరు ("trained_model") తో సరిచేసిన స్ట్రింగ్ ఉపయోగించి ట్రైండ్ మోడల్ కు పాత్ నిర్మిస్తుంది.

    - ఫైన్ ట్యూన్ చెయ్యబడిన మోడల్ కోసం పేరు నిర్వచిస్తుంది, ఇది అసలు మోడల్ పేరుకు "-ultrachat-200k" జత చేస్తుంది మరియు ఏమైనా స్లాష్‌లను హైఫెన్లతో భర్తీ చేస్తుంది.

    - మోడల్ రిజిస్టర్ చేయడానికి Model ఆబ్జెక్ట్ సృష్టించి, మోడల్ పాత్, మోడల్ రకం (MLflow మోడల్), మోడల్ పేరు మరియు వెర్షన్, మరియు మోడల్ వివరణ వంటి వివిధ పారామీటర్లతో సిద్ధం అవుతుంది.

    - workspace_ml_client లో models ఆబ్జెక్ట్ యొక్క create_or_update మెథడ్ పిలిచి Model ఆబ్జెక్ట్‌ను అందజేస్తూ మోడల్ ను రిజిస్టర్ చేస్తుంది.

    - రిజిస్టర్ అయిన మోడల్‌ను ప్రింట్ చేస్తుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ Azure Machine Learning పైప్లైన్‌లో శిక్షణ పొందిన ఒక మిషన్ లెర్నింగ్ మోడల్‌ను రిజిస్టర్ చేస్తోంది.
    
    ```python
    # Azure AI ML SDK నుండి అవసరమైన మాడ్యూల్స్ ను దిగుమతి చేసుకోండి
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # పైప్‌లైన్ జాబ్ నుండి `trained_model` అవుట్‌పుట్ అందుబాటులో ఉందా అని తనిఖీ చేయండి
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # పైప్‌లైన్ జాబ్ పేరు మరియు అవుట్‌పుట్ ("trained_model") పేరుతో స్ట్రింగ్‌ను ఫార్మాట్ చేసి ట్రైన్డ్ మోడల్ కు మార్గం నిర్మించండి
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # ఒరిజినల్ మోడల్ పేరుకు "-ultrachat-200k" జోడించి మరియు ఏవైనా స్లాష్‌లను హైఫెన్స్ తో మార్చి ఫైన్-ట్యూన్డ్ మోడల్ కు పేరు నిర్వచించండి
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # వివిధ పారామితులతో Model ఆబ్జెక్ట్ సృష్టించటం ద్వారా మోడల్‌ను నమోదుచేయడానికి సిద్దపడండి
    # ఇవి మోడల్ మార్గం, మోడల్ రకం (MLflow మోడల్), మోడల్ పేరు మరియు వెర్షన్, మోడల్ వివరణలను కలిగి ఉంటాయి
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # వెర్షన్ సంక్రమత నివారించడానికి టైమ్‌స్టాంప్ ను వెర్షన్ గా ఉపయోగించండి
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Model ఆబ్జెక్ట్‌ను ఆర్గ్యుమెంట్ గా తీసుకుని workspace_ml_client లో models ఆబ్జెక్ట్ యొక్క create_or_update పద్ధతిని పిలవడం ద్వారా మోడల్ ను నమోదు చేయండి
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # నమోదు చేయబడిన మోడల్ ను ప్రింట్ చేయండి
    print("registered model: \n", registered_model)
    ```

## 7. ఫైన్ ట్యూన్ చేసిన మోడల్‌ను ఆన్‌లైన్ ఎండ్‌పాయింట్‌లో పంపిణీ చేయండి

ఆన్‌లైన్ ఎండ్‌పాయింట్‌లు మోడల్ ఉపయోగించే అప్లికేషన్లతో సమన్వయం కోసం ఉపయోగించగల ఓ స్థిరమైన REST APIని ఇస్తాయి.

### ఎండ్‌పాయింట్ నిర్వహణ

1. ఈ Python స్క్రిప్ట్ Azure Machine Learning లో రిజిస్టర్ చేసిన మోడల్ కొరకు నిర్వహించబడే ఆన్‌లైన్ ఎండ్‌పాయింట్ సృష్టిస్తోంది. దీని వివరణ:

    - Azure AI ML SDK నుండి అవసరమైన మాడ్యూల్‌లను దిగుమతి తీసుకుంటుంది.

    - "ultrachat-completion-" స్ట్రింగ్‌కు ఒక టైమ్‌స్టాంప్ జతచేసి ఆన్‌లైన్ ఎండ్‌పాయింట్ కోసం ప్రత్యేకమైన పేరు నిర్వచిస్తుంది.

    - ManagedOnlineEndpoint ఆబ్జెక్ట్ సృష్టించి, పేరులో, వివరణలో మరియు ధృవీకరణ మోడ్ ("key") వంటి వివిధ పారామీటర్లతో ఆన్‌లైన్ ఎండ్‌పాయింట్ సృష్టించడానికి సిద్ధంగా ఉంటుంది.

    - workspace_ml_client లో begin_create_or_update మెథడ్ పిలిచి ManagedOnlineEndpoint ఆబ్జెక్ట్‌ను అందజేస్తూ ఆన్‌లైన్ ఎండ్‌పాయింట్ సృష్టిస్తుంది. ఆ ఆపరేషన్ పూర్తయ్యేవరకు wait మెథడ్ పిలుస్తూ ఎదురు చూస్తుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ Azure Machine Learning లో రిజిస్టర్ చేసిన మోడల్‌ కోసం నిర్వహించబడే ఆన్‌లైన్ ఎండ్‌పాయింట్ సృష్టిస్తోంది.

    ```python
    # ఆజ్యూర్ AI ML SDK నుండి అవసరమైన మాడ్యూల్స్‌ను దిగుమతి చేసుకోండి
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" స్ట్రింగ్‌కు టైమ్‌స్టాంప్ జోడించడం ద్వారా ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు ఒక ప్రత్యేక పేరు నిర్వచించండి
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # వివిధ పారామితులతో ManagedOnlineEndpoint ఆబ్జెక్ట్‌ని సృష్టించి ఆన్‌లైన్ ఎండ్‌పాయింట్ సృష్టించడానికి సిద్దమవ్వండి
    # వీటిలో ఎండ్‌పాయింట్ పేరు, ఎండ్‌పాయింట్ వివరణ, మరియు ప్రమాణీకరణ మోడ్ ("key") ఉన్నాయి
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint ఆబ్జెక్ట్‌ను ఆర్గ్యుమెంట్‌గా తీసుకుని workspace_ml_client యొక్క begin_create_or_update పద్ధతిని పిలిచి ఆన్‌లైన్ ఎండ్‌పాయింట్ సృష్టించండి
    # తరువాత wait పద్ధతిని పిలిచేటప్పుడు సృష్టి చర్య పూర్తవటానికి వేచి ఉండండి
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> మీరు ఇక్కడ పంపిణీకి మద్దతు ఇచ్చే SKU ల జాబితా చూడవచ్చు - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML మోడల్ పంపిణీ

1. ఈ Python స్క్రిప్ట్ ఒక రిజిస్టర్ చేసిన మిషన్ లెర్నింగ్ మోడల్‌ను Azure Machine Learningలో నిర్వహించబడే ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు పంపిణీ చేస్తోంది. దీని వివరణ:

    - Python abstract syntax grammar యొక్క ట్రీలను ప్రాసెస్ చేయడానికి ఉపయోగించే ఫంక్షన్లను అందించే ast మాడ్యూల్‌ను దిగుమతి చేస్తుంది.

    - పంపిణీకి instance type ను "Standard_NC6s_v3" గా సెట్ చేస్తుంది.

    - foundation model లో inference_compute_allow_list ట్యాగ్ ఉందో లేదో తనిఖీ చేస్తుంది. ఇది ఉంటే, ఆ ట్యాగ్ విలువను స్ట్రింగ్ నుండి Python లిస్ట్‌గా మారుస్తుంది మరియు inference_computes_allow_list కి కేటాయిస్తుంది. లేకపోతే None గా సెట్ చేస్తుంది.

    - ఇచ్చిన instance type allow list లో ఉంటుందో లేదో తనిఖీ చేస్తుంది. లేకపోతే, వినియోగదారుని allow list నుండి instance type ఎంచుకోవాలని సందేశం ముద్రిస్తుంది.

    - ManagedOnlineDeployment ఆబ్జెక్ట్ సృష్టించి, పంపిణీ పేరు, ఎండ్‌పాయింట్ పేరు, మోడల్ ID, instance type మరియు కౌంట్, లైవ్‌నెస్_probe సెట్టింగ్లు, మరియు రిక్వెస్ట్ సెట్టింగ్లు వంటి వివిధ పారామీటర్లతో పంపిణీ సృష్టించడానికి సిద్ధం అవుతుంది.

    - workspace_ml_client లో begin_create_or_update మెథడ్ పిలిచి ManagedOnlineDeployment ఆబ్జెక్ట్ తీసుకుని పంపిణీని సృష్టిస్తుంది. ఆ ఆపరేషన్ పూర్తయ్యేవరకు wait మెథడ్ ఉపయోగించి ఎదురు చూస్తుంది.

    - ఎండ్‌పాయింట్ ట్రాఫిక్‌ని "demo" పంపిణీకి 100% డైరెక్ట్ చేస్తుంది.

    - ఎండ్‌పాయింట్‌ను నవీకరించడానికి begin_create_or_update పిలుస్తుంది, ఆ ఆపరేషన్ పూర్తియే వరకు result మెథడ్ ఉపయోగించి ఎదురు చూస్తుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ Azure Machine Learningలో రిజిస్టర్ చేసిన మోడల్‌ను నిర్వహించబడే ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు పంపిణీ చేస్తోంది.

    ```python
    # Python అబ్స్ట్రాక్ట్ సింటాక్స్ గ్య్రామర్ యొక్క తణుకు నిర్మాణాలను ప్రాసెస్ చేయడానికి ఫంక్షన్లను అందించే ast మాడ్యూల్ను దిగుమతి చేయండి
    import ast
    
    # డిప్లాయ్‌మెంట్ కోసం ఇన్‌స్టాన్స్ టైప్ను సెట్ చేయండి
    instance_type = "Standard_NC6s_v3"
    
    # ఫౌండేషన్ మోడల్‌లో `inference_compute_allow_list` ట్యాగ్ ఉందో లేదో తనిఖీ చేయండి
    if "inference_compute_allow_list" in foundation_model.tags:
        # ఉంటే, ట్యాగ్ విలువను స్ట్రింగ్ నుండి Python లిస్ట్‌గా మార్చి `inference_computes_allow_list`కి కేటాయించాలి
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # లేకపోతే, `inference_computes_allow_list`ని `None`గా సెట్ చేయండి
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # నిర్దేశించిన ఇన్‌స్టాన్స్ టైప్ అనుమతినిచ్చిన జాబితాలో ఉందో లేదో తనిఖీ చేయండి
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # వివిధ పారామితులతో `ManagedOnlineDeployment` ఆబ్జెక్టును సృష్టించి డిప్లాయ్‌మెంట్ సృష్టించడానికి తయారు అవ్వండి
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `workspace_ml_client` యొక్క `begin_create_or_update` మెథడ్‌ను `ManagedOnlineDeployment` ఆబ్జెక్టుతో పిలిచి డిప్లాయ్‌మెంట్‌ను సృష్టించండి
    # తరువాత `wait` మెథడ్‌ను పిలిచి సృష్టింపు ఆపరేషన్ పూర్తయ్యే వరకు నిరీక్షించండి
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # ఎండ్‌పాయింట్ ట్రాఫిక్‌ను "demo" డిప్లాయ్‌మెంట్‌కి 100% ట్రాఫిక్‌ను పంపేందుకు సెట్ చేయండి
    endpoint.traffic = {"demo": 100}
    
    # `begin_create_or_update` మెథడ్‌ను `workspace_ml_client` తో `endpoint` ఆబ్జెక్టును Passed చేసి ఎండ్‌పాయింట్ను అప్‌డేట్ చేయండి
    # తరువాత `result` మెథడ్‌ను పిలిచి అప్‌డేట్ ఆపరేషన్ పూర్తయ్యే వరకు నిరీక్షించండి
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. నమూనా డేటాతో ఎండ్‌పాయింట్‌ను పరీక్షించండి

మేము పరీక్ష dataset నుండి కొన్ని నమూనా డేటాను తీసుకుని ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు ఇన్ఫరెన్స్ కోసం సమర్పిస్తాము. తర్వాత స్కోర్ చేసిన లేబుల్స్‌ను గ్రౌండ్ ట్రూత్ లేబుల్స్‌తో పాటు చూపిస్తాము

### ఫలితాలను చదవడం

1. ఈ Python స్క్రిప్ట్ JSON లైన్స్ ఫైల్‌ను pandas DataFrame లోకి చదివి, రాండమ్ సాంపిల్ని తీసుకుని, సూచికను రీసెట్ చేస్తోంది. దీని వివరణ:

    - ఇది ./ultrachat_200k_dataset/test_gen.jsonl ఫైల్‌ను pandas DataFrame లోకి చదవడం. read_json ఫంక్షన్ lines=True ఆర్గ్యుమెంట్‌తో ఉపయోగించబడింది ఎందుకంటే ఫైల్ JSON లైన్స్ ఫార్మాట్‌లో ఉంది, ప్రతి లైన్ వేరు JSON ఆబ్జెక్ట్.

    - DataFrame నుండి 1 వరుస రాండమ్‌గా సాంపిల్ గా తీసుకుంటుంది. sample ఫంక్షన్ n=1 ఆర్గ్యుమెంట్‌తో రాండమ్ రోస్ సంఖ్యను సూచిస్తుంది.

    - DataFrame యొక్క సూచికను రీసెట్ చేస్తుంది. reset_index ఫంక్షన్ drop=True ఆర్గ్యుమెంట్‌తో వాడి అసలైన సూచికను తొలగించి డిఫాల్ట్ ఇంటిజర్ సూచికతో భర్తీ చేస్తుంది.

    - head ఫంక్షన్ 2 తో DataFrame నుంచి మొదటి 2 వరుసలను ప్రదర్శిస్తుంది. కానీ సాంప్లింగ్ తరువాత ఒక్కటి మాత్రమే ఉన్నందున ఇది ఆ ఒక్క వరుసను మాత్రమే చూపిస్తుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ JSON లైన్స్ ఫైల్‌ను pandas DataFrame లోకి చదివి, 1 వరుస రాండమ్ సాంపిల్ తీసుకుని, సూచికను రీసెట్ చేసి మొదటి వరుసను ప్రదర్శిస్తుంది.
    
    ```python
    # pandas లైబ్రరీని దిగుమతి చేసుకోండి
    import pandas as pd
    
    # JSON లైన్స్ ఫైల్ './ultrachat_200k_dataset/test_gen.jsonl' ను pandas DataFrame లోకి చదవండి
    # 'lines=True' ఆర్గ్యుమెంట్ ఫైల్ JSON లైన్స్ ఫార్మాట్ లో ఉందని సూచిస్తుంది, ఇందులో ప్రతి లైన్ ఒక వేరు వేరు JSON ఆబ్జెక్ట్
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame నుండి 1 రౌను యాదృచ్ఛికంగా ఎంపిక చేయండి
    # 'n=1' ఆర్గ్యుమెంట్ ఎన్ని యాదృచ్ఛిక రౌలను ఎంచుకోవాలో సూచిస్తుంది
    test_df = test_df.sample(n=1)
    
    # DataFrame యొక్క సూచిక (index) ను రీసెట్ చేయండి
    # 'drop=True' ఆర్గ్యుమెంట్ الأصులు సూచిస్తుంది అసలు సూచికను తీసివేసి డిఫాల్ట్ సంపూర్ణ సంఖ్య విలువలతో కొత్త సూచికని ఉంచాలి
    # 'inplace=True' ఆర్గ్యుమెంట్ DataFrame ను నేరుగా సవరించాలనే సూచిస్తుంది (కొత్త ఆబ్జెక్ట్ సృష్టించకుండా)
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame యొక్క మొదటి 2 రౌలను ప్రదర్శించండి
    # అయితే, సాంప్లింగ్ తర్వాత DataFrameలో ఒకే ఒక్క రౌ మాత్రమే ఉండటంతో, ఇది ఆ ఒక్క రౌను మాత్రమే ప్రదర్శిస్తుంది
    test_df.head(2)
    ```

### JSON ఆబ్జెక్ట్ సృష్టించడం

1. ఈ Python స్క్రిప్ట్ నిర్దిష్ట పారామీటర్లతో JSON ఆబ్జెక్ట్‌ను సృష్టించి దానిని ఒక ఫైల్ లోకి సేవ్ చేస్తోంది. దీని వివరాలు ఇక్కడ ఉన్నాయి:

    - JSON డేటాతో పని చేయడానికి ఫంక్షన్లు అందించే json మాడ్యూల్‌ను దిగుమతి తీసుకుంటుంది.
- ఇది ఒక డిక్షనరీ parametersని సృష్టిస్తుంది, ఇది మెషీన్ లెర్నింగ్ మోడల్‌కు సంబంధించిన పరామితులను సూచించే కీలు మరియు విలువలను కలిగి ఉంటుంది. కీలు "temperature", "top_p", "do_sample", మరియు "max_new_tokens" కాగా, వాటి అనుబంధ విలువలు 0.6, 0.9, True, మరియు 200 వరుసగా ఉంటాయి.

- ఇది మరో డిక్షనరీ test_jsonని సృష్టిస్తుంది, దానిలో రెండు కీలు ఉంటాయి: "input_data" మరియు "params". "input_data" విలువ మరో డిక్షనరీ, దీనిలో "input_string" మరియు "parameters" కీలు ఉంటాయి. "input_string" విలువ test_df DataFrame నుండి మొదటి సందేశాన్ని కలిగిన లిస్ట్, "parameters" విలువ ముందుగా సృష్టించిన parameters డిక్షనరీ. "params" విలువ ఖాళీ డిక్షనరీ.

- ఇది sample_score.json అనే పేరుతో ఒక ఫైల్‌ను తెరిస్తుంది

    ```python
    # JSON డేటాతో పనిచేయడానికి ఫంక్షన్లను అందించే json మాడ్యూల్‌ను దిగుమతి చేయండి
    import json
    
    # యంత్ర అభ్యసన నమూనాకు పరామితులను సూచించే కీలు మరియు విలువలతో కూడిన `parameters` అనే డిక్షనరీని సృష్టించండి
    # కీలు "temperature", "top_p", "do_sample", మరియు "max_new_tokens" మరియు అవి వరుసగా 0.6, 0.9, True, మరియు 200 అనే విలువలతో ఉంటాయి
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # "input_data" మరియు "params" అనే రెండు కీలు ఉన్న మరో డిక్షనరీ `test_json`ని సృష్టించండి
    # "input_data" విలువు "input_string" మరియు "parameters" అనే కీలు ఉన్న మరో డిక్షనరీ
    # "input_string" విలువు `test_df` DataFrame నుండి మొదటి సందేశాన్ని కలిగిన జాబితా
    # "parameters" విలువు ముందుగా సృష్టించిన `parameters` డిక్షనరీ
    # "params" విలువు ఖాళీ డిక్షనరీ
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` డైరెక్టరీలోని `sample_score.json` అనే ఫైల్‌ను రాయడానికి తెరవండి
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` ఫంక్షన్ ఉపయోగించి `test_json` డిక్షనరీని JSON ఫార్మాట్‌లో ఫైల్‌కి రాయండి
        json.dump(test_json, f)
    ```

### ఎండ్‌పాయింట్‌ను పిలవడం

1. ఈ Python స్క్రిప్ట్ Azure Machine Learningలో ఆన్‌లైన్ ఎండ్‌పాయింట్‌ను పిలిచి ఒక JSON ఫైల్‌ను స్కోర్ చేయడానికి ఉపయోగిస్తుంది. ఇది ఏమైనా పనులను ఇలా వివరిస్తుంది:

    - ఇది workspace_ml_client ఆబ్జెక్ట్‌లోని online_endpoints ప్రాపర్టీ యొక్క invoke మెతడ్‌ను పిలుస్తుంది. ఈ మెతడ్ ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు అభ్యర్థనను పంపి ప్రతిస్పందన ప్రాప్తి కోసం ఉపయోగిస్తారు.

    - ఇది ఎండ్‌పాయింట్ పేరు మరియు డిప్లాయ్‌మెంట్‌ను endpoint_name మరియు deployment_name ఆర్గ్యూమెంట్లతో పేర్కొంటుంది. ఈ సందర్భంలో, ఎండ్‌పాయింట్ పేరు online_endpoint_name వేరియబుల్‌లో నిల్వ చేయబడింది మరియు డిప్లాయ్‌మెంట్ పేరు "demo".

    - స్కోర్ చేయాల్సిన JSON ఫైల్ మార్గం request_file ఆర్గ్యూమెంట్ ద్వారా ఇవ్వబడింది. ఈ సందర్భంలో ఫైల్ పేరు ./ultrachat_200k_dataset/sample_score.json.

    - ఇది ఎండ్‌పాయింట్ నుండి వచ్చిన ప్రతిస్పందనను response వేరియబుల్‌లో నిల్వ చేస్తుంది.

    - అది అసలైన ప్రతిస్పందనను ప్రింట్ చేస్తుంది.

1. సారాంశంగా, ఈ స్క్రిప్ట్ Azure Machine Learningలో ఆన్‌లైన్ ఎండ్‌పాయింట్‌ను పిలిచి ఒక JSON ఫైల్‌ను స్కోర్ చేసి ప్రతిస్పందనని ప్రింట్ చేస్తుంది.

    ```python
    # Azure మెషీన్ లెర్నింగ్‌లో ఆన్‌లైన్ ఎండ్‌పాయింట్‌ను పిలిచి `sample_score.json` ఫైల్‌ను స్కోర్ చేయండి
    # `workspace_ml_client` ఆబ్జెక్ట్ యొక్క `online_endpoints` ప్రాపర్టీకి చెందిన `invoke` మెథడ్ ఆన్‌లైన్ ఎండ్‌పాయింట్‌కు అభ్యర్థన పంపాలనుకుంటుంది మరియు స్పందన పొందుతుంది
    # `endpoint_name` ఆర్గుమెంట్ ఎండ్‌పాయింట్ యొక్క పేరును వివరిస్తుంది, ఇది `online_endpoint_name` వేరియబుల్‌లో సొరకబడి ఉంటుంది
    # `deployment_name` ఆర్గుమెంట్ డిప్లోయ్‌మెంట్ పేరును సూచిస్తుంది, ఇది "demo"
    # `request_file` ఆర్గుమెంట్ స్కోర్ చేయవలసిన JSON ఫైల్ యొక్క మార్గాన్ని తెలిపింది, అది `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # ఎండ్‌పాయింట్ నుండి వచ్చిన కచ్చితమైన స్పందనను ముద్రించండి
    print("raw response: \n", response, "\n")
    ```

## 9. ఆన్‌లైన్ ఎండ్‌పాయింట్ ను తొలగించండి

1. ఆన్‌లైన్ ఎండ్‌పాయింట్‌ను తొలగించడం మర్చిపోకండి, లేకపోతే ఎండ్‌పాయింట్ ఉపయోగించిన గణన కోసం బిల్లింగ్ మీటరు కొనసాగుతుంది. ఈ Python కోడ్ Azure Machine Learningలో ఒక ఆన్‌లైన్ ఎండ్‌పాయింట్‌ను తొలగిస్తోంది. ఇది ఏం చేస్తుందో ఇలా చెప్పొచ్చు:

    - ఇది workspace_ml_client ఆబ్జెక్ట్‌లోని online_endpoints ప్రాపర్టీ యొక్క begin_delete మెతడ్‌ను పిలుస్తుంది. ఈ మెతడ్ ఆన్‌లైన్ ఎండ్‌పాయింట్ తొలగింపు ప్రారంభించడానికి ఉపయోగిస్తారు.

    - ఇది తొలగించవలసిన ఎండ్‌పాయింట్ పేరును name ఆర్గ్యూమెంట్ ద్వారా పేర్కొంటుంది. ఈ సందర్భంలో, ఆ ఎండ్‌పాయింట్ పేరు online_endpoint_name వేరియబుల్‌లో ఉంటుంది.

    - ఇది wait మెతడ్‌ను పిలువుతుంది, అది తొలగింపు పూర్తయ్యేవరకు వేచి ఉంటది. ఇది బ్లాకింగ్ ఆపరేషన్, అంటే తొలగింపు పూర్తయ్యే వరకు స్క్రిప్ట్ కొనసాగదు.

    - సారాంశంగా, ఈ కోడ్ Azure Machine Learningలో ఆన్‌లైన్ ఎండ్‌పాయింట్ తొలగింపును ప్రారంభించి ఆ ఆపరేషణ పూర్తి అయ్యేవరకు వేచి ఉంటుంది.

    ```python
    # Azure Machine Learning లో ఆన్‌లైన్ ఎండ్‌పాయింట్‌ను తొలగించండి
    # `workspace_ml_client` αντικ తెలుగు ఆన్‌లైన్ ఎండ్‌పాయింట్లు లక్షణం యొక్క `begin_delete` పద్ధతి ఆన్‌లైన్ ఎండ్‌పాయింట్ తొలగింపును ప్రారంభించడానికి ఉపయోగిస్తారు
    # `name` ఆర్గ్యుమెంట్ తొలగించబడాల్సిన ఎండ్‌పాయింట్ యొక్క పేరును పేర్కొంటుంది, ఇది `online_endpoint_name` వేరియబుల్‌లో నిల్వ చేస్తారు
    # తొలగింపు చర్య పూర్తయ్యే వరకు వేచిచూడడానికి `wait` పద్ధతి పిలవబడుతుంది. ఇది ఒక అడ్డుపడే చర్య, అంటే తొలగింపు పూర్తయ్యే వరకు స్క్రిప్ట్ కొనసాగకుండా ఉండదు
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ఖ్యాతిపత్రం**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము సుశ్రద్ధగా అనువాదం చేయడానికి శ్రద్ధ వహించినప్పటికీ, స్వయంచాలకం అనువాదాలలో లోపాలు లేదా తెలివితేటలు ఉండవచ్చు. అసలు పత్రం దాని సొంత భాషలో ఉన్నది అధికారిక మూలం గా భావించాలి. కీలక సమాచారాల కోసం, నిపుణుల చేతి అనువాదం సూచించబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా గందరగోళాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->