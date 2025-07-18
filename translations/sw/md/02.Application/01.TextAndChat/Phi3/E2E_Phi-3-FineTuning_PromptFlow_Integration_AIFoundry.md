<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:50:18+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "sw"
}
-->
# Fine-tune na Unganisha modeli za Phi-3 za Kipekee na Prompt flow katika Azure AI Foundry

Mfano huu wa mwisho-mwisho (E2E) unategemea mwongozo wa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" kutoka Microsoft Tech Community. Unatoa maelezo ya mchakato wa kufinyaza, kupeleka, na kuunganisha modeli za Phi-3 za kipekee na Prompt flow katika Azure AI Foundry. Tofauti na mfano wa E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ambao ulihusisha kuendesha msimbo kwa ndani, mafunzo haya yanazingatia kabisa kufinyaza na kuunganisha modeli yako ndani ya Azure AI / ML Studio.

## Muhtasari

Katika mfano huu wa E2E, utajifunza jinsi ya kufinyaza modeli ya Phi-3 na kuunganisha na Prompt flow katika Azure AI Foundry. Kwa kutumia Azure AI / ML Studio, utaanzisha mtiririko wa kazi wa kupeleka na kutumia modeli za AI za kipekee. Mfano huu wa E2E umegawanywa katika matukio matatu:

**Mtukio 1: Weka rasilimali za Azure na Jiandae kwa kufinyaza**

**Mtukio 2: Finyaza modeli ya Phi-3 na Peleka katika Azure Machine Learning Studio**

**Mtukio 3: Unganisha na Prompt flow na Zungumza na modeli yako ya kipekee katika Azure AI Foundry**

Hapa kuna muhtasari wa mfano huu wa E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.sw.png)

### Jedwali la Yaliyomo

1. **[Mtukio 1: Weka rasilimali za Azure na Jiandae kwa kufinyaza](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Tengeneza Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Omba viwango vya GPU katika Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ongeza ugawaji wa jukumu](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Weka mradi](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Jiandae na seti ya data kwa kufinyaza](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Mtukio 2: Finyaza modeli ya Phi-3 na Peleka katika Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Finyaza modeli ya Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Peleka modeli ya Phi-3 iliyofinyazwa](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Mtukio 3: Unganisha na Prompt flow na Zungumza na modeli yako ya kipekee katika Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Unganisha modeli ya Phi-3 ya kipekee na Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Zungumza na modeli yako ya Phi-3 ya kipekee](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Mtukio 1: Weka rasilimali za Azure na Jiandae kwa kufinyaza

### Tengeneza Azure Machine Learning Workspace

1. Andika *azure machine learning* katika **kisanduku cha utafutaji** juu ya ukurasa wa portal na chagua **Azure Machine Learning** kutoka kwa chaguzi zinazojitokeza.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.sw.png)

2. Chagua **+ Create** kutoka kwenye menyu ya urambazaji.

3. Chagua **New workspace** kutoka kwenye menyu ya urambazaji.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.sw.png)

4. Fanya kazi zifuatazo:

    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakaotumia (tengeneza mpya ikiwa inahitajika).
    - Weka **Workspace Name**. Lazima iwe jina la kipekee.
    - Chagua **Region** unayotaka kutumia.
    - Chagua **Storage account** utakaotumia (tengeneza mpya ikiwa inahitajika).
    - Chagua **Key vault** utakaotumia (tengeneza mpya ikiwa inahitajika).
    - Chagua **Application insights** utakaotumia (tengeneza mpya ikiwa inahitajika).
    - Chagua **Container registry** utakaotumia (tengeneza mpya ikiwa inahitajika).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.sw.png)

5. Chagua **Review + Create**.

6. Chagua **Create**.

### Omba viwango vya GPU katika Azure Subscription

Katika mafunzo haya, utajifunza jinsi ya kufinyaza na kupeleka modeli ya Phi-3, ukitumia GPUs. Kwa kufinyaza, utatumia GPU ya *Standard_NC24ads_A100_v4*, ambayo inahitaji ombi la kiwango. Kwa kupeleka, utatumia GPU ya *Standard_NC6s_v3*, ambayo pia inahitaji ombi la kiwango.

