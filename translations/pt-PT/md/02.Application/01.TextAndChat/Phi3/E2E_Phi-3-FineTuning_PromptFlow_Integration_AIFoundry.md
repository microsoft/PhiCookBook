# Ajustar e Integrar modelos Phi-3 personalizados com Prompt flow no Microsoft Foundry

Este exemplo de ponta a ponta (E2E) baseia-se no guia "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community. Introduz os processos de ajuste fino, implementação e integração de modelos Phi-3 personalizados com Prompt flow no Microsoft Foundry.
Ao contrário do exemplo E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", que envolvia executar código localmente, este tutorial foca-se inteiramente no ajuste fino e integração do seu modelo dentro do Azure AI / ML Studio.

## Visão geral

Neste exemplo E2E, vai aprender a ajustar o modelo Phi-3 e integrá-lo com Prompt flow no Microsoft Foundry. Aproveitando o Azure AI / ML Studio, irá estabelecer um fluxo de trabalho para implementar e utilizar modelos de IA personalizados. Este exemplo E2E está dividido em três cenários:

**Cenário 1: Configurar recursos Azure e preparar para ajuste fino**

**Cenário 2: Ajustar o modelo Phi-3 e implementar no Azure Machine Learning Studio**

**Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado no Microsoft Foundry**

Aqui está uma visão geral deste exemplo E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/pt-PT/00-01-architecture.198ba0f1ae6d841a.webp)

### Índice

