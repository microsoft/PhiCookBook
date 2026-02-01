# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo for å vise frem WebGPU og RAG-mønsteret

RAG-mønsteret med Phi-3.5 Onnx Hosted-modellen benytter Retrieval-Augmented Generation-tilnærmingen, som kombinerer kraften i Phi-3.5-modeller med ONNX-hosting for effektive AI-distribusjoner. Dette mønsteret er viktig for finjustering av modeller til domene-spesifikke oppgaver, og tilbyr en kombinasjon av kvalitet, kostnadseffektivitet og lang-kontekstforståelse. Det er en del av Azure AI sin portefølje, som gir et bredt utvalg av modeller som er enkle å finne, prøve og bruke, og som dekker tilpasningsbehovene til ulike bransjer.

## Hva er WebGPU  
WebGPU er et moderne webgrafikk-API designet for å gi effektiv tilgang til enhetens grafikkprosesseringsenhet (GPU) direkte fra nettlesere. Det er ment å være etterfølgeren til WebGL, og tilbyr flere viktige forbedringer:

1. **Kompatibilitet med moderne GPU-er**: WebGPU er bygget for å fungere sømløst med moderne GPU-arkitekturer, og utnytter system-API-er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ytelse**: Det støtter generell GPU-beregning og raskere operasjoner, noe som gjør det egnet både for grafikkgjengivelse og maskinlæringsoppgaver.
3. **Avanserte funksjoner**: WebGPU gir tilgang til mer avanserte GPU-muligheter, som muliggjør mer komplekse og dynamiske grafikk- og beregningsarbeidsbelastninger.
4. **Redusert JavaScript-arbeidsmengde**: Ved å overføre flere oppgaver til GPU-en, reduserer WebGPU betydelig belastningen på JavaScript, noe som gir bedre ytelse og jevnere opplevelser.

WebGPU støttes for øyeblikket i nettlesere som Google Chrome, med pågående arbeid for å utvide støtten til andre plattformer.

### 03.WebGPU  
Nødvendig miljø:

**Støttede nettlesere:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktiver WebGPU:

- I Chrome/Microsoft Edge  

Aktiver flagget `chrome://flags/#enable-unsafe-webgpu`.

#### Åpne nettleseren din:  
Start Google Chrome eller Microsoft Edge.

#### Gå til Flags-siden:  
Skriv `chrome://flags` i adressefeltet og trykk Enter.

#### Søk etter flagget:  
Skriv 'enable-unsafe-webgpu' i søkefeltet øverst på siden.

#### Aktiver flagget:  
Finn #enable-unsafe-webgpu-flagget i listen over resultater.

Klikk på nedtrekksmenyen ved siden av og velg Enabled.

#### Start nettleseren på nytt:  

Etter at flagget er aktivert, må du starte nettleseren på nytt for at endringene skal tre i kraft. Klikk på Relaunch-knappen som vises nederst på siden.

- For Linux, start nettleseren med `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) har WebGPU aktivert som standard.  
- I Firefox Nightly, skriv about:config i adressefeltet og sett `dom.webgpu.enabled` til true.

### Sette opp GPU for Microsoft Edge  

Her er stegene for å sette opp en høyytelses-GPU for Microsoft Edge på Windows:

- **Åpne Innstillinger:** Klikk på Start-menyen og velg Innstillinger.  
- **Systeminnstillinger:** Gå til System og deretter Skjerm.  
- **Grafikkinnstillinger:** Bla ned og klikk på Grafikkinnstillinger.  
- **Velg app:** Under «Velg en app for å angi preferanse», velg Desktop-app og deretter Bla gjennom.  
- **Velg Edge:** Naviger til Edge-installasjonsmappen (vanligvis `C:\Program Files (x86)\Microsoft\Edge\Application`) og velg `msedge.exe`.  
- **Angi preferanse:** Klikk på Alternativer, velg Høy ytelse, og klikk deretter Lagre.  
Dette sikrer at Microsoft Edge bruker din høyytelses-GPU for bedre ytelse.  
- **Start** maskinen på nytt for at innstillingene skal tre i kraft.

### Eksempler : Vennligst [klikk på denne lenken](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.