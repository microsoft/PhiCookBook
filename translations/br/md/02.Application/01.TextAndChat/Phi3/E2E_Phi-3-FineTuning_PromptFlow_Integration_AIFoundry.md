<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:23:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "br"
}
-->
# Ajuste fino e Integração de modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry

Este exemplo de ponta a ponta (E2E) é baseado no guia "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community. Ele apresenta os processos de ajuste fino, implantação e integração de modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry.  
Diferente do exemplo E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", que envolvia executar código localmente, este tutorial foca inteiramente no ajuste fino e integração do seu modelo dentro do Azure AI / ML Studio.

## Visão geral

Neste exemplo E2E, você aprenderá como ajustar finamente o modelo Phi-3 e integrá-lo com Prompt flow no Azure AI Foundry. Aproveitando o Azure AI / ML Studio, você estabelecerá um fluxo de trabalho para implantar e utilizar modelos de IA personalizados. Este exemplo E2E está dividido em três cenários:

**Cenário 1: Configurar recursos do Azure e preparar para ajuste fino**

**Cenário 2: Ajustar finamente o modelo Phi-3 e implantar no Azure Machine Learning Studio**

**Cenário 3: Integrar com Prompt flow e conversar com seu modelo personalizado no Azure AI Foundry**

Aqui está uma visão geral deste exemplo E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.br.png)

### Sumário

1. **[Cenário 1: Configurar recursos do Azure e preparar para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Criar um Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Solicitar cotas de GPU na assinatura do Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adicionar atribuição de função](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurar projeto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparar conjunto de dados para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 2: Ajustar finamente o modelo Phi-3 e implantar no Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ajustar finamente o modelo Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implantar o modelo Phi-3 ajustado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 3: Integrar com Prompt flow e conversar com seu modelo personalizado no Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrar o modelo Phi-3 personalizado com Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Conversar com seu modelo Phi-3 personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Cenário 1: Configurar recursos do Azure e preparar para ajuste fino

### Criar um Azure Machine Learning Workspace

1. Digite *azure machine learning* na **barra de pesquisa** no topo da página do portal e selecione **Azure Machine Learning** nas opções que aparecerem.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.br.png)

2. Selecione **+ Criar** no menu de navegação.

3. Selecione **Novo workspace** no menu de navegação.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.br.png)

4. Realize as seguintes tarefas:

    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** a ser usado (crie um novo, se necessário).
    - Insira o **Nome do Workspace**. Deve ser um valor único.
    - Selecione a **Região** que deseja usar.
    - Selecione a **Conta de armazenamento** a ser usada (crie uma nova, se necessário).
    - Selecione o **Key vault** a ser usado (crie um novo, se necessário).
    - Selecione o **Application insights** a ser usado (crie um novo, se necessário).
    - Selecione o **Container registry** a ser usado (crie um novo, se necessário).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.br.png)

5. Selecione **Revisar + criar**.

6. Selecione **Criar**.

### Solicitar cotas de GPU na assinatura do Azure

Neste tutorial, você aprenderá como ajustar finamente e implantar um modelo Phi-3, usando GPUs. Para o ajuste fino, você usará a GPU *Standard_NC24ads_A100_v4*, que requer solicitação de cota. Para implantação, usará a GPU *Standard_NC6s_v3*, que também requer solicitação de cota.

> [!NOTE]
>
> Apenas assinaturas Pay-As-You-Go (tipo padrão de assinatura) são elegíveis para alocação de GPU; assinaturas de benefício não são suportadas atualmente.
>

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Realize as seguintes tarefas para solicitar a cota da família *Standard NCADSA100v4*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **família de máquinas virtuais** a ser usada. Por exemplo, selecione **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC24ads_A100_v4*.
    - Selecione **Solicitar cota** no menu de navegação.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.br.png)

    - Na página de solicitação de cota, insira o **Novo limite de núcleos** que deseja usar. Por exemplo, 24.
    - Na página de solicitação de cota, selecione **Enviar** para solicitar a cota da GPU.

