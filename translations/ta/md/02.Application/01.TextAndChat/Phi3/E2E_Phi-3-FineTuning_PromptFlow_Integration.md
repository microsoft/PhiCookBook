<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-10-11T12:02:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "ta"
}
-->
# Fine-tune மற்றும் Prompt flow உடன் தனிப்பயன் Phi-3 மாதிரிகளை ஒருங்கிணைத்தல்

இந்த முழுமையான (E2E) மாதிரி Microsoft Tech Community-இன் "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" வழிகாட்டுதலின் அடிப்படையில் உருவாக்கப்பட்டது. இது Prompt flow உடன் தனிப்பயன் Phi-3 மாதிரிகளை fine-tuning, வெளியிடுதல் மற்றும் ஒருங்கிணைத்தல் ஆகிய செயல்முறைகளை அறிமுகப்படுத்துகிறது.

## மேலோட்டம்

இந்த E2E மாதிரியில், Phi-3 மாதிரியை fine-tune செய்யவும், Prompt flow உடன் ஒருங்கிணைக்கவும் எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள். Azure Machine Learning மற்றும் Prompt flow-ஐ பயன்படுத்தி, தனிப்பயன் AI மாதிரிகளை வெளியிடவும் பயன்படுத்தவும் ஒரு வேலைப்போக்கு உருவாக்குவீர்கள். இந்த E2E மாதிரி மூன்று சூழல்களாகப் பிரிக்கப்பட்டுள்ளது:

**சூழல் 1: Azure வளங்களை அமைத்தல் மற்றும் fine-tuning க்கான தயாரிப்பு**

**சூழல் 2: Phi-3 மாதிரியை fine-tune செய்து Azure Machine Learning Studio-வில் வெளியிடுதல்**

**சூழல் 3: Prompt flow உடன் ஒருங்கிணைத்தல் மற்றும் உங்கள் தனிப்பயன் மாதிரியுடன் உரையாடுதல்**

இந்த E2E மாதிரியின் மேலோட்டம் இங்கே உள்ளது.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../imgs/02/FineTuning-PromptFlow/00-01-architecture.png)

### உள்ளடக்க அட்டவணை

