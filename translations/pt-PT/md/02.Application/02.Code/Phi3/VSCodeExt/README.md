# **Crie o seu próprio Visual Studio Code GitHub Copilot Chat com a Família Microsoft Phi-3**

Já utilizou o agente de espaço de trabalho no GitHub Copilot Chat? Quer construir o seu próprio agente de código para a sua equipa? Este laboratório prático pretende combinar o modelo open source para construir um agente empresarial de código a nível empresarial.

## **Fundação**

### **Por que escolher Microsoft Phi-3**

Phi-3 é uma série familiar, incluindo phi-3-mini, phi-3-small, e phi-3-medium baseados em diferentes parâmetros de treino para geração de texto, completamento de diálogo e geração de código. Existe também o phi-3-vision baseado em Vision. É adequado para empresas ou equipas diferentes criarem soluções de IA generativa offline.

Recomenda-se ler este link [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

A extensão GitHub Copilot Chat oferece uma interface de chat que lhe permite interagir com o GitHub Copilot e receber respostas a questões relacionadas com codificação diretamente no VS Code, sem necessidade de navegar na documentação ou pesquisar em fóruns online.

O Copilot Chat pode usar realce de sintaxe, indentação, e outras funcionalidades de formatação para adicionar clareza à resposta gerada. Dependendo do tipo de questão colocada pelo utilizador, o resultado pode conter ligações para o contexto que o Copilot utilizou para gerar a resposta, como ficheiros de código fonte ou documentação, ou botões para aceder a funcionalidades do VS Code.

- O Copilot Chat integra-se no seu fluxo de desenvolvimento e oferece assistência onde for necessário:

- Inicie uma conversa de chat em linha diretamente a partir do editor ou do terminal para obter ajuda enquanto codifica

- Use a vista de Chat para ter um assistente IA ao lado para ajudar a qualquer altura

- Lance o Quick Chat para colocar uma questão rápida e voltar ao que estava a fazer

Pode usar o GitHub Copilot Chat em vários cenários, tais como:

- Responder a perguntas de codificação sobre como resolver melhor um problema

- Explicar o código de outra pessoa e sugerir melhorias

- Propor correções de código

- Gerar casos de teste unitários

- Gerar documentação de código

Recomenda-se ler este link [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Referenciar **@workspace** no Copilot Chat permite-lhe colocar perguntas sobre toda a sua base de código. Com base na pergunta, o Copilot recupera inteligentemente ficheiros e símbolos relevantes, que depois referencia na sua resposta como links e exemplos de código.

Para responder à sua pergunta, **@workspace** procura nas mesmas fontes que um programador usaria ao navegar numa base de código no VS Code:

- Todos os ficheiros no espaço de trabalho, exceto ficheiros ignorados por um ficheiro .gitignore

- Estrutura de diretórios com pastas e nomes de ficheiros aninhados

- Índice de pesquisa de código do GitHub, se o espaço de trabalho for um repositório GitHub e estiver indexado pela pesquisa de código

- Símbolos e definições no espaço de trabalho

- Texto atualmente selecionado ou texto visível no editor ativo

Nota: o .gitignore é ignorado se tiver um ficheiro aberto ou tiver texto selecionado dentro de um ficheiro ignorado.

Recomenda-se ler este link [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Saiba mais sobre este Laboratório**

O GitHub Copilot tem melhorado significativamente a eficiência de programação nas empresas, e cada empresa espera personalizar as funcionalidades relevantes do GitHub Copilot. Muitas empresas personalizaram Extensões semelhantes ao GitHub Copilot baseadas nos seus próprios cenários de negócio e modelos open source. Para as empresas, Extensões personalizadas são mais fáceis de controlar, mas isso também afeta a experiência do utilizador. Afinal, o GitHub Copilot tem funções mais fortes no tratamento de cenários gerais e profissionalismo. Se a experiência puder ser mantida consistente, seria melhor personalizar a Extensão própria da empresa. O GitHub Copilot Chat fornece APIs relevantes para as empresas expandirem a experiência de Chat. Manter uma experiência consistente e ter funções personalizadas é uma melhor experiência para o utilizador.

Este laboratório usa principalmente o modelo Phi-3 combinado com o NPU local e uma arquitetura híbrida Azure para construir um Agente personalizado no GitHub Copilot Chat ***@PHI3*** para auxiliar os desenvolvedores empresariais a completar a geração de código***(@PHI3 /gen)*** e gerar código baseado em imagens ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/pt-PT/cover.1017ebc9a7c46d09.webp)

### ***Nota:*** 

Este laboratório está atualmente implementado no AIPC de CPU Intel e Apple Silicon. Continuaremos a atualizar a versão Qualcomm do NPU.


## **Laboratório**


| Nome | Descrição | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalações(✅) | Configurar e instalar ambientes relacionados e ferramentas de instalação | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Executar fluxo Prompt com Phi-3-mini (✅) | Combinado com AIPC / Apple Silicon, usando NPU local para criar geração de código através do Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Desplegar Phi-3-vision no Azure Machine Learning Service(✅) | Gerar código por meio do despliegue no Catálogo de Modelos do Azure Machine Learning Service - imagem Phi-3-vision | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Criar um agente @phi-3 no GitHub Copilot Chat(✅)  | Criar um agente Phi-3 personalizado no GitHub Copilot Chat para completar geração de código, código de geração gráfica, RAG, etc. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Código de Exemplo (✅)  | Descarregar código de exemplo | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Recursos**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Saiba mais sobre GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Saiba mais sobre GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Saiba mais sobre GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Saiba mais sobre Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Saiba mais sobre o Catálogo de Modelos da Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela exactidão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informação crítica, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas derivadas da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->