> [!NOTE]
>
> Subscription za Pay-As-You-Go pekee (aina ya kawaida ya subscription) ndizo zinazostahili kugawiwa GPU; subscription za faida hazijaungwa mkono kwa sasa.
>

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Fanya kazi zifuatazo kuomba kiwango cha *Standard NCADSA100v4 Family*:

    - Chagua **Quota** kutoka kwenye tabia ya upande wa kushoto.
    - Chagua **Virtual machine family** utakaotumia. Kwa mfano, chagua **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ambayo inajumuisha GPU ya *Standard_NC24ads_A100_v4*.
    - Chagua **Request quota** kutoka kwenye menyu ya urambazaji.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.sw.png)

    - Ndani ya ukurasa wa Request quota, weka **New cores limit** unayotaka kutumia. Kwa mfano, 24.
    - Ndani ya ukurasa wa Request quota, chagua **Submit** kuomba kiwango cha GPU.

1. Fanya kazi zifuatazo kuomba kiwango cha *Standard NCSv3 Family*:

    - Chagua **Quota** kutoka kwenye tabia ya upande wa kushoto.
    - Chagua **Virtual machine family** utakaotumia. Kwa mfano, chagua **Standard NCSv3 Family Cluster Dedicated vCPUs**, ambayo inajumuisha GPU ya *Standard_NC6s_v3*.
    - Chagua **Request quota** kutoka kwenye menyu ya urambazaji.
    - Ndani ya ukurasa wa Request quota, weka **New cores limit** unayotaka kutumia. Kwa mfano, 24.
    - Ndani ya ukurasa wa Request quota, chagua **Submit** kuomba kiwango cha GPU.

### Ongeza ugawaji wa jukumu

Ili kufinyaza na kupeleka modeli zako, lazima kwanza utengeneze User Assigned Managed Identity (UAI) na uipe ruhusa zinazofaa. UAI hii itatumika kwa uthibitishaji wakati wa kupeleka.

#### Tengeneza User Assigned Managed Identity (UAI)

1. Andika *managed identities* katika **kisanduku cha utafutaji** juu ya ukurasa wa portal na chagua **Managed Identities** kutoka kwa chaguzi zinazojitokeza.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.sw.png)

1. Chagua **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.sw.png)

1. Fanya kazi zifuatazo:

    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakaotumia (tengeneza mpya ikiwa inahitajika).
    - Chagua **Region** unayotaka kutumia.
    - Weka **Name**. Lazima iwe jina la kipekee.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.sw.png)

1. Chagua **Review + create**.

1. Chagua **+ Create**.

#### Ongeza ugawaji wa jukumu la Contributor kwa Managed Identity

1. Nenda kwenye rasilimali ya Managed Identity uliyotengeneza.

1. Chagua **Azure role assignments** kutoka kwenye tabia ya upande wa kushoto.

1. Chagua **+Add role assignment** kutoka kwenye menyu ya urambazaji.

1. Ndani ya ukurasa wa Add role assignment, fanya kazi zifuatazo:
    - Chagua **Scope** kuwa **Resource group**.
    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakaotumia.
    - Chagua **Role** kuwa **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.sw.png)

2. Chagua **Save**.

#### Ongeza ugawaji wa jukumu la Storage Blob Data Reader kwa Managed Identity

1. Andika *storage accounts* katika **kisanduku cha utafutaji** juu ya ukurasa wa portal na chagua **Storage accounts** kutoka kwa chaguzi zinazojitokeza.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.sw.png)

1. Chagua akaunti ya kuhifadhi inayohusiana na Azure Machine Learning workspace uliyotengeneza. Kwa mfano, *finetunephistorage*.

1. Fanya kazi zifuatazo kuingia kwenye ukurasa wa Add role assignment:

    - Nenda kwenye akaunti ya Azure Storage uliyotengeneza.
    - Chagua **Access Control (IAM)** kutoka kwenye tabia ya upande wa kushoto.
    - Chagua **+ Add** kutoka kwenye menyu ya urambazaji.
    - Chagua **Add role assignment** kutoka kwenye menyu ya urambazaji.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.sw.png)

