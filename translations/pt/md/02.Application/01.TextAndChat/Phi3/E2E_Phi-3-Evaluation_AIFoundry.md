<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:18:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "pt"
}
-->
# Avaliar o Modelo Fine-tuned Phi-3 / Phi-3.5 no Azure AI Foundry com Foco nos Princípios de IA Responsável da Microsoft

Este exemplo de ponta a ponta (E2E) é baseado no guia "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" da Microsoft Tech Community.

## Visão Geral

### Como avaliar a segurança e o desempenho de um modelo fine-tuned Phi-3 / Phi-3.5 no Azure AI Foundry?

O fine-tuning de um modelo pode, às vezes, levar a respostas não intencionais ou indesejadas. Para garantir que o modelo continue seguro e eficaz, é importante avaliar seu potencial para gerar conteúdo prejudicial e sua capacidade de produzir respostas precisas, relevantes e coerentes. Neste tutorial, você aprenderá como avaliar a segurança e o desempenho de um modelo fine-tuned Phi-3 / Phi-3.5 integrado ao Prompt flow no Azure AI Foundry.

Aqui está o processo de avaliação do Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pt.png)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para informações mais detalhadas e para explorar recursos adicionais sobre Phi-3 / Phi-3.5, visite o [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Pré-requisitos

- [Python](https://www.python.org/downloads)
- [Assinatura Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo fine-tuned Phi-3 / Phi-3.5

### Sumário

1. [**Cenário 1: Introdução à avaliação do Prompt flow do Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introdução à avaliação de segurança](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introdução à avaliação de desempenho](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Antes de começar](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Avaliar o modelo fine-tuned Phi-3 / Phi-3.5 usando a avaliação do Prompt flow do Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Parabéns!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Cenário 1: Introdução à avaliação do Prompt flow do Azure AI Foundry**

### Introdução à avaliação de segurança

Para garantir que seu modelo de IA seja ético e seguro, é fundamental avaliá-lo com base nos Princípios de IA Responsável da Microsoft. No Azure AI Foundry, as avaliações de segurança permitem verificar a vulnerabilidade do seu modelo a ataques de jailbreak e seu potencial para gerar conteúdo prejudicial, alinhando-se diretamente a esses princípios.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.pt.png)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Princípios de IA Responsável da Microsoft

Antes de iniciar as etapas técnicas, é essencial compreender os Princípios de IA Responsável da Microsoft, um marco ético criado para orientar o desenvolvimento, implantação e operação responsáveis de sistemas de IA. Esses princípios guiam o design, desenvolvimento e implantação responsáveis de sistemas de IA, garantindo que as tecnologias sejam construídas de maneira justa, transparente e inclusiva. Eles são a base para avaliar a segurança dos modelos de IA.

Os Princípios de IA Responsável da Microsoft incluem:

- **Justiça e Inclusão**: Sistemas de IA devem tratar todos de forma justa e evitar afetar grupos semelhantes de pessoas de maneiras diferentes. Por exemplo, quando sistemas de IA oferecem orientações sobre tratamento médico, pedidos de empréstimo ou emprego, eles devem fazer as mesmas recomendações para todos que tenham sintomas, condições financeiras ou qualificações profissionais semelhantes.

- **Confiabilidade e Segurança**: Para construir confiança, é fundamental que os sistemas de IA operem de forma confiável, segura e consistente. Esses sistemas devem funcionar conforme projetado originalmente, responder com segurança a condições inesperadas e resistir a manipulações prejudiciais. O comportamento deles e a variedade de condições que conseguem lidar refletem as situações e circunstâncias previstas pelos desenvolvedores durante o design e os testes.

- **Transparência**: Quando sistemas de IA ajudam a informar decisões que têm grande impacto na vida das pessoas, é fundamental que elas entendam como essas decisões foram tomadas. Por exemplo, um banco pode usar um sistema de IA para decidir se uma pessoa é creditável. Uma empresa pode usar um sistema de IA para determinar os candidatos mais qualificados para contratação.

- **Privacidade e Segurança**: Com o aumento do uso da IA, proteger a privacidade e garantir a segurança das informações pessoais e empresariais torna-se cada vez mais importante e complexo. Com a IA, privacidade e segurança de dados exigem atenção especial porque o acesso a dados é essencial para que os sistemas de IA façam previsões e decisões precisas e informadas sobre as pessoas.

- **Responsabilidade**: As pessoas que projetam e implantam sistemas de IA devem ser responsáveis pelo funcionamento desses sistemas. As organizações devem seguir padrões do setor para desenvolver normas de responsabilidade. Essas normas garantem que os sistemas de IA não sejam a autoridade final em qualquer decisão que afete a vida das pessoas. Também asseguram que humanos mantenham controle significativo sobre sistemas de IA altamente autônomos.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.pt.png)

*Fonte da imagem: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para saber mais sobre os Princípios de IA Responsável da Microsoft, visite [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de segurança

Neste tutorial, você avaliará a segurança do modelo fine-tuned Phi-3 usando as métricas de segurança do Azure AI Foundry. Essas métricas ajudam a analisar o potencial do modelo para gerar conteúdo prejudicial e sua vulnerabilidade a ataques de jailbreak. As métricas de segurança incluem:

- **Conteúdo relacionado a autoagressão**: Avalia se o modelo tem tendência a produzir conteúdo relacionado a autoagressão.
- **Conteúdo odioso e injusto**: Avalia se o modelo tende a gerar conteúdo odioso ou injusto.
- **Conteúdo violento**: Avalia se o modelo tende a produzir conteúdo violento.
- **Conteúdo sexual**: Avalia se o modelo tende a produzir conteúdo sexual inapropriado.

Avaliar esses aspectos garante que o modelo de IA não produza conteúdo prejudicial ou ofensivo, alinhando-o com valores sociais e normas regulatórias.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.pt.png)

### Introdução à avaliação de desempenho

Para garantir que seu modelo de IA esteja funcionando conforme esperado, é importante avaliar seu desempenho com base em métricas específicas. No Azure AI Foundry, as avaliações de desempenho permitem medir a eficácia do seu modelo na geração de respostas precisas, relevantes e coerentes.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.pt.png)

*Fonte da imagem: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de desempenho

Neste tutorial, você avaliará o desempenho do modelo fine-tuned Phi-3 / Phi-3.5 usando as métricas de desempenho do Azure AI Foundry. Essas métricas ajudam a medir a eficácia do modelo na geração de respostas precisas, relevantes e coerentes. As métricas de desempenho incluem:

- **Groundedness**: Avalia o quanto as respostas geradas estão alinhadas com as informações da fonte de entrada.
- **Relevância**: Avalia a pertinência das respostas geradas em relação às perguntas feitas.
- **Coerência**: Avalia a fluidez do texto gerado, sua naturalidade e semelhança com a linguagem humana.
- **Fluência**: Avalia a proficiência linguística do texto gerado.
- **Similaridade GPT**: Compara a resposta gerada com a verdade de base para medir similaridade.
- **F1 Score**: Calcula a proporção de palavras compartilhadas entre a resposta gerada e os dados da fonte.

Essas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.pt.png)