1. **[Cenário 1: Configurar recursos Azure e preparar para ajuste fino](#cenário-1-configurar-recursos-azure-e-preparar-para-ajuste-fino)**
    - [Criar um Workspace Azure Machine Learning](#criar-um-workspace-azure-machine-learning)
    - [Solicitar quotas de GPU na Subscrição Azure](#solicitar-quotas-de-gpu-na-subscrição-azure)
    - [Adicionar atribuição de função](#adicionar-atribuição-de-função)
    - [Configurar projeto](#configurar-projeto)
    - [Preparar conjunto de dados para ajuste fino](#preparar-o-dataset-para-fine-tuning)

1. **[Cenário 2: Ajustar o modelo Phi-3 e implementar no Azure Machine Learning Studio](#cenário-2-afinar-o-modelo-phi-3-e-desplegar-no-azure-machine-learning-studio)**
    - [Ajustar o modelo Phi-3](#afinar-o-modelo-phi-3)
    - [Implementar o modelo Phi-3 ajustado](#desplegar-o-modelo-phi-3-afinado)

1. **[Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado no Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrar o modelo Phi-3 personalizado com Prompt flow](#integrar-o-modelo-customizado-phi-3-com-prompt-flow)
    - [Conversar com o seu modelo Phi-3 personalizado](#conversar-com-o-seu-modelo-phi-3-personalizado)

## Cenário 1: Configurar recursos Azure e preparar para ajuste fino

### Criar um Workspace Azure Machine Learning

1. Digite *azure machine learning* na **barra de pesquisa** no topo da página do portal e selecione **Azure Machine Learning** das opções que aparecem.

    ![Type azure machine learning.](../../../../../../translated_images/pt-PT/01-01-type-azml.acae6c5455e67b4b.webp)

2. Selecione **+ Criar** no menu de navegação.

3. Selecione **Novo workspace** no menu de navegação.

    ![Select new workspace.](../../../../../../translated_images/pt-PT/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Execute as seguintes tarefas:

    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo, se necessário).
    - Introduza o **Nome do Workspace**. Deve ser um valor único.
    - Selecione a **Região** que deseja utilizar.
    - Selecione a **Conta de armazenamento** a utilizar (crie uma nova, se necessário).
    - Selecione o **Key vault** a utilizar (crie um novo, se necessário).
    - Selecione o **Application insights** a utilizar (crie um novo, se necessário).
    - Selecione o **Registo de contentores** a utilizar (crie um novo, se necessário).

    ![Fill azure machine learning.](../../../../../../translated_images/pt-PT/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Selecione **Rever + criar**.

6. Selecione **Criar**.

### Solicitar quotas de GPU na Subscrição Azure

Neste tutorial, irá aprender a ajustar e implementar um modelo Phi-3, utilizando GPUs. Para ajuste fino, vai utilizar a GPU *Standard_NC24ads_A100_v4*, que requer um pedido de quota. Para implementação, vai utilizar a GPU *Standard_NC6s_v3*, que também requer um pedido de quota.

> [!NOTE]
>
> Apenas subscrições Pay-As-You-Go (o tipo padrão de subscrição) são elegíveis para alocação de GPU; subscrições de benefício não são atualmente suportadas.
>

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Execute as seguintes tarefas para solicitar a quota *Standard NCADSA100v4 Family*:

    - Selecione **Quota** na aba do lado esquerdo.
    - Selecione a **Família de máquinas virtuais** a utilizar. Por exemplo, selecione **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC24ads_A100_v4*.
    - Selecione a **Solicitar quota** no menu de navegação.

        ![Request quota.](../../../../../../translated_images/pt-PT/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na página Solicitar quota, introduza o **Novo limite de núcleos** que deseja utilizar. Por exemplo, 24.
    - Na página Solicitar quota, selecione **Enviar** para solicitar a quota de GPU.

1. Execute as seguintes tarefas para solicitar a quota *Standard NCSv3 Family*:

    - Selecione **Quota** na aba do lado esquerdo.
    - Selecione a **Família de máquinas virtuais** a utilizar. Por exemplo, selecione **Standard NCSv3 Family Cluster Dedicated vCPUs**, que inclui a GPU *Standard_NC6s_v3*.
    - Selecione a **Solicitar quota** no menu de navegação.
    - Na página Solicitar quota, introduza o **Novo limite de núcleos** que deseja utilizar. Por exemplo, 24.
    - Na página Solicitar quota, selecione **Enviar** para solicitar a quota de GPU.

### Adicionar atribuição de função

Para ajustar e implementar os seus modelos, deve primeiro criar uma Identidade Gerida Atribuída pelo Utilizador (UAI) e atribuir-lhe as permissões apropriadas. Esta UAI será usada para autenticação durante a implementação.

#### Criar Identidade Gerida Atribuída pelo Utilizador (UAI)

1. Digite *managed identities* na **barra de pesquisa** no topo da página do portal e selecione **Managed Identities** das opções que aparecem.

    ![Type managed identities.](../../../../../../translated_images/pt-PT/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Selecione **+ Criar**.

    ![Select create.](../../../../../../translated_images/pt-PT/03-02-select-create.92bf8989a5cd98f2.webp)

1. Execute as seguintes tarefas:

    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo, se necessário).
    - Selecione a **Região** que deseja utilizar.
    - Introduza o **Nome**. Deve ser um valor único.

    ![Select create.](../../../../../../translated_images/pt-PT/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Selecione **Rever + criar**.

1. Selecione **+ Criar**.

#### Adicionar atribuição de função Contributor à Identidade Gerida

1. Navegue para o recurso da Identidade Gerida que criou.

1. Selecione **Atribuições de função Azure** na aba do lado esquerdo.

1. Selecione **+ Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, execute as seguintes tarefas:
    - Selecione o **Âmbito** para **Grupo de recursos**.
    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar.
    - Selecione a **Função** para **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/pt-PT/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Selecione **Guardar**.

#### Adicionar atribuição de função Storage Blob Data Reader à Identidade Gerida

1. Digite *storage accounts* na **barra de pesquisa** no topo da página do portal e selecione **Storage accounts** das opções que aparecem.

    ![Type storage accounts.](../../../../../../translated_images/pt-PT/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Selecione a conta de armazenamento associada ao workspace Azure Machine Learning que criou. Por exemplo, *finetunephistorage*.

1. Execute as seguintes tarefas para navegar até à página Adicionar atribuição de função:

    - Navegue para a conta Azure Storage que criou.
    - Selecione **Controlos de acesso (IAM)** na aba do lado esquerdo.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

    ![Add role.](../../../../../../translated_images/pt-PT/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na página Adicionar atribuição de função, execute as seguintes tarefas:

    - Na página Função, escreva *Storage Blob Data Reader* na **barra de pesquisa** e selecione **Storage Blob Data Reader** das opções que aparecem.
    - Na página Função, selecione **Seguinte**.
    - Na página Membros, selecione **Atribuir acesso a** **Identidade Gerida**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar identidades geridas, selecione a sua **Subscrição** Azure.
    - Na página Selecionar identidades geridas, selecione a **Identidade Gerida** para **Manage Identity**.
    - Na página Selecionar identidades geridas, selecione a Identidade Gerida que criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar identidades geridas, selecione **Selecionar**.

    ![Select managed identity.](../../../../../../translated_images/pt-PT/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Selecione **Rever + atribuir**.

#### Adicionar atribuição de função AcrPull à Identidade Gerida

1. Digite *container registries* na **barra de pesquisa** no topo da página do portal e selecione **Container registries** das opções que aparecem.

    ![Type container registries.](../../../../../../translated_images/pt-PT/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Selecione o registo de contentores associado ao workspace Azure Machine Learning. Por exemplo, *finetunephicontainerregistry*

1. Execute as seguintes tarefas para navegar até à página Adicionar atribuição de função:

    - Selecione **Controlos de acesso (IAM)** na aba do lado esquerdo.
    - Selecione **+ Adicionar** no menu de navegação.
    - Selecione **Adicionar atribuição de função** no menu de navegação.

1. Na página Adicionar atribuição de função, execute as seguintes tarefas:

    - Na página Função, escreva *AcrPull* na **barra de pesquisa** e selecione **AcrPull** das opções que aparecem.
    - Na página Função, selecione **Seguinte**.
    - Na página Membros, selecione **Atribuir acesso a** **Identidade Gerida**.
    - Na página Membros, selecione **+ Selecionar membros**.
    - Na página Selecionar identidades geridas, selecione a sua **Subscrição** Azure.
    - Na página Selecionar identidades geridas, selecione a **Identidade Gerida** para **Manage Identity**.
    - Na página Selecionar identidades geridas, selecione a Identidade Gerida que criou. Por exemplo, *finetunephi-managedidentity*.
    - Na página Selecionar identidades geridas, selecione **Selecionar**.
    - Selecione **Rever + atribuir**.

### Configurar projeto

Para descarregar os conjuntos de dados necessários para ajuste fino, vai configurar um ambiente local.

Neste exercício, irá

- Criar uma pasta para trabalhar dentro dela.
- Criar um ambiente virtual.
- Instalar os pacotes necessários.
- Criar um ficheiro *download_dataset.py* para descarregar o conjunto de dados.

#### Criar uma pasta para trabalhar dentro dela

1. Abra uma janela de terminal e digite o seguinte comando para criar uma pasta chamada *finetune-phi* no caminho padrão.

    ```console
    mkdir finetune-phi
    ```

2. Digite o seguinte comando dentro do seu terminal para navegar até à pasta *finetune-phi* que criou.

    ```console
    cd finetune-phi
    ```

#### Criar um ambiente virtual

1. Digite o seguinte comando dentro do seu terminal para criar um ambiente virtual chamado *.venv*.
    ```console
    python -m venv .venv
    ```

2. Escreva o seguinte comando no seu terminal para ativar o ambiente virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Se funcionar, deverá ver *(.venv)* antes do prompt de comando.

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

1. Selecione **Ficheiro** na barra de menus.

1. Selecione **Abrir Pasta**.

1. Selecione a pasta *finetune-phi* que criou, localizada em *C:\Users\yourUserName\finetune-phi*.

    ![Selecione a pasta que criou.](../../../../../../translated_images/pt-PT/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. No painel esquerdo do Visual Studio Code, clique com o botão direito e selecione **Novo Ficheiro** para criar um novo ficheiro chamado *download_dataset.py*.

    ![Crie um novo ficheiro.](../../../../../../translated_images/pt-PT/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Preparar o dataset para fine-tuning

Neste exercício, irá executar o ficheiro *download_dataset.py* para descarregar os datasets *ultrachat_200k* para o seu ambiente local. Depois, vai usar esses datasets para afinar o modelo Phi-3 no Azure Machine Learning.

Neste exercício, irá:

- Adicionar código ao ficheiro *download_dataset.py* para descarregar os datasets.
- Executar o ficheiro *download_dataset.py* para descarregar os datasets para o seu ambiente local.

#### Descarregar o seu dataset usando *download_dataset.py*

1. Abra o ficheiro *download_dataset.py* no Visual Studio Code.

1. Adicione o seguinte código no ficheiro *download_dataset.py*.

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
                # Despejar o registo como um objeto JSON e escrevê-lo no ficheiro
                json.dump(record, f)
                # Escrever um carácter de nova linha para separar os registos
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

1. Escreva o seguinte comando no seu terminal para executar o script e descarregar o dataset para o seu ambiente local.

    ```console
    python download_dataset.py
    ```

1. Verifique se os datasets foram guardados com sucesso no seu diretório local *finetune-phi/data*.

> [!NOTE]
>
> #### Nota sobre o tamanho do dataset e o tempo de fine-tuning
>
> Neste tutorial, usa apenas 1% do dataset (`split='train[:1%]'`). Isto reduz significativamente a quantidade de dados, acelerando tanto o upload como o processo de fine-tuning. Pode ajustar a percentagem para encontrar o equilíbrio correto entre o tempo de treino e o desempenho do modelo. Usar um subconjunto menor do dataset reduz o tempo necessário para o fine-tuning, tornando o processo mais manejável para um tutorial.

## Cenário 2: Afinar o modelo Phi-3 e Desplegar no Azure Machine Learning Studio

### Afinar o modelo Phi-3

Neste exercício, irá afinar o modelo Phi-3 no Azure Machine Learning Studio.

Neste exercício, irá:

- Criar um cluster de computação para o fine-tuning.
- Afinar o modelo Phi-3 no Azure Machine Learning Studio.

#### Criar cluster de computação para o fine-tuning

1. Aceda a [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione **Computação** no separador do lado esquerdo.

1. Selecione **Clusters de computação** no menu de navegação.

1. Selecione **+ Novo**.

    ![Selecione computação.](../../../../../../translated_images/pt-PT/06-01-select-compute.a29cff290b480252.webp)

1. Execute as seguintes tarefas:

    - Selecione a **Região** que deseja usar.
    - Selecione o **Tier da máquina virtual** para **Dedicado**.
    - Selecione o **Tipo de máquina virtual** para **GPU**.
    - Selecione o filtro **Tamanho da máquina virtual** para **Selecionar entre todas as opções**.
    - Selecione o **Tamanho da máquina virtual** para **Standard_NC24ads_A100_v4**.

    ![Criar cluster.](../../../../../../translated_images/pt-PT/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Selecione **Seguinte**.

1. Execute as seguintes tarefas:

    - Insira o **Nome do cluster**. Deve ser um valor único.
    - Selecione o **Número mínimo de nós** para **0**.
    - Selecione o **Número máximo de nós** para **1**.
    - Selecione o **Segundo de ociosidade antes de reduzir a escala** para **120**.

    ![Criar cluster.](../../../../../../translated_images/pt-PT/06-03-create-cluster.4a54ba20914f3662.webp)

1. Selecione **Criar**.

#### Afinar o modelo Phi-3

1. Aceda a [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o espaço de trabalho Azure Machine Learning que criou.

    ![Selecione o espaço de trabalho que criou.](../../../../../../translated_images/pt-PT/06-04-select-workspace.a92934ac04f4f181.webp)

1. Execute as seguintes tarefas:

    - Selecione **Catálogo de modelos** no separador do lado esquerdo.
    - Escreva *phi-3-mini-4k* na **barra de pesquisa** e selecione **Phi-3-mini-4k-instruct** entre as opções que aparecem.

    ![Escreva phi-3-mini-4k.](../../../../../../translated_images/pt-PT/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Selecione **Afinar** no menu de navegação.

    ![Selecione afinar.](../../../../../../translated_images/pt-PT/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Execute as seguintes tarefas:

    - Selecione **Selecionar tipo de tarefa** para **Conclusão de chat**.
    - Selecione **+ Selecionar dados** para carregar **Dados de treino**.
    - Selecione o tipo de carregamento dos dados de validação para **Fornecer dados de validação diferentes**.
    - Selecione **+ Selecionar dados** para carregar **Dados de validação**.

    ![Preencha a página de fine-tuning.](../../../../../../translated_images/pt-PT/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Pode selecionar **Definições avançadas** para personalizar configurações como **learning_rate** e **lr_scheduler_type** para otimizar o processo de fine-tuning conforme as suas necessidades específicas.

1. Selecione **Concluir**.

1. Neste exercício, afinou com sucesso o modelo Phi-3 usando Azure Machine Learning. Note que o processo de fine-tuning pode demorar bastante tempo. Depois de iniciar o trabalho de fine-tuning, precisa de aguardar a sua conclusão. Pode monitorizar o estado do trabalho de fine-tuning navegando para o separador Jobs no lado esquerdo do seu Espaço de Trabalho Azure Machine Learning. Na série seguinte, irá desplegar o modelo afinado e integrá-lo com o Prompt flow.

    ![Ver trabalho de fine-tuning.](../../../../../../translated_images/pt-PT/06-08-output.2bd32e59930672b1.webp)

### Desplegar o modelo Phi-3 afinado

Para integrar o modelo Phi-3 afinado com Prompt flow, precisa de desplegar o modelo para o tornar acessível para inferência em tempo real. Este processo envolve registar o modelo, criar um endpoint online e desplegar o modelo.

Neste exercício, irá:

- Registrar o modelo afinado no espaço de trabalho do Azure Machine Learning.
- Criar um endpoint online.
- Desplegar o modelo Phi-3 afinado registado.

#### Registar o modelo afinado

1. Aceda a [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecione o espaço de trabalho Azure Machine Learning que criou.

    ![Selecione o espaço de trabalho que criou.](../../../../../../translated_images/pt-PT/06-04-select-workspace.a92934ac04f4f181.webp)

1. Selecione **Modelos** no separador do lado esquerdo.
1. Selecione **+ Registar**.
1. Selecione **A partir da saída de um trabalho**.

    ![Registar modelo.](../../../../../../translated_images/pt-PT/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Selecione o trabalho que criou.

    ![Selecionar trabalho.](../../../../../../translated_images/pt-PT/07-02-select-job.3e2e1144cd6cd093.webp)

1. Selecione **Seguinte**.

1. Selecione **Tipo de modelo** para **MLflow**.

1. Certifique-se que **Saída do trabalho** está selecionada; deve estar selecionada automaticamente.

    ![Selecionar saída.](../../../../../../translated_images/pt-PT/07-03-select-output.4cf1a0e645baea1f.webp)

2. Selecione **Seguinte**.

3. Selecione **Registar**.

    ![Selecionar registar.](../../../../../../translated_images/pt-PT/07-04-register.fd82a3b293060bc7.webp)

4. Pode visualizar o seu modelo registado navegando para o menu **Modelos** no separador do lado esquerdo.

    ![Modelo registado.](../../../../../../translated_images/pt-PT/07-05-registered-model.7db9775f58dfd591.webp)

#### Desplegar o modelo afinado

1. Navegue para o espaço de trabalho Azure Machine Learning que criou.

1. Selecione **Endpoints** no separador do lado esquerdo.

1. Selecione **Endpoints em tempo real** no menu de navegação.

    ![Criar endpoint.](../../../../../../translated_images/pt-PT/07-06-create-endpoint.1ba865c606551f09.webp)

1. Selecione **Criar**.

1. Seleccione o modelo registado que criou.

    ![Selecionar modelo registado.](../../../../../../translated_images/pt-PT/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Selecione **Selecionar**.

1. Execute as seguintes tarefas:

    - Selecione **Máquina virtual** para *Standard_NC6s_v3*.
    - Selecione a **Contagem de instâncias** que deseja usar. Por exemplo, *1*.
    - Selecione o **Endpoint** para **Novo** para criar um endpoint.
    - Insira o **Nome do endpoint**. Deve ser um valor único.
    - Insira o **Nome da implantação**. Deve ser um valor único.

    ![Preencher definições da implantação.](../../../../../../translated_images/pt-PT/07-08-deployment-setting.43ddc4209e673784.webp)

1. Selecione **Desplegar**.

> [!WARNING]
> Para evitar custos adicionais na sua conta, assegure-se de eliminar o endpoint criado no espaço de trabalho Azure Machine Learning.
>

#### Verificar o estado da implantação no Azure Machine Learning Workspace

1. Navegue para o espaço de trabalho Azure Machine Learning que criou.

1. Selecione **Endpoints** no separador do lado esquerdo.

1. Selecione o endpoint que criou.

    ![Selecionar endpoints](../../../../../../translated_images/pt-PT/07-09-check-deployment.325d18cae8475ef4.webp)

1. Nesta página, pode gerir os endpoints durante o processo de implantação.

> [!NOTE]
> Após a conclusão da implantação, assegure-se que o **Tráfego em direto** está definido para **100%**. Se não estiver, selecione **Atualizar tráfego** para ajustar as definições do tráfego. Note que não pode testar o modelo se o tráfego estiver definido para 0%.
>
> ![Definir tráfego.](../../../../../../translated_images/pt-PT/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Cenário 3: Integrar com Prompt flow e conversar com o seu modelo personalizado no Microsoft Foundry

### Integrar o modelo customizado Phi-3 com Prompt flow

Após ter desplegado com sucesso o seu modelo afinado, agora pode integrá-lo com o Prompt Flow para usar o seu modelo em aplicações em tempo real, permitindo uma variedade de tarefas interativas com o seu modelo Phi-3 customizado.

Neste exercício, irá:

- Criar Microsoft Foundry Hub.
- Criar Microsoft Foundry Project.
- Criar Prompt flow.
- Adicionar uma conexão customizada para o modelo Phi-3 afinado.
- Configurar o Prompt flow para conversar com o seu modelo Phi-3 customizado

> [!NOTE]
> Também pode integrar com Promptflow usando Azure ML Studio. O mesmo processo de integração pode ser aplicado ao Azure ML Studio.

#### Criar Microsoft Foundry Hub

Precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo-lhe organizar e gerir múltiplos Projetos dentro do Microsoft Foundry.
1. Visite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selecione **All hubs** na aba do lado esquerdo.

1. Selecione **+ New hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/pt-PT/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Execute as seguintes tarefas:

    - Introduza **Hub name**. Deve ser um valor único.
    - Selecione a sua **Subscription** do Azure.
    - Selecione o **Resource group** a utilizar (crie um novo, se necessário).
    - Selecione a **Location** que pretende usar.
    - Selecione **Connect Azure AI Services** a utilizar (crie um novo, se necessário).
    - Selecione **Connect Azure AI Search** para **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/pt-PT/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Selecione **Next**.

#### Criar projeto no Microsoft Foundry

1. No Hub que criou, selecione **All projects** na aba do lado esquerdo.

1. Selecione **+ New project** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/pt-PT/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Introduza **Project name**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/pt-PT/08-05-create-project.4d97f0372f03375a.webp)

1. Selecione **Create a project**.

#### Adicionar uma ligação personalizada para o modelo Phi-3 ajustado

Para integrar o seu modelo Phi-3 personalizado com o Prompt flow, precisa de guardar o endpoint e a chave do modelo numa ligação personalizada. Esta configuração garante o acesso ao seu modelo Phi-3 personalizado no Prompt flow.

#### Definir a chave api e o endpoint do modelo Phi-3 afinado

1. Visite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue para o workspace Azure Machine learning que criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/pt-PT/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Selecione o endpoint que criou.

    ![Select endpoints.](../../../../../../translated_images/pt-PT/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Selecione **Consume** no menu de navegação.

1. Copie o seu **REST endpoint** e **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pt-PT/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Adicionar a Ligação Personalizada

1. Visite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navegue para o projeto Microsoft Foundry que criou.

1. No Projeto que criou, selecione **Settings** na aba do lado esquerdo.

1. Selecione **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/pt-PT/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Selecione **Custom keys** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/pt-PT/08-10-select-custom-keys.856f6b2966460551.webp)

1. Execute as seguintes tarefas:

    - Selecione **+ Add key value pairs**.
    - Para o nome da chave, insira **endpoint** e cole o endpoint que copiou do Azure ML Studio no campo de valor.
    - Selecione novamente **+ Add key value pairs**.
    - Para o nome da chave, insira **key** e cole a chave que copiou do Azure ML Studio no campo de valor.
    - Depois de adicionar as chaves, selecione **is secret** para impedir que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/pt-PT/08-11-add-connection.785486badb4d2d26.webp)

1. Selecione **Add connection**.

#### Criar Prompt flow

Adicionou uma ligação personalizada no Microsoft Foundry. Agora, vamos criar um Prompt flow usando os seguintes passos. Depois, irá ligar este Prompt flow à ligação personalizada para que possa usar o modelo afinado dentro do Prompt flow.

1. Navegue para o projeto Microsoft Foundry que criou.

1. Selecione **Prompt flow** na aba do lado esquerdo.

1. Selecione **+ Create** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/pt-PT/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Selecione **Chat flow** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/pt-PT/08-13-select-flow-type.2ec689b22da32591.webp)

1. Introduza **Folder name** a usar.

    ![Enter name.](../../../../../../translated_images/pt-PT/08-14-enter-name.ff9520fefd89f40d.webp)

2. Selecione **Create**.

#### Configurar Prompt flow para conversar com o seu modelo Phi-3 personalizado

Precisa de integrar o modelo Phi-3 afinado num Prompt flow. Contudo, o Prompt flow existente fornecido não está concebido para este propósito. Portanto, deve redesenhar o Prompt flow para permitir a integração do modelo personalizado.

1. No Prompt flow, realize as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Raw file mode**.
    - Apague todo o código existente no ficheiro *flow.dag.yml*.
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

    - Selecione **Save**.

    ![Select raw file mode.](../../../../../../translated_images/pt-PT/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Adicione o seguinte código ao ficheiro *integrate_with_promptflow.py* para usar o modelo Phi-3 personalizado no Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configuração do registo
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
            
            # Registar a resposta JSON completa
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

    ![Paste prompt flow code.](../../../../../../translated_images/pt-PT/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Para informações mais detalhadas sobre o uso do Prompt flow no Microsoft Foundry, pode consultar [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Chat input**, **Chat output** para ativar a conversa com o seu modelo.

    ![Input Output.](../../../../../../translated_images/pt-PT/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Agora está pronto para conversar com o seu modelo Phi-3 personalizado. No próximo exercício, vai aprender como iniciar o Prompt flow e usá-lo para conversar com o seu modelo Phi-3 afinado.

> [!NOTE]
>
> O fluxo reconstruído deve parecer com a imagem abaixo:
>
> ![Flow example.](../../../../../../translated_images/pt-PT/08-18-graph-example.d6457533952e690c.webp)
>

### Conversar com o seu modelo Phi-3 personalizado

Agora que afinou e integrou o seu modelo Phi-3 personalizado com o Prompt flow, está pronto para começar a interagir com ele. Este exercício irá guiá-lo pelo processo de configuração e início de uma conversa com o seu modelo usando o Prompt flow. Ao seguir estes passos, poderá utilizar plenamente as capacidades do seu modelo Phi-3 afinado para várias tarefas e conversas.

- Converse com o seu modelo Phi-3 personalizado usando Prompt flow.

#### Iniciar Prompt flow

1. Selecione **Start compute sessions** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pt-PT/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Selecione **Validate and parse input** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/pt-PT/09-02-validate-input.317c76ef766361e9.webp)

1. Selecione o **Value** da **connection** para a ligação personalizada que criou. Por exemplo, *connection*.

    ![Connection.](../../../../../../translated_images/pt-PT/09-03-select-connection.99bdddb4b1844023.webp)

#### Conversar com o seu modelo personalizado

1. Selecione **Chat**.

    ![Select chat.](../../../../../../translated_images/pt-PT/09-04-select-chat.61936dce6612a1e6.webp)

1. Eis um exemplo dos resultados: Agora pode conversar com o seu modelo Phi-3 personalizado. Recomenda-se fazer perguntas baseadas nos dados usados para o fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/pt-PT/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->