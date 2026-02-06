## Como usar componentes de chat-completion do registro do sistema Azure ML para ajuste fino de um modelo

Neste exemplo, realizaremos o ajuste fino do modelo Phi-3-mini-4k-instruct para completar uma conversa entre 2 pessoas usando o conjunto de dados ultrachat_200k.

![MLFineTune](../../../../translated_images/pt-BR/MLFineTune.928d4c6b3767dd35.webp)

O exemplo mostrará como realizar o ajuste fino usando o Azure ML SDK e Python e, em seguida, implantar o modelo ajustado em um endpoint online para inferência em tempo real.

### Dados de treinamento

Usaremos o conjunto de dados ultrachat_200k. Esta é uma versão fortemente filtrada do conjunto UltraChat e foi usada para treinar o Zephyr-7B-β, um modelo state of the art de chat 7b.

### Modelo

Usaremos o modelo Phi-3-mini-4k-instruct para mostrar como o usuário pode ajustar finamente um modelo para a tarefa de chat-completion. Se você abriu este notebook a partir de uma ficha específica de modelo, lembre-se de substituir o nome do modelo específico.

### Tarefas

- Escolher um modelo para ajustar finamente.
- Escolher e explorar os dados de treinamento.
- Configurar o trabalho de ajuste fino.
- Executar o trabalho de ajuste fino.
- Revisar métricas de treinamento e avaliação.
- Registrar o modelo ajustado.
- Implantar o modelo ajustado para inferência em tempo real.
- Limpar os recursos.

## 1. Configurar pré-requisitos

- Instale as dependências
- Conecte-se ao Workspace do AzureML. Saiba mais em configurar autenticação do SDK. Substitua <WORKSPACE_NAME>, <RESOURCE_GROUP> e <SUBSCRIPTION_ID> abaixo.
- Conecte-se ao registro do sistema azureml
- Defina um nome opcional para o experimento
- Verifique ou crie o compute.

> [!NOTE]
> Requisitos: um único nó de GPU pode ter múltiplas placas GPU. Por exemplo, em um nó do Standard_NC24rs_v3 há 4 GPUs NVIDIA V100, enquanto no Standard_NC12s_v3, há 2 GPUs NVIDIA V100. Consulte a documentação para essa informação. O número de placas GPU por nó é definido no parâmetro gpus_per_node abaixo. Configurar esse valor corretamente garantirá a utilização de todas as GPUs no nó. Os SKUs de computação GPU recomendados podem ser encontrados aqui e aqui.

### Bibliotecas Python

Instale as dependências executando a célula abaixo. Esta não é uma etapa opcional se estiver rodando em um ambiente novo.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interagindo com Azure ML

1. Este script Python é usado para interagir com o serviço Azure Machine Learning (Azure ML). Aqui está um resumo do que ele faz:

    - Importa módulos necessários dos pacotes azure.ai.ml, azure.identity e azure.ai.ml.entities. Também importa o módulo time.

    - Tenta autenticar usando DefaultAzureCredential(), que oferece uma experiência simplificada de autenticação para iniciar rapidamente o desenvolvimento de aplicações rodando na nuvem Azure. Se isso falhar, usa InteractiveBrowserCredential(), que fornece um prompt de login interativo.

    - Em seguida, tenta criar uma instância MLClient usando o método from_config, que lê a configuração do arquivo padrão config.json. Se isso falhar, cria uma instância MLClient fornecendo manualmente subscription_id, resource_group_name e workspace_name.

    - Cria outra instância MLClient, dessa vez para o registro Azure ML chamado "azureml". Esse registro é onde modelos, pipelines de fine-tuning e ambientes são armazenados.

    - Define o nome do experimento como "chat_completion_Phi-3-mini-4k-instruct".

    - Gera um timestamp único convertendo o tempo atual (em segundos desde a época, como número de ponto flutuante) para um inteiro e depois para string. Esse timestamp pode ser usado para criar nomes e versões únicos.

    ```python
    # Importe os módulos necessários do Azure ML e do Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Importe o módulo time
    
    # Tente autenticar usando DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Se DefaultAzureCredential falhar, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Tente criar uma instância de MLClient usando o arquivo de configuração padrão
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Se isso falhar, crie uma instância de MLClient fornecendo os detalhes manualmente
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Crie outra instância de MLClient para o registro Azure ML chamado "azureml"
    # Este registro é onde os modelos, pipelines de fine-tuning e ambientes são armazenados
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Defina o nome do experimento
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Gere um timestamp único que pode ser usado para nomes e versões que precisam ser únicos
    timestamp = str(int(time.time()))
    ```

## 2. Escolha um modelo base para ajuste fino

1. Phi-3-mini-4k-instruct é um modelo leve, state-of-the-art, com 3,8 bilhões de parâmetros, construído com base nos conjuntos utilizados para Phi-2. O modelo pertence à família Phi-3, e a versão Mini vem em dois variantes: 4K e 128K, que correspondem ao tamanho do contexto (em tokens) que o modelo suporta; precisamos ajustar o modelo para nosso propósito específico para poder usá-lo. Você pode navegar nestes modelos no Catálogo de Modelos do AzureML Studio, filtrando pela tarefa de chat-completion. Neste exemplo, usamos o modelo Phi-3-mini-4k-instruct. Se você abriu este notebook para um modelo diferente, substitua o nome e a versão do modelo conforme necessário.

