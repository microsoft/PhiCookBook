<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:45:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "hu"
}
-->
# Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val

Ez az end-to-end (E2E) minta a Microsoft Tech Community "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" útmutatóján alapul. Bemutatja az egyedi Phi-3 modellek finomhangolásának, telepítésének és Prompt flow-val való integrálásának lépéseit.

## Áttekintés

Ebben az E2E mintában megtanulhatod, hogyan finomhangold a Phi-3 modellt, és hogyan integráld azt a Prompt flow-val. Az Azure Machine Learning és a Prompt flow segítségével felállíthatsz egy munkafolyamatot az egyedi MI modellek telepítéséhez és használatához. Ez az E2E minta három forgatókönyvre van bontva:

**1. Forgatókönyv: Azure erőforrások beállítása és előkészítés a finomhangoláshoz**

**2. Forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban**

**3. Forgatókönyv: Integráció Prompt flow-val és csevegés az egyedi modellel**

Íme az E2E minta áttekintése.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.hu.png)

### Tartalomjegyzék

1. **[1. Forgatókönyv: Azure erőforrások beállítása és előkészítés a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace létrehozása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvóták igénylése az Azure előfizetésben](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Szerepkör hozzárendelés hozzáadása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt beállítása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adathalmaz előkészítése a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[2. Forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI beállítása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 modell finomhangolása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Finomhangolt modell telepítése](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[3. Forgatókönyv: Integráció Prompt flow-val és csevegés az egyedi modellel](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Egyedi Phi-3 modell integrálása Prompt flow-val](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Csevegés az egyedi modellel](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 1. Forgatókönyv: Azure erőforrások beállítása és előkészítés a finomhangoláshoz

### Azure Machine Learning Workspace létrehozása

1. Írd be az *azure machine learning* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki az **Azure Machine Learning** opciót.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.hu.png)

1. Válaszd a navigációs menüből a **+ Create** lehetőséget.

1. Válaszd a navigációs menüből az **Új munkaterület** opciót.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.hu.png)

1. Végezd el a következő beállításokat:

    - Válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot** (ha szükséges, hozz létre újat).
    - Írd be a **Munkaterület nevét**. Ez egyedi érték kell legyen.
    - Válaszd ki a kívánt **Régiót**.
    - Válaszd ki a használni kívánt **Tárolófiókot** (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Kulcstárat** (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Application Insights**-t (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Konténerregisztert** (ha szükséges, hozz létre újat).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.hu.png)

1. Válaszd a **Review + Create** lehetőséget.

1. Válaszd a **Create** gombot.

### GPU kvóták igénylése az Azure előfizetésben

Ebben az E2E mintában a finomhangoláshoz a *Standard_NC24ads_A100_v4 GPU*-t fogod használni, ami kvótaigényt támaszt, míg a telepítéshez a *Standard_E4s_v3* CPU-t, amihez nem szükséges kvótaigénylés.

> [!NOTE]
>
> Csak a Pay-As-You-Go típusú előfizetések jogosultak GPU-kiosztásra; az előnyös előfizetések jelenleg nem támogatottak.
>
> Azok számára, akik előnyös előfizetést használnak (például Visual Studio Enterprise Subscription), vagy gyorsan szeretnék kipróbálni a finomhangolást és telepítést, ez az útmutató útmutatást ad egy minimális adathalmazzal CPU-n történő finomhangoláshoz is. Fontos azonban megjegyezni, hogy a finomhangolás eredményei jelentősen jobbak, ha GPU-t használsz nagyobb adathalmazzal.

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. A *Standard NCADSA100v4 Family* kvóta igényléséhez végezd el a következő lépéseket:

    - Válaszd a bal oldali menüben a **Quota** lehetőséget.
    - Válaszd ki a használni kívánt **Virtuális gép családot**. Például a **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**-t, amely tartalmazza a *Standard_NC24ads_A100_v4* GPU-t.
    - Válaszd a navigációs menüből a **Request quota** opciót.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.hu.png)

    - A Request quota oldalon add meg a kívánt **Új magkorlátot** (pl. 24).
    - Válaszd a **Submit** gombot a GPU kvóta igényléséhez.

> [!NOTE]
> Szükség szerint a megfelelő GPU vagy CPU kiválasztásához tekintsd meg a [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) dokumentációt.

### Szerepkör hozzárendelés hozzáadása

A modellek finomhangolásához és telepítéséhez először létre kell hoznod egy User Assigned Managed Identity-t (UAI), és megfelelő jogosultságokat kell hozzárendelned. Ezt az UAI-t fogjuk használni hitelesítéshez a telepítés során.

#### User Assigned Managed Identity (UAI) létrehozása

1. Írd be a *managed identities* kifejezést a portál tetején található **keresősávba**, majd válaszd ki a **Managed Identities** opciót.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.hu.png)

1. Válaszd a **+ Create** gombot.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.hu.png)

