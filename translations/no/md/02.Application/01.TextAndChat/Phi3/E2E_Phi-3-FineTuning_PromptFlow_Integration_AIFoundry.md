<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:11:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "no"
}
-->
# Finjuster og integrer tilpassede Phi-3-modeller med Prompt flow i Azure AI Foundry

Denne ende-til-ende (E2E) eksempelen er basert på veiledningen "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community. Den introduserer prosessene for finjustering, distribusjon og integrasjon av tilpassede Phi-3-modeller med Prompt flow i Azure AI Foundry.  
I motsetning til E2E-eksempelet, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", som involverte lokal kjøring av kode, fokuserer denne veiledningen helt på finjustering og integrasjon av modellen din innen Azure AI / ML Studio.

## Oversikt

I denne E2E-eksempelen vil du lære hvordan du finjusterer Phi-3-modellen og integrerer den med Prompt flow i Azure AI Foundry. Ved å bruke Azure AI / ML Studio vil du etablere en arbeidsflyt for distribusjon og bruk av tilpassede AI-modeller. Denne E2E-eksempelen er delt inn i tre scenarier:

**Scenario 1: Sett opp Azure-ressurser og forbered for finjustering**

**Scenario 2: Finjuster Phi-3-modellen og distribuer i Azure Machine Learning Studio**

**Scenario 3: Integrer med Prompt flow og chat med din tilpassede modell i Azure AI Foundry**

Her er en oversikt over denne E2E-eksempelen.

![Phi-3-FineTuning_PromptFlow_Integration Oversikt.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.no.png)

### Innholdsfortegnelse

