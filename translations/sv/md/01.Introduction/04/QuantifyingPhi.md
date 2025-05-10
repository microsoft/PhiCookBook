<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:28:23+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sv"
}
-->
# **Kvantifiering av Phi-familjen**

Modellkvantisering avser processen att kartlägga parametrarna (såsom vikter och aktiveringsvärden) i en neuralt nätverksmodell från ett stort värdeintervall (vanligtvis ett kontinuerligt värdeintervall) till ett mindre ändligt värdeintervall. Denna teknik kan minska modellens storlek och beräkningskomplexitet samt förbättra modellens driftseffektivitet i resursbegränsade miljöer som mobila enheter eller inbäddade system. Modellkvantisering uppnår komprimering genom att minska precisionen på parametrarna, men det medför också en viss precisionförlust. Därför är det viktigt att i kvantiseringsprocessen balansera modellstorlek, beräkningskomplexitet och precision. Vanliga kvantiseringsmetoder inkluderar fastpunktkvantisering, flyttalskvantisering med mera. Du kan välja lämplig kvantiseringsstrategi beroende på specifikt scenario och behov.

Vi hoppas kunna distribuera GenAI-modeller till edge-enheter och möjliggöra för fler enheter att ingå i GenAI-scenarier, såsom mobila enheter, AI PC/Copilot+PC och traditionella IoT-enheter. Genom kvantiserade modeller kan vi distribuera dem till olika edge-enheter baserat på deras specifikationer. Tillsammans med modellacceleration och kvantiseringsmodeller från hårdvarutillverkare kan vi bygga bättre SLM-applikationsscenarier.

I kvantiseringsscenarier finns olika precisioner (INT4, INT8, FP16, FP32). Nedan följer en förklaring av de vanligaste kvantiseringsprecisionerna.

### **INT4**

INT4-kvantisering är en extrem kvantiseringsmetod som kvantiserar modellens vikter och aktiveringsvärden till 4-bitars heltal. INT4-kvantisering resulterar oftast i större precisionförlust på grund av det mindre representativa intervallet och lägre precision. Jämfört med INT8-kvantisering kan INT4 dock ytterligare minska lagringsbehov och beräkningskomplexitet. Det bör noteras att INT4-kvantisering är relativt ovanligt i praktiken, eftersom för låg noggrannhet kan leda till betydande försämring av modellens prestanda. Dessutom stöds inte INT4-operationer av all hårdvara, så hårdvarukompatibilitet måste beaktas vid val av kvantiseringsmetod.

### **INT8**

INT8-kvantisering innebär att modellens vikter och aktiveringar konverteras från flyttal till 8-bitars heltal. Trots att det numeriska intervallet för INT8 är mindre och mindre precist, kan det avsevärt minska lagrings- och beräkningskrav. Vid INT8-kvantisering genomgår modellens vikter och aktiveringsvärden en kvantiseringsprocess som inkluderar skalning och offset för att bevara den ursprungliga flyttalsinformationen så mycket som möjligt. Under inferens dekvantiseras dessa kvantiserade värden tillbaka till flyttal för beräkning och kvantiseras sedan åter till INT8 för nästa steg. Denna metod kan ge tillräcklig noggrannhet i de flesta tillämpningar samtidigt som hög beräkningseffektivitet bibehålls.

### **FP16**

FP16-formatet, alltså 16-bitars flyttal (float16), minskar minnesanvändningen med hälften jämfört med 32-bitars flyttal (float32), vilket är en betydande fördel vid storskaliga djupinlärningsapplikationer. FP16-formatet möjliggör att större modeller kan laddas eller mer data kan bearbetas inom samma GPU-minnesbegränsningar. Eftersom moderna GPU-hårdvaror fortsätter att stödja FP16-operationer kan användning av FP16-formatet även leda till förbättrad beräkningshastighet. Dock har FP16-formatet sina inneboende nackdelar, nämligen lägre precision, vilket i vissa fall kan leda till numerisk instabilitet eller precisionförlust.

### **FP32**

FP32-formatet erbjuder högre precision och kan exakt representera ett brett värdeintervall. I scenarier där komplexa matematiska operationer utförs eller där högprecisionsresultat krävs är FP32-formatet att föredra. Men hög precision innebär också större minnesanvändning och längre beräkningstid. För storskaliga djupinlärningsmodeller, särskilt när det finns många modellparametrar och enorma datamängder, kan FP32-formatet orsaka otillräckligt GPU-minne eller minskad inferenshastighet.

På mobila enheter eller IoT-enheter kan vi konvertera Phi-3.x-modeller till INT4, medan AI PC / Copilot PC kan använda högre precision som INT8, FP16 eller FP32.

För närvarande har olika hårdvarutillverkare olika ramverk för att stödja generativa modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX och Nvidias CUDA, med modellkvantisering för lokal distribution.

Tekniskt sett finns olika formatstöd efter kvantisering, som PyTorch / Tensorflow-format, GGUF och ONNX. Jag har gjort en jämförelse mellan GGUF och ONNX samt deras användningsscenarier. Här rekommenderar jag ONNX-kvantiseringsformatet, som har bra stöd från modellramverk till hårdvara. I detta kapitel fokuserar vi på ONNX Runtime för GenAI, OpenVINO och Apple MLX för att utföra modellkvantisering (om du har bättre metoder kan du även bidra via PR).

**Detta kapitel innehåller**

1. [Kvantifiering av Phi-3.5 / 4 med llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifiering av Phi-3.5 / 4 med Generative AI extensions för onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifiering av Phi-3.5 / 4 med Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifiering av Phi-3.5 / 4 med Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.