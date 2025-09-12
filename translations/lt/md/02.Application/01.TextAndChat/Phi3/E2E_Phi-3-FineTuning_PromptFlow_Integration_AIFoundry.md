<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-09-12T14:35:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "lt"
}
-->
# Tobulinkite ir integruokite pasirinktinius Phi-3 modelius su Prompt flow Azure AI Foundry

Šis nuo pradžios iki pabaigos (E2E) pavyzdys yra pagrįstas vadovu "[Tobulinkite ir integruokite pasirinktinius Phi-3 modelius su Prompt flow Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iš Microsoft Tech Community. Jame pristatomi procesai, kaip tobulinti, diegti ir integruoti pasirinktinius Phi-3 modelius su Prompt flow Azure AI Foundry. 
Skirtingai nuo E2E pavyzdžio "[Tobulinkite ir integruokite pasirinktinius Phi-3 modelius su Prompt flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", kuriame buvo vykdomas kodas lokaliai, šiame vadove dėmesys skiriamas tik modelio tobulinimui ir integravimui Azure AI / ML Studio aplinkoje.

## Apžvalga

Šiame E2E pavyzdyje sužinosite, kaip tobulinti Phi-3 modelį ir integruoti jį su Prompt flow Azure AI Foundry. Naudodamiesi Azure AI / ML Studio, sukursite darbo eigą, skirtą pasirinktinių AI modelių diegimui ir naudojimui. Šis E2E pavyzdys suskirstytas į tris scenarijus:

**Scenarijus 1: Azure resursų nustatymas ir pasiruošimas tobulinimui**

**Scenarijus 2: Phi-3 modelio tobulinimas ir diegimas Azure Machine Learning Studio**

**Scenarijus 3: Integracija su Prompt flow ir pokalbiai su jūsų pasirinktu modeliu Azure AI Foundry**

Štai šio E2E pavyzdžio apžvalga.

![Phi-3-FineTuning_PromptFlow_Integration Apžvalga.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/00-01-architecture.png)

### Turinys