1. **[Scenario 1: Sett opp Azure-ressurser og forbered for finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Opprett et Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Be om GPU-kvoter i Azure-abonnementet](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Legg til rolle-tilordning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Sett opp prosjekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Forbered datasett for finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Finjuster Phi-3-modellen og distribuer i Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Finjuster Phi-3-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuer den finjusterte Phi-3-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrer med Prompt flow og chat med din tilpassede modell i Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrer den tilpassede Phi-3-modellen med Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat med din tilpassede Phi-3-modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Sett opp Azure-ressurser og forbered for finjustering

### Opprett et Azure Machine Learning Workspace

1. Skriv *azure machine learning* i **søkelinjen** øverst på portalsiden og velg **Azure Machine Learning** fra alternativene som vises.

    ![Skriv azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.no.png)

2. Velg **+ Opprett** i navigasjonsmenyen.

3. Velg **Nytt workspace** i navigasjonsmenyen.

    ![Velg nytt workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.no.png)

4. Utfør følgende oppgaver:

    - Velg ditt Azure **Abonnement**.
    - Velg **Ressursgruppe** som skal brukes (opprett en ny om nødvendig).
    - Skriv inn **Workspace-navn**. Det må være en unik verdi.
    - Velg **Region** du ønsker å bruke.
    - Velg **Lagringskonto** som skal brukes (opprett en ny om nødvendig).
    - Velg **Nøkkelvalv** som skal brukes (opprett en ny om nødvendig).
    - Velg **Application insights** som skal brukes (opprett en ny om nødvendig).
    - Velg **Container registry** som skal brukes (opprett en ny om nødvendig).

    ![Fyll ut Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.no.png)

5. Velg **Gjennomgå + opprett**.

6. Velg **Opprett**.

### Be om GPU-kvoter i Azure-abonnementet

I denne veiledningen lærer du hvordan du finjusterer og distribuerer en Phi-3-modell ved bruk av GPUer. For finjustering bruker du *Standard_NC24ads_A100_v4*-GPU, som krever en kvotebegjæring. For distribusjon bruker du *Standard_NC6s_v3*-GPU, som også krever kvotebegjæring.

> [!NOTE]
>
> Kun Pay-As-You-Go-abonnementer (standard abonnementstype) kvalifiserer for GPU-tildeling; fordelabonnementer støttes foreløpig ikke.
>

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Utfør følgende for å be om kvote for *Standard NCADSA100v4 Family*:

    - Velg **Kvoter** i venstre sidefelt.
    - Velg **Virtuell maskinfamilie** som skal brukes. For eksempel, velg **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, som inkluderer *Standard_NC24ads_A100_v4*-GPU.
    - Velg **Be om kvote** i navigasjonsmenyen.

        ![Be om kvote.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.no.png)

    - På siden for kvotebegjæring, skriv inn **Nytt kjernegrense** du ønsker å bruke. For eksempel 24.
    - Velg **Send inn** for å be om GPU-kvoten.

1. Utfør følgende for å be om kvote for *Standard NCSv3 Family*:

    - Velg **Kvoter** i venstre sidefelt.
    - Velg **Virtuell maskinfamilie** som skal brukes. For eksempel, velg **Standard NCSv3 Family Cluster Dedicated vCPUs**, som inkluderer *Standard_NC6s_v3*-GPU.
    - Velg **Be om kvote** i navigasjonsmenyen.
    - På siden for kvotebegjæring, skriv inn **Nytt kjernegrense** du ønsker å bruke. For eksempel 24.
    - Velg **Send inn** for å be om GPU-kvoten.

### Legg til rolle-tilordning

For å kunne finjustere og distribuere modellene dine, må du først opprette en User Assigned Managed Identity (UAI) og tildele den riktige tillatelser. Denne UAI vil bli brukt for autentisering under distribusjon.

#### Opprett User Assigned Managed Identity (UAI)

1. Skriv *managed identities* i **søkelinjen** øverst på portalsiden og velg **Managed Identities** fra alternativene som vises.

    ![Skriv managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.no.png)

1. Velg **+ Opprett**.

    ![Velg opprett.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.no.png)

1. Utfør følgende oppgaver:

    - Velg ditt Azure **Abonnement**.
    - Velg **Ressursgruppe** som skal brukes (opprett en ny om nødvendig).
    - Velg **Region** du ønsker å bruke.
    - Skriv inn **Navn**. Det må være en unik verdi.

    ![Fyll ut for opprettelse.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.no.png)

1. Velg **Gjennomgå + opprett**.

1. Velg **+ Opprett**.

#### Legg til Contributor-rolle til Managed Identity

1. Naviger til Managed Identity-ressursen du opprettet.

1. Velg **Azure rolle-tilordninger** i venstre sidefelt.

1. Velg **+ Legg til rolle-tilordning** i navigasjonsmenyen.

1. På siden for rolle-tilordning, utfør følgende:
    - Velg **Omfang** til **Ressursgruppe**.
    - Velg ditt Azure **Abonnement**.
    - Velg **Ressursgruppe** som skal brukes.
    - Velg **Rolle** til **Bidragsyter**.

    ![Fyll ut contributor-rolle.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.no.png)

2. Velg **Lagre**.

#### Legg til Storage Blob Data Reader-rolle til Managed Identity

1. Skriv *storage accounts* i **søkelinjen** øverst på portalsiden og velg **Storage accounts** fra alternativene som vises.

    ![Skriv storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.no.png)

1. Velg lagringskontoen som er knyttet til Azure Machine Learning workspace du opprettet. For eksempel *finetunephistorage*.

1. Utfør følgende for å navigere til siden for å legge til rolle-tilordning:

    - Naviger til den opprettede Azure Storage-kontoen.
    - Velg **Tilgangskontroll (IAM)** i venstre sidefelt.
    - Velg **+ Legg til** i navigasjonsmenyen.
    - Velg **Legg til rolle-tilordning** i navigasjonsmenyen.

    ![Legg til rolle.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.no.png)

1. På siden for rolle-tilordning, utfør følgende:

    - I Rolle-søkefeltet, skriv *Storage Blob Data Reader* og velg **Storage Blob Data Reader** fra listen.
    - Velg **Neste**.
    - På Medlems-siden, velg **Tildel tilgang til** **Managed identity**.
    - Velg **+ Velg medlemmer**.
    - Velg ditt Azure **Abonnement**.
    - Velg **Managed identity** til **Manage Identity**.
    - Velg den Managed Identity du opprettet, for eksempel *finetunephi-managedidentity*.
    - Velg **Velg**.

    ![Velg managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.no.png)

1. Velg **Gjennomgå + tildel**.

#### Legg til AcrPull-rolle til Managed Identity

1. Skriv *container registries* i **søkelinjen** øverst på portalsiden og velg **Container registries** fra alternativene som vises.

    ![Skriv container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.no.png)

1. Velg container registry som er knyttet til Azure Machine Learning workspace. For eksempel *finetunephicontainerregistry*

1. Utfør følgende for å navigere til siden for å legge til rolle-tilordning:

    - Velg **Tilgangskontroll (IAM)** i venstre sidefelt.
    - Velg **+ Legg til** i navigasjonsmenyen.
    - Velg **Legg til rolle-tilordning** i navigasjonsmenyen.

1. På siden for rolle-tilordning, utfør følgende:

    - I Rolle-søkefeltet, skriv *AcrPull* og velg **AcrPull** fra listen.
    - Velg **Neste**.
    - På Medlems-siden, velg **Tildel tilgang til** **Managed identity**.
    - Velg **+ Velg medlemmer**.
    - Velg ditt Azure **Abonnement**.
    - Velg **Managed identity** til **Manage Identity**.
    - Velg den Managed Identity du opprettet, for eksempel *finetunephi-managedidentity*.
    - Velg **Velg**.
    - Velg **Gjennomgå + tildel**.

### Sett opp prosjekt

For å laste ned datasettene som trengs for finjustering, setter du opp et lokalt miljø.

I denne øvelsen vil du

- Opprette en mappe å jobbe i.
- Opprette et virtuelt miljø.
- Installere nødvendige pakker.
- Lage en fil *download_dataset.py* for å laste ned datasettet.

#### Opprett en mappe å jobbe i

1. Åpne et terminalvindu og skriv følgende kommando for å opprette en mappe kalt *finetune-phi* i standardmappen.

    ```console
    mkdir finetune-phi
    ```

2. Skriv følgende kommando i terminalen for å navigere til *finetune-phi* mappen du opprettet.

    ```console
    cd finetune-phi
    ```

#### Opprett et virtuelt miljø

1. Skriv følgende kommando i terminalen for å opprette et virtuelt miljø kalt *.venv*.

    ```console
    python -m venv .venv
    ```

2. Skriv følgende kommando i terminalen for å aktivere det virtuelle miljøet.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Hvis det fungerte, skal du se *(.venv)* før kommandoprompten.

#### Installer nødvendige pakker

1. Skriv følgende kommandoer i terminalen for å installere nødvendige pakker.

    ```console
    pip install datasets==2.19.1
    ```

#### Lag `download_dataset.py`

> [!NOTE]
> Fullstendig mappestruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Åpne **Visual Studio Code**.

1. Velg **Fil** i menylinjen.

1. Velg **Åpne mappe**.

1. Velg *finetune-phi* mappen du opprettet, som ligger i *C:\Users\yourUserName\finetune-phi*.

    ![Velg mappen du opprettet.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.no.png)

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny fil** for å lage en ny fil kalt *download_dataset.py*.

    ![Lag en ny fil.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.no.png)

### Forbered datasett for finjustering

I denne øvelsen skal du kjøre filen *download_dataset.py* for å laste ned *ultrachat_200k* datasettene til ditt lokale miljø. Disse datasettene skal du bruke til å finjustere Phi-3-modellen i Azure Machine Learning.

I denne øvelsen vil du:

- Legge til kode i *download_dataset.py* for å laste ned datasettene.
- Kjøre *download_dataset.py* for å laste ned datasettene til ditt lokale miljø.

#### Last ned datasettet ditt med *download_dataset.py*

1. Åpne *download_dataset.py* filen i Visual Studio Code.

1. Legg til følgende kode i *download_dataset.py* filen.

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

1. Skriv følgende kommando i terminalen for å kjøre skriptet og laste ned datasettet til ditt lokale miljø.

    ```console
    python download_dataset.py
    ```

1. Bekreft at datasettene ble lagret korrekt i din lokale *finetune-phi/data* mappe.

> [!NOTE]
>
> #### Merknad om dataset-størrelse og finjusteringstid
>
> I denne veiledningen bruker du kun 1 % av datasettet (`split='train[:1%]'`). Dette reduserer datamengden betydelig og gjør både opplasting og finjustering raskere. Du kan justere prosentandelen for å finne balansen mellom treningstid og modellens ytelse. Å bruke et mindre datasett reduserer tiden som trengs for finjustering, noe som gjør prosessen mer håndterbar for en veiledning.

## Scenario 2: Finjuster Phi-3-modellen og distribuer i Azure Machine Learning Studio

### Finjuster Phi-3-modellen

I denne øvelsen skal du finjustere Phi-3-modellen i Azure Machine Learning Studio.

I denne øvelsen vil du:

- Opprette en databehandlerklynge for finjustering.
- Finjustere Phi-3-modellen i Azure Machine Learning Studio.

#### Opprett databehandlerklynge for finjustering
1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Velg **Compute** fra fanen på venstre side.

1. Velg **Compute clusters** fra navigasjonsmenyen.

1. Velg **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.no.png)

