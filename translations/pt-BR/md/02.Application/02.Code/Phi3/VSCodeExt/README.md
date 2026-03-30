# **Construa seu próprio Visual Studio Code GitHub Copilot Chat com a Família Microsoft Phi-3**

Você já usou o agente do workspace no GitHub Copilot Chat? Quer construir seu próprio agente de código para sua equipe? Este laboratório prático espera combinar o modelo open source para construir um agente de negócios de código em nível empresarial.

## **Fundação**

### **Por que escolher o Microsoft Phi-3**

Phi-3 é uma família de séries, incluindo phi-3-mini, phi-3-small e phi-3-medium com base em diferentes parâmetros de treinamento para geração de texto, conclusão de diálogo e geração de código. Também existe o phi-3-vision baseado em Vision. É adequado para empresas ou diferentes equipes criarem soluções de IA generativa offline.

Recomendado ler este link [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

A extensão GitHub Copilot Chat oferece uma interface de chat que permite interagir com o GitHub Copilot e receber respostas para perguntas relacionadas à codificação diretamente dentro do VS Code, sem precisar navegar na documentação ou buscar em fóruns online.

O Copilot Chat pode usar destaque de sintaxe, indentação e outros recursos de formatação para adicionar clareza à resposta gerada. Dependendo do tipo de pergunta do usuário, o resultado pode conter links para o contexto que o Copilot usou para gerar a resposta, como arquivos de código fonte ou documentação, ou botões para acessar funcionalidades do VS Code.

- O Copilot Chat se integra ao seu fluxo de desenvolvimento e oferece assistência onde você precisar:

- Inicie uma conversa de chat inline diretamente do editor ou terminal para obter ajuda enquanto codifica

- Use a visualização de Chat para ter um assistente de IA ao lado para ajudar a qualquer momento

- Inicie o Quick Chat para fazer uma pergunta rápida e voltar ao que estava fazendo

Você pode usar o GitHub Copilot Chat em vários cenários, como:

- Responder perguntas de programação sobre a melhor forma de resolver um problema

- Explicar o código de outra pessoa e sugerir melhorias

- Propor correções de código

- Gerar casos de teste unitários

- Gerar documentação de código

Recomendado ler este link [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Referenciar **@workspace** no Copilot Chat permite que você faça perguntas sobre todo o seu código-fonte. Baseado na pergunta, o Copilot recupera inteligentemente arquivos e símbolos relevantes, que ele então referencia em sua resposta como links e exemplos de código.

Para responder à sua pergunta, **@workspace** pesquisa pelas mesmas fontes que um desenvolvedor usaria ao navegar em um código no VS Code:

- Todos os arquivos no workspace, exceto os arquivos que são ignorados por um arquivo .gitignore

- Estrutura de diretórios com pastas aninhadas e nomes de arquivos

- Índice de pesquisa de código do GitHub, se o workspace for um repositório GitHub e estiver indexado pela pesquisa de código

- Símbolos e definições no workspace

- Texto atualmente selecionado ou texto visível no editor ativo

Nota: o .gitignore é ignorado se você tiver um arquivo aberto ou texto selecionado dentro de um arquivo ignorado.

Recomendado ler este link [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Saiba mais sobre este Laboratório**

O GitHub Copilot melhorou muito a eficiência da programação nas empresas, e toda empresa deseja personalizar as funções relevantes do GitHub Copilot. Muitas empresas têm Extensões personalizadas similares ao GitHub Copilot baseadas em seus próprios cenários de negócios e modelos open source. Para as empresas, as Extensões personalizadas são mais fáceis de controlar, mas isso também afeta a experiência do usuário. Afinal, o GitHub Copilot tem funções mais fortes no tratamento de cenários gerais e profissionalismo. Se a experiência puder ser mantida consistente, seria melhor personalizar a própria Extensão da empresa. O GitHub Copilot Chat fornece APIs relevantes para as empresas expandirem a experiência de Chat. Manter uma experiência consistente e ter funções personalizadas é uma melhor experiência para o usuário.

Este laboratório usa principalmente o modelo Phi-3 combinado com o NPU local e o híbrido Azure para construir um Agente personalizado no GitHub Copilot Chat ***@PHI3*** para auxiliar desenvolvedores empresariais a completar geração de código***(@PHI3 /gen)*** e gerar código baseado em imagens ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/pt-BR/cover.1017ebc9a7c46d09.webp)

### ***Nota:***

Este laboratório está atualmente implementado no AIPC de CPU Intel e Apple Silicon. Continuaremos atualizando a versão Qualcomm do NPU.


## **Laboratório**


| Nome | Descrição | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalações(✅) | Configurar e instalar ambientes relacionados e ferramentas de instalação | [Ir](./HOL/AIPC/01.Installations.md) |[Ir](./HOL/Apple/01.Installations.md) |
| Lab1 - Executar fluxo Prompt com Phi-3-mini (✅) | Combinado com AIPC / Apple Silicon, usando NPU local para criar geração de código via Phi-3-mini | [Ir](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Ir](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Implantar Phi-3-vision no Azure Machine Learning Service(✅) | Gerar código implantando o Catálogo de Modelos do Azure Machine Learning Service - imagem Phi-3-vision | [Ir](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Ir](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Criar um agente @phi-3 no GitHub Copilot Chat(✅)  | Criar um agente Phi-3 personalizado no GitHub Copilot Chat para completar geração de código, geração de código gráfico, RAG, etc. | [Ir](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Ir](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Código de Exemplo (✅)  | Baixar código de exemplo | [Ir](../../../../../../../code/07.Lab/01/AIPC) | [Ir](../../../../../../../code/07.Lab/01/Apple) |


## **Recursos**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Saiba mais sobre GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Saiba mais sobre GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Saiba mais sobre a API do GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Saiba mais sobre o Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Saiba mais sobre o Catálogo de Modelos do Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->