> [!NOTE]
> a propriedade id do modelo. Ela será passada como input para o trabalho de ajuste fino. Também está disponível no campo Asset ID na página de detalhes do modelo no Catálogo de Modelos do AzureML Studio.

2. Este script Python interage com o serviço Azure Machine Learning (Azure ML). Aqui está um resumo do que ele faz:

    - Define o model_name como "Phi-3-mini-4k-instruct".

    - Usa o método get da propriedade models do objeto registry_ml_client para recuperar a versão mais recente do modelo com o nome especificado a partir do registro Azure ML. O método get é chamado com dois argumentos: o nome do modelo e um rótulo especificando que a versão mais recente deve ser recuperada.

    - Imprime uma mensagem no console indicando o nome, versão e id do modelo que será usado para o ajuste fino. O método format da string é usado para inserir o nome, versão e id do modelo na mensagem. O nome, versão e id do modelo são acessados como propriedades do objeto foundation_model.

    ```python
    # Defina o nome do modelo
    model_name = "Phi-3-mini-4k-instruct"
    
    # Obtenha a versão mais recente do modelo do registro Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Imprima o nome do modelo, a versão e o id
    # Esta informação é útil para rastreamento e depuração
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Crie um compute para ser usado no trabalho

O trabalho de ajuste fino funciona SOMENTE com computação GPU. O tamanho do compute depende de quão grande é o modelo e, na maioria dos casos, é difícil identificar o compute certo para o trabalho. Nesta célula, guiamos o usuário para selecionar o compute correto para o trabalho.

> [!NOTE]
> Os computes listados abaixo funcionam com a configuração mais otimizada. Qualquer alteração na configuração pode levar a erro Cuda Out Of Memory. Nestes casos, tente fazer upgrade do compute para um tamanho maior.

> [!NOTE]
> Ao selecionar o compute_cluster_size abaixo, certifique-se que o compute está disponível no seu grupo de recursos. Se um compute específico não estiver disponível, você pode solicitar acesso aos recursos de compute.

### Verificando suporte do modelo para ajuste fino

1. Este script Python interage com um modelo Azure Machine Learning (Azure ML). Aqui está um resumo do que ele faz:

    - Importa o módulo ast, que fornece funções para processar árvores da sintaxe abstrata do Python.

    - Verifica se o objeto foundation_model (que representa um modelo no Azure ML) tem uma tag chamada finetune_compute_allow_list. Tags no Azure ML são pares chave-valor que você pode criar e usar para filtrar e ordenar modelos.

    - Se a tag finetune_compute_allow_list estiver presente, usa a função ast.literal_eval para analisar de forma segura o valor da tag (uma string) em uma lista Python. Essa lista é então atribuída à variável computes_allow_list. Em seguida, imprime uma mensagem indicando que um compute deve ser criado a partir desta lista.

    - Se a tag não estiver presente, define computes_allow_list como None e imprime uma mensagem indicando que a tag finetune_compute_allow_list não faz parte das tags do modelo.

    - Em resumo, este script verifica uma tag específica nos metadados do modelo, converte o valor da tag para uma lista se existir, e fornece feedback ao usuário.

    ```python
    # Importe o módulo ast, que fornece funções para processar árvores da gramática abstrata de sintaxe do Python
    import ast
    
    # Verifique se a tag 'finetune_compute_allow_list' está presente nas tags do modelo
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Se a tag estiver presente, use ast.literal_eval para analisar com segurança o valor da tag (uma string) em uma lista Python
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # converter string para lista python
        # Imprima uma mensagem indicando que um compute deve ser criado a partir da lista
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Se a tag não estiver presente, defina computes_allow_list como None
        computes_allow_list = None
        # Imprima uma mensagem indicando que a tag 'finetune_compute_allow_list' não faz parte das tags do modelo
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Verificando Compute Instance

