# Doladění a integrace vlastních modelů Phi-3 s Prompt flow v Microsoft Foundry

Tento ukázkový příklad end-to-end (E2E) vychází z návodu "[Doladění a integrace vlastních modelů Phi-3 s Prompt flow v Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Představuje procesy doladění, nasazení a integrace vlastních modelů Phi-3 s Prompt flow v Microsoft Foundry.
Na rozdíl od E2E ukázkového příkladu "[Doladění a integrace vlastních modelů Phi-3 s Prompt flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", který zahrnoval spouštění kódu lokálně, se tento tutoriál plně zaměřuje na doladění a integraci vašeho modelu v rámci Azure AI / ML Studia.

## Přehled

V tomto E2E příkladu se naučíte, jak doladit model Phi-3 a integrovat ho s Prompt flow v Microsoft Foundry. S využitím Azure AI / ML Studia vytvoříte pracovní postup pro nasazení a využití vlastních AI modelů. Tento E2E příklad je rozdělen do tří scénářů:

**Scénář 1: Nastavení Azure zdrojů a příprava na doladění**

**Scénář 2: Doladění modelu Phi-3 a nasazení v Azure Machine Learning Studiu**

**Scénář 3: Integrace s Prompt flow a chatování s vlastním modelem v Microsoft Foundry**

Zde je přehled tohoto E2E příkladu.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/cs/00-01-architecture.198ba0f1ae6d841a.webp)

### Obsah

