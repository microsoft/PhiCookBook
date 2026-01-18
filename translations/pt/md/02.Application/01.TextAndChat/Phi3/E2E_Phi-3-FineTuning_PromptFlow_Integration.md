<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T14:05:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "pt"
}
-->
# Ajustar e Integrar modelos Phi-3 personalizados com Prompt flow

Este exemplo de ponta a ponta (E2E) baseia-se no guia "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community. Introduz os processos de ajuste fino, implementação e integração de modelos Phi-3 personalizados com Prompt flow.

## Visão geral

Neste exemplo E2E, irá aprender a ajustar o modelo Phi-3 e integrá-lo com Prompt flow. Ao tirar partido do Azure Machine Learning e do Prompt flow, irá estabelecer um fluxo de trabalho para implementar e utilizar modelos de IA personalizados. Este exemplo E2E está dividido em três cenários:

**Cenário 1: Configurar recursos Azure e Preparar para ajuste fino**

**Cenário 2: Ajustar o modelo Phi-3 e Implementar no Azure Machine Learning Studio**

**Cenário 3: Integrar com Prompt flow e Conversar com o seu modelo personalizado**

Aqui está uma visão geral deste exemplo E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/pt/00-01-architecture.02fc569e266d468c.webp)

### Índice

1. **[Cenário 1: Configurar recursos Azure e Preparar para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Criar um Workspace Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Solicitar quotas de GPU na Subscrição Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adicionar atribuição de funções](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurar projeto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparar dataset para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 2: Ajustar o modelo Phi-3 e Implementar no Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Configurar Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ajustar o modelo Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementar o modelo ajustado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 3: Integrar com Prompt flow e Conversar com o seu modelo personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrar o modelo Phi-3 personalizado com Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Conversar com o seu modelo personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Cenário 1: Configurar recursos Azure e Preparar para ajuste fino

### Criar um Workspace Azure Machine Learning

1. Escreva *azure machine learning* na **barra de pesquisa** no topo da página do portal e selecione **Azure Machine Learning** nas opções que aparecem.

    ![Type azure machine learning](../../../../../../translated_images/pt/01-01-type-azml.a5116f8454d98c60.webp)

1. Selecione **+ Create** no menu de navegação.

1. Selecione **New workspace** no menu de navegação.

    ![Select new workspace](../../../../../../translated_images/pt/01-02-select-new-workspace.83e17436f8898dc4.webp)

1. Realize as seguintes tarefas:

    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo caso necessário).
    - Introduza o **Nome do Workspace**. Deve ser um valor único.
    - Selecione a **Região** que pretende usar.
    - Selecione a **Conta de armazenamento** a utilizar (crie uma nova se necessário).
    - Selecione o **Key vault** a utilizar (crie um novo se necessário).
    - Selecione o **Application insights** a utilizar (crie um novo se necessário).
    - Selecione o **Container registry** a utilizar (crie um novo se necessário).

    ![Fill AZML.](../../../../../../translated_images/pt/01-03-fill-AZML.730a5177757bbebb.webp)

1. Selecione **Review + Create**.

1. Selecione **Create**.

### Solicitar quotas de GPU na Subscrição Azure

Neste exemplo E2E, irá usar o *Standard_NC24ads_A100_v4 GPU* para ajuste fino, que requer uma solicitação de quota, e o *Standard_E4s_v3* CPU para implementação, que não requer solicitação de quota.

> [!NOTE]
>
> Apenas subscrições Pay-As-You-Go (tipo de subscrição padrão) são elegíveis para atribuição de GPU; subscrições com benefícios não são atualmente suportadas.
>
> Para quem utiliza subscrições com benefícios (como Visual Studio Enterprise Subscription) ou para quem deseja testar rapidamente o processo de ajuste fino e implementação, este tutorial também fornece orientações para ajuste fino com um conjunto de dados mínimo usando uma CPU. No entanto, é importante notar que os resultados do ajuste fino são significativamente melhores ao usar GPU com conjuntos de dados maiores.

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Realize as seguintes tarefas para solicitar quota da família *Standard NCADSA100v4*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **Família de máquinas virtuais** a usar. Por exemplo, selecione **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC24ads_A100_v4*.
    - Selecione a opção **Request quota** no menu de navegação.

        ![Request quota.](../../../../../../translated_images/pt/01-04-request-quota.3d3670c3221ab834.webp)

    - Dentro da página Request quota, introduza o **Novo limite de núcleos** que deseja usar. Por exemplo, 24.
    - Dentro da página Request quota, selecione **Submit** para solicitar a quota de GPU.

