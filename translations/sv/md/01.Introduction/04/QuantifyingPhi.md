<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:47:13+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sv"
}
-->
# **Kvantifiering av Phi-familjen**

Modellkvantisering avser processen att mappa parametrarna (såsom vikter och aktiveringsvärden) i en neuralt nätverksmodell från ett stort värdeintervall (vanligtvis ett kontinuerligt värdeintervall) till ett mindre ändligt värdeintervall. Denna teknik kan minska modellens storlek och beräkningskomplexitet samt förbättra modellens driftseffektivitet i resursbegränsade miljöer som mobila enheter eller inbäddade system. Modellkvantisering uppnår komprimering genom att minska precisionen på parametrarna, men det medför också en viss förlust av precision. Därför är det i kvantiseringsprocessen nödvändigt att balansera modellstorlek, beräkningskomplexitet och precision. Vanliga kvantiseringsmetoder inkluderar fastpunktkvantisering, flyttalskvantisering med mera. Du kan välja lämplig kvantiseringsstrategi beroende på det specifika scenariot och behoven.

Vi vill distribuera GenAI-modeller till edge-enheter och låta fler enheter delta i GenAI-scenarier, såsom mobila enheter, AI PC/Copilot+PC och traditionella IoT-enheter. Genom kvantiserade modeller kan vi distribuera dem till olika edge-enheter baserat på enhetstyp. Tillsammans med modellaccelerationsramverk och kvantiserade modeller som tillhandahålls av hårdvarutillverkare kan vi bygga bättre SLM-applikationsscenarier.

I kvantiseringsscenarier har vi olika precisioner (INT4, INT8, FP16, FP32). Nedan följer en förklaring av de vanligaste kvantiseringsprecisionerna.

### **INT4**

INT4-kvantisering är en radikal kvantiseringsmetod som kvantiserar modellens vikter och aktiveringsvärden till 4-bitars heltal. INT4-kvantisering leder vanligtvis till större precisionstapp på grund av det mindre representationsintervallet och lägre precisionen. Jämfört med INT8-kvantisering kan INT4 dock ytterligare minska lagringskraven och beräkningskomplexiteten för modellen. Det bör noteras att INT4-kvantisering är relativt ovanligt i praktiken, eftersom för låg noggrannhet kan orsaka betydande försämring av modellens prestanda. Dessutom stöds inte INT4-operationer av all hårdvara, så hårdvarukompatibilitet måste beaktas vid val av kvantiseringsmetod.

### **INT8**

INT8-kvantisering är processen att konvertera modellens vikter och aktiveringar från flyttal till 8-bitars heltal. Även om det numeriska intervallet som representeras av INT8-heltal är mindre och mindre precist, kan det avsevärt minska lagrings- och beräkningskraven. Vid INT8-kvantisering genomgår modellens vikter och aktiveringsvärden en kvantiseringsprocess, inklusive skalning och offset, för att bevara den ursprungliga flyttalssinformationen så mycket som möjligt. Under inferens dekvantiseras dessa kvantiserade värden tillbaka till flyttal för beräkning och kvantiseras sedan tillbaka till INT8 för nästa steg. Denna metod kan ge tillräcklig noggrannhet i de flesta tillämpningar samtidigt som hög beräkningseffektivitet bibehålls.

### **FP16**

FP16-formatet, det vill säga 16-bitars flyttal (float16), halverar minnesanvändningen jämfört med 32-bitars flyttal (float32), vilket ger betydande fördelar i storskaliga djupinlärningsapplikationer. FP16-formatet möjliggör att ladda större modeller eller bearbeta mer data inom samma GPU-minnesbegränsningar. Eftersom modern GPU-hårdvara fortsätter att stödja FP16-operationer kan användning av FP16-formatet också leda till förbättrad beräkningshastighet. FP16-formatet har dock också sina inneboende nackdelar, nämligen lägre precision, vilket i vissa fall kan leda till numerisk instabilitet eller precisionstapp.

### **FP32**

FP32-formatet erbjuder högre precision och kan exakt representera ett brett värdeintervall. I scenarier där komplexa matematiska operationer utförs eller högprecisionsresultat krävs, föredras FP32-formatet. Hög precision innebär dock också högre minnesanvändning och längre beräkningstid. För storskaliga djupinlärningsmodeller, särskilt när det finns många modellparametrar och enorma datamängder, kan FP32-formatet orsaka otillräckligt GPU-minne eller minskad inferenshastighet.

På mobila enheter eller IoT-enheter kan vi konvertera Phi-3.x-modeller till INT4, medan AI PC / Copilot PC kan använda högre precisioner som INT8, FP16, FP32.

För närvarande har olika hårdvarutillverkare olika ramverk för att stödja generativa modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX och Nvidias CUDA, med kombination av modellkvantisering för lokal distribution.

Tekniskt sett har vi olika formatstöd efter kvantisering, såsom PyTorch / Tensorflow-format, GGUF och ONNX. Jag har gjort en jämförelse av format och användningsscenarier mellan GGUF och ONNX. Här rekommenderar jag ONNX-kvantiseringsformatet, som har bra stöd från modellramverk till hårdvara. I detta kapitel fokuserar vi på ONNX Runtime för GenAI, OpenVINO och Apple MLX för att utföra modellkvantisering (om du har en bättre metod kan du också bidra genom att skicka en PR).

**Detta kapitel innehåller**

1. [Kvantifiering av Phi-3.5 / 4 med llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifiering av Phi-3.5 / 4 med Generative AI extensions för onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifiering av Phi-3.5 / 4 med Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifiering av Phi-3.5 / 4 med Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.