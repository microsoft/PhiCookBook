<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:49:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "sl"
}
-->
# Prilagodite in integrirajte lastne modele Phi-3 s Prompt flow

Ta celovit (E2E) primer temelji na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community. Predstavlja postopke prilagajanja, nameščanja in integracije lastnih modelov Phi-3 s Prompt flow.

## Pregled

V tem E2E primeru se boste naučili, kako prilagoditi model Phi-3 in ga integrirati s Prompt flow. Z uporabo Azure Machine Learning in Prompt flow boste vzpostavili delovni tok za nameščanje in uporabo lastnih AI modelov. Ta E2E primer je razdeljen na tri scenarije:

**Scenarij 1: Nastavitev Azure virov in priprava na prilagajanje**

**Scenarij 2: Prilagoditev modela Phi-3 in nameščanje v Azure Machine Learning Studio**

**Scenarij 3: Integracija s Prompt flow in pogovor z vašim lastnim modelom**

Tukaj je pregled tega E2E primera.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.sl.png)

### Kazalo

1. **[Scenarij 1: Nastavitev Azure virov in priprava na prilagajanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ustvarite Azure Machine Learning delovno okolje](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Zahtevajte GPU kvote v Azure naročnini](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dodajte dodelitev vlog](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nastavite projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pripravite podatkovni niz za prilagajanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarij 2: Prilagodite model Phi-3 in ga namestite v Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Nastavite Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Prilagodite model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Namestite prilagojeni model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarij 3: Integrirajte s Prompt flow in se pogovarjajte z vašim lastnim modelom](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrirajte lastni model Phi-3 s Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pogovarjajte se z vašim lastnim modelom](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenarij 1: Nastavitev Azure virov in priprava na prilagajanje

### Ustvarite Azure Machine Learning delovno okolje

1. V iskalno vrstico na vrhu portala vpišite *azure machine learning* in izberite **Azure Machine Learning** med prikazanimi možnostmi.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.sl.png)

1. Izberite **+ Create** v navigacijskem meniju.

1. Izberite **New workspace** v navigacijskem meniju.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.sl.png)

1. Izvedite naslednje korake:

    - Izberite vašo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti (po potrebi ustvarite novo).
    - Vnesite **Workspace Name**. Mora biti edinstveno ime.
    - Izberite **Region**, ki ga želite uporabiti.
    - Izberite **Storage account**, ki ga želite uporabiti (po potrebi ustvarite novega).
    - Izberite **Key vault**, ki ga želite uporabiti (po potrebi ustvarite novega).
    - Izberite **Application insights**, ki ga želite uporabiti (po potrebi ustvarite novega).
    - Izberite **Container registry**, ki ga želite uporabiti (po potrebi ustvarite novega).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.sl.png)

1. Izberite **Review + Create**.

1. Izberite **Create**.

### Zahtevajte GPU kvote v Azure naročnini

V tem E2E primeru boste za prilagajanje uporabili *Standard_NC24ads_A100_v4 GPU*, ki zahteva zahtevo za kvoto, za nameščanje pa *Standard_E4s_v3* CPU, ki kvote ne zahteva.

> [!NOTE]
>
> GPU dodelitev je na voljo samo za naročnine Pay-As-You-Go (standardni tip naročnine); naročnine z ugodnostmi trenutno niso podprte.
>
> Za tiste, ki uporabljajo naročnine z ugodnostmi (kot je Visual Studio Enterprise Subscription) ali želijo hitro preizkusiti postopek prilagajanja in nameščanja, ta vodič ponuja tudi navodila za prilagajanje z minimalnim podatkovnim nizom na CPU. Pomembno pa je vedeti, da so rezultati prilagajanja bistveno boljši, če uporabljate GPU z večjimi podatkovnimi nizi.

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izvedite naslednje korake za zahtevo kvote *Standard NCADSA100v4 Family*:

    - Izberite **Quota** v levem zavihku.
    - Izberite **Virtual machine family**, ki jo želite uporabiti. Na primer, izberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ki vključuje *Standard_NC24ads_A100_v4* GPU.
    - Izberite **Request quota** v navigacijskem meniju.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.sl.png)

    - Na strani Request quota vnesite **New cores limit**, ki ga želite uporabiti. Na primer, 24.
    - Na strani Request quota izberite **Submit** za oddajo zahteve za GPU kvoto.

