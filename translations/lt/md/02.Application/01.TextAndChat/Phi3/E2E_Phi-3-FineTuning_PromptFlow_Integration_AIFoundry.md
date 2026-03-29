# Tikslinė redagavimo ir integracija su Prompt flow pritaikytais Phi-3 modeliais Microsoft Foundry

Šis end-to-end (E2E) pavyzdys yra pagrįstas vadovu „[Tikslinė redagavimo ir integracija su pritaikytais Phi-3 modeliais naudojant Prompt Flow Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)“ iš Microsoft Tech Community. Jame pristatomi procesai, kaip atlikti tikslinį modelio redagavimą, diegimą ir integraciją su pritaikytais Phi-3 modeliais naudojant Prompt flow Microsoft Foundry.
Skirtingai nuo E2E pavyzdžio „[Tikslinė redagavimo ir integracija su pritaikytais Phi-3 modeliais naudojant Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)“, kuriame reikėjo vykdyti kodą vietoje, ši pamoka visiškai skirta tiksliniam redagavimui ir modelio integracijai Azure AI / ML studijoje.

## Apžvalga

Šiame E2E pavyzdyje išmoksite, kaip tiksliai redaguoti Phi-3 modelį ir integruoti jį su Prompt flow Microsoft Foundry platformoje. Naudodamiesi Azure AI / ML studija sukursite darbo eigą, skirtą pritaikytų DI modelių diegimui ir naudojimui. Šis E2E pavyzdys padalintas į tris scenarijus:

**Scenarijus 1: Azure išteklių nustatymas ir pasirengimas tiksliniam redagavimui**

**Scenarijus 2: Phi-3 modelio tikslinis redagavimas ir diegimas Azure Machine Learning Studio**

**Scenarijus 3: Integracija su Prompt flow ir pokalbis su pritaikytu modeliu Microsoft Foundry**

Čia pateikiama šio E2E pavyzdžio apžvalga.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/lt/00-01-architecture.198ba0f1ae6d841a.webp)

### Turinys

