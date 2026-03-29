# **Phi-3 használata a Microsoft Foundry-ban**

A generatív MI fejlődésével arra törekszünk, hogy egy egységes platformot használjunk különböző LLM és SLM, vállalati adatintegráció, finomhangolás/RAG műveletek és az LLM és SLM integrálása utáni különböző vállalati üzletek értékelése kezelésére, hogy a generatív MI Smart alkalmazások jobban megvalósulhassanak. A [Microsoft Foundry](https://ai.azure.com) vállalati szintű generatív MI alkalmazásplatform.

![aistudo](../../../../translated_images/hu/aifoundry_home.f28a8127c96c7d93.webp)

A Microsoft Foundry segítségével kiértékelhetjük a nagy nyelvi modell (LLM) válaszait, és prompt flow-val szervezhetjük az utasítás alkalmazás elemeit a jobb teljesítmény érdekében. A platform megkönnyíti a koncepcióbizonyítások átalakítását teljes értékű gyártássá skálázhatósággal. A folyamatos felügyelet és finomítás a hosszú távú sikert támogatja.

Egyszerű lépésekkel gyorsan telepíthetjük a Phi-3 modellt a Microsoft Foundry-ban, majd a Microsoft Foundry segítségével készíthetjük el a Phi-3-hoz kapcsolódó Playground/Chat, finomhangolás, értékelés és más kapcsolódó munkálatokat.

## **1. Előkészület**

Ha már telepítve van a [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) a gépeden, ennek a sablonnak a használata olyan egyszerű, mint egy új mappában futtatni ezt a parancsot.

## Kézi létrehozás

Microsoft Foundry projekt és hub létrehozása nagyszerű módja az MI munkáid rendszerezésének és kezelésének. Íme egy lépésről lépésre útmutató a kezdéshez:

### Projekt létrehozása a Microsoft Foundry-ban

1. **Lépj be a Microsoft Foundry-ba**: Jelentkezz be a Microsoft Foundry portálra.
2. **Projekt létrehozása**:
   - Ha már egy projektben vagy, válaszd a bal felső sarokban a "Microsoft Foundry" lehetőséget, hogy visszajuss a Kezdőlapra.
   - Válaszd a "+ Projekt létrehozása" lehetőséget.
   - Add meg a projekt nevét.
   - Ha van hubod, az lesz az alapértelmezett választás. Ha több hubhoz is van hozzáférésed, a legördülőből választhatsz másikat. Ha új hubot szeretnél létrehozni, válaszd a "Új hub létrehozása" opciót, és adj meg nevet.
   - Válaszd a "Létrehozás" gombot.

### Hub létrehozása a Microsoft Foundry-ban

1. **Lépj be a Microsoft Foundry-ba**: Jelentkezz be Azure fiókoddal.
2. **Hub létrehozása**:
   - Válaszd a bal oldali menüből a Kezelőközpontot.
   - Válaszd az „Összes erőforrás” opciót, majd a "+ Új projekt" melletti lefelé mutató nyilat, és válassz "+ Új hub" lehetőséget.
   - A "Új hub létrehozása" párbeszédpanelen adj meg egy nevet a hubodnak (például contoso-hub), és módosítsd a többi mezőt igény szerint.
   - Válaszd a "Tovább" gombot, ellenőrizd az adatokat, majd válaszd a "Létrehozás" gombot.

Részletesebb útmutatóért lásd a hivatalos [Microsoft dokumentációt](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Sikeres létrehozás után a létrehozott stúdió elérhető a [ai.azure.com](https://ai.azure.com/) címen keresztül.

Egy AI Foundry-n belül több projekt is lehet. Készíts projektet az AI Foundry-ban a felkészüléshez.

Hozz létre Microsoft Foundry [QuickStartokat](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Phi modell telepítése a Microsoft Foundry-ban**

Kattints a projekt „Explore” (Felfedezés) opciójára a Modellkatalógusba lépéshez, majd válaszd ki a Phi-3 modellt.

Válaszd a Phi-3-mini-4k-instruct modellt.

Kattints a 'Deploy' gombra a Phi-3-mini-4k-instruct modell telepítéséhez.

> [!NOTE]
>
> A telepítés során választhatsz számítási kapacitást.

## **3. Playground Chat Phi használata a Microsoft Foundry-ban**

Lépj a telepítési oldalra, válaszd a Playground opciót, és beszélgess a Microsoft Foundry Phi-3 modelljével.

## **4. Modell telepítése a Microsoft Foundry-ból**

Egy modellt az Azure Modellkatalógusból a következő lépésekkel telepíthetsz:

- Jelentkezz be a Microsoft Foundry-ba.
- Válaszd ki a Microsoft Foundry modellkatalógusából azt a modellt, amelyet telepíteni szeretnél.
- A modell Adatok oldalán válaszd a Telepítés opciót, majd válaszd a Serverless API with Azure AI Content Safety lehetőséget.
- Válaszd ki azt a projektet, amelybe telepíteni szeretnéd a modelleket. A Serverless API használatához a munkaterületednek az East US 2 vagy Sweden Central régióhoz kell tartoznia. A telepítés nevét testreszabhatod.
- A telepítési varázslóban válaszd az Árazási és feltételek lehetőséget, hogy megismerd az árképzést és a használati feltételeket.
- Válaszd a Telepítés gombot. Várj, amíg a telepítés elkészül és átirányítanak a Telepítések oldalra.
- Válaszd az "Open in playground" opciót, hogy elkezdhesd a modellel való interakciót.
- Visszatérhetsz a Telepítések oldalra, kiválaszthatod a telepítést, és megtekintheted a végpont „Target URL” címét és a titkos kulcsot, amelyet a híváshoz és kimenetek generálásához használhatsz.
- Az endpoint részleteit, URL-jét és hozzáférési kulcsait mindig megtalálod a Build fülre navigálva, majd a Components szekcióból a Telepítések kiválasztásával.

> [!NOTE]
> Kérjük, vedd figyelembe, hogy a fiókodnak rendelkeznie kell az Azure AI Fejlesztő szerepkör jogosultsággal az adott Erőforráscsoporton a műveletek végrehajtásához.

## **5. Phi API használata a Microsoft Foundry-ban**

A https://{A projekt neve}.region.inference.ml.azure.com/swagger.json címhez hozzáférhetsz Postman GET kéréssel, és összevonhatod a kulccsal, hogy megismerd a biztosított interfészeket.

Nagyon kényelmesen megkaphatod a kérés paramétereit, valamint a válasz paramétereit is.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekinthető hivatalos forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->