1. **[சூழல் 1: Azure வளங்களை அமைத்தல் மற்றும் fine-tuning க்கான தயாரிப்பு](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace உருவாக்குதல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription-ல் GPU quotas கோருதல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [பங்கு ஒதுக்கீடு சேர்த்தல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [திட்டத்தை அமைத்தல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tuning க்கான dataset தயாரித்தல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[சூழல் 2: Phi-3 மாதிரியை fine-tune செய்து Azure Machine Learning Studio-வில் வெளியிடுதல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI அமைத்தல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 மாதிரியை fine-tune செய்தல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tuned மாதிரியை வெளியிடுதல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[சூழல் 3: Prompt flow உடன் ஒருங்கிணைத்தல் மற்றும் உங்கள் தனிப்பயன் மாதிரியுடன் உரையாடுதல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Prompt flow உடன் தனிப்பயன் Phi-3 மாதிரியை ஒருங்கிணைத்தல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [உங்கள் தனிப்பயன் மாதிரியுடன் உரையாடுதல்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## சூழல் 1: Azure வளங்களை அமைத்தல் மற்றும் fine-tuning க்கான தயாரிப்பு

### Azure Machine Learning Workspace உருவாக்குதல்

1. **search bar**-ல் *azure machine learning* என டைப் செய்து, தோன்றும் விருப்பங்களில் **Azure Machine Learning**-ஐ தேர்ந்தெடுக்கவும்.

    ![Type azure machine learning](../../../../../../imgs/02/FineTuning-PromptFlow/01-01-type-azml.png)

1. **+ Create** என்பதை navigation menu-ல் தேர்ந்தெடுக்கவும்.

1. Navigation menu-ல் **New workspace**-ஐ தேர்ந்தெடுக்கவும்.

    ![Select new workspace](../../../../../../imgs/02/FineTuning-PromptFlow/01-02-select-new-workspace.png)

1. பின்வரும் பணிகளைச் செய்யவும்:

    - உங்கள் Azure **Subscription**-ஐ தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதியது ஒன்றை உருவாக்கவும்).
    - **Workspace Name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - பயன்படுத்த விரும்பும் **Region**-ஐ தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Storage account**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதியது ஒன்றை உருவாக்கவும்).
    - பயன்படுத்த **Key vault**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதியது ஒன்றை உருவாக்கவும்).
    - பயன்படுத்த **Application insights**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதியது ஒன்றை உருவாக்கவும்).
    - பயன்படுத்த **Container registry**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதியது ஒன்றை உருவாக்கவும்).

    ![Fill AZML.](../../../../../../imgs/02/FineTuning-PromptFlow/01-03-fill-AZML.png)

1. **Review + Create** என்பதை தேர்ந்தெடுக்கவும்.

1. **Create** என்பதை தேர்ந்தெடுக்கவும்.

### Azure Subscription-ல் GPU quotas கோருதல்

இந்த E2E மாதிரியில், fine-tuning க்கான *Standard_NC24ads_A100_v4 GPU* மற்றும் deployment க்கான *Standard_E4s_v3* CPU பயன்படுத்தப்படும். GPU quota கோரிக்கையை அனுப்ப வேண்டும், ஆனால் CPU quota கோரிக்கையை அனுப்ப தேவையில்லை.

> [!NOTE]
>
> GPU ஒதுக்கீட்டுக்கு *Pay-As-You-Go* subscription-கள் மட்டுமே தகுதி வாய்ந்தவை; benefit subscription-கள் தற்போது ஆதரிக்கப்படவில்லை.
>
> Benefit subscription-களை (Visual Studio Enterprise Subscription போன்றவை) பயன்படுத்துபவர்கள் அல்லது fine-tuning மற்றும் deployment செயல்முறையை விரைவாக சோதிக்க விரும்புபவர்கள், இந்த டுடோரியல் CPU-ஐ பயன்படுத்தி குறைந்த அளவிலான dataset-ஐ fine-tune செய்ய வழிகாட்டுதலையும் வழங்குகிறது. இருப்பினும், பெரிய dataset-களுடன் GPU பயன்படுத்தும்போது fine-tuning முடிவுகள் குறிப்பிடத்தக்க அளவில் மேம்பட்டதாக இருக்கும்.

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

1. *Standard NCADSA100v4 Family* quota-ஐ கோர பின்வரும் பணிகளைச் செய்யவும்:

    - இடது பக்கத்திலுள்ள tab-ல் **Quota**-ஐ தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Virtual machine family**-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *Standard_NC24ads_A100_v4* GPU-ஐ உள்ளடக்கிய **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**-ஐ தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **Request quota**-ஐ தேர்ந்தெடுக்கவும்.

        ![Request quota.](../../../../../../imgs/02/FineTuning-PromptFlow/01-04-request-quota.png)

    - Request quota பக்கத்தில், பயன்படுத்த விரும்பும் **New cores limit**-ஐ உள்ளிடவும். உதாரணமாக, 24.
    - Request quota பக்கத்தில், GPU quota-ஐ கோர **Submit**-ஐ தேர்ந்தெடுக்கவும்.

> [!NOTE]
> உங்கள் தேவைகளுக்கு ஏற்ற GPU அல்லது CPU-ஐ தேர்ந்தெடுக்க [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) ஆவணத்தைப் பார்க்கவும்.

### பங்கு ஒதுக்கீடு சேர்த்தல்

உங்கள் மாதிரிகளை fine-tune மற்றும் deploy செய்ய, முதலில் ஒரு User Assigned Managed Identity (UAI) உருவாக்கி, அதற்கு பொருத்தமான அனுமதிகளை வழங்க வேண்டும். Deployment போது authentication க்காக இந்த UAI பயன்படுத்தப்படும்.

#### User Assigned Managed Identity(UAI) உருவாக்குதல்

1. **search bar**-ல் *managed identities* என டைப் செய்து, தோன்றும் விருப்பங்களில் **Managed Identities**-ஐ தேர்ந்தெடுக்கவும்.

    ![Type managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow/01-05-type-managed-identities.png)

1. **+ Create**-ஐ தேர்ந்தெடுக்கவும்.

    ![Select create.](../../../../../../imgs/02/FineTuning-PromptFlow/01-06-select-create.png)

1. பின்வரும் பணிகளைச் செய்யவும்:

    - உங்கள் Azure **Subscription**-ஐ தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதியது ஒன்றை உருவாக்கவும்).
    - பயன்படுத்த விரும்பும் **Region**-ஐ தேர்ந்தெடுக்கவும்.
    - **Name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.

1. **Review + create**-ஐ தேர்ந்தெடுக்கவும்.

1. **+ Create**-ஐ தேர்ந்தெடுக்கவும்.

#### Managed Identity-க்கு Contributor பங்கு ஒதுக்கீடு சேர்த்தல்

1. நீங்கள் உருவாக்கிய Managed Identity resource-க்கு செல்லவும்.

1. இடது பக்கத்திலுள்ள tab-ல் **Azure role assignments**-ஐ தேர்ந்தெடுக்கவும்.

1. Navigation menu-ல் **+Add role assignment**-ஐ தேர்ந்தெடுக்கவும்.

1. Add role assignment பக்கத்தில் பின்வரும் பணிகளைச் செய்யவும்:
    - **Scope**-ஐ **Resource group**-க்கு தேர்ந்தெடுக்கவும்.
    - உங்கள் Azure **Subscription**-ஐ தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐ தேர்ந்தெடுக்கவும்.
    - **Role**-ஐ **Contributor**-க்கு தேர்ந்தெடுக்கவும்.

    ![Fill contributor role.](../../../../../../imgs/02/FineTuning-PromptFlow/01-07-fill-contributor-role.png)

1. **Save**-ஐ தேர்ந்தெடுக்கவும்.

#### Managed Identity-க்கு Storage Blob Data Reader பங்கு ஒதுக்கீடு சேர்த்தல்

1. **search bar**-ல் *storage accounts* என டைப் செய்து, தோன்றும் விருப்பங்களில் **Storage accounts**-ஐ தேர்ந்தெடுக்கவும்.

    ![Type storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow/01-08-type-storage-accounts.png)

