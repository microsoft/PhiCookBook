<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-09-12T15:00:29+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "lt"
}
-->
Phi-3-mini WebGPU RAG pokalbių robotas

## Demonstracija, skirta parodyti WebGPU ir RAG modelį
RAG modelis su Phi-3 Onnx talpinamu modeliu naudoja Retrieval-Augmented Generation metodą, kuris sujungia Phi-3 modelių galimybes su ONNX talpinimu, siekiant efektyvaus AI diegimo. Šis modelis yra svarbus modelių pritaikymui specifinėms sritims, siūlant kokybės, ekonomiškumo ir ilgo konteksto supratimo derinį. Tai yra Azure AI dalis, kuri siūlo platų lengvai randamų, išbandomų ir naudojamų modelių pasirinkimą, pritaikytą įvairių pramonės šakų poreikiams. Phi-3 modeliai, įskaitant Phi-3-mini, Phi-3-small ir Phi-3-medium, yra prieinami Azure AI Model Catalog ir gali būti pritaikyti bei diegiami savarankiškai arba per platformas, tokias kaip HuggingFace ir ONNX, parodant Microsoft įsipareigojimą prieinamoms ir efektyvioms AI sprendimams.

## Kas yra WebGPU
WebGPU yra moderni interneto grafikos API, sukurta efektyviai pasiekti įrenginio grafikos procesorių (GPU) tiesiogiai iš interneto naršyklių. Ji skirta pakeisti WebGL, siūlydama keletą svarbių patobulinimų:

1. **Suderinamumas su šiuolaikiniais GPU**: WebGPU yra sukurta sklandžiai veikti su šiuolaikinėmis GPU architektūromis, naudojant sistemų API, tokias kaip Vulkan, Metal ir Direct3D 12.
2. **Pagerintas našumas**: Ji palaiko bendros paskirties GPU skaičiavimus ir greitesnes operacijas, todėl tinka tiek grafikos atvaizdavimui, tiek mašininio mokymosi užduotims.
3. **Pažangios funkcijos**: WebGPU suteikia prieigą prie pažangesnių GPU galimybių, leidžiančių sudėtingesnes ir dinamiškesnes grafikos bei skaičiavimo užduotis.
4. **Sumažintas JavaScript darbo krūvis**: Perkeldama daugiau užduočių į GPU, WebGPU žymiai sumažina JavaScript darbo krūvį, užtikrindama geresnį našumą ir sklandesnę patirtį.

WebGPU šiuo metu palaikoma naršyklėse, tokiose kaip Google Chrome, ir vyksta darbas, siekiant išplėsti palaikymą kitoms platformoms.

### 03.WebGPU
Reikalinga aplinka:

**Palaikomos naršyklės:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU įjungimas:

- Chrome/Microsoft Edge 

Įjunkite `chrome://flags/#enable-unsafe-webgpu` nustatymą.

#### Atidarykite naršyklę:
Paleiskite Google Chrome arba Microsoft Edge.

#### Pasiekite nustatymų puslapį:
Adreso juostoje įveskite `chrome://flags` ir paspauskite Enter.

#### Ieškokite nustatymo:
Paieškos laukelyje viršuje įveskite 'enable-unsafe-webgpu'.

#### Įjunkite nustatymą:
Rezultatų sąraše suraskite #enable-unsafe-webgpu nustatymą.

Spustelėkite išskleidžiamąjį meniu šalia jo ir pasirinkite Enabled.

#### Perkraukite naršyklę:

Po nustatymo įjungimo, turėsite perkrauti naršyklę, kad pakeitimai įsigaliotų. Spustelėkite mygtuką Relaunch, kuris pasirodys puslapio apačioje.

- Linux sistemoje paleiskite naršyklę su `--enable-features=Vulkan`.
- Safari 18 (macOS 15) turi WebGPU įjungtą pagal numatymą.
- Firefox Nightly naršyklėje įveskite about:config adreso juostoje ir nustatykite `dom.webgpu.enabled` į true.

