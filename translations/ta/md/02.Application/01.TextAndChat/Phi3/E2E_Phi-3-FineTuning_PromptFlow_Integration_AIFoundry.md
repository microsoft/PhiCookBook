<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-10-11T11:59:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ta"
}
-->
# Fine-tune மற்றும் Prompt flow உடன் தனிப்பயன் Phi-3 மாடல்களை Azure AI Foundry-யில் ஒருங்கிணைக்கவும்

இந்த முழுமையான (E2E) மாதிரி Microsoft Tech Community-ல் உள்ள "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" வழிகாட்டுதலின் அடிப்படையில் உருவாக்கப்பட்டுள்ளது. இது Azure AI Foundry-யில் Prompt flow உடன் தனிப்பயன் Phi-3 மாடல்களை fine-tune செய்யும், வெளியிடும் மற்றும் ஒருங்கிணைக்கும் செயல்முறைகளை அறிமுகப்படுத்துகிறது. 

முன்னைய E2E மாதிரியைப் போல, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", இது உள்ளூர் முறையில் கோடுகளை இயக்குவதைக் கொண்டிருந்தது, இந்த வழிகாட்டுதல் முழுமையாக Azure AI / ML Studio-வில் உங்கள் மாடலை fine-tune செய்யும் மற்றும் ஒருங்கிணைக்கும் செயல்முறைகளில் கவனம் செலுத்துகிறது.

## மேலோட்டம்

இந்த E2E மாதிரியில், நீங்கள் Phi-3 மாடலை fine-tune செய்யும் மற்றும் Azure AI Foundry-யில் Prompt flow உடன் ஒருங்கிணைக்கும் முறையை கற்றுக்கொள்வீர்கள். Azure AI / ML Studio-வை பயன்படுத்தி, தனிப்பயன் AI மாடல்களை வெளியிடுவதற்கும் பயன்படுத்துவதற்கும் ஒரு workflow-ஐ உருவாக்குவீர்கள். இந்த E2E மாதிரி மூன்று சூழல்களாகப் பிரிக்கப்பட்டுள்ளது:

**சூழல் 1: Azure வளங்களை அமைத்து fine-tune செய்ய தயாராகவும்**

**சூழல் 2: Phi-3 மாடலை fine-tune செய்து Azure Machine Learning Studio-வில் வெளியிடவும்**

**சூழல் 3: Prompt flow உடன் ஒருங்கிணைத்து Azure AI Foundry-யில் உங்கள் தனிப்பயன் மாடலுடன் உரையாடவும்**

இது இந்த E2E மாதிரியின் மேலோட்டம்.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/00-01-architecture.png)

### உள்ளடக்க அட்டவணை

1. **[சூழல் 1: Azure வளங்களை அமைத்து fine-tune செய்ய தயாராகவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace உருவாக்கவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription-ல் GPU quotas-ஐ கோரவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [பங்கு ஒதுக்கீட்டைச் சேர்க்கவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Project-ஐ அமைக்கவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tune செய்ய dataset-ஐ தயாரிக்கவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[சூழல் 2: Phi-3 மாடலை fine-tune செய்து Azure Machine Learning Studio-வில் வெளியிடவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 மாடலை fine-tune செய்யவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tuned Phi-3 மாடலை வெளியிடவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[சூழல் 3: Prompt flow உடன் ஒருங்கிணைத்து Azure AI Foundry-யில் உங்கள் தனிப்பயன் மாடலுடன் உரையாடவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Prompt flow உடன் தனிப்பயன் Phi-3 மாடலை ஒருங்கிணைக்கவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாடவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## சூழல் 1: Azure வளங்களை அமைத்து fine-tune செய்ய தயாராகவும்

### Azure Machine Learning Workspace உருவாக்கவும்

1. **search bar**-ல் *azure machine learning* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **Azure Machine Learning**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Type azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-01-type-azml.png)

2. **+ Create**-ஐ navigation menu-ல் தேர்ந்தெடுக்கவும்.

3. Navigation menu-ல் **New workspace**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Select new workspace.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-02-select-new-workspace.png)

4. பின்வரும் பணிகளைச் செய்யவும்:

    - உங்கள் Azure **Subscription**-ஐத் தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐத் தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது ஒன்றை உருவாக்கவும்).
    - **Workspace Name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - பயன்படுத்த விரும்பும் **Region**-ஐத் தேர்ந்தெடுக்கவும்.
    - **Storage account**-ஐத் தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது ஒன்றை உருவாக்கவும்).
    - **Key vault**-ஐத் தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது ஒன்றை உருவாக்கவும்).
    - **Application insights**-ஐத் தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது ஒன்றை உருவாக்கவும்).
    - **Container registry**-ஐத் தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது ஒன்றை உருவாக்கவும்).

    ![Fill azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-03-fill-AZML.png)

5. **Review + Create**-ஐத் தேர்ந்தெடுக்கவும்.

6. **Create**-ஐத் தேர்ந்தெடுக்கவும்.

### Azure Subscription-ல் GPU quotas-ஐ கோரவும்

இந்த வழிகாட்டுதலில், நீங்கள் GPUs-ஐப் பயன்படுத்தி Phi-3 மாடலை fine-tune செய்து வெளியிட கற்றுக்கொள்வீர்கள். Fine-tune செய்ய *Standard_NC24ads_A100_v4* GPU-ஐ பயன்படுத்துவீர்கள், இது quota கோரிக்கையைத் தேவைப்படும். வெளியிட *Standard_NC6s_v3* GPU-ஐ பயன்படுத்துவீர்கள், இது quota கோரிக்கையைத் தேவைப்படும்.