## **Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**

### Antes de começar

Este tutorial é uma continuação dos posts anteriores, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Nesses posts, mostramos o processo de fine-tuning de um modelo Phi-3 / Phi-3.5 no Azure AI Foundry e sua integração com o Prompt flow.

Neste tutorial, você vai implantar um modelo Azure OpenAI como avaliador no Azure AI Foundry e usá-lo para avaliar seu modelo fine-tuned Phi-3 / Phi-3.5.

Antes de começar este tutorial, certifique-se de que você possui os seguintes pré-requisitos, conforme descrito nos tutoriais anteriores:

1. Um conjunto de dados preparado para avaliar o modelo fine-tuned Phi-3 / Phi-3.5.
1. Um modelo Phi-3 / Phi-3.5 que foi fine-tuned e implantado no Azure Machine Learning.
1. Um Prompt flow integrado ao seu modelo fine-tuned Phi-3 / Phi-3.5 no Azure AI Foundry.

> [!NOTE]
> Você usará o arquivo *test_data.jsonl*, localizado na pasta data do conjunto de dados **ULTRACHAT_200k** baixado nos posts anteriores, como conjunto de dados para avaliar o modelo fine-tuned Phi-3 / Phi-3.5.

#### Integrar o modelo customizado Phi-3 / Phi-3.5 com Prompt flow no Azure AI Foundry (abordagem code first)

