<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:34:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "br"
}
-->
# Avaliando o Modelo Phi-3 / Phi-3.5 Fine-tuned no Azure AI Foundry com Foco nos Princípios de IA Responsável da Microsoft

Este exemplo de ponta a ponta (E2E) é baseado no guia "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community.

## Visão Geral

### Como avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 fine-tuned no Azure AI Foundry?

O fine-tuning de um modelo pode, às vezes, levar a respostas indesejadas ou inesperadas. Para garantir que o modelo continue seguro e eficaz, é importante avaliar seu potencial para gerar conteúdo prejudicial e sua capacidade de produzir respostas precisas, relevantes e coerentes. Neste tutorial, você aprenderá como avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 fine-tuned integrado com Prompt flow no Azure AI Foundry.

Aqui está o processo de avaliação do Azure AI Foundry.

![Arquitetura do tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4.br.png)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para informações mais detalhadas e para explorar recursos adicionais sobre Phi-3 / Phi-3.5, visite o [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Pré-requisitos

- [Python](https://www.python.org/downloads)
- [Assinatura Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Phi-3 / Phi-3.5 fine-tuned

### Sumário

1. [**Cenário 1: Introdução à avaliação do Prompt flow do Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introdução à avaliação de segurança](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introdução à avaliação de desempenho](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Antes de começar](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Avaliar o modelo Phi-3 / Phi-3.5 fine-tuned usando a avaliação do Prompt flow do Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Parabéns!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Cenário 1: Introdução à avaliação do Prompt flow do Azure AI Foundry**

### Introdução à avaliação de segurança

Para garantir que seu modelo de IA seja ético e seguro, é fundamental avaliá-lo com base nos Princípios de IA Responsável da Microsoft. No Azure AI Foundry, as avaliações de segurança permitem analisar a vulnerabilidade do seu modelo a ataques de jailbreak e seu potencial para gerar conteúdo prejudicial, alinhando-se diretamente a esses princípios.

![Avaliação de segurança.](../../../../../../translated_images/safety-evaluation.083586ec88dfa950.br.png)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Princípios de IA Responsável da Microsoft

Antes de iniciar as etapas técnicas, é essencial compreender os Princípios de IA Responsável da Microsoft, uma estrutura ética criada para orientar o desenvolvimento, implantação e operação responsáveis de sistemas de IA. Esses princípios guiam o design, desenvolvimento e implantação responsáveis de sistemas de IA, garantindo que as tecnologias de IA sejam construídas de forma justa, transparente e inclusiva. Eles são a base para avaliar a segurança dos modelos de IA.

Os Princípios de IA Responsável da Microsoft incluem:

- **Justiça e Inclusividade**: Sistemas de IA devem tratar todos de forma justa e evitar impactar grupos semelhantes de pessoas de maneiras diferentes. Por exemplo, quando sistemas de IA fornecem orientações sobre tratamentos médicos, solicitações de empréstimos ou emprego, eles devem fazer as mesmas recomendações para todos que tenham sintomas, condições financeiras ou qualificações profissionais semelhantes.

- **Confiabilidade e Segurança**: Para construir confiança, é fundamental que os sistemas de IA operem de forma confiável, segura e consistente. Esses sistemas devem funcionar conforme projetado originalmente, responder de forma segura a condições inesperadas e resistir a manipulações prejudiciais. Seu comportamento e a variedade de condições que podem lidar refletem o conjunto de situações e circunstâncias previstas pelos desenvolvedores durante o design e testes.

- **Transparência**: Quando sistemas de IA ajudam a informar decisões que têm grande impacto na vida das pessoas, é fundamental que elas entendam como essas decisões foram tomadas. Por exemplo, um banco pode usar um sistema de IA para decidir se uma pessoa é confiável para crédito. Uma empresa pode usar um sistema de IA para determinar os candidatos mais qualificados para contratação.

- **Privacidade e Segurança**: À medida que a IA se torna mais presente, proteger a privacidade e garantir a segurança das informações pessoais e empresariais se torna mais importante e complexo. Com a IA, privacidade e segurança de dados exigem atenção especial, pois o acesso a dados é essencial para que os sistemas de IA façam previsões e decisões precisas e informadas sobre as pessoas.

- **Responsabilidade**: As pessoas que projetam e implantam sistemas de IA devem ser responsáveis pelo funcionamento desses sistemas. As organizações devem se basear em padrões da indústria para desenvolver normas de responsabilidade. Essas normas garantem que sistemas de IA não sejam a autoridade final em decisões que afetam a vida das pessoas e asseguram que humanos mantenham controle significativo sobre sistemas de IA altamente autônomos.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c.br.png)

*Fonte da imagem: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para saber mais sobre os Princípios de IA Responsável da Microsoft, visite [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de segurança

Neste tutorial, você avaliará a segurança do modelo Phi-3 fine-tuned usando as métricas de segurança do Azure AI Foundry. Essas métricas ajudam a analisar o potencial do modelo para gerar conteúdo prejudicial e sua vulnerabilidade a ataques de jailbreak. As métricas de segurança incluem:

- **Conteúdo relacionado a autoagressão**: Avalia se o modelo tende a produzir conteúdo relacionado a autoagressão.
- **Conteúdo odioso e injusto**: Avalia se o modelo tende a produzir conteúdo odioso ou injusto.
- **Conteúdo violento**: Avalia se o modelo tende a produzir conteúdo violento.
- **Conteúdo sexual**: Avalia se o modelo tende a produzir conteúdo sexual inapropriado.

Avaliar esses aspectos garante que o modelo de IA não produza conteúdo prejudicial ou ofensivo, alinhando-o aos valores sociais e às normas regulatórias.

![Avaliar com base na segurança.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07.br.png)

### Introdução à avaliação de desempenho

Para garantir que seu modelo de IA esteja performando conforme esperado, é importante avaliar seu desempenho com base em métricas específicas. No Azure AI Foundry, as avaliações de desempenho permitem analisar a eficácia do seu modelo em gerar respostas precisas, relevantes e coerentes.

![Avaliação de segurança.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740.br.png)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de desempenho

Neste tutorial, você avaliará o desempenho do modelo Phi-3 / Phi-3.5 fine-tuned usando as métricas de desempenho do Azure AI Foundry. Essas métricas ajudam a analisar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes. As métricas de desempenho incluem:

- **Fundamentação (Groundedness)**: Avalia o quanto as respostas geradas estão alinhadas com as informações da fonte de entrada.
- **Relevância**: Avalia a pertinência das respostas geradas em relação às perguntas feitas.
- **Coerência**: Avalia a fluidez do texto gerado, se ele lê naturalmente e se se assemelha a uma linguagem humana.
- **Fluência**: Avalia a proficiência linguística do texto gerado.
- **Similaridade GPT**: Compara a resposta gerada com a verdade de base para medir similaridade.
- **F1 Score**: Calcula a proporção de palavras compartilhadas entre a resposta gerada e os dados da fonte.

Essas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes.

![Avaliar com base no desempenho.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e8.br.png)

## **Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**

### Antes de começar

Este tutorial é uma continuação dos posts anteriores, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Nesses posts, mostramos o processo de fine-tuning de um modelo Phi-3 / Phi-3.5 no Azure AI Foundry e sua integração com Prompt flow.

Neste tutorial, você irá implantar um modelo Azure OpenAI como avaliador no Azure AI Foundry e usá-lo para avaliar seu modelo Phi-3 / Phi-3.5 fine-tuned.

Antes de começar este tutorial, certifique-se de ter os seguintes pré-requisitos, conforme descrito nos tutoriais anteriores:

1. Um conjunto de dados preparado para avaliar o modelo Phi-3 / Phi-3.5 fine-tuned.
1. Um modelo Phi-3 / Phi-3.5 que tenha sido fine-tuned e implantado no Azure Machine Learning.
1. Um Prompt flow integrado com seu modelo Phi-3 / Phi-3.5 fine-tuned no Azure AI Foundry.

> [!NOTE]
> Você usará o arquivo *test_data.jsonl*, localizado na pasta data do conjunto de dados **ULTRACHAT_200k** baixado nos posts anteriores, como o conjunto de dados para avaliar o modelo Phi-3 / Phi-3.5 fine-tuned.

#### Integrar o modelo customizado Phi-3 / Phi-3.5 com Prompt flow no Azure AI Foundry (abordagem Code first)
> [!NOTE]  
> Se você seguiu a abordagem low-code descrita em "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", pode pular este exercício e seguir para o próximo.  
> No entanto, se você seguiu a abordagem code-first descrita em "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para ajustar e implantar seu modelo Phi-3 / Phi-3.5, o processo de conectar seu modelo ao Prompt flow é um pouco diferente. Você vai aprender esse processo neste exercício.
Para prosseguir, você precisa integrar seu modelo Phi-3 / Phi-3.5 ajustado no Prompt flow no Azure AI Foundry.

#### Criar Azure AI Foundry Hub

Você precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo que você organize e gerencie vários Projetos dentro do Azure AI Foundry.

1. Faça login no [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecione **All hubs** na aba lateral esquerda.

1. Selecione **+ New hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1.br.png)

1. Realize as seguintes tarefas:

    - Insira o **Hub name**. Deve ser um valor único.
    - Selecione sua **Subscription** do Azure.
    - Selecione o **Resource group** a ser usado (crie um novo, se necessário).
    - Selecione a **Location** que deseja usar.
    - Selecione **Connect Azure AI Services** para usar (crie um novo, se necessário).
    - Selecione **Connect Azure AI Search** para **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e34.br.png)

1. Selecione **Next**.

#### Criar Projeto no Azure AI Foundry

1. No Hub que você criou, selecione **All projects** na aba lateral esquerda.

1. Selecione **+ New project** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a3.br.png)

1. Insira o **Project name**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e420.br.png)

1. Selecione **Create a project**.

#### Adicionar uma conexão personalizada para o modelo Phi-3 / Phi-3.5 ajustado

Para integrar seu modelo customizado Phi-3 / Phi-3.5 com o Prompt flow, você precisa salvar o endpoint e a chave do modelo em uma conexão personalizada. Essa configuração garante o acesso ao seu modelo customizado Phi-3 / Phi-3.5 no Prompt flow.

#### Definir a chave da API e o URI do endpoint do modelo Phi-3 / Phi-3.5 ajustado

1. Acesse o [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até o workspace do Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba lateral esquerda.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d.br.png)

1. Selecione o endpoint que você criou.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2e.br.png)

