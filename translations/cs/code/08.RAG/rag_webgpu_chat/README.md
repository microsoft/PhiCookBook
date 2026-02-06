Phi-3-mini WebGPU RAG Chatbot

## Ukázka pro předvedení WebGPU a RAG vzoru
RAG vzor s modelem Phi-3 Onnx Hosted využívá přístup Retrieval-Augmented Generation, který kombinuje sílu modelů Phi-3 s ONNX hostingem pro efektivní nasazení AI. Tento vzor je klíčový pro doladění modelů na úkoly specifické pro danou oblast, nabízí kombinaci kvality, úspornosti a porozumění dlouhým kontextům. Je součástí sady Azure AI, která poskytuje široký výběr modelů snadno dostupných, vyzkoušitelných a použitelných, přizpůsobených potřebám různých odvětví. Modely Phi-3, včetně Phi-3-mini, Phi-3-small a Phi-3-medium, jsou dostupné v Azure AI Model Catalog a lze je doladit a nasadit samostatně nebo přes platformy jako HuggingFace a ONNX, což ukazuje závazek Microsoftu k dostupným a efektivním AI řešením.

## Co je WebGPU
WebGPU je moderní webové grafické API navržené pro efektivní přístup k grafickému procesoru (GPU) zařízení přímo z webových prohlížečů. Má nahradit WebGL a přináší několik klíčových vylepšení:

1. **Kompatibilita s moderními GPU**: WebGPU je navrženo tak, aby bez problémů fungovalo s aktuálními architekturami GPU, využívající systémová API jako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje obecné výpočty na GPU a rychlejší operace, což ho činí vhodným jak pro grafické vykreslování, tak pro úlohy strojového učení.
3. **Pokročilé funkce**: WebGPU umožňuje přístup k pokročilejším schopnostem GPU, což umožňuje složitější a dynamické grafické a výpočetní úlohy.
4. **Snížení zátěže JavaScriptu**: Přenesením více úloh na GPU WebGPU výrazně snižuje zátěž na JavaScript, což vede k lepšímu výkonu a plynulejšímu chodu.

WebGPU je aktuálně podporováno v prohlížečích jako Google Chrome, přičemž probíhá práce na rozšíření podpory i na další platformy.

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

#### Otevřete svůj prohlížeč:
Spusťte Google Chrome nebo Microsoft Edge.

#### Přístup na stránku Flags:
Do adresního řádku zadejte `chrome://flags` a stiskněte Enter.

#### Vyhledání příznaku:
Do vyhledávacího pole nahoře na stránce napište 'enable-unsafe-webgpu'

#### Povolení příznaku:
Najděte příznak #enable-unsafe-webgpu v seznamu výsledků.

Klikněte na rozbalovací menu vedle něj a vyberte Enabled.

#### Restartujte prohlížeč:

Po povolení příznaku je potřeba prohlížeč restartovat, aby se změny projevily. Klikněte na tlačítko Relaunch, které se objeví ve spodní části stránky.

- Na Linuxu spusťte prohlížeč s parametrem `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU povoleno ve výchozím nastavení.
- Ve Firefox Nightly zadejte do adresního řádku about:config a nastavte `dom.webgpu.enabled` na true.

### Nastavení GPU pro Microsoft Edge

Postup nastavení výkonného GPU pro Microsoft Edge na Windows:

- **Otevřete Nastavení:** Klikněte na nabídku Start a vyberte Nastavení.
- **Systémová nastavení:** Přejděte do Systém a poté Displej.
- **Nastavení grafiky:** Sjeďte dolů a klikněte na Nastavení grafiky.
- **Vyberte aplikaci:** Pod „Vyberte aplikaci pro nastavení předvolby“ zvolte Desktopová aplikace a klikněte na Procházet.
- **Vyberte Edge:** Přejděte do složky s instalací Edge (obvykle `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavte předvolbu:** Klikněte na Možnosti, vyberte Vysoký výkon a poté klikněte na Uložit.  
Tím zajistíte, že Microsoft Edge bude používat váš výkonný GPU pro lepší výkon.  
- **Restartujte** počítač, aby se nastavení projevilo.

### Otevřete svůj Codespace:
Přejděte do svého repozitáře na GitHubu.  
Klikněte na tlačítko Code a vyberte Open with Codespaces.

Pokud ještě nemáte Codespace, můžete si ho vytvořit kliknutím na New codespace.

**Poznámka** Instalace Node prostředí ve vašem codespace  
Spuštění npm ukázky z GitHub Codespace je skvělý způsob, jak testovat a vyvíjet svůj projekt. Zde je krok za krokem návod, jak začít:

### Nastavte své prostředí:
Jakmile máte Codespace otevřený, ujistěte se, že máte nainstalovaný Node.js a npm. Zkontrolujete to příkazy:  
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
Spusťte následující příkaz pro instalaci všech potřebných závislostí uvedených v souboru package.json:  

```
npm install
```

### Spuštění ukázky:
Jakmile jsou závislosti nainstalovány, můžete spustit svůj demo skript. Obvykle je uveden v sekci scripts v package.json. Například pokud se váš demo skript jmenuje start, spusťte:  

```
npm run build
```  
```
npm run dev
```

### Přístup k ukázce:
Pokud vaše ukázka zahrnuje webový server, Codespaces vám poskytne URL pro přístup. Sledujte oznámení nebo zkontrolujte záložku Ports, kde URL najdete.

**Poznámka:** Model musí být uložen v cache prohlížeče, takže načítání může chvíli trvat.

### RAG Demo
Nahrajte markdown soubor `intro_rag.md` pro dokončení RAG řešení. Pokud používáte codespaces, můžete si soubor stáhnout z `01.InferencePhi3/docs/`

### Vyberte svůj soubor:
Klikněte na tlačítko „Choose File“ a vyberte dokument, který chcete nahrát.

### Nahrajte dokument:
Po výběru souboru klikněte na tlačítko „Upload“ pro načtení dokumentu do RAG (Retrieval-Augmented Generation).

### Začněte chat:
Jakmile je dokument nahrán, můžete zahájit chatovací relaci pomocí RAG na základě obsahu vašeho dokumentu.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.