> [!NOTE]
> Se você seguiu a abordagem low-code descrita em "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", pode pular este exercício e seguir para o próximo.
> Contudo, se você seguiu a abordagem code-first descrita em "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para fine-tuning e implantação do seu modelo Phi-3 / Phi-3.5, o processo de conexão do seu modelo ao Prompt flow é um pouco diferente. Você aprenderá esse processo neste exercício.

Para prosseguir, é necessário integrar seu modelo fine-tuned Phi-3 / Phi-3.5 ao Prompt flow no Azure AI Foundry.

#### Criar Azure AI Foundry Hub

Você precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo organizar e gerenciar vários Projetos dentro do Azure AI Foundry.

1. Faça login no [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecione **All hubs** na aba do lado esquerdo.

1. Selecione **+ New hub** no menu de navegação.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.pt.png)

1. Realize as seguintes tarefas:

    - Insira o **Hub name**. Deve ser um valor único.
    - Selecione sua **Subscription** do Azure.
    - Selecione o **Resource group** a ser usado (crie um novo, se necessário).
    - Selecione a **Location** que deseja usar.
    - Selecione **Connect Azure AI Services** para usar (crie um novo, se necessário).
    - Selecione **Connect Azure AI Search** para **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.pt.png)

1. Selecione **Next**.

#### Criar Projeto Azure AI Foundry

1. No Hub que você criou, selecione **All projects** na aba do lado esquerdo.

1. Selecione **+ New project** no menu de navegação.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.pt.png)

1. Insira o **Project name**. Deve ser um valor único.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.pt.png)

1. Selecione **Create a project**.

#### Adicionar uma conexão personalizada para o modelo fine-tuned Phi-3 / Phi-3.5

Para integrar seu modelo customizado Phi-3 / Phi-3.5 com o Prompt flow, você precisa salvar o endpoint e a chave do modelo em uma conexão personalizada. Essa configuração garante o acesso ao seu modelo Phi-3 / Phi-3.5 customizado no Prompt flow.

#### Definir a chave da API e o endpoint URI do modelo fine-tuned Phi-3 / Phi-3.5

1. Acesse [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até o workspace Azure Machine learning que você criou.

1. Selecione **Endpoints** na aba do lado esquerdo.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.pt.png)

1. Selecione o endpoint que você criou.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.pt.png)

1. Selecione **Consume** no menu de navegação.

1. Copie seu **REST endpoint** e a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.pt.png)

#### Adicionar a Conexão Personalizada

1. Acesse [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

1. No projeto que você criou, selecione **Settings** na aba do lado esquerdo.

1. Selecione **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.pt.png)

1. Selecione **Custom keys** no menu de navegação.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.pt.png)

1. Realize as seguintes ações:

    - Selecione **+ Add key value pairs**.
    - Para o nome da chave, insira **endpoint** e cole o endpoint copiado do Azure ML Studio no campo de valor.
    - Selecione **+ Add key value pairs** novamente.
    - Para o nome da chave, insira **key** e cole a chave copiada do Azure ML Studio no campo de valor.
    - Após adicionar as chaves, selecione **is secret** para evitar que a chave seja exposta.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.pt.png)

1. Selecione **Add connection**.

#### Criar Prompt flow

Você adicionou uma conexão personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow seguindo os passos abaixo. Depois, você conectará esse Prompt flow à conexão personalizada para usar o modelo fine-tuned dentro do Prompt flow.

1. Navegue até o projeto Azure AI Foundry que você criou.

1. Selecione **Prompt flow** na aba do lado esquerdo.