1. Végezd el a következő beállításokat:

    - Válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot** (ha szükséges, hozz létre újat).
    - Válaszd ki a kívánt **Régiót**.
    - Írd be a **Nevedet**. Egyedi érték kell legyen.

1. Válaszd a **Review + create** lehetőséget.

1. Válaszd a **+ Create** gombot.

#### Contributor szerepkör hozzárendelése a Managed Identity-hez

1. Navigálj el a létrehozott Managed Identity erőforráshoz.

1. Válaszd a bal oldali menüben az **Azure role assignments** opciót.

1. Válaszd a navigációs menüből a **+Add role assignment** lehetőséget.

1. Az Add role assignment oldalon végezd el a következő beállításokat:
    - Állítsd a **Scope**-ot **Resource group**-ra.
    - Válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot**.
    - Válaszd ki a **Contributor** szerepkört.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.hu.png)

1. Válaszd a **Save** gombot.

#### Storage Blob Data Reader szerepkör hozzárendelése a Managed Identity-hez

1. Írd be a *storage accounts* kifejezést a portál tetején található **keresősávba**, majd válaszd ki a **Storage accounts** opciót.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.hu.png)

1. Válaszd ki azt a tárolófiókot, amely az Azure Machine Learning munkaterülethez tartozik, amit létrehoztál. Például *finetunephistorage*.

1. A szerepkör hozzárendelés oldalára navigáláshoz végezd el a következő lépéseket:

    - Navigálj az Azure Storage fiókhoz.
    - Válaszd a bal oldali menüben az **Access Control (IAM)** lehetőséget.
    - Válaszd a navigációs menüből a **+ Add** gombot.
    - Válaszd a **Add role assignment** opciót.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.hu.png)

1. Az Add role assignment oldalon végezd el a következőket:

    - Írd be a *Storage Blob Data Reader* kifejezést a **keresősávba**, majd válaszd ki a megjelenő lehetőségek közül.
    - Kattints a **Next** gombra.
    - A Members oldalon válaszd az **Assign access to** mezőnél a **Managed identity** opciót.
    - Kattints a **+ Select members** gombra.
    - A Select managed identities oldalon válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a **Managed identity**-t, amely a **Manage Identity** kategóriába tartozik.
    - Válaszd ki a létrehozott Managed Identity-t, például *finetunephi-managedidentity*.
    - Kattints a **Select** gombra.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.hu.png)

1. Válaszd a **Review + assign** gombot.

#### AcrPull szerepkör hozzárendelése a Managed Identity-hez

1. Írd be a *container registries* kifejezést a portál tetején található **keresősávba**, majd válaszd ki a **Container registries** opciót.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.hu.png)

1. Válaszd ki a konténerregisztert, amely az Azure Machine Learning munkaterülethez tartozik. Például *finetunephicontainerregistries*.

1. A szerepkör hozzárendelés oldalára navigáláshoz végezd el a következő lépéseket:

    - Válaszd a bal oldali menüben az **Access Control (IAM)** lehetőséget.
    - Kattints a navigációs menüből a **+ Add** gombra.
    - Válaszd a **Add role assignment** opciót.

1. Az Add role assignment oldalon végezd el a következő beállításokat:

    - Írd be az *AcrPull* kifejezést a **keresősávba**, majd válaszd ki a megjelenő lehetőségek közül.
    - Kattints a **Next** gombra.
    - A Members oldalon válaszd az **Assign access to** mezőnél a **Managed identity** opciót.
    - Kattints a **+ Select members** gombra.
    - A Select managed identities oldalon válaszd ki az Azure **Előfizetésedet**.
    - Válaszd ki a **Managed identity**-t, amely a **Manage Identity** kategóriába tartozik.
    - Válaszd ki a létrehozott Managed Identity-t, például *finetunephi-managedidentity*.
    - Kattints a **Select** gombra.
    - Válaszd a **Review + assign** gombot.

