<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T02:58:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "br"
}
-->
# Ajuste fino e Integração de modelos Phi-3 personalizados com Prompt flow

Este exemplo de ponta a ponta (E2E) baseia-se no guia "[Ajuste Fino e Integração de Modelos Phi-3 Personalizados com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community. Ele apresenta os processos de ajuste fino, implantação e integração de modelos Phi-3 personalizados com o Prompt flow.

## Visão geral

Neste exemplo E2E, você aprenderá como ajustar finamente o modelo Phi-3 e integrá-lo com o Prompt flow. Aproveitando o Azure Machine Learning e o Prompt flow, você estabelecerá um fluxo de trabalho para implantar e utilizar modelos de IA personalizados. Este exemplo E2E está dividido em três cenários:

**Cenário 1: Configurar recursos do Azure e Preparar para ajuste fino**

**Cenário 2: Ajuste fino do modelo Phi-3 e Implantação no Azure Machine Learning Studio**

**Cenário 3: Integrar com Prompt flow e Conversar com seu modelo personalizado**

Aqui está uma visão geral deste exemplo E2E.

![Visão geral da integração Phi-3 Fine-Tuning e Prompt Flow](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.br.png)

### Índice

1. **[Cenário 1: Configurar recursos do Azure e Preparar para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Criar um Workspace do Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Solicitar cotas de GPU na assinatura do Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adicionar atribuição de função](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurar projeto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparar conjunto de dados para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 2: Ajuste fino do modelo Phi-3 e Implantação no Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Configurar Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ajuste fino do modelo Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implantar o modelo ajustado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 3: Integrar com Prompt flow e Conversar com seu modelo personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrar o modelo Phi-3 personalizado com o Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Conversar com seu modelo personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Cenário 1: Configurar recursos do Azure e preparar para ajuste fino

### Criar um Workspace do Azure Machine Learning

1. Digite *azure machine learning* na **barra de pesquisa** na parte superior da página do portal e selecione **Azure Machine Learning** nas opções que aparecem.

    ![Digite azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.br.png)

1. Selecione **+ Create** no menu de navegação.

1. Selecione **New workspace** no menu de navegação.

    ![Selecione novo workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.br.png)

1. Execute as seguintes tarefas:

    - Selecione sua **Subscription** do Azure.
    - Selecione o **Resource group** a ser usado (crie um novo, se necessário).
    - Insira **Workspace Name**. Deve ser um valor exclusivo.
    - Selecione a **Region** que deseja usar.
    - Selecione a **Storage account** a ser usada (crie uma nova, se necessário).
    - Selecione o **Key vault** a ser usado (crie um novo, se necessário).
    - Selecione o **Application insights** a ser usado (crie um novo, se necessário).
    - Selecione o **Container registry** a ser usado (crie um novo, se necessário).

    ![Preencha AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.br.png)

1. Selecione **Review + Create**.

1. Selecione **Create**.

### Solicitar cotas de GPU na assinatura do Azure

Neste exemplo E2E, você usará a GPU *Standard_NC24ads_A100_v4* para ajuste fino, que requer uma solicitação de cota, e a CPU *Standard_E4s_v3* para implantação, que não requer solicitação de cota.

> [!NOTE]
>
> Apenas assinaturas Pay-As-You-Go (o tipo de assinatura padrão) são elegíveis para alocação de GPU; assinaturas com benefícios não são atualmente suportadas.
>
> Para aqueles que usam assinaturas com benefícios (como Visual Studio Enterprise Subscription) ou que desejam testar rapidamente o processo de ajuste fino e implantação, este tutorial também fornece orientação para ajustar com um conjunto de dados mínimo usando CPU. No entanto, é importante observar que os resultados do ajuste fino são significativamente melhores quando se utiliza uma GPU com conjuntos de dados maiores.

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Execute as seguintes tarefas para solicitar a cota *Standard NCADSA100v4 Family*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **Virtual machine family** a ser usada. Por exemplo, selecione **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC24ads_A100_v4*.
    - Selecione **Request quota** no menu de navegação.

        ![Solicitar cota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.br.png)

    - Dentro da página Request quota, insira o **New cores limit** que deseja utilizar. Por exemplo, 24.
    - Dentro da página Request quota, selecione **Submit** para solicitar a cota de GPU.

> [!NOTE]
> Você pode selecionar a GPU ou CPU apropriada para suas necessidades consultando o documento [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Adicionar atribuição de função

Para ajustar e implantar seus modelos, você deve primeiro criar uma Identidade Gerenciada Atribuída pelo Usuário (User Assigned Managed Identity - UAI) e atribuir as permissões apropriadas. Esta UAI será usada para autenticação durante a implantação

#### Criar User Assigned Managed Identity (UAI)

1. Digite *managed identities* na **barra de pesquisa** na parte superior da página do portal e selecione **Managed Identities** nas opções que aparecem.

    ![Digite managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.br.png)

1. Selecione **+ Create**.

    ![Selecione criar.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.br.png)

1. Execute as seguintes tarefas:

    - Selecione sua **Subscription** do Azure.
    - Selecione o **Resource group** a ser usado (crie um novo, se necessário).
    - Selecione a **Region** que deseja usar.
    - Insira o **Name**. Deve ser um valor exclusivo.

1. Selecione **Review + create**.

1. Selecione **+ Create**.

#### Adicionar atribuição de função Contributor à Managed Identity

1. Navegue até o recurso Managed Identity que você criou.

1. Selecione **Azure role assignments** na aba lateral esquerda.

1. Selecione **+Add role assignment** no menu de navegação.

1. Dentro da página Add role assignment, execute as seguintes tarefas:
    - Selecione o **Scope** para **Resource group**.
    - Selecione sua **Subscription** do Azure.
    - Selecione o **Resource group** a ser usado.
    - Selecione a **Role** para **Contributor**.

    ![Preencher função contributor.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.br.png)

1. Selecione **Save**.

#### Adicionar atribuição de função Storage Blob Data Reader à Managed Identity

1. Digite *storage accounts* na **barra de pesquisa** na parte superior da página do portal e selecione **Storage accounts** nas opções que aparecem.

    ![Digite storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.br.png)

1. Selecione a conta de armazenamento associada ao Azure Machine Learning workspace que você criou. Por exemplo, *finetunephistorage*.

1. Execute as seguintes tarefas para navegar até a página Add role assignment:

    - Navegue até a conta de armazenamento do Azure que você criou.
    - Selecione **Access Control (IAM)** na aba lateral esquerda.
    - Selecione **+ Add** no menu de navegação.
    - Selecione **Add role assignment** no menu de navegação.

    ![Adicionar função.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.br.png)

1. Dentro da página Add role assignment, execute as seguintes tarefas:

    - Na página Role, digite *Storage Blob Data Reader* na **barra de pesquisa** e selecione **Storage Blob Data Reader** nas opções que aparecem.
    - Na página Role, selecione **Next**.
    - Na página Members, selecione **Assign access to** **Managed identity**.
    - Na página Members, selecione **+ Select members**.
    - Na página Select managed identities, selecione sua **Subscription** do Azure.
    - Na página Select managed identities, selecione a **Managed identity** para **Manage Identity**.
    - Na página Select managed identities, selecione a Managed Identity que você criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Select managed identities, selecione **Select**.

    ![Selecionar managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.br.png)

1. Selecione **Review + assign**.

#### Adicionar atribuição de função AcrPull à Managed Identity

1. Digite *container registries* na **barra de pesquisa** na parte superior da página do portal e selecione **Container registries** nas opções que aparecem.

    ![Digite container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.br.png)

1. Selecione o registro de contêiner associado ao Azure Machine Learning workspace. Por exemplo, *finetunephicontainerregistries*

1. Execute as seguintes tarefas para navegar até a página Add role assignment:

    - Selecione **Access Control (IAM)** na aba lateral esquerda.
    - Selecione **+ Add** no menu de navegação.
    - Selecione **Add role assignment** no menu de navegação.

1. Dentro da página Add role assignment, execute as seguintes tarefas:

    - Na página Role, digite *AcrPull* na **barra de pesquisa** e selecione **AcrPull** nas opções que aparecem.
    - Na página Role, selecione **Next**.
    - Na página Members, selecione **Assign access to** **Managed identity**.
    - Na página Members, selecione **+ Select members**.
    - Na página Select managed identities, selecione sua **Subscription** do Azure.
    - Na página Select managed identities, selecione a **Managed identity** para **Manage Identity**.
    - Na página Select managed identities, selecione a Managed Identity que você criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Select managed identities, selecione **Select**.
    - Selecione **Review + assign**.

### Configurar projeto

Agora, você criará uma pasta para trabalhar e configurará um ambiente virtual para desenvolver um programa que interage com usuários e usa o histórico de chat armazenado no Azure Cosmos DB para informar suas respostas.

#### Criar uma pasta para trabalhar dentro dela

1. Abra uma janela de terminal e digite o seguinte comando para criar uma pasta chamada *finetune-phi* no caminho padrão.

    ```console
    mkdir finetune-phi
    ```

1. Digite o seguinte comando no seu terminal para navegar até a pasta *finetune-phi* que você criou.

    ```console
    cd finetune-phi
    ```

#### Criar um ambiente virtual

1. Digite o seguinte comando no seu terminal para criar um ambiente virtual chamado *.venv*.

    ```console
    python -m venv .venv
    ```

1. Digite o seguinte comando no seu terminal para ativar o ambiente virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Se funcionou, você deverá ver *(.venv)* antes do prompt de comando.

#### Instalar os pacotes necessários

1. Digite os seguintes comandos no seu terminal para instalar os pacotes necessários.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Criar arquivos do projeto
Neste exercício, você criará os arquivos essenciais para o nosso projeto. Esses arquivos incluem scripts para baixar o conjunto de dados, configurar o ambiente Azure Machine Learning, ajustar finamente o modelo Phi-3, e implantar o modelo ajustado. Você também criará um arquivo *conda.yml* para configurar o ambiente de fine-tuning.

Neste exercício, você irá:

- Criar um arquivo *download_dataset.py* para baixar o conjunto de dados.
- Criar um arquivo *setup_ml.py* para configurar o ambiente Azure Machine Learning.
- Criar um arquivo *fine_tune.py* na pasta *finetuning_dir* para ajustar finamente o modelo Phi-3 usando o conjunto de dados.
- Criar um arquivo *conda.yml* para configurar o ambiente de fine-tuning.
- Criar um arquivo *deploy_model.py* para implantar o modelo ajustado.
- Criar um arquivo *integrate_with_promptflow.py*, para integrar o modelo ajustado e executar o modelo usando Prompt flow.
- Criar um arquivo flow.dag.yml, para configurar a estrutura do fluxo de trabalho para o Prompt flow.
- Criar um arquivo *config.py* para inserir as informações do Azure.

> [!NOTE]
>
> Estrutura completa de pastas:
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

1. Selecione **Arquivo** na barra de menu.

1. Selecione **Abrir Pasta**.

1. Selecione a pasta *finetune-phi* que você criou, localizada em *C:\Users\yourUserName\finetune-phi*.

    ![Abrir pasta do projeto.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.br.png)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Arquivo** para criar um novo arquivo chamado *download_dataset.py*.

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Arquivo** para criar um novo arquivo chamado *setup_ml.py*.

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Arquivo** para criar um novo arquivo chamado *deploy_model.py*.

    ![Criar novo arquivo.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.br.png)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Nova Pasta** para criar uma nova pasta chamada *finetuning_dir*.

1. Na pasta *finetuning_dir*, crie um novo arquivo chamado *fine_tune.py*.

#### Create and Configure *conda.yml* file

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Arquivo** para criar um novo arquivo chamado *conda.yml*.

1. Adicione o código a seguir no arquivo *conda.yml* para configurar o ambiente de fine-tuning para o modelo Phi-3.

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

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Arquivo** para criar um novo arquivo chamado *config.py*.

1. Adicione o código a seguir no arquivo *config.py* para incluir suas informações do Azure.

    ```python
    # Configurações do Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "Grupo de Teste"

    # Configurações do Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-espaço-de-trabalho"

    # Configurações de Identidade Gerenciada do Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetune-phi-identidade-gerenciada"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Caminhos dos arquivos do conjunto de dados
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Configurações do modelo ajustado
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-modelo"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-implantação"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{nome-do-seu-endpoint}.{sua-região}.inference.ml.azure.com/score"
    ```

#### Add Azure environment variables

1. Execute as seguintes tarefas para adicionar o ID da Assinatura do Azure:

    - Digite *subscriptions* na **barra de pesquisa** no topo da página do portal e selecione **Subscriptions** nas opções que aparecerem.
    - Selecione a Assinatura do Azure que você está usando atualmente.
    - Copie e cole seu Subscription ID no arquivo *config.py*.

    ![Encontrar ID da assinatura.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.br.png)

1. Execute as seguintes tarefas para adicionar o Nome do Workspace do Azure:

    - Navegue até o recurso Azure Machine Learning que você criou.
    - Copie e cole o nome da sua conta no arquivo *config.py*.

    ![Encontrar nome do Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.br.png)

1. Execute as seguintes tarefas para adicionar o Nome do Grupo de Recursos do Azure:

    - Navegue até o recurso Azure Machine Learning que você criou.
    - Copie e cole o Nome do Grupo de Recursos do Azure no arquivo *config.py*.

    ![Encontrar nome do grupo de recursos.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.br.png)

2. Execute as seguintes tarefas para adicionar o nome da Identidade Gerenciada do Azure

    - Navegue até o recurso Managed Identities que você criou.
    - Copie e cole o nome da sua Identidade Gerenciada do Azure no arquivo *config.py*.

    ![Encontrar UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.br.png)

### Prepare dataset for fine-tuning

Neste exercício, você executará o arquivo *download_dataset.py* para baixar os conjuntos de dados *ULTRACHAT_200k* para o seu ambiente local. Em seguida, você usará esses conjuntos de dados para ajustar finamente o modelo Phi-3 no Azure Machine Learning.

#### Download your dataset using *download_dataset.py*

1. Abra o arquivo *download_dataset.py* no Visual Studio Code.

1. Adicione o código a seguir em *download_dataset.py*.

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
        # Carregar o conjunto de dados com o nome, configuração e proporção de divisão especificados
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
        # Criar o diretório se ele não existir
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Abrir o arquivo em modo de escrita
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterar sobre cada registro no conjunto de dados
            for record in dataset:
                # Serializar o registro como objeto JSON e escrevê-lo no arquivo
                json.dump(record, f)
                # Escrever um caractere de nova linha para separar os registros
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Carregar e dividir o conjunto de dados ULTRACHAT_200k com uma configuração específica e proporção de divisão
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrair os conjuntos de dados de treino e teste da divisão
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Salvar o conjunto de treino em um arquivo JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Salvar o conjunto de teste em um arquivo JSONL separado
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Guidance for fine-tuning with a minimal dataset using a CPU**
>
> If you want to use a CPU for fine-tuning, this approach is ideal for those with benefit subscriptions (such as Visual Studio Enterprise Subscription) or to quickly test the fine-tuning and deployment process.
>
> Replace `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Digite o seguinte comando dentro do seu terminal para executar o script e baixar o conjunto de dados para o seu ambiente local.

    ```console
    python download_data.py
    ```

1. Verifique se os conjuntos de dados foram salvos com sucesso no seu diretório local *finetune-phi/data*.

> [!NOTE]
>
> **Dataset size and fine-tuning time**
>
> In this E2E sample, you use only 1% of the dataset (`train_sft[:1%]`). This significantly reduces the amount of data, speeding up both the upload and fine-tuning processes. You can adjust the percentage to find the right balance between training time and model performance. Using a smaller subset of the dataset reduces the time required for fine-tuning, making the process more manageable for a E2E sample.

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Set up Azure CLI

Você precisa configurar o Azure CLI para autenticar seu ambiente. O Azure CLI permite gerenciar recursos do Azure diretamente pela linha de comando e fornece as credenciais necessárias para que o Azure Machine Learning acesse esses recursos. Para começar, instale o [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Abra uma janela de terminal e digite o seguinte comando para entrar na sua conta Azure.

    ```console
    az login
    ```

1. Selecione a conta Azure que deseja usar.

1. Selecione a assinatura Azure que deseja usar.

    ![Encontrar nome do grupo de recursos.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.br.png)

> [!TIP]
>
> If you're having trouble signing in to Azure, try using a device code. Open a terminal window and type the following command to sign in to your Azure account:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tune the Phi-3 model

Neste exercício, você ajustará finamente o modelo Phi-3 usando o conjunto de dados fornecido. Primeiro, você definirá o processo de fine-tuning no arquivo *fine_tune.py*. Em seguida, você configurará o ambiente Azure Machine Learning e iniciará o processo de fine-tuning executando o arquivo *setup_ml.py*. Esse script garante que o fine-tuning ocorra dentro do ambiente Azure Machine Learning.

Ao executar *setup_ml.py*, você executará o processo de fine-tuning no ambiente Azure Machine Learning.

#### Add code to the *fine_tune.py* file

1. Navegue até a pasta *finetuning_dir* e abra o arquivo *fine_tune.py* no Visual Studio Code.

1. Adicione o código a seguir em *fine_tune.py*.

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

    # Configuração de logs
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
> **You can fine-tune Phi-3.5 model**
>
> In *fine_tune.py* file, you can change the `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` field in your script.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Ajuste fino do Phi-3.5.">
>

#### Add code to the *setup_ml.py* file

1. Abra o arquivo *setup_ml.py* no Visual Studio Code.

1. Adicione o código a seguir em *setup_ml.py*.

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

    # Descomente as linhas a seguir para usar uma instância CPU para treinamento
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Descomente as linhas a seguir para usar uma instância GPU para treinamento
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Substitua pela localização do seu cluster de computação
    FINETUNING_DIR = "./finetuning_dir" # Caminho para o script de fine-tuning
    TRAINING_ENV_NAME = "phi-3-training-environment" # Nome do ambiente de treinamento
    MODEL_OUTPUT_DIR = "./model_output" # Caminho para o diretório de saída do modelo no Azure ML

    # Configuração de logging para acompanhar o processo
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
            conda_file=CONDA_FILE,  # Arquivo de ambiente Conda
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
            code=FINETUNING_DIR,  # Caminho para fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Ambiente de treinamento
            compute=compute_name,  # Cluster de computação a ser usado
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Caminho para o arquivo de dados de treinamento
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Caminho para o arquivo de dados de avaliação
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Inicializar o ML Client
        ml_client = get_ml_client()

        # Criar ambiente
        env = create_or_get_environment(ml_client)
        
        # Criar ou obter cluster de computação existente
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Criar e submeter job de fine-tuning
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submeter o job
        ml_client.jobs.stream(returned_job.name)  # Transmitir os logs do job
        
        # Capturar o nome do job
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, e `LOCATION` pelos seus detalhes específicos.

    ```python
   # Descomente as linhas a seguir para usar uma instância com GPU para treinamento
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Substitua pelo local do seu cluster de computação
    ```

> [!TIP]
>
> **Guidance for fine-tuning with a minimal dataset using a CPU**
>
> If you want to use a CPU for fine-tuning, this approach is ideal for those with benefit subscriptions (such as Visual Studio Enterprise Subscription) or to quickly test the fine-tuning and deployment process.
>
> 1. Open the *setup_ml* file.
> 1. Replace `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` with your specific details.
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

1. Neste exercício, você ajustou com sucesso o modelo Phi-3 usando o Azure Machine Learning. Ao executar o script *setup_ml.py*, você configurou o ambiente Azure Machine Learning e iniciou o processo de fine-tuning definido no arquivo *fine_tune.py*. Observe que o processo de fine-tuning pode levar um tempo considerável. Após executar o comando `python setup_ml.py`, você precisará aguardar até que o processo seja concluído. Você pode monitorar o status do trabalho de fine-tuning seguindo o link fornecido no terminal para o portal Azure Machine Learning.

    ![Ver trabalho de fine-tuning.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.br.png)

### Deploy the fine-tuned model

Para integrar o modelo Phi-3 ajustado com o Prompt Flow, você precisa implantar o modelo para torná-lo acessível para inferência em tempo real. Esse processo envolve registrar o modelo, criar um endpoint online e implantar o modelo.

#### Set the model name, endpoint name, and deployment name for deployment

1. Abra o arquivo *config.py*.

1. Substitua `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` pelo nome desejado para seu modelo.

1. Substitua `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` pelo nome desejado para seu endpoint.

1. Substitua `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` pelo nome desejado para sua implantação.

#### Add code to the *deploy_model.py* file

Executar o arquivo *deploy_model.py* automatiza todo o processo de implantação. Ele registra o modelo, cria um endpoint e executa a implantação com base nas configurações especificadas no arquivo config.py, que inclui o nome do modelo, o nome do endpoint e o nome da implantação.

1. Abra o arquivo *deploy_model.py* no Visual Studio Code.

1. Adicione o código a seguir em *deploy_model.py*.

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

    # Configuração de logs
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
            # Buscar os detalhes do endpoint atual
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Registrar a alocação de tráfego atual para depuração
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Definir a alocação de tráfego para a implantação
            endpoint.traffic = {deployment_name: 100}
            
            # Atualizar o endpoint com a nova alocação de tráfego
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Registrar a alocação de tráfego atualizada para depuração
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Registrar quaisquer erros que ocorram durante o processo
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

    - Navegue até o recurso Azure Machine Learning que você criou.
    - Selecione **Studio web URL** para abrir o workspace do Azure Machine Learning.
    - Selecione **Jobs** na guia do lado esquerdo.
    - Selecione o experimento de fine-tuning. Por exemplo, *finetunephi*.
    - Selecione o job que você criou.
    - Copie e cole o nome do seu job em `JOB_NAME = "your-job-name"` no arquivo *deploy_model.py*.

1. Substitua `COMPUTE_INSTANCE_TYPE` pelos seus detalhes específicos.

1. Digite o seguinte comando para executar o script *deploy_model.py* e iniciar o processo de implantação no Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Para evitar cobranças adicionais em sua conta, certifique-se de excluir o endpoint criado no espaço de trabalho do Azure Machine Learning.
>

#### Verificar o status da implantação no espaço de trabalho do Azure Machine Learning

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até o espaço de trabalho do Azure Machine Learning que você criou.

1. Selecione **Studio web URL** para abrir o espaço de trabalho do Azure Machine Learning.

1. Selecione **Endpoints** na aba lateral esquerda.

    ![Selecione endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.br.png)

2. Selecione o endpoint que você criou.

    ![Selecione o endpoint que você criou.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.br.png)

3. Nesta página, você pode gerenciar os endpoints criados durante o processo de implantação.

## Cenário 3: Integrar com o Prompt flow e conversar com seu modelo personalizado

### Integrar o modelo Phi-3 personalizado com o Prompt flow

Após implantar com sucesso seu modelo ajustado (fine-tuned), você agora pode integrá-lo ao Prompt flow para usar seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com seu modelo Phi-3 personalizado.

#### Definir a chave da API e o URI do endpoint do modelo Phi-3 ajustado

1. Navegue até o espaço de trabalho do Azure Machine Learning que você criou.
1. Selecione **Endpoints** na aba lateral esquerda.
1. Selecione o endpoint que você criou.
1. Selecione **Consume** no menu de navegação.
1. Copie e cole seu **REST endpoint** no arquivo *config.py*, substituindo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` pelo seu **REST endpoint**.
1. Copie e cole sua **Primary key** no arquivo *config.py*, substituindo `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` pela sua **Primary key**.

    ![Copie a chave da API e o URI do endpoint.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.br.png)

#### Adicione código ao arquivo *flow.dag.yml*

1. Abra o arquivo *flow.dag.yml* no Visual Studio Code.

1. Adicione o código a seguir em *flow.dag.yml*.

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

#### Adicione código ao arquivo *integrate_with_promptflow.py*

1. Abra o arquivo *integrate_with_promptflow.py* no Visual Studio Code.

1. Adicione o código a seguir em *integrate_with_promptflow.py*.

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

    # Configuração de logs
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

### Conversar com seu modelo personalizado

1. Digite o seguinte comando para executar o script *deploy_model.py* e iniciar o processo de implantação no Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Aqui está um exemplo dos resultados: agora você pode conversar com seu modelo Phi-3 personalizado. Recomenda-se fazer perguntas com base nos dados usados para o ajuste fino.

    ![Exemplo do Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.br.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->