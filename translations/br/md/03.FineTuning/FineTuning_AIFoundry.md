<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-07-17T06:03:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "br"
}
-->
# Ajustando o Phi-3 com Azure AI Foundry

Vamos explorar como ajustar o modelo de linguagem Phi-3 Mini da Microsoft usando o Azure AI Foundry. O ajuste fino permite adaptar o Phi-3 Mini para tarefas específicas, tornando-o ainda mais poderoso e sensível ao contexto.

## Considerações

- **Capacidades:** Quais modelos podem ser ajustados? Para que o modelo base pode ser ajustado?
- **Custo:** Qual é o modelo de precificação para ajuste fino?
- **Personalização:** Até que ponto posso modificar o modelo base – e de que formas?
- **Conveniência:** Como o ajuste fino acontece na prática – preciso escrever código personalizado? Preciso trazer meu próprio poder computacional?
- **Segurança:** Modelos ajustados são conhecidos por apresentar riscos de segurança – existem mecanismos de proteção para evitar danos não intencionais?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.0e1b16f7d0b09b73e15278aa4351740ed2076b3bdde88c48e6839f8f8cf640c7.br.png)

## Preparação para o ajuste fino

### Pré-requisitos

> [!NOTE]
> Para modelos da família Phi-3, a oferta de ajuste fino no modelo pay-as-you-go está disponível apenas para hubs criados na região **East US 2**.

- Uma assinatura do Azure. Se você não tem uma assinatura, crie uma [conta Azure paga](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) para começar.

- Um [projeto AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- O controle de acesso baseado em função do Azure (Azure RBAC) é usado para conceder acesso às operações no Azure AI Foundry. Para realizar os passos deste artigo, sua conta de usuário deve ter a __função Azure AI Developer__ atribuída no grupo de recursos.

### Registro do provedor de assinatura

Verifique se a assinatura está registrada no provedor de recursos `Microsoft.Network`.

1. Faça login no [portal do Azure](https://portal.azure.com).
1. Selecione **Assinaturas** no menu à esquerda.
1. Selecione a assinatura que deseja usar.
1. Selecione **Configurações do projeto AI** > **Provedores de recursos** no menu à esquerda.
1. Confirme que **Microsoft.Network** está na lista de provedores de recursos. Caso contrário, adicione-o.

### Preparação dos dados

Prepare seus dados de treinamento e validação para ajustar seu modelo. Seus conjuntos de dados de treinamento e validação consistem em exemplos de entrada e saída que mostram como você deseja que o modelo se comporte.

Certifique-se de que todos os seus exemplos de treinamento sigam o formato esperado para inferência. Para ajustar modelos de forma eficaz, garanta um conjunto de dados equilibrado e diversificado.

Isso envolve manter o equilíbrio dos dados, incluir vários cenários e refinar periodicamente os dados de treinamento para alinhar com as expectativas do mundo real, resultando em respostas mais precisas e equilibradas do modelo.

Diferentes tipos de modelos exigem formatos diferentes para os dados de treinamento.

### Chat Completion

Os dados de treinamento e validação que você usar **devem** estar formatados como um documento JSON Lines (JSONL). Para `Phi-3-mini-128k-instruct`, o conjunto de dados para ajuste fino deve estar no formato conversacional usado pela API de Chat completions.

### Exemplo de formato de arquivo

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

O tipo de arquivo suportado é JSON Lines. Os arquivos são enviados para o datastore padrão e disponibilizados no seu projeto.

## Ajustando o Phi-3 com Azure AI Foundry

O Azure AI Foundry permite personalizar grandes modelos de linguagem com seus próprios conjuntos de dados por meio de um processo conhecido como ajuste fino. O ajuste fino oferece grande valor ao possibilitar a customização e otimização para tarefas e aplicações específicas. Isso resulta em melhor desempenho, eficiência de custo, menor latência e saídas personalizadas.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.193aaddce48d553ce078eabed1526dfa300ae7fac7840e10b38fb50ea86b436c.br.png)

### Criar um Novo Projeto

1. Faça login no [Azure AI Foundry](https://ai.azure.com).

1. Selecione **+New project** para criar um novo projeto no Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.br.png)

1. Realize as seguintes tarefas:

    - Nome do **Hub** do projeto. Deve ser um valor único.
    - Selecione o **Hub** a ser usado (crie um novo, se necessário).

    ![FineTuneSelect](../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.br.png)

1. Realize as seguintes tarefas para criar um novo hub:

    - Insira o **Nome do Hub**. Deve ser um valor único.
    - Selecione sua **Assinatura** do Azure.
    - Selecione o **Grupo de recursos** a ser usado (crie um novo, se necessário).
    - Selecione a **Localização** que deseja usar.
    - Selecione o **Connect Azure AI Services** a ser usado (crie um novo, se necessário).
    - Selecione **Connect Azure AI Search** para **Pular conexão**.

    ![FineTuneSelect](../../../../translated_images/create-hub.49e53d235e80779e95293c08654daf213e003b942a2fa81045b994c088acad7f.br.png)

1. Selecione **Next**.
1. Selecione **Create a project**.

### Preparação dos Dados

Antes do ajuste fino, reúna ou crie um conjunto de dados relevante para sua tarefa, como instruções de chat, pares de perguntas e respostas ou qualquer outro dado textual pertinente. Limpe e pré-processe esses dados removendo ruídos, tratando valores ausentes e tokenizando o texto.

### Ajuste fino dos modelos Phi-3 no Azure AI Foundry

> [!NOTE]
> O ajuste fino dos modelos Phi-3 é atualmente suportado apenas em projetos localizados na região East US 2.

1. Selecione **Model catalog** na aba lateral esquerda.

1. Digite *phi-3* na **barra de busca** e selecione o modelo phi-3 que deseja usar.

    ![FineTuneSelect](../../../../translated_images/select-model.60ef2d4a6a3cec57c3c45a8404613f25f8ad41534a209a88f5549e95d21320f8.br.png)

1. Selecione **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.a976213b543dd9d8d621e322d186ff670c3fb92bbba8435e6bcd4e79b9aab251.br.png)

