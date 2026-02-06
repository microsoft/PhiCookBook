# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo WebGPU ja RAG mustri tutvustamiseks

RAG muster koos Phi-3.5 Onnx Hostitud mudeliga kasutab Retrieval-Augmented Generation lähenemist, ühendades Phi-3.5 mudelite võimsuse ONNX hostimisega tõhusate tehisintellekti juurutuste jaoks. See muster on oluline mudelite peenhäälestamiseks valdkonnapõhiste ülesannete jaoks, pakkudes kvaliteedi, kulutõhususe ja pika konteksti mõistmise kombinatsiooni. See on osa Azure AI tööriistakomplektist, mis pakub laia valikut mudeleid, mida on lihtne leida, proovida ja kasutada, rahuldades erinevate tööstusharude kohandamisvajadusi.

## Mis on WebGPU
WebGPU on kaasaegne veebigraafika API, mis on loodud pakkuma tõhusat juurdepääsu seadme graafikaprotsessorile (GPU) otse veebibrauseritest. See on mõeldud WebGL-i järglasena, pakkudes mitmeid olulisi täiustusi:

1. **Ühilduvus kaasaegsete GPU-dega**: WebGPU on loodud töötama sujuvalt kaasaegsete GPU arhitektuuridega, kasutades süsteemi API-sid nagu Vulkan, Metal ja Direct3D 12.
2. **Parendatud jõudlus**: See toetab üldotstarbelisi GPU arvutusi ja kiiremaid toiminguid, muutes selle sobivaks nii graafika renderdamiseks kui ka masinõppe ülesannete jaoks.
3. **Täpsemad funktsioonid**: WebGPU võimaldab juurdepääsu keerukamatele ja dünaamilisematele graafika- ja arvutuskoormustele.
4. **Väiksem JavaScripti koormus**: Rohkemate ülesannete GPU-le delegeerimisega vähendab WebGPU oluliselt JavaScripti koormust, pakkudes paremat jõudlust ja sujuvamat kasutuskogemust.

WebGPU-d toetavad praegu sellised brauserid nagu Google Chrome, ning tööd tehakse selleks, et laiendada tuge ka teistele platvormidele.

### 03.WebGPU
Nõutav keskkond:

**Toetatud brauserid:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU lubamine:

- Chrome'is/Microsoft Edge'is 

Luba `chrome://flags/#enable-unsafe-webgpu` lipp.

#### Ava oma brauser:
Käivita Google Chrome või Microsoft Edge.

#### Juurdepääs lippude lehele:
Sisesta aadressiribale `chrome://flags` ja vajuta Enter.

#### Otsi lippu:
Sisesta otsingukasti ülaosas 'enable-unsafe-webgpu'.

#### Luba lipp:
Leia tulemuste loendist #enable-unsafe-webgpu lipp.

Klõpsa selle kõrval olevat rippmenüüd ja vali Enabled.

#### Taaskäivita brauser:

Pärast lipu lubamist pead brauseri muudatuste jõustumiseks taaskäivitama. Klõpsa lehe allosas kuvatavat nuppu Relaunch.

- Linuxi puhul käivita brauser käsuga `--enable-features=Vulkan`.
- Safari 18 (macOS 15) puhul on WebGPU vaikimisi lubatud.
- Firefox Nightly's sisesta aadressiribale about:config ja `määra dom.webgpu.enabled väärtuseks true`.

### GPU seadistamine Microsoft Edge'i jaoks

Siin on juhised, kuidas seadistada Windowsis Microsoft Edge'i jaoks suure jõudlusega GPU:

- **Ava Seaded:** Klõpsa Start-menüül ja vali Seaded.
- **Süsteemi seaded:** Mine jaotisse Süsteem ja seejärel Ekraan.
- **Graafikaseaded:** Kerige alla ja klõpsake Graafikaseaded.
- **Vali rakendus:** Jaotises „Vali rakendus eelistuse seadmiseks” vali Töölaudrakendus ja seejärel Sirvi.
- **Vali Edge:** Navigeeri Edge'i installikausta (tavaliselt `C:\Program Files (x86)\Microsoft\Edge\Application`) ja vali `msedge.exe`.
- **Seadista eelistus:** Klõpsa Valikud, vali Kõrge jõudlus ja seejärel klõpsa Salvesta.
See tagab, et Microsoft Edge kasutab parema jõudluse saavutamiseks sinu suure jõudlusega GPU-d.
- **Taaskäivita** oma arvuti, et need seaded jõustuksid.

### Näited: Palun [klõpsa sellele lingile](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.