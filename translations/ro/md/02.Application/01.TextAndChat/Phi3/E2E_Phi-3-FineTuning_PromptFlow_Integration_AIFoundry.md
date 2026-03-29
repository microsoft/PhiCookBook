# Reglarea fină și integrarea modelelor personalizate Phi-3 cu Prompt flow în Microsoft Foundry

Acest exemplu end-to-end (E2E) este bazat pe ghidul "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" din Microsoft Tech Community. Introduce procesele de reglare fină, implementare și integrare a modelelor personalizate Phi-3 cu Prompt flow în Microsoft Foundry. Spre deosebire de exemplul E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", care presupunea rularea codului local, acest tutorial se concentrează integral pe reglarea fină și integrarea modelului dvs. în cadrul Azure AI / ML Studio.

## Prezentare generală

În acest exemplu E2E, veți învăța cum să reglați fin modelul Phi-3 și să îl integrați cu Prompt flow în Microsoft Foundry. Folosind Azure AI / ML Studio, veți stabili un flux de lucru pentru implementarea și utilizarea modelelor personalizate AI. Acest exemplu E2E este împărțit în trei scenarii:

**Scenariul 1: Configurarea resurselor Azure și pregătirea pentru reglarea fină**

**Scenariul 2: Reglarea fină a modelului Phi-3 și implementarea în Azure Machine Learning Studio**

**Scenariul 3: Integrarea cu Prompt flow și chat cu modelul dvs. personalizat în Microsoft Foundry**

Iată o prezentare generală a acestui exemplu E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ro/00-01-architecture.198ba0f1ae6d841a.webp)

### Cuprins

