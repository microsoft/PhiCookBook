<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-09T19:25:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "my"
}
-->
# Fine-tune နှင့် Azure AI Foundry တွင် Prompt flow ဖြင့် custom Phi-3 မော်ဒယ်များ ပေါင်းစပ်ခြင်း

ဤ end-to-end (E2E) နမူနာသည် Microsoft Tech Community မှ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" လမ်းညွှန်အပေါ် အခြေခံထားပြီး၊ custom Phi-3 မော်ဒယ်များကို fine-tune ပြုလုပ်ခြင်း၊ တပ်ဆင်ခြင်းနှင့် Azure AI Foundry တွင် Prompt flow နှင့် ပေါင်းစပ်အသုံးပြုခြင်းလုပ်ငန်းစဉ်များကို မိတ်ဆက်ပေးသည်။
E2E နမူနာ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" ကဲ့သို့ ကိုယ်ပိုင်ကွန်ပျူတာတွင် ကုဒ်များကို ပြေးဆွဲခြင်းမဟုတ်ဘဲ၊ ဤသင်ခန်းစာတွင် Azure AI / ML Studio အတွင်း မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် ပေါင်းစပ်ခြင်းကို အဓိကထားပြသသည်။

## အနှစ်ချုပ်

ဤ E2E နမူနာတွင် Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် Azure AI Foundry တွင် Prompt flow နှင့် ပေါင်းစပ်အသုံးပြုနည်းကို သင်ယူမည်ဖြစ်သည်။ Azure AI / ML Studio ကို အသုံးပြု၍ custom AI မော်ဒယ်များကို တပ်ဆင်ခြင်းနှင့် အသုံးပြုခြင်းအတွက် workflow တစ်ခုကို တည်ဆောက်မည်ဖြစ်သည်။ ဤ E2E နမူနာကို သုံးခုသော အခြေအနေများအဖြစ် ခွဲခြားထားသည်-

**အခြေအနေ ၁: Azure အရင်းအမြစ်များကို စတင်တည်ဆောက်ခြင်းနှင့် fine-tuning အတွက် ပြင်ဆင်ခြင်း**

**အခြေအနေ ၂: Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် Azure Machine Learning Studio တွင် တပ်ဆင်ခြင်း**

**အခြေအနေ ၃: Prompt flow နှင့် ပေါင်းစပ်ခြင်းနှင့် Azure AI Foundry တွင် ကိုယ်ပိုင်မော်ဒယ်ဖြင့် စကားပြောခြင်း**

ဤ E2E နမူနာ၏ အနှစ်ချုပ်ကို အောက်တွင် ဖော်ပြထားသည်။

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/00-01-architecture.png)

### အကြောင်းအရာ စာရင်း

1. **[အခြေအနေ ၁: Azure အရင်းအမြစ်များကို စတင်တည်ဆောက်ခြင်းနှင့် fine-tuning အတွက် ပြင်ဆင်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace တည်ဆောက်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription တွင် GPU ကွိုတားများ တောင်းဆိုခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Role assignment ထည့်သွင်းခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Project ကို စတင်တည်ဆောက်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tuning အတွက် dataset ပြင်ဆင်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[အခြေအနေ ၂: Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် Azure Machine Learning Studio တွင် တပ်ဆင်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tuned Phi-3 မော်ဒယ်ကို တပ်ဆင်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[အခြေအနေ ၃: Prompt flow နှင့် ပေါင်းစပ်ခြင်းနှင့် Azure AI Foundry တွင် ကိုယ်ပိုင်မော်ဒယ်ဖြင့် စကားပြောခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Custom Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစပ်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Custom Phi-3 မော်ဒယ်ဖြင့် စကားပြောခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## အခြေအနေ ၁: Azure အရင်းအမြစ်များကို စတင်တည်ဆောက်ခြင်းနှင့် fine-tuning အတွက် ပြင်ဆင်ခြင်း

### Azure Machine Learning Workspace တည်ဆောက်ခြင်း

1. Portal စာမျက်နှာ၏ အပေါ်ဆုံးရှိ **ရှာဖွေရေးဘား**တွင် *azure machine learning* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **Azure Machine Learning** ကို ရွေးချယ်ပါ။

    ![Type azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-01-type-azml.png)

2. နေရာပြောင်းခြင်း မီနူးမှ **+ Create** ကို ရွေးချယ်ပါ။

3. နေရာပြောင်းခြင်း မီနူးမှ **New workspace** ကို ရွေးချယ်ပါ။

    ![Select new workspace.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-02-select-new-workspace.png)

4. အောက်ပါ အချက်များကို ပြုလုပ်ပါ-

    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Resource group** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခု ဖန်တီးပါ)။
    - **Workspace Name** ထည့်သွင်းပါ။ ထူးခြားသော အမည်ဖြစ်ရမည်။
    - အသုံးပြုလိုသော **Region** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Storage account** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခု ဖန်တီးပါ)။
    - အသုံးပြုမည့် **Key vault** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခု ဖန်တီးပါ)။
    - အသုံးပြုမည့် **Application insights** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခု ဖန်တီးပါ)။
    - အသုံးပြုမည့် **Container registry** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခု ဖန်တီးပါ)။

    ![Fill azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-03-fill-AZML.png)

