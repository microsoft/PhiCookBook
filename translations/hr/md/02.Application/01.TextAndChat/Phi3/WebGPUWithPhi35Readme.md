<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T19:00:46+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "hr"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo za prikaz WebGPU i RAG obrasca

RAG obrazac s Phi-3.5 Onnx Hosted modelom koristi pristup Retrieval-Augmented Generation, kombinirajući snagu Phi-3.5 modela s ONNX hostingom za učinkovite AI implementacije. Ovaj obrazac je ključan za fino podešavanje modela za zadatke specifične za određena područja, nudeći kombinaciju kvalitete, isplativosti i razumijevanja dugog konteksta. Dio je Azure AI paketa, pružajući širok izbor modela koji su jednostavni za pronalaženje, isprobavanje i korištenje, prilagođene potrebama različitih industrija.

## Što je WebGPU  
WebGPU je moderna web grafička API dizajnirana za efikasan pristup grafičkoj procesorskoj jedinici (GPU) uređaja izravno preko web preglednika. Namijenjena je kao nasljednik WebGL-a, nudeći nekoliko ključnih poboljšanja:

1. **Kompatibilnost s modernim GPU-ima**: WebGPU je izrađena da besprijekorno radi s suvremenim GPU arhitekturama, koristeći sistemske API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opće GPU izračune i brže operacije, što je čini pogodnom i za grafički prikaz i za zadatke strojnog učenja.
3. **Napredne značajke**: WebGPU omogućuje pristup naprednijim GPU mogućnostima, omogućujući složenije i dinamičnije grafičke i računalne zadatke.
4. **Smanjen JavaScript workload**: Prebacivanjem većeg dijela zadataka na GPU, WebGPU znatno smanjuje opterećenje JavaScript-a, što rezultira boljim performansama i glatkijim iskustvom.

WebGPU je trenutno podržan u preglednicima poput Google Chrome-a, a radi se na proširenju podrške i na druge platforme.

### 03.WebGPU  
Potrebno okruženje:

**Podržani preglednici:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Omogućavanje WebGPU-a:

- U Chrome/Microsoft Edge

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite preglednik:  
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici s zastavicama:  
U adresnu traku upišite `chrome://flags` i pritisnite Enter.

#### Potražite zastavicu:  
U polje za pretraživanje na vrhu stranice upišite 'enable-unsafe-webgpu'

#### Omogućite zastavicu:  
Pronađite #enable-unsafe-webgpu zastavicu na popisu rezultata.

Kliknite padajući izbornik pored nje i odaberite Enabled.

#### Ponovno pokrenite preglednik:

Nakon što omogućite zastavicu, potrebno je ponovno pokrenuti preglednik da bi promjene stupile na snagu. Kliknite gumb Relaunch koji se pojavi na dnu stranice.

- Na Linuxu pokrenite preglednik s `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ima WebGPU omogućen po defaultu.  
- U Firefox Nightly, u adresnu traku upišite about:config i `set dom.webgpu.enabled to true`.

### Postavljanje GPU-a za Microsoft Edge  

Evo koraka za postavljanje GPU-a visokih performansi za Microsoft Edge na Windowsu:

- **Otvorite Postavke:** Kliknite na Start izbornik i odaberite Postavke.  
- **Sistemske postavke:** Idite na Sustav, a zatim na Prikaz.  
- **Postavke grafike:** Pomaknite se dolje i kliknite na Postavke grafike.  
- **Odaberite aplikaciju:** Pod "Odaberite aplikaciju za postavljanje preferenci," odaberite Desktop app, a zatim Pregledaj.  
- **Odaberite Edge:** Dođite do mape instalacije Edgea (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i odaberite `msedge.exe`.  
- **Postavite preferenciju:** Kliknite Opcije, odaberite Visoke performanse, zatim kliknite Spremi.  
Ovo će osigurati da Microsoft Edge koristi vaš GPU visokih performansi za bolje performanse.  
- **Ponovno pokrenite** računalo da bi ove postavke stupile na snagu.

### Primjeri : Molimo [kliknite ovaj link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.