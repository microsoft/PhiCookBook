<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T09:32:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "cs"
}
-->
# Doladění a integrace vlastních modelů Phi-3 s Prompt flow

Tento end-to-end (E2E) příklad je založen na průvodci „[Doladění a integrace vlastních modelů Phi-3 s Prompt Flow: krok za krokem](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)“ z Microsoft Tech Community. Představuje procesy doladění, nasazení a integrace vlastních modelů Phi-3 s Prompt flow.

## Přehled

V tomto E2E příkladu se naučíte, jak doladit model Phi-3 a integrovat ho s Prompt flow. Využitím Azure Machine Learning a Prompt flow vytvoříte workflow pro nasazení a využití vlastních AI modelů. Tento E2E příklad je rozdělen do tří scénářů:

**Scénář 1: Nastavení zdrojů Azure a příprava na doladění**

**Scénář 2: Doladění modelu Phi-3 a nasazení v Azure Machine Learning Studio**

**Scénář 3: Integrace s Prompt flow a chat s vaším vlastním modelem**

Zde je přehled tohoto E2E příkladu.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/cs/00-01-architecture.02fc569e266d468c.webp)

### Obsah

1. **[Scénář 1: Nastavení zdrojů Azure a příprava na doladění](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Vytvoření Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Žádost o kvóty GPU v Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Přidání přiřazení role](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nastavení projektu](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Příprava datové sady pro doladění](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénář 2: Doladění modelu Phi-3 a nasazení v Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Nastavení Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Doladění modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasazení doladěného modelu](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénář 3: Integrace s Prompt flow a chat s vaším vlastním modelem](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrace vlastního modelu Phi-3 s Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat s vlastním modelem](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scénář 1: Nastavení zdrojů Azure a příprava na doladění

### Vytvoření Azure Machine Learning Workspace

1. Do **vyhledávacího pole** v horní části portálu napište *azure machine learning* a z dostupných možností vyberte **Azure Machine Learning**.

    ![Type azure machine learning](../../../../../../translated_images/cs/01-01-type-azml.a5116f8454d98c60.webp)

1. Vyberte **+ Vytvořit** v navigačním menu.

1. Zvolte **Nové pracovní prostředí** v navigačním menu.

    ![Select new workspace](../../../../../../translated_images/cs/01-02-select-new-workspace.83e17436f8898dc4.webp)

1. Proveďte následující kroky:

    - Vyberte vaši Azure **Subscription**.
    - Vyberte **Resource group**, kterou chcete použít (vytvořte novou, pokud je potřeba).
    - Zadejte **Název pracovního prostředí**. Musí to být jedinečná hodnota.
    - Vyberte **Region**, který chcete použít.
    - Vyberte **Storage account**, který chcete použít (vytvořte nový, pokud je potřeba).
    - Vyberte **Key vault**, který chcete použít (vytvořte nový, pokud je potřeba).
    - Vyberte **Application insights**, který chcete použít (vytvořte nový, pokud je potřeba).
    - Vyberte **Container registry**, který chcete použít (vytvořte nový, pokud je potřeba).

    ![Fill AZML.](../../../../../../translated_images/cs/01-03-fill-AZML.730a5177757bbebb.webp)

1. Vyberte **Kontrola + vytvoření**.

1. Vyberte **Vytvořit**.

### Žádost o kvóty GPU v Azure Subscription

V tomto E2E příkladu budete používat *Standard_NC24ads_A100_v4 GPU* pro doladění, která vyžaduje žádost o kvótu, a *Standard_E4s_v3* CPU pro nasazení, která žádost o kvótu nevyžaduje.

> [!NOTE]
>
> Pouze předplatná typu Pay-As-You-Go (standardní typ předplatného) jsou způsobilá pro přidělení GPU; benefitní předplatná momentálně nejsou podporována.
>
> Pro ty, kteří používají benefitní předplatná (např. Visual Studio Enterprise Subscription) nebo chtějí rychle otestovat proces doladění a nasazení, tento tutoriál nabízí také návod na doladění s minimální datasetem pomocí CPU. Nicméně je důležité poznamenat, že výsledky doladění jsou výrazně lepší při použití GPU s většími datovými sadami.

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Proveďte následující kroky pro žádost o kvótu *Standard NCADSA100v4 Family*:

    - Vyberte **Kvóty** z levé boční záložky.
    - Vyberte **Rodinu virtuálních strojů**, kterou chcete použít. Například vyberte **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, která zahrnuje *Standard_NC24ads_A100_v4* GPU.
    - Vyberte **Žádat o kvótu** v navigačním menu.

        ![Request quota.](../../../../../../translated_images/cs/01-04-request-quota.3d3670c3221ab834.webp)

    - Na stránce žádosti o kvótu zadejte **Nový limit jader**, který chcete použít. Například 24.
    - Na stránce žádosti o kvótu vyberte **Odeslat** pro žádost o kvótu GPU.

> [!NOTE]
> Můžete si vybrat vhodné GPU nebo CPU podle svých potřeb, viz dokument [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Přidání přiřazení role

Pro doladění a nasazení vašich modelů musíte nejprve vytvořit User Assigned Managed Identity (UAI) a přiřadit jí odpovídající oprávnění. Tato UAI bude použita pro autentizaci během nasazení.

#### Vytvoření User Assigned Managed Identity (UAI)

1. Do **vyhledávacího pole** v horní části portálu napište *managed identities* a z dostupných možností vyberte **Managed Identities**.

    ![Type managed identities.](../../../../../../translated_images/cs/01-05-type-managed-identities.9297b6039874eff8.webp)

1. Vyberte **+ Vytvořit**.

    ![Select create.](../../../../../../translated_images/cs/01-06-select-create.936d8d66d7144f9a.webp)

1. Proveďte následující kroky:

    - Vyberte vaši Azure **Subscription**.
    - Vyberte **Resource group**, kterou chcete použít (vytvořte novou, pokud je potřeba).
    - Vyberte **Region**, který chcete použít.
    - Zadejte **Název**. Musí být jedinečná hodnota.

1. Vyberte **Kontrola + vytvoření**.

1. Vyberte **+ Vytvořit**.

#### Přidání role Přispěvatele (Contributor) pro Managed Identity

1. Přejděte na zdroj Managed Identity, který jste vytvořili.

1. Vyberte **Přiřazení rolí Azure** na levé boční záložce.

1. Zvolte **+ Přidat přiřazení role** v navigačním menu.

1. Na stránce Přidat přiřazení role proveďte následující kroky:
    - Nastavte **Rozsah** na **Resource group**.
    - Vyberte vaši Azure **Subscription**.
    - Vyberte **Resource group**, kterou chcete použít.
    - Vyberte roli **Přispěvatel (Contributor)**.

    ![Fill contributor role.](../../../../../../translated_images/cs/01-07-fill-contributor-role.29ca99b7c9f687e0.webp)

1. Vyberte **Uložit**.

#### Přidání role Storage Blob Data Reader pro Managed Identity

1. Do **vyhledávacího pole** v horní části portálu napište *storage accounts* a z dostupných možností vyberte **Storage accounts**.

    ![Type storage accounts.](../../../../../../translated_images/cs/01-08-type-storage-accounts.1186c8e42933e49b.webp)

1. Vyberte storage účet spojený s Azure Machine Learning workspace, který jste vytvořili. Například *finetunephistorage*.

1. Proveďte následující kroky pro navigaci na stránku Přidat přiřazení role:

    - Přejděte na vytvořený Azure Storage účet.
    - Vyberte **Řízení přístupu (IAM)** na levé boční záložce.
    - Vyberte **+ Přidat** v navigačním menu.
    - Zvolte **Přidat přiřazení role**.

    ![Add role.](../../../../../../translated_images/cs/01-09-add-role.d2db22fec1b187f0.webp)

1. Na stránce Přidat přiřazení role proveďte:

    - Do vyhledávacího pole zadejte *Storage Blob Data Reader* a vyberte **Storage Blob Data Reader**.
    - Zvolte **Další**.
    - Na stránce Členové vyberte **Přiřadit přístup k** **Spravované identitě (Managed identity)**.
    - Vyberte **+ Vybrat členy**.
    - Vyberte vaši Azure **Subscription**.
    - Vyberte **Spravovanou identitu (Managed Identity)**.
    - Vyberte spravovanou identitu, kterou jste vytvořili. Například *finetunephi-managedidentity*.
    - Klikněte na **Vybrat**.

    ![Select managed identity.](../../../../../../translated_images/cs/01-10-select-managed-identity.5ce5ba181f72a4df.webp)

1. Vyberte **Kontrola + přiřazení**.

#### Přidání role AcrPull pro Managed Identity

1. Do **vyhledávacího pole** v horní části portálu napište *container registries* a z dostupných možností vyberte **Container registries**.

    ![Type container registries.](../../../../../../translated_images/cs/01-11-type-container-registries.ff3b8bdc49dc596c.webp)

1. Vyberte container registry spojený s Azure Machine Learning workspace. Například *finetunephicontainerregistries*.

1. Proveďte kroky pro navigaci na stránku Přidat přiřazení role:

    - Vyberte **Řízení přístupu (IAM)** na levé záložce.
    - Klikněte na **+ Přidat**.
    - Vyberte **Přidat přiřazení role**.

1. Na stránce Přidat přiřazení role proveďte:

    - Do vyhledávacího pole zadejte *AcrPull* a vyberte **AcrPull**.
    - Zvolte **Další**.
    - Na stránce Členové vyberte **Přiřadit přístup k** **Spravované identitě**.
    - Klikněte na **+ Vybrat členy**.
    - Vyberte Azure **Subscription**.
    - Vyberte **Spravovanou identitu (Managed Identity)**.
    - Vyberte spravovanou identitu, kterou jste vytvořili, například *finetunephi-managedidentity*.
    - Klikněte na **Vybrat**.
    - Vyberte **Kontrola + přiřazení**.

### Nastavení projektu

Nyní vytvoříte složku, ve které budete pracovat, a nastavíte virtuální prostředí pro vývoj programu, který bude komunikovat s uživateli a využívat uloženou historii chatu z Azure Cosmos DB k informování svých odpovědí.

#### Vytvoření pracovní složky

1. Otevřete terminál a zadejte následující příkaz pro vytvoření složky s názvem *finetune-phi* v výchozí cestě.

    ```console
    mkdir finetune-phi
    ```

1. Zadejte do terminálu tento příkaz pro přechod do složky *finetune-phi*, kterou jste vytvořili.

    ```console
    cd finetune-phi
    ```

#### Vytvoření virtuálního prostředí

1. Zadejte do terminálu tento příkaz pro vytvoření virtuálního prostředí s názvem *.venv*.

    ```console
    python -m venv .venv
    ```

1. Zadejte do terminálu tento příkaz pro aktivaci virtuálního prostředí.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Pokud to fungovalo, měli byste před příkazovým řádkem vidět *(.venv)*.

#### Instalace potřebných balíčků

1. Zadejte do terminálu následující příkazy k instalaci požadovaných balíčků.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Vytvoření projektových souborů
V tomto cvičení vytvoříte základní soubory pro náš projekt. Tyto soubory zahrnují skripty pro stažení datové sady, nastavení prostředí Azure Machine Learning, doladění modelu Phi-3 a nasazení doladěného modelu. Také vytvoříte soubor *conda.yml* pro nastavení prostředí pro doladění.

V tomto cvičení:

- Vytvoříte soubor *download_dataset.py* ke stažení datové sady.
- Vytvoříte soubor *setup_ml.py* pro nastavení prostředí Azure Machine Learning.
- Vytvoříte soubor *fine_tune.py* ve složce *finetuning_dir* k doladění modelu Phi-3 za použití datové sady.
- Vytvoříte soubor *conda.yml* pro nastavení prostředí doladění.
- Vytvoříte soubor *deploy_model.py* k nasazení doladěného modelu.
- Vytvoříte soubor *integrate_with_promptflow.py*, pro integraci doladěného modelu a spuštění modelu pomocí Prompt flow.
- Vytvoříte soubor flow.dag.yml pro nastavení struktury pracovního postupu pro Prompt flow.
- Vytvoříte soubor *config.py*, do kterého zadáte informace o Azure.

> [!NOTE]
>
> Kompletní struktura složek:
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

1. Otevřete **Visual Studio Code**.

1. Vyberte **Soubor** v liště nabídky.

1. Vyberte **Otevřít složku**.

1. Vyberte složku *finetune-phi*, kterou jste vytvořili, nacházející se na cestě *C:\Users\yourUserName\finetune-phi*.

    ![Otevřít složku projektu.](../../../../../../translated_images/cs/01-12-open-project-folder.1fff9c7f41dd1639.webp)

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem myši a vyberte **Nový soubor** pro vytvoření nového souboru s názvem *download_dataset.py*.

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem myši a vyberte **Nový soubor** pro vytvoření nového souboru s názvem *setup_ml.py*.

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem myši a vyberte **Nový soubor** pro vytvoření nového souboru s názvem *deploy_model.py*.

    ![Vytvořit nový soubor.](../../../../../../translated_images/cs/01-13-create-new-file.c17c150fff384a39.webp)

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem myši a vyberte **Nová složka** pro vytvoření nové složky s názvem *finetuning_dir*.

1. Ve složce *finetuning_dir* vytvořte nový soubor s názvem *fine_tune.py*.

#### Vytvoření a konfigurace souboru *conda.yml*

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem myši a vyberte **Nový soubor** pro vytvoření nového souboru s názvem *conda.yml*.

1. Přidejte do souboru *conda.yml* následující kód pro nastavení prostředí doladění modelu Phi-3.

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

#### Vytvoření a konfigurace souboru *config.py*

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem myši a vyberte **Nový soubor** pro vytvoření nového souboru s názvem *config.py*.

1. Přidejte do souboru *config.py* následující kód, který obsahuje vaše informace o Azure.

    ```python
    # Nastavení Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Nastavení Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Nastavení Azure Managed Identity
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Cesty k souborům datasetu
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Nastavení jemně doladěného modelu
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Přidání proměnných prostředí Azure

1. Proveďte následující kroky pro přidání Azure Subscription ID:

    - Napište *subscriptions* do **vyhledávacího panelu** v horní části portálu a vyberte **Subscriptions** z nabídky.
    - Vyberte Azure Subscription, kterou právě používáte.
    - Zkopírujte a vložte své Subscription ID do souboru *config.py*.

    ![Najít ID předplatného.](../../../../../../translated_images/cs/01-14-find-subscriptionid.4f4ca33555f1e637.webp)

1. Proveďte následující kroky pro přidání názvu Azure Workspace:

    - Přejděte do zdroje Azure Machine Learning, který jste vytvořili.
    - Zkopírujte a vložte své jméno účtu do souboru *config.py*.

    ![Najít název Azure Machine Learning.](../../../../../../translated_images/cs/01-15-find-AZML-name.1975f0422bca19a7.webp)

1. Proveďte následující kroky pro přidání názvu Azure Resource Group:

    - Přejděte do zdroje Azure Machine Learning, který jste vytvořili.
    - Zkopírujte a vložte název vaší skupiny zdrojů Azure do souboru *config.py*.

    ![Najít název skupiny zdrojů.](../../../../../../translated_images/cs/01-16-find-AZML-resourcegroup.855a349d0af134a3.webp)

2. Proveďte následující kroky pro přidání názvu Azure Managed Identity:

    - Přejděte do zdroje spravovaných identit, který jste vytvořili.
    - Zkopírujte a vložte název vaší Azure Managed Identity do souboru *config.py*.

    ![Najít UAI.](../../../../../../translated_images/cs/01-17-find-uai.3529464f53499827.webp)

### Příprava datové sady pro doladění

V tomto cvičení spustíte soubor *download_dataset.py*, abyste stáhli datovou sadu *ULTRACHAT_200k* do svého lokálního prostředí. Tuto datovou sadu pak použijete k doladění modelu Phi-3 v Azure Machine Learning.

#### Stažení datové sady pomocí *download_dataset.py*

1. Otevřete soubor *download_dataset.py* ve Visual Studio Code.

1. Přidejte do souboru *download_dataset.py* následující kód.

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
        # Načíst datovou sadu se specifikovaným názvem, konfigurací a poměrem rozdělení
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Rozdělit datovou sadu na trénovací a testovací sady (80 % trénink, 20 % test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Vytvořit adresář, pokud neexistuje
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Otevřít soubor v režimu zápisu
        with open(filepath, 'w', encoding='utf-8') as f:
            # Projít každý záznam v datové sadě
            for record in dataset:
                # Zapsat záznam jako JSON objekt do souboru
                json.dump(record, f)
                # Zapsat znak nového řádku pro oddělení záznamů
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Načíst a rozdělit datovou sadu ULTRACHAT_200k se specifickou konfigurací a poměrem rozdělení
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrahovat tréninkovou a testovací datovou sadu ze splitu
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Uložit tréninkovou datovou sadu do JSONL souboru
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Uložit testovací datovou sadu do samostatného JSONL souboru
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Pokyny pro doladění s minimální datovou sadou pomocí CPU**
>
> Pokud chcete použít CPU pro doladění, tento přístup je ideální pro uživatele s výhodnými předplatnými (například Visual Studio Enterprise Subscription) nebo pro rychlé otestování procesu doladění a nasazení.
>
> Nahraďte `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` za `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Zadejte následující příkaz do terminálu, abyste spustili skript a stáhli datovou sadu do svého lokálního prostředí.

    ```console
    python download_data.py
    ```

1. Ověřte, že byly datové sady úspěšně uloženy do složky *finetune-phi/data* na vašem počítači.

> [!NOTE]
>
> **Velikost datové sady a doba doladění**
>
> V tomto E2E příkladu používáte pouze 1 % datové sady (`train_sft[:1%]`). To výrazně sníží množství dat, což urychlí jak nahrávání, tak proces doladění. Pro nalezení správné rovnováhy mezi dobou tréninku a výkonem modelu můžete procento upravit. Používání menšího podmnožiny dat snižuje čas potřebný pro doladění, takže je proces lépe zvládnutelný pro E2E příklad.

## Scénář 2: Doladění modelu Phi-3 a nasazení v Azure Machine Learning Studio

### Nastavení Azure CLI

Musíte nastavit Azure CLI pro ověření vašeho prostředí. Azure CLI umožňuje přímo spravovat zdroje Azure z příkazového řádku a poskytuje pověření potřebná pro přístup Azure Machine Learning k těmto zdrojům. Pro začátek nainstalujte [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Otevřete terminál a zadejte následující příkaz pro přihlášení ke svému Azure účtu.

    ```console
    az login
    ```

1. Vyberte Azure účet, který chcete použít.

1. Vyberte Azure subscription, kterou chcete použít.

    ![Najít název skupiny zdrojů.](../../../../../../translated_images/cs/02-01-login-using-azure-cli.dfde31cb75e58a87.webp)

> [!TIP]
>
> Pokud máte potíže s přihlášením do Azure, zkuste použít kód zařízení. Otevřete terminál a zadejte tento příkaz pro přihlášení do vašeho Azure účtu:
>
> ```console
> az login --use-device-code
> ```
>

### Doladění modelu Phi-3

V tomto cvičení doladíte model Phi-3 pomocí poskytnuté datové sady. Nejprve definujete proces doladění v souboru *fine_tune.py*. Poté nastavíte prostředí Azure Machine Learning a spustíte proces doladění spuštěním souboru *setup_ml.py*. Tento skript zajistí, že doladění proběhne v prostředí Azure Machine Learning.

Spuštěním *setup_ml.py* spustíte proces doladění v prostředí Azure Machine Learning.

#### Přidání kódu do souboru *fine_tune.py*

1. Přejděte do složky *finetuning_dir* a otevřete soubor *fine_tune.py* ve Visual Studio Code.

1. Přidejte do souboru *fine_tune.py* následující kód.

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

    # Chcete-li se vyhnout chybě INVALID_PARAMETER_VALUE v MLflow, zakažte integraci MLflow
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Nastavení protokolování
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

1. Uložte a zavřete soubor *fine_tune.py*.

> [!TIP]
> **Můžete doladit model Phi-3.5**
>
> V souboru *fine_tune.py* můžete změnit hodnotu `pretrained_model_name` z `"microsoft/Phi-3-mini-4k-instruct"` na jakýkoli model, který chcete doladit. Například pokud jej změníte na `"microsoft/Phi-3.5-mini-instruct"`, použijete pro doladění model Phi-3.5-mini-instruct. Pro vyhledání a použití požadovaného názvu modelu navštivte [Hugging Face](https://huggingface.co/), vyhledejte vámi požadovaný model a zkopírujte jeho název do pole `pretrained_model_name` ve vašem skriptu.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Doladění Phi-3.5.">
>

#### Přidání kódu do souboru *setup_ml.py*

1. Otevřete soubor *setup_ml.py* ve Visual Studio Code.

1. Přidejte do souboru *setup_ml.py* následující kód.

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

    # Konstanty

    # Odkomentujte následující řádky pro použití CPU instance pro trénink
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Odkomentujte následující řádky pro použití GPU instance pro trénink
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Nahraďte místem vašeho výpočetního clusteru
    FINETUNING_DIR = "./finetuning_dir" # Cesta k skriptu pro doladění
    TRAINING_ENV_NAME = "phi-3-training-environment" # Název tréninkového prostředí
    MODEL_OUTPUT_DIR = "./model_output" # Cesta k výstupní složce modelu v Azure ML

    # Nastavení logování pro sledování průběhu
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
            image=DOCKER_IMAGE_NAME,  # Docker image pro prostředí
            conda_file=CONDA_FILE,  # Conda soubor prostředí
            name=TRAINING_ENV_NAME,  # Název prostředí
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
                tier="Dedicated",  # Úroveň výpočetního clusteru
                min_instances=0,  # Minimální počet instancí
                max_instances=1  # Maximální počet instancí
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Čekat na vytvoření clusteru
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Cesta k fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Tréninkové prostředí
            compute=compute_name,  # Výpočetní cluster k použití
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Cesta k souboru s tréninkovými daty
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Cesta k souboru s evaluačními daty
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Inicializovat ML klienta
        ml_client = get_ml_client()

        # Vytvořit prostředí
        env = create_or_get_environment(ml_client)
        
        # Vytvořit nebo získat existující výpočetní cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Vytvořit a odeslat úlohu doladění
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Odeslat úlohu
        ml_client.jobs.stream(returned_job.name)  # Streamovat logy úlohy
        
        # Zachytit název úlohy
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Nahraďte `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` a `LOCATION` vašimi konkrétními údaji.

    ```python
   # Odkomentujte následující řádky pro použití GPU instance pro trénink
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Nahraďte polohou vašeho výpočetního clusteru
    ```

> [!TIP]
>
> **Pokyny pro doladění s minimální datovou sadou pomocí CPU**
>
> Pokud chcete použít CPU pro doladění, tento přístup je ideální pro uživatele s výhodnými předplatnými (například Visual Studio Enterprise Subscription) nebo pro rychlé otestování procesu doladění a nasazení.
>
> 1. Otevřete soubor *setup_ml*.
> 1. Nahraďte `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` a `DOCKER_IMAGE_NAME` podle následujícího. Pokud nemáte přístup k *Standard_E16s_v3*, můžete použít ekvivalentní CPU instanci nebo požádat o nový kvót.
> 1. Nahraďte `LOCATION` svými konkrétními údaji.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Zadejte následující příkaz pro spuštění skriptu *setup_ml.py* a zahájení procesu doladění v Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. V tomto cvičení jste úspěšně doladili model Phi-3 pomocí Azure Machine Learning. Spuštěním skriptu *setup_ml.py* jste nastavili prostředí Azure Machine Learning a inicializovali proces doladění definovaný v souboru *fine_tune.py*. Upozorňujeme, že proces doladění může trvat delší dobu. Po zadání příkazu `python setup_ml.py` musíte počkat na dokončení procesu. Stav úlohy doladění můžete sledovat pomocí odkazu zobrazeného v terminálu na portál Azure Machine Learning.

    ![Zobrazit úlohu doladění.](../../../../../../translated_images/cs/02-02-see-finetuning-job.59393bc3b143871e.webp)

### Nasazení doladěného modelu

Pro integraci doladěného modelu Phi-3 s Prompt Flow je potřeba model nasadit, aby byl dostupný pro vyhodnocení v reálném čase. Tento proces zahrnuje registraci modelu, vytvoření online koncového bodu a nasazení modelu.

#### Nastavení názvu modelu, jména koncového bodu a názvu nasazení

1. Otevřete soubor *config.py*.

1. Nahraďte `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` požadovaným názvem vašeho modelu.

1. Nahraďte `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` požadovaným názvem vašeho koncového bodu.

1. Nahraďte `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` požadovaným názvem vašeho nasazení.

#### Přidání kódu do souboru *deploy_model.py*

Spuštění souboru *deploy_model.py* automatizuje celý proces nasazení. Registrová model, vytvoří koncový bod a nasadí model na základě nastavení uvedených v souboru *config.py*, který zahrnuje název modelu, název koncového bodu a název nasazení.

1. Otevřete soubor *deploy_model.py* ve Visual Studio Code.

1. Přidejte do souboru *deploy_model.py* následující kód.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Importy konfigurace
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

    # Konstanty
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Nastavení logování
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
            # Získat aktuální detaily koncového bodu
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Zalogovat aktuální rozdělení provozu pro ladění
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Nastavit rozdělení provozu pro nasazení
            endpoint.traffic = {deployment_name: 100}
            
            # Aktualizovat koncový bod s novým rozdělením provozu
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Zalogovat aktualizované rozdělení provozu pro ladění
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Zalogovat jakékoli chyby, ke kterým během procesu dojde
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

1. Proveďte následující kroky k získání hodnoty `JOB_NAME`:

    - Přejděte do zdroje Azure Machine Learning, který jste vytvořili.
    - Vyberte **Studio web URL** pro otevření pracovního prostoru Azure Machine Learning.
    - Vyberte **Jobs** z levého postranního panelu.
    - Vyberte experiment pro doladění, například *finetunephi*.
    - Vyberte vytvořenou úlohu.
- Zkopírujte a vložte název své práce do `JOB_NAME = "your-job-name"` v souboru *deploy_model.py*.

1. Nahraďte `COMPUTE_INSTANCE_TYPE` svými konkrétními údaji.

1. Zadejte následující příkaz pro spuštění skriptu *deploy_model.py* a zahájení nasazovacího procesu v Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Aby nedošlo k dalším poplatkům na vašem účtu, ujistěte se, že odstraníte vytvořený endpoint v pracovním prostoru Azure Machine Learning.
>

#### Zkontrolujte stav nasazení v pracovním prostoru Azure Machine Learning

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Přejděte do pracovního prostoru Azure Machine Learning, který jste vytvořili.

1. Vyberte **Studio web URL** pro otevření pracovního prostoru Azure Machine Learning.

1. Vyberte **Endpoints** z levé boční záložky.

    ![Vyberte endpoints.](../../../../../../translated_images/cs/02-03-select-endpoints.c3136326510baff1.webp)

2. Vyberte endpoint, který jste vytvořili.

    ![Vyberte endpoint, který jste vytvořili.](../../../../../../translated_images/cs/02-04-select-endpoint-created.0363e7dca51dabb4.webp)

3. Na této stránce můžete spravovat endpointy vytvořené během nasazovacího procesu.

## Scénář 3: Integrace s Prompt flow a chatování s vaším vlastním modelem

### Integrace vlastního modelu Phi-3 s Prompt flow

Po úspěšném nasazení vašeho jemně doladěného modelu jej nyní můžete integrovat s Prompt flow a využívat váš model v aplikacích v reálném čase, což umožňuje různé interaktivní úkoly s vaším vlastním modelem Phi-3.

#### Nastavení klíče API a URI endpointu jemně doladěného modelu Phi-3

1. Přejděte do pracovního prostoru Azure Machine Learning, který jste vytvořili.
1. Vyberte **Endpoints** z levé boční záložky.
1. Vyberte endpoint, který jste vytvořili.
1. Vyberte **Consume** v navigační nabídce.
1. Zkopírujte a vložte svůj **REST endpoint** do souboru *config.py*, nahraďte `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` vaším **REST endpointem**.
1. Zkopírujte a vložte svůj **Primární klíč** do souboru *config.py*, nahraďte `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` vaším **Primárním klíčem**.

    ![Zkopírujte klíč API a URI endpointu.](../../../../../../translated_images/cs/02-05-copy-apikey-endpoint.88b5a92e6462c53b.webp)

#### Přidání kódu do souboru *flow.dag.yml*

1. Otevřete soubor *flow.dag.yml* ve Visual Studio Code.

1. Přidejte následující kód do *flow.dag.yml*.

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

#### Přidání kódu do souboru *integrate_with_promptflow.py*

1. Otevřete soubor *integrate_with_promptflow.py* ve Visual Studio Code.

1. Přidejte následující kód do *integrate_with_promptflow.py*.

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

    # Nastavení logování
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

### Chatování s vaším vlastním modelem

1. Zadejte následující příkaz pro spuštění skriptu *deploy_model.py* a zahájení nasazovacího procesu v Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Zde je příklad výsledků: Nyní můžete chatovat s vaším vlastním modelem Phi-3. Doporučuje se pokládat otázky založené na datech použitých pro jemné doladění.

    ![Příklad prompt flow.](../../../../../../translated_images/cs/02-06-promptflow-example.89384abaf3ad71f6.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->