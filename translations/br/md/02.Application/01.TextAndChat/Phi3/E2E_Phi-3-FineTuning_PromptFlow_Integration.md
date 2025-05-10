<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:27:46+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "br"
}
-->
# Fine-tune ha Integrate modéloù Phi-3 personelaet gant Prompt flow

An dibab-se a zo un doare E2E (end-to-end) diazezet war ar gelaouenn "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" eus Microsoft Tech Community. Diskouez a ra ar prosesoù evit fine-tune, deployañ ha integrañ modéloù Phi-3 personelaet gant Prompt flow.

## Disklêriadur

Er sampl E2E-mañ, vo desket penaos fine-tune ar model Phi-3 ha penaos leuniañ anezhañ gant Prompt flow. Gant Azure Machine Learning ha Prompt flow, vo krouet ur raktres evit deployañ ha implijout modéloù AI personelaet. Ar sampl E2E-mañ zo rannet e teir senarioù :

**Senario 1 : Staliañ an aferioù Azure ha prestaat evit fine-tuning**

**Senario 2 : Fine-tune ar model Phi-3 ha deployañ en Azure Machine Learning Studio**

**Senario 3 : Leuniañ gant Prompt flow ha komz gant ho model personelaet**

Setu un diskouezadeg eus ar sampl E2E-mañ.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.br.png)

### Roll an danvez

1. **[Senario 1 : Staliañ an aferioù Azure ha prestaat evit fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Krouiñ ur Workspace Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Goulenn quota GPU er Subscription Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ouzhpennañ ur roll](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Staliañ ar raktres](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Prestaat ar roadennoù evit fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Senario 2 : Fine-tune ar model Phi-3 ha deployañ en Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Staliañ Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tune ar model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deployañ ar model fine-tunet](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Senario 3 : Leuniañ gant Prompt flow ha komz gant ho model personelaet](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Leuniañ ar model Phi-3 personelaet gant Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Komz gant ho model personelaet](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Senario 1 : Staliañ an aferioù Azure ha prestaat evit fine-tuning

### Krouiñ ur Workspace Azure Machine Learning

1. Lakit *azure machine learning* er **bar reizhañ** e penn-kentañ ar bajenn portal ha dibabit **Azure Machine Learning** eus ar palioù a zispleg.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.br.png)

1. Dibabit **+ Create** er mennozh navigadur.

1. Dibabit **New workspace** er mennozh navigadur.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.br.png)