> [!NOTE]
>
> GPU ஒதுக்கீட்டுக்கு தகுதியானது Pay-As-You-Go subscriptions (இது நிலையான subscription வகை) மட்டுமே; பயனளிக்கும் subscriptions தற்போது ஆதரிக்கப்படவில்லை.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)-க்கு செல்லவும்.

1. *Standard NCADSA100v4 Family* quota-ஐ கோர பின்வரும் பணிகளைச் செய்யவும்:

    - இடது பக்கத்திலுள்ள **Quota**-ஐத் தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Virtual machine family**-ஐத் தேர்ந்தெடுக்கவும். உதாரணமாக, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**-ஐத் தேர்ந்தெடுக்கவும், இது *Standard_NC24ads_A100_v4* GPU-ஐ உள்ளடக்கியது.
    - Navigation menu-ல் **Request quota**-ஐத் தேர்ந்தெடுக்கவும்.

        ![Request quota.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/02-02-request-quota.png)

    - Request quota பக்கத்தில், பயன்படுத்த விரும்பும் **New cores limit**-ஐ உள்ளிடவும். உதாரணமாக, 24.
    - Request quota பக்கத்தில், GPU quota-ஐ கோர **Submit**-ஐத் தேர்ந்தெடுக்கவும்.

1. *Standard NCSv3 Family* quota-ஐ கோர பின்வரும் பணிகளைச் செய்யவும்:

    - இடது பக்கத்திலுள்ள **Quota**-ஐத் தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Virtual machine family**-ஐத் தேர்ந்தெடுக்கவும். உதாரணமாக, **Standard NCSv3 Family Cluster Dedicated vCPUs**-ஐத் தேர்ந்தெடுக்கவும், இது *Standard_NC6s_v3* GPU-ஐ உள்ளடக்கியது.
    - Navigation menu-ல் **Request quota**-ஐத் தேர்ந்தெடுக்கவும்.
    - Request quota பக்கத்தில், பயன்படுத்த விரும்பும் **New cores limit**-ஐ உள்ளிடவும். உதாரணமாக, 24.
    - Request quota பக்கத்தில், GPU quota-ஐ கோர **Submit**-ஐத் தேர்ந்தெடுக்கவும்.

### பங்கு ஒதுக்கீட்டைச் சேர்க்கவும்

உங்கள் மாடல்களை fine-tune செய்து வெளியிட, முதலில் User Assigned Managed Identity (UAI)-ஐ உருவாக்கி, அதற்கான உரிமைகளை ஒதுக்க வேண்டும். இந்த UAI வெளியீட்டின் போது authentication-க்கு பயன்படுத்தப்படும்.

#### User Assigned Managed Identity(UAI) உருவாக்கவும்

1. **search bar**-ல் *managed identities* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **Managed Identities**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Type managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-01-type-managed-identities.png)

1. **+ Create**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Select create.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-02-select-create.png)

1. பின்வரும் பணிகளைச் செய்யவும்:

    - உங்கள் Azure **Subscription**-ஐத் தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐத் தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது ஒன்றை உருவாக்கவும்).
    - பயன்படுத்த விரும்பும் **Region**-ஐத் தேர்ந்தெடுக்கவும்.
    - **Name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.

    ![Select create.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-03-fill-managed-identities-1.png)

1. **Review + create**-ஐத் தேர்ந்தெடுக்கவும்.

1. **+ Create**-ஐத் தேர்ந்தெடுக்கவும்.

#### Managed Identity-க்கு Contributor பங்கு ஒதுக்கீட்டைச் சேர்க்கவும்

1. நீங்கள் உருவாக்கிய Managed Identity resource-க்கு செல்லவும்.

1. இடது பக்கத்திலுள்ள **Azure role assignments**-ஐத் தேர்ந்தெடுக்கவும்.

1. Navigation menu-ல் **+Add role assignment**-ஐத் தேர்ந்தெடுக்கவும்.

1. Add role assignment பக்கத்தில், பின்வரும் பணிகளைச் செய்யவும்:
    - **Scope**-ஐ **Resource group**-ஆகத் தேர்ந்தெடுக்கவும்.
    - உங்கள் Azure **Subscription**-ஐத் தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐத் தேர்ந்தெடுக்கவும்.
    - **Role**-ஐ **Contributor**-ஆகத் தேர்ந்தெடுக்கவும்.

    ![Fill contributor role.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-04-fill-contributor-role.png)

2. **Save**-ஐத் தேர்ந்தெடுக்கவும்.

#### Managed Identity-க்கு Storage Blob Data Reader பங்கு ஒதுக்கீட்டைச் சேர்க்கவும்

1. **search bar**-ல் *storage accounts* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **Storage accounts**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Type storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-05-type-storage-accounts.png)

1. நீங்கள் உருவாக்கிய Azure Machine Learning workspace-க்கு தொடர்புடைய storage account-ஐத் தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephistorage*.

1. Add role assignment பக்கத்திற்குச் செல்ல பின்வரும் பணிகளைச் செய்யவும்:

    - நீங்கள் உருவாக்கிய Azure Storage account-க்கு செல்லவும்.
    - இடது பக்கத்திலுள்ள **Access Control (IAM)**-ஐத் தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **+ Add**-ஐத் தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **Add role assignment**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Add role.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-06-add-role.png)

