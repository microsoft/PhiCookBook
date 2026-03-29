# Fine-tune and Integrate custom Phi-3 models wit Prompt flow for Microsoft Foundry

Dis end-to-end (E2E) sample na based on di guide "[Fine-Tune and Integrate Custom Phi-3 Models wit Prompt Flow for Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from Microsoft Tech Community. E show how to fine-tune, deploy, and integrate custom Phi-3 models wit Prompt flow for Microsoft Foundry. 
No be like di other E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models wit Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", wey dey run code local, dis tutorial na pure fine-tuning and integration for inside Azure AI / ML Studio.

## Overview

For dis E2E sample, you go learn how to fine-tune Phi-3 model and integrate am wit Prompt flow for Microsoft Foundry. With Azure AI / ML Studio, you go fit create workflow to deploy and use custom AI models. Dis E2E sample get three scenarios:

**Scenario 1: Setup Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune di Phi-3 model and Deploy for Azure Machine Learning Studio**

**Scenario 3: Integrate wit Prompt flow and Chat wit your custom model for Microsoft Foundry**

Dis one na overview of dis E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/pcm/00-01-architecture.198ba0f1ae6d841a.webp)

### Table of Contents

1. **[Scenario 1: Setup Azure resources and Prepare for fine-tuning](#scenario-1-setup-azure-resources-and-prepare-for-fine-tuning)**
    - [Create Azure Machine Learning Workspace](#create-azure-machine-learning-workspace)
    - [Request GPU quotas for Azure Subscription](#request-gpu-quotas-for-azure-subscription)
    - [Add role assignment](#add-role-assignment)
    - [Setup project](#setup-project)
    - [Prepare dataset for fine-tuning](#prepare-dataset-for-fine-tuning)

1. **[Scenario 2: Fine-tune Phi-3 model and Deploy for Azure Machine Learning Studio](#scenario-2-fine-tune-phi-3-model-and-deploy-for-azure-machine-learning-studio)**
    - [Fine-tune di Phi-3 model](#fine-tune-di-phi-3-model)
    - [Deploy di fine-tuned Phi-3 model](#deploy-di-fine-tuned-phi-3-model)

1. **[Scenario 3: Integrate wit Prompt flow and Chat wit your custom model for Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrate di custom Phi-3 model wit Prompt flow](#join-di-custom-phi-3-model-with-prompt-flow)
    - [Chat wit your custom Phi-3 model](#chat-with-your-custom-phi-3-model)

## Scenario 1: Setup Azure resources and Prepare for fine-tuning

### Create Azure Machine Learning Workspace

1. Type *azure machine learning* for **search bar** wey dey top of di portal page make you select **Azure Machine Learning** from wetin show.

    ![Type azure machine learning.](../../../../../../translated_images/pcm/01-01-type-azml.acae6c5455e67b4b.webp)

2. Select **+ Create** from di navigation menu.

3. Select **New workspace** from di navigation menu.

    ![Select new workspace.](../../../../../../translated_images/pcm/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Do dis gbege:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (or create new one if you need).
    - Put **Workspace Name**. E must be unique.
    - Select the **Region** wey you wan use.
    - Select the **Storage account** to use (or create new one if you need).
    - Select the **Key vault** to use (or create new one if you need).
    - Select the **Application insights** to use (or create new one if you need).
    - Select the **Container registry** to use (or create new one if you need).

    ![Fill azure machine learning.](../../../../../../translated_images/pcm/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Select **Review + Create**.

6. Select **Create**.

### Request GPU quotas for Azure Subscription

For dis tutorial, you go learn how to fine-tune and deploy Phi-3 model, using GPUs. For fine-tuning, you go use *Standard_NC24ads_A100_v4* GPU, wey need quota request. For deployment, you go use *Standard_NC6s_v3* GPU, wey still need quota request.

> [!NOTE]
>
> Only Pay-As-You-Go subscriptions (standard subscription type) fit get GPU allocation; benefit subscriptions no dey supported now.
>

1. Go [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Do dis for request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** from left side tab.
    - Select **Virtual machine family** wey you wan use. Example: choose **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, wey get *Standard_NC24ads_A100_v4* GPU.
    - Select **Request quota** for navigation menu.

        ![Request quota.](../../../../../../translated_images/pcm/02-02-request-quota.c0428239a63ffdd5.webp)

    - For Request quota page, put **New cores limit** wey you wan use. Example: 24.
    - For Request quota page, select **Submit** to request GPU quota.

1. Do dis for request *Standard NCSv3 Family* quota:

    - Select **Quota** for left side tab.
    - Select **Virtual machine family** wey you wan use. Example: choose **Standard NCSv3 Family Cluster Dedicated vCPUs**, wey get *Standard_NC6s_v3* GPU.
    - Select **Request quota** for navigation menu.
    - For Request quota page, put **New cores limit** wey you wan use. Example: 24.
    - For Request quota page, select **Submit** to request GPU quota.

### Add role assignment

To fit fine-tune and deploy your models, you go need first create User Assigned Managed Identity (UAI) and give am di correct permissions. Dis UAI na for authentication during deployment.

#### Create User Assigned Managed Identity(UAI)

1. Type *managed identities* for **search bar** wey dey top of di portal page make you select **Managed Identities** from wetin show.

    ![Type managed identities.](../../../../../../translated_images/pcm/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/pcm/03-02-select-create.92bf8989a5cd98f2.webp)

1. Do dis gbege:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (or create new one if you need).
    - Select the **Region** wey you wan use.
    - Put **Name**. E must be unique.

    ![Select create.](../../../../../../translated_images/pcm/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Go the Managed Identity resource wey you create.

1. Select **Azure role assignments** from left side tab.

1. Select **+Add role assignment** from navigation menu.

1. For Add role assignment page, do dis gbege:
    - Select **Scope** to **Resource group**.
    - Select your Azure **Subscription**.
    - Select the **Resource group** wey you wan use.
    - Select the **Role** to **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/pcm/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* for **search bar** wey dey top of di portal page make you select **Storage accounts** from wetin show.

    ![Type storage accounts.](../../../../../../translated_images/pcm/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Select storage account wey link to Azure Machine Learning workspace wey you create. Example, *finetunephistorage*.

1. Do dis gbege to reach Add role assignment page:

    - Go Azure Storage account wey you create.
    - Select **Access Control (IAM)** from left side tab.
    - Select **+ Add** from navigation menu.
    - Select **Add role assignment** from navigation menu.

    ![Add role.](../../../../../../translated_images/pcm/03-06-add-role.353ccbfdcf0789c2.webp)

1. For Add role assignment page, do dis gbege:

    - For Role page, type *Storage Blob Data Reader* for **search bar** make you select **Storage Blob Data Reader** from wetin show.
    - For Role page, select **Next**.
    - For Members page, select **Assign access to** **Managed identity**.
    - For Members page, select **+ Select members**.
    - For Select managed identities page, select your Azure **Subscription**.
    - For Select managed identities page, select **Managed identity** to **Manage Identity**.
    - For Select managed identities page, select the Manage Identity wey you create. Example, *finetunephi-managedidentity*.
    - For Select managed identities page, select **Select**.

    ![Select managed identity.](../../../../../../translated_images/pcm/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* for **search bar** wey dey top of di portal page make you select **Container registries** from wetin show.

    ![Type container registries.](../../../../../../translated_images/pcm/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Select container registry wey link to Azure Machine Learning workspace. Example, *finetunephicontainerregistry*.

1. Do dis gbege to reach Add role assignment page:

    - Select **Access Control (IAM)** from left side tab.
    - Select **+ Add** from navigation menu.
    - Select **Add role assignment** from navigation menu.

1. For Add role assignment page, do dis gbege:

    - For Role page, type *AcrPull* for **search bar** make you select **AcrPull** from wetin show.
    - For Role page, select **Next**.
    - For Members page, select **Assign access to** **Managed identity**.
    - For Members page, select **+ Select members**.
    - For Select managed identities page, select your Azure **Subscription**.
    - For Select managed identities page, select **Managed identity** to **Manage Identity**.
    - For Select managed identities page, select the Manage Identity wey you create. Example, *finetunephi-managedidentity*.
    - For Select managed identities page, select **Select**.
    - Select **Review + assign**.

### Setup project

To download datasets wey you need for fine-tuning, you go setup local environment.

For dis exercise, you go

- Create folder to work inside am.
- Create virtual environment.
- Install required packages.
- Create *download_dataset.py* file to download dataset.

#### Create folder to work inside am

1. Open terminal window and type di command wey go create folder wey dem name *finetune-phi* for default path.

    ```console
    mkdir finetune-phi
    ```

2. Inside your terminal, type dis command to enter *finetune-phi* folder wey you create.

    ```console
    cd finetune-phi
    ```

#### Create virtual environment

1. Inside your terminal, type dis command to create virtual environment wey dem name *.venv*.
    ```console
    python -m venv .venv
    ```

2. Type di following command inside your terminal to activate di virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> If e work, you go see *(.venv)* before di command prompt.

#### Install di required packages

1. Type di following commands inside your terminal to install di required packages.

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

1. Select di *finetune-phi* folder wey you create, wey dey located at *C:\Users\yourUserName\finetune-phi*.

    ![Select di folder wey you create.](../../../../../../translated_images/pcm/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. For di left pane of Visual Studio Code, right-click and select **New File** to create new file wey name na *download_dataset.py*.

    ![Create new file.](../../../../../../translated_images/pcm/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Prepare dataset for fine-tuning

For dis exercise, you go run di *download_dataset.py* file to download di *ultrachat_200k* datasets to your local environment. You go then use dis datasets to fine-tune di Phi-3 model for Azure Machine Learning.

For dis exercise, you go:

- Add code to di *download_dataset.py* file to download di datasets.
- Run di *download_dataset.py* file to download datasets to your local environment.

#### Download your dataset using *download_dataset.py*

1. Open di *download_dataset.py* file for Visual Studio Code.

1. Add di following code inside *download_dataset.py* file.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load di dataset wey get di name, config and split ratio wey dem specify
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Divide di dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Make di directory if e no dey
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open di file make e dey write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # waka through each record inside di dataset
            for record in dataset:
                # Dump di record as JSON object come write am for di file
                json.dump(record, f)
                # Write one newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split di ULTRACHAT_200k dataset wit specific config and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Comot di train and test datasets from di split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save di train dataset enter one JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save di test dataset for one different JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Type di following command inside your terminal to run di script and download di dataset to your local environment.

    ```console
    python download_dataset.py
    ```

1. Verify say di datasets save well for your local *finetune-phi/data* directory.

> [!NOTE]
>
> #### Note on dataset size and fine-tuning time
>
> For dis tutorial, you dey use only 1% of di dataset (`split='train[:1%]'`). Dis one reduce di amount of data well well, e go quick both di upload and fine-tuning processes. You fit adjust di percentage to find di correct balance between training time and model performance. To use smaller part of di dataset reduce di time wey fine-tuning go take, e dey make di process easier for tutorial.

## Scenario 2: Fine-tune Phi-3 model and Deploy for Azure Machine Learning Studio

### Fine-tune di Phi-3 model

For dis exercise, you go fine-tune di Phi-3 model for Azure Machine Learning Studio.

For dis exercise, you go:

- Create computer cluster for fine-tuning.
- Fine-tune di Phi-3 model for Azure Machine Learning Studio.

#### Create computer cluster for fine-tuning

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select **Compute** from di left side tab.

1. Select **Compute clusters** from di navigation menu.

1. Select **+ New**.

    ![Select compute.](../../../../../../translated_images/pcm/06-01-select-compute.a29cff290b480252.webp)

1. Do di following tasks:

    - Select di **Region** wey you wan use.
    - Select di **Virtual machine tier** to **Dedicated**.
    - Select di **Virtual machine type** to **GPU**.
    - Select di **Virtual machine size** filter to **Select from all options**.
    - Select di **Virtual machine size** to **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/pcm/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Select **Next**.

1. Do di following tasks:

    - Enter **Compute name**. E must be unique.
    - Select di **Minimum number of nodes** to **0**.
    - Select di **Maximum number of nodes** to **1**.
    - Select di **Idle seconds before scale down** to **120**.

    ![Create cluster.](../../../../../../translated_images/pcm/06-03-create-cluster.4a54ba20914f3662.webp)

1. Select **Create**.

#### Fine-tune di Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select di Azure Machine Learning workspace wey you create.

    ![Select workspace wey you create.](../../../../../../translated_images/pcm/06-04-select-workspace.a92934ac04f4f181.webp)

1. Do di following tasks:

    - Select **Model catalog** from di left side tab.
    - Type *phi-3-mini-4k* for di **search bar** and select **Phi-3-mini-4k-instruct** from di options wey show.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/pcm/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Select **Fine-tune** from di navigation menu.

    ![Select fine tune.](../../../../../../translated_images/pcm/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Do di following tasks:

    - Select **Select task type** to **Chat completion**.
    - Select **+ Select data** to upload **Training data**.
    - Select di Validation data upload type to **Provide different validation data**.
    - Select **+ Select data** to upload **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/pcm/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> You fit select **Advanced settings** to customize configurations like **learning_rate** and **lr_scheduler_type** to optimize di fine-tuning process based on your own needs.

1. Select **Finish**.

1. For dis exercise, you don fine-tune di Phi-3 model well using Azure Machine Learning. Abeg note say di fine-tuning process fit take plenty time. After you run di fine-tuning job, you need wait sey e finish. You fit monitor di status of di fine-tuning job by going to di Jobs tab for di left side of your Azure Machine Learning workspace. For di next series, you go deploy di fine-tuned model and connect am with Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/pcm/06-08-output.2bd32e59930672b1.webp)

### Deploy di fine-tuned Phi-3 model

To join di fine-tuned Phi-3 model with Prompt flow, you need deploy di model make e dey accessible for real-time inference. Dis process get to do with registering di model, creating online endpoint, and deploying di model.

For dis exercise, you go:

- Register di fine-tuned model for di Azure Machine Learning workspace.
- Create online endpoint.
- Deploy di registered fine-tuned Phi-3 model.

#### Register di fine-tuned model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select di Azure Machine Learning workspace wey you create.

    ![Select workspace wey you create.](../../../../../../translated_images/pcm/06-04-select-workspace.a92934ac04f4f181.webp)

1. Select **Models** from di left side tab.
1. Select **+ Register**.
1. Select **From a job output**.

    ![Register model.](../../../../../../translated_images/pcm/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Select di job wey you create.

    ![Select job.](../../../../../../translated_images/pcm/07-02-select-job.3e2e1144cd6cd093.webp)

1. Select **Next**.

1. Select **Model type** to **MLflow**.

1. Make sure di **Job output** dey selected; e suppose dey selected automatically.

    ![Select output.](../../../../../../translated_images/pcm/07-03-select-output.4cf1a0e645baea1f.webp)

2. Select **Next**.

3. Select **Register**.

    ![Select register.](../../../../../../translated_images/pcm/07-04-register.fd82a3b293060bc7.webp)

4. You fit see your registered model by going to di **Models** menu from di left side tab.

    ![Registered model.](../../../../../../translated_images/pcm/07-05-registered-model.7db9775f58dfd591.webp)

#### Deploy di fine-tuned model

1. Go di Azure Machine Learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

1. Select **Real-time endpoints** from di navigation menu.

    ![Create endpoint.](../../../../../../translated_images/pcm/07-06-create-endpoint.1ba865c606551f09.webp)

1. Select **Create**.

1. select di registered model wey you create.

    ![Select registered model.](../../../../../../translated_images/pcm/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Select **Select**.

1. Do di following tasks:

    - Select **Virtual machine** to *Standard_NC6s_v3*.
    - Select di **Instance count** wey you want use. Example, *1*.
    - Select di **Endpoint** to **New** to create endpoint.
    - Enter **Endpoint name**. E must be unique.
    - Enter **Deployment name**. E must be unique.

    ![Fill di deployment setting.](../../../../../../translated_images/pcm/07-08-deployment-setting.43ddc4209e673784.webp)

1. Select **Deploy**.

> [!WARNING]
> To avoid extra charges to your account, make sure say you delete di created endpoint for di Azure Machine Learning workspace.
>

#### Check deployment status for Azure Machine Learning Workspace

1. Go Azure Machine Learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

1. Select di endpoint wey you create.

    ![Select endpoints](../../../../../../translated_images/pcm/07-09-check-deployment.325d18cae8475ef4.webp)

1. For dis page, you fit manage di endpoints during di deployment process.

> [!NOTE]
> Once di deployment don finish, make sure say **Live traffic** dey set to **100%**. If e never reach, select **Update traffic** to adjust di traffic settings. Note say you no fit test di model if di traffic dey 0%.
>
> ![Set traffic.](../../../../../../translated_images/pcm/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenario 3: Join with Prompt flow and Chat with your custom model for Microsoft Foundry

### Join di custom Phi-3 model with Prompt flow

After you don successfully deploy your fine-tuned model, you fit now join am with Prompt Flow to use your model for real-time applications, to enable plenty interactive tasks with your custom Phi-3 model.

For dis exercise, you go:

- Create Microsoft Foundry Hub.
- Create Microsoft Foundry Project.
- Create Prompt flow.
- Add custom connection for di fine-tuned Phi-3 model.
- Set up Prompt flow to chat with your custom Phi-3 model

> [!NOTE]
> You fit also join with Promptflow using Azure ML Studio. Di same integration process fit apply for Azure ML Studio.

#### Create Microsoft Foundry Hub

You need create Hub before you fit create di Project. Hub dey act like Resource Group, e go help you organize and manage plenty Projects inside Microsoft Foundry.
1. Visit [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Select **All hubs** for di left side tab.

1. Select **+ New hub** for di navigation menu.

    ![Create hub.](../../../../../../translated_images/pcm/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Do di following tins:

    - Enter **Hub name**. E for be unique value.
    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you wan use (make new one if you need am).
    - Select di **Location** wey you go like use.
    - Select di **Connect Azure AI Services** wey you go use (make new one if you need am).
    - Select **Connect Azure AI Search** to **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/pcm/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Select **Next**.

#### Create Microsoft Foundry Project

1. For di Hub wey you create, select **All projects** for di left side tab.

1. Select **+ New project** for di navigation menu.

    ![Select new project.](../../../../../../translated_images/pcm/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Enter **Project name**. E for be unique value.

    ![Create project.](../../../../../../translated_images/pcm/08-05-create-project.4d97f0372f03375a.webp)

1. Select **Create a project**.

#### Add a custom connection for di fine-tuned Phi-3 model

To join your custom Phi-3 model with Prompt flow, you need to save di model's endpoint and key for one custom connection. Dis setup go make sure say you fit access your custom Phi-3 model for Prompt flow.

#### Set api key and endpoint uri of di fine-tuned Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Go di Azure Machine learning workspace wey you create.

1. Select **Endpoints** for di left side tab.

    ![Select endpoints.](../../../../../../translated_images/pcm/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Select di endpoint wey you create.

    ![Select endpoints.](../../../../../../translated_images/pcm/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Select **Consume** for di navigation menu.

1. Copy your **REST endpoint** and **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pcm/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Add di Custom Connection

1. Visit [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Go the Microsoft Foundry project wey you create.

1. For di Project wey you create, select **Settings** for di left side tab.

1. Select **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/pcm/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Select **Custom keys** for di navigation menu.

    ![Select custom keys.](../../../../../../translated_images/pcm/08-10-select-custom-keys.856f6b2966460551.webp)

1. Do di following tins:

    - Select **+ Add key value pairs**.
    - For di key name, enter **endpoint** and paste di endpoint wey you copy from Azure ML Studio for di value field.
    - Select **+ Add key value pairs** again.
    - For di key name, enter **key** and paste di key wey you copy from Azure ML Studio for di value field.
    - After you add di keys, select **is secret** so di key no go show publicly.

    ![Add connection.](../../../../../../translated_images/pcm/08-11-add-connection.785486badb4d2d26.webp)

1. Select **Add connection**.

#### Create Prompt flow

You don add custom connection for Microsoft Foundry. Now, make we create Prompt flow using dis steps. Then, you go connect dis Prompt flow to di custom connection so you fit use di fine-tuned model inside di Prompt flow.

1. Go di Microsoft Foundry project wey you create.

1. Select **Prompt flow** for di left side tab.

1. Select **+ Create** for di navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/pcm/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Select **Chat flow** for di navigation menu.

    ![Select chat flow.](../../../../../../translated_images/pcm/08-13-select-flow-type.2ec689b22da32591.webp)

1. Enter **Folder name** wey you wan use.

    ![Enter name.](../../../../../../translated_images/pcm/08-14-enter-name.ff9520fefd89f40d.webp)

2. Select **Create**.

#### Set up Prompt flow to chat with your custom Phi-3 model

You need to join di fine-tuned Phi-3 model into Prompt flow. But, di Prompt flow wey dey now no design for dis kain work. So, you gats redesign di Prompt flow so e go fit join di custom model.

1. For di Prompt flow, do di following tasks to rebuild di flow wey dey:

    - Select **Raw file mode**.
    - Delete all di code wey dey for *flow.dag.yml* file.
    - Add dis code for *flow.dag.yml* file.

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

    ![Select raw file mode.](../../../../../../translated_images/pcm/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Add dis code for *integrate_with_promptflow.py* file to use di custom Phi-3 model for Prompt flow.

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

        # "connection" na di name of di Custom Connection, "endpoint", "key" na di keys for di Custom Connection
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

    ![Paste prompt flow code.](../../../../../../translated_images/pcm/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> For better info on how to use Prompt flow for Microsoft Foundry, you fit check [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Select **Chat input**, **Chat output** to fit chat with your model.

    ![Input Output.](../../../../../../translated_images/pcm/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Now you ready to chat with your custom Phi-3 model. For di next exercise, you go learn how to start Prompt flow and use am to chat with your fine-tuned Phi-3 model.

> [!NOTE]
>
> Di rebuilt flow go look like di picture below:
>
> ![Flow example.](../../../../../../translated_images/pcm/08-18-graph-example.d6457533952e690c.webp)
>

### Chat with your custom Phi-3 model

Now wey you don fine-tune and join your custom Phi-3 model with Prompt flow, you ready to start to dey interact wit am. Dis exercise go show you di way to set up and begin chat with your model using Prompt flow. If you follow dis steps, you go fit use all di power of your fine-tuned Phi-3 model for many tasks and conversations.

- Chat with your custom Phi-3 model using Prompt flow.

#### Start Prompt flow

1. Select **Start compute sessions** to start Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pcm/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Select **Validate and parse input** to refresh parameters.

    ![Validate input.](../../../../../../translated_images/pcm/09-02-validate-input.317c76ef766361e9.webp)

1. Select di **Value** of di **connection** to di custom connection wey you create. For example, *connection*.

    ![Connection.](../../../../../../translated_images/pcm/09-03-select-connection.99bdddb4b1844023.webp)

#### Chat with your custom model

1. Select **Chat**.

    ![Select chat.](../../../../../../translated_images/pcm/09-04-select-chat.61936dce6612a1e6.webp)

1. Dis na example of di results: Now you fit chat with your custom Phi-3 model. E good make you ask question based on di data wey dem use for fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/pcm/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg remember say automated translations fit get mistakes or errors. Di original document wey e dey for im correct language na di main source wey you suppose use. For important matter, make you use professional human translation. We no responsible if you no understand or if something wrong comot from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->