1. Ober ar palioù da-heul :

    - Dibabit ho **Subscription** Azure.
    - Dibabit ar **Resource group** da implijout (krouiñ ur nevez ma n'eus ket anezhañ).
    - Lakit ur **Anv Workspace**. Ret eo bezañ un anv diouzh all.
    - Dibabit ar **Rannvro** a fell deoc'h implijout.
    - Dibabit ar **Storage account** da implijout (krouiñ ur nevez ma n'eus ket anezhañ).
    - Dibabit ar **Key vault** da implijout (krouiñ ur nevez ma n'eus ket anezhañ).
    - Dibabit ar **Application insights** da implijout (krouiñ ur nevez ma n'eus ket anezhañ).
    - Dibabit ar **Container registry** da implijout (krouiñ ur nevez ma n'eus ket anezhañ).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.br.png)

1. Dibabit **Review + Create**.

1. Dibabit **Create**.

### Goulenn quota GPU er Subscription Azure

Er sampl E2E-mañ, implijout a rit an *Standard_NC24ads_A100_v4 GPU* evit fine-tuning, a rank bezañ goulennet evit quota, hag ar *Standard_E4s_v3* CPU evit deployañ, n’eo ket ret goulenn quota evit ar CPU-se.

> [!NOTE]
>
> N'eus an diben da GPU nemet evit abonementoù Pay-As-You-Go (an abonement standard) ; n’int ket bet implijet abonementoù benefis.
>
> Evit an dud a implij abonementoù benefis (da skouer Visual Studio Enterprise Subscription) pe evit ar re a fell dezho klask buan fine-tuning ha deployañ, ar c'hinnig-mañ a ginnig ivez ur mod evit fine-tune gant ur roadenn bihan gant ur CPU. Koulskoude, gwelloc'h eo ar rezultadoù gant GPU ha roadennoù brasoc'h.

1. Mont a ra d'ar bajenn [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Ober ar palioù da-heul evit goulenn quota evit *Standard NCADSA100v4 Family* :

    - Dibabit **Quota** er tabenn e-kichen.
    - Dibabit ar **Virtual machine family** da implijout. Da skouer, dibabit **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, en o zouez ar GPU *Standard_NC24ads_A100_v4*.
    - Dibabit **Request quota** er mennozh navigadur.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.br.png)

    - Er bajenn Request quota, lakaat ar **New cores limit** a fell deoc'h implijout. Da skouer, 24.
    - Er bajenn Request quota, dibabit **Submit** evit goulenn ar quota GPU.

> [!NOTE]
> Gellout a rit dibab ar GPU pe CPU a sikour ac'hanoc'h dre ma lennit an teul [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Ouzhpennañ ur roll

Evit fine-tune ha deployañ ho modéloù, ret eo krouiñ ur User Assigned Managed Identity (UAI) ha reiñ dezhi an tiriadennoù mat. Ar UAI-mañ a vo implijet evit arventenerezh e-pad ar deployañ.

#### Krouiñ User Assigned Managed Identity (UAI)

1. Lakit *managed identities* er **bar reizhañ** e penn-kentañ ar bajenn portal ha dibabit **Managed Identities** eus ar palioù a zispleg.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.br.png)

1. Dibabit **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.br.png)

1. Ober ar palioù da-heul :

    - Dibabit ho **Subscription** Azure.
    - Dibabit ar **Resource group** da implijout (krouiñ ur nevez ma n'eus ket anezhañ).
    - Dibabit ar **Rannvro** a fell deoc'h implijout.
    - Lakit ar **Anv**. Ret eo bezañ un anv diouzh all.

1. Dibabit **Review + create**.

1. Dibabit **+ Create**.

#### Ouzhpennañ roll Contributor d'ar Managed Identity

1. Mont d'ar servij Managed Identity oc'h ober.

1. Dibabit **Azure role assignments** er tabenn e-kichen.

1. Dibabit **+Add role assignment** er mennozh navigadur.

1. Er bajenn Add role assignment, ober ar palioù da-heul :
    - Dibabit ar **Scope** da **Resource group**.
    - Dibabit ho **Subscription** Azure.
    - Dibabit ar **Resource group** da implijout.
    - Dibabit ar **Role** da **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.br.png)

1. Dibabit **Save**.

#### Ouzhpennañ roll Storage Blob Data Reader d'ar Managed Identity

1. Lakit *storage accounts* er **bar reizhañ** e penn-kentañ ar bajenn portal ha dibabit **Storage accounts** eus ar palioù a zispleg.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.br.png)

1. Dibabit ar storage account liammet gant ar Workspace Azure Machine Learning ho peus krouet. Da skouer, *finetunephistorage*.

1. Ober ar palioù da-heul evit mont d'ar bajenn Add role assignment :

    - Mont d'ar storage account Azure ho peus krouet.
    - Dibabit **Access Control (IAM)** er tabenn e-kichen.
    - Dibabit **+ Add** er mennozh navigadur.
    - Dibabit **Add role assignment** er mennozh navigadur.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.br.png)

1. Er bajenn Add role assignment, ober ar palioù da-heul :

    - Er bajenn Role, klask *Storage Blob Data Reader* er **bar reizhañ** ha dibabit **Storage Blob Data Reader** eus ar palioù a zispleg.
    - Er bajenn Role, dibabit **Next**.
    - Er bajenn Members, dibabit **Assign access to** **Managed identity**.
    - Er bajenn Members, dibabit **+ Select members**.
    - Er bajenn Select managed identities, dibabit ho **Subscription** Azure.
    - Er bajenn Select managed identities, dibabit ar **Managed identity** da **Manage Identity**.
    - Er bajenn Select managed identities, dibabit ar Managed Identity ho peus krouet. Da skouer, *finetunephi-managedidentity*.
    - Er bajenn Select managed identities, dibabit **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.br.png)

1. Dibabit **Review + assign**.

#### Ouzhpennañ roll AcrPull d'ar Managed Identity

1. Lakit *container registries* er **bar reizhañ** e penn-kentañ ar bajenn portal ha dibabit **Container registries** eus ar palioù a zispleg.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.br.png)

1. Dibabit ar container registry liammet gant ar Workspace Azure Machine Learning. Da skouer, *finetunephicontainerregistries*

1. Ober ar palioù da-heul evit mont d'ar bajenn Add role assignment :

    - Dibabit **Access Control (IAM)** er tabenn e-kichen.
    - Dibabit **+ Add** er mennozh navigadur.
    - Dibabit **Add role assignment** er mennozh navigadur.