1. Gjør følgende:

    - Velg **Region** du ønsker å bruke.
    - Velg **Virtual machine tier** til **Dedicated**.
    - Velg **Virtual machine type** til **GPU**.
    - Velg filteret for **Virtual machine size** til **Select from all options**.
    - Velg **Virtual machine size** til **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.no.png)

1. Velg **Next**.

1. Gjør følgende:

    - Skriv inn **Compute name**. Det må være en unik verdi.
    - Velg **Minimum number of nodes** til **0**.
    - Velg **Maximum number of nodes** til **1**.
    - Velg **Idle seconds before scale down** til **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.no.png)

1. Velg **Create**.

#### Finjuster Phi-3-modellen

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Velg Azure Machine Learning-arbeidsområdet du opprettet.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.no.png)

1. Gjør følgende:

    - Velg **Model catalog** fra fanen på venstre side.
    - Skriv *phi-3-mini-4k* i **søkelinjen** og velg **Phi-3-mini-4k-instruct** fra alternativene som dukker opp.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.no.png)

1. Velg **Fine-tune** fra navigasjonsmenyen.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.no.png)

1. Gjør følgende:

    - Velg **Select task type** til **Chat completion**.
    - Velg **+ Select data** for å laste opp **Traning data**.
    - Velg opplastningstype for valideringsdata til **Provide different validation data**.
    - Velg **+ Select data** for å laste opp **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.no.png)

    > [!TIP]
    >
    > Du kan velge **Advanced settings** for å tilpasse innstillinger som **learning_rate** og **lr_scheduler_type** for å optimalisere finjusteringen etter dine behov.

