<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:33:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "pt"
}
-->
# Avaliar o Modelo Phi-3 / Phi-3.5 Ajustado no Azure AI Foundry com Foco nos Princípios de IA Responsável da Microsoft

Este exemplo de ponta a ponta (E2E) baseia-se no guia "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community.

## Visão Geral

### Como pode avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 ajustado no Azure AI Foundry?

O ajuste fino de um modelo pode, por vezes, levar a respostas não intencionais ou indesejadas. Para garantir que o modelo se mantém seguro e eficaz, é importante avaliar o potencial do modelo para gerar conteúdo prejudicial e a sua capacidade de produzir respostas precisas, relevantes e coerentes. Neste tutorial, irá aprender como avaliar a segurança e o desempenho de um modelo Phi-3 / Phi-3.5 ajustado, integrado com Prompt flow no Azure AI Foundry.

Aqui está o processo de avaliação do Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/pt/architecture.10bec55250f5d6a4.webp)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para informações mais detalhadas e para explorar recursos adicionais sobre Phi-3 / Phi-3.5, visite o [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Pré-requisitos

- [Python](https://www.python.org/downloads)
- [Assinatura Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Phi-3 / Phi-3.5 ajustado

### Índice

1. [**Cenário 1: Introdução à avaliação do Prompt flow do Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introdução à avaliação de segurança](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introdução à avaliação de desempenho](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Cenário 2: Avaliar o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Antes de começar](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Avaliar o modelo Phi-3 / Phi-3.5 ajustado usando a avaliação do Prompt flow do Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Parabéns!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Cenário 1: Introdução à avaliação do Prompt flow do Azure AI Foundry**

### Introdução à avaliação de segurança

Para garantir que o seu modelo de IA é ético e seguro, é fundamental avaliá-lo com base nos Princípios de IA Responsável da Microsoft. No Azure AI Foundry, as avaliações de segurança permitem avaliar a vulnerabilidade do seu modelo a ataques de jailbreak e o seu potencial para gerar conteúdo prejudicial, alinhando-se diretamente com estes princípios.

![Safaty evaluation.](../../../../../../translated_images/pt/safety-evaluation.083586ec88dfa950.webp)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Princípios de IA Responsável da Microsoft

Antes de iniciar os passos técnicos, é essencial compreender os Princípios de IA Responsável da Microsoft, um quadro ético concebido para orientar o desenvolvimento, implementação e operação responsáveis de sistemas de IA. Estes princípios orientam o design, desenvolvimento e implementação responsáveis de sistemas de IA, garantindo que as tecnologias de IA são construídas de forma justa, transparente e inclusiva. Estes princípios são a base para avaliar a segurança dos modelos de IA.

Os Princípios de IA Responsável da Microsoft incluem:

- **Justiça e Inclusividade**: Os sistemas de IA devem tratar todos de forma justa e evitar afetar grupos semelhantes de pessoas de maneiras diferentes. Por exemplo, quando sistemas de IA fornecem orientações sobre tratamentos médicos, pedidos de empréstimo ou emprego, devem fazer as mesmas recomendações a todos que tenham sintomas, circunstâncias financeiras ou qualificações profissionais semelhantes.

- **Confiabilidade e Segurança**: Para construir confiança, é fundamental que os sistemas de IA operem de forma confiável, segura e consistente. Estes sistemas devem ser capazes de funcionar conforme foram originalmente concebidos, responder de forma segura a condições imprevistas e resistir a manipulações prejudiciais. O seu comportamento e a variedade de condições que conseguem gerir refletem o leque de situações e circunstâncias que os desenvolvedores anteciparam durante o design e testes.

- **Transparência**: Quando os sistemas de IA ajudam a informar decisões que têm um impacto enorme na vida das pessoas, é fundamental que as pessoas compreendam como essas decisões foram tomadas. Por exemplo, um banco pode usar um sistema de IA para decidir se uma pessoa é creditável. Uma empresa pode usar um sistema de IA para determinar os candidatos mais qualificados para contratar.

- **Privacidade e Segurança**: À medida que a IA se torna mais prevalente, proteger a privacidade e garantir a segurança da informação pessoal e empresarial torna-se cada vez mais importante e complexo. Com a IA, a privacidade e a segurança dos dados exigem atenção especial porque o acesso aos dados é essencial para que os sistemas de IA façam previsões e decisões precisas e informadas sobre as pessoas.

- **Responsabilização**: As pessoas que projetam e implementam sistemas de IA devem ser responsáveis pelo funcionamento dos seus sistemas. As organizações devem basear-se em normas da indústria para desenvolver normas de responsabilização. Estas normas podem garantir que os sistemas de IA não sejam a autoridade final em qualquer decisão que afete a vida das pessoas. Também podem garantir que os humanos mantenham controlo significativo sobre sistemas de IA altamente autónomos.

![Fill hub.](../../../../../../translated_images/pt/responsibleai2.c07ef430113fad8c.webp)

*Fonte da imagem: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para saber mais sobre os Princípios de IA Responsável da Microsoft, visite [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de segurança

Neste tutorial, irá avaliar a segurança do modelo Phi-3 ajustado usando as métricas de segurança do Azure AI Foundry. Estas métricas ajudam a avaliar o potencial do modelo para gerar conteúdo prejudicial e a sua vulnerabilidade a ataques de jailbreak. As métricas de segurança incluem:

- **Conteúdo relacionado com autoagressão**: Avalia se o modelo tem tendência a produzir conteúdo relacionado com autoagressão.
- **Conteúdo odioso e injusto**: Avalia se o modelo tem tendência a produzir conteúdo odioso ou injusto.
- **Conteúdo violento**: Avalia se o modelo tem tendência a produzir conteúdo violento.
- **Conteúdo sexual**: Avalia se o modelo tem tendência a produzir conteúdo sexual inapropriado.

Avaliar estes aspetos garante que o modelo de IA não produz conteúdo prejudicial ou ofensivo, alinhando-o com os valores sociais e normas regulatórias.

![Evaluate based on safety.](../../../../../../translated_images/pt/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introdução à avaliação de desempenho

Para garantir que o seu modelo de IA está a funcionar conforme esperado, é importante avaliar o seu desempenho com base em métricas de desempenho. No Azure AI Foundry, as avaliações de desempenho permitem avaliar a eficácia do seu modelo em gerar respostas precisas, relevantes e coerentes.

![Safaty evaluation.](../../../../../../translated_images/pt/performance-evaluation.48b3e7e01a098740.webp)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de desempenho

Neste tutorial, irá avaliar o desempenho do modelo Phi-3 / Phi-3.5 ajustado usando as métricas de desempenho do Azure AI Foundry. Estas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes. As métricas de desempenho incluem:

- **Fundamentação**: Avalia o quão bem as respostas geradas se alinham com a informação da fonte de entrada.
- **Relevância**: Avalia a pertinência das respostas geradas em relação às perguntas feitas.
- **Coerência**: Avalia a fluidez do texto gerado, se lê naturalmente e se se assemelha a uma linguagem humana.
- **Fluência**: Avalia a proficiência linguística do texto gerado.
- **Semelhança GPT**: Compara a resposta gerada com a verdade de base para medir a semelhança.
- **Pontuação F1**: Calcula a proporção de palavras partilhadas entre a resposta gerada e os dados da fonte.

Estas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes.

![Evaluate based on performance.](../../../../../../translated_images/pt/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Cenário 2: Avaliar o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**

### Antes de começar

Este tutorial é uma continuação dos posts anteriores, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Nestes posts, percorremos o processo de ajuste fino de um modelo Phi-3 / Phi-3.5 no Azure AI Foundry e a sua integração com Prompt flow.

Neste tutorial, irá implementar um modelo Azure OpenAI como avaliador no Azure AI Foundry e usá-lo para avaliar o seu modelo Phi-3 / Phi-3.5 ajustado.

Antes de começar este tutorial, certifique-se de que tem os seguintes pré-requisitos, conforme descrito nos tutoriais anteriores:

1. Um conjunto de dados preparado para avaliar o modelo Phi-3 / Phi-3.5 ajustado.
1. Um modelo Phi-3 / Phi-3.5 que tenha sido ajustado e implementado no Azure Machine Learning.
1. Um Prompt flow integrado com o seu modelo Phi-3 / Phi-3.5 ajustado no Azure AI Foundry.

> [!NOTE]
> Vai usar o ficheiro *test_data.jsonl*, localizado na pasta data do conjunto de dados **ULTRACHAT_200k** descarregado nos posts anteriores, como o conjunto de dados para avaliar o modelo Phi-3 / Phi-3.5 ajustado.

#### Integrar o modelo Phi-3 / Phi-3.5 personalizado com Prompt flow no Azure AI Foundry (Abordagem orientada a código)
> [!NOTE]  
> Se seguiu a abordagem low-code descrita em "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", pode saltar este exercício e avançar para o seguinte.  
> No entanto, se seguiu a abordagem code-first descrita em "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para afinar e implementar o seu modelo Phi-3 / Phi-3.5, o processo de ligação do seu modelo ao Prompt flow é ligeiramente diferente. Vai aprender este processo neste exercício.
Para avançar, precisa de integrar o seu modelo Phi-3 / Phi-3.5 afinado no Prompt flow no Azure AI Foundry.

#### Criar Azure AI Foundry Hub

É necessário criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo-lhe organizar e gerir vários Projetos dentro do Azure AI Foundry.

1. Inicie sessão em [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecione **All hubs** no separador do lado esquerdo.

1. Selecione **+ New hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/pt/create-hub.5be78fb1e21ffbf1.webp)

1. Execute as seguintes tarefas:

    - Introduza o **Hub name**. Deve ser um valor único.
    - Selecione a sua **Subscription** Azure.
    - Selecione o **Resource group** a utilizar (crie um novo se necessário).
    - Selecione a **Location** que pretende usar.
    - Selecione **Connect Azure AI Services** a utilizar (crie um novo se necessário).
    - Selecione **Connect Azure AI Search** para **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/pt/fill-hub.baaa108495c71e34.webp)

1. Selecione **Next**.

#### Criar Projeto Azure AI Foundry

1. No Hub que criou, selecione **All projects** no separador do lado esquerdo.

1. Selecione **+ New project** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/pt/select-new-project.cd31c0404088d7a3.webp)

1. Introduza o **Project name**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/pt/create-project.ca3b71298b90e420.webp)

1. Selecione **Create a project**.

#### Adicionar uma ligação personalizada para o modelo Phi-3 / Phi-3.5 afinado

Para integrar o seu modelo personalizado Phi-3 / Phi-3.5 com o Prompt flow, precisa de guardar o endpoint e a chave do modelo numa ligação personalizada. Esta configuração garante o acesso ao seu modelo personalizado Phi-3 / Phi-3.5 no Prompt flow.

#### Definir a chave api e o endpoint uri do modelo Phi-3 / Phi-3.5 afinado

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até ao workspace Azure Machine Learning que criou.

1. Selecione **Endpoints** no separador do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/pt/select-endpoints.ee7387ecd68bd18d.webp)

1. Selecione o endpoint que criou.

    ![Select endpoints.](../../../../../../translated_images/pt/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Selecione **Consume** no menu de navegação.

1. Copie o seu **REST endpoint** e a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pt/copy-endpoint-key.0650c3786bd646ab.webp)

#### Adicionar a Ligação Personalizada

1. Visite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até ao projeto Azure AI Foundry que criou.

1. No Projeto que criou, selecione **Settings** no separador do lado esquerdo.

1. Selecione **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/pt/select-new-connection.fa0f35743758a74b.webp)

1. Selecione **Custom keys** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/pt/select-custom-keys.5a3c6b25580a9b67.webp)

1. Execute as seguintes tarefas:

    - Selecione **+ Add key value pairs**.
    - Para o nome da chave, introduza **endpoint** e cole o endpoint que copiou do Azure ML Studio no campo de valor.
    - Selecione novamente **+ Add key value pairs**.
    - Para o nome da chave, introduza **key** e cole a chave que copiou do Azure ML Studio no campo de valor.
    - Depois de adicionar as chaves, selecione **is secret** para evitar que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/pt/add-connection.ac7f5faf8b10b0df.webp)

