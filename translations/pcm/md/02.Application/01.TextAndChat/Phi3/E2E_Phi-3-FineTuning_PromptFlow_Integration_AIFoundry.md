<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-12-21T20:42:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "pcm"
}
-->
# Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Foundry

This end-to-end (E2E) sample dey based on di guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from Microsoft Tech Community. E dey introduce di process dem for fine-tuning, deploying, an integrating custom Phi-3 models wit Prompt flow for Azure AI Foundry.
No like di E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", wey require to run code for local machine, dis tutorial dey focus complete on fine-tuning an integrating your model inside Azure AI / ML Studio.

## Overview

For dis E2E sample, you go learn how to fine-tune di Phi-3 model an integrate am wit Prompt flow for Azure AI Foundry. By using Azure AI / ML Studio, you go set up workflow to deploy an use custom AI models. Dis E2E sample divide into three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**

**Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry**

Below na small overview of dis E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.pcm.png)

### Table of Contents

1. **[Scenario 1: Set up Azure resources and Prepare for fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Create an Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Request GPU quotas in Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Add role assignment](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Set up project](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Prepare dataset for fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Fine-tune the Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy the fine-tuned Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrate the custom Phi-3 model with Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat with your custom Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Set up Azure resources and Prepare for fine-tuning

### Create an Azure Machine Learning Workspace

1. Type *azure machine learning* for di **search bar** wey dey top of di portal page an select **Azure Machine Learning** from di options wey go show.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.pcm.png)

2. Select **+ Create** from di navigation menu.

3. Select **New workspace** from di navigation menu.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.pcm.png)

4. Do di following tasks:

    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use (create new one if you need).
    - Enter **Workspace Name**. E must be unique.
    - Select di **Region** wey you wan use.
    - Select di **Storage account** wey you go use (create new one if you need).
    - Select di **Key vault** wey you go use (create new one if you need).
    - Select di **Application insights** wey you go use (create new one if you need).
    - Select di **Container registry** wey you go use (create new one if you need).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.pcm.png)

5. Select **Review + Create**.

6. Select **Create**.

### Request GPU quotas in Azure Subscription

For dis tutorial, you go learn how to fine-tune an deploy a Phi-3 model, using GPUs. For fine-tuning, you go use di *Standard_NC24ads_A100_v4* GPU, wey need quota request. For deployment, you go use di *Standard_NC6s_v3* GPU, wey also need quota request.

> [!NOTE]
>
> Only Pay-As-You-Go subscriptions (di standard subscription type) fit get GPU allocation; benefit subscriptions no dey supported now.
>

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Do di following tasks to request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** from di left side tab.
    - Select di **Virtual machine family** wey you want use. For example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, wey include di *Standard_NC24ads_A100_v4* GPU.
    - Select di **Request quota** from di navigation menu.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.pcm.png)

    - For di Request quota page, enter di **New cores limit** wey you wan use. For example, 24.
    - For di Request quota page, select **Submit** to request di GPU quota.

1. Do di following tasks to request *Standard NCSv3 Family* quota:

    - Select **Quota** from di left side tab.
    - Select di **Virtual machine family** wey you want use. For example, select **Standard NCSv3 Family Cluster Dedicated vCPUs**, wey include di *Standard_NC6s_v3* GPU.
    - Select di **Request quota** from di navigation menu.
    - For di Request quota page, enter di **New cores limit** wey you wan use. For example, 24.
    - For di Request quota page, select **Submit** to request di GPU quota.

### Add role assignment

To fine-tune an deploy your models, you must first create a User Assigned Managed Identity (UAI) an give am correct permissions. Dis UAI go dey used for authentication during deployment

#### Create User Assigned Managed Identity(UAI)

1. Type *managed identities* for di **search bar** wey dey top of di portal page an select **Managed Identities** from di options wey go show.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.pcm.png)

1. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.pcm.png)

1. Do di following tasks:

    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use (create new one if you need).
    - Select di **Region** wey you wan use.
    - Enter di **Name**. E must be unique.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.pcm.png)

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Go to di Managed Identity resource wey you create.

