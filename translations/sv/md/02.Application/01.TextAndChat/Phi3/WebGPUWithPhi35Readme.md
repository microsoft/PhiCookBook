<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:10:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sv"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo för att visa WebGPU och RAG-mönstret

RAG-mönstret med Phi-3.5 Onnx Hosted-modellen använder Retrieval-Augmented Generation-metoden, som kombinerar kraften i Phi-3.5-modeller med ONNX-hosting för effektiva AI-distributioner. Detta mönster är avgörande för finjustering av modeller för domänspecifika uppgifter och erbjuder en kombination av kvalitet, kostnadseffektivitet och förståelse för långa kontexter. Det är en del av Azure AI:s svit, som erbjuder ett brett urval av modeller som är lätta att hitta, prova och använda, och som tillgodoser anpassningsbehoven inom olika branscher.

## Vad är WebGPU  
WebGPU är ett modernt webb-grafik-API som är utformat för att ge effektiv åtkomst till en enhets grafikprocessor (GPU) direkt från webbläsare. Det är tänkt att bli efterföljaren till WebGL och erbjuder flera viktiga förbättringar:

1. **Kompatibilitet med moderna GPU:er**: WebGPU är byggt för att fungera sömlöst med samtida GPU-arkitekturer och utnyttjar system-API:er som Vulkan, Metal och Direct3D 12.
2. **Förbättrad prestanda**: Det stödjer allmänna GPU-beräkningar och snabbare operationer, vilket gör det lämpligt både för grafikrendering och maskininlärningsuppgifter.
3. **Avancerade funktioner**: WebGPU ger tillgång till mer avancerade GPU-möjligheter, vilket möjliggör mer komplexa och dynamiska grafik- och beräkningsuppgifter.
4. **Minskad JavaScript-belastning**: Genom att flytta fler uppgifter till GPU:n minskar WebGPU avsevärt belastningen på JavaScript, vilket leder till bättre prestanda och smidigare upplevelser.

WebGPU stöds för närvarande i webbläsare som Google Chrome, och arbete pågår för att utöka stödet till andra plattformar.

### 03.WebGPU  
Krävd miljö:

**Stödda webbläsare:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktivera WebGPU:

- I Chrome/Microsoft Edge  

Aktivera flaggan `chrome://flags/#enable-unsafe-webgpu`.

#### Öppna din webbläsare:  
Starta Google Chrome eller Microsoft Edge.

#### Gå till Flags-sidan:  
Skriv `chrome://flags` i adressfältet och tryck Enter.

#### Sök efter flaggan:  
I sökrutan högst upp på sidan, skriv 'enable-unsafe-webgpu'

#### Aktivera flaggan:  
Hitta #enable-unsafe-webgpu i listan med resultat.

Klicka på rullgardinsmenyn bredvid och välj Enabled.

#### Starta om webbläsaren:  

Efter att ha aktiverat flaggan måste du starta om webbläsaren för att ändringarna ska träda i kraft. Klicka på knappen Relaunch som visas längst ner på sidan.

- För Linux, starta webbläsaren med `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) har WebGPU aktiverat som standard.  
- I Firefox Nightly, skriv about:config i adressfältet och sätt `dom.webgpu.enabled` till true.

### Konfigurera GPU för Microsoft Edge  

Här är stegen för att ställa in en högpresterande GPU för Microsoft Edge på Windows:

- **Öppna Inställningar:** Klicka på Start-menyn och välj Inställningar.  
- **Systeminställningar:** Gå till System och sedan Bildskärm.  
- **Grafikinställningar:** Scrolla ner och klicka på Grafikinställningar.  
- **Välj app:** Under ”Välj en app för att ställa in preferens,” välj Skrivbordsapp och klicka sedan på Bläddra.  
- **Välj Edge:** Navigera till Edge-installationsmappen (vanligtvis `C:\Program Files (x86)\Microsoft\Edge\Application`) och välj `msedge.exe`.  
- **Ställ in preferens:** Klicka på Alternativ, välj Hög prestanda och klicka sedan på Spara.  
Detta säkerställer att Microsoft Edge använder din högpresterande GPU för bättre prestanda.  
- **Starta om** datorn för att dessa inställningar ska börja gälla.

### Exempel: Vänligen [klicka på denna länk](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.