### GPU nustatymas Microsoft Edge naršyklėje 

Štai žingsniai, kaip nustatyti aukštos kokybės GPU Microsoft Edge naršyklėje Windows sistemoje:

- **Atidarykite nustatymus:** Spustelėkite Start meniu ir pasirinkite Settings.
- **Sistemos nustatymai:** Eikite į System, tada Display.
- **Grafikos nustatymai:** Slinkite žemyn ir spustelėkite Graphics settings.
- **Pasirinkite programą:** Skiltyje “Choose an app to set preference” pasirinkite Desktop app ir tada Browse.
- **Pasirinkite Edge:** Naršykite iki Edge diegimo aplanko (dažniausiai `C:\Program Files (x86)\Microsoft\Edge\Application`) ir pasirinkite `msedge.exe`.
- **Nustatykite prioritetą:** Spustelėkite Options, pasirinkite High performance ir tada spustelėkite Save.
Tai užtikrins, kad Microsoft Edge naudos jūsų aukštos kokybės GPU geresniam našumui. 
- **Perkraukite** kompiuterį, kad šie nustatymai įsigaliotų.

### Atidarykite savo Codespace:
Eikite į savo saugyklą GitHub.
Spustelėkite Code mygtuką ir pasirinkite Open with Codespaces.

Jei dar neturite Codespace, galite sukurti naują spustelėdami New codespace.

**Pastaba** Node aplinkos diegimas jūsų Codespace
npm demonstracijos paleidimas iš GitHub Codespace yra puikus būdas išbandyti ir kurti savo projektą. Štai žingsniai, kaip pradėti:

### Nustatykite aplinką:
Kai jūsų Codespace atidarytas, įsitikinkite, kad turite įdiegtą Node.js ir npm. Tai galite patikrinti paleisdami:
```
node -v
```
```
npm -v
```

Jei jie nėra įdiegti, galite juos įdiegti naudodami:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Eikite į savo projekto katalogą:
Naudokite terminalą, kad pereitumėte į katalogą, kuriame yra jūsų npm projektas:
```
cd path/to/your/project
```

### Įdiekite priklausomybes:
Paleiskite šią komandą, kad įdiegtumėte visas reikalingas priklausomybes, nurodytas jūsų package.json faile:

```
npm install
```

### Paleiskite demonstraciją:
Kai priklausomybės įdiegtos, galite paleisti savo demonstracinį scenarijų. Paprastai tai nurodyta scripts skiltyje jūsų package.json faile. Pavyzdžiui, jei jūsų demonstracinis scenarijus pavadintas start, galite paleisti:

```
npm run build
```
```
npm run dev
```

### Pasiekite demonstraciją:
Jei jūsų demonstracija apima interneto serverį, Codespaces suteiks URL, kad galėtumėte jį pasiekti. Ieškokite pranešimo arba patikrinkite Ports skiltį, kad rastumėte URL.

**Pastaba:** Modelis turi būti talpinamas naršyklėje, todėl gali užtrukti, kol jis bus įkeltas.

### RAG demonstracija
Įkelkite markdown failą `intro_rag.md`, kad užbaigtumėte RAG sprendimą. Jei naudojate Codespaces, galite atsisiųsti failą, esantį `01.InferencePhi3/docs/`.

### Pasirinkite savo failą:
Spustelėkite mygtuką “Choose File”, kad pasirinktumėte dokumentą, kurį norite įkelti.

### Įkelkite dokumentą:
Pasirinkę failą, spustelėkite “Upload” mygtuką, kad įkeltumėte dokumentą RAG (Retrieval-Augmented Generation) sprendimui.

### Pradėkite pokalbį:
Kai dokumentas įkeltas, galite pradėti pokalbio sesiją naudodami RAG, remdamiesi jūsų dokumento turiniu.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.