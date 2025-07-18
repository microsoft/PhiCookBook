<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:51:51+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hu"
}
-->
# Finomhangold és integráld az egyedi Phi-3 modelleket a Prompt flow-val az Azure AI Foundry-ban

Ez az end-to-end (E2E) példa a Microsoft Tech Community "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" útmutatóján alapul. Bemutatja az egyedi Phi-3 modellek finomhangolásának, telepítésének és integrálásának folyamatát a Prompt flow-val az Azure AI Foundry-ban.  
Ellentétben az E2E mintával, a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)"-vel, amely helyi kód futtatást igényelt, ez a bemutató teljes egészében az Azure AI / ML Studio-n belüli finomhangolásra és integrációra fókuszál.

## Áttekintés

Ebben az E2E példában megtanulod, hogyan finomhangold a Phi-3 modellt, és hogyan integráld azt a Prompt flow-val az Azure AI Foundry-ban. Az Azure AI / ML Studio segítségével létrehozol egy munkafolyamatot az egyedi AI modellek telepítésére és használatára. Ez az E2E minta három forgatókönyvre van bontva:

**1. forgatókönyv: Azure erőforrások beállítása és előkészítés a finomhangoláshoz**

**2. forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban**

**3. forgatókönyv: Integráció a Prompt flow-val és csevegés az egyedi modelleddel az Azure AI Foundry-ban**

Íme az E2E minta áttekintése.

![Phi-3-FineTuning_PromptFlow_Integration Áttekintés.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.hu.png)

### Tartalomjegyzék

