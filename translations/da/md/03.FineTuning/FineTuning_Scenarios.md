## Finjusteringsscenarier

![Finjustering med MS Services](../../../../translated_images/da/FinetuningwithMS.3d0cec8ae693e094.webp)

**Platform** Dette inkluderer forskellige teknologier såsom Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito og ONNX Runtime.

**Infrastruktur** Dette inkluderer CPU og FPGA, som er essentielle for finjusteringsprocessen. Lad mig vise dig ikonerne for hver af disse teknologier.

**Værktøjer & Framework** Dette inkluderer ONNX Runtime og ONNX Runtime. Lad mig vise dig ikonerne for hver af disse teknologier.  
[Indsæt ikoner for ONNX Runtime og ONNX Runtime]

Finjusteringsprocessen med Microsoft-teknologier involverer forskellige komponenter og værktøjer. Ved at forstå og udnytte disse teknologier kan vi effektivt finjustere vores applikationer og skabe bedre løsninger.

## Model som Service

Finjuster modellen ved hjælp af hosted fine-tuning, uden behov for at oprette og administrere compute.

![MaaS Finjustering](../../../../translated_images/da/MaaSfinetune.3eee4630607aff0d.webp)

Serverløs finjustering er tilgængelig for Phi-3-mini og Phi-3-medium modeller, hvilket gør det muligt for udviklere hurtigt og nemt at tilpasse modellerne til cloud- og edge-scenarier uden at skulle sørge for compute. Vi har også annonceret, at Phi-3-small nu er tilgængelig gennem vores Models-as-a-Service tilbud, så udviklere hurtigt og nemt kan komme i gang med AI-udvikling uden at skulle administrere den underliggende infrastruktur.

## Model som Platform

Brugere administrerer deres eget compute for at finjustere deres modeller.

![Maap Finjustering](../../../../translated_images/da/MaaPFinetune.fd3829c1122f5d1c.webp)

[Finjusterings-eksempel](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Finjusteringsscenarier

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Tilpasning af fortrænede LLM’er til specifikke opgaver eller domæner|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til NLP-opgaver som tekstklassificering, named entity recognition og maskinoversættelse|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til QA-opgaver|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til at generere menneskelignende svar i chatbots|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til at generere musik, kunst eller andre former for kreativitet|Ja|Ja|Ja|Ja|Ja|Ja|
|Reducerer beregnings- og økonomiske omkostninger|Ja|Ja|Nej|Ja|Ja|Nej|
|Reducerer hukommelsesforbrug|Nej|Ja|Nej|Ja|Ja|Ja|
|Brug af færre parametre for effektiv finjustering|Nej|Ja|Ja|Nej|Nej|Ja|
|Hukommelseseffektiv form for dataparallelisme, der giver adgang til den samlede GPU-hukommelse på alle tilgængelige GPU-enheder|Nej|Nej|Nej|Ja|Ja|Ja|

## Eksempler på finjusteringsperformance

![Finjusteringsperformance](../../../../translated_images/da/Finetuningexamples.a9a41214f8f5afc1.webp)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.