1. Select **Azure role assignments** from di left side tab.

1. Select **+Add role assignment** from di navigation menu.

1. For Add role assignment page, do di following tasks:
    - Select di **Scope** to **Resource group**.
    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use.
    - Select di **Role** to **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.pcm.png)

2. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* for di **search bar** wey dey top of di portal page an select **Storage accounts** from di options wey go show.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.pcm.png)

1. Select di storage account wey join wit di Azure Machine Learning workspace wey you create. For example, *finetunephistorage*.

1. Do di following tasks to go Add role assignment page:

    - Go to di Azure Storage account wey you create.
    - Select **Access Control (IAM)** from di left side tab.
    - Select **+ Add** from di navigation menu.
    - Select **Add role assignment** from di navigation menu.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.pcm.png)

1. For Add role assignment page, do di following tasks:

    - For di Role page, type *Storage Blob Data Reader* for di **search bar** an select **Storage Blob Data Reader** from di options wey go show.
    - For di Role page, select **Next**.
    - For di Members page, select **Assign access to** **Managed identity**.
    - For di Members page, select **+ Select members**.
    - For di Select managed identities page, select your Azure **Subscription**.
    - For di Select managed identities page, select di **Managed identity** to **Manage Identity**.
    - For di Select managed identities page, select di Manage Identity wey you create. For example, *finetunephi-managedidentity*.
    - For di Select managed identities page, select **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.pcm.png)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* for di **search bar** wey dey top of di portal page an select **Container registries** from di options wey go show.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.pcm.png)

1. Select di container registry wey join wit di Azure Machine Learning workspace. For example, *finetunephicontainerregistry*

1. Do di following tasks to go Add role assignment page:

    - Select **Access Control (IAM)** from di left side tab.
    - Select **+ Add** from di navigation menu.
    - Select **Add role assignment** from di navigation menu.

1. For Add role assignment page, do di following tasks:

    - For di Role page, Type *AcrPull* for di **search bar** an select **AcrPull** from di options wey go show.
    - For di Role page, select **Next**.
    - For di Members page, select **Assign access to** **Managed identity**.
    - For di Members page, select **+ Select members**.
    - For di Select managed identities page, select your Azure **Subscription**.
    - For di Select managed identities page, select di **Managed identity** to **Manage Identity**.
    - For di Select managed identities page, select di Manage Identity wey you create. For example, *finetunephi-managedidentity*.
    - For di Select managed identities page, select **Select**.
    - Select **Review + assign**.

### Set up project

To download di datasets wey you need for fine-tuning, you go set up local environment.

For dis exercise, you go

- Create one folder to work inside.
- Create virtual environment.
- Install di required packages.
- Create *download_dataset.py* file to download di dataset.

#### Create a folder to work inside it

1. Open terminal window an type dis command to create one folder wey name na *finetune-phi* for di default path.

    ```console
    mkdir finetune-phi
    ```

2. Type di following command for your terminal to navigate go inside di *finetune-phi* folder wey you don create.

    ```console
    cd finetune-phi
    ```

#### Create a virtual environment

1. Type di following command for your terminal to create virtual environment wey dem name *.venv*.

    ```console
    python -m venv .venv
    ```

2. Type di following command for your terminal to activate di virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> If e work, you go see *(.venv)* before di command prompt.

#### Install di required packages

1. Type di following commands for your terminal to install di required packages.

    ```console
    pip install datasets==2.19.1
    ```

#### Create `donload_dataset.py`

> [!NOTE]
> Complete folder structure:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Open **Visual Studio Code**.

1. Select **File** from di menu bar.

1. Select **Open Folder**.

1. Select di *finetune-phi* folder wey you create, wey dey for *C:\Users\yourUserName\finetune-phi*.

    ![Select di folder wey you create.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.pcm.png)

1. For left pane for Visual Studio Code, right-click and select **New File** make you create new file wey dem go name *download_dataset.py*.

    ![Create new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.pcm.png)

