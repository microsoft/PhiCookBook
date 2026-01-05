<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T14:50:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "pcm"
}
-->
# Fine-tune an Integrate custom Phi-3 models wit Prompt flow

Dis end-to-end (E2E) sample na based on di guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" from di Microsoft Tech Community. E dey introduce di processes dem for fine-tuning, deploying, an integrating custom Phi-3 models wit Prompt flow.

## Overview

For dis E2E sample, you go learn how to fine-tune di Phi-3 model an integrate am wit Prompt flow. By leveraging Azure Machine Learning, an Prompt flow you go establish workflow for deployin an use custom AI models. Dis E2E sample divide inside three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**

**Scenario 3: Integrate with Prompt flow and Chat with your custom model**

Dis na overview of dis E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.pcm.png)

### Table of Contents

1. **[Scenario 1: Set up Azure resources and Prepare for fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Create an Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Request GPU quotas in Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Add role assignment](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Set up project](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Prepare dataset for fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Set up Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Fine-tune the Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy the fine-tuned model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrate with Prompt flow and Chat with your custom model](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrate the custom Phi-3 model with Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat with your custom model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Set up Azure resources and Prepare for fine-tuning

### Create an Azure Machine Learning Workspace

1. Type *azure machine learning* for di **search bar** wey dey top of di portal page an select **Azure Machine Learning** from di options wey show.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.pcm.png)

1. Select **+ Create** from di navigation menu.

1. Select **New workspace** from di navigation menu.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.pcm.png)

1. Do di following tasks:

    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use (make new one if you need).
    - Enter **Workspace Name**. E must be unique value.
    - Select di **Region** wey you want use.
    - Select di **Storage account** wey you go use (make new one if you need).
    - Select di **Key vault** wey you go use (make new one if you need).
    - Select di **Application insights** wey you go use (make new one if you need).
    - Select di **Container registry** wey you go use (make new one if you need).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.pcm.png)

1. Select **Review + Create**.

1. Select **Create**.

### Request GPU quotas in Azure Subscription

For dis E2E sample, you go use di *Standard_NC24ads_A100_v4 GPU* for fine-tuning, wey need quota request, an di *Standard_E4s_v3* CPU for deployment, wey no need quota request.

> [!NOTE]
>
> Only Pay-As-You-Go subscriptions (di standard subscription type) get chance for GPU allocation; benefit subscriptions dem no dey supported currently.
>
> For dem wey dey use benefit subscriptions (like Visual Studio Enterprise Subscription) or wey wan quickly test fine-tuning an deployment process, dis tutorial still dey show how to fine-tune wit minimal dataset using CPU. But e important make you sabi say fine-tuning results better wella wen you use GPU wit bigger datasets.

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Do di following tasks to request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** for left side tab.
    - Select di **Virtual machine family** wey you wan use. For example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, wey get *Standard_NC24ads_A100_v4* GPU.
    - Select di **Request quota** from di navigation menu.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.pcm.png)

    - For di Request quota page, enter di **New cores limit** wey you want use. For example, 24.
    - For di Request quota page, select **Submit** to request di GPU quota.

> [!NOTE]
> You fit select di GPU or CPU wey fit your needs by referring to [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) document.

### Add role assignment

To fine-tune an deploy your models, first you must create User Assigned Managed Identity (UAI) an assign am di correct permissions. Dis UAI go dey use for authentication during deployment.

#### Create User Assigned Managed Identity(UAI)

1. Type *managed identities* for di **search bar** wey dey top of di portal page an select **Managed Identities** from di options wey show.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.pcm.png)

1. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.pcm.png)

1. Do di following tasks:

    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use (make new one if you need).
    - Select di **Region** wen you go use.
    - Enter di **Name**. E gots to be unique value.

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Go to di Managed Identity resource wey you create.

1. Select **Azure role assignments** for left side tab.

1. Select **+Add role assignment** from di navigation menu.

