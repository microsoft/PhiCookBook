<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:12:58+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sk"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo na predstavenie WebGPU a RAG vzoru

RAG vzor s modelom Phi-3.5 Onnx Hosted využíva prístup Retrieval-Augmented Generation, ktorý kombinuje silu modelov Phi-3.5 s ONNX hostingom pre efektívne nasadenie AI. Tento vzor je kľúčový pri doladení modelov pre špecifické doménové úlohy, ponúkajúc kombináciu kvality, nákladovej efektívnosti a porozumenia dlhému kontextu. Je súčasťou Azure AI balíka, ktorý poskytuje široký výber modelov, ktoré sa ľahko nájdu, vyskúšajú a používajú, pričom vyhovujú potrebám prispôsobenia v rôznych odvetviach.

## Čo je WebGPU  
WebGPU je moderné webové grafické API navrhnuté tak, aby poskytovalo efektívny prístup k grafickému procesoru (GPU) zariadenia priamo z webových prehliadačov. Má nahradiť WebGL a prináša niekoľko kľúčových vylepšení:

1. **Kompatibilita s modernými GPU:** WebGPU je vytvorené tak, aby bezproblémovo fungovalo s aktuálnymi architektúrami GPU, využívajúc systémové API ako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon:** Podporuje všeobecné výpočty na GPU a rýchlejšie operácie, čo ho robí vhodným pre grafické vykresľovanie aj úlohy strojového učenia.
3. **Pokročilé funkcie:** WebGPU umožňuje prístup k pokročilejším schopnostiam GPU, čo umožňuje zložitejšie a dynamickejšie grafické a výpočtové úlohy.
4. **Zníženie záťaže JavaScriptu:** Presunutím väčšiny úloh na GPU WebGPU výrazne znižuje záťaž na JavaScript, čo vedie k lepšiemu výkonu a plynulejšiemu používateľskému zážitku.

WebGPU je momentálne podporované v prehliadačoch ako Google Chrome, pričom prebieha práca na rozšírení podpory aj na ďalšie platformy.

### 03.WebGPU  
Požadované prostredie:

**Podporované prehliadače:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Ako povoliť WebGPU:

- V Chrome/Microsoft Edge  

Povoľte príznak `chrome://flags/#enable-unsafe-webgpu`.

#### Otvorte svoj prehliadač:  
Spustite Google Chrome alebo Microsoft Edge.

#### Prístup na stránku Flags:  
Do adresného riadku zadajte `chrome://flags` a stlačte Enter.

#### Vyhľadajte príznak:  
Do vyhľadávacieho poľa v hornej časti stránky zadajte 'enable-unsafe-webgpu'

#### Povoľte príznak:  
Nájdite príznak #enable-unsafe-webgpu v zozname výsledkov.

Kliknite na rozbaľovacie menu vedľa neho a vyberte Enabled.

#### Reštartujte prehliadač:  

Po povolení príznaku je potrebné prehliadač reštartovať, aby sa zmeny prejavili. Kliknite na tlačidlo Relaunch, ktoré sa zobrazí v spodnej časti stránky.

- Pre Linux spustite prehliadač s parametrom `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) má WebGPU predvolene povolené.  
- Vo Firefox Nightly zadajte do adresného riadku about:config a nastavte `dom.webgpu.enabled` na true.

### Nastavenie GPU pre Microsoft Edge  

Tu sú kroky na nastavenie vysoko výkonného GPU pre Microsoft Edge na Windows:

- **Otvorte Nastavenia:** Kliknite na Štart a vyberte Nastavenia.  
- **Systémové nastavenia:** Prejdite do Systém a potom Displej.  
- **Grafické nastavenia:** Posuňte sa nadol a kliknite na Grafické nastavenia.  
- **Vyberte aplikáciu:** Pod „Vyberte aplikáciu na nastavenie preferencie“ zvoľte Desktop app a potom Prehľadávať.  
- **Vyberte Edge:** Prejdite do inštalačného priečinka Edge (zvyčajne `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.  
- **Nastavte preferenciu:** Kliknite na Možnosti, vyberte Vysoký výkon a potom Uložiť.  
Tým zabezpečíte, že Microsoft Edge bude používať váš vysoko výkonný GPU pre lepší výkon.  
- **Reštartujte** počítač, aby sa nastavenia prejavili.

### Ukážky : Prosím, [kliknite na tento odkaz](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.