1. Insira o **Nome do modelo ajustado**.

    ![FineTuneSelect](../../../../translated_images/finetune1.c2b39463f0d34148be1473af400e30e936c425f1cb8d5dbefcf9454008923402.br.png)

1. Selecione **Next**.

1. Realize as seguintes tarefas:

    - Selecione o **tipo de tarefa** para **Chat completion**.
    - Selecione os **dados de treinamento** que deseja usar. Você pode enviá-los pelo Azure AI Foundry ou do seu ambiente local.

    ![FineTuneSelect](../../../../translated_images/finetune2.43cb099b1a94442df8f77c70e22fce46849329882a9e278ab1d87df196a63c4c.br.png)

1. Selecione **Next**.

1. Envie os **dados de validação** que deseja usar ou selecione **Divisão automática dos dados de treinamento**.

    ![FineTuneSelect](../../../../translated_images/finetune3.fd96121b67dcdd928568f64970980db22685ef54a4e48d1cc8d139c1ecb8c99f.br.png)

1. Selecione **Next**.

1. Realize as seguintes tarefas:

    - Selecione o **multiplicador do tamanho do lote** que deseja usar.
    - Selecione a **taxa de aprendizado** que deseja usar.
    - Selecione o número de **épocas** que deseja usar.

    ![FineTuneSelect](../../../../translated_images/finetune4.e18b80ffccb5834a2690f855223a6e007bd8ca771663f7b0f5dbefb3c47850c3.br.png)

1. Selecione **Submit** para iniciar o processo de ajuste fino.

    ![FineTuneSelect](../../../../translated_images/select-submit.0a3802d581bac27168ae1a8667026ad7f6c5f9188615113968272dbe1f7f774d.br.png)