### Prepare dataset for fine-tuning

For dis exercise, you go run di *download_dataset.py* file to download di *ultrachat_200k* datasets to your local environment. You go den use these datasets to fine-tune di Phi-3 model for Azure Machine Learning.

For dis exercise, you go:

- Add code to di *download_dataset.py* file to download di datasets.
- Run di *download_dataset.py* file to download di datasets to your local environment.

#### Download your dataset using *download_dataset.py*

1. Open di *download_dataset.py* file for Visual Studio Code.

1. Add di following code inside di *download_dataset.py* file.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load di dataset wey dem give name, configuration, an di split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split di dataset into train an test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create di directory if e no dey
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open di file for write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record inside di dataset
            for record in dataset:
                # Dump di record as JSON object an write am to di file
                json.dump(record, f)
                # Write one newline character make records separate
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load an split di ULTRACHAT_200k dataset with di specific configuration an split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract di train an test datasets from di split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save di train dataset to one JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save di test dataset to another JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Type di following command for your terminal to run di script and download di dataset to your local environment.

    ```console
    python download_dataset.py
    ```

1. Verify say di datasets don save well for your local *finetune-phi/data* directory.

> [!NOTE]
>
> #### Note on dataset size and fine-tuning time
>
> For dis tutorial, you dey use only 1% of di dataset (`split='train[:1%]'`). Dis one go reduce di amount of data wella, e go make upload and fine-tuning faster. You fit change di percentage to balance training time and how well di model go perform. If you use small subset of di dataset, e go reduce di time wey fine-tuning go take, make am easier for tutorial.

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Fine-tune the Phi-3 model

For dis exercise, you go fine-tune di Phi-3 model for Azure Machine Learning Studio.

For dis exercise, you go:

- Create computer cluster for fine-tuning.
- Fine-tune di Phi-3 model for Azure Machine Learning Studio.

#### Create computer cluster for fine-tuning

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select **Compute** for di left side tab.

1. Select **Compute clusters** from di navigation menu.

1. Select **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.pcm.png)

1. Do di following tasks:

    - Select di **Region** wey you want use.
    - Select di **Virtual machine tier** to **Dedicated**.
    - Select di **Virtual machine type** to **GPU**.
    - Select di **Virtual machine size** filter to **Select from all options**.
    - Select di **Virtual machine size** to **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.pcm.png)

1. Select **Next**.

1. Do di following tasks:

    - Enter **Compute name**. E must be unique.
    - Select di **Minimum number of nodes** to **0**.
    - Select di **Maximum number of nodes** to **1**.
    - Select di **Idle seconds before scale down** to **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.pcm.png)

1. Select **Create**.

#### Fine-tune the Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select di Azure Macnine Learning workspace wey you create.

    ![Select workspace wey you create.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.pcm.png)

1. Do di following tasks:

    - Select **Model catalog** from di left side tab.
    - Type *phi-3-mini-4k* for di **search bar** and select **Phi-3-mini-4k-instruct** from di options wey show.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.pcm.png)

1. Select **Fine-tune** from di navigation menu.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.pcm.png)

1. Do di following tasks:

    - Select **Select task type** to **Chat completion**.
    - Select **+ Select data** to upload **Traning data**.
    - Select di Validation data upload type to **Provide different validation data**.
    - Select **+ Select data** to upload **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.pcm.png)

    > [!TIP]
    >
    > You fit select **Advanced settings** to customize configurations like **learning_rate** and **lr_scheduler_type** to optimize di fine-tuning process as e suit your needs.

1. Select **Finish**.

1. For dis exercise, you don successfully fine-tune di Phi-3 model using Azure Machine Learning. Abeg note say fine-tuning fit take plenty time. After you run di fine-tuning job, you need wait make e finish. You fit monitor di status of di fine-tuning job by going to di Jobs tab for left side of your Azure Machine Learning Workspace. For di next series, you go deploy di fine-tuned model and integrate am with Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.pcm.png)

### Deploy the fine-tuned Phi-3 model