1. Este script Python interage com o serviço Azure Machine Learning (Azure ML) e realiza várias verificações em uma instância de compute. Aqui está um resumo do que ele faz:

    - Tenta recuperar a instância de compute com o nome armazenado em compute_cluster do workspace Azure ML. Se o estado de provisionamento da instância for "failed", ele lança um ValueError.

    - Verifica se computes_allow_list não é None. Se não for, converte todos os tamanhos de compute na lista para minúsculas e verifica se o tamanho da instância compute atual está na lista. Se não estiver, lança um ValueError.

    - Se computes_allow_list for None, verifica se o tamanho da instância compute está em uma lista de tamanhos de VM GPU não suportados. Se estiver, lança um ValueError.

    - Recupera uma lista de todos os tamanhos de compute disponíveis no workspace. Em seguida, itera esta lista, e para cada tamanho de compute, verifica se seu nome corresponde ao tamanho da instância compute atual. Se sim, recupera o número de GPUs para esse tamanho e define gpu_count_found como True.

    - Se gpu_count_found for True, imprime o número de GPUs na instância compute. Se for False, lança um ValueError.

    - Em resumo, este script realiza várias verificações em uma instância de compute no workspace Azure ML, incluindo seu estado de provisionamento, seu tamanho em relação a uma lista permitida ou negada, e o número de GPUs que ela possui.
    
    ```python
    # Imprima a mensagem de exceção
    print(e)
    # Levante um ValueError se o tamanho do compute não estiver disponível no workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Recupere a instância de computação do workspace Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Verifique se o estado de provisionamento da instância de computação é "failed"
    if compute.provisioning_state.lower() == "failed":
        # Levante um ValueError se o estado de provisionamento for "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Verifique se computes_allow_list não é None
    if computes_allow_list is not None:
        # Converta todos os tamanhos de compute em computes_allow_list para letras minúsculas
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Verifique se o tamanho da instância de computação está em computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Levante um ValueError se o tamanho da instância de computação não estiver em computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Defina uma lista de tamanhos de VM GPU não suportados
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Verifique se o tamanho da instância de computação está em unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Levante um ValueError se o tamanho da instância de computação estiver em unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Inicialize uma flag para verificar se o número de GPUs na instância de computação foi encontrado
    gpu_count_found = False
    # Recupere uma lista de todos os tamanhos de compute disponíveis no workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Itere sobre a lista de tamanhos de compute disponíveis
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Verifique se o nome do tamanho de compute corresponde ao tamanho da instância de computação
        if compute_sku.name.lower() == compute.size.lower():
            # Se corresponder, recupere o número de GPUs para esse tamanho de compute e defina gpu_count_found como True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Se gpu_count_found for True, imprima o número de GPUs na instância de computação
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Se gpu_count_found for False, levante um ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Escolher o conjunto de dados para ajuste fino do modelo

1. Usamos o conjunto de dados ultrachat_200k. O conjunto tem quatro divisões, adequadas para fine-tuning supervisionado (sft).
Rankeamento de geração (gen). O número de exemplos por divisão é mostrado a seguir:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. As próximas células mostram preparação básica dos dados para o ajuste fino:

### Visualizar algumas linhas dos dados

Queremos que esta amostra rode rapidamente, então salve os arquivos train_sft, test_sft contendo 5% das linhas já filtradas. Isso significa que o modelo ajustado terá precisão menor, portanto não deve ser usado em aplicações reais.
O script download-dataset.py é usado para baixar o conjunto ultrachat_200k e transformar os dados em um formato consumível pelo pipeline de fine-tuning. Também, como o conjunto é grande, aqui temos apenas parte dele.

1. Executar o script abaixo baixa apenas 5% dos dados. Isso pode ser aumentado alterando o parâmetro dataset_split_pc para o percentual desejado.

> [!NOTE]
> Alguns modelos de linguagem têm códigos de idioma diferentes e, portanto, os nomes das colunas no conjunto de dados devem refletir isso.

1. Aqui está um exemplo de como os dados devem parecer:
O conjunto de dados chat-completion é armazenado no formato parquet, com cada entrada usando o seguinte esquema:

    - Este é um documento JSON (JavaScript Object Notation), que é um formato popular para intercâmbio de dados. Não é código executável, mas uma forma de armazenar e transportar dados. Aqui está a estrutura:

    - "prompt": esta chave contém um valor string que representa uma tarefa ou pergunta feita a um assistente de IA.

    - "messages": esta chave contém um array de objetos. Cada objeto representa uma mensagem em uma conversa entre um usuário e um assistente de IA. Cada objeto de mensagem tem duas chaves:

    - "content": esta chave contém o conteúdo da mensagem como string.
    - "role": esta chave contém o papel da entidade que enviou a mensagem, como string. Pode ser "user" ou "assistant".
    - "prompt_id": esta chave contém um identificador único para o prompt.

1. Neste documento JSON específico, uma conversa é representada onde um usuário pede a um assistente de IA para criar um protagonista para uma história distópica. O assistente responde, e o usuário pede mais detalhes. O assistente concorda em fornecer mais detalhes. Toda a conversa está associada a um prompt_id específico.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Baixar Dados

1. Este script Python é usado para baixar um conjunto de dados usando um script auxiliar chamado download-dataset.py. Aqui está um resumo do que ele faz:

    - Importa o módulo os, que fornece uma forma portátil de usar funcionalidades dependentes do sistema operacional.

    - Usa a função os.system para rodar o script download-dataset.py no shell com argumentos específicos de linha de comando. Os argumentos especificam o conjunto a baixar (HuggingFaceH4/ultrachat_200k), o diretório para onde será baixado (ultrachat_200k_dataset), e a porcentagem do conjunto para dividir (5). A função os.system retorna o status de saída do comando executado; esse status é armazenado na variável exit_status.

    - Verifica se exit_status não é 0. Em sistemas tipo Unix, status 0 indica sucesso, qualquer outro indica erro. Se não for 0, levanta uma Exception com uma mensagem indicando que houve um erro ao baixar o conjunto de dados.

    - Em resumo, este script executa um comando para baixar um conjunto usando um script auxiliar, levantando exceção se o comando falhar.
    
    ```python
    # Importe o módulo os, que fornece uma maneira de usar funcionalidades dependentes do sistema operacional
    import os
    
    # Use a função os.system para executar o script download-dataset.py no shell com argumentos específicos de linha de comando
    # Os argumentos especificam o conjunto de dados para baixar (HuggingFaceH4/ultrachat_200k), o diretório para baixá-lo (ultrachat_200k_dataset) e a porcentagem do conjunto de dados para dividir (5)
    # A função os.system retorna o status de saída do comando executado; esse status é armazenado na variável exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Verifique se exit_status não é 0
    # Em sistemas operacionais tipo Unix, um status de saída 0 geralmente indica que um comando foi bem-sucedido, enquanto qualquer outro número indica um erro
    # Se exit_status não for 0, levante uma Exceção com uma mensagem indicando que houve um erro ao baixar o conjunto de dados
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Carregando dados em um DataFrame