1. Add role assignment பக்கத்தில், பின்வரும் பணிகளைச் செய்யவும்:

    - Role பக்கத்தில், **search bar**-ல் *Storage Blob Data Reader* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **Storage Blob Data Reader**-ஐத் தேர்ந்தெடுக்கவும்.
    - Role பக்கத்தில், **Next**-ஐத் தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில், **Assign access to** **Managed identity**-ஐத் தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில், **+ Select members**-ஐத் தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், உங்கள் Azure **Subscription**-ஐத் தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், **Managed identity**-ஐ **Manage Identity**-ஆகத் தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், நீங்கள் உருவாக்கிய Manage Identity-ஐத் தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephi-managedidentity*.
    - Select managed identities பக்கத்தில், **Select**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Select managed identity.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-08-select-managed-identity.png)

1. **Review + assign**-ஐத் தேர்ந்தெடுக்கவும்.

#### Managed Identity-க்கு AcrPull பங்கு ஒதுக்கீட்டைச் சேர்க்கவும்

1. **search bar**-ல் *container registries* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **Container registries**-ஐத் தேர்ந்தெடுக்கவும்.

    ![Type container registries.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-09-type-container-registries.png)

1. Azure Machine Learning workspace-க்கு தொடர்புடைய container registry-ஐத் தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephicontainerregistry*

1. Add role assignment பக்கத்திற்குச் செல்ல பின்வரும் பணிகளைச் செய்யவும்:

    - இடது பக்கத்திலுள்ள **Access Control (IAM)**-ஐத் தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **+ Add**-ஐத் தேர்ந்தெடுக்கவும்.
    - Navigation menu-ல் **Add role assignment**-ஐத் தேர்ந்தெடுக்கவும்.

1. Add role assignment பக்கத்தில், பின்வரும் பணிகளைச் செய்யவும்:

    - Role பக்கத்தில், **search bar**-ல் *AcrPull* எனத் தட்டச்சு செய்து, தோன்றும் விருப்பங்களில் **AcrPull**-ஐத் தேர்ந்தெடுக்கவும்.
    - Role பக்கத்தில், **Next**-ஐத் தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில், **Assign access to** **Managed identity**-ஐத் தேர்ந்தெடுக்கவும்.
    - Members பக்கத்தில், **+ Select members**-ஐத் தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், உங்கள் Azure **Subscription**-ஐத் தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், **Managed identity**-ஐ **Manage Identity**-ஆகத் தேர்ந்தெடுக்கவும்.
    - Select managed identities பக்கத்தில், நீங்கள் உருவாக்கிய Manage Identity-ஐத் தேர்ந்தெடுக்கவும். உதாரணமாக, *finetunephi-managedidentity*.
    - Select managed identities பக்கத்தில், **Select**-ஐத் தேர்ந்தெடுக்கவும்.
    - **Review + assign**-ஐத் தேர்ந்தெடுக்கவும்.

### Project-ஐ அமைக்கவும்

Fine-tune செய்ய datasets-ஐ பதிவிறக்க, நீங்கள் ஒரு உள்ளூர் சூழலை அமைக்க வேண்டும்.

இந்த பயிற்சியில், நீங்கள்

- வேலை செய்ய ஒரு கோப்புறையை உருவாக்கவும்.
- ஒரு virtual environment உருவாக்கவும்.
- தேவையான packages-ஐ நிறுவவும்.
- Dataset-ஐ பதிவிறக்க *download_dataset.py* கோப்பை உருவாக்கவும்.

#### வேலை செய்ய ஒரு கோப்புறையை உருவாக்கவும்

1. ஒரு terminal window-ஐ திறந்து, default பாதையில் *finetune-phi* என்ற கோப்புறையை உருவாக்க பின்வரும் கட்டளையைத் தட்டச்சு செய்யவும்.

    ```console
    mkdir finetune-phi
    ```

2. உங்கள் டெர்மினலில் கீழே உள்ள கட்டளையை டைப் செய்து, நீங்கள் உருவாக்கிய *finetune-phi* கோப்பகத்திற்கு செல்லவும்.

    ```console
    cd finetune-phi
    ```

#### ஒரு மெய்நிகர் சூழலை உருவாக்கவும்

1. உங்கள் டெர்மினலில் கீழே உள்ள கட்டளையை டைப் செய்து *.venv* என்ற பெயரில் ஒரு மெய்நிகர் சூழலை உருவாக்கவும்.

    ```console
    python -m venv .venv
    ```

2. மெய்நிகர் சூழலை செயல்படுத்த கீழே உள்ள கட்டளையை டைப் செய்யவும்.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> இது செயல்பட்டால், *(.venv)* என்ற குறிப்பு கட்டளை முன்பதிவில் தோன்றும்.

#### தேவையான தொகுதிகளை நிறுவவும்

