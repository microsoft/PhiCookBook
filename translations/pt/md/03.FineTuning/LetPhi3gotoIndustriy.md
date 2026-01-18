<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:55:38+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "pt"
}
-->
# **Deixe o Phi-3 tornar-se um especialista na indústria**

Para aplicar o modelo Phi-3 numa indústria, é necessário adicionar dados empresariais específicos dessa indústria ao modelo Phi-3. Temos duas opções diferentes: a primeira é RAG (Retrieval Augmented Generation) e a segunda é Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG é a combinação de recuperação de dados + geração de texto. Os dados estruturados e não estruturados da empresa são armazenados numa base de dados vetorial. Ao procurar conteúdo relevante, é encontrado um resumo e conteúdo pertinente para formar um contexto, e a capacidade de completamento de texto do LLM/SLM é combinada para gerar o conteúdo.

### **Fine-tuning**

Fine-tuning baseia-se na melhoria de um determinado modelo. Não é necessário começar pelo algoritmo do modelo, mas os dados precisam de ser acumulados continuamente. Se pretende uma terminologia e expressão linguística mais precisas nas aplicações industriais, o fine-tuning é a melhor escolha. Contudo, se os seus dados mudam frequentemente, o fine-tuning pode tornar-se complicado.

### **Como escolher**

1. Se a nossa resposta requer a introdução de dados externos, RAG é a melhor escolha

2. Se precisa de fornecer conhecimento industrial estável e preciso, o fine-tuning será uma boa opção. O RAG prioriza a extração de conteúdo relevante, mas pode não captar sempre as nuances especializadas.

3. O fine-tuning requer um conjunto de dados de alta qualidade, e se for apenas um pequeno conjunto de dados, não fará muita diferença. O RAG é mais flexível.

4. O fine-tuning é uma caixa preta, uma metafísica, e é difícil compreender o mecanismo interno. Mas o RAG facilita encontrar a origem dos dados, permitindo ajustar eficazmente alucinações ou erros de conteúdo e oferecendo melhor transparência.

### **Cenários**

1. Indústrias verticais que exigem vocabulário e expressões profissionais específicas, ***Fine-tuning*** será a melhor escolha

2. Sistemas de QA, que envolvem a síntese de diferentes pontos de conhecimento, ***RAG*** será a melhor escolha

3. A combinação de fluxo de negócio automatizado ***RAG + Fine-tuning*** é a melhor escolha

## **Como usar o RAG**

![rag](../../../../translated_images/pt/rag.2014adc59e6f6007.webp)

Uma base de dados vetorial é uma coleção de dados armazenados em forma matemática. Bases de dados vetoriais facilitam que modelos de machine learning recordem entradas anteriores, permitindo que o machine learning suporte casos de uso como pesquisa, recomendações e geração de texto. Os dados podem ser identificados com base em métricas de similaridade em vez de correspondências exatas, permitindo que os modelos computacionais compreendam o contexto dos dados.

A base de dados vetorial é a chave para realizar o RAG. Podemos converter dados em armazenamento vetorial através de modelos vetoriais como text-embedding-3, jina-ai-embedding, etc.

Saiba mais sobre como criar aplicações RAG em [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Como usar o Fine-tuning**

Os algoritmos mais usados no Fine-tuning são Lora e QLora. Como escolher?
- [Saiba mais com este notebook de exemplo](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplo de FineTuning em Python](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora e QLora**

![lora](../../../../translated_images/pt/qlora.e6446c988ee04ca0.webp)

LoRA (Low-Rank Adaptation) e QLoRA (Quantized Low-Rank Adaptation) são técnicas usadas para afinar grandes modelos de linguagem (LLMs) utilizando Parameter Efficient Fine Tuning (PEFT). As técnicas PEFT são desenhadas para treinar modelos de forma mais eficiente do que os métodos tradicionais.  
LoRA é uma técnica de fine-tuning autónoma que reduz a pegada de memória aplicando uma aproximação de baixa ordem à matriz de atualização de pesos. Oferece tempos de treino rápidos e mantém um desempenho próximo dos métodos tradicionais de fine-tuning.

QLoRA é uma versão estendida do LoRA que incorpora técnicas de quantização para reduzir ainda mais o uso de memória. QLoRA quantiza a precisão dos parâmetros de peso no LLM pré-treinado para precisão de 4 bits, o que é mais eficiente em termos de memória do que o LoRA. No entanto, o treino com QLoRA é cerca de 30% mais lento do que com LoRA devido aos passos adicionais de quantização e desquantização.

QLoRA usa LoRA como acessório para corrigir os erros introduzidos durante a quantização. QLoRA permite o fine-tuning de modelos massivos com milhares de milhões de parâmetros em GPUs relativamente pequenas e amplamente disponíveis. Por exemplo, QLoRA pode afinar um modelo de 70B parâmetros que normalmente requer 36 GPUs com apenas 2 GPUs...

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.