<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:56:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ro"
}
-->
# Ajustați și integrați modelele personalizate Phi-3 cu Prompt flow în Azure AI Foundry

Acest exemplu end-to-end (E2E) se bazează pe ghidul "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" din Microsoft Tech Community. Acesta prezintă procesele de ajustare fină, implementare și integrare a modelelor personalizate Phi-3 cu Prompt flow în Azure AI Foundry.  
Spre deosebire de exemplul E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", care presupunea rularea codului local, acest tutorial se concentrează exclusiv pe ajustarea fină și integrarea modelului în Azure AI / ML Studio.

## Prezentare generală

În acest exemplu E2E, vei învăța cum să ajustezi fin modelul Phi-3 și să îl integrezi cu Prompt flow în Azure AI Foundry. Folosind Azure AI / ML Studio, vei crea un flux de lucru pentru implementarea și utilizarea modelelor AI personalizate. Acest exemplu E2E este împărțit în trei scenarii:

**Scenariul 1: Configurarea resurselor Azure și pregătirea pentru ajustarea fină**

**Scenariul 2: Ajustarea fină a modelului Phi-3 și implementarea în Azure Machine Learning Studio**

**Scenariul 3: Integrarea cu Prompt flow și conversația cu modelul personalizat în Azure AI Foundry**

Iată o prezentare generală a acestui exemplu E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.ro.png)

### Cuprins

1. **[Scenariul 1: Configurarea resurselor Azure și pregătirea pentru ajustarea fină](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Crearea unui Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Solicitarea cotelor GPU în abonamentul Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adăugarea unei atribuiri de rol](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurarea proiectului](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pregătirea setului de date pentru ajustarea fină](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariul 2: Ajustarea fină a modelului Phi-3 și implementarea în Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ajustarea fină a modelului Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementarea modelului Phi-3 ajustat fin](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariul 3: Integrarea cu Prompt flow și conversația cu modelul personalizat în Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrarea modelului personalizat Phi-3 cu Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Conversația cu modelul personalizat Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenariul 1: Configurarea resurselor Azure și pregătirea pentru ajustarea fină

### Crearea unui Azure Machine Learning Workspace

1. Tastează *azure machine learning* în **bara de căutare** din partea de sus a paginii portalului și selectează **Azure Machine Learning** din opțiunile afișate.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.ro.png)

2. Selectează **+ Create** din meniul de navigare.

3. Selectează **New workspace** din meniul de navigare.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.ro.png)

4. Efectuează următoarele acțiuni:

    - Selectează **Subscription** Azure.
    - Selectează **Resource group** pe care vrei să îl folosești (creează unul nou dacă este necesar).
    - Introdu **Workspace Name**. Trebuie să fie o valoare unică.
    - Selectează **Region** pe care dorești să o folosești.
    - Selectează **Storage account** pe care vrei să îl folosești (creează unul nou dacă este necesar).
    - Selectează **Key vault** pe care vrei să îl folosești (creează unul nou dacă este necesar).
    - Selectează **Application insights** pe care vrei să îl folosești (creează unul nou dacă este necesar).
    - Selectează **Container registry** pe care vrei să îl folosești (creează unul nou dacă este necesar).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.ro.png)

5. Selectează **Review + Create**.

6. Selectează **Create**.

### Solicitarea cotelor GPU în abonamentul Azure

În acest tutorial, vei învăța cum să ajustezi fin și să implementezi un model Phi-3 folosind GPU-uri. Pentru ajustarea fină, vei folosi GPU-ul *Standard_NC24ads_A100_v4*, care necesită o solicitare de cotă. Pentru implementare, vei folosi GPU-ul *Standard_NC6s_v3*, care de asemenea necesită o solicitare de cotă.

> [!NOTE]
>
> Doar abonamentele Pay-As-You-Go (tipul standard de abonament) sunt eligibile pentru alocarea GPU-urilor; abonamentele de tip beneficii nu sunt suportate în prezent.
>

1. Accesează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Efectuează următoarele pentru a solicita cota pentru *Standard NCADSA100v4 Family*:

    - Selectează **Quota** din tab-ul din stânga.
    - Selectează **Virtual machine family** pe care vrei să o folosești. De exemplu, selectează **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, care include GPU-ul *Standard_NC24ads_A100_v4*.
    - Selectează **Request quota** din meniul de navigare.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.ro.png)

    - În pagina Request quota, introdu **New cores limit** pe care dorești să îl folosești. De exemplu, 24.
    - În pagina Request quota, selectează **Submit** pentru a trimite cererea de cotă GPU.