1. நீங்கள் உருவாக்கிய Azure Machine Learning workspace-க்கு தொடர்புடைய storage account-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephistorage*.

1. Add role assignment பக்கத்திற்குச் செல்ல பின்வரும் பணிகளைச் செய்யவும்:

    - நீங்கள் உருவாக்கிய Azure Storage account-க்கு செல்லவும்.
    - இடது பக்கத்திலுள்ள tab-ல் **Access Control (IAM)**-ஐ தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **+ Add**-ஐ தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **Add role assignment**-ஐ தேர்ந்தெடுக்கவும்.

    ![Add role.](../../../../../../imgs/02/FineTuning-PromptFlow/01-09-add-role.png)

1. Add role assignment பக்கத்தில் பின்வரும் பணிகளைச் செய்யவும்:

    - Role பக்கத்தில், **search bar**-ல் *Storage Blob Data Reader* என டைப் செய்து, தோன்றும் விருப்பங்களில் **Storage Blob Data Reader**-ஐ தேர்ந்தெடுக்கவும்.
    - Role பக்கத்தில் **Next**-ஐ தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில், **Assign access to** **Managed identity**-ஐ தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில் **+ Select members**-ஐ தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், உங்கள் Azure **Subscription**-ஐ தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், **Managed identity**-ஐ **Manage Identity**-க்கு தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், நீங்கள் உருவாக்கிய Manage Identity-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephi-managedidentity*.
    - Select managed identities பக்கத்தில் **Select**-ஐ தேர்ந்தெடுக்கவும்.

    ![Select managed identity.](../../../../../../imgs/02/FineTuning-PromptFlow/01-10-select-managed-identity.png)

1. **Review + assign**-ஐ தேர்ந்தெடுக்கவும்.

#### Managed Identity-க்கு AcrPull பங்கு ஒதுக்கீடு சேர்த்தல்

1. **search bar**-ல் *container registries* என டைப் செய்து, தோன்றும் விருப்பங்களில் **Container registries**-ஐ தேர்ந்தெடுக்கவும்.

    ![Type container registries.](../../../../../../imgs/02/FineTuning-PromptFlow/01-11-type-container-registries.png)

1. Azure Machine Learning workspace-க்கு தொடர்புடைய container registry-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephicontainerregistries*

1. Add role assignment பக்கத்திற்குச் செல்ல பின்வரும் பணிகளைச் செய்யவும்:

    - இடது பக்கத்திலுள்ள tab-ல் **Access Control (IAM)**-ஐ தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **+ Add**-ஐ தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **Add role assignment**-ஐ தேர்ந்தெடுக்கவும்.

1. Add role assignment பக்கத்தில் பின்வரும் பணிகளைச் செய்யவும்:

    - Role பக்கத்தில், **search bar**-ல் *AcrPull* என டைப் செய்து, தோன்றும் விருப்பங்களில் **AcrPull**-ஐ தேர்ந்தெடுக்கவும்.
    - Role பக்கத்தில் **Next**-ஐ தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில், **Assign access to** **Managed identity**-ஐ தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில் **+ Select members**-ஐ தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், உங்கள் Azure **Subscription**-ஐ தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், **Managed identity**-ஐ **Manage Identity**-க்கு தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், நீங்கள் உருவாக்கிய Manage Identity-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephi-managedidentity*.
    - Select managed identities பக்கத்தில் **Select**-ஐ தேர்ந்தெடுக்கவும்.
    - **Review + assign**-ஐ தேர்ந்தெடுக்கவும்.

### திட்டத்தை அமைத்தல்

இப்போது, நீங்கள் வேலை செய்ய ஒரு கோப்பகத்தை உருவாக்கி, Azure Cosmos DB-ல் சேமிக்கப்பட்ட உரையாடல் வரலாற்றைப் பயன்படுத்தி பயனர்களுடன் தொடர்பு கொள்ளும் ஒரு நிரல்தொகுப்பை உருவாக்க ஒரு மெய்நிகர் சூழலை அமைக்க வேண்டும்.

#### வேலை செய்ய ஒரு கோப்பகத்தை உருவாக்கவும்

1. ஒரு terminal window-ஐ திறந்து, *finetune-phi* என்ற பெயரில் default பாதையில் ஒரு கோப்பகத்தை உருவாக்க பின்வரும் கட்டளையை டைப் செய்யவும்.

    ```console
    mkdir finetune-phi
    ```

1. நீங்கள் உருவாக்கிய *finetune-phi* கோப்பகத்திற்கு செல்ல terminal-ல் பின்வரும் கட்டளையை டைப் செய்யவும்.

    ```console
    cd finetune-phi
    ```

#### மெய்நிகர் சூழலை உருவாக்கவும்

1. *.venv* என்ற பெயரில் மெய்நிகர் சூழலை உருவாக்க terminal-ல் பின்வரும் கட்டளையை டைப் செய்யவும்.

    ```console
    python -m venv .venv
    ```

1. மெய்நிகர் சூழலை செயல்படுத்த terminal-ல் பின்வரும் கட்டளையை டைப் செய்யவும்.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> இது வேலை செய்தால், *(.venv)* command prompt-க்கு முன் தோன்றும்.

