<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:00:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "pt"
}
-->
# Ajuste fino e integração de modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry

Este exemplo de ponta a ponta (E2E) é baseado no guia "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community. Ele apresenta os processos de ajuste fino, implantação e integração de modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry.  
Diferente do exemplo E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", que envolvia executar código localmente, este tutorial foca totalmente no ajuste fino e na integração do seu modelo dentro do Azure AI / ML Studio.

## Visão geral

Neste exemplo E2E, você aprenderá como ajustar fino o modelo Phi-3 e integrá-lo com Prompt flow no Azure AI Foundry. Aproveitando o Azure AI / ML Studio, você estabelecerá um fluxo de trabalho para implantar e utilizar modelos de IA personalizados. Este exemplo E2E está dividido em três cenários:

**Cenário 1: Configurar recursos do Azure e preparar para ajuste fino**

**Cenário 2: Ajustar fino o modelo Phi-3 e implantar no Azure Machine Learning Studio**

**Cenário 3: Integrar com Prompt flow e conversar com seu modelo personalizado no Azure AI Foundry**

Aqui está uma visão geral deste exemplo E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.pt.png)

### Sumário

1. **[Cenário 1: Configurar recursos do Azure e preparar para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Criar um Workspace do Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Solicitar cotas de GPU na assinatura do Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adicionar atribuição de função](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurar projeto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparar dataset para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 2: Ajustar fino o modelo Phi-3 e implantar no Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ajustar fino o modelo Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implantar o modelo Phi-3 ajustado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 3: Integrar com Prompt flow e conversar com seu modelo personalizado no Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrar o modelo Phi-3 personalizado com Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Conversar com seu modelo Phi-3 personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Cenário 1: Configurar recursos do Azure e preparar para ajuste fino

### Criar um Workspace do Azure Machine Learning

1. Digite *azure machine learning* na **barra de pesquisa** no topo da página do portal e selecione **Azure Machine Learning** nas opções que aparecerem.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.pt.png)

2. Selecione **+ Criar** no menu de navegação.

3. Selecione **Novo workspace** no menu de navegação.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.pt.png)

4. Realize as seguintes tarefas:

    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** que deseja usar (crie um novo se necessário).
    - Insira o **Nome do Workspace**. Deve ser um valor único.
    - Selecione a **Região** que deseja utilizar.
    - Selecione a **Conta de armazenamento** que deseja usar (crie uma nova se necessário).
    - Selecione o **Key vault** que deseja usar (crie um novo se necessário).
    - Selecione o **Application insights** que deseja usar (crie um novo se necessário).
    - Selecione o **Container registry** que deseja usar (crie um novo se necessário).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.pt.png)

5. Selecione **Revisar + criar**.

6. Selecione **Criar**.

### Solicitar cotas de GPU na assinatura do Azure

Neste tutorial, você aprenderá como ajustar fino e implantar um modelo Phi-3 usando GPUs. Para o ajuste fino, você usará a GPU *Standard_NC24ads_A100_v4*, que requer solicitação de cota. Para a implantação, usará a GPU *Standard_NC6s_v3*, que também requer solicitação de cota.

> [!NOTE]
>
> Apenas assinaturas Pay-As-You-Go (tipo padrão de assinatura) são elegíveis para alocação de GPU; assinaturas de benefício não são suportadas no momento.
>

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Realize as seguintes tarefas para solicitar a cota da família *Standard NCADSA100v4*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **família de máquinas virtuais** que deseja usar. Por exemplo, selecione **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC24ads_A100_v4*.
    - Selecione **Solicitar cota** no menu de navegação.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.pt.png)

    - Na página de solicitação de cota, insira o **Novo limite de núcleos** que deseja usar. Por exemplo, 24.
    - Na página de solicitação de cota, selecione **Enviar** para solicitar a cota da GPU.