1. Quando seu modelo estiver ajustado, o status será exibido como **Completed**, conforme a imagem abaixo. Agora você pode implantar o modelo e usá-lo em sua própria aplicação, no playground ou no prompt flow. Para mais informações, veja [Como implantar a família de modelos pequenos Phi-3 com Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.4dc8d2357144cdef5ba7303f42e9f1fca2baa37049bcededb5392d51cb21cc03.br.png)

> [!NOTE]
> Para informações mais detalhadas sobre ajuste fino do Phi-3, visite [Ajuste fino dos modelos Phi-3 no Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Limpando seus modelos ajustados

Você pode excluir um modelo ajustado da lista de modelos ajustados no [Azure AI Foundry](https://ai.azure.com) ou na página de detalhes do modelo. Selecione o modelo ajustado que deseja excluir na página de Ajuste Fino e depois selecione o botão Excluir para removê-lo.

> [!NOTE]
> Você não pode excluir um modelo personalizado se ele tiver uma implantação existente. Primeiro, é necessário excluir a implantação do modelo antes de poder excluir o modelo personalizado.

## Custos e cotas

### Considerações sobre custo e cota para modelos Phi-3 ajustados como serviço

Modelos Phi ajustados como serviço são oferecidos pela Microsoft e integrados ao Azure AI Foundry para uso. Você pode encontrar os preços ao [implantar](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ou ajustar os modelos na aba Preços e termos do assistente de implantação.

## Filtragem de conteúdo

Modelos implantados como serviço no modelo pay-as-you-go são protegidos pelo Azure AI Content Safety. Quando implantados em endpoints em tempo real, você pode optar por desativar essa funcionalidade. Com o Azure AI Content Safety ativado, tanto o prompt quanto a resposta passam por um conjunto de modelos de classificação que detectam e previnem a geração de conteúdo prejudicial. O sistema de filtragem detecta e age sobre categorias específicas de conteúdo potencialmente nocivo tanto nos prompts de entrada quanto nas respostas geradas. Saiba mais sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuração do Ajuste Fino**

Hiperparâmetros: Defina hiperparâmetros como taxa de aprendizado, tamanho do lote e número de épocas de treinamento.

**Função de Perda**

Escolha uma função de perda adequada para sua tarefa (ex.: entropia cruzada).

**Otimizador**

Selecione um otimizador (ex.: Adam) para as atualizações de gradiente durante o treinamento.

**Processo de Ajuste Fino**

- Carregar Modelo Pré-Treinado: Carregue o checkpoint do Phi-3 Mini.
- Adicionar Camadas Personalizadas: Adicione camadas específicas para a tarefa (ex.: cabeça de classificação para instruções de chat).

**Treinar o Modelo**  
Ajuste o modelo usando seu conjunto de dados preparado. Monitore o progresso do treinamento e ajuste os hiperparâmetros conforme necessário.

**Avaliação e Validação**

Conjunto de Validação: Separe seus dados em conjuntos de treinamento e validação.

**Avaliar Desempenho**

Use métricas como acurácia, F1-score ou perplexidade para avaliar o desempenho do modelo.

## Salvar Modelo Ajustado

**Checkpoint**  
Salve o checkpoint do modelo ajustado para uso futuro.

## Implantação

- Implantar como Serviço Web: Implante seu modelo ajustado como um serviço web no Azure AI Foundry.
- Testar o Endpoint: Envie consultas de teste para o endpoint implantado para verificar sua funcionalidade.

## Iterar e Melhorar

Iterar: Se o desempenho não estiver satisfatório, faça iterações ajustando hiperparâmetros, adicionando mais dados ou treinando por mais épocas.

## Monitorar e Refinar

Monitore continuamente o comportamento do modelo e refine conforme necessário.

## Personalizar e Expandir

Tarefas Personalizadas: O Phi-3 Mini pode ser ajustado para várias tarefas além de instruções de chat. Explore outros casos de uso!  
Experimente: Teste diferentes arquiteturas, combinações de camadas e técnicas para melhorar o desempenho.

> [!NOTE]
> O ajuste fino é um processo iterativo. Experimente, aprenda e adapte seu modelo para alcançar os melhores resultados para sua tarefa específica!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.