1. தேவையான தொகுதிகளை நிறுவ உங்கள் டெர்மினலில் கீழே உள்ள கட்டளைகளை டைப் செய்யவும்.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` உருவாக்கவும்

> [!NOTE]
> முழு கோப்பக அமைப்பு:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**-ஐ திறக்கவும்.

1. மெனு பட்டியில் **File**-ஐ தேர்ந்தெடுக்கவும்.

1. **Open Folder**-ஐ தேர்ந்தெடுக்கவும்.

1. நீங்கள் உருவாக்கிய *finetune-phi* கோப்பகத்தை தேர்ந்தெடுக்கவும், இது *C:\Users\yourUserName\finetune-phi*-ல் உள்ளது.

    ![நீங்கள் உருவாக்கிய கோப்பகத்தை தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-01-open-project-folder.png)

1. Visual Studio Code-இன் இடது பக்கத்தில், வலது கிளிக் செய்து **New File**-ஐ தேர்ந்தெடுத்து *download_dataset.py* என்ற புதிய கோப்பை உருவாக்கவும்.

    ![புதிய கோப்பை உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-02-create-new-file.png)

### நுணுக்கமாக அமைக்க தரவுத்தொகுப்பை தயாரிக்கவும்

இந்த பயிற்சியில், *download_dataset.py* கோப்பை இயக்கி *ultrachat_200k* தரவுத்தொகுப்புகளை உங்கள் உள்ளூர் சூழலுக்கு பதிவிறக்குவீர்கள். பின்னர், இந்த தரவுத்தொகுப்புகளை பயன்படுத்தி Azure Machine Learning-ல் Phi-3 மாடலை நுணுக்கமாக அமைப்பீர்கள்.

இந்த பயிற்சியில், நீங்கள்:

- தரவுத்தொகுப்புகளை பதிவிறக்க *download_dataset.py* கோப்பில் குறியீட்டை சேர்க்கவும்.
- *download_dataset.py* கோப்பை இயக்கி தரவுத்தொகுப்புகளை உங்கள் உள்ளூர் சூழலுக்கு பதிவிறக்கவும்.

#### *download_dataset.py* மூலம் உங்கள் தரவுத்தொகுப்பை பதிவிறக்கவும்

1. Visual Studio Code-ல் *download_dataset.py* கோப்பை திறக்கவும்.

1. *download_dataset.py* கோப்பில் கீழே உள்ள குறியீட்டை சேர்க்கவும்.

    ```python
    import json
    import os
    from datasets import load_dataset

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
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. ஸ்கிரிப்டை இயக்கி தரவுத்தொகுப்பை உங்கள் உள்ளூர் சூழலுக்கு பதிவிறக்க கீழே உள்ள கட்டளையை டைப் செய்யவும்.

    ```console
    python download_dataset.py
    ```

1. தரவுத்தொகுப்புகள் உங்கள் உள்ளூர் *finetune-phi/data* கோப்பகத்தில் வெற்றிகரமாக சேமிக்கப்பட்டுள்ளதா என்பதை சரிபார்க்கவும்.

> [!NOTE]
>
> #### தரவுத்தொகுப்பு அளவு மற்றும் நுணுக்கமாக அமைக்கும் நேரம் குறித்த குறிப்பு
>
> இந்த பயிற்சியில், நீங்கள் தரவுத்தொகுப்பின் 1% மட்டுமே பயன்படுத்துகிறீர்கள் (`split='train[:1%]'`). இது தரவின் அளவை குறிப்பிடத்தக்க அளவில் குறைக்கிறது, பதிவேற்றம் மற்றும் நுணுக்கமாக அமைக்கும் செயல்முறைகளை வேகமாக்குகிறது. பயிற்சியின் நேரம் மற்றும் மாடல் செயல்திறனுக்கு இடையிலான சரியான சமநிலையை கண்டறிய நீங்கள் சதவீதத்தை சரிசெய்யலாம். குறைந்த அளவிலான தரவுத்தொகுப்பைப் பயன்படுத்துவது நுணுக்கமாக அமைக்கும் நேரத்தை குறைக்கிறது, இது பயிற்சிக்காக மேலாண்மை செய்யக்கூடியதாக இருக்கும்.

## சூழல் 2: Phi-3 மாடலை நுணுக்கமாக அமைத்து Azure Machine Learning Studio-வில் பிரசுரிக்கவும்

### Phi-3 மாடலை நுணுக்கமாக அமைக்கவும்

இந்த பயிற்சியில், நீங்கள் Azure Machine Learning Studio-வில் Phi-3 மாடலை நுணுக்கமாக அமைப்பீர்கள்.

இந்த பயிற்சியில், நீங்கள்:

- நுணுக்கமாக அமைக்க கணினி கிளஸ்டரை உருவாக்கவும்.
- Azure Machine Learning Studio-வில் Phi-3 மாடலை நுணுக்கமாக அமைக்கவும்.

#### நுணுக்கமாக அமைக்க கணினி கிளஸ்டரை உருவாக்கவும்

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)-க்கு செல்லவும்.

1. இடது பக்க தாவலில் **Compute**-ஐ தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **Compute clusters**-ஐ தேர்ந்தெடுக்கவும்.

1. **+ New**-ஐ தேர்ந்தெடுக்கவும்.

    ![கணினியைத் தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-01-select-compute.png)

1. கீழே உள்ள பணிகளைச் செய்யவும்:

    - நீங்கள் பயன்படுத்த விரும்பும் **Region**-ஐ தேர்ந்தெடுக்கவும்.
    - **Virtual machine tier**-ஐ **Dedicated**-க்கு மாற்றவும்.
    - **Virtual machine type**-ஐ **GPU**-க்கு மாற்றவும்.
    - **Virtual machine size** வடிகட்டியை **Select from all options**-க்கு மாற்றவும்.
    - **Virtual machine size**-ஐ **Standard_NC24ads_A100_v4**-க்கு மாற்றவும்.

    ![கிளஸ்டரை உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-02-create-cluster.png)

