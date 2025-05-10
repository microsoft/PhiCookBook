<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:24:11+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sl"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo za prikaz WebGPU in RAG vzorca
RAG vzorec s Phi-3 Onnx gostovanim modelom izkorišča pristop Retrieval-Augmented Generation, ki združuje moč Phi-3 modelov z ONNX gostovanjem za učinkovite AI rešitve. Ta vzorec je ključen za fino prilagajanje modelov za specifične domene, saj ponuja kombinacijo kakovosti, stroškovne učinkovitosti in razumevanja dolgih kontekstov. Je del Azure AI zbirke, ki ponuja širok nabor modelov, ki jih je enostavno najti, preizkusiti in uporabiti, prilagojene potrebam različnih industrij. Phi-3 modeli, vključno s Phi-3-mini, Phi-3-small in Phi-3-medium, so na voljo v Azure AI Model Catalogu in jih je mogoče fino nastaviti ter uvajati samostojno ali preko platform, kot sta HuggingFace in ONNX, kar kaže na Microsoftovo zavezanost k dostopnim in učinkovitim AI rešitvam.

## Kaj je WebGPU
WebGPU je sodoben spletni grafični API, zasnovan za učinkovito dostopanje do grafične procesne enote (GPU) naprave neposredno iz spletnih brskalnikov. Namenjen je kot naslednik WebGL in prinaša več ključnih izboljšav:

1. **Združljivost z modernimi GPU-ji**: WebGPU je zasnovan za nemoteno delovanje z današnjimi GPU arhitekturami, pri čemer uporablja sistemske API-je, kot so Vulkan, Metal in Direct3D 12.
2. **Izboljšana zmogljivost**: Podpira splošne GPU izračune in hitrejše operacije, zato je primeren tako za grafično upodabljanje kot za naloge strojnega učenja.
3. **Napredne funkcije**: WebGPU omogoča dostop do bolj naprednih zmogljivosti GPU-ja, kar omogoča bolj kompleksne in dinamične grafične ter računske naloge.
4. **Zmanjšana obremenitev JavaScript-a**: S prenosom več nalog na GPU WebGPU znatno zmanjša obremenitev JavaScript-a, kar vodi do boljše zmogljivosti in bolj gladke izkušnje.

WebGPU trenutno podpirajo brskalniki, kot je Google Chrome, delo pa poteka za razširitev podpore tudi na druge platforme.

### 03.WebGPU
Zahtevano okolje:

**Podprti brskalniki:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogočite WebGPU:

- V Chrome/Microsoft Edge

Omogočite zastavico `chrome://flags/#enable-unsafe-webgpu`.

#### Odprite svoj brskalnik:
Zaženite Google Chrome ali Microsoft Edge.

#### Dostop do strani z zastavicami:
V naslovno vrstico vnesite `chrome://flags` in pritisnite Enter.

#### Poiščite zastavico:
V iskalno polje na vrhu strani vnesite 'enable-unsafe-webgpu'

#### Omogočite zastavico:
Poiščite zastavico #enable-unsafe-webgpu med rezultati.

Kliknite na spustni meni zraven in izberite Enabled.

#### Znova zaženite brskalnik:

Po omogočitvi zastavice boste morali brskalnik znova zagnati, da spremembe začnejo veljati. Kliknite gumb Relaunch, ki se pojavi na dnu strani.

- Za Linux zaženite brskalnik z `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU privzeto omogočen.
- V Firefox Nightly v naslovno vrstico vnesite about:config in `set dom.webgpu.enabled to true`.

### Nastavitev GPU za Microsoft Edge

Tukaj so koraki za nastavitev zmogljivega GPU za Microsoft Edge na Windows:

- **Odprite Nastavitve:** Kliknite na Start meni in izberite Nastavitve.
- **Sistemske nastavitve:** Pojdite na Sistem in nato na Zaslon.
- **Grafične nastavitve:** Pomaknite se navzdol in kliknite Grafične nastavitve.
- **Izberite aplikacijo:** Pod “Choose an app to set preference” izberite Desktop app in nato Prebrskaj.
- **Izberite Edge:** Pomaknite se do mape, kjer je nameščen Edge (običajno `C:\Program Files (x86)\Microsoft\Edge\Application`) in izberite `msedge.exe`.
- **Nastavite prednost:** Kliknite Opcije, izberite High performance in nato Shrani.
S tem zagotovite, da Microsoft Edge uporablja vaš zmogljivi GPU za boljšo zmogljivost.
- **Znova zaženite** računalnik, da spremembe začnejo veljati.

### Odprite svoj Codespace:
Pojdite v svoj repozitorij na GitHubu.
Kliknite gumb Code in izberite Open with Codespaces.

Če še nimate Codespace, ga lahko ustvarite s klikom na New codespace.

**Note** Namestitev Node okolja v vašem codespace-u
Zagon npm demo projekta iz GitHub Codespace je odličen način za testiranje in razvoj vaše aplikacije. Tukaj je vodnik po korakih, ki vam bo pomagal začeti:

### Nastavite svoje okolje:
Ko je Codespace odprt, preverite, ali imate nameščen Node.js in npm. To lahko preverite tako, da zaženete:
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

### Pojdite v mapo svojega projekta:
Uporabite terminal za navigacijo do mape, kjer je vaš npm projekt:
```
cd path/to/your/project
```

### Namestite odvisnosti:
Za namestitev vseh potrebnih odvisnosti, navedenih v datoteki package.json, zaženite:

```
npm install
```

### Zaženite demo:
Ko so odvisnosti nameščene, lahko zaženete demo skripto. Običajno je določena v sekciji scripts v package.json. Na primer, če se demo skripta imenuje start, zaženite:

```
npm run build
```
```
npm run dev
```

### Dostop do demo:
Če demo vključuje spletni strežnik, vam bo Codespaces ponudil URL za dostop. Poiščite obvestilo ali preverite zavihek Ports, da najdete URL.

**Note:** Model mora biti predpomnjen v brskalniku, zato lahko nalaganje traja nekaj časa.

### RAG Demo
Naložite markdown datoteko `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Izberite svojo datoteko:
Kliknite gumb “Choose File” in izberite dokument, ki ga želite naložiti.

### Naložite dokument:
Po izbiri datoteke kliknite “Upload”, da naložite dokument za RAG (Retrieval-Augmented Generation).

### Začnite klepet:
Ko je dokument naložen, lahko začnete klepetno sejo z RAG, ki temelji na vsebini vašega dokumenta.

**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v izvorni jezikovni različici velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.