1. **[1. forgatókönyv: Azure erőforrások beállítása és előkészítés a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace létrehozása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvóták igénylése az Azure előfizetésben](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Szerepkör hozzárendelés hozzáadása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt beállítása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adatkészlet előkészítése a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[2. forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 modell finomhangolása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Finomhangolt Phi-3 modell telepítése](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[3. forgatókönyv: Integráció a Prompt flow-val és csevegés az egyedi modelleddel az Azure AI Foundry-ban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Egyedi Phi-3 modell integrálása a Prompt flow-val](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Csevegés az egyedi Phi-3 modelleddel](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 1. forgatókönyv: Azure erőforrások beállítása és előkészítés a finomhangoláshoz

### Azure Machine Learning Workspace létrehozása

1. Írd be az *azure machine learning* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki az **Azure Machine Learning** lehetőséget a megjelenő opciók közül.

    ![Írd be az azure machine learning kifejezést.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.hu.png)

2. Válaszd a **+ Create** lehetőséget a navigációs menüből.

3. Válaszd a **New workspace** lehetőséget a navigációs menüből.

    ![Válaszd az új munkaterületet.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.hu.png)

4. Végezze el a következő lépéseket:

    - Válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot** (ha szükséges, hozz létre újat).
    - Add meg a **Workspace nevét**. Egyedi értéknek kell lennie.
    - Válaszd ki a használni kívánt **Régiót**.
    - Válaszd ki a használni kívánt **Tárolófiókot** (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Key vault-ot** (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Application insights**-t (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Container registry**-t (ha szükséges, hozz létre újat).

    ![Töltsd ki az azure machine learning adatokat.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.hu.png)

5. Válaszd a **Review + Create** lehetőséget.

6. Válaszd a **Create** lehetőséget.

### GPU kvóták igénylése az Azure előfizetésben

Ebben a bemutatóban megtanulod, hogyan finomhangold és telepítsd a Phi-3 modellt GPU-k használatával. A finomhangoláshoz a *Standard_NC24ads_A100_v4* GPU-t fogod használni, amelyhez kvótaigénylés szükséges. A telepítéshez a *Standard_NC6s_v3* GPU-t használod, amely szintén kvótaigénylést igényel.

> [!NOTE]
>
> Csak a Pay-As-You-Go előfizetések (az alapértelmezett előfizetési típus) jogosultak GPU-kiosztásra; a kedvezményes előfizetések jelenleg nem támogatottak.
>

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Végezze el a következő lépéseket a *Standard NCADSA100v4 Family* kvóta igényléséhez:

    - Válaszd a bal oldali menüben a **Quota** lehetőséget.
    - Válaszd ki a használni kívánt **Virtuális gép családot**. Például válaszd a **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** opciót, amely tartalmazza a *Standard_NC24ads_A100_v4* GPU-t.
    - Válaszd a navigációs menüből a **Request quota** lehetőséget.

        ![Kvóta igénylése.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.hu.png)

    - A Request quota oldalon add meg az új **cores limit** értéket, amelyet használni szeretnél. Például 24.
    - A Request quota oldalon válaszd a **Submit** gombot a GPU kvóta igényléséhez.

1. Végezze el a következő lépéseket a *Standard NCSv3 Family* kvóta igényléséhez:

    - Válaszd a bal oldali menüben a **Quota** lehetőséget.
    - Válaszd ki a használni kívánt **Virtuális gép családot**. Például válaszd a **Standard NCSv3 Family Cluster Dedicated vCPUs** opciót, amely tartalmazza a *Standard_NC6s_v3* GPU-t.
    - Válaszd a navigációs menüből a **Request quota** lehetőséget.
    - A Request quota oldalon add meg az új **cores limit** értéket, amelyet használni szeretnél. Például 24.
    - A Request quota oldalon válaszd a **Submit** gombot a GPU kvóta igényléséhez.

### Szerepkör hozzárendelés hozzáadása

A modellek finomhangolásához és telepítéséhez először létre kell hoznod egy User Assigned Managed Identity-t (UAI), és hozzá kell rendelned a megfelelő jogosultságokat. Ezt az UAI-t fogod használni az autentikációhoz a telepítés során.

#### User Assigned Managed Identity (UAI) létrehozása

1. Írd be a *managed identities* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki a **Managed Identities** lehetőséget a megjelenő opciók közül.

    ![Írd be a managed identities kifejezést.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.hu.png)

1. Válaszd a **+ Create** lehetőséget.

    ![Válaszd a létrehozást.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.hu.png)

1. Végezze el a következő lépéseket:

    - Válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot** (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Régiót**.
    - Add meg a **Nevet**. Egyedi értéknek kell lennie.

    ![Töltsd ki a managed identities adatokat.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.hu.png)

1. Válaszd a **Review + create** lehetőséget.

1. Válaszd a **+ Create** lehetőséget.

#### Contributor szerepkör hozzárendelése a Managed Identity-hez

1. Navigálj a létrehozott Managed Identity erőforráshoz.

1. Válaszd a bal oldali menüből az **Azure role assignments** lehetőséget.

1. Válaszd a navigációs menüből a **+Add role assignment** lehetőséget.

1. Az Add role assignment oldalon végezd el a következőket:
    - Állítsd be a **Scope**-ot **Resource group**-ra.
    - Válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot**.
    - Válaszd ki a **Contributor** szerepkört.

    ![Töltsd ki a contributor szerepkört.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.hu.png)

2. Válaszd a **Save** lehetőséget.

#### Storage Blob Data Reader szerepkör hozzárendelése a Managed Identity-hez

1. Írd be a *storage accounts* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki a **Storage accounts** lehetőséget a megjelenő opciók közül.

    ![Írd be a storage accounts kifejezést.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.hu.png)

1. Válaszd ki azt a tárolófiókot, amely az általad létrehozott Azure Machine Learning munkaterülethez tartozik. Például *finetunephistorage*.

1. Végezze el a következő lépéseket az Add role assignment oldal eléréséhez:

    - Navigálj az általad létrehozott Azure Storage fiókhoz.
    - Válaszd a bal oldali menüből az **Access Control (IAM)** lehetőséget.
    - Válaszd a navigációs menüből a **+ Add** lehetőséget.
    - Válaszd a **Add role assignment** lehetőséget.

    ![Szerepkör hozzáadása.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.hu.png)

1. Az Add role assignment oldalon végezd el a következőket:

    - A Role oldalon írd be a keresősávba a *Storage Blob Data Reader* kifejezést, majd válaszd ki a megjelenő opciók közül a **Storage Blob Data Reader**-t.
    - A Role oldalon válaszd a **Next** lehetőséget.
    - A Members oldalon válaszd az **Assign access to** mezőben a **Managed identity** opciót.
    - A Members oldalon válaszd a **+ Select members** lehetőséget.
    - A Select managed identities oldalon válaszd ki az Azure **Előfizetésedet**.
    - A Select managed identities oldalon válaszd ki a **Managed identity**-t, amely a **Manage Identity** típusú.
    - A Select managed identities oldalon válaszd ki a létrehozott Managed Identity-t. Például *finetunephi-managedidentity*.
    - A Select managed identities oldalon válaszd a **Select** lehetőséget.

    ![Managed identity kiválasztása.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.hu.png)

1. Válaszd a **Review + assign** lehetőséget.

#### AcrPull szerepkör hozzárendelése a Managed Identity-hez

1. Írd be a *container registries* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki a **Container registries** lehetőséget a megjelenő opciók közül.

    ![Írd be a container registries kifejezést.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.hu.png)

1. Válaszd ki azt a container registry-t, amely az Azure Machine Learning munkaterülethez tartozik. Például *finetunephicontainerregistry*.

1. Végezze el a következő lépéseket az Add role assignment oldal eléréséhez:

    - Válaszd a bal oldali menüből az **Access Control (IAM)** lehetőséget.
    - Válaszd a navigációs menüből a **+ Add** lehetőséget.
    - Válaszd a **Add role assignment** lehetőséget.

1. Az Add role assignment oldalon végezd el a következőket:

    - A Role oldalon írd be a keresősávba az *AcrPull* kifejezést, majd válaszd ki a megjelenő opciók közül az **AcrPull**-t.
    - A Role oldalon válaszd a **Next** lehetőséget.
    - A Members oldalon válaszd az **Assign access to** mezőben a **Managed identity** opciót.
    - A Members oldalon válaszd a **+ Select members** lehetőséget.
    - A Select managed identities oldalon válaszd ki az Azure **Előfizetésedet**.
    - A Select managed identities oldalon válaszd ki a **Managed identity**-t, amely a **Manage Identity** típusú.
    - A Select managed identities oldalon válaszd ki a létrehozott Managed Identity-t. Például *finetunephi-managedidentity*.
    - A Select managed identities oldalon válaszd a **Select** lehetőséget.
    - Válaszd a **Review + assign** lehetőséget.

### Projekt beállítása

A finomhangoláshoz szükséges adatkészletek letöltéséhez helyi környezetet állítasz be.

Ebben a gyakorlatban:

- Létrehozol egy mappát, amelyben dolgozni fogsz.
- Létrehozol egy virtuális környezetet.
- Telepíted a szükséges csomagokat.
- Létrehozol egy *download_dataset.py* fájlt az adatkészlet letöltéséhez.

#### Mappa létrehozása a munkához

1. Nyiss meg egy terminálablakot, és írd be a következő parancsot egy *finetune-phi* nevű mappa létrehozásához az alapértelmezett útvonalon.

    ```console
    mkdir finetune-phi
    ```

2. Írd be a következő parancsot a terminálba, hogy belépj a létrehozott *finetune-phi* mappába.
#### Hozz létre egy virtuális környezetet

1. Írd be a következő parancsot a terminálodba egy *.venv* nevű virtuális környezet létrehozásához.

    ```console
    python -m venv .venv
    ```

2. Írd be a következő parancsot a terminálodba a virtuális környezet aktiválásához.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Ha sikerült, akkor a parancssor előtt meg kell jelennie a *(.venv)* jelzésnek.

#### Telepítsd a szükséges csomagokat

1. Írd be a következő parancsokat a terminálodba a szükséges csomagok telepítéséhez.

    ```console
    pip install datasets==2.19.1
    ```

#### Hozd létre a `download_dataset.py` fájlt

> [!NOTE]
> Teljes mappaszerkezet:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Nyisd meg a **Visual Studio Code**-ot.

1. Válaszd ki a menüsorból a **File** menüpontot.

1. Válaszd az **Open Folder** lehetőséget.

1. Válaszd ki a *finetune-phi* mappát, amit létrehoztál, amely a *C:\Users\yourUserName\finetune-phi* helyen található.

    ![Válaszd ki a létrehozott mappát.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.hu.png)

1. A Visual Studio Code bal oldali paneljén kattints jobb gombbal, majd válaszd az **New File** lehetőséget egy új *download_dataset.py* nevű fájl létrehozásához.

    ![Hozz létre egy új fájlt.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.hu.png)

### Készítsd elő az adathalmazt a finomhangoláshoz

Ebben a gyakorlatban lefuttatod a *download_dataset.py* fájlt, hogy letöltsd az *ultrachat_200k* adathalmazokat a helyi környezetedbe. Ezt követően ezt az adathalmazt fogod használni a Phi-3 modell finomhangolásához az Azure Machine Learning-ben.

Ebben a gyakorlatban:

- Kódot adsz hozzá a *download_dataset.py* fájlhoz az adathalmazok letöltéséhez.
- Lefuttatod a *download_dataset.py* fájlt, hogy letöltsd az adathalmazokat a helyi környezetedbe.

#### Töltsd le az adathalmazodat a *download_dataset.py* segítségével

1. Nyisd meg a *download_dataset.py* fájlt a Visual Studio Code-ban.

1. Illeszd be a következő kódot a *download_dataset.py* fájlba.

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

1. Írd be a következő parancsot a terminálodba a szkript futtatásához és az adathalmaz letöltéséhez a helyi környezetedbe.

    ```console
    python download_dataset.py
    ```

1. Ellenőrizd, hogy az adathalmazok sikeresen elmentésre kerültek-e a helyi *finetune-phi/data* könyvtárba.

> [!NOTE]
>
> #### Megjegyzés az adathalmaz méretéről és a finomhangolás idejéről
>
> Ebben a bemutatóban csak az adathalmaz 1%-át használod (`split='train[:1%]'`). Ez jelentősen csökkenti az adatmennyiséget, így gyorsítva a feltöltést és a finomhangolást. A százalékos arányt módosíthatod, hogy megtaláld az optimális egyensúlyt a tanítási idő és a modell teljesítménye között. Az adathalmaz kisebb részhalmazának használata lerövidíti a finomhangolás idejét, így a folyamat kezelhetőbbé válik egy bemutató számára.

## 2. Forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban

### Finomhangold a Phi-3 modellt

Ebben a gyakorlatban a Phi-3 modellt finomhangolod az Azure Machine Learning Studioban.

Ebben a gyakorlatban:

- Létrehozol egy számítógép klasztert a finomhangoláshoz.
- Finomhangolod a Phi-3 modellt az Azure Machine Learning Studioban.

#### Hozz létre számítógép klasztert a finomhangoláshoz

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki a bal oldali menüből a **Compute** menüpontot.

1. A navigációs menüből válaszd a **Compute clusters** lehetőséget.

1. Kattints a **+ New** gombra.

    ![Válaszd a compute menüpontot.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.hu.png)

1. Végezze el a következő beállításokat:

    - Válaszd ki a használni kívánt **Region** régiót.
    - Állítsd a **Virtual machine tier** értékét **Dedicated**-re.
    - Állítsd a **Virtual machine type** értékét **GPU**-ra.
    - A **Virtual machine size** szűrőt állítsd **Select from all options**-ra.
    - Válaszd ki a **Virtual machine size**-t: **Standard_NC24ads_A100_v4**.

    ![Klaszter létrehozása.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.hu.png)

1. Kattints a **Next** gombra.

1. Végezze el a következő beállításokat:

    - Írd be a **Compute name**-et. Egyedi értéknek kell lennie.
    - Állítsd a **Minimum number of nodes** értékét **0**-ra.
    - Állítsd a **Maximum number of nodes** értékét **1**-re.
    - Állítsd az **Idle seconds before scale down** értékét **120**-ra.

    ![Klaszter létrehozása.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.hu.png)

1. Kattints a **Create** gombra.

#### Finomhangold a Phi-3 modellt

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki az általad létrehozott Azure Machine Learning munkaterületet.

    ![Válaszd ki a létrehozott munkaterületet.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hu.png)

1. Végezze el a következő lépéseket:

    - Válaszd ki a bal oldali menüből a **Model catalog** menüpontot.
    - Írd be a keresőmezőbe a *phi-3-mini-4k* kifejezést, majd válaszd ki a megjelenő lehetőségek közül a **Phi-3-mini-4k-instruct** modellt.

    ![Írd be a phi-3-mini-4k kifejezést.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.hu.png)

1. Válaszd ki a navigációs menüből a **Fine-tune** lehetőséget.

    ![Válaszd a finomhangolást.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.hu.png)

1. Végezze el a következő beállításokat:

    - Állítsd a **Select task type** értékét **Chat completion**-re.
    - Kattints a **+ Select data** gombra a **Training data** feltöltéséhez.
    - A validációs adatok feltöltési módját állítsd **Provide different validation data**-ra.
    - Kattints a **+ Select data** gombra a **Validation data** feltöltéséhez.

    ![Töltsd ki a finomhangolási oldalt.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.hu.png)

    > [!TIP]
    >
    > Az **Advanced settings** alatt testreszabhatod a konfigurációkat, például a **learning_rate** és **lr_scheduler_type** értékeket, hogy a finomhangolás a saját igényeid szerint optimalizálható legyen.

1. Kattints a **Finish** gombra.

1. Ebben a gyakorlatban sikeresen finomhangoltad a Phi-3 modellt az Azure Machine Learning segítségével. Fontos megjegyezni, hogy a finomhangolási folyamat jelentős időt vehet igénybe. A finomhangolási feladat futtatása után várnod kell a befejezésére. A finomhangolási feladat állapotát az Azure Machine Learning munkaterület bal oldali menüjében a Jobs fülön követheted nyomon. A következő részben telepíted a finomhangolt modellt és integrálod a Prompt Flow-val.

    ![Lásd a finomhangolási feladatot.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.hu.png)

### Telepítsd a finomhangolt Phi-3 modellt

Ahhoz, hogy a finomhangolt Phi-3 modellt integráld a Prompt Flow-val, telepítened kell a modellt, hogy valós idejű lekérdezésekhez elérhető legyen. Ez a folyamat magában foglalja a modell regisztrálását, egy online végpont létrehozását és a modell telepítését.

Ebben a gyakorlatban:

- Regisztrálod a finomhangolt modellt az Azure Machine Learning munkaterületen.
- Létrehozol egy online végpontot.
- Telepíted a regisztrált finomhangolt Phi-3 modellt.

#### Regisztráld a finomhangolt modellt

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki az általad létrehozott Azure Machine Learning munkaterületet.

    ![Válaszd ki a létrehozott munkaterületet.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hu.png)

1. Válaszd ki a bal oldali menüből a **Models** menüpontot.

1. Kattints a **+ Register** gombra.

1. Válaszd a **From a job output** lehetőséget.

    ![Regisztráld a modellt.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.hu.png)

1. Válaszd ki a létrehozott feladatot.

    ![Válaszd ki a feladatot.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.hu.png)

1. Kattints a **Next** gombra.

1. Állítsd a **Model type** értékét **MLflow**-ra.

1. Győződj meg róla, hogy a **Job output** ki van választva; ennek automatikusan ki kell választódnia.

    ![Válaszd ki a kimenetet.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.hu.png)

2. Kattints a **Next** gombra.

3. Kattints a **Register** gombra.

    ![Kattints a regisztrálásra.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.hu.png)

4. A regisztrált modell megtekintéséhez navigálj a bal oldali menü **Models** menüpontjához.

    ![Regisztrált modell.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.hu.png)

#### Telepítsd a finomhangolt modellt

1. Navigálj az általad létrehozott Azure Machine Learning munkaterületre.

1. Válaszd ki a bal oldali menüből az **Endpoints** menüpontot.

1. A navigációs menüből válaszd a **Real-time endpoints** lehetőséget.

    ![Hozz létre végpontot.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.hu.png)

1. Kattints a **Create** gombra.

1. Válaszd ki a regisztrált modellt, amit létrehoztál.

    ![Válaszd ki a regisztrált modellt.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.hu.png)

1. Kattints a **Select** gombra.

1. Végezze el a következő beállításokat:

    - Állítsd a **Virtual machine** értékét *Standard_NC6s_v3*-ra.
    - Állítsd be a kívánt **Instance count** értéket, például *1*.
    - Állítsd az **Endpoint** értékét **New**-re egy új végpont létrehozásához.
    - Írd be az **Endpoint name**-et. Egyedi értéknek kell lennie.
    - Írd be a **Deployment name**-et. Egyedi értéknek kell lennie.

    ![Töltsd ki a telepítési beállításokat.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.hu.png)

1. Kattints a **Deploy** gombra.

> [!WARNING]
> A további költségek elkerülése érdekében győződj meg róla, hogy törlöd a létrehozott végpontot az Azure Machine Learning munkaterületen.
>

#### Ellenőrizd a telepítés állapotát az Azure Machine Learning munkaterületen

1. Navigálj az általad létrehozott Azure Machine Learning munkaterületre.

1. Válaszd ki a bal oldali menüből az **Endpoints** menüpontot.

1. Válaszd ki a létrehozott végpontot.

    ![Válaszd ki a végpontokat.](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.hu.png)

1. Ezen az oldalon kezelheted a végpontokat a telepítési folyamat során.

> [!NOTE]
> A telepítés befejezése után győződj meg róla, hogy a **Live traffic** értéke **100%**. Ha nem az, válaszd az **Update traffic** lehetőséget a forgalom beállításainak módosításához. Ne feledd, hogy a modellt nem tudod tesztelni, ha a forgalom 0%-ra van állítva.
>
> ![Állítsd be a forgalmat.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.hu.png)
>

## 3. Forgatókönyv: Integráció a Prompt Flow-val és csevegés a saját modelleddel az Azure AI Foundry-ban

### Integráld a saját Phi-3 modellt a Prompt Flow-val

Miután sikeresen telepítetted a finomhangolt modellt, most integrálhatod azt a Prompt Flow-val, hogy valós idejű alkalmazásokban használhasd, lehetővé téve különféle interaktív feladatok végrehajtását a saját Phi-3 modelleddel.

Ebben a gyakorlatban:

- Létrehozol egy Azure AI Foundry Hub-ot.
- Létrehozol egy Azure AI Foundry projektet.
- Létrehozol egy Prompt Flow-t.
- Hozzáadsz egy egyedi kapcsolatot a finomhangolt Phi-3 modellhez.
- Beállítod a Prompt Flow-t, hogy csevegj a saját Phi-3 modelleddel.
> [!NOTE]
> A Promptflow-val való integrációt az Azure ML Studio segítségével is elvégezheted. Ugyanez az integrációs folyamat alkalmazható az Azure ML Studioban is.
#### Azure AI Foundry Hub létrehozása

A Projekt létrehozása előtt létre kell hoznod egy Hub-ot. A Hub olyan, mint egy Erőforráscsoport, amely lehetővé teszi, hogy több Projektet szervezz és kezelj az Azure AI Foundry-n belül.

1. Látogass el az [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Válaszd ki a bal oldali fülön az **All hubs** lehetőséget.

1. A navigációs menüből válaszd a **+ New hub** opciót.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.hu.png)

1. Végezze el a következő lépéseket:

    - Írd be a **Hub name**-et. Egyedi értéknek kell lennie.
    - Válaszd ki az Azure **Subscription**-t.
    - Válaszd ki a használni kívánt **Resource group**-ot (ha szükséges, hozz létre újat).
    - Válaszd ki a kívánt **Location**-t.
    - Válaszd ki a használni kívánt **Connect Azure AI Services**-t (ha szükséges, hozz létre újat).
    - A **Connect Azure AI Search** esetén válaszd a **Skip connecting** lehetőséget.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.hu.png)

1. Kattints a **Next** gombra.

#### Azure AI Foundry Projekt létrehozása

1. A létrehozott Hub-ban válaszd ki a bal oldali fülön az **All projects** lehetőséget.

1. A navigációs menüből válaszd a **+ New project** opciót.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.hu.png)

1. Írd be a **Project name**-et. Egyedi értéknek kell lennie.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.hu.png)

1. Kattints a **Create a project** gombra.

#### Egyedi kapcsolat hozzáadása a finomhangolt Phi-3 modellhez

Ahhoz, hogy a saját Phi-3 modelledet integráld a Prompt flow-val, el kell mentened a modell végpontját és kulcsát egy egyedi kapcsolatban. Ez a beállítás biztosítja, hogy a Prompt flow hozzáférjen a finomhangolt Phi-3 modelledhez.

#### A finomhangolt Phi-3 modell api kulcsának és végpont URI-jának beállítása

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Navigálj a létrehozott Azure Machine learning munkaterületre.

1. Válaszd ki a bal oldali fülön az **Endpoints** lehetőséget.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.hu.png)

1. Válaszd ki a létrehozott végpontot.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.hu.png)

1. A navigációs menüből válaszd a **Consume** opciót.

1. Másold ki a **REST endpoint**-ot és a **Primary key**-t.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.hu.png)

#### Egyedi kapcsolat hozzáadása

1. Látogass el az [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Navigálj a létrehozott Azure AI Foundry projekthez.

1. A létrehozott Projektben válaszd ki a bal oldali fülön a **Settings** lehetőséget.

1. Válaszd a **+ New connection** opciót.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.hu.png)

1. A navigációs menüből válaszd a **Custom keys** lehetőséget.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.hu.png)

