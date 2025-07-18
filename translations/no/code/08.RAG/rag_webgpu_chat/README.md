<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:18:30+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "no"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo for å vise WebGPU og RAG-mønsteret
RAG-mønsteret med Phi-3 Onnx Hosted-modellen benytter Retrieval-Augmented Generation-tilnærmingen, som kombinerer kraften i Phi-3-modeller med ONNX-hosting for effektive AI-distribusjoner. Dette mønsteret er viktig for finjustering av modeller til domene-spesifikke oppgaver, og tilbyr en kombinasjon av kvalitet, kostnadseffektivitet og forståelse av lange kontekster. Det er en del av Azure AI sin portefølje, som gir et bredt utvalg av modeller som er enkle å finne, prøve og bruke, og som dekker tilpasningsbehovene til ulike bransjer. Phi-3-modellene, inkludert Phi-3-mini, Phi-3-small og Phi-3-medium, er tilgjengelige i Azure AI Model Catalog og kan finjusteres og distribueres selvstendig eller gjennom plattformer som HuggingFace og ONNX, noe som viser Microsofts engasjement for tilgjengelige og effektive AI-løsninger.

## Hva er WebGPU
WebGPU er et moderne webgrafikk-API designet for å gi effektiv tilgang til enhetens grafikkprosesseringsenhet (GPU) direkte fra nettlesere. Det er ment å være etterfølgeren til WebGL, og tilbyr flere viktige forbedringer:

1. **Kompatibilitet med moderne GPUer**: WebGPU er bygget for å fungere sømløst med moderne GPU-arkitekturer, og utnytter system-APIer som Vulkan, Metal og Direct3D 12.
2. **Forbedret ytelse**: Det støtter generell GPU-beregning og raskere operasjoner, noe som gjør det egnet både for grafikkgjengivelse og maskinlæringsoppgaver.
3. **Avanserte funksjoner**: WebGPU gir tilgang til mer avanserte GPU-muligheter, som muliggjør mer komplekse og dynamiske grafikk- og beregningsarbeidsbelastninger.
4. **Redusert JavaScript-arbeidsmengde**: Ved å overføre flere oppgaver til GPUen, reduserer WebGPU betydelig arbeidsmengden på JavaScript, noe som gir bedre ytelse og jevnere opplevelser.

WebGPU støttes for øyeblikket i nettlesere som Google Chrome, med pågående arbeid for å utvide støtten til andre plattformer.

### 03.WebGPU
Krav til miljø:

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
- **Velg app:** Under “Velg en app for å angi preferanse,” velg Desktop-app og deretter Bla gjennom.
- **Velg Edge:** Naviger til Edge-installasjonsmappen (vanligvis `C:\Program Files (x86)\Microsoft\Edge\Application`) og velg `msedge.exe`.
- **Angi preferanse:** Klikk på Alternativer, velg Høy ytelse, og klikk deretter Lagre.  
Dette sikrer at Microsoft Edge bruker din høyytelses-GPU for bedre ytelse.  
- **Start** maskinen på nytt for at innstillingene skal tre i kraft.

### Åpne Codespace:
Gå til ditt repository på GitHub.  
Klikk på Code-knappen og velg Open with Codespaces.

Hvis du ikke har en Codespace ennå, kan du opprette en ved å klikke på New codespace.

**Note** Installere Node-miljø i din codespace  
Å kjøre en npm-demo fra en GitHub Codespace er en flott måte å teste og utvikle prosjektet ditt på. Her er en steg-for-steg guide for å komme i gang:

### Sett opp miljøet ditt:
Når Codespace er åpen, sørg for at du har Node.js og npm installert. Du kan sjekke dette ved å kjøre:  
```
node -v
```  
```
npm -v
```

Hvis de ikke er installert, kan du installere dem med:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Naviger til prosjektmappen:
Bruk terminalen til å gå til mappen der npm-prosjektet ditt ligger:  
```
cd path/to/your/project
```

### Installer avhengigheter:
Kjør følgende kommando for å installere alle nødvendige avhengigheter som er listet i package.json-filen din:  

```
npm install
```

### Kjør demoen:
Når avhengighetene er installert, kan du kjøre demo-skriptet ditt. Dette er vanligvis spesifisert i scripts-delen av package.json. For eksempel, hvis demo-skriptet heter start, kan du kjøre:  

```
npm run build
```  
```
npm run dev
```

### Få tilgang til demoen:
Hvis demoen din involverer en webserver, vil Codespaces gi en URL for å få tilgang til den. Se etter en varsling eller sjekk Ports-fanen for å finne URL-en.

**Note:** Modellen må caches i nettleseren, så det kan ta litt tid å laste.

### RAG Demo
Last opp markdown-filen `intro_rag.md` for å fullføre RAG-løsningen. Hvis du bruker codespaces, kan du laste ned filen som ligger i `01.InferencePhi3/docs/`

### Velg filen din:
Klikk på knappen som sier “Choose File” for å velge dokumentet du vil laste opp.

### Last opp dokumentet:
Etter at du har valgt filen, klikker du på “Upload”-knappen for å laste inn dokumentet for RAG (Retrieval-Augmented Generation).

### Start chatten:
Når dokumentet er lastet opp, kan du starte en chat-økt med RAG basert på innholdet i dokumentet ditt.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.