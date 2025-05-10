<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:19:17+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sv"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo för att visa WebGPU och RAG-mönstret  
RAG-mönstret med Phi-3 Onnx Hosted-modellen använder Retrieval-Augmented Generation-metoden, som kombinerar kraften i Phi-3-modeller med ONNX-hosting för effektiva AI-distributioner. Detta mönster är viktigt för finjustering av modeller för domänspecifika uppgifter och erbjuder en kombination av kvalitet, kostnadseffektivitet och förståelse för långa kontexter. Det är en del av Azure AI:s svit och erbjuder ett brett urval av modeller som är lätta att hitta, prova och använda, anpassade efter olika branschers behov. Phi-3-modellerna, inklusive Phi-3-mini, Phi-3-small och Phi-3-medium, finns tillgängliga i Azure AI Model Catalog och kan finjusteras och distribueras självständigt eller via plattformar som HuggingFace och ONNX, vilket visar Microsofts engagemang för tillgängliga och effektiva AI-lösningar.

## Vad är WebGPU  
WebGPU är ett modernt webbgrafik-API designat för att ge effektiv åtkomst till enhetens grafikprocessor (GPU) direkt från webbläsare. Det är tänkt att ersätta WebGL och erbjuder flera viktiga förbättringar:

1. **Kompatibilitet med moderna GPU:er**: WebGPU är byggt för att fungera sömlöst med samtida GPU-arkitekturer och använder system-API:er som Vulkan, Metal och Direct3D 12.  
2. **Förbättrad prestanda**: Det stödjer allmänna GPU-beräkningar och snabbare operationer, vilket gör det lämpligt för både grafikrendering och maskininlärningsuppgifter.  
3. **Avancerade funktioner**: WebGPU ger tillgång till mer avancerade GPU-möjligheter, vilket möjliggör mer komplexa och dynamiska grafik- och beräkningsarbetsbelastningar.  
4. **Minskad JavaScript-belastning**: Genom att flytta fler uppgifter till GPU:n minskar WebGPU avsevärt belastningen på JavaScript, vilket leder till bättre prestanda och smidigare upplevelser.

WebGPU stöds för närvarande i webbläsare som Google Chrome, och arbete pågår för att utöka stödet till andra plattformar.

### 03.WebGPU  
Nödvändig miljö:

**Stödda webbläsare:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktivera WebGPU:

- I Chrome/Microsoft Edge  

Aktivera `chrome://flags/#enable-unsafe-webgpu`-flaggan.

#### Öppna din webbläsare:  
Starta Google Chrome eller Microsoft Edge.

#### Gå till flags-sidan:  
Skriv `chrome://flags` i adressfältet och tryck på Enter.

#### Sök efter flaggan:  
Skriv 'enable-unsafe-webgpu' i sökrutan högst upp på sidan.

#### Aktivera flaggan:  
Hitta #enable-unsafe-webgpu-flaggan i resultatlistan.

Klicka på rullgardinsmenyn bredvid och välj Enabled.

#### Starta om webbläsaren:  

Efter att flaggan är aktiverad måste du starta om webbläsaren för att ändringarna ska träda i kraft. Klicka på knappen Relaunch som visas längst ner på sidan.

- För Linux, starta webbläsaren med `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) har WebGPU aktiverat som standard.  
- I Firefox Nightly, skriv about:config i adressfältet och `set dom.webgpu.enabled to true`.

### Ställa in GPU för Microsoft Edge  

Här är stegen för att konfigurera en högpresterande GPU för Microsoft Edge på Windows:

- **Öppna Inställningar:** Klicka på Start-menyn och välj Inställningar.  
- **Systeminställningar:** Gå till System och sedan Visa.  
- **Grafikinställningar:** Scrolla ned och klicka på Grafikinställningar.  
- **Välj app:** Under ”Välj en app för att ställa in preferens”, välj Skrivbordsapp och klicka sedan på Bläddra.  
- **Välj Edge:** Navigera till Edge-installationsmappen (vanligtvis `C:\Program Files (x86)\Microsoft\Edge\Application`) och välj `msedge.exe`.  
- **Ställ in preferens:** Klicka på Alternativ, välj Hög prestanda och klicka sedan på Spara.  
Detta säkerställer att Microsoft Edge använder din högpresterande GPU för bättre prestanda.  
- **Starta om** datorn för att inställningarna ska börja gälla.

### Öppna din Codespace:  
Navigera till ditt repository på GitHub.  
Klicka på knappen Code och välj Open with Codespaces.

Om du inte har en Codespace än kan du skapa en genom att klicka på New codespace.

**Note** Installera Node Environment i din codespace  
Att köra en npm-demo från en GitHub Codespace är ett utmärkt sätt att testa och utveckla ditt projekt. Här är en steg-för-steg-guide för att komma igång:

### Ställ in din miljö:  
När din Codespace är öppen, kontrollera att Node.js och npm är installerade. Du kan kontrollera detta genom att köra:  
```
node -v
```  
```
npm -v
```

Om de inte är installerade kan du installera dem med:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navigera till din projektmapp:  
Använd terminalen för att gå till katalogen där ditt npm-projekt finns:  
```
cd path/to/your/project
```

### Installera beroenden:  
Kör följande kommando för att installera alla nödvändiga beroenden som listas i din package.json-fil:  

```
npm install
```

### Kör demon:  
När beroendena är installerade kan du köra din demoskript. Detta anges vanligtvis i scripts-sektionen i din package.json. Till exempel, om din demoskript heter start, kan du köra:  

```
npm run build
```  
```
npm run dev
```

### Kom åt demon:  
Om din demo involverar en webbserver kommer Codespaces att ge en URL för åtkomst. Leta efter en notis eller kontrollera fliken Ports för att hitta URL:en.

**Note:** Modellen behöver cachelagras i webbläsaren, så det kan ta lite tid att ladda.

### RAG Demo  
Ladda upp markdown-filen `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Välj din fil:  
Klicka på knappen ”Choose File” för att välja det dokument du vill ladda upp.

### Ladda upp dokumentet:  
Efter att du valt din fil, klicka på ”Upload”-knappen för att ladda ditt dokument för RAG (Retrieval-Augmented Generation).

### Starta din chatt:  
När dokumentet är uppladdat kan du starta en chatt-session med RAG baserat på innehållet i ditt dokument.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.