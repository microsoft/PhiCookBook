# Dostosuj i zintegrować niestandardowe modele Phi-3 z Prompt flow w Microsoft Foundry

Ten przykład end-to-end (E2E) opiera się na przewodniku "[Dostosuj i zintegrować niestandardowe modele Phi-3 z Prompt Flow w Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Wprowadza procesy dostrajania, wdrażania i integracji niestandardowych modeli Phi-3 z Prompt flow w Microsoft Foundry.  
W przeciwieństwie do przykładu E2E, "[Dostosuj i zintegrować niestandardowe modele Phi-3 z Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", który obejmował uruchamianie kodu lokalnie, ten samouczek koncentruje się całkowicie na dostrajaniu oraz integracji modelu w Azure AI / ML Studio.

## Przegląd

W tym przykładzie E2E nauczysz się, jak dostroić model Phi-3 i zintegrować go z Prompt flow w Microsoft Foundry. Wykorzystując Azure AI / ML Studio, stworzysz przepływ pracy do wdrażania i korzystania z niestandardowych modeli AI. Ten przykład E2E jest podzielony na trzy scenariusze:

**Scenariusz 1: Skonfiguruj zasoby Azure i przygotuj się do dostrajania**

**Scenariusz 2: Dostrój model Phi-3 i wdroż go w Azure Machine Learning Studio**

**Scenariusz 3: Zintegruj z Prompt flow i rozmawiaj z niestandardowym modelem w Microsoft Foundry**

Oto przegląd tego przykładu E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/pl/00-01-architecture.198ba0f1ae6d841a.webp)

### Spis treści