1. Velg **Finish**.

1. I denne øvelsen har du finjustert Phi-3-modellen med Azure Machine Learning. Vær oppmerksom på at finjusteringsprosessen kan ta en god del tid. Etter at du har startet finjusteringsjobben, må du vente på at den fullføres. Du kan følge statusen for finjusteringsjobben ved å gå til fanen Jobs i venstre meny i Azure Machine Learning-arbeidsområdet ditt. I neste serie vil du distribuere den finjusterte modellen og integrere den med Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.no.png)

### Distribuer den finjusterte Phi-3-modellen

For å integrere den finjusterte Phi-3-modellen med Prompt flow, må du distribuere modellen slik at den er tilgjengelig for sanntidsinferenz. Denne prosessen innebærer å registrere modellen, opprette en online-endepunkt og distribuere modellen.

I denne øvelsen vil du:

- Registrere den finjusterte modellen i Azure Machine Learning-arbeidsområdet.
- Opprette et online-endepunkt.
- Distribuere den registrerte finjusterte Phi-3-modellen.

#### Registrer den finjusterte modellen

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Velg Azure Machine Learning-arbeidsområdet du opprettet.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.no.png)

1. Velg **Models** fra fanen på venstre side.
1. Velg **+ Register**.
1. Velg **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.no.png)

1. Velg jobben du opprettet.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.no.png)

1. Velg **Next**.

1. Velg **Model type** til **MLflow**.

1. Sørg for at **Job output** er valgt; dette skal være valgt automatisk.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.no.png)

2. Velg **Next**.

3. Velg **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.no.png)

4. Du kan se den registrerte modellen ved å gå til menyen **Models** på venstre side.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.no.png)

#### Distribuer den finjusterte modellen

1. Gå til Azure Machine Learning-arbeidsområdet du opprettet.

1. Velg **Endpoints** fra fanen på venstre side.

1. Velg **Real-time endpoints** fra navigasjonsmenyen.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.no.png)

1. Velg **Create**.

1. Velg den registrerte modellen du opprettet.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.no.png)

1. Velg **Select**.