> [!NOTE]
> Za izbiro primernega GPU ali CPU za vaše potrebe si lahko pomagate z dokumentacijo [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Dodajte dodelitev vlog

Za prilagajanje in nameščanje modelov morate najprej ustvariti User Assigned Managed Identity (UAI) in ji dodeliti ustrezna dovoljenja. Ta UAI bo uporabljena za preverjanje pristnosti med nameščanjem.

#### Ustvarite User Assigned Managed Identity (UAI)

1. V iskalno vrstico na vrhu portala vpišite *managed identities* in izberite **Managed Identities** med prikazanimi možnostmi.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.sl.png)

1. Izberite **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.sl.png)

1. Izvedite naslednje korake:

    - Izberite vašo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti (po potrebi ustvarite novo).
    - Izberite **Region**, ki ga želite uporabiti.
    - Vnesite **Name**. Mora biti edinstveno ime.

1. Izberite **Review + create**.

1. Izberite **+ Create**.

#### Dodajte dodelitev vloge Contributor za Managed Identity

1. Pojdite do vira Managed Identity, ki ste ga ustvarili.

1. Izberite **Azure role assignments** v levem zavihku.

1. Izberite **+Add role assignment** v navigacijskem meniju.

1. Na strani Add role assignment izvedite naslednje korake:
    - Izberite **Scope** na **Resource group**.
    - Izberite vašo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti.
    - Izberite **Role** na **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.sl.png)

1. Izberite **Save**.

#### Dodajte dodelitev vloge Storage Blob Data Reader za Managed Identity

1. V iskalno vrstico na vrhu portala vpišite *storage accounts* in izberite **Storage accounts** med prikazanimi možnostmi.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.sl.png)

1. Izberite storage account, ki je povezan z Azure Machine Learning delovnim okoljem, ki ste ga ustvarili. Na primer, *finetunephistorage*.

1. Izvedite naslednje korake za navigacijo do strani Add role assignment:

    - Pojdite do Azure Storage account, ki ste ga ustvarili.
    - Izberite **Access Control (IAM)** v levem zavihku.
    - Izberite **+ Add** v navigacijskem meniju.
    - Izberite **Add role assignment** v navigacijskem meniju.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.sl.png)

1. Na strani Add role assignment izvedite naslednje korake:

    - V polje za iskanje na strani Role vpišite *Storage Blob Data Reader* in izberite **Storage Blob Data Reader** med prikazanimi možnostmi.
    - Izberite **Next**.
    - Na strani Members izberite **Assign access to** **Managed identity**.
    - Izberite **+ Select members**.
    - Na strani Select managed identities izberite vašo Azure **Subscription**.
    - Izberite **Managed identity** kot **Manage Identity**.
    - Izberite Manage Identity, ki ste jo ustvarili. Na primer, *finetunephi-managedidentity*.
    - Izberite **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.sl.png)

1. Izberite **Review + assign**.

#### Dodajte dodelitev vloge AcrPull za Managed Identity

1. V iskalno vrstico na vrhu portala vpišite *container registries* in izberite **Container registries** med prikazanimi možnostmi.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.sl.png)

1. Izberite container registry, ki je povezan z Azure Machine Learning delovnim okoljem. Na primer, *finetunephicontainerregistries*

1. Izvedite naslednje korake za navigacijo do strani Add role assignment:

    - Izberite **Access Control (IAM)** v levem zavihku.
    - Izberite **+ Add** v navigacijskem meniju.
    - Izberite **Add role assignment** v navigacijskem meniju.

1. Na strani Add role assignment izvedite naslednje korake:

    - V polje za iskanje na strani Role vpišite *AcrPull* in izberite **AcrPull** med prikazanimi možnostmi.
    - Izberite **Next**.
    - Na strani Members izberite **Assign access to** **Managed identity**.
    - Izberite **+ Select members**.
    - Na strani Select managed identities izberite vašo Azure **Subscription**.
    - Izberite **Managed identity** kot **Manage Identity**.
    - Izberite Manage Identity, ki ste jo ustvarili. Na primer, *finetunephi-managedidentity*.
    - Izberite **Select**.
    - Izberite **Review + assign**.

