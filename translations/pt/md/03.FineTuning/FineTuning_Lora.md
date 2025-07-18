<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:31:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "pt"
}
-->
# **Ajuste fino do Phi-3 com Lora**

Ajuste fino do modelo de linguagem Phi-3 Mini da Microsoft usando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) num conjunto de dados personalizado de instruções para chat.

O LORA ajuda a melhorar a compreensão das conversas e a geração de respostas.

## Guia passo a passo para ajustar o Phi-3 Mini:

**Importações e Configuração**

Instalar loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comece por importar as bibliotecas necessárias, como datasets, transformers, peft, trl e torch.  
Configure o logging para acompanhar o processo de treino.

Pode optar por adaptar algumas camadas substituindo-as por equivalentes implementados em loralib. Atualmente, suportamos apenas nn.Linear, nn.Embedding e nn.Conv2d. Também suportamos MergedLinear para casos em que um único nn.Linear representa mais do que uma camada, como em algumas implementações da projeção qkv da atenção (veja Notas Adicionais para mais detalhes).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Antes de começar o ciclo de treino, marque apenas os parâmetros LoRA como treináveis.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Ao guardar um checkpoint, gere um state_dict que contenha apenas os parâmetros LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Ao carregar um checkpoint com load_state_dict, certifique-se de definir strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Agora o treino pode prosseguir normalmente.

**Hiperparâmetros**

Defina dois dicionários: training_config e peft_config. O training_config inclui hiperparâmetros para o treino, como taxa de aprendizagem, tamanho do batch e configurações de logging.

O peft_config especifica parâmetros relacionados ao LoRA, como rank, dropout e tipo de tarefa.

**Carregamento do Modelo e Tokenizer**

Especifique o caminho para o modelo Phi-3 pré-treinado (por exemplo, "microsoft/Phi-3-mini-4k-instruct"). Configure as definições do modelo, incluindo uso de cache, tipo de dados (bfloat16 para precisão mista) e implementação da atenção.

**Treino**

Ajuste fino do modelo Phi-3 usando o conjunto de dados personalizado de instruções para chat. Utilize as definições LoRA do peft_config para uma adaptação eficiente. Monitorize o progresso do treino com a estratégia de logging especificada.  
Avaliação e Guardar: Avalie o modelo ajustado.  
Guarde checkpoints durante o treino para uso posterior.

**Exemplos**  
- [Saiba mais com este notebook de exemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Exemplo de Script Python para Ajuste Fino](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Exemplo de Ajuste Fino no Hugging Face Hub com LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Exemplo de Model Card no Hugging Face - Ajuste Fino com LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Exemplo de Ajuste Fino no Hugging Face Hub com QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.