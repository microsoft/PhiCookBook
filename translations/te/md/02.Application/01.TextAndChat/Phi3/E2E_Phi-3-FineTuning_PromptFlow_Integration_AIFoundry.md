# Microsoft Foundryలో Prompt flowతో కస్టమ్ Phi-3 మోడల్స్‌ను ఫైన్‌ట్యూన్ చేయడం మరియు విలీనం చేయడం

Microsoft Tech Community నుండి "[Microsoft Foundryలో Prompt Flowతో కస్టమ్ Phi-3 మోడల్స్‌ను ఫైన్‌ట్యూన్ చేయడం మరియు విలీనం చేయడం](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" అనే గైడ్ ఆధారంగా రూపొందిన ఈ ఎండ్-టు-ఎండ్ (E2E) నమూనా, Microsoft Foundryలో Prompt flowతో కస్టమ్ Phi-3 మోడల్స్‌ను ఫైన్‌ట్యూన్ చేయడం, నిర్వహించడం మరియు విలీనం చేయడపు ప్రక్రియలను పరిచయం చేస్తుంది.
స్థానికంగా కోడ్ నడపడం జరిగిన "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" అనే E2E నమూనాతో భిన్నంగా, ఈ పాఠం పూర్తిగా Azure AI / ML స్టూడియోలో మీ మోడల్‌ను ఫైన్‌ట్యూన్ చేయడం మరియు విలీనం చేయడంపై దృష్టి సారిస్తుంది.

## అవలోకనం

ఈ E2E నమూనాలో, మీరు Phi-3 మోడల్‌ను ఫైన్‌ట్యూన్ చేయడం మరియు Microsoft Foundryలో Prompt flowతో దాన్ని విలీనం చేయడం నేర్చుకుంటారు. Azure AI / ML స్టూడియోను ఉపయోగించి, మీరు కస్టమ్ AI మోడల్స్‌ను విస్తరించడానికి మరియు వినియోగించడానికి వర్క్‌ఫ్లోను ఏర్పాటుచేస్తారు. ఈ E2E నమూనా మూడు సందర్భాల్లో విభజించబడింది:

**సందర్భం 1: Azure వనరులను సెట్ చేయడం మరియు ఫైన్‌ట్యూన్ చేయడానికి సిద్ధం కావడం**

**సందర్భం 2: Phi-3 మోడల్‌ను ఫైన్‌ట్యూన్ చేసి Azure Machine Learning Studioలో మోపడం**

**సందర్భం 3: Prompt flowతో విలీనం చేసి Microsoft Foundryలో మీ కస్టమ్ మోడల్‌తో చాట్ చేయడం**

ఈ E2E నమూనా యొక్క అవలోకనం ఇక్కడ ఉంది.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/te/00-01-architecture.198ba0f1ae6d841a.webp)

### వివరాల పట్టిక