5. **Review + Create** ကို ရွေးချယ်ပါ။

6. **Create** ကို ရွေးချယ်ပါ။

### Azure Subscription တွင် GPU ကွိုတားများ တောင်းဆိုခြင်း

ဤသင်ခန်းစာတွင် Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် တပ်ဆင်ခြင်းအတွက် GPU များကို အသုံးပြုမည်ဖြစ်သည်။ Fine-tuning အတွက် *Standard_NC24ads_A100_v4* GPU ကို အသုံးပြုမည်ဖြစ်ပြီး ကွိုတားတောင်းဆိုရန် လိုအပ်သည်။ တပ်ဆင်ခြင်းအတွက် *Standard_NC6s_v3* GPU ကို အသုံးပြုမည်ဖြစ်ပြီး ထိုကွိုတားကိုလည်း တောင်းဆိုရမည်ဖြစ်သည်။

> [!NOTE]
>
> Pay-As-You-Go subscription များသာ GPU ခွဲဝေပေးခြင်းအတွက် အရည်အချင်းရှိပြီး၊ benefit subscription များကို လက်ရှိတွင် မထောက်ပံ့သေးပါ။
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. *Standard NCADSA100v4 Family* ကွိုတားတောင်းဆိုရန် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - ဘယ်ဘက် tab မှ **Quota** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Virtual machine family** ကို ရွေးချယ်ပါ။ ဥပမာအားဖြင့် *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* ကို ရွေးချယ်ပါ၊ ၎င်းတွင် *Standard_NC24ads_A100_v4* GPU ပါဝင်သည်။
    - နေရာပြောင်းခြင်း မီနူးမှ **Request quota** ကို ရွေးချယ်ပါ။

        ![Request quota.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/02-02-request-quota.png)

    - Request quota စာမျက်နှာတွင် အသုံးပြုလိုသော **New cores limit** ကို ထည့်သွင်းပါ။ ဥပမာ 24။
    - Request quota စာမျက်နှာတွင် **Submit** ကို နှိပ်၍ GPU ကွိုတားတောင်းဆိုပါ။

1. *Standard NCSv3 Family* ကွိုတားတောင်းဆိုရန် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - ဘယ်ဘက် tab မှ **Quota** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Virtual machine family** ကို ရွေးချယ်ပါ။ ဥပမာအားဖြင့် *Standard NCSv3 Family Cluster Dedicated vCPUs* ကို ရွေးချယ်ပါ၊ ၎င်းတွင် *Standard_NC6s_v3* GPU ပါဝင်သည်။
    - နေရာပြောင်းခြင်း မီနူးမှ **Request quota** ကို ရွေးချယ်ပါ။
    - Request quota စာမျက်နှာတွင် အသုံးပြုလိုသော **New cores limit** ကို ထည့်သွင်းပါ။ ဥပမာ 24။
    - Request quota စာမျက်နှာတွင် **Submit** ကို နှိပ်၍ GPU ကွိုတားတောင်းဆိုပါ။

### Role assignment ထည့်သွင်းခြင်း

မော်ဒယ်များကို fine-tune ပြုလုပ်ခြင်းနှင့် တပ်ဆင်ခြင်းအတွက် User Assigned Managed Identity (UAI) တစ်ခု ဖန်တီးပြီး သင့်တော်သော ခွင့်ပြုချက်များ ပေးသင့်သည်။ ဤ UAI ကို တပ်ဆင်ခြင်းအတွင်း အတည်ပြုမှုအတွက် အသုံးပြုမည်ဖြစ်သည်။

#### User Assigned Managed Identity (UAI) ဖန်တီးခြင်း

1. Portal စာမျက်နှာ၏ အပေါ်ဆုံးရှိ **ရှာဖွေရေးဘား**တွင် *managed identities* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **Managed Identities** ကို ရွေးချယ်ပါ။

    ![Type managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-01-type-managed-identities.png)

1. **+ Create** ကို ရွေးချယ်ပါ။

    ![Select create.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-02-select-create.png)

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ-

    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Resource group** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခု ဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Region** ကို ရွေးချယ်ပါ။
    - **Name** ထည့်သွင်းပါ။ ထူးခြားသော အမည်ဖြစ်ရမည်။

    ![Select create.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-03-fill-managed-identities-1.png)

1. **Review + create** ကို ရွေးချယ်ပါ။

1. **+ Create** ကို ရွေးချယ်ပါ။

#### Managed Identity သို့ Contributor role assignment ထည့်သွင်းခြင်း

1. ဖန်တီးထားသော Managed Identity resource သို့ သွားပါ။

1. ဘယ်ဘက် tab မှ **Azure role assignments** ကို ရွေးချယ်ပါ။

1. နေရာပြောင်းခြင်း မီနူးမှ **+Add role assignment** ကို ရွေးချယ်ပါ။

1. Add role assignment စာမျက်နှာတွင် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-
    - **Scope** ကို **Resource group** အဖြစ် သတ်မှတ်ပါ။
    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Resource group** ကို ရွေးချယ်ပါ။
    - **Role** ကို **Contributor** အဖြစ် ရွေးချယ်ပါ။

    ![Fill contributor role.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-04-fill-contributor-role.png)

2. **Save** ကို နှိပ်ပါ။