1. Selecione **+ Create** no menu de navegação.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.pt.png)

1. Selecione **Chat flow** no menu de navegação.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.pt.png)

1. Insira o **Folder name** que deseja usar.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.pt.png)

1. Selecione **Create**.

#### Configurar Prompt flow para conversar com seu modelo customizado Phi-3 / Phi-3.5

Você precisa integrar o modelo fine-tuned Phi-3 / Phi-3.5 em um Prompt flow. No entanto, o Prompt flow existente não foi projetado para esse propósito. Portanto, é necessário redesenhar o Prompt flow para permitir a integração do modelo customizado.

1. No Prompt flow, realize as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Raw file mode**.
    - Apague todo o código existente no arquivo *flow.dag.yml*.
    - Adicione o seguinte código no *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.pt.png)

1. Adicione o seguinte código em *integrate_with_promptflow.py* para usar o modelo customizado Phi-3 / Phi-3.5 no Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.pt.png)

> [!NOTE]
> Para informações mais detalhadas sobre como usar o Prompt flow no Azure AI Foundry, consulte [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Chat input**, **Chat output** para habilitar a conversa com seu modelo.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.pt.png)

1. Agora você está pronto para conversar com seu modelo customizado Phi-3 / Phi-3.5. No próximo exercício, você aprenderá como iniciar o Prompt flow e usá-lo para conversar com seu modelo fine-tuned Phi-3 / Phi-3.5.

> [!NOTE]
>
> O fluxo reconstruído deve ficar parecido com a imagem abaixo:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.pt.png)
>

#### Iniciar Prompt flow

1. Selecione **Start compute sessions** para iniciar o Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.pt.png)

1. Selecione **Validate and parse input** para renovar os parâmetros.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.pt.png)

1. Selecione o **Value** da **connection** para a conexão personalizada que você criou. Por exemplo, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.pt.png)

#### Conversar com seu modelo customizado Phi-3 / Phi-3.5

1. Selecione **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.pt.png)

1. Aqui está um exemplo dos resultados: agora você pode conversar com seu modelo customizado Phi-3 / Phi-3.5. Recomenda-se fazer perguntas baseadas nos dados usados para o fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.pt.png)

### Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5

Para avaliar o modelo Phi-3 / Phi-3.5 no Azure AI Foundry, você precisa implantar um modelo Azure OpenAI. Esse modelo será usado para avaliar o desempenho do modelo Phi-3 / Phi-3.5.

#### Implantar Azure OpenAI

1. Faça login em [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pt.png)

1. No projeto que você criou, selecione **Deployments** na aba do lado esquerdo.

1. Selecione **+ Deploy model** no menu de navegação.

1. Selecione **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.pt.png)

1. Selecione o modelo Azure OpenAI que deseja usar. Por exemplo, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.pt.png)

1. Selecione **Confirm**.

### Avaliar o modelo fine-tuned Phi-3 / Phi-3.5 usando a avaliação do Prompt flow do Azure AI Foundry

### Iniciar uma nova avaliação

1. Acesse [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pt.png)

1. No projeto que você criou, selecione **Evaluation** na aba do lado esquerdo.

1. Selecione **+ New evaluation** no menu de navegação.
![Selecione a avaliação.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.pt.png)

1. Selecione a avaliação **Prompt flow**.

    ![Selecione a avaliação Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.pt.png)

1. execute as seguintes tarefas:

    - Insira o nome da avaliação. Deve ser um valor único.
    - Selecione **Question and answer without context** como o tipo de tarefa. Porque o conjunto de dados **UlTRACHAT_200k** usado neste tutorial não contém contexto.
    - Selecione o prompt flow que você deseja avaliar.

    ![Avaliação do prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.pt.png)

1. Selecione **Next**.

