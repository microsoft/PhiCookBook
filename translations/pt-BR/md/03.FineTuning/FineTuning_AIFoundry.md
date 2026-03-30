# Ajuste fino do Phi-3 com Microsoft Foundry

Vamos explorar como ajustar finamente o modelo de linguagem Phi-3 Mini da Microsoft usando o Microsoft Foundry. O ajuste fino permite adaptar o Phi-3 Mini a tarefas específicas, tornando-o ainda mais poderoso e com maior consciência de contexto.

## Considerações

- **Capacidades:** Quais modelos podem ser ajustados finamente? Para que o modelo base pode ser ajustado?
- **Custo:** Qual o modelo de precificação para ajuste fino
- **Personalização:** Até que ponto posso modificar o modelo base – e de que maneiras?
- **Conveniência:** Como o ajuste fino realmente acontece – preciso escrever código personalizado? Preciso trazer minha própria capacidade de computação?
- **Segurança:** Modelos ajustados finamente são conhecidos por terem riscos de segurança – existem proteções implementadas para evitar danos não intencionais?

![AIFoundry Models](../../../../translated_images/pt-BR/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Preparação para o ajuste fino

### Pré-requisitos

> [!NOTE]
> Para modelos da família Phi-3, a oferta de ajuste fino pay-as-you-go está disponível apenas para hubs criados nas regiões **East US 2**.

- Uma assinatura Azure. Se você não tem uma assinatura Azure, crie uma [conta Azure paga](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) para começar.

- Um [projeto AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Os controles de acesso baseados em função do Azure (Azure RBAC) são usados para conceder acesso às operações no Microsoft Foundry. Para executar as etapas deste artigo, sua conta de usuário deve ter a __função Azure AI Developer__ atribuída ao grupo de recursos.

### Registro do provedor de assinatura

Verifique se a assinatura está registrada no provedor de recursos `Microsoft.Network`.

1. Faça login no [portal do Azure](https://portal.azure.com).
1. Selecione **Assinaturas** no menu à esquerda.
1. Selecione a assinatura que deseja usar.
1. Selecione **Configurações do projeto AI** > **Provedores de recursos** no menu à esquerda.
1. Confirme que **Microsoft.Network** está na lista de provedores de recursos. Caso contrário, adicione-o.

### Preparação dos dados

Prepare seus dados de treinamento e validação para ajustar seu modelo. Seus conjuntos de dados de treinamento e validação consistem em exemplos de entrada e saída para como você deseja que o modelo se comporte.

Certifique-se de que todos os seus exemplos de treinamento sigam o formato esperado para inferência. Para ajustar modelos de forma eficaz, garanta um conjunto de dados equilibrado e diversificado.

Isso envolve manter o equilíbrio dos dados, incluir vários cenários e refinar periodicamente os dados de treinamento para alinhar com as expectativas do mundo real, levando a respostas mais precisas e equilibradas do modelo.

Diferentes tipos de modelos exigem formatos diferentes de dados de treinamento.

### Chat Completion

Os dados de treinamento e validação que você usar **devem** estar formatados como um documento JSON Lines (JSONL). Para o `Phi-3-mini-128k-instruct`, o conjunto de dados para ajuste fino deve estar no formato conversacional usado pela API de Chat completions.

### Exemplo de formato de arquivo

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```
  
O tipo de arquivo suportado é JSON Lines. Os arquivos são carregados no datastore padrão e disponibilizados no seu projeto.

## Ajustando fino o Phi-3 com Microsoft Foundry

O Microsoft Foundry permite que você personalize grandes modelos de linguagem com seus próprios conjuntos de dados, usando um processo conhecido como ajuste fino. O ajuste fino oferece valor significativo ao permitir personalização e otimização para tarefas e aplicações específicas. Isso resulta em melhor desempenho, eficiência de custo, redução de latência e saídas personalizadas.

![Finetune AI Foundry](../../../../translated_images/pt-BR/AIFoundryfinetune.193aaddce48d553c.webp)

### Criar um novo projeto

1. Faça login no [Microsoft Foundry](https://ai.azure.com).

1. Selecione **+Novo projeto** para criar um novo projeto no Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/pt-BR/select-new-project.cd31c0404088d7a3.webp)

1. Execute as seguintes tarefas:

    - Nome do **Hub** do projeto. Deve ser um valor exclusivo.
    - Selecione o **Hub** a ser usado (crie um novo se necessário).

    ![FineTuneSelect](../../../../translated_images/pt-BR/create-project.ca3b71298b90e420.webp)

1. Execute as seguintes tarefas para criar um novo hub:

    - Insira o **Nome do Hub**. Deve ser um valor exclusivo.
    - Selecione sua **Assinatura** Azure.
    - Selecione o **Grupo de recursos** a ser usado (crie um novo se necessário).
    - Selecione a **Localização** que deseja usar.
    - Selecione **Conectar serviços Azure AI** para usar (crie um novo se necessário).
    - Selecione **Conectar Azure AI Search** para **Pular conexão**.

    ![FineTuneSelect](../../../../translated_images/pt-BR/create-hub.49e53d235e80779e.webp)

1. Selecione **Avançar**.
1. Selecione **Criar um projeto**.

### Preparação dos dados

Antes do ajuste fino, reúna ou crie um conjunto de dados relevante para sua tarefa, como instruções de chat, pares pergunta-resposta ou qualquer outro dado textual pertinente. Limpe e pré-processe esses dados removendo ruídos, lidando com valores ausentes e tokenizando o texto.

### Ajuste fino dos modelos Phi-3 no Microsoft Foundry

> [!NOTE]
> O ajuste fino dos modelos Phi-3 é atualmente suportado apenas em projetos localizados em East US 2.

1. Selecione **Catálogo de modelos** na aba à esquerda.

1. Digite *phi-3* na **barra de pesquisa** e selecione o modelo phi-3 que deseja usar.

    ![FineTuneSelect](../../../../translated_images/pt-BR/select-model.60ef2d4a6a3cec57.webp)

1. Selecione **Ajustar fino**.

    ![FineTuneSelect](../../../../translated_images/pt-BR/select-finetune.a976213b543dd9d8.webp)

1. Insira o **Nome do modelo ajustado**.

    ![FineTuneSelect](../../../../translated_images/pt-BR/finetune1.c2b39463f0d34148.webp)

1. Selecione **Avançar**.

1. Execute as tarefas seguintes:

    - Selecione o **tipo de tarefa** para **Chat completion**.
    - Selecione os **dados de treinamento** que deseja usar. Você pode enviá-los pelo Microsoft Foundry ou do seu ambiente local.

    ![FineTuneSelect](../../../../translated_images/pt-BR/finetune2.43cb099b1a94442d.webp)

1. Selecione **Avançar**.

1. Faça upload dos **dados de validação** que deseja usar ou selecione **Divisão automática dos dados de treinamento**.

    ![FineTuneSelect](../../../../translated_images/pt-BR/finetune3.fd96121b67dcdd92.webp)

1. Selecione **Avançar**.

1. Execute as seguintes tarefas:

    - Selecione o **multiplicador do tamanho do lote** que deseja usar.
    - Selecione a **taxa de aprendizado** que deseja usar.
    - Selecione o número de **épocas** que deseja usar.

    ![FineTuneSelect](../../../../translated_images/pt-BR/finetune4.e18b80ffccb5834a.webp)

1. Selecione **Enviar** para iniciar o processo de ajuste fino.

    ![FineTuneSelect](../../../../translated_images/pt-BR/select-submit.0a3802d581bac271.webp)


1. Assim que seu modelo for ajustado, o status será exibido como **Concluído**, conforme mostrado na imagem abaixo. Agora você pode implantar o modelo e usá-lo em sua própria aplicação, no playground ou no prompt flow. Para mais informações, veja [Como implantar a família Phi-3 de modelos pequenos com Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/pt-BR/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Para informações mais detalhadas sobre ajuste fino do Phi-3, visite [Ajustar Phi-3 modelos no Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Limpando seus modelos ajustados

Você pode excluir um modelo ajustado da lista de modelos ajustados no [Microsoft Foundry](https://ai.azure.com) ou na página de detalhes do modelo. Selecione o modelo ajustado que deseja excluir na página de Ajuste fino e depois selecione o botão Excluir para remover o modelo ajustado.

> [!NOTE]
> Você não pode excluir um modelo personalizado se ele tiver uma implantação existente. Primeiro, você deve excluir a implantação do modelo antes de excluir o modelo personalizado.

## Custos e cotas

### Considerações sobre custo e cota para modelos Phi-3 ajustados como serviço

Modelos Phi ajustados como serviço são oferecidos pela Microsoft e integrados ao Microsoft Foundry para uso. Você pode encontrar a precificação ao [implantar](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ou ajustar os modelos na aba de Preços e termos no assistente de implantação.

## Filtragem de conteúdo

Modelos implantados como serviço pay-as-you-go são protegidos pelo Azure AI Content Safety. Quando implantados em endpoints em tempo real, você pode optar por desabilitar essa capacidade. Com o Azure AI Content Safety habilitado, tanto o prompt quanto a completude passam por um conjunto de modelos de classificação destinados a detectar e evitar a produção de conteúdo prejudicial. O sistema de filtragem de conteúdo detecta e atua sobre categorias específicas de conteúdo potencialmente prejudicial tanto em prompts de entrada quanto em completudes de saída. Saiba mais sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuração do Ajuste Fino**

Hiperparâmetros: Defina hiperparâmetros, como taxa de aprendizado, tamanho do lote e número de épocas de treinamento.

**Função de perda**

Escolha uma função de perda adequada para sua tarefa (por exemplo, entropia cruzada).

**Otimizador**

Selecione um otimizador (por exemplo, Adam) para atualizações de gradiente durante o treinamento.

**Processo de Ajuste Fino**

- Carregar modelo pré-treinado: carregue o checkpoint do Phi-3 Mini.
- Adicionar camadas personalizadas: adicione camadas específicas para a tarefa (por exemplo, cabeça de classificação para instruções de chat).

**Treinar o modelo**  
Ajuste o modelo com seu conjunto de dados preparado. Monitore o progresso do treinamento e ajuste os hiperparâmetros conforme necessário.

**Avaliação e Validação**

Conjunto de validação: separe seus dados em conjuntos de treinamento e validação.

**Avaliar desempenho**

Use métricas como precisão, F1-score ou perplexidade para avaliar o desempenho do modelo.

## Salvar modelo ajustado

**Checkpoint**  
Salve o checkpoint do modelo ajustado para uso futuro.

## Implantação

- Implante como serviço web: implante seu modelo ajustado como serviço web no Microsoft Foundry.
- Teste o endpoint: envie consultas de teste para o endpoint implantado para verificar sua funcionalidade.

## Iterar e Melhorar

Iterar: Se o desempenho não estiver satisfatório, itere ajustando hiperparâmetros, adicionando mais dados ou fazendo mais épocas de ajuste fino.

## Monitorar e Refinar

Monitore continuamente o comportamento do modelo e refine conforme necessário.

## Personalizar e Expandir

Tarefas personalizadas: o Phi-3 Mini pode ser ajustado para várias tarefas além de instruções de chat. Explore outros casos de uso!  
Experimente: teste diferentes arquiteturas, combinações de camadas e técnicas para melhorar o desempenho.

> [!NOTE]
> O ajuste fino é um processo iterativo. Experimente, aprenda e adapte seu modelo para alcançar os melhores resultados para sua tarefa específica!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->