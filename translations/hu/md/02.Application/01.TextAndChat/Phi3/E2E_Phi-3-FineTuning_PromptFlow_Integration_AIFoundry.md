# Fine-tune és integrálja az egyedi Phi-3 modelleket a Prompt flow-val a Microsoft Foundry-ban

Ez az end-to-end (E2E) minta a Microsoft Tech Community "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" című útmutatóján alapul. Bemutatja az egyedi Phi-3 modellek finomhangolásának, telepítésének és integrálásának folyamatait a Prompt flow segítségével a Microsoft Foundry-ban.
Az E2E mintától eltérően, amelyben a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" című anyag helyi kód-futtatást tartalmazott, ez az oktatóanyag teljes egészében az Azure AI / ML Studio-n belüli modell finomhangolására és integrálására összpontosít.

## Áttekintés

Ebben az E2E mintában megtanulja, hogyan finomhangolja a Phi-3 modellt, és hogyan integrálja azt a Prompt flow-val a Microsoft Foundry-ban. Az Azure AI / ML Studio segítségével létrehoz egy munkafolyamatot az egyedi MI modellek telepítésére és használatára. Ez az E2E minta három forgatókönyvre van felosztva:

**1. forgatókönyv: Azure erőforrások beállítása és felkészülés a finomhangolásra**

**2. forgatókönyv: A Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban**

**3. forgatókönyv: Integráció a Prompt flow-val és beszélgetés az egyedi modellel a Microsoft Foundry-ban**

Íme az E2E minta áttekintése.

![Phi-3-FineTuning_PromptFlow_Integration Áttekintés.](../../../../../../translated_images/hu/00-01-architecture.198ba0f1ae6d841a.webp)

### Tartalomjegyzék

