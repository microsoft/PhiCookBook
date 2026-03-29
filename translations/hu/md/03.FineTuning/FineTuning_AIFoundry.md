# Fine-tuning Phi-3 a Microsoft Foundry-val

 Fedezzük fel, hogyan lehet finomhangolni a Microsoft Phi-3 Mini nyelvi modellt a Microsoft Foundry segítségével. A finomhangolás lehetővé teszi, hogy a Phi-3 Mini specifikus feladatokra legyen testreszabva, így még hatékonyabbá és kontextusérzékenyebbé válik.

## Szempontok

- **Képességek:** Mely modellek finomhangolhatók? Mire lehet finomhangolni az alapmodellt?
- **Költség:** Milyen árazási modell érvényes a finomhangolásra?
**Testreszabhatóság:** Mennyire módosíthatom az alapmodellt – és milyen módokon?
- **Kényelem:** Hogyan történik a finomhangolás valójában – kell egyedi kódot írnom? Kell saját számítási kapacitást hoznom?
- **Biztonság:** A finomhangolt modelleknél ismertek biztonsági kockázatok – vannak-e olyan védvonalak, amelyek megakadályozzák a nem kívánt károkat?

![AIFoundry Models](../../../../translated_images/hu/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Előkészületek a finomhangoláshoz

### Előfeltételek

> [!NOTE]
> A Phi-3 család modelljei esetén a pay-as-you-go alapon működő finomhangolási szolgáltatás csak az **East US 2** régiókban létrehozott hub-okkal érhető el.

- Egy Azure előfizetés. Ha nincs Azure előfizetésed, hozd létre egy [fizetős Azure fiókot](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go).

- Egy [AI Foundry projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Az Azure szerepkör alapú hozzáférés-vezérlés (Azure RBAC) engedélyezi a Microsoft Foundry műveleteinek elérését. Az ebben a cikkben szereplő lépések végrehajtásához az Azure AI fejlesztő szerepkört (__Azure AI Developer role__) kell hozzárendelni a felhasználói fiókodhoz az erőforráscsoportban.

### Előfizetés-szolgáltató regisztrációja

Ellenőrizd, hogy az előfizetés regisztrálva van-e a `Microsoft.Network` erőforrás szolgáltatónál.

1. Jelentkezz be az [Azure portálra](https://portal.azure.com).
1. A bal oldali menüből válaszd a **Subscriptions** menüpontot.
1. Válaszd ki a kívánt előfizetést.
1. A bal oldali menüben válaszd az **AI project settings** > **Resource providers** pontot.
1. Győződj meg róla, hogy a **Microsoft.Network** szerepel az erőforrás-szolgáltatók listájában. Ha nem, add hozzá.

### Adat-előkészítés

Készítsd elő az edző és validációs adataidat a modell finomhangolásához. Az edző és validációs adatállományok bemeneti és kimeneti példákat tartalmaznak arra vonatkozóan, hogy szeretnéd, hogy a modell hogyan működjön.

Győződj meg róla, hogy minden edző példád az elvárt formátumot követi az inferenciához. A modellek hatékony finomhangolásához biztosíts kiegyensúlyozott és változatos adatállományt.

Ez magában foglalja az adat-egyensúly fenntartását, különböző helyzetek bevonását és az edző adatok időszakos finomítását, hogy megfeleljenek a valós elvárásoknak, ami pontosabb és kiegyensúlyozottabb modellválaszokat eredményez.

Különböző modell típusok eltérő formátumú edző adatokat igényelnek.

### Chat Completion

Az általad használt edző és validációs adatokat **JSON Lines (JSONL)** formátumban kell megadni. A `Phi-3-mini-128k-instruct` modell finomhangolásához a beszélgetési formátumot kell használni, amelyet a Chat completion API használ.

### Példa fájlformátum

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

A támogatott fájltípus a JSON Lines. A fájlokat feltöltik az alapértelmezett adattárba és elérhetővé teszik a projektben.

## Phi-3 finomhangolása a Microsoft Foundry-val

A Microsoft Foundry lehetővé teszi, hogy a nagy nyelvi modelleket a saját adatkészleteidhez személyre szabhasd egy ún. finomhangolási folyamat segítségével. A finomhangolás jelentős értéket nyújt azáltal, hogy testreszabást és optimalizálást tesz lehetővé speciális feladatokra és alkalmazásokra. Ez jobb teljesítményt, költséghatékonyságot, csökkentett válaszidőt és személyre szabott eredményeket eredményez.

![Finetune AI Foundry](../../../../translated_images/hu/AIFoundryfinetune.193aaddce48d553c.webp)

### Új projekt létrehozása

1. Jelentkezz be a [Microsoft Foundry-ba](https://ai.azure.com).

1. Válaszd a **+New project** lehetőséget, hogy új projektet hozz létre a Microsoft Foundry-ban.

    ![FineTuneSelect](../../../../translated_images/hu/select-new-project.cd31c0404088d7a3.webp)

1. Hajtsd végre a következő lépéseket:

    - Projekt **Hub neve**. Egyedi értéknek kell lennie.
    - Válaszd ki a használni kívánt **Hub**-ot (szükség esetén hozz létre újat).

    ![FineTuneSelect](../../../../translated_images/hu/create-project.ca3b71298b90e420.webp)

1. Az új hub létrehozásához hajtsd végre a következőket:

    - Írd be a **Hub nevét**. Egyedi értéknek kell lennie.
    - Válaszd ki az Azure **Előfizetést**.
    - Válaszd ki a használni kívánt **Erőforrás csoportot** (szükség esetén hozz létre újat).
    - Válaszd ki a használni kívánt **Helyszínt**.
    - Válaszd ki a használni kívánt **Connect Azure AI Services**-t (szükség esetén hozz létre újat).
    - Válaszd a **Connect Azure AI Search**-nál a **Skip connecting** opciót.

    ![FineTuneSelect](../../../../translated_images/hu/create-hub.49e53d235e80779e.webp)

1. Kattints a **Tovább** gombra.
1. Válaszd a **Create a project** lehetőséget.

### Adat-előkészítés

A finomhangolás előtt gyűjtsd össze vagy hozd létre a feladatodhoz releváns adatállományt, például chat utasításokat, kérdés-válasz párokat vagy más szöveges adatokat. Tisztítsd és előfeldolgozd ezeket az adatokat zaj eltávolításával, hiányzó értékek kezelésével és a szöveg tokenizálásával.

### Phi-3 modellek finomhangolása a Microsoft Foundry-ban

> [!NOTE]
> A Phi-3 modellek finomhangolása jelenleg csak az East US 2 régióban található projektekben támogatott.

1. Válaszd ki a bal oldali fülön a **Model catalog** lehetőséget.

1. Írd be a keresősávba *phi-3* kifejezést, majd válassz ki egy phi-3 modellt.

    ![FineTuneSelect](../../../../translated_images/hu/select-model.60ef2d4a6a3cec57.webp)

1. Kattints a **Fine-tune** gombra.

    ![FineTuneSelect](../../../../translated_images/hu/select-finetune.a976213b543dd9d8.webp)

1. Írd be a **Finomhangolt modell nevét**.

    ![FineTuneSelect](../../../../translated_images/hu/finetune1.c2b39463f0d34148.webp)

1. Kattints a **Tovább** gombra.

1. Hajtsd végre a következőket:

    - Válaszd a **feladat típusát**: **Chat completion**.
    - Válaszd ki a használni kívánt **Edző adatokat**. Feltöltheted Microsoft Foundry adatán keresztül vagy a helyi környezetből.

    ![FineTuneSelect](../../../../translated_images/hu/finetune2.43cb099b1a94442d.webp)

1. Kattints a **Tovább** gombra.

1. Töltsd fel a használni kívánt **Validációs adatokat**, vagy válaszd az **Automatikus megosztás az edző adatokból** opciót.

    ![FineTuneSelect](../../../../translated_images/hu/finetune3.fd96121b67dcdd92.webp)

1. Kattints a **Tovább** gombra.

1. Végezd el a következőket:

    - Válaszd ki a kívánt **Batch size multipplicitás** értéket.
    - Válaszd ki a kívánt **Tanulási rátát**.
    - Válaszd ki a kívánt **Epoch-ok számát**.

    ![FineTuneSelect](../../../../translated_images/hu/finetune4.e18b80ffccb5834a.webp)

1. Kattints a **Submit** gombra a finomhangolási folyamat elindításához.

    ![FineTuneSelect](../../../../translated_images/hu/select-submit.0a3802d581bac271.webp)


1. Ha a modell finomhangolása befejeződött, az állapot **Completed** lesz, ahogy az alábbi képen látható. Ekkor telepítheted a modellt és használhatod a saját alkalmazásodban, a playgroundban vagy prompt flow-ban. További információért lásd a [Hogyan telepítsük a Phi-3 család kis nyelvi modelljeit Microsoft Foundry-val](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) című dokumentációt.

    ![FineTuneSelect](../../../../translated_images/hu/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Részletesebb információkért a Phi-3 finomhangolásáról kérjük látogasd meg a [Phi-3 modellek finomhangolása Microsoft Foundry-ban](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini) oldalt.

## Finomhangolt modellek törlése

Törölhetsz egy finomhangolt modellt a finomhangolási modell listából a [Microsoft Foundry](https://ai.azure.com) oldalán, vagy a modell részletei oldalról. Válaszd ki a törölni kívánt finomhangolt modellt a Fine-tuning oldalon, majd kattints a Törlés gombra.

> [!NOTE]
> Nem törölhetsz egyéni modellt, ha az már rendelkezik telepítéssel. Előbb a telepítést kell törölnöd, hogy az egyéni modell törölhető legyen.

## Költségek és kvóták

### Költség- és kvóta szempontok a Phi-3 modellek finomhangolásához szolgáltatásként

A Phi modellek, amelyeket szolgáltatásként finomhangolnak, Microsoft által kínált és a Microsoft Foundryba integrált megoldások. Az árakat megtalálod a modell [telepítésekor](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) vagy finomhangolásakor, a Pricing and terms fül alatt a telepítési varázslóban.

## Tartalomszűrés

Az pay-as-you-go alapon szolgáltatásként telepített modelleket az Azure AI Content Safety védi. Valós időben futó végpontokra telepítve lehetőség van ezt a funkciót kikapcsolni. Az Azure AI content safety engedélyezésekor mind a prompt, mind a completion átesik egy osztályozó modellekből álló együttesen, amely célja a káros tartalom felismerése és megakadályozása. A tartalomszűrő rendszer képes észlelni és fellépni bizonyos potenciálisan káros tartalomtípusok ellen mind a bemeneti promptokban, mind a kimeneti válaszokban. További információkért lásd az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering) dokumentációt.

**Finomhangolási beállítások**

Hyperparaméterek: Határozd meg a hyperparamétereket, mint például tanulási ráta, batch méret és epoc szám.

**Loss függvény**

Válassz a feladatodhoz megfelelő veszteségfüggvényt (pl. keresztentrópia).

**Optimalizáló**

Válassz egy optimalizálót (pl. Adam), amely a gradiens frissítéseket végzi a tanítás során.

**Finomhangolási folyamat**

- Betöltés: Töltsd be a Phi-3 Mini ellenőrzőpontját.
- Egyedi rétegek hozzáadása: Adj hozzá feladatspecifikus rétegeket (pl. osztályozó fejet chat utasításokhoz).

**Modell tanítása**
Finomhangold a modellt az előkészített adatállományoddal. Kövesd a tanítás menetét és szükség szerint módosítsd a hyperparamétereket.

**Értékelés és validáció**

Validációs halmaz: Oszd meg az adatokat tanító és validációs készletekre.

**Teljesítmény értékelése**

Használj metrikákat, például pontosság, F1-érték vagy perplexitás a modell értékeléséhez.

## Finomhangolt modell mentése

**Ellenőrzőpont**
Mentsd el a finomhangolt modell ellenőrzőpontját későbbi használatra.

## Telepítés

- Webszolgáltatásként telepítés: Telepítsd a finomhangolt modelledet webszerverként a Microsoft Foundry segítségével.
- Végpont tesztelése: Küldj teszt lekérdezéseket a telepített végpontra, hogy ellenőrizd működését.

## Iterálás és fejlesztés

Iterálás: Ha a teljesítmény nem kielégítő, módosítsd a hyperparamétereket, adj hozzá több adatot, vagy finomhangolj további epoch-okra.

## Monitorozás és finomítás

Folyamatosan figyeld a modell viselkedését és szükség szerint finomítsd.

## Testreszabás és bővítés

Egyedi feladatok: A Phi-3 Mini különböző feladatokra finomhangolható a chat utasításokon túl is. Fedezd fel az egyéb felhasználási lehetőségeket!
Kísérletezés: Próbálj ki különböző architektúrákat, rétegkombinációkat és technikákat a teljesítmény javítására.

> [!NOTE]
> A finomhangolás iteratív folyamat. Kísérletezz, tanulj és alakítsd a modelledet, hogy elérd a legjobb eredményeket a saját speciális feladatodra!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén profi, emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy félreértelmezésért, amely a fordítás használatából ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->