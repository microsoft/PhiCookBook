<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:21:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hu"
}
-->
# Fine-tune és egyedi Phi-3 modellek integrálása a Prompt flow-val az Azure AI Foundry-ban

Ez az end-to-end (E2E) példa a Microsoft Tech Community „[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)” útmutatóján alapul. Bemutatja az egyedi Phi-3 modellek finomhangolásának, telepítésének és integrálásának folyamatát a Prompt flow-val az Azure AI Foundry-ban.
Ellentétben az E2E példával, a „[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)” gyakorlattal, amely helyi kód futtatást igényelt, ez a bemutató kizárólag az Azure AI / ML Studioban történő finomhangolásra és integrációra koncentrál.

## Áttekintés

Ebben az E2E példában megtanulod, hogyan finomhangold a Phi-3 modellt, és hogyan integráld a Prompt flow-val az Azure AI Foundry-ban. Az Azure AI / ML Studio segítségével létrehozol egy munkafolyamatot egyedi AI modellek telepítéséhez és használatához. Ez az E2E minta három szcenárióra oszlik:

**1. szcenárió: Azure erőforrások beállítása és előkészítés a finomhangoláshoz**

**2. szcenárió: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban**

**3. szcenárió: Integráció a Prompt flow-val és csevegés az egyedi modelleddel az Azure AI Foundry-ban**

Íme az E2E minta áttekintése.

![Phi-3-FineTuning_PromptFlow_Integration Áttekintés.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.hu.png)

### Tartalomjegyzék

