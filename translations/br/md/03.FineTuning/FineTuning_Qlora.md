<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:18:27+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "br"
}
-->
**Ajuste fino do Phi-3 com QLoRA**

Ajuste fino do modelo de linguagem Phi-3 Mini da Microsoft usando [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

O QLoRA ajuda a melhorar a compreensão em conversas e a geração de respostas.

Para carregar modelos em 4 bits com transformers e bitsandbytes, é necessário instalar accelerate e transformers a partir do código-fonte e garantir que você tenha a versão mais recente da biblioteca bitsandbytes.

**Exemplos**
- [Saiba mais com este notebook de exemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplo de script Python para FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemplo de Fine Tuning no Hugging Face Hub com LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemplo de Fine Tuning no Hugging Face Hub com QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.