1. Efectuează următoarele pentru a solicita cota pentru *Standard NCSv3 Family*:

    - Selectează **Quota** din tab-ul din stânga.
    - Selectează **Virtual machine family** pe care vrei să o folosești. De exemplu, selectează **Standard NCSv3 Family Cluster Dedicated vCPUs**, care include GPU-ul *Standard_NC6s_v3*.
    - Selectează **Request quota** din meniul de navigare.
    - În pagina Request quota, introdu **New cores limit** pe care dorești să îl folosești. De exemplu, 24.
    - În pagina Request quota, selectează **Submit** pentru a trimite cererea de cotă GPU.

### Adăugarea unei atribuiri de rol

Pentru a ajusta fin și implementa modelele, trebuie mai întâi să creezi o Identitate Gestionată Atribuită Utilizatorului (User Assigned Managed Identity - UAI) și să îi atribui permisiunile corespunzătoare. Această UAI va fi folosită pentru autentificare în timpul implementării.

#### Crearea unei User Assigned Managed Identity (UAI)

1. Tastează *managed identities* în **bara de căutare** din partea de sus a paginii portalului și selectează **Managed Identities** din opțiunile afișate.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.ro.png)

1. Selectează **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.ro.png)

1. Efectuează următoarele acțiuni:

    - Selectează **Subscription** Azure.
    - Selectează **Resource group** pe care vrei să îl folosești (creează unul nou dacă este necesar).
    - Selectează **Region** pe care dorești să o folosești.
    - Introdu **Name**. Trebuie să fie o valoare unică.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.ro.png)

1. Selectează **Review + create**.

1. Selectează **+ Create**.

#### Adăugarea rolului Contributor la Managed Identity

1. Navighează la resursa Managed Identity pe care ai creat-o.

1. Selectează **Azure role assignments** din tab-ul din stânga.

1. Selectează **+Add role assignment** din meniul de navigare.

1. În pagina Add role assignment, efectuează următoarele:

    - Selectează **Scope** la **Resource group**.
    - Selectează **Subscription** Azure.
    - Selectează **Resource group** pe care vrei să îl folosești.
    - Selectează **Role** la **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.ro.png)

2. Selectează **Save**.

#### Adăugarea rolului Storage Blob Data Reader la Managed Identity

1. Tastează *storage accounts* în **bara de căutare** din partea de sus a paginii portalului și selectează **Storage accounts** din opțiunile afișate.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.ro.png)

1. Selectează contul de stocare asociat cu Azure Machine Learning workspace pe care l-ai creat. De exemplu, *finetunephistorage*.

1. Efectuează următoarele pentru a naviga la pagina Add role assignment:

    - Navighează la contul de stocare Azure pe care l-ai creat.
    - Selectează **Access Control (IAM)** din tab-ul din stânga.
    - Selectează **+ Add** din meniul de navigare.
    - Selectează **Add role assignment** din meniul de navigare.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.ro.png)

1. În pagina Add role assignment, efectuează următoarele:

    - În pagina Role, tastează *Storage Blob Data Reader* în **bara de căutare** și selectează **Storage Blob Data Reader** din opțiunile afișate.
    - În pagina Role, selectează **Next**.
    - În pagina Members, selectează **Assign access to** **Managed identity**.
    - În pagina Members, selectează **+ Select members**.
    - În pagina Select managed identities, selectează **Subscription** Azure.
    - În pagina Select managed identities, selectează **Managed identity** la **Manage Identity**.
    - În pagina Select managed identities, selectează Managed Identity pe care ai creat-o. De exemplu, *finetunephi-managedidentity*.
    - În pagina Select managed identities, selectează **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.ro.png)

1. Selectează **Review + assign**.

#### Adăugarea rolului AcrPull la Managed Identity

1. Tastează *container registries* în **bara de căutare** din partea de sus a paginii portalului și selectează **Container registries** din opțiunile afișate.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.ro.png)

1. Selectează container registry asociat cu Azure Machine Learning workspace. De exemplu, *finetunephicontainerregistry*

1. Efectuează următoarele pentru a naviga la pagina Add role assignment:

    - Selectează **Access Control (IAM)** din tab-ul din stânga.
    - Selectează **+ Add** din meniul de navigare.
    - Selectează **Add role assignment** din meniul de navigare.