1. Gjør følgende:

    - Velg **Virtual machine** til *Standard_NC6s_v3*.
    - Velg antall instanser du ønsker. For eksempel *1*.
    - Velg **Endpoint** til **New** for å opprette et endepunkt.
    - Skriv inn **Endpoint name**. Det må være unikt.
    - Skriv inn **Deployment name**. Det må være unikt.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.no.png)

1. Velg **Deploy**.

> [!WARNING]
> For å unngå ekstra kostnader, sørg for å slette det opprettede endepunktet i Azure Machine Learning-arbeidsområdet når det ikke lenger er i bruk.
>

#### Sjekk distribusjonsstatus i Azure Machine Learning Workspace

1. Gå til Azure Machine Learning-arbeidsområdet du opprettet.

1. Velg **Endpoints** fra fanen på venstre side.

1. Velg endepunktet du opprettet.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.no.png)

1. På denne siden kan du administrere endepunktene under distribusjonsprosessen.

> [!NOTE]
> Når distribusjonen er ferdig, sørg for at **Live traffic** er satt til **100%**. Hvis ikke, velg **Update traffic** for å justere trafikkinnstillingene. Merk at du ikke kan teste modellen hvis trafikken er satt til 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.no.png)
>

## Scenario 3: Integrer med Prompt flow og chat med din tilpassede modell i Azure AI Foundry

### Integrer den tilpassede Phi-3-modellen med Prompt flow

Etter at du har distribuert den finjusterte modellen, kan du nå integrere den med Prompt Flow for å bruke modellen i sanntidsapplikasjoner, noe som åpner for ulike interaktive oppgaver med din tilpassede Phi-3-modell.

I denne øvelsen vil du:

- Opprette Azure AI Foundry Hub.
- Opprette Azure AI Foundry-prosjekt.
- Opprette Prompt flow.
- Legge til en egendefinert tilkobling for den finjusterte Phi-3-modellen.
- Sette opp Prompt flow for å chatte med din tilpassede Phi-3-modell.

> [!NOTE]
> Du kan også integrere med Promptflow via Azure ML Studio. Den samme integrasjonsprosessen gjelder for Azure ML Studio.

#### Opprett Azure AI Foundry Hub

Du må opprette en Hub før du kan opprette et prosjekt. En Hub fungerer som en Resource Group, og lar deg organisere og administrere flere prosjekter innen Azure AI Foundry.

1. Besøk [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Velg **All hubs** fra venstre fane.

1. Velg **+ New hub** fra navigasjonsmenyen.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.no.png)

1. Gjør følgende:

    - Skriv inn **Hub name**. Det må være unikt.
    - Velg Azure **Subscription**.
    - Velg **Resource group** som skal brukes (opprett ny om nødvendig).
    - Velg **Location** du ønsker å bruke.
    - Velg **Connect Azure AI Services** som skal brukes (opprett ny om nødvendig).
    - Velg **Connect Azure AI Search** til **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.no.png)

1. Velg **Next**.

#### Opprett Azure AI Foundry-prosjekt

1. I Hub-en du opprettet, velg **All projects** fra venstre fane.

1. Velg **+ New project** fra navigasjonsmenyen.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.no.png)

1. Skriv inn **Project name**. Det må være unikt.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.no.png)

1. Velg **Create a project**.

#### Legg til egendefinert tilkobling for den finjusterte Phi-3-modellen

For å integrere din tilpassede Phi-3-modell med Prompt flow, må du lagre modellens endepunkt og nøkkel i en egendefinert tilkobling. Dette sikrer tilgang til modellen i Prompt flow.

#### Sett API-nøkkel og endepunkt-URI for den finjusterte Phi-3-modellen

1. Besøk [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Naviger til Azure Machine Learning-arbeidsområdet du opprettet.

1. Velg **Endpoints** fra venstre fane.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.no.png)

1. Velg endepunktet du opprettet.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.no.png)

1. Velg **Consume** fra navigasjonsmenyen.

1. Kopier din **REST endpoint** og **Primary key**.
![Kopier API-nøkkel og endepunkt-URI.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.no.png)

#### Legg til egendefinert tilkobling

