<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:33:25+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "cs"
}
-->
# **Použití Azure AI Foundry pro hodnocení**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5a.cs.png)

Jak hodnotit vaši generativní AI aplikaci pomocí [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Ať už posuzujete jednorázové nebo vícekrokové konverzace, Azure AI Foundry nabízí nástroje pro hodnocení výkonu a bezpečnosti modelu.

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f.cs.png)

## Jak hodnotit generativní AI aplikace s Azure AI Foundry
Podrobné instrukce najdete v [dokumentaci Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Zde jsou kroky, jak začít:

## Hodnocení generativních AI modelů v Azure AI Foundry

**Požadavky**

- Testovací dataset ve formátu CSV nebo JSON.
- Nasazený generativní AI model (například Phi-3, GPT 3.5, GPT 4 nebo modely Davinci).
- Runtime s výpočetní instancí pro spuštění hodnocení.

## Vestavěné metriky hodnocení

Azure AI Foundry umožňuje hodnotit jak jednorázové, tak složité vícekrokové konverzace.  
Pro scénáře Retrieval Augmented Generation (RAG), kde je model založen na konkrétních datech, můžete výkon posoudit pomocí vestavěných metrik hodnocení.  
Navíc můžete hodnotit obecné scénáře jednorázového zodpovídání otázek (non-RAG).

## Vytvoření hodnocení

V uživatelském rozhraní Azure AI Foundry přejděte na stránku Evaluate nebo Prompt Flow.  
Postupujte podle průvodce vytvořením hodnocení a nastavte běh hodnocení. Můžete zadat volitelný název hodnocení.  
Vyberte scénář, který odpovídá cílům vaší aplikace.  
Zvolte jednu nebo více metrik hodnocení pro posouzení výstupu modelu.

## Vlastní hodnotící tok (volitelné)

Pro větší flexibilitu můžete vytvořit vlastní hodnotící tok. Přizpůsobte proces hodnocení podle svých specifických požadavků.

## Zobrazení výsledků

Po dokončení hodnocení si v Azure AI Foundry prohlédněte, zaznamenejte a analyzujte podrobné metriky hodnocení. Získejte přehled o schopnostech a omezeních vaší aplikace.

**Note** Azure AI Foundry je momentálně ve veřejné preview, proto jej používejte pro experimentování a vývoj. Pro produkční nasazení zvažte jiné možnosti. Pro více informací a podrobné návody navštivte oficiální [dokumentaci AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.