1. execute as seguintes tarefas:

    - Selecione **Add your dataset** para fazer o upload do conjunto de dados. Por exemplo, você pode enviar o arquivo do conjunto de dados de teste, como *test_data.json1*, que está incluído quando você baixa o conjunto de dados **ULTRACHAT_200k**.
    - Selecione a **Dataset column** apropriada que corresponde ao seu conjunto de dados. Por exemplo, se estiver usando o conjunto de dados **ULTRACHAT_200k**, selecione **${data.prompt}** como a coluna do conjunto de dados.

    ![Avaliação do prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.pt.png)

1. Selecione **Next**.

1. execute as seguintes tarefas para configurar as métricas de desempenho e qualidade:

    - Selecione as métricas de desempenho e qualidade que deseja usar.
    - Selecione o modelo Azure OpenAI que você criou para avaliação. Por exemplo, selecione **gpt-4o**.

    ![Avaliação do prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.pt.png)

1. execute as seguintes tarefas para configurar as métricas de risco e segurança:

    - Selecione as métricas de risco e segurança que deseja usar.
    - Selecione o limite para calcular a taxa de defeitos que deseja usar. Por exemplo, selecione **Medium**.
    - Para **question**, selecione **Data source** para **{$data.prompt}**.
    - Para **answer**, selecione **Data source** para **{$run.outputs.answer}**.
    - Para **ground_truth**, selecione **Data source** para **{$data.message}**.

    ![Avaliação do prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.pt.png)

1. Selecione **Next**.

1. Selecione **Submit** para iniciar a avaliação.

1. A avaliação levará algum tempo para ser concluída. Você pode acompanhar o progresso na aba **Evaluation**.

### Revise os Resultados da Avaliação

> [!NOTE]
> Os resultados apresentados abaixo têm o objetivo de ilustrar o processo de avaliação. Neste tutorial, usamos um modelo ajustado com um conjunto de dados relativamente pequeno, o que pode levar a resultados subótimos. Os resultados reais podem variar significativamente dependendo do tamanho, qualidade e diversidade do conjunto de dados usado, assim como da configuração específica do modelo.

Após a conclusão da avaliação, você pode revisar os resultados tanto das métricas de desempenho quanto das de segurança.

1. Métricas de desempenho e qualidade:

    - avalie a eficácia do modelo em gerar respostas coerentes, fluentes e relevantes.

    ![Resultado da avaliação.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.pt.png)

1. Métricas de risco e segurança:

    - Garanta que as respostas do modelo sejam seguras e estejam alinhadas com os Princípios de IA Responsável, evitando qualquer conteúdo prejudicial ou ofensivo.

    ![Resultado da avaliação.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.pt.png)

1. Você pode rolar para baixo para ver o **Resultado detalhado das métricas**.

    ![Resultado da avaliação.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.pt.png)

1. Avaliando seu modelo personalizado Phi-3 / Phi-3.5 tanto nas métricas de desempenho quanto de segurança, você pode confirmar que o modelo não apenas é eficaz, mas também segue práticas responsáveis de IA, tornando-o pronto para implantação no mundo real.

## Parabéns!

### Você concluiu este tutorial

Você avaliou com sucesso o modelo Phi-3 ajustado e integrado ao Prompt flow no Azure AI Foundry. Este é um passo importante para garantir que seus modelos de IA não apenas tenham bom desempenho, mas também sigam os princípios de IA Responsável da Microsoft para ajudar você a construir aplicações de IA confiáveis e seguras.

![Arquitetura.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pt.png)

## Limpeza dos Recursos do Azure

Limpe seus recursos do Azure para evitar cobranças adicionais na sua conta. Acesse o portal do Azure e exclua os seguintes recursos:

- O recurso Azure Machine learning.
- O endpoint do modelo Azure Machine learning.
- O recurso Azure AI Foundry Project.
- O recurso Azure AI Foundry Prompt flow.

### Próximos Passos

#### Documentação

- [Avalie sistemas de IA usando o Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de avaliação e monitoramento para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentação do Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conteúdo de Treinamento

- [Introdução à abordagem de IA Responsável da Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introdução ao Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referência

- [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anunciando novas ferramentas no Azure AI para ajudar a construir aplicações generativas de IA mais seguras e confiáveis](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Avaliação de aplicações generativas de IA](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.