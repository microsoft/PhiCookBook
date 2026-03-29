# Doladenie a integrácia vlastných modelov Phi-3 s Prompt flow v Microsoft Foundry

Tento end-to-end (E2E) príklad je založený na návode "[Doladenie a integrácia vlastných modelov Phi-3 s Prompt Flow v Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Predstavuje procesy doladenia, nasadenia a integrácie vlastných modelov Phi-3 s Prompt flow v Microsoft Foundry. Na rozdiel od E2E príkladu, "[Doladenie a integrácia vlastných modelov Phi-3 s Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ktorý zahŕňal spúšťanie kódu lokálne, sa tento tutoriál sústreďuje výhradne na doladenie a integráciu vášho modelu v rámci Azure AI / ML Studio.

## Prehľad

V tomto E2E príklade sa naučíte, ako doladiť model Phi-3 a integrovať ho s Prompt flow v Microsoft Foundry. Využitím Azure AI / ML Studia si vytvoríte pracovný tok na nasadenie a využívanie vlastných AI modelov. Tento E2E príklad je rozdelený do troch scenárov:

**Scenár 1: Nastavenie Azure zdrojov a príprava na doladenie**

**Scenár 2: Doladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studio**

**Scenár 3: Integrácia s Prompt flow a chatovanie s vaším vlastným modelom v Microsoft Foundry**

Tu je prehľad tohto E2E príkladu.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/sk/00-01-architecture.198ba0f1ae6d841a.webp)

### Obsah