1. **[Scenariusz 1: Skonfiguruj zasoby Azure i przygotuj się do dostrajania](#scenariusz-1-skonfiguruj-zasoby-azure-i-przygotuj-się-do-dostrajania)**  
    - [Utwórz obszar roboczy Azure Machine Learning](#utwórz-obszar-roboczy-azure-machine-learning)  
    - [Zgłoś limit GPU w subskrypcji Azure](#zgłoś-limit-gpu-w-subskrypcji-azure)  
    - [Dodaj przypisanie roli](#dodaj-przypisanie-roli)  
    - [Skonfiguruj projekt](#skonfiguruj-projekt)  
    - [Przygotuj zestaw danych do dostrajania](#przygotuj-zestaw-danych-do-dopasowania)  

1. **[Scenariusz 2: Dostrój model Phi-3 i wdroż go w Azure Machine Learning Studio](#scenariusz-2-dopasowanie-modelu-phi-3-i-wdrożenie-w-azure-machine-learning-studio)**  
    - [Dostrój model Phi-3](#dopasowanie-modelu-phi-3)  
    - [Wdroż dostrojony model Phi-3](#wdróż-dopasowany-model-phi-3)  

1. **[Scenariusz 3: Zintegruj z Prompt flow i rozmawiaj z niestandardowym modelem w Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**  
    - [Zintegruj niestandardowy model Phi-3 z Prompt flow](#integracja-dopasowanego-modelu-phi-3-z-prompt-flow)  
    - [Rozmawiaj z niestandardowym modelem Phi-3](#rozmowa-z-niestandardowym-modelem-phi-3)  

## Scenariusz 1: Skonfiguruj zasoby Azure i przygotuj się do dostrajania

### Utwórz obszar roboczy Azure Machine Learning

1. Wpisz *azure machine learning* w **pasku wyszukiwania** na górze strony portalu i wybierz **Azure Machine Learning** z pojawiających się opcji.

    ![Type azure machine learning.](../../../../../../translated_images/pl/01-01-type-azml.acae6c5455e67b4b.webp)

2. Wybierz **+ Utwórz** z menu nawigacyjnego.

3. Wybierz **Nowy obszar roboczy** z menu nawigacyjnego.

    ![Select new workspace.](../../../../../../translated_images/pl/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Wykonaj następujące zadania:

    - Wybierz swoją subskrypcję Azure **Subscription**.  
    - Wybierz grupę zasobów **Resource group** do użycia (utwórz nową, jeśli potrzeba).  
    - Wpisz **Nazwa obszaru roboczego**. Musi to być unikalna wartość.  
    - Wybierz **Region**, którego chcesz użyć.  
    - Wybierz konto magazynu **Storage account** do użycia (utwórz nowe, jeśli potrzeba).  
    - Wybierz obiekt Key Vault **Key vault** do użycia (utwórz nowy, jeśli potrzeba).  
    - Wybierz Usługę Application Insights **Application insights** do użycia (utwórz nową, jeśli potrzeba).  
    - Wybierz rejestr kontenerów **Container registry** do użycia (utwórz nowy, jeśli potrzeba).  

    ![Fill azure machine learning.](../../../../../../translated_images/pl/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Wybierz **Przegląd + utwórz**.

6. Wybierz **Utwórz**.

### Zgłoś limit GPU w subskrypcji Azure

W tym samouczku nauczysz się, jak dostroić i wdrożyć model Phi-3, używając GPU. Do dostrajania użyjesz GPU *Standard_NC24ads_A100_v4*, który wymaga zgłoszenia limitu. Do wdrożenia użyjesz GPU *Standard_NC6s_v3*, który również wymaga zgłoszenia limitu.

> [!NOTE]  
> Tylko subskrypcje typu Pay-As-You-Go (standardowy typ subskrypcji) kwalifikują się do przydziału GPU; subskrypcje benefitowe nie są obecnie obsługiwane.  
>

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wykonaj następujące kroki, aby zgłosić limit *Standard NCADSA100v4 Family*:

    - Wybierz **Quota** (Limity) w menu po lewej stronie.  
    - Wybierz **Virtual machine family** do użycia. Na przykład wybierz **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, który zawiera GPU *Standard_NC24ads_A100_v4*.  
    - Wybierz **Request quota** w menu nawigacyjnym.  

        ![Request quota.](../../../../../../translated_images/pl/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na stronie Request quota wpisz **Nowy limit rdzeni** (New cores limit), którego chcesz użyć. Na przykład 24.  
    - Na stronie Request quota wybierz **Submit**, aby zgłosić limit GPU.

1. Wykonaj następujące kroki, aby zgłosić limit *Standard NCSv3 Family*:

    - Wybierz **Quota** w menu po lewej stronie.  
    - Wybierz **Virtual machine family** do użycia. Na przykład wybierz **Standard NCSv3 Family Cluster Dedicated vCPUs**, który zawiera GPU *Standard_NC6s_v3*.  
    - Wybierz **Request quota** w menu nawigacyjnym.  
    - Na stronie Request quota wpisz **Nowy limit rdzeni**, którego chcesz użyć. Na przykład 24.  
    - Na stronie Request quota wybierz **Submit**, aby zgłosić limit GPU.

### Dodaj przypisanie roli

Aby dostroić i wdrożyć modele, musisz najpierw utworzyć Użytkownika Przypisanej Tożsamości Zarządzanej (User Assigned Managed Identity, UAI) i przypisać mu odpowiednie uprawnienia. Ta UAI będzie używana do uwierzytelniania podczas wdrożenia.

#### Utwórz Użytkownika Przypisanej Tożsamości Zarządzanej (UAI)

1. Wpisz *managed identities* w **pasku wyszukiwania** w górnej części strony portalu i wybierz **Managed Identities** z pojawiających się opcji.

    ![Type managed identities.](../../../../../../translated_images/pl/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Wybierz **+ Utwórz**.

    ![Select create.](../../../../../../translated_images/pl/03-02-select-create.92bf8989a5cd98f2.webp)

1. Wykonaj następujące zadania:

    - Wybierz swoją subskrypcję Azure **Subscription**.  
    - Wybierz grupę zasobów **Resource group** do użycia (utwórz nową, jeśli potrzeba).  
    - Wybierz **Region**, którego chcesz użyć.  
    - Wpisz **Nazwa**. Musi być unikalna.  

    ![Select create.](../../../../../../translated_images/pl/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Wybierz **Przegląd + utwórz**.

1. Wybierz **+ Utwórz**.

#### Dodaj przypisanie roli Współtwórcy (Contributor) do tożsamości zarządzanej

1. Przejdź do zasobu Managed Identity, który utworzyłeś.

1. Wybierz **Przypisania ról Azure** (Azure role assignments) z menu po lewej stronie.

1. Wybierz **+ Dodaj przypisanie roli** z menu nawigacyjnego.

1. Na stronie Dodaj przypisanie roli (Add role assignment) wykonaj następujące kroki:  
    - Wybierz zakres **Scope** na **Grupa zasobów** (Resource group).  
    - Wybierz swoją subskrypcję Azure **Subscription**.  
    - Wybierz grupę zasobów **Resource group** do użycia.  
    - Wybierz rolę **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/pl/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Wybierz **Zapisz**.

#### Dodaj przypisanie roli Odczytu danych Blob Storage do tożsamości zarządzanej

1. Wpisz *storage accounts* w **pasku wyszukiwania** na górze strony portalu i wybierz **Storage accounts** z pojawiających się opcji.

    ![Type storage accounts.](../../../../../../translated_images/pl/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Wybierz konto magazynu powiązane z obszarem roboczym Azure Machine Learning, który utworzyłeś. Na przykład *finetunephistorage*.

1. Wykonaj następujące kroki, aby przejść do strony Dodaj przypisanie roli:

    - Przejdź do utworzonego konta magazynu Azure.  
    - Wybierz **Kontrola dostępu (IAM)** z menu po lewej stronie.  
    - Wybierz **+ Dodaj** z menu nawigacyjnego.  
    - Wybierz **Dodaj przypisanie roli** z menu nawigacyjnego.

    ![Add role.](../../../../../../translated_images/pl/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na stronie Dodaj przypisanie roli wykonaj następujące kroki:

    - Na stronie roli wpisz *Storage Blob Data Reader* w **pasku wyszukiwania** i wybierz **Storage Blob Data Reader** z pojawiających się opcji.  
    - Na stronie roli wybierz **Dalej (Next)**.  
    - Na stronie członków (Members) wybierz **Przypisz dostęp do (Assign access to)**: **Managed identity**.  
    - Na stronie członków wybierz **+ Wybierz członków**.  
    - Na stronie wyboru zarządzanych tożsamości wybierz swoją subskrypcję Azure **Subscription**.  
    - Na stronie wyboru zarządzanych tożsamości wybierz tożsamość **Managed identity**.  
    - Na stronie wyboru zarządzanych tożsamości wybierz utworzoną tożsamość zarządzaną, np. *finetunephi-managedidentity*.  
    - Na stronie wyboru zarządzanych tożsamości wybierz **Wybierz (Select)**.

    ![Select managed identity.](../../../../../../translated_images/pl/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Wybierz **Przejrzyj + przypisz** (Review + assign).

#### Dodaj przypisanie roli AcrPull do tożsamości zarządzanej

1. Wpisz *container registries* w **pasku wyszukiwania** na górze strony portalu i wybierz **Container registries** z pojawiających się opcji.

    ![Type container registries.](../../../../../../translated_images/pl/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Wybierz rejestr kontenerów powiązany z obszarem roboczym Azure Machine Learning, np. *finetunephicontainerregistry*.

1. Wykonaj następujące kroki, aby przejść do strony Dodaj przypisanie roli:

    - Wybierz **Kontrola dostępu (IAM)** z menu po lewej stronie.  
    - Wybierz **+ Dodaj** z menu nawigacyjnego.  
    - Wybierz **Dodaj przypisanie roli** z menu nawigacyjnego.

1. Na stronie Dodaj przypisanie roli wykonaj następujące kroki:

    - Na stronie roli wpisz *AcrPull* w **pasku wyszukiwania** i wybierz **AcrPull** z pojawiających się opcji.  
    - Na stronie roli wybierz **Dalej**.  
    - Na stronie członków wybierz **Przypisz dostęp do** **Managed identity**.  
    - Na stronie członków wybierz **+ Wybierz członków**.  
    - Na stronie wyboru zarządzanych tożsamości wybierz swoją subskrypcję Azure **Subscription**.  
    - Na stronie wyboru zarządzanych tożsamości wybierz tożsamość **Managed identity**.  
    - Na stronie wyboru zarządzanych tożsamości wybierz utworzoną tożsamość zarządzaną, np. *finetunephi-managedidentity*.  
    - Na stronie wyboru zarządzanych tożsamości wybierz **Wybierz**.  
    - Wybierz **Przejrzyj + przypisz**.

### Skonfiguruj projekt

Aby pobrać zestawy danych potrzebne do dostrajania, skonfigurujesz środowisko lokalne.

W tym ćwiczeniu:

- Utworzysz folder do pracy.  
- Utworzysz środowisko wirtualne.  
- Zainstalujesz wymagane pakiety.  
- Utworzysz plik *download_dataset.py* do pobrania zestawu danych.  

#### Utwórz folder do pracy

1. Otwórz okno terminala i wpisz następujące polecenie, aby utworzyć folder o nazwie *finetune-phi* w domyślnej ścieżce.

    ```console
    mkdir finetune-phi
    ```

2. Wpisz następujące polecenie w terminalu, aby przejść do utworzonego folderu *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Utwórz środowisko wirtualne

1. Wpisz następujące polecenie w terminalu, aby utworzyć środowisko wirtualne o nazwie *.venv*.
    ```console
    python -m venv .venv
    ```

2. Wpisz następujące polecenie w terminalu, aby aktywować środowisko wirtualne.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jeśli się powiodło, powinieneś zobaczyć *(.venv)* przed znakiem zachęty do wpisywania poleceń.

#### Zainstaluj wymagane pakiety

1. Wpisz następujące polecenia w terminalu, aby zainstalować wymagane pakiety.

    ```console
    pip install datasets==2.19.1
    ```

#### Utwórz `donload_dataset.py`

> [!NOTE]
> Pełna struktura folderów:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otwórz **Visual Studio Code**.

1. Wybierz **Plik** na pasku menu.

1. Wybierz **Otwórz folder**.

1. Wybierz folder *finetune-phi*, który utworzyłeś, znajdujący się w *C:\Users\twojaNazwaUżytkownika\finetune-phi*.

    ![Wybierz folder, który utworzyłeś.](../../../../../../translated_images/pl/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **Nowy plik**, aby utworzyć nowy plik o nazwie *download_dataset.py*.

    ![Utwórz nowy plik.](../../../../../../translated_images/pl/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Przygotuj zestaw danych do dopasowania

W tym ćwiczeniu uruchomisz plik *download_dataset.py*, aby pobrać zestawy danych *ultrachat_200k* do lokalnego środowiska. Następnie użyjesz tego zestawu danych do dopasowania modelu Phi-3 w Azure Machine Learning.

W tym ćwiczeniu:

- Dodasz kod do pliku *download_dataset.py*, aby pobrać zestawy danych.
- Uruchomisz plik *download_dataset.py*, aby pobrać zestawy danych do lokalnego środowiska.

#### Pobierz swój zestaw danych za pomocą *download_dataset.py*

1. Otwórz plik *download_dataset.py* w Visual Studio Code.

1. Dodaj następujący kod do pliku *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Załaduj zestaw danych o podanej nazwie, konfiguracji i proporcji podziału
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Podziel zestaw danych na zestawy treningowe i testowe (80% trening, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Utwórz katalog, jeśli nie istnieje
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Otwórz plik w trybie zapisu
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iteruj po każdym rekordzie w zestawie danych
            for record in dataset:
                # Zapisz rekord jako obiekt JSON i zapisz go do pliku
                json.dump(record, f)
                # Zapisz znak nowej linii, aby oddzielić rekordy
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Załaduj i podziel zestaw danych ULTRACHAT_200k z określoną konfiguracją i proporcją podziału
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Wyodrębnij zestawy danych treningowe i testowe z podziału
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Zapisz zestaw treningowy do pliku JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Zapisz zestaw testowy do osobnego pliku JSONL
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Wpisz następujące polecenie w terminalu, aby uruchomić skrypt i pobrać zestaw danych do lokalnego środowiska.

    ```console
    python download_dataset.py
    ```

1. Sprawdź, czy zestawy danych zostały pomyślnie zapisane w lokalnym katalogu *finetune-phi/data*.

> [!NOTE]
>
> #### Uwagi dotyczące rozmiaru zestawu danych i czasu dopasowania
>
> W tym samouczku używasz tylko 1% zestawu danych (`split='train[:1%]'`). Znacznie zmniejsza to ilość danych, przyspieszając zarówno przesyłanie, jak i proces dopasowania. Możesz dostosować procent, aby znaleźć odpowiedni balans między czasem treningu a wydajnością modelu. Użycie mniejszego podzbioru zestawu danych skraca czas potrzebny na dopasowanie, co upraszcza proces na potrzeby samouczka.

## Scenariusz 2: Dopasowanie modelu Phi-3 i wdrożenie w Azure Machine Learning Studio

### Dopasowanie modelu Phi-3

W tym ćwiczeniu dopasujesz model Phi-3 w Azure Machine Learning Studio.

W tym ćwiczeniu:

- Utworzysz klaster obliczeniowy do dopasowywania.
- Dopasujesz model Phi-3 w Azure Machine Learning Studio.

#### Utwórz klaster obliczeniowy do dopasowania

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wybierz **Compute** po lewej stronie.

1. Wybierz **Compute clusters** z menu nawigacyjnego.

1. Wybierz **+ New**.

    ![Wybierz compute.](../../../../../../translated_images/pl/06-01-select-compute.a29cff290b480252.webp)

1. Wykonaj następujące zadania:

    - Wybierz **Region**, którego chcesz użyć.
    - Wybierz **Virtual machine tier** na **Dedicated**.
    - Wybierz **Virtual machine type** na **GPU**.
    - Ustaw filtr **Virtual machine size** na **Select from all options**.
    - Wybierz **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Utwórz klaster.](../../../../../../translated_images/pl/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Wybierz **Next**.

1. Wykonaj następujące zadania:

    - Wprowadź **Compute name**. Musi być to unikalna wartość.
    - Ustaw **Minimum number of nodes** na **0**.
    - Ustaw **Maximum number of nodes** na **1**.
    - Ustaw **Idle seconds before scale down** na **120**.

    ![Utwórz klaster.](../../../../../../translated_images/pl/06-03-create-cluster.4a54ba20914f3662.webp)

1. Wybierz **Create**.

#### Dopasuj model Phi-3

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wybierz przestrzeń roboczą Azure Machine Learning, którą utworzyłeś.

    ![Wybierz utworzoną przestrzeń.](../../../../../../translated_images/pl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Wykonaj następujące zadania:

    - Wybierz **Model catalog** po lewej stronie.
    - Wpisz *phi-3-mini-4k* w **pasku wyszukiwania** i wybierz **Phi-3-mini-4k-instruct** z pojawiających się opcji.

    ![Wpisz phi-3-mini-4k.](../../../../../../translated_images/pl/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Wybierz **Fine-tune** z menu nawigacyjnego.

    ![Wybierz fine tune.](../../../../../../translated_images/pl/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Wykonaj następujące zadania:

    - Ustaw **Select task type** na **Chat completion**.
    - Wybierz **+ Select data** aby przesłać **Traning data**.
    - Ustaw typ przesyłania danych walidacyjnych na **Provide different validation data**.
    - Wybierz **+ Select data** aby przesłać **Validation data**.

    ![Wypełnij stronę dopasowywania.](../../../../../../translated_images/pl/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Możesz wybrać **Advanced settings**, aby dostosować konfiguracje takie jak **learning_rate** i **lr_scheduler_type**, aby zoptymalizować proces dopasowywania do swoich potrzeb.

1. Wybierz **Finish**.

1. W tym ćwiczeniu pomyślnie dopasowałeś model Phi-3 za pomocą Azure Machine Learning. Pamiętaj, że proces dopasowywania może zająć znaczną ilość czasu. Po uruchomieniu zadania dopasowywania musisz poczekać na jego zakończenie. Status zadania dopasowywania możesz monitorować, przechodząc do zakładki Jobs po lewej stronie w Twojej przestrzeni roboczej Azure Machine Learning. W następnej serii wdrożysz dopasowany model i zintegrujesz go z Prompt flow.

    ![Zobacz zadanie dopasowywania.](../../../../../../translated_images/pl/06-08-output.2bd32e59930672b1.webp)

### Wdróż dopasowany model Phi-3

Aby zintegrować dopasowany model Phi-3 z Prompt flow, musisz wdrożyć model, aby był dostępny do użytku w czasie rzeczywistym. Proces ten obejmuje rejestrację modelu, stworzenie punktu końcowego online oraz wdrożenie modelu.

W tym ćwiczeniu:

- Zarejestrujesz dopasowany model w przestrzeni roboczej Azure Machine Learning.
- Utworzysz punkt końcowy online.
- Wdrożysz zarejestrowany dopasowany model Phi-3.

#### Zarejestruj dopasowany model

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wybierz przestrzeń roboczą Azure Machine Learning, którą utworzyłeś.

    ![Wybierz utworzoną przestrzeń.](../../../../../../translated_images/pl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Wybierz **Models** po lewej stronie.
1. Wybierz **+ Register**.
1. Wybierz **From a job output**.

    ![Zarejestruj model.](../../../../../../translated_images/pl/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Wybierz zadanie, które utworzyłeś.

    ![Wybierz zadanie.](../../../../../../translated_images/pl/07-02-select-job.3e2e1144cd6cd093.webp)

1. Wybierz **Next**.

1. Ustaw **Model type** na **MLflow**.

1. Upewnij się, że **Job output** jest wybrane; powinno być wybrane automatycznie.

    ![Wybierz output.](../../../../../../translated_images/pl/07-03-select-output.4cf1a0e645baea1f.webp)

2. Wybierz **Next**.

3. Wybierz **Register**.

    ![Wybierz register.](../../../../../../translated_images/pl/07-04-register.fd82a3b293060bc7.webp)

4. Możesz zobaczyć swój zarejestrowany model, przechodząc do menu **Models** po lewej stronie.

    ![Zarejestrowany model.](../../../../../../translated_images/pl/07-05-registered-model.7db9775f58dfd591.webp)

#### Wdróż dopasowany model

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.

1. Wybierz **Endpoints** po lewej stronie.

1. Wybierz **Real-time endpoints** z menu nawigacyjnego.

    ![Utwórz punkt końcowy.](../../../../../../translated_images/pl/07-06-create-endpoint.1ba865c606551f09.webp)

1. Wybierz **Create**.

1. Wybierz zarejestrowany model, który utworzyłeś.

    ![Wybierz zarejestrowany model.](../../../../../../translated_images/pl/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Wybierz **Select**.

1. Wykonaj następujące zadania:

    - Wybierz **Virtual machine** na *Standard_NC6s_v3*.
    - Wybierz liczbę instancji, której chcesz użyć. Na przykład *1*.
    - Ustaw **Endpoint** na **New**, aby utworzyć nowy punkt końcowy.
    - Wprowadź **Endpoint name**. Musi być to unikalna wartość.
    - Wprowadź **Deployment name**. Musi być to unikalna wartość.

    ![Wypełnij ustawienia wdrożenia.](../../../../../../translated_images/pl/07-08-deployment-setting.43ddc4209e673784.webp)

1. Wybierz **Deploy**.

> [!WARNING]
> Aby uniknąć dodatkowych opłat na swoim koncie, upewnij się, że usunąłeś utworzony punkt końcowy w przestrzeni roboczej Azure Machine Learning.
>

#### Sprawdź status wdrożenia w przestrzeni roboczej Azure Machine Learning

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.

1. Wybierz **Endpoints** po lewej stronie.

1. Wybierz punkt końcowy, który utworzyłeś.

    ![Wybierz endpoints](../../../../../../translated_images/pl/07-09-check-deployment.325d18cae8475ef4.webp)

1. Na tej stronie możesz zarządzać punktami końcowymi podczas procesu wdrożenia.

> [!NOTE]
> Po zakończeniu wdrożenia upewnij się, że **Live traffic** jest ustawione na **100%**. Jeśli nie, wybierz **Update traffic**, aby dostosować ustawienia ruchu. Pamiętaj, że nie możesz testować modelu, jeśli ruch jest ustawiony na 0%.
>
> ![Ustaw ruch.](../../../../../../translated_images/pl/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenariusz 3: Integracja z Prompt flow i rozmowa z własnym modelem w Microsoft Foundry

### Integracja dopasowanego modelu Phi-3 z Prompt flow

Po pomyślnym wdrożeniu dopasowanego modelu możesz teraz zintegrować go z Prompt Flow, aby używać modelu w aplikacjach w czasie rzeczywistym, umożliwiając różne interaktywne zadania z Twoim dostosowanym modelem Phi-3.

W tym ćwiczeniu:

- Utworzysz Microsoft Foundry Hub.
- Utworzysz Microsoft Foundry Project.
- Utworzysz Prompt flow.
- Dodasz niestandardowe połączenie dla dopasowanego modelu Phi-3.
- Skonfigurujesz Prompt flow do rozmowy z Twoim niestandardowym modelem Phi-3.

> [!NOTE]
> Możesz również integrować się z Promptflow używając Azure ML Studio. Ten sam proces integracji można zastosować w Azure ML Studio.

#### Utwórz Microsoft Foundry Hub

Musisz utworzyć Hub, zanim stworzysz Project. Hub działa jak grupa zasobów, pozwalając organizować i zarządzać wieloma projektami w Microsoft Foundry.
1. Odwiedź [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Wybierz **All hubs** z zakładki po lewej stronie.

1. Wybierz **+ New hub** z menu nawigacyjnego.

    ![Create hub.](../../../../../../translated_images/pl/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Wykonaj następujące czynności:

    - Wprowadź **Hub name**. Musi to być unikalna wartość.
    - Wybierz swoje subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć (jeśli to konieczne, utwórz nową).
    - Wybierz **Location**, którego chcesz użyć.
    - Wybierz **Connect Azure AI Services**, które chcesz użyć (jeśli to konieczne, utwórz nowe).
    - Wybierz **Connect Azure AI Search**, aby **pominąć łączenie**.

    ![Fill hub.](../../../../../../translated_images/pl/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Wybierz **Next**.

#### Utwórz projekt Microsoft Foundry

1. W utworzonym hubie wybierz **All projects** z zakładki po lewej stronie.

1. Wybierz **+ New project** z menu nawigacyjnego.

    ![Select new project.](../../../../../../translated_images/pl/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Wprowadź **Project name**. Musi to być unikalna wartość.

    ![Create project.](../../../../../../translated_images/pl/08-05-create-project.4d97f0372f03375a.webp)

1. Wybierz **Create a project**.

#### Dodaj niestandardowe połączenie dla wytrenowanego modelu Phi-3

Aby zintegrować swój niestandardowy model Phi-3 z Prompt flow, musisz zapisać punkt końcowy modelu oraz klucz w niestandardowym połączeniu. Ta konfiguracja zapewnia dostęp do twojego niestandardowego modelu Phi-3 w Prompt flow.

#### Ustaw klucz API i URI punktu końcowego modelu Phi-3

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.

1. Wybierz **Endpoints** z zakładki po lewej stronie.

    ![Select endpoints.](../../../../../../translated_images/pl/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Wybierz punkt końcowy, który utworzyłeś.

    ![Select endpoints.](../../../../../../translated_images/pl/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Wybierz **Consume** z menu nawigacyjnego.

1. Skopiuj swój **REST endpoint** oraz **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pl/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Dodaj niestandardowe połączenie

1. Odwiedź [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Przejdź do utworzonego projektu Microsoft Foundry.

1. W wybranym projekcie wybierz **Settings** z zakładki po lewej stronie.

1. Wybierz **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/pl/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Wybierz **Custom keys** z menu nawigacyjnego.

    ![Select custom keys.](../../../../../../translated_images/pl/08-10-select-custom-keys.856f6b2966460551.webp)

1. Wykonaj następujące czynności:

    - Wybierz **+ Add key value pairs**.
    - Dla nazwy klucza wpisz **endpoint** i wklej skopiowany punkt końcowy z Azure ML Studio w pole wartości.
    - Wybierz ponownie **+ Add key value pairs**.
    - Dla nazwy klucza wpisz **key** i wklej skopiowany klucz z Azure ML Studio w pole wartości.
    - Po dodaniu kluczy zaznacz **is secret**, aby zapobiec wyświetlaniu klucza.

    ![Add connection.](../../../../../../translated_images/pl/08-11-add-connection.785486badb4d2d26.webp)

1. Wybierz **Add connection**.

#### Utwórz Prompt flow

Dodałeś niestandardowe połączenie w Microsoft Foundry. Teraz utwórz Prompt flow, korzystając z poniższych kroków. Następnie połącz ten Prompt flow z niestandardowym połączeniem, aby móc używać wytrenowanego modelu w Prompt flow.

1. Przejdź do utworzonego projektu Microsoft Foundry.

1. Wybierz **Prompt flow** z zakładki po lewej stronie.

1. Wybierz **+ Create** z menu nawigacyjnego.

    ![Select Promptflow.](../../../../../../translated_images/pl/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Wybierz **Chat flow** z menu nawigacyjnego.

    ![Select chat flow.](../../../../../../translated_images/pl/08-13-select-flow-type.2ec689b22da32591.webp)

1. Wprowadź **Folder name**, którego chcesz użyć.

    ![Enter name.](../../../../../../translated_images/pl/08-14-enter-name.ff9520fefd89f40d.webp)

2. Wybierz **Create**.

#### Skonfiguruj Prompt flow do rozmowy z niestandardowym modelem Phi-3

Musisz zintegrować wytrenowany model Phi-3 z Prompt flow. Obecnie dostępny Prompt flow nie jest do tego przystosowany. Musisz więc przeprojektować Prompt flow, aby umożliwić integrację niestandardowego modelu.

1. W Prompt flow wykonaj następujące kroki, aby odbudować istniejący flow:

    - Wybierz **Raw file mode**.
    - Usuń cały istniejący kod z pliku *flow.dag.yml*.
    - Dodaj poniższy kod do pliku *flow.dag.yml*.

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

    - Wybierz **Save**.

    ![Select raw file mode.](../../../../../../translated_images/pl/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Dodaj poniższy kod do pliku *integrate_with_promptflow.py*, aby użyć niestandardowego modelu Phi-3 w Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Konfiguracja logowania
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

        # "connection" to nazwa Połączenia Niestandardowego, "endpoint", "key" to klucze w Połączeniu Niestandardowym
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
            
            # Zaloguj pełną odpowiedź JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/pl/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Aby uzyskać bardziej szczegółowe informacje na temat korzystania z Prompt flow w Microsoft Foundry, możesz zajrzeć do [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Włącz **Chat input**, **Chat output**, aby umożliwić rozmowę z modelem.

    ![Input Output.](../../../../../../translated_images/pl/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Teraz możesz rozpocząć rozmowę z niestandardowym modelem Phi-3. W następnym ćwiczeniu nauczysz się, jak uruchomić Prompt flow i używać go do rozmowy z wytrenowanym modelem Phi-3.

> [!NOTE]
>
> Odbudowany flow powinien wyglądać jak na poniższym obrazku:
>
> ![Flow example.](../../../../../../translated_images/pl/08-18-graph-example.d6457533952e690c.webp)
>

### Rozmowa z niestandardowym modelem Phi-3

Teraz, gdy wytrenowałeś i zintegrwałeś swój niestandardowy model Phi-3 z Prompt flow, możesz zacząć z nim wchodzić w interakcje. To ćwiczenie przeprowadzi Cię przez proces konfiguracji i uruchomienia rozmowy z modelem za pomocą Prompt flow. Postępując zgodnie z tymi krokami, będziesz mógł w pełni wykorzystać możliwości swojego wytrenowanego modelu Phi-3 do różnych zadań i rozmów.

- Rozmawiaj z niestandardowym modelem Phi-3 za pomocą Prompt flow.

#### Uruchom Prompt flow

1. Wybierz **Start compute sessions**, aby rozpocząć Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pl/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Wybierz **Validate and parse input**, aby odświeżyć parametry.

    ![Validate input.](../../../../../../translated_images/pl/09-02-validate-input.317c76ef766361e9.webp)

1. Wybierz **Value** dla **connection**, aby wybrać utworzone niestandardowe połączenie, np. *connection*.

    ![Connection.](../../../../../../translated_images/pl/09-03-select-connection.99bdddb4b1844023.webp)

#### Rozmawiaj z niestandardowym modelem

1. Wybierz **Chat**.

    ![Select chat.](../../../../../../translated_images/pl/09-04-select-chat.61936dce6612a1e6.webp)

1. Oto przykład wyników: teraz możesz rozmawiać ze swoim niestandardowym modelem Phi-3. Zaleca się zadawanie pytań na podstawie danych użytych do treningu.

    ![Chat with prompt flow.](../../../../../../translated_images/pl/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->