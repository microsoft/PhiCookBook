# Avaliar o Modelo Phi-3 / Phi-3.5 Ajustado na Microsoft Foundry com Foco nos Princípios de IA Responsável da Microsoft

Este exemplo de ponta a ponta (E2E) é baseado no guia "[Avaliar Modelos Phi-3 / 3.5 Ajustados na Microsoft Foundry com Foco nos Princípios de IA Responsável da Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community.

## Visão Geral

### Como você pode avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 ajustado na Microsoft Foundry?

O ajuste fino de um modelo pode às vezes levar a respostas indesejadas ou não intencionais. Para garantir que o modelo permaneça seguro e eficaz, é importante avaliar o potencial do modelo para gerar conteúdo nocivo e sua capacidade de produzir respostas precisas, relevantes e coerentes. Neste tutorial, você aprenderá como avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 ajustado, integrado com Prompt flow na Microsoft Foundry.

Aqui está o processo de avaliação da Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/pt-BR/architecture.10bec55250f5d6a4.webp)

*Fonte da Imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para informações mais detalhadas e para explorar recursos adicionais sobre Phi-3 / Phi-3.5, visite o [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Pré-requisitos

- [Python](https://www.python.org/downloads)
- [Assinatura Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Phi-3 / Phi-3.5 ajustado

### Índice

1. [**Cenário 1: Introdução à avaliação com Prompt flow da Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Introdução à avaliação de segurança](#introdução-à-avaliação-de-segurança)
    - [Introdução à avaliação de desempenho](#introdução-à-avaliação-de-desempenho)

1. [**Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 na Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Antes de começar](#antes-de-começar)
    - [Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Avaliar o modelo Phi-3 / Phi-3.5 ajustado usando a avaliação Prompt flow da Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Parabéns!](#parabéns)

## **Cenário 1: Introdução à avaliação com Prompt flow da Microsoft Foundry**

### Introdução à avaliação de segurança

Para garantir que seu modelo de IA seja ético e seguro, é crucial avaliá-lo com base nos Princípios de IA Responsável da Microsoft. Na Microsoft Foundry, as avaliações de segurança permitem que você avalie a vulnerabilidade do seu modelo a ataques de jailbreak e seu potencial para gerar conteúdo nocivo, o que está diretamente alinhado a esses princípios.

![Safaty evaluation.](../../../../../../translated_images/pt-BR/safety-evaluation.083586ec88dfa950.webp)

*Fonte da Imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Princípios de IA Responsável da Microsoft

Antes de iniciar as etapas técnicas, é essencial entender os Princípios de IA Responsável da Microsoft, uma estrutura ética projetada para orientar o desenvolvimento, implantação e operação responsáveis de sistemas de IA. Esses princípios guiam o design, desenvolvimento e implantação responsáveis de sistemas de IA, garantindo que as tecnologias de IA sejam construídas de forma justa, transparente e inclusiva. Esses princípios são a base para avaliar a segurança dos modelos de IA.

Os Princípios de IA Responsável da Microsoft incluem:

- **Justiça e Inclusividade**: Sistemas de IA devem tratar todos de forma justa e evitar afetar grupos de pessoas em situações semelhantes de maneira diferente. Por exemplo, quando sistemas de IA fornecem orientação sobre tratamentos médicos, solicitações de empréstimos ou emprego, eles devem oferecer as mesmas recomendações para todos que possuem sintomas, circunstâncias financeiras ou qualificações profissionais semelhantes.

- **Confiabilidade e Segurança**: Para construir confiança, é fundamental que os sistemas de IA operem de forma confiável, segura e consistente. Esses sistemas devem ser capazes de funcionar conforme originalmente projetados, responder com segurança a condições imprevistas e resistir a manipulações nocivas. O comportamento e a variedade de condições que podem lidar refletem o conjunto de situações e circunstâncias que os desenvolvedores anteviram durante o design e teste.

- **Transparência**: Quando sistemas de IA auxiliam nas decisões que têm impactos significativos na vida das pessoas, é fundamental que as pessoas entendam como essas decisões foram tomadas. Por exemplo, um banco pode usar um sistema de IA para decidir se uma pessoa é creditável. Uma empresa pode usar um sistema de IA para determinar os candidatos mais qualificados para contratação.

- **Privacidade e Segurança**: À medida que a IA se torna mais prevalente, proteger a privacidade e assegurar informações pessoais e comerciais torna-se mais importante e complexo. Na IA, privacidade e segurança de dados exigem atenção próxima porque o acesso a dados é essencial para que os sistemas de IA façam previsões e decisões precisas e informadas sobre as pessoas.

- **Responsabilidade**: As pessoas que projetam e implementam sistemas de IA devem ser responsáveis por como seus sistemas operam. As organizações devem utilizar padrões da indústria para desenvolver normas de responsabilidade. Essas normas podem garantir que sistemas de IA não sejam a autoridade final em qualquer decisão que afete a vida das pessoas. Elas também podem assegurar que humanos mantenham controle significativo sobre sistemas de IA altamente autônomos.

![Fill hub.](../../../../../../translated_images/pt-BR/responsibleai2.c07ef430113fad8c.webp)

*Fonte da Imagem: [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para saber mais sobre os Princípios de IA Responsável da Microsoft, visite o [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de segurança

Neste tutorial, você avaliará a segurança do modelo Phi-3 ajustado usando as métricas de segurança da Microsoft Foundry. Essas métricas ajudam a avaliar o potencial do modelo para gerar conteúdo nocivo e sua vulnerabilidade a ataques de jailbreak. As métricas de segurança incluem:

- **Conteúdo Relacionado a Auto-prejuízo**: Avalia se o modelo tem tendência a produzir conteúdo relacionado a auto-prejuízo.
- **Conteúdo Odioso e Injusto**: Avalia se o modelo tem tendência a produzir conteúdo odioso ou injusto.
- **Conteúdo Violento**: Avalia se o modelo tem tendência a produzir conteúdo violento.
- **Conteúdo Sexual**: Avalia se o modelo tem tendência a produzir conteúdo sexual inapropriado.

Avaliar esses aspectos garante que o modelo de IA não produza conteúdo nocivo ou ofensivo, alinhando-o com valores sociais e normas regulatórias.

![Evaluate based on safety.](../../../../../../translated_images/pt-BR/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introdução à avaliação de desempenho

Para garantir que seu modelo de IA esteja performando conforme esperado, é importante avaliar seu desempenho com base em métricas de desempenho. Na Microsoft Foundry, as avaliações de desempenho permitem que você avalie a eficácia do seu modelo em gerar respostas precisas, relevantes e coerentes.

![Safaty evaluation.](../../../../../../translated_images/pt-BR/performance-evaluation.48b3e7e01a098740.webp)

*Fonte da Imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de desempenho

Neste tutorial, você avaliará o desempenho do modelo Phi-3 / Phi-3.5 ajustado usando as métricas de desempenho da Microsoft Foundry. Essas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes. As métricas de desempenho incluem:

- **Fundamentação**: Avalia o quanto as respostas geradas estão alinhadas com as informações da fonte de entrada.
- **Relevância**: Avalia a pertinência das respostas geradas às perguntas feitas.
- **Coerência**: Avalia a fluidez do texto gerado, se lê naturalmente e se assemelha a uma linguagem humana.
- **Fluência**: Avalia a proficiência linguística do texto gerado.
- **Similaridade GPT**: Compara a resposta gerada com a verdade de referência para medir similaridade.
- **Pontuação F1**: Calcula a proporção de palavras compartilhadas entre a resposta gerada e os dados de origem.

Essas métricas ajudam a avaliar a eficácia do modelo para gerar respostas precisas, relevantes e coerentes.

![Evaluate based on performance.](../../../../../../translated_images/pt-BR/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 na Microsoft Foundry**

### Antes de começar

Este tutorial é uma continuação dos posts anteriores, "[Ajuste Fino e Integre Modelos Personalizados Phi-3 com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Ajuste Fino e Integre Modelos Personalizados Phi-3 com Prompt Flow na Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)". Nestes posts, percorremos o processo de ajuste fino de um modelo Phi-3 / Phi-3.5 na Microsoft Foundry e sua integração com Prompt flow.

Neste tutorial, você implantará um modelo Azure OpenAI como avaliador na Microsoft Foundry e o usará para avaliar seu modelo Phi-3 / Phi-3.5 ajustado.

Antes de iniciar este tutorial, verifique se possui os seguintes pré-requisitos, conforme descrito nos tutoriais anteriores:

1. Um conjunto de dados preparado para avaliar o modelo Phi-3 / Phi-3.5 ajustado.
1. Um modelo Phi-3 / Phi-3.5 que tenha sido ajustado e implantado no Azure Machine Learning.
1. Um Prompt flow integrado ao seu modelo Phi-3 / Phi-3.5 ajustado na Microsoft Foundry.

> [!NOTE]
> Você usará o arquivo *test_data.jsonl*, localizado na pasta data do conjunto de dados **ULTRACHAT_200k** baixado nos posts anteriores, como conjunto de dados para avaliar o modelo Phi-3 / Phi-3.5 ajustado.

#### Integre o modelo personalizado Phi-3 / Phi-3.5 com Prompt flow na Microsoft Foundry (abordagem primeiro código)

> [!NOTE]
> Se você seguiu a abordagem low-code descrita em "[Ajuste Fino e Integre Modelos Personalizados Phi-3 com Prompt Flow na Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", pode pular este exercício e prosseguir para o próximo.
> No entanto, se você seguiu a abordagem code-first descrita em "[Ajuste Fino e Integre Modelos Personalizados Phi-3 com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para ajustar e implantar seu modelo Phi-3 / Phi-3.5, o processo de conexão do modelo com Prompt flow é ligeiramente diferente. Você aprenderá esse processo neste exercício.

Para prosseguir, você precisa integrar seu modelo Phi-3 / Phi-3.5 ajustado ao Prompt flow na Microsoft Foundry.

#### Criar Hub da Microsoft Foundry

Você precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo organizar e gerenciar múltiplos Projetos dentro da Microsoft Foundry.
1. Faça login no [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecione **Todos os hubs** na aba lateral esquerda.

1. Selecione **+ Novo hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/pt-BR/create-hub.5be78fb1e21ffbf1.webp)

1. Realize as seguintes tarefas:

    - Insira o **Nome do hub**. Deve ser um valor único.
    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** a ser usado (crie um novo, se necessário).
    - Selecione a **Localização** que deseja usar.
    - Selecione **Conectar Serviços Azure AI** para usar (crie um novo, se necessário).
    - Selecione **Conectar Azure AI Search** para **Pular conexão**.

    ![Fill hub.](../../../../../../translated_images/pt-BR/fill-hub.baaa108495c71e34.webp)

1. Selecione **Avançar**.

#### Criar Projeto Microsoft Foundry

1. No Hub que você criou, selecione **Todos os projetos** na aba lateral esquerda.

1. Selecione **+ Novo projeto** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/pt-BR/select-new-project.cd31c0404088d7a3.webp)

1. Insira o **Nome do projeto**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/pt-BR/create-project.ca3b71298b90e420.webp)

1. Selecione **Criar projeto**.

#### Adicionar uma conexão personalizada para o modelo Phi-3 / Phi-3.5 ajustado

Para integrar seu modelo Phi-3 / Phi-3.5 personalizado com o Prompt flow, você precisa salvar o endpoint e a chave do modelo em uma conexão personalizada. Essa configuração garante o acesso ao seu modelo Phi-3 / Phi-3.5 personalizado no Prompt flow.

#### Definir chave api e URI do endpoint do modelo Phi-3 / Phi-3.5 ajustado

1. Visite o [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue para o workspace Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba lateral esquerda.

    ![Select endpoints.](../../../../../../translated_images/pt-BR/select-endpoints.ee7387ecd68bd18d.webp)

1. Selecione o endpoint que você criou.

    ![Select endpoints.](../../../../../../translated_images/pt-BR/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Selecione **Consumir** no menu de navegação.

1. Copie seu **Endpoint REST** e **Chave primária**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pt-BR/copy-endpoint-key.0650c3786bd646ab.webp)

#### Adicionar a Conexão Personalizada

1. Visite o [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Microsoft Foundry que você criou.

1. No projeto que você criou, selecione **Configurações** na aba lateral esquerda.

1. Selecione **+ Nova conexão**.

    ![Select new connection.](../../../../../../translated_images/pt-BR/select-new-connection.fa0f35743758a74b.webp)

1. Selecione **Chaves personalizadas** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/pt-BR/select-custom-keys.5a3c6b25580a9b67.webp)

1. Realize as seguintes tarefas:

    - Selecione **+ Adicionar pares de chave-valor**.
    - Para o nome da chave, insira **endpoint** e cole o endpoint que você copiou do Azure ML Studio no campo de valor.
    - Selecione **+ Adicionar pares de chave-valor** novamente.
    - Para o nome da chave, insira **key** e cole a chave que você copiou do Azure ML Studio no campo de valor.
    - Após adicionar as chaves, selecione **é segredo** para evitar que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/pt-BR/add-connection.ac7f5faf8b10b0df.webp)

1. Selecione **Adicionar conexão**.

#### Criar Prompt flow

Você adicionou uma conexão personalizada no Microsoft Foundry. Agora, vamos criar um Prompt flow usando os seguintes passos. Depois, você conectará este Prompt flow à conexão personalizada para usar o modelo ajustado dentro do Prompt flow.

1. Navegue até o projeto Microsoft Foundry que você criou.

1. Selecione **Prompt flow** na aba lateral esquerda.

1. Selecione **+ Criar** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/pt-BR/select-promptflow.18ff2e61ab9173eb.webp)

1. Selecione **Fluxo de chat** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/pt-BR/select-flow-type.28375125ec9996d3.webp)

1. Insira o **Nome da pasta** a ser usada.

    ![Select chat flow.](../../../../../../translated_images/pt-BR/enter-name.02ddf8fb840ad430.webp)

1. Selecione **Criar**.

#### Configurar Prompt flow para conversar com seu modelo Phi-3 / Phi-3.5 personalizado

Você precisa integrar o modelo Phi-3 / Phi-3.5 ajustado em um Prompt flow. Contudo, o Prompt flow existente fornecido não foi projetado para esse propósito. Portanto, você deve redesenhar o Prompt flow para permitir a integração do modelo personalizado.

1. No Prompt flow, realize as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Modo arquivo bruto**.
    - Apague todo o código existente no arquivo *flow.dag.yml*.
    - Adicione o código a seguir em *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/pt-BR/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Adicione o seguinte código em *integrate_with_promptflow.py* para usar o modelo Phi-3 / Phi-3.5 personalizado no Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configuração de registro
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" é o nome da Conexão Personalizada, "endpoint", "key" são as chaves na Conexão Personalizada
        endpoint_url = connection.endpoint
        api_key = connection.key

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
            
            # Registrar a resposta JSON completa
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/pt-BR/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Para informações mais detalhadas sobre como usar o Prompt flow no Microsoft Foundry, você pode consultar [Prompt flow no Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Entrada do chat**, **Saída do chat** para habilitar o chat com seu modelo.

    ![Select Input Output.](../../../../../../translated_images/pt-BR/select-input-output.c187fc58f25fbfc3.webp)

1. Agora você está pronto para conversar com seu modelo Phi-3 / Phi-3.5 personalizado. No próximo exercício, você aprenderá como iniciar o Prompt flow e usá-lo para conversar com seu modelo Phi-3 / Phi-3.5 ajustado.

> [!NOTE]
>
> O fluxo reconstruído deve se parecer com a imagem abaixo:
>
> ![Flow example](../../../../../../translated_images/pt-BR/graph-example.82fd1bcdd3fc545b.webp)
>

#### Iniciar Prompt flow

1. Selecione **Iniciar sessões de computação** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pt-BR/start-compute-session.9acd8cbbd2c43df1.webp)

1. Selecione **Validar e analisar entrada** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/pt-BR/validate-input.c1adb9543c6495be.webp)

1. Selecione o **Valor** da **conexão** para a conexão personalizada que você criou. Por exemplo, *conexão*.

    ![Connection.](../../../../../../translated_images/pt-BR/select-connection.1f2b59222bcaafef.webp)

#### Conversar com seu modelo Phi-3 / Phi-3.5 personalizado

1. Selecione **Chat**.

    ![Select chat.](../../../../../../translated_images/pt-BR/select-chat.0406bd9687d0c49d.webp)

1. Aqui está um exemplo dos resultados: Agora você pode conversar com seu modelo Phi-3 / Phi-3.5 personalizado. Recomenda-se fazer perguntas baseadas nos dados utilizados para o ajuste fino.

    ![Chat with prompt flow.](../../../../../../translated_images/pt-BR/chat-with-promptflow.1cf8cea112359ada.webp)

### Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5

Para avaliar o modelo Phi-3 / Phi-3.5 no Microsoft Foundry, você precisa implantar um modelo Azure OpenAI. Esse modelo será usado para avaliar o desempenho do modelo Phi-3 / Phi-3.5.

#### Implantar Azure OpenAI

1. Faça login no [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Microsoft Foundry que você criou.

    ![Select Project.](../../../../../../translated_images/pt-BR/select-project-created.5221e0e403e2c9d6.webp)

1. No projeto que você criou, selecione **Implantações** na aba lateral esquerda.

1. Selecione **+ Implantar modelo** no menu de navegação.

1. Selecione **Implantar modelo base**.

    ![Select Deployments.](../../../../../../translated_images/pt-BR/deploy-openai-model.95d812346b25834b.webp)

1. Selecione o modelo Azure OpenAI que deseja usar. Por exemplo, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/pt-BR/select-openai-model.959496d7e311546d.webp)

1. Selecione **Confirmar**.

### Avaliar o modelo Phi-3 / Phi-3.5 ajustado usando a avaliação Prompt flow do Microsoft Foundry

### Iniciar uma nova avaliação

1. Visite o [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Microsoft Foundry que você criou.

    ![Select Project.](../../../../../../translated_images/pt-BR/select-project-created.5221e0e403e2c9d6.webp)

1. No projeto que você criou, selecione **Avaliação** na aba lateral esquerda.

1. Selecione **+ Nova avaliação** no menu de navegação.

    ![Select evaluation.](../../../../../../translated_images/pt-BR/select-evaluation.2846ad7aaaca7f4f.webp)

1. Selecione avaliação **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/pt-BR/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Realize as seguintes tarefas:

    - Insira o nome da avaliação. Deve ser um valor único.
    - Selecione **Pergunta e resposta sem contexto** como tipo de tarefa. Porque o conjunto de dados **UlTRACHAT_200k** usado neste tutorial não contém contexto.
    - Selecione o prompt flow que deseja avaliar.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-BR/evaluation-setting1.4aa08259ff7a536e.webp)

1. Selecione **Avançar**.

1. Realize as seguintes tarefas:

    - Selecione **Adicionar seu conjunto de dados** para enviar o conjunto de dados. Por exemplo, você pode enviar o arquivo de conjunto de dados de teste, como *test_data.json1*, que está incluído quando você baixa o conjunto de dados **ULTRACHAT_200k**.
    - Selecione a **Coluna do conjunto de dados** apropriada que corresponda ao seu conjunto de dados. Por exemplo, se estiver usando o conjunto de dados **ULTRACHAT_200k**, selecione **${data.prompt}** como a coluna do conjunto de dados.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-BR/evaluation-setting2.07036831ba58d64e.webp)

1. Selecione **Avançar**.

1. Realize as seguintes tarefas para configurar as métricas de desempenho e qualidade:

    - Selecione as métricas de desempenho e qualidade que deseja usar.
    - Selecione o modelo Azure OpenAI que você criou para avaliação. Por exemplo, selecione **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-BR/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Realize as seguintes tarefas para configurar as métricas de risco e segurança:

    - Selecione as métricas de risco e segurança que deseja usar.
    - Selecione o limite para calcular a taxa de defeitos que deseja usar. Por exemplo, selecione **Médio**.
    - Para **pergunta**, selecione **Fonte dos dados** para **{$data.prompt}**.
    - Para **resposta**, selecione **Fonte dos dados** para **{$run.outputs.answer}**.
    - Para **verdadeiro**, selecione **Fonte dos dados** para **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-BR/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Selecione **Avançar**.

1. Selecione **Enviar** para iniciar a avaliação.

1. A avaliação levará algum tempo para ser concluída. Você pode monitorar o progresso na aba **Avaliação**.

### Revisar os Resultados da Avaliação

> [!NOTE]
> Os resultados apresentados abaixo destinam-se a ilustrar o processo de avaliação. Neste tutorial, utilizamos um modelo ajustado em um conjunto de dados relativamente pequeno, o que pode levar a resultados subótimos. Os resultados reais podem variar significativamente dependendo do tamanho, qualidade e diversidade do conjunto de dados usado, bem como da configuração específica do modelo.

Após a conclusão da avaliação, você pode revisar os resultados tanto das métricas de desempenho quanto das métricas de segurança.
1. Métricas de desempenho e qualidade:

    - avalie a eficácia do modelo em gerar respostas coerentes, fluentes e relevantes.

    ![Evaluation result.](../../../../../../translated_images/pt-BR/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Métricas de risco e segurança:

    - Garanta que as saídas do modelo sejam seguras e estejam alinhadas com os Princípios de IA Responsável, evitando qualquer conteúdo prejudicial ou ofensivo.

    ![Evaluation result.](../../../../../../translated_images/pt-BR/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Você pode rolar para baixo para visualizar o **Resultado detalhado das métricas**.

    ![Evaluation result.](../../../../../../translated_images/pt-BR/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Ao avaliar seu modelo personalizado Phi-3 / Phi-3.5 em relação às métricas de desempenho e segurança, você pode confirmar que o modelo não é apenas eficaz, mas também adere às práticas de IA responsável, tornando-o pronto para implantação no mundo real.

## Parabéns!

### Você concluiu este tutorial

Você avaliou com sucesso o modelo Phi-3 ajustado integrado ao Prompt flow no Microsoft Foundry. Este é um passo importante para garantir que seus modelos de IA não apenas ofereçam bom desempenho, mas também estejam alinhados com os princípios de IA Responsável da Microsoft para ajudar a construir aplicações de IA confiáveis e seguras.

![Architecture.](../../../../../../translated_images/pt-BR/architecture.10bec55250f5d6a4.webp)

## Limpar recursos do Azure

Limpe seus recursos do Azure para evitar cobranças adicionais em sua conta. Acesse o portal do Azure e exclua os seguintes recursos:

- O recurso Azure Machine Learning.
- O endpoint do modelo Azure Machine Learning.
- O recurso do projeto Microsoft Foundry.
- O recurso Microsoft Foundry Prompt flow.

### Próximos passos

#### Documentação

- [Avalie sistemas de IA usando o painel de IA Responsável](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de avaliação e monitoramento para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentação do Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentação do Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conteúdo de Treinamento

- [Introdução à abordagem de IA Responsável da Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introdução ao Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referência

- [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anúncio de novas ferramentas no Azure AI para ajudar a criar aplicações de IA generativa mais seguras e confiáveis](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para alcançar a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->