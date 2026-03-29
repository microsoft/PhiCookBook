# **Použití Microsoft Foundry pro vyhodnocení**

![aistudo](../../../../../translated_images/cs/AIFoundry.9e0b513e999a1c5a.webp)

Jak vyhodnotit vaši generativní AI aplikaci pomocí [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Ať už hodnotíte jednoduché nebo vícenásobné konverzace, Microsoft Foundry nabízí nástroje pro vyhodnocení výkonu modelu a bezpečnosti.

![aistudo](../../../../../translated_images/cs/AIPortfolio.69da59a8e1eaa70f.webp)

## Jak vyhodnotit generativní AI aplikace s Microsoft Foundry
Pro podrobné instrukce si prohlédněte [Microsoft Foundry Dokumentaci](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Zde jsou kroky, jak začít:

## Vyhodnocení generativních AI modelů v Microsoft Foundry

**Předpoklady**

- Testovací dataset ve formátu CSV nebo JSON.
- Nasazený generativní AI model (například Phi-3, GPT 3.5, GPT 4 nebo modely Davinci).
- Runtime s výpočetní instancí pro spuštění vyhodnocení.

## Vestavěné metriky vyhodnocení

Microsoft Foundry umožňuje hodnotit jak jednoduché, tak složité vícenásobné konverzace.
Pro scénáře Retrieval Augmented Generation (RAG), kde je model založen na konkrétních datech, můžete hodnotit výkon pomocí vestavěných metrik vyhodnocení.
Navíc můžete vyhodnocovat obecné scénáře jednostranných otázek a odpovědí (ne-RAG).

## Vytvoření vyhodnocovacího běhu

V uživatelském rozhraní Microsoft Foundry přejděte na stránku Evaluate nebo Prompt Flow.
Následujte průvodce vytvořením vyhodnocení a nastavte vyhodnocovací běh. Zadejte volitelný název vašeho vyhodnocení.
Vyberte scénář, který odpovídá cílům vaší aplikace.
Zvolte jednu nebo více metrik vyhodnocení pro posouzení výstupu modelu.

## Vlastní vyhodnocovací tok (volitelně)

Pro větší flexibilitu můžete vytvořit vlastní vyhodnocovací tok. Přizpůsobte proces vyhodnocení podle vašich specifických požadavků.

## Zobrazení výsledků

Po spuštění vyhodnocení zaznamenejte, prohlédněte a analyzujte podrobné metriky vyhodnocení v Microsoft Foundry. Získejte přehled o schopnostech a omezeních vaší aplikace.



**Poznámka** Microsoft Foundry je v současnosti ve veřejné ukázce, proto jej používejte pro experimenty a vývojové účely. Pro produkční nasazení zvažte jiné možnosti. Pro více informací a podrobné postupy si prohlédněte oficiální [dokumentaci AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakákoliv nedorozumění nebo špatné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->