1. Este script Python carrega um arquivo JSON Lines em um DataFrame pandas e exibe as primeiras 5 linhas. Aqui está um resumo do que ele faz:

    - Importa a biblioteca pandas, que é uma poderosa biblioteca para manipulação e análise de dados.

    - Define a largura máxima da coluna para as opções de exibição do pandas como 0. Isso significa que o texto completo de cada coluna será exibido sem truncamento quando o DataFrame for impresso.
    - Ele usa a função pd.read_json para carregar o arquivo train_sft.jsonl do diretório ultrachat_200k_dataset em um DataFrame. O argumento lines=True indica que o arquivo está no formato JSON Lines, onde cada linha é um objeto JSON separado.

    - Ele usa o método head para exibir as primeiras 5 linhas do DataFrame. Se o DataFrame tiver menos de 5 linhas, ele exibirá todas.

    - Em resumo, este script está carregando um arquivo JSON Lines em um DataFrame e exibindo as primeiras 5 linhas com o texto completo das colunas.
    
    ```python
    # Importe a biblioteca pandas, que é uma poderosa biblioteca de manipulação e análise de dados
    import pandas as pd
    
    # Defina a largura máxima da coluna nas opções de exibição do pandas para 0
    # Isso significa que o texto completo de cada coluna será exibido sem truncamento quando o DataFrame for impresso
    pd.set_option("display.max_colwidth", 0)
    
    # Use a função pd.read_json para carregar o arquivo train_sft.jsonl do diretório ultrachat_200k_dataset em um DataFrame
    # O argumento lines=True indica que o arquivo está no formato JSON Lines, onde cada linha é um objeto JSON separado
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use o método head para exibir as primeiras 5 linhas do DataFrame
    # Se o DataFrame tiver menos de 5 linhas, ele exibirá todas elas
    df.head()
    ```

## 5. Enviar o trabalho de fine tuning usando o modelo e dados como entradas

Crie o trabalho que usa o componente pipeline de chat-completion. Saiba mais sobre todos os parâmetros suportados para fine tuning.

### Definir parâmetros de fine tuning

1. Os parâmetros de fine tuning podem ser agrupados em 2 categorias - parâmetros de treinamento, parâmetros de otimização

1. Os parâmetros de treinamento definem os aspectos do treinamento como -

    - O otimizador, scheduler a ser usado
    - A métrica para otimizar o fine tuning
    - Número de passos de treinamento e o tamanho do lote, entre outros
    - Parâmetros de otimização ajudam a otimizar a memória da GPU e usar os recursos computacionais de forma eficiente.

1. Abaixo estão alguns dos parâmetros que pertencem a essa categoria. Os parâmetros de otimização diferem para cada modelo e são empacotados com o modelo para lidar com essas variações.

    - Habilitar o deepspeed e LoRA
    - Habilitar treinamento de precisão mista
    - Habilitar treinamento multi-nó

> [!NOTE]
> O fine tuning supervisionado pode resultar em perda de alinhamento ou esquecimento catastrófico. Recomendamos verificar essa questão e executar uma etapa de alinhamento após o fine tuning.

### Parâmetros de Fine Tuning