> [!NOTE]
> Pode selecionar a GPU ou CPU apropriada às suas necessidades consultando o documento [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Adicionar atribuição de função

Para ajustar e implementar os seus modelos, deve primeiro criar uma Identidade Gerida Atribuída pelo Utilizador (UAI) e atribuir-lhe as permissões apropriadas. Esta UAI será usada para autenticação durante a implementação.

#### Criar Identidade Gerida Atribuída pelo Utilizador (UAI)

1. Escreva *managed identities* na **barra de pesquisa** no topo da página do portal e selecione **Managed Identities** nas opções que aparecem.

    ![Type managed identities.](../../../../../../translated_images/pt/01-05-type-managed-identities.9297b6039874eff8.webp)

1. Selecione **+ Create**.

    ![Select create.](../../../../../../translated_images/pt/01-06-select-create.936d8d66d7144f9a.webp)

1. Realize as seguintes tarefas:

    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a usar (crie um novo caso necessário).
    - Selecione a **Região** que deseja usar.
    - Introduza o **Nome**. Deve ser um valor único.

1. Selecione **Review + create**.

1. Selecione **+ Create**.

#### Adicionar atribuição da função Contribuidor à Identidade Gerida

1. Navegue até ao recurso da Identidade Gerida que criou.

1. Selecione **Azure role assignments** na aba lateral esquerda.

1. Selecione **+Add role assignment** no menu de navegação.

1. Dentro da página Add role assignment, realize as seguintes tarefas:
    - Selecione o **Escopo** para **Resource group**.
    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a usar.
    - Selecione a **Função** para **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/pt/01-07-fill-contributor-role.29ca99b7c9f687e0.webp)

1. Selecione **Save**.

#### Adicionar atribuição da função Storage Blob Data Reader à Identidade Gerida

1. Escreva *storage accounts* na **barra de pesquisa** no topo da página do portal e selecione **Storage accounts** nas opções que aparecem.

    ![Type storage accounts.](../../../../../../translated_images/pt/01-08-type-storage-accounts.1186c8e42933e49b.webp)

1. Selecione a conta de armazenamento associada ao workspace Azure Machine Learning que criou. Por exemplo, *finetunephistorage*.

1. Realize as seguintes tarefas para navegar até à página Add role assignment:

    - Navegue até à conta de armazenamento Azure que criou.
    - Selecione **Access Control (IAM)** na aba lateral esquerda.
    - Selecione **+ Add** no menu de navegação.
    - Selecione **Add role assignment** no menu de navegação.

    ![Add role.](../../../../../../translated_images/pt/01-09-add-role.d2db22fec1b187f0.webp)

1. Dentro da página Add role assignment, realize as seguintes tarefas:

    - Na página Role, escreva *Storage Blob Data Reader* na **barra de pesquisa** e selecione **Storage Blob Data Reader** nas opções que aparecem.
    - Na página Role, selecione **Next**.
    - Na página Members, selecione **Assign access to** **Managed identity**.
    - Na página Members, selecione **+ Select members**.
    - Na página Select managed identities, selecione a sua **Subscrição** Azure.
    - Na página Select managed identities, selecione a **Identidade Gerida** para **Manage Identity**.
    - Na página Select managed identities, selecione a Identidade Gerida que criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Select managed identities, selecione **Select**.

    ![Select managed identity.](../../../../../../translated_images/pt/01-10-select-managed-identity.5ce5ba181f72a4df.webp)

1. Selecione **Review + assign**.

#### Adicionar atribuição da função AcrPull à Identidade Gerida

1. Escreva *container registries* na **barra de pesquisa** no topo da página do portal e selecione **Container registries** nas opções que aparecem.

    ![Type container registries.](../../../../../../translated_images/pt/01-11-type-container-registries.ff3b8bdc49dc596c.webp)

1. Selecione o container registry associado ao workspace Azure Machine Learning. Por exemplo, *finetunephicontainerregistries*

1. Realize as seguintes tarefas para navegar até à página Add role assignment:

    - Selecione **Access Control (IAM)** na aba lateral esquerda.
    - Selecione **+ Add** no menu de navegação.
    - Selecione **Add role assignment** no menu de navegação.

