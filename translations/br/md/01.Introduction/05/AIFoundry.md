<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-05-09T14:56:01+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "br"
}
-->
# **Usando Azure AI Foundry para avaliação**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.br.png)

Como avaliar sua aplicação de IA generativa usando [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Quer você esteja avaliando conversas de uma única rodada ou múltiplas rodadas, o Azure AI Foundry oferece ferramentas para medir o desempenho e a segurança do modelo.

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.br.png)

## Como avaliar apps de IA generativa com Azure AI Foundry  
Para instruções mais detalhadas, consulte a [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Aqui estão os passos para começar:

## Avaliando Modelos de IA Generativa no Azure AI Foundry

**Pré-requisitos**

- Um conjunto de dados de teste em formato CSV ou JSON.  
- Um modelo de IA generativa implantado (como Phi-3, GPT 3.5, GPT 4 ou modelos Davinci).  
- Um ambiente de execução com uma instância de computação para rodar a avaliação.

## Métricas de Avaliação Integradas

O Azure AI Foundry permite avaliar tanto conversas de uma única rodada quanto conversas complexas de múltiplas rodadas.  
Para cenários de Retrieval Augmented Generation (RAG), onde o modelo é fundamentado em dados específicos, você pode medir o desempenho usando as métricas de avaliação integradas.  
Além disso, é possível avaliar cenários gerais de perguntas e respostas de uma única rodada (não-RAG).

## Criando uma Execução de Avaliação

No UI do Azure AI Foundry, navegue até a página Evaluate ou Prompt Flow.  
Siga o assistente de criação para configurar uma execução de avaliação. Forneça um nome opcional para sua avaliação.  
Selecione o cenário que melhor se encaixa nos objetivos da sua aplicação.  
Escolha uma ou mais métricas de avaliação para medir a saída do modelo.

## Fluxo de Avaliação Personalizado (Opcional)

Para maior flexibilidade, você pode criar um fluxo de avaliação personalizado. Ajuste o processo de avaliação conforme suas necessidades específicas.

## Visualizando Resultados

Após rodar a avaliação, registre, visualize e analise as métricas detalhadas no Azure AI Foundry. Obtenha insights sobre as capacidades e limitações da sua aplicação.

**Note** Azure AI Foundry está atualmente em prévia pública, então utilize para experimentação e desenvolvimento. Para cargas de trabalho em produção, considere outras opções. Explore a [documentação oficial do AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para mais detalhes e instruções passo a passo.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.