1. Este script Python está configurando parâmetros para o fine tuning de um modelo de aprendizado de máquina. Aqui está uma descrição do que ele faz:

    - Configura parâmetros padrão de treinamento como número de épocas, tamanhos de lote para treinamento e avaliação, taxa de aprendizado e tipo do scheduler de taxa de aprendizado.

    - Configura parâmetros padrão de otimização, como se o Layer-wise Relevance Propagation (LoRa) e DeepSpeed serão aplicados, e o estágio do DeepSpeed.

    - Combina os parâmetros de treinamento e otimização em um único dicionário chamado finetune_parameters.

    - Verifica se o foundation_model possui parâmetros padrão específicos do modelo. Se possuir, imprime uma mensagem de aviso e atualiza o dicionário finetune_parameters com esses padrões específicos do modelo. A função ast.literal_eval é usada para converter esses parâmetros específicos de string para um dicionário Python.

    - Imprime o conjunto final de parâmetros de fine tuning que serão usados na execução.

    - Em resumo, este script está configurando e exibindo os parâmetros para fine tuning de um modelo de aprendizado de máquina, com a capacidade de sobrescrever os parâmetros padrão com os específicos do modelo.

    ```python
    # Configurar parâmetros padrão de treinamento, como o número de épocas de treinamento, tamanhos de lote para treinamento e avaliação, taxa de aprendizagem e tipo de agendador de taxa de aprendizagem
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Configurar parâmetros padrão de otimização, como se deve aplicar Layer-wise Relevance Propagation (LoRa) e DeepSpeed, e o estágio do DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combinar os parâmetros de treinamento e otimização em um único dicionário chamado finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Verificar se o foundation_model possui parâmetros padrão específicos do modelo
    # Se possuir, imprimir uma mensagem de aviso e atualizar o dicionário finetune_parameters com esses padrões específicos do modelo
    # A função ast.literal_eval é usada para converter os padrões específicos do modelo de uma string para um dicionário Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # converter string para dicionário Python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Imprimir o conjunto final de parâmetros de fine-tuning que serão usados para a execução
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline de Treinamento

1. Este script Python está definindo uma função para gerar um nome de exibição para um pipeline de treinamento de aprendizado de máquina e, em seguida, chamando essa função para gerar e imprimir o nome de exibição. Aqui está uma descrição do que ele faz:

1. A função get_pipeline_display_name é definida. Essa função gera um nome de exibição baseado em vários parâmetros relacionados ao pipeline de treinamento.

1. Dentro da função, calcula o tamanho total do lote multiplicando o tamanho do lote por dispositivo, o número de passos de acumulação de gradiente, o número de GPUs por nó e o número de nós usados para o fine tuning.

1. Recupera vários outros parâmetros como o tipo de scheduler de taxa de aprendizado, se o DeepSpeed é aplicado, o estágio do DeepSpeed, se o Layer-wise Relevance Propagation (LoRa) é aplicado, o limite no número de checkpoints do modelo para manter e o comprimento máximo da sequência.

1. Constrói uma string que inclui todos esses parâmetros, separados por hífens. Se DeepSpeed ou LoRa forem aplicados, a string inclui "ds" seguido do estágio do DeepSpeed ou "lora", respectivamente. Caso contrário, inclui "nods" ou "nolora", respectivamente.

1. A função retorna essa string, que serve como o nome de exibição para o pipeline de treinamento.

1. Após a definição da função, ela é chamada para gerar o nome de exibição, que é então impresso.

1. Em resumo, este script está gerando um nome de exibição para um pipeline de treinamento de aprendizado de máquina baseado em vários parâmetros, e então imprimindo esse nome.

    ```python
    # Defina uma função para gerar um nome de exibição para o pipeline de treinamento
    def get_pipeline_display_name():
        # Calcule o tamanho total do lote multiplicando o tamanho do lote por dispositivo, o número de etapas de acumulação de gradiente, o número de GPUs por nó e o número de nós usados para o fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Recupere o tipo de agendador de taxa de aprendizado
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Recupere se o DeepSpeed está aplicado
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Recupere o estágio do DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Se o DeepSpeed estiver aplicado, inclua "ds" seguido do estágio do DeepSpeed no nome de exibição; caso contrário, inclua "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Recupere se a Propagação de Relevância em Camadas (LoRa) está aplicada
        lora = finetune_parameters.get("apply_lora", "false")
        # Se o LoRa estiver aplicado, inclua "lora" no nome de exibição; caso contrário, inclua "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Recupere o limite no número de checkpoints do modelo a serem mantidos
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Recupere o comprimento máximo da sequência
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construa o nome de exibição concatenando todos esses parâmetros, separados por hífens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Chame a função para gerar o nome de exibição
    pipeline_display_name = get_pipeline_display_name()
    # Imprima o nome de exibição
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configurando o Pipeline

Este script Python está definindo e configurando um pipeline de aprendizado de máquina usando o Azure Machine Learning SDK. Aqui está uma descrição do que ele faz:

1. Importa os módulos necessários do Azure AI ML SDK.

1. Busca um componente de pipeline chamado "chat_completion_pipeline" do registro.

1. Define um job pipeline usando o decorador `@pipeline` e a função `create_pipeline`. O nome do pipeline é definido como `pipeline_display_name`.

1. Dentro da função `create_pipeline`, inicializa o componente de pipeline buscado com vários parâmetros, incluindo o caminho do modelo, clusters computacionais para diferentes etapas, divisões de conjunto de dados para treinamento e teste, o número de GPUs a usar para fine tuning, e outros parâmetros de fine tuning.

1. Mapeia a saída do trabalho de fine tuning para a saída do job pipeline. Isso é feito para que o modelo fine tuned possa ser facilmente registrado, o que é necessário para implantar o modelo em um endpoint online ou batch.

1. Cria uma instância do pipeline chamando a função `create_pipeline`.

1. Define a configuração `force_rerun` do pipeline para `True`, o que significa que os resultados em cache de trabalhos anteriores não serão usados.

1. Define a configuração `continue_on_step_failure` do pipeline para `False`, o que significa que o pipeline será interrompido se algum passo falhar.

