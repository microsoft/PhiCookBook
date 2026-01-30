<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0df910a227098303cc392b6ad204c271",
  "translation_date": "2026-01-06T04:32:01+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "pt"
}
-->
# Ajustar e Integrar modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry

Este exemplo de ponta a ponta (E2E) baseia-se no guia "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community. Introduz os processos de ajuste fino, implementação e integração de modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry.
Ao contrário do exemplo E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", que envolvia a execução local de código, este tutorial centra-se inteiramente no ajuste fino e na integração do seu modelo dentro do Azure AI / ML Studio.

## Visão geral

Neste exemplo E2E, aprenderá a ajustar o modelo Phi-3 e a integrá-lo com o Prompt flow no Azure AI Foundry. Aproveitando o Azure AI / ML Studio, estabelecerá um fluxo de trabalho para implementar e utilizar modelos de IA personalizados. Este exemplo E2E está dividido em três cenários:

**Cenário 1: Configurar recursos Azure e preparar para ajuste fino**

**Cenário 2: Ajustar o modelo Phi-3 e implementar no Azure Machine Learning Studio**

**Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado no Azure AI Foundry**

Aqui está uma visão geral deste exemplo E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/pt-PT/00-01-architecture.198ba0f1ae6d841a.webp)

### Índice

