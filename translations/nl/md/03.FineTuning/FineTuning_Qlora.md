<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:46+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "nl"
}
-->
**Fijn afstemmen van Phi-3 met QLoRA**

Fijn afstemmen van Microsoft’s Phi-3 Mini taalmodel met behulp van [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA helpt bij het verbeteren van het begrip in gesprekken en het genereren van reacties.

Om modellen in 4bits te laden met transformers en bitsandbytes, moet je accelerate en transformers vanuit de bron installeren en ervoor zorgen dat je de nieuwste versie van de bitsandbytes-bibliotheek hebt.

**Voorbeelden**
- [Leer meer met dit voorbeeldnotebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Voorbeeld van Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Voorbeeld van Hugging Face Hub Fine Tuning met LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Voorbeeld van Hugging Face Hub Fine Tuning met QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.