1. Realize as seguintes tarefas para solicitar a cota da família *Standard NCSv3*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **família de máquinas virtuais** a ser usada. Por exemplo, selecione **Standard NCSv3 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC6s_v3*.
    - Selecione **Solicitar cota** no menu de navegação.
    - Na página de solicitação de cota, insira o **Novo limite de núcleos** que deseja usar. Por exemplo, 24.
    - Na página de solicitação de cota, selecione **Enviar** para solicitar a cota da GPU.

### Adicionar atribuição de função

Para ajustar finamente e implantar seus modelos, você deve primeiro criar uma Identidade Gerenciada Atribuída pelo Usuário (User Assigned Managed Identity - UAI) e atribuir as permissões apropriadas. Essa UAI será usada para autenticação durante a implantação.

#### Criar User Assigned Managed Identity (UAI)

1. Digite *managed identities* na **barra de pesquisa** no topo da página do portal e selecione **Managed Identities** nas opções que aparecerem.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.br.png)

1. Selecione **+ Criar**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.br.png)

1. Realize as seguintes tarefas:

    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** a ser usado (crie um novo, se necessário).
    - Selecione a **Região** que deseja usar.
    - Insira o **Nome**. Deve ser um valor único.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.br.png)

1. Selecione **Revisar + criar**.

1. Selecione **+ Criar**.

#### Adicionar atribuição de função Contributor à Managed Identity

1. Navegue até o recurso Managed Identity que você criou.

1. Selecione **Atribuições de função do Azure** na aba lateral esquerda.

1. Selecione **+ Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, realize as seguintes tarefas:
    - Selecione o **Escopo** para **Grupo de recursos**.
    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** a ser usado.
    - Selecione a **Função** para **Colaborador (Contributor)**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.br.png)

2. Selecione **Salvar**.

#### Adicionar atribuição de função Storage Blob Data Reader à Managed Identity

1. Digite *storage accounts* na **barra de pesquisa** no topo da página do portal e selecione **Storage accounts** nas opções que aparecerem.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.br.png)

1. Selecione a conta de armazenamento associada ao Azure Machine Learning workspace que você criou. Por exemplo, *finetunephistorage*.

1. Realize as seguintes tarefas para navegar até a página Adicionar atribuição de função:

    - Navegue até a conta de armazenamento do Azure que você criou.
    - Selecione **Controle de acesso (IAM)** na aba lateral esquerda.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.br.png)

1. Na página Adicionar atribuição de função, realize as seguintes tarefas:

    - Na página Função, digite *Storage Blob Data Reader* na **barra de pesquisa** e selecione **Storage Blob Data Reader** nas opções que aparecerem.
    - Na página Função, selecione **Avançar**.
    - Na página Membros, selecione **Atribuir acesso a** **Identidade gerenciada**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar identidades gerenciadas, selecione sua **Assinatura** do Azure.
    - Na página Selecionar identidades gerenciadas, selecione a **Identidade gerenciada** para **Managed Identity**.
    - Na página Selecionar identidades gerenciadas, selecione a Managed Identity que você criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar identidades gerenciadas, selecione **Selecionar**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.br.png)

1. Selecione **Revisar + atribuir**.

#### Adicionar atribuição de função AcrPull à Managed Identity

1. Digite *container registries* na **barra de pesquisa** no topo da página do portal e selecione **Container registries** nas opções que aparecerem.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.br.png)

1. Selecione o registro de contêiner associado ao Azure Machine Learning workspace. Por exemplo, *finetunephicontainerregistry*

1. Realize as seguintes tarefas para navegar até a página Adicionar atribuição de função:

    - Selecione **Controle de acesso (IAM)** na aba lateral esquerda.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, realize as seguintes tarefas:

    - Na página Função, digite *AcrPull* na **barra de pesquisa** e selecione **AcrPull** nas opções que aparecerem.
    - Na página Função, selecione **Avançar**.
    - Na página Membros, selecione **Atribuir acesso a** **Identidade gerenciada**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar identidades gerenciadas, selecione sua **Assinatura** do Azure.
    - Na página Selecionar identidades gerenciadas, selecione a **Identidade gerenciada** para **Managed Identity**.
    - Na página Selecionar identidades gerenciadas, selecione a Managed Identity que você criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar identidades gerenciadas, selecione **Selecionar**.
    - Selecione **Revisar + atribuir**.