1. **[Cenário 1: Configurar recursos Azure e preparar para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Criar um Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Solicitar quotas de GPU na subscrição do Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adicionar atribuição de função](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurar projeto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparar conjunto de dados para ajuste fino](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 2: Ajustar modelo Phi-3 e implementar no Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ajustar o modelo Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementar o modelo Phi-3 ajustado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado no Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrar o modelo Phi-3 personalizado com o Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Conversar com o seu modelo Phi-3 personalizado](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Cenário 1: Configurar recursos Azure e preparar para ajuste fino

### Criar um Azure Machine Learning Workspace

1. Digite *azure machine learning* na **barra de pesquisa** no topo da página do portal e selecione **Azure Machine Learning** das opções que aparecem.

    ![Type azure machine learning.](../../../../../../translated_images/pt-PT/01-01-type-azml.acae6c5455e67b4b.webp)

2. Selecione **+ Criar** no menu de navegação.

3. Selecione **Novo workspace** no menu de navegação.

    ![Select new workspace.](../../../../../../translated_images/pt-PT/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Execute as seguintes tarefas:

    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo se necessário).
    - Insira o **Nome do workspace**. Deve ser um valor único.
    - Selecione a **Região** que deseja usar.
    - Selecione a **Conta de armazenamento** a usar (crie uma nova se necessário).
    - Selecione o **Key vault** a usar (crie um novo se necessário).
    - Selecione o **Application insights** a usar (crie um novo se necessário).
    - Selecione o **Registo de contentores** a usar (crie um novo se necessário).

    ![Fill azure machine learning.](../../../../../../translated_images/pt-PT/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Selecione **Analisar + Criar**.

6. Selecione **Criar**.

### Solicitar quotas de GPU na subscrição do Azure

Neste tutorial, aprenderá a ajustar e implementar um modelo Phi-3 usando GPUs. Para o ajuste fino, usará a GPU *Standard_NC24ads_A100_v4*, que requer um pedido de quota. Para a implementação, usará a GPU *Standard_NC6s_v3*, que também requer um pedido de quota.

> [!NOTE]
>
> Apenas subscrições Pay-As-You-Go (tipo de subscrição padrão) são elegíveis para alocação de GPU; subscrições de benefício não são atualmente suportadas.
>

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Execute as seguintes tarefas para solicitar a quota da *Standard NCADSA100v4 Family*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **Família de máquina virtual** a usar. Por exemplo, selecione **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC24ads_A100_v4*.
    - Selecione **Solicitar quota** no menu de navegação.

        ![Request quota.](../../../../../../translated_images/pt-PT/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na página de pedido de quota, insira o **Novo limite de núcleos** que pretende utilizar. Por exemplo, 24.
    - Na página de pedido de quota, selecione **Enviar** para solicitar a quota de GPU.

1. Execute as seguintes tarefas para solicitar a quota da *Standard NCSv3 Family*:

    - Selecione **Quota** na aba lateral esquerda.
    - Selecione a **Família de máquina virtual** a usar. Por exemplo, selecione **Standard NCSv3 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC6s_v3*.
    - Selecione **Solicitar quota** no menu de navegação.
    - Na página de pedido de quota, insira o **Novo limite de núcleos** que pretende utilizar. Por exemplo, 24.
    - Na página de pedido de quota, selecione **Enviar** para solicitar a quota de GPU.

### Adicionar atribuição de função

Para ajustar e implementar os seus modelos, deve primeiro criar uma Identidade Gerida Atribuída pelo Utilizador (User Assigned Managed Identity - UAI) e atribuir-lhe as permissões adequadas. Esta UAI será usada para autenticação durante a implementação.

#### Criar User Assigned Managed Identity(UAI)

1. Digite *managed identities* na **barra de pesquisa** no topo da página do portal e selecione **Managed Identities** das opções que aparecem.

    ![Type managed identities.](../../../../../../translated_images/pt-PT/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Selecione **+ Criar**.

    ![Select create.](../../../../../../translated_images/pt-PT/03-02-select-create.92bf8989a5cd98f2.webp)

1. Execute as seguintes tarefas:

    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo se necessário).
    - Selecione a **Região** que deseja usar.
    - Insira o **Nome**. Deve ser um valor único.

    ![Select create.](../../../../../../translated_images/pt-PT/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Selecione **Analisar + criar**.

1. Selecione **+ Criar**.

#### Adicionar atribuição de função de Contribuidor à Managed Identity

1. Navegue até ao recurso da Managed Identity que criou.

1. Selecione **Atribuições de função Azure** na aba lateral esquerda.

1. Selecione **+ Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, execute as seguintes tarefas:
    - Selecione o **Âmbito** para **Grupo de recursos**.
    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar.
    - Selecione a **Função** para **Contribuidor**.

    ![Fill contributor role.](../../../../../../translated_images/pt-PT/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Selecione **Guardar**.

#### Adicionar atribuição de função de Leitor de Dados de Blob de Armazenamento à Managed Identity

1. Digite *storage accounts* na **barra de pesquisa** no topo da página do portal e selecione **Storage accounts** das opções que aparecem.

    ![Type storage accounts.](../../../../../../translated_images/pt-PT/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Selecione a conta de armazenamento associada ao Azure Machine Learning workspace que criou. Por exemplo, *finetunephistorage*.

1. Execute as seguintes tarefas para navegar até à página Adicionar atribuição de função:

    - Navegue até à conta de armazenamento Azure que criou.
    - Selecione **Controlo de acesso (IAM)** na aba lateral esquerda.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

    ![Add role.](../../../../../../translated_images/pt-PT/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na página Adicionar atribuição de função, execute as seguintes tarefas:

    - Na página Função, escreva *Storage Blob Data Reader* na **barra de pesquisa** e selecione **Storage Blob Data Reader** das opções que aparecem.
    - Na página Função, selecione **Seguinte**.
    - Na página Membros, selecione **Atribuir acesso a** **Managed identity**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar managed identities, selecione a sua **Subscrição** Azure.
    - Na página Selecionar managed identities, selecione a **Managed identity** para **Managed Identity**.
    - Na página Selecionar managed identities, selecione a Managed Identity que criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar managed identities, selecione **Selecionar**.

    ![Select managed identity.](../../../../../../translated_images/pt-PT/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Selecione **Analisar + atribuir**.

#### Adicionar atribuição de função AcrPull à Managed Identity

1. Digite *container registries* na **barra de pesquisa** no topo da página do portal e selecione **Container registries** das opções que aparecem.

    ![Type container registries.](../../../../../../translated_images/pt-PT/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Selecione o registo de contentores associado ao Azure Machine Learning workspace. Por exemplo, *finetunephicontainerregistry*

1. Execute as seguintes tarefas para navegar até à página Adicionar atribuição de função:

    - Selecione **Controlo de acesso (IAM)** na aba lateral esquerda.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, execute as seguintes tarefas:

    - Na página Função, escreva *AcrPull* na **barra de pesquisa** e selecione **AcrPull** das opções que aparecem.
    - Na página Função, selecione **Seguinte**.
    - Na página Membros, selecione **Atribuir acesso a** **Managed identity**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar managed identities, selecione a sua **Subscrição** Azure.
    - Na página Selecionar managed identities, selecione a **Managed identity** para **Managed Identity**.
    - Na página Selecionar managed identities, selecione a Managed Identity que criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar managed identities, selecione **Selecionar**.
    - Selecione **Analisar + atribuir**.

### Configurar projeto

Para descarregar os conjuntos de dados necessários para o ajuste fino, irá configurar um ambiente local.

Neste exercício, irá

- Criar uma pasta para trabalhar dentro dela.
- Criar um ambiente virtual.
- Instalar os pacotes necessários.
- Criar um ficheiro *download_dataset.py* para descarregar o conjunto de dados.

#### Criar uma pasta para trabalhar dentro dela

1. Abra uma janela do terminal e escreva o seguinte comando para criar uma pasta chamada *finetune-phi* no caminho predefinido.

    ```console
    mkdir finetune-phi
    ```

2. Escreva o seguinte comando no seu terminal para navegar para a pasta *finetune-phi* que criou.

    ```console
    cd finetune-phi
    ```

#### Criar um ambiente virtual

1. Escreva o seguinte comando no seu terminal para criar um ambiente virtual chamado *.venv*.

    ```console
    python -m venv .venv
    ```

2. Escreva o seguinte comando no seu terminal para ativar o ambiente virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Se funcionar, deverá ver *(.venv)* antes do prompt do comando.

#### Instalar os pacotes necessários

1. Escreva os seguintes comandos no seu terminal para instalar os pacotes necessários.

    ```console
    pip install datasets==2.19.1
    ```

#### Criar `donload_dataset.py`

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

1. Selecione a pasta *finetune-phi* que criou, que está localizada em *C:\Users\yourUserName\finetune-phi*.

    ![Selecione a pasta que criou.](../../../../../../translated_images/pt-PT/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **New File** para criar um novo ficheiro chamado *download_dataset.py*.

    ![Criar um novo ficheiro.](../../../../../../translated_images/pt-PT/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Preparar o conjunto de dados para fine-tuning

Neste exercício, irá executar o ficheiro *download_dataset.py* para descarregar os conjuntos de dados *ultrachat_200k* para o seu ambiente local. Depois irá utilizar estes conjuntos de dados para afinar o modelo Phi-3 no Azure Machine Learning.

Neste exercício, irá:

- Adicionar código ao ficheiro *download_dataset.py* para descarregar os conjuntos de dados.
- Executar o ficheiro *download_dataset.py* para descarregar os conjuntos de dados para o seu ambiente local.

#### Descarregar o seu conjunto de dados usando *download_dataset.py*

1. Abra o ficheiro *download_dataset.py* no Visual Studio Code.

1. Adicione o seguinte código ao ficheiro *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

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
                # Escrever um caractere de nova linha para separar os registos
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Carregar e dividir o conjunto de dados ULTRACHAT_200k com uma configuração e proporção de divisão específicas
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrair os conjuntos de dados de treino e teste da divisão
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Guardar o conjunto de dados de treino num ficheiro JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Guardar o conjunto de dados de teste num ficheiro JSONL separado
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Escreva o seguinte comando no seu terminal para executar o script e descarregar o conjunto de dados para o seu ambiente local.

    ```console
    python download_dataset.py
    ```

1. Verifique que os conjuntos de dados foram guardados com sucesso no seu diretório local *finetune-phi/data*.

> [!NOTE]
>
> #### Nota sobre o tamanho do conjunto de dados e o tempo de fine-tuning
>
> Neste tutorial, utiliza apenas 1% do conjunto de dados (`split='train[:1%]'`). Isto reduz significativamente a quantidade de dados, acelerando tanto o processo de upload como o de fine-tuning. Pode ajustar a percentagem para encontrar o equilíbrio certo entre o tempo de treino e o desempenho do modelo. Usar um subconjunto menor do conjunto de dados reduz o tempo necessário para o fine-tuning, tornando o processo mais gerível para um tutorial.

## Cenário 2: Afinar o modelo Phi-3 e implementar no Azure Machine Learning Studio

### Afinar o modelo Phi-3

Neste exercício, irá afinar o modelo Phi-3 no Azure Machine Learning Studio.

Neste exercício, irá:

- Criar cluster de computação para fine-tuning.
- Afinar o modelo Phi-3 no Azure Machine Learning Studio.

#### Criar cluster de computação para fine-tuning

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione **Compute** no separador do lado esquerdo.

1. Selecione **Compute clusters** no menu de navegação.

1. Selecione **+ New**.

    ![Selecionar compute.](../../../../../../translated_images/pt-PT/06-01-select-compute.a29cff290b480252.webp)

1. Execute as seguintes tarefas:

    - Selecione a **Região** que pretende usar.
    - Selecione o **Nível da máquina virtual** para **Dedicated**.
    - Selecione o **Tipo da máquina virtual** para **GPU**.
    - Selecione o filtro **Tamanho da máquina virtual** para **Select from all options**.
    - Selecione o **Tamanho da máquina virtual** para **Standard_NC24ads_A100_v4**.

    ![Criar cluster.](../../../../../../translated_images/pt-PT/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Selecione **Next**.

1. Execute as seguintes tarefas:

    - Introduza o **Nome do cluster**. Deve ser um valor único.
    - Selecione o **Número mínimo de nós** para **0**.
    - Selecione o **Número máximo de nós** para **1**.
    - Selecione os **Segundos de inatividade antes de reduzir a escala** para **120**.

    ![Criar cluster.](../../../../../../translated_images/pt-PT/06-03-create-cluster.4a54ba20914f3662.webp)

1. Selecione **Create**.

#### Afinar o modelo Phi-3

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o workspace do Azure Machine Learning que criou.

    ![Selecionar workspace que criou.](../../../../../../translated_images/pt-PT/06-04-select-workspace.a92934ac04f4f181.webp)

1. Execute as seguintes tarefas:

    - Selecione **Model catalog** no separador do lado esquerdo.
    - Escreva *phi-3-mini-4k* na **barra de pesquisa** e selecione **Phi-3-mini-4k-instruct** nas opções que aparecem.

    ![Escreva phi-3-mini-4k.](../../../../../../translated_images/pt-PT/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Selecione **Fine-tune** no menu de navegação.

    ![Selecionar fine tune.](../../../../../../translated_images/pt-PT/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Execute as seguintes tarefas:

    - Selecione **Select task type** para **Chat completion**.
    - Selecione **+ Select data** para carregar os **Dados de treino**.
    - Selecione o tipo de upload dos dados de validação para **Provide different validation data**.
    - Selecione **+ Select data** para carregar os **Dados de validação**.

    ![Preencher a página do fine-tuning.](../../../../../../translated_images/pt-PT/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Pode selecionar **Advanced settings** para personalizar configurações como **learning_rate** e **lr_scheduler_type** para otimizar o processo de fine-tuning conforme as suas necessidades específicas.

1. Selecione **Finish**.

1. Neste exercício, afinou com sucesso o modelo Phi-3 usando o Azure Machine Learning. Note que o processo de fine-tuning pode levar um tempo considerável. Após iniciar o trabalho de fine-tuning, terá de aguardar que seja concluído. Pode monitorizar o estado do trabalho de fine-tuning navegando para o separador Jobs no lado esquerdo do seu Workspace do Azure Machine Learning. Na próxima série, irá implementar o modelo afinado e integrá-lo com o Prompt flow.

    ![Vejas o trabalho de fine-tuning.](../../../../../../translated_images/pt-PT/06-08-output.2bd32e59930672b1.webp)

### Implementar o modelo Phi-3 afinado

Para integrar o modelo Phi-3 afinado com o Prompt flow, necessita de implementar o modelo para que esteja acessível para inferência em tempo real. Este processo envolve registar o modelo, criar um endpoint online e implementar o modelo.

Neste exercício, irá:

- Registar o modelo afinado no workspace do Azure Machine Learning.
- Criar um endpoint online.
- Implementar o modelo Phi-3 afinado registado.

#### Registar o modelo afinado

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o workspace do Azure Machine Learning que criou.

    ![Selecionar workspace que criou.](../../../../../../translated_images/pt-PT/06-04-select-workspace.a92934ac04f4f181.webp)

1. Selecione **Models** no separador do lado esquerdo.
1. Selecione **+ Register**.
1. Selecione **From a job output**.

    ![Registar modelo.](../../../../../../translated_images/pt-PT/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Selecione o trabalho que criou.

    ![Selecionar trabalho.](../../../../../../translated_images/pt-PT/07-02-select-job.3e2e1144cd6cd093.webp)

1. Selecione **Next**.

1. Selecione **Model type** para **MLflow**.

1. Certifique-se de que **Job output** está selecionado; isto deve ser selecionado automaticamente.

    ![Selecionar output.](../../../../../../translated_images/pt-PT/07-03-select-output.4cf1a0e645baea1f.webp)

2. Selecione **Next**.

3. Selecione **Register**.

    ![Selecionar registar.](../../../../../../translated_images/pt-PT/07-04-register.fd82a3b293060bc7.webp)

4. Pode ver o seu modelo registado navegando para o menu **Models** no separador do lado esquerdo.

    ![Modelo registado.](../../../../../../translated_images/pt-PT/07-05-registered-model.7db9775f58dfd591.webp)

#### Implementar o modelo afinado

1. Navegue para o workspace do Azure Machine Learning que criou.

1. Selecione **Endpoints** no separador do lado esquerdo.

1. Selecione **Real-time endpoints** no menu de navegação.

    ![Criar endpoint.](../../../../../../translated_images/pt-PT/07-06-create-endpoint.1ba865c606551f09.webp)

1. Selecione **Create**.

1. selecione o modelo registado que criou.

    ![Selecionar modelo registado.](../../../../../../translated_images/pt-PT/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Selecione **Select**.

1. Execute as seguintes tarefas:

    - Selecione **Virtual machine** para *Standard_NC6s_v3*.
    - Selecione o **Número de instâncias** que deseja usar. Por exemplo, *1*.
    - Selecione o **Endpoint** para **New** para criar um endpoint.
    - Introduza o **Nome do endpoint**. Deve ser um valor único.
    - Introduza o **Nome da implementação**. Deve ser um valor único.

    ![Preencher as definições de implementação.](../../../../../../translated_images/pt-PT/07-08-deployment-setting.43ddc4209e673784.webp)

1. Selecione **Deploy**.

> [!WARNING]
> Para evitar cobranças adicionais na sua conta, certifique-se de eliminar o endpoint criado no workspace do Azure Machine Learning.
>

#### Verificar o estado da implementação no Azure Machine Learning Workspace

1. Navegue para o workspace do Azure Machine Learning que criou.

1. Selecione **Endpoints** no separador do lado esquerdo.

1. Selecione o endpoint que criou.

    ![Selecionar endpoints](../../../../../../translated_images/pt-PT/07-09-check-deployment.325d18cae8475ef4.webp)

1. Nesta página, pode gerir os endpoints durante o processo de implementação.

> [!NOTE]
> Após a conclusão da implementação, certifique-se de que o **Live traffic** está definido para **100%**. Se não estiver, selecione **Update traffic** para ajustar as definições de tráfego. Note que não pode testar o modelo se o tráfego estiver definido para 0%.
>
> ![Definir tráfego.](../../../../../../translated_images/pt-PT/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado no Azure AI Foundry

### Integrar o modelo Phi-3 personalizado com Prompt flow

Depois de implementar com sucesso o seu modelo afinado, agora pode integrá-lo com o Prompt Flow para usar o seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com o seu modelo Phi-3 personalizado.

Neste exercício, irá:

- Criar Azure AI Foundry Hub.
- Criar Projeto Azure AI Foundry.
- Criar Prompt flow.
- Adicionar uma ligação personalizada para o modelo Phi-3 afinado.
- Configurar o Prompt flow para conversar com o seu modelo Phi-3 personalizado.

> [!NOTE]
> Também pode integrar com Promptflow usando o Azure ML Studio. O mesmo processo de integração pode ser aplicado ao Azure ML Studio.

#### Criar Azure AI Foundry Hub

Precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo-lhe organizar e gerir múltiplos Projetos dentro do Azure AI Foundry.

1. Visite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selecione **All hubs** no separador do lado esquerdo.

1. Selecione **+ New hub** no menu de navegação.
    ![Criar hub.](../../../../../../translated_images/pt-PT/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Execute as seguintes tarefas:

    - Introduza **Nome do hub**. Deve ser um valor único.
    - Selecione a sua **Assinatura** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo se necessário).
    - Selecione a **Localização** que pretende utilizar.
    - Selecione **Ligar Serviços Azure AI** a utilizar (crie um novo se necessário).
    - Selecione **Ligar Azure AI Search** para **Ignorar ligar**.

    ![Preencher hub.](../../../../../../translated_images/pt-PT/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Selecione **Seguinte**.

#### Criar Projeto Azure AI Foundry

1. No Hub que criou, selecione **Todos os projetos** no separador do lado esquerdo.

1. Selecione **+ Novo projeto** no menu de navegação.

    ![Selecionar novo projeto.](../../../../../../translated_images/pt-PT/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Introduza **Nome do projeto**. Deve ser um valor único.

    ![Criar projeto.](../../../../../../translated_images/pt-PT/08-05-create-project.4d97f0372f03375a.webp)

1. Selecione **Criar um projeto**.

#### Adicionar uma ligação personalizada para o modelo Phi-3 ajustado

Para integrar o seu modelo Phi-3 personalizado com o Prompt flow, precisa de guardar o endpoint e a chave do modelo numa ligação personalizada. Esta configuração assegura o acesso ao seu modelo Phi-3 personalizado no Prompt flow.

#### Definir chave api e URI do endpoint do modelo Phi-3 ajustado

1. Visite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue até ao espaço de trabalho Azure Machine learning que criou.

1. Selecione **Endpoints** no separador do lado esquerdo.

    ![Selecionar endpoints.](../../../../../../translated_images/pt-PT/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Selecione o endpoint que criou.

    ![Selecionar endpoints.](../../../../../../translated_images/pt-PT/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Selecione **Consumir** no menu de navegação.

1. Copie o seu **endpoint REST** e a **Chave primária**.

    ![Copiar chave api e URI do endpoint.](../../../../../../translated_images/pt-PT/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Adicionar a Ligação Personalizada

1. Visite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue até ao projeto Azure AI Foundry que criou.

1. No projeto que criou, selecione **Definições** no separador do lado esquerdo.

1. Selecione **+ Nova ligação**.

    ![Selecionar nova ligação.](../../../../../../translated_images/pt-PT/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Selecione **Chaves personalizadas** no menu de navegação.

    ![Selecionar chaves personalizadas.](../../../../../../translated_images/pt-PT/08-10-select-custom-keys.856f6b2966460551.webp)

1. Execute as seguintes tarefas:

    - Selecione **+ Adicionar pares de chave e valor**.
    - Para o nome da chave, introduza **endpoint** e cole o endpoint que copiou do Azure ML Studio no campo valor.
    - Selecione **+ Adicionar pares de chave e valor** novamente.
    - Para o nome da chave, introduza **key** e cole a chave que copiou do Azure ML Studio no campo valor.
    - Depois de adicionar as chaves, selecione **é segredo** para evitar que a chave seja exposta.

    ![Adicionar ligação.](../../../../../../translated_images/pt-PT/08-11-add-connection.785486badb4d2d26.webp)

1. Selecione **Adicionar ligação**.

#### Criar Prompt flow

Adicionou uma ligação personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow usando os seguintes passos. Depois, irá ligar este Prompt flow à ligação personalizada para que possa usar o modelo ajustado dentro do Prompt flow.

1. Navegue até ao projeto Azure AI Foundry que criou.

1. Selecione **Prompt flow** no separador do lado esquerdo.

1. Selecione **+ Criar** no menu de navegação.

    ![Selecionar Promptflow.](../../../../../../translated_images/pt-PT/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Selecione **Chat flow** no menu de navegação.

    ![Selecionar chat flow.](../../../../../../translated_images/pt-PT/08-13-select-flow-type.2ec689b22da32591.webp)

1. Introduza **Nome da pasta** a utilizar.

    ![Introduzir nome.](../../../../../../translated_images/pt-PT/08-14-enter-name.ff9520fefd89f40d.webp)

2. Selecione **Criar**.

#### Configurar Prompt flow para conversar com o seu modelo Phi-3 personalizado

Precisa de integrar o modelo Phi-3 afinado num Prompt flow. No entanto, o Prompt flow existente fornecido não está desenhado para este propósito. Portanto, deve redesenhar o Prompt flow para permitir a integração do modelo personalizado.

1. No Prompt flow, execute as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Modo ficheiro bruto**.
    - Elimine todo o código existente no ficheiro *flow.dag.yml*.
    - Adicione o seguinte código ao ficheiro *flow.dag.yml*.

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

    - Selecione **Guardar**.

    ![Selecionar modo ficheiro bruto.](../../../../../../translated_images/pt-PT/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Adicione o seguinte código ao ficheiro *integrate_with_promptflow.py* para usar o modelo Phi-3 personalizado no Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configuração de registo
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

        # "connection" é o nome da Conexão Personalizada, "endpoint", "key" são as chaves na Conexão Personalizada
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
            
            # Regista a resposta JSON completa
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

    ![Colar código do prompt flow.](../../../../../../translated_images/pt-PT/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Para mais informações detalhadas sobre o uso do Prompt flow no Azure AI Foundry, pode consultar [Prompt flow no Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Entrada de chat**, **Saída de chat** para ativar a conversa com o seu modelo.

    ![Entrada Saída.](../../../../../../translated_images/pt-PT/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Agora está pronto para conversar com o seu modelo Phi-3 personalizado. No exercício seguinte, aprenderá como iniciar o Prompt flow e usá-lo para conversar com o seu modelo Phi-3 afinado.

> [!NOTE]
>
> O fluxo reconstruído deve parecer com a imagem abaixo:
>
> ![Exemplo de fluxo.](../../../../../../translated_images/pt-PT/08-18-graph-example.d6457533952e690c.webp)
>

### Conversar com o seu modelo Phi-3 personalizado

Agora que afinou e integrou o seu modelo Phi-3 personalizado com o Prompt flow, está pronto para começar a interagir com ele. Este exercício irá guiá-lo pelo processo de configurar e iniciar uma conversa com o seu modelo usando o Prompt flow. Seguindo estes passos, será capaz de utilizar plenamente as capacidades do seu modelo Phi-3 afinado para várias tarefas e conversas.

- Converse com o seu modelo Phi-3 personalizado usando o Prompt flow.

#### Iniciar Prompt flow

1. Selecione **Iniciar sessões de computação** para iniciar o Prompt flow.

    ![Iniciar sessão de computação.](../../../../../../translated_images/pt-PT/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Selecione **Validar e analisar entrada** para renovar os parâmetros.

    ![Validar entrada.](../../../../../../translated_images/pt-PT/09-02-validate-input.317c76ef766361e9.webp)

1. Selecione o **Valor** da **ligação** para a ligação personalizada que criou. Por exemplo, *ligação*.

    ![Ligação.](../../../../../../translated_images/pt-PT/09-03-select-connection.99bdddb4b1844023.webp)

#### Conversar com o seu modelo personalizado

1. Selecione **Conversar**.

    ![Selecionar conversar.](../../../../../../translated_images/pt-PT/09-04-select-chat.61936dce6612a1e6.webp)

1. Aqui está um exemplo dos resultados: Agora pode conversar com o seu modelo Phi-3 personalizado. Recomenda-se fazer perguntas baseadas nos dados usados para o ajuste fino.

    ![Conversar com prompt flow.](../../../../../../translated_images/pt-PT/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->