### Projekt beállítása

Most létrehozol egy mappát a munkához, és beállítasz egy virtuális környezetet, hogy fejleszthess egy programot, amely felhasználókkal kommunikál, és az Azure Cosmos DB-ben tárolt csevegési előzményeket használja a válaszaihoz.

#### Mappa létrehozása a munkához

1. Nyiss meg egy terminált, és írd be a következő parancsot egy *finetune-phi* nevű mappa létrehozásához az alapértelmezett útvonalon.

    ```console
    mkdir finetune-phi
    ```

1. Írd be a következő parancsot a terminálba, hogy belépj a létrehozott *finetune-phi* mappába.

    ```console
    cd finetune-phi
    ```

#### Virtuális környezet létrehozása

1. Írd be a következő parancsot a terminálba egy *.venv* nevű virtuális környezet létrehozásához.

    ```console
    python -m venv .venv
    ```

1. Írd be a következő parancsot a terminálba a virtuális környezet aktiválásához.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Ha sikeres volt, a parancssor előtt megjelenik a *(.venv)* jelzés.

#### Szükséges csomagok telepítése

1. Írd be a következő parancsokat a terminálba a szükséges csomagok telepítéséhez.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Projektfájlok létrehozása

Ebben a gyakorlatban létrehozod a projekt alapvető fájljait. Ezek a fájlok tartalmazzák a letöltő szkriptet az adathalmazhoz, az Azure Machine Learning környezet beállítását, a Phi-3 modell finomhangolását, valamint a finomhangolt modell telepítését. Emellett létrehozol egy *conda.yml* fájlt a finomhangolási környezet beállításához.

Ebben a gyakorlatban:

- Létrehozol egy *download_dataset.py* fájlt az adathalmaz letöltéséhez.
- Létrehozol egy *setup_ml.py* fájlt az Azure Machine Learning környezet beállításához.
- Létrehozol egy *fine_tune.py* fájlt a *finetuning_dir* mappában a Phi-3 modell finomhangolásához az adathalmaz segítségével.
- Létrehozol egy *conda.yml* fájlt a finomhangolási környezet beállításához.
- Létrehozol egy *deploy_model.py* fájlt a finomhangolt modell telepítéséhez.
- Létrehozol egy *integrate_with_promptflow.py* fájlt a finomhangolt modell integrálásához és futtatás
![Előfizetési azonosító keresése.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.hu.png)

1. Végezze el a következő lépéseket az Azure Workspace név hozzáadásához:

    - Navigáljon az Ön által létrehozott Azure Machine Learning erőforráshoz.
    - Másolja be a fióknevét a *config.py* fájlba.

    ![Azure Machine Learning név keresése.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.hu.png)

1. Végezze el a következő lépéseket az Azure Resource Group név hozzáadásához:

    - Navigáljon az Ön által létrehozott Azure Machine Learning erőforráshoz.
    - Másolja be az Azure Resource Group nevét a *config.py* fájlba.

    ![Erőforráscsoport név keresése.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.hu.png)

2. Végezze el a következő lépéseket az Azure Managed Identity név hozzáadásához

    - Navigáljon a létrehozott Managed Identities erőforráshoz.
    - Másolja be az Azure Managed Identity nevét a *config.py* fájlba.

    ![UAI keresése.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.hu.png)

### Adatkészlet előkészítése finomhangoláshoz

Ebben a gyakorlatban lefuttatja a *download_dataset.py* fájlt, hogy letöltse az *ULTRACHAT_200k* adatkészleteket a helyi környezetébe. Ezt az adatkészletet használja majd a Phi-3 modell finomhangolásához az Azure Machine Learningben.

#### Töltse le az adatkészletet a *download_dataset.py* segítségével

