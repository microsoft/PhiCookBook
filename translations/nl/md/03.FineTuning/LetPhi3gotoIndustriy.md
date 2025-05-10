<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-05-09T22:27:58+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "nl"
}
-->
# **Laat Phi-3 een industrie-expert worden**

Om het Phi-3 model in een industrie toe te passen, moet je bedrijfsspecifieke data aan het Phi-3 model toevoegen. We hebben twee verschillende opties: de eerste is RAG (Retrieval Augmented Generation) en de tweede is Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG is data-ophaling + tekstgeneratie. De gestructureerde en ongestructureerde data van het bedrijf worden opgeslagen in de vector database. Bij het zoeken naar relevante inhoud worden de relevante samenvatting en content gevonden om een context te vormen, en wordt de tekstvervolgcapaciteit van LLM/SLM gecombineerd om content te genereren.

### **Fine-tuning**

Fine-tuning is gebaseerd op het verbeteren van een bepaald model. Het hoeft niet te beginnen bij het modelalgoritme, maar data moet wel continu worden verzameld. Wil je nauwkeurigere terminologie en taalgebruik in industriële toepassingen, dan is fine-tuning de betere keuze. Maar als je data vaak verandert, kan fine-tuning ingewikkeld worden.

### **Hoe te kiezen**

1. Als ons antwoord externe data moet bevatten, is RAG de beste keuze.

2. Als je stabiele en precieze industriële kennis wilt outputten, is fine-tuning een goede optie. RAG haalt relevante content op, maar raakt niet altijd de gespecialiseerde nuances precies.

3. Fine-tuning vereist een hoogwaardige dataset, en als het maar om een klein datagebied gaat, maakt het weinig verschil. RAG is flexibeler.

4. Fine-tuning is een black box, een soort metafysica, en het is moeilijk om het interne mechanisme te begrijpen. Maar RAG maakt het makkelijker om de bron van de data te vinden, waardoor hallucinaties of fouten in de content effectiever kunnen worden bijgesteld en er betere transparantie is.

### **Scenario's**

1. Verticale industrieën die specifieke vaktermen en uitdrukkingen vereisen, ***Fine-tuning*** is dan de beste keuze.

2. QA-systemen die verschillende kennispunten combineren, ***RAG*** is dan de beste keuze.

3. De combinatie van geautomatiseerde bedrijfsprocessen, ***RAG + Fine-tuning*** is de beste keuze.

## **Hoe RAG te gebruiken**

![rag](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.nl.png)

Een vector database is een verzameling data die in wiskundige vorm is opgeslagen. Vector databases maken het makkelijker voor machine learning modellen om eerdere input te onthouden, waardoor machine learning kan worden ingezet voor toepassingen zoals zoeken, aanbevelingen en tekstgeneratie. Data kan worden herkend op basis van gelijkenis in plaats van exacte overeenkomsten, waardoor computermodellen de context van de data beter begrijpen.

De vector database is de sleutel tot het realiseren van RAG. We kunnen data omzetten naar vectoropslag via vector modellen zoals text-embedding-3, jina-ai-embedding, enz.

Lees meer over het maken van RAG applicaties [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Hoe Fine-tuning te gebruiken**

De meest gebruikte algoritmes bij Fine-tuning zijn Lora en QLora. Hoe kies je?
- [Leer meer met deze voorbeeldnotebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Voorbeeld van Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora en QLora**

![lora](../../../../translated_images/qlora.6aeba71122bc0c8d56ccf0bc36b861304939fee087f43c1fc6cc5c9cb8764725.nl.png)

LoRA (Low-Rank Adaptation) en QLoRA (Quantized Low-Rank Adaptation) zijn technieken die gebruikt worden om grote taalmodellen (LLM's) te fine-tunen met behulp van Parameter Efficient Fine Tuning (PEFT). PEFT-technieken zijn ontworpen om modellen efficiënter te trainen dan traditionele methoden.  
LoRA is een op zichzelf staande fine-tuning techniek die het geheugengebruik vermindert door een low-rank benadering toe te passen op de gewicht-update matrix. Het biedt snelle trainingstijden en behoudt prestaties die dicht bij traditionele fine-tuning methoden liggen.

QLoRA is een uitgebreide versie van LoRA die quantisatietechnieken gebruikt om het geheugengebruik nog verder te verminderen. QLoRA quantiseert de precisie van de gewichtparameters in het voorgetrainde LLM naar 4-bit precisie, wat efficiënter is dan LoRA. QLoRA training is echter ongeveer 30% langzamer dan LoRA vanwege de extra quantisatie- en dequantisatiestappen.

QLoRA gebruikt LoRA als aanvulling om fouten die tijdens quantisatie ontstaan te corrigeren. QLoRA maakt het mogelijk om enorme modellen met miljarden parameters te fine-tunen op relatief kleine, breed beschikbare GPU’s. Bijvoorbeeld, QLoRA kan een 70B parameter model fine-tunen dat normaal 36 GPU’s vereist met slechts 2.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.