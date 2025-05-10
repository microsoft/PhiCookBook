<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:35+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "no"
}
-->
**Finjustering av Phi-3 med QLoRA**

Finjustering av Microsofts Phi-3 Mini språkmodell ved hjelp av [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA vil bidra til å forbedre samtaleforståelse og generering av svar.

For å laste modeller i 4 bits med transformers og bitsandbytes, må du installere accelerate og transformers fra kildekoden, og sørge for at du har den nyeste versjonen av bitsandbytes-biblioteket.

**Eksempler**
- [Lær mer med dette eksempel-notatboken](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Eksempel på Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Eksempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Eksempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.