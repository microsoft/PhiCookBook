<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:54:51+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "sk"
}
-->
# Doladte a integrujte vlastné modely Phi-3 s Prompt flow v Azure AI Foundry

Tento komplexný (E2E) príklad je založený na návode "[Doladte a integrujte vlastné modely Phi-3 s Prompt Flow v Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Predstavuje procesy doladenia, nasadenia a integrácie vlastných modelov Phi-3 s Prompt flow v Azure AI Foundry. Na rozdiel od E2E príkladu "[Doladte a integrujte vlastné modely Phi-3 s Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ktorý zahŕňal spúšťanie kódu lokálne, sa tento tutoriál zameriava výhradne na doladenie a integráciu vášho modelu priamo v Azure AI / ML Studiu.

## Prehľad

V tomto E2E príklade sa naučíte, ako doladiť model Phi-3 a integrovať ho s Prompt flow v Azure AI Foundry. Využitím Azure AI / ML Studia si vytvoríte pracovný tok na nasadenie a používanie vlastných AI modelov. Tento E2E príklad je rozdelený do troch scenárov:

**Scenár 1: Nastavenie Azure zdrojov a príprava na doladenie**

**Scenár 2: Doladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studiu**

**Scenár 3: Integrácia s Prompt flow a chatovanie s vlastným modelom v Azure AI Foundry**

Tu je prehľad tohto E2E príkladu.

![Phi-3-FineTuning_PromptFlow_Integration Prehľad.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.sk.png)

### Obsah

1. **[Scenár 1: Nastavenie Azure zdrojov a príprava na doladenie](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Vytvorenie Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Žiadosť o GPU kvóty v Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pridanie priradenia rolí](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nastavenie projektu](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Príprava datasetu na doladenie](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenár 2: Doladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studiu](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Doladenie modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasadenie doladeného modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenár 3: Integrácia s Prompt flow a chatovanie s vlastným modelom v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrácia vlastného modelu Phi-3 s Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chatovanie s vlastným modelom Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenár 1: Nastavenie Azure zdrojov a príprava na doladenie

### Vytvorenie Azure Machine Learning Workspace

1. Do **vyhľadávacieho panela** v hornej časti portálu zadajte *azure machine learning* a zo zobrazených možností vyberte **Azure Machine Learning**.

    ![Zadajte azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.sk.png)

2. V navigačnom menu vyberte **+ Create**.

3. V navigačnom menu vyberte **New workspace**.

    ![Vyberte nový workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.sk.png)

4. Vykonajte nasledujúce kroky:

    - Vyberte svoju Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Zadajte **Workspace Name**. Musí byť jedinečný.
    - Vyberte **Region**, ktorý chcete použiť.
    - Vyberte **Storage account**, ktorý chcete použiť (v prípade potreby vytvorte nový).
    - Vyberte **Key vault**, ktorý chcete použiť (v prípade potreby vytvorte nový).
    - Vyberte **Application insights**, ktoré chcete použiť (v prípade potreby vytvorte nové).
    - Vyberte **Container registry**, ktorý chcete použiť (v prípade potreby vytvorte nový).

    ![Vyplňte údaje pre azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.sk.png)

5. Vyberte **Review + Create**.

6. Vyberte **Create**.

### Žiadosť o GPU kvóty v Azure Subscription

V tomto tutoriáli sa naučíte, ako doladiť a nasadiť model Phi-3 s využitím GPU. Na doladenie použijete GPU *Standard_NC24ads_A100_v4*, ktorý vyžaduje žiadosť o kvótu. Na nasadenie použijete GPU *Standard_NC6s_v3*, ktorý tiež vyžaduje žiadosť o kvótu.

> [!NOTE]
>
> GPU alokácia je dostupná len pre predplatné typu Pay-As-You-Go; benefitné predplatné momentálne nie je podporované.
>

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vykonajte nasledujúce kroky na žiadosť o kvótu pre *Standard NCADSA100v4 Family*:

    - Vyberte **Quota** v ľavom menu.
    - Vyberte **Virtual machine family**, napríklad **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ktorá obsahuje GPU *Standard_NC24ads_A100_v4*.
    - Vyberte **Request quota** v navigačnom menu.

        ![Žiadosť o kvótu.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.sk.png)

    - Na stránke Request quota zadajte **New cores limit**, ktorý chcete použiť, napríklad 24.
    - Na stránke Request quota vyberte **Submit** pre odoslanie žiadosti o GPU kvótu.

1. Vykonajte nasledujúce kroky na žiadosť o kvótu pre *Standard NCSv3 Family*:

    - Vyberte **Quota** v ľavom menu.
    - Vyberte **Virtual machine family**, napríklad **Standard NCSv3 Family Cluster Dedicated vCPUs**, ktorá obsahuje GPU *Standard_NC6s_v3*.
    - Vyberte **Request quota** v navigačnom menu.
    - Na stránke Request quota zadajte **New cores limit**, napríklad 24.
    - Na stránke Request quota vyberte **Submit** pre odoslanie žiadosti o GPU kvótu.

### Pridanie priradenia rolí

Na doladenie a nasadenie modelov musíte najskôr vytvoriť User Assigned Managed Identity (UAI) a priradiť jej príslušné oprávnenia. Táto UAI bude použitá na autentifikáciu počas nasadenia.

#### Vytvorenie User Assigned Managed Identity (UAI)

1. Do **vyhľadávacieho panela** v hornej časti portálu zadajte *managed identities* a zo zobrazených možností vyberte **Managed Identities**.

    ![Zadajte managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.sk.png)

1. Vyberte **+ Create**.

    ![Vyberte create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte svoju Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Vyberte **Region**, ktorý chcete použiť.
    - Zadajte **Name**. Musí byť jedinečný.

    ![Vyplňte údaje pre managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.sk.png)

1. Vyberte **Review + create**.

1. Vyberte **+ Create**.

#### Pridanie priradenia roly Contributor k Managed Identity

1. Prejdite na zdroj Managed Identity, ktorý ste vytvorili.

1. V ľavom menu vyberte **Azure role assignments**.

1. V navigačnom menu vyberte **+Add role assignment**.

1. Na stránke Add role assignment vykonajte nasledujúce kroky:
    - Nastavte **Scope** na **Resource group**.
    - Vyberte svoju Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť.
    - Vyberte rolu **Contributor**.

    ![Vyplňte rolu contributor.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.sk.png)

2. Vyberte **Save**.

#### Pridanie priradenia roly Storage Blob Data Reader k Managed Identity

1. Do **vyhľadávacieho panela** v hornej časti portálu zadajte *storage accounts* a zo zobrazených možností vyberte **Storage accounts**.

    ![Zadajte storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.sk.png)

1. Vyberte storage účet, ktorý je priradený k Azure Machine Learning workspace, ktorý ste vytvorili. Napríklad *finetunephistorage*.

1. Vykonajte nasledujúce kroky na navigáciu do stránky Add role assignment:

    - Prejdite do Azure Storage účtu, ktorý ste vytvorili.
    - V ľavom menu vyberte **Access Control (IAM)**.
    - V navigačnom menu vyberte **+ Add**.
    - Vyberte **Add role assignment**.

    ![Pridajte rolu.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.sk.png)

1. Na stránke Add role assignment vykonajte nasledujúce kroky:

    - Do vyhľadávacieho panela na stránke Role zadajte *Storage Blob Data Reader* a vyberte **Storage Blob Data Reader**.
    - Vyberte **Next**.
    - Na stránke Members vyberte **Assign access to** **Managed identity**.
    - Vyberte **+ Select members**.
    - Na stránke Select managed identities vyberte svoju Azure **Subscription**.
    - Vyberte **Managed identity** na **Manage Identity**.
    - Vyberte Manage Identity, ktorú ste vytvorili, napríklad *finetunephi-managedidentity*.
    - Vyberte **Select**.

    ![Vyberte managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.sk.png)

1. Vyberte **Review + assign**.

#### Pridanie priradenia roly AcrPull k Managed Identity

1. Do **vyhľadávacieho panela** v hornej časti portálu zadajte *container registries* a zo zobrazených možností vyberte **Container registries**.

    ![Zadajte container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.sk.png)

1. Vyberte container registry, ktorý je priradený k Azure Machine Learning workspace. Napríklad *finetunephicontainerregistry*.

1. Vykonajte nasledujúce kroky na navigáciu do stránky Add role assignment:

    - V ľavom menu vyberte **Access Control (IAM)**.
    - V navigačnom menu vyberte **+ Add**.
    - Vyberte **Add role assignment**.

1. Na stránke Add role assignment vykonajte nasledujúce kroky:

    - Do vyhľadávacieho panela na stránke Role zadajte *AcrPull* a vyberte **AcrPull**.
    - Vyberte **Next**.
    - Na stránke Members vyberte **Assign access to** **Managed identity**.
    - Vyberte **+ Select members**.
    - Na stránke Select managed identities vyberte svoju Azure **Subscription**.
    - Vyberte **Managed identity** na **Manage Identity**.
    - Vyberte Manage Identity, ktorú ste vytvorili, napríklad *finetunephi-managedidentity*.
    - Vyberte **Select**.
    - Vyberte **Review + assign**.

### Nastavenie projektu

Na stiahnutie datasetov potrebných na doladenie si nastavíte lokálne prostredie.

V tomto cvičení:

- Vytvoríte priečinok, v ktorom budete pracovať.
- Vytvoríte virtuálne prostredie.
- Nainštalujete potrebné balíky.
- Vytvoríte súbor *download_dataset.py* na stiahnutie datasetu.

#### Vytvorenie priečinka na prácu

1. Otvorte terminál a zadajte nasledujúci príkaz na vytvorenie priečinka s názvom *finetune-phi* v predvolenej ceste.

    ```console
    mkdir finetune-phi
    ```

2. Zadajte nasledujúci príkaz v termináli na prechod do priečinka *finetune-phi*, ktorý ste vytvorili.
#### Vytvorte virtuálne prostredie

1. Zadajte nasledujúci príkaz v termináli na vytvorenie virtuálneho prostredia s názvom *.venv*.

    ```console
    python -m venv .venv
    ```

2. Zadajte nasledujúci príkaz v termináli na aktiváciu virtuálneho prostredia.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Ak to fungovalo, mali by ste vidieť *(.venv)* pred príkazovým riadkom.

#### Nainštalujte potrebné balíky

1. Zadajte nasledujúce príkazy v termináli na inštaláciu potrebných balíkov.

    ```console
    pip install datasets==2.19.1
    ```

#### Vytvorte `download_dataset.py`

> [!NOTE]
> Kompletná štruktúra priečinkov:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otvorte **Visual Studio Code**.

1. Vyberte **Súbor** v menu.

1. Vyberte **Otvoriť priečinok**.

1. Vyberte priečinok *finetune-phi*, ktorý ste vytvorili, nachádzajúci sa na *C:\Users\yourUserName\finetune-phi*.

    ![Vyberte priečinok, ktorý ste vytvorili.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.sk.png)

1. V ľavom paneli Visual Studio Code kliknite pravým tlačidlom a vyberte **Nový súbor** na vytvorenie nového súboru s názvom *download_dataset.py*.

    ![Vytvorte nový súbor.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.sk.png)

### Pripravte dataset na doladenie

V tomto cvičení spustíte súbor *download_dataset.py*, ktorý stiahne dataset *ultrachat_200k* do vášho lokálneho prostredia. Tento dataset potom použijete na doladenie modelu Phi-3 v Azure Machine Learning.

V tomto cvičení:

- Pridáte kód do súboru *download_dataset.py* na stiahnutie datasetov.
- Spustíte súbor *download_dataset.py* na stiahnutie datasetov do lokálneho prostredia.

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

1. Zadajte nasledujúci príkaz v termináli na spustenie skriptu a stiahnutie datasetu do lokálneho prostredia.

    ```console
    python download_dataset.py
    ```

1. Overte, či boli datasety úspešne uložené do lokálneho priečinka *finetune-phi/data*.

> [!NOTE]
>
> #### Poznámka k veľkosti datasetu a času doladenia
>
> V tomto návode používate iba 1 % datasetu (`split='train[:1%]'`). To výrazne znižuje množstvo dát, čím sa zrýchľuje nahrávanie aj proces doladenia. Percento môžete upraviť podľa potreby, aby ste našli správnu rovnováhu medzi časom tréningu a výkonom modelu. Použitie menšej časti datasetu skracuje čas potrebný na doladenie, čo robí proces zvládnuteľnejším pre tento návod.

## Scenár 2: Doladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studio

### Doladenie modelu Phi-3

V tomto cvičení doladíte model Phi-3 v Azure Machine Learning Studio.

V tomto cvičení:

- Vytvoríte výpočtový cluster pre doladenie.
- Doladíte model Phi-3 v Azure Machine Learning Studio.

#### Vytvorenie výpočtového clustra pre doladenie

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte **Compute** v ľavom paneli.

1. Vyberte **Compute clusters** v navigačnom menu.

1. Vyberte **+ New**.

    ![Vyberte compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Región**, ktorý chcete použiť.
    - Vyberte **Virtual machine tier** na **Dedicated**.
    - Vyberte **Virtual machine type** na **GPU**.
    - Vyberte filter **Virtual machine size** na **Select from all options**.
    - Vyberte **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Vytvorte cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.sk.png)

1. Vyberte **Next**.

1. Vykonajte nasledujúce kroky:

    - Zadajte **Compute name**. Musí byť jedinečný.
    - Vyberte **Minimum number of nodes** na **0**.
    - Vyberte **Maximum number of nodes** na **1**.
    - Vyberte **Idle seconds before scale down** na **120**.

    ![Vytvorte cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.sk.png)

1. Vyberte **Create**.

#### Doladenie modelu Phi-3

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte Azure Machine Learning workspace, ktorý ste vytvorili.

    ![Vyberte workspace, ktorý ste vytvorili.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Model catalog** v ľavom paneli.
    - Do **vyhľadávacieho poľa** zadajte *phi-3-mini-4k* a vyberte **Phi-3-mini-4k-instruct** z ponúkaných možností.

    ![Zadajte phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.sk.png)

1. Vyberte **Fine-tune** v navigačnom menu.

    ![Vyberte fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Select task type** na **Chat completion**.
    - Vyberte **+ Select data** na nahranie **Tréningových dát**.
    - Vyberte typ nahrávania validačných dát na **Provide different validation data**.
    - Vyberte **+ Select data** na nahranie **Validačných dát**.

    ![Vyplňte stránku doladenia.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.sk.png)

    > [!TIP]
    >
    > Môžete vybrať **Advanced settings** na prispôsobenie nastavení ako **learning_rate** a **lr_scheduler_type** pre optimalizáciu procesu doladenia podľa vašich potrieb.

1. Vyberte **Finish**.

1. V tomto cvičení ste úspešne doladili model Phi-3 pomocou Azure Machine Learning. Upozorňujeme, že proces doladenia môže trvať pomerne dlho. Po spustení doladenia je potrebné počkať na jeho dokončenie. Stav doladenia môžete sledovať v záložke Jobs v ľavom paneli vášho Azure Machine Learning Workspace. V ďalšej časti nasadíte doladený model a integrujete ho s Prompt flow.

    ![Zobraziť úlohu doladenia.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.sk.png)

### Nasadenie doladeného modelu Phi-3

Na integráciu doladeného modelu Phi-3 s Prompt flow je potrebné model nasadiť, aby bol dostupný pre inferenciu v reálnom čase. Tento proces zahŕňa registráciu modelu, vytvorenie online endpointu a nasadenie modelu.

V tomto cvičení:

- Zaregistrujete doladený model v Azure Machine Learning workspace.
- Vytvoríte online endpoint.
- Nasadíte registrovaný doladený model Phi-3.

#### Registrácia doladeného modelu

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte Azure Machine Learning workspace, ktorý ste vytvorili.

    ![Vyberte workspace, ktorý ste vytvorili.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.sk.png)

1. Vyberte **Models** v ľavom paneli.
1. Vyberte **+ Register**.
1. Vyberte **From a job output**.

    ![Registrácia modelu.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.sk.png)

1. Vyberte úlohu, ktorú ste vytvorili.

    ![Vyberte úlohu.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.sk.png)

1. Vyberte **Next**.

1. Vyberte **Model type** na **MLflow**.

1. Uistite sa, že je vybratý **Job output**; malo by byť vybrané automaticky.

    ![Vyberte výstup.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.sk.png)

2. Vyberte **Next**.

3. Vyberte **Register**.

    ![Vyberte registráciu.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.sk.png)

4. Registrovaný model si môžete pozrieť v menu **Models** v ľavom paneli.

    ![Registrovaný model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.sk.png)

#### Nasadenie doladeného modelu

1. Prejdite do Azure Machine Learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** v ľavom paneli.

1. Vyberte **Real-time endpoints** v navigačnom menu.

    ![Vytvorte endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.sk.png)

1. Vyberte **Create**.

1. Vyberte registrovaný model, ktorý ste vytvorili.

    ![Vyberte registrovaný model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.sk.png)

1. Vyberte **Select**.

1. Vykonajte nasledujúce kroky:

    - Vyberte **Virtual machine** na *Standard_NC6s_v3*.
    - Vyberte počet inštancií, ktoré chcete použiť, napríklad *1*.
    - Vyberte **Endpoint** na **New** pre vytvorenie nového endpointu.
    - Zadajte **Endpoint name**. Musí byť jedinečný.
    - Zadajte **Deployment name**. Musí byť jedinečný.

    ![Vyplňte nastavenia nasadenia.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.sk.png)

1. Vyberte **Deploy**.

> [!WARNING]
> Aby ste predišli dodatočným poplatkom, nezabudnite odstrániť vytvorený endpoint v Azure Machine Learning workspace.
>

#### Skontrolujte stav nasadenia v Azure Machine Learning Workspace

1. Prejdite do Azure Machine Learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** v ľavom paneli.

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Vyberte endpointy](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.sk.png)

1. Na tejto stránke môžete spravovať endpointy počas procesu nasadenia.

> [!NOTE]
> Po dokončení nasadenia sa uistite, že **Live traffic** je nastavený na **100 %**. Ak nie je, vyberte **Update traffic** na úpravu nastavení prenosu. Model nie je možné testovať, ak je prenos nastavený na 0 %.
>
> ![Nastavte prenos.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.sk.png)
>

## Scenár 3: Integrácia s Prompt flow a chatovanie s vlastným modelom v Azure AI Foundry

### Integrácia vlastného modelu Phi-3 s Prompt flow

Po úspešnom nasadení doladeného modelu ho môžete integrovať s Prompt Flow, aby ste mohli model používať v aplikáciách v reálnom čase a umožnili tak rôzne interaktívne úlohy s vaším vlastným modelom Phi-3.

V tomto cvičení:

- Vytvoríte Azure AI Foundry Hub.
- Vytvoríte Azure AI Foundry projekt.
- Vytvoríte Prompt flow.
- Pridáte vlastné pripojenie pre doladený model Phi-3.
- Nastavíte Prompt flow na chatovanie s vaším vlastným modelom Phi-3.
> [!NOTE]
> Môžete sa tiež integrovať s Promptflow pomocou Azure ML Studio. Rovnaký integračný proces je možné použiť aj v Azure ML Studio.
#### Vytvorenie Azure AI Foundry Hubu

Pred vytvorením projektu je potrebné vytvoriť Hub. Hub funguje ako Resource Group, ktorá vám umožňuje organizovať a spravovať viacero projektov v rámci Azure AI Foundry.

1. Navštívte [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Vyberte **All hubs** v ľavom paneli.

1. Vyberte **+ New hub** v navigačnom menu.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.sk.png)

1. Vykonajte nasledujúce kroky:

    - Zadajte **Hub name**. Musí byť jedinečný.
    - Vyberte svoju Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Vyberte **Location**, ktorú chcete použiť.
    - Vyberte **Connect Azure AI Services**, ktoré chcete použiť (v prípade potreby vytvorte nové).
    - Vyberte **Connect Azure AI Search** a zvoľte **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.sk.png)

1. Kliknite na **Next**.

#### Vytvorenie Azure AI Foundry projektu

1. V Hube, ktorý ste vytvorili, vyberte **All projects** v ľavom paneli.

1. Vyberte **+ New project** v navigačnom menu.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.sk.png)

1. Zadajte **Project name**. Musí byť jedinečný.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.sk.png)

1. Kliknite na **Create a project**.

#### Pridanie vlastného pripojenia pre doladený model Phi-3

Aby ste integrovali svoj vlastný model Phi-3 s Prompt flow, je potrebné uložiť endpoint a kľúč modelu do vlastného pripojenia. Tento krok zabezpečí prístup k vášmu doladenému modelu Phi-3 v Prompt flow.

#### Nastavenie api kľúča a endpoint URI doladeného modelu Phi-3

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Prejdite do Azure Machine learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** v ľavom paneli.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.sk.png)

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.sk.png)

