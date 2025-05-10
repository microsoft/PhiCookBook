<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:45:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "br"
}
-->
# **Fine-tuning Phi-3 com Lora**

Fine-tuning do modelo de linguagem Phi-3 Mini da Microsoft usando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) em um conjunto de dados personalizado de instruções para chat.

O LORA ajuda a melhorar a compreensão da conversa e a geração de respostas.

## Guia passo a passo para fine-tunar o Phi-3 Mini:

**Imports e Configuração**

Instalando loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comece importando as bibliotecas necessárias, como datasets, transformers, peft, trl e torch.  
Configure o logging para acompanhar o processo de treinamento.

Você pode optar por adaptar algumas camadas substituindo-as por equivalentes implementados em loralib. Atualmente, suportamos apenas nn.Linear, nn.Embedding e nn.Conv2d. Também oferecemos suporte ao MergedLinear para casos em que um único nn.Linear representa mais de uma camada, como em algumas implementações da projeção qkv de atenção (veja Notas Adicionais para mais detalhes).

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

Antes de iniciar o loop de treinamento, marque apenas os parâmetros do LoRA como treináveis.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Ao salvar um checkpoint, gere um state_dict que contenha somente os parâmetros do LoRA.

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

Agora o treinamento pode prosseguir normalmente.

**Hiperparâmetros**

Defina dois dicionários: training_config e peft_config. O training_config inclui hiperparâmetros para o treinamento, como taxa de aprendizado, tamanho do batch e configurações de logging.

O peft_config especifica parâmetros relacionados ao LoRA, como rank, dropout e tipo de tarefa.

**Carregamento do Modelo e Tokenizer**

Especifique o caminho para o modelo pré-treinado Phi-3 (exemplo: "microsoft/Phi-3-mini-4k-instruct"). Configure as opções do modelo, incluindo uso de cache, tipo de dado (bfloat16 para precisão mista) e implementação da atenção.

**Treinamento**

Faça o fine-tuning do modelo Phi-3 usando o conjunto de dados personalizado de instruções para chat. Utilize as configurações do LoRA definidas no peft_config para uma adaptação eficiente. Monitore o progresso do treinamento usando a estratégia de logging especificada.

Avaliação e Salvamento: Avalie o modelo fine-tunado.  
Salve checkpoints durante o treinamento para uso posterior.

**Exemplos**  
- [Saiba Mais com este notebook de exemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Exemplo de Script Python para FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Exemplo de Fine Tuning no Hugging Face Hub com LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Exemplo de Model Card no Hugging Face - Fine Tuning com LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Exemplo de Fine Tuning no Hugging Face Hub com QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.