### Configurar projeto

Para baixar os conjuntos de dados necessários para o ajuste fino, você configurará um ambiente local.

Neste exercício, você irá:

- Criar uma pasta para trabalhar dentro dela.
- Criar um ambiente virtual.
- Instalar os pacotes necessários.
- Criar um arquivo *download_dataset.py* para baixar o conjunto de dados.

#### Criar uma pasta para trabalhar dentro dela

1. Abra uma janela do terminal e digite o seguinte comando para criar uma pasta chamada *finetune-phi* no caminho padrão.

    ```console
    mkdir finetune-phi
    ```

2. Digite o seguinte comando no terminal para navegar até a pasta *finetune-phi* que você criou.
#### Criar um ambiente virtual

1. Digite o seguinte comando no seu terminal para criar um ambiente virtual chamado *.venv*.

    ```console
    python -m venv .venv
    ```

2. Digite o seguinte comando no seu terminal para ativar o ambiente virtual.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Se funcionou, você deve ver *(.venv)* antes do prompt de comando.

#### Instalar os pacotes necessários

1. Digite os seguintes comandos no seu terminal para instalar os pacotes necessários.

    ```console
    pip install datasets==2.19.1
    ```

#### Criar `download_dataset.py`

> [!NOTE]
> Estrutura completa da pasta:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Abra o **Visual Studio Code**.

1. Selecione **File** na barra de menu.

1. Selecione **Open Folder**.

1. Selecione a pasta *finetune-phi* que você criou, localizada em *C:\Users\yourUserName\finetune-phi*.

    ![Selecione a pasta que você criou.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.br.png)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **New File** para criar um novo arquivo chamado *download_dataset.py*.

    ![Crie um novo arquivo.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.br.png)

### Preparar o dataset para fine-tuning

Neste exercício, você vai executar o arquivo *download_dataset.py* para baixar os datasets *ultrachat_200k* para o seu ambiente local. Depois, você usará esses datasets para fazer o fine-tuning do modelo Phi-3 no Azure Machine Learning.

Neste exercício, você irá:

- Adicionar código no arquivo *download_dataset.py* para baixar os datasets.
- Executar o arquivo *download_dataset.py* para baixar os datasets no seu ambiente local.

#### Baixar seu dataset usando *download_dataset.py*

1. Abra o arquivo *download_dataset.py* no Visual Studio Code.

1. Adicione o seguinte código no arquivo *download_dataset.py*.

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

1. Digite o seguinte comando no seu terminal para executar o script e baixar o dataset para o seu ambiente local.

    ```console
    python download_dataset.py
    ```

1. Verifique se os datasets foram salvos com sucesso no diretório local *finetune-phi/data*.

> [!NOTE]
>
> #### Nota sobre o tamanho do dataset e o tempo de fine-tuning
>
> Neste tutorial, você usa apenas 1% do dataset (`split='train[:1%]'`). Isso reduz significativamente a quantidade de dados, acelerando tanto o upload quanto o processo de fine-tuning. Você pode ajustar a porcentagem para encontrar o equilíbrio ideal entre o tempo de treinamento e o desempenho do modelo. Usar um subconjunto menor do dataset reduz o tempo necessário para o fine-tuning, tornando o processo mais viável para um tutorial.

## Cenário 2: Fazer fine-tuning do modelo Phi-3 e implantar no Azure Machine Learning Studio

### Fazer fine-tuning do modelo Phi-3

Neste exercício, você fará o fine-tuning do modelo Phi-3 no Azure Machine Learning Studio.

Neste exercício, você irá:

- Criar um cluster de computação para o fine-tuning.
- Fazer o fine-tuning do modelo Phi-3 no Azure Machine Learning Studio.