1. Ndani ya ukurasa wa Add role assignment, fanya kazi zifuatazo:

    - Ndani ya ukurasa wa Role, andika *Storage Blob Data Reader* katika **kisanduku cha utafutaji** na chagua **Storage Blob Data Reader** kutoka kwa chaguzi zinazojitokeza.
    - Ndani ya ukurasa wa Role, chagua **Next**.
    - Ndani ya ukurasa wa Members, chagua **Assign access to** **Managed identity**.
    - Ndani ya ukurasa wa Members, chagua **+ Select members**.
    - Ndani ya ukurasa wa Select managed identities, chagua **Subscription** yako ya Azure.
    - Ndani ya ukurasa wa Select managed identities, chagua **Managed identity** kuwa **Manage Identity**.
    - Ndani ya ukurasa wa Select managed identities, chagua Manage Identity uliyotengeneza. Kwa mfano, *finetunephi-managedidentity*.
    - Ndani ya ukurasa wa Select managed identities, chagua **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.sw.png)

1. Chagua **Review + assign**.

#### Ongeza ugawaji wa jukumu la AcrPull kwa Managed Identity

1. Andika *container registries* katika **kisanduku cha utafutaji** juu ya ukurasa wa portal na chagua **Container registries** kutoka kwa chaguzi zinazojitokeza.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.sw.png)

1. Chagua rejista ya kontena inayohusiana na Azure Machine Learning workspace. Kwa mfano, *finetunephicontainerregistry*

1. Fanya kazi zifuatazo kuingia kwenye ukurasa wa Add role assignment:

    - Chagua **Access Control (IAM)** kutoka kwenye tabia ya upande wa kushoto.
    - Chagua **+ Add** kutoka kwenye menyu ya urambazaji.
    - Chagua **Add role assignment** kutoka kwenye menyu ya urambazaji.

1. Ndani ya ukurasa wa Add role assignment, fanya kazi zifuatazo:

    - Ndani ya ukurasa wa Role, andika *AcrPull* katika **kisanduku cha utafutaji** na chagua **AcrPull** kutoka kwa chaguzi zinazojitokeza.
    - Ndani ya ukurasa wa Role, chagua **Next**.
    - Ndani ya ukurasa wa Members, chagua **Assign access to** **Managed identity**.
    - Ndani ya ukurasa wa Members, chagua **+ Select members**.
    - Ndani ya ukurasa wa Select managed identities, chagua **Subscription** yako ya Azure.
    - Ndani ya ukurasa wa Select managed identities, chagua **Managed identity** kuwa **Manage Identity**.
    - Ndani ya ukurasa wa Select managed identities, chagua Manage Identity uliyotengeneza. Kwa mfano, *finetunephi-managedidentity*.
    - Ndani ya ukurasa wa Select managed identities, chagua **Select**.
    - Chagua **Review + assign**.

### Weka mradi

Ili kupakua seti za data zinazohitajika kwa kufinyaza, utaweka mazingira ya ndani.

Katika zoezi hili, utafanya

- Tengeneza folda ya kufanya kazi ndani yake.
- Tengeneza mazingira ya virtual.
- Sakinisha vifurushi vinavyohitajika.
- Tengeneza faili la *download_dataset.py* kupakua seti ya data.

#### Tengeneza folda ya kufanya kazi ndani yake

1. Fungua dirisha la terminal na andika amri ifuatayo kutengeneza folda iitwayo *finetune-phi* katika njia ya chaguo-msingi.

    ```console
    mkdir finetune-phi
    ```

2. Andika amri ifuatayo ndani ya terminal yako kuingia kwenye folda ya *finetune-phi* uliyotengeneza.
#### Unda mazingira ya mtandao wa virtual

1. Andika amri ifuatayo ndani ya terminal yako kuunda mazingira ya virtual yenye jina *.venv*.

2. Andika amri ifuatayo ndani ya terminal yako kuwasha mazingira ya virtual.

> [!NOTE]
> Ikiwa imefanikiwa, unapaswa kuona *(.venv)* kabla ya alama ya amri.

#### Sakinisha vifurushi vinavyohitajika

1. Andika amri ifuatayo ndani ya terminal yako kusakinisha vifurushi vinavyohitajika.

#### Unda `download_dataset.py`

> [!NOTE]
> Muundo kamili wa folda:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Fungua **Visual Studio Code**.

1. Chagua **File** kutoka kwenye menyu ya juu.

1. Chagua **Open Folder**.

1. Chagua folda ya *finetune-phi* uliyounda, ambayo iko katika *C:\Users\yourUserName\finetune-phi*.

    ![Chagua folda uliyounda.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.sw.png)