1. For di Add role assignment page, do di following tasks:
    - Select di **Scope** to **Resource group**.
    - Select your Azure **Subscription**.
    - Select di **Resource group** you go use.
    - Select di **Role** to **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.pcm.png)

1. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* for di **search bar** wey dey top of di portal page an select **Storage accounts** from di options wey show.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.pcm.png)

1. Select di storage account wey relate to di Azure Machine Learning workspace wey you create. For example, *finetunephistorage*.

1. Do di following tasks to reach Add role assignment page:

    - Go to di Azure Storage account wey you create.
    - Select **Access Control (IAM)** for left side tab.
    - Select **+ Add** from di navigation menu.
    - Select **Add role assignment** from di navigation menu.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.pcm.png)

1. For di Add role assignment page, do di following tasks:

    - Inside di Role page, type *Storage Blob Data Reader* for di **search bar** an select **Storage Blob Data Reader** from di options wey show.
    - Inside di Role page, select **Next**.
    - Inside di Members page, select **Assign access to** **Managed identity**.
    - Inside di Members page, select **+ Select members**.
    - Inside Select managed identities page, select your Azure **Subscription**.
    - Inside Select managed identities page, select di **Managed identity** for **Manage Identity**.
    - Inside Select managed identities page, select di Manage Identity wey you create. For example, *finetunephi-managedidentity*.
    - Inside Select managed identities page, select **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.pcm.png)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* for di **search bar** wey dey top of di portal page an select **Container registries** from di options wey show.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.pcm.png)

1. Select di container registry wey relate to di Azure Machine Learning workspace. For example, *finetunephicontainerregistries*

1. Do di following tasks to reach Add role assignment page:

    - Select **Access Control (IAM)** for left side tab.
    - Select **+ Add** from di navigation menu.
    - Select **Add role assignment** from di navigation menu.

1. For di Add role assignment page, do di following tasks:

    - Inside di Role page, Type *AcrPull* for di **search bar** an select **AcrPull** from di options wey show.
    - Inside di Role page, select **Next**.
    - Inside di Members page, select **Assign access to** **Managed identity**.
    - Inside di Members page, select **+ Select members**.
    - Inside Select managed identities page, select your Azure **Subscription**.
    - Inside Select managed identities page, select di **Managed identity** for **Manage Identity**.
    - Inside Select managed identities page, select di Manage Identity wey you create. For example, *finetunephi-managedidentity*.
    - Inside Select managed identities page, select **Select**.
    - Select **Review + assign**.

### Set up project

Now, you go create folder to work inside an set up virtual environment to develop program wey dey interact wit users an use stored chat history from Azure Cosmos DB to help im responses.

#### Create a folder to work inside it

1. Open terminal window an type dis command to create folder wey dem go call *finetune-phi* inside di default path.

    ```console
    mkdir finetune-phi
    ```

1. Type dis command inside your terminal to waka enter di *finetune-phi* folder wey you create.

    ```console
    cd finetune-phi
    ```

#### Create a virtual environment

1. Type dis command inside your terminal to create virtual environment wey dem go call *.venv*.

    ```console
    python -m venv .venv
    ```

1. Type dis command inside your terminal to activate di virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> If e work, you go see *(.venv)* before command prompt.

#### Install the required packages

1. Type dis commands inside your terminal to install di packages wey you need.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Create project files
For dis exercise, you go create di important files wey our project need. Dis files go include scripts wey dem go use download di dataset, set up di Azure Machine Learning environment, fine-tune di Phi-3 model, plus deploy di fine-tuned model. You go still create one *conda.yml* file to set up di fine-tuning environment.

For dis exercise, you go:

- Create one *download_dataset.py* file to download di dataset.
- Create one *setup_ml.py* file to set up di Azure Machine Learning environment.
- Create one *fine_tune.py* file inside *finetuning_dir* folder to fine-tune di Phi-3 model with di dataset.
- Create one *conda.yml* file to set up fine-tuning environment.
- Create one *deploy_model.py* file to deploy di fine-tuned model.
- Create one *integrate_with_promptflow.py* file, to join di fine-tuned model and run di model using Prompt flow.
- Create one flow.dag.yml file, to set up di workflow structure for Prompt flow.
- Create one *config.py* file to put Azure information.