#### Criar cluster de computação para fine-tuning

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione **Compute** na aba lateral esquerda.

1. Selecione **Compute clusters** no menu de navegação.

1. Selecione **+ New**.

    ![Selecione compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.br.png)

1. Realize as seguintes configurações:

    - Selecione a **Região** que deseja usar.
    - Selecione o **Virtual machine tier** para **Dedicated**.
    - Selecione o **Virtual machine type** para **GPU**.
    - No filtro de **Virtual machine size**, selecione **Select from all options**.
    - Selecione o **Virtual machine size** para **Standard_NC24ads_A100_v4**.

    ![Criar cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.br.png)

1. Selecione **Next**.

1. Realize as seguintes configurações:

    - Informe o **Compute name**. Deve ser um valor único.
    - Selecione o **Minimum number of nodes** para **0**.
    - Selecione o **Maximum number of nodes** para **1**.
    - Selecione o **Idle seconds before scale down** para **120**.

    ![Criar cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.br.png)

1. Selecione **Create**.

#### Fazer fine-tuning do modelo Phi-3

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o workspace do Azure Machine Learning que você criou.

    ![Selecione o workspace que você criou.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.br.png)

1. Realize as seguintes ações:

    - Selecione **Model catalog** na aba lateral esquerda.
    - Digite *phi-3-mini-4k* na **barra de busca** e selecione **Phi-3-mini-4k-instruct** nas opções que aparecerem.

    ![Digite phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.br.png)

1. Selecione **Fine-tune** no menu de navegação.

    ![Selecione fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.br.png)

1. Realize as seguintes configurações:

    - Selecione **Select task type** para **Chat completion**.
    - Selecione **+ Select data** para enviar os **Training data**.
    - Selecione o tipo de upload dos dados de validação para **Provide different validation data**.
    - Selecione **+ Select data** para enviar os **Validation data**.

    ![Preencha a página de fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.br.png)

    > [!TIP]
    >
    > Você pode selecionar **Advanced settings** para personalizar configurações como **learning_rate** e **lr_scheduler_type** para otimizar o processo de fine-tuning conforme suas necessidades específicas.

1. Selecione **Finish**.

1. Neste exercício, você fez o fine-tuning do modelo Phi-3 usando o Azure Machine Learning. Note que o processo de fine-tuning pode levar um tempo considerável. Após iniciar o job de fine-tuning, é necessário aguardar sua conclusão. Você pode acompanhar o status do job na aba Jobs, no lado esquerdo do seu workspace do Azure Machine Learning. Na próxima série, você irá implantar o modelo fine-tuned e integrá-lo com o Prompt flow.

    ![Veja o job de fine-tuning.](../../../../../../translated_images/06-08-output.2bd32e59930672b1.br.png)

### Implantar o modelo Phi-3 fine-tuned

Para integrar o modelo Phi-3 fine-tuned com o Prompt flow, é necessário implantar o modelo para que ele fique acessível para inferência em tempo real. Esse processo envolve registrar o modelo, criar um endpoint online e implantar o modelo.

Neste exercício, você irá:

- Registrar o modelo fine-tuned no workspace do Azure Machine Learning.
- Criar um endpoint online.
- Implantar o modelo Phi-3 fine-tuned registrado.

#### Registrar o modelo fine-tuned

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o workspace do Azure Machine Learning que você criou.

    ![Selecione o workspace que você criou.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.br.png)

1. Selecione **Models** na aba lateral esquerda.

1. Selecione **+ Register**.

1. Selecione **From a job output**.

    ![Registrar modelo.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.br.png)

1. Selecione o job que você criou.

    ![Selecione o job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.br.png)

1. Selecione **Next**.

1. Selecione **Model type** para **MLflow**.

1. Certifique-se de que **Job output** está selecionado; isso deve ocorrer automaticamente.

    ![Selecione a saída.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.br.png)

2. Selecione **Next**.

3. Selecione **Register**.

    ![Selecione registrar.](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.br.png)

