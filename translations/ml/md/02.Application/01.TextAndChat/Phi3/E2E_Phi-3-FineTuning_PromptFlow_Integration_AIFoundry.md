# Microsoft Foundry-ൽ Prompt flow ഉപയോഗിച്ച് കസ്റ്റം Phi-3 മോഡലുകൾ ഫൈൻ-ട്യൂൺ ചെയ്ത് ഇന്റഗ്രേറ്റ് ചെയ്യുക

Microsoft Tech Community-ലെ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" എന്ന ഗൈഡിനെ അടിസ്ഥാനമാക്കി ഈ end-to-end (E2E) സാമ്പിൾ രൂപകൽപ്പന ചെയ്തതാണ്. ഈ ഗൈഡ് Microsoft Foundry-യിൽ Prompt flow ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്, ഡിപ്ലോയ്മെന്റ്, കസ്റ്റം Phi-3 മോഡലുകൾ ഇന്റഗ്രേറ്റ് ചെയ്യുന്നതിന്റെ പ്രക്രിയകൾ പരിചയപ്പെടുത്തുന്നു. E2E സാമ്പിള് "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" എന്നത് കോഡ് ലോക്കലിൽ റൺ ചെയ്യുന്നതുമായിരുന്നു, എന്നാൽ ഈ ട്യൂട്ടോറിയൽ പൂർണ്ണമായും Azure AI / ML Studio-വിൽ നിങ്ങളുടെ മോഡലിനെ ഫൈൻ-ട്യൂൺ ചെയ്യുന്നതിലും ഇന്റഗ്രേറ്റു ചെയ്യുന്നതിലുമായി ശ്രദ്ധ കേന്ദ്രീകരിക്കുന്നു.

## അവലോകനം

ഈ E2E സാമ്പിളിൽ, Phi-3 മോഡലിനെ ഫൈൻ-ട്യൂൺ ചെയ്യുകയും Microsoft Foundry-യിൽ Prompt flow-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുകയും ചെയ്യുന്നത് നിങ്ങൾ പഠിക്കും. Azure AI / ML Studio പ്രയോജനപ്പെടുത്തി, കസ്റ്റം AI മോഡലുകൾ ഡിപ്ലോയ് ചെയ്യാനും ഉപയോഗിക്കാനും ഒരു വർക്ക്ഫ്ലോ സ്ഥാപിക്കുകയും ചെയ്യും. ഈ E2E സാമ്പിൾ മൂന്ന് സീനാരിയോകളായി വിഭജിച്ചിരിക്കുന്നു:

**സീനാരിയോ 1: Azure റിസോഴ്സുകൾ സജ്ജമാക്കുക, ഫൈൻ-ട്യൂണിന് തയ്യാറെടുക്കുക**

**സീനാരിയോ 2: Phi-3 മോഡലിന് ഫൈൻ-ട്യൂൺ ചെയ്ത് Azure Machine Learning Studioയിൽ ഡിപ്ലോയ്മെന്റ്**

**സീനാരിയോ 3: Prompt flow-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് Microsoft Foundry-യിൽ നിങ്ങളുടെ কസ്റ്റം മോഡലിനൊപ്പം ചാറ്റ് ചെയ്യുക**

ഈ E2E സാമ്പിളിന്റേത് ഒരു അവലോകനമാണ്.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ml/00-01-architecture.198ba0f1ae6d841a.webp)

### ഉള്ളടക്കപ്പട്ടിക

