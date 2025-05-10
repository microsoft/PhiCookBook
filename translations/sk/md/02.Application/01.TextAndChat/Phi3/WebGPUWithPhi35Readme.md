<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T19:00:03+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sk"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo na ukážku WebGPU a RAG vzoru

RAG vzor s Phi-3.5 Onnx Hosted modelom využíva prístup Retrieval-Augmented Generation, ktorý spája silu Phi-3.5 modelov s ONNX hostingom pre efektívne nasadenie AI. Tento vzor je kľúčový pri dolaďovaní modelov na úlohy špecifické pre danú oblasť, ponúkajúc kombináciu kvality, úspornosti a porozumenia dlhým kontextom. Je súčasťou Azure AI balíka, ktorý poskytuje široký výber modelov, ktoré sa ľahko nájdu, vyskúšajú a používajú, pričom vychádza v ústrety potrebám prispôsobenia v rôznych odvetviach.

## Čo je WebGPU
WebGPU je moderné webové grafické API navrhnuté tak, aby poskytovalo efektívny prístup k grafickému procesoru (GPU) zariadenia priamo z webových prehliadačov. Má nahradiť WebGL a prináša niekoľko kľúčových vylepšení:

1. **Kompatibilita s modernými GPU:** WebGPU je vytvorené tak, aby hladko fungovalo s aktuálnymi GPU architektúrami, využívajúc systémové API ako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon:** Podporuje všeobecné výpočty na GPU a rýchlejšie operácie, vďaka čomu je vhodné nielen na grafické vykresľovanie, ale aj na úlohy strojového učenia.
3. **Pokročilé funkcie:** WebGPU umožňuje prístup k rozšíreným schopnostiam GPU, čo umožňuje zložitejšiu a dynamickejšiu grafiku a výpočtové zaťaženie.
4. **Zníženie záťaže JavaScriptu:** Presunutím viacerých úloh na GPU WebGPU výrazne znižuje záťaž na JavaScript, čo vedie k lepšiemu výkonu a plynulejšiemu používateľskému zážitku.

WebGPU je momentálne podporované v prehliadačoch ako Google Chrome, pričom prebieha práca na rozšírení podpory aj na ďalšie platformy.

### 03.WebGPU
Požadované prostredie:

**Podporované prehliadače:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Povolenie WebGPU:

- V Chrome/Microsoft Edge

Povoľte príznak `chrome://flags/#enable-unsafe-webgpu`.

#### Otvorte svoj prehliadač:
Spustite Google Chrome alebo Microsoft Edge.

#### Prístup na stránku s príznakmi:
Do adresného riadku zadajte `chrome://flags` a stlačte Enter.

#### Vyhľadanie príznaku:
Do vyhľadávacieho poľa v hornej časti stránky zadajte 'enable-unsafe-webgpu'.

#### Povolenie príznaku:
Nájdite príznak #enable-unsafe-webgpu v zozname výsledkov.

Kliknite na rozbaľovaciu ponuku vedľa neho a vyberte Enabled.

#### Reštartujte prehliadač:

Po povolení príznaku je potrebné prehliadač reštartovať, aby sa zmeny prejavili. Kliknite na tlačidlo Relaunch, ktoré sa zobrazí v dolnej časti stránky.

- Na Linuxe spustite prehliadač s `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) má WebGPU povolené štandardne.  
- Vo Firefox Nightly zadajte do adresného riadku about:config a `set dom.webgpu.enabled to true`.

### Nastavenie GPU pre Microsoft Edge

Tu sú kroky, ako nastaviť vysoko výkonnú GPU pre Microsoft Edge na Windows:

- **Otvorte Nastavenia:** Kliknite na Štart a vyberte Nastavenia.  
- **Systémové nastavenia:** Prejdite na Systém a potom Displej.  
- **Grafické nastavenia:** Posuňte sa nadol a kliknite na Grafické nastavenia.  
- **Vyberte aplikáciu:** V časti „Vyberte aplikáciu na nastavenie preferencie“ zvoľte Desktop app a potom Prehľadať.  
- **Vyberte Edge:** Prejdite do inštalačného priečinka Edge (zvyčajne `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.  
- **Nastavte preferenciu:** Kliknite na Možnosti, vyberte Vysoký výkon a potom Uložiť.  
Tým zabezpečíte, že Microsoft Edge bude používať vašu vysoko výkonnú GPU pre lepší výkon.  
- **Reštartujte** počítač, aby sa nastavenia prejavili.

### Ukážky : Prosím, [kliknite na tento odkaz](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.