1. Dentro da página Add role assignment, realize as seguintes tarefas:

    - Na página Role, escreva *AcrPull* na **barra de pesquisa** e selecione **AcrPull** nas opções que aparecem.
    - Na página Role, selecione **Next**.
    - Na página Members, selecione **Assign access to** **Managed identity**.
    - Na página Members, selecione **+ Select members**.
    - Na página Select managed identities, selecione a sua **Subscrição** Azure.
    - Na página Select managed identities, selecione a **Identidade Gerida** para **Manage Identity**.
    - Na página Select managed identities, selecione a Identidade Gerida que criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Select managed identities, selecione **Select**.
    - Selecione **Review + assign**.

### Configurar projeto

Agora, irá criar uma pasta para trabalhar e configurar um ambiente virtual para desenvolver um programa que interage com os utilizadores e usa o histórico de conversas armazenado no Azure Cosmos DB para informar as suas respostas.

#### Criar uma pasta para trabalhar dentro dela

1. Abra uma janela de terminal e escreva o seguinte comando para criar uma pasta chamada *finetune-phi* no caminho predefinido.

    ```console
    mkdir finetune-phi
    ```

1. Escreva o seguinte comando no seu terminal para navegar até à pasta *finetune-phi* que criou.

    ```console
    cd finetune-phi
    ```

#### Criar um ambiente virtual

1. Escreva o seguinte comando no seu terminal para criar um ambiente virtual chamado *.venv*.

    ```console
    python -m venv .venv
    ```

1. Escreva o seguinte comando no seu terminal para ativar o ambiente virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Se funcionar, deverá ver *(.venv)* antes do prompt de comando.

#### Instalar os pacotes necessários

1. Escreva os seguintes comandos no seu terminal para instalar os pacotes necessários.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Criar arquivos do projeto
Neste exercício, irá criar os ficheiros essenciais para o nosso projeto. Estes ficheiros incluem scripts para descarregar o conjunto de dados, configurar o ambiente Azure Machine Learning, realizar o fine-tuning do modelo Phi-3 e implementar o modelo ajustado. Também irá criar um ficheiro *conda.yml* para configurar o ambiente de fine-tuning.

Neste exercício, irá:

- Criar um ficheiro *download_dataset.py* para descarregar o conjunto de dados.
- Criar um ficheiro *setup_ml.py* para configurar o ambiente Azure Machine Learning.
- Criar um ficheiro *fine_tune.py* na pasta *finetuning_dir* para realizar o fine-tuning do modelo Phi-3 usando o conjunto de dados.
- Criar um ficheiro *conda.yml* para configurar o ambiente de fine-tuning.
- Criar um ficheiro *deploy_model.py* para implementar o modelo ajustado.
- Criar um ficheiro *integrate_with_promptflow.py*, para integrar o modelo ajustado e executar o modelo usando Prompt flow.
- Criar um ficheiro flow.dag.yml, para configurar a estrutura do fluxo de trabalho para o Prompt flow.
- Criar um ficheiro *config.py* para inserir informação da Azure.

> [!NOTE]
>
> Estrutura completa da pasta:
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

1. Selecione **Ficheiro** na barra de menu.

1. Selecione **Abrir Pasta**.

1. Selecione a pasta *finetune-phi* que criou, que está localizada em *C:\Users\yourUserName\finetune-phi*.

    ![Abrir pasta do projeto.](../../../../../../translated_images/pt/01-12-open-project-folder.1fff9c7f41dd1639.webp)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *download_dataset.py*.

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *setup_ml.py*.

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *deploy_model.py*.

    ![Criar novo ficheiro.](../../../../../../translated_images/pt/01-13-create-new-file.c17c150fff384a39.webp)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Nova Pasta** para criar uma nova pasta chamada *finetuning_dir*.

1. Na pasta *finetuning_dir*, crie um novo ficheiro chamado *fine_tune.py*.

#### Criar e Configurar o ficheiro *conda.yml*

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um ficheiro chamado *conda.yml*.

1. Adicione o seguinte código ao ficheiro *conda.yml* para configurar o ambiente de fine-tuning para o modelo Phi-3.

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

#### Criar e Configurar o ficheiro *config.py*

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um ficheiro chamado *config.py*.