#### Managed Identity သို့ Storage Blob Data Reader role assignment ထည့်သွင်းခြင်း

1. Portal စာမျက်နှာ၏ အပေါ်ဆုံးရှိ **ရှာဖွေရေးဘား**တွင် *storage accounts* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **Storage accounts** ကို ရွေးချယ်ပါ။

    ![Type storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-05-type-storage-accounts.png)

1. Azure Machine Learning workspace နှင့် ဆက်စပ်ထားသော storage account ကို ရွေးချယ်ပါ။ ဥပမာ *finetunephistorage*။

1. Add role assignment စာမျက်နှာသို့ သွားရန် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - ဖန်တီးထားသော Azure Storage account သို့ သွားပါ။
    - ဘယ်ဘက် tab မှ **Access Control (IAM)** ကို ရွေးချယ်ပါ။
    - နေရာပြောင်းခြင်း မီနူးမှ **+ Add** ကို ရွေးချယ်ပါ။
    - နေရာပြောင်းခြင်း မီနူးမှ **Add role assignment** ကို ရွေးချယ်ပါ။

    ![Add role.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-06-add-role.png)

1. Add role assignment စာမျက်နှာတွင် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - Role စာမျက်နှာတွင် **ရှာဖွေရေးဘား**တွင် *Storage Blob Data Reader* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **Storage Blob Data Reader** ကို ရွေးချယ်ပါ။
    - Role စာမျက်နှာတွင် **Next** ကို နှိပ်ပါ။
    - Members စာမျက်နှာတွင် **Assign access to** အဖြစ် **Managed identity** ကို ရွေးချယ်ပါ။
    - Members စာမျက်နှာတွင် **+ Select members** ကို နှိပ်ပါ။
    - Select managed identities စာမျက်နှာတွင် သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - Select managed identities စာမျက်နှာတွင် **Managed identity** အဖြစ် **Manage Identity** ကို ရွေးချယ်ပါ။
    - Select managed identities စာမျက်နှာတွင် ဖန်တီးထားသော Manage Identity ကို ရွေးချယ်ပါ။ ဥပမာ *finetunephi-managedidentity*။
    - Select managed identities စာမျက်နှာတွင် **Select** ကို နှိပ်ပါ။

    ![Select managed identity.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-08-select-managed-identity.png)

1. **Review + assign** ကို ရွေးချယ်ပါ။

#### Managed Identity သို့ AcrPull role assignment ထည့်သွင်းခြင်း

1. Portal စာမျက်နှာ၏ အပေါ်ဆုံးရှိ **ရှာဖွေရေးဘား**တွင် *container registries* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **Container registries** ကို ရွေးချယ်ပါ။

    ![Type container registries.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-09-type-container-registries.png)

1. Azure Machine Learning workspace နှင့် ဆက်စပ်ထားသော container registry ကို ရွေးချယ်ပါ။ ဥပမာ *finetunephicontainerregistry*

1. Add role assignment စာမျက်နှာသို့ သွားရန် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - ဘယ်ဘက် tab မှ **Access Control (IAM)** ကို ရွေးချယ်ပါ။
    - နေရာပြောင်းခြင်း မီနူးမှ **+ Add** ကို ရွေးချယ်ပါ။
    - နေရာပြောင်းခြင်း မီနူးမှ **Add role assignment** ကို ရွေးချယ်ပါ။

1. Add role assignment စာမျက်နှာတွင် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - Role စာမျက်နှာတွင် **ရှာဖွေရေးဘား**တွင် *AcrPull* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **AcrPull** ကို ရွ
#### virtual environment တစ်ခု ဖန်တီးခြင်း

1. terminal ထဲမှာ အောက်ပါ command ကို ရိုက်ထည့်ပြီး *.venv* ဆိုတဲ့ virtual environment ကို ဖန်တီးပါ။

2. terminal ထဲမှာ အောက်ပါ command ကို ရိုက်ထည့်ပြီး virtual environment ကို ဖွင့်ပါ။

> [!NOTE]
> အကယ်၍ အလုပ်လုပ်ခဲ့ပါက command prompt မတိုင်မီ *(.venv)* ကို တွေ့ရပါမည်။

#### လိုအပ်သော package များ ထည့်သွင်းခြင်း

1. terminal ထဲမှာ အောက်ပါ command များကို ရိုက်ထည့်ပြီး လိုအပ်သော package များကို ထည့်သွင်းပါ။

#### `download_dataset.py` ဖိုင် ဖန်တီးခြင်း

> [!NOTE]
> ဖိုင်ဖွဲ့စည်းမှု အပြည့်အစုံ:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** ကို ဖွင့်ပါ။

1. menu bar မှ **File** ကို ရွေးချယ်ပါ။

1. **Open Folder** ကို ရွေးချယ်ပါ။

1. သင်ဖန်တီးထားသော *finetune-phi* ဖိုလ်ဒါကို ရွေးချယ်ပါ၊ အဆိုပါဖိုလ်ဒါသည် *C:\Users\yourUserName\finetune-phi* တွင် တည်ရှိသည်။

    ![သင်ဖန်တီးထားသော ဖိုလ်ဒါကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-01-open-project-folder.png)

