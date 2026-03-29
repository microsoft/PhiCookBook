# **Použití Phi-3 v Microsoft Foundry**

S rozvojem Generativní AI doufáme použít sjednocenou platformu pro správu různých LLM a SLM, integraci podnikových dat, operace ladění/RAG a hodnocení různých podnikových procesů po integraci LLM a SLM, atd., aby bylo možné lépe implementovat chytré aplikace generativní AI. [Microsoft Foundry](https://ai.azure.com) je generativní AI aplikační platforma na podnikové úrovni.

![aistudo](../../../../translated_images/cs/aifoundry_home.f28a8127c96c7d93.webp)

S Microsoft Foundry můžete hodnotit odpovědi velkých jazykových modelů (LLM) a orchestraci komponent aplikace promptů pomocí prompt flow pro lepší výkon. Platforma usnadňuje škálovatelnost při transformaci konceptů do plnohodnotné produkce s lehkostí. Kontinuální monitorování a zdokonalování podporují dlouhodobý úspěch.

Můžeme rychle nasadit model Phi-3 na Microsoft Foundry pomocí jednoduchých kroků a poté použít Microsoft Foundry k dokončení souvisejících úloh jako Playground/Chat, ladění, hodnocení a dalších.

## **1. Příprava**

Pokud již máte na svém počítači nainstalovaný [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), použití této šablony je tak jednoduché jako spuštění tohoto příkazu v novém adresáři.

## Ruční vytvoření

Vytvoření projektu a hubu v Microsoft Foundry je skvělý způsob, jak organizovat a řídit vaši AI práci. Zde je krok za krokem průvodce, jak začít:

### Vytvoření projektu v Microsoft Foundry

1. **Přejděte do Microsoft Foundry**: Přihlaste se do portálu Microsoft Foundry.
2. **Vytvoření projektu**:
   - Pokud jste v projektu, vyberte v levém horním rohu stránky "Microsoft Foundry" pro návrat na domovskou stránku.
   - Vyberte "+ Vytvořit projekt".
   - Zadejte název projektu.
   - Pokud máte hub, bude vybrán automaticky. Pokud máte přístup k více hubům, můžete z rozevíracího seznamu vybrat jiný. Pokud chcete vytvořit nový hub, vyberte "Vytvořit nový hub" a zadejte název.
   - Vyberte "Vytvořit".

### Vytvoření hubu v Microsoft Foundry

1. **Přejděte do Microsoft Foundry**: Přihlaste se pomocí svého Azure účtu.
2. **Vytvoření hubu**:
   - Vyberte Správní centrum z levého menu.
   - Vyberte "Všechny zdroje", poté šipku dolů vedle "+ Nový projekt" a vyberte "+ Nový hub".
   - V dialogovém okně "Vytvořit nový hub" zadejte název hubu (např. contoso-hub) a upravte další pole dle potřeby.
   - Vyberte "Další", zkontrolujte informace a poté vyberte "Vytvořit".

Podrobnější pokyny naleznete v oficiální [Microsoft dokumentaci](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po úspěšném vytvoření můžete přistoupit ke studiu, které jste vytvořili, přes [ai.azure.com](https://ai.azure.com/)

Na jedné AI Foundry může být více projektů. V AI Foundry vytvořte projekt pro přípravu.

Vytvořte Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Nasazení modelu Phi v Microsoft Foundry**

Klikněte na možnost Prozkoumat projektu, vstupte do Katalogu modelů a vyberte Phi-3.

Vyberte Phi-3-mini-4k-instruct.

Klikněte na 'Nasadit' pro nasazení modelu Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Při nasazování můžete vybrat výpočetní výkon.

## **3. Playground Chat Phi v Microsoft Foundry**

Přejděte na stránku nasazení, vyberte Playground a chatujte s Phi-3 v Microsoft Foundry.

## **4. Nasazení modelu z Microsoft Foundry**

Pro nasazení modelu z Azure Model Catalog můžete provést tyto kroky:

- Přihlaste se do Microsoft Foundry.
- Vyberte model, který chcete nasadit, z katalogu modelů Microsoft Foundry.
- Na stránce Detail modelu vyberte Nasadit a poté zvolte Serverless API s Azure AI Content Safety.
- Vyberte projekt, ve kterém chcete modely nasadit. Pro využití nabídky Serverless API musí vaše pracovní prostor patřit do oblasti East US 2 nebo Sweden Central. Můžete upravit název nasazení.
- V průvodci nasazením vyberte Ceny a podmínky, abyste se seznámili s cenami a podmínkami užití.
- Vyberte Nasadit. Počkejte, až bude nasazení připraveno a budete přesměrováni na stránku Nasazení.
- Vyberte Otevřít v playgroundu pro zahájení interakce s modelem.
- Můžete se vrátit na stránku Nasazení, vybrat nasazení a poznamenat si cílovou URL koncového bodu a Tajný klíč, které můžete použít pro volání nasazení a generování výstupů.
- Detaily koncového bodu, URL a přístupové klíče můžete kdykoli najít tak, že přejdete na záložku Build a vyberete Nasazení v části Komponenty.

> [!NOTE]
> Upozorňujeme, že váš účet musí mít roli Azure AI Developer s oprávněními do Skupiny zdrojů, aby bylo možné tyto kroky provést.

## **5. Použití Phi API v Microsoft Foundry**

Můžete přistoupit na https://{Název vašeho projektu}.region.inference.ml.azure.com/swagger.json přes Postman GET a kombinovat to s klíčem pro seznámení se s poskytovanými rozhraními.

Velmi pohodlně získáte parametry požadavku i odpovědi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za případné nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->