1. Realize as seguintes tarefas para solicitar a cota da família *Standard NCSv3*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **família de máquinas virtuais** que deseja usar. Por exemplo, selecione **Standard NCSv3 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC6s_v3*.
    - Selecione **Solicitar cota** no menu de navegação.
    - Na página de solicitação de cota, insira o **Novo limite de núcleos** que deseja usar. Por exemplo, 24.
    - Na página de solicitação de cota, selecione **Enviar** para solicitar a cota da GPU.

### Adicionar atribuição de função

Para ajustar fino e implantar seus modelos, você deve primeiro criar uma Identidade Gerenciada Atribuída pelo Usuário (User Assigned Managed Identity - UAI) e atribuir as permissões apropriadas. Essa UAI será usada para autenticação durante a implantação.

#### Criar User Assigned Managed Identity (UAI)

1. Digite *managed identities* na **barra de pesquisa** no topo da página do portal e selecione **Managed Identities** nas opções que aparecerem.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.pt.png)

1. Selecione **+ Criar**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.pt.png)

1. Realize as seguintes tarefas:

    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** que deseja usar (crie um novo se necessário).
    - Selecione a **Região** que deseja utilizar.
    - Insira o **Nome**. Deve ser um valor único.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.pt.png)

1. Selecione **Revisar + criar**.

1. Selecione **+ Criar**.

#### Adicionar atribuição de função Contributor à Managed Identity

1. Navegue até o recurso Managed Identity que você criou.

1. Selecione **Azure role assignments** na aba lateral esquerda.

1. Selecione **+ Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, realize as seguintes tarefas:
    - Selecione o **Escopo** como **Grupo de recursos**.
    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** que deseja usar.
    - Selecione a **Função** como **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.pt.png)

2. Selecione **Salvar**.

#### Adicionar atribuição de função Storage Blob Data Reader à Managed Identity

1. Digite *storage accounts* na **barra de pesquisa** no topo da página do portal e selecione **Storage accounts** nas opções que aparecerem.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.pt.png)

1. Selecione a conta de armazenamento associada ao workspace Azure Machine Learning que você criou. Por exemplo, *finetunephistorage*.

1. Realize as seguintes tarefas para navegar até a página Adicionar atribuição de função:

    - Navegue até a conta de armazenamento do Azure que você criou.
    - Selecione **Controle de acesso (IAM)** na aba lateral esquerda.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.pt.png)

1. Na página Adicionar atribuição de função, realize as seguintes tarefas:

    - Na página Função, digite *Storage Blob Data Reader* na **barra de pesquisa** e selecione **Storage Blob Data Reader** nas opções que aparecerem.
    - Na página Função, selecione **Avançar**.
    - Na página Membros, selecione **Atribuir acesso a** **Managed identity**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar identidades gerenciadas, selecione sua **Assinatura** do Azure.
    - Na página Selecionar identidades gerenciadas, selecione a **Managed identity**.
    - Na página Selecionar identidades gerenciadas, selecione a Managed Identity que você criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar identidades gerenciadas, selecione **Selecionar**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.pt.png)

1. Selecione **Revisar + atribuir**.

#### Adicionar atribuição de função AcrPull à Managed Identity

1. Digite *container registries* na **barra de pesquisa** no topo da página do portal e selecione **Container registries** nas opções que aparecerem.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.pt.png)

1. Selecione o container registry associado ao workspace Azure Machine Learning. Por exemplo, *finetunephicontainerregistry*

1. Realize as seguintes tarefas para navegar até a página Adicionar atribuição de função:

    - Selecione **Controle de acesso (IAM)** na aba lateral esquerda.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, realize as seguintes tarefas:

    - Na página Função, digite *AcrPull* na **barra de pesquisa** e selecione **AcrPull** nas opções que aparecerem.
    - Na página Função, selecione **Avançar**.
    - Na página Membros, selecione **Atribuir acesso a** **Managed identity**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar identidades gerenciadas, selecione sua **Assinatura** do Azure.
    - Na página Selecionar identidades gerenciadas, selecione a **Managed identity**.
    - Na página Selecionar identidades gerenciadas, selecione a Managed Identity que você criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar identidades gerenciadas, selecione **Selecionar**.
    - Selecione **Revisar + atribuir**.