### Nastavite projekt

Zdaj boste ustvarili mapo za delo in nastavili virtualno okolje za razvoj programa, ki bo komuniciral z uporabniki in uporabljal shranjeno zgodovino pogovorov iz Azure Cosmos DB za oblikovanje odgovorov.

#### Ustvarite mapo za delo

1. Odprite terminal in vnesite naslednji ukaz za ustvarjanje mape z imenom *finetune-phi* v privzeti poti.

    ```console
    mkdir finetune-phi
    ```

1. V terminalu vnesite naslednji ukaz, da se premaknete v mapo *finetune-phi*, ki ste jo ustvarili.

    ```console
    cd finetune-phi
    ```

#### Ustvarite virtualno okolje

1. V terminalu vnesite naslednji ukaz za ustvarjanje virtualnega okolja z imenom *.venv*.

    ```console
    python -m venv .venv
    ```

1. V terminalu vnesite naslednji ukaz za aktivacijo virtualnega okolja.

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> Če je uspelo, bi morali pred pozivom ukaza videti *(.venv)*.
#### Namestite potrebne pakete

1. V terminal vnesite naslednje ukaze za namestitev potrebnih paketov.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Ustvarite projektne datoteke

V tej vaji boste ustvarili osnovne datoteke za naš projekt. Te datoteke vključujejo skripte za prenos podatkovnega nabora, nastavitev okolja Azure Machine Learning, fino prilagajanje modela Phi-3 in nameščanje fino prilagojenega modela. Prav tako boste ustvarili datoteko *conda.yml* za nastavitev okolja za fino prilagajanje.

V tej vaji boste:

- Ustvarili datoteko *download_dataset.py* za prenos podatkovnega nabora.
- Ustvarili datoteko *setup_ml.py* za nastavitev okolja Azure Machine Learning.
- Ustvarili datoteko *fine_tune.py* v mapi *finetuning_dir* za fino prilagajanje modela Phi-3 z uporabo podatkovnega nabora.
- Ustvarili datoteko *conda.yml* za nastavitev okolja za fino prilagajanje.
- Ustvarili datoteko *deploy_model.py* za nameščanje fino prilagojenega modela.
- Ustvarili datoteko *integrate_with_promptflow.py* za integracijo fino prilagojenega modela in izvajanje modela s pomočjo Prompt flow.
- Ustvarili datoteko flow.dag.yml za nastavitev strukture delovnega toka za Prompt flow.
- Ustvarili datoteko *config.py* za vnos Azure podatkov.

> [!NOTE]
>
> Celotna struktura mape:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Odprite **Visual Studio Code**.

1. Izberite **File** v menijski vrstici.

1. Izberite **Open Folder**.

1. Izberite mapo *finetune-phi*, ki ste jo ustvarili, in se nahaja na *C:\Users\yourUserName\finetune-phi*.

    ![Odprite mapo projekta.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.sl.png)

1. V levem delu Visual Studio Code z desnim klikom izberite **New File** in ustvarite novo datoteko z imenom *download_dataset.py*.

1. V levem delu Visual Studio Code z desnim klikom izberite **New File** in ustvarite novo datoteko z imenom *setup_ml.py*.

1. V levem delu Visual Studio Code z desnim klikom izberite **New File** in ustvarite novo datoteko z imenom *deploy_model.py*.

    ![Ustvarite novo datoteko.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.sl.png)

1. V levem delu Visual Studio Code z desnim klikom izberite **New Folder** in ustvarite novo mapo z imenom *finetuning_dir*.

1. V mapi *finetuning_dir* ustvarite novo datoteko z imenom *fine_tune.py*.

#### Ustvarite in konfigurirajte datoteko *conda.yml*

1. V levem delu Visual Studio Code z desnim klikom izberite **New File** in ustvarite novo datoteko z imenom *conda.yml*.

1. V datoteko *conda.yml* dodajte naslednjo kodo za nastavitev okolja za fino prilagajanje modela Phi-3.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### Ustvarite in konfigurirajte datoteko *config.py*

