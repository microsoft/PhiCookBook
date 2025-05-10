<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:20:13+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "nl"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo voor het tonen van WebGPU en het RAG-patroon
Het RAG-patroon met het Phi-3 Onnx Hosted-model maakt gebruik van de Retrieval-Augmented Generation-aanpak, waarbij de kracht van Phi-3-modellen wordt gecombineerd met ONNX-hosting voor efficiënte AI-implementaties. Dit patroon is essentieel voor het fijn afstemmen van modellen voor domeinspecifieke taken en biedt een mix van kwaliteit, kosteneffectiviteit en begrip van lange contexten. Het maakt deel uit van Azure AI’s suite, die een breed scala aan modellen biedt die makkelijk te vinden, uit te proberen en te gebruiken zijn, afgestemd op de aanpassingsbehoeften van verschillende industrieën. De Phi-3-modellen, waaronder Phi-3-mini, Phi-3-small en Phi-3-medium, zijn beschikbaar in de Azure AI Model Catalog en kunnen zelf worden fijn afgestemd en ingezet of via platforms zoals HuggingFace en ONNX, wat Microsofts inzet voor toegankelijke en efficiënte AI-oplossingen onderstreept.

## Wat is WebGPU
WebGPU is een moderne webgrafische API die is ontworpen om efficiënte toegang te bieden tot de grafische processor (GPU) van een apparaat, rechtstreeks vanuit webbrowsers. Het is bedoeld als opvolger van WebGL en biedt verschillende belangrijke verbeteringen:

1. **Compatibiliteit met moderne GPU’s**: WebGPU is gebouwd om naadloos te werken met hedendaagse GPU-architecturen, waarbij gebruik wordt gemaakt van systeem-API’s zoals Vulkan, Metal en Direct3D 12.
2. **Verbeterde prestaties**: Het ondersteunt algemene GPU-berekeningen en snellere bewerkingen, waardoor het geschikt is voor zowel grafische rendering als machine learning-taken.
3. **Geavanceerde functies**: WebGPU biedt toegang tot geavanceerdere GPU-mogelijkheden, waardoor complexere en dynamische grafische en computationele workloads mogelijk zijn.
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

Schakel de `chrome://flags/#enable-unsafe-webgpu` vlag in.

#### Open je browser:
Start Google Chrome of Microsoft Edge.

#### Ga naar de Flags-pagina:
Typ in de adresbalk `chrome://flags` en druk op Enter.

#### Zoek de vlag:
Typ in het zoekvak bovenaan de pagina 'enable-unsafe-webgpu'

#### Schakel de vlag in:
Zoek de #enable-unsafe-webgpu vlag in de lijst met resultaten.

Klik op het dropdown-menu ernaast en selecteer Enabled.

#### Herstart je browser:

Na het inschakelen van de vlag moet je je browser opnieuw starten om de wijzigingen door te voeren. Klik op de knop Relaunch onderaan de pagina.

- Voor Linux start je de browser met `--enable-features=Vulkan`.
- Safari 18 (macOS 15) heeft WebGPU standaard ingeschakeld.
- In Firefox Nightly typ je about:config in de adresbalk en `set dom.webgpu.enabled to true`.

### GPU instellen voor Microsoft Edge

Volg deze stappen om een high-performance GPU in te stellen voor Microsoft Edge op Windows:

- **Open Instellingen:** Klik op het Startmenu en selecteer Instellingen.
- **Systeeminstellingen:** Ga naar Systeem en vervolgens Beeldscherm.
- **Grafische instellingen:** Scroll naar beneden en klik op Grafische instellingen.
- **Kies app:** Onder “Kies een app om voorkeur in te stellen,” selecteer Desktop-app en klik op Bladeren.
- **Selecteer Edge:** Navigeer naar de Edge-installatiemap (meestal `C:\Program Files (x86)\Microsoft\Edge\Application`) en selecteer `msedge.exe`.
- **Stel voorkeur in:** Klik op Opties, kies Hoge prestaties en klik op Opslaan.  
Dit zorgt ervoor dat Microsoft Edge je high-performance GPU gebruikt voor betere prestaties.  
- **Herstart** je computer zodat deze instellingen van kracht worden.

### Open je Codespace:
Ga naar je repository op GitHub.  
Klik op de Code-knop en selecteer Openen met Codespaces.

Als je nog geen Codespace hebt, kun je er een aanmaken door op New codespace te klikken.

**Note** Node-omgeving installeren in je codespace  
Een npm-demo draaien vanuit een GitHub Codespace is een goede manier om je project te testen en te ontwikkelen. Hier volgt een stapsgewijze handleiding om te beginnen:

### Stel je omgeving in:
Zodra je Codespace geopend is, zorg dat Node.js en npm geïnstalleerd zijn. Controleer dit door het volgende uit te voeren:  
```
node -v
```  
```
npm -v
```

Als ze niet geïnstalleerd zijn, kun je ze installeren met:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navigeer naar je projectmap:
Gebruik de terminal om naar de map te gaan waar je npm-project staat:  
```
cd path/to/your/project
```

### Installeer afhankelijkheden:
Voer het volgende commando uit om alle benodigde afhankelijkheden uit je package.json te installeren:  

```
npm install
```

### Start de demo:
Zodra de afhankelijkheden geïnstalleerd zijn, kun je je demo-script uitvoeren. Dit staat meestal in het scripts-gedeelte van je package.json. Bijvoorbeeld, als je demo-script start heet, voer je het volgende uit:  

```
npm run build
```  
```
npm run dev
```

### Toegang tot de demo:
Als je demo een webserver gebruikt, geeft Codespaces een URL om deze te openen. Let op een melding of kijk in het tabblad Poorten om de URL te vinden.

**Note:** Het model moet eerst in de browser worden gecached, dus het kan even duren voordat het geladen is.

### RAG Demo
Upload het markdown-bestand `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecteer je bestand:
Klik op de knop “Choose File” om het document te kiezen dat je wilt uploaden.

### Upload het document:
Na het selecteren van je bestand klik je op de knop “Upload” om het document te laden voor RAG (Retrieval-Augmented Generation).

### Start je chat:
Zodra het document is geüpload, kun je een chatsessie starten met RAG op basis van de inhoud van je document.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.