1. Selecione **Add connection**.

#### Criar Prompt flow

Adicionou uma ligação personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow seguindo os passos abaixo. Depois, irá ligar este Prompt flow à ligação personalizada para usar o modelo afinado dentro do Prompt flow.

1. Navegue até ao projeto Azure AI Foundry que criou.

1. Selecione **Prompt flow** no separador do lado esquerdo.

1. Selecione **+ Create** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/pt/select-promptflow.18ff2e61ab9173eb.webp)

1. Selecione **Chat flow** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/pt/select-flow-type.28375125ec9996d3.webp)

1. Introduza o **Folder name** a utilizar.

    ![Select chat flow.](../../../../../../translated_images/pt/enter-name.02ddf8fb840ad430.webp)

1. Selecione **Create**.

#### Configurar o Prompt flow para conversar com o seu modelo Phi-3 / Phi-3.5 personalizado

Precisa de integrar o modelo Phi-3 / Phi-3.5 afinado num Prompt flow. Contudo, o Prompt flow existente fornecido não está desenhado para este propósito. Por isso, deve redesenhar o Prompt flow para permitir a integração do modelo personalizado.

1. No Prompt flow, execute as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Raw file mode**.
    - Apague todo o código existente no ficheiro *flow.dag.yml*.
    - Adicione o seguinte código ao *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/pt/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Adicione o seguinte código ao *integrate_with_promptflow.py* para usar o modelo personalizado Phi-3 / Phi-3.5 no Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/pt/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Para informações mais detalhadas sobre como usar o Prompt flow no Azure AI Foundry, pode consultar [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Chat input**, **Chat output** para ativar a conversa com o seu modelo.

    ![Select Input Output.](../../../../../../translated_images/pt/select-input-output.c187fc58f25fbfc3.webp)

1. Agora está pronto para conversar com o seu modelo personalizado Phi-3 / Phi-3.5. No próximo exercício, irá aprender como iniciar o Prompt flow e usá-lo para conversar com o seu modelo afinado Phi-3 / Phi-3.5.

> [!NOTE]
>
> O fluxo reconstruído deverá parecer com a imagem abaixo:
>
> ![Flow example](../../../../../../translated_images/pt/graph-example.82fd1bcdd3fc545b.webp)
>

#### Iniciar Prompt flow

1. Selecione **Start compute sessions** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pt/start-compute-session.9acd8cbbd2c43df1.webp)

