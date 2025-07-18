<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:10:36+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "da"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo til at fremvise WebGPU og RAG-mønsteret

RAG-mønsteret med Phi-3.5 Onnx Hosted-modellen udnytter Retrieval-Augmented Generation-tilgangen, som kombinerer kraften fra Phi-3.5-modeller med ONNX-hosting for effektive AI-implementeringer. Dette mønster er vigtigt til finjustering af modeller til domænespecifikke opgaver og tilbyder en kombination af kvalitet, omkostningseffektivitet og forståelse af lange kontekster. Det er en del af Azure AI’s suite, som giver et bredt udvalg af modeller, der er nemme at finde, prøve og bruge, og som imødekommer tilpasningsbehovene i forskellige brancher.

## Hvad er WebGPU  
WebGPU er en moderne webgrafik-API designet til at give effektiv adgang til en enheds grafiske processor (GPU) direkte fra webbrowsere. Den er tænkt som efterfølgeren til WebGL og tilbyder flere væsentlige forbedringer:

1. **Kompatibilitet med moderne GPU’er**: WebGPU er bygget til at fungere problemfrit med nutidige GPU-arkitekturer og udnytter system-API’er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ydeevne**: Den understøtter generelle GPU-beregninger og hurtigere operationer, hvilket gør den velegnet til både grafikrendering og maskinlæringsopgaver.
3. **Avancerede funktioner**: WebGPU giver adgang til mere avancerede GPU-muligheder, hvilket muliggør mere komplekse og dynamiske grafik- og beregningsarbejdsbelastninger.
4. **Reduceret JavaScript-arbejdsmængde**: Ved at flytte flere opgaver til GPU’en reducerer WebGPU betydeligt belastningen på JavaScript, hvilket fører til bedre ydeevne og mere flydende oplevelser.

WebGPU understøttes i øjeblikket i browsere som Google Chrome, og der arbejdes løbende på at udvide understøttelsen til andre platforme.

### 03.WebGPU  
Krav til miljø:

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

- På Linux skal du starte browseren med `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) har WebGPU aktiveret som standard.  
- I Firefox Nightly skal du indtaste about:config i adresselinjen og sætte `dom.webgpu.enabled` til true.

### Opsætning af GPU til Microsoft Edge  

Her er trinene til at konfigurere en højtydende GPU til Microsoft Edge på Windows:

- **Åbn Indstillinger:** Klik på Start-menuen og vælg Indstillinger.  
- **Systemindstillinger:** Gå til System og derefter Skærm.  
- **Grafikindstillinger:** Rul ned og klik på Grafikindstillinger.  
- **Vælg app:** Under “Vælg en app til at indstille præference” vælg Desktop-app og klik derefter på Gennemse.  
- **Vælg Edge:** Naviger til Edge-installationsmappen (normalt `C:\Program Files (x86)\Microsoft\Edge\Application`) og vælg `msedge.exe`.  
- **Indstil præference:** Klik på Indstillinger, vælg Høj ydeevne, og klik derefter på Gem.  
Dette sikrer, at Microsoft Edge bruger din højtydende GPU for bedre ydeevne.  
- **Genstart** din computer for at få disse indstillinger til at træde i kraft.

### Eksempler : Klik venligst på [dette link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.