1. **[Scenariul 1: Configurarea resurselor Azure și pregătirea pentru reglarea fină](#scenariul-1-configurarea-resurselor-azure-și-pregătirea-pentru-reglarea-fină)**
    - [Crearea unui Workspace Azure Machine Learning](#crearea-unui-workspace-azure-machine-learning)
    - [Solicitarea cotelor GPU în abonamentul Azure](#solicitarea-cotelor-gpu-în-abonamentul-azure)
    - [Adăugarea unei atribuiri de rol](#adăugarea-unei-atribuiri-de-rol)
    - [Configurarea proiectului](#configurarea-proiectului)
    - [Pregătirea setului de date pentru reglarea fină](#pregătește-setul-de-date-pentru-fine-tuning)

1. **[Scenariul 2: Reglarea fină a modelului Phi-3 și implementarea în Azure Machine Learning Studio](#scenariul-2-fine-tuning-al-modelului-phi-3-și-implementare-în-azure-machine-learning-studio)**
    - [Reglarea fină a modelului Phi-3](#fine-tunează-modelul-phi-3)
    - [Implementarea modelului Phi-3 reglat fin](#implementarea-modelului-phi-3-fine-tuned)

1. **[Scenariul 3: Integrarea cu Prompt flow și chat cu modelul dvs. personalizat în Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrarea modelului personalizat Phi-3 cu Prompt flow](#integrarea-modelului-personalizat-phi-3-cu-prompt-flow)
    - [Chat cu modelul dvs. personalizat Phi-3](#discutați-cu-modelul-phi-3-personalizat)

## Scenariul 1: Configurarea resurselor Azure și pregătirea pentru reglarea fină

### Crearea unui Workspace Azure Machine Learning

1. Tastați *azure machine learning* în **bara de căutare** din partea de sus a paginii portalului și selectați **Azure Machine Learning** din opțiunile care apar.

    ![Type azure machine learning.](../../../../../../translated_images/ro/01-01-type-azml.acae6c5455e67b4b.webp)

2. Selectați **+ Create** din meniul de navigare.

3. Selectați **New workspace** din meniul de navigare.

    ![Select new workspace.](../../../../../../translated_images/ro/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Efectuați următoarele sarcini:

    - Selectați abonamentul Azure **Subscription**.
    - Selectați **Resource group** de utilizat (creați unul nou dacă este necesar).
    - Introduceți **Workspace Name**. Trebuie să fie o valoare unică.
    - Selectați **Region** pe care doriți să o folosiți.
    - Selectați **Storage account** de utilizat (creați unul nou dacă este necesar).
    - Selectați **Key vault** de utilizat (creați unul nou dacă este necesar).
    - Selectați **Application insights** de utilizat (creați unul nou dacă este necesar).
    - Selectați **Container registry** de utilizat (creați unul nou dacă este necesar).

    ![Fill azure machine learning.](../../../../../../translated_images/ro/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Selectați **Review + Create**.

6. Selectați **Create**.

### Solicitarea cotelor GPU în abonamentul Azure

În acest tutorial, veți învăța cum să reglați fin și să implementați un model Phi-3, folosind GPU-uri. Pentru reglarea fină, veți folosi GPU-ul *Standard_NC24ads_A100_v4*, care necesită o solicitare de cotă. Pentru implementare, veți folosi GPU-ul *Standard_NC6s_v3*, care de asemenea necesită o solicitare de cotă.

> [!NOTE]
>
> Numai abonamentele Pay-As-You-Go (tipul standard de abonament) sunt eligibile pentru alocarea GPU; abonamentele benefit nu sunt suportate momentan.
>

1. Vizitați [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Efectuați următoarele pentru a solicita cota *Standard NCADSA100v4 Family*:

    - Selectați **Quota** din fila din stânga.
    - Selectați **Virtual machine family** de utilizat. De exemplu, selectați **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, care include GPU-ul *Standard_NC24ads_A100_v4*.
    - Selectați **Request quota** din meniul de navigare.

        ![Request quota.](../../../../../../translated_images/ro/02-02-request-quota.c0428239a63ffdd5.webp)

    - În pagina Request quota, introduceți **New cores limit** dorit. De exemplu, 24.
    - În pagina Request quota, selectați **Submit** pentru a solicita cota GPU.

1. Efectuați următoarele pentru a solicita cota *Standard NCSv3 Family*:

    - Selectați **Quota** din fila din stânga.
    - Selectați **Virtual machine family** de utilizat. De exemplu, selectați **Standard NCSv3 Family Cluster Dedicated vCPUs**, care include GPU-ul *Standard_NC6s_v3*.
    - Selectați **Request quota** din meniul de navigare.
    - În pagina Request quota, introduceți **New cores limit** dorit. De exemplu, 24.
    - În pagina Request quota, selectați **Submit** pentru a solicita cota GPU.

### Adăugarea unei atribuiri de rol

Pentru a regla fin și a implementa modelele, trebuie mai întâi să creați o Identitate Gestionată Asignată Utilizatorului (User Assigned Managed Identity - UAI) și să îi atribuiți permisiunile corespunzătoare. Această UAI va fi folosită pentru autentificare în timpul implementării.

#### Crearea unei Identități Gestionate Asignate Utilizatorului (UAI)

1. Tastați *managed identities* în **bara de căutare** de sus a paginii portalului și selectați **Managed Identities** din opțiunile care apar.

    ![Type managed identities.](../../../../../../translated_images/ro/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Selectați **+ Create**.

    ![Select create.](../../../../../../translated_images/ro/03-02-select-create.92bf8989a5cd98f2.webp)

1. Efectuați următoarele sarcini:

    - Selectați abonamentul Azure **Subscription**.
    - Selectați **Resource group** de utilizat (creați unul nou dacă este necesar).
    - Selectați **Region** pe care doriți să o folosiți.
    - Introduceți **Name**. Trebuie să fie o valoare unică.

    ![Select create.](../../../../../../translated_images/ro/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Selectați **Review + create**.

1. Selectați **+ Create**.

#### Adăugarea atribuției de rol Contributor pentru Identitatea Gestionată

1. Navigați la resursa de Identitate Gestionată pe care ați creat-o.

1. Selectați **Azure role assignments** din fila din stânga.

1. Selectați **+Add role assignment** din meniul de navigare.

1. În pagina Add role assignment, efectuați următoarele:
    - Selectați **Scope** la **Resource group**.
    - Selectați abonamentul Azure **Subscription**.
    - Selectați **Resource group** de utilizat.
    - Selectați **Role** la **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/ro/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Selectați **Save**.

#### Adăugarea rolului Storage Blob Data Reader pentru Identitatea Gestionată

1. Tastați *storage accounts* în **bara de căutare** din partea de sus a portalului și selectați **Storage accounts** din opțiunile care apar.

    ![Type storage accounts.](../../../../../../translated_images/ro/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Selectați contul de stocare asociat cu workspace-ul Azure Machine Learning pe care l-ați creat. De exemplu, *finetunephistorage*.

1. Efectuați următoarele pentru a naviga la pagina Add role assignment:

    - Navigați la contul Azure Storage creat.
    - Selectați **Access Control (IAM)** din fila din stânga.
    - Selectați **+ Add** din meniul de navigare.
    - Selectați **Add role assignment** din meniul de navigare.

    ![Add role.](../../../../../../translated_images/ro/03-06-add-role.353ccbfdcf0789c2.webp)

1. În pagina Add role assignment, efectuați următoarele:

    - În pagina Role, tastați *Storage Blob Data Reader* în **bara de căutare** și selectați **Storage Blob Data Reader** din opțiunile afișate.
    - În pagina Role, selectați **Next**.
    - În pagina Members, selectați **Assign access to** **Managed identity**.
    - În pagina Members, selectați **+ Select members**.
    - În pagina Select managed identities, selectați abonamentul Azure **Subscription**.
    - În pagina Select managed identities, selectați **Managed identity** la **Manage Identity**.
    - În pagina Select managed identities, alegeți Identitatea Gestionată pe care ați creat-o. De exemplu, *finetunephi-managedidentity*.
    - În pagina Select managed identities, selectați **Select**.

    ![Select managed identity.](../../../../../../translated_images/ro/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Selectați **Review + assign**.

#### Adăugarea rolului AcrPull pentru Identitatea Gestionată

1. Tastați *container registries* în **bara de căutare** din partea de sus a portalului și selectați **Container registries** din opțiunile care apar.

    ![Type container registries.](../../../../../../translated_images/ro/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Selectați container registry-ul asociat cu workspace-ul Azure Machine Learning. De exemplu, *finetunephicontainerregistry*

1. Efectuați următoarele pentru a naviga la pagina Add role assignment:

    - Selectați **Access Control (IAM)** din fila din stânga.
    - Selectați **+ Add** din meniul de navigare.
    - Selectați **Add role assignment** din meniul de navigare.

1. În pagina Add role assignment, efectuați următoarele:

    - În pagina Role, tastați *AcrPull* în **bara de căutare** și selectați **AcrPull** din opțiunile care apar.
    - În pagina Role, selectați **Next**.
    - În pagina Members, selectați **Assign access to** **Managed identity**.
    - În pagina Members, selectați **+ Select members**.
    - În pagina Select managed identities, selectați abonamentul Azure **Subscription**.
    - În pagina Select managed identities, selectați **Managed identity** la **Manage Identity**.
    - În pagina Select managed identities, alegeți Identitatea Gestionată pe care ați creat-o. De exemplu, *finetunephi-managedidentity*.
    - În pagina Select managed identities, selectați **Select**.
    - Selectați **Review + assign**.

### Configurarea proiectului

Pentru a descărca seturile de date necesare reglării fine, veți configura un mediu local.

În acest exercițiu, veți:

- Crea un dosar în care să lucrați.
- Crea un mediu virtual.
- Instala pachetele necesare.
- Crea un fișier *download_dataset.py* pentru a descărca setul de date.

#### Crearea unui folder în care să lucrați

1. Deschideți o fereastră de terminal și tastați comanda următoare pentru a crea un folder numit *finetune-phi* în calea implicită.

    ```console
    mkdir finetune-phi
    ```

2. Tastați comanda următoare în terminal pentru a naviga în folderul *finetune-phi* pe care l-ați creat.

    ```console
    cd finetune-phi
    ```

#### Crearea unui mediu virtual

1. Tastați următoarea comandă în terminal pentru a crea un mediu virtual numit *.venv*.
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

#### Creează `donload_dataset.py`

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

1. Selectează folderul *finetune-phi* pe care l-ai creat, aflat la *C:\Users\numeleTăuDeUtilizator\finetune-phi*.

    ![Selectează folderul pe care l-ai creat.](../../../../../../translated_images/ro/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. În panoul din stânga din Visual Studio Code, fă clic dreapta și selectează **New File** pentru a crea un fișier nou numit *download_dataset.py*.

    ![Creează un fișier nou.](../../../../../../translated_images/ro/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Pregătește setul de date pentru fine-tuning

În acest exercițiu, vei rula fișierul *download_dataset.py* pentru a descărca seturile de date *ultrachat_200k* în mediul tău local. Apoi vei folosi aceste seturi pentru a face fine-tuning modelului Phi-3 în Azure Machine Learning.

În acest exercițiu, vei:

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
        # Încarcă setul de date cu numele, configurația și raportul de împărțire specificate
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Împarte setul de date în seturi de antrenament și test (80% antrenament, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Creează directorul dacă nu există
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Deschide fișierul în modul scriere
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterează peste fiecare înregistrare din setul de date
            for record in dataset:
                # Salvează înregistrarea ca obiect JSON și scrie-l în fișier
                json.dump(record, f)
                # Scrie un caracter de linie nouă pentru a separa înregistrările
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Încarcă și împarte setul de date ULTRACHAT_200k cu o configurație și raport de împărțire specific
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrage seturile de date de antrenament și test din împărțire
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Salvează setul de date de antrenament într-un fișier JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Salvează setul de date de test într-un fișier JSONL separat
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Tastează următoarea comandă în terminal pentru a rula scriptul și a descărca setul de date în mediul tău local.

    ```console
    python download_dataset.py
    ```

1. Verifică dacă seturile de date au fost salvate cu succes în directorul tău local *finetune-phi/data*.

> [!NOTE]
>
> #### Notă privind dimensiunea setului de date și timpul de fine-tuning
>
> În acest tutorial, folosești doar 1% din setul de date (`split='train[:1%]'`). Aceasta reduce semnificativ cantitatea de date, accelerând atât încărcarea, cât și procesele de fine-tuning. Poți ajusta procentajul pentru a găsi echilibrul potrivit între timpul de antrenare și performanța modelului. Folosirea unui subset mai mic de date reduce timpul necesar pentru fine-tuning, făcând procesul mai accesibil într-un tutorial.

## Scenariul 2: Fine-tuning al modelului Phi-3 și implementare în Azure Machine Learning Studio

### Fine-tunează modelul Phi-3

În acest exercițiu, vei face fine-tuning modelului Phi-3 în Azure Machine Learning Studio.

În acest exercițiu, vei:

- Crea un cluster de calcul pentru fine-tuning.
- Face fine-tuning modelului Phi-3 în Azure Machine Learning Studio.

#### Creează un cluster de calcul pentru fine-tuning

1. Vizitează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectează **Compute** din tab-ul din stânga.

1. Selectează **Compute clusters** din meniul de navigare.

1. Selectează **+ New**.

    ![Selectează compute.](../../../../../../translated_images/ro/06-01-select-compute.a29cff290b480252.webp)

1. Efectuează următoarele acțiuni:

    - Selectează **Region** pe care dorești să o folosești.
    - Selectează **Virtual machine tier** la **Dedicated**.
    - Selectează **Virtual machine type** la **GPU**.
    - Selectează filtrul **Virtual machine size** la **Select from all options**.
    - Selectează **Virtual machine size** la **Standard_NC24ads_A100_v4**.

    ![Creează cluster.](../../../../../../translated_images/ro/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Selectează **Next**.

1. Efectuează următoarele acțiuni:

    - Introdu **Compute name**. Trebuie să fie o valoare unică.
    - Selectează **Minimum number of nodes** la **0**.
    - Selectează **Maximum number of nodes** la **1**.
    - Selectează **Idle seconds before scale down** la **120**.

    ![Creează cluster.](../../../../../../translated_images/ro/06-03-create-cluster.4a54ba20914f3662.webp)

1. Selectează **Create**.

#### Fine-tunează modelul Phi-3

1. Vizitează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectează spațiul de lucru Azure Machine Learning pe care l-ai creat.

    ![Selectează spațiul de lucru pe care l-ai creat.](../../../../../../translated_images/ro/06-04-select-workspace.a92934ac04f4f181.webp)

1. Efectuează următoarele acțiuni:

    - Selectează **Model catalog** din tab-ul din stânga.
    - Tastează *phi-3-mini-4k* în **bara de căutare** și selectează **Phi-3-mini-4k-instruct** din opțiunile apărute.

    ![Tastează phi-3-mini-4k.](../../../../../../translated_images/ro/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Selectează **Fine-tune** din meniul de navigare.

    ![Selectează fine tune.](../../../../../../translated_images/ro/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Efectuează următoarele acțiuni:

    - Selectează **Select task type** la **Chat completion**.
    - Selectează **+ Select data** pentru a încărca **datele de antrenament**.
    - Selectează tipul de încărcare a datelor de validare la **Provide different validation data**.
    - Selectează **+ Select data** pentru a încărca **datele de validare**.

    ![Completează pagina de fine-tuning.](../../../../../../translated_images/ro/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Poți selecta **Advanced settings** pentru a personaliza configurații precum **learning_rate** și **lr_scheduler_type** pentru a optimiza procesul de fine-tuning conform nevoilor tale specifice.

1. Selectează **Finish**.

1. În acest exercițiu, ai realizat cu succes fine-tuning modelului Phi-3 folosind Azure Machine Learning. Reține că procesul poate dura o perioadă considerabilă. După ce pornești job-ul de fine-tuning, trebuie să aștepți până la finalizare. Poți monitoriza starea job-ului din fila Jobs din partea stângă a spațiului tău de lucru Azure Machine Learning. În următoarea serie, vei implementa modelul fine-tuned și îl vei integra cu Prompt flow.

    ![Vezi job-ul de fine-tuning.](../../../../../../translated_images/ro/06-08-output.2bd32e59930672b1.webp)

### Implementarea modelului Phi-3 fine-tuned

Pentru a integra modelul Phi-3 fine-tuned cu Prompt flow, trebuie să implementezi modelul pentru a-l face accesibil pentru inferență în timp real. Acest proces implică înregistrarea modelului, crearea unui endpoint online și implementarea modelului.

În acest exercițiu, vei:

- Înregistra modelul fine-tuned în spațiul de lucru Azure Machine Learning.
- Crea un endpoint online.
- Implementa modelul Phi-3 fine-tuned înregistrat.

#### Înregistrează modelul fine-tuned

1. Vizitează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectează spațiul de lucru Azure Machine Learning pe care l-ai creat.

    ![Selectează spațiul de lucru pe care l-ai creat.](../../../../../../translated_images/ro/06-04-select-workspace.a92934ac04f4f181.webp)

1. Selectează **Models** din tab-ul din stânga.

1. Selectează **+ Register**.

1. Selectează **From a job output**.

    ![Înregistrează modelul.](../../../../../../translated_images/ro/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Selectează job-ul pe care l-ai creat.

    ![Selectează job-ul.](../../../../../../translated_images/ro/07-02-select-job.3e2e1144cd6cd093.webp)

1. Selectează **Next**.

1. Selectează tipul de model **Model type** la **MLflow**.

1. Asigură-te că este selectat **Job output**; acesta ar trebui să fie selectat automat.

    ![Selectează output-ul.](../../../../../../translated_images/ro/07-03-select-output.4cf1a0e645baea1f.webp)

2. Selectează **Next**.

3. Selectează **Register**.

    ![Selectează register.](../../../../../../translated_images/ro/07-04-register.fd82a3b293060bc7.webp)

4. Poți vizualiza modelul tău înregistrat navigând în meniul **Models** din tab-ul din stânga.

    ![Model înregistrat.](../../../../../../translated_images/ro/07-05-registered-model.7db9775f58dfd591.webp)

#### Implementează modelul fine-tuned

1. Navighează în spațiul de lucru Azure Machine Learning pe care l-ai creat.

1. Selectează **Endpoints** din tab-ul din stânga.

1. Selectează **Real-time endpoints** din meniul de navigație.

    ![Creează endpoint.](../../../../../../translated_images/ro/07-06-create-endpoint.1ba865c606551f09.webp)

1. Selectează **Create**.

1. Selectează modelul înregistrat pe care l-ai creat.

    ![Selectează modelul înregistrat.](../../../../../../translated_images/ro/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Selectează **Select**.

1. Efectuează următoarele acțiuni:

    - Selectează **Virtual machine** pe *Standard_NC6s_v3*.
    - Selectează **Instance count** după cum dorești, de exemplu, *1*.
    - Selectează **Endpoint** la **New** pentru a crea un nou endpoint.
    - Introdu **Endpoint name**. Trebuie să fie o valoare unică.
    - Introdu **Deployment name**. Trebuie să fie o valoare unică.

    ![Completează setările pentru implementare.](../../../../../../translated_images/ro/07-08-deployment-setting.43ddc4209e673784.webp)

1. Selectează **Deploy**.

> [!WARNING]
> Pentru a evita costurile suplimentare, asigură-te că ștergi endpoint-ul creat în spațiul de lucru Azure Machine Learning.
>

#### Verifică starea implementării în Azure Machine Learning Workspace

1. Navighează în spațiul de lucru Azure Machine Learning pe care l-ai creat.

1. Selectează **Endpoints** din tab-ul din stânga.

1. Selectează endpoint-ul pe care l-ai creat.

    ![Selectează endpoints](../../../../../../translated_images/ro/07-09-check-deployment.325d18cae8475ef4.webp)

1. Pe această pagină poți gestiona endpoint-urile în timpul procesului de implementare.

> [!NOTE]
> După ce implementarea este completă, asigură-te că **Live traffic** este setat la **100%**. Dacă nu, selectează **Update traffic** pentru a ajusta setările de trafic. Reține că nu poți testa modelul dacă traficul este setat la 0%.
>
> ![Configurează traficul.](../../../../../../translated_images/ro/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenariul 3: Integrare cu Prompt flow și conversație cu modelul tău personalizat în Microsoft Foundry

### Integrarea modelului personalizat Phi-3 cu Prompt flow

După ce ai implementat cu succes modelul fine-tuned, poți acum să îl integrezi cu Prompt Flow pentru a-l folosi în aplicații în timp real, permițând o varietate de sarcini interactive cu modelul tău Phi-3 personalizat.

În acest exercițiu, vei:

- Crea Microsoft Foundry Hub.
- Crea Microsoft Foundry Project.
- Crea Prompt flow.
- Adăuga o conexiune personalizată pentru modelul Phi-3 fine-tuned.
- Configura Prompt flow pentru a conversa cu modelul Phi-3 personalizat.

> [!NOTE]
> Poți integra de asemenea cu Promptflow folosind Azure ML Studio. Același proces de integrare poate fi aplicat în Azure ML Studio.

#### Creează Microsoft Foundry Hub

Trebuie să creezi un Hub înainte de a crea Proiectul. Un Hub funcționează ca un Grup de Resurse, permițând organizarea și gestionarea mai multor Proiecte în Microsoft Foundry.
1. Vizitați [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selectați **All hubs** din fila din stânga.

1. Selectați **+ New hub** din meniul de navigație.

    ![Create hub.](../../../../../../translated_images/ro/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Îndepliniți următoarele sarcini:

    - Introduceți **Hub name**. Trebuie să fie o valoare unică.
    - Selectați **Subscription** Azure.
    - Selectați **Resource group** de utilizat (creați unul nou dacă este necesar).
    - Selectați **Location** pe care doriți să o utilizați.
    - Selectați **Connect Azure AI Services** de utilizat (creați unul nou dacă este necesar).
    - Selectați **Connect Azure AI Search** pentru a **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/ro/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Selectați **Next**.

#### Creați un proiect Microsoft Foundry

1. În Hub-ul pe care l-ați creat, selectați **All projects** din fila din stânga.

1. Selectați **+ New project** din meniul de navigație.

    ![Select new project.](../../../../../../translated_images/ro/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Introduceți **Project name**. Trebuie să fie o valoare unică.

    ![Create project.](../../../../../../translated_images/ro/08-05-create-project.4d97f0372f03375a.webp)

1. Selectați **Create a project**.

#### Adăugați o conexiune personalizată pentru modelul Phi-3 finetuned

Pentru a integra modelul Phi-3 personalizat cu Prompt flow, trebuie să salvați endpoint-ul și cheia modelului într-o conexiune personalizată. Această configurare asigură accesul la modelul personalizat Phi-3 din Prompt flow.

#### Setați cheia API și URI-ul endpoint-ului modelului Phi-3 finetuned

1. Vizitați [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigați la spațiul de lucru Azure Machine Learning pe care l-ați creat.

1. Selectați **Endpoints** din fila din stânga.

    ![Select endpoints.](../../../../../../translated_images/ro/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Selectați endpoint-ul pe care l-ați creat.

    ![Select endpoints.](../../../../../../translated_images/ro/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Selectați **Consume** din meniul de navigație.

1. Copiați **REST endpoint** și **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ro/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Adăugați conexiunea personalizată

1. Vizitați [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigați la proiectul Microsoft Foundry pe care l-ați creat.

1. În proiectul pe care l-ați creat, selectați **Settings** din fila din stânga.

1. Selectați **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/ro/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Selectați **Custom keys** din meniul de navigație.

    ![Select custom keys.](../../../../../../translated_images/ro/08-10-select-custom-keys.856f6b2966460551.webp)

1. Îndepliniți următoarele sarcini:

    - Selectați **+ Add key value pairs**.
    - Pentru numele cheii introduceți **endpoint** și lipiți endpoint-ul copiat din Azure ML Studio în câmpul valoare.
    - Selectați din nou **+ Add key value pairs**.
    - Pentru numele cheii introduceți **key** și lipiți cheia copiată din Azure ML Studio în câmpul valoare.
    - După adăugarea cheilor, selectați **is secret** pentru a preveni expunerea cheii.

    ![Add connection.](../../../../../../translated_images/ro/08-11-add-connection.785486badb4d2d26.webp)

1. Selectați **Add connection**.

#### Creați Prompt flow

Ați adăugat o conexiune personalizată în Microsoft Foundry. Acum, să creăm un Prompt flow folosind următorii pași. Apoi, veți conecta acest Prompt flow la conexiunea personalizată pentru a putea utiliza modelul finetuned în Prompt flow.

1. Navigați la proiectul Microsoft Foundry pe care l-ați creat.

1. Selectați **Prompt flow** din fila din stânga.

1. Selectați **+ Create** din meniul de navigație.

    ![Select Promptflow.](../../../../../../translated_images/ro/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Selectați **Chat flow** din meniul de navigație.

    ![Select chat flow.](../../../../../../translated_images/ro/08-13-select-flow-type.2ec689b22da32591.webp)

1. Introduceți **Folder name** de utilizat.

    ![Enter name.](../../../../../../translated_images/ro/08-14-enter-name.ff9520fefd89f40d.webp)

2. Selectați **Create**.

#### Configurați Prompt flow pentru a conversa cu modelul personalizat Phi-3

Trebuie să integrați modelul Phi-3 finetuned într-un Prompt flow. Totuși, Prompt flow-ul existent nu este conceput pentru acest scop. Prin urmare, trebuie să reproiectați Prompt flow-ul pentru a permite integrarea modelului personalizat.

1. În Prompt flow, îndepliniți următoarele sarcini pentru a reconstrui fluxul existent:

    - Selectați **Raw file mode**.
    - Ștergeți tot codul existent din fișierul *flow.dag.yml*.
    - Adăugați următorul cod în fișierul *flow.dag.yml*.

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

    - Selectați **Save**.

    ![Select raw file mode.](../../../../../../translated_images/ro/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Adăugați următorul cod în fișierul *integrate_with_promptflow.py* pentru a utiliza modelul Phi-3 personalizat în Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configurare jurnalizare
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

        # "connection" este numele Conexiunii Personalizate, "endpoint", "key" sunt cheile din Conexiunea Personalizată
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
            
            # Înregistrează răspunsul JSON complet
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

    ![Paste prompt flow code.](../../../../../../translated_images/ro/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Pentru informații mai detaliate despre utilizarea Prompt flow în Microsoft Foundry, puteți consulta [Prompt flow în Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selectați **Chat input**, **Chat output** pentru a permite conversația cu modelul dvs.

    ![Input Output.](../../../../../../translated_images/ro/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Acum sunteți gata să discutați cu modelul dvs. personalizat Phi-3. În exercițiul următor, veți învăța cum să porniți Prompt flow și să îl utilizați pentru a conversa cu modelul Phi-3 finetuned.

> [!NOTE]
>
> Fluxul reconstruit ar trebui să arate ca în imaginea de mai jos:
>
> ![Flow example.](../../../../../../translated_images/ro/08-18-graph-example.d6457533952e690c.webp)
>

### Discutați cu modelul Phi-3 personalizat

Acum că ați finetuned și integrat modelul dvs. Phi-3 personalizat cu Prompt flow, sunteți gata să începeți interacțiunea cu el. Acest exercițiu vă va ghida prin procesul de configurare și inițiere a unei conversații cu modelul dvs. folosind Prompt flow. Urmând acești pași, veți putea utiliza pe deplin capabilitățile modelului Phi-3 finetuned pentru diverse sarcini și conversații.

- Discutați cu modelul dvs. Phi-3 personalizat folosind Prompt flow.

#### Porniți Prompt flow

1. Selectați **Start compute sessions** pentru a porni Prompt flow.

    ![Start compute session.](../../../../../../translated_images/ro/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Selectați **Validate and parse input** pentru a actualiza parametrii.

    ![Validate input.](../../../../../../translated_images/ro/09-02-validate-input.317c76ef766361e9.webp)

1. Selectați **Value** al **connection** la conexiunea personalizată pe care ați creat-o. De exemplu, *connection*.

    ![Connection.](../../../../../../translated_images/ro/09-03-select-connection.99bdddb4b1844023.webp)

#### Discutați cu modelul dvs. personalizat

1. Selectați **Chat**.

    ![Select chat.](../../../../../../translated_images/ro/09-04-select-chat.61936dce6612a1e6.webp)

1. Iată un exemplu al rezultatelor: Acum puteți discuta cu modelul dvs. Phi-3 personalizat. Este recomandat să puneți întrebări bazate pe datele utilizate pentru finetuning.

    ![Chat with prompt flow.](../../../../../../translated_images/ro/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->