1. Em resumo, este script está definindo e configurando um pipeline de aprendizado de máquina para uma tarefa de chat completion usando o Azure Machine Learning SDK.

    ```python
    # Importe os módulos necessários do SDK Azure AI ML
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Busque o componente de pipeline chamado "chat_completion_pipeline" do registro
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Defina o job do pipeline usando o decorador @pipeline e a função create_pipeline
    # O nome do pipeline é definido como pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Inicialize o componente de pipeline buscado com vários parâmetros
        # Estes incluem o caminho do modelo, clusters de computação para diferentes estágios, divisões de conjunto de dados para treinamento e teste, o número de GPUs a usar para fine-tuning e outros parâmetros de fine-tuning
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Mapeie as divisões do conjunto de dados para parâmetros
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Configurações de treinamento
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Definido como o número de GPUs disponíveis na computação
            **finetune_parameters
        )
        return {
            # Mapeie a saída do job de fine tuning para a saída do job do pipeline
            # Isso é feito para que possamos registrar facilmente o modelo ajustado
            # Registrar o modelo é necessário para implantar o modelo em um endpoint online ou batch
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Crie uma instância do pipeline chamando a função create_pipeline
    pipeline_object = create_pipeline()
    
    # Não use resultados em cache de jobs anteriores
    pipeline_object.settings.force_rerun = True
    
    # Defina continuar em caso de falha na etapa como False
    # Isso significa que o pipeline irá parar se qualquer etapa falhar
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Enviar o Job

1. Este script Python está enviando um job de pipeline de aprendizado de máquina para um workspace do Azure Machine Learning e então aguardando a conclusão do job. Aqui está uma descrição do que ele faz:

    - Chama o método create_or_update do objeto jobs no workspace_ml_client para enviar o job do pipeline. O pipeline a ser executado é especificado por pipeline_object, e o experimento sob o qual o trabalho é executado é especificado por experiment_name.

    - Em seguida, chama o método stream do objeto jobs no workspace_ml_client para aguardar a conclusão do job do pipeline. O job a aguardar é especificado pelo atributo nome do objeto pipeline_job.

    - Em resumo, este script está enviando um job de pipeline de aprendizado de máquina para um workspace do Azure Machine Learning, e esperando a conclusão do trabalho.

    ```python
    # Enviar o trabalho do pipeline para o workspace do Azure Machine Learning
    # O pipeline a ser executado é especificado por pipeline_object
    # O experimento sob o qual o trabalho é executado é especificado por experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Aguarde a conclusão do trabalho do pipeline
    # O trabalho a ser aguardado é especificado pelo atributo name do objeto pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registrar o modelo fine tuned no workspace

Vamos registrar o modelo a partir da saída do trabalho de fine tuning. Isso rastreará a linhagem entre o modelo fine tuned e o trabalho de fine tuning. O trabalho de fine tuning, por sua vez, rastreia a linhagem do modelo foundation, dados e código de treinamento.

### Registrando o Modelo de ML

1. Este script Python está registrando um modelo de aprendizado de máquina que foi treinado em um pipeline do Azure Machine Learning. Aqui está uma descrição do que ele faz:

    - Importa os módulos necessários do Azure AI ML SDK.

    - Verifica se a saída trained_model está disponível do job pipeline, chamando o método get do objeto jobs no workspace_ml_client e acessando seu atributo outputs.

    - Constrói um caminho para o modelo treinado formatando uma string com o nome do job pipeline e o nome da saída ("trained_model").

    - Define um nome para o modelo fine tuned acrescentando "-ultrachat-200k" ao nome do modelo original e substituindo quaisquer barras por hífens.

    - Prepara o registro do modelo criando um objeto Model com vários parâmetros, incluindo o caminho para o modelo, o tipo do modelo (modelo MLflow), o nome e a versão do modelo, e uma descrição do modelo.

    - Registra o modelo chamando o método create_or_update do objeto models no workspace_ml_client com o objeto Model como argumento.

    - Imprime o modelo registrado.

1. Em resumo, este script está registrando um modelo de aprendizado de máquina que foi treinado em um pipeline do Azure Machine Learning.
    
    ```python
    # Importe os módulos necessários do SDK Azure AI ML
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Verifique se a saída `trained_model` está disponível no trabalho do pipeline
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construa um caminho para o modelo treinado formatando uma string com o nome do trabalho do pipeline e o nome da saída ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Defina um nome para o modelo ajustado adicionando "-ultrachat-200k" ao nome original do modelo e substituindo barras por hífens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare o registro do modelo criando um objeto Model com vários parâmetros
    # Estes incluem o caminho para o modelo, o tipo do modelo (modelo MLflow), o nome e a versão do modelo, e uma descrição do modelo
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp como versão para evitar conflito de versão
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Registre o modelo chamando o método create_or_update do objeto models em workspace_ml_client com o objeto Model como argumento
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Imprima o modelo registrado
    print("registered model: \n", registered_model)
    ```

## 7. Implantar o modelo fine tuned em um endpoint online

Endpoints online fornecem uma API REST durável que pode ser usada para integrar com aplicações que precisam usar o modelo.

### Gerenciar Endpoint

1. Este script Python está criando um endpoint online gerenciado no Azure Machine Learning para um modelo registrado. Aqui está uma descrição do que ele faz:

    - Importa os módulos necessários do Azure AI ML SDK.

    - Define um nome único para o endpoint online acrescentando um timestamp à string "ultrachat-completion-".

    - Prepara a criação do endpoint online criando um objeto ManagedOnlineEndpoint com vários parâmetros, incluindo o nome do endpoint, uma descrição do endpoint, e o modo de autenticação ("key").

    - Cria o endpoint online chamando o método begin_create_or_update do workspace_ml_client com o objeto ManagedOnlineEndpoint como argumento. Em seguida, aguarda a conclusão da operação de criação chamando o método wait.