1. Vyberte **Consume** v navigačnom menu.

1. Skopírujte svoj **REST endpoint** a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.sk.png)

#### Pridanie vlastného pripojenia

1. Navštívte [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Prejdite do Azure AI Foundry projektu, ktorý ste vytvorili.

1. V projekte vyberte **Settings** v ľavom paneli.

1. Vyberte **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.sk.png)

1. Vyberte **Custom keys** v navigačnom menu.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.sk.png)

1. Vykonajte nasledujúce kroky:

    - Kliknite na **+ Add key value pairs**.
    - Ako názov kľúča zadajte **endpoint** a do hodnoty vložte endpoint, ktorý ste skopírovali z Azure ML Studio.
    - Opäť kliknite na **+ Add key value pairs**.
    - Ako názov kľúča zadajte **key** a do hodnoty vložte kľúč, ktorý ste skopírovali z Azure ML Studio.
    - Po pridaní kľúčov zaškrtnite **is secret**, aby sa kľúč nezobrazoval.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.sk.png)

1. Kliknite na **Add connection**.

#### Vytvorenie Prompt flow

Pridali ste vlastné pripojenie v Azure AI Foundry. Teraz vytvoríme Prompt flow podľa nasledujúcich krokov. Následne toto Prompt flow prepojíte s vlastným pripojením, aby ste mohli používať doladený model v rámci Prompt flow.

