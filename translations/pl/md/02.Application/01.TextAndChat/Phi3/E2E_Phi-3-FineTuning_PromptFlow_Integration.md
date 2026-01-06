<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T14:23:02+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "pl"
}
-->
# Dostosuj i Zintegruj niestandardowe modele Phi-3 z Prompt flow

Ten kompletny (E2E) przykład oparty jest na przewodniku "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Przedstawia procesy dostrajania, wdrażania i integracji niestandardowych modeli Phi-3 z Prompt flow.

## Przegląd

W tym przykładzie E2E nauczysz się, jak dostroić model Phi-3 i zintegrować go z Prompt flow. Wykorzystując Azure Machine Learning i Prompt flow, stworzysz przepływ pracy do wdrażania i używania niestandardowych modeli AI. Ten przykład E2E podzielony jest na trzy scenariusze:

**Scenariusz 1: Konfiguracja zasobów Azure i przygotowanie do dostrajania**

**Scenariusz 2: Dostrajanie modelu Phi-3 i wdrażanie w Azure Machine Learning Studio**

**Scenariusz 3: Integracja z Prompt flow i rozmowa z własnym modelem**

Oto przegląd tego przykładu E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.pl.png)

### Spis treści

1. **[Scenariusz 1: Konfiguracja zasobów Azure i przygotowanie do dostrajania](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Utwórz Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Złóż wniosek o limity GPU w subskrypcji Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dodaj przypisanie roli](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Skonfiguruj projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Przygotuj zestaw danych do dostrajania](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariusz 2: Dostrajanie modelu Phi-3 i wdrażanie w Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Skonfiguruj Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dostrój model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Wdróż dostrojony model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariusz 3: Integracja z Prompt flow i rozmowa z własnym modelem](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Zintegruj niestandardowy model Phi-3 z Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rozmawiaj z własnym modelem](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenariusz 1: Konfiguracja zasobów Azure i przygotowanie do dostrajania

### Utwórz Azure Machine Learning Workspace

1. Wpisz *azure machine learning* w **pasku wyszukiwania** u góry strony portalu i wybierz **Azure Machine Learning** z pojawiających się opcji.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.pl.png)

1. Wybierz **+ Utwórz** z menu nawigacyjnego.

1. Wybierz **Nowy workspace** z menu nawigacyjnego.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.pl.png)

1. Wykonaj następujące zadania:

    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć (utwórz nową, jeśli to konieczne).
    - Wprowadź **Nazwa workspace**. Musi to być unikalna wartość.
    - Wybierz **Region**, którego chcesz użyć.
    - Wybierz **Konto magazynu** (Storage account) do użytku (utwórz nowe, jeśli to konieczne).
    - Wybierz **Key vault** do użytku (utwórz nowy, jeśli to konieczne).
    - Wybierz **Application insights** do użytku (utwórz nowy, jeśli to konieczne).
    - Wybierz **Container registry** do użytku (utwórz nowy, jeśli to konieczne).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.pl.png)

1. Wybierz **Review + Create**.

1. Wybierz **Create**.

### Złóż wniosek o limity GPU w subskrypcji Azure

W tym przykładzie E2E użyjesz *Standard_NC24ads_A100_v4 GPU* do dostrajania, co wymaga zgłoszenia limitu, oraz *Standard_E4s_v3* CPU do wdrożenia, co nie wymaga zgłoszenia limitu.

> [!NOTE]
>
> Tylko subskrypcje typu Pay-As-You-Go (standardowy typ subskrypcji) mają prawo do przydziału GPU; subskrypcje benefitowe nie są obecnie obsługiwane.
>
> Dla osób korzystających z subskrypcji benefitowych (takich jak Visual Studio Enterprise Subscription) lub chcących szybko przetestować proces dostrajania i wdrożenia, ten samouczek zawiera również wskazówki dotyczące dostrajania z minimalnym zestawem danych przy użyciu CPU. Jednak warto zauważyć, że wyniki dostrajania są znacznie lepsze przy użyciu GPU z większymi zbiorami danych.

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wykonaj następujące zadania, aby zgłosić limit dla *Standard NCADSA100v4 Family*:

    - Wybierz **Quota** z lewego menu.
    - Wybierz **Virtual machine family**, które chcesz użyć. Na przykład wybierz **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, które zawiera *Standard_NC24ads_A100_v4* GPU.
    - Wybierz **Request quota** z menu nawigacyjnego.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.pl.png)

    - Na stronie Request quota wpisz **Nowy limit rdzeni** (New cores limit), którego chcesz użyć. Na przykład 24.
    - Na stronie Request quota wybierz **Submit**, aby zgłosić limit GPU.

