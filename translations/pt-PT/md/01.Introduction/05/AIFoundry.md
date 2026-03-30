# **Usar o Microsoft Foundry para avaliação**

![aistudo](../../../../../translated_images/pt-PT/AIFoundry.9e0b513e999a1c5a.webp)

Como avaliar a sua aplicação de IA generativa usando o [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Quer esteja a avaliar conversas de turno único ou de múltiplos turnos, o Microsoft Foundry oferece ferramentas para avaliar o desempenho do modelo e a segurança.

![aistudo](../../../../../translated_images/pt-PT/AIPortfolio.69da59a8e1eaa70f.webp)

## Como avaliar aplicações de IA generativa com o Microsoft Foundry
Para instruções mais detalhadas, consulte a [Documentação do Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Aqui estão os passos para começar:

## Avaliação de Modelos de IA Generativa no Microsoft Foundry

**Pré-requisitos**

- Um conjunto de dados de teste em formato CSV ou JSON.
- Um modelo de IA generativa implementado (como Phi-3, GPT 3.5, GPT 4, ou modelos Davinci).
- Um runtime com uma instância de computação para executar a avaliação.

## Métricas de Avaliação Integradas

O Microsoft Foundry permite avaliar tanto conversas de turno único como conversas complexas de múltiplos turnos.
Para cenários de Retrieval Augmented Generation (RAG), onde o modelo está fundamentado em dados específicos, pode avaliar o desempenho usando as métricas de avaliação integradas.
Além disso, pode avaliar cenários gerais de perguntas e respostas de turno único (não-RAG).

## Criar uma Execução de Avaliação

A partir da interface do Microsoft Foundry, navegue para a página Evaluate ou para a página Prompt Flow.
Siga o assistente de criação de avaliação para configurar uma execução de avaliação. Forneça um nome opcional para a sua avaliação.
Selecione o cenário que se alinha com os objetivos da sua aplicação.
Escolha uma ou mais métricas de avaliação para analisar a saída do modelo.

## Fluxo de Avaliação Personalizado (Opcional)

Para maior flexibilidade, pode estabelecer um fluxo de avaliação personalizado. Personalize o processo de avaliação com base nas suas necessidades específicas.

## Visualização dos Resultados

Após executar a avaliação, registe, visualize e analise métricas de avaliação detalhadas no Microsoft Foundry. Obtenha insights sobre as capacidades e limitações da sua aplicação.

**Nota** O Microsoft Foundry está atualmente em pré-visualização pública, pelo que deve ser usado para fins de experimentação e desenvolvimento. Para cargas de trabalho em produção, considere outras opções. Explore a [documentação oficial do AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para mais detalhes e instruções passo a passo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, deve-se ter em conta que traduções automatizadas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->