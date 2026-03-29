# **Microsoft Foundry használata az értékeléshez**

![aistudo](../../../../../translated_images/hu/AIFoundry.9e0b513e999a1c5a.webp)

Hogyan értékelheti generatív MI alkalmazását a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) segítségével. Legyen szó egyfordulós vagy többfordulós beszélgetések értékeléséről, a Microsoft Foundry eszközöket biztosít a modell teljesítményének és biztonságának értékeléséhez.

![aistudo](../../../../../translated_images/hu/AIPortfolio.69da59a8e1eaa70f.webp)

## Hogyan értékeljük a generatív MI alkalmazásokat Microsoft Foundry-val
Részletesebb útmutatásért lásd a [Microsoft Foundry dokumentációját](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Íme a kezdés lépései:

## Generatív MI modellek értékelése a Microsoft Foundry-ban

**Előfeltételek**

- Egy tesztadatkészlet CSV vagy JSON formátumban.
- Telepített generatív MI modell (például Phi-3, GPT 3.5, GPT 4 vagy Davinci modellek).
- Egy futtatási környezet egy számítási példánnyal az értékelés futtatásához.

## Beépített értékelési metrikák

A Microsoft Foundry lehetővé teszi egyfordulós és összetett, többfordulós beszélgetések értékelését.
A Retrieval Augmented Generation (RAG) helyzetekben, ahol a modellt meghatározott adatokra alapozzák, teljesítményét beépített értékelési metrikák segítségével meg lehet vizsgálni.
Ezenfelül általános egyfordulós kérdés-válasz helyzeteket is értékelhet (nem RAG).

## Értékelési futtatás létrehozása

A Microsoft Foundry felhasználói felületén navigáljon az Evaluate oldalra vagy a Prompt Flow oldalra.
Kövesse az értékelés létrehozási varázslót az értékelési futtatás beállításához. Adjon meg opcionális nevet az értékeléshez.
Válassza ki azt a forgatókönyvet, amely alkalmazása céljaihoz igazodik.
Válasszon egy vagy több értékelési metrikát a modell kimenetének értékeléséhez.

## Egyedi értékelési folyamat (opcionális)

Nagyobb rugalmasság érdekében létrehozhat egyedi értékelési folyamatot. Testreszabhatja az értékelési eljárást az Ön saját igényei szerint.

## Eredmények megtekintése

Az értékelés futtatása után naplózza, tekintse meg és elemezze a részletes értékelési metrikákat a Microsoft Foundry-ban. Szerezzen betekintést alkalmazása képességeibe és korlátaiba.



**Megjegyzés** A Microsoft Foundry jelenleg nyilvános előzetes verzióban van, ezért kísérletezésre és fejlesztési célokra használja. Éles munkaterheléshez fontolja meg más lehetőségek használatát. Tekintse meg a hivatalos [AI Foundry dokumentációt](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) további részletekért és lépésről lépésre szóló útmutatókért.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felmentés**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az adott nyelven tekintendő hiteles forrásnak. Kritikus információk esetén profi emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->