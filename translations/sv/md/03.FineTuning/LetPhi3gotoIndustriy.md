<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-05-09T22:27:12+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "sv"
}
-->
# **Låt Phi-3 bli en branschexpert**

För att använda Phi-3-modellen inom en bransch behöver du lägga till branschspecifika affärsdata till Phi-3-modellen. Vi har två olika alternativ, det första är RAG (Retrieval Augmented Generation) och det andra är Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG är datainhämtning + textgenerering. Den strukturerade och ostrukturerade datan från företaget lagras i en vektordatabas. När man söker efter relevant innehåll hittas relevanta sammanfattningar och innehåll för att skapa en kontext, och textkompletteringsfunktionen i LLM/SLM kombineras för att generera innehåll.

### **Fine-tuning**

Fine-tuning bygger på förbättring av en viss modell. Det kräver inte att man börjar från modellalgoritmen, men data behöver kontinuerligt samlas in. Om du vill ha mer exakt terminologi och språklig uttrycksform i branschapplikationer är fine-tuning ett bättre val. Men om din data förändras ofta kan fine-tuning bli komplicerat.

### **Hur man väljer**

1. Om vårt svar kräver införande av extern data är RAG det bästa valet.

2. Om du behöver leverera stabil och exakt branschkunskap är fine-tuning ett bra val. RAG prioriterar att hämta relevant innehåll men fångar inte alltid de specialiserade nyanserna.

3. Fine-tuning kräver en högkvalitativ datamängd, och om det bara är ett litet dataområde gör det inte så stor skillnad. RAG är mer flexibelt.

4. Fine-tuning är en svart låda, en metafysik, och det är svårt att förstå den interna mekanismen. Men RAG gör det lättare att hitta datakällan, vilket effektivt kan justera hallucinationer eller innehållsfel och ger bättre transparens.

### **Scenarier**

1. Vertikala branscher som kräver specifik professionell vokabulär och uttryck, ***Fine-tuning*** är det bästa valet.

2. QA-system som involverar syntes av olika kunskapspunkter, ***RAG*** är det bästa valet.

3. Kombinationen av automatiserade affärsflöden, ***RAG + Fine-tuning*** är det bästa valet.

## **Hur man använder RAG**

![rag](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.sv.png)

En vektordatabas är en samling data lagrad i matematisk form. Vektordatabaser gör det enklare för maskininlärningsmodeller att minnas tidigare indata, vilket möjliggör användning av maskininlärning för tillämpningar som sökning, rekommendationer och textgenerering. Data kan identifieras baserat på likhetsmått snarare än exakta matchningar, vilket gör att datorer kan förstå datans kontext.

Vektordatabasen är nyckeln för att realisera RAG. Vi kan konvertera data till vektorlagring via vektormodeller som text-embedding-3, jina-ai-embedding, etc.

Läs mer om hur man skapar RAG-applikationer på [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Hur man använder Fine-tuning**

De vanligaste algoritmerna inom Fine-tuning är Lora och QLora. Hur väljer man?

- [Lär dig mer med detta exempel på notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exempel på Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora och QLora**

![lora](../../../../translated_images/qlora.6aeba71122bc0c8d56ccf0bc36b861304939fee087f43c1fc6cc5c9cb8764725.sv.png)

LoRA (Low-Rank Adaptation) och QLoRA (Quantized Low-Rank Adaptation) är båda tekniker som används för att finjustera stora språkmodeller (LLMs) med Parameter Efficient Fine Tuning (PEFT). PEFT-tekniker är designade för att träna modeller mer effektivt än traditionella metoder.

LoRA är en fristående finjusteringsteknik som minskar minnesanvändningen genom att tillämpa en låg-rankad approximation på viktuppdateringsmatrisen. Det erbjuder snabba träningstider och bibehåller prestanda nära traditionella finjusteringsmetoder.

QLoRA är en utökad version av LoRA som integrerar kvantiseringstekniker för att ytterligare minska minnesanvändningen. QLoRA kvantiserar precisionen på viktparametrarna i den förtränade LLM:n till 4-bitars precision, vilket är mer minneseffektivt än LoRA. Dock är QLoRA-träningen cirka 30 % långsammare än LoRA på grund av de extra kvantiserings- och dekvantiseringsstegen.

QLoRA använder LoRA som ett tillägg för att korrigera de fel som introduceras under kvantiseringsprocessen. QLoRA möjliggör finjustering av enorma modeller med miljarder parametrar på relativt små, lättillgängliga GPU:er. Till exempel kan QLoRA finjustera en 70B-parametermodell som normalt kräver 36 GPU:er med endast 2.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.