1. Katika sehemu ya kushoto ya Visual Studio Code, bonyeza kulia na chagua **New File** kuunda faili mpya yenye jina *download_dataset.py*.

    ![Unda faili mpya.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.sw.png)

### Andaa dataset kwa ajili ya fine-tuning

Katika zoezi hili, utaendesha faili la *download_dataset.py* kupakua datasets za *ultrachat_200k* kwenye mazingira yako ya ndani. Kisha utatumia datasets hizi kufanyia fine-tune modeli ya Phi-3 katika Azure Machine Learning.

Katika zoezi hili, utafanya:

- Ongeza msimbo kwenye faili la *download_dataset.py* kupakua datasets.
- Endesha faili la *download_dataset.py* kupakua datasets kwenye mazingira yako ya ndani.

#### Pakua dataset yako kwa kutumia *download_dataset.py*

1. Fungua faili la *download_dataset.py* katika Visual Studio Code.

1. Ongeza msimbo ifuatayo ndani ya faili la *download_dataset.py*.

1. Andika amri ifuatayo ndani ya terminal yako kuendesha script na kupakua dataset kwenye mazingira yako ya ndani.

1. Hakiki kwamba datasets zilihifadhiwa kwa mafanikio kwenye saraka yako ya *finetune-phi/data*.

> [!NOTE]
>
> #### Kumbuka kuhusu ukubwa wa dataset na muda wa fine-tuning
>
> Katika mafunzo haya, unatumia asilimia 1 tu ya dataset (`split='train[:1%]'`). Hii inapunguza kiasi cha data kwa kiasi kikubwa, na kuharakisha mchakato wa kupakia na fine-tuning. Unaweza kubadilisha asilimia hii kupata usawa mzuri kati ya muda wa mafunzo na utendaji wa modeli. Kutumia sehemu ndogo ya dataset hupunguza muda unaohitajika kwa fine-tuning, na kufanya mchakato kuwa rahisi kwa mafunzo.

## Hali ya 2: Fanya fine-tune modeli ya Phi-3 na Tumia Azure Machine Learning Studio

### Fanya fine-tune modeli ya Phi-3

Katika zoezi hili, utafanya fine-tune modeli ya Phi-3 katika Azure Machine Learning Studio.

Katika zoezi hili, utafanya:

- Unda kundi la kompyuta kwa ajili ya fine-tuning.
- Fanya fine-tune modeli ya Phi-3 katika Azure Machine Learning Studio.

#### Unda kundi la kompyuta kwa ajili ya fine-tuning

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chagua **Compute** kutoka kwenye tab ya upande wa kushoto.

1. Chagua **Compute clusters** kutoka kwenye menyu ya urambazaji.

1. Chagua **+ New**.

    ![Chagua compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.sw.png)

1. Fanya yafuatayo:

    - Chagua **Region** unayotaka kutumia.
    - Chagua **Virtual machine tier** kuwa **Dedicated**.
    - Chagua **Virtual machine type** kuwa **GPU**.
    - Chagua kichujio cha **Virtual machine size** kuwa **Select from all options**.
    - Chagua **Virtual machine size** kuwa **Standard_NC24ads_A100_v4**.

    ![Unda kundi.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.sw.png)

1. Chagua **Next**.

1. Fanya yafuatayo:

    - Weka **Compute name**. Lazima iwe jina la kipekee.
    - Chagua **Minimum number of nodes** kuwa **0**.
    - Chagua **Maximum number of nodes** kuwa **1**.
    - Chagua **Idle seconds before scale down** kuwa **120**.

    ![Unda kundi.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.sw.png)

1. Chagua **Create**.

#### Fanya fine-tune modeli ya Phi-3

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chagua Azure Machine Learning workspace uliyounda.

    ![Chagua workspace uliyounda.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.sw.png)

1. Fanya yafuatayo:

    - Chagua **Model catalog** kutoka kwenye tab ya upande wa kushoto.
    - Andika *phi-3-mini-4k* kwenye **search bar** na chagua **Phi-3-mini-4k-instruct** kutoka kwenye chaguzi zinazojitokeza.

    ![Andika phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.sw.png)

1. Chagua **Fine-tune** kutoka kwenye menyu ya urambazaji.

    ![Chagua fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.sw.png)

