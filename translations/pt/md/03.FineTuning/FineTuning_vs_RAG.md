<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:15:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "pt"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG é a combinação de recuperação de dados + geração de texto. Os dados estruturados e não estruturados da empresa são armazenados no banco de dados vetorial. Ao buscar conteúdo relevante, o resumo e o conteúdo relacionados são encontrados para formar um contexto, e a capacidade de completamento de texto do LLM/SLM é combinada para gerar o conteúdo.

## Processo do RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.pt.png)

## Fine-tuning
Fine-tuning é baseado na melhoria de um determinado modelo. Não é necessário começar pelo algoritmo do modelo, mas os dados precisam ser acumulados continuamente. Se você deseja uma terminologia e expressão linguística mais precisas em aplicações industriais, fine-tuning é a melhor escolha. Mas se seus dados mudam com frequência, o fine-tuning pode se tornar complicado.

## Como escolher
Se nossa resposta exige a introdução de dados externos, RAG é a melhor opção.

Se você precisa entregar conhecimento estável e preciso da indústria, fine-tuning será uma boa escolha. RAG prioriza trazer conteúdo relevante, mas pode não captar sempre as nuances especializadas.

Fine-tuning requer um conjunto de dados de alta qualidade e, se for apenas um pequeno volume de dados, não fará muita diferença. RAG é mais flexível.  
Fine-tuning é uma caixa preta, uma metafísica, e é difícil entender seu mecanismo interno. Mas RAG facilita encontrar a origem dos dados, permitindo ajustar de forma eficaz alucinações ou erros de conteúdo e oferecendo melhor transparência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.