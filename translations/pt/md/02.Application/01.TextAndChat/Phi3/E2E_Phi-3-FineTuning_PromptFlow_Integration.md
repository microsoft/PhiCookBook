<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T02:47:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "pt"
}
-->
# Fine-tune and Integrate custom Phi-3 models with Prompt flow

This end-to-end (E2E) sample is based on the guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community. It introduces the processes of fine-tuning, deploying, and integrating custom Phi-3 models with Prompt flow.

## Overview

In this E2E sample, you will learn how to fine-tune the Phi-3 model and integrate it with Prompt flow. By leveraging Azure Machine Learning, and Prompt flow you will establish a workflow for deploying and utilizing custom AI models. This E2E sample is divided into three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**

**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**

**Scenario 3: Integrate with Prompt flow and Chat with your custom model**

Here is an overview of this E2E sample.

![Visão geral da Integração Phi-3 FineTuning com PromptFlow](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.pt.png)

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

1. Type *azure machine learning* in the **search bar** at the top of the portal page and select **Azure Machine Learning** from the options that appear.

    ![Escreva azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.pt.png)

1. Select **+ Create** from the navigation menu.

1. Select **New workspace** from the navigation menu.

    ![Selecionar new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.pt.png)

1. Perform the following tasks:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (create a new one if needed).
    - Enter **Workspace Name**. It must be a unique value.
    - Select the **Region** you'd like to use.
    - Select the **Storage account** to use (create a new one if needed).
    - Select the **Key vault** to use (create a new one if needed).
    - Select the **Application insights** to use (create a new one if needed).
    - Select the **Container registry** to use (create a new one if needed).

    ![Preencher AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.pt.png)

1. Select **Review + Create**.

1. Select **Create**.

### Request GPU quotas in Azure Subscription

In this E2E sample, you will use the *Standard_NC24ads_A100_v4 GPU* for fine-tuning, which requires a quota request, and the *Standard_E4s_v3* CPU for deployment, which does not require a quota request.

> [!NOTE]
>
> Apenas subscrições Pay-As-You-Go (o tipo de subscrição padrão) são elegíveis para alocação de GPU; subscrições com benefícios não são atualmente suportadas.
>
> Para quem utiliza subscrições com benefícios (como a Visual Studio Enterprise Subscription) ou para quem pretende testar rapidamente o processo de fine-tuning e deployment, este tutorial também fornece orientação para fine-tuning com um conjunto de dados mínimo usando CPU. No entanto, é importante notar que os resultados do fine-tuning são significativamente melhores quando se utiliza uma GPU com conjuntos de dados maiores.

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Perform the following tasks to request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** from the left side tab.
    - Select the **Virtual machine family** to use. For example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC24ads_A100_v4* GPU.
    - Select the **Request quota** from the navigation menu.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.pt.png)

    - Inside the Request quota page, enter the **New cores limit** you'd like to use. For example, 24.
    - Inside the Request quota page, select **Submit** to request the GPU quota.

> [!NOTE]
> You can select the appropriate GPU or CPU for your needs by referring to [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) document.

### Add role assignment

To fine-tune and deploy your models, you must first create a User Assigned Managed Identity (UAI) and assign it the appropriate permissions. This UAI will be used for authentication during deployment

#### Create User Assigned Managed Identity(UAI)

1. Type *managed identities* in the **search bar** at the top of the portal page and select **Managed Identities** from the options that appear.

    ![Escreva managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.pt.png)

1. Select **+ Create**.

    ![Selecionar create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.pt.png)

1. Perform the following tasks:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (create a new one if needed).
    - Select the **Region** you'd like to use.
    - Enter the **Name**. It must be a unique value.

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Navigate to the Managed Identity resource that you created.

1. Select **Azure role assignments** from the left side tab.

1. Select **+Add role assignment** from the navigation menu.

1. Inside Add role assignment page, Perform the following tasks:
    - Select the **Scope** to **Resource group**.
    - Select your Azure **Subscription**.
    - Select the **Resource group** to use.
    - Select the **Role** to **Contributor**.

    ![Preencher função contributor.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.pt.png)

1. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* in the **search bar** at the top of the portal page and select **Storage accounts** from the options that appear.

    ![Escreva storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.pt.png)

1. Select the storage account that associated with the Azure Machine Learning workspace that you created. For example, *finetunephistorage*.

1. Perform the following tasks to navigate to Add role assignment page:

    - Navigate to the Azure Storage account that you created.
    - Select **Access Control (IAM)** from the left side tab.
    - Select **+ Add** from the navigation menu.
    - Select **Add role assignment** from the navigation menu.

    ![Adicionar função.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.pt.png)

1. Inside Add role assignment page, Perform the following tasks:

    - Inside the Role page, type *Storage Blob Data Reader* in the **search bar** and select **Storage Blob Data Reader** from the options that appear.
    - Inside the Role page, select **Next**.
    - Inside the Members page, select **Assign access to** **Managed identity**.
    - Inside the Members page, select **+ Select members**.
    - Inside Select managed identities page, select your Azure **Subscription**.
    - Inside Select managed identities page, select the **Managed identity** to **Manage Identity**.
    - Inside Select managed identities page, select the Manage Identity that you created. For example, *finetunephi-managedidentity*.
    - Inside Select managed identities page, select **Select**.

    ![Selecionar managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.pt.png)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* in the **search bar** at the top of the portal page and select **Container registries** from the options that appear.

    ![Escreva container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.pt.png)

1. Select the container registry that associated with the Azure Machine Learning workspace. For example, *finetunephicontainerregistries*

1. Perform the following tasks to navigate to Add role assignment page:

    - Select **Access Control (IAM)** from the left side tab.
    - Select **+ Add** from the navigation menu.
    - Select **Add role assignment** from the navigation menu.

1. Inside Add role assignment page, Perform the following tasks:

    - Inside the Role page, Type *AcrPull* in the **search bar** and select **AcrPull** from the options that appear.
    - Inside the Role page, select **Next**.
    - Inside the Members page, select **Assign access to** **Managed identity**.
    - Inside the Members page, select **+ Select members**.
    - Inside Select managed identities page, select your Azure **Subscription**.
    - Inside Select managed identities page, select the **Managed identity** to **Manage Identity**.
    - Inside Select managed identities page, select the Manage Identity that you created. For example, *finetunephi-managedidentity*.
    - Inside Select managed identities page, select **Select**.
    - Select **Review + assign**.

### Set up project

Now, you will create a folder to work in and set up a virtual environment to develop a program that interacts with users and uses stored chat history from Azure Cosmos DB to inform its responses.

#### Create a folder to work inside it

1. Open a terminal window and type the following command to create a folder named *finetune-phi* in the default path.

    ```console
    mkdir finetune-phi
    ```

1. Type the following command inside your terminal to navigate to the *finetune-phi* folder you created.

    ```console
    cd finetune-phi
    ```

#### Create a virtual environment

1. Type the following command inside your terminal to create a virtual environment named *.venv*.

    ```console
    python -m venv .venv
    ```

1. Type the following command inside your terminal to activate the virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> If it worked, you should see *(.venv)* before the command prompt.

#### Install the required packages

1. Type the following commands inside your terminal to install the required packages.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Create project files
Neste exercício, irá criar os ficheiros essenciais para o nosso projeto. Estes ficheiros incluem scripts para descarregar o conjunto de dados, configurar o ambiente Azure Machine Learning, ajustar finamente o modelo Phi-3 e implantar o modelo afinado. Também irá criar um ficheiro *conda.yml* para configurar o ambiente de fine-tuning.

Neste exercício, irá:

- Criar um ficheiro *download_dataset.py* para descarregar o conjunto de dados.
- Criar um ficheiro *setup_ml.py* para configurar o ambiente Azure Machine Learning.
- Criar um ficheiro *fine_tune.py* na pasta *finetuning_dir* para ajustar finamente o modelo Phi-3 utilizando o conjunto de dados.
- Criar um ficheiro *conda.yml* para configurar o ambiente de fine-tuning.
- Criar um ficheiro *deploy_model.py* para implantar o modelo afinado.
- Criar um ficheiro *integrate_with_promptflow.py*, para integrar o modelo afinado e executar o modelo usando Prompt flow.
- Criar um ficheiro flow.dag.yml, para definir a estrutura do fluxo de trabalho para o Prompt flow.
- Criar um ficheiro *config.py* para inserir informações da Azure.

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