1. Er bajenn Add role assignment, ober ar palioù da-heul :

    - Er bajenn Role, klask *AcrPull* er **bar reizhañ** ha dibabit **AcrPull** eus ar palioù a zispleg.
    - Er bajenn Role, dibabit **Next**.
    - Er bajenn Members, dibabit **Assign access to** **Managed identity**.
    - Er bajenn Members, dibabit **+ Select members**.
    - Er bajenn Select managed identities, dibabit ho **Subscription** Azure.
    - Er bajenn Select managed identities, dibabit ar **Managed identity** da **Manage Identity**.
    - Er bajenn Select managed identities, dibabit ar Managed Identity ho peus krouet. Da skouer, *finetunephi-managedidentity*.
    - Er bajenn Select managed identities, dibabit **Select**.
    - Dibabit **Review + assign**.

### Staliañ ar raktres

Bremañ, krouit ur c'havlec'h da labourat enni ha staliañ ur endro virtual evit sevel ur programm a zegas gantañ an implijerien hag a implij an istorien komz miret er Azure Cosmos DB evit aozañ e respontoù.

#### Krouiñ ur c'havlec'h da labourat enni

1. Digorit ur prenestr terminal ha skriv an aozadur da heul evit krouiñ ur c'havlec'h anvet *finetune-phi* er lec'hioù diazez.

    ```console
    mkdir finetune-phi
    ```

1. Skriv ar gemenn da-heul er prenestr terminal evit mont d'an diavaez eus ar c'havlec'h *finetune-phi* ho peus krouet.

    ```console
    cd finetune-phi
    ```

#### Krouiñ ur endro virtual

1. Skriv ar gemenn da-heul er prenestr terminal evit krouiñ ur endro virtual anvet *.venv*.

    ```console
    python -m venv .venv
    ```

1. Skriv ar gemenn da-heul er prenestr terminal evit aktivañ an endro virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Mar bez ezhomm, e tlefe bezañ gwelet *(.venv)* a-raok ar c'hommand.

#### Staliañ ar paketioù ret

1. Skriv ar gemenn da-heul er prenestr terminal evit staliet ar paketioù ret.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Krouiñ teulioù ar raktres

Er seurt enklask-se, krouit ar c'hod pouezus evit hor raktres. Ar c'hod-se a zo skridoù evit telechargañ ar roadenn, staliañ an endro Azure Machine Learning, fine-tune ar model Phi-3, ha deployañ ar model fine-tunet. Krouit ivez un teul *conda.yml* evit staliañ an endro fine-tuning.

E-barzh ar c'hod-mañ e krouit :

- Ur fichier *download_dataset.py* evit telechargañ ar roadenn.
- Ur fichier *setup_ml.py* evit staliañ an endro Azure Machine Learning.
- Ur fichier *fine_tune.py* er c'havlec'h *finetuning_dir* evit fine-tune ar model Phi-3 gant ar roadenn.
- Ur fichier *conda.yml* evit staliañ an endro fine-tuning.
- Ur fichier *deploy_model.py* evit deployañ ar model fine-tunet.
- Ur fichier *integrate_with_promptflow.py* evit leuniañ ar model fine-tunet ha seveniñ ar model gant Prompt flow.
- Ur fichier flow.dag.yml evit krouiñ seurt raktres evit Prompt flow.
- Ur fichier *config.py* evit lakaat an titouroù Azure.

> [!NOTE]
>
> Roll a-stroll klok :
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

1. Digorit **Visual Studio Code**.

1. Dibabit **File** er mennozh-bar.

1. Dibabit **Open Folder**.

1. Dibabit ar c'havlec'h *finetune-phi* ho peus krouet, lec'hiet war *C:\Users\yourUserName\finetune-phi*.

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.br.png)

1. Er panel kleiz eus Visual Studio Code, klik-droit ha dibabit **New File** evit krouiñ ur fichier nevez anvet *download_dataset.py*.

1. Er panel kleiz eus Visual Studio Code, klik-droit ha dibabit **New File** evit krouiñ ur fichier nevez anvet *setup_ml.py*.

1. Er panel kleiz eus Visual Studio Code, klik-droit ha dibabit **New File** evit krouiñ ur fichier nevez anvet *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.br.png)

1. Er panel kleiz eus Visual Studio Code, klik-droit ha dibabit **New Folder** evit krouiñ ur c'havlec'h nevez anvet *finetuning_dir*.

