<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-09-12T14:33:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "lt"
}
-->
# Tobulinkite ir integruokite pritaikytus Phi-3 modelius su Prompt flow

Šis pilnas pavyzdys (E2E) yra pagrįstas vadovu "[Tobulinkite ir integruokite pritaikytus Phi-3 modelius su Prompt Flow: žingsnis po žingsnio vadovas](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" iš Microsoft Tech Community. Jame pristatomi pritaikymo, diegimo ir integravimo procesai, susiję su pritaikytais Phi-3 modeliais naudojant Prompt flow.

## Apžvalga

Šiame E2E pavyzdyje sužinosite, kaip pritaikyti Phi-3 modelį ir integruoti jį su Prompt flow. Naudodami Azure Machine Learning ir Prompt flow, sukursite darbo eigą, skirtą pritaikytų AI modelių diegimui ir naudojimui. Šis E2E pavyzdys suskirstytas į tris scenarijus:

**Scenarijus 1: Azure resursų nustatymas ir pasiruošimas pritaikymui**

**Scenarijus 2: Phi-3 modelio pritaikymas ir diegimas Azure Machine Learning Studio**

**Scenarijus 3: Integracija su Prompt flow ir pokalbiai su pritaikytu modeliu**

Štai šio E2E pavyzdžio apžvalga.

![Phi-3-FineTuning_PromptFlow_Integration Apžvalga](../../../../../../imgs/02/FineTuning-PromptFlow/00-01-architecture.png)

### Turinys