4. Você pode visualizar seu modelo registrado navegando até o menu **Models** na aba lateral esquerda.

    ![Modelo registrado.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.br.png)

#### Implantar o modelo fine-tuned

1. Navegue até o workspace do Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba lateral esquerda.

1. Selecione **Real-time endpoints** no menu de navegação.

    ![Criar endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.br.png)

1. Selecione **Create**.

1. Selecione o modelo registrado que você criou.

    ![Selecione o modelo registrado.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.br.png)

1. Selecione **Select**.

1. Realize as seguintes configurações:

    - Selecione **Virtual machine** para *Standard_NC6s_v3*.
    - Selecione a **Quantidade de instâncias** que deseja usar. Por exemplo, *1*.
    - Selecione **Endpoint** para **New** para criar um endpoint.
    - Informe o **Nome do endpoint**. Deve ser um valor único.
    - Informe o **Nome da implantação**. Deve ser um valor único.

    ![Preencha as configurações de implantação.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.br.png)

1. Selecione **Deploy**.

> [!WARNING]
> Para evitar cobranças adicionais na sua conta, certifique-se de excluir o endpoint criado no workspace do Azure Machine Learning.
>

#### Verificar status da implantação no Azure Machine Learning Workspace

1. Navegue até o workspace do Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba lateral esquerda.

1. Selecione o endpoint que você criou.

    ![Selecione endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.br.png)

1. Nesta página, você pode gerenciar os endpoints durante o processo de implantação.

> [!NOTE]
> Após a implantação ser concluída, certifique-se de que o **Live traffic** esteja configurado para **100%**. Se não estiver, selecione **Update traffic** para ajustar as configurações de tráfego. Note que não é possível testar o modelo se o tráfego estiver configurado para 0%.
>
> ![Configurar tráfego.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.br.png)
>

## Cenário 3: Integrar com Prompt flow e conversar com seu modelo customizado no Azure AI Foundry

### Integrar o modelo Phi-3 customizado com Prompt flow

Após implantar com sucesso seu modelo fine-tuned, você pode integrá-lo com o Prompt Flow para usar seu modelo em aplicações em tempo real, possibilitando diversas tarefas interativas com seu modelo Phi-3 customizado.

Neste exercício, você irá:

- Criar o Azure AI Foundry Hub.
- Criar um projeto no Azure AI Foundry.
- Criar um Prompt flow.
- Adicionar uma conexão customizada para o modelo Phi-3 fine-tuned.
- Configurar o Prompt flow para conversar com seu modelo Phi-3 customizado.
> [!NOTE]
> Você também pode integrar com o Promptflow usando o Azure ML Studio. O mesmo processo de integração pode ser aplicado ao Azure ML Studio.
#### Criar Azure AI Foundry Hub

Você precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo que você organize e gerencie vários Projetos dentro do Azure AI Foundry.

1. Acesse [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selecione **All hubs** na aba do lado esquerdo.

1. Selecione **+ New hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.br.png)

1. Realize as seguintes tarefas:

    - Insira o **Hub name**. Deve ser um valor único.
    - Selecione sua **Subscription** do Azure.
    - Selecione o **Resource group** que deseja usar (crie um novo, se necessário).
    - Selecione a **Location** que deseja utilizar.
    - Selecione o **Connect Azure AI Services** que deseja usar (crie um novo, se necessário).
    - Selecione **Connect Azure AI Search** para **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.br.png)

1. Selecione **Next**.

#### Criar Projeto Azure AI Foundry

1. No Hub que você criou, selecione **All projects** na aba do lado esquerdo.

1. Selecione **+ New project** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.br.png)

1. Insira o **Project name**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.br.png)

1. Selecione **Create a project**.

#### Adicionar uma conexão personalizada para o modelo Phi-3 fine-tuned

Para integrar seu modelo Phi-3 customizado com o Prompt flow, você precisa salvar o endpoint e a chave do modelo em uma conexão personalizada. Essa configuração garante o acesso ao seu modelo Phi-3 customizado no Prompt flow.