1. Végezze el a következő lépéseket:

    - Válaszd a **+ Add key value pairs** opciót.
    - A kulcsnévhez írd be: **endpoint**, majd illeszd be az Azure ML Studio-ból kimásolt végpontot az érték mezőbe.
    - Ismét válaszd a **+ Add key value pairs** opciót.
    - A kulcsnévhez írd be: **key**, majd illeszd be az Azure ML Studio-ból kimásolt kulcsot az érték mezőbe.
    - A kulcsok hozzáadása után jelöld be az **is secret** opciót, hogy a kulcs ne legyen látható.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.hu.png)

1. Kattints az **Add connection** gombra.

#### Prompt flow létrehozása

Hozzáadtál egy egyedi kapcsolatot az Azure AI Foundry-ban. Most hozzunk létre egy Prompt flow-t a következő lépésekkel. Ezután összekapcsolod ezt a Prompt flow-t az egyedi kapcsolattal, hogy a finomhangolt modellt használni tudd a Prompt flow-n belül.

1. Navigálj a létrehozott Azure AI Foundry projekthez.

1. Válaszd ki a bal oldali fülön a **Prompt flow** lehetőséget.

1. A navigációs menüből válaszd a **+ Create** opciót.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.hu.png)

1. A navigációs menüből válaszd a **Chat flow** lehetőséget.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.hu.png)