1. În pagina Add role assignment, efectuează următoarele:

    - În pagina Role, tastează *AcrPull* în **bara de căutare** și selectează **AcrPull** din opțiunile afișate.
    - În pagina Role, selectează **Next**.
    - În pagina Members, selectează **Assign access to** **Managed identity**.
    - În pagina Members, selectează **+ Select members**.
    - În pagina Select managed identities, selectează **Subscription** Azure.
    - În pagina Select managed identities, selectează **Managed identity** la **Manage Identity**.
    - În pagina Select managed identities, selectează Managed Identity pe care ai creat-o. De exemplu, *finetunephi-managedidentity*.
    - În pagina Select managed identities, selectează **Select**.
    - Selectează **Review + assign**.

### Configurarea proiectului

Pentru a descărca seturile de date necesare pentru ajustarea fină, vei configura un mediu local.

În acest exercițiu, vei:

- Crea un folder în care să lucrezi.
- Crea un mediu virtual.
- Instala pachetele necesare.
- Crea un fișier *download_dataset.py* pentru a descărca setul de date.

#### Crearea unui folder în care să lucrezi

1. Deschide o fereastră de terminal și tastează următoarea comandă pentru a crea un folder numit *finetune-phi* în calea implicită.

    ```console
    mkdir finetune-phi
    ```

2. Tastează următoarea comandă în terminal pentru a naviga în folderul *finetune-phi* pe care l-ai creat.
#### Creează un mediu virtual

1. Tastează următoarea comandă în terminal pentru a crea un mediu virtual numit *.venv*.

    ```console
    python -m venv .venv
    ```

2. Tastează următoarea comandă în terminal pentru a activa mediul virtual.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Dacă a funcționat, ar trebui să vezi *(.venv)* înaintea promptului de comandă.

#### Instalează pachetele necesare

1. Tastează următoarele comenzi în terminal pentru a instala pachetele necesare.

    ```console
    pip install datasets==2.19.1
    ```

#### Creează `download_dataset.py`

> [!NOTE]
> Structura completă a folderului:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Deschide **Visual Studio Code**.

1. Selectează **File** din bara de meniu.

1. Selectează **Open Folder**.

1. Selectează folderul *finetune-phi* pe care l-ai creat, situat la *C:\Users\yourUserName\finetune-phi*.

    ![Selectează folderul pe care l-ai creat.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.ro.png)

1. În panoul din stânga al Visual Studio Code, dă click dreapta și selectează **New File** pentru a crea un fișier nou numit *download_dataset.py*.

    ![Creează un fișier nou.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.ro.png)

### Pregătește setul de date pentru fine-tuning

În acest exercițiu, vei rula fișierul *download_dataset.py* pentru a descărca seturile de date *ultrachat_200k* în mediul tău local. Apoi vei folosi aceste seturi de date pentru a face fine-tuning modelului Phi-3 în Azure Machine Learning.

În acest exercițiu vei:

- Adăuga cod în fișierul *download_dataset.py* pentru a descărca seturile de date.
- Rula fișierul *download_dataset.py* pentru a descărca seturile de date în mediul local.

#### Descarcă setul tău de date folosind *download_dataset.py*

1. Deschide fișierul *download_dataset.py* în Visual Studio Code.

1. Adaugă următorul cod în fișierul *download_dataset.py*.

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

1. Tastează următoarea comandă în terminal pentru a rula scriptul și a descărca setul de date în mediul local.

    ```console
    python download_dataset.py
    ```

1. Verifică dacă seturile de date au fost salvate cu succes în directorul local *finetune-phi/data*.

> [!NOTE]
>
> #### Notă despre dimensiunea setului de date și timpul de fine-tuning
>
> În acest tutorial, folosești doar 1% din setul de date (`split='train[:1%]'`). Aceasta reduce semnificativ cantitatea de date, accelerând atât încărcarea, cât și procesul de fine-tuning. Poți ajusta procentajul pentru a găsi echilibrul potrivit între timpul de antrenare și performanța modelului. Folosirea unui subset mai mic din setul de date reduce timpul necesar pentru fine-tuning, făcând procesul mai ușor de gestionat într-un tutorial.

## Scenariul 2: Fine-tune modelul Phi-3 și deploy în Azure Machine Learning Studio

### Fine-tune modelul Phi-3

În acest exercițiu, vei face fine-tuning modelului Phi-3 în Azure Machine Learning Studio.

În acest exercițiu vei:

- Crea un cluster de calcul pentru fine-tuning.
- Face fine-tuning modelului Phi-3 în Azure Machine Learning Studio.

#### Creează un cluster de calcul pentru fine-tuning