1. **[Scenarijus 1: Azure resursų nustatymas ir pasiruošimas tobulinimui](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Sukurti Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Prašyti GPU kvotų Azure prenumeratoje](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pridėti rolės priskyrimą](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nustatyti projektą](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Paruošti duomenų rinkinį tobulinimui](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarijus 2: Phi-3 modelio tobulinimas ir diegimas Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Tobulinti Phi-3 modelį](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Diegti patobulintą Phi-3 modelį](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarijus 3: Integracija su Prompt flow ir pokalbiai su jūsų pasirinktu modeliu Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integruoti pasirinktą Phi-3 modelį su Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pokalbiai su jūsų pasirinktu Phi-3 modeliu](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenarijus 1: Azure resursų nustatymas ir pasiruošimas tobulinimui

### Sukurti Azure Machine Learning Workspace

1. Įveskite *azure machine learning* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Azure Machine Learning** iš pasirodžiusių parinkčių.

    ![Įveskite azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-01-type-azml.png)

2. Pasirinkite **+ Create** iš navigacijos meniu.

3. Pasirinkite **New workspace** iš navigacijos meniu.

    ![Pasirinkite naują workspace.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-02-select-new-workspace.png)

4. Atlikite šiuos veiksmus:

    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti (sukurkite naują, jei reikia).
    - Įveskite **Workspace Name**. Jis turi būti unikalus.
    - Pasirinkite **Regioną**, kurį norite naudoti.
    - Pasirinkite **Saugojimo paskyrą**, kurią norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Key vault**, kurį norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Application insights**, kurį norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Container registry**, kurį norite naudoti (sukurkite naują, jei reikia).

    ![Užpildykite azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-03-fill-AZML.png)

5. Pasirinkite **Review + Create**.

6. Pasirinkite **Create**.

### Prašyti GPU kvotų Azure prenumeratoje

Šiame vadove sužinosite, kaip tobulinti ir diegti Phi-3 modelį, naudojant GPU. Tobulinimui naudosite *Standard_NC24ads_A100_v4* GPU, kuriam reikia kvotos prašymo. Diegimui naudosite *Standard_NC6s_v3* GPU, kuriam taip pat reikia kvotos prašymo.

> [!NOTE]
>
> Tik Pay-As-You-Go prenumeratos (standartinis prenumeratos tipas) yra tinkamos GPU paskirstymui; naudos prenumeratos šiuo metu nepalaikomos.
>

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Atlikite šiuos veiksmus, kad paprašytumėte *Standard NCADSA100v4 Family* kvotos:

    - Pasirinkite **Quota** iš kairės pusės skirtuko.
    - Pasirinkite **Virtual machine family**, kurią norite naudoti. Pavyzdžiui, pasirinkite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, kuriame yra *Standard_NC24ads_A100_v4* GPU.
    - Pasirinkite **Request quota** iš navigacijos meniu.

        ![Prašyti kvotos.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/02-02-request-quota.png)

    - Kvotos prašymo puslapyje įveskite **Naują branduolių limitą**, kurį norite naudoti. Pavyzdžiui, 24.
    - Kvotos prašymo puslapyje pasirinkite **Submit**, kad paprašytumėte GPU kvotos.

1. Atlikite šiuos veiksmus, kad paprašytumėte *Standard NCSv3 Family* kvotos:

    - Pasirinkite **Quota** iš kairės pusės skirtuko.
    - Pasirinkite **Virtual machine family**, kurią norite naudoti. Pavyzdžiui, pasirinkite **Standard NCSv3 Family Cluster Dedicated vCPUs**, kuriame yra *Standard_NC6s_v3* GPU.
    - Pasirinkite **Request quota** iš navigacijos meniu.
    - Kvotos prašymo puslapyje įveskite **Naują branduolių limitą**, kurį norite naudoti. Pavyzdžiui, 24.
    - Kvotos prašymo puslapyje pasirinkite **Submit**, kad paprašytumėte GPU kvotos.

### Pridėti rolės priskyrimą

Norėdami tobulinti ir diegti savo modelius, pirmiausia turite sukurti Vartotojo priskirtą valdomą tapatybę (UAI) ir priskirti jai tinkamus leidimus. Ši UAI bus naudojama autentifikacijai diegimo metu.

#### Sukurti Vartotojo priskirtą valdomą tapatybę (UAI)

1. Įveskite *managed identities* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Managed Identities** iš pasirodžiusių parinkčių.

    ![Įveskite managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-01-type-managed-identities.png)

1. Pasirinkite **+ Create**.

    ![Pasirinkite sukurti.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-02-select-create.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Regioną**, kurį norite naudoti.
    - Įveskite **Pavadinimą**. Jis turi būti unikalus.

    ![Pasirinkite sukurti.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-03-fill-managed-identities-1.png)

1. Pasirinkite **Review + create**.

1. Pasirinkite **+ Create**.

#### Pridėti Contributor rolės priskyrimą valdomai tapatybei

1. Eikite į valdomos tapatybės resursą, kurį sukūrėte.

1. Pasirinkite **Azure role assignments** iš kairės pusės skirtuko.

1. Pasirinkite **+Add role assignment** iš navigacijos meniu.

1. Priskyrimo puslapyje atlikite šiuos veiksmus:
    - Pasirinkite **Scope** kaip **Resource group**.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti.
    - Pasirinkite **Rolę** kaip **Contributor**.

    ![Užpildykite Contributor rolę.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-04-fill-contributor-role.png)

2. Pasirinkite **Save**.

#### Pridėti Storage Blob Data Reader rolės priskyrimą valdomai tapatybei

1. Įveskite *storage accounts* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Storage accounts** iš pasirodžiusių parinkčių.

    ![Įveskite storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-05-type-storage-accounts.png)

1. Pasirinkite saugojimo paskyrą, susijusią su Azure Machine Learning workspace, kurį sukūrėte. Pavyzdžiui, *finetunephistorage*.

1. Atlikite šiuos veiksmus, kad pereitumėte į Pridėti rolės priskyrimo puslapį:

    - Eikite į Azure saugojimo paskyrą, kurią sukūrėte.
    - Pasirinkite **Access Control (IAM)** iš kairės pusės skirtuko.
    - Pasirinkite **+ Add** iš navigacijos meniu.
    - Pasirinkite **Add role assignment** iš navigacijos meniu.

    ![Pridėti rolę.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-06-add-role.png)

1. Priskyrimo puslapyje atlikite šiuos veiksmus:

    - Rolės puslapyje įveskite *Storage Blob Data Reader* į **paieškos juostą** ir pasirinkite **Storage Blob Data Reader** iš pasirodžiusių parinkčių.
    - Rolės puslapyje pasirinkite **Next**.
    - Narių puslapyje pasirinkite **Assign access to** **Managed identity**.
    - Narių puslapyje pasirinkite **+ Select members**.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Valdomą tapatybę** kaip **Manage Identity**.
    - Pasirinkite valdomą tapatybę, kurią sukūrėte. Pavyzdžiui, *finetunephi-managedidentity*.
    - Pasirinkite **Select**.

    ![Pasirinkite valdomą tapatybę.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-08-select-managed-identity.png)

1. Pasirinkite **Review + assign**.

#### Pridėti AcrPull rolės priskyrimą valdomai tapatybei

1. Įveskite *container registries* į **paieškos juostą** portalo puslapio viršuje ir pasirinkite **Container registries** iš pasirodžiusių parinkčių.

    ![Įveskite container registries.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-09-type-container-registries.png)

1. Pasirinkite konteinerių registrą, susijusį su Azure Machine Learning workspace. Pavyzdžiui, *finetunephicontainerregistry*

1. Atlikite šiuos veiksmus, kad pereitumėte į Pridėti rolės priskyrimo puslapį:

    - Pasirinkite **Access Control (IAM)** iš kairės pusės skirtuko.
    - Pasirinkite **+ Add** iš navigacijos meniu.
    - Pasirinkite **Add role assignment** iš navigacijos meniu.

1. Priskyrimo puslapyje atlikite šiuos veiksmus:

    - Rolės puslapyje įveskite *AcrPull* į **paieškos juostą** ir pasirinkite **AcrPull** iš pasirodžiusių parinkčių.
    - Rolės puslapyje pasirinkite **Next**.
    - Narių puslapyje pasirinkite **Assign access to** **Managed identity**.
    - Narių puslapyje pasirinkite **+ Select members**.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Valdomą tapatybę** kaip **Manage Identity**.
    - Pasirinkite valdomą tapatybę, kurią sukūrėte. Pavyzdžiui, *finetunephi-managedidentity*.
    - Pasirinkite **Select**.
    - Pasirinkite **Review + assign**.

### Nustatyti projektą

Norėdami atsisiųsti duomenų rinkinius, reikalingus tobulinimui, nustatysite vietinę aplinką.

Šiame pratime jūs:

- Sukursite aplanką darbui.
- Sukursite virtualią aplinką.
- Įdiegsite reikalingus paketus.
- Sukursite *download_dataset.py* failą duomenų rinkiniui atsisiųsti.

#### Sukurti aplanką darbui

1. Atidarykite terminalo langą ir įveskite šią komandą, kad sukurtumėte aplanką pavadinimu *finetune-phi* numatytame kelyje.

    ```console
    mkdir finetune-phi
    ```

2. Įveskite šią komandą savo terminale, kad pereitumėte į sukurtą *finetune-phi* aplanką.
#### Sukurkite virtualią aplinką

1. Įveskite šią komandą terminale, kad sukurtumėte virtualią aplinką pavadinimu *.venv*.

    ```console
    python -m venv .venv
    ```

2. Įveskite šią komandą terminale, kad aktyvuotumėte virtualią aplinką.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jei viskas pavyko, prieš komandų eilutę turėtumėte matyti *(.venv)*.

#### Įdiekite reikalingus paketus

1. Įveskite šias komandas terminale, kad įdiegtumėte reikalingus paketus.

    ```console
    pip install datasets==2.19.1
    ```

#### Sukurkite `download_dataset.py`

> [!NOTE]
> Pilna aplanko struktūra:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Atidarykite **Visual Studio Code**.

1. Pasirinkite **File** iš meniu juostos.

1. Pasirinkite **Open Folder**.

1. Pasirinkite aplanką *finetune-phi*, kurį sukūrėte, esantį *C:\Users\yourUserName\finetune-phi*.

    ![Pasirinkite sukurtą aplanką.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-01-open-project-folder.png)

1. Kairėje Visual Studio Code pusėje spustelėkite dešiniuoju pelės mygtuku ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *download_dataset.py*.

    ![Sukurkite naują failą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-02-create-new-file.png)

### Paruoškite duomenų rinkinį modelio tobulinimui

Šioje užduotyje paleisite *download_dataset.py* failą, kad atsisiųstumėte *ultrachat_200k* duomenų rinkinius į savo vietinę aplinką. Tada naudosite šiuos duomenų rinkinius Phi-3 modelio tobulinimui Azure Machine Learning platformoje.

Šioje užduotyje atliksite:

- Pridėsite kodą į *download_dataset.py* failą, kad atsisiųstumėte duomenų rinkinius.
- Paleisite *download_dataset.py* failą, kad atsisiųstumėte duomenų rinkinius į savo vietinę aplinką.

#### Atsisiųskite duomenų rinkinį naudodami *download_dataset.py*

1. Atidarykite *download_dataset.py* failą Visual Studio Code.

1. Pridėkite šį kodą į *download_dataset.py* failą.

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

1. Įveskite šią komandą terminale, kad paleistumėte skriptą ir atsisiųstumėte duomenų rinkinį į savo vietinę aplinką.

    ```console
    python download_dataset.py
    ```

1. Patikrinkite, ar duomenų rinkiniai buvo sėkmingai išsaugoti vietiniame *finetune-phi/data* aplanke.

> [!NOTE]
>
> #### Pastaba apie duomenų rinkinio dydį ir tobulinimo laiką
>
> Šioje pamokoje naudojate tik 1% duomenų rinkinio (`split='train[:1%]'`). Tai žymiai sumažina duomenų kiekį, pagreitindama tiek įkėlimo, tiek tobulinimo procesus. Galite koreguoti procentą, kad rastumėte tinkamą balansą tarp mokymo laiko ir modelio našumo. Naudojant mažesnį duomenų rinkinio dalį, tobulinimo procesas tampa lengviau valdomas pamokos metu.

## Scenarijus 2: Tobulinkite Phi-3 modelį ir diekite jį Azure Machine Learning Studio

### Tobulinkite Phi-3 modelį

Šioje užduotyje tobulinsite Phi-3 modelį Azure Machine Learning Studio platformoje.

Šioje užduotyje atliksite:

- Sukursite kompiuterių klasterį modelio tobulinimui.
- Tobulinsite Phi-3 modelį Azure Machine Learning Studio.

#### Sukurkite kompiuterių klasterį modelio tobulinimui

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pasirinkite **Compute** iš kairės pusės skirtuko.

1. Pasirinkite **Compute clusters** iš navigacijos meniu.

1. Pasirinkite **+ New**.

    ![Pasirinkite kompiuterių klasterį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-01-select-compute.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Region**, kurį norite naudoti.
    - Pasirinkite **Virtual machine tier** į **Dedicated**.
    - Pasirinkite **Virtual machine type** į **GPU**.
    - Pasirinkite **Virtual machine size** filtrą į **Select from all options**.
    - Pasirinkite **Virtual machine size** į **Standard_NC24ads_A100_v4**.

    ![Sukurkite klasterį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-02-create-cluster.png)

1. Pasirinkite **Next**.

1. Atlikite šiuos veiksmus:

    - Įveskite **Compute name**. Jis turi būti unikalus.
    - Pasirinkite **Minimum number of nodes** į **0**.
    - Pasirinkite **Maximum number of nodes** į **1**.
    - Pasirinkite **Idle seconds before scale down** į **120**.

    ![Sukurkite klasterį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-03-create-cluster.png)

1. Pasirinkite **Create**.

#### Tobulinkite Phi-3 modelį

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pasirinkite Azure Machine Learning darbo sritį, kurią sukūrėte.

    ![Pasirinkite sukurtą darbo sritį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Model catalog** iš kairės pusės skirtuko.
    - Įveskite *phi-3-mini-4k* į **paieškos laukelį** ir pasirinkite **Phi-3-mini-4k-instruct** iš pasirodžiusių parinkčių.

    ![Įveskite phi-3-mini-4k.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-05-type-phi-3-mini-4k.png)

1. Pasirinkite **Fine-tune** iš navigacijos meniu.

    ![Pasirinkite tobulinimą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-06-select-fine-tune.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Select task type** į **Chat completion**.
    - Pasirinkite **+ Select data**, kad įkeltumėte **Mokymo duomenis**.
    - Pasirinkite **Validation data upload type** į **Provide different validation data**.
    - Pasirinkite **+ Select data**, kad įkeltumėte **Validacijos duomenis**.

    ![Užpildykite tobulinimo puslapį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-07-fill-finetuning.png)

    > [!TIP]
    >
    > Galite pasirinkti **Advanced settings**, kad pritaikytumėte konfigūracijas, tokias kaip **learning_rate** ir **lr_scheduler_type**, optimizuodami tobulinimo procesą pagal savo specifinius poreikius.

1. Pasirinkite **Finish**.

1. Šioje užduotyje sėkmingai patobulinote Phi-3 modelį naudodami Azure Machine Learning. Atkreipkite dėmesį, kad tobulinimo procesas gali užtrukti nemažai laiko. Po tobulinimo darbo paleidimo turite palaukti, kol jis bus baigtas. Galite stebėti tobulinimo darbo būseną, naršydami į **Jobs** skirtuką kairėje Azure Machine Learning darbo srities pusėje. Kitoje serijoje diegsite patobulintą modelį ir integruosite jį su Prompt flow.

    ![Peržiūrėkite tobulinimo darbą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-08-output.png)

### Diekite patobulintą Phi-3 modelį

Norėdami integruoti patobulintą Phi-3 modelį su Prompt flow, turite diegti modelį, kad jis būtų prieinamas realaus laiko prognozėms. Šis procesas apima modelio registravimą, internetinio galutinio taško sukūrimą ir modelio diegimą.

Šioje užduotyje atliksite:

- Registruosite patobulintą modelį Azure Machine Learning darbo srityje.
- Sukursite internetinį galutinį tašką.
- Diegsite registruotą patobulintą Phi-3 modelį.

#### Registruokite patobulintą modelį

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pasirinkite Azure Machine Learning darbo sritį, kurią sukūrėte.

    ![Pasirinkite sukurtą darbo sritį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. Pasirinkite **Models** iš kairės pusės skirtuko.
1. Pasirinkite **+ Register**.
1. Pasirinkite **From a job output**.

    ![Registruokite modelį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-01-register-model.png)

1. Pasirinkite darbą, kurį sukūrėte.

    ![Pasirinkite darbą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-02-select-job.png)

1. Pasirinkite **Next**.

1. Pasirinkite **Model type** į **MLflow**.

1. Įsitikinkite, kad **Job output** yra pasirinktas; jis turėtų būti automatiškai pasirinktas.

    ![Pasirinkite išvestį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-03-select-output.png)

2. Pasirinkite **Next**.

3. Pasirinkite **Register**.

    ![Pasirinkite registravimą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-04-register.png)

4. Galite peržiūrėti registruotą modelį, naršydami į **Models** meniu iš kairės pusės skirtuko.

    ![Registruotas modelis.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-05-registered-model.png)

#### Diekite patobulintą modelį

1. Naršykite į Azure Machine Learning darbo sritį, kurią sukūrėte.

1. Pasirinkite **Endpoints** iš kairės pusės skirtuko.

1. Pasirinkite **Real-time endpoints** iš navigacijos meniu.

    ![Sukurkite galutinį tašką.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-06-create-endpoint.png)

1. Pasirinkite **Create**.

1. Pasirinkite registruotą modelį, kurį sukūrėte.

    ![Pasirinkite registruotą modelį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-07-select-registered-model.png)

1. Pasirinkite **Select**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Virtual machine** į *Standard_NC6s_v3*.
    - Pasirinkite **Instance count**, kurį norite naudoti. Pavyzdžiui, *1*.
    - Pasirinkite **Endpoint** į **New**, kad sukurtumėte galutinį tašką.
    - Įveskite **Endpoint name**. Jis turi būti unikalus.
    - Įveskite **Deployment name**. Jis turi būti unikalus.

    ![Užpildykite diegimo nustatymus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-08-deployment-setting.png)

1. Pasirinkite **Deploy**.

> [!WARNING]
> Kad išvengtumėte papildomų mokesčių savo paskyroje, įsitikinkite, kad ištrynėte sukurtą galutinį tašką Azure Machine Learning darbo srityje.
>

#### Patikrinkite diegimo būseną Azure Machine Learning darbo srityje

1. Naršykite į Azure Machine Learning darbo sritį, kurią sukūrėte.

1. Pasirinkite **Endpoints** iš kairės pusės skirtuko.

1. Pasirinkite galutinį tašką, kurį sukūrėte.

    ![Pasirinkite galutinius taškus](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-09-check-deployment.png)

1. Šiame puslapyje galite valdyti galutinius taškus diegimo proceso metu.

> [!NOTE]
> Kai diegimas bus baigtas, įsitikinkite, kad **Live traffic** nustatytas į **100%**. Jei ne, pasirinkite **Update traffic**, kad koreguotumėte srauto nustatymus. Atkreipkite dėmesį, kad negalite testuoti modelio, jei srautas nustatytas į 0%.
>
> ![Nustatykite srautą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-10-set-traffic.png)
>

## Scenarijus 3: Integracija su Prompt flow ir pokalbiai su jūsų pritaikytu modeliu Azure AI Foundry

### Integruokite pritaikytą Phi-3 modelį su Prompt flow

Po sėkmingo patobulinto modelio diegimo dabar galite integruoti jį su Prompt Flow, kad galėtumėte naudoti modelį realaus laiko programose, leidžiančiose atlikti įvairias interaktyvias užduotis su jūsų pritaikytu Phi-3 modeliu.

Šioje užduotyje atliksite:

- Sukursite Azure AI Foundry Hub.
- Sukursite Azure AI Foundry Project.
- Sukursite Prompt flow.
- Pridėsite pritaikytą ryšį patobulintam Phi-3 modeliui.
- Nustatysite Prompt flow pokalbiams su jūsų pritaikytu Phi-3 modeliu.
> [!NOTE]  
> Taip pat galite integruoti su Promptflow naudodami Azure ML Studio. Tas pats integracijos procesas gali būti taikomas Azure ML Studio.
#### Sukurkite Azure AI Foundry centrą

Prieš kurdami projektą, turite sukurti centrą. Centras veikia kaip išteklių grupė, leidžianti organizuoti ir valdyti kelis projektus Azure AI Foundry platformoje.

1. Apsilankykite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Kairėje pusėje pasirinkite **Visi centrai**.

1. Iš navigacijos meniu pasirinkite **+ Naujas centras**.

    ![Sukurti centrą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-01-create-hub.png)

1. Atlikite šiuos veiksmus:

    - Įveskite **Centro pavadinimą**. Jis turi būti unikalus.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Išteklių grupę**, kurią norite naudoti (jei reikia, sukurkite naują).
    - Pasirinkite **Vietą**, kurią norite naudoti.
    - Pasirinkite **Prisijungti prie Azure AI paslaugų**, kurias norite naudoti (jei reikia, sukurkite naują).
    - Pasirinkite **Prisijungti prie Azure AI paieškos** ir **Praleisti prisijungimą**.

    ![Užpildyti centrą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-02-fill-hub.png)

1. Pasirinkite **Toliau**.

#### Sukurkite Azure AI Foundry projektą

1. Sukurtame centre pasirinkite **Visi projektai** iš kairės pusės meniu.

1. Iš navigacijos meniu pasirinkite **+ Naujas projektas**.

    ![Pasirinkti naują projektą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-04-select-new-project.png)

1. Įveskite **Projekto pavadinimą**. Jis turi būti unikalus.

    ![Sukurti projektą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-05-create-project.png)

1. Pasirinkite **Sukurti projektą**.

#### Pridėkite tinkintą ryšį su pritaikytu Phi-3 modeliu

Norėdami integruoti savo pritaikytą Phi-3 modelį su Prompt flow, turite išsaugoti modelio galinį tašką ir raktą tinkintame ryšyje. Ši sąranka užtikrina prieigą prie jūsų pritaikyto Phi-3 modelio Prompt flow aplinkoje.

#### Nustatykite pritaikyto Phi-3 modelio API raktą ir galinio taško URI

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Eikite į sukurtą Azure Machine Learning darbo sritį.

1. Kairėje pusėje pasirinkite **Galiniai taškai**.

    ![Pasirinkti galinius taškus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-06-select-endpoints.png)

1. Pasirinkite sukurtą galinį tašką.

    ![Pasirinkti sukurtą galinį tašką.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-07-select-endpoint-created.png)

1. Iš navigacijos meniu pasirinkite **Naudoti**.

1. Nukopijuokite savo **REST galinį tašką** ir **Pirminį raktą**.

    ![Nukopijuoti API raktą ir galinio taško URI.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-08-copy-endpoint-key.png)

#### Pridėkite tinkintą ryšį

1. Apsilankykite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Eikite į sukurtą Azure AI Foundry projektą.

1. Sukurtame projekte pasirinkite **Nustatymai** iš kairės pusės meniu.

1. Pasirinkite **+ Naujas ryšys**.

    ![Pasirinkti naują ryšį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-09-select-new-connection.png)

1. Iš navigacijos meniu pasirinkite **Tinkinti raktai**.

    ![Pasirinkti tinkintus raktus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-10-select-custom-keys.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **+ Pridėti rakto ir reikšmės poras**.
    - Rakto pavadinimui įveskite **endpoint** ir įklijuokite galinį tašką, kurį nukopijavote iš Azure ML Studio, į reikšmės lauką.
    - Dar kartą pasirinkite **+ Pridėti rakto ir reikšmės poras**.
    - Rakto pavadinimui įveskite **key** ir įklijuokite raktą, kurį nukopijavote iš Azure ML Studio, į reikšmės lauką.
    - Po rakto pridėjimo pasirinkite **yra slaptas**, kad raktas nebūtų atskleistas.

    ![Pridėti ryšį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-11-add-connection.png)

1. Pasirinkite **Pridėti ryšį**.

#### Sukurkite Prompt flow

Jūs pridėjote tinkintą ryšį Azure AI Foundry platformoje. Dabar sukurkime Prompt flow naudodami šiuos veiksmus. Tada prijungsite šį Prompt flow prie tinkinto ryšio, kad galėtumėte naudoti pritaikytą modelį Prompt flow aplinkoje.

1. Eikite į sukurtą Azure AI Foundry projektą.

1. Pasirinkite **Prompt flow** iš kairės pusės meniu.

1. Iš navigacijos meniu pasirinkite **+ Kurti**.

    ![Pasirinkti Prompt flow.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-12-select-promptflow.png)

1. Iš navigacijos meniu pasirinkite **Pokalbių srautas**.

    ![Pasirinkti pokalbių srautą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-13-select-flow-type.png)

1. Įveskite **Aplanko pavadinimą**, kurį norite naudoti.

    ![Įvesti pavadinimą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-14-enter-name.png)

2. Pasirinkite **Kurti**.

#### Nustatykite Prompt flow pokalbiui su pritaikytu Phi-3 modeliu

Jums reikia integruoti pritaikytą Phi-3 modelį į Prompt flow. Tačiau esamas Prompt flow nėra pritaikytas šiam tikslui. Todėl turite pertvarkyti Prompt flow, kad galėtumėte integruoti tinkintą modelį.

1. Prompt flow aplinkoje atlikite šiuos veiksmus, kad pertvarkytumėte esamą srautą:

    - Pasirinkite **Neapdoroto failo režimą**.
    - Ištrinkite visą esamą kodą *flow.dag.yml* faile.
    - Į *flow.dag.yml* failą įtraukite šį kodą:

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

    - Pasirinkite **Išsaugoti**.

    ![Pasirinkti neapdoroto failo režimą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-15-select-raw-file-mode.png)

1. Į *integrate_with_promptflow.py* failą įtraukite šį kodą, kad Prompt flow aplinkoje galėtumėte naudoti pritaikytą Phi-3 modelį.

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

    ![Įklijuoti Prompt flow kodą.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-16-paste-promptflow-code.png)

> [!NOTE]
> Daugiau informacijos apie Prompt flow naudojimą Azure AI Foundry platformoje rasite [Prompt flow Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pasirinkite **Pokalbio įvestį**, **Pokalbio išvestį**, kad galėtumėte bendrauti su savo modeliu.

    ![Įvestis ir išvestis.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-17-select-input-output.png)

1. Dabar esate pasiruošę bendrauti su pritaikytu Phi-3 modeliu. Kitoje užduotyje sužinosite, kaip pradėti Prompt flow ir naudoti jį pokalbiui su pritaikytu Phi-3 modeliu.

> [!NOTE]
>
> Pertvarkytas srautas turėtų atrodyti kaip paveikslėlyje žemiau:
>
> ![Srauto pavyzdys.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-18-graph-example.png)
>

### Pokalbis su pritaikytu Phi-3 modeliu

Dabar, kai pritaikėte ir integravote savo pritaikytą Phi-3 modelį su Prompt flow, esate pasiruošę pradėti bendrauti su juo. Ši užduotis padės jums nustatyti ir inicijuoti pokalbį su modeliu naudojant Prompt flow. Atlikdami šiuos veiksmus, galėsite pilnai išnaudoti pritaikyto Phi-3 modelio galimybes įvairioms užduotims ir pokalbiams.

- Bendraukite su pritaikytu Phi-3 modeliu naudodami Prompt flow.

#### Pradėkite Prompt flow

1. Pasirinkite **Pradėti skaičiavimo sesijas**, kad pradėtumėte Prompt flow.

    ![Pradėti skaičiavimo sesiją.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-01-start-compute-session.png)

1. Pasirinkite **Patvirtinti ir analizuoti įvestį**, kad atnaujintumėte parametrus.

    ![Patvirtinti įvestį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-02-validate-input.png)

1. Pasirinkite **Ryšio** reikšmę, kad prisijungtumėte prie sukurto tinkinto ryšio. Pavyzdžiui, *connection*.

    ![Ryšys.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-03-select-connection.png)

#### Pokalbis su pritaikytu modeliu

1. Pasirinkite **Pokalbis**.

    ![Pasirinkti pokalbį.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-04-select-chat.png)

1. Štai pavyzdys, kaip atrodo rezultatai: Dabar galite bendrauti su pritaikytu Phi-3 modeliu. Rekomenduojama užduoti klausimus, pagrįstus duomenimis, naudotais pritaikymui.

    ![Pokalbis su Prompt flow.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-05-chat-with-promptflow.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.