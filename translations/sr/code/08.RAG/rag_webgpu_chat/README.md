<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:23:35+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sr"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo za prikazivanje WebGPU i RAG obrasca  
RAG obrazac sa Phi-3 Onnx Hosted modelom koristi pristup Retrieval-Augmented Generation, kombinujući snagu Phi-3 modela sa ONNX hostingom za efikasne AI implementacije. Ovaj obrazac je ključan za fino podešavanje modela za zadatke specifične za određenu oblast, nudeći spoj kvaliteta, isplativosti i razumevanja dugog konteksta. Deo je Azure AI paketa, pružajući širok izbor modela koji su laki za pronalaženje, isprobavanje i korišćenje, prilagođavajući se potrebama različitih industrija. Phi-3 modeli, uključujući Phi-3-mini, Phi-3-small i Phi-3-medium, dostupni su u Azure AI Model Catalog-u i mogu se fino podešavati i implementirati samostalno ili preko platformi kao što su HuggingFace i ONNX, što pokazuje Microsoftovu posvećenost dostupnim i efikasnim AI rešenjima.

## Šta je WebGPU  
WebGPU je moderan web grafički API dizajniran da omogući efikasan pristup grafičkom procesoru (GPU) uređaja direktno iz web pregledača. Namenjen je da bude naslednik WebGL-a, donoseći nekoliko ključnih poboljšanja:

1. **Kompatibilnost sa modernim GPU-ovima**: WebGPU je napravljen da besprekorno radi sa savremenim GPU arhitekturama, koristeći sistemske API-je kao što su Vulkan, Metal i Direct3D 12.  
2. **Poboljšane performanse**: Podržava generalne GPU proračune i brže operacije, što ga čini pogodnim za grafičko renderovanje i zadatke mašinskog učenja.  
3. **Napredne funkcije**: WebGPU omogućava pristup naprednijim GPU mogućnostima, dozvoljavajući složenije i dinamičnije grafičke i računarske zadatke.  
4. **Smanjenje opterećenja JavaScript-a**: Prebacivanjem većeg dela posla na GPU, WebGPU značajno smanjuje opterećenje JavaScript-a, što vodi ka boljim performansama i glađem iskustvu.

WebGPU je trenutno podržan u pregledačima kao što je Google Chrome, uz rad na proširenju podrške na druge platforme.

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
U adresnoj liniji otkucajte `chrome://flags` i pritisnite Enter.

#### Potražite zastavicu:  
U polju za pretragu na vrhu stranice otkucajte 'enable-unsafe-webgpu'

#### Omogućite zastavicu:  
Pronađite #enable-unsafe-webgpu zastavicu u listi rezultata.

Kliknite na padajući meni pored i izaberite Enabled.

#### Restartujte pregledač:  

Nakon omogućavanja zastavice, potrebno je da restartujete pregledač da bi promene stupile na snagu. Kliknite na dugme Relaunch koje se pojavi na dnu stranice.

- Za Linux, pokrenite pregledač sa `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ima WebGPU podrazumevano omogućen.  
- U Firefox Nightly, unesite about:config u adresnu liniju i `set dom.webgpu.enabled to true`.

### Podešavanje GPU-a za Microsoft Edge  

Evo koraka za podešavanje GPU-a visokih performansi za Microsoft Edge na Windows-u:

- **Otvorite Settings:** Kliknite na Start meni i izaberite Settings.  
- **Podešavanja sistema:** Idite na System pa Display.  
- **Grafička podešavanja:** Skrolujte dole i kliknite na Graphics settings.  
- **Izaberite aplikaciju:** Pod „Choose an app to set preference,“ izaberite Desktop app pa Browse.  
- **Izaberite Edge:** Navigirajte do foldera gde je instaliran Edge (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i izaberite `msedge.exe`.  
- **Postavite preferencu:** Kliknite Options, izaberite High performance i zatim kliknite Save.  
Ovo će osigurati da Microsoft Edge koristi vaš GPU visokih performansi za bolje performanse.  
- **Restartujte** računar da bi podešavanja stupila na snagu.

### Otvorite svoj Codespace:  
Idite na vaš repozitorijum na GitHub-u.  
Kliknite na dugme Code i izaberite Open with Codespaces.

Ako još nemate Codespace, možete ga napraviti klikom na New codespace.

**Napomena** Instalacija Node okruženja u vašem codespace-u  
Pokretanje npm demo aplikacije iz GitHub Codespace-a je odličan način da testirate i razvijate vaš projekat. Evo vodiča korak po korak da započnete:

### Pripremite okruženje:  
Kada se Codespace otvori, proverite da li imate instalirane Node.js i npm. To možete proveriti pokretanjem:  
```
node -v
```  
```
npm -v
```

Ako nisu instalirani, možete ih instalirati koristeći:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Pređite u direktorijum vašeg projekta:  
Koristite terminal da odete u direktorijum gde se nalazi vaš npm projekat:  
```
cd path/to/your/project
```

### Instalirajte zavisnosti:  
Pokrenite sledeću komandu da instalirate sve potrebne zavisnosti navedene u package.json fajlu:  

```
npm install
```

### Pokrenite demo:  
Kada su zavisnosti instalirane, možete pokrenuti demo skriptu. Obično je navedena u scripts delu package.json. Na primer, ako se demo skripta zove start, pokrenite:  

```
npm run build
```  
```
npm run dev
```

### Pristupite demou:  
Ako vaš demo uključuje web server, Codespaces će vam dati URL za pristup. Obratite pažnju na notifikacije ili proverite karticu Ports da pronađete URL.

**Napomena:** Model mora biti keširan u pregledaču, pa može potrajati dok se učita.

### RAG Demo  
Otpremite markdown fajl `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Izaberite fajl:  
Kliknite na dugme „Choose File“ da odaberete dokument koji želite da otpremite.

### Otpremite dokument:  
Nakon što izaberete fajl, kliknite na dugme „Upload“ da učitate dokument za RAG (Retrieval-Augmented Generation).

### Pokrenite ćaskanje:  
Kada je dokument otpremljen, možete započeti ćaskanje koristeći RAG na osnovu sadržaja vašeg dokumenta.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.