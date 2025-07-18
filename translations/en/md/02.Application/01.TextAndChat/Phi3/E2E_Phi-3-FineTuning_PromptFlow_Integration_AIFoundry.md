<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T00:55:08+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "en"
}
-->
# Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Foundry

This end-to-end (E2E) sample is based on the guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community. It walks you through the process of fine-tuning, deploying, and integrating custom Phi-3 models with Prompt flow in Azure AI Foundry.  
Unlike the E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", which involved running code locally, this tutorial focuses entirely on fine-tuning and integrating your model within Azure AI / ML Studio.

## Overview

In this E2E sample, you will learn how to fine-tune the Phi-3 model and integrate it with Prompt flow in Azure AI Foundry. Using Azure AI / ML Studio, you will set up a workflow for deploying and using custom AI models. This E2E sample is divided into three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**

**Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry**

Here is an overview of this E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.en.png)

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

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.en.png)

2. Select **+ Create** from the navigation menu.

3. Select **New workspace** from the navigation menu.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.en.png)

4. Complete the following:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (create a new one if needed).
    - Enter a **Workspace Name**. It must be unique.
    - Select the **Region** you'd like to use.
    - Select the **Storage account** to use (create a new one if needed).
    - Select the **Key vault** to use (create a new one if needed).
    - Select the **Application insights** to use (create a new one if needed).
    - Select the **Container registry** to use (create a new one if needed).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.en.png)

5. Select **Review + Create**.

6. Select **Create**.

### Request GPU quotas in Azure Subscription

In this tutorial, you will fine-tune and deploy a Phi-3 model using GPUs. For fine-tuning, you will use the *Standard_NC24ads_A100_v4* GPU, which requires a quota request. For deployment, you will use the *Standard_NC6s_v3* GPU, which also requires a quota request.

> [!NOTE]
>
> Only Pay-As-You-Go subscriptions (the standard subscription type) are eligible for GPU allocation; benefit subscriptions are not currently supported.
>

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. To request *Standard NCADSA100v4 Family* quota, do the following:

    - Select **Quota** from the left side tab.
    - Select the **Virtual machine family** to use. For example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC24ads_A100_v4* GPU.
    - Select **Request quota** from the navigation menu.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.en.png)

    - On the Request quota page, enter the **New cores limit** you'd like to request. For example, 24.
    - On the Request quota page, select **Submit** to request the GPU quota.

1. To request *Standard NCSv3 Family* quota, do the following:

    - Select **Quota** from the left side tab.
    - Select the **Virtual machine family** to use. For example, select **Standard NCSv3 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC6s_v3* GPU.
    - Select **Request quota** from the navigation menu.
    - On the Request quota page, enter the **New cores limit** you'd like to request. For example, 24.
    - On the Request quota page, select **Submit** to request the GPU quota.

### Add role assignment

To fine-tune and deploy your models, you first need to create a User Assigned Managed Identity (UAI) and assign it the necessary permissions. This UAI will be used for authentication during deployment.

#### Create User Assigned Managed Identity (UAI)

1. Type *managed identities* in the **search bar** at the top of the portal page and select **Managed Identities** from the options that appear.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.en.png)

1. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.en.png)

1. Complete the following:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (create a new one if needed).
    - Select the **Region** you'd like to use.
    - Enter a **Name**. It must be unique.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.en.png)

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Navigate to the Managed Identity resource you created.

1. Select **Azure role assignments** from the left side tab.

1. Select **+ Add role assignment** from the navigation menu.

1. On the Add role assignment page, complete the following:
    - Set the **Scope** to **Resource group**.
    - Select your Azure **Subscription**.
    - Select the **Resource group** to use.
    - Select the **Role** as **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.en.png)

2. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* in the **search bar** at the top of the portal page and select **Storage accounts** from the options that appear.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.en.png)

1. Select the storage account associated with the Azure Machine Learning workspace you created. For example, *finetunephistorage*.

1. To navigate to the Add role assignment page, do the following:

    - Go to the Azure Storage account you created.
    - Select **Access Control (IAM)** from the left side tab.
    - Select **+ Add** from the navigation menu.
    - Select **Add role assignment** from the navigation menu.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.en.png)