> [!NOTE]
> Możesz wybrać odpowiedni GPU lub CPU dla swoich potrzeb, odwołując się do dokumentu [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Dodaj przypisanie roli

Aby dostroić i wdrożyć swoje modele, musisz najpierw utworzyć User Assigned Managed Identity (UAI) i przypisać jej odpowiednie uprawnienia. Ta UAI będzie używana do uwierzytelniania podczas wdrożenia.

#### Utwórz User Assigned Managed Identity (UAI)

1. Wpisz *managed identities* w **pasku wyszukiwania** u góry strony portalu i wybierz **Managed Identities** z dostępnych opcji.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.pl.png)

1. Wybierz **+ Utwórz**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.pl.png)

1. Wykonaj następujące zadania:

    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć (utwórz nową, jeśli to konieczne).
    - Wybierz **Region**, którego chcesz użyć.
    - Wprowadź **Nazwa**. Musi być unikalna.

1. Wybierz **Review + create**.

1. Wybierz **+ Utwórz**.

#### Dodaj przypisanie roli Contributor do Managed Identity

1. Przejdź do zasobu Managed Identity, który utworzyłeś.

1. Wybierz **Azure role assignments** z lewego menu.

1. Wybierz **+ Dodaj przypisanie roli** z menu nawigacyjnego.

1. Na stronie Dodaj przypisanie roli wykonaj następujące czynności:
    - Wybierz **Zakres** (Scope) na **Resource group**.
    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć.
    - Wybierz rolę **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.pl.png)

1. Wybierz **Zapisz**.

#### Dodaj przypisanie roli Storage Blob Data Reader do Managed Identity

1. Wpisz *storage accounts* w **pasku wyszukiwania** u góry strony portalu i wybierz **Storage accounts** z dostępnych opcji.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.pl.png)

1. Wybierz konto magazynu powiązane z Azure Machine Learning workspace, które utworzyłeś. Na przykład *finetunephistorage*.

1. Wykonaj następujące zadania, aby przejść do strony Dodaj przypisanie roli:

    - Przejdź do konta Azure Storage, które utworzyłeś.
    - Wybierz **Access Control (IAM)** z lewego menu.
    - Wybierz **+ Dodaj** z menu nawigacyjnego.
    - Wybierz **Dodaj przypisanie roli** z menu nawigacyjnego.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.pl.png)

1. Na stronie Dodaj przypisanie roli wykonaj następujące zadania:

    - Na stronie roli wpisz *Storage Blob Data Reader* w **pasku wyszukiwania** i wybierz **Storage Blob Data Reader** z pojawiających się opcji.
    - Na stronie roli wybierz **Dalej** (Next).
    - Na stronie członków (Members) wybierz **Przydziel dostęp do** **Managed identity**.
    - Na stronie członków wybierz **+ Wybierz członków**.
    - Na stronie wyboru zarządzanych tożsamości (Select managed identities) wybierz swoją subskrypcję Azure **Subscription**.
    - Na stronie wyboru zarządzanych tożsamości wybierz **Managed identity**.
    - Na stronie wyboru zarządzanych tożsamości wybierz zarządzaną tożsamość, którą utworzyłeś. Na przykład *finetunephi-managedidentity*.
    - Na stronie wyboru zarządzanych tożsamości wybierz **Wybierz**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.pl.png)

1. Wybierz **Review + assign**.

#### Dodaj przypisanie roli AcrPull do Managed Identity

1. Wpisz *container registries* w **pasku wyszukiwania** u góry strony portalu i wybierz **Container registries** z dostępnych opcji.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.pl.png)

1. Wybierz rejestr kontenerów powiązany z Azure Machine Learning workspace. Na przykład *finetunephicontainerregistries*

1. Wykonaj następujące zadania, aby przejść do strony Dodaj przypisanie roli:

    - Wybierz **Access Control (IAM)** z lewego menu.
    - Wybierz **+ Dodaj** z menu nawigacyjnego.
    - Wybierz **Dodaj przypisanie roli** z menu nawigacyjnego.

