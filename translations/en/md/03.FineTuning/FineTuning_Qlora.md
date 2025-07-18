<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "en"
}
-->
**Fine-tuning Phi-3 with QLoRA**

Fine-tuning Microsoft’s Phi-3 Mini language model using [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA helps enhance conversational understanding and response generation.

To load models in 4bits with transformers and bitsandbytes, you need to install accelerate and transformers from source and ensure you have the latest version of the bitsandbytes library.

**Samples**
- [Learn More with this sample notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.