### Configurar projeto

Para baixar os datasets necessários para ajuste fino, você vai configurar um ambiente local.

Neste exercício, você irá:

- Criar uma pasta para trabalhar dentro dela.
- Criar um ambiente virtual.
- Instalar os pacotes necessários.
- Criar um arquivo *download_dataset.py* para baixar o dataset.

#### Criar uma pasta para trabalhar dentro dela

1. Abra uma janela do terminal e digite o seguinte comando para criar uma pasta chamada *finetune-phi* no caminho padrão.

    ```console
    mkdir finetune-phi
    ```

2. Digite o seguinte comando no terminal para navegar até a pasta *finetune-phi* que você criou.

    ```console
    cd finetune-phi
    ```

#### Criar um ambiente virtual

1. Digite o seguinte comando no terminal para criar um ambiente virtual chamado *.venv*.

    ```console
    python -m venv .venv
    ```

2. Digite o seguinte comando no terminal para ativar o ambiente virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Se funcionou, você deve ver *(.venv)* antes do prompt de comando.

#### Instalar os pacotes necessários

1. Digite os seguintes comandos no terminal para instalar os pacotes necessários.

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

1. Selecione **Arquivo** na barra de menu.

1. Selecione **Abrir Pasta**.

1. Selecione a pasta *finetune-phi* que você criou, localizada em *C:\Users\seuNomeDeUsuario\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.pt.png)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Arquivo** para criar um novo arquivo chamado *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.pt.png)

### Preparar dataset para ajuste fino

Neste exercício, você executará o arquivo *download_dataset.py* para baixar os datasets *ultrachat_200k* para seu ambiente local. Você usará esses datasets para ajustar fino o modelo Phi-3 no Azure Machine Learning.

Neste exercício, você irá:

- Adicionar código ao arquivo *download_dataset.py* para baixar os datasets.
- Executar o arquivo *download_dataset.py* para baixar os datasets para seu ambiente local.

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

1. Digite o seguinte comando no terminal para executar o script e baixar o dataset para seu ambiente local.

    ```console
    python download_dataset.py
    ```

1. Verifique se os datasets foram salvos com sucesso no diretório local *finetune-phi/data*.

> [!NOTE]
>
> #### Nota sobre o tamanho do dataset e o tempo de ajuste fino
>
> Neste tutorial, você usa apenas 1% do dataset (`split='train[:1%]'`). Isso reduz significativamente a quantidade de dados, acelerando tanto o upload quanto o processo de ajuste fino. Você pode ajustar a porcentagem para encontrar o equilíbrio certo entre o tempo de treinamento e o desempenho do modelo. Usar um subconjunto menor do dataset reduz o tempo necessário para o ajuste fino, tornando o processo mais gerenciável para um tutorial.

## Cenário 2: Ajustar fino o modelo Phi-3 e implantar no Azure Machine Learning Studio

### Ajustar fino o modelo Phi-3

Neste exercício, você vai ajustar fino o modelo Phi-3 no Azure Machine Learning Studio.

Neste exercício, você irá:

- Criar um cluster de computação para ajuste fino.
- Ajustar fino o modelo Phi-3 no Azure Machine Learning Studio.

#### Criar cluster de computação para ajuste fino
1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione **Compute** na aba do lado esquerdo.

1. Selecione **Compute clusters** no menu de navegação.

1. Clique em **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.pt.png)

1. Realize as seguintes tarefas:

    - Selecione a **Região** que deseja usar.
    - Defina o **Virtual machine tier** para **Dedicated**.
    - Defina o **Virtual machine type** para **GPU**.
    - No filtro de **Virtual machine size**, selecione **Select from all options**.
    - Escolha o **Virtual machine size** como **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.pt.png)

