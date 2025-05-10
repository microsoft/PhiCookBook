<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:58:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "no"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo for å vise WebGPU og RAG-mønsteret

RAG-mønsteret med Phi-3.5 Onnx Hosted-modellen bruker Retrieval-Augmented Generation-tilnærmingen, som kombinerer kraften til Phi-3.5-modeller med ONNX-hosting for effektive AI-distribusjoner. Dette mønsteret er viktig for finjustering av modeller for domene-spesifikke oppgaver, og tilbyr en kombinasjon av kvalitet, kostnadseffektivitet og forståelse av lange kontekster. Det er en del av Azure AI sitt tilbud, som gir et bredt utvalg av modeller som er enkle å finne, prøve og bruke, og dekker tilpasningsbehovene til ulike bransjer.

## Hva er WebGPU  
WebGPU er et moderne webgrafikk-API designet for å gi effektiv tilgang til enhetens grafikkprosesseringsenhet (GPU) direkte fra nettlesere. Det er ment å være etterfølgeren til WebGL, med flere viktige forbedringer:

1. **Kompatibilitet med moderne GPU-er**: WebGPU er laget for å fungere sømløst med moderne GPU-arkitekturer, ved å utnytte system-API-er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ytelse**: Det støtter generell GPU-beregning og raskere operasjoner, noe som gjør det egnet for både grafikkrendering og maskinlæringsoppgaver.
3. **Avanserte funksjoner**: WebGPU gir tilgang til mer avanserte GPU-muligheter, som muliggjør mer komplekse og dynamiske grafikk- og beregningsarbeidsmengder.
4. **Redusert JavaScript-belastning**: Ved å flytte flere oppgaver til GPU-en, reduserer WebGPU betydelig arbeidsmengden for JavaScript, noe som gir bedre ytelse og jevnere opplevelser.

WebGPU støttes for øyeblikket i nettlesere som Google Chrome, med pågående arbeid for å utvide støtten til andre plattformer.

### 03.WebGPU  
Påkrevd miljø:

**Støttede nettlesere:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktiver WebGPU:

- I Chrome/Microsoft Edge  

Aktiver `chrome://flags/#enable-unsafe-webgpu`-flagget.

#### Åpne nettleseren din:  
Start Google Chrome eller Microsoft Edge.

#### Gå til flags-siden:  
Skriv `chrome://flags` i adressefeltet og trykk Enter.

#### Søk etter flagget:  
Skriv 'enable-unsafe-webgpu' i søkefeltet øverst på siden.

#### Aktiver flagget:  
Finn #enable-unsafe-webgpu-flagget i resultatlisten.

Klikk på nedtrekksmenyen ved siden av og velg Enabled.

#### Start nettleseren på nytt:  

Etter at flagget er aktivert, må du starte nettleseren på nytt for at endringene skal tre i kraft. Klikk på Relaunch-knappen som vises nederst på siden.

- For Linux, start nettleseren med `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) har WebGPU aktivert som standard.  
- I Firefox Nightly, skriv about:config i adressefeltet og `set dom.webgpu.enabled to true`.

### Sette opp GPU for Microsoft Edge  

Her er stegene for å sette opp en høyytelses-GPU for Microsoft Edge på Windows:

- **Åpne Innstillinger:** Klikk på Start-menyen og velg Innstillinger.  
- **Systeminnstillinger:** Gå til System og deretter Skjerm.  
- **Grafikkinnstillinger:** Bla ned og klikk på Grafikkinnstillinger.  
- **Velg app:** Under “Velg en app for å sette preferanse,” velg Desktop app og deretter Bla gjennom.  
- **Velg Edge:** Naviger til Edge-installasjonsmappen (vanligvis `C:\Program Files (x86)\Microsoft\Edge\Application`) og velg `msedge.exe`.  
- **Sett preferanse:** Klikk på Alternativer, velg Høy ytelse, og klikk deretter Lagre.  
Dette vil sørge for at Microsoft Edge bruker din høyytelses-GPU for bedre ytelse.  
- **Start maskinen på nytt** for at disse innstillingene skal tre i kraft.

### Eksempler: Vennligst [klikk på denne linken](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.