1. **[1. szcenárió: Azure erőforrások beállítása és előkészítés a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace létrehozása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvóták igénylése az Azure előfizetésben](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Szerepkör-hozzárendelés hozzáadása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt beállítása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adatkészlet előkészítése finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[2. szcenárió: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studioban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 modell finomhangolása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Finomhangolt Phi-3 modell telepítése](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[3. szcenárió: Integráció a Prompt flow-val és csevegés az egyedi modelleddel az Azure AI Foundry-ban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Egyedi Phi-3 modell integrálása a Prompt flow-val](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Csevegés az egyedi Phi-3 modelleddel](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 1. szcenárió: Azure erőforrások beállítása és előkészítés a finomhangoláshoz

### Azure Machine Learning Workspace létrehozása

1. Írd be a *azure machine learning* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki az **Azure Machine Learning** opciót.

    ![Írd be az azure machine learning kifejezést.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.hu.png)

2. Válaszd a **+ Create** lehetőséget a navigációs menüből.

3. Válaszd a **New workspace** lehetőséget a navigációs menüből.

    ![Új workspace kiválasztása.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.hu.png)

4. Végezze el a következő lépéseket:

    - Válaszd ki az Azure **Subscription**-t.
    - Válaszd ki a használni kívánt **Resource group**-ot (ha szükséges, hozz létre újat).
    - Add meg a **Workspace Name**-et. Egyedi értéknek kell lennie.
    - Válaszd ki a kívánt **Region**-t.
    - Válaszd ki a használni kívánt **Storage account**-ot (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Key vault**-ot (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Application insights**-t (ha szükséges, hozz létre újat).
    - Válaszd ki a használni kívánt **Container registry**-t (ha szükséges, hozz létre újat).

    ![Azure Machine Learning kitöltése.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.hu.png)

5. Válaszd a **Review + Create** lehetőséget.

6. Válaszd a **Create** gombot.

### GPU kvóták igénylése az Azure előfizetésben

Ebben a bemutatóban megtanulod, hogyan finomhangold és telepítsd a Phi-3 modellt GPU-k használatával. A finomhangoláshoz a *Standard_NC24ads_A100_v4* GPU-t fogod használni, amelyhez kvótaigénylés szükséges. A telepítéshez pedig a *Standard_NC6s_v3* GPU-t, amely szintén kvótaigénylést igényel.

> [!NOTE]
>
> Csak a Pay-As-You-Go előfizetések (az alapértelmezett előfizetés típus) jogosultak GPU-kiosztásra; a kedvezményes előfizetések jelenleg nem támogatottak.
>

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Hajtsd végre a következő lépéseket a *Standard NCADSA100v4 Family* kvóta igényléséhez:

    - Válaszd a bal oldali fülön a **Quota** menüpontot.
    - Válaszd ki a használni kívánt **Virtual machine family**-t. Például válaszd a **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**-t, amely tartalmazza a *Standard_NC24ads_A100_v4* GPU-t.
    - Válaszd a **Request quota** lehetőséget a navigációs menüből.

        ![Kvóta igénylése.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.hu.png)

    - A Request quota oldalon add meg az új, kívánt **New cores limit** értéket. Például 24.
    - A Request quota oldalon válaszd a **Submit** gombot a GPU kvóta igényléséhez.

1. Hajtsd végre a következő lépéseket a *Standard NCSv3 Family* kvóta igényléséhez:

    - Válaszd a bal oldali fülön a **Quota** menüpontot.
    - Válaszd ki a használni kívánt **Virtual machine family**-t. Például válaszd a **Standard NCSv3 Family Cluster Dedicated vCPUs**-t, amely tartalmazza a *Standard_NC6s_v3* GPU-t.
    - Válaszd a **Request quota** lehetőséget a navigációs menüből.
    - A Request quota oldalon add meg az új, kívánt **New cores limit** értéket. Például 24.
    - A Request quota oldalon válaszd a **Submit** gombot a GPU kvóta igényléséhez.

### Szerepkör-hozzárendelés hozzáadása

A modellek finomhangolásához és telepítéséhez először létre kell hoznod egy User Assigned Managed Identity-t (UAI), és hozzá kell rendelni a megfelelő jogosultságokat. Ezt az UAI-t fogod használni az autentikációhoz a telepítés során.

#### User Assigned Managed Identity (UAI) létrehozása

1. Írd be a *managed identities* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki a **Managed Identities** opciót.

    ![Írd be a managed identities kifejezést.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.hu.png)

1. Válaszd a **+ Create** lehetőséget.

    ![Create kiválasztása.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.hu.png)

1. Végezze el a következő lépéseket:

    - Válaszd ki az Azure **Subscription**-t.
    - Válaszd ki a használni kívánt **Resource group**-ot (ha szükséges, hozz létre újat).
    - Válaszd ki a kívánt **Region**-t.
    - Add meg a **Name**-et. Egyedi értéknek kell lennie.

    ![Managed Identities kitöltése.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.hu.png)

1. Válaszd a **Review + create** lehetőséget.

1. Válaszd a **+ Create** gombot.

#### Contributor szerepkör-hozzárendelés hozzáadása a Managed Identity-hez

1. Navigálj az általad létrehozott Managed Identity erőforráshoz.

1. Válaszd a bal oldali fülön az **Azure role assignments** lehetőséget.

1. Válaszd a navigációs menüből a **+Add role assignment** lehetőséget.

1. Az Add role assignment oldalon végezd el a következőket:
    - Állítsd be a **Scope**-ot **Resource group**-ra.
    - Válaszd ki az Azure **Subscription**-t.
    - Válaszd ki a használni kívánt **Resource group**-ot.
    - Válaszd a **Role**-nál a **Contributor** szerepkört.

    ![Contributor szerepkör kitöltése.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.hu.png)

2. Válaszd a **Save** gombot.

#### Storage Blob Data Reader szerepkör-hozzárendelés hozzáadása a Managed Identity-hez

1. Írd be a *storage accounts* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki a **Storage accounts** opciót.

    ![Írd be a storage accounts kifejezést.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.hu.png)

1. Válaszd ki azt a storage accountot, amely az általad létrehozott Azure Machine Learning workspace-hez tartozik. Például *finetunephistorage*.

1. Végezze el a következő lépéseket az Add role assignment oldal megnyitásához:

    - Navigálj az Azure Storage accounthoz, amit létrehoztál.
    - Válaszd a bal oldali fülön az **Access Control (IAM)** lehetőséget.
    - Válaszd a navigációs menüből a **+ Add** lehetőséget.
    - Válaszd a navigációs menüből az **Add role assignment** lehetőséget.

    ![Szerepkör hozzáadása.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.hu.png)

1. Az Add role assignment oldalon végezd el a következő lépéseket:

    - A Role oldalon írd be a keresősávba a *Storage Blob Data Reader* kifejezést, majd válaszd ki a megjelenő opciók közül a **Storage Blob Data Reader** szerepkört.
    - A Role oldalon válaszd a **Next** gombot.
    - A Members oldalon válaszd az **Assign access to** mezőnél a **Managed identity** lehetőséget.
    - A Members oldalon válaszd a **+ Select members** lehetőséget.
    - A Select managed identities oldalon válaszd ki az Azure **Subscription**-t.
    - A Select managed identities oldalon válaszd ki a **Managed identity**-t, azaz a korábban létrehozott Managed Identity-t.
    - A Select managed identities oldalon válaszd ki a létrehozott Managed Identity-t, például *finetunephi-managedidentity*.
    - A Select managed identities oldalon válaszd a **Select** gombot.

    ![Managed Identity kiválasztása.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.hu.png)

1. Válaszd a **Review + assign** lehetőséget.

#### AcrPull szerepkör-hozzárendelés hozzáadása a Managed Identity-hez

1. Írd be a *container registries* kifejezést a portál oldal tetején található **keresősávba**, majd válaszd ki a **Container registries** opciót.

    ![Írd be a container registries kifejezést.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.hu.png)

1. Válaszd ki azt a container registry-t, amely az Azure Machine Learning workspace-hez tartozik. Például *finetunephicontainerregistry*.

1. Végezze el a következő lépéseket az Add role assignment oldal megnyitásához:

    - Válaszd a bal oldali fülön az **Access Control (IAM)** lehetőséget.
    - Válaszd a navigációs menüből a **+ Add** lehetőséget.
    - Válaszd a navigációs menüből az **Add role assignment** lehetőséget.

1. Az Add role assignment oldalon végezd el a következő lépéseket:

    - A Role oldalon írd be a keresősávba az *AcrPull* kifejezést, majd válaszd ki a megjelenő opciók közül az **AcrPull** szerepkört.
    - A Role oldalon válaszd a **Next** gombot.
    - A Members oldalon válaszd az **Assign access to** mezőnél a **Managed identity** lehetőséget.
    - A Members oldalon válaszd a **+ Select members** lehetőséget.
    - A Select managed identities oldalon válaszd ki az Azure **Subscription**-t.
    - A Select managed identities oldalon válaszd ki a **Managed identity**-t, azaz a korábban létrehozott Managed Identity-t.
    - A Select managed identities oldalon válaszd ki a létrehozott Managed Identity-t, például *finetunephi-managedidentity*.
    - A Select managed identities oldalon válaszd a **Select** gombot.
    - Válaszd a **Review + assign** lehetőséget.

### Projekt beállítása

A finomhangoláshoz szükséges adatkészletek letöltéséhez helyi környezetet állítasz be.

Ebben a gyakorlatban:

- Létrehozol egy mappát, ahol dolgozni fogsz.
- Létrehozol egy virtuális környezetet.
- Telepíted a szükséges csomagokat.
- Létrehozol egy *download_dataset.py* fájlt az adatkészlet letöltéséhez.

#### Mappa létrehozása a munkához

1. Nyiss egy terminálablakot, és írd be a következő parancsot egy *finetune-phi* nevű mappa létrehozásához az alapértelmezett útvonalon.

    ```console
    mkdir finetune-phi
    ```

2. Írd be a következő parancsot a terminálban, hogy belépj a létrehozott *finetune-phi* mappába.

    ```console
    cd finetune-phi
    ```

#### Virtuális környezet létrehozása

1. Írd be a következő parancsot a terminálban egy *.venv* nevű virtuális környezet létrehozásához.

    ```console
    python -m venv .venv
    ```

2. Írd be a következő parancsot a terminálban a virtuális környezet aktiválásához.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ha sikerült, akkor a
1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki a bal oldali menüből a **Compute** lehetőséget.

1. A navigációs menüből válaszd a **Compute clusters** opciót.

1. Kattints a **+ New** gombra.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.hu.png)

1. Végezze el a következő lépéseket:

    - Válaszd ki a kívánt **Region**-t.
    - Állítsd be a **Virtual machine tier** értékét **Dedicated**-re.
    - Állítsd be a **Virtual machine type** értékét **GPU**-ra.
    - A **Virtual machine size** szűrőjét állítsd **Select from all options**-ra.
    - Válaszd ki a **Virtual machine size**-t: **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.hu.png)

1. Kattints a **Next** gombra.

1. Végezze el a következő lépéseket:

    - Írd be a **Compute name**-et. Egyedi értéknek kell lennie.
    - Állítsd be a **Minimum number of nodes** értékét **0**-ra.
    - Állítsd be a **Maximum number of nodes** értékét **1**-re.
    - Állítsd be az **Idle seconds before scale down** értékét **120**-ra.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.hu.png)

1. Kattints a **Create** gombra.

#### A Phi-3 modell finomhangolása

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki az általad létrehozott Azure Machine Learning workspace-et.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hu.png)

1. Végezze el a következő lépéseket:

    - Válaszd ki a bal oldali menüből a **Model catalog**-ot.
    - Írd be a keresőmezőbe a *phi-3-mini-4k* kifejezést, majd válaszd ki a megjelenő opciók közül a **Phi-3-mini-4k-instruct** modellt.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.hu.png)