1. Accesează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectează **Compute** din tab-ul din stânga.

1. Selectează **Compute clusters** din meniul de navigare.

1. Selectează **+ New**.

    ![Selectează compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.ro.png)

1. Efectuează următoarele setări:

    - Selectează **Region** pe care dorești să o folosești.
    - Selectează **Virtual machine tier** la **Dedicated**.
    - Selectează **Virtual machine type** la **GPU**.
    - Selectează filtrul **Virtual machine size** la **Select from all options**.
    - Selectează **Virtual machine size** la **Standard_NC24ads_A100_v4**.

    ![Creează cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.ro.png)

1. Selectează **Next**.

1. Efectuează următoarele setări:

    - Introdu un **Compute name**. Trebuie să fie un nume unic.
    - Selectează **Minimum number of nodes** la **0**.
    - Selectează **Maximum number of nodes** la **1**.
    - Selectează **Idle seconds before scale down** la **120**.

    ![Creează cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.ro.png)

1. Selectează **Create**.

#### Fine-tune modelul Phi-3

1. Accesează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectează workspace-ul Azure Machine Learning pe care l-ai creat.

    ![Selectează workspace-ul pe care l-ai creat.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.ro.png)

1. Efectuează următoarele acțiuni:

    - Selectează **Model catalog** din tab-ul din stânga.
    - Tastează *phi-3-mini-4k* în **bara de căutare** și selectează **Phi-3-mini-4k-instruct** din opțiunile afișate.

    ![Tastează phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.ro.png)

1. Selectează **Fine-tune** din meniul de navigare.

    ![Selectează fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.ro.png)

1. Efectuează următoarele setări:

    - Selectează **Select task type** la **Chat completion**.
    - Selectează **+ Select data** pentru a încărca **Training data**.
    - Selectează tipul de încărcare pentru datele de validare la **Provide different validation data**.
    - Selectează **+ Select data** pentru a încărca **Validation data**.

    ![Completează pagina de fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.ro.png)

    > [!TIP]
    >
    > Poți selecta **Advanced settings** pentru a personaliza configurații precum **learning_rate** și **lr_scheduler_type** pentru a optimiza procesul de fine-tuning conform nevoilor tale specifice.

1. Selectează **Finish**.

1. În acest exercițiu, ai realizat cu succes fine-tuning modelului Phi-3 folosind Azure Machine Learning. Reține că procesul de fine-tuning poate dura destul de mult timp. După ce ai lansat jobul de fine-tuning, trebuie să aștepți finalizarea acestuia. Poți monitoriza starea jobului accesând tab-ul Jobs din partea stângă a workspace-ului Azure Machine Learning. În următoarea serie, vei face deploy modelului fine-tuned și îl vei integra cu Prompt flow.

    ![Vezi jobul de fine-tuning.](../../../../../../translated_images/06-08-output.2bd32e59930672b1.ro.png)

### Deploy modelul Phi-3 fine-tuned

Pentru a integra modelul Phi-3 fine-tuned cu Prompt flow, trebuie să faci deploy modelului pentru a-l face accesibil pentru inferență în timp real. Acest proces implică înregistrarea modelului, crearea unui endpoint online și deploy-ul modelului.

În acest exercițiu vei:

- Înregistra modelul fine-tuned în workspace-ul Azure Machine Learning.
- Crea un endpoint online.
- Face deploy modelului Phi-3 fine-tuned înregistrat.

#### Înregistrează modelul fine-tuned

1. Accesează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectează workspace-ul Azure Machine Learning pe care l-ai creat.

    ![Selectează workspace-ul pe care l-ai creat.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.ro.png)

1. Selectează **Models** din tab-ul din stânga.
1. Selectează **+ Register**.
1. Selectează **From a job output**.

    ![Înregistrează modelul.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.ro.png)

1. Selectează jobul pe care l-ai creat.

    ![Selectează jobul.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.ro.png)

1. Selectează **Next**.

1. Selectează **Model type** la **MLflow**.

1. Asigură-te că este selectat **Job output**; ar trebui să fie selectat automat.

    ![Selectează output-ul.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.ro.png)

2. Selectează **Next**.

3. Selectează **Register**.

    ![Selectează register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.ro.png)

4. Poți vedea modelul înregistrat accesând meniul **Models** din tab-ul din stânga.

    ![Model înregistrat.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.ro.png)

#### Deploy modelul fine-tuned

1. Navighează la workspace-ul Azure Machine Learning pe care l-ai creat.

1. Selectează **Endpoints** din tab-ul din stânga.