1. Fanya yafuatayo:

    - Chagua **Select task type** kuwa **Chat completion**.
    - Chagua **+ Select data** kupakia **Traning data**.
    - Chagua aina ya kupakia Validation data kuwa **Provide different validation data**.
    - Chagua **+ Select data** kupakia **Validation data**.

    ![Jaza ukurasa wa fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.sw.png)

    > [!TIP]
    >
    > Unaweza kuchagua **Advanced settings** kubadilisha mipangilio kama **learning_rate** na **lr_scheduler_type** ili kuboresha mchakato wa fine-tuning kulingana na mahitaji yako maalum.

1. Chagua **Finish**.

1. Katika zoezi hili, umefanikiwa kufanya fine-tune modeli ya Phi-3 kwa kutumia Azure Machine Learning. Tafadhali fahamu kuwa mchakato wa fine-tuning unaweza kuchukua muda mrefu. Baada ya kuendesha kazi ya fine-tuning, unahitaji kusubiri mpaka itakapokamilika. Unaweza kufuatilia hali ya kazi ya fine-tuning kwa kwenda kwenye tab ya Jobs upande wa kushoto wa Azure Machine Learning Workspace yako. Katika mfululizo unaofuata, utatuma modeli iliyofinyangwa na kuunganisha na Prompt flow.

    ![Tazama kazi ya fine-tuning.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.sw.png)

### Tuma modeli iliyofinyangwa ya Phi-3

Ili kuunganisha modeli iliyofinyangwa ya Phi-3 na Prompt flow, unahitaji kuituma modeli hiyo ili iweze kupatikana kwa ajili ya utambuzi wa wakati halisi. Mchakato huu unahusisha kusajili modeli, kuunda endpoint mtandaoni, na kuituma modeli.

Katika zoezi hili, utafanya:

- Sajili modeli iliyofinyangwa katika Azure Machine Learning workspace.
- Unda endpoint mtandaoni.
- Tuma modeli iliyosajiliwa ya Phi-3 iliyofinyangwa.

#### Sajili modeli iliyofinyangwa

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chagua Azure Machine Learning workspace uliyounda.

    ![Chagua workspace uliyounda.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.sw.png)

1. Chagua **Models** kutoka kwenye tab ya upande wa kushoto.
1. Chagua **+ Register**.
1. Chagua **From a job output**.

    ![Sajili modeli.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.sw.png)

1. Chagua kazi uliyounda.

    ![Chagua kazi.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.sw.png)

1. Chagua **Next**.

1. Chagua **Model type** kuwa **MLflow**.

1. Hakikisha **Job output** imechaguliwa; inapaswa kuchaguliwa moja kwa moja.

    ![Chagua output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.sw.png)

2. Chagua **Next**.

3. Chagua **Register**.

    ![Chagua register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.sw.png)

4. Unaweza kuona modeli uliyosajili kwa kwenda kwenye menyu ya **Models** kutoka kwenye tab ya upande wa kushoto.

    ![Modeli iliyosajiliwa.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.sw.png)

#### Tuma modeli iliyofinyangwa

1. Nenda kwenye Azure Machine Learning workspace uliyounda.

1. Chagua **Endpoints** kutoka kwenye tab ya upande wa kushoto.

1. Chagua **Real-time endpoints** kutoka kwenye menyu ya urambazaji.

    ![Unda endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.sw.png)

1. Chagua **Create**.

1. Chagua modeli uliyosajili uliyounda.

    ![Chagua modeli iliyosajiliwa.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.sw.png)

1. Chagua **Select**.

1. Fanya yafuatayo:

    - Chagua **Virtual machine** kuwa *Standard_NC6s_v3*.
    - Chagua **Instance count** unayotaka kutumia. Kwa mfano, *1*.
    - Chagua **Endpoint** kuwa **New** kuunda endpoint mpya.
    - Weka **Endpoint name**. Lazima iwe jina la kipekee.
    - Weka **Deployment name**. Lazima iwe jina la kipekee.

    ![Jaza mipangilio ya deployment.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.sw.png)

1. Chagua **Deploy**.

> [!WARNING]
> Ili kuepuka malipo ya ziada kwenye akaunti yako, hakikisha unafuta endpoint uliyounda katika Azure Machine Learning workspace.
>