1. Válaszd ki a navigációs menüből a **Fine-tune** opciót.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.hu.png)

1. Végezze el a következő lépéseket:

    - Állítsd be a **Select task type** értékét **Chat completion**-re.
    - Kattints a **+ Select data** gombra, és töltsd fel a **Traning data**-t.
    - A validációs adat feltöltés típusát állítsd **Provide different validation data**-ra.
    - Kattints ismét a **+ Select data** gombra, és töltsd fel a **Validation data**-t.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.hu.png)

    > [!TIP]
    >
    > Az **Advanced settings** alatt testre szabhatod a konfigurációkat, például a **learning_rate** vagy a **lr_scheduler_type** beállításokat, hogy a finomhangolási folyamatot az igényeid szerint optimalizáld.

1. Kattints a **Finish** gombra.

1. Ebben a gyakorlatban sikeresen finomhangoltad a Phi-3 modellt az Azure Machine Learning segítségével. Fontos megjegyezni, hogy a finomhangolás hosszabb időt vehet igénybe. Miután elindítottad a finomhangolási feladatot, várnod kell, amíg befejeződik. A folyamat állapotát a bal oldali menü **Jobs** fülén követheted nyomon az Azure Machine Learning Workspace-ben. A következő részben telepíted a finomhangolt modellt, és integrálod a Prompt flow-val.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.hu.png)

