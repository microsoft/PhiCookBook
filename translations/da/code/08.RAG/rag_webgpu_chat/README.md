<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:18:15+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "da"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo til at fremvise WebGPU og RAG-mønsteret  
RAG-mønsteret med Phi-3 Onnx Hosted-modellen udnytter Retrieval-Augmented Generation-tilgangen, som kombinerer styrken fra Phi-3-modeller med ONNX-hosting for effektive AI-implementeringer. Dette mønster er afgørende for finjustering af modeller til domænespecifikke opgaver og tilbyder en kombination af kvalitet, omkostningseffektivitet og forståelse af lange kontekster. Det er en del af Azure AI’s suite, som tilbyder et bredt udvalg af modeller, der er nemme at finde, prøve og bruge, og som imødekommer tilpasningsbehovene i forskellige brancher. Phi-3-modellerne, herunder Phi-3-mini, Phi-3-small og Phi-3-medium, findes i Azure AI Model Catalog og kan finjusteres og implementeres selvstændigt eller via platforme som HuggingFace og ONNX, hvilket viser Microsofts engagement i tilgængelige og effektive AI-løsninger.

## Hvad er WebGPU  
WebGPU er en moderne webgrafik-API designet til at give effektiv adgang til en enheds grafiske processor (GPU) direkte fra webbrowsere. Den er tænkt som efterfølgeren til WebGL og tilbyder flere væsentlige forbedringer:

1. **Kompatibilitet med moderne GPU’er**: WebGPU er bygget til at fungere problemfrit med nutidige GPU-arkitekturer og udnytter system-API’er som Vulkan, Metal og Direct3D 12.  
2. **Forbedret ydeevne**: Den understøtter generelle GPU-beregninger og hurtigere operationer, hvilket gør den velegnet til både grafikrendering og maskinlæringsopgaver.  
3. **Avancerede funktioner**: WebGPU giver adgang til mere avancerede GPU-muligheder, hvilket muliggør mere komplekse og dynamiske grafik- og beregningsarbejdsbelastninger.  
4. **Reduceret JavaScript-arbejdsmængde**: Ved at flytte flere opgaver til GPU’en reducerer WebGPU betydeligt belastningen på JavaScript, hvilket fører til bedre ydeevne og mere flydende oplevelser.

WebGPU understøttes i øjeblikket i browsere som Google Chrome, og der arbejdes løbende på at udvide understøttelsen til andre platforme.

### 03.WebGPU  
Påkrævet miljø:

**Understøttede browsere:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktiver WebGPU:

- I Chrome/Microsoft Edge  

Aktivér flaget `chrome://flags/#enable-unsafe-webgpu`.

#### Åbn din browser:  
Start Google Chrome eller Microsoft Edge.

#### Gå til Flags-siden:  
Skriv `chrome://flags` i adresselinjen og tryk Enter.

#### Søg efter flaget:  
Skriv 'enable-unsafe-webgpu' i søgefeltet øverst på siden.

#### Aktivér flaget:  
Find #enable-unsafe-webgpu-flaget i listen over resultater.  

Klik på dropdown-menuen ved siden af og vælg Enabled.

#### Genstart din browser:  

Efter aktivering af flaget skal du genstarte din browser for at ændringerne træder i kraft. Klik på knappen Relaunch, der vises nederst på siden.

- For Linux, start browseren med `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) har WebGPU aktiveret som standard.  
- I Firefox Nightly, skriv about:config i adresselinjen og sæt `dom.webgpu.enabled` til true.

### Opsætning af GPU til Microsoft Edge  

Her er trinene til at konfigurere en højtydende GPU til Microsoft Edge på Windows:

- **Åbn Indstillinger:** Klik på Start-menuen og vælg Indstillinger.  
- **Systemindstillinger:** Gå til System og derefter Skærm.  
- **Grafikindstillinger:** Rul ned og klik på Grafikindstillinger.  
- **Vælg app:** Under “Vælg en app til at indstille præference” vælg Desktop-app og klik derefter på Gennemse.  
- **Vælg Edge:** Naviger til Edge-installationsmappen (normalt `C:\Program Files (x86)\Microsoft\Edge\Application`) og vælg `msedge.exe`.  
- **Indstil præference:** Klik på Indstillinger, vælg Høj ydeevne, og klik derefter på Gem.  
Dette sikrer, at Microsoft Edge bruger din højtydende GPU for bedre ydeevne.  
- **Genstart** din computer for at indstillingerne træder i kraft.

### Åbn din Codespace:  
Gå til dit repository på GitHub.  
Klik på knappen Code og vælg Open with Codespaces.

Hvis du ikke har en Codespace endnu, kan du oprette en ved at klikke på New codespace.

**Note** Installation af Node-miljø i din codespace  
At køre en npm-demo fra en GitHub Codespace er en god måde at teste og udvikle dit projekt på. Her er en trin-for-trin guide til at komme i gang:

### Opsæt dit miljø:  
Når din Codespace er åben, skal du sikre dig, at du har Node.js og npm installeret. Det kan du tjekke ved at køre:  
```
node -v
```  
```
npm -v
```

Hvis de ikke er installeret, kan du installere dem med:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Naviger til din projektmappe:  
Brug terminalen til at gå til den mappe, hvor dit npm-projekt ligger:  
```
cd path/to/your/project
```

### Installer afhængigheder:  
Kør følgende kommando for at installere alle nødvendige afhængigheder, som er listet i din package.json-fil:  

```
npm install
```

### Kør demoen:  
Når afhængighederne er installeret, kan du køre dit demo-script. Det er normalt angivet i scripts-sektionen i din package.json. For eksempel, hvis dit demo-script hedder start, kan du køre:  

```
npm run build
```  
```
npm run dev
```

### Få adgang til demoen:  
Hvis din demo involverer en webserver, vil Codespaces give en URL til at tilgå den. Hold øje med en notifikation eller tjek fanen Ports for at finde URL’en.

**Note:** Modellen skal caches i browseren, så det kan tage lidt tid at indlæse.

### RAG Demo  
Upload markdown-filen `intro_rag.md` for at fuldføre RAG-løsningen. Hvis du bruger codespaces, kan du downloade filen, som ligger i `01.InferencePhi3/docs/`

### Vælg din fil:  
Klik på knappen “Choose File” for at vælge det dokument, du vil uploade.

### Upload dokumentet:  
Efter at have valgt din fil, klik på “Upload” for at indlæse dit dokument til RAG (Retrieval-Augmented Generation).

### Start din chat:  
Når dokumentet er uploadet, kan du starte en chatsession med RAG baseret på indholdet i dit dokument.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.