#### Angalia hali ya deployment katika Azure Machine Learning Workspace

1. Nenda kwenye Azure Machine Learning workspace uliyounda.

1. Chagua **Endpoints** kutoka kwenye tab ya upande wa kushoto.

1. Chagua endpoint uliyounda.

    ![Chagua endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.sw.png)

1. Kwenye ukurasa huu, unaweza kusimamia endpoints wakati wa mchakato wa deployment.

> [!NOTE]
> Mara deployment itakapokamilika, hakikisha **Live traffic** imewekwa kwa **100%**. Ikiwa haijawa hivyo, chagua **Update traffic** kurekebisha mipangilio ya trafiki. Kumbuka huwezi kujaribu modeli ikiwa trafiki imewekwa kwa 0%.
>
> ![Weka trafiki.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.sw.png)
>

## Hali ya 3: Unganisha na Prompt flow na Zungumza na modeli yako maalum katika Azure AI Foundry

### Unganisha modeli maalum ya Phi-3 na Prompt flow

Baada ya kufanikisha kutuma modeli yako iliyofinyangwa, sasa unaweza kuunganisha na Prompt Flow ili kutumia modeli yako katika programu za wakati halisi, kuruhusu aina mbalimbali za kazi za mwingiliano na modeli yako maalum ya Phi-3.

Katika zoezi hili, utafanya:

- Unda Azure AI Foundry Hub.
- Unda Mradi wa Azure AI Foundry.
- Unda Prompt flow.
- Ongeza muunganisho maalum kwa modeli iliyofinyangwa ya Phi-3.
- Sanidi Prompt flow kuzungumza na modeli yako maalum ya Phi-3.
> [!NOTE]
> Unaweza pia kuunganishwa na Promptflow kwa kutumia Azure ML Studio. Mchakato ule ule wa kuunganishwa unaweza kutumika kwa Azure ML Studio.
#### Unda Azure AI Foundry Hub

Unahitaji kuunda Hub kabla ya kuunda Mradi. Hub hufanya kazi kama Resource Group, ikikuruhusu kupanga na kusimamia Miradi mingi ndani ya Azure AI Foundry.

1. Tembelea [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Chagua **All hubs** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New hub** kutoka kwenye menyu ya urambazaji.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.sw.png)

1. Fanya kazi zifuatazo:

    - Ingiza **Hub name**. Lazima iwe thamani ya kipekee.
    - Chagua Azure yako **Subscription**.
    - Chagua **Resource group** utakayotumia (unda mpya ikiwa inahitajika).
    - Chagua **Location** unayotaka kutumia.
    - Chagua **Connect Azure AI Services** utakayotumia (unda mpya ikiwa inahitajika).
    - Chagua **Connect Azure AI Search** kwa **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.sw.png)

1. Chagua **Next**.

#### Unda Azure AI Foundry Project

1. Katika Hub uliyounda, chagua **All projects** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New project** kutoka kwenye menyu ya urambazaji.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.sw.png)

1. Ingiza **Project name**. Lazima iwe thamani ya kipekee.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.sw.png)

1. Chagua **Create a project**.

#### Ongeza muunganisho maalum kwa mfano wa Phi-3 ulioboreshwa

Ili kuunganisha mfano wako maalum wa Phi-3 na Prompt flow, unahitaji kuhifadhi endpoint na ufunguo wa mfano katika muunganisho maalum. Mpangilio huu unahakikisha upatikanaji wa mfano wako maalum wa Phi-3 katika Prompt flow.

#### Weka api key na endpoint uri ya mfano wa Phi-3 ulioboreshwa

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Nenda kwenye Azure Machine learning workspace uliyounda.

1. Chagua **Endpoints** kutoka kwenye kichupo cha upande wa kushoto.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.sw.png)

1. Chagua endpoint uliyounda.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.sw.png)

1. Chagua **Consume** kutoka kwenye menyu ya urambazaji.

1. Nakili **REST endpoint** na **Primary key** zako.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.sw.png)

#### Ongeza Muunganisho Maalum

1. Tembelea [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Nenda kwenye mradi wa Azure AI Foundry uliyounda.

1. Katika Mradi uliyounda, chagua **Settings** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.sw.png)

1. Chagua **Custom keys** kutoka kwenye menyu ya urambazaji.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.sw.png)

