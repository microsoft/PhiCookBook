<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:22:21+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "hr"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo za prikaz WebGPU i RAG obrasca
RAG obrazac s Phi-3 Onnx Hosted modelom koristi pristup Retrieval-Augmented Generation, spajajući snagu Phi-3 modela s ONNX hostingom za učinkovite AI implementacije. Ovaj obrazac je ključan za fino podešavanje modela za zadatke specifične za određena područja, nudeći kombinaciju kvalitete, isplativosti i razumijevanja dugih konteksta. Dio je Azure AI paketa, koji pruža širok izbor modela koji su jednostavni za pronalazak, isprobavanje i korištenje, prilagođavajući se potrebama različitih industrija. Phi-3 modeli, uključujući Phi-3-mini, Phi-3-small i Phi-3-medium, dostupni su u Azure AI Model Catalogu i mogu se fino podešavati i implementirati samostalno ili putem platformi poput HuggingFace i ONNX, pokazujući Microsoftovu predanost pristupačnim i učinkovitim AI rješenjima.

## Što je WebGPU
WebGPU je moderna web grafička API namijenjena za efikasan pristup grafičkoj procesorskoj jedinici (GPU) uređaja izravno iz web preglednika. Namijenjena je da naslijedi WebGL, donoseći nekoliko ključnih poboljšanja:

1. **Kompatibilnost s modernim GPU-ima**: WebGPU je dizajniran da besprijekorno radi s suvremenim GPU arhitekturama, koristeći sistemske API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opće GPU izračune i brže operacije, što ga čini prikladnim za grafički prikaz i zadatke strojnog učenja.
3. **Napredne značajke**: WebGPU omogućuje pristup naprednijim GPU mogućnostima, što omogućuje složenije i dinamičnije grafičke i računalne zadatke.
4. **Smanjen JavaScript teret**: Prebacivanjem više zadataka na GPU, WebGPU značajno smanjuje opterećenje JavaScripta, što rezultira boljim performansama i glađim iskustvom.

WebGPU je trenutno podržan u preglednicima poput Google Chromea, a rad na proširenju podrške na druge platforme je u tijeku.

### 03.WebGPU
Potrebno okruženje:

**Podržani preglednici:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogućavanje WebGPU-a:

- U Chrome/Microsoft Edge 

Omogućite zastavicu `chrome://flags/#enable-unsafe-webgpu`.

#### Otvorite preglednik:
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici s zastavicama:
U adresnu traku upišite `chrome://flags` i pritisnite Enter.

#### Potražite zastavicu:
U polje za pretraživanje na vrhu stranice upišite 'enable-unsafe-webgpu'

#### Omogućite zastavicu:
Pronađite #enable-unsafe-webgpu zastavicu na popisu rezultata.

Kliknite na padajući izbornik pored nje i odaberite Enabled.

#### Ponovno pokrenite preglednik:

Nakon omogućavanja zastavice, potrebno je ponovno pokrenuti preglednik da bi promjene stupile na snagu. Kliknite na gumb Relaunch koji se pojavi na dnu stranice.

- Za Linux, pokrenite preglednik s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU omogućen prema zadanim postavkama.
- U Firefox Nightly, upišite about:config u adresnu traku i postavite `dom.webgpu.enabled` na true.

### Postavljanje GPU-a za Microsoft Edge

Evo koraka za postavljanje visokoučinkovitog GPU-a za Microsoft Edge na Windowsu:

- **Otvorite Postavke:** Kliknite na Start izbornik i odaberite Postavke.
- **Sistemske postavke:** Idite na Sustav, zatim na Prikaz.
- **Postavke grafike:** Pomaknite se dolje i kliknite na Postavke grafike.
- **Odaberite aplikaciju:** Pod “Odaberite aplikaciju za postavljanje preferencija,” odaberite Desktop app, zatim Pregledaj.
- **Odaberite Edge:** Dođite do mape instalacije Edgea (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i odaberite `msedge.exe`.
- **Postavite preferenciju:** Kliknite Opcije, odaberite Visoke performanse, zatim kliknite Spremi.
Ovo će osigurati da Microsoft Edge koristi vaš visokoučinkoviti GPU za bolje performanse.
- **Ponovno pokrenite** računalo da bi postavke stupile na snagu.

### Otvorite svoj Codespace:
Idite u svoj repozitorij na GitHubu.
Kliknite na gumb Code i odaberite Open with Codespaces.

Ako još nemate Codespace, možete ga stvoriti klikom na New codespace.

**Note** Instalacija Node okruženja u vašem codespaceu
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

### Idite u direktorij svog projekta:
Koristite terminal da odete u direktorij gdje se nalazi vaš npm projekt:
```
cd path/to/your/project
```

### Instalirajte ovisnosti:
Pokrenite sljedeću naredbu za instalaciju svih potrebnih ovisnosti navedenih u vašem package.json:

```
npm install
```

### Pokrenite demo:
Nakon instalacije ovisnosti, možete pokrenuti demo skriptu. Obično je navedena u sekciji scripts vašeg package.json. Na primjer, ako se vaša demo skripta zove start, pokrenite:

```
npm run build
```
```
npm run dev
```

### Pristupite demou:
Ako vaš demo uključuje web poslužitelj, Codespaces će vam dati URL za pristup. Potražite obavijest ili provjerite karticu Ports za URL.

**Note:** Model treba biti keširan u pregledniku, pa učitavanje može potrajati.

### RAG Demo
Prenesite markdown datoteku `intro_rag.md` da biste dovršili RAG rješenje. Ako koristite codespaces, datoteku možete preuzeti iz `01.InferencePhi3/docs/`

### Odaberite svoju datoteku:
Kliknite na gumb “Choose File” da odaberete dokument koji želite prenijeti.

### Prenesite dokument:
Nakon odabira datoteke, kliknite na gumb “Upload” da učitate dokument za RAG (Retrieval-Augmented Generation).

### Započnite chat:
Nakon što je dokument prenesen, možete započeti chat sesiju koristeći RAG na temelju sadržaja vašeg dokumenta.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.