1. Er c'havlec'h *finetuning_dir*, krouit ur fichier nevez anvet *fine_tune.py*.

#### Krouiñ ha Konfigurañ ar fichier *conda.yml*

1. Er panel kleiz eus Visual Studio Code, klik-droit ha dibabit **New File** evit krouiñ ur fichier nevez anvet *conda.yml*.

1. Ouzhpennañ ar c'hod da-heul er fichier *conda.yml* evit staliañ an endro fine-tuning evit ar model Phi-3.

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

#### Krouiñ ha Konfigurañ ar fichier *config.py*

1. Er panel kleiz eus Visual Studio Code, klik-droit ha dibabit **New File** evit krouiñ ur fichier nevez anvet *config.py*.

1. Ouzhpennañ ar c'hod
![Find subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.br.png)

1. Realize as seguintes tarefas para adicionar o Nome do Azure Workspace:

    - Navegue até o recurso Azure Machine Learning que você criou.
    - Copie e cole o nome da sua conta no arquivo *config.py*.

    ![Find Azure Machine Learning name.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.br.png)

1. Realize as seguintes tarefas para adicionar o Nome do Azure Resource Group:

    - Navegue até o recurso Azure Machine Learning que você criou.
    - Copie e cole o Nome do seu Azure Resource Group no arquivo *config.py*.

    ![Find resource group name.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.br.png)

2. Realize as seguintes tarefas para adicionar o nome do Azure Managed Identity

    - Navegue até o recurso Managed Identities que você criou.
    - Copie e cole o nome do seu Azure Managed Identity no arquivo *config.py*.

    ![Find UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.br.png)

### Prepare o dataset para fine-tuning

Neste exercício, você vai executar o arquivo *download_dataset.py* para baixar os datasets *ULTRACHAT_200k* para seu ambiente local. Depois, você usará esses datasets para fazer o fine-tuning do modelo Phi-3 no Azure Machine Learning.

#### Baixe seu dataset usando *download_dataset.py*

1. Abra o arquivo *download_dataset.py* no Visual Studio Code.

