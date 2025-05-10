<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:23:57+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "hr"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo za prikaz WebGPU i RAG obrasca
RAG obrazac s Phi-3 Onnx Hosted modelom koristi pristup Retrieval-Augmented Generation, kombinirajući snagu Phi-3 modela s ONNX hostingom za učinkovite AI implementacije. Ovaj obrazac je ključan za fino podešavanje modela za zadatke specifične za određene domene, nudeći spoj kvalitete, isplativosti i razumijevanja dugog konteksta. Dio je Azure AI paketa, pružajući širok izbor modela koji su jednostavni za pronalazak, isprobavanje i korištenje, prilagođeni potrebama različitih industrija. Phi-3 modeli, uključujući Phi-3-mini, Phi-3-small i Phi-3-medium, dostupni su u Azure AI Model Catalogu i mogu se fino podešavati i implementirati samostalno ili preko platformi poput HuggingFace i ONNX, pokazujući Microsoftovu predanost pristupačnim i učinkovitim AI rješenjima.

## Što je WebGPU
WebGPU je moderni web grafički API dizajniran za efikasan pristup grafičkoj procesnoj jedinici (GPU) uređaja izravno iz web preglednika. Namijenjen je kao nasljednik WebGL-a, donoseći nekoliko ključnih poboljšanja:

1. **Kompatibilnost s modernim GPU-ima**: WebGPU je izgrađen da besprijekorno radi s suvremenim GPU arhitekturama, koristeći sustavne API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opće računalne zadatke na GPU-u i brže operacije, što ga čini pogodnim i za grafički prikaz i za zadatke strojnog učenja.
3. **Napredne značajke**: WebGPU omogućuje pristup naprednijim GPU mogućnostima, što omogućava složenije i dinamičnije grafičke i računalne zadatke.
4. **Smanjen JavaScript workload**: Prebacivanjem više zadataka na GPU, WebGPU značajno smanjuje opterećenje na JavaScript, što rezultira boljim performansama i glatkijim iskustvom.

WebGPU je trenutno podržan u preglednicima poput Google Chromea, a radi se na proširenju podrške i na druge platforme.

### 03.WebGPU
Potrebno okruženje:

**Podržani preglednici:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogućite WebGPU:

- U Chrome/Microsoft Edge

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite preglednik:
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici s zastavicama:
U adresnu traku upišite `chrome://flags` i pritisnite Enter.

#### Potražite zastavicu:
U polju za pretraživanje na vrhu stranice upišite 'enable-unsafe-webgpu'

#### Omogućite zastavicu:
Pronađite #enable-unsafe-webgpu zastavicu na popisu rezultata.

Kliknite na padajući izbornik pored nje i odaberite Enabled.

#### Ponovno pokrenite preglednik:

Nakon omogućavanja zastavice, potrebno je ponovno pokrenuti preglednik da bi promjene stupile na snagu. Kliknite na gumb Relaunch koji se pojavi na dnu stranice.

- Na Linuxu pokrenite preglednik s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU omogućen prema zadanim postavkama.
- U Firefox Nightly, u adresnu traku unesite about:config i `set dom.webgpu.enabled to true`.

### Postavljanje GPU-a za Microsoft Edge

Evo koraka za postavljanje visokoučinkovitog GPU-a za Microsoft Edge na Windowsu:

- **Otvorite Postavke:** Kliknite na Start izbornik i odaberite Postavke.
- **Sistemske postavke:** Idite na Sustav, zatim Prikaz.
- **Grafičke postavke:** Pomaknite se dolje i kliknite na Grafičke postavke.
- **Odaberite aplikaciju:** Pod “Odaberite aplikaciju za postavljanje preferenci,” odaberite Desktop app i zatim Pregledaj.
- **Odaberite Edge:** Dođite do mape instalacije Edgea (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i odaberite `msedge.exe`.
- **Postavite preferenciju:** Kliknite Opcije, odaberite Visoke performanse, zatim kliknite Spremi.
Ovo će osigurati da Microsoft Edge koristi vaš visokoučinkoviti GPU za bolje performanse.
- **Ponovno pokrenite** računalo da bi ove postavke stupile na snagu.

### Otvorite svoj Codespace:
Idite na svoj repozitorij na GitHubu.
Kliknite na gumb Code i odaberite Open with Codespaces.

Ako još nemate Codespace, možete ga kreirati klikom na New codespace.

**Napomena** Instalacija Node okruženja u vašem codespaceu
Pokretanje npm demo projekta iz GitHub Codespacea odličan je način za testiranje i razvoj vašeg projekta. Evo vodiča korak po korak za početak:

### Postavite svoje okruženje:
Kad se Codespace otvori, provjerite imate li instalirane Node.js i npm. To možete provjeriti pokretanjem:
```
node -v
```
```
npm -v
```

Ako nisu instalirani, možete ih instalirati pomoću:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Idite u direktorij vašeg projekta:
Koristite terminal da odete u direktorij gdje se nalazi vaš npm projekt:
```
cd path/to/your/project
```

### Instalirajte ovisnosti:
Pokrenite sljedeću naredbu da instalirate sve potrebne ovisnosti navedene u vašoj package.json datoteci:

```
npm install
```

### Pokrenite demo:
Kad su ovisnosti instalirane, možete pokrenuti svoj demo skriptu. Obično je navedena u sekciji scripts vaše package.json datoteke. Na primjer, ako se vaša demo skripta zove start, pokrenite:

```
npm run build
```
```
npm run dev
```

### Pristupite demou:
Ako vaš demo uključuje web poslužitelj, Codespaces će vam dati URL za pristup. Potražite obavijest ili provjerite karticu Ports da pronađete URL.

**Napomena:** Model se mora keširati u pregledniku, pa učitavanje može potrajati.

### RAG Demo
Učitajte markdown datoteku `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Odaberite svoju datoteku:
Kliknite na gumb “Choose File” kako biste odabrali dokument koji želite učitati.

### Učitajte dokument:
Nakon odabira datoteke, kliknite na gumb “Upload” kako biste učitali dokument za RAG (Retrieval-Augmented Generation).

### Započnite chat:
Nakon što je dokument učitan, možete započeti chat sesiju koristeći RAG na temelju sadržaja vašeg dokumenta.

**Odricanje od odgovornosti**:  
Ovaj je dokument preveden pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.