1. Abra o **Visual Studio Code**.

1. Selecione **Ficheiro** na barra de menus.

1. Selecione **Abrir Pasta**.

1. Selecione a pasta *finetune-phi* que criou, localizada em *C:\Users\yourUserName\finetune-phi*.

    ![Abrir pasta do projeto.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.pt.png)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *download_dataset.py*.

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *setup_ml.py*.

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *deploy_model.py*.

    ![Criar novo ficheiro.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.pt.png)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Nova Pasta** para criar uma nova pasta chamada *finetuning_dir*.

1. Na pasta *finetuning_dir*, crie um novo ficheiro chamado *fine_tune.py*.

#### Create and Configure *conda.yml* file

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *conda.yml*.

1. Adicione o código seguinte ao ficheiro *conda.yml* para configurar o ambiente de fine-tuning para o modelo Phi-3.

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

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *config.py*.

1. Adicione o código seguinte ao ficheiro *config.py* para incluir as suas informações da Azure.

    ```python
    # Configurações do Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "Grupo de Teste"

    # Configurações do Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-espaço-de-trabalho"

    # Configurações de Identidade Gerida do Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-identidade-gerida"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Caminhos dos ficheiros do conjunto de dados
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Configurações do modelo ajustado
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-modelo"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-ponto-de-extremidade"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-implantação"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{seu-nome-de-endpoint}.{sua_regiao}.inference.ml.azure.com/score"
    ```

#### Add Azure environment variables

1. Execute as seguintes tarefas para adicionar o Azure Subscription ID:

    - Escreva *subscriptions* na **barra de pesquisa** no topo da página do portal e selecione **Subscrições** nas opções apresentadas.
    - Selecione a Subscrição Azure que está a utilizar atualmente.
    - Copie e cole o seu Subscription ID no ficheiro *config.py*.

    ![Encontrar ID de subscrição.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.pt.png)

1. Execute as seguintes tarefas para adicionar o Nome do Workspace do Azure:

    - Navegue até ao recurso Azure Machine Learning que criou.
    - Copie e cole o nome da sua conta no ficheiro *config.py*.

    ![Encontrar nome do Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.pt.png)

1. Execute as seguintes tarefas para adicionar o Nome do Resource Group do Azure:

    - Navegue até ao recurso Azure Machine Learning que criou.
    - Copie e cole o Nome do seu Resource Group no ficheiro *config.py*.

    ![Encontrar nome do grupo de recursos.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.pt.png)

2. Execute as seguintes tarefas para adicionar o nome da Azure Managed Identity

    - Navegue até ao recurso Managed Identities que criou.
    - Copie e cole o nome da sua Azure Managed Identity no ficheiro *config.py*.

    ![Encontrar UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.pt.png)

### Prepare dataset for fine-tuning

Neste exercício, irá executar o ficheiro *download_dataset.py* para descarregar os conjuntos de dados *ULTRACHAT_200k* para o seu ambiente local. Em seguida, irá utilizar estes conjuntos de dados para ajustar finamente o modelo Phi-3 no Azure Machine Learning.

#### Download your dataset using *download_dataset.py*

1. Abra o ficheiro *download_dataset.py* no Visual Studio Code.