1. Visual Studio Code ၏ ဘယ်ဘက် panel တွင် right-click ပြုလုပ်ပြီး **New File** ကို ရွေးချယ်ကာ *download_dataset.py* ဆိုသော ဖိုင်အသစ်ကို ဖန်တီးပါ။

    ![ဖိုင်အသစ် ဖန်တီးခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-02-create-new-file.png)

### fine-tuning အတွက် dataset ပြင်ဆင်ခြင်း

ဒီလေ့ကျင့်မှုတွင် *download_dataset.py* ဖိုင်ကို အသုံးပြု၍ *ultrachat_200k* datasets များကို သင့်ဒေသတွင် ဒေါင်းလုပ်လုပ်ပါမည်။ ထို့နောက် ဒီ datasets များကို အသုံးပြု၍ Azure Machine Learning တွင် Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ပါမည်။

ဒီလေ့ကျင့်မှုတွင် သင်လုပ်ဆောင်မည့်အချက်များမှာ -

- *download_dataset.py* ဖိုင်ထဲတွင် datasets များ ဒေါင်းလုပ်လုပ်ရန် ကုဒ်များ ထည့်သွင်းခြင်း။
- *download_dataset.py* ဖိုင်ကို run ပြီး datasets များကို ဒေသတွင် ဒေါင်းလုပ်လုပ်ခြင်း။

#### *download_dataset.py* ဖြင့် dataset ကို ဒေါင်းလုပ်လုပ်ခြင်း

1. Visual Studio Code တွင် *download_dataset.py* ဖိုင်ကို ဖွင့်ပါ။

1. အောက်ပါ ကုဒ်များကို *download_dataset.py* ဖိုင်ထဲ ထည့်သွင်းပါ။

1. terminal ထဲတွင် အောက်ပါ command ကို ရိုက်ထည့်ကာ script ကို run ပြီး dataset ကို ဒေသတွင် ဒေါင်းလုပ်လုပ်ပါ။

1. datasets များကို သင့်ဒေသရှိ *finetune-phi/data* ဖိုလ်ဒါထဲ သေချာ သိမ်းဆည်းထားကြောင်း စစ်ဆေးပါ။

> [!NOTE]
>
> #### dataset အရွယ်အစားနှင့် fine-tuning အချိန်အကြောင်း မှတ်ချက်
>
> ဒီသင်ခန်းစာတွင် dataset ၏ 1% (`split='train[:1%]'`) ကိုသာ အသုံးပြုသည်။ ဒါကြောင့် ဒေတာအရေအတွက် လျော့နည်းပြီး upload နှင့် fine-tuning လုပ်ငန်းစဉ်များ မြန်ဆန်စေသည်။ သင် training အချိန်နှင့် မော်ဒယ်စွမ်းဆောင်ရည်အကြား သင့်တော်သော အချိုးကို ရှာဖွေရန် အချိုးကို ပြင်ဆင်နိုင်သည်။ dataset ၏ အပိုင်းသေးငယ်တစ်ခုကို အသုံးပြုခြင်းသည် fine-tuning အချိန်ကို လျော့နည်းစေပြီး သင်ခန်းစာအတွက် လုပ်ငန်းစဉ်ကို ပိုမိုထိန်းချုပ်နိုင်စေသည်။

## အခြေအနေ ၂: Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် Azure Machine Learning Studio တွင် Deploy ပြုလုပ်ခြင်း

### Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်း

ဒီလေ့ကျင့်မှုတွင် Azure Machine Learning Studio တွင် Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ပါမည်။

ဒီလေ့ကျင့်မှုတွင် သင်လုပ်ဆောင်မည့်အချက်များမှာ -

- fine-tuning အတွက် computer cluster တစ်ခု ဖန်တီးခြင်း။
- Azure Machine Learning Studio တွင် Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်း။

#### fine-tuning အတွက် computer cluster ဖန်တီးခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. ဘယ်ဘက် tab မှ **Compute** ကို ရွေးချယ်ပါ။

1. navigation menu မှ **Compute clusters** ကို ရွေးချယ်ပါ။

1. **+ New** ကို နှိပ်ပါ။

    ![Compute ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-01-select-compute.png)

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ -

    - သင်အသုံးပြုလိုသော **Region** ကို ရွေးချယ်ပါ။
    - **Virtual machine tier** ကို **Dedicated** အဖြစ် ရွေးချယ်ပါ။
    - **Virtual machine type** ကို **GPU** အဖြစ် ရွေးချယ်ပါ။
    - **Virtual machine size** filter ကို **Select from all options** အဖြစ် ရွေးချယ်ပါ။
    - **Virtual machine size** ကို **Standard_NC24ads_A100_v4** အဖြစ် ရွေးချယ်ပါ။

    ![Cluster ဖန်တီးခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-02-create-cluster.png)

1. **Next** ကို နှိပ်ပါ။

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ -

    - **Compute name** ထည့်ပါ။ ထူးခြားသော အမည်ဖြစ်ရမည်။
    - **Minimum number of nodes** ကို **0** အဖြစ် ရွေးချယ်ပါ။
    - **Maximum number of nodes** ကို **1** အဖြစ် ရွေးချယ်ပါ။
    - **Idle seconds before scale down** ကို **120** အဖြစ် ရွေးချယ်ပါ။

    ![Cluster ဖန်တီးခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-03-create-cluster.png)

1. **Create** ကို နှိပ်ပါ။

#### Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace ကို ရွေးချယ်ပါ။

    ![သင်ဖန်တီးထားသော workspace ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ -

    - ဘယ်ဘက် tab မှ **Model catalog** ကို ရွေးချယ်ပါ။
    - **search bar** တွင် *phi-3-mini-4k* ဟု ရိုက်ထည့်ပြီး ပေါ်လာသော ရွေးချယ်စရာများထဲမှ **Phi-3-mini-4k-instruct** ကို ရွေးချယ်ပါ။

    ![phi-3-mini-4k ဟု ရိုက်ထည့်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-05-type-phi-3-mini-4k.png)

1. navigation menu မှ **Fine-tune** ကို ရွေးချယ်ပါ။

    ![fine tune ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-06-select-fine-tune.png)

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ -

    - **Select task type** ကို **Chat completion** အဖြစ် ရွေးချယ်ပါ။
    - **+ Select data** ကို နှိပ်ကာ **Training data** ကို အပ်လုဒ်ပါ။
    - Validation data upload အမျိုးအစားကို **Provide different validation data** အဖြစ် ရွေးချယ်ပါ။
    - **+ Select data** ကို နှိပ်ကာ **Validation data** ကို အပ်လုဒ်ပါ။

    ![fine-tuning စာမျက်နှာ ဖြည့်စွက်ခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-07-fill-finetuning.png)

    > [!TIP]
    >
    > **Advanced settings** ကို ရွေးချယ်ကာ **learning_rate** နှင့် **lr_scheduler_type** စသည့် ဖန်တီးမှုများကို ကိုယ်ပိုင်လိုအပ်ချက်အရ ပြင်ဆင်နိုင်ပြီး fine-tuning လုပ်ငန်းစဉ်ကို ပိုမိုထိရောက်စေပါသည်။

1. **Finish** ကို နှိပ်ပါ။

1. ဒီလေ့ကျင့်မှုတွင် သင် Azure Machine Learning ကို အသုံးပြု၍ Phi-3 မော်ဒယ်ကို အောင်မြင်စွာ fine-tune ပြုလုပ်နိုင်ခဲ့ပါသည်။ fine-tuning လုပ်ငန်းစဉ်သည် အချိန်ကြာနိုင်ပါသည်။ fine-tuning job ကို run ပြီးနောက် အပြီးသတ်ရန် စောင့်ဆိုင်းရမည်ဖြစ်သည်။ Azure Machine Learning Workspace ၏ ဘယ်ဘက် tab မှ Jobs tab သို့ သွားကာ fine-tuning job ၏ အခြေအနေကို ကြည့်ရှုနိုင်ပါသည်။ နောက်တစ်ကြိမ်တွင် fine-tuned မော်ဒယ်ကို deploy ပြုလုပ်ပြီး Prompt flow နှင့် ပေါင်းစည်းမည်ဖြစ်သည်။

    ![finetuning job ကို ကြည့်ရှုပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-08-output.png)

### fine-tuned Phi-3 မော်ဒယ်ကို deploy ပြုလုပ်ခြင်း

fine-tuned Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစည်းရန် မော်ဒယ်ကို real-time inference အတွက် အသုံးပြုနိုင်ရန် deploy ပြုလုပ်ရမည်ဖြစ်သည်။ ဒီလုပ်ငန်းစဉ်တွင် မော်ဒယ်ကို register ပြုလုပ်ခြင်း၊ online endpoint တစ်ခု ဖန်တီးခြင်းနှင့် မော်ဒယ်ကို deploy ပြုလုပ်ခြင်းတို့ ပါဝင်သည်။

ဒီလေ့ကျင့်မှုတွင် သင်လုပ်ဆောင်မည့်အချက်များမှာ -

- Azure Machine Learning workspace တွင် fine-tuned မော်ဒယ်ကို register ပြုလုပ်ခြင်း။
- online endpoint တစ်ခု ဖန်တီးခြင်း။
- register ပြုလုပ်ထားသော fine-tuned Phi-3 မော်ဒယ်ကို deploy ပြုလုပ်ခြင်း။

#### fine-tuned မော်ဒယ်ကို register ပြုလုပ်ခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace ကို ရွေးချယ်ပါ။

    ![သင်ဖန်တီးထားသော workspace ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. ဘယ်ဘက် tab မှ **Models** ကို ရွေးချယ်ပါ။

1. **+ Register** ကို နှိပ်ပါ။

1. **From a job output** ကို ရွေးချယ်ပါ။

    ![မော်ဒယ် register ပြုလုပ်ခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-01-register-model.png)

1. သင်ဖန်တီးထားသော job ကို ရွေးချယ်ပါ။

    ![job ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-02-select-job.png)

1. **Next** ကို နှိပ်ပါ။

1. **Model type** ကို **MLflow** အဖြစ် ရွေးချယ်ပါ။

1. **Job output** ကို ရွေးထားပြီးဖြစ်ကြောင်း သေချာစေပါ၊ အလိုအလျောက် ရွေးထားမည်ဖြစ်သည်။

    ![output ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-03-select-output.png)

2. **Next** ကို နှိပ်ပါ။

3. **Register** ကို နှိပ်ပါ။

    ![register ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-04-register.png)

4. ဘယ်ဘက် tab မှ **Models** မီနူးသို့ သွားကာ သင့် register ပြုလုပ်ထားသော မော်ဒယ်ကို ကြည့်ရှုနိုင်ပါသည်။

    ![register ပြုလုပ်ထားသော မော်ဒယ်။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-05-registered-model.png)

#### fine-tuned မော်ဒယ်ကို deploy ပြုလုပ်ခြင်း

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace သို့ သွားပါ။

1. ဘယ်ဘက် tab မှ **Endpoints** ကို ရွေးချယ်ပါ။

1. navigation menu မှ **Real-time endpoints** ကို ရွေးချယ်ပါ။

    ![endpoint ဖန်တီးခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-06-create-endpoint.png)

1. **Create** ကို နှိပ်ပါ။

1. သင် register ပြုလုပ်ထားသော မော်ဒယ်ကို ရွေးချယ်ပါ။

    ![register ပြုလုပ်ထားသော မော်ဒယ်ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-07-select-registered-model.png)

1. **Select** ကို နှိပ်ပါ။

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ -

    - **Virtual machine** ကို *Standard_NC6s_v3* အဖြစ် ရွေးချယ်ပါ။
    - သင်အသုံးပြုလိုသော **Instance count** ကို ရွေးချယ်ပါ။ ဥပမာ - *1*။
    - **Endpoint** ကို **New** အဖြစ် ရွေးချယ်ကာ endpoint အသစ် ဖန်တီးပါ။
    - **Endpoint name** ထည့်ပါ။ ထူးခြားသော အမည်ဖြစ်ရမည်။
    - **Deployment name** ထည့်ပါ။ ထူးခြားသော အမည်ဖြစ်ရမည်။

    ![deployment ဆက်တင်များ ဖြည့်စွက်ခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-08-deployment-setting.png)

1. **Deploy** ကို နှိပ်ပါ။

> [!WARNING]
> သင့်အကောင့်တွင် အပိုကြေးများ မဖြစ်ပေါ်စေရန် Azure Machine Learning workspace တွင် ဖန်တီးထားသော endpoint ကို ဖျက်ပစ်ရန် သေချာစေပါ။
>

#### Azure Machine Learning Workspace တွင် deployment အခြေအနေ စစ်ဆေးခြင်း

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace သို့ သွားပါ။

1. ဘယ်ဘက် tab မှ **Endpoints** ကို ရွေးချယ်ပါ။

1. သင်ဖန်တီးထားသော endpoint ကို ရွေးချယ်ပါ။

    ![Endpoints ကို ရွေးချယ်ပါ။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-09-check-deployment.png)

1. ဒီစာမျက်နှာတွင် deployment လုပ်ငန်းစဉ်အတွင်း endpoint များကို စီမံခန့်ခွဲနိုင်ပါသည်။

> [!NOTE]
> deployment ပြီးဆုံးပြီးနောက် **Live traffic** ကို **100%** အဖြစ် သတ်မှတ်ထားရန် သေချာစေပါ။ မဟုတ်ပါက **Update traffic** ကို နှိပ်ကာ traffic ဆက်တင်များကို ပြင်ဆင်နိုင်သည်။ traffic ကို 0% သတ်မှတ်ထားပါက မော်ဒယ်ကို စမ်းသပ်၍ မရပါ။
>
> ![traffic ကို သတ်မှတ်ခြင်း။](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-10-set-traffic.png)
>

## အခြေအနေ ၃: Prompt flow နှင့် ပေါင်းစည်းပြီး Azure AI Foundry တွင် သင့်ကိုယ်ပိုင် မော်ဒယ်ဖြင့် စကားပြောခြင်း

### Prompt flow နှင့် ကိုယ်ပိုင် Phi-3 မော်ဒယ် ပေါင်းစည်းခြင်း

fine-tuned မော်ဒယ်ကို အောင်မြင်စွာ deploy ပြုလုပ်ပြီးနောက် Prompt Flow နှင့် ပေါင်းစည်းကာ သင့်မော်ဒယ်ကို real-time application များတွင် အသုံးပြုနိုင်ပါပြီ။ ၎င်းဖြင့် သင့်ကိုယ်ပိုင် Phi-3 မော်ဒယ်ဖြင့် အမျိုးမျိုးသော အပြန်အလှန် လုပ်ငန်းများ ဆောင်ရွက်နိုင်ပါသည်။

ဒီလေ့ကျင့်မှုတွင် သင်လုပ်ဆောင်မည့်အချက်များမှာ -

- Azure AI Foundry Hub ဖန်တီးခြင်း။
- Azure AI Foundry Project ဖန်တီးခြင်း။
- Prompt flow ဖန်
> [!NOTE]
> သင်သည် Azure ML Studio ကို အသုံးပြု၍ Promptflow နှင့် ပေါင်းစည်းနိုင်ပါသည်။ အဲဒီပေါင်းစည်းမှုလုပ်ငန်းစဉ်ကို Azure ML Studio တွင်လည်း အတူတူ အသုံးပြုနိုင်ပါသည်။
#### Azure AI Foundry Hub ဖန်တီးခြင်း

Project ဖန်တီးမပြုလုပ်မီ Hub တစ်ခု ဖန်တီးရပါမည်။ Hub သည် Resource Group အဖြစ် လုပ်ဆောင်ပြီး Azure AI Foundry အတွင်းရှိ Project များစွာကို စီမံခန့်ခွဲရန် အဆင်ပြေစေပါသည်။

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) သို့ သွားပါ။

1. ဘယ်ဘက်ဘားမှ **All hubs** ကို ရွေးချယ်ပါ။

1. navigation menu မှ **+ New hub** ကို ရွေးချယ်ပါ။

    ![Create hub.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-01-create-hub.png)

1. အောက်ပါအချက်များကို ပြုလုပ်ပါ-

    - **Hub name** ထည့်ပါ။ ထူးခြားသောတန်ဖိုးဖြစ်ရပါမည်။
    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Resource group** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်ဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Location** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Connect Azure AI Services** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်ဖန်တီးပါ)။
    - **Connect Azure AI Search** ကို **Skip connecting** အဖြစ် ရွေးချယ်ပါ။

    ![Fill hub.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-02-fill-hub.png)

