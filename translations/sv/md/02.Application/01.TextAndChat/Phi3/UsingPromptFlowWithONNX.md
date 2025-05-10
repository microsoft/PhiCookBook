<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:53:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "sv"
}
-->
# Använda Windows GPU för att skapa Prompt flow-lösning med Phi-3.5-Instruct ONNX

Följande dokument är ett exempel på hur man använder PromptFlow med ONNX (Open Neural Network Exchange) för att utveckla AI-applikationer baserade på Phi-3-modeller.

PromptFlow är en svit utvecklingsverktyg som är designade för att effektivisera hela utvecklingscykeln för LLM-baserade (Large Language Model) AI-applikationer, från idé och prototypframställning till testning och utvärdering.

Genom att integrera PromptFlow med ONNX kan utvecklare:

- Optimera modellprestanda: Utnyttja ONNX för effektiv modellinferens och distribution.
- Förenkla utvecklingen: Använd PromptFlow för att hantera arbetsflödet och automatisera repetitiva uppgifter.
- Förbättra samarbetet: Underlätta bättre samarbete mellan teammedlemmar genom att erbjuda en enhetlig utvecklingsmiljö.

**Prompt flow** är en svit utvecklingsverktyg som är utformade för att effektivisera hela utvecklingscykeln för LLM-baserade AI-applikationer, från idé, prototypframställning, testning, utvärdering till produktionssättning och övervakning. Det gör prompt-engineering mycket enklare och gör det möjligt för dig att bygga LLM-appar med produktionskvalitet.

Prompt flow kan kopplas till OpenAI, Azure OpenAI Service och anpassningsbara modeller (Huggingface, lokala LLM/SLM). Vi hoppas kunna distribuera Phi-3.5:s kvantiserade ONNX-modell till lokala applikationer. Prompt flow kan hjälpa oss att bättre planera vår verksamhet och färdigställa lokala lösningar baserade på Phi-3.5. I detta exempel kombinerar vi ONNX Runtime GenAI Library för att slutföra Prompt flow-lösningen baserad på Windows GPU.

## **Installation**

### **ONNX Runtime GenAI för Windows GPU**

Läs denna riktlinje för att ställa in ONNX Runtime GenAI för Windows GPU [klicka här](./ORTWindowGPUGuideline.md)

### **Ställ in Prompt flow i VSCode**

1. Installera Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.sv.png)

2. Efter att ha installerat Prompt flow VS Code Extension, klicka på tillägget och välj **Installation dependencies** följ denna riktlinje för att installera Prompt flow SDK i din miljö

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.sv.png)

3. Ladda ner [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) och öppna detta exempel i VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.sv.png)

4. Öppna **flow.dag.yaml** för att välja din Python-miljö

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.sv.png)

   Öppna **chat_phi3_ort.py** för att ändra platsen för din Phi-3.5-instruct ONNX-modell

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.sv.png)

5. Kör din prompt flow för testning

Öppna **flow.dag.yaml** och klicka på visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.sv.png)

Efter att ha klickat på detta, kör den för att testa

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.sv.png)

1. Du kan köra batch i terminalen för att se fler resultat


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan kontrollera resultaten i din standardwebbläsare


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.sv.png)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.