Phi-3-mini WebGPU RAG Chatbot

## Demo WebGPU ja RAG mustri tutvustamiseks
RAG muster koos Phi-3 Onnx Hosted mudeliga kasutab Retrieval-Augmented Generation lähenemist, ühendades Phi-3 mudelite võimsuse ONNX hostimisega tõhusate AI lahenduste jaoks. See muster on oluline mudelite peenhäälestamiseks valdkonnapõhiste ülesannete jaoks, pakkudes kvaliteedi, kulutõhususe ja pika konteksti mõistmise kombinatsiooni. See on osa Azure AI lahendustest, pakkudes laia valikut mudeleid, mida on lihtne leida, proovida ja kasutada, vastates erinevate tööstusharude kohandamisvajadustele. Phi-3 mudelid, sealhulgas Phi-3-mini, Phi-3-small ja Phi-3-medium, on saadaval Azure AI mudelikataloogis ning neid saab peenhäälestada ja juurutada iseseisvalt või platvormide kaudu nagu HuggingFace ja ONNX, näidates Microsofti pühendumust ligipääsetavatele ja tõhusatele AI lahendustele.

## Mis on WebGPU
WebGPU on kaasaegne veebigraafika API, mis on loodud pakkuma tõhusat juurdepääsu seadme graafikaprotsessorile (GPU) otse veebibrauseritest. See on mõeldud WebGL-i järglaseks, pakkudes mitmeid olulisi täiustusi:

1. **Ühilduvus kaasaegsete GPU-dega**: WebGPU on loodud töötama sujuvalt kaasaegsete GPU arhitektuuridega, kasutades süsteemi API-sid nagu Vulkan, Metal ja Direct3D 12.
2. **Parendatud jõudlus**: See toetab üldotstarbelisi GPU arvutusi ja kiiremaid operatsioone, muutes selle sobivaks nii graafika renderdamiseks kui ka masinõppe ülesannete jaoks.
3. **Täiustatud funktsioonid**: WebGPU pakub juurdepääsu keerukamatele GPU võimalustele, võimaldades keerukamaid ja dünaamilisemaid graafika- ja arvutuskoormusi.
4. **Vähendatud JavaScripti koormus**: Rohkem ülesandeid GPU-le üle kandes vähendab WebGPU oluliselt JavaScripti koormust, pakkudes paremat jõudlust ja sujuvamat kasutuskogemust.

WebGPU on praegu toetatud brauserites nagu Google Chrome, ning tööd tehakse selle toetuse laiendamiseks teistele platvormidele.

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

#### Juurdepääs lipu lehele:
Sisesta aadressiribale `chrome://flags` ja vajuta Enter.

#### Otsi lippu:
Sisesta otsingukasti ülaosas 'enable-unsafe-webgpu'.

#### Luba lipp:
Leia tulemuste loendist #enable-unsafe-webgpu lipp.

Klõpsa selle kõrval olevat rippmenüüd ja vali Enabled.

#### Taaskäivita brauser:

Pärast lipu lubamist tuleb brauseri muudatuste jõustumiseks taaskäivitada. Klõpsa lehe allosas kuvatavat Relaunch nuppu.

- Linuxi puhul käivita brauser `--enable-features=Vulkan` abil.
- Safari 18 (macOS 15) on WebGPU vaikimisi lubatud.
- Firefox Nightly puhul sisesta aadressiribale about:config ja `set dom.webgpu.enabled to true`.

### GPU seadistamine Microsoft Edge jaoks 

Siin on juhised, kuidas seadistada Microsoft Edge'i jaoks Windowsis suure jõudlusega GPU:

- **Ava Seaded:** Klõpsa Start menüül ja vali Seaded.
- **Süsteemi seaded:** Mine Süsteem ja seejärel Kuva.
- **Graafikaseaded:** Kerige alla ja klõpsake Graafikaseaded.
- **Vali rakendus:** Valiku „Vali rakendus eelistuse seadistamiseks“ all vali Töölauda rakendus ja seejärel Sirvi.
- **Vali Edge:** Navigeeri Edge'i installikausta (tavaliselt `C:\Program Files (x86)\Microsoft\Edge\Application`) ja vali `msedge.exe`.
- **Seadista eelistus:** Klõpsa Valikud, vali Kõrge jõudlus ja seejärel klõpsa Salvesta.
See tagab, et Microsoft Edge kasutab parema jõudluse jaoks teie suure jõudlusega GPU-d. 
- **Taaskäivita** oma arvuti, et need seaded jõustuksid.

### Ava oma Codespace:
Navigeeri oma GitHubi repositooriumisse.
Klõpsa nupul Kood ja vali Ava Codespaces'iga.

Kui sul pole veel Codespace'i, saad selle luua, klõpsates Uus Codespace.

**Märkus** Node keskkonna installimine Codespace'is
npm demo käivitamine GitHub Codespace'ist on suurepärane viis oma projekti testimiseks ja arendamiseks. Siin on samm-sammuline juhend alustamiseks:

### Seadista oma keskkond:
Kui Codespace on avatud, veendu, et Node.js ja npm oleksid installitud. Seda saab kontrollida käivitades:
```
node -v
```
```
npm -v
```

Kui need pole installitud, saad need installida kasutades:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigeeri oma projekti kataloogi:
Kasuta terminali, et navigeerida kataloogi, kus asub sinu npm projekt:
```
cd path/to/your/project
```

### Paigalda sõltuvused:
Käivita järgmine käsk, et paigaldada kõik vajalikud sõltuvused, mis on loetletud sinu package.json failis:

```
npm install
```

### Käivita demo:
Kui sõltuvused on paigaldatud, saad käivitada oma demo skripti. See on tavaliselt määratud package.json failis skriptide sektsioonis. Näiteks, kui sinu demo skripti nimi on start, saad käivitada:

```
npm run build
```
```
npm run dev
```

### Juurdepääs demole:
Kui sinu demo hõlmab veebiserverit, pakub Codespaces URL-i sellele juurdepääsuks. Otsi teavitust või kontrolli Ports vahekaarti, et leida URL.

**Märkus:** Mudel tuleb brauseris vahemällu salvestada, seega võib selle laadimine aega võtta.

### RAG Demo
Laadi üles markdown fail `intro_rag.md`, et lõpetada RAG lahendus. Kui kasutad Codespaces'i, saad faili alla laadida asukohast `01.InferencePhi3/docs/`.

### Vali oma fail:
Klõpsa nupul „Vali fail“, et valida dokument, mida soovid üles laadida.

### Laadi dokument üles:
Pärast faili valimist klõpsa nupul „Laadi üles“, et laadida oma dokument RAG (Retrieval-Augmented Generation) jaoks.

### Alusta vestlust:
Kui dokument on üles laaditud, saad alustada vestlussessiooni, kasutades RAG-i oma dokumendi sisu põhjal.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.