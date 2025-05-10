<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:22:45+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sk"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo na predvedenie WebGPU a RAG vzoru
RAG vzor s Phi-3 Onnx Hosted modelom využíva prístup Retrieval-Augmented Generation, ktorý kombinuje silu Phi-3 modelov s ONNX hostingom pre efektívne AI nasadenia. Tento vzor je kľúčový pri doladení modelov pre špecifické doménové úlohy, ponúkajúc kombináciu kvality, úspornosti a porozumenia dlhým kontextom. Je súčasťou Azure AI balíka, ktorý poskytuje široký výber modelov, ktoré je jednoduché nájsť, vyskúšať a používať, prispôsobené potrebám rôznych odvetví. Phi-3 modely, vrátane Phi-3-mini, Phi-3-small a Phi-3-medium, sú dostupné v Azure AI Model Catalog a môžu byť doladené a nasadené samostatne alebo cez platformy ako HuggingFace a ONNX, čo ukazuje záväzok Microsoftu k prístupným a efektívnym AI riešeniam.

## Čo je WebGPU
WebGPU je moderné webové grafické API navrhnuté tak, aby poskytovalo efektívny prístup k grafickému procesoru (GPU) zariadenia priamo z webových prehliadačov. Má nahradiť WebGL a prináša niekoľko dôležitých vylepšení:

1. **Kompatibilita s modernými GPU**: WebGPU je vytvorené tak, aby bezproblémovo fungovalo s aktuálnymi GPU architektúrami, využívajúc systémové API ako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje všeobecné výpočty na GPU a rýchlejšie operácie, čo ho robí vhodným pre grafické vykresľovanie aj úlohy strojového učenia.
3. **Pokročilé funkcie**: WebGPU poskytuje prístup k pokročilejším schopnostiam GPU, umožňujúc zložitejšiu a dynamickejšiu grafiku a výpočtové zaťaženie.
4. **Znížené zaťaženie JavaScriptu**: Presunom väčšiny úloh na GPU WebGPU výrazne znižuje záťaž na JavaScript, čo vedie k lepšiemu výkonu a plynulejšiemu používateľskému zážitku.

WebGPU je momentálne podporované v prehliadačoch ako Google Chrome, pričom prebiehajú práce na rozšírení podpory na ďalšie platformy.

### 03.WebGPU
Požadované prostredie:

**Podporované prehliadače:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Povolenie WebGPU:

- V Chrome/Microsoft Edge

Povoľte `chrome://flags/#enable-unsafe-webgpu` flag.

#### Otvorte svoj prehliadač:
Spustite Google Chrome alebo Microsoft Edge.

#### Prístup na stránku s flagmi:
Do adresného riadku zadajte `chrome://flags` a stlačte Enter.

#### Vyhľadanie flagu:
Do vyhľadávacieho poľa hore na stránke zadajte 'enable-unsafe-webgpu'

#### Povolenie flagu:
Nájdite #enable-unsafe-webgpu flag v zozname výsledkov.

Kliknite na rozbaľovaciu ponuku vedľa neho a vyberte Enabled.

#### Reštartujte prehliadač:

Po povolení flagu je potrebné prehliadač reštartovať, aby sa zmeny prejavili. Kliknite na tlačidlo Relaunch, ktoré sa zobrazí v spodnej časti stránky.

- Pre Linux spustite prehliadač s `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) má WebGPU povolené štandardne.  
- Vo Firefox Nightly zadajte do adresného riadku about:config a `set dom.webgpu.enabled to true`.

### Nastavenie GPU pre Microsoft Edge

Tu sú kroky na nastavenie vysoko výkonného GPU pre Microsoft Edge na Windows:

- **Otvorte Nastavenia:** Kliknite na Štart menu a vyberte Nastavenia.  
- **Systémové nastavenia:** Prejdite do Systém a potom Displej.  
- **Nastavenia grafiky:** Posuňte sa dole a kliknite na Nastavenia grafiky.  
- **Vyberte aplikáciu:** Pod „Vyberte aplikáciu na nastavenie preferencie“ zvoľte Desktop app a kliknite na Prehľadávať.  
- **Vyberte Edge:** Prejdite do inštalačného priečinka Edge (zvyčajne `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.  
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
Keď máte otvorený Codespace, uistite sa, že máte nainštalované Node.js a npm. Skontrolujete to spustením:  
```
node -v
```  
```
npm -v
```

Ak nie sú nainštalované, môžete ich doinštalovať pomocou:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Prejdite do priečinka projektu:
Použite terminál na presun do priečinka, kde sa nachádza váš npm projekt:  
```
cd path/to/your/project
```

### Inštalácia závislostí:
Spustite nasledujúci príkaz na inštaláciu všetkých potrebných závislostí uvedených v package.json:  

```
npm install
```

### Spustite demo:
Po nainštalovaní závislostí môžete spustiť demo skript. Ten je obvykle definovaný v sekcii scripts v package.json. Napríklad, ak sa demo skript volá start, spustíte ho takto:  

```
npm run build
```  
```
npm run dev
```

### Prístup k demu:
Ak demo využíva webový server, Codespaces vám poskytne URL pre prístup. Sledujte notifikácie alebo skontrolujte záložku Ports, kde nájdete URL.

**Poznámka:** Model musí byť uložený v cache prehliadača, takže načítanie môže chvíľu trvať.

### RAG Demo
Nahrajte markdown súbor `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Výber súboru:
Kliknite na tlačidlo „Choose File“ a vyberte dokument, ktorý chcete nahrať.

### Nahranie dokumentu:
Po výbere súboru kliknite na tlačidlo „Upload“, aby ste dokument načítali pre RAG (Retrieval-Augmented Generation).

### Spustite chat:
Keď je dokument nahraný, môžete začať chatovaciu reláciu využívajúcu RAG na základe obsahu vášho dokumentu.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.