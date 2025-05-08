<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-07T14:18:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "mo"
}
-->
# Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Foundry

This end-to-end (E2E) sample is based on the guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community. It introduces the processes of fine-tuning, deploying, and integrating custom Phi-3 models with Prompt flow in Azure AI Foundry.  
Unlike the E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", which involved running code locally, this tutorial focuses entirely on fine-tuning and integrating your model within the Azure AI / ML Studio.

## Overview

In this E2E sample, you will learn how to fine-tune the Phi-3 model and integrate it with Prompt flow in Azure AI Foundry. By leveraging Azure AI / ML Studio, you will establish a workflow for deploying and utilizing custom AI models. This E2E sample is divided into three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**

**Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry**

Here is an overview of this E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.mo.png)

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

1. Type *azure machine learning* in the **search bar** at the top of the portal page and select **Azure Machine Learning** from the options that appear.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.mo.png)

2. Select **+ Create** from the navigation menu.

3. Select **New workspace** from the navigation menu.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.mo.png)

4. Complete the following:

    - Select your Azure **Subscription**.
    - Choose the **Resource group** to use (or create a new one).
    - Enter a unique **Workspace Name**.
    - Select the **Region** you want to use.
    - Choose the **Storage account** to use (or create a new one).
    - Select the **Key vault** to use (or create a new one).
    - Choose the **Application insights** to use (or create a new one).
    - Select the **Container registry** to use (or create a new one).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.mo.png)

5. Select **Review + Create**.

6. Select **Create**.

### Request GPU quotas in Azure Subscription

In this tutorial, you will fine-tune and deploy a Phi-3 model using GPUs. For fine-tuning, you will use the *Standard_NC24ads_A100_v4* GPU, which requires a quota request. For deployment, you will use the *Standard_NC6s_v3* GPU, which also requires a quota request.

> [!NOTE]
>
> Only Pay-As-You-Go subscriptions (standard subscription type) are eligible for GPU allocation; benefit subscriptions are not currently supported.
>

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

2. To request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** from the left sidebar.
    - Choose the **Virtual machine family**. For example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC24ads_A100_v4* GPU.
    - Click **Request quota** from the navigation menu.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.mo.png)

    - On the Request quota page, enter the **New cores limit** you want, e.g., 24.
    - Click **Submit** to request the GPU quota.

3. To request *Standard NCSv3 Family* quota:

    - Select **Quota** from the left sidebar.
    - Choose the **Virtual machine family**. For example, select **Standard NCSv3 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC6s_v3* GPU.
    - Click **Request quota** from the navigation menu.
    - Enter the **New cores limit**, e.g., 24.
    - Click **Submit** to request the GPU quota.

### Add role assignment

To fine-tune and deploy your models, you first need to create a User Assigned Managed Identity (UAI) and assign it the proper permissions. This UAI will be used for authentication during deployment.

#### Create User Assigned Managed Identity(UAI)

1. Type *managed identities* in the **search bar** at the top of the portal and select **Managed Identities**.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.mo.png)

2. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.mo.png)

3. Complete the following:

    - Select your Azure **Subscription**.
    - Choose the **Resource group** to use (or create a new one).
    - Select the **Region**.
    - Enter a unique **Name**.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.mo.png)

4. Select **Review + create**.

5. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Navigate to the Managed Identity resource you created.

2. Select **Azure role assignments** from the left sidebar.

3. Click **+Add role assignment** from the navigation menu.

4. On the Add role assignment page, complete the following:

    - Set **Scope** to **Resource group**.
    - Select your Azure **Subscription**.
    - Choose the **Resource group**.
    - Select the **Role** as **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.mo.png)

5. Click **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* in the **search bar** and select **Storage accounts**.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.mo.png)

2. Select the storage account linked to your Azure Machine Learning workspace, e.g., *finetunephistorage*.

3. To open Add role assignment page:

    - Navigate to the storage account.
    - Select **Access Control (IAM)** from the left sidebar.
    - Click **+ Add** from the navigation menu.
    - Select **Add role assignment**.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.mo.png)

4. On the Add role assignment page:

    - Search for *Storage Blob Data Reader* in the **search bar** and select it.
    - Click **Next**.
    - Under **Assign access to**, select **Managed identity**.
    - Click **+ Select members**.
    - Choose your Azure **Subscription**.
    - Select the **Managed identity** type.
    - Choose the Managed Identity you created, e.g., *finetunephi-managedidentity*.
    - Click **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.mo.png)

5. Click **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* in the **search bar** and select **Container registries**.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.mo.png)

2. Select the container registry linked to your Azure Machine Learning workspace, e.g., *finetunephicontainerregistry*.

