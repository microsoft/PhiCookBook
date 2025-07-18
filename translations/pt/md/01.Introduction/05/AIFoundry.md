<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:30:37+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "pt"
}
-->
# **Utilizar o Azure AI Foundry para avaliação**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5aa227e4c7028b5ff9a6cb712e6613c696705445ee4ca8f35d.pt.png)

Como avaliar a sua aplicação de IA generativa usando o [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Quer esteja a avaliar conversas de uma única interação ou de múltiplas interações, o Azure AI Foundry oferece ferramentas para avaliar o desempenho e a segurança do modelo.

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f2bab1836c11a69fc97e59f1b1b4154ce5e58bc589d278047.pt.png)

## Como avaliar aplicações de IA generativa com o Azure AI Foundry  
Para instruções mais detalhadas, consulte a [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Aqui estão os passos para começar:

## Avaliar Modelos de IA Generativa no Azure AI Foundry

**Pré-requisitos**

- Um conjunto de dados de teste em formato CSV ou JSON.  
- Um modelo de IA generativa implementado (como Phi-3, GPT 3.5, GPT 4 ou modelos Davinci).  
- Um runtime com uma instância de computação para executar a avaliação.

## Métricas de Avaliação Integradas

O Azure AI Foundry permite avaliar tanto conversas de uma única interação como conversas complexas de múltiplas interações.  
Para cenários de Retrieval Augmented Generation (RAG), onde o modelo está fundamentado em dados específicos, pode avaliar o desempenho usando métricas de avaliação integradas.  
Além disso, pode avaliar cenários gerais de perguntas e respostas de uma única interação (não RAG).

## Criar uma Execução de Avaliação

Na interface do Azure AI Foundry, navegue até à página Evaluate ou à página Prompt Flow.  
Siga o assistente de criação de avaliação para configurar uma execução de avaliação. Pode fornecer um nome opcional para a sua avaliação.  
Selecione o cenário que melhor se alinha com os objetivos da sua aplicação.  
Escolha uma ou mais métricas de avaliação para analisar a saída do modelo.

## Fluxo de Avaliação Personalizado (Opcional)

Para maior flexibilidade, pode criar um fluxo de avaliação personalizado. Personalize o processo de avaliação conforme as suas necessidades específicas.

## Visualizar Resultados

Após executar a avaliação, registe, visualize e analise métricas detalhadas no Azure AI Foundry. Obtenha insights sobre as capacidades e limitações da sua aplicação.

**Note** O Azure AI Foundry está atualmente em pré-visualização pública, pelo que deve ser usado para fins de experimentação e desenvolvimento. Para cargas de trabalho em produção, considere outras opções. Explore a [documentação oficial do AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para mais detalhes e instruções passo a passo.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.