1. **Next**-ஐ தேர்ந்தெடுக்கவும்.

1. கீழே உள்ள பணிகளைச் செய்யவும்:

    - **Compute name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - **Minimum number of nodes**-ஐ **0**-க்கு மாற்றவும்.
    - **Maximum number of nodes**-ஐ **1**-க்கு மாற்றவும்.
    - **Idle seconds before scale down**-ஐ **120**-க்கு மாற்றவும்.

    ![கிளஸ்டரை உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-03-create-cluster.png)

1. **Create**-ஐ தேர்ந்தெடுக்கவும்.

#### Phi-3 மாடலை நுணுக்கமாக அமைக்கவும்

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)-க்கு செல்லவும்.

1. நீங்கள் உருவாக்கிய Azure Machine Learning workspace-ஐ தேர்ந்தெடுக்கவும்.

    ![நீங்கள் உருவாக்கிய workspace-ஐ தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. கீழே உள்ள பணிகளைச் செய்யவும்:

    - இடது பக்க தாவலில் **Model catalog**-ஐ தேர்ந்தெடுக்கவும்.
    - **search bar**-ல் *phi-3-mini-4k* என டைப் செய்து தோன்றும் விருப்பங்களில் **Phi-3-mini-4k-instruct**-ஐ தேர்ந்தெடுக்கவும்.

    ![phi-3-mini-4k என டைப் செய்யவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-05-type-phi-3-mini-4k.png)

1. வழிசெலுத்தல் மெனுவில் **Fine-tune**-ஐ தேர்ந்தெடுக்கவும்.

    ![Fine-tune-ஐ தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-06-select-fine-tune.png)

1. கீழே உள்ள பணிகளைச் செய்யவும்:

    - **Select task type**-ஐ **Chat completion**-க்கு மாற்றவும்.
    - **+ Select data**-ஐ தேர்ந்தெடுத்து **Training data**-ஐ பதிவேற்றவும்.
    - Validation data பதிவேற்ற வகையை **Provide different validation data**-க்கு மாற்றவும்.
    - **+ Select data**-ஐ தேர்ந்தெடுத்து **Validation data**-ஐ பதிவேற்றவும்.

    ![Fine-tuning பக்கத்தை நிரப்பவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-07-fill-finetuning.png)

    > [!TIP]
    >
    > **Advanced settings**-ஐ தேர்ந்தெடுத்து **learning_rate** மற்றும் **lr_scheduler_type** போன்ற அமைப்புகளை தனிப்பயனாக்கி, உங்கள் தேவைகளுக்கு ஏற்ப fine-tuning செயல்முறையை மேம்படுத்தலாம்.

1. **Finish**-ஐ தேர்ந்தெடுக்கவும்.

1. இந்த பயிற்சியில், நீங்கள் Azure Machine Learning-ஐப் பயன்படுத்தி Phi-3 மாடலை வெற்றிகரமாக fine-tune செய்துள்ளீர்கள். Fine-tuning செயல்முறை குறிப்பிடத்தக்க நேரத்தை எடுத்துக்கொள்ளலாம் என்பதை நினைவில் கொள்ளவும். Fine-tuning வேலை இயக்கப்பட்ட பிறகு, அது முடிவடையும் வரை காத்திருக்க வேண்டும். Azure Machine Learning Workspace-இல் இடது பக்கத்தில் உள்ள Jobs தாவலில் fine-tuning வேலை நிலையை கண்காணிக்கலாம். அடுத்த தொடரில், fine-tuned மாடலை பிரசுரித்து Prompt flow-இன் மூலம் ஒருங்கிணைப்பீர்கள்.

    ![Fine-tuning வேலை பார்க்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-08-output.png)

### Fine-tuned Phi-3 மாடலை பிரசுரிக்கவும்

Fine-tuned Phi-3 மாடலை Prompt flow-இன் மூலம் ஒருங்கிணைக்க, மாடலை நேரடி முன்னறிவிப்பு பயன்பாட்டிற்கு அணுகக்கூடியதாக மாற்ற பிரசுரிக்க வேண்டும். இந்த செயல்முறை மாடலை பதிவு செய்வது, ஒரு ஆன்லைன் இறுதிப்புள்ளியை உருவாக்குவது மற்றும் மாடலை பிரசுரிப்பது ஆகியவற்றை உள்ளடக்கியது.

இந்த பயிற்சியில், நீங்கள்:

- Azure Machine Learning workspace-இல் fine-tuned மாடலை பதிவு செய்யவும்.
- ஒரு ஆன்லைன் இறுதிப்புள்ளியை உருவாக்கவும்.
- பதிவு செய்யப்பட்ட fine-tuned Phi-3 மாடலை பிரசுரிக்கவும்.

#### Fine-tuned மாடலை பதிவு செய்யவும்

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)-க்கு செல்லவும்.