> [!NOTE]
>
> Complete folder structure:
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

1. Open **Visual Studio Code**.

1. Select **File** from di menu bar.

1. Select **Open Folder**.

1. Select di *finetune-phi* folder wey you create, wey dey for *C:\Users\yourUserName\finetune-phi*.

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.pcm.png)

1. For left side pane for Visual Studio Code, right-click then select **New File** to create new file named *download_dataset.py*.

1. For left side pane for Visual Studio Code, right-click then select **New File** to create new file named *setup_ml.py*.

1. For left side pane for Visual Studio Code, right-click then select **New File** to create new file named *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.pcm.png)

1. For left side pane for Visual Studio Code, right-click then select **New Folder** to create one new folder named *finetuning_dir*.

1. For *finetuning_dir* folder, create new file named *fine_tune.py*.

#### Create and Configure *conda.yml* file

1. For left side pane for Visual Studio Code, right-click then select **New File** to create new file named *conda.yml*.

1. Add di following code to di *conda.yml* file to set up di fine-tuning environment for Phi-3 model.

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

#### Create and Configure *config.py* file

1. For left side pane for Visual Studio Code, right-click then select **New File** to create new file named *config.py*.

1. Add di following code to di *config.py* file to put your Azure information inside.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Add Azure environment variables

1. Do dis tasks to add Azure Subscription ID:

    - Type *subscriptions* for **search bar** wey dey top for di portal page, select **Subscriptions** from di options wey show.
    - Select di Azure Subscription wey you dey use now.
    - Copy and paste your Subscription ID inside *config.py* file.

    ![Find subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.pcm.png)

1. Do dis tasks to add Azure Workspace Name:

    - Go Azure Machine Learning resource wey you create.
    - Copy and paste your account name inside *config.py* file.

    ![Find Azure Machine Learning name.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.pcm.png)

1. Do dis tasks to add Azure Resource Group Name:

    - Go Azure Machine Learning resource wey you create.
    - Copy and paste your Azure Resource Group Name inside *config.py* file.

    ![Find resource group name.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.pcm.png)

2. Do dis tasks to add Azure Managed Identity name:

    - Go Managed Identities resource wey you create.
    - Copy and paste your Azure Managed Identity name inside *config.py* file.

    ![Find UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.pcm.png)

### Prepare dataset for fine-tuning

For dis exercise, you go run *download_dataset.py* file to download di *ULTRACHAT_200k* datasets to your local environment. Then you go use dis datasets to fine-tune di Phi-3 model for Azure Machine Learning.

#### Download your dataset using *download_dataset.py*

1. Open *download_dataset.py* file for Visual Studio Code.

1. Add di following code inside *download_dataset.py*.

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
        # Load di dataset wit di name, configuration, an split ratio wey you specify
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Divide di dataset into train an test sets (80% train, 20% test)
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
        
        # Open di file make you fit write inside am
        with open(filepath, 'w', encoding='utf-8') as f:
            # Go through every record wey dey di dataset
            for record in dataset:
                # Dump di record as JSON object an write am for di file
                json.dump(record, f)
                # Write one newline character to separate di records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load an split di ULTRACHAT_200k dataset wit one specific configuration an split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract di train an test datasets from di split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save di train dataset to one JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save di test dataset to one different JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Advice for fine-tuning with small dataset using CPU**