1. **[Scenarijus 1: Azure išteklių nustatymas ir pasiruošimas tiksliniam redagavimui](#scenarijus-1-azure-išteklių-nustatymas-ir-pasirengimas-tiksliniam-redagavimui)**
    - [Azure Machine Learning darbo srities kūrimas](#azure-machine-learning-darbo-srities-kūrimas)
    - [GPU kvotų prašymas Azure prenumeratoje](#gpu-kvotų-prašymas-azure-prenumeratoje)
    - [Rolės priskyrimas](#rolės-priskyrimas)
    - [Projekto nustatymas](#projekto-nustatymas)
    - [Duomenų rinkinio paruošimas tiksliniam redagavimui](#paruoškite-duomenų-rinkinį-smulkiam-apmokymui)

1. **[Scenarijus 2: Phi-3 modelio tikslinis redagavimas ir diegimas Azure Machine Learning Studio](#scenarijus-2-smulkiai-apmokykite-phi-3-modelį-ir-išdiekite-azure-machine-learning-studio)**
    - [Tikslinis Phi-3 modelio redagavimas](#smulkus-phi-3-modelio-apmokymas)
    - [Tiksliai redaguoto Phi-3 modelio diegimas](#išdiekite-smulkiai-apmokytą-phi-3-modelį)

1. **[Scenarijus 3: Integracija su Prompt flow ir pokalbis su pritaikytu modeliu Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integracija su Prompt flow pritaikyto Phi-3 modelio](#integruokite-suasmenintą-phi-3-modelį-su-prompt-flow)
    - [Pokalbis su savo pritaikytu Phi-3 modeliu](#bendraukite-su-savo-vartotojišku-phi-3-modeliu)

## Scenarijus 1: Azure išteklių nustatymas ir pasirengimas tiksliniam redagavimui

### Azure Machine Learning darbo srities kūrimas

1. Įveskite *azure machine learning* į **paieškos juostą** puslapio viršuje ir pasirinkite **Azure Machine Learning** iš pasirodžiusių variantų.

    ![Type azure machine learning.](../../../../../../translated_images/lt/01-01-type-azml.acae6c5455e67b4b.webp)

2. Iš naršymo meniu pasirinkite **+ Create**.

3. Iš naršymo meniu pasirinkite **New workspace**.

    ![Select new workspace.](../../../../../../translated_images/lt/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Atlikite šiuos veiksmus:

    - Pasirinkite savo Azure **Subscription**.
    - Pasirinkite naudotiną **Resource group** (sukurkite naują, jei reikia).
    - Įveskite **Workspace Name**. Tai turi būti unikalus pavadinimas.
    - Pasirinkite norimą **Region**.
    - Pasirinkite naudotiną **Storage account** (sukurkite naują, jei reikia).
    - Pasirinkite naudotiną **Key vault** (sukurkite naują, jei reikia).
    - Pasirinkite naudotiną **Application insights** (sukurkite naują, jei reikia).
    - Pasirinkite naudotiną **Container registry** (sukurkite naują, jei reikia).

    ![Fill azure machine learning.](../../../../../../translated_images/lt/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Pasirinkite **Review + Create**.

6. Pasirinkite **Create**.

### GPU kvotų prašymas Azure prenumeratoje

Šioje pamokoje sužinosite, kaip tiksliai redaguoti ir diegti Phi-3 modelį naudojant GPU. Tiksliniam redagavimui naudosite *Standard_NC24ads_A100_v4* GPU, kuriam reikalingas kvotos prašymas. Diegimui naudosite *Standard_NC6s_v3* GPU, kuris taip pat reikalauja kvotos prašymo.

> [!NOTE]
>
> Tik Pay-As-You-Go prenumeratos (standartinis prenumeratos tipas) yra tinkamos GPU paskirstymui; naudos prenumeratos šiuo metu nepalaikomos.
>

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Atlikite šiuos veiksmus, kad paprašytumėte *Standard NCADSA100v4 šeimos* kvotą:

    - Kairėje pusėje pasirinkite **Quota**.
    - Pasirinkite naudotiną **Virtual machine family**. Pavyzdžiui, pasirinkite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, kuri apima *Standard_NC24ads_A100_v4* GPU.
    - Iš naršymo meniu pasirinkite **Request quota**.

        ![Request quota.](../../../../../../translated_images/lt/02-02-request-quota.c0428239a63ffdd5.webp)

    - Kvotos prašymo puslapyje įveskite norimą **New cores limit** (pvz., 24).
    - Kvotos prašymo puslapyje pasirinkite **Submit**, kad pateiktumėte GPU kvotos prašymą.

1. Atlikite šiuos veiksmus, kad paprašytumėte *Standard NCSv3 šeimos* kvotą:

    - Kairėje pusėje pasirinkite **Quota**.
    - Pasirinkite naudotiną **Virtual machine family**. Pavyzdžiui, pasirinkite **Standard NCSv3 Family Cluster Dedicated vCPUs**, kuri apima *Standard_NC6s_v3* GPU.
    - Iš naršymo meniu pasirinkite **Request quota**.
    - Kvotos prašymo puslapyje įveskite norimą **New cores limit** (pvz., 24).
    - Kvotos prašymo puslapyje pasirinkite **Submit**, kad pateiktumėte GPU kvotos prašymą.

### Rolės priskyrimas

Norėdami tiksliai redaguoti ir diegti savo modelius, pirmiausia turite sukurti naudotojo priskirtą valdomą tapatybę (User Assigned Managed Identity, UAI) ir priskirti jai tinkamas teises. Ši UAI bus naudojama autentifikacijai diegimo metu.

#### Naudotojo priskirtos valdomos tapatybės kūrimas (UAI)

1. Įveskite *managed identities* į **paieškos juostą** puslapio viršuje ir pasirinkite **Managed Identities** iš pasirodžiusių variantų.

    ![Type managed identities.](../../../../../../translated_images/lt/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Pasirinkite **+ Create**.

    ![Select create.](../../../../../../translated_images/lt/03-02-select-create.92bf8989a5cd98f2.webp)

1. Atlikite šiuos veiksmus:

    - Pasirinkite savo Azure **Subscription**.
    - Pasirinkite naudotiną **Resource group** (sukurkite naują, jei reikia).
    - Pasirinkite norimą **Region**.
    - Įveskite **Name**. Tai turi būti unikalus pavadinimas.

    ![Select create.](../../../../../../translated_images/lt/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Pasirinkite **Review + create**.

1. Pasirinkite **+ Create**.

#### Priskirkite valdytojo (Contributor) rolę valdomajai tapatybei

1. Eikite į sukurtą valdomos tapatybės išteklių puslapį.

1. Kairėje pusėje pasirinkite **Azure role assignments**.

1. Naršymo meniu pasirinkite **+Add role assignment**.

1. Pridėjimo rolės priskyrimo puslapyje atlikite šiuos veiksmus:
    - Pasirinkite **Scope** kaip **Resource group**.
    - Pasirinkite savo Azure **Subscription**.
    - Pasirinkite naudotiną **Resource group**.
    - Pasirinkite rolę **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/lt/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Paspauskite **Save**.

#### Priskirkite Storage Blob Data Reader rolę valdomajai tapatybei

1. Įveskite *storage accounts* į **paieškos juostą** puslapio viršuje ir pasirinkite **Storage accounts** iš pasirodžiusių variantų.

    ![Type storage accounts.](../../../../../../translated_images/lt/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Pasirinkite storage paskyrą, susijusią su sukurtu Azure Machine Learning darbo srities pavadinimu. Pavyzdžiui, *finetunephistorage*.

1. Atlikite šiuos veiksmus, kad pasiektumėte rolės priskyrimo puslapį:

    - Eikite į sukurtą Azure Storage paskyrą.
    - Kairėje pusėje pasirinkite **Access Control (IAM)**.
    - Naršymo meniu pasirinkite **+ Add**.
    - Pasirinkite **Add role assignment**.

    ![Add role.](../../../../../../translated_images/lt/03-06-add-role.353ccbfdcf0789c2.webp)

1. Rolės priskyrimo puslapyje atlikite šiuos veiksmus:

    - Rolės puslapyje įveskite *Storage Blob Data Reader* į **paieškos juostą** ir pasirinkite iš sąrašo **Storage Blob Data Reader**.
    - Rolės puslapyje pasirinkite **Next**.
    - Narių puslapyje pasirinkite **Assign access to** kaip **Managed identity**.
    - Narių puslapyje pasirinkite **+ Select members**.
    - Puslapyje „Pasirinkti valdomas tapatybes“ pasirinkite savo Azure **Subscription**.
    - Pasirinkite valdomąją tapatybę kaip **Manage Identity**.
    - Pasirinkite anksčiau sukurtą valdomą tapatybę, pavyzdžiui, *finetunephi-managedidentity*.
    - Pasirinkite **Select**.

    ![Select managed identity.](../../../../../../translated_images/lt/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Paspauskite **Review + assign**.

#### Priskirkite AcrPull rolę valdomajai tapatybei

1. Įveskite *container registries* į **paieškos juostą** puslapio viršuje ir pasirinkite **Container registries** iš pasirodžiusių variantų.

    ![Type container registries.](../../../../../../translated_images/lt/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Pasirinkite konteinerių registrą, susietą su Azure Machine Learning darbo sritimi. Pavyzdžiui, *finetunephicontainerregistry*.

1. Atlikite šiuos veiksmus, kad pasiektumėte rolės priskyrimo puslapį:

    - Kairėje pusėje pasirinkite **Access Control (IAM)**.
    - Naršymo meniu pasirinkite **+ Add**.
    - Pasirinkite **Add role assignment**.

1. Rolės priskyrimo puslapyje atlikite šiuos veiksmus:

    - Rolės puslapyje įveskite *AcrPull* į **paieškos juostą** ir pasirinkite iš sąrašo **AcrPull**.
    - Rolės puslapyje pasirinkite **Next**.
    - Narių puslapyje pasirinkite **Assign access to** kaip **Managed identity**.
    - Narių puslapyje pasirinkite **+ Select members**.
    - Puslapyje „Pasirinkti valdomas tapatybes“ pasirinkite savo Azure **Subscription**.
    - Pasirinkite valdomąją tapatybę kaip **Manage Identity**.
    - Pasirinkite anksčiau sukurtą valdomą tapatybę, pvz., *finetunephi-managedidentity*.
    - Pasirinkite **Select**.
    - Paspauskite **Review + assign**.

### Projekto nustatymas

Norėdami atsisiųsti duomenų rinkinius, reikalingus tiksliniam redagavimui, nustatysite vietinę aplinką.

Šiame pratime jūs:

- Sukursite aplanką darbui.
- Sukursite virtualią aplinką.
- Įdiegsite reikiamas paketas.
- Sukursite *download_dataset.py* failą, skirtą duomenų rinkinio atsisiuntimui.

#### Sukurkite aplanką darbui

1. Atverkite terminalo langą ir įveskite šią komandą, kad sukurtumėte aplanką pavadinimu *finetune-phi* numatytame kelyje.

    ```console
    mkdir finetune-phi
    ```

2. Įveskite šią komandą terminale, kad pereitumėte į ką tik sukurtą *finetune-phi* aplanką.

    ```console
    cd finetune-phi
    ```

#### Sukurkite virtualią aplinką

1. Įveskite šią komandą terminale, kad sukurtumėte virtualią aplinką pavadinimu *.venv*.
    ```console
    python -m venv .venv
    ```

2. Terminale įveskite šią komandą, kad suaktyvintumėte virtualią aplinką.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jei pavyko, prieš komandų eilutę turėtumėte matyti *(.venv)*.

#### Įdiekite reikalingus paketus

1. Terminale įveskite šias komandas, kad įdiegtumėte reikalingus paketus.

    ```console
    pip install datasets==2.19.1
    ```

#### Sukurkite `donload_dataset.py`

> [!NOTE]
> Pilna aplanko struktūra:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Atidarykite **Visual Studio Code**.

1. Meniu juostoje pasirinkite **File**.

1. Pasirinkite **Open Folder**.

1. Pasirinkite *finetune-phi* aplanką, kurį sukūrėte, esantį *C:\Users\yourUserName\finetune-phi*.

    ![Pasirinkite sukurtą aplanką.](../../../../../../translated_images/lt/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Kairėje Visual Studio Code pusėje dešiniu pelės mygtuku spustelėkite ir pasirinkite **New File**, kad sukurtumėte naują failą pavadinimu *download_dataset.py*.

    ![Sukurkite naują failą.](../../../../../../translated_images/lt/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Paruoškite duomenų rinkinį smulkiam apmokymui

Šioje užduotyje vykdysite *download_dataset.py* failą, kad atsisiųstumėte *ultrachat_200k* duomenų rinkinius į savo vietinę aplinką. Tuomet naudosite šiuos duomenų rinkinius Phi-3 modelio smulkiam apmokymui Azure Machine Learning platformoje.

Šioje užduotyje jūs:

- Pridėsite kodą į *download_dataset.py* failą, kad atsisiųstumėte duomenų rinkinius.
- Vykdysite *download_dataset.py* failą, kad atsisiųstumėte duomenų rinkinius į savo vietinę aplinką.

#### Atsisiųskite savo duomenų rinkinį naudodami *download_dataset.py*

1. Atidarykite *download_dataset.py* failą Visual Studio Code.

1. Įtraukite šį kodą į *download_dataset.py* failą.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Įkelkite duomenų rinkinį su nurodytu pavadinimu, konfigūracija ir padalijimo santykiu
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Padalinkite duomenų rinkinį į mokymo ir testavimo rinkinius (80% mokymo, 20% testavimo)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Sukurkite katalogą, jei jis neegzistuoja
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Atidarykite failą rašymo režimu
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iteruokite per kiekvieną įrašą duomenų rinkinyje
            for record in dataset:
                # Išsaugokite įrašą kaip JSON objektą ir rašykite jį į failą
                json.dump(record, f)
                # Parašykite naujos eilutės simbolį, kad atskirtumėte įrašus
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Įkelkite ir padalinkite ULTRACHAT_200k duomenų rinkinį su konkrečia konfigūracija ir padalijimo santykiu
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Išskirkite mokymo ir testavimo duomenų rinkinius iš padalinimo
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Išsaugokite mokymo duomenų rinkinį į JSONL failą
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Išsaugokite testavimo duomenų rinkinį į atskirą JSONL failą
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Terminale įveskite šią komandą, kad paleistumėte skriptą ir atsisiųstumėte duomenų rinkinį į savo vietinę aplinką.

    ```console
    python download_dataset.py
    ```

1. Patikrinkite, ar duomenų rinkiniai buvo sėkmingai išsaugoti jūsų vietiniame *finetune-phi/data* kataloge.

> [!NOTE]
>
> #### Pastaba apie duomenų rinkinio dydį ir smulkiojo apmokymo laiką
>
> Šiame vadove naudojate tik 1% duomenų rinkinio (`split='train[:1%]'`). Tai ženkliai sumažina duomenų kiekį, pagreitindamas tiek įkėlimą, tiek smulkųjį apmokymą. Galite reguliuoti procentinę dalį, kad rastumėte tinkamą pusiausvyrą tarp mokymo laiko ir modelio našumo. Naudojant mažesnę duomenų rinkinio dalį, sumažėja smulkiojo apmokymo laikas, o procesas tampa valdomesnis vadovėliui.

## Scenarijus 2: Smulkiai apmokykite Phi-3 modelį ir išdiekite Azure Machine Learning Studio

### Smulkus Phi-3 modelio apmokymas

Šioje užduotyje smulkiai apmokysite Phi-3 modelį Azure Machine Learning Studio aplinkoje.

Šioje užduotyje jūs:

- Sukursite kompiuterių klasterį smulkiam apmokymui.
- Smulkiai apmokysite Phi-3 modelį Azure Machine Learning Studio aplinkoje.

#### Sukurkite kompiuterių klasterį smulkiam apmokymui

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Kairėje pusėje pasirinkite **Compute**.

1. Navigacijos meniu pasirinkite **Compute clusters**.

1. Paspauskite **+ New**.

    ![Pasirinkite compute.](../../../../../../translated_images/lt/06-01-select-compute.a29cff290b480252.webp)

1. Atlikite šiuos veiksmus:

    - Pasirinkite norimą **Region**.
    - Pasirinkite **Virtual machine tier** kaip **Dedicated**.
    - Pasirinkite **Virtual machine type** kaip **GPU**.
    - Filtruokite **Virtual machine size** pasirinkdami **Select from all options**.
    - Pasirinkite **Virtual machine size** *Standard_NC24ads_A100_v4*.

    ![Sukurkite klasterį.](../../../../../../translated_images/lt/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Paspauskite **Next**.

1. Atlikite šiuos veiksmus:

    - Įveskite **Compute name**, kuris turi būti unikalus.
    - Nustatykite **Minimum number of nodes** į **0**.
    - Nustatykite **Maximum number of nodes** į **1**.
    - Nustatykite **Idle seconds before scale down** į **120**.

    ![Sukurkite klasterį.](../../../../../../translated_images/lt/06-03-create-cluster.4a54ba20914f3662.webp)

1. Paspauskite **Create**.

#### Smulkiai apmokykite Phi-3 modelį

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pasirinkite sukurtą Azure Machine Learning darbo sritį.

    ![Pasirinkite sukurtą darbo sritį.](../../../../../../translated_images/lt/06-04-select-workspace.a92934ac04f4f181.webp)

1. Atlikite šiuos veiksmus:

    - Kairėje pusėje pasirinkite **Model catalog**.
    - Paieškos juostoje įveskite *phi-3-mini-4k* ir pasirinkite **Phi-3-mini-4k-instruct** iš pasirodžiusių variantų.

    ![Įveskite phi-3-mini-4k.](../../../../../../translated_images/lt/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Navigacijos meniu pasirinkite **Fine-tune**.

    ![Pasirinkite fine tune.](../../../../../../translated_images/lt/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Select task type** kaip **Chat completion**.
    - Pasirinkite **+ Select data**, kad įkeltumėte **Training data**.
    - Validacijos duomenų įkėlimo tipą pasirinkite kaip **Provide different validation data**.
    - Pasirinkite **+ Select data**, kad įkeltumėte **Validation data**.

    ![Užpildykite smulkiojo apmokymo puslapį.](../../../../../../translated_images/lt/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Galite pasirinkti **Advanced settings**, kad pritaikytumėte parametrus, tokius kaip **learning_rate** ir **lr_scheduler_type**, optimizuodami smulkiojo apmokymo procesą pagal savo poreikius.

1. Paspauskite **Finish**.

1. Šioje užduotyje sėkmingai smulkiai apmokėte Phi-3 modelį Azure Machine Learning platformoje. Atkreipkite dėmesį, kad smulkiojo apmokymo procesas gali užtrukti nemažai laiko. Paleidę smulkiojo apmokymo užduotį, turėsite palaukti, kol ji bus baigta. Galite stebėti apmokymo užduoties būseną eikite į Jobs skirtuką kairėje Azure Machine Learning darbo srityje. Sekančiame serijos etape išdėstysite smulkiai apmokytą modelį ir integruosite jį su Prompt flow.

    ![Žiūrėkite smulkiojo apmokymo užduotį.](../../../../../../translated_images/lt/06-08-output.2bd32e59930672b1.webp)

### Išdiekite smulkiai apmokytą Phi-3 modelį

Norint integruoti smulkiai apmokytą Phi-3 modelį su Prompt flow, reikia išdiegti modelį, kad būtų pasiekiamas realaus laiko prognozėms. Šis procesas apima modelio registraciją, internetinio pabaigos taško sukūrimą ir modelio išdiegimą.

Šioje užduotyje jūs:

- Užregistruosite smulkiai apmokytą modelį Azure Machine Learning darbo srityje.
- Sukursite internetinį pabaigos tašką.
- Išdiegsite užregistruotą smulkiai apmokytą Phi-3 modelį.

#### Užregistruokite smulkiai apmokytą modelį

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pasirinkite sukurtą Azure Machine Learning darbo sritį.

    ![Pasirinkite sukurtą darbo sritį.](../../../../../../translated_images/lt/06-04-select-workspace.a92934ac04f4f181.webp)

1. Kairėje pusėje pasirinkite **Models**.
1. Paspauskite **+ Register**.
1. Pasirinkite **From a job output**.

    ![Užregistruokite modelį.](../../../../../../translated_images/lt/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Pasirinkite sukurtą užduotį.

    ![Pasirinkite užduotį.](../../../../../../translated_images/lt/07-02-select-job.3e2e1144cd6cd093.webp)

1. Paspauskite **Next**.

1. Pasirinkite **Model type** - **MLflow**.

1. Užtikrinkite, kad pasirinktas **Job output**; jis turėtų būti pasirenkamas automatiškai.

    ![Pasirinkite output.](../../../../../../translated_images/lt/07-03-select-output.4cf1a0e645baea1f.webp)

2. Paspauskite **Next**.

3. Paspauskite **Register**.

    ![Pasirinkite register.](../../../../../../translated_images/lt/07-04-register.fd82a3b293060bc7.webp)

4. Užregistruotą modelį galite peržiūrėti pasirinkę meniu punktą **Models** kairėje pusėje.

    ![Užregistruotas modelis.](../../../../../../translated_images/lt/07-05-registered-model.7db9775f58dfd591.webp)

#### Išdiekite smulkiai apmokytą modelį

1. Eikite į sukurtą Azure Machine Learning darbo sritį.

1. Pasirinkite **Endpoints** kairėje pusėje.

1. Navigacijos meniu pasirinkite **Real-time endpoints**.

    ![Sukurkite pabaigos tašką.](../../../../../../translated_images/lt/07-06-create-endpoint.1ba865c606551f09.webp)

1. Paspauskite **Create**.

1. Pasirinkite sukurtą užregistruotą modelį.

    ![Pasirinkite užregistruotą modelį.](../../../../../../translated_images/lt/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Paspauskite **Select**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Virtual machine** kaip *Standard_NC6s_v3*.
    - Pasirinkite norimą **Instance count**, pavyzdžiui, *1*.
    - Pasirinkite **Endpoint** kaip **New**, kad sukurtumėte naują pabaigos tašką.
    - Įveskite **Endpoint name**, kuris turi būti unikalus.
    - Įveskite **Deployment name**, kuris taip pat turi būti unikalus.

    ![Užpildykite išdiegimo nustatymus.](../../../../../../translated_images/lt/07-08-deployment-setting.43ddc4209e673784.webp)

1. Paspauskite **Deploy**.

> [!WARNING]
> Kad išvengtumėte papildomų mokesčių savo paskyrai, būtinai ištrinkite sukurtą pabaigos tašką Azure Machine Learning darbo srityje.
>

#### Patikrinkite išdiegimo būseną Azure Machine Learning darbo srityje

1. Eikite į sukurtą Azure Machine Learning darbo sritį.

1. Pasirinkite **Endpoints** kairėje pusėje.

1. Pasirinkite sukurtą pabaigos tašką.

    ![Pasirinkite pabaigos taškus](../../../../../../translated_images/lt/07-09-check-deployment.325d18cae8475ef4.webp)

1. Šiame puslapyje galite valdyti pabaigos taškus vykdant išdiegimo procesą.

> [!NOTE]
> Kai išdiegimas bus baigtas, įsitikinkite, kad **Live traffic** nustatyta į **100%**. Jei ne, pasirinkite **Update traffic** ir sureguliuokite srauto nustatymus. Atminkite, kad negalite testuoti modelio, jei srautas nustatytas į 0%.
>
> ![Nustatykite srautą.](../../../../../../translated_images/lt/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenarijus 3: Integracija su Prompt flow ir pokalbiai su jūsų suasmenintu modeliu Microsoft Foundry platformoje

### Integruokite suasmenintą Phi-3 modelį su Prompt flow

Sėkmingai išdiegę savo smulkiai apmokytą modelį, dabar galite jį integruoti su Prompt Flow, kad naudotumėte savo modelį realaus laiko programose, leidžiančiose atlikti įvairias sąveikių užduotis su suasmenintu Phi-3 modeliu.

Šioje užduotyje jūs:

- Sukursite Microsoft Foundry Hub.
- Sukursite Microsoft Foundry projektą.
- Sukursite Prompt flow.
- Pridėsite suasmenintą ryšį su smulkiai apmokytu Phi-3 modeliu.
- Suvesite Prompt flow, kad galėtumėte bendrauti su suasmenintu Phi-3 modeliu.

> [!NOTE]
> Taip pat galite integruotis su Promptflow naudodami Azure ML Studio. Tas pats integravimo procesas galioja Azure ML Studio aplinkoje.

#### Sukurkite Microsoft Foundry Hub

Prieš kuriant projektą, turite sukurti Hub. Hub veikia kaip Išteklių grupė, leidžianti organizuoti ir valdyti kelis projektus Microsoft Foundry platformoje.
1. Apsilankykite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pasirinkite **Visi centrai** iš kairėje esančio skirtuko.

1. Iš naršymo meniu pasirinkite **+ Naujas centras**.

    ![Sukurti centrą.](../../../../../../translated_images/lt/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Atlikite šiuos veiksmus:

    - Įveskite **Centro pavadinimą**. Jis turi būti unikalus.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite naudojamą **Išteklių grupę** (jei reikia, sukurkite naują).
    - Pasirinkite norimą naudoti **Vietą**.
    - Pasirinkite **Prisijungti prie Azure AI paslaugų** (jei reikia, sukurkite naują).
    - Pasirinkite **Prisijungti prie Azure AI paieškos** ir pasirinkite **Praleisti prisijungimą**.

    ![Užpildyti centrą.](../../../../../../translated_images/lt/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Pasirinkite **Toliau**.

#### Sukurti Microsoft Foundry projektą

1. Pasirinktame centre pasirinkite **Visi projektai** iš kairėje esančio skirtuko.

1. Iš naršymo meniu pasirinkite **+ Naujas projektas**.

    ![Pasirinkti naują projektą.](../../../../../../translated_images/lt/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Įveskite **Projekto pavadinimą**. Jis turi būti unikalus.

    ![Sukurti projektą.](../../../../../../translated_images/lt/08-05-create-project.4d97f0372f03375a.webp)

1. Pasirinkite **Sukurti projektą**.

#### Pridėti vartotojišką ryšį prie fine-tuned Phi-3 modelio

Norėdami integruoti savo vartotojišką Phi-3 modelį su Prompt flow, turite saugoti modelio galinį tašką ir raktą vartotojiškame ryšyje. Šis nustatymas užtikrina prieigą prie jūsų vartotojiško Phi-3 modelio Prompt flow aplinkoje.

#### Nustatyti api raktą ir galinio taško uri fine-tuned Phi-3 modeliui

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Eikite į savo sukurtą Azure Machine learning darbo sritį.

1. Pasirinkite **Galiniai taškai** iš kairėje esančio skirtuko.

    ![Pasirinkite galinius taškus.](../../../../../../translated_images/lt/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Pasirinkite sukurtą galinį tašką.

    ![Pasirinkite sukurtą galinį tašką.](../../../../../../translated_images/lt/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Iš naršymo meniu pasirinkite **Naudoti**.

1. Nukopijuokite savo **REST galinį tašką** ir **Pagrindinį raktą**.

    ![Nukopijuokite api raktą ir galinio taško uri.](../../../../../../translated_images/lt/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Pridėti vartotojišką ryšį

1. Apsilankykite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Eikite į sukurtą Microsoft Foundry projektą.

1. Projekto, kurį sukūrėte, kairiajame skirtuke pasirinkite **Nustatymai**.

1. Pasirinkite **+ Naujas ryšys**.

    ![Pasirinkite naują ryšį.](../../../../../../translated_images/lt/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Iš naršymo meniu pasirinkite **Vartotojiški raktai**.

    ![Pasirinkite vartotojiškus raktus.](../../../../../../translated_images/lt/08-10-select-custom-keys.856f6b2966460551.webp)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **+ Pridėti raktų ir vertės poras**.
    - Rakto pavadinimui įveskite **endpoint** ir įklijuokite galinį tašką, nukopijuotą iš Azure ML Studio, į vertės laukelį.
    - Dar kartą pasirinkite **+ Pridėti raktų ir vertės poras**.
    - Rakto pavadinimui įveskite **key** ir įklijuokite raktą, nukopijuotą iš Azure ML Studio, į vertės laukelį.
    - Pridėję raktus, pažymėkite **yra slapta** („is secret“), kad raktas nebūtų atskleistas.

    ![Pridėti ryšį.](../../../../../../translated_images/lt/08-11-add-connection.785486badb4d2d26.webp)

1. Pasirinkite **Pridėti ryšį**.

#### Kurti Prompt flow

Pridėjote vartotojišką ryšį Microsoft Foundry. Dabar sukursime Prompt flow naudodami šiuos veiksmus. Vėliau sujungsite šį Prompt flow su vartotojišku ryšiu, kad galėtumėte naudoti fine-tuned modelį Prompt flow aplinkoje.

1. Eikite į sukurtą Microsoft Foundry projektą.

1. Pasirinkite **Prompt flow** iš kairiojo skirtuko.

1. Iš naršymo meniu pasirinkite **+ Kurti**.

    ![Pasirinkite Promptflow.](../../../../../../translated_images/lt/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Iš naršymo meniu pasirinkite **Pokalbio srautas**.

    ![Pasirinkite pokalbio srautą.](../../../../../../translated_images/lt/08-13-select-flow-type.2ec689b22da32591.webp)

1. Įveskite naudojamo **aplanko pavadinimą**.

    ![Įveskite pavadinimą.](../../../../../../translated_images/lt/08-14-enter-name.ff9520fefd89f40d.webp)

2. Pasirinkite **Sukurti**.

#### Nustatyti Prompt flow pokalbiui su savo vartotojišku Phi-3 modeliu

Reikia integruoti fine-tuned Phi-3 modelį į Prompt flow. Tačiau esamas pateiktas Prompt flow nėra sukurtas šiam tikslui. Todėl turite pertvarkyti Prompt flow, kad būtų galima integruoti vartotojišką modelį.

1. Prompt flow aplinkoje atlikite šiuos veiksmus, kad perdarytumėte esamą srautą:

    - Pasirinkite **Žalio failo režimą**.
    - Ištrinkite visą esamą kodą faile *flow.dag.yml*.
    - Įdėkite šį kodą į *flow.dag.yml* failą.

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

    ![Pasirinkite žalią failo režimą.](../../../../../../translated_images/lt/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Į *integrate_with_promptflow.py* failą įdėkite šį kodą, kad naudotumėte vartotojišką Phi-3 modelį Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Žurnalo nustatymas
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

        # "connection" yra pasirinktinio ryšio pavadinimas, "endpoint", "key" yra raktai pasirinktinio ryšio nustatymuose
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
            
            # Užfiksuokite pilną JSON atsaką
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

    ![Įklijuokite prompt flow kodą.](../../../../../../translated_images/lt/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Daugiau detalių apie Prompt flow naudojimą Microsoft Foundry rasite čia: [Prompt flow Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pasirinkite **Pokalbio įvestis** ir **Pokalbio išvestis**, kad būtų įgalintas pokalbis su jūsų modeliu.

    ![Įvesties ir išvesties pasirinkimas.](../../../../../../translated_images/lt/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Dabar esate pasiruošę bendrauti su savo vartotojišku Phi-3 modeliu. Kitoje užduotyje išmoksite, kaip paleisti Prompt flow ir naudoti jį pokalbiui su fine-tuned Phi-3 modeliu.

> [!NOTE]
>
> Perdarytas srautas turėtų atrodyti kaip žemiau pateiktoje nuotraukoje:
>
> ![Srauto pavyzdys.](../../../../../../translated_images/lt/08-18-graph-example.d6457533952e690c.webp)
>

### Bendraukite su savo vartotojišku Phi-3 modeliu

Dabar, kai fine-tun'inote ir integravote savo vartotojišką Phi-3 modelį su Prompt flow, galite pradėti su juo bendrauti. Ši užduotis padės jums nustatyti ir pradėti pokalbį su jūsų modeliu naudojant Prompt flow. Sekdami šiuos žingsnius galėsite pilnai išnaudoti savo fine-tuned Phi-3 modelio galimybes įvairioms užduotims ir pokalbiams.

- Bendraukite su savo vartotojišku Phi-3 modeliu naudodami Prompt flow.

#### Paleisti Prompt flow

1. Pasirinkite **Pradėti skaičiavimo sesijas** paleisti Prompt flow.

    ![Pradėti skaičiavimo sesiją.](../../../../../../translated_images/lt/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Pasirinkite **Patvirtinti ir apdoroti įvestį** atnaujinti parametrus.

    ![Patvirtinti įvestį.](../../../../../../translated_images/lt/09-02-validate-input.317c76ef766361e9.webp)

1. Pasirinkite jūsų sukurtam vartotojiškam ryšiui priskirtos **connection** reikšmę. Pvz., *connection*.

    ![Ryšys.](../../../../../../translated_images/lt/09-03-select-connection.99bdddb4b1844023.webp)

#### Bendrauti su savo vartotojišku modeliu

1. Pasirinkite **Pokalbis**.

    ![Pasirinkite pokalbį.](../../../../../../translated_images/lt/09-04-select-chat.61936dce6612a1e6.webp)

1. Štai pavyzdys: dabar galite bendrauti su savo vartotojišku Phi-3 modeliu. Rekomenduojama užduoti klausimus pagal duomenis, naudotus fine-tun'inimui.

    ![Bendrauti su prompt flow.](../../../../../../translated_images/lt/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Esant kritinei informacijai, rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingus interpretavimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->