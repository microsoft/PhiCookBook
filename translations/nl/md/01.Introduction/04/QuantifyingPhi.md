# **Quantificeren van de Phi-familie**

Modelquantificatie verwijst naar het proces waarbij de parameters (zoals gewichten en activatiewaarden) in een neuraal netwerkmodel worden omgezet van een groot waardebereik (meestal een continu waardebereik) naar een kleiner, eindig waardebereik. Deze technologie kan de grootte en rekencomplexiteit van het model verminderen en de operationele efficiëntie van het model verbeteren in omgevingen met beperkte middelen, zoals mobiele apparaten of ingebedde systemen. Modelquantificatie bereikt compressie door de precisie van parameters te verlagen, maar brengt ook een bepaald precisieverlies met zich mee. Daarom is het in het kwantisatieproces noodzakelijk om een balans te vinden tussen modelgrootte, rekencomplexiteit en precisie. Veelgebruikte kwantisatiemethoden zijn onder andere fixed-point kwantisatie, floating-point kwantisatie, enzovoort. Je kunt de geschikte kwantisatiestrategie kiezen op basis van de specifieke situatie en behoeften.

We hopen het GenAI-model te implementeren op randapparaten en meer apparaten toe te laten in GenAI-scenario’s, zoals mobiele apparaten, AI PC/Copilot+PC en traditionele IoT-apparaten. Door middel van het gekwantiseerde model kunnen we het op verschillende randapparaten implementeren, afhankelijk van het type apparaat. Gecombineerd met het modelversnellingsframework en het door hardwarefabrikanten geleverde gekwantiseerde model kunnen we betere SLM-toepassingsscenario’s creëren.

In het kwantisatiescenario hebben we verschillende precisies (INT4, INT8, FP16, FP32). Hieronder volgt een uitleg van de veelgebruikte kwantisatieprecisies.

### **INT4**

INT4-kwantisatie is een radicale kwantisatiemethode die de gewichten en activatiewaarden van het model omzet in 4-bit gehele getallen. INT4-kwantisatie resulteert meestal in een groter precisieverlies vanwege het kleinere representatiebereik en de lagere precisie. Echter, vergeleken met INT8-kwantisatie kan INT4-kwantisatie de opslagvereisten en rekencomplexiteit van het model verder verminderen. Het moet worden opgemerkt dat INT4-kwantisatie relatief zeldzaam is in praktische toepassingen, omdat een te lage nauwkeurigheid kan leiden tot aanzienlijke achteruitgang in de modelprestaties. Bovendien wordt niet alle hardware ondersteund door INT4-bewerkingen, dus hardwarecompatibiliteit moet worden overwogen bij het kiezen van een kwantisatiemethode.

### **INT8**

INT8-kwantisatie is het proces waarbij de gewichten en activaties van een model worden omgezet van floating point-getallen naar 8-bit gehele getallen. Hoewel het numerieke bereik dat door INT8-gehele getallen wordt weergegeven kleiner en minder nauwkeurig is, kan het de opslag- en berekeningsvereisten aanzienlijk verminderen. Bij INT8-kwantisatie ondergaan de gewichten en activatiewaarden van het model een kwantisatieproces, inclusief schaling en offset, om de oorspronkelijke floating point-informatie zoveel mogelijk te behouden. Tijdens inferentie worden deze gekwantiseerde waarden weer terug omgezet naar floating point-getallen voor berekening, en vervolgens weer gekwantiseerd naar INT8 voor de volgende stap. Deze methode kan in de meeste toepassingen voldoende nauwkeurigheid bieden, terwijl een hoge reken efficiëntie behouden blijft.

### **FP16**

Het FP16-formaat, dat wil zeggen 16-bit floating point-getallen (float16), vermindert het geheugenverbruik met de helft vergeleken met 32-bit floating point-getallen (float32), wat aanzienlijke voordelen heeft in grootschalige toepassingen voor deep learning. Het FP16-formaat maakt het mogelijk om grotere modellen te laden of meer gegevens te verwerken binnen dezelfde GPU-geheugenbeperkingen. Aangezien moderne GPU-hardware FP16-bewerkingen blijft ondersteunen, kan het gebruik van het FP16-formaat ook leiden tot verbeteringen in de reken snelheid. Het FP16-formaat heeft echter ook inherente nadelen, namelijk een lagere precisie, die in sommige gevallen kan leiden tot numerieke instabiliteit of precisieverlies.

### **FP32**

Het FP32-formaat biedt een hogere precisie en kan een breed scala aan waarden nauwkeurig weergeven. In scenario’s waarbij complexe wiskundige bewerkingen worden uitgevoerd of hoge precisieresultaten vereist zijn, heeft het FP32-formaat de voorkeur. Hoge nauwkeurigheid betekent echter ook een hoger geheugenverbruik en langere berekeningstijd. Voor grootschalige deep learning-modellen, vooral wanneer er veel modelparameters en enorme hoeveelheden gegevens zijn, kan het FP32-formaat leiden tot onvoldoende GPU-geheugen of een daling van de inferentiesnelheid.

Op mobiele apparaten of IoT-apparaten kunnen we Phi-3.x-modellen omzetten naar INT4, terwijl AI PC / Copilot PC hogere precisies kan gebruiken zoals INT8, FP16, FP32.

Op dit moment hebben verschillende hardwarefabrikanten verschillende frameworks ter ondersteuning van generatieve modellen, zoals Intel’s OpenVINO, Qualcomm’s QNN, Apple’s MLX en Nvidia’s CUDA, gecombineerd met modelkwantisatie om lokale implementatie te voltooien.

Op technologisch gebied hebben we verschillende formaten die worden ondersteund na kwantisatie, zoals het PyTorch / TensorFlow-formaat, GGUF en ONNX. Ik heb een vergelijking gemaakt van formaten en toepassingsscenario’s tussen GGUF en ONNX. Hier raad ik het ONNX-kwantisatieformaat aan, dat goede ondersteuning heeft van het modelframework tot de hardware. In dit hoofdstuk richten we ons op ONNX Runtime voor GenAI, OpenVINO en Apple MLX voor modelkwantisatie (als je een betere methode hebt, kun je die ook aan ons doorgeven door een PR in te dienen).

**Dit hoofdstuk bevat**

1. [Quantificeren van Phi-3.5 / 4 met llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantificeren van Phi-3.5 / 4 met de Generative AI-uitbreidingen voor onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantificeren van Phi-3.5 / 4 met Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantificeren van Phi-3.5 / 4 met Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->