1. Adicione o código seguinte em *download_dataset.py*.

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
        # Carregar o conjunto de dados com o nome, configuração e rácio de divisão especificados
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Dividir o conjunto de dados em conjuntos de treino e teste (80% treino, 20% teste)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Criar o diretório se não existir
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Abrir o ficheiro em modo de escrita
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterar sobre cada registo no conjunto de dados
            for record in dataset:
                # Converter o registo num objeto JSON e escrevê-lo no ficheiro
                json.dump(record, f)
                # Escrever um carácter de nova linha para separar registos
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Carregar e dividir o conjunto de dados ULTRACHAT_200k com uma configuração específica e rácio de divisão
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrair os conjuntos de treino e teste da divisão
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Guardar o conjunto de treino num ficheiro JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Guardar o conjunto de teste num ficheiro JSONL separado
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Orientações para fine-tuning com um conjunto de dados mínimo usando CPU**
>
> Se pretende utilizar uma CPU para o fine-tuning, esta abordagem é ideal para quem tem subscrições com benefícios (por exemplo, Visual Studio Enterprise Subscription) ou para testar rapidamente o processo de fine-tuning e implantação.
>
> Substitua `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` por `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Escreva o seguinte comando no seu terminal para executar o script e descarregar o conjunto de dados para o seu ambiente local.

    ```console
    python download_data.py
    ```

1. Verifique se os conjuntos de dados foram guardados com sucesso na sua diretoria local *finetune-phi/data*.

> [!NOTE]
>
> **Tamanho do conjunto de dados e tempo de fine-tuning**
>
> Neste exemplo E2E, utiliza apenas 1% do conjunto de dados (`train_sft[:1%]`). Isto reduz significativamente a quantidade de dados, acelerando tanto o upload como os processos de fine-tuning. Pode ajustar a percentagem para encontrar o equilíbrio certo entre o tempo de treino e o desempenho do modelo. Utilizar um subconjunto menor do conjunto de dados reduz o tempo necessário para o fine-tuning, tornando o processo mais manejável para um exemplo E2E.

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Set up Azure CLI

Precisa de configurar o Azure CLI para autenticar o seu ambiente. O Azure CLI permite gerir recursos Azure diretamente a partir da linha de comandos e fornece as credenciais necessárias para que o Azure Machine Learning aceda a esses recursos. Para começar, instale o [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Abra uma janela de terminal e escreva o seguinte comando para iniciar sessão na sua conta Azure.

    ```console
    az login
    ```

1. Selecione a sua conta Azure a utilizar.

1. Selecione a sua subscrição Azure a utilizar.

    ![Encontrar nome do grupo de recursos.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.pt.png)

> [!TIP]
>
> Se estiver a ter problemas para iniciar sessão no Azure, experimente usar um código de dispositivo. Abra uma janela de terminal e escreva o seguinte comando para iniciar sessão na sua conta Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tune the Phi-3 model

Neste exercício, irá ajustar finamente o modelo Phi-3 utilizando o conjunto de dados fornecido. Primeiro, irá definir o processo de fine-tuning no ficheiro *fine_tune.py*. Em seguida, irá configurar o ambiente Azure Machine Learning e iniciar o processo de fine-tuning executando o ficheiro *setup_ml.py*. Este script garante que o fine-tuning ocorre dentro do ambiente Azure Machine Learning.

Ao executar *setup_ml.py*, irá correr o processo de fine-tuning no ambiente Azure Machine Learning.

#### Add code to the *fine_tune.py* file

1. Navegue até à pasta *finetuning_dir* e abra o ficheiro *fine_tune.py* no Visual Studio Code.

1. Adicione o código seguinte em *fine_tune.py*.

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

    # Para evitar o erro INVALID_PARAMETER_VALUE no MLflow, desative a integração com o MLflow
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Configuração de registo
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

1. Guarde e feche o ficheiro *fine_tune.py*.

> [!TIP]
> **Pode ajustar o modelo Phi-3.5**
>
> No ficheiro *fine_tune.py*, pode alterar o `pretrained_model_name` de `"microsoft/Phi-3-mini-4k-instruct"` para qualquer modelo que pretenda afinar. Por exemplo, se o alterar para `"microsoft/Phi-3.5-mini-instruct"`, estará a utilizar o modelo Phi-3.5-mini-instruct para o fine-tuning. Para encontrar e usar o nome do modelo que preferir, visite o [Hugging Face](https://huggingface.co/), procure o modelo de que está interessado e, em seguida, copie e cole o seu nome no campo `pretrained_model_name` no seu script.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Ajuste fino do Phi-3.5.">
>

#### Add code to the *setup_ml.py* file

1. Abra o ficheiro *setup_ml.py* no Visual Studio Code.

1. Adicione o código seguinte em *setup_ml.py*.

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

    # Constantes

    # Descomente as linhas seguintes para usar uma instância CPU para treino
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Descomente as linhas seguintes para usar uma instância GPU para treino
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Substitua pela localização do seu cluster de computação
    FINETUNING_DIR = "./finetuning_dir" # Caminho para o script de ajuste fino
    TRAINING_ENV_NAME = "phi-3-training-environment" # Nome do ambiente de treino
    MODEL_OUTPUT_DIR = "./model_output" # Caminho para o diretório de saída do modelo no Azure ML

    # Configuração de registo para acompanhar o processo
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
            image=DOCKER_IMAGE_NAME,  # Imagem Docker para o ambiente
            conda_file=CONDA_FILE,  # Ficheiro do ambiente Conda
            name=TRAINING_ENV_NAME,  # Nome do ambiente
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
                tier="Dedicated",  # Nível do cluster de computação
                min_instances=0,  # Número mínimo de instâncias
                max_instances=1  # Número máximo de instâncias
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Aguardar a criação do cluster
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Caminho para o fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Ambiente de treino
            compute=compute_name,  # Cluster de computação a utilizar
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Caminho para o ficheiro de dados de treino
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Caminho para o ficheiro de dados de avaliação
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Inicializar o cliente ML
        ml_client = get_ml_client()

        # Criar ambiente
        env = create_or_get_environment(ml_client)
        
        # Criar ou obter um cluster de computação existente
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Criar e submeter o trabalho de ajuste fino
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submeter o trabalho
        ml_client.jobs.stream(returned_job.name)  # Transmitir os registos do trabalho
        
        # Capturar o nome do trabalho
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, e `LOCATION` pelos seus detalhes específicos.

    ```python
   # Descomente as linhas seguintes para usar uma instância com GPU para treino
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Substitua pela localização do seu cluster de computação
    ```

> [!TIP]
>
> **Orientações para fine-tuning com um conjunto de dados mínimo usando CPU**
>
> Se pretende utilizar uma CPU para o fine-tuning, esta abordagem é ideal para quem tem subscrições com benefícios (por exemplo, Visual Studio Enterprise Subscription) ou para testar rapidamente o processo de fine-tuning e implantação.
>
> 1. Abra o ficheiro *setup_ml*.
> 1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, e `DOCKER_IMAGE_NAME` pelos valores seguintes. Se não tiver acesso a *Standard_E16s_v3*, pode usar uma instância CPU equivalente ou requisitar uma nova quota.
> 1. Substitua `LOCATION` pelos seus detalhes específicos.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Escreva o seguinte comando para executar o script *setup_ml.py* e iniciar o processo de fine-tuning no Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. Neste exercício, afinou com sucesso o modelo Phi-3 utilizando o Azure Machine Learning. Ao executar o script *setup_ml.py*, configurou o ambiente Azure Machine Learning e iniciou o processo de fine-tuning definido no ficheiro *fine_tune.py*. Note que o processo de fine-tuning pode demorar um tempo considerável. Após executar o comando `python setup_ml.py`, precisa de aguardar que o processo seja concluído. Pode monitorizar o estado do trabalho de fine-tuning seguindo o link fornecido no terminal para o portal Azure Machine Learning.

    ![Ver trabalho de fine-tuning.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.pt.png)

### Deploy the fine-tuned model

Para integrar o modelo Phi-3 afinado com o Prompt Flow, é necessário implantar o modelo para o tornar acessível para inferência em tempo real. Este processo envolve registar o modelo, criar um endpoint online e implantar o modelo.

#### Set the model name, endpoint name, and deployment name for deployment

1. Abra o ficheiro *config.py*.

1. Substitua `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` pelo nome pretendido para o seu modelo.

1. Substitua `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` pelo nome pretendido para o seu endpoint.

1. Substitua `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` pelo nome pretendido para a sua deployment.

#### Add code to the *deploy_model.py* file

A execução do ficheiro *deploy_model.py* automatiza todo o processo de implantação. Regista o modelo, cria um endpoint e executa a implantação com base nas definições especificadas no ficheiro config.py, que inclui o nome do modelo, o nome do endpoint e o nome da implantação.

1. Abra o ficheiro *deploy_model.py* no Visual Studio Code.

1. Adicione o código seguinte em *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Importações de configuração
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

    # Constantes
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Configuração do registo
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
            # Obter os detalhes do endpoint atual
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Registar a alocação de tráfego atual para depuração
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Definir a alocação de tráfego para a implantação
            endpoint.traffic = {deployment_name: 100}
            
            # Atualizar o endpoint com a nova alocação de tráfego
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Registar a alocação de tráfego atualizada para depuração
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Registar quaisquer erros que ocorram durante o processo
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

1. Execute as seguintes tarefas para obter o `JOB_NAME`:

    - Navegue até ao recurso Azure Machine Learning que criou.
    - Selecione **URL web do Studio** para abrir o workspace do Azure Machine Learning.
    - Selecione **Jobs** a partir do separador lateral esquerdo.
    - Selecione o experimento de fine-tuning. Por exemplo, *finetunephi*.
    - Selecione o job que criou.
    - Copie e cole o nome do seu job em `JOB_NAME = "your-job-name"` no ficheiro *deploy_model.py*.

1. Substitua `COMPUTE_INSTANCE_TYPE` pelos seus detalhes específicos.

1. Execute o seguinte comando para correr o script *deploy_model.py* e iniciar o processo de implantação no Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Para evitar custos adicionais na sua conta, certifique-se de eliminar o endpoint criado no workspace do Azure Machine Learning.
>

#### Verificar o estado da implantação no espaço de trabalho do Azure Machine Learning

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até ao espaço de trabalho do Azure Machine Learning que criou.

1. Selecione **Studio web URL** para abrir o espaço de trabalho do Azure Machine Learning.

1. Selecione **Endpoints** no separador lateral esquerdo.

    ![Selecione endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.pt.png)

2. Selecione o endpoint que criou.

    ![Selecione o endpoint que criou.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.pt.png)

3. Nesta página, pode gerir os endpoints criados durante o processo de implantação.

## Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado

### Integrar o modelo Phi-3 personalizado com o Prompt flow

Após implantar com sucesso o seu modelo ajustado, pode agora integrá-lo com o Prompt flow para usar o seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com o seu modelo Phi-3 personalizado.

#### Definir a chave API e o URI do endpoint do modelo Phi-3 ajustado

1. Navegue até ao espaço de trabalho do Azure Machine learning que criou.
1. Selecione **Endpoints** no separador lateral esquerdo.
1. Selecione o endpoint que criou.
1. Selecione **Consume** no menu de navegação.
1. Copie e cole o seu **endpoint REST** no ficheiro *config.py*, substituindo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` pelo seu **endpoint REST**.
1. Copie e cole a sua **chave primária** no ficheiro *config.py*, substituindo `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` pela sua **chave primária**.

    ![Copiar chave API e URI do endpoint.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.pt.png)

#### Adicionar código ao ficheiro *flow.dag.yml*

1. Abra o ficheiro *flow.dag.yml* no Visual Studio Code.

1. Adicione o código seguinte em *flow.dag.yml*.

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

#### Adicionar código ao ficheiro *integrate_with_promptflow.py*

1. Abra o ficheiro *integrate_with_promptflow.py* no Visual Studio Code.

1. Adicione o código seguinte em *integrate_with_promptflow.py*.

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

    # Configuração de registos
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

### Conversar com o seu modelo personalizado

1. Execute o seguinte comando para correr o script *deploy_model.py* e iniciar o processo de implantação no Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Aqui está um exemplo dos resultados: Agora pode conversar com o seu modelo Phi-3 personalizado. Recomenda-se fazer perguntas com base nos dados usados para o ajuste fino.

    ![Exemplo do Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.pt.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido utilizando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, note que as traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua de origem deverá ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->