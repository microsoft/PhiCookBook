## Finjusteringsscenarier

![FineTuning with MS Services](../../../../translated_images/sv/FinetuningwithMS.3d0cec8ae693e094.webp)

Denna sektion ger en översikt över finjusteringsscenarier i Microsoft Foundry och Azure-miljöer, inklusive distributionsmodeller, infrastrukturlager och vanligt använda optimeringstekniker.

**Plattform**  
Detta inkluderar hanterade tjänster såsom Microsoft Foundry (tidigare Microsoft Foundry) och Azure Machine Learning, som tillhandahåller modellhantering, orkestrering, spårning av experiment och distributionsarbetsflöden.

**Infrastruktur**  
Finjustering kräver skalbara datorresurser. I Azure-miljöer inkluderar detta typiskt GPU-baserade virtuella maskiner och CPU-resurser för lättare arbetsbelastningar, tillsammans med skalbar lagring för dataset och kontrollpunkter.

**Verktyg & Ramverk**  
Finjusteringsarbetsflöden förlitar sig ofta på ramverk och optimeringsbibliotek såsom Hugging Face Transformers, DeepSpeed och PEFT (Parameter-Efficient Fine-Tuning).

Finjusteringsprocessen med Microsoft-teknologier spänner över plattformstjänster, datorinfrastruktur och träningsramverk. Genom att förstå hur dessa komponenter samverkar kan utvecklare effektivt anpassa grundmodeller till specifika uppgifter och produktionsscenarier.

## Modell som tjänst

Finjustera modellen med hostad finjustering, utan behov av att skapa och hantera datorresurser.

![MaaS Fine Tuning](../../../../translated_images/sv/MaaSfinetune.3eee4630607aff0d.webp)

Serverlös finjustering är nu tillgänglig för Phi-3, Phi-3.5 och Phi-4 modelfamiljer, vilket gör det möjligt för utvecklare att snabbt och enkelt anpassa modellerna för moln- och kantscenarier utan att behöva ordna datorresurser.

## Modell som plattform

Användare hanterar sina egna datorresurser för att finjustera sina modeller.

![Maap Fine Tuning](../../../../translated_images/sv/MaaPFinetune.fd3829c1122f5d1c.webp)

[Exempel på finjustering](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Jämförelse av finjusteringstekniker

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Anpassa förtränade LLM:er till specifika uppgifter eller domäner|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering för NLP-uppgifter såsom textklassificering, namngiven entitetsigenkänning och maskinöversättning|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering för fråge- och svarsuppgifter|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering för att generera människoliknande svar i chatbots|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering för att skapa musik, konst eller andra former av kreativitet|Ja|Ja|Ja|Ja|Ja|Ja|
|Minska beräkningsmässiga och ekonomiska kostnader|Ja|Ja|Ja|Ja|Ja|Ja|
|Minska minnesanvändning|Ja|Ja|Ja|Ja|Ja|Ja|
|Använda färre parametrar för effektiv finjustering|Ja|Ja|Ja|Nej|Nej|Ja|
|Minneseffektiv form av dataparallellism som ger åtkomst till den aggregerade GPU-minnet från alla tillgängliga GPU-enheter|Nej|Nej|Nej|Ja|Ja|Nej|

> [!NOTE]
> LoRA, QLoRA, PEFT och DoRA är parameter-effektiva finjusteringsmetoder, medan DeepSpeed och ZeRO fokuserar på distribuerad träning och minnesoptimering.

## Exempel på finjusteringsprestanda

![Finetuning Performance](../../../../translated_images/sv/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->