1. Prejdite do Azure AI Foundry projektu, ktorý ste vytvorili.

1. Vyberte **Prompt flow** v ľavom paneli.

1. Vyberte **+ Create** v navigačnom menu.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.sk.png)

1. Vyberte **Chat flow** v navigačnom menu.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.sk.png)

1. Zadajte **Folder name**, ktorý chcete použiť.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.sk.png)

2. Kliknite na **Create**.

#### Nastavenie Prompt flow pre chat s vaším vlastným modelom Phi-3

Je potrebné integrovať doladený model Phi-3 do Prompt flow. Existujúce Prompt flow však nie je na tento účel navrhnuté, preto ho musíte prerobiť, aby umožňovalo integráciu vlastného modelu.

1. V Prompt flow vykonajte nasledujúce kroky na prestavbu existujúceho flow:

    - Vyberte **Raw file mode**.
    - Vymažte všetok existujúci kód v súbore *flow.dag.yml*.
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

    - Kliknite na **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.sk.png)

1. Pridajte nasledujúci kód do súboru *integrate_with_promptflow.py* pre použitie vlastného modelu Phi-3 v Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.sk.png)

> [!NOTE]
> Pre podrobnejšie informácie o používaní Prompt flow v Azure AI Foundry môžete navštíviť [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output** pre povolenie chatu s vaším modelom.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.sk.png)

