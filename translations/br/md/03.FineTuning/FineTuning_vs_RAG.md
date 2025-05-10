<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:15:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "br"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG é recuperação de dados + geração de texto. Os dados estruturados e não estruturados da empresa são armazenados no banco de dados vetorial. Ao buscar conteúdo relevante, o resumo e o conteúdo relacionados são encontrados para formar um contexto, e a capacidade de completamento de texto do LLM/SLM é combinada para gerar o conteúdo.

## RAG Process
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.br.png)

## Fine-tuning
Fine-tuning é baseado na melhoria de um determinado modelo. Não é necessário começar pelo algoritmo do modelo, mas os dados precisam ser acumulados continuamente. Se você quer terminologia e expressão linguística mais precisas em aplicações industriais, fine-tuning é a melhor escolha. Mas se seus dados mudam com frequência, fine-tuning pode se tornar complicado.

## How to choose
Se nossa resposta requer a introdução de dados externos, RAG é a melhor opção

Se você precisa gerar conhecimento industrial estável e preciso, fine-tuning será uma boa escolha. RAG prioriza puxar conteúdo relevante, mas pode não capturar sempre as nuances especializadas.

Fine-tuning exige um conjunto de dados de alta qualidade, e se for apenas um pequeno conjunto de dados, não fará muita diferença. RAG é mais flexível.  
Fine-tuning é uma caixa preta, uma espécie de metafísica, e é difícil entender seu mecanismo interno. Mas RAG facilita encontrar a origem dos dados, permitindo ajustar efetivamente alucinações ou erros de conteúdo e oferecendo melhor transparência.

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.