1. Írd be a használni kívánt **Folder name**-et.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.hu.png)

2. Kattints a **Create** gombra.

#### Prompt flow beállítása a finomhangolt Phi-3 modellel való csevegéshez

Integrálnod kell a finomhangolt Phi-3 modellt a Prompt flow-ba. Azonban a meglévő Prompt flow nem erre a célra készült, ezért újra kell tervezned a Prompt flow-t, hogy lehetővé tedd az egyedi modell integrációját.

1. A Prompt flow-ban végezd el a következő lépéseket az aktuális folyamat újraépítéséhez:

    - Válaszd a **Raw file mode**-ot.
    - Töröld az összes meglévő kódot a *flow.dag.yml* fájlból.
    - Illeszd be a következő kódot a *flow.dag.yml* fájlba.

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

    - Kattints a **Save** gombra.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.hu.png)

1. Illeszd be a következő kódot az *integrate_with_promptflow.py* fájlba, hogy a finomhangolt Phi-3 modellt használd a Prompt flow-ban.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.hu.png)

> [!NOTE]
> Részletesebb információkért az Azure AI Foundry-ban történő Prompt flow használatáról, tekintsd meg a [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) dokumentációt.

1. Engedélyezd a csevegést a **Chat input** és **Chat output** kiválasztásával.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.hu.png)

