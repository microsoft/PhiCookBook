# **Usando Phi-3 no Microsoft Foundry**

Com o desenvolvimento da IA Generativa, esperamos usar uma plataforma unificada para gerenciar diferentes LLM e SLM, integração de dados empresariais, operações de fine-tuning/RAG e a avaliação de diferentes negócios empresariais após a integração de LLM e SLM, etc., para que a IA generativa possa ser melhor implementada em aplicativos inteligentes. [Microsoft Foundry](https://ai.azure.com) é uma plataforma de aplicação de IA generativa em nível empresarial.

![aistudo](../../../../translated_images/pt-BR/aifoundry_home.f28a8127c96c7d93.webp)

Com o Microsoft Foundry, você pode avaliar as respostas do grande modelo de linguagem (LLM) e orquestrar componentes de aplicação de prompt com prompt flow para melhor desempenho. A plataforma facilita a escalabilidade para transformar provas de conceito em produção completa com facilidade. Monitoramento contínuo e refinamento suportam o sucesso a longo prazo.

Podemos implantar rapidamente o modelo Phi-3 no Microsoft Foundry através de passos simples, e então usar o Microsoft Foundry para completar o Playground/Chat, Fine-tuning, avaliação e outros trabalhos relacionados ao Phi-3.

## **1. Preparação**

Se você já tem o [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) instalado em sua máquina, usar este template é tão simples quanto executar este comando em um novo diretório.

## Criação Manual

Criar um projeto e hub no Microsoft Foundry é uma ótima forma de organizar e gerenciar seu trabalho com IA. Aqui está um guia passo a passo para você começar:

### Criando um Projeto no Microsoft Foundry

1. **Vá para o Microsoft Foundry**: Faça login no portal do Microsoft Foundry.
2. **Crie um Projeto**:
   - Se você estiver dentro de um projeto, selecione "Microsoft Foundry" no canto superior esquerdo da página para ir à página inicial.
   - Selecione "+ Create project".
   - Insira um nome para o projeto.
   - Se você tiver um hub, ele será selecionado por padrão. Se você tiver acesso a mais de um hub, pode selecionar outro no menu suspenso. Se quiser criar um novo hub, selecione "Create new hub" e forneça um nome.
   - Selecione "Create".

### Criando um Hub no Microsoft Foundry

1. **Vá para o Microsoft Foundry**: Faça login com sua conta Azure.
2. **Crie um Hub**:
   - Selecione o Centro de Gerenciamento no menu à esquerda.
   - Selecione "All resources", depois a seta para baixo ao lado de "+ New project" e selecione "+ New hub".
   - Na janela "Create a new hub", insira um nome para seu hub (por exemplo, contoso-hub) e modifique os outros campos conforme desejar.
   - Selecione "Next", revise as informações e então selecione "Create".

Para instruções mais detalhadas, você pode consultar a [documentação oficial da Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Após a criação bem-sucedida, você pode acessar o estúdio criado através de [ai.azure.com](https://ai.azure.com/).

Pode haver múltiplos projetos em um AI Foundry. Crie um projeto no AI Foundry para se preparar.

Crie os [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code) do Microsoft Foundry

## **2. Implantar um modelo Phi no Microsoft Foundry**

Clique na opção Explore do projeto para entrar no Catálogo de Modelos e selecione Phi-3

Selecione Phi-3-mini-4k-instruct

Clique em 'Deploy' para implantar o modelo Phi-3-mini-4k-instruct

> [!NOTE]
>
> Você pode selecionar a potência de computação ao implantar

## **3. Playground Chat Phi no Microsoft Foundry**

Vá para a página de implantação, selecione Playground e converse com o Phi-3 do Microsoft Foundry

## **4. Implantando o Modelo a partir do Microsoft Foundry**

Para implantar um modelo a partir do Catálogo de Modelos Azure, você pode seguir estes passos:

- Faça login no Microsoft Foundry.
- Escolha o modelo que deseja implantar no catálogo de modelos do Microsoft Foundry.
- Na página de Detalhes do modelo, selecione Deploy e depois selecione Serverless API com Azure AI Content Safety.
- Selecione o projeto no qual deseja implantar seus modelos. Para usar a oferta Serverless API, seu workspace deve pertencer à região East US 2 ou Sweden Central. Você pode personalizar o nome da implantação.
- No assistente de implantação, selecione Pricing and terms para saber sobre preços e termos de uso.
- Selecione Deploy. Aguarde até que a implantação esteja pronta e você seja redirecionado para a página de Deployments.
- Selecione Open in playground para começar a interagir com o modelo.
- Você pode voltar à página de Deployments, selecionar a implantação e anotar a URL de destino (Target URL) do endpoint e a Chave Secreta, que você pode usar para chamar a implantação e gerar concluídas.
- Você sempre pode encontrar os detalhes do endpoint, URL e chaves de acesso navegando até a aba Build e selecionando Deployments na seção Components.

> [!NOTE]
> Por favor, note que sua conta deve ter permissões da função Azure AI Developer no Grupo de Recursos para executar esses passos.

## **5. Usando a API Phi no Microsoft Foundry**

Você pode acessar https://{Seu nome do projeto}.region.inference.ml.azure.com/swagger.json via Postman GET e combiná-lo com a Chave para conhecer as interfaces fornecidas

Você pode obter os parâmetros de requisição de forma muito conveniente, assim como os parâmetros de resposta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->