>
> If you want use CPU for fine-tuning, dis method good for people wey get benefit subscriptions (like Visual Studio Enterprise Subscription) or to quickly test fine-tuning and deployment process.
>
> Change `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` to `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Type dis command inside your terminal to run di script and download di dataset to your local environment.

    ```console
    python download_data.py
    ```

1. Check say di datasets save well for your local *finetune-phi/data* directory.

> [!NOTE]
>
> **Dataset size and fine-tuning time**
>
> For dis E2E sample, you use just 1% of di dataset (`train_sft[:1%]`). Dis one reduce data size well well, e go make di upload and fine-tuning process quick. You fit change di percentage to balance training time and model performance. To use small part of di dataset go reduce di time wey you go spend fine-tuning, e go make di process easier for E2E sample.

## Scenario 2: Fine-tune Phi-3 model and Deploy for Azure Machine Learning Studio

### Set up Azure CLI

You need set up Azure CLI to authenticate your environment. Azure CLI allow you manage Azure resources straight from di command line and e dey provide credentials wey Azure Machine Learning need to access di resources. To start install [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Open terminal window and type di follow command to log in to your Azure account.

    ```console
    az login
    ```

1. Select di Azure account wey you want use.

1. Select di Azure subscription wey you want use.

    ![Find resource group name.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.pcm.png)

> [!TIP]
>
> If you get wahala to sign in to Azure, try use device code. Open terminal window and type di follow command to sign in to your Azure account:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tune di Phi-3 model

For dis exercise, you go fine-tune di Phi-3 model with di dataset we dem provide. First, you go define di fine-tuning process inside *fine_tune.py* file. Then, you go set up di Azure Machine Learning environment and start di fine-tuning process by running *setup_ml.py* file. Dis script go make sure say di fine-tuning go happen inside di Azure Machine Learning environment.

When you run *setup_ml.py*, you go run di fine-tuning process for inside Azure Machine Learning environment.

#### Add code to *fine_tune.py* file

1. Go *finetuning_dir* folder and open *fine_tune.py* file for Visual Studio Code.

1. Add di follow code inside *fine_tune.py*.

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

    # Make you no get the INVALID_PARAMETER_VALUE error for MLflow, turn off MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # How to set up logging
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

1. Save and close *fine_tune.py* file.

> [!TIP]
> **You fit fine-tune Phi-3.5 model**
>
> For *fine_tune.py* file, you fit change `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model wey you wan fine-tune. For example, if you change am to `"microsoft/Phi-3.5-mini-instruct"`, you go use Phi-3.5-mini-instruct model for fine-tuning. To find and use di model name wey you like, go [Hugging Face](https://huggingface.co/), search di model wey you want, then copy and paste di name enter `pretrained_model_name` field for your script.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.">
>

#### Add code to *setup_ml.py* file

1. Open *setup_ml.py* file for Visual Studio Code.

1. Add di follow code inside *setup_ml.py*.

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

    # Unkomen di lines wey dey under so yu fit use CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Unkomen di lines wey dey under so yu fit use GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace wit di place wey your compute cluster dey
    FINETUNING_DIR = "./finetuning_dir" # Path to di fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of di training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to di model output directory for azure ml

    # Logging setup wey dey track di process
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
            image=DOCKER_IMAGE_NAME,  # Docker image for di environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of di environment
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
                tier="Dedicated",  # Tier of di compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait make di cluster get created
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
            compute=compute_name,  # Compute cluster wey you go use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to di training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to di evaluation data file
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
        
        # Create or find existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit di job
        ml_client.jobs.stream(returned_job.name)  # Stream di job logs
        
        # Capture di job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Change `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` to your own details.

    ```python
   # Make e no dey comment for di following lines if you wan use GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Change am to where your compute cluster dey located
    ```

> [!TIP]
>
> **Advice for fine-tuning with small dataset using CPU**
>
> If you want use CPU for fine-tuning, dis method good for people wey get benefit subscriptions (like Visual Studio Enterprise Subscription) or to quickly test fine-tuning and deployment process.
>
> 1. Open *setup_ml* file.
> 1. Change `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` to dis settings. If you no get access to *Standard_E16s_v3*, you fit use any similar CPU instance or ask for new quota.
> 1. Change `LOCATION` to your own details.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Type dis command to run *setup_ml.py* script and start fine-tuning process for Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. For dis exercise, you don successfully fine-tune Phi-3 model using Azure Machine Learning. When you run *setup_ml.py* script, you don set up di Azure Machine Learning environment and start di fine-tuning process wey dey inside *fine_tune.py* file. Abeg note say fine-tuning process fit take plenty time. After you run `python setup_ml.py` command, you go need to wait di process finish. You fit check di fine-tuning job status by following di link wey dey terminal to Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.pcm.png)