1. Selecione **Validate and parse input** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/pt/validate-input.c1adb9543c6495be.webp)

1. Selecione o **Value** da **connection** para a ligação personalizada que criou. Por exemplo, *connection*.

    ![Connection.](../../../../../../translated_images/pt/select-connection.1f2b59222bcaafef.webp)

#### Conversar com o seu modelo personalizado Phi-3 / Phi-3.5

1. Selecione **Chat**.

    ![Select chat.](../../../../../../translated_images/pt/select-chat.0406bd9687d0c49d.webp)

1. Aqui está um exemplo dos resultados: Agora pode conversar com o seu modelo personalizado Phi-3 / Phi-3.5. Recomenda-se que faça perguntas baseadas nos dados usados para o fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/pt/chat-with-promptflow.1cf8cea112359ada.webp)

### Implementar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5

Para avaliar o modelo Phi-3 / Phi-3.5 no Azure AI Foundry, precisa de implementar um modelo Azure OpenAI. Este modelo será usado para avaliar o desempenho do modelo Phi-3 / Phi-3.5.

#### Implementar Azure OpenAI

1. Inicie sessão em [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até ao projeto Azure AI Foundry que criou.

    ![Select Project.](../../../../../../translated_images/pt/select-project-created.5221e0e403e2c9d6.webp)

1. No Projeto que criou, selecione **Deployments** no separador do lado esquerdo.

1. Selecione **+ Deploy model** no menu de navegação.

1. Selecione **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/pt/deploy-openai-model.95d812346b25834b.webp)