### A finomhangolt Phi-3 modell telepítése

Ahhoz, hogy a finomhangolt Phi-3 modellt integráld a Prompt flow-val, telepítened kell a modellt, hogy valós idejű lekérdezésekhez elérhető legyen. Ez a folyamat magában foglalja a modell regisztrálását, egy online végpont létrehozását és a modell telepítését.

Ebben a gyakorlatban:

- Regisztrálod a finomhangolt modellt az Azure Machine Learning workspace-ben.
- Létrehozol egy online végpontot.
- Telepíted a regisztrált finomhangolt Phi-3 modellt.

#### A finomhangolt modell regisztrálása

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki az általad létrehozott Azure Machine Learning workspace-et.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hu.png)

1. Válaszd ki a bal oldali menüből a **Models** opciót.
1. Kattints a **+ Register** gombra.
1. Válaszd ki a **From a job output** lehetőséget.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.hu.png)

1. Válaszd ki az általad létrehozott munkát.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.hu.png)

1. Kattints a **Next** gombra.

1. Állítsd be a **Model type**-ot **MLflow**-ra.

1. Győződj meg róla, hogy a **Job output** ki van választva; ennek automatikusan ki kell választottnak lennie.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.hu.png)

2. Kattints a **Next** gombra.

3. Kattints a **Register** gombra.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.hu.png)