1. Em resumo, este script está criando um endpoint online gerenciado no Azure Machine Learning para um modelo registrado.

    ```python
    # Importar módulos necessários do SDK Azure AI ML
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Definir um nome único para o endpoint online adicionando um timestamp à string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Preparar para criar o endpoint online criando um objeto ManagedOnlineEndpoint com vários parâmetros
    # Estes incluem o nome do endpoint, uma descrição do endpoint e o modo de autenticação ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Criar o endpoint online chamando o método begin_create_or_update do workspace_ml_client com o objeto ManagedOnlineEndpoint como argumento
    # Depois esperar a conclusão da operação de criação chamando o método wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Você pode encontrar aqui a lista de SKU's suportados para implantação - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Implantando Modelo de ML

1. Este script Python está implantando um modelo de aprendizado de máquina registrado em um endpoint online gerenciado no Azure Machine Learning. Aqui está uma descrição do que ele faz:

    - Importa o módulo ast, que fornece funções para processar árvores da gramática de sintaxe abstrata do Python.

    - Define o tipo de instância para a implantação como "Standard_NC6s_v3".

    - Verifica se a tag inference_compute_allow_list está presente no foundation model. Se estiver, converte o valor da tag de string para uma lista Python e a atribui a inference_computes_allow_list. Caso contrário, define inference_computes_allow_list como None.

    - Verifica se o tipo de instância especificado está na lista permitida. Se não estiver, imprime uma mensagem pedindo ao usuário para selecionar um tipo de instância da lista permitida.

    - Prepara a criação da implantação criando um objeto ManagedOnlineDeployment com vários parâmetros, incluindo o nome da implantação, o nome do endpoint, o ID do modelo, o tipo e a contagem da instância, as configurações da sondagem de liveness e as configurações de requisição.

    - Cria a implantação chamando o método begin_create_or_update do workspace_ml_client com o objeto ManagedOnlineDeployment como argumento. Em seguida, aguarda a conclusão da operação de criação chamando o método wait.

    - Define o tráfego do endpoint para direcionar 100% do tráfego para a implantação "demo".

    - Atualiza o endpoint chamando o método begin_create_or_update do workspace_ml_client com o objeto endpoint como argumento. Em seguida, aguarda a conclusão da operação de atualização chamando o método result.

1. Em resumo, este script está implantando um modelo de aprendizado de máquina registrado em um endpoint online gerenciado no Azure Machine Learning.

    ```python
    # Importe o módulo ast, que fornece funções para processar árvores da gramática de sintaxe abstrata do Python
    import ast
    
    # Defina o tipo de instância para o deployment
    instance_type = "Standard_NC6s_v3"
    
    # Verifique se a tag `inference_compute_allow_list` está presente no modelo base
    if "inference_compute_allow_list" in foundation_model.tags:
        # Se estiver, converta o valor da tag de uma string para uma lista Python e atribua-a a `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Se não estiver, defina `inference_computes_allow_list` como `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Verifique se o tipo de instância especificado está na lista permitida
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare-se para criar o deployment criando um objeto `ManagedOnlineDeployment` com vários parâmetros
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Crie o deployment chamando o método `begin_create_or_update` do `workspace_ml_client` com o objeto `ManagedOnlineDeployment` como argumento
    # Então espere a operação de criação ser concluída chamando o método `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Defina o tráfego do endpoint para direcionar 100% do tráfego ao deployment "demo"
    endpoint.traffic = {"demo": 100}
    
    # Atualize o endpoint chamando o método `begin_create_or_update` do `workspace_ml_client` com o objeto `endpoint` como argumento
    # Então espere a operação de atualização ser concluída chamando o método `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Testar o endpoint com dados de amostra

Vamos buscar alguns dados de amostra do conjunto de testes e enviar para o endpoint online para inferência. Em seguida, vamos mostrar as labels pontuadas ao lado das labels da verdade de terreno.

### Lendo os resultados

1. Este script Python está lendo um arquivo JSON Lines em um DataFrame do pandas, pegando uma amostra aleatória e resetando o índice. Aqui está uma descrição do que ele faz:

    - Lê o arquivo ./ultrachat_200k_dataset/test_gen.jsonl em um DataFrame do pandas. A função read_json é usada com o argumento lines=True porque o arquivo está no formato JSON Lines, onde cada linha é um objeto JSON separado.

    - Pega uma amostra aleatória de 1 linha do DataFrame. A função sample é usada com o argumento n=1 para especificar o número de linhas aleatórias a selecionar.

    - Reseta o índice do DataFrame. A função reset_index é usada com o argumento drop=True para descartar o índice original e substituí-lo por um novo índice com valores inteiros padrão.

    - Exibe as primeiras 2 linhas do DataFrame usando a função head com o argumento 2. Contudo, como o DataFrame contém apenas uma linha após a amostragem, isso exibirá apenas essa linha.

1. Em resumo, este script está lendo um arquivo JSON Lines em um DataFrame do pandas, pegando uma amostra aleatória de 1 linha, resetando o índice e exibindo a primeira linha.
    
    ```python
    # Importar a biblioteca pandas
    import pandas as pd
    
    # Ler o arquivo JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' em um DataFrame do pandas
    # O argumento 'lines=True' indica que o arquivo está no formato JSON Lines, onde cada linha é um objeto JSON separado
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Selecionar uma amostra aleatória de 1 linha do DataFrame
    # O argumento 'n=1' especifica o número de linhas aleatórias a serem selecionadas
    test_df = test_df.sample(n=1)
    
    # Redefinir o índice do DataFrame
    # O argumento 'drop=True' indica que o índice original deve ser descartado e substituído por um novo índice com valores inteiros padrão
    # O argumento 'inplace=True' indica que o DataFrame deve ser modificado no lugar (sem criar um novo objeto)
    test_df.reset_index(drop=True, inplace=True)
    
    # Exibir as primeiras 2 linhas do DataFrame
    # No entanto, como o DataFrame contém apenas uma linha após a amostragem, isso exibirá apenas essa única linha
    test_df.head(2)
    ```