1. Selecione **Consume** no menu de navegação.

1. Copie seu **REST endpoint** e a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab.br.png)

#### Adicionar a Conexão Personalizada

1. Acesse o [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

1. No projeto que você criou, selecione **Settings** na aba lateral esquerda.

1. Selecione **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b.br.png)

1. Selecione **Custom keys** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67.br.png)

1. Realize as seguintes tarefas:

    - Selecione **+ Add key value pairs**.
    - Para o nome da chave, insira **endpoint** e cole o endpoint copiado do Azure ML Studio no campo de valor.
    - Selecione **+ Add key value pairs** novamente.
    - Para o nome da chave, insira **key** e cole a chave copiada do Azure ML Studio no campo de valor.
    - Após adicionar as chaves, selecione **is secret** para evitar que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0df.br.png)

1. Selecione **Add connection**.

#### Criar Prompt flow

Você adicionou uma conexão personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow seguindo os passos abaixo. Depois, você conectará esse Prompt flow à conexão personalizada para usar o modelo ajustado dentro do Prompt flow.

1. Navegue até o projeto Azure AI Foundry que você criou.

1. Selecione **Prompt flow** na aba lateral esquerda.

1. Selecione **+ Create** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb.br.png)

1. Selecione **Chat flow** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d3.br.png)