4. A regisztrált modelljeidet megtekintheted a bal oldali menü **Models** menüpontjában.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.hu.png)

#### A finomhangolt modell telepítése

1. Navigálj az általad létrehozott Azure Machine Learning workspace-be.

1. Válaszd ki a bal oldali menüből az **Endpoints** opciót.

1. A navigációs menüből válaszd a **Real-time endpoints** lehetőséget.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.hu.png)

1. Kattints a **Create** gombra.

1. Válaszd ki a regisztrált modellt, amelyet létrehoztál.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.hu.png)

1. Kattints a **Select** gombra.

1. Végezze el a következő beállításokat:

    - Válaszd ki a **Virtual machine**-t: *Standard_NC6s_v3*.
    - Állítsd be az **Instance count** értékét a kívánt számra, például *1*.
    - Az **Endpoint** beállítását állítsd **New**-ra egy új végpont létrehozásához.
    - Írd be az **Endpoint name**-et. Egyedi értéknek kell lennie.
    - Írd be a **Deployment name**-et. Egyedi értéknek kell lennie.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.hu.png)

1. Kattints a **Deploy** gombra.

> [!WARNING]
> Az esetleges további költségek elkerülése érdekében győződj meg róla, hogy törlöd a létrehozott végpontot az Azure Machine Learning workspace-ben.
>

#### A telepítés állapotának ellenőrzése az Azure Machine Learning Workspace-ben

1. Navigálj az általad létrehozott Azure Machine Learning workspace-be.

1. Válaszd ki a bal oldali menüből az **Endpoints** opciót.

1. Válaszd ki a létrehozott végpontot.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.hu.png)

1. Ezen az oldalon kezelheted a végpontokat a telepítés folyamata alatt.

> [!NOTE]
> A telepítés befejezése után győződj meg róla, hogy a **Live traffic** értéke **100%**. Ha nem, válaszd az **Update traffic** opciót a forgalom beállításainak módosításához. Ne feledd, ha a forgalom 0%-ra van állítva, nem tudod tesztelni a modellt.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.hu.png)
>

## 3. Forgatókönyv: Integráció a Prompt flow-val és beszélgetés az egyedi modelleddel az Azure AI Foundry-ban

### Az egyedi Phi-3 modell integrálása a Prompt flow-val

Miután sikeresen telepítetted a finomhangolt modellt, most integrálhatod azt a Prompt Flow-val, hogy valós idejű alkalmazásokban használd, és különféle interaktív feladatokat végezhess az egyedi Phi-3 modelleddel.

Ebben a gyakorlatban:

- Létrehozol egy Azure AI Foundry Hub-ot.
- Létrehozol egy Azure AI Foundry Project-et.
- Létrehozol egy Prompt flow-t.
- Hozzáadsz egy egyedi kapcsolatot a finomhangolt Phi-3 modellhez.
- Beállítod a Prompt flow-t, hogy beszélgessen az egyedi Phi-3 modelleddel.

> [!NOTE]
> A Promptflow integrációt az Azure ML Studio-n keresztül is elvégezheted. Az integrációs folyamat ugyanígy alkalmazható az Azure ML Studio-ban is.