1. Selecione o modelo Azure OpenAI que pretende usar. Por exemplo, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/pt/select-openai-model.959496d7e311546d.webp)

1. Selecione **Confirm**.

### Avaliar o modelo Phi-3 / Phi-3.5 afinado usando a avaliação Prompt flow do Azure AI Foundry

### Iniciar uma nova avaliação

1. Visite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até ao projeto Azure AI Foundry que criou.

    ![Select Project.](../../../../../../translated_images/pt/select-project-created.5221e0e403e2c9d6.webp)

1. No Projeto que criou, selecione **Evaluation** no separador do lado esquerdo.

1. Selecione **+ New evaluation** no menu de navegação.

    ![Select evaluation.](../../../../../../translated_images/pt/select-evaluation.2846ad7aaaca7f4f.webp)

1. Selecione a avaliação **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/pt/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Execute as seguintes tarefas:

    - Introduza o nome da avaliação. Deve ser um valor único.
    - Selecione **Question and answer without context** como tipo de tarefa. Porque o conjunto de dados **UlTRACHAT_200k** usado neste tutorial não contém contexto.
    - Selecione o prompt flow que pretende avaliar.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt/evaluation-setting1.4aa08259ff7a536e.webp)

1. Selecione **Next**.

1. Execute as seguintes tarefas:

    - Selecione **Add your dataset** para carregar o conjunto de dados. Por exemplo, pode carregar o ficheiro do conjunto de dados de teste, como *test_data.json1*, que está incluído quando descarrega o conjunto de dados **ULTRACHAT_200k**.
    - Selecione a **Dataset column** apropriada que corresponda ao seu conjunto de dados. Por exemplo, se estiver a usar o conjunto de dados **ULTRACHAT_200k**, selecione **${data.prompt}** como a coluna do conjunto de dados.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt/evaluation-setting2.07036831ba58d64e.webp)

