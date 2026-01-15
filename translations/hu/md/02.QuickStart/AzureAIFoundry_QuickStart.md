<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:27:02+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "hu"
}
-->
# **Phi-3 használata az Azure AI Foundry-ban**

A generatív MI fejlődésével arra törekszünk, hogy egy egységes platformon kezeljük a különböző LLM és SLM modelleket, vállalati adatintegrációt, finomhangolást/RAG műveleteket, valamint az LLM és SLM integrálása utáni különböző vállalati üzletek értékelését, hogy a generatív MI okos alkalmazásai hatékonyabban valósulhassanak meg. Az [Azure AI Foundry](https://ai.azure.com) egy vállalati szintű generatív MI alkalmazásplatform.

![aistudo](../../../../translated_images/hu/aifoundry_home.f28a8127c96c7d93.png)

Az Azure AI Foundry segítségével értékelhetjük a nagy nyelvi modellek (LLM) válaszait, és prompt flow-val irányíthatjuk a prompt alkalmazás komponenseit a jobb teljesítmény érdekében. A platform támogatja a skálázhatóságot, így a koncepcióbizonyításokat könnyedén alakíthatjuk teljes értékű termelési környezetté. A folyamatos monitorozás és finomhangolás hosszú távú sikert biztosít.

Gyorsan telepíthetjük a Phi-3 modellt az Azure AI Foundry-ban néhány egyszerű lépésben, majd az Azure AI Foundry segítségével végezhetjük el a Phi-3-hoz kapcsolódó Playground/Chat, finomhangolás, értékelés és egyéb feladatokat.

## **1. Előkészületek**

Ha már telepítve van a gépeden az [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), akkor ennek a sablonnak a használata annyit jelent, hogy egy új mappában lefuttatod ezt a parancsot.

## Kézi létrehozás

Egy Microsoft Azure AI Foundry projekt és hub létrehozása nagyszerű módja annak, hogy rendszerezd és kezeld az MI munkáidat. Íme egy lépésről lépésre útmutató a kezdéshez:

### Projekt létrehozása az Azure AI Foundry-ban

1. **Lépj be az Azure AI Foundry-ba**: Jelentkezz be az Azure AI Foundry portálra.
2. **Projekt létrehozása**:
   - Ha már egy projektben vagy, válaszd a bal felső sarokban az „Azure AI Foundry” opciót a kezdőlapra való visszatéréshez.
   - Kattints a „+ Create project” gombra.
   - Add meg a projekt nevét.
   - Ha van hubod, az alapértelmezettként lesz kiválasztva. Ha több hubhoz is hozzáférsz, a legördülő menüből választhatsz másikat. Ha új hubot szeretnél létrehozni, válaszd a „Create new hub” opciót, és adj meg egy nevet.
   - Kattints a „Create” gombra.

### Hub létrehozása az Azure AI Foundry-ban

1. **Lépj be az Azure AI Foundry-ba**: Jelentkezz be az Azure fiókoddal.
2. **Hub létrehozása**:
   - Válaszd a bal oldali menüből a Management centert.
   - Kattints az „All resources” menüpontra, majd a „+ New project” melletti lefelé mutató nyílra, és válaszd a „+ New hub” opciót.
   - A „Create a new hub” ablakban add meg a hub nevét (pl. contoso-hub), és módosítsd a többi mezőt igény szerint.
   - Kattints a „Next”-re, ellenőrizd az adatokat, majd válaszd a „Create” gombot.

Részletesebb útmutatóért tekintsd meg a hivatalos [Microsoft dokumentációt](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

A sikeres létrehozás után az általad létrehozott stúdiót az [ai.azure.com](https://ai.azure.com/) oldalon érheted el.

Egy AI Foundry-n belül több projekt is lehet. Hozz létre egy projektet az AI Foundry-ban a felkészüléshez.

Hozz létre Azure AI Foundry [QuickStartokat](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Phi modell telepítése az Azure AI Foundry-ban**

Kattints a projekt Explore opciójára, hogy belépj a Model Catalog-ba, majd válaszd ki a Phi-3 modellt.

Válaszd ki a Phi-3-mini-4k-instruct modellt.

Kattints a 'Deploy' gombra a Phi-3-mini-4k-instruct modell telepítéséhez.

> [!NOTE]
>
> A telepítés során választhatsz számítási kapacitást is.

## **3. Playground Chat Phi az Azure AI Foundry-ban**

Lépj a telepítési oldalra, válaszd a Playground opciót, és beszélgess az Azure AI Foundry Phi-3 modelljével.

## **4. Modell telepítése az Azure AI Foundry-ból**

Modell telepítéséhez az Azure Model Catalogból kövesd az alábbi lépéseket:

- Jelentkezz be az Azure AI Foundry-ba.
- Válaszd ki a telepíteni kívánt modellt az Azure AI Foundry modell katalógusából.
- A modell Részletek oldalán válaszd a Deploy opciót, majd a Serverless API with Azure AI Content Safety-t.
- Válaszd ki azt a projektet, amelybe telepíteni szeretnéd a modellt. A Serverless API használatához a munkaterületnek az East US 2 vagy Sweden Central régióban kell lennie. A Deployment nevet testre szabhatod.
- A telepítési varázslóban válaszd a Pricing and terms opciót, hogy megismerd az árakat és a használati feltételeket.
- Kattints a Deploy gombra. Várj, amíg a telepítés elkészül, és átirányítanak a Deployments oldalra.
- Válaszd az Open in playground opciót, hogy elkezdhess interakciót a modellel.
- Visszatérhetsz a Deployments oldalra, kiválaszthatod a telepítést, és megtekintheted az endpoint Target URL-jét és a Secret Key-t, amelyeket a telepítés hívásához és válaszok generálásához használhatsz.
- Az endpoint részleteit, URL-jét és hozzáférési kulcsait mindig megtalálod a Build fülön, a Components szekcióban a Deployments menüpont alatt.

> [!NOTE]
> Kérjük, vedd figyelembe, hogy a fenti lépések végrehajtásához az Azure AI Developer szerepkör jogosultságokkal kell rendelkezned az adott Resource Groupon.

## **5. Phi API használata az Azure AI Foundry-ban**

A https://{Your project name}.region.inference.ml.azure.com/swagger.json címet elérheted Postman GET kéréssel, és a Key kombinálásával megismerheted a rendelkezésre álló interfészeket.

Nagyon kényelmesen megkaphatod a kérés paramétereit, valamint a válasz paramétereit is.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.