<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:43:38+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "hu"
}
-->
# **Építsd meg saját Visual Studio Code GitHub Copilot Chat-ed a Microsoft Phi-3 családdal**

Használtad már a workspace agentet a GitHub Copilot Chat-ben? Szeretnéd megalkotni a saját csapatod kódügynökét? Ez a gyakorlati labor arra törekszik, hogy az open source modellt kombinálva vállalati szintű kódüzleti ügynököt építsen.

## **Alapok**

### **Miért válaszd a Microsoft Phi-3-at**

A Phi-3 egy család, amely tartalmazza a phi-3-mini, phi-3-small és phi-3-medium modelleket, különböző tanítási paraméterekkel szöveg generálásra, párbeszéd befejezésre és kód generálásra. Emellett létezik a phi-3-vision, amely a Vision-re épül. Ez ideális vállalatok vagy különböző csapatok számára offline generatív AI megoldások létrehozásához.

Ajánlott elolvasni ezt a linket [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

A GitHub Copilot Chat bővítmény egy csevegőfelületet biztosít, amely lehetővé teszi, hogy közvetlenül a VS Code-on belül kommunikálj a GitHub Copilot-tal, és kódolással kapcsolatos kérdésekre kapj válaszokat anélkül, hogy dokumentációt kellene böngészned vagy online fórumokat keresgélned.

A Copilot Chat használhat szintaxiskiemelést, behúzást és egyéb formázási elemeket, hogy átláthatóbbá tegye a generált választ. A felhasználó kérdésének típusától függően az eredmény tartalmazhat hivatkozásokat a Copilot által a válasz generálásához használt kontextusra, például forráskód fájlokra vagy dokumentációra, illetve gombokat a VS Code funkcióinak eléréséhez.

- A Copilot Chat beépül a fejlesztői munkafolyamatodba, és ott segít, ahol szükséged van rá:

- Indíts inline csevegést közvetlenül a szerkesztőből vagy a terminálból, hogy segítséget kapj kódolás közben

- Használd a Chat nézetet, hogy mindig legyen egy AI asszisztensed az oldaladon

- Indíts Quick Chat-et, hogy gyors kérdést tegyél fel, és folytathasd a munkát

A GitHub Copilot Chat különböző helyzetekben használható, például:

- Kódolási kérdések megválaszolására, hogyan lehet a legjobban megoldani egy problémát

- Mások kódjának magyarázatára és fejlesztési javaslatok adására

- Kódhibák javításának javaslatára

- Egységtesztes esetek generálására

- Kód dokumentáció generálására

Ajánlott elolvasni ezt a linket [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Az **@workspace** hivatkozás a Copilot Chat-ben lehetővé teszi, hogy az egész kódbázisodra vonatkozó kérdéseket tegyél fel. A kérdés alapján a Copilot intelligensen lekéri a releváns fájlokat és szimbólumokat, amelyeket aztán hivatkozásként és kódpéldaként használ a válaszában.

A kérdés megválaszolásához az **@workspace** ugyanazokat a forrásokat vizsgálja át, amelyeket egy fejlesztő is használna a VS Code-ban történő kódbázis navigáció során:

- Az összes fájl a workspace-ben, kivéve azokat, amelyeket a .gitignore fájl figyelmen kívül hagy

- Könyvtárstruktúra, beleértve a beágyazott mappákat és fájlneveket

- A GitHub kódkereső indexe, ha a workspace egy GitHub tároló és a kódkereső indexelte

- Szimbólumok és definíciók a workspace-ben

- Az aktív szerkesztőben kijelölt vagy látható szöveg

Megjegyzés: a .gitignore figyelmen kívül hagyása megtörténik, ha meg van nyitva egy fájl vagy szöveg van kijelölve egy figyelmen kívül hagyott fájlban.

Ajánlott elolvasni ezt a linket [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Tudj meg többet erről a laborról**

A GitHub Copilot jelentősen javította a vállalatok programozási hatékonyságát, és minden vállalat szeretné testreszabni a GitHub Copilot releváns funkcióit. Sok vállalat testreszabott bővítményeket készített, amelyek hasonlóak a GitHub Copilot-hoz, saját üzleti forgatókönyveik és open source modelljeik alapján. A vállalatok számára a testreszabott bővítmények könnyebben kezelhetők, de ez befolyásolja a felhasználói élményt is. Végül is a GitHub Copilot erősebb funkciókkal rendelkezik az általános helyzetek és a szakmaiság kezelésében. Ha az élmény következetes maradhat, jobb lenne a vállalat saját bővítményét testreszabni. A GitHub Copilot Chat releváns API-kat biztosít a vállalatok számára a Chat élmény bővítéséhez. A következetes élmény fenntartása és a testreszabott funkciók jobb felhasználói élményt nyújtanak.

Ez a labor főként a Phi-3 modellt használja, amelyet helyi NPU-val és Azure hibriddel kombinálva épít egy egyedi ügynököt a GitHub Copilot Chat-ben ***@PHI3***, hogy segítsen a vállalati fejlesztőknek kód generálásában***(@PHI3 /gen)*** és képek alapján történő kód generálásban ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.hu.png)

### ***Megjegyzés:***

Ez a labor jelenleg az Intel CPU és Apple Silicon AIPC-n valósul meg. A Qualcomm NPU verzióját továbbra is fejlesztjük.

## **Labor**

| Név | Leírás | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Telepítések(✅) | Kapcsolódó környezetek és telepítőeszközök konfigurálása és telepítése | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Prompt flow futtatása Phi-3-mini-vel (✅) | AIPC / Apple Silicon kombinálásával, helyi NPU használatával kód generálás létrehozása Phi-3-mini segítségével | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Phi-3-vision telepítése az Azure Machine Learning Service-re(✅) | Kód generálása az Azure Machine Learning Service Model Catalog - Phi-3-vision kép telepítésével | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - @phi-3 ügynök létrehozása a GitHub Copilot Chat-ben(✅)  | Egyedi Phi-3 ügynök létrehozása a GitHub Copilot Chat-ben kód generálás, grafikon generálás, RAG stb. elvégzéséhez | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Minta kód (✅)  | Minta kód letöltése | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Források**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Tudj meg többet a GitHub Copilot-ról [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Tudj meg többet a GitHub Copilot Chat-ről [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Tudj meg többet a GitHub Copilot Chat API-ról [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Tudj meg többet az Azure AI Foundry-ról [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Tudj meg többet az Azure AI Foundry Model Catalog-járól [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.