1. Most már készen állsz arra, hogy csevegj a finomhangolt Phi-3 modelleddel. A következő gyakorlatban megtanulod, hogyan indítsd el a Prompt flow-t, és hogyan használd a finomhangolt Phi-3 modelleddel való csevegéshez.

> [!NOTE]
>
> Az újraépített folyamatnak az alábbi képhez hasonlónak kell lennie:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.hu.png)
>

### Csevegés a saját Phi-3 modelleddel

Most, hogy finomhangoltad és integráltad a saját Phi-3 modelledet a Prompt flow-val, készen állsz a vele való interakcióra. Ez a gyakorlat végigvezet a beállítás és a csevegés elindításának folyamatán a modelleddel a Prompt flow segítségével. Ezeknek a lépéseknek a követésével teljes mértékben kihasználhatod a finomhangolt Phi-3 modell képességeit különféle feladatok és beszélgetések során.

- Csevegj a saját Phi-3 modelleddel a Prompt flow használatával.

#### Prompt flow indítása

1. Kattints a **Start compute sessions** gombra a Prompt flow elindításához.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.hu.png)

1. Válaszd a **Validate and parse input** lehetőséget a paraméterek frissítéséhez.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.hu.png)

1. Válaszd ki a **Value** mezőt a létrehozott egyedi kapcsolathoz. Például *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.hu.png)

#### Csevegés az egyedi modelleddel

1. Kattints a **Chat** gombra.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.hu.png)

1. Íme egy példa az eredményekre: Most már cseveghetsz a saját Phi-3 modelleddel. Ajánlott olyan kérdéseket feltenni, amelyek a finomhangoláshoz használt adatokon alapulnak.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.hu.png)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.