1. Clique em **Next**.

1. Realize as seguintes tarefas:

    - Insira o **Compute name**. Deve ser um valor único.
    - Defina o **Minimum number of nodes** para **0**.
    - Defina o **Maximum number of nodes** para **1**.
    - Defina o tempo de **Idle seconds before scale down** para **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.pt.png)

1. Clique em **Create**.

#### Ajuste fino do modelo Phi-3

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o workspace do Azure Machine Learning que você criou.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.pt.png)

1. Realize as seguintes tarefas:

    - Selecione **Model catalog** na aba do lado esquerdo.
    - Digite *phi-3-mini-4k* na **barra de busca** e selecione **Phi-3-mini-4k-instruct** entre as opções que aparecerem.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.pt.png)

1. Selecione **Fine-tune** no menu de navegação.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.pt.png)

1. Realize as seguintes tarefas:

    - Defina **Select task type** para **Chat completion**.
    - Clique em **+ Select data** para enviar os **Training data**.
    - Defina o tipo de upload dos dados de validação para **Provide different validation data**.
    - Clique em **+ Select data** para enviar os **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.pt.png)

    > [!TIP]
    >
    > Você pode selecionar **Advanced settings** para personalizar configurações como **learning_rate** e **lr_scheduler_type** para otimizar o processo de fine-tuning conforme suas necessidades específicas.

1. Clique em **Finish**.

1. Neste exercício, você ajustou com sucesso o modelo Phi-3 usando Azure Machine Learning. Note que o processo de fine-tuning pode levar um tempo considerável. Após iniciar o trabalho de fine-tuning, será necessário aguardar sua conclusão. Você pode monitorar o status do trabalho na aba Jobs, localizada no lado esquerdo do seu workspace Azure Machine Learning. Na próxima etapa, você fará o deploy do modelo ajustado e o integrará com o Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.pt.png)

### Faça o deploy do modelo Phi-3 ajustado

Para integrar o modelo Phi-3 ajustado com o Prompt flow, é necessário fazer o deploy do modelo para torná-lo acessível para inferência em tempo real. Esse processo envolve registrar o modelo, criar um endpoint online e fazer o deploy do modelo.

Neste exercício, você irá:

- Registrar o modelo ajustado no workspace Azure Machine Learning.
- Criar um endpoint online.
- Fazer o deploy do modelo Phi-3 ajustado registrado.

#### Registrar o modelo ajustado

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o workspace Azure Machine Learning que você criou.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.pt.png)

1. Selecione **Models** na aba do lado esquerdo.
1. Clique em **+ Register**.
1. Selecione **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.pt.png)

1. Selecione o job que você criou.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.pt.png)

1. Clique em **Next**.

1. Defina o **Model type** para **MLflow**.

1. Certifique-se que **Job output** está selecionado; isso deve acontecer automaticamente.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.pt.png)

2. Clique em **Next**.

3. Clique em **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.pt.png)

4. Você pode visualizar seu modelo registrado navegando até o menu **Models** na aba do lado esquerdo.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.pt.png)

#### Fazer o deploy do modelo ajustado

1. Acesse o workspace Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

1. Selecione **Real-time endpoints** no menu de navegação.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.pt.png)

1. Clique em **Create**.

1. Selecione o modelo registrado que você criou.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.pt.png)

1. Clique em **Select**.

1. Realize as seguintes tarefas:

    - Defina **Virtual machine** para *Standard_NC6s_v3*.
    - Escolha a **Instance count** que deseja usar. Por exemplo, *1*.
    - Defina o **Endpoint** como **New** para criar um novo endpoint.
    - Insira o **Endpoint name**. Deve ser um valor único.
    - Insira o **Deployment name**. Deve ser um valor único.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.pt.png)

1. Clique em **Deploy**.

