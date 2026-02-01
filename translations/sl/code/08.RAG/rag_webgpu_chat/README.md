Phi-3-mini WebGPU RAG Chatbot

## Demo za predstavitev WebGPU in RAG vzorca
RAG vzorec s Phi-3 Onnx gostovanim modelom uporablja pristop Retrieval-Augmented Generation, ki združuje moč Phi-3 modelov z ONNX gostovanjem za učinkovite AI rešitve. Ta vzorec je ključen za prilagajanje modelov za specifične naloge v določenih domenah, saj ponuja kombinacijo kakovosti, stroškovne učinkovitosti in razumevanja dolgih kontekstov. Je del Azure AI zbirke, ki ponuja širok nabor modelov, ki jih je enostavno najti, preizkusiti in uporabljati, ter zadovoljuje potrebe po prilagoditvah v različnih panogah. Phi-3 modeli, vključno s Phi-3-mini, Phi-3-small in Phi-3-medium, so na voljo v Azure AI Model Catalog in jih je mogoče prilagoditi ter namestiti samostojno ali preko platform, kot sta HuggingFace in ONNX, kar kaže na Microsoftovo zavezanost dostopnim in učinkovitih AI rešitvam.

## Kaj je WebGPU
WebGPU je sodoben spletni grafični API, zasnovan za učinkovito dostopanje do grafične procesne enote (GPU) naprave neposredno iz spletnih brskalnikov. Namenjen je kot naslednik WebGL in prinaša več ključnih izboljšav:

1. **Združljivost z modernimi GPU-ji**: WebGPU je zasnovan za nemoteno delovanje z današnjimi GPU arhitekturami, pri čemer uporablja sistemske API-je, kot so Vulkan, Metal in Direct3D 12.
2. **Izboljšana zmogljivost**: Podpira splošne GPU izračune in hitrejše operacije, zato je primeren tako za grafično upodabljanje kot tudi za naloge strojnega učenja.
3. **Napredne funkcije**: WebGPU omogoča dostop do bolj naprednih zmogljivosti GPU-ja, kar omogoča bolj kompleksne in dinamične grafične ter računske obremenitve.
4. **Zmanjšana obremenitev JavaScripta**: Z večjim prenosom nalog na GPU WebGPU znatno zmanjša obremenitev JavaScript kode, kar vodi do boljše zmogljivosti in gladke uporabniške izkušnje.

WebGPU je trenutno podprt v brskalnikih, kot je Google Chrome, potekajo pa dela za razširitev podpore na druge platforme.

### 03.WebGPU
Zahtevano okolje:

**Podprti brskalniki:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Omogočanje WebGPU:

- V Chrome/Microsoft Edge

Omogočite zastavico `chrome://flags/#enable-unsafe-webgpu`.

#### Odprite brskalnik:
Zaženite Google Chrome ali Microsoft Edge.

#### Dostop do strani z zastavicami:
V naslovno vrstico vpišite `chrome://flags` in pritisnite Enter.

#### Poiščite zastavico:
V iskalno polje na vrhu strani vpišite 'enable-unsafe-webgpu'

#### Omogočite zastavico:
Poiščite zastavico #enable-unsafe-webgpu med rezultati.

Kliknite na spustni meni zraven in izberite Enabled.

#### Ponovni zagon brskalnika:

Po omogočitvi zastavice je potrebno brskalnik znova zagnati, da spremembe začnejo veljati. Kliknite gumb Relaunch, ki se pojavi na dnu strani.

- Za Linux zaženite brskalnik z `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU privzeto omogočen.
- V Firefox Nightly v naslovno vrstico vpišite about:config in nastavite dom.webgpu.enabled na true.

### Nastavitev GPU za Microsoft Edge

Tukaj so koraki za nastavitev zmogljivega GPU-ja za Microsoft Edge na Windows:

- **Odprite Nastavitve:** Kliknite na Start meni in izberite Nastavitve.
- **Sistemske nastavitve:** Pojdite na Sistem in nato na Zaslon.
- **Grafične nastavitve:** Pomaknite se navzdol in kliknite na Grafične nastavitve.
- **Izberite aplikacijo:** Pod “Izberite aplikacijo za nastavitev prednosti” izberite Namizna aplikacija in nato Brskaj.
- **Izberite Edge:** Pomaknite se do mape z namestitvijo Edge (običajno `C:\Program Files (x86)\Microsoft\Edge\Application`) in izberite `msedge.exe`.
- **Nastavite prednost:** Kliknite Možnosti, izberite Visoka zmogljivost in nato Shrani.  
To bo zagotovilo, da Microsoft Edge uporablja vaš zmogljiv GPU za boljšo zmogljivost.  
- **Ponovni zagon** računalnika, da spremembe začnejo veljati.

### Odprite svoj Codespace:
Pojdite v svoj repozitorij na GitHubu.  
Kliknite na gumb Code in izberite Open with Codespaces.

Če še nimate Codespace, ga lahko ustvarite s klikom na New codespace.

**Opomba** Namestitev Node okolja v vašem codespace-u  
Zagon npm demo projekta iz GitHub Codespace je odličen način za testiranje in razvoj vašega projekta. Tukaj je korak za korakom vodič, ki vam pomaga začeti:

### Pripravite okolje:
Ko je Codespace odprt, preverite, ali imate nameščen Node.js in npm. To lahko preverite z ukazom:  
```
node -v
```  
```
npm -v
```

Če nista nameščena, ju lahko namestite z:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Pomaknite se v mapo projekta:
Uporabite terminal, da se premaknete v mapo, kjer se nahaja vaš npm projekt:  
```
cd path/to/your/project
```

### Namestite odvisnosti:
Za namestitev vseh potrebnih odvisnosti, navedenih v datoteki package.json, zaženite naslednji ukaz:  

```
npm install
```

### Zaženite demo:
Ko so odvisnosti nameščene, lahko zaženete demo skripto. Običajno je določena v razdelku scripts v package.json. Na primer, če je vaša demo skripta imenovana start, zaženite:  

```
npm run build
```  
```
npm run dev
```

### Dostop do demoja:
Če vaš demo vključuje spletni strežnik, vam bo Codespaces zagotovil URL za dostop. Poiščite obvestilo ali preverite zavihek Ports, da najdete URL.

**Opomba:** Model mora biti predpomnjen v brskalniku, zato lahko nalaganje traja nekaj časa.

### RAG Demo
Naložite markdown datoteko `intro_rag.md`, da dokončate RAG rešitev. Če uporabljate codespaces, lahko datoteko prenesete iz `01.InferencePhi3/docs/`

### Izberite svojo datoteko:
Kliknite gumb “Choose File” in izberite dokument, ki ga želite naložiti.

### Naložite dokument:
Po izbiri datoteke kliknite gumb “Upload”, da naložite dokument za RAG (Retrieval-Augmented Generation).

### Začnite klepet:
Ko je dokument naložen, lahko začnete klepetno sejo z uporabo RAG na podlagi vsebine vašega dokumenta.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.