1. Adicione o seguinte código no *download_dataset.py*.

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
> **Dica para fine-tuning com dataset mínimo usando CPU**
>
> Se quiser usar CPU para fine-tuning, essa abordagem é ideal para quem tem assinaturas de benefício (como Visual Studio Enterprise Subscription) ou para testar rapidamente o processo de fine-tuning e deployment.
>
> Substitua `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Digite o seguinte comando no terminal para rodar o script e baixar o dataset para seu ambiente local.

    ```console
    python download_data.py
    ```

1. Verifique se os datasets foram salvos com sucesso no diretório local *finetune-phi/data*.

> [!NOTE]
>
> **Tamanho do dataset e tempo de fine-tuning**
>
> Neste exemplo E2E, você usa apenas 1% do dataset (`train_sft[:1%]`). Isso reduz significativamente a quantidade de dados, acelerando tanto o upload quanto o processo de fine-tuning. Você pode ajustar a porcentagem para encontrar o equilíbrio ideal entre tempo de treinamento e desempenho do modelo. Usar um subconjunto menor do dataset reduz o tempo necessário para o fine-tuning, tornando o processo mais gerenciável para um exemplo E2E.

## Cenário 2: Fine-tune do modelo Phi-3 e Deploy no Azure Machine Learning Studio

### Configure o Azure CLI

Você precisa configurar o Azure CLI para autenticar seu ambiente. O Azure CLI permite gerenciar recursos Azure diretamente pela linha de comando e fornece as credenciais necessárias para o Azure Machine Learning acessar esses recursos. Para começar, instale o [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Abra uma janela de terminal e digite o seguinte comando para fazer login na sua conta Azure.

    ```console
    az login
    ```

1. Selecione a conta Azure que deseja usar.

1. Selecione a assinatura Azure que deseja usar.

    ![Find resource group name.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.br.png)

> [!TIP]
>
> Se estiver com problemas para entrar no Azure, tente usar um código de dispositivo. Abra uma janela de terminal e digite o seguinte comando para fazer login na sua conta Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Faça o fine-tuning do modelo Phi-3

Neste exercício, você vai fazer o fine-tuning do modelo Phi-3 usando o dataset fornecido. Primeiro, você vai definir o processo de fine-tuning no arquivo *fine_tune.py*. Depois, vai configurar o ambiente Azure Machine Learning e iniciar o fine-tuning executando o arquivo *setup_ml.py*. Esse script garante que o fine-tuning ocorra dentro do ambiente Azure Machine Learning.

Ao executar o *setup_ml.py*, você rodará o processo de fine-tuning no ambiente Azure Machine Learning.

#### Adicione código no arquivo *fine_tune.py*

1. Navegue até a pasta *finetuning_dir* e abra o arquivo *fine_tune.py* no Visual Studio Code.

1. Adicione o seguinte código no *fine_tune.py*.

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

1. Salve e feche o arquivo *fine_tune.py*.

> [!TIP]
> **Você pode fazer fine-tuning do modelo Phi-3.5**
>
> No arquivo *fine_tune.py*, você pode alterar o campo `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` no seu script.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### Adicione código no arquivo *setup_ml.py*

1. Abra o arquivo *setup_ml.py* no Visual Studio Code.

1. Adicione o seguinte código no *setup_ml.py*.

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

1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` pelos seus dados específicos.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Dica para fine-tuning com dataset mínimo usando CPU**
>
> Se quiser usar CPU para fine-tuning, essa abordagem é ideal para quem tem assinaturas de benefício (como Visual Studio Enterprise Subscription) ou para testar rapidamente o processo de fine-tuning e deployment.
>
> 1. Abra o arquivo *setup_ml*.
> 1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` pelos seus dados específicos.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Digite o seguinte comando para executar o script *setup_ml.py* e iniciar o processo de fine-tuning no Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. Neste exercício, você fez o fine-tuning do modelo Phi-3 usando o Azure Machine Learning. Ao rodar o script *setup_ml.py*, você configurou o ambiente Azure Machine Learning e iniciou o processo de fine-tuning definido no arquivo *fine_tune.py*. Lembre-se que o processo de fine-tuning pode levar um tempo considerável. Após rodar o comando `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.br.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` com o nome desejado para sua implantação.

#### Adicione código no arquivo *deploy_model.py*

Executar o arquivo *deploy_model.py* automatiza todo o processo de deployment. Ele registra o modelo, cria um endpoint e executa o deployment com base nas configurações especificadas no arquivo config.py, que inclui o nome do modelo, nome do endpoint e nome do deployment.

1. Abra o arquivo *deploy_model.py* no Visual Studio Code.

1. Adicione o seguinte código no *deploy_model.py*.

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

1. Realize as seguintes tarefas para obter o `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` com seus dados específicos.

1. Digite o seguinte comando para rodar o script *deploy_model.py* e iniciar o processo de deployment no Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Para evitar cobranças adicionais na sua conta, certifique-se de excluir o endpoint criado no workspace Azure Machine Learning.
>

#### Verifique o status do deployment no Azure Machine Learning Workspace

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até o workspace Azure Machine Learning que você criou.

1. Selecione **Studio web URL** para abrir o workspace Azure Machine Learning.

1. Selecione **Endpoints** na aba lateral esquerda.

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.br.png)

2. Selecione o endpoint que você criou.

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.br.png)

3. Nesta página, você pode gerenciar os endpoints criados durante o processo de deployment.

## Cenário 3: Integre com Prompt flow e converse com seu modelo customizado

### Integre o modelo Phi-3 customizado com Prompt flow

Após implantar seu modelo fine-tuned com sucesso, agora você pode integrá-lo ao Prompt flow para usar seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com seu modelo Phi-3 customizado.

#### Defina a api key e o endpoint uri do modelo Phi-3 fine-tuned

1. Navegue até o workspace Azure Machine Learning que você criou.
1. Selecione **Endpoints** na aba lateral esquerda.
1. Selecione o endpoint que você criou.
1. Selecione **Consume** no menu de navegação.
1. Copie e cole seu **REST endpoint** no arquivo *config.py*, substituindo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` pela sua **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.br.png)

#### Adicione código no arquivo *flow.dag.yml*

1. Abra o arquivo *flow.dag.yml* no Visual Studio Code.

1. Adicione o seguinte código no *flow.dag.yml*.

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

#### Adicione código no arquivo *integrate_with_promptflow.py*

1. Abra o arquivo *integrate_with_promptflow.py* no Visual Studio Code.

1. Adicione o seguinte código no *integrate_with_promptflow.py*.

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

### Converse com seu modelo customizado

1. Digite o seguinte comando para rodar o script *deploy_model.py* e iniciar o processo de deployment no Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Aqui está um exemplo dos resultados: agora você pode conversar com seu modelo Phi-3 customizado. É recomendado fazer perguntas baseadas nos dados usados para o fine-tuning.

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.br.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.