1. **[Scenár 1: Nastavenie Azure zdrojov a príprava na doladenie](#scenár-1-nastavenie-azure-zdrojov-a-príprava-na-doladenie)**
    - [Vytvorenie Azure Machine Learning Workspace](#vytvorenie-azure-machine-learning-workspace)
    - [Žiadosť o GPU kvóty v Azure Subscription](#žiadosť-o-gpu-kvóty-v-azure-subscription)
    - [Pridanie priradenia role](#pridanie-priradenia-role)
    - [Nastavenie projektu](#nastavenie-projektu)
    - [Príprava datasetu na doladenie](#pripravte-dataset-na-doladenie)

1. **[Scenár 2: Doladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studio](#scenár-2-doladenie-modelu-phi-3-a-nasadenie-v-azure-machine-learning-studio)**
    - [Doladenie modelu Phi-3](#doladenie-modelu-phi-3)
    - [Nasadenie doladeného modelu Phi-3](#nasadenie-doladeného-modelu-phi-3)

1. **[Scenár 3: Integrácia s Prompt flow a chatovanie s vaším vlastným modelom v Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrácia vlastného modelu Phi-3 s Prompt flow](#integrácia-vlastného-modelu-phi-3-s-prompt-flow)
    - [Chatovanie s vaším vlastným modelom Phi-3](#chatovanie-s-vlastným-modelom-phi-3)

## Scenár 1: Nastavenie Azure zdrojov a príprava na doladenie

### Vytvorenie Azure Machine Learning Workspace

1. Do **vyhľadávacieho riadku** v hornej časti portálu zadajte *azure machine learning* a vyberte **Azure Machine Learning** z zobrazenej ponuky.

    ![Type azure machine learning.](../../../../../../translated_images/sk/01-01-type-azml.acae6c5455e67b4b.webp)

2. Vyberte **+ Create** z navigačného menu.

3. Vyberte **New workspace** z navigačného menu.

    ![Select new workspace.](../../../../../../translated_images/sk/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Vykonajte nasledujúce úlohy:

    - Vyberte svoj Azure **Subscription**.
    - Vyberte **Resource group** na použitie (vytvorte novú, ak je to potrebné).
    - Zadajte **Workspace Name**. Musí byť jedinečný.
    - Vyberte **Región**, ktorý chcete použiť.
    - Vyberte **Storage account** na použitie (vytvorte nový, ak je to potrebné).
    - Vyberte **Key vault** na použitie (vytvorte nový, ak je to potrebné).
    - Vyberte **Application insights** na použitie (vytvorte nové, ak je to potrebné).
    - Vyberte **Container registry** na použitie (vytvorte nové, ak je to potrebné).

    ![Fill azure machine learning.](../../../../../../translated_images/sk/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Vyberte **Review + Create**.

6. Vyberte **Create**.

### Žiadosť o GPU kvóty v Azure Subscription

V tomto návode sa naučíte, ako doladiť a nasadiť model Phi-3 pomocou GPU. Pre doladenie použijete GPU *Standard_NC24ads_A100_v4*, ktorá vyžaduje žiadosť o kvótu. Pre nasadenie použijete GPU *Standard_NC6s_v3*, ktorá tiež vyžaduje žiadosť o kvótu.

> [!NOTE]
>
> Len Pay-As-You-Go predplatné (štandardný typ predplatného) je oprávnené získať GPU; benefitné predplatné momentálne nie sú podporované.
>

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vykonajte nasledujúce kroky na žiadosť o kvótu *Standard NCADSA100v4 Family*:

    - Vyberte **Quota** z ľavého menu.
    - Vyberte **Virtual machine family** na použitie. Napríklad vyberte **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ktorá obsahuje GPU *Standard_NC24ads_A100_v4*.
    - Vyberte **Request quota** z navigačnej ponuky.

        ![Request quota.](../../../../../../translated_images/sk/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na stránke Request quota zadajte **New cores limit**, ktorý chcete použiť, napríklad 24.
    - Na stránke Request quota vyberte **Submit** na požiadanie o GPU kvótu.

1. Vykonajte nasledujúce kroky na žiadosť o kvótu *Standard NCSv3 Family*:

    - Vyberte **Quota** z ľavého menu.
    - Vyberte **Virtual machine family** na použitie. Napríklad vyberte **Standard NCSv3 Family Cluster Dedicated vCPUs**, ktorá obsahuje GPU *Standard_NC6s_v3*.
    - Vyberte **Request quota** z navigačnej ponuky.
    - Na stránke Request quota zadajte **New cores limit**, ktorý chcete použiť. Napríklad 24.
    - Na stránke Request quota vyberte **Submit** na požiadanie o GPU kvótu.

### Pridanie priradenia role

Na doladenie a nasadenie modelov musíte najskôr vytvoriť User Assigned Managed Identity (UAI) a priradiť jej príslušné povolenia. Táto UAI sa použije na autentifikáciu počas nasadenia.

#### Vytvorenie User Assigned Managed Identity (UAI)

1. Do **vyhľadávacieho riadku** v hornej časti portálu zadajte *managed identities* a vyberte **Managed Identities** z zobrazenej ponuky.

    ![Type managed identities.](../../../../../../translated_images/sk/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Vyberte **+ Create**.

    ![Select create.](../../../../../../translated_images/sk/03-02-select-create.92bf8989a5cd98f2.webp)

1. Vykonajte nasledujúce úlohy:

    - Vyberte svoj Azure **Subscription**.
    - Vyberte **Resource group** na použitie (vytvorte novú, ak je to potrebné).
    - Vyberte **Región**, ktorý chcete použiť.
    - Zadajte **Meno**. Musí byť jedinečné.

    ![Select create.](../../../../../../translated_images/sk/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Vyberte **Review + create**.

1. Vyberte **+ Create**.

#### Pridanie priradenia roly Contributor Managed Identity

1. Prejdite na zdroj Managed Identity, ktorý ste vytvorili.

1. Vyberte **Azure role assignments** z ľavého menu.

1. Vyberte **+Add role assignment** z navigačnej ponuky.

1. Na stránke Add role assignment vykonajte nasledovné úlohy:
    - Vyberte **Scope** na **Resource group**.
    - Vyberte svoj Azure **Subscription**.
    - Vyberte **Resource group** na použitie.
    - Vyberte **Role** na **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/sk/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Vyberte **Save**.

#### Pridanie priradenia roly Storage Blob Data Reader Managed Identity

1. Do **vyhľadávacieho riadku** v hornej časti portálu zadajte *storage accounts* a vyberte **Storage accounts** z zobrazenej ponuky.

    ![Type storage accounts.](../../../../../../translated_images/sk/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Vyberte storage account, ktorý je spojený s Azure Machine Learning workspace, ktorý ste vytvorili. Napríklad *finetunephistorage*.

1. Vykonajte nasledujúce kroky na navigáciu na stránku Add role assignment:

    - Prejdite do Azure Storage účtu, ktorý ste vytvorili.
    - Vyberte **Access Control (IAM)** z ľavého menu.
    - Vyberte **+ Add** z navigačnej ponuky.
    - Vyberte **Add role assignment** z navigačnej ponuky.

    ![Add role.](../../../../../../translated_images/sk/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na stránke Add role assignment vykonajte nasledovné úlohy:

    - Na stránke Role zadajte do **vyhľadávacieho riadku** *Storage Blob Data Reader* a vyberte **Storage Blob Data Reader** z ponuky.
    - Na stránke Role vyberte **Next**.
    - Na stránke Members vyberte **Assign access to** **Managed identity**.
    - Na stránke Members vyberte **+ Select members**.
    - Na stránke Select managed identities vyberte svoj Azure **Subscription**.
    - Na stránke Select managed identities vyberte **Managed identity** na **Manage Identity**.
    - Na stránke Select managed identities vyberte Manage Identity, ktorú ste vytvorili. Napríklad *finetunephi-managedidentity*.
    - Na stránke Select managed identities vyberte **Select**.

    ![Select managed identity.](../../../../../../translated_images/sk/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Vyberte **Review + assign**.

#### Pridanie priradenia roly AcrPull Managed Identity

1. Do **vyhľadávacieho riadku** v hornej časti portálu zadajte *container registries* a vyberte **Container registries** z ponuky.

    ![Type container registries.](../../../../../../translated_images/sk/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Vyberte container registry, ktorý súvisí s Azure Machine Learning workspace. Napríklad *finetunephicontainerregistry*

1. Vykonajte tieto kroky na navigáciu na stránku Add role assignment:

    - Vyberte **Access Control (IAM)** z ľavého menu.
    - Vyberte **+ Add** z navigačnej ponuky.
    - Vyberte **Add role assignment** z navigačnej ponuky.

1. Na stránke Add role assignment vykonajte tieto úlohy:

    - Na stránke Role zadajte do **vyhľadávacieho riadku** *AcrPull* a vyberte **AcrPull** z ponuky.
    - Na stránke Role vyberte **Next**.
    - Na stránke Members vyberte **Assign access to** **Managed identity**.
    - Na stránke Members vyberte **+ Select members**.
    - Na stránke Select managed identities vyberte svoj Azure **Subscription**.
    - Na stránke Select managed identities vyberte **Managed identity** na **Manage Identity**.
    - Na stránke Select managed identities vyberte Manage Identity, ktorú ste vytvorili, napríklad *finetunephi-managedidentity*.
    - Na stránke Select managed identities vyberte **Select**.
    - Vyberte **Review + assign**.

### Nastavenie projektu

Na stiahnutie datasetov potrebných na doladenie si nastavíte lokálne prostredie.

V tomto cvičení:

- Vytvoríte priečinok, v ktorom budete pracovať.
- Vytvoríte virtuálne prostredie.
- Nainštalujete potrebné balíčky.
- Vytvoríte súbor *download_dataset.py* na stiahnutie datasetu.

#### Vytvorenie priečinka na prácu

1. Otvorte terminál a zadajte nasledujúci príkaz na vytvorenie priečinka s názvom *finetune-phi* v predvolenej ceste.

    ```console
    mkdir finetune-phi
    ```

2. Zadajte v termináli nasledujúci príkaz na prechod do vytvoreného priečinka *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Vytvorenie virtuálneho prostredia

1. Zadajte v termináli nasledujúci príkaz na vytvorenie virtuálneho prostredia s názvom *.venv*.
    ```console
    python -m venv .venv
    ```

2. Zadajte nasledujúci príkaz do terminálu na aktiváciu virtuálneho prostredia.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ak to fungovalo, mali by ste vidieť *(.venv)* pred príkazovým riadkom.

#### Inštalujte požadované balíky

1. Zadajte nasledujúce príkazy do terminálu na inštaláciu požadovaných balíkov.

    ```console
    pip install datasets==2.19.1
    ```

#### Vytvorte `donload_dataset.py`

> [!NOTE]
> Kompletná štruktúra priečinka:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otvorte **Visual Studio Code**.

1. Vyberte **File** v lište menu.

1. Vyberte **Open Folder**.

1. Vyberte priečinok *finetune-phi*, ktorý ste vytvorili, nachádzajúci sa na *C:\Users\yourUserName\finetune-phi*.

    ![Vyberte priečinok ktorý ste vytvorili.](../../../../../../translated_images/sk/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. V ľavom paneli Visual Studio Code kliknite pravým tlačidlom a vyberte **New File** na vytvorenie nového súboru s názvom *download_dataset.py*.

    ![Vytvorte nový súbor.](../../../../../../translated_images/sk/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Pripravte dataset na doladenie

V tomto cvičení spustíte súbor *download_dataset.py*, aby ste stiahli datasety *ultrachat_200k* do vášho lokálneho prostredia. Následne tieto datasety použijete na doladenie modelu Phi-3 v Azure Machine Learning.

V tomto cvičení:

- Pridáte kód do súboru *download_dataset.py*, aby ste stiahli datasety.
- Spustíte súbor *download_dataset.py*, aby ste stiahli datasety do vášho lokálneho prostredia.

#### Stiahnite si dataset pomocou *download_dataset.py*

1. Otvorte súbor *download_dataset.py* vo Visual Studio Code.

1. Pridajte nasledujúci kód do súboru *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Načítajte dataset so zadaným názvom, konfiguráciou a pomerom rozdelenia
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Rozdeľte dataset na trénovacie a testovacie sady (80 % trénovanie, 20 % testovanie)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Vytvorte adresár, ak neexistuje
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Otvorte súbor v režime zápisu
        with open(filepath, 'w', encoding='utf-8') as f:
            # Prejdite každý záznam v datasete
            for record in dataset:
                # Uložte záznam ako JSON objekt a zapíšte ho do súboru
                json.dump(record, f)
                # Zapíšte znak nového riadku pre oddelenie záznamov
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Načítajte a rozdelte dataset ULTRACHAT_200k so špecifickou konfiguráciou a pomerom rozdelenia
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrahujte trénovací a testovací dataset z rozdelenia
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Uložte trénovací dataset do JSONL súboru
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Uložte testovací dataset do samostatného JSONL súboru
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Zadajte nasledujúci príkaz v termináli na spustenie skriptu a stiahnutie datasetu do lokálneho prostredia.

    ```console
    python download_dataset.py
    ```

1. Overte, či boli datasety úspešne uložené do vášho lokálneho priečinka *finetune-phi/data*.

> [!NOTE]
>
> #### Poznámka o veľkosti datasetu a čase doladenia
>
> V tomto návode používate iba 1 % datasetu (`split='train[:1%]'`). To výrazne znižuje množstvo dát, čím zrýchľuje nahrávanie aj proces doladenia. Percentuálny podiel môžete upraviť podľa potreby, aby ste našli správnu rovnováhu medzi časom trénovania a výkonnosťou modelu. Použitie menšieho podielu datasetu znižuje čas potrebný na doladenie, čo uľahčuje prácu s návodom.

## Scenár 2: Doladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studio

### Doladenie modelu Phi-3

V tomto cvičení doladíte model Phi-3 v Azure Machine Learning Studio.

V tomto cvičení:

- Vytvoríte výpočtový klaster pre doladenie.
- Doladíte model Phi-3 v Azure Machine Learning Studio.

#### Vytvorenie výpočtového klastru pre doladenie

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte **Compute** v ľavom paneli.

1. Vyberte **Compute clusters** v navigačnom menu.

1. Vyberte **+ New**.

    ![Vyberte compute.](../../../../../../translated_images/sk/06-01-select-compute.a29cff290b480252.webp)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Región**, ktorý chcete použiť.
    - Nastavte **Virtual machine tier** na **Dedicated**.
    - Nastavte **Virtual machine type** na **GPU**.
    - Nastavte filter **Virtual machine size** na **Select from all options**.
    - Vyberte veľkosť **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Vytvorenie klastru.](../../../../../../translated_images/sk/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Vyberte **Next**.

1. Vykonajte nasledujúce nastavenia:

    - Zadajte jedinečný **Compute name**.
    - Nastavte **Minimálny počet uzlov** na **0**.
    - Nastavte **Maximálny počet uzlov** na **1**.
    - Nastavte **Idle seconds before scale down** na **120**.

    ![Vytvorenie klastru.](../../../../../../translated_images/sk/06-03-create-cluster.4a54ba20914f3662.webp)

1. Vyberte **Create**.

#### Doladenie modelu Phi-3

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte Azure Machine Learning workspace, ktorý ste vytvorili.

    ![Vyberte workspace, ktorý ste vytvorili.](../../../../../../translated_images/sk/06-04-select-workspace.a92934ac04f4f181.webp)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Model catalog** v ľavom paneli.
    - Do **vyhľadávacieho poľa** napíšte *phi-3-mini-4k* a vyberte **Phi-3-mini-4k-instruct** z dostupných možností.

    ![Napíšte phi-3-mini-4k.](../../../../../../translated_images/sk/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Vyberte **Fine-tune** v navigačnom menu.

    ![Vyberte doladenie.](../../../../../../translated_images/sk/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Vykonajte nasledujúce kroky:

    - Nastavte **Select task type** na **Chat completion**.
    - Vyberte **+ Select data** na nahranie **Tréningových dát**.
    - Nastavte typ nahrávania validačných dát na **Provide different validation data**.
    - Vyberte **+ Select data** na nahranie **Validačných dát**.

    ![Vyplňte stránku doladenia.](../../../../../../translated_images/sk/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Môžete vybrať **Advanced settings** na prispôsobenie nastavení ako **learning_rate** a **lr_scheduler_type** na optimalizáciu doladenia podľa vašich potrieb.

1. Vyberte **Finish**.

1. V tomto cvičení ste úspešne doladili model Phi-3 pomocou Azure Machine Learning. Upozorňujeme, že proces doladenia môže trvať značný čas. Po spustení doladiacej úlohy musíte počkať na jej dokončenie. Stav doladiacej úlohy môžete sledovať v záložke Jobs v ľavom paneli vášho Azure Machine Learning Workspace. V nasledujúcom postupe nasadíte doladený model a integrujete ho s Prompt flow.

    ![Pozrite si úlohu doladenia.](../../../../../../translated_images/sk/06-08-output.2bd32e59930672b1.webp)

### Nasadenie doladeného modelu Phi-3

Aby ste mohli integrovať doladený model Phi-3 s Prompt flow, musíte model nasadiť, aby bol dostupný pre inferenciu v reálnom čase. Tento proces zahŕňa registráciu modelu, vytvorenie online endpointu a samotné nasadenie modelu.

V tomto cvičení:

- Zaregistrujete doladený model v Azure Machine Learning workspace.
- Vytvoríte online endpoint.
- Nasadíte registrovaný doladený model Phi-3.

#### Registrácia doladeného modelu

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte Azure Machine Learning workspace, ktorý ste vytvorili.

    ![Vyberte workspace, ktorý ste vytvorili.](../../../../../../translated_images/sk/06-04-select-workspace.a92934ac04f4f181.webp)

1. Vyberte **Models** v ľavom paneli.
1. Vyberte **+ Register**.
1. Vyberte **From a job output**.

    ![Registrovať model.](../../../../../../translated_images/sk/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Vyberte úlohu, ktorú ste spustili.

    ![Vyberte úlohu.](../../../../../../translated_images/sk/07-02-select-job.3e2e1144cd6cd093.webp)

1. Vyberte **Next**.

1. Nastavte **Model type** na **MLflow**.

1. Uistite sa, že je vybraný **Job output**; malo by byť vybrané automaticky.

    ![Vyberte výstup.](../../../../../../translated_images/sk/07-03-select-output.4cf1a0e645baea1f.webp)

2. Vyberte **Next**.

3. Vyberte **Register**.

    ![Vyberte register.](../../../../../../translated_images/sk/07-04-register.fd82a3b293060bc7.webp)

4. Registrovaný model môžete zobraziť v menu **Models** v ľavom paneli.

    ![Registrovaný model.](../../../../../../translated_images/sk/07-05-registered-model.7db9775f58dfd591.webp)

#### Nasadenie doladeného modelu

1. Prejdite do Azure Machine Learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** v ľavom paneli.

1. Vyberte **Real-time endpoints** v navigačnom menu.

    ![Vytvorte endpoint.](../../../../../../translated_images/sk/07-06-create-endpoint.1ba865c606551f09.webp)

1. Vyberte **Create**.

1. Vyberte registrovaný model, ktorý ste vytvorili.

    ![Vyberte registrovaný model.](../../../../../../translated_images/sk/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Vyberte **Select**.

1. Vykonajte nasledujúce kroky:

    - Vyberte **Virtual machine** na *Standard_NC6s_v3*.
    - Vyberte **Instance count**, ktorý chcete použiť. Napríklad *1*.
    - Nastavte **Endpoint** na **New** na vytvorenie endpointu.
    - Zadajte **Endpoint name**. Musí byť jedinečný.
    - Zadajte **Deployment name**. Musí byť jedinečný.

    ![Vyplňte nastavenia nasadenia.](../../../../../../translated_images/sk/07-08-deployment-setting.43ddc4209e673784.webp)

1. Vyberte **Deploy**.

> [!WARNING]
> Aby ste predišli ďalším poplatkom na vašom účte, nezabudnite zmazať vytvorený endpoint v Azure Machine Learning workspace.
>

#### Kontrola stavu nasadenia v Azure Machine Learning Workspace

1. Prejdite do Azure Machine Learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** v ľavom paneli.

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Vyberte endpointy](../../../../../../translated_images/sk/07-09-check-deployment.325d18cae8475ef4.webp)

1. Na tejto stránke môžete spravovať endpointy počas procesu nasadenia.

> [!NOTE]
> Po dokončení nasadenia sa uistite, že **Live traffic** je nastavený na **100%**. Ak nie je, vyberte **Update traffic** na úpravu nastavení prenosu. Ak je prenos nastavený na 0 %, nemôžete model testovať.
>
> ![Nastavte prenos.](../../../../../../translated_images/sk/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenár 3: Integrácia s Prompt flow a chatovanie s vlastným modelom v Microsoft Foundry

### Integrácia vlastného modelu Phi-3 s Prompt flow

Po úspešnom nasadení vášho doladeného modelu ho môžete integrovať s Prompt Flow, aby ste mohli model používať v aplikáciách v reálnom čase a umožnili rôzne interaktívne úlohy s vaším vlastným modelom Phi-3.

V tomto cvičení:

- Vytvoríte Microsoft Foundry Hub.
- Vytvoríte Microsoft Foundry Projekt.
- Vytvoríte Prompt flow.
- Pridáte vlastné pripojenie pre doladený model Phi-3.
- Nastavíte Prompt flow na chatovanie s vaším vlastným modelom Phi-3

> [!NOTE]
> Integráciu s Promptflow môžete tiež vykonať pomocou Azure ML Studio. Rovnaký integračný proces platí pre Azure ML Studio.

#### Vytvorenie Microsoft Foundry Hub

Je potrebné vytvoriť Hub pred vytvorením Projektu. Hub funguje ako Resource Group, ktorá vám umožní organizovať a spravovať niekoľko Projektov v rámci Microsoft Foundry.
1. Navštívte [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Vyberte **Všetky huby** z ľavého bočného panela.

1. Vyberte **+ Nový hub** z navigačného menu.

    ![Create hub.](../../../../../../translated_images/sk/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Vykonajte nasledujúce úlohy:

    - Zadajte **Názov hubu**. Musí byť jedinečná hodnota.
    - Vyberte svoj Azure **Predplatné**.
    - Vyberte **Skupinu prostriedkov** na použitie (vytvorte novú, ak je to potrebné).
    - Vyberte **Lokalitu**, ktorú chcete použiť.
    - Vyberte **Pripojiť Azure AI služby** na použitie (vytvorte novú, ak je to potrebné).
    - Vyberte **Pripojiť Azure AI vyhľadávanie** a zvoľte **Preskočiť pripojenie**.

    ![Fill hub.](../../../../../../translated_images/sk/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Vyberte **Ďalej**.

#### Vytvorte projekt v Microsoft Foundry

1. V hube, ktorý ste vytvorili, vyberte **Všetky projekty** z ľavého bočného panela.

1. Vyberte **+ Nový projekt** z navigačného menu.

    ![Select new project.](../../../../../../translated_images/sk/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Zadajte **Názov projektu**. Musí byť jedinečná hodnota.

    ![Create project.](../../../../../../translated_images/sk/08-05-create-project.4d97f0372f03375a.webp)

1. Vyberte **Vytvoriť projekt**.

#### Pridanie vlastného pripojenia pre jemne doladený model Phi-3

Na integráciu vášho vlastného modelu Phi-3 s Prompt flow je potrebné uložiť koncový bod modelu a kľúč v rámci vlastného pripojenia. Táto konfigurácia zabezpečí prístup k vášmu vlastnému modelu Phi-3 v Prompt flow.

#### Nastavenie api kľúča a URI koncového bodu jemne doladeného modelu Phi-3

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Prejdite do pracovného priestoru Azure Machine learning, ktorý ste vytvorili.

1. Vyberte **Koncové body** z ľavého bočného panela.

    ![Select endpoints.](../../../../../../translated_images/sk/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Vyberte koncový bod, ktorý ste vytvorili.

    ![Select endpoints.](../../../../../../translated_images/sk/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Vyberte **Použiť** z navigačného menu.

1. Skopírujte svoj **REST endpoint** a **Primárny kľúč**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sk/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Pridajte vlastné pripojenie

1. Navštívte [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Prejdite do projektu Microsoft Foundry, ktorý ste vytvorili.

1. V projekte, ktorý ste vytvorili, vyberte **Nastavenia** z ľavého bočného panela.

1. Vyberte **+ Nové pripojenie**.

    ![Select new connection.](../../../../../../translated_images/sk/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Vyberte **Vlastné kľúče** z navigačného menu.

    ![Select custom keys.](../../../../../../translated_images/sk/08-10-select-custom-keys.856f6b2966460551.webp)

1. Vykonajte nasledujúce úlohy:

    - Vyberte **+ Pridať dvojice kľúč - hodnota**.
    - Pre názov kľúča zadajte **endpoint** a vložte koncový bod, ktorý ste skopírovali z Azure ML Studio, do poľa hodnota.
    - Opäť vyberte **+ Pridať dvojice kľúč - hodnota**.
    - Pre názov kľúča zadajte **key** a vložte kľúč, ktorý ste skopírovali z Azure ML Studio, do poľa hodnota.
    - Po pridaní kľúčov vyberte **je tajný** na zabránenie zverejneniu kľúča.

    ![Add connection.](../../../../../../translated_images/sk/08-11-add-connection.785486badb4d2d26.webp)

1. Vyberte **Pridať pripojenie**.

#### Vytvorte Prompt flow

Pridali ste vlastné pripojenie v Microsoft Foundry. Teraz vytvoríme Prompt flow pomocou nasledujúcich krokov. Následne pripojíte tento Prompt flow k vlastnému pripojeniu, aby ste mohli používať jemne doladený model v rámci Prompt flow.

1. Prejdite do projektu Microsoft Foundry, ktorý ste vytvorili.

1. Vyberte **Prompt flow** z ľavého bočného panela.

1. Vyberte **+ Vytvoriť** z navigačného menu.

    ![Select Promptflow.](../../../../../../translated_images/sk/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Vyberte **Chat flow** z navigačného menu.

    ![Select chat flow.](../../../../../../translated_images/sk/08-13-select-flow-type.2ec689b22da32591.webp)

1. Zadajte **Názov priečinka** na použitie.

    ![Enter name.](../../../../../../translated_images/sk/08-14-enter-name.ff9520fefd89f40d.webp)

2. Vyberte **Vytvoriť**.

#### Nastavte Prompt flow na chatovanie s vaším vlastným modelom Phi-3

Je potrebné integrovať jemne doladený model Phi-3 do Prompt flow. Existujúci Prompt flow nie je pre tento účel navrhnutý. Preto je potrebné prepracovať Prompt flow, aby umožnil integráciu vlastného modelu.

1. V Prompt flow vykonajte tieto úlohy na prestavbu existujúceho toku:

    - Vyberte **Režim surového súboru**.
    - Odstráňte všetok existujúci kód v súbore *flow.dag.yml*.
    - Pridajte nasledujúci kód do súboru *flow.dag.yml*.

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

    - Vyberte **Uložiť**.

    ![Select raw file mode.](../../../../../../translated_images/sk/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Pridajte nasledujúci kód do súboru *integrate_with_promptflow.py* na použitie vlastného modelu Phi-3 v Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Nastavenie protokolovania
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

        # "connection" je názov vlastného pripojenia, "endpoint", "key" sú kľúče vo vlastnom pripojení
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
            
            # Protokolovať celú JSON odpoveď
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

    ![Paste prompt flow code.](../../../../../../translated_images/sk/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Pre podrobnejšie informácie o používaní Prompt flow v Microsoft Foundry môžete nahliadnuť do [Prompt flow v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Vstup chatu**, **Výstup chatu** na povolenie chatovania s vaším modelom.

    ![Input Output.](../../../../../../translated_images/sk/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Teraz ste pripravení chatovať s vaším vlastným modelom Phi-3. V ďalšom cvičení sa naučíte, ako spustiť Prompt flow a použiť ho na chatovanie s vaším jemne doladeným modelom Phi-3.

> [!NOTE]
>
> Prestavaný tok by mal vyzerať ako na obrázku nižšie:
>
> ![Flow example.](../../../../../../translated_images/sk/08-18-graph-example.d6457533952e690c.webp)
>

### Chatovanie s vlastným modelom Phi-3

Teraz, keď ste jemne doladili a integrovali vlastný model Phi-3 s Prompt flow, ste pripravení začať s ním komunikovať. Toto cvičenie vás prevedie procesom nastavenia a spustenia chatu s vaším modelom pomocou Prompt flow. Dodržiavaním týchto krokov budete môcť plne využiť možnosti vášho jemne doladeného modelu Phi-3 na rôzne úlohy a konverzácie.

- Chatovanie s vlastným modelom Phi-3 pomocou Prompt flow.

#### Spustite Prompt flow

1. Vyberte **Spustiť výpočtové relácie** na spustenie Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sk/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Vyberte **Overiť a rozparsovať vstup** na obnovenie parametrov.

    ![Validate input.](../../../../../../translated_images/sk/09-02-validate-input.317c76ef766361e9.webp)

1. Vyberte **Hodnotu** **pripojenia** k vlastnému pripojeniu, ktoré ste vytvorili. Napríklad *connection*.

    ![Connection.](../../../../../../translated_images/sk/09-03-select-connection.99bdddb4b1844023.webp)

#### Chatovanie s vlastným modelom

1. Vyberte **Chat**.

    ![Select chat.](../../../../../../translated_images/sk/09-04-select-chat.61936dce6612a1e6.webp)

1. Tu je príklad výsledkov: Teraz môžete chatovať s vaším vlastným modelom Phi-3. Odporúča sa klásť otázky vychádzajúce z dát použitých na jemné doladenie.

    ![Chat with prompt flow.](../../../../../../translated_images/sk/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhradenie zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu nenesieme zodpovednosť.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->