To integrate di fine-tuned Phi-3 model with Prompt flow, you need deploy di model make e available for real-time inference. Dis process involve registering di model, creating online endpoint, and deploying di model.

For dis exercise, you go:

- Register di fine-tuned model for Azure Machine Learning workspace.
- Create online endpoint.
- Deploy di registered fine-tuned Phi-3 model.

#### Register the fine-tuned model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select di Azure Macnine Learning workspace wey you create.

    ![Select workspace wey you create.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.pcm.png)

1. Select **Models** from di left side tab.
1. Select **+ Register**.
1. Select **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.pcm.png)

1. Select di job wey you create.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.pcm.png)

1. Select **Next**.

1. Select **Model type** to **MLflow**.

1. Make sure say **Job output** dey selected; e suppose select am automatically.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.pcm.png)

2. Select **Next**.

3. Select **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.pcm.png)

4. You fit view your registered model by going to **Models** menu for left side tab.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.pcm.png)

#### Deploy the fine-tuned model

1. Navigate go di Azure Macnine Learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

1. Select **Real-time endpoints** from di navigation menu.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.pcm.png)

1. Select **Create**.

1. Select di registered model wey you create.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.pcm.png)

1. Select **Select**.

1. Do di following tasks:

    - Select **Virtual machine** to *Standard_NC6s_v3*.
    - Select di **Instance count** wey you want use. For example, *1*.
    - Select di **Endpoint** to **New** to create new endpoint.
    - Enter **Endpoint name**. E must be unique.
    - Enter **Deployment name**. E must be unique.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.pcm.png)

1. Select **Deploy**.

> [!WARNING]
> To avoid extra charges for your account, make sure say you delete di endpoint wey you create for Azure Machine Learning workspace.
>

#### Check deployment status in Azure Machine Learning Workspace

1. Navigate go di Azure Machine Learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

1. Select di endpoint wey you create.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.pcm.png)

1. For dis page, you fit manage di endpoints while dem dey deploy.

> [!NOTE]
> Once di deployment don complete, make sure say **Live traffic** set to **100%**. If e never, select **Update traffic** to change di traffic settings. Note say you no fit test di model if di traffic set to 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.pcm.png)
>

## Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry

### Integrate the custom Phi-3 model with Prompt flow

After you don successfully deploy your fine-tuned model, you fit now integrate am with Prompt Flow to use your model for real-time applications, make you fit do different interactive tasks with your custom Phi-3 model.

For dis exercise, you go:

- Create Azure AI Foundry Hub.
- Create Azure AI Foundry Project.
- Create Prompt flow.
- Add custom connection for di fine-tuned Phi-3 model.
- Set up Prompt flow to chat with your custom Phi-3 model

> [!NOTE]
> You fit still integrate with Promptflow using Azure ML Studio. Di same integration process fit apply for Azure ML Studio.

#### Create Azure AI Foundry Hub

You need create Hub before you fit create di Project. Hub dey act like Resource Group, e help organize and manage many Projects inside Azure AI Foundry.

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Select **All hubs** from di left side tab.

1. Select **+ New hub** from di navigation menu.
![Create di hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.pcm.png)

1. Do di following tasks:

    - Enter **Hub name**. E must be unique value.
    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use (create new one if need).
    - Select di **Location** wey you wan use.
    - Select di **Connect Azure AI Services** wey you go use (create new one if need).
    - Select **Connect Azure AI Search** make e **Skip connecting**.

    ![Fill di hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.pcm.png)

1. Select **Next**.

#### Create Azure AI Foundry Project

1. For di Hub wey you create, select **All projects** from di left side tab.

1. Select **+ New project** from di navigation menu.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.pcm.png)

1. Enter **Project name**. E must be unique value.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.pcm.png)

1. Select **Create a project**.

#### Add a custom connection for the fine-tuned Phi-3 model

To join your custom Phi-3 model with Prompt flow, you need save di model's endpoint and key for a custom connection. Dis setup go make sure say Prompt flow fit access your custom Phi-3 model.