### Deploy di fine-tuned model

To join di fine-tuned Phi-3 model with Prompt Flow, you need deploy di model to make e dey ready for real-time inference. Dis process involve to register di model, create online endpoint, plus deploy di model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Change `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` to di name wey you want for your model.

1. Change `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` to di name wey you want for your endpoint.

1. Change `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` to di name wey you want for your deployment.

#### Add code to *deploy_model.py* file

When you run *deploy_model.py* file, e go automatically do all di deployment work. E go register di model, create endpoint, and run di deployment based on di settings wey dey inside config.py file, wey get model name, endpoint name, and deployment name.

1. Open *deploy_model.py* file for Visual Studio Code.

1. Add di follow code inside *deploy_model.py*.

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
            # Make we fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Make we log de current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set de traffic allocation for de deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update de endpoint wit de new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Make we log de updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Make we log any errors wey happen during de process
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

1. Do di follow tasks to get `JOB_NAME`:

    - Go Azure Machine Learning resource wey you create.
    - Select **Studio web URL** to open Azure Machine Learning workspace.
    - Select **Jobs** from di left side tab.
    - Select di experiment for fine-tuning. For example, *finetunephi*.
    - Select di job wey you create.
    - Copy and paste your job Name inside `JOB_NAME = "your-job-name"` for *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` wit your correct info.

1. Type dis command to run *deploy_model.py* script and start deployment process for Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> To avoid extra charges for your account, make sure say you delete di created endpoint for Azure Machine Learning workspace.
>

#### Check deployment status for Azure Machine Learning Workspace

1. Go [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Go di Azure Machine Learning workspace wey you create.

1. Click **Studio web URL** to open Azure Machine Learning workspace.

1. Select **Endpoints** from di left side tab.

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.pcm.png)

2. Select di endpoint wey you create.

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.pcm.png)

3. For dis page, you fit manage di endpoints wey you create during deployment process.

## Scenario 3: Integrate wit Prompt flow and Chat wit your custom model

### Integrate di custom Phi-3 model wit Prompt flow

After you don successfully deploy your fine-tuned model, you fit now join am wit Prompt flow to use your model inside real-time apps, wey go allow different interactive tasks wit your custom Phi-3 model.

#### Set api key and endpoint uri for di fine-tuned Phi-3 model

1. Go Azure Machine learning workspace wey you create.
1. Select **Endpoints** from di left side tab.
1. Select di endpoint wey you create.
1. Select **Consume** from di navigation menu.
1. Copy and paste your **REST endpoint** into *config.py* file, replace `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` wit your **REST endpoint**.
1. Copy and paste your **Primary key** into *config.py* file, replace `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` wit your **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.pcm.png)

#### Add code to *flow.dag.yml* file

1. Open *flow.dag.yml* file for Visual Studio Code.

1. Add dis code inside *flow.dag.yml*.

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

#### Add code to *integrate_with_promptflow.py* file

1. Open *integrate_with_promptflow.py* file for Visual Studio Code.

1. Add dis code inside *integrate_with_promptflow.py*.

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

    # Di logging setup
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

### Chat wit your custom model

1. Type dis command to run *deploy_model.py* script and start deployment process for Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Example of results be dis: Now you fit chat wit your custom Phi-3 model. E dey advised make you ask questions wey relate to data wey dem use for fine-tuning.

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.pcm.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg make you understand say automated translation fit get mistake or no too correct. Di original document wey dey im own language na di correct one. If na serious information, e better make person wey sabi human translation do am. We no go take responsibility if wahala or misunderstanding happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->