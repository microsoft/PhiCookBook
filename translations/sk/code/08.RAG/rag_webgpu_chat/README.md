<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:21:12+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sk"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo na predstavenie WebGPU a RAG vzoru
RAG vzor s modelom Phi-3 Onnx Hosted využíva prístup Retrieval-Augmented Generation, ktorý kombinuje silu modelov Phi-3 s ONNX hostingom pre efektívne nasadenie AI. Tento vzor je kľúčový pri doladení modelov pre špecifické doménové úlohy, ponúkajúc kombináciu kvality, nákladovej efektívnosti a porozumenia dlhým kontextom. Je súčasťou balíka Azure AI, ktorý poskytuje široký výber modelov, ktoré sa ľahko nájdu, vyskúšajú a používajú, pričom vyhovujú potrebám prispôsobenia v rôznych odvetviach. Modely Phi-3, vrátane Phi-3-mini, Phi-3-small a Phi-3-medium, sú dostupné v Azure AI Model Catalog a môžu byť doladené a nasadené samosprávne alebo cez platformy ako HuggingFace a ONNX, čo demonštruje záväzok Microsoftu k dostupným a efektívnym AI riešeniam.

## Čo je WebGPU
WebGPU je moderné webové grafické API navrhnuté tak, aby poskytovalo efektívny priamy prístup k grafickému procesoru (GPU) zariadenia priamo z webových prehliadačov. Má nahradiť WebGL a prináša niekoľko kľúčových vylepšení:

1. **Kompatibilita s modernými GPU**: WebGPU je vytvorené tak, aby bezproblémovo fungovalo s aktuálnymi architektúrami GPU, využívajúc systémové API ako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje všeobecné výpočty na GPU a rýchlejšie operácie, čo ho robí vhodným pre grafické vykresľovanie aj úlohy strojového učenia.
3. **Pokročilé funkcie**: WebGPU umožňuje prístup k pokročilejším schopnostiam GPU, čo umožňuje zložitejšie a dynamickejšie grafické a výpočtové úlohy.
4. **Zníženie záťaže JavaScriptu**: Presunutím väčšiny úloh na GPU WebGPU výrazne znižuje záťaž na JavaScript, čo vedie k lepšiemu výkonu a plynulejšiemu používateľskému zážitku.

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

#### Prístup na stránku s príznakmi:
Do adresného riadku zadajte `chrome://flags` a stlačte Enter.

#### Vyhľadajte príznak:
V hornej časti stránky do vyhľadávacieho poľa zadajte 'enable-unsafe-webgpu'.

#### Povoľte príznak:
Nájdite príznak #enable-unsafe-webgpu v zozname výsledkov.

Kliknite na rozbaľovaciu ponuku vedľa neho a vyberte Enabled.

#### Reštartujte prehliadač:

Po povolení príznaku je potrebné prehliadač reštartovať, aby sa zmeny prejavili. Kliknite na tlačidlo Relaunch, ktoré sa zobrazí v spodnej časti stránky.

- Pre Linux spustite prehliadač s parametrom `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU predvolene povolené.
- Vo Firefox Nightly zadajte do adresného riadku about:config a nastavte `dom.webgpu.enabled` na true.

### Nastavenie GPU pre Microsoft Edge

Tu sú kroky na nastavenie vysoko výkonného GPU pre Microsoft Edge na Windows:

- **Otvorte Nastavenia:** Kliknite na Štart a vyberte Nastavenia.
- **Systémové nastavenia:** Prejdite do Systém a potom Displej.
- **Nastavenia grafiky:** Posuňte sa nadol a kliknite na Nastavenia grafiky.
- **Vyberte aplikáciu:** Pod „Vyberte aplikáciu na nastavenie preferencie“ zvoľte Desktop app a potom Prehľadávať.
- **Vyberte Edge:** Prejdite do inštalačnej zložky Edge (zvyčajne `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavte preferenciu:** Kliknite na Možnosti, vyberte Vysoký výkon a potom Uložiť.  
Tým zabezpečíte, že Microsoft Edge bude používať váš vysoko výkonný GPU pre lepší výkon.  
- **Reštartujte** počítač, aby sa nastavenia prejavili.

### Otvorte svoj Codespace:
Prejdite do svojho repozitára na GitHub.
Kliknite na tlačidlo Code a vyberte Open with Codespaces.

Ak ešte nemáte Codespace, môžete si ho vytvoriť kliknutím na New codespace.

**Poznámka** Inštalácia Node prostredia vo vašom codespace  
Spustenie npm demo z GitHub Codespace je skvelý spôsob, ako testovať a vyvíjať váš projekt. Tu je krok za krokom návod, ako začať:

### Nastavte svoje prostredie:
Keď máte Codespace otvorený, uistite sa, že máte nainštalované Node.js a npm. Skontrolujete to spustením:  
```
node -v
```  
```
npm -v
```

Ak nie sú nainštalované, môžete ich nainštalovať pomocou:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Prejdite do adresára projektu:
Použite terminál na prechod do adresára, kde sa nachádza váš npm projekt:  
```
cd path/to/your/project
```

### Nainštalujte závislosti:
Spustite nasledujúci príkaz na inštaláciu všetkých potrebných závislostí uvedených v súbore package.json:

```
npm install
```

### Spustite demo:
Keď sú závislosti nainštalované, môžete spustiť demo skript. Zvyčajne je definovaný v sekcii scripts v package.json. Napríklad, ak sa váš demo skript volá start, spustíte:

```
npm run build
```  
```
npm run dev
```

### Prístup k demu:
Ak demo zahŕňa webový server, Codespaces poskytne URL na jeho prístup. Sledujte notifikácie alebo záložku Ports, kde nájdete URL.

**Poznámka:** Model musí byť uložený v cache prehliadača, preto môže načítanie chvíľu trvať.

### RAG Demo
Nahrajte markdown súbor `intro_rag.md` na dokončenie RAG riešenia. Ak používate codespaces, môžete si súbor stiahnuť z `01.InferencePhi3/docs/`.

### Vyberte svoj súbor:
Kliknite na tlačidlo „Choose File“ a vyberte dokument, ktorý chcete nahrať.

### Nahrajte dokument:
Po výbere súboru kliknite na tlačidlo „Upload“ pre načítanie dokumentu do RAG (Retrieval-Augmented Generation).

### Začnite chat:
Po nahraní dokumentu môžete začať chatovaciu reláciu pomocou RAG na základe obsahu vášho dokumentu.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.