1. நீங்கள் உருவாக்கிய Azure Machine Learning workspace-ஐ தேர்ந்தெடுக்கவும்.

    ![நீங்கள் உருவாக்கிய workspace-ஐ தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. இடது பக்க தாவலில் **Models**-ஐ தேர்ந்தெடுக்கவும்.
1. **+ Register**-ஐ தேர்ந்தெடுக்கவும்.
1. **From a job output**-ஐ தேர்ந்தெடுக்கவும்.

    ![மாடலை பதிவு செய்யவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-01-register-model.png)

1. நீங்கள் உருவாக்கிய வேலைகளைத் தேர்ந்தெடுக்கவும்.

    ![வேலைகளைத் தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-02-select-job.png)

1. **Next**-ஐ தேர்ந்தெடுக்கவும்.

1. **Model type**-ஐ **MLflow**-க்கு மாற்றவும்.

1. **Job output** தானாகவே தேர்ந்தெடுக்கப்பட்டிருக்கும்; இது சரியாக இருக்க வேண்டும்.

    ![வெளியீட்டைத் தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-03-select-output.png)

2. **Next**-ஐ தேர்ந்தெடுக்கவும்.

3. **Register**-ஐ தேர்ந்தெடுக்கவும்.

    ![Register-ஐ தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-04-register.png)

4. இடது பக்க தாவலில் **Models** மெனுவில் செல்லும் மூலம் உங்கள் பதிவு செய்யப்பட்ட மாடலைப் பார்க்கலாம்.

    ![பதிவு செய்யப்பட்ட மாடல்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-05-registered-model.png)

#### Fine-tuned மாடலை பிரசுரிக்கவும்

1. நீங்கள் உருவாக்கிய Azure Machine Learning workspace-க்கு செல்லவும்.

1. இடது பக்க தாவலில் **Endpoints**-ஐ தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **Real-time endpoints**-ஐ தேர்ந்தெடுக்கவும்.

    ![Endpoint உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-06-create-endpoint.png)

1. **Create**-ஐ தேர்ந்தெடுக்கவும்.

1. நீங்கள் உருவாக்கிய பதிவு செய்யப்பட்ட மாடலைத் தேர்ந்தெடுக்கவும்.

    ![பதிவு செய்யப்பட்ட மாடலைத் தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-07-select-registered-model.png)

1. **Select**-ஐ தேர்ந்தெடுக்கவும்.

1. கீழே உள்ள பணிகளைச் செய்யவும்:

    - **Virtual machine**-ஐ *Standard_NC6s_v3*-க்கு மாற்றவும்.
    - நீங்கள் பயன்படுத்த விரும்பும் **Instance count**-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *1*.
    - **Endpoint**-ஐ **New**-க்கு மாற்றி ஒரு புதிய இறுதிப்புள்ளியை உருவாக்கவும்.
    - **Endpoint name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - **Deployment name**-ஐ உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.

    ![Deployment அமைப்புகளை நிரப்பவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-08-deployment-setting.png)

1. **Deploy**-ஐ தேர்ந்தெடுக்கவும்.

> [!WARNING]
> உங்கள் கணக்கில் கூடுதல் கட்டணங்களைத் தவிர்க்க, Azure Machine Learning workspace-இல் உருவாக்கப்பட்ட இறுதிப்புள்ளியை நீக்கவும்.
>

#### Azure Machine Learning Workspace-இல் பிரசுர நிலையைச் சரிபார்க்கவும்

1. நீங்கள் உருவாக்கிய Azure Machine Learning workspace-க்கு செல்லவும்.

1. இடது பக்க தாவலில் **Endpoints**-ஐ தேர்ந்தெடுக்கவும்.

1. நீங்கள் உருவாக்கிய இறுதிப்புள்ளியைத் தேர்ந்தெடுக்கவும்.

    ![Endpoints-ஐ தேர்ந்தெடுக்கவும்](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-09-check-deployment.png)

1. இந்த பக்கத்தில், பிரசுர செயல்முறையின் போது இறுதிப்புள்ளிகளை நிர்வகிக்கலாம்.

> [!NOTE]
> பிரசுரம் முடிந்ததும், **Live traffic** **100%**-க்கு அமைக்கப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும். அது இல்லையெனில், **Update traffic**-ஐ தேர்ந்தெடுத்து போக்குவரத்து அமைப்புகளை சரிசெய்யவும். போக்குவரத்து **0%**-க்கு அமைக்கப்பட்டிருந்தால், மாடலை சோதிக்க முடியாது என்பதை நினைவில் கொள்ளவும்.
>
> ![Traffic அமைக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-10-set-traffic.png)
>

## சூழல் 3: Prompt flow-இன் மூலம் ஒருங்கிணைத்து Azure AI Foundry-ல் உங்கள் தனிப்பயன் மாடலுடன் உரையாடவும்

### Prompt flow-இன் மூலம் தனிப்பயன் Phi-3 மாடலை ஒருங்கிணைக்கவும்

Fine-tuned மாடலை வெற்றிகரமாக பிரசுரித்த பிறகு, Prompt Flow-இன் மூலம் அதை ஒருங்கிணைத்து உங்கள் மாடலை நேரடி பயன்பாடுகளில் பயன்படுத்தலாம், இது உங்கள் தனிப்பயன் Phi-3 மாடலுடன் பல்வேறு தொடர்பு பணிகளைச் செய்ய உதவுகிறது.

இந்த பயிற்சியில், நீங்கள்:

- Azure AI Foundry Hub உருவாக்கவும்.
- Azure AI Foundry Project உருவாக்கவும்.
- Prompt flow உருவாக்கவும்.
- Fine-tuned Phi-3 மாடலுக்கான தனிப்பயன் இணைப்பைச் சேர்க்கவும்.
- Prompt flow அமைப்பைச் செய்து உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாடவும்.

> [!NOTE]
> Promptflow-இன் மூலம் Azure ML Studio-வுடன் ஒருங்கிணைக்கவும் முடியும். ஒரே ஒருங்கிணைப்பு செயல்முறை Azure ML Studio-விற்கும் பொருந்தும்.

#### Azure AI Foundry Hub உருவாக்கவும்

Project உருவாக்குவதற்கு முன் Hub உருவாக்க வேண்டும். Hub என்பது Resource Group போல செயல்படுகிறது, இது Azure AI Foundry-இல் பல Project-களை அமைக்கவும் நிர்வகிக்கவும் உதவுகிறது.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)-க்கு செல்லவும்.