1. **[1. forgatókönyv: Azure erőforrások beállítása és felkészülés a finomhangolásra](#1-forgatókönyv-azure-erőforrások-beállítása-és-felkészülés-a-finomhangolásra)**
    - [Azure Machine Learning Workspace létrehozása](#azure-machine-learning-workspace-létrehozása)
    - [GPU kvóták igénylése az Azure-előfizetésben](#gpu-kvóták-igénylése-az-azure-előfizetésben)
    - [Szerepkör hozzárendelés hozzáadása](#szerepkör-hozzárendelés-hozzáadása)
    - [Projekt beállítása](#projekt-beállítása)
    - [Adatkészlet előkészítése a finomhangoláshoz](#adatkészlet-előkészítése-a-finomhangoláshoz)

1. **[2. forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban](#2-forgatókönyv-phi-3-modell-finomhangolása-és-telepítése-az-azure-machine-learning-studio-ban)**
    - [Phi-3 modell finomhangolása](#a-phi-3-modell-finomhangolása)
    - [Finomhangolt Phi-3 modell telepítése](#a-finomhangolt-phi-3-modell-telepítése)

1. **[3. forgatókönyv: Integráció a Prompt flow-val és beszélgetés az egyedi modellel a Microsoft Foundry-ban](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Az egyedi Phi-3 modell integrálása a Prompt flow-val](#egyedi-phi-3-modell-integrálása-a-prompt-flow-val)
    - [Beszélgetés az egyedi Phi-3 modellel](#beszélgetés-az-egyéni-phi-3-modellel)

## 1. forgatókönyv: Azure erőforrások beállítása és felkészülés a finomhangolásra

### Azure Machine Learning Workspace létrehozása

1. Írja be az *azure machine learning* kifejezést a portál oldalán felül található **keresőmezőbe**, és válassza ki az megjelenő lehetőségek közül az **Azure Machine Learning**-et.

    ![Írja be az azure machine learning kifejezést.](../../../../../../translated_images/hu/01-01-type-azml.acae6c5455e67b4b.webp)

2. Válassza a navigációs menüből a **+ Létrehozás** lehetőséget.

3. Válassza a navigációs menüből az **Új munkaterület** lehetőséget.

    ![Válassza az új munkaterületet.](../../../../../../translated_images/hu/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Végezze el az alábbi feladatokat:

    - Válassza ki az Azure **Előfizetését**.
    - Válassza ki a használni kívánt **Erőforráscsoportot** (ha szükséges, hozzon létre újat).
    - Adja meg a **Munkaterület nevét**. Ez egyedi érték kell legyen.
    - Válassza ki a használni kívánt **Régiót**.
    - Válassza ki a használni kívánt **Tárolófiókot** (ha szükséges, hozzon létre újat).
    - Válassza ki a használni kívánt **Kulcstárolót** (ha szükséges, hozzon létre újat).
    - Válassza ki a használni kívánt **Application Insights** szolgáltatást (ha szükséges, hozzon létre újat).
    - Válassza ki a használni kívánt **Tárolóregisztert** (ha szükséges, hozzon létre újat).

    ![Töltse ki az azure machine learning adatokat.](../../../../../../translated_images/hu/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Válassza a **Áttekintés + létrehozás** lehetőséget.

6. Válassza a **Létrehozás** lehetőséget.

### GPU kvóták igénylése az Azure-előfizetésben

Ebben az oktatóanyagban megtanulja, hogyan finomhangolja és telepítse a Phi-3 modellt GPU-k használatával. A finomhangoláshoz a *Standard_NC24ads_A100_v4* GPU-t fogja használni, amelyhez kvótaigénylés szükséges. A telepítéshez a *Standard_NC6s_v3* GPU-t használja, amely szintén kvótaigénylést igényel.

> [!NOTE]
>
> Csak a Pay-As-You-Go előfizetések (azaz az alapértelmezett előfizetés típus) jogosultak GPU-kiosztásra; a kedvezményes előfizetések jelenleg nem támogatottak.
>

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Végezze el a következő feladatokat a *Standard NCADSA100v4 Family* kvóta igényléséhez:

    - Válassza a bal oldali fülnél a **Kvóta** menüt.
    - Válassza ki a használni kívánt **Virtuális gép családot**. Például válassza a **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** opciót, amely tartalmazza a *Standard_NC24ads_A100_v4* GPU-t.
    - Válassza a navigációs menüből a **Kvóta igénylése** lehetőséget.

        ![Kvóta igénylés.](../../../../../../translated_images/hu/02-02-request-quota.c0428239a63ffdd5.webp)

    - A Kvóta igénylés oldalán adja meg az új **magkorlátot** (New cores limit) számértékként, például 24-et.
    - A Kvóta igénylés oldalán válassza a **Beküldés** gombot a GPU kvóta kéréséhez.

1. Végezze el a következő feladatokat a *Standard NCSv3 Family* kvóta igényléséhez:

    - Válassza a bal oldali fülnél a **Kvóta** menüt.
    - Válassza ki a használni kívánt **Virtuális gép családot**. Például válassza a **Standard NCSv3 Family Cluster Dedicated vCPUs** opciót, amely tartalmazza a *Standard_NC6s_v3* GPU-t.
    - Válassza a navigációs menüből a **Kvóta igénylése** lehetőséget.
    - A Kvóta igénylés oldalán adja meg az új **magkorlátot** (New cores limit) számértékként, például 24-et.
    - A Kvóta igénylés oldalán válassza a **Beküldés** gombot a GPU kvóta kéréséhez.

### Szerepkör hozzárendelés hozzáadása

A modellek finomhangolásához és telepítéséhez először létre kell hozni egy felhasználó által hozzárendelt kezelt identitást (UAI), és hozzá kell rendelni a megfelelő engedélyeket. Ezt az UAI-t a hitelesítéshez használja majd telepítés közben.

#### Felhasználó által hozzárendelt kezelt identitás létrehozása (UAI)

1. Írja be a *managed identities* kifejezést a portál tetején található **keresőmezőbe**, és válassza a megjelenő lehetőségek közül a **Managed Identities** elemet.

    ![Írja be a managed identities kifejezést.](../../../../../../translated_images/hu/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Válassza a **+ Létrehozás** lehetőséget.

    ![Válassza a létrehozás gombot.](../../../../../../translated_images/hu/03-02-select-create.92bf8989a5cd98f2.webp)

1. Végezze el a következő beállításokat:

    - Válassza ki az Azure **Előfizetését**.
    - Válassza ki a használni kívánt **Erőforráscsoportot** (ha kell, hozzon létre újat).
    - Válassza ki a használni kívánt **Régiót**.
    - Adja meg az **Nevet**. Ez egyedi érték kell, hogy legyen.

    ![Válassza a létrehozás gombot.](../../../../../../translated_images/hu/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Válassza az **Áttekintés + létrehozás** lehetőséget.

1. Válassza a **+ Létrehozás** gombot.

#### Hozzárendeljen Contributor szerepkört a Managed Identity-hez

1. Navigáljon a korábban létrehozott Managed Identity erőforráshoz.

1. Válassza a bal oldali fülön az **Azure szerepkör hozzárendelések** lehetőséget.

1. Válassza a navigációs menüből a **+ Szerepkör hozzárendelés hozzáadása** lehetőséget.

1. Az Szerepkör hozzárendelés hozzáadása oldalon végezze el a következő lépéseket:
    - Állítsa a **Hatókört** **Erőforráscsoport**-ra.
    - Válassza ki az Azure **Előfizetését**.
    - Válassza ki a használni kívánt **Erőforráscsoportot**.
    - Állítsa a **Szerepkört** **Contributor**-ra.

    ![Töltse ki a contributor szerepkört.](../../../../../../translated_images/hu/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Válassza a **Mentés** gombot.

#### Hozzárendeljen Storage Blob Data Reader szerepkört a Managed Identity-hez

1. Írja be a *storage accounts* kifejezést a portál tetején található **keresőmezőbe**, és válassza az megjelenő opciók közül a **Storage accounts** lehetőséget.

    ![Írja be a storage accounts szót.](../../../../../../translated_images/hu/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Válassza ki azt a tárolófiókot, amely az Azure Machine Learning munkaterülethez kapcsolódik, amelyet létrehozott. Például *finetunephistorage*.

1. Végezze el a következő lépéseket az Szerepkör hozzárendelés hozzáadása oldal eléréséhez:

    - Navigáljon az Azure Storage-fiókhoz, amelyet létrehozott.
    - A bal oldali fülön válassza az **Hozzáférés-vezérlés (IAM)** menüpontot.
    - A navigációs menüből válassza a **+ Hozzáadás** lehetőséget.
    - Válassza az **Szerepkör hozzárendelés hozzáadása** lehetőséget.

    ![Szerepkör hozzáadás.](../../../../../../translated_images/hu/03-06-add-role.353ccbfdcf0789c2.webp)

1. Az Szerepkör hozzárendelés hozzáadása oldalon végezze el a következőket:

    - A Szerepkör oldalon írja be a **search bar**-ba a *Storage Blob Data Reader* kifejezést, majd válassza ki a megjelenő lehetőségek közül a **Storage Blob Data Reader**-t.
    - A Szerepkör oldalon válassza a **Tovább** lehetőséget.
    - A Tagok oldalon állítsa be az **Hozzáférés hozzárendelése** lehetőséget **Kezelt identitás**-ra.
    - A Tagok oldalon válassza a **+ Tagok kiválasztása** lehetőséget.
    - A Kezelt identitások kiválasztása oldalon válassza ki az Azure **Előfizetését**.
    - A Kezelt identitások kiválasztása oldalon válassza ki a **Kezelt identitást** (Manage Identity).
    - A Kezelt identitások kiválasztása oldalon válassza ki a korábban létrehozott Kezelt identitást, például *finetunephi-managedidentity*.
    - A Kezelt identitások kiválasztása oldalon nyomja meg a **Kiválasztás** gombot.

    ![Kezelt identitás kiválasztása.](../../../../../../translated_images/hu/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Válassza a **Áttekintés + hozzárendelés** lehetőséget.

#### Hozzárendeljen AcrPull szerepkört a Managed Identity-hez

1. Írja be a *container registries* kifejezést a portál tetején található **keresőmezőbe**, és válassza ki a megjelenő opciók közül a **Container registries**-t.

    ![Írja be a container registries kifejezést.](../../../../../../translated_images/hu/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Válassza ki azt a tárolóregisztert, amely az Azure Machine Learning munkaterülethez kapcsolódik. Például *finetunephicontainerregistry*.

1. Végezze el a következő lépéseket az Szerepkör hozzárendelés hozzáadása oldal eléréséhez:

    - Válassza a bal oldali fülön az **Hozzáférés-vezérlés (IAM)** menüpontot.
    - A navigációs menüből válassza a **+ Hozzáadás** lehetőséget.
    - Válassza az **Szerepkör hozzárendelés hozzáadása** lehetőséget.

1. Az Szerepkör hozzárendelés hozzáadása oldalon végezze el a következőket:

    - A Szerepkör oldalon írja be a *AcrPull* kifejezést a **keresőmezőbe**, majd válassza ki a megjelenő lehetőségek közül az **AcrPull**-t.
    - A Szerepkör oldalon válassza a **Tovább** lehetőséget.
    - A Tagok oldalon állítsa be az **Hozzáférés hozzárendelése** értéket **Kezelt identitás**-ra.
    - A Tagok oldalon válassza a **+ Tagok kiválasztása** lehetőséget.
    - A Kezelt identitások kiválasztása oldalon válassza ki az Azure **Előfizetését**.
    - A Kezelt identitások kiválasztása oldalon válassza ki a **Kezelt identitást** (Manage Identity).
    - A Kezelt identitások kiválasztása oldalon válassza ki a létrehozott Kezelt identitást, például *finetunephi-managedidentity*.
    - A Kezelt identitások kiválasztása oldalon válassza a **Kiválasztás** gombot.
    - Válassza az **Áttekintés + hozzárendelés** lehetőséget.

### Projekt beállítása

Az adatkészletek letöltéséhez, amelyek szükségesek a finomhangoláshoz, helyi környezetet fog beállítani.

Ebben a gyakorlatban a következőket teszi:

- Létrehoz egy mappát, amelyben dolgozhat.
- Létrehoz egy virtuális környezetet.
- Telepíti a szükséges csomagokat.
- Létrehoz egy *download_dataset.py* fájlt az adatkészlet letöltéséhez.

#### Hozzon létre egy mappát, amelyben dolgozhat

1. Nyisson meg egy terminálablakot, és írja be a következő parancsot, amellyel létrehoz egy *finetune-phi* nevű mappát az alapértelmezett helyen.

    ```console
    mkdir finetune-phi
    ```

2. Írja be a következő parancsot a terminálban, hogy átlépjen a létrehozott *finetune-phi* mappába.

    ```console
    cd finetune-phi
    ```

#### Virtuális környezet létrehozása

1. Írja be a következő parancsot a terminálban egy *.venv* nevű virtuális környezet létrehozásához.
    ```console
    python -m venv .venv
    ```

2. Írja be a következő parancsot a termináljába a virtuális környezet aktiválásához.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ha sikerült, a parancssor előtt meg kell jelennie a *(.venv)* jelzésnek.

#### Szükséges csomagok telepítése

1. Írja be a következő parancsokat a termináljába a szükséges csomagok telepítéséhez.

    ```console
    pip install datasets==2.19.1
    ```

#### Készítse el a `donload_dataset.py` fájlt

> [!NOTE]
> Teljes mappastruktúra:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Nyissa meg a **Visual Studio Code**-ot.

1. Válassza ki a menüsorból a **File** menüpontot.

1. Válassza az **Open Folder** lehetőséget.

1. Válassza ki a *finetune-phi* mappát, amelyet létrehozott, és amely a *C:\Users\yourUserName\finetune-phi* helyen található.

    ![Válassza ki a létrehozott mappát.](../../../../../../translated_images/hu/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. A Visual Studio Code bal oldali paneljén kattintson jobb gombbal, és válassza az **New File** lehetőséget egy új fájl létrehozásához, amelynek neve *download_dataset.py* lesz.

    ![Új fájl létrehozása.](../../../../../../translated_images/hu/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Adatkészlet előkészítése a finomhangoláshoz

Ebben a feladatban a *download_dataset.py* fájlt futtatja, hogy letöltse az *ultrachat_200k* adatkészleteket a helyi környezetébe. Ezután ezeket az adatokat fogja használni a Phi-3 modell finomhangolásához az Azure Machine Learning szolgáltatásban.

Ebben a gyakorlatban:

- Kódot ad a *download_dataset.py* fájlhoz az adatkészletek letöltéséhez.
- Futtatja a *download_dataset.py* fájlt az adatkészletek helyi környezetbe történő letöltéséhez.

#### Adatkészlet letöltése a *download_dataset.py* segítségével

1. Nyissa meg a *download_dataset.py* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot a *download_dataset.py* fájlba.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Töltse be az adatkészletet a megadott névvel, konfigurációval és felosztási aránnyal
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Ossza fel az adatkészletet tanuló és teszt készletekre (80% tanuló, 20% teszt)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Hozza létre a könyvtárat, ha az nem létezik
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Nyissa meg a fájlt írási módban
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iteráljon végig az adatkészlet minden rekordján
            for record in dataset:
                # Mentse a rekordot JSON objektumként, és írja a fájlba
                json.dump(record, f)
                # Írjon új sor karaktert a rekordok elválasztására
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Töltse be és ossza fel az ULTRACHAT_200k adatkészletet egy adott konfigurációval és felosztási aránnyal
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Kinyeri a tanuló és teszt adatokat a felosztásból
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Mentse el a tanuló adatokat JSONL fájlba
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Mentse el a teszt adatokat egy külön JSONL fájlba
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Írja be a következő parancsot a termináljában a szkript futtatásához és az adatok helyi környezetbe történő letöltéséhez.

    ```console
    python download_dataset.py
    ```

1. Ellenőrizze, hogy az adatkészletek sikeresen elmentésre kerültek-e a helyi *finetune-phi/data* könyvtárba.

> [!NOTE]
>
> #### Megjegyzés az adatkészlet méretéről és a finomhangolás idejéről
>
> Ebben az oktatóanyagban csak az adatkészlet 1%-át használja (`split='train[:1%]'`). Ez jelentősen csökkenti az adatmennyiséget, gyorsítva ezzel a feltöltést és a finomhangolást. Az arányt módosíthatja, hogy megtalálja az edzésidő és a modell teljesítménye közötti megfelelő egyensúlyt. Az adatkészlet kisebb részhalmazának használata lerövidíti a finomhangoláshoz szükséges időt, így az folyamat kezelhetőbb egy oktatóanyag számára.

## 2. Forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studio-ban

### A Phi-3 modell finomhangolása

Ebben a gyakorlatban a Phi-3 modellt finomhangolja az Azure Machine Learning Studio-ban.

Ebben a gyakorlatban:

- Létrehoz számítógép klasztert a finomhangoláshoz.
- Finomhangolja a Phi-3 modellt az Azure Machine Learning Studio-ban.

#### Számítógép klaszter létrehozása finomhangoláshoz

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válassza a bal oldali fülön a **Compute** menüpontot.

1. Válassza a navigációs menüből a **Compute clusters** lehetőséget.

1. Kattintson a **+ New** gombra.

    ![Számítástechnikai erőforrás kiválasztása.](../../../../../../translated_images/hu/06-01-select-compute.a29cff290b480252.webp)

1. Végezze el a következő beállításokat:

    - Válassza ki a használni kívánt **Régiót**.
    - Válassza a **Dedicated** opciót a **Virtual machine tier**-nél.
    - Válassza a **GPU** opciót a **Virtual machine type**-nél.
    - A **Virtual machine size** szűrőnél válassza a **Select from all options** lehetőséget.
    - Válassza a **Standard_NC24ads_A100_v4** méretet a virtuális géphez.

    ![Klaszter létrehozása.](../../../../../../translated_images/hu/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Kattintson a **Next** gombra.

1. Végezze el a következő beállításokat:

    - Adjon meg egy egyedi nevet a **Compute name** mezőben.
    - Állítsa a **Minimum number of nodes** értékét **0**-ra.
    - Állítsa a **Maximum number of nodes** értékét **1**-re.
    - Állítsa az **Idle seconds before scale down** értékét **120** másodpercre.

    ![Klaszter létrehozása.](../../../../../../translated_images/hu/06-03-create-cluster.4a54ba20914f3662.webp)

1. Kattintson a **Create** gombra.

#### A Phi-3 modell finomhangolása

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válassza ki az Azure Machine Learning munkaterületet, amelyet létrehozott.

    ![Válassza ki a létrehozott munkaterületet.](../../../../../../translated_images/hu/06-04-select-workspace.a92934ac04f4f181.webp)

1. Végezze el a következő lépéseket:

    - Válassza a bal oldali menüben a **Model catalog** lehetőséget.
    - Írja be a keresősávba a *phi-3-mini-4k* kifejezést, és az előugró lehetőségek közül válassza a **Phi-3-mini-4k-instruct** elemet.

    ![Írja be a phi-3-mini-4k-t.](../../../../../../translated_images/hu/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Válassza ki a navigációs menüből a **Fine-tune** lehetőséget.

    ![Válassza a finomhangolást.](../../../../../../translated_images/hu/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Végezze el a következőket:

    - Állítsa a **Select task type** értékét **Chat completion**-re.
    - Válassza a **+ Select data** lehetőséget és töltse fel az **Edzésadatokat** (Training data).
    - A validációs adat feltöltése beállításnál válassza a **Provide different validation data** lehetőséget.
    - Válassza a **+ Select data** lehetőséget, hogy feltöltse a **Validációs adatokat**.

    ![Töltse ki a finomhangolási oldalt.](../../../../../../translated_images/hu/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Az **Advanced settings** (Speciális beállítások) menüpontban testre szabhatja például a **learning_rate** vagy a **lr_scheduler_type** konfigurációkat, hogy a finomhangolási folyamatot az igényeihez igazítsa.

1. Válassza a **Finish** gombot.

1. Ebben a gyakorlatban sikeresen finomhangolta a Phi-3 modellt az Azure Machine Learning segítségével. Felhívjuk a figyelmét, hogy a finomhangolási folyamat akár jelentős időt is igénybe vehet. A finomhangolási feladat elindítása után várnia kell a befejezésére. A finomhangolási munka állapotát az Azure Machine Learning munkaterület bal oldali menüjében található Jobs fül alatt követheti nyomon. A következő sorozatban a finomhangolt modellt telepíti és integrálja a Prompt flow-val.

    ![Megtekintés finomhangolási munkáról.](../../../../../../translated_images/hu/06-08-output.2bd32e59930672b1.webp)

### A finomhangolt Phi-3 modell telepítése

Ahhoz, hogy a finomhangolt Phi-3 modellt integrálni tudja a Prompt flow-val, telepítenie kell a modellt, hogy valós idejű lekérdezések számára elérhető legyen. Ez magában foglalja a modell regisztrálását, egy online végpont létrehozását és a modell telepítését.

Ebben a lépésben:

- Regisztrálja a finomhangolt modellt az Azure Machine Learning munkaterületen.
- Létrehoz egy online végpontot.
- Telepíti a regisztrált finomhangolt Phi-3 modellt.

#### A finomhangolt modell regisztrálása

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válassza ki az általad létrehozott Azure Machine Learning munkaterületet.

    ![Válassza ki a létrehozott munkaterületet.](../../../../../../translated_images/hu/06-04-select-workspace.a92934ac04f4f181.webp)

1. Válassza a bal oldali fülön a **Models** menüpontot.
1. Kattintson a **+ Register** gombra.
1. Válassza a **From a job output** opciót.

    ![Modell regisztrálása.](../../../../../../translated_images/hu/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Válassza ki a létrehozott munkaelemet.

    ![Munka kijelölése.](../../../../../../translated_images/hu/07-02-select-job.3e2e1144cd6cd093.webp)

1. Kattintson a **Next** gombra.

1. Állítsa be a **Model type** értékét **MLflow**-ra.

1. Győződjön meg arról, hogy a **Job output** van kiválasztva; az automatikusan ki kell legyen választva.

    ![Kimenet kiválasztása.](../../../../../../translated_images/hu/07-03-select-output.4cf1a0e645baea1f.webp)

2. Kattintson a **Next** gombra.

3. Kattintson a **Register** gombra.

    ![Kattintson a regisztrációra.](../../../../../../translated_images/hu/07-04-register.fd82a3b293060bc7.webp)

4. A regisztrált modellt megtekintheti a bal oldali menü **Models** pontjára navigálva.

    ![Regisztrált modell.](../../../../../../translated_images/hu/07-05-registered-model.7db9775f58dfd591.webp)

#### A finomhangolt modell telepítése

1. Navigáljon az által létrehozott Azure Machine Learning munkaterületre.

1. Válassza az oldalsávban az **Endpoints** menüt.

1. A navigációs menüben válassza a **Real-time endpoints** lehetőséget.

    ![Végpont létrehozása.](../../../../../../translated_images/hu/07-06-create-endpoint.1ba865c606551f09.webp)

1. Kattintson a **Create** gombra.

1. Válassza ki a korábban regisztrált modellt.

    ![Válassza ki a regisztrált modellt.](../../../../../../translated_images/hu/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Kattintson a **Select** gombra.

1. Végezze el a következő beállításokat:

    - Válassza ki a **Virtual machine** opciót *Standard_NC6s_v3*-ra.
    - Állítsa be a használni kívánt **Instance count**-ot, például *1*.
    - Az **Endpoint** beállításnál válassza az **New** opciót, hogy új végpontot hozzon létre.
    - Adjon meg egy egyedi nevet az **Endpoint name** mezőben.
    - Adjon meg egy egyedi nevet a **Deployment name** mezőben.

    ![Telepítési beállítások kitöltése.](../../../../../../translated_images/hu/07-08-deployment-setting.43ddc4209e673784.webp)

1. Kattintson a **Deploy** gombra.

> [!WARNING]
> A további költségek elkerülése érdekében győződjön meg arról, hogy törölte a létrehozott végpontot az Azure Machine Learning munkaterületen.
>

#### Telepítés állapotának ellenőrzése az Azure Machine Learning munkaterületen

1. Navigáljon az általa létrehozott Azure Machine Learning munkaterületre.

1. Válassza az **Endpoints** pontot a bal oldali fülön.

1. Válassza ki a létrehozott végpontot.

    ![Válassza az endpoinokat](../../../../../../translated_images/hu/07-09-check-deployment.325d18cae8475ef4.webp)

1. Ezen az oldalon menedzselheti a végpontokat a telepítés folyamata alatt.

> [!NOTE]
> Ha a telepítés befejeződött, győződjön meg róla, hogy a **Live traffic** értéke **100%**-ra van állítva. Ha nem, válassza az **Update traffic** lehetőséget a forgalmi beállítások módosításához. Megjegyzés: a modellt nem lehet tesztelni, ha a forgalom 0%-ra van állítva.
>
> ![Forgalom beállítása.](../../../../../../translated_images/hu/07-10-set-traffic.085b847e5751ff3d.webp)
>

## 3. Forgatókönyv: Integráció a Prompt flow-val és csevegés az egyedi modellel a Microsoft Foundry-ban

### Egyedi Phi-3 modell integrálása a Prompt flow-val

Miután sikeresen telepítette a finomhangolt modellt, integrálhatja azt a Prompt Flow-val, hogy valós idejű alkalmazásokban használhassa, interaktív feladatokat végezve az egyedi Phi-3 modellel.

Ebben a gyakorlatban:

- Létrehozza a Microsoft Foundry Hub-ot.
- Létrehozza a Microsoft Foundry projektet.
- Létrehozza a Prompt flow-t.
- Hozzáad egy egyedi kapcsolatot a finomhangolt Phi-3 modellhez.
- Beállítja a Prompt flow-t, hogy csevegni tudjon az egyedi Phi-3 modellel.

> [!NOTE]
> A Promptflow Azure ML Studioval is integrálható. Ugyanaz a folyamat alkalmazható az Azure ML Studióra is.

#### Microsoft Foundry Hub létrehozása

A projekt létrehozása előtt létre kell hoznia egy Hub-ot. A Hub olyan, mint egy erőforrás csoport, amely lehetővé teszi több projekt kezelését és szervezését a Microsoft Foundry-ban.
1. Látogasson el a [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Válassza ki a bal oldali fülön az **All hubs** lehetőséget.

1. Válassza a navigációs menüből a **+ New hub** opciót.

    ![Create hub.](../../../../../../translated_images/hu/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Végezze el a következő feladatokat:

    - Írja be a **Hub name** mezőt. Egyedi értéknek kell lennie.
    - Válassza ki Azure **Előfizetését**.
    - Válassza ki a használni kívánt **Erőforráscsoportot** (szükség esetén hozzon létre újat).
    - Válassza ki a használni kívánt **Helyet**.
    - Válassza ki a használni kívánt **Kapcsolódó Azure AI szolgáltatásokat** (szükség esetén hozzon létre újat).
    - Válassza a **Kapcsolódás Azure AI Kereséshez** lehetőségnél a **Kapcsolódás kihagyása** opciót.

    ![Fill hub.](../../../../../../translated_images/hu/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Válassza a **Next** lehetőséget.

#### Microsoft Foundry projekt létrehozása

1. A létrehozott Hub-ban válassza a bal oldali fülön az **All projects** opciót.

1. Válassza a navigációs menüből a **+ New project** lehetőséget.

    ![Select new project.](../../../../../../translated_images/hu/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Írja be a **Projekt nevét**. Egyedi értéknek kell lennie.

    ![Create project.](../../../../../../translated_images/hu/08-05-create-project.4d97f0372f03375a.webp)

1. Válassza a **Create a project** lehetőséget.

#### Egyéni kapcsolat hozzáadása a finomhangolt Phi-3 modellhez

Ahhoz, hogy az egyéni Phi-3 modellt integrálja a Prompt flow-hoz, mentenie kell a modell végpontját és kulcsát egy egyéni kapcsolatként. Ez a beállítás biztosítja az elérést az egyéni Phi-3 modellhez a Prompt flow-ban.

#### Állítsa be a finomhangolt Phi-3 modell api kulcsát és végpont URI-ját

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Navigáljon a létrehozott Azure Machine learning munkaterületre.

1. Válassza a bal oldali fülön az **Endpoints** lehetőséget.

    ![Select endpoints.](../../../../../../translated_images/hu/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Válassza ki a létrehozott végpontot.

    ![Select endpoints.](../../../../../../translated_images/hu/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Válassza a navigációs menüből a **Consume** opciót.

1. Másolja ki a **REST endpoint** és a **Primary key** értékeit.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/hu/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Egyéni kapcsolatok hozzáadása

1. Látogasson el a [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Navigáljon a létrehozott Microsoft Foundry projekthez.

1. A létrehozott Projektben válassza a bal oldali fülön a **Settings** lehetőséget.

1. Válassza a **+ New connection** opciót.

    ![Select new connection.](../../../../../../translated_images/hu/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Válassza a navigációs menüből a **Custom keys** lehetőséget.

    ![Select custom keys.](../../../../../../translated_images/hu/08-10-select-custom-keys.856f6b2966460551.webp)

1. Végezze el a következő feladatokat:

    - Válassza a **+ Add key value pairs** lehetőséget.
    - A kulcs névhez írja be, hogy **endpoint** és illessze be az Azure ML Studioból másolt végpontot az érték mezőbe.
    - Újra válassza a **+ Add key value pairs** lehetőséget.
    - A kulcs névhez írja be, hogy **key** és illessze be az Azure ML Studioból másolt kulcsot az érték mezőbe.
    - A kulcsok hozzáadása után válassza az **is secret** opciót, hogy a kulcs ne legyen látható.

    ![Add connection.](../../../../../../translated_images/hu/08-11-add-connection.785486badb4d2d26.webp)

1. Válassza az **Add connection** lehetőséget.

#### Prompt flow létrehozása

Hozzáadott egy egyéni kapcsolatot a Microsoft Foundry-ban. Most hozzunk létre egy Prompt flow-t az alábbi lépések szerint. Ezután a Prompt flow-t csatlakoztatni fogja az egyéni kapcsolathoz, így használhatja a finomhangolt modellt a Prompt flow-on belül.

1. Navigáljon a létrehozott Microsoft Foundry projekthez.

1. Válassza a bal oldali fülön a **Prompt flow** lehetőséget.

1. Válassza a navigációs menüből a **+ Create** opciót.

    ![Select Promptflow.](../../../../../../translated_images/hu/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Válassza a navigációs menüből a **Chat flow** lehetőséget.

    ![Select chat flow.](../../../../../../translated_images/hu/08-13-select-flow-type.2ec689b22da32591.webp)

1. Írja be a használni kívánt **Mappa nevét**.

    ![Enter name.](../../../../../../translated_images/hu/08-14-enter-name.ff9520fefd89f40d.webp)

2. Válassza a **Create** lehetőséget.

#### Állítsa be a Prompt flow-t, hogy csevegjen az egyéni Phi-3 modellel

Integrálni kell a finomhangolt Phi-3 modellt a Prompt flow-ba. Azonban a meglévő Prompt flow nem erre a célra készült. Ezért át kell terveznie a Prompt flow-t, hogy lehetővé tegye az egyéni modell integrációját.

1. A Prompt flow-ban végezze el a következő feladatokat a meglévő folyamat átalakításához:

    - Válassza a **Raw file mode** opciót.
    - Törölje az összes meglévő kódot a *flow.dag.yml* fájlból.
    - Adja hozzá az alábbi kódot a *flow.dag.yml* fájlhoz.

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

    - Válassza a **Save** lehetőséget.

    ![Select raw file mode.](../../../../../../translated_images/hu/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Illessze be az alábbi kódot az *integrate_with_promptflow.py* fájlba, hogy használhassa az egyéni Phi-3 modellt a Prompt flow-ban.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Naplóbeállítás
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

        # A "connection" a Egyedi Kapcsolat neve, az "endpoint", "key" kulcsok az Egyedi Kapcsolatban
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
            
            # Naplózza a teljes JSON választ
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

    ![Paste prompt flow code.](../../../../../../translated_images/hu/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> További részletes információkért a Prompt flow használatáról a Microsoft Foundry-ban tekintse meg a [Prompt flow a Microsoft Foundry-ban](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) dokumentációt.

1. Válassza a **Chat input**, **Chat output** opciókat, hogy engedélyezze a csevegést a modelljével.

    ![Input Output.](../../../../../../translated_images/hu/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Most készen áll arra, hogy csevegjünk az egyéni Phi-3 modellel. A következő gyakorlatban megtanulja, hogyan indítsa el a Prompt flow-t és hogyan használja az finomhangolt Phi-3 modellel való csevegéshez.

> [!NOTE]
>
> Az átalakított folyamatnak az alábbi képhez hasonlónak kell lennie:
>
> ![Flow example.](../../../../../../translated_images/hu/08-18-graph-example.d6457533952e690c.webp)
>

### Beszélgetés az egyéni Phi-3 modellel

Most, hogy finomhangolta és integrálta az egyéni Phi-3 modellt a Prompt flow-val, készen áll arra, hogy elkezdjen vele interakcióba lépni. Ez a gyakorlat végigvezeti Önt azon, hogyan állítsa be és indítson el egy beszélgetést a modelljével a Prompt flow segítségével. Ezeknek a lépéseknek a követésével teljes mértékben ki tudja használni a finomhangolt Phi-3 modell képességeit különféle feladatok és beszélgetések során.

- Beszélgessen az egyéni Phi-3 modelljével a Prompt flow segítségével.

#### Prompt flow elindítása

1. Válassza a **Start compute sessions** lehetőséget a Prompt flow indításához.

    ![Start compute session.](../../../../../../translated_images/hu/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Válassza a **Validate and parse input** lehetőséget a paraméterek megújításához.

    ![Validate input.](../../../../../../translated_images/hu/09-02-validate-input.317c76ef766361e9.webp)

1. Válassza ki a **Value** mezőt a létrehozott egyéni kapcsolat nevével. Például: *connection*.

    ![Connection.](../../../../../../translated_images/hu/09-03-select-connection.99bdddb4b1844023.webp)

#### Beszélgetés az egyéni modellel

1. Válassza a **Chat** lehetőséget.

    ![Select chat.](../../../../../../translated_images/hu/09-04-select-chat.61936dce6612a1e6.webp)

1. Íme egy példa az eredményekre: most már tud csevegni az egyéni Phi-3 modellel. Ajánlott olyan kérdéseket feltenni, amelyek a finomhangoláshoz használt adatokon alapulnak.

    ![Chat with prompt flow.](../../../../../../translated_images/hu/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->