1. Na stronie Dodaj przypisanie roli wykonaj następujące zadania:

    - Na stronie roli wpisz *AcrPull* w **pasku wyszukiwania** i wybierz **AcrPull** z pojawiających się opcji.
    - Na stronie roli wybierz **Dalej** (Next).
    - Na stronie członków (Members) wybierz **Przydziel dostęp do** **Managed identity**.
    - Na stronie członków wybierz **+ Wybierz członków**.
    - Na stronie wyboru zarządzanych tożsamości (Select managed identities) wybierz swoją subskrypcję Azure **Subscription**.
    - Na stronie wyboru zarządzanych tożsamości wybierz **Managed identity**.
    - Na stronie wyboru zarządzanych tożsamości wybierz zarządzaną tożsamość, którą utworzyłeś. Na przykład *finetunephi-managedidentity*.
    - Na stronie wyboru zarządzanych tożsamości wybierz **Wybierz**.
    - Wybierz **Review + assign**.

### Skonfiguruj projekt

Teraz utworzysz folder do pracy i skonfigurujesz wirtualne środowisko do tworzenia programu, który będzie wchodził w interakcję z użytkownikami i używał zapisanego historii rozmów z Azure Cosmos DB, aby wspierać swoje odpowiedzi.

#### Utwórz folder do pracy

1. Otwórz okno terminala i wpisz następującą komendę, aby utworzyć folder o nazwie *finetune-phi* w domyślnej ścieżce.

    ```console
    mkdir finetune-phi
    ```

1. Wpisz następującą komendę w terminalu, aby przejść do utworzonego folderu *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Utwórz wirtualne środowisko

1. Wpisz następującą komendę w terminalu, aby utworzyć wirtualne środowisko o nazwie *.venv*.

    ```console
    python -m venv .venv
    ```

1. Wpisz następującą komendę w terminalu, aby aktywować wirtualne środowisko.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Jeśli się powiodło, powinieneś zobaczyć *(.venv)* przed znakiem zachęty poleceń.

#### Zainstaluj wymagane pakiety

1. Wpisz następujące komendy w terminalu, aby zainstalować wymagane pakiety.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Utwórz pliki projektu
W tym ćwiczeniu utworzysz niezbędne pliki dla naszego projektu. Te pliki obejmują skrypty do pobierania zestawu danych, konfiguracji środowiska Azure Machine Learning, dopasowywania modelu Phi-3 oraz wdrażania dopasowanego modelu. Stworzysz również plik *conda.yml* do skonfigurowania środowiska dopasowywania.

W tym ćwiczeniu wykonasz:

- Utworzenie pliku *download_dataset.py* do pobrania zestawu danych.
- Utworzenie pliku *setup_ml.py* do utworzenia środowiska Azure Machine Learning.
- Utworzenie pliku *fine_tune.py* w folderze *finetuning_dir* do dopasowania modelu Phi-3 przy użyciu zestawu danych.
- Utworzenie pliku *conda.yml* do konfiguracji środowiska dopasowywania.
- Utworzenie pliku *deploy_model.py* do wdrożenia dopasowanego modelu.
- Utworzenie pliku *integrate_with_promptflow.py* do integracji dopasowanego modelu i uruchamiania modelu za pomocą Prompt flow.
- Utworzenie pliku flow.dag.yml do ustawienia struktury przepływu pracy dla Prompt flow.
- Utworzenie pliku *config.py* do wpisania informacji o Azure.

> [!NOTE]
>
> Pełna struktura folderów:
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

1. Otwórz **Visual Studio Code**.

1. Wybierz **File** z paska menu.

1. Wybierz **Open Folder**.

1. Wybierz folder *finetune-phi*, który utworzyłeś, znajdujący się w *C:\Users\yourUserName\finetune-phi*.

    ![Otwórz folder projektu.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.pl.png)

1. Po lewej stronie w Visual Studio Code, kliknij prawym przyciskiem i wybierz **New File**, aby utworzyć nowy plik o nazwie *download_dataset.py*.

1. Po lewej stronie w Visual Studio Code, kliknij prawym przyciskiem i wybierz **New File**, aby utworzyć nowy plik o nazwie *setup_ml.py*.