#### Azure AI Foundry Hub létrehozása

A projekt létrehozása előtt szükség van egy Hub-ra. A Hub olyan, mint egy Resource Group, amely lehetővé teszi több projekt szervezését és kezelését az Azure AI Foundry-n belül.

1. Látogass el az [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Válaszd ki a bal oldali menüből az **All hubs** opciót.

1. A navigációs menüből válaszd a **+ New hub** lehetőséget.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.hu.png)

1. Végezze el a következő lépéseket:

    - Írd be a **Hub name**-et. Egyedi értéknek kell lennie.
    - Válaszd ki az Azure **Subscription**-t.
    - Válaszd ki a használni kívánt **Resource group**-ot (ha szükséges, hozz létre újat).
    - Válaszd ki a kívánt **Location**-t.
    - Válaszd ki a használni kívánt **Connect Azure AI Services**-t (ha szükséges, hozz létre újat).
    - A **Connect Azure AI Search** beállítást állítsd **Skip connecting**-re.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.hu.png)

1. Kattints a **Next** gombra.

#### Azure AI Foundry Project létrehozása

1. Az általad létrehozott Hub-ban válaszd ki a bal oldali menüből az **All projects** opciót.

1. A navigációs menüből válaszd a **+ New project** lehetőséget.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.hu.png)

1. Írd be a **Project name**-et. Egyedi értéknek kell lennie.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.hu.png)

1. Kattints a **Create a project** gombra.

#### Egyedi kapcsolat hozzáadása a finomhangolt Phi-3 modellhez

Ahhoz, hogy az egyedi Phi-3 modellt integráld a Prompt flow-val, el kell mentened a modell végpontját és kulcsát egy egyedi kapcsolatként. Ez a beállítás biztosítja, hogy a Prompt flow hozzáférjen az egyedi Phi-3 modelledhez.

#### Az api kulcs és az endpoint URI beállítása a finomhangolt Phi-3 modellhez

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Navigálj az általad létrehozott Azure Machine Learning workspace-be.

1. Válaszd ki a bal oldali menüből az **Endpoints** opciót.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.hu.png)

1. Válaszd ki a létrehozott végpontot.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.hu.png)

1. A navigációs menüből válaszd a **Consume** opciót.

1. Másold ki a **REST endpoint**-ot és a **Primary key**-t.
![Másold ki az api kulcsot és az endpoint URI-t.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.hu.png)

#### Egyedi kapcsolat hozzáadása

