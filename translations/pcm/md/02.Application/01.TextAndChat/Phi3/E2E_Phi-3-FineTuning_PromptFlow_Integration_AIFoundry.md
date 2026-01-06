<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0df910a227098303cc392b6ad204c271",
  "translation_date": "2026-01-06T05:32:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "pcm"
}
-->
# Fine-tune and Integrate custom Phi-3 models wit Prompt flow for Azure AI Foundry

Dis end-to-end (E2E) sample na based on di guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from Microsoft Tech Community. E dey show di process dem to fine-tune, deploy, and integrate custom Phi-3 models wit Prompt flow for Azure AI Foundry.  
Different from di E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", wey involve to run code for local machine, dis tutorial na totally about fine-tuning and integrating your model for inside Azure AI / ML Studio.

## Overview

For dis E2E sample, you go learn how to fine-tune di Phi-3 model and integrate am wit Prompt flow for Azure AI Foundry. By to work wit Azure AI / ML Studio, you go set workflow to deploy and run your own AI models. Dis E2E sample dem divide into three scenario:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy for Azure Machine Learning Studio**

**Scenario 3: Integrate wit Prompt flow and Chat wit your custom model for Azure AI Foundry**

Na overview of dis E2E sample be dis one.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.pcm.png)

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

1. Type *azure machine learning* for di **search bar** wey dey top for di portal page and select **Azure Machine Learning** from di options wey show.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.pcm.png)

2. Select **+ Create** for di navigation menu.

3. Select **New workspace** for di navigation menu.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.pcm.png)

4. Make you do these:

    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you wan use (make new one if you need am).
    - Put **Workspace Name**. E must be one kain value wey no get wahala.
    - Select di **Region** wey you wan use.
    - Select di **Storage account** to use (make new one if you need am).
    - Select di **Key vault** to use (make new one if you need am).
    - Select di **Application insights** to use (make new one if you need am).
    - Select di **Container registry** to use (make new one if you need am).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.pcm.png)

5. Select **Review + Create**.

6. Select **Create**.

### Request GPU quotas in Azure Subscription

For dis tutorial, you go learn how to fine-tune and deploy Phi-3 model, to use GPUs. For fine-tuning, you go use *Standard_NC24ads_A100_v4* GPU, wey need make you request quota. For deployment, you go use *Standard_NC6s_v3* GPU, wey also need make you request quota.

> [!NOTE]
>
> Na only Pay-As-You-Go subscriptions (di standard subscription kind) dey eligible for GPU allocation; benefit subscriptions dem no dey support yet.
>

1. Go [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Do these tasks to request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** for left side tab.
    - Select di **Virtual machine family** wey you wan use. Example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, wey get *Standard_NC24ads_A100_v4* GPU.
    - Select di **Request quota** for di navigation menu.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.pcm.png)

    - For Request quota page, put **New cores limit** wey you want use. Example, 24.
    - For Request quota page, select **Submit** to request GPU quota.

1. Do these tasks to request *Standard NCSv3 Family* quota:

    - Select **Quota** for left side tab.
    - Select di **Virtual machine family** wey you wan use. Example, select **Standard NCSv3 Family Cluster Dedicated vCPUs**, wey get *Standard_NC6s_v3* GPU.
    - Select di **Request quota** for di navigation menu.
    - For Request quota page, put **New cores limit** wey you want use. Example, 24.
    - For Request quota page, select **Submit** to request GPU quota.

### Add role assignment

To fit fine-tune and deploy your models, you gats first create User Assigned Managed Identity (UAI) and assign am correct permissions. Dis UAI na im you go use for authentication during deployment.

#### Create User Assigned Managed Identity(UAI)

1. Type *managed identities* for di **search bar** top for di portal page and select **Managed Identities** from di options wey show.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.pcm.png)

1. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.pcm.png)

1. Do these tasks:

    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you wan use (make new one if need).
    - Select di **Region** you wan use.
    - Put di **Name**. E must be one kain value wey no get wahala.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.pcm.png)

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Go your Managed Identity resource wey you create.

