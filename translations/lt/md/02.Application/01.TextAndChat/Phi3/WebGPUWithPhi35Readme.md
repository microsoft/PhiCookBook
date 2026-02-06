# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demonstracija, skirta parodyti WebGPU ir RAG modelį

RAG modelis su Phi-3.5 Onnx Hosted modeliu naudoja Retrieval-Augmented Generation metodą, kuris sujungia Phi-3.5 modelių galimybes su ONNX talpinimu, siekiant efektyvaus AI diegimo. Šis modelis yra svarbus norint pritaikyti modelius specifinėms sritims, siūlant kokybės, ekonomiškumo ir ilgo konteksto supratimo derinį. Tai yra Azure AI dalis, kuri siūlo platų modelių pasirinkimą, lengvai randamą, išbandomą ir pritaikomą įvairių pramonės šakų poreikiams.

## Kas yra WebGPU
WebGPU yra moderni interneto grafikos API, sukurta tam, kad efektyviai pasiektų įrenginio grafinį procesorių (GPU) tiesiai iš interneto naršyklių. Ji yra skirta pakeisti WebGL, siūlydama keletą svarbių patobulinimų:

1. **Suderinamumas su šiuolaikiniais GPU**: WebGPU yra sukurta taip, kad sklandžiai veiktų su šiuolaikinėmis GPU architektūromis, naudojant sistemines API, tokias kaip Vulkan, Metal ir Direct3D 12.
2. **Pagerintas našumas**: Ji palaiko bendros paskirties GPU skaičiavimus ir greitesnes operacijas, todėl tinka tiek grafikos atvaizdavimui, tiek mašininio mokymosi užduotims.
3. **Pažangios funkcijos**: WebGPU suteikia prieigą prie pažangesnių GPU galimybių, leidžiančių atlikti sudėtingesnius ir dinamiškesnius grafikos bei skaičiavimo darbus.
4. **Sumažinta JavaScript apkrova**: Perkeldama daugiau užduočių į GPU, WebGPU žymiai sumažina JavaScript apkrovą, užtikrindama geresnį našumą ir sklandesnę patirtį.

WebGPU šiuo metu palaikoma tokiose naršyklėse kaip Google Chrome, o darbas tęsiamas siekiant išplėsti palaikymą kitose platformose.

### 03.WebGPU
Reikalinga aplinka:

**Palaikomos naršyklės:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU įjungimas:

- Chrome/Microsoft Edge naršyklėse 

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

Po nustatymo įjungimo turėsite perkrauti naršyklę, kad pakeitimai įsigaliotų. Spustelėkite mygtuką Relaunch, kuris pasirodys puslapio apačioje.

- Linux sistemoje paleiskite naršyklę su `--enable-features=Vulkan`.
- Safari 18 (macOS 15) turi WebGPU įjungtą pagal numatytuosius nustatymus.
- Firefox Nightly naršyklėje įveskite about:config adreso juostoje ir nustatykite `dom.webgpu.enabled` į true.

### GPU nustatymas Microsoft Edge naršyklei 

Štai žingsniai, kaip nustatyti aukštos kokybės GPU Microsoft Edge naršyklėje Windows sistemoje:

- **Atidarykite nustatymus:** Spustelėkite Start meniu ir pasirinkite Settings.
- **Sistemos nustatymai:** Eikite į System, tada Display.
- **Grafikos nustatymai:** Slinkite žemyn ir spustelėkite Graphics settings.
- **Pasirinkite programą:** Skiltyje „Choose an app to set preference“ pasirinkite Desktop app ir tada Browse.
- **Pasirinkite Edge:** Naršykite iki Edge diegimo aplanko (dažniausiai `C:\Program Files (x86)\Microsoft\Edge\Application`) ir pasirinkite `msedge.exe`.
- **Nustatykite prioritetą:** Spustelėkite Options, pasirinkite High performance ir tada spustelėkite Save.
Tai užtikrins, kad Microsoft Edge naudos jūsų aukštos kokybės GPU geresniam našumui.
- **Perkraukite** kompiuterį, kad šie nustatymai įsigaliotų.

### Pavyzdžiai: Prašome [spustelėti šią nuorodą](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.