1. Nyissa meg a *download_dataset.py* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot a *download_dataset.py* fájlba.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

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
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Útmutató minimális adatkészlettel történő finomhangoláshoz CPU használatával**
>
> Ha CPU-t szeretne használni a finomhangoláshoz, ez a megközelítés ideális azoknak, akik rendelkeznek előnyös előfizetéssel (például Visual Studio Enterprise Subscription), vagy gyorsan szeretnék tesztelni a finomhangolási és telepítési folyamatot.
>
> Cserélje ki a `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')` sort.
>

1. Írja be a következő parancsot a terminálba a szkript futtatásához és az adatkészlet letöltéséhez a helyi környezetbe.

    ```console
    python download_data.py
    ```

1. Ellenőrizze, hogy az adatkészletek sikeresen elmentésre kerültek-e a helyi *finetune-phi/data* könyvtárba.

> [!NOTE]
>
> **Adatkészlet mérete és a finomhangolás időtartama**
>
> Ebben a teljes körű mintában csak az adatkészlet 1%-át használja (`train_sft[:1%]`). Ez jelentősen csökkenti az adatmennyiséget, így gyorsítva mind a feltöltést, mind a finomhangolást. Állítsa be a százalékos arányt, hogy megtalálja az optimális egyensúlyt a tanítási idő és a modell teljesítménye között. Az adatkészlet kisebb részhalmazának használata lerövidíti a finomhangolás idejét, így kezelhetőbbé teszi a folyamatot egy teljes körű mintában.

## 2. Forgatókönyv: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban

### Azure CLI beállítása

