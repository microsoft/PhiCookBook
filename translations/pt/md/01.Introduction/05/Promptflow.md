<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-16T22:39:21+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "pt"
}
-->
# **Introdução ao Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) é uma ferramenta visual de automação de fluxos de trabalho que permite aos utilizadores criar fluxos automatizados usando modelos pré-construídos e conectores personalizados. Foi concebida para permitir que desenvolvedores e analistas de negócio construam rapidamente processos automatizados para tarefas como gestão de dados, colaboração e otimização de processos. Com o Prompt Flow, os utilizadores podem facilmente ligar diferentes serviços, aplicações e sistemas, e automatizar processos empresariais complexos.

O Microsoft Prompt Flow foi desenvolvido para simplificar o ciclo completo de desenvolvimento de aplicações de IA alimentadas por Large Language Models (LLMs). Quer esteja a idealizar, prototipar, testar, avaliar ou implementar aplicações baseadas em LLM, o Prompt Flow simplifica o processo e permite construir aplicações LLM com qualidade de produção.

## Aqui estão as principais funcionalidades e benefícios de usar o Microsoft Prompt Flow:

**Experiência Interativa de Criação**

O Prompt Flow oferece uma representação visual da estrutura do seu fluxo, facilitando a compreensão e navegação dos seus projetos.  
Proporciona uma experiência de codificação semelhante a um notebook para um desenvolvimento e depuração eficientes do fluxo.

**Variantes de Prompt e Ajustes**

Crie e compare múltiplas variantes de prompt para facilitar um processo iterativo de refinamento. Avalie o desempenho de diferentes prompts e escolha os mais eficazes.

**Fluxos de Avaliação Integrados**  
Avalie a qualidade e eficácia dos seus prompts e fluxos usando ferramentas de avaliação incorporadas.  
Compreenda o desempenho das suas aplicações baseadas em LLM.

**Recursos Abrangentes**

O Prompt Flow inclui uma biblioteca de ferramentas, exemplos e modelos incorporados. Estes recursos servem como ponto de partida para o desenvolvimento, inspiram criatividade e aceleram o processo.

**Colaboração e Preparação para Empresas**

Suporte à colaboração em equipa, permitindo que vários utilizadores trabalhem juntos em projetos de engenharia de prompts.  
Mantenha controlo de versões e partilhe conhecimento de forma eficaz. Simplifique todo o processo de engenharia de prompts, desde o desenvolvimento e avaliação até à implementação e monitorização.

## Avaliação no Prompt Flow

No Microsoft Prompt Flow, a avaliação desempenha um papel crucial na análise do desempenho dos seus modelos de IA. Vamos explorar como pode personalizar fluxos e métricas de avaliação dentro do Prompt Flow:

![PFVizualise](../../../../../translated_images/pt-PT/pfvisualize.c1d9ca75baa2a222.webp)

**Compreender a Avaliação no Prompt Flow**

No Prompt Flow, um fluxo representa uma sequência de nós que processam a entrada e geram saída. Os fluxos de avaliação são tipos especiais de fluxos concebidos para avaliar o desempenho de uma execução com base em critérios e objetivos específicos.

**Principais características dos fluxos de avaliação**

Normalmente, são executados após o fluxo a ser testado, utilizando as suas saídas. Calculam pontuações ou métricas para medir o desempenho do fluxo testado. As métricas podem incluir precisão, pontuações de relevância ou outras medidas relevantes.

### Personalização dos Fluxos de Avaliação

**Definição de Entradas**

Os fluxos de avaliação precisam de receber as saídas da execução que está a ser testada. Defina as entradas de forma semelhante aos fluxos padrão.  
Por exemplo, se estiver a avaliar um fluxo QnA, nomeie uma entrada como "answer". Se estiver a avaliar um fluxo de classificação, nomeie uma entrada como "category". Também podem ser necessárias entradas de ground truth (por exemplo, etiquetas reais).

**Saídas e Métricas**

Os fluxos de avaliação produzem resultados que medem o desempenho do fluxo testado. As métricas podem ser calculadas usando Python ou LLM (Large Language Models). Utilize a função log_metric() para registar as métricas relevantes.

**Utilização de Fluxos de Avaliação Personalizados**

Desenvolva o seu próprio fluxo de avaliação adaptado às suas tarefas e objetivos específicos. Personalize as métricas com base nos seus objetivos de avaliação.  
Aplique este fluxo de avaliação personalizado a execuções em lote para testes em grande escala.

## Métodos de Avaliação Incorporados

O Prompt Flow também oferece métodos de avaliação incorporados.  
Pode submeter execuções em lote e usar estes métodos para avaliar o desempenho do seu fluxo com grandes conjuntos de dados.  
Consulte os resultados da avaliação, compare métricas e itere conforme necessário.  
Lembre-se, a avaliação é essencial para garantir que os seus modelos de IA cumprem os critérios e objetivos desejados. Explore a documentação oficial para instruções detalhadas sobre como desenvolver e usar fluxos de avaliação no Microsoft Prompt Flow.

Em resumo, o Microsoft Prompt Flow capacita os desenvolvedores a criar aplicações LLM de alta qualidade, simplificando a engenharia de prompts e fornecendo um ambiente robusto de desenvolvimento. Se trabalha com LLMs, o Prompt Flow é uma ferramenta valiosa para explorar. Consulte os [Documentos de Avaliação do Prompt Flow](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) para instruções detalhadas sobre como desenvolver e usar fluxos de avaliação no Microsoft Prompt Flow.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.