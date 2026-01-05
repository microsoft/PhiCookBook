<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T12:25:57+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sv"
}
-->
# **Kvantifiering av Phi-familjen**

Modellkvantisering avser processen att kartlägga parametrarna (såsom vikter och aktiveringsvärden) i en neuralt nätverksmodell från ett stort värdeintervall (vanligtvis ett kontinuerligt värdeintervall) till ett mindre ändligt värdeintervall. Denna teknik kan minska modellens storlek och beräkningskomplexitet samt förbättra modellens driftseffektivitet i resursbegränsade miljöer som mobila enheter eller inbyggda system. Modellkvantisering uppnår komprimering genom att minska precisionen hos parametrarna, men det medför också en viss förlust av precision. Därför är det nödvändigt att i kvantiseringsprocessen balansera modellstorlek, beräkningskomplexitet och precision. Vanliga kvantiseringsmetoder inkluderar fastpunktskvantisering, flyttalskvantisering med mera. Du kan välja lämplig kvantiseringsstrategi utifrån den specifika situationen och behoven.

Vi hoppas kunna distribuera GenAI-modellen till edge-enheter och låta fler enheter komma in i GenAI-scenarier, såsom mobila enheter, AI PC/Copilot+PC och traditionella IoT-enheter. Genom kvantiseringsmodellen kan vi distribuera den till olika edge-enheter baserat på olika enheter. Tillsammans med modellaccelerationramverket och kvantiseringsmodellen som tillhandahålls av hårdvarutillverkare kan vi bygga bättre SLM-applikationsscenarier.

I kvantiseringsscenarier har vi olika precisioner (INT4, INT8, FP16, FP32). Nedan följer en förklaring av de vanligt använda kvantiseringsprecisionerna

### **INT4**

INT4-kvantisering är en radikal kvantiseringsmetod som kvantiserar modellens vikter och aktiveringsvärden till 4-bitars heltal. INT4-kvantisering leder vanligtvis till större precisionförlust på grund av det mindre representationsintervallet och lägre precisionen. Jämfört med INT8-kvantisering kan INT4-kvantisering dock ytterligare minska lagringskraven och beräkningskomplexiteten för modellen. Det bör noteras att INT4-kvantisering är relativt sällsynt i praktiska tillämpningar eftersom för låg noggrannhet kan orsaka betydande försämring av modellens prestanda. Dessutom stöder inte all hårdvara INT4-operationer, så hårdvarukompatibilitet måste beaktas vid val av kvantiseringsmetod.

### **INT8**

INT8-kvantisering är processen att konvertera en modells vikter och aktiveringar från flyttal till 8-bitars heltal. Trots att det numeriska intervallet som representeras av INT8-heltal är mindre och mindre precist, kan det avsevärt minska lagrings- och beräkningskrav. Vid INT8-kvantisering genomgår modellens vikter och aktiveringsvärden en kvantiseringsprocess, inklusive skalning och offset, för att bevara den ursprungliga flyttalsinformationen så mycket som möjligt. Under inferens kommer dessa kvantiserade värden att dekvantisera tillbaka till flyttal för beräkning och sedan kvantiseras tillbaka till INT8 för nästa steg. Denna metod kan ge tillräcklig noggrannhet i de flesta tillämpningar samtidigt som hög beräknings-effektivitet bibehålls.

### **FP16**

FP16-formatet, det vill säga 16-bitars flyttal (float16), reducerar minnesanvändningen till hälften jämfört med 32-bitars flyttal (float32), vilket har betydande fördelar i storskaliga djupinlärningsapplikationer. FP16-formatet möjliggör att ladda större modeller eller bearbeta mer data inom samma GPU-minnesbegränsningar. Eftersom moderna GPU-hårdvaror fortsätter att stödja FP16-operationer kan användningen av FP16-formatet även leda till förbättrad beräkningshastighet. FP16-formatet har dock också sina inneboende nackdelar, nämligen lägre precision, vilket i vissa fall kan leda till numerisk instabilitet eller precisionförlust.

### **FP32**

FP32-formatet erbjuder högre precision och kan noggrant representera ett brett spektrum av värden. I scenarier där komplexa matematiska operationer utförs eller högprecisionsresultat krävs är FP32-formatet att föredra. Men hög precision medför också högre minnesanvändning och längre beräkningstid. För storskaliga djupinlärningsmodeller, särskilt när det finns många modellparametrar och enorma datamängder, kan FP32-formatet leda till otillräckligt GPU-minne eller minskad inferenshastighet.

På mobila enheter eller IoT-enheter kan vi konvertera Phi-3.x-modeller till INT4, medan AI PC / Copilot PC kan använda högre precision såsom INT8, FP16, FP32.

För närvarande har olika hårdvarutillverkare olika ramverk för att stödja generativa modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX och Nvidias CUDA osv., kombinerat med modellkvantisering för att slutföra lokal distribution.

Tekniskt sett har vi olika formatstöd efter kvantisering, såsom PyTorch / TensorFlow-format, GGUF och ONNX. Jag har gjort en formatjämförelse och applikationsscenarier mellan GGUF och ONNX. Här rekommenderar jag ONNX-kvantiseringsformatet, som har bra stöd från modellramverket till hårdvaran. I detta kapitel fokuserar vi på ONNX Runtime för GenAI, OpenVINO och Apple MLX för att utföra modellkvantisering (om du har ett bättre sätt kan du även ge det till oss genom att skicka en PR).

**Detta kapitel inkluderar**

1. [Kvantifiering av Phi-3.5 / 4 med llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifiering av Phi-3.5 / 4 med Generative AI extensions för onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifiering av Phi-3.5 / 4 med Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifiering av Phi-3.5 / 4 med Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller inkonsekvenser. Originaldokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->