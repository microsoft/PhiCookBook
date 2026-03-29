# Finjustera och integrera anpassade Phi-3-modeller med Prompt flow i Microsoft Foundry

Detta end-to-end (E2E) exempel är baserat på guiden "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" från Microsoft Tech Community. Den introducerar processerna för finjustering, distribuering och integrering av anpassade Phi-3-modeller med Prompt flow i Microsoft Foundry.
Till skillnad från E2E-exemplet, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", som involverade att köra kod lokalt, fokuserar denna handledning helt på att finjustera och integrera din modell inom Azure AI / ML Studio.

## Översikt

I detta E2E-exempel kommer du att lära dig hur man finjusterar Phi-3-modellen och integrerar den med Prompt flow i Microsoft Foundry. Genom att utnyttja Azure AI / ML Studio kommer du att etablera ett arbetsflöde för att distribuera och använda anpassade AI-modeller. Detta E2E-exempel är uppdelat i tre scenarier:

**Scenario 1: Ställ in Azure-resurser och förbered för finjustering**

**Scenario 2: Finjustera Phi-3-modellen och distribuera i Azure Machine Learning Studio**

**Scenario 3: Integrera med Prompt flow och chatta med din anpassade modell i Microsoft Foundry**

Här är en översikt av detta E2E-exempel.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/sv/00-01-architecture.198ba0f1ae6d841a.webp)

### Innehållsförteckning

