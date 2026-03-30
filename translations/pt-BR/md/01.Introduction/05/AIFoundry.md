# **Usando o Microsoft Foundry para avaliação**

![aistudo](../../../../../translated_images/pt-BR/AIFoundry.9e0b513e999a1c5a.webp)

Como avaliar sua aplicação de IA generativa usando o [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Seja você avaliando conversas de uma única rodada ou multilaterais, o Microsoft Foundry fornece ferramentas para avaliar o desempenho e a segurança do modelo.

![aistudo](../../../../../translated_images/pt-BR/AIPortfolio.69da59a8e1eaa70f.webp)

## Como avaliar aplicativos de IA generativa com o Microsoft Foundry
Para instruções mais detalhadas, veja a [Documentação do Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Aqui estão os passos para começar:

## Avaliando Modelos de IA Generativa no Microsoft Foundry

**Pré-requisitos**

- Um conjunto de dados de teste no formato CSV ou JSON.
- Um modelo de IA generativa implantado (como Phi-3, GPT 3.5, GPT 4 ou modelos Davinci).
- Um ambiente de execução com uma instância de computação para realizar a avaliação.

## Métricas de Avaliação Integradas

O Microsoft Foundry permite avaliar tanto conversas de uma única rodada quanto conversas complexas e multilaterais.
Para cenários de Geração Aumentada por Recuperação (RAG), onde o modelo está fundamentado em dados específicos, você pode avaliar o desempenho usando métricas de avaliação integradas.
Além disso, é possível avaliar cenários gerais de perguntas e respostas de uma única rodada (não-RAG).

## Criando uma Execução de Avaliação

No UI do Microsoft Foundry, navegue até a página Avaliar ou a página Fluxo de Prompt.
Siga o assistente de criação de avaliação para configurar uma execução de avaliação. Forneça um nome opcional para sua avaliação.
Selecione o cenário que esteja alinhado com os objetivos do seu aplicativo.
Escolha uma ou mais métricas de avaliação para analisar a saída do modelo.

## Fluxo de Avaliação Personalizado (Opcional)

Para maior flexibilidade, você pode estabelecer um fluxo de avaliação personalizado. Personalize o processo de avaliação com base em seus requisitos específicos.

## Visualizando Resultados

Após executar a avaliação, registre, visualize e analise métricas detalhadas de avaliação no Microsoft Foundry. Obtenha insights sobre as capacidades e limitações do seu aplicativo.



**Nota** O Microsoft Foundry está atualmente em prévia pública, portanto use-o para experimentação e fins de desenvolvimento. Para cargas de trabalho em produção, considere outras opções. Explore a [documentação oficial do AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para mais detalhes e instruções passo a passo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->