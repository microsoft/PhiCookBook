<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:58:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "nl"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo ter demonstratie van WebGPU en het RAG-patroon

Het RAG-patroon met het Phi-3.5 Onnx Hosted-model maakt gebruik van de Retrieval-Augmented Generation-aanpak, waarbij de kracht van Phi-3.5-modellen wordt gecombineerd met ONNX-hosting voor efficiënte AI-implementaties. Dit patroon is essentieel voor het fijn afstemmen van modellen voor domeinspecifieke taken en biedt een combinatie van kwaliteit, kosteneffectiviteit en begrip van lange contexten. Het maakt deel uit van de Azure AI-suite, die een breed scala aan modellen biedt die gemakkelijk te vinden, uit te proberen en te gebruiken zijn, afgestemd op de aanpassingsbehoeften van diverse sectoren.

## Wat is WebGPU  
WebGPU is een moderne webgrafische API die is ontworpen om efficiënte toegang te bieden tot de grafische verwerkingseenheid (GPU) van een apparaat, rechtstreeks vanuit webbrowsers. Het is bedoeld als opvolger van WebGL en biedt verschillende belangrijke verbeteringen:

1. **Compatibiliteit met moderne GPU's**: WebGPU is gebouwd om naadloos samen te werken met hedendaagse GPU-architecturen en maakt gebruik van systeem-API’s zoals Vulkan, Metal en Direct3D 12.
2. **Verbeterde prestaties**: Het ondersteunt algemene GPU-berekeningen en snellere bewerkingen, waardoor het geschikt is voor zowel grafische weergave als machine learning-taken.
3. **Geavanceerde functies**: WebGPU biedt toegang tot meer geavanceerde GPU-mogelijkheden, waardoor complexere en dynamischere grafische en computationele workloads mogelijk zijn.
4. **Verminderde JavaScript-belasting**: Door meer taken naar de GPU te verplaatsen, vermindert WebGPU aanzienlijk de belasting van JavaScript, wat leidt tot betere prestaties en soepelere ervaringen.

WebGPU wordt momenteel ondersteund in browsers zoals Google Chrome, met lopende werkzaamheden om de ondersteuning naar andere platforms uit te breiden.

### 03.WebGPU  
Vereiste omgeving:

**Ondersteunde browsers:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### WebGPU inschakelen:

- In Chrome/Microsoft Edge

Schakel de `chrome://flags/#enable-unsafe-webgpu`-vlag in.

#### Open je browser:  
Start Google Chrome of Microsoft Edge.

#### Ga naar de Flags-pagina:  
Typ `chrome://flags` in de adresbalk en druk op Enter.

#### Zoek de vlag:  
Typ in het zoekvak bovenaan de pagina 'enable-unsafe-webgpu'.

#### Schakel de vlag in:  
Zoek de #enable-unsafe-webgpu-vlag in de lijst met resultaten.

Klik op het dropdown-menu ernaast en selecteer Ingeschakeld.

#### Herstart je browser:  

Na het inschakelen van de vlag moet je je browser opnieuw starten om de wijzigingen door te voeren. Klik op de knop Opnieuw starten die onderaan de pagina verschijnt.

- Voor Linux start je de browser met `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) heeft WebGPU standaard ingeschakeld.  
- In Firefox Nightly typ je about:config in de adresbalk en `set dom.webgpu.enabled to true`.

### GPU instellen voor Microsoft Edge  

Hier zijn de stappen om een high-performance GPU in te stellen voor Microsoft Edge op Windows:

- **Open Instellingen:** Klik op het Startmenu en selecteer Instellingen.  
- **Systeeminstellingen:** Ga naar Systeem en vervolgens Beeldscherm.  
- **Grafische instellingen:** Scroll naar beneden en klik op Grafische instellingen.  
- **Kies app:** Onder “Kies een app om voorkeur in te stellen,” selecteer je Desktop-app en klik op Bladeren.  
- **Selecteer Edge:** Navigeer naar de Edge-installatiemap (meestal `C:\Program Files (x86)\Microsoft\Edge\Application`) en selecteer `msedge.exe`.  
- **Voorkeur instellen:** Klik op Opties, kies Hoge prestaties en klik op Opslaan.  
Dit zorgt ervoor dat Microsoft Edge je high-performance GPU gebruikt voor betere prestaties.  
- **Herstart** je computer zodat deze instellingen van kracht worden.

### Voorbeelden: Klik [deze link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal moet als de gezaghebbende bron worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.