3. To open Add role assignment page:

    - Select **Access Control (IAM)** from the left sidebar.
    - Click **+ Add**.
    - Select **Add role assignment**.

4. On the Add role assignment page:

    - Search for *AcrPull* in the **search bar** and select it.
    - Click **Next**.
    - Under **Assign access to**, select **Managed identity**.
    - Click **+ Select members**.
    - Choose your Azure **Subscription**.
    - Select the **Managed identity** type.
    - Choose the Managed Identity you created, e.g., *finetunephi-managedidentity*.
    - Click **Select**.
    - Click **Review + assign**.

### Set up project

To download the datasets needed for fine-tuning, you will set up a local environment.

In this exercise, you will:

- Create a folder to work in.
- Create a virtual environment.
- Install the required packages.
- Create a *download_dataset.py* file to download the dataset.

#### Create a folder to work in

1. Open a terminal and run the following command to create a folder named *finetune-phi* in the default path.

    ```console
    mkdir finetune-phi
    ```

2. Run the following command to navigate to the *finetune-phi* folder.

    ```console
    cd finetune-phi
    ```

#### Create a virtual environment

1. Run the following command to create a virtual environment named *.venv*.

    ```console
    python -m venv .venv
    ```

2. Run the following command to activate the virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> If successful, you should see *(.venv)* before the command prompt.

#### Install the required packages

1. Run the following commands to install the required packages.

    ```console
    pip install datasets==2.19.1
    ```

#### Create `download_dataset.py`

> [!NOTE]
> Complete folder structure:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Open **Visual Studio Code**.

2. Select **File** from the menu bar.

3. Select **Open Folder**.

4. Choose the *finetune-phi* folder you created, located at *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.mo.png)

5. In the left pane, right-click and select **New File** to create *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.mo.png)

### Prepare dataset for fine-tuning

In this exercise, you will run *download_dataset.py* to download the *ultrachat_200k* datasets to your local environment. You will then use this dataset to fine-tune the Phi-3 model in Azure Machine Learning.

You will:

- Add code to *download_dataset.py* to download the dataset.
- Run *download_dataset.py* to download the dataset locally.

#### Download your dataset using *download_dataset.py*

1. Open *download_dataset.py* in Visual Studio Code.

2. Add the following code to the file.

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

3. Run the following command in your terminal to execute the script and download the dataset.

    ```console
    python download_dataset.py
    ```

4. Verify that the datasets were successfully saved to your local *finetune-phi/data* directory.

> [!NOTE]
>
> #### Note on dataset size and fine-tuning time
>
> In this tutorial, you use only 1% of the dataset (`split='train[:1%]'`). This significantly reduces data size, speeding both upload and fine-tuning. You can adjust this percentage to balance training time and model quality. Using a smaller subset makes fine-tuning faster and more manageable for this tutorial.

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Fine-tune the Phi-3 model

In this exercise, you will fine-tune the Phi-3 model in Azure Machine Learning Studio.

You will:

- Create a compute cluster for fine-tuning.
- Fine-tune the Phi-3 model in Azure Machine Learning Studio.

#### Create compute cluster for fine-tuning
1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select **Compute** from the left side tab.

1. Select **Compute clusters** from the navigation menu.

1. Select **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.mo.png)

1. Perform the following tasks:

    - Select the **Region** you'd like to use.
    - Select the **Virtual machine tier** to **Dedicated**.
    - Select the **Virtual machine type** to **GPU**.
    - Select the **Virtual machine size** filter to **Select from all options**.
    - Select the **Virtual machine size** to **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.mo.png)

1. Select **Next**.

1. Perform the following tasks:

    - Enter **Compute name**. It must be a unique value.
    - Select the **Minimum number of nodes** to **0**.
    - Select the **Maximum number of nodes** to **1**.
    - Select the **Idle seconds before scale down** to **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.mo.png)

1. Select **Create**.

#### Fine-tune the Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select the Azure Macnine Learning workspace that you created.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.mo.png)

1. Perform the following tasks:

    - Select **Model catalog** from the left side tab.
    - Type *phi-3-mini-4k* in the **search bar** and select **Phi-3-mini-4k-instruct** from the options that appear.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.mo.png)

1. Select **Fine-tune** from the navigation menu.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.mo.png)

1. Perform the following tasks:

    - Select **Select task type** to **Chat completion**.
    - Select **+ Select data** to upload **Traning data**.
    - Select the Validation data upload type to **Provide different validation data**.
    - Select **+ Select data** to upload **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.mo.png)

    > [!TIP]
    >
    > You can select **Advanced settings** to customize configurations such as **learning_rate** and **lr_scheduler_type** to optimize the fine-tuning process according to your specific needs.