1. Adicione o seguinte código ao ficheiro *config.py* para incluir a sua informação da Azure.

    ```python
    # Configurações do Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Configurações do Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Configurações da Identidade Gerida do Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Caminhos dos ficheiros do conjunto de dados
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Configurações do modelo afinado
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Adicionar variáveis de ambiente Azure

1. Execute as seguintes tarefas para adicionar o ID da Subscrição Azure:

    - Escreva *subscriptions* na **barra de pesquisa** no topo da página do portal e selecione **Subscriptions** nas opções que aparecem.
    - Selecione a Subscrição Azure que está a usar atualmente.
    - Copie e cole o seu ID de Subscrição no ficheiro *config.py*.

    ![Encontrar id da subscrição.](../../../../../../translated_images/pt/01-14-find-subscriptionid.4f4ca33555f1e637.webp)

1. Execute as seguintes tarefas para adicionar o Nome do Workspace Azure:

    - Navegue até ao recurso Azure Machine Learning que criou.
    - Copie e cole o nome da sua conta no ficheiro *config.py*.

    ![Encontrar nome Azure Machine Learning.](../../../../../../translated_images/pt/01-15-find-AZML-name.1975f0422bca19a7.webp)

1. Execute as seguintes tarefas para adicionar o Nome do Grupo de Recursos Azure:

    - Navegue até ao recurso Azure Machine Learning que criou.
    - Copie e cole o Nome do seu Grupo de Recursos Azure no ficheiro *config.py*.

    ![Encontrar nome do grupo de recursos.](../../../../../../translated_images/pt/01-16-find-AZML-resourcegroup.855a349d0af134a3.webp)

2. Execute as seguintes tarefas para adicionar o nome da Identidade Gerida Azure

    - Navegue até ao recurso Managed Identities que criou.
    - Copie e cole o nome da sua Identidade Gerida Azure no ficheiro *config.py*.

    ![Encontrar UAI.](../../../../../../translated_images/pt/01-17-find-uai.3529464f53499827.webp)

### Preparar conjunto de dados para fine-tuning

Neste exercício, vai executar o ficheiro *download_dataset.py* para descarregar os conjuntos de dados *ULTRACHAT_200k* para o seu ambiente local. Depois, irá usar estes conjuntos de dados para realizar o fine-tuning do modelo Phi-3 em Azure Machine Learning.

#### Descarregar o conjunto de dados usando *download_dataset.py*

1. Abra o ficheiro *download_dataset.py* no Visual Studio Code.

1. Adicione o seguinte código dentro do *download_dataset.py*.

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
        # Criar o diretório se não existir
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Abrir o ficheiro em modo de escrita
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterar sobre cada registo no conjunto de dados
            for record in dataset:
                # Descarregar o registo como um objeto JSON e escrevê-lo no ficheiro
                json.dump(record, f)
                # Escrever um carácter de nova linha para separar os registos
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

        # Guardar o conjunto de dados de treino num ficheiro JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Guardar o conjunto de dados de teste num ficheiro JSONL separado
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Orientação para fine-tuning com um conjunto de dados mínimo usando CPU**
>
> Se quiser usar uma CPU para fine-tuning, esta abordagem é ideal para quem tem subscrições de benefício (como Visual Studio Enterprise Subscription) ou para testar rapidamente o processo de fine-tuning e implementação.
>
> Substitua `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` por `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Escreva o seguinte comando no seu terminal para executar o script e descarregar o conjunto de dados para o seu ambiente local.

    ```console
    python download_data.py
    ```

1. Verifique que os conjuntos de dados foram guardados com sucesso na sua diretoria local *finetune-phi/data*.

> [!NOTE]
>
> **Tamanho do conjunto de dados e tempo de fine-tuning**
>
> Neste exemplo E2E, usa apenas 1% do conjunto de dados (`train_sft[:1%]`). Isto reduz significativamente a quantidade de dados, acelerando o processo de upload e fine-tuning. Pode ajustar a percentagem para encontrar o equilíbrio certo entre o tempo de treino e o desempenho do modelo. Usar um subconjunto menor do conjunto de dados reduz o tempo necessário para o fine-tuning, tornando o processo mais gerível para um exemplo E2E.

## Cenário 2: Ajustar o modelo Phi-3 e Implementar no Azure Machine Learning Studio

### Configurar Azure CLI

