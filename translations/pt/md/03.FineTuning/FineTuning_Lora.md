<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:44:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "pt"
}
-->
# **Ajuste fino do Phi-3 com Lora**

Ajuste fino do modelo de linguagem Phi-3 Mini da Microsoft usando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) em um conjunto de dados personalizado de instruções para chat.

LoRA ajudará a melhorar a compreensão das conversas e a geração de respostas.

## Guia passo a passo para ajustar fino o Phi-3 Mini:

**Importações e Configuração**

Instalando loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comece importando as bibliotecas necessárias, como datasets, transformers, peft, trl e torch.
Configure o logging para acompanhar o processo de treinamento.

Você pode optar por adaptar algumas camadas substituindo-as por equivalentes implementados em loralib. Por enquanto, suportamos apenas nn.Linear, nn.Embedding e nn.Conv2d. Também oferecemos suporte ao MergedLinear para casos em que um único nn.Linear representa mais de uma camada, como em algumas implementações da projeção qkv da atenção (veja Notas Adicionais para mais detalhes).

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

Antes do início do loop de treinamento, marque apenas os parâmetros LoRA como treináveis.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Ao salvar um checkpoint, gere um state_dict que contenha somente os parâmetros LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Ao carregar um checkpoint usando load_state_dict, certifique-se de definir strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Agora o treinamento pode prosseguir normalmente.

**Hiperparâmetros**

Defina dois dicionários: training_config e peft_config. training_config inclui hiperparâmetros para o treinamento, como taxa de aprendizado, tamanho do batch e configurações de logging.

peft_config especifica parâmetros relacionados ao LoRA, como rank, dropout e tipo de tarefa.

**Carregamento do Modelo e Tokenizer**

Especifique o caminho para o modelo Phi-3 pré-treinado (exemplo: "microsoft/Phi-3-mini-4k-instruct"). Configure as definições do modelo, incluindo uso de cache, tipo de dado (bfloat16 para precisão mista) e implementação da atenção.

**Treinamento**

Realize o ajuste fino do modelo Phi-3 usando o conjunto de dados personalizado de instruções para chat. Utilize as configurações do LoRA definidas em peft_config para uma adaptação eficiente. Acompanhe o progresso do treinamento usando a estratégia de logging especificada.
Avaliação e Salvamento: Avalie o modelo ajustado.
Salve checkpoints durante o treinamento para uso posterior.

**Exemplos**
- [Saiba mais com este notebook de exemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplo de script de FineTuning em Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemplo de Fine Tuning no Hugging Face Hub com LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemplo de Hugging Face Model Card - Exemplo de Fine Tuning com LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exemplo de Fine Tuning no Hugging Face Hub com QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.