#### தேவையான தொகுப்புகளை நிறுவவும்

1. தேவையான தொகுப்புகளை நிறுவ terminal-ல் பின்வரும் கட்டளைகளை டைப் செய்யவும்.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### திட்ட கோப்புகளை உருவாக்கவும்
இந்த பயிற்சியில், நீங்கள் எங்கள் திட்டத்திற்கான முக்கிய கோப்புகளை உருவாக்குவீர்கள். இந்த கோப்புகளில் தரவுத்தொகுப்பை பதிவிறக்க, Azure Machine Learning சூழலை அமைக்க, Phi-3 மாடலை நன்றாகத் தகுக்க, மற்றும் நன்றாகத் தகுக்கப்பட்ட மாடலை வெளியிடுவதற்கான ஸ்கிரிப்ட்கள் அடங்கும். மேலும், நன்றாகத் தகுக்கப்பட்ட சூழலை அமைக்க *conda.yml* கோப்பையும் உருவாக்குவீர்கள்.

இந்த பயிற்சியில், நீங்கள்:

- தரவுத்தொகுப்பை பதிவிறக்க *download_dataset.py* கோப்பை உருவாக்கவும்.
- Azure Machine Learning சூழலை அமைக்க *setup_ml.py* கோப்பை உருவாக்கவும்.
- *finetuning_dir* கோப்பகத்தில் *fine_tune.py* கோப்பை உருவாக்கி, தரவுத்தொகுப்பைப் பயன்படுத்தி Phi-3 மாடலை நன்றாகத் தகுக்கவும்.
- *conda.yml* கோப்பை உருவாக்கி, நன்றாகத் தகுக்கப்பட்ட சூழலை அமைக்கவும்.
- நன்றாகத் தகுக்கப்பட்ட மாடலை வெளியிட *deploy_model.py* கோப்பை உருவாக்கவும்.
- *integrate_with_promptflow.py* கோப்பை உருவாக்கி, Prompt Flow மூலம் மாடலை ஒருங்கிணைத்து இயக்கவும்.
- Prompt Flow-க்கு வேலைப்பாடுகளை அமைக்க *flow.dag.yml* கோப்பை உருவாக்கவும்.
- Azure தகவல்களை உள்ளிட *config.py* கோப்பை உருவாக்கவும்.

> [!NOTE]
>
> முழு கோப்பக அமைப்பு:
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

1. **Visual Studio Code**-ஐ திறக்கவும்.

1. மெனு பட்டியில் **File**-ஐ தேர்ந்தெடுக்கவும்.

1. **Open Folder**-ஐ தேர்ந்தெடுக்கவும்.

1. நீங்கள் உருவாக்கிய *finetune-phi* கோப்பகத்தைத் தேர்ந்தெடுக்கவும், இது *C:\Users\yourUserName\finetune-phi* இடத்தில் உள்ளது.

    ![திட்ட கோப்பகத்தைத் திறக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/01-12-open-project-folder.png)

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New File**-ஐ தேர்ந்தெடுத்து *download_dataset.py* என்ற புதிய கோப்பை உருவாக்கவும்.

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New File**-ஐ தேர்ந்தெடுத்து *setup_ml.py* என்ற புதிய கோப்பை உருவாக்கவும்.

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New File**-ஐ தேர்ந்தெடுத்து *deploy_model.py* என்ற புதிய கோப்பை உருவாக்கவும்.

    ![புதிய கோப்பை உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/01-13-create-new-file.png)

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New Folder**-ஐ தேர்ந்தெடுத்து *finetuning_dir* என்ற புதிய கோப்பகத்தை உருவாக்கவும்.

1. *finetuning_dir* கோப்பகத்தில் *fine_tune.py* என்ற புதிய கோப்பை உருவாக்கவும்.

#### *conda.yml* கோப்பை உருவாக்கி அமைக்கவும்

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New File**-ஐ தேர்ந்தெடுத்து *conda.yml* என்ற புதிய கோப்பை உருவாக்கவும்.

1. *conda.yml* கோப்பில் கீழே உள்ள குறியீட்டை சேர்த்து, Phi-3 மாடலுக்கான நன்றாகத் தகுக்கப்பட்ட சூழலை அமைக்கவும்.

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

#### *config.py* கோப்பை உருவாக்கி அமைக்கவும்

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New File**-ஐ தேர்ந்தெடுத்து *config.py* என்ற புதிய கோப்பை உருவாக்கவும்.

1. *config.py* கோப்பில் உங்கள் Azure தகவல்களைச் சேர்க்க கீழே உள்ள குறியீட்டை சேர்க்கவும்.

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

#### Azure சூழல் மாறிகளைச் சேர்க்கவும்

1. Azure Subscription ID சேர்க்க கீழே உள்ள பணிகளைச் செய்யவும்:

    - **search bar**-இல் *subscriptions* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **Subscriptions**-ஐ தேர்ந்தெடுக்கவும்.
    - நீங்கள் தற்போது பயன்படுத்தும் Azure Subscription-ஐ தேர்ந்தெடுக்கவும்.
    - உங்கள் Subscription ID-ஐ *config.py* கோப்பில் நகலெடுத்து ஒட்டவும்.

    ![Subscription ID-ஐ கண்டறியவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/01-14-find-subscriptionid.png)

