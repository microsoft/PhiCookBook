# Rekebisha na Unganisha modeli maalum za Phi-3 na Prompt flow katika Microsoft Foundry

Mfano huu wa mwisho hadi mwisho (E2E) unategemea mwongozo "[Rekebisha na Unganisha modeli maalum za Phi-3 na Prompt Flow katika Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" kutoka Microsoft Tech Community. Unaleta michakato ya kurekebisha, kusambaza, na kuunganisha modeli maalum za Phi-3 na Prompt flow katika Microsoft Foundry. Tofauti na mfano wa E2E, "[Rekebisha na Unganisha modeli maalum za Phi-3 na Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ambayo ilihusisha kuendesha msimbo mahali hapa, mafunzo haya yanalenga kabisa kurekebisha na kuunganisha modeli yako ndani ya Azure AI / ML Studio.

## Muhtasari

Katika mfano huu wa E2E, utajifunza jinsi ya kurekebisha modeli ya Phi-3 na kuintegrate na Prompt flow katika Microsoft Foundry. Kwa kutumia Azure AI / ML Studio, utaanzisha mtiririko wa kazi wa kusambaza na kutumia modeli za AI maalum. Mfano huu wa E2E umegawanyika katika matukio matatu:

**Mtukio 1: Weka rasilimali za Azure na Jiandae kwa urejeshaji**

**Mtukio 2: Rekebisha modeli ya Phi-3 na Sambaza katika Azure Machine Learning Studio**

**Mtukio 3: Unganisha na Prompt flow na Zungumza na modeli yako maalum katika Microsoft Foundry**

Hapa kuna muhtasari wa mfano huu wa E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/sw/00-01-architecture.198ba0f1ae6d841a.webp)

### Jedwali la Maudhui

