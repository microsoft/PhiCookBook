<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:47:25+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "da"
}
-->
# **Kvantisering af Phi-familien**

Modelkvantisering refererer til processen med at omsætte parametrene (såsom vægte og aktiveringsværdier) i en neuralt netværksmodel fra et stort værdimængdeområde (normalt et kontinuert værdimængdeområde) til et mindre, endeligt værdimængdeområde. Denne teknologi kan reducere modellens størrelse og beregningskompleksitet samt forbedre modellens driftseffektivitet i ressourcebegrænsede miljøer som mobiltelefoner eller indlejrede systemer. Modelkvantisering opnår komprimering ved at reducere præcisionen af parametrene, men det medfører også et vist tab af præcision. Derfor er det nødvendigt at afveje modelstørrelse, beregningskompleksitet og præcision i kvantiseringsprocessen. Almindelige kvantiseringsmetoder inkluderer fastpunktkvantisering, flydende punkt-kvantisering osv. Du kan vælge den passende kvantiseringsstrategi ud fra det konkrete scenarie og behov.

Vi ønsker at implementere GenAI-modeller på edge-enheder og gøre det muligt for flere enheder at indgå i GenAI-scenarier, såsom mobiltelefoner, AI PC/Copilot+PC og traditionelle IoT-enheder. Gennem kvantiserede modeller kan vi implementere dem på forskellige edge-enheder baseret på enhedens type. Kombineret med modelaccelerationsrammer og kvantiserede modeller leveret af hardwareproducenter kan vi opbygge bedre SLM-applikationsscenarier.

I kvantiseringsscenarier har vi forskellige præcisioner (INT4, INT8, FP16, FP32). Nedenfor følger en forklaring af de mest anvendte kvantiseringspræcisioner.

### **INT4**

INT4-kvantisering er en radikal kvantiseringsmetode, der kvantiserer modellens vægte og aktiveringsværdier til 4-bit heltal. INT4-kvantisering resulterer normalt i et større præcisionstab på grund af det mindre repræsentationsområde og lavere præcision. Sammenlignet med INT8-kvantisering kan INT4-kvantisering dog yderligere reducere lagerkrav og beregningskompleksitet. Det skal bemærkes, at INT4-kvantisering er relativt sjælden i praksis, da for lav præcision kan føre til betydelig forringelse af modellens ydeevne. Derudover understøtter ikke al hardware INT4-operationer, så hardwarekompatibilitet skal overvejes ved valg af kvantiseringsmetode.

### **INT8**

INT8-kvantisering er processen med at konvertere en models vægte og aktiveringer fra flydende tal til 8-bit heltal. Selvom det numeriske område, som INT8 heltal repræsenterer, er mindre og mindre præcist, kan det markant reducere lager- og beregningsbehov. Ved INT8-kvantisering gennemgår modellens vægte og aktiveringsværdier en kvantiseringsproces, der inkluderer skalering og offset, for at bevare den oprindelige flydende punkt-information så meget som muligt. Under inferens dekvantiseres disse kvantiserede værdier tilbage til flydende tal til beregning og kvantiseres derefter igen til INT8 til næste trin. Denne metode kan give tilstrækkelig præcision i de fleste anvendelser samtidig med at opretholde høj beregningseffektivitet.

### **FP16**

FP16-formatet, altså 16-bit flydende punkt-tal (float16), halverer hukommelsesforbruget sammenlignet med 32-bit flydende punkt-tal (float32), hvilket giver betydelige fordele i storskala dyb læringsapplikationer. FP16-formatet tillader indlæsning af større modeller eller behandling af mere data inden for de samme GPU-hukommelsesbegrænsninger. Da moderne GPU-hardware fortsat understøtter FP16-operationer, kan brugen af FP16-formatet også medføre forbedringer i beregningshastighed. FP16-formatet har dog også sine iboende ulemper, nemlig lavere præcision, hvilket i visse tilfælde kan føre til numerisk ustabilitet eller tab af præcision.

### **FP32**

FP32-formatet giver højere præcision og kan nøjagtigt repræsentere et bredt spektrum af værdier. I scenarier, hvor komplekse matematiske operationer udføres, eller hvor der kræves resultater med høj præcision, foretrækkes FP32-formatet. Høj præcision betyder dog også større hukommelsesforbrug og længere beregningstid. For storskala dyb læringsmodeller, især når der er mange modelparametre og enorme datamængder, kan FP32-formatet føre til utilstrækkelig GPU-hukommelse eller nedsat inferenshastighed.

På mobile enheder eller IoT-enheder kan vi konvertere Phi-3.x modeller til INT4, mens AI PC / Copilot PC kan bruge højere præcisioner som INT8, FP16, FP32.

I øjeblikket har forskellige hardwareproducenter forskellige rammer til at understøtte generative modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX og Nvidias CUDA osv., kombineret med modelkvantisering for at muliggøre lokal implementering.

Teknologisk set har vi forskelligt formatsupport efter kvantisering, såsom PyTorch / Tensorflow-format, GGUF og ONNX. Jeg har lavet en format sammenligning og anvendelsesscenarier mellem GGUF og ONNX. Her anbefaler jeg ONNX-kvantiseringformatet, som har god understøttelse fra modelrammer til hardware. I dette kapitel vil vi fokusere på ONNX Runtime for GenAI, OpenVINO og Apple MLX til at udføre modelkvantisering (hvis du har en bedre metode, kan du også bidrage ved at indsende en PR).

**Dette kapitel indeholder**

1. [Kvantisering af Phi-3.5 / 4 ved brug af llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantisering af Phi-3.5 / 4 ved brug af Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantisering af Phi-3.5 / 4 ved brug af Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantisering af Phi-3.5 / 4 ved brug af Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.