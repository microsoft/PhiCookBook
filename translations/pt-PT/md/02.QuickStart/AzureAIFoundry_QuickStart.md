# **Usar o Phi-3 no Microsoft Foundry**

Com o desenvolvimento da IA Generativa, esperamos usar uma plataforma unificada para gerir diferentes LLM e SLM, integração de dados empresariais, operações de fine-tuning/RAG, e a avaliação de diferentes negócios empresariais após a integração de LLM e SLM, etc., para que as aplicações inteligentes de IA generativa sejam melhor implementadas. [Microsoft Foundry](https://ai.azure.com) é uma plataforma de aplicação de IA generativa a nível empresarial.

![aistudo](../../../../translated_images/pt-PT/aifoundry_home.f28a8127c96c7d93.webp)

Com o Microsoft Foundry, pode avaliar respostas de modelos de linguagem large (LLM) e orquestrar componentes de aplicação de prompt com prompt flow para melhor desempenho. A plataforma facilita a escalabilidade para transformar provas de conceito em produção completa com facilidade. O monitoramento contínuo e o refinamento suportam o sucesso a longo prazo.

Podemos rapidamente implementar o modelo Phi-3 no Microsoft Foundry através de passos simples, e depois usar o Microsoft Foundry para completar o Playground/Chat relacionado com o Phi-3, Fine-tuning, avaliação e outros trabalhos relacionados.

## **1. Preparação**

Se já tiver o [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) instalado na sua máquina, usar este template é tão simples como executar este comando numa nova diretoria.

## Criação Manual

Criar um projeto e um hub no Microsoft Foundry é uma excelente forma de organizar e gerir o seu trabalho de IA. Aqui está um guia passo a passo para começar:

### Criar um Projeto no Microsoft Foundry

1. **Aceda ao Microsoft Foundry**: Inicie sessão no portal do Microsoft Foundry.
2. **Criar um Projeto**:
   - Se estiver num projeto, selecione "Microsoft Foundry" no canto superior esquerdo da página para ir para a página Inicial.
   - Selecione "+ Criar projeto".
   - Introduza um nome para o projeto.
   - Se tiver um hub, será selecionado por predefinição. Se tiver acesso a mais do que um hub, pode selecionar um diferente no menu pendente. Se quiser criar um novo hub, selecione "Criar novo hub" e forneça um nome.
   - Selecione "Criar".

### Criar um Hub no Microsoft Foundry

1. **Aceda ao Microsoft Foundry**: Inicie sessão com a sua conta Azure.
2. **Criar um Hub**:
   - Selecione o Centro de Gestão no menu à esquerda.
   - Selecione "Todos os recursos", depois a seta para baixo junto a "+ Novo projeto" e selecione "+ Novo hub".
   - Na janela "Criar um novo hub", introduza um nome para o seu hub (ex., contoso-hub) e modifique os outros campos conforme desejar.
   - Selecione "Seguinte", reveja as informações e depois selecione "Criar".

Para instruções mais detalhadas, pode consultar a [documentação oficial da Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Após a criação bem-sucedida, pode aceder ao estúdio que criou através de [ai.azure.com](https://ai.azure.com/)

Podem existir vários projetos num Foundry de IA. Crie um projeto no Foundry de IA para preparar.

Crie Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Implementar um modelo Phi no Microsoft Foundry**

Clique na opção Explorar do projeto para entrar no Catálogo de Modelos e selecione Phi-3

Selecione Phi-3-mini-4k-instruct

Clique 'Implementar' para implementar o modelo Phi-3-mini-4k-instruct

> [!NOTE]
>
> Pode selecionar a potência de cálculo ao implementar

## **3. Playground Chat Phi no Microsoft Foundry**

Vá para a página de implementação, selecione Playground, e converse com o Phi-3 do Microsoft Foundry

## **4. Implementar o Modelo a partir do Microsoft Foundry**

Para implementar um modelo a partir do Catálogo de Modelos Azure, pode seguir estes passos:

- Inicie sessão no Microsoft Foundry.
- Escolha o modelo que deseja implementar no catálogo de modelos do Microsoft Foundry.
- Na página de Detalhes do modelo, selecione Implementar e depois selecione API Serverless com Azure AI Content Safety.
- Selecione o projeto no qual deseja implementar os seus modelos. Para usar a oferta de API Serverless, o seu espaço de trabalho deve pertencer à região East US 2 ou Sweden Central. Pode personalizar o nome da Implementação.
- No assistente de implementação, selecione os Preços e termos para conhecer os preços e termos de utilização.
- Selecione Implementar. Aguarde até que a implementação esteja pronta e seja redirecionado para a página de Implementações.
- Selecione Abrir no playground para começar a interagir com o modelo.
- Pode voltar à página de Implementações, selecionar a implementação, e anotar o URL alvo do endpoint e a Chave Secreta, que pode usar para chamar a implementação e gerar completions.
- Pode sempre encontrar os detalhes do endpoint, URL e chaves de acesso navegando para o separador Build e selecionando Implementações na seção Componentes.

> [!NOTE]
> Note que a sua conta deve ter permissões da função Azure AI Developer no Grupo de Recursos para realizar estes passos.

## **5. Usar a API Phi no Microsoft Foundry**

Pode aceder a https://{Nome do seu projeto}.region.inference.ml.azure.com/swagger.json através do Postman GET e combiná-lo com a Chave para conhecer as interfaces fornecidas

Pode obter os parâmetros de pedido muito convenientemente, assim como os parâmetros de resposta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->