1. Insira o **Folder name** que deseja usar.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad430.br.png)

1. Selecione **Create**.

#### Configurar o Prompt flow para conversar com seu modelo Phi-3 / Phi-3.5 customizado

Você precisa integrar o modelo Phi-3 / Phi-3.5 ajustado em um Prompt flow. No entanto, o Prompt flow existente fornecido não foi projetado para esse propósito. Portanto, é necessário redesenhar o Prompt flow para permitir a integração do modelo customizado.

1. No Prompt flow, realize as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Raw file mode**.
    - Apague todo o código existente no arquivo *flow.dag.yml*.
    - Adicione o código abaixo no *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f53.br.png)

1. Adicione o código abaixo no arquivo *integrate_with_promptflow.py* para usar o modelo customizado Phi-3 / Phi-3.5 no Prompt flow.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec28.br.png)

> [!NOTE]
> Para informações mais detalhadas sobre o uso do Prompt flow no Azure AI Foundry, você pode consultar [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Chat input**, **Chat output** para habilitar a conversa com seu modelo.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc3.br.png)

1. Agora você está pronto para conversar com seu modelo customizado Phi-3 / Phi-3.5. No próximo exercício, você aprenderá como iniciar o Prompt flow e usá-lo para conversar com seu modelo Phi-3 / Phi-3.5 ajustado.