#### Set api key and endpoint uri of the fine-tuned Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Go to di Azure Machine learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.pcm.png)

1. Select di endpoint wey you create.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.pcm.png)

1. Select **Consume** from di navigation menu.

1. Copy your **REST endpoint** and **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.pcm.png)

#### Add the Custom Connection

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Go to di Azure AI Foundry project wey you create.

1. For di Project wey you create, select **Settings** from di left side tab.

1. Select **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.pcm.png)

1. Select **Custom keys** from di navigation menu.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.pcm.png)

1. Do di following tasks:

    - Select **+ Add key value pairs**.
    - For di key name, enter **endpoint** and paste di endpoint wey you copy from Azure ML Studio inside di value field.
    - Select **+ Add key value pairs** again.
    - For di key name, enter **key** and paste di key wey you copy from Azure ML Studio inside di value field.
    - After you don add di keys, select **is secret** make di key no open.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.pcm.png)

1. Select **Add connection**.

#### Create Prompt flow

You don add custom connection for Azure AI Foundry. Now, make we create Prompt flow follow dis steps. After dat, you go connect dis Prompt flow to di custom connection so you fit use di fine-tuned model inside Prompt flow.

1. Go to di Azure AI Foundry project wey you create.

1. Select **Prompt flow** from di left side tab.

1. Select **+ Create** from di navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.pcm.png)

1. Select **Chat flow** from di navigation menu.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.pcm.png)

1. Enter **Folder name** wey you wan use.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.pcm.png)

2. Select **Create**.

#### Set up Prompt flow to chat with your custom Phi-3 model

You need to join di fine-tuned Phi-3 model into a Prompt flow. But, di Prompt flow wey dem give no set up for dis kind thing. So, you go redesign di Prompt flow make e fit use di custom model.

1. For di Prompt flow, do di following tasks to rebuild di existing flow:

    - Select **Raw file mode**.
    - Delete all existing code inside di *flow.dag.yml* file.
    - Add di following code to *flow.dag.yml* file.

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

    - Select **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.pcm.png)

1. Add di following code to *integrate_with_promptflow.py* file to use di custom Phi-3 model inside Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # How we go set up logging
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

        # "connection" na di name of di Custom Connection, "endpoint", "key" na di keys wey dey inside di Custom Connection
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
            
            # Log di full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.pcm.png)

> [!NOTE]
> If you want more detail gist about how to use Prompt flow inside Azure AI Foundry, you fit check [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Select **Chat input**, **Chat output** to enable chat with your model.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.pcm.png)

1. Now you ready to chat with your custom Phi-3 model. For di next exercise, you go learn how to start Prompt flow and how to use am to yarn with your fine-tuned Phi-3 model.

> [!NOTE]
>
> Di rebuilt flow suppose resemble di image below:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.pcm.png)
>

### Chat with your custom Phi-3 model

Now wey you don fine-tune and join your custom Phi-3 model with Prompt flow, you ready to start to dey interact with am. Dis exercise go guide you step-by-step to set up and start chat with your model using Prompt flow. If you follow di steps, you go fit use di kain power wey your fine-tuned Phi-3 model get for different tasks and conversations.

- Yarn with your custom Phi-3 model using Prompt flow.

#### Start Prompt flow

1. Select **Start compute sessions** to start Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.pcm.png)

1. Select **Validate and parse input** to renew parameters.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.pcm.png)

1. Select di **Value** of di **connection** to di custom connection wey you create. For example, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.pcm.png)

#### Chat with your custom model

1. Select **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.pcm.png)

1. Check example of di results: Now you fit yarn with your custom Phi-3 model. E better make you ask questions wey base on di data wey dem use for fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.pcm.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclayma:
Dis dokument don translate wit AI translation service wey dem dey call Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, make you sabi say automatic translations fit get mistakes or wrong parts. Di original dokument for im original language na di official source wey you suppose take. If na important mata, e better make person wey sabi do professional human translation do am. We no go responsible for any misunderstanding or wrong interpretation wey fit follow because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->