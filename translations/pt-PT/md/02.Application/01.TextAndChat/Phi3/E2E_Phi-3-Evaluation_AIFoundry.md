# Avaliar o Modelo Phi-3 / Phi-3.5 Ajustado na Microsoft Foundry com Foco nos Princípios de IA Responsável da Microsoft

Este exemplo de ponta a ponta (E2E) baseia-se no guia "[Avaliar Modelos Phi-3 / 3.5 Ajustados na Microsoft Foundry com Foco nos Princípios de IA Responsável da Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community.

## Visão Geral

### Como pode avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 ajustado na Microsoft Foundry?

Ajustar um modelo pode por vezes levar a respostas não intencionais ou indesejadas. Para garantir que o modelo permanece seguro e eficaz, é importante avaliar o potencial do modelo para gerar conteúdo nocivo e a sua capacidade de produzir respostas precisas, relevantes e coerentes. Neste tutorial, irá aprender a avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 ajustado integrado com Prompt flow na Microsoft Foundry.

Aqui está o processo de avaliação da Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/pt-PT/architecture.10bec55250f5d6a4.webp)

*Fonte da imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para informações mais detalhadas e para explorar recursos adicionais sobre Phi-3 / Phi-3.5, por favor visite o [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Pré-requisitos

- [Python](https://www.python.org/downloads)
- [Subscrição Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Phi-3 / Phi-3.5 ajustado

### Índice

1. [**Cenário 1: Introdução à avaliação Prompt flow da Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Introdução à avaliação de segurança](#introdução-à-avaliação-de-segurança)
    - [Introdução à avaliação de desempenho](#introdução-à-avaliação-de-desempenho)

1. [**Cenário 2: Avaliação do modelo Phi-3 / Phi-3.5 na Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Antes de começar](#antes-de-começar)
    - [Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Avaliar o modelo Phi-3 / Phi-3.5 ajustado usando a avaliação Prompt flow da Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Parabéns!](#parabéns)

## **Cenário 1: Introdução à avaliação Prompt flow da Microsoft Foundry**

### Introdução à avaliação de segurança

Para garantir que o seu modelo de IA seja ético e seguro, é crucial avaliá-lo tendo por base os Princípios de IA Responsável da Microsoft. Na Microsoft Foundry, as avaliações de segurança permitem avaliar a vulnerabilidade do seu modelo a ataques de jailbreak e o seu potencial para gerar conteúdo nocivo, o que está diretamente alinhado com estes princípios.

![Safaty evaluation.](../../../../../../translated_images/pt-PT/safety-evaluation.083586ec88dfa950.webp)

*Fonte da imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Princípios de IA Responsável da Microsoft

Antes de iniciar os passos técnicos, é essencial compreender os Princípios de IA Responsável da Microsoft, uma estrutura ética concebida para orientar o desenvolvimento, implementação e operação responsáveis de sistemas de IA. Estes princípios orientam o design, desenvolvimento e implementação responsáveis de sistemas de IA, garantindo que as tecnologias de IA sejam construídas de forma justa, transparente e inclusiva. Estes princípios são a base para avaliar a segurança dos modelos de IA.

Os Princípios de IA Responsável da Microsoft incluem:

- **Justiça e Inclusividade**: Os sistemas de IA devem tratar todos de forma justa e evitar afetar grupos semelhantes de pessoas de maneiras diferentes. Por exemplo, quando os sistemas de IA fornecem orientações sobre tratamento médico, pedidos de empréstimo ou emprego, devem fazer as mesmas recomendações a todos os que tenham sintomas, circunstâncias financeiras ou qualificações profissionais semelhantes.

- **Confiabilidade e Segurança**: Para gerar confiança, é crítico que os sistemas de IA operem de forma confiável, segura e consistente. Estes sistemas devem ser capazes de funcionar como foram originalmente concebidos, responder de forma segura a condições não previstas e resistir a manipulações nocivas. O seu comportamento e a variedade de condições que podem gerir refletem o leque de situações e circunstâncias que os desenvolvedores anteciparam durante o design e os testes.

- **Transparência**: Quando os sistemas de IA ajudam a informar decisões que têm um grande impacto na vida das pessoas, é crucial que as pessoas compreendam como essas decisões foram tomadas. Por exemplo, um banco pode usar um sistema de IA para decidir se uma pessoa é credível financeiramente. Uma empresa pode usar um sistema de IA para determinar os candidatos mais qualificados para contratar.

- **Privacidade e Segurança**: À medida que a IA se torna mais prevalente, proteger a privacidade e assegurar a informação pessoal e empresarial torna-se cada vez mais importante e complexo. Com a IA, a privacidade e a segurança dos dados requerem atenção especial porque o acesso a dados é essencial para que os sistemas de IA façam previsões e decisões precisas e informadas sobre as pessoas.

- **Responsabilização**: As pessoas que projetam e implementam sistemas de IA devem ser responsáveis pelo modo como os seus sistemas operam. As organizações devem basear-se em normas da indústria para desenvolver normas de responsabilização. Estas normas podem garantir que os sistemas de IA não sejam a autoridade final em qualquer decisão que afete a vida das pessoas. Podem também garantir que os humanos mantenham controlo significativo sobre sistemas de IA altamente autónomos.

![Fill hub.](../../../../../../translated_images/pt-PT/responsibleai2.c07ef430113fad8c.webp)

*Fonte da imagem: [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para saber mais sobre os Princípios de IA Responsável da Microsoft, visite [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de segurança

Neste tutorial, irá avaliar a segurança do modelo Phi-3 ajustado usando as métricas de segurança da Microsoft Foundry. Estas métricas ajudam a avaliar o potencial do modelo para gerar conteúdo nocivo e a sua vulnerabilidade a ataques de jailbreak. As métricas de segurança incluem:

- **Conteúdo relacionado com auto-mutilação**: Avalia se o modelo tem tendência para produzir conteúdo relacionado com auto-mutilação.
- **Conteúdo odioso e injusto**: Avalia se o modelo tem tendência para produzir conteúdo odioso ou injusto.
- **Conteúdo violento**: Avalia se o modelo tem tendência para produzir conteúdo violento.
- **Conteúdo sexual**: Avalia se o modelo tem tendência para produzir conteúdo sexual inapropriado.

Avaliar estes aspetos assegura que o modelo de IA não produza conteúdo nocivo ou ofensivo, alinhando-o com os valores sociais e normas regulamentares.

![Evaluate based on safety.](../../../../../../translated_images/pt-PT/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introdução à avaliação de desempenho

Para garantir que o seu modelo de IA está a funcionar conforme o esperado, é importante avaliar o seu desempenho com base em métricas de desempenho. Na Microsoft Foundry, as avaliações de desempenho permitem avaliar a eficácia do seu modelo na geração de respostas precisas, relevantes e coerentes.

![Safaty evaluation.](../../../../../../translated_images/pt-PT/performance-evaluation.48b3e7e01a098740.webp)

*Fonte da imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de desempenho

Neste tutorial, irá avaliar o desempenho do modelo Phi-3 / Phi-3.5 ajustado usando as métricas de desempenho da Microsoft Foundry. Estas métricas ajudam a avaliar a eficácia do modelo na geração de respostas precisas, relevantes e coerentes. As métricas de desempenho incluem:

- **Fundamentação**: Avalia o quanto as respostas geradas estão alinhadas com as informações da fonte de entrada.
- **Relevância**: Avalia a pertinência das respostas geradas às perguntas feitas.
- **Coerência**: Avalia a fluidez do texto gerado, sua naturalidade e semelhança com a linguagem humana.
- **Fluência**: Avalia a proficiência linguística do texto gerado.
- **Semelhança GPT**: Compara a resposta gerada com a verdade fundamental para medir a semelhança.
- **Pontuação F1**: Calcula a proporção de palavras comuns entre a resposta gerada e os dados fonte.

Estas métricas ajudam a avaliar a eficácia do modelo na geração de respostas precisas, relevantes e coerentes.

![Evaluate based on performance.](../../../../../../translated_images/pt-PT/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Cenário 2: Avaliar o modelo Phi-3 / Phi-3.5 na Microsoft Foundry**

### Antes de começar

Este tutorial é a continuação dos posts anteriores, "[Ajustar e Integrar Modelos Phi-3 Personalizados com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Ajustar e Integrar Modelos Phi-3 Personalizados com Prompt Flow na Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Nestes posts, percorremos o processo de ajuste fino de um modelo Phi-3 / Phi-3.5 na Microsoft Foundry e a sua integração com Prompt flow.

Neste tutorial, irá implantar um modelo Azure OpenAI como avaliador na Microsoft Foundry e usá-lo para avaliar o seu modelo Phi-3 / Phi-3.5 ajustado.

Antes de começar este tutorial, certifique-se de que tem os seguintes pré-requisitos, conforme descrito nos tutoriais anteriores:

1. Um conjunto de dados preparado para avaliar o modelo Phi-3 / Phi-3.5 ajustado.
1. Um modelo Phi-3 / Phi-3.5 que tenha sido ajustado e implantado no Azure Machine Learning.
1. Um Prompt flow integrado com o seu modelo Phi-3 / Phi-3.5 ajustado na Microsoft Foundry.

> [!NOTE]
> Vai usar o ficheiro *test_data.jsonl*, localizado na pasta data do conjunto de dados **ULTRACHAT_200k** descarregado nos posts anteriores, como o conjunto de dados para avaliar o modelo Phi-3 / Phi-3.5 ajustado.

#### Integrar o modelo Phi-3 / Phi-3.5 personalizado com Prompt flow na Microsoft Foundry ( abordagem code first )

> [!NOTE]
> Se seguiu a abordagem low-code descrita em "[Ajustar e Integrar Modelos Phi-3 Personalizados com Prompt Flow na Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", pode saltar este exercício e avançar para o próximo.
> No entanto, se seguiu a abordagem code-first descrita em "[Ajustar e Integrar Modelos Phi-3 Personalizados com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para ajustar e implantar o seu modelo Phi-3 / Phi-3.5, o processo de ligação do seu modelo ao Prompt flow é ligeiramente diferente. Irá aprender este processo neste exercício.

Para continuar, precisa de integrar o seu modelo Phi-3 / Phi-3.5 ajustado no Prompt flow na Microsoft Foundry.

#### Criar Microsoft Foundry Hub

Precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo organizar e gerir múltiplos Projetos dentro da Microsoft Foundry.
1. Inicie sessão em [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecione **Todos os hubs** na aba do lado esquerdo.

1. Selecione **+ Novo hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/pt-PT/create-hub.5be78fb1e21ffbf1.webp)

1. Execute as seguintes tarefas:

    - Introduza o **Nome do hub**. Deve ser um valor único.
    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a utilizar (crie um novo se necessário).
    - Selecione a **Localização** que pretende usar.
    - Selecione os **Serviços Azure AI para ligar** a utilizar (crie um novo se necessário).
    - Selecione **Ligar Azure AI Search** para **Ignorar ligação**.

    ![Fill hub.](../../../../../../translated_images/pt-PT/fill-hub.baaa108495c71e34.webp)

1. Selecione **Seguinte**.

#### Criar projeto Microsoft Foundry

1. No Hub que criou, selecione **Todos os projetos** na aba do lado esquerdo.

1. Selecione **+ Novo projeto** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/pt-PT/select-new-project.cd31c0404088d7a3.webp)

1. Introduza o **Nome do projeto**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/pt-PT/create-project.ca3b71298b90e420.webp)

1. Selecione **Criar um projeto**.

#### Adicionar uma ligação personalizada para o modelo Phi-3 / Phi-3.5 afinado

Para integrar o seu modelo personalizado Phi-3 / Phi-3.5 com o Prompt flow, precisa de guardar o endpoint e a chave do modelo numa ligação personalizada. Esta configuração garante o acesso ao seu modelo personalizado Phi-3 / Phi-3.5 no Prompt flow.

#### Definir a chave API e o URI do endpoint do modelo afinado Phi-3 / Phi-3.5

1. Visite o [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até ao espaço de trabalho Azure Machine Learning que criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/pt-PT/select-endpoints.ee7387ecd68bd18d.webp)

1. Selecione o endpoint que criou.

    ![Select endpoints.](../../../../../../translated_images/pt-PT/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Selecione **Consumir** no menu de navegação.

1. Copie o seu **REST endpoint** e **Chave primária**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pt-PT/copy-endpoint-key.0650c3786bd646ab.webp)

#### Adicionar a ligação personalizada

1. Visite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até ao projeto Microsoft Foundry que criou.

1. No projeto que criou, selecione **Definições** na aba do lado esquerdo.

1. Selecione **+ Nova ligação**.

    ![Select new connection.](../../../../../../translated_images/pt-PT/select-new-connection.fa0f35743758a74b.webp)

1. Selecione **Chaves personalizadas** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/pt-PT/select-custom-keys.5a3c6b25580a9b67.webp)

1. Execute as seguintes tarefas:

    - Selecione **+ Adicionar pares chave-valor**.
    - Para o nome da chave, introduza **endpoint** e cole o endpoint copiado do Azure ML Studio no campo do valor.
    - Selecione novamente **+ Adicionar pares chave-valor**.
    - Para o nome da chave, introduza **key** e cole a chave copiada do Azure ML Studio no campo do valor.
    - Após adicionar as chaves, selecione **é secreto** para evitar que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/pt-PT/add-connection.ac7f5faf8b10b0df.webp)

1. Selecione **Adicionar ligação**.

#### Criar Prompt flow

Adicionou uma ligação personalizada no Microsoft Foundry. Agora, vamos criar um Prompt flow usando os seguintes passos. Depois, irá ligar este Prompt flow à ligação personalizada para usar o modelo afinado dentro do Prompt flow.

1. Navegue até ao projeto Microsoft Foundry que criou.

1. Selecione **Prompt flow** na aba do lado esquerdo.

1. Selecione **+ Criar** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/pt-PT/select-promptflow.18ff2e61ab9173eb.webp)

1. Selecione **Fluxo de chat** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/pt-PT/select-flow-type.28375125ec9996d3.webp)

1. Introduza o **Nome da pasta** a utilizar.

    ![Select chat flow.](../../../../../../translated_images/pt-PT/enter-name.02ddf8fb840ad430.webp)

1. Selecione **Criar**.

#### Configurar Prompt flow para conversar com o seu modelo personalizado Phi-3 / Phi-3.5

Precisa de integrar o modelo afinado Phi-3 / Phi-3.5 num Prompt flow. No entanto, o Prompt flow existente fornecido não está desenhado para este propósito. Portanto, deve redesenhar o Prompt flow para permitir a integração do modelo personalizado.

1. No Prompt flow, execute as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Modo de ficheiro bruto**.
    - Apague todo o código existente no ficheiro *flow.dag.yml*.
    - Adicione o código seguinte ao *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/pt-PT/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Adicione o seguinte código a *integrate_with_promptflow.py* para usar o modelo personalizado Phi-3 / Phi-3.5 no Prompt flow.

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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/pt-PT/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Para informações mais detalhadas sobre como usar o Prompt flow no Microsoft Foundry, pode consultar [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Entrada do chat**, **Saída do chat** para ativar a conversa com o seu modelo.

    ![Select Input Output.](../../../../../../translated_images/pt-PT/select-input-output.c187fc58f25fbfc3.webp)

1. Agora está pronto para conversar com o seu modelo personalizado Phi-3 / Phi-3.5. No próximo exercício, irá aprender como iniciar o Prompt flow e usá-lo para conversar com o seu modelo afinado Phi-3 / Phi-3.5.

> [!NOTE]
>
> O fluxo reconstruído deverá parecer com a imagem abaixo:
>
> ![Flow example](../../../../../../translated_images/pt-PT/graph-example.82fd1bcdd3fc545b.webp)
>

#### Iniciar Prompt flow

1. Selecione **Iniciar sessões de computação** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pt-PT/start-compute-session.9acd8cbbd2c43df1.webp)

1. Selecione **Validar e analisar entrada** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/pt-PT/validate-input.c1adb9543c6495be.webp)

1. Selecione o **Valor** da **ligação** para a ligação personalizada que criou. Por exemplo, *connection*.

    ![Connection.](../../../../../../translated_images/pt-PT/select-connection.1f2b59222bcaafef.webp)

#### Conversar com o seu modelo personalizado Phi-3 / Phi-3.5

1. Selecione **Conversar**.

    ![Select chat.](../../../../../../translated_images/pt-PT/select-chat.0406bd9687d0c49d.webp)

1. Aqui está um exemplo dos resultados: Agora pode conversar com o seu modelo personalizado Phi-3 / Phi-3.5. Recomenda-se fazer perguntas baseadas nos dados usados para o afinamento.

    ![Chat with prompt flow.](../../../../../../translated_images/pt-PT/chat-with-promptflow.1cf8cea112359ada.webp)

### Implementar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5

Para avaliar o modelo Phi-3 / Phi-3.5 no Microsoft Foundry, precisa de implementar um modelo Azure OpenAI. Este modelo será usado para avaliar o desempenho do modelo Phi-3 / Phi-3.5.

#### Implementar Azure OpenAI

1. Inicie sessão em [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até ao projeto Microsoft Foundry que criou.

    ![Select Project.](../../../../../../translated_images/pt-PT/select-project-created.5221e0e403e2c9d6.webp)

1. No projeto que criou, selecione **Implementações** na aba do lado esquerdo.

1. Selecione **+ Implementar modelo** no menu de navegação.

1. Selecione **Implementar modelo base**.

    ![Select Deployments.](../../../../../../translated_images/pt-PT/deploy-openai-model.95d812346b25834b.webp)

1. Selecione o modelo Azure OpenAI que pretende usar. Por exemplo, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/pt-PT/select-openai-model.959496d7e311546d.webp)

1. Selecione **Confirmar**.

### Avaliar o modelo afinado Phi-3 / Phi-3.5 utilizando a avaliação Prompt flow do Microsoft Foundry

### Iniciar uma nova avaliação

1. Visite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até ao projeto Microsoft Foundry que criou.

    ![Select Project.](../../../../../../translated_images/pt-PT/select-project-created.5221e0e403e2c9d6.webp)

1. No projeto que criou, selecione **Avaliação** na aba do lado esquerdo.

1. Selecione **+ Nova avaliação** no menu de navegação.

    ![Select evaluation.](../../../../../../translated_images/pt-PT/select-evaluation.2846ad7aaaca7f4f.webp)

1. Selecione avaliação **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/pt-PT/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Execute as seguintes tarefas:

    - Introduza o nome da avaliação. Deve ser um valor único.
    - Selecione **Pergunta e resposta sem contexto** como tipo de tarefa. Porque o conjunto de dados **ULTRACHAT_200k** usado neste tutorial não contém contexto.
    - Selecione o prompt flow que deseja avaliar.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-PT/evaluation-setting1.4aa08259ff7a536e.webp)

1. Selecione **Seguinte**.

1. Execute as seguintes tarefas:

    - Selecione **Adicionar o seu conjunto de dados** para carregar o conjunto de dados. Por exemplo, pode carregar o ficheiro do conjunto de dados de teste, como *test_data.json1*, que está incluído ao baixar o conjunto de dados **ULTRACHAT_200k**.
    - Selecione a **Coluna do conjunto de dados** apropriada que corresponde ao seu conjunto de dados. Por exemplo, se estiver a usar o conjunto de dados **ULTRACHAT_200k**, selecione **${data.prompt}** como a coluna do conjunto de dados.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-PT/evaluation-setting2.07036831ba58d64e.webp)

1. Selecione **Seguinte**.

1. Execute as seguintes tarefas para configurar as métricas de performance e qualidade:

    - Selecione as métricas de performance e qualidade que deseja usar.
    - Selecione o modelo Azure OpenAI que criou para avaliação. Por exemplo, selecione **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-PT/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Execute as seguintes tarefas para configurar as métricas de risco e segurança:

    - Selecione as métricas de risco e segurança que deseja usar.
    - Selecione o limiar para calcular a taxa de defeitos que deseja usar. Por exemplo, selecione **Médio**.
    - Para **pergunta**, selecione **Fonte dos dados** para **{$data.prompt}**.
    - Para **resposta**, selecione **Fonte dos dados** para **{$run.outputs.answer}**.
    - Para **verdadeiro**, selecione **Fonte dos dados** para **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt-PT/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Selecione **Seguinte**.

1. Selecione **Submeter** para iniciar a avaliação.

1. A avaliação demorará algum tempo até ser concluída. Pode acompanhar o progresso na aba **Avaliação**.

### Rever os resultados da avaliação

> [!NOTE]
> Os resultados apresentados abaixo destinam-se a ilustrar o processo de avaliação. Neste tutorial, foi usado um modelo afinado num conjunto de dados relativamente pequeno, o que pode levar a resultados subótimos. Os resultados reais podem variar significativamente dependendo do tamanho, qualidade e diversidade do conjunto de dados usado, assim como da configuração específica do modelo.

Assim que a avaliação estiver concluída, pode rever os resultados para métricas de performance e segurança.
1. Métricas de desempenho e qualidade:

    - avaliar a eficácia do modelo na geração de respostas coerentes, fluentes e relevantes.

    ![Evaluation result.](../../../../../../translated_images/pt-PT/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Métricas de risco e segurança:

    - Garantir que as saídas do modelo são seguras e alinhadas com os Princípios de IA Responsável, evitando qualquer conteúdo prejudicial ou ofensivo.

    ![Evaluation result.](../../../../../../translated_images/pt-PT/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Pode deslocar-se para baixo para ver o **Resultado detalhado das métricas**.

    ![Evaluation result.](../../../../../../translated_images/pt-PT/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Ao avaliar o seu modelo personalizado Phi-3 / Phi-3.5 em relação às métricas de desempenho e segurança, pode confirmar que o modelo não é apenas eficaz, mas também cumpre as práticas de IA responsável, tornando-o pronto para implantação no mundo real.

## Parabéns!

### Terminou este tutorial

Avaliou com sucesso o modelo Phi-3 ajustado e integrado com Prompt flow no Microsoft Foundry. Este é um passo importante para garantir que os seus modelos de IA não apenas tenham um bom desempenho, mas também cumpram os princípios de IA Responsável da Microsoft, ajudando-o a construir aplicações de IA fiáveis e dignas de confiança.

![Architecture.](../../../../../../translated_images/pt-PT/architecture.10bec55250f5d6a4.webp)

## Limpar Recursos Azure

Limpe os seus recursos Azure para evitar encargos adicionais na sua conta. Aceda ao portal Azure e elimine os seguintes recursos:

- O recurso Azure Machine Learning.
- O endpoint do modelo Azure Machine Learning.
- O recurso Microsoft Foundry Project.
- O recurso Microsoft Foundry Prompt flow.

### Próximos passos

#### Documentação

- [Avaliar sistemas de IA utilizando o painel de IA Responsável](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de avaliação e monitorização para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentação Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentação Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conteúdos de Formação

- [Introdução à Abordagem de IA Responsável da Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introdução ao Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referência

- [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anúncio de novas ferramentas no Azure AI para ajudar a criar aplicações de IA generativa mais seguras e fiáveis](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela exactidão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informação crítica, é recomendada uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->