#### Definir a chave da API e o URI do endpoint do modelo Phi-3 fine-tuned

1. Acesse [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue até o workspace do Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.br.png)

1. Selecione o endpoint que você criou.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.br.png)

1. Selecione **Consume** no menu de navegação.

1. Copie seu **REST endpoint** e a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.br.png)

#### Adicionar a Conexão Personalizada

1. Acesse [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue até o projeto Azure AI Foundry que você criou.

1. No projeto que você criou, selecione **Settings** na aba do lado esquerdo.

1. Selecione **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.br.png)

1. Selecione **Custom keys** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.br.png)

1. Realize as seguintes tarefas:

    - Selecione **+ Add key value pairs**.
    - Para o nome da chave, insira **endpoint** e cole o endpoint copiado do Azure ML Studio no campo de valor.
    - Selecione **+ Add key value pairs** novamente.
    - Para o nome da chave, insira **key** e cole a chave copiada do Azure ML Studio no campo de valor.
    - Após adicionar as chaves, selecione **is secret** para evitar que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.br.png)

1. Selecione **Add connection**.

#### Criar Prompt flow

Você adicionou uma conexão personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow seguindo os passos abaixo. Depois, você conectará esse Prompt flow à conexão personalizada para poder usar o modelo fine-tuned dentro do Prompt flow.

1. Navegue até o projeto Azure AI Foundry que você criou.

1. Selecione **Prompt flow** na aba do lado esquerdo.

1. Selecione **+ Create** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.br.png)

1. Selecione **Chat flow** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.br.png)

1. Insira o **Folder name** que deseja usar.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.br.png)

2. Selecione **Create**.

#### Configurar Prompt flow para conversar com seu modelo Phi-3 customizado

Você precisa integrar o modelo Phi-3 fine-tuned em um Prompt flow. No entanto, o Prompt flow existente não foi projetado para esse propósito. Portanto, é necessário redesenhar o Prompt flow para permitir a integração do modelo customizado.

1. No Prompt flow, realize as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Raw file mode**.
    - Apague todo o código existente no arquivo *flow.dag.yml*.
    - Adicione o seguinte código no arquivo *flow.dag.yml*.

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

    - Selecione **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.br.png)

1. Adicione o seguinte código no arquivo *integrate_with_promptflow.py* para usar o modelo Phi-3 customizado no Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.br.png)

> [!NOTE]
> Para informações mais detalhadas sobre o uso do Prompt flow no Azure AI Foundry, você pode consultar [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Chat input**, **Chat output** para habilitar o chat com seu modelo.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.br.png)

1. Agora você está pronto para conversar com seu modelo Phi-3 customizado. No próximo exercício, você aprenderá como iniciar o Prompt flow e usá-lo para conversar com seu modelo Phi-3 fine-tuned.

> [!NOTE]
>
> O fluxo reconstruído deve ficar parecido com a imagem abaixo:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.br.png)
>

### Conversar com seu modelo Phi-3 customizado

Agora que você fine-tunou e integrou seu modelo Phi-3 customizado com o Prompt flow, está pronto para começar a interagir com ele. Este exercício irá guiá-lo pelo processo de configuração e início de uma conversa com seu modelo usando o Prompt flow. Seguindo esses passos, você poderá aproveitar ao máximo as capacidades do seu modelo Phi-3 fine-tuned para diversas tarefas e conversas.

- Converse com seu modelo Phi-3 customizado usando o Prompt flow.

#### Iniciar Prompt flow

1. Selecione **Start compute sessions** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.br.png)

1. Selecione **Validate and parse input** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.br.png)

1. Selecione o **Value** da **connection** para a conexão personalizada que você criou. Por exemplo, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.br.png)

#### Conversar com seu modelo customizado

1. Selecione **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.br.png)

1. Aqui está um exemplo dos resultados: agora você pode conversar com seu modelo Phi-3 customizado. Recomenda-se fazer perguntas baseadas nos dados usados para o fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.br.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.