<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:22:39+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "pt"
}
-->
# **Utilizar o Phi-3 no Azure AI Foundry**

Com o desenvolvimento da IA Generativa, esperamos usar uma plataforma unificada para gerir diferentes LLM e SLM, integração de dados empresariais, operações de fine-tuning/RAG, e a avaliação de diferentes negócios empresariais após a integração de LLM e SLM, entre outros, para que as aplicações inteligentes de IA generativa sejam melhor implementadas. O [Azure AI Foundry](https://ai.azure.com) é uma plataforma de aplicações de IA generativa a nível empresarial.

![aistudo](../../../../translated_images/pt/aifoundry_home.f28a8127c96c7d93.png)

Com o Azure AI Foundry, pode avaliar as respostas de modelos de linguagem grande (LLM) e orquestrar componentes de aplicação de prompts com prompt flow para melhor desempenho. A plataforma facilita a escalabilidade para transformar provas de conceito em produção completa com facilidade. O monitoramento contínuo e o refinamento apoiam o sucesso a longo prazo.

Podemos rapidamente implementar o modelo Phi-3 no Azure AI Foundry através de passos simples, e depois usar o Azure AI Foundry para completar o Playground/Chat, Fine-tuning, avaliação e outros trabalhos relacionados com o Phi-3.

## **1. Preparação**

Se já tem o [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) instalado na sua máquina, usar este template é tão simples como executar este comando numa nova diretoria.

## Criação Manual

Criar um projeto e um hub no Microsoft Azure AI Foundry é uma ótima forma de organizar e gerir o seu trabalho de IA. Aqui está um guia passo a passo para começar:

### Criar um Projeto no Azure AI Foundry

1. **Aceda ao Azure AI Foundry**: Inicie sessão no portal Azure AI Foundry.
2. **Criar um Projeto**:
   - Se estiver dentro de um projeto, selecione "Azure AI Foundry" no canto superior esquerdo da página para ir à página inicial.
   - Selecione "+ Create project".
   - Introduza um nome para o projeto.
   - Se tiver um hub, este será selecionado por defeito. Se tiver acesso a mais do que um hub, pode escolher outro no menu suspenso. Se quiser criar um novo hub, selecione "Create new hub" e forneça um nome.
   - Selecione "Create".

### Criar um Hub no Azure AI Foundry

1. **Aceda ao Azure AI Foundry**: Inicie sessão com a sua conta Azure.
2. **Criar um Hub**:
   - Selecione o Centro de Gestão no menu à esquerda.
   - Selecione "All resources", depois a seta para baixo ao lado de "+ New project" e escolha "+ New hub".
   - Na janela "Create a new hub", introduza um nome para o seu hub (ex.: contoso-hub) e modifique os outros campos conforme desejar.
   - Selecione "Next", reveja a informação e depois selecione "Create".

Para instruções mais detalhadas, pode consultar a documentação oficial da [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Após a criação bem-sucedida, pode aceder ao estúdio que criou através do [ai.azure.com](https://ai.azure.com/)

Podem existir vários projetos num único AI Foundry. Crie um projeto no AI Foundry para se preparar.

Crie Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Implementar um modelo Phi no Azure AI Foundry**

Clique na opção Explore do projeto para entrar no Catálogo de Modelos e selecione Phi-3

Selecione Phi-3-mini-4k-instruct

Clique em 'Deploy' para implementar o modelo Phi-3-mini-4k-instruct

> [!NOTE]
>
> Pode selecionar a potência de computação durante a implementação

## **3. Playground Chat Phi no Azure AI Foundry**

Vá à página de implementação, selecione Playground e converse com o Phi-3 do Azure AI Foundry

## **4. Implementar o Modelo a partir do Azure AI Foundry**

Para implementar um modelo a partir do Catálogo de Modelos do Azure, pode seguir estes passos:

- Inicie sessão no Azure AI Foundry.
- Escolha o modelo que pretende implementar no catálogo de modelos do Azure AI Foundry.
- Na página de Detalhes do modelo, selecione Deploy e depois selecione Serverless API com Azure AI Content Safety.
- Selecione o projeto onde pretende implementar os seus modelos. Para usar a oferta Serverless API, o seu workspace deve pertencer à região East US 2 ou Sweden Central. Pode personalizar o nome da implementação.
- No assistente de implementação, selecione Pricing and terms para conhecer os preços e termos de uso.
- Selecione Deploy. Aguarde até que a implementação esteja pronta e seja redirecionado para a página de Implementações.
- Selecione Open in playground para começar a interagir com o modelo.
- Pode voltar à página de Implementações, selecionar a implementação e anotar a URL de destino do endpoint e a Chave Secreta, que pode usar para chamar a implementação e gerar respostas.
- Pode sempre encontrar os detalhes do endpoint, URL e chaves de acesso navegando até ao separador Build e selecionando Deployments na secção Components.

> [!NOTE]
> Note que a sua conta deve ter permissões de função Azure AI Developer no Resource Group para realizar estes passos.

## **5. Utilizar a API Phi no Azure AI Foundry**

Pode aceder a https://{Your project name}.region.inference.ml.azure.com/swagger.json através do Postman com um pedido GET e combiná-lo com a Key para conhecer as interfaces fornecidas

Pode obter os parâmetros de pedido de forma muito conveniente, assim como os parâmetros de resposta.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.