1. **[സീനാരിയോ 1: Azure റിസോഴ്സുകൾ സജ്ജമാക്കുക, ഫൈൻ-ട്യൂണിന് തയ്യാറെടുക്കുക](#സീനാരിയോ-1-azure-റിസോഴ്സുകൾ-സജ്ജമാക്കുക-ഫൈൻ-ട്യൂണിന്-തയ്യാറെടുക്കുക)**
    - [Azure Machine Learning Workspace സൃഷ്ടിക്കുക](#azure-machine-learning-workspace-സൃഷ്ടിക്കുക)
    - [Azure Subscription-ൽ GPU ക്വോട്ടാസ് അഭ്യര്‍ത്ഥിക്കുക](#azure-subscription-ൽ-gpu-ക്വോട്ടാസ്-അഭ്യർത്ഥിക്കുക)
    - [Role Assignment ചേർക്കുക](#role-assignment-ചേർക്കുക)
    - [പ്രോജക്റ്റ് സജ്ജമാക്കുക](#പ്രോജക്റ്റ്-സജ്ജമാക്കുക)
    - [ഫൈൻ-ട്യൂണിനായി Dataset സജ്ജീകരിക്കുക](#ഫൈൻ-ട്യൂണിംഗിനായി-ഡാറ്റാസെറ്റ്-ഒരുക്കുക)

1. **[സീനാരിയോ 2: Phi-3 മോഡലിന് ഫൈൻ-ട്യൂൺ ചെയ്ത് Azure Machine Learning Studio-യിൽ ഡിപ്ലോയ്മെന്റ്](#സീനാരിയോ-2-phi-3-മോഡൽ-ഫൈൻ-ട്യൂൺ-ചെയ്ത്-azure-machine-learning-studio-ലിൽ-ഡിപ്ലോയ്-ചെയ്യുക)**
    - [Phi-3 മോഡലിന് ഫൈൻ-ട്യൂൺ ചെയ്യുക](#phi-3-മോഡൽ-ഫൈൻ-ട്യൂൺ-ചെയ്യുക)
    - [ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡൽ ഡിപ്ലോയ് ചെയ്യുക](#ഫൈൻ-ട്യൂൺ-ചെയ്ത-phi-3-മോഡൽ-ഡിപ്ലോയ്-ചെയ്യുക)

1. **[സീനാരിയോ 3: Prompt flow-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് Microsoft Foundry-യിൽ നിങ്ങളുടെ കസ്റ്റം മോഡലിനൊപ്പം ചാറ്റ് ചെയ്യുക](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [കസ്റ്റം Phi-3 മോഡൽ Prompt flow-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുക](#കസ്റ്റം-phi-3-മോഡൽ-prompt-flow-വുമായോഴിച്ചു-സംയോജിപ്പിക്കുക)
    - [നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലിനൊപ്പം ചാറ്റ് ചെയ്യുക](#നിങ്ങളുടെ-കസ്റ്റം-phi-3-മോഡലുമായി-ചാറ്റ്-ചെയ്യുക)

## സീനാരിയോ 1: Azure റിസോഴ്സുകൾ സജ്ജമാക്കുക, ഫൈൻ-ട്യൂണിന് തയ്യാറെടുക്കുക

### Azure Machine Learning Workspace സൃഷ്ടിക്കുക

1. പോർട്ടൽ പേജിന്റെ മുകളിൽ ഉള്ള **search bar**-ൽ *azure machine learning* ടൈപ്പ് ചെയ്ത് പ്രത്യക്ഷപ്പെടുന്ന ഓപ്ഷൻകളിൽ നിന്ന് **Azure Machine Learning** തിരഞ്ഞെടുക്കുക.

    ![Type azure machine learning.](../../../../../../translated_images/ml/01-01-type-azml.acae6c5455e67b4b.webp)

2. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ Create** തിരഞ്ഞെടുക്കുക.

3. നാവിഗേഷൻ മെനുവിൽ നിന്നു **New workspace** തിരഞ്ഞെടുക്കുക.

    ![Select new workspace.](../../../../../../translated_images/ml/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. താഴെപ്പറയുന്ന പ്രവർത്തനങ്ങൾ നിർവ്വഹിക്കുക:

    - നിങ്ങളുടെ Azure **Subscription** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാനുള്ള **Resource group** തിരഞ്ഞെടുക്കുക (ആവശ്യമായാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - **Workspace Name** നൽകുക. അതേത്രയും ഒരേയൊരു മൂല്യം ആകണം.
    - ഉപയോഗിക്കാനുള്ള **Region** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാനുള്ള **Storage account** തിരഞ്ഞെടുക്കുക (ആവശ്യമായാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - ഉപയോഗിക്കാനുള്ള **Key vault** തിരഞ്ഞെടുക്കുക (ആവശ്യമായാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - ഉപയോഗിക്കാനുള്ള **Application insights** തിരഞ്ഞെടുക്കുക (ആവശ്യമായാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - ഉപയോഗിക്കാനുള്ള **Container registry** തിരഞ്ഞെടുക്കുക (ആവശ്യമായാൽ പുതിയതായി സൃഷ്ടിക്കുക).

    ![Fill azure machine learning.](../../../../../../translated_images/ml/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** തിരഞ്ഞെടുക്കുക.

6. **Create** തിരഞ്ഞെടുക്കുക.

### Azure Subscription-ൽ GPU ക്വോട്ടാസ് അഭ്യർത്ഥിക്കുക

ഈ ട്യൂട്ടോറിയലിൽ, GPU-കൾ ഉപയോഗിച്ച് Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്ത് ഡിപ്ലോയ് ചെയ്യുന്നതായി നിങ്ങൾ പഠിക്കും. ഫൈൻ-ട്യൂണിംഗിന് *Standard_NC24ads_A100_v4* GPU ഉപയോഗിക്കും, ഇതിന് quota അഭ്യർത്ഥിക്കേണ്ടതുണ്ടാകും. ഡിപ്ലോയ്മെന്റിനായി *Standard_NC6s_v3* GPU ഉപയോഗിക്കും, ഇതിലും quota അഭ്യർത്ഥിക്കേണ്ടതുണ്ട്.

> [!NOTE]
>
> GPU ഓ allocated ചയ്യാനുള്ള യോഗ്യതക്കുള്ളവരായിരിക്കും Pay-As-You-Go സബ്സ്ക്രിപ്ഷനുകൾ (സ്റ്റാൻഡേർഡ് സബ്സ്ക്രിപ്ഷൻ ടൈപ്പ്); ബെനിഫിറ്റ് സബ്സ്ക്രിപ്ഷനുകൾ നിലവിൽ പിന്തുണയ്ക്കുന്നില്ല.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. *Standard NCADSA100v4 Family* ക്വോട്ട ആവശ്യപ്പെടുന്നതിന് താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - ഇടത്തിരിയിലുള്ള ടാബിൽ നിന്നും **Quota** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാനുള്ള **Virtual machine family** തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *Standard_NC24ads_A100_v4* GPU ഉൾക്കൊള്ളുന്ന **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** തിരഞ്ഞെടുക്കുക.
    - നാവിഗേഷൻ മെനുവിൽ നിന്നു **Request quota** തിരഞ്ഞെടുക്കുക.

        ![Request quota.](../../../../../../translated_images/ml/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota പേജിൽ, നിങ്ങൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന **New cores limit** നൽകുക. ഉദാഹരണത്തിന്, 24.
    - Request quota പേജിൽ, GPU ക്വോട്ട അഭ്യർത്ഥിക്കുന്നതിന് **Submit** തിരഞ്ഞെടുക്കുക.

1. *Standard NCSv3 Family* ക്വോട്ട ആവശ്യപ്പെടുന്നതിന് താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - ഇടത്തിരിയിലുള്ള ടാബിൽ നിന്നും **Quota** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാനുള്ള **Virtual machine family** തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *Standard_NC6s_v3* GPU ഉൾക്കൊള്ളുന്ന **Standard NCSv3 Family Cluster Dedicated vCPUs** തിരഞ്ഞെടുക്കുക.
    - നാവിഗേഷൻ മെനുവിൽ നിന്നും **Request quota** തിരഞ്ഞെടുക്കുക.
    - Request quota പേജിൽ, നിങ്ങൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന **New cores limit** നൽകുക. ഉദാഹരണത്തിന്, 24.
    - Request quota പേജിൽ, GPU ക്വോട്ട അഭ്യർത്ഥിക്കുന്നതിന് **Submit** തിരഞ്ഞെടുക്കുക.

### Role Assignment ചേർക്കുക

നിങ്ങളുടെ മോഡലുകൾ ഫൈൻ-ട്യൂൺ ചെയ്ത് ഡിപ്ലോയ് ചെയ്യാൻ, ആദ്യം Use Assigned Managed Identity (UAI) സൃഷ്ടിക്കുകയും അതിന് വേണ്ട അനുവാദങ്ങൾ നൽകുകയും വേണം. ഈ UAI ഡിപ്ലോയ്മെന്റിന് സമയമുള്ള ഓതന്റിക്കേഷനായി ഉപയോഗിക്കപ്പെടും.

#### User Assigned Managed Identity (UAI) സൃഷ്ടിക്കുക

1. പോർട്ടൽ പേജിന്റെ മുകളിൽ ഉള്ള **search bar**-ൽ *managed identities* ടൈപ്പ് ചെയ്ത് പ്രത്യക്ഷപ്പെടുന്ന ഓപ്ഷനുകളിൽ നിന്നും **Managed Identities** തിരഞ്ഞെടുക്കുക.

    ![Type managed identities.](../../../../../../translated_images/ml/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** തിരഞ്ഞെടുക്കുക.

    ![Select create.](../../../../../../translated_images/ml/03-02-select-create.92bf8989a5cd98f2.webp)

1. താഴെപ്പറയുന്ന പ്രവർത്തനങ്ങൾ നിർവ്വഹിക്കുക:

    - നിങ്ങളുടെ Azure **Subscription** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാനുള്ള **Resource group** തിരഞ്ഞെടുക്കുക (ആവശ്യമായാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - ഉപയോഗിക്കാനുള്ള **Region** തിരഞ്ഞെടുക്കുക.
    - **Name** നൽകുക. ഒരേയൊരു മൂല്യം ആയിരിക്കണം.

    ![Select create.](../../../../../../translated_images/ml/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** തിരഞ്ഞെടുക്കുക.

1. **+ Create** തിരഞ്ഞെടുക്കുക.

#### Managed Identity-ക്ക് Contributor Role Assignment ചേർക്കുക

1. സൃഷ്ടിച്ച Managed Identity റിസോഴ്‌സിലേക്ക് പോവുക.

1. ഇടത്തിരിയിലുള്ള ടാബിൽ നിന്നും **Azure role assignments** തിരഞ്ഞെടുക്കുക.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+Add role assignment** തിരഞ്ഞെടുക്കുക.

1. Add role assignment പേജിൽ താഴെപറയുന്നവ ചെയ്യുക:
    - **Scope** ആയി **Resource group** തിരഞ്ഞെടുക്കുക.
    - നിങ്ങളുടെ Azure **Subscription** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാനുള്ള **Resource group** തിരഞ്ഞെടുക്കുക.
    - **Role** ആയി **Contributor** തിരഞ്ഞെടുക്കുക.

    ![Fill contributor role.](../../../../../../translated_images/ml/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** തിരഞ്ഞെടുക്കുക.

#### Managed Identity-ക്ക് Storage Blob Data Reader Role Assignment ചേർക്കുക

1. പോർട്ടൽ പേജിലേയ്ക്ക് മുകളിൽ ഉള്ള **search bar**-ൽ *storage accounts* ടൈപ്പ് ചെയ്ത് പ്രത്യക്ഷപ്പെടുന്ന ഓപ്ഷൻകളിൽ നിന്ന് **Storage accounts** തിരഞ്ഞെടുക്കുക.

    ![Type storage accounts.](../../../../../../translated_images/ml/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. നിങ്ങൾ സൃഷ്ടിച്ച Azure Machine Learning workspace-നെ ബന്ധിപ്പിച്ച് ഉള്ള storage account തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *finetunephistorage*.

1. Add role assignment പേജിലേയ്ക്ക് പോകുന്നതിന് താഴെ പറയുന്ന പ്രവൃത്തി നിർവ്വഹിക്കുക:

    - നിങ്ങൾ സൃഷ്ടിച്ച Azure Storage account-ൽ പോകുക.
    - ഇടത്തിരി ടാബിൽ നിന്നു **Access Control (IAM)** തിരഞ്ഞെടുക്കുക.
    - നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ Add** തിരഞ്ഞെടുക്കുക.
    - വീണ്ടും **Add role assignment** തിരഞ്ഞെടുക്കുക.

    ![Add role.](../../../../../../translated_images/ml/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment പേജിൽ താഴെ പറയുന്ന പ്രവൃത്തി നിർവ്വഹിക്കുക:

    - Role പേജിൽ **search bar**-ൽ *Storage Blob Data Reader* ടൈപ്പ് ചെയ്ത് **Storage Blob Data Reader** തിരഞ്ഞെടുക്കുക.
    - Role പേജിൽ **Next** തിരഞ്ഞെടുക്കുക.
    - Members പേജിൽ **Assign access to**-യിൽ **Managed identity** തിരഞ്ഞെടുക്കുക.
    - Members പേജിൽ **+ Select members** തിരഞ്ഞെടുക്കുക.
    - Select managed identities പേജിൽ നിങ്ങളുടെ Azure **Subscription** തിരഞ്ഞെടുക്കുക.
    - Select managed identities പേജിൽ **Managed identity**-വായി **Manage Identity** തിരഞ്ഞെടുക്കുക.
    - നിങ്ങള് സൃഷ്ടിച്ച Manage Identity തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *finetunephi-managedidentity*.
    - Select managed identities പേജിൽ **Select** തിരഞ്ഞെടുക്കുക.

    ![Select managed identity.](../../../../../../translated_images/ml/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** തിരഞ്ഞെടുക്കുക.

#### Managed Identity-ക്ക് AcrPull Role Assignment ചേർക്കുക

1. പോർട്ടൽ പേജിലേയ്ക്ക് മുകളിൽ ഉള്ള **search bar**-ൽ *container registries* ടൈപ്പ് ചെയ്ത് പ്രത്യക്ഷപ്പെടുന്ന ഓപ്ഷനുകളിൽ നിന്നും **Container registries** തിരഞ്ഞെടുക്കുക.

    ![Type container registries.](../../../../../../translated_images/ml/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. നിങ്ങളുടെ Azure Machine Learning workspace-നെ ബന്ധിപ്പിച്ച container registry തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *finetunephicontainerregistry*.

1. Add role assignment പേജിലേയ്ക്ക് പോകുവാൻ താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ നിർവ്വഹിക്കുക:

    - ഇടത്തിരി ടാബിൽ നിന്നു **Access Control (IAM)** തിരഞ്ഞെടുക്കുക.
    - നാവിഗേഷൻ മെനുവിൽ നിന്ന് **+ Add** തിരഞ്ഞെടുക്കുക.
    - വീണ്ടും **Add role assignment** തിരഞ്ഞെടുക്കുക.

1. Add role assignment പേജിൽ താഴെ പറയുന്ന പ്രവൃത്തി നിർവ്വഹിക്കുക:

    - Role പേജിൽ **search bar**-ൽ *AcrPull* ടൈപ്പ് ചെയ്ത് **AcrPull** തിരഞ്ഞെടുക്കുക.
    - Role പേജിൽ **Next** തിരഞ്ഞെടുക്കുക.
    - Members പേജിൽ **Assign access to**-ൽ **Managed identity** തിരഞ്ഞെടുക്കുക.
    - Members പേജിൽ **+ Select members** തിരഞ്ഞെടുക്കുക.
    - Select managed identities പേജിൽ നിങ്ങളുടെ Azure **Subscription** തിരഞ്ഞെടുക്കുക.
    - Select managed identities പേജിൽ **Managed identity**-വായി **Manage Identity** തിരഞ്ഞെടുക്കുക.
    - നിങ്ങൾ സൃഷ്ടിച്ച Manage Identity തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *finetunephi-managedidentity*.
    - Select managed identities പേജിൽ **Select** തിരഞ്ഞെടുക്കുക.
    - **Review + assign** തിരഞ്ഞെടുക്കുക.

### പ്രോജക്റ്റ് സജ്ജമാക്കുക

ഫൈൻ-ട്യൂണിനായി ആവശ്യമായ ഡാറ്റാസെറ്റുകൾ ഡൗൺലോഡ് ചെയ്യുന്നതിനായി, നിങ്ങൾ ഒരു ലോക്കൽ എൻവയൺമെന്റ് സജ്ജമാക്കും.

ഈ അභ്യാസത്തിൽ, നിങ്ങൾ

- ഉള്ളിൽ ജോലി ചെയ്യാനുള്ള ഫോൾഡർ സൃഷ്ടിക്കും.
- ഒരു വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കും.
- ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യും.
- ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യുന്നതിനുള്ള *download_dataset.py* ഫയൽ സൃഷ്ടിക്കും.

#### ജോലി ചെയ്യാനുള്ള ഫോൾഡർ സൃഷ്ടിക്കുക

1. ഒരു ടെർമിനൽ വിൻഡോ തുറന്ന് ഡിഫോൾട്ട് പാത്തിൽ *finetune-phi* എന്ന പേരിൽ ഫോൾഡർ സൃഷ്ടിക്കുന്നതിന് താഴെ പറയുന്ന കമാൻഡ് ടൈപ്പ് ചെയ്യുക.

    ```console
    mkdir finetune-phi
    ```

2. നിങ്ങൾ സൃഷ്ടിച്ച *finetune-phi* ഫോൾഡറിലേക്ക് നാവിഗേറ്റ് ചെയ്യുന്നതിന് നിങ്ങളുടെ ടെർമിനലിൽ താഴെ പറയുന്ന കമാൻഡ് ടൈപ്പ് ചെയ്യുക.

    ```console
    cd finetune-phi
    ```

#### വെർച്വൽ എൻവയേണ്മെന്റ് സൃഷ്ടിക്കുക

1. നിങ്ങളുടെ ടെർമിനലിൽ *.venv* എന്ന പേരിൽ ഒരു വെർച്വൽ എൻവയൺമെന്റ് സൃഷ്ടിക്കുന്നതിന് താഴെ പറയുന്ന കമാൻഡ് ടൈപ്പ് ചെയ്യുക.
    ```console
    python -m venv .venv
    ```

2. നിങ്ങളുടെ ടെർമിനലിനുള്ളിൽ താഴെ കൊടുത്തിരിക്കുന്ന കമാൻഡ് ടൈപ്പ് ചെയ്ത് വിർച്വൽ എൻവൈരൺമെന്റ് സജീവമാക്കുക.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> ഇത് പ്രവർത്തിച്ചാൽ, കമാൻഡ് പ്രോമ്പ്റ്റിന് മുമ്പ് *(.venv)* കാണേണ്ടതാണ്.

#### ആവശ്യമായ പാക്കറുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

1. ആവശ്യമായ പാക്കറുകൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ നിങ്ങളുടെ ടെർമിനലിൽ താഴെ കൊടുത്തിരിക്കുന്ന കമാൻഡുകൾ ടൈപ്പ് ചെയ്യുക.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` സൃഷ്ടിക്കുക

> [!NOTE]
> പൂർണ്ണ ഫോൾഡർ ഘടന:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** തുറക്കുക.

1. മെനു ബാറിൽ നിന്നു **File** തിരഞ്ഞെടുക്കുക.

1. **Open Folder** തിരഞ്ഞെടുത്തുകൊടുക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച *finetune-phi* ഫോള്ഡർ തിരഞ്ഞെടുക്കുക, അത് *C:\Users\yourUserName\finetune-phi* ലൊക്കേറ്റഡ് ആണ്.

    ![Select the folder that you created.](../../../../../../translated_images/ml/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code ലെ ഇടത് പാനലിൽ റൈറ്റ്-ക്ലിക് ചെയ്ത് **New File** തിരഞ്ഞെടുക്കുക, പുതിയ ഫയൽ *download_dataset.py* എന്ന പേരിൽ സൃഷ്ടിക്കുക.

    ![Create a new file.](../../../../../../translated_images/ml/04-02-create-new-file.cf9a330a3a9cff92.webp)

### ഫൈൻ-ട്യൂണിംഗിനായി ഡാറ്റാസെറ്റ് ഒരുക്കുക

ഈ അവസരത്തിൽ, നിങ്ങൾ *download_dataset.py* ഫയൽ റൺ ചെയ്ത് *ultrachat_200k* ഡാറ്റാസെറ്റുകൾ ലൊക്കൽ എൻവൈരൺമെന്റിലേക്ക് ഡൗൺലോഡ് ചെയ്യും. പിന്നീട് ഈ ഡാറ്റാസെറ്റുകൾ Azure Machine Learning-ലുള്ള Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യാൻ ഉപയോഗിക്കും.

ഈ പ്രവൃത്തിയിൽ നിങ്ങൾ:

- *download_dataset.py* ഫയലിൽ ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യാനുള്ള കോഡ് ചേർക്കും.
- *download_dataset.py* ഫയൽ റൺ ചെയ്ത് ഡാറ്റാസെറ്റുകൾ ലൊക്കലിലേക്ക് ഡൗൺലോഡ് ചെയ്യും.

#### *download_dataset.py* ഉപയോഗിച്ച് ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യുക

1. Visual Studio Code-ലിൽ *download_dataset.py* ഫയൽ തുറക്കുക.

1. താഴെ കാണിച്ചിരിക്കുന്ന കോഡ് *download_dataset.py* ഫയലിൽ ചേർക്കുക.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # നിഷ്കർഷിച്ച പേര്, കോൺഫിഗറേഷനും സ്പ്ലിറ്റ് അനുപാതവും ഉപയോഗിച്ച് ഡാറ്റാസെറ്റ് ലോഡ് ചെയ്യുക
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # ഡാറ്റാസെറ്റ് ട്രെയിൻ, ടെസ്റ്റ് സെറ്റുകളായി വിഭജിക്കുക (80% ട്രെയിൻ, 20% ടെസ്റ്റ്)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # ഡയറക്ടറി നിലവിലില്ലെങ്കിൽ സൃഷ്‌ടിക്കുക
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # ഫയൽ എഴുതൽ മോഡിൽ തുറക്കുക
        with open(filepath, 'w', encoding='utf-8') as f:
            # ഡാറ്റാസെറ്റിലെ ഓരോ റെക്കോർഡും തരണം ചെയ്യുക
            for record in dataset:
                # റെക്കോർഡ് JSON ഒബ്‌ജക്റ്റായി ഡമ്പ് ചെയ്ത് ഫയൽത്ത് എഴുതുക
                json.dump(record, f)
                # റെക്കോർഡുകൾ വേർതിരിക്കാൻ ഒരു ന്യുവ്ലൈൻ അക്ഷരം എഴുതുക
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ULTRACHAT_200k ഡാറ്റാസെറ്റ് ഒരു പ്രത്യേക കോൺഫിഗറേഷൻ, സ്പ്ലിറ്റ് അനുപാതത്തോടെ ലോഡ് ചെയ്ത് വിഭജിക്കുക
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # സ്പ്ലിറ്റിൽ നിന്നും ട്രെയിൻ, ടെസ്റ്റ് ഡാറ്റാസെറ്റുകൾ എടുക്കുക
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ട്രെയിൻ ഡാറ്റാസെറ്റ് JSONL ഫയലായി സൂക്ഷിക്കുക
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # ടെസ്റ്റ് ഡാറ്റാസെറ്റ് വേറെ JSONL ഫയലായി സൂക്ഷിക്കുക
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. സ്ക്രിപ്റ്റ് റൺ ചെയ്ത് ഡാറ്റാസെറ്റ് നിങ്ങളുടെ ലൊക്കൽ എൻവൈരൺമെന്റിൽ ഡൗൺലോഡ് ചെയ്യാൻ ടെർമിനലിൽ താഴെ കൊടുത്തിരിക്കുന്ന കമാൻഡ് ടൈപ്പ് ചെയ്യുക.

    ```console
    python download_dataset.py
    ```

1. ഡാറ്റാസെറ്റുകൾ വിജയകരമായി നിങ്ങളുടെ ലൊക്കൽ *finetune-phi/data* ഡയറക്ടറിയിൽ സെവ് ചെയ്തിട്ടുണ്ടെന്ന് പരിശോധിക്കുക.

> [!NOTE]
>
> #### ഡാറ്റാസെറ്റ് വലിപ്പവും ഫൈൻ-ട്യൂണിംഗ് സമയവും സംബന്ധിച്ച കുറിപ്പ്
>
> ഈ ട്യൂട്ടോറിയലിൽ, നിങ്ങൾ ഡാറ്റാസെറ്റിന്റെ 1% മാത്രം ഉപയോഗിക്കുന്നു (`split='train[:1%]'`). ഇത് ഡാറ്റയുടെ അളവ് കുറക്കുകയും അപ്ലോഡ് ചിത്രവും ഫൈൻ-ട്യൂണിംഗ് പ്രക്രിയയും വേഗത്തിലാക്കുകയും ചെയ്യുന്നു. പരിശീലന സമയത്തിന്റെ ഉത്തമവും മോഡൽ പ്രകടനത്തിനും ഇടയിലെ മികച്ച ഒത്തുചേർപ്പ് കണ്ടെത്താൻ നിങ്ങൾ ടിശ്ചം ചെയ്യാവുന്നതാണ്. ഡാറ്റാസെറ്റിന്റെ കുറച്ച് സൂക്ഷ്മ ഭാഗം ഉപയോഗിക്കുന്നത് ഫൈൻ-ട്യൂണിംഗിന് ആവശ്യമായ സമയം കുറയ്ക്കാൻ സഹായിക്കുന്നു, ഇത് ട്യൂട്ടോറിയലിന് കൂടുതൽ കൈകാര്യം ചെയ്യാവുന്നതാക്കുന്നു.

## സീനാരിയോ 2: Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്ത് Azure Machine Learning Studio-ലിൽ ഡിപ്ലോയ് ചെയ്യുക

### Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുക

ഈ സാഹചര്യത്തിൽ, നിങ്ങൾ Azure Machine Learning Studio-യിൽ Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യും.

ഈ പ്രവൃത്തിയിൽ നിങ്ങൾ:

- ഫൈൻ-ട്യൂണിംഗിനായി കമ്പ്യൂട്ടർ ക്ലസ്റ്റർ സൃഷ്ടിക്കും.
- Azure Machine Learning Studio-യിൽ Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യും.

#### ഫൈൻ-ട്യൂണിംഗിനായി കമ്പ്യൂട്ടർ ക്ലസ്റ്റർ സൃഷ്ടിക്കുക

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. ഇടത് പാനലിൽ നിന്നു **Compute** തിരഞ്ഞെടുക്കുക.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **Compute clusters** തിരഞ്ഞെടുക്കുക.

1. **+ New** തെരഞ്ഞെടുക്കുക.

    ![Select compute.](../../../../../../translated_images/ml/06-01-select-compute.a29cff290b480252.webp)

1. താഴെ കൊടുത്തിരിക്കുന്ന പ്രവർത്തനങ്ങൾ നിർവഹിക്കുക:

    - നിങ്ങൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന **Region** തിരഞ്ഞെടുക്കുക.
    - **Virtual machine tier** യായി **Dedicated** തിരഞ്ഞെടുക്കുക.
    - **Virtual machine type** GPU ആയി തിരഞ്ഞെടുക്കുക.
    - **Virtual machine size** ഫിൽറ്ററിൽ **Select from all options** തിരഞ്ഞെടുക്കുക.
    - **Virtual machine size** യായി **Standard_NC24ads_A100_v4** തിരഞ്ഞെടുക്കുക.

    ![Create cluster.](../../../../../../translated_images/ml/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** തിരഞ്ഞെടുക്കുക.

1. താഴെ കൊടുത്തിരിക്കുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - **Compute name** നൽകുക. ഇത് വ്യത്യസ്തമായ മൂല്യം ആയിരിക്കണം.
    - **Minimum number of nodes** 0 ആയി തിരഞ്ഞെടുക്കുക.
    - **Maximum number of nodes** 1 ആയി തിരഞ്ഞെടുക്കുക.
    - **Idle seconds before scale down** 120 ആയി തിരഞ്ഞെടുക്കുക.

    ![Create cluster.](../../../../../../translated_images/ml/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** തിരഞ്ഞെടുക്കുക.

#### Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുക

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച Azure Machine Learning വർക്ക്സ്പേസ് തിരഞ്ഞെടുക്കുക.

    ![Select workspace that you created.](../../../../../../translated_images/ml/06-04-select-workspace.a92934ac04f4f181.webp)

1. താഴെ കൊടുത്തിരിക്കുന്ന പ്രവർത്തനങ്ങൾ നടത്തുക:

    - ഇടത് പാനലിൽ നിന്നു **Model catalog** തിരഞ്ഞെടുക്കുക.
    - **search bar** ൽ *phi-3-mini-4k* ടൈപ്പ് ചെയ്ത് പ്രത്യക്ഷമാകുന്ന ഓപ്ഷനുകളിൽ നിന്നു **Phi-3-mini-4k-instruct** തിരഞ്ഞെടുക്കുക.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/ml/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. നാവിഗേഷൻ മെനുവിൽ **Fine-tune** തിരഞ്ഞെടുക്കുക.

    ![Select fine tune.](../../../../../../translated_images/ml/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. താഴെ കൊടുത്തിരിക്കുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - **Select task type** **Chat completion** ആയി തിരഞ്ഞെടുക്കുക.
    - **+ Select data** തിരഞ്ഞെടുക്കുക, **Training data** അപ്‌ലോഡ് ചെയ്യാൻ.
    - Validation data അപ്‌ലോഡ് ടൈപ്പ് **Provide different validation data** ആയി തിരഞ്ഞെടുത്തുക.
    - **+ Select data** തിരഞ്ഞെടുക്കുക, **Validation data** അപ്‌ലോഡ് ചെയ്യാൻ.

    ![Fill fine-tuning page.](../../../../../../translated_images/ml/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> **Advanced settings** തിരഞ്ഞെടുക്കാൻ കഴിയും, ഇത് learning_rate, lr_scheduler_type പോലുള്ള കോൺഫിഗറേഷനുകൾ കസ്റ്റമൈസ് ചെയ്യാനും ഫൈൻ-ട്യൂണിംഗ് പ്രക്രിയ നിങ്ങളുടെ ആവശ്യങ്ങളിൽ അനുസരിച്ച് മെച്ചപ്പെടുത്താനും സഹായിക്കും.

1. **Finish** തിരഞ്ഞെടുക്കുക.

1. ഈ പ്രവർത്തിയിൽ, നിങ്ങൾ വിജയകരമായി Azure Machine Learning ഉപയോഗിച്ച് Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്തു. ഫൈൻ-ട്യൂണിംഗ് പ്രക്രിയക്ക് നല്ലൊരു സമയം എടുക്കാവുന്നതാണ്. ഫൈൻ-ട്യൂൺ ജോബ് റൺ ചെയ്ത ശേഷം, അത് പൂർത്തിയാകുമ്പോൾ വരെ കാത്തിരിക്കണം. Azure Machine Learning Workspace-ന്റെ ഇടത് പാനലിലുള്ള Jobs ടാബിൽ നിങ്ങൾ ഫൈൻ-ട്യൂൺ ജോബിന്റെ സ്റ്റാറ്റസ് നിരീക്ഷിക്കാം. അടുത്ത ഭാഗങ്ങളിൽ, നിങ്ങൾ ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡലം ഡിപ്ലോയ് ചെയ്ത് Prompt flow-വുമായോഴിച്ചു നടപ്പിലാക്കും.

    ![See finetuning job.](../../../../../../translated_images/ml/06-08-output.2bd32e59930672b1.webp)

### ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡൽ ഡിപ്ലോയ് ചെയ്യുക

ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡൽ Prompt flow-വുമായോഴിച്ചു സംയോജിപ്പിക്കാൻ, മോഡൽ റിയൽ-ടൈം ഇൻഫറൻസിന് പ്രാപ്യമായിരിക്കണമെന്നു ഡിപ്ലോയ് ചെയ്യേണ്ടതുണ്ട്. ഈ പ്രക്രിയയിൽ മോഡൽ രജിസ്റ്റർ ചെയ്യുക, ഓൺലൈൻ എൻഡ്പോയിന്റ് സൃഷ്ടിക്കുക, മോഡൽ ഡിപ്ലോയ് ചെയ്യുക എന്നിവ ഉൾപ്പെടുന്നു.

ഈ പ്രവർത്തിയിൽ നിങ്ങൾ:

- Azure Machine Learning വർക്ക്സ്പേസിൽ ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ രജിസ്റ്റർ ചെയ്യും.
- ഒരു ഓൺലൈൻ എൻഡ്പോയിന്റ് സൃഷ്ടിക്കും.
- രജിസ്റ്റർ ചെയ്ത ഫൈൻ-ಟ്യൂൺ ചെയ്ത Phi-3 മോഡൽ ഡിപ്ലോയ് ചെയ്യും.

#### ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ രജിസ്റ്റർ ചെയ്യുക

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച Azure Machine Learning വർക്ക്സ്പേസ് തിരഞ്ഞെടുക്കുക.

    ![Select workspace that you created.](../../../../../../translated_images/ml/06-04-select-workspace.a92934ac04f4f181.webp)

1. ഇടത് പാനലിൽ നിന്നു **Models** തിരഞ്ഞെടുക്കുക.

1. **+ Register** തിരഞ്ഞെടുക്കുക.

1. **From a job output** തിരഞ്ഞെടുക്കുക.

    ![Register model.](../../../../../../translated_images/ml/07-01-register-model.ad1e7cc05e4b2777.webp)

1. നിങ്ങൾ സൃഷ്ടിച്ച ജോബ് തിരഞ്ഞെടുക്കുക.

    ![Select job.](../../../../../../translated_images/ml/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** തിരഞ്ഞെടുക്കുക.

1. **Model type** MLflow ആയി തിരഞ്ഞെടുക്കുക.

1. **Job output** തിരഞ്ഞെടുക്കപ്പെട്ടതാണെന്ന് ഉറപ്പാക്കുക; അത് സ്വാഭാവികമായി തിരഞ്ഞെടുത്തിരിക്കണം.

    ![Select output.](../../../../../../translated_images/ml/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** തിരഞ്ഞെടുക്കുക.

3. **Register** തിരഞ്ഞെടുക്കുക.

    ![Select register.](../../../../../../translated_images/ml/07-04-register.fd82a3b293060bc7.webp)

4. നിങ്ങൾ രജിസ്റ്റർ ചെയ്ത മോഡൽ കാണാൻ ഇടത് പാനലിൽ **Models** മെനു തുറക്കുക.

    ![Registered model.](../../../../../../translated_images/ml/07-05-registered-model.7db9775f58dfd591.webp)

#### ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ ഡിപ്ലോയ് ചെയ്യുക

1. നിങ്ങൾ സൃഷ്ടിച്ച Azure Machine Learning വർക്ക്സ്പേസ് സന്ദർശിക്കുക.

1. ഇടത് പാനലിൽ **Endpoints** തിരഞ്ഞെടുക്കുക.

1. നാവിഗേഷൻ മെനുവിൽ **Real-time endpoints** തിരഞ്ഞെടുക്കുക.

    ![Create endpoint.](../../../../../../translated_images/ml/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** തിരഞ്ഞെടുക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച രജിസ്റ്റർ ചെയ്ത മോഡൽ തിരഞ്ഞെടുക്കുക.

    ![Select registered model.](../../../../../../translated_images/ml/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** തിരഞ്ഞെടുക്കുക.

1. താഴെ കൊടുത്തിരിക്കുന്ന പ്രവർത്തനങ്ങൾ നിർവഹിക്കുക:

    - **Virtual machine** *Standard_NC6s_v3* ആയി തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന **Instance count** തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *1*.
    - **Endpoint** പുതിയതായി സൃഷ്ടിക്കാൻ **New** തിരഞ്ഞെടുക്കുക.
    - **Endpoint name** നൽകുക. ഇത് വ്യത്യസ്തമായ മൂല്യം ആയിരിക്കണം.
    - **Deployment name** നൽകുക. ഇത് വ്യത്യസ്തമായ മൂല്യം ആയിരിക്കണം.

    ![Fill the deployment setting.](../../../../../../translated_images/ml/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** തിരഞ്ഞെടുക്കുക.

> [!WARNING]
> നിങ്ങളുടെ അക്കൗണ്ടിൽ അധിക ചാർജുകൾ ഒഴിവാക്കാൻ, Azure Machine Learning വർക്ക്സ്പേസിൽ സൃഷ്ടിച്ച എൻഡ്പോയിന്റ് നീക്കം ചെയ്യുക.
>

#### Azure Machine Learning Workspace-ലിലെ ഡിപ്ലോയ്മെന്റ് സ്റ്റാറ്റസ് പരിശോധിക്കുക

1. നിങ്ങൾ സൃഷ്ടിച്ച Azure Machine Learning വർക്ക്സ്പേസ് സന്ദർശിക്കുക.

1. ഇടത് പാനലിൽ **Endpoints** തിരഞ്ഞെടുക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച എൻഡ്പോയിന്റ് തിരഞ്ഞെടുക്കുക.

    ![Select endpoints](../../../../../../translated_images/ml/07-09-check-deployment.325d18cae8475ef4.webp)

1. ഈ പേജിൽ, നിങ്ങൾ എൻഡ്പോയിന്റുകൾ ഡിപ്ലോയ് ചെയ്യുന്നതിനിടെ നിയന്ത്രിക്കാം.

> [!NOTE]
> ഡിപ്ലോയ്മെന്റ് പൂർത്തിയായതിനുശേഷം, **Live traffic** 100% ആയി സജ്ജമാക്കണമെന്ന് ഉറപ്പുവരുത്തുക. അല്ലെങ്കിൽ **Update traffic** തിരഞ്ഞെടുക്കി ട്രാഫിക് ക്രമീകരണങ്ങൾ പുതുക്കുക. ട്രാഫിക് 0% ആണെങ്കിൽ മോഡൽ പരിശോധിക്കാൻ കഴിയില്ല.
>
> ![Set traffic.](../../../../../../translated_images/ml/07-10-set-traffic.085b847e5751ff3d.webp)
>

## സീനാരിയോ 3: Prompt flow-വുമായോഴിച്ചുള്ള സംയോജനം және Microsoft Foundry-യിൽ നിങ്ങളുടെ കസ്റ്റം മോഡലോടെ ചാറ്റ് ചെയ്യുക

### കസ്റ്റം Phi-3 മോഡൽ Prompt flow-വുമായോഴിച്ചു സംയോജിപ്പിക്കുക

ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ വിജയകരമായി ഡിപ്ലോയുചെയ്ത ശേഷം, നിങ്ങൾ അതിനെ Prompt Flow-വുമായോഴിച്ചു സംയോജിപ്പിക്കാം. ഈ മോഡലിനെ റിയൽ-ടൈം ആപ്ലിക്കേഷനുകളിൽ ഉപയോഗപ്പെടുത്താൻ സാധിക്കും, വിവിധ ഇന്ററാക്ടീവ് ടാസ്കുകൾ നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലിൽ നടപ്പിലാക്കാം.

ഈ പ്രവർത്തിയിൽ നിങ്ങൾ:

- Microsoft Foundry ഹബ് സൃഷ്ടിക്കും.
- Microsoft Foundry പ്രോജക്ട് സൃഷ്ടിക്കും.
- Prompt flow സൃഷ്ടിക്കും.
- ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡലിനായി ഒരു കസ്റ്റം കണക്ട് ചേർക്കും.
- നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലോടു ചാറ്റ് നടത്താൻ Prompt flow സജ്ജമാക്കും.

> [!NOTE]
> Azure ML Studio ഉപയോഗിച്ചു Promptflow-വുമായോഴിച്ചുള്ള സംയോജനം നടത്താം. ഈ സമാന സംയോജനം Azure ML Studio-ഉം ബാധകമാണ്.

#### Microsoft Foundry ഹബ് സൃഷ്ടിക്കുക

പ്രോജക്ട് സൃഷ്ടിക്കുന്നതിന് മുമ്പ് ഒരു ഹബ് സൃഷ്ടിക്കേണ്ടതാണ്. ഹബ് ഒരു_RESOURCES_ഗ്രൂപ്പായി പ്രവർത്തിക്കുന്നു, Microsoft Foundryയിൽ ഉള്ള പല പ്രോജക്ടുകളും അതിന്റെ കീഴിൽ എന്നിവയെ ക്രമീകരിക്കുകയും നിയന്ത്രിക്കാനും സഹായിക്കുന്നു.
1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) സന്ദർശിക്കുക.

1. ഇടത് വശത്തെ ടാബിൽ നിന്നും **All hubs** തിരഞ്ഞെടുക്കുക.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **+ New hub** തിരഞ്ഞെടുക്കുക.

    ![Create hub.](../../../../../../translated_images/ml/08-01-create-hub.8f7dd615bb8d9834.webp)

1. താഴെ പറയുന്ന കാര്യങ്ങൾ ചെയ്യുക:

    - **Hub name** നൽകി. ഇത് അന്തരീക്ഷമായ മൂല്യം ആയിരിക്കണം.
    - നിങ്ങളുടെ Azure **Subscription** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാൻ വേണ്ടി **Resource group** തിരഞ്ഞെടുക്കുക (താത്കാലികമായി പുതിയതായി സൃഷ്‌ടിക്കാം).
    - നിങ്ങൾക്ക് ഉപയോഗിക്കാൻ താല്പര്യമുള്ള **Location** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാൻ **Connect Azure AI Services** തിരഞ്ഞെടുക്കുക (പുതിയതായി സൃഷ്‌ടിക്കാം).
    - **Connect Azure AI Search**-ഇൽ **Skip connecting** തിരഞ്ഞെടുക്കുക.

    ![Fill hub.](../../../../../../translated_images/ml/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** തിരഞ്ഞെടുക്കുക.

#### Microsoft Foundry പ്രോജക്ട് സൃഷ്‌ടിക്കുക

1. നിങ്ങൾ സൃഷ്‌ടിച്ച ഹബിൽ, ഇടത് വശത്തെ ടാബിൽ നിന്നും **All projects** തിരഞ്ഞെടുക്കുക.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **+ New project** തിരഞ്ഞെടുക്കുക.

    ![Select new project.](../../../../../../translated_images/ml/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** നൽകി. ഇത് അന്തരീക്ഷമായ മൂല്യം ആയിരിക്കണം.

    ![Create project.](../../../../../../translated_images/ml/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** തിരഞ്ഞെടുക്കുക.

#### ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡലിനായുള്ള കസ്റ്റം കണക്ഷൻ ചേർക്കുക

നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലിനെ Prompt flow-ലോടു സംയോജിപ്പിക്കാൻ, മോഡലിന്റെ എൻഡ്‌പോയിന്റും കീയും കസ്റ്റം കണക്ഷനിൽ സേവ് ചെയ്യേണ്ടതാണ്. ഈ ക്രമീകരണം Prompt flow-ൽ നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലിലേക്ക് പ്രവേശനം ഉറപ്പാക്കും.

#### ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡലിന്റെ api കീയും എൻഡ്‌പോയിന്റ്(uri)യും സെറ്റ് ചെയ്യുക

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്‌ടിച്ച Azure മെഷീൻ ലേണിംഗ് വർക്ക്‌സ്‌പേസിലേക്ക് നോക്കുക.

1. ഇടത് വശത്തെ ടാബിൽ നിന്നും **Endpoints** തിരഞ്ഞെടുക്കുക.

    ![Select endpoints.](../../../../../../translated_images/ml/08-06-select-endpoints.aff38d453bcf9605.webp)

1. നിങ്ങൾ സൃഷ്‌ടിച്ച എൻഡ്‌പോയിന്റ് തിരഞ്ഞെടുക്കുക.

    ![Select endpoints.](../../../../../../translated_images/ml/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **Consume** തിരഞ്ഞെടുക്കുക.

1. നിങ്ങളുടെ **REST endpoint**യും **Primary key**യും കോപ്പി ചെയ്യുക.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ml/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### കസ്റ്റം കണക്ഷൻ ചേർക്കുക

1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്‌ടിച്ച Microsoft Foundry പ്രോജക്ടിലേക്ക് നോക്കുക.

1. സൃഷ്‌ടിച്ച പ്രോജക്ടിൽ, ഇടത് വശത്തെ ടാബിൽ നിന്നും **Settings** തിരഞ്ഞെടുക്കുക.

1. **+ New connection** തിരഞ്ഞെടുക്കുക.

    ![Select new connection.](../../../../../../translated_images/ml/08-09-select-new-connection.02eb45deadc401fc.webp)

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **Custom keys** തിരഞ്ഞെടുക്കുക.

    ![Select custom keys.](../../../../../../translated_images/ml/08-10-select-custom-keys.856f6b2966460551.webp)

1. താഴെ പറയുന്ന കാര്യങ്ങൾ ചെയ്യുക:

    - **+ Add key value pairs** തിരഞ്ഞെടുക്കുക.
    - കീ നാമമായി **endpoint** നൽകുകയും Azure ML Studio-യിൽ നിന്ന് കോപ്പി ചെയ്ത എൻഡ്‌പോയിന്റ് മൂല്യം വാല്യുവായി പേസ്റ്റ് ചെയ്യുക.
    - വീണ്ടും **+ Add key value pairs** തിരഞ്ഞെടുക്കുക.
    - കീ നാമമായി **key** നൽകി, Azure ML Studio-യിൽ നിന്ന് കോപ്പി ചെയ്ത കീ വാല്യുവായി പേസ്റ്റ് ചെയ്യുക.
    - കീകൾ ചേർത്തശേഷം, കീ പ്രദർശനം തടയാൻ **is secret** തിരഞ്ഞെടുക്കുക.

    ![Add connection.](../../../../../../translated_images/ml/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** തിരഞ്ഞെടുക്കുക.

#### Prompt flow സൃഷ്‌ടിക്കുക

നിങ്ങൾ Microsoft Foundry-യിൽ ഒരു കസ്റ്റം കണക്ഷൻ ചേർത്തു കഴിഞ്ഞു. ഇനി, താഴെ പറയുന്ന ഘടികാരങ്ങൾ ഉപയോഗിച്ച് Prompt flow സൃഷ്‌ടിക്കാം. അതിന്റെ ശേഷം, ഈ Prompt flow-നെ കസ്റ്റം കണക്ഷനുമായി ബന്ധിപ്പിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ Prompt flow-ൽ ഉപയോഗിക്കാം.

1. നിങ്ങൾ സൃഷ്‌ടിച്ച Microsoft Foundry പ്രോജക്ടിലേക്ക് പോകുക.

1. ഇടത് വശത്തെ ടാബിൽ നിന്നും **Prompt flow** തിരഞ്ഞെടുക്കുക.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **+ Create** തിരഞ്ഞെടുക്കുക.

    ![Select Promptflow.](../../../../../../translated_images/ml/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **Chat flow** തിരഞ്ഞെടുക്കുക.

    ![Select chat flow.](../../../../../../translated_images/ml/08-13-select-flow-type.2ec689b22da32591.webp)

1. ഉപയോഗിക്കാനുള്ള **Folder name** നൽകുക.

    ![Enter name.](../../../../../../translated_images/ml/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** തിരഞ്ഞെടുക്കുക.

#### Prompt flow ഇതിന്റെ കസ്റ്റം Phi-3 മോഡലുമായി ചാറ്റ് ചെയ്യാൻ സജ്ജീകരിക്കുക

ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡലിനെ Prompt flow-ലിൽ സംയോജിപ്പിക്കേണ്ടതാണ്. എന്നാൽ, നിലവിലുള്ള Prompt flow ഈ ആവശ്യത്തിനു രൂപകല്പന ചെയ്തതല്ല. അതിനാൽ, Prompt flow പുനഃരൂപീകരിച്ച് കസ്റ്റം മോഡലിന്റെ സംയോജനം സാധ്യമാക്കണം.

1. Prompt flow-ലിൽ, നിലവിലുള്ള ഫ്ലോ പുനർനിർമിക്കാൻ താഴെ പറയുന്ന കാര്യങ്ങൾ ചെയ്യുക:

    - **Raw file mode** തിരഞ്ഞെടുക്കുക.
    - *flow.dag.yml* ഫയലിലുള്ള എല്ലാ കോഡുകളും ഇല്ലാതാക്കുക.
    - താഴെ കൊടുത്ത കോഡ് *flow.dag.yml* ഫയലിൽ ചേർക്കുക.

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

    - **Save** തിരഞ്ഞെടുക്കുക.

    ![Select raw file mode.](../../../../../../translated_images/ml/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Prompt flow-ൽ കസ്റ്റം Phi-3 മോഡൽ ഉപയോഗിക്കാൻ *integrate_with_promptflow.py* ഫയലിൽ താഴെ കൊടുത്ത കോഡ് ചേർക്കുക.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ലോഗിംഗ് ക്രമീകരണം
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

        # "connection" ഒരു കസ്റ്റം കണക്ഷന്റെ പേര് ആണ്, "endpoint", "key" മുണ്ടല് കണക്ഷനിലെ കീകൾ ആണ്
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
            
            # പൂർണ്ണമായ JSON പ്രതികരണം ലോഗ് ചെയ്യുക
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

    ![Paste prompt flow code.](../../../../../../translated_images/ml/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry-ൽ Prompt flow ഉപയോഗിക്കുന്നതിനെ കുറിച്ചുള്ള കൂടുതൽ വിശദമായ വിവരങ്ങൾക്ക്, നിങ്ങൾക്ക് [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) സന്ദർശിക്കാം.

1. **Chat input**, **Chat output** തിരഞ്ഞെടുക്കുക, നിങ്ങളുടെ മോഡലുമായി ചാറ്റ് നടത്താനായി.

    ![Input Output.](../../../../../../translated_images/ml/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. ഇപ്പോൾ, നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലുമായി ചാറ്റ് ചെയ്യാൻ നിങ്ങളാണ് സജ്ജം. അടുത്ത വ്യായാമത്തിൽ, നിങ്ങൾക്ക് Prompt flow ആരംഭിക്കാനും ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡലുമായി ചാറ്റ് നടത്താനും ഒരുങ്ങും.

> [!NOTE]
>
> പുനഃരൂപീകരിച്ച ഫ്ലോ താഴെ കാണുന്ന ചിത്രത്തോട് സാമ്യമാകണം:
>
> ![Flow example.](../../../../../../translated_images/ml/08-18-graph-example.d6457533952e690c.webp)
>

### നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലുമായി ചാറ്റ് ചെയ്യുക

നിങ്ങൾ ഫൈൻ-ട്യൂൺ ചെയ്ത നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലിനെ Prompt flow-ലിൽ സംയോജിപ്പിച്ചതിനാൽ, ഇപ്പോൾ അതുമായി ആശയവിനിമയം ആരംഭിക്കാൻ തയ്യാറാണ്. ഈ വ്യായാമം, Prompt flow ഉപയോഗിച്ച് നിങ്ങളുടേ മോഡലുമായി ചാറ്റ് ആരംഭിക്കുന്നതിനുള്ള ക്രമീകരണവും നടപടിക്രമവും വിശദീകരിക്കും. ഈ ഘടികാരങ്ങൾ പിന്തുടർന്ന്, ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡലിന്റെ സമ്പൂർണ ശേഷികൾ വിവിധകാര്യങ്ങൾക്കും സംഭാഷണങ്ങൾക്കും ഉപയോഗിക്കാം.

- Prompt flow ഉപയോഗിച്ച് നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലുമായി ചാറ്റ് ചെയ്യുക.

#### Prompt flow ആരംഭിക്കുക

1. Prompt flow ആരംഭിക്കാൻ **Start compute sessions** തിരഞ്ഞെടുക്കുക.

    ![Start compute session.](../../../../../../translated_images/ml/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. പാരാമീറ്ററുകൾ പുതുക്കാൻ **Validate and parse input** തിരഞ്ഞെടുക്കുക.

    ![Validate input.](../../../../../../translated_images/ml/09-02-validate-input.317c76ef766361e9.webp)

1. നിങ്ങൾ സൃഷ്‌ടിച്ച കസ്റ്റം കണക്ഷനായി **connection** ഉള്ള **Value** തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, *connection*.

    ![Connection.](../../../../../../translated_images/ml/09-03-select-connection.99bdddb4b1844023.webp)

#### നിങ്ങളുടെ കസ്റ്റം മോഡലുമായി ചാറ്റ് ചെയ്യുക

1. **Chat** തിരഞ്ഞെടുക്കുക.

    ![Select chat.](../../../../../../translated_images/ml/09-04-select-chat.61936dce6612a1e6.webp)

1. ഇവിടെ ഫലങ്ങളുടെ ഒരു ഉദാഹരണം നൽകിയിരിക്കുന്നു: ഇപ്പോൾ നിങ്ങൾക്ക് നിങ്ങളുടെ കസ്റ്റം Phi-3 മോഡലുമായി ചാറ്റ് ചെയ്യാം. ഫൈൻ-ട്യൂണിങ്ങിനായി ഉപയോഗിച്ച ഡാറ്റയുടെ അടിസ്ഥാനത്തിൽ ചോദ്യങ്ങൾ ചോദിക്കുന്നതാണ് ശുപാർശ ചെയ്യുന്നത്.

    ![Chat with prompt flow.](../../../../../../translated_images/ml/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ഡി‌സ്‌ക്ലെയിമര്‍:**
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ നിർവികാരമായതിൽ ശ്രമിച്ചിരിക്കുന്നെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ ശുദ്ധിമുട്ടുകൾ ഉണ്ടാകാവുന്നതാണ് എന്നതാണ് ശ്രദ്ധിക്കുക. ഉടമസ്ഥഭാഷയിലെ മൗലിക രേഖയെ അധികാരപരമായ ഉറവിടമായി പരിഗണിക്കണം. പ്രധാനമായ വിവരംകൾക്കായി പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന യാതൊരു തെറ്റിദ്ധാരണകൾക്കും അല്ലെങ്കിൽ തെറ്റായി വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾക്ക് ഉത്തരവാദിത്വം ഇല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->