1. Select **Azure role assignments** for left side tab.

1. Select **+Add role assignment** from di navigation menu.

1. For Add role assignment page, do these tasks:  
    - Select the **Scope** to **Resource group**.  
    - Select your Azure **Subscription**.  
    - Select the **Resource group** to use.  
    - Select the **Role** to **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.pcm.png)

2. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* for di **search bar** at top of portal page and select **Storage accounts** from options wey show.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.pcm.png)

1. Select di storage account wey connect wit di Azure Machine Learning workspace wey you create. Example, *finetunephistorage*.

1. Do these to waka reach Add role assignment page:

    - Waka go di Azure Storage account wey you create.
    - Select **Access Control (IAM)** for left side tab.
    - Select **+ Add** for di navigation menu.
    - Select **Add role assignment** for di navigation menu.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.pcm.png)

1. For Add role assignment page, do these tasks:

    - For Role page, type *Storage Blob Data Reader* inside **search bar** and select **Storage Blob Data Reader** from options wey show.
    - For Role page, select **Next**.
    - For Members page, select **Assign access to** **Managed identity**.
    - For Members page, select **+ Select members**.
    - For Select managed identities page, select your Azure **Subscription**.
    - For Select managed identities page, select di **Managed identity** wey be **Manage Identity**.
    - For Select managed identities page, select di Manage Identity wey you create. Example, *finetunephi-managedidentity*.
    - For Select managed identities page, select **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.pcm.png)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* for di **search bar** at top portal page and select **Container registries** from options wey show.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.pcm.png)

1. Select di container registry wey connect wit di Azure Machine Learning workspace. Example, *finetunephicontainerregistry*

1. Do these to waka reach Add role assignment page:

    - Select **Access Control (IAM)** for left side tab.
    - Select **+ Add** for the navigation menu.
    - Select **Add role assignment** for di navigation menu.

1. For Add role assignment page, do these tasks:

    - For Role page, type *AcrPull* inside **search bar** and select **AcrPull** from options wey show.
    - For Role page, select **Next**.
    - For Members page, select **Assign access to** **Managed identity**.
    - For Members page, select **+ Select members**.
    - For Select managed identities page, select your Azure **Subscription**.
    - For Select managed identities page, select di **Managed identity** wey be **Manage Identity**.
    - For Select managed identities page, select di Manage Identity wey you create. Example, *finetunephi-managedidentity*.
    - For Select managed identities page, select **Select**.
    - Select **Review + assign**.

### Set up project

To download di dataset dem wey you need for fine-tuning, you go set local environment.

For dis exercise, you go

- Create folder wey you go work inside.
- Create virtual environment.
- Install di packages wey you need.
- Create *download_dataset.py* file to download di dataset.

#### Create a folder to work inside it

1. Open terminal window and type dis command below to create folder wey get name *finetune-phi* for di default path.

    ```console
    mkdir finetune-phi
    ```

2. Type di following command for inside your terminal to waka go di *finetune-phi* folder wey you don create.

    ```console
    cd finetune-phi
    ```

#### Create virtual environment

1. Type di following command for inside your terminal to create virtual environment wey dem call *.venv*.

    ```console
    python -m venv .venv
    ```

2. Type di following command for inside your terminal to activate di virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> If e work, you go fit see *(.venv)* for front of di command prompt.

#### Install di packages wey dem need

1. Type di following commands for inside your terminal to install di packages wey you need.

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

    ![Select di folder wey you create.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.pcm.png)

1. For left side pane for Visual Studio Code, right-click and select **New File** to create new file wey dem go call *download_dataset.py*.

    ![Create new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.pcm.png)

### Prepare dataset for fine-tuning

For dis exercise, you go run di *download_dataset.py* file to download di *ultrachat_200k* datasets go your local environment. Then you go use dis datasets to fine-tune di Phi-3 model inside Azure Machine Learning.