1. **[Mtukio 1: Weka rasilimali za Azure na Jiandae kwa urejeshaji](#mtukio-1-weka-rasilimali-za-azure-na-jiandae-kwa-urejeshaji)**
    - [Unda Eneo la Kazi la Azure Machine Learning](#unda-eneo-la-kazi-la-azure-machine-learning)
    - [Omba sehemu za GPU katika Usajili wa Azure](#omba-sehemu-za-gpu-katika-usajili-wa-azure)
    - [Ongeza mgawo wa jukumu](#ongeza-mgawo-wa-jukumu)
    - [Weka mradi](#weka-mradi)
    - [Jiandae dataset kwa urejeshaji](#andaa-dataset-kwa-ajili-ya-fine-tuning)

1. **[Mtukio 2: Rekebisha modeli ya Phi-3 na Sambaza katika Azure Machine Learning Studio](#hali-ya-2-rekebisha-modeli-ya-phi-3-na-tumia-azure-machine-learning-studio)**
    - [Rekebisha modeli ya Phi-3](#rekebisha-modeli-ya-phi-3)
    - [Sambaza modeli ya Phi-3 iliyorekebishwa](#tuma-modeli-iliyorekebishwa-ya-phi-3)

1. **[Mtukio 3: Unganisha na Prompt flow na Zungumza na modeli yako maalum katika Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Unganisha modeli maalum ya Phi-3 na Prompt flow](#unganisha-modeli-maalum-ya-phi-3-na-prompt-flow)
    - [Zungumza na modeli yako maalum ya Phi-3](#zungumza-na-mfano-wako-wa-kawaida-wa-phi-3)

## Mtukio 1: Weka rasilimali za Azure na Jiandae kwa urejeshaji

### Unda Eneo la Kazi la Azure Machine Learning

1. Andika *azure machine learning* katika **kisanduku cha utafutaji** juu ya ukurasa wa lango na chagua **Azure Machine Learning** kutoka kwa chaguzi zinazojitokeza.

    ![Type azure machine learning.](../../../../../../translated_images/sw/01-01-type-azml.acae6c5455e67b4b.webp)

2. Chagua **+ Create** kutoka kwenye menyu ya urambazaji.

3. Chagua **New workspace** kutoka kwenye menyu ya urambazaji.

    ![Select new workspace.](../../../../../../translated_images/sw/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Fanya kazi zifuatazo:

    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakaotumia (unda mpya ikiwa inahitajika).
    - Ingiza **Workspace Name**. Lazima iwe thamani ya kipekee.
    - Chagua **Region** unayotaka kutumia.
    - Chagua **Storage account** kutumia (unda mpya ikiwa inahitajika).
    - Chagua **Key vault** kutumia (unda mpya ikiwa inahitajika).
    - Chagua **Application insights** kutumia (unda mpya ikiwa inahitajika).
    - Chagua **Container registry** kutumia (unda mpya ikiwa inahitajika).

    ![Fill azure machine learning.](../../../../../../translated_images/sw/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Chagua **Review + Create**.

6. Chagua **Create**.

### Omba sehemu za GPU katika Usajili wa Azure

Katika mafunzo haya, utajifunza jinsi ya kurekebisha na kusambaza modeli ya Phi-3, ukitumia GPUs. Kwa urejeshaji, utatumia *Standard_NC24ads_A100_v4* GPU, ambayo inahitaji ombi la sehemu. Kwa usambazaji, utatumia *Standard_NC6s_v3* GPU, ambayo pia inahitaji ombi la sehemu.

> [!NOTE]
>
> Usajili wa Pay-As-You-Go pekee (aina ya kawaida ya usajili) unastahili kugawiwa GPU; usajili wa faida hauungi mkono kwa sasa.
>

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Fanya kazi zifuatazo kuomba *Standard NCADSA100v4 Family* sehemu:

    - Chagua **Quota** kutoka kwenye kipengele cha upande wa kushoto.
    - Chagua **Virtual machine family** unayotaka kutumia. Kwa mfano, chagua **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ambayo inajumuisha GPU *Standard_NC24ads_A100_v4*.
    - Chagua **Request quota** kutoka kwenye menyu ya urambazaji.

        ![Request quota.](../../../../../../translated_images/sw/02-02-request-quota.c0428239a63ffdd5.webp)

    - Ndani ya ukurasa wa Ombi la sehemu, ingiza **New cores limit** unayotaka kutumia. Kwa mfano, 24.
    - Ndani ya ukurasa wa Ombi la sehemu, chagua **Submit** kuomba sehemu ya GPU.

1. Fanya kazi zifuatazo kuomba *Standard NCSv3 Family* sehemu:

    - Chagua **Quota** kutoka kwenye kipengele cha upande wa kushoto.
    - Chagua **Virtual machine family** unayotaka kutumia. Kwa mfano, chagua **Standard NCSv3 Family Cluster Dedicated vCPUs**, ambayo inajumuisha GPU *Standard_NC6s_v3*.
    - Chagua **Request quota** kutoka kwenye menyu ya urambazaji.
    - Ndani ya ukurasa wa Ombi la sehemu, ingiza **New cores limit** unayotaka kutumia. Kwa mfano, 24.
    - Ndani ya ukurasa wa Ombi la sehemu, chagua **Submit** kuomba sehemu ya GPU.

### Ongeza mgawo wa jukumu

Ili kurekebisha na kusambaza modeli zako, lazima kwanza uunde Utambulisho Usimamizi Uliopewa Mtumiaji (UAI) na upe ruhusa zinazofaa. UAI huu utatumika kwa ajili ya uthibitishaji wakati wa usambazaji.

#### Unda Utambulisho Usimamizi Uliopewa Mtumiaji (UAI)

1. Andika *managed identities* katika **kisanduku cha utafutaji** juu ya ukurasa wa lango na chagua **Managed Identities** kutoka kwa chaguzi zinazojitokeza.

    ![Type managed identities.](../../../../../../translated_images/sw/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Chagua **+ Create**.

    ![Select create.](../../../../../../translated_images/sw/03-02-select-create.92bf8989a5cd98f2.webp)

1. Fanya kazi zifuatazo:

    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakaotumia (unda mpya ikiwa inahitajika).
    - Chagua **Region** unayotaka kutumia.
    - Ingiza **Name**. Lazima iwe thamani ya kipekee.

    ![Select create.](../../../../../../translated_images/sw/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Chagua **Review + create**.

1. Chagua **+ Create**.

#### Ongeza mgawo wa jukumu la Contributor kwa Utambulisho Usimamizi

1. Elekea kwenye rasilimali ya Utambulisho Usimamizi uliyounda.

1. Chagua **Azure role assignments** kutoka kwenye kipengele cha upande wa kushoto.

1. Chagua **+Add role assignment** kutoka kwenye menyu ya urambazaji.

1. Ndani ya ukurasa wa Ongeza mgawo wa jukumu, fanya kazi zifuatazo:
    - Chagua **Scope** kuwa **Resource group**.
    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakaotumia.
    - Chagua **Role** kuwa **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/sw/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Chagua **Save**.

#### Ongeza mgawo wa jukumu la Storage Blob Data Reader kwa Utambulisho Usimamizi

1. Andika *storage accounts* katika **kisanduku cha utafutaji** juu ya ukurasa wa lango na chagua **Storage accounts** kutoka kwa chaguzi zinazojitokeza.

    ![Type storage accounts.](../../../../../../translated_images/sw/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Chagua akaunti ya kuhifadhi inayohusiana na eneo la kazi la Azure Machine Learning uliyounda. Kwa mfano, *finetunephistorage*.

1. Fanya kazi zifuatazo kuuelekea ukurasa wa Ongeza mgawo wa jukumu:

    - Elekea kwenye akaunti ya Azure Storage uliyounda.
    - Chagua **Access Control (IAM)** kutoka kwenye kipengele cha upande wa kushoto.
    - Chagua **+ Add** kutoka kwenye menyu ya urambazaji.
    - Chagua **Add role assignment** kutoka kwenye menyu ya urambazaji.

    ![Add role.](../../../../../../translated_images/sw/03-06-add-role.353ccbfdcf0789c2.webp)

1. Ndani ya ukurasa wa Ongeza mgawo wa jukumu, fanya kazi zifuatazo:

    - Ndani ya ukurasa wa Jukumu, andika *Storage Blob Data Reader* katika **kisanduku cha utafutaji** na chagua **Storage Blob Data Reader** kutoka kwa chaguzi zinazojitokeza.
    - Ndani ya ukurasa wa Jukumu, chagua **Next**.
    - Ndani ya ukurasa wa Wajumbe, chagua **Assign access to** **Managed identity**.
    - Ndani ya ukurasa wa Wajumbe, chagua **+ Select members**.
    - Ndani ya ukurasa wa Chagua managed identities, chagua **Subscription** yako ya Azure.
    - Ndani ya ukurasa wa Chagua managed identities, chagua **Managed identity** ya **Manage Identity**.
    - Ndani ya ukurasa wa Chagua managed identities, chagua Manage Identity uliyounda. Kwa mfano, *finetunephi-managedidentity*.
    - Ndani ya ukurasa wa Chagua managed identities, chagua **Select**.

    ![Select managed identity.](../../../../../../translated_images/sw/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Chagua **Review + assign**.

#### Ongeza mgawo wa jukumu la AcrPull kwa Utambulisho Usimamizi

1. Andika *container registries* katika **kisanduku cha utafutaji** juu ya ukurasa wa lango na chagua **Container registries** kutoka kwa chaguzi zinazojitokeza.

    ![Type container registries.](../../../../../../translated_images/sw/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Chagua rejista ya kontena inayohusiana na eneo la kazi la Azure Machine Learning. Kwa mfano, *finetunephicontainerregistry*

1. Fanya kazi zifuatazo kuuelekea ukurasa wa Ongeza mgawo wa jukumu:

    - Chagua **Access Control (IAM)** kutoka kwenye kipengele cha upande wa kushoto.
    - Chagua **+ Add** kutoka kwenye menyu ya urambazaji.
    - Chagua **Add role assignment** kutoka kwenye menyu ya urambazaji.

1. Ndani ya ukurasa wa Ongeza mgawo wa jukumu, fanya kazi zifuatazo:

    - Ndani ya ukurasa wa Jukumu, andika *AcrPull* katika **kisanduku cha utafutaji** na chagua **AcrPull** kutoka kwa chaguzi zinazojitokeza.
    - Ndani ya ukurasa wa Jukumu, chagua **Next**.
    - Ndani ya ukurasa wa Wajumbe, chagua **Assign access to** **Managed identity**.
    - Ndani ya ukurasa wa Wajumbe, chagua **+ Select members**.
    - Ndani ya ukurasa wa Chagua managed identities, chagua **Subscription** yako ya Azure.
    - Ndani ya ukurasa wa Chagua managed identities, chagua **Managed identity** ya **Manage Identity**.
    - Ndani ya ukurasa wa Chagua managed identities, chagua Manage Identity uliyounda. Kwa mfano, *finetunephi-managedidentity*.
    - Ndani ya ukurasa wa Chagua managed identities, chagua **Select**.
    - Chagua **Review + assign**.

### Weka mradi

Ili kupakua dataset zinazohitajika kwa urejeshaji, utasakinisha mazingira ya ndani.

Katika mazoezi haya, utafanya

- Unda folda ya kufanya kazi ndani yake.
- Unda mazingira ya virtual.
- Sakinisha vifurushi vinavyohitajika.
- Unda faili *download_dataset.py* kupakua dataset.

#### Unda folda ya kufanya kazi ndani yake

1. Fungua dirisha la terminal na andika amri ifuatayo kuunda folda inayoitwa *finetune-phi* katika njia ya kawaida.

    ```console
    mkdir finetune-phi
    ```

2. Andika amri ifuatayo ndani ya terminal yako kuingia kwenye folda ya *finetune-phi* uliyounda.

    ```console
    cd finetune-phi
    ```

#### Unda mazingira ya virtual

1. Andika amri ifuatayo ndani ya terminal yako kuunda mazingira ya virtual yanayoitwa *.venv*.
    ```console
    python -m venv .venv
    ```

2. Andika amri ifuatayo ndani ya terminal yako ili kuamsha mazingira ya kweli.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ikiwa imetokea, unapaswa kuona *(.venv)* kabla ya dalili ya amri.

#### Sakinisha vifurushi vinavyohitajika

1. Andika amri zifuatazo ndani ya terminal yako ili kusakinisha vifurushi vinavyohitajika.

    ```console
    pip install datasets==2.19.1
    ```

#### Unda `donload_dataset.py`

> [!NOTE]
> Muundo kamili wa folda:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Fungua **Visual Studio Code**.

1. Chagua **File** kutoka kwenye upau wa menyu.

1. Chagua **Open Folder**.

1. Chagua folda *finetune-phi* uliyounda, iliyopo kwenye *C:\Users\yourUserName\finetune-phi*.

    ![Chagua folda uliyounda.](../../../../../../translated_images/sw/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Katika pane ya kushoto ya Visual Studio Code, bonyeza kulia kisha chagua **New File** kuunda faili mpya linaloitwa *download_dataset.py*.

    ![Unda faili mpya.](../../../../../../translated_images/sw/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Andaa dataset kwa ajili ya fine-tuning

Katika zoezi hili, utawala faili la *download_dataset.py* kupakua datasets za *ultrachat_200k* kwenye mazingira yako ya ndani. Kisha utatumia datasets hizi kurekebisha modeli ya Phi-3 katika Azure Machine Learning.

Katika zoezi hili, utafanya:

- Ongeza msimbo kwenye faili la *download_dataset.py* kupakua datasets.
- Endesha faili la *download_dataset.py* kupakua datasets kwenye mazingira yako ya ndani.

#### Pakua dataset yako kwa kutumia *download_dataset.py*

1. Fungua faili la *download_dataset.py* katika Visual Studio Code.

1. Ongeza msimbo ifuatayo ndani ya faili la *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Pakia seti ya data kwa jina lililotajwa, usanidi, na uwiano wa mgawanyiko
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Gawanya seti ya data kuwa makundi ya mafunzo na mtihani (80% mafunzo, 20% mtihani)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Tengeneza saraka ikiwa haipo
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Fungua faili kwa hali ya kuandika
        with open(filepath, 'w', encoding='utf-8') as f:
            # Pitia kila rekodi katika seti ya data
            for record in dataset:
                # Chomeka rekodi kama kitu cha JSON na uandike kwenye faili
                json.dump(record, f)
                # Andika tabia ya mstari mpya kutenganisha rekodi
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Paka na gawanya seti ya data ya ULTRACHAT_200k na usanidi maalum na uwiano wa mgawanyiko
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Chukua seti za data za mafunzo na mtihani kutoka mgawanyiko
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Hifadhi seti ya data ya mafunzo kwenye faili la JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Hifadhi seti ya data ya mtihani kwenye faili tofauti la JSONL
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Andika amri ifuatayo ndani ya terminal yako kuendesha skripti na kupakua dataset kwenye mazingira yako ya ndani.

    ```console
    python download_dataset.py
    ```

1. Thibitisha kuwa datasets zilihifadhiwa kwa mafanikio kwenye saraka ya *finetune-phi/data* kwenye mfumo wako wa ndani.

> [!NOTE]
>
> #### Kumbuka kuhusu ukubwa wa dataset na muda wa fine-tuning
>
> Katika mafunzo haya, unatumia asilimia 1 tu ya dataset (`split='train[:1%]'`). Hii inapunguza kwa kiasi kikubwa kiasi cha data, na kuharakisha mchakato wa kupakia na fine-tuning. Unaweza kurekebisha asilimia ili kupata uwiano sahihi kati ya muda wa mafunzo na utendaji wa modeli. Kutumia sehemu ndogo ya dataset hupunguza muda unaohitajiwa kwa fine-tuning, na kufanya mchakato kuwa rahisi zaidi kwa mafunzo.

## Hali ya 2: Rekebisha modeli ya Phi-3 na Tumia Azure Machine Learning Studio

### Rekebisha modeli ya Phi-3

Katika zoezi hili, utarekebisha modeli ya Phi-3 katika Azure Machine Learning Studio.

Katika zoezi hili, utafanya:

- Unda kundi la kompyuta kwa ajili ya fine-tuning.
- Rekebisha modeli ya Phi-3 katika Azure Machine Learning Studio.

#### Unda kundi la kompyuta kwa ajili ya fine-tuning

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chagua **Compute** kutoka kwenye tabia ya upande wa kushoto.

1. Chagua **Compute clusters** kutoka kwenye menyu ya urambazaji.

1. Chagua **+ New**.

    ![Chagua compute.](../../../../../../translated_images/sw/06-01-select-compute.a29cff290b480252.webp)

1. Fanya kazi zifuatazo:

    - Chagua **Region** ungependa kutumia.
    - Chagua **Virtual machine tier** kuwa **Dedicated**.
    - Chagua **Virtual machine type** kuwa **GPU**.
    - Chagua kichujio cha **Virtual machine size** kwa **Select from all options**.
    - Chagua ukubwa wa **Virtual machine size** kuwa **Standard_NC24ads_A100_v4**.

    ![Unda kundi.](../../../../../../translated_images/sw/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Chagua **Next**.

1. Fanya kazi zifuatazo:

    - Weka **Compute name**. Lazima iwe thamani ya kipekee.
    - Chagua **Minimum number of nodes** kuwa **0**.
    - Chagua **Maximum number of nodes** kuwa **1**.
    - Chagua **Idle seconds before scale down** kuwa **120**.

    ![Unda kundi.](../../../../../../translated_images/sw/06-03-create-cluster.4a54ba20914f3662.webp)

1. Chagua **Create**.

#### Rekebisha modeli ya Phi-3

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chagua eneo la Azure Machine Learning workspace ulilounda.

    ![Chagua workspace ulilounda.](../../../../../../translated_images/sw/06-04-select-workspace.a92934ac04f4f181.webp)

1. Fanya kazi zifuatazo:

    - Chagua **Model catalog** kutoka kwenye tabia ya kushoto.
    - Andika *phi-3-mini-4k* kwenye **barua ya utafutaji** na uchague **Phi-3-mini-4k-instruct** kutoka kwa chaguzi zinazojitokeza.

    ![Andika phi-3-mini-4k.](../../../../../../translated_images/sw/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Chagua **Fine-tune** kutoka kwenye menyu ya urambazaji.

    ![Chagua fine tune.](../../../../../../translated_images/sw/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Fanya kazi zifuatazo:

    - Chagua **Select task type** kuwa **Chat completion**.
    - Chagua **+ Select data** kupakia **Data la Mafunzo**.
    - Chagua aina ya kupakia Data la Uhakiki kuwa **Provide different validation data**.
    - Chagua **+ Select data** kupakia **Data la Uhakiki**.

    ![Jaza ukurasa wa fine-tuning.](../../../../../../translated_images/sw/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Unaweza kuchagua **Advanced settings** kubadilisha mipangilio kama **learning_rate** na **lr_scheduler_type** ili kuboresha mchakato wa fine-tuning kulingana na mahitaji yako maalum.

1. Chagua **Finish**.

1. Katika zoezi hili, umefanikiwa kurekebisha modeli ya Phi-3 kwa kutumia Azure Machine Learning. Tafadhali kumbuka kuwa mchakato wa fine-tuning unaweza kuchukua muda mrefu. Baada ya kuendesha kazi ya fine-tuning, unahitaji kusubiri ikamilike. Unaweza kufuatilia hali ya kazi ya fine-tuning kwa kwenda kwenye tab ya Jobs upande wa kushoto wa Azure Machine Learning Workspace yako. Katika mfululizo unaofuata, utatuma modeli iliyorekebishwa na kuiongeza na Prompt flow.

    ![Tazama kazi ya fine-tuning.](../../../../../../translated_images/sw/06-08-output.2bd32e59930672b1.webp)

### Tuma modeli iliyorekebishwa ya Phi-3

Ili kuunganisha modeli iliyorekebishwa ya Phi-3 na Prompt flow, unahitaji kuituma modeli ili iweze kufikiwa kwa ajili ya utabiri wa wakati halisi. Mchakato huu unahusisha kusajili modeli, kuunda kiungo mtandaoni, na kisha kuituma modeli.

Katika zoezi hili, utafanya:

- Sajili modeli iliyorekebishwa katika Azure Machine Learning workspace.
- Unda kiungo mtandaoni.
- Tuma modeli iliyosajiliwa ya Phi-3 iliyorekebishwa.

#### Sajili modeli iliyorekebishwa

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chagua eneo la Azure Machine Learning workspace ulilounda.

    ![Chagua workspace ulilounda.](../../../../../../translated_images/sw/06-04-select-workspace.a92934ac04f4f181.webp)

1. Chagua **Models** kutoka kwenye tabia ya kushoto.
1. Chagua **+ Register**.
1. Chagua **From a job output**.

    ![Sajili modeli.](../../../../../../translated_images/sw/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Chagua kazi uliyounda.

    ![Chagua kazi.](../../../../../../translated_images/sw/07-02-select-job.3e2e1144cd6cd093.webp)

1. Chagua **Next**.

1. Chagua **Model type** kuwa **MLflow**.

1. Hakikisha kuwa **Job output** imechaguliwa; inapaswa kuchaguliwa kiotomatiki.

    ![Chagua output.](../../../../../../translated_images/sw/07-03-select-output.4cf1a0e645baea1f.webp)

2. Chagua **Next**.

3. Chagua **Register**.

    ![Chagua sajili.](../../../../../../translated_images/sw/07-04-register.fd82a3b293060bc7.webp)

4. Unaweza kuona modeli uliosajili kwa kwenda kwenye menyu ya **Models** kutoka kwa tabia ya kushoto.

    ![Modeli iliyosajiliwa.](../../../../../../translated_images/sw/07-05-registered-model.7db9775f58dfd591.webp)

#### Tuma modeli iliyorekebishwa

1. Nenda kwenye Azure Machine Learning workspace ulilounda.

1. Chagua **Endpoints** kutoka kwenye tabia ya kushoto.

1. Chagua **Real-time endpoints** kutoka kwenye menyu ya urambazaji.

    ![Unda endpoint.](../../../../../../translated_images/sw/07-06-create-endpoint.1ba865c606551f09.webp)

1. Chagua **Create**.

1. Chagua modeli iliyosajiliwa uliyounda.

    ![Chagua modeli iliyosajiliwa.](../../../../../../translated_images/sw/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Chagua **Select**.

1. Fanya kazi zifuatazo:

    - Chagua **Virtual machine** kuwa *Standard_NC6s_v3*.
    - Chagua **Instance count** ungependa kutumia. Kwa mfano, *1*.
    - Chagua **Endpoint** kuwa **New** kuunda endpoint mpya.
    - Weka **Endpoint name**. Lazima iwe thamani ya kipekee.
    - Weka **Deployment name**. Lazima iwe thamani ya kipekee.

    ![Jaza mipangilio ya deployment.](../../../../../../translated_images/sw/07-08-deployment-setting.43ddc4209e673784.webp)

1. Chagua **Deploy**.

> [!WARNING]
> Ili kuepuka malipo ya ziada kwa akaunti yako, hakikisha kufuta endpoint uliounda katika Azure Machine Learning workspace.
>

#### Angalia hali ya deployment katika Azure Machine Learning Workspace

1. Nenda kwenye Azure Machine Learning workspace ulilounda.

1. Chagua **Endpoints** kutoka kwenye tabia ya kushoto.

1. Chagua endpoint uliyounda.

    ![Chagua endpoints](../../../../../../translated_images/sw/07-09-check-deployment.325d18cae8475ef4.webp)

1. Ukurasa huu unaweza kusimamia endpoints wakati wa mchakato wa deployment.

> [!NOTE]
> Mara deployment itakapokamilika, hakikisha **Live traffic** imewekwa kwa **100%**. Ikiwa siyo, chagua **Update traffic** kurekebisha mipangilio ya trafik. Fahamu kuwa huwezi kujaribu modeli ikiwa trafik imewekwa 0%.
>
> ![Weka trafik.](../../../../../../translated_images/sw/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Hali ya 3: Unganisha na Prompt flow na Zungumza na modeli yako maalum katika Microsoft Foundry

### Unganisha modeli maalum ya Phi-3 na Prompt flow

Baada ya kufanikisha kupeleka modeli yako iliyorekebishwa, sasa unaweza kuunganisha na Prompt Flow kutumia modeli yako katika matumizi ya wakati halisi, kuwezesha aina mbalimbali za kazi zinazoshirikiana na modeli maalum ya Phi-3.

Katika zoezi hili, utafanya:

- Unda Microsoft Foundry Hub.
- Unda Mradi wa Microsoft Foundry.
- Unda Prompt flow.
- Ongeza muunganisho maalum kwa modeli iliyorekebishwa ya Phi-3.
- Sanidi Prompt flow kuzungumza na modeli yako maalum ya Phi-3.

> [!NOTE]
> Pia unaweza kuunganisha na Promptflow kwa kutumia Azure ML Studio. Mchakato ule ule wa kuunganisha unaweza kutumika kwa Azure ML Studio.

#### Unda Microsoft Foundry Hub

Unahitaji kuunda Hub kabla ya kuunda Mradi. Hub inafanya kazi kama Kundi la Rasilimali, likikuwezesha kupanga na kusimamia Miradi mingi ndani ya Microsoft Foundry.
1. Tembelea [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Chagua **All hubs** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New hub** kutoka kwenye menyu ya urambazaji.

    ![Create hub.](../../../../../../translated_images/sw/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Fanya kazi zifuatazo:

    - Weka **Hub name**. Lazima iwe thamani ya kipekee.
    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** ya kutumia (tengeneza mpya ikiwa inahitajika).
    - Chagua **Location** unayotaka kutumia.
    - Chagua **Connect Azure AI Services** ya kutumia (tengeneza mpya ikiwa inahitajika).
    - Chagua **Connect Azure AI Search** ili **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sw/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Chagua **Next**.

#### Tengeneza Mradi wa Microsoft Foundry

1. Katika Hub uliotengeneza, chagua **All projects** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New project** kutoka kwenye menyu ya urambazaji.

    ![Select new project.](../../../../../../translated_images/sw/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Weka **Project name**. Lazima iwe thamani ya kipekee.

    ![Create project.](../../../../../../translated_images/sw/08-05-create-project.4d97f0372f03375a.webp)

1. Chagua **Create a project**.

#### Ongeza muunganisho wa kawaida kwa mfano uliobinafsishwa wa Phi-3 uliobinafsishwa

Ili kuunganishwa kwa mfano wako wa kawaida wa Phi-3 na Prompt flow, unahitaji kuhifadhi kituo na ufunguo wa mfano katika muunganisho wa kawaida. Mpangilio huu unahakikisha upatikanaji wa mfano wako wa kawaida wa Phi-3 katika Prompt flow.

#### Weka api key na endpoint uri ya mfano uliobinafsishwa wa Phi-3

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Elekea kwenye eneo la kazi la Azure Machine learning ulilotengeneza.

1. Chagua **Endpoints** kutoka kwenye kichupo cha upande wa kushoto.

    ![Select endpoints.](../../../../../../translated_images/sw/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Chagua kituo (endpoint) ulilotengeneza.

    ![Select endpoints.](../../../../../../translated_images/sw/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Chagua **Consume** kutoka kwenye menyu ya urambazaji.

1. Nakili **REST endpoint** na **Primary key** yako.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sw/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Ongeza Muunganisho wa Kawaida

1. Tembelea [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Elekea kwenye mradi wa Microsoft Foundry ulilotengeneza.

1. Katika Mradi ulilotengeneza, chagua **Settings** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sw/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Chagua **Custom keys** kutoka kwenye menyu ya urambazaji.

    ![Select custom keys.](../../../../../../translated_images/sw/08-10-select-custom-keys.856f6b2966460551.webp)

1. Fanya kazi zifuatazo:

    - Chagua **+ Add key value pairs**.
    - Kwa jina la ufunguo, ingiza **endpoint** na bandika endpoint uliyonakili kutoka Azure ML Studio kwenye kisanduku cha thamani.
    - Chagua tena **+ Add key value pairs**.
    - Kwa jina la ufunguo, ingiza **key** na bandika ufunguo uliyonakili kutoka Azure ML Studio kwenye kisanduku cha thamani.
    - Baada ya kuongeza funguo, chagua **is secret** ili kuzuia ufunguo usionekane wazi.

    ![Add connection.](../../../../../../translated_images/sw/08-11-add-connection.785486badb4d2d26.webp)

1. Chagua **Add connection**.

#### Tengeneza Prompt flow

Umeongeza muunganisho wa kawaida katika Microsoft Foundry. Sasa, wacha tuundie Prompt flow kwa kutumia hatua zifuatazo. Kisha, utaunganisha Prompt flow hii na muunganisho wa kawaida ili uweze kutumia mfano uliobinafsishwa ndani ya Prompt flow.

1. Elekea kwenye mradi wa Microsoft Foundry ulilotengeneza.

1. Chagua **Prompt flow** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ Create** kutoka kwenye menyu ya urambazaji.

    ![Select Promptflow.](../../../../../../translated_images/sw/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Chagua **Chat flow** kutoka kwenye menyu ya urambazaji.

    ![Select chat flow.](../../../../../../translated_images/sw/08-13-select-flow-type.2ec689b22da32591.webp)

1. Weka **Folder name** ya kutumia.

    ![Enter name.](../../../../../../translated_images/sw/08-14-enter-name.ff9520fefd89f40d.webp)

2. Chagua **Create**.

#### Weka Prompt flow kuzungumza na mfano wako wa kawaida wa Phi-3

Unahitaji kuunganisha mfano uliobinafsishwa wa Phi-3 katika Prompt flow. Hata hivyo, Prompt flow iliyopo haikutengenezwa kwa madhumuni haya. Kwa hivyo, lazima upange tena Prompt flow ili kuruhusu kuunganishwa kwa mfano wa kawaida.

1. Katika Prompt flow, fanya kazi zifuatazo kujenga upya mtiririko uliopo:

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

    ![Select raw file mode.](../../../../../../translated_images/sw/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Ongeza msimbo ufuatao kwenye faili *integrate_with_promptflow.py* ili kutumia mfano wa kawaida wa Phi-3 katika Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Mpangilio wa uandishi wa kumbukumbu
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

        # "connection" ni jina la Muunganisho Mbadala, "endpoint", "key" ni funguo katika Muunganisho Mbadala
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
            
            # Andika kumbukumbu ya jibu kamili la JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/sw/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Kwa maelezo zaidi kuhusu kutumia Prompt flow katika Microsoft Foundry, unaweza rejelea [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chagua **Chat input**, **Chat output** kuwezesha mazungumzo na mfano wako.

    ![Input Output.](../../../../../../translated_images/sw/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Sasa uko tayari kuzungumza na mfano wako wa kawaida wa Phi-3. Katika mazoezi yafuatayo, utajifunza jinsi ya kuanzisha Prompt flow na kuitumia kuzungumza na mfano wako uliobinafsishwa wa Phi-3.

> [!NOTE]
>
> Mtiririko ulioumbwa upya unapaswa kuonekana kama picha ifuatayo:
>
> ![Flow example.](../../../../../../translated_images/sw/08-18-graph-example.d6457533952e690c.webp)
>

### Zungumza na mfano wako wa kawaida wa Phi-3

Sasa baada ya kubinafsisha na kuunganisha mfano wako wa kawaida wa Phi-3 na Prompt flow, uko tayari kuanza kuwasiliana nao. Mazoezi haya yataongoza kwa hatua za kuandaa na kuanzisha mazungumzo na mfano wako kwa kutumia Prompt flow. Kwa kufuata hatua hizi, utaweza kutumia kikamilifu uwezo wa mfano wako uliobinafsishwa wa Phi-3 kwa kazi mbalimbali na mazungumzo.

- Zungumza na mfano wako wa kawaida wa Phi-3 ukiwa unatumia Prompt flow.

#### Anzisha Prompt flow

1. Chagua **Start compute sessions** kuanzisha Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sw/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Chagua **Validate and parse input** kusasisha vigezo.

    ![Validate input.](../../../../../../translated_images/sw/09-02-validate-input.317c76ef766361e9.webp)

1. Chagua **Value** ya **connection** kwa muunganisho wa kawaida ulioutengeneza. Kwa mfano, *connection*.

    ![Connection.](../../../../../../translated_images/sw/09-03-select-connection.99bdddb4b1844023.webp)

#### Zungumza na mfano wako wa kawaida

1. Chagua **Chat**.

    ![Select chat.](../../../../../../translated_images/sw/09-04-select-chat.61936dce6612a1e6.webp)

1. Hapa ni mfano wa matokeo: Sasa unaweza kuzungumza na mfano wako wa kawaida wa Phi-3. Inashauriwa kuuliza maswali yanayotegemea data zilizotumiwa kwa ubinafsishaji.

    ![Chat with prompt flow.](../../../../../../translated_images/sw/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Angalizo**:
Hati hii imetatumiwa kwa huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Sisi hatubeba dhamana kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->