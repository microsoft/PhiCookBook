<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:19:09+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "sv"
}
-->
**Finjustering av Phi-3 med QLoRA**

Finjustering av Microsofts språkmodell Phi-3 Mini med hjälp av [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA hjälper till att förbättra förståelsen i konversationer och generering av svar.

För att ladda modeller i 4 bitar med transformers och bitsandbytes måste du installera accelerate och transformers från källkod och se till att du har den senaste versionen av bitsandbytes-biblioteket.

**Exempel**
- [Lär dig mer med detta exempel på notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exempel på Python FineTuning-exempel](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.