> [!NOTE]
>
> O fluxo reconstruído deve ficar parecido com a imagem abaixo:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545b.br.png)
>

#### Iniciar Prompt flow

1. Selecione **Start compute sessions** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df1.br.png)

1. Selecione **Validate and parse input** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be.br.png)

1. Selecione o **Value** da **connection** para a conexão personalizada que você criou. Por exemplo, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafef.br.png)

#### Conversar com seu modelo customizado Phi-3 / Phi-3.5

1. Selecione **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d.br.png)

1. Aqui está um exemplo dos resultados: agora você pode conversar com seu modelo customizado Phi-3 / Phi-3.5. Recomenda-se fazer perguntas baseadas nos dados usados para o fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada.br.png)

### Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5

Para avaliar o modelo Phi-3 / Phi-3.5 no Azure AI Foundry, você precisa implantar um modelo Azure OpenAI. Esse modelo será usado para avaliar o desempenho do modelo Phi-3 / Phi-3.5.

#### Implantar Azure OpenAI

1. Faça login no [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6.br.png)

1. No projeto que você criou, selecione **Deployments** na aba lateral esquerda.

1. Selecione **+ Deploy model** no menu de navegação.

1. Selecione **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b.br.png)

1. Selecione o modelo Azure OpenAI que deseja usar. Por exemplo, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d.br.png)

1. Selecione **Confirm**.

### Avaliar o modelo Phi-3 / Phi-3.5 ajustado usando a avaliação do Prompt flow do Azure AI Foundry

### Iniciar uma nova avaliação

1. Acesse o [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6.br.png)

1. No projeto que você criou, selecione **Evaluation** na aba lateral esquerda.

1. Selecione **+ New evaluation** no menu de navegação.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f.br.png)

1. Selecione a avaliação **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f.br.png)

1. Realize as seguintes tarefas:

    - Insira o nome da avaliação. Deve ser um valor único.
    - Selecione **Question and answer without context** como tipo de tarefa. Isso porque o conjunto de dados **ULTRACHAT_200k** usado neste tutorial não contém contexto.
    - Selecione o prompt flow que deseja avaliar.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e.br.png)

1. Selecione **Next**.

1. Realize as seguintes tarefas:

    - Selecione **Add your dataset** para enviar o conjunto de dados. Por exemplo, você pode enviar o arquivo de teste, como *test_data.json1*, que está incluído ao baixar o conjunto de dados **ULTRACHAT_200k**.
    - Selecione a **Dataset column** apropriada que corresponde ao seu conjunto de dados. Por exemplo, se estiver usando o conjunto **ULTRACHAT_200k**, selecione **${data.prompt}** como a coluna do conjunto de dados.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64e.br.png)

