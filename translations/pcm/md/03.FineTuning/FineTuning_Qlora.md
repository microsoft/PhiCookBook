<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-12-21T17:17:05+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "pcm"
}
-->
**Fine-tuning Phi-3 wit QLoRA**

We dey fine-tune Microsoft’s Phi-3 Mini language model using [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora). 

QLoRA go help improve how the model dey understand conversations and how e dey generate responses. 

If you wan load models for 4bits with transformers and bitsandbytes, you must install accelerate and transformers from source and make sure say you get the latest version of the bitsandbytes library.

**Samples**
- [Learn More with this sample notebook](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document na AI dem use translate — dem use Co-op Translator (https://github.com/Azure/co-op-translator). Even though we try make am correct, abeg note say automated translation fit get mistakes or no too accurate. The original document for dia own language na di authoritative source. If na important information, make person wey sabi human professional translator check am. We no dey liable for any misunderstanding or wrong interpretation wey fit come from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->