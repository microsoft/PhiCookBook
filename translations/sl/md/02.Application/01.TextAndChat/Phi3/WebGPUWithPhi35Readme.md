<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:14:06+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sl"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo za predstavitev WebGPU in RAG vzorca

RAG vzorec s Phi-3.5 Onnx gostovanim modelom uporablja pristop Retrieval-Augmented Generation, ki združuje moč modelov Phi-3.5 z ONNX gostovanjem za učinkovite AI rešitve. Ta vzorec je ključen za prilagajanje modelov za specifične naloge, saj ponuja kombinacijo kakovosti, stroškovne učinkovitosti in razumevanja dolgih kontekstov. Je del Azure AI zbirke, ki nudi širok izbor modelov, ki jih je enostavno najti, preizkusiti in uporabljati, ter zadovoljuje potrebe po prilagoditvah v različnih panogah.

## Kaj je WebGPU  
WebGPU je sodoben spletni grafični API, zasnovan za učinkovito dostopanje do grafične procesne enote (GPU) naprave neposredno iz spletnih brskalnikov. Namenjen je kot naslednik WebGL in prinaša več ključnih izboljšav:

1. **Združljivost z modernimi GPU-ji**: WebGPU je zasnovan za nemoteno delovanje z današnjimi GPU arhitekturami, pri čemer uporablja sistemske API-je, kot so Vulkan, Metal in Direct3D 12.
2. **Izboljšana zmogljivost**: Podpira splošne GPU izračune in hitrejše operacije, kar ga naredi primernega tako za grafično upodabljanje kot tudi za naloge strojnega učenja.
3. **Napredne funkcije**: WebGPU omogoča dostop do bolj naprednih zmogljivosti GPU, kar omogoča bolj kompleksne in dinamične grafične ter računske obremenitve.
4. **Zmanjšana obremenitev JavaScripta**: Z večjim prenosom nalog na GPU WebGPU znatno zmanjša obremenitev JavaScripta, kar vodi do boljše zmogljivosti in gladke uporabniške izkušnje.

WebGPU trenutno podpirajo brskalniki, kot je Google Chrome, pri čemer potekajo dela za razširitev podpore na druge platforme.

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
Poiščite zastavico #enable-unsafe-webgpu na seznamu rezultatov.

Kliknite na spustni meni zraven in izberite Enabled.

#### Ponovni zagon brskalnika:  

Po omogočitvi zastavice boste morali znova zagnati brskalnik, da spremembe začnejo veljati. Kliknite gumb Relaunch, ki se pojavi na dnu strani.

- Za Linux zaženite brskalnik z `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ima WebGPU privzeto omogočen.  
- V Firefox Nightly v naslovno vrstico vpišite about:config in nastavite `dom.webgpu.enabled` na true.

### Nastavitev GPU za Microsoft Edge  

Tukaj so koraki za nastavitev zmogljivega GPU za Microsoft Edge na Windows:

- **Odprite Nastavitve:** Kliknite na Start meni in izberite Nastavitve.  
- **Sistemske nastavitve:** Pojdite na Sistem in nato na Zaslon.  
- **Grafične nastavitve:** Pomaknite se navzdol in kliknite na Grafične nastavitve.  
- **Izberite aplikacijo:** Pod “Izberite aplikacijo za nastavitev prednosti” izberite Namizna aplikacija in nato Brskaj.  
- **Izberite Edge:** Pomaknite se do mape z namestitvijo Edge (običajno `C:\Program Files (x86)\Microsoft\Edge\Application`) in izberite `msedge.exe`.  
- **Nastavite prednost:** Kliknite Možnosti, izberite Visoka zmogljivost in nato kliknite Shrani.  
To bo zagotovilo, da Microsoft Edge uporablja vaš zmogljiv GPU za boljšo zmogljivost.  
- **Ponovni zagon** računalnika, da spremembe začnejo veljati.

### Vzorci : Prosimo, [kliknite na to povezavo](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.