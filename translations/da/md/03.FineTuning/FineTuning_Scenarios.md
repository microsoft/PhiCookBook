## Fine Tuning Scenarier

![FineTuning med MS Services](../../../../translated_images/da/FinetuningwithMS.3d0cec8ae693e094.webp)

Dette afsnit giver en oversigt over fine-tuning scenarier i Microsoft Foundry og Azure-miljøer, herunder implementeringsmodeller, infrastrukturlag og ofte anvendte optimeringsteknikker.

**Platform**  
Dette omfatter administrerede tjenester såsom Microsoft Foundry (tidligere Azure AI Foundry) og Azure Machine Learning, som leverer modelstyring, orkestrering, eksperimentsporing og udrulningsarbejdsgange.

**Infrastruktur**  
Fine-tuning kræver skalerbare beregningsressourcer. I Azure-miljøer inkluderer dette typisk GPU-baserede virtuelle maskiner og CPU-ressourcer til letvægts arbejdsbelastninger, sammen med skalerbar lagring til datasæt og checkpoints.

**Værktøjer & Framework**  
Fine-tuning arbejdsgange er almindeligvis baseret på frameworks og optimeringsbiblioteker som Hugging Face Transformers, DeepSpeed og PEFT (Parameter-Efficient Fine-Tuning).

Fine-tuning processen med Microsoft teknologier spænder over platformstjenester, compute infrastruktur og træningsframeworks. Ved at forstå hvordan disse komponenter arbejder sammen, kan udviklere effektivt tilpasse fundamentmodeller til specifikke opgaver og produktionsscenarier.

## Model som Service

Finjuster modellen ved hjælp af hostet fine-tuning, uden behov for at oprette og administrere compute.

![MaaS Fine Tuning](../../../../translated_images/da/MaaSfinetune.3eee4630607aff0d.webp)

Serverløs fine-tuning er nu tilgængelig for Phi-3, Phi-3.5 og Phi-4 modelserier, hvilket gør det muligt for udviklere hurtigt og nemt at tilpasse modellerne til sky- og edge scenarier uden at skulle arrangere compute.

## Model som en Platform

Brugere administrerer deres eget compute for at finjustere deres modeller.

![Maap Fine Tuning](../../../../translated_images/da/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Eksempel](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Sammenligning af Fine-Tuning Teknikker

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Tilpasning af fortrænede LLM’er til specifikke opgaver eller domæner|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til NLP-opgaver såsom tekstklassificering, navngiven entitetsgenkendelse og maskinoversættelse|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til QA-opgaver|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til at generere menneskelignende svar i chatbots|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering til at generere musik, kunst eller andre former for kreativitet|Ja|Ja|Ja|Ja|Ja|Ja|
|Reducerer beregnings- og finansielle omkostninger|Ja|Ja|Ja|Ja|Ja|Ja|
|Reducerer hukommelsesforbrug|Ja|Ja|Ja|Ja|Ja|Ja|
|Bruger færre parametre for effektiv finjustering|Ja|Ja|Ja|Nej|Nej|Ja|
|Hukommelseseffektiv form for data-parallelisme, der giver adgang til den samlede GPU-hukommelse af alle tilgængelige GPU-enheder|Nej|Nej|Nej|Ja|Ja|Nej|

> [!NOTE]
> LoRA, QLoRA, PEFT og DoRA er parametereffektive fine-tuning metoder, mens DeepSpeed og ZeRO fokuserer på distribueret træning og hukommelsesoptimering.

## Eksempler på Fine Tuning Ydeevne

![Finetuning Performance](../../../../translated_images/da/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For væsentlige oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->