**Finjustering af Phi-3 med QLoRA**

Finjustering af Microsofts sprogmodel Phi-3 Mini ved hjælp af [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA hjælper med at forbedre forståelsen i samtaler og generering af svar.

For at indlæse modeller i 4 bits med transformers og bitsandbytes, skal du installere accelerate og transformers fra kildekoden og sikre, at du har den nyeste version af bitsandbytes-biblioteket.

**Eksempler**
- [Lær mere med denne eksempel-notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Eksempel på Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Eksempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Eksempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.