1. On the Add role assignment page, complete the following:

    - In the Role search bar, type *Storage Blob Data Reader* and select **Storage Blob Data Reader** from the options.
    - Select **Next**.
    - On the Members page, set **Assign access to** to **Managed identity**.
    - Select **+ Select members**.
    - On the Select managed identities page, select your Azure **Subscription**.
    - Select the **Managed identity** option.
    - Select the Managed Identity you created. For example, *finetunephi-managedidentity*.
    - Select **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.en.png)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* in the **search bar** at the top of the portal page and select **Container registries** from the options that appear.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.en.png)

1. Select the container registry associated with the Azure Machine Learning workspace. For example, *finetunephicontainerregistry*.

1. To navigate to the Add role assignment page, do the following:

    - Select **Access Control (IAM)** from the left side tab.
    - Select **+ Add** from the navigation menu.
    - Select **Add role assignment** from the navigation menu.

1. On the Add role assignment page, complete the following:

    - In the Role search bar, type *AcrPull* and select **AcrPull** from the options.
    - Select **Next**.
    - On the Members page, set **Assign access to** to **Managed identity**.
    - Select **+ Select members**.
    - On the Select managed identities page, select your Azure **Subscription**.
    - Select the **Managed identity** option.
    - Select the Managed Identity you created. For example, *finetunephi-managedidentity*.
    - Select **Select**.
    - Select **Review + assign**.

### Set up project

To download the datasets needed for fine-tuning, you will set up a local environment.

In this exercise, you will:

- Create a folder to work in.
- Create a virtual environment.
- Install the required packages.
- Create a *download_dataset.py* file to download the dataset.

#### Create a folder to work in

1. Open a terminal window and run the following command to create a folder named *finetune-phi* in the default path.

    ```console
    mkdir finetune-phi
    ```

2. Run the following command in your terminal to navigate to the *finetune-phi* folder you created.
#### Create a virtual environment

1. Run the following command in your terminal to create a virtual environment named *.venv*.

2. Run the following command in your terminal to activate the virtual environment.

> [!NOTE]
> If successful, you should see *(.venv)* before the command prompt.

#### Install the required packages

1. Run the following commands in your terminal to install the required packages.

#### Create `download_dataset.py`

> [!NOTE]
> Complete folder structure:
>
> 1. Open **Visual Studio Code**.

1. Select **File** from the menu bar.

1. Select **Open Folder**.

1. Choose the *finetune-phi* folder you created, located at *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.en.png)

1. In the left pane of Visual Studio Code, right-click and select **New File** to create a new file named *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.en.png)

### Prepare dataset for fine-tuning

In this exercise, you will run the *download_dataset.py* file to download the *ultrachat_200k* datasets to your local environment. You will then use these datasets to fine-tune the Phi-3 model in Azure Machine Learning.

In this exercise, you will:

- Add code to the *download_dataset.py* file to download the datasets.
- Run the *download_dataset.py* file to download datasets to your local environment.

#### Download your dataset using *download_dataset.py*

1. Open the *download_dataset.py* file in Visual Studio Code.

1. Add the following code into the *download_dataset.py* file.

1. Run the following command in your terminal to execute the script and download the dataset to your local environment.

1. Verify that the datasets were saved successfully to your local *finetune-phi/data* directory.

> [!NOTE]
>
> #### Note on dataset size and fine-tuning time
>
> In this tutorial, you use only 1% of the dataset (`split='train[:1%]'`). This significantly reduces the amount of data, speeding up both the upload and fine-tuning processes. You can adjust the percentage to find the right balance between training time and model performance. Using a smaller subset of the dataset reduces the time required for fine-tuning, making the process more manageable for a tutorial.

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Fine-tune the Phi-3 model

In this exercise, you will fine-tune the Phi-3 model in Azure Machine Learning Studio.

In this exercise, you will:

- Create a compute cluster for fine-tuning.
- Fine-tune the Phi-3 model in Azure Machine Learning Studio.

#### Create compute cluster for fine-tuning

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select **Compute** from the left side tab.

1. Select **Compute clusters** from the navigation menu.

1. Select **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.en.png)

1. Complete the following:

    - Choose the **Region** you want to use.
    - Set the **Virtual machine tier** to **Dedicated**.
    - Set the **Virtual machine type** to **GPU**.
    - Set the **Virtual machine size** filter to **Select from all options**.
    - Choose the **Virtual machine size** as **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.en.png)

1. Select **Next**.

