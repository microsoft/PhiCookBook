<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T12:31:25+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "da"
}
-->
# **Kvantificering af Phi-familien**

Modelkvantisering refererer til processen med at afbilde parametrene (såsom vægte og aktiveringsværdier) i en neuralt netværksmodel fra et stort værdinterval (normalt et kontinuert værdinterval) til et mindre endeligt værdinterval. Denne teknologi kan reducere størrelsen og den beregningsmæssige kompleksitet af modellen og forbedre modellens driftseffektivitet i ressourcebegrænsede miljøer som mobile enheder eller indlejrede systemer. Modelkvantisering opnår komprimering ved at reducere præcisionen af parametrene, men det introducerer også et vist tab af præcision. Derfor er det i kvantiseringsprocessen nødvendigt at balancere modelstørrelse, beregningskompleksitet og præcision. Almindelige kvantiseringsteknikker inkluderer fastpunktkvantisering, flydende punktkvantisering osv. Du kan vælge den passende kvantiseringsstrategi efter den specifikke situation og behov.

Vi håber at implementere GenAI-modeller på edge-enheder og tillade flere enheder at indgå i GenAI-scenarier, såsom mobile enheder, AI PC/Copilot+PC og traditionelle IoT-enheder. Gennem kvantiseringsmodellen kan vi implementere den på forskellige edge-enheder baseret på forskellige enheder. Kombineret med modelaccelerationsrammen og kvantiseringsmodellen, der leveres af hardwareproducenter, kan vi bygge bedre SLM-applikationsscenarier.

I kvantiseringsscenariet har vi forskellige præcisioner (INT4, INT8, FP16, FP32). Følgende er en forklaring af de almindeligt anvendte kvantiseringspræcisioner

### **INT4**

INT4-kvantisering er en radikal kvantiseringsmetode, der kvantiserer vægte og aktiveringsværdier i modellen til 4-bit heltal. INT4-kvantisering resulterer normalt i et større præcisionstab på grund af det mindre repræsentationsområde og lavere præcision. Dog kan INT4-kvantisering sammenlignet med INT8-kvantisering yderligere reducere lagerkrav og beregningskompleksitet for modellen. Det skal bemærkes, at INT4-kvantisering er relativt sjælden i praktiske anvendelser, fordi for lav nøjagtighed kan forårsage betydelig forringelse af modelpræstationen. Derudover understøtter ikke al hardware INT4-operationer, så hardwarekompatibilitet skal overvejes, når kvantiseringsmetode vælges.

### **INT8**

INT8-kvantisering er processen med at konvertere en models vægte og aktiveringer fra flydende punkttal til 8-bit heltal. Selvom det numeriske område repræsenteret af INT8-heltal er mindre og mindre præcist, kan det markant reducere lager- og beregningsbehov. Ved INT8-kvantisering gennemgår modellens vægte og aktiveringsværdier en kvantiseringsproces, inklusive skalering og offset, for at bevare de oprindelige flydende punktoplysninger så meget som muligt. Under inferens vil disse kvantiserede værdier blive dekvantiseret tilbage til flydende punkttal til beregning og derefter kvantiseret tilbage til INT8 til næste trin. Denne metode kan sikre tilstrækkelig nøjagtighed i de fleste applikationer samtidig med høj beregningseffektivitet.

### **FP16**

FP16-formatet, dvs. 16-bit flydende punkttal (float16), reducerer hukommelsesforbruget til det halve sammenlignet med 32-bit flydende punkttal (float32), hvilket har betydelige fordele i storskala dyb læring-applikationer. FP16-formatet tillader indlæsning af større modeller eller behandling af flere data inden for de samme GPU-hukommelsesbegrænsninger. Idet moderne GPU-hardware fortsat understøtter FP16-operationer, kan brugen af FP16-formatet også medføre forbedringer i beregningshastigheden. FP16-formatet har dog også sine iboende ulemper, nemlig lavere præcision, hvilket i nogle tilfælde kan føre til numerisk ustabilitet eller tab af præcision.

### **FP32**

FP32-formatet giver højere præcision og kan nøjagtigt repræsentere et bredt spektrum af værdier. I scenarier, hvor komplekse matematiske operationer udføres, eller hvor der kræves høj præcision, foretrækkes FP32-formatet. Dog indebærer høj præcision også større hukommelsesforbrug og længere beregningstid. For storskala dyb læring-modeller, især når der er mange modelparametre og enorme datamængder, kan FP32-formatet forårsage utilstrækkelig GPU-hukommelse eller et fald i inferenshastigheden.

På mobile enheder eller IoT-enheder kan vi konvertere Phi-3.x modeller til INT4, mens AI PC / Copilot PC kan bruge højere præcision såsom INT8, FP16, FP32.

I øjeblikket har forskellige hardwareproducenter forskellige rammer til at understøtte generative modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX og Nvidias CUDA, mv., kombineret med modelkvantisering til lokal implementering.

Teknologisk set har vi forskellige formatunderstøttelser efter kvantisering, såsom PyTorch / TensorFlow-format, GGUF og ONNX. Jeg har lavet en format sammenligning og applikationsscenarier mellem GGUF og ONNX. Her anbefaler jeg ONNX-kvantiseringformatet, som har god understøttelse fra modelframework til hardware. I dette kapitel vil vi fokusere på ONNX Runtime for GenAI, OpenVINO og Apple MLX til udførelse af modelkvantisering (hvis du har en bedre metode, kan du også give den til os ved at indsende et PR).

**Dette kapitel indeholder**

1. [Kvantificering af Phi-3.5 / 4 ved brug af llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantificering af Phi-3.5 / 4 ved brug af Generative AI-udvidelser for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantificering af Phi-3.5 / 4 ved brug af Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantificering af Phi-3.5 / 4 ved brug af Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog skal betragtes som den autoritative kilde. For kritiske informationer anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->