<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:22:57+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "br"
}
-->
# **Usando Phi-3 no Azure AI Foundry**

Com o desenvolvimento da IA Generativa, esperamos usar uma plataforma unificada para gerenciar diferentes LLM e SLM, integração de dados empresariais, operações de fine-tuning/RAG e a avaliação de diferentes negócios após a integração de LLM e SLM, entre outros, para que as aplicações inteligentes baseadas em IA generativa sejam melhor implementadas. O [Azure AI Foundry](https://ai.azure.com) é uma plataforma de aplicação de IA generativa em nível empresarial.

![aistudo](../../../../translated_images/br/aifoundry_home.f28a8127c96c7d93.png)

Com o Azure AI Foundry, você pode avaliar as respostas de grandes modelos de linguagem (LLM) e orquestrar componentes de aplicação de prompt com prompt flow para melhor desempenho. A plataforma facilita a escalabilidade para transformar provas de conceito em produção completa com facilidade. Monitoramento contínuo e refinamento suportam o sucesso a longo prazo.

Podemos implantar rapidamente o modelo Phi-3 no Azure AI Foundry por meio de passos simples e, em seguida, usar o Azure AI Foundry para completar Playground/Chat, Fine-tuning, avaliação e outros trabalhos relacionados ao Phi-3.

## **1. Preparação**

Se você já tem o [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) instalado na sua máquina, usar este template é tão simples quanto executar este comando em um diretório novo.

## Criação Manual

Criar um projeto e um hub no Microsoft Azure AI Foundry é uma ótima forma de organizar e gerenciar seu trabalho com IA. Aqui está um guia passo a passo para começar:

### Criando um Projeto no Azure AI Foundry

1. **Acesse o Azure AI Foundry**: Faça login no portal do Azure AI Foundry.
2. **Crie um Projeto**:
   - Se você estiver dentro de um projeto, selecione "Azure AI Foundry" no canto superior esquerdo da página para ir à página inicial.
   - Selecione "+ Create project".
   - Insira um nome para o projeto.
   - Se você já tiver um hub, ele será selecionado por padrão. Se tiver acesso a mais de um hub, pode escolher outro no menu suspenso. Se quiser criar um novo hub, selecione "Create new hub" e informe um nome.
   - Selecione "Create".

### Criando um Hub no Azure AI Foundry

1. **Acesse o Azure AI Foundry**: Faça login com sua conta Azure.
2. **Crie um Hub**:
   - Selecione o Centro de Gerenciamento no menu à esquerda.
   - Selecione "All resources", depois a seta para baixo ao lado de "+ New project" e escolha "+ New hub".
   - Na janela "Create a new hub", insira um nome para seu hub (exemplo: contoso-hub) e modifique os outros campos conforme desejar.
   - Selecione "Next", revise as informações e depois selecione "Create".

Para instruções mais detalhadas, você pode consultar a [documentação oficial da Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Após a criação bem-sucedida, você pode acessar o estúdio criado através do [ai.azure.com](https://ai.azure.com/)

É possível ter múltiplos projetos em um único AI Foundry. Crie um projeto no AI Foundry para se preparar.

Crie Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Implantar um modelo Phi no Azure AI Foundry**

Clique na opção Explore do projeto para entrar no Catálogo de Modelos e selecione Phi-3

Selecione Phi-3-mini-4k-instruct

Clique em 'Deploy' para implantar o modelo Phi-3-mini-4k-instruct

> [!NOTE]
>
> Você pode escolher a capacidade computacional durante a implantação

## **3. Playground Chat Phi no Azure AI Foundry**

Vá para a página de implantação, selecione Playground e converse com o Phi-3 do Azure AI Foundry

## **4. Implantando o Modelo a partir do Azure AI Foundry**

Para implantar um modelo a partir do Catálogo de Modelos do Azure, siga estes passos:

- Faça login no Azure AI Foundry.
- Escolha o modelo que deseja implantar no catálogo de modelos do Azure AI Foundry.
- Na página de Detalhes do modelo, selecione Deploy e depois selecione Serverless API com Azure AI Content Safety.
- Selecione o projeto no qual deseja implantar seus modelos. Para usar a oferta Serverless API, seu workspace deve estar nas regiões East US 2 ou Sweden Central. Você pode personalizar o nome da implantação.
- No assistente de implantação, selecione Pricing and terms para conhecer os preços e termos de uso.
- Selecione Deploy. Aguarde até que a implantação esteja pronta e você seja redirecionado para a página de Deployments.
- Selecione Open in playground para começar a interagir com o modelo.
- Você pode voltar à página de Deployments, selecionar a implantação e anotar a URL do endpoint (Target URL) e a Chave Secreta, que podem ser usadas para chamar a implantação e gerar respostas.
- Você sempre pode encontrar os detalhes do endpoint, URL e chaves de acesso navegando até a aba Build e selecionando Deployments na seção Components.

> [!NOTE]
> Lembre-se que sua conta deve ter permissões de função Azure AI Developer no Resource Group para realizar esses passos.

## **5. Usando a API Phi no Azure AI Foundry**

Você pode acessar https://{Seu nome do projeto}.region.inference.ml.azure.com/swagger.json via Postman com método GET e combinar com a Key para conhecer as interfaces fornecidas

Você pode obter os parâmetros de requisição de forma muito prática, assim como os parâmetros de resposta.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.