1. Fanya kazi zifuatazo:

    - Chagua **+ Add key value pairs**.
    - Kwa jina la ufunguo, ingiza **endpoint** na bandika endpoint uliyokopa kutoka Azure ML Studio kwenye sehemu ya thamani.
    - Chagua tena **+ Add key value pairs**.
    - Kwa jina la ufunguo, ingiza **key** na bandika ufunguo uliyokopa kutoka Azure ML Studio kwenye sehemu ya thamani.
    - Baada ya kuongeza funguo, chagua **is secret** ili kuzuia ufunguo kuonyeshwa.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.sw.png)

1. Chagua **Add connection**.

#### Unda Prompt flow

Umeongeza muunganisho maalum katika Azure AI Foundry. Sasa, hebu tuunde Prompt flow kwa kutumia hatua zifuatazo. Kisha, utaunganisha Prompt flow hii na muunganisho maalum ili uweze kutumia mfano ulioboreshwa ndani ya Prompt flow.

1. Nenda kwenye mradi wa Azure AI Foundry uliyounda.

1. Chagua **Prompt flow** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ Create** kutoka kwenye menyu ya urambazaji.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.sw.png)

1. Chagua **Chat flow** kutoka kwenye menyu ya urambazaji.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.sw.png)

1. Ingiza **Folder name** utakayotumia.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.sw.png)

2. Chagua **Create**.

#### Sanidi Prompt flow kuzungumza na mfano wako maalum wa Phi-3

Unahitaji kuingiza mfano ulioboreshwa wa Phi-3 ndani ya Prompt flow. Hata hivyo, Prompt flow iliyopo haijaundwa kwa madhumuni haya. Kwa hivyo, lazima ubadilishe Prompt flow ili kuwezesha kuingiza mfano maalum.

1. Katika Prompt flow, fanya kazi zifuatazo ili kujenga upya mtiririko uliopo:

    - Chagua **Raw file mode**.
    - Futa msimbo wote uliopo katika faili *flow.dag.yml*.
    - Ongeza msimbo ufuatao kwenye faili *flow.dag.yml*.

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

    - Chagua **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.sw.png)

1. Ongeza msimbo ufuatao kwenye faili *integrate_with_promptflow.py* ili kutumia mfano maalum wa Phi-3 katika Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.sw.png)

> [!NOTE]
> Kwa maelezo zaidi kuhusu kutumia Prompt flow katika Azure AI Foundry, unaweza rejelea [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chagua **Chat input**, **Chat output** kuwezesha mazungumzo na mfano wako.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.sw.png)

1. Sasa uko tayari kuzungumza na mfano wako maalum wa Phi-3. Katika zoezi lijalo, utajifunza jinsi ya kuanzisha Prompt flow na kuitumia kuzungumza na mfano wako ulioboreshwa wa Phi-3.

> [!NOTE]
>
> Mtiririko ulioumbwa upya unapaswa kuonekana kama picha iliyo hapa chini:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.sw.png)
>

### Zungumza na mfano wako maalum wa Phi-3

Sasa baada ya kuboresha na kuunganisha mfano wako maalum wa Phi-3 na Prompt flow, uko tayari kuanza kuwasiliana nao. Zoezi hili litakuongoza katika mchakato wa kuanzisha na kuanzisha mazungumzo na mfano wako kwa kutumia Prompt flow. Kwa kufuata hatua hizi, utaweza kutumia kikamilifu uwezo wa mfano wako ulioboreshwa wa Phi-3 kwa kazi mbalimbali na mazungumzo.

- Zungumza na mfano wako maalum wa Phi-3 kwa kutumia Prompt flow.

#### Anza Prompt flow

1. Chagua **Start compute sessions** kuanzisha Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.sw.png)

1. Chagua **Validate and parse input** ili kusasisha vigezo.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.sw.png)

1. Chagua **Value** ya **connection** kwa muunganisho maalum uliouunda. Kwa mfano, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.sw.png)

#### Zungumza na mfano wako maalum

1. Chagua **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.sw.png)

1. Hapa kuna mfano wa matokeo: Sasa unaweza kuzungumza na mfano wako maalum wa Phi-3. Inashauriwa kuuliza maswali yanayohusiana na data iliyotumika kuboresha mfano.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.sw.png)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.