1. **Next** ကို နှိပ်ပါ။

#### Azure AI Foundry Project ဖန်တီးခြင်း

1. ဖန်တီးထားသော Hub အတွင်းမှ ဘယ်ဘက်ဘားမှ **All projects** ကို ရွေးချယ်ပါ။

1. navigation menu မှ **+ New project** ကို ရွေးချယ်ပါ။

    ![Select new project.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-04-select-new-project.png)

1. **Project name** ထည့်ပါ။ ထူးခြားသောတန်ဖိုးဖြစ်ရပါမည်။

    ![Create project.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-05-create-project.png)

1. **Create a project** ကို နှိပ်ပါ။

#### fine-tuned Phi-3 မော်ဒယ်အတွက် custom connection ထည့်သွင်းခြင်း

သင့် custom Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစည်းရန် မော်ဒယ်၏ endpoint နှင့် key ကို custom connection အဖြစ် သိမ်းဆည်းရပါမည်။ ဒီစနစ်က Prompt flow မှာ သင့် custom Phi-3 မော်ဒယ်ကို အသုံးပြုနိုင်ရန် အာမခံပေးပါသည်။

#### fine-tuned Phi-3 မော်ဒယ်၏ api key နှင့် endpoint uri သတ်မှတ်ခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) သို့ သွားပါ။