1. Azure Workspace Name சேர்க்க கீழே உள்ள பணிகளைச் செய்யவும்:

    - நீங்கள் உருவாக்கிய Azure Machine Learning வளத்திற்குச் செல்லவும்.
    - உங்கள் கணக்கு பெயரை *config.py* கோப்பில் நகலெடுத்து ஒட்டவும்.

    ![Azure Machine Learning பெயரை கண்டறியவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/01-15-find-AZML-name.png)

1. Azure Resource Group Name சேர்க்க கீழே உள்ள பணிகளைச் செய்யவும்:

    - நீங்கள் உருவாக்கிய Azure Machine Learning வளத்திற்குச் செல்லவும்.
    - உங்கள் Azure Resource Group Name-ஐ *config.py* கோப்பில் நகலெடுத்து ஒட்டவும்.

    ![Resource Group Name-ஐ கண்டறியவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/01-16-find-AZML-resourcegroup.png)

2. Azure Managed Identity Name சேர்க்க கீழே உள்ள பணிகளைச் செய்யவும்:

    - நீங்கள் உருவாக்கிய Managed Identities வளத்திற்குச் செல்லவும்.
    - உங்கள் Azure Managed Identity Name-ஐ *config.py* கோப்பில் நகலெடுத்து ஒட்டவும்.

    ![Managed Identity-ஐ கண்டறியவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/01-17-find-uai.png)

### நன்றாகத் தகுக்கப்படுவதற்கான தரவுத்தொகுப்பை தயாரிக்கவும்

இந்த பயிற்சியில், *download_dataset.py* கோப்பை இயக்கி *ULTRACHAT_200k* தரவுத்தொகுப்புகளை உங்கள் உள்ளூர் சூழலுக்கு பதிவிறக்குவீர்கள். பின்னர், இந்த தரவுத்தொகுப்புகளை Azure Machine Learning-இல் Phi-3 மாடலை நன்றாகத் தகுக்க பயன்படுத்துவீர்கள்.

#### *download_dataset.py* கோப்பைப் பயன்படுத்தி உங்கள் தரவுத்தொகுப்பை பதிவிறக்கவும்

1. Visual Studio Code-இல் *download_dataset.py* கோப்பைத் திறக்கவும்.

1. *download_dataset.py* கோப்பில் கீழே உள்ள குறியீட்டைச் சேர்க்கவும்.

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
> **CPU-ஐப் பயன்படுத்தி குறைந்த தரவுத்தொகுப்புடன் நன்றாகத் தகுக்க வழிகாட்டுதல்**
>
> நீங்கள் CPU-ஐப் பயன்படுத்த விரும்பினால், இந்த அணுகுமுறை Visual Studio Enterprise Subscription போன்ற சலுகை சந்தாக்களுடன் அல்லது நன்றாகத் தகுக்க மற்றும் வெளியிடும் செயல்முறையை விரைவாகச் சோதிக்க சிறந்தது.
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')`-ஐ `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`-ஆக மாற்றவும்.
>

1. உங்கள் டெர்மினலில் கீழே உள்ள கட்டளையைத் தட்டச்சு செய்து ஸ்கிரிப்ட்டை இயக்கி, தரவுத்தொகுப்பை உங்கள் உள்ளூர் சூழலுக்கு பதிவிறக்கவும்.

    ```console
    python download_data.py
    ```

1. தரவுத்தொகுப்புகள் உங்கள் உள்ளூர் *finetune-phi/data* கோப்பகத்தில் வெற்றிகரமாக சேமிக்கப்பட்டுள்ளதா என்பதைச் சரிபார்க்கவும்.

> [!NOTE]
>
> **தரவுத்தொகுப்பு அளவு மற்றும் நன்றாகத் தகுக்க நேரம்**
>
> இந்த E2E மாதிரியில், நீங்கள் தரவுத்தொகுப்பின் 1% மட்டுமே பயன்படுத்துகிறீர்கள் (`train_sft[:1%]`). இது தரவின் அளவைக் குறிப்பிடத்தக்க அளவில் குறைக்கிறது, பதிவேற்றம் மற்றும் நன்றாகத் தகுக்க செயல்முறைகளை வேகமாகச் செய்கிறது. பயிற்சி நேரம் மற்றும் மாடல் செயல்திறனுக்கு இடையில் சரியான சமநிலையை கண்டறிய நீங்கள் சதவீதத்தை சரிசெய்யலாம். குறைந்த தரவுத்தொகுப்பைப் பயன்படுத்துவது நன்றாகத் தகுக்க தேவையான நேரத்தை குறைக்கிறது, இது E2E மாதிரிக்கான செயல்முறையை மேலாண்மை செய்யக்கூடியதாக மாற்றுகிறது.

## சூழல் 2: Phi-3 மாடலை நன்றாகத் தகுக்கவும் மற்றும் Azure Machine Learning Studio-வில் வெளியிடவும்

### Azure CLI-ஐ அமைக்கவும்