1. Po lewej stronie w Visual Studio Code, kliknij prawym przyciskiem i wybierz **New File**, aby utworzyć nowy plik o nazwie *deploy_model.py*.

    ![Utwórz nowy plik.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.pl.png)

1. Po lewej stronie w Visual Studio Code, kliknij prawym przyciskiem i wybierz **New Folder**, aby utworzyć nowy folder o nazwie *finetuning_dir*.

1. W folderze *finetuning_dir* utwórz nowy plik o nazwie *fine_tune.py*.

#### Utwórz i skonfiguruj plik *conda.yml*

1. Po lewej stronie w Visual Studio Code, kliknij prawym przyciskiem i wybierz **New File**, aby utworzyć nowy plik o nazwie *conda.yml*.

1. Dodaj następujący kod do pliku *conda.yml*, aby skonfigurować środowisko dopasowywania dla modelu Phi-3.

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

#### Utwórz i skonfiguruj plik *config.py*

1. Po lewej stronie w Visual Studio Code, kliknij prawym przyciskiem i wybierz **New File**, aby utworzyć nowy plik o nazwie *config.py*.

1. Dodaj następujący kod do pliku *config.py*, aby umieścić swoje informacje o Azure.

    ```python
    # Ustawienia Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Ustawienia Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Ustawienia zarządzanej tożsamości Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Ścieżki do plików zestawu danych
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Ustawienia modelu dostrojonego
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Dodaj zmienne środowiskowe Azure

1. Wykonaj następujące czynności, aby dodać identyfikator subskrypcji Azure:

    - Wpisz *subscriptions* w **pasku wyszukiwania** na górze strony portalowej i wybierz **Subscriptions** z pojawiających się opcji.
    - Wybierz subskrypcję Azure, której aktualnie używasz.
    - Skopiuj i wklej swój identyfikator subskrypcji do pliku *config.py*.

    ![Znajdź identyfikator subskrypcji.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.pl.png)

1. Wykonaj następujące czynności, aby dodać nazwę Azure Workspace:

    - Przejdź do zasobu Azure Machine Learning, który utworzyłeś.
    - Skopiuj i wklej swoją nazwę konta do pliku *config.py*.

    ![Znajdź nazwę Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.pl.png)

1. Wykonaj następujące czynności, aby dodać nazwę grupy zasobów Azure:

    - Przejdź do zasobu Azure Machine Learning, który utworzyłeś.
    - Skopiuj i wklej nazwę swojej grupy zasobów Azure do pliku *config.py*.

    ![Znajdź nazwę grupy zasobów.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.pl.png)

2. Wykonaj następujące czynności, aby dodać nazwę Managed Identity Azure:

    - Przejdź do zasobu Managed Identities, który utworzyłeś.
    - Skopiuj i wklej nazwę swojej Managed Identity Azure do pliku *config.py*.

    ![Znajdź UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.pl.png)

### Przygotuj zestaw danych do dopasowywania

W tym ćwiczeniu uruchomisz plik *download_dataset.py*, aby pobrać zestawy danych *ULTRACHAT_200k* do swojego lokalnego środowiska. Następnie użyjesz tych zestawów danych do dopasowania modelu Phi-3 w Azure Machine Learning.

#### Pobierz swój zestaw danych używając *download_dataset.py*

1. Otwórz plik *download_dataset.py* w Visual Studio Code.

1. Dodaj następujący kod do pliku *download_dataset.py*.

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
        # Załaduj zestaw danych o określonej nazwie, konfiguracji i proporcji podziału
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Podziel zestaw danych na zbiór treningowy i testowy (80% trening, 20% test)
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
        
        # Otwórz plik w trybie do zapisu
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iteruj po każdym rekordzie w zestawie danych
            for record in dataset:
                # Zrzutuj rekord jako obiekt JSON i zapisz go do pliku
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
        
        # Wyodrębnij z podziału zbiory treningowy i testowy
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Zapisz zbiór treningowy do pliku JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Zapisz zbiór testowy do osobnego pliku JSONL
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Wskazówki dotyczące dopasowywania z minimalnym zestawem danych używając CPU**
>
> Jeśli chcesz użyć CPU do dopasowywania, to podejście jest idealne dla osób z subskrypcjami benefitowymi (takimi jak Visual Studio Enterprise Subscription) lub do szybkiego przetestowania procesu dopasowywania i wdrażania.
>
> Zamień `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` na `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Wpisz następujące polecenie w terminalu, aby uruchomić skrypt i pobrać zestaw danych do lokalnego środowiska.

    ```console
    python download_data.py
    ```

