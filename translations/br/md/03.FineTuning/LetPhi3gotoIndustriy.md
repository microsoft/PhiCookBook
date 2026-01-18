<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:55:54+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "br"
}
-->
# **Deixe o Phi-3 se tornar um especialista da indústria**

Para aplicar o modelo Phi-3 em um setor industrial, é necessário adicionar dados comerciais específicos da indústria ao modelo Phi-3. Temos duas opções diferentes: a primeira é RAG (Retrieval Augmented Generation) e a segunda é Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG é a combinação de recuperação de dados + geração de texto. Os dados estruturados e não estruturados da empresa são armazenados no banco de dados vetorial. Ao buscar conteúdo relevante, o resumo e o conteúdo relacionados são encontrados para formar um contexto, e a capacidade de conclusão de texto do LLM/SLM é combinada para gerar o conteúdo.

### **Fine-tuning**

Fine-tuning é baseado na melhoria de um modelo específico. Não é necessário começar pelo algoritmo do modelo, mas os dados precisam ser acumulados continuamente. Se você deseja uma terminologia e expressão linguística mais precisas em aplicações industriais, fine-tuning é a melhor escolha. Porém, se seus dados mudam com frequência, o fine-tuning pode se tornar complicado.

### **Como escolher**

1. Se nossa resposta requer a introdução de dados externos, RAG é a melhor escolha

2. Se você precisa de uma saída estável e precisa de conhecimento específico da indústria, fine-tuning será uma boa opção. RAG prioriza puxar conteúdo relevante, mas pode não capturar sempre as nuances especializadas.

3. Fine-tuning exige um conjunto de dados de alta qualidade, e se for apenas um pequeno conjunto de dados, não fará muita diferença. RAG é mais flexível.

4. Fine-tuning é uma caixa preta, uma espécie de metafísica, e é difícil entender seu mecanismo interno. Já o RAG facilita encontrar a origem dos dados, permitindo ajustar de forma eficaz alucinações ou erros de conteúdo e oferecendo melhor transparência.

### **Cenários**

1. Indústrias verticais que exigem vocabulário e expressões profissionais específicas, ***Fine-tuning*** será a melhor escolha

2. Sistema de perguntas e respostas, envolvendo a síntese de diferentes pontos de conhecimento, ***RAG*** será a melhor escolha

3. A combinação de fluxo de negócios automatizado ***RAG + Fine-tuning*** é a melhor escolha

## **Como usar RAG**

![rag](../../../../translated_images/br/rag.2014adc59e6f6007.webp)

Um banco de dados vetorial é uma coleção de dados armazenados em forma matemática. Bancos de dados vetoriais facilitam que modelos de aprendizado de máquina lembrem entradas anteriores, permitindo que o aprendizado de máquina seja usado para suportar casos de uso como busca, recomendações e geração de texto. Os dados podem ser identificados com base em métricas de similaridade, em vez de correspondências exatas, permitindo que os modelos computacionais entendam o contexto dos dados.

O banco de dados vetorial é a chave para realizar o RAG. Podemos converter dados em armazenamento vetorial por meio de modelos vetoriais como text-embedding-3, jina-ai-embedding, etc.

Saiba mais sobre como criar uma aplicação RAG em [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Como usar Fine-tuning**

Os algoritmos mais usados em Fine-tuning são Lora e QLora. Como escolher?
- [Saiba mais com este notebook de exemplo](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplo de FineTuning em Python](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora e QLora**

![lora](../../../../translated_images/br/qlora.e6446c988ee04ca0.webp)

LoRA (Low-Rank Adaptation) e QLoRA (Quantized Low-Rank Adaptation) são técnicas usadas para fine-tuning de grandes modelos de linguagem (LLMs) utilizando Parameter Efficient Fine Tuning (PEFT). Técnicas PEFT são projetadas para treinar modelos de forma mais eficiente do que métodos tradicionais.  
LoRA é uma técnica de fine-tuning independente que reduz o uso de memória aplicando uma aproximação de baixa ordem à matriz de atualização de pesos. Oferece tempos de treinamento rápidos e mantém desempenho próximo aos métodos tradicionais de fine-tuning.

QLoRA é uma versão estendida do LoRA que incorpora técnicas de quantização para reduzir ainda mais o uso de memória. QLoRA quantiza a precisão dos parâmetros de peso no LLM pré-treinado para precisão de 4 bits, o que é mais eficiente em memória do que LoRA. No entanto, o treinamento com QLoRA é cerca de 30% mais lento que o LoRA devido às etapas adicionais de quantização e desquantização.

QLoRA usa LoRA como um acessório para corrigir os erros introduzidos durante a quantização. QLoRA permite o fine-tuning de modelos massivos com bilhões de parâmetros em GPUs relativamente pequenas e disponíveis. Por exemplo, QLoRA pode fazer fine-tuning de um modelo de 70 bilhões de parâmetros que normalmente exigiria 36 GPUs, usando apenas 2 GPUs.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.