உங்கள் சூழலை அங்கீகரிக்க Azure CLI-ஐ அமைக்க வேண்டும். Azure CLI உங்களுக்கு Azure வளங்களை நேரடியாக கட்டளைகள் மூலம் நிர்வகிக்க அனுமதிக்கிறது மற்றும் Azure Machine Learning-க்கு இந்த வளங்களை அணுக தேவையான சான்றுகளை வழங்குகிறது. [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) நிறுவுவதற்கான வழிகாட்டுதலைப் பெற.

1. ஒரு டெர்மினல் சாளரத்தைத் திறந்து, உங்கள் Azure கணக்கில் உள்நுழைய கீழே உள்ள கட்டளையைத் தட்டச்சு செய்யவும்.

    ```console
    az login
    ```

1. நீங்கள் பயன்படுத்த விரும்பும் Azure கணக்கைத் தேர்ந்தெடுக்கவும்.

1. நீங்கள் பயன்படுத்த விரும்பும் Azure Subscription-ஐத் தேர்ந்தெடுக்கவும்.

    ![Resource Group Name-ஐ கண்டறியவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/02-01-login-using-azure-cli.png)

> [!TIP]
>
> Azure-இல் உள்நுழைய சிக்கல் இருந்தால், ஒரு சாதன குறியீட்டை பயன்படுத்த முயற்சிக்கவும். ஒரு டெர்மினல் சாளரத்தைத் திறந்து, உங்கள் Azure கணக்கில் உள்நுழைய கீழே உள்ள கட்டளையைத் தட்டச்சு செய்யவும்:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 மாடலை நன்றாகத் தகுக்கவும்

இந்த பயிற்சியில், நீங்கள் வழங்கப்பட்ட தரவுத்தொகுப்பைப் பயன்படுத்தி Phi-3 மாடலை நன்றாகத் தகுக்குவீர்கள். முதலில், *fine_tune.py* கோப்பில் நன்றாகத் தகுக்க செயல்முறையை வரையறுக்கவும். பின்னர், Azure Machine Learning சூழலை அமைத்து, *setup_ml.py* கோப்பை இயக்குவதன் மூலம் நன்றாகத் தகுக்க செயல்முறையைத் தொடங்கவும். இந்த ஸ்கிரிப்ட் Azure Machine Learning சூழலில் நன்றாகத் தகுக்க செயல்முறையை உறுதிசெய்கிறது.

*setup_ml.py* கோப்பை இயக்குவதன் மூலம், Azure Machine Learning சூழலில் நன்றாகத் தகுக்க செயல்முறையை இயக்குவீர்கள்.

#### *fine_tune.py* கோப்பில் குறியீட்டைச் சேர்க்கவும்

1. *finetuning_dir* கோப்பகத்திற்குச் செல்லவும், *fine_tune.py* கோப்பை Visual Studio Code-இல் திறக்கவும்.

1. *fine_tune.py* கோப்பில் கீழே உள்ள குறியீட்டைச் சேர்க்கவும்.

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

1. *fine_tune.py* கோப்பைச் சேமித்து மூடவும்.