For dis exercise, you go:

- Add code into di *download_dataset.py* file to download di datasets.
- Run di *download_dataset.py* file to download di datasets inside your local environment.

#### Download your dataset with *download_dataset.py*

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
        # Load di dataset wit di spesefay configureshon an split ratio
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
        # Make di folder if e no dey
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open di file for write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Pass through every record for di dataset
            for record in dataset:
                # Dump di record as JSON objet an write am for di file
                json.dump(record, f)
                # Write one newline characta to separate di records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load an split di ULTRACHAT_200k dataset wit spesefay configureshon an split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Commot di train an test datasets from di split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save di train dataset go JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save di test dataset go separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Type di following command for inside your terminal to run di script and download di dataset inside your local environment.

    ```console
    python download_dataset.py
    ```

1. Check to confirm say di datasets dem don save well for your local *finetune-phi/data* directory.

> [!NOTE]
>
> #### Note on dataset size and fine-tuning time
>
> For dis tutorial, you dey use only 1% of di dataset (`split='train[:1%]'`). Dis one dey reduce plenti data, e dey make the upload and fine-tuning process quick pass. You fit adjust di percent make you find di balance between training time and how di model go perform. If you use smaller part of di dataset, e go reduce di fine-tuning time, e go make am easier to do dis tutorial.

## Scenario 2: Fine-tune Phi-3 model and Deploy inside Azure Machine Learning Studio

### Fine-tune Phi-3 model

For dis exercise, you go fine-tune di Phi-3 model for Azure Machine Learning Studio.

For dis exercise, you go:

- Create computer cluster for fine-tuning.
- Fine-tune di Phi-3 model inside Azure Machine Learning Studio.

#### Create computer cluster for fine-tuning

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select **Compute** from di left side tab.

1. Select **Compute clusters** from di navigation menu.

1. Select **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.pcm.png)

1. Do the following tasks:

    - Select di **Region** wey you wan use.
    - Select **Virtual machine tier** to **Dedicated**.
    - Select **Virtual machine type** to **GPU**.
    - Select **Virtual machine size** filter to **Select from all options**.
    - Select di **Virtual machine size** to **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.pcm.png)

1. Select **Next**.

1. Do di following tasks:

    - Enter **Compute name**. E gats be unique name.
    - Select **Minimum number of nodes** to **0**.
    - Select **Maximum number of nodes** to **1**.
    - Select **Idle seconds before scale down** to **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.pcm.png)

1. Select **Create**.

#### Fine-tune di Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select di Azure Machine Learning workspace wey you don create.

    ![Select workspace wey you create.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.pcm.png)

1. Do di following tasks:

    - Select **Model catalog** from di left side tab.
    - Type *phi-3-mini-4k* for di **search bar** and select **Phi-3-mini-4k-instruct** from di options wey go show.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.pcm.png)

1. Select **Fine-tune** from di navigation menu.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.pcm.png)

1. Do di following tasks:

    - Select **Select task type** to **Chat completion**.
    - Select **+ Select data** to upload **Training data**.
    - Select di Validation data upload type to **Provide different validation data**.
    - Select **+ Select data** to upload **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.pcm.png)

> [!TIP]
>
> You fit select **Advanced settings** to customize things like **learning_rate** and **lr_scheduler_type** to make fine-tuning process better based on wetin you need.

1. Select **Finish**.

1. For dis exercise, you don successfully fine-tune di Phi-3 model using Azure Machine Learning. Abeg note say di fine-tuning process fit take plenty time. After you run di fine-tuning job, you go need wait till e complete. You fit monitor di status of di fine-tuning job by waka go Jobs tab for left side of your Azure Machine Learning Workspace. For di next series, you go deploy di fine-tuned model and connect am with Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1.pcm.png)

### Deploy di fine-tuned Phi-3 model

To join di fine-tuned Phi-3 model with Prompt flow, you go need deploy di model make e dey available for real-time inference. Dis process involve to register di model, create online endpoint, and deploy di model.