> [!WARNING]
> Para evitar cobranças adicionais na sua conta, certifique-se de excluir o endpoint criado no workspace Azure Machine Learning.
>

#### Verificar status do deploy no Azure Machine Learning Workspace

1. Acesse o workspace Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

1. Selecione o endpoint que você criou.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.pt.png)

1. Nesta página, você pode gerenciar os endpoints durante o processo de deploy.

> [!NOTE]
> Assim que o deploy for concluído, verifique se o **Live traffic** está definido para **100%**. Se não estiver, selecione **Update traffic** para ajustar as configurações de tráfego. Note que você não poderá testar o modelo se o tráfego estiver definido como 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.pt.png)
>

## Cenário 3: Integrar com Prompt flow e conversar com seu modelo personalizado no Azure AI Foundry

### Integrar o modelo Phi-3 personalizado com Prompt flow

Após fazer o deploy do seu modelo ajustado com sucesso, agora você pode integrá-lo ao Prompt Flow para usar seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com seu modelo Phi-3 personalizado.

Neste exercício, você irá:

- Criar um Azure AI Foundry Hub.
- Criar um projeto Azure AI Foundry.
- Criar um Prompt flow.
- Adicionar uma conexão personalizada para o modelo Phi-3 ajustado.
- Configurar o Prompt flow para conversar com seu modelo Phi-3 personalizado.

> [!NOTE]
> Você também pode integrar com o Promptflow usando o Azure ML Studio. O mesmo processo de integração pode ser aplicado ao Azure ML Studio.

#### Criar Azure AI Foundry Hub

Você precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo organizar e gerenciar múltiplos Projetos dentro do Azure AI Foundry.

1. Acesse [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selecione **All hubs** na aba do lado esquerdo.

1. Clique em **+ New hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.pt.png)

1. Realize as seguintes tarefas:

    - Insira o **Hub name**. Deve ser um valor único.
    - Selecione sua **Subscription** do Azure.
    - Escolha o **Resource group** a ser usado (crie um novo, se necessário).
    - Selecione a **Location** que deseja usar.
    - Selecione **Connect Azure AI Services** para usar (crie um novo, se necessário).
    - Selecione **Connect Azure AI Search** como **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.pt.png)

1. Clique em **Next**.

#### Criar projeto Azure AI Foundry

1. No Hub que você criou, selecione **All projects** na aba do lado esquerdo.

1. Clique em **+ New project** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.pt.png)

1. Insira o **Project name**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.pt.png)

1. Clique em **Create a project**.

#### Adicionar uma conexão personalizada para o modelo Phi-3 ajustado

Para integrar seu modelo Phi-3 personalizado com o Prompt flow, você precisa salvar o endpoint e a chave do modelo em uma conexão personalizada. Essa configuração garante o acesso ao seu modelo Phi-3 personalizado no Prompt flow.

#### Definir a chave de API e o URI do endpoint do modelo Phi-3 ajustado

1. Acesse [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue até o workspace Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.pt.png)

1. Selecione o endpoint que você criou.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.pt.png)

1. Selecione **Consume** no menu de navegação.

1. Copie seu **REST endpoint** e a **Primary key**.
![Copie a chave da API e o URI do endpoint.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.pt.png)

#### Adicionar a Conexão Personalizada

