<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:00:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "sv"
}
-->
# Använda Windows GPU för att skapa Prompt flow-lösning med Phi-3.5-Instruct ONNX

Följande dokument är ett exempel på hur man använder PromptFlow med ONNX (Open Neural Network Exchange) för att utveckla AI-applikationer baserade på Phi-3-modeller.

PromptFlow är en uppsättning utvecklingsverktyg som är utformade för att effektivisera hela utvecklingscykeln för LLM-baserade (Large Language Model) AI-applikationer, från idé och prototypframtagning till testning och utvärdering.

Genom att integrera PromptFlow med ONNX kan utvecklare:

- Optimera modellprestanda: Utnyttja ONNX för effektiv modellinferens och distribution.
- Förenkla utvecklingen: Använd PromptFlow för att hantera arbetsflödet och automatisera repetitiva uppgifter.
- Förbättra samarbetet: Underlätta bättre samarbete mellan teammedlemmar genom att erbjuda en enhetlig utvecklingsmiljö.

**Prompt flow** är en uppsättning utvecklingsverktyg som är utformade för att effektivisera hela utvecklingscykeln för LLM-baserade AI-applikationer, från idé, prototypframtagning, testning, utvärdering till produktionssättning och övervakning. Det gör prompt engineering mycket enklare och gör det möjligt att bygga LLM-appar med produktionskvalitet.

Prompt flow kan kopplas till OpenAI, Azure OpenAI Service och anpassningsbara modeller (Huggingface, lokala LLM/SLM). Vi hoppas kunna distribuera Phi-3.5:s kvantiserade ONNX-modell till lokala applikationer. Prompt flow kan hjälpa oss att bättre planera vår verksamhet och slutföra lokala lösningar baserade på Phi-3.5. I detta exempel kommer vi att kombinera ONNX Runtime GenAI Library för att slutföra Prompt flow-lösningen baserad på Windows GPU.

## **Installation**

### **ONNX Runtime GenAI för Windows GPU**

Läs denna riktlinje för att ställa in ONNX Runtime GenAI för Windows GPU [klicka här](./ORTWindowGPUGuideline.md)

### **Ställ in Prompt flow i VSCode**

1. Installera Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.sv.png)

2. Efter att ha installerat Prompt flow VS Code Extension, klicka på extensionen och välj **Installation dependencies** följ denna riktlinje för att installera Prompt flow SDK i din miljö

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.sv.png)

3. Ladda ner [Exempelkod](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) och öppna detta exempel i VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.sv.png)

4. Öppna **flow.dag.yaml** för att välja din Python-miljö

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.sv.png)

   Öppna **chat_phi3_ort.py** för att ändra platsen för din Phi-3.5-instruct ONNX-modell

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.sv.png)

5. Kör din prompt flow för testning

Öppna **flow.dag.yaml** och klicka på visual editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.sv.png)

Efter att ha klickat på detta, kör den för att testa

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.sv.png)

1. Du kan köra batch i terminalen för att se fler resultat


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan se resultaten i din standardwebbläsare


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.sv.png)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.