<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:30+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "da"
}
-->
**Finjustering af Phi-3 med QLoRA**

Finjustering af Microsofts sprogmodel Phi-3 Mini ved hjælp af [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA hjælper med at forbedre samtaleforståelse og generering af svar.

For at indlæse modeller i 4 bits med transformers og bitsandbytes, skal du installere accelerate og transformers fra kilden og sikre, at du har den nyeste version af bitsandbytes-biblioteket.

**Eksempler**
- [Lær mere med dette eksempel-notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Eksempel på Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Eksempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Eksempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.