1. **[Scenarijus 1: Azure resursų nustatymas ir pasiruošimas pritaikymui](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Sukurti Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Prašyti GPU kvotų Azure prenumeratoje](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pridėti rolės priskyrimą](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nustatyti projektą](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Paruošti duomenų rinkinį pritaikymui](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarijus 2: Phi-3 modelio pritaikymas ir diegimas Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Nustatyti Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pritaikyti Phi-3 modelį](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Diegti pritaikytą modelį](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarijus 3: Integracija su Prompt flow ir pokalbiai su pritaikytu modeliu](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integruoti pritaikytą Phi-3 modelį su Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pokalbiai su pritaikytu modeliu](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenarijus 1: Azure resursų nustatymas ir pasiruošimas pritaikymui

### Sukurti Azure Machine Learning Workspace

1. Įveskite *azure machine learning* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Azure Machine Learning** iš pasirodžiusių parinkčių.

    ![Įveskite azure machine learning](../../../../../../imgs/02/FineTuning-PromptFlow/01-01-type-azml.png)

1. Pasirinkite **+ Create** iš navigacijos meniu.

1. Pasirinkite **New workspace** iš navigacijos meniu.

    ![Pasirinkite naują workspace](../../../../../../imgs/02/FineTuning-PromptFlow/01-02-select-new-workspace.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti (sukurkite naują, jei reikia).
    - Įveskite **Workspace Name**. Jis turi būti unikalus.
    - Pasirinkite **Regioną**, kurį norite naudoti.
    - Pasirinkite **Saugojimo paskyrą**, kurią norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Key vault**, kurį norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Application insights**, kurį norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Container registry**, kurį norite naudoti (sukurkite naują, jei reikia).

    ![Užpildykite AZML.](../../../../../../imgs/02/FineTuning-PromptFlow/01-03-fill-AZML.png)

1. Pasirinkite **Review + Create**.

1. Pasirinkite **Create**.

### Prašyti GPU kvotų Azure prenumeratoje

Šiame E2E pavyzdyje naudosite *Standard_NC24ads_A100_v4 GPU* pritaikymui, kuriam reikia kvotos prašymo, ir *Standard_E4s_v3* CPU diegimui, kuriam kvotos prašymo nereikia.

> [!NOTE]
>
> Tik Pay-As-You-Go prenumeratos (standartinis prenumeratos tipas) yra tinkamos GPU paskirstymui; naudos prenumeratos šiuo metu nepalaikomos.
>
> Tiems, kurie naudoja naudos prenumeratas (pvz., Visual Studio Enterprise Subscription) arba tiems, kurie nori greitai išbandyti pritaikymo ir diegimo procesą, šis vadovas taip pat pateikia instrukcijas, kaip pritaikyti minimalų duomenų rinkinį naudojant CPU. Tačiau svarbu pažymėti, kad pritaikymo rezultatai yra žymiai geresni naudojant GPU su didesniais duomenų rinkiniais.

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Atlikite šiuos veiksmus, kad prašytumėte *Standard NCADSA100v4 Family* kvotos:

    - Pasirinkite **Quota** iš kairės pusės skirtuko.
    - Pasirinkite **Virtual machine family**, kurią norite naudoti. Pavyzdžiui, pasirinkite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, kuri apima *Standard_NC24ads_A100_v4* GPU.
    - Pasirinkite **Request quota** iš navigacijos meniu.

        ![Prašyti kvotos.](../../../../../../imgs/02/FineTuning-PromptFlow/01-04-request-quota.png)

    - Kvotos prašymo puslapyje įveskite **Naują branduolių limitą**, kurį norite naudoti. Pavyzdžiui, 24.
    - Kvotos prašymo puslapyje pasirinkite **Submit**, kad pateiktumėte GPU kvotos prašymą.

> [!NOTE]
> Galite pasirinkti tinkamą GPU arba CPU pagal savo poreikius, remdamiesi dokumentu [Virtualių mašinų dydžiai Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Pridėti rolės priskyrimą

Norėdami pritaikyti ir diegti savo modelius, pirmiausia turite sukurti Vartotojo priskirtą valdomą tapatybę (UAI) ir priskirti jai tinkamus leidimus. Ši UAI bus naudojama autentifikacijai diegimo metu.

#### Sukurti Vartotojo priskirtą valdomą tapatybę (UAI)

1. Įveskite *managed identities* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Managed Identities** iš pasirodžiusių parinkčių.

    ![Įveskite managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow/01-05-type-managed-identities.png)

1. Pasirinkite **+ Create**.

    ![Pasirinkite sukurti.](../../../../../../imgs/02/FineTuning-PromptFlow/01-06-select-create.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Regioną**, kurį norite naudoti.
    - Įveskite **Pavadinimą**. Jis turi būti unikalus.

1. Pasirinkite **Review + create**.

1. Pasirinkite **+ Create**.

#### Pridėti Contributor rolės priskyrimą valdomai tapatybei

1. Eikite į valdomos tapatybės resursą, kurį sukūrėte.

1. Pasirinkite **Azure role assignments** iš kairės pusės skirtuko.

1. Pasirinkite **+Add role assignment** iš navigacijos meniu.

1. Pridėti rolės priskyrimo puslapyje atlikite šiuos veiksmus:
    - Pasirinkite **Scope** kaip **Resource group**.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti.
    - Pasirinkite **Rolę** kaip **Contributor**.

    ![Užpildykite Contributor rolę.](../../../../../../imgs/02/FineTuning-PromptFlow/01-07-fill-contributor-role.png)

1. Pasirinkite **Save**.

#### Pridėti Storage Blob Data Reader rolės priskyrimą valdomai tapatybei

1. Įveskite *storage accounts* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Storage accounts** iš pasirodžiusių parinkčių.

    ![Įveskite storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow/01-08-type-storage-accounts.png)

1. Pasirinkite saugojimo paskyrą, susijusią su Azure Machine Learning workspace, kurį sukūrėte. Pavyzdžiui, *finetunephistorage*.

1. Atlikite šiuos veiksmus, kad pereitumėte į Pridėti rolės priskyrimo puslapį:

    - Eikite į Azure saugojimo paskyrą, kurią sukūrėte.
    - Pasirinkite **Access Control (IAM)** iš kairės pusės skirtuko.
    - Pasirinkite **+ Add** iš navigacijos meniu.
    - Pasirinkite **Add role assignment** iš navigacijos meniu.

    ![Pridėti rolę.](../../../../../../imgs/02/FineTuning-PromptFlow/01-09-add-role.png)

1. Pridėti rolės priskyrimo puslapyje atlikite šiuos veiksmus:

    - Rolės puslapyje įveskite *Storage Blob Data Reader* į **paieškos juostą** ir pasirinkite **Storage Blob Data Reader** iš pasirodžiusių parinkčių.
    - Rolės puslapyje pasirinkite **Next**.
    - Narių puslapyje pasirinkite **Assign access to** **Managed identity**.
    - Narių puslapyje pasirinkite **+ Select members**.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite **Valdomą tapatybę** kaip **Manage Identity**.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite valdomą tapatybę, kurią sukūrėte. Pavyzdžiui, *finetunephi-managedidentity*.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite **Select**.

    ![Pasirinkti valdomą tapatybę.](../../../../../../imgs/02/FineTuning-PromptFlow/01-10-select-managed-identity.png)

1. Pasirinkite **Review + assign**.

#### Pridėti AcrPull rolės priskyrimą valdomai tapatybei

1. Įveskite *container registries* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Container registries** iš pasirodžiusių parinkčių.

    ![Įveskite container registries.](../../../../../../imgs/02/FineTuning-PromptFlow/01-11-type-container-registries.png)

1. Pasirinkite konteinerių registrą, susijusį su Azure Machine Learning workspace. Pavyzdžiui, *finetunephicontainerregistries*

1. Atlikite šiuos veiksmus, kad pereitumėte į Pridėti rolės priskyrimo puslapį:

    - Pasirinkite **Access Control (IAM)** iš kairės pusės skirtuko.
    - Pasirinkite **+ Add** iš navigacijos meniu.
    - Pasirinkite **Add role assignment** iš navigacijos meniu.

1. Pridėti rolės priskyrimo puslapyje atlikite šiuos veiksmus:

    - Rolės puslapyje įveskite *AcrPull* į **paieškos juostą** ir pasirinkite **AcrPull** iš pasirodžiusių parinkčių.
    - Rolės puslapyje pasirinkite **Next**.
    - Narių puslapyje pasirinkite **Assign access to** **Managed identity**.
    - Narių puslapyje pasirinkite **+ Select members**.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite **Valdomą tapatybę** kaip **Manage Identity**.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite valdomą tapatybę, kurią sukūrėte. Pavyzdžiui, *finetunephi-managedidentity*.
    - Pasirinkti valdomas tapatybes puslapyje pasirinkite **Select**.
    - Pasirinkite **Review + assign**.

### Nustatyti projektą

Dabar sukursite aplanką darbui ir nustatysite virtualią aplinką, kad sukurtumėte programą, kuri bendrauja su vartotojais ir naudoja saugomą pokalbių istoriją iš Azure Cosmos DB, kad informuotų savo atsakymus.

#### Sukurti aplanką darbui

1. Atidarykite terminalo langą ir įveskite šią komandą, kad sukurtumėte aplanką pavadinimu *finetune-phi* numatytame kelyje.

    ```console
    mkdir finetune-phi
    ```

1. Įveskite šią komandą terminale, kad pereitumėte į sukurtą *finetune-phi* aplanką.

    ```console
    cd finetune-phi
    ```

#### Sukurti virtualią aplinką

1. Įveskite šią komandą terminale, kad sukurtumėte virtualią aplinką pavadinimu *.venv*.

    ```console
    python -m venv .venv
    ```

1. Įveskite šią komandą terminale, kad aktyvuotumėte virtualią aplinką.

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> Jei viskas pavyko, prieš komandų eilutę turėtumėte matyti *(.venv)*.
#### Įdiekite reikalingus paketus

1. Terminale įveskite šias komandas, kad įdiegtumėte reikalingus paketus.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Sukurkite projekto failus

Šiame pratime sukursite pagrindinius failus mūsų projektui. Šie failai apima scenarijus, skirtus duomenų rinkinio atsisiuntimui, Azure Machine Learning aplinkos nustatymui, Phi-3 modelio pritaikymui ir pritaikyto modelio diegimui. Taip pat sukursite *conda.yml* failą, skirtą pritaikymo aplinkos nustatymui.

Šiame pratime atliksite šiuos veiksmus:

- Sukurkite *download_dataset.py* failą, skirtą duomenų rinkinio atsisiuntimui.
- Sukurkite *setup_ml.py* failą, skirtą Azure Machine Learning aplinkos nustatymui.
- Sukurkite *fine_tune.py* failą aplanke *finetuning_dir*, skirtą Phi-3 modelio pritaikymui naudojant duomenų rinkinį.
- Sukurkite *conda.yml* failą, skirtą pritaikymo aplinkos nustatymui.
- Sukurkite *deploy_model.py* failą, skirtą pritaikyto modelio diegimui.
- Sukurkite *integrate_with_promptflow.py* failą, skirtą pritaikyto modelio integravimui ir vykdymui naudojant Prompt Flow.
- Sukurkite *flow.dag.yml* failą, skirtą Prompt Flow darbo eigos struktūros nustatymui.
- Sukurkite *config.py* failą, skirtą Azure informacijos įvedimui.

> [!NOTE]
>
> Pilna aplankų struktūra:
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

1. Atidarykite **Visual Studio Code**.

1. Pasirinkite **File** iš meniu juostos.

1. Pasirinkite **Open Folder**.

1. Pasirinkite aplanką *finetune-phi*, kurį sukūrėte, esantį *C:\Users\yourUserName\finetune-phi*.

    ![Atidarykite projekto aplanką.](../../../../../../imgs/02/FineTuning-PromptFlow/01-12-open-project-folder.png)

1. Kairiajame Visual Studio Code skydelyje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *download_dataset.py*.

1. Kairiajame Visual Studio Code skydelyje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *setup_ml.py*.

1. Kairiajame Visual Studio Code skydelyje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *deploy_model.py*.

    ![Sukurkite naują failą.](../../../../../../imgs/02/FineTuning-PromptFlow/01-13-create-new-file.png)

1. Kairiajame Visual Studio Code skydelyje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New Folder**, kad sukurtumėte naują aplanką pavadinimu *finetuning_dir*.

1. Aplanke *finetuning_dir* sukurkite naują failą pavadinimu *fine_tune.py*.

#### Sukurkite ir sukonfigūruokite *conda.yml* failą

1. Kairiajame Visual Studio Code skydelyje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *conda.yml*.

1. Į *conda.yml* failą įtraukite šį kodą, kad nustatytumėte Phi-3 modelio pritaikymo aplinką.

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

#### Sukurkite ir sukonfigūruokite *config.py* failą

1. Kairiajame Visual Studio Code skydelyje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *config.py*.

1. Į *config.py* failą įtraukite šį kodą, kad įvestumėte savo Azure informaciją.

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

#### Pridėkite Azure aplinkos kintamuosius

1. Atlikite šiuos veiksmus, kad pridėtumėte Azure prenumeratos ID:

    - Viršutinėje portalo puslapio paieškos juostoje įveskite *subscriptions* ir pasirinkite **Subscriptions** iš pasirodžiusių parinkčių.
    - Pasirinkite Azure prenumeratą, kurią šiuo metu naudojate.
    - Nukopijuokite ir įklijuokite savo prenumeratos ID į *config.py* failą.

    ![Raskite prenumeratos ID.](../../../../../../imgs/02/FineTuning-PromptFlow/01-14-find-subscriptionid.png)

1. Atlikite šiuos veiksmus, kad pridėtumėte Azure darbo srities pavadinimą:

    - Eikite į sukurtą Azure Machine Learning resursą.
    - Nukopijuokite ir įklijuokite savo paskyros pavadinimą į *config.py* failą.

    ![Raskite Azure Machine Learning pavadinimą.](../../../../../../imgs/02/FineTuning-PromptFlow/01-15-find-AZML-name.png)

1. Atlikite šiuos veiksmus, kad pridėtumėte Azure resursų grupės pavadinimą:

    - Eikite į sukurtą Azure Machine Learning resursą.
    - Nukopijuokite ir įklijuokite savo Azure resursų grupės pavadinimą į *config.py* failą.

    ![Raskite resursų grupės pavadinimą.](../../../../../../imgs/02/FineTuning-PromptFlow/01-16-find-AZML-resourcegroup.png)

2. Atlikite šiuos veiksmus, kad pridėtumėte Azure valdomos tapatybės pavadinimą:

    - Eikite į sukurtą Managed Identities resursą.
    - Nukopijuokite ir įklijuokite savo Azure valdomos tapatybės pavadinimą į *config.py* failą.

    ![Raskite UAI.](../../../../../../imgs/02/FineTuning-PromptFlow/01-17-find-uai.png)

### Paruoškite duomenų rinkinį pritaikymui

Šiame pratime paleisite *download_dataset.py* failą, kad atsisiųstumėte *ULTRACHAT_200k* duomenų rinkinius į savo vietinę aplinką. Tada naudosite šiuos duomenų rinkinius Phi-3 modelio pritaikymui Azure Machine Learning aplinkoje.

#### Atsisiųskite duomenų rinkinį naudodami *download_dataset.py*

1. Atidarykite *download_dataset.py* failą Visual Studio Code.

1. Įtraukite šį kodą į *download_dataset.py* failą.

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
> **Pritaikymo su minimaliu duomenų rinkiniu naudojant CPU gairės**
>
> Jei norite naudoti CPU pritaikymui, ši strategija idealiai tinka tiems, kurie turi prenumeratos privalumų (pvz., Visual Studio Enterprise Subscription) arba nori greitai išbandyti pritaikymo ir diegimo procesą.
>
> Pakeiskite `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` į `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Terminale įveskite šią komandą, kad paleistumėte scenarijų ir atsisiųstumėte duomenų rinkinį į savo vietinę aplinką.

    ```console
    python download_data.py
    ```

1. Patikrinkite, ar duomenų rinkiniai buvo sėkmingai išsaugoti jūsų vietiniame *finetune-phi/data* aplanke.

> [!NOTE]
>
> **Duomenų rinkinio dydis ir pritaikymo laikas**
>
> Šiame E2E pavyzdyje naudojate tik 1% duomenų rinkinio (`train_sft[:1%]`). Tai žymiai sumažina duomenų kiekį, pagreitindama tiek įkėlimo, tiek pritaikymo procesus. Galite reguliuoti procentą, kad rastumėte tinkamą balansą tarp mokymo laiko ir modelio našumo. Naudojant mažesnį duomenų rinkinio dalį sumažėja pritaikymo laikas, todėl procesas tampa lengviau valdomas E2E pavyzdžiui.
- Nukopijuokite ir įklijuokite savo darbo pavadinimą į `JOB_NAME = "your-job-name"` faile *deploy_model.py*.

1. Pakeiskite `COMPUTE_INSTANCE_TYPE` savo specifinėmis detalėmis.

1. Įveskite šią komandą, kad paleistumėte *deploy_model.py* skriptą ir pradėtumėte diegimo procesą Azure Machine Learning.

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> Kad išvengtumėte papildomų mokesčių savo paskyrai, įsitikinkite, kad ištrynėte sukurtą galinį tašką Azure Machine Learning darbo erdvėje.
>

#### Patikrinkite diegimo būseną Azure Machine Learning darbo erdvėje

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Eikite į Azure Machine Learning darbo erdvę, kurią sukūrėte.

1. Pasirinkite **Studio web URL**, kad atidarytumėte Azure Machine Learning darbo erdvę.

1. Pasirinkite **Endpoints** iš kairės pusės skirtuko.

    ![Pasirinkite galinius taškus.](../../../../../../imgs/02/FineTuning-PromptFlow/02-03-select-endpoints.png)

2. Pasirinkite galinį tašką, kurį sukūrėte.

    ![Pasirinkite sukurtus galinius taškus.](../../../../../../imgs/02/FineTuning-PromptFlow/02-04-select-endpoint-created.png)

3. Šiame puslapyje galite valdyti galinius taškus, sukurtus diegimo proceso metu.

## Scenarijus 3: Integracija su Prompt flow ir pokalbiai su jūsų pritaikytu modeliu

### Integruokite pritaikytą Phi-3 modelį su Prompt flow

Sėkmingai įdiegę savo pritaikytą modelį, dabar galite jį integruoti su Prompt flow, kad galėtumėte naudoti modelį realaus laiko programose, leidžiančiose atlikti įvairias interaktyvias užduotis su jūsų pritaikytu Phi-3 modeliu.

#### Nustatykite API raktą ir galinio taško URI pritaikytam Phi-3 modeliui

1. Eikite į Azure Machine Learning darbo erdvę, kurią sukūrėte.
1. Pasirinkite **Endpoints** iš kairės pusės skirtuko.
1. Pasirinkite galinį tašką, kurį sukūrėte.
1. Pasirinkite **Consume** iš navigacijos meniu.
1. Nukopijuokite ir įklijuokite savo **REST endpoint** į *config.py* failą, pakeisdami `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` savo **REST endpoint**.
1. Nukopijuokite ir įklijuokite savo **Primary key** į *config.py* failą, pakeisdami `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` savo **Primary key**.

    ![Nukopijuokite API raktą ir galinio taško URI.](../../../../../../imgs/02/FineTuning-PromptFlow/02-05-copy-apikey-endpoint.png)

#### Pridėkite kodą į *flow.dag.yml* failą

1. Atidarykite *flow.dag.yml* failą Visual Studio Code.

1. Pridėkite šį kodą į *flow.dag.yml*.

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

#### Pridėkite kodą į *integrate_with_promptflow.py* failą

1. Atidarykite *integrate_with_promptflow.py* failą Visual Studio Code.

1. Pridėkite šį kodą į *integrate_with_promptflow.py*.

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

### Pokalbiai su jūsų pritaikytu modeliu

1. Įveskite šią komandą, kad paleistumėte *deploy_model.py* skriptą ir pradėtumėte diegimo procesą Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Štai pavyzdys rezultatų: Dabar galite bendrauti su savo pritaikytu Phi-3 modeliu. Rekomenduojama užduoti klausimus, pagrįstus duomenimis, naudotais pritaikymui.

    ![Prompt flow pavyzdys.](../../../../../../imgs/02/FineTuning-PromptFlow/02-06-promptflow-example.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.