1. Complete the following:

    - Enter a unique **Compute name**.
    - Set the **Minimum number of nodes** to **0**.
    - Set the **Maximum number of nodes** to **1**.
    - Set the **Idle seconds before scale down** to **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.en.png)

1. Select **Create**.

#### Fine-tune the Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select the Azure Machine Learning workspace you created.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.en.png)

1. Complete the following:

    - Select **Model catalog** from the left side tab.
    - Type *phi-3-mini-4k* in the **search bar** and select **Phi-3-mini-4k-instruct** from the options.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.en.png)

1. Select **Fine-tune** from the navigation menu.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.en.png)

1. Complete the following:

    - Set **Select task type** to **Chat completion**.
    - Select **+ Select data** to upload **Training data**.
    - Set the Validation data upload type to **Provide different validation data**.
    - Select **+ Select data** to upload **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.en.png)

    > [!TIP]
    >
    > You can select **Advanced settings** to customize configurations such as **learning_rate** and **lr_scheduler_type** to optimize the fine-tuning process according to your specific needs.

1. Select **Finish**.

1. In this exercise, you have successfully fine-tuned the Phi-3 model using Azure Machine Learning. Please note that fine-tuning can take a significant amount of time. After starting the fine-tuning job, wait for it to complete. You can monitor the job status by going to the Jobs tab on the left side of your Azure Machine Learning Workspace. In the next part, you will deploy the fine-tuned model and integrate it with Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.en.png)

### Deploy the fine-tuned Phi-3 model

To integrate the fine-tuned Phi-3 model with Prompt flow, you need to deploy the model so it can be accessed for real-time inference. This involves registering the model, creating an online endpoint, and deploying the model.

In this exercise, you will:

- Register the fine-tuned model in the Azure Machine Learning workspace.
- Create an online endpoint.
- Deploy the registered fine-tuned Phi-3 model.

#### Register the fine-tuned model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select the Azure Machine Learning workspace you created.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.en.png)

1. Select **Models** from the left side tab.

1. Select **+ Register**.

1. Select **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.en.png)

1. Select the job you created.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.en.png)

1. Select **Next**.

1. Set **Model type** to **MLflow**.

1. Ensure **Job output** is selected; it should be selected automatically.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.en.png)

2. Select **Next**.

3. Select **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.en.png)

4. You can view your registered model by going to the **Models** menu on the left side tab.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.en.png)

#### Deploy the fine-tuned model

1. Go to the Azure Machine Learning workspace you created.

1. Select **Endpoints** from the left side tab.

1. Select **Real-time endpoints** from the navigation menu.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.en.png)

1. Select **Create**.

1. Select the registered model you created.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.en.png)

1. Select **Select**.

1. Complete the following:

    - Set **Virtual machine** to *Standard_NC6s_v3*.
    - Choose the **Instance count** you want to use, for example, *1*.
    - Set **Endpoint** to **New** to create a new endpoint.
    - Enter a unique **Endpoint name**.
    - Enter a unique **Deployment name**.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.en.png)

1. Select **Deploy**.

> [!WARNING]
> To avoid extra charges, be sure to delete the endpoint you created in the Azure Machine Learning workspace when you no longer need it.

#### Check deployment status in Azure Machine Learning Workspace

1. Go to the Azure Machine Learning workspace you created.

1. Select **Endpoints** from the left side tab.

1. Select the endpoint you created.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.en.png)

1. On this page, you can manage the endpoints during deployment.

> [!NOTE]
> Once deployment is complete, make sure **Live traffic** is set to **100%**. If not, select **Update traffic** to adjust the settings. You cannot test the model if traffic is set to 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.en.png)
>

## Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry

### Integrate the custom Phi-3 model with Prompt flow

After successfully deploying your fine-tuned model, you can now integrate it with Prompt Flow to use your model in real-time applications, enabling a variety of interactive tasks with your custom Phi-3 model.

In this exercise, you will:

- Create an Azure AI Foundry Hub.
- Create an Azure AI Foundry Project.
- Create a Prompt flow.
- Add a custom connection for the fine-tuned Phi-3 model.
- Set up Prompt flow to chat with your custom Phi-3 model.
> [!NOTE]  
> You can also integrate with Promptflow using Azure ML Studio. The same integration process applies to Azure ML Studio.
#### Create Azure AI Foundry Hub

You need to create a Hub before creating the Project. A Hub functions like a Resource Group, allowing you to organize and manage multiple Projects within Azure AI Foundry.

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Select **All hubs** from the left side tab.