1. இடது பக்க தாவலில் **All hubs**-ஐ தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ New hub**-ஐ தேர்ந்தெடுக்கவும்.
![Hub உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-01-create-hub.png)

1. பின்வரும் பணிகளை செய்யவும்:

    - **Hub name** உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - உங்கள் Azure **Subscription** தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group** தேர்ந்தெடுக்கவும் (தேவையானால் புதியது உருவாக்கவும்).
    - நீங்கள் பயன்படுத்த விரும்பும் **Location** தேர்ந்தெடுக்கவும்.
    - **Connect Azure AI Services** தேர்ந்தெடுக்கவும் (தேவையானால் புதியது உருவாக்கவும்).
    - **Connect Azure AI Search** தேர்ந்தெடுத்து **Skip connecting** செய்யவும்.

    ![Hub நிரப்பவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-02-fill-hub.png)

1. **Next** தேர்ந்தெடுக்கவும்.

#### Azure AI Foundry Project உருவாக்கவும்

1. நீங்கள் உருவாக்கிய Hub-இல், இடது பக்கம் உள்ள தாவலில் **All projects** தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ New project** தேர்ந்தெடுக்கவும்.

    ![புதிய Project தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-04-select-new-project.png)

1. **Project name** உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.

    ![Project உருவாக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-05-create-project.png)

1. **Create a project** தேர்ந்தெடுக்கவும்.

#### Fine-tuned Phi-3 மாடலுக்கான தனிப்பயன் இணைப்பைச் சேர்க்கவும்

உங்கள் தனிப்பயன் Phi-3 மாடலை Prompt flow-இன் மூலம் ஒருங்கிணைக்க, மாடலின் endpoint மற்றும் key-ஐ தனிப்பயன் இணைப்பில் சேமிக்க வேண்டும். இந்த அமைப்பு Prompt flow-இல் உங்கள் தனிப்பயன் Phi-3 மாடலுக்கு அணுகலை உறுதிசெய்கிறது.

#### Fine-tuned Phi-3 மாடலின் api key மற்றும் endpoint uri அமைக்கவும்

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) ஐ பார்வையிடவும்.

1. நீங்கள் உருவாக்கிய Azure Machine learning workspace-க்கு செல்லவும்.

1. இடது பக்கம் உள்ள தாவலில் **Endpoints** தேர்ந்தெடுக்கவும்.

    ![Endpoints தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-06-select-endpoints.png)

1. நீங்கள் உருவாக்கிய endpoint-ஐ தேர்ந்தெடுக்கவும்.

    ![உருவாக்கிய endpoint-ஐ தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-07-select-endpoint-created.png)

1. வழிசெலுத்தல் மெனுவில் **Consume** தேர்ந்தெடுக்கவும்.

1. உங்கள் **REST endpoint** மற்றும் **Primary key** ஐ நகலெடுக்கவும்.

    ![api key மற்றும் endpoint uri ஐ நகலெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-08-copy-endpoint-key.png)

#### Custom Connection சேர்க்கவும்

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) ஐ பார்வையிடவும்.

1. நீங்கள் உருவாக்கிய Azure AI Foundry project-க்கு செல்லவும்.

1. நீங்கள் உருவாக்கிய Project-இல், இடது பக்கம் உள்ள தாவலில் **Settings** தேர்ந்தெடுக்கவும்.

1. **+ New connection** தேர்ந்தெடுக்கவும்.

    ![புதிய இணைப்பைத் தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-09-select-new-connection.png)

1. வழிசெலுத்தல் மெனுவில் **Custom keys** தேர்ந்தெடுக்கவும்.

    ![Custom keys தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-10-select-custom-keys.png)

1. பின்வரும் பணிகளை செய்யவும்:

    - **+ Add key value pairs** தேர்ந்தெடுக்கவும்.
    - Key name-க்கு **endpoint** உள்ளிடவும் மற்றும் Azure ML Studio-இல் நீங்கள் நகலெடுத்த endpoint-ஐ value புலத்தில் ஒட்டவும்.
    - மீண்டும் **+ Add key value pairs** தேர்ந்தெடுக்கவும்.
    - Key name-க்கு **key** உள்ளிடவும் மற்றும் Azure ML Studio-இல் நீங்கள் நகலெடுத்த key-ஐ value புலத்தில் ஒட்டவும்.
    - Keys சேர்த்த பிறகு, **is secret** தேர்ந்தெடுத்து key வெளிப்படாமல் இருக்கச் செய்யவும்.

    ![இணைப்பைச் சேர்க்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-11-add-connection.png)

1. **Add connection** தேர்ந்தெடுக்கவும்.

#### Prompt flow உருவாக்கவும்

நீங்கள் Azure AI Foundry-இல் தனிப்பயன் இணைப்பைச் சேர்த்துள்ளீர்கள். இப்போது, பின்வரும் படிகளைப் பயன்படுத்த Prompt flow உருவாக்குவோம். பின்னர், Prompt flow-ஐ தனிப்பயன் இணைப்புடன் இணைத்து, Prompt flow-இல் fine-tuned மாடலைப் பயன்படுத்தலாம்.