### Criar Objeto JSON

1. Este script Python está criando um objeto JSON com parâmetros específicos e salvando-o em um arquivo. Aqui está uma descrição do que ele faz:

    - Importa o módulo json, que fornece funções para trabalhar com dados JSON.
    - Ele cria um dicionário parameters com chaves e valores que representam parâmetros para um modelo de aprendizado de máquina. As chaves são "temperature", "top_p", "do_sample" e "max_new_tokens", e seus valores correspondentes são 0.6, 0.9, True e 200, respectivamente.

    - Ele cria outro dicionário test_json com duas chaves: "input_data" e "params". O valor de "input_data" é outro dicionário com as chaves "input_string" e "parameters". O valor de "input_string" é uma lista contendo a primeira mensagem do DataFrame test_df. O valor de "parameters" é o dicionário parameters criado anteriormente. O valor de "params" é um dicionário vazio.

    - Ele abre um arquivo chamado sample_score.json
    
    ```python
    # Importe o módulo json, que fornece funções para trabalhar com dados JSON
    import json
    
    # Crie um dicionário `parameters` com chaves e valores que representam parâmetros para um modelo de aprendizado de máquina
    # As chaves são "temperature", "top_p", "do_sample" e "max_new_tokens", e seus valores correspondentes são 0.6, 0.9, True e 200, respectivamente
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Crie outro dicionário `test_json` com duas chaves: "input_data" e "params"
    # O valor de "input_data" é outro dicionário com as chaves "input_string" e "parameters"
    # O valor de "input_string" é uma lista contendo a primeira mensagem do DataFrame `test_df`
    # O valor de "parameters" é o dicionário `parameters` criado anteriormente
    # O valor de "params" é um dicionário vazio
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Abra um arquivo chamado `sample_score.json` no diretório `./ultrachat_200k_dataset` no modo de escrita
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Escreva o dicionário `test_json` no arquivo em formato JSON usando a função `json.dump`
        json.dump(test_json, f)
    ```

### Invocando Endpoint

1. Este script Python está invocando um endpoint online no Azure Machine Learning para avaliar um arquivo JSON. Aqui está uma explicação do que ele faz:

    - Ele chama o método invoke da propriedade online_endpoints do objeto workspace_ml_client. Esse método é usado para enviar uma solicitação a um endpoint online e obter uma resposta.

    - Ele especifica o nome do endpoint e da implantação com os argumentos endpoint_name e deployment_name. Neste caso, o nome do endpoint está armazenado na variável online_endpoint_name e o nome da implantação é "demo".

    - Ele especifica o caminho para o arquivo JSON a ser avaliado com o argumento request_file. Neste caso, o arquivo é ./ultrachat_200k_dataset/sample_score.json.

    - Ele armazena a resposta do endpoint na variável response.

    - Ele imprime a resposta bruta.

1. Em resumo, este script está invocando um endpoint online no Azure Machine Learning para avaliar um arquivo JSON e imprimindo a resposta.

    ```python
    # Invocar o endpoint online no Azure Machine Learning para pontuar o arquivo `sample_score.json`
    # O método `invoke` da propriedade `online_endpoints` do objeto `workspace_ml_client` é usado para enviar uma solicitação a um endpoint online e obter uma resposta
    # O argumento `endpoint_name` especifica o nome do endpoint, que está armazenado na variável `online_endpoint_name`
    # O argumento `deployment_name` especifica o nome da implantação, que é "demo"
    # O argumento `request_file` especifica o caminho para o arquivo JSON a ser pontuado, que é `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Imprimir a resposta bruta do endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Deletar o endpoint online

1. Não se esqueça de deletar o endpoint online, caso contrário, você deixará o medidor de cobrança funcionando para o compute usado pelo endpoint. Esta linha de código Python está deletando um endpoint online no Azure Machine Learning. Aqui está uma explicação do que ela faz:

    - Ela chama o método begin_delete da propriedade online_endpoints do objeto workspace_ml_client. Esse método é usado para iniciar a exclusão de um endpoint online.

    - Ela especifica o nome do endpoint a ser deletado com o argumento name. Neste caso, o nome do endpoint está armazenado na variável online_endpoint_name.

    - Ela chama o método wait para aguardar a conclusão da operação de exclusão. Esta é uma operação bloqueante, o que significa que ela impedirá que o script continue até que a exclusão esteja finalizada.

    - Em resumo, esta linha de código está iniciando a exclusão de um endpoint online no Azure Machine Learning e aguardando a conclusão da operação.

    ```python
    # Excluir o endpoint online no Azure Machine Learning
    # O método `begin_delete` da propriedade `online_endpoints` do objeto `workspace_ml_client` é usado para iniciar a exclusão de um endpoint online
    # O argumento `name` especifica o nome do endpoint a ser excluído, que está armazenado na variável `online_endpoint_name`
    # O método `wait` é chamado para aguardar a conclusão da operação de exclusão. Esta é uma operação bloqueante, o que significa que impedirá o script de continuar até que a exclusão seja concluída
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->