1. Selectează **Real-time endpoints** din meniul de navigare.

    ![Creează endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.ro.png)

1. Selectează **Create**.

1. Selectează modelul înregistrat pe care l-ai creat.

    ![Selectează modelul înregistrat.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.ro.png)

1. Selectează **Select**.

1. Efectuează următoarele setări:

    - Selectează **Virtual machine** la *Standard_NC6s_v3*.
    - Selectează **Instance count** dorit. De exemplu, *1*.
    - Selectează **Endpoint** la **New** pentru a crea un endpoint.
    - Introdu un **Endpoint name**. Trebuie să fie un nume unic.
    - Introdu un **Deployment name**. Trebuie să fie un nume unic.

    ![Completează setările pentru deploy.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.ro.png)

1. Selectează **Deploy**.

> [!WARNING]
> Pentru a evita costuri suplimentare, asigură-te că ștergi endpoint-ul creat în workspace-ul Azure Machine Learning după ce nu mai ai nevoie de el.
>

#### Verifică starea deploy-ului în Azure Machine Learning Workspace

1. Navighează la workspace-ul Azure Machine Learning pe care l-ai creat.

1. Selectează **Endpoints** din tab-ul din stânga.

1. Selectează endpoint-ul pe care l-ai creat.

    ![Selectează endpoint-urile](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.ro.png)

1. Pe această pagină poți gestiona endpoint-urile în timpul procesului de deploy.

> [!NOTE]
> După ce deploy-ul este complet, asigură-te că **Live traffic** este setat la **100%**. Dacă nu este, selectează **Update traffic** pentru a ajusta setările de trafic. Reține că nu poți testa modelul dacă traficul este setat la 0%.
>
> ![Setează traficul.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.ro.png)
>

## Scenariul 3: Integrează cu Prompt flow și discută cu modelul tău personalizat în Azure AI Foundry

### Integrează modelul Phi-3 personalizat cu Prompt flow

După ce ai făcut deploy cu succes modelului tău fine-tuned, acum îl poți integra cu Prompt Flow pentru a-l folosi în aplicații în timp real, permițând o varietate de sarcini interactive cu modelul tău Phi-3 personalizat.

În acest exercițiu vei:

- Crea Azure AI Foundry Hub.
- Crea un proiect Azure AI Foundry.
- Crea Prompt flow.
- Adăuga o conexiune personalizată pentru modelul Phi-3 fine-tuned.
- Configura Prompt flow pentru a discuta cu modelul tău Phi-3 personalizat.
> [!NOTE]
> Poți integra Promptflow și folosind Azure ML Studio. Același proces de integrare se aplică și pentru Azure ML Studio.
#### Crearea Azure AI Foundry Hub

Trebuie să creezi un Hub înainte de a crea Proiectul. Un Hub funcționează ca un Grup de Resurse, permițându-ți să organizezi și să gestionezi mai multe Proiecte în cadrul Azure AI Foundry.

1. Accesează [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selectează **All hubs** din meniul lateral stâng.

1. Selectează **+ New hub** din meniul de navigare.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.ro.png)

1. Realizează următoarele acțiuni:

    - Introdu **Hub name**. Trebuie să fie o valoare unică.
    - Selectează **Subscription** Azure.
    - Selectează **Resource group** pe care vrei să îl folosești (creează unul nou dacă este necesar).
    - Selectează **Location** pe care dorești să o folosești.
    - Selectează **Connect Azure AI Services** pe care vrei să le folosești (creează unul nou dacă este necesar).
    - Selectează **Connect Azure AI Search** și alege **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.ro.png)

1. Selectează **Next**.

#### Crearea unui Proiect Azure AI Foundry

1. În Hub-ul creat, selectează **All projects** din meniul lateral stâng.

1. Selectează **+ New project** din meniul de navigare.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.ro.png)

1. Introdu **Project name**. Trebuie să fie o valoare unică.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.ro.png)

1. Selectează **Create a project**.

#### Adăugarea unei conexiuni personalizate pentru modelul Phi-3 ajustat fin

Pentru a integra modelul tău personalizat Phi-3 cu Prompt flow, trebuie să salvezi endpoint-ul și cheia modelului într-o conexiune personalizată. Această configurare asigură accesul la modelul tău Phi-3 personalizat în Prompt flow.

#### Setarea cheii API și a URI-ului endpoint-ului modelului Phi-3 ajustat fin