1. Select **Finish**.

1. In this exercise, you successfully fine-tuned the Phi-3 model using Azure Machine Learning. Please note that the fine-tuning process can take a considerable amount of time. After running the fine-tuning job, you need to wait for it to complete. You can monitor the status of the fine-tuning job by navigating to the Jobs tab on the left side of your Azure Machine Learning Workspace. In the next series, you will deploy the fine-tuned model and integrate it with Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.mo.png)

### Deploy the fine-tuned Phi-3 model

To integrate the fine-tuned Phi-3 model with Prompt flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

In this exercise, you will:

- Register the fine-tuned model in the Azure Machine Learning workspace.
- Create an online endpoint.
- Deploy the registered fine-tuned Phi-3 model.

#### Register the fine-tuned model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select the Azure Macnine Learning workspace that you created.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.mo.png)

1. Select **Models** from the left side tab.
1. Select **+ Register**.
1. Select **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.mo.png)

1. Select the job that you created.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.mo.png)

1. Select **Next**.

1. Select **Model type** to **MLflow**.

1. Ensure that **Job output** is selected; it should be automatically selected.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.mo.png)

2. Select **Next**.

3. Select **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.mo.png)

4. You can view your registered model by navigating to the **Models** menu from the left side tab.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.mo.png)

#### Deploy the fine-tuned model

1. Navigate to the Azure Macnine Learning workspace that you created.

1. Select **Endpoints** from the left side tab.

1. Select **Real-time endpoints** from the navigation menu.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.mo.png)

1. Select **Create**.

1. select the registered model that you created.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.mo.png)

1. Select **Select**.

1. Perform the following tasks:

    - Select **Virtual machine** to *Standard_NC6s_v3*.
    - Select the **Instance count** you'd like to use. For example, *1*.
    - Select the **Endpoint** to **New** to create an endpoint.
    - Enter **Endpoint name**. It must be a unique value.
    - Enter **Deployment name**. It must be a unique value.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.mo.png)

1. Select **Deploy**.

> [!WARNING]
> To avoid additional charges to your account, make sure to delete the created endpoint in the Azure Machine Learning workspace.
>

#### Check deployment status in Azure Machine Learning Workspace

1. Navigate to Azure Machine Learning workspace that you created.

1. Select **Endpoints** from the left side tab.

1. Select the endpoint that you created.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.mo.png)

1. On this page, you can manage the endpoints during the deployment process.

> [!NOTE]
> Once the deployment is complete, ensure that **Live traffic** is set to **100%**. If it is not, select **Update traffic** to adjust the traffic settings. Note that you cannot test the model if the traffic is set to 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.mo.png)
>

## Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry

### Integrate the custom Phi-3 model with Prompt flow

After successfully deploying your fine-tuned model, you can now integrate it with Prompt Flow to use your model in real-time applications, enabling a variety of interactive tasks with your custom Phi-3 model.

In this exercise, you will:

- Create Azure AI Foundry Hub.
- Create Azure AI Foundry Project.
- Create Prompt flow.
- Add a custom connection for the fine-tuned Phi-3 model.
- Set up Prompt flow to chat with your custom Phi-3 model

> [!NOTE]
> You can also integrate with Promptflow using Azure ML Studio. The same integration process can be applied to Azure ML Studio.

#### Create Azure AI Foundry Hub

You need to create a Hub before creating the Project. A Hub acts like a Resource Group, allowing you to organize and manage multiple Projects within Azure AI Foundry.

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Select **All hubs** from the left side tab.

1. Select **+ New hub** from the navigation menu.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.mo.png)

1. Perform the following tasks:

    - Enter **Hub name**. It must be a unique value.
    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (create a new one if needed).
    - Select the **Location** you'd like to use.
    - Select the **Connect Azure AI Services** to use (create a new one if needed).
    - Select **Connect Azure AI Search** to **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.mo.png)

1. Select **Next**.

#### Create Azure AI Foundry Project

1. In the Hub that you created, select **All projects** from the left side tab.

1. Select **+ New project** from the navigation menu.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.mo.png)

1. Enter **Project name**. It must be a unique value.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.mo.png)

1. Select **Create a project**.

#### Add a custom connection for the fine-tuned Phi-3 model

To integrate your custom Phi-3 model with Prompt flow, you need to save the model's endpoint and key in a custom connection. This setup ensures access to your custom Phi-3 model in Prompt flow.

#### Set api key and endpoint uri of the fine-tuned Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigate to the Azure Machine learning workspace that you created.

1. Select **Endpoints** from the left side tab.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.mo.png)

1. Select endpoint that you created.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.mo.png)