For dis exercise, you go:

- Register di fine-tuned model inside di Azure Machine Learning workspace.
- Create online endpoint.
- Deploy di registered fine-tuned Phi-3 model.

#### Register di fine-tuned model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select di Azure Machine Learning workspace wey you create.

    ![Select workspace wey you create.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.pcm.png)

1. Select **Models** from di left side tab.
1. Select **+ Register**.
1. Select **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.pcm.png)

1. Select di job wey you create.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.pcm.png)

1. Select **Next**.

1. Select **Model type** to **MLflow**.

1. Make sure say **Job output** dey selected; e suppose select automatically.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.pcm.png)

2. Select **Next**.

3. Select **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.pcm.png)

4. You fit see your registered model by waka go **Models** menu from left side tab.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.pcm.png)

#### Deploy di fine-tuned model

1. Waka go di Azure Machine Learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

1. Select **Real-time endpoints** from di navigation menu.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.pcm.png)

1. Select **Create**.

1. Select di registered model wey you create.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.pcm.png)

1. Select **Select**.

1. Do di following tasks:

    - Select **Virtual machine** to *Standard_NC6s_v3*.
    - Select di **Instance count** wey you wan use. For example, *1*.
    - Select **Endpoint** to **New** to create new endpoint.
    - Enter **Endpoint name**. E gats be unique name.
    - Enter **Deployment name**. E gats be unique name.

    ![Fill di deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.pcm.png)

1. Select **Deploy**.

> [!WARNING]
> To avoid extra charges for your account, make sure say you delete di endpoint wey you create for Azure Machine Learning workspace.
>

#### Check deployment status inside Azure Machine Learning Workspace

1. Waka go Azure Machine Learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

1. Select di endpoint wey you create.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.pcm.png)

1. For dis page, you fit manage di endpoints during di deployment process.

> [!NOTE]
> Once di deployment don complete, make sure say **Live traffic** dey set to **100%**. If e never reach, select **Update traffic** to adjust di traffic settings. Note say you no fit test di model if di traffic set to 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.pcm.png)
>

## Scenario 3: Join am with Prompt flow and Chat with your custom model inside Azure AI Foundry

### Join di custom Phi-3 model with Prompt flow

After you don successfully deploy your fine-tuned model, you fit now join am with Prompt Flow to use your model for real-time applications, to enable plenty interactive tasks with your custom Phi-3 model.

For dis exercise, you go:

- Create Azure AI Foundry Hub.
- Create Azure AI Foundry Project.
- Create Prompt flow.
- Add custom connection for di fine-tuned Phi-3 model.
- Set Prompt flow to chat with your custom Phi-3 model

> [!NOTE]
> You fit also join am with Promptflow using Azure ML Studio. Di same joining process fit apply for Azure ML Studio.

#### Create Azure AI Foundry Hub

You gats create Hub before you create Project. Hub dey act like Resource Group, e help you organize and manage multiple Projects inside Azure AI Foundry.

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Select **All hubs** from di left side tab.

1. Select **+ New hub** from di navigation menu.
    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.pcm.png)

1. Make dis tins:

    - Put **Hub name**. E must be unique value.
    - Choose your Azure **Subscription**.
    - Choose the **Resource group** wey you go use (make new one if e no dey).
    - Choose the **Location** wey you want use.
    - Choose the **Connect Azure AI Services** wey you go use (make new one if e no dey).
    - Choose **Connect Azure AI Search** make e **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.pcm.png)

1. Choose **Next**.

#### Create Azure AI Foundry Project

1. For the Hub wey you create, choose **All projects** from left side tab.

1. Choose **+ New project** from navigation menu.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.pcm.png)

1. Put **Project name**. E must be unique value.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.pcm.png)

1. Choose **Create a project**.

#### Add a custom connection for the fine-tuned Phi-3 model

To join your custom Phi-3 model with Prompt flow, you need save the model's endpoint and key inside custom connection. Dis setup go make sure say you fit access your custom Phi-3 model for Prompt flow.

