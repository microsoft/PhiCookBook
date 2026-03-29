# **Építsd meg a saját Visual Studio Code GitHub Copilot Chat-edet a Microsoft Phi-3 családdal**

Használtad már a workspace agentet a GitHub Copilot Chat-ben? Szeretnél saját csapatod kódügynökét létrehozni? Ez a gyakorlati labor arra törekszik, hogy az open source modellt kombinálva egy vállalati szintű kódüzleti ügynököt építsen.

## **Alapok**

### **Miért válaszd a Microsoft Phi-3-at**

A Phi-3 egy család sorozat, amely tartalmazza a phi-3-mini, phi-3-small és phi-3-medium modelleket a különböző tanítási paraméterek alapján szöveggenerálásra, párbeszédfolyamat-kiegészítésre és kódgenerálásra. Van továbbá a Vision alapú phi-3-vision is. Ez alkalmas vállalatok vagy különböző csapatok számára offline generatív AI megoldások létrehozására.

Ajánlott elolvasni ezt a linket [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

A GitHub Copilot Chat kiterjesztés egy csevegőfelületet biztosít, amely lehetővé teszi, hogy interakcióba lépj a GitHub Copilot-tal, és kódolással kapcsolatos kérdésekre közvetlenül a VS Code-on belül kapsz választ, anélkül, hogy dokumentációt kellene böngészned vagy online fórumokat keresned.

A Copilot Chat használhat szintaxiskiemelést, behúzást és más formázási lehetőségeket, hogy tisztábbá tegye a generált választ. A felhasználó kérdésétől függően a válasz tartalmazhat hivatkozásokat a kontextusra, amelyet a Copilot a választ generálásához felhasznált, például forráskód fájlokra vagy dokumentációra, illetve gombokat a VS Code funkcióinak eléréséhez.

- A Copilot Chat integrálódik a fejlesztői munkafolyamatodba, és ott segít, ahol szükséged van rá:
  
- Indíts inline csevegést közvetlenül a szerkesztőből vagy terminálból, ha kódolás közben segítségre van szükséged

- Használd a Chat nézetet, hogy bármikor legyen egy AI asszisztensed a segítségre

- Indíts Quick Chat-et, hogy gyors kérdést tegyél fel és folytathasd a munkádat

A GitHub Copilot Chat különböző esetekben használható, mint például:

- Kódolási kérdések megválaszolása a legjobb megoldásokról

- Mások kódjának magyarázata és javaslatok fejlesztésre

- Kód javításainak javaslata

- Egységteszt esetek generálása

- Kód dokumentáció generálása

Ajánlott elolvasni ezt a linket [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

A **@workspace**-re való hivatkozás a Copilot Chat-ben lehetővé teszi, hogy az egész kódalapodra vonatkozó kérdéseket tegyél fel. A kérdés alapján a Copilot intelligensen lekéri a releváns fájlokat és szimbólumokat, amelyeket aztán válaszában linkek és kódpéldák formájában említ.

A kérdés megválaszolásához a **@workspace** ugyanazokat a forrásokat használja, amelyeket egy fejlesztő használna a VS Code kódalap navigálásához:

- Az összes fájl a workspace-ben, kivéve azokat, amelyeket egy .gitignore fájl figyelmen kívül hagy

- Könyvtárszerkezet beágyazott mappákkal és fájlnevekkel

- A GitHub kódkutató indexe, ha a workspace egy GitHub tároló és kódkeresés által indexelt

- Szimbólumok és definíciók a workspace-ben

- Az aktuálisan kijelölt vagy látható szöveg az aktív szerkesztőben

Megjegyzés: .gitignore figyelmen kívül hagyható, ha egy fájl nyitva van vagy szöveg van kijelölve egy figyelmen kívül hagyott fájlban.

Ajánlott elolvasni ezt a linket [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Tudj meg többet erről a laborról**

A GitHub Copilot jelentősen javította a vállalatok programozási hatékonyságát, és minden vállalat szeretné testreszabni a GitHub Copilot releváns funkcióit. Sok vállalat testreszabott bővítményeket készített, amelyek hasonlóak a GitHub Copilot-hoz, saját üzleti forgatókönyveik és open source modelljeik alapján. A vállalatok számára a testreszabott bővítmények könnyebben kezelhetők, de ez hatással van a felhasználói élményre is. A GitHub Copilot erősebb funkciókkal rendelkezik a általános helyzetek és a szakmaiság kezelésében. Ha az élmény következetes marad, jobb testreszabni a vállalat saját bővítményét. A GitHub Copilot Chat releváns API-kat biztosít a vállalatok számára a Chat élmény bővítéséhez. A következetes élmény fenntartása és a testreszabott funkciók jobb felhasználói élményt biztosítanak.

Ez a labor főként a Phi-3 modellt használja a helyi NPU és Azure hibrid kombinációjával, hogy egy egyedi Ügynököt építsen a GitHub Copilot Chat-ben ***@PHI3*** néven, amely segíti a vállalati fejlesztőket a kódgenerálásban***(@PHI3 /gen)*** és kép alapján történő kódgenerálásban ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/hu/cover.1017ebc9a7c46d09.webp)

### ***Megjegyzés:*** 

Ez a labor jelenleg Intel CPU és Apple Silicon AIPC-n fut. A Qualcomm NPU verzióját továbbra is frissítjük.


## **Labor**

| Név | Leírás | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Telepítések(✅) | Kapcsolódó környezetek és telepítési eszközök konfigurálása és telepítése | [Ugrás](./HOL/AIPC/01.Installations.md) |[Ugrás](./HOL/Apple/01.Installations.md) |
| Lab1 - Prompt folyam futtatása Phi-3-mini-vel (✅) | Az AIPC / Apple Silicon helyi NPU-ját használva Phi-3-mini segítségével kódgenerálás létrehozása | [Ugrás](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Ugrás](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Phi-3-vision telepítése az Azure Machine Learning Service-en (✅) | Kódgenerálás az Azure Machine Learning Service Model Katalógusának - Phi-3-vision kép telepítésével | [Ugrás](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Ugrás](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - @phi-3 ügynök létrehozása GitHub Copilot Chat-ben (✅)  | Egyedi Phi-3 ügynök létrehozása GitHub Copilot Chat-ben kódgenerálás, gráfgenerálás, RAG stb. elvégzéséhez | [Ugrás](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Ugrás](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Minta kód (✅)  | Minta kód letöltése | [Ugrás](../../../../../../../code/07.Lab/01/AIPC) | [Ugrás](../../../../../../../code/07.Lab/01/Apple) |


## **Források**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Tudj meg többet a GitHub Copilot-ról [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Tudj meg többet a GitHub Copilot Chat-ről [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Tudj meg többet a GitHub Copilot Chat API-ról [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Tudj meg többet a Microsoft Foundry-ról [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Tudj meg többet a Microsoft Foundry Model Katalógusáról [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával fordítottuk le. Bár pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekinthető hiteles forrásnak. Kritikus információk esetén szakképzett emberi fordítás igénybevétele javasolt. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy helytelen értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->