1. Selecione **Next**.

1. Realize as seguintes tarefas para configurar as métricas de desempenho e qualidade:

    - Selecione as métricas de desempenho e qualidade que deseja usar.
    - Selecione o modelo Azure OpenAI que você criou para avaliação. Por exemplo, selecione **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e.br.png)

1. Realize as seguintes tarefas para configurar as métricas de risco e segurança:

    - Selecione as métricas de risco e segurança que deseja usar.
    - Selecione o limite para calcular a taxa de defeitos que deseja usar. Por exemplo, selecione **Medium**.
    - Para **question**, selecione **Data source** para **{$data.prompt}**.
    - Para **answer**, selecione **Data source** para **{$run.outputs.answer}**.
    - Para **ground_truth**, selecione **Data source** para **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2.br.png)

1. Selecione **Next**.

1. Selecione **Submit** para iniciar a avaliação.

1. A avaliação levará algum tempo para ser concluída. Você pode acompanhar o progresso na aba **Evaluation**.

### Revisar os Resultados da Avaliação
> [!NOTE]
> Os resultados apresentados abaixo têm o objetivo de ilustrar o processo de avaliação. Neste tutorial, utilizamos um modelo ajustado com um conjunto de dados relativamente pequeno, o que pode levar a resultados abaixo do ideal. Os resultados reais podem variar significativamente dependendo do tamanho, qualidade e diversidade do conjunto de dados utilizado, assim como da configuração específica do modelo.
Após a conclusão da avaliação, você pode revisar os resultados tanto para métricas de desempenho quanto de segurança.

1. Métricas de desempenho e qualidade:

    - avalie a eficácia do modelo em gerar respostas coerentes, fluentes e relevantes.

    ![Resultado da avaliação.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb74254.br.png)

1. Métricas de risco e segurança:

    - Garanta que as saídas do modelo sejam seguras e estejam alinhadas com os Princípios de IA Responsável, evitando qualquer conteúdo prejudicial ou ofensivo.

    ![Resultado da avaliação.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0.br.png)

1. Você pode rolar a página para baixo para ver o **resultado detalhado das métricas**.

    ![Resultado da avaliação.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f17.br.png)

1. Ao avaliar seu modelo personalizado Phi-3 / Phi-3.5 com base nas métricas de desempenho e segurança, você pode confirmar que o modelo não é apenas eficaz, mas também segue práticas responsáveis de IA, tornando-o pronto para implantação no mundo real.

## Parabéns!

### Você concluiu este tutorial

Você avaliou com sucesso o modelo Phi-3 ajustado, integrado ao Prompt flow no Azure AI Foundry. Este é um passo importante para garantir que seus modelos de IA não apenas tenham bom desempenho, mas também estejam alinhados com os princípios de IA Responsável da Microsoft, ajudando você a construir aplicações de IA confiáveis e seguras.

![Arquitetura.](../../../../../../translated_images/architecture.10bec55250f5d6a4.br.png)

## Limpeza dos Recursos do Azure

Limpe seus recursos do Azure para evitar cobranças adicionais na sua conta. Acesse o portal do Azure e exclua os seguintes recursos:

- O recurso Azure Machine learning.
- O endpoint do modelo Azure Machine learning.
- O recurso do projeto Azure AI Foundry.
- O recurso Prompt flow do Azure AI Foundry.

### Próximos Passos

#### Documentação

- [Avalie sistemas de IA usando o painel Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de avaliação e monitoramento para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentação do Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conteúdo de Treinamento

- [Introdução à abordagem de IA Responsável da Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introdução ao Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referência

- [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anúncio de novas ferramentas no Azure AI para ajudar você a criar aplicações de IA generativa mais seguras e confiáveis](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.