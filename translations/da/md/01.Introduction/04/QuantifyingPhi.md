<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:29:02+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "da"
}
-->
# **Kvantisering af Phi-familien**

Modelkvantisering refererer til processen med at omsætte parametrene (såsom vægte og aktiveringsværdier) i en neuralt netværksmodel fra et stort værdierum (normalt et kontinuert værdierum) til et mindre, endeligt værdierum. Denne teknologi kan reducere modellens størrelse og beregningskompleksitet samt forbedre modellens driftsmæssige effektivitet i ressourcebegrænsede miljøer som mobiltelefoner eller indlejrede systemer. Modelkvantisering opnår komprimering ved at reducere præcisionen af parametrene, men det medfører også et vist tab af præcision. Derfor er det nødvendigt at finde en balance mellem modelstørrelse, beregningskompleksitet og præcision i kvantiseringsprocessen. Almindelige kvantiseringsmetoder inkluderer fastpunktkvantisering, flydende punktkvantisering osv. Du kan vælge den passende kvantiseringsstrategi ud fra det specifikke scenarie og behov.

Vi ønsker at implementere GenAI-modellen på edge-enheder og lade flere enheder indgå i GenAI-scenarier, såsom mobiltelefoner, AI PC/Copilot+PC og traditionelle IoT-enheder. Gennem kvantiseringsmodellen kan vi implementere den på forskellige edge-enheder baseret på enhedstype. Kombineret med modelaccelerationsrammen og kvantiseringsmodellen leveret af hardwareproducenter kan vi skabe bedre SLM-applikationsscenarier.

I kvantiseringsscenariet har vi forskellige præcisioner (INT4, INT8, FP16, FP32). Følgende er en forklaring på de mest anvendte kvantiseringspræcisioner.

### **INT4**

INT4-kvantisering er en radikal kvantiseringsmetode, der kvantiserer modellens vægte og aktiveringsværdier til 4-bit heltal. INT4-kvantisering medfører normalt et større præcisionstab på grund af det mindre repræsentationsområde og lavere præcision. Sammenlignet med INT8-kvantisering kan INT4 dog yderligere reducere lagringsbehov og beregningskompleksitet. Det skal bemærkes, at INT4-kvantisering er relativt sjælden i praksis, da for lav præcision kan føre til betydelig forringelse af modellens ydeevne. Desuden understøtter ikke al hardware INT4-operationer, så hardwarekompatibilitet skal tages i betragtning ved valg af kvantiseringsmetode.

### **INT8**

INT8-kvantisering er processen, hvor modellens vægte og aktiveringer konverteres fra flydende tal til 8-bit heltal. Selvom det numeriske område, som INT8 heltal repræsenterer, er mindre og mindre præcist, kan det markant reducere lagrings- og beregningsbehov. I INT8-kvantisering gennemgår modellens vægte og aktiveringsværdier en kvantiseringsproces, der inkluderer skalering og offset, for så vidt muligt at bevare den oprindelige flydende tal-information. Under inferens dekvantiseres disse kvantiserede værdier tilbage til flydende tal for beregning og kvantiseres derefter igen til INT8 til næste trin. Denne metode kan give tilstrækkelig præcision i de fleste anvendelser samtidig med at opretholde høj beregningseffektivitet.

### **FP16**

FP16-formatet, altså 16-bit flydende tal (float16), halverer hukommelsesforbruget sammenlignet med 32-bit flydende tal (float32), hvilket har betydelige fordele i store dybdelæringsapplikationer. FP16-formatet tillader at indlæse større modeller eller behandle mere data inden for de samme GPU-hukommelsesbegrænsninger. Efterhånden som moderne GPU-hardware fortsat understøtter FP16-operationer, kan brug af FP16-formatet også medføre forbedringer i beregningshastighed. Dog har FP16-formatet også sine iboende ulemper, nemlig lavere præcision, hvilket i nogle tilfælde kan føre til numerisk ustabilitet eller præcisionstab.

### **FP32**

FP32-formatet giver højere præcision og kan nøjagtigt repræsentere et bredt spektrum af værdier. I scenarier, hvor der udføres komplekse matematiske operationer, eller hvor der kræves resultater med høj præcision, foretrækkes FP32-formatet. Dog betyder høj præcision også større hukommelsesforbrug og længere beregningstid. For store dybdelæringsmodeller, især når der er mange modelparametre og store datamængder, kan FP32-formatet føre til utilstrækkelig GPU-hukommelse eller nedsat inferenshastighed.

På mobile enheder eller IoT-enheder kan vi konvertere Phi-3.x modeller til INT4, mens AI PC / Copilot PC kan bruge højere præcisioner som INT8, FP16 og FP32.

I øjeblikket har forskellige hardwareproducenter forskellige rammer til at understøtte generative modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX og Nvidias CUDA, kombineret med modelkvantisering for at fuldføre lokal implementering.

Teknologisk set har vi forskellige formatunderstøttelser efter kvantisering, såsom PyTorch / Tensorflow-format, GGUF og ONNX. Jeg har lavet en formatformsammenligning og anvendelsesscenarier mellem GGUF og ONNX. Her anbefaler jeg ONNX-kvantiseringsformatet, som har god understøttelse fra modelrammen til hardwaren. I dette kapitel fokuserer vi på ONNX Runtime for GenAI, OpenVINO og Apple MLX til at udføre modelkvantisering (hvis du har en bedre metode, kan du også bidrage ved at indsende en PR).

**Dette kapitel indeholder**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.