1. **[సందర్భం 1: Azure వనరులను సెట్ చేయడం మరియు ఫైన్‌ట్యూన్ కోసం సిద్ధం కావడం](#సందర్భం-1-azure-వనరులను-సెట్-చేయడం-మరియు-ఫైన్‌ట్యూన్-కోసం-సిద్ధం-కావడం)**
    - [Azure Machine Learning వర్క్‌స్పేస్‌ను సృష్టించండి](#azure-machine-learning-వర్క్‌స్పేస్‌ను-సృష్టించండి)
    - [Azure సబ్‌స్క్రిప్షన్‌లో GPU కోటాలను అభ్యర్థించండి](#azure-సబ్‌స్క్రిప్షన్‌లో-gpu-కోటాలను-అభ్యర్థించండి)
    - [పాత్ర కేటాయింపు జత చేయండి](#పాత్ర-కేటాయింపు-జత-చేయండి)
    - [ప్రాజెక్ట్‌ను సెట్ చేయండి](#ప్రాజెక్ట్‌ను-సెట్-చేయండి)
    - [ఫైన్‌ట్యూన్ కోసం డేటాసెట్‌ను సిద్ధం చేయండి](#ఫైన్-ట్యూనింగ్-కోసం-డేటాసెట్-సిద్ధం-చేయండి)

1. **[సందర్భం 2: Phi-3 మోడల్‌ను ఫైన్‌ట్యూన్ చేసి Azure Machine Learning Studioలో మోపండి](#సన్నివేశం-2-phi-3-మోడల్‌ను-ఫైన్-ట్యూన్-చేయడం-మరియు-azure-machine-learning-studio-లో-పంపిణీ-చేయడం)**
    - [Phi-3 మోడల్‌ను ఫైన్‌ట్యూన్ చేయండి](#phi-3-మోడల్‌ను-ఫైన్-ట్యూన్-చేయండి)
    - [ఫైన్‌ట్యూన్ చేసిన Phi-3 మోడల్‌ను మోపండి](#ఫైన్-ట్యూన్-చేసిన-phi-3-మోడల్-ను-డిప్లాయ్-చేయండి)

1. **[సందర్భం 3: Prompt flowతో విలీనం చేసి Microsoft Foundryలో మీ కస్టమ్ మోడల్‌తో చాట్ చేయండి](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [కస్టమ్ Phi-3 మోడల్‌ను Prompt flowతో విలీనం చేయండి](#prompt-flow-తో-అనుకూల-phi-3-మోడల్-ను-సమ్మిళితం-చేయండి)
    - [మీ కస్టమ్ Phi-3 మోడల్‌తో చాట్ చేయండి](#మీ-కస్టమ్-phi-3-మోడల్‌తో-చాట్-చేయండి)

## సందర్భం 1: Azure వనరులను సెట్ చేయడం మరియు ఫైన్‌ట్యూన్ కోసం సిద్ధం కావడం

### Azure Machine Learning వర్క్‌స్పేస్‌ను సృష్టించండి

1. పోర్టల్ పేజీపై మీస్థానంలో ఉన్న **search bar**లో *azure machine learning* అని టైప్ చేసి అందులోని విస్తృతాల నుండి **Azure Machine Learning**ను ఎంచుకోండి.

    ![Type azure machine learning.](../../../../../../translated_images/te/01-01-type-azml.acae6c5455e67b4b.webp)

2. నావిగేషన్ మెనూనుంచి **+ Create** ఎంచుకోండి.

3. నావిగేషన్ మెనూనుంచి **New workspace** ఎంచుకోండి.

    ![Select new workspace.](../../../../../../translated_images/te/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. క్రింది పనులు చేయండి:

    - మీ Azure **Subscription**ను ఎంచుకోండి.
    - ఉపయోగించేందుకు **Resource group** ఎంచుకోండి (తొలి సారి కావాలంటే కొత్తదాన్ని సృష్టించండి).
    - **Workspace Name**ను ఎంటర్ చేయండి. ఇది ప్రత్యేకమైన విలువగా ఉండాలి.
    - మీరు ఉపయోగించదలుచుకున్న **Region**ను ఎంచుకోండి.
    - ఉపయోగించేందుకు **Storage account** ఎంచుకోండి (కావాలంటే కొత్తదాన్ని సృష్టించండి).
    - ఉపయోగించేందుకు **Key vault** ఎంచుకోండి (కావాలంటే కొత్తదాన్ని సృష్టించండి).
    - ఉపయోగించేందుకు **Application insights** ఎంచుకోండి (కావాలంటే కొత్తదాన్ని సృష్టించండి).
    - ఉపయోగించేందుకు **Container registry** ఎంచుకోండి (కావాలంటే కొత్తదాన్ని సృష్టించండి).

    ![Fill azure machine learning.](../../../../../../translated_images/te/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** పై క్లిక్ చేయండి.

6. **Create** పై క్లిక్ చేయండి.

### Azure సబ్‌స్క్రిప్షన్‌లో GPU కోటాలను అభ్యర్థించండి

ఈ పాఠంలో, మీరు GPUs ఉపయోగించి Phi-3 మోడల్‌ను ఫైన్‌ట్యూన్ చేసి మోపడం నేర్చుకుంటారు. ఫైన్‌ట్యూన్ కోసం మీరు *Standard_NC24ads_A100_v4* GPUని ఉపయోగించబోతున్నారు, దీనికి కోటా అభ్యర్థన అవసరం. మోపడానికి మీరు *Standard_NC6s_v3* GPUని ఉపయోగిస్తారు, దీనికి కూడా కోటా అభ్యర్థన అవసరం.

> [!NOTE]
>
> GPU కేటాయింపుకు మాత్రమే Pay-As-You-Go సబ్‌స్క్రిప్షన్లు (ప్రామాణిక సబ్‌స్క్రిప్షన్ రకం) అర్హత కలిగి ఉంటాయి; ప్రస్తుతం బెనిఫిట్ సబ్‌స్క్రిప్షన్లు మద్దతు లేవు.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) సందర్శించండి.

1. *Standard NCADSA100v4 Family* కోటాను అభ్యర్థించడానికి క్రింది పనులు చేయండి:

    - ఎడమ కణిపై ఉన్న ట్యాబ్ నుంచి **Quota** ఎంచుకోండి.
    - ఉపయోగించదలిచిన **Virtual machine family**ని ఎంచుకోండి. ఉదాహరణకి, *Standard_NC24ads_A100_v4* GPUతో కూడిన **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**ని ఎంచుకోండి.
    - నావిగేషన్ మెనూలోని **Request quota**ని ఎంచుకోండి.

        ![Request quota.](../../../../../../translated_images/te/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota పేజీలో మీరు ఉపయోగించదలిచిన **New cores limit**ని ఎంటర్ చేయండి. ఉదాహరణకి, 24.
    - Request quota పేజీలో **Submit**పై క్లిక్ చేసి GPU కోటాను అభ్యర్థించండి.

1. *Standard NCSv3 Family* కోటాను అభ్యర్థించడానికి క్రింది పనులు చేయండి:

    - ఎడమ కణిపై ఉన్న ట్యాబ్ నుంచి **Quota** ఎంచుకోండి.
    - ఉపయోగించదలిచిన **Virtual machine family**ని ఎంచుకోండి. ఉదాహరణకి, *Standard_NC6s_v3* GPUతో కూడిన **Standard NCSv3 Family Cluster Dedicated vCPUs**ని ఎంచుకోండి.
    - నావిగేషన్ మెనూలోని **Request quota**ని ఎంచుకోండి.
    - Request quota పేజీలో మీరు ఉపయోగించదలిచిన **New cores limit**ని ఎంటర్ చేయండి. ఉదాహరణకి, 24.
    - Request quota పేజీలో **Submit**పై క్లిక్ చేసి GPU కోటాను అభ్యర్థించండి.

### పాత్ర కేటాయింపు జత చేయండి

మీ మోడల్స్‌ను ఫైన్‌ట్యూన్ చేసి మోపడానికి, ముందుగా యూజర్ అసైన్ చేసిన మేనేజ్డ్ ఐడెంటిటీ (UAI)ను సృష్టించి దానికి సరైన అనుమతులను కేటాయిస్తారు. ఈ UAIని మోపడం సమయంలో గుర్తింపు కోసం ఉపయోగిస్తారు.

#### User Assigned Managed Identity(UAI)ని సృష్టించండి

1. పోర్టల్ పేజీ పైభాగంలోని **search bar**లో *managed identities* అని టైప్ చేసి అందులోని ఎంపికల నుంచి **Managed Identities**ని ఎంచుకోండి.

    ![Type managed identities.](../../../../../../translated_images/te/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** ఎంచుకోండి.

    ![Select create.](../../../../../../translated_images/te/03-02-select-create.92bf8989a5cd98f2.webp)

1. క్రింది పనులు చేయండి:

    - మీ Azure **Subscription**ను ఎంచుకోండి.
    - ఉపయోగించేందుకు **Resource group** ఎంచుకోండి (కావాలంటే కొత్తదాన్ని సృష్టించండి).
    - మీరు ఉపయోగించదలుచుకున్న **Region**ను ఎంచుకోండి.
    - **Name**ను ఎంటర్ చేయండి. ఇది ప్రత్యేకమైన విలువగా ఉండాలి.

    ![Select create.](../../../../../../translated_images/te/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** ఎంచుకోండి.

1. **+ Create** ఎంచుకోండి.

#### Managed Identityకు Contributor పాత్ర కేటాయింపు జత చేయండి

1. మీరు సృష్టించిన Managed Identity వనరుకు వెళ్లండి.

1. ఎడమ కణిపై ట్యాబ్ నుండి **Azure role assignments** ఎంచుకోండి.

1. నావిగేషన్ మెనూనుంచి **+Add role assignment** ఎంచుకోండి.

1. Add role assignment పేజీలో క్రింది పనులు చేయండి:
    - **Scope**ను **Resource group**గా ఎంచుకోండి.
    - మీ Azure **Subscription**ను ఎంచుకోండి.
    - ఉపయోగించేందుకు **Resource group**ను ఎంచుకోండి.
    - **Role**ను **Contributor**గా ఎంచుకోండి.

    ![Fill contributor role.](../../../../../../translated_images/te/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** ఎంచుకోండి.

#### Managed Identityకు Storage Blob Data Reader పాత్ర కేటాయింపు జత చేయండి

1. పోర్టల్ పేజీ పైభాగంలోని **search bar**లో *storage accounts* అని టైప్ చేసి అందులోని ఎంపికల నుంచి **Storage accounts**ను ఎంచుకోండి.

    ![Type storage accounts.](../../../../../../translated_images/te/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. మీరు సృష్టించిన Azure Machine Learning వర్క్‌స్పేస్‌కు సంబంధించిన స్టోరేజ్ ఖాతాను ఎంచుకోండి. ఉదాహరణకి, *finetunephistorage*.

1. Add role assignment పేజీకి నావిగేట్ చేయడానికి క్రింది పనులు చేయండి:

    - మీరు సృష్టించిన Azure Storage ఖాతాకు వెళ్లండి.
    - ఎడమ ట్యాబ్ నుండి **Access Control (IAM)** ఎంచుకోండి.
    - నావిగేషన్ మెనూ నుండి **+ Add** ఎంచుకోండి.
    - **Add role assignment** ఎంచుకోండి.

    ![Add role.](../../../../../../translated_images/te/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment పేజీలో క్రింది పనులు చేయండి:

    - Role పేజీలో, **search bar**లో *Storage Blob Data Reader* అని టైప్ చేసి అందులో నుండి **Storage Blob Data Reader**ని ఎంచుకోండి.
    - Role పేజీలో **Next** ఎంచుకోండి.
    - Members పేజీలో **Assign access to**ను **Managed identity**గా ఎంచుకోండి.
    - Members పేజీలో **+ Select members** ఎంచుకోండి.
    - Select managed identities పేజీలో మీ Azure **Subscription**ను ఎంచుకోండి.
    - Select managed identities పేజీలో **Managed identity**ను **Manage Identity**గా ఎంచుకోండి.
    - Select managed identities పేజీలో మీరు సృష్టించిన Manage Identityని ఎంచుకోండి. ఉదాహరణకి, *finetunephi-managedidentity*.
    - Select managed identities పేజీలో **Select** ఎంచుకోండి.

    ![Select managed identity.](../../../../../../translated_images/te/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** ఎంచుకోండి.

#### Managed Identityకు AcrPull పాత్ర కేటాయింపు జత చేయండి

1. పోర్టల్ పేజీ పైభాగంలోని **search bar**లో *container registries* అని టైప్ చేసి అందులోని ఎంపికల నుంచి **Container registries**ను ఎంచుకోండి.

    ![Type container registries.](../../../../../../translated_images/te/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning వర్క్‌స్పేస్‌కు సంబంధించిన కంటెయినర్ రిజిస్ట్రీని ఎంచుకోండి. ఉదాహరణకి, *finetunephicontainerregistry*

1. Add role assignment పేజీకి నావిగేట్ చేయడానికి క్రింది పనులు చేయండి:

    - ఎడమ ట్యాబ్ నుండి **Access Control (IAM)** ఎంచుకోండి.
    - నావిగేషన్ మెనూ నుండి **+ Add** ఎంచుకోండి.
    - **Add role assignment** ఎంచుకోండి.

1. Add role assignment పేజీలో క్రింది పనులు చేయండి:

    - Role పేజీలో, **search bar**లో *AcrPull* అని టైప్ చేసి అందులో నుండి **AcrPull**ని ఎంచుకోండి.
    - Role పేజీలో **Next** ఎంచుకోండి.
    - Members పేజీలో **Assign access to**ను **Managed identity**గా ఎంచుకోండి.
    - Members పేజీలో **+ Select members** ఎంచుకోండి.
    - Select managed identities పేజీలో మీ Azure **Subscription**ను ఎంచుకోండి.
    - Select managed identities పేజీలో **Managed identity**ని **Manage Identity**గా ఎంచుకోండి.
    - Select managed identities పేజీలో మీరు సృష్టించిన Manage Identityని ఎంచుకోండి. ఉదాహరణకి, *finetunephi-managedidentity*.
    - Select managed identities పేజీలో **Select** ఎంచుకోండి.
    - **Review + assign** ఎంచుకోండి.

### ప్రాజెక్ట్‌ను సెట్ చేయండి

ఫైన్‌ట్యూనింగ్‌కు కావలసిన డేటాసెట్‌లను దిగుమతి చేసుకోవడానికి, మీరు స్థానిక పరిసరాన్ని సెట్ చేయాలి.

ఈ వ్యాయామంలో, మీరు

- పనిచేయడానికి ఒక ఫోల్డర్‌ను సృష్టించండి.
- ఒక వర్చువల్ ఎన్విరాన్‌మెంట్‌ని సృష్టించండి.
- అవసరమైన ప్యాకేజీలను ఇన్స్టాల్ చేయండి.
- డేటాసెట్‌ను డౌన్‌లోడ్ చేయడానికి *download_dataset.py* ఫైల్‌ని సృష్టించండి.

#### పనిచేయడానికి ఒక ఫోల్డర్ సృష్టించండి

1. టెర్మినల్ విండో ఓపెన్ చేసి డిఫాల్ట్ మార్గంలో *finetune-phi* అనే ఫోల్డర్ సృష్టించడానికి క్రింది ఆదేశాన్ని టైప్ చేయండి.

    ```console
    mkdir finetune-phi
    ```

2. మీరు సృష్టించిన *finetune-phi* ఫోల్డర్‌లోకి వెళ్లేందుకు క్రింది ఆదేశాన్ని మీ టెర్మినల్‌లో టైప్ చేయండి.

    ```console
    cd finetune-phi
    ```

#### వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి

1. *.venv* అనే వర్చువల్ఎన్విరాన్‌మెంట్ సృష్టించేందుకు క్రింది ఆదేశాన్ని టెర్మినల్‌లో టైప్ చేయండి.
    ```console
    python -m venv .venv
    ```

2. మీ టెర్మినల్ లో క్రింది కమాండ్ టైప్ చేసి వర్చువల్ ఎన్విరాన్‌మెంట్ ప్రారంభించండి.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> ఇది పనిచేస్తే, కమాండ్ ప్రాంప్ట్ ముందు *(.venv)* కనిపించాలి.

#### అవసరమయ్యే ప్యాకేజీలను ఇన్‌స్టాల్ చేయండి

1. అవసరమయ్యే ప్యాకేజీలను ఇన్‌స్టాల్ చేయడానికి మీ టెర్మినల్ లో క్రింది కమాండ్లు టైప్ చేయండి.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` సృష్టించండి

> [!NOTE]
> సంపూర్ణ ఫోల్డర్ నిర్మాణం:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** ని ఓపెన్ చేయండి.

1. మెనూ బార్‌లోని **File** ఎంపికను ఎంచుకోండి.

1. **Open Folder** ను ఎంచుకోండి.

1. మీరు సృష్టించిన *finetune-phi* ఫోల్డర్ ను ఎంచుకోండి, ఇది *C:\Users\yourUserName\finetune-phi* లో ఉంటుంది.

    ![మీరు సృష్టించిన ఫోల్డర్‌ను ఎంచుకోండి.](../../../../../../translated_images/te/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code ఎడమ పానెల్లో రైటు-క్లిక్ చేసి **New File** ఎంచుకుని *download_dataset.py* అనే కొత్త ఫైల్ సృష్టించండి.

    ![కొత్త ఫైల్ సృష్టించండి.](../../../../../../translated_images/te/04-02-create-new-file.cf9a330a3a9cff92.webp)

### ఫైన్-ట్యూనింగ్ కోసం డేటాసెట్ సిద్ధం చేయండి

ఈ వ్యాయామంలో, మీరు *download_dataset.py* ఫైల్ ను చలావించి *ultrachat_200k* డేటాసెట్లను మీ స్థానిక వాతావరణానికి డౌన్లోడ్ చేస్తారు. ఆ డేటాసెట్లను ఉపయోగించి మీరు Azure Machine Learning లో Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేస్తారు.

ఈ వ్యాయామంలో, మీరు:

- డేటాసెట్లను డౌన్లోడ్ చేయడానికి *download_dataset.py* ఫైల్‌లో కోడ్ జోడించండి.
- డేటాసెట్లను మీ స్థానిక వాతావరణానికి డౌన్లోడ్ చేయడానికి *download_dataset.py* ఫైల్ ని రన్ చేయండి.

#### *download_dataset.py* ఉపయోగించి డేటాసెట్ డౌన్లోడ్ చేయండి

1. Visual Studio Code లో *download_dataset.py* ఫైల్ ను ఓపెన్ చేయండి.

1. క్రింది కోడ్ ను *download_dataset.py* ఫైల్ లో చేర్చండి.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # పేర్కొన్న పేరు, కాన్ఫిగరేషన్, మరియు విభజన నిష్పత్తితో డేటాసెట్‌ని లోడ్ చేయండి
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # డేటాసెట్‌ని ట్రైన్ మరియు టెస్ట్ సెట్‌లుగా విభజించండి (80% ట్రైన్, 20% టెస్ట్)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # డైరెక్టరీ లేని పక్షంలో సృష్టించండి
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # ఫైల్‌ని రైట్ మోడ్‌లో తెరవండి
        with open(filepath, 'w', encoding='utf-8') as f:
            # డేటాసెట్‌లోని ప్రతి రికార్డ్‌పై దొంగతనం చేయండి
            for record in dataset:
                # రికార్డ్ ని JSON ఆబ్జెక్టుగా డంప్ చేసి ఫైల్‌లో వ్రాయండి
                json.dump(record, f)
                # రికార్డ్‌లను వేరుచేయడానికి ఒక న్యూలైన్ అక్షరం వ్రాయండి
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ఒక ప్రత్యేక కాన్ఫిగరేషన్ మరియు విభజన నిష్పత్తితో ULTRACHAT_200k డేటాసెట్‌ని లోడ్ చేసి విభజించండి
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # విభజన నుండి ట్రైన్ మరియు టెస్ట్ డేటాసెట్‌లను వెలికి తీయండి
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ట్రైన్ డేటాసెట్‌ని JSONL ఫైలు‌గా సేవ్ చేయండి
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # టెస్ట్ డేటాసెట్‌ని వేరే JSONL ఫైల్‌గా సేవ్ చేయండి
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. స్క్రిప్ట్ ని రన్ చేసి డేటాసెట్ ని మీ స్థానిక వాతావరణానికి డౌన్లోడ్ చేయడానికి క్రింది కమాండ్ ను టెర్మినల్ లో టైప్ చేయండి.

    ```console
    python download_dataset.py
    ```

1. డేటాసెట్లు సఫలంగా మీ స్థానిక *finetune-phi/data* డైరెక్టరీ లో సేవ్ అయ్యాయా అని నిర్ధారించుకోండి.

> [!NOTE]
>
> #### డేటాసెట్ పరిమాణం మరియు ఫైన్-ట్యూనింగ్ వ్యవధి గురించి గమనిక
>
> ఈ ట్యుటోరియల్ లో, మీరు డేటాసెట్ లో 1% (`split='train[:1%]'`) మాత్రమే ఉపయోగిస్తున్నారు. ఇది డేటా పరిమాణాన్ని భారీగా తగ్గించి, అప్లోడ్ మరియు ఫైన్-ట్యూనింగ్ ప్రక్రియలను వేగవంతంగా చేస్తుంది. మీరు శిక్షణ సమయం మరియు మోడల్ పనితీరులో సరైన సమతుల్యత కోసం శాతం సర్దుబాటు చేయవచ్చు. కుదిరిన డేటాసెట్ ఉపసమితి ఫైన్-ట్యూనింగ్ కు కావలసిన సమయాన్ని తగ్గిస్తుంది, ఇది ట్యుటోరియల్ కోసం సులభతరం చేస్తుంది.

## సన్నివేశం 2: Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేయడం మరియు Azure Machine Learning Studio లో పంపిణీ చేయడం

### Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేయండి

ఈ వ్యాయామంలో, మీరు Azure Machine Learning Studio లో Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేస్తారు.

ఈ వ్యాయామంలో, మీరు:

- ఫైన్-ట్యూనింగ్ కోసం కంప్యూటర్ క్లస్టర్ సృష్టించండి.
- Azure Machine Learning Studio లో Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేయండి.

#### ఫైన్-ట్యూనింగ్ కోసం కంప్యూటర్ క్లస్టర్ ను సృష్టించండి

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ను సందర్శించండి.

1. ఎడమ వైపు టాబ్ నుండి **Compute** ఎంచుకోండి.

1. నావిగేషన్ మెనూ నుండి **Compute clusters** ఎంచుకోండి.

1. **+ New** ఎంచుకోండి.

    ![కంప్యూట్ ఎంచుకోండి.](../../../../../../translated_images/te/06-01-select-compute.a29cff290b480252.webp)

1. క్రింది పనులు చేయండి:

    - మీరు ఉపయోగించదలచుకున్న **Region** ఎంచుకోండి.
    - **Virtual machine tier** ను **Dedicated** గా ఎంచుకోండి.
    - **Virtual machine type** ను **GPU** గా ఎంచుకోండి.
    - **Virtual machine size** ఫిల్టర్ ను **Select from all options** గా ఎంచుకోండి.
    - **Virtual machine size** ని **Standard_NC24ads_A100_v4** గా ఎంచుకోండి.

    ![క్లస్టర్ సృష్టించండి.](../../../../../../translated_images/te/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** ఎంచుకోండి.

1. క్రింది పనులు చేయండి:

    - **Compute name** నమోదు చేయండి. ఇది ప్రత్యేకమైన విలువ కావాలి.
    - **Minimum number of nodes** ను **0** గా ఎంచుకోండి.
    - **Maximum number of nodes** ను **1** గా ఎంచుకోండి.
    - **Idle seconds before scale down** ను **120** గా ఎంచుకోండి.

    ![క్లస్టర్ సృష్టించండి.](../../../../../../translated_images/te/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** ఎంచుకోండి.

#### Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేయండి

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ను సందర్శించండి.

1. మీరు సృష్టించిన Azure Machine Learning వర్క్‌స్పేస్ ఎంచుకోండి.

    ![మీరు సృష్టించిన వర్క్‌స్పేస్ ఎంచుకోండి.](../../../../../../translated_images/te/06-04-select-workspace.a92934ac04f4f181.webp)

1. క్రింది పనులు చేయండి:

    - ఎడమ వైపు టాబ్ నుండి **Model catalog** ఎంచుకోండి.
    - **search bar** లో *phi-3-mini-4k* టైప్ చేసి, చెక్కడ జాబితా నుండి **Phi-3-mini-4k-instruct** ఎంచుకోండి.

    ![phi-3-mini-4k ఎంటర్ చేయండి.](../../../../../../translated_images/te/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. నావిగేషన్ మెనూ నుండి **Fine-tune** ఎంచుకోండి.

    ![ఫైన్-ట్యూన్ ఎంచుకోండి.](../../../../../../translated_images/te/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. క్రింది పనులు చేయండి:

    - **Select task type** ను **Chat completion** గా ఎంచుకోండి.
    - **+ Select data** ఎంచుకొని **Training data** అప్‌లోడ్ చేయండి.
    - Validaton data అప్‌లోడ్ రకాన్ని **Provide different validation data** గా ఎంచుకోండి.
    - **+ Select data** ఎంచుకొని **Validation data** అప్‌లోడ్ చేయండి.

    ![ఫైన్-ట్యూనింగ్ పేజీ పూర్తి చేయండి.](../../../../../../translated_images/te/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> మీరు **Advanced settings** ఎంచుకుని **learning_rate** మరియు **lr_scheduler_type** వంటి కాన్ఫిగరేషన్‌లను అనుకూలీకరించి ఫైన్-ట్యూనింగ్ ప్రక్రియను మీ అవసరాలకు తగ్గట్టు మెరుగుపరుచుకోవచ్చు.

1. **Finish** ఎంచుకోండి.

1. ఈ వ్యాయామంలో, మీరు Azure Machine Learning ఉపయోగించి విజయవంతంగా Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేయగలిగారు. గమనించవలసింది ఏమంటే ఫైన్-ట్యూనింగ్ ప్రక్రియ కొంత సమయం తీసుకోవచ్చు. ఫైన్-ట్యూనింగ్ జాబ్ నడుస్తుండగా పూర్తి అయ్యే వరకూ వేచివుండాలి. Azure Machine Learning వర్క్‌స్పేస్ ఎడమ వైపు నుండి Jobs టాబ్ లో జాబ్ స్థితిని మీరు పర్యవేక్షించవచ్చు. తదుపరి సిరీస్‌లో, మీరు ఫైన్-ట్యూన్ చేసిన మోడల్‌ను నిర్వీర్యంగా ఉంచి Prompt flow తో సమ్మిళితంచుకుంటారు.

    ![ఫైన్-ట్యూనింగ్ జాబ్ చూడండి.](../../../../../../translated_images/te/06-08-output.2bd32e59930672b1.webp)

### ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్ ను డిప్లాయ్ చేయండి

ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్‌ను Prompt flow తో సమ్మిళితం చేసేందుకు, మీరు ఆ మోడల్‌ను రియల్-టైమ్ ఇన్ఫరెన్సీకి అందుబాటులోకి తీసుకురావాలి. దీని కోసం మోడల్ రిజిస్టర్ చేయడం, ఆన్‌లైన్ ఎండ్పాయింట్ సృష్టించడం, మరియు మోడల్‌ను డిప్లాయ్ చేయడం కావాలి.

ఈ వ్యాయామంలో, మీరు:

- Azure Machine Learning వర్క్‌స్పేస్ లో ఫైన్-ట్యూన్ చేసిన మోడల్‌ను రిజిస్టర్ చేయండి.
- ఆన్‌లైన్ ఎండ్పాయింట్ సృష్టించండి.
- రిజిస్టర్ చేసిన ఫైన్-ట్యూన్ Phi-3 మోడల్‌ను డిప్లాయ్ చేయండి.

#### ఫైన్-ట్యూన్ చేసిన మోడల్‌ను రిజిస్టర్ చేయండి

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ను సందర్శించండి.

1. మీరు సృష్టించిన Azure Machine Learning వర్క్‌స్పేస్ ఎంచుకోండి.

    ![మీరు సృష్టించిన వర్క్‌స్పేస్ ఎంచుకోండి.](../../../../../../translated_images/te/06-04-select-workspace.a92934ac04f4f181.webp)

1. ఎడమ వైపు టాబ్ నుండి **Models** ఎంచుకోండి.
1. **+ Register** ఎంచుకోండి.
1. **From a job output** ఎంచుకోండి.

    ![మోడల్ రిజిస్టర్ చేయండి.](../../../../../../translated_images/te/07-01-register-model.ad1e7cc05e4b2777.webp)

1. మీరు సృష్టించిన జాబ్ ని ఎంచుకోండి.

    ![జాబ్ ఎంచుకోండి.](../../../../../../translated_images/te/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** ఎంచుకోండి.

1. **Model type** ను **MLflow** గా ఎంచుకోండి.

1. **Job output** ఎంచుకున్నదై ఉండాలి; ఇది ఆటోమేటిగ్గా ఎంచుకోబడుతుంది.

    ![ఆట్పుట్ ఎంచుకోండి.](../../../../../../translated_images/te/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** ఎంచుకోండి.

3. **Register** ఎంచుకోండి.

    ![రిజిస్టర్ ఎంచుకోండి.](../../../../../../translated_images/te/07-04-register.fd82a3b293060bc7.webp)

4. రిజిస్టర్ చేసిన మోడల్‌ను మీరు ఎడమ వైపు టాబ్ లో **Models** మెను లో చూడవచ్చు.

    ![రిజిస్టర్ చేసిన మోడల్.](../../../../../../translated_images/te/07-05-registered-model.7db9775f58dfd591.webp)

#### ఫైన్-ట్యూన్ చేసిన మోడల్‌ను డిప్లాయ్ చేయండి

1. మీరు సృష్టించిన Azure Machine Learning వర్క్‌స్పేస్‌కు వెళ్లండి.

1. ఎడమ వైపు టాబ్ నుండి **Endpoints** ఎంచుకోండి.

1. నావిగేషన్ మెన్యూ నుండి **Real-time endpoints** ఎంచుకోండి.

    ![ఎండ్పాయింట్ సృష్టించండి.](../../../../../../translated_images/te/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** ఎంచుకోండి.

1. మీరు సృష్టించిన రిజిస్టర్ చేసిన మోడల్‌ను ఎంచుకోండి.

    ![రిజిస్టర్ చేసిన మోడల్ ఎంచుకోండి.](../../../../../../translated_images/te/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** ఎంచుకోండి.

1. క్రింది పనులు చేయండి:

    - **Virtual machine** ను *Standard_NC6s_v3* గా ఎంచుకోండి.
    - మీరు ఉపయోగించదలచుకున్న **Instance count** ఎంచుకోండి. ఉదాహరణకి, *1*.
    - **Endpoint** ను **New** గా ఎంచుకుని ఎండ్పాయింట్ సృష్టించండి.
    - **Endpoint name** నమోదు చేయండి. ఇది ప్రత్యేకమైన విలువ కావాలి.
    - **Deployment name** నమోదు చేయండి. ఇది ప్రత్యేకమైన విలువ కావాలి.

    ![డిప్లాయ్ సెట్టింగ్ పూర్తి చేయండి.](../../../../../../translated_images/te/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** ఎంచుకోండి.

> [!WARNING]
> మీ ఖాతాకు అదనపు ఛార్జిలు రాకుండా ఉండేందుకు, Azure Machine Learning వర్క్‌స్పేస్‌లో సృష్టించిన ఎండ్పాయింట్ ను తుడచివేయండి.
>

#### Azure Machine Learning వర్క్‌స్పేస్ లో డిప్లాయ్ స్థితిని పరిశీలించండి

1. మీరు సృష్టించిన Azure Machine Learning వర్క్‌స్పేస్‌కు వెళ్లండి.

1. ఎడమ వైపు టాబ్ నుండి **Endpoints** ఎంచుకోండి.

1. మీరు సృష్టించిన ఎండ్పాయింట్‌ను ఎంచుకోండి.

    ![ఎండ్పాయింట్లు ఎంచుకోండి](../../../../../../translated_images/te/07-09-check-deployment.325d18cae8475ef4.webp)

1. ఈ పేజీలో, మీరు డిప్లాయ్ ప్రక్రియలో ఎండ్పాయింట్లను నిర్వహించవచ్చు.

> [!NOTE]
> డిప్లాయ్ పూర్తయిన వెంటనే, **Live traffic** ను **100%** గా సెట్ చేసినట్లుంది పడాలి. అది కాదు అంటే, **Update traffic** ఎంచుకొని ట్రాఫిక్ సెట్టింగ్స్ ను సర్దుబాటు చేయండి. ట్రాఫిక్ ను 0% గా ఉంచితే మోడల్ ను పరీక్షించడం సాధ్యం కాదు.
>
> ![ట్రాఫిక్ సెట్ చేయండి.](../../../../../../translated_images/te/07-10-set-traffic.085b847e5751ff3d.webp)
>

## సన్నివేశం 3: Prompt flow తో సమ్మిళితం చేసి Microsoft Foundry లో మీ అనుకూల మోడల్ తో చాట్ చేయండి

### Prompt flow తో అనుకూల Phi-3 మోడల్ ను సమ్మిళితం చేయండి

మీరు విజయవంతంగా ఫైన్-ట్యూన్ చేసిన మోడల్‌ను డిప్లాయ్ చేసిన తరువాత, మీరు Prompt Flow తో దీన్ని సమ్మిళితం చేసి, రియల్-టైమ్ అప్లికేషన్లలో మీ మోడల్‌ను ఉపయోగించవచ్చు, తద్వారా మీ అనుకూల Phi-3 మోడల్ తో వివిధ ఇంటరాక్టివ్ పనులు చేయవచ్చు.

ఈ వ్యాయామంలో, మీరు:

- Microsoft Foundry Hub సృష్టించండి.
- Microsoft Foundry Project సృష్టించండి.
- Prompt flow సృష్టించండి.
- ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్ కోసం అనుకూల కనెక్షన్ జోడించండి.
- మీ అనుకూల Phi-3 మోడల్ తో చాట్ కోసం Prompt flow ను సెటప్ చేయండి.

> [!NOTE]
> మీరు Azure ML Studio ను ఉపయోగించి కూడా Promptflow తో సమ్మిళితం చేయవచ్చు. అదే సమ్మిళిత ప్రక్రియ Azure ML Studio కు వర్తిస్తుంది.

#### Microsoft Foundry Hub సృష్టించండి

Project సృష్టించే ముందు Hub సృష్టించడం అవసరం. Hub ఒక Resource Group వలె పనిచేస్తుంది, ఇది Microsoft Foundry లో అనేక ప్రాజెక్టులను సవ్య మీరు నిర్వహించడానికి, ఆర్గనైజ్ చేయడానికి సహాయపడుతుంది.
1. సందర్శించండి [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. ఎడమ వైపు ట్యాబ్ నుండి **అన్ని హబ్‌లు** ను ఎంచుకోండి.

1. నావిగేషన్ మెనూలోని **+ కొత్త హబ్** ను ఎంచుకోండి.

    ![Create hub.](../../../../../../translated_images/te/08-01-create-hub.8f7dd615bb8d9834.webp)

1. క్రింది పనులను చేయండి:

    - **హబ్ పేరు** ను నమోదు చేయండి. అది ఒక ప్రత్యేకమైన విలువగా ఉండాలి.
    - మీ Azure **సబ్‌స్క్రిప్షన్** ను ఎంచుకోండి.
    - ఉపయోగించాలనుకుంటున్న **రీసోర్సు గ్రూప్** ను ఎంచుకోండి (అవసరమైతే కొత్తదాన్ని సృష్టించండి).
    - మీరు ఉపయోగించాలనుకుంటున్న **స్థానం** ను ఎంచుకోండి.
    - ఉపయోగించాల్సిన **Azure AI Services** ని **కనెక్ట్ చేయండి** (అవసరమైతే కొత్తదాన్ని సృష్టించండి).
    - **Connect Azure AI Search** ను **కనెక్షన్ స్కిప్ చేయడానికి** ఎంచుకోండి.

    ![Fill hub.](../../../../../../translated_images/te/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **తర్వాత** ను ఎంచుకోండి.

#### Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

1. మీరు సృష్టించిన హబ్‌లో, ఎడమ వైపు ట్యాబ్ నుండి **అన్ని ప్రాజెక్ట్లు** ను ఎంచుకోండి.

1. నావిగేషన్ మెనూలో **+ కొత్త ప్రాజెక్ట్** ను ఎంచుకోండి.

    ![Select new project.](../../../../../../translated_images/te/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **ప్రాజెక్ట్ పేరు** ను నమోదు చేయండి. ఇది ఒక ప్రత్యేకమైన విలువగా ఉండాలి.

    ![Create project.](../../../../../../translated_images/te/08-05-create-project.4d97f0372f03375a.webp)

1. **ఒక ప్రాజెక్ట్ సృష్టించండి** ను ఎంచుకోండి.

#### ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్ కోసం కస్టమ్ కనెక్షన్ జోడించండి

మీ కస్టమ్ Phi-3 మోడల్‌ను Prompt flow తో ఇంటిగ్రేట్ చేయడానికి, మోడల్ యొక్క ఎండ్‌పాయింట్ మరియు కీని కస్టమ్ కనెక్షన్‌లో సేవ్ చేయాలి. ఈ సెటప్ ద్వారా Prompt flowలో మీ కస్టమ్ Phi-3 మోడల్‌కు యాక్సెస్ సులభమవుతుంది.

#### ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్ యొక్క api కీ మరియు ఎండ్పాయింట్ uri సెట్ చేయండి

1. సందర్శించండి [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. మీరు సృష్టించిన Azure మెషీన్ లెర్నింగ్ వర్క్‌స్పేస్‌కు నావిగేట్ చేయండి.

1. ఎడమ వైపు ట్యాబ్ నుండి **ఎండ్‌పాయింట్లు** ను ఎంచుకోండి.

    ![Select endpoints.](../../../../../../translated_images/te/08-06-select-endpoints.aff38d453bcf9605.webp)

1. మీరు సృష్టించిన ఎండ్పాయింట్‌ను ఎంచుకోండి.

    ![Select endpoints.](../../../../../../translated_images/te/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. నావిగేషన్ మెనూలోని **Consume** ను ఎంచుకోండి.

1. మీ **REST ఎండ్‌పాయింట్** మరియు **ప్రైమరీ కీ** ను కాపీ చేసుకోండి.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/te/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### కస్టమ్ కనెక్షన్ జోడించండి

1. సందర్శించండి [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. మీరు సృష్టించిన Microsoft Foundry ప్రాజెక్ట్‌కు నావిగేట్ చేయండి.

1. మీరు సృష్టించిన ప్రాజెక్ట్‌లో, ఎడమ వైపు ట్యాబ్ నుండి **సెట్టింగ్స్** ను ఎంచుకోండి.

1. **+ కొత్త కనెక్షన్** ను ఎంచుకోండి.

    ![Select new connection.](../../../../../../translated_images/te/08-09-select-new-connection.02eb45deadc401fc.webp)

1. నావిగేషన్ మెనూలో **కస్టమ్ కీస్** ను ఎంచుకోండి.

    ![Select custom keys.](../../../../../../translated_images/te/08-10-select-custom-keys.856f6b2966460551.webp)

1. క్రింది పనులను చేయండి:

    - **+ కీ విలువ జంటలు జోడించండి** ను ఎంచుకోండి.
    - కీ పేరు కోసం **endpoint** ను నమోదు చేసి, Azure ML స్టూడియో నుంచి కాపీ చేసిన ఎండ్‌పాయింట్ విలువను value ఫీల్డ్‌లో పేస్ట్ చేయండి.
    - మళ్ళీ **+ కీ విలువ జంటలు జోడించండి** ను ఎంచుకోండి.
    - కీ పేరు కోసం **key** ను నమోదు చేసి, Azure ML స్టూడియో నుంచి కాపీ చేసిన కీని value ఫీల్డ్‌లో పేస్ట్ చేయండి.
    - కీలు జోడించిన తర్వాత, కీ బయట కనిపించకుండా **is secret** ని ఎంచుకోండి.

    ![Add connection.](../../../../../../translated_images/te/08-11-add-connection.785486badb4d2d26.webp)

1. **కనెక్షన్ జోడించండి** ను ఎంచుకోండి.

#### Prompt flow సృష్టించండి

మీరు Microsoft Foundryలో ఒక కస్టమ్ కనెక్షన్ జోడించారు. ఇప్పుడు, క్రింద ఇచ్చిన దశలనుసరిస్తూ Prompt flow ను సృష్టిద్దాం. తరువాత, మీరు ఈ Prompt flow ను కస్టమ్ కనెక్షన్‌తో కనెక్ట్ చేసి, ఫైన్-ట్యూన్ చేసిన మోడల్‌ను Prompt flow లో ఉపయోగించొచ్చు.

1. మీరు సృష్టించిన Microsoft Foundry ప్రాజెక్ట్‌కు నావిగేట్ చేయండి.

1. ఎడమ వైపు ట్యాబ్ నుండి **Prompt flow** ను ఎంచుకోండి.

1. నావిగేషన్ మెనూలో **+ సృష్టించు** ను ఎంచుకోండి.

    ![Select Promptflow.](../../../../../../translated_images/te/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. నావిగేషన్ మెనూలో **చాట్ ఫ్లో** ను ఎంచుకోండి.

    ![Select chat flow.](../../../../../../translated_images/te/08-13-select-flow-type.2ec689b22da32591.webp)

1. ఉపయోగించడానికి **ఫోల్డర్ పేరు** ను నమోదు చేయండి.

    ![Enter name.](../../../../../../translated_images/te/08-14-enter-name.ff9520fefd89f40d.webp)

2. **సృష్టించు** ను ఎంచుకోండి.

#### మీ కస్టమ్ Phi-3 మోడల్‌తో చాట్ చేయడానికి Prompt flow సెటప్ చేయండి

మీరు ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్‌ను Prompt flowలో ఇంటిగ్రేట్ చేయాలి. ప్రస్తుతం అందుబాటులో ఉన్న Prompt flow ఈ ఉద్దేశ్యానికి రూపొందించబడలేదు. అందుకనే, Prompt flow‌ని మళ్లీ డిజైన్ చేసి, కస్టమ్ మోడల్ ఇంటిగ్రేషన్‌కు అనుగుణంగా మార్చాలి.

1. Prompt flow లో, క్రింద ఇచ్చిన పనులను చేసి ప్రస్తుత ఫ్లో ని పునర్నిర్మించండి:

    - **Raw file mode** ను ఎంచుకోండి.
    - *flow.dag.yml* ఫైల్ లోని అన్ని ఉన్న కోడ్ ను తొలగించండి.
    - క్రింది కోడ్‌ను *flow.dag.yml* ఫైల్‌లో జోడించండి.

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

    - **సేవ్** ను ఎంచుకోండి.

    ![Select raw file mode.](../../../../../../translated_images/te/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Prompt flowలో మీ కస్టమ్ Phi-3 మోడల్‌ను ఉపయోగించడానికి *integrate_with_promptflow.py* ఫైల్‌కి క్రింది కోడ్ జోడించండి.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # లాగింగ్ సెట్‌అప్
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

        # "connection" అనేది కస్టమ్ కనెక్షన్ పేరు, "endpoint", "key" అనేవి కస్టమ్ కనెక్షన్‌లో కీలు
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
            
            # పూర్ణ JSON ప్రతిస్పందనను లాగ్ చేయండి
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

    ![Paste prompt flow code.](../../../../../../translated_images/te/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundryలో Prompt flowను ఉపయోగించే వివరమైన సమాచారం కోసం, మీరు ఈ లింక్‌ని చూడవచ్చు [Microsoft Foundryలో Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. మీరు మీ మోడల్‌తో చాట్ చేయడానికి **Chat input**, **Chat output** ను ఎంచుకోండి.

    ![Input Output.](../../../../../../translated_images/te/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. ఇప్పుడు మీరు మీ కస్టమ్ Phi-3 మోడల్‌తో చాట్ చేయ آماده అయ్యారు. తదుపరి వ్యాసంలో, మీరు Prompt flow ప్రారంభించడం మరియు దానితో ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్‌తో ఎలా చాట్ చేయాలో నేర్చుకుంటారు.

> [!NOTE]
>
> పునర్నిర్మించబడిన ఫ్లో ఈ క్రింది చిత్రంలాగే కనిపించాలి:
>
> ![Flow example.](../../../../../../translated_images/te/08-18-graph-example.d6457533952e690c.webp)
>

### మీ కస్టమ్ Phi-3 మోడల్‌తో చాట్ చేయండి

మీరు ఇప్పుడు ఫైన్-ట్యూన్ చేసిన మరియు Prompt flowతో ఇంటిగ్రేట్ చేసిన మీ కస్టమ్ Phi-3 మోడల్‌తో ఇంటరాక్ట్ చేయడానికి సిద్ధంగా ఉన్నారు. ఈ వ్యాసం ద్వారా మీరు Prompt flow ఉపయోగించి మీ మోడల్‌తో చాట్ సెటప్ మరియు ప్రారంభించే విధానాన్ని తెలుసుకుంటారు. ఈ దశలను అనుసరించడం ద్వారా, మీరు వివిధ పనుల మరియు సంభాషణల కోసం మీ ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్ యొక్క సామర్థ్యాలను పూర్తి స్థాయిలో ఉపయోగించగలుగుతారు.

- Prompt flow ఉపయోగించి మీ కస్టమ్ Phi-3 మోడల్‌తో చాట్ చేయండి.

#### Prompt flow ప్రారంభించండి

1. Prompt flow ప్రారంభించడానికి **Start compute sessions** ను ఎంచుకోండి.

    ![Start compute session.](../../../../../../translated_images/te/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. పరామితులను పునరుద్ధరించడానికి **Validate and parse input** ను ఎంచుకోండి.

    ![Validate input.](../../../../../../translated_images/te/09-02-validate-input.317c76ef766361e9.webp)

1. మీరు సృష్టించిన కస్టమ్ కనెక్షన్‌కు సంబంధించిన **connection** విలువను ఎంచుకోండి. ఉదాహరణకు, *connection*.

    ![Connection.](../../../../../../translated_images/te/09-03-select-connection.99bdddb4b1844023.webp)

#### మీ కస్టమ్ మోడల్‌తో చాట్ చేయండి

1. **Chat** ను ఎంచుకోండి.

    ![Select chat.](../../../../../../translated_images/te/09-04-select-chat.61936dce6612a1e6.webp)

1. ఇక్కడ ఫలితాల ఒక ఉదాహరణ ఉంది: ఇప్పుడు మీరు మీ కస్టమ్ Phi-3 మోడల్‌తో చాట్ చేయవచ్చు. ఫైన్-ట్యూనింగ్ కోసం ఉపయోగించిన డేటా ఆధారంగా ప్రశ్నలు అడగాలని సూచించబడింది.

    ![Chat with prompt flow.](../../../../../../translated_images/te/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించామని తెలియజేస్తున్నాము. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో లోపాలు లేదా తప్పిదాలు ఉండవచ్చును. మూల పత్రం దాని స్వదేశీ భాషలో ఉన్నది అధికారిక మూలం అని పరిగణించాలి. ముఖ్యమైన సమాచారానికి, నిపుణుల చేతిప్రవేశం చేసిన అనువాదాన్ని అభ్యర్థించండి. ఈ అనువాదాన్ని ఉపయోగించినందున ఉండే అవగాహన తప్పుగా అర్థం చేసుకోవడంలో లేదా غلط్ అన్వయాలలో మేము బాధ్యులు కంలో.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->