1. **[Scénář 1: Nastavení Azure zdrojů a příprava na doladění](#scénář-1-nastavení-azure-zdrojů-a-příprava-na-doladění)**
    - [Vytvoření Azure Machine Learning Workspace](#vytvoření-azure-machine-learning-workspace)
    - [Žádost o GPU kvóty v Azure Subscription](#žádost-o-gpu-kvóty-v-azure-subscription)
    - [Přidání role assignment](#přidání-role-assignment)
    - [Nastavení projektu](#nastavení-projektu)
    - [Příprava datasetu pro doladění](#připravte-dataset-pro-doladění)

1. **[Scénář 2: Doladění modelu Phi-3 a nasazení v Azure Machine Learning Studiu](#scénář-2-doladění-modelu-phi-3-a-nasazení-v-azure-machine-learning-studio)**
    - [Doladění modelu Phi-3](#doladění-modelu-phi-3)
    - [Nasazení doladěného modelu Phi-3](#nasazení-doladěného-modelu-phi-3)

1. **[Scénář 3: Integrace s Prompt flow a chatování s vlastním modelem v Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrace vlastního modelu Phi-3 s Prompt flow](#integrace-vlastního-modelu-phi-3-s-prompt-flow)
    - [Chatování s vlastním modelem Phi-3](#chatovat-se-svým-vlastním-modelem-phi-3)

## Scénář 1: Nastavení Azure zdrojů a příprava na doladění

### Vytvoření Azure Machine Learning Workspace

1. Zadejte *azure machine learning* do **vyhledávacího pole** v horní části portálu a vyberte **Azure Machine Learning** z nabízených možností.

    ![Type azure machine learning.](../../../../../../translated_images/cs/01-01-type-azml.acae6c5455e67b4b.webp)

2. Vyberte **+ Vytvořit** z navigačního menu.

3. Vyberte **Nový workspace** z navigačního menu.

    ![Select new workspace.](../../../../../../translated_images/cs/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Proveďte následující kroky:

    - Vyberte svou Azure **Subscription**.
    - Vyberte **Resource group** k použití (vytvořte novou, pokud je potřeba).
    - Zadejte **Název Workspace**. Musí být jedinečný.
    - Vyberte **Region**, který chcete použít.
    - Vyberte **Storage account** k použití (vytvořte nový, pokud je potřeba).
    - Vyberte **Key vault** k použití (vytvořte nový, pokud je potřeba).
    - Vyberte **Application insights** k použití (vytvořte nové, pokud je potřeba).
    - Vyberte **Container registry** k použití (vytvořte nový, pokud je potřeba).

    ![Fill azure machine learning.](../../../../../../translated_images/cs/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Vyberte **Zkontrolovat + vytvořit**.

6. Vyberte **Vytvořit**.

### Žádost o GPU kvóty v Azure Subscription

V tomto tutoriálu se naučíte, jak doladit a nasadit model Phi-3 s využitím GPU. Pro doladění použijete GPU *Standard_NC24ads_A100_v4*, který vyžaduje žádost o kvótu. Pro nasazení použijete GPU *Standard_NC6s_v3*, který rovněž vyžaduje žádost o kvótu.

> [!NOTE]
>
> Pouze předplatné typu Pay-As-You-Go (standardní typ předplatného) je způsobilé pro přidělení GPU; benefitní předplatné momentálně není podporováno.
>

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pro žádost o kvótu *Standard NCADSA100v4 Family* proveďte následující:

    - Vyberte **Kvóty** z levého panelu.
    - Vyberte **Rodinu virtuálních strojů**, kterou chcete použít. Například vyberte **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, která obsahuje GPU *Standard_NC24ads_A100_v4*.
    - Vyberte **Požádat o kvótu** z navigačního menu.

        ![Request quota.](../../../../../../translated_images/cs/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na stránce Žádost o kvótu zadejte **Nový limit jader**, které chcete použít. Například 24.
    - Na stránce Žádost o kvótu vyberte **Odeslat** pro podání žádosti o kvótu GPU.

1. Pro žádost o kvótu *Standard NCSv3 Family* proveďte následující:

    - Vyberte **Kvóty** z levého panelu.
    - Vyberte **Rodinu virtuálních strojů**, kterou chcete použít. Například vyberte **Standard NCSv3 Family Cluster Dedicated vCPUs**, která obsahuje GPU *Standard_NC6s_v3*.
    - Vyberte **Požádat o kvótu** z navigačního menu.
    - Na stránce Žádost o kvótu zadejte **Nový limit jader**, které chcete použít. Například 24.
    - Na stránce Žádost o kvótu vyberte **Odeslat** pro podání žádosti o kvótu GPU.

### Přidání role assignment

Pro doladění a nasazení svých modelů je nutné nejdříve vytvořit User Assigned Managed Identity (UAI) a přiřadit jí odpovídající oprávnění. Tuto UAI budete používat pro ověřování při nasazení.

#### Vytvoření User Assigned Managed Identity (UAI)

1. Zadejte *managed identities* do **vyhledávacího pole** v horní části portálu a vyberte **Managed Identities** z nabízených možností.

    ![Type managed identities.](../../../../../../translated_images/cs/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Vyberte **+ Vytvořit**.

    ![Select create.](../../../../../../translated_images/cs/03-02-select-create.92bf8989a5cd98f2.webp)

1. Proveďte následující kroky:

    - Vyberte svou Azure **Subscription**.
    - Vyberte **Resource group** k použití (vytvořte novou, pokud je potřeba).
    - Vyberte **Region**, který chcete použít.
    - Zadejte **Název**. Musí být jedinečný.

    ![Select create.](../../../../../../translated_images/cs/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Vyberte **Zkontrolovat + vytvořit**.

1. Vyberte **+ Vytvořit**.

#### Přidání role Contributor Managed Identity

1. Přejděte k prostředku Managed Identity, který jste vytvořili.

1. Vyberte **Azure role assignments** z levého panelu.

1. Vyberte **+ Přidat přiřazení role** z navigačního menu.

1. Na stránce Přidání role proveďte následující:
    - Vyberte **Rozsah** jako **Resource group**.
    - Vyberte svou Azure **Subscription**.
    - Vyberte **Resource group** k použití.
    - Vyberte **Role** jako **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/cs/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Vyberte **Uložit**.

#### Přidání role Storage Blob Data Reader Managed Identity

1. Zadejte *storage accounts* do **vyhledávacího pole** v horní části portálu a vyberte **Storage accounts** z nabízených možností.

    ![Type storage accounts.](../../../../../../translated_images/cs/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Vyberte storage účet spojený s Azure Machine Learning workspace, který jste vytvořili. Například *finetunephistorage*.

1. Pro navigaci na stránku Přidání role proveďte následující:

    - Přejděte k Azure Storage účtu, který jste vytvořili.
    - Vyberte **Řízení přístupu (IAM)** z levého panelu.
    - Vyberte **+ Přidat** z navigačního menu.
    - Vyberte **Přidat přiřazení role** z navigačního menu.

    ![Add role.](../../../../../../translated_images/cs/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na stránce Přidání role proveďte následující:

    - Na stránce Role zadejte *Storage Blob Data Reader* do **vyhledávacího pole** a vyberte **Storage Blob Data Reader** z nabízených možností.
    - Na stránce Role vyberte **Další**.
    - Na stránce Členové vyberte **Přiřadit přístup k** **Managed identity**.
    - Na stránce Členové vyberte **+ Vybrat členy**.
    - Na stránce Výběr spravovaných identit zvolte svou Azure **Subscription**.
    - Na stránce Výběr spravovaných identit vyberte **Managed identity** jako **Manage Identity**.
    - Na stránce Výběr spravovaných identit vyberte Manage Identity, kterou jste vytvořili. Například *finetunephi-managedidentity*.
    - Na stránce Výběr spravovaných identit vyberte **Vybrat**.

    ![Select managed identity.](../../../../../../translated_images/cs/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Vyberte **Zkontrolovat + přiřadit**.

#### Přidání role AcrPull Managed Identity

1. Zadejte *container registries* do **vyhledávacího pole** v horní části portálu a vyberte **Container registries** z nabízených možností.

    ![Type container registries.](../../../../../../translated_images/cs/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Vyberte container registry spojený s Azure Machine Learning workspace. Například *finetunephicontainerregistry*

1. Pro navigaci na stránku Přidání role proveďte následující:

    - Vyberte **Řízení přístupu (IAM)** z levého panelu.
    - Vyberte **+ Přidat** z navigačního menu.
    - Vyberte **Přidat přiřazení role** z navigačního menu.

1. Na stránce Přidání role proveďte následující:

    - Na stránce Role zadejte *AcrPull* do **vyhledávacího pole** a vyberte **AcrPull** z nabízených možností.
    - Na stránce Role vyberte **Další**.
    - Na stránce Členové vyberte **Přiřadit přístup k** **Managed identity**.
    - Na stránce Členové vyberte **+ Vybrat členy**.
    - Na stránce Výběr spravovaných identit zvolte svou Azure **Subscription**.
    - Na stránce Výběr spravovaných identit vyberte **Managed identity** jako **Manage Identity**.
    - Na stránce Výběr spravovaných identit vyberte Manage Identity, kterou jste vytvořili. Například *finetunephi-managedidentity*.
    - Na stránce Výběr spravovaných identit vyberte **Vybrat**.
    - Vyberte **Zkontrolovat + přiřadit**.

### Nastavení projektu

Pro stažení datasetů potřebných k doladění si nastavíte místní prostředí.

V tomto cvičení budete

- Vytvářet složku pro práci uvnitř ní.
- Vytvoříte virtuální prostředí.
- Nainstalujete požadované balíčky.
- Vytvoříte soubor *download_dataset.py* pro stažení datasetu.

#### Vytvoření složky pro práci uvnitř ní

1. Otevřete terminál a zadejte následující příkaz pro vytvoření složky nazvané *finetune-phi* v implicitní cestě.

    ```console
    mkdir finetune-phi
    ```

2. Zadejte následující příkaz v terminálu pro přechod do složky *finetune-phi*, kterou jste vytvořili.

    ```console
    cd finetune-phi
    ```

#### Vytvoření virtuálního prostředí

1. Zadejte následující příkaz v terminálu pro vytvoření virtuálního prostředí pojmenovaného *.venv*.
    ```console
    python -m venv .venv
    ```

2. Do terminálu zadejte následující příkaz pro aktivaci virtuálního prostředí.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Pokud to fungovalo, měli byste vidět *(.venv)* před příkazovým řádkem.

#### Nainstalujte požadované balíčky

1. Do terminálu zadejte následující příkazy pro instalaci požadovaných balíčků.

    ```console
    pip install datasets==2.19.1
    ```

#### Vytvořte `download_dataset.py`

> [!NOTE]
> Kompletní struktura složek:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otevřete **Visual Studio Code**.

1. V nabídce vyberte **Soubor**.

1. Vyberte **Otevřít složku**.

1. Vyberte složku *finetune-phi*, kterou jste vytvořili, nacházející se na *C:\Users\yourUserName\finetune-phi*.

    ![Vyberte složku, kterou jste vytvořili.](../../../../../../translated_images/cs/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem a vyberte **Nový soubor**, vytvořte nový soubor pojmenovaný *download_dataset.py*.

    ![Vytvořte nový soubor.](../../../../../../translated_images/cs/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Připravte dataset pro doladění

V tomto cvičení spustíte soubor *download_dataset.py*, abyste si stáhli datové sady *ultrachat_200k* do lokálního prostředí. Poté tyto datové sady použijete pro doladění modelu Phi-3 v Azure Machine Learning.

V tomto cvičení:

- Přidáte kód do souboru *download_dataset.py* pro stažení datových sad.
- Spustíte soubor *download_dataset.py* pro stažení dat do lokálního prostředí.

#### Stáhněte svůj dataset pomocí *download_dataset.py*

1. Otevřete soubor *download_dataset.py* ve Visual Studio Code.

1. Přidejte do souboru *download_dataset.py* následující kód.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Načtěte dataset se specifikovaným názvem, konfigurací a poměrem rozdělení
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Rozdělte dataset na trénovací a testovací sady (80 % trénink, 20 % test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Vytvořte adresář, pokud neexistuje
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Otevřete soubor v režimu zápisu
        with open(filepath, 'w', encoding='utf-8') as f:
            # Procházejte každý záznam v datasetu
            for record in dataset:
                # Uložte záznam jako JSON objekt a zapište ho do souboru
                json.dump(record, f)
                # Zapište znak nového řádku pro oddělení záznamů
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Načtěte a rozdělte dataset ULTRACHAT_200k se specifickou konfigurací a poměrem rozdělení
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrahujte trénovací a testovací datasety ze splitu
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Uložte trénovací dataset do JSONL souboru
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Uložte testovací dataset do samostatného JSONL souboru
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Do terminálu zadejte následující příkaz pro spuštění skriptu a stažení datasetu do lokálního prostředí.

    ```console
    python download_dataset.py
    ```

1. Ověřte, zda byly datové sady úspěšně uloženy do vaší lokální složky *finetune-phi/data*.

> [!NOTE]
>
> #### Poznámka o velikosti datasetu a čase doladění
>
> V tomto tutoriálu používáte pouze 1% datasetu (`split='train[:1%]'`). To výrazně snižuje množství dat, což zrychluje jak nahrávání, tak proces doladění. Pro nalezení správné rovnováhy mezi dobou tréninku a výkonem modelu můžete procento upravit. Použití menší podmnožiny datasetu zkracuje dobu potřebnou pro doladění, což činí proces lépe zvládnutelným v rámci tutoriálu.

## Scénář 2: Doladění modelu Phi-3 a nasazení v Azure Machine Learning Studio

### Doladění modelu Phi-3

V tomto cvičení doladíte model Phi-3 v Azure Machine Learning Studio.

V tomto cvičení:

- Vytvoříte výpočetní cluster pro doladění.
- Doladíte model Phi-3 v Azure Machine Learning Studio.

#### Vytvořte výpočetní cluster pro doladění

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. V levém panelu vyberte **Výpočet**.

1. V navigačním menu vyberte **Výpočetní clustery**.

1. Klikněte na **+ Nový**.

    ![Vyberte výpočet.](../../../../../../translated_images/cs/06-01-select-compute.a29cff290b480252.webp)

1. Proveďte následující kroky:

    - Vyberte **Region**, který chcete použít.
    - Vyberte **Úroveň virtuálního stroje** na **Dedikovaný**.
    - Vyberte **Typ virtuálního stroje** na **GPU**.
    - Ve filtru **Velikost virtuálního stroje** vyberte **Vybrat ze všech možností**.
    - Vyberte velikost virtuálního stroje **Standard_NC24ads_A100_v4**.

    ![Vytvoření clusteru.](../../../../../../translated_images/cs/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Klikněte na **Další**.

1. Proveďte následující kroky:

    - Zadejte **Název výpočetního prostředí**. Musí být jedinečný.
    - Nastavte **Minimální počet uzlů** na **0**.
    - Nastavte **Maximální počet uzlů** na **1**.
    - Nastavte hodnotu **Nečinné sekundy před snížením kapacity** na **120**.

    ![Vytvoření clusteru.](../../../../../../translated_images/cs/06-03-create-cluster.4a54ba20914f3662.webp)

1. Klikněte na **Vytvořit**.

#### Doladění modelu Phi-3

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte pracovní prostor Azure Machine Learning, který jste vytvořili.

    ![Vyberte pracovní prostor, který jste vytvořili.](../../../../../../translated_images/cs/06-04-select-workspace.a92934ac04f4f181.webp)

1. Proveďte následující kroky:

    - V levém panelu vyberte **Katalog modelů**.
    - Do **vyhledávacího pole** zadejte *phi-3-mini-4k* a vyberte **Phi-3-mini-4k-instruct** z nabídnutých možností.

    ![Zadejte phi-3-mini-4k.](../../../../../../translated_images/cs/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. V navigačním menu vyberte **Doladit**.

    ![Vyberte doladění.](../../../../../../translated_images/cs/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Proveďte následující kroky:

    - Nastavte **Vybrat typ úlohy** na **Chat completions**.
    - Klikněte na **+ Vybrat data** pro nahrání **tréninkových dat**.
    - Nastavte typ nahrání validačních dat na **Poskytnout odlišná validační data**.
    - Klikněte na **+ Vybrat data** pro nahrání **validačních dat**.

    ![Vyplňte stránku doladění.](../../../../../../translated_images/cs/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Můžete vybrat **Pokročilá nastavení** pro přizpůsobení konfigurací, jako jsou **learning_rate** a **lr_scheduler_type**, aby bylo doladění optimalizováno podle vašich potřeb.

1. Klikněte na **Dokončit**.

1. V tomto cvičení jste úspěšně doladili model Phi-3 pomocí Azure Machine Learning. Upozorňujeme, že proces doladění může trvat značný čas. Po spuštění úlohy doladění je potřeba počkat na její dokončení. Stav doladění můžete sledovat na záložce Úlohy v levém panelu vašeho pracovního prostoru Azure Machine Learning. V dalším díle nasadíte doladěný model a integrujete jej s Prompt flow.

    ![Zobrazit úlohu doladění.](../../../../../../translated_images/cs/06-08-output.2bd32e59930672b1.webp)

### Nasazení doladěného modelu Phi-3

Pro integraci doladěného modelu Phi-3 s Prompt flow je potřeba model nasadit tak, aby byl dostupný pro inference v reálném čase. Tento proces zahrnuje registraci modelu, vytvoření online endpointu a nasazení modelu.

V tomto cvičení:

- Zaregistrujete doladěný model v pracovním prostoru Azure Machine Learning.
- Vytvoříte online endpoint.
- Nasadíte registrovaný doladěný model Phi-3.

#### Registrace doladěného modelu

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte pracovní prostor Azure Machine Learning, který jste vytvořili.

    ![Vyberte pracovní prostor, který jste vytvořili.](../../../../../../translated_images/cs/06-04-select-workspace.a92934ac04f4f181.webp)

1. V levém panelu vyberte **Modely**.
1. Klikněte na **+ Registrovat**.
1. Vyberte **Z výstupu úlohy**.

    ![Registrace modelu.](../../../../../../translated_images/cs/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Vyberte úlohu, kterou jste vytvořili.

    ![Vyberte úlohu.](../../../../../../translated_images/cs/07-02-select-job.3e2e1144cd6cd093.webp)

1. Klikněte na **Další**.

1. Nastavte **Typ modelu** na **MLflow**.

1. Ujistěte se, že je vybrán **Výstup úlohy**; toto by mělo být vybráno automaticky.

    ![Vyberte výstup.](../../../../../../translated_images/cs/07-03-select-output.4cf1a0e645baea1f.webp)

2. Klikněte na **Další**.

3. Klikněte na **Registrovat**.

    ![Klikněte na registrovat.](../../../../../../translated_images/cs/07-04-register.fd82a3b293060bc7.webp)

4. Registrovaný model můžete zobrazit v menu **Modely** v levém panelu.

    ![Registrovaný model.](../../../../../../translated_images/cs/07-05-registered-model.7db9775f58dfd591.webp)

#### Nasazení doladěného modelu

1. Přejděte do pracovního prostoru Azure Machine Learning, který jste vytvořili.

1. V levém panelu vyberte **Endpointy**.

1. V navigačním menu vyberte **Endpointy v reálném čase**.

    ![Vytvoření endpointu.](../../../../../../translated_images/cs/07-06-create-endpoint.1ba865c606551f09.webp)

1. Klikněte na **Vytvořit**.

1. Vyberte registrovaný model, který jste vytvořili.

    ![Vyberte registrovaný model.](../../../../../../translated_images/cs/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Klikněte na **Vybrat**.

1. Proveďte následující kroky:

    - Vyberte **Virtuální stroj** na *Standard_NC6s_v3*.
    - Vyberte počet instancí, které chcete použít. Například *1*.
    - Nastavte **Endpoint** na **Nový** pro vytvoření endpointu.
    - Zadejte **Název endpointu**. Musí být jedinečný.
    - Zadejte **Název nasazení**. Musí být jedinečný.

    ![Vyplňte nastavení nasazení.](../../../../../../translated_images/cs/07-08-deployment-setting.43ddc4209e673784.webp)

1. Klikněte na **Nasadit**.

> [!WARNING]
> Aby nedošlo k dodatkovým poplatkům na vašem účtu, nezapomeňte smazat vytvořený endpoint v pracovním prostoru Azure Machine Learning.
>

#### Kontrola stavu nasazení v Azure Machine Learning Workspace

1. Přejděte do pracovního prostoru Azure Machine Learning, který jste vytvořili.

1. V levém panelu vyberte **Endpointy**.

1. Vyberte endpoint, který jste vytvořili.

    ![Vyberte endpointy](../../../../../../translated_images/cs/07-09-check-deployment.325d18cae8475ef4.webp)

1. Na této stránce můžete spravovat endpointy během procesu nasazení.

> [!NOTE]
> Po dokončení nasazení se ujistěte, že **Živý provoz** je nastaven na **100%**. Pokud ne, klikněte na **Aktualizovat provoz** pro nastavení správného provozu. Model nelze testovat, pokud je provoz nastaven na 0%.
>
> ![Nastavení provozu.](../../../../../../translated_images/cs/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scénář 3: Integrace s Prompt flow a chatování s vlastním modelem v Microsoft Foundry

### Integrace vlastního modelu Phi-3 s Prompt flow

Po úspěšném nasazení doladěného modelu jej nyní můžete integrovat s Prompt Flow, abyste mohli svůj model používat v reálných aplikacích a umožnit různorodé interaktivní úkoly s vaším vlastním modelem Phi-3.

V tomto cvičení:

- Vytvoříte Microsoft Foundry Hub.
- Vytvoříte projekt v Microsoft Foundry.
- Vytvoříte Prompt flow.
- Přidáte vlastní připojení k doladěnému modelu Phi-3.
- Nastavíte Prompt flow pro chatování s vlastním modelem Phi-3.

> [!NOTE]
> S Promptflow se můžete integrovat také pomocí Azure ML Studio. Stejný integrační proces lze použít i pro Azure ML Studio.

#### Vytvoření Microsoft Foundry Hub

Nejprve musíte vytvořit Hub, než budete moci vytvořit Projekt. Hub funguje jako skupina zdrojů, která umožňuje organizovat a spravovat více projektů v rámci Microsoft Foundry.
1. Navštivte [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. V levé postranní záložce vyberte **Všechny uzly**.

1. V navigační nabídce vyberte **+ Nový uzel**.

    ![Vytvořit uzel.](../../../../../../translated_images/cs/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Proveďte následující úkony:

    - Zadejte **Název uzlu**. Musí to být jedinečná hodnota.
    - Vyberte svůj předplatný plán Azure (**Subscription**).
    - Vyberte **Skupinu prostředků** k použití (vytvořte novou, pokud je potřeba).
    - Vyberte **Umístění**, které chcete použít.
    - Vyberte **Připojit Azure AI služby**, které chcete použít (vytvořte nové, pokud je potřeba).
    - Vyberte **Připojit Azure AI Search** a zvolte **Přeskočit připojení**.

    ![Vyplnit uzel.](../../../../../../translated_images/cs/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Vyberte **Další**.

#### Vytvořit projekt Microsoft Foundry

1. V uzlu, který jste vytvořili, vyberte v levé postranní záložce **Všechny projekty**.

1. V navigační nabídce vyberte **+ Nový projekt**.

    ![Vybrat nový projekt.](../../../../../../translated_images/cs/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Zadejte **Název projektu**. Musí to být jedinečná hodnota.

    ![Vytvořit projekt.](../../../../../../translated_images/cs/08-05-create-project.4d97f0372f03375a.webp)

1. Vyberte **Vytvořit projekt**.

#### Přidat vlastní připojení pro jemně laděný model Phi-3

Pro integraci vašeho vlastního modelu Phi-3 s Prompt flow je nutné uložit koncový bod modelu a klíč do vlastního připojení. Toto nastavení zajistí přístup k vašemu vlastnímu modelu Phi-3 v Prompt flow.

#### Nastavit api klíč a URI koncového bodu jemně laděného modelu Phi-3

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Přejděte do pracovního prostoru Azure Machine learning, který jste vytvořili.

1. V levé postranní záložce vyberte **Koncové body**.

    ![Vybrat koncové body.](../../../../../../translated_images/cs/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Vyberte koncový bod, který jste vytvořili.

    ![Vybrat vytvořený koncový bod.](../../../../../../translated_images/cs/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. V navigační nabídce vyberte **Použít**.

1. Zkopírujte svůj **REST koncový bod** a **Primární klíč**.

    ![Zkopírovat api klíč a URI koncového bodu.](../../../../../../translated_images/cs/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Přidat vlastní připojení

1. Navštivte [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Přejděte do projektu Microsoft Foundry, který jste vytvořili.

1. V projektu, který jste vytvořili, vyberte v levé postranní záložce **Nastavení**.

1. Vyberte **+ Nové připojení**.

    ![Vybrat nové připojení.](../../../../../../translated_images/cs/08-09-select-new-connection.02eb45deadc401fc.webp)

1. V navigační nabídce vyberte **Vlastní klíče**.

    ![Vybrat vlastní klíče.](../../../../../../translated_images/cs/08-10-select-custom-keys.856f6b2966460551.webp)

1. Proveďte následující úkony:

    - Vyberte **+ Přidat dvojice klíč-hodnota**.
    - Pro název klíče zadejte **endpoint** a vložte koncový bod, který jste zkopírovali z Azure ML Studio, do pole hodnoty.
    - Opět vyberte **+ Přidat dvojice klíč-hodnota**.
    - Pro název klíče zadejte **key** a vložte klíč, který jste zkopírovali z Azure ML Studio, do pole hodnoty.
    - Po přidání klíčů vyberte **je tajný** (is secret), aby klíč nebyl viditelný.

    ![Přidat připojení.](../../../../../../translated_images/cs/08-11-add-connection.785486badb4d2d26.webp)

1. Vyberte **Přidat připojení**.

#### Vytvořit Prompt flow

Přidali jste vlastní připojení v Microsoft Foundry. Nyní vytvoříme Prompt flow pomocí následujících kroků. Poté toto Prompt flow připojíte k vlastnímu připojení, abyste mohli používat jemně laděný model uvnitř Prompt flow.

1. Přejděte do projektu Microsoft Foundry, který jste vytvořili.

1. V levé postranní záložce vyberte **Prompt flow**.

1. V navigační nabídce vyberte **+ Vytvořit**.

    ![Vybrat Promptflow.](../../../../../../translated_images/cs/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. V navigační nabídce vyberte **Chat flow**.

    ![Vybrat chat flow.](../../../../../../translated_images/cs/08-13-select-flow-type.2ec689b22da32591.webp)

1. Zadejte **Název složky**, kterou chcete použít.

    ![Zadat název.](../../../../../../translated_images/cs/08-14-enter-name.ff9520fefd89f40d.webp)

2. Vyberte **Vytvořit**.

#### Nastavit Prompt flow pro chat s vaším vlastním modelem Phi-3

Musíte integrovat jemně laděný model Phi-3 do Prompt flow. Nicméně stávající Prompt flow není pro tento účel navržený. Proto musíte Prompt flow přepracovat, aby bylo možné integrovat vlastní model.

1. V Prompt flow proveďte následující kroky pro přestavbu existujícího toku:

    - Vyberte **Režim surového souboru**.
    - Odstraňte veškerý existující kód v souboru *flow.dag.yml*.
    - Přidejte následující kód do souboru *flow.dag.yml*.

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

    - Vyberte **Uložit**.

    ![Vybrat režim surového souboru.](../../../../../../translated_images/cs/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Přidejte následující kód do souboru *integrate_with_promptflow.py*, aby bylo možné použít vlastní model Phi-3 v Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Nastavení protokolování
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

        # "connection" je název vlastní konekce, "endpoint", "key" jsou klíče ve vlastní konekci
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
            
            # Zaznamenejte celou odpověď ve formátu JSON
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

    ![Vložit kód Prompt flow.](../../../../../../translated_images/cs/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Pro podrobnější informace o používání Prompt flow v Microsoft Foundry můžete navštívit [Prompt flow v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chatovací vstup**, **Chatovací výstup** pro povolení chatu s vaším modelem.

    ![Vstup Výstup.](../../../../../../translated_images/cs/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Nyní jste připraveni chatovat se svým vlastním modelem Phi-3. V následujícím cvičení se naučíte, jak spustit Prompt flow a používat jej ke komunikaci s vaším jemně laděným modelem Phi-3.

> [!NOTE]
>
> Přestavěný tok by měl vypadat jako na obrázku níže:
>
> ![Příklad toku.](../../../../../../translated_images/cs/08-18-graph-example.d6457533952e690c.webp)
>

### Chatovat se svým vlastním modelem Phi-3

Nyní, když jste jemně doladili a integrovali svůj vlastní model Phi-3 s Prompt flow, jste připraveni s ním začít interagovat. Toto cvičení vás provede nastavením a zahájením chatu s modelem pomocí Prompt flow. Následováním těchto kroků budete moci plně využít schopnosti jemně laděného modelu Phi-3 pro různé úkoly a rozhovory.

- Chatovat se svým vlastním modelem Phi-3 pomocí Prompt flow.

#### Spustit Prompt flow

1. Vyberte **Spustit výpočetní relace**, aby se spustil Prompt flow.

    ![Spustit výpočetní relaci.](../../../../../../translated_images/cs/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Vyberte **Ověřit a analyzovat vstup**, aby se obnovily parametry.

    ![Ověřit vstup.](../../../../../../translated_images/cs/09-02-validate-input.317c76ef766361e9.webp)

1. Vyberte **Hodnotu** u **připojení** (connection) k vlastnímu připojení, které jste vytvořili. Například *connection*.

    ![Připojení.](../../../../../../translated_images/cs/09-03-select-connection.99bdddb4b1844023.webp)

#### Chatovat se svým vlastním modelem

1. Vyberte **Chat**.

    ![Vybrat chat.](../../../../../../translated_images/cs/09-04-select-chat.61936dce6612a1e6.webp)

1. Zde je příklad výsledků: Nyní můžete chatovat se svým vlastním modelem Phi-3. Doporučuje se klást otázky založené na datech použitých k jemnému ladění.

    ![Chat s prompt flow.](../../../../../../translated_images/cs/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->