1. Accesează [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navighează la workspace-ul Azure Machine Learning pe care l-ai creat.

1. Selectează **Endpoints** din meniul lateral stâng.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.ro.png)

1. Selectează endpoint-ul pe care l-ai creat.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.ro.png)

1. Selectează **Consume** din meniul de navigare.

1. Copiază **REST endpoint** și **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.ro.png)

#### Adăugarea conexiunii personalizate

1. Accesează [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navighează la proiectul Azure AI Foundry pe care l-ai creat.

1. În proiectul creat, selectează **Settings** din meniul lateral stâng.

1. Selectează **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.ro.png)

1. Selectează **Custom keys** din meniul de navigare.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.ro.png)

1. Realizează următoarele acțiuni:

    - Selectează **+ Add key value pairs**.
    - Pentru numele cheii, introdu **endpoint** și lipește endpoint-ul copiat din Azure ML Studio în câmpul de valoare.
    - Selectează din nou **+ Add key value pairs**.
    - Pentru numele cheii, introdu **key** și lipește cheia copiată din Azure ML Studio în câmpul de valoare.
    - După adăugarea cheilor, bifează **is secret** pentru a preveni expunerea cheii.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.ro.png)

1. Selectează **Add connection**.

#### Crearea Prompt flow

Ai adăugat o conexiune personalizată în Azure AI Foundry. Acum, să creăm un Prompt flow urmând pașii de mai jos. Apoi, vei conecta acest Prompt flow la conexiunea personalizată pentru a putea folosi modelul ajustat fin în cadrul Prompt flow.

1. Navighează la proiectul Azure AI Foundry pe care l-ai creat.

1. Selectează **Prompt flow** din meniul lateral stâng.

1. Selectează **+ Create** din meniul de navigare.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.ro.png)

1. Selectează **Chat flow** din meniul de navigare.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.ro.png)

1. Introdu **Folder name** pe care vrei să îl folosești.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.ro.png)

2. Selectează **Create**.

#### Configurarea Prompt flow pentru a conversa cu modelul tău personalizat Phi-3

Trebuie să integrezi modelul Phi-3 ajustat fin într-un Prompt flow. Totuși, Prompt flow-ul existent nu este conceput pentru acest scop. Prin urmare, trebuie să reproiectezi Prompt flow-ul pentru a permite integrarea modelului personalizat.

1. În Prompt flow, realizează următoarele pentru a reconstrui fluxul existent:

    - Selectează **Raw file mode**.
    - Șterge tot codul existent din fișierul *flow.dag.yml*.
    - Adaugă următorul cod în fișierul *flow.dag.yml*.

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

    - Selectează **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.ro.png)

1. Adaugă următorul cod în fișierul *integrate_with_promptflow.py* pentru a folosi modelul personalizat Phi-3 în Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.ro.png)

> [!NOTE]
> Pentru informații mai detaliate despre utilizarea Prompt flow în Azure AI Foundry, poți consulta [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selectează **Chat input**, **Chat output** pentru a activa conversația cu modelul tău.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.ro.png)

1. Acum ești gata să conversezi cu modelul tău personalizat Phi-3. În exercițiul următor, vei învăța cum să pornești Prompt flow și să îl folosești pentru a conversa cu modelul tău Phi-3 ajustat fin.

> [!NOTE]
>
> Fluxul reconstruit ar trebui să arate ca în imaginea de mai jos:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.ro.png)
>

### Conversație cu modelul tău personalizat Phi-3

Acum că ai ajustat fin și integrat modelul tău personalizat Phi-3 cu Prompt flow, ești gata să începi să interacționezi cu el. Acest exercițiu te va ghida prin procesul de configurare și inițiere a unei conversații cu modelul folosind Prompt flow. Urmând acești pași, vei putea valorifica pe deplin capabilitățile modelului tău Phi-3 ajustat fin pentru diverse sarcini și conversații.

- Conversează cu modelul tău personalizat Phi-3 folosind Prompt flow.

#### Pornirea Prompt flow

1. Selectează **Start compute sessions** pentru a porni Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.ro.png)

1. Selectează **Validate and parse input** pentru a reînnoi parametrii.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.ro.png)

1. Selectează **Value** al **connection** către conexiunea personalizată pe care ai creat-o. De exemplu, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.ro.png)

#### Conversație cu modelul tău personalizat

1. Selectează **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.ro.png)

1. Iată un exemplu de rezultate: Acum poți conversa cu modelul tău personalizat Phi-3. Este recomandat să pui întrebări bazate pe datele folosite pentru ajustarea fină.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.ro.png)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.