1. V levem delu Visual Studio Code z desnim klikom izberite **New File** in ustvarite novo datoteko z imenom *config.py*.

1. V datoteko *config.py* dodajte naslednjo kodo za vnos vaših Azure podatkov.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Dodajte Azure okoljske spremenljivke

1. Izvedite naslednje korake za dodajanje Azure Subscription ID:

    - V **iskalno vrstico** na vrhu portala vnesite *subscriptions* in izberite **Subscriptions** iz prikazanih možnosti.
    - Izberite Azure naročnino, ki jo trenutno uporabljate.
    - Kopirajte in prilepite vaš Subscription ID v datoteko *config.py*.

    ![Poiščite ID naročnine.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.sl.png)

1. Izvedite naslednje korake za dodajanje imena Azure Workspace:

    - Pojdite do Azure Machine Learning vira, ki ste ga ustvarili.
    - Kopirajte in prilepite ime vašega delovnega prostora v datoteko *config.py*.

    ![Poiščite ime Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.sl.png)

1. Izvedite naslednje korake za dodajanje imena Azure Resource Group:

    - Pojdite do Azure Machine Learning vira, ki ste ga ustvarili.
    - Kopirajte in prilepite ime vaše Azure Resource Group v datoteko *config.py*.

    ![Poiščite ime skupine virov.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.sl.png)

2. Izvedite naslednje korake za dodajanje imena Azure Managed Identity:

    - Pojdite do vira Managed Identities, ki ste ga ustvarili.
    - Kopirajte in prilepite ime vaše Azure Managed Identity v datoteko *config.py*.

    ![Poiščite UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.sl.png)

### Pripravite podatkovni nabor za fino prilagajanje

V tej vaji boste zagnali datoteko *download_dataset.py*, da prenesete podatkovni nabor *ULTRACHAT_200k* v vaše lokalno okolje. Nato boste uporabili ta podatkovni nabor za fino prilagajanje modela Phi-3 v Azure Machine Learning.

#### Prenesite podatkovni nabor z uporabo *download_dataset.py*

1. Odprite datoteko *download_dataset.py* v Visual Studio Code.

