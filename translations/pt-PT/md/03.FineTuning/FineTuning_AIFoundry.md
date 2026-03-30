# Ajustar o Phi-3 com Microsoft Foundry

Vamos explorar como ajustar o modelo de linguagem Phi-3 Mini da Microsoft usando o Microsoft Foundry. O fine-tuning permite que adapte o Phi-3 Mini a tarefas específicas, tornando-o ainda mais potente e contextualizado.

## Considerações

- **Capacidades:** Quais modelos podem ser ajustados? Para que pode o modelo base ser ajustado?
- **Custo:** Qual é o modelo de preços para o ajuste
- **Personalização:** Quanto posso modificar no modelo base – e de que formas?
- **Comodidade:** Como acontece o ajuste – preciso de escrever código personalizado? Preciso de trazer o meu próprio poder computacional?
- **Segurança:** Os modelos ajustados são conhecidos por ter riscos de segurança – existem barreiras para proteger contra danos não intencionais?

![AIFoundry Models](../../../../translated_images/pt-PT/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Preparação para o fine-tuning

### Pré-requisitos

> [!NOTE]
> Para os modelos da família Phi-3, a oferta de fine-tuning pay-as-you-go está disponível apenas para hubs criados na região **East US 2**.

- Uma subscrição Azure. Se não tiver uma subscrição Azure, crie uma [conta Azure paga](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) para começar.

- Um [projeto AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Os controlos de acesso baseados em função do Azure (Azure RBAC) são usados para conceder acesso às operações no Microsoft Foundry. Para realizar os passos deste artigo, a sua conta de utilizador deve ter atribuído o __papel Azure AI Developer__ no grupo de recursos.

### Registo do fornecedor da subscrição

Verifique se a subscrição está registada no fornecedor de recursos `Microsoft.Network`.

1. Inicie sessão no [portal Azure](https://portal.azure.com).
1. Selecione **Subscrições** no menu esquerdo.
1. Selecione a subscrição que deseja usar.
1. Selecione **Definições do projeto AI** > **Fornecedores de recursos** no menu esquerdo.
1. Confirme que **Microsoft.Network** está na lista de fornecedores de recursos. Caso contrário, adicione-o.

### Preparação dos dados

Prepare os seus dados de treino e validação para ajustar o seu modelo. Os seus conjuntos de dados de treino e validação consistem em exemplos de entrada e saída para como gostaria que o modelo se comportasse.

Assegure-se de que todos os seus exemplos de treino seguem o formato esperado para inferência. Para ajustar os modelos eficazmente, garanta um conjunto de dados equilibrado e diversificado.

Isto envolve manter o equilíbrio dos dados, incluir vários cenários e refinar periodicamente os dados de treino para alinhar com as expectativas do mundo real, conduzindo a respostas do modelo mais precisas e equilibradas.

Diferentes tipos de modelo requerem formatos diferentes dos dados de treino.

### Chat Completion

Os dados de treino e validação que usar **devem** estar formatados como um documento JSON Lines (JSONL). Para `Phi-3-mini-128k-instruct` o conjunto de dados para fine-tuning deve estar no formato de conversação usado pela API de Chat completions.

### Exemplo de formato de ficheiro

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

O tipo de ficheiro suportado é JSON Lines. Os ficheiros são carregados no datastore padrão e ficam disponíveis no seu projeto.

## Ajustar o Phi-3 com Microsoft Foundry

O Microsoft Foundry permite personalizar grandes modelos de linguagem com os seus próprios conjuntos de dados, usando um processo conhecido como fine-tuning. O fine-tuning oferece um valor significativo, permitindor personalizar e otimizar para tarefas e aplicações específicas. Conduz a melhorias no desempenho, eficiência de custo, diminuição da latência e resultados personalizados.

![Finetune AI Foundry](../../../../translated_images/pt-PT/AIFoundryfinetune.193aaddce48d553c.webp)

### Criar um Novo Projeto

1. Inicie sessão no [Microsoft Foundry](https://ai.azure.com).

1. Selecione **+New project** para criar um novo projeto no Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/pt-PT/select-new-project.cd31c0404088d7a3.webp)

1. Execute as seguintes tarefas:

    - Nome do **Hub** do projeto. Deve ser um valor único.
    - Selecione o **Hub** a utilizar (crie um novo se necessário).

    ![FineTuneSelect](../../../../translated_images/pt-PT/create-project.ca3b71298b90e420.webp)

1. Execute as seguintes tarefas para criar um novo hub:

    - Introduza o **Nome do Hub**. Deve ser um valor único.
    - Selecione a sua **Subscrição** Azure.
    - Selecione o **Grupo de recursos** a usar (crie um novo se necessário).
    - Selecione a **Localização** que deseja usar.
    - Selecione **Conectar Azure AI Services** a utilizar (crie um novo se necessário).
    - Selecione **Conectar Azure AI Search** para **Pular ligação**.

    ![FineTuneSelect](../../../../translated_images/pt-PT/create-hub.49e53d235e80779e.webp)

1. Selecione **Seguinte**.
1. Selecione **Criar um projeto**.

### Preparação dos dados

Antes do fine-tuning, recolha ou crie um conjunto de dados relevante para a sua tarefa, como instruções de chat, pares de perguntas e respostas ou quaisquer outros dados textuais pertinentes. Limpe e pré-processe estes dados removendo ruído, tratando valores em falta e tokenizando o texto.

### Ajustar modelos Phi-3 no Microsoft Foundry

> [!NOTE]
> O fine-tuning dos modelos Phi-3 é atualmente suportado apenas em projetos localizados na região East US 2.

1. Selecione **Catálogo de modelos** na barra lateral esquerda.

1. Digite *phi-3* na **barra de pesquisa** e selecione o modelo phi-3 que deseja usar.

    ![FineTuneSelect](../../../../translated_images/pt-PT/select-model.60ef2d4a6a3cec57.webp)

1. Selecione **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/pt-PT/select-finetune.a976213b543dd9d8.webp)

1. Insira o **Nome do modelo ajustado**.

    ![FineTuneSelect](../../../../translated_images/pt-PT/finetune1.c2b39463f0d34148.webp)

1. Selecione **Seguinte**.

1. Execute as seguintes tarefas:

    - Selecione o **tipo de tarefa** para **Chat completion**.
    - Selecione os **Dados de treino** que deseja usar. Pode carregá-los através dos dados do Microsoft Foundry ou a partir do seu ambiente local.

    ![FineTuneSelect](../../../../translated_images/pt-PT/finetune2.43cb099b1a94442d.webp)

1. Selecione **Seguinte**.

1. Carregue os **Dados de validação** que deseja usar. ou pode selecionar **Divisão automática dos dados de treino**.

    ![FineTuneSelect](../../../../translated_images/pt-PT/finetune3.fd96121b67dcdd92.webp)

1. Selecione **Seguinte**.

1. Execute as seguintes tarefas:

    - Selecione o **Multiplicador do tamanho do batch** que deseja usar.
    - Selecione a **Taxa de aprendizagem** que deseja usar.
    - Selecione os **Epochs** que deseja usar.

    ![FineTuneSelect](../../../../translated_images/pt-PT/finetune4.e18b80ffccb5834a.webp)

1. Selecione **Submeter** para iniciar o processo de fine-tuning.

    ![FineTuneSelect](../../../../translated_images/pt-PT/select-submit.0a3802d581bac271.webp)

1. Uma vez que o seu modelo esteja ajustado, o estado será exibido como **Concluído**, como mostrado na imagem abaixo. Agora pode implementar o modelo e usá-lo na sua própria aplicação, no playground, ou no prompt flow. Para mais informações, veja [Como implementar a família Phi-3 de pequenos modelos de linguagem com o Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/pt-PT/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Para informações mais detalhadas sobre fine-tuning do Phi-3, por favor visite [Ajustar modelos Phi-3 no Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Limpar os seus modelos ajustados

Pode apagar um modelo ajustado da lista de modelos fine-tuning no [Microsoft Foundry](https://ai.azure.com) ou a partir da página de detalhes do modelo. Selecione o modelo ajustado para apagar na página Fine-tuning, e depois selecione o botão Apagar para o eliminar.

> [!NOTE]
> Não pode apagar um modelo personalizado se ele tiver uma implementação existente. Deve primeiro apagar a implementação do modelo antes de poder eliminar o modelo personalizado.

## Custos e quotas

### Considerações sobre custo e quota para modelos Phi-3 ajustados como serviço

Os modelos Phi ajustados como serviço são oferecidos pela Microsoft e integrados com o Microsoft Foundry para utilização. Pode encontrar os preços quando [implementa](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ou ajusta os modelos na aba de Preços e termos no assistente de implementação.

## Filtragem de conteúdo

Modelos implementados como serviço com pay-as-you-go são protegidos pelo Azure AI Content Safety. Quando implementados em endpoints em tempo real, pode optar por não utilizar esta capacidade. Com o Azure AI Content Safety ativado, tanto o prompt como a resposta passam por um conjunto de modelos de classificação destinados a detectar e prevenir a geração de conteúdo prejudicial. O sistema de filtragem de conteúdo deteta e atua em categorias específicas de conteúdo potencialmente prejudicial tanto nos prompts de entrada como nas respostas. Saiba mais sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuração do Fine-Tuning**

Hiperparâmetros: Defina hiperparâmetros como taxa de aprendizagem, tamanho do batch, e número de épocas de treino.

**Função de perda**

Escolha uma função de perda apropriada para a sua tarefa (por exemplo, cross-entropy).

**Otimização**

Selecione um otimizador (por exemplo, Adam) para atualizações de gradiente durante o treino.

**Processo de fine-tuning**

- Carregar modelo pré-treinado: carregue o checkpoint do Phi-3 Mini.
- Adicionar camadas personalizadas: adicione camadas específicas da tarefa (por exemplo, cabeça de classificação para instruções de chat).

**Treinar o modelo**
Ajuste o modelo usando o seu conjunto de dados preparado. Monitorize o progresso do treino e ajuste os hiperparâmetros conforme necessário.

**Avaliação e validação**

Conjunto de validação: divida os seus dados em conjuntos de treino e validação.

**Avaliar desempenho**

Use métricas como acurácia, F1-score ou perplexidade para avaliar o desempenho do modelo.

## Guardar modelo ajustado

**Checkpoint**
Guarde o checkpoint do modelo ajustado para uso futuro.

## Implementação

- Implementar como serviço Web: implemente o seu modelo ajustado como um serviço web no Microsoft Foundry.
- Testar o endpoint: envie queries de teste para o endpoint implementado para verificar a sua funcionalidade.

## Iterar e melhorar

Iterar: Se o desempenho não for satisfatório, itere ajustando hiperparâmetros, adicionando mais dados ou ajustando por mais épocas.

## Monitorizar e refinar

Monitorize continuamente o comportamento do modelo e refine conforme necessário.

## Personalizar e expandir

Tarefas personalizadas: O Phi-3 Mini pode ser ajustado para várias tarefas além de instruções de chat. Explore outros casos de uso!
Experimente: Teste diferentes arquiteturas, combinações de camadas e técnicas para melhorar o desempenho.

> [!NOTE]
> O fine-tuning é um processo iterativo. Experimente, aprenda e adapte o seu modelo para alcançar os melhores resultados para a sua tarefa específica!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automatizadas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um ser humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->