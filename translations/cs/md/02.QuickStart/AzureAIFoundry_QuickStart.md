<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:27:18+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "cs"
}
-->
# **Použití Phi-3 v Azure AI Foundry**

S rozvojem generativní AI doufáme, že využijeme jednotnou platformu pro správu různých LLM a SLM, integraci podnikových dat, operace ladění/RAG a hodnocení různých podnikových procesů po integraci LLM a SLM, atd., aby bylo možné lépe implementovat chytré aplikace založené na generativní AI. [Azure AI Foundry](https://ai.azure.com) je podniková platforma pro aplikace generativní AI.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93d6fb1d0a69b635bc36834da1f0615d7d2b8be216021d9eeb.cs.png)

S Azure AI Foundry můžete hodnotit odpovědi velkých jazykových modelů (LLM) a orchestraci komponent aplikací s prompt flow pro lepší výkon. Platforma usnadňuje škálovatelnost při přechodu od konceptů k plnohodnotné produkci. Nepřetržité monitorování a vylepšování podporují dlouhodobý úspěch.

Model Phi-3 lze rychle nasadit na Azure AI Foundry pomocí jednoduchých kroků a poté využít Azure AI Foundry k dokončení souvisejících úloh jako Playground/Chat, ladění, hodnocení a dalších.

## **1. Příprava**

Pokud již máte na svém počítači nainstalovaný [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), použití této šablony je stejně jednoduché jako spuštění tohoto příkazu v novém adresáři.

## Ruční vytvoření

Vytvoření projektu a hubu v Microsoft Azure AI Foundry je skvělý způsob, jak organizovat a spravovat svou práci s AI. Zde je krok za krokem návod, jak začít:

### Vytvoření projektu v Azure AI Foundry

1. **Přejděte do Azure AI Foundry**: Přihlaste se do portálu Azure AI Foundry.
2. **Vytvořte projekt**:
   - Pokud jste již v projektu, vyberte v levém horním rohu stránky „Azure AI Foundry“ pro návrat na domovskou stránku.
   - Klikněte na „+ Create project“.
   - Zadejte název projektu.
   - Pokud máte hub, bude vybrán automaticky. Pokud máte přístup k více hubům, můžete vybrat jiný z rozbalovací nabídky. Pokud chcete vytvořit nový hub, vyberte „Create new hub“ a zadejte jeho název.
   - Klikněte na „Create“.

### Vytvoření hubu v Azure AI Foundry

1. **Přejděte do Azure AI Foundry**: Přihlaste se pomocí svého Azure účtu.
2. **Vytvořte hub**:
   - V levém menu vyberte Management center.
   - Vyberte „All resources“, poté klikněte na šipku vedle „+ New project“ a zvolte „+ New hub“.
   - V dialogu „Create a new hub“ zadejte název hubu (např. contoso-hub) a upravte další pole podle potřeby.
   - Klikněte na „Next“, zkontrolujte informace a poté klikněte na „Create“.

Pro podrobnější instrukce můžete nahlédnout do oficiální [dokumentace Microsoftu](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po úspěšném vytvoření můžete přistupovat ke studiu, které jste vytvořili, přes [ai.azure.com](https://ai.azure.com/)

Na jednom AI Foundry může být více projektů. Vytvořte projekt v AI Foundry jako přípravu.

Vytvořte Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Nasazení modelu Phi v Azure AI Foundry**

Klikněte na možnost Explore u projektu, vstupte do Model Catalog a vyberte Phi-3

Vyberte Phi-3-mini-4k-instruct

Klikněte na 'Deploy' pro nasazení modelu Phi-3-mini-4k-instruct

> [!NOTE]
>
> Při nasazení můžete vybrat výpočetní výkon

## **3. Playground Chat Phi v Azure AI Foundry**

Přejděte na stránku nasazení, vyberte Playground a začněte chatovat s Phi-3 v Azure AI Foundry

## **4. Nasazení modelu z Azure AI Foundry**

Pro nasazení modelu z Azure Model Catalog postupujte takto:

- Přihlaste se do Azure AI Foundry.
- Vyberte model, který chcete nasadit, z katalogu modelů Azure AI Foundry.
- Na stránce Detail modelu klikněte na Deploy a poté vyberte Serverless API s Azure AI Content Safety.
- Vyberte projekt, ve kterém chcete model nasadit. Pro použití Serverless API musí vaše pracovní prostředí patřit do regionu East US 2 nebo Sweden Central. Můžete si přizpůsobit název nasazení.
- V průvodci nasazením si přečtěte informace o cenách a podmínkách použití.
- Klikněte na Deploy. Počkejte, až bude nasazení připraveno a budete přesměrováni na stránku Deployments.
- Klikněte na Open in playground pro zahájení interakce s modelem.
- Můžete se vrátit na stránku Deployments, vybrat nasazení a zapsat si cílovou URL endpointu a Secret Key, které můžete použít pro volání nasazení a generování odpovědí.
- Detaily endpointu, URL a přístupové klíče najdete vždy v záložce Build pod sekcí Components v části Deployments.

> [!NOTE]
> Upozorňujeme, že pro provedení těchto kroků musí mít váš účet oprávnění role Azure AI Developer na Resource Group.

## **5. Použití Phi API v Azure AI Foundry**

Přes Postman můžete pomocí GET požadavku přistoupit na https://{Název vašeho projektu}.region.inference.ml.azure.com/swagger.json a v kombinaci s klíčem získat informace o dostupných rozhraních.

Velmi pohodlně tak získáte parametry požadavků i odpovědí.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.