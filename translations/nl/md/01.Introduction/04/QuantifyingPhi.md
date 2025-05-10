<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:30:58+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "nl"
}
-->
# **Kwantiseren van de Phi-familie**

Modelkwantisering verwijst naar het proces waarbij de parameters (zoals gewichten en activatiewaarden) in een neuraal netwerkmodel worden omgezet van een groot waardebereik (meestal een continu bereik) naar een kleiner eindig waardebereik. Deze technologie kan de grootte en de rekencomplexiteit van het model verminderen en de operationele efficiëntie van het model verbeteren in omgevingen met beperkte middelen, zoals mobiele apparaten of embedded systemen. Modelkwantisering bereikt compressie door de precisie van parameters te verlagen, maar dit brengt ook een zekere precisieverlies met zich mee. Daarom is het bij het kwantiseren belangrijk om een balans te vinden tussen modelgrootte, rekencomplexiteit en precisie. Veelgebruikte kwantiseringstechnieken zijn onder andere fixed-point kwantisering en floating-point kwantisering. Je kunt de juiste kwantisatiestrategie kiezen op basis van de specifieke situatie en behoeften.

We willen GenAI-modellen inzetten op edge-apparaten en zo meer apparaten toegang geven tot GenAI-scenario’s, zoals mobiele apparaten, AI PC/Copilot+PC en traditionele IoT-apparaten. Door het kwantiseren van modellen kunnen we deze op verschillende edge-apparaten inzetten, afhankelijk van het apparaat. In combinatie met het modelversnellingsframework en de kwantisatiemodellen die door hardwarefabrikanten worden geleverd, kunnen we betere SLM-toepassingsscenario’s creëren.

In kwantisering zijn er verschillende precisies (INT4, INT8, FP16, FP32). Hieronder volgt een uitleg van de meest gebruikte kwantisatieprecisies.

### **INT4**

INT4-kwantisering is een radicale methode waarbij de gewichten en activatiewaarden van het model worden omgezet naar 4-bits gehele getallen. INT4-kwantisering leidt doorgaans tot een groter precisieverlies vanwege het kleinere representatiebereik en de lagere precisie. Vergeleken met INT8-kwantisering kan INT4 echter de opslagvereisten en rekencomplexiteit van het model verder verminderen. Het is belangrijk op te merken dat INT4-kwantisering in de praktijk vrij zeldzaam is, omdat de nauwkeurigheid te laag kan zijn en daardoor de modelprestaties aanzienlijk kunnen verslechteren. Bovendien wordt INT4 niet door alle hardware ondersteund, dus hardwarecompatibiliteit moet worden overwogen bij het kiezen van een kwantisatiemethode.

### **INT8**

INT8-kwantisering is het proces waarbij de gewichten en activaties van een model worden omgezet van drijvende-kommagetallen naar 8-bits gehele getallen. Hoewel het numerieke bereik van INT8 kleiner en minder precies is, kan dit de opslag- en rekenvereisten aanzienlijk verminderen. Bij INT8-kwantisering ondergaan de gewichten en activatiewaarden een kwantisatieproces, inclusief schaling en offset, om de oorspronkelijke floating point-informatie zoveel mogelijk te behouden. Tijdens inferentie worden deze gekwantiseerde waarden weer terug omgezet naar drijvende-kommagetallen voor berekeningen en daarna opnieuw gekwantiseerd naar INT8 voor de volgende stap. Deze methode biedt voldoende nauwkeurigheid in de meeste toepassingen en behoudt tegelijkertijd een hoge rekenefficiëntie.

### **FP16**

Het FP16-formaat, oftewel 16-bits floating point-getallen (float16), halveert het geheugengebruik in vergelijking met 32-bits floating point-getallen (float32), wat aanzienlijke voordelen biedt bij grootschalige deep learning-toepassingen. Het FP16-formaat maakt het mogelijk om grotere modellen te laden of meer data te verwerken binnen dezelfde GPU-geheugenlimieten. Omdat moderne GPU-hardware FP16-bewerkingen blijft ondersteunen, kan het gebruik van FP16 ook leiden tot een hogere rekensnelheid. Echter, FP16 heeft ook zijn nadelen, namelijk een lagere precisie, wat in sommige gevallen kan leiden tot numerieke instabiliteit of precisieverlies.

### **FP32**

Het FP32-formaat biedt een hogere precisie en kan een breed scala aan waarden nauwkeurig weergeven. In scenario’s waarbij complexe wiskundige bewerkingen worden uitgevoerd of hoge precisie vereist is, verdient FP32 de voorkeur. Hoge nauwkeurigheid betekent echter ook meer geheugengebruik en langere rekentijd. Voor grootschalige deep learning-modellen, vooral met veel modelparameters en enorme hoeveelheden data, kan FP32 leiden tot onvoldoende GPU-geheugen of een lagere inferentiesnelheid.

Op mobiele apparaten of IoT-apparaten kunnen we Phi-3.x modellen converteren naar INT4, terwijl AI PC / Copilot PC hogere precisies zoals INT8, FP16, FP32 kunnen gebruiken.

Op dit moment hebben verschillende hardwarefabrikanten verschillende frameworks om generatieve modellen te ondersteunen, zoals Intel's OpenVINO, Qualcomm's QNN, Apple's MLX en Nvidia's CUDA, die in combinatie met modelkwantisering lokale inzet mogelijk maken.

Op technologisch vlak ondersteunen we na kwantisering verschillende formaten, zoals PyTorch / Tensorflow, GGUF en ONNX. Ik heb een vergelijking gemaakt tussen GGUF en ONNX qua formaat en toepassingsscenario’s. Hier raad ik het ONNX-kwantisatieformaat aan, dat goede ondersteuning biedt van het modelframework tot aan de hardware. In dit hoofdstuk richten we ons op ONNX Runtime voor GenAI, OpenVINO en Apple MLX voor modelkwantisering (als je een betere methode hebt, kun je die ook aanleveren via een PR).

**Dit hoofdstuk bevat**

1. [Kwantiseren van Phi-3.5 / 4 met llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kwantiseren van Phi-3.5 / 4 met Generative AI-extensies voor onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kwantiseren van Phi-3.5 / 4 met Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kwantiseren van Phi-3.5 / 4 met Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.