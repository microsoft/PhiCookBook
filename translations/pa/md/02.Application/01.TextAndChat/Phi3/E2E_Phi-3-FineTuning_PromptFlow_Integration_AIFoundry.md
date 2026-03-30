# Fine-tune and Integrate custom Phi-3 models with Prompt flow in Microsoft Foundry

This end-to-end (E2E) sample is based on the guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community. It introduces the processes of fine-tuning, deploying, and integrating custom Phi-3 models with Prompt flow in Microsoft Foundry.
Unlike the E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", which involved running code locally, this tutorial focuses entirely on fine-tuning and integrating your model within the Azure AI / ML Studio.

## Overview

In this E2E sample, you will learn how to fine-tune the Phi-3 model and integrate it with Prompt flow in Microsoft Foundry. By leveraging Azure AI / ML Studio, you will establish a workflow for deploying and utilizing custom AI models. This E2E sample is divided into three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**

**Scenario 3: Integrate with Prompt flow and Chat with your custom model in Microsoft Foundry**

Here is an overview of this E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/pa/00-01-architecture.198ba0f1ae6d841a.webp)

### Table of Contents

1. **[Scenario 1: Set up Azure resources and Prepare for fine-tuning](#scenario-1-set-up-azure-resources-and-prepare-for-fine-tuning)**
    - [Create an Azure Machine Learning Workspace](#create-an-azure-machine-learning-workspace)
    - [Request GPU quotas in Azure Subscription](#request-gpu-quotas-in-azure-subscription)
    - [Add role assignment](#add-role-assignment)
    - [Set up project](#set-up-project)
    - [Prepare dataset for fine-tuning](#ਫਾਈਨ-ਟਿਊਨਿੰਗ-ਲਈ-ਡਾਟਾਸੈੱਟ-ਤਿਆਰ-ਕਰੋ)

1. **[Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio](#ਪਰਿਣਾਮ-2-phi-3-ਮਾਡਲ-ਦੀ-ਫਾਈਨ-ਟਿਊਨਿੰਗ-ਅਤੇ-azure-machine-learning-studio-ਵਿੱਚ-ਡਿਪਲਾਇ)**
    - [Fine-tune the Phi-3 model](#phi-3-ਮਾਡਲ-ਦੀ-ਫਾਈਨ-ਟਿਊਨਿੰਗ)
    - [Deploy the fine-tuned Phi-3 model](#ਫਾਈਨ-ਟਿਊਨ-ਕੀਤੇ-phi-3-ਮਾਡਲ-ਨੂੰ-ਡਿਪਲਾਇ-ਕਰੋ)

1. **[Scenario 3: Integrate with Prompt flow and Chat with your custom model in Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrate the custom Phi-3 model with Prompt flow](#ਕਸਟਮ-phi-3-ਮਾਡਲ-ਨੂੰ-prompt-flow-ਨਾਲ-ਇਕਜੁੱਟ-ਕਰੋ)
    - [Chat with your custom Phi-3 model](#ਆਪਣੇ-ਕਸਟਮ-phi-3-ਮਾਡਲ-ਨਾਲ-ਗੱਲਬਾਤ-ਕਰੋ)

## Scenario 1: Set up Azure resources and Prepare for fine-tuning

### Create an Azure Machine Learning Workspace

1. Type *azure machine learning* in the **search bar** at the top of the portal page and select **Azure Machine Learning** from the options that appear.

    ![Type azure machine learning.](../../../../../../translated_images/pa/01-01-type-azml.acae6c5455e67b4b.webp)

2. Select **+ Create** from the navigation menu.

3. Select **New workspace** from the navigation menu.

    ![Select new workspace.](../../../../../../translated_images/pa/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Perform the following tasks:

    - ਆਪਣਾ Azure **Subscription** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Resource group** ਚੁਣੋ (ਲੋੜ ਹੋਵਿਆਂ ਨਵਾਂ ਬਣਾਓ)।
    - **Workspace Name** ਦਰਜ ਕਰੋ। ਇਹ ਇਕ ਵਿਲੱਖਣ ਮੂਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - ਉਹ **Region** ਚੁਣੋ ਜਿਸਨੂੰ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ।
    - ਵਰਤੋਂ ਲਈ **Storage account** ਚੁਣੋ (ਲੋੜ ਹੋਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।
    - ਵਰਤੋਂ ਲਈ **Key vault** ਚੁਣੋ (ਲੋੜ ਹੋਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।
    - ਵਰਤੋਂ ਲਈ **Application insights** ਚੁਣੋ (ਲੋੜ ਹੋਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।
    - ਵਰਤੋਂ ਲਈ **Container registry** ਚੁਣੋ (ਲੋੜ ਹੋਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।

    ![Fill azure machine learning.](../../../../../../translated_images/pa/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. ਚੁਣੋ **Review + Create**।

6. ਚੁਣੋ **Create**।

### Request GPU quotas in Azure Subscription

ਇਸ ਟਿਊਟੋਰੀਅਲ ਵਿੱਚ, ਤੁਸੀਂ ਗ੍ਰਾਫਿਕਸ ਕਾਰਡ (GPU) ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਡਿਪਲੌਏ ਕਰਨਾ ਸਿਖੋਗੇ। ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ, ਤੁਸੀਂ *Standard_NC24ads_A100_v4* GPU ਦੀ ਵਰਤੋਂ ਕਰੋਗੇ, ਜਿਸ ਲਈ ਕੋਟਾ ਬੇਨਤੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਡਿਪਲੌਏਮੈਂਟ ਲਈ, ਤੁਸੀਂ *Standard_NC6s_v3* GPU ਦੀ ਵਰਤੋਂ ਕਰੋਗੇ, ਜਿਸ ਲਈ ਵੀ ਕੋਟਾ ਬੇਨਤੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

> [!NOTE]
>
> ਸਿਰਫ਼ Pay-As-You-Go ਸਭਸਕ੍ਰਿਪਸ਼ਨਾਂ (ਸਟੈਂਡਰਡ ਕ੍ਰਮ ਦੀਆਂ ਸਭਸਕ੍ਰਿਪਸ਼ਨਾਂ) ਨੂੰ GPU ਅਲੋਕੇਸ਼ਨ ਲਈ ਯੋਗਤਾ ਹੈ; ਲਾਭ ਵਾਲੀਆਂ ਸਭਸਕ੍ਰਿਪਸ਼ਨਾਂ ਹੁਣੇ ਸਮੇਤ ਸਮਰਥਿਤ ਨਹੀਂ ਹਨ।
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

1. *Standard NCADSA100v4 Family* ਕੋਟਾ ਬੇਨਤੀ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Quota** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Virtual machine family** ਚੁਣੋ। ਉਦਾਹਰਣ ਵਜੋਂ, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** ਚੁਣੋ, ਜਿਸ ਵਿੱਚ *Standard_NC24ads_A100_v4* GPU ਸ਼ਾਮਿਲ ਹੈ।
    - ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **Request quota** ਚੁਣੋ।

        ![Request quota.](../../../../../../translated_images/pa/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quota ਪੇਜ਼ ਵਿੱਚ, ਆਪਣਾ **New cores limit** ਦਰਜ ਕਰੋ। ਉਦਾਹਰਣ ਵਜੋਂ, 24।
    - Request quota ਪੇਜ਼ ਵਿੱਚ, GPU ਕੋਟਾ ਦੀ ਬੇਨਤੀ ਕਰਨ ਲਈ **Submit** ਚੁਣੋ।

1. *Standard NCSv3 Family* ਕੋਟਾ ਬੇਨਤੀ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Quota** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Virtual machine family** ਚੁਣੋ। ਉਦਾਹਰਣ ਵਜੋਂ, **Standard NCSv3 Family Cluster Dedicated vCPUs** ਚੁਣੋ, ਜਿਸ ਵਿੱਚ *Standard_NC6s_v3* GPU ਸ਼ਾਮਿਲ ਹੈ।
    - ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **Request quota** ਚੁਣੋ।
    - Request quota ਪੇਜ਼ ਵਿੱਚ, ਆਪਣਾ **New cores limit** ਦਰਜ ਕਰੋ। ਉਦਾਹਰਣ ਵਜੋਂ, 24।
    - Request quota ਪੇਜ਼ ਵਿੱਚ, GPU ਕੋਟਾ ਦੀ ਬੇਨਤੀ ਕਰਨ ਲਈ **Submit** ਚੁਣੋ।

### Add role assignment

ਆਪਣੇ ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਡਿਪਲੌਏ ਕਰਨ ਲਈ, ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਤੁਹਾਨੂੰ ਇੱਕ User Assigned Managed Identity (UAI) ਬਣਾਉਣੀ ਪਵੇਗੀ ਅਤੇ ਇਸ ਨੂੰ ਸਹੀ ਅਨੁਮਤੀਆਂ ਦੈਣੀਆਂ ਪਣਗੀ। ਇਹ UAI ਡਿਪਲੌਏਮੈਂਟ ਦੌਰਾਨ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ।

#### Create User Assigned Managed Identity(UAI)

1. ਹੁੱਛੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚ *managed identities* ਟਾਈਪ ਕਰੋ ਅਤੇ ਆਉਣ ਵਾਲੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ **Managed Identities** ਚੁਣੋ।

    ![Type managed identities.](../../../../../../translated_images/pa/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Create** ਚੁਣੋ।

    ![Select create.](../../../../../../translated_images/pa/03-02-select-create.92bf8989a5cd98f2.webp)

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਆਪਣਾ Azure **Subscription** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Resource group** ਚੁਣੋ (ਲੋੜ ਹੋਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।
    - ਆਪਣਾ **Region** ਚੁਣੋ।
    - **Name** ਦਰਜ ਕਰੋ। ਇਹ ਇਕ ਵਿਲੱਖਣ ਮੂਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

    ![Select create.](../../../../../../translated_images/pa/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Review + create** ਚੁਣੋ।

1. **+ Create** ਚੁਣੋ।

#### Add Contributor role assignment to Managed Identity

1. ਬਣਾਈ ਗਈ Managed Identity ਵਸਾਧਨ 'ਤੇ ਜਾਓ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Azure role assignments** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **+Add role assignment** ਚੁਣੋ।

1. Add role assignment ਪੇਜ਼ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:
    - **Scope** ਨੂੰ **Resource group** ਤੇ ਸੈਟ ਕਰੋ।
    - ਆਪਣਾ Azure **Subscription** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Resource group** ਚੁਣੋ।
    - **Role** ਨੂੰ **Contributor** ਤੇ ਸੈਟ ਕਰੋ।

    ![Fill contributor role.](../../../../../../translated_images/pa/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Save** ਚੁਣੋ।

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. ਹੁੱਛੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚ *storage accounts* ਲਿਖੋ ਅਤੇ ਆਉਣ ਵਾਲੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ **Storage accounts** ਚੁਣੋ।

    ![Type storage accounts.](../../../../../../translated_images/pa/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. ਉਸ ਸਟੋਰੇਜ ਅਕਾਊਂਟ ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ ਅਤੇ ਜੋ Azure Machine Learning ਵਰਕਸਪੇਸ ਨਾਲ ਜੁੜਿਆ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ, *finetunephistorage*।

1. Add role assignment ਪੇਜ਼ ਨੂੰ ਖੋਲ੍ਹਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਉਸ Azure Storage ਅਕਾਊਂਟ ਤੇ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।
    - ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Access Control (IAM)** ਚੁਣੋ।
    - ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **+ Add** ਚੁਣੋ।
    - ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **Add role assignment** ਚੁਣੋ।

    ![Add role.](../../../../../../translated_images/pa/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignment ਪੇਜ਼ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - Role ਪੇਜ਼ ਵਿੱਚ, ਖੋਜ ਬਾਰ ਵਿੱਚ *Storage Blob Data Reader* ਟਾਈਪ ਕਰੋ ਅਤੇ **Storage Blob Data Reader** ਚੁਣੋ।
    - Role ਪੇਜ਼ ਵਿੱਚ **Next** ਚੁਣੋ।
    - Members ਪੇਜ਼ ਵਿੱਚ, **Assign access to** ਤੋਂ **Managed identity** ਚੁਣੋ।
    - Members ਪੇਜ਼ ਵਿੱਚ **+ Select members** ਚੁਣੋ।
    - Select managed identities ਪੇਜ਼ ਵਿੱਚ ਆਪਣਾ Azure **Subscription** ਚੁਣੋ।
    - Select managed identities ਪੇਜ਼ ਵਿੱਚ, **Managed identity** ਨੂੰ **Manage Identity** ਸੈੱਟ ਕਰੋ।
    - ਉਸ Manage Identity ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਈ ਸੀ। ਉਦਾਹਰਣ ਵਜੋਂ, *finetunephi-managedidentity*।
    - Select managed identities ਪੇਜ਼ ਵਿੱਚ **Select** ਚੁਣੋ।

    ![Select managed identity.](../../../../../../translated_images/pa/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Review + assign** ਚੁਣੋ।

#### Add AcrPull role assignment to Managed Identity

1. ਹੁੱਛੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚ *container registries* ਲਿਖੋ ਅਤੇ ਆਉਣ ਵਾਲੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ **Container registries** ਚੁਣੋ।

    ![Type container registries.](../../../../../../translated_images/pa/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. ਉਸ container registry ਨੂੰ ਚੁਣੋ ਜੋ Azure Machine Learning ਵਰਕਸਪੇਸ ਨਾਲ ਜੁੜਿਆ ਹੋਵੇ। ਉਦਾਹਰਣ ਵਜੋਂ, *finetunephicontainerregistry*

1. Add role assignment ਪੇਜ਼ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Access Control (IAM)** ਚੁਣੋ।
    - ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **+ Add** ਚੁਣੋ।
    - ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂੰ ਤੋਂ **Add role assignment** ਚੁਣੋ।

1. Add role assignment ਪੇਜ਼ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - Role ਪੇਜ਼ ਵਿੱਚ ਖੋਜ ਬਾਰ ਵਿੱਚ *AcrPull* ਲਿਖੋ ਅਤੇ **AcrPull** ਚੁਣੋ।
    - Role ਪੇਜ਼ ਵਿੱਚ **Next** ਚੁਣੋ।
    - Members ਪੇਜ਼ ਵਿੱਚ, **Assign access to** ਤੋਂ **Managed identity** ਚੁਣੋ।
    - Members ਪੇਜ਼ ਵਿੱਚ **+ Select members** ਚੁਣੋ।
    - Select managed identities ਪੇਜ਼ ਵਿੱਚ ਆਪਣਾ Azure **Subscription** ਚੁਣੋ।
    - Select managed identities ਪੇਜ਼ ਵਿੱਚ, **Managed identity** ਨੂੰ **Manage Identity** ਸੈੱਟ ਕਰੋ।
    - ਉਹ Manage Identity ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਈ ਸੀ। ਉਦਾਹਰਣ ਵਜੋਂ, *finetunephi-managedidentity*।
    - Select managed identities ਪੇਜ਼ ਵਿੱਚ **Select** ਚੁਣੋ।
    - **Review + assign** ਚੁਣੋ।

### Set up project

ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਜਰੂਰੀ ਡੇਟਾਸੈਟ ਡਾਊਨਲੋਡ ਕਰਨ ਲਈ, ਤੁਸੀਂ ਇੱਕ ਲੋਕਲ ਇਨਵਾਇਰਨਮੈਂਟ ਸੈਟਅਪ ਕਰੋਗੇ।

ਇਸ ਕਸਰਤ ਵਿੱਚ, ਤੁਸੀਂ

- ਕੰਮ ਕਰਨ ਲਈ ਇੱਕ ਫੋਲਡਰ ਬਣਾਵੋਗੇ।
- ਇੱਕ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਵੋਗੇ।
- ਜਰੂਰੀ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋਗੇ।
- ਡੇਟਾਸੈਟ ਡਾਊਨਲੋਡ ਕਰਨ ਲਈ *download_dataset.py* ਫਾਇਲ ਬਣਾਵੋਗੇ।

#### Create a folder to work inside it

1. ਇੱਕ ਟਰਮੀਨਲ ਵਿੰਡੋ ਖੋਲ੍ਹੋ ਅਤੇ ਡਿਫੌਲਟ ਰਸਤੇ ਵਿੱਚ *finetune-phi* ਨਾਮ ਦਾ ਇੱਕ ਫੋਲਡਰ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਲਿਖੋ।

    ```console
    mkdir finetune-phi
    ```

2. ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਲਿਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਬਣਾਏ ਹੋਏ *finetune-phi* ਫੋਲਡਰ ਵਿੱਚ ਜਾ ਸਕੋ।

    ```console
    cd finetune-phi
    ```

#### Create a virtual environment

1. ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਲਿਖੋ ਤਾਂ ਜੋ *.venv* ਨਾਂ ਦਾ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਇਆ ਜਾ ਸਕੇ।


    ```console
    python -m venv .venv
    ```

2. ਆਪਣੀ ਟਰਮੀਨਲ ਦੇ ਅੰਦਰ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਟਾਈਪ ਕਰੋ ਤਾਂ ਜੋ ਵਰਚੁਅਲ ਵਾਤਾਵਰਨ ਸਰਗਰਮ ਕੀਤਾ ਜਾ ਸਕੇ।

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> ਜੇ ਇਹ ਕੰਮ ਕਰ ਗਿਆ, ਤਾਂ ਤੁਹਾਨੂੰ ਕਮਾਂਡ ਪ੍ਰਾਂਪਟ ਤੋਂ ਪਹਿਲਾਂ *(.venv)* ਵੇਖਾਈ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ।

#### ਲੋੜੀਂਦੇ ਪੈਕੇਜਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ

1. ਆਪਣੀ ਟਰਮੀਨਲ ਵਿੱਚ ਵਾਲੇ ਕਮਾਂਡਾਂ ਨੂੰ ਟਾਈਪ ਕਰੋ ਤਾਂ ਜੋ ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕੀਤੇ ਜਾ ਸਕਣ।

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` ਬਣਾਓ

> [!NOTE]
> ਪੂਰੀ ਫੋਲਡਰ ਰਚਨਾ:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** ਖੋਲ੍ਹੋ।

1. ਮੇਨੂ ਬਾਰ ਵਿੱਚੋਂ **File** ਚੁਣੋ।

1. **Open Folder** ਚੁਣੋ।

1. *finetune-phi* ਫੋਲਡਰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ, ਜੋ *C:\Users\yourUserName\finetune-phi* ਤੇ ਸਥਿਤ ਹੈ।

    ![Select the folder that you created.](../../../../../../translated_images/pa/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code ਦੇ ਖੱਬੇ ਪੈਨ ਵਿੱਚ, ਰਾਈਟ ਕਲਿੱਕ ਕਰਕੇ **New File** ਚੁਣੋ ਅਤੇ *download_dataset.py* ਨਾਮ ਦਾ ਨਵਾਂ ਫਾਈਲ ਬਣਾਓ।

    ![Create a new file.](../../../../../../translated_images/pa/04-02-create-new-file.cf9a330a3a9cff92.webp)

### ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਡਾਟਾਸੈੱਟ ਤਿਆਰ ਕਰੋ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ *download_dataset.py* ਫਾਈਲ ਚਲਾਕੇ *ultrachat_200k* ਡਾਟਾਸੈੱਟਸ ਆਪਣੇ ਲੋਕਲ ਵਾਤਾਵਰਨ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋਗੇ। ਫਿਰ ਤੁਸੀਂ ਇਹ ਡਾਟਾਸੈੱਟਸ Azure Machine Learning ਵਿਚ Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤੋਂ ਕਰੋਗੇ।

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ:

- ਡਾਟਾਸੈੱਟਸ ਡਾਊਨਲੋਡ ਕਰਨ ਲਈ *download_dataset.py* ਫਾਈਲ ਵਿੱਚ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋਗੇ।
- *download_dataset.py* ਫਾਈਲ ਚਲਾਕੇ ਡਾਟਾਸੈੱਟਸ ਨੂੰ ਆਪਣੇ ਲੋਕਲ ਵਾਤਾਵਰਨ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋਗੇ।

#### *download_dataset.py* ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣਾ ਡਾਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰੋ

1. Visual Studio Code ਵਿੱਚ *download_dataset.py* ਫਾਈਲ ਖੋਲ੍ਹੋ।

1. ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ *download_dataset.py* ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ।

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # ਦਿੱਤੇ ਨਾਂ, ਕਾਂfiguration, ਅਤੇ ਵੰਡ ਦਰ ਨਾਲ ਡਾਟਾਸੇਟ ਲੋਡ ਕਰੋ
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # ਡਾਟਾਸੇਟ ਨੂੰ ਟ੍ਰੇਨ ਅਤੇ ਟੈਸਟ ਸੈੱਟਾਂ ਵਿੱਚ ਵੰਡੋ (80% ਟ੍ਰੇਨ, 20% ਟੈਸਟ)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # ਜੇ ਡਾਇਰੈਕਟਰੀ ਮੌਜੂਦ ਨਹੀਂ ਹੈ ਤਾਂ ਬਣਾਓ
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # ਫਾਇਲ ਨੂੰ ਲੇਖਣ ਮੋਡ ਵਿੱਚ ਖੋਲ੍ਹੋ
        with open(filepath, 'w', encoding='utf-8') as f:
            # ਡਾਟਾਸੇਟ ਵਿੱਚ ਹਰ ਰਿਕਾਰਡ ਨੂੰ ਦੁਹਰਾਓ
            for record in dataset:
                # ਰਿਕਾਰਡ ਨੂੰ JSON ਑ਬਜੈਕਟ ਵਜੋਂ ਡੰਪ ਕਰੋ ਅਤੇ ਫਾਇਲ ਵਿੱਚ ਲਿਖੋ
                json.dump(record, f)
                # ਰਿਕਾਰਡਾਂ ਨੂੰ ਵੱਖ ਕਰਨ ਲਈ ਨਵੀਂ ਲਾਈਨ ਕੈਰੈਕਟਰ ਲਿਖੋ
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ਵਿਸ਼ੇਸ਼ ਕਾਂfiguration ਅਤੇ ਵੰਡ ਦਰ ਨਾਲ ULTRACHAT_200k ਡਾਟਾਸੇਟ ਨੂੰ ਲੋਡ ਅਤੇ ਵੰਡੋ
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # ਵੰਡ ਤੋਂ ਟ੍ਰੇਨ ਅਤੇ ਟੈਸਟ ਡਾਟਾਸੇਟ ਪ੍ਰਾਪਤ ਕਰੋ
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # ਟ੍ਰੇਨ ਡਾਟਾਸੇਟ ਨੂੰ JSONL ਫਾਇਲ ਵਿੱਚ ਸੇਵ ਕਰੋ
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # ਟੈਸਟ ਡਾਟਾਸੇਟ ਨੂੰ ਇੱਕ ਵੱਖਰੀ JSONL ਫਾਇਲ ਵਿੱਚ ਸੇਵ ਕਰੋ
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. ਆਪਣੀ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਟਾਈਪ ਕਰੋ ਤਾਂ ਕਿ ਸਕ੍ਰਿਪਟ ਚਲਾਈ ਜਾ ਸਕੇ ਅਤੇ ਡਾਟਾਸੈੱਟ ਤੁਹਾਡੇ ਲੋਕਲ ਵਾਤਾਵਰਨ ਵਿੱਚ ਡਾਊਨਲੋਡ ਹੋ ਸਕੇ।

    ```console
    python download_dataset.py
    ```

1. ਪੱਕਾ ਕਰੋ ਕਿ ਡਾਟਾਸੈੱਟਸ ਸਫਲਤਾਪੂਰਵਕ ਤੁਹਾਡੇ ਲੋਕਲ *finetune-phi/data* ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸੇਵ ਹੋ ਚੁੱਕੇ ਹਨ।

> [!NOTE]
>
> #### ਡਾਟਾਸੈੱਟ ਦਾ ਆਕਾਰ ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸਮੇਂ ਬਾਰੇ ਨੋਟ
>
> ਇਸ ਟਿਊਟੋਰਿਆਲ ਵਿੱਚ, ਤੁਸੀਂ ਸਿਰਫ 1% ਡਾਟਾਸੈੱਟ (`split='train[:1%]'`) ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ। ਇਹ ਡਾਟਾ ਦੀ ਮਾਤਰਾ ਨੂੰ ਕਾਫੀ ਘਟਾ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਅਪਲੋਡ ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੋਹਾਂ ਤੇਜ਼ ਹੋ ਜਾਂਦੇ ਹਨ। ਤੁਸੀਂ ਪ੍ਰਸ਼िक्षਣ ਸਮੇਂ ਅਤੇ ਮਾਡਲ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਵਿਚਕਾਰ ਸਹੀ ਸੰਤੁਲਨ ਲੱਭਣ ਲਈ ਪ੍ਰਤੀਸ਼ਤ ਵਿੱਚ ਤਬਦੀਲੀ ਕਰ ਸਕਦੇ ਹੋ। ਡਾਟਾਸੈੱਟ ਦਾ ਛੋਟਾ ਸੈਟ ਵਰਤਣਾ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਲੱਗਣ ਵਾਲਾ ਸਮਾਂ ਘਟਾ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਪ੍ਰਕਿਰਿਆ ਟਿਊਟੋਰਿਆਲ ਲਈ ਵਧੀਆ ਬਣ ਜਾਂਦੀ ਹੈ।

## ਪਰਿਣਾਮ 2: Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਅਤੇ Azure Machine Learning Studio ਵਿੱਚ ਡਿਪਲਾਇ

### Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ Azure Machine Learning Studio ਵਿੱਚ Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕਰੋਗੇ।

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ:

- ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਕੰਪਿਊਟਰ ਕਲੱਸਟਰ ਬਣਾਓਗੇ।
- Azure Machine Learning Studio ਵਿੱਚ Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕਰੋਗੇ।

#### ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਕੰਪਿਊਟਰ ਕਲੱਸਟਰ ਬਣਾਓ

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ਤੇ ਜਾਓ।

1. ਖੱਬੇ ਪਾਸੇ ਦੇ ਟੈਬ ਤੋਂ **Compute** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਵਿੱਚੋਂ **Compute clusters** ਚੁਣੋ।

1. **+ New** ਚੁਣੋ।

    ![Select compute.](../../../../../../translated_images/pa/06-01-select-compute.a29cff290b480252.webp)

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕਾਰਜ ਕਰੋ:

    - ਉਹ **Region** ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ।
    - **Virtual machine tier** ਨੂੰ **Dedicated** ਚੁਣੋ।
    - **Virtual machine type** ਨੂੰ **GPU** ਚੁਣੋ।
    - **Virtual machine size** ਫਿਲਟਰ ਨੂੰ **Select from all options** ਚੁਣੋ।
    - **Virtual machine size** ਨੂੰ **Standard_NC24ads_A100_v4** ਚੁਣੋ।

    ![Create cluster.](../../../../../../translated_images/pa/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** ਚੁਣੋ।

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕਾਰਜ ਕਰੋ:

    - **Compute name** ਦਿਓ। ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - **Minimum number of nodes** ਨੂੰ **0** ਚੁਣੋ।
    - **Maximum number of nodes** ਨੂੰ **1** ਚੁਣੋ।
    - **Idle seconds before scale down** ਨੂੰ **120** ਚੁਣੋ।

    ![Create cluster.](../../../../../../translated_images/pa/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** ਚੁਣੋ।

#### Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕਰੋ

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ਤੇ ਜਾਓ।

1. ਉਸ Azure Machine Learning ਵਰਕਸਪੇਸ ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

    ![Select workspace that you created.](../../../../../../translated_images/pa/06-04-select-workspace.a92934ac04f4f181.webp)

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕਾਰਜ ਕਰੋ:

    - ਖੱਬੇ ਪਾਸੇ ਦੇ ਟੈਬ ਵਿੱਚੋਂ **Model catalog** ਚੁਣੋ।
    - **search bar** ਵਿੱਚ *phi-3-mini-4k* ਟਾਈਪ ਕਰੋ ਅਤੇ ਉੱਥੇ ਆਉਣ ਵਾਲੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ **Phi-3-mini-4k-instruct** ਚੁਣੋ।

    ![Type phi-3-mini-4k.](../../../../../../translated_images/pa/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਵਿੱਚੋਂ **Fine-tune** ਚੁਣੋ।

    ![Select fine tune.](../../../../../../translated_images/pa/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕਾਰਜ ਕਰੋ:

    - **Select task type** ਨੂੰ **Chat completion** ਚੁਣੋ।
    - **+ Select data** ਚੁਣੋ ਤਾਂ ਜੋ **Training data** ਅਪਲੋਡ ਕੀਤਾ ਜਾਵੇ।
    - Validation data ਅਪਲੋਡ ਟਾਈਪ ਨੂੰ **Provide different validation data** ਚੁਣੋ।
    - **+ Select data** ਚੁਣੋ ਤਾਂ ਜੋ **Validation data** ਅਪਲੋਡ ਕੀਤਾ ਜਾਵੇ।

    ![Fill fine-tuning page.](../../../../../../translated_images/pa/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> ਤੁਸੀਂ **Advanced settings** ਚੁਣ ਕੇ **learning_rate** ਅਤੇ **lr_scheduler_type** ਵਰਗੀਆਂ ਵਿਵਸਥਾਵਾਂ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ, ਤਾਂ ਜੋ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਤੁਹਾਡੇ ਵਿਸ਼ੇਸ਼ ਜ਼ਰੂਰਤਾਂ ਮੁਤਾਬਕ ਢਾਲਿਆ ਜਾ ਸਕੇ।

1. **Finish** ਚੁਣੋ।

1. ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਵਕ Azure Machine Learning ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕੀਤੀ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪ੍ਰਕਿਰਿਆ ਕਾਫੀ ਸਮਾਂ ਲੈ ਸਕਦੀ ਹੈ। ਫਾਈਨ-ਟਿਊਨਿੰਗ ਜਾਬ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਨੂੰ ਇਸ ਦੇ ਪੂਰਾ ਹੋਣ ਦੀ ਉਡੀਕ करनी ਪੈਂਦੀ ਹੈ। ਤੁਸੀਂ ਆਪਣੀ Azure Machine Learning ਵਰਕਸਪੇਸ ਦੇ ਖੱਬੇ ਪਾਸੇ ਟੈਬ 'Jobs' ਵਿੱਚ ਜਾ ਕੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਜਾਬ ਦੀ ਸਥਿਤੀ ਨਿਗਰਾਨੀ ਕਰ ਸਕਦੇ ਹੋ। ਅਗਲੀ ਸਿਰੀਜ਼ ਵਿੱਚ, ਤੁਸੀਂ ਇਸ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਡਿਪਲੌਇ ਕਰਕੇ ਇਸ ਨੂੰ Prompt flow ਨਾਲ ਜੋੜੋਗੇ।

    ![See finetuning job.](../../../../../../translated_images/pa/06-08-output.2bd32e59930672b1.webp)

### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 ਮਾਡਲ ਨੂੰ ਡਿਪਲਾਇ ਕਰੋ

ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 ਮਾਡਲ ਨੂੰ Prompt flow ਨਾਲ ਇਕਜੁੱਟ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਮਾਡਲ ਨੂੰ ਡਿਪਲਾਇ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਇਹ ਰੀਅਲ-ਟਾਈਮ ਇੰਫਰੇਂਸ ਲਈ ਉਪਲਬਧ ਹੋ ਜਾਏ। ਇਸ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਮਾਡਲ ਰਜਿਸਟਰ ਕਰਨ, ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪਾਇੰਟ ਬਣਾਉਣ ਅਤੇ ਮਾਡਲ ਨੂੰ ਡਿਪਲਾਇ ਕਰਨ ਦੀ ਸ਼ਾਮਿਲ ਹੈ।

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ:

- ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਰਜਿਸਟਰ ਕਰੋਗੇ।
- ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪਾਇੰਟ ਬਣਾਵੋਗੇ।
- ਰਜਿਸਟਰਡ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 ਮਾਡਲ ਨੂੰ ਡਿਪਲਾਇ ਕਰੋਗੇ।

#### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰੋ

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ਤੇ ਜਾਓ।

1. ਉਸ Azure Machine Learning ਵਰਕਸਪੇਸ ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

    ![Select workspace that you created.](../../../../../../translated_images/pa/06-04-select-workspace.a92934ac04f4f181.webp)

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚੋਂ **Models** ਚੁਣੋ।
1. **+ Register** ਚੁਣੋ।
1. **From a job output** ਚੁਣੋ।

    ![Register model.](../../../../../../translated_images/pa/07-01-register-model.ad1e7cc05e4b2777.webp)

1. ਉਸ ਜਾਬ ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

    ![Select job.](../../../../../../translated_images/pa/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** ਚੁਣੋ।

1. **Model type** ਨੂੰ **MLflow** ਚੁਣੋ।

1. ਪੱਕਾ ਕਰੋ ਕਿ **Job output** ਚੁਣਿਆ ਹੋਇਆ ਹੈ; ਇਹ ਆਪੋ-ਆਪ ਸਿਲੈਕਟ ਹੋ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

    ![Select output.](../../../../../../translated_images/pa/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** ਚੁਣੋ।

3. **Register** ਚੁਣੋ।

    ![Select register.](../../../../../../translated_images/pa/07-04-register.fd82a3b293060bc7.webp)

4. ਤੁਸੀਂ ਆਪਣੇ ਰਜਿਸਟਰਡ ਮਾਡਲ ਨੂੰ ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚੋਂ **Models** ਮੀਨੂ ਵਿੱਚ ਜਾ ਕੇ ਦੇਖ ਸਕਦੇ ਹੋ।

    ![Registered model.](../../../../../../translated_images/pa/07-05-registered-model.7db9775f58dfd591.webp)

#### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਡਿਪਲਾਇ ਕਰੋ

1. ਉਸ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚੋਂ **Endpoints** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਵਿੱਚੋਂ **Real-time endpoints** ਚੁਣੋ।

    ![Create endpoint.](../../../../../../translated_images/pa/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** ਚੁਣੋ।

1. ਉਸ ਰਜਿਸਟਰਡ ਮਾਡਲ ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

    ![Select registered model.](../../../../../../translated_images/pa/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** ਚੁਣੋ।

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕਾਰਜ ਕਰੋ:

    - **Virtual machine** ਲਈ *Standard_NC6s_v3* ਚੁਣੋ।
    - ਤੁਹਾਡੇ ਵਰਤੋਂ ਲਈ **Instance count** ਚੁਣੋ, ਉਦਾਹਰਣ ਲਈ *1*।
    - ਐਂਡਪਾਇੰਟ ਲਈ **New** ਚੁਣੋ ਤਾਂ ਜੋ ਨਵਾਂ ਐਂਡਪਾਇੰਟ ਬਣਾਇਆ ਜਾਵੇ।
    - **Endpoint name** ਦਿਓ। ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - **Deployment name** ਦਿਓ। ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

    ![Fill the deployment setting.](../../../../../../translated_images/pa/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** ਚੁਣੋ।

> [!WARNING]
> ਆਪਣੇ ਖਾਤੇ ਵਿੱਚ ਵਾਧੂ ਚਾਰਜ ਤੋਂ ਬਚਣ ਲਈ, ਇਸ ਗੱਲ ਦੀ ਯਕੀਨੀ ਕਰ ਲਓ ਕਿ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਬਣਾਇਆ ਐਂਡਪਾਇੰਟ ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ।
>

#### Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਡਿਪਲਾਇਮੈਂਟ ਦੀ ਸਥਿਤੀ ਚੈੱਕ ਕਰੋ

1. ਉਹ Azure Machine Learning ਵਰਕਸਪੇਸ ਖੋਲ੍ਹੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚੋਂ **Endpoints** ਚੁਣੋ।

1. ਜਿਸ ਐਂਡਪਾਇੰਟ ਨੂੰ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ, ਉਸਨੂੰ ਚੁਣੋ।

    ![Select endpoints](../../../../../../translated_images/pa/07-09-check-deployment.325d18cae8475ef4.webp)

1. ਇਸ ਪੇਜ਼ ਤੇ, ਤੁਸੀਂ ਡਿਪਲਾਇਮੈਂਟ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਐਂਡਪਾਇੰਟਸ ਨੂੰ ਮੈਨੇਜ ਕਰ ਸਕਦੇ ਹੋ।

> [!NOTE]
> ਜਦੋਂ ਡਿਪਲਾਇਮੈਂਟ ਪੂਰਾ ਹੋ ਜਾਵੇ, ਯਕੀਨੀ ਕਰੋ ਕਿ **Live traffic** ਨੂੰ **100%** ਤੇ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ। ਜੇ ਇਹ ਸੈੱਟ ਨਹੀਂ ਹੈ, ਤਾਂ ਟ੍ਰੈਫਿਕ ਵਿਵਸਥਾਵਾਂ ਨੂੰ ਸੋਧਣ ਲਈ **Update traffic** ਚੁਣੋ। ਧਿਆਨ ਦਿਓ ਕਿ ਜੇ ਟ੍ਰੈਫਿਕ 0% ਤੇ ਹੈ ਤਾਂ ਤੁਸੀਂ ਮਾਡਲ ਦੀ ਟੈਸਟਿੰਗ ਨਹੀਂ ਕਰ ਸਕਦੇ।
>
> ![Set traffic.](../../../../../../translated_images/pa/07-10-set-traffic.085b847e5751ff3d.webp)
>

## ਪਰਿਣਾਮ 3: Prompt flow ਨਾਲ ਇਕਜੁੱਟ ਹੋਣਾ ਅਤੇ Microsoft Foundry ਵਿੱਚ ਆਪਣੇ ਕਸਟਮ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨਾ

### ਕਸਟਮ Phi-3 ਮਾਡਲ ਨੂੰ Prompt flow ਨਾਲ ਇਕਜੁੱਟ ਕਰੋ

ਆਪਣੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲਾਇ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਹੁਣ ਤੁਸੀਂ ਇਸ ਨੂੰ Prompt Flow ਨਾਲ ਜੋੜ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਰੀਅਲ-ਟਾਈਮ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਆਪਣੀ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕੇ, ਅਤੇ ਇਸ ਨਾਲ ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਇੰਟਰਐਕਟਿਵ ਟਾਸਕ ਕਰਨ ਯੋਗ ਹੋ ਜਾਓ।

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ:

- Microsoft Foundry Hub ਬਣਾਵੋਗੇ।
- Microsoft Foundry Project ਬਣਾਵੋਗੇ।
- Prompt flow ਬਣਾਵੋਗੇ।
- ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 ਮਾਡਲ ਲਈ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਸ਼ਾਮਿਲ ਕਰੋਗੇ।
- ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ Prompt flow ਸੈੱਟ ਕਰੋਗੇ।

> [!NOTE]
> ਤੁਸੀਂ Azure ML Studio ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੀ Promptflow ਨਾਲ ਇਕਜੁੱਟ ਹੋ ਸਕਦੇ ਹੋ। ਇਹੋ ਜਿਹੀ ਇਕਜੁੱਟ ਪ੍ਰਕਿਰਿਆ Azure ML Studio ਉੱਤੇ ਵੀ ਲਾਗੂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

#### Microsoft Foundry Hub ਬਣਾਓ

ਤੁਹਾਨੂੰ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਹਬ ਬਣਾਉਣੀ ਹੋਵੇਗੀ। ਇੱਕ ਹਬ ਇੱਕ Resource Group ਵਾਂਗ ਕੰਮ ਕਰਦਾ ਹੈ, ਜੋ ਤੁਹਾਨੂੰ Microsoft Foundry ਦੇ ਅੰਦਰ ਕਈ ਪ੍ਰੋਜੈਕਟਸ ਨੂੰ ਠੀਕ ਤਰ੍ਹਾਂ ਸੰਗਠਿਤ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
1. ਦੌਰਾ ਕਰੋ [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਵਿੱਚੋਂ **All hubs** ਚੁਣੋ।

1. ਨੈਵਿਗੇਸ਼ਨ ਮੈਨੂ ਤੋਂ **+ New hub** ਚੁਣੋ।

    ![Create hub.](../../../../../../translated_images/pa/08-01-create-hub.8f7dd615bb8d9834.webp)

1. ਹੇਠਲੇ ਕੰਮ ਕਰੋ:

    - **Hub name** ਦਰਜ ਕਰੋ। ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - ਆਪਣੀ Azure **Subscription** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Resource group** ਚੁਣੋ (ਲੋੜ ਹੋਵੇ ਤਾਂ ਨਵਾਂ ਬਣਾਓ)।
    - ਵਰਤੋਂ ਲਈ **Location** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Connect Azure AI Services** ਚੁਣੋ (ਲੋੜ ਹੋਵੇ ਤਾਂ ਨਵਾਂ ਬਣਾਓ)।
    - **Connect Azure AI Search** ਨੂੰ **Skip connecting** ਤੇ ਚੁਣੋ।

    ![Fill hub.](../../../../../../translated_images/pa/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** ਚੁਣੋ।

#### Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

1. ਬਣਾਏ ਹੋਏ Hub ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **All projects** ਚੁਣੋ।

1. ਨੈਵਿਗੇਸ਼ਨ ਮੈਨੂ ਤੋਂ **+ New project** ਚੁਣੋ।

    ![Select new project.](../../../../../../translated_images/pa/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** ਦਾਖਲ ਕਰੋ। ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

    ![Create project.](../../../../../../translated_images/pa/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** ਚੁਣੋ।

#### fine-tuned Phi-3 ਮਾਡਲ ਲਈ ਕਸਟਮ ਕਨੇਕਸ਼ਨ ਸ਼ਾਮِل ਕਰੋ

ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨੂੰ Prompt flow ਨਾਲ ਜੋੜਨ ਲਈ, ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੇ ਏਂਡਪੌਇੰਟ ਅਤੇ ਕੀ ਕਸਟਮ ਕਨੇਕਸ਼ਨ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਕਰਨੇ ਹਨ। ਇਹ ਸੈਟਅਪ ਤੁਹਾਡੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਤੱਕ Prompt flow ਵਿੱਚ ਪਹੁੰਚ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ।

#### fine-tuned Phi-3 ਮਾਡਲ ਦੀ api ਕੁੰਜੀ ਅਤੇ ਏਂਡਪੌਇੰਟ uri ਸੈਟ ਕਰੋ

1. ਦੌਰਾ ਕਰੋ [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Azure Machine Learning ਵਰਕਸਪੇਸ 'ਤੇ ਜਾਓ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Endpoints** ਚੁਣੋ।

    ![Select endpoints.](../../../../../../translated_images/pa/08-06-select-endpoints.aff38d453bcf9605.webp)

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ ਏਂਡਪੌਇੰਟ ਨੂੰ ਚੁਣੋ।

    ![Select endpoints.](../../../../../../translated_images/pa/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. ਨੈਵਿਗੇਸ਼ਨ ਮੈਨੂ ਤੋਂ **Consume** ਚੁਣੋ।

1. ਆਪਣਾ **REST endpoint** ਅਤੇ **Primary key** ਕੌਪੀ ਕਰੋ।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pa/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### ਕਸਟਮ ਕਨੇਕਸ਼ਨ ਸ਼ਾਮِل ਕਰੋ

1. ਦੌਰਾ ਕਰੋ [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ।

1. ਬਣਾਏ ਹੋਏ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Settings** ਚੁਣੋ।

1. **+ New connection** ਚੁਣੋ।

    ![Select new connection.](../../../../../../translated_images/pa/08-09-select-new-connection.02eb45deadc401fc.webp)

1. ਨੈਵਿਗੇਸ਼ਨ ਮੈਨੂ ਤੋਂ **Custom keys** ਚੁਣੋ।

    ![Select custom keys.](../../../../../../translated_images/pa/08-10-select-custom-keys.856f6b2966460551.webp)

1. ਹੇਠਲੇ ਕੰਮ ਕਰੋ:

    - **+ Add key value pairs** ਚੁਣੋ।
    - ਕੁੰਜੀ ਨਾਮ ਲਈ, **endpoint** ਦਰਜ ਕਰੋ ਅਤੇ Azure ML Studio ਤੋਂ ਕੌਪੀ ਕੀਤਾ ਏਂਡਪੌਇੰਟ ਮੁੱਲ ਫੀਲਡ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
    - ਫਿਰ ਤੋਂ **+ Add key value pairs** ਚੁਣੋ।
    - ਕੁੰਜੀ ਨਾਮ ਲਈ, **key** ਦਰਜ ਕਰੋ ਅਤੇ Azure ML Studio ਤੋਂ ਕੌਪੀ ਕੀਤੀ ਕੀ ਮੁੱਲ ਫੀਲਡ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
    - ਕੁੰਜੀਆਂ ਸ਼ਾਮਿਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਕੁੰਜੀ ਨੂੰ ਕੁਝ ਹੋਰ ਕਿਸੇ ਨੂੰ ਨਾ ਵੇਖਣ ਲਈ **is secret** ਚੁਣੋ।

    ![Add connection.](../../../../../../translated_images/pa/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** ਚੁਣੋ।

#### Prompt flow ਬਣਾਓ

ਤੁਹਾਡੇ Microsoft Foundry ਵਿੱਚ ਇੱਕ ਕਸਟਮ ਕਨੇਕਸ਼ਨ ਸ਼ਾਮਿਲ ਹੋ ਚੁੱਕਾ ਹੈ। ਹੁਣ, ਹੇਠਲੇ ਕਦਮਾਂ ਦਾ ਪਾਲਣ ਕਰਕੇ ਇੱਕ Prompt flow ਬਣਾਓ। ਫਿਰ, ਇਸ Prompt flow ਨੂੰ ਕਸਟਮ ਕਨੇਕਸ਼ਨ ਨਾਲ ਜੁੜੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੇ fine-tuned ਮਾਡਲ ਨੂੰ Prompt flow ਵਿੱਚ ਵਰਤ ਸਕੋ।

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Prompt flow** ਚੁਣੋ।

1. ਨੈਵਿਗੇਸ਼ਨ ਮੈਨੂ ਤੋਂ **+ Create** ਚੁਣੋ।

    ![Select Promptflow.](../../../../../../translated_images/pa/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. ਨੈਵਿਗੇਸ਼ਨ ਮੈਨੂ ਤੋਂ **Chat flow** ਚੁਣੋ।

    ![Select chat flow.](../../../../../../translated_images/pa/08-13-select-flow-type.2ec689b22da32591.webp)

1. ਵਰਤੋਂ ਲਈ **Folder name** ਦਾਖਲ ਕਰੋ।

    ![Enter name.](../../../../../../translated_images/pa/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** ਚੁਣੋ।

#### ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਲਈ Prompt flow ਸੈੱਟ ਕਰੋ

ਤੁਹਾਨੂੰ fine-tuned Phi-3 ਮਾਡਲ ਨੂੰ Prompt flow ਵਿੱਚ ਜੋੜਨਾ ਹੈ। ਮੌਜੂਦਾ ਦਿੱਤਾ ਗਿਆ Prompt flow ਇਸ ਮਕਸਦ ਲਈ ਬਣਾਇਆ ਨਹੀਂ ਗਿਆ। ਇਸ ਲਈ, ਤੁਹਾਨੂੰ Prompt flow ਨੂੰ ਦੁਬਾਰਾ ਡਿਜ਼ਾਈਨ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਕਸਟਮ ਮਾਡਲ ਦਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਹੋ ਸਕੇ।

1. Prompt flow ਵਿੱਚ, ਮੌਜੂਦਾ ਫਲੋ ਨੂੰ ਦੁਬਾਰਾ ਤਿਆਰ ਕਰਨ ਲਈ ਹੇਠਲੇ ਦਿਜੀਤਲੇ ਕਾਰਜ ਕਰੋ:

    - **Raw file mode** ਚੁਣੋ।
    - *flow.dag.yml* ਫਾਈਲ ਵਿੱਚ ਸਾਰਾ ਮੌਜੂਦਾ ਕੋਡ ਮਿਟਾ ਦਿਓ।
    - ਹੇਠਲਾ ਕੋਡ *flow.dag.yml* ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ।

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

    - **Save** ਚੁਣੋ।

    ![Select raw file mode.](../../../../../../translated_images/pa/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. *integrate_with_promptflow.py* ਫਾਈਲ ਵਿੱਚ ਹੇਠਲਾ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋ ਤਾਂ ਜੋ Prompt flow ਵਿੱਚ ਕਸਟਮ Phi-3 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਹੋ ਸਕੇ।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ਲਾਗਿੰਗ ਸੈਟਅਪ
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

        # "connection" Custom Connection ਦਾ ਨਾਮ ਹੈ, "endpoint", "key" Custom Connection ਵਿੱਚ ਕੁੰਜੀਆਂ ਹਨ
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
            
            # ਪੂਰਾ JSON ਜਵਾਬ ਲਾਗ ਕਰੋ
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

    ![Paste prompt flow code.](../../../../../../translated_images/pa/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry ਵਿੱਚ Prompt flow ਦੀ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ, ਤੁਸੀਂ ਇੱਥੇ ਵੇਖ ਸਕਦੇ ਹੋ [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. **Chat input**, **Chat output** ਚੁਣੋ ਤਾਂ ਜੋ ਆਪਣੇ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਸਾਮਰਥ ਹੋ ਜਾਏ।

    ![Input Output.](../../../../../../translated_images/pa/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਤਿਆਰੀ ਹੈ। ਅਗਲੇ ਐਕਸਰਸਾਈਜ਼ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ Prompt flow ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਆਪਣੇ fine-tuned Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ।

> [!NOTE]
>
> ਦੁਬਾਰਾ ਤਿਆਰ ਕੀਤਾ ਫਲੋ ਹੇਠਾਂ ਦਿੱਤੀ ਤਸਵੀਰ ਵਰਗਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:
>
> ![Flow example.](../../../../../../translated_images/pa/08-18-graph-example.d6457533952e690c.webp)
>

### ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰੋ

ਹੁਣ ਜਦੋਂ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਹੋਇਆ ਕਸਟਮ Phi-3 ਮਾਡਲ Prompt flow ਦੇ ਨਾਲ ਜੋੜ ਚੁੱਕੇ ਹੋ, ਤੁਸੀਂ ਇਸਦੇ ਨਾਲ ਸੰਵਾਦ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋ। ਇਹ ਵਿਅਾਖਿਆ ਤੁਹਾਨੂੰ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ Prompt flow ਸੈੱਟ ਅੱਪ ਕਰਨ ਅਤੇ ਸ਼ੁਰੂ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦਿਖਾਏਗੀ। ਇਹ ਕਦਮ ਪ徠 ਕਰਨ ਨਾਲ, ਤੁਸੀਂ ਆਪਣੇ fine-tuned Phi-3 ਮਾਡਲ ਦੀਆਂ ਸਾਰੀਆਂ ਖੂਬੀਆਂ ਵਰਤ ਸਕੋਂਗੇ।

- Prompt flow ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰੋ।

#### Prompt flow ਸ਼ੁਰੂ ਕਰੋ

1. Prompt flow ਸ਼ੁਰੂ ਕਰਨ ਲਈ **Start compute sessions** ਚੁਣੋ।

    ![Start compute session.](../../../../../../translated_images/pa/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. ਪੈਰਾਮੀਟਰ ਨਵੀਨਤਮ ਕਰਨ ਲਈ **Validate and parse input** ਚੁਣੋ।

    ![Validate input.](../../../../../../translated_images/pa/09-02-validate-input.317c76ef766361e9.webp)

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ ਕਸਟਮ ਕਨੇਕਸ਼ਨ ਦੀ **connection** ਦਾ **Value** ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, *connection*।

    ![Connection.](../../../../../../translated_images/pa/09-03-select-connection.99bdddb4b1844023.webp)

#### ਆਪਣੇ ਕਸਟਮ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰੋ

1. **Chat** ਚੁਣੋ।

    ![Select chat.](../../../../../../translated_images/pa/09-04-select-chat.61936dce6612a1e6.webp)

1. ਨਤੀਜਿਆਂ ਦਾ ਉਦਾਹਰਨ: ਹੁਣ ਤੁਸੀਂ ਆਪਣੇ ਕਸਟਮ Phi-3 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤੇ ਗਏ ਡਾਟਾ ਆਧਾਰਤ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

    ![Chat with prompt flow.](../../../../../../translated_images/pa/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸੁਤੰਤਰ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->