> [!TIP]
> **Phi-3.5 மாடலை நன்றாகத் தகுக்கலாம்**
>
> *fine_tune.py* கோப்பில், `pretrained_model_name`-ஐ `"microsoft/Phi-3-mini-4k-instruct"`-இல் இருந்து `"microsoft/Phi-3.5-mini-instruct"`-ஆக மாற்றலாம். இதனால், நீங்கள் Phi-3.5-mini-instruct மாடலை நன்றாகத் தகுக்க பயன்படுத்துவீர்கள். உங்கள் விருப்பமான மாடல் பெயரை கண்டறிந்து பயன்படுத்த [Hugging Face](https://huggingface.co/) இணையதளத்திற்குச் செல்லவும், உங்கள் விருப்பமான மாடலைத் தேடவும், அதன் பெயரை நகலெடுத்து `pretrained_model_name` புலத்தில் ஒட்டவும்.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 மாடலை நன்றாகத் தகுக்கவும்.":::
>

#### *setup_ml.py* கோப்பில் குறியீட்டைச் சேர்க்கவும்

1. *setup_ml.py* கோப்பை Visual Studio Code-இல் திறக்கவும்.

1. *setup_ml.py* கோப்பில் கீழே உள்ள குறியீட்டைச் சேர்க்கவும்.

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

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, மற்றும் `LOCATION` ஆகியவற்றை உங்கள் குறிப்பிட்ட விவரங்களுடன் மாற்றவும்.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **CPU-ஐப் பயன்படுத்தி குறைந்த தரவுத்தொகுப்புடன் நன்றாகத் தகுக்க வழிகாட்டுதல்**
>
> நீங்கள் CPU-ஐப் பயன்படுத்த விரும்பினால், இந்த அணுகுமுறை Visual Studio Enterprise Subscription போன்ற சலுகை சந்தாக்களுடன் அல்லது நன்றாகத் தகுக்க மற்றும் வெளியிடும் செயல்முறையை விரைவாகச் சோதிக்க சிறந்தது.
>
> 1. *setup_ml* கோப்பைத் திறக்கவும்.
> 1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, மற்றும் `DOCKER_IMAGE_NAME` ஆகியவற்றை கீழே உள்ளவாறு மாற்றவும். *Standard_E16s_v3*-க்கு அணுகல் இல்லையெனில், சமமான CPU instance-ஐப் பயன்படுத்தலாம் அல்லது புதிய quota-ஐ கோரலாம்.
> 1. `LOCATION`-ஐ உங்கள் குறிப்பிட்ட விவரங்களுடன் மாற்றவும்.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. *setup_ml.py* ஸ்கிரிப்ட்டை இயக்கி Azure Machine Learning-இல் நன்றாகத் தகுக்க செயல்முறையைத் தொடங்க கீழே உள்ள கட்டளையைத் தட்டச்சு செய்யவும்.

    ```python
    python setup_ml.py
    ```

1. இந்த பயிற்சியில், நீங்கள் Azure Machine Learning-ஐப் பயன்படுத்தி Phi-3 மாடலை நன்றாகத் தகுக்க வெற்றிகரமாக முடித்தீர்கள். *setup_ml.py* ஸ்கிரிப்ட்டை இயக்குவதன் மூலம், Azure Machine Learning சூழலை அமைத்து, *fine_tune.py* கோப்பில் வரையறுக்கப்பட்ட நன்றாகத் தகுக்க செயல்முறையைத் தொடங்கியுள்ளீர்கள். தயவுசெய்து கவனிக்கவும், நன்றாகத் தகுக்க செயல்முறை குறிப்பிடத்தக்க நேரத்தை எடுத்துக்கொள்ளலாம். `python setup_ml.py` கட்டளையை இயக்கிய பிறகு, செயல்முறை முடிவடையும் வரை காத்திருக்க வேண்டும். டெர்மினலில் வழங்கப்பட்ட Azure Machine Learning போர்ட்டலுக்கான இணைப்பைப் பின்பற்றுவதன் மூலம், நன்றாகத் தகுக்க வேலைக்கான நிலையை கண்காணிக்கலாம்.

    ![நன்றாகத் தகுக்க வேலைக்கான நிலையைப் பார்க்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/02-02-see-finetuning-job.png)

### நன்றாகத் தகுக்கப்பட்ட மாடலை வெளியிடவும்

Prompt Flow-இன் மூலம் நன்றாகத் தகுக்கப்பட்ட Phi-3 மாடலை ஒருங்கிணைக்க, மாடலை நேரடி முன்னறிவிப்பு பயன்பாட்டிற்கு அணுகக்கூடியதாக மாற்ற வெளியிட வேண்டும். இந்த செயல்முறை மாடலை பதிவு செய்வது, ஆன்லைன் இறுதிப்புள்ளியை உருவாக்குவது, மற்றும் மாடலை வெளியிடுவது ஆகியவற்றை உள்ளடக்கியது.

#### வெளியிட மாடல் பெயர், இறுதிப்புள்ளி பெயர், மற்றும் வெளியீட்டு பெயரை அமைக்கவும்

1. *config.py* கோப்பைத் திறக்கவும்.

1. `AZURE_MODEL_NAME = "your_fine_tuned_model_name"`-ஐ உங்கள் மாடலுக்கான விருப்பமான பெயருடன் மாற்றவும்.

1. `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"`-ஐ உங்கள் இறுதிப்புள்ளிக்கான விருப்பமான பெயருடன் மாற்றவும்.

1. `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"`-ஐ உங்கள் வெளியீட்டுக்கான விருப்பமான பெயருடன் மாற்றவும்.

#### *deploy_model.py* கோப்பில் குறியீட்டைச் சேர்க்கவும்

*deploy_model.py* கோப்பை இயக்குவது முழு வெளியீட்டு செயல்முறையை தானியங்கமாக்குகிறது. இது மாடலை பதிவு செய்கிறது, இறுதிப்புள்ளியை உருவாக்குகிறது, மற்றும் *config.py* கோப்பில் குறிப்பிடப்பட்ட அமைப்புகளின் அடிப்படையில் வெளியீட்டைச் செய்கிறது, இதில் மாடல் பெயர், இறுதிப்புள்ளி பெயர், மற்றும் வெளியீட்டு பெயர் அடங்கும்.

1. *deploy_model.py* கோப்பை Visual Studio Code-இல் திறக்கவும்.

1. *deploy_model.py* கோப்பில் கீழே உள்ள குறியீட்டைச் சேர்க்கவும்.

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

1. `JOB_NAME`-ஐ பெற கீழே உள்ள பணிகளைச் செய்யவும்:

    - நீங்கள் உருவாக்கிய Azure Machine Learning வளத்திற்குச் செல்லவும்.
    - **Studio web URL**-ஐத் தேர்ந்தெடுத்து Azure Machine Learning வேலைப்பகுதியைத் திறக்கவும்.
    - இடது பக்கத்திலுள்ள **Jobs**-ஐத் தேர்ந்தெடுக்கவும்.
    - நன்றாகத் தகுக்க முயற்சிக்கான பரிசோதனையைத் தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephi*.
    - நீங்கள் உருவாக்கிய வேலைப்பாட்டைத் தேர்ந்தெடுக்கவும்.
- உங்கள் வேலை பெயரை `JOB_NAME = "your-job-name"` என *deploy_model.py* கோப்பில் நகலெடுத்து ஒட்டவும்.

1. `COMPUTE_INSTANCE_TYPE` ஐ உங்கள் குறிப்பிட்ட விவரங்களுடன் மாற்றவும்.

1. *deploy_model.py* ஸ்கிரிப்டை இயக்கி Azure Machine Learning-ல் பிரசார செயல்முறையை தொடங்க கீழே உள்ள கட்டளையை தட்டச்சு செய்யவும்.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> உங்கள் கணக்கில் கூடுதல் கட்டணங்களை தவிர்க்க, Azure Machine Learning வேலைப்பிடத்தில் உருவாக்கப்பட்ட endpoint ஐ நீக்க உறுதிப்படுத்தவும்.
>

#### Azure Machine Learning Workspace-ல் பிரசார நிலையை சரிபார்க்கவும்

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

1. நீங்கள் உருவாக்கிய Azure Machine Learning வேலைப்பிடத்திற்கு செல்லவும்.

1. **Studio web URL** ஐ தேர்வு செய்து Azure Machine Learning வேலைப்பிடத்தை திறக்கவும்.

1. இடது பக்க தாவலில் இருந்து **Endpoints** ஐ தேர்வு செய்யவும்.

    ![Endpoints ஐ தேர்வு செய்யவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/02-03-select-endpoints.png)

2. நீங்கள் உருவாக்கிய endpoint ஐ தேர்வு செய்யவும்.

    ![நீங்கள் உருவாக்கிய endpoint ஐ தேர்வு செய்யவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/02-04-select-endpoint-created.png)

3. இந்த பக்கத்தில், பிரசார செயல்முறையின் போது உருவாக்கப்பட்ட endpoint-களை நிர்வகிக்கலாம்.

## சூழல் 3: Prompt flow உடன் ஒருங்கிணைத்து உங்கள் தனிப்பயன் மாடலுடன் உரையாடவும்

### Prompt flow உடன் தனிப்பயன் Phi-3 மாடலை ஒருங்கிணைக்கவும்

உங்கள் fine-tuned மாடலை வெற்றிகரமாக பிரசாரம் செய்த பிறகு, Prompt flow உடன் அதை ஒருங்கிணைத்து உங்கள் மாடலை நேரடி பயன்பாடுகளில் பயன்படுத்தலாம், இது உங்கள் தனிப்பயன் Phi-3 மாடலுடன் பல்வேறு தொடர்பு பணிகளை செயல்படுத்த உதவுகிறது.

#### Fine-tuned Phi-3 மாடலின் api key மற்றும் endpoint uri அமைக்கவும்

1. நீங்கள் உருவாக்கிய Azure Machine Learning வேலைப்பிடத்திற்கு செல்லவும்.
1. இடது பக்க தாவலில் இருந்து **Endpoints** ஐ தேர்வு செய்யவும்.
1. நீங்கள் உருவாக்கிய endpoint ஐ தேர்வு செய்யவும்.
1. வழிசெலுத்தல் மெனுவில் இருந்து **Consume** ஐ தேர்வு செய்யவும்.
1. உங்கள் **REST endpoint** ஐ *config.py* கோப்பில் நகலெடுத்து ஒட்டவும், `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` ஐ உங்கள் **REST endpoint** உடன் மாற்றவும்.
1. உங்கள் **Primary key** ஐ *config.py* கோப்பில் நகலெடுத்து ஒட்டவும், `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` ஐ உங்கள் **Primary key** உடன் மாற்றவும்.

    ![api key மற்றும் endpoint uri ஐ நகலெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow/02-05-copy-apikey-endpoint.png)

#### *flow.dag.yml* கோப்பில் குறியீட்டை சேர்க்கவும்

1. Visual Studio Code-ல் *flow.dag.yml* கோப்பை திறக்கவும்.

1. *flow.dag.yml* கோப்பில் கீழே உள்ள குறியீட்டை சேர்க்கவும்.

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

#### *integrate_with_promptflow.py* கோப்பில் குறியீட்டை சேர்க்கவும்

1. Visual Studio Code-ல் *integrate_with_promptflow.py* கோப்பை திறக்கவும்.

1. *integrate_with_promptflow.py* கோப்பில் கீழே உள்ள குறியீட்டை சேர்க்கவும்.

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

### உங்கள் தனிப்பயன் மாடலுடன் உரையாடவும்

1. *deploy_model.py* ஸ்கிரிப்டை இயக்கி Azure Machine Learning-ல் பிரசார செயல்முறையை தொடங்க கீழே உள்ள கட்டளையை தட்டச்சு செய்யவும்.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. இதோ ஒரு எடுத்துக்காட்டு: இப்போது நீங்கள் உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாடலாம். Fine-tuning செய்ய பயன்படுத்திய தரவின் அடிப்படையில் கேள்விகளை கேட்க பரிந்துரைக்கப்படுகிறது.

    ![Prompt flow எடுத்துக்காட்டு.](../../../../../../imgs/02/FineTuning-PromptFlow/02-06-promptflow-example.png)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறையை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.