1. ဖန်တီးထားသော Azure Machine learning workspace သို့ သွားပါ။

1. ဘယ်ဘက်ဘားမှ **Endpoints** ကို ရွေးချယ်ပါ။

    ![Select endpoints.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-06-select-endpoints.png)

1. ဖန်တီးထားသော endpoint ကို ရွေးချယ်ပါ။

    ![Select endpoints.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-07-select-endpoint-created.png)

1. navigation menu မှ **Consume** ကို ရွေးချယ်ပါ။

1. သင့် **REST endpoint** နှင့် **Primary key** ကို ကူးယူပါ။

    ![Copy api key and endpoint uri.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-08-copy-endpoint-key.png)

#### Custom Connection ထည့်သွင်းခြင်း

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) သို့ သွားပါ။

1. ဖန်တီးထားသော Azure AI Foundry project သို့ သွားပါ။

1. ဖန်တီးထားသော Project အတွင်း ဘယ်ဘက်ဘားမှ **Settings** ကို ရွေးချယ်ပါ။

1. **+ New connection** ကို ရွေးချယ်ပါ။

    ![Select new connection.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-09-select-new-connection.png)

1. navigation menu မှ **Custom keys** ကို ရွေးချယ်ပါ။

    ![Select custom keys.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-10-select-custom-keys.png)

1. အောက်ပါအချက်များကို ပြုလုပ်ပါ-

    - **+ Add key value pairs** ကို ရွေးချယ်ပါ။
    - key name အတွက် **endpoint** ထည့်ပြီး Azure ML Studio မှ ကူးယူထားသော endpoint ကို value field ထဲတွင် ပေးပါ။
    - ထပ်မံ၍ **+ Add key value pairs** ကို ရွေးချယ်ပါ။
    - key name အတွက် **key** ထည့်ပြီး Azure ML Studio မှ ကူးယူထားသော key ကို value field ထဲတွင် ပေးပါ။
    - key များ ထည့်သွင်းပြီးနောက် **is secret** ကို ရွေးချယ်၍ key များ ဖော်ပြခြင်းမှ ကာကွယ်ပါ။

    ![Add connection.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-11-add-connection.png)

1. **Add connection** ကို နှိပ်ပါ။

#### Prompt flow ဖန်တီးခြင်း

Azure AI Foundry တွင် custom connection ထည့်သွင်းပြီးပါပြီ။ ယခုအခါ အောက်ပါအဆင့်များဖြင့် Prompt flow တစ်ခု ဖန်တီးပါမည်။ ထို့နောက် ဒီ Prompt flow ကို custom connection နှင့် ချိတ်ဆက်ပြီး fine-tuned မော်ဒယ်ကို Prompt flow အတွင်း အသုံးပြုနိုင်ပါမည်။

1. ဖန်တီးထားသော Azure AI Foundry project သို့ သွားပါ။

1. ဘယ်ဘက်ဘားမှ **Prompt flow** ကို ရွေးချယ်ပါ။