1. V datoteko *download_dataset.py* dodajte naslednjo kodo.

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
> **Navodila za fino prilagajanje z minimalnim podatkovnim naborom na CPU**
>
> Če želite za fino prilagajanje uporabiti CPU, je ta pristop idealen za tiste z naročninami z ugodnostmi (kot je Visual Studio Enterprise Subscription) ali za hitro testiranje postopka fino prilagajanja in nameščanja.
>
> Zamenjajte `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` z `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. V terminal vnesite naslednji ukaz za zagon skripte in prenos podatkovnega nabora v lokalno okolje.

    ```console
    python download_data.py
    ```

1. Preverite, da so bili podatkovni nabori uspešno shranjeni v lokalno mapo *finetune-phi/data*.

> [!NOTE]
>
> **Velikost podatkovnega nabora in čas fino prilagajanja**
>
> V tem E2E primeru uporabljate le 1 % podatkovnega nabora (`train_sft[:1%]`). To znatno zmanjša količino podatkov, kar pospeši tako nalaganje kot proces fino prilagajanja. Delež lahko prilagodite, da najdete pravo ravnovesje med časom učenja in zmogljivostjo modela. Uporaba manjšega podnabora podatkov zmanjša čas, potreben za fino prilagajanje, kar proces naredi bolj obvladljiv za E2E primer.

## Scenarij 2: Fino prilagodite model Phi-3 in ga namestite v Azure Machine Learning Studio

### Nastavite Azure CLI

Za avtentikacijo vašega okolja morate nastaviti Azure CLI. Azure CLI omogoča upravljanje Azure virov neposredno iz ukazne vrstice in zagotavlja poverilnice, potrebne za dostop Azure Machine Learning do teh virov. Za začetek namestite [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Odprite terminal in vnesite naslednji ukaz za prijavo v vaš Azure račun.

    ```console
    az login
    ```

1. Izberite vaš Azure račun za uporabo.

1. Izberite vašo Azure naročnino za uporabo.

    ![Poiščite ime skupine virov.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.sl.png)

> [!TIP]
>
> Če imate težave s prijavo v Azure, poskusite uporabiti kodo naprave. Odprite terminal in vnesite naslednji ukaz za prijavo v vaš Azure račun:
>
> ```console
> az login --use-device-code
> ```
>

### Fino prilagodite model Phi-3

V tej vaji boste fino prilagodili model Phi-3 z uporabo danega podatkovnega nabora. Najprej boste definirali postopek fino prilagajanja v datoteki *fine_tune.py*. Nato boste konfigurirali okolje Azure Machine Learning in začeli postopek fino prilagajanja z zagonom datoteke *setup_ml.py*. Ta skripta zagotavlja, da se fino prilagajanje izvede znotraj okolja Azure Machine Learning.

Z zagonom *setup_ml.py* boste zagnali postopek fino prilagajanja v okolju Azure Machine Learning.

#### Dodajte kodo v datoteko *fine_tune.py*

1. Pojdite v mapo *finetuning_dir* in odprite datoteko *fine_tune.py* v Visual Studio Code.

1. V datoteko *fine_tune.py* dodajte naslednjo kodo.

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

1. Shranite in zaprite datoteko *fine_tune.py*.

> [!TIP]
> **Fino lahko prilagodite tudi model Phi-3.5**
>
> V datoteki *fine_tune.py* lahko spremenite `pretrained_model_name` iz `"microsoft/Phi-3-mini-4k-instruct"` v kateri koli model, ki ga želite fino prilagoditi. Na primer, če ga spremenite v `"microsoft/Phi-3.5-mini-instruct"`, boste za fino prilagajanje uporabili model Phi-3.5-mini-instruct. Za iskanje in uporabo imena modela, ki vam ustreza, obiščite [Hugging Face](https://huggingface.co/), poiščite želeni model in nato kopirajte ter prilepite njegovo ime v polje `pretrained_model_name` v vaši skripti.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fino prilagodite Phi-3.5.":::
>

#### Dodajte kodo v datoteko *setup_ml.py*

1. Odprite datoteko *setup_ml.py* v Visual Studio Code.

1. V datoteko *setup_ml.py* dodajte naslednjo kodo.

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

1. Zamenjajte `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` in `LOCATION` z vašimi podatki.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Navodila za fino prilagajanje z minimalnim podatkovnim naborom na CPU**
>
> Če želite za fino prilagajanje uporabiti CPU, je ta pristop idealen za tiste z naročninami z ugodnostmi (kot je Visual Studio Enterprise Subscription) ali za hitro testiranje postopka fino prilagajanja in nameščanja.
>
> 1. Odprite datoteko *setup_ml*.
> 2. Zamenjajte `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` in `DOCKER_IMAGE_NAME` z naslednjim. Če nimate dostopa do *Standard_E16s_v3*, lahko uporabite ustrezno CPU instanco ali zaprosite za nov kvoto.
> 3. Zamenjajte `LOCATION` z vašimi podatki.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. V terminal vnesite naslednji ukaz za zagon skripte *setup_ml.py* in začetek postopka fino prilagajanja v Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. V tej vaji ste uspešno fino prilagodili model Phi-3 z uporabo Azure Machine Learning. Z zagonom skripte *setup_ml.py* ste nastavili okolje Azure Machine Learning in začeli postopek fino prilagajanja, definiran v datoteki *fine_tune.py*. Upoštevajte, da lahko postopek fino prilagajanja traja precej časa. Po zagonu ukaza `python setup_ml.py` morate počakati, da se postopek zaključi. Status naloge fino prilagajanja lahko spremljate preko povezave, ki je prikazana v terminalu in vodi do portala Azure Machine Learning.

    ![Oglejte si nalogo fino prilagajanja.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.sl.png)

### Namestite fino prilagojen model

Za integracijo fino prilagojenega modela Phi-3 s Prompt Flow morate model namestiti, da bo dostopen za izvajanje v realnem času. Ta postopek vključuje registracijo modela, ustvarjanje spletne točke in nameščanje modela.

#### Nastavite ime modela, ime končne točke in ime nameščanja

1. Odprite datoteko *config.py*.

1. Zamenjajte `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` z želenim imenom vašega modela.

1. Zamenjajte `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` z želenim imenom vaše končne točke.

1. Zamenjajte `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` z želenim imenom vašega nameščanja.

#### Dodajte kodo v datoteko *deploy_model.py*

Zagon datoteke *deploy_model.py* avtomatizira celoten postopek nameščanja. Registrira model, ustvari končno točko in izvede nameščanje na podlagi nastavitev, določenih v datoteki *config.py*, ki vključujejo ime modela, ime končne točke in ime nameščanja.

1. Odprite datoteko *deploy_model.py* v Visual Studio Code.

1. V datoteko *deploy_model.py* dodajte naslednjo kodo.

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

1. Izvedite naslednje korake za pridobitev `JOB_NAME`:

    - Pojdite do vira Azure Machine Learning, ki ste ga ustvarili.
    - Izberite **Studio web URL** za odprtje delovnega prostora Azure Machine Learning.
    - Izberite **Jobs** v levem meniju.
    - Izberite eksperiment za fino prilagajanje, na primer *finetunephi*.
    - Izberite nalogo, ki ste jo ustvarili.
- Kopirajte in prilepite ime vaše naloge v `JOB_NAME = "your-job-name"` v datoteki *deploy_model.py*.

1. Zamenjajte `COMPUTE_INSTANCE_TYPE` z vašimi specifičnimi podatki.

1. Vnesite naslednji ukaz za zagon skripte *deploy_model.py* in začetek procesa nameščanja v Azure Machine Learning.

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> Da se izognete dodatnim stroškom na vašem računu, poskrbite, da izbrišete ustvarjeni endpoint v delovnem prostoru Azure Machine Learning.
>

#### Preverite stanje nameščanja v delovnem prostoru Azure Machine Learning

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pomaknite se do delovnega prostora Azure Machine Learning, ki ste ga ustvarili.

1. Izberite **Studio web URL** za odprtje delovnega prostora Azure Machine Learning.

1. Izberite **Endpoints** v levem zavihku.

    ![Izberite endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.sl.png)

2. Izberite endpoint, ki ste ga ustvarili.

    ![Izberite endpoint, ki ste ga ustvarili.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.sl.png)

3. Na tej strani lahko upravljate z endpointi, ustvarjenimi med procesom nameščanja.

## Scenarij 3: Integracija s Prompt flow in pogovor z vašim prilagojenim modelom

### Integracija prilagojenega modela Phi-3 s Prompt flow

Po uspešnem nameščanju vašega fino nastavljanega modela ga lahko zdaj integrirate s Prompt flow, da uporabite vaš model v aplikacijah v realnem času, kar omogoča različne interaktivne naloge z vašim prilagojenim modelom Phi-3.

#### Nastavite api ključ in endpoint uri fino nastavljenega modela Phi-3

1. Pomaknite se do delovnega prostora Azure Machine Learning, ki ste ga ustvarili.
1. Izberite **Endpoints** v levem zavihku.
1. Izberite endpoint, ki ste ga ustvarili.
1. Izberite **Consume** v navigacijskem meniju.
1. Kopirajte in prilepite vaš **REST endpoint** v datoteko *config.py*, tako da zamenjate `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` z vašim **REST endpoint**.
1. Kopirajte in prilepite vaš **Primary key** v datoteko *config.py*, tako da zamenjate `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` z vašim **Primary key**.

    ![Kopirajte api ključ in endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.sl.png)

#### Dodajte kodo v datoteko *flow.dag.yml*

1. Odprite datoteko *flow.dag.yml* v Visual Studio Code.

1. Dodajte naslednjo kodo v *flow.dag.yml*.

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

#### Dodajte kodo v datoteko *integrate_with_promptflow.py*

1. Odprite datoteko *integrate_with_promptflow.py* v Visual Studio Code.

1. Dodajte naslednjo kodo v *integrate_with_promptflow.py*.

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

### Pogovor z vašim prilagojenim modelom

1. Vnesite naslednji ukaz za zagon skripte *deploy_model.py* in začetek procesa nameščanja v Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Tukaj je primer rezultatov: Zdaj lahko klepetate z vašim prilagojenim modelom Phi-3. Priporočljivo je postavljati vprašanja, ki temeljijo na podatkih, uporabljenih za fino nastavljanje.

    ![Primer Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.sl.png)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.