1. Sprawdź, czy zestawy danych zostały poprawnie zapisane w lokalnym katalogu *finetune-phi/data*.

> [!NOTE]
>
> **Rozmiar zestawu danych i czas dopasowywania**
>
> W tym próbce E2E używasz tylko 1% zestawu danych (`train_sft[:1%]`). To znacząco zmniejsza ilość danych, przyspieszając zarówno proces przesyłania, jak i dopasowywania. Możesz dostosować procent, aby znaleźć właściwy balans między czasem treningu a wydajnością modelu. Użycie mniejszego podzbioru zestawu danych skraca czas dopasowywania, czyniąc proces bardziej wykonalnym dla próbki E2E.

## Scenariusz 2: Dopasuj model Phi-3 i wdroż go w Azure Machine Learning Studio

### Skonfiguruj Azure CLI

Musisz skonfigurować Azure CLI, aby uwierzytelnić swoje środowisko. Azure CLI pozwala zarządzać zasobami Azure bezpośrednio z wiersza polecenia i dostarcza poświadczenia niezbędne do dostępu Azure Machine Learning do tych zasobów. Aby zacząć, zainstaluj [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

1. Otwórz okno terminala i wpisz następujące polecenie, aby zalogować się na swoje konto Azure.

    ```console
    az login
    ```

1. Wybierz konto Azure, którego chcesz używać.

1. Wybierz subskrypcję Azure, której chcesz używać.

    ![Znajdź nazwę grupy zasobów.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.pl.png)

> [!TIP]
>
> Jeśli masz problemy z zalogowaniem do Azure, spróbuj użyć kodu urządzenia. Otwórz okno terminala i wpisz następujące polecenie, aby zalogować się do Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Dopasuj model Phi-3

W tym ćwiczeniu dopasujesz model Phi-3 przy użyciu dostarczonego zestawu danych. Najpierw zdefiniujesz proces dopasowywania w pliku *fine_tune.py*. Następnie skonfigurujesz środowisko Azure Machine Learning i zainicjujesz proces dopasowywania, uruchamiając plik *setup_ml.py*. Ten skrypt zapewnia, że dopasowanie odbywa się w środowisku Azure Machine Learning.

Uruchamiając *setup_ml.py*, przeprowadzisz proces dopasowywania w środowisku Azure Machine Learning.

#### Dodaj kod do pliku *fine_tune.py*

1. Przejdź do folderu *finetuning_dir* i otwórz plik *fine_tune.py* w Visual Studio Code.

1. Dodaj następujący kod do pliku *fine_tune.py*.

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

    # Aby uniknąć błędu INVALID_PARAMETER_VALUE w MLflow, wyłącz integrację MLflow
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Konfiguracja logowania
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

1. Zapisz i zamknij plik *fine_tune.py*.

> [!TIP]
> **Możesz dopasować model Phi-3.5**
>
> W pliku *fine_tune.py* możesz zmienić `pretrained_model_name` z `"microsoft/Phi-3-mini-4k-instruct"` na dowolny model, który chcesz dopasować. Na przykład, jeśli zmienisz go na `"microsoft/Phi-3.5-mini-instruct"`, użyjesz modelu Phi-3.5-mini-instruct do dopasowywania. Aby znaleźć i użyć preferowaną nazwę modelu, odwiedź [Hugging Face](https://huggingface.co/), wyszukaj interesujący Cię model, a następnie skopiuj i wklej jego nazwę do pola `pretrained_model_name` w swoim skrypcie.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Dopasowanie Phi-3.5.">
>

#### Dodaj kod do pliku *setup_ml.py*

1. Otwórz plik *setup_ml.py* w Visual Studio Code.

1. Dodaj następujący kod do pliku *setup_ml.py*.

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

    # Stałe

    # Odkomentuj poniższe linie, aby użyć instancji CPU do trenowania
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Odkomentuj poniższe linie, aby użyć instancji GPU do trenowania
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Zamień na lokalizację twojego klastra obliczeniowego
    FINETUNING_DIR = "./finetuning_dir" # Ścieżka do skryptu dostrajania
    TRAINING_ENV_NAME = "phi-3-training-environment" # Nazwa środowiska treningowego
    MODEL_OUTPUT_DIR = "./model_output" # Ścieżka do katalogu wyjściowego modelu w Azure ML

    # Konfiguracja logowania do śledzenia procesu
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
            image=DOCKER_IMAGE_NAME,  # Obraz Dockera dla środowiska
            conda_file=CONDA_FILE,  # Plik środowiska Conda
            name=TRAINING_ENV_NAME,  # Nazwa środowiska
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
                tier="Dedicated",  # Poziom klastra obliczeniowego
                min_instances=0,  # Minimalna liczba instancji
                max_instances=1  # Maksymalna liczba instancji
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Czekaj na utworzenie klastra
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Ścieżka do fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Środowisko treningowe
            compute=compute_name,  # Klastr obliczeniowy do użycia
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Ścieżka do pliku danych treningowych
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Ścieżka do pliku danych ewaluacyjnych
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Inicjalizuj klienta ML
        ml_client = get_ml_client()

        # Utwórz środowisko
        env = create_or_get_environment(ml_client)
        
        # Utwórz lub pobierz istniejący klaster obliczeniowy
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Utwórz i wyślij zadanie dostrajania
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Wyślij zadanie
        ml_client.jobs.stream(returned_job.name)  # Strumieniuj logi zadania
        
        # Przechwyć nazwę zadania
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Zamień `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` oraz `LOCATION` na swoje konkretne dane.

    ```python
   # Odkomentuj poniższe linie, aby użyć instancji GPU do treningu
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Zamień na lokalizację swojego klastra obliczeniowego
    ```

> [!TIP]
>
> **Wskazówki dotyczące dopasowywania z minimalnym zestawem danych używając CPU**
>
> Jeśli chcesz użyć CPU do dopasowywania, to podejście jest idealne dla osób z subskrypcjami benefitowymi (takimi jak Visual Studio Enterprise Subscription) lub do szybkiego przetestowania procesu dopasowywania i wdrażania.
>
> 1. Otwórz plik *setup_ml*.
> 1. Zamień `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` oraz `DOCKER_IMAGE_NAME` zgodnie z poniższym. Jeżeli nie masz dostępu do *Standard_E16s_v3*, możesz użyć równoważnej instancji CPU lub poprosić o nową kwotę.
> 1. Zamień `LOCATION` na swoje dane.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Wpisz następujące polecenie, aby uruchomić skrypt *setup_ml.py* i rozpocząć proces dopasowywania w Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. W tym ćwiczeniu skutecznie dopasowałeś model Phi-3 przy użyciu Azure Machine Learning. Uruchamiając skrypt *setup_ml.py*, skonfigurowałeś środowisko Azure Machine Learning oraz zainicjowałeś proces dopasowywania określony w pliku *fine_tune.py*. Należy pamiętać, że proces dopasowywania może potrwać dość długo. Po uruchomieniu polecenia `python setup_ml.py` musisz poczekać na jego zakończenie. Możesz monitorować status zadania dopasowywania, śledząc link podany w terminalu do portalu Azure Machine Learning.

    ![Zobacz zadanie dopasowywania.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.pl.png)

### Wdróż dopasowany model

Aby zintegrować dopasowany model Phi-3 z Prompt Flow, musisz wdrożyć model, by był dostępny do inferencji w czasie rzeczywistym. Proces ten obejmuje zarejestrowanie modelu, utworzenie punktu końcowego online oraz wdrożenie modelu.

#### Ustaw nazwę modelu, nazwę punktu końcowego i nazwę wdrożenia do wdrożenia

1. Otwórz plik *config.py*.

1. Zamień `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` na pożądaną nazwę swojego modelu.

1. Zamień `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` na pożądaną nazwę punktu końcowego.

1. Zamień `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` na pożądaną nazwę swojego wdrożenia.

#### Dodaj kod do pliku *deploy_model.py*

Uruchomienie pliku *deploy_model.py* automatyzuje cały proces wdrożenia. Rejestruje model, tworzy punkt końcowy oraz realizuje wdrożenie na podstawie ustawień określonych w pliku config.py, które obejmują nazwę modelu, nazwę punktu końcowego oraz nazwę wdrożenia.

1. Otwórz plik *deploy_model.py* w Visual Studio Code.

1. Dodaj następujący kod do pliku *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Importy konfiguracji
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

    # Stałe
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Konfiguracja logowania
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
            # Pobierz bieżące szczegóły punktu końcowego
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Zaloguj bieżący przydział ruchu do celów debugowania
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Ustaw przydział ruchu dla wdrożenia
            endpoint.traffic = {deployment_name: 100}
            
            # Zaktualizuj punkt końcowy z nowym przydziałem ruchu
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Zaloguj zaktualizowany przydział ruchu do celów debugowania
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Zaloguj wszelkie błędy, które wystąpią podczas procesu
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

1. Wykonaj następujące czynności, aby uzyskać `JOB_NAME`:

    - Przejdź do zasobu Azure Machine Learning, który utworzyłeś.
    - Wybierz **Studio web URL**, aby otworzyć przestrzeń roboczą Azure Machine Learning.
    - Wybierz **Jobs** z lewego panelu.
    - Wybierz eksperyment dotyczacy dopasowywania, na przykład *finetunephi*.
    - Wybierz utworzone zadanie.
    - Skopiuj i wklej nazwę swojego zadania do `JOB_NAME = "twoja-nazwa-zadania"` w pliku *deploy_model.py*.

1. Zamień `COMPUTE_INSTANCE_TYPE` na swoje konkretne dane.

1. Wpisz następujące polecenie, aby uruchomić skrypt *deploy_model.py* i rozpocząć proces wdrażania w Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Aby uniknąć dodatkowych opłat na swoim koncie, upewnij się, że usuniesz utworzony punkt końcowy w przestrzeni roboczej Azure Machine Learning.
>

#### Sprawdź status wdrożenia w przestrzeni roboczej Azure Machine Learning

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Przejdź do utworzonej przez siebie przestrzeni roboczej Azure Machine Learning.

1. Wybierz **Studio web URL**, aby otworzyć przestrzeń roboczą Azure Machine Learning.

1. Wybierz **Endpoints** z lewego panelu.

    ![Wybierz punkty końcowe.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.pl.png)

2. Wybierz punkt końcowy, który utworzyłeś.

    ![Wybierz utworzone punkty końcowe.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.pl.png)

3. Na tej stronie możesz zarządzać punktami końcowymi utworzonymi podczas procesu wdrażania.

## Scenariusz 3: Integracja z Prompt flow i rozmowa z własnym modelem

### Integracja własnego modelu Phi-3 z Prompt flow

Po pomyślnym wdrożeniu wytrenowanego modelu możesz teraz zintegrować go z Prompt flow, aby używać modelu w aplikacjach w czasie rzeczywistym, umożliwiając różnorodne interaktywne zadania z Twoim niestandardowym modelem Phi-3.

#### Ustaw klucz API i URI punktu końcowego wytrenowanego modelu Phi-3

1. Przejdź do utworzonej przestrzeni roboczej Azure Machine Learning.
1. Wybierz **Endpoints** z lewego panelu.
1. Wybierz punkt końcowy, który utworzyłeś.
1. Wybierz **Consume** z menu nawigacyjnego.
1. Skopiuj i wklej swój **REST endpoint** do pliku *config.py*, zastępując `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` swoim **REST endpoint**.
1. Skopiuj i wklej swój **Primary key** do pliku *config.py*, zastępując `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` swoim **Primary key**.

    ![Kopiuj klucz API i URI punktu końcowego.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.pl.png)

#### Dodaj kod do pliku *flow.dag.yml*

1. Otwórz plik *flow.dag.yml* w Visual Studio Code.

1. Dodaj następujący kod do *flow.dag.yml*.

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

#### Dodaj kod do pliku *integrate_with_promptflow.py*

1. Otwórz plik *integrate_with_promptflow.py* w Visual Studio Code.

1. Dodaj następujący kod do *integrate_with_promptflow.py*.

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

    # Konfiguracja logowania
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

### Rozmowa z własnym modelem

1. Wpisz następujące polecenie, aby uruchomić skrypt *deploy_model.py* i rozpocząć proces wdrażania w Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Oto przykład wyników: teraz możesz rozmawiać ze swoim niestandardowym modelem Phi-3. Zaleca się zadawanie pytań opartych na danych użytych do dostrojenia.

    ![Przykład prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.pl.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego, tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->