1. நீங்கள் உருவாக்கிய Azure AI Foundry project-க்கு செல்லவும்.

1. இடது பக்கம் உள்ள தாவலில் **Prompt flow** தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ Create** தேர்ந்தெடுக்கவும்.

    ![Prompt flow தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-12-select-promptflow.png)

1. வழிசெலுத்தல் மெனுவில் **Chat flow** தேர்ந்தெடுக்கவும்.

    ![Chat flow தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-13-select-flow-type.png)

1. பயன்படுத்த **Folder name** உள்ளிடவும்.

    ![பெயரை உள்ளிடவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-14-enter-name.png)

2. **Create** தேர்ந்தெடுக்கவும்.

#### Prompt flow-ஐ உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாட அமைக்கவும்

Fine-tuned Phi-3 மாடலை Prompt flow-இல் ஒருங்கிணைக்க வேண்டும். இருப்பினும், வழங்கப்பட்ட Prompt flow இதற்காக வடிவமைக்கப்படவில்லை. எனவே, Prompt flow-ஐ மறுவடிவமைத்து தனிப்பயன் மாடலை ஒருங்கிணைக்க வேண்டும்.

1. Prompt flow-இல், பின்வரும் பணிகளைச் செய்யவும்:

    - **Raw file mode** தேர்ந்தெடுக்கவும்.
    - *flow.dag.yml* கோப்பில் உள்ள அனைத்து உள்ளடக்கங்களையும் நீக்கவும்.
    - *flow.dag.yml* கோப்பில் பின்வரும் குறியீட்டைச் சேர்க்கவும்.

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

    - **Save** தேர்ந்தெடுக்கவும்.

    ![Raw file mode தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-15-select-raw-file-mode.png)

1. Prompt flow-இல் தனிப்பயன் Phi-3 மாடலைப் பயன்படுத்த *integrate_with_promptflow.py* கோப்பில் பின்வரும் குறியீட்டைச் சேர்க்கவும்.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Prompt flow குறியீட்டை ஒட்டவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-16-paste-promptflow-code.png)

> [!NOTE]
> Azure AI Foundry-இல் Prompt flow-ஐப் பயன்படுத்துவதற்கான விரிவான தகவலுக்கு, [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ஐப் பார்க்கவும்.

1. **Chat input**, **Chat output** தேர்ந்தெடுத்து உங்கள் மாடலுடன் உரையாடவும்.

    ![Input Output.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-17-select-input-output.png)

1. இப்போது உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாட தயாராக உள்ளீர்கள். அடுத்த பயிற்சியில், Prompt flow-ஐ தொடங்குவது மற்றும் fine-tuned Phi-3 மாடலுடன் உரையாட Prompt flow-ஐப் பயன்படுத்துவது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள்.

> [!NOTE]
>
> மறுவடிவமைக்கப்பட்ட flow கீழே உள்ள படத்தைப் போன்றதாக இருக்க வேண்டும்:
>
> ![Flow எடுத்துக்காட்டு.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-18-graph-example.png)
>

### உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாடவும்

நீங்கள் உங்கள் தனிப்பயன் Phi-3 மாடலை fine-tune செய்து Prompt flow-இல் ஒருங்கிணைத்துள்ளீர்கள். இப்போது அதுடன் தொடர்பு கொள்ளத் தயாராக உள்ளீர்கள். இந்த பயிற்சி உங்கள் மாடலுடன் உரையாட Prompt flow-ஐ அமைப்பது மற்றும் தொடங்குவது எப்படி என்பதை வழிநடத்தும். இந்த படிகளைப் பின்பற்றுவதன் மூலம், உங்கள் fine-tuned Phi-3 மாடலின் திறன்களை பல்வேறு பணிகள் மற்றும் உரையாடல்களுக்கு முழுமையாக பயன்படுத்த முடியும்.

- Prompt flow-ஐப் பயன்படுத்த உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாடவும்.

#### Prompt flow தொடங்கவும்

1. Prompt flow-ஐ தொடங்க **Start compute sessions** தேர்ந்தெடுக்கவும்.

    ![Compute session தொடங்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-01-start-compute-session.png)

1. அளவுருக்களை புதுப்பிக்க **Validate and parse input** தேர்ந்தெடுக்கவும்.

    ![Input சரிபார்க்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-02-validate-input.png)

1. நீங்கள் உருவாக்கிய தனிப்பயன் இணைப்பின் **connection**-இன் **Value** ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *connection*.

    ![Connection.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-03-select-connection.png)

#### உங்கள் தனிப்பயன் மாடலுடன் உரையாடவும்

1. **Chat** தேர்ந்தெடுக்கவும்.

    ![Chat தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-04-select-chat.png)

1. இதோ ஒரு எடுத்துக்காட்டு: இப்போது உங்கள் தனிப்பயன் Phi-3 மாடலுடன் உரையாடலாம். Fine-tuning செய்ய பயன்படுத்திய தரவின் அடிப்படையில் கேள்விகள் கேட்க பரிந்துரைக்கப்படுகிறது.

    ![Prompt flow-இன் மூலம் உரையாடவும்.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-05-chat-with-promptflow.png)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் நோக்கம் துல்லியமாக இருக்க வேண்டும் என்பதுதான், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.