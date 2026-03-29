# Microsoft Foundry တွင် Prompt flow ဖြင့် စိတ်ကြိုက် Phi-3 မော်ဒယ်များကို Fine-tune ပြုလုပ်ခြင်းနှင့် ပေါင်းစပ်ခြင်း

Microsoft Tech Community မှ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" အသုံးပြု ဤ end-to-end (E2E) နမူနာသည် Microsoft Foundry တွင် Prompt flow နှင့် စိတ်ကြိုက် Phi-3 မော်ဒယ်များကို fine-tune ပြုလုပ်ခြင်း၊ တင်ပို့ခြင်း နှင့် ပေါင်းစပ်ခြင်း အခြေအနေများကို မိတ်ဆက်ပေးသည်။ ကိုယ်ပိုင် ကွန်ယူတာပေါ်တွင် ကုဒ်ကို run ပြုလုပ်ခြင်း ပါဝင်ခဲ့သော "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" E2E နမူနာမှ ကွဲပြားပြီး ဤ သင်ခန်းစာသည် Azure AI / ML Studio အတွင်းသို့သာ သင့်မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်း နှင့် ပေါင်းစပ်ခြင်း အပေါ် အာရုံစိုက်ထားသည်။

## အနှုတ်ချုပ်

ဤ E2E နမူနာတွင် Microsoft Foundry တွင် Prompt flow ဖြင့် Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်ခြင်းနှင့် ပေါင်းစပ်ခြင်း ကို သင်ကြားမည်ဖြစ်သည်။ Azure AI / ML Studio ကို အသုံးပြု၍ စိတ်ကြိုက် AI မော်ဒယ်များကို တင်ပို့ခြင်းနှင့် အသုံးပြုခြင်း workflow ကို ရရှိစေမည်။ ဤ E2E နမူနာကို သုံးခုသော အခြေအနေများအဖြစ် ခွဲခြားထားသည်-

**အခြေအနေ ၁: Azure အရင်းအမြစ်များ စီစဉ်တပ်ဆင်ခြင်းနှင့် fine-tuning အတွက် ပြင်ဆင်ခြင်း**

**အခြေအနေ ၂: Phi-3 မော်ဒယ်ကို fine-tune ပြုလုပ်၍ Azure Machine Learning Studio တွင် တင်ပို့ခြင်း**

**အခြေအနေ ၃: Prompt flow နှင့် ပေါင်းစပ်ပြီး Microsoft Foundry တွင် ကိုယ်ပိုင်မော်ဒယ်ဖြင့် စကားပြောခြင်း**

ဤ E2E နမူနာ၏ အနှုတ်ချုပ်ကို အောက်တွင် ကြည့်ရှုနိုင်ပါသည်။

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/my/00-01-architecture.198ba0f1ae6d841a.webp)

### အကြောင်းအရာ စာရင်း