1. Selecione **Next**.

1. Execute as seguintes tarefas para configurar as métricas de desempenho e qualidade:

    - Selecione as métricas de desempenho e qualidade que pretende usar.
    - Selecione o modelo Azure OpenAI que criou para avaliação. Por exemplo, selecione **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Execute as seguintes tarefas para configurar as métricas de risco e segurança:

    - Selecione as métricas de risco e segurança que pretende usar.
    - Selecione o limiar para calcular a taxa de defeitos que pretende usar. Por exemplo, selecione **Medium**.
    - Para **question**, selecione **Data source** para **{$data.prompt}**.
    - Para **answer**, selecione **Data source** para **{$run.outputs.answer}**.
    - Para **ground_truth**, selecione **Data source** para **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pt/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Selecione **Next**.

1. Selecione **Submit** para iniciar a avaliação.

1. A avaliação demorará algum tempo a ser concluída. Pode acompanhar o progresso no separador **Evaluation**.

### Rever os Resultados da Avaliação
> [!NOTE]
> Os resultados apresentados abaixo destinam-se a ilustrar o processo de avaliação. Neste tutorial, utilizámos um modelo ajustado com um conjunto de dados relativamente pequeno, o que pode levar a resultados subótimos. Os resultados reais podem variar significativamente dependendo do tamanho, qualidade e diversidade do conjunto de dados utilizado, bem como da configuração específica do modelo.
Depois de concluída a avaliação, pode rever os resultados tanto para os indicadores de desempenho como para os de segurança.

1. Indicadores de desempenho e qualidade:

    - avalie a eficácia do modelo na geração de respostas coerentes, fluentes e relevantes.

    ![Resultado da avaliação.](../../../../../../translated_images/pt/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Indicadores de risco e segurança:

    - Garanta que as respostas do modelo são seguras e estão alinhadas com os Princípios de IA Responsável, evitando qualquer conteúdo prejudicial ou ofensivo.

    ![Resultado da avaliação.](../../../../../../translated_images/pt/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Pode descer a página para ver o **resultado detalhado dos indicadores**.

    ![Resultado da avaliação.](../../../../../../translated_images/pt/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Ao avaliar o seu modelo personalizado Phi-3 / Phi-3.5 com base nos indicadores de desempenho e segurança, pode confirmar que o modelo não só é eficaz, como também cumpre as práticas de IA responsável, estando pronto para ser implementado no mundo real.

## Parabéns!

### Concluiu este tutorial

Avaliou com sucesso o modelo Phi-3 ajustado, integrado com Prompt flow no Azure AI Foundry. Este é um passo importante para garantir que os seus modelos de IA não só têm um bom desempenho, como também respeitam os princípios de IA Responsável da Microsoft, ajudando-o a criar aplicações de IA fiáveis e de confiança.

![Arquitetura.](../../../../../../translated_images/pt/architecture.10bec55250f5d6a4.webp)

## Limpar Recursos do Azure

Limpe os seus recursos do Azure para evitar custos adicionais na sua conta. Aceda ao portal do Azure e elimine os seguintes recursos:

- O recurso Azure Machine learning.
- O endpoint do modelo Azure Machine learning.
- O recurso do projeto Azure AI Foundry.
- O recurso Prompt flow do Azure AI Foundry.

### Próximos Passos

#### Documentação

- [Avaliar sistemas de IA usando o dashboard Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de avaliação e monitorização para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentação do Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conteúdos de Formação

- [Introdução à abordagem de IA Responsável da Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introdução ao Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referência

- [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anúncio de novas ferramentas no Azure AI para ajudar a criar aplicações de IA generativa mais seguras e fiáveis](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.