1. Besøk [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. I prosjektet du opprettet, velg **Innstillinger** fra fanen på venstre side.

1. Velg **+ Ny tilkobling**.

    ![Velg ny tilkobling.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.no.png)

1. Velg **Egendefinerte nøkler** fra navigasjonsmenyen.

    ![Velg egendefinerte nøkler.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.no.png)

1. Utfør følgende oppgaver:

    - Velg **+ Legg til nøkkel-verdi-par**.
    - For nøkkelnavnet, skriv inn **endpoint** og lim inn endepunktet du kopierte fra Azure ML Studio i verdifeltet.
    - Velg **+ Legg til nøkkel-verdi-par** igjen.
    - For nøkkelnavnet, skriv inn **key** og lim inn nøkkelen du kopierte fra Azure ML Studio i verdifeltet.
    - Etter å ha lagt til nøklene, velg **er hemmelig** for å hindre at nøkkelen eksponeres.

    ![Legg til tilkobling.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.no.png)

1. Velg **Legg til tilkobling**.

#### Opprett Prompt flow

Du har lagt til en egendefinert tilkobling i Azure AI Foundry. Nå skal vi opprette en Prompt flow ved å følge stegene nedenfor. Deretter kobler du denne Prompt flow til den egendefinerte tilkoblingen slik at du kan bruke den finjusterte modellen i Prompt flow.

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. Velg **Prompt flow** fra fanen på venstre side.

1. Velg **+ Opprett** fra navigasjonsmenyen.

    ![Velg Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.no.png)

1. Velg **Chat flow** fra navigasjonsmenyen.

    ![Velg chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.no.png)

1. Skriv inn **Mappenavn** som skal brukes.

    ![Skriv inn navn.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.no.png)

2. Velg **Opprett**.

#### Sett opp Prompt flow for å chatte med din egendefinerte Phi-3-modell

Du må integrere den finjusterte Phi-3-modellen i en Prompt flow. Den eksisterende Prompt flow som følger med, er imidlertid ikke laget for dette formålet. Derfor må du redesigne Prompt flow for å muliggjøre integrasjon av den egendefinerte modellen.

1. I Prompt flow gjør du følgende for å bygge opp den eksisterende flyten på nytt:

    - Velg **Rå filmodus**.
    - Slett all eksisterende kode i *flow.dag.yml*-filen.
    - Legg til følgende kode i *flow.dag.yml*-filen.

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

    - Velg **Lagre**.

    ![Velg rå filmodus.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.no.png)

1. Legg til følgende kode i *integrate_with_promptflow.py*-filen for å bruke den egendefinerte Phi-3-modellen i Prompt flow.

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

    ![Lim inn Prompt flow-kode.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.no.png)

> [!NOTE]
> For mer detaljert informasjon om bruk av Prompt flow i Azure AI Foundry, kan du se [Prompt flow i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Velg **Chat input**, **Chat output** for å aktivere chatting med modellen din.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.no.png)

1. Nå er du klar til å chatte med din egendefinerte Phi-3-modell. I neste øvelse lærer du hvordan du starter Prompt flow og bruker den til å chatte med din finjusterte Phi-3-modell.

> [!NOTE]
>
> Den ombygde flyten skal se ut som bildet nedenfor:
>
> ![Flyteksempel.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.no.png)
>

### Chat med din egendefinerte Phi-3-modell

Nå som du har finjustert og integrert din egendefinerte Phi-3-modell med Prompt flow, er du klar til å begynne å samhandle med den. Denne øvelsen vil veilede deg gjennom prosessen med å sette opp og starte en chat med modellen din ved hjelp av Prompt flow. Ved å følge disse stegene vil du kunne utnytte mulighetene til din finjusterte Phi-3-modell fullt ut for ulike oppgaver og samtaler.

- Chat med din egendefinerte Phi-3-modell ved hjelp av Prompt flow.

#### Start Prompt flow

1. Velg **Start compute sessions** for å starte Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.no.png)

1. Velg **Validate and parse input** for å oppdatere parametere.

    ![Valider input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.no.png)

1. Velg **Value** for **connection** til den egendefinerte tilkoblingen du opprettet. For eksempel *connection*.

    ![Tilkobling.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.no.png)

#### Chat med din egendefinerte modell

1. Velg **Chat**.

    ![Velg chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.no.png)

1. Her er et eksempel på resultatene: Nå kan du chatte med din egendefinerte Phi-3-modell. Det anbefales å stille spørsmål basert på dataene som ble brukt til finjusteringen.

    ![Chat med prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.no.png)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.