1. **[အခြေအနေ ၁: Azure အရင်းအမြစ်များ စီစဉ်တပ်ဆင်ခြင်းနှင့် fine-tuning အတွက် ပြင်ဆင်ခြင်း](#အခြေအနေ-၁-azure-အရင်းအမြစ်များ-စီစဉ်တပ်ဆင်ခြင်းနှင့်-fine-tuning-အတွက်-ပြင်ဆင်ခြင်း)**
    - [Azure Machine Learning Workspace တည်ဆောက်ခြင်း](#azure-machine-learning-workspace-တည်ဆောက်ခြင်း)
    - [Azure Subscription တွင် GPU ကို အရေအတွက် တောင်းဆိုခြင်း](#azure-subscription-တွင်-gpu-ကို-အရေအတွက်-တောင်းဆိုခြင်း)
    - [Role တစ်ခု ခန့်အပ်ခြင်း](#role-တစ်ခု-ခန့်အပ်ခြင်း)
    - [ပရောဂျက် စီစဉ်တပ်ဆင်ခြင်း](#ပရောဂျက်-စီစဉ်တပ်ဆင်ခြင်း)
    - [Fine-tuning အတွက် ဒေတာစုစုစည်းခြင်း ပြင်ဆင်ခြင်း](#fine-tuning-အတွက်-dataset-ပြင်ဆင်ခြင်း)

1. **[အခြေအနေ ၂: Phi-3 မော်ဒယ်ကို Fine-tune ပြုလုပ်၍ Azure Machine Learning Studio တွင် တင်ပို့ခြင်း](#scenario-2-phi-3-မော်ဒယ်ကို-fine-tune-လုပ်ခြင်းနှင့်-azure-machine-learning-studio-တွင်-deploy-လုပ်ခြင်း)**
    - [Phi-3 မော်ဒယ်ကို Fine-tune ပြုလုပ်ခြင်း](#phi-3-မော်ဒယ်ကို-fine-tune-လုပ်ခြင်း)
    - [Fine-tuned Phi-3 မော်ဒယ်ကို တင်ပို့ခြင်း](#fine-tuned-phi-3-မော်ဒယ်ကို-deploy-လုပ်ခြင်း)

1. **[အခြေအနေ ၃: Prompt flow နှင့် ပေါင်းစပ်ပြီး Microsoft Foundry တွင် ကိုယ်ပိုင်မော်ဒယ်ဖြင့် စကားပြောခြင်း](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [စိတ်ကြိုက် Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစပ်ခြင်း](#custom-phi-3-မော်ဒယ်ကို-prompt-flow-နှင့်-ပေါင်းစည်းခြင်း)
    - [ကိုယ်ပိုင် Phi-3 မော်ဒယ်ဖြင့် စကားပြောခြင်း](#သင့်-custom-phi-3-မော်ဒယ်နှင့်-စကားပြောခြင်း)

## အခြေအနေ ၁: Azure အရင်းအမြစ်များ စီစဉ်တပ်ဆင်ခြင်းနှင့် fine-tuning အတွက် ပြင်ဆင်ခြင်း

### Azure Machine Learning Workspace တည်ဆောက်ခြင်း

1. Portal စာမျက်နှာအပေါ်ယံရှိ **ရှာဖွေမှုဘား**တွင် *azure machine learning* ဟူ၍ရိုက်ထည့်ပြီး ပြသသောရွေးချယ်စရာများထဲမှ **Azure Machine Learning** ကို ရွေးချယ်ပါ။

    ![Type azure machine learning.](../../../../../../translated_images/my/01-01-type-azml.acae6c5455e67b4b.webp)

2. လမ်းညွှန်မီνούမှ **+ Create** ကို ရွေးချယ်ပါ။

3. လမ်းညွှန်မီνούမှ **New workspace** ကို ရွေးချယ်ပါ။

    ![Select new workspace.](../../../../../../translated_images/my/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. အောက်ပါအချက်များကို ပြုလုပ်ပါ-

    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုလိုသော **Resource group** ကို ရွေးပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - **Workspace Name** ထည့်ပါ။ အမှတ်တံဆိပ်ထူးခြားရမည်။
    - အသုံးပြုလိုသော **Region** ကို ရွေးပါ။
    - အသုံးပြုလိုသော **Storage account** ကို ရွေးပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Key vault** ကို ရွေးပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Application insights** ကို ရွေးပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Container registry** ကို ရွေးပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။

    ![Fill azure machine learning.](../../../../../../translated_images/my/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Review + Create** ကို ရွေးချယ်ပါ။

6. **Create** ကို ရွေးချယ်ပါ။

### Azure Subscription တွင် GPU ကို အရေအတွက် တောင်းဆိုခြင်း

ဤ သင်ခန်းစာတွင် Phi-3 မော်ဒယ်ကို fine-tune နှင့် တင်ပို့ရာတွင် GPU များကို အသုံးပြုမည်ဖြစ်သည်။ Fine-tuning အတွက် *Standard_NC24ads_A100_v4* GPU ကို အသုံးပြုမည်ဖြစ်၍ အရေအတွက် တောင်းဆိုရန် လိုအပ်သည်။ Deployment အတွက် *Standard_NC6s_v3* GPU ကို အသုံးပြုမည်ဖြစ်ပြီး ၎င်းအတွက်လည်း အသုံးပြုခွင့် တောင်းဆိုရမည်။

> [!NOTE]
>
> GPU ထောက်ပံ့မှုမှာ Pay-As-You-Go subscription များ(စံတမ်း subscription) အတွက်သာဖြစ်ပြီး benefit subscription များ မထောက်ပံ့သေးပါ။
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) မှ ဝင်ရောက်ပါ။

1. *Standard NCADSA100v4 Family* အတွက် quota တောင်းဆိုရန် အောက်ပါအတိုင်း ဆောင်ရွက်ပါ-

    - ဘားဘယ်ဖက် tab မှ **Quota** ကို ရွေးပါ။
    - အသုံးပြုမည့် **Virtual machine family** ကို ရွေးပါ။ ဥပမာ - *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* ကို ရွေးပါ၊ ၎င်းတွင် *Standard_NC24ads_A100_v4* GPU ပါဝင်သည်။
    - လမ်းညွှန်မီνούမှ **Request quota** ကို ရွေးပါ။

        ![Request quota.](../../../../../../translated_images/my/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota စာမျက်နှာတွင် အသုံးပြုလိုသော **New cores limit** ကို ထည့်ပါ၊ ဥပမာ 24။
    - Request quota စာမျက်နှာတွင် **Submit** ကို နှိပ်၍ GPU quota ကို တောင်းဆိုပါ။

1. *Standard NCSv3 Family* အတွက် quota တောင်းဆိုရန် အောက်ပါအတိုင်း ဆောင်ရွက်ပါ-

    - ဘားဘယ်ဖက် tab မှ **Quota** ကို ရွေးပါ။
    - အသုံးပြုမည့် **Virtual machine family** ကို ရွေးပါ။ ဥပမာ - *Standard NCSv3 Family Cluster Dedicated vCPUs* ကို ရွေးပါ၊ ၎င်းတွင် *Standard_NC6s_v3* GPU ပါဝင်သည်။
    - လမ်းညွှန်မီνούမှ **Request quota** ကို ရွေးပါ။
    - Request quota စာမျက်နှာတွင် အသုံးပြုလိုသော **New cores limit** ကို ထည့်ပါ၊ ဥပမာ 24။
    - Request quota စာမျက်နှာတွင် **Submit** ကို နှိပ်၍ GPU quota ကို တောင်းဆိုပါ။

### Role တစ်ခု ခန့်အပ်ခြင်း

မော်ဒယ်များကို fine-tune ပြုလုပ်ခြင်းနှင့် တင်ပို့ခြင်း အတွက် User Assigned Managed Identity (UAI) တစ်ခု ဖန်တီးပြီး သင့်လျော်သော ခွင့်များ ခန့်အပ်ရမည်ဖြစ်သည်။ ၎င်း UAI သည် deployment အတွက် အထောက်အထား olarak အသုံးပြုမည်ဖြစ်သည်။

#### User Assigned Managed Identity(UAI) ဖန်တီးခြင်း

1. Portal စာမျက်နှာအပေါ်ယံရှိ **ရှာဖွေမှုဘား**တွင် *managed identities* ဟူ၍ရိုက်ထည့်ပြီး ပြသသောရွေးချယ်စရာများထဲမှ **Managed Identities** ကို ရွေးချယ်ပါ။

    ![Type managed identities.](../../../../../../translated_images/my/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** ကို ရွေးချယ်ပါ။

    ![Select create.](../../../../../../translated_images/my/03-02-select-create.92bf8989a5cd98f2.webp)

1. အောက်ပါအချက်များကို ပြုလုပ်ပါ-

    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုလိုသော **Resource group** ကို ရွေးပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Region** ကို ရွေးပါ။
    - **Name** ထည့်ပါ။ အမှတ်တံဆိပ်ထူးခြားရမည်။

    ![Select create.](../../../../../../translated_images/my/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** ကို ရွေးချယ်ပါ။

1. **+ Create** ကို ရွေးချယ်ပါ။

#### Managed Identity သို့ Contributor role ခန့်အပ်ခြင်း

1. ဖန်တီးပြီးသား Managed Identity အရင်းအမြစ်သို့ သွားပါ။

1. ဘားဘယ်ဖက် tab မှ **Azure role assignments** ကို ရွေးပါ။

1. လမ်းညွှန်မီνούမှ **+Add role assignment** ကို ရွေးပါ။

1. Add role assignment စာမျက်နှာ၌ အောက်ပါအချက်များကို ပြုလုပ်ပါ-
    - **Scope** ကို **Resource group** သို့ သတ်မှတ်ပါ။
    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Resource group** ကို ရွေးပါ။
    - **Role** ကို **Contributor** ဟု ရွေးပါ။

    ![Fill contributor role.](../../../../../../translated_images/my/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** ကို နှိပ်ပါ။

#### Managed Identity သို့ Storage Blob Data Reader role ခန့်အပ်ခြင်း

1. Portal စာမျက်နှာအပေါ်ယံရှိ **ရှာဖွေမှုဘား**တွင် *storage accounts* ဟူ၍ရိုက်ထည့်ပြီး ပြသသောရွေးချယ်စရာများထဲမှ **Storage accounts** ကို ရွေးပါ။

    ![Type storage accounts.](../../../../../../translated_images/my/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Azure Machine Learning workspace အတွက် သတ်မှတ်ထားသော storage account ကို ရွေးပါ။ ဥပမာ - *finetunephistorage*။

1. Add role assignment စာမျက်နှာသို့ ရောက်ရှိရန် အောက်ပါအတိုင်း ဆောင်ရွက်ပါ-

    - ဖန်တီးထားသော Azure Storage account သို့ သွားပါ။
    - ဘားဘယ်ဖက် tab မှ **Access Control (IAM)** ကို ရွေးပါ။
    - လမ်းညွှန်မီνούမှ **+ Add** ကို ရွေးပါ။
    - လမ်းညွှန်မီνούမှ **Add role assignment** ကို ရွေးပါ။

    ![Add role.](../../../../../../translated_images/my/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment စာမျက်နှာတွင် အောက်ဖော်ပြပါအတိုင်း လုပ်ဆောင်ပါ-

    - Role စာမျက်နှာ၌ **Storage Blob Data Reader** ကို ရှာဖွေ၍ ရွေးချယ်ပါ။
    - Role စာမျက်နှာ၌ **Next** ကို နှိပ်ပါ။
    - Members စာမျက်နှာ၌ **Assign access to** အနေဖြင့် **Managed identity** ကို ရွေးချယ်ပါ။
    - Members စာမျက်နှာ၌ **+ Select members** ကို နှိပ်ပါ။
    - Select managed identities စာမျက်နှာ၌ သင့် Azure **Subscription** ကို ရွေးပါ။
    - Select managed identities စာမျက်နှာ၌ **Managed identity** အဖြစ် **Manage Identity** ကို ရွေးပါ။
    - Select managed identities စာမျက်နှာ၌ ဖန်တီးပြီးသား Manage Identity ကို ရွေးပါ။ ဥပမာ - *finetunephi-managedidentity*။
    - Select managed identities စာမျက်နှာ၌ **Select** ကို နှိပ်ပါ။

    ![Select managed identity.](../../../../../../translated_images/my/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** ကို ရွေးချယ်ပါ။

#### Managed Identity သို့ AcrPull role ခန့်အပ်ခြင်း

1. Portal စာမျက်နှာအပေါ်ယံရှိ **ရှာဖွေမှုဘား**တွင် *container registries* ဟူ၍ရိုက်ထည့်ပြီး ပြသသောရွေးချယ်စရာများထဲမှ **Container registries** ကို ရွေးပါ။

    ![Type container registries.](../../../../../../translated_images/my/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning workspace နှင့် သက်ဆိုင်ရာ container registry ကို ရွေးပါ။ ဥပမာ - *finetunephicontainerregistry*

1. Add role assignment စာမျက်နှာသို့ ရောက်ရှိရန် အောက်ပါအတိုင်း ဆောင်ရွက်ပါ-

    - ဘားဘယ်ဖက် tab မှ **Access Control (IAM)** ကို ရွေးပါ။
    - လမ်းညွှန်မီνούမှ **+ Add** ကို ရွေးပါ။
    - လမ်းညွှန်မီνούမှ **Add role assignment** ကို ရွေးပါ။

1. Add role assignment စာမျက်နှာ၌ အောက်ပါအတိုင်း ဆောင်ရွက်ပါ-

    - Role စာမျက်နှာ၌ *AcrPull* ကို ရှာဖွေနိုင်ရန် ရိုက်ထည့်ပြီး **AcrPull** ကို ရွေးချယ်ပါ။
    - Role စာမျက်နှာ၌ **Next** ကို နှိပ်ပါ။
    - Members စာမျက်နှာ၌ **Assign access to** အနေဖြင့် **Managed identity** ကို ရွေးချယ်ပါ။
    - Members စာမျက်နှာ၌ **+ Select members** ကို နှိပ်ပါ။
    - Select managed identities စာမျက်နှာ၌ သင့် Azure **Subscription** ကို ရွေးပါ။
    - Select managed identities စာမျက်နှာ၌ **Managed identity** အဖြစ် **Manage Identity** ကို ရွေးပါ။
    - Select managed identities စာမျက်နှာ၌ ဖန်တီးပြီးသား Manage Identity ကို ရွေးပါ။ ဥပမာ - *finetunephi-managedidentity*။
    - Select managed identities စာမျက်နှာ၌ **Select** ကို နှိပ်ပါ။
    - **Review + assign** ကို ရွေးချယ်ပါ။

### ပရောဂျက် စီစဉ်တပ်ဆင်ခြင်း

Fine-tuning အတွက် လိုအပ်သော ဒေတာများကို ဒေါင်းလုပ် ဆွဲရန် ပတ်ဝန်းကျင်ကို လုံခြုံစွာ ပြင်ဆင်မည်ဖြစ်သည်။

ဤ လေ့ကျင့်ခန်းတွင်-

- အတွင်း၌ လုပ်ဆောင်ရန် ဖိုဒါကို ဖန်တီးမည်။
- Virtual environment တစ်ခုဖန်တီးမည်။
- လိုအပ်သော package များကို ထည့်သွင်းမည်။
- ဒေတာဒေါင်းလုပ်ဆွဲရန် *download_dataset.py* ဖိုင်ကို ဖန်တီးမည်။

#### အတွင်း၌ လုပ်ရန် ဖိုဒါ တစ်ခုဖန်တီးခြင်း

1. Terminal ပြတင်းပေါ် ဖွင့်ပြီး ကျယ်သော လမ်းကြောင်းတွင် *finetune-phi* ဟု အမည်ပေးထားသော ဖိုဒါတစ်ခု ဖန်တီးရန် အောက်ပါ ကုဒ်ကို ရိုက်ထည့်ပါ။

    ```console
    mkdir finetune-phi
    ```

2. Terminal တွင် *finetune-phi* ဖိုဒါသို့ ရောက်ရှိရန် အောက်ပါ ကုဒ်ကို ရိုက်ထည့်ပါ။

    ```console
    cd finetune-phi
    ```

#### Virtual environment တစ်ခုဖန်တီးခြင်း

1. Terminal တွင် *.venv* ဟု အမည်ပေးထားသော virtual environment တစ်ခု ဖန်တီးရန် အောက်ပါ ကုဒ်ကို ရိုက်ထည့်ပါ။
    ```console
    python -m venv .venv
    ```

2. သင့် terminal ထဲမှာ အောက်ပါ command ကိုရိုက်ထည့်ပြီး virtual environment ကို လှုပ်အားဖြင့်ဖွင့်ပါ။

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> အကောင်အထည်ဖော်နိုင်ခဲ့ပါက command prompt မတိုင်မီ *(.venv)* ကို တွေ့မြင်ရပါမယ်။

#### လိုအပ်သော package များကို 설치 လုပ်ခြင်း

1. terminal ထဲမှာ အောက်ပါ command များကို ရိုက်ထည့်ပြီး လိုအပ်သော package များကို 설치 လုပ်ပါ။

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` ဖိုင်ကို ဖန်တီးပါ။

> [!NOTE]
> ပြည့်စုံသောဖိုင်ဖွဲ့စည်းမှု -
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** ကို ဖွင့်ပါ။

1. မီနူးဘားမှ **File** ကို ရွေးချယ်ပါ။

1. **Open Folder** ကို ရွေးချယ်ပါ။

1. သင်ဖန်တီးထားသော *finetune-phi* ဖိုဒါကို ရွေးချယ်ပါ၊ ဒါက *C:\Users\yourUserName\finetune-phi* အတွင်းတွင် ရှိပါတယ်။

    ![Select the folder that you created.](../../../../../../translated_images/my/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code နောက်ကျောဘက် (left pane) တွင် ရိုက်နှိပ်ပြီး **New File** ကို ရွေး၍ *download_dataset.py* ဆိုသောဖိုင်အသစ်ကို ဖန်တီးပါ။

    ![Create a new file.](../../../../../../translated_images/my/04-02-create-new-file.cf9a330a3a9cff92.webp)

### fine-tuning အတွက် dataset ပြင်ဆင်ခြင်း

ဒီ လေ့လာမှုမှာ သင်သည် *download_dataset.py* ဖိုင်ကို run လုပ်ပြီး *ultrachat_200k* dataset များကို သင့်ဒေသခံ environment သို့ download လုပ်ပါမည်။ ထို့နောက် အဲဒီ dataset များကို အသုံးပြုပြီး Phi-3 module ကို Azure Machine Learning မှာ fine-tune လုပ်မှာ ဖြစ်ပါတယ်။

ဒီလေ့ကျင့်ရေးမှာသင်လုပ်ရမယ့် အရာတွေကတော့ -

- *download_dataset.py* ဖိုင်ထဲ ကုတ်တွေ ထည့်ရေးခြင်းဖြင့် dataset များကို download လုပ်ရန်။
- အဆိုပါ *download_dataset.py* ဖိုင်ကို သွားပြီး run လုပ်ခြင်းဖြင့် ဒေသခံ environment သို့ dataset များရယူခြင်း။

#### *download_dataset.py* ဖြင့် သင့် dataset ကို တင်ပါ

1. Visual Studio Code မှာ *download_dataset.py* ဖိုင်ကို ဖွင့်ပါ။

1. အောက်ပါ code ကို *download_dataset.py* ဖိုင်ထဲ ထည့်ပါ။

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # သတ်မှတ်ထားသောနာမည်၊ ပုံစံဖြင့် dataset ကို load ပြုလုပ်ရန်နှင့် ကျပ်တည်းခြားနားမှုအရ လုပ်ဆောင်ရန်
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # dataset ကို train နှင့် test စုစည်းမှုများအဖြစ် ခွဲခြားရန် (train ၈၀%, test ၂၀%)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # directory မရှိပါက ဖန်တီးရန်
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # ဖိုင်ကို စာရေးမုဒ်ဖြင့်ဖွင့်ရန်
        with open(filepath, 'w', encoding='utf-8') as f:
            # dataset ထဲရှိ တစ်ခုချင်း record များအား iterate ပြုလုပ်ရန်
            for record in dataset:
                # record ကို JSON object အဖြစ် dump ပြုလုပ်၍ ဖိုင်ထဲသို့ ရေးရန်
                json.dump(record, f)
                # record များ ခွဲရန် newline အက္ခရာရေးရန်
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ULTRACHAT_200k dataset ကို သတ်မှတ်ထားသော ပုံစံနှင့် ကျပ်တည်းခြားနာမှုနှုန်းဖြင့် load ပြုလုပ်ခြင်းနှင့် ခွဲခြားခြင်း
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # ခွဲထားသော train နှင့် test dataset များ ထုတ်ယူရန်
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # train dataset ကို JSONL ဖိုင်အဖြစ် သိမ်းဆည်းရန်
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # test dataset ကို အခြား JSONL ဖိုင်တစ်ခုအဖြစ် သိမ်းဆည်းရန်
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. terminal ထဲတွင် အောက်ပါ command ကိုရိုက်ထည့်ပြီး script run လိုက်ပါ၊ ဒါက သင့်ဒေသခံ environment သို့ dataset ကို download လုပ်ပေးပါလိမ့်မယ်။

    ```console
    python download_dataset.py
    ```

1. dataset များ *finetune-phi/data* ဖိုဒါတွင် ဂုဏ်ယူစွာ သိမ်းဆည်းထားသည်ဟု သေချာစစ်ဆေးပါ။

> [!NOTE]
>
> #### Dataset အရွယ်အစားနှင့် fine-tuning အချိန် ဒေါ်တွေးချက်
>
> ဒီ သင်ခန်းစာမှာ dataset ရဲ့ 1% (`split='train[:1%]'`) ကိုသာ သုံးပါမယ်။ ဒါကြောင့် ဒေတာအမျိုးအစားကို ပြင်းပြင်းထန်ထန်လျော့ချပေးပြီး upload နဲ့ fine-tuning နှစ်ခုလုံးကိုလျင်မြန်စေပါတယ်။ သင့် training အချိန်နဲ့မော်ဒယ်ထိရောက်မှုကို ဆင်ခြင်ပြီး မူတည်၍ အရာရာကို လိုအပ်သလို အချိုးချိန်ကိုညှိနိုင်ပါတယ်။ Dataset ၏ သေးငယ်သော အပိုင်းကို အသုံးပြုခြင်းသည် fine-tuning အလုပ်အချိန်ကိုလျော့ချပေးပြီး ဒီသင်ခန်းစာအတွက် လွယ်ကူစေပါသည်။

## Scenario 2: Phi-3 မော်ဒယ်ကို fine-tune လုပ်ခြင်းနှင့် Azure Machine Learning Studio တွင် Deploy လုပ်ခြင်း

### Phi-3 မော်ဒယ်ကို fine-tune လုပ်ခြင်း

ဒီ လေ့ကျင့်ရေးမှာ သင်သည် Azure Machine Learning Studio တွင် Phi-3 မော်ဒယ်ကို fine-tune လုပ်ပါမည်။

ဒီ လေ့ကျင့်ရေးမှာ သင်လုပ်ကိုင်မယ့်အရာတွေကတော့ -

- fine-tuning အတွက် computer cluster ဖန်တီးခြင်း။
- Azure Machine Learning Studio မှာ Phi-3 မော်ဒယ်ကို fine-tune လုပ်ခြင်း။

#### fine-tuning အတွက် computer cluster ဖန်တီးခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ကို သွားပါ။

1. ဘယ်ဘက် tab မှ **Compute** ကို ရွေးချယ်ပါ။

1. navigation menu ထဲက **Compute clusters** ကို ရွေးချယ်ပါ။

1. **+ New** ကို နှိပ်ပါ။

    ![Select compute.](../../../../../../translated_images/my/06-01-select-compute.a29cff290b480252.webp)

1. အောက်ပါ အဆင့်များကို ပြုလုပ်ပါ -

    - သင်အသုံးပြုမယ့် **Region** ကိုရွေးပါ။
    - **Virtual machine tier** ကို **Dedicated** ဖြင့်ရွေးချယ်ပါ။
    - **Virtual machine type** ကို **GPU** ဖြင့်ရွေးချယ်ပါ။
    - **Virtual machine size** filter ကို **Select from all options** ဖြင့်ရွေးပါ။
    - **Virtual machine size** အနေနဲ့ **Standard_NC24ads_A100_v4** ကိုရွေးပါ။

    ![Create cluster.](../../../../../../translated_images/my/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** ကို နှိပ်ပါ။

1. အောက်ပါ အချက်အလက်များကို ထည့်သွင်းပါ -

    - **Compute name** ထည့်ပါ။ ဤအရာသည် unique ဖြစ်ရပါမည်။
    - **Minimum number of nodes** ကို **0** ဖြင့်ရွေးပါ။
    - **Maximum number of nodes** ကို **1** ဖြင့်ရွေးပါ။
    - **Idle seconds before scale down** ကို **120** ဖြင့်ရွေးပါ။

    ![Create cluster.](../../../../../../translated_images/my/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** ကို နှိပ်ပါ။

#### Phi-3 မော်ဒယ်ကို fine-tune လုပ်ခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ကို သွားပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace ကို ရွေးချယ်ပါ။

    ![Select workspace that you created.](../../../../../../translated_images/my/06-04-select-workspace.a92934ac04f4f181.webp)

1. အောက်ဖော်ပြပါ အချက်များကို ဆောင်ရွက်ပါ -

    - ဘယ်ဘက် tab မှ **Model catalog** ကို ရွေးချယ်ပါ။
    - **search bar** မှာ *phi-3-mini-4k* ကို ရိုက်ထည့်ပြီး ဖော်ပြသောရွေးချယ်စရာများထဲမှ **Phi-3-mini-4k-instruct** ကို ရွေးပါ။

    ![Type phi-3-mini-4k.](../../../../../../translated_images/my/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. navigation menu မှ **Fine-tune** ကို ရွေးချယ်ပါ။

    ![Select fine tune.](../../../../../../translated_images/my/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. အောက်ပါအချက်များကို ဖြည့်သွင်းပါ -

    - **Select task type** ကို **Chat completion** ဖြင့် ရွေးချယ်ပါ။
    - **+ Select data** ကို နှိပ်ပြီး **Training data** ကို upload လုပ်ပါ။
    - Validation data upload အမျိုးအစားကို **Provide different validation data** ဖြင့်ရွေးပါ။
    - **+ Select data** ကို နှိပ်ပြီး **Validation data** ကို upload လုပ်ပါ။

    ![Fill fine-tuning page.](../../../../../../translated_images/my/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> **Advanced settings** ကို ရွေးပြီး **learning_rate** နဲ့ **lr_scheduler_type** စတဲ့ options တွေကို အလိုက်သင့် စိတ်ကြိုက် ပြင်ဆင်နိုင်ပါတယ်၊ ဒါမှ fine-tuning လုပ်ငန်းစဉ်အတွက် ပိုမိုကောင်းမွန်စေပါသည်။

1. **Finish** ကို နှိပ်ပါ။

1. ဒီ လေ့ကျင့်ရေးမှာ သင် Azure Machine Learning ဖြင့် Phi-3 မော်ဒယ်ကို အောင်မြင်စွာ fine-tune လုပ်နိုင်ခဲ့ပြီဖြစ်သည်။ fine-tuning လုပ်ငန်းစဉ်မှာ အချိန်ကြာမြင့်နိုင်ပါသည်။ fine-tuning job run လုပ်ပြီးပါက အပြီးသတ်ရန် စောင့်ဆိုင်းရမည်ဖြစ်ပြီး အလုပ်အခြေအနေကို Azure Machine Learning workspace ၏ ဘယ်ဘက် tab တွင်ရှိသော Jobs tab တွင်စစ်ဆေးနိုင်ပါသည်။ နောက်တစ်ပိုင်းတွင် fine-tuned model ကို deploy လုပ်ပြီး Prompt flow နဲ့ ပေါင်းစည်းသွားပါမည်။

    ![See finetuning job.](../../../../../../translated_images/my/06-08-output.2bd32e59930672b1.webp)

### Fine-tuned Phi-3 မော်ဒယ်ကို deploy လုပ်ခြင်း

Fine-tuned Phi-3 မော်ဒယ်ကို Prompt flow နဲ့ ပေါင်းစည်းရန်၊ မော်ဒယ်ကို real-time inference အတွက် အသုံးပြုနိုင်အောင် deploy လုပ်ဖို့ လိုအပ်ပါတယ်။ ဒီလုပ်ငန်းစဉ်မှာ model ကို register လုပ်ခြင်း၊ online endpoint တစ်ခု ဖန်တီးခြင်းနဲ့ model ကို deploy လုပ်ခြင်း ပါဝင်သည်။

ဒီ လေ့ကျင့်ရေးမှာ သင်လုပ်မယ့်အရာတွေကတော့ -

- Azure Machine Learning workspace အတွင်း fine-tuned မော်ဒယ်ကို မှတ်ပုံတင်ခြင်း။
- Online endpoint တစ်ခု ဖန်တီးခြင်း။
- မှတ်ပုံတင်ထားသော fine-tuned Phi-3 မော်ဒယ် ကို deploy လုပ်ခြင်း။

#### Fine-tuned မော်ဒယ်ကို မှတ်ပုံတင်ခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ကို သွားပါ။

1. သင့်ဖန်တီးထားသော Azure Machine Learning workspace ကို ရွေးချယ်ပါ။

    ![Select workspace that you created.](../../../../../../translated_images/my/06-04-select-workspace.a92934ac04f4f181.webp)

1. ဘယ်ဘက် tab မှ **Models** ကို ရွေးချယ်ပါ။
1. **+ Register** ကို နှိပ်ပါ။
1. **From a job output** ကို ရွေးချယ်ပါ။

    ![Register model.](../../../../../../translated_images/my/07-01-register-model.ad1e7cc05e4b2777.webp)

1. သင်ဖန်တီးခဲ့သော job ကို ရွေးချယ်ပါ။

    ![Select job.](../../../../../../translated_images/my/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** ကို နှိပ်ပါ။

1. **Model type** ကို **MLflow** အဖြစ် ရွေးချယ်ပါ။

1. **Job output** မှာ အလိုအလျောက် ရွေးထားပြီး ဖြစ်ရပါမည်။

    ![Select output.](../../../../../../translated_images/my/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** ကို နှိပ်ပါ။

3. **Register** ကို နှိပ်ပါ။

    ![Select register.](../../../../../../translated_images/my/07-04-register.fd82a3b293060bc7.webp)

4. သင်မှတ်ပုံတင်ထားသော မော်ဒယ်ကို ဘယ်ဘက် tab ထဲမှ **Models** မီနူးတွင် ဖော်ပြပါက ကြည့်ရှုနိုင်ပါသည်။

    ![Registered model.](../../../../../../translated_images/my/07-05-registered-model.7db9775f58dfd591.webp)

#### Fine-tuned မော်ဒယ်ကို deploy လုပ်ခြင်း

1. သင့်ဖန်တီးထားသော Azure Machine Learning workspace သို့ သွားပါ။

1. ဘယ်ဘက် tab မှ **Endpoints** ကို ရွေးချယ်ပါ။

1. navigation menu မှ **Real-time endpoints** ကို ရွေးပါ။

    ![Create endpoint.](../../../../../../translated_images/my/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** ကို နှိပ်ပါ။

1. သင်မှတ်ပုံတင်ထားသည့် မော်ဒယ်ကို ရွေးချယ်ပါ။

    ![Select registered model.](../../../../../../translated_images/my/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** ကို နှိပ်ပါ။

1. အောက်ပါ အချက်အလက်များ ထည့်သွင်းပါ -

    - **Virtual machine** ကို *Standard_NC6s_v3* အဖြစ် ရွေးချယ်ပါ။
    - သင်အသုံးပြုလိုသည့် **Instance count** ကို ရွေးချယ်ပါ၊ ဥပမာ *1* ဖြစ်စေ။
    - **Endpoint** ကို **New** နှင့် ရွေးပြီး endpoint အသစ် ဖန်တီးပါ။
    - **Endpoint name** ကို ထည့်ပါ။ ဤအရာသည် အထူးထူးခြားသည့် တန်ဖိုးဖြစ်ရမည်။
    - **Deployment name** ကို ထည့်ပါ။ ဤအရာသည် အထူးထူးခြားသည့် တန်ဖိုးဖြစ်ရမည်။

    ![Fill the deployment setting.](../../../../../../translated_images/my/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** ကို နှိပ်ပါ။

> [!WARNING]
> သင့်အကောင့်ထံမှ အပိုကျပ်ငွေများရှောင်ရှားရန်၊ Azure Machine Learning workspace တွင်ဖန်တီးထားသော endpoint များအား ဖျက်ပစ်ရန် သေချာပါစေရန်။
>

#### Azure Machine Learning Workspace တွင် deployment အခြေအနေ စစ်ဆေးခြင်း

1. သင့်ဖန်တီးထားသော Azure Machine Learning workspace သို့ သွားပါ။

1. ဘယ်ဘက် tab မှ **Endpoints** ကို ရွေးချယ်ပါ။

1. သင်ဖန်တီးထားသော endpoint ကို ရွေးချယ်ပါ။

    ![Select endpoints](../../../../../../translated_images/my/07-09-check-deployment.325d18cae8475ef4.webp)

1. ဒီစာမျက်နှာတွင် deployment လုပ်ငန်းစဉ်အတွင်း endpoints များကို စီမံခန့်ခွဲနိုင်ပါသည်။

> [!NOTE]
> Deployment အပြီးသတ်သည့်နောက်၊ **Live traffic** သည် **100%** အဖြစ် သတ်မှတ်ထားကြောင်းသေချာပါစေ။ မဟုတ်လျှင် **Update traffic** ကို နှိပ်ကာ traffic ကို ပြင်ဆင်ပါ။ Traffic ကို 0% သတ်မှတ်ထားသည်ဆိုလျှင် မော်ဒယ်ကို စမ်းသပ်၍ မရပါ။
>
> ![Set traffic.](../../../../../../translated_images/my/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenario 3: Prompt flow နှင့် ပေါင်းစည်းခြင်းနှင့် Microsoft Foundry တွင် အကွ personnalisée Phi-3 မော်ဒယ်ဖြင့် စကားပြောခြင်း

### custom Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစည်းခြင်း

fine-tuned မော်ဒယ် တပ်ဆင်ပြီးနောက် Prompt Flow နှင့်ပေါင်းစည်းပြီး သင့်မော်ဒယ်ကို လက်တွေ့ အချိန်နှင့်တပြေးညီ လုပ်ဆောင်နိုင်မည့် app မျိုးများတွင် အသုံးပြုနိုင်သွားပါပြီ။

ဒီ လေ့ကျင့်ရေးတွင် သင်လုပ်ငန်းများမှာ -

- Microsoft Foundry Hub ဖန်တီးခြင်း။
- Microsoft Foundry Project ဖန်တီးခြင်း။
- Prompt flow ဖန်တီးခြင်း။
- fine-tuned Phi-3 မော်ဒယ်အတွက် custom connection ထည့်သွင်းခြင်း။
- သင့် custom Phi-3 မော်ဒယ်နှင့် chat လုပ်ရန် Prompt flow ကို စီစဉ်ခြင်း။

> [!NOTE]
> Azure ML Studio ကို အသုံးပြုပြီး Promptflow နှင့် ပေါင်းစည်းနိုင်ပါသည်။ ယင်းပေါင်းစည်းမှု လုပ်ငန်းစဉ်သည် Azure ML Studio တွင်လည်း သုံးနိုင်သည်။

#### Microsoft Foundry Hub ဖန်တီးခြင်း

Project ဖန်တီးမပြုမီ Hub တစ်ခုဖန်တီးရပါမည်။ Hub သည် Resource Group အဖြစ် လုပ်ဆောင်ကာ Microsoft Foundry အတွင်း Project များစွာကို စည်းရုံးစီမံခန့်ခွဲနိုင်သည့် အဖွဲ့အစည်းဖြစ်ပါသည်။
1. Visit [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)။

1. ဘယ်ဘက်ဘားမှ **All hubs** ကိုရွေးချယ်ပါ။

1. နေဗီဂေးရှင်းမူးနူးမှ **+ New hub** ကိုရွေးချယ်ပါ။

    ![Create hub.](../../../../../../translated_images/my/08-01-create-hub.8f7dd615bb8d9834.webp)

1. လုပ်ဆောင်မှုများကိုအောက်ပါအတိုင်းပြုလုပ်ပါ-

    - **Hub name** ကိုထည့်သွင်းပါ။ ဤအမည်မှာ တူညီမှုမရှိသောတန်ဖိုးဖြစ်ရမည်။
    - သင့် Azure **Subscription** ကိုရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Resource group** ကိုရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - အသုံးပြုလိုသော **Location** ကိုရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Connect Azure AI Services** ကိုရွေးချယ်ပါ (လိုအပ်ပါက အသစ်တစ်ခုဖန်တီးပါ)။
    - **Connect Azure AI Search** ကို **Skip connecting** အဖြစ်ရွေးချယ်ပါ။

    ![Fill hub.](../../../../../../translated_images/my/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** ကိုရွေးချယ်ပါ။

#### Microsoft Foundry Project ဖန်တီးခြင်း

1. ဖန်တီးထားသော Hub အတွင်းမှ ဘယ်ဘက်ဘားမှ **All projects** ကိုရွေးချယ်ပါ။

1. နေဗီဂေးရှင်းမူးနူးမှ **+ New project** ကိုရွေးချယ်ပါ။

    ![Select new project.](../../../../../../translated_images/my/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** ထည့်သွင်းပါ။ ဤအမည်မှာ တူညီမှုမရှိသောတန်ဖိုးဖြစ်ရမည်။

    ![Create project.](../../../../../../translated_images/my/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** ကိုရွေးချယ်ပါ။

#### fine-tuned Phi-3 မော်ဒယ်အတွက် custom connection ထည့်ခြင်း

သင့်ရဲ့ custom Phi-3 မော်ဒယ်ကို Prompt flow နှင့်ပေါင်းစပ်ရန်၊ မော်ဒယ်၏ endpoint နှင့် key ကို custom connection အနေနှင့်သိမ်းဆည်းရန်လိုအပ်သည်။ ဤဖော်ပြချက်ကနေ Prompt flow တွင် သင့် custom Phi-3 မော်ဒယ်ကို အသုံးပြုခွင့်ရရှိစေပါသည်။

#### fine-tuned Phi-3 မော်ဒယ်အတွက် api key နှင့် endpoint uri ကို သတ်မှတ်ခြင်း

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)။

1. သင့်ဖန်တီးထားသော Azure Machine learning workspace သို့သွားပါ။

1. ဘယ်ဘက်ဘားမှ **Endpoints** ကိုရွေးချယ်ပါ။

    ![Select endpoints.](../../../../../../translated_images/my/08-06-select-endpoints.aff38d453bcf9605.webp)

1. ဖန်တီးထားသော endpoint ကိုရွေးချယ်ပါ။

    ![Select endpoints.](../../../../../../translated_images/my/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. နေဗီဂေးရှင်းမူးနူးမှ **Consume** ကိုရွေးချယ်ပါ။

1. သင့် **REST endpoint** နှင့် **Primary key** ကိုကူးယူပါ။

    ![Copy api key and endpoint uri.](../../../../../../translated_images/my/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Custom Connection ထည့်ခြင်း

1. Visit [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)။

1. သင့်ဖန်တီးထားသော Microsoft Foundry project သို့သွားပါ။

1. ဖန်တီးထားသော Project အတွင်း ဘယ်ဘက်ဘားမှ **Settings** ကိုရွေးချယ်ပါ။

1. **+ New connection** ကိုရွေးချယ်ပါ။

    ![Select new connection.](../../../../../../translated_images/my/08-09-select-new-connection.02eb45deadc401fc.webp)

1. နေဗီဂေးရှင်းမူးနူးမှ **Custom keys** ကိုရွေးချယ်ပါ။

    ![Select custom keys.](../../../../../../translated_images/my/08-10-select-custom-keys.856f6b2966460551.webp)

1. အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - **+ Add key value pairs** ကိုရွေးချယ်ပါ။
    - key name အဖြစ် **endpoint** ထည့်ပြီး Azure ML Studio မှကူးယူထားသော endpoint ကို value field တွင်ကပ်ပါ။
    - ပြန်လည် **+ Add key value pairs** ကိုရွေးချယ်ပါ။
    - key name အဖြစ် **key** ထည့်ပြီး Azure ML Studio မှကူးယူထားသော key ကို value field တွင်ကပ်ပါ။
    - ချိတ်ဆက်ထားသည့် keys များထည့်ပြီးပါက၊ key ကို ဖော်ပြခြင်းမဖြစ်စေရန် **is secret** ကိုရွေးချယ်ပါ။

    ![Add connection.](../../../../../../translated_images/my/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** ကိုရွေးချယ်ပါ။

#### Prompt flow ဖန်တီးခြင်း

Microsoft Foundry တွင် custom connection ထည့်ပြီးပြီဖြစ်သည်။ ယခု အောက်ပါအဆင့်များ အတိုင်း Prompt flow အသစ်တစ်ခု ဖန်တီးပါ။ ထို့နောက် Prompt flow ကို custom connection နှင့် ချိတ်ဆက်ပြီး fine-tuned မော်ဒယ်ကို Prompt flow အတွင်း အသုံးပြုနိုင်ပါမည်။

1. သင့်ဖန်တီးထားသော Microsoft Foundry project သို့သွားပါ။

1. ဘယ်ဘက်ဘားမှ **Prompt flow** ကိုရွေးချယ်ပါ။

1. နေဗီဂေးရှင်းမူးနူးမှ **+ Create** ကိုရွေးချယ်ပါ။

    ![Select Promptflow.](../../../../../../translated_images/my/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. နေဗီဂေးရှင်းမူးနူးမှ **Chat flow** ကိုရွေးချယ်ပါ။

    ![Select chat flow.](../../../../../../translated_images/my/08-13-select-flow-type.2ec689b22da32591.webp)

1. အသုံးပြုမည့် **Folder name** ကိုထည့်ပါ။

    ![Enter name.](../../../../../../translated_images/my/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** ကိုရွေးချယ်ပါ။

#### သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောရန် Prompt flow ကိုချိန်ညှိခြင်း

fine-tuned Phi-3 မော်ဒယ်ကို Prompt flow အတွင်း ပေါင်းစပ်ရန်လိုအပ်သည်။ သို့သော် ရှိပြီးသား Prompt flow ကို သင်၏လိုချင်သည့်အတိုင်း မဖန်တီးထားသေးသောကြောင့် Prompt flow ကို ပြန်လည်ဒီဇိုင်းပြုလုပ်ရပါမည်။

1. ဒါ့အတွက် Prompt flow ထဲတွင်ရှိသည့် flow ကို ပြန်လည်တည်ဆောက်ဖို့အတွက် အောက်ပါအတိုင်း လုပ်ဆောင်ပါ-

    - **Raw file mode** ကိုရွေးချယ်ပါ။
    - *flow.dag.yml* ဖိုင်ထဲရှိ ရှိပြီးသား code အားလုံးကို ဖျက်ပါ။
    - *flow.dag.yml* ဖိုင်ထဲ အောက်ပါ code ကိုထည့်ပါ။

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

    - **Save** ကိုရွေးချယ်ပါ။

    ![Select raw file mode.](../../../../../../translated_images/my/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. *integrate_with_promptflow.py* ဖိုင်တွင် အောက်ပါ code ကို ထည့်ပြီး Prompt flow တွင် custom Phi-3 မော်ဒယ်ကို အသုံးပြုပါ။

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # မှတ်တမ်းသွင်းခြင်း စီစဉ်မှု
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

        # "connection" သည် Custom Connection ၏နာမည်ဖြစ်ပြီး၊ "endpoint", "key" များသည် Custom Connection ထဲမှ key များဖြစ်သည်
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
            
            # JSON တုံ့ပြန်မှုအပြည့်အစုံကို မှတ်သားပါ။
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

    ![Paste prompt flow code.](../../../../../../translated_images/my/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry တွင် Prompt flow အသုံးပြု နည်းပိုမိုလေ့လာလိုပါက [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ကိုကြည့်ရှုနိုင်သည်။

1. သင်၏ မော်ဒယ်နှင့် စကားပြောရန် **Chat input**, **Chat output** ကိုရွေးချယ်ပါ။

    ![Input Output.](../../../../../../translated_images/my/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. ယခု သင့်စိတ်ကြိုက် Phi-3 မော်ဒယ်နှင့် စကားပြောရန် အသင့်ဖြစ်ပါပြီ။ နောက်လေ့ကျင့်ခန်းတွင် Prompt flow ကို စတင်ရန်နှင့် fine-tuned Phi-3 မော်ဒယ်နှင့် စကားပြောနည်းကို လေ့လာမည်ဖြစ်ပါသည်။

> [!NOTE]
>
> ပြန်လည်တည်ဆောက်ပြီးသော flow သည် အောက်ပါပုံစံအတိုင်း ဖြစ်ရမည်-
>
> ![Flow example.](../../../../../../translated_images/my/08-18-graph-example.d6457533952e690c.webp)
>

### သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောခြင်း

ယခုအချိန်တွင် သင့် custom Phi-3 မော်ဒယ်ကို fine-tune ပြီး Prompt flow နှင့် ပေါင်းစပ်သွားပြီ ဖြစ်သည်။ ယခု လုပ်ငန်းစဉ်က Prompt flow ကိုအသုံးပြု၍ မော်ဒယ်နှင့် စကားပြောခြင်း စတင်ရန် လမ်းညွှန်ပေးပါမည်။ အောက်ပါအဆင့်များကိုချက်ချင်းလိုက်နာပါက fine-tuned Phi-3 မော်ဒယ်၏ စွမ်းရည်များကို အပြည့်အဝ အသုံးချနိုင်ပါမည်။

- Prompt flow ကိုအသုံးပြု၍ သင့် custom Phi-3 မော်ဒယ်နှင့် စကားပြောပါ။

#### Prompt flow ကို စတင်ရန်

1. Prompt flow ကို စတင်ရန် **Start compute sessions** ကိုနှိပ်ပါ။

    ![Start compute session.](../../../../../../translated_images/my/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. အချက်အလက်များကို အသစ်အဆန်းလုပ်ရန် **Validate and parse input** ကိုနှိပ်ပါ။

    ![Validate input.](../../../../../../translated_images/my/09-02-validate-input.317c76ef766361e9.webp)

1. သင့်ဖန်တီးထားသော custom connection ၏ **connection** တန်ဖိုးကိုရွေးချယ်ပါ။ ဥပမာ*, connection*။

    ![Connection.](../../../../../../translated_images/my/09-03-select-connection.99bdddb4b1844023.webp)

#### သင့် custom မော်ဒယ်နှင့် စကားပြောခြင်း

1. **Chat** ကိုရွေးချယ်ပါ။

    ![Select chat.](../../../../../../translated_images/my/09-04-select-chat.61936dce6612a1e6.webp)

1. ရလဒ်ဥပမာဖြစ်ပါသည်- ယခု သင်သည် သင်၏ custom Phi-3 မော်ဒယ်နှင့် စကားပြောနိုင်ပါပြီ။ fine-tuning အတွက်သုံးထားသော data အခြေပြု၍ မေးခွန်းများမေးရန် အကြံဉာဏ်ပေးသည်။

    ![Chat with prompt flow.](../../../../../../translated_images/my/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:  
ဤစာတမ်းကို AI ဘာသာပြန်ခြင်းဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည်တိကျမှန်ကန်မှုအတွက် ကြိုးစားသောကြောင့်၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားအယွင်းများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အရင်းအမြစ်အဖြစ် ချမှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် မည်သည့်အရာမဆို လူ့ပရော်ဖက်ရှင်နယ် ဘာသာပြန်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းနားလည်မှုများအတွက် ကျွန်ုပ်တို့ တာဝန် မှားမခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->