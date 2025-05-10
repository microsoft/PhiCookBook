<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:22:26+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "cs"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo pro předvedení WebGPU a RAG vzoru
RAG vzor s modelem Phi-3 Onnx Hosted využívá přístup Retrieval-Augmented Generation, který kombinuje sílu modelů Phi-3 s ONNX hostingem pro efektivní nasazení AI. Tento vzor je klíčový pro doladění modelů na úkoly specifické pro danou doménu, nabízí kombinaci kvality, úspory nákladů a porozumění dlouhým kontextům. Je součástí sady Azure AI, která poskytuje široký výběr modelů snadno dostupných k vyzkoušení a použití, vyhovujících potřebám přizpůsobení v různých odvětvích. Modely Phi-3, včetně Phi-3-mini, Phi-3-small a Phi-3-medium, jsou dostupné v Azure AI Model Catalog a lze je doladit a nasadit samostatně nebo přes platformy jako HuggingFace a ONNX, což demonstruje závazek Microsoftu k přístupným a efektivním AI řešením.

## Co je WebGPU
WebGPU je moderní webové grafické API navržené pro efektivní přístup k grafické jednotce (GPU) zařízení přímo z webových prohlížečů. Má být nástupcem WebGL a přináší několik klíčových vylepšení:

1. **Kompatibilita s moderními GPU**: WebGPU je navrženo tak, aby hladce fungovalo s aktuálními architekturami GPU, využívá systémová API jako Vulkan, Metal a Direct3D 12.
2. **Vylepšený výkon**: Podporuje výpočty na GPU obecného určení a rychlejší operace, což ho činí vhodným jak pro grafické vykreslování, tak pro úlohy strojového učení.
3. **Pokročilé funkce**: WebGPU umožňuje přístup k pokročilejším schopnostem GPU, což umožňuje složitější a dynamické grafické i výpočetní úlohy.
4. **Snížená zátěž JavaScriptu**: Přenesením více úloh na GPU WebGPU výrazně snižuje zátěž na JavaScript, což vede k lepšímu výkonu a plynulejšímu chodu.

WebGPU je momentálně podporováno v prohlížečích jako Google Chrome, s probíhající prací na rozšíření podpory i na dalších platformách.

### 03.WebGPU
Požadované prostředí:

**Podporované prohlížeče:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Povolení WebGPU:

- V Chrome/Microsoft Edge 

Povolte příznak `chrome://flags/#enable-unsafe-webgpu`.

#### Otevřete prohlížeč:
Spusťte Google Chrome nebo Microsoft Edge.

#### Přístup na stránku s příznaky:
Do adresního řádku zadejte `chrome://flags` a stiskněte Enter.

#### Vyhledání příznaku:
Do vyhledávacího pole nahoře na stránce napište 'enable-unsafe-webgpu'

#### Povolení příznaku:
Najděte příznak #enable-unsafe-webgpu v seznamu výsledků.

Klikněte na rozbalovací menu vedle něj a vyberte Enabled.

#### Restartujte prohlížeč:

Po povolení příznaku je nutné prohlížeč restartovat, aby se změny projevily. Klikněte na tlačítko Relaunch, které se objeví ve spodní části stránky.

- Na Linuxu spusťte prohlížeč s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU povoleno ve výchozím nastavení.
- Ve Firefox Nightly zadejte do adresního řádku about:config a `set dom.webgpu.enabled to true`.

### Nastavení GPU pro Microsoft Edge

Zde jsou kroky pro nastavení výkonného GPU pro Microsoft Edge na Windows:

- **Otevřete Nastavení:** Klikněte na nabídku Start a vyberte Nastavení.
- **Systémová nastavení:** Přejděte do Systém a poté Displej.
- **Nastavení grafiky:** Sjeďte dolů a klikněte na Nastavení grafiky.
- **Vyberte aplikaci:** Pod „Vyberte aplikaci pro nastavení předvolby“ zvolte Desktop app a poté Procházet.
- **Vyberte Edge:** Přejděte do instalační složky Edge (obvykle `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavte předvolbu:** Klikněte na Možnosti, vyberte Vysoký výkon a poté klikněte na Uložit.
Tím zajistíte, že Microsoft Edge bude používat váš výkonný GPU pro lepší výkon.
- **Restartujte** počítač, aby se nastavení projevila.

### Otevřete svůj Codespace:
Přejděte do svého repozitáře na GitHubu.
Klikněte na tlačítko Code a vyberte Open with Codespaces.

Pokud ještě nemáte Codespace, můžete si vytvořit nový kliknutím na New codespace.

**Note** Instalace Node prostředí ve vašem codespace
Spuštění npm demo z GitHub Codespace je skvělý způsob, jak projekt testovat a vyvíjet. Zde je krok za krokem návod, jak začít:

### Nastavte své prostředí:
Po otevření Codespace se ujistěte, že máte nainstalovaný Node.js a npm. Zkontrolujete to spuštěním:
```
node -v
```
```
npm -v
```

Pokud nejsou nainstalovány, můžete je nainstalovat pomocí:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Přejděte do adresáře projektu:
Použijte terminál k přechodu do složky, kde se nachází váš npm projekt:
```
cd path/to/your/project
```

### Instalace závislostí:
Spusťte následující příkaz pro instalaci všech potřebných závislostí uvedených v package.json:

```
npm install
```

### Spuštění demo:
Po instalaci závislostí můžete spustit demo skript. Obvykle je definován v sekci scripts vašeho package.json. Například pokud se demo skript jmenuje start, spusťte:

```
npm run build
```
```
npm run dev
```

### Přístup k demu:
Pokud demo zahrnuje webový server, Codespaces poskytne URL pro přístup. Hledejte oznámení nebo zkontrolujte záložku Ports pro nalezení URL.

**Note:** Model musí být uložen v cache prohlížeče, proto načítání může chvíli trvat.

### RAG Demo
Nahrajte markdown soubor `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Vyberte svůj soubor:
Klikněte na tlačítko „Choose File“ a vyberte dokument, který chcete nahrát.

### Nahrajte dokument:
Po výběru souboru klikněte na tlačítko „Upload“ pro načtení dokumentu pro RAG (Retrieval-Augmented Generation).

### Začněte chat:
Po nahrání dokumentu můžete zahájit chatovací relaci pomocí RAG založenou na obsahu vašeho dokumentu.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo mylné výklady vzniklé použitím tohoto překladu.