1. Teraz ste pripravení komunikovať s vaším vlastným modelom Phi-3. V ďalšej úlohe sa naučíte, ako spustiť Prompt flow a používať ho na chatovanie s doladeným modelom Phi-3.

> [!NOTE]
>
> Prestavaný flow by mal vyzerať ako na obrázku nižšie:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.sk.png)
>

### Chatovanie s vaším vlastným modelom Phi-3

Keďže ste doladili a integrovali svoj vlastný model Phi-3 s Prompt flow, ste pripravení začať s ním komunikovať. Táto úloha vás prevedie nastavením a spustením chatu s modelom pomocou Prompt flow. Dodržiavaním týchto krokov budete môcť plne využiť schopnosti vášho doladeného modelu Phi-3 pre rôzne úlohy a konverzácie.

- Komunikujte s vaším vlastným modelom Phi-3 pomocou Prompt flow.

#### Spustenie Prompt flow

1. Kliknite na **Start compute sessions** pre spustenie Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.sk.png)

1. Kliknite na **Validate and parse input** pre obnovenie parametrov.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.sk.png)

1. Vyberte **Value** pre **connection** na vlastné pripojenie, ktoré ste vytvorili. Napríklad *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.sk.png)

#### Chatovanie s vaším vlastným modelom

1. Kliknite na **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.sk.png)

1. Tu je príklad výsledkov: Teraz môžete komunikovať s vaším vlastným modelom Phi-3. Odporúča sa klásť otázky založené na dátach použitých pri doladení.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.sk.png)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.