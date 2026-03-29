## Fine Tuning Scenario's

![FineTuning with MS Services](../../../../translated_images/nl/FinetuningwithMS.3d0cec8ae693e094.webp)

Deze sectie biedt een overzicht van fine-tuning scenario's in Microsoft Foundry en Azure-omgevingen, inclusief implementatiemodellen, infrastructuurlagen en veelgebruikte optimalisatietechnieken.

**Platform**  
Dit omvat beheerde diensten zoals Microsoft Foundry (voorheen Microsoft Foundry) en Azure Machine Learning, die modelbeheer, orkestratie, experimenttracking en implementatieworkflows bieden.

**Infrastructuur**  
Fine-tuning vereist schaalbare rekenresources. In Azure-omgevingen omvat dit doorgaans GPU-gebaseerde virtuele machines en CPU-resources voor lichte workloads, samen met schaalbare opslag voor datasets en checkpoints.

**Tools & Framework**  
Fine-tuning workflows vertrouwen vaak op frameworks en optimalisatiebibliotheken zoals Hugging Face Transformers, DeepSpeed en PEFT (Parameter-Efficient Fine-Tuning).

Het fine-tuning proces met Microsoft-technologieën beslaat platformdiensten, compute-infrastructuur en trainingsframeworks. Door te begrijpen hoe deze componenten samenwerken, kunnen ontwikkelaars foundation models efficiënt aanpassen aan specifieke taken en productieomgevingen.

## Model as Service

Fijn afstemmen van het model met gehoste fine-tuning, zonder dat compute hoeft te worden gecreëerd of beheerd.

![MaaS Fine Tuning](../../../../translated_images/nl/MaaSfinetune.3eee4630607aff0d.webp)

Serverless fine-tuning is nu beschikbaar voor Phi-3, Phi-3.5 en Phi-4 modelfamilies, waarmee ontwikkelaars de modellen snel en eenvoudig kunnen aanpassen voor cloud- en edge-scenario's zonder zelf compute te regelen.

## Model as a Platform

Gebruikers beheren hun eigen compute om hun modellen te fine-tunen.

![Maap Fine Tuning](../../../../translated_images/nl/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Vergelijking van Fine-Tuning Technieken

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Aanpassen van voorgetrainde LLM's aan specifieke taken of domeinen|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-tuning voor NLP-taken zoals tekstclassificatie, named entity recognition en machinevertaling|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-tuning voor QA-taken|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-tuning voor het genereren van mensachtige antwoorden in chatbots|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-tuning voor het genereren van muziek, kunst of andere vormen van creativiteit|Ja|Ja|Ja|Ja|Ja|Ja|
|Verminderen van computationele en financiële kosten|Ja|Ja|Ja|Ja|Ja|Ja|
|Verminderen van geheugengebruik|Ja|Ja|Ja|Ja|Ja|Ja|
|Gebruik van minder parameters voor efficiënte fine-tuning|Ja|Ja|Ja|Nee|Nee|Ja|
|Geheugenefficiënte vorm van dataparallelisme die toegang geeft tot het totale GPU-geheugen van alle beschikbare GPU-apparaten|Nee|Nee|Nee|Ja|Ja|Nee|

> [!NOTE]
> LoRA, QLoRA, PEFT en DoRA zijn parameter-efficiënte fine-tuning methoden, terwijl DeepSpeed en ZeRO zich richten op gedistribueerde training en geheugenoptimalisatie.

## Voorbeelden van Fine Tuning Prestaties

![Finetuning Performance](../../../../translated_images/nl/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->