1. Látogass el az [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalra.

1. Navigálj az általad létrehozott Azure AI Foundry projekthez.

1. A létrehozott projektben válaszd a bal oldali fülön a **Beállítások** menüpontot.

1. Válaszd a **+ Új kapcsolat** lehetőséget.

    ![Új kapcsolat kiválasztása.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.hu.png)

1. A navigációs menüből válaszd a **Custom keys** opciót.

    ![Egyedi kulcsok kiválasztása.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.hu.png)

1. Hajtsd végre a következő lépéseket:

    - Válaszd a **+ Kulcspár hozzáadása** lehetőséget.
    - A kulcs neve legyen **endpoint**, és illeszd be az Azure ML Studioból másolt endpointot az érték mezőbe.
    - Ismét válaszd a **+ Kulcspár hozzáadása** opciót.
    - A kulcs neve legyen **key**, és illeszd be az Azure ML Studioból másolt kulcsot az érték mezőbe.
    - A kulcsok hozzáadása után jelöld be az **is secret** opciót, hogy a kulcs ne legyen nyilvánosan látható.

    ![Kapcsolat hozzáadása.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.hu.png)

1. Válaszd az **Add connection** gombot.

#### Prompt flow létrehozása

Hozzáadtál egy egyedi kapcsolatot az Azure AI Foundry-ban. Most hozzunk létre egy Prompt flow-t az alábbi lépésekkel. Ezután csatlakoztatni fogod a Prompt flow-t az egyedi kapcsolathoz, hogy a finomhangolt modellt használni tudd a Prompt flow-n belül.

1. Navigálj az általad létrehozott Azure AI Foundry projekthez.

1. Válaszd a bal oldali fülön a **Prompt flow** menüpontot.

1. A navigációs menüből válaszd a **+ Create** lehetőséget.

    ![Promptflow kiválasztása.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.hu.png)

1. Válaszd a navigációs menüből a **Chat flow** opciót.

    ![Chat flow kiválasztása.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.hu.png)

1. Írd be a használni kívánt **Mappa nevét**.

    ![Név megadása.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.hu.png)

2. Válaszd a **Create** gombot.

#### Prompt flow beállítása a saját Phi-3 modellel való csevegéshez

Integrálnod kell a finomhangolt Phi-3 modellt a Prompt flow-ba. Azonban a meglévő Prompt flow nem erre a célra készült, ezért újra kell tervezned a Prompt flow-t, hogy támogassa az egyedi modell integrációját.

1. A Prompt flow-ban végezd el a következőket a meglévő folyamat újraépítéséhez:

    - Válaszd a **Raw file mode** módot.
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

    - Válaszd a **Mentés** gombot.

    ![Raw file mode kiválasztása.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.hu.png)

1. Add hozzá a következő kódot az *integrate_with_promptflow.py* fájlhoz, hogy a Prompt flow-ban használd az egyedi Phi-3 modellt.

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

    ![Prompt flow kód beillesztése.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.hu.png)

> [!NOTE]
> Részletesebb információkért az Azure AI Foundry-ban történő Prompt flow használatról, lásd a [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) dokumentációt.

1. Válaszd a **Chat input** és **Chat output** opciókat, hogy engedélyezd a csevegést a modelleddel.

    ![Bemenet és kimenet kiválasztása.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.hu.png)

1. Most már készen állsz arra, hogy csevegj a saját Phi-3 modelleddel. A következő gyakorlatban megtanulod, hogyan indítsd el a Prompt flow-t, és hogyan használhatod a finomhangolt Phi-3 modelleddel való csevegéshez.

> [!NOTE]
>
> Az újraépített folyamatnak a következő képhez hasonlónak kell lennie:
>
> ![Példa folyamat.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.hu.png)
>

### Csevegj a saját Phi-3 modelleddel

Most, hogy finomhangoltad és integráltad a saját Phi-3 modelledet a Prompt flow-val, készen állsz a vele való interakcióra. Ez a gyakorlat végigvezet a beállítás és a csevegés elindításának folyamatán a modelleddel a Prompt flow segítségével. Ezeknek a lépéseknek a követésével teljes mértékben kihasználhatod a finomhangolt Phi-3 modell képességeit különféle feladatok és beszélgetések során.

- Csevegj a saját Phi-3 modelleddel a Prompt flow használatával.

#### Prompt flow indítása

1. Válaszd a **Start compute sessions** lehetőséget a Prompt flow elindításához.

    ![Számítási munkamenet indítása.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.hu.png)

1. Válaszd a **Validate and parse input** opciót a paraméterek frissítéséhez.

    ![Bemenet érvényesítése.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.hu.png)

1. Válaszd ki a **connection** értékét az általad létrehozott egyedi kapcsolathoz. Például *connection*.

    ![Kapcsolat kiválasztása.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.hu.png)

#### Csevegj az egyedi modelleddel

1. Válaszd a **Chat** lehetőséget.

    ![Csevegés kiválasztása.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.hu.png)

1. Íme egy példa az eredményekre: Most már cseveghetsz a saját Phi-3 modelleddel. Ajánlott olyan kérdéseket feltenni, amelyek a finomhangoláshoz használt adatokra épülnek.

    ![Csevegés a prompt flow-val.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.hu.png)

**Felelősségkizárás**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai, emberi fordítást javasolunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.