Az Azure CLI-t be kell állítania a környezet hitelesítéséhez. Az Azure CLI lehetővé teszi az Azure erőforrások közvetlen kezelését a parancssorból, és biztosítja az Azure Machine Learning számára szükséges hitelesítő adatokat az erőforrások eléréséhez. A kezdéshez telepítse az [Azure CLI-t](https://learn.microsoft.com/cli/azure/install-azure-cli).

1. Nyisson meg egy terminálablakot, és írja be a következő parancsot az Azure fiókba történő bejelentkezéshez.

    ```console
    az login
    ```

1. Válassza ki az Azure fiókját.

1. Válassza ki az Azure előfizetését.

    ![Erőforráscsoport név keresése.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.hu.png)

> [!TIP]
>
> Ha problémája van az Azure-ba való bejelentkezéssel, próbáljon meg eszközkódos bejelentkezést használni. Nyisson meg egy terminált, és írja be a következő parancsot az Azure fiókba történő bejelentkezéshez:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 modell finomhangolása

Ebben a gyakorlatban a megadott adatkészlet segítségével finomhangolja a Phi-3 modellt. Először definiálja a finomhangolási folyamatot a *fine_tune.py* fájlban. Ezután konfigurálja az Azure Machine Learning környezetet, és elindítja a finomhangolási folyamatot a *setup_ml.py* fájl futtatásával. Ez a szkript biztosítja, hogy a finomhangolás az Azure Machine Learning környezetében történjen.

A *setup_ml.py* futtatásával elindítja a finomhangolási folyamatot az Azure Machine Learning környezetben.

#### Kód hozzáadása a *fine_tune.py* fájlhoz

1. Navigáljon a *finetuning_dir* mappába, és nyissa meg a *fine_tune.py* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot a *fine_tune.py* fájlba.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Mentse el és zárja be a *fine_tune.py* fájlt.

> [!TIP]
> **Phi-3.5 modell finomhangolása is lehetséges**
>
> A *fine_tune.py* fájlban megváltoztathatja a `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` mezőt a szkriptben.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 finomhangolása.":::
>

#### Kód hozzáadása a *setup_ml.py* fájlhoz

1. Nyissa meg a *setup_ml.py* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot a *setup_ml.py* fájlba.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Cserélje ki a `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` helyőrzőket a saját adataira.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Útmutató minimális adatkészlettel történő finomhangoláshoz CPU használatával**
>
> Ha CPU-t szeretne használni a finomhangoláshoz, ez a megközelítés ideális azoknak, akik előnyös előfizetéssel rendelkeznek (például Visual Studio Enterprise Subscription), vagy gyorsan szeretnék tesztelni a finomhangolási és telepítési folyamatot.
>
> 1. Nyissa meg a *setup_ml* fájlt.
> 1. Cserélje ki a `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` helyőrzőket a saját adataira.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Írja be a következő parancsot a *setup_ml.py* szkript futtatásához és a finomhangolási folyamat elindításához az Azure Machine Learningben.

    ```python
    python setup_ml.py
    ```

1. Ebben a gyakorlatban sikeresen finomhangolta a Phi-3 modellt az Azure Machine Learning segítségével. A *setup_ml.py* szkript futtatásával beállította az Azure Machine Learning környezetet, és elindította a *fine_tune.py* fájlban definiált finomhangolási folyamatot. Vegye figyelembe, hogy a finomhangolás jelentős időt vehet igénybe. A `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.hu.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` parancs futtatása után adja meg a kívánt nevet a telepítéshez.

#### Kód hozzáadása a *deploy_model.py* fájlhoz

A *deploy_model.py* fájl futtatása automatizálja az egész telepítési folyamatot. Regisztrálja a modellt, létrehozza a végpontot, és végrehajtja a telepítést a config.py fájlban megadott beállítások alapján, amelyek tartalmazzák a modell nevét, a végpont nevét és a telepítés nevét.

1. Nyissa meg a *deploy_model.py* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot a *deploy_model.py* fájlba.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Végezze el a következő lépéseket a `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` saját adatokkal történő kitöltéséhez.

1. Írja be a következő parancsot a *deploy_model.py* szkript futtatásához és a telepítési folyamat elindításához az Azure Machine Learningben.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Az extra költségek elkerülése érdekében győződjön meg róla, hogy törli a létrehozott végpontot az Azure Machine Learning munkaterületen.
>

#### A telepítés állapotának ellenőrzése az Azure Machine Learning munkaterületen

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Navigáljon az Ön által létrehozott Azure Machine Learning munkaterületre.

1. Válassza a **Studio web URL** lehetőséget az Azure Machine Learning munkaterület megnyitásához.

1. A bal oldali menüből válassza az **Endpoints** lehetőséget.

    ![Válassza az endpoints lehetőséget.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.hu.png)

2. Válassza ki a létrehozott végpontot.

    ![Válassza ki a létrehozott végpontot.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.hu.png)

3. Ezen az oldalon kezelheti a telepítési folyamat során létrehozott végpontokat.

## 3. Forgatókönyv: Integráció a Prompt flow-val és csevegés az egyedi modellel

### Egyedi Phi-3 modell integrálása a Prompt flow-val

A finomhangolt modell sikeres telepítése után integrálhatja azt a Prompt flow-val, hogy valós idejű alkalmazásokban használhassa, lehetővé téve különféle interaktív feladatok elvégzését az egyedi Phi-3 modellel.

#### Állítsa be az api kulcsot és a végpont URI-t a finomhangolt Phi-3 modellhez

1. Navigáljon az Ön által létrehozott Azure Machine Learning munkaterületre.
1. Válassza az **Endpoints** lehetőséget a bal oldali menüből.
1. Válassza ki a létrehozott végpontot.
1. Válassza a **Consume** lehetőséget a navigációs menüben.
1. Másolja be a **REST endpoint** értékét a *config.py* fájlba, és cserélje le az `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` értékeket a saját **Primary key** értékére.

    ![API kulcs és végpont URI másolása.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.hu.png)

#### Kód hozzáadása a *flow.dag.yml* fájlhoz

1. Nyissa meg a *flow.dag.yml* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot a *flow.dag.yml* fájlba.

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

#### Kód hozzáadása az *integrate_with_promptflow.py* fájlhoz

1. Nyissa meg az *integrate_with_promptflow.py* fájlt a Visual Studio Code-ban.

1. Illessze be a következő kódot az *integrate_with_promptflow.py* fájlba.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Csevegés az egyedi modellel

1. Írja be a következő parancsot a *deploy_model.py* szkript futtatásához és a telepítési folyamat elindításához az Azure Machine Learningben.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Íme egy példa az eredményekre: Most már cseveghet az egyedi Phi-3 modellel. Ajánlott olyan kérdéseket feltenni, amelyek az adatkészletből származnak, amelyet a finomhangoláshoz használt.

    ![Prompt flow példa.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.hu.png)

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.