1. **[Scenario 1: Ställ in Azure-resurser och förbered för finjustering](#scenario-1-ställ-in-azure-resurser-och-förbered-för-finjustering)**
    - [Skapa ett Azure Machine Learning-arbetsyta](#skapa-ett-azure-machine-learning-arbetsyta)
    - [Begär GPU-kvoter i Azure-prenumerationen](#begär-gpu-kvoter-i-azure-prenumerationen)
    - [Lägg till rolltilldelning](#lägg-till-rolltilldelning)
    - [Ställ in projekt](#ställ-in-projektet)
    - [Förbered dataset för finjustering](#förbered-dataset-för-finjustering)

1. **[Scenario 2: Finjustera Phi-3-modellen och distribuera i Azure Machine Learning Studio](#scenario-2-finjustera-phi-3-modellen-och-distribuera-i-azure-machine-learning-studio)**
    - [Finjustera Phi-3-modellen](#finjustera-phi-3-modellen)
    - [Distribuera den finjusterade Phi-3-modellen](#distribuera-den-finjusterade-phi-3-modellen)

1. **[Scenario 3: Integrera med Prompt flow och chatta med din anpassade modell i Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrera den anpassade Phi-3-modellen med Prompt flow](#integrera-den-anpassade-phi-3-modellen-med-prompt-flow)
    - [Chatta med din anpassade Phi-3-modell](#chatta-med-din-anpassade-phi-3-modell)

## Scenario 1: Ställ in Azure-resurser och förbered för finjustering

### Skapa ett Azure Machine Learning-arbetsyta

1. Skriv *azure machine learning* i **sökfältet** högst upp på portalsidan och välj **Azure Machine Learning** från alternativen som visas.

    ![Type azure machine learning.](../../../../../../translated_images/sv/01-01-type-azml.acae6c5455e67b4b.webp)

2. Välj **+ Skapa** från navigeringsmenyn.

3. Välj **Ny arbetsyta** från navigeringsmenyn.

    ![Select new workspace.](../../../../../../translated_images/sv/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Utför följande uppgifter:

    - Välj din Azure **Prenumeration**.
    - Välj den **Resursgrupp** som ska användas (skapa en ny om det behövs).
    - Ange **Arbetsytans namn**. Det måste vara unikt.
    - Välj den **Region** du vill använda.
    - Välj det **Lagringskonto** som ska användas (skapa ett nytt om det behövs).
    - Välj den **Key vault** som ska användas (skapa en ny om det behövs).
    - Välj **Application Insights** som ska användas (skapa en ny om det behövs).
    - Välj **Container Registry** som ska användas (skapa en ny om det behövs).

    ![Fill azure machine learning.](../../../../../../translated_images/sv/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Välj **Granska + skapa**.

6. Välj **Skapa**.

### Begär GPU-kvoter i Azure-prenumerationen

I denna handledning kommer du att lära dig hur man finjusterar och distribuerar en Phi-3-modell med hjälp av GPU:er. För finjustering kommer du att använda *Standard_NC24ads_A100_v4* GPU, som kräver en kvotbegäran. För distribution kommer du att använda *Standard_NC6s_v3* GPU, som också kräver en kvotbegäran.

> [!NOTE]
>
> Endast Pay-As-You-Go-prenumerationer (standardtyp av prenumeration) är berättigade till GPU-allokering; förmånsprenumerationer stöds inte för närvarande.
>

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Utför följande för att begära kvot för *Standard NCADSA100v4 Family*:

    - Välj **Kvot** från fliken till vänster.
    - Välj den **Virtuella maskinfamilj** som ska användas. Till exempel, välj **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, som inkluderar *Standard_NC24ads_A100_v4* GPU:n.
    - Välj **Begär kvot** från navigeringsmenyn.

        ![Request quota.](../../../../../../translated_images/sv/02-02-request-quota.c0428239a63ffdd5.webp)

    - På sidan Begär kvot anger du det **Nya kärngränsvärde** du vill använda. Till exempel 24.
    - På sidan Begär kvot väljer du **Skicka** för att begära GPU-kvoten.

1. Utför följande för att begära kvot för *Standard NCSv3 Family*:

    - Välj **Kvot** från fliken till vänster.
    - Välj den **Virtuella maskinfamilj** som ska användas. Till exempel, välj **Standard NCSv3 Family Cluster Dedicated vCPUs**, som inkluderar *Standard_NC6s_v3* GPU:n.
    - Välj **Begär kvot** från navigeringsmenyn.
    - På sidan Begär kvot anger du det **Nya kärngränsvärde** du vill använda. Till exempel 24.
    - På sidan Begär kvot väljer du **Skicka** för att begära GPU-kvoten.

### Lägg till rolltilldelning

För att finjustera och distribuera dina modeller måste du först skapa en User Assigned Managed Identity (UAI) och tilldela den lämpliga behörigheter. Denna UAI kommer att användas för autentisering vid distribution.

#### Skapa User Assigned Managed Identity (UAI)

1. Skriv *managed identities* i **sökfältet** högst upp på portalsidan och välj **Managed Identities** från alternativen som visas.

    ![Type managed identities.](../../../../../../translated_images/sv/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Välj **+ Skapa**.

    ![Select create.](../../../../../../translated_images/sv/03-02-select-create.92bf8989a5cd98f2.webp)

1. Utför följande uppgifter:

    - Välj din Azure **Prenumeration**.
    - Välj den **Resursgrupp** som ska användas (skapa en ny om det behövs).
    - Välj den **Region** du vill använda.
    - Ange **Namn**. Det måste vara unikt.

    ![Select create.](../../../../../../translated_images/sv/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Välj **Granska + skapa**.

1. Välj **+ Skapa**.

#### Lägg till rolltilldelning för bidragsgivare till Managed Identity

1. Navigera till resursen Managed Identity som du skapade.

1. Välj **Azure rolltilldelningar** från fliken till vänster.

1. Välj **+ Lägg till rolltilldelning** från navigeringsmenyn.

1. På sidan Lägg till rolltilldelning utför du följande:
    - Välj **Omfattning** till **Resursgrupp**.
    - Välj din Azure **Prenumeration**.
    - Välj den **Resursgrupp** som ska användas.
    - Välj **Roll** till **Bidragsgivare**.

    ![Fill contributor role.](../../../../../../translated_images/sv/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Välj **Spara**.

#### Lägg till rolltilldelning Storage Blob Data Reader till Managed Identity

1. Skriv *storage accounts* i **sökfältet** högst upp på portalsidan och välj **Storage accounts** från alternativen som visas.

    ![Type storage accounts.](../../../../../../translated_images/sv/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Välj det lagringskonto som är kopplat till Azure Machine Learning-arbetsytan du skapade. Till exempel, *finetunephistorage*.

1. Utför följande för att navigera till sidan för att lägga till rolltilldelning:

    - Navigera till det Azure Storage-konto som du skapade.
    - Välj **Access Control (IAM)** från fliken till vänster.
    - Välj **+ Lägg till** från navigeringsmenyn.
    - Välj **Lägg till rolltilldelning** från navigeringsmenyn.

    ![Add role.](../../../../../../translated_images/sv/03-06-add-role.353ccbfdcf0789c2.webp)

1. På sidan Lägg till rolltilldelning utför du följande:

    - På sidan Roll, skriv *Storage Blob Data Reader* i **sökfältet** och välj **Storage Blob Data Reader** från alternativen som visas.
    - På sidan Roll, välj **Nästa**.
    - På sidan Medlemmar, välj **Tilldela åtkomst till** **Managed identity**.
    - På sidan Medlemmar, välj **+ Välj medlemmar**.
    - På sidan Välj hanterade identiteter, välj din Azure **Prenumeration**.
    - På sidan Välj hanterade identiteter, välj den **Managed identity** till **Manage Identity**.
    - På sidan Välj hanterade identiteter, välj den hanterade identitet du skapade. Till exempel, *finetunephi-managedidentity*.
    - På sidan Välj hanterade identiteter, välj **Välj**.

    ![Select managed identity.](../../../../../../translated_images/sv/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Välj **Granska + tilldela**.

#### Lägg till AcrPull rolltilldelning till Managed Identity

1. Skriv *container registries* i **sökfältet** högst upp på portalsidan och välj **Container registries** från alternativen som visas.

    ![Type container registries.](../../../../../../translated_images/sv/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Välj container-registret som är kopplat till Azure Machine Learning-arbetsytan. Till exempel, *finetunephicontainerregistry*

1. Utför följande för att navigera till sidan Lägg till rolltilldelning:

    - Välj **Access Control (IAM)** från fliken till vänster.
    - Välj **+ Lägg till** från navigeringsmenyn.
    - Välj **Lägg till rolltilldelning** från navigeringsmenyn.

1. På sidan Lägg till rolltilldelning utför du följande:

    - På sidan Roll, skriv *AcrPull* i **sökfältet** och välj **AcrPull** från alternativen som visas.
    - På sidan Roll, välj **Nästa**.
    - På sidan Medlemmar, välj **Tilldela åtkomst till** **Managed identity**.
    - På sidan Medlemmar, välj **+ Välj medlemmar**.
    - På sidan Välj hanterade identiteter, välj din Azure **Prenumeration**.
    - På sidan Välj hanterade identiteter, välj den **Managed identity** till **Manage Identity**.
    - På sidan Välj hanterade identiteter, välj den hanterade identitet du skapade. Till exempel, *finetunephi-managedidentity*.
    - På sidan Välj hanterade identiteter, välj **Välj**.
    - Välj **Granska + tilldela**.

### Ställ in projektet

För att ladda ner de dataset som behövs för finjustering kommer du att ställa in en lokal miljö.

I denna övning ska du

- Skapa en mapp att arbeta i.
- Skapa en virtuell miljö.
- Installera de nödvändiga paketen.
- Skapa en fil *download_dataset.py* för att ladda ner datasetet.

#### Skapa en mapp att arbeta i

1. Öppna ett terminalfönster och skriv följande kommando för att skapa en mapp med namnet *finetune-phi* i standardvägen.

    ```console
    mkdir finetune-phi
    ```

2. Skriv följande kommando i terminalen för att navigera till mappen *finetune-phi* som du skapade.

    ```console
    cd finetune-phi
    ```

#### Skapa en virtuell miljö

1. Skriv följande kommando i terminalen för att skapa en virtuell miljö med namnet *.venv*.
    ```console
    python -m venv .venv
    ```

2. Skriv följande kommando i din terminal för att aktivera den virtuella miljön.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Om det fungerade ska du se *(.venv)* före kommandoprompten.

#### Installera de nödvändiga paketen

1. Skriv följande kommandon i din terminal för att installera de nödvändiga paketen.

    ```console
    pip install datasets==2.19.1
    ```

#### Skapa `donload_dataset.py`

> [!NOTE]
> Komplett mappstruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Öppna **Visual Studio Code**.

1. Välj **File** i menyraden.

1. Välj **Open Folder**.

1. Välj mappen *finetune-phi* som du skapade, vilken finns på *C:\Users\dinAnvändare\finetune-phi*.

    ![Välj mappen som du skapade.](../../../../../../translated_images/sv/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. I vänstra panelen i Visual Studio Code, högerklicka och välj **New File** för att skapa en ny fil med namnet *download_dataset.py*.

    ![Skapa en ny fil.](../../../../../../translated_images/sv/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Förbered dataset för finjustering

I denna övning kommer du att köra filen *download_dataset.py* för att ladda ner *ultrachat_200k* dataseten till din lokala miljö. Du kommer sedan att använda detta dataset för att finjustera Phi-3-modellen i Azure Machine Learning.

I denna övning kommer du att:

- Lägga till kod i filen *download_dataset.py* för att ladda ner dataset.
- Köra filen *download_dataset.py* för att ladda ner dataset till din lokala miljö.

#### Ladda ner ditt dataset med *download_dataset.py*

1. Öppna filen *download_dataset.py* i Visual Studio Code.

1. Lägg till följande kod i filen *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Ladda datasetet med det angivna namnet, konfigurationen och delningsförhållandet
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Dela datasetet i tränings- och testuppsättningar (80% träning, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Skapa katalogen om den inte finns
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Öppna filen i skrivläge
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterera över varje post i datasetet
            for record in dataset:
                # Dumpa posten som ett JSON-objekt och skriv det till filen
                json.dump(record, f)
                # Skriv en ny rad för att separera poster
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Ladda och dela ULTRACHAT_200k-datasetet med en specifik konfiguration och delningsförhållande
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrahera tränings- och testdataseten från delningen
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Spara träningsdatasetet till en JSONL-fil
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Spara testdatasetet till en separat JSONL-fil
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Skriv följande kommando i din terminal för att köra skriptet och ladda ner datasetet till din lokala miljö.

    ```console
    python download_dataset.py
    ```

1. Kontrollera att dataset har sparats framgångsrikt till din lokala *finetune-phi/data*-mapp.

> [!NOTE]
>
> #### Notera datasetets storlek och finjusteringstid
>
> I denna handledning använder du endast 1% av datasetet (`split='train[:1%]'`). Detta minskar mängden data avsevärt, vilket påskyndar både uppladdning och finjustering. Du kan justera procentandelen för att hitta rätt balans mellan träningstid och modellprestanda. Att använda en mindre delmängd av datasetet minskar tiden som krävs för finjustering, vilket gör processen mer hanterbar för en handledning.

## Scenario 2: Finjustera Phi-3-modellen och distribuera i Azure Machine Learning Studio

### Finjustera Phi-3-modellen

I denna övning kommer du att finjustera Phi-3-modellen i Azure Machine Learning Studio.

I denna övning kommer du att:

- Skapa ett dator-kluster för finjustering.
- Finjustera Phi-3-modellen i Azure Machine Learning Studio.

#### Skapa dator-kluster för finjustering

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Välj **Compute** från fliken till vänster.

1. Välj **Compute clusters** i navigationsmenyn.

1. Välj **+ New**.

    ![Välj compute.](../../../../../../translated_images/sv/06-01-select-compute.a29cff290b480252.webp)

1. Utför följande uppgifter:

    - Välj önskad **Region**.
    - Välj **Virtual machine tier** till **Dedicated**.
    - Välj **Virtual machine type** till **GPU**.
    - Välj filtret för **Virtual machine size** till **Select from all options**.
    - Välj **Virtual machine size** till **Standard_NC24ads_A100_v4**.

    ![Skapa kluster.](../../../../../../translated_images/sv/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Välj **Next**.

1. Utför följande uppgifter:

    - Ange **Compute name**. Det måste vara ett unikt namn.
    - Välj **Minimum number of nodes** till **0**.
    - Välj **Maximum number of nodes** till **1**.
    - Välj **Idle seconds before scale down** till **120**.

    ![Skapa kluster.](../../../../../../translated_images/sv/06-03-create-cluster.4a54ba20914f3662.webp)

1. Välj **Create**.

#### Finjustera Phi-3-modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Välj den Azure Machine Learning-arbetsytan som du skapade.

    ![Välj arbetsyta som du skapade.](../../../../../../translated_images/sv/06-04-select-workspace.a92934ac04f4f181.webp)

1. Utför följande uppgifter:

    - Välj **Model catalog** från fliken till vänster.
    - Skriv *phi-3-mini-4k* i **sökfältet** och välj **Phi-3-mini-4k-instruct** från alternativen som visas.

    ![Skriv phi-3-mini-4k.](../../../../../../translated_images/sv/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Välj **Fine-tune** i navigationsmenyn.

    ![Välj finjustering.](../../../../../../translated_images/sv/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Utför följande uppgifter:

    - Välj **Select task type** till **Chat completion**.
    - Välj **+ Select data** för att ladda upp **Träningsdata**.
    - Välj valideringsdata-typ till **Provide different validation data**.
    - Välj **+ Select data** för att ladda upp **Valideringsdata**.

    ![Fyll i finjusteringssidan.](../../../../../../translated_images/sv/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Du kan välja **Advanced settings** för att anpassa inställningar som **learning_rate** och **lr_scheduler_type** för att optimera finjusteringsprocessen efter dina specifika behov.

1. Välj **Finish**.

1. I denna övning finjusterade du framgångsrikt Phi-3-modellen med Azure Machine Learning. Observera att finjusteringsprocessen kan ta betydande tid. Efter att ha startat finjusteringsjobbet måste du vänta på att det ska slutföras. Du kan övervaka jobbstatus genom att gå till fliken Jobs på vänster sida i din Azure Machine Learning-arbetsyta. I nästa del kommer du att distribuera den finjusterade modellen och integrera den med Prompt flow.

    ![Se finjusteringsjobb.](../../../../../../translated_images/sv/06-08-output.2bd32e59930672b1.webp)

### Distribuera den finjusterade Phi-3-modellen

För att integrera den finjusterade Phi-3-modellen med Prompt flow, måste du distribuera modellen för att göra den tillgänglig för realtidsinferenz. Denna process innefattar att registrera modellen, skapa en online-endpoint och distribuera modellen.

I denna övning kommer du att:

- Registrera den finjusterade modellen i Azure Machine Learning-arbetsytan.
- Skapa en online-endpoint.
- Distribuera den registrerade finjusterade Phi-3-modellen.

#### Registrera den finjusterade modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Välj den Azure Machine Learning-arbetsyta som du skapade.

    ![Välj arbetsyta som du skapade.](../../../../../../translated_images/sv/06-04-select-workspace.a92934ac04f4f181.webp)

1. Välj **Models** från fliken till vänster.
1. Välj **+ Register**.
1. Välj **From a job output**.

    ![Registrera modell.](../../../../../../translated_images/sv/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Välj det jobb som du skapade.

    ![Välj jobb.](../../../../../../translated_images/sv/07-02-select-job.3e2e1144cd6cd093.webp)

1. Välj **Next**.

1. Välj **Model type** till **MLflow**.

1. Säkerställ att **Job output** är valt; det ska väljas automatiskt.

    ![Välj output.](../../../../../../translated_images/sv/07-03-select-output.4cf1a0e645baea1f.webp)

2. Välj **Next**.

3. Välj **Register**.

    ![Välj registrera.](../../../../../../translated_images/sv/07-04-register.fd82a3b293060bc7.webp)

4. Du kan se din registrerade modell genom att navigera till menyn **Models** från fliken till vänster.

    ![Registrerad modell.](../../../../../../translated_images/sv/07-05-registered-model.7db9775f58dfd591.webp)

#### Distribuera den finjusterade modellen

1. Navigera till den Azure Machine Learning-arbetsyta som du skapade.

1. Välj **Endpoints** från fliken till vänster.

1. Välj **Real-time endpoints** från navigationsmenyn.

    ![Skapa endpoint.](../../../../../../translated_images/sv/07-06-create-endpoint.1ba865c606551f09.webp)

1. Välj **Create**.

1. välj den registrerade modellen som du skapade.

    ![Välj registrerad modell.](../../../../../../translated_images/sv/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Välj **Select**.

1. Utför följande uppgifter:

    - Välj **Virtual machine** till *Standard_NC6s_v3*.
    - Välj **Instance count** som du vill använda. Till exempel *1*.
    - Välj **Endpoint** till **New** för att skapa en endpoint.
    - Ange **Endpoint name**. Det måste vara unikt.
    - Ange **Deployment name**. Det måste vara unikt.

    ![Fyll i distributionsinställningarna.](../../../../../../translated_images/sv/07-08-deployment-setting.43ddc4209e673784.webp)

1. Välj **Deploy**.

> [!WARNING]
> För att undvika extra kostnader på ditt konto, se till att ta bort den skapade endpointen i Azure Machine Learning-arbetsytan.
>

#### Kontrollera distributionsstatus i Azure Machine Learning Workspace

1. Navigera till Azure Machine Learning-arbetsytan som du skapade.

1. Välj **Endpoints** från fliken till vänster.

1. Välj den endpoint som du skapade.

    ![Välj endpoints](../../../../../../translated_images/sv/07-09-check-deployment.325d18cae8475ef4.webp)

1. På denna sida kan du hantera endpoints under distributionsprocessen.

> [!NOTE]
> När distributionen är klar, se till att **Live traffic** är satt till **100%**. Om det inte är det, välj **Update traffic** för att justera trafikinställningarna. Observera att du inte kan testa modellen om trafiken är satt till 0%.
>
> ![Sätt trafik.](../../../../../../translated_images/sv/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenario 3: Integrera med Prompt flow och chatta med din anpassade modell i Microsoft Foundry

### Integrera den anpassade Phi-3-modellen med Prompt flow

Efter att ha framgångsrikt distribuerat din finjusterade modell kan du nu integrera den med Prompt Flow för att använda din modell i realtidsapplikationer, vilket möjliggör en rad interaktiva uppgifter med din anpassade Phi-3-modell.

I denna övning kommer du att:

- Skapa Microsoft Foundry Hub.
- Skapa Microsoft Foundry-projekt.
- Skapa Prompt flow.
- Lägga till en anpassad anslutning för den finjusterade Phi-3-modellen.
- Konfigurera Prompt flow för att chatta med din anpassade Phi-3-modell.

> [!NOTE]
> Du kan också integrera med Promptflow via Azure ML Studio. Samma integrationsprocess kan användas för Azure ML Studio.

#### Skapa Microsoft Foundry Hub

Du måste skapa en Hub innan du skapar projektet. En Hub fungerar som en resursgrupp och låter dig organisera och hantera flera projekt inom Microsoft Foundry.
1. Besök [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Välj **All hubs** från vänstermenyn.

1. Välj **+ New hub** från navigationsmenyn.

    ![Create hub.](../../../../../../translated_images/sv/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Utför följande uppgifter:

    - Ange **Hub name**. Det måste vara ett unikt värde.
    - Välj din Azure **Subscription**.
    - Välj den **Resource group** som ska användas (skapa en ny om det behövs).
    - Välj den **Location** du vill använda.
    - Välj **Connect Azure AI Services** att använda (skapa en ny om det behövs).
    - Välj **Connect Azure AI Search** och **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sv/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Välj **Next**.

#### Skapa Microsoft Foundry-projekt

1. I den Hub du skapade, välj **All projects** från vänstermenyn.

1. Välj **+ New project** från navigationsmenyn.

    ![Select new project.](../../../../../../translated_images/sv/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Ange **Project name**. Det måste vara ett unikt värde.

    ![Create project.](../../../../../../translated_images/sv/08-05-create-project.4d97f0372f03375a.webp)

1. Välj **Create a project**.

#### Lägg till en anpassad anslutning för den finjusterade Phi-3-modellen

För att integrera din anpassade Phi-3-modell med Prompt flow behöver du spara modellens endpoint och nyckel i en anpassad anslutning. Denna inställning säkerställer tillgång till din anpassade Phi-3-modell i Prompt flow.

#### Ställ in api-nyckel och endpoint-URI för den finjusterade Phi-3-modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigera till den Azure Machine learning-arbetsyta som du skapade.

1. Välj **Endpoints** från vänstermenyn.

    ![Select endpoints.](../../../../../../translated_images/sv/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Välj den endpoint som du skapade.

    ![Select endpoints.](../../../../../../translated_images/sv/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Välj **Consume** från navigationsmenyn.

1. Kopiera din **REST endpoint** och **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sv/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Lägg till den anpassade anslutningen

1. Besök [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigera till det Microsoft Foundry-projekt som du skapade.

1. I projektet du skapade, välj **Settings** från vänstermenyn.

1. Välj **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sv/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Välj **Custom keys** från navigationsmenyn.

    ![Select custom keys.](../../../../../../translated_images/sv/08-10-select-custom-keys.856f6b2966460551.webp)

1. Utför följande uppgifter:

    - Välj **+ Add key value pairs**.
    - För nyckelnamn, ange **endpoint** och klistra in endpointen du kopierade från Azure ML Studio i värdefältet.
    - Välj **+ Add key value pairs** igen.
    - För nyckelnamn, ange **key** och klistra in nyckeln du kopierade från Azure ML Studio i värdefältet.
    - Efter att ha lagt till nycklarna, välj **is secret** för att förhindra att nyckeln exponeras.

    ![Add connection.](../../../../../../translated_images/sv/08-11-add-connection.785486badb4d2d26.webp)

1. Välj **Add connection**.

#### Skapa Prompt flow

Du har lagt till en anpassad anslutning i Microsoft Foundry. Nu ska vi skapa ett Prompt flow med följande steg. Sedan kommer du ansluta detta Prompt flow till den anpassade anslutningen så att du kan använda den finjusterade modellen inom Prompt flow.

1. Navigera till det Microsoft Foundry-projekt som du skapade.

1. Välj **Prompt flow** från vänstermenyn.

1. Välj **+ Create** från navigationsmenyn.

    ![Select Promptflow.](../../../../../../translated_images/sv/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Välj **Chat flow** från navigationsmenyn.

    ![Select chat flow.](../../../../../../translated_images/sv/08-13-select-flow-type.2ec689b22da32591.webp)

1. Ange **Folder name** att använda.

    ![Enter name.](../../../../../../translated_images/sv/08-14-enter-name.ff9520fefd89f40d.webp)

2. Välj **Create**.

#### Konfigurera Prompt flow för att chatta med din anpassade Phi-3-modell

Du behöver integrera den finjusterade Phi-3-modellen i ett Prompt flow. Den befintliga Prompt flow som tillhandahålls är dock inte designad för detta ändamål. Därför måste du designa om Prompt flow för att möjliggöra integration av den anpassade modellen.

1. I Prompt flow, utför följande uppgifter för att bygga om det befintliga flödet:

    - Välj **Raw file mode**.
    - Radera all befintlig kod i *flow.dag.yml*-filen.
    - Lägg till följande kod i *flow.dag.yml*-filen.

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

    - Välj **Save**.

    ![Select raw file mode.](../../../../../../translated_images/sv/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Lägg till följande kod i *integrate_with_promptflow.py*-filen för att använda den anpassade Phi-3-modellen i Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logginställning
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

        # "connection" är namnet på den anpassade anslutningen, "endpoint", "key" är nycklarna i den anpassade anslutningen
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
            
            # Logga hela JSON-svaret
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

    ![Paste prompt flow code.](../../../../../../translated_images/sv/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> För mer detaljerad information om att använda Prompt flow i Microsoft Foundry kan du referera till [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Välj **Chat input**, **Chat output** för att aktivera chatt med din modell.

    ![Input Output.](../../../../../../translated_images/sv/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Nu är du redo att chatta med din anpassade Phi-3-modell. I nästa övning lär du dig hur du startar Prompt flow och använder det för att chatta med din finjusterade Phi-3-modell.

> [!NOTE]
>
> Det ombyggda flödet bör se ut som bilden nedan:
>
> ![Flow example.](../../../../../../translated_images/sv/08-18-graph-example.d6457533952e690c.webp)
>

### Chatta med din anpassade Phi-3-modell

Nu när du har finjusterat och integrerat din anpassade Phi-3-modell med Prompt flow är du redo att börja interagera med den. Den här övningen guidar dig genom processen att ställa in och initiera en chatt med din modell med hjälp av Prompt flow. Genom att följa dessa steg kan du fullt ut använda kapabiliteterna hos din finjusterade Phi-3-modell för olika uppgifter och samtal.

- Chatta med din anpassade Phi-3-modell med hjälp av Prompt flow.

#### Starta Prompt flow

1. Välj **Start compute sessions** för att starta Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sv/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Välj **Validate and parse input** för att förnya parametrar.

    ![Validate input.](../../../../../../translated_images/sv/09-02-validate-input.317c76ef766361e9.webp)

1. Välj **Value** för **connection** till den anpassade anslutning du skapade. Till exempel, *connection*.

    ![Connection.](../../../../../../translated_images/sv/09-03-select-connection.99bdddb4b1844023.webp)

#### Chatta med din anpassade modell

1. Välj **Chat**.

    ![Select chat.](../../../../../../translated_images/sv/09-04-select-chat.61936dce6612a1e6.webp)

1. Här är ett exempel på resultat: Nu kan du chatta med din anpassade Phi-3-modell. Det rekommenderas att ställa frågor baserade på den data som användes för finjusteringen.

    ![Chat with prompt flow.](../../../../../../translated_images/sv/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->