1. Select **Consume** from the navigation menu.

1. Copy your **REST endpoint** and **Primary key**.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.mo.png)

#### הוסף את החיבור המותאם אישית

1. בקר ב-[Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. נווט לפרויקט Azure AI Foundry שיצרת.

1. בפרויקט שיצרת, בחר ב**Settings** מהכרטיסייה בצד שמאל.

1. בחר ב**+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.mo.png)

1. בחר ב**Custom keys** מתפריט הניווט.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.mo.png)

1. בצע את הפעולות הבאות:

    - בחר ב**+ Add key value pairs**.
    - בשדה שם המפתח, הזן **endpoint** והדבק את ה-endpoint שהעתקת מ-Azure ML Studio בשדה הערך.
    - בחר שוב ב**+ Add key value pairs**.
    - בשדה שם המפתח, הזן **key** והדבק את המפתח שהעתקת מ-Azure ML Studio בשדה הערך.
    - לאחר הוספת המפתחות, סמן את **is secret** כדי למנוע חשיפת המפתח.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.mo.png)

1. בחר ב**Add connection**.

#### צור Prompt flow

הוספת חיבור מותאם אישית ב-Azure AI Foundry. כעת, ניצור Prompt flow באמצעות השלבים הבאים. לאחר מכן, תחבר את Prompt flow הזה לחיבור המותאם כדי שתוכל להשתמש במודל המותאם בתוך Prompt flow.

1. נווט לפרויקט Azure AI Foundry שיצרת.

1. בחר ב**Prompt flow** מהכרטיסייה בצד שמאל.

1. בחר ב**+ Create** מתפריט הניווט.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.mo.png)

1. בחר ב**Chat flow** מתפריט הניווט.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.mo.png)

1. הזן **Folder name** לשימוש.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.mo.png)

2. בחר ב**Create**.

#### הגדר Prompt flow לשיחה עם מודל Phi-3 המותאם אישית שלך

עליך לשלב את מודל Phi-3 המותאם בתוך Prompt flow. עם זאת, Prompt flow הקיים אינו מותאם למטרה זו. לכן, עליך לעצב מחדש את Prompt flow כדי לאפשר את שילוב המודל המותאם.

1. ב-Prompt flow, בצע את הפעולות הבאות כדי לבנות מחדש את ה-flow הקיים:

    - בחר ב**Raw file mode**.
    - מחק את כל הקוד הקיים בקובץ *flow.dag.yml*.
    - הוסף את הקוד הבא לקובץ *flow.dag.yml*.

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

    - בחר ב**Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.mo.png)

1. הוסף את הקוד הבא לקובץ *integrate_with_promptflow.py* כדי להשתמש במודל Phi-3 המותאם ב-Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.mo.png)

> [!NOTE]
> למידע מפורט יותר על שימוש ב-Prompt flow ב-Azure AI Foundry, ניתן לעיין ב-[Prompt flow ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. בחר ב**Chat input**, **Chat output** כדי לאפשר שיחה עם המודל שלך.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.mo.png)

1. כעת אתה מוכן לשוחח עם מודל Phi-3 המותאם שלך. בתרגיל הבא תלמד כיצד להפעיל את Prompt flow ולהשתמש בו לשיחה עם מודל Phi-3 המותאם שלך.

> [!NOTE]
>
> ה-flow שהוקם מחדש אמור להיראות כמו בתמונה למטה:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.mo.png)
>

### שוחח עם מודל Phi-3 המותאם שלך

כעת כשכיוונת ושילבת את מודל Phi-3 המותאם שלך עם Prompt flow, אתה מוכן להתחיל אינטראקציה איתו. תרגיל זה ינחה אותך בתהליך ההגדרה וההפעלה של שיחה עם המודל שלך באמצעות Prompt flow. בעקבות שלבים אלו תוכל למצות את כל היכולות של מודל Phi-3 המותאם שלך למשימות ושיחות שונות.

- שוחח עם מודל Phi-3 המותאם שלך באמצעות Prompt flow.

#### הפעל את Prompt flow

1. בחר ב**Start compute sessions** כדי להפעיל את Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.mo.png)

1. בחר ב**Validate and parse input** כדי לעדכן פרמטרים.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.mo.png)

1. בחר את **Value** של **connection** לחיבור המותאם שיצרת. לדוגמה, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.mo.png)

#### שוחח עם המודל המותאם שלך

1. בחר ב**Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.mo.png)

1. הנה דוגמה לתוצאות: כעת תוכל לשוחח עם מודל Phi-3 המותאם שלך. מומלץ לשאול שאלות המבוססות על הנתונים ששימשו לאימון המודל.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.mo.png)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.