#### Set api key and endpoint uri of the fine-tuned Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Go meet the Azure Machine learning workspace wey you create.

1. Choose **Endpoints** from left side tab.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.pcm.png)

1. Choose endpoint wey you create.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.pcm.png)

1. Choose **Consume** from navigation menu.

1. Copy your **REST endpoint** and **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.pcm.png)

#### Add the Custom Connection

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Go enter the Azure AI Foundry project wey you create.

1. For the Project wey you create, choose **Settings** from left side tab.

1. Choose **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.pcm.png)

1. Choose **Custom keys** from navigation menu.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.pcm.png)

1. Make dis tins:

    - Choose **+ Add key value pairs**.
    - For key name, enter **endpoint** then paste the endpoint wey you copy from Azure ML Studio enter the value field.
    - Choose **+ Add key value pairs** again.
    - For key name, enter **key** then paste the key wey you copy from Azure ML Studio enter the value field.
    - After you add the keys, choose **is secret** to make sure say the key no go show.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.pcm.png)

1. Choose **Add connection**.

#### Create Prompt flow

You don add custom connection for Azure AI Foundry. Now, make we create Prompt flow with this steps. Then, you go connect this Prompt flow to the custom connection so you fit use the fine-tuned model inside the Prompt flow.

1. Go the Azure AI Foundry project wey you create.

1. Choose **Prompt flow** from left side tab.

1. Choose **+ Create** from navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.pcm.png)

1. Choose **Chat flow** from navigation menu.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.pcm.png)

1. Put **Folder name** wey you want use.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.pcm.png)

2. Choose **Create**.

#### Set up Prompt flow to chat with your custom Phi-3 model

You need join the fine-tuned Phi-3 model enter Prompt flow. But the Prompt flow wey dey already no design for dis kain work. So, you need redesign the Prompt flow to make am fit join the custom model.

1. For the Prompt flow, do dis to rebuild the existing flow:

    - Choose **Raw file mode**.
    - Delete all the kode wey dey for *flow.dag.yml* file.
    - Add dis kode inside *flow.dag.yml* file.

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

    - Choose **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.pcm.png)

1. Add dis kode inside *integrate_with_promptflow.py* file to use the custom Phi-3 model for Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Setup for logging
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

        # "connection" na the name of Custom Connection, "endpoint", "key" be the keys for the Custom Connection
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
            
            # Make you log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.pcm.png)

> [!NOTE]
> For detailed information on how to use Prompt flow inside Azure AI Foundry, you fit check [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Choose **Chat input**, then **Chat output** to enable chat with your model.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.pcm.png)

1. Now you ready to chat with your custom Phi-3 model. For the next exercise, you go learn how to start Prompt flow and use am to chat with your fine-tuned Phi-3 model.

> [!NOTE]
>
> The rebuilt flow go look like this picture below:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.pcm.png)
>

### Chat with your custom Phi-3 model

Now wey you don fine-tune and join your custom Phi-3 model with Prompt flow, you ready to start to dey interact with am. This exercise go show you how to set up and start chat with your model using Prompt flow. If you follow the steps well, you go fit use all the powers of your fine-tuned Phi-3 model for different tasks and conversation.

- Chat with your custom Phi-3 model using Prompt flow.

#### Start Prompt flow

1. Choose **Start compute sessions** to start Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.pcm.png)

1. Choose **Validate and parse input** to renew parameters.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.pcm.png)

1. Choose the **Value** of the **connection** to the custom connection wey you create. For example, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.pcm.png)

#### Chat with your custom model

1. Choose **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.pcm.png)

1. See example results: Now you fit chat with your custom Phi-3 model. E good make you ask questions based on the data wey them use do fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.pcm.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automated translation fit get some wahala or mistakes. Di original document wey e dey for im correct language na di main correct source. If na important matter, e better make person wey sabi human translation do am. We no go responsible for any kind misunderstanding or wrong meaning wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->