1. Select **+ New hub** from the navigation menu.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.en.png)

1. Complete the following:

    - Enter a **Hub name**. It must be unique.
    - Select your Azure **Subscription**.
    - Choose the **Resource group** to use (create a new one if needed).
    - Select the **Location** you want to use.
    - Choose the **Connect Azure AI Services** to use (create a new one if needed).
    - For **Connect Azure AI Search**, select **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.en.png)

1. Select **Next**.

#### Create Azure AI Foundry Project

1. In the Hub you created, select **All projects** from the left side tab.

1. Select **+ New project** from the navigation menu.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.en.png)

1. Enter a **Project name**. It must be unique.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.en.png)

1. Select **Create a project**.

#### Add a custom connection for the fine-tuned Phi-3 model

To connect your custom Phi-3 model with Prompt flow, you need to save the model’s endpoint and key in a custom connection. This setup ensures Prompt flow can access your custom Phi-3 model.

#### Set API key and endpoint URI of the fine-tuned Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Go to the Azure Machine Learning workspace you created.

1. Select **Endpoints** from the left side tab.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.en.png)

1. Select the endpoint you created.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.en.png)

1. Select **Consume** from the navigation menu.

1. Copy your **REST endpoint** and **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.en.png)

#### Add the Custom Connection

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigate to the Azure AI Foundry project you created.

1. In your Project, select **Settings** from the left side tab.

1. Select **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.en.png)

1. Select **Custom keys** from the navigation menu.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.en.png)

1. Complete the following:

    - Select **+ Add key value pairs**.
    - For the key name, enter **endpoint** and paste the endpoint you copied from Azure ML Studio into the value field.
    - Select **+ Add key value pairs** again.
    - For the key name, enter **key** and paste the key you copied from Azure ML Studio into the value field.
    - After adding the keys, select **is secret** to keep the key hidden.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.en.png)

1. Select **Add connection**.

#### Create Prompt flow

You have added a custom connection in Azure AI Foundry. Now, let’s create a Prompt flow using the following steps. Then, you will link this Prompt flow to the custom connection so you can use the fine-tuned model within the Prompt flow.

1. Navigate to the Azure AI Foundry project you created.

1. Select **Prompt flow** from the left side tab.

1. Select **+ Create** from the navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.en.png)

1. Select **Chat flow** from the navigation menu.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.en.png)

1. Enter a **Folder name** to use.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.en.png)

2. Select **Create**.

#### Set up Prompt flow to chat with your custom Phi-3 model

You need to integrate the fine-tuned Phi-3 model into a Prompt flow. However, the existing Prompt flow isn’t designed for this, so you must redesign it to enable integration with your custom model.

1. In the Prompt flow, rebuild the existing flow by doing the following:

    - Select **Raw file mode**.
    - Delete all existing code in the *flow.dag.yml* file.
    - Add the following code to the *flow.dag.yml* file.

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.en.png)

1. Add the following code to the *integrate_with_promptflow.py* file to use the custom Phi-3 model in Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.en.png)

> [!NOTE]
> For more detailed information on using Prompt flow in Azure AI Foundry, see [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Select **Chat input** and **Chat output** to enable chatting with your model.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.en.png)

1. Now you’re ready to chat with your custom Phi-3 model. In the next exercise, you’ll learn how to start Prompt flow and use it to chat with your fine-tuned Phi-3 model.

> [!NOTE]
>
> The rebuilt flow should look like the image below:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.en.png)
>

### Chat with your custom Phi-3 model

Now that you’ve fine-tuned and integrated your custom Phi-3 model with Prompt flow, you’re ready to start interacting with it. This exercise will guide you through setting up and initiating a chat with your model using Prompt flow. By following these steps, you’ll be able to fully leverage your fine-tuned Phi-3 model for various tasks and conversations.

- Chat with your custom Phi-3 model using Prompt flow.

#### Start Prompt flow

1. Select **Start compute sessions** to launch Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.en.png)

1. Select **Validate and parse input** to refresh parameters.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.en.png)

1. Select the **Value** of the **connection** to the custom connection you created, for example, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.en.png)

#### Chat with your custom model

1. Select **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.en.png)

1. Here’s an example of the results: You can now chat with your custom Phi-3 model. It’s recommended to ask questions based on the data used for fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.en.png)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.