É necessário configurar a Azure CLI para autenticar o seu ambiente. A Azure CLI permite gerir recursos Azure diretamente a partir da linha de comandos e fornece as credenciais necessárias para o Azure Machine Learning aceder a esses recursos. Para começar, instale a [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Abra uma janela de terminal e escreva o seguinte comando para iniciar sessão na sua conta Azure.

    ```console
    az login
    ```

1. Selecione a sua conta Azure a usar.

1. Selecione a subscrição Azure a usar.

    ![Encontrar nome do grupo de recursos.](../../../../../../translated_images/pt/02-01-login-using-azure-cli.dfde31cb75e58a87.webp)

> [!TIP]
>
> Se tiver problemas em iniciar sessão na Azure, experimente usar um código de dispositivo. Abra uma janela de terminal e escreva o seguinte comando para iniciar sessão na sua conta Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Ajustar o modelo Phi-3

Neste exercício, irá realizar o fine-tuning do modelo Phi-3 usando o conjunto de dados fornecido. Primeiro, irá definir o processo de fine-tuning no ficheiro *fine_tune.py*. Depois, irá configurar o ambiente Azure Machine Learning e iniciar o processo de fine-tuning executando o ficheiro *setup_ml.py*. Este script garante que o fine-tuning ocorre dentro do ambiente Azure Machine Learning.

Ao executar *setup_ml.py*, irá executar o processo de fine-tuning no ambiente Azure Machine Learning.

#### Adicionar código ao ficheiro *fine_tune.py*

1. Navegue até à pasta *finetuning_dir* e abra o ficheiro *fine_tune.py* no Visual Studio Code.

1. Adicione o seguinte código dentro do *fine_tune.py*.

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

    # Para evitar o erro INVALID_PARAMETER_VALUE no MLflow, desative a integração com MLflow
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
> No ficheiro *fine_tune.py*, pode alterar o `pretrained_model_name` de `"microsoft/Phi-3-mini-4k-instruct"` para qualquer modelo que queira ajustar. Por exemplo, se o alterar para `"microsoft/Phi-3.5-mini-instruct"`, estará a usar o modelo Phi-3.5-mini-instruct para o fine-tuning. Para encontrar e usar o nome do modelo que preferir, visite [Hugging Face](https://huggingface.co/), pesquise o modelo do seu interesse e copie e cole o seu nome no campo `pretrained_model_name` no seu script.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Ajustar modelo Phi-3.5.">
>

#### Adicionar código ao ficheiro *setup_ml.py*

1. Abra o ficheiro *setup_ml.py* no Visual Studio Code.

1. Adicione o seguinte código dentro do *setup_ml.py*.

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

    # Descomente as seguintes linhas para usar uma instância CPU para treino
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Descomente as seguintes linhas para usar uma instância GPU para treino
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Substitua pela localização do seu cluster de computação
    FINETUNING_DIR = "./finetuning_dir" # Caminho para o script de fine-tuning
    TRAINING_ENV_NAME = "phi-3-training-environment" # Nome do ambiente de treino
    MODEL_OUTPUT_DIR = "./model_output" # Caminho para o diretório de saída do modelo no azure ml

    # Configuração de logging para seguir o processo
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
            conda_file=CONDA_FILE,  # Ficheiro de ambiente Conda
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
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Aguarde pela criação do cluster
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
            environment=env,  # Ambiente de treino
            compute=compute_name,  # Cluster de computação a usar
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
        # Inicializar o Cliente ML
        ml_client = get_ml_client()

        # Criar Ambiente
        env = create_or_get_environment(ml_client)
        
        # Criar ou obter cluster de computação existente
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Criar e Submeter o Trabalho de Fine-Tuning
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submeter o trabalho
        ml_client.jobs.stream(returned_job.name)  # Transmitir os logs do trabalho
        
        # Capturar o nome do trabalho
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` e `LOCATION` pelos seus detalhes específicos.

    ```python
   # Remova o comentário das linhas seguintes para usar uma instância GPU para treino
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Substitua pelo local do seu cluster de computação
    ```

> [!TIP]
>
> **Orientação para fine-tuning com um conjunto de dados mínimo usando CPU**
>
> Se quiser usar uma CPU para fine-tuning, esta abordagem é ideal para quem tem subscrições de benefício (como Visual Studio Enterprise Subscription) ou para testar rapidamente o processo de fine-tuning e implementação.
>
> 1. Abra o ficheiro *setup_ml*.
> 1. Substitua `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` e `DOCKER_IMAGE_NAME` pelos seguintes valores. Se não tiver acesso a *Standard_E16s_v3*, pode usar uma instância CPU equivalente ou solicitar uma nova quota.
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

1. Neste exercício, ajustou com sucesso o modelo Phi-3 usando o Azure Machine Learning. Ao executar o script *setup_ml.py*, configurou o ambiente Azure Machine Learning e iniciou o processo de fine-tuning definido no ficheiro *fine_tune.py*. Note que o processo de fine-tuning pode demorar um tempo considerável. Após executar o comando `python setup_ml.py`, terá que aguardar a conclusão do processo. Pode monitorizar o estado do trabalho de fine-tuning seguindo o link fornecido no terminal para o portal Azure Machine Learning.

    ![Ver trabalho de fine-tuning.](../../../../../../translated_images/pt/02-02-see-finetuning-job.59393bc3b143871e.webp)

### Implementar o modelo ajustado

Para integrar o modelo Phi-3 ajustado com o Prompt Flow, é necessário implementar o modelo para o tornar acessível para inferência em tempo real. Este processo envolve registar o modelo, criar um endpoint online e implementar o modelo.

#### Definir o nome do modelo, nome do endpoint e nome da implementação para a implementação

1. Abra o ficheiro *config.py*.

1. Substitua `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` pelo nome desejado para o seu modelo.

1. Substitua `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` pelo nome desejado para o seu endpoint.

1. Substitua `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` pelo nome desejado para a sua implementação.

#### Adicionar código ao ficheiro *deploy_model.py*

Executar o ficheiro *deploy_model.py* automatiza todo o processo de implementação. Regista o modelo, cria um endpoint e executa a implementação com base nas definições especificadas no ficheiro config.py, que inclui o nome do modelo, nome do endpoint e nome da implementação.

1. Abra o ficheiro *deploy_model.py* no Visual Studio Code.

1. Adicione o seguinte código dentro do *deploy_model.py*.

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

    # Configuração de registo
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
    - Selecione **Studio web URL** para abrir o workspace Azure Machine Learning.
    - Selecione **Jobs** na aba lateral esquerda.
    - Selecione o experimento de fine-tuning. Por exemplo, *finetunephi*.
    - Selecione o trabalho que criou.
    - Copie e cole o nome do seu trabalho em `JOB_NAME = "your-job-name"` no ficheiro *deploy_model.py*.

1. Substitua `COMPUTE_INSTANCE_TYPE` pelos seus detalhes específicos.

1. Escreva o seguinte comando para executar o script *deploy_model.py* e iniciar o processo de implantação no Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Para evitar encargos adicionais na sua conta, certifique-se de eliminar o endpoint criado no espaço de trabalho do Azure Machine Learning.
>

#### Verificar o estado da implantação no Espaço de Trabalho Azure Machine Learning

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até ao espaço de trabalho Azure Machine Learning que criou.

1. Selecione **Studio web URL** para abrir o espaço de trabalho Azure Machine Learning.

1. Selecione **Endpoints** na aba do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/pt/02-03-select-endpoints.c3136326510baff1.webp)

2. Selecione o endpoint que criou.

    ![Select endpoints that you created.](../../../../../../translated_images/pt/02-04-select-endpoint-created.0363e7dca51dabb4.webp)

3. Nesta página, pode gerir os endpoints criados durante o processo de implantação.

## Cenário 3: Integrar com Prompt flow e Conversar com o seu modelo personalizado

### Integrar o modelo personalizado Phi-3 com Prompt flow

Após implantar com sucesso o seu modelo ajustado, pode agora integrá-lo com o Prompt flow para usar o seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com o seu modelo Phi-3 personalizado.

#### Defina a chave API e a URI do endpoint do modelo Phi-3 ajustado

1. Navegue até ao espaço de trabalho Azure Machine Learning que criou.
1. Selecione **Endpoints** na aba do lado esquerdo.
1. Selecione o endpoint que criou.
1. Selecione **Consume** no menu de navegação.
1. Copie e cole o seu **endpoint REST** no ficheiro *config.py*, substituindo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` pelo seu **endpoint REST**.
1. Copie e cole a sua **Chave Primária** no ficheiro *config.py*, substituindo `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` pela sua **Chave Primária**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pt/02-05-copy-apikey-endpoint.88b5a92e6462c53b.webp)

#### Adicione código ao ficheiro *flow.dag.yml*

1. Abra o ficheiro *flow.dag.yml* no Visual Studio Code.

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

#### Adicione código ao ficheiro *integrate_with_promptflow.py*

1. Abra o ficheiro *integrate_with_promptflow.py* no Visual Studio Code.

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

    # Configuração de registo
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

### Converse com o seu modelo personalizado

1. Escreva o seguinte comando para executar o script *deploy_model.py* e iniciar o processo de implantação no Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Eis um exemplo dos resultados: Agora pode conversar com o seu modelo Phi-3 personalizado. Recomenda-se que faça perguntas baseadas nos dados usados para o fine-tuning.

    ![Prompt flow example.](../../../../../../translated_images/pt/02-06-promptflow-example.89384abaf3ad71f6.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informação crítica, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->