1. Acesse o [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue até o projeto Azure AI Foundry que você criou.

1. No projeto que você criou, selecione **Configurações** na aba lateral esquerda.

1. Selecione **+ Nova conexão**.

    ![Selecione nova conexão.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.pt.png)

1. Selecione **Chaves personalizadas** no menu de navegação.

    ![Selecione chaves personalizadas.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.pt.png)

1. Realize as seguintes tarefas:

    - Selecione **+ Adicionar pares chave-valor**.
    - Para o nome da chave, digite **endpoint** e cole o endpoint que você copiou do Azure ML Studio no campo de valor.
    - Selecione **+ Adicionar pares chave-valor** novamente.
    - Para o nome da chave, digite **key** e cole a chave que você copiou do Azure ML Studio no campo de valor.
    - Após adicionar as chaves, selecione **é segredo** para evitar que a chave seja exposta.

    ![Adicionar conexão.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.pt.png)

1. Selecione **Adicionar conexão**.

#### Criar Prompt flow

Você adicionou uma conexão personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow seguindo os passos abaixo. Em seguida, você conectará esse Prompt flow à conexão personalizada para poder usar o modelo ajustado dentro do Prompt flow.

1. Navegue até o projeto Azure AI Foundry que você criou.

1. Selecione **Prompt flow** na aba lateral esquerda.

1. Selecione **+ Criar** no menu de navegação.

    ![Selecione Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.pt.png)

1. Selecione **Chat flow** no menu de navegação.

    ![Selecione chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.pt.png)

1. Digite o **Nome da pasta** a ser usado.

    ![Digite o nome.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.pt.png)

2. Selecione **Criar**.

#### Configurar Prompt flow para conversar com seu modelo Phi-3 personalizado

Você precisa integrar o modelo Phi-3 ajustado em um Prompt flow. Porém, o Prompt flow existente não foi projetado para esse propósito. Portanto, é necessário redesenhar o Prompt flow para permitir a integração do modelo personalizado.

1. No Prompt flow, execute as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Modo de arquivo bruto**.
    - Apague todo o código existente no arquivo *flow.dag.yml*.
    - Adicione o código abaixo no arquivo *flow.dag.yml*.

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

    - Selecione **Salvar**.

    ![Selecione modo de arquivo bruto.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.pt.png)

1. Adicione o código abaixo no arquivo *integrate_with_promptflow.py* para usar o modelo Phi-3 personalizado no Prompt flow.

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

    ![Cole o código do prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.pt.png)

> [!NOTE]
> Para informações mais detalhadas sobre o uso do Prompt flow no Azure AI Foundry, consulte [Prompt flow no Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Entrada de chat**, **Saída de chat** para habilitar a conversa com seu modelo.

    ![Entrada e saída.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.pt.png)

1. Agora você está pronto para conversar com seu modelo Phi-3 personalizado. No próximo exercício, você aprenderá como iniciar o Prompt flow e usá-lo para conversar com seu modelo Phi-3 ajustado.

> [!NOTE]
>
> O fluxo reconstruído deve ficar parecido com a imagem abaixo:
>
> ![Exemplo de fluxo.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.pt.png)
>

### Conversar com seu modelo Phi-3 personalizado

Agora que você ajustou e integrou seu modelo Phi-3 personalizado com o Prompt flow, está pronto para começar a interagir com ele. Este exercício vai guiá-lo pelo processo de configuração e início de uma conversa com seu modelo usando o Prompt flow. Seguindo esses passos, você poderá aproveitar ao máximo as capacidades do seu modelo Phi-3 ajustado para diversas tarefas e diálogos.

- Converse com seu modelo Phi-3 personalizado usando o Prompt flow.

#### Iniciar Prompt flow

1. Selecione **Iniciar sessões de computação** para iniciar o Prompt flow.

    ![Iniciar sessão de computação.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.pt.png)

1. Selecione **Validar e analisar entrada** para renovar os parâmetros.

    ![Validar entrada.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.pt.png)

1. Selecione o **Valor** da **conexão** para a conexão personalizada que você criou. Por exemplo, *connection*.

    ![Conexão.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.pt.png)

#### Conversar com seu modelo personalizado

1. Selecione **Chat**.

    ![Selecione chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.pt.png)

1. Aqui está um exemplo dos resultados: agora você pode conversar com seu modelo Phi-3 personalizado. Recomenda-se fazer perguntas baseadas nos dados usados para o ajuste fino.

    ![Converse com o prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.pt.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.