1. navigation menu မှ **+ Create** ကို ရွေးချယ်ပါ။

    ![Select Promptflow.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-12-select-promptflow.png)

1. navigation menu မှ **Chat flow** ကို ရွေးချယ်ပါ။

    ![Select chat flow.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-13-select-flow-type.png)

1. အသုံးပြုမည့် **Folder name** ထည့်ပါ။

    ![Enter name.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-14-enter-name.png)

2. **Create** ကို နှိပ်ပါ။

#### သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောရန် Prompt flow ကို ပြင်ဆင်ခြင်း

fine-tuned Phi-3 မော်ဒယ်ကို Prompt flow ထဲသို့ ပေါင်းစည်းရန် လိုအပ်ပါသည်။ သို့သော် ယခင်ရှိပြီးသား Prompt flow သည် ဒီရည်ရွယ်ချက်အတွက် မသင့်တော်ပါ။ ထို့ကြောင့် custom မော်ဒယ် ပေါင်းစည်းနိုင်ရန်အတွက် Prompt flow ကို ပြန်လည်ဒီဇိုင်းဆွဲရပါမည်။

1. Prompt flow အတွင်း အောက်ပါအချက်များကို ပြုလုပ်၍ ရှိပြီးသား flow ကို ပြန်လည်တည်ဆောက်ပါ-

    - **Raw file mode** ကို ရွေးချယ်ပါ။
    - *flow.dag.yml* ဖိုင်အတွင်းရှိ ရှိပြီးသားကုဒ်အားလုံးကို ဖျက်ပါ။
    - *flow.dag.yml* ဖိုင်တွင် အောက်ပါကုဒ်ကို ထည့်သွင်းပါ။

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

    - **Save** ကို နှိပ်ပါ။

    ![Select raw file mode.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-15-select-raw-file-mode.png)

1. Prompt flow တွင် custom Phi-3 မော်ဒယ်ကို အသုံးပြုရန် *integrate_with_promptflow.py* ဖိုင်တွင် အောက်ပါကုဒ်ကို ထည့်သွင်းပါ။

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

    ![Paste prompt flow code.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-16-paste-promptflow-code.png)

> [!NOTE]
> Azure AI Foundry တွင် Prompt flow အသုံးပြုနည်း ပိုမိုအသေးစိတ် သိရှိလိုပါက [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ကို ကြည့်ရှုနိုင်ပါသည်။

1. **Chat input**, **Chat output** ကို ရွေးချယ်၍ မော်ဒယ်နှင့် စကားပြောနိုင်ရန် ဖွင့်ပါ။

    ![Input Output.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-17-select-input-output.png)

1. ယခု သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောရန် အသင့်ဖြစ်ပါပြီ။ နောက်ထပ် လေ့ကျင့်မှုတွင် Prompt flow ကို စတင်အသုံးပြုပုံနှင့် fine-tuned Phi-3 မော်ဒယ်နှင့် စကားပြောနည်းကို သင်ယူပါမည်။

> [!NOTE]
>
> ပြန်လည်တည်ဆောက်ထားသော flow သည် အောက်ပါပုံစံကဲ့သို့ ဖြစ်ရပါမည်-
>
> ![Flow example.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-18-graph-example.png)
>

### သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောခြင်း

fine-tuned ပြီး သင့် custom Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစည်းပြီးဖြစ်သောကြောင့် ယခု မော်ဒယ်နှင့် ဆက်သွယ်စကားပြောရန် အသင့်ဖြစ်ပါပြီ။ ဒီလေ့ကျင့်မှုက Prompt flow ကို အသုံးပြုပြီး မော်ဒယ်နှင့် စကားပြောရန် စတင်ပြင်ဆင်ခြင်းနှင့် စတင်အသုံးပြုခြင်းကို လမ်းညွှန်ပေးပါမည်။ ဒီအဆင့်များကို လိုက်နာခြင်းဖြင့် fine-tuned Phi-3 မော်ဒယ်၏ စွမ်းဆောင်ရည်များကို အပြည့်အဝ အသုံးချနိုင်ပါမည်။

- Prompt flow ကို အသုံးပြုပြီး သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောပါ။

#### Prompt flow စတင်ခြင်း

1. Prompt flow စတင်ရန် **Start compute sessions** ကို နှိပ်ပါ။

    ![Start compute session.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-01-start-compute-session.png)

1. ပါရာမီတာများကို ပြန်လည်သတ်မှတ်ရန် **Validate and parse input** ကို နှိပ်ပါ။

    ![Validate input.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-02-validate-input.png)

1. သင့်ဖန်တီးထားသော custom connection ၏ **connection** တန်ဖိုးကို ရွေးချယ်ပါ။ ဥပမာ- *connection*။

    ![Connection.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-03-select-connection.png)

#### သင့် custom မော်ဒယ်နှင့် စကားပြောခြင်း

1. **Chat** ကို ရွေးချယ်ပါ။

    ![Select chat.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-04-select-chat.png)

1. ရလဒ်ဥပမာ- ယခု သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောနိုင်ပါပြီ။ fine-tuning အတွက် အသုံးပြုထားသော ဒေတာအပေါ် အခြေခံ၍ မေးခွန်းများ မေးရန် အကြံပြုပါသည်။

    ![Chat with prompt flow.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-05-chat-with-promptflow.png)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။