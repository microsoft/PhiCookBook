<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T19:00:36+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sr"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo za prikaz WebGPU i RAG šablona

RAG šablon sa Phi-3.5 Onnx Hosted modelom koristi pristup Retrieval-Augmented Generation, kombinujući snagu Phi-3.5 modela sa ONNX hostingom za efikasne AI implementacije. Ovaj šablon je ključan za fino podešavanje modela za zadatke specifične za određene oblasti, nudeći kombinaciju kvaliteta, isplativosti i razumevanja dugih konteksta. Deo je Azure AI paketa, pružajući širok izbor modela koji su lako dostupni, isprobavajući i koristeći, prilagođeni potrebama različitih industrija.

## Šta je WebGPU  
WebGPU je moderan web grafički API dizajniran da omogući efikasan pristup grafičkoj procesorskoj jedinici (GPU) uređaja direktno iz web pregledača. Namenjen je da bude naslednik WebGL-a, nudeći nekoliko ključnih poboljšanja:

1. **Kompatibilnost sa savremenim GPU-ovima**: WebGPU je napravljen da besprekorno radi sa savremenim GPU arhitekturama, koristeći sistemske API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opšteprihvaćene GPU proračune i brže operacije, što ga čini pogodnim kako za renderovanje grafike, tako i za zadatke mašinskog učenja.
3. **Napredne funkcije**: WebGPU omogućava pristup naprednijim GPU mogućnostima, omogućavajući složenije i dinamičnije grafičke i računarske zadatke.
4. **Smanjeno opterećenje JavaScript-a**: Prebacivanjem više zadataka na GPU, WebGPU značajno smanjuje opterećenje JavaScript-a, što vodi ka boljim performansama i glatkijem radu.

WebGPU je trenutno podržan u pregledačima kao što je Google Chrome, a rad na proširenju podrške na druge platforme je u toku.

### 03.WebGPU  
Potrebno okruženje:

**Podržani pregledači:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Omogućavanje WebGPU-a:

- U Chrome/Microsoft Edge 

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite pregledač:  
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici sa zastavicama:  
U adresnoj liniji unesite `chrome://flags` i pritisnite Enter.

#### Pretražite zastavicu:  
U polju za pretragu na vrhu stranice unesite 'enable-unsafe-webgpu'

#### Omogućite zastavicu:  
Pronađite #enable-unsafe-webgpu zastavicu u listi rezultata.

Kliknite na padajući meni pored nje i izaberite Enabled.

#### Restartujte pregledač:  

Nakon omogućavanja zastavice, potrebno je da restartujete pregledač da bi promene stupile na snagu. Kliknite na dugme Relaunch koje se pojavljuje na dnu stranice.

- Na Linux-u, pokrenite pregledač sa `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ima WebGPU podrazumevano omogućen.  
- U Firefox Nightly, unesite about:config u adresnoj liniji i `set dom.webgpu.enabled to true`.

### Podešavanje GPU-a za Microsoft Edge  

Evo koraka za podešavanje GPU-a visokih performansi za Microsoft Edge na Windows-u:

- **Otvorite Podešavanja:** Kliknite na Start meni i izaberite Settings.  
- **Podešavanja sistema:** Idite na System, pa zatim Display.  
- **Podešavanja grafike:** Skrolujte dole i kliknite na Graphics settings.  
- **Izaberite aplikaciju:** Pod “Choose an app to set preference,” izaberite Desktop app, pa kliknite Browse.  
- **Izaberite Edge:** Idite do foldera gde je instaliran Edge (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i izaberite `msedge.exe`.  
- **Postavite preferencu:** Kliknite Options, izaberite High performance, pa kliknite Save.  
Ovo će osigurati da Microsoft Edge koristi vaš GPU visokih performansi za bolje performanse.  
- **Restartujte** računar da bi ova podešavanja stupila na snagu.

### Primeri : Molimo [kliknite na ovaj link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ограничење одговорности**:  
Овај документ је преведен помоћу AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења настала употребом овог превода.