<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:59:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "cs"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo pro předvedení WebGPU a RAG vzoru

RAG vzor s modelem Phi-3.5 Onnx Hosted využívá přístup Retrieval-Augmented Generation, který kombinuje sílu modelů Phi-3.5 s ONNX hostingem pro efektivní nasazení AI. Tento vzor je klíčový pro doladění modelů na specifické doménové úkoly a nabízí kombinaci kvality, úspory nákladů a porozumění dlouhým kontextům. Je součástí sady Azure AI, která poskytuje široký výběr modelů snadno dostupných, vyzkoušitelných a použitelných, uspokojujících potřeby přizpůsobení v různých odvětvích.

## Co je WebGPU
WebGPU je moderní webové grafické API navržené pro efektivní přístup k grafickému procesoru (GPU) zařízení přímo z webových prohlížečů. Má nahradit WebGL a přináší několik klíčových vylepšení:

1. **Kompatibilita s moderními GPU**: WebGPU je postaveno tak, aby bez problémů fungovalo s aktuálními architekturami GPU, využívající systémová API jako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje obecné výpočty na GPU a rychlejší operace, což ho činí vhodným jak pro grafické vykreslování, tak pro úlohy strojového učení.
3. **Pokročilé funkce**: WebGPU umožňuje přístup k pokročilejším schopnostem GPU, což umožňuje složitější a dynamické grafické a výpočetní úlohy.
4. **Snížená zátěž JavaScriptu**: Díky přesunu větší části úloh na GPU výrazně snižuje zátěž na JavaScript, což vede k lepšímu výkonu a plynulejšímu chodu.

WebGPU je momentálně podporováno v prohlížečích jako Google Chrome, s probíhající prací na rozšíření podpory i na další platformy.

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

#### Přístup na stránku s příznaky:
Do adresního řádku napište `chrome://flags` a stiskněte Enter.

#### Vyhledání příznaku:
Do vyhledávacího pole nahoře zadejte 'enable-unsafe-webgpu'

#### Povolení příznaku:
Najděte příznak #enable-unsafe-webgpu v seznamu výsledků.

Klikněte na rozbalovací menu vedle něj a vyberte Enabled.

#### Restartujte prohlížeč:

Po povolení příznaku je třeba prohlížeč restartovat, aby se změny projevily. Klikněte na tlačítko Relaunch, které se objeví ve spodní části stránky.

- Na Linuxu spusťte prohlížeč s `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) má WebGPU povolené ve výchozím nastavení.  
- Ve Firefox Nightly zadejte do adresního řádku about:config a `set dom.webgpu.enabled to true`.

### Nastavení GPU pro Microsoft Edge

Postup pro nastavení vysokovýkonného GPU pro Microsoft Edge na Windows:

- **Otevřete Nastavení:** Klikněte na Start a vyberte Nastavení.  
- **Systémová nastavení:** Přejděte do Systém a poté Displej.  
- **Nastavení grafiky:** Sjeďte dolů a klikněte na Nastavení grafiky.  
- **Vyberte aplikaci:** Pod „Vyberte aplikaci pro nastavení preference“ zvolte Desktop app a klikněte na Procházet.  
- **Vyberte Edge:** Najděte složku instalace Edge (obvykle `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.  
- **Nastavte preferenci:** Klikněte na Možnosti, zvolte Vysoký výkon a potvrďte Uložit.  
Tím zajistíte, že Microsoft Edge bude používat váš vysokovýkonný GPU pro lepší výkon.  
- **Restartujte** počítač, aby se nastavení projevilo.

### Ukázky : Prosím [klikněte na tento odkaz](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.